# How a Tesla Works

A high-level but genuinely technical overview of how a modern electric car works,
using Tesla (Model 3 / Model Y) as the worked example. Written for the technically
curious non-engineer.

Knowledge cutoff for the text: **2026**. The book dates itself rather than pretending
to be timeless.

- Free on GitHub. Optional donations: _[donation link TBD]_
- Built from one markdown file per subchapter, concatenated into PDF and EPUB.

## Build

### PDF — `out/how-a-tesla-works.pdf`

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
Renders A4 via PyMuPDF, and is the route used to build the shipped PDF. It
also does two things the renderer will not do on its own: it prints a
**clickable Contents section** (every line is a link, and the bookmark
outline matches it), and it keeps every ASCII diagram whole — `markdown-pdf`
ignores `page-break-inside`, so the build detects diagrams straddling a page
boundary and pushes them onto the next page, repeating until none split.

### EPUB — `out/how-a-tesla-works.epub`

```bash
pip install markdown
python build_ebook.py
```

The EPUB is assembled directly, so it carries both navigation documents:
`nav.xhtml` (EPUB 3) and `toc.ncx` (EPUB 2). Every reader therefore gets a
clickable, nested table of contents — parts, chapters and subchapters.

No MOBI is produced. Amazon retired the format in 2022, and current Kindles
take EPUB directly via Send-to-Kindle, so the EPUB covers Kindle too.

## Status

Drafting in progress. See `PROJECT-BRIEF.md` for structure, voice, and conventions.
