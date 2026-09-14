#!/usr/bin/env python3
"""Table image: what a barrel costs landed in China, mid-September 2026.
Figures are the editorial estimates in research/NOTES.md section 4l; this
script is the single place they are typed for the post.
    .venv/bin/python scripts/landed_cost_table.py
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent / "posts" / "supertanker-rates" / "images" / "02-landed-cost-table.png"
BG, INK, MUTED, GRID, HEAD = "#181A1B", "#BBBDC0", "#8f9296", "#2c2f31", "#e6e7e8"
ACCENT = "#7fb0cf"

cols = ["", "At the headline rate\n(loads inside the strait,\nBaltic TD3C $862,150 a day)", "The way the oil moves now\n(loads at Fujairah, outside\nthe strait, Murban)", "Atlantic barrel\n(US Gulf, for\ncomparison)"]
rows = [
    ("Price at the loading port", "$115", "$131", "$108"),
    ("Supertanker freight to China", "$18.60 to $22", "$8 to $11.50", "about $15"),
    ("War-risk cover on the ship, one transit", "$5 to $13", "about $1", "none"),
    ("War-risk cover on the oil itself", "$10 to $16*", "$0.65 to $1.30*", "none"),
    ("Landed in China", "$149 to $166", "$141 to $145", "about $123"),
    ("Round trip for the ship, days", "about 40", "about 38", "about 90"),
]

fig = plt.figure(figsize=(12, 6.9), dpi=150)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off(); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
plt.rcParams["font.family"] = "sans-serif"
esc = lambda t: t.replace("$", r"\$")   # keep matplotlib from reading $...$ as math
fig.text(0.05, 0.935, "What a barrel of oil really costs, landed in China", fontsize=19, fontweight="bold", color=HEAD, va="top")
fig.text(0.05, 0.878, "US dollars per barrel, mid-September 2026. Prices dated September 11 to 14; freight and insurance are ranges from published rates.",
         fontsize=10.5, color=MUTED, va="top")

x0, x1 = 0.05, 0.95
colx = [x0, 0.45, 0.62, 0.79]
top, bottom = 0.80, 0.16
hdr_h = 0.10
row_h = (top - hdr_h - bottom) / len(rows)
# header
for i, c in enumerate(cols):
    if i == 0: continue
    fig.text(colx[i] + 0.075, top - 0.012, c, fontsize=10.5, color=HEAD, ha="center", va="top", linespacing=1.25)
ax.plot([x0, x1], [top - hdr_h, top - hdr_h], color=GRID, lw=1)
y = top - hdr_h
for r, (label, *vals) in enumerate(rows):
    y -= row_h
    total = label.startswith("Landed")
    if total:
        ax.add_patch(plt.Rectangle((x0, y), x1 - x0, row_h, color="#222527", zorder=0))
    fig.text(colx[0], y + row_h / 2, esc(label), fontsize=10.5 if not total else 12, color=HEAD if total else INK,
             fontweight="bold" if total else "normal", va="center", wrap=True)
    for i, v in enumerate(vals, start=1):
        fig.text(colx[i] + 0.075, y + row_h / 2, esc(v), fontsize=11 if not total else 13, color=ACCENT if total else INK,
                 fontweight="bold" if total else "normal", ha="center", va="center")
    ax.plot([x0, x1], [y, y], color=GRID, lw=0.8)
fig.text(0.05, 0.115, "* Our estimate; no published rate. Cover on the oil itself is priced separately from cover on the ship. The headline rate is the Baltic\n"
         "Exchange's assessment for a 40-day round trip from Ras Tanura; freight is the day rate times the trip plus fuel and port costs, over 2 million barrels.",
         fontsize=9, color=MUTED, va="top", linespacing=1.35)
fig.text(0.05, 0.055, "Prices: ICE Futures Abu Dhabi (Murban), Platts (Dubai), ICE (Brent). Freight: Baltic Exchange, Bloomberg. Insurance: Lloyd's List, Marsh, Breakwave, Howden Re.",
         fontsize=9, color=MUTED, va="top")
fig.text(0.95, 0.018, "Built by Data 4 The People", fontsize=9.5, color=MUTED, va="bottom", ha="right")
fig.savefig(OUT, facecolor=BG)
print("wrote", OUT)
