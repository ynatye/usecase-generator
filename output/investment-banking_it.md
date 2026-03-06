# Investment Banking × IT Playbook

## Overview

IT departments in investment banking are among the most complex and heavily regulated technology organizations in any industry. A typical bulge-bracket bank employs 10,000-40,000 technologists; mid-market and boutique firms still dedicate 20-30% of total headcount to technology. The IT organization spans infrastructure (data centers, cloud, networking), application development (trading systems, risk engines, client portals), cybersecurity, data management, enterprise architecture, and production support. Annual technology budgets range from $1-12 billion at major firms, with 60-70% consumed by "run the bank" (keeping existing systems operational) and only 30-40% available for "change the bank" (new capabilities).

The technology landscape in investment banking is uniquely challenging. Legacy systems — some dating to the 1980s and 1990s — run critical trading and settlement processes. These COBOL, C++, and early Java applications are deeply embedded, poorly documented, and maintained by a shrinking pool of specialized developers. Simultaneously, regulators demand modern capabilities: real-time risk reporting, comprehensive audit trails, cyber resilience, and data lineage. The result is a technology estate of staggering complexity — a large bank may run 3,000-5,000 distinct applications, with hundreds of integration points.

IT teams in IB face relentless demand from every business line: front office wants faster execution and analytics, Operations needs automation, Compliance requires new regulatory reporting, and Risk demands real-time calculations. The traditional project delivery model (6-18 month waterfall cycles) is being pressured toward agile/DevOps, but regulated change management processes, extensive testing requirements, and production stability concerns create tension. CIOs are simultaneously asked to cut costs, modernize infrastructure, strengthen cybersecurity, and deliver AI capabilities — all while maintaining 99.99% uptime on systems that process trillions of dollars daily.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | IB IT manages thousands of applications and dozens of project/workflow tools; consolidation reduces license costs, integration complexity, and context-switching |
| 2 | Scale Impact Without Overhead | High | Technology demand far exceeds delivery capacity; IT must do more with flat or shrinking budgets and headcount |
| 3 | Replace or Radically Augment Headcount | Medium-High | Production support, incident management, and change management consume massive manual effort ripe for AI augmentation |

## Prioritized Use Cases

---

### Use Case 1: IT Project Portfolio Management (PPM)

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banking IT departments manage 200-1,000+ concurrent projects ranging from minor system enhancements to multi-year platform migrations. These projects compete for the same scarce resources: developers, QA engineers, infrastructure capacity, and production deployment windows. Currently, portfolio visibility is fragmented across Jira (development teams), ServiceNow (infrastructure), Confluence (documentation), Excel (resource planning and financials), and PowerPoint (executive reporting). No single view shows the true state of the portfolio — which projects are on track, which are consuming more resources than planned, and where interdependencies create risk. CIOs spend hours each week in status meetings that could be dashboards. Resource allocation is based on tribal knowledge rather than data, leading to chronic overcommitment and delivery delays. The average IB IT project is delivered 40% late and 30% over budget.

#### The Solution
monday.com serves as the unified IT portfolio management layer. Each project is an item with structured fields for financials, timeline, resources, risk, and business alignment. Portfolio-level dashboards show real-time health across all projects with drill-down capability. Resource management views reveal allocation conflicts and capacity gaps. Integration with Jira pulls development progress automatically, while financial data flows from SAP/Oracle. Executive reporting is auto-generated from live data rather than manually assembled from stale spreadsheets. Strategic alignment scoring ensures the portfolio reflects business priorities, with AI-powered recommendations for resource reallocation when constraints are identified.

#### The Outcome
- 60% reduction in time spent on status reporting and executive presentations
- 25% improvement in on-time project delivery through early warning and resource optimization
- Real-time portfolio visibility for CIO and business stakeholders — no more waiting for monthly reports
- 15% improvement in resource utilization through data-driven allocation
- Single source of truth replacing 5-8 disconnected tools for portfolio tracking

#### Discovery Questions
1. "How many active IT projects do you have right now, and if I asked you which 10 are most at risk, how quickly could you answer that?"
2. "How much time does your team spend each week preparing status updates and executive presentations versus actually delivering projects?"
3. "When two projects need the same senior developer or architect, how is that conflict identified and resolved — proactively or when something breaks?"
4. "How do you currently ensure your IT portfolio is aligned with business strategic priorities — is there a scoring mechanism, or is it relationship-driven?"
5. "What's your average project delivery variance against plan — both timeline and budget — and do you have that data readily available?"

#### Industry Context
IB IT portfolio management is more complex than most industries because of: (1) regulatory-driven projects that are non-negotiable regardless of resource constraints, (2) cross-business dependencies where a single platform change affects multiple trading desks, (3) strict production change windows (typically weekends for major releases), and (4) the need to maintain development, UAT, and production environments for each application. The SE should understand that IB IT leaders think in terms of "run the bank" vs. "change the bank" budgets, and that any new tool must demonstrate either cost reduction in "run" or acceleration in "change."

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Project Portfolio Management system for an investment bank. Create a board called 'IT Project Portfolio' with columns: Project Name (text), Project ID (text), Project Manager (people), Executive Sponsor (people), Business Line (dropdown: Equities, Fixed Income, Derivatives, FX, Prime Brokerage, Operations, Risk, Compliance, Cross-Business, Infrastructure), Project Category (dropdown: Regulatory/Mandatory, Strategic, Efficiency, Maintenance, Security, Data), Priority Tier (dropdown: Tier 1 — Critical, Tier 2 — High, Tier 3 — Standard), Strategic Alignment Score (numbers, 1-100), Status (status: Intake, Planning, In Delivery, UAT, Deployment, Complete, On Hold, Cancelled), Health (status: Green, Amber, Red, Black), Phase (dropdown: Discovery, Build Sprint 1-N, Integration Testing, UAT, Pre-Prod, Production), Planned Start (date), Planned End (date), Actual Start (date), Forecast End (date), Schedule Variance (formula: Forecast End - Planned End in days), Approved Budget (numbers, USD), Spent to Date (numbers, USD), Budget Variance % (formula), Headcount Allocated (numbers — FTEs), Key Risks (long text), Dependencies (link to other items), Jira Epic Link (text). Group by Business Line. Add automations: when Health changes to Red, notify CIO office and create item on Risk Register board; when Budget Variance exceeds 20%, auto-change Health to Amber; monthly on the 1st, generate snapshot of all projects for trend analysis. Create Dashboard with: portfolio health summary (pie chart of Green/Amber/Red/Black), budget overview (total approved vs. spent vs. forecast), timeline view of all Tier 1 projects, resource demand vs. capacity (bar chart by month), projects by Business Line and Category (heat map), delivery performance metrics (on-time %, on-budget %). Add Timeline view for Gantt-style visualization and a Workload view for resource allocation."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PortfolioSense — IT Portfolio Intelligence Agent
**Agent Purpose:** Provide real-time portfolio health intelligence, predict delivery risks, and optimize resource allocation across the IT project portfolio.

**Triggers:**
- Weekly Monday 7:00 AM portfolio health scan
- Project health status changes to Amber or Red
- Resource allocation conflict detected (same person >120% allocated)
- Budget variance exceeds threshold (15% for Tier 1, 20% for Tier 2/3)
- New project intake request submitted
- Quarterly portfolio rebalancing review

**Actions:**
- Generate weekly CIO portfolio summary with risk-ranked project list and recommended actions
- Predict project delivery risks based on historical patterns (projects with similar profiles that went Red)
- Identify resource conflicts and suggest reallocation options with impact analysis
- Score new project intake requests against strategic criteria and recommend prioritization
- Auto-update project status from Jira integration data (sprint velocity, burndown trends)
- Flag interdependency risks when a dependent project's timeline shifts

**Data Required:**
- All project data from IT Project Portfolio board
- Historical project delivery data (mondayDB) — actuals vs. plans
- Resource allocation data across all projects
- Jira sprint data via API integration
- Financial data (budget actuals) from finance systems
- Strategic priority framework and scoring criteria

**Autonomy Level:** Escalation-Based
Fully autonomous for monitoring, analysis, reporting, and alerting. Escalates to human for: resource reallocation decisions, project priority changes, budget increase approvals, and project cancellation recommendations.

**Example Interaction:**
> During its Monday morning scan, PortfolioSense identifies that the "FRTB Regulatory Reporting" project (Tier 1, regulatory deadline in 4 months) has slowed its Jira sprint velocity by 35% over the past 3 sprints. Cross-referencing resource data, it discovers that 2 of the 4 senior developers were partially reassigned to an urgent cybersecurity remediation project 3 weeks ago. Based on the current velocity and remaining backlog, PortfolioSense forecasts a 6-week delay — pushing past the regulatory deadline.
>
> It immediately generates an alert for the CIO with three options: (1) Restore the developers to FRTB full-time, accepting 3-week delay on the cybersecurity project, (2) Bring in 2 contractors at estimated cost of $180K to backfill on either project, (3) Descope FRTB Phase 2 features to meet the deadline with current resources. Each option includes projected timeline impact, cost, and risk assessment. The CIO reviews the analysis and selects option 2 within an hour — a decision that would have taken 2 weeks of meetings to surface and resolve in the old model.

---

### Use Case 2: Production Incident & Major Incident Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
When a trading system goes down or a critical application fails, every minute costs money — potentially millions in lost trading revenue, failed settlements, or regulatory exposure. IB IT manages hundreds of production incidents daily (P3/P4) and 2-5 major incidents (P1/P2) weekly. The incident management process involves: detection (monitoring alerts), triage, bridge call coordination, investigation, resolution, and post-incident review. Major incidents require assembling cross-functional teams (application support, infrastructure, DBA, networking, vendor) in minutes, managing communications to business stakeholders, and maintaining detailed timelines for regulators. Current ServiceNow-based processes are heavyweight, slow to update, and provide poor real-time visibility. War room coordination happens on conference calls and chat — with no structured tracking of actions, decisions, and ownership. Post-incident reviews are inconsistent, and lessons learned rarely translate into preventive action.

#### The Solution
monday.com provides a streamlined, real-time incident management workspace. Each incident is an item with structured fields for severity, impact, timeline, and ownership. Major incidents trigger automated war room workflows: assembling the response team, creating a real-time timeline board, managing stakeholder communications, and tracking resolution actions. Dashboards show live incident status, MTTR trends, and recurring issue patterns. Post-incident reviews are structured and tracked to completion. Integration with monitoring tools (PagerDuty, Datadog, Splunk) auto-creates incidents from alerts. The system is optimized for speed — updating incident status takes seconds, not the minutes required in ServiceNow.

#### The Outcome
- 30% reduction in Mean Time to Resolution (MTTR) for P1/P2 incidents
- 100% completion rate on post-incident review actions (up from ~40%)
- Real-time stakeholder communication — no more "what's happening?" calls during outages
- Pattern identification: recurring issues flagged for permanent fix before they become major
- Complete incident timeline for regulatory inquiries (especially critical for trading system outages)

#### Discovery Questions
1. "When a critical trading system goes down, how quickly can you assemble the right people and start coordinated troubleshooting — minutes or hours?"
2. "During a major incident, how do you keep business stakeholders informed — is that structured or ad-hoc, and how much of the response team's time does communication consume?"
3. "What percentage of your P1 incidents are repeat occurrences of previously identified issues, and do you have confidence that post-incident actions are being completed?"
4. "If a regulator asked you to produce a detailed timeline of your last major trading system outage — including all actions taken, decisions made, and communications sent — how long would that take?"
5. "How many monitoring tools generate alerts into your incident management process, and how often do alert storms during major events create noise that slows resolution?"

#### Industry Context
Production stability in IB IT is existential. A 30-minute outage of a trading system during market hours can mean millions in lost revenue and regulatory scrutiny. Regulators (SEC, FCA) increasingly focus on operational resilience — requiring banks to demonstrate they can handle technology failures without market disruption. The FCA's operational resilience framework requires firms to set "impact tolerances" for important business services and test their ability to stay within them. Key concepts: RPO (Recovery Point Objective), RTO (Recovery Time Objective), BCP (Business Continuity Planning), DR (Disaster Recovery), runbooks, playbooks.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Production Incident Management system for investment banking IT. Create a board called 'Production Incidents' with columns: Incident ID (auto-number), Title (text), Severity (dropdown: P1 — Critical Trading Impact, P2 — Significant Business Impact, P3 — Moderate Impact, P4 — Low Impact), Affected System (dropdown: Equities Trading, Fixed Income Trading, Derivatives Platform, Risk Engine, Settlement System, Market Data, Client Portal, Internal Portal, Infrastructure, Network), Business Impact (text), Detected By (dropdown: Monitoring Alert, User Report, Automated Test, Business Escalation), Incident Commander (people), Status (status: Detected, Triaged, Investigating, Fix Identified, Fix Deployed, Monitoring, Resolved, Post-Incident Review, Closed), Start Time (date with time), Resolution Time (date with time), MTTR (formula in minutes), Root Cause Category (dropdown: Code Defect, Infrastructure Failure, Configuration Error, Capacity, Third Party, Data Issue, Network, Human Error, Unknown), Impacted Trades/Transactions (numbers), Estimated Financial Impact (numbers, USD), Resolution Summary (long text), Post-Incident Review Status (status: Not Started, Scheduled, Completed, Actions Tracked), Assigned Team (dropdown: App Support, Infrastructure, DBA, Networking, Security, Vendor). Group by Severity. Add automations: P1 incidents auto-notify CTO, Head of Trading Technology, and Ops leadership; if P1 Status hasn't changed in 15 minutes, escalate to next management level; when Status changes to Resolved, auto-create Post-Incident Review item due within 5 business days. Create a Dashboard with: open incidents by severity (numbers widgets), MTTR trend (line chart by week), incidents by root cause (bar chart), incidents by system (bar chart), P1/P2 incident timeline (last 90 days), post-incident review completion rate (percentage). Add a Timeline view showing incident duration visualization."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** IncidentIQ — Major Incident Response Agent
**Agent Purpose:** Accelerate incident detection, coordinate response teams, manage communications, and drive post-incident improvements.

**Triggers:**
- P1 or P2 incident created (manual or via monitoring integration)
- Incident status unchanged for 15 minutes (P1) or 30 minutes (P2)
- Correlation: multiple P3/P4 incidents from same system within 30 minutes (possible underlying P1)
- Post-incident review deadline approaching
- Weekly incident trend analysis

**Actions:**
- Auto-assemble response team based on affected system's on-call roster and expertise matrix
- Generate real-time incident timeline, logging every status change, communication, and decision
- Send structured business stakeholder updates every 15 minutes during P1 (templated, consistent)
- Correlate current incident with historical incidents on same system — surface prior resolution steps
- Draft post-incident review document pre-populated with timeline, impact data, and suggested root cause categories
- Track all post-incident review actions to completion with automated follow-ups

**Data Required:**
- On-call roster and escalation matrices by system and team
- Historical incident database with resolution details (mondayDB)
- Monitoring tool integration feeds (PagerDuty, Datadog, Splunk alerts)
- System dependency map (which systems depend on which)
- Business stakeholder distribution lists by affected business line

**Autonomy Level:** Human-in-the-Loop
Auto-assembles teams, sends communications, logs timeline, and correlates with history. Requires human for: declaring severity level, approving production fixes, deciding escalation path, and signing off on root cause analysis.

**Example Interaction:**
> At 9:47 AM ET — 17 minutes after US equity market open — Datadog fires a latency alert on the equities order management system. Within 30 seconds, IncidentIQ correlates this with 3 P4 alerts from the same system cluster in the past 10 minutes, recognizes the pattern, and auto-creates a P1 incident. It pages the Equities Technology on-call engineer, the infrastructure team lead, and the DBA on-call, and opens a war room channel.
>
> While the team assembles (average 4 minutes), IncidentIQ has already pulled up the last 3 incidents on this system: one was a database connection pool exhaustion (resolved by pool expansion), one was a memory leak in the pricing module (resolved by restart), and one was a network switch failover. It presents these as "likely similar" with confidence scores. The initial investigation confirms connection pool exhaustion — the team applies the known fix in 8 minutes, and IncidentIQ sends the "service restored" notification to all business stakeholders at 10:02 AM, total MTTR: 15 minutes.
>
> IncidentIQ notes this is the 3rd connection pool incident in 6 months and escalates to the engineering manager with a recommendation for a permanent architectural fix, pre-populated with cost-of-incidents data ($2.1M in estimated trading impact across all 3 events).

---

### Use Case 3: Technology Change & Release Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Change management in investment banking IT is a high-stakes coordination exercise. Every code deployment, configuration change, infrastructure modification, and database update must go through a formal Change Advisory Board (CAB) process. A large bank processes 500-2,000 changes per week, each requiring risk assessment, testing evidence, rollback plans, and approvals from multiple stakeholders. Production deployment windows are limited — typically weekends for major releases, with specific blackout periods (month-end, quarter-end, regulatory reporting dates). The change management process is often the biggest bottleneck to delivery speed: changes queue for weeks waiting for CAB review, deployment coordination is manual, and post-deployment verification is inconsistent. When changes fail in production, the rollback process is panicked and poorly documented.

#### The Solution
monday.com manages the end-to-end change lifecycle: request → risk assessment → CAB review → scheduling → deployment → verification → closure. Each change is an item with structured risk scoring, automated routing based on change type and risk level, and visual scheduling against the production calendar. Low-risk, standard changes are auto-approved based on predefined criteria. CAB review dashboards show the week's changes with risk heat maps and dependency analysis. Deployment runbooks are attached to change items, and post-deployment verification checklists ensure nothing is missed. Calendar views prevent scheduling conflicts and blackout violations.

#### The Outcome
- 50% reduction in change lead time (from request to production deployment)
- 70% of low-risk changes auto-approved (eliminating CAB bottleneck for routine updates)
- Zero blackout period violations through automated calendar enforcement
- 40% reduction in change-related incidents through better risk assessment and verification
- Complete change audit trail for regulatory compliance (SOX, OCC requirements)

#### Discovery Questions
1. "How many changes does your team process weekly, and what's the average lead time from change request to production deployment?"
2. "What percentage of your changes would you classify as truly low-risk and routine — and do those still go through the full CAB process?"
3. "How often do production changes cause incidents, and can you trace the root cause back to a specific change quickly?"
4. "How do you manage the scheduling of changes to avoid conflicts — especially around month-end, quarter-end, and regulatory reporting dates?"
5. "If an auditor asked you to demonstrate your change management controls for a specific application over the past quarter, how easily could you produce that evidence?"

#### Industry Context
Change management in IB is governed by ITIL frameworks but heavily influenced by regulatory requirements. SOX (Sarbanes-Oxley) requires segregation of duties between developers and deployers. OCC (Office of the Comptroller of the Currency) examiners review change management controls. The FCA's operational resilience framework extends to technology change. Key concepts: CAB (Change Advisory Board), RFC (Request for Change), standard vs. normal vs. emergency changes, deployment windows, change freeze periods, rollback plan, PIR (Post-Implementation Review).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Technology Change & Release Management system. Create a board called 'Change Management' with columns: Change ID (auto-number), Change Title (text), Change Type (dropdown: Standard, Normal, Emergency, Expedited), Risk Level (dropdown: Low, Medium, High, Critical), Category (dropdown: Code Deployment, Configuration Change, Infrastructure, Database, Network, Security Patch, Vendor Update), Affected Application (text), Business Line Impacted (dropdown: Equities, Fixed Income, Derivatives, FX, Operations, Risk, Compliance, Infrastructure, Cross-Business), Requestor (people), Change Owner (people), Approver (people), Status (status: Draft, Submitted, Risk Assessed, CAB Pending, CAB Approved, Scheduled, Deploying, Deployed — Verifying, Verified — Closed, Rolled Back, Rejected, Cancelled), Planned Deployment Date (date), Deployment Window (dropdown: Market Hours — Emergency Only, After Hours, Weekend, Maintenance Window), Risk Score (numbers, 1-100), Testing Evidence (file), Rollback Plan (long text), Pre-Deployment Checklist (status: Complete, Incomplete), Post-Deployment Verification (status: Not Started, In Progress, Pass, Fail), SOX Segregation Check (status: Compliant, Non-Compliant), Dependencies (link to other changes), Blackout Check (status: Clear, Blackout Period — Requires Exception). Group by Status. Add automations: when Risk Level is Low and Change Type is Standard, auto-advance to CAB Approved (skip manual CAB); when Planned Deployment Date falls in a blackout period, flag and notify change manager; when Post-Deployment Verification changes to Fail, auto-create P2 incident and initiate rollback workflow; when Status is Submitted and no action for 3 business days, notify Change Owner and escalate. Create Dashboard with: changes by status pipeline (funnel), weekly change volume trend, risk distribution (pie chart), deployment success rate (percentage), changes by application (bar chart), upcoming deployment calendar (calendar view), failed changes requiring rollback (table). Add Calendar view showing all scheduled deployments against blackout periods."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ChangeGuard — Intelligent Change Management Agent
**Agent Purpose:** Accelerate change processing, automate risk assessment, prevent scheduling conflicts, and ensure compliant deployments.

**Triggers:**
- New change request submitted
- Change scheduled within 48 hours — pre-deployment readiness check
- Post-deployment verification not completed within 2 hours of deployment
- Emergency change requested during market hours
- Weekly CAB preparation (every Wednesday for Friday/weekend CAB)

**Actions:**
- Auto-calculate risk score based on: change type, application criticality tier, deployment complexity, historical change failure rate for this application, and proximity to blackout periods
- Route low-risk standard changes for auto-approval; flag high-risk changes for senior CAB review
- Check scheduling conflicts against production calendar, other changes, and blackout periods
- Generate pre-deployment checklist customized to change type and application
- Run post-deployment verification reminders and escalate failures
- Compile weekly CAB package with all pending changes, risk heat map, and scheduling recommendations

**Data Required:**
- Change request details from the board
- Application criticality tier registry
- Historical change success/failure rates by application (mondayDB)
- Production calendar with blackout periods and deployment windows
- SOX compliance rules (segregation of duties requirements)
- Team availability and on-call schedules for deployment support

**Autonomy Level:** Human-in-the-Loop
Auto-scores risk, routes for approval, checks schedules, and generates reports. Requires human for: CAB approval decisions, emergency change authorization, and rollback decisions.

**Example Interaction:**
> A developer submits a change request for a code deployment to the fixed income pricing engine — classified as "Normal" change. ChangeGuard auto-assesses: the application is Tier 1 (critical trading system), the change touches pricing logic (high-impact area), and the last 2 deployments to this application had post-deployment issues. Risk score: 82/100 (High). ChangeGuard flags it for senior CAB review rather than standard processing, and recommends a weekend deployment window with extended monitoring.
>
> It also detects that another change to the downstream risk calculation engine is scheduled for the same weekend. ChangeGuard flags the dependency, recommends sequencing (pricing engine first, risk engine 4 hours later with verification gate between them), and generates a combined deployment runbook. The CAB reviews both changes together, approves the sequenced plan, and ChangeGuard creates the deployment timeline with automated checkpoints.

---

### Use Case 4: Vendor & Third-Party Risk Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banks rely on hundreds of technology vendors — from core trading platforms (Bloomberg, Refinitiv, Murex) to cloud providers (AWS, Azure), market data feeds, cybersecurity tools, and niche utilities. Each vendor represents a concentration risk: if Bloomberg Terminal goes down, trading stops; if a cloud region fails, applications are impacted. Regulators (OCC, FCA, EBA) increasingly require comprehensive third-party risk management (TPRM) programs with regular due diligence, performance monitoring, and exit planning. Currently, vendor management is scattered across procurement (contracts), IT (technical oversight), risk (due diligence), and legal (contract terms) — with no unified view. Contract renewals sneak up, SLA breaches go untracked, and when a vendor has a security incident, determining exposure takes days of manual analysis.

#### The Solution
monday.com provides a unified vendor lifecycle management platform. Each vendor is an item with comprehensive profiling: criticality tier, services provided, contract details, SLA metrics, risk assessment scores, and due diligence status. Automated workflows manage the annual due diligence cycle, contract renewals, and performance reviews. Dashboard views show vendor risk landscape, upcoming renewals, SLA compliance trends, and concentration risks. When a vendor security incident occurs, the system immediately surfaces all affected applications and business lines. Integration with contract management and procurement systems provides end-to-end visibility.

#### The Outcome
- 100% compliance with regulatory TPRM requirements (zero gaps in due diligence cycles)
- 90% reduction in time to assess vendor incident impact (from days to hours)
- Zero missed contract renewals (currently 5-10% result in unfavorable auto-renewals)
- Consolidated vendor spend visibility enabling 10-15% savings through negotiation leverage
- Proactive concentration risk identification before it becomes a regulatory finding

#### Discovery Questions
1. "How many technology vendors does your bank rely on, and can you tell me today which are your top 10 most critical — meaning their failure would stop a business function?"
2. "When a vendor like CrowdStrike has a major incident, how quickly can you determine which of your systems and business processes are affected?"
3. "How do you currently manage the annual due diligence cycle for your critical vendors — is it proactive or reactive?"
4. "Have you experienced a contract auto-renewal on unfavorable terms because the renewal date wasn't tracked centrally?"
5. "How do you demonstrate to regulators that your third-party risk management program is comprehensive and actively maintained?"

#### Industry Context
TPRM is one of the fastest-growing regulatory focus areas for banks. The OCC's 2023 Third-Party Risk Management guidance, the EU's DORA (Digital Operational Resilience Act, effective January 2025), and the FCA's operational resilience framework all require banks to demonstrate robust vendor oversight. Key concepts: fourth-party risk (your vendor's vendors), critical service providers (CSPs), exit strategy/transition planning, right-to-audit clauses, data residency requirements. Cloud providers (AWS, Azure, GCP) are treated as "material outsourcing arrangements" requiring board-level oversight in many jurisdictions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor & Third-Party Risk Management system. Create a board called 'Technology Vendor Registry' with columns: Vendor Name (text), Vendor ID (text), Criticality Tier (dropdown: Tier 1 — Critical, Tier 2 — Important, Tier 3 — Standard, Tier 4 — Low), Services Provided (tags: Trading Platform, Market Data, Cloud Infrastructure, Cybersecurity, Settlement, Communication, Analytics, Storage, Compliance Tool), Business Lines Served (tags: Equities, Fixed Income, Derivatives, FX, Operations, Risk, Compliance, Cross-Business), Primary Contact (text), Relationship Owner (people), IT Owner (people), Risk Owner (people), Contract Start Date (date), Contract End Date (date), Auto-Renewal Notice Period (text — e.g. 90 days), Annual Spend (numbers, USD), SLA Uptime Target (numbers, percentage), SLA Actual Uptime (numbers, percentage), SLA Compliance (status: Exceeding, Meeting, Below — Warning, Breach), Risk Score (numbers, 1-100), Due Diligence Status (status: Current, Due Soon, Overdue, Not Assessed), Last Due Diligence Date (date), Next Due Diligence Date (date), Exit Plan Status (status: Documented, Draft, Not Started, Not Required), Data Residency (dropdown: US Only, EU, UK, Multi-Region, Unknown), SOC 2 Report Status (status: Current, Expired, Not Available), Notes (long text). Group by Criticality Tier. Add automations: when Contract End Date is within 90 days, notify Relationship Owner and Procurement; when Due Diligence Status changes to Overdue, escalate to Risk Owner's manager; when SLA Compliance changes to Breach, create item on Vendor Issues board and notify IT and business owners. Create Dashboard with: vendor count by tier (pie chart), total annual spend by tier (bar chart), due diligence compliance status (percentage current vs. overdue), upcoming contract renewals (next 6 months — table), SLA performance by Tier 1 vendors (table), risk score distribution (chart), concentration analysis (which vendors serve most business lines)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorWatch — Third-Party Risk Intelligence Agent
**Agent Purpose:** Continuously monitor vendor risk, automate due diligence workflows, and provide instant impact analysis when vendor incidents occur.

**Triggers:**
- Vendor security incident reported (via news feed, vendor notification, or manual entry)
- Due diligence date approaching (60 days, 30 days, 7 days)
- Contract renewal notice period reached
- SLA performance drops below threshold for 3 consecutive periods
- Quarterly vendor risk report generation
- New vendor onboarding request

**Actions:**
- Monitor vendor news and security feeds for incident alerts
- When vendor incident detected, auto-generate impact assessment mapping affected systems, business lines, and data exposure
- Send due diligence reminders with pre-populated assessment questionnaires
- Generate contract renewal briefing with: performance history, spend trend, market alternatives, and negotiation recommendations
- Compile quarterly board-level TPRM report with risk trends and remediation status
- Assess new vendor requests against existing capabilities to identify redundancy

**Data Required:**
- Vendor registry with complete profiles
- Application-to-vendor dependency mapping
- Vendor security news feeds and alert services
- Historical SLA performance data (mondayDB)
- Contract terms and financial data
- Regulatory requirements by jurisdiction (DORA, OCC, FCA)

**Autonomy Level:** Escalation-Based
Autonomous for monitoring, alerting, report generation, and due diligence scheduling. Escalates to human for: vendor risk rating changes, contract decisions, and incident response actions.

**Example Interaction:**
> VendorWatch detects via its security news feed that a major cloud infrastructure provider used by the bank has disclosed a data exposure vulnerability. Within 5 minutes, it generates a comprehensive impact assessment: 47 applications hosted on this provider, spanning all business lines, including 3 Tier 1 critical trading systems. It identifies which applications are in the affected region, cross-references data classification to determine if sensitive data (PII, trading data) is at risk, and generates an executive brief.
>
> The brief includes: immediate actions required (patch applications, review access logs), a recommended communication to the board risk committee, and a list of contractual remedies available (right-to-audit, SLA credits, indemnification provisions — all pulled from the contract terms stored in the system). The CISO and CTO have actionable intelligence within 15 minutes of the vendor's disclosure, rather than the typical 2-3 days of manual impact analysis.

---

### Use Case 5: IT Service Request & Demand Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Business lines constantly submit requests to IT: new application features, data extracts, report modifications, environment provisioning, access management, and ad-hoc support. A typical IB IT team receives 100-500 service requests weekly, ranging from 30-minute tasks to multi-week efforts. These requests arrive via email, ServiceNow tickets, Slack messages, and hallway conversations — with no standardized intake, prioritization, or capacity planning. As a result: business lines have no visibility into when their request will be addressed, IT teams are constantly context-switching between planned project work and reactive demand, and leadership can't distinguish between legitimate capacity constraints and inefficient demand management. The "shadow IT" problem — business lines building their own solutions because IT is too slow — creates security, compliance, and architectural risks.

#### The Solution
monday.com provides a unified demand intake and management platform. Standardized Forms capture requests with structured categorization, business justification, and urgency assessment. Incoming requests are triaged into a prioritized backlog with estimated effort and target dates. Capacity views show available team bandwidth against incoming demand. Business stakeholders get self-service status tracking and transparent prioritization rationale. Automation routes requests to appropriate teams, applies SLA timers, and escalates aging items. Analytics reveal demand patterns — which business lines are heaviest requestors, which request types consume the most capacity, where self-service could reduce volume.

#### The Outcome
- 80% reduction in "where is my request?" inquiries through self-service tracking
- 40% improvement in request fulfillment speed through structured prioritization and routing
- 30% reduction in overall request volume through self-service capabilities and demand rationalization
- Complete visibility into IT demand vs. capacity for resource planning
- Elimination of shadow IT risk through responsive, transparent service delivery

#### Discovery Questions
1. "How many service requests does your IT team receive weekly, and what's the current average fulfillment time?"
2. "How do business lines submit requests to IT today — is there a single channel, or do requests come through multiple paths?"
3. "Can your business stakeholders check the status of their request without contacting someone in IT?"
4. "How do you balance capacity between planned project work and incoming service requests — is that a constant tension?"
5. "Are you seeing business lines building their own solutions (shadow IT) because they perceive IT as too slow, and what risks does that create?"

#### Industry Context
IT demand management in IB is complicated by the hierarchical power dynamics — a Managing Director on the trading desk can effectively queue-jump by escalating to the CIO, disrupting planned work. Effective demand management requires transparent prioritization criteria that even senior business stakeholders accept. The SE should frame monday.com as enabling IT to say "yes, and here's when" rather than "we'll get to it" — transforming the relationship from adversarial to collaborative.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Service Request & Demand Management system. Create a board called 'IT Service Requests' with columns: Request ID (auto-number), Request Title (text), Requestor (people), Business Line (dropdown: Equities, Fixed Income, Derivatives, FX, Prime Brokerage, Operations, Risk, Compliance, Finance, HR, Legal), Request Category (dropdown: New Feature, Enhancement, Bug Fix, Data Extract, Report Modification, Access Management, Environment Provisioning, Infrastructure, Integration, Ad-Hoc Support), Priority (dropdown: Critical — Trading Impact, High — Business Deadline, Medium — Important, Low — Nice to Have), Business Justification (long text), Estimated Effort (dropdown: XS — <2 hours, S — 2-8 hours, M — 1-3 days, L — 1-2 weeks, XL — >2 weeks), Assigned Team (dropdown: App Dev — Equities, App Dev — Fixed Income, App Dev — Derivatives, Infrastructure, Data Engineering, DBA, Support, Security), Assigned To (people), Status (status: Submitted, Triaged, Backlog, In Progress, In Review, Testing, Complete, Rejected, On Hold), SLA Target Date (date), Actual Completion Date (date), SLA Met (formula: compare dates), Requestor Satisfaction (dropdown: 5-Excellent, 4-Good, 3-Adequate, 2-Poor, 1-Unacceptable), Notes (long text). Create a Form for business users with: Request Title, Description, Business Line, Category, Priority, Business Justification, Desired Date. Add automations: Critical priority auto-notifies team lead and assigns to senior engineer; if Status is Submitted for >2 business days, escalate to triage manager; when Status changes to Complete, send satisfaction survey to Requestor. Create Dashboard with: open requests by status (funnel), requests by business line (bar chart), average fulfillment time by category (bar chart), SLA compliance rate (percentage), team workload distribution (bar chart), request volume trend (line chart, weekly), satisfaction scores (average). Add Workload view showing team capacity."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DemandIQ — IT Demand Management Agent
**Agent Purpose:** Intelligently triage, route, and prioritize IT service requests while managing capacity and reducing manual coordination.

**Triggers:**
- New service request submitted via Form
- Request aging in Submitted or Backlog status beyond SLA
- Team capacity falls below 20% available
- Weekly demand vs. capacity analysis
- Monthly demand pattern report generation

**Actions:**
- Auto-triage requests: classify category, estimate effort based on similar historical requests, suggest priority level
- Route to appropriate team based on category, application area, and current workload
- Identify duplicate or similar requests and link them for batch processing
- Generate capacity alerts when team utilization exceeds sustainable levels
- Suggest self-service alternatives when request matches a pattern that could be automated
- Compile weekly demand report showing: incoming volume, fulfillment rate, aging items, and capacity forecast

**Data Required:**
- Service request board data
- Historical request fulfillment data with effort actuals (mondayDB)
- Team capacity and allocation data
- Application ownership and team mapping
- Self-service catalog of available automations/tools

**Autonomy Level:** Human-in-the-Loop
Auto-triages, routes, and generates reports. Requires human for: priority overrides, capacity reallocation, and request rejection decisions.

**Example Interaction:**
> A portfolio manager submits a request for a "custom P&L report by strategy" — DemandIQ recognizes this is similar to 4 requests fulfilled in the past quarter, all taking 3-5 days of developer time. It suggests an alternative: the existing BI dashboard has a strategy-level filter that wasn't exposed to this user. DemandIQ drafts a response offering to enable the existing capability (30-minute task) as an immediate solution, while logging the underlying need for a more robust self-service reporting initiative. The PM gets their data the same day instead of waiting 2 weeks, and the development team saves 4 days of effort.

---

### Use Case 6: Cybersecurity Operations & Vulnerability Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks are among the most targeted organizations for cyberattacks. The IT security team manages thousands of vulnerabilities across an estate of 3,000-5,000 applications and tens of thousands of infrastructure components. Vulnerability scanners (Qualys, Tenable, Rapid7) generate tens of thousands of findings monthly. Each vulnerability must be assessed for exploitability, business impact, and remediation priority — then assigned to the appropriate application or infrastructure team for patching. Regulatory requirements (FFIEC, NYDFS Cybersecurity Regulation, DORA) mandate specific remediation timelines by severity. Currently, vulnerability tracking lives in spreadsheets or security-specific tools that application teams don't access, creating a disconnect between "what security knows" and "what gets fixed." Remediation rates for medium-severity vulnerabilities often lag at 40-60% within required timelines.

#### The Solution
monday.com bridges the gap between security identification and business remediation. Vulnerability scan results are imported and auto-assigned to application owners based on asset inventory mapping. Each vulnerability is tracked with regulatory-mandated remediation timelines, business impact context, and clear ownership. Application teams see their vulnerability backlog alongside their other work, enabling integrated prioritization. Dashboards give the CISO real-time visibility into remediation progress by business line, application tier, and severity. Exception and risk acceptance workflows formalize the process for vulnerabilities that can't be patched immediately.

#### The Outcome
- 90%+ remediation rate within regulatory timelines (up from 60%)
- 50% reduction in time from scan to remediation assignment (from weeks to hours)
- Application teams take ownership of security posture with integrated visibility
- CISO has real-time board-ready security metrics without manual report building
- Complete audit trail for regulatory examination of vulnerability management program

#### Discovery Questions
1. "How many open vulnerabilities does your organization have right now across all severity levels, and how confident are you in that number?"
2. "When a critical vulnerability is identified — say a new zero-day — how long does it take to determine which of your applications are affected and get remediation started?"
3. "Do your application development teams have visibility into their vulnerability backlog, or is that managed separately by the security team?"
4. "What's your current remediation rate within regulatory timelines for critical and high-severity vulnerabilities?"
5. "How do you handle vulnerabilities that can't be immediately patched — is there a formal risk acceptance process, or do they just age in the backlog?"

#### Industry Context
Cybersecurity in banking is heavily regulated. NYDFS Cybersecurity Regulation (23 NYCRR 500) requires specific vulnerability management controls. FFIEC (Federal Financial Institutions Examination Council) provides examination guidance. DORA requires ICT risk management including vulnerability management. The SE should understand that banks often have a "three lines of defense" model: 1st line (IT teams doing the work), 2nd line (security and risk teams providing oversight), 3rd line (internal audit providing assurance). Vulnerability management spans all three lines.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Cybersecurity Vulnerability Management system. Create a board called 'Vulnerability Tracker' with columns: Vuln ID (text), CVE ID (text), Title (text), Severity (dropdown: Critical — CVSS 9.0-10.0, High — CVSS 7.0-8.9, Medium — CVSS 4.0-6.9, Low — CVSS 0.1-3.9, Informational), CVSS Score (numbers), Affected Asset (text), Asset Type (dropdown: Application, Server, Database, Network Device, Endpoint, Container, Cloud Resource), Application Tier (dropdown: Tier 1 — Critical, Tier 2 — Important, Tier 3 — Standard), Business Line Owner (dropdown: Equities Tech, FI Tech, Derivatives Tech, Infrastructure, Operations Tech, Risk Tech), Assigned To (people), Discovery Date (date), Regulatory Remediation Deadline (date — auto-calculated based on severity), Status (status: New, Assessed, Assigned, Remediation In Progress, Remediation Complete, Verified, Risk Accepted, Exception Granted, Closed), Remediation Plan (long text), Risk Acceptance Justification (long text — required if Risk Accepted), Compensating Controls (text), Exploitability (dropdown: Active Exploit Known, Proof of Concept Exists, Theoretical, None Known), Scanner Source (dropdown: Qualys, Tenable, Rapid7, Pen Test, Bug Bounty, Manual). Group by Severity. Add automations: Critical vulns with Active Exploit Known auto-notify CISO and affected business line CTO; when Regulatory Remediation Deadline is within 7 days and Status is not Complete or Verified, escalate to manager; when Status changes to Risk Accepted, require approval from CISO (approval workflow). Create Dashboard with: open vulns by severity (stacked bar chart), remediation progress vs. regulatory timeline (gauge chart per severity), vuln aging analysis (how long vulns stay open), top 10 most vulnerable applications (table), remediation rate trend by month (line chart), exception/risk acceptance count and trend."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VulnGuard — Vulnerability Management Intelligence Agent
**Agent Purpose:** Automate vulnerability triage, accelerate remediation through intelligent routing, and ensure regulatory compliance for vulnerability management timelines.

**Triggers:**
- New vulnerability scan results imported
- Critical vulnerability with known active exploit detected
- Remediation deadline approaching (14 days, 7 days, 3 days, 1 day)
- Weekly vulnerability metrics compilation
- New CVE published matching bank's technology stack

**Actions:**
- Auto-triage vulnerabilities: map to affected applications via asset inventory, assign to application owners, set regulatory deadlines
- Prioritize based on: exploitability + asset criticality + business exposure (not just CVSS score)
- Detect duplicate findings across scanners and consolidate
- Generate weekly remediation status reports for CISO and business line CTOs
- Monitor CVE feeds for new vulnerabilities matching the bank's technology stack
- Track remediation verification and close vulnerabilities after confirmation

**Data Required:**
- Vulnerability scanner feeds (Qualys, Tenable, etc.)
- Asset inventory with application-to-owner mapping
- Application criticality tier registry
- Regulatory remediation timeline requirements by severity
- CVE and exploit intelligence feeds (NVD, CISA KEV catalog)
- Historical remediation data for trend analysis

**Autonomy Level:** Escalation-Based
Fully autonomous for triage, assignment, tracking, and reporting. Escalates to human for: risk acceptance decisions, compensating control approvals, and CISO-level notifications for critical/exploited vulnerabilities.

**Example Interaction:**
> A Tuesday morning Qualys scan surfaces 2,847 new findings. VulnGuard processes them in minutes: 12 are Critical, 89 High, 456 Medium, and the rest Low/Informational. It de-duplicates 340 findings already tracked from prior scans. For the 12 Critical findings, it cross-references the CISA Known Exploited Vulnerabilities catalog and flags 3 as actively exploited — these get immediate CISO notification and 24-hour remediation deadlines.
>
> One critical finding affects the derivatives trading platform (Tier 1). VulnGuard identifies that a patch is available, checks the change management board to see if a maintenance window is scheduled this weekend, and pre-creates a change request for the patch deployment, pre-populated with the vulnerability details, business impact assessment, and recommended rollback plan. The application team lead receives a notification with everything needed to approve and schedule the fix — reducing the typical 5-day cycle from discovery to change request to under 1 hour.

---

### Use Case 7: IT Budget & Financial Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
IT financial management in investment banking involves tracking budgets of $100M-$12B across thousands of cost centers, projects, vendors, and headcount categories. The "run the bank" vs. "change the bank" split must be maintained and reported to regulators and the board. Technology cost allocation to business lines is a quarterly exercise of epic spreadsheet complexity. Actual spending rarely aligns with forecasts — project overruns, unplanned infrastructure costs, vendor price increases, and FX fluctuations create constant variance. Finance and IT speak different languages: finance wants cost center-level detail; IT thinks in projects and applications. Reconciliation between the two views consumes significant effort each month-end and quarter-end.

#### The Solution
monday.com provides a real-time IT financial management dashboard that bridges the Finance and IT perspectives. Budget items are structured by: cost center, project, application, vendor, and business line — enabling multi-dimensional analysis. Actual spending data flows from SAP/Oracle via integration. Variance analysis is automated, with threshold-based alerts for budget overruns. Forecasting dashboards allow IT leaders to model scenarios (hiring acceleration, project delays, vendor renegotiation). The platform serves as the single source for IT financial data, eliminating the reconciliation exercise between multiple spreadsheets.

#### The Outcome
- 70% reduction in time spent on monthly/quarterly financial reporting
- Real-time budget visibility replacing month-old snapshots
- Proactive variance management through automated alerts (catch overruns at $50K, not $500K)
- Unified view bridging Finance and IT perspectives, reducing reconciliation effort
- Scenario modeling capability for strategic planning (cloud migration cost projections, vendor consolidation savings)

#### Discovery Questions
1. "How long does it take your team to produce the monthly IT financial report, and how current is the data by the time it reaches leadership?"
2. "How do you currently track and report the 'run the bank' vs. 'change the bank' spending split, and how accurate is that categorization?"
3. "When a project is trending over budget, at what point do you typically identify it — early enough to course-correct, or after it's too late?"
4. "How do you allocate technology costs to business lines, and is that process accepted by the businesses or constantly challenged?"
5. "Do you have the ability to model financial scenarios — like 'what if we accelerate cloud migration by 6 months' — or does that require building a new spreadsheet from scratch?"

#### Industry Context
IT financial management in IB is uniquely complex because of the regulatory dimension. Basel III requires technology costs to be factored into operational risk capital calculations. BCBS 239 (Risk Data Aggregation) has implications for data infrastructure spending. The CIO reports total cost of ownership (TCO) metrics to the board. "Run/change" ratios are benchmarked against peers — top-quartile banks target 60/40 run/change while many are stuck at 75/25. The SE should understand that reducing "run" costs (through platform consolidation, automation, cloud migration) frees budget for "change" — which is where strategic value is created.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Budget & Financial Management system. Create a board called 'IT Financial Tracker' with columns: Cost Item Name (text), Cost Center (text), Category (dropdown: Run the Bank — Infrastructure, Run — Application Maintenance, Run — Licensing, Run — Headcount, Change — Project Delivery, Change — Innovation, Change — Regulatory), Business Line (dropdown: Equities, Fixed Income, Derivatives, FX, Operations, Risk, Compliance, Infrastructure, Shared Services), Vendor (text), Project Link (link to IT Project Portfolio), Annual Budget (numbers, USD), YTD Actual (numbers, USD), YTD Forecast (numbers, USD), Variance Amount (formula: YTD Actual - YTD Forecast), Variance % (formula), Budget Status (status: On Track, Amber — 5-10% Over, Red — >10% Over, Under Budget, Not Started), Q1 Actual (numbers), Q2 Actual (numbers), Q3 Actual (numbers), Q4 Actual (numbers), Budget Owner (people), Finance Partner (people), Notes (long text). Group by Category (Run/Change). Add automations: when Variance % exceeds 10%, change Budget Status to Red and notify Budget Owner and Finance Partner; monthly on the 5th, send reminder to all Budget Owners to review and update forecasts; quarterly, generate snapshot for trend analysis. Create Dashboard with: total budget vs. actual vs. forecast (bar chart by quarter), Run vs. Change split (pie chart for budget and actual), variance by business line (bar chart), top 10 over-budget items (table), spending trend by month (line chart), vendor spend concentration (bar chart top 20 vendors), headcount cost vs. non-headcount (pie chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FinOps IQ — IT Financial Intelligence Agent
**Agent Purpose:** Provide real-time IT financial intelligence, predict budget variances, and automate financial reporting across the technology organization.

**Triggers:**
- Monthly actual spending data import (from finance systems)
- Budget variance exceeds threshold (5% for Tier 1 items, 10% for others)
- Quarterly board report preparation (30 days before quarter-end)
- New vendor contract or renewal exceeding $500K
- Annual budget planning cycle kickoff

**Actions:**
- Auto-calculate variances and generate variance commentary drafts based on known factors (project delays, vendor changes)
- Predict quarter-end and year-end financial position based on current run rate and known future commitments
- Generate monthly CIO financial summary with key metrics, trends, and action items
- Identify cost optimization opportunities (underutilized licenses, redundant vendor services)
- Model scenario impacts (e.g., "what if we consolidate 3 monitoring tools into one?")
- Prepare quarterly board-ready technology investment report

**Data Required:**
- Budget and actuals data from finance systems
- Vendor contract terms and renewal dates
- Project timeline and financial data from IT Project Portfolio
- Headcount data and compensation benchmarks
- Industry benchmarking data for run/change ratios

**Autonomy Level:** Escalation-Based
Autonomous for monitoring, analysis, and report generation. Escalates to human for: budget reallocation decisions, vendor contract negotiations, and board reporting sign-off.

**Example Interaction:**
> During monthly reconciliation, FinOps IQ identifies that cloud infrastructure spending is 23% over forecast for the third consecutive month. It traces the root cause: three projects accelerated their cloud migration timelines without corresponding budget adjustments. It quantifies the full-year impact ($4.2M over budget) and presents three mitigation options: (1) reserve instance commitments for predictable workloads (estimated 30% savings), (2) rightsizing analysis showing 40% of instances are over-provisioned, (3) budget reallocation from delayed on-premise decommissioning projects. The CTO reviews the options and approves a combination of options 1 and 2, with FinOps IQ tracking implementation against a savings target.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Run the Bank (RTB) | Ongoing technology costs to maintain existing operations — infrastructure, support, licensing, maintenance |
| Change the Bank (CTB) | Technology investment in new capabilities — projects, innovation, transformation |
| CAB | Change Advisory Board — the governance body that reviews and approves production changes |
| ITIL | Information Technology Infrastructure Library — the framework governing IT service management practices |
| SLA | Service Level Agreement — contractual performance targets (uptime, response time, resolution time) |
| MTTR | Mean Time to Resolution — average time from incident detection to service restoration |
| RTO/RPO | Recovery Time Objective / Recovery Point Objective — disaster recovery targets for how fast and how completely systems must recover |
| TPRM | Third-Party Risk Management — the program governing vendor oversight and due diligence |
| DORA | Digital Operational Resilience Act — EU regulation requiring financial entities to manage ICT risk comprehensively |
| NYDFS | New York Department of Financial Services — issues cybersecurity regulation (23 NYCRR 500) for financial institutions |
| FFIEC | Federal Financial Institutions Examination Council — issues IT examination guidance for US banks |
| SOX | Sarbanes-Oxley Act — requires controls over financial reporting, including IT change management and access controls |
| BCBS 239 | Basel Committee standard for risk data aggregation and reporting — drives data infrastructure investment |
| CVSS | Common Vulnerability Scoring System — standardized severity scoring for security vulnerabilities |
| CISA KEV | Cybersecurity and Infrastructure Security Agency Known Exploited Vulnerabilities catalog |
| Shadow IT | Technology solutions built or acquired by business lines without IT governance |
| CI/CD | Continuous Integration / Continuous Deployment — automated software delivery pipelines |
| SRE | Site Reliability Engineering — discipline combining software engineering and operations |
| BCP/DR | Business Continuity Planning / Disaster Recovery — frameworks for maintaining operations during disruptions |
| FIX Protocol | Financial Information eXchange — standard electronic communications protocol for securities trading |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CIO / CTO | Overall technology strategy, budget, vendor relationships, regulatory technology compliance | Decision-maker |
| Head of IT Operations / VP Infrastructure | Production stability, incident management, infrastructure, cloud strategy | Decision-maker for operational tools |
| Head of Application Development | Software delivery, development methodology, technical architecture | Decision-maker for development tools |
| CISO (Chief Information Security Officer) | Cybersecurity strategy, vulnerability management, security operations, regulatory compliance | Decision-maker for security tools |
| IT Finance Manager / Controller | Technology budget management, cost allocation, financial reporting | Influencer — controls budget approval process |
| Head of Change Management | Production change governance, CAB process, release management | Key influencer for workflow tools |
| Enterprise Architect | Technology standards, application rationalization, integration strategy | Influencer — defines technology direction |
| Head of IT PMO | Project portfolio management, resource allocation, delivery methodology | Decision-maker for PPM tools |
| Business Line CTO | Technology strategy for specific trading/business area | Influencer / Demand generator |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations | Depends on IT for system stability, automation, and new capabilities | Connected incident management, shared change calendar, Ops workflow automation |
| Risk Management | Requires IT for risk system delivery, data infrastructure, model validation platforms | Risk project tracking, model validation workflows, data quality management |
| Compliance | Needs IT for regulatory reporting systems, surveillance tools, and compliance platforms | Regulatory change management, compliance tool deployment tracking |
| Finance | Manages IT budget allocation, cost reporting, and technology investment governance | Integrated financial tracking, automated cost allocation, investment portfolio views |
| HR | IT supports HR systems and employee technology experience | Employee onboarding technology provisioning, HRIS integration projects |
| Legal | Requires IT for e-discovery, contract management, and legal technology platforms | Legal technology project management, vendor contract workflow integration |
| Front Office | Primary consumer of trading technology, market data, and analytics platforms | Feature request management, trading technology roadmap visibility |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow | Enterprise ITSM market leader; deeply embedded for incident, change, and service management | monday.com offers better UX, faster time-to-value for project/portfolio management and cross-functional workflows. Coexist with ServiceNow for ITSM, displace for PPM and demand management |
| Jira / Atlassian Suite | Developer-centric project management; strong in agile teams | monday.com bridges the gap between developer workflows and business/management visibility. Not replacing Jira for sprint management — adding the portfolio and cross-team orchestration layer above it |
| Planview / Broadcom Clarity | Traditional enterprise PPM tools; expensive, complex, slow to implement | monday.com delivers 80% of PPM functionality at a fraction of the cost and implementation time. Modern UX drives actual adoption vs. shelfware |
| Microsoft Project / Planner | Commodity project management; limited portfolio visibility and automation | monday.com provides significantly richer automation, dashboards, and cross-project visibility |
| Archer / RSA (now Diligent) | GRC platforms for risk management, vendor management, compliance | monday.com is more accessible to front-line users, driving better data quality. Can displace Archer for operational workflows while keeping it for regulatory-specific functions |
| Excel / SharePoint | The universal default for anything not covered by specialized tools | Every Excel tracker is a monday.com board waiting to happen — with governance, automation, and collaboration built in |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have ServiceNow for everything" | ServiceNow excels at ITSM — incident, change, service request. But for project portfolio management, cross-functional workflows, vendor management, and financial tracking, it's often over-engineered and under-adopted. monday.com integrates with ServiceNow and adds the collaboration and visibility layers that ServiceNow struggles with. Many banks run both. |
| "Our developers use Jira and won't switch" | We're not asking them to. Jira is great for sprint-level development work. monday.com sits above Jira as the portfolio and business engagement layer — pulling sprint progress into management dashboards, connecting development work to business outcomes, and managing the non-development aspects of IT delivery (budget, stakeholder communication, vendor coordination). |
| "We need enterprise-grade security and compliance" | monday.com is SOC 2 Type II, ISO 27001, HIPAA-ready, and used by multiple global banks. We support SSO/SAML, SCIM provisioning, data residency options, and comprehensive audit logging. Our security controls are designed for regulated industries. |
| "We can't add another tool — we're trying to consolidate" | That's exactly the point. monday.com replaces 5-10 point solutions and shadow IT spreadsheets with one platform. Every Excel tracker, SharePoint list, and email-based process that your teams use today is fragmentation. Consolidating those into monday.com actually reduces your tool count while improving governance. |
| "The CIO won't approve a 'project management tool'" | Frame it as an AI work platform, not a project management tool. The AI capabilities — intelligent triage, predictive analytics, automated reporting — are what differentiate this from the PPM tools of the past. The CIO cares about delivery velocity, cost optimization, and risk reduction. monday.com delivers all three with measurable ROI within months. |
| "We need on-premise deployment for sensitive data" | monday.com's architecture keeps sensitive data in your core systems (trading platforms, risk engines). What flows through monday.com is workflow metadata — status, ownership, timelines, priorities. The actual trade data, position data, and financial data stays where it is. monday.com orchestrates the work around that data, not the data itself. |

## Proof Points
*(To be populated with customer references)*
- [Global bank consolidating IT project tracking from Excel/SharePoint to monday.com]
- [Financial services firm reducing incident resolution time with monday.com-based war rooms]
- [Investment management firm managing 500+ IT changes weekly through monday.com workflows]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
