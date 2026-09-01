# How a Tesla Works

A high-level but genuinely technical overview of how a modern electric car works,
using Tesla (Model 3 / Model Y) as the worked example. Written for the technically
curious non-engineer.

Knowledge cutoff for the text: **2026**. The book dates itself rather than pretending
to be timeless.

- Sold as an ebook. Source kept here.
- Built from one markdown file per subchapter, concatenated into markdown,
  PDF and EPUB.

## Build

**A build is always all three artefacts:**

```bash
python build_all.py
```

The book ships as markdown, PDF and EPUB, and all three come from the same
pass over `book/` so they cannot disagree. Never finish a change by running
just one of the builds below — a stale artefact still looks finished, which
is how `out/how-a-tesla-works.md` once spent three commits contradicting the
other two.

The individual scripts are there for iterating on a single builder.

### Single-file markdown — `out/how-a-tesla-works.md`

```bash
python build_markdown.py
```

Every subchapter concatenated in book order and otherwise untouched, LaTeX
directives included. This is the source edition; the two builds below each
drop what they cannot use.

### PDF — `out/how-a-tesla-works.pdf`

```bash
pip install pymupdf markdown-it-py
python build_pdf.py
```
Renders A4 via PyMuPDF's Story engine, and is the route used to build the
shipped PDF. It also does two things the renderer will not do on its own.

It prints a **clickable Contents section** — every line is a link, and the
bookmark outline matches it.

And it keeps every ASCII diagram whole, without leaving half-empty pages
behind. The book is laid out as one continuous flow, so text fills each page
to the bottom; PyMuPDF ignores `page-break-inside`, so where a diagram would
be cut across a page boundary — or parted from the one-line lead-in that
introduces it — the build ends that page early, just above the lead-in, and
the pair moves down together. The gap left behind is never worse than the
diagram's own height, whereas a hard page break strands whatever was still
empty. The build reports its emptiest pages so this stays visible.

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

### `build.sh` — the LaTeX route, PDF only

```bash
./build.sh
```

Renders the PDF alone, via `pandoc` and `xelatex`, and leaves the markdown
and EPUB untouched. It is not a build in the sense above — use it only to
compare typesetting against the Python route, never to produce a release.

## Status

Drafting in progress. See `PROJECT-BRIEF.md` for structure, voice, and conventions.
