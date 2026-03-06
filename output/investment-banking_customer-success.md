# Investment Banking × Customer Success Playbook

## Overview

Customer Success in investment banking operates fundamentally differently from typical SaaS or tech CS functions. Here, "Customer Success" manifests as client relationship management (CRM), coverage banking, and institutional client servicing — ensuring that buy-side clients (asset managers, pension funds, sovereign wealth funds, family offices) and corporate clients continue to engage the bank for advisory mandates, capital markets transactions, and structured products. The function sits at the intersection of front-office revenue generation and middle-office operations, with relationship managers (RMs) and coverage bankers responsible for wallet share growth, cross-sell orchestration, and institutional client satisfaction.

Investment banking client success teams typically manage relationships worth $5M–$500M+ in annual revenue per client. The complexity is staggering: a single institutional client may interact with dozens of product groups (M&A, ECM, DCM, leveraged finance, restructuring, derivatives, prime brokerage, research), each with different coverage teams, fee structures, and regulatory requirements. Client success means orchestrating these touchpoints seamlessly while maintaining compliance with MiFID II, Dodd-Frank, SEC regulations, and internal Chinese walls.

The organizational structure usually includes a Global Head of Client Management, regional coverage heads (Americas, EMEA, APAC), sector-aligned coverage bankers, and dedicated client service teams for top-tier accounts. Revenue attribution is notoriously complex — multiple bankers may claim credit for a single deal, creating internal friction. The CS function must also manage league table positioning, pitch coordination, and competitive intelligence to ensure the bank remains top-of-wallet for key clients.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Junior coverage analysts spend 60%+ of time on CRM hygiene, call logs, and pipeline tracking rather than client-facing work |
| 2 | Scale Impact Without Overhead | High | Top-tier banks manage 500+ institutional relationships globally with limited coverage bandwidth; need to deepen engagement without proportional headcount growth |
| 3 | Consolidate Tech Stack with AI | Medium-High | Banks run fragmented stacks (Salesforce, Dealogic, internal CRMs, Bloomberg, Excel trackers) creating data silos that impede cross-sell visibility |

## Prioritized Use Cases

---

### Use Case 1: Institutional Client 360° Coverage Dashboard

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Coverage bankers lack a unified view of client activity across product groups. A managing director in M&A may not know that the same client is in active dialogue with the DCM team about a bond issuance, missing a critical cross-sell opportunity. Client interaction data lives in email threads, call logs in disparate CRMs, deal records in Dealogic, and research consumption data in Bloomberg. Assembling a client review deck for a quarterly coverage meeting takes analysts 15-20 hours per client. Wallet share analysis requires manually pulling league table data and comparing it against estimated addressable wallet — a process prone to errors and political manipulation.

#### The Solution
Build a comprehensive Client 360° board in monday.com Work Management. Each client is an item with subitems for active engagements across product groups. Use mondayDB to aggregate interaction history, deal pipeline status, revenue attribution, research consumption metrics, and competitive positioning. Create connected boards linking client records to deal pipeline, pitch tracker, and team capacity. Use Dashboard views to visualize wallet share penetration, engagement frequency heat maps, and cross-sell opportunity matrices. Integrate with email systems via API for automatic interaction logging.

#### The Outcome
Reduce client review preparation time from 15-20 hours to 2-3 hours per client. Increase cross-sell identification by 40% through unified visibility. Enable coverage bankers to manage 30% more relationships effectively by eliminating manual data aggregation. Improve revenue attribution accuracy, reducing internal disputes and accelerating compensation calculations.

#### Discovery Questions
1. "How do your coverage bankers currently track interactions across product groups for a single institutional client — and how often do cross-sell opportunities slip through the cracks?"
2. "When preparing for a quarterly client review with your top 20 accounts, how many hours does an analyst spend assembling the coverage deck, and how many systems do they pull from?"
3. "How do you currently measure wallet share penetration versus estimated addressable wallet for your institutional clients?"
4. "What happens when two product groups are independently pitching the same client without coordination — how often does that create friction or competitive disadvantage?"
5. "How do you attribute revenue when multiple coverage teams contribute to landing a mandate?"

#### Industry Context
Investment banks categorize clients by tier (Tier 1 = $50M+ annual revenue, Tier 2 = $10-50M, Tier 3 = $1-10M). Coverage models vary: some banks use a "universal banker" approach where one RM coordinates all products; others use product-aligned coverage with a matrix overlay. The "wallet share" concept is central — banks estimate each client's total addressable spend on IB services and track their share versus competitors. League tables (Bloomberg, Refinitiv, Dealogic) are obsessively tracked as competitive benchmarks. MiFID II unbundling requirements in EMEA have added complexity to tracking research-related revenue.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client 360° Coverage Management system. Create a main board called 'Institutional Client Registry' with columns: Client Name (text), Client Tier (dropdown: Tier 1, Tier 2, Tier 3, Prospect), Industry Sector (dropdown: Financial Sponsors, Corporates, Sovereign & Government, Financial Institutions, Real Estate, Infrastructure), Region (dropdown: Americas, EMEA, APAC), Primary Coverage Banker (people), Secondary Coverage (people), Estimated Addressable Wallet ($M) (numbers), Current Wallet Share (%) (numbers), YTD Revenue ($K) (numbers), Last Interaction Date (date), Engagement Status (status: Active Dialogue, Dormant >90 Days, New Prospect, At Risk), Next Action (text). Add subitems for each active engagement with columns: Product Group (dropdown: M&A, ECM, DCM, Leveraged Finance, Restructuring, Derivatives, Prime Brokerage), Deal Stage (status: Origination, Pitch Submitted, Mandate Won, Execution, Closed), Estimated Fee ($K) (numbers), Probability (%) (numbers), Expected Close (date), Competing Banks (text). Create a connected board called 'Interaction Log' with columns: Client (connect to Registry), Contact Person (text), Interaction Type (dropdown: Meeting, Call, Email, Conference, Roadshow, Social), Product Group (dropdown), Date (date), Summary (long text), Follow-Up Required (checkbox), Follow-Up Owner (people), Follow-Up Date (date). Build a Dashboard with widgets: Wallet Share by Client Tier (chart), Revenue Pipeline by Product Group (chart), Interaction Frequency Heat Map (chart), Dormant Clients Alert (table filtered to >90 days), Cross-Sell Opportunities (table showing clients active in <3 product groups). Add automations: When Last Interaction Date is more than 60 days ago, change Engagement Status to 'Dormant >90 Days' and notify Primary Coverage Banker. When a subitem Deal Stage changes to 'Mandate Won', notify the group and create an item in a 'Revenue Recognition' board."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Coverage Intelligence Agent
**Agent Purpose:** Automatically surface cross-sell opportunities and client engagement gaps across product groups.

**Triggers:**
- New deal record created in any product group pipeline
- Client interaction logged after 60+ day dormancy period
- Quarterly client review cycle initiated (scheduled)
- New league table data published (manual trigger)
- Client organizational change detected (integration trigger from news feed)

**Actions:**
- Analyze client's active engagements and identify product groups with zero coverage in past 12 months — generate cross-sell recommendation memo
- Compare wallet share trends quarter-over-quarter and flag clients with declining share for immediate coverage banker review
- Auto-generate client review deck draft by aggregating recent interactions, deal pipeline, wallet share data, and competitive positioning
- Send personalized coverage gap alerts to relevant product group heads when high-potential cross-sell is identified
- Create pre-populated pitch items in the pipeline when cross-sell confidence exceeds threshold
- Escalate to regional coverage head when Tier 1 client shows engagement decline across 2+ consecutive quarters

**Data Required:**
- Client interaction history (email integration, CRM logs)
- Deal pipeline data across all product groups
- Revenue attribution records (finance systems integration)
- League table feeds (Dealogic, Refinitiv API)
- Client organizational chart data

**Autonomy Level:** Human-in-the-Loop
Cross-sell recommendations and client review deck drafts are generated automatically, but coverage bankers review and approve before any client-facing action. Escalation alerts to regional heads are automatic. Revenue attribution suggestions require MD sign-off.

**Example Interaction:**
> The Coverage Intelligence Agent detects that GlobalTech Corp (Tier 1, $120M addressable wallet, current 18% share) completed a $2B bond issuance with the DCM team last month but has had zero M&A advisory engagement in 14 months — despite being in an active acquisition cycle per recent press coverage. The agent generates a cross-sell alert to the M&A sector coverage MD: "GlobalTech Corp completed DCM transaction (Feb 2026). Company announced strategic review of Asia-Pacific portfolio. Zero M&A engagement since Dec 2024. Estimated M&A addressable fees: $15-25M. Recommend outreach within 2 weeks." It simultaneously creates a draft pitch item in the M&A pipeline with pre-populated context and suggests scheduling a joint coverage call with the DCM relationship lead.
>
> During quarterly review prep, the agent automatically compiles a 12-slide coverage summary for each Tier 1 client — pulling YTD revenue by product, interaction timeline, competitive positioning from recent league tables, and a "white space" analysis showing untapped product opportunities. What previously took an analyst 18 hours per client now takes 30 minutes of review and refinement.

---

### Use Case 2: Deal Pipeline & Revenue Attribution Tracker

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banking deal pipelines are managed through a chaotic combination of Excel spreadsheets, Salesforce (poorly adopted by senior bankers), and tribal knowledge. Revenue attribution — determining which teams and individuals contributed to winning a mandate — is one of the most politically charged processes in any bank. Junior analysts spend countless hours reconciling pipeline data across product groups for management reporting. The lack of a single source of truth means that leadership reviews often devolve into debates about pipeline accuracy rather than strategic discussion. Forecast accuracy for quarterly revenue typically sits at 50-60% because pipeline data is stale, probabilities are subjective, and bankers game the system to protect their numbers.

#### The Solution
Deploy monday.com Work Management as the unified deal pipeline across all product groups. Each deal is an item with comprehensive tracking: client, product group, deal type, estimated fees, probability, stage, origination credit splits, execution credit splits, competitive dynamics, and key milestones. Use formulas to calculate weighted pipeline value. Create status automations to enforce stage-gate progression (e.g., cannot move to "Mandate Won" without fee letter upload). Build connected boards for revenue recognition and compensation attribution. Use monday.com Dashboard for real-time pipeline visibility across the entire bank, with filters by region, product, sector, and banker.

#### The Outcome
Reduce pipeline reporting preparation from 20+ analyst hours/week to real-time dashboards. Improve forecast accuracy from 55% to 80%+ through enforced data discipline. Eliminate 90% of revenue attribution disputes through transparent, auditable credit splits agreed at deal origination. Free senior bankers from administrative burden, recovering 5-8 hours/week for client-facing activity.

#### Discovery Questions
1. "How confident is your leadership team in the accuracy of your current deal pipeline — and how often do actual quarterly revenues deviate significantly from forecasts?"
2. "Walk me through what happens when two MDs both claim origination credit on the same mandate. How is that resolved today, and how much senior leadership time does it consume?"
3. "How many different systems does an analyst touch to compile your weekly or monthly pipeline report for the global head of investment banking?"
4. "What stage-gate controls exist in your current pipeline process — can a banker mark a deal as 'high probability' without any supporting documentation?"
5. "How do you currently track competitive dynamics — knowing which other banks are pitching the same client for the same mandate?"

#### Industry Context
Investment banking deals progress through stages: Origination → Pitch/Proposal → Mandate → Execution → Close. Fee structures vary dramatically: M&A advisory fees are typically 0.5-2% of deal value; ECM fees (IPO underwriting) range 3-7%; DCM fees are 0.1-0.5%. Revenue attribution uses "origination credits" (who sourced the deal) and "execution credits" (who delivered it), often split across multiple bankers. Banks track "pipeline coverage ratio" — how much weighted pipeline they need relative to revenue targets (typically 3-4x). League table credit allocation follows specific rules (e.g., bookrunner vs. co-manager splits in capital markets).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Deal Pipeline & Revenue Attribution system. Create a board called 'Global Deal Pipeline' with columns: Deal Name (text), Client (connect to Client Registry board), Product Group (dropdown: M&A Advisory, ECM, DCM, Leveraged Finance, Restructuring, Private Capital, Derivatives Advisory), Deal Type (dropdown: Sell-Side M&A, Buy-Side M&A, IPO, Follow-On, Rights Issue, Investment Grade Bond, High Yield Bond, Leveraged Loan, Restructuring Advisory, Fairness Opinion), Estimated Deal Size ($M) (numbers), Estimated Fee ($K) (numbers), Fee Probability (%) (numbers), Weighted Fee ($K) (formula: Estimated Fee × Fee Probability / 100), Stage (status: Origination, Pitch Preparation, Pitch Submitted, Shortlisted, Mandate Won, Execution, Closed Won, Closed Lost, Withdrawn), Origination Banker (people), Origination Credit % (numbers), Execution Lead (people), Execution Credit % (numbers), Region (dropdown: Americas, EMEA, APAC), Sector (dropdown: TMT, Healthcare, Industrials, Consumer, Energy, FIG, Real Estate), Expected Close Quarter (dropdown: Q1, Q2, Q3, Q4), Competing Banks (text), Win Probability Notes (long text), Last Updated (date). Add subitems for deal milestones: Milestone Name (text), Due Date (date), Owner (people), Status (status: Not Started, In Progress, Complete, Blocked). Create a Dashboard with: Pipeline by Stage (funnel chart), Weighted Pipeline by Product Group (stacked bar), Pipeline Coverage Ratio vs Target (gauge), Win Rate by Product and Region (table), Monthly Pipeline Movement (chart showing additions, progressions, losses). Add automations: When Stage changes to 'Mandate Won', send notification to all stakeholders and create item in 'Fee Recognition Tracker' board. When Stage hasn't changed in 30 days, notify deal owner for update. When Probability is set above 75%, require a note in Win Probability Notes (manual check). Create a separate 'Revenue Attribution' connected board with columns: Deal (connect), Banker (people), Role (dropdown: Originator, Executor, Coverage, Product Specialist), Credit Percentage (numbers), Revenue Attributed ($K) (formula from deal fee × credit %), Quarter Recognized (dropdown)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pipeline Intelligence Agent
**Agent Purpose:** Maintain pipeline hygiene, flag stale deals, and generate accurate revenue forecasts by challenging subjective probability estimates.

**Triggers:**
- Deal stage unchanged for 30+ days
- Quarter-end approaching (T-30, T-14, T-7 days)
- New deal created without required fields populated
- Probability changed by more than 20 percentage points in single update
- Weekly scheduled pipeline review summary

**Actions:**
- Flag stale deals and send escalation notifications to product group heads with specific questions ("Deal X has been in 'Pitch Submitted' for 45 days — is the client still engaged?")
- Generate weekly pipeline movement report: new deals added, stage progressions, deals lost, probability changes, and net pipeline change
- Challenge probability estimates by comparing against historical win rates for similar deal types, sizes, and competitive dynamics
- Auto-calculate pipeline coverage ratios by product group and region, alerting when below 3x target
- Compile quarter-end revenue forecast with confidence intervals based on stage, probability, and historical close rates
- Identify potential revenue attribution conflicts where credit splits exceed 100% or key contributors are missing

**Data Required:**
- Historical deal outcomes (win/loss rates by type, size, region)
- Current pipeline data across all product groups
- Banker capacity and active deal count
- Calendar data for expected close dates
- Finance system integration for actual revenue recognition

**Autonomy Level:** Escalation-Based
Pipeline hygiene alerts and forecast reports are fully automatic. Probability challenges are surfaced as recommendations — bankers can override with justification. Revenue attribution conflict flags require MD-level resolution. Quarter-end forecasts are auto-generated but reviewed by CFO office before distribution.

**Example Interaction:**
> It's March 15th, two weeks before Q1 close. The Pipeline Intelligence Agent generates the Q1 forecast: "Current weighted pipeline for Q1 close: $142M in fees. Based on historical close rates for deals at current stages, adjusted forecast: $98-118M (vs. $130M target). Risk factors: 3 deals totaling $28M weighted have been in 'Shortlisted' stage for 60+ days with no client interaction logged. Recommendation: Coverage heads should prioritize client engagement on these 3 deals this week." The agent also flags that the TMT M&A team has a 2.1x pipeline coverage ratio — below the 3x minimum — and suggests the sector head accelerate origination efforts. For each stale deal, it provides specific context: "Apex Corp sell-side ($15M est. fee, 60% probability) — last client meeting was Jan 28. Similar deals historically have a 35% win rate at this stage duration. Consider downgrading probability or confirming continued engagement."

---

### Use Case 3: Pitch Book & Proposal Coordination

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Creating pitch books is the bane of every investment banking analyst's existence. A single M&A pitch book requires pulling data from 10+ sources (financial databases, company filings, internal precedent transactions, league tables, market data), coordinating content from multiple product specialists, navigating compliance review for marketing materials, and managing multiple revision cycles with senior bankers who provide feedback at 11 PM. The average pitch book takes 40-80 analyst hours to produce. Banks pitch 5-10 deals for every mandate won, meaning the vast majority of this effort results in no revenue. Coordination failures — wrong data, missed deadlines, inconsistent messaging across sections — erode client confidence and lose mandates.

#### The Solution
Build a Pitch Coordination workflow in monday.com Work Management. Each pitch is an item with subitems for every section (executive summary, credentials, market overview, valuation, deal structure, team bios). Track section ownership, draft status, review cycles, and compliance approval. Use Timeline views for production scheduling. Create template boards for common pitch types (sell-side M&A, IPO, DCM). Integrate with document management for version control. Use monday.com automations to route sections through compliance review automatically when marked complete. Build a "Pitch Library" board cataloging reusable components (credentials slides, market overviews, team bios) to reduce duplication.

#### The Outcome
Reduce pitch production time by 40% through templatization and reusable components. Decrease compliance review bottlenecks by 60% through automated routing. Improve pitch quality consistency through standardized workflows. Enable analysts to produce 2x more pitches without additional headcount, directly increasing mandate win probability through higher pitch volume.

#### Discovery Questions
1. "How many pitch books does your team produce per month, and what's the average production time from kick-off to final delivery?"
2. "When a senior banker requests a pitch deck at 6 PM for a 9 AM client meeting, what does that production process look like — and how often does quality suffer under time pressure?"
3. "How much of each new pitch book is truly original content versus recycled credentials, market data, and boilerplate — and do you have a systematic way to reuse previous work?"
4. "How does compliance review work for your marketing materials — is it a bottleneck, and how often does it delay pitch delivery?"
5. "After a pitch is delivered, do you systematically track outcomes and capture learnings about what resonated with the client?"

#### Industry Context
Pitch books in investment banking are highly structured documents, typically 30-60 pages in PowerPoint format. Common sections include: situation overview, credentials/tombstones (previous relevant deals), market landscape, valuation analysis (DCF, comparable companies, precedent transactions), proposed deal structure, financing considerations, and team/timeline. "Tombstones" are mini-case studies of completed deals — banks obsessively curate these as proof of capability. Compliance must review all client-facing materials to ensure no misleading claims, proper disclaimers, and adherence to SEC/FCA marketing rules. The pitch-to-mandate conversion rate varies: 15-25% for competitive M&A processes, higher for relationship-driven mandates.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Pitch Book Production & Coordination system. Create a board called 'Active Pitches' with columns: Pitch Name (text), Client (connect to Client Registry), Product Group (dropdown: M&A, ECM, DCM, LevFin, Restructuring), Pitch Type (dropdown: Competitive Bake-Off, Sole Source, Follow-On, Proactive), Target Delivery Date (date), Pitch Lead MD (people), Production Analyst (people), Status (status: Brief Received, In Production, MD Review, Compliance Review, Final QC, Delivered, Won, Lost), Priority (status: Urgent <24h, Standard 3-5 Days, Proactive), Estimated Hours (numbers), Competing Banks Known (text). Add subitems for sections: Section Name (text: Executive Summary, Credentials, Market Overview, Valuation, Deal Structure, Financing, Team & Process, Appendix), Section Owner (people), Content Status (status: Not Started, Drafting, Data Pull Complete, MD Review, Revisions, Compliance Submitted, Approved, Final), Due Date (date), Data Sources Needed (text), Reusable Component Used (checkbox). Create a connected 'Pitch Library' board: Component Name (text), Type (dropdown: Credentials Slide, Market Overview, Valuation Template, Team Bio, Sector Overview, Boilerplate), Product Group (dropdown), Sector (dropdown), Last Updated (date), Last Used (date), File Link (link), Usage Count (numbers). Create a Dashboard: Active Pitches by Stage (chart), Production Capacity (workload by analyst), Compliance Queue (filtered table), Win Rate by Pitch Type (chart), Average Production Time Trend (chart). Automations: When all subitem statuses are 'Approved', change pitch status to 'Final QC' and notify Pitch Lead. When any subitem changes to 'Compliance Submitted', create item in 'Compliance Review Queue' board. When Pitch Status is 'Won' or 'Lost', prompt for outcome notes. 3 days after delivery with no outcome update, send reminder."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pitch Accelerator Agent
**Agent Purpose:** Accelerate pitch book production by auto-assembling reusable components, pulling relevant data, and managing the production workflow.

**Triggers:**
- New pitch item created with client and product group specified
- Section subitem created or assigned
- Pitch deadline is within 24 hours and sections still in draft
- Pitch outcome recorded (won/lost)
- Weekly pitch pipeline capacity review (scheduled)

**Actions:**
- Auto-search Pitch Library for reusable components matching the pitch's product group, sector, and client type — pre-populate section subitems with suggested templates
- Generate draft credentials section by pulling relevant completed deals from the deal pipeline for the same sector and product group
- Monitor production timeline and send escalation alerts when sections are behind schedule relative to delivery deadline
- After pitch outcome, analyze win/loss patterns and update conversion rate data by pitch type, sector, and competing bank
- Compile weekly capacity report showing analyst workload, upcoming pitch deadlines, and resource conflicts
- Suggest optimal analyst assignment based on current workload, sector expertise, and pitch complexity

**Data Required:**
- Pitch Library (all reusable components)
- Historical deal data for credentials
- Analyst workload and capacity data
- Pitch outcome history
- Compliance review turnaround time data

**Autonomy Level:** Human-in-the-Loop
Component suggestions and draft assembly are automatic but require analyst review before inclusion. Escalation alerts are automatic. Analyst assignment suggestions require MD approval. Credentials section auto-generation requires banker sign-off on deal selection.

**Example Interaction:**
> An MD briefs a new pitch: sell-side M&A advisory for a mid-cap healthcare company, competitive bake-off, due in 4 business days. The Pitch Accelerator Agent immediately springs into action: it identifies 8 relevant healthcare M&A credentials from the past 3 years, pulls the latest healthcare sector market overview (updated 2 weeks ago), finds a recent valuation template used for a similar-sized healthcare deal, and suggests team bios for the proposed deal team. Within 15 minutes of pitch creation, the agent has pre-populated 5 of 8 sections with draft content and assigned the remaining original-content sections to the designated analyst with specific data pull requirements. It estimates 35 hours of production time and flags that the assigned analyst already has 2 other pitches due this week, recommending a secondary analyst for support. The MD sees a production plan before they've even left the briefing meeting.

---

### Use Case 4: Client Onboarding & KYC Workflow

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Know Your Customer (KYC) and client onboarding in investment banking is a regulatory nightmare that directly impacts revenue. Opening a new institutional client account requires collecting beneficial ownership information, conducting sanctions screening, assessing PEP (Politically Exposed Person) status, verifying corporate structure, and obtaining compliance sign-off — a process that typically takes 4-12 weeks. During this time, the bank cannot transact with the client, meaning lost revenue on time-sensitive deals. The process involves multiple teams (front office, compliance, legal, operations) using disconnected systems. Document collection alone can require 50+ back-and-forth exchanges with the client. Periodic KYC reviews (typically annual for high-risk clients, triennial for standard) create another wave of work, often duplicating effort because historical documentation isn't easily accessible.

#### The Solution
Build a Client Onboarding & KYC management system in monday.com. Each onboarding is an item with status tracking through every stage: initial request, document collection, beneficial ownership mapping, sanctions screening, PEP screening, risk assessment, compliance review, account opening, and post-onboarding verification. Use subitems for each required document with status tracking. Create forms for client-facing document requests. Build automations for escalation when stages exceed SLA timelines. Use connected boards to link KYC records to the client registry for ongoing monitoring. Create Dashboard views showing onboarding pipeline, average cycle times, compliance bottlenecks, and upcoming periodic reviews.

#### The Outcome
Reduce average onboarding time from 8 weeks to 3 weeks through workflow automation and parallel processing. Decrease document collection time by 50% through structured request forms. Achieve 100% SLA visibility for compliance teams. Reduce periodic review effort by 60% through historical document reuse. Eliminate revenue leakage from delayed account opening — estimated at $500K-$2M per quarter for mid-tier banks.

#### Discovery Questions
1. "What's your current average time from client engagement approval to first transaction — and how much revenue do you estimate is delayed or lost during that onboarding window?"
2. "How many different teams touch the KYC onboarding process, and do they work in the same system or pass documents between disconnected platforms?"
3. "When it's time for a periodic KYC review, how much of the original documentation and assessment can you reuse versus starting from scratch?"
4. "How do you currently track which onboardings are stuck, where the bottleneck is, and whether you're meeting regulatory SLA requirements?"
5. "Has your bank ever faced regulatory findings or fines related to KYC process deficiencies or documentation gaps?"

#### Industry Context
KYC requirements are governed by the Bank Secrecy Act (BSA), USA PATRIOT Act, EU Anti-Money Laundering Directives (AMLD), and local regulations. Client risk ratings (High, Medium, Standard) determine review frequency and documentation depth. Beneficial ownership requires identifying all individuals with 25%+ ownership (10% for some jurisdictions). Enhanced Due Diligence (EDD) applies to PEPs, clients in high-risk jurisdictions (FATF grey/blacklist), and complex corporate structures. Banks face substantial fines for KYC failures — billions in aggregate across the industry over the past decade. The "Golden Source" concept means KYC data should be maintained centrally and accessible across business lines to avoid duplicative onboarding when the same client engages multiple product groups.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client Onboarding & KYC Management system. Create a board called 'Client Onboarding Pipeline' with columns: Client Legal Name (text), Client Type (dropdown: Corporate, Financial Institution, Fund/SPV, Sovereign, HNW Individual), Requesting Banker (people), Request Date (date), Risk Rating (status: Standard, Medium, High, PEP/EDD Required), Onboarding Stage (status: Intake, Document Collection, Beneficial Ownership Mapping, Sanctions Screening, PEP Screening, Risk Assessment, Compliance Review, Account Opening, Complete, Blocked), Target Completion Date (date), Actual Completion Date (date), Cycle Time Days (formula: Actual Completion - Request Date), Compliance Analyst (people), Jurisdiction (dropdown: US, UK, EU, APAC, Multi-Jurisdiction), Product Groups Requested (dropdown multi-select: M&A, ECM, DCM, Trading, Prime Brokerage), Blocker Description (long text), SLA Status (status: On Track, At Risk, Breached). Add subitems for required documents: Document Name (text: Certificate of Incorporation, Beneficial Ownership Declaration, Board Resolution, Financial Statements, Tax Forms, Sanctions Certification, Source of Wealth Declaration), Status (status: Requested, Received, Under Review, Approved, Rejected/Resubmit), Requested Date (date), Received Date (date), Reviewer (people). Create a 'Periodic Review Calendar' connected board: Client (connect), Review Type (dropdown: Annual, Triennial, Triggered), Due Date (date), Last Review Date (date), Risk Rating (mirror), Status (status: Not Started, In Progress, Pending Compliance, Complete, Overdue), Changes Detected (checkbox). Dashboard with: Onboarding Pipeline by Stage (funnel), Average Cycle Time Trend (line chart), SLA Compliance Rate (gauge), Upcoming Periodic Reviews (table, next 90 days), Blocked Onboardings (filtered table). Automations: When any stage exceeds 5 business days, change SLA Status to 'At Risk' and notify Compliance Analyst. When all document subitems are 'Approved', auto-advance to 'Sanctions Screening'. When Periodic Review Due Date is 30 days away, create review item and notify compliance. When Stage is 'Blocked' for 3+ days, escalate to Compliance Head."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** KYC Orchestrator Agent
**Agent Purpose:** Accelerate client onboarding by automating document tracking, screening coordination, and SLA management.

**Triggers:**
- New onboarding request created
- Document subitem status changed to 'Received'
- Stage exceeds configured SLA threshold
- Periodic review due date approaching (T-30 days)
- Sanctions list updated (external data feed)

**Actions:**
- Generate client-specific document checklist based on client type, risk rating, and jurisdiction — pre-populate subitems with required documents
- Auto-send structured document request forms to client contacts with clear instructions and deadlines
- When documents are received, perform initial validation (completeness, format, date currency) and route to appropriate reviewer
- Monitor SLA timelines and generate daily compliance dashboard with at-risk onboardings and recommended actions
- For periodic reviews, compare current client data against original KYC file and flag material changes requiring enhanced review
- Cross-reference new client data against updated sanctions lists and generate screening reports

**Data Required:**
- Regulatory document requirements by jurisdiction and client type
- Client contact information for document requests
- Sanctions databases (OFAC, EU, UN consolidated lists)
- Historical KYC records for periodic review comparison
- SLA configuration by risk rating and jurisdiction

**Autonomy Level:** Escalation-Based
Document checklist generation and request distribution are fully automatic. Initial document validation is automatic with human review for final approval. Sanctions screening results are auto-generated but require compliance officer sign-off. SLA escalations are automatic. No client account can be opened without human compliance approval — this is a regulatory requirement.

**Example Interaction:**
> A coverage banker creates an onboarding request for a new institutional client — a Luxembourg-domiciled fund of funds seeking prime brokerage and DCM services. The KYC Orchestrator Agent immediately identifies this as a High-risk profile (fund structure + Luxembourg jurisdiction) requiring Enhanced Due Diligence. It generates a 22-item document checklist specific to fund vehicles in EU jurisdictions, creates all subitems with regulatory citations, and sends a structured intake form to the client's COO. Within the first hour, the agent has also queued the entity for sanctions screening across OFAC, EU, and UN lists, identified two connected entities that require parallel screening, and calculated a target completion date of 25 business days (adjusted for EDD requirements). As documents trickle in over the next 2 weeks, the agent validates each one, flags a financial statement that's more than 12 months old (requiring updated version), and automatically advances the onboarding through stages as checkpoints are cleared. The compliance analyst sees a clean dashboard showing exactly what's pending, what's approved, and what needs attention.

---

### Use Case 5: Client Event & Roadshow Coordination

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks run hundreds of client events annually — investor conferences, non-deal roadshows (NDRs), management access days, sector seminars, and bespoke client entertainment. Coordinating these events involves matching institutional investor interest with corporate management availability, booking venues, managing travel logistics, tracking RSVPs, producing briefing materials, and conducting post-event follow-up. A single investor conference can involve 200+ meetings over 3 days, requiring military-precision scheduling. Non-deal roadshows — where a bank facilitates meetings between a public company's management and institutional investors — are critical relationship-building tools but logistically nightmarish. The teams managing these events typically juggle spreadsheets, email chains, and CRM systems, frequently resulting in double-bookings, missed investor preferences, and inadequate post-event follow-up that squanders the relationship capital built during the event.

#### The Solution
Build an Event & Roadshow Management system in monday.com. Create boards for event planning (logistics, venues, speakers), attendee management (RSVPs, preferences, meeting requests), scheduling (1-on-1 meeting grids, group sessions), and post-event follow-up (action items, client feedback, pipeline opportunities). Use Timeline views for event production schedules. Integrate forms for RSVP collection and meeting requests. Build automation workflows for confirmation emails, briefing packet distribution, and post-event survey triggers. Create a "Client Interaction" integration that automatically logs event attendance into the Client 360° system.

#### The Outcome
Reduce event coordination labor by 50% through automated scheduling and communication workflows. Increase meeting density at investor conferences by 25% through optimized scheduling algorithms. Improve post-event follow-up completion from 40% to 90% through automated action item tracking. Generate measurable pipeline from events — track which client interactions at events convert to mandates within 12 months.

#### Discovery Questions
1. "How many client events and non-deal roadshows does your bank facilitate annually, and what does the coordination process look like from planning to post-event follow-up?"
2. "At your last investor conference, how were 1-on-1 meeting schedules created — and how many scheduling conflicts or missed preferences did you have to resolve manually?"
3. "After a major client event, what percentage of action items and follow-ups actually get completed within the first two weeks?"
4. "Can you currently track the ROI of your events — specifically, which client interactions at events eventually led to deal mandates?"
5. "How do you capture and utilize investor preferences (sector focus, deal size interest, meeting format preference) across events over time?"

#### Industry Context
Non-deal roadshows (NDRs) are a core IB service — banks arrange meetings between corporate management teams and institutional investors without a specific transaction. This builds relationships and generates future deal flow. Investor conferences are major productions: banks like Goldman Sachs, JP Morgan, and Morgan Stanley host marquee annual conferences that attract hundreds of companies and thousands of investors. The "1-on-1 meeting" scheduling at these events is incredibly complex — matching investor requests with corporate availability while respecting time zones, travel schedules, and relationship priorities. MiFID II in EMEA has added complexity by requiring banks to track and potentially charge for corporate access services (research unbundling).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client Event & Roadshow Management system. Create a board called 'Events Calendar' with columns: Event Name (text), Event Type (dropdown: Investor Conference, Non-Deal Roadshow, Management Access Day, Sector Seminar, Client Dinner, Bespoke Meeting Series), Date Range (timeline), Location (text), Hosting Product Group (dropdown), Event Lead (people), Logistics Coordinator (people), Status (status: Planning, Invitations Sent, RSVPs Open, Scheduling, Confirmed, Live, Post-Event, Complete), Budget ($) (numbers), Expected Attendees (numbers), Confirmed Attendees (numbers), Post-Event Actions Completed (%) (numbers). Create a connected 'Attendee Management' board: Attendee Name (text), Company (text), Role (dropdown: Corporate Presenter, Institutional Investor, Internal Banker, VIP Guest), Event (connect to Events Calendar), RSVP Status (status: Invited, Confirmed, Declined, Waitlisted, No-Show), Meeting Preferences (long text: sectors, companies, format), Dietary Requirements (text), Travel Assistance Needed (checkbox), Briefing Packet Sent (checkbox). Create a '1-on-1 Meeting Grid' board: Time Slot (text), Room (text), Corporate Presenter (connect to Attendees), Investor Attendee (connect to Attendees), Meeting Status (status: Scheduled, Confirmed, Completed, Cancelled, No-Show), Post-Meeting Notes (long text), Follow-Up Action (text), Follow-Up Owner (people), Follow-Up Completed (checkbox). Dashboard with: Event Calendar (timeline), RSVP Response Rates (chart), Meeting Grid Utilization (chart), Post-Event Follow-Up Completion (gauge), Pipeline Generated from Events (chart, connected to deal pipeline). Automations: When RSVP changes to 'Confirmed', send confirmation email and trigger briefing packet preparation. When Event Status changes to 'Post-Event', create follow-up action items for all meeting participants. When Follow-Up is not completed 14 days post-event, escalate to Event Lead."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Event Intelligence Agent
**Agent Purpose:** Optimize event meeting schedules, automate attendee communications, and track event-to-pipeline conversion.

**Triggers:**
- New event created with dates and type specified
- RSVP received or meeting preference submitted
- Event status changes to scheduling phase
- Event concludes (status → Post-Event)
- Quarterly event ROI review (scheduled)

**Actions:**
- Analyze investor meeting preferences and corporate presenter availability to generate optimized 1-on-1 meeting schedules maximizing meeting density and preference match rates
- Generate personalized briefing packets for each attendee combining relevant research notes, presenter backgrounds, and meeting schedules
- Send automated pre-event communications (confirmation, logistics, schedule) and post-event thank-you notes with meeting summaries
- Track post-event follow-up completion and generate weekly status reports for event leads
- Analyze event-to-pipeline conversion by tracking which client interactions at events result in deal mandates within 12 months
- Compile historical investor preference profiles across events to improve future scheduling

**Data Required:**
- Attendee RSVP and preference data
- Corporate presenter availability and topic areas
- Room/venue capacity and logistics data
- Historical meeting preference and attendance data
- Deal pipeline data for ROI tracking

**Autonomy Level:** Human-in-the-Loop
Meeting schedule generation is automatic but requires event coordinator review before distribution. Communications (confirmations, reminders) are automatic. Briefing packet assembly is automatic but requires banker review for sensitive content. Follow-up escalations are automatic.

**Example Interaction:**
> The annual Healthcare Investor Conference is 3 weeks out with 45 corporate presenters and 180 confirmed institutional investors. The Event Intelligence Agent has collected meeting preferences from all investors — 1,200+ individual meeting requests. It generates an optimized schedule across 3 days, 12 meeting rooms, and 8 time slots per day, achieving a 92% preference match rate (vs. 75% when done manually). It flags 15 scheduling conflicts that require human judgment (e.g., two top-tier investors both requesting the same company at the same time slot) and suggests resolution options ranked by relationship priority. Simultaneously, it generates 180 personalized briefing packets, each containing the investor's specific meeting schedule, one-page summaries of each company they're meeting, relevant recent research notes, and logistical details. Post-conference, it creates 540 follow-up action items across the coverage team and tracks completion daily, escalating when items go stale.

---

### Use Case 6: Competitive Intelligence & Market Positioning Tracker

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks live and die by league table rankings and competitive positioning. Coverage bankers need to know which competitors are pitching their clients, what fee levels competitors are quoting, how the bank's market share is trending by product and sector, and where competitors are winning mandates. This intelligence is scattered across individual banker knowledge, Dealogic/Refinitiv league table data, industry press, and informal networks. There's no systematic way to aggregate competitive intelligence across the firm, meaning strategic decisions about where to invest coverage resources are based on incomplete data. When a bank loses a mandate, the post-mortem is often superficial — "they went with Goldman" — without understanding why or what could be improved.

#### The Solution
Build a Competitive Intelligence hub in monday.com. Create boards for tracking competitive encounters (which banks are pitching which clients), win/loss analysis (detailed post-mortems on lost mandates), market share tracking (league table data by product, sector, region), and competitor profiles (key personnel, strategy shifts, recent hires). Use forms for bankers to quickly log competitive sightings. Build Dashboard views showing competitive trends, win rates by competitor, and market share movement. Connect to the deal pipeline to automatically populate competitive data when deals are won or lost.

#### The Outcome
Build an institutional competitive memory that persists beyond individual banker tenure. Increase competitive win rate by 10-15% through better preparation and pricing intelligence. Enable strategic resource allocation by identifying product/sector combinations where the bank is underperforming. Reduce time spent on competitive analysis for pitches by 40% through centralized, searchable intelligence.

#### Discovery Questions
1. "When you lose a mandate to a competitor, how thorough is your win/loss analysis — and is that intelligence captured in a way that benefits the broader firm?"
2. "How do your bankers currently share competitive intelligence — if an MD in Chicago learns that a competitor is aggressively pitching a client in London, how quickly does that information flow?"
3. "When preparing a pitch, how do bankers assess which competitors they're likely facing and what fee levels might be competitive?"
4. "How do you use league table data strategically — is it just a backward-looking scorecard, or does it actively inform where you invest coverage resources?"

#### Industry Context
League tables are the scorecards of investment banking — rankings by deal volume and value published by Dealogic, Refinitiv, and Bloomberg. Banks obsess over rankings because clients use them as a selection criterion ("we want a top-3 bookrunner"). League table positioning can be gamed through fee discounts, co-manager positions, and creative deal attribution. Key competitive dynamics vary by product: M&A advisory is relationship-driven (top 5 banks dominate); ECM/DCM is more transactional and fee-sensitive; leveraged finance involves syndication relationships. Competitor intelligence includes tracking senior banker lateral moves — when a top MD leaves Goldman for Jefferies, their client relationships often follow.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Competitive Intelligence & Market Positioning system. Create a board called 'Competitive Sightings' with columns: Date (date), Client (connect to Client Registry), Product Group (dropdown: M&A, ECM, DCM, LevFin, Restructuring), Competitor Bank (dropdown: Goldman Sachs, JP Morgan, Morgan Stanley, Bank of America, Citi, Barclays, Deutsche Bank, UBS, Credit Suisse, Jefferies, Lazard, Evercore, PJT, Centerview, Moelis, Rothschild, Other), Source (dropdown: Client Mention, Market Intel, Press/News, Banker Network, RFP Process), Context (long text), Reported By (people), Outcome (status: Pending, We Won, Competitor Won, Withdrawn, Unknown). Create a 'Win/Loss Analysis' board: Deal Name (text), Client (connect), Product Group (dropdown), Competing Banks (text), Outcome (status: Won, Lost, No Decision), Primary Reason (dropdown: Relationship, Fees, Credentials, Team, Idea Quality, Execution Capability, Other), Fee Quoted ($K) (numbers), Winning Fee Estimate ($K) (numbers), Detailed Analysis (long text), Lessons Learned (long text), Analyst (people), Date (date). Create a 'League Table Tracker' board: Period (dropdown: Q1, Q2, Q3, Q4, Full Year), Year (numbers), Product Group (dropdown), Region (dropdown), Our Rank (numbers), Our Deal Count (numbers), Our Volume ($B) (numbers), #1 Competitor (text), #1 Volume ($B) (numbers), Market Share % (numbers), YoY Change (numbers), Source (dropdown: Dealogic, Refinitiv, Bloomberg). Dashboard with: League Table Trends (line chart by product over time), Win Rate by Competitor (bar chart), Loss Reasons Analysis (pie chart), Competitive Sighting Frequency (heat map by competitor × product), Market Share vs Top 3 (comparison chart). Automations: When a deal in the pipeline changes to 'Closed Lost', create item in Win/Loss Analysis board and assign to deal originator for completion within 5 business days. Monthly reminder to update league table data."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Competitive Radar Agent
**Agent Purpose:** Aggregate competitive intelligence across the firm and generate actionable insights for coverage and pitch strategy.

**Triggers:**
- New competitive sighting logged
- Deal closed as lost
- League table data updated
- Pre-pitch preparation initiated (connected to Pitch Coordination)
- Monthly competitive review (scheduled)

**Actions:**
- When a pitch is initiated, automatically compile competitive dossier: recent sightings of likely competitors for this client/product, historical win/loss record against those competitors, fee benchmarks from similar deals
- Analyze loss patterns to identify systemic weaknesses (e.g., "We've lost 6 of 8 healthcare M&A pitches against Centerview — primary reasons: senior team credibility and idea quality")
- Generate monthly competitive briefing summarizing market share movements, notable competitor wins/losses, and strategic implications
- Track senior banker movements at competitors and flag potential relationship risks/opportunities
- Alert coverage bankers when a competitor is sighted pitching one of their key clients

**Data Required:**
- Competitive sighting logs from bankers
- Win/loss analysis records
- League table data feeds
- Industry news and press (competitor hires, deal announcements)
- Internal deal pipeline and outcome data

**Autonomy Level:** Fully Autonomous
Competitive intelligence aggregation, analysis, and reporting are fully automatic. Alerts and briefings are distributed without human approval. Competitive dossiers for pitch preparation are auto-generated and attached to pitch items. The agent cannot take any external action — all intelligence stays internal.

**Example Interaction:**
> The M&A coverage head for the Technology sector opens their Monday morning briefing from the Competitive Radar Agent: "Weekly TMT M&A Intelligence Brief — Week of Feb 16, 2026. Key developments: (1) Morgan Stanley hired Sarah Chen from our TMT group — she covered 4 of our Tier 1 accounts. Recommend immediate relationship reinforcement outreach to those clients. (2) Evercore won the MegaSoft divestiture mandate — we pitched and lost. Win/Loss analysis shows they proposed an innovative dual-track process that we didn't consider. Lesson captured and circulated to TMT team. (3) Our TMT M&A league table ranking slipped from #3 to #5 in Q4 — driven by 2 large deals where we were displaced as lead advisor. Coverage gap identified: we have no active dialogue with 3 of the top 10 TMT acquirers by deal volume. (4) Upcoming competitive risk: Goldman Sachs is reportedly pitching NovaTech (our Tier 1 client) for a potential IPO — sighting logged by our ECM desk yesterday."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Wallet Share | Percentage of a client's total investment banking spend captured by the bank |
| League Table | Rankings of banks by deal volume/value published by Dealogic, Refinitiv, Bloomberg |
| Tombstone | Mini-case study of a completed deal used in pitch books as credentials |
| NDR (Non-Deal Roadshow) | Meetings arranged between corporate management and investors without a specific transaction |
| KYC (Know Your Customer) | Regulatory process for verifying client identity and assessing risk |
| PEP (Politically Exposed Person) | Individual in a prominent public function requiring enhanced due diligence |
| EDD (Enhanced Due Diligence) | Deeper investigation required for high-risk clients |
| Origination Credit | Revenue attribution for sourcing/winning a deal mandate |
| Coverage Banker | Relationship manager responsible for overall client relationship across products |
| Bake-Off | Competitive pitch process where multiple banks present to win a mandate |
| Mandate | Formal engagement of a bank to execute a specific transaction |
| Bookrunner | Lead bank on a capital markets transaction responsible for managing the offering |
| Chinese Wall | Information barrier between different divisions to prevent conflicts of interest |
| MiFID II | EU regulation affecting research unbundling and corporate access charges |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Head of Investment Banking | Overall P&L, strategy, resource allocation | Decision-maker |
| Coverage/Relationship MD | Client relationship ownership, cross-sell coordination | Decision-maker |
| Product Group Head (M&A, ECM, DCM) | Product-specific revenue, pitch quality, execution | Decision-maker |
| Chief Compliance Officer | KYC/AML policy, regulatory adherence | Veto power |
| COO / Head of IB Operations | Technology, process efficiency, cost management | Influencer / Budget holder |
| VP/Director Coverage Banker | Day-to-day client management, pipeline management | Influencer / Champion |
| Analyst / Associate | Data aggregation, pitch production, pipeline maintenance | End user / Champion |
| Head of Client Management | CRM strategy, client segmentation, event coordination | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | CRM systems, data infrastructure, compliance technology | monday.com as unified platform replacing fragmented CRM/pipeline tools |
| Operations | Trade settlement, account onboarding, middle-office processes | Extend workflow automation from front-office to middle-office |
| Sales (Capital Markets) | ECM/DCM syndication, investor relationship management | Unified investor database across advisory and capital markets |
| Legal | Deal documentation, regulatory filings, compliance review | Connected workflow from pitch approval through deal closing documentation |
| HR | Talent management, compensation planning (revenue attribution feeds comp) | Integrated performance tracking from deal attribution to compensation |
| Finance | Revenue recognition, fee billing, P&L reporting | Real-time revenue visibility from pipeline through recognition |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce Financial Services Cloud | Enterprise CRM for banking relationships | Poorly adopted by senior bankers due to complexity; monday.com offers simpler UX that MDs actually use |
| Dealogic / Refinitiv | League table data and deal intelligence | Data source, not workflow tool — monday.com complements rather than competes |
| DealCloud (Intapp) | Purpose-built IB CRM and pipeline management | Expensive, rigid, limited workflow customization — monday.com offers more flexibility at lower cost |
| Dynamo / Altvia | PE/IB deal flow and relationship management | Niche tools with limited broader workflow capability — monday.com provides unified platform |
| Excel/SharePoint | Default pipeline and tracking tool in most banks | Universal pain point — everyone knows it's inadequate but nothing has been compelling enough to replace it |
| Ipreo (IHS Markit) | Capital markets workflow and investor targeting | Acquired by S&P Global, focus narrowing; monday.com covers broader workflow needs |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "Our data is too sensitive for cloud-based tools" | monday.com offers enterprise-grade security (SOC 2 Type II, ISO 27001, HIPAA), data residency options, and SSO/SAML integration. Many regulated financial institutions already use monday.com. We can discuss specific compliance requirements with our security team. |
| "Senior bankers won't adopt another CRM" | That's exactly the problem we solve. monday.com's visual, intuitive interface has dramatically higher adoption rates than traditional CRMs. We've seen MDs actually use it because it surfaces value (pipeline visibility, competitive intel) without requiring data entry burden — that's handled by junior team members and automations. |
| "We've already invested heavily in Salesforce" | We're not asking you to rip out Salesforce. monday.com excels as the workflow and collaboration layer that sits on top of your data infrastructure. Many banks use Salesforce as the system of record but monday.com as the system of action — where work actually gets coordinated. |
| "Compliance won't approve a new tool for KYC data" | We support the compliance conversation with our security documentation, and we can architect a solution where monday.com manages the workflow and status tracking while sensitive documents remain in your approved document management system. Workflow orchestration doesn't require moving regulated data. |
| "We need something purpose-built for investment banking" | Purpose-built IB tools (DealCloud, etc.) are rigid and expensive. monday.com's flexibility means you can build exactly the workflows you need — and change them as your processes evolve. You're not locked into someone else's opinion of how IB should work. Your best analysts know your processes better than any vendor. |

## Proof Points
*(To be populated with customer references)*
- [Financial services firms using monday.com for deal pipeline management]
- [Banks that consolidated CRM and workflow tools onto monday.com]
- [Compliance-approved implementations in regulated financial institutions]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
