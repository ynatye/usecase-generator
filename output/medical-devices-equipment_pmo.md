# Medical Devices & Equipment × PMO Playbook

## Overview
Project Management Offices (PMOs) in the medical device industry operate as the strategic nerve center for complex, highly regulated product development initiatives. These teams orchestrate new product development (NPD) stage-gate processes, coordinate cross-functional design reviews, and manage regulatory submission timelines across multiple product portfolios. PMO teams typically range from 5-25 professionals at mid-market companies to 50-150+ at large multinational organizations, supporting R&D, regulatory, clinical, and manufacturing teams through intricate project lifecycles that can span 2-7 years.

Medical device PMOs face unique challenges including FDA/CE marking compliance requirements, design control milestone tracking, V&V protocol execution coordination, and post-market surveillance project management. They must balance aggressive time-to-market pressures with rigorous quality standards while managing resource allocation across R&D, regulatory, and clinical workstreams. The regulatory complexity—from 510(k) clearances to PMA submissions—demands specialized project tracking capabilities that traditional PMO tools struggle to address.

The stakes are extraordinarily high: a single missed design control milestone can delay product launch by 6-18 months, while regulatory submission errors can cost millions in remediation and FDA warning letter responses. PMOs must provide real-time visibility into manufacturing validation schedules (IQ/OQ/PQ), supplier qualification timelines, and clinical trial project management while maintaining audit-ready documentation for quality system inspections.

## Value Driver Mapping
| Value Driver | Relevance | Why It Resonates |
|--------------|-----------|------------------|
| **Replace or Radically Augment Headcount** | High | PMO analysts spend 60-80% of time on manual status reporting, milestone tracking, and compliance documentation. AI agents can handle routine project updates, regulatory deadline monitoring, and cross-functional communication 24/7. |
| **Consolidate Tech Stack with AI** | Very High | Medical device PMOs typically juggle 8-15 disconnected tools: MS Project, Smartsheet, Veeva Vault, MasterControl, Excel trackers, SharePoint, and department-specific systems. One AI platform can replace most while providing unified visibility. |
| **Scale Impact Without Overhead** | High | Product portfolios are expanding 30-50% annually while regulatory complexity increases. PMOs need to manage more projects without proportional headcount growth, especially as companies pursue multiple market entries simultaneously. |

## Prioritized Use Cases

---

### Use Case 1: NPD Stage-Gate Orchestration

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Medical device PMOs manually track 15-30+ stage-gate milestones across product development phases (Concept, Feasibility, Development, Verification/Validation, Launch). Teams use disconnected Excel trackers, MS Project files, and SharePoint sites, creating visibility gaps and version control nightmares. Critical design control checkpoints get missed, causing regulatory submission delays worth $2-5M in lost revenue per month. Cross-functional teams (R&D, regulatory, clinical, manufacturing) lack real-time visibility into interdependent deliverables.

#### The Solution
monday.com Work Management creates a unified NPD stage-gate command center with automated milestone tracking, cross-functional dashboards, and intelligent deadline management. Custom board templates for each gate phase capture design control requirements, regulatory deliverables, and V&V protocols. Timeline views show critical path dependencies across R&D, regulatory, and manufacturing workstreams. Automated notifications keep stakeholders aligned on gate readiness criteria and escalate at-risk milestones.

#### The Outcome
- 40% reduction in stage-gate cycle time through eliminated handoff delays
- 90% decrease in missed design control milestones 
- $3-8M revenue protection per product through faster time-to-market
- 70% less time spent on status reporting across cross-functional teams

#### Discovery Questions
- "How many active NPD projects are you tracking through stage-gate right now, and what's your typical timeline from concept to commercial launch?"
- "When a design control milestone gets missed, what's the cascading impact on your regulatory submission timeline and commercial launch date?"
- "How do you currently ensure R&D, regulatory, clinical, and manufacturing teams stay synchronized on interdependent deliverables?"
- "What percentage of your PMO team's time is spent manually updating project status across different systems versus strategic project guidance?"
- "How visible are you to potential bottlenecks in your V&V protocol execution or design transfer activities?"

#### Industry Context
Medical device stage-gate processes are far more complex than traditional product development due to FDA design controls (21 CFR Part 820), which require formal documentation at each phase. Gate criteria include design inputs/outputs, risk analysis updates, verification protocols, validation studies, and regulatory strategy alignment. PMOs must coordinate with quality assurance for design control compliance while balancing aggressive commercial timelines. The average Class II device requires 18-24 months from concept to 510(k) submission, with Class III devices extending 3-5 years through PMA pathways.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an NPD Stage-Gate Project Tracker with these columns: Product Name (text), Stage-Gate Phase (dropdown: Concept, Feasibility, Development, V&V, Launch, Post-Market), Gate Status (status: Not Started, In Progress, Gate Review Pending, Approved, On Hold), Target Gate Date (date), Actual Gate Date (date), Days Behind/Ahead (formula), Project Manager (people), R&D Lead (people), Regulatory Lead (people), Clinical Lead (people), Manufacturing Lead (people), Risk Level (dropdown: Low, Medium, High, Critical), Design Control Deliverables (checklist), Regulatory Submission Type (dropdown: 510k, PMA, CE Mark, De Novo), Commercial Launch Date (date), Revenue Impact (numbers), and Notes (long text). Add automations: notify project manager when gate review is 7 days overdue, notify executives when projects are more than 30 days behind schedule, and change status to 'At Risk' when target dates are missed. Include timeline view showing all projects with gate milestones and dashboard view with stage-gate pipeline metrics."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Stage-Gate Orchestrator

**Agent Purpose:**  
Autonomously monitors NPD stage-gate progress, identifies bottlenecks, and orchestrates cross-functional alignment to prevent milestone delays.

**Triggers:**
- Gate milestone approaching (7, 14, 30 day alerts)
- Design control deliverable marked complete
- Regulatory submission status change
- Cross-functional dependency conflict detected
- Gate review meeting scheduled

**Actions:**
- Generate gate readiness assessments with deliverable status
- Create cross-functional alignment meetings when dependencies conflict
- Escalate at-risk projects to executives with impact analysis
- Update commercial launch forecasts based on gate progression
- Generate regulatory submission checklists customized by device type
- Coordinate design review scheduling across R&D, regulatory, and quality teams

**Data Required:**
- NPD project timelines and dependencies
- Design control deliverable templates by device class
- Regulatory submission requirements by market (FDA, CE, others)
- Resource calendars for cross-functional teams
- Historical stage-gate performance data

**Autonomy Level:** Human-in-the-Loop  
Agent autonomously monitors and coordinates routine activities but escalates strategic decisions like gate approval recommendations, resource reallocation, or commercial launch date changes to PMO leadership.

**Example Interaction:**
> The Stage-Gate Orchestrator detects that the CardioVue monitor project's Development gate is at risk—the design verification protocol is 2 weeks overdue and the manufacturing lead just flagged a supplier qualification delay. The agent immediately generates a gate readiness assessment showing 7 of 12 deliverables complete, calculates the downstream impact on the 510(k) submission timeline (pushed from Q3 to Q4), and creates an urgent cross-functional alignment meeting for tomorrow morning. It notifies the PMO director with a detailed impact analysis: "CardioVue launch delay will shift $12M revenue from Q4 to Q1, affecting annual targets. Recommend expediting backup supplier qualification or considering design modification." The agent pre-populates the meeting agenda with specific decision points and alternative mitigation strategies based on similar historical delays.

---

### Use Case 2: Regulatory Submission Timeline Management

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device PMOs manually track complex regulatory submission timelines across multiple markets (FDA 510(k)/PMA, CE marking, Health Canada, etc.). Regulatory affairs teams work in isolation using separate systems, creating visibility gaps for PMO leadership. Critical submission deadlines get missed due to incomplete documentation, causing 6-18 month launch delays worth millions in lost revenue. Cross-functional teams lack visibility into regulatory requirements and submission dependencies, leading to last-minute scrambling and expedited consulting fees.

#### The Solution
monday.com creates a centralized regulatory submission command center with automated milestone tracking, document management, and cross-functional coordination. Custom templates for 510(k), PMA, and CE marking submissions ensure nothing falls through cracks. Integration with quality management systems provides real-time document status updates. AI-powered timeline optimization identifies critical path bottlenecks and recommends mitigation strategies.

#### The Outcome
- 50% reduction in regulatory submission preparation time
- 80% decrease in missed submission deadlines
- $2-5M revenue protection per product through faster market entry
- 60% reduction in external regulatory consulting costs

#### Discovery Questions
- "What's your current timeline from design freeze to FDA 510(k) submission, and how often do you hit those targets?"
- "How do you currently coordinate between R&D, regulatory affairs, and quality assurance for submission readiness?"
- "When regulatory requirements change mid-project, how quickly can you assess impact across your entire product portfolio?"
- "What percentage of your regulatory submissions require amendment cycles, and what's typically the root cause?"
- "How visible are you to potential bottlenecks in predicate device research or clinical data collection?"

#### Industry Context
Regulatory submission complexity varies dramatically by device classification and target markets. 510(k) submissions average 6-12 months preparation time with 180+ supporting documents, while PMA submissions can require 2-3 years with clinical trial data coordination. CE marking requires MDR compliance with authorized representative coordination across EU markets. PMOs must coordinate technical documentation, clinical evidence, risk management files, and quality system documentation while managing parallel submissions across multiple markets to optimize global launch timing.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Regulatory Submission Tracker with these columns: Product Name (text), Submission Type (dropdown: 510k, PMA, CE Mark, Health Canada, De Novo), Target Market (dropdown: US, EU, Canada, Australia, Japan, Global), Submission Status (status: Planning, Document Prep, Technical Review, Submitted, Under Review, Approved, Additional Info Requested), Submission Date (date), Target Approval Date (date), Regulatory Lead (people), Technical Writer (people), Clinical Lead (people), Quality Lead (people), Predicate Device (text), Essential Requirements Checklist (checklist), Clinical Data Required (dropdown: None, Literature Review, Clinical Study, Post-Market Data), Risk Classification (dropdown: Class I, Class II, Class III), Review Timeline (numbers), Revenue at Risk (numbers), and Priority (dropdown: Critical, High, Medium, Low). Add automations: notify team when submission deadline is 30 days away, escalate to executives when submissions are rejected or additional info requested, and update revenue forecasts when approval dates change. Include Kanban view for submission pipeline and dashboard showing regulatory approval metrics by market."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Submission Coordinator

**Agent Purpose:**  
Autonomously manages regulatory submission workflows, ensures documentation completeness, and optimizes approval timelines across multiple markets.

**Triggers:**
- Submission milestone approaching (30, 60, 90 day alerts)
- Regulatory document status change in quality system
- FDA/regulatory body guidance update affecting active submissions
- Clinical data milestone completion
- Predicate device recall or classification change

**Actions:**
- Generate submission readiness checklists customized by device type and market
- Coordinate technical writing assignments based on team availability
- Monitor regulatory body processing times and adjust timeline forecasts
- Create contingency plans when submissions face additional info requests
- Update commercial launch forecasts based on regulatory approval delays
- Generate competitive analysis when predicate devices face regulatory issues

**Data Required:**
- Regulatory submission templates by device class and market
- Historical regulatory review timelines by submission type
- Technical documentation status from quality management systems
- Clinical study progress and data availability
- Predicate device regulatory status monitoring

**Autonomy Level:** Escalation-Based  
Agent autonomously handles routine coordination and documentation tracking but escalates to regulatory affairs leadership when submissions face rejection risk, require strategic pivots, or impact commercial launch timing.

**Example Interaction:**
> The Regulatory Submission Coordinator identifies that the FlexiStent 510(k) submission is at risk—the biocompatibility testing report is 3 weeks overdue and the chosen predicate device just received an FDA warning letter. The agent immediately flags this high-risk situation, generates alternative predicate device options with comparative analysis, and calculates the impact: switching predicate devices could delay submission by 6-8 weeks but reduces approval risk by 40%. It schedules an urgent regulatory strategy meeting, pre-populates decision matrices comparing predicate options, and creates parallel work streams to minimize timeline impact. The agent also monitors the original predicate's warning letter response timeline to assess if that pathway remains viable.

---

### Use Case 3: Clinical Trial Project Management

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device PMOs struggle to coordinate clinical trials across multiple sites, investigators, and regulatory jurisdictions. Clinical project timelines frequently slip due to enrollment challenges, site activation delays, and data collection issues. PMOs lack real-time visibility into trial progress, creating blind spots for commercial planning. CROs provide inconsistent reporting formats, making it difficult to aggregate progress across studies. Protocol amendments and regulatory changes create cascading impacts that are difficult to track and communicate.

#### The Solution
monday.com provides centralized clinical trial oversight with site-level tracking, enrollment monitoring, and milestone management. Custom dashboards aggregate CRO reporting and provide real-time trial health metrics. Automated workflows coordinate protocol amendments, regulatory submissions, and site communications. Integration capabilities pull data from EDC systems and clinical databases for comprehensive project visibility.

#### The Outcome
- 30% reduction in clinical trial timeline variability
- 50% improvement in enrollment rate predictability  
- $1-3M cost savings per trial through optimized site management
- 80% reduction in time spent consolidating CRO reports

#### Discovery Questions
- "How many clinical trials are you currently managing, and what's your typical enrollment timeline versus plan?"
- "When a clinical site underperforms on enrollment, how quickly can you identify and address the issue?"
- "How do you currently track protocol amendments across multiple studies and their impact on timelines?"
- "What's your process for coordinating between CROs, regulatory affairs, and clinical operations teams?"
- "How visible are you to potential data quality issues or regulatory inspection readiness across trial sites?"

#### Industry Context
Medical device clinical trials differ significantly from pharmaceutical studies—often shorter duration but requiring specialized surgical procedures or device implantation expertise. Site selection is critical as only certain centers have qualified investigators and adequate case volume. IDE studies for Class III devices may require 5-20 sites with 100-500 patients, while some Class II studies can be completed with literature reviews or small feasibility studies. PMOs must coordinate with clinical affairs, biostatistics, regulatory affairs, and external CROs while maintaining GCP compliance and FDA inspection readiness.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Clinical Trial Management system with these columns: Study Name (text), Study Phase (dropdown: Feasibility, Pivotal, Post-Market, Registry), Study Status (status: Planning, Site Selection, IRB Approval, Patient Enrollment, Data Collection, Database Lock, Statistical Analysis, Report Writing, Complete), Principal Investigator (people), Clinical Lead (people), CRO Name (text), Target Enrollment (numbers), Current Enrollment (numbers), Enrollment Rate (formula), Sites Activated (numbers), Total Planned Sites (numbers), First Patient In (date), Last Patient Out (date), Database Lock Date (date), Study Budget (numbers), Enrollment Behind/Ahead Schedule (formula), and Primary Endpoint (text). Add automations: notify when enrollment is 20% behind target, escalate when sites haven't enrolled patients in 30 days, and alert when database lock date approaches with incomplete data. Include timeline view showing all study milestones and dashboard with enrollment metrics and site performance."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Clinical Trial Optimizer

**Agent Purpose:**  
Autonomously monitors clinical trial progress, identifies enrollment bottlenecks, and optimizes site performance to accelerate study completion.

**Triggers:**
- Site enrollment rate falls below threshold
- Protocol amendment submitted to regulatory authorities
- Adverse event report filed requiring safety database update
- Database query resolution overdue
- Regulatory inspection scheduled at trial site

**Actions:**
- Generate site performance reports with enrollment rate analysis
- Create site activation improvement plans for underperforming locations
- Coordinate protocol amendment impact assessments across all active sites
- Update commercial launch timelines based on clinical milestone performance
- Generate regulatory inspection preparation checklists for trial sites
- Optimize patient screening processes based on enrollment data patterns

**Data Required:**
- Clinical trial protocols and inclusion/exclusion criteria
- Site activation timelines and investigator qualifications
- Patient screening and enrollment data from EDC systems
- Historical site performance benchmarks
- Regulatory submission timelines and approval status

**Autonomy Level:** Human-in-the-Loop  
Agent autonomously optimizes routine trial operations and site management but requires clinical affairs approval for protocol modifications, site additions/removals, or study timeline changes.

**Example Interaction:**
> The Clinical Trial Optimizer detects that the CardioMax pivotal study is falling behind enrollment targets—3 of 12 sites haven't enrolled patients in 6 weeks, and the current rate projects a 4-month delay in database lock. The agent analyzes screening data and identifies the issue: 40% of potential patients are being excluded due to overly restrictive blood pressure criteria. It generates a protocol amendment recommendation to expand eligibility criteria, models the impact (could accelerate enrollment by 60% with minimal safety risk based on literature review), and creates implementation timelines. The agent schedules a clinical affairs review meeting, prepares regulatory submission templates for the amendment, and calculates the commercial impact: 4-month delay would push launch from Q2 to Q3, affecting $15M in first-year revenue. It also identifies backup sites with similar patient populations that could be activated to mitigate timeline risk.

---

### Use Case 4: Design Transfer Coordination

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Design transfer from R&D to manufacturing involves coordinating hundreds of technical documents, specifications, and validation activities across engineering, quality, and manufacturing teams. PMOs spend countless hours tracking design control deliverables, manufacturing validation protocols (IQ/OQ/PQ), and supplier qualification activities. Process validation failures during design transfer can delay launch by 6-12 months and require expensive remediation. Cross-functional teams struggle to maintain version control across design history files (DHF) and device master records (DMR).

#### The Solution
monday.com orchestrates design transfer with automated deliverable tracking, cross-functional coordination, and validation milestone management. Custom workflows ensure design controls compliance while managing IQ/OQ/PQ execution across manufacturing sites. Integration with quality management systems provides real-time document control and approval tracking. Automated notifications keep stakeholders aligned on design transfer readiness and manufacturing validation progress.

#### The Outcome
- 40% reduction in design transfer timeline through improved coordination
- 60% decrease in process validation failures and rework
- $1-2M cost savings per product through efficient manufacturing startup
- 50% less time spent on design control documentation management

#### Discovery Questions
- "How long does your typical design transfer process take from design freeze to commercial production?"
- "What percentage of your design transfers encounter process validation failures requiring remediation?"
- "How do you currently coordinate between R&D, quality assurance, and manufacturing during design transfer?"
- "When manufacturing validation protocols fail, what's the typical root cause and timeline to resolution?"
- "How do you ensure design history file completeness and maintain version control across multiple manufacturing sites?"

#### Industry Context
Design transfer is a critical FDA design control requirement (21 CFR 820.30(i)) that ensures products can be manufactured consistently to design specifications. The process involves transferring design outputs to manufacturing, establishing production processes, and validating that manufacturing can produce devices meeting all specifications. IQ/OQ/PQ validation sequences must be completed before commercial production, with detailed protocols documenting equipment qualification, process validation, and performance verification. Any failures during this phase can trigger CAPA requirements and delay product launch.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Design Transfer Coordination system with these columns: Product Name (text), Transfer Phase (dropdown: Pre-Transfer, DHF Review, Process Development, IQ Validation, OQ Validation, PQ Validation, Commercial Ready), Transfer Status (status: Planning, In Progress, On Hold, Complete, Failed), R&D Lead (people), Manufacturing Lead (people), Quality Lead (people), Manufacturing Site (dropdown: Site A, Site B, Contract Manufacturer), DHF Completeness (progress), IQ Status (status), OQ Status (status), PQ Status (status), Process Validation Batch (numbers), Commercial Launch Date (date), Transfer Budget (numbers), Risk Assessment (dropdown: Low, Medium, High), and Validation Findings (long text). Add automations: notify quality when DHF review is complete, escalate when validation protocols fail, alert manufacturing when process development is ready, and update commercial timelines when delays occur. Include Kanban view for transfer pipeline and timeline view showing validation milestones across products."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Design Transfer Orchestrator

**Agent Purpose:**  
Autonomously coordinates design transfer activities, monitors validation progress, and ensures manufacturing readiness for commercial production.

**Triggers:**
- Design freeze milestone reached in NPD project
- Design history file (DHF) review completed by quality
- Manufacturing validation protocol scheduled
- Process validation batch results available
- Supplier qualification status change

**Actions:**
- Generate design transfer readiness checklists with DHF completeness verification
- Coordinate validation protocol scheduling across manufacturing sites
- Create process development timelines based on manufacturing capacity
- Generate supplier qualification tracking with critical component priorities
- Update commercial production forecasts based on validation progress
- Create CAPA workflows when validation protocols fail

**Data Required:**
- Design control deliverables from NPD projects
- Manufacturing site capabilities and capacity planning
- Supplier qualification status and lead times
- Historical validation performance data
- Quality system requirements by manufacturing location

**Autonomy Level:** Human-in-the-Loop  
Agent autonomously coordinates routine transfer activities and validation scheduling but requires quality and manufacturing approval for protocol modifications, site selection, or commercial production authorization.

**Example Interaction:**
> The Design Transfer Orchestrator identifies that the SurgiScope product is ready to begin design transfer—the design freeze is complete and DHF review passed quality inspection. The agent automatically generates the transfer timeline, coordinates IQ/OQ/PQ validation scheduling across 3 manufacturing sites, and identifies a potential bottleneck: the critical imaging sensor supplier hasn't completed qualification protocols. It creates expedited supplier qualification workflows, calculates the risk (30% chance of 8-week delay if supplier fails), and recommends backup supplier activation. The agent schedules cross-functional transfer kickoff meetings, pre-populates validation protocol templates with product-specific requirements, and establishes commercial production forecasts. When OQ validation fails at Site B due to environmental chamber calibration issues, the agent immediately creates CAPA workflows, reschedules validation for 2 weeks out, and notifies commercial teams of potential launch impact while exploring alternative site options.

---

### Use Case 5: Post-Market Surveillance & CAPA Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Medical device PMOs struggle to coordinate post-market surveillance activities, complaint investigations, and CAPA (Corrective and Preventive Action) projects across quality, clinical, and regulatory teams. Customer complaints, field corrections, and adverse event reports create complex investigation workflows that span multiple departments. CAPA projects often stall due to poor coordination, creating FDA inspection risks and potential recall scenarios. PMOs lack visibility into surveillance trends and their impact on existing product portfolios and future development priorities.

#### The Solution
monday.com creates a centralized post-market surveillance command center with automated complaint tracking, CAPA project management, and trend analysis capabilities. Custom workflows coordinate investigation activities across quality, clinical affairs, and regulatory teams. Integration with complaint handling systems provides real-time case status updates. AI-powered analytics identify emerging safety trends and their impact on product lifecycle decisions.

#### The Outcome
- 50% reduction in CAPA project closure time
- 70% improvement in complaint investigation coordination
- 80% decrease in FDA inspection findings related to post-market surveillance
- 60% faster identification of emerging safety trends requiring field actions

#### Discovery Questions
- "How many active CAPA projects are you currently managing, and what's your average time to closure?"
- "When a customer complaint suggests a potential safety issue, how quickly can you coordinate investigation across quality, clinical, and regulatory teams?"
- "How do you currently track post-market surveillance trends and their impact on your product development pipeline?"
- "What's your process for determining when a field issue requires a field correction versus recall?"
- "How visible are you to potential systemic quality issues across your manufacturing sites and product lines?"

#### Industry Context
Post-market surveillance is a critical FDA requirement (21 CFR 820.198) that requires manufacturers to monitor device performance and take corrective action when issues arise. Medical device complaints must be investigated within specific timeframes, with reportable events submitted to FDA via MDR reporting. CAPA projects address systemic issues and require root cause analysis, corrective actions, preventive measures, and effectiveness verification. Field corrections and recalls require coordinated responses across quality, regulatory, clinical, and commercial teams with strict FDA notification requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Post-Market Surveillance & CAPA Management system with these columns: Issue ID (text), Issue Type (dropdown: Customer Complaint, Field Correction, Adverse Event, CAPA Project, Recall), Product Affected (text), Issue Status (status: New, Investigation, Root Cause Analysis, Corrective Action, Preventive Action, Verification, Closed), Quality Lead (people), Clinical Lead (people), Regulatory Lead (people), Commercial Lead (people), Severity Level (dropdown: Minor, Moderate, Major, Critical), Investigation Deadline (date), CAPA Due Date (date), Root Cause (long text), Corrective Actions (checklist), Preventive Actions (checklist), Effectiveness Verified (checkbox), MDR Required (checkbox), Field Action Required (dropdown: None, Field Correction, Recall), and Customer Impact (numbers). Add automations: escalate when investigation deadlines are missed, notify regulatory when MDR reporting is required, alert executives when recalls are recommended, and track CAPA effectiveness verification deadlines. Include dashboard showing surveillance trends by product line and timeline view for CAPA project milestones."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Post-Market Surveillance Coordinator

**Agent Purpose:**  
Autonomously monitors post-market safety signals, coordinates investigation activities, and ensures timely CAPA closure to maintain regulatory compliance.

**Triggers:**
- New customer complaint received requiring investigation
- Adverse event report submitted to regulatory database
- CAPA investigation deadline approaching
- Field correction effectiveness review due
- Regulatory inspection announced

**Actions:**
- Generate investigation assignment workflows based on complaint severity and product type
- Coordinate cross-functional investigation teams with appropriate expertise
- Create MDR reporting templates with regulatory submission deadlines
- Generate trend analysis reports identifying emerging safety patterns
- Update product risk assessments based on post-market surveillance data
- Create field action recommendations when safety thresholds are exceeded

**Data Required:**
- Customer complaint databases and case management systems
- Adverse event reporting requirements by regulatory jurisdiction
- Historical CAPA closure performance and effectiveness data
- Product risk management files and safety specifications
- Field performance data from sales and service teams

**Autonomy Level:** Escalation-Based  
Agent autonomously handles routine surveillance coordination and investigation workflows but escalates to quality leadership when field corrections or recalls are recommended, or when systematic quality issues are identified.

**Example Interaction:**
> The Post-Market Surveillance Coordinator detects a concerning trend: 5 customer complaints in 2 weeks about CardioVue monitor battery performance, all from the same manufacturing lot. The agent immediately flags this as a potential systematic issue, generates investigation workflows with lot-specific analysis requirements, and coordinates teams across quality (manufacturing investigation), clinical affairs (safety assessment), and regulatory (MDR evaluation). It identifies that this lot was produced during a recent process change and creates comparative analysis with pre/post change performance. The agent calculates the population at risk (2,847 devices in field), generates field correction recommendation templates, and schedules emergency cross-functional review. When investigation confirms a manufacturing process deviation, the agent creates comprehensive field correction workflows, drafts customer notification letters, and establishes effectiveness monitoring protocols to track field action success.

---

### Use Case 6: Portfolio Prioritization & Resource Allocation

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device PMOs struggle with portfolio prioritization across competing NPD projects, each requiring specialized resources (R&D engineers, regulatory specialists, clinical investigators). Resource allocation decisions are made with incomplete visibility into cross-project dependencies and capacity constraints. Clinical, regulatory, and manufacturing resources are often over-allocated, creating bottlenecks that cascade across multiple projects. PMO leadership lacks real-time visibility into resource utilization and project portfolio health, making strategic planning reactive rather than proactive.

#### The Solution
monday.com provides comprehensive portfolio management with resource capacity planning, cross-project dependency tracking, and strategic prioritization frameworks. Custom dashboards show resource allocation across all projects with bottleneck identification and optimization recommendations. Scenario planning capabilities model the impact of priority changes and resource reallocation decisions. Integration with time tracking and capacity planning tools provides real-time utilization metrics.

#### The Outcome
- 35% improvement in resource utilization across R&D, regulatory, and clinical teams
- 50% reduction in project delays caused by resource conflicts
- $3-7M increased portfolio value through optimized prioritization
- 60% less time spent on resource allocation decisions and project portfolio reviews

#### Discovery Questions
- "How many active NPD projects are competing for the same pool of R&D and regulatory resources?"
- "When you need to reprioritize projects due to market changes, how quickly can you assess resource reallocation impact?"
- "What visibility do you have into utilization rates across your specialized teams like regulatory affairs and clinical operations?"
- "How do you currently balance high-revenue opportunities against strategic platform investments?"
- "When resource conflicts arise between projects, what's your decision-making framework for resolution?"

#### Industry Context
Medical device portfolio management is complicated by highly specialized resource requirements and long development timelines. Regulatory expertise cannot be easily substituted between projects, and clinical investigators may have specific therapeutic area specialization. Resource planning must account for regulatory submission timelines (can't accelerate FDA review), clinical enrollment rates (site-dependent), and manufacturing validation sequences (must follow predetermined protocols). Strategic decisions must balance immediate revenue opportunities against long-term platform investments and regulatory pathway optimization.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Portfolio Prioritization & Resource Allocation system with these columns: Project Name (text), Strategic Priority (dropdown: Critical, High, Medium, Low, On Hold), Commercial Potential (numbers), Development Stage (dropdown: Concept, Feasibility, Development, Clinical, Regulatory, Launch), Resource Category (dropdown: R&D Engineering, Regulatory Affairs, Clinical Operations, Manufacturing, Quality), Resource Allocation (numbers), Resource Utilization (progress), Required FTEs (numbers), Available FTEs (numbers), Resource Gap (formula), Project Manager (people), Executive Sponsor (people), Risk Level (dropdown: Low, Medium, High, Critical), Market Opportunity (numbers), Competition Level (dropdown: First-to-Market, Competitive, Crowded), and Strategic Rationale (long text). Add automations: alert when resource utilization exceeds 100%, notify executives when critical projects face resource shortages, escalate when multiple high-priority projects compete for same resources, and update portfolio metrics when project priorities change. Include matrix view showing resource allocation across all projects and dashboard with portfolio health metrics."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio Optimization Engine

**Agent Purpose:**  
Autonomously optimizes project portfolio prioritization and resource allocation to maximize strategic value while maintaining delivery commitments.

**Triggers:**
- New project proposal submitted for portfolio inclusion
- Resource capacity change (hiring, attrition, allocation changes)
- Market opportunity update affecting project priorities
- Project milestone achievement changing resource requirements
- Competitive landscape shift requiring strategic response

**Actions:**
- Generate portfolio optimization recommendations based on strategic value scoring
- Create resource reallocation scenarios with timeline and revenue impact analysis
- Identify resource bottlenecks and recommend capacity expansion or priority adjustments
- Update commercial forecasts based on portfolio prioritization changes
- Generate competitive response strategies when market dynamics shift
- Create resource development plans to address chronic skill shortages

**Data Required:**
- Strategic value frameworks and scoring criteria
- Resource capacity and skill availability across departments
- Market opportunity assessments and competitive intelligence
- Historical project performance and resource utilization data
- Financial models and revenue forecasting assumptions

**Autonomy Level:** Human-in-the-Loop  
Agent autonomously generates optimization recommendations and scenario analyses but requires executive approval for major portfolio priority changes, resource reallocation decisions, or project cancellations.

**Example Interaction:**
> The Portfolio Optimization Engine identifies a critical resource conflict: the CardioVue and NeuroStim projects both require the same senior regulatory specialist for 510(k) submissions in Q3, but she's already allocated 120% capacity. The agent analyzes alternatives: delaying NeuroStim by 6 weeks would cost $2M in lost revenue but CardioVue has higher strategic priority and competitive urgency. It generates three scenarios: (1) hire contract regulatory consultant for NeuroStim ($150K cost, 3-week delay), (2) delay NeuroStim to Q4 ($2M revenue impact), or (3) accelerate junior regulatory associate development with intensive mentoring (6-month investment, builds capability). The agent schedules portfolio review with executives, pre-populates decision matrices with financial impact analysis, and identifies similar upcoming conflicts across the 18-month planning horizon. It also recommends expanding regulatory affairs capacity as a strategic initiative to prevent recurring bottlenecks.

---

### Use Case 7: Manufacturing Validation & Supply Chain Coordination

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device PMOs coordinate complex manufacturing validation schedules (IQ/OQ/PQ) across multiple production sites while managing supplier qualification timelines for critical components. Process validation sequences require precise coordination between quality, manufacturing, and supplier teams, with any failures creating significant launch delays. Supply chain disruptions frequently impact validation schedules, requiring rapid resequencing of activities across multiple products. PMOs spend enormous effort manually tracking supplier qualification status, validation protocol execution, and manufacturing readiness across their portfolio.

#### The Solution
monday.com orchestrates manufacturing validation with automated protocol scheduling, supplier qualification tracking, and cross-site coordination capabilities. Custom workflows manage IQ/OQ/PQ sequences with dependency tracking and failure recovery procedures. Real-time dashboards provide visibility into manufacturing readiness across all products and sites. Integration with supplier management systems enables proactive supply chain risk management and validation impact assessment.

#### The Outcome
- 40% reduction in manufacturing validation timeline variability
- 60% decrease in validation protocol failures and rework
- $1-3M cost savings per product through optimized validation sequencing
- 70% less time spent coordinating validation activities across sites and suppliers

#### Discovery Questions
- "How many manufacturing sites are you currently validating processes across, and what's your typical IQ/OQ/PQ timeline?"
- "When a supplier qualification fails or gets delayed, how quickly can you assess impact across your validation schedule?"
- "What percentage of your process validation protocols require repeat execution, and what are the common failure modes?"
- "How do you currently coordinate validation activities between your direct manufacturing and contract manufacturer sites?"
- "What visibility do you have into supplier qualification timelines for critical components across your product portfolio?"

#### Industry Context
Manufacturing validation is a critical FDA requirement that ensures production processes can consistently manufacture devices meeting all specifications. IQ/OQ/PQ validation sequences must be completed in order, with Installation Qualification verifying equipment setup, Operational Qualification confirming process parameters, and Performance Qualification demonstrating consistent output quality. Supplier qualification is equally critical, as medical device regulations require validated suppliers for all components affecting device safety and performance. Any validation failures trigger CAPA requirements and can delay commercial production approval.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Manufacturing Validation & Supply Chain Coordination system with these columns: Product Name (text), Manufacturing Site (dropdown: Site A, Site B, Site C, Contract Manufacturer), Validation Phase (dropdown: Pre-Validation, IQ, OQ, PQ, Complete), Validation Status (status: Planning, In Progress, On Hold, Passed, Failed, Rework Required), Quality Lead (people), Manufacturing Lead (people), Supplier Lead (people), Critical Suppliers (text), Supplier Qualification Status (status), IQ Completion Date (date), OQ Completion Date (date), PQ Completion Date (date), Validation Budget (numbers), Protocol Failures (numbers), Commercial Ready Date (date), Risk Assessment (dropdown: Low, Medium, High, Critical), and Validation Notes (long text). Add automations: notify when validation protocols fail and require rework, escalate when supplier qualifications are delayed, alert when commercial ready dates are at risk, and coordinate cross-site validation scheduling. Include timeline view showing validation milestones across all products and dashboard with manufacturing readiness metrics by site."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Manufacturing Validation Coordinator

**Agent Purpose:**  
Autonomously coordinates manufacturing validation activities, monitors supplier qualification progress, and optimizes production readiness across multiple sites.

**Triggers:**
- Design transfer milestone completed for new product
- Manufacturing validation protocol scheduled
- Supplier qualification status change
- Process validation batch results available
- Equipment qualification failure detected

**Actions:**
- Generate validation protocol scheduling with cross-site resource optimization
- Coordinate supplier qualification timelines with validation dependencies
- Create validation failure recovery workflows with root cause analysis
- Update commercial production forecasts based on validation progress
- Generate supplier risk assessments with alternative sourcing recommendations
- Create cross-site validation best practice sharing when protocols succeed

**Data Required:**
- Manufacturing site capabilities and validation capacity
- Supplier qualification requirements and performance history
- Historical validation performance data and failure modes
- Equipment qualification status and maintenance schedules
- Commercial production volume forecasts and capacity requirements

**Autonomy Level:** Human-in-the-Loop  
Agent autonomously coordinates routine validation activities and supplier management but requires quality and manufacturing approval for protocol modifications, supplier changes, or production authorization decisions.

**Example Interaction:**
> The Manufacturing Validation Coordinator detects that FlexiStent's PQ validation at Contract Manufacturer Site C just failed due to dimensional variations exceeding specifications. The agent immediately creates failure investigation workflows, analyzes the root cause (tooling wear beyond tolerance), and generates recovery options: (1) retool and revalidate in 4 weeks ($75K cost), (2) transfer to Site A with 6-week timeline ($125K cost), or (3) modify design tolerance if clinically acceptable (2-week design review required). It schedules emergency cross-functional review, calculates commercial impact ($3M revenue at risk if 6-week delay), and explores expedited tooling options. The agent also identifies that the same tooling issue could affect two other products scheduled for validation next month, creating proactive mitigation workflows to prevent cascade failures. It coordinates with supplier management to implement tooling maintenance protocols and updates validation risk assessments across the portfolio.

---

## Industry Terminology
| Term | Definition |
|------|------------|
| **510(k) Clearance** | FDA premarket notification demonstrating substantial equivalence to predicate device |
| **PMA (Premarket Approval)** | FDA's most stringent premarket review for highest-risk (Class III) medical devices |
| **CE Marking** | European conformity marking indicating compliance with EU Medical Device Regulation |
| **Design Controls** | FDA quality system regulation (21 CFR Part 820.30) governing medical device development |
| **DHF (Design History File)** | Complete documentation of device design including inputs, outputs, reviews, and validation |
| **DMR (Device Master Record)** | Compilation of records containing procedures and specifications for finished device |
| **IQ/OQ/PQ** | Installation/Operational/Performance Qualification - manufacturing validation sequence |
| **V&V (Verification & Validation)** | Confirmation that design meets specifications (V) and user needs (V) |
| **MDR (Medical Device Reporting)** | FDA adverse event reporting system for device-related incidents |
| **CAPA** | Corrective and Preventive Action - systematic approach to address quality issues |
| **Stage-Gate Process** | Structured NPD methodology with go/no-go decision points at each development phase |
| **Design Transfer** | Process of transferring device design from R&D to manufacturing |
| **Predicate Device** | Legally marketed device used as comparison basis for 510(k) substantial equivalence |
| **Clinical Investigation** | Systematic study of device safety and effectiveness in human subjects |

## Typical Stakeholder Roles
| Role | Responsibility | Influence |
|------|----------------|-----------|
| **PMO Director** | Portfolio strategy, resource allocation, executive reporting | High - Budget and priority decisions |
| **Project Manager** | Day-to-day project execution, cross-functional coordination | Medium - Tactical execution authority |
| **Regulatory Affairs Manager** | FDA/international submission strategy, compliance oversight | High - Launch timeline gatekeeper |
| **R&D Director** | Technical development leadership, design control oversight | High - Product feasibility and timeline |
| **Clinical Affairs Manager** | Clinical study design, investigator relations, data management | Medium - Clinical timeline control |
| **Quality Assurance Manager** | Design control compliance, validation oversight, CAPA management | High - Commercial approval authority |
| **Manufacturing Director** | Production planning, validation execution, cost optimization | Medium - Commercial production readiness |

## Adjacent Departments
| Department | Connection | Opportunity |
|------------|-------------|-------------|
| **Regulatory Affairs** | PMO coordinates submission timelines and regulatory milestones | Unified regulatory tracking across portfolio with automated deadline management |
| **Clinical Operations** | PMO oversees clinical trial project management and enrollment | Centralized clinical trial oversight with site performance optimization |
| **Quality Assurance** | PMO manages design control compliance and CAPA projects | Integrated quality management with automated workflow coordination |
| **Manufacturing** | PMO coordinates validation schedules and production readiness | Manufacturing validation orchestration with supplier qualification tracking |
| **Commercial** | PMO provides launch timeline visibility and market readiness | Commercial planning integration with real-time development milestone updates |
| **Finance** | PMO reports on development spend and resource utilization | Portfolio financial management with resource allocation optimization |

## Competitive Landscape
| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Microsoft Project** | "Legacy project management tool that doesn't understand medical device complexity" | Replace with medical device-specific templates, automated regulatory tracking, and AI-powered optimization |
| **Smartsheet** | "Spreadsheet-based solution that breaks down with regulatory complexity" | Consolidate with purpose-built medical device workflows and compliance automation |
| **Veeva Vault** | "Document management focused, lacks project orchestration capabilities" | Complement or replace with integrated project management plus document control |
| **MasterControl** | "Quality system focused, limited portfolio visibility and resource management" | Expand beyond quality to full portfolio management with resource optimization |
| **Clarity PPM** | "IT project focus, lacks medical device industry expertise" | Replace with medical device-specific portfolio management and regulatory intelligence |
| **Oracle Primavera** | "Engineering project tool, overwhelming complexity for most medical device PMOs" | Simplify with intuitive medical device project management and automated coordination |

## Objection Handling
| Objection | Response |
|-----------|----------|
| **"We're already invested in MS Project/Smartsheet"** | "Those tools were built for generic project management. Medical device PMOs need regulatory timeline management, design control tracking, and clinical trial coordination. How much time does your team spend manually managing these complexities across disconnected systems?" |
| **"Our regulatory team uses specialized tools like Veeva Vault"** | "monday.com integrates with your existing regulatory systems while providing PMO-level visibility and coordination. We're not replacing your regulatory tools - we're orchestrating them for better project outcomes." |
| **"Medical device projects are too complex for standard PM tools"** | "Exactly why we've built medical device-specific templates with stage-gate workflows, design control tracking, and regulatory submission management. Plus AI agents that understand 510(k) timelines and clinical trial coordination." |
| **"We need audit-ready documentation and compliance"** | "monday.com provides enterprise-grade audit trails, role-based permissions, and compliance documentation. Our medical device customers regularly pass FDA inspections using our platform for project documentation." |
| **"What about data security and HIPAA compliance?"** | "We're SOC2 Type II certified with enterprise security controls. For clinical data, we integrate with your existing EDC systems rather than storing PHI directly. Many Fortune 500 medical device companies trust us with their most sensitive projects." |

## Proof Points
*(To be populated with customer references)*
- Fortune 500 medical device manufacturer reduced NPD cycle time by 35% using monday.com stage-gate orchestration
- Mid-market orthopedic company accelerated 510(k) submissions by 60 days through automated regulatory timeline management  
- Global cardiac device leader consolidated 12 project management tools into unified monday.com platform
- Class III device manufacturer improved clinical trial enrollment predictability by 50% with centralized trial management
- Medical technology PMO achieved 40% resource utilization improvement through AI-powered portfolio optimization
- Surgical device company reduced design transfer timeline variability by 45% using automated validation coordination

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*