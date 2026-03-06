# Banking × IT Playbook

## Overview

IT departments in banking institutions operate under some of the most demanding conditions in any industry. They must balance relentless innovation pressure — mobile banking, real-time payments, open banking APIs — against an extraordinarily complex regulatory environment (OCC, FDIC, Federal Reserve, FFIEC, PCI-DSS, SOX, GDPR, DORA). A mid-size bank's IT org typically runs 500–2,000+ applications, manages thousands of endpoints, and supports critical systems with 99.99% uptime SLAs where minutes of downtime translate to millions in lost transactions and reputational damage.

Banking IT teams are typically structured around infrastructure and operations (network, cloud, data centers), application development and maintenance (core banking, digital channels), cybersecurity and risk, data management and analytics, enterprise architecture, and IT governance/compliance. Headcounts range from 200–500 at regional banks to 10,000–50,000+ at global institutions. The CIO or CTO reports to the CEO or COO, with dotted-line accountability to the Chief Risk Officer for technology risk. Budget allocation skews heavily toward "keep the lights on" (60–70%) with the remainder for strategic initiatives — a ratio the C-suite is desperate to invert.

The defining tension in banking IT is the dual mandate: innovate at fintech speed while maintaining the stability and compliance posture of a century-old institution. Legacy core banking systems (often mainframe-based COBOL), technical debt, siloed data, and an aging workforce compound the challenge. Every project requires security review, risk assessment, and regulatory sign-off — processes that can add weeks or months to delivery timelines. monday.com's value proposition centers on making this complexity visible, manageable, and increasingly automated.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Banks run dozens of overlapping ITSM, project management, and governance tools; consolidation reduces license costs, audit surface, and integration maintenance |
| 2 | Scale Impact Without Overhead | High | IT headcount is capped while demand for digital services grows 20-30% annually; automation and self-service are the only path to scale |
| 3 | Replace or Radically Augment Headcount | Medium-High | Tier-1 support, change management coordination, compliance documentation, and vendor management consume significant FTEs that AI can augment |

## Prioritized Use Cases

---

### Use Case 1: IT Change Management & CAB Governance

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banks process thousands of change requests monthly — infrastructure patches, application releases, configuration updates, database changes. Each requires risk classification (Standard, Normal, Emergency), impact assessment, CAB (Change Advisory Board) review, and post-implementation verification. Most banks cobble together ServiceNow or BMC Remedy for ticketing, SharePoint for documentation, Excel for the change calendar, and email chains for approvals. Changes slip through cracks, conflicts between changes cause outages, and auditors find gaps in the approval trail. A single failed change in production can trigger regulatory scrutiny and cost millions.

#### The Solution
monday.com Work Management as the unified change management platform. A master **Change Request Board** with columns for: Change ID (auto-number), Requester (people), Change Type (dropdown: Standard/Normal/Emergency/Expedited), Risk Level (status: Low/Medium/High/Critical), Affected Systems (dropdown linked to CMDB board), Implementation Window (timeline), Rollback Plan (long text), CAB Decision (status: Pending/Approved/Rejected/Deferred), and Implementer (people). Connected boards link to the **CMDB Asset Registry**, **Incident Board** (for change-related incidents), and **Release Calendar** (timeline view showing all scheduled changes). Automations enforce governance: High/Critical changes auto-notify CAB members and block implementation until approval status is set; Emergency changes trigger immediate Slack/Teams alerts to on-call managers; post-implementation reviews auto-create after 48 hours.

#### The Outcome
40–60% reduction in change-related incidents through conflict detection and proper governance. CAB meeting prep time cut from 4 hours to 30 minutes with dashboard views. Complete audit trail satisfying OCC/FFIEC examination requirements. Mean time from change request to implementation reduced by 35%.

#### Discovery Questions
- How many change requests does your CAB review per week, and what percentage are emergency changes?
- When was the last time a change conflict caused a production incident, and what was the blast radius?
- How do your examiners currently assess your change management controls during audits?
- What's the average elapsed time from change request submission to production deployment?
- How many tools are involved in your end-to-end change management process today?

#### Industry Context
Banking regulators (OCC, FDIC, Federal Reserve) specifically examine IT change management controls under FFIEC IT Examination Handbook guidelines. Failed changes that impact customer-facing systems may trigger Matters Requiring Attention (MRAs) or Matters Requiring Immediate Attention (MRIAs). SOX Section 404 requires documented controls over changes to financially significant systems. The CAB is not optional — it's a regulatory expectation for material changes.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Change Management system for a bank. Create a main board called 'Change Requests' with these columns: Change ID (auto-number), Title (text), Requester (people), Change Type (dropdown: Standard, Normal, Emergency, Expedited), Risk Level (status with colors: Low=green, Medium=yellow, High=orange, Critical=red), Affected Systems (dropdown: Core Banking, Digital Channels, Payment Processing, Data Warehouse, Network Infrastructure, ATM/Branch Systems, Fraud Detection, CRM), Implementation Window (timeline), Rollback Plan (long text), Testing Evidence (files), CAB Decision (status: Pending Review=grey, Approved=green, Rejected=red, Deferred=yellow), Implementer (people), Post-Implementation Status (status: Not Started, Verified OK, Issues Found, Rollback Executed). Add automations: when Risk Level is Critical or High, notify the group 'CAB Members'; when CAB Decision is Approved, move to 'Approved Changes' group; when Implementation Window end date passes, create an item in a connected 'Post-Implementation Reviews' board. Create views: a Timeline view called 'Change Calendar' grouped by Affected Systems, a Dashboard with widgets showing changes by risk level, approval rate, and change volume trends, and a Kanban view by CAB Decision status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ChangeGuard
**Agent Purpose:** Automatically assess change risk, detect scheduling conflicts, and prepare CAB briefing packages.

**Triggers:**
- New change request item created
- Implementation Window dates modified
- Risk Level changed to High or Critical
- Every Monday at 8 AM (weekly CAB prep)
- Emergency change type selected

**Actions:**
- Analyze change description and affected systems to auto-suggest Risk Level based on historical incident correlation
- Scan all approved/pending changes for implementation window overlaps on the same systems and flag conflicts
- Generate CAB briefing document summarizing all pending changes with risk assessment, system dependencies, and rollback plans
- Auto-classify Standard changes that match pre-approved templates and route for auto-approval
- Notify on-call manager and CISO immediately for Emergency changes with full context summary
- Create post-implementation review items with pre-populated checklists 48 hours after implementation window closes

**Data Required:**
- Change request history (past 12 months for pattern analysis)
- CMDB/asset registry for system dependency mapping
- Incident board for change-failure correlation
- On-call rotation schedule
- Pre-approved standard change templates

**Autonomy Level:** Human-in-the-Loop
Standard changes matching pre-approved templates can be auto-approved. All Normal, Emergency, and High/Critical changes require human CAB approval. Agent prepares recommendations and briefings but never approves material changes autonomously.

**Example Interaction:**
> On Monday morning, ChangeGuard scans the 23 pending change requests for the upcoming week. It identifies that CR-2847 (core banking database migration) and CR-2851 (payment gateway SSL certificate rotation) are both scheduled for Wednesday's maintenance window and both affect the payment processing subsystem. ChangeGuard flags the conflict, recommends separating the changes to different windows, and drafts an alternative schedule. It also notes that CR-2849 (branch network firmware update) matches the pre-approved standard template ST-012 and auto-approves it with documentation. The weekly CAB briefing package is generated with risk heat maps, dependency diagrams, and historical success rates for similar changes — ready for the 10 AM CAB meeting.

---

### Use Case 2: Application Portfolio Rationalization & Technical Debt Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
A typical mid-size bank runs 800–1,500 applications, many of which overlap in functionality, run on unsupported platforms, or serve a dwindling user base. The CIO knows 30–40% of the portfolio could be decommissioned or consolidated, but nobody has a clear picture of what each application does, who owns it, what it costs, or what depends on it. Application portfolio data lives in scattered spreadsheets, outdated CMDB entries, and tribal knowledge. Meanwhile, annual software licensing costs run $50M–$200M+, and every redundant application increases the attack surface and compliance burden. Regulators increasingly ask about technology obsolescence risk and third-party concentration risk.

#### The Solution
monday.com as the **Application Portfolio Management (APM)** platform. A master **Application Registry Board** with columns: Application Name (text), App ID (auto-number), Business Owner (people), Technical Owner (people), Vendor (dropdown), Annual Cost (numbers with currency), User Count (numbers), Business Criticality (status: Mission Critical/Important/Standard/Low), Technology Stack (tags: Java, .NET, COBOL, Python, Cloud-Native, On-Prem), End-of-Support Date (date), Risk Score (formula combining criticality + age + support status), Rationalization Decision (status: Retain/Invest, Migrate, Replace, Retire, Tolerate), and Target Retirement Date (date). Connected boards for **Integration Dependencies** (showing which apps talk to which), **Vendor Contracts**, and **Migration Projects**. Dashboard views with portfolio heat maps by risk score, cost distribution charts, technology stack distribution, and retirement pipeline timeline.

#### The Outcome
Identification of 25–35% of applications as candidates for retirement or consolidation. Projected annual savings of $5M–$30M in licensing, infrastructure, and support costs. Reduced audit findings related to unsupported technology. Clear roadmap for modernization aligned to business priorities.

#### Discovery Questions
- How many applications are in your portfolio today, and how confident are you in that number?
- What percentage of your applications run on platforms that are end-of-life or approaching end-of-support?
- When was the last time a regulator asked about your technology obsolescence strategy?
- How do you currently track application interdependencies, and has a surprise dependency ever caused a project delay?
- What's your annual software licensing spend, and how much do you estimate is redundant?

#### Industry Context
The FFIEC IT Examination Handbook requires banks to maintain inventories of information assets and manage technology lifecycle risk. OCC Heightened Standards (12 CFR Part 30, Appendix D) require large banks to have comprehensive technology risk management programs. Application rationalization directly impacts Third-Party Risk Management (TPRM) programs since every application with a vendor creates a third-party relationship requiring ongoing due diligence. Core banking system modernization (moving off mainframe COBOL to cloud-native architectures) is a $1B+ multi-year initiative at large banks.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Application Portfolio Management system for a bank. Create a board called 'Application Registry' with columns: App Name (text), App ID (auto-number), Business Owner (people), Technical Owner (people), Vendor (text), Annual License Cost (numbers, currency USD), Infrastructure Cost (numbers, currency USD), Total Cost (formula: Annual License + Infrastructure), Active Users (numbers), Business Criticality (status: Mission Critical=red, Important=orange, Standard=yellow, Low=green), Tech Stack (tags), Deployment Model (dropdown: On-Premise, Private Cloud, Public Cloud, Hybrid, SaaS), Go-Live Date (date), End-of-Support Date (date), Rationalization Decision (status: Retain & Invest=dark green, Migrate=blue, Replace=purple, Retire=red, Tolerate=grey), Target Retirement Date (date), Regulatory Classification (dropdown: SOX In-Scope, PCI In-Scope, Privacy Critical, Standard). Create groups: Mission Critical Apps, Business Applications, Infrastructure Tools, Legacy/Retirement Pipeline. Add a Timeline view called 'Retirement Roadmap' showing Target Retirement Dates, a Chart view showing Total Cost by Rationalization Decision, and a Dashboard with widgets for total portfolio cost, apps by criticality, technology stack distribution pie chart, and apps approaching end-of-support (filtered by End-of-Support Date within next 12 months)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PortfolioAnalyst
**Agent Purpose:** Continuously analyze the application portfolio for rationalization opportunities, risk signals, and cost optimization.

**Triggers:**
- New application added to registry
- End-of-Support Date within 180 days
- Quarterly portfolio review schedule (first Monday of each quarter)
- Annual Cost updated above threshold ($500K)
- Active Users drops below 10

**Actions:**
- Score each application on a composite risk index (criticality × age × support status × dependency count) and flag high-risk items
- Identify functional overlaps by analyzing application descriptions and tag patterns, recommending consolidation candidates
- Generate quarterly portfolio health report with cost trends, risk distribution, and rationalization progress
- Alert Technical and Business Owners when End-of-Support dates approach with recommended actions
- Flag applications with declining user counts as retirement candidates with cost-savings projections
- Create migration project items automatically when Rationalization Decision changes to Migrate or Replace

**Data Required:**
- Application registry with complete metadata
- Integration/dependency mapping between applications
- Vendor contract renewal dates and terms
- Historical user count trends
- Infrastructure cost allocation data

**Autonomy Level:** Escalation-Based
Agent performs analysis and generates recommendations autonomously. Rationalization decisions require Architecture Review Board approval. Retirement actions require Business Owner sign-off. Agent auto-creates alerts and reports but never decommissions or modifies applications.

**Example Interaction:**
> During the Q1 portfolio review, PortfolioAnalyst identifies that three separate document management systems (FileNet, Documentum, and a legacy SharePoint 2013 instance) serve overlapping functions across retail banking, commercial lending, and compliance. Combined annual cost: $2.8M. User analysis shows the SharePoint instance has only 12 active users, down from 340 three years ago. The agent recommends consolidating to FileNet (highest criticality rating, deepest integration with core banking), retiring SharePoint immediately (saving $180K/year), and planning a Documentum-to-FileNet migration over 18 months (projected savings: $1.1M/year post-migration). It generates a summary for the Architecture Review Board with cost-benefit analysis and creates draft migration project items.

---

### Use Case 3: Cybersecurity Incident Response & Threat Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banks are the #1 target for cyberattacks. The average financial institution faces 700+ attempted intrusions per day, and the cost of a data breach in financial services averages $5.9M (IBM 2025). The Security Operations Center (SOC) is drowning in alerts — 90%+ are false positives, but the one that's real could be catastrophic. Incident response processes involve coordination across IT operations, information security, legal, compliance, communications, and executive management. Most banks track incidents in a mix of SIEM tools, ticketing systems, email threads, and (horrifyingly) spreadsheets. When regulators ask for incident response metrics or evidence of tabletop exercises, the team scrambles to compile data from multiple sources.

#### The Solution
monday.com as the **Security Incident Management** coordination layer (not replacing the SIEM, but orchestrating the response). A **Security Incidents Board** with: Incident ID (auto-number), Severity (status: SEV-1 Critical/SEV-2 High/SEV-3 Medium/SEV-4 Low), Category (dropdown: Malware, Phishing, DDoS, Data Exfiltration, Insider Threat, Ransomware, Third-Party Breach, Unauthorized Access), Detection Source (dropdown: SIEM, SOC Analyst, User Report, Automated Scan, Regulatory Alert, Third-Party Notification), Affected Systems (connected to CMDB board), Incident Commander (people), Status (status: Detected, Triaged, Contained, Eradicated, Recovered, Lessons Learned, Closed), Customer Impact (status: None/Limited/Significant/Severe), Regulatory Notification Required (checkbox), Timeline (timeline for incident lifecycle), and Resolution Notes (long text). Connected **Incident Response Playbook Board** with step-by-step procedures for each incident category. Dashboard showing MTTR (Mean Time to Resolve), incidents by category trends, open incidents by severity, and SLA compliance.

#### The Outcome
30% improvement in Mean Time to Detect (MTTD) through structured triage workflows. 45% improvement in MTTR through automated playbook activation and coordination. Complete incident documentation satisfying FFIEC, NYDFS 23 NYCRR 500, and GDPR Article 33 notification requirements. Regulatory examination readiness with real-time incident metrics.

#### Discovery Questions
- What's your current Mean Time to Detect and Mean Time to Resolve for security incidents?
- How do you coordinate response across SOC, IT ops, legal, and communications during a SEV-1 incident?
- When was your last regulatory examination of incident response capabilities, and what feedback did you receive?
- How do you track and enforce SLAs for incident response at different severity levels?
- What's your process for conducting and documenting post-incident reviews?

#### Industry Context
NYDFS 23 NYCRR 500 requires covered entities to notify the superintendent within 72 hours of a cybersecurity event. GDPR requires notification within 72 hours for data involving EU customers. The Federal Reserve's SR 05-23 and OCC Bulletin 2005-35 establish expectations for incident response programs. Banks must also comply with FinCEN SAR filing requirements if incidents involve suspected fraud. The FFIEC Cybersecurity Assessment Tool (CAT) specifically evaluates incident response maturity across five domains.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Incident Response tracker for a bank. Create a board called 'Security Incidents' with columns: Incident ID (auto-number, prefix 'INC-'), Title (text), Severity (status: SEV-1 Critical=red, SEV-2 High=orange, SEV-3 Medium=yellow, SEV-4 Low=green), Category (dropdown: Malware, Phishing, DDoS, Data Exfiltration, Insider Threat, Ransomware, Unauthorized Access, Third-Party Breach), Detection Time (date), Containment Time (date), Resolution Time (date), Incident Commander (people), Status (status: Detected=light blue, Triaged=blue, Contained=orange, Eradicated=purple, Recovered=green, Lessons Learned=grey, Closed=dark green), Customer Data Impacted (checkbox), Regulatory Notification Required (checkbox), Notification Deadline (date, formula: Detection Time + 72 hours), Systems Affected (tags), Root Cause (long text), Lessons Learned (long text). Create groups: Active Incidents, Under Investigation, Resolved This Month, Closed. Add automations: when Severity is SEV-1 Critical, notify group 'CISO Team' and group 'Executive Leadership'; when Customer Data Impacted is checked, set Regulatory Notification Required to checked and calculate Notification Deadline. Create a Dashboard with: open incidents by severity chart, MTTR trend over 12 months, incidents by category pie chart, and a number widget showing 'Days Since Last SEV-1'."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CyberResponder
**Agent Purpose:** Orchestrate incident response by activating playbooks, coordinating response teams, tracking SLAs, and generating regulatory notifications.

**Triggers:**
- New incident created with SEV-1 or SEV-2 severity
- Containment SLA approaching (severity-based thresholds)
- Regulatory Notification Deadline within 24 hours and notification not sent
- Incident status unchanged for more than defined escalation period
- Weekly summary schedule (every Friday at 4 PM)

**Actions:**
- Activate the appropriate response playbook based on incident category, creating checklist items for each response step
- Assign Incident Commander based on rotation schedule and category expertise
- Escalate to CISO and executive team for SEV-1 with pre-formatted situation report
- Draft regulatory notification letters (NYDFS, OCC, FDIC) with incident details pre-populated
- Generate weekly incident summary report with MTTD, MTTR, trend analysis, and open items
- Create post-incident review items with pre-populated timeline and invite relevant stakeholders

**Data Required:**
- Incident response playbooks by category
- On-call rotation and escalation paths
- Regulatory notification templates and requirements by jurisdiction
- Historical incident data for trend analysis
- System/asset inventory for impact assessment

**Autonomy Level:** Human-in-the-Loop
Agent activates playbooks and drafts notifications autonomously. All regulatory notifications require CISO or CLO approval before sending. Containment and eradication actions require human execution. Agent manages coordination and documentation, not technical remediation.

**Example Interaction:**
> At 2:47 AM, a new SEV-1 incident is created: "Suspicious lateral movement detected in commercial lending subnet." CyberResponder immediately activates the Unauthorized Access playbook, creating 14 response steps as checklist items. It assigns Sarah Chen as Incident Commander (she's on-call this week and has unauthorized access expertise). Within 30 seconds, the CISO and CTO receive a formatted situation report via Slack and SMS. The agent identifies three critical systems in the affected subnet (commercial loan origination, credit decisioning engine, and customer document repository) and flags that customer PII may be at risk — setting Regulatory Notification Required to true and calculating the 72-hour NYDFS deadline. Every 2 hours, it generates a status update compiling actions taken from the checklist, keeping the executive team informed without requiring the Incident Commander to pause response work to write reports.

---

### Use Case 4: IT Vendor & Third-Party Risk Management (TPRM)

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banks typically manage 3,000–10,000+ third-party vendor relationships, of which 200–500 are considered "critical" or "significant" based on data access, operational dependency, or financial materiality. OCC Bulletin 2013-29 and Federal Reserve SR 13-19 require banks to manage third-party risk through the full lifecycle: planning, due diligence, contract negotiation, ongoing monitoring, and termination. Each critical vendor requires annual risk assessments, SOC 2 report reviews, business continuity plan evaluation, financial health monitoring, and performance reviews. TPRM teams of 5–15 people are buried under manual questionnaires, chasing vendors for documents, and struggling to maintain accurate records. When examiners arrive, producing evidence of comprehensive vendor oversight takes weeks of preparation.

#### The Solution
monday.com as the **Third-Party Risk Management** platform. A **Vendor Registry Board** with: Vendor Name, Vendor ID (auto-number), Criticality Tier (status: Critical/Significant/Limited/Minimal), Services Provided (tags), Data Access Level (dropdown: Customer PII, Financial Data, No Sensitive Data, System Access Only), Contract Value (numbers), Contract Expiration (date), Primary Contact (text), Bank Relationship Owner (people), Risk Rating (status: Low/Medium/High/Critical), Last Assessment Date (date), Next Assessment Due (date formula), SOC 2 Report Status (status: Current/Expiring Soon/Expired/Not Applicable), and Concentration Risk Flag (checkbox). Connected boards: **Risk Assessments** (one per vendor per assessment cycle), **Contract Repository**, **Issue Tracking** (findings and remediation), and **Fourth-Party Mapping** (sub-contractors of critical vendors). Automations: SOC 2 expiring within 60 days → notify relationship owner; assessment overdue → escalate to TPRM manager; contract expiring within 90 days → trigger renewal workflow.

#### The Outcome
50% reduction in TPRM team effort through automated tracking and notifications. 100% on-time completion of critical vendor assessments (vs. typical 60–75%). Examination-ready vendor oversight documentation at all times. Identification of concentration risk and fourth-party dependencies previously invisible.

#### Discovery Questions
- How many third-party vendors do you manage, and how do you classify them by risk tier?
- What's your on-time completion rate for annual vendor risk assessments?
- How do you currently track fourth-party risk (your vendors' critical sub-contractors)?
- What was your last regulatory finding related to third-party risk management?
- How long does it take to compile vendor oversight documentation for an examination?

#### Industry Context
OCC Bulletin 2013-29 (updated 2023) is the foundational guidance for bank TPRM programs. The Interagency Guidance on Third-Party Relationships (June 2023) from OCC, Federal Reserve, and FDIC unified expectations. Banks must assess operational risk, compliance risk, strategic risk, reputation risk, credit risk, and information security risk for each critical vendor. The concept of "concentration risk" — over-reliance on a single vendor or a few vendors in a service category — is under increasing regulatory scrutiny, especially for cloud services (AWS, Azure, GCP). Fourth-party risk (what happens if your vendor's critical vendor fails?) is the emerging frontier.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Third-Party Risk Management system for a bank. Create a board called 'Vendor Registry' with columns: Vendor Name (text), Vendor ID (auto-number, prefix 'VND-'), Criticality Tier (status: Critical=red, Significant=orange, Limited=yellow, Minimal=green), Services (tags: Cloud Infrastructure, Core Banking, Payment Processing, Data Analytics, Cybersecurity, Document Management, HR Systems, Marketing Tech), Data Access Level (dropdown: Customer PII, Financial Records, System-Level Access, No Sensitive Data), Annual Contract Value (numbers, currency USD), Contract Start (date), Contract End (date), Relationship Owner (people), TPRM Analyst (people), Overall Risk Rating (status: Critical=red, High=orange, Medium=yellow, Low=green), Last Assessment Date (date), Next Assessment Due (date), SOC 2 Expiry (date), Business Continuity Plan Reviewed (checkbox), Financial Health Score (numbers 1-100). Create groups by Criticality Tier. Add automations: when SOC 2 Expiry is within 60 days, notify Relationship Owner; when Next Assessment Due is today, create item in connected 'Risk Assessments' board; when Contract End is within 90 days, notify group 'Procurement'. Create a Dashboard with: vendors by criticality tier, total contract value by tier, overdue assessments count, SOC 2 expiration timeline, and a risk rating distribution chart."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorWatch
**Agent Purpose:** Proactively monitor vendor risk signals, automate assessment workflows, and maintain examination-ready TPRM documentation.

**Triggers:**
- Next Assessment Due date reached
- SOC 2 report expiry within 90 days
- Contract renewal window opens (90 days before expiration)
- New critical/significant vendor added
- Quarterly concentration risk review schedule

**Actions:**
- Generate pre-populated risk assessment questionnaires based on vendor tier and services, pulling forward prior year responses for comparison
- Monitor vendor financial health signals (credit ratings, news) and update Financial Health Score with alerts for deterioration
- Produce quarterly TPRM dashboard reports formatted for board of directors and regulatory examination readiness
- Identify concentration risk by analyzing service category dependencies and flagging single-vendor categories
- Auto-escalate overdue assessments through management chain with days-overdue and regulatory risk context
- Map fourth-party relationships by analyzing vendor SOC 2 reports and sub-contractor disclosures

**Data Required:**
- Vendor registry with complete profiles
- Historical risk assessments and findings
- Contract terms and renewal dates
- SOC 2 and compliance report repository
- Industry news feeds for vendor monitoring

**Autonomy Level:** Escalation-Based
Agent autonomously generates assessments, monitors signals, and produces reports. Vendor risk rating changes require TPRM analyst review. Contract decisions and vendor terminations require VP-level approval. Agent flags but never makes vendor continuation/termination decisions.

**Example Interaction:**
> VendorWatch detects that CriticalPay Systems (a Tier 1 payment processor handling 40% of the bank's ACH volume) has been downgraded by Moody's from Baa2 to Baa3. The agent immediately updates the Financial Health Score from 72 to 54, changes the risk flag to High, and generates an alert to the TPRM Director and the VP of Payments. It also identifies that no alternative payment processor is currently onboarded — a concentration risk it highlights in a brief that includes the regulatory expectation (OCC 2013-29 Section III.C.3), the potential business impact of a processor failure, and a recommendation to accelerate the secondary processor onboarding project that's been sitting in backlog for six months. The brief is formatted for immediate inclusion in the next Risk Committee meeting.

---

### Use Case 5: IT Project Portfolio & Resource Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking IT departments juggle 50–200+ concurrent projects across digital transformation, regulatory mandates, infrastructure upgrades, and business-requested enhancements. Resource allocation is a constant battle — the same senior architects and DBAs are requested on every critical project. Project status reporting consumes 15–20% of project managers' time as they aggregate data from Jira (dev work), ServiceNow (infrastructure), Excel (budgets), and PowerPoint (executive updates). Dependencies between projects are poorly tracked, leading to cascading delays when one project slips. Regulatory-mandated projects (CECL implementation, AML system upgrades, DORA compliance) must be prioritized regardless of capacity, squeezing discretionary innovation projects.

#### The Solution
monday.com as the **IT Portfolio Management Office (PMO)** platform. A **Project Portfolio Board** with: Project Name, Project ID (auto-number), Sponsor (people), Project Manager (people), Category (dropdown: Regulatory/Mandatory, Digital Transformation, Infrastructure, Business Enhancement, Security, Innovation), Status (status: Proposed, In Planning, In Flight, On Hold, Completed, Cancelled), Health (status: Green/Yellow/Red), Budget Allocated (numbers), Budget Spent (numbers), Budget Variance (formula), Start Date (date), Target End Date (date), Resource FTEs Required (numbers), Strategic Alignment (dropdown: Revenue Growth, Cost Reduction, Risk Mitigation, Customer Experience, Regulatory Compliance). Connected boards for **Resource Allocation** (people × project matrix), **Project Milestones**, **Risks & Issues**, and **Dependencies** (project-to-project links). Executive Dashboard showing portfolio health distribution, budget utilization, resource utilization heat map, and regulatory vs. discretionary project balance.

#### The Outcome
Real-time portfolio visibility replacing weekly manual status aggregation. 25% improvement in resource utilization through conflict detection and capacity planning. 90%+ on-time delivery for regulatory-mandated projects. Executive decision-making accelerated with always-current dashboards instead of stale monthly reports.

#### Discovery Questions
- How many active IT projects do you have right now, and how many project managers support them?
- What percentage of your project portfolio is regulatory-mandated vs. discretionary?
- How do you currently identify and manage resource conflicts across projects?
- When was the last time a project dependency caused a significant delay, and how was it discovered?
- How long does it take to produce your monthly IT steering committee portfolio report?

#### Industry Context
Banking IT portfolios are unique because regulatory-mandated projects are non-negotiable and often come with hard deadlines (e.g., CECL by adoption date, LIBOR transition by cessation date, DORA compliance by January 2025). The OCC expects banks to demonstrate that IT strategy aligns with overall business strategy and that resource allocation reflects risk priorities. Large banks typically have a formal IT Governance Committee or Technology Steering Committee that reviews portfolio prioritization quarterly. The tension between "must do" regulatory work and "want to do" innovation work is the central portfolio management challenge.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Project Portfolio Management system for a bank. Create a board called 'IT Project Portfolio' with columns: Project Name (text), Project ID (auto-number, prefix 'PRJ-'), Executive Sponsor (people), Project Manager (people), Category (dropdown: Regulatory Mandate, Digital Transformation, Infrastructure Modernization, Security Enhancement, Business Request, Innovation Lab), Status (status: Proposed=grey, Planning=light blue, In Flight=blue, On Hold=orange, Completed=green, Cancelled=red), Health (status: On Track=green, At Risk=yellow, Off Track=red), Approved Budget (numbers, currency USD), Actual Spend (numbers, currency USD), Variance % (formula), Start Date (date), Target Completion (date), FTEs Allocated (numbers), Strategic Priority (dropdown: P1 Critical, P2 High, P3 Medium, P4 Low), Dependencies (connect to same board). Create groups: Regulatory & Compliance, Digital & Customer, Infrastructure & Operations, Innovation & Emerging. Add a Timeline view called 'Portfolio Roadmap' colored by Category. Create a Dashboard with: project health distribution pie chart, budget allocated vs spent bar chart by category, resource allocation by category, projects by status, and a table widget showing all Red-status projects with PM and variance."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PortfolioNavigator
**Agent Purpose:** Proactively monitor project health, detect resource conflicts and dependency risks, and generate executive-ready portfolio reports.

**Triggers:**
- Project Health changed to Yellow or Red
- Budget Variance exceeds 10%
- Target Completion date within 30 days and status not near completion
- New project proposed (status = Proposed)
- Bi-weekly executive reporting schedule

**Actions:**
- Analyze resource allocation across all in-flight projects and flag over-allocated individuals (>120% capacity)
- Detect dependency chain risks: if Project A slips and Project B depends on it, alert Project B's PM with impact analysis
- Generate bi-weekly portfolio health report with executive summary, red/yellow project deep-dives, budget forecast, and resource heat map
- Score new project proposals against strategic alignment criteria and current capacity, recommending prioritization
- Forecast portfolio completion timeline using historical velocity data and current status trends
- Alert steering committee when regulatory project deadlines are at risk with mitigation recommendations

**Data Required:**
- All project board data including milestones and dependencies
- Resource allocation matrix
- Historical project delivery data (velocity, budget accuracy)
- Regulatory deadline calendar
- Strategic priority framework

**Autonomy Level:** Escalation-Based
Agent generates reports, detects conflicts, and recommends prioritization autonomously. Project status changes require PM confirmation. Budget reallocation and project prioritization changes require steering committee approval. Agent surfaces risks early but doesn't change project parameters.

**Example Interaction:**
> PortfolioNavigator detects that the DORA Compliance Implementation project (PRJ-089, regulatory mandate, hard deadline June 2026) has three critical-path milestones slipping by 2–3 weeks each. It traces the root cause to two senior architects who are also allocated 80% to the Core Banking Migration (PRJ-072). The agent generates an impact analysis showing that without intervention, PRJ-089 will miss its regulatory deadline by approximately 6 weeks. It proposes three options: (1) temporarily reassign architects from PRJ-072, delaying it by one quarter, (2) engage contract architects at estimated cost $340K, or (3) descope PRJ-072's current phase to free capacity. The analysis is formatted for the Thursday steering committee meeting with cost/risk/timeline implications for each option.

---

### Use Case 6: IT Service Request & Self-Service Portal

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banking IT service desks handle 2,000–10,000+ requests per month: access provisioning, software installations, hardware requests, password resets, VPN issues, branch technology problems, and application support. 60–70% of these are routine, repetitive requests that follow standard procedures but still require a human to process. Tier-1 analysts spend their days on password resets and access requests instead of meaningful work. Mean time to fulfill a standard request is 3–5 days due to approval chains and manual provisioning. New employee onboarding requires 15–25 separate access requests across different systems. Branch managers calling about printer issues wait in the same queue as fraud analysts reporting system anomalies.

#### The Solution
monday.com as a **Service Request Management** platform with WorkForms as the self-service intake layer. **IT Service Request Board** with: Request ID (auto-number), Requester (people), Request Type (dropdown: Access Request, Software Installation, Hardware Request, Password Reset, VPN/Connectivity, Branch Technology, Application Support, New Employee Onboarding), Priority (status: Critical/High/Medium/Low), Category auto-routed to groups: Access Management, Desktop Support, Network & Infrastructure, Applications. WorkForms for common requests with conditional logic (e.g., "Access Request" form asks which system, what level of access, manager approval, business justification). Automations route requests to appropriate teams, auto-assign based on workload balancing, send SLA breach notifications, and create bundled onboarding packages when "New Employee" type is selected (auto-generating 15+ access requests from a template).

#### The Outcome
70% of routine requests fulfilled without Tier-1 human intervention through automated workflows. New employee onboarding time reduced from 5 days to same-day. SLA compliance improved from 72% to 95%. Tier-1 analysts redeployed to higher-value security monitoring and proactive support. Annual cost savings of $500K–$1.5M in service desk labor.

#### Discovery Questions
- What's your monthly service request volume, and what percentage are routine/repetitive?
- How long does it take to fully provision a new employee with all necessary system access?
- What's your current SLA compliance rate for standard service requests?
- How many Tier-1 analysts are dedicated to the service desk, and what's their average handling time?
- Do you have a self-service portal today, and what's the adoption rate?

#### Industry Context
Banking service desks face unique complexity because access provisioning must comply with least-privilege principles, segregation of duties requirements (SOX), and role-based access control (RBAC) frameworks. A teller requesting access to the wire transfer system triggers compliance review. Recertification of access (quarterly or semi-annual) is a regulatory expectation. Branch technology support adds geographic complexity — 500+ locations each with their own equipment. The rise of remote/hybrid work has increased VPN and collaboration tool support requests by 200%+ since 2020.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Service Request system for a bank. Create a board called 'Service Requests' with columns: Ticket ID (auto-number, prefix 'SR-'), Requester Name (people), Request Type (dropdown: Access Request, Software Install, Hardware Request, Password Reset, VPN/Connectivity, Branch Tech Support, Application Issue, New Hire Onboarding, Offboarding), Priority (status: Critical=red, High=orange, Medium=yellow, Low=green), Assigned To (people), Status (status: New=grey, In Progress=blue, Pending Approval=yellow, Fulfilled=green, Rejected=red, Cancelled=grey), SLA Target (date), SLA Status (formula-based or status: Within SLA=green, At Risk=yellow, Breached=red), Manager Approval (status: Pending/Approved/Denied), System Affected (dropdown: Core Banking, Trading Platform, Email, Active Directory, CRM, Branch POS, VPN, Intranet), Resolution Notes (long text). Create groups: New Requests, In Progress, Pending Approval, Completed This Week. Add automations: when Request Type is 'Access Request' and Priority is not Critical, request approval from manager column; when SLA Target is today and Status is not Fulfilled, notify Assigned To and group 'IT Managers'; when Request Type is 'New Hire Onboarding', create subitems for each standard access (email, AD, core banking view-only, VPN, intranet, time tracking). Create a WorkForm called 'IT Help Request' with fields for request type, description, urgency, and system affected."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ServiceBot
**Agent Purpose:** Auto-triage service requests, fulfill routine requests without human intervention, and optimize service desk operations.

**Triggers:**
- New service request submitted via WorkForm
- SLA target approaching (within 2 hours of breach)
- Request status unchanged for more than 24 hours
- New Hire Onboarding request created
- Daily service desk metrics summary (8 AM)

**Actions:**
- Auto-classify and prioritize incoming requests based on content analysis, requester role, and system affected
- Fulfill password reset requests automatically via integration with Active Directory (with identity verification)
- Generate complete onboarding access packages based on role/department templates, pre-populating all required access requests with appropriate approval chains
- Escalate SLA-at-risk tickets to team leads with context and suggested reassignment based on current workload
- Produce daily service desk performance report: volume, resolution rate, SLA compliance, top request categories, and staffing recommendations
- Route branch technology issues to the nearest regional support team based on branch location mapping

**Data Required:**
- Request history for classification training
- Role-based access templates by department and job title
- SLA definitions by request type and priority
- Team member workload and availability
- Branch location and regional support team mapping

**Autonomy Level:** Fully Autonomous (for routine) / Human-in-the-Loop (for access)
Password resets, status updates, and request routing are fully autonomous. Access provisioning requires manager approval (SOX compliance). Hardware procurement requires budget approval. Agent handles everything up to the approval gate, then executes post-approval automatically.

**Example Interaction:**
> A new hire notification comes in: "Maria Santos, starting Monday as Senior Credit Analyst in Commercial Lending, reporting to VP James Wu." ServiceBot immediately creates an onboarding package with 18 access requests: Active Directory account, email, VPN, core banking (read-only commercial module), credit decisioning system (analyst role), Moody's analytics portal, Bloomberg terminal access, loan origination system, document management, intranet, time tracking, expense reporting, Teams channels (Commercial Lending, Credit Committee, All-Bank), building access badge request, laptop provisioning (analyst spec), and dual monitor setup. Each request is pre-populated with the appropriate access level based on the "Senior Credit Analyst" role template, with James Wu auto-assigned as approver. ServiceBot sends James a single consolidated approval request rather than 18 separate ones, and upon approval, begins executing provisioning in parallel.

---

### Use Case 7: Regulatory Technology (RegTech) Compliance Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking IT must comply with a constantly expanding web of technology-related regulations: FFIEC IT Handbook, NYDFS 23 NYCRR 500, PCI-DSS, SOX IT controls, GLBA Safeguards Rule, CCPA/CPRA, GDPR, BCBS 239, and now DORA (for EU operations). Each regulation has dozens to hundreds of specific control requirements. Compliance teams maintain control inventories in massive spreadsheets, conduct periodic assessments against each framework, track remediation of findings, and prepare evidence packages for examinations. The overlap between frameworks (a single control may satisfy requirements across 3–4 regulations) is poorly mapped, leading to duplicate testing and wasted effort. When a new regulation drops (or an existing one is updated), the gap analysis process takes months.

#### The Solution
monday.com as a **Regulatory Compliance Management** platform. A **Control Inventory Board** with: Control ID (text), Control Description (long text), Control Owner (people), Frameworks Mapped (tags: FFIEC, NYDFS, PCI-DSS, SOX, GLBA, GDPR, DORA, CCPA), Control Category (dropdown: Access Management, Change Management, Incident Response, BCP/DR, Data Protection, Network Security, Vendor Management, Audit & Logging), Testing Frequency (dropdown: Continuous, Monthly, Quarterly, Semi-Annual, Annual), Last Tested (date), Next Test Due (date), Test Result (status: Effective/Partially Effective/Ineffective/Not Tested), Evidence Location (link), and Remediation Required (checkbox). Connected boards: **Regulatory Updates** (tracking new regulations and amendments), **Examination Calendar**, **Findings & Remediation** (with severity, due dates, and status), and **Framework Crosswalk** (mapping control-to-requirement for each framework).

#### The Outcome
40% reduction in compliance testing effort through framework crosswalk eliminating duplicate testing. Examination preparation time reduced from 4–6 weeks to 1 week with always-current evidence. Zero missed remediation deadlines for regulatory findings (MRAs/MRIAs). Real-time compliance posture dashboard for CISO and Board Risk Committee reporting.

#### Discovery Questions
- How many regulatory frameworks does your IT department need to comply with?
- How do you currently map controls across overlapping frameworks to avoid duplicate testing?
- What was the last regulatory finding your IT team received, and how long did remediation take?
- How much time does your team spend preparing for regulatory examinations each year?
- Do you have a process for assessing the impact of new or updated regulations on your control environment?

#### Industry Context
Banks face overlapping and sometimes conflicting regulatory requirements from multiple supervisors. A bank with international operations might answer to the OCC, Federal Reserve, FDIC, NYDFS, SEC, CFTC, FCA, ECB, and MAS — each with their own technology risk expectations. FFIEC IT Examination Handbook was substantially updated in 2024, adding new expectations around cloud computing, API security, and AI governance. The concept of a "single control, multiple frameworks" approach (sometimes called Unified Compliance Framework or UCF) is industry best practice but rarely implemented well. MRAs typically carry 90-day remediation deadlines; MRIAs may require immediate action.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Compliance Tracker for bank IT. Create a board called 'IT Control Inventory' with columns: Control ID (text), Control Title (text), Description (long text), Owner (people), Regulatory Frameworks (tags: FFIEC, NYDFS 500, PCI-DSS, SOX, GLBA, GDPR, DORA, CCPA, BCBS 239), Domain (dropdown: Access Management, Change Management, Incident Response, BCP/DR, Data Protection, Network Security, Third-Party Risk, Audit Logging, Cryptography), Testing Frequency (dropdown: Continuous, Monthly, Quarterly, Annual), Last Test Date (date), Next Test Due (date), Test Result (status: Effective=green, Partially Effective=yellow, Ineffective=red, Not Yet Tested=grey), Evidence Link (link), Remediation Status (status: None Required=green, In Progress=orange, Overdue=red, Completed=blue). Create groups by Domain. Add automations: when Next Test Due is today, notify Owner; when Test Result is Ineffective, create item in connected 'Findings & Remediation' board with 90-day due date; when Remediation Status is Overdue, notify group 'Compliance Leadership'. Create a Dashboard with: control effectiveness distribution pie chart, overdue tests count, findings by domain bar chart, upcoming examination timeline, and remediation aging chart."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ComplianceMapper
**Agent Purpose:** Track regulatory changes, map controls across frameworks, eliminate duplicate testing, and ensure examination readiness.

**Triggers:**
- New regulatory update added to Regulatory Updates board
- Control test result marked as Ineffective
- Remediation due date within 14 days
- Examination scheduled within 60 days
- Monthly compliance posture report schedule

**Actions:**
- Analyze new regulatory requirements and map them to existing controls, identifying gaps that require new controls or enhanced testing
- Generate framework crosswalk reports showing which controls satisfy which requirements across all applicable frameworks
- Recommend consolidated testing schedules that satisfy multiple framework requirements with a single test
- Produce examination preparation packages: control inventory, test results, evidence index, remediation status, organized by examiner's expected review areas
- Alert compliance leadership when remediation deadlines approach with progress assessment and risk of missing deadline
- Generate monthly Board Risk Committee compliance dashboard with posture scores by framework and domain

**Data Required:**
- Complete control inventory with framework mappings
- Regulatory framework requirement databases
- Testing history and evidence repository
- Examination schedule and examiner focus areas
- Remediation tracking with historical completion rates

**Autonomy Level:** Human-in-the-Loop
Agent performs analysis, generates mappings, and produces reports autonomously. New control creation requires compliance officer approval. Framework mapping recommendations require validation by subject matter experts. Examination evidence packages require compliance director sign-off before submission.

**Example Interaction:**
> The FFIEC releases updated guidance on cloud computing risk management. ComplianceMapper analyzes the 47 new or modified requirements and maps them against the existing control inventory. It finds that 31 requirements are already addressed by existing controls (mapping them with specific control IDs and evidence references), 9 require enhancements to existing controls (flagging specific gaps), and 7 require entirely new controls. For the 7 new controls, it drafts proposed control descriptions, suggests owners based on domain expertise, and estimates testing effort. It also identifies that 4 of the new requirements overlap with NYDFS 500 Section 500.19 requirements already being tested, recommending a combined testing approach that saves approximately 60 hours of assessment work annually. The analysis is delivered to the CISO with a recommended 90-day implementation roadmap.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| CAB | Change Advisory Board — governance body that reviews and approves IT changes |
| CMDB | Configuration Management Database — inventory of IT assets and their relationships |
| FFIEC | Federal Financial Institutions Examination Council — interagency body setting IT examination standards |
| MRA | Matter Requiring Attention — regulatory finding requiring remediation |
| MRIA | Matter Requiring Immediate Attention — urgent regulatory finding |
| SOC 2 | Service Organization Control Type 2 — audit report on vendor security controls |
| TPRM | Third-Party Risk Management — vendor oversight discipline |
| NYDFS | New York Department of Financial Services — state regulator with cyber regulations |
| DORA | Digital Operational Resilience Act — EU regulation for financial sector IT resilience |
| RBAC | Role-Based Access Control — access management methodology |
| SLA | Service Level Agreement — performance commitment for IT service delivery |
| MTTR | Mean Time to Resolve — average incident resolution time |
| MTTD | Mean Time to Detect — average time to identify an incident |
| SOX | Sarbanes-Oxley Act — US law requiring controls over financial reporting systems |
| PCI-DSS | Payment Card Industry Data Security Standard — card payment security requirements |
| BCBS 239 | Basel Committee standard for risk data aggregation and reporting |
| Core Banking | Central system processing daily transactions, maintaining accounts, and managing ledgers |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CIO / CTO | IT strategy, budget, architecture decisions | Decision-maker |
| CISO | Cybersecurity, compliance, risk management | Decision-maker (security spend) |
| VP Infrastructure & Operations | Data centers, network, cloud, service desk | Decision-maker (infrastructure) |
| VP Application Development | Core banking, digital channels, custom development | Decision-maker (application spend) |
| IT PMO Director | Portfolio management, resource allocation, governance | Influencer |
| TPRM Director | Vendor oversight, third-party risk assessment | Influencer |
| Enterprise Architect | Technology standards, integration strategy | Influencer |
| IT Audit Director | Control testing, regulatory examination support | Influencer |
| COO | Operations oversight (IT often reports here) | Executive sponsor |
| Chief Risk Officer | Enterprise risk including technology risk | Executive sponsor |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations | IT supports all operational systems; shared interest in automation | Process automation, workflow management |
| Security & Infosec | Deeply intertwined with IT; shared tools and processes | Unified security operations, GRC platform |
| Finance | IT budget management, vendor payments, SOX compliance | Budget tracking, procurement workflows |
| Legal | Contract management for IT vendors, regulatory response | Contract lifecycle management |
| HR | Employee onboarding/offboarding drives access management | Identity lifecycle management |
| Product & R&D | Digital product development, DevOps collaboration | Product development workflows, sprint management |
| Compliance | Regulatory examination support, control testing | Unified compliance management platform |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow | Enterprise ITSM, dominant in large banks | monday.com for PMO, TPRM, and compliance where ServiceNow is over-engineered; complement for business-facing workflows |
| Jira / Atlassian | Development teams, agile project management | monday.com as the portfolio layer above Jira; unified view for non-technical stakeholders |
| BMC Remedy | Legacy ITSM, declining market share | Full replacement for mid-size banks modernizing away from Remedy |
| Archer (RSA) | GRC platform, risk and compliance management | monday.com for operational risk tracking at lower cost and higher usability |
| Excel / SharePoint | The "shadow IT" default for everything not in a tool | Eliminate spreadsheet-based tracking for TPRM, compliance, and portfolio management |
| Smartsheet | Lightweight project management, some banking adoption | Superior automation, integrations, and AI capabilities |
| Planview | Enterprise portfolio management | More intuitive, faster time-to-value, better adoption rates |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We're standardized on ServiceNow" | monday.com complements ServiceNow — it excels at cross-functional workflows (PMO, TPRM, compliance) where ServiceNow's rigidity creates shadow IT. Many banks run both. |
| "Is monday.com FedRAMP / SOC 2 certified?" | monday.com maintains SOC 2 Type II certification, GDPR compliance, and HIPAA readiness. Enterprise security features include SSO, SCIM, audit logs, data residency, and IP restrictions. Discuss specific compliance requirements to map capabilities. |
| "Our data can't leave our environment" | monday.com offers data residency options, encryption at rest and in transit, and enterprise-grade security controls. For highly sensitive data, discuss hybrid approaches where monday.com manages workflows while sensitive data remains in internal systems via integrations. |
| "We already have too many tools" | That's exactly the problem we solve. monday.com consolidates 5-10 point solutions (project management, compliance tracking, vendor management, service requests) into one platform, reducing license costs, integration maintenance, and context-switching. |
| "Our regulators won't approve a cloud platform" | Major regulators (OCC, Fed, FDIC) have issued guidance supporting responsible cloud adoption. Hundreds of banks use cloud-based work management. The key is demonstrating proper vendor due diligence, data controls, and exit strategies — which we help document. |
| "IT teams need specialized tools, not general-purpose platforms" | monday.com's flexibility IS the specialization. Banking IT needs change in every cycle — new regulations, new threats, new technologies. A platform that adapts in hours beats a rigid tool that requires months of professional services to reconfigure. |

## Proof Points
*(To be populated with customer references)*
- [Banking/financial services customers using monday.com for IT operations]
- [Compliance or security workflow case studies]
- [IT PMO consolidation success stories]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
