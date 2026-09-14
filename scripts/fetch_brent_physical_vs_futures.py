#!/usr/bin/env python3
"""Daily physical (spot) crude prices against the front-month futures screen.

Physical: EIA daily spot assessments, Europe Brent FOB (RBRTE) and WTI
Cushing (RWTC). Futures: ICE Brent front month (BZ=F) and NYMEX WTI front
month (CL=F) daily closes as relayed by Yahoo Finance; EIA's own NYMEX WTI
contract 1 series (RCLC1) is pulled too as the official cross-check.
Writes data/crude_spot_vs_futures_daily.csv from 2018.
"""
import csv, json, os, sys, urllib.parse, urllib.request, datetime
from pathlib import Path
sys.path.insert(0, os.path.expanduser("~/.claude/d4tp-process"))
from d4tp_env import load_env, get_key

OUT = Path(__file__).resolve().parent.parent / "data" / "crude_spot_vs_futures_daily.csv"
UA = {"User-Agent": "Mozilla/5.0 (Data 4 The People research; eric@asaltollc.com)"}

def eia(series, path):
    load_env()
    out = {}
    offset = 0
    while True:
        u = f"https://api.eia.gov/v2/petroleum/pri/{path}/data/?" + urllib.parse.urlencode({
            "api_key": get_key("EIA_API_KEY"), "frequency": "daily", "data[0]": "value",
            "facets[series][]": series, "start": "2018-01-01",
            "sort[0][column]": "period", "sort[0][direction]": "asc", "length": 5000, "offset": offset})
        rows = json.load(urllib.request.urlopen(u, timeout=90))["response"]["data"]
        for r in rows:
            if r["value"] is not None:
                out[r["period"]] = float(r["value"])
        if len(rows) < 5000:
            break
        offset += 5000
    return out

def yahoo(sym):
    import time
    u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d"
         f"&period1=1514764800&period2={int(time.time())}")
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
    r = d["chart"]["result"][0]
    ts, c = r["timestamp"], r["indicators"]["quote"][0]["close"]
    return {datetime.datetime.utcfromtimestamp(t).date().isoformat(): round(v, 2)
            for t, v in zip(ts, c) if v is not None and t >= 1514764800}

def main():
    cols = {
        "brent_spot_eia": eia("RBRTE", "spt"),
        "wti_spot_eia": eia("RWTC", "spt"),
        "wti_fut1_eia": eia("RCLC1", "fut"),
        "brent_fut1_yahoo": yahoo("BZ=F"),
        "wti_fut1_yahoo": yahoo("CL=F"),
    }
    dates = sorted(set().union(*[set(c) for c in cols.values()]))
    with OUT.open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["date"] + list(cols))
        for d in dates:
            w.writerow([d] + [cols[k].get(d, "") for k in cols])
    for k, v in cols.items():
        ks = sorted(v); print(f"{k}: {len(v)} days, {ks[0]} to {ks[-1]}, latest {v[ks[-1]]}")
    print(f"wrote {OUT.name}: {len(dates)} rows")

if __name__ == "__main__":
    main()
