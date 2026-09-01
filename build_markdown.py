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
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(ROOT, "book")
OUT_DIR = os.path.join(ROOT, "out")
OUT_MD = os.path.join(OUT_DIR, "how-a-tesla-works.md")


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
            parts.append(fh.read())

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("".join(parts))

    words = sum(len(p.split()) for p in parts)
    print(f"Built from {len(files)} markdown files")
    print(f"  MD    -> {OUT_MD}")
    print(f"  Words -> {words:,}")


if __name__ == "__main__":
    main()
