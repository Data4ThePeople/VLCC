#!/usr/bin/env python3
"""Pull the Fearnleys VLCC Middle East Gulf to Far East assessments.

Source: Fearnleys market data backend behind fearnpulse.com (public GraphQL).
Series 340 = Worldscale points (daily, May 2018 to present).
Series 342 = time charter equivalent, US dollars per day (daily, May 2018 to
April 25, 2023, when Fearnleys stopped publishing the TCE branch).

Writes data/fearnleys_vlcc_meg_feast_daily.csv with one row per date.
"""
import csv, json, sys, urllib.request
from pathlib import Path

ENDPOINT = "https://pbrokerapp.hasura.app/v1/graphql"
SERIES = {"ws": 340, "tce_usd_day": 342}
OUT = Path(__file__).resolve().parent.parent / "data" / "fearnleys_vlcc_meg_feast_daily.csv"

def fetch(meta_id):
    q = ('query { rate_meta(where:{id:{_eq:%d}}) { id rate_unit '
         'info { rate_type rate_subtype route } rates(order_by:{date:asc}) { date rate } } }' % meta_id)
    req = urllib.request.Request(ENDPOINT, data=json.dumps({"query": q}).encode(),
        headers={"Content-Type": "application/json", "Origin": "https://fearnpulse.com",
                 "User-Agent": "Mozilla/5.0 (Data 4 The People research; eric@asaltollc.com)"})
    d = json.load(urllib.request.urlopen(req, timeout=120))
    if "errors" in d:
        sys.exit(f"GraphQL error: {d['errors']}")
    m = d["data"]["rate_meta"][0]
    assert m["info"]["rate_subtype"] == "VLCC" and m["info"]["route"] == "MEG/FEAST", m["info"]
    return {r["date"]: r["rate"] for r in m["rates"] if r["rate"] is not None}

def main():
    cols = {k: fetch(v) for k, v in SERIES.items()}
    dates = sorted(set().union(*[set(c) for c in cols.values()]))
    if len(dates) != len(set(dates)):
        sys.exit("duplicate dates")  # hard failure by house rule
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["date", "ws", "tce_usd_day"])
        for d in dates:
            w.writerow([d, cols["ws"].get(d, ""), cols["tce_usd_day"].get(d, "")])
    print(f"wrote {OUT.name}: {len(dates)} rows, {dates[0]} to {dates[-1]}; "
          f"ws n={len(cols['ws'])}, tce n={len(cols['tce_usd_day'])} "
          f"(tce last {max(cols['tce_usd_day'])})")

if __name__ == "__main__":
    main()
