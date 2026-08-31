#!/usr/bin/env bash
# Build the book: concatenate every markdown file in sort order, render one PDF.
# Requires: pandoc, xelatex (TeX Live / MacTeX), and a monospace font that
# preserves ASCII-diagram alignment.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOK_DIR="$ROOT/book"
OUT_DIR="$ROOT/out"
OUT_PDF="$OUT_DIR/how-a-tesla-works.pdf"

mkdir -p "$OUT_DIR"

# Collect all markdown files under book/ in ascending sort order.
# Filenames are numbered so a plain alphabetical sort produces book order.
mapfile -t FILES < <(find "$BOOK_DIR" -type f -name '*.md' | sort)

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "No markdown files found under $BOOK_DIR" >&2
  exit 1
fi

echo "Rendering ${#FILES[@]} files -> $OUT_PDF"

pandoc "${FILES[@]}" \
  --from=gfm \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=2 \
  -V documentclass=report \
  -V papersize=a4 \
  -V geometry:margin=2.2cm \
  -V mainfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V fontsize=11pt \
  -V linkcolor=blue \
  -V pagestyle=plain \
  --metadata title="How a Tesla Works" \
  --metadata author="" \
  -o "$OUT_PDF"

echo "Done: $OUT_PDF"
