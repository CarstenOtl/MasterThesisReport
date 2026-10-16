#!/usr/bin/env bash
# Build the thesis PDF with latexmk and print only a compact summary.
# Usage: build.sh [folder]   (default: thesis; expose/ is frozen and refused)
set -u
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
DOC="${1:-thesis}"
if [ "$DOC" = "expose" ]; then
  echo "refused: expose/ is frozen (see CLAUDE.md)"; exit 2
fi
DIR="$REPO/$DOC"
[ -f "$DIR/main.tex" ] || { echo "no $DIR/main.tex"; exit 2; }
cd "$DIR" || exit 2

latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null 2>&1
RC=$?
LOG=main.log

if [ $RC -ne 0 ]; then
  echo "BUILD FAILED (latexmk exit $RC)"
  # first LaTeX error with context line
  grep -n -A3 -m1 '^!' "$LOG" | sed 's/^/  /'
  # biber errors, if any
  [ -f main.blg ] && grep -m5 'ERROR' main.blg | sed 's/^/  /'
  exit $RC
fi

PAGES=$(grep -o 'Output written on main.pdf ([0-9]* pages' "$LOG" | grep -o '[0-9]* pages')
echo "BUILD OK: main.pdf, ${PAGES:-? pages}"

UNDEF_REF=$(grep -c "Reference .* undefined" "$LOG")
UNDEF_CIT=$(grep -c "Citation .* undefined" "$LOG")
OVERFULL=$(grep -c '^Overfull' "$LOG")
UNDERFULL=$(grep -c '^Underfull' "$LOG")
BIBWARN=$( [ -f main.blg ] && grep -c 'WARN' main.blg || echo 0)
echo "undefined refs: $UNDEF_REF | undefined citations: $UNDEF_CIT | overfull: $OVERFULL | underfull: $UNDERFULL | biber warnings: $BIBWARN"

if [ "$UNDEF_REF" -gt 0 ]; then
  grep -o "Reference \`[^']*' on page [0-9]*" "$LOG" | sort -u | head -10 | sed 's/^/  /'
fi
if [ "$UNDEF_CIT" -gt 0 ]; then
  grep -o "Citation \`[^']*' on page [0-9]*" "$LOG" | sort -u | head -10 | sed 's/^/  /'
fi
if [ "$OVERFULL" -gt 0 ]; then
  grep '^Overfull' "$LOG" | sort -t'(' -k2 -rn | head -5 | sed 's/^/  /'
fi
