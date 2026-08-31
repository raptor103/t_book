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


def main():
    try:
        from markdown_pdf import MarkdownPdf, Section
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

    os.makedirs(OUT_DIR, exist_ok=True)
    pdf = MarkdownPdf(toc_level=2)
    pdf.add_section(Section(combined, toc=True, paper_size="A4"), user_css=CSS)
    pdf.meta["title"] = "How a Tesla Works"
    pdf.meta["author"] = ""
    pdf.save(OUT_PDF)
    numbered = stamp_page_numbers(OUT_PDF)
    print(f"Rendered {len(files)} files -> {OUT_PDF}")
    print(f"Numbered {numbered} pages (title page left blank)")


if __name__ == "__main__":
    main()
