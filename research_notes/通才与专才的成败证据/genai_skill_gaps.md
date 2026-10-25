# Generative AI and the novice/generalist vs expert/specialist gap, including game content creation (notes as of Oct 2026)

*Method note: WebFetch and curl were blocked for nearly every academic domain this session (nber.org, hbs.edu, metr.org, arxiv.org, pmc, informs, stanford). Verification therefore used search-engine extraction from primary pages (QJE article page, HBS WP 24-013 PDF, METR posts, journal DOI pages, Stanford Digital Economy Lab PDFs), cross-checked against reputable secondary coverage. Numbers I could confirm only from secondary sources, or not at all, are flagged.*

## 1. Core studies: does generative AI raise the performance floor? (Brynjolfsson/Li/Raymond; Dell'Acqua et al.; Noy & Zhang)

### Takeaway
All three flagship studies find that, on tasks AI handles well, AI narrows the gap: the least skilled or least experienced gain the most. Examples are +34–36% for the lowest-skill customer-support agents versus roughly zero for the top group, +43% vs +17% for below- vs above-average BCG consultants, and lower inequality among ChatGPT-assisted writers. The same studies also mark the limits. Top performers saw small quality declines, consultants were 19 percentage points less likely to be correct on a task outside the AI's frontier, and Noy & Zhang conclude that ChatGPT mostly substitutes for effort rather than building skill.

### Cited Findings

#### Brynjolfsson, Li & Raymond, "Generative AI at Work"
- **Citation and versions:** NBER Working Paper 31161 (April 2023). arXiv 2304.11771 (v2 revised November 2024). Published in the *Quarterly Journal of Economics* 140(2): 889–942 (2025), DOI 10.1093/qje/qjae044. — [QJE](https://academic.oup.com/qje/article/140/2/889/7990658); [DOI](https://doi.org/10.1093/qje/qjae044); [arXiv](https://arxiv.org/abs/2304.11771)
- **Design:** Staggered (quasi-random) rollout of a generative-AI conversational assistant to customer-support agents at one firm. BLS's Monthly Labor Review describes the firm as a Fortune 500 software company; some secondary sources describe it inconsistently. — [QJE](https://academic.oup.com/qje/article/140/2/889/7990658); [BLS MLR](https://www.bls.gov/opub/mlr/2024/beyond-bls/ai-improved-the-productivity-of-a-fortune-500-software-company.htm)
- **Sample:** 5,172 agents in the QJE/arXiv v2 version; 5,179 agents in the 2023 NBER version. — [QJE](https://academic.oup.com/qje/article/140/2/889/7990658); [NBER WP PDF](https://www.nber.org/system/files/working_papers/w31161/w31161.pdf)
- **Average effect:** Issues resolved per hour rose 15% on average in the QJE version ("with substantial heterogeneity across workers"); the 2023 NBER version reported 14%. — [QJE](https://academic.oup.com/qje/article/140/2/889/7990658); [arXiv v2](https://arxiv.org/html/2304.11771v2)
- **Effect by baseline skill:**
  - Lowest-skill quintile: +0.5 resolutions/hour, about +36%, in the published version. The NBER WP reported 0.29 log points (about 34%) for "novice and low-skilled workers".
  - Experienced and high-skilled workers: "minimal impact" (WP).
  - The QJE abstract says the most experienced and highest-skilled workers see "small gains in speed and small declines in quality", while less experienced and lower-skilled workers improve both speed and quality.
  - [QJE](https://academic.oup.com/qje/article/140/2/889/7990658); [Li-hosted PDF](http://danielle.li/assets/docs/GenerativeAIatWork.pdf); [NBER WP PDF](https://www.nber.org/system/files/working_papers/w31161/w31161.pdf)
- **Mechanism:** The authors argue the tool "disseminates the potentially tacit knowledge of more able workers" and helps newer workers move down the experience curve. AI assistance also improved customer sentiment, increased retention, and may have led to worker learning. — [arXiv](https://arxiv.org/abs/2304.11771)
- **Limitations (from the design):**
  - One firm, one occupation, and a highly codifiable, high-volume task.
  - The assistant's suggestions encode top performers' behaviour, so experts have little to gain and their measured quality slightly fell.
  - Quality is measured by firm metrics (resolution, sentiment), not by expert review.
  - [QJE](https://academic.oup.com/qje/article/140/2/889/7990658)

#### Dell'Acqua et al., "Navigating the Jagged Technological Frontier" (BCG consultants)
- **Citation and versions:** HBS Working Paper 24-013 (September 2023). Now published in *Organization Science* 37(2): 403–423 (March–April 2026), DOI 10.1287/orsc.2025.21838. The published author list is Dell'Acqua, McFowland III, Mollick, Lifshitz (listed as "Hila Lifshitz", not "Lifshitz-Assaf"), Kellogg, Rajendran, Krayer, Candelon and Lakhani. — [Org Sci PDF](https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2025.21838); [IDEAS/RePEc](https://ideas.repec.org/a/inm/ororsc/v37y2026i2p403-423.html); [HBS WP PDF](https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf)
- **Design:** Preregistered randomized field experiment with 758 BCG consultants (about 7% of the firm's individual-contributor consultants), using GPT-4 on realistic consulting tasks. — [HBS WP (MIT-hosted copy)](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf); [Org Sci](https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2025.21838)
- **Inside the frontier (18 tasks):** Consultants completed 12.2% more tasks, worked 25.1% faster, and produced output rated more than 40% higher in quality. One summary gives 40.2%; an HBS AI Institute retrospective gives about 32%, so the quality figure depends on version and measure. — [Harvard Crimson](https://www.thecrimson.com/article/2023/10/13/jagged-edge-ai-bcg/); [JobCannon summary of WP 24-013](https://jobcannon.io/research/stats/dell-acqua-hbs-24-013); [HBS AI Institute](https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/)
- **Effect by baseline skill:**
  - WP abstract: "those below the average performance threshold increasing by 43% and those above increasing by 17% compared to their own scores." These are within-person gains relative to each consultant's baseline.
  - HBS Working Knowledge describes the split as below vs above median on a pre-task.
  - Conflicting figure: the HBS AI Institute retrospective reports bottom-half +31% and top-half +11% "on the experimental task". Which number appears in the 2026 Organization Science version is not confirmed.
  - [HBS WP (MIT-hosted)](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf); [HBS Working Knowledge](https://www.library.hbs.edu/working-knowledge/humans-vs-machines-untangling-the-tasks-ai-can-and-cant-handle); [HBS AI Institute](https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/)
- **Outside the frontier:** On a task deliberately chosen to fall outside GPT-4's capability, AI users were 19 percentage points less likely to produce the correct solution than consultants without AI. — [HBS WP (MIT-hosted)](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf); [Harvard Crimson](https://www.thecrimson.com/article/2023/10/13/jagged-edge-ai-bcg/)
- **Published framing:** AI "improves performance for some tasks but worsens it for others, even within the same knowledge workflow and with a seemingly similar level of difficulty". Workers "who skillfully navigate this frontier" gain substantial quality and productivity benefits, and the paper stresses "human judgment in discerning when AI augmentation is beneficial". — [Org Sci via IDEAS](https://ideas.repec.org/a/inm/ororsc/v37y2026i2p403-423.html)
- **Centaurs and cyborgs:** Successful users followed either a "centaur" pattern (dividing tasks between human and AI) or a "cyborg" pattern (tightly interleaving the two). — [Mollick, One Useful Thing](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)
- **Limitations:**
  - Participants were an elite, highly screened population, not true novices.
  - Tasks were designed by the researchers and done in a single session.
  - The model was the 2023 version of GPT-4.
  - The outside-frontier result rests on one task.
  - "Below-average" means below-average among BCG consultants.
  - [HBS WP (MIT-hosted)](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)

#### Noy & Zhang, *Science* (July 2023)
- **Citation:** "Experimental evidence on the productivity effects of generative artificial intelligence," *Science* (July 2023). — [Stanford SCALE listing](https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence); [MIT-hosted WP](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf)
- **Design:** Preregistered online experiment in which 453 college-educated professionals did occupation-specific, incentivized writing tasks, with half randomly given ChatGPT. The March 2023 working paper reported 444 participants and expressed effects in standard deviations. — [SUFE abstract mirror](https://academicnewsletter.sufe.edu.cn/info/256290); [Stanford SCALE](https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence)
- **Effects:**
  - Time taken fell 40% (0.8 SD in the WP) and output quality rose 18% (0.4 SD), as graded by independent evaluators.
  - "Inequality between workers decreased": ChatGPT "compresses the productivity distribution by benefiting low-ability workers more".
  - [EurekAlert](https://www.eurekalert.org/news-releases/995024); [MIT-hosted WP](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf)
- **Mechanism:** ChatGPT "largely substitutes for worker effort rather than complementing workers' skills". Time shifted away from rough drafting toward idea generation and editing. — [MIT-hosted WP](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf); [Continuum Labs summary](https://training.continuumlabs.ai/continuum-applications/discussion-and-use-cases/experimental-evidence-on-the-productivity-effects-of-generative-artificial-intelligence)
- **Adoption spillover:** Treated workers were 2 times as likely to use ChatGPT in their real job two weeks later, and 1.6 times as likely two months later. — [SUFE abstract mirror](https://academicnewsletter.sufe.edu.cn/info/256290)
- **Limitations:**
  - Tasks were short and self-contained (the WP itself warns this may overstate real-job usefulness).
  - Outputs were not fact-checked, so accuracy is unmeasured.
  - The model was early ChatGPT.
  - [TechXplore](https://techxplore.com/news/2023-07-productivity-effects-chatgpt-college-educated-professionals.amp); [MIT-hosted WP](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf)

### Inferences
- In all three studies the "floor-raising" effect has the same structure. The AI holds codified best practice (top agents' replies, consulting templates, competent prose), and the novice gains by borrowing it. That is exactly the "good enough" layer a generalist needs. It is weakest where the task is open-ended or outside the model's competence.
- These results measure output on assigned, well-specified tasks. They do not measure whether the novice became more skilled. Noy & Zhang explicitly read the result as effort substitution, and Brynjolfsson et al. find top performers' quality slips slightly.
- For a solo developer, the evidence supports this: AI can lift you quickly to "competent" on codifiable sub-tasks, but by itself it does not produce top-tier output, and it can mislead you on tasks beyond the frontier that you are not equipped to judge.

### Gaps
- I could not open the QJE full text to confirm the 36% lowest-quintile figure directly; it comes from search extraction of the published-version text. I also could not verify the oft-quoted claim that "agents with 2 months' tenure plus AI perform like 6-month agents without AI".
- I could not confirm whether the Organization Science version keeps the 43%/17% split or changes to the 31%/11% figure in the HBS retrospective.
- The page numbers and volume for Noy & Zhang's *Science* article were not re-verified this session (DOI 10.1126/science.adh2586 per standard records).

## 2. Counter-evidence and nuance: where AI widens gaps, slows experts, harms learning, or homogenizes output

### Takeaway
The "AI equalizes" result does not hold everywhere.
- **Judgment-heavy tasks favour the skilled:** in open-ended work where the user must select and implement AI advice (Kenyan entrepreneurs, debate), higher-skilled people gain and lower-skilled people gain nothing or are harmed.
- **Experts in their own mature domain:** experienced developers were 19% slower in early 2025. METR's 2026 update suggests a probable speedup now, but calls its own data unreliable.
- **Learners:** unguarded AI use cut later test scores by about 17% in two separate RCTs.
- **Homogenization:** AI-assisted creative output becomes more similar across people, which works against differentiation.
- **Excluded evidence:** the Toner-Rodgers materials-science paper, previously the main "AI favours top experts" evidence, was disavowed by MIT in May 2025 and must not be used.

### Cited Findings

#### Where higher-skilled people gain more, or low-skilled are harmed
- **Otis, Clarke, Delecourt, Holtz & Koning, citation:** Published in *Management Science* as "The Uneven Impact of Generative Artificial Intelligence on Entrepreneurial Performance: Evidence from a Field Experiment in Kenya", DOI 10.1287/mnsc.2024.06909. eScholarship lists a 2026-07-10 publication date, so the year is 2026, not 2024 or 2025; the 2024 date belongs to the working paper. — [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.06909); [eScholarship](https://escholarship.org/content/qt0fb001r8/qt0fb001r8.pdf)
- **Otis et al., design:** A 5-month RCT with 640 Kenyan entrepreneurs. The treatment group got a GPT-4-powered AI business mentor via WhatsApp; the control group got a standard business guide. — [Berkeley Haas](https://newsroom.haas.berkeley.edu/research/gen-ai-experiment-shows-mixed-results-in-helping-small-businesses-grow/); [HKS/CID listing](https://www.hks.harvard.edu/centers/cid/publications/uneven-impact-generative-ai-entrepreneurial-performance)
- **Otis et al., average effect:** The authors could not reject a zero average effect on revenue or profits. — [NBER conference paper](https://conference.nber.org/conf_papers/f194654.pdf)
- **Otis et al., effect by baseline performance:**
  - Above-median (high) performers gained "just over 15%" in revenue and profits.
  - Below-median performers did about 8% worse (Haas). HBS Working Knowledge reports a 10% decline instead.
  - [Berkeley Haas](https://newsroom.haas.berkeley.edu/research/gen-ai-experiment-shows-mixed-results-in-helping-small-businesses-grow/); [HBS Working Knowledge](https://www.library.hbs.edu/working-knowledge/what-happens-when-business-owners-turn-to-chatbots-for-advice)
- **Otis et al., mechanism (two versions):**
  - The early account said low performers asked AI about harder, more challenging problems.
  - The later framing says the widening inequality "does not stem from differences in the questions posed to or advice received from the AI, but from how entrepreneurs selected from and implemented the AI advice."
  - [Berkeley Haas](https://newsroom.haas.berkeley.edu/research/gen-ai-experiment-shows-mixed-results-in-helping-small-businesses-grow/); [Harvard D^3 summary](https://d3.harvard.edu/?p=30663)
- **Otis et al., limitations:** One country and context; the high/low split is a subgroup analysis; 2023-era GPT-4. — [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.06909)
- **Roldán-Monés (Esade EcPol WP, 2024), "When GenAI increases inequality":** An RCT with 142 law, economics and business undergraduates at a university debating competition, randomly given GenAI support to prepare 1-on-1 debates.
  - High-ability students "benefit significantly more from GenAI than their lower ability counterparts". IMF F&D reports high-ability debaters were 12% more likely to win with AI, with little change for lower-ability debaters.
  - Mechanism: high-ability students were better at extracting and using AI information.
  - The author argues that when tasks need higher-order skills and unpredictable interaction, and answers cannot be copy-pasted, high-ability workers benefit more.
  - [Esade EcPol](https://www.esade.edu/ecpol/en/publications/when-generative-ai-increases-inequality-experimental-evidence-from-a-university-debate-competition/); [PDF](https://esade.edu/ecpol/wp-content/uploads/2019/09/2409-ChatGPTRoldan_ecpol.pdf); [IMF F&D](https://www.imf.org/en/publications/fandd/issues/2025/06/machine-intelligence-and-human-judgement-ajay-agrawal)
- **Dell'Acqua et al. outside-frontier result (see Q1):** −19 percentage points in correctness. Relying on AI for a task it cannot do hurts, and the user must already have the judgment to know where the frontier lies. — [HBS WP (MIT-hosted)](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)

#### Experts working in their own domain: METR's randomized trial and its 2026 update
- **Early-2025 study:** Sixteen experienced open-source developers worked on their own mature repositories, with tasks randomized to allow or disallow AI (mainly Cursor Pro with Claude 3.5/3.7 Sonnet).
  - With AI, tasks took 19% longer (95% CI +2% to +39%).
  - Afterwards, developers estimated AI had made them about 20% faster.
  - [METR 2026 update post (restates the 2025 result)](https://metr.org/blog/2026-02-24-uplift-update/); [ScienceBlog](https://scienceblog.com/t-a-randomized-trial-by-metr-found-that-experienced-developers-completed-real-coding-tasks-19-slower-when-allowed-to-use-ai-tools-yet-afterwards-they-estimated-on-average-that-ai-had-made-them-20-fast/); [original METR post](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
  - *Not re-verified this session:* that developers forecast a 24% speedup beforehand, and that the study had 246 tasks. Both come from my recollection of METR's July 2025 post (arXiv 2507.09089).
- **Feb 24, 2026 update ("We are Changing our Developer Productivity Experiment Design"):** A new experiment began in August 2025 with a larger pool. Secondary coverage gives 57 developers, 143 repositories and 800+ tasks.
  - Returning developers: estimated "speedup of −18%" (CI −38% to +9%). In METR's sign convention, negative means faster, so this indicates a probable speedup.
  - Newly recruited developers: −4% (CI −15% to +9%).
  - [METR](https://metr.org/blog/2026-02-24-uplift-update/); [Rob Bowley summary](https://blog.robbowley.net/2026/04/04/metrs-developer-productivity-research-2026-update/)
- **METR's caveats on the update:**
  - METR calls the new data an unreliable signal. More developers refused to join because they did not want to work without AI, and 30–50% said they withheld tasks they did not want to do without AI.
  - These selection effects likely bias the measured speedup downward.
  - METR believes developers are "likely more sped up" in early 2026 than in early 2025, but calls its data "only very weak evidence for the size of this increase".
  - [METR](https://metr.org/blog/2026-02-24-uplift-update/)
- **Secondary coverage warning:** Some secondary sources misreport the −18% as an "18% slowdown", or as a definitive 18% speedup. — [Particula](https://particula.tech/blog/metr-reversed-19-percent-slower-ai-coding-study); [Yutuo](https://www.yutuo-tech.com/en/blog/metr-19-percent-claim/)

#### Software developers in field experiments (Cui, Demirer et al.): supports floor-raising
- **Citation:** Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz, "The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers". SSRN 4945566 (revised August 2025); *Management Science*, DOI 10.1287/mnsc.2025.00535. — [SSRN](https://papers.ssrn.com/abstract=4945566); [Management Science](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535)
- **Design:** RCTs at Microsoft, Accenture and an anonymous Fortune 100 firm, with GitHub Copilot access randomized and 4,867 developers in total. — [Demirer PDF](https://www.mertdemirer.com/Papers/Demirer_AI_productivity.pdf)
- **Average effect:** Pooled, completed tasks rose 26.08% (SE 10.3%). Each experiment on its own is noisy. — [SSRN](https://papers.ssrn.com/abstract=4945566)
- **Effect by experience:**
  - Recent hires and junior developers: +27% to +39% (MIT Sloan's figures).
  - Senior and long-tenure developers: +8% to +13%. Demirer: "For those who are more experienced we actually don't see much of an effect."
  - Short-tenure developers were 9.5% more likely to adopt Copilot.
  - [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-affects-highly-skilled-workers); [getDX summary](https://newsletter.getdx.com/p/copilot-impact-on-productivity)
- **Limitations:**
  - Outcomes are output counts (pull requests, commits, builds), not code quality.
  - The tool was the 2022–23 Copilot autocomplete, not today's agents.
  - The paper is also hosted by Microsoft Research, and some co-authors are industry researchers.
  - [Microsoft Research page](https://www.microsoft.com/en-us/research/?p=1148213)

#### Learning and deskilling (directly relevant to someone learning new crafts with AI)
- **Bastani et al., citation:** "Generative AI without guardrails can harm learning: Evidence from high school mathematics", *PNAS* 122(26), 2025, DOI 10.1073/pnas.2422633122. — [IDEAS](https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html); [Penn CHIBE](https://chibe.upenn.edu/publications/generative-ai-without-guardrails-can-harm-learning-evidence-from-high-school-mathematics)
- **Bastani et al., design and results:** About 1,000 Turkish high-school students across three arms: GPT Base (ChatGPT-like), GPT Tutor (learning-safeguard prompts) and a no-AI control.
  - GPT Base: practice performance +48%, but exam scores −17% vs control.
  - GPT Tutor: practice +127%, with exam scores about the same as control.
  - The authors attribute the loss to students using the tool as a "crutch".
  - Limitation: only short-term outcomes were measured.
  - [Wharton Knowledge](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education); [PsyPost](https://www.psypost.org/unrestricted-generative-ai-harms-high-school-math-learning-by-acting-as-a-crutch/)
- **Anthropic (late Jan 2026), "How AI assistance impacts the formation of coding skills":** An RCT with 52 mostly junior software engineers learning a new Python library (Trio).
  - Quiz scores: about 50% for the AI group vs about 67% for hand-coders, which Anthropic describes as "17% lower", roughly two letter grades. The biggest gap was on debugging.
  - The AI group was about 2 minutes faster, which was not statistically significant.
  - How people used AI mattered: those who asked conceptual and follow-up questions retained more.
  - Limitations: one hour of learning, an immediate test, small N, and a sidebar assistant rather than an agentic coder.
  - [Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills); [InfoQ](https://infoq.com/news/2026/02/ai-coding-skill-formation/)

#### Homogenization: AI raises individual quality but reduces collective diversity
- **Doshi & Hauser, citation and core result:** *Science Advances* 10, eadn5290 (12 July 2024). In an online experiment, writers who got story ideas from GPT-4 produced stories rated more creative, better written and more enjoyable, "especially among less creative writers". But "generative AI–enabled stories are more similar to each other than stories by humans alone", which the authors frame as a social dilemma. — [Science Advances](https://www.science.org/doi/10.1126/sciadv.adn5290); [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532)
- **Doshi & Hauser, effects for low-creativity writers (low DAT scores):**
  - Novelty: +6.3% with one AI idea, +10.7% with five AI ideas.
  - Summary figure for less creative writers: about 10–11% gains in creativity and 22–26% in how enjoyable and well written the stories were.
  - [EurekAlert](https://www.eurekalert.org/news-releases/1050888); [ResearchBunny summary](https://www.researchbunny.com/papers/generative-ai-enhances-individual-creativity-but-reduces-the-collective-diversity-of-novel-content-ge6b)
- **Doshi & Hauser, self-ratings:** AI-assisted writers did not rate their own stories as more creative; external evaluators did. — [PsyPost](https://psypost.org/new-study-on-ai-assisted-creativity-reveals-an-interesting-social-dilemma)
- **Zhou & Lee, citation and design:** "Generative artificial intelligence, human creativity, and art", *PNAS Nexus* 3(3): pgae052 (March 2024). An observational study (staggered adoption) of more than 4 million artworks from more than 50,000 users on an art-sharing platform. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10914360)
- **Zhou & Lee, results:**
  - Text-to-image AI raised creative productivity by 25% (about 2x in the first month, settling to 25%).
  - Value, measured as the likelihood of receiving a favorite per view, rose 50%.
  - Peak content novelty rose while average content novelty fell, which the authors call "an expanding but inefficient idea space".
  - Both peak and average visual novelty consistently declined.
  - Artists who successfully explored novel ideas got better peer evaluations.
  - AI adoption decreased the concentration of favorites among adopters.
  - [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10914360); [BU DBI](https://www.bu.edu/dbi/2024/03/04/generative-ai-human-creativity-and-art)
- **Zhou & Lee, limitations:** Observational; favorites are a proxy for value; a single platform.
- **Meincke, Nave & Terwiesch (*Nature Human Behaviour*, 2025, per Wharton's Mack Institute):** A reanalysis of brainstorming experiments.
  - In 37 of 45 comparisons, ChatGPT-assisted ideas were significantly less diverse.
  - In a toy-invention task, 94% of ChatGPT-assisted ideas shared overlapping concepts, and nine participants independently named their toy "Build-a-Breeze Castle".
  - GPT-4 was more diverse than GPT-3.5 but still well below humans.
  - Suggested mitigation: ask the model for several ideas that are explicitly different from each other.
  - [Wharton Mack Institute](https://mackinstitute.wharton.upenn.edu/2025/new-in-nature-chatgpt-decreases-idea-diversity-in-brainstorming/); [Wharton Knowledge](https://knowledge.wharton.upenn.edu/article/does-ai-limit-our-creativity); [Axios](https://www.axios.com/2025/06/18/ai-chatgpt-research-creativity-brainstorming)

#### AI as a substitute for a cross-functional teammate (generalist-relevant)
- **Dell'Acqua et al., "The Cybernetic Teammate" (NBER WP 33641, 2025):** A preregistered field experiment with 776 Procter & Gamble professionals on new-product development, in a 2×2 design (AI vs no AI; individual vs two-person team).
  - Individuals with AI matched the performance of teams without AI.
  - AI broke down functional silos. Without AI, R&D people proposed technical solutions and commercial people proposed commercial ones; with AI, both produced balanced solutions regardless of background.
  - AI also produced more positive self-reported emotions.
  - Caveat: P&G staff are co-authors, and P&G gave financial support to a Harvard research institute.
  - [NBER](https://www.nber.org/papers/w33641); [Mollick, One Useful Thing](https://www.oneusefulthing.org/p/the-cybernetic-teammate)

#### Withdrawn study: exclude
- **Toner-Rodgers, "Artificial Intelligence, Scientific Discovery, and Product Innovation" (2024):**
  - On May 16, 2025, MIT said it had "no confidence in the provenance, reliability or validity of the data" and "no confidence in the veracity of the research contained in the paper".
  - MIT asked arXiv to mark the paper withdrawn (the author had not done so) and asked that it be withdrawn from the *Quarterly Journal of Economics*, where it had been submitted. The author is "no longer at MIT".
  - Concerns were raised via Daron Acemoglu and David Autor.
  - As of late May 2025 the paper was still visible on arXiv; I found no later confirmation of its arXiv status.
  - [TechCrunch](https://techcrunch.com/2025/05/17/mit-disavows-doctoral-students-paper-on-ai-productivity-benefits); [The Decoder](https://the-decoder.com/mit-says-a-high-profile-ai-productivity-study-used-data-that-cannot-be-trusted/)

### Inferences
- Across these studies, what predicts benefit is not "generalist vs specialist" but the user's ability to judge, select and integrate AI output. Otis et al. (published framing), Roldán-Monés, Dell'Acqua's "navigating the frontier", and Anthropic's finding that conceptual questioners retained more all point the same way. Novices gain most when the AI already encodes the right answer; skilled people gain more when the task is open-ended and the AI produces a mix of good and bad suggestions.
- For a beginner learning 3D, animation and music, two RCTs show that unguarded AI use can sharply cut learning, about −17% in each. AI used as a tutor or explainer does not show this loss (GPT Tutor in Bastani; conceptual questioners in Anthropic). This matters more than the productivity numbers for a three-year self-training plan.
- Homogenization is consistent across text, ideas and images. If everyone's "good enough" comes from the same models, it becomes a commodity, and the remaining differentiator is whatever the human adds: taste, unusual ideas, curation. This is an inference across the studies; none directly measures market returns to that differentiation (but see Q4's Steam data).
- METR's experts-in-own-codebase result and the Cui et al. junior/senior split fit one picture. AI helps most when you know little about a codebase or task, and least or negatively when you already know it deeply. For someone who cannot code and relies on AI, expect large early gains. The risk is a growing codebase you cannot debug, which ties to the Anthropic debugging gap.

### Gaps
- Exact overall novelty/usefulness gains and the similarity percentage in Doshi & Hauser could not be verified. Commonly cited "+8.1% novelty / +9.0% usefulness (5 ideas)" figures are unconfirmed, and participant counts differ by source (PsyPost reports 500 Prolific participants).
- METR's 2025 forecast (+24%) and task count (246) are from recollection, not re-verified.
- No rigorous study found on the 3D-art, animation or music skill gap specifically (e.g., novice vs professional 3D artists with AI tools). Evidence for those crafts is extrapolated from writing, ideation, images and code.
- I recall the Toner-Rodgers paper's claim that top scientists benefited most while the bottom third gained little. This was not re-verified, and the paper should not be used either way.

## 3. Labor-market evidence: freelancers and early-career workers

### Takeaway
The early labor-market evidence points the same way across studies. Generative AI has cut demand for freelance work in directly substitutable crafts:
- Writing: −2% jobs and −5.2% earnings.
- Images: −3.7% jobs and −9.4% earnings; −17% image-creation job posts.
- Writing and coding: −21% job posts relative to manual work.

Top-rated freelancers were not protected, and in image work they were hit hardest. Early-career workers in AI-exposed occupations show a growing relative employment gap (−13% in Aug 2025 → −16% → −19% in Aug 2026), operating mainly through fewer hires. However, Danish administrative data show precise nulls on earnings and hours. The losers are people selling automatable execution, whether specialists or juniors. The evidence does not show generalists specifically being hurt or helped.

### Cited Findings
- **Hui, Reshef & Zhou, citation:** "The Short-Term Effects of Generative Artificial Intelligence on Employment: Evidence from an Online Labor Market", *Organization Science* 35(6): 1977–1989 (2024), DOI 10.1287/orsc.2023.18441. — [Organization Science](https://pubsonline.informs.org/doi/abs/10.1287/orsc.2023.18441?journalCode=orsc); [WashU profile](https://profiles.wustl.edu/en/publications/the-short-term-effects-of-generative-artificial-intelligence-on-e/)
- **Hui et al., design and results:** Difference-in-differences on Upwork around the releases of ChatGPT, DALL-E 2 and Midjourney.
  - Writing-related freelancers: −2% monthly jobs and −5.2% monthly earnings after ChatGPT.
  - Image-related freelancers: −3.7% monthly jobs and −9.4% monthly earnings after DALL-E 2 and Midjourney.
  - Freelancers with more years of experience were not affected any less.
  - Figures are from the 2023 working-paper coverage; I could not confirm whether the published version's estimates differ.
  - [WashU Olin news](https://olin.washu.edu/about/news-and-media/news/2023/08/study-ai-tools-cause-a-decline-in-freelance-work-and-incomeat-least-in-the-short-run.php); [VoxEU](https://cepr.org/voxeu/columns/artificial-intelligence-and-its-short-term-effects-employment)
- **Hui et al., high-quality freelancers:**
  - High-quality service (past performance and employment) "did not moderate the adverse effects on employment".
  - There is "suggestive evidence that top freelancers are disproportionately affected", especially in image-focused occupations.
  - [Organization Science](https://pubsonline.informs.org/doi/abs/10.1287/orsc.2023.18441?journalCode=orsc); [WashU Olin news](https://olin.washu.edu/about/news-and-media/news/2023/08/study-ai-tools-cause-a-decline-in-freelance-work-and-incomeat-least-in-the-short-run.php)
- **Demirci, Hannane & Zhu, citation:** "Who Is AI Replacing? The Impact of Generative AI on Online Freelancing Platforms", *Management Science* 71(10) (2025), DOI 10.1287/mnsc.2024.05420. — [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420)
- **Demirci et al., results:**
  - Eight months after ChatGPT, job posts for automation-prone writing and coding work fell about 21% relative to manual-intensive jobs. This is a relative, not absolute, decline.
  - Job posts for image creation fell 17% after image-generating AI.
  - Competition among freelancers increased, and the surviving automation-prone jobs were more complex and better paid.
  - Google Trends data link the drop to public awareness of ChatGPT.
  - [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420); [Semantic Scholar](https://www.semanticscholar.org/paper/Who-is-AI-Replacing-The-Impact-of-Generative-AI-on-Demirci-Hannane/753eb709e52f37699e994553088857e8aa3d1d6c); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4602944)
- **Brynjolfsson, Chandar & Chen, "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence" (Stanford Digital Economy Lab; ADP payroll data):**
  - August 2025 version: workers aged 22–25 in the most AI-exposed occupations saw a 13% relative employment decline after controlling for firm-level shocks. Less-exposed workers and older workers in the same occupations were stable or growing. Declines were concentrated where AI automates rather than augments.
  - November 2025 revision: the relative decline is 16%.
  - August 2026 version: employment is 19% below where it would be had it kept pace with less-exposed peers. The divergence "has widened steadily", and it works "primarily through reduced hiring of young workers rather than increased separations".
  - The authors call these "early, descriptive indicators", not causal estimates, and find "no evidence of widespread, economy-wide job displacement".
  - [Stanford DEL news](https://digitaleconomy.stanford.edu/news/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/); [Aug 2026 PDF](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- **Canaries, software developers:** Employment of software developers aged 22–25 fell nearly 20% from its late-2022 peak by July 2025. — [HCA Magazine](https://www.hcamag.com/nz/news/general/the-entry-level-job-is-disappearing/575696); [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/09/ai-taking-jobs/)
- **Hosseini & Lichtinger, "Generative AI as Seniority-Biased Technological Change" (latest version May 2026):** Based on US résumé and job-posting data covering about 65 million workers at more than 280,000 firms (2015–2025).
  - Starting in 2023Q1, junior employment at GenAI-adopting firms fell sharply relative to non-adopters, while senior employment kept rising. Adoption is identified by postings for "GenAI integrator" roles.
  - The decline came from slower hiring, not separations or promotions.
  - By education the pattern is U-shaped: mid-tier graduates were hit hardest, elite and low-tier graduates less.
  - The authors describe this as associational evidence.
  - [May 2026 PDF](https://raw.githack.com/s-mahdihosseini/Website/b99fa2962dcc4c165bbc3c41dd283afa99c5ccfb/GenAI_SenBTC_May_2026.pdf); [Stanford DEL seminar](https://digitaleconomy.stanford.edu/event/seyed-m-hosseini-and-guy-lichtinger-generative-ai-as-seniority-biased-technological-change-evidence-from-u-s-resume-and-job-posting-data)
- **Humlum & Vestergaard, "Large Language Models, Small Labor Market Effects" (NBER WP 33777, May 2025):** Two adoption surveys covering 11 exposed occupations were linked to Danish administrative data (25,000 workers, 7,000 workplaces).
  - Precise null effects on earnings and recorded hours, ruling out effects larger than 2% two years after adoption.
  - Time savings were modest (about 3%), and new oversight and integration tasks emerged.
  - The nulls hold for early-career jobs and intensive users.
  - [IDEAS/NBER](https://ideas.repec.org/p/nbr/nberwo/33777.html); [BFI WP](https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf); [ETUI slides](https://www.tsl.fi/media/koulutus/etui/kurssit-syksy2025/ai-talks-etui-large-language-models-small-labor-market-effects-9.9.2025.pdf)

### Inferences
- The labor data separate who loses by what they sell, not by breadth. People selling commodity execution lose: freelance illustrators, copywriters and translators, and junior coders. That holds even for highly rated specialists (Hui et al.). Work that survives skews toward more complex, better-paid tasks (Demirci et al.), meaning work that requires judgment and integration.
- "Today only specialists succeed" is not supported in that form. A narrow specialist in an automatable craft (e.g., a freelance image maker) is among the most exposed groups. Conversely, entry-level roles are where AI substitution shows up, which cuts against "learn by doing junior work".
- The Danish nulls versus the US youth-hiring declines suggest effects so far fall on hiring and entry, not on incumbents' pay. Evidence is still early and contested.

### Gaps
- I found no study that directly compares generalist vs specialist freelancers (e.g., multi-category vs single-category profiles) before and after generative AI. This is a key missing piece for the user's question.
- I could not retrieve the published Organization Science estimates for Hui et al., so the 2023 working-paper figures may differ.
- I did not locate the formal critiques of "Canaries" (e.g., confounding from post-2022 tech-hiring cycles and interest rates), so I cannot summarize them.
- There is no labor-market evidence specific to game artists, animators or game composers. Survey-based industry data are covered in Q4.

## 4. Game industry: adoption, developer sentiment, Steam disclosures and player attitudes

### Takeaway
- **Developers:** use is broad but mostly non-creative (research, email, code). Sentiment has turned sharply negative: 52% said generative AI is harming the industry in the 2026 GDC survey, up from 30% in 2025 and 18% in 2024, with only 7% positive.
- **Steam:** AI-disclosed games rose from 10.9% of releases in 2024 to 19.9% in 2025 and 30.8% in 2026 year-to-date. They account for most of the growth in release volume but a disproportionately small share of revenue and reviews.
- **Players:** most are hostile in surveys, especially to AI art, music and writing, and Steam reviews of AI-disclosing games are more negative. However, a large neutral majority says quality matters more, and a commercial hit with AI voices (Arc Raiders) still sold 12.4 million copies.
- **Valve rules:** since January 2026, AI coding and other dev-tool use does not need to be disclosed, but AI-generated shipped content does.

### Cited Findings
- **GDC 2025 State of the Game Industry:**
  - 52% of respondents work at companies using generative AI tools.
  - 30% believe generative AI is having a negative impact on the industry, a 12-point rise from 2024.
  - [GDC](https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/); [PlayStation Universe](https://www.psu.com/news/gdc-survey-finds-52-developers-work-at-companies-that-are-using-generative-ai/); [BusinessWire](https://www.businesswire.com/news/home/20250121745145/en/The-2025-Game-Industry-Survey-Reveals-Increasing-Impact-Of-Layoffs-Concerns-With-The-Usage-Of-Generative-AI-Funding-Challenges-and-More)
- **GDC 2026 State of the Game Industry (released late January 2026; 2,300+ respondents), sentiment:**
  - 52% (1,196 people) say generative AI is having a negative impact on the industry, up from 30% (2025) and 18% (2024).
  - Only 7% say it is positive; the rest are mixed.
  - [GDC](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [GameSpot](https://www.gamespot.com/articles/more-developers-than-ever-believe-generative-ai-is-hurting-the-game-industry/1100-6537793/); [BusinessWire](https://www.businesswire.com/news/home/20260129438528/en/2026-State-of-the-Game-Industry-Report-Reveals-Widening-Effect-of-Layoffs-Broader-Perspectives-on-Generative-AI-Unionization-Tariffs-and-More)
- **GDC 2026, usage:**
  - 36% personally use generative AI at work: 30% at game studios vs 58% at publishing, support and marketing/PR firms.
  - Tools: ChatGPT 74%, Gemini 37%, Microsoft Copilot 22%.
  - Uses: research or brainstorming 81%, daily tasks such as email 47%, code assistance 47%, prototyping 35%.
  - A GDC content manager said most users apply it to non-creative tasks.
  - [GamesBeat](https://gamesbeat.com/state-of-game-industry-survey-sheds-light-on-layoffs-genai-views-unionization-and-tariffs-gdc-survey/); [Game Developer](https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry); [Winbuzzer](https://winbuzzer.com/2026/03/23/generative-ai-gaming-gdc-2026-developer-opposition-xcxwbn/)
- **GDC 2024 positive figure:** One analysis gives 21% positive in 2024, falling to 7% in 2026. — [Ziva](https://ziva.sh/blogs/gdc-2026-generative-ai-game-development-data)
- **Caution on the 52% figures:** "52%" appears both as "work at a company using gen AI" (2025, and per Winbuzzer also 2026) and as "negative impact" (2026). The report writer should label which is which.
- **Valve's January 2026 rewrite of Steam's AI disclosure form:**
  - "Efficiency gains through the use of [AI-powered dev tools] is not the focus", so code helpers and similar tools need no disclosure.
  - AI-generated content that ships in the game, on the store page or in marketing must still be disclosed, as must AI content generated live during gameplay. Developers describe their use in a text box.
  - This was the first revision since the disclosures began in January 2024.
  - [VGC](https://www.videogameschronicle.com/news/valve-has-significantly-rewritten-steams-rules-for-how-developers-much-disclose-ai-use); [Game Developer](https://gamedeveloper.com/business/valve-tweaks-and-clarifies-ai-disclosure-rules-for-steam)
- **Sulka Haro's census of Steam disclosures (53,597 releases, July 2023 – July 2026):**
  - AI-flagged launches went from about 13/month before the disclosure mandate to about 530/month.
  - "60–90% of the growth in monthly Steam releases is AI-flagged games."
  - AI-disclosed share of releases: 10.9% (2024), 19.9% (2025), 30.8% (2026 to date). PC Gamer projects that more than half of new releases could carry disclosures by 2027–28 (a projection).
  - [Haro, Substack](https://fragwyz.substack.com/p/three-years-of-ai-on-steam); [GamesRadar](https://www.gamesradar.com/games/steam-study-of-over-53-000-games-finds-60-90-percent-of-the-growth-in-monthly-releases-on-valves-store-is-from-games-using-ai-and-almost-none-of-them-make-money/); [PC Gamer](https://www.pcgamer.com/gaming-industry/steam-week-in-review-take-cover-because-it-looks-like-more-than-half-of-steam-games-will-have-an-ai-disclosure-by-2027-2028/)
- **Haro's census, revenue concentration (estimated by the Boxleiter method: reviews × 30 × price; order-of-magnitude only):**
  - The top 1% of titles take about 94% of estimated revenue, and the top 10 games about 62%.
  - A typical game with any reviews earns about $300, and about 28% get zero reviews.
  - GamesRadar stresses that "almost none make money" applies to non-AI games too.
  - [GamesRadar](https://www.gamesradar.com/games/steam-study-of-over-53-000-games-finds-60-90-percent-of-the-growth-in-monthly-releases-on-valves-store-is-from-games-using-ai-and-almost-none-of-them-make-money/); [Haro](https://fragwyz.substack.com/p/three-years-of-ai-on-steam)
- **Secondary reports on Haro's data:**
  - AI-flagged games reach 100 reviews at about 55% of the rate of non-AI games, with no improvement over two years.
  - In Q2 2026, AI-disclosed games were about 33% of new releases but about 10% of sales.
  - Disclosure covers art, sound and text, not code, so "vibe-coded" games are invisible in these numbers.
  - [Cinevva](https://app.cinevva.com/news/2026-07-20-steam-ai-disclosure-study); [GetRekt](https://www.getrekt.com/news/steam-2026-release-record-ai-vibe-coding/)
- **Quantic Foundry gamer survey (published December 18, 2025):**
  - 85% of respondents have a below-neutral attitude to generative AI in games, and 63% picked the most negative option.
  - Ages 13–17: only 3% positive; ages 45+: 22% positive.
  - Most negative for artistic and creative uses (art, music/SFX, narrative/dialogue). Backend uses do better: dynamic difficulty is 26% positive and 24% neutral.
  - The sample is reported differently by outlet (one says 1,799 respondents surveyed October–December 2025).
  - [Quantic Foundry](https://quanticfoundry.com/2025/12/18/gen-ai/)
- **MIDiA Research:** Daily gamers are largely neutral about AI in development "if the game is good". — [MIDiA](https://www.midiaresearch.com/blog/new-research-what-do-gamers-really-think-about-generative-ai-in-games)
- **GameDiscoverCo survey (about 3,800 Steam users):** 8.1% are unwilling to buy games with AI content under any circumstances. — [Gamereactor](https://www.gamereactor.eu/only-8-of-steam-users-say-they-wouldnt-buy-a-game-if-it-contained-ai-1745073/); [WN Hub](https://wnhub.io/news/analytics/item-51398)
- **Bazzaz & Cooper, "Player Perceptions of Generative AI in Games: A Steam Review Analysis" (arXiv 2608.11539, 2026; Northeastern; ACM HCI journal):**
  - Analysis of 508,192 English Steam reviews, using procedurally generated (PCG) games as the baseline.
  - Gen-AI-disclosing games get lower recommendation rates and more negative sentiment.
  - A thematic analysis of 600 reviews finds players read generative AI use as a sign of low developer investment.
  - The authors recommend deploying gen AI "for what players need, not for what makes development cheaper".
  - Only the abstract was retrieved, so effect sizes are unknown.
  - [arXiv](https://arxiv.org/pdf/2608.11539)
- **Counterpoint (Madanamootoo & Alla, arXiv 2608.07825, July 2026; not peer-reviewed; first author co-founded the studied platform):**
  - AI-disclosed releases in a verified subsample got catalog-typical review scores (median 85.9% positive).
  - AI-disclosed releases rose eightfold in 18 months.
  - [arXiv](https://arxiv.org/pdf/2608.07825)
- **Clair Obscur: Expedition 33 and the Indie Game Awards:**
  - On December 20, 2025, the Indie Game Awards rescinded the game's Game of the Year and Debut Game awards, two days after granting them.
  - IGA rules make "games developed using generative AI strictly ineligible", and Sandfall had said no gen AI was used.
  - Sandfall had briefly used gen AI for placeholder textures (newspaper-clipping-like backgrounds), which were patched out after launch.
  - [AV Club](https://www.avclub.com/clair-obscur-genai-iga-awards-rescinded); [Push Square](https://www.pushsquare.com/news/2025/12/ps5-fave-expedition-33-stripped-of-indie-game-awards-but-not-for-the-reasons-you-may-think)
- **Arc Raiders (Embark/Nexon):**
  - Its AI-generated voice lines drew criticism ("dull and flat"; concern for voice actors) and some boycott calls.
  - It still passed 12.4 million sales by January 2026 and set Steam concurrent-player records.
  - Embark later re-recorded some lines with human actors, and studio head Patrick Söderlund said the game now has fewer AI voice lines than at launch.
  - [GamingOnLinux](https://www.gamingonlinux.com/2026/01/arc-raiders-hits-over-12-4m-sales-new-patch-out-with-weapon-nerfs-a-free-gift-and-a-darker-stella-montis/page=1/); [ScreenHub](https://www.screenhub.com.au/news/games/arc-raiders-ai-voice-actors-replaced-2695984/); [TopGear](https://www.topgear.com/car-news/gaming/extraction-shooter-arc-raiders-already-a-hit-its-ai-voice-acting-has-ruffled-some); [Gfinity](https://www.gfinityesports.com/article/arc-raiders-is-facing-boycotts-for-its-use-of-ai-content)

### Inferences
- For a small indie game, visible AI assets (art, music, voices, text) carry a measurable reputational and discoverability cost: stated hostility, more negative reviews, a lower rate of reaching 100 reviews, and award ineligibility. Players read them as "low investment". AI-written code carries no disclosure obligation on Steam and is largely invisible to players.
- The Steam data show what floor-raising looks like at market scale. AI makes it easy to ship "good enough" content, so supply floods (60–90% of release growth), while revenue stays extremely concentrated. Being "good enough" across many domains is necessary but nowhere near sufficient. Differentiation decides outcomes, and that is exactly where AI homogenizes (Q2).
- Big studios can absorb AI backlash when the game itself is strong (Arc Raiders). A solo indie lacks that buffer, and the indie press and awards ecosystem is the most hostile to it (IGA rule).

### Gaps
- I could not access the GDC primary PDFs, so the 2025 personal-use percentage and any 2026 asset-generation breakdown (share using gen AI for art, audio or 3D) are unverified.
- Totally Human's mid-2025 count (about 7,818 titles, about 7% of the Steam library, about 60% of disclosures for asset generation) and Game Oracle's figure (20.9% of January–November 2025 releases) appeared only in aggregator summaries; their primary pages were not retrieved.
- I found no rigorous causal estimate of the sales penalty from AI disclosure, controlling for game quality. Existing comparisons are descriptive.
- Larian's December 2025 gen-AI controversy was not covered by my searches.

## 5. Practical state (2025–2026) of AI tools for solo game content, and the legal status of AI music

### Takeaway
As of late 2026:
- **3D generation** (Meshy, Tripo, Rodin, Hunyuan3D, TRELLIS.2) reliably produces props and blockout or "draft" assets. Deforming hero characters still typically need retopology, UV and texture fixes, rigging, LODs and engine testing.
- **Auto-rigging** is solid for standard humanoids. Non-humanoid support is mostly vendor claims.
- **Single-camera markerless mocap** is cheap but limited by depth ambiguity and contact errors, so it needs cleanup (e.g., in Cascadeur).
- **Open text-to-motion models** exist (Tencent HY-Motion 1.0, December 2025) but output generic motions on standard skeletons.
- **AI music** is in legal flux. Udio disabled downloads after settling with UMG. Suno settled with Warner, retired all older models for licensed V6 models (September 2026), and still faces UMG and Sony litigation. Purely AI-generated tracks are not copyrightable in the US.

The human-skill layer that remains is art direction and style consistency, deformation-ready topology, animation acting and timing, game feel, and a coherent musical identity.

### Cited Findings

#### 3D model generation
- **General limits:** The 2026 reviews agree that AI 3D generators are "not reliably one-click production tools" for deforming characters, exact hard-surface parts or a consistent hero-asset library. Hero assets and animated characters "typically still need retopology, UV and texture review, rigging, collision, LODs and target-engine testing". Most generators output dense triangle meshes. — [Cinevva guide](https://app.cinevva.com/guides/ai-3d-model-generators); [Wavect](https://wavect.io/blog/ai-3d-model-generators-game-development-2026/); [IndieHackers test of 9 tools](https://www.indiehackers.com/post/best-ai-3d-model-generator-in-2026-i-tested-9-of-the-best-and-here-is-what-i-found-70ecab1a0a)
- **Meshy:** Claims "Smart Topology" generates directly at a 100–300k face budget, with no separate retopology pass. This is a vendor claim; an independent review says Meshy output still needs retopology for hero assets but works for secondary props. — [Meshy blog (vendor)](https://www.meshy.ai/blog/best-ai-tools-for-3d-game-assets); [Wavect](https://wavect.io/blog/ai-3d-model-generators-game-development-2026/)
- **Tripo:** Offers auto-retopology and rigging (rigging limited, paid tiers only). A reviewer found output still needed UV and topology adjustment before Unity or Unreal import, "particularly for organic shapes and characters with complex silhouettes". — [Rapid Direct test](https://www.rapiddirect.com/blog/best-8-ai-3d-model-generators/); [Trify3D](https://trify3d.com/blog/what-ai-makes-game-models-the-best)
- **TRELLIS.2 (Microsoft):** Open-source (MIT), image-to-3D only. Retopology, UVs and rigging must be done in external DCC tools (per a competitor's comparison page, so possibly biased), and a review says it needs a 24GB GPU to run locally. — [Meshy vs TRELLIS 2 (vendor)](https://www.meshy.ai/compare/meshy-vs-trellis-2); [Triverse](https://triverse.ai/blog/best-ai-3d-model-generators-for-game-dev)
- **Hunyuan3D (Tencent):** A strong open-source option, but hosting, licensing and hardware costs can erase the saving. — [Cinevva guide](https://app.cinevva.com/guides/ai-3d-model-generators)

#### Auto-rigging
- **Armature (FabricatorStudio, August 2026):** A free, AI-assisted standalone rigging tool with templates for bipeds, quadrupeds and props, plus modular parts for creatures. Finger counts are set by the artist, not inferred. — [CG Channel](https://www.cgchannel.com/2026/08/armature-is-a-free-ai-assisted-standalone-character-rigging-tool/); [Digital Production](https://digitalproduction.com/2026/08/17/armature-2-automates-character-rigging/)
- **Meshy vs competitors:** Meshy's built-in auto-rig handles only humanoids, according to a competitor's documentation. 3D AI Studio's "Prism" claims non-humanoid rigs that follow the Mixamo spec, which is a vendor claim. — [3D AI Studio docs](https://docs.3daistudio.com/processing/rigging)

#### Markerless video motion capture and cleanup
- **Move.ai:** Generally seen as the quality leader for markerless capture, with its accuracy advantage coming from multi-camera solves. Paid plans are reportedly around $99/month, with a small free single-camera tier. — [3DXDev comparison](https://3dxdev.com/ai-motion-capture-from-video-in-2026-every-tool-compared/); [Neolemon](https://www.neolemon.com/blog/best-ai-motion-capture-tools-for-character-animation/)
- **Single-camera limits:** Depth ambiguity weakens crossed limbs and ground contact. — [3DXDev](https://3dxdev.com/ai-motion-capture-from-video-in-2026-every-tool-compared/)
- **Rokoko Vision:** Offers free single-camera browser capture. — [3DXDev](https://3dxdev.com/ai-motion-capture-from-video-in-2026-every-tool-compared/)
- **Cascadeur:** Used to clean up "raw, sometimes floaty" capture with AutoPhysics and animation unbaking. Version 2026.1 added an AI Root Motion tool and collision-penetration cleaning. — [3DXDev](https://3dxdev.com/ai-motion-capture-from-video-in-2026-every-tool-compared/); [AI Central comparison](https://www.aicentralresources.com/compare/move-ai-vs-cascadeur)

#### Text-to-motion
- **Tencent HY-Motion 1.0 (open weights and code, released around December 30, 2025):**
  - A billion-parameter Diffusion Transformer with flow matching, pretrained on 3,000+ hours of motion data, then fine-tuned and RLHF-tuned.
  - Covers 200+ motion categories in 6 classes, with a Lite variant.
  - Outputs SMPL-H skeletons for integration into DCC tools and engines.
  - [arXiv 2512.23464](https://arxiv.org/abs/2512.23464v1); [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/tencent-open-sources-hy-motion-1-0-a-billion-parameter-text-to-motion-ai-model/)

#### AI music: lawsuits, settlements and licensing (status as of October 2026; many details only from secondary trackers)
- **Udio:** UMG settled with Udio in late October 2025, and the same day Udio told users that downloads were no longer available (a walled-garden pivot). Financial terms were not disclosed. — [Dubspot](https://blog.dubspot.com/suno-udio-ai-music-lawsuits-2026); [AI Vortex tracker](https://www.aivortex.io/legal/ai-case-law/suno-udio-music-ai/)
- **Warner–Suno:** Warner Music Group settled with Suno on November 25, 2025, becoming the first major label to do so. Suno agreed to build new models trained on licensed music and bought Songkick from WMG. — [Wikipedia: Suno](https://en.wikipedia.org/wiki/Suno_(platform)); [Dubspot](https://blog.dubspot.com/suno-udio-ai-music-lawsuits-2026)
- **Suno V6 licensed models:**
  - Launched September 9, 2026 (v6, v6-wild, v6-mini) with WMG, BMG and Believe, and all older models (v4.5, v5, v5.5) were retired.
  - Downloads reportedly now require a paid account and are capped monthly, and free-tier songs cannot be used commercially.
  - Source reliability is low (blogs).
  - [Undetectr](https://undetectr.com/blog/suno-licensed-models-2026); [Tech-Insider](https://tech-insider.org/suno-v6-warner-bmg-licensing-deal-2026/)
- **Still-active litigation (secondary trackers, not checked against court filings):**
  - Talks between Suno and the two holdout majors reportedly broke down in April 2026.
  - On September 18, 2026, UMG and Sony filed a joint complaint against Suno in Boston federal court alleging 60,202 recordings were copied.
  - Sony filed a new suit against Udio on July 20, 2026 over 30,117 recordings.
  - A GEMA (Germany) decision against Suno in Munich is reported but not final.
  - [AI Vortex](https://www.aivortex.io/legal/ai-case-law/suno-udio-music-ai/); [Chartlex tracker](https://www.chartlex.com/blog/business/music-industry-ai-lawsuits-tracker-2026); [Dubspot](https://blog.dubspot.com/suno-udio-ai-music-lawsuits-2026)
- **Suno ownership terms:**
  - The wording changed from paid users "owning" outputs to paid users who "may be granted commercial use rights".
  - Paid-plan rights cover monetisation including sync.
  - Free-tier tracks are non-commercial, with no retroactive license on later subscription.
  - [Music In Africa](https://www.musicinafrica.net/magazine/suno-adjusts-ai-music-ownership-terms-after-warner-music-partnership); [terms.law guide](https://terms.law/ai-output-rights/suno/)
- **US copyright:**
  - The US Copyright Office has held that works generated entirely by AI without meaningful human creative input cannot be registered, and a text prompt alone does not meet the authorship threshold.
  - A platform license is a contract, not copyright protection against third-party similarity claims.
  - One legal guide says Suno's terms provide no user indemnification.
  - [The Conversation](https://theconversation.com/ai-can-make-up-songs-now-but-who-owns-the-copyright-the-answer-is-complicated-229714); [terms.law guide](https://terms.law/ai-output-rights/suno/)

### Inferences
- For a three-year solo 3D character-animation game, AI realistically speeds up props, environment filler, blockouts, reference and concept exploration, base rigs for humanoids, rough mocap passes and code. The parts that define a character-animation game's quality still need human skill:
  - clean, deformation-ready topology on the hero characters;
  - weight painting and fixes at problem joints;
  - the animation itself (timing, weight, appeal, personality);
  - a consistent art style;
  - the game feel.
  This is an inference from tool limitations plus the homogenization findings.
- The AI music landscape changed several times during 2025–26: Udio downloads ended, Suno retired its models, and terms were rewritten. A three-year project cannot assume today's tool or license terms will last. AI music also cannot be copyrighted as such, must be disclosed on Steam, and is the category players dislike most. Learning enough composition to own the soundtrack, or using AI only as a sketch tool, is the lower-risk path. This is an inference.

### Gaps
- No independent, systematic benchmark was found of AI-generated character topology or deformation quality (most 2026 "tests" are vendor or affiliate content).
- No retrieved sources cover UniRig, AccuRIG or Mixamo's 2026 status, or the quality of text-to-motion output for stylized characters.
- The US Copyright Office report itself was not retrieved this session.
- Licensed alternatives (e.g., ElevenLabs music with label deals) were not checked.
- The current exact Suno and Udio license terms need checking against the vendors' own pages at the time of use.

## 6. Synthesis: does the evidence make "deep in one area, good enough elsewhere" more viable, and where does differentiation still need human depth or taste?

### Takeaway
Yes, with conditions. The evidence robustly shows that AI raises the floor on codifiable tasks that sit inside the AI frontier. That makes "good enough elsewhere" much cheaper to reach: novices gain 30–40% in customer support, consulting and coding, and individuals with AI matched cross-functional teams at P&G.

The same evidence shows three limits:
- Turning AI output into good results requires judgment, so AI amplifies the skilled in open-ended work.
- "Good enough" AI output converges across users and floods markets, as on Steam.
- Leaning on AI while learning can stop skills forming.

So the strategy that fits the evidence is "deep judgment and taste in the differentiating core, plus AI-assisted competence at the edges". "Specialists only" fits it less well, because narrow specialists in automatable execution are among those AI hurts most.

### Cited Findings
- **Floor-raising inside the frontier:**
  - Customer support: +34–36% for the lowest-skill quintile vs small speed gains and small quality declines for the top. — [QJE](https://academic.oup.com/qje/article/140/2/889/7990658)
  - Consultants: +43% below vs +17% above baseline average. — [HBS WP](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)
  - Coders: juniors +27–39% vs seniors +8–13%. — [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-affects-highly-skilled-workers)
  - Writing: the productivity distribution compresses. — [Noy & Zhang WP](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf)
- **Breadth across functions:** Individuals with AI matched two-person teams without AI and produced balanced technical and commercial solutions regardless of their own function. — [NBER w33641](https://www.nber.org/papers/w33641)
- **Judgment amplifies gains:**
  - In open-ended entrepreneurship, high performers gained about 15% while low performers lost 8–10%, driven by how advice was selected and implemented. — [Berkeley Haas](https://newsroom.haas.berkeley.edu/research/gen-ai-experiment-shows-mixed-results-in-helping-small-businesses-grow/); [Harvard D^3](https://d3.harvard.edu/?p=30663)
  - High-ability debaters benefited more. — [Esade](https://www.esade.edu/ecpol/en/publications/when-generative-ai-increases-inequality-experimental-evidence-from-a-university-debate-competition/)
  - Workers who "skillfully navigate" the frontier gain, while uncritical use outside it costs 19 points of correctness. — [Org Sci via IDEAS](https://ideas.repec.org/a/inm/ororsc/v37y2026i2p403-423.html)
- **Homogenization:** AI-assisted outputs are more similar to each other in stories, brainstormed ideas and visual art. — [Science Advances](https://www.science.org/doi/10.1126/sciadv.adn5290); [Wharton Mack](https://mackinstitute.wharton.upenn.edu/2025/new-in-nature-chatgpt-decreases-idea-diversity-in-brainstorming/); [PNAS Nexus/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10914360)
- **Steam as the market-level example:** AI-flagged games drive most release growth but convert to reviews and sales at a much lower rate, and players read visible AI as low investment. — [GamesRadar](https://www.gamesradar.com/games/steam-study-of-over-53-000-games-finds-60-90-percent-of-the-growth-in-monthly-releases-on-valves-store-is-from-games-using-ai-and-almost-none-of-them-make-money/); [Bazzaz & Cooper](https://arxiv.org/pdf/2608.11539)
- **Skill formation:** Unguarded AI cut later test performance by about 17% in two RCTs (high-school math; junior engineers learning a library). Tutor-style or conceptual use avoided the loss. — [Penn CHIBE](https://chibe.upenn.edu/publications/generative-ai-without-guardrails-can-harm-learning-evidence-from-high-school-mathematics); [Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)
- **Narrow specialists in automatable crafts:** Freelance writers and image-makers lost jobs and earnings, top-rated ones included, and image-creation postings fell 17%. Surviving work skews complex and better paid. — [WashU Olin](https://olin.washu.edu/about/news-and-media/news/2023/08/study-ai-tools-cause-a-decline-in-freelance-work-and-incomeat-least-in-the-short-run.php); [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420)

### Inferences
- **"People who do many things never go deep":** The studies imply a different reading. AI makes breadth cheap, so breadth is no longer what distinguishes anyone. Depth now matters in a narrower set of places: the judgment and taste needed to direct, select and fix AI output in the parts of the work that define quality.
- **Applied to this game:** a small 3D character-animation game's differentiators are the character animation itself (acting, timing, appeal), a coherent visual style and the game feel. Those deserve real depth. Code, props, environment filler, base rigs and rough mocap are the "good enough" layer where AI does the work.
- **"Today only specialists succeed":** The evidence does not support this as stated. Specialists whose specialty is automatable execution are among the measured losers (Hui et al.; Demirci et al.; Canaries' early-career declines). Gains accrue to people with judgment over AI output (Otis et al.; Roldán-Monés; Dell'Acqua). A solo developer who builds genuine depth in one craft and uses AI with judgment elsewhere is close to the profile the evidence favours. The market's winner-take-all structure on Steam applies regardless of method.
- **Practical guardrails implied by the evidence:**
  1. Use AI as a tutor or explainer while learning the core crafts (3D modeling, animation), not as a substitute for practice (Bastani; Anthropic).
  2. Keep player-visible assets (characters, animation, music) human-led, or treat AI output as a heavily edited base. Disclosure is required, and players penalise visible AI (Valve; Quantic Foundry; Bazzaz & Cooper).
  3. Use AI aggressively for code, which needs no Steam disclosure. Invest enough coding understanding to debug a three-year codebase (Cui juniors' gains vs METR experts' slowdown; Anthropic's debugging gap).
  4. Actively counter homogenization by asking AI for divergent options and curating hard (Meincke et al.).
- **Strength of the evidence:** Most of it comes from short tasks, 2023–2024 models, and writing, consulting and coding. None directly studies solo game developers or 3D animation novices. The "T-shaped" conclusion is therefore an informed extrapolation, not a measured result.

### Gaps
- I found no study testing the "generalist plus AI" vs "specialist" strategy head-to-head in creative production or game development, and no longitudinal study of novices learning 3D or animation with AI tools.
- I found no evidence on whether AI-assisted solo developers ship more successful games, controlling for quality. The Steam data are descriptive, and the Boxleiter revenue estimates are rough.
- Most experiments predate 2025-era agentic tools. METR's 2026 note implies effects are moving quickly, so the 2023–24 effect sizes may not describe late-2026 tools.
