can you# Supertanker rates: research notes for the Data 4 Thought piece

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
- **Early July low.** Baltic weekly $286,500 a day, week of Jul 3 (chart).
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

## 3b. 2022 versus 2026: an oil spike without a tanker spike, then both

Eric's observation, checked against the data (chart, and Brent from the EIA
weekly Europe Brent spot series):

| | 2022 | 2026 |
|---|---|---|
| Brent weekly high | $127.40 (week of Jun 10, 2022) | $124.61 (week of Apr 10, 2026) |
| Baltic TD3C the same week | minus $22,200 a day | $444,200 a day |
| Baltic from the shock to the Brent peak | Feb 25 to Jul 1, 2022: average minus $10,294 a day; 15 of 17 weeks below zero | Mar 6 to Apr 10, 2026: $326,198 to $485,959 a day |
| Brent the week before the shock | $97.80 (Feb 18, 2022) | $71.36 (Feb 27, 2026) |

The Baltic series was below zero for 48 weeks between January 22, 2021 and
July 15, 2022, and VesselsValue called early 2021 to August 2022 the longest
stretch of negative VLCC earnings on record. Oil went to $127 in the middle of
that stretch and supertankers still lost money on the Gulf-to-China run.

**Why 2022 did not move VLCCs.** A tanker rate is a price for ships, not for
oil. It moves when the number of ships needed changes, or when the number
available changes. In 2022 neither did, at first:

- Russia's barrels never rode VLCCs. They load at Primorsk, Ust-Luga and
  Novorossiysk, shallow Baltic and Black Sea ports served by Aframaxes and
  Suezmaxes. The 2022 shock repriced oil and rerouted Russian crude, and the
  freight boom landed in those smaller ships. The VLCC's home trade, Middle
  East to Asia, did not change.
- Middle East loadings were still being held back. OPEC+ was only unwinding
  its 2020 cuts month by month, so there were fewer Gulf cargoes than the
  fleet could carry.
- The fleet was long. Ships hired as floating storage in 2020 came back into
  the market through 2021, few were scrapped, and China's 2022 lockdowns cut
  its crude imports.
- Fuel costs rose with oil, so the same Worldscale rate paid the owner less.

VLCC earnings only turned up in the second half of 2022, once the EU ban on
Russian crude pushed Europe to buy from the Gulf, West Africa and the US, and
Asia took the displaced Russian barrels, which lengthened the average voyage.
The Baltic series reached $96,400 a day on November 18, 2022 (chart).
https://www.rivieramm.com/opinion/opinion/vesselsvalue-vlcc-supply-and-demand-analysis-72775
https://oilprice.com/Latest-Energy-News/World-News/Supertanker-Rates-Skyrocket-as-Asia-Rushes-to-Replace-Russian-Oil.html

**Why 2026 moves both at once.** This time the shock hit the ships directly.
The Strait of Hormuz is the VLCC trade's front door: about 20 million barrels
a day passed through before the war (IEA). Closing it trapped roughly 58
VLCCs inside (about 10% of the fleet), withdrew insurance, forced cargoes onto
shuttle and ship-to-ship arrangements, and sent replacement barrels from the
Atlantic on trips 2.6 times as long. Fewer usable ships, longer voyages and a
war-risk premium all pushed the same way. Oil rose because supply was cut;
freight rose because the surviving oil needed more ship-days per barrel.

**The line for the post.** An oil price spike alone does not make supertankers
expensive. What does is a shock that changes where ships have to go or how
many are available. 2022 was the first kind. 2026 is the second, and it is the
first time since at least 2004 that oil and freight have spiked together.

## 3c. 2008 to 2009: the peak, the crash, the bottom

For the intro. Free sources give three views of the same slide, saved in
`data/history_2008_2009.csv` and `data/history_2008_2009_quarterly.csv`:
the Baltic Dirty Tanker Index (a daily composite of crude routes, monthly
averages here), the Drewry monthly Worldscale assessment for Persian Gulf to
Japan as reprinted by UNCTAD, and two owners' quarterly spot earnings for
VLCCs. OSG's figure is its own conversion of Arabian Gulf fixtures (60% east,
40% west) and is the one that shows the highs and lows within each quarter.
Frontline's is what its modern double-hull ships actually earned. No free
source gives a weekly dollar figure for 2008.

| | Baltic Dirty Tanker Index, monthly avg | OSG Arabian Gulf VLCC spot, $/day (quarter avg; high / low) | Frontline double-hull VLCC spot, $/day | Drewry WS, Gulf to Japan |
|---|---|---|---|---|
| Jan to Mar 2008 | 1,396 / 1,093 / 1,313 | $83,600 (high $250,000) | $104,700 | |
| Apr to Jun 2008 | 1,539 / 1,939 / 1,943 | $108,300 (high $199,300) | $105,200 | |
| Jul 2008 | 2,072; all-2008 high 2,347 on Jul 23 | | | |
| Aug 2008 | 1,510 | Q3: $77,600 (high $196,200, low $7,200) | Q3: $88,600 | |
| Sep 2008 | 1,498 | | | |
| Oct 2008 | 1,377 | | | |
| Nov 2008 | 1,065 | Q4: $54,900 (high $104,000, low $32,900) | Q4: $59,800 | |
| Dec 2008 | 1,280 | | | 66 |
| Jan to Mar 2009 | 718 / 590 / 635 | $40,400 (high $80,700, low $15,500) | $56,200 | 51 / 44 / 41 |
| Apr to Jun 2009 | 480 / 478 / 613; low 453 on Apr 15 | $13,300 (low minus $4,500) | $38,700 | 27 / 27 / 46 |
| Jul to Sep 2009 | 516 / 485 / 514 | $7,200 (low minus $5,800) | $26,800 | 42 / 40 / 33 |
| Oct to Dec 2009 | 565 / 634 / 753 | $17,000 | $30,400 | 43 / 44 / 56 |
| Jan 2010 | 1,127 | | | 104 |
| Full year | | 2008 $81,100; 2009 $19,500 (down 76%) | 2008 $74,500; 2009 $38,300 | |

Sources: BDTI daily history (Baltic Exchange, via the yieldchaser mirror);
UNCTAD Review of Maritime Transport 2010, table 4.2, from Drewry Shipping
Insight; OSG 2008 and 2009 annual reports; Frontline quarterly releases 2008
and 2009.
https://unctad.org/system/files/official-document/rmt2010_en.pdf
https://www.annualreports.com/HostedData/AnnualReportArchive/o/NYSE_OSG_2008.pdf
https://www.annualreports.com/HostedData/AnnualReportArchive/o/NYSE_OSG_2009.pdf
https://www.frontline.bm/fro-third-quarter-2008-results/
https://www.frontline.bm/fro-preliminary-fourth-quarter-and-financial-year-2009-results/

**What August and September 2008 looked like from a desk.** The peak was
already behind the market. Rates for the Gulf-to-Asia run had touched about
$200,000 a day in the second week of July, then, in Frontline's words, "the
market took such a sudden fall at the end of July" that its strategy of
fixing short voyages "proved wrong." OSG's Gulf index printed a low of
$7,200 a day somewhere in the third quarter, and the Baltic dirty index
dropped from 2,347 on July 23 to a monthly average of about 1,500 in August
and September, roughly the level of the previous spring. Third-quarter
averages were still very good money: $77,600 (OSG) to $88,600 (Frontline) a
day against a cash cost of running a VLCC of roughly $10,000 a day at the
time. Anyone starting in September 2008 walked into a market that had just
halved from a record and still looked strong by any historical standard.
Lehman filed on September 15. Oil had already fallen from $147 on July 11
to about $90.

**Why rates had been so high in the first half of 2008.**
- OPEC, led by Saudi Arabia and Iraq, had raised output by about 900,000
  barrels a day over 2007, and most of it moved long-haul out of the Gulf.
  Chinese crude imports rose 12% in 2008, with imports from the Middle East
  and South America each up 20% (OSG).
- The VLCC fleet did not grow. Conversions to dry bulk and storage plus
  scrapping offset deliveries; OSG counted no net change in 2008, with the
  fleet ending the year at 519 ships.
- Iran had put unsold heavy crude on ten or more of its own VLCCs, taking
  them off the market.
- Bunker fuel hit its record in July, so ships slowed down, which tightened
  supply further. Asian refiners were also refusing single-hull ships after
  the Hebei Spirit spill off Korea in December 2007, which split the market
  and pushed modern-ship rates higher.
- Traders were long oil and long freight together. UNCTAD's read: "high oil
  prices fuelled higher demand as traders sought speculative positions.
  Ultimately, this bubble collapsed when the market saw that oil prices had
  reached a peak, and consequently freight rates collapsed too."

**Fourth quarter 2008: the demand shock.** World oil demand fell 2.5% year
on year in the quarter, the opposite of the usual winter rise. OPEC
announced cuts on October 24 (1.5 million barrels a day) and December 17 in
Oran (2.2 million, the largest single cut it had ever made), 4.2 million a
day in total from September levels, effective January 1, 2009. Fewer Gulf
cargoes means fewer VLCC fixtures, and the cuts fell hardest on the long-haul
grades. Quarterly VLCC earnings fell about 29% from the third quarter. Two
things cushioned the drop: oil went into a steep contango as spot prices
collapsed to about $35 a barrel, so traders hired VLCCs to store crude for
later delivery (as many as 35 ships by early 2009, OSG), and Somali piracy
pushed some ships around the Cape. Secondhand tanker values fell 35% to 40%
from their third-quarter highs, and scrap steel fell from $740 to about $300
a ton. Nine VLCCs delivered in the fourth quarter alone.

**2009: the slide to the bottom.** Middle East OPEC production ran 1.8
million barrels a day below 2008 and West Africa 200,000 lower, while the
fleet grew 4.5% as the ships ordered in the boom arrived (31.9 million
deadweight tons of tankers delivered across all sizes in 2009 against 8.4
million scrapped). Refiners outside China cut runs. OSG's Gulf VLCC index
fell every quarter: $40,400, $13,300, $7,200, then $17,000. Its quarterly
lows went negative in the second and third quarters, meaning a ship could
finish a voyage having paid to carry the cargo. The Drewry Worldscale
assessment for Gulf to Japan bottomed at WS 27 in April and May 2009, the
Baltic dirty index at 453 on April 15, 2009, the lowest since the index
began in 1998. Frontline's modern ships did better than the index, at
$38,700 in the second quarter and $26,800 in the third, because charterers
paid up for double hulls. Floating storage was the only thing soaking up
ships: about 100 million barrels at sea during 2009, and UNCTAD counts 143
million barrels on 129 tankers in October 2009. The market turned in
December 2009 as winter demand and a colder-than-usual season met a fleet
partly tied up in storage; the Drewry assessment doubled to WS 104 in
January 2010. The recovery was brief. Deliveries from the 2007 to 2008
orderbook kept VLCC earnings weak until 2013, with the single-hull phase-out
of 2010 the only relief.

**Numbers for the intro.** From the July 2008 peak (about $200,000 a day on
the Gulf-to-Asia run) to the summer of 2009 (OSG quarter average $7,200,
Frontline $26,800), earnings fell by more than 90% on the index measure and
by about 85% for a modern ship. On the Baltic dirty index, the drop from the
July 23, 2008 high to the April 15, 2009 low was 81%. It took about nine
months from Lehman to the bottom, and the bottom lasted most of a year.

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

**h. The two $150 calls, for the intro.** In June 2008 Morgan Stanley told
clients crude could reach $150 by July 4, citing Asian demand and falling
inventories; WTI peaked at $147 on July 11 and never got there. In May 2026
Exxon's Neil Chapman warned that physical Brent cargoes would spike to $150
to $160 once inventories hit record lows. On the futures screen Brent is
about $108 in mid-September, so on paper that call has not come true either.
Landed in Asia it has: Murban at Fujairah was about $131 on September 14
(ICE Futures Abu Dhabi, 16-minute delay) and the Gulf of Oman to China
freight about $11.50 a barrel, so a Gulf barrel that can actually leave
costs roughly $142 delivered before war-risk insurance. Dubai was about $115
(Platts, three-day lag), above Brent, which it normally trades below. Date
every one of these prices in the post.
https://www.cnbc.com/2026/05/28/oil-inventory-exxon-strait-hormuz-iran-war.html
https://www.forbes.com/2008/06/06/oil-energy-update-markets-comm-cx_cg_0606markets27.html

**i. Headline candidate and the $150 arithmetic.** "$150 oil arrived. It
just came by ship." Chapman's May 28 warning was for physical Brent cargoes,
a North Sea barrel at the loading port, and that barrel is about $108 in
mid-September, so the forecast has not come true where he said it would. It
has in Asia once the ship is counted:

| Barrel | Price at loading port | Freight to China | Landed in China |
|---|---|---|---|
| Gulf crude loading outside Hormuz (Murban at Fujairah, Sep 14, ICE Futures Abu Dhabi) | about $131 | about $11.50 (Baltic Gulf of Oman to China, WS 450, Sep 11) | about $142 |
| Atlantic crude (US Gulf, priced off Brent, Sep 14) | about $108 | about $15 ($29.5 million per VLCC voyage, Bloomberg, Sep 11, over 2 million barrels) | about $123 |

Both are before war-risk insurance, which adds more. The two prices are
both real: the screen price is what a producer gets, the landed price is
what a refiner pays, and the gap between them is freight, insurance and the
premium for a barrel that can leave the Gulf at all. That gap is what the
tanker chart measures. Keep the claim to Gulf crude: "$150 in Asia" holds
for a Fujairah barrel, not for every barrel. Date every price.

**j. The math on the route in use now: Gulf of Oman to China.** Gulf crude
that leaves today loads outside Hormuz, either grades that already load
there (Murban at Fujairah) or barrels shuttled out of the Gulf by smaller
tankers and transferred ship-to-ship. The published freight for that leg is
the Baltic's Gulf of Oman to China route, WS 450 on September 11, which
Reuters put at about $11.50 a barrel.

Voyage assumptions (ours, stated so they can be checked): Fujairah to Ningbo
about 5,400 nautical miles via Malacca; 13 knots laden, 13.5 in ballast; four
days in port; 270,000-tonne cargo, 7.33 barrels a tonne, 1.98 million
barrels; bunkers 70 tonnes a day laden, 55 in ballast, at $650 a tonne.

| | Value |
|---|---|
| Sailing time, Fujairah to Ningbo, laden | about 17 days |
| Round trip including port time | about 38 days |
| Freight at WS 450 (2026 flat rate backed out of the Reuters figure, about $18.70 a tonne) | $84 a tonne, $22.8 million a cargo, $11.50 a barrel |
| Same cargo at the Lloyd's List Oman to China earnings of $358,201 a day (Sep 9) | $15.6 million, about $7.90 a barrel |
| Cost of each extra day at sea, per barrel | $0.18 to $0.23 |
| For comparison, the TD3C assessment (Ras Tanura, WS 821.11, about 5,750 nm, 40-day round trip) | $18.50 to $22 a barrel |
| For comparison, Yanbu around the Cape to Ningbo | about 11,200 nm, 36 days laden, 76-day round trip |

The two Gulf of Oman figures differ because the market rose between
September 9 and 11 and because Reuters' conversion assumes a flat rate we
cannot see. Use "$8 to $11.50 a barrel, about 17 days at sea" for the post.

If the barrel starts inside the Gulf, add the shuttle: an Aframax at roughly
$150,000 a day for a six-day round trip carrying 700,000 barrels, war-risk
cover of $1 to $2 million per transit, and ship-to-ship fees, which comes to
roughly $3 to $5 a barrel on top. This is our estimate; no published figure
was found, so mark it as an estimate or leave it out.

So the landed cost of a Murban barrel in China on September 14 is about
$131 plus $8 to $11.50, or $139 to $143, before war-risk insurance on the
main leg. A Saudi barrel shuttled out of the Gulf would be a few dollars
more.

**k. War-risk insurance: how much, and whether it can be had.** War-risk
cover is a separate policy from hull insurance, bought per transit of a
listed area and quoted day by day. Underwriters can cancel it on seven days'
notice (Lloyd's wordings) or 48 hours (US wordings), which is what happened
on March 1, when Gard, Skuld, NorthStandard, the London Club and the
American Club gave notice effective March 5. The Joint War Committee listed
the whole Arabian Gulf as a conflict zone that week.

Premiums, as a share of the ship's insured value, per transit:

| When | Rate | Source |
|---|---|---|
| Before Feb 28, 2026 | about 0.25% (some say 0.15%) | The National, Hormuz Strait Monitor |
| Mar 11 | 2.5% for a plain Hormuz transit; 5% to 10% for ships with a US, UK or Israeli connection; "10% minimum" after a bad night | Lloyd's List |
| July | 3% to 10%; up from 1% to 3% a few weeks earlier | The National, Jul 17; S&P Global on Marsh, Jul 22 |
| Sep 8, before the tanker strikes | 7.5% to 12.5% | Breakwave bi-weekly report |
| 1980s tanker war, for scale | about 5% | Lloyd's List |

Dollars per barrel, our arithmetic on a 1.98-million-barrel VLCC:

| Ship and leg | Insured value | Premium per transit | Per barrel |
|---|---|---|---|
| VLCC through Hormuz at 7.5% to 12.5% | $138 million (Lloyd's List's five-year-old example) | $10 million to $17 million | $5 to $9 |
| Same, on a $210 million modern VLCC | $210 million | $16 million to $26 million | $8 to $13 |
| VLCC loading at Fujairah, never entering the strait, at roughly 1% for static tonnage in the listed area | $138 million to $210 million | $1.4 million to $2.1 million | about $1 |
| Aframax shuttle through the strait, 700,000 barrels, at 7.5% to 12.5% | $80 million to $100 million | $6 million to $12.5 million | $9 to $18 |

Lloyd's List's own March example: $10 million to $14 million for a US-linked
VLCC transit, "to the charterer's rather than owner's account." So on the
route in use now, the cover on the big ship is cheap (about $1 a barrel)
and the cost sits on the shuttle leg inside the Gulf, where it can exceed
the freight itself. That is why so much Gulf crude moves under US escort or
on Gulf-state and Iranian ships that carry their own risk, and why the STS
model took over. Cargo war-risk cover (on the oil rather than the ship) is
priced separately; no published figure was found.

Can it be had? Yes, at a price. The Lloyd's Market Association said in
March that reports of cover being unavailable or unaffordable were "not
accurate," and Marsh in July described plentiful regional capacity with an
"inconsistent response" among insurers. In practice quotes are withdrawn
overnight after an attack, insurers cap their exposure on any one ship, and
some decline ships with the wrong ownership or flag. The World Economic
Forum described governments stepping in as insurers of last resort in
April (the article could not be fetched; verify before citing). Marsh's
Marcus Baker: "War rates have been on a roller coaster mirroring the
development of the price of oil."
https://www.lloydslist.com/LL1156586/Gulf-war-risk-premiums-topping-double-digit-millions-of-dollars-per-trip
https://www.thenationalnews.com/business/2026/07/17/war-risk-shipping-premium-surges-again-as-tensions-escalate-at-strait-of-hormuz/
https://www.spglobal.com/energy/en/news-research/latest-news/shipping/072226-middle-east-shipping-insurance-costs-rise-on-hormuz-risks-marsh
https://www.breakwaveadvisors.com/insights/980026wetreportkju458-ook57
https://lmalloyds.com/safety-concerns-not-insurance-availability-driving-reduced-vessel-traffic-in-the-strait-of-hormuz/
https://finance.yahoo.com/news/marine-insurers-cancel-war-risk-082111845.html
https://www.weforum.org/stories/2026/04/how-middle-east-war-turning-governments-into-insurers-last-resort/

**k2. Cargo war-risk cover, the oil itself.** No published 2026 rate was
found for crude cargoes through Hormuz, and every broker piece prices the
ship, not the oil. What the sources do say: Howden Re's March 26 report lists
cargo war risk for energy and bulk commodities as "available at standard
rates" before the war and "voyage-by-voyage basis only, significant
increase, +50% to more than 1,000%" after it, and adds that "the cargo could
now be worth almost the same value as the ship that carries it, possibly
doubling the insurance premium if the cargo is also insured by the
shipowner." Al Jazeera (July 23) quotes 0.5% for Bab al-Mandeb transits and
0.1% in the northern Red Sea, which is the nearest published crisis rate.
Pre-war, cargo war risk on a Gulf voyage was a few hundredths of a percent.

Our arithmetic, labeled as an estimate:

| Cargo | Value | Rate assumed | Premium | Per barrel |
|---|---|---|---|---|
| 1.98 million barrels of Murban at $131 on a VLCC loading at Fujairah, never entering the strait | $259 million | 0.5% to 1% | $1.3 million to $2.6 million | $0.65 to $1.30 |
| Same cargo if the VLCC transited Hormuz at hull-like rates of 7.5% to 12.5% (Howden's "doubling") | $259 million | 7.5% to 12.5% | $19 million to $32 million | $10 to $16 |
| 700,000 barrels at $115 on a shuttle Aframax through the strait, if commercially insured | $80 million | 7.5% to 12.5% | $6 million to $10 million | $9 to $14 |

For the route in use, the cargo line on the big ship is small, roughly $1 a
barrel. The exposure sits on the shuttle leg, where cargo cover at
hull-like rates would add as much again as the hull cover. In practice most
of that oil moves on Gulf-state, Iranian and US-escorted ships, and the
producers self-insure or run without cover, so treat the shuttle lines as
what a commercial charterer would face rather than what is being paid.

With cargo cover added, the landed cost in section l becomes about $141 to
$145 for the Murban barrel, and $135 to about $162 for a shuttled Saudi
barrel if every leg were commercially insured. Use the Murban figure in the
post; it is the one built on published numbers.
https://www.howdenre.com/sites/howdenre.howdenprod.com/files/2026-03/HowdenRe_Strait_of_Hormuz_report_March272026.pdf
https://www.aljazeera.com/economy/2026/7/23/how-shipping-insurance-rates-are-rising-as-hormuz-bab-al-mandeb-shut-down

**l. The whole bill: delivered cost of a barrel in China, mid-September 2026.**
Adding sections i, j, k and k2. Prices are dated; freight and insurance are
ranges from the published figures and our arithmetic above. The cargo
war-risk lines are estimates (no published rate; see k2).

| | Murban barrel loading at Fujairah, outside the strait | Saudi barrel shuttled out of the Gulf | Atlantic barrel (US Gulf) for comparison |
|---|---|---|---|
| Price at the loading port | $131 (Murban, Sep 14) | $115 (Dubai, Sep 11, three-day lag) | $108 (Brent, Sep 14) |
| Shuttle inside the Gulf, freight plus ship-to-ship | none | about $2 (estimate) | none |
| War-risk cover on the shuttle transit, 7.5% to 12.5% of an $80 to $100 million Aframax over 700,000 barrels | none | $9 to $18 | none |
| VLCC freight to China | $8 to $11.50 (Gulf of Oman route, Sep 9 to 11) | $8 to $11.50 | about $15 ($29.5 million voyage, Sep 11) |
| War-risk cover on the VLCC, about 1% for a ship that never enters the strait | about $1 | about $1 | none |
| Cargo war-risk cover on the oil, shuttle leg (estimate, if commercially insured) | none | $9 to $14 | none |
| Cargo war-risk cover on the oil, VLCC leg (estimate, 0.5% to 1%) | $0.65 to $1.30 | $0.65 to $1.30 | none |
| **Landed in China** | **about $141 to $145** | **about $145 to $163** | **about $123** |
| Days at sea | about 17 | about 17 plus the shuttle | about 45 (US Gulf to China via the Cape) |

Priced straight off the headline rate instead (added Sep 14 after Eric asked
why the $862,150 was not in the table): a Ras Tanura barrel at Dubai $115,
freight $18.60 to $22 (the TD3C day rate times a 40-day round trip plus
about $2 million of fuel and port costs, over 1.98 million barrels; or WS
821 times the flat rate), hull war-risk for the transit $5 to $13, cargo
cover at hull-like rates $10 to $16, lands at about $149 to $166. That is
within a few dollars of the shuttle model above, which is reassuring: two
ways of pricing the same barrel land in the same place. Possible overlap:
the Baltic says its TD3C assessment already carries a risk premium for
entering the strait, so the low end is the more likely figure. The post's
table now uses this column in place of the shuttle column.

Two cautions. The shuttle column is the most uncertain line in the notes:
much of that crude moves on Gulf-state, Iranian or US-escorted ships that
carry their own risk, so the insurance line is what a commercial charterer
would be quoted, not necessarily what is paid. And the Dubai price is the
stale one; if it has moved with Murban since September 11, the Saudi column
is higher. The point survives either way: the screen says $108, and a Gulf
barrel in a Chinese refinery costs about $141 to $145 today by the route
that is actually in use, with $10 to $14 of it for the trip and its cover;
a barrel that has to be shuttled out of the Gulf and insured commercially
at every step would cost $145 to $163, $30 to $48 of it for the trip.

**m. Physical oil versus the futures screen.** The Brent price on the news
is the ICE front-month futures contract. The price a refiner pays for a real
cargo is Dated Brent, the assessment for North Sea cargoes loading in the
next few weeks, which the EIA publishes daily as its "Europe Brent spot price
FOB." The chart's Brent panel now draws both (physical in dark ink, futures
in light gray) so the gap can be seen; the daily file is
`data/crude_spot_vs_futures_daily.csv`, futures via Yahoo Finance's relay of
ICE closes.

The EIA's own description, April 24, 2026: Dated Brent "reflects trading and
pricing for a given cargo of crude oil as it is loaded from a handful of
North Sea terminals"; "under normal market conditions, the spread between
the Dated Brent spot price and the front-month Brent futures price is narrow
and tends to be positive"; in early April it "reached a premium exceeding
$25 per barrel" because buyers scrambling for immediate barrels are "better
represented in spot market prices than in futures contracts, which are
pricing crude for later delivery."
https://www.eia.gov/todayinenergy/detail.php?id=67544

Physical minus front-month futures, dollars a barrel (chart data):

| Year | Average gap | Widest | Date |
|---|---|---|---|
| 2019 | +$0.16 | +$3.16 | Dec 19, 2019 |
| 2020 | minus $1.38 | minus $11.25 (contango, storage glut) | Apr 9, 2020 |
| 2022 | +$2.00 | +$11.10 | Jul 15, 2022 |
| 2023 | +$0.30 | +$4.21 | Oct 5, 2023 |
| 2024 | +$0.69 | +$3.78 | Mar 4, 2024 |
| 2025 | +$0.88 | +$3.29 | Apr 1, 2025 |
| 2026 to Sep 9 | +$3.71 | +$28.94 (spot $138.21, futures $109.27) | Apr 7, 2026 |

2026 by month: January +$1.82, February +$1.48, March +$3.54, April +$15.19,
May +$3.59, June +$1.02, July minus $0.07, August +$3.12, September so far
+$5.13. On September 9 physical Brent was $109.51 against $101.21 on the
screen, a gap of $8.30 and widening for six straight sessions.

The reading for the post: the screen price is a bet on oil in a month or
more; the physical price is what a cargo costs now. When the strait closed,
the physical barrel ran $29 ahead of the screen, nearly three times the
worst day of 2022 ($11.10). It is doing it again in September. In 2020 the
gap ran the other way, minus $11 in April, because nobody wanted a prompt
barrel and tankers were being hired to hold them. Same three episodes, same
signature as the tanker chart.

Parameta Solutions, on the futures curve itself: the spread between the
front month near $119 and contracts two years out at $70 to $75 reached
about $50 in early April 2026, "exceeding even the June 2022 dislocation";
the one-month to twelve-month spread went from about $10 to about $35 in
four weeks.
https://www.parametasolutions.com/insights/extreme-brent-backwardation-managing-curve-dislocation-with-otc-oil-data/

Asian physical benchmarks (Dubai, Murban) sit further above the screen
still; see sections i and l. No free daily history exists for them, which
is why the panel uses Brent.

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
