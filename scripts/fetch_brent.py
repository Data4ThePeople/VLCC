#!/usr/bin/env python3
"""Weekly Europe Brent spot price (FOB), dollars per barrel, from the EIA API.
Series RBRTE, weekly (each row is the Friday of that week). From 2018.
Writes data/brent_weekly.csv. Needs EIA_API_KEY from the central .env."""
import csv, json, os, sys, urllib.parse, urllib.request
from pathlib import Path
sys.path.insert(0, os.path.expanduser("~/.claude/d4tp-process"))
from d4tp_env import load_env, get_key

OUT = Path(__file__).resolve().parent.parent / "data" / "brent_weekly.csv"

def main():
    load_env()
    url = "https://api.eia.gov/v2/petroleum/pri/spt/data/?" + urllib.parse.urlencode({
        "api_key": get_key("EIA_API_KEY"), "frequency": "weekly", "data[0]": "value",
        "facets[series][]": "RBRTE", "start": "2018-01-01",
        "sort[0][column]": "period", "sort[0][direction]": "asc", "length": 5000})
    rows = json.load(urllib.request.urlopen(url, timeout=90))["response"]["data"]
    dates = [r["period"] for r in rows]
    if len(dates) != len(set(dates)):
        sys.exit("duplicate weeks in EIA response")
    with OUT.open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["date", "brent_usd_bbl"])
        for r in rows:
            if r["value"] is not None:
                w.writerow([r["period"], r["value"]])
    print(f"wrote {OUT.name}: {len(rows)} rows, {dates[0]} to {dates[-1]}, latest ${rows[-1]['value']}")

if __name__ == "__main__":
    main()
