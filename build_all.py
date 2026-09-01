#!/usr/bin/env python3
"""
Build every artefact in out/ from the sources in book/.

    python build_all.py

A build of this book means all three artefacts, always:

    build_markdown.py  ->  out/how-a-tesla-works.md
    build_pdf.py       ->  out/how-a-tesla-works.pdf
    build_ebook.py     ->  out/how-a-tesla-works.epub

They are three editions of one book, so shipping one that disagrees with the
others is worse than shipping nothing -- whichever is stale still looks
finished. Running all three off one pass over book/ is what stops them
drifting apart, and this is the only entry point that does it.

The individual scripts remain runnable for iterating on a single builder.
build.sh is a separate pandoc + LaTeX route to the PDF alone, and leaves the
other two stale.
"""
import sys

import build_ebook
import build_markdown
import build_pdf

STEPS = (build_markdown, build_pdf, build_ebook)


def main():
    for step in STEPS:
        print(f"=== {step.__name__} ===")
        step.main()
        print()
    print(f"All {len(STEPS)} outputs rebuilt.")


if __name__ == "__main__":
    sys.exit(main())
