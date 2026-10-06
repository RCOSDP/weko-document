#!/bin/bash
# Build the weko-document books with honkit and check the HTML for broken links/anchors/images.
#
# usage: build_docs.sh [--compare <git ref>] [--work <dir>] [--pdf] [book ...]
#   book:       spec admin user GUIDE (default: all four)
#   --compare:  also build the books of <git ref> (e.g. main, or the previous release commit)
#               and report only the issues that are new in the working tree (check_build.py --baseline)
#   --work:     where logs and the <git ref> build go (default: $TMPDIR or /tmp, weko-doc-build)
#   --pdf:      also make the PDF (needs calibre's ebook-convert; slow)
# Run from the weko-document repository root. Output of the working tree: docs/build/<book>/html (gitignored).
# Exit code 1 if a build fails or check_build.py finds new issues.
set -u
SCRIPTS=$(cd "$(dirname "$0")" && pwd)
cd "$(git rev-parse --show-toplevel)/docs" || exit 1
REF= WORK=${TMPDIR:-/tmp}/weko-doc-build PDF= BOOKS=()
while [ $# -gt 0 ]; do
  case $1 in
    --compare) REF=$2; shift 2 ;;
    --work) WORK=$2; shift 2 ;;
    --pdf) PDF=1; shift ;;
    *) BOOKS+=("$1"); shift ;;
  esac
done
[ ${#BOOKS[@]} -eq 0 ] && BOOKS=(spec admin user GUIDE)
declare -A SRC=([spec]=spec/base [admin]=manuals/ADMIN/base [user]=manuals/USER/base [GUIDE]=manuals/GUIDE/base)
mkdir -p "$WORK/logs"

# honkit and its plugins. --ignore-scripts would skip plugin setup, so skip only the puppeteer
# download instead (it has no arm64 Chromium). npm ci keeps package-lock.json unchanged.
if [ ! -x node_modules/.bin/honkit ]; then
  PUPPETEER_SKIP_DOWNLOAD=true PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true npm ci > "$WORK/logs/npm.log" 2>&1 \
    || { echo "npm ci failed: $WORK/logs/npm.log"; exit 1; }
fi

build() {  # build <docs dir> <book> <out dir> <log>
  local docs=$1 b=$2 out=$3 log=$4 s=$SECONDS
  rm -rf "$out"; mkdir -p "$out"
  (cd "$docs" && npx honkit build "$PWD/${SRC[$b]}" "$out/html") > "$log" 2>&1
  local rc=$?
  echo "  $b: exit=$rc $((SECONDS - s))s -> $out/html"
  if [ -n "$PDF" ] && [ $rc -eq 0 ]; then
    (cd "$docs" && npx honkit pdf "$PWD/${SRC[$b]}" "$out/$b.pdf") >> "$log" 2>&1 && echo "  $b: pdf -> $out/$b.pdf"
  fi
  return $rc
}

FAIL=0
if [ -n "$REF" ]; then
  echo "build $REF"
  rm -rf "$WORK/ref"; mkdir -p "$WORK/ref"
  git archive "$REF" . | tar -x -C "$WORK/ref" || exit 1
  ln -s "$PWD/node_modules" "$WORK/ref/node_modules"
  for b in "${BOOKS[@]}"; do build "$WORK/ref" "$b" "$WORK/ref/build/$b" "$WORK/logs/ref_$b.log"; done
fi
echo "build working tree"
for b in "${BOOKS[@]}"; do build "$PWD" "$b" "$PWD/build/$b" "$WORK/logs/$b.log" || FAIL=1; done

echo "check"
for b in "${BOOKS[@]}"; do
  BASE=()
  [ -n "$REF" ] && BASE=(--baseline "$WORK/ref/build/$b/html")
  python3 "$SCRIPTS/check_build.py" "build/$b/html" "${BASE[@]}" --log "$WORK/logs/$b.log" --max 10 || FAIL=1
done
exit $FAIL
