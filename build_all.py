#!/usr/bin/env python3
"""
Build every artefact in out/ from the sources in book/.

    python build_all.py

Runs the three builds that together make a release:

    build_markdown.py  ->  out/how-a-tesla-works.md
    build_pdf.py       ->  out/how-a-tesla-works.pdf
    build_ebook.py     ->  out/how-a-tesla-works.epub

Each is still runnable on its own when only one output is wanted; this is
the one that leaves nothing stale behind. build.sh is a separate route to
the PDF alone, via pandoc and LaTeX.
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
