# Banking × Security & Infosec Playbook

## Overview

Security and Information Security (Infosec) departments in banking are among the most critical, heavily regulated, and well-funded functions in any industry. Banks are the #1 target for cyberattacks globally — financial services firms experience 300x more cyberattacks than other industries. A typical mid-size bank's security team manages threat detection across thousands of endpoints, hundreds of applications, and billions of daily transactions, while simultaneously satisfying examination requirements from the OCC, FDIC, Federal Reserve, state regulators, and increasingly, the SEC. The CISO reports to the CIO or directly to the board's risk committee, with budgets ranging from $20M-50M at regional banks to $500M+ at G-SIBs.

Banking security organizations are structured around the NIST Cybersecurity Framework or similar standards (ISO 27001, CIS Controls), with teams typically segmented into: Security Operations Center (SOC), Threat Intelligence, Vulnerability Management, Identity & Access Management (IAM), Application Security (AppSec), Cloud Security, Third-Party Risk Management (TPRM), Governance Risk & Compliance (GRC), Incident Response, and Security Architecture. Headcount ranges from 50-100 at regional banks to 1,000+ at the largest institutions. The talent shortage is acute — the cybersecurity skills gap in financial services is estimated at 40,000+ unfilled positions in the US alone.

Regulatory pressure is relentless and increasing. The OCC's Heightened Standards require boards to set and monitor cybersecurity risk appetite. The Federal Reserve's SR 23-4 guidance on cybersecurity incident reporting mandates 36-hour notification windows. The SEC's cybersecurity disclosure rules require public companies to report material incidents within four business days. NYDFS 23 NYCRR 500 (updated 2023) imposes detailed cybersecurity requirements on all New York-regulated financial institutions. The FFIEC's Cybersecurity Assessment Tool (CAT) and IT Examination Handbook drive examination expectations. Banks operating internationally must also comply with GDPR, DORA (EU), and various APAC regulations. Managing this compliance burden while actually protecting the bank from threats is the central tension of banking infosec.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | The cybersecurity talent shortage is existential for banking security teams. Every analyst-hour saved through automation can be redirected to higher-value threat hunting and architecture work. SOC analyst burnout and turnover exceed 35% annually. |
| 2 | Consolidate Tech Stack with AI | High | Banks average 70-100 security tools. Tool sprawl creates integration gaps, alert fatigue, and massive licensing costs. Consolidating workflow orchestration, GRC, and third-party risk management onto fewer platforms reduces both cost and risk. |
| 3 | Scale Impact Without Overhead | Medium-High | Regulatory examination scope expands every year. Third-party risk portfolios grow with every fintech partnership. Attack surface expands with every cloud migration. Security teams must scale their coverage without proportional headcount growth. |

## Prioritized Use Cases

---

### Use Case 1: Third-Party Risk Management (TPRM) Lifecycle

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banks rely on thousands of third-party vendors — from core banking processors (FIS, Fiserv, Jack Henry) to cloud providers, fintech partners, and office supply companies. Regulatory guidance (OCC Bulletin 2013-29, Federal Reserve SR 13-19, FDIC FIL-44-2008, and the 2023 Interagency Guidance on Third-Party Relationships) requires banks to manage the full lifecycle: planning, due diligence, contract negotiation, ongoing monitoring, and termination. A typical regional bank manages 1,500-3,000 vendor relationships with 200-500 classified as "critical" or "significant." Due diligence alone requires collecting SOC 2 reports, business continuity plans, information security policies, financial statements, insurance certificates, and regulatory compliance attestations — annually for critical vendors. Most banks manage this in spreadsheets, SharePoint libraries, and email, leading to missed renewal dates, incomplete assessments, and examination findings.

#### The Solution
monday.com Work Management as a comprehensive TPRM platform. A Vendor Registry board maintains the complete inventory with risk-tiering columns (Critical/High/Medium/Low based on data access, financial materiality, and substitutability). Connected boards manage due diligence workflows: each annual assessment moves through stages (Initiated → Documents Requested → Documents Received → Under Review → Risk Rated → Approved/Remediation Required → Complete). Automations handle the orchestration: 90-day advance notices for annual reviews, escalation when documents are overdue, automatic risk re-rating when assessment scores change. Dashboards give the CISO and board risk committee real-time visibility into TPRM portfolio health.

#### The Outcome
80% reduction in time spent chasing vendor documentation (automated reminders and tracking vs. manual email follow-up). Zero missed annual review deadlines. Examination-ready reporting: produce the complete TPRM portfolio status in minutes instead of weeks. Risk-based resource allocation: focus analyst time on critical vendors, not spreadsheet maintenance. 40% reduction in TPRM-related examination findings.

#### Discovery Questions
- "How many third-party vendors do you manage, and how many are classified as critical or significant?"
- "Walk me through your annual due diligence process — from initiating the review to final approval. How long does it take on average?"
- "When your examiner asks for the current status of all critical vendor assessments, how quickly can you produce that?"
- "How do you handle fourth-party risk — vendors of your vendors?"
- "Have you received examination findings related to TPRM? What were the themes?"

#### Industry Context
The 2023 Interagency Guidance on Third-Party Relationships raised the bar significantly, requiring banks to manage risk throughout the entire vendor lifecycle — including "planning" (pre-engagement risk assessment) and "termination" (ensuring data return and destruction). The guidance explicitly covers fintech partnerships, which are growing rapidly. Fourth-party risk (your vendor's vendors) is an emerging examination focus. Concentration risk — multiple critical functions relying on the same vendor (e.g., AWS) — is a board-level concern. The MOVEit breach (2023) and SolarWinds attack demonstrated how vendor compromises cascade through the banking sector.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Third-Party Risk Management system for a bank's security team. Board 1 — Vendor Registry: columns for Vendor Name (text), Risk Tier (dropdown: Critical/High/Medium/Low), Service Category (dropdown: Core Banking/Cloud Infrastructure/Payment Processing/Data Analytics/Fintech Partner/IT Services/Professional Services/Facilities/Other), Data Access Level (dropdown: Customer PII/Financial Data/Internal Only/No Sensitive Data/Transaction Data), Business Owner (people), Security Reviewer (people), Contract Expiration (date), Last Assessment Date (date), Next Assessment Due (date), Overall Risk Rating (status: Acceptable/Elevated/High/Critical/Not Assessed), SOC 2 Current (checkbox), BCP Reviewed (checkbox), Cyber Insurance Verified (checkbox), Regulatory Classification (dropdown: OCC Critical/Significant/Limited), Fourth-Party Dependencies (text), Concentration Risk Flag (checkbox). Board 2 — Due Diligence Tracker: columns for Vendor (connect to Board 1), Assessment Year (text), Status (status: Initiated/Documents Requested/Awaiting Response/Under Review/Risk Scoring/Remediation Required/Approved/Escalated), Assigned Analyst (people), Documents Received (numbers showing X of Y), Risk Score (numbers 1-100), Findings Count (numbers), Remediation Items (numbers), Due Date (date), Days Overdue (formula), Examiner Ready (checkbox). Automations: 90 days before Next Assessment Due, create new Due Diligence item and notify Security Reviewer; when Documents Requested status is set and no change in 14 days, escalate to Business Owner; when Risk Score exceeds 75, auto-set Risk Tier to Critical and notify CISO; when Findings Count > 0, create linked Remediation items with 30/60/90 day SLAs. Dashboard: vendor portfolio by risk tier (pie chart), overdue assessments, assessment completion rate, average time-to-complete by tier, upcoming deadlines in next 90 days, concentration risk heat map."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorShield Risk Analyst
**Agent Purpose:** Automate vendor due diligence document collection, initial risk scoring, and continuous monitoring to scale TPRM coverage without proportional headcount.

**Triggers:**
- New due diligence assessment item created (annual review cycle)
- Vendor's SOC 2 report expiration date approaching (30 days)
- News alert: vendor appears in breach notification, regulatory action, or financial distress article
- Contract expiration within 90 days
- New vendor onboarding request submitted

**Actions:**
- Auto-generate and send due diligence questionnaire to vendor contact with document request checklist customized by risk tier
- Parse received SOC 2 Type II reports: extract control exceptions, identify gaps against bank's minimum requirements, generate summary scorecard
- Calculate initial risk score based on: data access level, service criticality, financial health indicators, SOC 2 findings, geographic risk, concentration risk
- Generate continuous monitoring alerts from dark web monitoring, breach databases, and financial distress indicators
- Produce quarterly TPRM board report: portfolio risk distribution changes, new critical vendors, remediation progress, regulatory readiness assessment
- Auto-create remediation tracking items when assessment identifies gaps, with SLAs based on severity

**Data Required:**
- Vendor contact database and contract repository
- SOC 2 reports and security questionnaire responses
- Threat intelligence feeds (recorded future, SecurityScorecard)
- Financial health data (D&B, credit ratings)
- Regulatory guidance requirements by vendor tier
- Historical assessment data for trend analysis

**Autonomy Level:** Human-in-the-Loop
Document collection, initial parsing, and risk scoring are automated. Final risk ratings, vendor approvals, and remediation decisions require human analyst review. Critical risk escalations go directly to CISO.

**Example Interaction:**
> It's January, and VendorShield initiates the annual review cycle for 487 vendors. For each, it auto-generates a customized document request based on risk tier: critical vendors get a 47-item questionnaire plus document requests for SOC 2, penetration test results, BCP/DR test results, and cyber insurance certificates. Medium-tier vendors get a streamlined 15-item questionnaire. The agent sends requests, tracks responses, and sends escalating reminders at 14, 21, and 28 days. As documents arrive, it parses SOC 2 reports automatically: "Vendor XYZ's SOC 2 Type II has 3 control exceptions: (1) privileged access review not performed quarterly — HIGH risk given they access customer PII, (2) backup restoration not tested — MEDIUM risk, (3) password complexity below standard — LOW risk. Recommended risk score: 72 (Elevated). Two remediation items recommended with 60-day SLA." The analyst reviews the summary, agrees with the scoring, and approves — a process that took 15 minutes instead of the previous 4 hours per vendor.

---

### Use Case 2: Security Incident Response & Tracking

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
When a security incident occurs — phishing compromise, malware detection, unauthorized access, DDoS attack, or data breach — banking security teams must execute a complex, time-sensitive response. They must contain the threat, assess impact, preserve evidence, notify regulators (within 36 hours per SR 23-4, within 72 hours per NYDFS, within 4 business days per SEC for material incidents), coordinate with legal, communicate with affected customers, and document everything for post-incident review. Most banks manage incidents through a combination of SIEM alerts, ticketing systems (ServiceNow, Jira), email chains, and war room calls. The lack of a unified incident lifecycle view means critical steps are missed, evidence chains are broken, and regulatory notification timelines are violated. The average cost of a data breach in financial services is $5.9M (IBM 2024).

#### The Solution
monday.com Work Management as the incident response orchestration layer. An Incident Board tracks each incident through its lifecycle with status columns (Detected → Triaged → Contained → Eradicated → Recovered → Post-Incident Review → Closed). Connected boards manage: evidence preservation tasks, regulatory notification workflows (with countdown timers for each regulator's deadline), customer notification campaigns, and remediation actions. Automations enforce SLAs: triage must complete within 1 hour for Severity 1, containment plan within 4 hours, regulatory notification assessment within 24 hours. Dashboards provide real-time incident status to CISO and executive leadership.

#### The Outcome
50% faster mean-time-to-contain (MTTC) through automated workflow orchestration. 100% regulatory notification compliance — no missed deadlines. Complete evidence chain documentation for forensic investigations and legal proceedings. 60% reduction in post-incident review time through pre-documented incident timelines. Reduced breach-related costs through faster containment.

#### Discovery Questions
- "Walk me through your last significant security incident — from detection to closure. What worked well? What broke down?"
- "How do you track regulatory notification deadlines during an active incident? Have you ever been close to missing one?"
- "How do you coordinate between SOC analysts, incident commanders, legal counsel, and executive leadership during an incident?"
- "What's your current mean-time-to-detect and mean-time-to-contain? Are you tracking these metrics?"
- "After an incident, how do you ensure remediation actions are actually completed and verified?"

#### Industry Context
Banking incident response operates under intense regulatory scrutiny. The OCC expects banks to have tested incident response plans (IRP) and to demonstrate they can execute them under pressure. NYDFS 23 NYCRR 500 requires notification to the superintendent within 72 hours. The SEC's cybersecurity disclosure rules (effective December 2023) require assessment of materiality and disclosure within 4 business days. The Federal Reserve's SR 23-4 requires notification within 36 hours for "computer-security incidents" that materially affect the bank or its customers. Each regulator has different notification thresholds and timelines, creating a complex compliance matrix during an already chaotic event. Banks must also coordinate with law enforcement (FBI, Secret Service), payment networks (Visa, Mastercard), and potentially FS-ISAC.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Incident Response Tracker for a bank. Columns: Incident ID (auto-number with prefix INC-), Incident Name (text), Severity (dropdown: SEV-1 Critical/SEV-2 High/SEV-3 Medium/SEV-4 Low), Category (dropdown: Data Breach/Ransomware/Phishing Compromise/Unauthorized Access/DDoS/Insider Threat/Malware/Third-Party Compromise/Account Takeover/ATM-Card Fraud), Status (status: Detected/Triaged/Contained/Eradicated/Recovered/Post-Incident Review/Closed), Incident Commander (people), SOC Lead (people), Legal Counsel (people), Detection Time (date with time), Triage Deadline (date — auto-calculate 1hr from Detection for SEV-1), Containment Deadline (date — 4hr from Detection for SEV-1), Affected Systems (text), Data Impact (dropdown: Confirmed PII Exposed/Suspected PII Exposed/No PII/Financial Data Exposed/Under Investigation), Customer Impact Count (numbers), Regulatory Notifications Required (dropdown multi-select: OCC/FDIC/Federal Reserve/NYDFS/SEC/State AG/FS-ISAC/FBI/Card Networks), OCC Notification Deadline (date), SEC Materiality Assessment Due (date), NYDFS 72hr Deadline (date), Evidence Preserved (checkbox), Root Cause (dropdown: Phishing/Vulnerability Exploitation/Misconfiguration/Insider/Third-Party/Unknown), Remediation Items (numbers), Lessons Learned Completed (checkbox). Groups: Active Incidents, Under Investigation, Post-Incident Review, Closed. Automations: when Severity is SEV-1, immediately notify CISO, CIO, General Counsel, and CEO; when Status is Detected and Severity is SEV-1, start 1-hour triage countdown; when Data Impact changes to Confirmed PII Exposed, auto-populate all Regulatory Notification deadlines based on detection time; when Post-Incident Review status set and Lessons Learned not completed after 14 days, escalate. Dashboard: active incidents by severity, time-in-stage metrics, regulatory notification countdown timers, incident trends over 12 months, MTTD and MTTC averages."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** IncidentForce Commander
**Agent Purpose:** Orchestrate incident response workflows, track regulatory notification deadlines, and ensure no step in the incident lifecycle is missed.

**Triggers:**
- SIEM integration creates new incident item (via API from Splunk, Microsoft Sentinel, or CrowdStrike)
- Incident severity upgraded
- Regulatory notification deadline within 12/6/2 hours
- Incident status unchanged for longer than SLA threshold
- New threat intelligence matching active incident indicators of compromise (IOCs)

**Actions:**
- Auto-assign incident roles from on-call roster based on incident category and severity
- Generate incident-specific runbook checklist from playbook library (ransomware playbook, data breach playbook, DDoS playbook, etc.)
- Calculate and populate all regulatory notification deadlines based on incident characteristics and detection time
- Create evidence preservation task list with chain-of-custody tracking
- Send escalating notifications as regulatory deadlines approach (12hr, 6hr, 2hr warnings)
- Generate real-time incident status brief for executive leadership (auto-updating every 30 minutes during SEV-1)
- Create post-incident review items with pre-populated timeline from incident board activity log
- Track related threat intelligence and update incident scope if new IOCs are discovered

**Data Required:**
- SIEM/SOAR integration APIs
- On-call rotation schedule
- Incident response playbook library
- Regulatory notification requirements matrix
- Threat intelligence platform feeds
- Asset inventory for impact assessment

**Autonomy Level:** Human-in-the-Loop
Workflow orchestration, deadline tracking, and status reporting are automated. All containment decisions, regulatory notifications, and customer communications require human approval. The agent coordinates — humans decide.

**Example Interaction:**
> At 2:17 AM, the SIEM fires an alert: suspicious lateral movement detected on three servers in the commercial lending environment. IncidentForce Commander auto-creates an INC-2026-0147, classifies it as SEV-2 (potential unauthorized access to financial data), and pages the on-call SOC lead and incident commander. Within 60 seconds, it populates the ransomware response playbook (closest match to lateral movement pattern), assigns evidence preservation tasks, and calculates regulatory deadlines: "If PII exposure confirmed, OCC notification due by Feb 20 2:17 AM (36 hours), NYDFS due by Feb 22 2:17 AM (72 hours), SEC materiality assessment due by Feb 21." As the SOC team investigates, the agent tracks progress against SLA: triage must complete by 3:17 AM. At 2:58 AM, the SOC confirms unauthorized access but no evidence of data exfiltration yet. The agent upgrades the status to "Contained — monitoring" and generates the first executive brief: "Incident INC-2026-0147: Unauthorized access to 3 commercial lending servers. Contained at 02:52. No confirmed data exfiltration. Investigation ongoing. Regulatory notification clock started."

---

### Use Case 3: GRC (Governance, Risk & Compliance) Policy Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking security teams maintain hundreds of policies, standards, and procedures that must be reviewed annually, approved by appropriate governance bodies, mapped to regulatory requirements, and communicated to employees. Frameworks include NIST CSF, ISO 27001, CIS Controls, FFIEC IT Examination Handbook, NYDFS 23 NYCRR 500, PCI DSS, and SOX IT controls. Each policy must cross-reference multiple regulatory requirements, be version-controlled, have documented approval chains, and be accessible to examiners on demand. Most banks manage this in document management systems (SharePoint) with spreadsheet-based control mapping — resulting in stale policies, missed review deadlines, incomplete regulatory mappings, and weeks of preparation before examinations.

#### The Solution
monday.com Work Management as a policy lifecycle and control mapping platform. A Policy Registry board tracks every security policy with version, owner, approval status, review cycle, and regulatory mapping. Connected boards manage the review workflow (Annual Review → Draft Update → Security Review → Legal Review → CISO Approval → Board Committee → Published). Control mapping boards link each policy to specific regulatory requirements (NIST CSF subcategories, FFIEC objectives, NYDFS sections, PCI DSS requirements). Automations trigger annual review cycles, track approval workflows, and flag expired policies.

#### The Outcome
100% on-time policy review completion (vs. industry average of 60-70%). Examination preparation reduced from 3-4 weeks to 2-3 days — all policies, approvals, and regulatory mappings are in one searchable platform. Zero examination findings for stale or un-approved policies. Cross-framework mapping eliminates duplicate compliance effort across NIST, FFIEC, NYDFS, and PCI.

#### Discovery Questions
- "How many security policies and standards does your team maintain, and what's your current on-time review completion rate?"
- "When an examiner asks to see your access management policy, its approval history, and its mapping to FFIEC controls, how long does that take to pull together?"
- "How do you handle cross-framework mapping? If NIST CSF, FFIEC, and NYDFS all require access controls, do you maintain separate documentation or a unified view?"
- "What happens when a regulatory requirement changes — how do you identify which policies need updating?"
- "How do you ensure employees have read and understood updated security policies?"

#### Industry Context
Bank examiners increasingly evaluate cybersecurity programs against multiple frameworks simultaneously. An OCC examiner might assess FFIEC CAT maturity, NIST CSF alignment, and NYDFS 500 compliance in a single examination. Banks without unified control mapping spend enormous time producing framework-specific evidence packages. PCI DSS 4.0 (effective March 2025) introduces new customized approach options that require even more detailed documentation. SOX IT general controls (ITGCs) overlap significantly with security controls, creating another compliance thread. The DORA regulation (EU, effective January 2025) adds ICT risk management requirements for banks operating in Europe.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a GRC Policy Management system for a banking security team. Board 1 — Policy Registry: columns for Policy Name (text), Policy ID (text, e.g., SEC-POL-001), Category (dropdown: Access Management/Data Protection/Incident Response/Network Security/Cloud Security/Third-Party Risk/Physical Security/Business Continuity/Acceptable Use/Encryption/Vulnerability Management/Change Management), Version (text), Status (status: Draft/Under Review/Approved/Published/Expired/Retired), Owner (people), Approver (people), Last Approved Date (date), Review Cycle (dropdown: Annual/Semi-Annual/Quarterly), Next Review Due (date), NIST CSF Mapping (dropdown multi-select: Identify/Protect/Detect/Respond/Recover with subcategories), FFIEC Mapping (text), NYDFS 500 Section (dropdown multi-select), PCI DSS Requirement (dropdown multi-select), SOX ITGC (checkbox), Document Link (link), Employee Acknowledgment Rate (numbers with %). Board 2 — Control Mapping: columns for Control ID (text), Control Description (text), Connected Policy (connect to Board 1), Framework (dropdown: NIST CSF/FFIEC/NYDFS 500/PCI DSS 4.0/ISO 27001/SOX/CIS Controls/DORA), Framework Reference (text), Control Effectiveness (status: Effective/Partially Effective/Ineffective/Not Tested), Last Test Date (date), Evidence Location (link), Examiner Ready (checkbox). Automations: 60 days before Next Review Due, create review workflow item and notify Owner; when Status is Approved, auto-update Last Approved Date and calculate Next Review Due; when any connected control's Effectiveness changes to Ineffective, flag policy for emergency review; when NYDFS 500 Section is populated and Review Cycle is not at least Annual, flag non-compliance. Dashboard: policy status overview (approved vs. expired vs. under review), upcoming reviews timeline, control effectiveness by framework, examination readiness score, cross-framework coverage heat map."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PolicyGuard GRC Engine
**Agent Purpose:** Automate policy review cycles, maintain cross-framework control mappings, and generate examination-ready evidence packages on demand.

**Triggers:**
- Policy review due date within 60 days
- Regulatory body publishes updated guidance or new requirement
- Control effectiveness test completed with findings
- Examination notification received (create exam prep workflow)
- New policy or standard created (auto-generate framework mappings)

**Actions:**
- Initiate policy review workflow: pull current policy, generate redline comparison with regulatory changes since last review, assign to owner with change summary
- Auto-map new policies to applicable regulatory frameworks based on content analysis (NIST CSF, FFIEC, NYDFS, PCI DSS)
- Generate examination evidence package: for each requested framework, compile all mapped policies, approval histories, control test results, and remediation status
- Track regulatory changes (Federal Register, NYDFS updates, PCI SSC bulletins) and flag affected policies
- Produce quarterly GRC dashboard report for board risk committee: policy compliance rate, control effectiveness trends, examination readiness score
- Generate gap analysis when new regulatory requirement is identified: which existing controls cover it, what's missing

**Data Required:**
- Complete policy document repository
- Regulatory framework requirement databases
- Control test results and evidence
- Regulatory agency update feeds
- Examination schedule and scope notifications
- Historical examination findings

**Autonomy Level:** Human-in-the-Loop
Framework mapping suggestions, review cycle management, and report generation are automated. Policy approvals, control effectiveness ratings, and examination responses require human judgment and sign-off.

**Example Interaction:**
> The OCC notifies the bank of an upcoming IT examination focused on cloud security and third-party risk management. PolicyGuard immediately creates an exam prep board with all relevant policies, control mappings, and evidence items. It identifies 14 policies mapped to cloud security and TPRM, pulls their approval histories, and checks all connected controls: "12 of 14 policies are current (approved within review cycle). 2 policies flagged: Cloud Security Standard SEC-STD-008 is 45 days overdue for annual review — recommend emergency review before exam. Third-Party Incident Response Procedure SEC-PROC-023 was last tested 14 months ago — recommend tabletop exercise. All FFIEC IT Handbook cloud computing references mapped. Evidence package generated: 847 items organized by examination objective. Estimated exam prep completion: 2.5 days with recommended actions." The CISO reviews the package and prioritizes the two flagged items for immediate attention.

---

### Use Case 4: Vulnerability Management Program

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banks scan thousands of assets weekly, generating tens of thousands of vulnerability findings. Each finding must be risk-rated in the context of the bank's environment (a critical vulnerability on an internet-facing payment server is very different from the same CVE on an isolated test system), assigned to the appropriate remediation team, tracked through patching or mitigation, and verified as resolved. Regulatory expectations are clear: FFIEC expects banks to have risk-based vulnerability management programs with defined SLAs (e.g., critical: 15 days, high: 30 days, medium: 90 days). Most banks struggle with the volume — security teams spend more time managing spreadsheets and chasing remediation owners than actually reducing risk. SLA compliance for critical vulnerabilities is often below 70%, creating examination findings and real security exposure.

#### The Solution
monday.com Work Management as the vulnerability management orchestration layer between scanning tools (Qualys, Tenable, Rapid7) and remediation teams (IT operations, application development, cloud engineering). Vulnerabilities feed in via API integration, are auto-enriched with asset context (business criticality, data classification, internet exposure), and assigned to remediation owners with SLA deadlines. Status tracking through the remediation lifecycle (New → Assigned → In Progress → Patched → Verified → Closed) provides real-time visibility. Exception management workflows handle cases where patching isn't possible (compensating controls, risk acceptance). Dashboards show SLA compliance, aging trends, and risk reduction over time.

#### The Outcome
SLA compliance improved from 65% to 92%+ for critical vulnerabilities. 70% reduction in time spent on vulnerability tracking and follow-up. Clear accountability: every vulnerability has an owner and a deadline. Examination-ready reporting: produce SLA compliance, aging, and remediation trend reports instantly. Mean-time-to-remediate (MTTR) reduced by 40%.

#### Discovery Questions
- "How many vulnerability findings does your team process per month, and what's your current SLA compliance rate for critical findings?"
- "How do you assign vulnerabilities to remediation teams — is it automated or manual?"
- "When a vulnerability can't be patched (legacy system, vendor dependency), what's your exception and compensating control process?"
- "How do you prioritize — is it purely CVSS score, or do you factor in asset context like internet exposure and data sensitivity?"
- "What does your examiner expect to see for vulnerability management, and how do you produce those reports today?"

#### Industry Context
Banking regulators view vulnerability management as a leading indicator of cybersecurity program maturity. FFIEC examiners specifically review patching SLAs, exception management, and trend data. NYDFS 500.5 requires periodic penetration testing and vulnerability assessments. PCI DSS 4.0 Requirement 6 mandates identification and remediation of vulnerabilities in payment systems. The challenge is compounded by legacy systems — many banks run mainframes and applications that are 20-30 years old and can't be easily patched, requiring compensating controls and risk acceptance documentation. Zero-day vulnerabilities (Log4Shell, MOVEit) require emergency response capabilities that bypass normal change management.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vulnerability Management Tracker for a banking security team. Columns: Vuln ID (text, auto-populated from scanner), CVE ID (text), CVSS Score (numbers), Bank Risk Rating (dropdown: Critical/High/Medium/Low — may differ from CVSS based on context), Affected Asset (text), Asset Criticality (dropdown: Tier 1-Mission Critical/Tier 2-Business Critical/Tier 3-Standard/Tier 4-Non-Production), Internet Facing (checkbox), Data Classification (dropdown: PII/Financial/Internal/Public), Scanner Source (dropdown: Qualys/Tenable/Rapid7/Pen Test/Bug Bounty), Status (status: New/Assigned/In Progress/Patched/Verification Pending/Verified Closed/Exception-Compensating Control/Exception-Risk Accepted), Remediation Owner (people), Assigned Date (date), SLA Deadline (date — auto-calculated based on Bank Risk Rating), Days to SLA (formula: SLA Deadline minus today), Actual Remediation Date (date), SLA Met (formula: checkbox if remediated before deadline), Exception Approved By (people), Compensating Control (text), PCI Scope (checkbox), Regulatory Exam Relevant (checkbox). Groups: Critical-Overdue, Critical-Active, High-Active, Medium-Active, Exceptions, Closed This Month. Automations: when new item created with Critical rating, auto-calculate SLA (15 days) and notify Remediation Owner and CISO; when Days to SLA reaches 5, send warning; when Days to SLA reaches 0 and Status is not Patched/Exception, escalate to CISO and move to Critical-Overdue group; when Exception requested, route to CISO for approval with compensating control documentation. Dashboard: SLA compliance rate by severity, vulnerability aging chart, open vulns by remediation team, MTTR trends, overdue critical count (big number widget), PCI-scope vulnerability status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VulnOps Prioritizer
**Agent Purpose:** Ingest vulnerability scan results, contextually prioritize them beyond CVSS scores, auto-assign to remediation teams, and relentlessly track SLA compliance.

**Triggers:**
- Vulnerability scanner completes scan and pushes results via API
- New CVE published with CISA KEV (Known Exploited Vulnerabilities) designation
- SLA deadline approaching (5 days, 2 days, overdue)
- Remediation owner marks item as patched (trigger verification scan)
- Monthly vulnerability management report due

**Actions:**
- Ingest scan results, deduplicate, and enrich with asset context (criticality tier, internet exposure, data classification, PCI scope)
- Re-rate CVSS score based on environmental context: internet-facing + PII + Tier 1 asset = always Critical regardless of base CVSS
- Auto-assign to remediation team based on asset ownership mapping
- Track CISA KEV entries and auto-escalate matching vulnerabilities to Critical with shortened 7-day SLA
- Generate monthly vulnerability management report: new vs. closed trend, SLA compliance by team, aging analysis, risk reduction metrics
- Trigger verification scan after remediation to confirm fix, auto-close or reopen based on results
- Identify vulnerability patterns (same CVE across many systems = systemic issue, escalate to architecture team)

**Data Required:**
- Vulnerability scanner APIs (Qualys/Tenable/Rapid7)
- Asset inventory with owner, criticality, and network zone data
- CISA KEV feed
- NVD/CVE database for enrichment
- Remediation team and asset owner mappings
- Historical vulnerability and remediation data

**Autonomy Level:** Fully Autonomous for ingestion, prioritization, and tracking; Human-in-the-Loop for exceptions and risk acceptance
Scan ingestion, contextual re-rating, assignment, and SLA tracking happen without human intervention. Exception requests and risk acceptance decisions require CISO approval.

**Example Interaction:**
> Tuesday morning, Qualys completes its weekly enterprise scan: 12,847 findings across 3,200 assets. VulnOps Prioritizer processes them in under 10 minutes: deduplicates to 8,934 unique findings (3,913 were already tracked), identifies 23 new Critical items (12 based on CVSS 9.0+, 11 re-rated to Critical due to environmental context). Of the 23, it flags 3 as highest priority: "CVE-2026-1847 — Remote code execution in Apache Struts. Found on 3 internet-facing customer portal servers (Tier 1, PII). CISA KEV listed. Assigned to WebOps team with 7-day SLA. Additionally, this CVE is present on 14 internal application servers — assigned to AppOps with standard 15-day Critical SLA." The SOC manager opens their dashboard to find everything triaged, assigned, and SLA-tracked — no spreadsheet wrangling required.

---

### Use Case 5: Security Awareness & Phishing Simulation Program

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Phishing remains the #1 attack vector in banking, responsible for over 80% of initial compromises. Regulators expect banks to maintain robust security awareness programs with regular training, phishing simulations, and measurable improvement in employee behavior. Banking security teams must train 5,000-50,000+ employees, track completion rates for compliance (FFIEC, NYDFS 500.14), manage phishing simulation campaigns, remediate repeat offenders, and report metrics to the board. Most programs use standalone tools (KnowBe4, Proofpoint Security Awareness) but lack workflow integration — when an employee fails a phishing simulation, who follows up? When a department consistently underperforms, who owns the remediation? These operational gaps between the training tool and actual behavior change are where programs stall.

#### The Solution
monday.com Work Management as the security awareness program management layer. A Campaign Calendar board manages the annual training and simulation schedule. A Phishing Simulation Results board tracks each campaign's results by department, with connected items for employees requiring additional training. A Compliance Tracker board ensures 100% training completion with automated escalation. Department-level dashboards give business unit leaders visibility into their team's security posture. Remediation workflows auto-assign additional training modules to repeat offenders.

#### The Outcome
Training completion rates improved from 82% to 99%+ through automated escalation. 45% reduction in phishing simulation click rates over 12 months through targeted remediation. Department-level accountability: business unit leaders see their team's metrics and own improvement. Regulatory compliance: produce training completion evidence for any examination in minutes. 60% reduction in manual program administration time.

#### Discovery Questions
- "What's your current phishing simulation click rate, and how has it trended over the past year?"
- "When an employee fails a phishing simulation, what happens next? Is there a structured remediation process?"
- "How do you ensure 100% completion of mandatory security awareness training? What's your current completion rate?"
- "Can you report security awareness metrics by department to business unit leaders?"
- "How do you tailor training content to role-specific risks — e.g., wire transfer fraud for treasury staff vs. social engineering for branch employees?"

#### Industry Context
NYDFS 23 NYCRR 500.14 requires cybersecurity awareness training for all personnel. FFIEC examiners evaluate awareness programs as part of management assessment. Wire transfer fraud (Business Email Compromise) is a particularly acute risk in banking — the FBI reports $2.7B in BEC losses in financial services annually. Role-based training is increasingly expected: branch staff need training on physical social engineering (tailgating, impersonation), treasury staff on wire fraud schemes, developers on secure coding, and executives on whale phishing. The quality and measurability of awareness programs has become a board-level governance topic at most banks.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Awareness Program Manager for a bank. Board 1 — Campaign Calendar: columns for Campaign Name (text), Type (dropdown: Phishing Simulation/Mandatory Training/Role-Based Training/Tabletop Exercise/Awareness Communication/Security Month Event), Target Audience (dropdown: All Employees/Branch Staff/Corporate/IT Staff/Developers/Executives/Treasury/New Hires), Status (status: Planning/Content Development/Compliance Review/Scheduled/Active/Completed/Analyzing Results), Start Date (date), End Date (date), Owner (people), Completion Target (numbers with %), Actual Completion (numbers with %), Click Rate (numbers with % — phishing only), Report Rate (numbers with % — phishing only). Board 2 — Employee Remediation Tracker: columns for Employee Name (text), Department (dropdown), Manager (people), Phishing Failures (numbers — lifetime count), Last Failure Date (date), Remediation Status (status: Additional Training Assigned/Training Completed/Manager Notified/Escalated to HR/Remediated), Risk Level (status: Low-1 failure/Medium-2 failures/High-3+ failures), Training Module Assigned (text), Completion Deadline (date). Automations: when Phishing Failures reaches 2, notify employee's manager; when Phishing Failures reaches 3, escalate to HR and assign mandatory 1-on-1 training; when Campaign Type is Mandatory Training and Actual Completion is below target 7 days after End Date, escalate incomplete employees to their managers; when new employee onboarded, auto-assign baseline security training with 30-day deadline. Dashboard: click rate trends over 12 months, completion rates by department, repeat offender count, upcoming campaigns, department risk ranking (worst performing to best), training compliance percentage for regulatory reporting."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PhishGuard Training Orchestrator
**Agent Purpose:** Design targeted phishing campaigns, manage remediation workflows for repeat offenders, and generate regulatory-ready awareness program reports.

**Triggers:**
- Monthly phishing simulation schedule date
- Employee fails phishing simulation (via KnowBe4/Proofpoint API integration)
- Mandatory training deadline approaching with completion below 95%
- New employee onboarded (HR system integration)
- Quarterly board report due

**Actions:**
- Design phishing simulation campaigns tailored to current threat landscape: use recent real-world banking phishing examples as templates (wire transfer requests, regulatory notice spoofs, IT password reset lures)
- Process simulation results: update employee records, calculate department scores, identify trends
- Auto-assign remediation training modules based on failure type (clicked link vs. entered credentials vs. opened attachment — different risk levels)
- Generate escalation chain for repeat offenders: 1st offense → micro-training, 2nd → manager notification + extended training, 3rd → HR escalation + mandatory 1-on-1
- Produce quarterly board report: program effectiveness trends, comparison to industry benchmarks, regulatory compliance status, ROI calculation (phishing incidents prevented × average incident cost)
- Recommend department-specific training focus areas based on failure patterns

**Data Required:**
- Phishing simulation platform API (KnowBe4, Proofpoint)
- HR system for employee data, department structure, new hires
- Current threat intelligence on active phishing campaigns targeting banks
- Industry benchmark data for comparison
- Historical training and simulation data

**Autonomy Level:** Fully Autonomous for campaign execution and tracking; Human-in-the-Loop for HR escalations
Campaign scheduling, result processing, and remediation assignment are automated. HR escalations and disciplinary recommendations require human review.

**Example Interaction:**
> PhishGuard launches the February phishing simulation: a spoofed email appearing to be from the FDIC requesting urgent verification of the bank's deposit insurance information — modeled after a real campaign currently targeting regional banks. Of 8,400 employees, 312 click the link (3.7% click rate, down from 5.2% last quarter), and 47 enter credentials (0.56%). The agent processes results within the hour: "Highest risk department: Commercial Lending (8.1% click rate, 3x average). 12 employees are now at 3+ lifetime failures — HR escalation recommended. Wire operations team showed marked improvement: 1.2% click rate, down from 6.8% after targeted BEC training last quarter. Recommended: schedule focused social engineering training for Commercial Lending, include wire fraud scenario given their role. Board report updated with February data."

---

### Use Case 6: Security Project & Initiative Portfolio Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking CISOs manage portfolios of 20-40 concurrent security projects: technology deployments (SIEM migration, zero-trust implementation, cloud security posture management), compliance initiatives (NYDFS remediation, PCI DSS 4.0 upgrade, DORA compliance), and risk reduction programs (legacy system decommissioning, identity modernization, data loss prevention rollout). Each project involves multiple teams (security, IT operations, application development, vendors), has regulatory dependencies, and competes for limited engineering resources. Without portfolio-level visibility, the CISO can't effectively prioritize, identify resource conflicts, or communicate progress to the board risk committee. Most CISOs rely on a combination of project managers with individual project plans, monthly status decks assembled manually, and gut feeling.

#### The Solution
monday.com Work Management as the CISO's portfolio management platform. A Security Portfolio board provides the strategic view: every initiative with status, timeline, budget, resource allocation, and risk/compliance driver. Connected project boards manage individual initiative execution. Resource management views identify allocation conflicts and bottlenecks. Executive dashboards translate technical project status into board-ready risk language. Automations flag at-risk projects (behind schedule, over budget, dependency blocked) for CISO attention.

#### The Outcome
CISO can produce board risk committee update in 30 minutes instead of 2 days. Resource conflicts identified 4-6 weeks earlier, enabling proactive reallocation. 30% improvement in on-time project delivery through better visibility and earlier intervention. Clear linkage between security spending and risk reduction for budget justification.

#### Discovery Questions
- "How many active security projects and initiatives are you managing simultaneously?"
- "How do you currently communicate security program status to the board risk committee?"
- "When two security projects need the same engineering team at the same time, how do you resolve that?"
- "Can you show the direct connection between your security investments and measurable risk reduction?"
- "How do you prioritize between regulatory-driven initiatives and threat-driven initiatives when budgets are constrained?"

#### Industry Context
Banking boards are increasingly engaged on cybersecurity oversight (OCC Heightened Standards, SEC disclosure rules). They expect quarterly reporting on cybersecurity program status, risk posture, and investment effectiveness — not in technical jargon, but in business risk terms. The CISO must translate "we're implementing zero-trust network architecture" into "we're reducing our exposure to lateral movement attacks by 80%, addressing finding #3 from last year's OCC examination." Budget justification requires demonstrating ROI: "this $2M DLP investment prevents an estimated $15M-50M data breach." Portfolio management discipline is how CISOs maintain strategic coherence across dozens of competing priorities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a CISO Portfolio Management board for a bank. Columns: Initiative Name (text), Category (dropdown: Technology Deployment/Compliance Program/Risk Reduction/Architecture Transformation/Incident Capability/Third-Party Security/Identity & Access), Status (status: Planning/In Progress/On Track/At Risk/Blocked/Completed/Deferred), Priority (status: Must-Do Regulatory/Critical Risk/High/Medium/Strategic), Executive Sponsor (people), Project Lead (people), Start Date (date), Target Completion (date), Actual Completion (date), Budget Allocated (numbers $), Budget Spent (numbers $), Budget Variance (formula), Regulatory Driver (dropdown: OCC Finding/NYDFS Requirement/FFIEC Gap/PCI DSS 4.0/SEC Disclosure/DORA/Internal Risk Assessment/None), Risk Reduced (dropdown: Critical/High/Medium/Low — what risk does this address), Resource FTEs (numbers), Dependencies (connect boards), Board Reporting Status (dropdown: Green/Yellow/Red), Last Status Update (date). Groups: Regulatory-Mandated, Threat-Driven, Strategic, Operational. Automations: when Target Completion is within 30 days and Status is not On Track, auto-set Board Reporting Status to Yellow and notify CISO; when Budget Spent exceeds Budget Allocated, flag Red and notify CISO; when Status changes to Completed, trigger post-implementation review; weekly auto-remind Project Leads to update status if Last Status Update is >7 days old. Dashboard: portfolio health (Green/Yellow/Red breakdown), budget allocation vs. spend by category, timeline Gantt chart, resource allocation heat map, regulatory-driven vs. strategic split, completed initiatives this quarter."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CISOView Portfolio Intelligence
**Agent Purpose:** Synthesize security portfolio status into executive-ready reporting, identify resource conflicts, and predict project risks before they materialize.

**Triggers:**
- Weekly portfolio status review (every Monday)
- Project status unchanged for >14 days (stale update detection)
- Budget variance exceeds 15% on any initiative
- Board risk committee meeting scheduled (auto-generate board deck data)
- New regulatory requirement identified (assess portfolio impact)

**Actions:**
- Generate weekly CISO brief: portfolio health summary, projects at risk, resource bottlenecks, upcoming milestones, budget status
- Produce quarterly board risk committee report: executive summary, risk posture changes, regulatory compliance progress, investment effectiveness metrics
- Identify resource conflicts: multiple projects competing for same team during same timeframe, recommend prioritization based on regulatory criticality and risk impact
- Predict project delays based on historical patterns: projects with similar characteristics (scope, team, dependencies) that took longer than planned
- When new regulatory requirement emerges, assess which existing projects address it and identify gaps requiring new initiatives
- Calculate and visualize risk reduction: map completed initiatives to measurable risk posture improvement

**Data Required:**
- All security project boards and status data
- Resource allocation and team capacity data
- Budget and finance data
- Regulatory requirements and examination findings
- Historical project performance data
- Risk register and risk assessment data

**Autonomy Level:** Fully Autonomous for reporting and analysis; Human-in-the-Loop for prioritization decisions
Report generation, conflict identification, and risk prediction are automated. Resource allocation decisions and project prioritization changes require CISO approval.

**Example Interaction:**
> Monday morning, CISOView generates the weekly brief: "Portfolio: 34 active initiatives. 28 Green, 4 Yellow, 2 Red. RED: Zero Trust Phase 2 — blocked by network team capacity (shared with DORA compliance project, both need the same 3 network engineers in March). Recommendation: defer DORA network segmentation component by 4 weeks (still within regulatory deadline) to unblock Zero Trust. RED: PCI DSS 4.0 migration — vendor delayed delivery of updated payment module by 6 weeks. New completion estimate: June 15 (PCI deadline: March 31, 2025 already passed — this is remediation). Escalation recommended. YELLOW: SIEM migration — 12% over budget due to unexpected data volume. Requesting additional $180K. Board report for Thursday's risk committee meeting is pre-populated — review and approve by Wednesday."

---

### Use Case 7: Identity & Access Management (IAM) Governance

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banking regulators consider access management a foundational control. FFIEC, NYDFS, SOX, and PCI DSS all require periodic access reviews (recertification), privileged access management, and timely deprovisioning when employees leave or change roles. A mid-size bank may have 50,000-200,000 user-application entitlements to review quarterly or annually. Access reviews are typically managed through IAM tools (SailPoint, CyberArk, Saviynt) but the workflow around them — getting managers to actually complete reviews on time, handling exceptions, tracking remediation of inappropriate access, and producing audit evidence — often falls apart. Access review completion rates hover around 60-75% at many banks, creating significant examination risk and real security exposure.

#### The Solution
monday.com Work Management as the IAM governance workflow layer. An Access Review Campaign board manages each quarterly or annual review cycle with completion tracking by department and application. Connected boards track individual access exceptions and remediation items. Manager-facing views simplify the review process: clear lists of their team's access with approve/revoke actions. Automations handle escalation: reminder at 7 days, manager's manager at 14 days, CISO at 21 days. Privileged access reviews get separate, more frequent workflows with additional approvers.

#### The Outcome
Access review completion rates improved from 70% to 98%+ through automated escalation. 50% reduction in time managers spend on access reviews through simplified interface. Zero examination findings for incomplete access reviews. Timely identification and revocation of inappropriate access — average remediation time reduced from 30 days to 5 days.

#### Discovery Questions
- "What's your current access review completion rate, and how long does a full review cycle take?"
- "How do you handle privileged access reviews — are they on a different cadence than standard reviews?"
- "When a reviewer identifies inappropriate access, what's the remediation process and how long does it typically take?"
- "Have you received examination findings related to access management? What were they?"
- "How do you handle access for contractors and third-party users?"

#### Industry Context
Access management is consistently one of the top examination finding categories across all banking regulators. SOX 404 auditors specifically test ITGCs including access provisioning, review, and deprovisioning. The concept of "toxic combinations" (segregation of duties violations — e.g., someone who can both initiate and approve wire transfers) requires specialized analysis. Privileged access (admin accounts, database access, production server access) carries the highest risk and regulatory scrutiny. Dormant accounts (active credentials for departed employees) are a red-flag finding. The trend toward zero-trust architecture is redefining IAM from periodic reviews to continuous verification.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IAM Governance Tracker for a banking security team. Board 1 — Access Review Campaigns: columns for Campaign Name (text), Review Type (dropdown: Quarterly Standard/Annual Comprehensive/Privileged Access/SOX ITGC/Third-Party/Emergency), Status (status: Planning/Active/Escalation Phase/Completing/Closed/Audit Ready), Application (dropdown with 50+ common banking apps: Core Banking/Lending Platform/Treasury Management/Wire Transfer/SWIFT/Trading Platform/HR System/Email/VPN/Cloud Console/Database), Department Under Review (dropdown), Reviewer (people — the manager), Total Entitlements (numbers), Reviewed (numbers), Approved (numbers), Revoked (numbers), Exceptions (numbers), Completion Rate (formula: Reviewed/Total as %), Start Date (date), Due Date (date), Days Remaining (formula). Board 2 — Remediation & Exceptions: columns for Employee (text), Application (mirror), Entitlement (text), Issue Type (dropdown: Inappropriate Access/Segregation of Duties Violation/Dormant Account/Excessive Privilege/Orphan Account/Third-Party Overdue), Status (status: Identified/Revocation Requested/Revoked/Exception Requested/Exception Approved/Exception Denied), Remediation Owner (people), SLA Deadline (date), Risk Level (status: Critical-SOD Violation/High/Medium/Low), Exception Justification (long text), Exception Approved By (people). Automations: when Campaign Due Date is 7 days away and Completion Rate < 80%, notify Reviewer; at 14 days overdue, escalate to Reviewer's manager; at 21 days, escalate to CISO; when Issue Type is Segregation of Duties Violation, auto-set Risk Level to Critical and notify CISO; when Revocation Requested, create IT ticket via integration. Dashboard: campaign completion rates by department, remediation SLA compliance, SOD violations count, dormant account trend, privileged access review status, audit readiness score."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AccessGuard Governance Bot
**Agent Purpose:** Orchestrate access review campaigns, detect segregation of duties violations, and ensure timely remediation of inappropriate access.

**Triggers:**
- Quarterly/annual access review campaign start date
- HR system reports employee termination or role change
- Review completion rate below threshold at deadline milestones (50% at midpoint, 80% at 7 days before due)
- New application onboarded to IAM governance program
- SOX audit notification received

**Actions:**
- Generate access review packages for each manager: list of direct reports, their application access, and last review decisions for context
- Analyze entitlements for segregation of duties violations using predefined toxic combination rules (e.g., wire initiation + wire approval, trade execution + trade settlement)
- Send progressive escalation notifications for incomplete reviews
- Auto-detect dormant accounts: no login in 90 days with active credentials — flag for immediate review
- Generate SOX audit evidence package: complete review history, remediation documentation, exception approvals with justification
- Track employee terminations and verify deprovisioning: cross-reference HR termination date with application access removal — flag any accounts still active 24 hours after termination

**Data Required:**
- IAM platform APIs (SailPoint, CyberArk, Saviynt, Azure AD)
- HR system for org structure, role changes, terminations
- SOD rule matrix (toxic combinations by application)
- Application login activity logs
- Historical review and remediation data

**Autonomy Level:** Human-in-the-Loop
Campaign generation, violation detection, and escalation are automated. All access decisions (approve, revoke, exception) require human reviewer sign-off. SOD violations require CISO and business line approval for exceptions.

**Example Interaction:**
> It's Q1 access review season. AccessGuard launches campaigns for 47 applications across 12 departments — 156,000 total entitlements. For each manager, it generates a personalized review package: "You have 23 direct reports with 187 total entitlements across 14 applications. 3 items flagged for attention: (1) John Smith has wire transfer approval access but moved from Treasury to Marketing 4 months ago — likely inappropriate, recommend revoke. (2) Sarah Chen has both trade execution and trade settlement access in the trading platform — SOD violation, requires immediate review. (3) Mike Johnson's VPN credentials show no login in 127 days — dormant account." The manager reviews the flagged items in 10 minutes, approves the remaining 184 entitlements in bulk (all appropriate for current roles), and revokes the 3 flagged items. Completion: 100% for this manager, done in 12 minutes vs. the previous 3-hour spreadsheet exercise.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| SIEM | Security Information and Event Management — centralized log collection and threat detection (Splunk, Microsoft Sentinel, IBM QRadar) |
| SOC | Security Operations Center — team monitoring for and responding to security threats 24/7 |
| TPRM | Third-Party Risk Management — program for assessing and monitoring vendor security risk |
| IAM | Identity and Access Management — systems and processes for managing user identities and access rights |
| SOD | Segregation of Duties — control principle preventing one person from having conflicting responsibilities (e.g., initiating and approving transactions) |
| CVSS | Common Vulnerability Scoring System — industry standard for rating vulnerability severity (0-10 scale) |
| CISA KEV | Cybersecurity & Infrastructure Security Agency Known Exploited Vulnerabilities catalog — authoritative list of actively exploited CVEs |
| FFIEC CAT | Federal Financial Institutions Examination Council Cybersecurity Assessment Tool — framework examiners use to evaluate bank cyber programs |
| NYDFS 23 NYCRR 500 | New York Department of Financial Services cybersecurity regulation — among the most prescriptive state-level requirements |
| DORA | Digital Operational Resilience Act — EU regulation on ICT risk management for financial entities (effective January 2025) |
| Zero Trust | Security architecture model: "never trust, always verify" — no implicit trust based on network location |
| SOC 2 Type II | Service Organization Control report auditing a vendor's security, availability, and confidentiality controls over a period |
| PCI DSS | Payment Card Industry Data Security Standard — requirements for protecting cardholder data |
| MTTR | Mean Time to Remediate — average time from vulnerability discovery to fix |
| MTTD / MTTC | Mean Time to Detect / Mean Time to Contain — key incident response metrics |
| BEC | Business Email Compromise — social engineering attack targeting wire transfers and financial transactions |
| GRC | Governance, Risk, and Compliance — the framework for managing security program obligations |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Information Security Officer (CISO) | Owns cybersecurity strategy, budget, risk management, regulatory compliance | Decision-maker |
| VP, Security Operations | Manages SOC, incident response, threat detection | Decision-maker for tools |
| Director, GRC | Manages policy, compliance, audit preparation, regulatory engagement | Influencer / Champion |
| VP, Third-Party Risk Management | Oversees vendor security assessment program | Decision-maker for TPRM tools |
| Director, IAM | Manages identity governance, access reviews, privileged access | Influencer |
| Security Architects | Design security controls, evaluate tools, define standards | Influencer (technical authority) |
| Chief Information Officer (CIO) | CISO often reports to CIO; controls IT budget | Decision-maker (budget) |
| Board Risk Committee | Oversees cybersecurity risk at governance level | Ultimate authority |
| Chief Risk Officer (CRO) | Enterprise risk management, increasingly includes cyber risk | Influencer |
| Internal Audit (IT Audit) | Independent assessment of security controls | Influencer (findings drive action) |
| Examiners (OCC, Fed, FDIC) | Evaluate cybersecurity program during examinations | External authority |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT Operations | Executes remediation (patching, configuration changes), manages infrastructure | Joint vulnerability remediation workflows, change management integration |
| Risk Management (Enterprise) | Cyber risk feeds into enterprise risk appetite and reporting | Integrated risk dashboards, unified GRC platform |
| Compliance | Regulatory mapping, examination coordination, policy alignment | Shared GRC platform, compliance workflow automation |
| Legal | Incident response, breach notification, vendor contracts, regulatory engagement | Incident management coordination, contract workflow |
| Internal Audit | Tests security controls, provides independent assurance | Audit finding tracking, evidence management |
| HR | Employee onboarding/offboarding (access provisioning/deprovisioning), awareness training | IAM lifecycle integration, training compliance tracking |
| Application Development | Secure coding, AppSec testing, DevSecOps | Security requirements tracking, vulnerability management for code |
| Cloud Engineering | Cloud security posture, configuration management | Cloud security governance workflows |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow GRC / SecOps | Enterprise GRC and security operations platform | monday.com for teams that find ServiceNow too complex, expensive, and slow to customize. Faster time-to-value, more intuitive UX, 60-70% lower TCO. Best for TPRM, policy management, and project portfolio — not replacing SIEM/SOAR. |
| RSA Archer | Legacy GRC platform, strong in large banks | Aging UI, complex implementation, expensive. monday.com as modern alternative for mid-market banks or as supplementary workflow layer for specific use cases. |
| OneTrust | Third-party risk and privacy management | monday.com provides more flexible workflow customization for TPRM programs that don't need OneTrust's full privacy suite. |
| Jira / Confluence | Used by security teams for project tracking and documentation | monday.com offers better executive visibility, cross-functional workflows, and non-technical user experience. Security teams love Jira; CISOs need more. |
| Spreadsheets (Excel/Google Sheets) | The actual incumbent for most TPRM, vuln tracking, and awareness programs | monday.com replaces the spreadsheet chaos with structured workflows, automation, and real-time dashboards. This is the most common displacement. |
| KnowBe4 / Proofpoint SA | Security awareness training and phishing simulation | Not displacing — integrating. monday.com as the workflow orchestration layer around these tools (remediation tracking, compliance reporting, program management). |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have ServiceNow for security" | "ServiceNow is great for IT service management. But how's it working for TPRM, security awareness program management, and CISO portfolio reporting? Those workflow-heavy, cross-functional use cases are where monday.com excels — faster to build, easier for non-security stakeholders to use, and a fraction of the cost." |
| "Security data can't go in a cloud platform" | "monday.com is SOC 2 Type II certified, offers data residency options, HIPAA-capable, and provides enterprise-grade encryption and access controls. The question isn't whether cloud is secure enough — it's whether your current spreadsheets and shared drives are. They're not." |
| "Our security team will build their own tools" | "Your security engineers should be hunting threats, not building TPRM dashboards. monday.com gives them a platform they can customize in hours instead of building from scratch over months. Save the engineering cycles for security-specific problems." |
| "We need a FedRAMP-authorized tool" | "monday.com is pursuing FedRAMP authorization. In the meantime, for non-CUI workloads like TPRM workflow, project management, and awareness program tracking, monday.com meets the security bar with SOC 2, encryption, and access controls. Let's scope what can move now vs. what needs to wait." |
| "Examiners won't accept this as evidence" | "Examiners care about completeness, accuracy, and audit trail — not which tool you use. monday.com provides timestamped records, approval chains, version history, and exportable reports. That's better evidence than most banks produce from their current spreadsheet-based processes." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for banking security team TPRM case study]
- [Placeholder for financial services incident response workflow example]
- [Placeholder for regulated industry GRC/compliance management reference]
- [Placeholder for enterprise vulnerability management program]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
