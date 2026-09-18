#!/usr/bin/env python3
"""Static PNG of the same chart in the house dark palette, for Prismic and
Mailchimp. Reads dist/data.json so it can never disagree with the page.

    .venv/bin/python scripts/static_chart.py
Writes posts/supertanker-rates/images/01-vlcc-earnings-weekly.png.
"""
import json
from datetime import date
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parent.parent
D = json.loads((ROOT / "dist" / "data.json").read_text())
OUT = ROOT / "posts" / "supertanker-rates" / "images" / "01-vlcc-earnings-weekly.png"
OUT.parent.mkdir(exist_ok=True)

BG, INK, MUTED, GRID = "#181A1B", "#BBBDC0", "#8f9296", "#2c2f31"
BALTIC, FEARN = "#7fb0cf", "#e0895a"

def series(pts):
    xs, ys = [], []
    prev = None
    for p in pts:
        if p["tce"] is None:
            continue
        d = date.fromisoformat(p["d"])
        if prev and (d - prev).days > 21:       # break the line across a gap
            xs.append(d); ys.append(float("nan"))
        xs.append(d); ys.append(p["tce"]); prev = d
    return xs, ys

plt.rcParams.update({"font.family": "serif", "font.serif": ["Georgia", "DejaVu Serif"],
                     "text.color": INK, "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
fx, fy = series(D["fearnleys"]["points"]); bx, by = series(D["baltic"]["points"])
ax.plot(fx, fy, color=FEARN, lw=1.8, solid_joinstyle="round")
ax.plot(bx, by, color=BALTIC, lw=1.8, solid_joinstyle="round")
bt = [p for p in D["baltic"]["points"] if p["tce"] is not None]
latest = bt[-1]
ax.plot([date.fromisoformat(latest["d"])], [latest["tce"]], "o", color=BALTIC, ms=6, mec=BG, mew=1.5)
ax.annotate(f"${latest['tce']:,} a day\n{date.fromisoformat(latest['d']).strftime('%b %-d, %Y')}",
            (date.fromisoformat(latest["d"]), latest["tce"]), xytext=(-12, -4), textcoords="offset points",
            ha="right", va="top", fontsize=11, color=INK, fontweight="bold")

for ev, txt in [("2019-10-11", "Oct 2019: US sanctions\non COSCO tankers"),
                ("2020-03-13", "Mar 2020: price war,\noil stored at sea"),
                ("2026-02-28", "Feb 28, 2026: strikes on Iran,\nHormuz closes")]:
    d0 = date.fromisoformat(ev)
    cands = [(date.fromisoformat(p["d"]), p["tce"]) for s in ("baltic", "fearnleys") for p in D[s]["points"]
             if p["tce"] is not None and 0 <= (date.fromisoformat(p["d"]) - d0).days <= 21]
    if not cands:
        continue
    px, py = max(cands, key=lambda c: c[1])
    left = ev in ("2019-10-11", "2026-02-28")     # 2019 and 2026 labels sit up-left, 2020 up-right
    ax.annotate(txt, (px, py), xytext=(-12 if left else 14, 70 if ev != "2020-03-13" else 95), textcoords="offset points",
                ha="right" if left else "left", va="bottom", fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="-", color=GRID, lw=1))

ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v/1000:,.0f}k" if v else "$0"))
ax.xaxis.set_major_locator(mdates.YearLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.grid(axis="y", color=GRID, lw=0.8); ax.axhline(0, color=MUTED, lw=0.8)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.tick_params(length=0, labelsize=10.5)
ax.set_ylabel("US dollars per day", fontsize=10.5, color=MUTED)
fig.text(0.085, 0.955, "VLCC time charter rates, by the day", fontsize=17, fontweight="bold", color=INK, va="top")
fig.text(0.085, 0.905, "Weekly time charter rates for a very large crude carrier, Middle East to China, since 2019",
         fontsize=11.5, color=MUTED, va="top")
fb = [p for p in D["fearnleys"]["points"] if p["tce"] is not None]
def span(p): return f"{date.fromisoformat(p[0]['d']).strftime('%b %Y')} to {date.fromisoformat(p[-1]['d']).strftime('%b %Y')}"
fig.canvas.draw()
r = fig.canvas.get_renderer()
def put(x, y, txt, **kw):
    t = fig.text(x, y, txt, fontsize=10.5, **kw); return x + t.get_window_extent(r).width / fig.get_size_inches()[0] / fig.dpi
x = put(0.085, 0.04, "Baltic Exchange TD3C", color=BALTIC, fontweight="bold")
put(x + 0.006, 0.04, f"({span(bt)})", color=MUTED)
x = put(0.085, 0.012, "Fearnleys VLCC Middle East to Far East", color=FEARN, fontweight="bold")
put(x + 0.006, 0.012, f"({span(fb)})", color=MUTED)
fig.text(0.985, 0.012, "Built by Data 4 The People", color=MUTED, fontsize=10.5, ha="right")
fig.subplots_adjust(left=0.085, right=0.985, top=0.84, bottom=0.14)
fig.savefig(OUT, facecolor=BG)
print(f"wrote {OUT}")
