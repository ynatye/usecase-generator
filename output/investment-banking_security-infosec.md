# Investment Banking × Security & Infosec Playbook

## Overview

Security and Information Security within investment banking operates under one of the most heavily regulated and threat-targeted environments in global finance. Investment banks handle trillions of dollars in deal flow, M&A advisory mandates, underwriting commitments, and proprietary trading positions — making them prime targets for nation-state actors, sophisticated cybercriminal groups, and insider threats. The Infosec function must protect deal-sensitive MNPI (Material Non-Public Information), ensure compliance with SEC Rule 21F, SOX Section 404, GLBA Safeguards Rule, NYDFS 23 NYCRR 500, and increasingly the EU's DORA (Digital Operational Resilience Act).

The typical security organization in a bulge-bracket or elite boutique bank ranges from 50-300+ professionals spanning SOC (Security Operations Center) analysts, threat intelligence, identity and access management (IAM), application security, GRC (Governance, Risk & Compliance), third-party risk management, and red/purple team specialists. Middle-market banks may have 10-30 security professionals covering broader mandates. Reporting lines vary — CISO may report to CTO, CRO, or directly to the Board's Risk Committee. The function is under constant pressure to demonstrate ROI on security spend (typically 8-12% of IT budget) while managing audit findings, regulatory examinations, and an expanding attack surface driven by cloud migration, API proliferation, and remote/hybrid work models.

Investment banking security teams face unique challenges: managing information barriers (ethical walls) between advisory teams, securing virtual data rooms (VDRs) for live deals, protecting algorithmic trading IP, ensuring secure communication channels for deal teams, and maintaining 24/7 SOC coverage across global time zones (New York, London, Hong Kong, Tokyo). The convergence of operational technology in trading floors, cloud-native development, and third-party fintech integrations creates a complex risk landscape that demands both technical depth and business fluency from the security organization.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Security teams are perpetually understaffed relative to expanding attack surfaces, regulatory mandates, and deal volume. Automation and centralized visibility multiply analyst effectiveness without linear headcount growth. |
| 2 | Replace or Radically Augment Headcount | Medium-High | Tier 1 SOC analysis, access review campaigns, vendor risk questionnaire processing, and audit evidence collection consume massive FTE hours that can be automated or AI-augmented. |
| 3 | Consolidate Tech Stack with AI | Medium | Security teams suffer from tool sprawl (avg. 60-80 tools in enterprise banks). Centralizing workflow orchestration, risk registers, and compliance tracking reduces context-switching and integration maintenance costs. |

## Prioritized Use Cases

---

### Use Case 1: Security Incident Response Orchestration

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks average 1,200+ security alerts per day across SIEM, EDR, DLP, and email gateway systems. Tier 1 SOC analysts spend 70% of their time on triage — opening tickets, enriching indicators, checking threat intel feeds, and routing to the correct response team. Mean time to acknowledge (MTTA) averages 45 minutes; mean time to resolve (MTTR) stretches to 4-6 hours for medium-severity incidents. During live deals (M&A, IPO roadshows), any security incident involving deal team assets triggers mandatory escalation to Legal, Compliance, and the deal sponsor — a process that currently relies on email chains, phone trees, and manual Jira tickets. Missed SLAs on regulatory incident reporting (72 hours under DORA, 36 hours under NYDFS) carry seven-figure fines.

#### The Solution
monday.com Work Management as the central incident response coordination platform. Create a dedicated **Security Incident Board** with structured columns: Incident ID (auto-number), Severity (dropdown: P1-Critical/P2-High/P3-Medium/P4-Low), Status (status: Detected → Triaging → Containing → Eradicating → Recovering → Closed), Affected Systems (tags), Deal Impact (dropdown: Active Deal/No Deal Impact), Assigned Analyst (people), Escalation Required (checkbox), Regulatory Notification Deadline (date + formula), Timeline (timeline for incident duration tracking). Build automations that route based on severity — P1 triggers immediate Slack/Teams notification to CISO and on-call lead, auto-creates a war room sub-item structure (Containment, Evidence Collection, Communication, Post-Mortem). Dashboard views aggregate MTTA/MTTR metrics, open incident counts by severity, and regulatory deadline countdowns. Integration with SIEM (Splunk/Sentinel) via API to auto-create items from high-confidence alerts.

#### The Outcome
Reduce MTTA from 45 minutes to under 10 minutes through automated triage and routing. Cut MTTR by 40% via structured playbook execution. Achieve 100% regulatory notification compliance. Free up 2-3 FTE equivalent of Tier 1 analyst time through automated enrichment and low-severity auto-closure. Provide Board-ready incident metrics dashboards for quarterly Risk Committee reporting.

#### Discovery Questions
1. "How do you currently track the lifecycle of a security incident from detection through post-mortem — is it centralized or spread across SIEM, ticketing, and email?"
2. "When an incident potentially touches a live deal — say an M&A mandate in the pipeline — what's your escalation workflow to Legal and the deal sponsor? How long does that take?"
3. "What's your current MTTA and MTTR, and how confident are you in those numbers? Can you pull them in real-time for a Board presentation?"
4. "How many security tools feed alerts into your SOC, and what percentage of those alerts are false positives that still require human triage?"
5. "Have you had any close calls with regulatory notification deadlines under NYDFS 500 or DORA? What would a miss cost you?"

#### Industry Context
Investment banking SOCs operate under heightened scrutiny because of MNPI exposure. A breach involving deal data can trigger SEC investigation, client litigation, and reputational damage that costs advisory mandates. The concept of "blast radius" is critical — security teams must immediately assess whether compromised systems had access to deal rooms, trading algorithms, or client PII. Many banks still use legacy ITSM tools (ServiceNow, BMC Remedy) that weren't designed for security-specific workflows, leading to process friction and reporting gaps.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Security Incident Response board for an investment bank SOC. Columns: Incident ID (auto-number), Incident Name (text), Severity (dropdown: P1-Critical, P2-High, P3-Medium, P4-Low), Status (status labels: Detected, Triaging, Containing, Eradicating, Recovering, Closed, False Positive), Source System (dropdown: SIEM, EDR, DLP, Email Gateway, User Report, Threat Intel), Affected Assets (text), Deal Impact (dropdown: Active Deal Impacted, No Deal Impact, Under Investigation), Assigned Analyst (people), Escalation Group (people), Regulatory Notification Due (date), MTTA Minutes (numbers), MTTR Hours (numbers), Root Cause (long text), Post-Mortem Link (link). Groups: Active Incidents, Under Investigation, Resolved This Week, Resolved This Month. Automations: When Severity is P1-Critical, notify the Escalation Group and set Regulatory Notification Due to 36 hours from now. When Status changes to Closed, calculate MTTR Hours. When Status changes to False Positive, move to Resolved group. Views: Kanban by Status, Dashboard with average MTTA, average MTTR, incident count by Severity (chart), open incidents timeline."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SOC Triage Commander
**Agent Purpose:** Automatically enrich, classify, and route security incidents based on threat intelligence and deal exposure analysis.

**Triggers:**
- New incident item created (via SIEM integration or manual entry)
- Severity field changed to P1-Critical or P2-High
- Deal Impact field changed to "Active Deal Impacted"
- Status unchanged for >30 minutes (stale incident detection)
- Daily schedule at 06:00 UTC for overnight incident summary

**Actions:**
- Auto-enrich incident with IOC lookups (IP reputation, domain age, hash analysis) and populate Affected Assets field
- Cross-reference Affected Assets against active deal room access logs and flag Deal Impact accordingly
- Route P1/P2 incidents to on-call analyst via rotation schedule; assign backup if primary doesn't acknowledge within 10 minutes
- Generate regulatory notification draft (NYDFS/DORA template) when Deal Impact = Active Deal Impacted
- Produce daily incident summary with trends, false positive rate, and analyst workload distribution
- Escalate stale incidents to SOC Lead with recommended next steps

**Data Required:**
- SIEM alert feed (Splunk/Sentinel API)
- Threat intelligence platform (Recorded Future, Mandiant)
- Active deal registry (deal names, VDR access lists, deal team members)
- On-call rotation schedule
- Historical incident data for pattern matching

**Autonomy Level:** Human-in-the-Loop
Auto-enrichment and classification run fully autonomously. P3/P4 incidents with known signatures can be auto-closed. P1/P2 incidents and anything flagged as deal-impacting require human confirmation before containment actions are executed. Regulatory notifications are drafted but require CISO approval before submission.

**Example Interaction:**
> At 2:47 AM EST, the SOC Triage Commander agent detects a new P2-High alert from the SIEM: suspicious lateral movement from a workstation in the Healthcare M&A advisory team's VLAN. The agent immediately enriches the alert — the source IP maps to a contractor laptop, the destination is a file server hosting VDR preparation documents for a $3.2B acquisition. The agent cross-references the deal registry and flags "Deal Impact: Active Deal Impacted — Project Evergreen." It auto-assigns the incident to Sarah Chen (on-call analyst, NYC shift), sends a Teams notification to the CISO and Deputy General Counsel, and begins drafting a NYDFS 72-hour notification template. Within 8 minutes of detection, the full incident context is assembled and the response team is mobilized — a process that previously took 45+ minutes of manual correlation across four different tools.

---

### Use Case 2: Third-Party / Vendor Risk Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banks maintain relationships with 500-2,000+ third-party vendors spanning market data providers (Bloomberg, Refinitiv), cloud infrastructure (AWS, Azure), custodians, prime brokers, legal counsel, and fintech partners. NYDFS 23 NYCRR 500.11 and OCC guidance require risk assessment of every vendor with access to NPI (Nonpublic Information). The typical vendor risk assessment involves a 200-400 question questionnaire (SIG Lite or custom), SOC 2 report review, penetration test result analysis, and ongoing monitoring. A team of 3-5 TPRM analysts can process 15-25 assessments per month — against an annual review requirement of 500+ vendors. The result: assessment backlogs of 6-12 months, stale risk ratings, and audit findings that invite regulatory scrutiny.

#### The Solution
monday.com as the centralized TPRM lifecycle platform. **Vendor Registry Board** with columns: Vendor Name (text), Risk Tier (dropdown: Critical/High/Medium/Low), Service Category (dropdown: Market Data, Cloud, Legal, Trading, Operations), Data Access Level (dropdown: MNPI, Client PII, Public Only), Last Assessment Date (date), Next Assessment Due (date), Assessment Status (status: Not Started → Questionnaire Sent → Under Review → Risk Rated → Approved → Remediation Required), Risk Score (numbers 0-100), SOC 2 Expiry (date), Primary Contact (people), Relationship Owner (people). Sub-items for each assessment cycle contain individual control findings. Automations send questionnaire reminders 30 days before due date, escalate overdue assessments to CISO, and trigger reassessment when vendor risk tier changes. Dashboard shows vendor risk heat map, assessment completion rate, overdue count, and tier distribution.

#### The Outcome
Increase assessment throughput by 3x (from 20 to 60+ per month) through templated workflows and automated follow-up. Eliminate assessment backlog within 2 quarters. Achieve 100% on-time annual review completion for Critical and High-tier vendors. Reduce audit findings related to TPRM by 80%. Save $400K-600K annually in consultant/contractor costs for assessment surge capacity.

#### Discovery Questions
1. "How many third-party vendors do you currently maintain, and what percentage have a current risk assessment on file?"
2. "What's your average time from questionnaire issuance to completed risk rating? How many rounds of follow-up does it typically take?"
3. "Have your regulators or auditors flagged TPRM gaps in recent examinations? What was the remediation commitment?"
4. "How do you handle vendor concentration risk — do you have visibility into which critical business processes depend on a single vendor?"
5. "When a vendor has a public breach (like the MOVEit incident), how quickly can you determine your exposure and notify stakeholders?"

#### Industry Context
Investment banking TPRM is uniquely high-stakes because vendor compromise can expose deal data, trading strategies, or client information that moves markets. The SolarWinds and MOVEit breaches demonstrated that supply chain attacks target financial services disproportionately. Banks face examiner scrutiny from multiple regulators (OCC, NYDFS, SEC, FCA) with overlapping but inconsistent TPRM requirements. Fourth-party risk (your vendor's vendors) is an emerging concern that most banks haven't operationalized. The SIG (Standardized Information Gathering) questionnaire from Shared Assessments is industry standard, but response quality varies wildly and review is highly manual.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Third-Party Vendor Risk Management board for an investment bank. Columns: Vendor Name (text), Risk Tier (dropdown: Critical, High, Medium, Low), Service Category (dropdown: Market Data, Cloud Infrastructure, Trading Technology, Legal Services, Operations, Consulting, Facilities), Data Access (dropdown: MNPI Access, Client PII, Internal Only, Public Data), Contract Value (numbers, USD), Relationship Owner (people), TPRM Analyst (people), Assessment Status (status: Not Started, Questionnaire Sent, Responses Received, Under Review, Risk Rated, Approved, Remediation Required, On Hold), Risk Score (numbers 0-100), Last Assessment Date (date), Next Assessment Due (date), SOC 2 Report Expiry (date), Findings Count (numbers), Remediation Items (numbers). Groups: Critical Tier, High Tier, Medium Tier, Low Tier. Sub-items for each vendor: individual control findings with Finding Description (text), Severity (dropdown: Critical, High, Medium, Low), Remediation Status (status: Open, In Progress, Remediated, Accepted Risk), Due Date (date). Automations: When Next Assessment Due is 30 days away, notify TPRM Analyst. When Assessment Status is Questionnaire Sent for more than 14 days, send reminder and notify Relationship Owner. When SOC 2 Report Expiry is within 30 days, create notification. Views: Dashboard with risk score distribution chart, assessment completion percentage, overdue assessments count, vendors by tier (pie chart), upcoming deadlines calendar."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Vendor Risk Analyst AI
**Agent Purpose:** Automate vendor questionnaire analysis, risk scoring, and continuous monitoring to eliminate assessment backlogs.

**Triggers:**
- Vendor questionnaire responses received (file uploaded or form submitted)
- SOC 2 report uploaded for review
- Vendor appears in threat intelligence breach notification
- Assessment Status changes to "Under Review"
- Monthly schedule for continuous monitoring sweep

**Actions:**
- Parse completed SIG questionnaire responses and auto-score against bank's control framework (flag gaps, calculate risk score)
- Analyze SOC 2 Type II report — extract exceptions, qualified opinions, and complementary user entity controls (CUECs)
- Cross-reference vendor name against breach databases, OFAC sanctions, and negative news feeds
- Generate risk assessment summary with recommended risk tier, key findings, and remediation requirements
- Auto-create sub-item findings for each control gap identified
- Alert TPRM team and Relationship Owner when a monitored vendor appears in a breach notification

**Data Required:**
- SIG questionnaire template and scoring rubric
- SOC 2 reports (PDF parsing)
- Threat intelligence feeds (vendor breach monitoring)
- Bank's control framework mapping
- Historical assessment data for benchmarking

**Autonomy Level:** Human-in-the-Loop
Questionnaire parsing and initial scoring are fully automated. Risk tier recommendations for Medium/Low vendors can be auto-approved. Critical and High tier vendors require analyst review and sign-off. Breach notifications are auto-generated but remediation decisions require human judgment.

**Example Interaction:**
> The Vendor Risk Analyst AI receives a completed 350-question SIG Lite questionnaire from CloudTrade Systems, a Critical-tier vendor providing algorithmic trade execution infrastructure. Within 12 minutes, the agent has parsed all responses, identified 14 control gaps (3 High: no MFA on admin consoles, 90-day patch cycle instead of 30-day, no annual penetration test), cross-referenced against the vendor's SOC 2 Type II (which had 2 exceptions related to change management), and generated a risk score of 72/100 — down from 81 at last assessment. The agent creates the risk assessment summary, populates 14 sub-item findings with severity ratings and recommended remediation timelines, and notifies TPRM analyst Mike Torres that CloudTrade's risk tier may need elevation from "Critical — Approved" to "Critical — Remediation Required." Mike reviews the AI's analysis in 20 minutes instead of the usual 6-8 hours of manual review.

---

### Use Case 3: Information Barrier (Ethical Wall) Monitoring & Compliance

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks are legally required to maintain information barriers (Chinese walls) between advisory teams working on conflicting mandates, between research and banking, and between proprietary trading and client-facing divisions. Managing these barriers involves controlling physical access (floor/room restrictions), logical access (email DLP rules, shared drive permissions, VDR access), and communication monitoring. When a new deal is announced internally ("over the wall"), Compliance must rapidly update barrier configurations across 10+ systems — Active Directory groups, email transport rules, Bloomberg terminal permissions, collaboration tools, and physical badge access. A single miss can result in MNPI leakage, SEC enforcement action, and deal collapse. Current processes involve spreadsheets, email requests to IT, and manual verification — taking 24-48 hours to fully implement a new barrier.

#### The Solution
monday.com as the Information Barrier management and tracking system. **Deal Barrier Board** with columns: Deal Code Name (text), Deal Type (dropdown: M&A Buy-Side, M&A Sell-Side, IPO, Debt Offering, Restructuring), Status (status: Pre-Engagement → Active → Over the Wall → Closed/Archived), Restricted List Date (date), Wall-Crossed Personnel (people), Barrier Systems (tags: AD, Email DLP, Bloomberg, VDR, Physical, Collaboration), Implementation Status (status per system as sub-items), Compliance Officer (people), Verification Date (date). Sub-items track each system's barrier implementation with screenshot evidence. Automations trigger barrier implementation checklists when deal status changes, send daily verification reminders until all systems confirmed, and alert Compliance leadership if any system remains unconfirmed after 4 hours. Dashboard provides real-time barrier status across all active deals.

#### The Outcome
Reduce barrier implementation time from 24-48 hours to under 4 hours. Achieve 100% documented verification across all systems. Eliminate spreadsheet-based tracking that creates audit trail gaps. Provide real-time compliance dashboard for regulatory examinations. Reduce risk of inadvertent MNPI leakage from barrier configuration errors by 90%.

#### Discovery Questions
1. "How many active information barriers are you managing at any given time, and how do you track which personnel are wall-crossed on which deals?"
2. "When a new deal kicks off and barriers need to go up, how many systems need to be configured and how long does end-to-end implementation take?"
3. "Have you ever had an audit finding or near-miss related to information barrier gaps? What was the root cause?"
4. "How do you verify that barriers are actually effective — do you have ongoing monitoring or is it point-in-time checks?"
5. "What happens when a deal closes or falls apart — how quickly are barriers taken down and access normalized?"

#### Industry Context
Information barriers are a cornerstone of investment banking compliance, mandated by SEC regulations (Section 15(g) of the Securities Exchange Act), MiFID II, and individual firm policies. The SEC's enforcement actions related to MNPI leakage have increased 40% since 2020, with average fines exceeding $10M. The complexity multiplies in large banks where a single banker may be wall-crossed on multiple deals simultaneously, requiring matrix-level barrier management. The rise of collaboration tools (Teams, Slack) and cloud storage has made barrier management significantly more complex than the physical-separation models of the past.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Information Barrier Tracking board for investment banking compliance. Columns: Deal Code Name (text), Deal Type (dropdown: M&A Buy-Side, M&A Sell-Side, IPO, Debt Offering, Restructuring, PIPE, Block Trade), Barrier Status (status: Pre-Engagement, Active, Modifications Pending, Closed/Teardown, Archived), Restricted List Added (date), Wall-Crossed Count (numbers), Compliance Officer (people), Deal Sponsor (people), Implementation Deadline (date), All Systems Confirmed (checkbox), Verification Date (date), Notes (long text). Groups: Active Barriers, Pending Implementation, Teardown in Progress, Archived. Sub-items for each barrier system: System Name (dropdown: Active Directory, Email DLP, Bloomberg Terminal, VDR Platform, Physical Badge Access, Teams/Slack, Shared Drives, CRM), Configuration Status (status: Pending, Configured, Verified, Failed), Configured By (people), Evidence (file), Timestamp (date). Automations: When Barrier Status changes to Active, create sub-items for all 8 systems with status Pending. When any sub-item Configuration Status is Pending for more than 4 hours, notify Compliance Officer as urgent. When all sub-items are Verified, check All Systems Confirmed. When Barrier Status changes to Closed/Teardown, create reverse teardown sub-items. Views: Dashboard with active barriers count, systems pending configuration, average implementation time, overdue items, Kanban by Barrier Status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Ethical Wall Guardian
**Agent Purpose:** Monitor information barrier integrity in real-time and orchestrate rapid implementation/teardown of cross-system access controls.

**Triggers:**
- New deal item created with Barrier Status = Active
- Barrier Status changed to Closed/Teardown
- Sub-item Configuration Status remains "Pending" for >2 hours
- Daily verification scan at 07:00 and 19:00 UTC
- Personnel changes on wall-crossed list (people column updated)

**Actions:**
- Generate system-specific barrier configuration instructions for each sub-item (AD group changes, DLP rule templates, Bloomberg entitlement requests)
- Monitor email and collaboration tool logs for potential barrier violations (communication between restricted parties)
- Send escalation alerts with specific barrier gap details to Compliance Officer
- Auto-generate regulatory-ready barrier implementation report with timestamps and evidence
- Track personnel across multiple deals and flag conflicts (same person wall-crossed on competing mandates)
- Initiate teardown verification checklist when deals close

**Data Required:**
- Active deal registry with wall-crossed personnel lists
- Active Directory group membership data
- Email DLP rule configurations
- Bloomberg entitlement system access
- Physical access control system (badge reader logs)
- Collaboration tool (Teams/Slack) channel membership

**Autonomy Level:** Escalation-Based
Monitoring and alerting are fully autonomous. Configuration instruction generation is automated but implementation requires IT team execution. Violation alerts are automatically escalated to Compliance — no human approval needed for alerts. Barrier modifications (adding/removing personnel) require Compliance Officer approval.

**Example Interaction:**
> At 3:15 PM, Managing Director Lisa Park is added to the wall-crossed list for Project Neptune (a $5.8B cross-border M&A mandate). The Ethical Wall Guardian immediately generates barrier configuration requests for all 8 systems: AD group addition to "Neptune_Restricted," email DLP rule update to block communication with the target company's known domains, Bloomberg terminal restriction on target company securities, VDR access provisioning, and physical badge restriction to the 42nd floor deal room. Each request is created as a sub-item with specific technical instructions. By 5:30 PM, 7 of 8 systems show "Configured" — but Physical Badge Access remains "Pending." The agent sends an urgent notification to the Compliance Officer and the Facilities Security team: "ALERT: Physical access restriction for Lisa Park (Project Neptune) has not been confirmed after 2 hours. Badge access to floors 38-40 (where conflicting mandate Project Aurora is housed) remains unrestricted. Immediate action required." The issue is resolved within 30 minutes, and the agent logs the complete implementation timeline with timestamps for audit purposes.

---

### Use Case 4: Regulatory Compliance & Audit Evidence Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banks face examinations from 4-8 regulators annually (SEC, FINRA, OCC, NYDFS, FCA, BaFin, MAS, HKMA depending on jurisdictions). Each examination involves hundreds of document requests (RFIs — Requests for Information), evidence collection across multiple departments, and strict response deadlines. The security/infosec team is typically responsible for 30-50% of all RFI items across examinations. Evidence is scattered across ticketing systems, shared drives, email archives, and individual analysts' machines. A typical regulatory examination consumes 2,000-4,000 person-hours over 8-12 weeks. Internal audit conducts its own testing cycles (SOX 404, NIST CSF assessments) with similar evidence demands. The result: security team members spend 25-35% of their time on audit support rather than actual security operations.

#### The Solution
monday.com as the centralized audit and examination management platform. **Regulatory Examination Board** with columns: Regulator (dropdown: SEC, FINRA, OCC, NYDFS, FCA, etc.), Examination Type (dropdown: Targeted, Routine, Sweep, For Cause), RFI Number (text), RFI Description (long text), Assigned Owner (people), Department (dropdown), Status (status: Received → Gathering Evidence → Under Review → Submitted → Follow-Up Required → Closed), Due Date (date), Submitted Date (date), Evidence Files (file), Reviewer (people), Quality Check (checkbox). Automations send daily digest of upcoming deadlines, escalate items due within 48 hours, and notify department heads of overdue items. Template boards for common examination types pre-populate standard RFIs. Dashboard tracks submission rate, on-time percentage, outstanding items by department, and examiner feedback.

#### The Outcome
Reduce per-examination effort by 40% (800-1,600 person-hours saved) through templated evidence collection and automated tracking. Achieve 98%+ on-time RFI submission rate. Build reusable evidence library that reduces future collection time by 60%. Free 1-2 FTE equivalent of security analyst time from audit support back to security operations. Demonstrate examination readiness to regulators, improving institutional credibility and reducing examination frequency/intensity.

#### Discovery Questions
1. "How many regulatory examinations did your security team support last year, and roughly how many person-hours did each consume?"
2. "Where does your examination evidence currently live — is it centralized or do you recreate evidence packages from scratch each time?"
3. "What's your on-time RFI submission rate? When items are late, what's the root cause — is it collection, review, or approval?"
4. "Do you have a reusable evidence library, or does every examination feel like starting from zero?"
5. "How do you track remediation commitments from examination findings — MRAs (Matters Requiring Attention) and MRIAs (Matters Requiring Immediate Attention)?"

#### Industry Context
Regulatory examination management is a massive hidden cost in investment banking. The concept of "examination readiness" — being perpetually prepared rather than scrambling when examiners arrive — is aspirational for most banks. MRAs and MRIAs from OCC examinations carry enforcement consequences if not remediated on time. SEC examination priorities are published annually and increasingly focus on cybersecurity controls, operational resilience, and third-party risk. The trend toward continuous supervision (real-time regulatory monitoring) means banks need persistent evidence repositories rather than point-in-time collection.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Regulatory Examination Management board for an investment bank's security team. Columns: Examination ID (auto-number), Regulator (dropdown: SEC, FINRA, OCC, NYDFS, FCA, BaFin, MAS, HKMA, Internal Audit), Exam Type (dropdown: Routine, Targeted, Sweep, For Cause, SOX 404, NIST Assessment), RFI Number (text), RFI Description (long text), Control Domain (dropdown: Access Management, Incident Response, Data Protection, Network Security, Change Management, Business Continuity, Third-Party Risk, Encryption, Logging & Monitoring), Assigned Owner (people), Reviewer (people), Status (status: Received, Evidence Gathering, Draft Ready, Under Review, Approved, Submitted, Follow-Up, Closed), Priority (dropdown: Critical, High, Standard), Due Date (date), Submitted Date (date), Evidence Package (file), Quality Approved (checkbox), Examiner Feedback (long text). Groups by examination: SEC 2026 Routine, OCC Targeted Cyber, NYDFS Annual, Internal SOX. Automations: When Due Date is 48 hours away and Status is not Submitted, notify Assigned Owner and escalate to CISO. When Status changes to Submitted, set Submitted Date to today. When Quality Approved is checked, change Status to Approved. Views: Calendar view of all due dates, Dashboard with submission rate percentage, items by status (chart), overdue items count, items by control domain (chart), timeline view of examination lifecycle."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Examination Response Coordinator
**Agent Purpose:** Automate evidence collection, track RFI status across examinations, and maintain an evergreen evidence library for rapid regulatory response.

**Triggers:**
- New RFI item created (manual or bulk import from examination letter)
- Status unchanged at "Evidence Gathering" for >3 business days
- Due Date within 72 hours with Status not "Submitted"
- New examination board created from template
- Weekly summary schedule (Monday 09:00 EST)

**Actions:**
- Match RFI descriptions to evidence library and auto-attach relevant artifacts from previous examinations
- Identify evidence gaps and create collection tasks assigned to appropriate system owners
- Generate weekly status report for CISO with submission metrics, risk items, and projected completion timeline
- Auto-populate standard RFIs from template when new examination is created
- Track examiner follow-up questions and link to original RFI items
- Build and maintain evidence library index with freshness scoring (flag stale evidence >90 days)

**Data Required:**
- Historical examination RFIs and submitted evidence
- Evidence library (centralized document repository)
- Control framework mapping (NIST CSF, ISO 27001, CIS)
- Team directory for auto-assignment
- Examination calendar and regulatory contacts

**Autonomy Level:** Human-in-the-Loop
Evidence matching and preliminary attachment are automated. RFI response drafts are auto-generated but require owner review and approval before submission. Escalation notifications are fully autonomous. Evidence library maintenance runs autonomously with quarterly human review.

**Example Interaction:**
> The SEC sends a routine examination letter with 127 RFI items. The Examination Response Coordinator agent bulk-imports all items, parses each description, and maps them to NIST CSF control domains. Within 2 hours, the agent has matched 89 of 127 items (70%) to evidence artifacts from the previous year's examination — attaching SOC logs, policy documents, access review reports, and penetration test summaries. For the remaining 38 items, it creates targeted collection tasks: "RFI-47 requests evidence of quarterly access reviews for privileged accounts — assigning to IAM Lead Jennifer Wu, pulling last 4 quarterly review exports from CyberArk." The CISO receives a dashboard showing 70% pre-populated, 30% in collection, with projected full completion in 18 business days versus the 30-day deadline. What previously took 3 weeks of scrambling is now a structured, trackable process from day one.

---

### Use Case 5: Security Awareness & Phishing Simulation Campaign Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banking employees — from analysts to managing directors — are prime targets for spear-phishing, business email compromise (BEC), and social engineering attacks. Threat actors research deal teams via LinkedIn, press releases, and SEC filings to craft highly targeted lures ("Project Neptune closing documents attached"). Banks are required to conduct security awareness training (GLBA, NYDFS 500.14) and phishing simulations quarterly at minimum. Managing these campaigns involves coordinating with HR for employee lists, segmenting by division/seniority, designing realistic templates, scheduling sends across time zones, tracking results, managing remediation training for failures, and reporting to Compliance. With 5,000-50,000+ employees across global offices, this is a logistical challenge that typically requires 1-2 dedicated FTEs plus vendor management (KnowBe4, Proofpoint, Cofense).

#### The Solution
monday.com as the campaign management layer on top of phishing simulation tools. **Phishing Campaign Board** with columns: Campaign Name (text), Campaign Type (dropdown: Credential Harvest, Attachment, Link Click, BEC Simulation, Vishing), Target Segment (dropdown: All Employees, Banking Division, Trading, Operations, Executive, New Hires), Target Count (numbers), Status (status: Planning → Template Design → Approval → Scheduled → Active → Analysis → Remediation → Complete), Launch Date (date), End Date (date), Click Rate (numbers %), Report Rate (numbers %), Failure Count (numbers), Remediation Assigned (numbers), Campaign Owner (people). Sub-items track individual cohort results. Automations trigger remediation training assignment when click rate exceeds threshold, notify managers of repeat offenders, and generate quarterly Board reporting.

#### The Outcome
Reduce campaign management overhead by 50% through templated workflows. Decrease firm-wide phishing click rate from 12% to under 4% within 12 months. Achieve 100% completion rate for remediation training. Provide granular risk scoring by division for targeted security investment. Automate quarterly compliance reporting that previously required 20+ hours of manual data aggregation.

#### Discovery Questions
1. "What's your current phishing simulation click rate, and how does it vary by division — are bankers more susceptible than operations staff?"
2. "How do you handle repeat offenders — people who fail multiple simulations? Is there an escalation path to their managers?"
3. "How long does it take to plan, execute, and report on a single phishing campaign from start to finish?"
4. "Do you segment campaigns by sophistication level — basic for general staff, advanced spear-phishing for executives and deal teams?"
5. "Can you show me how you report security awareness metrics to the Board or Risk Committee? How much manual work goes into that report?"

#### Industry Context
Investment banking phishing attacks are uniquely dangerous because successful compromise can lead to MNPI theft, wire fraud (BEC attacks targeting deal closings have resulted in $50M+ losses), and unauthorized trading. Deal-themed lures are extremely effective because bankers are conditioned to open urgent attachments from counterparties. The SEC has specifically called out phishing resilience in examination priorities. Regulatory expectations include not just training delivery but demonstrable improvement in employee behavior over time. Vishing (voice phishing) targeting executive assistants who manage MDs' calendars and travel is an emerging threat vector.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Security Awareness & Phishing Campaign Management board. Columns: Campaign Name (text), Campaign Type (dropdown: Credential Harvest, Malicious Attachment, Link Click, BEC Simulation, QR Code, Vishing, SMS Phishing), Target Segment (dropdown: All Employees, Investment Banking Division, Sales & Trading, Operations, Technology, Executive Leadership, New Hires <90 Days), Target Employee Count (numbers), Status (status: Planning, Template Design, Legal/Compliance Approval, Scheduled, Active, Data Collection, Analysis, Remediation Tracking, Complete), Launch Date (date), End Date (date), Emails Sent (numbers), Emails Opened (numbers %), Links Clicked (numbers %), Credentials Submitted (numbers %), Reported to SOC (numbers %), Remediation Required (numbers), Remediation Complete (numbers), Campaign Owner (people), Approver (people). Groups: Q1 2026 Campaigns, Q2 2026 Campaigns, Q3 2026 Campaigns, Q4 2026 Campaigns. Automations: When Links Clicked percentage exceeds 15, notify CISO. When Status changes to Complete, calculate all percentage columns. When Remediation Required is greater than 0, create sub-items for each cohort needing training. Views: Dashboard with click rate trend over time (line chart), click rate by segment (bar chart), report rate trend, remediation completion rate, calendar view of upcoming campaigns."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Phishing Campaign Strategist
**Agent Purpose:** Design targeted phishing simulation campaigns using current threat intelligence and analyze results to improve organizational resilience.

**Triggers:**
- Quarterly campaign planning date reached
- Campaign Status changes to "Analysis"
- New employee cohort onboarded (>25 new hires)
- Real phishing attempt detected by email gateway (use as template inspiration)
- Annual reporting deadline approaching

**Actions:**
- Generate campaign templates based on current threat landscape (real-world IB phishing lures, active BEC campaigns)
- Segment employee population and recommend targeting based on historical failure rates and risk exposure
- Analyze campaign results: identify patterns (department, seniority, time of day, template type) and generate insights report
- Auto-assign remediation training to employees who clicked, with escalation path for 3+ time repeat offenders
- Generate Board-ready quarterly security awareness report with trends, benchmarks, and recommendations
- Recommend campaign calendar optimization based on employee fatigue patterns and regulatory requirements

**Data Required:**
- Employee directory with department, seniority, location, hire date
- Historical phishing simulation results
- Real-world threat intelligence (phishing lure samples)
- Remediation training completion records
- Industry benchmark data for comparison

**Autonomy Level:** Human-in-the-Loop
Campaign template generation and result analysis are automated. Campaign scheduling and template approval require Compliance sign-off. Remediation training assignment is automated. Manager notifications for repeat offenders are automated. Board reports are generated but require CISO review before distribution.

**Example Interaction:**
> It's the start of Q2, and the Phishing Campaign Strategist agent begins planning the quarterly simulation. It analyzes Q1 results: the Investment Banking Division had a 14% click rate on BEC-themed lures (2x the firm average), while Trading had the highest report-to-SOC rate at 45%. The agent reviews current threat intelligence — there's been a surge in AI-generated voice cloning attacks targeting IB executive assistants. It designs three campaigns: (1) A BEC simulation targeting IBD with a fake "deal amendment" attachment from a known law firm, (2) A credential harvest targeting Operations with a fake "benefits enrollment" page, and (3) A vishing simulation targeting 50 executive assistants with AI-cloned voice messages requesting calendar access. The agent presents the campaign plan to the CISO with expected impact, resource requirements, and recommended send windows (Tuesday-Thursday, 10 AM-2 PM local time, when click rates historically peak). Total planning time: 45 minutes instead of 2 weeks.

---

### Use Case 6: Security Policy Lifecycle & Exception Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banks maintain 50-100+ security policies, standards, and procedures covering everything from acceptable use to cryptographic key management. These documents require annual review, version control, stakeholder approval chains (CISO → CRO → Board Risk Committee for Tier 1 policies), and exception management. Policy exceptions — when a business unit cannot comply with a control (e.g., a legacy trading system that can't support MFA) — require risk acceptance documentation, compensating controls, and time-bound remediation plans. Most banks manage this through SharePoint document libraries, email approval chains, and spreadsheet-based exception trackers. The result: policies go stale, exceptions pile up without remediation, and audit reveals gaps between documented policy and actual practice.

#### The Solution
monday.com as the policy lifecycle and exception management platform. **Policy Registry Board** with columns: Policy Name (text), Policy ID (text), Category (dropdown: Access Control, Data Protection, Incident Response, Network Security, etc.), Owner (people), Approver (people), Version (text), Status (status: Draft → Review → Approved → Published → Under Revision → Retired), Last Review Date (date), Next Review Due (date), Document (file). **Exception Management Board** linked via connect boards: Exception ID (auto-number), Related Policy (connect board), Requesting Business Unit (dropdown), Exception Description (long text), Risk Level (dropdown), Compensating Controls (long text), Approval Status (status), Expiration Date (date), Remediation Plan (long text). Automations flag policies due for review 60 days in advance, escalate overdue reviews, and alert when exceptions approach expiration.

#### The Outcome
Achieve 100% on-time policy review completion (up from typical 60-70%). Reduce average policy review cycle from 45 days to 15 days through automated routing. Maintain auditable exception inventory with zero expired/unreviewed exceptions. Eliminate the "policy graveyard" problem where documents exist but aren't actively maintained. Provide instant policy compliance dashboard for examiner requests.

#### Discovery Questions
1. "How many security policies do you currently maintain, and what percentage were reviewed on schedule in the last 12 months?"
2. "How do you manage the approval workflow for policy updates — is it email-based or do you have a structured workflow?"
3. "How many active security exceptions do you have, and do you have confidence that all have current compensating controls and remediation timelines?"
4. "When a regulator asks 'show me your access control policy and its revision history,' how quickly can you produce that?"
5. "Have you experienced situations where documented policy didn't reflect actual practice? How did you discover the gap?"

#### Industry Context
Regulatory expectations for policy management in investment banking are explicit and prescriptive. NYDFS 500.03 requires a written cybersecurity policy approved by a Senior Officer or the Board. OCC heightened standards (12 CFR 30) mandate Board oversight of information security policies. Examiners routinely request policy documents, revision histories, and exception logs as foundational evidence. The gap between "policy on paper" and "policy in practice" is a top audit finding category. Policy exception management is particularly fraught — compensating controls degrade over time, and exceptions that were temporary become permanent without active tracking.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Security Policy Lifecycle Management board. Columns: Policy Name (text), Policy ID (text), Category (dropdown: Access Management, Data Protection, Incident Response, Network Security, Encryption, Change Management, Business Continuity, Acceptable Use, Third-Party, Physical Security, Cloud Security), Tier (dropdown: Tier 1 Board Approved, Tier 2 CISO Approved, Tier 3 Department Approved), Owner (people), Primary Reviewer (people), Approver (people), Current Version (text), Status (status: Draft, Under Review, Pending Approval, Approved, Published, Revision Needed, Retired), Last Review (date), Next Review Due (date), Document Link (link), Change Summary (long text). Groups: Published Policies, Under Review, Drafts, Retired. Automations: When Next Review Due is 60 days away, notify Owner. When Next Review Due is 30 days away, notify Owner and Approver. When Next Review Due has passed, mark Status as Revision Needed and notify CISO. When Status changes to Approved, update Last Review to today and Next Review Due to one year from today. Views: Calendar of review dates, Dashboard with policies by status (pie chart), overdue reviews count, policies by category (bar chart), upcoming reviews in 30/60/90 days."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Policy Compliance Sentinel
**Agent Purpose:** Manage security policy review cycles, track exceptions, and ensure continuous alignment between documented policy and operational reality.

**Triggers:**
- Policy Next Review Due within 60 days
- New exception request submitted
- Exception Expiration Date within 30 days
- Policy Status changed to "Published" (trigger distribution)
- Quarterly policy health report schedule

**Actions:**
- Generate policy review summary highlighting regulatory changes since last review that may require policy updates
- Route review and approval workflows based on policy tier (Tier 1 → Board, Tier 2 → CISO, Tier 3 → Department Head)
- Monitor exception portfolio: flag expired exceptions, assess compensating control adequacy, recommend remediation priorities
- Compare policy requirements against operational evidence (audit logs, configuration data) to identify policy-practice gaps
- Generate quarterly policy health report: review completion rate, exception inventory, gap analysis, regulatory mapping updates
- Auto-distribute updated policies to affected employee groups with acknowledgment tracking

**Data Required:**
- Policy document repository with version history
- Regulatory change feeds (SEC, OCC, NYDFS, FCA rule updates)
- Exception register with compensating control documentation
- Audit findings and remediation tracking data
- Employee acknowledgment records

**Autonomy Level:** Escalation-Based
Review reminders and routing are fully autonomous. Regulatory change impact analysis is automated with human review. Exception expiration alerts are automatic. Policy-practice gap identification flags issues for human investigation. Board-level policy approvals obviously require human decision-making.

**Example Interaction:**
> The Policy Compliance Sentinel detects that the "Remote Access Security Standard" (Policy SEC-024, Tier 2) is due for annual review in 58 days. It analyzes regulatory changes since the last review: NYDFS has updated 23 NYCRR 500.12 to require enhanced MFA requirements for remote access to NPI systems, effective January 2027. The agent drafts a review summary: "Recommended Updates: (1) Add requirement for phishing-resistant MFA (FIDO2/WebAuthn) for all remote access — aligns with updated 500.12. (2) Remove exception allowance for SMS-based MFA — no longer meets regulatory bar. (3) Add section on BYOD conditional access policies reflecting hybrid work model." It notifies policy owner David Kim with the summary and pre-populates a revision checklist. David's review time drops from 2 weeks of research to 3 days of validation and refinement.

---

### Use Case 7: Security Metrics & Executive Risk Reporting

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
CISOs in investment banks report to Boards, Risk Committees, and senior management on a quarterly (sometimes monthly) basis. Creating these reports requires aggregating data from 15-20+ security tools (SIEM, vulnerability scanner, EDR, IAM, DLP, TPRM, training platform), normalizing metrics, adding context and trend analysis, and formatting for executive consumption. A single quarterly Board report takes 40-80 hours to produce — pulling data, building charts, writing narrative, getting reviews, and iterating on feedback. The data is often stale by the time it reaches the Board (2-3 weeks from collection to presentation). Meanwhile, operational teams lack real-time visibility into how their daily work maps to strategic risk metrics. There's a fundamental disconnect between operational data and executive risk communication.

#### The Solution
monday.com Dashboards as the real-time security metrics and reporting layer. Create a **CISO Dashboard** that aggregates data across all security operational boards (Incident Response, TPRM, Policy Management, Phishing Campaigns, Vulnerability Management). Key widgets: Open P1/P2 incidents (number), MTTR trend (chart), Vendor risk distribution (pie chart), Policy review compliance (percentage), Phishing click rate trend (line chart), Audit RFI completion rate (progress bar), Exception count by risk level (stacked bar), Top 10 risk items (table). Build a separate **Board Reporting Dashboard** with simplified, color-coded views designed for non-technical audiences. Automate monthly data snapshots for trend analysis. Use monday.com docs for narrative context alongside data visualizations.

#### The Outcome
Reduce Board report preparation from 40-80 hours to under 8 hours (80-90% reduction). Provide real-time risk visibility to CISO and security leadership — no more waiting for quarterly reports. Enable data-driven resource allocation decisions based on actual operational metrics. Improve Board confidence in security posture through consistent, timely, and transparent reporting. Create a single source of truth that eliminates "which spreadsheet has the latest numbers?" debates.

#### Discovery Questions
1. "How long does it take your team to produce a quarterly Board security report, and how many people are involved?"
2. "How many different tools do you pull data from for executive reporting? Is any of that automated or is it all manual extraction?"
3. "When the Board asks 'what's our current risk posture?' — can you answer in real-time or do you need to go research?"
4. "Do your operational teams see how their daily work connects to the metrics the CISO reports to the Board?"
5. "Has the Board ever challenged the timeliness or accuracy of security metrics you've presented?"

#### Industry Context
Board-level cybersecurity reporting in investment banking is a regulatory requirement (NYDFS 500.04 requires the CISO to report to the Board at least annually; most banks do quarterly). The quality and timeliness of these reports directly impacts Board confidence, budget decisions, and regulatory perception. Regulators assess Board oversight partly by reviewing Board minutes and security presentations — superficial or stale reporting is a red flag. The trend toward quantitative risk metrics (FAIR model, risk quantification in dollar terms) means CISOs need data platforms that can normalize and present complex operational data for financial audiences.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a CISO Executive Dashboard that pulls from multiple boards. Create a dashboard with these widgets: (1) Number widget showing Open P1/P2 Incidents from the Incident Response board. (2) Chart widget showing MTTR trend over last 6 months (line chart). (3) Chart widget showing Vendor Risk Score distribution from TPRM board (pie chart: Critical, High, Medium, Low tiers). (4) Battery widget showing Policy Review Compliance percentage. (5) Chart widget showing Phishing Click Rate trend by quarter (line chart with target line at 5%). (6) Number widget showing Active Security Exceptions count. (7) Chart showing Audit RFI completion rate by examination (stacked bar). (8) Table widget showing Top 10 Risk Items (highest severity, oldest open). (9) Number widget showing Mean Days to Remediate Critical Vulnerabilities. (10) Chart showing Security Budget Utilization (bar chart: planned vs actual by category). Add text widgets between sections for narrative context areas. Use red/yellow/green color coding for status indicators."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CISO Reporting Analyst
**Agent Purpose:** Continuously aggregate security metrics across all operational boards and generate executive-ready risk reports with trend analysis and recommendations.

**Triggers:**
- Monthly report generation (1st business day of each month)
- Quarterly Board report preparation (2 weeks before Board meeting)
- Ad-hoc request for risk posture summary
- Significant metric threshold breach (e.g., MTTR exceeds SLA, click rate spikes)
- New Board meeting scheduled (calendar integration)

**Actions:**
- Aggregate metrics across all security boards: incidents, vulnerabilities, vendor risk, policy compliance, training, exceptions
- Generate trend analysis comparing current period to previous periods with statistical significance indicators
- Draft executive narrative for Board presentation: key risks, notable incidents, improvement areas, resource requests
- Create risk heat map visualization mapping operational data to business impact categories
- Highlight metric anomalies and recommend investigation or action items
- Produce PDF-ready Board report package with appendices

**Data Required:**
- All security operational boards (Incident Response, TPRM, Policy, Phishing, Vulnerability, Exception)
- Historical metric snapshots for trend analysis
- Board meeting calendar and reporting templates
- Industry benchmark data for peer comparison
- Budget and headcount data for resource utilization metrics

**Autonomy Level:** Human-in-the-Loop
Data aggregation and trend analysis are fully automated. Draft narratives and recommendations are generated but require CISO review and editing. Board report formatting is automated. Anomaly alerts are autonomous. Final Board package requires CISO sign-off.

**Example Interaction:**
> Two weeks before the Q1 Board meeting, the CISO Reporting Analyst agent begins assembling the quarterly package. It pulls data across all security boards: 847 incidents handled (down 12% QoQ), MTTR improved from 4.2 to 3.1 hours, vendor assessment backlog reduced from 89 to 23, policy review compliance at 94% (up from 78%), phishing click rate down to 5.8% from 8.2%. The agent drafts the executive narrative: "Q1 2026 highlights: Incident volume decreased despite a 15% increase in monitored assets, indicating improved preventive controls. TPRM backlog reduction exceeded target by 2 months. Key risk: Three Critical-tier vendors have SOC 2 reports expiring in Q2 with no renewal confirmation — recommend Board-level attention. Resource request: One additional IAM analyst to support MFA modernization project required by NYDFS 500.12 deadline." The draft includes 12 slides with charts, a risk heat map, and an appendix with detailed metrics. CISO Sarah Martinez reviews and adjusts the narrative tone in 2 hours — versus the 60+ hours the previous manual process required.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| MNPI | Material Non-Public Information — deal or trading data that could move markets if disclosed |
| Information Barrier (Chinese Wall) | Controls preventing flow of confidential information between conflicting business units |
| VDR | Virtual Data Room — secure document sharing platform for deal due diligence |
| NYDFS 23 NYCRR 500 | New York Department of Financial Services cybersecurity regulation for financial institutions |
| DORA | Digital Operational Resilience Act — EU regulation for ICT risk management in financial entities |
| SIG | Standardized Information Gathering questionnaire — industry standard for vendor risk assessment |
| MRA/MRIA | Matters Requiring Attention / Matters Requiring Immediate Attention — OCC examination findings |
| BEC | Business Email Compromise — social engineering attack impersonating executives or counterparties |
| SOC 2 Type II | Service Organization Control audit report covering security, availability, and confidentiality controls |
| FAIR | Factor Analysis of Information Risk — quantitative risk assessment methodology |
| RFI | Request for Information — document request from regulators during examinations |
| Wall-Crossed | Personnel who have been brought "over the wall" and given access to MNPI for a specific deal |
| Bulge Bracket | Largest global investment banks (Goldman Sachs, JPMorgan, Morgan Stanley, etc.) |
| CUEC | Complementary User Entity Controls — controls that SOC 2 reports assume the customer implements |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CISO | Overall security strategy, Board reporting, regulatory liaison | Decision-maker |
| Deputy CISO / VP Security | Day-to-day security operations management | Decision-maker (operational) |
| SOC Director | Security Operations Center management, incident response | Influencer |
| Head of GRC | Governance, risk, compliance program management | Decision-maker (policy) |
| TPRM Director | Third-party risk assessment and vendor security | Influencer |
| IAM Lead | Identity and access management, privileged access | Influencer |
| Chief Risk Officer (CRO) | Enterprise risk oversight, CISO reporting line | Decision-maker (executive) |
| Head of Compliance | Regulatory examination management, information barriers | Decision-maker |
| CTO / CIO | Technology strategy, security budget approval | Decision-maker (budget) |
| Board Risk Committee | Board-level security oversight and governance | Decision-maker (governance) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT / Infrastructure | Security tool deployment, patch management, cloud security | Unified IT-Security operations dashboard, vulnerability management workflows |
| Compliance | Information barriers, regulatory examinations, policy management | Integrated compliance-security platform eliminating duplicate tracking |
| Legal | Incident response (breach notification), contract security terms, regulatory defense | Streamlined incident-to-legal escalation, contract clause tracking |
| Operations | Business continuity, disaster recovery, physical security | Unified resilience program management |
| HR | Security clearances, insider threat, termination access revocation | Automated joiner/mover/leaver security provisioning workflows |
| Trading Technology | Trading platform security, algorithmic IP protection | Secure development lifecycle tracking, trading system change management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow SecOps | Enterprise security operations and incident response | monday.com offers faster deployment, better UX for cross-functional collaboration, and lower TCO. ServiceNow implementations average 6-12 months; monday.com deploys in weeks. |
| Archer (RSA) | GRC platform for risk and compliance management | Legacy, expensive, and complex. monday.com provides modern UX with equivalent workflow capability at 40-60% lower cost. |
| OneTrust | Privacy and third-party risk management | Narrow focus on privacy/TPRM. monday.com offers broader platform consolidation across security, compliance, and operations. |
| Jira / Confluence | Ad-hoc security task and documentation management | Developer-centric, not designed for security workflows. monday.com provides purpose-built status tracking, automations, and executive dashboards. |
| Spreadsheets (Excel/Sheets) | Universal fallback for everything | No workflow automation, no audit trail, no real-time dashboards, version control nightmares. monday.com replaces the "spreadsheet sprawl" problem entirely. |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have ServiceNow for security operations." | "ServiceNow is powerful but complex — how long did implementation take? Are your non-SOC stakeholders (Compliance, Legal, executives) actually using it? monday.com excels at the cross-functional coordination layer that ServiceNow struggles with. Many banks use monday.com alongside ServiceNow for stakeholder-facing workflows." |
| "Security data is too sensitive for a cloud platform." | "monday.com is SOC 2 Type II certified, HIPAA compliant, and supports data residency requirements. Leading financial institutions including banks use monday.com today. We can discuss your specific data classification requirements — most security workflow data (status, assignments, timelines) isn't classified at the same level as raw security telemetry." |
| "We need a GRC-specific platform, not a general work management tool." | "General work management is our foundation — but with automations, integrations, and customizable workflows, we become your GRC platform without the 12-month implementation timeline and $500K+ professional services cost. Would you rather wait a year for a rigid tool or be operational in 4 weeks with something your team actually wants to use?" |
| "Our regulators expect specific GRC tools." | "Regulators care about demonstrable controls, audit trails, and evidence — not vendor logos. monday.com provides complete audit trails, automated evidence collection, and reporting that exceeds what most GRC tools deliver. We can show you how other regulated institutions have passed examinations using monday.com." |
| "We can't justify another tool in our stack." | "That's exactly the point — we're not adding to the stack, we're consolidating. How many spreadsheets, SharePoint sites, and email threads are you using for policy tracking, exception management, exam prep, and Board reporting today? monday.com replaces all of those with one auditable platform." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder: Global bank using monday.com for security operations coordination]
- [Placeholder: Financial services firm that consolidated GRC workflows onto monday.com]
- [Placeholder: Investment bank that reduced Board reporting preparation by 80%]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
