#!/usr/bin/env python3
"""
Build the single-file markdown edition of "How a Tesla Works".

    python build_markdown.py

Output: out/how-a-tesla-works.md

Every subchapter file concatenated in book order and otherwise untouched --
LaTeX directives included, because this is the source edition rather than a
rendered one. The PDF and EPUB builds each drop what they cannot use.

Filenames are numbered so a plain alphabetical sort produces book order,
which is the same thing the other two builds rely on.
"""
import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(ROOT, "book")
OUT_DIR = os.path.join(ROOT, "out")
OUT_MD = os.path.join(OUT_DIR, "how-a-tesla-works.md")

# Image cover: copied next to the markdown and shown at the top, so the .md
# and its cover travel together.
COVER = os.path.join(ROOT, "front_cover", "Book cover V1.png")
COVER_FILE = "cover.png"

# The per-subchapter "Sources" note -- a bold label and a bullet list -- is
# reference apparatus, not body text. Plain markdown carries no type size, so
# the block is wrapped in a div with an inline style: renderers that honour it
# set the sources a step smaller and greyer, and those that strip it lose
# nothing but the size cue. The blank lines inside keep the label and list
# rendering as markdown, and the trailing blank line keeps the following
# chapter heading from being swallowed into the closing tag.
SOURCES = re.compile(
    r"(?m)^\*\*Sources\*\*[ \t]*\n\n"
    r"(?:[ \t]*[-*][ \t].*\n?|[ \t]+\S.*\n?)+")


def shrink_sources(text):
    def wrap(m):
        block = m.group(0).strip()
        return ('<div class="sources" style="font-size:0.85em;color:#555">\n\n'
                f"{block}\n\n</div>\n\n")
    return SOURCES.sub(wrap, text)


def center_title(text):
    """Centre the title block for the markdown edition.

    Plain markdown has no alignment, so the three title lines are wrapped in a
    center-aligned div (honoured by GitHub and most renderers); any trailing
    \\newpage directive is left outside it. Renderers that strip the tag simply
    show the title left-aligned, losing nothing but the centring.
    """
    m = re.search(r"\A(.*?)(\n+\\newpage\s*)?\Z", text, re.S)
    body, tail = m.group(1).strip(), (m.group(2) or "")
    return f'<div align="center">\n\n{body}\n\n</div>\n{tail}'


def source_files():
    files = sorted(glob.glob(os.path.join(BOOK, "**", "*.md"), recursive=True))
    if not files:
        sys.exit(f"No markdown files found under {BOOK}")
    return files


def main():
    files = source_files()
    parts = []
    for path in files:
        with open(path, encoding="utf-8") as fh:
            text = shrink_sources(fh.read())
        if os.path.basename(path) == "00-00-title.md":
            text = center_title(text)
        parts.append(text)

    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(COVER, os.path.join(OUT_DIR, COVER_FILE))
    cover = (f'<p align="center"><img src="{COVER_FILE}" '
             f'alt="How a Tesla Works" width="480"></p>\n\n')
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(cover + "".join(parts))

    words = sum(len(p.split()) for p in parts)
    print(f"Built from {len(files)} markdown files")
    print(f"  MD    -> {OUT_MD}")
    print(f"  Words -> {words:,}")


if __name__ == "__main__":
    main()
