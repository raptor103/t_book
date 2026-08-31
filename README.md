# How a Tesla Works

A high-level but genuinely technical overview of how a modern electric car works,
using Tesla (Model 3 / Model Y) as the worked example. Written for the technically
curious non-engineer.

Knowledge cutoff for the text: **2026**. The book dates itself rather than pretending
to be timeless.

- Free on GitHub. Optional donations: _[donation link TBD]_
- Built from one markdown file per subchapter, concatenated to a single PDF.

## Build

Two ways to produce `out/how-a-tesla-works.pdf`:

**Canonical (pandoc + LaTeX):**
```bash
./build.sh
```
Requires `pandoc` and a LaTeX engine (`xelatex`).

**Dependency-light (pure Python, no LaTeX):**
```bash
pip install markdown-pdf
python build_pdf.py
```
Renders an A4 PDF with a generated table of contents using PyMuPDF. This is
the route used to build the current PDF (140 pages).

## Status

Drafting in progress. See `PROJECT-BRIEF.md` for structure, voice, and conventions.
