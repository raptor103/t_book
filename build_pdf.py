#!/usr/bin/env python3
"""
Pure-Python PDF build for "How a Tesla Works".

Concatenates every markdown file under book/ in sort order and renders a
single A4 PDF with a generated table of contents. Uses markdown-pdf
(PyMuPDF), so no LaTeX / pandoc is required.

    pip install markdown-pdf
    python build_pdf.py

Output: out/how-a-tesla-works.pdf

The canonical build (pandoc + xelatex) lives in build.sh; this script is the
dependency-light fallback that runs anywhere Python does. Monospace ASCII
diagrams are kept <=76 chars wide, so at 8pt they never overflow A4 margins.

markdown-pdf cannot draw footers, so page numbers are stamped on afterwards
with PyMuPDF. The title page is left unnumbered, and every other page prints
its own PDF page number, so the printed folio matches the bookmark targets.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(ROOT, "book")
OUT_DIR = os.path.join(ROOT, "out")
OUT_PDF = os.path.join(OUT_DIR, "how-a-tesla-works.pdf")

CSS = """
body { font-family: serif; font-size: 11pt; line-height: 1.45; }
h1 { font-family: sans-serif; font-size: 20pt; margin-top: 18pt; }
h2 { font-family: sans-serif; font-size: 15pt; margin-top: 14pt; }
h3 { font-family: sans-serif; font-size: 12pt; }
p  { margin: 6pt 0; }
pre, code { font-family: monospace; font-size: 8pt; }
pre { white-space: pre; line-height: 1.15; margin: 6pt 0; }
table { border-collapse: collapse; font-size: 10pt; }
th, td { border: 1px solid #999; padding: 3pt 6pt; }
hr { border: none; border-top: 1px solid #ccc; }
"""

# Page-number footer. Section borders are (36, 36, -36, -36), so body text
# stops 36pt above the page foot; the folio sits in that margin.
FOLIO_FONT = "helv"
FOLIO_SIZE = 9
FOLIO_COLOR = (0.45, 0.45, 0.45)
FOLIO_BASELINE_FROM_BOTTOM = 22
SKIP_PAGES = 1  # title page carries no number

# Keeping diagrams whole is iterative; cap the passes so a pathological
# diagram (one taller than a page) cannot loop forever.
MAX_BREAK_PASSES = 12


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

    markdown-pdf emits a bookmark outline but no visible contents, so this
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


def find_code_blocks(lines):
    """Locate fenced blocks. Returns dicts with fence line indices and text."""
    blocks, inside, start, body = [], False, 0, []
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            if inside:
                blocks.append({"start": start, "end": i, "lines": body})
                inside = False
            else:
                inside, start, body = True, i, []
        elif inside and ln.strip():
            body.append(ln.strip())
    return blocks


def mono_lines_by_page(path):
    """Every monospace line in the PDF, in reading order, with its page."""
    import pymupdf

    out = []
    doc = pymupdf.open(path)
    for pno, page in enumerate(doc):
        rows = []
        for blk in page.get_text("dict")["blocks"]:
            if blk.get("type") != 0:
                continue
            for ln in blk["lines"]:
                if not any("mono" in s["font"].lower() or "courier" in s["font"].lower()
                           for s in ln["spans"]):
                    continue
                txt = "".join(s["text"] for s in ln["spans"]).strip()
                if txt:
                    rows.append((ln["bbox"][1], txt))
        rows.sort()
        out.extend((pno, t) for _, t in rows)
    doc.close()
    return out


def split_diagrams(blocks, rendered):
    """Align source blocks to rendered lines; report blocks spanning pages."""
    bad, cursor = [], 0
    for b in blocks:
        pages, matched = set(), 0
        for want in b["lines"]:
            # Skip ahead to this line; tolerates prose that shares the font.
            probe = cursor
            while probe < len(rendered) and rendered[probe][1] != want:
                probe += 1
            if probe >= len(rendered):
                continue           # unmatched: ignore rather than guess
            pages.add(rendered[probe][0])
            cursor, matched = probe + 1, matched + 1
        if matched >= 2 and len(pages) > 1:
            b["pages"] = sorted(pages)
            bad.append(b)
    return bad


def break_line_for(lines, block):
    """Line index to break at: keep the caption paragraph with its diagram."""
    i = block["start"] - 1
    while i > 0 and not lines[i].strip():          # back over blank lines
        i -= 1
    while i > 0 and lines[i].strip():              # back over the caption
        i -= 1
    return i + 1


def render(combined, break_lines, files_count):
    from markdown_pdf import MarkdownPdf, Section

    lines = combined.split("\n")
    cuts = sorted(set(break_lines))
    chunks, prev = [], 0
    for c in cuts:
        chunks.append("\n".join(lines[prev:c]))
        prev = c
    chunks.append("\n".join(lines[prev:]))

    pdf = MarkdownPdf(toc_level=2)
    for chunk in chunks:
        if chunk.strip():
            pdf.add_section(Section(chunk, toc=True, paper_size="A4"), user_css=CSS)
    pdf.meta["title"] = "How a Tesla Works"
    pdf.meta["author"] = ""
    pdf.save(OUT_PDF)


def main():
    try:
        import markdown_pdf  # noqa: F401
    except ImportError:
        sys.exit("markdown-pdf not installed. Run: pip install markdown-pdf")

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
    lines = combined.split("\n")
    blocks = find_code_blocks(lines)

    os.makedirs(OUT_DIR, exist_ok=True)

    # The renderer ignores page-break-inside, but every Section starts on a
    # fresh page. So: render, find diagrams straddling a page boundary, cut a
    # Section just before each one, and repeat. Adding a break moves later
    # content, so this has to converge rather than run once.
    break_lines = set()
    for attempt in range(1, MAX_BREAK_PASSES + 1):
        render(combined, break_lines, len(files))
        bad = split_diagrams(blocks, mono_lines_by_page(OUT_PDF))
        if not bad:
            break
        new = {break_line_for(lines, b) for b in bad} - break_lines
        if not new:
            print(f"  warning: {len(bad)} diagram(s) still split; no new break points")
            break
        break_lines |= new
        print(f"  pass {attempt}: {len(bad)} split diagram(s), "
              f"{len(break_lines)} page break(s) inserted")

    toc_pages = prepend_toc(OUT_PDF, source_headings(combined))
    numbered = stamp_page_numbers(OUT_PDF)
    print(f"Rendered {len(files)} files -> {OUT_PDF}")
    print(f"Contents: {toc_pages} page(s), every line a clickable link")
    print(f"Numbered {numbered} pages (title page left blank)")
    print(f"Page breaks inserted to keep diagrams whole: {len(break_lines)}")


if __name__ == "__main__":
    main()
