# Advertising & Marketing × Sustainability Playbook

## Overview

Sustainability departments within advertising and marketing agencies have emerged as strategic functions in the last several years, driven by client demand for ESG-aligned campaigns, regulatory pressure around greenwashing claims, and internal corporate commitments to reduce environmental footprints across operations. In mid-to-large agencies (500+ employees), sustainability teams typically sit as a cross-functional unit reporting to the COO or a dedicated Chief Sustainability Officer, bridging creative, media buying, production, and corporate operations.

These teams are responsible for measuring and reducing the carbon footprint of ad production (shoots, travel, digital infrastructure), ensuring campaign messaging meets increasingly strict advertising standards around environmental claims (FTC Green Guides, EU Green Claims Directive), and helping clients navigate their own sustainability storytelling. They also manage the agency's own ESG reporting — tracking scope 1-3 emissions, DEI metrics, and community impact for B Corp certifications, CDP disclosures, and client RFPs that now routinely include sustainability questionnaires.

The challenge is acute: sustainability teams in agencies are chronically understaffed (often 2-5 people for a global agency), rely on manual data collection from dozens of departments and production partners, and face pressure from both clients demanding sustainable production options and regulators cracking down on unsubstantiated green claims. The work is high-stakes, cross-functional, and data-intensive — yet most agencies still manage it with spreadsheets, email chains, and quarterly heroics.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Tiny sustainability teams must track emissions, compliance, and reporting across hundreds of campaigns and dozens of offices without headcount growth |
| 2 | Replace or Radically Augment Headcount | Medium-High | Manual data collection from production partners, vendors, and internal teams consumes 60-70% of sustainability team bandwidth — AI can automate most of it |
| 3 | Consolidate Tech Stack with AI | Medium | Agencies cobble together carbon calculators, ESG reporting tools, compliance trackers, and project management — monday.com can unify these workflows |

## Prioritized Use Cases

---

### Use Case 1: Campaign Carbon Footprint Tracker

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every campaign has a carbon footprint — travel for shoots, energy for studios, server load for digital delivery, print runs, event builds. Clients increasingly demand carbon estimates *before* production and verified actuals *after*. Most agencies estimate manually using spreadsheets, often missing major emission sources. A single global campaign can involve 15+ production partners across 8 countries, each reporting in different formats (or not at all). The sustainability team spends weeks chasing data that's stale by the time it's compiled.

#### The Solution
monday.com Work Management with a Campaign Carbon Tracking workspace. Each campaign gets a group with items for every production element (shoot days, travel legs, digital delivery, print runs, events). Number columns capture estimated vs. actual emissions (kgCO2e). Formula columns auto-calculate totals by scope. Integrations pull data from travel booking systems and production management tools. Dashboards show real-time carbon budgets per campaign, per client, per quarter. Status columns flag campaigns exceeding carbon thresholds.

#### The Outcome
- 80% reduction in time spent collecting production carbon data
- Real-time carbon budget visibility for every active campaign
- Client-ready carbon reports generated in minutes, not weeks
- Ability to compare carbon intensity across campaign types to guide greener production choices

#### Discovery Questions
1. "How do you currently estimate the carbon footprint of a campaign before production begins — and how accurate are those estimates compared to actuals?"
2. "When a client asks for a sustainability report on their campaign, how long does it take your team to compile it?"
3. "Are your production partners required to report emissions data, and if so, how do they submit it?"
4. "Have you ever lost a pitch or RFP because you couldn't demonstrate sustainable production practices?"
5. "How do you track scope 3 emissions from freelancers, vendors, and subcontractors across campaigns?"

#### Industry Context
Ad production carbon accounting follows the AdGreen framework (UK) or similar methodologies. Key emission categories: travel & transport, energy (studio/office), materials & set builds, post-production (render farms, cloud storage), distribution (broadcast, digital, print). Agencies pursuing Ad Net Zero commitments must report annually. Clients like Unilever, P&G, and L'Oréal now include sustainability requirements in agency contracts and pitch briefs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Campaign Carbon Tracker board. Groups: Pre-Production, Production, Post-Production, Distribution. Columns: Campaign Name (text), Client (dropdown: list of clients), Production Element (text), Transport Mode (dropdown: Air, Rail, Road, Sea, None), Estimated kgCO2e (numbers), Actual kgCO2e (numbers), Variance % (formula: (Actual-Estimated)/Estimated*100), Scope (dropdown: Scope 1, Scope 2, Scope 3), Data Source (dropdown: Partner Report, Estimate, Calculated), Status (status: Pending Data, In Progress, Verified, Flagged), Owner (people), Due Date (date). Add automations: When Status changes to Flagged, notify the Sustainability Lead. When Actual kgCO2e exceeds Estimated by more than 20%, change Status to Flagged. Create a Dashboard view with widgets: total kgCO2e by campaign (chart), Scope breakdown (pie chart), campaigns exceeding budget (table filtered by Flagged status), month-over-month trend (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CarbonPulse
**Agent Purpose:** Automatically collect, validate, and compile carbon emission data from campaign production activities.

**Triggers:**
- New campaign item created in production board
- Production partner submits data via monday.com form
- Status changes to "Production Complete"
- Weekly schedule (Mondays) for data gap detection
- Client requests carbon report (manual trigger)

**Actions:**
- Parse incoming partner emission reports and populate kgCO2e columns
- Flag inconsistencies (e.g., 10-hour shoot reported with zero energy consumption)
- Calculate scope 1/2/3 breakdowns using AdGreen emission factors
- Generate client-ready carbon summary documents
- Send automated reminders to partners with missing data
- Escalate campaigns exceeding carbon thresholds to sustainability lead

**Data Required:**
- Campaign briefs and production schedules (from production management board)
- Partner emission report submissions (forms/email integration)
- Emission factor databases (AdGreen, DEFRA, EPA)
- Travel booking data (integration with Concur, Egencia, or similar)

**Autonomy Level:** Human-in-the-Loop
CarbonPulse autonomously collects and calculates data but requires human verification before reports are sent to clients. Flagged anomalies require human review.

**Example Interaction:**
> CarbonPulse detects that the "Summer Refresh" campaign for PepsiCo has completed its 3-day shoot in Barcelona. It pulls travel data showing 14 crew members flew from London (economy class) and 3 from New York (business class), calculates flight emissions using DEFRA factors, adds studio energy estimates based on the production company's average consumption data, and flags that the total is tracking 34% over the pre-production estimate.
>
> It sends a notification to the sustainability coordinator: "Summer Refresh carbon tracking update: 12.4 tCO2e actual vs. 9.2 tCO2e estimated. Primary driver: transatlantic flights for NY-based talent. Recommend reviewing post-production plan — shifting color grading to London facility would save ~0.8 tCO2e in additional travel." The coordinator reviews, approves the figures, and CarbonPulse updates the client dashboard automatically.

---

### Use Case 2: Greenwashing Compliance & Claims Review

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Advertising regulators worldwide are aggressively targeting greenwashing. The FTC (US), ASA (UK), and ARPP (France) have all tightened rules on environmental claims in advertising. A single misleading sustainability claim can result in campaign bans, fines, and devastating reputational damage — for both the agency and the client. Sustainability teams must review every piece of creative that contains environmental claims, but they're bottlenecked: a large agency might produce 500+ assets per week, many containing sustainability messaging. Reviews are ad hoc, often happening too late in the production cycle, and rely on the sustainability team catching every instance of "eco-friendly," "carbon neutral," or "sustainable" across hundreds of assets.

#### The Solution
monday.com Work Management as a Claims Review Pipeline. Creative teams submit assets containing environmental claims via a form that captures the claim text, supporting evidence, target market, and regulatory jurisdiction. Items flow through a Kanban board with stages: Submitted → Under Review → Evidence Check → Approved / Rejected / Revise. Dropdown columns track claim type (carbon, materials, sourcing, biodiversity), jurisdiction (US FTC, UK ASA, EU UCPD), and risk level. File columns hold supporting documentation. Automations route high-risk claims to legal review.

#### The Outcome
- 100% of environmental claims reviewed before publication (vs. ~40% ad hoc coverage)
- 70% faster review turnaround through structured submission and routing
- Complete audit trail for regulatory defense
- Reduced risk of campaign bans and fines (ASA banned 40% more ads for greenwashing in 2024 vs. 2023)

#### Discovery Questions
1. "What percentage of your creative output contains environmental or sustainability claims, and what's your current review process for those?"
2. "Have any of your campaigns been challenged or banned by an advertising regulator for misleading environmental claims?"
3. "When a creative team uses terms like 'eco-friendly' or 'sustainable,' who is responsible for verifying the claim — and at what stage of production?"
4. "How do you track which regulatory frameworks apply to campaigns running in multiple markets?"
5. "Do you maintain a library of pre-approved sustainability claims that creative teams can reference?"

#### Industry Context
Key regulatory frameworks: FTC Green Guides (US), ASA/CAP Code Section 11 (UK), EU Green Claims Directive (2024+), ARPP Climate Recommendations (France), ACCC greenwashing guidance (Australia). Common violations: vague claims ("eco-friendly" without specifics), unsubstantiated carbon neutral claims, misleading imagery (nature imagery for polluting products), hidden trade-offs. The International Chamber of Commerce (ICC) Advertising Code also provides global guidance. Major holding companies (WPP, Publicis, Omnicom) have all issued internal greenwashing policies requiring sustainability review.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Greenwashing Claims Review board. Groups: Pending Review, Under Review, Evidence Check, Approved, Rejected, Revise. Columns: Asset Name (text), Client (dropdown), Campaign (text), Claim Text (long text), Claim Type (dropdown: Carbon/Emissions, Materials/Packaging, Sourcing/Supply Chain, Biodiversity, General Environmental, Social/DEI), Jurisdiction (dropdown: US FTC, UK ASA, EU UCPD, France ARPP, Australia ACCC, Multi-Market), Risk Level (status: Low, Medium, High, Critical), Supporting Evidence (files), Reviewer (people), Submitted By (people), Submit Date (date), Review Deadline (date), Decision (status: Approved, Rejected, Revise, Escalated to Legal), Decision Notes (long text). Automations: When Risk Level is Critical, assign to Legal Reviewer and notify Sustainability Lead. When new item created, set Review Deadline to 3 business days from Submit Date. When Decision changes to Rejected, notify Submitted By with Decision Notes. Create a Dashboard with: claims by risk level (chart), approval rate by client (chart), average review time (number widget), overdue reviews (table filtered by past-due deadline)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** GreenGuard
**Agent Purpose:** Pre-screen advertising creative for potential greenwashing risks and flag claims requiring sustainability team review.

**Triggers:**
- New asset uploaded to creative review board
- Campaign brief contains sustainability-related keywords
- Creative team manually requests green claims check
- Weekly scan of all in-production campaigns for unreviewed claims

**Actions:**
- Scan asset text/copy for environmental claim keywords and phrases
- Cross-reference claims against pre-approved claims library
- Assign risk score based on claim specificity, jurisdiction, and evidence availability
- Auto-approve low-risk claims matching pre-approved templates
- Route medium/high-risk claims to sustainability reviewer with jurisdiction-specific guidance
- Generate regulatory compliance checklist tailored to target markets

**Data Required:**
- Pre-approved claims library (maintained by sustainability team)
- Regulatory frameworks database (FTC, ASA, EU GCD requirements)
- Campaign briefs and target market data
- Historical review decisions for pattern matching

**Autonomy Level:** Escalation-Based
GreenGuard auto-approves claims matching pre-approved templates verbatim. All novel claims, high-risk categories, and multi-market campaigns escalate to human review with AI-generated risk assessment.

**Example Interaction:**
> A creative team uploads final assets for a client's new product launch. The hero banner reads "Made with 100% recycled ocean plastic." GreenGuard detects the environmental claim, checks it against the pre-approved library (no match), identifies it as a Materials/Packaging claim, and flags it as Medium-High risk because: (1) "100%" is an absolute claim requiring robust evidence, (2) "ocean plastic" is a specific sourcing claim regulated differently than general recycled content, (3) the campaign targets UK and EU markets where the ASA and EU Green Claims Directive require life-cycle evidence.
>
> GreenGuard creates a review item with a pre-populated checklist: "☐ Certificate of recycled content from supplier ☐ Ocean plastic sourcing verification (OBP or similar) ☐ Life-cycle assessment data ☐ UK ASA Section 11.1 compliance check ☐ EU GCD substantiation requirements." It assigns the item to the sustainability reviewer with a note: "Similar claim was challenged by ASA in Case #A23-1156 (competitor brand) — recommend reviewing precedent."

---

### Use Case 3: ESG Reporting & B Corp Compliance Dashboard

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Agencies pursuing or maintaining B Corp certification, responding to client ESG questionnaires, or filing CDP/GRI disclosures must collect data from across the entire organization — HR (DEI metrics, benefits, turnover), Finance (charitable giving, pay equity), Operations (energy, waste, water), Procurement (supplier diversity, ethical sourcing), and every department in between. Data collection for the annual B Impact Assessment alone takes 200-400 hours at a mid-size agency. Client RFPs increasingly include sustainability questionnaires (EcoVadis, custom ESG surveys) that require the same data in different formats. The sustainability team becomes a permanent bottleneck, chasing the same data from the same people in slightly different formats multiple times per year.

#### The Solution
monday.com Work Management as a centralized ESG Data Hub. A master board maps every data point required across all reporting frameworks (B Corp BIA, CDP, GRI, EcoVadis, client questionnaires). Each item represents a specific metric (e.g., "Scope 2 emissions — electricity kWh by office"). People columns assign data owners. Date columns track collection deadlines. Status columns show: Not Started → Data Requested → Submitted → Verified → Published. Number columns capture current period vs. prior period values. Automations send collection reminders, flag overdue items, and notify verifiers. Dashboards provide real-time completion tracking by framework and department.

#### The Outcome
- 60% reduction in ESG data collection time through structured workflows and automation
- Single source of truth for all sustainability metrics across frameworks
- Real-time visibility into reporting completeness (vs. scrambling at year-end)
- Ability to respond to client ESG questionnaires in days, not weeks

#### Discovery Questions
1. "How many distinct sustainability/ESG reporting frameworks or questionnaires does your agency respond to annually?"
2. "What percentage of your B Impact Assessment data collection is manual — and how many hours does it consume?"
3. "When a client sends an ESG questionnaire as part of an RFP, how quickly can you turn it around?"
4. "Do different departments use different systems to track the sustainability metrics you need — and how do you reconcile them?"
5. "Have you ever missed a reporting deadline or submitted incomplete data because collection took too long?"

#### Industry Context
B Corp certification requires scoring 80+ on the B Impact Assessment (BIA), which covers Governance, Workers, Community, Environment, and Customers. CDP (formerly Carbon Disclosure Project) focuses on climate, water, and forests. GRI (Global Reporting Initiative) is the most widely used sustainability reporting framework globally. EcoVadis is increasingly required in procurement processes. Major agency holding companies publish annual sustainability reports following GRI or SASB standards. The EU Corporate Sustainability Reporting Directive (CSRD) will impact agencies with EU operations starting 2025-2026.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an ESG Reporting Hub board. Groups organized by framework section: Environment, Social/Workforce, Governance, Community, Client Impact. Columns: Metric Name (text), Framework (dropdown: B Corp BIA, CDP, GRI, EcoVadis, Client Custom), Category (dropdown: Emissions, Energy, Water, Waste, DEI, Pay Equity, Benefits, Governance, Procurement, Community), Data Owner (people), Collection Deadline (date), Status (status: Not Started, Data Requested, Submitted, Under Verification, Verified, Published), Current Value (numbers), Prior Year Value (numbers), Unit (dropdown: kgCO2e, kWh, gallons, %, headcount, USD, yes/no), Evidence (files), Notes (long text), Verifier (people). Automations: 30 days before Collection Deadline, change Status to Data Requested and notify Data Owner. 7 days before deadline, send reminder if Status is still Data Requested. When Status changes to Submitted, notify Verifier. Dashboard: completion rate by framework (progress bars), overdue items (table), year-over-year comparisons (charts), department response rates (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Compiler
**Agent Purpose:** Automate ESG data collection, cross-map metrics across reporting frameworks, and generate framework-specific reports.

**Triggers:**
- Reporting cycle kickoff (annual/quarterly schedule)
- New client ESG questionnaire received
- Data owner submits metric value
- Deadline approaching with incomplete data (7 days, 3 days, 1 day)

**Actions:**
- Send personalized data collection requests to department owners with clear instructions
- Cross-reference submitted data against prior year values and flag anomalies (>20% variance)
- Map collected data points to multiple framework requirements automatically
- Generate draft reports in framework-specific formats (BIA, CDP, GRI)
- Compile client questionnaire responses from existing data without re-requesting
- Escalate persistent non-responders to their department heads

**Data Required:**
- Framework requirement mappings (BIA questions → data points → departments)
- Historical ESG data (prior years for trend analysis)
- Organizational structure (department heads, data owners)
- Client questionnaire templates

**Autonomy Level:** Human-in-the-Loop
ESG Compiler autonomously collects and cross-maps data but requires human verification of all reported figures before external submission. Anomaly flags require human review and explanation.

**Example Interaction:**
> It's Q1 and the annual B Corp recertification data collection has kicked off. ESG Compiler identifies 127 data points needed, maps them to 34 data owners across 12 departments, and sends personalized collection requests. The HR Director receives: "Hi Sarah — I need 8 data points for our B Corp recertification by March 15: employee turnover rate, gender pay gap ratio, % employees with health benefits, average training hours per employee, % living wage compliance, parental leave utilization rate, DEI program participation, and employee satisfaction score. Last year's values are pre-filled for reference. Please update with 2025 actuals."
>
> Three weeks in, ESG Compiler reports: "87/127 data points collected (69%). 14 overdue from Operations and Finance. Anomaly detected: Scope 2 emissions reported 45% lower than last year — please verify with Facilities Manager. Cross-mapping complete: 94% of CDP Water questionnaire can be auto-populated from B Corp data already collected." The sustainability lead reviews the anomaly (new office moved to renewable energy — legitimate), approves, and ESG Compiler updates all relevant frameworks simultaneously.

---

### Use Case 4: Sustainable Supplier & Vendor Scoring

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Agencies work with hundreds of suppliers — production companies, printers, event venues, freelancers, tech vendors, media partners. Clients increasingly require agencies to demonstrate sustainable supply chain practices. Procurement and sustainability teams must assess each vendor's environmental credentials, but there's no centralized system. Sustainability questionnaires are sent via email, responses are stored in scattered folders, certifications expire without anyone noticing, and when a client asks "what percentage of your suppliers meet our sustainability criteria?" the answer takes weeks to compile.

#### The Solution
monday.com Work Management as a Supplier Sustainability Scorecard. Each vendor is an item with columns for: sustainability certifications (ISO 14001, B Corp, carbon neutral, SBTi), questionnaire completion status, risk rating, last assessment date, and next review date. File columns store certificates and questionnaire responses. Formula columns calculate composite sustainability scores. Automations trigger reassessment reminders when certifications approach expiry. Dashboards show portfolio-level sustainability metrics for client reporting.

#### The Outcome
- Centralized vendor sustainability database replacing scattered spreadsheets and email
- Automated certification tracking — no more expired certificates going unnoticed
- Client-ready supplier sustainability metrics available on demand
- 50% reduction in vendor assessment cycle time

#### Discovery Questions
1. "How many active suppliers and vendors does your agency work with, and what percentage have been formally assessed for sustainability practices?"
2. "When a client requires proof that your supply chain meets their sustainability standards, how do you compile that data?"
3. "Do you track supplier certifications like ISO 14001 or B Corp, and how do you know when they expire?"
4. "Have you ever had to switch vendors mid-project because they couldn't meet a client's sustainability requirements?"

#### Industry Context
Key certifications in ad production: ISO 14001 (environmental management), AdGreen certification, albert certification (broadcast), B Corp, FSC (paper/print), Green Seal. Production companies are increasingly expected to demonstrate carbon measurement capabilities. The Advertising Association's Ad Net Zero initiative requires agencies to use AdGreen-certified production partners by certain milestones. Scope 3 emissions (which include supplier activities) typically represent 80-90% of an agency's total carbon footprint.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Supplier Sustainability Scorecard board. Groups: Production Partners, Print & Packaging, Event & Experiential, Technology, Media, Freelancers & Contractors. Columns: Vendor Name (text), Primary Contact (text), Contact Email (email), Sustainability Questionnaire Status (status: Not Sent, Sent, Partial, Complete, Overdue), ISO 14001 (status: Certified, In Progress, Not Certified, Expired), B Corp (status: Certified, Pending, Not Certified), Carbon Measurement (status: Yes - Verified, Yes - Self-Reported, No), AdGreen Certified (status: Yes, No, N/A), Sustainability Score (numbers, 0-100), Last Assessment Date (date), Next Review Date (date), Certificates (files), Risk Level (status: Low, Medium, High), Notes (long text). Automations: 60 days before Next Review Date, notify Procurement to initiate reassessment. When Sustainability Questionnaire Status is Overdue (30 days past Sent), notify vendor contact. When any certification status changes to Expired, change Risk Level to High. Dashboard: score distribution (chart), certification coverage (pie chart), overdue assessments (table), risk breakdown (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorGreen
**Agent Purpose:** Manage supplier sustainability assessments, track certifications, and calculate composite sustainability scores.

**Triggers:**
- New vendor added to procurement board
- Certification expiry approaching (90, 60, 30 days)
- Vendor submits sustainability questionnaire via form
- Client requests supply chain sustainability report
- Quarterly portfolio review schedule

**Actions:**
- Send sustainability questionnaires to new vendors automatically
- Parse questionnaire responses and update vendor profile columns
- Verify certifications against public registries (B Corp directory, ISO accreditation bodies)
- Calculate composite sustainability scores based on weighted criteria
- Generate client-specific supply chain sustainability reports
- Recommend alternative vendors when current suppliers fail sustainability thresholds

**Data Required:**
- Vendor contact database and categorization
- Sustainability questionnaire template and scoring rubric
- Certification registry APIs (B Corp, ISO, FSC)
- Client-specific sustainability requirements

**Autonomy Level:** Human-in-the-Loop
VendorGreen autonomously manages questionnaire distribution, reminders, and score calculations. Vendor risk ratings and client reports require human approval before sharing externally.

**Example Interaction:**
> A new production company, Bright Frame Studios, is onboarded for an upcoming shoot. VendorGreen automatically sends them the agency's sustainability questionnaire and checks public registries. It finds Bright Frame is B Corp certified (score: 89.2, expires Dec 2026) but has no ISO 14001 or AdGreen certification. The questionnaire comes back showing they measure production carbon but don't offset. VendorGreen calculates a composite score of 62/100 (Medium risk) and flags: "Suitable for standard productions. For clients with Net Zero requirements (Unilever, Diageo), recommend requesting a carbon management plan or considering alternative partner Studio Green (score: 84/100)."

---

### Use Case 5: Sustainable Production Planning & Green Shoot Toolkit

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Ad production is resource-intensive: sets are built and torn down, crews fly internationally, generators power remote locations, catering creates food waste, and post-production render farms consume significant energy. Sustainability teams want producers to make greener choices (local crew, virtual production, renewable energy) but lack a systematic way to embed sustainability into production planning. Green production guidelines exist as PDF documents that nobody reads. By the time sustainability is considered, budgets are locked and flights are booked.

#### The Solution
monday.com Work Management as a Green Production Planning board integrated into the existing production workflow. Each production gets a sustainability checklist generated from the production type (shoot, event, digital, print). Items cover: travel alternatives assessment, local crew sourcing, renewable energy options, catering waste reduction, set material reuse plans, and carbon offset requirements. Status columns track compliance. Automations flag productions that skip sustainability planning steps.

#### The Outcome
- Sustainability embedded into production planning from day one (not afterthought)
- 30-40% reduction in production-related emissions through systematic green choices
- Standardized green production practices across all teams and offices
- Production sustainability data feeds directly into campaign carbon tracker

#### Discovery Questions
1. "At what point in production planning does sustainability get considered — and is that early enough to actually influence decisions?"
2. "Do your producers have clear guidelines for sustainable production practices, and how consistently are they followed?"
3. "What's the biggest source of avoidable emissions in your production process?"
4. "Have you explored virtual production or LED volume technology as a lower-carbon alternative to location shoots?"

#### Industry Context
AdGreen provides a production carbon calculator and best practice guides. albert (BAFTA's sustainability initiative) certifies sustainable broadcast productions. Key levers: virtual production (LED volumes like those at ARRI Stage London or Lux Machina reduce travel), local crew sourcing, renewable-powered studios, digital-first reviews (reducing travel for approvals), sustainable catering, and set material libraries for reuse. The industry is moving toward mandatory carbon action plans for productions above certain budget thresholds.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Green Production Planner board. Groups: Pre-Production Sustainability, Travel & Transport, On-Set Practices, Post-Production, Wrap & Waste. Columns: Checklist Item (text), Production Name (connect to Productions board), Category (dropdown: Travel, Energy, Materials, Waste, Catering, Digital), Required (status: Mandatory, Recommended, Optional), Compliance (status: Complete, In Progress, Skipped, N/A), Responsible (people), Green Alternative Considered (text), Estimated Carbon Saving (numbers, kgCO2e), Cost Impact (dropdown: Lower Cost, Neutral, +5-10%, +10-20%, +20%+), Notes (long text). Automations: When new production created on Productions board, auto-create Green Production Planner items from template. When any Mandatory item has Compliance set to Skipped, notify Sustainability Lead. Create a Kanban view by Compliance status. Dashboard: compliance rate by category (chart), total estimated carbon savings (number widget), productions with skipped mandatory items (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** GreenProducer
**Agent Purpose:** Embed sustainability best practices into production planning and recommend green alternatives for every production decision.

**Triggers:**
- New production created on production management board
- Travel booking request submitted
- Location/venue selection in progress
- Production budget finalized
- Post-production kickoff

**Actions:**
- Generate production-type-specific sustainability checklists
- Recommend green alternatives (e.g., local crew vs. fly-in, virtual production vs. location, renewable-powered studio options)
- Estimate carbon impact of production choices with alternatives comparison
- Connect producers to pre-vetted sustainable suppliers from VendorGreen database
- Flag high-carbon decisions that could be modified without budget impact
- Generate post-production sustainability report card

**Data Required:**
- Production brief (type, locations, duration, crew size, budget)
- Sustainable supplier database (from VendorGreen)
- Emission factors for production activities (AdGreen methodology)
- Studio and venue sustainability credentials

**Autonomy Level:** Escalation-Based
GreenProducer autonomously generates checklists and recommendations. Budget-impacting suggestions are presented as options with cost/carbon trade-offs for producer decision. Mandatory compliance items that are skipped escalate to sustainability lead.

**Example Interaction:**
> A producer creates a new campaign shoot: 3-day production in Cape Town for a UK client, 12-person crew flying from London. GreenProducer immediately generates the sustainability checklist and flags: "This production has estimated emissions of 18.2 tCO2e, with 72% from flights. Alternatives to consider: (1) Hire 8 of 12 crew locally in Cape Town — saves 9.4 tCO2e and ~£14,000 in travel costs. (2) If London crew is required, route via direct flights only (connecting flights add 40% emissions). (3) Cape Town studio options with solar power: Studio 7 (verified renewable), Sunset Studios (50% solar). Shall I connect you with local crew agencies from our verified supplier list?"

---

### Use Case 6: Client Sustainability Storytelling & Impact Reporting

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Agencies are increasingly asked to help clients tell their sustainability stories — but the sustainability team must ensure those stories are accurate, substantiated, and compliant. At the same time, agencies need to demonstrate *their own* sustainability impact to clients in regular business reviews. Both require compiling data from multiple sources, creating visualizations, and crafting narratives. This is time-consuming, creative work that the small sustainability team does manually alongside their compliance and operations responsibilities.

#### The Solution
monday.com Work Management and monday.com Dashboards as a client-facing Sustainability Impact Portal. Each client gets a board tracking: campaigns produced, carbon footprint data, green production choices made, sustainable supplier usage, and year-over-year improvements. Dashboards create visual impact summaries. Automations pull data from campaign carbon trackers and production planners. Templates standardize quarterly sustainability updates.

#### The Outcome
- Automated client sustainability reports generated from existing workflow data
- Consistent storytelling framework across all client relationships
- Differentiation in pitches through demonstrable sustainability capabilities
- Upsell opportunity: sustainability consulting packaged with campaign production

#### Discovery Questions
1. "How do you currently demonstrate your agency's sustainability impact to clients during business reviews?"
2. "Do clients ever ask for sustainability dashboards or reports specific to their campaigns?"
3. "Is sustainability storytelling a revenue-generating service, or is it bundled into existing fees?"
4. "How do you ensure the sustainability claims in client campaigns are backed by verifiable data?"

#### Industry Context
Purpose-driven marketing is a $25B+ market. Clients want agencies that practice what they preach — ESG credentials are becoming table stakes in agency pitches. The "say-do gap" (agencies marketing sustainability for clients while ignoring their own footprint) is a growing reputational risk. Leading agencies now include sustainability dashboards in client portals alongside campaign performance metrics. Some agencies have created standalone sustainability consulting practices as revenue streams.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client Sustainability Impact board. Groups by client name (one group per major client). Columns: Reporting Period (dropdown: Q1 2025, Q2 2025, Q3 2025, Q4 2025), Campaigns Produced (numbers), Total kgCO2e (numbers), kgCO2e Per Campaign (formula), Green Production Choices Made (numbers), Sustainable Suppliers Used % (numbers), YoY Carbon Reduction % (numbers), Highlights (long text), Areas for Improvement (long text), Status (status: Draft, Under Review, Approved, Delivered), Owner (people), Delivery Date (date), Report File (files). Automations: At end of each quarter, create new items for all active clients. When Status changes to Approved, notify client lead. Dashboard: carbon intensity trend by client (line chart), green production adoption rate (bar chart), client satisfaction scores (if tracked), top sustainable clients leaderboard."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ImpactWriter
**Agent Purpose:** Automatically compile sustainability data and generate narrative impact reports for client quarterly reviews.

**Triggers:**
- Quarterly reporting cycle (automated schedule)
- Client requests ad hoc sustainability update
- Campaign reaches completion milestone
- Annual review preparation

**Actions:**
- Pull campaign carbon data, production sustainability scores, and supplier metrics from connected boards
- Calculate period-over-period trends and benchmarks
- Generate narrative sustainability summary with data visualizations
- Highlight top green production achievements and improvement areas
- Create framework-specific reporting (GRI, SASB) when required by client
- Draft executive summary email for account lead review

**Data Required:**
- Campaign carbon tracker data (per client)
- Green production planner compliance data
- Supplier sustainability scores (for client's campaigns)
- Historical reporting data for trend analysis

**Autonomy Level:** Human-in-the-Loop
ImpactWriter generates draft reports and narratives automatically. Account leads review and approve before client delivery. All data claims are sourced and verifiable.

**Example Interaction:**
> Q4 reporting cycle triggers ImpactWriter. For the agency's largest client, GlobalBev Inc., it compiles: "12 campaigns produced in Q4, total carbon footprint of 34.2 tCO2e (down 22% from Q4 2024). 8 of 12 campaigns used 100% local crew (vs. 3 of 14 in Q4 2024). Sustainable supplier usage: 78% (up from 51%). Key achievement: Holiday campaign achieved albert certification — first for this client. Area for improvement: Print materials for retail activations still using non-FSC paper — recommend transitioning to FSC-certified suppliers in Q1." It attaches a formatted PDF with charts and sends to the account director for review.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| AdGreen | Industry body providing carbon calculator and sustainable production tools for the advertising sector |
| albert | BAFTA-backed sustainability certification for screen production (broadcast, film, digital) |
| Ad Net Zero | Global advertising industry initiative to achieve net-zero carbon emissions from advertising |
| Greenwashing | Making misleading or unsubstantiated claims about environmental benefits of products/services/practices |
| Scope 1/2/3 Emissions | Direct emissions (Scope 1), purchased energy (Scope 2), and value chain emissions (Scope 3) per GHG Protocol |
| B Corp | Certification from B Lab verifying a company meets high standards of social and environmental performance |
| B Impact Assessment (BIA) | The assessment tool used to measure and certify B Corp status, covering five impact areas |
| FTC Green Guides | US Federal Trade Commission guidelines on environmental marketing claims |
| ASA/CAP Code | UK Advertising Standards Authority code governing advertising content, including environmental claims |
| EcoVadis | Business sustainability ratings platform used in procurement and supply chain assessment |
| CDP | Global disclosure system for environmental data (climate, water, forests) — formerly Carbon Disclosure Project |
| GRI | Global Reporting Initiative — most widely used sustainability reporting standards |
| Virtual Production | LED volume/stage technology enabling in-studio location simulation, reducing travel and environmental impact |
| FSC | Forest Stewardship Council certification for responsibly managed forest products (paper, packaging) |
| kgCO2e | Kilograms of carbon dioxide equivalent — standard unit for measuring greenhouse gas emissions |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Sustainability Officer / Head of Sustainability | Sets agency sustainability strategy, owns ESG reporting and certifications | Decision-maker |
| Sustainability Coordinator/Manager | Day-to-day execution: data collection, compliance reviews, vendor assessments | Key User / Champion |
| COO / Chief Operating Officer | Operational authority over production practices, facilities, procurement | Decision-maker / Budget holder |
| Head of Production | Oversees all production activities — key partner for green production practices | Influencer / Gate-keeper |
| Executive Producer | Makes production-level decisions on crew, locations, suppliers | User / Implementer |
| Procurement Manager | Manages vendor relationships and contracts — enforces sustainability criteria | Influencer |
| Legal / Compliance | Reviews advertising claims, manages regulatory risk from greenwashing | Influencer / Blocker |
| Client Lead / Account Director | Interfaces with clients on sustainability requirements and reporting | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations | Facilities management, energy, waste — provides core environmental data | Unified operations + sustainability tracking |
| Procurement | Vendor management, supplier diversity — sustainability criteria enforcement | Combined vendor management with sustainability scoring |
| Creative & Design | Produces assets containing environmental claims — needs review workflow | Integrated creative review with sustainability compliance |
| PR & Communications | Manages agency's own sustainability communications and reputation | Shared ESG data and narrative generation |
| HR | DEI metrics, employee benefits, wellness — social pillar of ESG reporting | Combined workforce data for ESG reporting |
| Finance | Charitable giving, pay equity, sustainability investment tracking | Unified data collection for B Corp and ESG frameworks |
| IT | Digital carbon footprint, cloud infrastructure, e-waste management | Tech stack sustainability measurement |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Sphera / SimaPro | Enterprise LCA and carbon accounting software | Too complex and expensive for agency use cases — monday.com provides workflow-centric carbon tracking without needing a dedicated analyst |
| Watershed / Persefoni | Corporate carbon accounting platforms | Designed for corporate finance/compliance, not creative production workflows — monday.com embeds sustainability into existing production processes |
| EcoVadis | Supply chain sustainability ratings | Assessment-only — doesn't manage the workflow of collecting data, remediating issues, or tracking improvements over time |
| AdGreen Carbon Calculator | Free production carbon calculator for advertising | Calculator only — no workflow, no tracking, no automation — monday.com wraps the methodology in actionable project management |
| Spreadsheets (Google Sheets/Excel) | Default tool for ESG data collection at most agencies | No automation, no audit trail, version control nightmares, no real-time dashboards — monday.com replaces the annual spreadsheet scramble |
| Workiva / Diligent ESG | Enterprise ESG reporting platforms | Enterprise pricing ($50K+), designed for public company compliance — overkill for agencies, monday.com provides 80% of the value at a fraction of cost |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use AdGreen's carbon calculator" | "AdGreen is great for individual production calculations, but it doesn't connect to your production planning workflow, track data over time, or generate client reports. monday.com wraps AdGreen-compatible methodology into your existing production process with automation and reporting built in." |
| "Sustainability is just one person's job — we don't need a platform for it" | "That's exactly why you need it. One person managing ESG data collection from 12 departments via email doesn't scale. monday.com automates the data collection, tracks deadlines, and reduces that person's manual work by 60-70% so they can focus on strategy instead of spreadsheets." |
| "Our clients don't really ask about sustainability" | "They will. 78% of Fortune 500 companies now include sustainability criteria in agency RFPs. Being ahead of this curve is a competitive advantage. And tracking your own sustainability isn't just client-facing — it reduces costs (energy, waste, travel) and attracts talent." |
| "We're evaluating dedicated ESG platforms like Watershed" | "Watershed is designed for corporate carbon accounting at scale. For an agency, the value isn't just measuring carbon — it's embedding sustainability into your production workflows, creative review processes, and vendor management. monday.com does this while also serving as your project management platform, so you're not adding another tool nobody logs into." |
| "We can't afford to slow down production with sustainability reviews" | "The review process actually speeds up when it's structured. Right now, sustainability checks happen ad hoc — last-minute scrambles before client deadlines. With a systematic claims review pipeline and automated green production checklists, sustainability becomes a 5-minute check integrated into existing workflows, not a production-blocking bottleneck." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for agency B Corp certification journey using monday.com]
- [Placeholder for production company carbon tracking implementation]
- [Placeholder for holding company ESG reporting consolidation]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
