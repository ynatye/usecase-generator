# Electricity, Oil & Gas × IT Playbook

## Overview

Information Technology departments in the electricity, oil, and gas sector operate under extraordinary constraints that distinguish them from IT in virtually any other industry. These teams must maintain operational technology (OT) environments—SCADA systems, distributed control systems (DCS), pipeline monitoring networks, and smart grid infrastructure—alongside conventional enterprise IT stacks. The convergence of IT and OT (often called IT/OT convergence) is the defining challenge of the decade, driven by digital oilfield initiatives, grid modernization programs, and regulatory mandates like NERC CIP (North American Electric Reliability Corporation Critical Infrastructure Protection) for utilities and TSA Pipeline Security Directives for midstream operators.

A typical upstream or midstream energy company's IT organization supports 5,000–50,000 endpoints spread across remote wellheads, offshore platforms, compressor stations, refineries, and corporate offices spanning multiple countries and time zones. Downtime costs are staggering—an unplanned refinery outage can exceed $1 million per day, and grid disruptions carry regulatory penalties plus public-safety implications. IT teams must manage cybersecurity across air-gapped and connected environments, ensure compliance with SOX, NERC CIP, EPA reporting, and FERC regulations, and simultaneously modernize legacy systems that may be running on decades-old protocols (Modbus, DNP3, OPC).

The organizational structure typically includes a CIO or VP of IT reporting to the CFO or COO, with directors overseeing Enterprise Applications (SAP/Oracle ERP, Maximo, PI Historian), Infrastructure & Operations (data centers, cloud, networking), Cybersecurity & OT Security, Data & Analytics (reservoir modeling, grid analytics, commodity trading platforms), and Digital Transformation / Innovation teams. Budgets range from $50M to $500M+ for major operators, with 30–40% allocated to "keep the lights on" maintenance and a growing share shifting toward cloud migration, AI/ML initiatives, and cybersecurity hardening.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Energy IT teams manage 200+ applications across IT/OT; consolidation reduces integration debt, licensing costs, and attack surface |
| 2 | Replace or Radically Augment Headcount | High | Chronic talent shortage in energy IT (especially OT-skilled engineers); automation of L1/L2 support and change management is critical |
| 3 | Scale Impact Without Overhead | Medium-High | Digital transformation mandates from leadership require IT to deliver more projects without proportional headcount growth |

## Prioritized Use Cases

---

### Use Case 1: IT/OT Convergence Program Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies are merging historically siloed IT and OT environments to enable predictive maintenance, remote operations, and data-driven decision-making. But the convergence program involves dozens of interdependent workstreams—network segmentation, historian modernization, edge computing deployment, cybersecurity policy alignment—managed across multiple business units and geographies. Today, these are tracked in disconnected spreadsheets, SharePoint sites, and Primavera schedules that nobody trusts. Program managers spend 60% of their time chasing status updates instead of removing blockers.

#### The Solution
monday.com Work Management serves as the central IT/OT convergence program hub. A master program board tracks every workstream (Network Architecture, Data Integration, Security Hardening, Edge Deployment, Application Rationalization) with status columns, timeline views for Gantt-style scheduling, dependency tracking between workstreams, and rollup dashboards showing overall program health. Sub-boards for each workstream contain granular tasks with people assignments, priority flags, and integration with Jira (for OT engineering tickets) and ServiceNow (for IT change requests). monday.com Dashboards aggregate KPIs: milestones hit vs. planned, budget burn rate, risk register items by severity, and cross-workstream dependency conflicts.

#### The Outcome
40% reduction in status-reporting overhead. Real-time program visibility for CIO and VP of Engineering without waiting for monthly steering committee decks. 25% improvement in milestone adherence through proactive dependency management. Single source of truth eliminates "which version is correct?" debates.

#### Discovery Questions
1. "How many workstreams does your IT/OT convergence program currently span, and how do you track cross-workstream dependencies today?"
2. "What's your current cadence for program status reporting, and how many hours per week does your PMO spend assembling those reports?"
3. "When a network segmentation delay impacts your historian migration timeline, how quickly does that cascade become visible to leadership?"
4. "Are your OT engineering teams using different project tools than your IT teams, and how do you reconcile those views?"
5. "What's your biggest concern about the convergence program—timeline, budget, security risk, or organizational alignment?"

#### Industry Context
IT/OT convergence is not optional—it's driven by digital oilfield economics (remote wellhead monitoring can reduce field visits by 70%), grid modernization mandates (FERC Order 2222 for distributed energy resources), and insurance requirements for cyber-physical risk management. The Purdue Model (ISA-95) defines the reference architecture for how IT (Levels 4-5) connects to OT (Levels 0-3) through a demilitarized zone (DMZ). SEs should understand that OT teams historically distrust IT involvement ("you'll break my plant"), so the platform must demonstrate respect for OT workflows while enabling visibility.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT/OT Convergence Program Tracker with these boards: (1) Master Program Board — columns: Workstream Name (text), Workstream Lead (people), Status (status: Not Started, In Planning, In Progress, Testing, Complete, Blocked), Priority (status: Critical Path, High, Medium, Low), Target Start (date), Target End (date), Actual End (date), Budget Allocated (numbers, USD), Budget Spent (numbers, USD), Risk Level (status: Low, Medium, High, Critical), Dependencies (connect boards to same board for cross-workstream links), Notes (long text). Create items: Network Segmentation, Historian Modernization, Edge Computing Rollout, Security Policy Alignment, Application Rationalization, Data Lake Integration, Remote Operations Enablement. (2) Risk Register Board — columns: Risk ID (text), Risk Description (long text), Workstream (dropdown: same list), Probability (status: Low, Medium, High), Impact (status: Low, Medium, High, Critical), Mitigation Plan (long text), Owner (people), Status (status: Open, Mitigating, Accepted, Closed), Review Date (date). Add views: Timeline view on Master Board grouped by workstream, Dashboard with widgets showing program milestone burndown, budget burn rate pie chart, risk heat map by workstream, and blocked items count."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Convergence Sentinel
**Agent Purpose:** Automatically detect cross-workstream dependency conflicts and escalate risks before they cascade into program delays.

**Triggers:**
- Status change on any workstream task to "Blocked" or "Delayed"
- Target End date within 5 business days and status not "Complete" or "Testing"
- New item added to Risk Register with Impact = "Critical"
- Weekly scheduled scan every Monday at 7:00 AM
- Budget Spent exceeds 80% of Budget Allocated on any workstream

**Actions:**
- Cross-reference dependency links to identify all downstream workstreams impacted by a delay
- Generate impact assessment summary with revised timeline projections
- Create notification items in affected workstream leads' boards
- Auto-update Risk Register with new dependency-driven risks
- Compose weekly Convergence Health Briefing and post to executive dashboard
- Escalate to CIO if two or more critical-path workstreams are simultaneously blocked

**Data Required:**
- All workstream boards with dependency connections
- Risk Register board
- Budget tracking data (integration with SAP or Oracle Financials)
- Resource allocation data (people assignments across workstreams)

**Autonomy Level:** Escalation-Based
Routine dependency analysis and risk register updates are fully autonomous. Timeline re-projection notifications require workstream lead acknowledgment within 24 hours before escalating. Any recommendation to re-sequence critical-path workstreams requires CIO approval.

**Example Interaction:**
> On Tuesday morning, the Convergence Sentinel detects that the Network Segmentation workstream has moved to "Blocked" status due to a delayed firewall hardware delivery from Palo Alto Networks. The agent immediately traces dependency links and identifies that the Historian Modernization workstream (scheduled to begin data migration in 2 weeks) depends on the segmented network being in place. It also flags that Edge Computing Rollout has a secondary dependency on the same network zones.
>
> The agent generates an impact assessment: "Network Segmentation delay of 3 weeks will push Historian Modernization start from March 15 to April 5 and Edge Computing Rollout from April 1 to April 22. Cumulative program delay: 3 weeks. Budget impact: estimated $180K in extended contractor costs." It creates risk items in the Risk Register, notifies the Historian and Edge workstream leads, and posts a summary to the executive dashboard.
>
> When the workstream leads don't acknowledge within 24 hours, the agent escalates to the VP of IT with a recommended re-sequencing option: "Accelerate Application Rationalization (no network dependency) to maintain overall program velocity while Network Segmentation resolves."

---

### Use Case 2: Cybersecurity Compliance & Audit Management (NERC CIP / TSA Directives)

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy companies face the most demanding cybersecurity compliance landscape of any industry. Electric utilities must comply with 40+ NERC CIP standards covering electronic security perimeters, physical security, personnel training, incident reporting, and configuration change management—with potential fines of $1 million per violation per day. Pipeline operators face TSA Pipeline Security Directives requiring cybersecurity implementation plans, incident reporting within 12 hours, and annual architecture reviews. Compliance teams of 3–8 people manage thousands of evidence artifacts, audit trails, and remediation tickets across spreadsheets, GRC tools like Archer or ServiceNow, and email threads. Audit prep consumes 4–6 weeks of intensive labor, and findings often result from documentation gaps rather than actual security failures.

#### The Solution
monday.com Work Management structures the entire compliance lifecycle. A master Compliance Standards board maps every applicable NERC CIP requirement (or TSA directive) with columns for standard ID, requirement description, control owner, evidence type, evidence location, last review date, next review date, and compliance status. Connected boards track Evidence Collection (with file uploads, approval workflows, and version control), Remediation Actions (with priority, assignee, due date, and verification steps), and Audit Calendar (with timeline views for audit schedules, evidence submission deadlines, and regulatory filing dates). Automations trigger evidence review reminders 30 days before expiration, escalate overdue remediation items, and generate audit-ready reports.

#### The Outcome
60% reduction in audit preparation time. Zero documentation-related findings in annual NERC CIP audits. 50% reduction in compliance team overtime during audit seasons. Continuous compliance posture visibility replaces point-in-time scrambles.

#### Discovery Questions
1. "How many NERC CIP standards or TSA directives are in scope for your organization, and how do you currently map controls to evidence?"
2. "What happened during your last audit—were findings related to actual security gaps or documentation/process gaps?"
3. "How many person-hours does your team spend preparing for a NERC CIP audit, and what does that cost in terms of other deferred security work?"
4. "Do you have a single view of your compliance posture across all applicable standards, or do different teams own different pieces?"
5. "How do you handle evidence that spans IT and OT environments—is there a unified collection process?"

#### Industry Context
NERC CIP standards range from CIP-002 (BES Cyber System Categorization) through CIP-014 (Physical Security). Each has specific evidence requirements—for example, CIP-007 requires documented patch management processes with evidence of patch applicability assessments within 35 days of release. TSA Pipeline Security Directives (SD-01, SD-02) were emergency mandates post-Colonial Pipeline attack (2021) requiring cybersecurity implementation plans, network segmentation documentation, and 12-hour incident reporting. SEs should know that compliance teams often feel trapped between "we need better tools" and "our GRC platform costs $500K/year and still doesn't work well."

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a NERC CIP Compliance Management System with these boards: (1) Standards & Controls Board — columns: Standard ID (text, e.g. CIP-007-6 R2), Requirement Description (long text), Control Category (dropdown: Access Control, Audit & Accountability, Configuration Management, Incident Response, Patch Management, Personnel & Training, Physical Security, Recovery, System Security), Control Owner (people), Evidence Type (dropdown: Policy Document, Screen Capture, System Report, Log Export, Training Record, Configuration File, Interview Notes), Evidence Status (status: Current, Expiring Soon, Expired, Not Collected), Last Review Date (date), Next Review Date (date), Compliance Status (status: Compliant, Partially Compliant, Non-Compliant, Not Assessed), Risk Rating (status: Low, Medium, High, Critical). Add 10 sample items for CIP-002 through CIP-011 key requirements. (2) Evidence Repository Board — columns: Evidence ID (auto-number), Linked Standard (connect boards to Standards board), Evidence File (files), Collected By (people), Collection Date (date), Expiration Date (date), Approved By (people), Approval Date (date), Status (status: Draft, Under Review, Approved, Expired). (3) Remediation Tracker — columns: Finding ID (text), Source (dropdown: Internal Audit, External Audit, Self-Assessment, Incident), Related Standard (connect boards), Description (long text), Priority (status: Critical, High, Medium, Low), Assigned To (people), Due Date (date), Status (status: Open, In Progress, Verification, Closed), Verification Evidence (files). Add automations: when Evidence Status changes to Expiring Soon notify Control Owner; when Remediation Due Date is within 7 days and Status is not Closed notify Assigned To and their manager. Create Dashboard with compliance percentage by category, overdue remediation count, evidence freshness timeline, and upcoming audit calendar."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CIP Compliance Watchdog
**Agent Purpose:** Continuously monitor compliance posture, auto-collect recurring evidence, and generate audit-ready packages on demand.

**Triggers:**
- Daily scan at 6:00 AM for evidence items approaching expiration (within 30 days)
- New remediation item created with Priority = "Critical"
- Quarterly scheduled audit readiness assessment
- Manual trigger: "Generate audit package for [Standard ID]"
- Integration trigger: new vulnerability scan results from Tenable/Qualys

**Actions:**
- Auto-generate evidence collection tasks for expiring items with pre-populated instructions
- Cross-reference remediation items against original findings to verify closure completeness
- Compile audit packages: gather all evidence files, organize by standard, generate cover sheet with compliance summary
- Analyze vulnerability scan results against CIP-007 patch management requirements and create remediation items for applicable patches
- Generate monthly Compliance Posture Report with trend analysis
- Escalate any standard moving from "Compliant" to "Partially Compliant" to CISO

**Data Required:**
- Standards & Controls board with all NERC CIP mappings
- Evidence Repository with file attachments
- Integration with vulnerability scanning tools (Tenable, Qualys, Nessus)
- Integration with patch management system (WSUS, SCCM, or OT-specific like Claroty)
- Audit calendar and regulatory filing deadlines

**Autonomy Level:** Human-in-the-Loop
Evidence collection task creation and reminder generation are autonomous. Audit package compilation is autonomous but requires compliance manager review before submission. Any change to compliance status requires human verification. Vulnerability-to-remediation mapping is suggested but requires security analyst approval.

**Example Interaction:**
> Thirty days before the annual NERC CIP audit, the CIP Compliance Watchdog initiates its quarterly readiness assessment. It scans all 147 control requirements and identifies 12 evidence items that will expire before the audit date, 3 remediation items still marked "In Progress" from the previous audit cycle, and 1 standard (CIP-010-3 R1 - Configuration Change Management) where the evidence file is a policy document last updated 18 months ago.
>
> The agent creates prioritized evidence collection tasks: "Re-capture screen evidence for CIP-007-6 R2 patch management process — last captured June 2025, expires Feb 28, 2026." For the outdated policy document, it flags: "CIP-010-3 R1 Configuration Change Management Policy was last revised August 2024. Recommend review and update before audit." It compiles a draft audit package for the compliance manager showing 94.5% readiness with a clear action list to reach 100%.
>
> The compliance manager reviews, approves the package structure, and assigns the 12 evidence collection tasks to team members. The agent tracks completion daily and provides a countdown dashboard: "Audit in 22 days — 8 of 12 evidence items collected, 2 remediation items closed, 1 policy under review."

---

### Use Case 3: IT Service Management & Intelligent Ticket Routing

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy company IT help desks handle 5,000–20,000 tickets per month spanning corporate IT (laptop issues, VPN access, SAP problems) and operational technology requests (historian tag configuration, SCADA HMI updates, DCS patch coordination). L1 analysts struggle to triage OT-related tickets because they lack domain knowledge, leading to misrouting rates of 25–35%. Average resolution time for OT tickets is 3x longer than corporate IT because they bounce between queues. Meanwhile, the talent market for OT-literate IT support staff is brutally competitive—qualified candidates command $120K–$160K salaries and still leave for operators offering better rotational schedules.

#### The Solution
monday.com Service replaces or augments the existing ITSM platform for intelligent ticket management. Intake forms capture structured data: asset type (IT/OT), location (facility, unit, area), system affected (dropdown: SAP, PI Historian, SCADA, DCS, Network, Endpoint, Cloud), urgency, and business impact. Automations route tickets based on asset type and system: OT tickets go directly to the OT support queue with required context fields pre-populated. monday.com AI assists L1 analysts by suggesting categorization based on ticket description patterns. Dashboards show SLA compliance by category, backlog aging, and resolution trends segmented by IT vs. OT.

#### The Outcome
Ticket misrouting reduced from 30% to under 8%. Mean time to resolution (MTTR) for OT tickets reduced by 40%. L1 analyst productivity increased 25% through AI-assisted categorization. Annual savings of $200K+ in reduced escalation costs and avoided headcount.

#### Discovery Questions
1. "What percentage of your IT tickets involve operational technology systems, and how do you triage those differently from standard corporate IT requests?"
2. "What's your current ticket misrouting rate, and what does each misroute cost in terms of resolution time?"
3. "How many L1 analysts do you have, and how many open positions have been unfilled for more than 90 days?"
4. "Do your OT engineers submit tickets through the same portal as corporate users, or do they have a separate process?"
5. "What's your SLA for critical OT-related tickets—and how often do you actually meet it?"

#### Industry Context
In energy, a misrouted OT ticket isn't just an inconvenience—if a SCADA alarm configuration request sits in the wrong queue for 48 hours, it could delay safety-critical maintenance. The IT/OT support divide is cultural as much as technical: OT engineers often bypass IT ticketing entirely, calling or texting their "guy" directly. A good ITSM solution must feel lightweight enough for OT engineers while providing the structure IT leadership needs for compliance and capacity planning. Integration with PI System (OSIsoft/AVEVA) historian and CMMS (Maximo, SAP PM) is a key differentiator.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Energy IT/OT Service Desk with these boards: (1) Ticket Intake Board — columns: Ticket ID (auto-number), Requester (people), Request Type (dropdown: Incident, Service Request, Change Request, Problem), Asset Category (status: Corporate IT, Operational Technology, Network Infrastructure, Cloud Services), Facility (dropdown: HQ, Refinery A, Refinery B, Pipeline Control Center, Field Office West, Field Office East, Offshore Platform 1), System Affected (dropdown: SAP ERP, PI Historian, SCADA/HMI, DCS, Active Directory, VPN/Network, Endpoints, Cloud Apps, Other), Urgency (status: Critical-Safety, Critical-Production, High, Medium, Low), Description (long text), Assigned Team (dropdown: L1 Support, OT Engineering, Network Ops, SAP Team, Cloud Team, Security), Assigned To (people), Status (status: New, Triaged, In Progress, Waiting on Vendor, Waiting on User, Resolved, Closed), SLA Due (date), Resolution Notes (long text). Add automation: when Asset Category is Operational Technology, set Assigned Team to OT Engineering; when Urgency is Critical-Safety, notify OT Engineering lead and facility manager immediately. (2) SLA Dashboard — widgets: Average resolution time by Asset Category, SLA compliance percentage gauge, ticket volume trend (last 30 days), open tickets by facility (bar chart), backlog aging by team (stacked bar). Add form view for ticket submission with conditional fields: if Asset Category = OT, show Facility and System Affected as required."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SmartRoute Dispatcher
**Agent Purpose:** Intelligently triage and route incoming IT/OT tickets using historical patterns and asset context to eliminate misrouting.

**Triggers:**
- New ticket created via form or email integration
- Ticket status unchanged for more than 4 hours (stale ticket detection)
- Ticket reassigned more than twice (bounce detection)
- Shift change schedule (6:00 AM, 2:00 PM, 10:00 PM) for handoff summaries

**Actions:**
- Analyze ticket description using NLP to classify as IT or OT and suggest system category
- Cross-reference requester's facility and role against asset database to validate categorization
- Route to appropriate team queue with confidence score and reasoning
- If confidence < 70%, flag for human triage with top-2 routing recommendations
- Detect ticket bounces and escalate to service delivery manager with root cause suggestion
- Generate shift handoff summaries listing critical open tickets, approaching SLAs, and overnight activity

**Data Required:**
- Historical ticket data (12+ months) for pattern learning
- Asset database (CMDB) with facility-to-system mappings
- Personnel directory with facility assignments and roles
- SLA definitions by ticket category and urgency
- On-call rotation schedules

**Autonomy Level:** Human-in-the-Loop
High-confidence routing (>85%) is autonomous with a 15-minute human override window. Medium-confidence routing (70–85%) presents recommendation for L1 analyst to confirm with one click. Low-confidence routing (<70%) requires manual triage. All safety-critical tickets (Urgency = Critical-Safety) are routed autonomously to OT Engineering AND flagged to the facility safety officer simultaneously.

**Example Interaction:**
> A ticket arrives at 2:47 AM from a control room operator at Refinery B: "PI tag for FCC reactor temperature not updating — last good value was 3 hours ago. Need historian support ASAP." The SmartRoute Dispatcher analyzes the description, identifies keywords "PI tag," "FCC reactor," and "historian," and cross-references the requester against the personnel directory (confirmed: Senior Operator, Refinery B FCC Unit).
>
> The agent routes with 96% confidence to the OT Engineering queue, sets Urgency to "Critical-Production" (FCC reactor monitoring is production-critical), assigns the on-call OT historian engineer (pulled from the rotation schedule), and sends an immediate notification: "Critical PI Historian ticket from Refinery B FCC — tag update failure for 3+ hours. On-call engineer notified." The entire triage happens in under 30 seconds — compared to the 4+ hours it would have taken if the ticket landed in the general L1 queue during overnight shift.

---

### Use Case 4: Application Portfolio Rationalization & Cloud Migration Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Large energy companies maintain 300–800 enterprise applications accumulated through decades of acquisitions, technology shifts, and departmental shadow IT. The IT application portfolio is a tangled mess: 5 different document management systems, 3 ERP instances from pre-merger entities, 12 analytics tools with overlapping capabilities, and dozens of custom-built applications with single-person dependencies ("Bob built this 15 years ago and he's retiring in March"). Cloud migration mandates from leadership add urgency, but nobody has a clear picture of what to migrate, what to consolidate, what to retire, and what to leave on-premises (especially OT-adjacent applications that can't move to public cloud for latency or security reasons).

#### The Solution
monday.com Work Management creates a comprehensive Application Portfolio Management (APM) system. The master Application Inventory board captures every application with columns for name, vendor, business owner, technical owner, user count, annual cost (license + support + infrastructure), technology stack, data classification (public, internal, confidential, restricted/OT), cloud readiness score, business criticality (mission-critical, important, convenience, candidate for retirement), and disposition decision (migrate, consolidate, modernize, retain, retire). Connected boards track Migration Projects (with timeline, milestones, dependencies, and go/no-go checklists), Vendor Contracts (renewal dates, terms, exit clauses), and Technical Debt items. Dashboards show total portfolio cost by disposition category, migration progress, and applications approaching contract renewal decisions.

#### The Outcome
Identification of $2M–$5M in annual savings through application retirement and consolidation. 35% faster migration decision-making. Zero "surprise" contract renewals (auto-renewal notifications 90 days out). Clear retirement roadmap eliminates single-person dependencies before they become crises.

#### Discovery Questions
1. "How many applications are in your IT portfolio today, and when was the last time you did a full inventory?"
2. "How many applications are on your 'retire' list that have been there for more than two years without actually being retired?"
3. "What happens when a contract auto-renews for an application you intended to sunset—how much has that cost you in the last 3 years?"
4. "How do you assess cloud readiness for applications that touch OT data or have latency-sensitive dependencies?"
5. "Do you have visibility into shadow IT—applications that business units procured directly without IT involvement?"

#### Industry Context
Energy companies face unique APM challenges: OT applications (PI Historian, ABB Ability, Honeywell Experion) cannot move to public cloud due to latency requirements for real-time control and NERC CIP restrictions on BES Cyber System connectivity. Merger-driven complexity is extreme—when two utilities merge, they often run parallel ERP, CMMS, and trading systems for 3–5 years. SEs should understand that "rationalization" in energy IT is politically charged because every application has a constituency of users who will resist change. The platform needs to make the business case visible (cost, risk, overlap) so leadership can make informed decisions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Application Portfolio Rationalization Tracker with: (1) Application Inventory Board — columns: App Name (text), App ID (text), Vendor (text), Business Owner (people), Technical Owner (people), Department (dropdown: Operations, Finance, Trading, Engineering, HR, IT, HSE, Legal), User Count (numbers), Annual Cost (numbers, USD), Technology Stack (tags: Java, .NET, Python, COBOL, SAP, Oracle, Cloud-Native, Legacy), Data Classification (status: Public, Internal, Confidential, Restricted-OT), Cloud Readiness (status: Ready, Needs Refactoring, Not Eligible, Assessment Needed), Business Criticality (status: Mission Critical, Important, Convenience, Retire Candidate), Disposition (status: Migrate to Cloud, Consolidate, Modernize, Retain On-Prem, Retire), Contract Renewal Date (date), Migration Target Date (date), Single Person Dependency (checkbox), Notes (long text). Populate with 15 sample apps: SAP S/4HANA, OSIsoft PI Historian, Maximo CMMS, Endur/Ion Trading, ABB Ability Symphony, Oracle EBS (legacy), SharePoint 2016, Documentum, Power BI, Tableau, ServiceNow, Custom Well Planning Tool, Custom Pipeline Scheduling, Legacy Corrosion Tracking (Access DB), HR Portal (custom .NET). (2) Contract Watch Board — columns: App (connect to Inventory), Vendor (mirror), Contract Value (numbers), Start Date (date), End Date (date), Auto-Renew (checkbox), Notice Period Days (numbers), Exit Clause (long text), Action Needed (status: Renew, Renegotiate, Cancel, Under Review). Automation: when Contract End Date is within 90 days, notify Business Owner and IT Procurement. Dashboard: total annual spend by disposition category (pie), cloud migration progress (battery), applications by criticality (bar), upcoming renewals timeline, single-person dependency risk list."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio Optimizer
**Agent Purpose:** Continuously analyze the application portfolio for consolidation opportunities, cost savings, and risk reduction.

**Triggers:**
- Monthly scheduled full portfolio analysis (1st of each month)
- New application added to inventory
- Contract renewal date within 120 days
- Business Owner or Technical Owner changed to "Unassigned" (ownership gap)
- Annual cost updated (budget cycle trigger)

**Actions:**
- Identify overlapping applications by analyzing department, function tags, and user overlap
- Generate consolidation recommendations with projected savings and migration effort estimates
- Flag single-person dependencies and create knowledge transfer task templates
- Alert IT Procurement of approaching contract renewals with renewal/cancel recommendation based on disposition status
- Produce quarterly Portfolio Health Scorecard: total apps, total cost, apps retired this quarter, cost saved, migration progress, risk items
- Detect shadow IT candidates by cross-referencing expense reports and SaaS management data for unapproved tools

**Data Required:**
- Complete Application Inventory board
- Contract Watch board
- Financial data (annual costs, expense reports)
- User access logs (Active Directory / SSO) for actual usage analysis
- SaaS management platform integration (Zylo, Productiv, or similar)

**Autonomy Level:** Escalation-Based
Portfolio analysis and recommendation generation are fully autonomous. Consolidation recommendations are presented to IT governance board for approval. Contract renewal alerts are autonomous with recommended action. Shadow IT detection flags are sent to IT governance for investigation. No autonomous retirement or cancellation actions.

**Example Interaction:**
> During its monthly portfolio analysis, the Portfolio Optimizer identifies that three separate analytics tools (Power BI, Tableau, and a legacy custom reporting tool) serve overlapping user bases: 340 users have both Power BI and Tableau licenses, and the custom reporting tool has only 12 active users (down from 85 three years ago). Total combined annual cost: $890,000.
>
> The agent generates a consolidation recommendation: "Standardize on Power BI (already included in Microsoft E5 licenses). Migrate 23 Tableau-only dashboards to Power BI (estimated 4-week effort). Retire custom reporting tool — 12 remaining users can be migrated to Power BI with 2 custom reports rebuilt. Projected annual savings: $420,000. Risk: 3 Tableau dashboards use advanced statistical features requiring Power BI Premium capacity ($60K/year net new)." The recommendation lands in the IT governance board's review queue with supporting data and a draft migration timeline.

---

### Use Case 5: Capital Project IT Infrastructure Delivery

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
When the company builds a new gas processing plant, expands a wind farm, or constructs a transmission substation, IT must deliver infrastructure—networking, servers, SCADA connectivity, historian integration, cybersecurity controls, end-user computing—on the capital project's timeline. But IT project managers are typically allocated to 5–8 capital projects simultaneously, each in different phases, each with its own EPC (Engineering, Procurement, Construction) contractor expecting IT deliverables at specific construction milestones. Miss the network installation window during construction and you're paying $50K+ for retrofit work. There's no standardized IT delivery playbook, so every project manager reinvents the wheel.

#### The Solution
monday.com Work Management provides a templatized IT Capital Project Delivery framework. A master template board contains every standard IT deliverable for a new facility (network design, cybersecurity assessment, server provisioning, SCADA integration, historian configuration, end-user computing setup, communications systems, physical security IT components) with typical durations, dependencies, and milestone alignment to construction phases (Foundation, Structural, Mechanical, Electrical, Commissioning, Handover). Each new capital project spawns a copy of the template, customized for facility type and scale. Timeline views align IT milestones with construction schedules. Automations alert IT PMs when construction milestones are approaching that require IT deliverables.

#### The Outcome
Standardized delivery eliminates "reinventing the wheel"—new project setup reduced from 2 weeks to 2 hours. Zero missed construction windows for IT infrastructure installation. 30% reduction in IT PM time per project through templatized workflows. Portfolio view gives IT leadership visibility across all active capital projects.

#### Discovery Questions
1. "How many active capital projects does your IT team currently support, and how do you track IT deliverables against construction milestones?"
2. "Has your team ever missed a construction installation window for network or SCADA infrastructure—and what did the retrofit cost?"
3. "Do you have a standardized IT delivery template for new facilities, or does each project manager create their own plan?"
4. "How do you coordinate with EPC contractors on IT infrastructure requirements—is it formal or ad hoc?"
5. "When a capital project timeline shifts (which it always does), how quickly can you replan IT deliverables?"

#### Industry Context
Capital projects in energy are massive—a new gas processing plant is $500M–$2B, a utility-scale solar farm $200M–$500M, a transmission line $50M–$500M. IT infrastructure is typically 2–5% of the capital budget but is on the critical path for commissioning: you can't commission a plant if the SCADA system isn't connected and the historian isn't collecting data. EPC contractors (Bechtel, Fluor, McDermott, Quanta) have their own project controls systems (Primavera P6, typically) and expect IT to integrate with their schedules. SEs should position monday.com as the IT team's own project management layer that feeds into and receives from the master EPC schedule.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Capital Project IT Delivery Tracker with: (1) IT Deliverables Template Board — columns: Deliverable (text), Category (dropdown: Network, Cybersecurity, Servers/Compute, SCADA Integration, Historian, End-User Computing, Communications, Physical Security IT), Construction Phase Dependency (dropdown: Foundation, Structural, Mechanical, Electrical, Pre-Commissioning, Commissioning, Handover), Duration Days (numbers), Predecessor Deliverable (connect boards to self), Owner Role (dropdown: Network Engineer, Security Architect, OT Engineer, Systems Admin, IT PM), Status (status: Not Started, Design, Procurement, Install, Configure, Test, Complete), Target Start (date), Target End (date), Actual End (date), Notes (long text). Populate template items: Site Network Design, Firewall & Security Appliance Procurement, Cable Pathway Installation Coordination, Network Switch & Router Install, SCADA Server Provisioning, DCS Network Connectivity, PI Historian Node Deployment, Cybersecurity Assessment (NERC CIP), End-User Workstation Setup, Radio/Communications System, Physical Security Camera IT Infrastructure, Final Integration Testing. (2) Capital Projects Portfolio Board — columns: Project Name (text), Facility Type (dropdown: Gas Plant, Solar Farm, Wind Farm, Substation, Pipeline, Refinery Expansion), IT PM (people), Construction Start (date), Target Commissioning (date), IT Budget (numbers), IT Spend (numbers), Overall IT Status (status: On Track, At Risk, Behind, Complete), Linked Deliverables Board (connect boards). Timeline view showing all capital projects with IT milestone overlays. Dashboard: projects by status, budget vs spend, upcoming milestones this month."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Capital IT Coordinator
**Agent Purpose:** Synchronize IT deliverable timelines with construction schedules and proactively alert teams when construction milestone shifts impact IT delivery windows.

**Triggers:**
- Construction milestone date changed (integration with Primavera P6 or Procore)
- IT deliverable status not progressing as scheduled (>5 days behind)
- New capital project created in Portfolio board
- Procurement lead time exceeding expected duration for hardware orders
- 30 days before each construction phase requiring IT deliverables

**Actions:**
- Auto-generate IT deliverables board from template when new capital project is created, adjusting dates based on construction schedule
- Recalculate all IT deliverable dates when construction milestones shift, highlighting items that become critical
- Send proactive alerts to IT PMs and relevant engineers: "Electrical phase at Gas Plant Alpha moved up 2 weeks — SCADA server provisioning must complete by March 1 instead of March 15"
- Track hardware procurement status and flag items at risk of missing installation windows
- Generate weekly Capital IT Status Report for IT leadership across all active projects

**Data Required:**
- Capital Projects Portfolio board
- IT Deliverables boards for each project
- Construction schedule integration (Primavera P6, Procore, or manual updates)
- Hardware procurement tracking (PO status, shipping tracking)
- Resource allocation (which engineers are assigned to which projects)

**Autonomy Level:** Human-in-the-Loop
Template instantiation and date calculation are autonomous. Schedule change impact notifications are autonomous. Resource conflict detection alerts IT PM for resolution. Any recommendation to de-scope or defer IT deliverables requires IT leadership approval.

**Example Interaction:**
> The Capital IT Coordinator receives an update from the Primavera P6 integration: the Electrical phase at the new West Texas Gas Processing Plant has been accelerated by 3 weeks due to favorable weather. The agent immediately recalculates all dependent IT deliverables: SCADA server provisioning moves from April 15 to March 25, DCS network connectivity from April 22 to April 1, and cybersecurity assessment from May 1 to April 10.
>
> It detects a conflict: the Palo Alto firewall hardware ordered for this project has an estimated delivery date of April 5—which is now 11 days after the SCADA server needs to be online. The agent alerts the IT PM: "Hardware conflict: PA-5260 firewall delivery (April 5) is 11 days after accelerated SCADA server deadline (March 25). Options: (1) Request vendor expedite, (2) Deploy temporary firewall from spare inventory, (3) Request construction phase delay exception for IT zone." The IT PM selects option 2 and the agent creates deployment tasks for the spare equipment.

---

### Use Case 6: Vendor & Third-Party Risk Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy IT departments manage relationships with 100–300 technology vendors, from major platforms (Microsoft, SAP, Schneider Electric, ABB) to niche OT vendors (specialized SCADA integrators, pipeline modeling software companies). Each vendor relationship requires contract management, performance monitoring, security assessments (especially post-SolarWinds—supply chain security is now a board-level concern), and renewal negotiations. Most organizations track this in a combination of procurement systems, spreadsheets, and tribal knowledge. When a critical OT vendor has a security incident, it takes days to determine exposure because nobody knows exactly which systems use that vendor's components.

#### The Solution
monday.com Work Management centralizes vendor lifecycle management. The Vendor Registry board captures every vendor with columns for name, category (IT Infrastructure, OT/ICS, SaaS, Professional Services, Telecom), criticality tier, contract value, contract dates, primary contact, security assessment status, performance score, and linked applications (connected to APM board). A Security Assessment board tracks the annual vendor security review cycle with questionnaire status, findings, remediation requirements, and risk acceptance decisions. A Performance Scorecard board captures quarterly metrics: SLA compliance, incident count, responsiveness, and innovation contribution. Dashboards show vendor spend concentration, security assessment compliance, and upcoming renewal pipeline.

#### The Outcome
100% vendor security assessment completion (up from 60%). 45-day average reduction in contract renewal cycle time. Instant exposure analysis when vendor security incidents occur. $500K+ saved annually through consolidated negotiation insights.

#### Discovery Questions
1. "How many technology vendors do you actively manage, and do you have a single registry or is it spread across procurement, IT, and individual teams?"
2. "When the MOVEit or SolarWinds vulnerabilities were disclosed, how quickly could you determine which of your vendors and systems were affected?"
3. "What percentage of your critical vendors have completed a security assessment in the last 12 months?"
4. "How do you track vendor performance—is it formal or 'we'll know if they're bad when something breaks'?"
5. "When a vendor contract is up for renewal, do you have consolidated data on their performance, security posture, and total spend across all contracts?"

#### Industry Context
Post-Colonial Pipeline, energy sector vendor security scrutiny intensified dramatically. NERC CIP-013 specifically addresses Supply Chain Risk Management for BES Cyber Systems, requiring documented processes for assessing vendor security practices. TSA directives similarly require pipeline operators to evaluate third-party cyber risks. SEs should know that many OT vendors are small companies (50–200 employees) without mature security programs, making assessment and remediation tracking even more critical. The energy sector's reliance on specialized OT vendors means switching costs are extremely high—making performance management and relationship health critical.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor & Third-Party Risk Management system with: (1) Vendor Registry Board — columns: Vendor Name (text), Vendor ID (text), Category (dropdown: IT Infrastructure, OT/ICS Systems, SaaS/Cloud, Professional Services, Telecom, Hardware, Security), Criticality Tier (status: Tier 1-Critical, Tier 2-Important, Tier 3-Standard, Tier 4-Low), Primary Contact (text), Account Manager (people), Annual Spend (numbers, USD), Contract Count (numbers), Security Assessment Status (status: Current, Due Soon, Overdue, Not Required), Last Assessment Date (date), Next Assessment Due (date), Overall Risk Rating (status: Low, Medium, High, Critical), Performance Score (numbers, 1-5), NERC CIP-013 In Scope (checkbox), Notes (long text). Populate with 10 sample vendors: Microsoft, SAP, Schneider Electric, ABB, OSIsoft/AVEVA, Palo Alto Networks, Cisco, Honeywell, Claroty, Custom OT Integrator. (2) Security Assessment Tracker — columns: Vendor (connect to Registry), Assessment Year (text), Questionnaire Sent (date), Questionnaire Received (date), Findings Count (numbers), Critical Findings (numbers), Remediation Status (status: No Findings, In Remediation, Remediated, Risk Accepted, Overdue), Risk Acceptance Approver (people), Completion Date (date). (3) Performance Scorecard Board — columns: Vendor (connect to Registry), Quarter (dropdown: Q1-Q4), SLA Compliance % (numbers), Incidents (numbers), Mean Response Time Hours (numbers), Innovation Score (numbers, 1-5), Overall Score (numbers, calculated). Automation: when Security Assessment Status changes to Overdue, notify Account Manager and CISO. Dashboard: spend by vendor category (pie), security assessment compliance (gauge), vendor risk heat map, performance trend by quarter."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Vendor Risk Sentinel
**Agent Purpose:** Monitor vendor security posture, automate assessment workflows, and provide instant exposure analysis during vendor security incidents.

**Triggers:**
- Security assessment due date within 30 days
- External threat intelligence feed reports vulnerability affecting a tracked vendor
- Vendor performance score drops below 3.0 in any quarter
- New vendor onboarding request
- Manual trigger: "Assess exposure to [vendor name] security incident"

**Actions:**
- Generate and send security assessment questionnaires to vendors with pre-populated context
- Track questionnaire responses and flag overdue vendors with escalating reminders
- When a vendor security incident is reported, instantly map all applications, systems, and facilities using that vendor's products
- Generate exposure report: "Vendor X is used in 12 applications across 3 facilities. 4 applications are Tier-1 Critical. Recommended actions: [specific steps]"
- Compile quarterly vendor risk report for CISO with trend analysis
- Flag concentration risk: "60% of OT infrastructure depends on Vendor Y — recommend diversification assessment"

**Data Required:**
- Vendor Registry with all vendor-to-application mappings
- Application Portfolio board (connected)
- Threat intelligence feed integration (Recorded Future, Mandiant, or industry ISACs)
- Security assessment questionnaires and responses
- Contract and financial data

**Autonomy Level:** Escalation-Based
Assessment scheduling, reminder generation, and exposure mapping are autonomous. Risk rating changes are recommended but require security team validation. Vendor communication (sending questionnaires, requesting remediation) is autonomous for standard processes. Incident-triggered exposure reports are generated autonomously and sent to CISO and relevant application owners.

**Example Interaction:**
> At 9:15 AM, the Vendor Risk Sentinel receives an alert from the Electricity ISAC (E-ISAC): a critical vulnerability has been disclosed in Schneider Electric's EcoStruxure platform affecting versions 3.1 through 3.4. The agent immediately queries the Vendor Registry and Application Portfolio: Schneider Electric is a Tier-1 Critical vendor with products deployed across 4 facilities.
>
> Within 2 minutes, the agent generates an exposure report: "Schneider Electric EcoStruxure vulnerability (CVE-2026-XXXX) — Your exposure: 4 facilities (Refinery A, Refinery B, Gas Plant Alpha, Substation 7). Version 3.2 confirmed at Refinery A and Gas Plant Alpha (CRITICAL — in vulnerable range). Version 3.5 at Refinery B and Substation 7 (NOT affected). Recommended actions: (1) Engage Schneider Electric account team for patch timeline, (2) Implement compensating controls per vendor advisory at Refinery A and Gas Plant Alpha, (3) Verify network segmentation isolates affected systems per NERC CIP requirements." The report is sent to the CISO, OT Security lead, and facility IT managers simultaneously with a remediation tracking board auto-created.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| SCADA | Supervisory Control and Data Acquisition — systems that monitor and control industrial processes remotely |
| DCS | Distributed Control System — process control system used in refineries, power plants, and chemical facilities |
| PI Historian (OSIsoft) | Time-series database that stores operational data from sensors, now owned by AVEVA |
| NERC CIP | North American Electric Reliability Corporation Critical Infrastructure Protection — mandatory cybersecurity standards for bulk electric system |
| OT | Operational Technology — hardware and software that monitors/controls physical processes (distinct from IT) |
| IT/OT Convergence | Integration of information technology and operational technology networks and processes |
| Purdue Model (ISA-95) | Reference architecture defining levels of IT/OT integration from physical process (Level 0) to enterprise (Level 5) |
| BES Cyber System | Bulk Electric System Cyber System — NERC CIP term for cyber assets critical to grid reliability |
| HMI | Human-Machine Interface — operator screens for monitoring and controlling industrial processes |
| EPC | Engineering, Procurement, and Construction — the contract model for building energy facilities |
| CMMS | Computerized Maintenance Management System (e.g., IBM Maximo, SAP PM) |
| E-ISAC | Electricity Information Sharing and Analysis Center — industry cybersecurity threat intelligence sharing |
| TSA SD | Transportation Security Administration Security Directives — mandatory cybersecurity requirements for pipeline operators |
| Digital Oilfield | Technology-driven approach to upstream oil & gas operations using sensors, analytics, and remote monitoring |
| Modbus / DNP3 / OPC | Legacy industrial communication protocols used in OT environments |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CIO / VP of IT | Overall IT strategy, budget, and digital transformation agenda | Decision-maker |
| Director of OT/ICS Security | Cybersecurity for operational technology environments | Decision-maker (OT) |
| IT Infrastructure Director | Data centers, networking, cloud, and compute infrastructure | Decision-maker (infra) |
| CISO | Enterprise cybersecurity strategy and compliance | Decision-maker (security) |
| IT PMO Director | Portfolio management for IT projects and capital project IT delivery | Influencer |
| Enterprise Architecture Lead | Application portfolio strategy and technology standards | Influencer |
| OT Engineering Manager | Day-to-day OT system operations and maintenance | Influencer (OT adoption) |
| IT Service Delivery Manager | Help desk operations, SLAs, and user satisfaction | User/Influencer |
| IT Procurement Manager | Vendor contracts, licensing, and procurement processes | Influencer (vendor) |
| Plant/Facility IT Lead | On-site IT/OT support at specific facilities | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations / Engineering | IT provides the technology backbone for all operational systems; closest IT/OT integration point | Operations-side work management, maintenance planning, digital twin program management |
| HSE (Health, Safety & Environment) | Safety systems, environmental monitoring, and compliance reporting depend on IT infrastructure | Incident management, compliance tracking, safety observation workflows |
| Finance / Accounting | IT supports financial systems, trading platforms, and regulatory financial reporting (SOX, FERC) | Financial close management, audit workflows, trading operations dashboards |
| Procurement / Supply Chain | IT manages procurement systems and vendor integrations; natural partner for vendor risk management | Procurement workflows, supplier management, inventory optimization |
| Legal / Regulatory | Compliance requirements drive many IT projects (NERC CIP, TSA, SOX); legal manages vendor contracts | Contract lifecycle management, regulatory change tracking |
| HR | IT provisions access, manages identity systems, and supports workforce technology | Employee onboarding/offboarding workflows, training tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow | ITSM + GRC + CMDB — dominant in enterprise energy IT | Complex, expensive ($500K–$2M+/year), over-engineered for many use cases. Win on speed-to-value, usability, and total cost for teams that need project management + service management without ServiceNow's complexity |
| Jira / Atlassian | Dev/engineering task management — used by OT engineering teams | Strong in sprint-based development but weak in cross-functional program management, executive visibility, and non-technical user adoption. Win for IT/OT convergence programs that span engineering and business |
| Primavera P6 (Oracle) | Enterprise project scheduling — dominant for capital projects | Excellent for CPM scheduling but terrible for collaboration, real-time status, and non-PM users. Position monday.com as the collaboration layer that connects to P6 schedules |
| Archer (RSA/Mastercard) | GRC platform for compliance and risk management | Expensive, implementation-heavy, and often requires dedicated administrators. Win for compliance teams that want usable, configurable compliance tracking without 6-month implementation cycles |
| Microsoft Project / Planner | Basic project management in Microsoft ecosystem | Limited portfolio visibility, weak automation, no service management. Win on unified platform (projects + service + dashboards) and superior automation |
| Spreadsheets (Excel/SharePoint) | The actual incumbent in most energy IT organizations | The real competitor. 70%+ of energy IT tracking happens in spreadsheets. Win by demonstrating the cost of spreadsheet chaos: version conflicts, no automation, no real-time visibility, audit risk |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have ServiceNow for ITSM" | "ServiceNow is great for incident/change management. But how are you managing the projects, programs, and cross-functional initiatives that IT delivers? Most ServiceNow customers still use spreadsheets for project management and capital project IT delivery. monday.com fills that gap and can integrate with ServiceNow for ticket data." |
| "Our OT team won't use another IT tool" | "That's exactly the problem we solve. OT engineers resist tools designed for IT because they feel foreign. monday.com's flexibility means you can create OT-friendly views with their terminology, their workflows, their priorities—while giving IT leadership the visibility they need. It meets OT where they are." |
| "We're in a regulated industry—can monday.com handle compliance?" | "Absolutely. monday.com provides SOC 2 Type II certification, HIPAA compliance capabilities, and enterprise-grade security. For NERC CIP evidence management, the platform's structured data, file attachments, audit trails, and automated workflows actually improve compliance posture compared to spreadsheets and shared drives—which auditors increasingly flag as control weaknesses." |
| "We need on-premises deployment for OT data" | "We understand the sensitivity around OT data. monday.com operates in the cloud with enterprise security controls, but the key insight is that your IT management workflows (project tracking, compliance evidence, vendor management) don't contain OT control data—they contain metadata about OT projects. The actual SCADA configurations and control logic stay in your OT systems. monday.com manages the work around those systems, not the systems themselves." |
| "The pricing doesn't work for our scale" | "Let's look at it through the lens of what you're spending today: ServiceNow licensing, Archer GRC, Primavera licenses, plus the hidden cost of thousands of hours managing spreadsheets. When you consolidate project management, compliance tracking, and vendor management onto one platform, the total cost of ownership often decreases even before accounting for productivity gains." |

## Proof Points
*(To be populated with customer references)*
- Energy sector customers using monday.com for IT project management
- Utility companies managing compliance workflows
- Oil & gas companies tracking capital project IT delivery
- [Placeholder for specific customer stories and metrics]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
