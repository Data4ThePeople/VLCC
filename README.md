# VLCC supertanker rates, Middle East to China, updated weekly

An interactive chart of what a very large crude carrier (VLCC) earns per day on the Middle East to China route, one reading per week from March 2019 to today. An optional panel adds the price of Brent crude, comparing physical cargoes with the futures screen.

## Live link

- Interactive chart: https://data4thepeople.github.io/VLCC/dist/index.html
- Published post: https://www.data4thepeople.com/p/supertanker-rates

The post text describes the market as of September 14, 2026. The chart updates each week, so the two will drift apart over time.

## What's here

- `dist/index.html`: the interactive chart, a self-contained page with the data inlined and no CDN.
- `dist/data.json`: the same weekly series as JSON.
- `data/`: the source data as CSV files.
  - `baltic_td3c_weekly.csv`: Baltic Exchange TD3C, weekly (Fridays).
  - `fearnleys_vlcc_meg_feast_daily.csv`: Fearnleys VLCC Middle East Gulf to Far East, daily.
  - `fearnleys_vlcc_usg_asia_lumpsum_daily.csv`: Fearnleys VLCC US Gulf to Asia, lump sum per cargo.
  - `brent_weekly.csv`: weekly Brent spot price.
  - `crude_spot_vs_futures_daily.csv`: daily physical (spot) crude prices against front-month futures.
  - `history_2008_2009.csv`, `history_2008_2009_quarterly.csv`: background figures for the 2008 to 2009 period.
- `scripts/`: fetch, update and build scripts (listed below).
- `research/NOTES.md`: research notes with sources for the background in the post.
- `research/TIEOUT.md`: every headline number, recomputed from `data/` by `scripts/build.py`.
- `posts/supertanker-rates/`: the post text (`POST.md`) and its images.

## Data sources

| Series | Publisher | Details |
|---|---|---|
| TD3C round-trip time charter equivalent (TCE), $/day | Baltic Exchange, London | Ras Tanura to Ningbo, weekly tanker report, Fridays, from December 2020 |
| VLCC Middle East Gulf to Far East | Fearnleys, Oslo | Daily; dollars per day from March 2019 to April 2023, Worldscale points to today |
| VLCC US Gulf to Asia, lump sum per cargo | Fearnleys | Daily |
| Europe Brent spot price, FOB (series RBRTE) | U.S. Energy Information Administration (EIA) | Weekly and daily, from 2018 |
| WTI Cushing spot (RWTC) and NYMEX WTI contract 1 (RCLC1) | U.S. Energy Information Administration (EIA) | Daily, used as a cross-check |
| ICE Brent and NYMEX WTI front-month futures | ICE and NYMEX, daily closes via Yahoo Finance | Daily |
| 2008 to 2009 background | Baltic Dirty Tanker Index; Drewry via UNCTAD; OSG and Frontline company reports | Monthly and quarterly, see `research/NOTES.md` |

The Baltic site blocks scripted downloads. `scripts/update.py` reads each weekly report through a reader proxy first, then through mirrors (Hellenic Shipping News and the Wayback Machine). If none has the report, the rate can be entered by hand from the report text.

## How to rebuild

Requirements: Python 3 in a virtual environment at `.venv/`, with `matplotlib` for the static images. The fetch scripts load settings through a private helper (`d4tp_env.py`) and an env file kept outside this repo.

- `EIA_API_KEY`: an EIA API key is needed for the Brent fetch scripts.
- `D4TP_CONTACT_EMAIL`: optional contact address for the User-Agent header.

Weekly update, in order (this is what `scripts/weekly.sh` runs):

```sh
.venv/bin/python3 scripts/fetch_brent.py                        # EIA weekly Brent
.venv/bin/python3 scripts/fetch_brent_physical_vs_futures.py    # daily spot vs futures
.venv/bin/python3 scripts/update.py                             # Fearnleys + this week's Baltic row, then rebuild
```

If the Baltic row cannot be fetched, pass it by hand from the report:

```sh
.venv/bin/python3 scripts/update.py --date YYYY-MM-DD --ws <worldscale> --tce <dollars_per_day>
```

To rebuild from the data already in `data/` without adding a row:

```sh
.venv/bin/python3 scripts/fetch_fearnleys.py
.venv/bin/python3 scripts/build.py          # writes dist/ and research/TIEOUT.md
```

Static images for the post:

```sh
.venv/bin/python3 scripts/static_chart.py        # weekly earnings chart PNG
.venv/bin/python3 scripts/landed_cost_table.py   # landed cost table PNG
```

`scripts/build_baltic_csv.py` assembled the original Baltic file from archived report pages. Its inputs are not in the repo, so it is kept as a record of how the file was built.

## Method notes

- The chart uses dollars per day (the time charter equivalent) rather than Worldscale points, because the Worldscale base rate is reset every January and points are only roughly comparable across years.
- Two lines are drawn: the Baltic Exchange TD3C series and the Fearnleys series. Fearnleys stopped publishing the dollar figure in April 2023.
- A Baltic dollar figure the report did not state is left blank, never estimated, unless a note in the data file says so. Interpolated weeks are flagged in the data. Where a report gives a range, the midpoint is used.
- Since March 2026 the TD3C rate is an assessment for a voyage that loads inside the Strait of Hormuz, which few ships are making. Cargoes that load just outside it pay less.
- The landed cost table in the post is an editorial estimate for mid-September 2026. Its figures are typed in `scripts/landed_cost_table.py`, with sources in `research/NOTES.md`.

Data 4 The People
