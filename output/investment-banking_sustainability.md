# Investment Banking × Sustainability Playbook

## Overview

Sustainability within investment banking has evolved from a peripheral CSR (Corporate Social Responsibility) function into a core strategic imperative that directly impacts deal origination, client relationships, regulatory compliance, and institutional reputation. The sustainability department — sometimes called ESG Strategy, Responsible Banking, or Sustainable Finance — is responsible for integrating Environmental, Social, and Governance (ESG) considerations across the bank's advisory mandates, underwriting activities, proprietary investments, and operational footprint. In bulge-bracket banks, this team ranges from 15-50+ professionals; in middle-market firms, it may be 3-8 people wearing multiple hats.

The function operates at the intersection of multiple high-stakes domains: regulatory compliance (EU SFDR, CSRD, SEC Climate Disclosure Rules, UK SDR), client advisory (helping corporates structure green bonds, sustainability-linked loans, and transition finance), deal screening (ESG due diligence on M&A targets and IPO candidates), and internal reporting (carbon footprint, DEI metrics, modern slavery statements, TCFD/TNFD disclosures). Investment banks that lead in sustainable finance capture disproportionate deal flow — the green bond market alone exceeded $600B in annual issuance by 2025, and sustainability-linked lending surpassed $1.5T in cumulative volume.

The sustainability team's challenge is fundamentally one of data aggregation, standardization, and reporting across highly fragmented sources. ESG data comes from portfolio companies (often inconsistent and incomplete), third-party rating agencies (MSCI, Sustainalytics, ISS — each with different methodologies), regulatory frameworks (GRI, SASB, ISSB, EU Taxonomy), and internal operational systems (facilities management, HR, procurement). The team must translate this data deluge into actionable insights for deal teams, credible disclosures for regulators, and compelling narratives for clients — all while navigating the reputational minefield of greenwashing accusations. The stakes are existential: regulatory fines for non-compliance are escalating rapidly, and institutional investors increasingly condition mandates on credible ESG commitments.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Sustainability teams are small relative to the massive data aggregation, reporting, and advisory workload. ESG disclosure requirements are multiplying (CSRD alone adds 1,000+ data points) while headcount remains flat. |
| 2 | Consolidate Tech Stack with AI | Medium-High | ESG data lives in 10-20+ disparate sources (rating agencies, portfolio systems, facilities data, HR systems). Centralizing workflow orchestration reduces data reconciliation burden and reporting errors. |
| 3 | Replace or Radically Augment Headcount | Medium | Manual ESG data collection from portfolio companies, regulatory framework mapping, and report generation consume enormous analyst hours that AI can automate or radically accelerate. |

## Prioritized Use Cases

---

### Use Case 1: ESG Disclosure & Regulatory Reporting Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks must now comply with a growing web of ESG disclosure requirements: EU CSRD (Corporate Sustainability Reporting Directive) requiring detailed double materiality assessments and 1,000+ data points across ESRS (European Sustainability Reporting Standards), SEC Climate Disclosure Rules mandating Scope 1/2/3 greenhouse gas emissions reporting, UK SDR (Sustainability Disclosure Requirements), TCFD (Task Force on Climate-related Financial Disclosures), and TNFD (Taskforce on Nature-related Financial Disclosures). Each framework has different reporting boundaries, metrics, timelines, and assurance requirements. A single CSRD report requires data from facilities (energy, waste, water), HR (DEI, pay equity, training hours), procurement (supply chain due diligence), operations (travel, commuting), and business units (financed emissions). The sustainability team spends 60-70% of its annual capacity on compliance reporting, leaving minimal bandwidth for strategic advisory work that actually drives revenue.

#### The Solution
monday.com as the ESG disclosure project management and data collection orchestration platform. **ESG Reporting Board** with columns: Framework (dropdown: CSRD/ESRS, SEC Climate, TCFD, TNFD, GRI, SASB, UK SDR, CDP), Disclosure Topic (text), ESRS Standard (dropdown: E1-Climate, E2-Pollution, E3-Water, E4-Biodiversity, E5-Circular Economy, S1-Own Workforce, S2-Value Chain Workers, S3-Affected Communities, S4-Consumers, G1-Business Conduct), Data Point ID (text), Data Owner (people), Source System (dropdown: Facilities, HR, Finance, Procurement, Business Units, External), Status (status: Not Started → Data Requested → Data Received → Validated → Drafted → Reviewed → Final → Submitted), Due Date (date), Data Value (text), Prior Year Value (text), Variance (numbers %), Assurance Required (checkbox), Auditor Notes (long text). Sub-items for each data point's collection trail. Automations send data requests to owners 90 days before filing deadline, escalate overdue items, and flag material year-over-year variances for review.

#### The Outcome
Reduce ESG report preparation time by 50% through structured data collection workflows. Achieve 100% on-time regulatory filing compliance across all jurisdictions. Eliminate the annual "fire drill" of disclosure season by establishing continuous data collection processes. Provide audit-ready evidence trails for every data point. Free 30-40% of sustainability team capacity from reporting mechanics to strategic advisory work.

#### Discovery Questions
1. "How many distinct ESG disclosure frameworks are you currently reporting against, and do you manage them as separate projects or try to consolidate overlapping requirements?"
2. "What's your biggest bottleneck in the reporting cycle — is it getting data from internal departments, validating the numbers, or drafting the narrative?"
3. "How do you handle the overlap between CSRD, TCFD, and GRI — are you mapping data points across frameworks or collecting separately for each?"
4. "What's your current process for getting Scope 3 financed emissions data from portfolio companies and deal teams? How complete is that data?"
5. "Have you had to restate any ESG disclosures due to data quality issues? What was the reputational impact?"

#### Industry Context
The CSRD represents a seismic shift for investment banks with EU operations — requiring detailed double materiality assessments (financial materiality AND impact materiality) across environmental, social, and governance topics. For banks, "financed emissions" (Scope 3, Category 15) is the most challenging metric — it requires estimating the GHG emissions attributable to the bank's lending and investment portfolio. The Partnership for Carbon Accounting Financials (PCAF) standard provides methodology, but data gaps are enormous. The EU Taxonomy Regulation adds another layer — banks must disclose the proportion of their lending/investment activities aligned with taxonomy-eligible and taxonomy-aligned activities. Greenwashing enforcement is intensifying: the SEC, FCA, and ESMA have all brought enforcement actions related to misleading ESG disclosures.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an ESG Disclosure & Regulatory Reporting board for an investment bank. Columns: Framework (dropdown: CSRD-ESRS, SEC Climate Disclosure, TCFD, TNFD, GRI, SASB-ISSB, UK SDR, CDP), ESRS Topic (dropdown: E1 Climate Change, E2 Pollution, E3 Water & Marine, E4 Biodiversity, E5 Circular Economy, S1 Own Workforce, S2 Value Chain Workers, S3 Communities, S4 Consumers, G1 Business Conduct, Cross-Cutting), Data Point ID (text), Data Point Description (text), Metric Type (dropdown: Quantitative, Qualitative, Narrative, Target, Policy), Data Owner (people), Source Department (dropdown: Facilities, HR, Finance, Procurement, Legal, Business Units, Risk, Treasury), Status (status: Not Started, Data Requested, Data Received, Quality Check, Validated, Draft Narrative, Under Review, Approved, Filed), Due Date (date), Reporting Period (dropdown: FY 2025, H1 2026, FY 2026), Current Value (text), Prior Period Value (text), YoY Change Percent (numbers), Assurance Level (dropdown: Reasonable, Limited, None), Evidence File (file), Reviewer Notes (long text). Groups: Environmental Metrics, Social Metrics, Governance Metrics, Cross-Cutting Standards. Automations: When Status is Not Started and Due Date is 90 days away, notify Data Owner. When Data Received, auto-assign to Quality Check and notify reviewer. When YoY Change Percent exceeds 20 or is below negative 20, flag for management review. Views: Dashboard with completion percentage by framework (battery widgets), data points by status (pie chart), overdue items count, timeline view of filing deadlines, chart showing completion trend over time."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Disclosure Orchestrator
**Agent Purpose:** Automate ESG data collection workflows, cross-map disclosure requirements across frameworks, and ensure timely, accurate regulatory filings.

**Triggers:**
- Reporting cycle kickoff date (configurable per framework)
- Data point Status changes to "Data Received" (trigger quality check)
- Filing deadline within 30 days with incomplete data points
- New regulatory framework requirement published (manual trigger)
- Quarterly progress review schedule

**Actions:**
- Map data points across overlapping frameworks (e.g., CSRD E1 → TCFD Metrics & Targets → CDP Climate → SEC Scope 1/2) to eliminate duplicate collection
- Generate personalized data collection requests to department owners with specific metrics, formats, and deadlines
- Validate received data against prior period values, industry benchmarks, and logical consistency checks (flag anomalies)
- Draft narrative disclosures based on quantitative data and prior year language, adapted for each framework's requirements
- Generate progress reports showing completion rate by framework, overdue items, and projected filing timeline
- Maintain framework mapping matrix that auto-updates when regulatory requirements change

**Data Required:**
- ESG reporting framework requirements databases (ESRS, SEC rules, TCFD recommendations)
- Historical disclosure data (3+ years for trend analysis)
- Internal data source connections (facilities management, HRIS, finance ERP, procurement system)
- Industry benchmark data (peer bank ESG disclosures)
- Regulatory update feeds (EU Official Journal, SEC releases, FCA updates)

**Autonomy Level:** Human-in-the-Loop
Data collection request generation and distribution are automated. Data validation and anomaly flagging are automated. Narrative drafts are auto-generated but require sustainability analyst review and editing. Final filing approval requires Head of Sustainability sign-off. Framework mapping updates are automated but require periodic human validation.

**Example Interaction:**
> It's September 1st and the ESG Disclosure Orchestrator kicks off the FY 2025 CSRD reporting cycle — the bank's first mandatory filing under the directive. The agent identifies 847 discrete data points required across 12 ESRS topics. It maps 312 of these (37%) to data already collected for TCFD and GRI disclosures, automatically pre-populating those fields. For the remaining 535 data points, it generates 23 personalized data collection packages: Facilities receives requests for energy consumption by building (kWh), water withdrawal by source, and waste by type; HR receives requests for headcount by gender/age/disability, pay gap ratios, and training hours per employee; Treasury receives requests for green bond issuance volume and taxonomy-aligned lending percentages. Each request includes the specific ESRS reference, format template, prior year comparators (where available), and a 60-day collection deadline. The sustainability team's Sarah Johnson receives a dashboard showing the full reporting timeline, critical path items, and an estimated 85% completion probability by the December 31 filing deadline.

---

### Use Case 2: Sustainable Finance Deal Pipeline & Advisory Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks are aggressively building sustainable finance practices — green bonds, sustainability-linked bonds (SLBs), social bonds, transition bonds, sustainability-linked loans (SLLs), and ESG-integrated M&A advisory. The sustainability team provides critical input on deal structuring (KPI selection for SLBs, use-of-proceeds frameworks for green bonds, ESG due diligence for M&A). However, they lack visibility into the full deal pipeline, often learning about sustainability-relevant opportunities too late to influence deal structure. Deal teams don't always recognize when a transaction has sustainability angles. The result: missed revenue opportunities (sustainability structuring fees, green bond second-party opinion coordination), suboptimal deal structures (KPIs that don't withstand market scrutiny), and reputational risk (deals that attract greenwashing allegations). The global sustainable debt market represents $4T+ in cumulative issuance — banks without credible sustainable finance capabilities lose mandates to competitors.

#### The Solution
monday.com CRM and Work Management as the sustainable finance pipeline and advisory platform. **Sustainable Finance Pipeline Board** with columns: Deal Name (text), Client (text), Deal Type (dropdown: Green Bond, SLB, Social Bond, Transition Bond, SLL, ESG M&A Advisory, Carbon Credit, Blended Finance), Deal Size (numbers, USD millions), Sustainability Team Involvement (dropdown: Lead Structuring, Advisory Support, Due Diligence, Second-Party Opinion Coordination, Not Yet Engaged), Status (status: Identified → Qualification → Structuring → Execution → Closed → Post-Issuance), Banker Lead (people), Sustainability Lead (people), Framework (dropdown: ICMA GBP, ICMA SBP, ICMA SLB Principles, LMA SLLP, EU Taxonomy Aligned, Transition Finance), KPIs Selected (long text), SPO Provider (dropdown: Sustainalytics, ISS, Cicero, Vigeo Eiris, S&P), Revenue Potential (numbers), Close Date (date). Dashboard shows pipeline by deal type, projected sustainable finance revenue, team capacity allocation, and deals at risk of greenwashing flags.

#### The Outcome
Increase sustainable finance deal identification by 40% through systematic pipeline visibility. Capture $5-15M in incremental annual revenue from sustainability structuring and advisory fees. Reduce deal structuring cycle time by 30% through templated frameworks and KPI libraries. Eliminate reputational risk from poorly structured sustainable finance deals. Provide leadership with real-time sustainable finance revenue attribution and market share metrics.

#### Discovery Questions
1. "How does your sustainability team currently learn about deals in the pipeline that have ESG or sustainable finance angles? Is it systematic or ad hoc?"
2. "What percentage of your bank's debt capital markets deals have a sustainability component (green, social, sustainability-linked)? How does that compare to competitors?"
3. "When a deal team is structuring a sustainability-linked bond, what's the process for selecting KPIs and engaging a second-party opinion provider? Who owns that?"
4. "Have you ever had a deal attract greenwashing criticism or fail to achieve a credible sustainability label? What happened?"
5. "Can you quantify the revenue your sustainability team directly influences — structuring fees, advisory premiums, mandate wins attributed to ESG capability?"

#### Industry Context
Sustainable finance is the fastest-growing revenue segment in investment banking. ICMA (International Capital Market Association) principles govern green bond and SLB structuring — compliance with these principles is market standard and failure to adhere damages issuer and arranger reputation. KPI selection for SLBs is particularly contentious: regulators and investors scrutinize whether KPIs are material, ambitious, and measurable. The EU Green Bond Standard (EU GBS) introduces mandatory taxonomy alignment and external review requirements. Second-party opinions (SPOs) from providers like Sustainalytics and ISS are quasi-mandatory for market credibility. Banks compete aggressively on league table rankings for sustainable finance — these rankings directly influence mandate awards from ESG-focused issuers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Sustainable Finance Deal Pipeline board for an investment bank. Columns: Deal Name (text), Client Name (text), Sector (dropdown: Energy, Utilities, Real Estate, Transportation, Manufacturing, Financial Institutions, Sovereign/SSA, TMT, Healthcare, Consumer), Deal Type (dropdown: Green Bond, Sustainability-Linked Bond, Social Bond, Transition Bond, Green Loan, Sustainability-Linked Loan, ESG M&A Advisory, Carbon Credit Structuring, Blended Finance, Impact Fund), Deal Size USD Millions (numbers), Bank Role (dropdown: Bookrunner, Co-Manager, Structuring Advisor, ESG Advisor, Sole Arranger), Sustainability Involvement (status: Not Engaged, Identified, Qualification, Active Advisory, Structuring Lead, Monitoring), Banker Lead (people), Sustainability Advisor (people), Framework Applied (dropdown: ICMA Green Bond Principles, ICMA SLB Principles, ICMA Social Bond Principles, LMA Green Loan Principles, LMA SLL Principles, EU Green Bond Standard, EU Taxonomy, Custom), KPIs or Use of Proceeds (long text), SPO Provider (dropdown: Sustainalytics, ISS ESG, CICERO, Vigeo Eiris, S&P Global, DNV, None Yet), SPO Status (status: Not Needed, To Be Engaged, In Progress, Received, Published), Revenue Estimate (numbers), Probability (dropdown: 25%, 50%, 75%, 90%, Closed), Target Close Date (date), Greenwashing Risk Flag (dropdown: Low, Medium, High), Notes (long text). Groups: Active Pipeline, Structuring Phase, Closed Won, Closed Lost, Monitoring Post-Issuance. Automations: When Deal Type is SLB and KPIs field is empty for 7 days, notify Sustainability Advisor. When Greenwashing Risk Flag is High, notify Head of Sustainability. When Sustainability Involvement changes to Active Advisory, create sub-items checklist: Framework Selection, KPI Identification, SPO Engagement, Impact Reporting Setup. Views: Dashboard with pipeline value by deal type (bar chart), deals by status (funnel chart), revenue forecast (weighted pipeline), deals by sector (pie chart), timeline of expected closings."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Sustainable Finance Deal Scout
**Agent Purpose:** Identify sustainability angles in the bank's deal pipeline, recommend frameworks and KPIs, and monitor post-issuance compliance.

**Triggers:**
- New deal created in the bank's main deal pipeline board (cross-board automation)
- Deal Type contains sustainability-related keywords
- Client's industry flagged as high sustainability relevance (Energy, Utilities, Real Estate, Transport)
- SLB KPI review dates approaching (annual measurement)
- League table reporting deadline approaching

**Actions:**
- Screen new deals for sustainability structuring potential based on client sector, deal type, and comparable transactions
- Recommend applicable frameworks (ICMA GBP vs. SLB Principles vs. EU GBS) based on deal characteristics
- Generate KPI shortlists for SLBs based on sector materiality analysis and market precedent
- Monitor post-issuance KPI performance against targets and flag potential covenant breaches
- Compile league table submission data (deal counts, volumes, roles) for sustainable finance rankings
- Assess greenwashing risk based on KPI ambition, framework alignment, and sector controversies

**Data Required:**
- Bank's full deal pipeline (all divisions: DCM, ECM, M&A, Leveraged Finance)
- Sustainable finance market databases (Bloomberg NEF, Climate Bonds Initiative)
- ICMA, LMA framework documentation
- Historical SPO reports and KPI benchmarks by sector
- Client ESG ratings and controversy scores
- League table databases (Bloomberg, Refinitiv, Dealogic)

**Autonomy Level:** Human-in-the-Loop
Deal screening and sustainability angle identification are automated. Framework and KPI recommendations are generated but require sustainability advisor validation. Greenwashing risk flags are autonomous alerts. Post-issuance monitoring runs automatically with breach alerts requiring human review. League table submissions are compiled but require team lead approval.

**Example Interaction:**
> The Sustainable Finance Deal Scout detects a new $750M bond issuance in the DCM pipeline for NorthGrid Energy, a European utility transitioning from natural gas to renewables. The deal team hasn't engaged sustainability. The agent flags the opportunity: "NorthGrid Energy — high sustainability structuring potential. Recommendation: Green Bond under ICMA GBP with EU Taxonomy alignment for renewable energy capex (NACE code D35.11). Alternative: Sustainability-Linked Bond if NorthGrid prefers general corporate purposes — recommended KPIs: (1) Scope 1+2 GHG intensity reduction aligned with SBTi 1.5°C pathway, (2) Renewable generation capacity as % of total, (3) Methane leak rate reduction. Estimated structuring premium: 15-20bps greenium based on comparable utility green bonds. SPO recommendation: CICERO (strong utility sector coverage). Greenwashing risk: Medium — NorthGrid still has 40% gas generation; transition narrative must be credible." The sustainability advisor reviews the recommendation, confirms the green bond approach, and engages the deal team — a process that previously might have been missed entirely or discovered 3 weeks into structuring.

---

### Use Case 3: Financed Emissions Calculation & Portfolio Carbon Tracking

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The most complex and resource-intensive sustainability metric for investment banks is "financed emissions" — the greenhouse gas emissions attributable to the bank's lending and investment portfolio. Under PCAF (Partnership for Carbon Accounting Financials) methodology, banks must calculate their share of portfolio company emissions proportional to their outstanding exposure. For a bank with 5,000+ corporate clients across lending, underwriting, and investment portfolios, this requires: (1) collecting or estimating emissions data for each counterparty, (2) applying attribution factors based on exposure type and enterprise value, (3) aggregating across portfolios, (4) trending year-over-year to demonstrate portfolio decarbonization. Data quality varies enormously — Tier 1 reported data is available for maybe 20% of counterparties; the rest requires estimation models. A team of 3-5 analysts spends 4-6 months annually on this calculation, producing results that are stale by the time they're published and riddled with estimation uncertainty.

#### The Solution
monday.com as the financed emissions data collection and calculation orchestration platform. **Portfolio Carbon Tracking Board** with columns: Client Name (text), Sector (dropdown: aligned to PCAF asset classes), Outstanding Exposure (numbers, USD millions), Exposure Type (dropdown: Corporate Loans, Listed Equity, Bonds, Project Finance, Commercial Real Estate, Mortgages), Scope 1 Emissions (numbers, tCO2e), Scope 2 Emissions (numbers, tCO2e), Scope 3 Emissions (numbers, tCO2e), Data Quality Score (dropdown: PCAF 1-5, where 1=reported verified, 5=estimated), EVIC (numbers, Enterprise Value Including Cash), Attribution Factor (numbers %), Attributed Emissions (numbers, tCO2e), SBTi Alignment (dropdown: Committed, 1.5°C, Well-Below 2°C, No Target), Year (dropdown), Data Source (dropdown: CDP, Annual Report, Estimated-Sector Avg, Estimated-Revenue Based). Sub-items for historical year-over-year data. Dashboard shows total financed emissions by sector, data quality distribution, portfolio carbon intensity trends, and top 20 emitters.

#### The Outcome
Reduce annual financed emissions calculation cycle from 4-6 months to 6-8 weeks through structured collection and automated attribution. Improve data quality score from average PCAF 4.2 to 3.0 within 2 years through systematic engagement with high-emission clients. Provide quarterly (not just annual) portfolio carbon snapshots for internal decision-making. Enable deal-level carbon impact assessment at point of origination. Support NZBA (Net-Zero Banking Alliance) target-setting with reliable baseline data.

#### Discovery Questions
1. "Where are you in your financed emissions calculation journey — have you published PCAF-aligned numbers, or are you still building the methodology?"
2. "What percentage of your portfolio's emissions are based on reported data versus sector-average estimates? What's your PCAF data quality score?"
3. "How do you currently handle the data collection from portfolio companies — is it automated from CDP or manual outreach?"
4. "Can your deal teams see the carbon impact of a new transaction at the point of credit decision? Or is that information only available annually?"
5. "Have you set Net-Zero Banking Alliance targets? How confident are you in the baseline data those targets are built on?"

#### Industry Context
Financed emissions represent 99%+ of a bank's total carbon footprint — dwarfing operational emissions by orders of magnitude. PCAF has become the de facto standard, with 500+ financial institutions signed up. The methodology covers 7 asset classes with different attribution approaches. Data quality is the critical challenge: only large public companies reliably report emissions; SME and private company emissions must be estimated using revenue-based or sector-average proxies. The Net-Zero Banking Alliance (NZBA) requires members to set intermediate (2030) and long-term (2050) sector-level decarbonization targets — which requires granular portfolio carbon data. Regulatory pressure is mounting: the ECB expects Pillar 3 ESG disclosures, and the SEC's climate rules mandate Scope 3 reporting for large accelerated filers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Financed Emissions Portfolio Tracking board for an investment bank. Columns: Client Name (text), Client ID (text), GICS Sector (dropdown: Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Health Care, Financials, Information Technology, Communication Services, Utilities, Real Estate), PCAF Asset Class (dropdown: Listed Equity & Corporate Bonds, Business Loans & Unlisted Equity, Project Finance, Commercial Real Estate, Mortgages, Motor Vehicle Loans, Sovereign Debt), Outstanding Exposure USD M (numbers), Scope 1 tCO2e (numbers), Scope 2 tCO2e (numbers), Scope 3 tCO2e (numbers), Data Quality Score (dropdown: Score 1 Reported Verified, Score 2 Reported Unverified, Score 3 Estimated Physical Activity, Score 4 Estimated Revenue, Score 5 Estimated Sector Average), Data Source (dropdown: CDP Response, Annual Report/Sustainability Report, Estimated PCAF Database, Estimated Revenue Proxy, Direct Client Engagement), EVIC USD M (numbers), Attribution Factor Percent (numbers), Attributed Emissions tCO2e (numbers), Carbon Intensity tCO2e per M USD (numbers), SBTi Status (dropdown: No Target, Committed, 1.5C Aligned, Well Below 2C, 2C Aligned, Business Ambition), Engagement Priority (dropdown: Top 20 Emitter, High Priority, Standard, Low Exposure), Year (dropdown: 2023, 2024, 2025), Notes (long text). Groups by sector: Energy Sector, Utilities, Industrials, Materials, Other Sectors. Automations: When Data Quality Score is 4 or 5 and Outstanding Exposure exceeds 50M, flag Engagement Priority as High Priority. When Attributed Emissions changes, recalculate Carbon Intensity. Views: Dashboard with total financed emissions by sector (stacked bar chart), data quality distribution (pie chart), top 20 clients by attributed emissions (table), year-over-year emissions trend (line chart), portfolio carbon intensity trend (line chart), SBTi alignment percentage (battery widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Carbon Portfolio Analyst
**Agent Purpose:** Automate financed emissions data collection, PCAF-aligned calculations, and portfolio decarbonization tracking.

**Triggers:**
- Annual calculation cycle kickoff (configurable date)
- New client emissions data published (CDP release, annual report publication)
- Significant exposure change for Top 20 emitters (threshold-based)
- New deal added to pipeline for high-carbon sector client
- Quarterly portfolio snapshot schedule

**Actions:**
- Scrape CDP responses and sustainability reports for updated emissions data and auto-populate client records
- Apply PCAF attribution methodology to calculate attributed emissions based on exposure type and EVIC
- Identify data quality improvement opportunities (clients with Score 4-5 that could provide reported data)
- Generate client engagement letters requesting direct emissions disclosure
- Calculate deal-level carbon impact for new transactions in pipeline (incremental financed emissions)
- Produce NZBA target tracking dashboard comparing actual portfolio trajectory against committed decarbonization pathway

**Data Required:**
- Client exposure data from credit risk/loan management systems
- CDP climate change responses
- PCAF emissions factor database
- Company financial data (EVIC, revenue) from Bloomberg/Refinitiv
- SBTi target validation database
- NZBA sector decarbonization pathways

**Autonomy Level:** Human-in-the-Loop
Data collection and attribution calculations are automated. Emission estimates using sector averages are automated but flagged for review. Client engagement outreach requires sustainability team approval. NZBA target progress reports are auto-generated but require Head of Sustainability review before external submission.

**Example Interaction:**
> The Carbon Portfolio Analyst begins the FY 2025 financed emissions calculation. It pulls the bank's $187B lending portfolio — 4,847 corporate clients. Step 1: Cross-references client list against CDP 2025 responses — matches found for 612 clients (Scope 1+2 reported). Step 2: Scrapes published sustainability reports for 428 additional clients, extracting emissions data with confidence scoring. Step 3: For remaining 3,807 clients, applies PCAF revenue-based estimation using sector emission factors. The portfolio weighted average data quality score: 3.8 (up from 4.2 last year). Total financed emissions: 47.3M tCO2e, down 8% from FY 2024. The agent flags that 72% of total financed emissions come from just 47 clients (top 1%) — and 12 of those have no science-based targets. It generates a prioritized engagement plan: "Recommend direct engagement with these 12 clients representing 34M tCO2e in financed emissions and $28B in exposure. Template engagement letters drafted for sustainability team review." The Head of Sustainability receives a complete calculation package 6 weeks into the cycle — versus the 5-month timeline of previous years.

---

### Use Case 4: ESG Due Diligence for M&A and IPO Transactions

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every M&A advisory mandate and IPO underwriting engagement now requires ESG due diligence — assessing the target company's environmental liabilities (contaminated sites, carbon exposure, water stress), social risks (labor practices, supply chain human rights, community impact), and governance quality (board diversity, executive compensation, anti-corruption controls). Institutional investors demand ESG disclosures in offering memoranda and prospectuses. Buyers increasingly require ESG reps and warranties in M&A purchase agreements. Yet ESG due diligence is often an afterthought — conducted in the final weeks before deal close by overloaded sustainability analysts working from fragmented data sources (public filings, news searches, ESG rating reports, site assessments). The result: rushed analysis, missed material risks, and post-close surprises that erode deal value. A single missed environmental liability (e.g., PFAS contamination) can destroy hundreds of millions in deal value.

#### The Solution
monday.com as the ESG due diligence workflow management platform. **ESG Due Diligence Board** with columns: Deal Code Name (text), Target Company (text), Deal Type (dropdown: M&A Buy-Side, M&A Sell-Side, IPO, SPAC, LBO, Recap), Sector (dropdown), Deal Value (numbers, USD millions), ESG Analyst (people), Deal Team Lead (people), Status (status: Scoping → Data Collection → Analysis → Draft Report → Review → Final → Delivered), Priority (dropdown: Critical/High/Standard), Environmental Risk Score (numbers 1-10), Social Risk Score (numbers 1-10), Governance Risk Score (numbers 1-10), Overall ESG Risk Rating (dropdown: Low/Medium/High/Critical), Key Findings (long text), Due Date (date). Sub-items as standardized due diligence checklist: Environmental (climate risk, pollution liabilities, biodiversity, resource dependency), Social (workforce, supply chain, community, product safety), Governance (board, ethics, lobbying, tax). Templates for each deal type pre-populate relevant checklist items.

#### The Outcome
Reduce ESG due diligence cycle time from 4-6 weeks to 2-3 weeks through templated checklists and parallel workstreams. Ensure zero deals close without ESG assessment (currently 15-20% of deals skip or minimally address ESG). Identify material ESG risks earlier in deal process, enabling price/structure adjustments. Build institutional knowledge base of sector-specific ESG risks from completed deals. Reduce post-close ESG surprises by 80%.

#### Discovery Questions
1. "At what stage of a deal does ESG due diligence typically begin — is it early enough to influence deal structure and pricing, or is it often last-minute?"
2. "Have you experienced situations where an ESG issue was discovered post-close that should have been caught in due diligence? What was the impact?"
3. "How standardized is your ESG due diligence process — do you use consistent frameworks and checklists, or does it vary by deal team?"
4. "How do you handle sector-specific ESG risks — is your team deep enough to know the material issues for mining versus healthcare versus tech?"
5. "Do buyers/investors ever push back on the quality or depth of your ESG disclosures in deal documents? What do they want that you're not providing?"

#### Industry Context
ESG due diligence has moved from "nice to have" to "deal-critical" in investment banking. PE firms now routinely conduct ESG due diligence alongside financial, legal, and commercial workstreams. The EU's Corporate Sustainability Due Diligence Directive (CSDDD) will make human rights and environmental due diligence legally mandatory for large companies — including assessing M&A targets. SASB (now part of ISSB) materiality maps identify sector-specific ESG issues that are financially material. Environmental liability assessment is particularly high-stakes: CERCLA (Superfund) liability follows the property, and emerging contaminants like PFAS have created multi-billion-dollar liabilities. The International Valuation Standards Council increasingly recognizes ESG as a factor in business valuation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an ESG Due Diligence Management board for investment banking deal teams. Columns: Deal Code Name (text), Target Company (text), Deal Type (dropdown: M&A Buy-Side, M&A Sell-Side, IPO, SPAC Merger, LBO, Secondary Sale, Restructuring), Target Sector (dropdown: Energy, Mining, Manufacturing, Real Estate, Technology, Healthcare, Financial Services, Consumer, Agriculture, Transportation), Deal Value USD M (numbers), ESG Lead Analyst (people), Deal Team Lead (people), Status (status: Scoping, Data Collection, Analysis, Draft Report, Internal Review, Client Review, Final, Delivered), Priority (dropdown: Critical, High, Standard), Environmental Risk Score (numbers 1-10), Social Risk Score (numbers 1-10), Governance Risk Score (numbers 1-10), Overall ESG Rating (dropdown: Low Risk, Medium Risk, High Risk, Critical Risk, Insufficient Data), Material Findings Count (numbers), Red Flags (long text), Recommendations (long text), Report Due Date (date), Delivered Date (date). Sub-items as due diligence checklist with Category (dropdown: Environmental, Social, Governance), Check Item (text), Status (status: Not Applicable, Not Started, In Progress, Complete, Flag Raised), Risk Level (dropdown: None, Low, Medium, High, Critical), Finding Notes (long text), Evidence (file). Groups: Active Due Diligence, Completed This Quarter, Templates. Template sub-items for Environmental: Climate transition risk, Physical climate risk, GHG emissions profile, Environmental permits and violations, Contaminated land/PFAS, Water stress, Biodiversity impact, Waste management, Circular economy. Social: Workforce composition and DEI, Labor relations and union status, Supply chain human rights, Health and safety record, Community relations, Product safety, Data privacy. Governance: Board composition and independence, Executive compensation, Anti-corruption program, Political lobbying, Tax transparency, Cybersecurity governance, Shareholder rights. Automations: When Status changes to Scoping, create all template sub-items. When any sub-item Risk Level is Critical, notify Deal Team Lead and ESG Lead. When Report Due Date is 5 days away and Status is not Final, escalate to ESG Lead. Views: Dashboard with active deals count, deals by ESG rating (pie chart), average risk scores by sector (bar chart), overdue reports count, timeline of due dates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Due Diligence Accelerator
**Agent Purpose:** Automate preliminary ESG risk screening, populate due diligence checklists with sector-specific intelligence, and generate draft risk reports.

**Triggers:**
- New deal item created on ESG Due Diligence board
- Target company name populated (trigger screening)
- Sub-item status changed to "Flag Raised"
- Status changed to "Analysis" (trigger draft report generation)
- Completed deal archived (trigger knowledge base update)

**Actions:**
- Conduct automated ESG screening of target company: aggregate ESG ratings (MSCI, Sustainalytics), controversy history, regulatory violations, environmental permits, litigation history, and news sentiment
- Pre-populate sector-specific due diligence checklist items based on SASB materiality map for target's industry
- Generate preliminary risk scores based on screening data, with confidence levels
- Draft ESG due diligence report narrative incorporating screening findings, sector benchmarks, and identified risk areas
- Flag critical risks for immediate deal team attention (e.g., active environmental litigation, sanctions exposure, modern slavery indicators)
- After deal completion, extract learnings into sector-specific risk knowledge base for future due diligence

**Data Required:**
- ESG rating agency data (MSCI, Sustainalytics, ISS)
- Regulatory violation databases (EPA Enforcement, OSHA, SEC EDGAR)
- News and controversy monitoring feeds
- SASB materiality maps by industry
- Prior ESG due diligence reports (internal knowledge base)
- Public filings (10-K, proxy statements, sustainability reports)

**Autonomy Level:** Human-in-the-Loop
Automated screening and preliminary scoring run autonomously. Checklist pre-population is automatic. Draft report generation is automated but clearly marked as "AI Draft — Analyst Review Required." Critical risk flags are autonomous alerts. Final report approval requires ESG Lead sign-off. Knowledge base updates are automated with quarterly human curation.

**Example Interaction:**
> A new M&A buy-side mandate is created: Project Titan, a $2.1B acquisition of ClearWater Industrial, a specialty chemicals manufacturer. The ESG Due Diligence Accelerator immediately screens ClearWater: MSCI ESG rating BB (laggard for chemicals sector), Sustainalytics High Risk (32.5), two EPA consent decrees in the past 5 years (Clean Air Act violations), a pending community lawsuit regarding wastewater discharge in Ohio, and no published sustainability report. The agent pre-populates 34 sector-specific checklist items (chemicals sector SASB materiality: GHG emissions, air quality, energy management, water management, hazardous waste, community relations, workforce health & safety, product design for use-phase efficiency). Environmental Risk Score set at 8/10 (high), Social at 6/10 (medium-high), Governance at 5/10 (medium). Three items auto-flagged as "Critical": EPA consent decrees, pending litigation, and absence of PFAS disclosure. The agent notifies ESG Lead and Deal Team Lead: "ALERT: Project Titan target ClearWater Industrial has significant environmental risk indicators requiring deep-dive assessment. Recommend environmental liability insurance evaluation and PFAS-specific site assessment as deal conditions." The deal team receives actionable intelligence within 2 hours of deal creation — before the first management presentation.

---

### Use Case 5: EU Taxonomy Alignment Assessment & Reporting

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The EU Taxonomy Regulation requires financial institutions to disclose the proportion of their lending, investment, and underwriting activities that are "taxonomy-eligible" and "taxonomy-aligned" with EU environmental objectives (climate mitigation, climate adaptation, water, circular economy, pollution, biodiversity). For an investment bank, this means classifying every corporate exposure by NACE economic activity code, assessing whether each activity meets Technical Screening Criteria (TSC), verifying "Do No Significant Harm" (DNSH) compliance, and confirming Minimum Social Safeguards. With thousands of counterparties across diverse sectors, this classification exercise is extraordinarily labor-intensive. Most banks have 1-3 analysts manually classifying exposures using spreadsheets, producing results with inconsistent methodology and limited auditability. The Taxonomy is still evolving (delegated acts for remaining environmental objectives are being finalized), adding regulatory uncertainty to an already complex process.

#### The Solution
monday.com as the EU Taxonomy classification and reporting workflow platform. **Taxonomy Assessment Board** with columns: Client Name (text), NACE Code (text), Economic Activity (text), Eligible (dropdown: Eligible/Not Eligible/Under Review), Environmental Objective (dropdown: Climate Mitigation, Climate Adaptation, Water, Circular Economy, Pollution, Biodiversity), TSC Met (status: Met/Not Met/Partial/Data Gap), DNSH Assessment (status: Passed/Failed/Data Gap per objective), Minimum Safeguards (status: Met/Not Met/Under Review), Alignment Status (status: Aligned/Eligible Not Aligned/Not Eligible), Exposure Amount (numbers), Analyst (people), Data Quality (dropdown: High/Medium/Low), Evidence (file), Review Date (date). Sub-items for each DNSH objective assessment. Dashboard shows portfolio taxonomy alignment KAR (Key Asset Ratio), eligibility by sector, data gap analysis, and year-over-year progression.

#### The Outcome
Increase taxonomy assessment throughput by 4x through templated NACE-to-TSC mapping workflows. Improve data quality and consistency by standardizing the classification methodology. Reduce taxonomy reporting preparation from 3 months to 6 weeks. Build an institutional taxonomy classification database that becomes more efficient each year. Provide real-time taxonomy alignment metrics for client-facing sustainable finance discussions.

#### Discovery Questions
1. "How are you currently classifying your portfolio for EU Taxonomy reporting — is it a centralized process or distributed across business lines?"
2. "What's your current taxonomy eligibility and alignment ratio? How confident are you in those numbers?"
3. "Where are the biggest data gaps in your taxonomy assessment — is it the TSC assessment, DNSH compliance, or Minimum Safeguards?"
4. "How do you handle the taxonomy classification for multi-activity companies — do you break down by revenue segment?"
5. "Are your deal teams using taxonomy alignment as a selling point for sustainable finance transactions? Can they access classification data easily?"

#### Industry Context
The EU Taxonomy is the most granular sustainability classification system ever imposed on financial institutions. The Green Asset Ratio (GAR) — the proportion of taxonomy-aligned assets to total covered assets — is a key metric that investors, regulators, and competitors compare. Banks with low GAR face questions about their transition commitment. The Technical Screening Criteria are highly specific and technical (e.g., for electricity generation: lifecycle GHG emissions below 100g CO2e/kWh; for buildings: primary energy demand at least 10% below NZEB threshold). DNSH assessment requires checking each activity against ALL other environmental objectives — a matrix that multiplies complexity. The Minimum Social Safeguards requirement (aligned with OECD Guidelines, UN Guiding Principles on Business and Human Rights) adds a social due diligence layer.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an EU Taxonomy Alignment Assessment board for a bank's lending portfolio. Columns: Client Name (text), Client Sector (dropdown: Energy, Construction, Manufacturing, Transportation, Forestry, Water Supply, ICT, Financial, Professional Services), NACE Code (text), Economic Activity Description (text), Exposure Amount EUR M (numbers), Taxonomy Eligibility (dropdown: Eligible, Not Eligible, Under Review, Partial - Multi Activity), Primary Environmental Objective (dropdown: Climate Change Mitigation, Climate Change Adaptation, Sustainable Use of Water, Transition to Circular Economy, Pollution Prevention, Biodiversity Protection), TSC Assessment (status: Criteria Met, Criteria Not Met, Data Insufficient, Not Assessed), DNSH Climate Mitigation (status: Pass, Fail, N/A, Data Gap), DNSH Climate Adaptation (status: Pass, Fail, N/A, Data Gap), DNSH Water (status: Pass, Fail, N/A, Data Gap), DNSH Circular Economy (status: Pass, Fail, N/A, Data Gap), DNSH Pollution (status: Pass, Fail, N/A, Data Gap), DNSH Biodiversity (status: Pass, Fail, N/A, Data Gap), Minimum Safeguards (status: Met, Not Met, Under Review), Final Alignment (dropdown: Taxonomy Aligned, Eligible Not Aligned, Not Eligible), Analyst (people), Reviewer (people), Assessment Date (date), Evidence Package (file), Notes (long text). Groups: Aligned, Eligible Not Yet Aligned, Not Eligible, Under Assessment. Automations: When TSC Assessment is Criteria Met and all DNSH statuses are Pass and Minimum Safeguards is Met, set Final Alignment to Taxonomy Aligned. When any DNSH status is Data Gap, flag for analyst follow-up. Views: Dashboard with GAR percentage (battery widget), alignment by sector (stacked bar), eligibility vs alignment gap (funnel), data gap count, exposure by alignment status (pie chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Taxonomy Classification Engine
**Agent Purpose:** Automate EU Taxonomy eligibility screening, map NACE activities to Technical Screening Criteria, and orchestrate DNSH assessment workflows.

**Triggers:**
- New client added to portfolio with exposure data
- Annual taxonomy reassessment cycle kickoff
- EU Taxonomy delegated act updates published (regulatory change)
- Client's reported emissions or activity data updated
- Quarterly taxonomy KPI refresh

**Actions:**
- Auto-classify client economic activities to NACE codes based on company description and revenue breakdown
- Map NACE codes to relevant Taxonomy TSC and pre-populate assessment criteria
- Screen publicly available data (sustainability reports, CDP responses) against TSC thresholds
- Generate DNSH assessment checklists specific to each activity's environmental objective
- Calculate portfolio-level GAR and related KPIs (CapEx/OpEx alignment where data available)
- Flag regulatory updates that may change existing classifications (new delegated acts, TSC amendments)

**Data Required:**
- Client portfolio with NACE code mapping and exposure amounts
- EU Taxonomy regulation text, delegated acts, and TSC databases
- Client sustainability disclosures and emissions data
- NACE code reference database
- Prior year taxonomy classifications for comparison

**Autonomy Level:** Human-in-the-Loop
NACE code mapping and eligibility screening are automated. TSC pre-screening against public data is automated. DNSH assessment checklist generation is automated. Final alignment determination requires analyst review and sign-off. Regulatory update impact analysis is flagged for team review.

**Example Interaction:**
> The annual taxonomy reassessment cycle begins for the bank's €94B European lending portfolio — 2,134 corporate clients. The Taxonomy Classification Engine processes each client: it auto-maps NACE codes for 1,876 clients (88%) using company descriptions and sector classifications. Of these, 743 are identified as taxonomy-eligible across climate mitigation and adaptation activities. The agent pre-screens TSC compliance: for 312 clients in eligible sectors, sufficient public data exists to make preliminary TSC assessments. It finds 189 likely meeting TSC thresholds (e.g., renewable energy generators below 100g CO2e/kWh, buildings with EPC certificates showing NZEB compliance). For DNSH, it generates activity-specific checklists for each client — flagging 47 clients with potential DNSH concerns (e.g., water-intensive manufacturers in water-stressed basins, construction companies without biodiversity management plans). The sustainability team receives a prioritized work queue: "189 clients recommended for Aligned classification pending DNSH verification. 123 clients eligible but TSC data gaps — engagement recommended. 47 clients with DNSH flags requiring detailed assessment." Estimated completion: 6 weeks versus last year's 14 weeks.

---

### Use Case 6: Sustainability Client Advisory & Thought Leadership Pipeline

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks differentiate on thought leadership and advisory capability. The sustainability team is expected to produce sector-specific ESG research notes, host client webinars on regulatory developments (CSRD, SEC Climate Rules, EU Taxonomy), participate in conferences, and provide bespoke advisory to relationship clients. This advisory work directly drives mandate wins — clients choose banks whose sustainability teams demonstrate deep sector expertise and regulatory foresight. However, with 70%+ of team capacity consumed by compliance reporting and deal support, thought leadership is perpetually deprioritized. Content is produced ad hoc, distributed inconsistently, and rarely tracked for client engagement or revenue impact. The bank's knowledge assets — decades of ESG due diligence findings, sector expertise, regulatory interpretations — remain trapped in individual analysts' heads and scattered files.

#### The Solution
monday.com as the sustainability advisory and thought leadership management platform. **Advisory Pipeline Board** with columns: Client Name (text), Relationship Manager (people), Advisory Topic (dropdown: CSRD Readiness, Net-Zero Strategy, Green Bond Structuring, Taxonomy Alignment, Supply Chain Due Diligence, Climate Risk Assessment), Engagement Type (dropdown: Bespoke Advisory, Webinar, Research Note, Conference Presentation, CAB Participation), Status (status: Identified → Scoped → Scheduled → Delivered → Follow-Up), Revenue Opportunity (numbers), Sustainability Advisor (people), Delivery Date (date). **Content Calendar Board** for thought leadership: Publication Name (text), Topic (dropdown), Author (people), Status (status: Idea → Research → Draft → Review → Published → Distributed), Publish Date (date), Distribution Channels (tags: Email, LinkedIn, Client Portal, Event), Engagement Metrics (numbers). Connect boards link advisory engagements to deal pipeline opportunities.

#### The Outcome
Systematize advisory delivery, increasing client engagement touchpoints by 60%. Track revenue influence from sustainability advisory ($10-50M+ annually in identifiable mandate attribution). Build reusable content library reducing production time for similar materials by 70%. Demonstrate sustainability team's revenue contribution to bank leadership, justifying headcount investment. Create flywheel: thought leadership → client engagement → deal pipeline → market intelligence → better thought leadership.

#### Discovery Questions
1. "How does your sustainability team's advisory work connect to deal origination — can you trace mandate wins back to ESG advisory relationships?"
2. "What's your current cadence for sustainability thought leadership — research notes, webinars, client briefings? Is it systematic or ad hoc?"
3. "How do your relationship managers identify which clients need sustainability advisory? Is there a proactive screening process?"
4. "When a major regulatory development hits (like CSRD adoption), how quickly can your team produce client-facing guidance? Who coordinates distribution?"
5. "Do you measure client engagement with your sustainability content — open rates, follow-up requests, meeting conversions?"

#### Industry Context
Sustainability advisory is a revenue multiplier for investment banks — clients who receive high-quality ESG advisory are 3-5x more likely to award sustainable finance mandates. The competitive landscape is intense: Goldman Sachs, JPMorgan, BNP Paribas, and Citi all have large sustainability teams producing prolific thought leadership. Clients increasingly expect their banking partners to be ahead of regulation, not reactive. The "advisory-to-mandate" pipeline is well-understood but poorly operationalized at most banks — the connection between a CSRD readiness workshop and a subsequent green bond mandate six months later is real but rarely tracked.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Sustainability Advisory & Thought Leadership board for an investment bank. Columns: Activity Name (text), Client or Audience (text), Type (dropdown: Bespoke Client Advisory, Sector Research Note, Regulatory Update Brief, Client Webinar, Conference Presentation, Podcast/Interview, White Paper, Client Workshop), Topic (dropdown: CSRD/ESRS Readiness, Net-Zero Strategy, Green Bond Structuring, EU Taxonomy, TNFD/Biodiversity, Supply Chain CSDDD, Climate Scenario Analysis, Social Impact Measurement, Carbon Markets, Transition Finance), Status (status: Idea, Scoping, Research, Drafting, Review, Approved, Scheduled, Delivered, Follow-Up Complete), Author/Presenter (people), Reviewer (people), Target Audience (dropdown: Existing Clients, Prospects, Internal Teams, Industry Conference, Media), Delivery Date (date), Revenue Opportunity Link (text), Engagement Score (numbers: views, attendees, or downloads), Follow-Up Actions (long text), Content File (file). Groups: Q1 2026, Q2 2026, Evergreen Content, Ideas Backlog. Automations: When Status changes to Delivered, prompt for Engagement Score entry. When Type is Bespoke Client Advisory, auto-create follow-up task for 2 weeks post-delivery. Views: Calendar of delivery dates, Dashboard with activities by type (pie chart), activities by topic (bar chart), engagement trends (line chart), upcoming deliverables in next 30 days."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Sustainability Knowledge Curator
**Agent Purpose:** Monitor regulatory developments, identify client advisory opportunities, and accelerate thought leadership production.

**Triggers:**
- Major ESG regulatory announcement (EU, SEC, FCA — monitored via news feeds)
- Client portfolio analysis reveals sector-specific ESG exposure patterns
- Quarterly thought leadership planning cycle
- Client meeting notes mentioning sustainability topics (integration with CRM)
- Content engagement metrics cross threshold (high-interest topics)

**Actions:**
- Scan regulatory feeds and generate executive summaries of material ESG developments with client impact assessment
- Match regulatory developments to client portfolio and recommend targeted advisory outreach
- Draft thought leadership content outlines with key messages, data points, and recommended visualizations
- Maintain curated ESG knowledge base organized by topic, sector, and regulatory framework
- Analyze content engagement patterns and recommend topics for next quarter's thought leadership calendar
- Generate personalized client briefing notes for relationship managers ahead of meetings

**Data Required:**
- Regulatory announcement feeds (EU Official Journal, SEC, FCA, ISSB)
- Client portfolio data with sector classifications
- Historical advisory engagement records
- Content engagement analytics (email opens, webinar attendance, download counts)
- CRM meeting notes and client interaction history
- Internal research and due diligence knowledge base

**Autonomy Level:** Escalation-Based
Regulatory monitoring and summary generation are fully autonomous. Client opportunity identification and matching are automated with RM notification. Content draft outlines are generated but require author review. Knowledge base maintenance is automated with periodic human curation. Client briefing notes are auto-generated for RM review before meetings.

**Example Interaction:**
> The EU Parliament formally adopts amendments to the CSRD timeline, accelerating reporting requirements for certain financial institutions by one year. Within 2 hours, the Sustainability Knowledge Curator agent generates: (1) A 2-page executive summary of the changes and their implications for banks and bank clients, (2) A client impact analysis identifying 47 corporate banking clients affected by the accelerated timeline, (3) A recommended outreach list prioritized by relationship value and CSRD readiness gap, (4) A draft webinar outline titled "CSRD Timeline Accelerated: What Your Bank Needs to Know Now" with proposed speaker panel and key messages. It sends the impact analysis to 12 relationship managers with personalized notes: "Your client [Company] in the chemicals sector is now subject to FY 2025 CSRD reporting (moved up from FY 2026). Their current sustainability reporting maturity suggests they'll need significant support. Recommend reaching out to offer our CSRD readiness advisory package." Three RMs book client meetings within the week, leading to one advisory engagement and one green bond structuring conversation.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| CSRD | Corporate Sustainability Reporting Directive — EU regulation requiring detailed sustainability disclosures |
| ESRS | European Sustainability Reporting Standards — the detailed reporting standards under CSRD |
| EU Taxonomy | Classification system defining environmentally sustainable economic activities |
| GAR | Green Asset Ratio — proportion of taxonomy-aligned assets to total covered assets |
| PCAF | Partnership for Carbon Accounting Financials — methodology for calculating financed emissions |
| Financed Emissions | GHG emissions attributable to a bank's lending and investment portfolio (Scope 3, Category 15) |
| SBTi | Science Based Targets initiative — validates corporate decarbonization targets against climate science |
| NZBA | Net-Zero Banking Alliance — commitment by banks to align portfolios with net-zero by 2050 |
| SFDR | Sustainable Finance Disclosure Regulation — EU disclosure requirements for financial market participants |
| ICMA GBP | International Capital Market Association Green Bond Principles — market standard for green bond issuance |
| SLB | Sustainability-Linked Bond — bond with financial terms tied to sustainability KPI achievement |
| SPO | Second-Party Opinion — independent assessment of a sustainable finance framework's credibility |
| TCFD | Task Force on Climate-related Financial Disclosures — framework for climate risk reporting |
| TNFD | Taskforce on Nature-related Financial Disclosures — framework for biodiversity and nature risk reporting |
| CSDDD | Corporate Sustainability Due Diligence Directive — EU law mandating human rights and environmental due diligence |
| Double Materiality | Assessing both financial impact of ESG on the company AND the company's impact on society/environment |
| Greenium | Pricing premium (lower yield) achieved by green bonds versus conventional bonds from the same issuer |
| NACE Code | Statistical Classification of Economic Activities in the European Community — used for EU Taxonomy classification |
| TSC | Technical Screening Criteria — specific thresholds activities must meet for EU Taxonomy alignment |
| DNSH | Do No Significant Harm — EU Taxonomy requirement that aligned activities don't harm other environmental objectives |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Head of Sustainability / Chief Sustainability Officer | Overall ESG strategy, regulatory compliance, Board reporting | Decision-maker |
| Sustainable Finance Lead | Green bond/SLB structuring, deal-level advisory | Decision-maker (deal) |
| ESG Analyst | Data collection, taxonomy classification, due diligence | User (primary) |
| Regulatory Reporting Manager | CSRD/SFDR/TCFD filing coordination | Influencer |
| Financed Emissions Analyst | PCAF calculations, portfolio carbon tracking | User (primary) |
| Head of DCM / Capital Markets | Sustainable finance revenue targets, league table positioning | Decision-maker (revenue) |
| Chief Risk Officer | Climate risk integration, scenario analysis | Decision-maker (risk) |
| General Counsel | ESG disclosure liability, greenwashing risk management | Influencer |
| Investor Relations | ESG narrative for bank's own investors and stakeholders | Influencer |
| Board ESG Committee | Governance oversight of sustainability strategy | Decision-maker (governance) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Risk Management | Climate risk modeling, scenario analysis (NGFS), transition risk assessment | Integrated climate risk + sustainability data platform |
| Capital Markets (DCM/ECM) | Green bond and SLB origination, ESG-integrated offerings | Sustainable finance pipeline visibility and structuring workflows |
| M&A Advisory | ESG due diligence integration into deal processes | Standardized ESG DD workflows linked to deal management |
| Compliance | Regulatory filing coordination (CSRD, SFDR, SEC Climate) | Unified regulatory reporting platform across financial and non-financial disclosures |
| Operations / Facilities | Operational carbon footprint data (Scope 1/2) | Automated operational emissions data feeds for reporting |
| Procurement | Supply chain ESG assessment, responsible sourcing | Third-party ESG due diligence linked to vendor management |
| HR | DEI metrics, pay equity data, workforce disclosures | Social metrics pipeline for ESRS S1 reporting |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Workiva | ESG and financial reporting platform with XBRL tagging | Narrowly focused on disclosure filing mechanics. monday.com covers the full lifecycle — data collection, workflow orchestration, advisory management — not just the final report. |
| Persefoni | Carbon accounting and climate disclosure platform | Strong on carbon math but weak on workflow orchestration and cross-departmental collaboration. monday.com integrates sustainability workflows with the rest of the bank's operations. |
| Sphera / Ecoinvent | Environmental data management and LCA platforms | Technical environmental data tools, not designed for workflow management. monday.com orchestrates the people, process, and approvals around the data. |
| Sustainalytics / MSCI | ESG ratings and data providers | Data inputs, not workflow tools. monday.com consumes ESG ratings data while managing the workflows around assessment, disclosure, and advisory. |
| Spreadsheets (Excel/Google Sheets) | Universal ESG reporting workhorse | No workflow automation, no audit trail, no collaboration features, version control chaos. monday.com eliminates the "sustainability team runs on spreadsheets" problem. |
| Salesforce Net Zero Cloud | Sustainability data management on Salesforce platform | Requires Salesforce ecosystem commitment and significant customization. monday.com deploys faster, costs less, and doesn't lock the sustainability team into a CRM platform's paradigm. |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We need a dedicated ESG reporting tool like Workiva or Persefoni." | "Those tools are strong at the final reporting output — but who's orchestrating the 6-month data collection process across 15 departments? monday.com manages the workflow that feeds those tools. Many teams use both: monday.com for orchestration, specialized tools for calculation and filing." |
| "Our sustainability data requirements are too complex for a work management platform." | "The data lives in your source systems — ERP, HRIS, facilities management. What you need is orchestration: who provides what data, by when, in what format, and who reviews it. That's exactly what monday.com excels at. We're the conductor, not the instruments." |
| "We only have 5 people on the sustainability team — we can't adopt another platform." | "That's precisely why you need this. With 5 people covering CSRD, TCFD, PCAF, deal DD, and advisory, you need force multiplication. monday.com automates the coordination that currently happens over email and spreadsheets — giving your small team the capacity of a team twice its size." |
| "Our ESG data is sensitive — taxonomy alignment, financed emissions." | "monday.com's enterprise security (SOC 2, HIPAA compliance, data residency options) meets financial institution standards. The data points you're tracking — NACE codes, emission factors, taxonomy alignment — aren't trading secrets. They're operational workflow data that benefits enormously from centralized management." |
| "We're still figuring out our ESG strategy — it's too early to systematize." | "That's actually the ideal time. Building structured workflows now means your processes scale as requirements grow. Banks that wait until CSRD is due to build systems end up in crisis mode. We can start with your most pressing need (portfolio carbon? taxonomy? disclosure?) and expand organically." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder: Financial institution using monday.com for ESG disclosure management]
- [Placeholder: Bank that reduced sustainability reporting preparation time by 50%+]
- [Placeholder: Asset manager tracking portfolio ESG metrics on monday.com]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
