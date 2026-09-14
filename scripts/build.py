#!/usr/bin/env python3
"""Build the interactive chart and the tie-out from the two data files.

Inputs
  data/baltic_td3c_weekly.csv           Baltic Exchange TD3C, weekly (Fridays)
  data/fearnleys_vlcc_meg_feast_daily.csv  Fearnleys VLCC MEG/Far East, daily

Outputs
  dist/index.html    self-contained page, data inlined, no CDN
  dist/data.json     the same weekly series as JSON
  research/TIEOUT.md every headline number, recomputed here

Nothing is hardcoded in the page: the template carries a /*__DATA__*/ slot
and every figure on the page is computed from the inlined data at render time.
"""
import csv, json, sys
from collections import OrderedDict
from datetime import date, timedelta
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent
BALTIC = ROOT / "data" / "baltic_td3c_weekly.csv"
FEARN = ROOT / "data" / "fearnleys_vlcc_meg_feast_daily.csv"
BRENT = ROOT / "data" / "brent_weekly.csv"
CRUDE = ROOT / "data" / "crude_spot_vs_futures_daily.csv"
TEMPLATE = ROOT / "scripts" / "template.html"
DIST = ROOT / "dist"
TIEOUT = ROOT / "research" / "TIEOUT.md"

FEARN_TCE_START = "2019-03-13"   # zeros before this are placeholders, not earnings


def num(s):
    return None if s in ("", None) else float(s)


def load_baltic():
    rows = list(csv.DictReader(BALTIC.open()))
    dates = [r["date"] for r in rows]
    weeks = [r["week"] for r in rows]
    if len(set(dates)) != len(dates) or len(set(weeks)) != len(weeks):
        sys.exit("baltic: duplicate date or week")   # hard failure by house rule
    out = []
    for r in rows:
        tce = num(r["tce_usd_day"])
        out.append(OrderedDict(d=r["date"], ws=num(r["ws"]),
                               tce=None if tce is None else int(tce),
                               note=r["note"] or None))
    return out


def load_fearnleys_weekly():
    """One point per ISO week: the Friday value, else the last trading day of
    the week. Worldscale from May 2018; dollars from March 13, 2019."""
    rows = list(csv.DictReader(FEARN.open()))
    if len({r["date"] for r in rows}) != len(rows):
        sys.exit("fearnleys: duplicate date")
    byweek = OrderedDict()
    for r in rows:
        d = date.fromisoformat(r["date"])
        if d.weekday() >= 5:
            continue                       # weekend rows repeat Friday
        ws = num(r["ws"])
        if ws == 0:
            ws = None                      # year-end placeholder rows
        tce = num(r["tce_usd_day"])
        if r["date"] < FEARN_TCE_START or ws is None:
            tce = None
        key = d.isocalendar()[:2]
        byweek[key] = OrderedDict(d=r["date"], ws=ws, tce=None if tce is None else int(tce))
    return [v for v in byweek.values() if v["ws"] is not None or v["tce"] is not None]


def load_brent():
    rows = list(csv.DictReader(BRENT.open()))
    if len({r["date"] for r in rows}) != len(rows):
        sys.exit("brent: duplicate week")
    return [OrderedDict(d=r["date"], usd=float(r["brent_usd_bbl"])) for r in rows]


def load_crude_daily():
    """Daily physical Brent (EIA spot) and ICE front-month futures closes."""
    spot, fut = [], []
    seen = set()
    for r in csv.DictReader(CRUDE.open()):
        if r["date"] in seen:
            sys.exit("crude daily: duplicate date")
        seen.add(r["date"])
        if r["brent_spot_eia"]:
            spot.append(OrderedDict(d=r["date"], usd=float(r["brent_spot_eia"])))
        if r["brent_fut1_yahoo"]:
            fut.append(OrderedDict(d=r["date"], usd=float(r["brent_fut1_yahoo"])))
    return spot, fut


def fmt(v):
    return "n/a" if v is None else f"${v:,.0f}"


def tieout(baltic, fearn, fearn_daily, brent, spot, fut):
    b = {r["d"]: r for r in baltic}
    f = {r["d"]: r for r in fearn}
    lines = ["# Tie-out", "",
             "Every number below is recomputed from `data/` by `scripts/build.py`.",
             "Dates are the Friday of the Baltic weekly report unless stated.", ""]
    L = lines.append
    latest = baltic[-1]
    L(f"- Latest Baltic TD3C: {latest['d']}, WS {latest['ws']:g}, {fmt(latest['tce'])} a day.")
    bt = [r for r in baltic if r["tce"] is not None]
    pk = max(bt, key=lambda r: r["tce"])
    L(f"- Baltic weekly high: {pk['d']}, {fmt(pk['tce'])} a day.")
    for d in ("2026-02-27", "2026-03-06"):
        L(f"- Baltic {d}: WS {b[d]['ws']:g}, {fmt(b[d]['tce'])} a day.")
    jun = min((r for r in bt if "2026-05-01" <= r["d"] <= "2026-07-31"), key=lambda r: r["tce"])
    L(f"- Baltic 2026 low between May and July: {jun['d']}, {fmt(jun['tce'])} a day.")
    spring = [r for r in bt if "2026-03-06" <= r["d"] <= "2026-07-31"]
    L(f"- Baltic Mar 6 to Jul 31, 2026 range: {fmt(min(r['tce'] for r in spring))} to "
      f"{fmt(max(r['tce'] for r in spring))} a day.")
    avg = [r["tce"] for r in bt if "2022-01-01" <= r["d"] <= "2025-12-31"]
    L(f"- Baltic 2022 to 2025 average: {fmt(mean(avg))} a day over {len(avg)} weeks.")
    pre = [r for r in bt if r["d"] < "2026-01-01"]
    pm = max(pre, key=lambda r: r["tce"])
    L(f"- Baltic weekly high before 2026: {pm['d']}, {fmt(pm['tce'])} a day.")
    L(f"- Baltic first reading: {baltic[0]['d']}; first with a dollar figure: {bt[0]['d']}.")
    L(f"- Baltic weeks with TCE: {len(bt)} of {len(baltic)} rows; "
      f"flagged rows: {sum(1 for r in baltic if r['note'])}.")
    # gaps in Baltic weekly coverage
    gaps = []
    for a, c in zip(baltic, baltic[1:]):
        da, dc = date.fromisoformat(a["d"]), date.fromisoformat(c["d"])
        if (dc - da).days > 7:
            gaps.append(f"{a['d']} to {c['d']}")
    L(f"- Baltic gaps longer than a week: {len(gaps)}: " + "; ".join(gaps))
    L("")
    ft = [r for r in fearn if r["tce"] is not None]
    L(f"- Fearnleys dollar series: {ft[0]['d']} to {ft[-1]['d']}, {len(ft)} weekly points.")
    L(f"- Fearnleys Worldscale series: {fearn[0]['d']} to {fearn[-1]['d']}, {len(fearn)} weekly points; latest WS {fearn[-1]['ws']:g}.")
    for y in ("2019", "2020"):
        wk = max((r for r in ft if r["d"].startswith(y)), key=lambda r: r["tce"])
        dy = max((r for r in fearn_daily if r["date"].startswith(y) and r["tce_usd_day"] not in ("", "0")),
                 key=lambda r: float(r["tce_usd_day"]))
        L(f"- Fearnleys {y} high: weekly {wk['d']} {fmt(wk['tce'])}; daily {dy['date']} {fmt(float(dy['tce_usd_day']))}.")
    ov = [(d, b[d]["tce"], f[d]["tce"]) for d in b if d in f and b[d]["tce"] is not None and f[d]["tce"] is not None]
    diffs = [abs(x - y) for _, x, y in ov]
    L(f"- Overlap weeks with both dollar figures: {len(ov)} ({ov[0][0]} to {ov[-1][0]}); "
      f"median absolute gap {fmt(sorted(diffs)[len(diffs)//2])}, max {fmt(max(diffs))}.")
    ovw = [(abs(b[d]["ws"] - f[d]["ws"])) for d in b if d in f and f[d]["ws"] is not None and b[d]["ws"] is not None and d <= "2023-04-28"]
    L(f"- Overlap Worldscale gap through Apr 2023: median {sorted(ovw)[len(ovw)//2]:.2f} points, max {max(ovw):.2f}.")
    L("")
    br = {r["d"]: r["usd"] for r in brent}
    def near_b(d):
        dd = date.fromisoformat(d)
        for k in range(0, 4):
            for c in (dd - timedelta(days=k), dd + timedelta(days=k)):
                if c.isoformat() in br: return c.isoformat(), br[c.isoformat()]
        return None, None
    L(f"- Brent weekly (EIA RBRTE): {brent[0]['d']} to {brent[-1]['d']}; latest ${brent[-1]['usd']:.2f} a barrel.")
    for y in ("2022", "2026"):
        hi = max((r for r in brent if r["d"].startswith(y)), key=lambda r: r["usd"])
        bd = min(bt, key=lambda r: abs(date.fromisoformat(r["d"]) - date.fromisoformat(hi["d"])))
        L(f"- Brent {y} high: {hi['d']} ${hi['usd']:.2f}; Baltic TD3C that week ({bd['d']}): {fmt(bd['tce'])} a day.")
    w22 = [r for r in bt if "2022-02-25" <= r["d"] <= "2022-07-01"]
    L(f"- Baltic Feb 25 to Jul 1, 2022 (invasion to Brent peak): average {fmt(mean(r['tce'] for r in w22))} a day, "
      f"range {fmt(min(r['tce'] for r in w22))} to {fmt(max(r['tce'] for r in w22))}, {sum(1 for r in w22 if r['tce'] < 0)} of {len(w22)} weeks negative.")
    neg = [r for r in bt if r["tce"] < 0]
    L(f"- Baltic weeks below zero: {len(neg)}, from {neg[0]['d']} to {neg[-1]['d']}.")
    h22 = [r for r in bt if "2022-10-01" <= r["d"] <= "2022-12-31"]
    L(f"- Baltic Oct to Dec 2022 high: {fmt(max(r['tce'] for r in h22))} a day ({max(h22, key=lambda r: r['tce'])['d']}).")
    d26, v26 = near_b("2026-02-27"); L(f"- Brent week of Feb 27, 2026: ${v26:.2f} ({d26}); week of Sep 4, 2026: ${br.get('2026-09-04', float('nan')):.2f}.")
    L("")
    fm = {r["d"]: r["usd"] for r in fut}
    pairs = [(r["d"], r["usd"], fm[r["d"]]) for r in spot if r["d"] in fm]
    wide = max(pairs, key=lambda x: x[1] - x[2]); last = pairs[-1]
    L(f"- Brent physical vs futures: {len(pairs)} matched days {pairs[0][0]} to {last[0]}; widest gap {wide[0]} spot ${wide[1]:.2f} vs futures ${wide[2]:.2f} = +${wide[1]-wide[2]:.2f}; latest {last[0]} ${last[1]:.2f} vs ${last[2]:.2f} = {last[1]-last[2]:+.2f}.")
    for y in ("2022", "2026"):
        ys = [x for x in pairs if x[0].startswith(y)]
        L(f"- Brent physical minus futures {y}: average {sum(x[1]-x[2] for x in ys)/len(ys):+.2f}, widest {max(x[1]-x[2] for x in ys):+.2f} on {max(ys, key=lambda x: x[1]-x[2])[0]}.")
    L("")
    L("Cross-series comparisons are editorial, not published: the Sept 2026 Baltic high "
      f"is {pk['tce']/326000:.1f} times the Baltic TD3C March 2020 peak quoted by Hellenic "
      f"Shipping News (above $326,000) and {pk['tce']/300391:.1f} times the Oct 11, 2019 "
      "Baltic figure quoted by Lloyd's List ($300,391).")
    return "\n".join(lines) + "\n"


def main():
    baltic = load_baltic()
    fearn = load_fearnleys_weekly()
    fearn_daily = list(csv.DictReader(FEARN.open()))
    brent = load_brent()
    spot, fut = load_crude_daily()
    data = OrderedDict(
        built=date.today().isoformat(),
        baltic=OrderedDict(name="Baltic Exchange TD3C", publisher="Baltic Exchange",
                           route="Ras Tanura to Ningbo, 270,000 tonnes, round-trip TCE",
                           unit="US dollars per day", points=baltic),
        fearnleys=OrderedDict(name="Fearnleys VLCC MEG/Far East", publisher="Fearnleys",
                              route="Middle East Gulf to Far East, TCE",
                              unit="US dollars per day", points=fearn),
        brent=OrderedDict(name="Brent crude oil spot price", publisher="U.S. Energy Information Administration",
                          route="Europe Brent spot price FOB, weekly (series RBRTE)",
                          unit="US dollars per barrel", points=brent),
        brent_spot=OrderedDict(name="Brent physical (Dated Brent) spot price", publisher="U.S. Energy Information Administration",
                               route="Europe Brent spot price FOB, daily (series RBRTE)",
                               unit="US dollars per barrel", points=spot),
        brent_fut=OrderedDict(name="ICE Brent front-month futures", publisher="ICE, daily closes via Yahoo Finance (BZ=F)",
                              route="front-month contract, daily close",
                              unit="US dollars per barrel", points=fut),
    )
    DIST.mkdir(exist_ok=True)
    (DIST / "data.json").write_text(json.dumps(data, indent=1))
    tpl = TEMPLATE.read_text()
    if "/*__DATA__*/" not in tpl:
        sys.exit("template has no data slot")
    import base64
    logo = (ROOT / "logo" / "d4tp-text-dark.svg").read_bytes()
    logo_uri = "data:image/svg+xml;base64," + base64.b64encode(logo).decode()
    html = (tpl.replace("/*__DATA__*/", "const DATA = " + json.dumps(data, separators=(",", ":")) + ";")
               .replace("__LOGO__", logo_uri))
    (DIST / "index.html").write_text(html)
    TIEOUT.write_text(tieout(baltic, fearn, fearn_daily, brent, spot, fut))
    print(f"dist/index.html {len(html)//1024} KB; baltic {len(baltic)} weeks, fearnleys {len(fearn)} weeks")
    print(TIEOUT.read_text())


if __name__ == "__main__":
    main()
