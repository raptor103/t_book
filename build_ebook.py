#!/usr/bin/env python3
"""
Build EPUB (and, if Calibre is present, MOBI) for "How a Tesla Works".

    pip install markdown
    python build_ebook.py

Output: out/how-a-tesla-works.epub
        out/how-a-tesla-works.mobi   (needs Calibre's ebook-convert)

The EPUB is written by hand rather than via a library so that both
navigation documents are guaranteed present and correct:

  * nav.xhtml  - the EPUB 3 navigation document (clickable TOC)
  * toc.ncx    - the EPUB 2 fallback, which older readers use and which
                 Calibre carries across into the MOBI's TOC

Both list every chapter and every subchapter, so the table of contents is
clickable in every format the repo ships.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(ROOT, "book")
OUT_DIR = os.path.join(ROOT, "out")
OUT_EPUB = os.path.join(OUT_DIR, "how-a-tesla-works.epub")
OUT_MOBI = os.path.join(OUT_DIR, "how-a-tesla-works.mobi")

TITLE = "How a Tesla Works"
AUTHOR = ""
LANG = "en"
UID = "urn:uuid:how-a-tesla-works-2026"

# ASCII diagrams must stay in monospace and must not re-wrap: a wrapped
# diagram is a destroyed diagram. 76 columns is the repo-wide limit, so the
# type is sized to let that fit on a modest screen.
CSS = """
body { font-family: Georgia, "Times New Roman", serif; line-height: 1.5;
       margin: 0 5%; text-align: left; }
h1 { font-family: Helvetica, Arial, sans-serif; font-size: 1.5em;
     margin: 1.2em 0 0.6em; page-break-before: always; }
h2 { font-family: Helvetica, Arial, sans-serif; font-size: 1.2em;
     margin: 1.2em 0 0.5em; }
h3 { font-family: Helvetica, Arial, sans-serif; font-size: 1.05em; }
p { margin: 0.6em 0; }
hr { border: 0; border-top: 1px solid #bbb; margin: 1.4em 0; }
ul { margin: 0.6em 0 0.6em 1.2em; }
code { font-family: "Courier New", monospace; }
pre { font-family: "Courier New", monospace; font-size: 0.62em;
      line-height: 1.15; white-space: pre; overflow-x: auto;
      margin: 0.9em 0; page-break-inside: avoid; }
nav#toc ol { list-style: none; padding-left: 0; }
nav#toc ol ol { padding-left: 1.2em; }
nav#toc li { margin: 0.25em 0; }
"""

XHTML = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}">
<head><meta charset="utf-8"/><title>{title}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{body}
</body>
</html>
"""


def source_files():
    files = sorted(glob.glob(os.path.join(BOOK, "**", "*.md"), recursive=True))
    if not files:
        sys.exit(f"No markdown files found under {BOOK}")
    return files


def _flatten(tokens, out):
    for t in tokens:
        out.append(t)
        _flatten(t.get("children", []), out)


def convert(files):
    """Markdown -> (xhtml docs, nested TOC tree).

    Each file is converted separately, so per-file heading nesting says
    nothing about the book's structure -- a subchapter file's only heading
    is an <h2>, which looks top-level inside that file. So headings are
    collected flat across the whole book and re-nested here by rank:

        # Part ...   -> a part
        # anything   -> a chapter
        ## / ###     -> a subchapter
    """
    import markdown

    docs, flat = [], []
    for n, path in enumerate(files):
        name = f"text{n:03d}.xhtml"
        with open(path, encoding="utf-8") as fh:
            text = re.sub(r"^\\newpage\s*$", "", fh.read(), flags=re.M)

        md = markdown.Markdown(extensions=["fenced_code", "toc"],
                               output_format="xhtml")
        body = md.convert(text)
        docs.append((name, XHTML.format(lang=LANG, title=escape(TITLE), body=body)))

        toks = []
        _flatten(md.toc_tokens, toks)
        for t in toks:
            if t["level"] == 1:
                rank = 0 if t["name"].startswith("Part ") else 1
            else:
                rank = 2
            flat.append({"rank": rank, "name": t["name"], "id": t["id"],
                         "file": name, "children": []})

    # Re-nest: a chapter joins the current part, a subchapter the current
    # chapter. Anything appearing before its parent (the front matter) simply
    # stays at the top level.
    tree, part, chapter = [], None, None
    for e in flat:
        if e["rank"] == 0:
            tree.append(e); part, chapter = e, None
        elif e["rank"] == 1:
            (part["children"] if part else tree).append(e); chapter = e
        else:
            (chapter["children"] if chapter else tree).append(e)
    return docs, tree


def nav_xhtml(toc):
    """EPUB 3 navigation document - the clickable TOC."""
    def render(entries):
        out = ["<ol>"]
        for e in entries:
            out.append(f'<li><a href="{e["file"]}#{e["id"]}">'
                       f'{escape(e["name"])}</a>')
            if e["children"]:
                out += render(e["children"])
            out.append("</li>")
        out.append("</ol>")
        return out

    body = (['<nav epub:type="toc" id="toc"><h1>Contents</h1>']
            + render(toc) + ["</nav>"])
    return XHTML.format(lang=LANG, title="Contents", body="\n".join(body))


def toc_ncx(toc):
    """EPUB 2 fallback. Calibre reads this when building the MOBI TOC."""
    counter = [0]

    def render(entries):
        rows = []
        for e in entries:
            counter[0] += 1
            n = counter[0]
            rows.append(
                f'<navPoint id="n{n}" playOrder="{n}">'
                f'<navLabel><text>{escape(e["name"])}</text></navLabel>'
                f'<content src="{e["file"]}#{e["id"]}"/>')
            rows += render(e["children"])
            rows.append("</navPoint>")
        return rows

    rows = render(toc)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{UID}"/><meta name="dtb:depth" content="3"/>
<meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/></head>
<docTitle><text>{escape(TITLE)}</text></docTitle>
<navMap>
{chr(10).join(rows)}
</navMap>
</ncx>
"""


def content_opf(docs):
    items = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
             '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
             '<item id="css" href="style.css" media-type="text/css"/>']
    spine = ['<itemref idref="nav"/>']
    for i, (name, _) in enumerate(docs):
        items.append(f'<item id="t{i}" href="{name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="t{i}"/>')
    return f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{UID}</dc:identifier>
<dc:title>{escape(TITLE)}</dc:title>
<dc:language>{LANG}</dc:language>
<dc:creator>{escape(AUTHOR)}</dc:creator>
<meta property="dcterms:modified">2026-01-01T00:00:00Z</meta>
</metadata>
<manifest>
{chr(10).join(items)}
</manifest>
<spine toc="ncx">
{chr(10).join(spine)}
</spine>
</package>
"""


def write_epub(docs, toc):
    os.makedirs(OUT_DIR, exist_ok=True)
    with zipfile.ZipFile(OUT_EPUB, "w") as z:
        # The mimetype entry must come first and be stored uncompressed.
        z.writestr("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0" encoding="utf-8"?>\n'
                   '<container version="1.0" '
                   'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles></container>',
                   zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", content_opf(docs), zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml", nav_xhtml(toc), zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", toc_ncx(toc), zipfile.ZIP_DEFLATED)
        for name, body in docs:
            z.writestr(f"OEBPS/{name}", body, zipfile.ZIP_DEFLATED)


def find_ebook_convert():
    exe = shutil.which("ebook-convert")
    if exe:
        return exe
    for base in (r"C:\Program Files\Calibre2", r"C:\Program Files (x86)\Calibre2",
                 os.path.expandvars(r"%LOCALAPPDATA%\Programs\Calibre2")):
        cand = os.path.join(base, "ebook-convert.exe")
        if os.path.exists(cand):
            return cand
    return None


def write_mobi():
    exe = find_ebook_convert()
    if not exe:
        print("  MOBI skipped: Calibre's ebook-convert not found.")
        print("  Install Calibre, then re-run: python build_ebook.py")
        return False
    # --mobi-file-type=both writes the old MOBI6 plus KF8, so the file opens
    # on both older Kindles and current ones, TOC intact.
    r = subprocess.run([exe, OUT_EPUB, OUT_MOBI,
                        "--mobi-file-type=both",
                        "--toc-title=Contents",
                        "--no-inline-toc"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("  MOBI failed:\n" + (r.stderr or r.stdout)[-800:])
        return False
    print(f"  MOBI  -> {OUT_MOBI}")
    return True


def main():
    try:
        import markdown  # noqa: F401
    except ImportError:
        sys.exit("markdown not installed. Run: pip install markdown")

    files = source_files()
    docs, toc = convert(files)
    write_epub(docs, toc)
    def count(es):
        return sum(1 + count(e["children"]) for e in es)
    subs = count(toc)
    print(f"Built from {len(files)} markdown files")
    print(f"  EPUB  -> {OUT_EPUB}")
    print(f"  TOC   -> {len(toc)} parts, {subs} entries in total")
    write_mobi()


if __name__ == "__main__":
    main()
