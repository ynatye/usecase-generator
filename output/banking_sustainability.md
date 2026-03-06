# Banking × Sustainability Playbook

## Overview

Sustainability in banking has evolved from a peripheral corporate social responsibility (CSR) function into a strategic imperative driven by regulatory mandates, investor expectations, and stakeholder activism. Global frameworks like the EU Taxonomy, Task Force on Climate-related Financial Disclosures (TCFD), and the SEC's proposed climate disclosure rules have transformed sustainability departments from small ESG reporting teams into cross-functional hubs managing climate risk assessment, green finance portfolios, and decarbonization commitments across the entire institution.

A typical large bank's sustainability department comprises 15–50 professionals spanning ESG strategy, climate risk modeling, sustainable finance product development, regulatory reporting, and stakeholder engagement. They coordinate with Risk, Finance, Legal, Lending, and Investment Banking divisions to embed environmental and social criteria into credit decisions, portfolio management, and product design. Mid-market banks are rapidly building these capabilities as regulators extend disclosure requirements downstream.

The operational complexity is staggering: tracking financed emissions across thousands of counterparties, managing green bond frameworks, conducting climate scenario analyses across multiple time horizons, and producing auditable ESG reports for regulators, rating agencies, and investors — all while the regulatory landscape shifts quarterly. Most teams cobble together spreadsheets, consultant deliverables, and siloed databases, creating massive inefficiency and audit risk.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | ESG reporting scope expanding 3-5x while headcount stays flat; automation is the only path |
| 2 | Consolidate Tech Stack with AI | High | Teams juggle 8-12 tools (Bloomberg ESG, MSCI, Sustainalytics, spreadsheets, SharePoint) with no single source of truth |
| 3 | Replace or Radically Augment Headcount | Medium-High | Climate risk analysts and ESG data specialists are scarce and expensive ($150K-$250K); AI can augment capacity |

## Prioritized Use Cases

---

### Use Case 1: ESG Regulatory Reporting & Disclosure Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banks face an alphabet soup of ESG disclosure requirements — TCFD, CDP, GRI, SASB, EU CSRD, SEC Climate, ISSB — each with different taxonomies, metrics, timelines, and formats. A single bank may produce 15+ ESG reports annually. Teams manually extract data from dozens of systems, reconcile conflicting methodologies, and manage review cycles across Legal, Risk, Finance, and the Board. A single missed disclosure or data error can trigger regulatory action, rating downgrades, or reputational damage. Most teams spend 60-70% of their time on data collection rather than analysis.

#### The Solution
monday.com Work Management serves as the central ESG reporting command center. Each disclosure framework gets its own board with columns for metric name (text), data source (dropdown), data owner (people), collection deadline (date), review status (status: Draft → Under Review → Legal Approved → Final), value (numbers), YoY change (formula), and evidence/documentation (files). Automations trigger data collection requests 8 weeks before deadlines, escalate overdue items, and notify Legal when reviews are pending. Dashboards aggregate completion rates across all frameworks, flag gaps, and track regulatory calendar milestones. mondayDB stores historical ESG data for trend analysis and audit trails.

#### The Outcome
60% reduction in reporting cycle time (from 12 weeks to 5 weeks per major disclosure). Elimination of data reconciliation errors through single source of truth. 100% audit trail for every data point. Capacity to absorb 2-3 new regulatory frameworks without additional headcount.

#### Discovery Questions
- How many distinct ESG disclosure frameworks do you currently report against, and how do you manage the overlapping but different metrics across them?
- What percentage of your sustainability team's time is spent collecting data versus analyzing it and making strategic recommendations?
- Have you ever had a material restatement or late filing on an ESG disclosure, and what was the impact?
- How do you currently track the provenance and quality of each ESG data point for audit purposes?
- With CSRD and SEC climate rules expanding scope, how are you planning to absorb the additional reporting burden?

#### Industry Context
Banks typically report against 5-8 frameworks simultaneously. The EU CSRD alone requires ~1,100 data points. "Double materiality" (reporting on both financial impact of ESG issues AND the bank's impact on environment/society) is becoming standard. ESG rating agencies (MSCI, Sustainalytics, ISS) each use proprietary methodologies, so the same bank can have wildly different ratings — creating internal confusion about which metrics to prioritize.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an ESG Regulatory Reporting Hub. Create a board called 'ESG Disclosure Tracker' with these columns: Framework (dropdown: TCFD, CDP, GRI, SASB, EU CSRD, SEC Climate, ISSB, PRI), Metric Name (text), Metric Category (dropdown: Climate, Social, Governance, Environmental), Data Source System (dropdown: Bloomberg, Internal Risk, Finance ERP, HR System, Facilities, Manual), Data Owner (people), Collection Deadline (date), Submission Deadline (date), Status (status: Not Started, Data Requested, In Collection, Under Review, Legal Approved, Final, Submitted), Current Value (numbers), Prior Year Value (numbers), YoY Change % (formula), Evidence Documents (files), Notes (long text), Materiality Rating (dropdown: High, Medium, Low). Add automations: when Status is 'Not Started' and Collection Deadline is within 8 weeks, change Status to 'Data Requested' and notify Data Owner. When Status changes to 'Under Review', notify the Legal group. When Submission Deadline is within 2 weeks and Status is not 'Final' or 'Submitted', send urgent notification to board owners. Create a Dashboard view showing: completion rate by Framework (pie chart), overdue items (table widget filtered by past-due deadlines), submission calendar (timeline), and data quality score (number widget counting items with Evidence Documents attached vs total). Add a Timeline view grouped by Framework showing collection and submission windows. Add a Kanban view grouped by Status for daily standups."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Disclosure Sentinel
**Agent Purpose:** Automate ESG data collection orchestration, deadline management, and cross-framework metric reconciliation.

**Triggers:**
- 10 weeks before any Submission Deadline, initiate collection workflow
- When Data Owner hasn't updated an item within 5 business days of Collection Deadline
- When new regulatory framework is added to the board
- Weekly on Monday at 8 AM for status digest
- When Status changes to "Under Review"

**Actions:**
- Send personalized data collection requests to Data Owners with specific metric definitions and format requirements
- Auto-populate Current Value from connected data sources where integrations exist
- Flag metric inconsistencies across frameworks (e.g., Scope 1 emissions reported differently to CDP vs TCFD)
- Generate weekly progress reports for Sustainability leadership with risk-ranked overdue items
- Draft metric narratives based on Current Value, Prior Year Value, and contextual notes
- Escalate to department head when items are >5 days overdue with impact assessment

**Data Required:**
- Integration with Bloomberg ESG terminal or data feeds
- Access to Finance ERP for financial metrics
- HR system for workforce diversity data
- Facilities management for energy/water consumption data
- Prior year submissions for benchmarking

**Autonomy Level:** Human-in-the-Loop
Auto-populates data and drafts narratives; all values require human verification before status moves to "Final." Legal review is always manual.

**Example Interaction:**
> The ESG Disclosure Sentinel detects that CDP submission is due in 10 weeks and initiates the collection workflow. It sends tailored requests to 23 data owners across Risk, Finance, Facilities, and HR — each message specifying the exact metrics needed, acceptable units, and deadline. Three weeks in, it flags that Scope 3 Category 15 (financed emissions) data from the lending portfolio hasn't been updated. It escalates to the Head of Climate Risk with context: "Financed emissions data for commercial real estate portfolio is outstanding. This metric was flagged by CDP as 'high scrutiny' last year. Recommend prioritizing — 6 weeks remain." Simultaneously, it notices that the Scope 1 emissions figure entered for TCFD (45,230 tCO2e) differs from the value staged for CDP (44,890 tCO2e) and creates a reconciliation task: "Scope 1 discrepancy of 340 tCO2e detected between TCFD and CDP submissions. Likely cause: different reporting boundary treatment for leased offices. Please confirm which boundary methodology applies to each framework."

---

### Use Case 2: Financed Emissions Tracking & Portfolio Decarbonization

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Under PCAF (Partnership for Carbon Accounting Financials) standards, banks must calculate and disclose the greenhouse gas emissions associated with their lending and investment portfolios — "financed emissions." This requires mapping thousands of counterparties to emission factors, applying attribution methodologies by asset class (corporate loans, mortgages, project finance, commercial real estate), and tracking progress against net-zero commitments (e.g., NZBA targets). Most banks do this quarterly in massive spreadsheets with 50,000+ rows, resulting in 3-4 month lag times, frequent errors, and inability to make real-time portfolio steering decisions.

#### The Solution
monday.com Work Management with mondayDB creates a financed emissions tracking system. A master board tracks each counterparty/sector with columns: Sector (dropdown: Power, Oil & Gas, Real Estate, Agriculture, Transport, Steel, etc.), Counterparty Name (text), Outstanding Exposure ($M) (numbers), Emission Factor Source (dropdown: Reported, Estimated, PCAF DB, CDP), Scope 1+2 Emissions (numbers - tCO2e), Scope 3 Emissions (numbers), Attribution Factor (numbers - %), Financed Emissions (formula), PCAF Data Quality Score (dropdown: 1-5), Decarbonization Target Year (date), Sector Pathway Alignment (status: Aligned, Lagging, Misaligned, No Target). Dashboards visualize portfolio-level emissions by sector, track trajectory against NZBA commitments, and flag high-emitting counterparties needing engagement.

#### The Outcome
Portfolio emissions visibility reduced from quarterly (3-month lag) to monthly. Identification of top 50 counterparties driving 80% of financed emissions for targeted engagement. Data quality score improvement from PCAF Level 4 (estimated) to Level 2 (reported) across 60% of portfolio within 18 months. Regulatory exam readiness with full audit trail.

#### Discovery Questions
- How do you currently calculate financed emissions across your lending portfolio, and what's the typical lag time between data collection and reporting?
- What PCAF data quality score distribution does your portfolio have, and what's your roadmap to improve it?
- How do you translate portfolio-level decarbonization commitments into sector-specific targets and individual counterparty engagement strategies?
- When a regulator or investor asks about your climate transition risk in a specific sector, how quickly can you produce that analysis?
- Are your front-office relationship managers equipped with ESG data to have informed conversations with clients about their transition plans?

#### Industry Context
PCAF defines 6 asset classes with different attribution methodologies. Data quality scores range from 1 (audited emissions) to 5 (estimated based on revenue). Most banks' portfolios sit at an average of 3.5-4.0. The NZBA (Net-Zero Banking Alliance) requires members to set 2030 intermediate targets for priority sectors. "Transition finance" — lending to high-emitting companies with credible decarbonization plans — is a critical strategic debate: too aggressive means losing clients; too lenient means greenwashing risk.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Financed Emissions Portfolio Tracker. Create a board called 'Portfolio Carbon Dashboard' with columns: Sector (dropdown: Power Generation, Oil & Gas, Real Estate - Commercial, Real Estate - Residential, Agriculture, Transport - Aviation, Transport - Shipping, Transport - Auto, Steel & Cement, Manufacturing, Other), Counterparty Name (text), Relationship Manager (people), Outstanding Exposure $M (numbers), Asset Class (dropdown: Corporate Loans, Project Finance, Commercial Real Estate, Mortgages, Listed Equity, Bonds), Emission Factor Source (dropdown: Company Reported & Verified, Company Reported, CDP Disclosed, PCAF Database, Sector Average, Revenue Estimated), Scope 1+2 tCO2e (numbers), Scope 3 tCO2e (numbers), Attribution Factor % (numbers), Financed Emissions tCO2e (formula: Scope 1+2 × Attribution Factor), PCAF Data Quality Score (dropdown: Score 1, Score 2, Score 3, Score 4, Score 5), Emissions Intensity (formula: Financed Emissions / Exposure), Client Transition Plan (status: Science-Based Target, Committed, In Progress, No Plan, Assessed - Insufficient), Engagement Priority (status: Immediate, Planned, Monitoring, N/A), Last Engagement Date (date), Next Review Date (date), Notes (long text). Add automations: when PCAF Data Quality Score is 'Score 4' or 'Score 5', set Engagement Priority to 'Planned' and notify Relationship Manager. When Client Transition Plan is 'No Plan' and Outstanding Exposure is greater than 50, set Engagement Priority to 'Immediate'. Create a Dashboard with: total financed emissions by Sector (bar chart), emissions intensity trend (chart widget), PCAF quality score distribution (pie chart), top 20 emitters table (sorted by Financed Emissions descending), and sector pathway alignment summary. Add a Chart view showing portfolio emissions trajectory vs. NZBA 2030 target."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Carbon Portfolio Analyst
**Agent Purpose:** Continuously monitor and analyze portfolio carbon exposure, flag misalignment with net-zero targets, and generate counterparty engagement briefs.

**Triggers:**
- Monthly on the 1st: recalculate portfolio-level emissions
- When Outstanding Exposure changes by more than 10% for any counterparty
- When new counterparty is added to the board
- Quarterly for NZBA target progress assessment
- When Client Transition Plan status changes

**Actions:**
- Calculate financed emissions using PCAF methodology appropriate to each asset class
- Compare sector-level emissions trajectory against NZBA 2030 intermediate targets and flag sectors off-track
- Generate counterparty engagement briefs for top emitters including: current emissions profile, peer comparison, transition plan assessment, and recommended talking points
- Alert Risk and Lending teams when new loan originations would materially increase sector emissions concentration
- Produce quarterly Board-ready decarbonization progress summary with RAG status by sector
- Recommend PCAF data quality improvement actions (e.g., "Request CDP disclosure from these 15 counterparties to move from Score 4 to Score 2")

**Data Required:**
- Loan management system (exposure data)
- CDP and company sustainability reports
- PCAF emission factor database
- NZBA sector pathway benchmarks
- Counterparty financial data for revenue-based estimation fallbacks

**Autonomy Level:** Escalation-Based
Routine calculations and report generation are fully autonomous. New counterparty assessments and engagement recommendations require analyst review. Any recommendation that could affect lending decisions is escalated to Credit Risk.

**Example Interaction:**
> On March 1st, the Carbon Portfolio Analyst runs its monthly recalculation. It identifies that the Power Generation sector's financed emissions have increased 8% month-over-month due to a $200M project finance facility for a new gas-fired power plant. It flags this to the Head of Sustainable Finance: "Power sector financed emissions now at 2.3M tCO2e, 12% above the linear trajectory to our 2030 NZBA target of 1.5M tCO2e. Primary driver: new $200M facility for Meridian Energy's 800MW CCGT plant. Recommend: (1) request Meridian's full transition plan including planned CCS retrofit timeline, (2) assess whether carbon offset provisions in loan documentation are sufficient, (3) consider whether this facility should be classified as 'transition finance' under our framework." It simultaneously generates an engagement brief for the Relationship Manager with peer comparison data showing Meridian's emissions intensity vs. sector median.

---

### Use Case 3: Green Bond & Sustainable Finance Product Lifecycle

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
The sustainable finance market ($1.6T annual issuance) requires rigorous lifecycle management: structuring green/social/sustainability-linked bonds and loans, managing use-of-proceeds tracking, conducting annual impact reporting, maintaining second-party opinion (SPO) compliance, and responding to investor inquiries. Each green bond requires tracking proceeds allocation to eligible projects, monitoring environmental impact metrics, and producing investor reports — often across 10-year tenors. Teams manage this across deal folders, spreadsheets, investor relations databases, and external verifier portals with no integrated workflow.

#### The Solution
monday.com Work Management creates an end-to-end sustainable finance product lifecycle board. Columns include: Instrument Name (text), Type (dropdown: Green Bond, Social Bond, Sustainability Bond, SLB, Green Loan, Sustainability-Linked Loan), Issuance Date (date), Maturity Date (date), Total Proceeds (numbers), Allocated Proceeds (numbers), Unallocated Balance (formula), Eligible Project Categories (dropdown multi-select: Renewable Energy, Clean Transport, Green Buildings, Water, Waste, Biodiversity), Framework Alignment (dropdown: ICMA GBP, LMA GLP, CBI Standard), SPO Provider (dropdown: Sustainalytics, ISS, Vigeo Eiris, CICERO), SPO Status (status: Drafting, Under Review, Approved, Published), Annual Reporting Status (status: Data Collection, Drafting, External Review, Published), Impact Metrics (subitems for each allocated project with specific KPIs). Automations trigger annual reporting workflows 3 months before anniversary dates.

#### The Outcome
100% on-time annual impact reporting (vs. industry average of 73%). Elimination of proceeds misallocation risk. Investor inquiry response time reduced from 5 days to same-day. Capacity to scale sustainable finance issuance 3x without adding operations headcount.

#### Discovery Questions
- How many outstanding green/social/sustainability-linked instruments do you currently manage, and how do you track proceeds allocation across their full tenor?
- What's your process for annual impact reporting — how many people are involved and how long does each report take?
- Have you ever had an investor or regulator challenge whether proceeds were allocated to genuinely eligible projects?
- How do you manage the relationship with your second-party opinion provider, and how do framework updates (e.g., EU Green Bond Standard) affect existing instruments?
- What's your pipeline for new sustainable finance issuance, and how confident are you in your operational capacity to support it?

#### Industry Context
ICMA Green Bond Principles require annual reporting on use of proceeds and environmental impact. The EU Green Bond Standard (effective 2025) adds mandatory alignment with EU Taxonomy, external review requirements, and proceeds tracking with European Securities regulator oversight. "Greenwashing" accusations are the #1 reputational risk — a misallocated dollar can make headlines. SLBs (Sustainability-Linked Bonds) add another complexity layer: tracking KPI performance against targets that trigger coupon step-ups.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Sustainable Finance Product Lifecycle Manager. Create a board called 'Sustainable Finance Portfolio' with columns: Instrument Name (text), Instrument Type (dropdown: Green Bond, Social Bond, Sustainability Bond, Sustainability-Linked Bond, Green Loan, SLL), ISIN (text), Issuance Date (date), Maturity Date (date), Currency (dropdown: USD, EUR, GBP, JPY, CHF), Total Proceeds $M (numbers), Allocated Proceeds $M (numbers), Unallocated Balance $M (formula), Allocation % (formula), Framework (dropdown: ICMA GBP 2021, LMA GLP, CBI Climate Bonds Standard, EU Green Bond Standard), Eligible Categories (dropdown multi-select: Renewable Energy, Energy Efficiency, Clean Transportation, Green Buildings, Sustainable Water, Pollution Prevention, Biodiversity, Climate Adaptation), SPO Provider (dropdown: Sustainalytics, ISS ESG, CICERO, Vigeo Eiris, S&P), SPO Expiry Date (date), Annual Report Due Date (date), Annual Report Status (status: Not Started, Data Collection, Impact Calculation, Draft Review, External Verification, Published), Lead Structurer (people), Impact Reporting Owner (people), Investor Inquiries Open (numbers), Notes (long text). Create subitems for each instrument to track individual eligible project allocations with: Project Name (text), Allocation Amount $M (numbers), Category (dropdown matching parent), Impact Metric (text), Impact Value (numbers), Impact Unit (text), Verification Status (status). Add automations: 90 days before Annual Report Due Date, change Annual Report Status to 'Data Collection' and notify Impact Reporting Owner. When Unallocated Balance exceeds 20% of Total Proceeds and instrument age > 24 months, notify Lead Structurer with alert. When SPO Expiry Date is within 60 days, notify team. Create Dashboard showing: total sustainable finance outstanding (number widget), allocation status across portfolio (stacked bar), annual reporting completion (progress widget), impact metrics summary by category, and upcoming deadlines calendar."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Green Finance Lifecycle Manager
**Agent Purpose:** Automate proceeds tracking, impact metric collection, annual report drafting, and investor inquiry responses across the sustainable finance portfolio.

**Triggers:**
- Monthly: reconcile proceeds allocation against treasury records
- 90 days before each Annual Report Due Date
- When investor inquiry is logged (new item in connected Inquiries board)
- When new eligible project is funded and needs allocation
- When regulatory framework updates are published (manual trigger)

**Actions:**
- Auto-calculate impact metrics from project-level data (e.g., MWh renewable energy generated, tCO2e avoided, m² green buildings certified)
- Draft annual impact report sections using templates aligned to ICMA Harmonized Framework
- Generate investor inquiry responses by pulling relevant data points and formatting for the specific question
- Flag proceeds allocation anomalies (e.g., project no longer meets eligibility criteria due to scope change)
- Track SLB KPI performance against targets and calculate coupon step-up probability
- Alert Legal and Treasury when framework updates may affect existing instruments

**Data Required:**
- Treasury system for proceeds flow data
- Project finance system for individual project metrics
- SPO documentation and framework texts
- Investor relations CRM for inquiry history
- Regulatory update feeds (ICMA, EU, CBI)

**Autonomy Level:** Human-in-the-Loop
Proceeds reconciliation and impact calculation are autonomous. Report drafts require review by Impact Reporting Owner. Investor inquiry responses require approval before sending. Framework compliance assessments are escalated to Legal.

**Example Interaction:**
> The Green Finance Lifecycle Manager detects that the $500M Green Bond (ISIN: XS1234567890) annual report is due in 90 days. It initiates data collection from 12 allocated projects spanning renewable energy and green buildings. For the 50MW solar farm in Arizona, it pulls generation data (87,600 MWh) and calculates avoided emissions (37,674 tCO2e using EPA eGRID factors). It notices that one allocated project — a mixed-use development originally classified as "Green Buildings" — has reduced its LEED certification target from Platinum to Gold. It flags this: "Project 'Harbor Tower' LEED target downgrade may affect eligibility under our framework's 'top 15% energy performance' requirement. Recommend: request updated energy modeling from developer and assess against ICMA criteria. If ineligible, $35M proceeds reallocation needed — current unallocated balance is $22M, so additional eligible project identification required." It drafts the remaining 11 project impact summaries and stages the report for review.

---

### Use Case 4: Climate Risk Scenario Analysis & Stress Testing

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Regulators (Fed, ECB, PRA, APRA) now require banks to conduct climate scenario analyses across multiple pathways (orderly transition, disorderly transition, hot house world) and time horizons (2030, 2040, 2050). This involves translating NGFS scenarios into sector-specific impacts, modeling physical risk (floods, wildfires, sea-level rise) and transition risk (carbon pricing, technology shifts, policy changes) across the entire portfolio. Each analysis requires coordination between Risk, Economics, Lending, Treasury, and Sustainability — often involving 50+ people across 6+ months. The process is largely manual, poorly documented, and nearly impossible to reproduce for regulatory examination.

#### The Solution
monday.com Work Management orchestrates the climate scenario analysis process as a structured project. A master board tracks each scenario-sector combination with columns: Scenario (dropdown: NGFS Net Zero 2050, Below 2°C, Delayed Transition, Current Policies, NDCs), Sector (dropdown), Risk Type (dropdown: Physical - Acute, Physical - Chronic, Transition - Policy, Transition - Technology, Transition - Market, Transition - Reputation), Time Horizon (dropdown: 2030, 2040, 2050), Analysis Owner (people), Status (status: Scoping, Data Collection, Modeling, Peer Review, Calibration, Final), Key Assumptions (long text), Portfolio Impact Estimate (numbers), Confidence Level (dropdown: High, Medium, Low), Documentation (files), Review Notes (long text). Connected boards track individual model inputs, data sources, and methodology decisions for audit trail.

#### The Outcome
Scenario analysis cycle time reduced from 6 months to 10 weeks. Full audit trail of every assumption and methodology decision for regulatory examination. Ability to run ad-hoc scenarios (e.g., sudden carbon tax) in days rather than months. Consistent, reproducible methodology across the organization.

#### Discovery Questions
- How did your last climate scenario analysis exercise go — how long did it take, and what feedback did you get from your regulator?
- How do you currently document the assumptions and methodology decisions that underpin your scenario analysis, and could you reproduce the analysis if asked?
- When your CEO or Board asks "what happens to our portfolio if carbon prices hit $150/ton by 2030," how long does it take to answer?
- How do you bridge the gap between macro-level NGFS scenarios and the specific impact on individual sectors and counterparties in your portfolio?
- Are your climate scenarios integrated with your broader enterprise stress testing framework, or are they run as a parallel exercise?

#### Industry Context
The NGFS (Network for Greening the Financial System) provides reference scenarios that most regulators use as a starting point. Banks must translate these macro scenarios into micro-level portfolio impacts — a highly specialized skill combining climate science, economics, and financial modeling. The ECB's 2022 climate stress test revealed that most banks' capabilities are "at an early stage." Physical risk modeling requires geospatial analysis (flood maps, wildfire zones) overlaid on collateral locations — a data integration challenge most banks haven't solved.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Climate Scenario Analysis Project Tracker. Create a board called 'Climate Stress Test Workstream' with columns: Workstream ID (text auto-number), Scenario (dropdown: Net Zero 2050, Below 2°C, Delayed Transition, Current Policies, Nationally Determined Contributions, Custom), Sector (dropdown: Power, Oil & Gas, Real Estate, Agriculture, Transport, Manufacturing, Financial Institutions, Sovereign), Risk Category (dropdown: Physical - Acute, Physical - Chronic, Transition - Policy, Transition - Technology, Transition - Market, Transition - Reputation), Time Horizon (dropdown: 2025, 2030, 2035, 2040, 2050), Analysis Owner (people), Reviewer (people), Status (status: Not Started, Scoping, Data Gathering, Modeling, Peer Review, Calibration, Management Review, Final), Methodology (dropdown: Top-Down, Bottom-Up, Hybrid), Key Assumptions (long text), Data Sources (long text), Portfolio Exposure $B (numbers), Estimated Impact - Base Case $M (numbers), Estimated Impact - Severe Case $M (numbers), Confidence Level (dropdown: High, Medium, Low, Very Low), Documentation (files), Regulatory Alignment (dropdown: Fed SR 23-7, ECB Guide, PRA SS3-19, APRA CPG 229), Due Date (date), Completion Date (date). Add automations: when Status changes to 'Peer Review', notify Reviewer. When Due Date is within 2 weeks and Status is not 'Final', escalate to board owner. Create a Dashboard with: completion by Scenario (stacked bar), total estimated impact by Sector (bar chart), confidence level distribution (pie chart), timeline of workstreams (Gantt/timeline widget), and overdue items table. Add a Table view filtered to show only items with Confidence Level 'Low' or 'Very Low' for methodology improvement focus."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Climate Scenario Coordinator
**Agent Purpose:** Orchestrate multi-team climate scenario analysis exercises, track methodology consistency, and generate regulatory-ready documentation.

**Triggers:**
- When a new scenario analysis exercise is initiated (new group created on board)
- When Status changes for any workstream
- Weekly on Wednesday for cross-workstream consistency review
- When regulatory guidance updates are detected (manual trigger)
- 30 days before regulatory submission deadline

**Actions:**
- Generate workstream task breakdowns based on scenario × sector matrix with pre-populated methodology templates
- Cross-check assumptions across workstreams for consistency (e.g., same carbon price path used for all sectors under same scenario)
- Create methodology documentation drafts capturing key decisions, data sources, and limitations
- Produce management-ready summary decks showing portfolio-level impacts with drill-down by sector and scenario
- Flag workstreams where confidence level is "Low" and recommend specific data improvements
- Generate regulatory response templates pre-populated with methodology descriptions and results

**Data Required:**
- NGFS scenario data (GDP, carbon prices, energy mix projections)
- Internal portfolio exposure data by sector and geography
- Historical loss data for calibration
- Geospatial data for physical risk (flood maps, climate projections)
- Prior scenario analysis outputs for consistency benchmarking

**Autonomy Level:** Human-in-the-Loop
Task creation and progress tracking are autonomous. Methodology consistency checks generate recommendations that require analyst confirmation. All portfolio impact estimates require modeling team validation. Regulatory submissions always require senior management approval.

**Example Interaction:**
> The Climate Scenario Coordinator detects that the 2026 Fed climate scenario analysis has been initiated with 5 scenarios × 8 sectors = 40 workstreams. It auto-generates the workstream structure, assigns owners based on last year's analysis team (adjusting for team changes), and pre-populates methodology templates. Two weeks in, it runs a consistency check and flags: "The Power sector workstream under 'Delayed Transition' assumes a carbon price of $85/ton by 2035, while the Oil & Gas workstream under the same scenario assumes $95/ton. NGFS reference value is $89/ton. Recommend aligning to $89/ton or documenting rationale for deviation." It also notices that the Real Estate physical risk workstream has Confidence Level "Very Low" and recommends: "Consider engaging ClimateWise or Four Twenty Seven for geospatial flood risk overlay on your commercial real estate collateral portfolio — this was a specific examiner finding in 2025."

---

### Use Case 5: ESG Data Quality & Third-Party Data Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banks consume ESG data from 8-15 providers (MSCI, Sustainalytics, Bloomberg, ISS, CDP, Refinitiv, S&P Global, RepRisk, Trucost), each with different coverage, methodologies, update frequencies, and formats. The same company can have an "AA" rating from MSCI and a "Medium Risk" from Sustainalytics — creating confusion for portfolio managers and credit analysts. Data gaps are pervasive: only 40% of mid-cap counterparties have published emissions data. Teams spend enormous effort reconciling, gap-filling, and maintaining internal ESG scores, often in disconnected spreadsheets that become stale within weeks.

#### The Solution
monday.com with mondayDB becomes the ESG data quality management hub. A board tracks each data provider relationship with columns: Provider (dropdown), Contract Renewal Date (date), Annual Cost (numbers), Coverage Universe (numbers), Data Types (dropdown multi-select: Ratings, Raw Metrics, Controversy Screening, Physical Risk, Transition Risk), Update Frequency (dropdown: Real-time, Daily, Weekly, Monthly, Quarterly, Annual), Data Quality Score (numbers), Integration Status (status), Account Manager (text). A connected "Data Gaps" board tracks counterparties with missing or low-quality ESG data with remediation workflows: Counterparty Name (text), Missing Data Types (dropdown), Exposure $M (numbers), Gap Priority (formula based on exposure), Remediation Action (status: Contact Company, Use Proxy, Estimate, Accept Gap), Owner (people).

#### The Outcome
Single dashboard showing ESG data coverage and quality across all providers. Data gap remediation reducing "no ESG data" counterparties from 35% to 10% within 12 months. $200K+ annual savings through identifying redundant data subscriptions. Consistent internal ESG scoring methodology applied across 95% of portfolio.

#### Discovery Questions
- How many ESG data providers do you currently subscribe to, and what's the total annual spend across them?
- When two providers give conflicting assessments of the same company, how do you resolve it — and is that process documented?
- What percentage of your lending or investment portfolio currently has no ESG data coverage, and how do you handle those counterparties in your ESG risk assessment?
- How do you evaluate whether you're getting value from each data subscription, and when did you last conduct a rationalization review?
- Are your front-office teams confident in the ESG data they're using for client conversations and deal screening?

#### Industry Context
ESG data correlation between providers averages only 0.54 (vs. 0.99 for credit ratings) — the "aggregate confusion" problem documented in academic research. SFDR, MiFID II sustainability preferences, and EU Taxonomy alignment requirements have massively increased demand for granular ESG data. "Estimated" vs. "reported" data is a major quality distinction: most SME counterparty data is modeled/estimated, creating significant uncertainty in portfolio-level ESG metrics.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an ESG Data Quality Management Hub. Create two connected boards. Board 1: 'ESG Data Providers' with columns: Provider Name (dropdown: MSCI, Sustainalytics, Bloomberg ESG, ISS ESG, CDP, Refinitiv, S&P Global CSA, RepRisk, Trucost, Moody's ESG, Custom), Contract Start Date (date), Renewal Date (date), Annual Cost $ (numbers), Universe Coverage Count (numbers), Data Categories (dropdown multi-select: ESG Ratings, Carbon Emissions, Physical Risk Scores, Transition Risk, Controversy Screening, SDG Alignment, EU Taxonomy, Supply Chain ESG), Update Frequency (dropdown: Real-Time, Daily, Weekly, Monthly, Quarterly, Annually), API Available (status: Yes, No, In Development), Integration Status (status: Live, Testing, Planned, Not Integrated), Data Quality Score (numbers 1-10), Coverage Gap % (numbers), Owner (people), Notes (long text). Board 2: 'ESG Data Gap Registry' with columns: Counterparty Name (text), Sector (dropdown), Outstanding Exposure $M (numbers), MSCI Rating (text), Sustainalytics Risk (text), Bloomberg ESG Score (text), Has Reported Emissions (status: Yes, Estimated, None), Missing Critical Data (dropdown multi-select: Scope 1-2 Emissions, Scope 3, Board Diversity, Water Usage, Waste, Human Rights Policy, Climate Target), Gap Severity (formula based on exposure and missing data count), Remediation Action (status: Direct Engagement, Proxy Data Applied, Sector Average Used, CDP Request Sent, Accepted Gap), Remediation Owner (people), Target Resolution Date (date). Connect the boards via Provider as data source. Add automations on Board 2: when Gap Severity formula exceeds threshold and Remediation Action is empty, notify Remediation Owner. Create Dashboard: provider cost vs coverage scatter chart, data gap heatmap by sector, remediation progress by status, and top 25 highest-exposure gaps table."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Data Steward
**Agent Purpose:** Monitor ESG data quality across providers, identify gaps, reconcile conflicting assessments, and manage remediation workflows.

**Triggers:**
- Daily: scan for new data updates from connected providers
- When new counterparty is onboarded (appears in lending system)
- When ESG rating changes by more than 2 notches for any counterparty
- Monthly: provider coverage and quality assessment
- When Contract Renewal Date is within 90 days

**Actions:**
- Auto-populate Data Gap Registry for new counterparties by checking coverage across all subscribed providers
- Flag material rating discrepancies across providers with analysis of likely driver (methodology difference, data lag, scope difference)
- Generate provider value-for-money reports comparing cost per covered counterparty, update timeliness, and unique coverage
- Recommend gap remediation strategies based on counterparty characteristics (public vs private, geography, sector)
- Draft CDP disclosure request letters for high-priority data gap counterparties
- Alert portfolio managers when a counterparty's ESG profile changes significantly

**Data Required:**
- API connections to all subscribed ESG data providers
- Internal counterparty master data (sector, geography, exposure)
- Historical rating data for trend analysis
- Provider contract and cost information

**Autonomy Level:** Fully Autonomous for data monitoring and gap identification. Human-in-the-Loop for remediation action decisions and provider contract recommendations.

**Example Interaction:**
> The ESG Data Steward runs its daily scan and detects that MSCI has downgraded GlobalChem Corp from "BBB" to "B" — a 3-notch drop — citing a new environmental controversy. It checks other providers: Sustainalytics still shows "Medium Risk" (no change), Bloomberg ESG score unchanged at 52/100. It creates an alert: "Material MSCI downgrade for GlobalChem Corp (Exposure: $180M). Driver: EPA enforcement action for PFAS contamination at 3 facilities — classified as 'Very Severe' controversy. Other providers haven't updated yet (expected lag: Sustainalytics 2-4 weeks, Bloomberg next quarterly refresh). Recommend: (1) Flag to Credit Risk for watchlist review, (2) Alert Relationship Manager, (3) Update internal ESG score immediately using MSCI controversy data rather than waiting for other providers to catch up."

---

### Use Case 6: Sustainability Stakeholder Engagement & Communications

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking sustainability teams manage a complex web of stakeholder relationships: ESG rating agencies (MSCI, Sustainalytics, ISS — each with annual questionnaires and engagement meetings), investor ESG analysts (dozens of institutional investors with specific ESG information requests), regulators (multiple jurisdictions with different ESG expectations), industry bodies (UNEP FI, NZBA, PRB, Equator Principles), NGOs (environmental groups monitoring lending practices), and internal stakeholders (Board ESG Committee, business line heads, investor relations). Each interaction requires tailored messaging, data preparation, and follow-up tracking. Without a system, engagement history lives in individual email inboxes, leading to inconsistent messaging and missed commitments.

#### The Solution
monday.com CRM functionality adapted for stakeholder engagement. A board tracks each stakeholder relationship: Stakeholder Name (text), Organization (text), Category (dropdown: Rating Agency, Investor, Regulator, Industry Body, NGO, Internal, Media), Engagement Type (dropdown: Questionnaire, Meeting, Inquiry, Commitment, Complaint), Priority (dropdown: Critical, High, Medium, Low), Last Contact Date (date), Next Scheduled Interaction (date), Owner (people), Status (status: Active, Scheduled, Awaiting Response, Closed), Key Topics (dropdown multi-select), Commitments Made (long text), Follow-Up Actions (subitems). Automations track engagement frequency and flag stakeholders overdue for contact.

#### The Outcome
360-degree view of all ESG stakeholder interactions. Zero missed rating agency questionnaire deadlines. Consistent messaging across all stakeholder touchpoints. 50% reduction in time preparing for stakeholder meetings through centralized briefing materials.

#### Discovery Questions
- How many distinct ESG stakeholder groups does your team actively manage relationships with, and how do you ensure consistent messaging across them?
- When MSCI or Sustainalytics sends their annual questionnaire, what's your process — and have you ever missed a deadline or submitted inconsistent data?
- How do you track commitments made to investors, regulators, or industry bodies regarding your sustainability strategy?
- When an NGO publishes a report criticizing your bank's fossil fuel lending, how quickly can you coordinate a response across Sustainability, PR, and Legal?
- Does your Board ESG Committee have visibility into the full landscape of external ESG engagements and commitments?

#### Industry Context
Banks typically interact with 50-100+ ESG stakeholders annually. Rating agency questionnaires (MSCI: ~100 questions, CDP: ~150 questions, Sustainalytics: ~80 indicators) consume 2-3 months of team time each. ShareAction and other NGOs regularly publish "banking scorecard" reports that can move stock prices. The "say-do" gap — commitments made publicly vs. actual progress — is increasingly scrutinized by investors and media.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an ESG Stakeholder Engagement Tracker. Create a board called 'ESG Stakeholder CRM' with columns: Stakeholder Name (text), Organization (text), Stakeholder Category (dropdown: ESG Rating Agency, Institutional Investor, Regulator, Industry Coalition, NGO/Advocacy, Media, Internal - Board Committee, Internal - Business Line, Proxy Advisor), Region (dropdown: Global, North America, Europe, APAC, LATAM, Middle East), Primary Contact (people), Relationship Priority (dropdown: Tier 1 - Critical, Tier 2 - Important, Tier 3 - Monitor), Engagement Frequency Target (dropdown: Weekly, Monthly, Quarterly, Semi-Annual, Annual, Ad-Hoc), Last Engagement Date (date), Next Scheduled (date), Days Since Last Contact (formula), Engagement Status (status: Active, Scheduled, Overdue, Dormant), Key Topics (dropdown multi-select: Climate Strategy, Financed Emissions, Biodiversity, Human Rights, Governance, Net Zero Targets, Green Finance, Diversity, Just Transition), Open Commitments Count (numbers), Sentiment (dropdown: Positive, Neutral, Cautious, Critical), Notes (long text), Briefing Document (files). Create subitems for each engagement: Date (date), Type (dropdown: Meeting, Questionnaire Response, Inquiry Response, Presentation, Letter, Report Submission), Summary (long text), Commitments Made (long text), Follow-up Required (status: Yes, No, Done), Follow-up Owner (people), Follow-up Due (date). Add automations: when Days Since Last Contact exceeds Engagement Frequency Target equivalent in days, change Engagement Status to 'Overdue' and notify Primary Contact owner. When Follow-up Due date passes and Follow-up Required is 'Yes', escalate. Create Dashboard: engagement activity calendar, overdue stakeholders table, commitment tracker (open vs closed), stakeholder sentiment distribution, and upcoming deadlines."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Engagement Concierge
**Agent Purpose:** Prepare stakeholder briefings, track commitment delivery, draft questionnaire responses, and maintain engagement consistency.

**Triggers:**
- 2 weeks before any Next Scheduled engagement date
- When new ESG rating agency questionnaire arrives (manual trigger)
- When Engagement Status changes to "Overdue"
- When external ESG report mentioning the bank is published (manual trigger)
- Monthly: commitment delivery status review

**Actions:**
- Generate pre-meeting briefing documents with: stakeholder history, last interaction summary, open commitments status, recent developments relevant to their focus areas, and recommended talking points
- Draft questionnaire responses by pulling data from ESG Disclosure Tracker and prior year submissions, flagging questions where data has changed materially
- Track commitment delivery across all stakeholders and flag at-risk commitments 60 days before due
- Monitor for inconsistencies in messaging across stakeholder interactions (e.g., different net-zero timeline communicated to different audiences)
- Generate quarterly Board ESG Committee summary of all external engagement activity, stakeholder sentiment trends, and commitment status

**Data Required:**
- Historical engagement records and meeting notes
- ESG disclosure data (connected to Disclosure Tracker board)
- Public ESG reports and commitments register
- External news/report monitoring feeds
- Prior questionnaire submissions

**Autonomy Level:** Human-in-the-Loop
Briefing preparation and commitment tracking are autonomous. Questionnaire draft responses require subject-matter expert review. Any external communication requires approval. Inconsistency flags are escalated to Head of Sustainability.

**Example Interaction:**
> The ESG Engagement Concierge detects that a meeting with BlackRock's ESG investment stewardship team is scheduled in 2 weeks. It generates a briefing package: "Last meeting (Oct 2025): BlackRock raised concerns about our thermal coal phase-out timeline and requested quarterly updates on Scope 3 financed emissions methodology. Status: (1) Coal phase-out policy updated in Dec 2025 — new commitment to exit thermal coal by 2030 (prev: 2035). ✅ Delivered. (2) Scope 3 methodology — PCAF-aligned calculation now covers 85% of portfolio (up from 60%). In progress — full coverage targeted Q3 2026. Suggested talking points: Lead with coal policy acceleration as evidence of ambition. Proactively share financed emissions methodology improvements. Anticipate questions about new gas-fired power project financing (they monitor Project Finance International). Prepare response on how gas fits transition strategy."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| TCFD | Task Force on Climate-related Financial Disclosures — framework for climate risk reporting |
| PCAF | Partnership for Carbon Accounting Financials — standard for measuring financed emissions |
| NZBA | Net-Zero Banking Alliance — commitment to align portfolios with net-zero by 2050 |
| Financed Emissions | GHG emissions attributable to a bank's lending and investment portfolio |
| Scope 1/2/3 | Direct emissions (1), purchased energy (2), value chain including financed emissions (3) |
| EU Taxonomy | Classification system defining environmentally sustainable economic activities |
| CSRD | Corporate Sustainability Reporting Directive — EU mandatory ESG disclosure regulation |
| SPO | Second-Party Opinion — independent assessment of a green bond framework's credibility |
| ICMA GBP | International Capital Market Association Green Bond Principles |
| Double Materiality | Reporting on both financial impact of ESG issues AND entity's impact on environment/society |
| NGFS | Network for Greening the Financial System — central banks' climate scenario consortium |
| SLB | Sustainability-Linked Bond — coupon tied to achieving sustainability KPI targets |
| Transition Risk | Financial risk from the shift to a low-carbon economy (policy, technology, market, reputation) |
| Physical Risk | Financial risk from climate change impacts (acute: storms, floods; chronic: sea-level rise, heat) |
| Greenwashing | Misleading claims about environmental credentials of a product, service, or strategy |
| ESG Integration | Systematic incorporation of ESG factors into investment analysis and credit decisions |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Sustainability Officer (CSO) | Overall ESG strategy, Board reporting, external commitments | Decision-maker |
| Head of Climate Risk | Climate scenario analysis, TCFD compliance, physical/transition risk modeling | Decision-maker |
| Head of Sustainable Finance | Green bond structuring, ESG-linked product development | Decision-maker |
| ESG Data Manager | Data provider management, quality assurance, internal scoring | Influencer |
| Sustainability Reporting Lead | Disclosure management, annual report production, rating agency engagement | Influencer |
| Chief Risk Officer (CRO) | Enterprise risk framework including climate risk integration | Decision-maker |
| Investor Relations (ESG) | Investor ESG inquiries, proxy advisor engagement | Influencer |
| Board ESG Committee Chair | Governance oversight of sustainability strategy | Decision-maker |
| Front-Office Sustainability Champions | Embed ESG into deal origination and client conversations | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Risk Management | Climate risk modeling, ESG risk integration into credit frameworks | Joint workflow for climate stress testing and counterparty ESG assessment |
| Finance & Treasury | Green bond proceeds tracking, ESG-related financial reporting | Integrated reporting platform bridging financial and ESG data |
| Legal & Compliance | Regulatory interpretation, greenwashing risk, disclosure liability | Connected compliance tracking across ESG regulations |
| Lending & Credit | ESG criteria in credit decisions, transition finance structuring | Deal screening and ESG due diligence workflows |
| IT | ESG data integration, API management, reporting automation | Data infrastructure and system integration projects |
| Investor Relations | ESG investor engagement, proxy advisory firm responses | Unified stakeholder engagement platform |
| Marketing/Communications | Sustainability report design, public messaging, social media | Brand reputation and disclosure consistency |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Workiva | SEC/ESG reporting and disclosure management | monday.com offers broader workflow + project management vs Workiva's reporting-only focus |
| Salesforce Net Zero Cloud | Emissions tracking and ESG reporting | monday.com is more flexible and faster to deploy; Net Zero Cloud is rigid and expensive |
| Persefoni | Carbon accounting platform | Niche tool; monday.com provides the workflow layer Persefoni lacks |
| Sphera | Environmental compliance and risk | Legacy enterprise tool; monday.com is more modern and user-friendly |
| Excel/SharePoint | De facto tool for 70%+ of sustainability teams | Direct displacement with structured workflows, automation, and collaboration |
| Power BI / Tableau | ESG data visualization | monday.com combines data management + visualization + workflow in one platform |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We need a specialized ESG platform, not a work management tool" | Specialized ESG tools handle calculation but not workflow. 70% of sustainability team time is coordination, data collection, and stakeholder management — that's exactly where monday.com excels. Use us as the orchestration layer alongside your ESG data providers. |
| "Our ESG data is too sensitive for a cloud platform" | monday.com offers enterprise-grade security (SOC 2 Type II, ISO 27001, GDPR) with granular permissions. ESG data increasingly needs to be shared across departments — a secure, permissioned platform is safer than spreadsheets emailed between teams. |
| "We already have Bloomberg/MSCI for ESG" | Those are data sources, not workflow tools. Who manages the 200-step process of collecting data from 20 teams, reviewing it, getting Legal sign-off, and publishing your TCFD report? That's the gap monday.com fills. |
| "The regulatory landscape changes too fast — we'll just have to redo everything" | monday.com's flexibility is the advantage. When a new regulation drops, you reconfigure boards in hours, not months. Try that with a rigid enterprise ESG platform. |
| "We're still early in our ESG journey — too soon for a platform" | That's exactly the right time. Building structured processes now prevents the technical debt that mature sustainability programs are struggling with. Start simple, scale as requirements grow. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for banking sustainability customer references]
- [Placeholder for ESG reporting workflow case studies]
- [Placeholder for financial services climate risk management examples]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
