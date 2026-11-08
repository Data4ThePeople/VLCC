#!/bin/zsh
# Unattended weekly update, run by launchd (Friday, Saturday and Monday at 11:00).
#   1. Brent weekly (EIA) and daily physical vs futures.
#   2. Baltic TD3C row for last Friday plus Fearnleys (update.py). If the row is
#      already there, Fearnleys is refreshed and the chart rebuilt anyway.
#   3. If anything changed: STATUS.md log line, commit, push.
# Success and failure each show a macOS alert box; details are in logs/weekly.log.
set -u
ROOT="${0:A:h:h}"
PY="$ROOT/.venv/bin/python3"
LOG="$ROOT/logs/weekly.log"
mkdir -p "$ROOT/logs"
exec >>"$LOG" 2>&1
cd "$ROOT" || exit 1
echo "\n=== $(date '+%Y-%m-%d %H:%M %Z') ==="

# An alert box stays on screen until clicked; a banner notification can come
# and go unseen. "Open chart" opens the live page.
alert() {
  b=$(osascript -e "display alert \"$1\" message \"$2\" buttons {\"Open chart\", \"OK\"} default button \"OK\" giving up after 86400" 2>/dev/null)
  [[ "$b" == *"Open chart"* ]] && open "https://data4thepeople.github.io/VLCC/dist/index.html"
}

fail() {
  echo "FAILED: $1"
  alert "VLCC weekly update failed" "$1. Details in logs/weekly.log."
  exit 1
}

# A run that dies partway leaves edited files behind, and git pull refuses to
# run over them. Files this run rewrites from scratch are reset to the last
# commit. Anything else left over (a Baltic row, a STATUS.md line) is set aside
# by --autostash and put back after the pull. If putting it back conflicts with
# the pulled commits, stop rather than commit a file with conflict markers.
REGEN=(data/brent_weekly.csv data/crude_spot_vs_futures_daily.csv
       data/fearnleys_vlcc_meg_feast_daily.csv data/fearnleys_vlcc_usg_asia_lumpsum_daily.csv
       dist/index.html dist/data.json research/TIEOUT.md)
git diff --quiet || echo "leftover changes from an earlier run: $(git diff --name-only | tr '\n' ' ')"
git checkout -q -- $REGEN || fail "reset of generated files"
git pull -q --rebase --autostash || fail "git pull"
[[ -z "$(git diff --name-only --diff-filter=U)" ]] || fail "leftover changes conflict with pulled commits; resolve by hand"
"$PY" scripts/fetch_brent.py || fail "Brent weekly fetch"
"$PY" scripts/fetch_brent_physical_vs_futures.py || fail "Brent daily fetch"

out=$("$PY" scripts/update.py 2>&1); rc=$?
echo "$out"
baltic=""
if [[ $rc -eq 0 ]]; then
  baltic=$(echo "$out" | grep '^added ')
elif echo "$out" | grep -q 'already in'; then
  "$PY" scripts/fetch_fearnleys.py && "$PY" scripts/build.py >/dev/null || fail "Fearnleys or build"
else
  fail "Baltic row for last Friday not found; run update.py by hand with --ws and --tce"
fi

if git diff --quiet -- data dist research; then
  echo "no changes"; exit 0
fi

brent=$(tail -1 data/brent_weekly.csv)
line="- $(date +%F) Automatic weekly update."
[[ -n "$baltic" ]] && line="$line Baltic ${baltic#added }."
line="$line Brent weekly through ${brent%%,*} (\\\$${brent##*,})."
echo "$line" >> STATUS.md

git add STATUS.md data dist research
git commit -q -m "supertanker-rates: automatic weekly update $(date +%F)" || fail "git commit"
git push -q || fail "git push"
echo "pushed: $line"
msg=${line#- * }
alert "VLCC chart updated" "${msg//\\/}"
exit 0
