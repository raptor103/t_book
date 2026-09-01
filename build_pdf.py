#!/usr/bin/env python3
"""
Pure-Python PDF build for "How a Tesla Works".

Concatenates every markdown file under book/ in sort order and renders a
single A4 PDF with a generated table of contents. Uses markdown-it for the
markdown and PyMuPDF's Story engine for layout, so no LaTeX / pandoc is
required.

    pip install pymupdf markdown-it-py
    python build_pdf.py

Output: out/how-a-tesla-works.pdf

The canonical build (pandoc + xelatex) lives in build.sh; this script is the
dependency-light fallback that runs anywhere Python does. Monospace ASCII
diagrams are kept <=76 chars wide, so at 8pt they never overflow A4 margins.

The book is laid out as one continuous flow, so text fills every page. The
one exception is a diagram that would land badly -- cut across a page
boundary, or parted from the lead-in that introduces it. That page is ended
early, just above the lead-in, and the pair moves down together. The gap
this leaves is never worse than the diagram's own height, unlike a hard page
break, which strands however much of the page was still empty.

PyMuPDF cannot draw footers, so page numbers are stamped on afterwards. The
title page is left unnumbered, and every other page prints its own PDF page
number, so the printed folio matches the bookmark targets.
"""
import glob
import io
import itertools
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(ROOT, "book")
OUT_DIR = os.path.join(ROOT, "out")
OUT_PDF = os.path.join(OUT_DIR, "how-a-tesla-works.pdf")

PAPER = "A4"
BORDERS = (36, 36, -36, -36)
TOC_LEVEL = 2

# Diagram height is worked out from these rather than measured, so they must
# stay the numbers the stylesheet actually uses -- hence the interpolation.
PRE_PT = 8
PRE_SPACING = 1.15
PRE_LINE_PT = PRE_PT * PRE_SPACING

CSS = f"""
body {{ font-family: serif; font-size: 11pt; line-height: 1.45; }}
h1 {{ font-family: sans-serif; font-size: 20pt; margin-top: 18pt; }}
h2 {{ font-family: sans-serif; font-size: 15pt; margin-top: 14pt; }}
h3 {{ font-family: sans-serif; font-size: 12pt; }}
p  {{ margin: 6pt 0; }}
pre, code {{ font-family: monospace; font-size: {PRE_PT}pt; }}
pre {{ white-space: pre; line-height: {PRE_SPACING}; margin: 6pt 0; }}
table {{ border-collapse: collapse; font-size: 10pt; }}
th, td {{ border: 1px solid #999; padding: 3pt 6pt; }}
hr {{ border: none; border-top: 1px solid #ccc; }}
"""

# Page-number footer. Borders stop body text 36pt above the page foot; the
# folio sits in that margin.
FOLIO_FONT = "helv"
FOLIO_SIZE = 9
FOLIO_COLOR = (0.45, 0.45, 0.45)
FOLIO_BASELINE_FROM_BOTTOM = 22
SKIP_PAGES = 1  # title page carries no number

# A placed diagram shorter than this much of its full height was cut off.
SPLIT_SLACK = 0.5

# One trim is added per pass, so this only has to exceed the diagram count.
MAX_TRIM_PASSES = 200


def source_headings(combined):
    """Heading levels and text, straight from the markdown, in book order."""
    out, inside = [], False
    for ln in combined.split("\n"):
        if ln.startswith("```"):
            inside = not inside
            continue
        if inside:
            continue
        m = re.match(r"^(#{1,2}) +(\S.*)$", ln)
        if m:
            out.append((len(m.group(1)), m.group(2).strip()))
    return out


# The base-14 fonts PyMuPDF draws with cannot encode these, and silently
# substitute a middle dot. The contents page is the only place we draw text
# ourselves, so fold them down to ASCII here.
_TR = {"—": "-", "–": "-", "‘": "'", "’": "'",
       "“": '"', "”": '"', "…": "..."}


def _ascii(s):
    for k, v in _TR.items():
        s = s.replace(k, v)
    return s


def prepend_toc(path, headings=None):
    """Insert a printed, clickable Contents section after the title page.

    The render produces a bookmark outline but no visible contents, so this
    reads that outline, lays it out as pages, inserts them, and adds a GoTo
    link over every line. Line count does not depend on the page numbers
    printed, so one pass is enough -- but the targets must be shifted by the
    number of pages inserted, and the outline shifted with them.

    The outline's *pages* are reliable; its *titles* are not (a heading that
    wrapped when rendered comes back with the space at the wrap point lost).
    So when the source headings line up one-for-one, their text is used.
    """
    import pymupdf

    doc = pymupdf.open(path)
    outline = doc.get_toc()                       # [level, title, page]
    if not outline:
        doc.close()
        return 0

    if headings and len(headings) == len(outline):
        outline = [[lvl, title, pg]
                   for (lvl, title), (_, _, pg) in zip(headings, outline)]

    X0, X1, TOP, BOT = 54, 541, 92, 800
    ROW = {0: 15.5, 1: 13.5, 2: 11.5}             # part / chapter / subchapter
    SIZE = {0: 10.5, 1: 9.5, 2: 8.5}
    INDENT = {0: 0, 1: 14, 2: 30}
    FONT = {0: "hebo", 1: "helv", 2: "helv"}

    def rank(level, title):
        if level >= 2:
            return 2
        return 0 if title.startswith("Part ") else 1

    rows = [(rank(lvl, t), t, pg) for lvl, t, pg in outline]

    # Paginate.
    pages, cur, y = [], [], TOP
    for r, title, pg in rows:
        step = ROW[r] + (6 if r == 0 and cur else 0)
        if y + step > BOT:
            pages.append(cur)
            cur, y = [], TOP
            step = ROW[r]
        y += step
        cur.append((r, title, pg, y))
    if cur:
        pages.append(cur)
    n = len(pages)

    for i in range(n):
        doc.new_page(1 + i, width=595, height=842)

    # Pages are inserted *after* the title page, so anything already on
    # page 1 stays put; everything from page 2 on moves down by n.
    def shift(p):
        return p if p <= 1 else p + n

    for i, rowset in enumerate(pages):
        page = doc[1 + i]
        if i == 0:
            page.insert_text((X0, 60), "Contents", fontname="hebo", fontsize=17)
        for r, title, target, y in rowset:
            size, font, x = SIZE[r], FONT[r], X0 + INDENT[r]
            title = _ascii(title)
            num = str(shift(target))
            numw = pymupdf.get_text_length(num, fontname="helv", fontsize=size)
            # Trim anything that would otherwise run into the page number.
            room = X1 - x - numw - 14
            width = lambda s: pymupdf.get_text_length(s, fontname=font,
                                                      fontsize=size)
            if width(title) > room:
                while len(title) > 8 and width(title + "...") > room:
                    title = title[:-1]
                title = title.rstrip(" ,;:-") + "..."
            titlew = width(title)
            page.insert_text((x, y), title, fontname=font, fontsize=size)
            page.insert_text((X1 - numw, y), num, fontname="helv", fontsize=size)
            # dot leader between title and page number
            gap0, gap1 = x + titlew + 5, X1 - numw - 5
            if gap1 > gap0:
                dotw = pymupdf.get_text_length(".", fontname="helv", fontsize=size)
                dots = "." * max(0, int((gap1 - gap0) / dotw))
                page.insert_text((gap0, y), dots, fontname="helv",
                                 fontsize=size, color=(0.6, 0.6, 0.6))
            page.insert_link({
                "kind": pymupdf.LINK_GOTO,
                "from": pymupdf.Rect(x, y - size - 1, X1, y + 3),
                "page": shift(target) - 1,        # 0-based
                "to": pymupdf.Point(0, 0),
            })

    # Shift every existing bookmark past the inserted pages, and put a
    # Contents bookmark at the front so the outline matches the printed TOC.
    doc.set_toc([[1, "Contents", 2]] +
                [[lvl, t, shift(pg)] for lvl, t, pg in outline])
    doc.saveIncr()
    doc.close()
    return n


def stamp_page_numbers(path):
    """Draw a centred page number at the foot of every page but the title."""
    import pymupdf

    doc = pymupdf.open(path)
    for i, page in enumerate(doc):
        if i < SKIP_PAGES:
            continue
        label = str(i + 1)
        width = pymupdf.get_text_length(label, fontname=FOLIO_FONT,
                                        fontsize=FOLIO_SIZE)
        page.insert_text(
            ((page.rect.width - width) / 2,
             page.rect.height - FOLIO_BASELINE_FROM_BOTTOM),
            label,
            fontname=FOLIO_FONT,
            fontsize=FOLIO_SIZE,
            color=FOLIO_COLOR,
        )
    # Incremental save keeps the generated bookmark outline intact.
    doc.save(path, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    numbered = doc.page_count - SKIP_PAGES
    doc.close()
    return numbered


# Every diagram in the book is introduced by a one-line lead-in ending in a
# colon, so the lead-in is tagged along with the diagram and the two are
# moved as a pair -- a caption stranded at the foot of a page while its
# diagram starts the next one reads worse than the gap it saves.
LEAD_IN = re.compile(r"(?:<p>(?P<lead>(?:(?!</p>).)*)</p>\s*)?<pre>", re.S)


def markdown_html(combined):
    """Render the book to HTML, tagging each diagram and its lead-in.

    The ids are what make the layout engine report where each diagram
    landed; nothing in the finished PDF refers to them.
    """
    from markdown_it import MarkdownIt

    html = MarkdownIt("commonmark").enable("table").render(combined)
    n = itertools.count()

    def tag(m):
        i = next(n)
        pre = f'<pre id="d{i}">'
        if m.group("lead") is None:
            return pre
        return f'<p id="c{i}">{m.group("lead")}</p>\n{pre}'

    return LEAD_IN.sub(tag, html)


def diagram_heights(combined):
    """Full laid-out height of every fenced block, in points, in book order.

    A fenced block is one monospace line per source line at a fixed line
    height, so this is exact -- and knowing what a diagram *should* measure
    is how a placed one can be told to have been cut short.
    """
    heights, inside, n = [], False, 0
    for ln in combined.split("\n"):
        if ln.startswith("```"):
            if inside:
                heights.append(n * PRE_LINE_PT)
            inside, n = not inside, 0
        elif inside:
            n += 1
    return heights


def render(html, trims):
    """Lay the whole book out as one continuous flow; return the document.

    `trims` maps a 0-based page index to the y-coordinate that page should
    end at, so everything below flows onto the next page. Also returns the
    bookmark outline and where every tagged element landed, as
    ``{"d": {index: (page, top, height)}, "c": {...}}`` -- diagrams and
    their lead-ins.
    """
    import pymupdf

    rect = pymupdf.paper_rect(PAPER)
    full = rect + BORDERS
    buf = io.BytesIO()
    writer = pymupdf.DocumentWriter(buf)
    story = pymupdf.Story(html=html, user_css=CSS)

    toc, hrefs, page = [], [], [0]
    placed = {"d": {}, "c": {}}

    def record(pos):
        pos.page_num = page[0] + 1
        hrefs.append(pos)
        if not pos.open_close & 1:                # only "open" items
            return
        if pos.id:
            placed[pos.id[0]][int(pos.id[1:])] = (page[0], pos.rect[1],
                                                  pos.rect[3] - pos.rect[1])
        if 0 < pos.heading <= TOC_LEVEL:
            toc.append([pos.heading, pos.text, page[0] + 1])

    more = 1
    while more:
        where = pymupdf.Rect(full)
        if page[0] in trims:
            where.y1 = trims[page[0]]
        device = writer.begin_page(rect)
        more, _ = story.place(where)
        story.element_positions(record, {})
        story.draw(device)
        writer.end_page()
        page[0] += 1

    writer.close()
    buf.seek(0)
    return pymupdf.Story.add_pdf_links(buf, hrefs), toc, placed


def misplaced(heights, placed, skip):
    """Diagrams that fell badly, earliest first, as (page, top, index).

    Two faults count: a diagram cut across a page boundary, and a diagram
    parted from the lead-in that introduces it. Both are cured the same way
    -- end the page where the pair begins -- so both are reported as the
    point the pair starts at.
    """
    diagrams, leads = placed["d"], placed["c"]
    out = []
    for i, height in enumerate(heights):
        if i in skip:
            continue
        page, top, drawn = diagrams[i]
        lead = leads.get(i)
        if drawn >= height - SPLIT_SLACK and not (lead and lead[0] < page):
            continue
        out.append((lead[0], lead[1], i) if lead else (page, top, i))
    return sorted(out)


def keep_diagrams_whole(html, heights):
    """Render, ending pages early where needed so no diagram falls badly.

    Each pass fixes only the *earliest* remaining fault. Ending a page early
    moves nothing above it, so every trim already agreed stays correct and
    the loop can never undo its own work -- which is what lets it walk down
    the book once instead of iterating to a fixed point.
    """
    import pymupdf

    full = pymupdf.paper_rect(PAPER) + BORDERS
    trims, stuck = {}, set()
    for _ in range(MAX_TRIM_PASSES):
        doc, toc, placed = render(html, trims)
        faults = misplaced(heights, placed, stuck)
        if not faults:
            return doc, toc, trims, stuck
        page, top, i = faults[0]
        if top - 1 <= full.y0 + 1:
            # The pair already begins a page, so no trim can lift it higher.
            # Settle for the diagram alone if that is still worth moving.
            page, top, _ = placed["d"][i]
        if heights[i] > full.y1 - full.y0 or top - 1 <= full.y0 + 1:
            stuck.add(i)
            continue
        doc.close()
        trims[page] = top - 1
    raise RuntimeError("diagram layout did not settle")


def page_fill(doc):
    """How much of each page's text block is used, emptiest page first.

    Measured against the text block rather than the sheet, and ignoring
    anything in the bottom margin, so the stamped folio does not read as a
    full page.
    """
    top, foot = BORDERS[1], -BORDERS[3]
    out = []
    for pno, page in enumerate(doc):
        floor = page.rect.height - foot
        bottom = top
        for blk in page.get_text("dict")["blocks"]:
            if blk.get("type") != 0:
                continue
            for ln in blk["lines"]:
                if ln["bbox"][3] <= floor and "".join(
                        sp["text"] for sp in ln["spans"]).strip():
                    bottom = max(bottom, ln["bbox"][3])
        out.append(((bottom - top) / (floor - top), pno + 1))
    return sorted(out)


def main():
    try:
        import markdown_it                        # noqa: F401
        import pymupdf                            # noqa: F401
    except ImportError:
        sys.exit("Missing dependency. Run: pip install pymupdf markdown-it-py")

    files = sorted(glob.glob(os.path.join(BOOK, "**", "*.md"), recursive=True))
    if not files:
        sys.exit(f"No markdown files found under {BOOK}")

    parts = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        # Drop LaTeX-only directives meant for the pandoc build.
        text = re.sub(r"^\\newpage\s*$", "", text, flags=re.MULTILINE)
        parts.append(text.strip())

    combined = "\n\n".join(parts) + "\n"
    html = markdown_html(combined)
    heights = diagram_heights(combined)
    if html.count("<pre id=") != len(heights):
        sys.exit("fenced blocks and rendered <pre> elements do not correspond")

    os.makedirs(OUT_DIR, exist_ok=True)

    doc, toc, trims, stuck = keep_diagrams_whole(html, heights)
    doc.set_metadata({"title": "How a Tesla Works", "author": ""})
    doc.set_toc(toc)
    doc.save(OUT_PDF)
    body_pages = doc.page_count
    doc.close()

    toc_pages = prepend_toc(OUT_PDF, source_headings(combined))
    numbered = stamp_page_numbers(OUT_PDF)

    import pymupdf
    with pymupdf.open(OUT_PDF) as final:
        # The front matter and the last page of the book are short by nature.
        worst = [(f, p) for f, p in page_fill(final)
                 if 1 + toc_pages < p < final.page_count]

    print(f"Rendered {len(files)} files -> {OUT_PDF}")
    print(f"Contents: {toc_pages} page(s), every line a clickable link")
    print(f"Numbered {numbered} pages (title page left blank)")
    print(f"Body set as one flow over {body_pages} pages; {len(trims)} "
          f"page(s) ended early to keep a diagram with its lead-in")
    if stuck:
        print(f"  warning: {len(stuck)} diagram(s) could not be placed cleanly")
    print("Emptiest body pages: " +
          ", ".join(f"p{p} {f:.0%}" for f, p in worst[:5]))


if __name__ == "__main__":
    main()
