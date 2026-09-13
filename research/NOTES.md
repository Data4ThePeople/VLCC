# Supertanker rates: research notes for the Data 4 Thought piece

Working notes for Eric, compiled September 13, 2026. Everything here is
background for the narrative. Numbers marked "chart" are recomputed from the
data files in `data/`; the rest carry a source link. Nothing in this file is
post text.

## 1. What the chart shows

**The measure.** What a very large crude carrier (VLCC) earns per day carrying
Middle East crude to China, in US dollars, one reading per week. Brokers call
this the time charter equivalent, or TCE: the voyage revenue minus fuel and port
costs, spread over the days of a round trip. It is the number the industry
quotes when it says "supertankers are earning $800,000 a day."

**Two published series, drawn as two lines.**

| Series | Publisher | Route | Coverage in $/day | Cadence |
|---|---|---|---|---|
| TD3C round-trip TCE | Baltic Exchange, London | Ras Tanura to Ningbo, 270,000 tonnes | Dec 4, 2020 to now | weekly report, Fridays |
| VLCC MEG/Far East TCE | Fearnleys, Oslo | Middle East Gulf to Far East | Mar 13, 2019 to Apr 25, 2023 | daily; we take Fridays |

The two overlap for about two and a half years and agree closely (chart:
Worldscale within about a point, earnings within a few thousand dollars a day
through 2022). Fearnleys stopped publishing the dollar figure in April 2023
when it changed its data layout. Fearnleys still publishes the Worldscale
points daily, from May 18, 2018 to now, and those are in `data/` too.

**Why the series starts in 2019, not earlier.** The Baltic's weekly report
quoted only Worldscale points before December 2020. The Fearnleys dollar
series starts in March 2019. Earlier history exists only behind paywalls
(Clarksons, Bloomberg) or as quotes in news reports. So: weekly dollars per day
from March 2019; the earlier spikes (2004, 2008) are covered by cited figures
in section 3, not by the chart.

**Worldscale, in one sentence.** Tanker freight is quoted as a percentage of a
reference rate for each route that is reset every January, so "WS 821" means
821% of that year's base rate. The base rate moves with fuel prices, so
Worldscale points are only roughly comparable across years. That is why the
chart uses dollars per day.

**Caveats that belong in the post.**

- Since March 2026 the Baltic's TD3C has been an assessment for a voyage few
  ships are making. The route loads at Ras Tanura, inside the Strait of
  Hormuz. The Baltic told Lloyd's List its panelists "can reference Yanbu
  fixtures but they need to apply a risk premium that the owner could accept
  to transit inside the Strait." A Signal Ocean analyst put it bluntly: "Does
  anybody pay such freights at the moment? Nope." Real Yanbu-to-China cargoes
  were paying about $13 a barrel against $18 implied by the index in
  mid-March. The index still matters because forward freight agreements, the
  BWET tanker ETF (90% of its contracts price off TD3C) and floating-rate
  charter contracts settle against it.
  https://www.lloydslist.com/LL1156643/How-imaginary-Middle-East-VLCC-rates-are-having-real-world-effects
  https://www.fairwayeta.com/insights/td3c-index-doesnt-exist-may-2026
- The Baltic opened a consultation in July 2026 (feedback closed August 3)
  on letting "alternative load ports outside the Middle East Gulf" be used in
  its Gulf assessments when the route is unworkable. If it adopts that, the
  TD3C definition changes and the weekly update needs a note.
  https://www.xindemarinenews.com/news/2079834497039503361
- The Baltic also publishes a Gulf of Oman to China route (TD34) that loads
  outside Hormuz. It was WS 220 in week 26 and about WS 450 (roughly $11.50 a
  barrel) on September 11. It is the "real" Gulf rate right now, but it has no
  history, so the chart stays on TD3C.
  https://boereport.com/2026/09/11/oil-tanker-rates-hit-record-highs-following-iran-us-shipping-attacks/
- Two Baltic weeks are interpolated and flagged in the data (Aug 18, 2023 and
  Aug 14, 2026). Nine weeks between December 2020 and December 2021 are
  missing because the report was not archived, and ten reports in that
  stretch gave a Worldscale figure without a dollar figure.

## 2. The 2026 spike, in order

Sources: IEA Oil Market Report March 2026; Hormuz Strait Monitor timeline;
Lloyd's List; CNBC; Poten via Maritime Executive; World Bank.

- **Before the war.** Rates were already high. VLCC earnings passed $100,000 a
  day in the fall of 2025 on sanctions (about 200 VLCCs, 23% of the fleet,
  pushed out of compliant trade), OPEC+ restoring output, and Asia buying
  more crude from the Atlantic Basin, which means longer voyages.
  https://tankersinternational.com/2026/01/07/2025-market-review-and-outlook-for-2026/
  https://www.eia.gov/todayinenergy/detail.php?id=67064
- **Feb 27, 2026.** Baltic TD3C at WS 216.89, $209,550 a day, "not seen since
  the spike of March 2020" (chart, and the Baltic report republished by
  Hellenic Shipping News). Gulf-to-China freight was about $5 a barrel.
  https://www.hellenicshippingnews.com/tankers-vlcc-market-skyrocketing/
  https://www.mees.com/2026/2/27/refining-petrochemicals/middle-east-crude-shipping-costs-surge-to-six-year-highs/c0d9c9a0-13e8-11f1-917b-c9bc2043c45f
- **Feb 28.** US and Israeli strikes on Iran. Iran closes the Strait of Hormuz
  to traffic without its permission. Insurers pull war-risk cover.
- **Mar 2.** Baltic TD3C prints $423,736 a day, up 94% from the Friday. The
  Baltic's global average VLCC index hits $280,941, above the prior record of
  $264,072 set March 16, 2020. Brokers say little has actually been fixed.
  https://www.lloydslist.com/LL1156492/Crude-tanker-rates-in-unchartered-territory-VLCC-index-tops-420K
- **Mar 6.** First weekly Baltic reading after the strikes: $485,959 a day
  (chart).
- **March.** IEA: flows through Hormuz fall "from around 20 mb/d before the
  war to a trickle." About 8 million barrels a day of crude output shut in,
  plus 2 mb/d of condensate and NGLs. "The largest supply disruption in the
  history of the global oil market." Brent up $20 to $92, briefly near $120.
  World Bank: Brent up 65% ($46) in March, the biggest monthly rise on record;
  global supply down 10.1 mb/d in March.
  https://www.iea.org/reports/oil-market-report-march-2026
  https://blogs.worldbank.org/en/opendata/strait-of-hormuz-disruption-sends-oil-prices-surging
- **Apr 7 to 8.** Two-week ceasefire; traffic resumes but stays far below
  normal. **Apr 13.** US blockade of Iranian ports after talks fail.
- **May 6.** Lloyd's List: VLCC crude exports down 36% (8.1 mb/d, about four
  VLCC loads a day) but voyages are longer. Atlantic-to-Pacific trips rose to
  35% of VLCC volume from 22%. A Texas-to-China trip is 2.6 times the length
  of Saudi-to-China. About 58 VLCCs, roughly 10% of the fleet, were trapped
  inside the strait. Rates held near $100,000 a day at the low.
  https://www.lloydslist.com/LL1157100/Hormuz-crisis-slashes-VLCC-volumes-by-36-but-voyages-are-longer
- **May 11.** TD3C $462,102 a day (fairwayeta; chart shows $467,408 for the
  week of April 24 and the spring plateau of $400,000 to $490,000).
- **Jun 14 to 18.** Memorandum of understanding; blockade lifted; record
  barrels exit in single days but ship counts stay a third of pre-war.
- **Late June low.** Baltic weekly $286,500 a day (chart).
- **Jul 7 to 12.** Talks collapse. Iran attacks ships, US strikes, Iran
  declares the strait "closed until further notice." **Jul 23.** Houthis hit
  two Saudi tankers in the Red Sea; Brent back above $100.
- **August.** Exports shift to ship-to-ship transfer: 80% of cross-Hormuz
  exports now move by STS, up from 603,000 b/d in April to 4.6 mb/d in
  August. Shuttle tankers run under US escort. Yanbu barrels go around by the
  Red Sea. Poten: the Gulf-to-Far East route averaged $600,000 a day in
  August.
  https://www.lloydslist.com/LL1158394/VLCC-market-hits-historic-high-in-latest-phase-of-Hormuz-crisis
  https://maritime-executive.com/editorials/poten-vlcc-rates-hit-unprecedented-levels-amidst-mideast-conflict
- **Aug 31.** Saudi tanker Sidr struck near Musandam; two seafarers killed.
- **Sep 5 to 9.** First direct Iran-US Navy exchange. US sinks or disables at
  least ten Iranian tankers in a week ("tanker for tanker"). Brent back to
  $100. Bab el-Mandeb transits restricted too (Poten).
- **Sep 9.** Lloyd's List: TD3C $759,969 a day, 26% above the March peak.
  Oman-to-China $358,201, West Africa-to-China $237,259, US Gulf-to-China
  $210,307. Vortexa: global crude exports down 10% year on year, VLCC loadings
  down 27%. Clarksons Securities raised its 2026 VLCC forecast from $75,000 to
  $135,000 a day and assumes disruption through mid-2027.
- **Sep 11.** Baltic weekly: WS 821.11, $862,150 a day (chart). OilPrice and
  Bloomberg: "$800,000 a day"; Kpler sees earnings above $100,000 a day into
  early 2027; a "historical norm" of about $45,000 a day; US Gulf-to-Asia
  cargoes at $29.5 million a voyage; about $15 a barrel before war-risk
  charges. Fearnleys' own Worldscale reading the same day: WS 800.
  https://oilprice.com/Energy/Energy-General/Supertanker-Rates-Hit-800000-a-Day-as-Gulf-Tensions-Escalate.html

## 3. The earlier spikes, and how each one differs

| Spike | Peak | What caused it | What it meant for oil |
|---|---|---|---|
| Nov 2004 | Baltic Dirty Tanker Index all-time high 3,194 on Nov 17, 2004; Gulf-to-Japan rates above WS 420; TCE above $200,000 a day (Gulf News, Business Standard) | China's import surge met a fleet that had not grown | Demand pull. Oil and freight rose together. |
| Jul 2008 | About $200,000 a day (Poten) | End of the commodity super-cycle; heavy ordering followed | Rates crashed with the financial crisis to below $20,000 by mid-2009. |
| Oct 11, 2019 | Baltic TD3C $300,391 a day (Lloyd's List); Fearnleys $269,000 (chart) | US sanctions on COSCO Dalian took about 50 VLCCs (6% of capacity) out of the market on Sep 25, on top of the Abqaiq attack and scrubber retrofits | Ships removed, not oil. Rates fell back within weeks as charterers refused to pay. |
| Mar 16, 2020 | Baltic TD3C above $326,000 a day (Hellenic Shipping News); Fearnleys $239,500 (chart); Baltic global VLCC average $264,072 | Saudi-Russia price war flooded the market while COVID cut demand; oil went into steep contango, so traders hired tankers to store cheap crude | The opposite signal: tankers were expensive because oil was cheap and unwanted. Bahri took more than a dozen VLCCs off the spot market; about three dozen were fixed in the Gulf in 24 hours. |
| Sep 2026 | Baltic TD3C $862,150 a day (chart), 2.6 times the 2020 peak | Hormuz closed or restricted for six months; ships trapped, insurance withdrawn, STS shuttles, longer routes, tankers sunk | Freight is rising because oil supply is cut and the surviving cargoes travel farther. Oil and freight up together, like 2004, but from a supply shock rather than demand. |

Sources for the table:
https://www.lloydslist.com/LL1129517/VLCC-spot-charter-breaks-300000-level-on-market-disruption
https://www.seatrade-maritime.com/accidents/vlcc-rates-hit-300-000-a-day-in-robust-yet-volatile-market
https://www.freightwaves.com/news/supertanker-rates-stratospheric-as-market-goes-bonkers
https://www.rigzone.com/news/saudi_belligerence_pushes_vlcc_rates_to_comedic_highs-01-apr-2020-161585-article/
https://www.seatrade-maritime.com/tankers/oil-prices-vlccs-and-floating-storage
https://www.business-standard.com/article/markets/shippers-hurt-as-tanker-rates-hit-decade-s-low-109042100020_1.html
https://gulfnews.com/business/vlcc-market-poised-to-firm-up-1.274242
https://maritime-executive.com/editorials/poten-vlcc-rates-hit-unprecedented-levels-amidst-mideast-conflict

The point for the narrative: a tanker rate spike is a symptom with more than
one possible disease. 2019 was ships removed. 2020 was oil nobody wanted.
2026 is oil that cannot get out. The chart alone does not say which; the
cause does.

## 4. Why supertanker rates matter for oil prices

Plain-language mechanics, for Eric to write from.

**a. Freight is part of the price of a barrel.** A VLCC carries about 2
million barrels. In a normal year the Gulf-to-Asia trip costs $1 to $2 a
barrel. At $200,000 a day (Feb 27) it was about $5. At WS 450 on the Gulf of
Oman route (Sep 11) it was about $11.50. Bloomberg's figure for the current
market is about $15 a barrel before war-risk insurance. Scaling the Gulf of
Oman figure by the ratio of the two Worldscale readings puts TD3C at roughly
$20 a barrel, an estimate, not a published number. On $100 oil that is a
fifth of the price of the crude itself, paid by the refiner and passed to the
pump. Say "roughly" and show the method if this goes in the post.

**b. Freight opens a gap between where oil is sold and where it is burned.**
The refiner in Ningbo pays crude plus freight. When freight jumps, either the
seller cuts the price at the loading port (Saudi official selling prices,
Dubai-linked grades) or the buyer pays more, or both. That is why the gap
between Middle East crude and Atlantic Basin crude (Brent, WTI) moves with
tanker rates, and why US Gulf exports to Asia get priced in or out of the
market by freight. (Lloyd's List, Sep 9: "few owners interested in the
Atlantic given huge returns on offer in the East.")

**c. Ton-miles: the same oil, a longer trip, fewer ships.** If a cargo that
used to take 25 days to reach Asia now takes 60 (around the Cape, or shuttled
out of the Gulf by STS), the same number of barrels needs more than twice the
ships. Fleet supply does not change; effective supply falls. Rates rise even
when volumes fall, which is exactly what happened in May 2026 (volumes down
36%, rates stable at double year-ago). This is why tanker rates can stay high
after the oil shock itself eases.

**d. Insurance and risk premium.** War-risk premiums hit 16 times pre-war
levels in April, 8 times by mid-June (Hormuz Strait Monitor). An owner
willing to sail inside the strait prices the risk to the ship and the 25 crew
into the rate. Only a few owners do, so those few set the marginal price.

**e. Storage: the signal that runs the other way.** When the futures curve is
in contango (later months cost more than now), traders hire tankers as
floating warehouses. Rates spike while oil prices fall. 2020 is the textbook
case. So a rate spike with falling oil prices means glut; a spike with rising
oil prices means shortage or blockage. Read the two together.

**f. What the forward market and forecasters say.** Clarksons Securities:
$135,000 a day average for 2026, disruption through mid-2027. Kpler: above
$100,000 into early 2027. Poten: the orderbook is 40% of the fleet, and every
past boom ended in a bust; "Owners should take advantage of the current
market. This may never happen again!" The BWET ETF was up 292% year to date
by mid-March against about 50% for the listed tanker owners, because the
index runs ahead of what ships actually earn.

**g. What would bring rates down.** Reopening of Hormuz with insurance cover;
the Baltic redefining the route to a port outside the strait; the 40 or so
newbuild deliveries a year; a demand hit from $100 oil (World Bank: demand
down 0.8 mb/d in March, 1.5 mb/d more in Q2). Rates fell by about half in
the two months after the March peak when traffic partially resumed, then
tripled again when it did not hold (chart).

## 5. Numbers to reuse (recomputed from the data)

See `research/TIEOUT.md`, produced by `scripts/build.py`, for the list. The
headline set: the latest reading, the week before the strikes, the first week
after, the late-June low, the 2019 and 2020 peaks in both series, and the
2022-to-2025 average.

## 6. Open questions before publishing

- Whether the Baltic adopted the alternative-load-port change after the
  August 3 consultation. Check the week 38 report language.
- The exact 2026 Worldscale flat rate for Ras Tanura-Ningbo, to state freight
  per barrel precisely rather than by proportion.
- Whether to show the Gulf of Oman route (TD34) as a third line once it has
  a few months of history.
