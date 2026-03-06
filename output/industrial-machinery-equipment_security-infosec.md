# Industrial Machinery & Equipment × Security & Infosec Playbook

## Overview

Security and Information Security teams in industrial machinery and equipment companies operate at the intersection of IT security, operational technology (OT) security, and physical plant protection. These organizations manufacture heavy equipment—CNC machines, turbines, compressors, conveyor systems, packaging lines—and increasingly embed IoT sensors, PLCs, and networked controllers into their products and factory floors. The convergence of IT and OT networks has dramatically expanded the attack surface, making cybersecurity a board-level concern.

Typical org structures include a CISO or Director of Information Security reporting to the CIO or COO, with sub-teams covering IT security (network, endpoint, identity), OT/ICS security (SCADA, DCS, PLCs), product security (firmware, connected equipment), compliance (NIST, IEC 62443, ISO 27001), and physical security (facility access, surveillance). Headcount ranges from 5-15 in mid-market manufacturers to 50+ in large industrials with multiple plants.

Regulatory pressure is intensifying: NIS2 in Europe, CMMC for defense supply chain manufacturers, IEC 62443 for industrial automation, and sector-specific requirements from customers in energy, defense, and critical infrastructure. Supply chain security audits from OEM customers (Caterpillar, Siemens, John Deere) increasingly require documented cybersecurity programs, creating compliance urgency that didn't exist five years ago.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Security teams juggle 15-25 point tools (SIEM, vulnerability scanners, OT monitors, GRC platforms, ticketing). Consolidating visibility into a single operational layer saves licensing costs and reduces alert fatigue. |
| 2 | Replace or Radically Augment Headcount | High | Cybersecurity talent shortage is acute in manufacturing—rural plant locations can't compete with tech hubs for talent. AI-augmented workflows can multiply a lean team's capacity 3-5×. |
| 3 | Scale Impact Without Overhead | Medium-High | As plants add IoT/connected equipment and new regulatory mandates emerge, security workload grows exponentially while budgets grow linearly. Scaling programs without proportional headcount is essential. |

## Prioritized Use Cases

---

### Use Case 1: Unified Vulnerability Management Tracker

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Vulnerabilities arrive from multiple scanners (Qualys, Tenable, Nessus for IT; Claroty or Dragos for OT), email advisories from ICS-CERT, and manual penetration test reports. Security analysts spend 10-15 hours/week manually triaging, deduplicating, and assigning remediation tasks across IT and OT teams. Critical OT vulnerabilities in PLCs or HMIs often sit unpatched for months because there's no unified tracking that bridges IT ticketing (ServiceNow) and plant maintenance (SAP PM). Mean time to remediate (MTTR) for critical vulnerabilities averages 45-90 days—far above the 15-day target.

#### The Solution
monday.com Work Management as the central vulnerability operations hub. Boards structured by asset type (IT Infrastructure, OT/ICS, Product Firmware) with items representing individual CVEs. Columns: CVE ID (text), CVSS Score (number), Asset Affected (dropdown), Plant Location (dropdown), Scanner Source (dropdown), Discovery Date (date), SLA Due Date (date with formula), Owner (people), Remediation Status (status: Open → Triaged → Scheduled → Patched → Verified), Risk Acceptance (checkbox + approval workflow). Integrations pull from scanner APIs. Dashboard views show MTTR trends, aging vulnerabilities, SLA compliance by plant, and OT vs. IT remediation velocity.

#### The Outcome
Reduce MTTR from 60+ days to under 20 days. Eliminate 12+ hours/week of manual triage. Achieve 95%+ SLA compliance for critical/high vulnerabilities. Provide audit-ready reporting for IEC 62443 and CMMC assessments without manual spreadsheet compilation.

#### Discovery Questions
1. "How do you currently track vulnerabilities across both your IT network and plant-floor OT systems—is that unified or separate workflows?"
2. "When ICS-CERT publishes an advisory affecting a PLC or HMI you use, what's the process from advisory to patch verification on the plant floor?"
3. "What's your current mean time to remediate for critical vulnerabilities, and does that differ between IT and OT assets?"
4. "How do you report vulnerability posture to the board or to OEM customers conducting supply chain audits?"
5. "How many different scanning tools feed into your remediation workflow today?"

#### Industry Context
In industrial manufacturing, OT patching is fundamentally different from IT patching. You can't just push a Windows update to a PLC running a $2M stamping press during a production shift. Maintenance windows are rare (quarterly shutdowns), and firmware updates require vendor coordination. SEs should understand that "patching" in OT often means compensating controls (network segmentation, firewall rules) rather than actual software updates. ICS-CERT advisories (now CISA ICS advisories) are the primary vulnerability intelligence source for OT. IEC 62443 is the gold standard for industrial cybersecurity maturity.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vulnerability Management Tracker for an industrial manufacturer. Create a board called 'Vulnerability Operations Center' with these columns: CVE ID (text), Vulnerability Title (text), CVSS Score (number), Severity (status: Critical in red, High in orange, Medium in yellow, Low in green), Asset Type (dropdown: IT Server, IT Endpoint, Network Device, PLC/RTU, HMI/SCADA, Product Firmware), Asset Name (text), Plant Location (dropdown: HQ, Plant 1 - Ohio, Plant 2 - Texas, Plant 3 - Germany), Scanner Source (dropdown: Qualys, Tenable, Claroty, ICS-CERT Advisory, Pen Test, Manual), Discovery Date (date), SLA Due Date (date), Remediation Owner (people), Status (status: New → Triaged → Remediation Planned → Patch Scheduled → Patched → Verified → Risk Accepted), Compensating Control (long text), Risk Acceptance Approved By (people). Create groups: Critical/High Active, Medium Active, Pending Verification, Risk Accepted, Closed. Add automations: when Status is 'New' for more than 2 days notify the security team lead; when SLA Due Date arrives and Status is not 'Patched' or 'Verified' change Severity label to 'SLA Breach' and notify CISO; when Status changes to 'Patched' assign to original scanner owner for verification. Create a Dashboard with widgets: vulnerability count by Severity (pie chart), MTTR trend by month (chart), open vulnerabilities by Plant Location (bar chart), SLA compliance percentage (number), aging vulnerabilities over 30 days (table), IT vs OT split (pie chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VulnOps Triage Agent
**Agent Purpose:** Automatically triage incoming vulnerabilities, enrich with asset context, calculate risk-adjusted priority, and assign to the correct remediation team.

**Triggers:**
- New item created on Vulnerability Operations Center board (from scanner integration or manual entry)
- ICS-CERT advisory keyword match in RSS feed integration
- Weekly scheduled scan of all open items for SLA deadline proximity
- Status changed to "Patched" (triggers verification workflow)

**Actions:**
- Enrich CVE with NVD data (CVSS vector, exploit availability, affected products) and auto-populate CVSS Score and Severity
- Cross-reference Asset Name against CMDB/asset inventory board to identify asset criticality, plant location, and business impact
- Calculate risk-adjusted priority: CVSS × Asset Criticality × Exploit Availability × Network Exposure
- Auto-assign to IT Security team (IT assets) or OT Security team (PLC/HMI/SCADA) based on Asset Type
- Generate compensating control recommendations for OT assets where direct patching isn't feasible
- Escalate to CISO when: critical + exploited-in-the-wild + internet-facing, or SLA breach on any critical vulnerability

**Data Required:**
- NVD/CVE API access for enrichment
- Asset inventory board (CMDB equivalent) with asset criticality ratings
- Plant maintenance schedule board (to identify next available patching windows for OT)
- Team assignment rules (which team owns which asset categories)

**Autonomy Level:** Human-in-the-Loop
Auto-triages and assigns all Medium/Low vulnerabilities. Critical/High vulnerabilities are triaged and recommended but require human confirmation before assignment. Risk acceptance decisions always require CISO approval.

**Example Interaction:**
> The VulnOps Triage Agent detects a new item on the board: CVE-2025-4471, a critical (CVSS 9.8) remote code execution vulnerability in Siemens S7-1500 PLC firmware. The agent queries the asset inventory and finds 14 affected PLCs across Plant 1 (Ohio) and Plant 3 (Germany), all running firmware version 2.9.4. It checks CISA's Known Exploited Vulnerabilities catalog and confirms active exploitation in the wild. The agent immediately escalates to the CISO with a summary: "Critical RCE in 14 S7-1500 PLCs across 2 plants. Actively exploited. No patch available from Siemens yet. Recommending immediate compensating controls: isolate affected PLCs from enterprise network, enable Claroty monitoring rules for exploit signatures, and schedule emergency maintenance window." It creates sub-items for each compensating control, assigns them to the OT Security Lead and Network Engineering, and sets a 48-hour SLA. The agent also drafts a customer notification template for the product security team, since the company ships equipment using the same PLC model.

---

### Use Case 2: IT/OT Security Incident Response Workflow

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
When a security incident hits—ransomware on the corporate network, anomalous traffic from a PLC, or a phishing compromise—the response is chaotic. The IR plan lives in a 40-page PDF that nobody reads during a crisis. Communication happens over ad-hoc Slack messages and phone calls. OT incidents require plant operations, maintenance, and engineering involvement, but those teams aren't in the security tools. Post-incident reviews reveal the same gaps: unclear ownership, missed containment steps, delayed executive communication. Manufacturers that have experienced ransomware (and 65% of manufacturing firms reported attacks in 2024) know the cost: $1.5-4M average per incident including production downtime.

#### The Solution
monday.com Work Management as the incident response orchestration platform. A master "Security Incidents" board with items per incident. Columns: Incident ID (auto-number), Incident Title (text), Severity (status: SEV1-Critical, SEV2-High, SEV3-Medium, SEV4-Low), Type (dropdown: Ransomware, Phishing, OT Anomaly, Data Breach, Insider Threat, Physical), Affected Zone (dropdown: Corporate IT, Plant Floor OT, Product/Customer, Cloud), Incident Commander (people), Status (status: Detected → Contained → Eradicated → Recovered → Lessons Learned → Closed), Detection Source (dropdown: SIEM, OT Monitor, User Report, Threat Intel, Physical). Connected sub-item boards for Containment Tasks, Evidence Collection, Communications Log, and Regulatory Notifications. Automated playbook execution via automations that create standardized task sets based on incident type.

#### The Outcome
Reduce mean time to contain from 8+ hours to under 2 hours through automated playbook execution. Ensure 100% of regulatory notification deadlines are met (NIS2 requires 24-hour initial notification). Cut post-incident review prep time from 2 days to 2 hours with auto-documented timelines. Enable non-security staff (plant managers, maintenance) to participate in IR without security tool access.

#### Discovery Questions
1. "When you had your last significant security incident, how did you coordinate between the SOC, plant operations, and executive leadership?"
2. "Do your incident response playbooks account for OT-specific scenarios like PLC compromise or safety system anomalies?"
3. "How do you currently document incident timelines and actions for post-incident review and regulatory reporting?"
4. "If ransomware hit your corporate network at 2 AM, who gets called and in what order—is that documented and tested?"
5. "How do you handle NIS2 or other regulatory notification requirements during an active incident?"

#### Industry Context
Manufacturing IR is uniquely complex because IT and OT have different priorities. IT security's instinct is "isolate and contain"—but isolating the OT network from IT might mean PLCs lose connectivity to historian servers, and operators lose visibility into production. Shutting down a blast furnace or chemical process without proper procedure can cause physical damage or safety hazards. IR plans must include "safe shutdown" procedures coordinated with plant operations. The Purdue Model (Levels 0-5) defines IT/OT network segmentation—SEs should understand that Level 3 (site operations) is where IT and OT converge and where most lateral movement happens.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Incident Response system for an industrial manufacturer. Create a board called 'Security Incidents' with these columns: Incident ID (auto-number), Title (text), Severity (status: SEV1-Critical in red, SEV2-High in orange, SEV3-Medium in yellow, SEV4-Low in green), Incident Type (dropdown: Ransomware, Phishing/Social Engineering, OT Network Anomaly, Data Breach, Insider Threat, Supply Chain Compromise, Physical Security), Affected Zone (dropdown: Corporate IT, Plant Floor OT, DMZ/Level 3, Cloud Infrastructure, Product/Customer-Facing), Detection Source (dropdown: SIEM Alert, OT Monitor/Claroty, User Report, Threat Intelligence, Automated Scan, Physical Security), Incident Commander (people), Current Phase (status: Detected → Triage → Containment → Eradication → Recovery → Post-Incident Review → Closed), Plant Impact (status: No Impact, Monitoring, Degraded Operations, Production Stopped), Executive Notified (checkbox), Regulatory Notification Required (checkbox), Notification Deadline (date), Timeline Log (long text). Create groups: Active Incidents, Under Review, Closed (Last 90 Days). Add automations: when Severity is SEV1-Critical, immediately notify CISO and CIO and set Notification Deadline to 24 hours from now; when Current Phase changes to Containment, create sub-items from template (Isolate Affected Systems, Preserve Evidence, Notify Legal, Update Executive Brief, Assess Plant Impact); when Regulatory Notification Required is checked and Notification Deadline is approaching, send urgent reminder to Legal and CISO. Create a connected board called 'IR Task Tracker' for sub-tasks with columns: Task (text), Owner (people), Priority (status), Due (date), Completed (checkbox), Evidence Attached (file). Create a Dashboard with: active incidents by severity (chart), mean time to contain trend (chart), incidents by type last 12 months (bar chart), open IR tasks (table), regulatory notification compliance rate (number)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Incident Response Orchestrator
**Agent Purpose:** Automate incident triage, execute response playbooks, coordinate cross-functional teams, and ensure regulatory compliance during security incidents.

**Triggers:**
- New incident item created (from SIEM integration, manual report, or OT monitoring alert)
- Severity escalation (SEV3 → SEV2 or higher)
- Phase transition (e.g., Containment → Eradication)
- Regulatory Notification Deadline approaching (24h, 12h, 4h, 1h warnings)
- Scheduled: daily check for incidents open > 72 hours without phase progression

**Actions:**
- Auto-classify incident type and severity based on detection source data and affected assets
- Instantiate the correct response playbook (create task sub-items specific to incident type: ransomware playbook differs from OT anomaly playbook)
- Assign Incident Commander based on severity and affected zone (IT Security Lead for corporate, OT Security Lead for plant floor, CISO for SEV1)
- Generate executive briefing summary updated every 2 hours during active SEV1/SEV2 incidents
- Track regulatory notification deadlines and auto-draft notification templates for NIS2, state breach notification laws
- After incident closure, auto-generate post-incident review document with full timeline, actions taken, and recommended improvements

**Data Required:**
- SIEM alert feed (Splunk, Microsoft Sentinel, etc.)
- OT monitoring platform alerts (Claroty, Dragos, Nozomi)
- Employee directory with on-call rotations
- Regulatory notification requirement matrix (by jurisdiction and data type)
- Historical incident database for pattern analysis

**Autonomy Level:** Escalation-Based
Fully autonomous for SEV3/SEV4 incidents (auto-triage, assign, create tasks). SEV2 incidents are triaged with recommendations but require IC confirmation. SEV1 incidents trigger immediate human escalation with pre-populated response plan—all actions require human authorization. Regulatory notifications always require Legal review before sending.

**Example Interaction:**
> At 3:47 AM, the OT monitoring platform detects anomalous Modbus TCP traffic from a packaging line PLC at Plant 2 (Texas). The Incident Response Orchestrator creates a new SEV2 incident, classifying it as "OT Network Anomaly." It assigns the OT Security Lead as Incident Commander and creates the OT-specific playbook tasks: capture network traffic (assign to SOC analyst), isolate affected network segment at Level 3 switch (assign to network engineer, with warning: "Verify packaging line can operate in local mode before isolation"), contact PLC vendor for firmware integrity check (assign to OT engineer), and notify Plant 2 operations manager of potential production impact. The agent checks the production schedule and notes that the packaging line is running a high-priority customer order due in 36 hours. It adds this context to the executive brief: "Containment may impact Order #4471 delivery timeline. Recommend parallel discussion with Supply Chain." Two hours later, the SOC analyst confirms the traffic is a compromised HMI running unauthorized remote access software. The agent escalates to SEV1, notifies the CISO, and expands the playbook with data breach assessment tasks and NIS2 notification countdown.

---

### Use Case 3: Compliance & Audit Management (IEC 62443 / CMMC / ISO 27001)

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Industrial manufacturers face a growing matrix of compliance requirements: IEC 62443 for industrial automation security, CMMC for defense supply chain, ISO 27001 for general information security, SOC 2 for cloud-connected products, and customer-specific security questionnaires. Each framework has hundreds of controls, and evidence collection for audits consumes 200-400 hours annually. The security team maintains separate spreadsheets for each framework, duplicating effort where controls overlap (60-70% overlap between ISO 27001 and IEC 62443). When a customer sends a security questionnaire, the team spends 2-3 days manually pulling evidence from scattered systems.

#### The Solution
monday.com Work Management as a unified compliance management platform. A master "Security Controls" board with one item per control, mapped across frameworks. Columns: Control ID (text), Control Description (long text), Framework Mapping (tags: IEC 62443, CMMC, ISO 27001, SOC 2, NIST CSF), Control Owner (people), Implementation Status (status: Not Started → In Progress → Implemented → Evidenced → Audit-Ready), Evidence Location (link), Last Evidence Date (date), Next Review Date (date), Risk Rating (status: Compliant, Minor Gap, Major Gap, Not Applicable). Connected boards for Audit Engagements (tracking individual audits), Evidence Repository, and Customer Security Questionnaires. Dashboard showing compliance posture by framework, control gap heatmaps, and upcoming evidence deadlines.

#### The Outcome
Reduce audit preparation time by 60% (from 400 hours to 160 hours annually). Eliminate duplicate control tracking across frameworks. Respond to customer security questionnaires in 1-2 days instead of 1-2 weeks. Maintain continuous compliance posture visibility instead of annual scrambles. Pass IEC 62443 SL2 certification on first attempt.

#### Discovery Questions
1. "How many different compliance frameworks are you currently managing, and do you track control overlaps between them?"
2. "When an auditor asks for evidence of a specific control, how long does it take your team to locate and compile it?"
3. "How do you handle the 200+ security questionnaires from customers and prospects each year?"
4. "Are you pursuing IEC 62443 certification, and if so, what security level are you targeting?"
5. "How do you currently track remediation of audit findings across frameworks?"

#### Industry Context
IEC 62443 is organized into Security Levels (SL1-SL4) and zones/conduits architecture. Most manufacturers target SL2 (protection against intentional violation using simple means). CMMC 2.0 has three levels; Level 2 (Advanced) applies to manufacturers handling CUI (Controlled Unclassified Information) in defense contracts. The overlap between frameworks is significant but the mapping is non-trivial—understanding that ISO 27001 Annex A.8 (Asset Management) maps to IEC 62443-2-1 Section 4.2.3.4 is the kind of detail that makes or breaks efficient compliance management.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Compliance & Audit Management system for an industrial manufacturer. Create a board called 'Security Controls Library' with columns: Control ID (text), Control Title (text), Description (long text), Frameworks (tags: IEC 62443, CMMC 2.0, ISO 27001, SOC 2, NIST CSF, Customer-Specific), Control Domain (dropdown: Access Control, Network Security, Incident Response, Asset Management, Risk Management, Physical Security, Supply Chain, Data Protection, Monitoring & Logging, Business Continuity), Owner (people), Implementation Status (status: Not Implemented in red, In Progress in yellow, Implemented in blue, Evidenced in green, Audit-Ready in purple), Evidence Link (link), Evidence Last Updated (date), Next Review Due (date), Gap Notes (long text), Risk Level (status: Compliant, Minor Gap, Major Gap, N/A). Create groups organized by IEC 62443 Foundational Requirements: FR1-Identification & Authentication, FR2-Use Control, FR3-System Integrity, FR4-Data Confidentiality, FR5-Restricted Data Flow, FR6-Timely Response, FR7-Resource Availability. Add automations: when Next Review Due arrives, notify Owner and change status to 'Review Required'; when Implementation Status changes to 'Evidenced' set Evidence Last Updated to today; monthly notification to CISO summarizing controls with Major Gaps. Create a connected board called 'Audit Tracker' with columns: Audit Name (text), Framework (dropdown), Auditor (text), Audit Date (date), Status (status: Scheduled, Preparation, In Progress, Findings Remediation, Closed), Findings Count (number), Critical Findings (number). Create a Dashboard showing: compliance percentage by framework (chart), controls by implementation status (pie chart), overdue evidence reviews (table), gap heatmap by domain (chart), upcoming audits timeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Compliance Navigator Agent
**Agent Purpose:** Automate control mapping across frameworks, track evidence currency, generate audit-ready reports, and auto-respond to customer security questionnaires.

**Triggers:**
- New framework added to a control's tags (triggers cross-mapping verification)
- Evidence Last Updated exceeds 90 days on any control
- New audit engagement created on Audit Tracker board
- Customer security questionnaire uploaded (form submission)
- Monthly scheduled compliance posture report

**Actions:**
- Auto-map new controls across frameworks (e.g., when adding a CMMC control, identify overlapping ISO 27001 and IEC 62443 controls already tracked)
- Flag stale evidence (>90 days old) and notify control owners with specific evidence refresh instructions
- Pre-populate audit preparation checklists based on framework and scope
- Parse incoming customer security questionnaires (PDF/Excel), match questions to existing controls, and draft responses with current evidence links
- Generate executive compliance dashboard summaries with trend analysis and risk highlights

**Data Required:**
- Framework control mapping database (IEC 62443 ↔ ISO 27001 ↔ CMMC ↔ NIST CSF crosswalk)
- Evidence repository (SharePoint/OneDrive links, screenshots, policy documents)
- Historical audit findings and remediation tracking
- Customer questionnaire templates library

**Autonomy Level:** Human-in-the-Loop
Auto-maps controls and drafts questionnaire responses, but all external-facing outputs (audit evidence packages, customer questionnaire responses) require security team review before submission. Internal tracking (evidence reminders, status updates, report generation) is fully autonomous.

**Example Interaction:**
> A major automotive OEM customer sends a 150-question security assessment as part of their annual supply chain review. The Compliance Navigator Agent parses the Excel file, identifies that 112 questions map to controls already tracked in the Security Controls Library (87 with current evidence, 25 with stale evidence). It auto-drafts responses for the 87 evidenced controls, pulling in policy references, tool configurations, and certification dates. For the 25 stale-evidence controls, it notifies the respective owners: "Caterpillar supply chain audit requires updated evidence for Control AC-7 (Unsuccessful Login Attempts). Your last evidence is from August 2025. Please update by March 1." For the remaining 38 unmapped questions, it flags them for manual review with suggested control mappings. The security team reviews and approves the responses in 6 hours instead of the usual 3 days. The agent also identifies 4 questions pointing to gaps where the company lacks formal documentation and creates remediation items on the controls board.

---

### Use Case 4: Security Awareness & Phishing Simulation Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Manufacturing companies have diverse workforces: corporate office staff, plant-floor operators, field service technicians, and remote engineers. Each group has different security risks and different levels of technology access. Phishing simulation results are trapped in the email security vendor's portal (KnowBe4, Proofpoint). Training completion data lives in the LMS. Actual phishing incidents are tracked in the SIEM. There's no unified view of human risk by department, plant, or role. Plant-floor workers who rarely use email still need training on USB threats, badge tailgating, and social engineering at the loading dock. The security team can't demonstrate program effectiveness to leadership beyond "we sent X simulations."

#### The Solution
monday.com Work Management as the security awareness program management hub. Board for "Phishing Campaign Tracker" with items per campaign: Campaign Name, Target Group (dropdown: Corporate, Plant 1, Plant 2, Field Service, Executive), Send Date, Click Rate (number), Report Rate (number), Failure Rate (number), Training Assigned (status). Connected "Security Training Matrix" board tracking: Employee Group, Required Courses, Completion %, Due Date, Compliance Status. Dashboard combining phishing metrics, training completion, and actual incident correlation (high-click-rate departments vs. actual phishing incidents).

#### The Outcome
Achieve 95%+ security training completion across all employee groups including plant-floor workers. Reduce phishing click rates from industry average 30% to under 5% within 12 months. Demonstrate program ROI by correlating training investment with incident reduction. Identify highest-risk groups for targeted intervention. Meet compliance training requirements for ISO 27001 and CMMC.

#### Discovery Questions
1. "How do you deliver security awareness training to plant-floor workers who may not have corporate email or computer access?"
2. "Can you currently correlate your phishing simulation results with actual phishing incidents to measure program effectiveness?"
3. "How do you track that contractors and temporary workers complete required security training before accessing your networks?"
4. "What's your current phishing click rate, and how does it vary across departments and plants?"

#### Industry Context
Manufacturing has among the highest phishing susceptibility rates across industries (28-35% average click rate) due to workforce diversity and lower baseline security awareness among production staff. Many plant workers access systems through shared workstations or kiosks, complicating individual training tracking. USB-based attacks remain a significant vector—operators plug in personal devices, and attackers drop infected USBs in parking lots (still works, still common). Tailgating at plant entrances is a physical security vector unique to manufacturing environments.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Awareness Program Manager for a manufacturing company. Create a board called 'Phishing Campaign Tracker' with columns: Campaign Name (text), Target Group (dropdown: All Corporate, Plant 1 - Ohio, Plant 2 - Texas, Plant 3 - Germany, Field Service, Executive Team, IT Department), Launch Date (date), Total Recipients (number), Emails Opened (number), Links Clicked (number), Click Rate (number with percentage format), Credentials Submitted (number), Reported to SOC (number), Report Rate (number with percentage), Campaign Status (status: Planned, Active, Completed, Analyzed), Risk Rating (status: Low Risk under 5%, Moderate 5-15%, High Risk over 15%), Follow-up Training (status: Not Required, Assigned, Completed). Create groups: 2026 Q1 Campaigns, 2026 Q2 Campaigns, Completed Campaigns. Create a second board called 'Security Training Matrix' with columns: Employee Group (dropdown: Corporate Staff, Plant Operators, Maintenance Technicians, Field Service Engineers, Contractors, Executives), Training Module (text), Delivery Method (dropdown: Online LMS, In-Person Workshop, Toolbox Talk, Kiosk Module, Video), Required By (dropdown: ISO 27001, CMMC, IEC 62443, Company Policy), Assigned Count (number), Completed Count (number), Completion Rate (number), Due Date (date), Status (status: On Track, At Risk, Overdue, Complete). Add automations: when Click Rate exceeds 15% change Risk Rating to High Risk and create follow-up training item; when Completion Rate is below 80% and Due Date is within 2 weeks change status to At Risk and notify training coordinator. Create a Dashboard with: click rate trend by quarter (line chart), click rate by target group (bar chart), training completion by employee group (bar chart), highest risk departments (table), phishing vs actual incidents correlation (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Human Risk Intelligence Agent
**Agent Purpose:** Analyze security awareness program data to identify highest-risk employee groups, recommend targeted interventions, and correlate training with incident reduction.

**Triggers:**
- Phishing campaign status changes to "Completed"
- Training module deadline approaching with completion below 80%
- Monthly scheduled human risk score recalculation
- New security incident involving social engineering or human error

**Actions:**
- Calculate department-level and plant-level Human Risk Scores combining: phishing click rate, training completion, actual incident history, and access privilege level
- Identify "repeat clickers" and recommend progressive interventions (additional training → manager notification → access restriction)
- Generate targeted campaign recommendations: "Plant 2 maintenance team has 32% click rate on invoice-themed phishing—recommend focused training on vendor impersonation"
- Correlate training completion with incident rates and generate quarterly ROI reports
- Auto-assign follow-up training modules based on simulation failure type

**Data Required:**
- Phishing simulation platform API (KnowBe4, Proofpoint)
- LMS training completion data
- Security incident board (for correlation)
- HR system employee data (department, location, role)

**Autonomy Level:** Fully Autonomous
All analytics, scoring, and recommendations run automatically. Training assignments auto-generated. Manager notifications for repeat offenders require security team approval before sending.

**Example Interaction:**
> After the March phishing campaign completes, the Human Risk Intelligence Agent analyzes results: overall click rate 8.2% (down from 12.4% in January). However, it identifies an anomaly—Plant 3 (Germany) field service engineers had a 28% click rate on a shipping notification theme, up from 9% last quarter. The agent investigates and correlates this with three recent actual phishing emails targeting the same group with DHL-branded lures. It recommends: "Immediate targeted training for Plant 3 field service (22 employees) on logistics/shipping phishing. Consider adding DHL-specific phishing template to next simulation. Alert SOC to increase monitoring on Plant 3 VPN connections." It auto-creates training items and notifies the regional security coordinator.

---

### Use Case 5: Third-Party / Supply Chain Risk Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Industrial manufacturers have deep supply chains: raw material suppliers, component vendors, subcontract manufacturers, logistics providers, software/SaaS vendors, and MRO (maintenance, repair, operations) suppliers. Each represents a potential attack vector. The 2020 SolarWinds and 2021 Kaseya attacks demonstrated that supply chain compromises can cascade to thousands of organizations. Yet most manufacturers manage vendor security assessments in email and spreadsheets. Vendor security questionnaires are sent once during onboarding and never updated. There's no continuous monitoring of supplier security posture. When a major supplier has a breach, the security team scrambles to determine exposure.

#### The Solution
monday.com Work Management as the vendor security risk management platform. "Vendor Risk Registry" board with items per vendor. Columns: Vendor Name (text), Category (dropdown: Software/SaaS, Component Supplier, Subcontract Manufacturer, Logistics, MRO, Professional Services), Data Access Level (dropdown: None, Limited, Sensitive, Critical), Network Access (dropdown: None, VPN, Direct Connect, Cloud Integration), Risk Tier (status: Tier 1-Critical, Tier 2-High, Tier 3-Standard, Tier 4-Low), Assessment Status (status: Not Assessed, Questionnaire Sent, Under Review, Approved, Conditional, Rejected), Last Assessment (date), Next Assessment Due (date), Risk Score (number), Owner (people). Connected boards for Assessment Questionnaires, Findings & Remediation, and Continuous Monitoring Alerts.

#### The Outcome
Achieve 100% vendor assessment coverage for Tier 1 and Tier 2 vendors (vs. typical 40-60%). Reduce vendor onboarding security review time from 3 weeks to 5 days. Enable continuous risk monitoring instead of point-in-time assessments. Meet CMMC and IEC 62443 supply chain security requirements. Respond to vendor breach notifications within 4 hours with impact analysis.

#### Discovery Questions
1. "How many vendors have network access or handle sensitive data in your environment, and what percentage have completed a security assessment in the last 12 months?"
2. "When Log4Shell hit, how long did it take to determine which of your vendors were affected and what your exposure was?"
3. "Do you differentiate vendor security requirements based on their access level—for example, a PLC firmware vendor vs. an office supply company?"
4. "How do you monitor ongoing vendor security posture between annual assessments?"

#### Industry Context
In manufacturing, supply chain security has a physical dimension: a compromised component supplier could introduce tampered firmware in PLCs or sensors. The SolarWinds attack was software supply chain; Stuxnet was essentially a supply chain attack on industrial equipment. CMMC requires "flow-down" of security requirements to subcontractors handling CUI. IEC 62443 addresses supply chain in Part 2-4 (Security requirements for IACS service providers) and Part 4-1 (Secure product development lifecycle). Vendor risk tiering is essential—a company may have 500+ suppliers but only 30-50 with meaningful security exposure.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Security Risk Management system for an industrial manufacturer. Create a board called 'Vendor Risk Registry' with columns: Vendor Name (text), Vendor Category (dropdown: Software/SaaS, Component Supplier, Subcontract Manufacturer, Logistics Provider, MRO Supplier, Professional Services, Cloud Provider), Primary Contact (text), Data Access Level (dropdown: No Data Access, Non-Sensitive Only, Sensitive/PII, Critical/IP, CUI-Controlled Unclassified), Network Access Type (dropdown: No Access, Internet-Facing API, VPN Access, Direct Network Connection, OT Network Access), Risk Tier (status: Tier 1-Critical in red, Tier 2-High in orange, Tier 3-Standard in yellow, Tier 4-Low in green), Assessment Status (status: Not Assessed, Questionnaire Sent, Questionnaire Received, Under Review, Approved, Conditional Approval, Rejected, Reassessment Required), Last Assessment Date (date), Next Assessment Due (date), Composite Risk Score (number 1-100), Assessment Owner (people), Contract Expiry (date), Findings Open (number), CMMC Flow-Down Required (checkbox). Create groups: Tier 1 - Critical Vendors, Tier 2 - High Risk, Tier 3 - Standard, Tier 4 - Low / Not Yet Tiered. Add automations: when Next Assessment Due is within 30 days notify Assessment Owner; when Assessment Status is Questionnaire Sent for more than 14 days send reminder and notify procurement contact; when Risk Tier is Tier 1-Critical and Assessment Status is Not Assessed for more than 7 days escalate to CISO. Create a Dashboard with: vendor count by Risk Tier (pie chart), assessment completion rate by tier (bar chart), vendors with open critical findings (table), upcoming assessment deadlines (calendar), risk score distribution (histogram), CMMC flow-down compliance rate (number)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Supply Chain Risk Sentinel
**Agent Purpose:** Continuously monitor vendor security posture, automate risk tiering, and provide rapid impact analysis when vendor breaches occur.

**Triggers:**
- New vendor added to registry (from procurement integration or form)
- Vendor breach reported in threat intelligence feeds
- Assessment questionnaire response received
- Quarterly scheduled risk score recalculation
- Contract renewal approaching (90 days before expiry)

**Actions:**
- Auto-tier new vendors based on data access level and network access type using risk matrix
- Scan external threat intelligence sources for vendor breach notifications and vulnerability disclosures
- When vendor breach detected: identify all systems/data the vendor touches, assess blast radius, draft impact assessment, notify incident response team
- Parse completed security questionnaires and auto-score against assessment criteria, flagging high-risk answers for manual review
- Generate risk trending reports showing vendor posture changes over time
- Flag vendors approaching contract renewal that have overdue assessments or open critical findings

**Data Required:**
- Procurement/ERP vendor master list
- Threat intelligence feeds (SecurityScorecard, BitSight, or OSINT)
- Network access control logs (which vendors connect to what)
- Historical assessment results and findings

**Autonomy Level:** Human-in-the-Loop
Auto-tiers Tier 3/4 vendors and processes routine assessments. Tier 1/2 assessments and all rejection/conditional approval decisions require human review. Breach impact assessments are auto-generated but response actions require security team authorization.

**Example Interaction:**
> The Supply Chain Risk Sentinel detects a cybersecurity news alert: Rexroth (Bosch subsidiary), a Tier 1 vendor providing hydraulic control systems with direct OT network connectivity at Plant 1 and Plant 2, has disclosed a critical vulnerability in their ctrlX CORE controllers. The agent immediately queries the Vendor Risk Registry, identifies 23 Rexroth controllers across two plants, cross-references with the vulnerability management board, and generates an impact brief: "Rexroth CVE-2026-1847 affects ctrlX CORE firmware <1.20. You have 23 units, 14 running firmware 1.18. Vendor has released patch. Recommend: (1) Contact Rexroth support for patch deployment timeline, (2) Apply compensating network controls immediately, (3) Increase OT monitoring for affected controller IP ranges." It creates a SEV2 incident on the Security Incidents board, links it to the vendor record, and notifies the OT Security Lead and Vendor Relationship Manager simultaneously.

---

### Use Case 6: Security Asset Inventory & OT/IT CMDB

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
"You can't protect what you can't see." In industrial environments, asset inventory is notoriously incomplete. IT assets are partially tracked in Active Directory and endpoint management tools, but OT assets—PLCs, HMIs, RTUs, switches, historians, engineering workstations—are often undocumented or tracked in plant maintenance systems (SAP PM, Maximo) without security-relevant attributes. Nobody knows exactly how many Windows XP machines are still running on the plant floor (it's always more than you think). When a vulnerability is disclosed for a specific PLC model, the first question is "do we have any of those?"—and it takes days to answer.

#### The Solution
monday.com Work Management as the unified security asset inventory. "Security Asset Inventory" board with items per asset. Columns: Asset ID (text), Asset Name (text), Asset Type (dropdown: Server, Workstation, Network Device, PLC, HMI, RTU, SCADA Server, Historian, Engineering Workstation, IoT Sensor, Mobile Device), Zone (dropdown per Purdue Model: Level 0-Process, Level 1-Control, Level 2-Supervisory, Level 3-Site Ops, Level 3.5-DMZ, Level 4-Enterprise, Level 5-Cloud), Plant Location (dropdown), OS/Firmware (text), Version (text), End of Life (date), Network Segment (text), IP Address (text), Criticality (status: Mission Critical, Important, Standard, Low), Owner (people), Last Scanned (date), Vulnerabilities Open (number). Connected to vulnerability management and incident response boards.

#### The Outcome
Achieve 95%+ asset visibility across IT and OT environments (vs. typical 60-70% in manufacturing). Reduce vulnerability assessment scoping time from days to minutes. Enable instant impact analysis when new vulnerabilities are disclosed. Identify and track end-of-life systems requiring compensating controls. Meet IEC 62443 asset inventory requirements (FR1) and CMMC Asset Management controls.

#### Discovery Questions
1. "If I asked you right now how many PLCs from a specific vendor you have across all plants, how quickly could you answer that?"
2. "Where do your OT assets live from a documentation perspective—is that in the same system as IT assets or separate?"
3. "How many end-of-life operating systems are running in your OT environment, and do you have compensating controls documented for each?"
4. "When Claroty or your OT scanner discovers a new asset on the plant network, what's the process to identify and authorize it?"

#### Industry Context
The Purdue Model (ISA-95) defines industrial network architecture in levels: Level 0 (physical process), Level 1 (basic control—sensors, actuators, PLCs), Level 2 (area supervisory—HMIs, SCADA), Level 3 (site operations—historians, MES), Level 3.5 (DMZ), Level 4 (enterprise IT), Level 5 (cloud/internet). Security asset inventory must span all levels. OT assets have much longer lifecycles than IT—PLCs run 15-20 years, and many run obsolete firmware that can't be updated. "Air-gapped" networks are often not truly air-gapped (USB transfers, maintenance laptops, vendor remote access create bridges).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Asset Inventory for an industrial manufacturer covering IT and OT. Create a board called 'Security Asset Inventory' with columns: Asset ID (auto-number with prefix 'AST-'), Asset Name (text), Asset Type (dropdown: Server, Workstation, Laptop, Network Switch, Firewall, PLC, HMI, RTU, SCADA Server, Historian, Engineering Workstation, IoT Sensor/Gateway, Mobile Device, Printer/MFP), Purdue Level (dropdown: L0-Process, L1-Basic Control, L2-Area Supervisory, L3-Site Operations, L3.5-DMZ, L4-Enterprise, L5-Cloud), Plant Location (dropdown: HQ Corporate, Plant 1 - Ohio, Plant 2 - Texas, Plant 3 - Germany, Field/Remote), Manufacturer (text), Model (text), OS/Firmware (text), Version (text), End of Life Date (date), EOL Status (status: Supported in green, Approaching EOL in yellow, End of Life in orange, End of Support in red), Network Segment/VLAN (text), IP Address (text), Business Criticality (status: Mission Critical, Important, Standard, Low), Asset Owner (people), Last Vulnerability Scan (date), Open Vulnerabilities (number), Compensating Controls (long text). Create groups by Purdue Level: Enterprise IT (L4-L5), DMZ (L3.5), Site Operations (L3), Supervisory (L2), Control (L1), Process (L0). Add automations: when End of Life Date is within 90 days change EOL Status to 'Approaching EOL' and notify Asset Owner; when Last Vulnerability Scan is more than 30 days ago for Mission Critical assets, flag for rescan; when Open Vulnerabilities exceeds 5 on any Mission Critical asset, notify security team. Create a Dashboard with: asset count by type (bar chart), assets by Purdue Level (pie chart), EOL status breakdown (pie chart), assets by plant location (bar chart), mission critical assets with open vulnerabilities (table), unscanned assets over 30 days (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Asset Discovery Reconciler
**Agent Purpose:** Continuously reconcile asset inventory with scanner discoveries, identify shadow OT assets, and maintain security-relevant asset attributes.

**Triggers:**
- New asset detected by OT scanner (Claroty, Nozomi) not matching existing inventory
- Weekly reconciliation between IT endpoint management (Intune, SCCM) and asset board
- Manufacturer publishes end-of-life or end-of-support announcement
- Asset vulnerability scan completed (update Open Vulnerabilities count)

**Actions:**
- Match discovered assets to inventory records using MAC address, IP, hostname, and fingerprint
- Create "Unidentified Asset" items for discovered assets not in inventory, flagging for investigation
- Auto-update firmware versions and vulnerability counts from scanner data
- Track EOL/EOS timelines and proactively create compensating control tasks 180 days before support ends
- Generate "shadow IT/OT" reports for assets found on network but not in inventory

**Data Required:**
- OT discovery scanner feeds (Claroty, Nozomi, Dragos)
- IT endpoint management data (SCCM, Intune, Active Directory)
- Manufacturer product lifecycle databases
- Network access control logs

**Autonomy Level:** Fully Autonomous
Asset reconciliation, attribute updates, and EOL tracking run automatically. Unidentified asset alerts require human investigation. Decommission recommendations require asset owner and security team approval.

**Example Interaction:**
> During the weekly reconciliation, the Asset Discovery Reconciler identifies a discrepancy: Claroty detected 4 Schneider Electric Modicon M340 PLCs on the Plant 1 Level 1 network that aren't in the Security Asset Inventory. The agent creates items flagged as "Unidentified - Investigation Required," pre-populating manufacturer, model, firmware version (2.90, which is 3 versions behind current), and network location from scanner data. It cross-references with the plant maintenance system and finds they were installed during a line expansion 8 months ago but never registered with IT Security. The agent also flags that firmware 2.90 has 3 known critical CVEs and recommends immediate vulnerability assessment. It assigns investigation to the OT Security Lead and the Plant 1 maintenance supervisor, noting: "These PLCs appear to be on the packaging line expansion from June 2025. They're running vulnerable firmware and were never security-baselined. Priority: assess network exposure and patch status."

---

### Use Case 7: Security Metrics & Executive Reporting

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The CISO needs to report to the board, the CIO, and increasingly to customers and insurers. But security metrics are scattered across a dozen tools: vulnerability counts from scanners, incident data from the SIEM, phishing stats from KnowBe4, compliance status from GRC spreadsheets, and vendor risk from email threads. Creating a monthly security report takes 15-20 hours of manual data collection and PowerPoint creation. The metrics lack context—"we have 3,247 open vulnerabilities" means nothing without risk-adjusted prioritization and trending. Cyber insurance renewal questionnaires require detailed metrics that take weeks to compile.

#### The Solution
monday.com Dashboards as the security metrics command center, pulling data from all the previously described boards (Vulnerability Management, Incident Response, Compliance, Training, Vendor Risk, Asset Inventory). A master "CISO Dashboard" with executive-level widgets: Overall Security Posture Score (calculated from weighted metrics), Key Risk Indicators (KRIs) with red/amber/green status, 12-month trend charts for MTTR, incident count, phishing click rate, compliance percentage, and vendor risk. Automated monthly report generation from dashboard data. Board for "Security KRI Tracker" with historical metric snapshots for trending.

#### The Outcome
Reduce monthly security report creation from 20 hours to 1 hour. Provide real-time security posture visibility to executive leadership. Support cyber insurance renewal with instant metric retrieval. Enable data-driven security investment decisions. Demonstrate program maturity improvement over time.

#### Discovery Questions
1. "How much time does your team spend each month compiling security metrics for leadership reporting?"
2. "Can you currently show a 12-month trend of your key security metrics, or is that a manual exercise?"
3. "When your cyber insurance provider asks for your incident frequency, MTTR, and patching metrics, how quickly can you provide that?"
4. "Does your board or executive leadership receive regular security posture updates, and in what format?"

#### Industry Context
Manufacturing CISOs increasingly report to the board, driven by SEC cybersecurity disclosure rules (for public companies) and insurance requirements. Key metrics boards care about: incident count and severity trend, ransomware readiness posture, supply chain security coverage, regulatory compliance status, and security investment ROI. Cyber insurance premiums for manufacturers have increased 50-100% since 2022, and insurers now require detailed security metrics for renewal. Demonstrating a mature, measured security program directly reduces premiums.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a CISO Executive Dashboard for an industrial manufacturer. Create a board called 'Security KRI Tracker' with columns: Metric Name (text), Category (dropdown: Vulnerability Management, Incident Response, Compliance, Training & Awareness, Vendor Risk, Asset Management), Current Value (number), Target Value (number), Previous Month (number), Trend (status: Improving in green, Stable in yellow, Declining in red), RAG Status (status: Green-On Target, Amber-Watch, Red-Action Required), Last Updated (date), Notes (long text). Pre-populate with items: Mean Time to Remediate Critical Vulns (days), Open Critical Vulnerabilities, Incident Count (Monthly), Mean Time to Contain (hours), Phishing Click Rate (%), Security Training Completion (%), Vendor Assessment Coverage Tier 1 (%), Compliance Score IEC 62443 (%), Compliance Score CMMC (%), Asset Inventory Coverage (%), EOL Systems Count, Cyber Insurance Readiness Score. Create groups: Vulnerability & Patch, Incident Response, People & Awareness, Compliance & Audit, Third Party Risk, Asset Management. Add automations: when RAG Status changes to Red-Action Required notify CISO; monthly reminder to update all metrics. Create a Dashboard called 'CISO Command Center' with widgets: Overall Security Posture (number widget averaging key scores), KRI summary table (all metrics with RAG), MTTR trend 12 months (line chart), incident count by severity 12 months (stacked bar), phishing click rate trend (line chart), compliance by framework (bar chart), vendor risk tier coverage (pie chart), top 5 risks requiring action (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Security Metrics Curator
**Agent Purpose:** Automatically collect, calculate, and contextualize security metrics from all security boards, generate executive reports, and identify emerging risk trends.

**Triggers:**
- Monthly scheduled metric collection (1st of each month)
- Any KRI crosses from Green to Red threshold
- Board/executive meeting scheduled (triggers pre-meeting brief generation)
- Cyber insurance renewal date approaching (90 days)

**Actions:**
- Pull current values from all security boards (vulnerability counts, incident metrics, training rates, compliance scores, vendor coverage)
- Calculate composite scores and update KRI Tracker board
- Generate narrative executive summary: "Security posture improved 8% this month, driven by MTTR reduction from 32 to 21 days. Key concern: Plant 3 phishing click rate increased to 18%, triggering targeted training."
- Create trend analysis identifying patterns: "Third consecutive month of increasing OT vulnerability count—correlates with 12 new IoT sensors deployed without security baseline"
- Pre-populate cyber insurance renewal questionnaires with current metrics and supporting evidence

**Data Required:**
- All security operational boards (Vulnerability, Incident, Compliance, Training, Vendor, Asset)
- Historical KRI snapshots (minimum 12 months for trending)
- Executive calendar (for pre-meeting brief timing)
- Insurance renewal questionnaire templates

**Autonomy Level:** Fully Autonomous
All data collection, calculation, and internal reporting is automatic. External reports (board presentations, insurance submissions) are generated as drafts requiring CISO review.

**Example Interaction:**
> On March 1st, the Security Metrics Curator runs its monthly collection. It pulls data across all boards: MTTR dropped to 18 days (target: 15, previous: 21—improving), phishing click rate 6.8% (target: 5%, previous 8.2%—improving), IEC 62443 compliance 78% (target: 85%, previous: 75%—improving but behind schedule), Tier 1 vendor assessment coverage 92% (target: 100%, previous: 88%—improving). It flags one Red KRI: EOL systems count increased from 14 to 19 due to 5 Windows Server 2012 R2 systems identified in Plant 2 that weren't previously inventoried. The agent generates the monthly executive brief: "February 2026 Security Posture: Overall score 74/100 (up from 71). Highlights: MTTR at 18 days—best in 6 months. Phishing program showing clear results. Concern: 5 newly discovered EOL systems in Plant 2 require immediate compensating controls or decommission plan. IEC 62443 certification readiness at 78%—on track for Q3 audit but requires accelerated effort on FR5 (Restricted Data Flow) controls, currently at 62%."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| OT (Operational Technology) | Hardware and software that monitors/controls physical equipment and industrial processes |
| ICS (Industrial Control System) | Umbrella term for control systems including SCADA, DCS, and PLCs |
| PLC (Programmable Logic Controller) | Ruggedized computer controlling manufacturing processes (e.g., Siemens S7, Allen-Bradley) |
| HMI (Human-Machine Interface) | Operator interface screen for monitoring/controlling plant equipment |
| SCADA | Supervisory Control and Data Acquisition — centralized monitoring of distributed industrial processes |
| Purdue Model | ISA-95 reference architecture defining industrial network levels (0-5) |
| IEC 62443 | International standard for industrial automation and control system cybersecurity |
| CMMC | Cybersecurity Maturity Model Certification — required for US defense supply chain |
| IT/OT Convergence | The increasing connection between enterprise IT networks and plant-floor OT networks |
| Historian | Database server that records time-series data from industrial processes |
| DMZ (Level 3.5) | Demilitarized zone between IT and OT networks where data exchange is controlled |
| ICS-CERT / CISA | US agency publishing vulnerability advisories for industrial control systems |
| Compensating Controls | Alternative security measures when direct patching/remediation isn't possible |
| Air Gap | Physical network isolation (often claimed, rarely truly implemented) |
| MES (Manufacturing Execution System) | Software managing production operations between ERP and plant floor |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CISO / Director of Infosec | Overall security strategy, risk management, board reporting | Decision-maker |
| IT Security Manager | Corporate network security, endpoint protection, identity management | Decision-maker (IT scope) |
| OT Security Lead | Plant-floor network security, ICS protection, IEC 62443 compliance | Decision-maker (OT scope) |
| CIO / VP of IT | IT strategy, budget, technology stack decisions | Budget authority |
| COO / VP of Operations | Plant performance, uptime, production continuity | Veto power on OT changes |
| Plant Manager | Individual facility operations and safety | Influencer / Gate-keeper for plant access |
| Compliance / GRC Analyst | Framework mapping, audit coordination, evidence management | User / Influencer |
| SOC Analyst | Alert triage, incident detection, investigation | User |
| Network Engineer | IT/OT network architecture, segmentation, firewall management | User / Influencer |
| VP of Engineering | Product security, firmware, connected equipment strategy | Influencer (product security) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Shared infrastructure, identity management, network operations | Unified IT/Security operations board, ITSM integration |
| Operations | Plant uptime dependency, OT change management, maintenance windows | Coordinated OT patching and maintenance scheduling |
| Product & R&D | Product security, secure development lifecycle, connected equipment | Product security vulnerability tracking, SDL workflow |
| Procurement | Vendor onboarding, contract security requirements, supplier management | Vendor risk assessment integrated into procurement workflow |
| Legal | Regulatory compliance, breach notification, contract review | Compliance tracking, incident response legal coordination |
| HR | Employee onboarding/offboarding, access management, security awareness | Identity lifecycle management, training tracking |
| Finance | Cyber insurance, security budget, risk quantification | Risk quantification dashboard, insurance renewal support |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow SecOps | Enterprise security operations + GRC | Expensive, complex, poor OT coverage. monday.com offers faster deployment and better cross-functional collaboration at 1/3 the cost. |
| Archer (RSA) | GRC and compliance management | Legacy, complex, expensive. Compliance teams often build shadow trackers in Excel anyway. monday.com replaces both the shadow tracker and the expensive GRC. |
| Jira (with security plugins) | Developer-oriented vulnerability tracking | Doesn't speak the language of security teams or plant operations. No native dashboard/reporting for executive consumption. |
| Spreadsheets (Excel/Sheets) | "The universal GRC tool" | No automation, no real-time visibility, version control nightmare, audit-unfriendly. monday.com is the upgrade path from spreadsheet-based security management. |
| KnowBe4 / Proofpoint AT | Phishing simulation + training | Siloed — great at phishing but doesn't connect to vulnerability data, incident tracking, or compliance. monday.com provides the operational layer above. |
| Qualys / Tenable | Vulnerability scanning | Scanners find vulnerabilities but don't manage remediation workflows across IT and OT teams. monday.com is the remediation orchestration layer. |
| Claroty / Dragos / Nozomi | OT network monitoring and asset discovery | Excellent OT visibility but no workflow management. monday.com is the action layer where OT security findings become tracked, assigned, remediated work. |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have a SIEM/SOAR for security operations." | "SIEM/SOAR handles detection and automated response. monday.com handles the human workflow layer—vulnerability remediation tracking, compliance management, vendor assessments, executive reporting. These are the workflows your analysts currently manage in spreadsheets alongside the SIEM." |
| "Security tools need to be purpose-built for security." | "Your vulnerability scanner, OT monitor, and SIEM should absolutely be purpose-built. But the workflow layer—tracking remediation, managing compliance evidence, coordinating incident response across departments—doesn't need a $200K GRC tool. It needs a flexible platform your whole team (including non-security staff like plant ops) can actually use." |
| "We can't put security data in a SaaS platform." | "monday.com is SOC 2 Type II certified and supports data residency. You'd track operational workflow data (who's assigned to fix what, when), not raw security telemetry. Your SIEM keeps the logs; monday.com tracks the work. Same principle as using Jira for vulnerability remediation—the scanner has the details, the tracker has the workflow." |
| "Our OT team won't adopt another IT tool." | "That's exactly the problem we solve. OT teams won't log into ServiceNow or Jira. But a visual board where they can see 'these 5 PLCs need firmware updates during the April shutdown' with clear ownership and status? That's how you bridge the IT/OT collaboration gap without forcing OT into IT's tooling." |
| "We're too small for formal security program management." | "You have 3 plants, 200+ networked OT assets, and customers asking for security questionnaires. You're not too small for a security program—you're too small to waste analyst time on spreadsheets. monday.com lets a 5-person security team operate like a 15-person team." |

## Proof Points
*(To be populated with customer references)*
- Manufacturing companies using monday.com for compliance and audit management
- Industrial organizations managing IT/OT security workflows
- Companies that consolidated security tracking from spreadsheets to monday.com
- Defense supply chain manufacturers using monday.com for CMMC compliance tracking

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
