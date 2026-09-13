#!/usr/bin/env python3
"""Assemble data/baltic_td3c_weekly.csv, the Baltic Exchange TD3C weekly series.

Two inputs, both hand-checked against the Baltic weekly tanker report text:
  * scratch/wayback_rows.json  parsed from Wayback Machine captures of the
    Baltic report, Dec 2020 to Dec 2021 (the report started quoting a TCE on
    Dec 4, 2020). OVERRIDES below fix the rows the regex misread, taken from
    a manual read of each report's VLCC paragraph.
  * scratch/td3c_vlcc_weekly_2022_2026.csv  pulled report-by-report from the
    Baltic site in the Sept 12, 2026 desktop session, Jan 2022 to Sept 2026.

Rule: one row per Baltic report date, never a duplicate. A TCE the report
did not state is left blank, never estimated, unless the note says so.
"""
import csv, json, sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
SCR = ROOT / "scratch"
OUT = ROOT / "data" / "baltic_td3c_weekly.csv"

# date -> (ws, tce, note). Midpoint used where the report gives a range.
OVERRIDES = {
    "2020-12-04": (31, 11500, "first report to state a TCE"),
    "2020-12-11": (34, None, "TCE not stated"),
    "2020-12-18": (35, None, "TCE not stated"),
    "2021-01-08": (40.5, None, "TCE not stated; 2021 Worldscale flat rates fell about 17%"),
    "2021-01-15": (35, None, "'just below WS35'; TCE not stated"),
    "2021-01-29": (32.5, None, "'just about a positive TCE'; not stated"),
    "2021-02-12": (31.5, None, "TCE not stated"),
    "2021-02-19": (32.75, None, "WS32.5/33 midpoint; TCE not stated"),
    "2021-03-12": (28.25, -6000, "WS28-28.5 midpoint"),
    "2021-04-09": (31.5, -500, "'about $500 below zero'"),
    "2021-05-07": (32.75, 800, "WS32.5/33 midpoint"),
    "2021-05-28": (36.25, 3250, "WS36-36.5 midpoint"),
    "2021-06-04": (34.25, -100, "WS34-34.5 midpoint"),
    "2021-07-02": (31.75, -4600, "WS31.5-32 midpoint"),
    "2021-07-09": (31.75, -5000, "WS31.5-32 midpoint"),
    "2021-08-20": (31.32, -3164, ""),
    "2021-09-03": (34, -2000, "'just shy of WS34'"),
    "2021-09-24": (39, 1900, ""),
    "2021-10-08": (40.75, 1700, "WS40.5-41 midpoint"),
}

def iso_week(d):
    y, w, _ = date.fromisoformat(d).isocalendar()
    return f"{y}-{w}"

rows = {}
for d, ws, tce, seg, url in json.load(open(SCR / "wayback_rows.json")):
    if d in OVERRIDES:
        ws, tce, note = OVERRIDES[d]
    else:
        note = ""
        if ws is None:
            sys.exit(f"no WS parsed for {d} and no override")
        ws = float(ws)
    rows[d] = dict(date=d, week=iso_week(d), ws=ws, tce_usd_day=tce, source=url, note=note)

with open(SCR / "td3c_vlcc_weekly_2022_2026.csv") as f:
    for r in csv.DictReader(f):
        if r["date"] in rows:
            sys.exit(f"duplicate date {r['date']}")
        y, w = r["week"].split("-")
        url = f"https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/{y}/tanker-report-week-{int(w)}.html"
        rows[r["date"]] = dict(date=r["date"], week=r["week"], ws=float(r["ws"]),
                               tce_usd_day=int(float(r["tce_usd_day"])), source=url, note=r["note"])

out = sorted(rows.values(), key=lambda r: r["date"])
weeks = [r["week"] for r in out]
if len(weeks) != len(set(weeks)):
    dups = {w for w in weeks if weeks.count(w) > 1}
    sys.exit(f"duplicate ISO weeks: {dups}")
with OUT.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["date", "week", "ws", "tce_usd_day", "source", "note"])
    w.writeheader()
    for r in out:
        r = dict(r); r["ws"] = f"{r['ws']:g}"; r["tce_usd_day"] = "" if r["tce_usd_day"] is None else r["tce_usd_day"]
        w.writerow(r)
n_tce = sum(1 for r in out if r["tce_usd_day"] is not None)
print(f"wrote {OUT.name}: {len(out)} rows {out[0]['date']} to {out[-1]['date']}, {n_tce} with TCE")
