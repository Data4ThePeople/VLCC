#!/usr/bin/env python3
"""Weekly update. Run on or after the Friday Baltic tanker report.

    python3 scripts/update.py                      # try to fetch this week automatically
    python3 scripts/update.py --date 2026-09-18 --ws 850.5 --tce 905000
    python3 scripts/update.py --date 2026-09-18 --ws 850.5 --tce 905000 --note "..."

What it does
  1. Refreshes the Fearnleys daily file (open API, always works).
  2. Adds one Baltic TD3C row for the report date. The Baltic site blocks
     scripted downloads, so the automatic path tries two mirrors that do not:
     Hellenic Shipping News, which sometimes republishes the report, and the
     Wayback Machine. If neither has it, open the report in a browser and pass
     --ws and --tce from the VLCC paragraph ("270,000mt Middle East Gulf to
     China ... WS xxx ... round-trip TCE of $yyy"). The Claude desktop app's
     in-app browser can also read the page.
  3. Rebuilds dist/ and the tie-out. A duplicate report date is a hard stop.

Baltic report URL pattern (ISO week number of the Friday):
  https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/<year>/tanker-report-week-<n>.html
"""
import argparse, csv, html as htmlmod, json, re, subprocess, sys, urllib.request
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BALTIC = ROOT / "data" / "baltic_td3c_weekly.csv"
UA = {"User-Agent": "Mozilla/5.0 (Data 4 The People research; eric@asaltollc.com)"}


def last_friday(today=None):
    d = today or date.today()
    return d - timedelta(days=(d.weekday() - 4) % 7)


def report_url(d):
    y, w, _ = d.isocalendar()
    return f"https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/{y}/tanker-report-week-{w}.html"


def strip(h):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = htmlmod.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"\s+", " ", t)


def parse_vlcc(text):
    """Return (ws, tce) from the report's TD3C sentence, or None.

    The Baltic sentence looks like "270,000mt Middle East Gulf to China (TD3C)
    ... WS216.89 which corresponds to a daily round-trip TCE of $209,550" or
    "270,000mt to China eased 1.5 points to WS28-28.5 (a TCE of minus $6,000/day)".
    A Worldscale range is read as its midpoint.
    """
    i = text.find("VLCC")
    if i < 0:
        return None
    j = text.find("Suezmax", i)
    para = text[i:j if j > i else i + 2500]
    para = para.split("In the Atlantic")[0]
    sents = re.split(r"(?<=[a-z\)])\. (?=[A-Z])", para)
    sent = next((s for s in sents if "270,000" in s and "China" in s), None)
    if not sent:
        sent = next((s for s in sents if "TD3C" in s), None)
    if not sent:
        return None
    k = sent.find("China", sent.find("270,000"))
    if k < 0:
        k = sent.find("China")
    seg = sent[k:]
    for stop in (" for 280,000", " while ", " whilst ", "260,000", "West Africa", "US Gulf"):
        cut = seg.find(stop)
        if cut > 0:
            seg = seg[:cut]
    wsre = r"\bW[S]?\s?(\d{2,4}(?:\.\d+)?)(?:\s?[-/]\s?(\d{2,4}(?:\.\d+)?))?"
    m = re.search(wsre, seg)
    if m:
        after = seg[m.end():]
    else:                                   # "WS31 (about $11,500 per day) for 270,000mt ME Gulf to China"
        before = sent[:sent.find("270,000")]
        ms = list(re.finditer(wsre, before))
        if not ms:
            return None
        m = ms[-1]
        after = before[m.end():]
    ws = float(m.group(1))
    if m.group(2) and 0 < float(m.group(2)) - ws <= 5:
        ws = (ws + float(m.group(2))) / 2
    money = r"(minus\s+|-\s?)?\$\s?(-?)\s?(\d[\d,]*(?:\.\d+)?)\s*(k)?"
    t = None
    for kw in ("TCE", "equivalent", "per day", "/day"):
        ti = after.find(kw)
        if ti >= 0:
            t = re.search(money, after[max(0, ti - 24 if kw in ("per day", "/day") else ti):])
            if t:
                break
    tce = None
    if t:
        v = float(t.group(3).replace(",", ""))
        if t.group(4):
            v *= 1000
        if t.group(1) or t.group(2):
            v = -v
        tce = int(round(v))
    return ws, tce


def fetch(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read().decode("utf-8", "ignore")


def try_hsn(d):
    y, w, _ = d.isocalendar()
    q = f"https://www.hellenicshippingnews.com/?s=%22tanker+report%22+week+{w}"
    try:
        h = fetch(q)
    except Exception:
        return None
    for u in re.findall(r'https://www\.hellenicshippingnews\.com/tanker-report-week-\d+[-\d]*/', h):
        try:
            t = strip(fetch(u))
        except Exception:
            continue
        m = re.search(r"(\d{1,2}/\d{2}/\d{4})", t)
        if m:
            dd, mm, yy = m.group(1).split("/")
            if date(int(yy), int(mm), int(dd)) - d > timedelta(days=6) or date(int(yy), int(mm), int(dd)) < d:
                continue
        r = parse_vlcc(t)
        if r:
            print(f"  found on Hellenic Shipping News: {u}")
            return r, u
    return None


def try_wayback(d):
    u = report_url(d)
    try:
        j = json.loads(fetch(f"http://archive.org/wayback/available?url={u}"))
        snap = j.get("archived_snapshots", {}).get("closest")
        if not snap:
            return None
        t = strip(fetch(snap["url"].replace("/web/", "/web/").replace("http://", "https://")))
        r = parse_vlcc(t)
        if r:
            print(f"  found on the Wayback Machine: {snap['url']}")
            return r, snap["url"]
    except Exception as e:
        print(f"  wayback: {e}")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="Friday of the Baltic report, YYYY-MM-DD (default: last Friday)")
    ap.add_argument("--ws", type=float)
    ap.add_argument("--tce", type=float, help="round-trip TCE in dollars per day")
    ap.add_argument("--note", default="")
    ap.add_argument("--skip-fearnleys", action="store_true")
    a = ap.parse_args()

    if not a.skip_fearnleys:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "fetch_fearnleys.py")], check=True)

    d = date.fromisoformat(a.date) if a.date else last_friday()
    rows = list(csv.DictReader(BALTIC.open()))
    if any(r["date"] == d.isoformat() for r in rows):
        sys.exit(f"{d} is already in {BALTIC.name}; nothing added")
    y, w, _ = d.isocalendar()
    if any(r["week"] == f"{y}-{w}" for r in rows):
        sys.exit(f"ISO week {y}-{w} is already in {BALTIC.name}; nothing added")

    src = report_url(d)
    if a.ws is not None and a.tce is not None:
        ws, tce = a.ws, int(a.tce)
        note = a.note or "entered by hand from the Baltic report"
    else:
        print(f"looking for the Baltic report of {d} ...")
        got = try_hsn(d) or try_wayback(d)
        if not got:
            sys.exit(f"could not fetch the report for {d}. Open {src} and rerun with --ws and --tce.")
        (ws, tce), src = got
        if tce is None:
            sys.exit(f"found WS {ws} but no TCE in the text; rerun with --ws {ws} --tce <value>")
        note = a.note
    last = rows[-1]
    if last["tce_usd_day"] and abs(tce - float(last["tce_usd_day"])) > 0.6 * max(abs(float(last["tce_usd_day"])), 50000):
        print(f"  warning: {tce:,} is far from last week's {float(last['tce_usd_day']):,.0f}; check the report")
    with BALTIC.open("a", newline="") as f:
        csv.writer(f).writerow([d.isoformat(), f"{y}-{w}", f"{ws:g}", tce, src, note])
    print(f"added {d}: WS {ws:g}, ${tce:,} a day")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py")], check=True)


if __name__ == "__main__":
    main()
