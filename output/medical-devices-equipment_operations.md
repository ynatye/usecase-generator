# Medical Devices & Equipment × Operations Playbook

## Overview
Operations teams in medical device companies manage the most highly regulated manufacturing environments in industry. Under FDA 21 CFR Part 820 (Quality System Regulation) and ISO 13485 standards, these teams orchestrate complex workflows spanning design transfer, supplier qualification, production planning for Class I/II/III devices, and rigorous process validation (IQ/OQ/PQ). Operations must maintain clean room manufacturing environments, execute sterilization validation protocols, and ensure complete lot/batch traceability from raw materials to patient delivery. The department typically manages 50-500+ person teams across manufacturing, quality assurance, supply chain, and regulatory compliance functions, with every decision requiring extensive documentation for FDA audit trails and post-market surveillance requirements.

Modern medical device operations face unprecedented pressure to accelerate time-to-market while maintaining zero-defect quality standards. Between CAPA investigations, MDR reporting, UDI compliance, and field safety corrective actions, teams spend 40-60% of their time on documentation and compliance activities rather than value-adding work. The complexity of coordinating device master records (DMR) with device history records (DHR) while managing supplier qualifications and incoming inspections creates bottlenecks that can delay critical medical innovations reaching patients.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|-------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | HIGH | Quality documentation, batch record reviews, and CAPA investigations require massive manual effort. AI agents can work 24/7 on document review, compliance checking, and routine inspections. |
| **Consolidate Tech Stack with AI** | HIGH | Most med device companies use 8-15 disconnected systems (ERP, QMS, MES, LIMS, document control). One AI platform can replace multiple tools while ensuring regulatory compliance. |
| **Scale Impact Without Overhead** | MEDIUM | Growing production volume without proportionally growing quality and compliance teams. AI enables scaling oversight and documentation without linear headcount growth. |

## Prioritized Use Cases

---

### Use Case 1: Automated CAPA Investigation Management

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
CAPA investigations consume 20-40 hours per incident, requiring cross-functional teams to analyze root causes, implement corrective actions, and document everything for FDA compliance. With medical device companies averaging 50-200+ CAPAs annually, this represents 1,000-8,000 hours of high-skilled labor. Traditional manual processes create bottlenecks in identifying systemic issues, often leading to repeat deviations and extended FDA responses times.

#### The Solution
monday.com AI Agents automatically initiate CAPA workflows upon deviation detection, pulling relevant data from quality systems, assigning cross-functional investigation teams based on device type and severity, and tracking all documentation requirements through resolution. The Service product manages customer complaints that trigger CAPAs, while Vibe-built boards provide real-time dashboards for FDA audit readiness.

#### The Outcome
Reduce CAPA investigation cycle time from 30-45 days to 15-20 days. Save 60% of administrative time (12-24 hours per CAPA). Achieve 99%+ on-time FDA response compliance. Enable quality teams to focus on root cause analysis rather than paperwork coordination.

#### Discovery Questions
- How many CAPAs does your organization handle annually, and what's your average time to closure?
- What percentage of your quality team's time is spent on CAPA documentation versus actual investigation work?
- How do you currently track the effectiveness of implemented corrective actions?
- What's your biggest challenge in meeting FDA response timelines for CAPA-related inquiries?
- How do you ensure visibility into systemic trends across multiple CAPA investigations?

#### Industry Context
CAPA (Corrective and Preventive Action) is mandated by FDA 21 CFR Part 820.100 and ISO 13485. Every nonconformance, customer complaint, or internal audit finding can trigger a CAPA. The investigation must document root cause analysis, corrective actions, preventive actions, and effectiveness verification. FDA expects trending analysis to identify systemic issues before they become major problems.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a CAPA Investigation Management board with these columns: CAPA Number (text), Device Product Line (dropdown with Class I, Class II, Class III), Issue Description (long text), Severity Level (dropdown with Critical, Major, Minor), Root Cause Category (dropdown with Design, Process, Supplier, Training, Documentation), Investigation Team (people), Investigation Due Date (date), FDA Response Required (checkbox), Corrective Actions (long text), Preventive Actions (long text), Effectiveness Verification (date), Status (status with New, Investigating, Actions Pending, Verification, Closed). Add automation to notify quality manager when new CAPA is created and when FDA response deadline approaches in 3 days. Create dashboard view showing open CAPAs by product line and overdue items. Include Kanban view by Status for investigation workflow management."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CAPA Investigation Orchestrator

**Agent Purpose:**  
Automatically initiates, coordinates, and tracks CAPA investigations from deviation detection through FDA-compliant closure.

**Triggers:**
- New quality deviation or nonconformance entry
- Customer complaint submission via Service integration
- Internal audit finding flagged for CAPA
- Supplier quality notification received
- Manual CAPA initiation by quality personnel

**Actions:**
- Create CAPA investigation workspace with all required documentation templates
- Assign investigation team based on device type, severity, and departmental expertise
- Generate root cause analysis framework specific to the deviation category
- Schedule and track all investigation milestones with FDA timeline compliance
- Automatically escalate overdue items to quality management
- Compile effectiveness verification reports and trend analysis

**Data Required:**
- Quality management system integration
- Product classification data (Class I/II/III devices)
- Personnel expertise profiles and availability
- Historical CAPA data for trending analysis

**Autonomy Level:** Human-in-the-Loop
Agent handles workflow orchestration and administrative tasks autonomously. Human expertise required for root cause analysis, corrective action determination, and final approval.

**Example Interaction:**
> A batch of Class III cardiac stents fails sterility testing during final inspection. Within 30 minutes, the CAPA Investigation Orchestrator detects the deviation, creates a new investigation workspace, and assembles a cross-functional team including manufacturing engineer, microbiologist, and regulatory specialist. The agent generates a sterility failure investigation template, schedules team meetings, and begins pulling relevant batch records, environmental monitoring data, and sterilization validation protocols. It immediately flags this as FDA-reportable under MDR requirements and creates parallel workflows for customer notification and regulatory submission. The quality manager receives a comprehensive briefing with all relevant data organized for immediate investigation launch.

---

### Use Case 2: Design Transfer & Process Validation Coordination

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Design transfer from R&D to manufacturing requires coordinating 15-25 different workstreams including process validation (IQ/OQ/PQ), supplier qualification, equipment qualification, and training validation. These projects typically span 6-18 months with complex dependencies across engineering, quality, manufacturing, and regulatory teams. Manual coordination using spreadsheets and email leads to delays, missed requirements, and FDA Form 483 observations.

#### The Solution
Vibe creates comprehensive design transfer project templates with automated dependency tracking, milestone management, and regulatory deliverable checklists. AI agents monitor project health, automatically escalate risks, and ensure all FDA requirements are met before production release. Integration with document control systems ensures all design controls and DHR requirements are satisfied.

#### The Outcome
Reduce design transfer timeline by 25-40% (2-7 months faster). Achieve 95%+ first-pass FDA inspection success rate. Eliminate 80% of administrative coordination overhead. Enable simultaneous parallel workstreams with automated dependency management.

#### Discovery Questions
- How long does your typical design transfer process take from design freeze to production release?
- What percentage of your design transfers experience significant delays due to coordination challenges?
- How do you currently track the hundreds of deliverables required for a successful design transfer?
- What's your biggest bottleneck in coordinating process validation activities across multiple departments?
- How do you ensure design control requirements are properly transferred to manufacturing documentation?

#### Industry Context
Design transfer per FDA 21 CFR Part 820.30(h) requires formal procedures to ensure design requirements are correctly translated to production. Process validation must demonstrate the manufacturing process consistently produces devices meeting specifications. IQ (Installation Qualification), OQ (Operational Qualification), and PQ (Performance Qualification) protocols must be executed and approved before commercial production.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Design Transfer Master Project board with columns: Work Package (text), Deliverable Type (dropdown with IQ Protocol, OQ Protocol, PQ Protocol, DMR Creation, Training Materials, Supplier Qual, Process Flow, Risk Assessment), Responsible Department (dropdown with Engineering, Quality, Manufacturing, Regulatory, Supply Chain), Owner (people), Planned Start (date), Planned Complete (date), Status (status with Not Started, In Progress, Review, Approved, On Hold), Dependencies (connect to items), Risk Level (dropdown with Low, Medium, High, Critical), FDA Requirement (checkbox). Add automation to notify project manager when high-risk items are overdue and send weekly status reports to leadership. Create Timeline view for project Gantt chart and Dashboard view showing completion percentage by department and overdue critical path items."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Design Transfer Project Controller

**Agent Purpose:**  
Orchestrates complex design transfer projects ensuring all FDA requirements and dependencies are managed automatically.

**Triggers:**
- Design freeze milestone achieved in R&D
- New product transfer request submitted
- Process validation schedule update
- Dependency change notification
- Weekly project health assessment

**Actions:**
- Generate comprehensive design transfer project plan with all FDA-required deliverables
- Monitor critical path dependencies and automatically adjust schedules
- Validate design control documentation completeness before transfer initiation
- Coordinate cross-functional team assignments based on workload and expertise
- Generate regulatory submission packages with all required validation data
- Create training schedules and track completion for all involved personnel

**Data Required:**
- Design history file (DHF) from R&D systems
- Manufacturing resource availability
- Supplier qualification status database
- Personnel training records and certifications

**Autonomy Level:** Escalation-Based
Agent manages routine scheduling, documentation tracking, and status reporting autonomously. Escalates to human project managers for resource conflicts, scope changes, or critical path issues.

**Example Interaction:**
> When the R&D team completes design freeze for a new Class II orthopedic implant, the Design Transfer Project Controller immediately creates a 127-task project plan spanning 14 months. It identifies that titanium supplier qualification is the critical path bottleneck and automatically escalates to procurement with a 6-week acceleration request. The agent coordinates IQ/OQ/PQ protocol development across three manufacturing sites, schedules equipment qualifications around planned maintenance windows, and generates a master training matrix for 23 personnel across four departments. Weekly automated reports show leadership that the project is tracking 3 weeks ahead of schedule due to optimized parallel workstream coordination.

---

### Use Case 3: Supplier Quality & Incoming Inspection Management

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device companies manage 100-500+ suppliers across raw materials, components, and contract manufacturing. Each supplier requires qualification, periodic audits, incoming inspection protocols, and performance monitoring. Supplier quality issues can trigger FDA regulatory actions and patient safety concerns. Manual tracking across multiple suppliers creates blind spots and reactive rather than proactive quality management.

#### The Solution
monday.com CRM tracks supplier relationships with quality performance dashboards. AI agents monitor supplier scorecards, automatically trigger audits based on performance degradation, and coordinate incoming inspection schedules based on risk profiles. Automated workflows ensure supplier nonconformances are addressed within regulatory timelines.

#### The Outcome
Reduce supplier quality incidents by 40-60%. Automate 70% of routine supplier management tasks. Enable proactive supplier risk management with real-time performance monitoring. Scale supplier oversight without proportional headcount growth.

#### Discovery Questions
- How many active suppliers do you manage, and what's your current supplier audit frequency?
- What percentage of incoming material requires inspection, and how do you prioritize inspection activities?
- How quickly do you identify and respond to supplier performance trends?
- What's your biggest challenge in maintaining supplier qualification documentation?
- How do you coordinate supplier corrective actions across multiple product lines?

#### Industry Context
FDA 21 CFR Part 820.50 requires supplier controls ensuring purchased products conform to specified requirements. Supplier qualification must include evaluation of quality systems, and incoming inspection requirements vary based on supplier performance and criticality of supplied components. ISO 13485 requires risk-based supplier management approaches.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Supplier Quality Management board with columns: Supplier Name (text), Product Category (dropdown with Raw Materials, Components, Contract Manufacturing, Packaging), Risk Classification (dropdown with Critical, High, Medium, Low), Quality Score (numbers), Last Audit Date (date), Next Audit Due (date), Incoming Inspection Rate (percentage), Recent Nonconformances (numbers), CAPA Status (status with None, Open, Closed), Contract Manufacturer (checkbox), ISO Certification (date), Supplier Contact (people). Add automation to send audit reminder 30 days before due date and escalate to quality manager when quality score drops below 85. Create dashboard showing supplier risk distribution, overdue audits, and quality trend charts. Include calendar view for audit scheduling."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Supplier Risk Intelligence Agent

**Agent Purpose:**  
Continuously monitors supplier performance and proactively manages quality risks across the entire supplier network.

**Triggers:**
- Incoming inspection failure threshold exceeded
- Quality score trending downward over 3 months
- Supplier audit due date approaching
- Nonconformance report submitted
- New supplier onboarding initiated

**Actions:**
- Calculate risk-adjusted inspection rates based on supplier performance history
- Generate audit schedules optimizing resource allocation across risk priorities
- Automatically escalate suppliers approaching critical quality thresholds
- Coordinate supplier corrective action requests with defined response timelines
- Compile supplier performance reports for management review and FDA readiness
- Update incoming inspection protocols based on real-time performance data

**Data Required:**
- Incoming inspection results database
- Supplier audit history and findings
- Nonconformance tracking system
- Purchase order and delivery data

**Autonomy Level:** Fully Autonomous
Agent operates independently for routine monitoring, risk assessment, and escalation. Human oversight required only for final supplier qualification decisions and audit scope definition.

**Example Interaction:**
> The Supplier Risk Intelligence Agent detects that titanium rod supplier TitanMed's incoming inspection failure rate has increased from 2% to 7% over six weeks, while delivery delays have doubled. The agent immediately escalates TitanMed to enhanced incoming inspection (100% vs. standard 10%), schedules an expedited supplier audit within 30 days, and generates a supplier corrective action request with specific performance requirements. It simultaneously identifies backup suppliers for critical titanium components and provides procurement with qualified alternatives. Quality management receives a comprehensive briefing showing the issue timeline, financial impact analysis, and recommended actions - all delivered within hours of detecting the performance degradation pattern.

---

### Use Case 4: Production Planning & Batch Record Management

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device production requires meticulous batch record management with complete traceability from raw materials to finished goods. Production planners must coordinate device master records (DMR) with device history records (DHR) while managing lot/batch traceability, sterilization validation schedules, and clean room capacity constraints. Manual coordination often leads to production delays and incomplete batch documentation.

#### The Solution
Work Management provides production planning boards with automated batch record generation, material traceability tracking, and clean room scheduling optimization. AI agents monitor production progress, automatically update DHR documentation, and ensure UDI compliance for all manufactured devices.

#### The Outcome
Reduce production planning time by 50-70%. Achieve 99%+ batch record accuracy and completeness. Eliminate manual DHR compilation saving 8-15 hours per batch. Enable real-time production visibility and predictive capacity planning.

#### Discovery Questions
- How many production batches do you manufacture monthly, and what's your average batch record compilation time?
- What percentage of your production delays are caused by documentation or material traceability issues?
- How do you currently manage clean room scheduling and capacity optimization?
- What's your biggest challenge in maintaining complete lot/batch traceability?
- How do you ensure UDI compliance across all manufactured devices?

#### Industry Context
Device Master Record (DMR) contains device specifications, production processes, quality assurance procedures, and labeling. Device History Record (DHR) documents the production history of each batch including material lot numbers, equipment used, personnel involved, and quality test results. UDI (Unique Device Identification) requires unique identifiers for medical devices to enable tracking and traceability.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Production Planning & Batch Management board with columns: Batch Number (text), Product SKU (text), Device Class (dropdown with Class I, Class II, Class III), Planned Quantity (numbers), Production Start Date (date), Production Complete Date (date), Clean Room Assignment (dropdown with CR-101, CR-102, CR-103, CR-201), Sterilization Method (dropdown with EtO, Gamma, Steam, Aseptic), Material Lots Used (long text), UDI Generated (checkbox), DHR Status (status with Incomplete, In Progress, Review, Complete), Lot Release Approved (checkbox), Quality Inspector (people). Add automation to notify production manager when batch is overdue and alert quality when DHR review is needed. Create Timeline view for production scheduling and Dashboard view showing clean room utilization and batch completion rates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Batch Production Orchestrator

**Agent Purpose:**  
Automates batch record creation, material traceability tracking, and production documentation throughout the manufacturing process.

**Triggers:**
- New production order created in ERP system
- Material receipt confirmation for scheduled batch
- Production milestone completion (setup, processing, inspection)
- Quality hold or deviation detected during production
- Sterilization cycle completion notification

**Actions:**
- Generate device history record (DHR) templates with all required documentation sections
- Track material lot consumption and update traceability records in real-time
- Coordinate clean room scheduling based on product requirements and capacity optimization
- Monitor sterilization validation parameters and document cycle completion
- Generate UDI labels and update device identification databases
- Compile final batch release documentation with all quality approvals

**Data Required:**
- Device master record (DMR) specifications
- Material inventory and lot tracking systems
- Clean room capacity and scheduling data
- Sterilization equipment status and validation records

**Autonomy Level:** Human-in-the-Loop
Agent handles routine documentation and tracking automatically. Human approval required for batch release decisions and deviation investigations.

**Example Interaction:**
> When a production order for 5,000 cardiac stents enters the system, the Batch Production Orchestrator immediately generates DHR templates, reserves clean room CR-201 for three days, schedules EtO sterilization cycles, and pulls all required material lots from inventory. As production progresses, the agent tracks each operation completion, documents personnel assignments, and monitors environmental conditions. When a minor deviation occurs during packaging (label misalignment), the agent immediately creates a deviation report, notifies quality assurance, and holds the affected units pending investigation. Upon resolution, it updates the DHR with corrective actions taken and enables batch release with complete traceability documentation ready for FDA inspection.

---

### Use Case 5: Post-Market Surveillance & Field Action Coordination

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Post-market surveillance requires monitoring device performance in the field, investigating adverse events, and coordinating field safety corrective actions when necessary. Medical device companies must track MDR reporting requirements, manage customer complaints, and maintain vigilance for emerging safety signals. Manual processes often delay critical safety responses and create compliance gaps.

#### The Solution
Service product manages customer complaints and adverse event reports with automated MDR timeline tracking. AI agents analyze complaint patterns for safety signals, coordinate field corrective actions, and ensure regulatory reporting compliance across global markets.

#### The Outcome
Reduce post-market surveillance response time by 60%. Achieve 100% MDR reporting compliance within required timelines. Enable proactive safety signal detection through automated pattern analysis. Coordinate global field actions efficiently.

#### Discovery Questions
- How many customer complaints do you receive annually, and what's your current investigation timeline?
- What's your process for identifying safety trends from complaint data?
- How do you currently manage MDR reporting requirements across different regulatory jurisdictions?
- What's your biggest challenge in coordinating field corrective actions when required?
- How do you ensure post-market data feeds back into design improvements?

#### Industry Context
MDR (Medical Device Reporting) requires manufacturers to report deaths, serious injuries, and certain device malfunctions to FDA within specific timelines (24 hours to 30 days depending on severity). Post-market surveillance per 21 CFR Part 820.198 requires monitoring and analysis of device performance data to identify potential safety issues requiring field corrective actions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Post-Market Surveillance board with columns: Complaint ID (text), Product Line (dropdown), Device Serial Number (text), Customer Location (location), Date Reported (date), Complaint Category (dropdown with Performance, Safety, Labeling, Packaging), Severity Level (dropdown with Death, Serious Injury, Malfunction, Minor), MDR Required (checkbox), MDR Report Date (date), Investigation Status (status with New, Investigating, Complete, Closed), Field Action Required (checkbox), Root Cause (long text), Corrective Action (long text), Reporter (people). Add automation to alert regulatory team when MDR deadline approaches and notify management for serious injury cases. Create Dashboard view showing complaint trends by product line and geographical distribution. Include calendar view for regulatory reporting deadlines."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Post-Market Safety Intelligence Agent

**Agent Purpose:**  
Continuously monitors post-market data to identify safety signals and orchestrates regulatory-compliant investigation and response activities.

**Triggers:**
- New customer complaint submitted via multiple channels
- Adverse event report received from healthcare provider
- Pattern recognition threshold exceeded for specific product line
- Regulatory authority inquiry received
- Field service report indicating potential safety issue

**Actions:**
- Automatically categorize and prioritize complaints based on severity and regulatory requirements
- Generate MDR reports with pre-populated data and regulatory timeline tracking
- Analyze complaint patterns using statistical methods to identify emerging safety signals
- Coordinate field corrective action plans when safety signals are confirmed
- Compile trend analysis reports for regulatory submissions and management review
- Interface with global regulatory databases for international reporting requirements

**Data Required:**
- Customer complaint database with detailed device information
- Field service reports and performance data
- Regulatory submission tracking system
- Global regulatory requirement database by jurisdiction

**Autonomy Level:** Escalation-Based
Agent handles routine complaint processing, data analysis, and report generation autonomously. Escalates to human experts for safety signal evaluation and field action decisions.

**Example Interaction:**
> The Post-Market Safety Intelligence Agent detects a cluster of seven similar complaints about catheter tip separation across four hospitals in the past 30 days - a 300% increase from baseline. Within hours, the agent initiates comprehensive investigation workflows, pulls all manufacturing records for affected lot numbers, and begins MDR report preparation. It identifies 847 potentially affected devices in the field and generates a preliminary field safety notice for regulatory review. The agent coordinates with field service teams to inspect similar devices at key accounts and provides quality assurance with a complete investigation framework including recommended laboratory testing protocols. Senior management receives a comprehensive briefing with risk assessment, regulatory implications, and recommended response options - enabling critical safety decisions within 24 hours of pattern detection.

---

### Use Case 6: GMP Training & Compliance Management

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
GMP compliance requires extensive personnel training on procedures, equipment operation, and regulatory requirements. Training records must be maintained for FDA inspections, and retraining must occur when procedures change. Managing training compliance across large manufacturing teams creates administrative burden and compliance risks when personnel work on products they're not qualified to handle.

#### The Solution
Work Management provides training matrix management with automated scheduling, completion tracking, and compliance reporting. AI agents monitor training compliance, automatically schedule refresher training, and ensure personnel qualifications match production assignments.

#### The Outcome
Achieve 100% training compliance with automated tracking. Reduce training administration time by 80%. Eliminate production delays due to unqualified personnel. Enable real-time compliance reporting for FDA readiness.

#### Discovery Questions
- How many personnel require GMP training, and how often must training be refreshed?
- What percentage of your training activities are currently tracked manually?
- How do you ensure only qualified personnel work on specific products or processes?
- What's your biggest challenge in managing training records for FDA inspections?
- How do you coordinate training schedules with production demands?

#### Industry Context
FDA 21 CFR Part 820.25 requires personnel performing work affecting conformity to device requirements be competent on the basis of appropriate education, training, skills and experience. Training records must demonstrate personnel competency for specific tasks and be available during FDA inspections.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a GMP Training Management board with columns: Employee Name (people), Department (dropdown with Manufacturing, Quality, Warehouse, Maintenance), Training Module (dropdown with GMP Basics, Aseptic Technique, Equipment Operation, Document Control, CAPA Procedures), Training Date (date), Expiration Date (date), Training Status (status with Current, Expiring Soon, Expired, Scheduled), Trainer (people), Test Score (numbers), Retraining Required (checkbox), Product Line Qualification (tags). Add automation to notify employee and manager 30 days before training expires and alert HR when someone works on unqualified product line. Create Dashboard showing compliance percentage by department and upcoming training requirements."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Training Compliance Guardian

**Agent Purpose:**  
Ensures 100% GMP training compliance by automatically managing training schedules, tracking qualifications, and preventing unqualified personnel assignments.

**Triggers:**
- New employee onboarding initiated
- Training certificate approaching expiration (30/60/90 days)
- Procedure revision requiring retraining
- Production assignment for unqualified personnel detected
- FDA inspection or audit scheduled

**Actions:**
- Generate personalized training plans based on role requirements and product assignments
- Schedule training sessions optimizing instructor availability and production schedules
- Monitor training completion and automatically update qualification databases
- Block production system access for personnel with expired qualifications
- Generate training compliance reports by department, product line, and regulatory requirement
- Coordinate refresher training when procedures are revised or updated

**Data Required:**
- Personnel database with role assignments and product responsibilities
- Training curriculum and regulatory requirement mappings
- Production scheduling system integration
- Document control system for procedure revisions

**Autonomy Level:** Fully Autonomous
Agent operates independently for routine training scheduling, compliance monitoring, and reporting. Human oversight required only for training content development and exception approvals.

**Example Interaction:**
> The Training Compliance Guardian identifies that sterile processing technician Maria Santos' aseptic technique certification expires in 25 days, coinciding with a scheduled 10,000-unit cardiac catheter production run she's assigned to support. The agent immediately schedules her recertification training during the following week's maintenance shutdown, reserves qualified backup coverage for the production run, and notifies both Maria and her supervisor. When a procedure revision is issued for catheter tip assembly, the agent identifies 12 personnel requiring retraining, schedules group sessions to minimize production impact, and temporarily restricts their access to the affected work instructions until retraining is complete. All training records are automatically updated and compiled into FDA-ready compliance reports.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **FDA 21 CFR Part 820** | Quality System Regulation governing medical device manufacturing |
| **ISO 13485** | International standard for medical device quality management systems |
| **Design Controls** | FDA requirement for systematic controls during device design process |
| **DHR (Device History Record)** | Documentation of the production history of a finished device |
| **DMR (Device Master Record)** | Compilation of records containing device specifications and production processes |
| **CAPA** | Corrective and Preventive Action process for addressing nonconformances |
| **MDR** | Medical Device Reporting - mandatory adverse event reporting to FDA |
| **UDI** | Unique Device Identification system for device traceability |
| **Process Validation** | IQ/OQ/PQ protocols demonstrating consistent manufacturing process |
| **Clean Room Manufacturing** | Controlled environment with specified contamination levels |
| **Sterilization Validation** | Documented evidence that sterilization process achieves required sterility assurance |
| **Lot/Batch Traceability** | Ability to track products from raw materials through distribution |
| **Incoming Inspection** | Testing and verification of purchased products and materials |
| **Supplier Qualification** | Process to evaluate and approve suppliers of materials and services |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **VP Operations** | Overall manufacturing strategy, capacity planning, regulatory compliance | High - Budget authority and strategic decisions |
| **Manufacturing Director** | Daily production operations, workforce management, cost control | High - Direct operational control |
| **Quality Assurance Manager** | Regulatory compliance, quality systems, FDA inspection readiness | High - Veto power over production releases |
| **Production Planning Manager** | Scheduling, material coordination, capacity optimization | Medium - Tactical execution focus |
| **Regulatory Affairs Director** | FDA submissions, compliance monitoring, audit management | Medium - Specialist influence on compliance |
| **Supply Chain Manager** | Supplier relationships, material procurement, inventory management | Medium - Controls material flow |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **R&D/Engineering** | Design transfer, change control, technical documentation | Design history file management, engineering change workflow automation |
| **Quality Assurance** | CAPA investigations, audit management, compliance reporting | Integrated quality management system replacing multiple tools |
| **Regulatory Affairs** | FDA submissions, global compliance, labeling requirements | Regulatory submission tracking and deadline management |
| **Customer Service** | Complaint handling, field service coordination, customer communication | Post-market surveillance integration and customer feedback analysis |
| **Supply Chain** | Supplier management, material planning, procurement | Supplier quality management and procurement workflow optimization |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **TrackWise/Sparta QMS** | Legacy quality management systems with limited AI capabilities | Replace with AI-powered quality workflows and automated compliance |
| **SAP/Oracle ERP** | Enterprise systems with basic manufacturing modules | Supplement with AI-driven production optimization and real-time visibility |
| **MasterControl** | Document control and training management | Consolidate multiple quality tools into single AI platform |
| **Arena PLM** | Product lifecycle management for design controls | Integrate design transfer workflows with manufacturing execution |
| **Salesforce** | CRM with basic complaint handling | Replace with medical device-specific Service product and AI agents |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We're heavily regulated - can't risk changing systems" | "We understand FDA compliance is non-negotiable. Our platform is designed for regulated industries with built-in audit trails, electronic signatures, and FDA 21 CFR Part 11 compliance. We help customers pass inspections, not risk them." |
| "Our ERP handles production planning already" | "ERPs are great for transactions, but they lack the AI-powered insights and cross-functional collaboration that modern medical device operations require. We integrate with your ERP while providing the operational intelligence and automation layer on top." |
| "Quality can't be automated - it requires human judgment" | "Absolutely correct. Our AI agents handle the administrative burden - documentation, scheduling, data compilation - so your quality experts can focus their judgment on actual root cause analysis and decision-making, not paperwork." |
| "We need specialized medical device functionality" | "We've built specific capabilities for medical device operations including DHR/DMR management, CAPA workflows, supplier qualification tracking, and post-market surveillance. This isn't generic software adapted for medical devices." |
| "Integration with existing systems seems complex" | "We integrate with QMS, ERP, and LIMS systems that medical device companies already use. Our professional services team has deep experience with FDA-regulated environments and handles technical integration while your team focuses on operational improvements." |

## Proof Points
*(To be populated with customer references)*

- [ ] Class III device manufacturer achieving 40% reduction in design transfer timeline
- [ ] Orthopedic device company eliminating 60% of CAPA investigation administrative time
- [ ] Cardiac device manufacturer achieving 100% FDA inspection readiness with automated documentation
- [ ] Medical device contract manufacturer scaling 3x production volume without proportional quality team growth
- [ ] Diagnostic device company reducing supplier quality incidents by 50% through proactive monitoring

---

*Generated: 2026-02-21 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*