# Banking × PMO Playbook

## Overview

The Project Management Office (PMO) in banking institutions serves as the central nervous system for strategic execution, overseeing portfolios that can span hundreds of concurrent initiatives — from core banking system migrations and regulatory remediation programs to digital transformation efforts and branch modernization. Banking PMOs typically operate under a tiered governance model: an Enterprise PMO (EPMO) sets standards and portfolio-level prioritization, while divisional PMOs (within Retail Banking, Wholesale Banking, Wealth Management, etc.) manage execution within their domains.

The regulatory environment fundamentally shapes how banking PMOs operate. Every major initiative must account for OCC, FDIC, Federal Reserve, and potentially international regulatory requirements (Basel III/IV, DORA, PSD2). This means PMOs carry heavy compliance documentation burdens, stage-gate processes with mandatory risk reviews, and audit trail requirements that would be foreign to PMOs in less regulated industries. A single core banking migration can involve 200+ workstreams, 18-24 month timelines, and $50M-$500M budgets.

Banking PMOs also face unique challenges around change management velocity. Regulatory deadlines are immovable — a CECL implementation or LIBOR transition doesn't wait because your project is behind schedule. This creates a constant tension between the desire for agile delivery and the reality of compliance-driven waterfall gates. Most banking PMOs operate hybrid methodologies, and the tooling fragmentation that results (Jira for tech teams, MS Project for traditional PM, SharePoint for documentation, Excel for everything else) is a persistent pain point.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Banking PMOs manage exponentially growing portfolios (digital, regulatory, ESG) without proportional headcount increases; PMO teams of 15-25 oversee 100+ active projects |
| 2 | Consolidate Tech Stack with AI | High | Average banking PMO uses 6-8 tools (MS Project, Jira, ServiceNow, SharePoint, Excel, PowerBI, Clarity, custom); consolidation reduces risk and cost |
| 3 | Replace or Radically Augment Headcount | Medium-High | Junior PM roles (status collection, report generation, RAID log maintenance) are prime automation targets, freeing senior PMs for stakeholder management |

## Prioritized Use Cases

---

### Use Case 1: Enterprise Portfolio Dashboard & Health Scoring

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking PMOs spend 30-40% of their time aggregating project status across disparate tools and business units. The weekly "status collection ritual" involves chasing 50+ project managers for updates, manually consolidating RAG statuses into PowerPoint decks for the CIO and steering committees. By the time the portfolio view is assembled (often Thursday/Friday), the data is already stale. Worse, RAG statuses are subjective — a PM reporting "green" on a $100M core banking migration might be hiding scope creep that won't surface until a stage-gate review. The bank's leadership makes resource allocation decisions on data that's 5-7 days old and potentially inaccurate.

#### The Solution
monday.com Work Management as the single portfolio layer across all project types. Each project lives as a high-level item with standardized fields: RAG status (formula-driven, not subjective), budget consumed vs. planned, milestone completion %, regulatory dependency flags, and risk score. Sub-items break down into workstreams. Connected boards link divisional portfolios to the EPMO view. Dashboard widgets show portfolio health by business unit, budget burn rates, resource utilization heat maps, and regulatory deadline proximity. monday.com AI Sidekick surfaces anomalies — projects where timeline is green but budget burn rate suggests trouble.

#### The Outcome
- Portfolio status assembly time reduced from 2 days to real-time
- 85% reduction in manual status collection effort
- Early detection of at-risk projects 3-4 weeks sooner through AI-driven anomaly detection
- Single source of truth for steering committee decisions

#### Discovery Questions
1. "How many active projects are in your current portfolio, and how many tools do your PMs use to manage them?"
2. "Walk me through your weekly status reporting cycle — how long does it take from first request to final steering committee deck?"
3. "Have you ever had a project that was reporting green suddenly flip to red? What was the cost of that late detection?"
4. "How do you currently flag projects with regulatory deadline risk versus those with internal-only deadlines?"
5. "What's your CIO's biggest frustration with portfolio visibility today?"

#### Industry Context
Banking portfolios typically categorize projects as: Run-the-Bank (RTB) vs. Change-the-Bank (CTB), with typical 60/40 to 70/30 budget splits. Regulatory projects get automatic "must-do" classification and can't be deprioritized. Understanding the bank's fiscal year planning cycle (usually Q3-Q4 for next year) is critical for timing the conversation. Key acronyms: EPMO (Enterprise PMO), BRD (Business Requirements Document), PIR (Post-Implementation Review), MRA/MRIA (Matter Requiring Attention / Immediate Attention — regulatory findings).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Banking Enterprise Portfolio Dashboard. Create a main board called 'Enterprise Portfolio' with columns: Project Name (text), Business Unit (dropdown: Retail Banking, Wholesale Banking, Wealth Management, Capital Markets, Risk & Compliance, Technology), Project Type (dropdown: Regulatory, Digital Transformation, Infrastructure, Process Improvement, M&A Integration), Overall RAG (status: On Track/At Risk/Critical/On Hold/Complete), Budget Approved (numbers, USD), Budget Consumed (numbers, USD), Budget Health (formula: if Budget Consumed/Budget Approved > 0.9 then 'Critical' elif > 0.75 then 'At Risk' else 'On Track'), Milestone Completion % (numbers), Regulatory Deadline (date), Project Sponsor (people), PM Lead (people), Risk Score (numbers 1-10), Last Updated (date). Add sub-items for workstreams. Create a Dashboard with widgets: portfolio by RAG status (chart), budget burn by business unit (chart), regulatory deadline timeline (timeline view), projects at risk table (filtered to At Risk + Critical), resource allocation by department. Add automations: when Last Updated is more than 7 days ago notify PM Lead 'Please update project status'; when Budget Health changes to Critical notify Project Sponsor; when Regulatory Deadline is within 30 days and Overall RAG is not On Track, notify channel. Create a Kanban view grouped by Business Unit and a Timeline view showing all projects with Regulatory Deadline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio Sentinel
**Agent Purpose:** Continuously monitor portfolio health indicators and proactively surface risks before they become crises.

**Triggers:**
- Daily at 7:00 AM ET scan all active projects
- When any project's Budget Consumed exceeds 75% of Budget Approved
- When a Regulatory Deadline is within 45 days and milestone completion is below 80%
- When Last Updated exceeds 5 business days
- When three or more sub-items in a project shift to "Blocked" status

**Actions:**
- Generate a daily Portfolio Intelligence Brief summarizing top 5 risks across the portfolio
- Calculate predictive completion dates based on milestone velocity trends
- Auto-escalate projects meeting risk criteria to the EPMO review queue
- Create a "Risk Alert" item in the EPMO board with analysis and recommended actions
- Send targeted notifications to project sponsors with specific concern details
- Generate weekly steering committee summary with trend analysis vs. prior week

**Data Required:**
- All project boards with milestone and budget data
- Historical project performance data for velocity calculations
- Regulatory calendar integration (compliance team's deadline tracker)
- Resource capacity data from HR/staffing boards

**Autonomy Level:** Human-in-the-Loop
Portfolio Sentinel auto-generates alerts and reports but escalation actions (reassigning resources, pausing projects, triggering stage-gate reviews) require EPMO Director approval. Risk scoring is autonomous; remediation recommendations require human decision.

**Example Interaction:**
> On Monday morning, Portfolio Sentinel detects that the CECL Phase 2 Implementation project has consumed 82% of its $12M budget but only completed 61% of milestones. It cross-references the regulatory deadline (March 31) with the current velocity and calculates a projected completion date of April 18 — 18 days past the regulatory deadline. The agent creates a Critical Risk Alert on the EPMO board: "CECL Phase 2: Budget overrun trajectory + regulatory deadline miss projected. Current burn rate: $420K/week vs. planned $310K/week. Recommend: (1) Emergency resource augmentation from Retail Banking PMO bench, (2) Scope review for Phase 2b deferral, (3) Regulatory liaison engagement for extension feasibility." The EPMO Director receives a notification with a one-click option to schedule an emergency steering committee review, which auto-populates the agenda with the agent's analysis.

---

### Use Case 2: Regulatory Program Tracking & Compliance Assurance

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banks face a relentless cadence of regulatory changes — on average, a global bank must track 200+ regulatory changes per year. Each regulatory program (Basel III.1 implementation, AML/KYC enhancement, DORA compliance, consumer protection updates) spawns dozens of workstreams across multiple business units. The PMO must maintain detailed evidence of compliance: who did what, when, with what approval, and how it was tested. Today this evidence lives in SharePoint document libraries, email chains, and spreadsheets — making audit preparation a multi-week scramble. A single MRA (Matter Requiring Attention) from a regulator can cost the bank $5-50M in remediation and reputational damage.

#### The Solution
monday.com Work Management with a dedicated Regulatory Program structure. Each regulation gets a board with workstreams as groups, requirements as items, and evidence artifacts linked as file columns. Status columns track: Requirement Interpreted → Controls Designed → Implemented → Tested → Evidenced → Audit-Ready. Connected boards link requirements to impacted business processes and systems. Automations enforce stage-gate discipline — items can't move to "Implemented" without mandatory approval from Compliance. Dashboard views show regulatory program health by deadline, gap analysis (requirements not yet addressed), and audit readiness scores.

#### The Outcome
- Audit preparation time reduced from 4-6 weeks to 3-5 days
- 100% traceability from regulatory requirement to implementation evidence
- Zero missed regulatory deadlines through proactive alerting
- 60% reduction in MRA/MRIA findings related to documentation gaps

#### Discovery Questions
1. "How many active regulatory programs is your PMO tracking right now, and what's the biggest one by budget or complexity?"
2. "When your examiners come in, how long does it take to assemble the evidence package for a specific regulation?"
3. "Have you received any MRAs or MRIAs in the last two years related to project execution or documentation gaps?"
4. "How do you currently track the dependency chain between a regulatory requirement, the business process it impacts, and the technology change needed?"
5. "What happens when a regulatory deadline changes or a new interpretation is issued mid-program?"

#### Industry Context
Key regulations banking PMOs manage: Basel III/IV (capital adequacy), CECL (credit loss accounting), BSA/AML (anti-money laundering), GDPR/CCPA (data privacy), SOX (financial controls), DORA (digital operational resilience — EU), CRA (Community Reinvestment Act). Exam cycles: OCC continuous supervision for large banks, FDIC periodic for community banks. Consent orders and enforcement actions are public and devastating. The term "three lines of defense" (1st: business, 2nd: risk/compliance, 3rd: internal audit) governs the governance model.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Program Tracker for a bank. Create a board called 'Regulatory Programs' with groups for each major regulation (Basel III.1, AML Enhancement, DORA Compliance, Consumer Data Privacy, CECL Phase 2). Each item represents a regulatory requirement with columns: Requirement ID (text), Requirement Description (long text), Impacted Business Unit (dropdown: Retail, Wholesale, Wealth, Capital Markets, Operations, Technology), Compliance Stage (status: Interpreting/Controls Design/Implementing/Testing/Evidenced/Audit-Ready), Regulatory Deadline (date), Owner (people), Compliance Reviewer (people), Evidence Attached (files), Risk Rating (dropdown: Critical/High/Medium/Low), Gap Status (status: Open Gap/Mitigated/Closed/N-A), Notes (long text). Add automations: when Compliance Stage changes to Implementing require approval from Compliance Reviewer; when Regulatory Deadline is within 60 days and Compliance Stage is not Testing or later, change Risk Rating to Critical and notify Owner; when Evidence Attached is updated and Compliance Stage is Evidenced, notify Compliance Reviewer for final sign-off. Create a Dashboard with: audit readiness by regulation (chart showing % items at Audit-Ready), open gaps by business unit (chart), regulatory deadline timeline (timeline), critical items table. Add a Calendar view showing all Regulatory Deadlines."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Compliance Compass
**Agent Purpose:** Automatically track regulatory requirement completion, flag evidence gaps, and generate audit-ready documentation packages.

**Triggers:**
- When a requirement item's Compliance Stage changes
- Weekly scan every Monday at 6:00 AM for approaching deadlines (30/60/90 day windows)
- When a new regulatory update is added to the program board
- When an examiner request is logged (manual trigger)
- When Evidence Attached column is updated

**Actions:**
- Validate evidence completeness against requirement checklist (are all required artifacts present?)
- Generate audit evidence package: compile all linked documents, approval timestamps, and status change history into a formatted report
- Create dependency impact analysis when a requirement changes scope
- Auto-assign remediation tasks when gaps are identified
- Generate examiner response drafts based on evidence trail
- Produce monthly regulatory program status report for Board Risk Committee

**Data Required:**
- Regulatory program boards with full history
- Document management integration (SharePoint/file storage)
- Compliance team's regulatory change feed
- Internal audit findings database

**Autonomy Level:** Escalation-Based
Evidence validation and report generation are fully autonomous. Gap identification triggers automatic task creation but flags for Compliance Officer review. Examiner response drafts always require human approval before submission.

**Example Interaction:**
> The OCC examination team sends a request for all evidence related to the bank's Basel III.1 Fundamental Review of the Trading Book (FRTB) implementation. The Compliance Compass agent receives the examiner request trigger and immediately compiles: 47 requirement items, their current compliance stages, 183 linked evidence documents, 12 approval chains with timestamps, and 3 outstanding gaps with documented remediation plans and target dates. Within 15 minutes, it produces a formatted evidence package organized by requirement category (market risk, credit risk, operational risk) with an executive summary noting: "94% of FRTB requirements at Audit-Ready status. 3 items in Testing phase with remediation target dates of Feb 28. All critical-path items complete." The package is routed to the Chief Compliance Officer for review before examiner submission.

---

### Use Case 3: Technology Demand Management & Intake

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking PMOs sit at the intersection of business demand and technology capacity. Every business unit wants technology resources — marketing wants a new digital campaign platform, risk wants model validation tools, operations wants RPA bots, and everyone wants AI. The intake process is typically a nightmare: business cases submitted via email or Word documents, reviewed in committee meetings with incomplete information, prioritized based on whoever has the loudest voice. The result: technology teams are overcommitted by 150-200%, projects start without proper scoping, and the PMO spends more time managing intake politics than delivering value. In a $500M technology budget, poor demand management can waste $50-75M annually on misaligned or abandoned projects.

#### The Solution
monday.com as the single demand intake and prioritization platform. A Form collects standardized business cases: strategic alignment, expected business value, regulatory mandate flag, estimated effort, required capabilities, and dependencies. Items flow through an automated pipeline: Submitted → PMO Triage → Business Case Review → Sizing → Prioritization Committee → Approved/Deferred/Declined. Scoring formulas calculate priority based on weighted criteria (strategic alignment, regulatory urgency, revenue impact, risk reduction, feasibility). Connected boards show technology team capacity and current commitments. Dashboard views give the CTO/CIO real-time visibility into the demand pipeline, committed capacity, and the "parking lot" of deferred requests.

#### The Outcome
- Demand intake cycle reduced from 6-8 weeks to 2 weeks
- 40% improvement in technology resource utilization through better demand matching
- Elimination of "shadow projects" that bypass governance
- Transparent prioritization reduces political friction by 70%

#### Discovery Questions
1. "How do business units currently submit technology project requests, and how many do you receive per quarter?"
2. "What percentage of approved projects actually start on time with the resources they were promised?"
3. "How do you currently balance regulatory must-do projects against strategic nice-to-have requests?"
4. "Have you ever discovered 'shadow IT' projects that bypassed the intake process? What happened?"
5. "If your CTO could see one view of the demand pipeline that doesn't exist today, what would it show?"

#### Industry Context
Banking technology organizations typically operate a "demand council" or "investment committee" that meets monthly/quarterly to prioritize. Run-the-Bank (RTB) vs. Change-the-Bank (CTB) allocation is a constant tension. Many banks use a "T-shirt sizing" approach (S/M/L/XL) for initial estimates before detailed scoping. The concept of "regulatory tax" — the percentage of technology capacity consumed by mandatory regulatory work — is a key metric (often 30-45% of total capacity).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Technology Demand Intake & Prioritization system for a bank. Create a Form called 'Technology Project Request' with fields: Project Name, Requesting Business Unit (dropdown: Retail Banking, Wholesale Banking, Wealth Management, Capital Markets, Risk, Compliance, Operations, Finance, HR), Business Sponsor (text), Project Description (long text), Strategic Alignment (dropdown: Revenue Growth, Cost Optimization, Regulatory Compliance, Risk Reduction, Customer Experience, Operational Excellence), Regulatory Mandate (yes/no), Expected Annual Business Value (numbers, USD), Estimated Effort (dropdown: Small <500hrs, Medium 500-2000hrs, Large 2000-5000hrs, XL 5000+hrs), Target Start Date (date), Target Completion Date (date), Key Dependencies (long text). Form submissions create items on a 'Demand Pipeline' board with additional columns: Pipeline Stage (status: Submitted/PMO Triage/Business Case Review/Sizing/Committee Review/Approved/Deferred/Declined), Priority Score (formula based on: Regulatory Mandate×40 + Strategic Alignment score×30 + Business Value score×20 + Feasibility×10), Assigned PM (people), Committee Decision Date (date), Decision Notes (long text). Create groups: New Requests, In Review, Approved Backlog, Active, Deferred, Declined. Add automations: when Pipeline Stage changes to PMO Triage assign to PMO Lead; when Pipeline Stage changes to Committee Review notify all committee members; when Regulatory Mandate is Yes auto-set priority boost. Create Dashboard with: demand by business unit (chart), pipeline funnel (chart), capacity vs. demand (numbers widget), approved backlog timeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Demand Analyst
**Agent Purpose:** Triage incoming technology requests, enrich business cases with historical data, and generate prioritization recommendations for the investment committee.

**Triggers:**
- When a new Form submission creates an item on the Demand Pipeline board
- 48 hours before each Investment Committee meeting
- When a project's estimated effort or business value changes significantly
- Monthly capacity refresh from technology resource boards

**Actions:**
- Auto-triage: classify request type (regulatory/strategic/operational), flag duplicates or overlaps with existing projects
- Enrich business case with comparable project data (similar past projects' actual effort, duration, and outcomes)
- Generate prioritization recommendation with narrative explanation
- Produce Investment Committee briefing deck: ranked demand list, capacity analysis, trade-off scenarios
- Flag requests that exceed current capacity thresholds with deferral recommendations
- Track demand trends by business unit over time for capacity planning

**Data Required:**
- Historical project portfolio data (actuals vs. estimates)
- Technology team capacity boards
- Strategic plan alignment criteria and weights
- Regulatory calendar for mandate verification

**Autonomy Level:** Human-in-the-Loop
Auto-triage and enrichment are autonomous. Prioritization recommendations are advisory — the Investment Committee makes final decisions. The agent prepares materials but doesn't approve or decline requests.

**Example Interaction:**
> A new request arrives from Wholesale Banking: "AI-Powered Trade Surveillance Enhancement" with an estimated $2.1M business value and regulatory mandate flag. Demand Analyst auto-classifies it as Regulatory + Strategic, identifies overlap with an existing "Market Surveillance Modernization" project in Capital Markets (potential consolidation opportunity), and pulls historical data showing that the bank's last three surveillance projects averaged 140% of initial effort estimates. It generates a triage note: "Recommend consolidation discussion with Capital Markets PMO before independent scoping. Historical data suggests effort estimate should be adjusted to Large (3,200 hrs) from Medium (1,800 hrs). Regulatory mandate confirmed via 2026 OCC examination priority letter. Recommend expedited committee review." The item is auto-moved to PMO Triage with the enriched analysis attached.

---

### Use Case 4: Resource Capacity Planning & Allocation

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banking PMOs wrestle with resource management across a complex matrix: full-time employees, contractors, offshore teams, and managed service providers — often 500-2,000+ technology resources across the portfolio. Resource managers maintain sprawling spreadsheets that are outdated the moment they're saved. PMs hoard resources "just in case," creating phantom allocations that make capacity planning fictional. When a critical regulatory project needs 15 senior Java developers, the PMO can't tell whether those resources exist in the organization, are truly allocated, or are sitting on a bench. The cost of poor resource management in a large bank: $10-20M annually in underutilization, over-reliance on expensive contractors, and project delays from resource conflicts.

#### The Solution
monday.com as the resource capacity and allocation platform. Each resource (employee/contractor) has a profile item with skills, certifications, current assignments, and availability. Project boards link to resource boards through connected columns, showing who's assigned where and at what allocation percentage. Workload views display capacity by team, skill set, and time period. Automations flag over-allocations (>100%) and under-allocations (<50%). Dashboard views give resource managers real-time visibility into bench strength, contractor dependency ratios, and skill gap analysis. AI Sidekick recommends optimal resource assignments based on skills match, availability, and project priority.

#### The Outcome
- Resource utilization improved from 65% to 85%
- 50% reduction in contractor spend through better internal resource matching
- Zero double-booking of critical resources
- 3-week reduction in average project start delay due to resource availability

#### Discovery Questions
1. "How many total technology resources (FTE + contractors) does your PMO manage across the portfolio?"
2. "Can you tell me right now, with confidence, which senior developers are available to start a new project next month?"
3. "What percentage of your project delays are caused by resource availability issues?"
4. "How do you currently manage the balance between full-time employees and contractors across programs?"
5. "What's your annual contractor spend, and how much of that do you believe is due to poor visibility into internal capacity?"

#### Industry Context
Banks typically have complex resource structures: onshore FTEs, nearshore contractors, offshore development centers (India, Eastern Europe), and managed service agreements. Regulatory requirements often mandate that certain roles (risk management, compliance) must be FTEs, not contractors. The "bench" concept — resources between projects — is a key PMO metric. Many banks track "productive utilization" (time on projects vs. administrative/training/bench time) as a KPI. Typical target: 75-80% productive utilization.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Resource Capacity Management system for a banking PMO. Create a board called 'Resource Pool' with columns: Resource Name (text), Employment Type (dropdown: FTE/Contractor/Offshore/Managed Service), Primary Skill (dropdown: Java, .NET, Python, Cloud/AWS, Data Engineering, Project Management, Business Analysis, QA/Testing, Security, Architecture), Certifications (tags: PMP, AWS, Azure, CISSP, Agile, Six Sigma), Team (dropdown: Retail Tech, Wholesale Tech, Infrastructure, Data & Analytics, Security, Enterprise Architecture), Current Allocation % (numbers), Available From (date), Hourly Rate (numbers, USD), Location (dropdown: Onshore/Nearshore/Offshore). Create a second board 'Project Assignments' with columns: Resource (connected to Resource Pool), Project (connected to Enterprise Portfolio), Role on Project (text), Allocation % (numbers), Start Date (date), End Date (date), Status (status: Active/Planned/Completed/On Hold). Add automations: when sum of Allocation % for a resource across active assignments exceeds 100, change item status to Over-Allocated and notify resource manager; when Allocation % drops below 50 and no upcoming assignments within 2 weeks, flag as Bench. Create a Dashboard with: utilization heat map by team (chart), FTE vs contractor ratio (chart), bench list (filtered table), skill availability matrix (table grouped by Primary Skill showing Available From), over-allocated resources alert (filtered table). Add Workload view on Project Assignments board."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Resource Optimizer
**Agent Purpose:** Intelligently match available resources to project needs, predict capacity gaps, and recommend staffing actions.

**Triggers:**
- When a new project is approved and moves to "Staffing" stage
- Weekly capacity scan every Monday
- When a resource's project assignment ends within 2 weeks
- When a project manager submits a resource request
- Monthly for forward-looking capacity forecast

**Actions:**
- Generate resource matching recommendations: top 3 candidates for each open role based on skills, availability, location, and cost
- Predict capacity gaps 60-90 days out based on project timelines and resource end-dates
- Recommend contractor-to-FTE conversion opportunities (resources on long-term assignments)
- Flag projects at risk of delay due to upcoming resource departures
- Produce monthly resource utilization report with trend analysis
- Auto-create requisition items when predicted gaps exceed internal capacity

**Data Required:**
- Resource Pool board with skills and availability
- Project Assignment boards with timeline data
- Project portfolio pipeline (upcoming approved projects)
- HR data for FTE headcount and hiring pipeline status

**Autonomy Level:** Human-in-the-Loop
Resource matching recommendations and gap predictions are autonomous. Actual resource assignments, contractor procurement, and hiring requisitions require resource manager approval.

**Example Interaction:**
> The recently approved "Real-Time Payments (RTP) Integration" project needs 3 senior Java developers, 2 cloud architects, and 1 security engineer starting March 1. Resource Optimizer scans the pool and recommends: "2 of 3 Java developers available internally — Raj (current project ends Feb 15, 95% skill match) and Maria (on bench since Jan 20, 88% skill match). Third Java developer: no internal match available; recommend contractor requisition with minimum 5 years banking payments experience. Cloud architects: 1 available internally (Chen, completing AML project Feb 28), 1 requires contractor. Security engineer: James available at 50% allocation — can split with current DORA project if approved." The agent creates a staffing plan item with cost comparison: internal-only option ($0 incremental) vs. hybrid option ($45K/month contractor cost) vs. fully staffed timeline impact.

---

### Use Case 5: Stage-Gate Governance & Approval Workflows

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking projects must pass through rigorous stage-gates: Initiation → Planning → Execution → UAT → Deployment → Post-Implementation Review. Each gate requires specific deliverables (BRD, technical design, test plans, operational readiness), approvals from multiple stakeholders (business sponsor, technology lead, risk officer, compliance, architecture review board), and evidence documentation. Today, gate reviews are calendar-driven meetings where PMs present PowerPoint decks and approvers rubber-stamp or send back. The PMO coordinator spends 10-15 hours per gate per project chasing approvals, scheduling reviews, and documenting decisions. For a portfolio of 80 active projects, that's a full-time job just managing gates — and gates still get bypassed when executives pressure for speed.

#### The Solution
monday.com automations and approval workflows to digitize the entire stage-gate process. Each project board has gate milestone items with mandatory checklist sub-items (deliverables required). Approval columns capture sign-offs from each required stakeholder. Automations enforce sequencing — a project cannot move to "Execution" until all "Planning" gate deliverables are marked complete and all approvers have signed off. Items automatically route to the next approver in sequence. Dashboard views show gate approval status across the portfolio, bottleneck analysis (which approver is holding up the most projects), and average gate cycle time.

#### The Outcome
- Gate review cycle time reduced from 3 weeks to 5 days
- 100% gate compliance — no bypasses without documented exception
- 75% reduction in PMO coordinator time spent on gate administration
- Full audit trail of every approval decision with timestamp

#### Discovery Questions
1. "How many stage-gates does a typical project pass through, and how many approvers are required at each gate?"
2. "What's the average time from gate submission to gate approval today?"
3. "Have you ever had an audit finding related to projects that bypassed governance gates?"
4. "How do you currently document gate decisions and the rationale behind them?"
5. "What percentage of gate review time is spent on administrative logistics versus actual quality review?"

#### Industry Context
The "three lines of defense" model means banking projects often need approvals from business (1st line), risk/compliance (2nd line), and sometimes internal audit (3rd line) at major gates. Architecture Review Boards (ARBs) are common gatekeepers for technology projects. "Change Advisory Boards" (CABs) govern production deployments. Many banks have a formal "Delegated Authority Matrix" specifying who can approve what based on project size and risk. Post-implementation reviews (PIRs) are often mandatory for regulatory projects but frequently skipped — an audit red flag.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Stage-Gate Governance system for banking projects. Create a board called 'Project Gate Tracker' with groups for each gate: Initiation Gate, Planning Gate, Execution Gate, UAT Gate, Deployment Gate, PIR Gate. Items represent individual projects passing through gates. Columns: Project Name (connected to Enterprise Portfolio), Gate Status (status: Not Started/Deliverables In Progress/Ready for Review/Under Review/Approved/Sent Back/Exception Granted), Gate Owner (people), Business Sponsor Approval (status: Pending/Approved/Rejected), Technology Lead Approval (status: Pending/Approved/Rejected), Risk Officer Approval (status: Pending/Approved/Rejected), Compliance Approval (status: Pending/Approved/Rejected), Architecture Review (status: Pending/Approved/Rejected/N-A), Submission Date (date), Target Approval Date (date), Actual Approval Date (date), Gate Cycle Time (formula: Actual Approval Date - Submission Date), Decision Notes (long text), Exception Justification (long text). Add sub-items for gate deliverables as a checklist. Add automations: when all deliverable sub-items are complete, change Gate Status to Ready for Review and notify Gate Owner; when Gate Status changes to Under Review, notify all approvers; when all approval columns are Approved, change Gate Status to Approved and move project to next gate group; when any approval is Rejected, change Gate Status to Sent Back and notify project PM. Create Dashboard with: gate approval funnel (chart), average cycle time by gate (chart), bottleneck analysis showing approver with most pending reviews (table), projects stuck at gate >10 days (filtered table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Gate Keeper
**Agent Purpose:** Orchestrate stage-gate reviews, ensure deliverable completeness, and eliminate approval bottlenecks.

**Triggers:**
- When all sub-item deliverables in a gate are marked complete
- When a gate has been "Under Review" for more than 3 business days
- Daily scan for approaching gate target dates
- When an approver rejects a gate submission
- When a gate exception is requested

**Actions:**
- Validate deliverable completeness: check that all required documents are attached, all mandatory fields populated
- Generate gate review briefing for approvers: project summary, deliverables index, risk assessment, recommendations
- Send escalation notifications to approvers who haven't responded within SLA
- Route rejection feedback to PM with specific remediation requirements
- Track and report gate cycle time trends to identify systemic bottlenecks
- Generate exception request documentation with risk analysis for governance committee

**Data Required:**
- Gate Tracker board with deliverable sub-items
- Project portfolio boards for context
- Approver availability/delegation data
- Gate SLA definitions by project type and size

**Autonomy Level:** Escalation-Based
Deliverable validation, notification routing, and reporting are fully autonomous. Exception approvals always route to the Governance Committee. Gate approval decisions remain with human approvers — the agent facilitates but never auto-approves.

**Example Interaction:**
> The "Digital Onboarding Platform" project submits its Execution Gate with 12 deliverables attached. Gate Keeper validates: technical design document ✓, updated BRD ✓, security assessment ✓, test strategy ✓, but notices the operational readiness plan is missing and the data privacy impact assessment has an outdated template version. It sends the PM a specific notification: "Gate submission incomplete. Missing: Operational Readiness Plan (template v3.2 required). Issue: Data Privacy Impact Assessment uses template v2.1 — current requirement is v3.0 per Policy Update #2025-47. Please remediate and resubmit." This prevents a reviewer from having to identify these issues manually, saving 2-3 days in the review cycle.

---

### Use Case 6: Vendor & Third-Party Program Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking PMOs increasingly manage programs with significant vendor components — system integrators (Accenture, Deloitte, Infosys), SaaS providers, and fintech partners. Each vendor has its own reporting cadence, milestone definitions, and deliverable formats. The PMO must track vendor performance against SLAs, manage change orders (which in banking can require procurement, legal, and compliance review), and ensure vendor deliverables meet the bank's quality and regulatory standards. With 20-40 active vendor engagements across the portfolio, the PMO lacks a unified view of vendor performance, spend, and risk. Vendor management often lives in procurement's system (Ariba, Coupa) while project delivery lives in the PMO's tools — creating a dangerous disconnect.

#### The Solution
monday.com as the vendor program management layer. Each vendor engagement has a board tracking: contract milestones, deliverable acceptance, SLA performance, change orders, risk items, and invoicing. Connected boards link vendor engagements to the projects they support. Automations track SLA compliance (deliverable due dates vs. actual delivery), flag overdue items, and route change orders through the approval chain (PM → PMO → Procurement → Legal → Compliance). Dashboard views show vendor performance scorecards, spend vs. contract, and risk heat maps across all vendor engagements.

#### The Outcome
- 30% reduction in vendor change order processing time
- Real-time vendor performance visibility replacing quarterly review cycles
- $2-5M annual savings from improved SLA enforcement and early issue detection
- Single view connecting vendor delivery to project outcomes

#### Discovery Questions
1. "How many active vendor/SI engagements does your PMO oversee, and what's the total annual spend?"
2. "How do you currently track whether a vendor is meeting their SLA commitments?"
3. "Walk me through what happens when a vendor needs a change order — how many approvals and how long?"
4. "Have you ever had a project delayed because a vendor issue wasn't visible until it was too late?"
5. "How do you share vendor performance data between your PMO and procurement?"

#### Industry Context
Banking vendor management is heavily regulated. OCC Bulletin 2013-29 (Third-Party Risk Management) and its 2023 interagency update require banks to maintain oversight of third-party service providers commensurate with the risk they pose. "Critical activities" (anything touching customer data, financial transactions, or regulatory compliance) require enhanced due diligence, ongoing monitoring, and contingency planning. Many banks classify vendors into tiers (Critical, Significant, General) with different oversight requirements. SOC 2 reports, business continuity plans, and cyber assessments are standard vendor requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Program Management system for a banking PMO. Create a board called 'Vendor Engagements' with columns: Vendor Name (text), Engagement Name (text), Vendor Tier (dropdown: Critical/Significant/General), Associated Project (connected to Enterprise Portfolio), Contract Value (numbers, USD), Spent to Date (numbers, USD), Engagement Status (status: Active/On Hold/Winding Down/Complete), Contract End Date (date), SLA Performance Score (numbers, 0-100), PM Lead (people), Vendor Manager (people), Risk Rating (dropdown: Low/Medium/High/Critical). Create a second board 'Vendor Deliverables & Milestones' with columns: Deliverable Name (text), Vendor Engagement (connected to Vendor Engagements), Due Date (date), Actual Delivery Date (date), Delivery Status (status: On Track/At Risk/Overdue/Delivered/Accepted/Rejected), Acceptance Criteria (long text), Review Notes (long text), SLA Met (formula: if Actual Delivery Date <= Due Date then Yes else No). Create a third board 'Change Orders' with columns: CO Number (text auto-increment), Vendor Engagement (connected), Description (long text), Cost Impact (numbers, USD), Timeline Impact (text), CO Status (status: Drafted/PM Review/PMO Review/Procurement Review/Legal Review/Compliance Review/Approved/Rejected), Requested By (people), Urgency (dropdown: Standard/Expedited/Emergency). Add automations: when Delivery Status is Overdue notify PM Lead and Vendor Manager; when CO Status changes step through approval chain automatically; when SLA Performance Score drops below 70 flag Vendor Engagement as High Risk. Create Dashboard: vendor performance scorecard (chart), spend tracking (chart), overdue deliverables (table), active change orders by status (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Vendor Watch
**Agent Purpose:** Monitor vendor performance across all engagements, predict delivery risks, and automate SLA tracking.

**Triggers:**
- When a deliverable due date is within 5 business days
- When a deliverable is marked Overdue
- When SLA Performance Score changes
- Monthly vendor performance review cycle
- When a new change order is submitted

**Actions:**
- Calculate rolling SLA performance scores based on deliverable history
- Generate vendor performance reports with trend analysis
- Predict at-risk deliverables based on vendor's historical delivery patterns
- Route change orders through the appropriate approval chain based on value thresholds
- Create quarterly vendor review packages with performance data, spend analysis, and recommendations
- Flag vendors approaching contract end dates for renewal planning

**Data Required:**
- Vendor Engagements and Deliverables boards
- Change Order board with approval history
- Contract terms and SLA definitions
- Historical vendor performance data

**Autonomy Level:** Human-in-the-Loop
Performance tracking, reporting, and alerting are autonomous. Vendor escalations, contract decisions, and change order approvals require human decision-makers.

**Example Interaction:**
> Vendor Watch detects that Infosys has missed 3 of the last 8 deliverable deadlines on the Core Banking Migration program, with an average delay of 4.2 business days. The SLA performance score has dropped from 88 to 71 over the past quarter. The agent generates an alert: "Infosys performance degradation detected on Core Banking Migration. SLA score trending below threshold (71, minimum 75 per contract). Pattern: delays concentrated in data migration workstream — possible resource constraint. Recommend: (1) Formal performance discussion per contract Section 8.3, (2) Request resource plan update, (3) Activate contingency plan for data migration workstream." It creates a risk item on the project board and schedules a vendor review meeting invitation.

---

### Use Case 7: Change Management & Organizational Readiness

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking transformation programs fail not because of technology — they fail because of people. A core banking migration, digital channel launch, or new regulatory process affects thousands of employees across branches, operations centers, and corporate offices. The PMO is often responsible for change management but treats it as a checkbox: a few training sessions, an email blast, and hope for the best. The result: 40-60% of banking technology projects fail to achieve expected benefits because end-users revert to old processes. The cost of failed adoption on a $50M core banking migration can be $10-20M in unrealized benefits.

#### The Solution
monday.com as the change management command center. Each major program has a change management board tracking: stakeholder analysis (who's impacted, their readiness level, their influence), communication plan (messages, channels, timing), training plan (sessions, materials, completion tracking), and adoption metrics (usage data, feedback, support tickets). Connected boards link change activities to project milestones. Automations trigger change activities at project milestones — when development hits UAT, training material development auto-starts; when deployment is scheduled, communication campaigns auto-launch. Forms collect stakeholder feedback and readiness assessments.

#### The Outcome
- 35% improvement in technology adoption rates post-implementation
- Structured change management for all Tier 1 and Tier 2 programs
- Real-time stakeholder sentiment tracking replacing annual surveys
- 25% reduction in post-go-live support tickets through better preparation

#### Discovery Questions
1. "How do you currently manage change management activities for major programs — is it embedded in the PMO or a separate function?"
2. "Can you think of a recent project where the technology worked fine but adoption was disappointing? What happened?"
3. "How do you assess organizational readiness before a major deployment?"
4. "What's your current approach to training — and how do you know if people actually learned what they needed?"
5. "How do you measure whether a transformation actually achieved its intended business benefits?"

#### Industry Context
Banking change management is complicated by regulatory training requirements (BSA/AML training, cybersecurity awareness), union considerations in some institutions, and the geographic distribution of branches. The ADKAR model (Awareness, Desire, Knowledge, Ability, Reinforcement) is commonly used. "Business readiness" is a formal gate criterion at most banks — operations, training, communications, and support must all be certified ready before go-live. Many banks now have dedicated Organizational Change Management (OCM) teams within the PMO.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Change Management Tracker for banking programs. Create a board called 'Change Management Plan' with groups: Stakeholder Analysis, Communications, Training, Adoption Tracking. In Stakeholder Analysis group, items represent stakeholder groups with columns: Stakeholder Group (text), Population Size (numbers), Impact Level (dropdown: High/Medium/Low), Current Readiness (status: Unaware/Aware/Understanding/Committed/Advocating), Desired Readiness (status: same options), Key Concerns (long text), Change Champion (people). In Communications group, items are communication activities: Message Theme (text), Target Audience (dropdown matching stakeholder groups), Channel (dropdown: Email/Town Hall/Intranet/Manager Cascade/Video/Branch Memo), Scheduled Date (date), Status (status: Drafting/Approved/Sent/Complete), Owner (people). In Training group: Training Module (text), Target Audience (dropdown), Delivery Method (dropdown: Instructor-Led/eLearning/Simulation/Job Aid), Scheduled Dates (date range), Completion Rate % (numbers), Assessment Pass Rate % (numbers), Status (status: Developing/Ready/In Progress/Complete). In Adoption Tracking: Metric Name (text), Target Value (numbers), Current Value (numbers), Measurement Method (text), Status (status: Below Target/On Track/Exceeding). Add automations: when associated project milestone reaches UAT, change Training Status to In Progress for relevant modules; when Completion Rate drops below 80% at scheduled end date, notify Change Champion. Create Dashboard with: readiness heat map by stakeholder group, communication calendar, training completion rates, adoption metrics vs. targets."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Change Pulse
**Agent Purpose:** Monitor organizational readiness, automate change communications, and predict adoption risks.

**Triggers:**
- When a project milestone triggers a change management phase
- Weekly readiness assessment scan
- When training completion rates fall below threshold
- When adoption metrics diverge from targets post-go-live
- When stakeholder feedback (via forms) indicates resistance

**Actions:**
- Generate stakeholder impact assessments based on project scope changes
- Draft change communications tailored to each stakeholder group
- Create training completion reports with gap analysis
- Predict adoption risk based on readiness scores, training completion, and historical patterns
- Generate post-implementation adoption dashboard comparing expected vs. actual benefits
- Recommend targeted interventions for low-readiness stakeholder groups

**Data Required:**
- Change Management Plan board
- Project milestone boards
- Training completion data
- Stakeholder feedback forms
- Post-go-live usage/adoption metrics

**Autonomy Level:** Human-in-the-Loop
Readiness monitoring, reporting, and draft communications are autonomous. Communication distribution, training schedule changes, and go-live readiness certification require OCM Lead approval.

**Example Interaction:**
> Three weeks before the new Digital Lending Platform go-live, Change Pulse runs a readiness assessment. It finds: branch managers (450 people, high impact) are at "Aware" readiness vs. target "Committed." Training completion for the branch manager module is only 34%. Support team readiness is on track. The agent generates an alert: "Go-live readiness risk: Branch Manager population significantly below readiness target. Root cause: only 34% training completion, likely due to Q4 branch production pressures. Recommend: (1) Deploy condensed 90-minute virtual training sessions during low-traffic branch hours, (2) Activate Branch Manager Change Champions for peer coaching, (3) Consider 2-week phased rollout starting with highest-readiness regions, (4) Escalate to Regional Directors for protected training time." The OCM Lead reviews and approves the phased rollout approach.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| EPMO | Enterprise Project Management Office — centralized PMO overseeing all divisional PMOs |
| RTB / CTB | Run-the-Bank / Change-the-Bank — budget categorization for operational vs. transformational spending |
| MRA / MRIA | Matter Requiring Attention / Matter Requiring Immediate Attention — regulatory findings |
| Stage-Gate | Governance checkpoints requiring deliverables and approvals before proceeding |
| RAG Status | Red/Amber/Green health indicator for project status |
| BRD | Business Requirements Document — formal specification of business needs |
| PIR | Post-Implementation Review — mandatory assessment after project completion |
| ARB | Architecture Review Board — governance body for technology decisions |
| CAB | Change Advisory Board — governance body for production deployments |
| Three Lines of Defense | Banking governance model: Business (1st), Risk/Compliance (2nd), Internal Audit (3rd) |
| FRTB | Fundamental Review of the Trading Book — Basel III.1 market risk regulation |
| SOC 2 | Service Organization Control report — vendor security/controls certification |
| T-shirt Sizing | Quick estimation method: Small, Medium, Large, XL for project effort |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CIO / CTO | Technology strategy, portfolio investment decisions | Decision-maker |
| EPMO Director | Portfolio governance, resource allocation, methodology standards | Decision-maker |
| Divisional PMO Lead | Business unit portfolio execution, demand prioritization | Decision-maker / Influencer |
| Senior Project Manager | Large program delivery, stakeholder management | Influencer |
| PMO Analyst / Coordinator | Status reporting, gate administration, resource tracking | User |
| Chief Risk Officer | Risk oversight on technology programs | Decision-maker (governance) |
| Chief Compliance Officer | Regulatory program oversight and sign-off | Decision-maker (governance) |
| Business Sponsor | Project justification, benefit realization, funding | Decision-maker |
| Enterprise Architect | Technology standards, architecture review gates | Influencer |
| Vendor/SI Engagement Manager | Third-party delivery oversight | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT / Technology | PMO manages IT's project portfolio — natural extension | Core platform user; IT service management, DevOps tracking |
| Finance | PMO needs budget tracking, Finance needs project cost data | CapEx/OpEx tracking, financial forecasting boards |
| Risk & Compliance | Regulatory programs are PMO's biggest portfolio segment | Risk register management, compliance tracking |
| HR | Resource capacity requires HR headcount data; OCM is HR-adjacent | Workforce planning, onboarding, training management |
| Operations | Many PMO programs impact Operations processes | Process improvement tracking, operational readiness |
| Procurement | Vendor management requires procurement coordination | Vendor lifecycle management, contract tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Microsoft Project / Project for the Web | Traditional PM tool, strong in scheduling | Limited collaboration, no AI, poor portfolio visibility; monday.com offers real-time collaboration + AI |
| Planview / Clarity | Enterprise PPM for large portfolios | Expensive, complex, poor UX; monday.com delivers 80% of capability at 30% of cost with better adoption |
| ServiceNow SPM | IT-centric project/portfolio management | Heavy ITSM bias, requires dedicated admin team; monday.com is more flexible and business-user friendly |
| Smartsheet | Spreadsheet-like PM collaboration | Limited governance capabilities, weak portfolio views; monday.com has superior dashboards and automations |
| Jira / Atlassian | Agile development management | Developer-focused, poor for business stakeholder reporting; monday.com bridges business and technology |
| Excel / SharePoint | The "incumbent" for reporting and tracking | Zero automation, no real-time visibility, audit nightmare; monday.com replaces with structured, auditable workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We need an enterprise PPM tool like Planview, not a work management platform" | monday.com's portfolio capabilities (connected boards, dashboards, workload management, automations) deliver enterprise PPM functionality with 10x better adoption. Planview implementations take 12-18 months and cost $500K+; monday.com is live in weeks. The best PPM tool is the one people actually use. |
| "Our regulatory environment requires tools with specific compliance certifications" | monday.com is SOC 2 Type II certified, GDPR compliant, HIPAA capable, and supports data residency requirements. Activity logs provide full audit trails. Many regulated financial institutions already use monday.com. |
| "We've standardized on Microsoft Project / Project Online" | MS Project excels at scheduling but fails at collaboration, real-time visibility, and AI-powered insights. Most banks using MS Project supplement with Excel and SharePoint anyway — monday.com replaces all three. Integration with Microsoft ecosystem (Teams, Outlook, Azure AD) ensures coexistence. |
| "Our PMs are trained on traditional methodologies and won't adopt a new tool" | monday.com supports waterfall, agile, and hybrid methodologies. The intuitive UX means PMs become productive in days, not months. The time they save on status collection and reporting converts them into advocates. Offer a pilot with one program to prove adoption. |
| "We can't put project data in the cloud — security concerns" | monday.com offers enterprise-grade security: encryption at rest and in transit, SSO/SAML, IP restrictions, audit logs, and data residency options. Many Tier 1 banks already trust monday.com with sensitive project data. We can work with your InfoSec team on a security review. |

## Proof Points
*(To be populated with customer references)*
- [Large bank using monday.com for portfolio management]
- [Financial institution that consolidated from 5+ PM tools to monday.com]
- [Regulatory program managed on monday.com with successful audit outcome]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
