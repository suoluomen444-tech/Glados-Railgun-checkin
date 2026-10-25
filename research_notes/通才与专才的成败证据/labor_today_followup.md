# Does today's labor market (2015–2026) reward specialization or hybrid/broad skill combinations? Follow-up verification notes (compiled Oct 2026)

How these notes were made, and what the labels mean:

- **Access:** Direct page fetches failed in this session. WebFetch could not resolve hosts (nber.org, scholar.harvard.edu), and curl through the proxy got 403 on nber.org, scholar.harvard.edu and sas.upenn.edu. Every item below was verified through search results that surfaced abstracts, press releases, author pages or secondary coverage.
- **(secondary):** Seen only in secondary coverage (press, blogs, summaries), not in the primary document. Nothing was filled in from memory; anything unverified is in the Gaps sections.
- **Evidence-type tags:**
  - **[Causal–RCT]:** randomized experiment.
  - **[Causal–quasi-exp]:** natural experiment, difference-in-differences, IV or regression discontinuity; causal only under its identifying assumptions.
  - **[Correlational]:** observational association, even with controls.
  - **[Descriptive]:** counts or shares.
  - **[Projection]:** employer or forecaster expectations.
  - **[Theory]:** a model.
- **Scope:** This file follows up the items left "unverified" in `labor_entrepreneurship.md` (its Q5). It does not repeat the core AI-productivity studies (Brynjolfsson et al., Dell'Acqua et al., Noy & Zhang) or the freelancer and "canaries" studies already verified in `genai_skill_gaps.md`. Those are only cross-referenced here. Steam revenue concentration is covered in `indie_game_market.md` and is cross-referenced, not re-verified.

---

## Q1. Deming & Noray (2020, *QJE*): how fast do specialized technical skills depreciate, and what happens to the STEM earnings premium as workers age?

### Takeaway
Graduates in applied STEM fields (computer science, engineering) start with a large earnings premium. It erodes fast: the NBER version says the return "falls by more than half within the first decade of work." By around age 40, social-science and history majors have caught up in Deming's public summary of the data.

The authors model this as a race between on-the-job learning and **skill obsolescence**. Faster-changing careers have flatter age-earnings profiles, and graduates sort out of fast-changing occupations as they age. The evidence is **observational plus a structural model**, not causal. It cuts against "deep technical specialization is a durable asset". It does not show the premium disappears: it shrinks to roughly 10% in one comparison.

### Cited Findings
- **Citation:** David J. Deming & Kadeem Noray, "Earnings Dynamics, Changing Job Skills, and STEM Careers," *Quarterly Journal of Economics* 135(4), 2020, DOI 10.1093/qje/qjaa021. An earlier version is NBER Working Paper 25065 (2018), under a different title. — [DOI](https://doi.org/10.1093/qje/qjaa021); [NBER WP PDF](https://www.nber.org/papers/w25065.pdf); [author-copy PDF hosted at UPenn](https://www.sas.upenn.edu/~vr0j/oldteaching/712tqm-22/DemingNoray_2020.pdf); [SUFE abstract page](https://academicnewsletter.sufe.edu.cn/info/344981)
- **[Correlational/descriptive] Size of the decline (NBER WP abstract):** The initially high return to applied STEM degrees falls by more than half within the first decade of work. The paper argues the perceived "STEM shortage" reflects technological change that adds new job tasks and makes old ones obsolete. — [NBER WP PDF](https://www.nber.org/papers/w25065.pdf)
- **[Theory + correlational] Mechanism (QJE abstract):** Returns to experience are modeled as a contest between on-the-job learning and skill obsolescence. Careers whose skill requirements change faster have **flatter age-earnings profiles**. — [SUFE abstract page](https://academicnewsletter.sufe.edu.cn/info/344981); [DOI](https://doi.org/10.1093/qje/qjaa021)
- **[Correlational] Premium and sorting (QJE abstract):** The premium for technology-intensive majors (computer science, engineering, business) declines rapidly. These graduates **sort out of faster-changing occupations** as they gain experience. — [SUFE abstract page](https://academicnewsletter.sufe.edu.cn/info/344981); [UPenn-hosted PDF](https://www.sas.upenn.edu/~vr0j/oldteaching/712tqm-22/DemingNoray_2020.pdf)
- **(secondary) Deming's NYT op-ed:** Deming, "In the Salary Race, Engineers Sprint but English Majors Endure," *New York Times*, 2019. The STEM advantage fades steadily after the first job, and by age 40 people who majored in fields such as social science or history have caught up. — [HKS listing](https://pw.hks.harvard.edu/post/in-the-salary-race-engineers-sprint-but-english-majors-endure-nytimes); [a2ru summary](https://a2ru.org/?p=468)
- **(secondary) Women:** The pay premium of applied-STEM majors over social-science/history majors fell from **nearly 50% at ages 23–25 to about 10% at ages 38–40**. The search summary attributes this figure to women; I could not confirm the gender split in the original. — [Greenspun blog quoting the NYT op-ed](https://philip.greenspun.com/blog/2019/11/12/stem-doing-what-you-dont-love-for-a-short-career-and-minimal-extra/)
- **(secondary) Men at age 40:**
  - Men who studied computer science or engineering roughly doubled their starting salaries by 40, averaging about **$124,458**.
  - All male graduates averaged about **$111,870**.
  - Social-science and history majors averaged about **$131,154**, partly because they move into high-paying management, business and law jobs.
  - [Greenspun blog quoting the NYT op-ed](https://philip.greenspun.com/blog/2019/11/12/stem-doing-what-you-dont-love-for-a-short-career-and-minimal-extra/)
- **(secondary) Deming's explanation:** Technical skills become obsolete, and newer graduates with up-to-date skills compete for the same jobs. — [a2ru](https://a2ru.org/?p=468)

### Inferences
- **What depreciates:** The scarce, rewarded asset in fast-moving technical fields looks less like a fixed stock of specialist knowledge and more like the ability to keep re-learning. Tool-level specialization has a short shelf life.
- **Where careers go:** STEM graduates "sort out" of fast-changing occupations, and the age-40 catch-up runs through management, business and law. So late-career earnings partly reward moves into broader, coordination-heavy roles. This is consistent with Deming (2017) in Q2.
- **Applied to the user (inference only; no study measured artistic-skill depreciation):**
  - Engine-, software- and AI-tool-specific know-how is the analogue of fast-changing STEM skills, and is likely to depreciate within the 3-year horizon.
  - Fundamentals change slowly: animation principles, anatomy and silhouette, composition, music theory, game-design judgment.
  - The evidence favours investing in fundamentals and treating tool skills as disposable.
- **Not a reversal:** The premium erodes but does not vanish. About 10% remains at 38–40 in the comparison above, and male CS/engineering graduates still out-earn the average male graduate at 40. The finding is "technical depth alone is a depreciating asset", not "specialists lose".

### Gaps
- The full text was blocked. I did not retrieve:
  - the paper's measured rate of skill change (for example, the share of new skills appearing in job requirements per decade);
  - the data sources used to measure skill change;
  - the regression magnitudes.
- Earlier notes said skill change was "measured from job-ad text"; that remains unverified.
- I could not confirm whether the op-ed's age-40 figures come from cross-sections, which would mix cohort and age effects.
- I found no comparable depreciation estimates for creative or craft skills such as 3D modeling, animation or composition.
- Popular "half-life of skills ≈ 5 years (2.5 for technical skills)" claims were not verified and should not be used.

---

## Q2. Deming (2017, *QJE*): what are the returns to combining cognitive and social skills, and how did they change?

### Takeaway
Between 1980 and 2012 in the US:
- Jobs requiring high social interaction grew by nearly **12 percentage points** as a share of the labor force.
- Math-intensive but less social jobs, including many STEM jobs, shrank by **3.3 pp**.
- Jobs needing **both** high math and high social skill saw particularly strong employment and wage growth (secondary: +7.2 pp and +26% wages).

The return to social skills was much larger in the 2000s (NLSY97) than in the mid-1980s and 1990s (NLSY79). Cognitive and social skills are complements, and that complementarity grew. All of this is **correlational**. It supports "skill combinations gained value", but the combination is cognitive plus interpersonal, not several technical crafts.

### Cited Findings
- **Citation:** David J. Deming, "The Growing Importance of Social Skills in the Labor Market," *QJE* (2017); NBER WP 21473 (2015). — [NBER WP page](https://www.nber.org/papers/w21473); [author QJE PDF (Harvard)](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/ddeming/files/deming_socialskills_qje.pdf); [NLS bibliography record](https://nlsinfo.org/bibliography/search/title=%22The+Growing+Importance+of+Social+Skills+in+the+Labor+Market%22/id=9579)
- **[Descriptive] Social-interaction jobs:** Their share of the US labor force rose by **nearly 12 pp** from 1980 to 2012. — [NBER Digest, Nov 2015](https://www.nber.org/digest/nov15/growing-importance-social-skills-labor-market); [Silicon Canals](https://siliconcanals.com/g-economists-tracked-us-jobs-from-1980-to-2012-and-found-the-ones-demanding-social-skills-grew-by-about-12-percentage-points-as-the-maths-heavy-less-social-ones-shrank-the-case-for-people-skills-at-wo/)
- **[Descriptive] Math-heavy, less social jobs:** These jobs, including many STEM occupations, **shrank by 3.3 pp** over the same period. — [NBER Digest](https://www.nber.org/digest/nov15/growing-importance-social-skills-labor-market)
- **[Descriptive] Combined skills:** Employment and wage growth was particularly strong for jobs requiring high levels of **both** math skill and social skill (abstract). — [NBER WP page](https://www.nber.org/papers/w21473)
- **(secondary) High-math/high-social jobs, 1980–2012:** **+7.2 pp** in employment share and a **26% wage increase**. — [Harvard Gazette, Oct 2017 (URL as surfaced by search; may be truncated)](https://news.harvard.edu/gazette/story/2017/10/social-skills-increasingl)
- **[Correlational] Rising return:** With comparable skill measures across the NLSY79 and NLSY97 cohorts, the labor-market return to social skills was **much greater in the 2000s than in the mid-1980s and 1990s**. — [NBER Digest](https://www.nber.org/digest/nov15/growing-importance-social-skills-labor-market); [NLS bibliography](https://nlsinfo.org/bibliography/search/title=%22The+Growing+Importance+of+Social+Skills+in+the+Labor+Market%22/id=9579)
- **[Correlational] Complementarity:**
  - The wage return to social skills stays positive after controlling for cognitive skill, non-cognitive skill and many other wage determinants.
  - Cognitive and social skills are **complements** in wage determination, and that complementarity **has grown over time**.
  - [NBER Digest](https://www.nber.org/digest/nov15/growing-importance-social-skills-labor-market)
- **[Theory] Mechanism:** Social skills are modeled as lowering coordination costs. Workers can then "trade tasks" by comparative advantage, which makes team production more efficient. — [NBER Digest](https://www.nber.org/digest/nov15/growing-importance-social-skills-labor-market)
- **Caveat (secondary commentary):** The paper documents where demand moved, not a promise about any single career, and its task measures are estimates rather than direct observation of daily work. — [Silicon Canals](https://siliconcanals.com/g-economists-tracked-us-jobs-from-1980-to-2012-and-found-the-ones-demanding-social-skills-grew-by-about-12-percentage-points-as-the-maths-heavy-less-social-ones-shrank-the-case-for-people-skills-at-wo/)

### Inferences
- **What kind of combination:** Deming's "combination" is a cognitive and interpersonal T-shape. It supports "combinations beat a single strong skill" in wage work. It does not directly test the user's kind of breadth (3D modeling + animation + music + AI-assisted code).
- **It is not anti-specialization:** In the model, social skill lets people specialize within teams and trade tasks at low cost. The lesson is that specialist depth captures more value when paired with coordination skills.
  - For a solo developer, the internal coordination benefit is moot.
  - It still matters externally: commissioning freelancers, working with a composer or voice actor, community-building and publisher relations. That is an inference.
- **Read together with Q1:** Over 1980–2019, US data show pure technical depth without complementary skills as the slower-growing and faster-depreciating position.

### Gaps
- The cohort-specific coefficients (size of the social-skill return in NLSY79 vs NLSY97) and the math × social interaction estimate were not retrieved.
- I did not verify whether the trends continued after 2012, or after generative AI.
- Weinberger (2014, *Review of Economics and Statistics*), "The Increasing Complementarity between Cognitive and Social Skills," the main predecessor, was not checked.

---

## Q3. Burning Glass Technologies (2019) "The Hybrid Job Economy" and Lightcast follow-ups (2022–2026): share, growth and pay premiums of hybrid jobs

### Takeaway
The Burning Glass report was seen only through secondary coverage. It reported:
- Hybrid jobs projected to grow **~21% over a decade, vs 10%** for all jobs.
- Large premiums for specific scarce combinations, e.g. **~40%** for marketing managers with data-analysis skills.
- Hybrid jobs much less exposed to automation: **12% vs ~42%** of all jobs.
- One secondary source puts hybrids at **~12% (about 1 in 8) of openings**.

I found **no Lightcast "hybrid jobs" sequel for 2022–2026**. The closest follow-ups:
- **Lightcast's 2025 AI-skills report:** postings requiring AI skills pay **~28% more**, and **51%** of them are outside IT/computer science.
- **Stephany & Teutloff (2024, *Research Policy*):** across 962 skills, a skill's value depends on its complementarity with skills of a *different type*, and AI skills carry a **~21%** average premium.

All of this is **correlational** (posting- or platform-based).

### Cited Findings
- **(secondary) Growth projection:** Burning Glass projected that hybrid jobs will grow **21% over the next decade, more than twice the 10%** rate for the job market overall. — [World Economic Forum Agenda, Mar 2019](https://www.weforum.org/stories/2019/03/are-you-ready-for-the-rise-of-hybrid-jobs/); [Fortune, 21 Mar 2019](https://www.fortune.com/2019/03/21/hybrid-jobs-purple-squirrels)
- **(secondary) Pay premium:** Employers pay extra for scarce hybrid combinations ("purple squirrels"). The best-cited example: **marketing managers with data-analysis expertise often earn ~40% more** than those without it. — [WEF Agenda 2019](https://www.weforum.org/stories/2019/03/are-you-ready-for-the-rise-of-hybrid-jobs/); [Fortune 2019](https://www.fortune.com/2019/03/21/hybrid-jobs-purple-squirrels)
- **(secondary) Automation exposure:** Burning Glass estimated that automation could eventually take over **only 12% of hybrid jobs, vs ~42% of jobs overall**. — [Fortune 2019](https://www.fortune.com/2019/03/21/hybrid-jobs-purple-squirrels); [WEF Agenda 2019](https://www.weforum.org/stories/2019/03/are-you-ready-for-the-rise-of-hybrid-jobs/)
- **(secondary, single source) Share of openings:** Hybrid jobs are about **12% of all job openings** (≈ one in eight). — [Josh Bersin blog, Jan 2019](https://joshbersin.com/2019/01/want-to-make-more-money-join-the-hybrid-jobs-revolution/)
- **[Descriptive/correlational] Lightcast, "Beyond the Buzz" (press release, 23 Jul 2025):**
  - Based on an analysis of **more than 1.3 billion job postings**.
  - Postings that include AI skills offer **~28% higher salaries** than those without.
  - As of 2024, **51% of postings requiring AI skills fall outside IT and computer-science occupations**.
  - [Lightcast press release](https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23)
- **[Correlational] Stephany & Teutloff, citation and data:** Fabian Stephany & Ole Teutloff, "What is the price of a skill? The value of complementarity," *Research Policy* 53(1), 2024, article 104898, DOI 10.1016/j.respol.2023.104898. Data: about **50,000 jobs posted 2014–2022** on a large US online freelance platform, covering **962 skills**. — [arXiv preprint](https://arxiv.org/pdf/2210.01535); [INET Oxford](https://www.inet.ox.ac.uk/publications/what-is-the-price-of-a-skill-the-value-of-complementarity); [EconPapers record](https://econpapers.repec.org/RePEc:eee:respol:v:53:y:2024:i:1:s0048733323001828)
- **[Correlational] Stephany & Teutloff, main result:**
  - A skill's value depends on its **complementarity**: how many other high-value skills it can be combined with.
  - Value is relative to the worker's background. For most skills, **value is highest when combined with skills of a different type**.
  - **AI skills raise wages by ~21% on average**, which the authors attribute to strong complementarities and rising demand.
  - [arXiv](https://arxiv.org/pdf/2210.01535); [INET Oxford](https://www.inet.ox.ac.uk/publications/what-is-the-price-of-a-skill-the-value-of-complementarity)
- **(secondary, press summary) Individual AI-skill premiums:** Machine Learning **+40%**, TensorFlow **+38%**, Deep Learning **+27%**, NLP **+19%**, Data Science **+17%**. — [University of Oxford news, 24 Oct 2023](https://www.ox.ac.uk/news/2023-10-24-artificial-intelligence-skills-can-increase-salaries-much-40)
- **Sample discrepancy:** The paper and most releases describe ~50,000 jobs. One Oxford release cites ~25,000 workers. Prefer the journal version. Platform data may not generalize to the wider labor market. — [Oxford news](https://www.ox.ac.uk/news/2023-10-24-artificial-intelligence-skills-can-increase-salaries-much-40); [arXiv](https://arxiv.org/pdf/2210.01535)

### Inferences
- **What kind of hybrid pays:** The documented premiums attach to **specific scarce pairings** in which one part is a high-value technical skill (data, SQL, AI) bolted onto a domain role. That is a "domain + technical tool" T-shape, not generic breadth. Burning Glass's framing ("purple squirrels") is about scarcity of the combination.
- **Stephany & Teutloff is the most rigorous support for "hybrid pays":** Skill value rises with complementary skills of a different type. But a hot specialist skill (AI/ML) also carries its own premium. So the pattern is **specialist depth × complementary breadth**, not breadth instead of depth.
- **AI skills are moving into domain jobs:** With 51% of AI-skill postings outside IT, much of the AI premium is earned by domain workers adding AI (hybrids), not only by AI specialists.
- **Relevance to the user is indirect:** These are wage and posting premiums for employees. A solo game developer's returns come from a product market with superstar dynamics (Q4). The hybrid evidence mainly says that being able to combine art, animation and technical implementation is a recognized scarce combination in labor markets. Technical-artist roles are a plausible analogue, but that was not verified here.

### Gaps
- The primary Burning Glass 2019 report was not accessed. Its definition of "hybrid," its methods, and whether premiums control for experience, location or employer are unknown.
- Secondary coverage also mentioned a **41%** premium for marketing managers who know SQL and **21%** for engineers with project-management skills. The outlet could not be identified, so treat these as unverified.
- I found no Lightcast or Burning Glass Institute "hybrid jobs" update for 2022–2026 within the search budget.
- Anderson (2017, *PNAS*), "Skill networks and measures of complex human capital" (Upwork; reportedly finds that diverse, complementary skills pay more), was not verified.
- No source tests whether hybrid premiums survive controls for worker ability (selection). All the evidence is posting- or platform-based.

---

## Q4. Superstar / winner-take-all economics: Rosen (1981) and recent concentration in creative markets (music, games, apps, creator economy). What does it imply about being top-tier in one thing vs good at many?

### Takeaway
Rosen's model predicts that **small talent differences become huge earnings differences** when two things hold: consumers do not substitute quantity for quality, and technology lets one seller serve the whole market. Recent data show extreme concentration:
- **Concerts:** the top 1% of artists took ~60% of concert revenue in 2017, up from 26% in 1982.
- **Streaming catalogue:** ~88% of 253 million streaming tracks got fewer than 1,000 streams in 2025.
- **Spotify payouts:** 80 artists each generated more than $10M on Spotify in 2025.
- **Apps:** the top 1% of US App Store publishers took ~94% of revenue (2016, dated).
- **Creators:** only a few percent of creators earn more than $100k (secondary).

Two important qualifications:
1. Spotify's own data show the paid **professional middle has grown** since 2015.
2. A **randomized experiment** shows that social influence makes hits partly unpredictable: quality is necessary but not sufficient.

Everything is descriptive except Salganik et al. (causal) and Rosen (theory).

### Cited Findings
**Theory**
- **Citation:** Sherwin Rosen, "The Economics of Superstars," *American Economic Review* 71(5): 845–858 (1981). The White House document's reference list also cites Krueger (2005), "The Economics of Real Superstars," *Journal of Labor Economics* 23(1): 1–30. — [White House document](https://obamawhitehouse.archives.gov/sites/default/files/docs/hope%5Fand%5Fdreams%5F-%5Ffinal.pdf)
- **[Theory] Core result:** Small talent advantages at the top translate into much larger revenue gaps. Better sellers earn more mainly by selling much larger quantities, not by charging much higher prices. — [Wikipedia: Superstar](https://en.wikipedia.org/wiki/Superstar)
- **[Theory] Two conditions:**
  1. Imperfect substitution among sellers: lesser talent is a poor substitute for greater talent, so demand for top quality rises more than proportionally.
  2. A technology with joint consumption, in which one or a few sellers can serve the whole market. Broadcasting enormously enlarged such markets.
  - [Wikipedia: Superstar](https://en.wikipedia.org/wiki/Superstar); [Minneapolis Fed, 2002](https://minneapolisfed.org/article/2002/perfectly-competitive-superstars)
- **[Theory critique]:** Rosen also assumes perfect knowledge of quality. Perri (2012, *Eastern Economic Journal*) argues the main result can fail without these features, and offers a competitive model that still produces superstar effects. — [Perri 2012 PDF](https://www.appstate.edu/~perritj/SS-EEJ.pdf)

**Concerts (live music)**
- **[Descriptive] Top 1% share of concert revenue:**
  - **26%** in 1982.
  - **56%** in 2003 (Connolly & Krueger).
  - **60%** in 2017 (Krueger, *Rockonomics*, 2019).
  - The **top 5% took ~85%** in 2017.
  - (secondary): [Peter Orszag column, Salt Lake Tribune, Jun 2019](https://sltrib.com/opinion/commentary/2019/06/20/peter-orszag-taylor-swift); [The Economist](https://econ.st/2Y38M30); [ArtsJournal, 2014](https://artsjournal.com/worth/2014/12/are-bands-on-tour-winner-take-all)
- **Critique:** A review of *Rockonomics* argues the 1982 starting point is not justified, noting that this percentile's revenues rose by more than 15% between 1982 and 1984. — [IEA review PDF](https://iea.org.uk/wp-content/uploads/2020/08/COVER-STORY_revised.pdf)

**Music streaming**
- **[Descriptive] Luminate 2025 Year-End Report:** About **253 million tracks** sit on audio streaming services. About **88% got fewer than 1,000 streams in 2025**. By stream count:

  | Streams in 2025 | Tracks |
  |---|---|
  | 10 or fewer | ~120.5 million (nearly half the catalogue) |
  | 11–100 | 62.6 million |
  | 101–1,000 | 40.7 million |

  [Music Business Worldwide](https://www.musicbusinessworldwide.com/quarter-of-a-billion-tracks-now-sit-on-music-streaming-services-where-does-it-end); [DJ Mag](https://djmag.com/news/music-streams-nearly-10-globally-51-trillion-2025-report-finds); [Hypebot](https://www.hypebot.com/luminate-reports-music-streaming-saturation-2025-2026/); [Nialler9](https://nialler9.com/88-of-songs-on-spotify-didnt-make-money-last-year-due-to-this-rule/)
- **Earlier Luminate data point (year not confirmed):** More than 200 million tracks, nearly 100 million of them with no more than 10 plays each. — [MBW headline](https://www.musicbusinessworldwide.com/there-are-now-more-than-200m-tracks-on-audio-streaming-services-nearly-100m-of-them-attracted-no-more-than-10-plays-each/)
- **Commentary:** Nialler9 links the sub-1,000-stream share to Spotify's rule excluding such tracks from royalty payouts. That is commentary, not a Luminate finding. — [Nialler9](https://nialler9.com/88-of-songs-on-spotify-didnt-make-money-last-year-due-to-this-rule/)
- **[Descriptive; interested party] Spotify Loud & Clear 2026 (11 Mar 2026, covering 2025 royalties "generated" for rights holders, not artists' take-home pay):**

  | Measure | 2025 | Comparison |
  |---|---|---|
  | Artists generating >$1M | >1,500 | — |
  | Artists generating >$100k | >13,800 | ~1,400 more than the prior year; ~7,800 in 2015 |
  | Top 80 artists | each >$10M | — |
  | 100,000th-ranked artist | >$7,300 | ~$350 in 2015 |
  | Total paid out | >$11B in 2025 | nearly $70B lifetime |

  [Spotify newsroom](https://newsroom.spotify.com/2026-03-11/loud-and-clear-music-economics-highlights/); [Billboard Canada](https://ca.billboard.com/business/streaming/spotify-says-over-13800-artists-generated-100000-on-the-platform-last-year-loud-clear-report); [Relix](https://relix.com/?p=157747)
- **(secondary):** More than 80% of artists generating $1M+ on Spotify have never had a Top-50 hit. — [Billboard Canada](https://ca.billboard.com/business/streaming/spotify-says-over-13800-artists-generated-100000-on-the-platform-last-year-loud-clear-report)

**Apps**
- **[Descriptive] Sensor Tower, Q1 2016:** The **top 1% of US App Store publishers** with paid or in-app-purchase apps generated **~94% of revenue** (~$1.34B of $1.43B) and captured ~70% of downloads. This is US iOS only and a decade old. — [Sensor Tower blog](https://sensortower.com/blog/app-store-one-percent); [MarTech](https://martech.org/report-ios-app-store-revenue)
- **Apple, June 2026:** The App Store ecosystem facilitated over $1.4 trillion in 2025 billings and sales (Analysis Group study). This is **not** a concentration measure, and no developer-level breakdown was found. — [Apple Newsroom (LatAm), Jun 2026](https://www.apple.com/la/newsroom/2026/06/app-store-ecosystem-reaches-1-point-4-trillion-usd-as-developers-thrive-globally/)

**Creator economy**
- **(secondary; self-selected survey; 2022 income data) Share above $100k:** About **4%** of creators earn more than $100,000 a year (Kajabi, *State of Creators '24*). The attribution in secondary coverage is somewhat muddled. — [Netinfluencer](https://www.netinfluencer.com/kajabi-state-of-creators-2024-report/); [Netinfluencer (alt.)](https://www.netinfluencer.com/kajabi-state-of-creators-24-report/)
- **(secondary) Income sources:**
  - Two-thirds of creators rely on a single revenue source.
  - The most successful creators diversify across five or more streams.
  - Creators earning more than $150k have about seven income sources.
  - This is **[Correlational]**: reverse causation is likely, since bigger audiences enable more streams.
  - [Netinfluencer](https://www.netinfluencer.com/kajabi-state-of-creators-2024-report/)
- **Conflicting source:** An Adobe-linked survey of influencers with more than 5,000 followers claims over half are in the top income bracket. Its restricted sample conflicts with the figures above, so it should not be read as a general estimate. — [Netinfluencer on the Adobe report](https://www.netinfluencer.com/creator-economy-report-by-adobe/)

**Games (cross-reference; verified by another researcher, not re-verified here)**
- Steam's median new-release revenue fell for 12 consecutive years: about $15,000 for the 2016 cohort vs $1,728 for 2026 releases.
- Titles earning over $100k roughly doubled (~3,000 → 5,863) while supply roughly doubled.
- See `indie_game_market.md` §1. — [Game World Observer, Sep 2026](https://gameworldobserver.com/2026/09/01/the-median-revenue-of-games-on-steam-has-been-declining-for-12-consecutive-years)

**Luck vs quality in winner-take-all markets**
- **[Causal–RCT] Salganik, Dodds & Watts (2006), *Science* (DOI 10.1126/science.1121066), design:** **14,341** participants could download previously unknown songs. Some saw no download counts. Others saw counts from one of **eight independent "worlds"** that evolved separately. — [Dodds (UVM) paper page](https://pdodds.w3.uvm.edu/research/papers/salganik2006a); [PDF](https://www.cs.toronto.edu/~bor/303s19/docs/salganik_dodds_watts.pdf)
- **Salganik et al., results:**
  - Social influence **increased both inequality and unpredictability** of success.
  - Quality only partly determined outcomes: the best songs rarely did poorly and the worst rarely did well, but any other result was possible.
  - [AcaWiki summary](https://acawiki.org/Experimental_Study_of_Inequality_and_Unpredictability_in_an_Artificial_Cultural_Market); [PDF](https://www.cs.toronto.edu/~bor/303s19/docs/salganik_dodds_watts.pdf)
- **Follow-ups:** Later MusicLab-style experiments largely confirm the result, and a generative model reproduces the experimental data. — [arXiv 1408.1542](https://arxiv.org/pdf/1408.1542); [arXiv 1505.02469](https://arxiv.org/pdf/1505.02469)

### Inferences
- **Imperfect substitution is the key:** Two decent games are not a substitute for one great one. The payoff goes to being **top-ranked on what buyers value**, and "good at many things" does not add up across dimensions in the buyer's eyes. This is the strongest real support for the intuition behind "only specialists succeed".
- **Top-tier output is not the same as a specialist person:** The market rewards a top-tier product, not a single-skill creator.
  - A solo generalist can make a top product if the combination itself is the differentiator, for example a coherent personal vision or style.
  - Teams of specialists often ship mediocre products.
  - The superstar literature measures product and performer outcomes, not creators' skill breadth.
- **Base rates are low for everyone:** Concentration is so extreme that most entrants earn little, specialist or generalist. Salganik et al. show that rank among good-quality entrants is partly luck plus cumulative advantage.
- **Strategic implications (inference):**
  - Quality is a precondition, not a guarantee.
  - Early social proof (wishlists, community) is amplified by the market.
  - Strategies that allow more than one attempt (smaller scope, earlier releases) reduce exposure to variance.
- **The middle has grown, per Spotify:** Its 2015→2025 data show more artists earning $100k+ and a much higher income at rank 100,000. Even with an ultra-concentrated top, a larger professional tier has formed. Caveats: this is interested-party data, total market growth drives much of it, and it is not inflation-adjusted.
- **Creators diversify revenue:** The creator data suggest top earners diversify revenue streams. That is a business-side breadth, separate from craft breadth, and causality is unclear.

### Gaps
- No 2023–2026 app-store revenue-concentration figure was found; Sensor Tower's 2016 figure is dated.
- Krueger's concert-share figures were seen only in secondary coverage.
- No study was found that tests, within music, app or game markets, whether creators who are top-tier in one craft out-earn creators competent in many. For related creative-team evidence (Taylor & Greve, Mannucci & Yong, de Vaan et al.), see `creative_innovation.md`.
- Adler (1985), "Stardom and Talent" (superstars arising without talent differences), and Goldman Sachs creator-economy estimates were not verified.

---

## Q5. Large employer surveys (WEF Future of Jobs 2025, plus LinkedIn 2025): which skills are rising and falling, and do they say anything about specialists vs generalists?

### Takeaway
WEF 2025 surveyed more than 1,000 employers. It expects "nearly 40%" (39%) of required skills to change by 2030. The fastest-rising skills are technological (AI and big data; networks and cybersecurity; technological literacy) **plus** human and adaptive skills (creative thinking; resilience, flexibility and agility; curiosity and lifelong learning). Manual dexterity, endurance and precision decline. LinkedIn (Jan 2025) projects that **70%** of the skills used in most jobs will change by 2030.

Neither source frames the question as specialists vs generalists. The growth in job titles is led by specialist tech roles (secondary), but the rising *skill* profile pairs technological literacy for everyone with adaptability. All of this is **[Projection]**: expectations, not measured outcomes and not causal.

### Cited Findings
- **[Projection] WEF Future of Jobs Report 2025 (press release, 8 Jan 2025):**
  - Jobs: **170 million new jobs** and **92 million displaced** by 2030, a **net gain of 78 million**. About **22%** of jobs will be disrupted.
  - Skills change: **nearly 40% of required skills** on the job are set to change.
  - Barrier: **63% of employers** cite skills gaps as the key barrier to transformation.
  - Skills: AI, big data and cybersecurity skills will grow fast, while human skills such as creative thinking, resilience, flexibility and agility stay critical.
  - [WEF press release](https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/)
- **[Projection] WEF skills ranking:**
  - **AI and big data** top the list of fastest-growing skills, followed by **networks and cybersecurity** and **technological literacy**.
  - **Creative thinking**, **resilience, flexibility and agility**, and **curiosity and lifelong learning** are also expected to rise.
  - [WEF Skills Outlook chapter](https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/3-skills-outlook/); [EU Digital Skills & Jobs Platform (secondary)](https://digital-skills-jobs.europa.eu/en/latest/news/great-skills-reset-wefs-future-jobs-report-2025-catch-22-future-work)
- **(secondary) Skill-change share:** The exact figure is **39%** of core skills changing by 2030, down from 44% predicted in the 2023 edition. The 44% comparison came from a LinkedIn post, a weak source. — [EU Digital Skills & Jobs Platform](https://digital-skills-jobs.europa.eu/en/latest/news/great-skills-reset-wefs-future-jobs-report-2025-catch-22-future-work)
- **(secondary) Declining skills:** **Manual dexterity, endurance and precision** show notable net declines, with **24%** of respondents foreseeing a decrease in their importance. — [QKS Group summary](https://qksgroup.com/blogs/world-economic-forum-s-the-future-of-jobs-report-2025-what-does-the-latest-report-reveal-about-workplace-of-the-future-in-general-938); [EU platform](https://digital-skills-jobs.europa.eu/en/latest/news/great-skills-reset-wefs-future-jobs-report-2025-catch-22-future-work)
- **(secondary) Other skill findings:**
  - **Analytical thinking** remains the top core skill. Shares vary across sources at roughly 69–70% of employers.
  - Resource management, quality control, and programming and technological literacy are the skills that most distinguish growing roles from declining ones.
  - [EU platform](https://digital-skills-jobs.europa.eu/en/latest/news/great-skills-reset-wefs-future-jobs-report-2025-catch-22-future-work); [QKS Group](https://qksgroup.com/blogs/world-economic-forum-s-the-future-of-jobs-report-2025-what-does-the-latest-report-reveal-about-workplace-of-the-future-in-general-938)
- **(secondary) Reskilling need:** Of every 100 workers, **59** will need training by 2030, and **11** of them are unlikely to receive it, putting more than 120 million workers at medium-term redundancy risk. — [WAM](https://www.wam.ae/en/article/15cz0cb-urgent-upskilling-needed-cater-million-new-jobs)
- **(secondary) Growing and shrinking roles:**
  - Fastest-growing in percentage terms: AI and data roles are among the fastest-growing. Renewable-energy engineers, environmental engineers and electric/autonomous-vehicle specialists are among the 15 fastest-growing.
  - Largest absolute growth: frontline jobs such as farmworkers and delivery drivers.
  - Shrinking: clerical roles such as cashiers, data-entry clerks and bank tellers.
  - [Longterm Wiki summary](https://www.longtermwiki.com/resources/76b2231bb5b520c3); [Alison blog](https://alison.com/blog/?p=6408); [Drishti IAS](https://www.drishtiias.com/daily-updates/daily-news-analysis/future-of-jobs-report-2025/print_manually); [digit.fyi](https://www.digit.fyi/?p=110392)
- **[Projection] LinkedIn Work Change Report (Jan 2025):**
  - By 2030, **70% of the skills used in most jobs will change**, with AI as a catalyst.
  - Since 2022, the rate at which members add new skills to profiles is up **140%**.
  - Workforce entrants today are on pace to hold **twice as many jobs** over their careers as entrants 15 years ago.
  - [LinkedIn News](https://news.linkedin.com/2025/work-change-report-2025); [Report PDF](https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/Work-Change-Report.pdf)
- **(secondary) LinkedIn method:** The "skills used in most jobs" combine skills listed in job descriptions and member profiles, plus historical skill shifts and projections of AI-replicable skills. — [CNBC via NBC New York](https://www.nbcnewyork.com/news/business/money-report/within-5-years-70-of-skills-used-in-most-jobs-will-change-linkedin-report-says-how-you-can-keep-up/6262118/?amp=1)
- **Earlier LinkedIn projection (2023):** Job responsibilities will change by nearly **65%** by 2030 because of AI. This measures responsibilities, not skills, so it is not comparable to the 70% figure. — [insideHPC, Aug 2023](https://insidehpc.com/2023/08/linkedin-releases-state-of-ai-work-report/)

### Inferences
- **A portfolio, not a single deep skill:** Employers' expectations point to tech literacy rising for *everyone*, not just specialists, alongside adaptive and creative skills. That fits a "T-shape plus continuous learning" profile better than either a pure specialist or a pure generalist.
- **Some support for the specialist claim:** The fastest-growing job *titles* in percentage terms are specialist tech roles (AI/data, specialized engineers). Depth in a high-demand technical niche remains well rewarded.
- **Fits Q1:** Expected churn of 39–70% of skills by 2030 is consistent with Deming & Noray's obsolescence mechanism. The durable asset is learning speed. These forecasts are softer evidence than Deming & Noray's realized earnings data.
- **Forecasts get revised:** These are expectations. WEF's own headline figure moved from 44% (2023) to 39% (2025).

### Gaps
- The full WEF report was not opened. The fastest-growing-jobs list (for example, whether "big data specialists", "FinTech engineers" and "AI/ML specialists" are named) was **not verified** from the primary source.
- In the material I could see, WEF does not address specialists vs generalists directly.
- PwC's 2025 claim that skills are changing "66% faster" in AI-exposed occupations, sometimes quoted alongside WEF, was not verified in this session.

---

## Q6. 2023–2026 evidence: does generative AI shift returns toward specialists or toward generalists? (task bundling, "expertise compression", value of breadth)

### Takeaway
**No study found directly measures generalist vs specialist returns under generative AI.** The strongest evidence reframes the question as *which tasks within a job AI removes*:
- **Autor & Thompson (2025):** When automation removes a job's **inexpert** tasks, the remaining experts earn more but fewer are employed. When it removes **expert** tasks, wages fall and more people can do the job.
- **Teutloff et al. (2025, quasi-experimental):** On a freelance platform after ChatGPT, demand fell **20–50%** for substitutable skills (writing, translation) and for novices. Demand rose for specialized AI-complementary skills (ML programming **+24%**; chatbot development nearly **tripled**).
- **PwC 2026 job-ad data:** "Professionalised" roles, where AI supports experts, show twice the job growth and 42% faster pay growth than "democratised" roles. The AI-skill wage premium is 56–62%.
- **Hampole et al. (IV design):** Jobs whose AI exposure is **concentrated in a few tasks** are buffered, because workers reallocate effort. That is a bundling or breadth-as-insurance effect.
- **Copilot study (natural experiment):** Developers shifted time from project management to coding.

Net: AI devalues commodity execution, whether sold by specialists or novices. It raises the value of expertise that AI *complements* and of the ability to integrate. Neither "only specialists win" nor "generalists win" fits.

### Cited Findings
**Autor & Thompson (2025): the expertise framework**
- **Citation:** David Autor & Neil Thompson, "Expertise," *Journal of the European Economic Association* 23(4): 1203–1271 (2025). — [EconPapers record](https://econpapers.repec.org/RePEc:oup:jeurec:v:23:y:2025:i:4:p:1203-1271.); [MIT Blueprint Labs](https://blueprintlabs.mit.edu/research/expertise); [Autor, MIT page](https://economics.mit.edu/people/faculty/david-h-autor/ai-and-future-work)
- **[Correlational; occupation-level panel over four decades, model-guided, not an experiment]:**
  - The authors build a content-agnostic measure of task expertise.
  - Automation **raised wages and decreased employment** in occupations where it eliminated **inexpert** tasks.
  - It **reduced wages and increased employment** where it eliminated **expert** tasks.
  - This explains why routine-task automation reduced employment but often raised wages.
  - [EconPapers](https://econpapers.repec.org/RePEc:oup:jeurec:v:23:y:2025:i:4:p:1203-1271.); [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/a-new-look-how-automation-changes-value-labor)
- **(secondary) Examples:**
  - **Inventory clerks:** employment more than doubled while real wages fell **13%**, as computerization took their most expert tasks.
  - **Taxi drivers:** GPS automated local route knowledge, leading to lower wages but many more drivers.
  - [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/a-new-look-how-automation-changes-value-labor); [Wladawsky-Berger blog, Jul 2025](https://blog.irvingwb.com/blog/2025/07/does-automation-replace-or-augment-expertise.html)

**Teutloff et al. (2025): freelancer demand after ChatGPT**
- **Citation:** Teutloff, Einsiedler, Kässi, Braesemann, Mishkin & del Rio-Chanona, "Winners and Losers of Generative AI: Early Evidence of Shifts in Freelancer Demand," *Journal of Economic Behavior & Organization* (2025). — [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:af491969-bee7-4b09-a696-2b500b6b21d8); [OII](https://sosi.oii.ox.ac.uk/publications/winners-and-losers-of-generative-ai-early-evidence-of-shifts-in-freelancer-demand/); [CSH Vienna](https://csh.ac.at/publication/winners-and-losers-of-generative-ai-early-evidence-of-shifts-in-freelancer-demand/)
- **[Causal–quasi-exp: postings compared with counterfactual trends; abstract-level]:**
  - Postings on a leading freelancing platform were split into **116 skill clusters**, each classed as substitutable by, complementary to, or unaffected by LLMs.
  - **Substitutable skills** such as writing and translation fell **20–50%** relative to the counterfactual. The sharpest drop was in short-term jobs of 1–3 weeks.
  - **Complementary skills** were mixed: ML programming **+24%**, AI-powered chatbot development **nearly tripled**.
  - **Demand for novice workers declined** overall.
  - The authors read this as a shift toward **more specialized expertise**.
  - [ORA](https://ora.ox.ac.uk/objects/uuid:af491969-bee7-4b09-a696-2b500b6b21d8); [CSH](https://csh.ac.at/publication/winners-and-losers-of-generative-ai-early-evidence-of-shifts-in-freelancer-demand/)

**PwC 2026 Global AI Jobs Barometer (released 15 Jun 2026; one PwC country page dates it 13 Jul 2026)**
- **[Descriptive/correlational; press-release level; based on "over one billion job ads across 27 countries" as reported]:**

  | Measure | Reported figure |
  |---|---|
  | AI-skill wage premium | **62%**, "up from 57%" in the prior edition. The 2025 edition was widely reported at **56%**, so the prior figure may have been revised. |
  | Premium by sector | 16% (government) to 118% (some consumer sectors) |
  | Growth in roles requiring specific AI skills | **69%**, vs **9%** for all jobs (period not stated in coverage) |
  | "Professionalised" roles (AI supports experts) vs "democratised" roles (AI makes work easier for non-experts) | professionalised: **twice the job growth** and **42% faster salary gains** |
  | Most vs least AI-exposed companies, 2018→2025 | headcount +52% vs +36%; wages +24% vs +17% |
  | US entry-level analysis | AI-exposed roles are **7× more likely to require senior-level skills**; their openings grew 35% since 2019 while other entry-level roles shrank 10% (wording ambiguous in coverage) |

  [PwC global press release](https://pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html); [AAP release copy](https://www.aap.com.au/aapreleases/cision20260615ae78182/); [PwC Indonesia](https://www.pwc.com/id/en/media-centre/press-release/2026/english/ai-jobs-barometer-en.html); [Enterprise DNA (secondary)](https://enterprisedna.co/resources/news/pwc-2026-ai-jobs-barometer-human-skills-premium-2026); [2025 edition's 56% (secondary)](https://letsdatascience.com/news/ai-skilled-workers-command-56-wage-premium-95ad08bf)

**Burning Glass Institute + HBS, "The Expertise Upheaval" (July 2025): the closest thing to "expertise compression"**
- **Report:** Authors Matt Sigelman, Joseph Fuller, Michael Fenlon, Erik Leiden and Gwynn Guilford. — [BGI report page](https://www.burningglassinstitute.org/research/the-expertise-upheaval); [HKS CID listing](https://www.hks.harvard.edu/centers/cid/publications/expertise-upheaval-how-generative-ais-impact-learning-curves-will-reshape)
- **[Projection/scenario analysis; not causal] Thesis:**
  - Generative AI's biggest impact is on the *level of expertise* jobs require, not on job counts.
  - AI is compressing time-to-mastery and stripping away entry-level rungs.
  - [BGI](https://www.burningglassinstitute.org/research/the-expertise-upheaval); [BGI on its HBR article](https://www.burningglassinstitute.org/news/hbr-how-genai-could-change-the-value-of-expertise)
- **(secondary) Two kinds of roles:**
  - **"Mastery" roles:** entry pathways narrow, leaving work that needs experience and oversight. Washington Monthly calls this an "experience trap" for young workers.
  - **"Growth" roles:** AI lowers barriers to entry, opening the role to more people.
  - [Washington Monthly, Aug 2025](https://washingtonmonthly.com/2025/08/27/ai-boon-for-jobs/); [HBS Working Knowledge interview with Fuller](https://www.library.hbs.edu/working-knowledge/talent-shift-ai-could-spark-interview-with-joseph-fuller); [MindWorks podcast](https://mindworks.buzzsprout.com/1309438/episodes/18080392-ai-s-expertise-upheaval-mastery-vs-growth-roles)
- **(secondary) Scale:** A BGI chief economist's post says "the better part of 50 million" US jobs will be affected one way or the other. — [BGI report page (as surfaced in search)](https://www.burningglassinstitute.org/research/the-expertise-upheaval)
- **Critique:** The fall-off in new-graduate hiring predates widespread generative-AI adoption. — [Phil Hill, On EdTech](https://onedtech.philhillaa.com/p/many-explanations-are-making-premature-analysis-on-recent-grad-unemployment)

**Hampole et al. (2025): task bundling within jobs**
- **Citation:** Menaka Hampole, Dimitris Papanikolaou, Lawrence D.W. Schmidt & Bryan Seegmiller, "Artificial Intelligence and the Labor Market," NBER WP 33509 (Feb 2025, revised Sep 2025; not peer-reviewed). — [NBER](https://www.nber.org/papers/w33509); [Kellogg](https://www.kellogg.northwestern.edu/faculty/research/detail/2025/artificial-intelligence-and-the-labor-market/)
- **[Causal–quasi-exp: IV based on historical university hiring networks]:**
  - Task-level AI exposure is measured with NLP for 2010–2023.
  - Highly exposed tasks see reduced labor demand.
  - An occupation's **mean** task exposure **depresses** demand.
  - **Concentration** of exposure in a few tasks **offsets** losses, because workers reallocate effort to other tasks.
  - Aggregate employment effects are modest: lost demand in exposed occupations is offset by productivity-driven demand at AI-adopting firms.
  - [NBER](https://www.nber.org/papers/w33509)

**Copilot natural experiment: what AI does to the content of work**
- **Citation:** "Generative AI and the Nature of Work." HBS working paper with Microsoft and GitHub co-authors (including Frank Nagle; commonly cited as Hoffmann et al.; full author list not re-verified here); also CESifo WP 11479; MIT IDE version 2, Aug 2025. — [CESifo WP](https://www.ifo.de/DocDL/cesifo1_wp11479.pdf); [MIT IDE v2](https://ide.mit.edu/wp-content/uploads/2025/08/GenAI-and-the-nature-of-work-Version-2.pdf)
- **[Causal–quasi-exp: access assigned by an internal ranking threshold]:**
  - About **187,000 developers** were observed weekly from July 2022.
  - Copilot access shifted time **from project management toward core coding**.
  - The proposed mechanisms are autonomy and exploration.
  - Effects were larger for lower-ability developers.
  - [CESifo WP](https://www.ifo.de/DocDL/cesifo1_wp11479.pdf); [Wharton summary](https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2025/04/WTIC.2025_Nagle-Frank_Generative-AI.pdf); [MIT IDE v2](https://ide.mit.edu/wp-content/uploads/2025/08/GenAI-and-the-nature-of-work-Version-2.pdf)
- **(secondary) Size of the shift:** Coding time **+12.4%**, project management **−24.9%**. — [MIT Sloan](https://mitsloan.mit.edu/node/51270)
- **Caveat:** The New Stack cites a Google DORA report linking AI-assisted code to more bugs and rework. — [The New Stack](https://thenewstack.io/copilot-reshapes-developer-work/)

**AI skills spreading into domain jobs (hybrid evidence)**
- **[Descriptive]:** 51% of AI-skill postings are outside IT/CS, and AI-skill postings pay ~28% more. — [Lightcast, Jul 2025](https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23)

**Cross-references (verified in `genai_skill_gaps.md`; not repeated)**
- **Hui, Reshef & Zhou (2024, *Organization Science*):** After ChatGPT and image generators, writing freelancers saw −2% jobs and −5.2% earnings, and image freelancers −3.7% jobs and −9.4% earnings. **Top-rated freelancers** were disproportionately affected. — [Organization Science](https://pubsonline.informs.org/doi/abs/10.1287/orsc.2023.18441?journalCode=orsc)
- **Demirci et al. (*Management Science*):** Image-creation postings fell. — [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420)
- **Stanford "canaries":** Relative employment of early-career workers in AI-exposed occupations fell from −13% (Aug 2025) to −19% (Aug 2026). — [Stanford DEL, Aug 2026 PDF](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- **Humlum & Vestergaard (NBER WP 33777):** Precise nulls on earnings and hours in Denmark. See `genai_skill_gaps.md` §3.
- **Dell'Acqua et al., "Cybernetic Teammate":** Individuals with AI matched teams without it and produced less function-siloed solutions. See `science_range.md` and `genai_skill_gaps.md`.

### Inferences
- **"Specialist" is the wrong unit; "which tasks AI takes" is the right one.**
  - Specialists in AI-substitutable crafts lost demand, top-rated ones included: writers, translators, image-makers (Teutloff; Hui et al.).
  - Specialists in AI-complementary skills gained (ML, chatbot development).
  - Novices lost across the board.
  - So the claim gets **partial support** from 2023–2026 freelance data, but only for specialists whose expertise AI complements.
- **Applying Autor & Thompson and PwC to the user (inference):**
  - AI coding "democratises" programming for the user. AI removes the expert part of coding *for them*, a big personal capability gain. By the same logic, generic coding ability is not where differentiation or scarcity value will come from.
  - Conversely, if AI absorbs the *inexpert* parts of 3D work (boilerplate rigging, cleanup, retopology-like chores; not verified as of 2026), human expertise in animation feel, art direction and game-design judgment becomes relatively scarcer and more valuable.
- **Bundling as insurance (Hampole et al.):** Jobs made of varied tasks, where AI hits only some, let people reallocate rather than be displaced. That is a concrete mechanism by which breadth protects against AI. It concerns tasks within an occupation, not individuals' skill portfolios, so the analogy to a solo developer is loose.
- **AI cuts coordination overhead (Copilot study):** AI moves effort from coordination and project management to core production. That strengthens the case that a solo or tiny team can cover more ground than before. Quality-control limits remain; see `genai_skill_gaps.md` on METR and debugging.
- **An unresolved tension:** Autor & Thompson predict that "democratised" work gains **employment**. PwC finds democratised roles have **slower** job growth than professionalised ones. Possible reasons: different eras (pre-AI automation vs generative AI), postings vs employment, and different definitions.

### Gaps
- No paper titled or framed as "**expertise compression**" was found. The closest are BGI's "compressing time-to-mastery" (*The Expertise Upheaval*) and Autor & Thompson's expertise framework.
- No direct study was found comparing **generalist vs specialist** workers (for example, multi-category vs single-category freelancers) before and after generative AI. `genai_skill_gaps.md` flags the same gap.
- PwC details are press-release level only. Unverified: how "professionalised/democratised" is defined, the time window behind 69% vs 9%, and the 56%/57% prior-edition discrepancy.
- BGI's report-level quantitative findings (named occupations, magnitudes) were not retrieved. One weakly sourced summary claims ~18 million US entry-level jobs (~12% of the workforce) could become obsolete; it is unverified and should not be used.
- The size of the Copilot paper's "exploration" effect (for example, adoption of new programming languages) was not retrieved.
- Theoretical work not checked: Agrawal, Gans & Goldfarb, "The Turing Transformation" (AI and skill premiums); Ide & Talamas, "Artificial Intelligence in the Knowledge Economy" (autonomous AI vs copilots and who benefits).

---

## Q7. Bottom line: does 2015–2026 evidence support "nowadays only specialists can succeed"?

### Takeaway
**Not in that form.**
- **Wage labor markets** (mostly correlational evidence): the opposite trend. Specialist technical premiums erode fast (Deming & Noray), while combinations of skills (cognitive + social; domain + data/AI) gained value (Deming 2017; Burning Glass; Stephany & Teutloff; Lightcast).
- **Superstar product markets:** the strongest support for the claim. Returns are extremely concentrated, so being *top-tier on what buyers value* matters enormously.
- **Early AI evidence:** also supports the claim in part. Demand is shifting toward deep expertise that AI complements and away from novices.

However, a "top-tier product" is not a "single-skill person". Specialists in AI-substitutable crafts are among the clearest losers. Luck amplifies outcomes in winner-take-all markets.

The best-supported reading is a **T-shape**: real depth in something AI complements and buyers value, plus enough breadth to integrate, keep re-learning, and ship.

### Cited Findings
**Evidence that supports the specialist side, at least partly**
- Concert revenue for the top 1% of artists rose from 26% (1982) to 60% (2017) (secondary). — [Orszag](https://sltrib.com/opinion/commentary/2019/06/20/peter-orszag-taylor-swift); [The Economist](https://econ.st/2Y38M30)
- ~88% of 253M tracks got fewer than 1,000 streams in 2025. — [MBW](https://www.musicbusinessworldwide.com/quarter-of-a-billion-tracks-now-sit-on-music-streaming-services-where-does-it-end)
- The top 1% of US App Store publishers took ~94% of revenue (2016). — [Sensor Tower](https://sensortower.com/blog/app-store-one-percent)
- After ChatGPT, freelance demand shifted toward specialized, AI-complementary expertise, and novice demand fell (quasi-experimental). — [Teutloff et al. (ORA)](https://ora.ox.ac.uk/objects/uuid:af491969-bee7-4b09-a696-2b500b6b21d8)
- "Professionalised" roles, where AI supports experts, grow twice as fast with 42% faster pay growth (correlational). — [PwC 2026](https://pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html)
- When automation removes inexpert tasks, the remaining experts' wages rise. — [Autor & Thompson 2025](https://econpapers.repec.org/RePEc:oup:jeurec:v:23:y:2025:i:4:p:1203-1271.)
- BGI's "mastery roles" that need experience. — [BGI](https://www.burningglassinstitute.org/research/the-expertise-upheaval)
- Specialist tech roles are among the fastest-growing job titles in WEF 2025 (secondary). — [Longterm Wiki](https://www.longtermwiki.com/resources/76b2231bb5b520c3)

**Evidence against the claim, or for combinations**
- The applied-STEM premium halves within a decade, and humanities and social-science majors catch up by about 40. — [NBER WP 25065](https://www.nber.org/papers/w25065.pdf); [a2ru](https://a2ru.org/?p=468)
- High-math + high-social jobs grew most; the complementarity between the skills grew. — [NBER Digest](https://www.nber.org/digest/nov15/growing-importance-social-skills-labor-market)
- Hybrid jobs: projected 21% growth vs 10%; ~40% premiums for specific combinations; 12% vs 42% automation exposure (secondary). — [WEF Agenda 2019](https://www.weforum.org/stories/2019/03/are-you-ready-for-the-rise-of-hybrid-jobs/); [Fortune 2019](https://www.fortune.com/2019/03/21/hybrid-jobs-purple-squirrels)
- Skill value rises with complementary skills of a different type. — [Stephany & Teutloff 2024](https://arxiv.org/pdf/2210.01535)
- 51% of AI-skill postings are outside IT, and they carry a ~28% premium. — [Lightcast 2025](https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23)
- Top-rated specialist freelancers were hit hardest in image work. — [Hui et al. 2024](https://pubsonline.informs.org/doi/abs/10.1287/orsc.2023.18441?journalCode=orsc)
- Concentrated task exposure lets workers reallocate (breadth buffers AI). — [Hampole et al.](https://www.nber.org/papers/w33509)
- Expected skill churn by 2030 is 39–70%. — [WEF](https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/); [LinkedIn](https://news.linkedin.com/2025/work-change-report-2025)
- In the MusicLab experiment, hits were partly unpredictable even given quality (causal). — [Salganik et al. 2006](https://pdodds.w3.uvm.edu/research/papers/salganik2006a)

**Evidence-quality summary (design → what it can support)**

| Evidence | Design | Causal? | Direction for the "only specialists" claim |
|---|---|---|---|
| Deming & Noray 2020 (*QJE*) | Observational earnings data + structural model | No (correlational, model-based) | Against (technical-specialist premium erodes) |
| Deming 2017 (*QJE*) | Occupational shares + NLSY panels with controls | No | Against (skill combinations rose) |
| Burning Glass 2019 | Job-posting analysis + projections (secondary) | No | Against (hybrid premiums, lower automation risk) |
| Stephany & Teutloff 2024 (*Res. Policy*) | Freelance-platform wage regressions | No | Mostly against (complementarity), but specialist AI skills also pay |
| Lightcast 2025 | Posting analysis (press release) | No | Mixed (AI premium; mostly earned in domain roles) |
| Rosen 1981 | Theory | n/a | For (top-tier output captures the market) |
| Krueger / Luminate / Spotify / Sensor Tower / Kajabi | Descriptive industry data | No | For (extreme concentration), with a growing paid middle on Spotify |
| Salganik et al. 2006 (*Science*) | Randomized experiment | **Yes** | Qualifies (luck and social influence, not just quality) |
| WEF 2025 / LinkedIn 2025 | Employer survey / platform projections | No (expectations) | Mixed (tech skills plus adaptability; churn) |
| Autor & Thompson 2025 (*JEEA*) | Four-decade occupational panel, model-guided | No (observational) | Depends on which tasks are automated |
| Teutloff et al. 2025 (*JEBO*) | Comparison with counterfactual trends after ChatGPT | **Quasi-causal** | Partly for (AI-complementary specialists; novices lose) |
| PwC 2026 | Job-ad analysis (press release) | No | Partly for (professionalised roles) |
| BGI Expertise Upheaval 2025 | Scenario/projection | No | Mixed (mastery vs growth roles) |
| Hampole et al. 2025 (NBER) | IV (university hiring networks) | **Quasi-causal** | Against (task breadth buffers) |
| Copilot natural experiment | Threshold-based access | **Quasi-causal** | Neutral to against (less coordination load; more solo production) |
| Hui et al. 2024 (*Org. Sci.*; cross-ref) | Difference-in-differences | **Quasi-causal** | Against (top specialists in substitutable crafts hit) |

### Inferences
- **Labor markets and creative product markets reward different things.**
  - In employment, the 2015–2026 data favour people who pair a valuable skill with complements and keep re-learning.
  - In winner-take-most creative markets, what matters is whether the *product* is top-tier on dimensions buyers value. The creator's breadth matters only through its effect on that.
  - The user is entering the second kind of market. The specialist intuition is therefore most relevant to the **product**: it needs at least one dimension that is clearly top-tier. It is least relevant to the **person**, who must be broad enough to ship alone.
- **For a solo 3D character-animation game with AI-written code (inference, not tested by any study found):**
  1. Code is the domain AI "democratises." It is a capability gain, not a differentiator.
  2. The marketable "specialist" asset should be the one dimension buyers notice first and that AI complements rather than substitutes. Plausibly that is **character animation and visual style**, given the concept.
  3. Other domains, including modeling breadth and music, can be "good enough". AI or assets can raise their floor, but substitutable crafts are where AI competition is fiercest (Hui et al.; Teutloff).
  4. Plan for variance and luck (Salganik; Steam base rates in `indie_game_market.md`): keep scope small, build an audience early, and allow for more than one attempt.
  5. Expect tool skills to depreciate within the 3-year window (Deming & Noray; WEF/LinkedIn churn). Invest in slow-changing fundamentals.

### Gaps
- No study found directly tests specialist vs generalist **solo or indie creators'** commercial outcomes in 2015–2026. The closest evidence is in `creative_innovation.md` and `labor_entrepreneurship.md`.
- Specialization-pays evidence from wage employment was not verified within the search budget: Kambourov & Manovskii (2009, *IER*) on occupation-specific human capital, and Gathmann & Schönberg (2010, *JOLE*) on task-specific human capital. Both predate 2015 in any case.
- Most labor-market numbers here are correlational, and several are visible only via secondary coverage or press releases. The report should present them as associations and expectations, not effects.
