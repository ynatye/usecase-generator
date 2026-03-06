# Electricity, Oil & Gas × Legal Playbook

## Overview

Legal departments in electricity, oil, and gas companies are among the most complex and high-stakes corporate legal functions in any industry. They operate at the intersection of regulatory law, environmental compliance, land and mineral rights, commercial transactions, and increasingly, energy transition policy. A single mid-major E&P company may manage 10,000+ active leases, 500+ joint operating agreements, dozens of regulatory proceedings, and hundreds of litigation matters simultaneously. The legal team's work directly impacts billions in asset value—a single unfavorable regulatory ruling or environmental consent decree can wipe out hundreds of millions in shareholder value overnight.

These departments typically employ 30–200+ attorneys and legal professionals organized into specialty groups: land and title, regulatory/government affairs, commercial/transactional, litigation, environmental, and increasingly, ESG/sustainability counsel. The org structure often mirrors business segments—upstream counsel handling exploration and production matters, midstream counsel managing pipeline rights-of-way and FERC proceedings, and downstream counsel covering refining, retail, and trading compliance. Many energy legal teams also manage large networks of outside counsel (50–200+ law firms) across dozens of jurisdictions.

The industry is experiencing unprecedented legal complexity from the energy transition: renewable energy PPAs, carbon capture agreements, hydrogen offtake contracts, ESG disclosure liability, climate litigation (350+ cases filed globally against fossil fuel companies), and the regulatory whiplash of changing administrations. Legal teams are overwhelmed—drowning in contract review, buried in regulatory filings, and spending 60%+ of their time on routine matters rather than strategic counsel. The cost of outside counsel has increased 20–30% in three years, and the volume of matters continues to grow.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Massive volume of routine legal work (lease review, contract management, regulatory filings) can be automated or AI-assisted |
| 2 | Scale Impact Without Overhead | High | Energy transition creates entirely new legal workstreams (renewables, carbon, ESG) without proportional budget increases |
| 3 | Consolidate Tech Stack with AI | Medium | Legal teams juggle CLM tools, matter management systems, land management software, and e-billing platforms — fragmented and expensive |

## Prioritized Use Cases

---

### Use Case 1: Contract Lifecycle Management for Energy Agreements

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy companies manage thousands of active contracts spanning dozens of specialized agreement types: joint operating agreements (JOAs), farmout agreements, production sharing contracts (PSCs), gas purchase agreements, pipeline transportation agreements, master service agreements (MSAs) with oilfield service companies, power purchase agreements (PPAs), tolling agreements, and interconnection agreements. Each has unique commercial terms, renewal provisions, force majeure clauses, and regulatory compliance requirements. Most legal teams track contracts in a patchwork of spreadsheets, shared drives, and legacy CLM tools that don't understand energy-specific terms. Key dates are missed, auto-renewal traps cost millions, and finding a specific indemnification clause across 5,000 agreements takes hours of manual review.

#### The Solution
monday.com Work Management creates an energy-specific CLM platform. Boards organize contracts by type, counterparty, business segment, and jurisdiction. Columns capture critical commercial terms: effective dates, expiration, renewal terms, termination provisions, volume commitments, pricing mechanisms, assignment restrictions, and governing law. Automations trigger renewal review workflows 90/180 days before expiration, alert attorneys when contract thresholds are approaching (volume commitments, spend caps), and route new contract requests through intake and approval workflows. monday AI can extract key terms from uploaded contracts, compare clauses against standard templates, and flag deviations that require attorney review. CRM integration tracks counterparty relationships across all agreement types.

#### The Outcome
- 70% reduction in contract review time for standard agreement types
- Zero missed renewal deadlines or auto-renewal traps (vs. 5–10 per year industry average)
- 50% faster contract turnaround time from request to execution
- $3–5M annual savings in avoided unfavorable auto-renewals and missed termination windows
- Single source of truth for 10,000+ active agreements

#### Discovery Questions
1. "How many active contracts does your legal department manage, and what are the top 5 agreement types by volume?"
2. "Have you had any instances where a missed renewal deadline or auto-renewal resulted in significant financial impact?"
3. "How long does it currently take to get a new MSA or JOA from initial request to full execution?"
4. "When a commercial team asks 'what are our obligations under contract X,' how quickly can you answer—and how confident are you in that answer?"
5. "Are you using any CLM tool today, and how well does it handle energy-specific contract types like JOAs, PSCs, or PPAs?"

#### Industry Context
JOAs (Joint Operating Agreements) govern the relationship between working interest owners in a well or unit—they define operator responsibilities, cost sharing, and decision-making (consent vs. non-consent operations). Farmout agreements transfer the right to earn a working interest by drilling. PSCs (Production Sharing Contracts) are common in international operations, where the host government retains ownership and the operator recovers costs from a share of production. PPAs (Power Purchase Agreements) for renewables are 15–25 year contracts with complex pricing escalators. Force majeure clauses in energy contracts received intense scrutiny during COVID-19 and the 2021 Texas Winter Storm Uri.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Energy Contract Management system with these boards: (1) 'Contract Registry' with columns: Contract ID (text), Contract Name (text), Contract Type (dropdown: JOA/Farmout/PSC/Gas Purchase/Pipeline Transport/MSA/PPA/Tolling/Interconnection/Lease/Surface Use/ROW/Other), Counterparty (text), Business Segment (dropdown: Upstream/Midstream/Downstream/Renewables/Corporate), Jurisdiction (dropdown: TX/OK/ND/CO/PA/WV/NM/LA/Federal/International/Multi-State), Effective Date (date), Expiration Date (date), Renewal Type (dropdown: Auto-Renew/Manual Renew/Evergreen/Fixed Term), Renewal Notice Period Days (numbers), Termination for Convenience (status: Yes/No/Conditional), Contract Value (numbers), Status (status: Draft/In Negotiation/Pending Execution/Active/Expiring/Expired/Terminated), Assigned Attorney (people), Key Terms Summary (long text). (2) 'Contract Requests' with columns: Requestor (people), Request Type (dropdown: New Contract/Amendment/Renewal/Assignment/Termination), Contract Type (dropdown — same list), Counterparty (text), Business Need (long text), Priority (status: Standard/Expedited/Urgent), Requested By Date (date), Assigned Attorney (people), Status (status: Intake/Drafting/Counterparty Review/Negotiation/Management Approval/Execution/Complete). (3) 'Key Date Alerts' with columns: Contract (connect to board 1), Alert Type (dropdown: Renewal Window/Expiration/Volume Commitment Deadline/Rate Adjustment/Regulatory Filing/Option Exercise), Alert Date (date), Days Until (numbers), Action Required (long text), Owner (people), Status (status: Upcoming/Action Required/Completed/Waived). Add automations: when Key Date Alert is 90 days away, notify Assigned Attorney; when Key Date Alert is 30 days away and Status is still Upcoming, escalate to General Counsel; when Contract Request Status changes to Complete, create items in Contract Registry. Create Dashboard with: contracts expiring in 90 days (table), request pipeline by status (chart), contract volume by type (chart), average turnaround time by request type (chart), key date alert status (battery)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Contract Intelligence Agent
**Agent Purpose:** Extract key terms from energy contracts, flag deviations from standards, and proactively manage the contract portfolio lifecycle.

**Triggers:**
- New contract uploaded or created in registry
- Key date alert threshold reached (90/60/30 days)
- Contract request submitted
- Counterparty sends amended terms (email integration)
- Quarterly portfolio review initiated

**Actions:**
- Extract and populate key terms from uploaded PDF/Word contracts (dates, parties, pricing, obligations)
- Compare contract clauses against company standard templates and flag deviations
- Generate renewal/termination recommendations based on contract performance and market conditions
- Create contract request intake summaries with risk assessment
- Identify cross-contract obligations with the same counterparty
- Generate quarterly contract portfolio reports with risk heat maps

**Data Required:**
- Company standard contract templates by agreement type
- Historical contract negotiation outcomes
- Counterparty relationship data
- Market benchmarks for key commercial terms (rates, pricing)
- Regulatory requirements by jurisdiction

**Autonomy Level:** Human-in-the-Loop
Agent extracts terms and generates analysis autonomously. All contract recommendations require attorney review. Execution decisions require authorized signatory approval per delegation of authority.

**Example Interaction:**
> A new 20-year PPA for a 200 MW solar project in West Texas is uploaded to the registry. The Contract Intelligence Agent extracts 47 key terms including the base price ($28/MWh), annual escalator (2.5%), curtailment provisions, force majeure definition, credit support requirements, and change-in-law protections. It compares against the company's standard PPA template and flags 6 deviations: (1) the curtailment cap is 5% vs. company standard of 3%, (2) the force majeure clause doesn't include "grid emergency" as a qualifying event, (3) the assignment clause requires consent for indirect transfers (non-standard), (4) the performance guarantee uses P75 vs. company standard P90, (5) the termination payment calculation uses book value rather than fair market value, and (6) the tax equity flip structure isn't addressed. The agent generates a negotiation memo for the assigned attorney with recommended positions on each deviation, citing precedent from the 3 most recent PPAs the company executed.

---

### Use Case 2: Land & Mineral Rights Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Upstream oil and gas companies manage vast land positions—often 100,000+ acres spread across dozens of counties and states. Each lease has specific terms: primary term (typically 3–5 years), royalty rate, bonus payments, depth restrictions, pooling provisions, Pugh clause implications, continuous drilling obligations, and shut-in provisions. Land departments must track lease expirations to avoid losing valuable acreage, manage held-by-production (HBP) requirements, process division order title opinions, and coordinate with landmen who are acquiring new leases. A single missed lease expiration on a section with proved reserves can result in $5–50M in lost asset value. Most companies still manage this in legacy land management systems (P2 Land, Quorum Land, or worse—spreadsheets) with limited workflow automation.

#### The Solution
monday.com Work Management creates a modern land management orchestration layer. Boards track every lease with columns for all critical terms—expiration dates, royalty rates, depth clauses, continuous development obligations, and HBP status. Automations trigger renewal/extension workflows 12/6/3 months before expiration, create tasks for title examination when new wells are proposed, and coordinate between land, legal, and operations teams on lease compliance. Timeline views show the lease expiration calendar across the entire acreage position. monday AI can analyze lease terms to identify optimization opportunities (which leases to extend vs. let expire based on development plans), flag Pugh clause exposures, and predict title issues based on historical patterns.

#### The Outcome
- Zero lost leases due to missed expirations (vs. 2–5 per year industry average for mid-size operators)
- 60% reduction in title examination cycle time through automated workflow coordination
- $10–50M in preserved asset value from proactive lease management
- Single view of entire acreage position with drill-down to individual lease terms

#### Discovery Questions
1. "How many active leases are you managing, and across how many counties/states?"
2. "Have you ever lost a lease due to a missed expiration or continuous development obligation—and what was the financial impact?"
3. "What's your current lease management system, and how well does it integrate with your legal and operations workflows?"
4. "How do you coordinate between your land department, title attorneys, and drilling operations when proposing a new well?"
5. "Do you have exposure to Pugh clauses that could release undeveloped depths or horizons?"

#### Industry Context
HBP (Held by Production) means a lease continues beyond its primary term as long as production continues. Pugh clauses release unleased depths or non-pooled acreage at the end of the primary term—a significant risk for operators who haven't drilled all horizons. Continuous development obligations (CDOs) require drilling a new well every X months to maintain acreage. Division order title opinions (DOTOs) examine the chain of title to verify mineral ownership. Landmen are the field professionals who acquire leases and manage surface relationships. A "title curative" is the process of resolving defects found in the chain of title.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Land & Mineral Rights Management system with these boards: (1) 'Lease Registry' with columns: Lease Name (text), Lessor (text), County (text), State (dropdown: TX/OK/ND/CO/NM/PA/WV/LA/WY/Other), Gross Acres (numbers), Net Mineral Acres (numbers), Primary Term Expiration (date), Royalty Rate (numbers), Bonus per Acre (numbers), Depth Restriction (text), Pugh Clause (status: Yes-Depth/Yes-Horizontal/No), Continuous Development Obligation (status: Yes/No), CDO Interval Days (numbers), HBP Status (status: Primary Term/HBP-Producing/HBP-Shut In/Expiring/Expired), Producing Wells (numbers), Assigned Landman (people), Legal Contact (people), Status (status: Active/Expiring <12mo/Expiring <6mo/Expiring <3mo/Expired/Released). (2) 'Title Work Queue' with columns: Lease (connect to board 1), Well Name (text), Title Opinion Type (dropdown: Drilling/Division Order/Supplemental/Curative), Title Attorney (people — outside counsel), Status (status: Ordered/In Progress/Received/Under Review/Approved/Curative Required), Due Date (date), Cost (numbers), Title Defects Found (numbers), Curative Status (status: None/In Progress/Cleared). (3) 'Lease Expiration Actions' with columns: Lease (connect to board 1), Expiration Date (date), Acreage at Risk (numbers), Estimated Value at Risk (numbers), Recommended Action (dropdown: Drill/Extend-Negotiate/Release/Assign/Top Lease), Action Owner (people), Status (status: Assessment/Action Planned/In Progress/Resolved), Notes (long text). Add automations: when Lease Primary Term Expiration is 12 months away, create item in Expiration Actions board; when HBP Status changes to Expiring, notify Assigned Landman and Legal Contact; when Title Work Status changes to Curative Required, create curative tasks and notify title attorney. Create Dashboard with: acreage expiration timeline (timeline), value at risk by state (chart), title work pipeline (chart), HBP status distribution (battery), Pugh clause exposure summary (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Lease Portfolio Guardian
**Agent Purpose:** Monitor the entire lease portfolio for expiration risks, optimize hold/release decisions, and coordinate title workflows proactively.

**Triggers:**
- Lease expiration date within 12/6/3/1 month
- New well proposed on leased acreage (from drilling schedule)
- Production decline below HBP threshold on a lease
- Title opinion received with defects
- Quarterly acreage portfolio review initiated

**Actions:**
- Generate prioritized expiration action list ranked by value-at-risk
- Cross-reference drilling schedule against expiring leases to ensure development timing maintains HBP
- Identify Pugh clause exposures and recommend protective drilling or release strategies
- Create title work orders and route to appropriate outside counsel by county/state expertise
- Track curative items and send automated follow-ups to title attorneys
- Generate quarterly acreage position reports for management

**Data Required:**
- Complete lease database with all material terms
- Drilling schedule and well proposals from operations
- Production data by well/lease
- Outside counsel roster with jurisdictional expertise
- Historical title defect patterns by county
- Current commodity prices and type curves for value-at-risk calculations

**Autonomy Level:** Escalation-Based
Agent monitors and generates reports autonomously. Title work orders under $25K are auto-routed. Lease extension negotiations and release decisions require Land Manager approval. Value-at-risk above $5M requires VP Land/Legal approval.

**Example Interaction:**
> The Lease Portfolio Guardian identifies that 47 leases totaling 12,400 net mineral acres in the Delaware Basin are entering their final 12 months of primary term, with combined estimated value-at-risk of $186M based on current type curves and commodity prices. It cross-references the drilling schedule and finds that 31 leases are already slated for development (drilling planned within 9 months), 8 have producing offset wells that may qualify for pooling to maintain HBP, and 8 require immediate attention. Of those 8, the agent recommends: negotiate 2-year extensions on 5 leases ($340K estimated bonus cost) based on similar recent transactions in the county, release 2 leases with marginal economics (saving $45K in annual rental payments), and top-lease 1 where the lessor relationship is strained. It generates extension offer letters pre-populated with market-rate terms and routes them to the Senior Landman for review.

---

### Use Case 3: Regulatory Proceedings & Government Affairs Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies are involved in dozens to hundreds of concurrent regulatory proceedings across federal (FERC, EPA, BLM, PHMSA, NRC), state (PUCs, oil & gas commissions, environmental agencies), and local jurisdictions. Each proceeding has its own docket, filing deadlines, intervention opportunities, and hearing schedules. Regulated utilities manage rate cases that determine billions in allowed revenue. Pipeline companies track FERC certificate proceedings that can take 2–5 years. E&P companies monitor state commission actions on well spacing, flaring rules, and produced water disposal. The volume is staggering—a large utility may track 500+ open regulatory dockets simultaneously. Missing a filing deadline or intervention window can have catastrophic consequences (lost revenue, permit denials, enforcement actions). Most companies track this in spreadsheets or basic matter management systems that don't handle the multi-year, multi-party nature of regulatory proceedings.

#### The Solution
monday.com Work Management serves as a regulatory proceedings command center. Each proceeding is tracked with columns for docket number, jurisdiction, proceeding type, current phase, key dates, assigned counsel, and impact assessment. Sub-items capture individual filings, testimony, and discovery within each proceeding. Automations trigger filing preparation workflows based on regulatory calendars, notify attorneys of upcoming deadlines, and escalate when proceedings enter critical phases (hearings, settlement negotiations, orders). monday AI can monitor regulatory agency websites for new docket entries, summarize lengthy orders and testimony, and identify regulatory trends that could impact the business. Dashboards provide executive-level views of the regulatory landscape with drill-down to individual proceedings.

#### The Outcome
- Zero missed regulatory filing deadlines
- 50% reduction in time tracking and managing regulatory proceedings
- Executive visibility into the entire regulatory landscape in one dashboard
- Early identification of regulatory trends affecting business strategy

#### Discovery Questions
1. "How many active regulatory proceedings are you tracking across all jurisdictions?"
2. "Have you ever missed a filing deadline or intervention window, and what was the consequence?"
3. "How do you currently monitor for new regulatory actions or docket entries that affect your operations?"
4. "For your rate cases, how long is the cycle from filing to order, and how many internal teams are involved?"
5. "How does regulatory intelligence flow from your legal team to the business units that need to act on it?"

#### Industry Context
FERC regulates interstate electricity transmission, wholesale power markets, and natural gas pipelines. Rate cases allow utilities to recover prudent costs plus a reasonable return on equity (ROE). PHMSA (Pipeline and Hazardous Materials Safety Administration) regulates pipeline safety. BLM (Bureau of Land Management) manages federal mineral leases. State oil and gas commissions (Railroad Commission of Texas, Oklahoma Corporation Commission, NDIC) regulate drilling permits, spacing, and production. Intervention is the legal process of becoming a party to a regulatory proceeding. An order is the regulatory agency's binding decision.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Proceedings Tracker with these boards: (1) 'Active Proceedings' with columns: Docket Number (text), Proceeding Name (text), Jurisdiction (dropdown: FERC/EPA/BLM/PHMSA/SEC/State-TX RRC/State-OK OCC/State-ND NDIC/State PUC/State Environmental/Local/Other), Proceeding Type (dropdown: Rate Case/Certificate/Rulemaking/Enforcement/Permit/Complaint/Merger Review/Environmental Review/Other), Business Segment (dropdown: Upstream/Midstream/Downstream/Renewables/Utility), Current Phase (status: Pre-Filing/Filed/Discovery/Hearing/Briefing/Settlement/Awaiting Order/Order Issued/Rehearing/Appeal/Closed), Financial Impact Estimate (numbers), Impact Level (status: Low/Medium/High/Critical), Lead Attorney (people), Outside Counsel (text), Filing Deadline (date), Next Key Date (date), Status (status: Active/On Hold/Closed-Favorable/Closed-Unfavorable/Closed-Settled). (2) 'Proceeding Filings & Tasks' with columns: Proceeding (connect to board 1), Filing/Task Name (text), Filing Type (dropdown: Initial Filing/Testimony/Discovery Response/Brief/Settlement Offer/Motion/Reply/Intervention/Comment/Other), Due Date (date), Assigned To (people), Reviewer (people), Status (status: Not Started/Drafting/Internal Review/Management Approval/Filed/Acknowledged), Document Link (link). (3) 'Regulatory Monitoring' with columns: Agency (dropdown — same jurisdiction list), Topic (text), Date Identified (date), Summary (long text), Impact Assessment (status: No Action/Monitor/Action Required/Urgent), Affected Proceedings (connect to board 1), Assigned To (people). Add automations: when Filing Due Date is 30 days away, change Status to Drafting and notify Assigned To; when Filing Due Date is 7 days away and Status is not Filed, escalate to Lead Attorney and General Counsel; when Regulatory Monitoring Impact Assessment is Action Required, create filing tasks in board 2. Create Dashboard with: active proceedings by jurisdiction (chart), upcoming deadlines (timeline), financial exposure by impact level (chart), proceeding phase distribution (battery), regulatory monitoring alerts (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Radar Agent
**Agent Purpose:** Monitor regulatory developments, manage proceeding deadlines, and provide strategic intelligence on regulatory trends.

**Triggers:**
- New regulatory docket entry detected (via agency website monitoring)
- Filing deadline approaching (60/30/14/7 days)
- Regulatory order issued in a tracked proceeding
- New rulemaking proposed that could affect operations
- Quarterly regulatory landscape review scheduled

**Actions:**
- Scan regulatory agency docket systems for new entries in tracked proceedings
- Summarize lengthy regulatory orders, testimony, and rulemaking proposals (50+ page documents into 1-page briefs)
- Generate filing deadline calendars with preparation timelines
- Identify cross-proceeding dependencies (e.g., rate case outcome affecting pending certificate application)
- Create regulatory trend reports highlighting patterns across jurisdictions
- Draft routine regulatory filings (comments, interventions, compliance reports)

**Data Required:**
- Regulatory agency docket systems and websites
- Historical proceeding data and outcomes
- Company's regulatory filing templates
- Business strategy documents (for impact assessment)
- Outside counsel expertise database

**Autonomy Level:** Escalation-Based
Agent monitors and summarizes autonomously. Filing recommendations require attorney review. Intervention decisions require General Counsel approval. Settlement authority requires CEO/Board depending on amount.

**Example Interaction:**
> The Regulatory Radar Agent detects that FERC has issued a Notice of Proposed Rulemaking (NOPR) on transmission incentives that could affect the company's three pending certificate applications for interstate pipeline projects (combined $2.8B capital investment). The agent downloads the 127-page NOPR, generates a 2-page executive summary highlighting the 5 proposed changes most relevant to the company, identifies that the comment deadline is 75 days away, creates a filing task assigned to the regulatory counsel with a 45-day drafting timeline, and flags that two industry trade groups (INGAA and AGA) have announced plans to file joint comments. The agent recommends coordinating with trade group counsel before filing independent comments and creates a meeting request. The VP of Regulatory Affairs receives a dashboard alert showing this NOPR at "High Impact" alongside the 3 affected proceedings.

---

### Use Case 4: Environmental Compliance & Litigation Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies face an extraordinary volume of environmental legal matters: EPA consent decrees, state environmental agency enforcement actions, Superfund liability allocations, Clean Air Act compliance, Clean Water Act permitting, SPCC (Spill Prevention) plan reviews, methane emissions regulations, and the rising tide of climate litigation. A single legacy refinery may have 20+ open environmental remediation sites, each with its own regulatory timeline, monitoring requirements, and cost allocation among PRPs (Potentially Responsible Parties). Environmental litigation is uniquely complex—it involves technical experts, long timelines (5–20+ years for remediation cases), multiple responsible parties, and evolving scientific standards. Most legal departments track environmental matters separately from commercial litigation, creating silos. Climate litigation is adding a new vector: 30+ cases have been filed against major energy companies in the U.S. alone, with discovery demands consuming thousands of attorney hours.

#### The Solution
monday.com Work Management creates a unified environmental legal management platform. Boards track every environmental matter—enforcement actions, remediation sites, permit compliance, and litigation—with columns for regulatory agency, site location, estimated liability, insurance coverage, remediation phase, and assigned counsel. Sub-items capture specific compliance tasks, monitoring events, and regulatory submissions. Automations trigger monitoring report submissions, coordinate between legal and environmental engineers on remediation milestones, and escalate when compliance deadlines approach. monday AI can analyze environmental liability reserves, predict remediation cost trends, and identify patterns across sites. Service management capabilities can handle internal environmental compliance requests from operations.

#### The Outcome
- Unified view of all environmental legal exposure (previously scattered across 5+ systems)
- 40% reduction in environmental compliance management overhead
- Improved liability reserve accuracy through data-driven analysis
- Faster response to environmental incidents with automated notification workflows
- Complete audit trail for regulatory defense

#### Discovery Questions
1. "How many active environmental remediation sites and enforcement matters is your legal team managing?"
2. "How do you currently track environmental compliance obligations—are they in your matter management system, a separate database, or spreadsheets?"
3. "What's your estimated aggregate environmental liability reserve, and how confident is your actuarial analysis?"
4. "Are you facing any climate litigation, and how are you managing the document preservation and discovery demands?"
5. "How do you coordinate between your environmental legal team, environmental engineers, and operations on remediation projects?"

#### Industry Context
PRPs (Potentially Responsible Parties) share liability at Superfund sites, often requiring complex cost allocation negotiations. RCRA (Resource Conservation and Recovery Act) governs hazardous waste management. CERCLA (Superfund) addresses contaminated site cleanup. SPCC plans are required for facilities with significant oil storage. Methane regulations under the EPA's Methane Emissions Reduction Program (and the Inflation Reduction Act's methane fee) are creating new compliance obligations. Climate litigation theories include public nuisance, consumer fraud/greenwashing, and securities fraud. Environmental insurance (pollution legal liability, cost cap) is increasingly important for managing remediation risk.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Environmental Legal Management system with these boards: (1) 'Environmental Matters' with columns: Matter ID (text), Matter Name (text), Matter Type (dropdown: Remediation-Superfund/Remediation-RCRA/Enforcement-EPA/Enforcement-State/Permit Compliance/Climate Litigation/Toxic Tort/Water Discharge/Air Quality/Spill Response/Other), Regulatory Agency (dropdown: EPA/State DEQ/State AG/TCEQ/Private Plaintiff/Multi-Agency), Site Location (text), State (dropdown), Current Phase (status: Investigation/Remediation Design/Active Remediation/Monitoring/Closed-No Further Action/Litigation-Discovery/Litigation-Trial/Settlement/Appeal), Estimated Liability (numbers), Insurance Coverage (numbers), Net Exposure (numbers), PRP Allocation % (numbers), Lead Attorney (people), Outside Counsel (text), Next Milestone (date), Status (status: Active/Watch/Closed). (2) 'Compliance Tasks' with columns: Matter (connect to board 1), Task Description (text), Task Type (dropdown: Monitoring Report/Sampling Event/Regulatory Submission/Remediation Milestone/Document Production/Deposition/Expert Report/Court Filing), Due Date (date), Assigned To (people), Status (status: Upcoming/In Progress/Under Review/Submitted/Overdue), Frequency (dropdown: One-time/Monthly/Quarterly/Semi-Annual/Annual), Notes (long text). (3) 'Environmental Incidents' with columns: Incident Date (date), Location (text), Incident Type (dropdown: Spill/Release/Permit Exceedance/Enforcement Notice/Citizen Complaint/Agency Inspection), Volume/Quantity (text), Regulatory Notification Required (status: Yes-Immediate/Yes-24hr/Yes-Written Followup/No), Notification Status (status: Pending/Notified/Complete), Related Matter (connect to board 1), Assigned Attorney (people). Add automations: when Compliance Task Due Date is 14 days away, notify Assigned To; when Environmental Incident Regulatory Notification Required is Yes-Immediate, send urgent notification to Lead Attorney and Environmental Director; when Compliance Task is Overdue, escalate to General Counsel. Create Dashboard with: total environmental exposure (numbers), matters by type and phase (chart), upcoming compliance deadlines (table), incident trend (chart), liability by site (chart), insurance coverage gap analysis (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Environmental Compliance Sentinel
**Agent Purpose:** Monitor environmental compliance obligations, manage incident response workflows, and track aggregate environmental liability exposure.

**Triggers:**
- Environmental incident reported (new item in Incidents board)
- Compliance task deadline approaching (30/14/7 days)
- Regulatory agency communication received (new enforcement notice, NOV)
- Quarterly environmental liability reserve review initiated
- New environmental regulation proposed or finalized

**Actions:**
- Generate incident response checklists based on incident type and jurisdiction
- Route regulatory notifications to correct agencies within required timeframes
- Track remediation milestones and flag when projects fall behind schedule
- Calculate aggregate environmental liability exposure across all sites
- Analyze environmental monitoring data trends and flag anomalies
- Generate quarterly environmental legal reports for management and board

**Data Required:**
- Environmental matter database with all active sites and litigation
- Regulatory compliance calendars by jurisdiction
- Environmental monitoring data from field operations
- Insurance policy details and coverage triggers
- Historical remediation cost data by site type and contamination

**Autonomy Level:** Human-in-the-Loop
Agent monitors, alerts, and generates reports autonomously. Regulatory notifications require attorney review before submission. Settlement decisions require General Counsel and business unit approval. Liability reserve changes require CFO approval.

**Example Interaction:**
> At 2:47 AM, an operations alert reports a 500-barrel crude oil release from a pipeline leak in Weld County, Colorado. The Environmental Compliance Sentinel immediately activates the Colorado-specific spill response protocol: (1) confirms the spill exceeds the reportable quantity threshold (1 barrel for Colorado), (2) generates the COGCC (Colorado Oil and Gas Conservation Commission) and EPA Region 8 notification forms pre-populated with incident details, (3) creates a matter in the Environmental Matters board with initial liability estimate of $750K–$2.5M based on similar incidents in the same county, (4) alerts the lead environmental attorney, the VP of Operations, and the insurance broker, (5) identifies that the company's pollution legal liability policy has a $100K deductible and $10M per-occurrence limit—adequate for the estimated range, and (6) creates a 30-item compliance task list covering the 30/60/90-day regulatory milestones. By the time the legal team arrives at 7:00 AM, the regulatory notifications are drafted, the incident response team is mobilized, and the matter file is organized.

---

### Use Case 5: Litigation & Dispute Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies carry large litigation portfolios—often 200–1,000+ active matters including royalty disputes, surface damage claims, personal injury, employment matters, commercial disputes, securities litigation, and regulatory enforcement. Outside counsel spend is a major cost center ($20–100M+ annually for large companies), but managing budgets, staffing, and performance across 100+ law firms is largely manual. Matter management systems like Aderant or TeamConnect provide case tracking but poor workflow automation. E-billing systems (Legal Tracker, Brightflag) handle invoices but don't connect to strategy. Legal departments lack real-time visibility into total litigation exposure, can't easily identify which outside firms deliver the best outcomes per dollar, and spend enormous time on status reporting that could be automated.

#### The Solution
monday.com Work Management replaces or supplements legacy matter management with a workflow-driven litigation platform. Each matter is a board item with columns for case details, key dates, assigned counsel, budget, exposure assessment, and litigation phase. Sub-items track motions, depositions, discovery deadlines, and settlement discussions. Automations enforce litigation hold preservation notices, trigger deadline-driven workflows (discovery responses, motion filing), and generate management reports. monday AI can analyze litigation portfolio trends, predict case outcomes based on historical data, and summarize deposition transcripts and lengthy court filings. Dashboards provide real-time views of total litigation exposure, budget performance by outside firm, and matter pipeline by category.

#### The Outcome
- Real-time litigation portfolio visibility replacing monthly manual reports
- 25% reduction in outside counsel spend through better budget management and firm performance tracking
- Automated litigation hold compliance reducing spoliation risk
- 50% faster matter intake and assignment process

#### Discovery Questions
1. "How many active litigation matters is your legal department managing, and what's your annual outside counsel spend?"
2. "How do you currently assess and report total litigation exposure to the board and audit committee?"
3. "What's your matter management system today, and how well does it support workflow automation vs. just data storage?"
4. "How do you evaluate outside counsel performance—are you tracking outcomes, budgets, and efficiency systematically?"
5. "How are you handling litigation hold preservation notices—is that process automated or manual?"

#### Industry Context
Royalty disputes are among the most common litigation in upstream O&G—owners challenge deductions, calculation methods, or underpayment. Surface damage claims arise from drilling operations on private land. Securities litigation risk increases with reserves restatements or ESG disclosure issues. Litigation holds (preservation notices) are legally required when litigation is reasonably anticipated—failure to preserve can result in adverse inference instructions or sanctions. E-billing guidelines (UTBMS codes, Litigation Advisor billing rules) standardize how outside counsel bills are submitted and reviewed.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Litigation Management system with these boards: (1) 'Litigation Portfolio' with columns: Matter Number (text), Case Name (text), Court/Venue (text), Matter Type (dropdown: Royalty Dispute/Surface Damage/Personal Injury/Commercial/Employment/Securities/Environmental/Regulatory Enforcement/IP/Tax/Other), Business Segment (dropdown: Upstream/Midstream/Downstream/Renewables/Corporate), Role (dropdown: Plaintiff/Defendant/Third Party/Intervenor), Lead In-House Attorney (people), Outside Counsel Firm (text), Outside Counsel Lead (text), Litigation Phase (status: Pre-Suit/Filed/Discovery/Motions/Mediation/Trial Prep/Trial/Post-Trial/Appeal/Settled/Closed), Exposure Low (numbers), Exposure High (numbers), Reserve (numbers), Budget (numbers), Actual Spend (numbers), Settlement Authority (numbers), Key Deadline (date), Status (status: Active/Settled/Closed-Won/Closed-Lost/Dismissed). (2) 'Litigation Tasks & Deadlines' with columns: Matter (connect to board 1), Task (text), Task Type (dropdown: Discovery Response/Deposition/Motion Filing/Brief/Mediation/Expert Report/Trial Date/Appeal Deadline/Other), Due Date (date), Assigned To (people), Status (status: Upcoming/In Progress/Filed/Complete/Continued), Court-Ordered (status: Yes/No), Notes (long text). (3) 'Outside Counsel Performance' with columns: Firm Name (text), Practice Area (dropdown), Matters Assigned (numbers), Total Billed (numbers), Budget Variance % (numbers), Average Matter Duration (numbers), Win Rate % (numbers), Client Satisfaction (numbers — 1 to 5), Diversity Score (numbers), Status (status: Preferred/Approved/Under Review/Restricted). Add automations: when Litigation Task Due Date is 14 days away and Court-Ordered is Yes, send urgent notification; when Actual Spend exceeds 80% of Budget, notify Lead In-House Attorney; when Matter is created, trigger litigation hold workflow. Create Dashboard with: total portfolio exposure range (numbers), matters by type and phase (chart), outside counsel spend vs. budget (chart), upcoming deadlines (table), matter resolution trend (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Litigation Portfolio Analyst
**Agent Purpose:** Analyze the litigation portfolio, predict outcomes, manage outside counsel performance, and automate litigation reporting.

**Triggers:**
- New matter created in portfolio
- Quarterly litigation reserve review initiated
- Outside counsel invoice submitted
- Court filing or order received
- Board/audit committee reporting cycle

**Actions:**
- Analyze litigation portfolio trends and predict quarterly reserve adjustments
- Benchmark outside counsel performance (cost, duration, outcomes) across firms
- Summarize lengthy court filings, depositions, and motions into brief attorney summaries
- Generate board-ready litigation reports with exposure analysis
- Flag matters where actual spend is trending over budget with root cause analysis
- Automate litigation hold notices with custodian tracking and acknowledgment

**Data Required:**
- Complete matter database with outcomes and financials
- Outside counsel billing data (UTBMS coded)
- Historical case outcome data by matter type, venue, and counsel
- Litigation reserve methodology and assumptions
- Court docket systems for filing tracking

**Autonomy Level:** Human-in-the-Loop
Agent analyzes and generates reports autonomously. Reserve recommendations require General Counsel and CFO review. Outside counsel selection requires GC approval. Settlement recommendations require authorization per delegation matrix.

**Example Interaction:**
> During the Q4 litigation reserve review, the Litigation Portfolio Analyst examines 347 active matters with aggregate reserves of $124M. It identifies 12 matters where reserves should be adjusted: 5 upward (total +$8.2M) based on unfavorable recent rulings and discovery developments, 4 downward (-$3.1M) following favorable mediation sessions, and 3 where new information changes the probability assessment from "possible" to "probable" (requiring $11.4M in new reserves). The agent generates a detailed memo for each adjustment with supporting evidence, maps the impact to financial statements, and prepares the audit committee presentation. It also flags that outside counsel Firm X has billed 40% over budget on 3 of its 7 matters, while Firm Y—handling similar matter types—is 10% under budget with comparable outcomes. The GC receives a recommendation to shift 2 pending matter assignments from Firm X to Firm Y, with projected savings of $800K.

---

### Use Case 6: Outside Counsel & Legal Spend Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies spend $20–100M+ annually on outside counsel across litigation, regulatory, transactional, and specialized energy practices. Managing this spend is a nightmare: invoices arrive in different formats, UTBMS task codes are inconsistently applied, budget overruns are discovered after the fact, and there's no systematic way to evaluate which firms deliver the best value. Legal operations teams spend 30–40% of their time processing and reviewing invoices rather than driving strategy. Rate negotiations happen annually with limited data on actual firm performance. Diversity spending commitments are tracked manually. Most e-billing tools (Legal Tracker, Brightflag, CounselLink) are expensive, inflexible, and poorly integrated with matter management.

#### The Solution
monday.com Work Management creates a legal spend management platform that connects matter performance to firm performance to invoice processing. Boards track firm relationships, rate cards, diversity metrics, and performance scores. Invoice processing workflows route bills through automated compliance checking (UTBMS code validation, rate cap enforcement, block billing detection), attorney review, and payment approval. Automations flag budget variances, enforce billing guidelines, and generate spend analytics. monday AI can analyze invoice line items for billing compliance, compare firm performance across similar matters, and predict annual legal spend based on current matter trajectories.

#### The Outcome
- 15–20% reduction in outside counsel spend through better budget management and billing compliance
- 80% reduction in invoice processing time through automated compliance checking
- Data-driven outside counsel selection replacing relationship-based decisions
- Real-time legal spend visibility replacing quarterly retrospective reports

#### Discovery Questions
1. "What's your annual outside counsel spend, and how many firms are you working with?"
2. "What e-billing or legal spend management tool are you using today?"
3. "How do you evaluate outside counsel performance—is it systematic or anecdotal?"
4. "What percentage of invoices require adjustment after review, and what's the average write-down?"
5. "Do you have diversity spending targets for outside counsel, and how do you track them?"

#### Industry Context
UTBMS (Uniform Task-Based Management System) codes standardize legal billing line items. Block billing (lumping multiple tasks into one time entry) is a common compliance issue. LEDES (Legal Electronic Data Exchange Standard) is the electronic billing format. Alternative fee arrangements (AFAs) include fixed fees, success fees, and blended rates—increasingly common in energy litigation. Most Am Law 100 firms have dedicated energy practices with specialized rate cards. Legal operations is a growing function in energy companies, focused on efficiency, technology, and spend optimization.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Legal Spend Management system with these boards: (1) 'Outside Counsel Directory' with columns: Firm Name (text), Primary Contact (text), Practice Areas (dropdown: Litigation/Regulatory/Transactional/Environmental/Employment/IP/Tax/Energy-Specialized), Rate Card Year (numbers), Partner Rate (numbers), Associate Rate (numbers), Annual Spend (numbers), Matters Assigned (numbers), Performance Score (numbers — 1 to 10), Diversity Certification (status: Yes/No/Pending), Fee Arrangement (dropdown: Hourly/Fixed/Blended/Success/Hybrid), Status (status: Preferred/Approved/Probation/Terminated). (2) 'Invoice Processing' with columns: Firm (connect to board 1), Invoice Number (text), Invoice Date (date), Matter (text), Billed Amount (numbers), Approved Amount (numbers), Adjustment Amount (numbers), Adjustment Reason (dropdown: Rate Exceeded/Block Billing/Excessive Research/Overhead Charges/Staffing Issue/No Adjustment), Reviewer (people), Status (status: Received/Auto-Checked/Attorney Review/Approved/Paid/Disputed), Payment Date (date). (3) 'Budget Tracking' with columns: Matter (text), Firm (connect to board 1), Annual Budget (numbers), YTD Spend (numbers), Remaining Budget (numbers), Budget Utilization % (numbers), Projected Annual (numbers), Variance (numbers), Alert Level (status: On Track/Watch/Over Budget/Critical). Add automations: when Invoice received, run auto-compliance check and route to reviewer; when Budget Utilization exceeds 80%, notify in-house attorney and legal ops; when Performance Score drops below 5, flag for GC review. Create Dashboard with: total annual spend by firm (chart), spend by practice area (chart), invoice adjustment rate by firm (chart), budget performance (table), diversity spend tracking (chart), monthly spend trend (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Legal Spend Optimizer
**Agent Purpose:** Analyze outside counsel invoices for billing compliance, track firm performance, and recommend spend optimization strategies.

**Triggers:**
- New invoice received from outside counsel
- Monthly spend report cycle
- Budget threshold exceeded (80%, 100%)
- Annual rate negotiation period approaching
- New matter requiring outside counsel assignment

**Actions:**
- Scan invoice line items for billing guideline violations (block billing, rate overages, prohibited charges)
- Calculate invoice adjustment recommendations with detailed reasoning
- Benchmark firm performance across comparable matters (cost, speed, outcomes)
- Recommend outside counsel for new matter assignments based on expertise, performance, and rate
- Generate annual firm performance scorecards for rate negotiations
- Project annual legal spend and flag budget risks

**Data Required:**
- Outside counsel billing guidelines and rate cards
- Historical invoice data (3+ years)
- Matter outcome and duration data by firm
- Firm diversity certifications and spend reports
- Industry benchmarks for legal spend by matter type

**Autonomy Level:** Human-in-the-Loop
Agent auto-checks invoices and generates recommendations. Invoice adjustments >$10K require attorney review. Firm assignments require GC approval. Rate negotiations are attorney-led with agent data support.

**Example Interaction:**
> The Legal Spend Optimizer processes 47 invoices totaling $3.8M for the month. It auto-checks each against the company's billing guidelines and flags 11 invoices with issues: 4 contain block billing entries totaling $127K, 3 have associate rates exceeding the approved rate card by $15–40/hour ($43K impact), 2 include charges for services not pre-approved (mock trial consultant, $85K), and 2 have excessive legal research charges (>10% of total bill). The agent generates detailed adjustment memos, reducing the total approved amount to $3.54M (7% write-down). It also notes that Firm Z, which handles pipeline regulatory matters, has billed $1.2M against a $900K annual budget with 4 months remaining—recommending an immediate budget conversation with the firm's relationship partner. The Legal Ops Director reviews the adjustments on her dashboard and approves all but one (the mock trial charge, which she confirms was verbally approved but not documented—she approves payment and notes the process gap).

---

### Use Case 7: Energy Transition & Renewables Legal Support

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The energy transition is creating entirely new categories of legal work for which traditional oil and gas legal departments are unprepared. Renewable energy projects require PPAs, interconnection agreements, renewable energy certificate (REC) contracts, tax equity partnership structures (ITC/PTC), land leases for solar/wind (fundamentally different from mineral leases), and environmental permitting under different regulatory frameworks. Carbon capture projects need pipeline right-of-way agreements, Class VI well permits, 45Q tax credit documentation, and pore space ownership resolution. Hydrogen projects involve offtake agreements, electrolyzer procurement contracts, and emerging regulatory frameworks. Legal teams trained in traditional energy law are learning on the fly, outside counsel costs for specialized renewable work are premium, and the volume of new agreements is doubling annually as companies accelerate transition investments.

#### The Solution
monday.com Work Management creates a dedicated energy transition legal workstream that integrates with the broader legal management platform. Boards track renewable project legal milestones, from site control through commercial operation. Contract management boards are templated for renewable-specific agreement types (PPAs, interconnection agreements, EPC contracts, tax equity documents). Automations coordinate between legal, development, finance, and engineering on project milestones. monday AI can compare PPA terms across the portfolio, identify non-standard provisions, and maintain a knowledge base of energy transition legal precedents. Dashboards show the entire renewable project pipeline with legal readiness status.

#### The Outcome
- 40% faster legal workstream for renewable project development
- Standardized templates and playbooks reducing outside counsel dependence for routine renewable agreements
- Portfolio-level visibility into energy transition legal commitments
- Reduced risk of non-standard provisions proliferating across renewable contracts

#### Discovery Questions
1. "How many renewable energy or energy transition projects are you currently developing, and what types (solar, wind, battery, CCUS, hydrogen)?"
2. "Does your in-house legal team have renewable energy expertise, or are you relying primarily on outside counsel?"
3. "How many PPAs has your company executed, and are you seeing consistency in terms or significant variation?"
4. "Are you pursuing any carbon capture or hydrogen projects, and how far along is the legal framework for those?"
5. "What's your company's stated energy transition investment target, and how is that translating into legal workload?"

#### Industry Context
ITC (Investment Tax Credit) and PTC (Production Tax Credit) are federal incentives for renewable energy, recently extended and expanded by the Inflation Reduction Act. Tax equity structures (partnership flip, sale-leaseback, inverted lease) allow project developers to monetize tax credits by partnering with tax equity investors. Interconnection agreements define how a renewable project connects to the grid—FERC's interconnection queue backlog is a major bottleneck. RECs (Renewable Energy Certificates) represent the environmental attributes of renewable generation. Class VI wells are EPA-permitted injection wells for CO2 sequestration under the Underground Injection Control program. Pore space ownership (who owns the underground space for CO2 storage) varies by state and is unsettled in many jurisdictions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Energy Transition Legal Tracker with these boards: (1) 'Transition Projects' with columns: Project Name (text), Project Type (dropdown: Solar/Wind-Onshore/Wind-Offshore/Battery Storage/CCUS-Carbon Capture/Hydrogen-Green/Hydrogen-Blue/Biogas/Geothermal/Other), Capacity MW or MTPA (numbers), Location (text), State (dropdown), Development Phase (status: Site Control/Permitting/PPA Negotiation/Interconnection/Financing/Construction/COD/Operating), Legal Readiness (status: Not Started/In Progress/Substantially Complete/Clear), Lead Attorney (people), Outside Counsel (text), Target COD (date), Estimated Project Value (numbers). (2) 'Transition Agreements' with columns: Project (connect to board 1), Agreement Type (dropdown: PPA/Interconnection/EPC/O&M/Land Lease/Tax Equity/REC Purchase/Carbon Offtake/Pore Space/Class VI Permit/45Q Documentation/Other), Counterparty (text), Status (status: Template/Drafting/Negotiation/Execution/Active/Expired), Key Terms Summary (long text), Execution Date (date), Term Years (numbers), Annual Value (numbers), Key Dates (date), Assigned Attorney (people). (3) 'Transition Knowledge Base' with columns: Topic (text), Category (dropdown: PPA Best Practices/Tax Equity Structures/Interconnection/Carbon Capture Regulatory/Hydrogen Framework/Permitting/Land Rights/Emerging Issues), Summary (long text), Source Document (link), Last Updated (date), Expert Contact (people). Add automations: when Project Development Phase changes, update Legal Readiness checklist; when Agreement is in Negotiation for >60 days, escalate to Lead Attorney; when new Knowledge Base item added, notify relevant attorneys. Create Dashboard with: project pipeline by type (chart), legal readiness across projects (battery), agreement status summary (chart), upcoming key dates (timeline), project value by type (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Energy Transition Legal Advisor
**Agent Purpose:** Accelerate energy transition legal work by maintaining institutional knowledge, standardizing agreements, and tracking regulatory developments.

**Triggers:**
- New energy transition project created
- PPA or other transition agreement enters negotiation
- Regulatory development affecting renewables/CCUS/hydrogen
- Tax equity closing milestone approached
- Quarterly portfolio review scheduled

**Actions:**
- Generate project-specific legal checklists based on project type and jurisdiction
- Compare new PPA terms against portfolio benchmarks and flag outliers
- Track interconnection queue positions and regulatory milestones
- Summarize new IRA guidance, Treasury regulations, and state renewable policies
- Recommend tax equity structure based on project characteristics and market conditions
- Maintain and update the transition knowledge base with new precedents and learnings

**Data Required:**
- Executed transition agreement database with key terms
- Regulatory trackers for IRA implementation, state renewable policies
- Interconnection queue data from ISOs/RTOs
- Tax equity market terms and investor preferences
- Energy transition project pipeline and development schedules

**Autonomy Level:** Human-in-the-Loop
Agent generates checklists, comparisons, and recommendations autonomously. All agreement negotiations and regulatory positions require attorney direction. Tax equity structure recommendations require tax counsel and finance review.

**Example Interaction:**
> A new 150 MW solar + 75 MW battery storage project in ERCOT is approved for development. The Energy Transition Legal Advisor generates a 34-item legal checklist covering: (1) surface lease negotiation (flagging that Texas landowners in this county typically request $1,200–1,500/acre/year based on 3 recent comparable transactions), (2) ERCOT interconnection application requirements and current queue timeline (18–24 months based on recent approvals), (3) PPA strategy recommendation (corporate PPA vs. utility PPA, with market analysis showing corporate PPAs in ERCOT currently pricing at $32–38/MWh for 15-year terms), (4) tax equity documentation requirements for ITC election under the IRA (including prevailing wage and apprenticeship requirements for full credit value), and (5) battery storage-specific agreements (tolling vs. merchant, ERCOT ancillary services participation). The agent identifies that the company's standard PPA template needs 3 updates based on recent ERCOT protocol changes and drafts the amendments for attorney review.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| JOA | Joint Operating Agreement — governs co-ownership of oil and gas properties |
| Farmout | Agreement transferring right to earn working interest by drilling |
| PSC | Production Sharing Contract — international petroleum agreement structure |
| PPA | Power Purchase Agreement — long-term contract to buy renewable electricity |
| HBP | Held by Production — lease maintained by ongoing production beyond primary term |
| Pugh Clause | Lease provision releasing undeveloped depths or non-pooled acreage |
| Division Order | Document specifying ownership percentages for revenue distribution |
| FERC | Federal Energy Regulatory Commission — interstate energy regulator |
| COPAS | Council of Petroleum Accountants Societies — JV accounting standards |
| CERCLA/Superfund | Federal law governing contaminated site cleanup |
| PRP | Potentially Responsible Party — entity liable for environmental cleanup |
| UTBMS | Uniform Task-Based Management System — legal billing code standard |
| ITC/PTC | Investment Tax Credit / Production Tax Credit for renewable energy |
| Tax Equity | Financial structure to monetize renewable energy tax credits |
| REC | Renewable Energy Certificate — tradeable proof of renewable generation |
| Class VI Well | EPA-permitted CO2 injection well for carbon sequestration |
| 45Q | Federal tax credit for carbon capture and sequestration |
| ERCOT | Electric Reliability Council of Texas — Texas grid operator |
| ISO/RTO | Independent System Operator / Regional Transmission Organization |
| Force Majeure | Contract clause excusing performance due to extraordinary events |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| General Counsel | Overall legal strategy, enterprise risk, board advisory | Decision-maker |
| VP/Deputy GC Litigation | Litigation portfolio, dispute strategy, outside counsel management | Decision-maker |
| VP/Deputy GC Commercial | Transactional work, contract negotiations, M&A | Decision-maker |
| VP Regulatory/Government Affairs | Regulatory proceedings, policy advocacy, government relations | Decision-maker |
| Senior Land Counsel | Mineral rights, lease management, title issues | Influencer |
| Environmental Counsel | Environmental compliance, remediation, climate litigation | Influencer |
| Energy Transition Counsel | Renewable projects, carbon capture, tax equity structures | Influencer |
| Legal Operations Director | Technology, spend management, process optimization | Influencer |
| Paralegal Manager | Document management, filing coordination, legal support | User |
| Chief Compliance Officer | Ethics, anti-corruption, sanctions, trade compliance | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Finance | Litigation reserves, contract financial terms, tax equity structures | Financial close, reserve management |
| Operations | Regulatory compliance, permits, lease obligations, environmental incidents | Operations management, incident tracking |
| Land/Real Estate | Lease management, surface rights, right-of-way acquisition | Land management workflows |
| HR | Employment litigation, investigations, policy review | HR case management |
| IT | eDiscovery, legal technology, data privacy | IT project management |
| Government Affairs | Regulatory proceedings, legislative tracking, lobbying compliance | Stakeholder management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| iManage / NetDocuments | Document management for law departments | Not direct replacement — complement with workflow orchestration around documents |
| TeamConnect / Aderant | Matter management — case tracking and reporting | More flexible, modern UX, better cross-functional collaboration and automation |
| Legal Tracker / Brightflag | E-billing and spend management | Integrate spend management into broader legal operations platform |
| ContractPodAi / Ironclad | CLM — contract lifecycle management | Energy-specific customization advantage, better integration with other business workflows |
| P2 Land / Quorum Land | Land management — lease tracking specialized for energy | Orchestration layer for land workflows; complement rather than replace data of record |
| Spreadsheets / Email / SharePoint | The real competitor — most legal workflow is manual | Direct replacement for tracking, coordination, reporting, and deadline management |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We use iManage/NetDocuments for everything" | "Those are excellent document repositories. But they don't manage workflows—who's doing what, by when, and what's the status. monday.com orchestrates the work around the documents." |
| "Legal data is too sensitive for a general platform" | "monday.com supports enterprise security controls, SSO, data residency, and granular permissions. Your attorneys see only their matters. Many Fortune 500 legal departments are on the platform." |
| "Our attorneys won't adopt new technology" | "That's actually our strength—monday.com is intuitive enough that attorneys adopt without training. We've seen 85%+ adoption in legal departments because it replaces the inbox chaos they already hate." |
| "We just implemented a CLM/matter management tool" | "Great—that handles one slice. What about regulatory proceedings, outside counsel performance, energy transition projects, and the 100 other workflows in spreadsheets? monday.com connects it all." |
| "Energy legal is too specialized" | "Exactly why generic legal tech fails. monday.com's flexibility lets you build energy-specific workflows—JOA tracking, lease management, regulatory dockets—configured by your team, not a vendor's implementation consultant." |

## Proof Points
*(To be populated with customer references)*
- [Energy company CLM implementation]
- [Utility regulatory proceedings management]
- [Oil and gas land department modernization]
- [Legal operations transformation in energy]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
