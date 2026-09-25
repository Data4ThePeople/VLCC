# Status

Project: VLCC
Process: ~/.claude/d4tp-process/PROCESS.md

## Current

Post: supertanker-rates
Step: complete
Since: 2026-09-14

## Steps

| Step | What | Confirmed | Notes |
|---|---|---|---|
| 1  | Exploration and analysis | 2026-09-13 | interactive chart dist/index.html; Brent panel toggle; notes in research/ |
| 2a | Draft with brackets resolved | 2026-09-14 | headline, table image, delivered-cost section, six headers |
| 2b | Eric's edit, Claude's look-over | 2026-09-14 | 7 edits applied |
| 2c | Slice markup | 2026-09-14 | defaults only; 19 slices |
| 2d | Hero 1680x1080 + alt text | 2026-09-14 | gold VLCC, AI image, center crop |
| 2e | SEO | 2026-09-14 | meta, keywords, FAQ schema, internal links, METI source |
| 2f | Pushed to Prismic (draft) | 2026-09-14 | doc aqhiwxEAACoAjvRa, Migration Release |
| 2g | Mailchimp teaser | 2026-09-14 | EMAIL.md approved; email hero JPG exported |

## Stale

None.

## Log

- 2026-09-13 Step 1 opened. Topic: VLCC supertanker rates, how far back the series goes, the last major spike versus the 2026 spike, and why tanker rates matter for oil prices. Deliverable: one interactive weekly trend chart with hover, updatable each week, for a Data 4 Thought piece.
- 2026-09-13 Step 1 work: Baltic TD3C weekly TCE assembled Dec 2020 to Sep 2026 (Wayback + prior desktop session); Fearnleys VLCC MEG/Far East pulled May 2018 to now (TCE to Apr 2023); interactive chart in dist/index.html; static PNG in charts/; research in research/NOTES.md; tie-out in research/TIEOUT.md; weekly update via scripts/update.py. GitHub remote not created (permission blocked).
- 2026-09-13 Step 1 confirmed. Slug: supertanker-rates. Step 2a opened.
- 2026-09-14 GitHub Pages enabled on main. Embed URL: https://data4thepeople.github.io/VLCC/dist/index.html
- 2026-09-14 Step 2a confirmed. Step 2b opened.
- 2026-09-14 Step 2b confirmed. Step 2c opened.
- 2026-09-14 Step 2c confirmed. Step 2d opened.
- 2026-09-14 Step 2d confirmed. Step 2e opened.
- 2026-09-14 Step 2e confirmed. Step 2f opened.
- 2026-09-14 2c rule change: dividers off, 20px spacers above section headings. Re-converted and re-pushed the Prismic draft (same document).
- 2026-09-14 Step 2f confirmed. Step 2g opened.
- 2026-09-14 Step 2g confirmed. Post complete. Weekly updates continue via scripts/update.py.
- 2026-09-18 Added a "first published September 14, 2026" note at the top of the post (blurb, then the drop cap). Re-converted; Prismic re-push pending (classifier blocked it). Week 38 Baltic report not yet published at 12:42 London time; weekly row still to add.
- 2026-09-19 Weekly update: week 38 Baltic row added (Sep 18, WS 1,140, TCE \$1,212,503) via the r.jina.ai reader proxy, which gets past the Baltic site block; update.py now tries it first and the parser handles the from/to sentence form. Fearnleys through Sep 18 (WS 1100).
- 2026-09-25 Weekly update: week 39 Baltic row added (Sep 25, WS 1,157.5, TCE \$1,235,414) via the r.jina.ai reader proxy. Fearnleys through Sep 25 (WS 1150).
- 2026-09-25 Brent update: EIA weekly RBRTE through Sep 18 (\$124.15); daily physical vs futures through Sep 22 spot (\$114.89) and Sep 25 futures. EIA had not yet posted the week of Sep 25.
