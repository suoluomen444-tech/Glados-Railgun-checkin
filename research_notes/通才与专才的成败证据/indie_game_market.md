# Indie game market base rates and survivorship bias (focus: solo developers)

Research-process note for the report writer: research done Oct 24–25, 2026. Every full-page fetch was blocked by the session's egress policy (HTTP 403 / DNS failure), and the shared web-search budget ran out partway through. **All figures below therefore come from search-engine extracts of the cited pages, not from reading the full pages.** Treat exact wording and definitions as "as reported". Evidence tags: **[Official]** = Valve or developer/publisher statement; **[Estimate]** = third-party model (Gamalytic, VG Insights, Alinea, GameDiscoverCo, review-multiplier methods); **[Survey]** = developer survey; **[Weak]** = secondary or SEO blog, unverified.

## 1. Steam release volume (2020–2026) and revenue distribution

### Takeaway
Steam releases roughly doubled from about 9,700 (2020) to about 19,000–20,300 (2025). 2026 is on pace for a new record, with 11,979 releases in H1 alone. Independent estimators broadly agree on the shape of the distribution:
- The median new game grosses about $250–$1,800 (lifetime median for the 2019 cohort: about $1,100).
- About two-thirds gross under $1,000.
- About 8–14% exceed $100k gross.
- Only about 1–1.5% exceed $1M.

All of these are model estimates of gross revenue, apart from a few Valve aggregates.

### Cited Findings

**Release volume (SteamDB-based counts; they differ by snapshot date and filtering)**
- 2020: 9,686 new games, per TechSpot citing SteamDB — [TechSpot](https://www.techspot.com/news/106158-russia-plans-domestic-game-console-launch-decade.html). Kevuru Games' table lists 9,646 — [Kevuru Games (vendor blog)](https://kevurugames.com/blog/how-many-video-games-are-released-each-year-industry-statistics/).
- 2021: 11,232. 2022: 12,268. Both are from Kevuru's SteamDB-derived table — [Kevuru Games](https://kevurugames.com/blog/how-many-video-games-are-released-each-year-industry-statistics/).
- 2023: 14,423 (+14.5% YoY) — [Game World Observer, Dec 2023](https://gameworldobserver.com/2023/12/27/steam-record-14k-games-2023-most-played-top-rated-titles). GameSpot counted 14,535 unique games — [GameSpot](https://gamespot.com/articles/the-number-of-2023-steam-releases-is-too-damn-high/1100-6520121/).
- 2024: a record of about 18,949–18,965 at end-Dec 2024 (+33% YoY) — [ITC.ua](https://itc.ua/en/news/steam-sets-a-record-almost-19-000-games-released-in-2024); [Mezha](https://mezha.media/en/2024/12/30/a-new-record-nearly-19-000-new-games-were-released-on-steam-in-2024).
  - GamesRadar used 18,908 (SteamDB) — [GamesRadar, 2025](https://www.gamesradar.com/games/steams-new-game-revenue-is-10x-higher-than-it-was-10-years-ago-but-only-around-200-made-more-than-usd1-million-in-their-first-30-days/).
  - A Dec 2025 SteamDB reading gave 18,558 for 2024 — [GamingOnLinux, Dec 2025](https://www.gamingonlinux.com/2025/12/over-19000-games-have-released-on-steam-in-2025-with-nearly-half-seeing-fewer-than-10-reviews/page=1/).
- 2025, by source:

  | Count | Source |
  |---|---|
  | 19,008 (SteamDB, Dec 2025) | [GamingOnLinux](https://www.gamingonlinux.com/2025/12/over-19000-games-have-released-on-steam-in-2025-with-nearly-half-seeing-fewer-than-10-reviews/page=1/) |
  | ~19,200 | [WN Hub](https://wnhub.io/news/analytics/item-49561) |
  | "around 20,000" | [Alinea via GameDev Reports](https://gamedevreports.substack.com/p/alinea-analytics-2025-year-in-review) |
  | 20,282 (Chris Zukowski's tally) | [Shazoo, Jan 2026](https://shazoo.ru/2026/01/29/178897/za-2025-god-v-steam-vyslo-bolee-20-tysiac-igr-no-tolko-608-polucili-bolee-1000-otzyvov) |

- Nearly half of 2025 releases received fewer than 10 Steam reviews — [GamingOnLinux](https://www.gamingonlinux.com/2025/12/over-19000-games-have-released-on-steam-in-2025-with-nearly-half-seeing-fewer-than-10-reviews/page=1/); [80.lv](https://80.lv/articles/steam-earned-usd16b-in-2025-but-nearly-half-of-19-000-games-got-under-10-reviews).
- 2026: 11,979 releases in H1 2026 per SteamDB, about 66 per day — [Game World Observer, Sep 2026](https://gameworldobserver.com/2026/09/01/the-median-revenue-of-games-on-steam-has-been-declining-for-12-consecutive-years).

**Revenue distribution of release cohorts**
- **[Estimate: VG Insights data analysed by Chris Zukowski, Nov 2022]** Lifetime gross for the 2019 Steam cohort — [Game World Observer, 2022-11-29](https://gameworldobserver.com/2022/11/29/median-indie-game-earnings-steam-barely-over-1000):
  - Median: $1,136.
  - 68% earned under $10k.
  - 91.5% earned under $250k.
  - Top-20% threshold: $34k. Top-10% threshold: $198k.
- **[Estimate: Gamalytic, Sep 2023 report]** Covers the ~41,000 games released in the prior three years (58% of ~71,000 Steam titles) — [WN Hub](https://wnhub.io/news/stores-and-publishing/item-42136); [Game World Observer](https://gameworldobserver.com/tag/gamalytic):
  - 50% grossed $500 or less.
  - Median excluding free titles: $700.
  - Median for games priced over $5: about $4,000. Priced over $10: about $17,000.
  - More than 70% of these releases were "hobbyist projects."
- **[Estimate: Gamalytic, 2023]** Of games on Steam: 67% earned under $5k, 17.2% earned $5k–$50k, 6.9% earned $50k–$200k, and 8.9% earned over $200k — [GameDev Reports](https://gamedevreports.substack.com/p/gamalytic-67-of-games-on-steam-earned). The base (all titles vs. a cohort) was not clear in the extract.
- **[Estimate: Gamalytic data, Oct 2025 snapshot of ~12,700 2025 releases; analysis by Soulash developer Artur Smiarowski]** — [Inven Global](https://www.invenglobal.com/articles/24127/steams-record-revenue-the-shrinking-space-for-new-releases); [MP1st](https://mp1st.com/news/40-of-steam-games-in-2025-earned-less-than-100); [DualShockers](https://www.dualshockers.com/steam-games-gross-over-100-thousand-less-than-steam-listing-fees/); [NeonLightsMedia](https://www.neonlightsmedia.com/blog/steam-game-releases-2025-fail-gamalytic-data); [Yahoo/GamesRadar syndication](https://tech.yahoo.com/gaming/articles/over-5-000-games-released-152604830.html):
  - 65.9% (8,388 games) grossed under $1,000.
  - About 40% grossed under $100, so they did not even cover the $100 Steam Direct fee.
  - About 8% (~1,140 games) grossed over $100k.
  - The bottom 30% averaged about $37 gross.
- **[Weak]** A median 2025 gross of $249, with 66% under $1,000 and 0.5% over $1M, attributed to "VG Insights / Alinea Analytics" — [Ziva.sh blog, Mar 2026](https://ziva.sh/blogs/indie-game-revenue). This is not verified against a VG Insights publication.
- **[Estimate: "We Love It" study by Totally Human Media, Sep 2026]** — [Game World Observer](https://gameworldobserver.com/2026/09/01/the-median-revenue-of-games-on-steam-has-been-declining-for-12-consecutive-years); [WN Hub](https://wnhub.io/news/stores-and-publishing/item-51948); [Mezha](https://mezha.ua/en/news/steam-games-statistics-315726/):
  - The median revenue of new releases has fallen for 12 consecutive years: about $15,000 for the 2016 cohort versus $1,728 for 2026 releases.
  - The 2026 cohort has been on sale for under a year, so this comparison is not like-for-like.
  - The study says only 14.4% of titles can expect more than $100,000.
  - The Steam catalog is growing faster than store revenue.
  - The firm's CEO, Ichiro Lambe, previously ran Steam Labs at Valve.
- **[Estimate]** Games-Stats reported a $290 median for a Q1 2026 sample — [Games-Stats](https://games-stats.com/blog/Steam_in_Q12026/).

**Success thresholds: over $100k and over $1M**
- **[Official: Valve, 2024 Year in Review, early 2025]** These counts cover only first-30-days revenue plus pre-orders — [GamesRadar](https://www.gamesradar.com/games/steams-new-game-revenue-is-10x-higher-than-it-was-10-years-ago-but-only-around-200-made-more-than-usd1-million-in-their-first-30-days/); [Tech4Gamers](https://tech4gamers.com/500-steam-games-earned-250k-last-year/):
  - More than 500 new games earned over $250k (+27% vs 2023).
  - More than 200 (later reported as 224) earned over $1M (+15%).
  - That is about 1% of 2024 releases.
- **[Official: Valve at GDC, Mar 10, 2026]** — [Game Developer](https://www.gamedeveloper.com/business/valve-says-5-836-titles-earned-over-100-000-on-steam-in-2025); [Game World Observer](https://gameworldobserver.com/2026/03/11/in-2025-nearly-6000-games-earned-over-100000-on-steam-a-record); [PC Gamer](https://www.pcgamer.com/gaming-industry/valve-says-over-5000-games-made-over-usd100k-on-steam-last-year/); [PCGamesN](https://www.pcgamesn.com/steam/2025-report-valve-gdc):
  - 5,863 games earned more than $100k on Steam in 2025, a record. Comparable figures: about 5,000 (2024), about 4,000 (2022), about 3,000 (2020).
  - The scope is unclear. PCGamesN says it "appears" to include games released before 2025, while [Outlook India](https://respawn.outlookindia.com/gaming/gaming-news/steam-growth-continues-as-5863-games-cross-100k-revenue-in-2025) described it as 2025 releases only.
  - Valve's Tom Giardino said $100k is "a drop in the ocean" for AAA but "a substantial reward for a solo developer," and that the trend holds at the $500k and $1M thresholds.
- **[Estimate: Alinea Analytics, 2025 Year in Review, covering Jan 1–Nov 20, 2025]** — [GameDev Reports](https://gamedevreports.substack.com/p/alinea-analytics-2025-year-in-review); [Notebookcheck](https://www.notebookcheck.net/Indie-games-accounted-for-25-of-Steam-s-revenue-in-2025.1189429.0.html):
  - Just over 300 of about 20,000 2025 releases grossed more than $1M, about 1.5%.
  - Indies were about 25% of Steam revenue, roughly $4.5B.
  - Top indie grossers: Schedule I $151M, R.E.P.O. $147M, PEAK $87M, Silksong $75M, Escape from Duckov $53M.
- **[Estimate: Chris Zukowski, Jan 2026]** Only 608 of 20,282 2025 releases (about 3.0%) reached 1,000 Steam reviews — [Shazoo](https://shazoo.ru/2026/01/29/178897/za-2025-god-v-steam-vyslo-bolee-20-tysiac-igr-no-tolko-608-polucili-bolee-1000-otzyvov). Zukowski says 1,000 reviews "typically correlates with revenue of $150,000+" — reported secondhand by [Steam Page Analyzer (Weak)](https://www.steampageanalyzer.com/blog/how-many-games-release-on-steam). At GDC 2025 he told developers to aim for at least 250 reviews in the first month — [WN Hub](https://wnhub.io/news/stores-and-publishing/item-47399).

**Concentration and long tail**
- **[Estimate: VG Insights Global Indie Games Market Report 2024, data through Sep 30, 2024]** — [Game World Observer](https://gameworldobserver.com/2024/10/16/indie-games-revenue-steam-vs-aaa-titles-vg-insights); [VGI report PDF](https://app.sensortower.com/vgi/assets/reports/VGI_Global_Indie_Games_Market_Report_2024.pdf); [GameDev Reports](https://gamedevreports.substack.com/p/video-game-insights-indie-games-on):
  - "Indie" earned about $4B on Steam, 48% of full-game revenue.
  - Growth was driven by Black Myth: Wukong and Palworld. Excluding Black Myth: Wukong, growth was 11%, which shows VGI's "indie" definition is very broad.
  - More than half of indie revenue came from "a handful of Triple-I games."
  - Revenue share by tier: Triple-I 53%, small teams 20%, middle market 19%, hobbyists 8%.
- **[Weak]** "The top 1% of games account for 84.6% of revenue" — [Beacon Digital PR blog, 2026](https://beacondigitalpr.com/indie-game-statistics-2026).
- **[Estimate: GameDiscoverCo, 2026]** Based on about 5,000 games released July 2023–July 2025 that sold at least 1,000 copies in their first month — [GameDev Reports summary](https://gamedevreports.substack.com/p/gamediscoverco-the-long-tail-of-steam):
  - Median revenue at the end of month 1 is 1.42× first-week revenue.
  - Year 1 is 2.46×, and year 2 is 2.99×.
  - The 2021 study found 3.05× for year 1, and the 2023 cohort 2.64–2.69×.
  - In other words, about 40% of year-one revenue arrives in the launch week.
- **[Survey: Zukowski reader survey, 160 games]** 2023–2025 launches sold about half as many first-month units per launch wishlist as 2020–2022 launches. The two groups contain 126 and 34 games respectively — [GameDev Reports](https://gamedevreports.substack.com/p/how-to-market-a-game-steam-wishlists).

**Methodology limits**
- Gamalytic estimates revenue from concurrent player counts, "an advanced version of the review multiplier method," and publicly disclosed sales. Figures are gross, before Valve's 30% cut, and exclude DLC and in-app purchases — [WN Hub](https://wnhub.io/news/stores-and-publishing/item-42136).
- Gamalytic's self-assessment says 77% of per-game estimates fall within ±30% and 98% within ±50%. Accuracy is worse for small and free-to-play games. Only Valve holds actual sales data — [DualShockers](https://www.dualshockers.com/steam-games-gross-over-100-thousand-less-than-steam-listing-fees/); [NeonLightsMedia](https://www.neonlightsmedia.com/blog/steam-game-releases-2025-fail-gamalytic-data).
- A vendor comparison says:
  - Gamalytic combines top-seller rank movements, concurrent players, and a "tuned Boxleiter-style review model" with regression on games whose sales are publicly confirmed.
  - VG Insights self-reports about 5% accuracy at the aggregate level.
  - Source: [Steam Page Analyzer (Weak)](https://www.steampageanalyzer.com/blog/steamdb-vs-steamspy-vs-vginsights).
- Denominators differ: Gamalytic's Oct-2025 snapshot covered about 12,700 2025 games, while SteamDB counted 18,015 by November — [MP1st](https://mp1st.com/news/18k-games-released-steam-2025-half-have-10-reviews). Shares from different trackers are therefore not strictly comparable.

### Inferences
- Robust base rate for a new Steam release, triangulated from Gamalytic, Valve, Alinea, Zukowski and the VGI 2019 cohort:
  - The median grosses about $1k or less.
  - About two-thirds gross under $1k–$5k.
  - About 8–14% gross over $100k (lifetime or first year, depending on source).
  - About 1–1.5% gross over $1M.
- After Valve's standard 30% cut, $100k gross is about $70k before refunds, VAT and income tax. Over a 3-year solo project, even a top-decile result is a modest wage (about $23k/year before tax).
- Restricting to serious commercial attempts improves the median a lot but not to a living. Gamalytic 2023 put the median at about $17k for games priced over $10. Many of the failures counted in the raw base rate are hobby projects, so a serious solo project's prior is better than the raw median but still poor.
- Supply roughly doubled from 2020 to 2025. The number of titles earning over $100k (Valve) also roughly doubled, from about 3,000 to 5,863, so the success *rate* has stayed roughly flat while the *median* fell (We Love It study).

### Gaps
- Primary pages could not be opened, so definitions could not be confirmed. Examples: whether Valve's 5,863 includes back-catalog titles, and the cohort and time window behind each percentile.
- No consistent P25/P75/P90 tables for 2024–2026 cohorts were found.
- VG Insights' own 2025 report was not found, so the $249 median is unverified.
- A search extract claimed only 3,973 (~20%) of 2024 releases had Steam community features enabled. I could not tie it to a specific source, so it is excluded.
- The Boxleiter method's commonly quoted review-to-sales multipliers could not be sourced in this session (the search returned nothing relevant).

## 2. Solo developers: share of releases and outcomes vs. small teams

### Takeaway
I found no public dataset that measures what share of Steam releases come from solo developers, or that directly compares solo and team revenue. The best proxies point the same way:
- Most releases are hobbyist or 1–2-person projects that earn very little.
- Developers above $1M are "typically a team."
- The one direct (and old) income comparison found solo indies averaging about a quarter of indie team members' income.

### Cited Findings
- **[Estimate: VG Insights 2024 report]** VGI's tiers — [Game World Observer](https://gameworldobserver.com/2024/10/16/indie-games-revenue-steam-vs-aaa-titles-vg-insights); [VGI report PDF](https://app.sensortower.com/vgi/assets/reports/VGI_Global_Indie_Games_Market_Report_2024.pdf):

  | Tier | Team size | Rule-of-thumb lifetime revenue | Share of 2024 indie revenue |
  |---|---|---|---|
  | Hobbyists ("typically solo developers where the focus is more on creativity than business") | 1–2 people | ~$50K | 8% |
  | Small teams | 3–15 | ~$1M | 20% |
  | Middle market | 15–50 | ~$10M | 19% |
  | Triple-I | 50+ | $50M+ | 53% |

- **[Estimate: Gamalytic, Sep 2023]** More than 70% of games released on Steam in the prior three years were hobbyist projects — [WN Hub](https://wnhub.io/news/stores-and-publishing/item-42136).
- **[Estimate: VG Insights, "There are 44,000 game developers on Steam," c. 2023]** — [Game Developer](https://www.gamedeveloper.com/game-platforms/there-are-44-000-game-developers-on-steam-who-are-they-); [GameDev Reports](https://gamedevreports.substack.com/p/there-are-44000-developers-in-steam):
  - 75% of Steam developers have released only one game. Only 443 have released more than 10.
  - About 57% of developers have never made $1k in gross revenue. These are almost all one-game developers, often hobby or learning projects.
  - About one-third work with publishers. Only 4% (about 1,900) have tried both self-publishing and a publisher.
- **[Estimate: VG Insights, "What can we learn from the 1,600 highest earning indie developers on Steam?"]** — [Game Developer](https://www.gamedeveloper.com/game-platforms/what-can-we-learn-from-the-1-600-highest-earning-indie-developers-on-steam-):
  - Only about 10% of Steam developers have ever made more than $100k gross.
  - Developers above $1M gross are "typically a team, not a solo dev."
  - Top developers keep releasing, and later games tend to earn more. Example: Reiza Studios' first game earned under $100k, each later release earned more, and Automobilista 2 (2020) made millions.
- **[Survey: Gamasutra Game Developer Salary Survey 2014, covering 2013 income, more than 4,000 responses]** — [Game Developer](https://gamedeveloper.com/audio/game-developer-salary-survey-2014-the-results-are-in-); [GameSkinny](https://www.gameskinny.com/news/report-most-indie-game-devs-made-less-than-500-in-game-sales-in-2013/); [MCV](https://www.mcvuk.com/business/average-game-developer-salary-down-from-2012):
  - Non-salaried **solo** indie developers averaged $11,812 (−49% YoY).
  - Members of indie **teams** averaged $50,833 (+161%).
  - Both averages exclude people earning under $10k or over $200k.
  - 57% of all indies, solo and team, earned under $500 from game sales. 2% reported more than $200k.
  - Gamasutra warned that indie averages fluctuate a lot from year to year.
- **[Official: Valve, GDC 2026]** Giardino called $100k "a substantial reward for a solo developer" — [Game World Observer](https://gameworldobserver.com/2026/03/11/in-2025-nearly-6000-games-earned-over-100000-on-steam-a-record).
- **[Estimate: GameDiscoverCo solo-developer case studies — anecdotes, selected on success]**
  - Rooftops & Alleys (solo, Berlin) sold about 70k units on Steam in its first month — [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-this-solo-dev-parkour-game-sold).
  - Gnorp Apologue (solo developer, Norway) was the #4 new Steam game of Dec 2023 by copies. GameDiscoverCo's "solo-dev 'incremental' game hit 100k+ sales" piece appears to be about this game, but the pairing was not confirmed from the full page — [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-this-solo-dev-incremental-game).
  - A solo-developer 3D "gladiator sim" sold 10k units in its first 24 hours — [GameDiscoverCo](https://newsletter.gamediscover.co/p/analysis-how-a-solo-dev-gladiator).
- **[Estimate: Alinea 2025]** The top-grossing 2025 indie, Schedule I (about $151M), launched as essentially a one-person project — [GameDev Reports](https://gamedevreports.substack.com/p/alinea-analytics-2025-year-in-review); [PC Gamer](https://www.pcgamer.com/games/sim/schedule-1-is-the-kind-of-instant-steam-hit-that-was-only-ever-going-to-come-from-a-complete-rando/).
- Academic work: postmortem studies exist, but none found reports commercial outcome by team size.
  - Washburn et al. (ICSE 2016) analysed 155 Gamasutra postmortems — [paper PDF](https://thomas-zimmermann.com/publications/files/washburn-icse-2016.pdf).
  - "What Makes a Game High-rated?" coded team size for 170 of 200 postmortems, with solo = 1, but it studies ratings, not revenue — [arXiv 2105.14137](https://arxiv.org/pdf/2105.14137).
  - A Tampere thesis analyses indie postmortems, but its findings were not visible in the extract — [Suorsa thesis](https://trepo.tuni.fi/handle/10024/102593).

### Inferences
- Revenue in the 1–2-person segment is very low relative to its volume:
  - Hobbyists made up more than 70% of releases (Gamalytic) but took about 8% of indie revenue (VGI).
  - So the *typical* solo release earns far less than the typical small-team release.
  - Much of this gap is selection: learning and hobby projects, and the fact that promising projects attract funding and team members. Solo development is not by itself shown to cause worse results.
- Per person, solo developers do not split revenue. $100k gross for a solo game is per-head equivalent to $300k for a three-person team. The 2014 survey's 4× gap in average income (solo vs. team member) suggests teams still out-earn solo developers per head on average.
- A first-time solo developer should use the Section 1 base rates, adjusted downward:
  - 75% of Steam developers never release a second game.
  - VGI's top earners show earnings growing with each successive release.
  - A first game is mostly a learning investment.

### Gaps
- I found no data on what share of Steam or itch.io releases come from solo developers. SteamDB, Gamalytic and VGI do not tag team size, and no Zukowski or GameDiscoverCo solo-vs-team breakdown was found.
- No GDC State of the Game Industry breakdown of outcomes for solo respondents was found.
- The following claims appear only in SEO-style blogs (e.g., [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/how-much-do-indie-game-developers-make), [Shane the Gamer](https://www.shanethegamer.com/research/indie-games-statistics/)) and could not be traced to a primary source. They should **not** be used as facts:
  - "Only 15% of solo developers take home more than $100k annually (VGI)."
  - "Only 3% of indie developers ever pass $1M."
  - "Debut games average about $120k, second $168k, third $209k."
  - "86% of solo developers self-fund (GDC 2026)."
  - "70% of solo/indie projects fail."

## 3. Developer income, making a living, and projects that never ship

### Takeaway
No current, representative survey measures what share of indie or solo developers make a living from games. The available proxies imply a small minority:
- Developer-level lifetime gross on Steam: about 57% under $1k and about 10% over $100k.
- The 2014 salary survey found 57% of indies earned under $500 from game sales.

For PC/indie projects that never ship, no data was found. The closest proxy is mobile: 43% of games cancelled during development.

### Cited Findings
- **[Estimate: VG Insights, c. 2023]** Of about 44,000 Steam developers, about 57% have lifetime gross under $1k and about 10% have ever exceeded $100k gross — [Game Developer (44k devs)](https://www.gamedeveloper.com/game-platforms/there-are-44-000-game-developers-on-steam-who-are-they-); [Game Developer (1,600 top devs)](https://www.gamedeveloper.com/game-platforms/what-can-we-learn-from-the-1-600-highest-earning-indie-developers-on-steam-).
- **[Survey: Gamasutra 2014]** 57% of indies earned under $500 from game sales in 2013. Averages: solo $11,812 and indie team member $50,833 (excluding under $10k and over $200k) — [Game Developer](https://gamedeveloper.com/audio/game-developer-salary-survey-2014-the-results-are-in-); [GameSkinny](https://www.gameskinny.com/news/report-most-indie-game-devs-made-less-than-500-in-game-sales-in-2013/).
- **[Survey: GDC State of the Game Industry 2025, more than 3,000 respondents, ±2%]** — [Game Developer](https://www.gamedeveloper.com/business/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more); [80.lv](https://80.lv/articles/one-in-ten-developers-lost-their-jobs-in-2024-according-to-gdc-report/):
  - 11% were laid off in the past year.
  - 41% said their company was affected by layoffs, up from 35% the year before.
- **[Survey: GDC State of the Game Industry 2026, 2,300+ respondents, published Jan 29, 2026]** — [GDC](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [BusinessWire](https://www.businesswire.com/news/home/20260129438528/en/2026-State-of-the-Game-Industry-Report-Reveals-Widening-Effect-of-Layoffs-Broader-Perspectives-on-Generative-AI-Unionization-Tariffs-and-More); [GamesBeat](https://gamesbeat.com/state-of-game-industry-survey-sheds-light-on-layoffs-genai-views-unionization-and-tariffs-gdc-survey/):
  - 28% of respondents were laid off in the past two years (33% in the US).
  - Half say their current or most recent employer had layoffs in the past 12 months.
  - 74% of the 50 students surveyed worry about job prospects.
- **[Survey: SuperScale / Atomik Research, 2023, 504 UK/US mobile developers]** 43% of mobile games are cancelled during development, and 83% of those released shut down within three years — [PocketGamer.biz](https://www.pocketgamer.biz/news/82908/almost-half-of-all-mobile-games-are-axed-in-development-and-83-dont-last-three-years/).
- Chris Zukowski (How To Market A Game) built his consultancy while working a corporate UX job and went full-time only in 2019, once he had paying clients. He advises developers not to quit their day jobs — [Freaking Cool Indies profile](https://freakingcoolindies.com/chris-z-teaches-indie-devs-to-build-an-audience-heres-how-he-built-his/).
- Several hit-makers kept a job for most of development:
  - Tom Happ worked full-time at Petroglyph for 4 of Axiom Verge's 5 years — [Thomas Happ Games](https://www.thomashapp.com/about).
  - Animal Well was a part-time side project for about 4 years alongside a full-time job — [Noisy Pixel](https://noisypixel.net/animal-well-2024-indie-game-success/).
  - LocalThunk became a full-time developer only in Jan 2023 — [Balatro Wiki](https://balatrowiki.org/w/LocalThunk).
- Scope slips and abandonment are common even among eventual hits:
  - Lethal Company was "initially planned to be completed within 6 months" — [Wikipedia](https://en.wikipedia.org/wiki/Lethal_Company).
  - LocalThunk shelved Balatro for about 3 months in 2022 — [PC Gamer](https://www.pcgamer.com/games/localthunk-gave-up-making-balatro-for-3-months-but-resumed-because-i-was-bored-but-the-internet-was-out-so-i-couldnt-play-rocket-league/).
  - Zeekerss's text adventure (Welcome to the Dark Place) took about 10 years on and off and was finally released free — [GamesRadar](https://www.gamesradar.com/games/horror/solo-dev-behind-one-of-steams-biggest-viral-hits-lethal-company-gives-his-new-game-away-for-free-after-10-years-of-work-i-only-want-to-sell-a-game-if-im-very-certain-that-most-people-will-enjoy-it/).

### Inferences
- Living from games alone is plausibly a low-single-digit to ~10% outcome among developers who ship on Steam, and lower among first-time solo developers. Reasoning: only about 10% of Steam developers ever exceed $100k *lifetime* gross, Valve keeps 30%, and a living requires that income *per year*. This is an inference, not a measured survey figure.
- The common thread among hit-makers is keeping outside income during development (day job, savings, partner, or a separate revenue stream). Blue Prince was funded from savings plus ad revenue from a Magic: The Gathering fan site (see Section 4).

### Gaps
- No recent, representative income survey of indie or solo developers was found. The GDC surveys found do not publish income by indie/solo status.
- Blog claims are unverified and should not be used: "5–10% make a full-time living," "most indies make under $20k/year," "GDC 2021: 30% of indies earned under $10k," and "18.2% of Early Access games abandoned" ([VoxBooster](https://voxbooster.com/blog/early-access-game-statistics-2026/)).
- I found no data on what share of indie PC projects or announced Steam "Coming Soon" pages never ship.
- itch.io statistics were not collected because the search budget ran out.

## 4. Profiles of notable solo / near-solo hits

### Takeaway
Almost every famous "solo" hit had three things:
1. A developer with years of prior depth in at least one core discipline, usually programming (several were professional game programmers) or, for Toby Fox, music.
2. Either a small, tightly scoped design built quickly, or a 4.5–8-year grind, often done alongside a day job.
3. Help with the weakest discipline: hired art or music, bought asset packs, or a publisher.

Seven of the 13 are 2D pixel-art games. Of the six 3D ones, two were made by experienced programmers or game-makers (Banished, Lethal Company), and one (Blue Prince) had a dedicated art director and other staff.

### Cited Findings

**Stardew Valley (2016) — Eric Barone (ConcernedApe)**
- Development took at least 4.5 years: "at least 8 hours a day," about 10 hours a day "every day of the week" — [Game Developer (crunch interview)](https://www.gamedeveloper.com/business/the-4-years-of-self-imposed-crunch-that-went-into-i-stardew-valley-i-); [GoNintendo](https://www.gonintendo.com/archives/255188-stardew-valley-dev-spent-4-5-years-creating-the-game-talks-about-solo-development). Wikipedia says about 5 years, counting from the earlier "Sprout Valley" — [Wikipedia](https://en.wikipedia.org/wiki/Stardew_Valley).
- He was the sole developer, including all pixel art, music and sound effects — [Wikipedia](https://en.wikipedia.org/wiki/Stardew_Valley). The publisher was Chucklefish — [Wikipedia: Chucklefish](https://en.wikipedia.org/wiki/Chucklefish).
- Background:
  - He taught himself game-making while studying computer science.
  - The project began as a Harvest Moon clone "to teach himself how to code in C#" — [Game Developer (Road to the IGF)](https://www.gamedeveloper.com/design/road-to-the-igf-concernedape-s-i-stardew-valley-i-).
  - He could not find programming work after graduating in 2011 and worked as a theater usher when production began — [GameRevolution](https://www.gamerevolution.com/originals/13384-stardew-valleys-single-developer-has-made-over-30-million).
- Style: 2D pixel art.
- Sales **[developer-claimed]**: more than 41M copies across platforms (more than 26M on PC, 7.9M on Switch) — [VGC](https://videogameschronicle.com/news/stardew-valley-has-now-sold-more-than-40-million-copies). It passed 30M in early 2024 — [WN Hub](https://wnhub.io/news/other/item-42973).

**Undertale (2015) — Toby Fox**
- Development took about 2.7 years — [Wikiversity (Weak)](https://en.wikiversity.org/wiki/Digital_Media_Concepts/Toby_Fox).
- It was funded on Kickstarter: a $5,000 goal, about 10× raised, nearly 2,400 backers — [Wikipedia](https://en.wikipedia.org/wiki/Undertale); [Kickstarter interview](https://medium.com/kickstarter/undertale-creator-toby-fox-on-the-indie-computer-game-that-s-become-an-industry-darling-fa4df6cee2db).
- Engine: GameMaker Studio. Fox had already built a battle system in GameMaker before starting — [Wikipedia](https://en.wikipedia.org/wiki/Undertale).
- **Not fully solo:** Temmie Chang contributed art and character designs and was "primarily responsible" for complex elements, including cutscenes and several characters. Fox: "it's really time-consuming to develop all aspects of the game. So I hired artists like Temmie Chang" — [Wikipedia: Temmie Chang](https://en.wikipedia.org/wiki/Temmie_Chang); [Kickstarter interview](https://medium.com/kickstarter/undertale-creator-toby-fox-on-the-indie-computer-game-that-s-become-an-industry-darling-fa4df6cee2db).
- Prior expertise: he was known as a composer for the webcomic Homestuck. Megalovania was originally intended for Homestuck — [Gamers Decide (Weak)](https://gamersdecide.com/pc-game-news/what-undertale-and-who-toby-fox).
- Style: 2D, deliberately simple pixel art.
- Sales **[Weak, conflicting]**: more than 1M by 2016 ([Gamers Decide](https://gamersdecide.com/pc-game-news/what-undertale-and-who-toby-fox)); about 6.3M on Steam per a VGI-attributed estimate ([Levvvel](https://levvvel.com/undertale-statistics/)).

**Axiom Verge (2015) — Tom Happ**
- One person made "the entire game (programming, design, art, animations, music)" during "evenings and weekends over the course of 5 years" — [Axiom Verge press release](http://www.axiomverge.com/press-releases).
- He began in March 2010 as a side project — [Wikipedia](https://en.wikipedia.org/wiki/Axiom_Verge). An earlier report said four years — [Siliconera](https://www.siliconera.com/axiom-verge-one-guys-four-year-effort-create-metroidvania/).
- Prior expertise: a professional game programmer, full-time at Petroglyph Games for 4 of the 5 years (on End of Nations) — [Thomas Happ Games](https://www.thomashapp.com/about); [Nintendo Life](https://www.nintendolife.com/news/2016/09/interview_learning_more_about_tom_happ_and_the_making_of_axiom_verge).
- Engine: C# on XNA, later MonoGame/FNA for ports; Wii U required porting the engine to C++ — [Windows Central](https://www.windowscentral.com/axiom-verge-pax-east-interview); [Hanselminutes](https://hanselminutes.com/605/thomas-happ-from-axiom-verge).
- Style: 2D pixel art, Metroid-like.
- A fan-wiki claim of Sony funding is unconfirmed — [Axiom Verge fandom (Weak)](https://axiom-verge.fandom.com/wiki/Thomas_Happ).

**Cave Story (2004) — Daisuke "Pixel" Amaya**
- About 5 years of development in his free time. He did all the art, music, writing and programming. Released as freeware on Dec 20, 2004 — [Wikipedia](https://en.wikipedia.org/wiki/Daisuke_Amaya); [Game Developer](https://www.gamedeveloper.com/design/the-solitary-creativity-of-pixel); [Kotaku AU archive](https://archive.cavestory.one/kotakuau/).
- A documentary summary says he worked full-time for a printer company — [TheTVDB/ThatGuyGlen (Weak)](https://thetvdb.com/series/thatguyglen/episodes/9465055).
- Style: 2D pixel art, an homage to Metroid, Blaster Master and Castlevania.

**Lethal Company (Early Access Oct 23, 2023) — Zeekerss**
- Solo developer and self-publisher. Engine: Unity. Price: $10. Style: 3D — [Wikipedia](https://en.wikipedia.org/wiki/Lethal_Company).
- Prior expertise: making games on Roblox since 2012. First Steam game was It Steals (July 2020), followed by The Upturned — [Wikipedia: Zeekerss](https://en.wikipedia.org/wiki/Zeekerss). One source claims 19 games before Lethal Company — [Pushtotalk (Weak)](https://www.pushtotalk.gg/p/how-lethal-company-sold-10-million-copies).
- Planned development time was 6 months — [Wikipedia](https://en.wikipedia.org/wiki/Lethal_Company). The actual time was not verified.
- Sales **[Estimates]**:
  - GameDiscoverCo estimated about 642k units and $5.7M projected gross by mid-Nov 2023 — [Game World Observer](https://gameworldobserver.com/2023/11/16/lethal-company-sales-640k-copies-57k-ccu-new-indie-hit-zeekerss).
  - Later reports say more than 10M copies — [Wikipedia](https://en.wikipedia.org/wiki/Lethal_Company).

**Balatro (Feb 20, 2024) — LocalThunk**
- The project folder dates from Dec 13, 2021, so about 2.2 years to release. Wikipedia says about 2.5 years — [LocalThunk timeline](https://localthunk.com/blog/balatro-timeline-3aarh); [Wikipedia](https://en.wikipedia.org/wiki/Balatro).
- It began during a vacation from his job. He became a full-time developer in Jan 2023 — [Balatro Wiki](https://balatrowiki.org/w/LocalThunk). Bloomberg describes him as a former IT worker — [Bloomberg interview repost](https://icon-era.com/threads/bloomberg-interview-with-balatro-developer-localthunk.15875/).
- Engine: LÖVE (Lua).
- **Outsourced:** music by Luis Clemente (LouisF). Publisher: Playstack — [Wikipedia](https://en.wikipedia.org/wiki/Balatro).
- Style: 2D, "hand-drawn pixel art," with the game "built almost entirely by one person" — [Globe and Mail](https://theglobeandmail.com/arts/article-inside-the-stunning-success-of-balatro-the-video-game-sensation-made).
- Sales **[Official, publisher]**: more than 5M by Jan 20, 2025 — [Niche Gamer](https://nichegamer.com/balatro-tops-5-million-copies-sold/); [WN Hub](https://wnhub.io/news/investment/item-46849).

**Animal Well (May 2024) — Billy Basso (Shared Memory)**
- About 7 years of development. The first ~4 years were part-time while he held a full-time job — [Noisy Pixel](https://noisypixel.net/animal-well-2024-indie-game-success/).
- Engine: a custom C++ engine started in 2014 in off-hours, after a 2012 Metroidvania prototype, with a built-in level editor — [Game Developer (engine)](https://www.gamedeveloper.com/design/why-animal-well-s-home-brewed-engine-was-key-to-its-success); [Game Developer (GDC talk)](https://www.gamedeveloper.com/programming/the-scratch-coding-and-discipline-at-the-heart-of-animal-well).
- Prior expertise: about 10 years "programming games at larger studios including Netherrealm, Phosphor Games, and Level Ex" — [Official site](https://www.animalwell.net/).
- Publisher: Bigmode (Dunkey) — [Gameranx](https://gameranx.com/tag/animal-well/). He used Reaper for audio — [Noisy Pixel](https://noisypixel.net/animal-well-2024-indie-game-success/).
- Style: 2D pixel art.

**Vampire Survivors — Luca Galante (poncle)**
- He started in 2020 with the Phaser (HTML5/JavaScript) framework, using default engine assets — [Game Developer](https://www.gamedeveloper.com/design/vampire-survivors-development-sounds-like-an-open-source-fueled-fever-dream); [Wikipedia](https://en.wikipedia.org/wiki/Vampire_Survivors).
- **Bought art:** he swapped in a Castlevania-inspired asset pack he had bought years earlier. He spent "a total of £1100 on assets… between the illustrations and the sounds" — [PC Gamer](https://www.pcgamer.com/vampire-survivors-didnt-rip-off-castlevania-sprites-after-all/).
- Prior expertise: several years in the gambling industry making virtual slot machines in London, where he learned JavaScript and HTML5. Slot-machine visual knowledge shaped the chest openings. He quit in Feb 2022 — [Multiplayer.it interview](https://multiplayer.it/articoli/vampire-survivors-intervista.html); [Multiplayer.it](https://multiplayer.it/notizie/vampire-survivors-ha-salvato-il-suo-autore-dal-lavorare-ai-giochi-dazzardo-per-sistemi-mobile.html); [Wikipedia](https://en.wikipedia.org/wiki/Vampire_Survivors).
  - Conflict: Wikipedia also says he was unemployed when development began in 2020.
- Style: 2D pixel art from asset packs.

**Buckshot Roulette (itch.io first, then Steam) — Mike Klubnika**
- Made in about 2 months. Engine: Godot. Released on itch.io first, then Steam — [GamesRadar](https://www.gamesradar.com/games/horror/he-made-a-viral-horror-game-in-2-months-it-sold-6-million-copies-and-now-he-can-make-whatever-he-wants-for-the-rest-of-his-life-my-final-theory-is-that-gambling-is-very-fun/); [Wikipedia](https://en.wikipedia.org/wiki/Buckshot_Roulette).
- Described as a "tabletop horror" game — [DEV Community](https://dev.to/wlz/why-buckshot-roulette-bet-on-godot-the-free-engine-behind-a-4-million-copy-tabletop-horror-3dpb). Its 3D first-person presentation was not re-verified from extracts (see Gaps).
- Sales **[Reported; rising over time]**:
  - About 1M on Steam in two weeks — [Wikipedia](https://en.wikipedia.org/wiki/Buckshot_Roulette).
  - More than 4M — [Noisy Pixel](https://noisypixel.net/buckshot-roulette-ps5-ps4-nintendo-switch-4-million-sales/).
  - More than 6M — [GamesRadar](https://www.gamesradar.com/games/horror/he-made-a-viral-horror-game-in-2-months-it-sold-6-million-copies-and-now-he-can-make-whatever-he-wants-for-the-rest-of-his-life-my-final-theory-is-that-gambling-is-very-fun/).
  - More than 8M — [GameDaily via NewsBreak](https://www.newsbreak.com/gamedaily-333497653/4416300265064-buckshot-roulette-started-off-free-now-it-s-sold-over-8-million-copies).
- He became a Godot "Platinum" sponsor at €36,000 per year — [WN Hub](https://wnhub.io/news/engines/item-50134).

**Schedule I (Early Access 2025) — Tyler (TVGS), Australia**
- "Besides the music and some graffiti art, Schedule 1 was entirely made by one guy in Australia named Tyler" — [PC Gamer](https://www.pcgamer.com/games/sim/schedule-1-is-the-kind-of-instant-steam-hit-that-was-only-ever-going-to-come-from-a-complete-rando/).
- Engine: Unity — [Wikipedia](https://en.wikipedia.org/wiki/Schedule_I_(video_game)). Style: 3D.
- Prior expertise: "almost a decade" of non-professional game development — [daily.dev summary (Weak)](https://daily.dev/posts/how-schedule-1-was-created-by-a-22-year-old-dev-uhosjxlol); [ScreenRant](https://screenrant.com/schedule-1-creator-tyler-age/).
- A claim of "three years" of development using Unity plus Blender is unverified — [Fryos Studios (Weak)](https://fryosstudios.com/how-tyler-created-schedule-i-the-open-world-crime-game-by-a-solo-developer-and-how-small-studios-can-make-a-huge-impact/).
- After launch, TVGS became a studio with a Sydney office and expected "likely 4 people" by year-end — [PC Gamer via Yahoo](https://tech.yahoo.com/gaming/articles/schedule-1-developer-tvgs-actual-210136373.html). In Apr 2025, he said 1.0 was "two to three years" away — [TheGamer](https://www.thegamer.com/schedule-1-relase-date-leave-early-access-two-three-years/).
- Sales **[Estimates]**:
  - Gamalytic: about 9M copies (range 6.4M–11.7M) — [Gamalytic](https://gamalytic.com/game/3164500).
  - Alinea: $151M gross in 2025 — [GameDev Reports](https://gamedevreports.substack.com/p/alinea-analytics-2025-year-in-review).

**Blue Prince (2025) — Tonda Ros / Dogubomb (near-solo; a small team, not solo)**
- Credits — [Wikipedia](https://en.wikipedia.org/wiki/Blue_Prince); [Unity blog](https://unity.com/blog/blue-prince-why-dogubomb-watched-2000-hours-gameplay):
  - Tonda Ros: director, designer and writer.
  - Davide Pellino: artist / art director, who worked with Ros for several years on the look.
  - Axel Haavikko: producer.
  - Trigg & Gusset: composers.
  - Engine: Unity. Publisher: Raw Fury.
- About 8 years of development, from around 2016 — [WN Hub](https://wnhub.io/news/other/item-47631). One reviewer said more than 10 years — [Andrea Blythe](https://andreablythe-games.com/2025/07/16/blue-prince-is-the-best-game-ive-played-thats-ultimately-not-for-me/).
  - Ros reportedly had no prior game-development experience.
  - The game was playable by 2021; later years went to balancing and polish — [WN Hub](https://wnhub.io/news/other/item-47631).
- The first prototype used Unity Asset Store assets and cube rooms — [Unity blog](https://unity.com/blog/blue-prince-why-dogubomb-watched-2000-hours-gameplay).
- Funded from personal savings plus ad revenue from a Magic: The Gathering fan site — [Wikipedia](https://en.wikipedia.org/wiki/Blue_Prince).
- Style: 3D, first-person, inspired by Myst and Riven — [Thinky Games](https://thinkygames.com/features/interview-how-myst-riven-and-tabletop-games-built-the-foundation-of-blue-prince/).

**Banished (Feb 18, 2014) — Luke Hodorowicz (Shining Rock Software)**
- Sole developer. Spent "three years developing my own technology and a first game." Before that, he spent 10 years in the industry "coding graphics engines and tools for consoles" — [Shining Rock: About](https://shiningrocksoftware.com/about/).
- Logged more than 5,500 hours — [Wikipedia](https://en.wikipedia.org/wiki/Banished_(video_game)). Development began Aug 2011 — [Game Grumps fandom (Weak)](https://gamegrumps.fandom.com/wiki/Banished).
- He handled programming, graphics and sound himself — [Pressakey (German press release)](https://pressakey.com/news,4046,Banished-Indie-Aufbau-Strategiespiel-erscheint-im-Februar,.html).
- Engine: custom. He later wrote his own GPU shading language — [Slashdot, 2015](https://developers.slashdot.org/story/15/03/31/172205/developer-of-banished-develops-his-own-shading-language).
- Style: 3D city builder.
- It topped Steam's sales chart in launch week — [PC Invasion](https://www.pcinvasion.com/?p=74451). It later had about 42,500 reviews, 90% positive — [Mein-MMO](https://mein-mmo.de/die-10-besten-spiele-steam-solo-dev/2/). No unit sales were found.

**A Short Hike (2019) — Adam Robinson-Yu**
- It began in Dec 2018 as a personal art project during a break from his RPG.
  - About 4 months later (Apr 2019) it shipped as a Humble Monthly exclusive.
  - Full PC release: Jul 30, 2019. Switch: Aug 18, 2020.
  - Sources: [Wikipedia](https://en.wikipedia.org/wiki/A_Short_Hike); [Press kit](https://ashorthike.com/press/); [Game Developer (Road to the IGF)](https://www.gamedeveloper.com/business/road-to-the-igf-adam-robinson-yu-s-i-a-short-hike-i-).
- Robinson-Yu did programming, art, level design, sound design and writing.
- **Outsourced/collaborators:**
  - All music by Mark Sparling, adaptive by area. Robinson-Yu knew him from game-jam work.
  - Dawn Blair and Andrew Wong contributed art and writing.
  - Sources: [Press kit](https://ashorthike.com/press/); [Fan wiki: Music](https://ashorthike.fandom.com/wiki/Music).
- Engine: Unity. Style: 3D — [Wikipedia](https://en.wikipedia.org/wiki/A_Short_Hike).

### Inferences
Summary compiled from the cited findings above. "n/v" means not verified in this session.

| Game | Who did what | Dev time | Prior deep expertise | Engine | 2D/3D |
|---|---|---|---|---|---|
| Stardew Valley | Solo, including art and music; publisher Chucklefish | 4.5–5 yrs, ~10 h/day | CS training; learned C# on the project | C# (framework n/v) | 2D pixel |
| Undertale | Fox plus hired artists (Temmie Chang: cutscenes, characters) | ~2.7 yrs | Established composer | GameMaker | 2D pixel |
| Axiom Verge | Solo, including music | ~5 yrs, evenings/weekends | Professional game programmer (Petroglyph) | C#/XNA → MonoGame/FNA | 2D pixel |
| Cave Story | Solo, including music | ~5 yrs, spare time | n/v (day job reported) | n/v | 2D pixel |
| Lethal Company | Solo | planned 6 months; actual n/v | Making games since 2012 (Roblox), then earlier Steam games from 2020 | Unity | 3D |
| Balatro | Solo; music LouisF; publisher Playstack | ~2.2–2.5 yrs | IT worker | LÖVE | 2D pixel |
| Animal Well | Solo; publisher Bigmode | ~7 yrs (4 part-time) | ~10 yrs pro game programmer | custom C++ | 2D pixel |
| Vampire Survivors | Solo plus bought asset packs (~£1,100) | started 2020 | Slot-machine game programmer (JS) | Phaser | 2D pixel |
| Buckshot Roulette | Solo | ~2 months | n/v | Godot | 3D |
| Schedule I | Solo except music and some graffiti art | n/v | ~decade of hobby game development | Unity | 3D |
| Blue Prince | Small team (art director, producer, composers) | ~8 yrs | reportedly none in games | Unity | 3D |
| Banished | Solo, including graphics and sound | ~3 yrs, 5,500+ h | 10 yrs console graphics-engine programmer | custom | 3D |
| A Short Hike | Solo core; music Mark Sparling; art and writing help | ~4–7 months | n/v | Unity | 3D |

- **Depth-plus-breadth ("T-shaped"), not shallow generalism.** Roughly 9 of 13 developers had prior depth in one core discipline (Tyler's rests on a weak source): Happ, Basso, Hodorowicz, Galante, LocalThunk and Barone in programming; Fox in music; Zeekerss and Tyler through about a decade of hobby game-making. They were broad in *production* but deep in at least one craft. Where they lacked depth, they usually bought or borrowed it:
  - Fox hired artists.
  - LocalThunk, Tyler and Robinson-Yu used outside composers.
  - Galante bought sprite and sound packs.
  - Ros worked with an art director.
  - This complicates the user's framing in both directions. These are not "jack of all trades, master of none" cases, but they are not single-discipline specialists either.
- **Two development patterns:**
  - Tiny scope shipped fast: Buckshot Roulette (~2 months), A Short Hike (~4–7 months), Vampire Survivors.
  - Long grinds of 4.5–8 years: Stardew Valley, Axiom Verge, Cave Story, Animal Well, Blue Prince.
  - The long grinds were typically funded by a day job, savings or a side business.
- **3D solo hits:** five near-solo games here are 3D. Banished came from a veteran console graphics-engine programmer. Lethal Company, Buckshot Roulette and Schedule I are horror, tabletop or sim designs. None is a character-animation-heavy game with high-fidelity character art. That last point is my inference: their visual styles were not verified in this session.
- **Survivorship caveat:** these 13 were selected *because* they succeeded. Thousands of games share their traits (solo, multi-year, generalist) and sit in the "under $1k" bucket from Section 1. The profiles show what was *possible* and which preconditions were common among winners. They cannot show the odds.

### Gaps
Searches ran out before these could be verified:
- Lethal Company's actual development time and art pipeline (models, animation, music credits).
- Buckshot Roulette developer's background and art or music credits.
- Animal Well's music credit and sales.
- A Short Hike's sales and Robinson-Yu's prior job.
- Cave Story's engine and the developer's day job (only a weak source).
- Stardew's framework (XNA/MonoGame), and whether Barone redid his art.
- Undertale's verified sales.
- Banished's unit sales.
- The 2D/3D labels for Lethal Company, Buckshot Roulette, Schedule I, Blue Prince, Banished and A Short Hike come from general knowledge of these widely played games, not from search extracts. They are uncontroversial but were not re-verified. Specific art-style claims, such as "low-poly with retro post-processing," are deliberately not made.
- Undertale's "2.7 years" comes from a weak secondary page.

## 5. 3D vs 2D for solo developers; cost of 3D character art and animation

### Takeaway
No dataset was found that measures solo success rates for 3D versus 2D games. The evidence available:
- Pixel-art data shows 2D is **not** a safer bet: roughly 5–10% of pixel-art games hit modest success thresholds, versus about 10% for other categories.
- Several of the biggest 2023–2025 small-team hits are 3D, so 3D is clearly in demand.
- 3D character production is expensive if outsourced: about $1k–$6k per stylized character before rigging and animation, plus $200–$1,000 per animation cycle. If self-made, it is very time-intensive.

### Cited Findings
- **[Estimate: Game Oracle]** About 10% of games in other categories sell more than 10,000 copies, versus 7–9.6% for 2D pixel-art games. The author says claims of pixel-art oversaturation "are not unfounded" — [Game Oracle](https://www.game-oracle.com/blog/deep-dive-2D-pixel-art-part-1).
- **[Estimate: Gamalytic data analysed by OP Game Marketing, ~2025]** Of 6,422 pixel-art games released over two years, only 343 (about 5%) reached 500 or more reviews. The author also notes "a trend of successful pixel art games moving to 3D art for their sequels" — [OP Game Marketing](https://opgamemarketing.substack.com/p/so-youre-making-a-pixel-art-game).
- **[Opinion]** Solo developers can make 3D games, but it is "a more challenging path" — [Game Dev Dairy](https://gamedevdairy.substack.com/p/should-solo-game-developers-do-3d); [Game Dev Dairy: Risks of solo 3D](https://gamedevdairy.substack.com/p/risks-of-solo-3d). A vendor blog argues the idea that "3D automatically sells better" is not supported by data, but shows no analysis — [Style3D (Weak)](https://www.style3d.com/blog/3d-or-2d-which-game-style-is-better-for-indie-developers/).
- **[Estimate: GameDiscoverCo]** A solo developer's 3D gladiator sim sold 10,000 units in its first 24 hours. The developer kept art costs down by reusing textures and models — [GameDiscoverCo](https://newsletter.gamediscover.co/p/analysis-how-a-solo-dev-gladiator).
- **[Estimate: Alinea 2025]** The top three 2025 indie grossers were 3D games from small teams: Schedule I ($151M), R.E.P.O. ($147M), PEAK ($87M) — [GameDev Reports](https://gamedevreports.substack.com/p/alinea-analytics-2025-year-in-review).
  - The 3D co-op "friendslop" wave, driven by PEAK and others, is covered by [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-two-friendslop-hits-got-the-audience) and [Wikipedia: Friendslop](https://en.wikipedia.org/wiki/Friendslop).
- **[Academic, 2025]** A machine-learning study using Gamalytic revenue data found the Early Access tag positively associated with revenue, and "indie" and F2P tags negatively. Art-style effects were not reported in the extract — [Int. J. Computer Games Technology (Wiley)](https://onlinelibrary.wiley.com/doi/10.1155/ijcg/5776632).
- **Outsourcing price lists for 3D characters** (vendor self-reports, 2025–2026; indicative only):

  | Source | What is priced | Price |
  |---|---|---|
  | RocketBrush | Stylized character | $2,000–$5,000 |
  | RocketBrush | Photoreal / studio-grade character | $4,000–$20,000+ |
  | RocketBrush | Basic low-poly character | $1,000–$2,500 |
  | RocketBrush | Animation, 2–3 s cycle | $200–$1,000 per cycle |
  | RocketBrush | Hourly rates | Studios $50–$200+/h; mid-level freelancers $30–$80/h |
  | Pixune | Model + texture + retopology + UV | Stylized $2,500–$4,000; realistic $4,000–$6,000 |
  | Pixune | Rig | $500–$2,000 |
  | Pixune | Animation | $200–$500 per cycle |
  | Whimsy Games | Rigged 3D character | Mobile $1,500–$4,000; PC/console $4,000–$12,000 |
  | Cubix | AAA hero character, full pipeline | $5,000–$25,000+ |
  | Cubix | Secondary cast of 5–10 characters | $15,000–$80,000+ |
  | FreelanceNation | Game-ready rigged character | $1,000–$5,000+, taking 3–6 weeks |
  | FreelanceNation | US freelance 3D artist | $45–$75/h |

  Sources: [RocketBrush (character prices)](https://rocketbrush.com/blog/3d-character-art-prices-guide); [RocketBrush (outsourcing prices)](https://rocketbrush.com/blog/game-art-outsourcing-prices-complete-pricing-breakdown); [Pixune](https://pixune.com/blog/game-art-outsourcing-price/); [Whimsy Games](https://whimsygames.co/?p=17441); [Cubix](https://www.cubix.co/blog/video-game-character-design-outsourcing-pick-the-right-partner/); [FreelanceNation](https://freelancenation.com/blog/cost-to-hire-a-3d-artist).
- Marketplace asking rates for riggers are much lower ($8–$30/h on Guru and Freelancer.com; Fiverr gigs from $10–$40), but quality varies widely — [Freelancer.com](https://www.freelancer.com/hire/3d-rigging); [Guru](https://www.guru.com/d/freelancers/skill/character-rigging/); [Fiverr](https://www.fiverr.com/categories/video-animation/rigging/3d-rigging).
- Cheap asset routes used by hits:
  - Vampire Survivors spent about £1,100 in total on 2D art and sound assets — [PC Gamer](https://www.pcgamer.com/vampire-survivors-didnt-rip-off-castlevania-sprites-after-all/).
  - Blue Prince was prototyped with Unity Asset Store assets — [Unity blog](https://unity.com/blog/blue-prince-why-dogubomb-watched-2000-hours-gameplay).

### Inferences
- **Illustrative outsourced budget** for a small stylized 3D character-animation game, using the vendor ranges above:

  | Item | Calculation | Cost |
  |---|---|---|
  | Main characters | 3 × $2.5k–$5k | $7.5k–$15k |
  | Rigs | 3 × $0.5k–$2k | $1.5k–$6k |
  | Animation cycles | 30 × $200–$500 | $6k–$15k |
  | **Total** | | **≈$15k–$36k** |

- Recouping that budget requires roughly a top-20% outcome. For comparison, the 2019 cohort's top-20% threshold was $34k lifetime gross, about $24k after Valve's cut.
- If the developer makes the art themselves instead, the cost becomes learning time. This compounds the solo-learner risk the user faces: learning 3D modeling, rigging, animation and music at once.
- Demand for 3D is not the problem: 3D small-team games topped 2025 indie revenue. Production cost and skill depth for *character animation* is the problem. Successful solo 3D games typically avoid animation-heavy, high-fidelity characters. That is an inference consistent with the profiles in Section 4 but not verified with art-style data.

### Gaps
- No Gamalytic, VGI or GameDiscoverCo dataset splitting outcomes by 3D vs 2D, or by solo × 3D, was found.
- No primary postmortem quantifying hours per 3D character or animation for a solo developer was found.
- Free animation libraries and asset-store pipelines (Mixamo, Synty and similar) were not researched because the search budget ran out.

## 6. Layoffs 2023–2026 and what they imply for specialized AAA roles vs. independent paths

### Takeaway
About 10,500 jobs were cut in 2023 and a record 14,600–15,600 in 2024. 2025 eased to about 9,100–9,200 (Satvat). 2026 is forecast at about 14,700 (as of Aug 2026), close to the record.
- Layoffs hit AAA companies hardest: two-thirds of AAA respondents report layoffs at their company, versus one-third at indie studios.
- They are concentrated in North America, while global headcount is roughly flat as jobs shift to cheaper regions.
- Specialized AAA roles proved insecure. Even so, Section 1's base rates show the independent path has a much worse *expected* income. The evidence supports "no path is safe," not "only specialists succeed."

### Cited Findings
- **[Tracker: Amir Satvat]** — [GamesBeat](https://gamesbeat.com/gaming-layoffs-slowed-from-15631-in-2024-to-9053-in-2025-amir-satvat/); [GameDev Reports (Satvat 2026)](https://gamedevreports.substack.com/p/amir-satvat-layoffs-in-the-gaming); [GamesBeat (2026 forecast)](https://gamesbeat.com/game-industry-layoffs-projected-to-hit-14259-in-2026-amir-satvat/):

  | Year | Layoffs |
  |---|---|
  | 2022 | 8,500 |
  | 2023 | 10,500 |
  | 2024 | 15,631 (record) |
  | 2025 | 9,053 (Dec 2025 estimate; later revised to 9,197) |
  | 2026 forecast | rose from 8,025 (Jan 6) to 14,259, then 14,666 (Aug 11, 2026) |

  - Confirmed 2026 layoffs as of Aug 11: 10,140.
  - North America accounts for 66% of layoff events and about 79% of affected people.
  - The same summary reports Microsoft's gaming division cutting 1,600 people.
  - At Gamescom 2026, about 15,000 layoffs were predicted for 2026 — [36Kr](https://eu.36kr.com/en/p/3953714458852485).
- **[Other trackers]**
  - Farhan Noor's Video Game Layoffs site estimated about 10,500 for 2023 — [Game World Observer](https://gameworldobserver.com/2024/06/03/over-10k-games-industry-layoffs-in-2024-so-far-vs-2023).
  - Udonis lists more than 10,500 for 2023 and more than 14,600 for 2024 — [Udonis](https://www.blog.udonis.co/mobile-marketing/mobile-games/game-industry-layoffs).
  - The Game Industry Layoffs tracker passed 13,000 for 2024 by Oct 2024 — [WN Hub](https://wnhub.io/news/hr/item-46078).
  - More than 5,000 were already laid off in early 2024 — [VGC](https://videogameschronicle.com/news/over-5000-games-industry-workers-have-already-lost-their-jobs-in-2024).
- **[Tracker/analysis: Satvat, 2026]** Global games employment rose about 0.6% from 2022 to 2026, from roughly 750k to 754k — [GamesBeat](https://gamesbeat.com/global-gamings-workforce-grew-0-6-in-4-years-but-north-americas-shrank-11-5-amir-satvat/):
  - About 48,000 roles were eliminated but about 52,500 hires were made.
  - North American employment fell 11.5%.
  - Other estimates of North America's decline are larger: 19.2% ([Inven Global](https://www.invenglobal.com/articles/21183/global-gaming-industry-stagnates-north-american-jobs-plummet-11)), or about 25,000 roles, roughly 15% ([Edge](https://knowledge.edge-online.com/p/the-great-industry-reset-amir-satvat-on-geographical-cycling-treating-workers-with-humanity-and-disc)).
  - Satvat calls this "geographical cycling" of jobs away from the US and Western Europe toward cheaper regions.
- **[Survey: GDC 2026, 2,300+ respondents]** — [GDC](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [GamesBeat](https://gamesbeat.com/state-of-game-industry-survey-sheds-light-on-layoffs-genai-views-unionization-and-tariffs-gdc-survey/); [BusinessWire](https://www.businesswire.com/news/home/20260129438528/en/2026-State-of-the-Game-Industry-Report-Reveals-Widening-Effect-of-Layoffs-Broader-Perspectives-on-Generative-AI-Unionization-Tariffs-and-More):
  - 28% were laid off in the past two years (33% in the US).
  - About two-thirds of AAA-studio respondents said their company had layoffs, versus about one-third at indie studios. Some secondary write-ups give different AAA figures.
  - Reasons cited: restructuring 43%, budget cuts 38%, market conditions 38%, project cancellations 32%, strategic shifts 31%.
- **[Survey: GDC 2025, more than 3,000 respondents]** 11% were laid off in the past year. By discipline, the most affected were narrative (19%), managerial (16%) and art (16%) — [Game Developer](https://www.gamedeveloper.com/business/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more); [80.lv](https://80.lv/articles/one-in-ten-developers-lost-their-jobs-in-2024-according-to-gdc-report/).
- Background reference on the layoff wave: [Wikipedia: 2022–2026 video game industry layoffs](https://en.wikipedia.org/wiki/2022%E2%80%932026_video_game_industry_layoffs).

### Inferences
- Over 2023–2026, depth in a single AAA specialty did not protect jobs:
  - More than a quarter of surveyed developers lost a job within two years.
  - AAA employers were about twice as likely as indie studios to have layoffs.
  - Specialist disciplines such as art and narrative were among the hardest hit in 2024.
  - This directly weakens the user's premise that "today only specialists succeed," at least in employment-security terms.
- But the independent path is not a safe alternative. Its base rates are worse: median gross around $1k, about 1–1.5% above $1M, and about 10% of developers ever above $100k lifetime gross.
- The defensible synthesis is that both paths carry high risk. What distinguishes successful soloists (Section 4) is deep skill in one area combined with enough breadth to ship, while keeping income during development.
- Global headcount being roughly flat while North America shrinks suggests specialized roles still exist but are migrating to lower-cost regions. Competition for specialist jobs is therefore global.

### Gaps
- No data was found on re-employment rates or time-to-rehire by discipline, which would show which specialties are more secure.
- Satvat's final 2026 numbers are not available; the latest found forecast is Aug 11, 2026.
- Tracker methodologies differ (announced cuts vs. modeled estimates). One search extract said an announcement-based tracker counted only about 5,300 layoffs in 2025 (and 8,500 for 2022, 10,500 for 2023, 14,600 for 2024). I could not tie that to a specific page, so it is not used above. If accurate, it shows how much the 2025 total depends on method.
- I could not open the GDC PDFs for exact question wording. Secondary claims of "35% primarily self-fund" and "86% of solo devs self-fund" (GDC 2026) remain unverified; the PDF is listed at [InvestGame](https://investgame.net/news/pdf/2026-01-29-dec052f4_d88e_48ce_9f83_a18ce2f2a6e5_541400_gdc26_pdf_soti_report/) but could not be fetched.
