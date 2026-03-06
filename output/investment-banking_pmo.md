# Investment Banking × PMO Playbook

## Overview

The Project Management Office (PMO) function within investment banking operates in a uniquely challenging environment where "projects" are not traditional IT implementations or corporate initiatives — they are live financial transactions worth hundreds of millions to tens of billions of dollars, each with razor-thin margin for error and immovable market-driven deadlines. The PMO in an investment bank typically spans two distinct domains: (1) transaction execution project management — coordinating the complex workstreams within live deals (M&A processes, IPOs, debt offerings, restructurings), and (2) strategic/operational PMO — managing internal transformation programs, technology migrations, regulatory compliance initiatives, and organizational change across the bank.

On the transaction side, the PMO function is often embedded rather than centralized. Deal teams act as their own project managers, with VPs and associates playing de facto PM roles without formal PM training or tooling. This creates enormous inconsistency: one M&A team might run a disciplined, milestone-driven process while another operates through email chains and tribal knowledge. The result is preventable delays, miscommunication between workstreams, and senior bankers spending time on coordination rather than client-facing activities. Some larger banks have begun creating dedicated "deal operations" or "execution management" teams — essentially PMO functions purpose-built for transaction workflows.

On the strategic side, investment banks face a staggering volume of concurrent change initiatives: regulatory programs (Basel IV implementation, ESG reporting mandates, AML/KYC enhancements), technology transformations (cloud migration, trading platform upgrades, AI adoption), organizational restructuring (post-merger integration, geographic expansion, business line rationalization), and operational efficiency programs. The strategic PMO must manage a portfolio of 50-200+ concurrent projects across divisions, each competing for budget, executive sponsorship, and scarce technical resources. Many banks still rely on a patchwork of Microsoft Project files, SharePoint sites, and Excel trackers — tools that provide no portfolio-level visibility and create massive overhead in status reporting.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | PMO teams of 5-15 people must coordinate 50-200+ concurrent projects and deals across the bank — current tools make portfolio visibility nearly impossible |
| 2 | Consolidate Tech Stack with AI | High | Banks run fragmented PM stacks: MS Project, Smartsheet, Jira, SharePoint, Excel — no unified portfolio view, massive reporting overhead |
| 3 | Replace or Radically Augment Headcount | Medium-High | Status reporting, resource tracking, and risk escalation consume 40-50% of PMO staff time — all highly automatable |

## Prioritized Use Cases

---

### Use Case 1: Enterprise Program Portfolio Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The strategic PMO in an investment bank manages a portfolio that might include 150+ active programs: a $200M core banking platform migration, a regulatory compliance program with 30 sub-workstreams, a post-merger integration across 12 countries, and dozens of smaller operational improvement initiatives. Leadership (COO, CTO, division heads) needs portfolio-level visibility: Which programs are on track? Which are at risk? Where are resource conflicts? What's the burn rate against budget? Today, this visibility requires PMO analysts to manually collect status updates from dozens of program managers, aggregate them in Excel, and produce a monthly portfolio review deck — a process that takes 2-3 weeks and is stale the moment it's printed.

#### The Solution
monday.com Work Management as the enterprise portfolio management platform. Three-tier board structure: Portfolio Overview (all programs with health status), Program Boards (individual program workstreams and milestones), and Project Boards (detailed task-level tracking within each program). Custom columns for program health scoring (scope, schedule, budget, risk — each Red/Amber/Green), budget tracking (approved vs. spent vs. forecast), resource allocation, executive sponsor, and strategic alignment tagging. Portfolio Dashboard providing real-time aggregate views: programs by health status, budget burn rate, resource utilization across the portfolio, upcoming milestones, and escalations requiring executive decision.

#### The Outcome
- Portfolio visibility goes from "monthly stale report" to "real-time dashboard" — saving 3 weeks of reporting cycle time
- PMO analysts reclaim 60% of time spent on manual status aggregation
- Executive decisions on program prioritization are data-driven, not based on who lobbies hardest
- Resource conflicts identified weeks earlier through portfolio-level visibility
- Regulatory programs have auditable milestone tracking for regulator scrutiny

#### Discovery Questions
1. "How many active strategic programs does your PMO currently track across the bank, and what tool or tools hold that data today?"
2. "How long does it take to produce your monthly portfolio review for the COO or CTO — and how confident is leadership that the data reflects reality?"
3. "When two programs compete for the same engineering team or the same budget pool, how is that conflict surfaced and resolved?"
4. "Have regulators ever questioned your ability to demonstrate program milestone adherence — for example, on a Basel IV or AML remediation program?"
5. "What percentage of your PMO team's time is spent collecting status updates versus actually managing and improving program delivery?"

#### Industry Context
"Program" in banking PMO typically means a large-scale, multi-year initiative (technology migration, regulatory compliance, organizational transformation). "RAG status" (Red/Amber/Green) is the universal health indicator. "Regulatory programs" carry special urgency — failure to deliver on time can result in consent orders, fines, or business restrictions from regulators (OCC, Fed, FCA, ECB). "Post-merger integration" (PMI) programs in banking are notoriously complex, involving IT system consolidation, organizational alignment, branch rationalization, and regulatory approvals across jurisdictions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Investment Banking Program Portfolio board. Columns: Program Name (text), Program ID (text), Executive Sponsor (people), Program Manager (people), Division (dropdown: Investment Banking Division, Global Markets, Wealth Management, Technology, Operations, Risk & Compliance, Corporate Functions), Program Type (dropdown: Regulatory Compliance, Technology Transformation, Post-Merger Integration, Operational Efficiency, New Business Initiative, Organizational Change, Infrastructure), Strategic Priority (status: Tier 1 Critical, Tier 2 High, Tier 3 Standard), Overall Health (status: Green — On Track, Amber — At Risk, Red — Off Track, Blue — Complete, Grey — On Hold), Scope Health (status: Green, Amber, Red), Schedule Health (status: Green, Amber, Red), Budget Health (status: Green, Amber, Red), Risk Level (status: Low, Medium, High, Critical), Start Date (date), Target End Date (date), Approved Budget $M (numbers), Spent to Date $M (numbers), Forecast at Completion $M (numbers), Budget Variance % (formula), FTE Allocated (numbers), Key Milestones Next 30 Days (long text), Top Risks & Issues (long text), Last Status Update (date), Regulatory Deadline (date). Create groups: Active — Tier 1, Active — Tier 2, Active — Tier 3, On Hold, Completed 2026. Add Dashboard with: portfolio health distribution (pie chart — Green/Amber/Red), programs by division (chart), total budget allocation vs. spend (chart), programs with regulatory deadlines in next 90 days (filtered table), programs at risk or off track (filtered table with escalation details), FTE allocation by division (chart), budget variance top 10 (table). Add automations: when Overall Health changes to 'Red', immediately notify Executive Sponsor and PMO Head: 'ALERT: {Program Name} is now RED — review required.' When Last Status Update is more than 14 days ago, notify Program Manager: 'Status update overdue for {Program Name} — please update.' When Budget Variance % exceeds 15%, change Budget Health to Red."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio Health Monitor Agent
**Agent Purpose:** Continuously monitor program portfolio health, auto-detect emerging risks, and generate executive-ready portfolio intelligence without manual aggregation.

**Triggers:**
- Daily scan at 7 AM for status changes and overdue updates
- When any program's health status changes to Amber or Red
- When budget variance exceeds threshold (10% Amber, 20% Red)
- Weekly portfolio digest generation (Friday 4 PM)
- Monthly portfolio review preparation (5 business days before review)

**Actions:**
- Auto-detect programs trending toward risk: schedule slippage patterns, accelerating budget burn, stale status updates
- Generate weekly portfolio digest: programs changed status, new risks surfaced, milestones achieved, upcoming deadlines, resource conflicts
- Prepare monthly portfolio review deck content: executive summary, health dashboard, budget rollup, resource utilization, top 10 risks, decision items
- Cross-reference resource allocation across programs to identify conflicts (same team assigned to overlapping critical milestones)
- Track regulatory program deadlines and generate 90/60/30-day countdown alerts with escalating urgency
- Identify "zombie programs" — initiatives that haven't had meaningful progress in 30+ days but are still consuming budget

**Data Required:**
- Portfolio board and all connected program boards
- Budget and spend data from finance systems
- Resource allocation boards
- Regulatory deadline database
- Historical program delivery data for trend analysis

**Autonomy Level:** Fully Autonomous (monitoring and reporting), Escalation-Based (action recommendations)
Portfolio monitoring, alerts, and report generation are fully automated. Resource reallocation recommendations and program deprioritization suggestions require executive approval.

**Example Interaction:**
> The Portfolio Health Monitor runs its Friday afternoon scan and generates the weekly digest: "Portfolio Summary: 147 active programs. 112 Green (76%), 24 Amber (16%), 8 Red (5%), 3 On Hold (2%). Week-over-week: 3 programs moved from Green to Amber, 1 moved from Amber to Red (Cloud Migration Phase 3 — schedule delay due to vendor staffing issues). Budget: $2.34B total approved, $1.02B spent YTD (43.6% — tracking slightly ahead of plan). Key alert: AML Remediation Program and Core Banking Migration both require the Data Engineering team for critical milestones in weeks 12-14 — resource conflict detected. Recommendation: escalate to CTO for prioritization."
>
> The agent also flags: "Zombie program detected: 'Branch Digital Signage Refresh' — no status update in 47 days, last milestone completed in November, still consuming $120K/month in contractor costs. Recommend review for pause or closure."

---

### Use Case 2: Deal Execution Workstream Orchestration

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Every major investment banking transaction is a complex project with 15-30 parallel workstreams, strict dependencies, and immovable deadlines driven by market windows, regulatory filings, and client needs. An IPO process, for example, involves legal drafting (S-1/prospectus), SEC comments and responses, due diligence workstreams (financial, legal, commercial, IT), management roadshow logistics, syndicate formation, book-building, pricing, and allocation — all coordinated across the bank's coverage team, ECM product group, legal counsel (internal and external), the client's management team, and auditors. Today, the VP or associate on the deal manages this through personal spreadsheets and email chains. There is no institutional process — each deal team reinvents the wheel.

#### The Solution
monday.com Work Management with deal execution templates. Pre-built templates for each transaction type (M&A sell-side, M&A buy-side, IPO, follow-on, investment-grade debt offering, high-yield debt offering, leveraged buyout financing, restructuring). Each template contains the standard workstreams, milestones, dependencies, and role assignments for that deal type. When a new deal kicks off, the team instantiates the template, customizes it for the specific transaction, and has a fully structured project plan in minutes. Timeline/Gantt view shows critical path. Automated dependency tracking flags downstream impacts when workstreams slip. Status dashboards give senior bankers and deal committee members instant visibility.

#### The Outcome
- Deal setup time reduced from 2-3 days to 30 minutes with pre-built templates
- 20-30% improvement in deal execution timeline through proactive dependency management
- Institutional deal execution knowledge preserved in templates rather than in individual bankers' heads
- Consistent execution quality across all deal teams regardless of team composition
- Senior bankers and deal committee get real-time visibility without status meetings

#### Discovery Questions
1. "When a new M&A mandate kicks off, how does the deal team set up their project tracking — is there a standard template or does each team create their own?"
2. "How often do you see deal workstreams slip because a dependency wasn't tracked — for example, the CIM wasn't ready because management interviews ran late?"
3. "If a deal committee member asks 'Where are we on the XYZ deal?', how long does it take to get an accurate answer?"
4. "Have you quantified how many hours per deal are spent on coordination and status reporting versus actual execution work?"
5. "When a deal type you've done 50 times before kicks off, does the team still build the project plan from scratch?"

#### Industry Context
Each deal type has standard workstreams that experienced bankers know but are rarely documented systematically. "S-1" is the SEC registration statement for an IPO. "Red herring" is the preliminary prospectus. "Roadshow" is the series of investor presentations before pricing. "Book-building" is the process of collecting investor orders. "Syndicate" is the group of banks co-managing a securities offering. "Green shoe" (or overallotment option) allows the syndicate to sell additional shares. Understanding these terms lets the SE speak credibly about building execution templates.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an IPO Deal Execution template board. Create groups for each workstream: 1) Legal & Registration (tasks: Engage external counsel, Draft S-1 registration statement, SEC initial filing, Respond to SEC comments Round 1, Respond to SEC comments Round 2, File amendment, SEC effectiveness), 2) Due Diligence (tasks: Financial DD kickoff, Business DD sessions, Legal DD — material contracts review, IT/cyber DD, Environmental DD, Management reference checks, DD report compilation), 3) Financial Analysis (tasks: Build valuation model — DCF/comps/precedents, Prepare valuation range, Draft pricing committee memo, Sensitivity analysis, Peer benchmarking), 4) Marketing Materials (tasks: Draft CIM/investor presentation, Management team bios and Q&A prep, Roadshow presentation draft, Roadshow video production, Print preliminary prospectus — red herring), 5) Syndicate Formation (tasks: Select co-managers, Negotiate economics/fees, Prepare syndicate agreement, Distribute preliminary prospectus to syndicate), 6) Investor Roadshow (tasks: Schedule roadshow — 2 week calendar, Book management travel, Conduct roadshow meetings, Track investor feedback daily, Compile demand book), 7) Pricing & Allocation (tasks: Build order book, Pricing committee meeting, Set final price, Allocate shares, Trade date — T+0, Settlement — T+2), 8) Post-IPO (tasks: Stabilization period monitoring, Lock-up period tracking, Analyst initiation of coverage, 25-day quiet period management). Columns for all: Task Name (text), Owner (people), Status (status: Not Started, In Progress, Under Review, Blocked, Complete), Due Date (date), Dependencies (dependency), Workstream Lead (people), Notes (long text), Regulatory Deadline (checkbox), External Party (dropdown: None, External Counsel, Auditor, SEC, Printer, Investor Relations). Add Timeline view with dependencies. Add Dashboard: overall completion %, tasks by status, overdue tasks, upcoming milestones next 2 weeks, workstream health summary. Add automations: when Status changes to 'Blocked', notify Workstream Lead and Deal Captain. When a task with Regulatory Deadline checked is 3 days from Due Date and not Complete, send urgent alert."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Deal Orchestration Agent
**Agent Purpose:** Monitor deal execution workstreams, manage dependencies, predict delays, and keep all deal participants synchronized on the critical path.

**Triggers:**
- Deal template instantiated (new deal kickoff)
- Any task Status changes
- Daily morning scan (7 AM) for overdue and at-risk items
- When a task with dependencies is delayed (cascade analysis)
- Deal Captain requests status summary

**Actions:**
- On deal kickoff: auto-assign standard workstream leads based on deal team composition, set initial milestone dates based on target pricing date working backward
- When a task is delayed, auto-calculate cascade impact on all dependent tasks and generate a revised timeline with highlighted changes
- Generate daily deal status brief for Deal Captain: tasks completed yesterday, tasks due today, blockers, and critical path assessment
- Monitor external party deliverables (counsel, auditors, SEC) and flag when responses are overdue
- 48 hours before each major milestone (SEC filing, roadshow start, pricing), verify all prerequisite tasks are complete and generate readiness checklist
- After deal closes, auto-generate lessons-learned template pre-populated with timeline analysis (planned vs. actual for each workstream)

**Data Required:**
- Deal execution board with all workstream tasks
- Deal team roster and role assignments
- Historical deal timelines for benchmark comparison
- External party contact information and SLA expectations

**Autonomy Level:** Escalation-Based
Monitoring, alerting, and cascade analysis are autonomous. Timeline changes and task reassignments are recommended to the Deal Captain for approval. External communications are never automated.

**Example Interaction:**
> Three weeks into the TechVenture Inc. IPO process, the Deal Orchestration Agent detects that "Respond to SEC Comments Round 1" was due yesterday but remains "In Progress." It traces the dependency chain: SEC comment resolution must complete before filing the amendment, which must happen before the red herring can be printed, which must happen 15 days before the roadshow begins. The roadshow is currently scheduled to start in 22 days.
>
> The agent alerts the Deal Captain: "SEC Comment Response (Round 1) is 1 day overdue. Cascade impact: if not resolved within 5 business days, the roadshow start date of March 15 is at risk. Currently 2 days of buffer remain in the critical path. External counsel (Sullivan & Cromwell) was last contacted Tuesday — recommend follow-up today. The printing deadline for the red herring is March 3 — this is now the binding constraint."
>
> The agent updates the timeline view with the revised critical path highlighted in red and creates a task for the Deal Captain: "Decision required: if SEC response takes >5 days, choose between (a) compress roadshow from 10 days to 8 days, or (b) push pricing date by 2 days."

---

### Use Case 3: Resource Capacity Planning & Allocation

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment bank PMOs face a unique resource planning challenge: they must allocate scarce specialist resources (quantitative analysts, technology architects, compliance officers, project managers) across dozens of concurrent programs, each with fluctuating demands and competing priorities. Unlike a product company where teams are relatively stable, banking resource allocation shifts constantly as deals close, new programs launch, and regulatory deadlines create sudden spikes in demand. PMO leaders spend enormous time in "resource negotiations" — manually tracking who's available, who's overcommitted, and which program gets priority for the next available architect. The lack of real-time visibility into resource utilization means decisions are based on politics rather than data.

#### The Solution
monday.com Work Management as a resource planning and allocation system. Resource board showing all PMO-managed resources with current assignments, utilization rates, skills, and availability forecasts. Connected to program boards so that when a program's timeline changes, resource impact is immediately visible. Demand planning view showing projected resource needs by skill type over the next 6-12 months. Capacity vs. demand dashboard highlighting gaps and surpluses. Request queue for program managers to submit resource needs with skill requirements and priority justification.

#### The Outcome
- Real-time resource utilization visibility replaces manual tracking (save 15+ PMO hours/week)
- Resource conflicts identified 4-6 weeks earlier through demand forecasting
- 30% improvement in resource utilization through better matching and planning
- Data-driven resource allocation decisions reduce political friction
- Contractor/vendor hiring decisions informed by capacity gap analysis rather than reactive scrambling

#### Discovery Questions
1. "How many specialized resources does your PMO allocate across programs — and how do you currently track who's working on what?"
2. "When a high-priority regulatory program needs a data architect, how long does it take to find one who's available — and what happens to the program they're pulled from?"
3. "Do you have forward visibility into resource demand — can you see, 3 months from now, where the bottlenecks will be?"
4. "How much of your contractor/vendor spending is reactive — brought in because you didn't anticipate a resource gap early enough?"
5. "When two Tier 1 programs both need the same scarce resource, what's the escalation path — and does the right program always win?"

#### Industry Context
"FTE" (Full-Time Equivalent) is the standard resource unit. "Blended rate" is the cost per FTE including salary, benefits, and overhead. "Contractor augmentation" or "body shop" refers to bringing in external consultants to fill gaps — extremely common in banking PMO. "Run the bank" (RTB) vs. "change the bank" (CTB) distinguishes ongoing operational work from project/transformation work — both compete for the same resources. Banks often have a "strategic workforce planning" function that should align with PMO resource planning but rarely does.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a PMO Resource Planning board. Columns: Resource Name (people), Role (dropdown: Project Manager, Program Manager, Business Analyst, Technical Architect, Data Engineer, Compliance Specialist, Change Manager, QA/Testing Lead, Scrum Master, Vendor Manager), Skill Tags (tags: Regulatory, Cloud Migration, Data/Analytics, Risk Systems, Trading Platforms, Client Onboarding, AML/KYC, Core Banking, Payments, Cybersecurity, Agile, Waterfall), Employment Type (dropdown: FTE, Contractor, Vendor Consultant), Cost Rate $/Day (numbers), Current Programs (connect to Portfolio board), Current Utilization % (numbers), Availability Status (status: Available, Partially Available, Fully Allocated, Overallocated, On Leave, Departing), Available From (date), Capacity Next 4 Weeks — Hours (numbers), Location (dropdown: New York, London, Hong Kong, Singapore, Mumbai, Remote), Notes (long text). Create a second board: Resource Requests with columns: Requesting Program (connect to Portfolio board), Program Manager (people), Role Needed (dropdown — same as above), Skills Required (tags — same as above), Hours/Week (numbers), Duration (text), Start Date Needed (date), Priority (status: Critical — Regulatory, High, Medium, Low), Request Status (status: Submitted, Under Review, Approved — Searching, Filled, Waitlisted, Declined), Assigned Resource (people), Decision Notes (long text), Request Date (date). Add Dashboard on Resource Planning board: utilization distribution (chart — % of resources in each utilization band), resources by role (chart), resource demand vs. capacity next 12 weeks (stacked bar chart), overallocated resources (filtered table), open requests by priority (table), contractor vs. FTE mix (pie chart). Add automations: when Utilization % exceeds 110%, change Availability to 'Overallocated' and notify PMO Lead. When new Resource Request created with Priority 'Critical — Regulatory', immediately notify PMO Lead and move to top of queue."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Capacity Planning Agent
**Agent Purpose:** Forecast resource demand, optimize allocation across the program portfolio, and proactively identify capacity gaps before they become crises.

**Triggers:**
- New resource request submitted
- Program timeline changes that affect resource needs
- Weekly capacity forecast update (Monday morning)
- When any resource utilization exceeds 100% for 2+ consecutive weeks
- Monthly strategic capacity review preparation

**Actions:**
- When a resource request arrives, instantly match against available resources by role, skills, location, and availability window; present top 3 candidates with utilization impact analysis
- Generate weekly capacity forecast: demand vs. supply by role for next 12 weeks, highlighting gaps that require contractor hiring decisions (with 4-week lead time factored in)
- Detect "resource collision" scenarios: two programs entering critical phases simultaneously, both requiring the same specialist pool
- Produce monthly capacity report: utilization trends, contractor spend vs. budget, skills gaps, hiring recommendations
- When a program completes or pauses, automatically update affected resource availability and check if any waitlisted requests can be fulfilled
- Forecast quarterly contractor budget based on projected FTE gaps and blended rates

**Data Required:**
- Resource Planning board and Resource Requests board
- Program Portfolio board (for timeline and milestone data)
- Budget data for contractor spending caps
- Historical resource utilization patterns
- Skills database and development plans

**Autonomy Level:** Human-in-the-Loop
Matching recommendations, capacity forecasts, and gap analysis are autonomous. All resource assignments and contractor hiring decisions require PMO Lead approval. Budget recommendations are advisory.

**Example Interaction:**
> On Monday morning, the Capacity Planning Agent generates the weekly forecast: "Capacity Alert — Weeks 8-10 Critical. Three programs entering peak phase simultaneously: AML Remediation (needs 4 compliance specialists), Core Banking Migration (needs 3 technical architects), and Regulatory Reporting Enhancement (needs 2 data engineers). Current supply: 3 compliance specialists available (gap: 1), 2 technical architects available (gap: 1), 1 data engineer available (gap: 1). Recommended action: initiate contractor search for 1 compliance specialist, 1 technical architect, and 1 data engineer. If contractors require 3-week onboarding, hiring decision needed by end of this week. Estimated monthly cost: $85K for all three contractors."
>
> The agent also surfaces: "Optimization opportunity: Maria Santos (Business Analyst) is allocated to the Branch Optimization program at 60% but the program is in 'steady state' — no critical milestones for 6 weeks. She has the regulatory skills needed by AML Remediation. Recommend partial reallocation: 40% to AML Remediation for weeks 8-14."

---

### Use Case 4: Regulatory Program Compliance & Milestone Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banks operate under intense regulatory scrutiny. At any given time, a large bank might be executing 20-40 regulatory programs: Basel IV capital requirements implementation, FRTB (Fundamental Review of the Trading Book), AML/KYC remediation, sanctions compliance upgrades, ESG reporting frameworks, operational resilience (DORA in the EU), and consent order remediation from past enforcement actions. These programs have immovable deadlines set by regulators (OCC, Federal Reserve, FCA, ECB, MAS) — missing them can result in fines, business restrictions, or forced management changes. Yet regulatory programs are tracked with the same ad hoc tools as any other project, and demonstrating to examiners that milestones were met on time requires manual evidence gathering.

#### The Solution
monday.com Work Management as a regulatory program management system with built-in audit trail capabilities. Each regulatory program has a structured board with mandated milestones, evidence requirements, and regulatory reporting dates. Compliance-grade tracking with timestamped status changes, approval workflows, and document attachments for evidence. Dashboard providing "regulatory program readiness" across all active regulatory initiatives. Automated alerts at 90/60/30-day intervals before regulatory deadlines. Connection to the enterprise portfolio for resource prioritization when regulatory programs are at risk.

#### The Outcome
- Regulator-ready milestone evidence available in minutes, not weeks of manual compilation
- Zero missed regulatory deadlines through automated countdown alerting
- Audit trail provides defensible proof of governance and oversight
- Regulatory program status visible to Board Risk Committee without manual reporting
- Resource prioritization automatically favors at-risk regulatory programs over discretionary initiatives

#### Discovery Questions
1. "How many active regulatory programs are you managing right now, and what tools do you use to track milestone adherence?"
2. "When your regulator (OCC, Fed, FCA) examines a program, how long does it take to produce evidence that milestones were met on time?"
3. "Have you ever had a regulatory deadline slip — and what was the consequence?"
4. "How does your PMO prioritize regulatory programs against other strategic initiatives when they compete for resources?"
5. "What does your Board Risk Committee or regulatory affairs function need from the PMO in terms of reporting — and how much effort goes into producing it?"

#### Industry Context
"Consent order" (or "enforcement action") is when a regulator formally requires a bank to remediate specific deficiencies within a timeframe — failure is severe. "MRA" (Matter Requiring Attention) and "MRIA" (Matter Requiring Immediate Attention) are specific regulatory findings that must be addressed. "Three lines of defense" is the banking governance model: 1st line (business), 2nd line (risk/compliance), 3rd line (internal audit). Regulatory programs typically require evidence that not just the deliverable was completed, but that proper governance (approvals, reviews, sign-offs) was followed throughout.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Regulatory Program Tracker board. Columns: Program Name (text), Regulatory Body (dropdown: OCC, Federal Reserve, FDIC, SEC, FINRA, FCA, ECB, MAS, APRA, OSFI, Multiple), Regulation/Mandate (text), Program Sponsor (people), Program Manager (people), Program Type (dropdown: New Regulation Implementation, Consent Order Remediation, MRA/MRIA Remediation, Self-Identified Enhancement, Industry Standard Adoption), Regulatory Deadline (date), Internal Target Date (date), Buffer Days (formula: Regulatory Deadline minus Internal Target Date), Overall Status (status: Green — On Track, Amber — At Risk, Red — Off Track, Complete — Pending Validation, Complete — Regulator Accepted), Milestones Total (numbers), Milestones Complete (numbers), Completion % (formula), Evidence Status (status: All Evidence Collected, Gaps Identified, Collection In Progress, Not Started), Last Examiner Interaction (date), Next Examiner Touchpoint (date), Budget $M (numbers), Spend $M (numbers), Key Risks (long text), Remediation Actions if Red (long text). Create groups: Active — Consent Orders, Active — New Regulations, Active — MRA/MRIA, Active — Self-Identified, Completed 2026. Create a connected board: Regulatory Milestones with columns: Milestone Name (text), Parent Program (connect), Owner (people), Due Date (date), Completed Date (date), Status (status), Evidence Required (long text), Evidence Attached (file), Approved By (people), Approval Date (date), Examiner Reviewed (checkbox), Notes (long text). Add Dashboard: regulatory programs by status (chart), programs by regulatory body (chart), milestones due next 30/60/90 days (table), evidence collection gaps (filtered table), budget tracking (chart). Add automations: when Regulatory Deadline is 90 days away, notify Program Manager and Sponsor: '90-day alert: {Program Name} regulatory deadline approaching.' Repeat at 60 and 30 days with escalating urgency. When a Milestone Status changes to 'Complete', check if Evidence Attached is empty — if so, change status to 'Complete — Pending Evidence' and notify Owner."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Compliance Sentinel
**Agent Purpose:** Continuously monitor regulatory program health, ensure evidence integrity, and generate regulator-ready status reports with zero manual effort.

**Triggers:**
- Daily scan at 6 AM for regulatory deadlines within 90 days
- When any regulatory program status changes to Amber or Red
- When a milestone is marked complete (evidence validation check)
- Monthly regulatory report generation (3rd business day)
- When a new regulatory mandate is announced (manual input or news monitoring)

**Actions:**
- Generate automated 90/60/30/14/7-day countdown alerts with escalating recipients (PM → Sponsor → COO → Board Risk Committee)
- Validate evidence completeness: when milestones are marked complete, verify that required evidence documents are attached and approvals are recorded
- Produce monthly regulatory status report formatted for Board Risk Committee: program summaries, milestone adherence rates, risk assessments, examiner feedback
- Cross-reference regulatory program resource needs with portfolio capacity data and flag programs at risk due to resource constraints
- Track examiner interaction cadence and alert when a program hasn't had examiner contact in the expected timeframe
- Generate "regulatory readiness score" for each program based on milestone completion, evidence quality, and buffer days remaining

**Data Required:**
- Regulatory Program Tracker and Regulatory Milestones boards
- Portfolio resource data
- Examiner interaction logs
- Evidence document repository
- Regulatory calendar (published regulatory deadlines)

**Autonomy Level:** Fully Autonomous (monitoring, alerting, reporting), Escalation-Based (remediation actions)
All monitoring and report generation is autonomous. Remediation actions for at-risk programs are recommended to the Program Sponsor with specific options and impact analysis.

**Example Interaction:**
> The Regulatory Compliance Sentinel's 6 AM scan identifies a critical issue: the AML Transaction Monitoring Enhancement program (consent order remediation, OCC) has a regulatory deadline in 47 days. Three of its 12 milestones are overdue, and evidence has not been attached for 2 completed milestones. The agent escalates immediately: "🚨 CONSENT ORDER RISK: AML Transaction Monitoring — 47 days to OCC deadline. 3 milestones overdue (Model Validation Testing, Alert Tuning UAT, Production Deployment). 2 completed milestones missing evidence documentation. Regulatory readiness score: 42/100 (Critical). At current velocity, projected completion is 21 days PAST the regulatory deadline. Required acceleration: all 3 overdue milestones must complete within 14 days. Resource need: 2 additional QA testers and 1 model validation specialist for the next 4 weeks. Recommend emergency steering committee meeting within 48 hours."
>
> The agent simultaneously updates the Portfolio board to flag the resource need and checks if any lower-priority programs have QA resources that could be temporarily reassigned.

---

### Use Case 5: Change Management & Stakeholder Communication

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Large programs in investment banks — technology migrations, organizational restructurings, new system rollouts — require extensive change management. Thousands of users across multiple geographies must be trained, communications must be tailored to different audiences (front office, middle office, back office, technology, compliance), and adoption must be tracked. Yet change management is often the most under-resourced and poorly tracked aspect of bank programs. PMOs typically manage communications through email distribution lists with no tracking of readership or effectiveness, training through scattered calendar invites and Excel attendance sheets, and stakeholder engagement through ad hoc meetings with no systematic tracking of sentiment or resistance.

#### The Solution
monday.com Work Management for structured change management execution. Communication plan board with audience segmentation, messaging drafts, approval workflows, distribution schedules, and effectiveness tracking. Training management board tracking sessions, attendance, completion rates, and assessment scores. Stakeholder map board showing key stakeholders, their influence level, current sentiment, engagement history, and required actions. Adoption metrics dashboard tracking go-live readiness by user group, training completion, communication receipt, and post-deployment support tickets.

#### The Outcome
- Structured change management increases program adoption rates from 60% to 85%+
- Communication effectiveness tracked by audience segment — no more "spray and pray"
- Training completion gaps identified by geography and role weeks before go-live
- Stakeholder resistance detected early through systematic sentiment tracking
- Post-implementation support costs reduced 40% through better pre-launch preparation

#### Discovery Questions
1. "For your last major technology rollout, how did you track which users were trained and ready versus which ones weren't?"
2. "How do you manage stakeholder sentiment across a large program — do you have a systematic way to track who's supportive, neutral, or resistant?"
3. "When you send change communications to 5,000 users, do you know who actually read them?"
4. "What's your typical adoption rate on new system launches — and what percentage of post-launch support tickets are things that should have been caught in training?"
5. "Do your change management activities feed into a central view, or are communications, training, and stakeholder management tracked separately?"

#### Industry Context
"Change management" in banking often follows frameworks like Prosci ADKAR or Kotter's 8 Steps. "Front office" (revenue-generating roles like bankers and traders) is the most resistant to change and the most important to get right. "UAT" (User Acceptance Testing) is when business users test the new system before go-live. "Hypercare" is the intensive support period immediately after go-live (typically 2-4 weeks). Banks often have "change champions" or "floor walkers" — volunteers in each business unit who provide peer support during transitions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Change Management Hub with three connected boards. Board 1 — Communications Plan: Columns: Communication Name (text), Program (connect to Portfolio board), Target Audience (dropdown: Front Office — IB, Front Office — Markets, Middle Office, Back Office, Technology, Compliance, All Staff), Channel (dropdown: Email, Town Hall, Intranet, Manager Cascade, Training Portal, Video, Slack/Teams), Message Status (status: Drafting, In Review, Approved, Sent, Follow-Up Needed), Send Date (date), Audience Size (numbers), Open/Read Rate % (numbers), Owner (people), Approval By (people), Content Link (link). Board 2 — Training Tracker: Columns: Session Name (text), Program (connect), Format (dropdown: Instructor-Led, Virtual, eLearning, Hands-On Lab, Video), Target Role (dropdown), Region (dropdown: Americas, EMEA, APAC), Total Target Attendees (numbers), Completed (numbers), Completion Rate % (formula), Session Date (date), Trainer (people), Assessment Pass Rate % (numbers), Status (status: Scheduled, In Progress, Completed, Cancelled). Board 3 — Stakeholder Map: Columns: Stakeholder Name (text), Title (text), Division (dropdown), Influence Level (status: Executive Sponsor, Key Decision Maker, Influencer, Standard User), Current Sentiment (status: Champion, Supportive, Neutral, Skeptical, Resistant), Engagement Actions (long text), Last Engagement (date), Next Engagement (date), Owner (people), Risk Notes (long text). Add Dashboard across all three boards: communication completion by audience (chart), training completion by region (chart), stakeholder sentiment distribution (chart), readiness score by business unit, overdue communications and training sessions (table). Add automation: when Training Completion Rate % drops below 70% with Session Date in the past, notify Change Manager: 'Training gap: {Session Name} — only {Completion Rate %}% complete. Schedule catch-up sessions.'"

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Change Readiness Agent
**Agent Purpose:** Monitor organizational readiness for program go-lives, detect adoption risks early, and coordinate communication and training activities to maximize successful change outcomes.

**Triggers:**
- Program go-live date minus 60 days (readiness assessment initiation)
- Training completion rate drops below target threshold
- Stakeholder sentiment changes to "Skeptical" or "Resistant"
- Weekly change management digest (Monday morning)
- Post-go-live: daily for first 2 weeks (hypercare monitoring)

**Actions:**
- Generate go-live readiness scorecard by business unit: training completion, communication receipt, UAT sign-off, stakeholder sentiment weighted by influence
- Identify training gaps by role and geography; auto-suggest catch-up session schedule based on available dates and trainer capacity
- When a key stakeholder turns skeptical/resistant, create an engagement action item for the change lead with suggested talking points based on known concerns
- Produce weekly change management digest: communications sent, training completion delta, stakeholder engagement summary, readiness trend
- During hypercare: monitor support ticket themes, correlate with training gaps, and recommend targeted re-training
- Post-program: generate adoption report with lessons learned and recommendations for future change programs

**Data Required:**
- Communications Plan, Training Tracker, and Stakeholder Map boards
- Program timeline and go-live date
- IT support ticket data (for hypercare monitoring)
- User login/system usage data (for adoption measurement)
- Historical change management metrics for benchmarking

**Autonomy Level:** Human-in-the-Loop
Monitoring, scoring, and recommendations are autonomous. Communication sends, stakeholder outreach, and schedule changes require change lead approval.

**Example Interaction:**
> With 30 days to the Core Banking Migration go-live, the Change Readiness Agent generates the readiness scorecard: "Overall Readiness: 67% (target: 85% for go-live approval). Breakdown by business unit: Back Office Operations — 88% ✅, Technology — 82% ✅, Middle Office — 71% ⚠️ (training gap in APAC region — only 45% complete), Front Office — 52% 🔴 (3 key stakeholders marked 'Resistant', eLearning completion at 38%). Risk: Front Office readiness will not reach 85% by go-live unless immediate action is taken."
>
> The agent recommends: "1) Schedule 3 additional instructor-led sessions for APAC Middle Office in weeks 3-4 — Trainer availability confirmed for Wed/Thu slots. 2) Front Office: arrange 1:1 meetings with resistant stakeholders (MD James Hartford, MD Lisa Wong, VP Raj Patel) — all cite 'workflow disruption during deal execution season' as concern. Suggested approach: offer dedicated hypercare support during their active deals and staggered migration timeline. 3) Convert eLearning to 15-minute micro-modules for Front Office — completion rate for micro-format is historically 3x higher in this population."

---

### Use Case 6: Risk & Issue Management Across Programs

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Every program has risks and issues. Across 150+ programs, a bank's PMO might be tracking 500-1,000+ active risks and issues. Today, each program manager maintains their own risk register (usually Excel), uses their own severity taxonomy (what's "High" to one PM is "Medium" to another), and escalates issues through ad hoc emails to their steering committee. The PMO has no aggregate view of risk across the portfolio: Which risks are the most severe? Are there systemic risks appearing across multiple programs? Which issues are blocked pending executive decisions? The annual "top 10 risks" report for the Board takes weeks to compile and is inevitably subjective.

#### The Solution
monday.com Work Management as a centralized risk and issue management system. Standardized risk register board with consistent scoring methodology (likelihood × impact matrix), connected to individual programs. Issue board tracking active issues with owner, severity, escalation status, and resolution target date. Automated escalation workflows: issues unresolved beyond target date automatically escalate to the next management tier. Portfolio risk dashboard showing aggregate risk heat map, top risks by category, systemic risk patterns (risks appearing across multiple programs), and issue aging.

#### The Outcome
- Consistent risk taxonomy across all programs enables meaningful portfolio-level risk analysis
- Escalation automation ensures no issue festers unresolved — average issue resolution time improves 35%
- Systemic risk identification: pattern detection across programs reveals bank-wide vulnerabilities
- Board and steering committee reporting produced in minutes instead of weeks
- Risk-informed resource allocation — highest-risk programs get priority resourcing automatically

#### Discovery Questions
1. "How many active risks and issues are being tracked across your program portfolio right now — and in how many different spreadsheets or tools?"
2. "Do all your program managers use the same risk scoring methodology, or does each team define 'High' differently?"
3. "When an issue is escalated to a steering committee, how long does it typically take to get a decision — and how is the decision communicated back?"
4. "Have you ever discovered that the same risk was being tracked independently by multiple programs — a systemic issue no one realized was systemic?"
5. "What does your Board risk reporting look like for the program portfolio — and how much effort goes into producing it?"

#### Industry Context
"RCSA" (Risk and Control Self-Assessment) is a standard banking risk identification exercise. "Three lines of defense" model means first line (business/PM) owns risks, second line (risk management) provides oversight, third line (internal audit) provides assurance. "Key Risk Indicators" (KRIs) are metrics that signal increasing risk. "Risk appetite" is the Board-approved level of risk the bank is willing to accept. "Operational risk" (as defined under Basel) includes program execution risk. Regulators increasingly scrutinize program risk management as part of operational resilience examinations.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a PMO Risk & Issue Register board. Create two groups: Risks and Issues. For Risks group, columns: Risk ID (text — auto-number), Risk Description (text), Program (connect to Portfolio board), Risk Category (dropdown: Technology, Resource, Vendor/Third Party, Regulatory, Budget, Scope, Organizational, Security/Cyber, Data Quality, Integration), Likelihood (status: Rare, Unlikely, Possible, Likely, Almost Certain), Impact (status: Insignificant, Minor, Moderate, Major, Catastrophic), Risk Score (formula: Likelihood rank × Impact rank), Risk Level (status: Low, Medium, High, Critical), Risk Owner (people), Mitigation Strategy (long text), Mitigation Status (status: Not Started, In Progress, Implemented, Accepted), Target Mitigation Date (date), Last Reviewed (date), Systemic Flag (checkbox — mark if risk appears in 2+ programs). For Issues group, columns: Issue ID (text), Issue Description (text), Program (connect), Severity (status: Low, Medium, High, Critical), Issue Owner (people), Raised Date (date), Target Resolution Date (date), Actual Resolution Date (date), Days Open (formula), Escalation Level (status: Program Team, Program Steering, PMO Leadership, Executive Committee, Board), Resolution Status (status: Open, In Progress, Escalated, Blocked, Resolved, Closed), Blocking Impact (long text), Decision Required (long text). Add Dashboard: risk heat map — likelihood vs. impact scatter (chart), risks by category (chart), top 10 risks by risk score (table), open issues by severity and aging (chart), issues pending escalation decisions (filtered table), systemic risks (filtered — Systemic Flag checked). Add automations: when Issue Target Resolution Date has passed and Resolution Status is not Resolved or Closed, auto-escalate: change Escalation Level to next tier and notify next-level approver. When Risk Score changes to Critical, immediately notify PMO Leadership."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Risk Intelligence Agent
**Agent Purpose:** Aggregate, analyze, and escalate risks and issues across the program portfolio, detecting systemic patterns and ensuring timely resolution.

**Triggers:**
- Daily scan for overdue issues and risk review dates
- When a new risk with Critical level is created
- When the same risk category appears in 3+ programs within 30 days (systemic pattern)
- Monthly portfolio risk report generation
- When an issue is escalated to Executive Committee level

**Actions:**
- Auto-detect systemic risks: identify similar risks appearing across multiple programs and flag for portfolio-level mitigation
- Generate monthly portfolio risk report: top risks by program, risk trends (new, escalated, mitigated, closed), systemic patterns, issue resolution metrics
- Auto-escalate issues that exceed target resolution dates through the escalation hierarchy with context summary for the next decision-maker
- Produce risk-adjusted program health scores incorporating risk and issue data into portfolio health assessments
- Track mitigation effectiveness: when risks are marked "Implemented," monitor for recurrence and validate mitigation held
- Generate Board Risk Committee summary: portfolio risk posture, top 5 risks requiring Board attention, regulatory program risk status

**Data Required:**
- Risk & Issue Register board
- Program Portfolio board
- Historical risk data for trend analysis
- Escalation hierarchy and approval workflows
- Regulatory program milestone data

**Autonomy Level:** Escalation-Based
Risk monitoring, pattern detection, and reporting are fully autonomous. Escalation notifications are automated per defined rules. Mitigation strategy recommendations require Risk Owner approval.

**Example Interaction:**
> The Risk Intelligence Agent detects a systemic pattern: "Vendor Delivery Delay" risks have been raised in 5 programs within the last 3 weeks, all involving the same technology vendor — Infosys. Individual program managers rated them as Medium, but the agent recognizes the portfolio-level impact: "🚨 Systemic Risk Detected: Infosys delivery delays affecting 5 programs (AML Remediation, Core Banking Migration, Trading Platform Upgrade, Client Onboarding v2, Regulatory Reporting Enhancement). Aggregate impact: if delays persist, 3 of 5 programs will miss Q3 milestones. Combined budget at risk: $12.4M in schedule-driven cost overruns. Individual programs rated this as Medium — but at portfolio level, this is Critical. Recommended action: PMO Leadership to convene vendor review meeting with Infosys delivery management. Consider activating backup vendor clause in MSA for the 2 highest-priority programs."

---

### Use Case 7: PMO Governance & Reporting Automation

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
PMO teams in investment banks spend a staggering amount of time producing governance reports. Weekly status updates to program steering committees, monthly portfolio reviews for the COO, quarterly updates for the Board Risk Committee, and ad hoc reports for regulators. The content is largely the same data repackaged for different audiences with different levels of detail. A PMO of 12 people might have 3-4 FTEs effectively working full-time on report production: collecting data from program managers (who are slow to respond), formatting it into the required templates, getting it reviewed and approved, and distributing it. This reporting overhead leaves less time for actual program management — the PMO becomes a reporting factory rather than a value-adding governance function.

#### The Solution
monday.com Work Management as the single source of truth that auto-generates reports at different levels of aggregation. Program-level status reports auto-populated from task and milestone data. Portfolio-level dashboards that roll up in real-time. Scheduled report generation and distribution to governance committees. Custom views for different audiences: detailed workstream view for steering committees, executive summary for the COO, and risk-focused view for the Board. Eliminated the need for manual status collection — if it's in the system, it's in the report.

#### The Outcome
- 70-80% reduction in report production time — PMO analysts refocused on value-add activities
- Reports are always current — no more 2-week-old data in monthly reviews
- Consistent reporting format across all programs eliminates "every PM does it differently" problem
- Self-service dashboards mean ad hoc requests no longer require PMO analyst time
- Governance meetings become decision-focused (reviewing real-time data) rather than information-focused (reviewing stale reports)

#### Discovery Questions
1. "How many governance reports does your PMO produce per week/month, and how many FTE-hours go into producing them?"
2. "What percentage of a steering committee meeting is spent reviewing status information versus making decisions?"
3. "How long is the lag between when program data changes and when it appears in a governance report?"
4. "If the COO asked right now for the status of all Tier 1 programs, how quickly could you produce an accurate answer?"
5. "Have you ever considered that your PMO spends more time reporting on work than managing work?"

#### Industry Context
"Steering committee" (or "SteerCo") is the governance body for each major program — typically meets monthly with the executive sponsor, program manager, and key stakeholders. "RAID log" (Risks, Assumptions, Issues, Dependencies) is a standard PM artifact expected in every status report. "RAG report" is the one-page Red/Amber/Green status summary that executives expect. "Gate review" or "stage gate" is a formal decision point where a program must demonstrate readiness before proceeding to the next phase. Banks often require committee approval at each gate.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a PMO Governance Reporting board. Columns: Report Name (text), Report Type (dropdown: Weekly Program Status, Monthly Steering Committee, Monthly Portfolio Review, Quarterly Board Update, Regulatory Status, Ad Hoc Executive Request), Program/Portfolio (connect to Portfolio board), Audience (dropdown: Steering Committee, COO Office, CTO Office, Board Risk Committee, Regulatory Affairs, Division Head, Ad Hoc), Reporting Period (text), Status (status: Data Collection, Draft, In Review, Approved, Distributed), Report Owner (people), Reviewer (people), Distribution Date (date), Template Link (link), Generated Report Link (link), Notes (long text). Create groups: Recurring Reports, Ad Hoc Requests, Report Templates. Add Dashboard: report calendar (timeline view), reports due this week (filtered table), report production metrics — average days from start to distribution (chart), reports by type per month (chart). Add automations: 5 days before Distribution Date, create task for Data Collection and notify Report Owner. 2 days before Distribution Date if Status is not 'Approved', alert Report Owner and Reviewer: 'Report due in 2 days — still in {Status} stage.' When Status changes to 'Distributed', log completion date for metrics tracking."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Governance Report Generator
**Agent Purpose:** Auto-generate governance reports by aggregating live program data, eliminating manual status collection and formatting.

**Triggers:**
- Reporting schedule (configured per report type — weekly, monthly, quarterly)
- Report item created with Status = "Data Collection"
- Ad hoc request: "Generate a status summary for [Program/Portfolio]"
- 48 hours before Board Risk Committee meeting
- Manual trigger by PMO analyst

**Actions:**
- Auto-pull program status data from Portfolio and Program boards, Risk Register, Resource boards, and Milestone trackers
- Generate formatted report drafts tailored to audience: executive summary for Board (1-2 pages), detailed workstream status for Steering Committee (5-10 pages), portfolio health overview for COO (dashboard-style)
- Highlight changes since last report: status changes, new risks escalated, milestones completed, milestones missed
- Pre-populate RAID log summaries from centralized risk and issue boards
- Generate "decision items" section: list of open items requiring governance body approval or direction
- After distribution, track acknowledgment and log completion metrics for PMO performance dashboards

**Data Required:**
- All PMO boards (Portfolio, Programs, Risks, Issues, Resources, Milestones)
- Previous report versions for change tracking
- Governance calendar and distribution lists
- Report templates by audience type

**Autonomy Level:** Human-in-the-Loop
Report generation and data aggregation are autonomous. All reports require PMO analyst review and approver sign-off before distribution. Draft quality is high enough that review time drops from hours to minutes.

**Example Interaction:**
> It's the 3rd business day of the month, and the Governance Report Generator activates for the Monthly Portfolio Review. It pulls data from all 147 active programs, aggregates risk and issue data, and generates a draft report: "Monthly Portfolio Review — February 2026. Executive Summary: 147 active programs. Portfolio health: 76% Green, 16% Amber, 5% Red, 3% On Hold. Month-over-month: 4 programs improved (Amber → Green), 2 declined (Green → Red — Cloud Migration Phase 3 and Payments Platform Upgrade). Budget: $2.34B total, $1.02B YTD spend (43.6%), $2.41B forecast at completion (2.9% over budget). Key decisions required: (1) Cloud Migration Phase 3 — approve $2.1M budget increase for vendor staff augmentation, (2) Payments Platform Upgrade — approve 6-week timeline extension due to regulatory scope change. Top 3 risks: [details]. Regulatory program status: 23 active, 19 Green, 3 Amber, 1 Red (AML Transaction Monitoring — see separate escalation memo)."
>
> The PMO Head reviews the draft, adjusts two commentary sections, approves, and the report is distributed to the COO's office and all division heads — total time from generation to distribution: 45 minutes (previously: 12 business days).

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| RAG Status | Red/Amber/Green health indicator used universally in program governance |
| Steering Committee (SteerCo) | Governance body for a program, typically executive sponsor + key stakeholders |
| RAID Log | Risks, Assumptions, Issues, Dependencies — standard program management artifact |
| Gate Review / Stage Gate | Formal checkpoint where a program must demonstrate readiness to proceed |
| Consent Order | Regulatory enforcement action requiring remediation within a specified timeframe |
| MRA / MRIA | Matter Requiring Attention / Matter Requiring Immediate Attention — regulatory findings |
| Three Lines of Defense | Banking governance model: business (1st), risk/compliance (2nd), internal audit (3rd) |
| Run the Bank (RTB) | Ongoing operational activities to maintain current business operations |
| Change the Bank (CTB) | Project/transformation activities to improve or change the business |
| FTE | Full-Time Equivalent — standard resource measurement unit |
| Hypercare | Intensive post-go-live support period, typically 2-4 weeks |
| UAT | User Acceptance Testing — business users validate system before go-live |
| PMI | Post-Merger Integration — the program of work to combine two organizations after an acquisition |
| DORA | Digital Operational Resilience Act — EU regulation requiring operational resilience in financial services |
| Basel IV | Comprehensive banking regulation framework affecting capital requirements and risk modeling |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Operating Officer (COO) | P&L owner for operations, PMO governance, strategic portfolio decisions | Decision-maker / Budget holder |
| Chief Technology Officer (CTO) | Technology strategy, IT program oversight, platform decisions | Decision-maker |
| PMO Head / VP of Program Management | Portfolio oversight, resource allocation, governance, methodology | Champion / Influencer |
| Program Manager | Individual program delivery, stakeholder management, risk mitigation | User / Champion |
| Division Head (IB, Markets, Wealth) | Business line leader, program sponsor for division-specific initiatives | Decision-maker / Sponsor |
| Chief Risk Officer (CRO) | Risk oversight, regulatory program governance, Board Risk Committee reporting | Influencer / Decision-maker |
| Head of Regulatory Affairs | Regulatory relationship management, compliance program oversight | Influencer |
| Chief Administrative Officer (CAO) | Corporate functions oversight, operational efficiency mandates | Decision-maker |
| Internal Audit | Independent assurance on program governance and control effectiveness | Gatekeeper |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Technology program delivery, infrastructure, development teams | End-to-end technology program management, DevOps integration |
| Operations | Process improvement, operational resilience, BAU/change integration | Operational efficiency programs, process automation tracking |
| Sales (Coverage) | Deal execution coordination, pipeline-driven resource planning | Deal execution PMO, transaction workstream management |
| Finance | Budget tracking, cost allocation, financial reporting | Program financial management, cost-to-complete forecasting |
| HR | Organizational change management, training delivery, workforce planning | Change management for transformation programs, resource capability building |
| Legal & Compliance | Regulatory program delivery, compliance milestone tracking | Regulatory program management, consent order remediation tracking |
| Security & Infosec | Cybersecurity programs, operational resilience, audit remediation | Security program portfolio management, vulnerability remediation tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Microsoft Project / Project for the Web | Legacy PM tool, often mandated by IT | Limited portfolio visibility, no real-time collaboration; monday.com offers modern UX + portfolio dashboards |
| Planview / Clarity PPM | Enterprise portfolio management for large banks | Expensive, complex, low adoption; monday.com offers comparable portfolio features with 10x better user experience and faster deployment |
| Smartsheet | Spreadsheet-like PM tool gaining traction in bank PMOs | Strong for individual PMs but weak on portfolio aggregation and AI; monday.com offers deeper portfolio management |
| ServiceNow PPM | IT-focused portfolio management | Strong in IT operations but poor for business-led programs; monday.com bridges IT and business PMO |
| Jira / Atlassian | Used by technology teams for agile delivery | Monday.com complements Jira for business-side program management; integration opportunity |
| Excel / SharePoint | Default for many bank PMOs | Zero portfolio visibility, massive manual overhead; monday.com replaces the spreadsheet PMO |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Planview/Clarity" | "Planview is powerful but notoriously difficult to adopt — most banks use it at 30-40% of capability with PMs reverting to Excel. monday.com can either replace it with a more adoptable solution or sit alongside it as the daily working layer that drives actual PM adoption while syncing data back for enterprise reporting." |
| "Our PMs use different methodologies — Waterfall, Agile, Hybrid" | "monday.com is methodology-agnostic. Your Waterfall programs get Gantt charts and stage gates. Your Agile teams get sprint boards and burndown charts. Your PMO gets a unified portfolio view regardless of delivery methodology." |
| "We can't put program data in the cloud — security concerns" | "monday.com serves regulated financial institutions globally with enterprise-grade security: SOC 2 Type II, ISO 27001, data residency options, SSO, and fine-grained permissions. Your program metadata (status, milestones, resources) isn't client data — it's operational data that benefits enormously from accessible, collaborative tooling." |
| "We need audit trails for regulatory programs" | "monday.com provides timestamped activity logs, version history, and approval workflows that create defensible audit trails. Every status change, every document upload, every approval is logged with who, what, and when — exactly what regulators want to see." |
| "We tried this before and PMs didn't adopt it" | "Adoption fails when the tool adds work instead of removing it. monday.com eliminates the biggest PMO pain point — manual status collection and report production. When the tool does the reporting for you, PMs adopt it because it makes their life easier, not harder." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for banking/financial services PMO implementations]
- [Placeholder for regulatory program management success stories]
- [Placeholder for portfolio management efficiency metrics]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
