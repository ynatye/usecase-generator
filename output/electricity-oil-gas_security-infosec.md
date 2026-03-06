# Electricity, Oil & Gas × Security & Infosec Playbook

## Overview

Security and Information Security (Infosec) teams in the electricity, oil & gas sector occupy one of the most critical and complex cybersecurity landscapes of any industry. These organizations operate vast networks of Operational Technology (OT) — SCADA systems controlling power grids, DCS (Distributed Control Systems) managing refineries, PLCs on pipeline compressor stations, smart meters across millions of homes, and increasingly, IoT sensors on offshore platforms and wellheads. The convergence of IT and OT networks has created an attack surface that nation-state actors (Russia's Sandworm, China's Volt Typhoon), ransomware gangs (DarkSide/Colonial Pipeline), and hacktivists actively target. A successful cyberattack on energy infrastructure isn't a data breach — it's a potential public safety catastrophe affecting millions.

Regulatory pressure on energy cybersecurity is immense and growing. NERC CIP (North American Electric Reliability Corporation Critical Infrastructure Protection) standards are mandatory for the bulk electric system, with violations carrying fines up to $1M per day. TSA Security Directives (post-Colonial Pipeline) mandate cybersecurity requirements for pipeline operators. The DOE's CESER (Cybersecurity, Energy Security, and Emergency Response) office drives sector-wide initiatives. NRC regulates cybersecurity for nuclear facilities under 10 CFR 73.54. State PUCs increasingly require cybersecurity investment plans as part of rate cases. Internationally, EU's NIS2 Directive and the UK's NIS Regulations add requirements for energy operators in those jurisdictions. Compliance is not optional — it's existential.

Security teams in energy are typically structured with a CISO reporting to the CIO or directly to the CEO/board (increasingly common post-Colonial Pipeline), with separate teams for IT security, OT security, physical security, and compliance/GRC. Team sizes range from 20-50 at mid-size utilities to 200+ at major integrated oil companies, but they're universally understaffed relative to the threat landscape. The average energy company takes 254 days to identify a breach and 79 days to contain it. The challenge is compounded by the legacy nature of OT systems — many SCADA components run decades-old software that cannot be patched without shutting down critical infrastructure, and the Purdue Model segmentation that separates IT from OT networks creates visibility gaps that attackers exploit.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Energy security teams typically run 30-60 different security tools (SIEM, SOAR, EDR, OT monitoring, vulnerability scanners, GRC platforms, PAM, identity management) with minimal integration, creating alert fatigue and blind spots |
| 2 | Scale Impact Without Overhead | High | The cybersecurity talent shortage hits energy especially hard — OT security expertise is extremely scarce, and teams must cover 24/7 operations across geographically dispersed infrastructure |
| 3 | Replace or Radically Augment Headcount | Medium-High | AI agents can handle Tier 1 SOC alert triage, compliance evidence gathering, vulnerability tracking, and incident documentation that consume 60-70% of analyst time |

## Prioritized Use Cases

---

### Use Case 1: Unified Security Operations & Incident Management Hub

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy SOC (Security Operations Center) teams manage alerts from dozens of sources: SIEM platforms (Splunk, Sentinel, QRadar) for IT networks, OT monitoring tools (Claroty, Nozomi Networks, Dragos) for SCADA/DCS environments, EDR (CrowdStrike, SentinelOne) on endpoints, cloud security (Prisma, Wiz) for cloud workloads, email security gateways, firewall logs, PAM (Privileged Access Management) alerts, and physical security systems. The average energy SOC receives 10,000–50,000 alerts per day with a false positive rate of 80-95%. Incident response is managed through a patchwork of ticketing systems (ServiceNow, Jira), email chains, and war room calls. When a real incident occurs — like the Colonial Pipeline ransomware attack that shut down 5,500 miles of pipeline — the lack of a unified incident management workflow costs hours of response time. Post-incident, assembling a complete timeline for regulators (NERC, TSA, CISA) is a manual, weeks-long effort.

#### The Solution
monday.com Work Management configured as a Security Incident Management Hub. **Active Incidents** board: Incident ID (auto-number), Incident Name (text), Severity (dropdown: P1 - Critical/Active Attack, P2 - High/Confirmed Compromise, P3 - Medium/Suspicious Activity, P4 - Low/Policy Violation), Category (dropdown: Ransomware, APT/Nation-State, Insider Threat, Phishing Campaign, OT Compromise, DDoS, Data Exfiltration, Supply Chain, Unauthorized Access, Physical Security), Affected Systems (tags: IT Network, OT/SCADA, Cloud, Email, Endpoints, Physical, Third-Party), Affected Facilities (dropdown multi: [list facilities]), Status (status: Detected, Triaging, Containing, Eradicating, Recovering, Post-Incident Review, Closed), Incident Commander (people), IT Lead (people), OT Lead (people), Regulatory Notification Required (checkbox), Regulatory Deadline (date), MITRE ATT&CK Tactics (tags), Timeline (timeline). **Incident Tasks** as subitems: containment actions, forensic collection, communications, recovery steps — each with assignee, status, and timestamps. **Threat Intelligence** board tracking active threat actors targeting the energy sector. **Vulnerability Management** board with risk-prioritized tracking. Dashboards providing real-time SOC status, incident trends, and compliance metrics.

#### The Outcome
50% reduction in mean time to respond (MTTR) through standardized incident workflows. Complete audit trail for every incident from detection to closure — critical for NERC CIP and TSA compliance. Unified visibility across IT and OT security incidents. Automated regulatory notification tracking ensuring zero missed deadlines. Post-incident reviews become structured data that improves response over time.

#### Discovery Questions
1. "When Colonial Pipeline happened, your board probably asked 'could that happen to us?' — what's changed in your incident management process since then?"
2. "How many different tools does your SOC team alt-tab between during an active incident? And how much of the post-incident timeline reconstruction is manual?"
3. "If NERC or TSA auditors asked you right now to show the complete incident response timeline for your last significant security event, how long would it take to produce?"
4. "Do your IT security and OT security teams use the same incident management system, or do they run parallel processes? How do they coordinate when an incident spans both?"
5. "What percentage of your SOC analysts' time is spent on actual threat hunting vs. administrative tasks like updating tickets, writing reports, and chasing down context?"

#### Industry Context
The Colonial Pipeline ransomware attack (May 2021) was a watershed moment for energy cybersecurity. DarkSide ransomware led to a 6-day shutdown of the largest US fuel pipeline, causing fuel shortages across the Southeast. This triggered TSA Security Directives mandating cybersecurity requirements for pipeline operators. NERC CIP has 13 standards (CIP-002 through CIP-014) covering everything from BES (Bulk Electric System) cyber system identification to physical security. CIP-008 specifically governs incident reporting and response planning. CISA (Cybersecurity and Infrastructure Security Agency) mandates reporting of significant cyber incidents within 72 hours under CIRCIA. The MITRE ATT&CK for ICS framework is the standard taxonomy for OT-specific attack techniques. SEs should understand the difference between IT incidents (data breach, phishing) and OT incidents (unauthorized SCADA access, PLC manipulation) — OT incidents can cause physical damage and endanger lives.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Incident Management Hub for an energy company. Create a board called 'Security Incidents' with columns: Incident ID (auto-number), Incident Title (text), Severity (dropdown: P1 - Critical Active Attack, P2 - High Confirmed Compromise, P3 - Medium Suspicious Activity, P4 - Low Policy Violation), Category (dropdown: Ransomware, APT/Nation-State, Insider Threat, Phishing, OT/SCADA Compromise, DDoS, Data Exfiltration, Supply Chain Attack, Unauthorized Access, Physical Breach), Attack Vector (dropdown: Email/Phishing, Exploit - Public Facing, Exploit - Internal, Credential Theft, Supply Chain, Removable Media, Wireless, Physical, Unknown), Domain (dropdown: IT Only, OT Only, IT-OT Crossover, Cloud, Physical), Affected Facilities (tags), Status (status: Detected, Triaging, Containing, Eradicating, Recovering, Post-Incident Review, Closed), Incident Commander (people), IT Security Lead (people), OT Security Lead (people), MITRE ATT&CK Tactics (tags: Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command & Control, Exfiltration, Impact), Detection Source (dropdown: SIEM, OT Monitor, EDR, Firewall, User Report, Threat Intel, Physical Security, Third Party), Regulatory Notification Required (status: Not Required, Required - NERC, Required - TSA, Required - CISA, Required - State, Required - Multiple), Regulatory Deadline (date), Regulatory Submission Status (status: N/A, Pending, Drafted, Submitted, Acknowledged), Timeline (timeline), Estimated Business Impact (dropdown: None, Minor, Significant, Major, Catastrophic). Add subitems for incident tasks: Task Name, Task Type (dropdown: Containment, Evidence Collection, Forensics, Communication, Recovery, Documentation), Assignee (people), Priority, Status, Due Date, Completion Timestamp. Create automations: when Severity is P1, notify CISO, VP Operations, and Legal immediately and set SLA timer to 15 minutes for first response; when Regulatory Notification Required changes from Not Required, auto-calculate deadline based on regulation and create deadline reminder at 48h/24h/4h before; when Status changes to Post-Incident Review, create a linked Post-Incident Review board item with auto-populated incident details; when all subitems are complete and Status is Recovering, prompt Incident Commander to move to Post-Incident Review. Create a Dashboard with: Active Incidents by Severity (chart), Incidents by Category This Quarter (bar chart), Mean Time to Detect/Respond/Recover (number widgets), Incidents by Domain IT vs OT (pie chart), Pending Regulatory Notifications (filtered table), Open Incident Tasks by Assignee (table), Incident Trend 12-Month (line chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SOC Incident Orchestrator

**Agent Purpose:** Automatically triage incoming security alerts, create and populate incident records, assign response teams based on incident type and affected domain, track response SLAs, and ensure regulatory notification deadlines are met.

**Triggers:**
- New item created in Security Incidents board (manual or API from SIEM/SOAR)
- Severity escalated from P3/P4 to P1/P2
- Regulatory Deadline within 48/24/4 hours with Submission Status still Pending
- Status unchanged for longer than SLA threshold (P1: 15 min, P2: 1 hour, P3: 4 hours)
- Multiple P3+ incidents detected from same attack vector within 1 hour (possible coordinated attack)

**Actions:**
- Auto-populate incident record with enrichment data from threat intelligence feeds (known IOCs, threat actor profiles, MITRE ATT&CK mapping)
- Assign incident response team based on Domain (IT vs OT vs crossover) and Category, pulling from on-call rotation schedule
- Generate incident containment checklist based on Category and Attack Vector (e.g., ransomware playbook, OT compromise playbook)
- Create regulatory notification draft pre-populated with incident details, timeline, and required fields for the specific regulation (NERC CIP-008, TSA SD, CISA CIRCIA)
- Escalate to CISO and executive leadership when SLA thresholds are breached
- Compile post-incident timeline from all subitem timestamps for regulatory submission and lessons learned

**Data Required:**
- SIEM/SOAR integration for alert ingestion
- Threat intelligence feeds (CISA KEV, ICS-CERT, sector-specific ISACs)
- On-call rotation schedules for IT and OT security teams
- Regulatory notification templates and deadline rules
- Asset inventory (IT and OT) for impact assessment
- MITRE ATT&CK for Enterprise and ICS frameworks

**Autonomy Level:** Human-in-the-Loop
Alert triage, enrichment, and team assignment are automated. Containment actions require human approval (especially for OT systems where incorrect actions can cause physical damage). Regulatory notifications are drafted automatically but require CISO sign-off. Escalations are fully autonomous.

**Example Interaction:**
> At 2:23 AM, the SOC Incident Orchestrator receives an alert from the Dragos OT monitoring platform: anomalous communication detected between a Human-Machine Interface (HMI) workstation at the Baytown refinery and an external IP address not on the approved communication list. The agent creates a P2 incident — "Suspicious OT Network Communication — Baytown HMI" — auto-classified as Category: OT/SCADA Compromise, Domain: OT Only, Attack Vector: Unknown, Detection Source: OT Monitor. It maps the behavior to MITRE ATT&CK for ICS: T0869 (Standard Application Layer Protocol) and T0884 (Connection Proxy). The agent pulls the Baytown facility OT network diagram from the asset inventory, identifies the HMI as Level 2 in the Purdue Model controlling a catalytic cracking unit, and assesses Estimated Business Impact as Major. It assigns the on-call OT Security Lead (Sarah Chen) and the Baytown Plant Security Manager, creates containment subitems (isolate HMI from network, capture memory image, block external IP at firewall, review DMZ logs), and notifies the CISO. It also flags that TSA Security Directive SD-02D requires reporting of this type of anomaly within 24 hours and begins drafting the CISA notification form. Sarah Chen receives a complete briefing packet on her phone within 4 minutes of the initial alert.

---

### Use Case 2: NERC CIP Compliance Management & Evidence Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
NERC CIP compliance is the single largest regulatory burden for electric utilities and grid operators. The 13 CIP standards contain over 100 specific requirements, each requiring documented evidence of compliance. Utilities must maintain a complete inventory of BES (Bulk Electric System) Cyber Systems, demonstrate access controls, prove patching cadence, document personnel training, maintain physical security evidence, and show incident response capabilities — all subject to audit by NERC Regional Entities (RF, SERC, WECC, etc.) with fines up to $1M per violation per day. A single compliance gap can result in a "Possible Violation" finding that takes 2-3 years and millions in legal fees to resolve. Most utilities manage CIP compliance through a combination of GRC platforms (RSA Archer, ServiceNow GRC), spreadsheets, shared drives full of evidence screenshots, and the institutional knowledge of a compliance team of 5-15 people who live in perpetual audit preparation mode. When a key compliance analyst leaves, institutional knowledge walks out the door.

#### The Solution
monday.com Work Management as a CIP Compliance Evidence & Workflow Hub. **CIP Requirements Matrix** board: Standard (dropdown: CIP-002 through CIP-014), Requirement Number, Requirement Text (long text), Applicability (dropdown: High BES, Medium BES, Low BES, EACMS, PACS, PCA), Evidence Type Required (dropdown: Policy Document, System Screenshot, Log Extract, Training Record, Physical Security Record, Test Report, Configuration Baseline), Evidence Owner (people), Evidence Refresh Frequency (dropdown: Annual, Quarterly, Monthly, Per Change, Continuous), Last Evidence Collected (date), Next Evidence Due (date), Evidence Status (status: Current, Due Soon, Overdue, Gap Identified, Remediation In Progress), Evidence Files (files), Auditor Notes (long text). **Audit Preparation** board tracking readiness for upcoming NERC audits with progress by standard. **Change Management** board specifically for CIP-010 configuration change management with baseline tracking. **Training Compliance** board for CIP-004 personnel risk assessments and training records. **Access Management** board for CIP-004/CIP-005 electronic and physical access reviews. Dashboards showing compliance posture at a glance — green/yellow/red by standard with drill-down capability.

#### The Outcome
100% evidence currency — zero overdue compliance evidence items through automated reminders and workflow. 70% reduction in audit preparation time through centralized, organized evidence management. Elimination of "evidence scavenger hunts" before audits. Real-time compliance posture visibility for CISO and board reporting. Institutional knowledge captured in workflows rather than individuals' heads.

#### Discovery Questions
1. "How many FTEs do you have dedicated to CIP compliance, and what percentage of their time is spent collecting and organizing evidence vs. actually improving security?"
2. "When your NERC Regional Entity announces an audit, what's the scramble like? Is your evidence already organized, or does your team go into emergency collection mode?"
3. "How do you handle CIP-010 configuration baseline management today? When someone makes a change to a BES Cyber System, how does that change flow through your compliance documentation?"
4. "If your lead CIP compliance analyst left tomorrow, how much institutional knowledge would walk out the door? Could someone new pick up where they left off?"
5. "Have you ever received a Possible Violation or Area of Concern from a NERC audit? What was the root cause — an actual security gap, or a documentation/evidence gap?"

#### Industry Context
NERC CIP applies to all owners, users, and operators of the Bulk Electric System (BES). The standards are enforced by Regional Entities (ReliabilityFirst, SERC, WECC, MRO, Texas RE, etc.) through periodic audits, spot checks, and self-certifications. CIP-002 requires categorization of BES Cyber Systems as High, Medium, or Low impact. CIP-003-CIP-011 establish specific security controls. CIP-012 protects communication links. CIP-013 addresses supply chain risk management. CIP-014 covers physical security for critical substations. The compliance evidence burden is enormous — utilities maintain tens of thousands of evidence artifacts. The SE should understand that CIP compliance is not just a security concern — it's a business risk that directly affects rate cases (PUCs approve cybersecurity investment recovery) and executive accountability (NERC can fine individuals, not just organizations).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a NERC CIP Compliance Management workspace for an electric utility. Create a board called 'CIP Requirements Tracker' with columns: CIP Standard (dropdown: CIP-002, CIP-003, CIP-004, CIP-005, CIP-006, CIP-007, CIP-008, CIP-009, CIP-010, CIP-011, CIP-012, CIP-013, CIP-014), Requirement ID (text, e.g. CIP-007-R2.1), Requirement Description (long text), Impact Level Applicability (tags: High BES, Medium BES, Low BES, EACMS, PACS, PCA), Control Category (dropdown: Access Control, Configuration Management, Incident Response, Personnel & Training, Physical Security, System Security, Recovery Planning, Vulnerability Management, Supply Chain, Information Protection), Evidence Type (dropdown: Policy Document, Procedure Document, System Configuration, Log Extract, Screenshot, Training Certificate, Test Report, Audit Trail, Physical Security Record, Vendor Attestation), Evidence Owner (people), Backup Owner (people), Collection Frequency (dropdown: Continuous, Monthly, Quarterly, Semi-Annual, Annual, Per Change Event), Last Collected Date (date), Next Due Date (date), Compliance Status (status: Compliant - Green, Due Within 30 Days - Yellow, Overdue - Red, Gap Identified - Purple, Remediation Active - Blue, Not Applicable - Gray), Evidence Location (link), Evidence Files (files), Auditor Notes from Last Audit (long text), Remediation Plan (long text). Create a connected board called 'CIP Audit Tracker' with columns: Audit Name (text), Audit Type (dropdown: On-Site Audit, Off-Site Audit, Spot Check, Self-Certification, Self-Report), Regional Entity (dropdown: ReliabilityFirst, SERC, WECC, MRO, SPP RE, Texas RE, NPCC), Audit Dates (timeline), Standards In Scope (tags), Preparation Status (status: Not Started, Gathering Evidence, Review In Progress, Ready for Audit, Audit Active, Findings Response, Closed), Lead Auditor (people), Connected Requirements (connect to CIP Requirements Tracker), Findings Count (numbers), Possible Violations (numbers). Add automations: when Next Due Date is within 30 days and Compliance Status is Compliant, change to Due Within 30 Days and notify Evidence Owner; when Next Due Date is past and evidence not updated, change to Overdue and escalate to CISO; when Compliance Status changes to Gap Identified, auto-create a remediation task and assign to Evidence Owner with 30-day deadline; when new Audit Tracker item is created, auto-populate Connected Requirements based on Standards In Scope. Create a Dashboard with: Overall Compliance Posture (battery widget by standard), Overdue Evidence Items (filtered table), Compliance Status Distribution (pie chart), Upcoming Due Dates Next 60 Days (calendar), Evidence Collection Trend (line chart showing % current over time), Open Gaps and Remediations (table), Compliance by Impact Level (stacked bar chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CIP Compliance Guardian

**Agent Purpose:** Continuously monitor CIP compliance evidence currency, automate evidence collection workflows, prepare audit readiness reports, and ensure zero compliance gaps across all NERC CIP standards.

**Triggers:**
- Evidence Next Due Date within 30/14/7 days
- Compliance Status changes to Overdue or Gap Identified
- New CIP Audit Tracker item created (audit announced)
- CIP standard revision published by NERC (annual check)
- Change Management board item created (CIP-010 baseline change triggers evidence update)
- Quarterly compliance posture report schedule

**Actions:**
- Generate evidence collection reminders with specific instructions for what evidence is needed, in what format, and where to upload
- Pre-populate evidence collection tasks with templates based on Evidence Type and CIP standard
- Cross-reference Change Management entries against CIP-010 baseline requirements to ensure all changes are documented
- Generate audit readiness report showing compliance posture by standard, identifying gaps, and estimating remediation effort
- Compile evidence packages for specific audit requests, organizing by standard and requirement
- Alert when a CIP standard revision changes requirements, mapping new requirements to existing controls and identifying gaps
- Generate board-level compliance summary reports with trend analysis

**Data Required:**
- CIP Requirements Tracker with all evidence metadata
- Change Management board for CIP-010 baseline tracking
- Training records system integration for CIP-004 evidence
- Access management system integration for CIP-004/CIP-005 evidence
- NERC standards library and revision tracking
- Historical audit findings and remediation records

**Autonomy Level:** Escalation-Based
Evidence reminders, due date tracking, and report generation are fully autonomous. Gap identification and remediation recommendations require compliance team review. Audit response packages require compliance manager and legal review. No evidence is submitted to auditors without explicit human approval.

**Example Interaction:**
> The CIP Compliance Guardian agent detects that SERC has announced a comprehensive on-site audit for Q3 2026, covering CIP-002 through CIP-011. It immediately creates an Audit Tracker item and cross-references all in-scope requirements against current compliance status. The analysis reveals: 87 of 94 applicable requirements show "Compliant" status with current evidence. However, 4 CIP-007-R2 (security patch management) items show evidence last collected 45 days ago — the agent notes that the quarterly patch cycle evidence from 3 BES Cyber Systems at the Riverside generating station is overdue because the OT team delayed a maintenance window. It also identifies 2 CIP-004-R3 (personnel risk assessment) items where employee background checks are due for renewal within 60 days, and 1 CIP-010-R1 baseline configuration documentation that hasn't been updated since a firmware upgrade last month. The agent generates a prioritized remediation plan: "Critical: Collect CIP-007-R2 patch evidence from Riverside (assign to OT Security Lead, 7-day deadline). High: Update CIP-010-R1 baseline documentation for firmware change (assign to Configuration Manager, 14-day deadline). Medium: Schedule CIP-004-R3 background check renewals (assign to HR Security Liaison, 45-day deadline)." It sends the remediation plan to the CIP Compliance Manager and schedules weekly readiness check-ins until the audit date.

---

### Use Case 3: OT/ICS Asset Inventory & Vulnerability Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
You can't protect what you don't know you have. Energy companies operate thousands of OT/ICS (Industrial Control Systems) assets: SCADA servers, RTUs (Remote Terminal Units), PLCs (Programmable Logic Controllers), HMIs (Human-Machine Interfaces), engineering workstations, historians, data diodes, and safety instrumented systems (SIS). Many of these assets were deployed decades ago, run unsupported operating systems (Windows XP Embedded is still common in substations), and have never been inventoried with the rigor applied to IT assets. NERC CIP-002 requires identification and categorization of BES Cyber Systems, but maintaining an accurate, real-time inventory across hundreds of substations, generating stations, and control centers is a massive challenge. Vulnerability management is even harder: OT systems often can't be patched on the same cadence as IT systems because patching requires operational outages. CVEs affecting Siemens, Schneider Electric, ABB, GE, Honeywell, and Emerson equipment accumulate while security teams struggle to prioritize which vulnerabilities represent real risk in their specific OT environment.

#### The Solution
monday.com Work Management as an OT Asset & Vulnerability Management Hub. **OT Asset Registry** board: Asset Name (text), Asset Type (dropdown: SCADA Server, RTU, PLC, HMI, Engineering Workstation, Historian, Data Diode, SIS, Network Switch, Firewall, Other), Vendor (dropdown: Siemens, Schneider Electric, ABB, GE, Honeywell, Emerson, Rockwell, Yokogawa, Other), Model (text), Firmware/OS Version (text), Location/Facility (dropdown), Network Zone (dropdown per Purdue Model: Level 0 - Process, Level 1 - Basic Control, Level 2 - Area Supervisory, Level 3 - Site Operations, Level 3.5 - DMZ, Level 4 - Enterprise), BES Cyber System Category (dropdown: High, Medium, Low, Not BES), Last Patched (date), Patch Status (status: Current, Patch Available, Patch Deferred — Operational, Patch Deferred — Vendor Approval, End of Life, Compensating Controls), Known Vulnerabilities (numbers), Risk Score (numbers), Owner (people). **Vulnerability Tracker** board: CVE ID (text), CVSS Score (numbers), Affected Vendor/Product (connect to Asset Registry), Affected Asset Count (numbers from connection), Exploitability (dropdown: Actively Exploited, POC Available, Theoretical, Not Exploitable in Environment), ICS-CERT Advisory (link), Remediation (dropdown: Patch, Compensating Control, Accept Risk, Mitigate), Remediation Status (status), Remediation Owner (people), Due Date. **Patch Campaign** board tracking planned maintenance windows for OT patching with operational coordination. Dashboards showing fleet vulnerability posture, aging assets, and patch compliance metrics.

#### The Outcome
Complete OT asset visibility across all facilities — the foundation for all other security activities. Risk-prioritized vulnerability management based on actual exploitability in the energy OT context, not just CVSS scores. 40% improvement in patch compliance through coordinated patch campaign management. Regulatory compliance evidence for NERC CIP-007 (system security management) and CIP-010 (configuration change management). Data-driven business case for OT modernization investments.

#### Discovery Questions
1. "If I asked you right now how many PLCs are running firmware older than 5 years across all your facilities, could you tell me? How about which ones have known CVEs?"
2. "When ICS-CERT publishes an advisory for a Siemens vulnerability that affects equipment in your substations, what's your process for determining which assets are affected and prioritizing remediation?"
3. "How do you coordinate OT patching with Operations? I've heard from other utilities that the biggest challenge isn't the patch itself — it's getting the maintenance window."
4. "What's your strategy for assets running Windows XP or other end-of-life operating systems that can't be upgraded without replacing the entire control system?"
5. "For your NERC CIP-002 BES Cyber System categorization — how confident are you that your inventory is complete and current? When was the last time it was validated?"

#### Industry Context
ICS-CERT (now CISA ICS) publishes advisories for vulnerabilities in industrial control systems. Major OT vendors include Siemens, Schneider Electric, ABB, GE Vernova, Honeywell, Emerson, Rockwell Automation, and Yokogawa. The Purdue Model (ISA-95) defines network segmentation levels from Level 0 (physical process) through Level 5 (enterprise). OT patching is fundamentally different from IT patching: it requires operational coordination, vendor-approved patches (you can't just apply a Microsoft patch to a Siemens HMI without vendor certification), and often physical presence at the facility. "Compensating controls" — network segmentation, monitoring, access controls — are commonly used when patching isn't feasible. Safety Instrumented Systems (SIS) like Triconex are the last line of defense against physical catastrophe and have their own security considerations (see Triton/Trisis malware). SEs should understand that "just patch it" is not a valid answer in OT environments.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an OT Asset & Vulnerability Management workspace for an energy company. Create a board called 'OT Asset Registry' with columns: Asset Name (text), Asset ID (text), Asset Type (dropdown: SCADA Server, RTU, PLC, HMI, Engineering Workstation, Historian, Data Diode, Safety Instrumented System, OT Network Switch, OT Firewall, DCS Controller, Relay/IED, Other), Vendor (dropdown: Siemens, Schneider Electric, ABB, GE Vernova, Honeywell, Emerson, Rockwell Automation, Yokogawa, SEL, Other), Model Number (text), Firmware Version (text), OS Version (text), Install Date (date), Facility (dropdown: [list facilities]), Purdue Level (dropdown: L0 - Process, L1 - Basic Control, L2 - Area Supervisory, L3 - Site Operations, L3.5 - DMZ), BES Category (dropdown: High Impact BES, Medium Impact BES, Low Impact BES, Not BES Applicable), Network Segment (text), IP Address (text), Patch Status (status: Current - Green, Patch Available - Yellow, Patch Deferred - Orange, End of Life - Red, Compensating Controls - Blue), Last Patched Date (date), Known CVE Count (numbers), Risk Score (numbers 1-100), Asset Owner (people), Maintenance Window (dropdown: Q1, Q2, Q3, Q4, Emergency Only, Cannot Patch), Notes (long text). Create a connected board called 'Vulnerability Tracker' with columns: CVE ID (text), CVSS Base Score (numbers), CVSS Severity (dropdown: Critical 9.0-10.0, High 7.0-8.9, Medium 4.0-6.9, Low 0.1-3.9), Affected Vendor (dropdown: same as Asset Registry), Affected Product (text), Affected Assets (connect to OT Asset Registry), Affected Asset Count (mirror count), Exploitability (dropdown: Known Active Exploitation - CISA KEV, Proof of Concept Public, Theoretical, Not Exploitable in OT Context), ICS-CERT Advisory Link (link), Discovery Date (date), Remediation Strategy (dropdown: Vendor Patch, Firmware Upgrade, Compensating Control, Network Segmentation, Accept Risk, Decommission Asset), Remediation Status (status: Open, Planned, In Progress, Verified, Risk Accepted, Deferred), Remediation Owner (people), Target Date (date), Actual Completion Date (date). Add automations: when new CVE item created with Exploitability as Known Active Exploitation, set priority to urgent and notify CISO and OT Security Lead immediately; when Affected Assets connection is made, auto-calculate Affected Asset Count and if >10, escalate; when Target Date is past and Remediation Status is not Verified or Risk Accepted, escalate to CISO; when OT Asset Registry Patch Status changes to End of Life, create a linked remediation planning item. Create a Dashboard with: Assets by Type (pie chart), Assets by Patch Status (bar chart), Vulnerability Severity Distribution (chart), Open CVEs by Exploitability (stacked bar), End of Life Assets by Facility (table), Top 10 Highest Risk Assets (table sorted by Risk Score), Patch Compliance Trend (line chart), CVE Aging (chart showing days open)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OT Vulnerability Sentinel

**Agent Purpose:** Continuously monitor ICS-CERT advisories and vendor security bulletins, match vulnerabilities to the company's OT asset inventory, calculate contextual risk scores, and orchestrate remediation campaigns coordinated with Operations.

**Triggers:**
- New ICS-CERT/CISA advisory published (daily API check)
- New CVE published affecting known OT vendors in the asset registry
- CISA KEV (Known Exploited Vulnerabilities) catalog updated with ICS-relevant entry
- Quarterly vulnerability review cycle
- OT Asset Registry item updated (new asset added or firmware version changed)

**Actions:**
- Parse ICS-CERT advisory and match affected vendor/product/version against OT Asset Registry to identify exposed assets
- Create Vulnerability Tracker items with auto-populated CVE details, CVSS scores, and connected affected assets
- Calculate contextual risk score (CVSS base × asset criticality × Purdue Level × BES Category × exploitability) to prioritize remediation
- Recommend remediation strategy based on asset type and operational constraints (patch if maintenance window available, compensating control if not)
- Create Patch Campaign items grouping vulnerabilities by facility and maintenance window for coordinated remediation
- Generate monthly vulnerability posture report for CISO and board with trend analysis and risk reduction metrics
- Cross-reference new assets added to the registry against existing open CVEs to identify immediate exposure

**Data Required:**
- ICS-CERT/CISA advisory feed API
- NVD (National Vulnerability Database) API for CVE details
- CISA KEV catalog
- OT vendor security bulletin feeds (Siemens ProductCERT, Schneider PSIRT, etc.)
- OT Asset Registry with complete version information
- Operations maintenance window calendar
- Purdue Model network architecture documentation

**Autonomy Level:** Escalation-Based
Advisory monitoring, asset matching, and risk scoring are fully autonomous. Remediation recommendations require OT Security team review. Patch campaigns require Operations coordination and approval. Risk acceptance decisions require CISO sign-off.

**Example Interaction:**
> The OT Vulnerability Sentinel agent detects a new CISA advisory: ICSA-26-050-01 — a critical vulnerability (CVSS 9.8) in Schneider Electric Modicon M340 PLCs allowing remote code execution via crafted Modbus packets. The agent queries the OT Asset Registry and identifies 47 Modicon M340 PLCs across 12 facilities — 8 in substations categorized as Medium BES Cyber Systems and 3 in a generating station categorized as High BES. It checks CISA KEV: not yet listed, but proof-of-concept exploit code was published on GitHub 48 hours ago. Contextual risk score: 94/100 for the High BES generating station PLCs (critical asset × Purdue Level 1 × High BES × POC available). The agent creates a Vulnerability Tracker item, connects all 47 affected assets, and generates a tiered remediation plan: "Immediate (72 hours): Apply network segmentation rule to block external Modbus access to all 47 PLCs — this is a compensating control that doesn't require an outage. Priority (30 days): Schedule firmware update for the 3 High BES PLCs during the next generating station maintenance window (March 15). Standard (90 days): Roll firmware update across remaining 44 PLCs during quarterly substation maintenance cycles." The agent sends this to the OT Security Lead and the Operations scheduling team simultaneously, and flags it for discussion at the weekly vulnerability review meeting.

---

### Use Case 4: Third-Party & Supply Chain Risk Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The SolarWinds attack (2020) and Log4j vulnerability (2021) demonstrated that supply chain attacks can compromise even well-defended organizations. For energy companies, the supply chain risk is amplified: they depend on OT vendors (Siemens, Schneider, GE, Honeywell) for critical infrastructure components, managed service providers for IT operations, cloud providers for enterprise workloads, and hundreds of contractors with VPN or physical access to facilities. NERC CIP-013 specifically requires supply chain risk management plans for BES Cyber Systems. TSA Security Directives require pipeline operators to identify and report supply chain risks. Most energy companies manage vendor security assessments through annual questionnaires sent via email, tracked in spreadsheets, with no continuous monitoring of vendor risk posture between assessments. When a critical vendor is compromised (as happened with the Kaseya VSA attack), energy companies often learn about their exposure from the news rather than from their risk management program.

#### The Solution
monday.com Work Management as a Supply Chain Risk Management platform. **Vendor Risk Registry** board: Vendor Name (text), Vendor Type (dropdown: OT/ICS Vendor, IT Service Provider, Cloud Provider, Physical Security Vendor, Consulting/Professional Services, Contractor - Facility Access, Software Vendor, Telecom Provider), Criticality (dropdown: Critical - Single Point of Failure, High - Difficult to Replace, Medium - Alternatives Available, Low - Easily Replaceable), Access Level (dropdown: OT Network Access, IT Network Access, Physical Facility Access, Data Access Only, No Direct Access), BES Cyber System Connection (checkbox), CIP-013 In Scope (checkbox), Last Assessment Date (date), Next Assessment Due (date), Risk Rating (status: Low - Green, Medium - Yellow, High - Orange, Critical - Red), Assessment Status (status: Current, Assessment Due, Assessment In Progress, Remediation Required, Suspended, Terminated), Contract Expiry (date), Primary Contact (text), Security Contact (text), Risk Owner (people). **Assessment Workflow** board: tracking security questionnaire distribution, completion, review, and findings. **Vendor Incidents** board: tracking security events at vendor organizations that may affect the energy company. **CIP-013 Compliance** board: specifically tracking supply chain risk management plan requirements, vendor notification obligations, and software integrity verification. Dashboards showing vendor risk landscape, assessment pipeline, and CIP-013 compliance status.

#### The Outcome
Continuous visibility into third-party risk posture across all vendor categories. 60% reduction in assessment cycle time through automated workflow and questionnaire management. CIP-013 compliance evidence maintained automatically. Early warning capability when critical vendors experience security incidents. Data-driven vendor risk ratings that inform procurement decisions and contract renewals.

#### Discovery Questions
1. "How many vendors have direct access to your OT network or BES Cyber Systems? Can you list them right now, or would someone need to go check?"
2. "When the SolarWinds or Log4j incidents happened, how quickly could you determine which of your vendors were affected and what your exposure was?"
3. "For NERC CIP-013, how do you verify the integrity of software and patches from your OT vendors before deploying them in your BES environment?"
4. "How often do you reassess vendor security posture? Is it annual, or do you have continuous monitoring? What happens between assessments?"
5. "If one of your critical OT vendors — say, your SCADA platform provider — experienced a significant breach, would you find out from them first, or from the news?"

#### Industry Context
NERC CIP-013 (Supply Chain Risk Management) requires entities to develop and implement plans addressing: software integrity and authenticity verification, vendor remote access controls, information system planning (including transition from one vendor to another), and vendor risk assessment. The standard was developed in response to growing supply chain threats to the bulk power system. The SolarWinds Orion compromise (2020) affected energy companies that used the IT management platform. The Triton/Trisis malware (2017) specifically targeted Schneider Electric Triconex safety systems in a petrochemical facility. CISA's Software Bill of Materials (SBOM) initiative aims to improve software supply chain transparency. TSA Security Directives require pipeline operators to implement supply chain risk management. SEs should understand that OT supply chain risk is different from IT — there are far fewer vendors, switching costs are enormous, and the relationship between an energy company and its OT vendors is deeply embedded.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Third-Party Risk Management workspace for an energy company security team. Create a board called 'Vendor Risk Registry' with columns: Vendor Name (text), Vendor Type (dropdown: OT/ICS Vendor, Managed IT Services, Cloud/SaaS Provider, Physical Security Vendor, Consulting/Professional Services, Facility Contractor, Software Vendor, Telecom/Network Provider, Fuel/Commodity Supplier), Criticality (dropdown: Critical, High, Medium, Low), Access Type (tags: OT Network, IT Network, Physical Facility, Sensitive Data, Cloud Environment, VPN/Remote, Badge/Physical Only, No Direct Access), BES Cyber System Touchpoint (status: Yes - Direct, Yes - Indirect, No), CIP-013 In Scope (checkbox), Contract Value (numbers with $), Contract Expiry (date), Last Security Assessment (date), Next Assessment Due (date), Overall Risk Rating (status: Low - Green, Moderate - Yellow, High - Orange, Critical - Red, Not Assessed - Gray), Assessment Status (status: Current, Due, In Progress, Overdue, Findings Open, Suspended), Key Findings Count (numbers), Open Remediation Items (numbers), Risk Owner (people), Vendor Security Contact (text), SLA for Incident Notification (dropdown: 24 Hours, 48 Hours, 72 Hours, No SLA, Unknown). Create a connected board called 'Vendor Assessments' with columns: Assessment Name (text), Vendor (connect to Vendor Risk Registry), Assessment Type (dropdown: Initial Onboarding, Annual Review, Triggered Reassessment, CIP-013 Specific, Incident Response), Questionnaire Sent Date (date), Questionnaire Due Date (date), Questionnaire Status (status: Not Sent, Sent, In Progress, Received, Under Review, Complete), Reviewer (people), Findings (subitems with: Finding Description, Severity, Remediation Required, Remediation Deadline, Vendor Response, Status), Overall Assessment Result (dropdown: Approved, Approved with Conditions, Conditional - Remediation Required, Rejected, Suspended). Add automations: when Next Assessment Due is within 30 days, create new Assessment item and notify Risk Owner; when Questionnaire Due Date is past and Status is not Received, send reminder to vendor contact and escalate to Risk Owner; when any Finding subitem has Severity Critical, change Overall Risk Rating on Vendor Risk Registry to Critical; when Contract Expiry is within 90 days, trigger reassessment if last assessment is older than 6 months. Create a Dashboard with: Vendors by Risk Rating (pie chart), Vendors by Type (bar chart), Overdue Assessments (filtered table), CIP-013 In-Scope Vendors Status (table), Assessment Pipeline (funnel), Open Findings by Severity (chart), Contract Expirations Next 6 Months (calendar), Risk Rating Trend Over Time (line chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Supply Chain Threat Watcher

**Agent Purpose:** Continuously monitor for security incidents at vendor organizations, correlate vendor exposure with the company's OT and IT asset inventory, manage CIP-013 compliance workflows, and automate vendor assessment cycles.

**Triggers:**
- Security incident reported in news or threat intelligence feeds involving a vendor in the Vendor Risk Registry
- Vendor Assessment questionnaire deadline approaching or overdue
- New vendor onboarding request (new item in Vendor Risk Registry)
- CIP-013 compliance review schedule (semi-annual)
- CISA or ICS-CERT advisory mentioning a vendor product used by the company
- Contract renewal approaching for Critical or High criticality vendor

**Actions:**
- Monitor news feeds and threat intelligence for vendor security incidents; create Vendor Incident item and assess potential impact on company systems
- Cross-reference vendor incidents against asset inventory to determine exposure (e.g., "Vendor X breached — they have VPN access to 3 substations")
- Auto-generate and distribute security assessment questionnaires for upcoming reviews
- Track questionnaire responses and auto-flag incomplete or concerning answers for reviewer attention
- Generate CIP-013 compliance evidence packages showing supply chain risk management plan execution
- Recommend risk rating adjustments based on assessment results, incident history, and industry threat intelligence

**Data Required:**
- Vendor Risk Registry with full details
- Threat intelligence feeds and news monitoring for vendor names
- IT and OT asset inventory with vendor relationships
- CIP-013 plan requirements and evidence templates
- Vendor assessment questionnaire templates
- Historical assessment and incident data

**Autonomy Level:** Escalation-Based
Monitoring, alerting, and questionnaire distribution are fully autonomous. Risk rating changes require security team review. Vendor suspension or termination recommendations require CISO and procurement approval. CIP-013 evidence packages require compliance team review.

**Example Interaction:**
> The Supply Chain Threat Watcher detects a SecurityWeek article reporting that Honeywell has disclosed a security incident affecting its cloud-based building management platform. The agent immediately queries the Vendor Risk Registry: Honeywell is listed as a Critical vendor with OT Network Access, providing DCS controllers and the Experion PKS system at 4 refinery and chemical plant facilities. CIP-013 In Scope: Yes. The agent creates a Vendor Incident item, cross-references with the OT Asset Registry (127 Honeywell Experion components across the 4 facilities), and assesses: "The disclosed incident involves Honeywell's cloud platform, not the on-premise Experion PKS system. However, Honeywell has remote diagnostic access to our Experion systems via a vendor VPN. Recommended actions: (1) Immediately audit Honeywell remote access logs for the past 30 days, (2) Contact Honeywell PSIRT for an impact assessment specific to Experion PKS customers, (3) Consider temporarily suspending Honeywell remote access until impact is confirmed, (4) Prepare NERC CIP-013 supply chain incident documentation." The agent has already drafted an email to Honeywell's security contact requesting a customer impact statement and created task items for the OT Security Lead to review access logs.

---

### Use Case 5: Security Awareness Training & Phishing Simulation Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Human error remains the #1 attack vector in the energy sector — 74% of breaches involve a human element (Verizon DBIR). Energy companies must train diverse workforces: corporate IT users who face sophisticated spear-phishing, OT operators who may encounter USB-based attacks or social engineering at remote facilities, executives targeted by business email compromise (BEC), and contractors with varying levels of security awareness. NERC CIP-004 requires security awareness training for personnel with authorized electronic or physical access to BES Cyber Systems, with documented evidence of completion. Most energy companies manage training through a standalone LMS (Learning Management System), run phishing simulations through a separate platform (KnowBe4, Proofpoint), and track compliance in yet another spreadsheet. The training program often feels disconnected from real threats — generic "don't click suspicious links" content rather than energy-industry-specific scenarios like spear-phishing emails impersonating NERC, fake SCADA vendor firmware update notices, or social engineering attempts targeting control room operators.

#### The Solution
monday.com Work Management as a Security Training & Phishing Program Manager. **Training Program** board: Training Module (text), Category (dropdown: General Awareness, Phishing/Social Engineering, OT-Specific Security, Physical Security, CIP Compliance, Incident Reporting, Data Protection, Executive/BEC Protection), Target Audience (dropdown: All Employees, IT Staff, OT Operators, Executives, Contractors, New Hires), Delivery Method (dropdown: eLearning, Instructor-Led, Toolbox Talk, Simulation, Tabletop Exercise), Frequency (dropdown: Annual, Quarterly, Monthly, One-Time, Upon Hire), Due Date, Completion Rate (numbers %), CIP-004 Required (checkbox), Status (status: Scheduled, Active, Completed, Overdue). **Phishing Simulation** board: Campaign Name, Template Theme (dropdown: Vendor Impersonation, Regulatory Notice, IT Helpdesk, Executive Request, Industry News, Benefits/HR, Delivery Notification), Target Group, Send Date, Click Rate (numbers %), Report Rate (numbers %), Compromised Rate (numbers %), Follow-Up Training Assigned (checkbox). **Individual Compliance** board tracking per-person training completion for CIP-004 evidence. **Metrics & Trends** board with dashboards showing program effectiveness over time.

#### The Outcome
CIP-004 training compliance maintained at 100% with automated tracking and reminders. 50% reduction in phishing simulation click rates through targeted, industry-specific training content. Elimination of manual training compliance tracking — automated evidence collection for NERC audits. Risk-based training targeting: employees who fail simulations get additional training automatically. Data-driven security culture metrics for board reporting.

#### Discovery Questions
1. "What's your current phishing simulation click rate, and how does it vary between your corporate and field populations?"
2. "For CIP-004 training compliance, how much time does your team spend tracking who's completed training and chasing down stragglers before the deadline?"
3. "Do your phishing simulations use energy-industry-specific templates — like fake ICS-CERT advisories or vendor firmware update emails — or generic templates?"
4. "When someone fails a phishing simulation, what happens? Is there a structured remediation process, or just a 'don't do that' email?"
5. "How do you handle security training for contractors who have access to your OT environment or BES Cyber Systems? Same program as employees, or separate?"

#### Industry Context
NERC CIP-004 requires security awareness training at least once every 15 calendar months for personnel with authorized electronic or unescorted physical access to BES Cyber Systems. Training must cover the organization's security policies, access controls, and handling of BES Cyber System information. Documented evidence of training completion is required for audits. Beyond CIP, energy companies face industry-specific social engineering threats: attackers impersonating NERC, ICS-CERT, or OT vendors to deliver malware; USB attacks targeting air-gapped OT networks; and physical social engineering at unmanned or remote facilities (substations, pump stations, compressor stations). The 2015 and 2016 Ukraine power grid attacks both involved spear-phishing as the initial access vector. SEs should understand that OT operators require different security training than IT users — they need to recognize threats specific to the OT environment.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Security Awareness Training & Phishing Simulation Management workspace for an energy company. Create a board called 'Training Program' with columns: Module Name (text), Category (dropdown: General Security Awareness, Phishing & Social Engineering, OT/ICS Security, Physical Security, CIP-004 Compliance, Incident Reporting, Data Protection, Executive Protection/BEC, Insider Threat, Supply Chain Security), Target Audience (dropdown: All Employees, Corporate IT Users, OT Operators & Engineers, Control Room Staff, Executives & C-Suite, Contractors & Third Party, New Hires, IT Security Team), Delivery Method (dropdown: eLearning Module, Instructor-Led Classroom, Virtual Instructor-Led, Toolbox Talk, Tabletop Exercise, Phishing Simulation, Hands-On Lab, Video/Micro-Learning), CIP-004 Required (checkbox), Frequency (dropdown: Annual, Semi-Annual, Quarterly, Monthly, Upon Hire, One-Time, Ad Hoc), Current Cycle Due Date (date), Total Assigned (numbers), Completed Count (numbers), Completion Rate (formula as %), Status (status: Upcoming, Active, Completed, Overdue), Owner (people), Next Refresh Date (date). Create a connected board called 'Phishing Simulations' with columns: Campaign Name (text), Simulation Date (date), Template Category (dropdown: OT Vendor Impersonation, Regulatory/NERC Notice, IT Helpdesk, CEO/CFO Request, Industry Conference, Benefits Enrollment, Delivery/Shipping, Breaking News, Vendor Invoice, Password Reset), Difficulty Level (dropdown: Basic, Intermediate, Advanced, Targeted/Spear-Phish), Target Group (dropdown: same as Target Audience), Emails Sent (numbers), Emails Opened (numbers), Links Clicked (numbers), Credentials Entered (numbers), Reported to SOC (numbers), Click Rate (formula), Report Rate (formula), Follow-Up Training Triggered (checkbox), Simulation Status (status: Planning, Approved, Sent, Measuring, Complete). Add automations: when Training Program Completion Rate is below 90% and Due Date is within 14 days, send escalation to department managers of non-completers; when Phishing Simulation Click Rate exceeds 15%, auto-assign remedial training module to clickers; when CIP-004 Required is checked and Due Date is within 30 days and Completion Rate is below 100%, escalate to CIP Compliance Manager; when new Phishing Simulation Complete, create comparison item in Metrics board. Create a Dashboard with: Training Completion by Category (bar chart), Overall CIP-004 Compliance Rate (battery widget), Phishing Click Rate Trend (line chart over 12 months), Click Rate by Template Category (bar chart), Click Rate by Department (table), Overdue Training Modules (filtered table), Upcoming Simulations (calendar), Year-over-Year Improvement (comparison widgets)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Security Culture Coach

**Agent Purpose:** Manage the end-to-end security training lifecycle, personalize training paths based on individual risk profiles, generate energy-industry-specific phishing templates, and ensure CIP-004 compliance with zero manual tracking.

**Triggers:**
- New employee onboarded (HR integration)
- Training module due date approaching (30/14/7 days)
- Phishing simulation completed (results available)
- Individual fails phishing simulation or scores below threshold on training assessment
- CIP-004 training cycle reset (15-month calendar)
- New threat trend identified in energy sector (ICS-CERT advisory, CISA alert)

**Actions:**
- Assign role-appropriate training path to new employees based on department, job role, and access level (IT, OT, executive, contractor)
- Generate customized phishing simulation templates based on current energy sector threats (e.g., "fake ICS-CERT advisory for recently disclosed Siemens vulnerability")
- Create personalized remediation plans for employees who fail simulations, with targeted micro-learning modules
- Track CIP-004 compliance at the individual level, sending escalating reminders (email → manager notification → CISO notification)
- Generate CIP-004 evidence reports showing training completion by individual, date, and module for audit preparation
- Analyze phishing simulation trends to identify high-risk departments or roles and recommend targeted interventions
- Create "threat of the month" awareness campaigns based on current energy sector attack patterns

**Data Required:**
- HR system integration for employee directory, roles, and access levels
- LMS integration for training delivery and completion tracking
- Phishing simulation platform integration (KnowBe4, Proofpoint)
- ICS-CERT/CISA threat intelligence for current energy sector threats
- CIP-004 compliance tracking requirements and deadlines
- Historical training and simulation performance data

**Autonomy Level:** Human-in-the-Loop
Training assignment and reminders are fully autonomous. Phishing simulation scheduling requires security team approval. Phishing template generation (especially spear-phish scenarios) requires review. CIP-004 evidence reports are auto-generated but require compliance manager review before audit submission. Escalations to managers and CISO are automatic.

**Example Interaction:**
> The Security Culture Coach reviews the latest phishing simulation results for the Gulf Coast operations division: a campaign using a template impersonating Schneider Electric ("Critical Firmware Update Required for Modicon M340 — Action Needed") had a 28% click rate among OT engineers — significantly higher than the 8% company average. The agent identifies 14 OT engineers who clicked the simulated phishing link and 3 who entered credentials on the fake page. It immediately assigns a targeted 20-minute micro-learning module on "Verifying OT Vendor Communications" to all 14, with a mandatory completion deadline of 7 days. For the 3 who entered credentials, it assigns an additional 1-hour instructor-led session on "OT-Specific Social Engineering Attacks" and flags their access for enhanced monitoring for 30 days. The agent also generates a recommendation to the Security Awareness Manager: "OT engineering staff show high susceptibility to vendor impersonation attacks. Recommend adding a standing 'Verify Before You Click' toolbox talk topic to the monthly OT safety briefing rotation, and creating a quick-reference card for control rooms showing how to verify legitimate vendor communications." It updates the CIP-004 training records for all affected individuals.

---

### Use Case 6: Identity & Access Management (IAM) Governance

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies manage access for thousands of users across IT systems, OT networks, physical facilities, and third-party vendor connections. NERC CIP-004 requires documented authorization for electronic and unescorted physical access to BES Cyber Systems, with quarterly access reviews and revocation within 24 hours of personnel changes. CIP-005 requires identification of all electronic access points and management of remote access. In practice, access reviews are manual, painful exercises where the IT team exports user lists from 30+ systems, sends them to managers for review, and chases responses for weeks. Orphaned accounts from departed employees or deactivated contractors persist because no one owns the cleanup. OT system access is especially problematic — shared accounts are common on HMIs and engineering workstations because individual authentication was never designed into legacy systems. When a contractor's access isn't revoked promptly, it becomes a compliance violation and a security risk.

#### The Solution
monday.com Work Management as an IAM Governance platform. **Access Entitlements Registry** board: User/Account Name, User Type (dropdown: Employee, Contractor, Vendor, Service Account, Shared Account), Department, Role, Systems with Access (tags: IT Network, OT Network, SCADA, DCS, BES Cyber System, Cloud, Physical Facility, VPN), Access Level (dropdown: Read Only, Standard User, Privileged, Admin, Emergency), BES Access (checkbox), CIP-004 In Scope (checkbox), Access Granted Date, Last Access Review Date, Next Review Due, Review Status (status: Current, Review Due, Under Review, Revocation Pending, Revoked), Manager/Approver (people), Risk Level (status: Low, Medium, High, Critical). **Access Review Campaigns** board: quarterly review cycles with automated workflow for manager certification of access. **Access Requests** board: new access requests with multi-level approval workflow. **Termination/Transfer** board: access revocation tracking with SLA compliance (24-hour CIP requirement). Dashboards showing access review status, orphaned accounts, privileged access inventory, and CIP compliance metrics.

#### The Outcome
100% on-time quarterly access reviews through automated campaign management. 24-hour access revocation SLA met consistently (CIP-004 compliance). Elimination of orphaned and excessive accounts. Complete audit trail of who has access to what, when it was granted, who approved it, and when it was last reviewed. Privileged access inventory providing visibility into the most critical risk.

#### Discovery Questions
1. "How long do your quarterly access reviews take end-to-end? I've heard from other utilities it's a 6-8 week process — is that your experience?"
2. "When someone leaves the company or a contractor's engagement ends, how quickly is their access to BES Cyber Systems revoked? Can you prove it within the CIP-004 24-hour requirement?"
3. "How many shared accounts exist on your OT systems — HMIs, engineering workstations, SCADA servers? How do you attribute actions to individuals on those systems?"
4. "If a NERC auditor asked you to produce a complete list of every person with electronic access to your High Impact BES Cyber Systems — with authorization documentation and last review date — how long would that take?"
5. "Do you have visibility into vendor remote access sessions? When a Siemens or Schneider engineer connects to your OT systems, do you know what they did and for how long?"

#### Industry Context
NERC CIP-004 R4 requires authorization of electronic access and unescorted physical access to BES Cyber Systems, with documented approval by a manager. CIP-004 R5 requires revocation of access within 24 hours for terminations and reassignments, with quarterly reviews to verify access is appropriate. CIP-005 requires identification of all Electronic Access Points (EAPs) and Interactive Remote Access (IRA) sessions. Shared accounts in OT environments are a known challenge — many legacy HMIs and engineering workstations use generic logins because individual authentication wasn't supported. NERC expects compensating controls (logging, badge-in records, camera footage) when individual authentication isn't technically feasible. Privileged Access Management (PAM) solutions like CyberArk and BeyondTrust are common in enterprise IT but often don't extend to OT environments. The SE should understand that IAM in energy is uniquely complex because it spans IT identity (Active Directory), OT access (often separate systems), physical access (badge systems), and vendor access (VPN tunnels).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Identity & Access Management Governance workspace for an energy company. Create a board called 'Access Entitlements Registry' with columns: User Name (text), Employee ID (text), User Type (dropdown: Full-Time Employee, Contractor, Vendor/Third Party, Service Account, Shared/Generic Account), Department (dropdown: IT, OT Engineering, Operations, Corporate, Contractor Pool), Job Role (text), Systems with Access (tags: Active Directory, SAP, SCADA Primary, SCADA Backup, DCS, HMI Workstations, Engineering Workstations, Historian, EMS/ADMS, OT VPN, Cloud AWS, Cloud Azure, Physical Facility, BES Cyber System), Access Level (dropdown: Read Only, Standard, Privileged, Administrator, Emergency/Break Glass), BES Electronic Access (checkbox), BES Physical Access (checkbox), CIP-004 In Scope (checkbox), Access Granted Date (date), Granted By (people), Last Review Date (date), Next Review Due (date), Review Status (status: Current - Green, Due This Month - Yellow, Overdue - Red, Under Review - Blue, Revocation Pending - Orange, Revoked - Gray), Reviewing Manager (people), Risk Level (status: Low, Medium, High, Critical), Notes (long text). Create a connected board called 'Access Review Campaigns' with columns: Campaign Name (text like Q1 2026 Quarterly Review), Review Period (timeline), Review Type (dropdown: Quarterly CIP-004, Annual Full Review, Triggered Review, Termination), Scope (dropdown: All BES Access, All Privileged Access, Specific System, Department-Level), Total Accounts in Scope (numbers), Reviews Completed (numbers), Completion Rate (formula), Exceptions Found (numbers), Revocations Initiated (numbers), Campaign Status (status: Planning, In Progress, Manager Review, Remediation, Complete, Overdue), Campaign Owner (people). Create a board called 'Access Revocations' with columns: User Name (text), Connected Entitlement (connect to Access Entitlements Registry), Trigger (dropdown: Termination, Transfer, Contractor End Date, Review Finding, Security Incident, Voluntary Request), Trigger Date (date), 24-Hour SLA Deadline (date), Systems to Revoke (tags), Revocation Status (status: Pending, In Progress, Completed, Verified, SLA Breached), Completed Date (date), Completed By (people), Verification Evidence (files). Add automations: when Next Review Due is within 14 days and Review Status is Current, change to Due This Month and notify Reviewing Manager; when Trigger Date is set in Access Revocations, auto-calculate 24-Hour SLA Deadline and if not Completed within 24 hours, mark SLA Breached and escalate to CISO; when Review Campaign Completion Rate reaches 100%, change Campaign Status to Complete. Create a Dashboard with: Access Review Completion Rate (battery widget), Accounts by User Type (pie chart), CIP-004 In-Scope Accounts Status (bar chart), Overdue Reviews (filtered table), Active Revocations (table), SLA Compliance Rate (number widget), Privileged Account Count by System (bar chart), Access Review Campaign Progress (stacked bar chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Access Lifecycle Manager

**Agent Purpose:** Automate access review campaigns, ensure 24-hour revocation SLA compliance, identify excessive and orphaned access, and maintain CIP-004/CIP-005 compliance evidence automatically.

**Triggers:**
- Quarterly access review cycle start date
- HR integration: employee termination, transfer, or role change event
- Contractor end-date approaching (14 days/7 days/day-of)
- CIP-004 24-hour revocation SLA timer approaching deadline
- New access request submitted
- Access anomaly detected (e.g., dormant account suddenly active)

**Actions:**
- Generate and distribute access review campaigns to appropriate managers with per-user certification interface
- Create immediate revocation tasks when termination or contractor end-date events are received from HR
- Track revocation progress across all systems and escalate when SLA is at risk
- Identify orphaned accounts (no associated active employee/contractor record) and flag for review
- Identify excessive access (users with privileges beyond their role) and recommend right-sizing
- Generate CIP-004 and CIP-005 compliance evidence packages showing access authorizations, reviews, and revocations with timestamps
- Audit shared/generic OT accounts and document compensating controls

**Data Required:**
- HR system integration (employee status, department, role changes, terminations)
- Active Directory / identity provider integration
- OT system access lists (SCADA, DCS, HMI user accounts)
- Physical access system (badge/card access) integration
- VPN and remote access gateway logs
- CIP-004/CIP-005 compliance requirements and evidence templates

**Autonomy Level:** Escalation-Based
Review campaign generation, reminders, and revocation task creation are fully autonomous. Actual access revocation (disabling accounts) requires IT/OT admin execution and verification. CIP compliance evidence packages require compliance team review. Access anomaly alerts are autonomous with escalation to security team.

**Example Interaction:**
> At 4:15 PM on a Friday, the Access Lifecycle Manager receives an HR integration event: contractor Maria Santos from Burns & McDonnell has had her engagement terminated effective today. The agent immediately creates a revocation task, sets the 24-hour SLA deadline for 4:15 PM Saturday, and queries the Access Entitlements Registry. Maria has access to: Active Directory (standard), OT VPN (for remote SCADA monitoring during a substation upgrade project), two HMI workstations at the Riverview substation, and badge access to the Riverview control house. All are CIP-004 in scope. The agent creates sub-tasks for each system revocation: (1) Disable AD account — assigned to IT helpdesk, (2) Revoke OT VPN certificate — assigned to OT Network Admin, (3) Remove HMI workstation credentials — assigned to Riverview OT Engineer (on-site required), (4) Deactivate badge — assigned to Physical Security. It sends notifications to all assignees with the SLA deadline prominently displayed. At 9 AM Saturday, the agent checks progress: AD and badge are done, OT VPN is done, but HMI credentials haven't been addressed because the OT Engineer is on day shift starting at 6 AM Monday. The agent escalates to the OT Security Lead, noting that the SLA will breach in 7 hours, and recommends an interim compensating control: "Disable the OT VPN path to the Riverview HMIs so Maria's HMI credentials are unreachable even if not yet removed locally."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| SCADA | Supervisory Control and Data Acquisition — systems that monitor and control industrial processes across large geographic areas (pipelines, power grids) |
| DCS | Distributed Control System — controls industrial processes within a single facility (refineries, power plants) |
| PLC | Programmable Logic Controller — ruggedized computer controlling specific industrial equipment or processes |
| HMI | Human-Machine Interface — display/workstation where operators interact with SCADA/DCS systems |
| OT | Operational Technology — hardware and software that detects or causes changes in physical processes (vs. IT) |
| ICS | Industrial Control Systems — umbrella term for SCADA, DCS, PLCs, and related OT systems |
| NERC CIP | North American Electric Reliability Corporation Critical Infrastructure Protection — mandatory cybersecurity standards for the bulk electric system |
| BES | Bulk Electric System — the interconnected electrical generation and transmission system |
| FERC | Federal Energy Regulatory Commission — oversees NERC and approves CIP standards |
| TSA SD | Transportation Security Administration Security Directives — cybersecurity requirements for pipeline operators issued post-Colonial Pipeline |
| CISA | Cybersecurity and Infrastructure Security Agency — federal agency coordinating critical infrastructure cybersecurity |
| ICS-CERT | Industrial Control Systems Cyber Emergency Response Team (now CISA ICS) — publishes advisories for OT vulnerabilities |
| Purdue Model | ISA-95 reference architecture defining network segmentation levels (Level 0-5) for industrial environments |
| MITRE ATT&CK for ICS | Framework cataloging tactics and techniques used by adversaries against industrial control systems |
| SIS | Safety Instrumented System — independent automated system designed to prevent catastrophic industrial accidents |
| RTU | Remote Terminal Unit — device that interfaces with physical equipment and communicates with SCADA |
| SIEM | Security Information and Event Management — platform aggregating and analyzing security logs |
| SOAR | Security Orchestration, Automation, and Response — platform automating security operations workflows |
| EDR | Endpoint Detection and Response — security tool monitoring endpoints for threats |
| PAM | Privileged Access Management — controls and audits administrative/elevated access |
| SOC | Security Operations Center — team/facility monitoring for security threats 24/7 |
| GRC | Governance, Risk, and Compliance — framework and tools for managing regulatory and security requirements |
| CVE | Common Vulnerabilities and Exposures — standardized identifier for security vulnerabilities |
| CVSS | Common Vulnerability Scoring System — standard for rating vulnerability severity (0-10) |
| CISA KEV | CISA Known Exploited Vulnerabilities catalog — list of vulnerabilities confirmed to be actively exploited |
| CIRCIA | Cyber Incident Reporting for Critical Infrastructure Act — requires 72-hour incident reporting to CISA |
| CIP-013 | NERC CIP standard specifically addressing supply chain risk management for BES Cyber Systems |
| Air Gap | Physical isolation of a network from external connections — increasingly rare in modern OT due to operational needs |
| DMZ | Demilitarized Zone — network segment between IT and OT networks that mediates data exchange (Purdue Level 3.5) |
| LDAR | Leak Detection and Repair — environmental compliance program (relevant because LDAR systems are increasingly connected to OT networks) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CISO | Owns cybersecurity strategy, risk management, and regulatory compliance across IT and OT | Decision-maker |
| VP/Director OT Security | Manages security for SCADA, DCS, and all industrial control systems | Decision-maker for OT tools |
| Director IT Security | Manages enterprise IT security operations, SOC, and incident response | Decision-maker for IT tools |
| CIP Compliance Manager | Ensures NERC CIP compliance, manages evidence, coordinates audits | Influencer — drives compliance tool requirements |
| SOC Manager | Runs 24/7 security monitoring and initial incident response | Influencer — drives operational tool requirements |
| VP/Director GRC | Manages governance, risk, and compliance programs including third-party risk | Influencer — drives GRC platform decisions |
| OT Network Engineer | Manages and secures OT network infrastructure (firewalls, switches, DMZ) | User — technical evaluator |
| Security Analyst/Engineer | Performs threat hunting, vulnerability management, and incident investigation | User — primary daily operator |
| VP Operations / Plant Manager | Owns production availability — must approve any OT changes including security patches | Gatekeeper — operational authority over OT |
| CIO | Oversees IT organization; CISO may report to CIO or separately | Executive sponsor (IT side) |
| Chief Risk Officer | Enterprise risk management including cyber risk | Executive sponsor (enterprise risk) |
| Board Audit/Risk Committee | Provides board-level oversight of cybersecurity program | Executive oversight |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT Operations | Manages IT infrastructure, service desk, and network that Security monitors and protects | Cross-sell IT service management; infrastructure monitoring dashboards |
| OT/Operations Engineering | Owns and operates the SCADA/DCS/ICS systems that Security must protect without disrupting | Cross-sell OT operations management; maintenance scheduling |
| Legal | Handles regulatory response (NERC violations, TSA directives), breach notification, and litigation | Cross-sell legal workflow management; regulatory tracking |
| Compliance/Audit | Internal audit function that tests security controls and CIP compliance | Cross-sell audit management; control testing workflows |
| Procurement | Manages vendor relationships and contracts with security requirements | Cross-sell procurement management; vendor lifecycle tracking |
| HR | Manages employee lifecycle events that trigger access provisioning/revocation | Cross-sell HR workflow automation; onboarding/offboarding |
| Physical Security | Manages facility access, surveillance, and physical protection that intersects with CIP-006 | Cross-sell physical security management; convergence of cyber-physical |
| Executive/Board | Receives cybersecurity risk reports and approves security investment | Cross-sell executive dashboards; board reporting |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow GRC / SecOps | Enterprise GRC and security operations platform | monday.com offers faster deployment, better UX, and significantly lower cost; ideal for mid-size utilities that can't afford ServiceNow's complexity; supplements rather than replaces for large enterprises |
| RSA Archer | Legacy GRC platform dominant in energy sector | Aging platform with poor UX and high TCO; monday.com provides modern, flexible alternative for compliance tracking and risk management |
| Splunk / Microsoft Sentinel | SIEM platforms for security monitoring | monday.com doesn't replace SIEM but provides the workflow layer that SIEM tools lack — incident management, compliance tracking, and cross-team coordination that lives on top of SIEM data |
| Dragos / Claroty / Nozomi | OT security monitoring platforms | monday.com complements rather than replaces these — provides the vulnerability management, incident tracking, and compliance workflows that OT monitoring tools feed into |
| KnowBe4 / Proofpoint Security Awareness | Phishing simulation and training platforms | monday.com manages the training program lifecycle, compliance tracking, and metrics that these tools don't handle well — program management on top of training delivery |
| CyberArk / BeyondTrust | Privileged Access Management | monday.com provides the governance layer (access reviews, certification campaigns, compliance evidence) that complements PAM technical controls |
| Jira / Asana | General project management used by security teams | monday.com offers better customization for security-specific workflows, compliance evidence management, and cross-team visibility |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use ServiceNow GRC for CIP compliance" | "ServiceNow GRC is powerful but requires dedicated administrators and months of implementation for each new workflow. monday.com gives your compliance team the ability to build and modify workflows themselves — when NERC revises a CIP standard, you can update your tracking in hours, not months. Many energy companies use monday.com alongside ServiceNow for operational flexibility." |
| "Security tools need to be hardened enterprise platforms — monday.com is a work management tool" | "You're right that your SIEM, EDR, and OT monitoring tools need to be specialized. But the workflow on top of those tools — incident management, compliance tracking, access reviews, training programs — that's project management with security context. monday.com gives security teams the flexibility to build exactly the workflows they need without waiting for IT to configure a GRC platform." |
| "Our CISO would never approve storing security data in a SaaS platform" | "monday.com is SOC 2 Type II certified with enterprise security controls. The data in monday.com isn't your raw security telemetry — it's workflow metadata: who's assigned to what, what's the status of an access review, which evidence is overdue. Your sensitive data stays in your SIEM and OT monitoring tools. monday.com manages the process around that data." |
| "We're in the middle of a NERC audit — we can't change tools right now" | "That's actually the perfect time to evaluate. After the audit, ask your team how much time they spent manually assembling evidence vs. how much time they could have saved with automated tracking. Most CIP compliance teams tell us the audit preparation alone justifies the investment." |
| "OT security is too specialized for a general platform" | "That specialization lives in your Dragos, Claroty, or Nozomi platforms. But vulnerability prioritization, patch campaign coordination with Operations, and CIP compliance evidence management? That's workflow orchestration — exactly what monday.com excels at. The Vibe capability means you can build OT-specific workflows in minutes." |
| "We need FedRAMP/StateRAMP authorization for government-regulated infrastructure" | "monday.com is pursuing FedRAMP authorization. In the interim, the platform's SOC 2 Type II certification and HIPAA compliance capabilities meet the security requirements for most energy companies. The compliance tracking and workflow management use case doesn't require storing CUI or classified data — it manages the process, not the sensitive telemetry." |

## Proof Points
*(To be populated with customer references)*
- [Utility using monday.com for NERC CIP compliance evidence management]
- [Energy company managing security incident response workflows in monday.com]
- [Oil & gas company tracking OT vulnerability management in monday.com]
- [Energy company consolidating security program management from spreadsheets to monday.com]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*