# Medical Devices & Equipment × Customer Success Playbook

## Overview

Customer Success in the medical devices industry operates at the intersection of complex clinical environments, stringent regulatory requirements, and life-critical technology. CS teams typically manage relationships across hospital systems, IDNs (Integrated Delivery Networks), GPOs (Group Purchasing Organizations), and individual facilities ranging from 100-bed community hospitals to 1,000+ bed academic medical centers. Unlike traditional SaaS customer success, medical device CS teams must coordinate clinical specialist support, manage surgeon onboarding programs, oversee device utilization tracking, handle FDA-mandated complaint processes (21 CFR 803), and maintain post-market surveillance feedback loops.

The department structure often includes Customer Success Managers focused on strategic accounts, Clinical Specialists providing training and technical support, Field Service Engineers managing maintenance schedules, and Complaint Coordinators ensuring regulatory compliance. Teams are measured on device utilization rates, NPS scores by account and product line, contract renewal rates for service agreements, time-to-proficiency for new surgeons, and clinical outcome improvements. The regulatory environment demands meticulous documentation, with every customer interaction, training session, and complaint requiring detailed records that can withstand FDA audits.

Customer Success teams coordinate closely with R&D for product feedback, Sales for competitive displacement defense, and Field Service for preventive maintenance scheduling. They manage complex logistics including loaner programs, consignment inventory, and upgrade path management while navigating Value Analysis Committees (VACs) that scrutinize every device purchase decision based on clinical evidence and economic outcomes.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|-------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | High | Clinical specialists and customer success managers are expensive, specialized resources. AI agents can handle routine patient inquiries, schedule maintenance, track utilization, and manage compliance documentation 24/7 |
| **Consolidate Tech Stack with AI** | High | Medical device companies typically juggle 8-12 disconnected systems: CRM, complaint management, training platforms, field service tools, regulatory databases, and clinical data systems. Single AI platform eliminates integration nightmares |
| **Scale Impact Without Overhead** | Very High | As device portfolios expand and hospital networks consolidate, CS teams need to manage more accounts without proportional headcount growth. AI enables one CSM to effectively manage 3x more accounts |

## Prioritized Use Cases

---

### Use Case 1: Intelligent Complaint Management & 21 CFR 803 Compliance

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device complaint handling requires complex workflows involving clinical evaluation, regulatory assessment, trending analysis, and potential FDA reporting within strict timelines. Each complaint costs $2,000-5,000 in labor to process properly, with serious events requiring immediate escalation. Manual processes lead to missed deadlines, incomplete investigations, and compliance risks that can trigger FDA Warning Letters.

#### The Solution
monday.com's AI agents automatically classify complaints by severity, route to appropriate specialists, track investigation timelines, and generate regulatory reports. The AI analyzes complaint patterns across product lines and facilities, identifying trends before they become systemic issues. Automated workflows ensure 21 CFR 803 deadlines are met while reducing manual processing time by 80%.

#### The Outcome
Reduce complaint processing costs from $4,000 to $800 per case. Eliminate missed FDA reporting deadlines. Identify product issues 60 days earlier through pattern analysis. Free up clinical specialists to focus on complex cases requiring human expertise.

#### Discovery Questions
- How many complaints do you process monthly across your product portfolio?
- What's your average time to complete a complaint investigation?
- Have you ever missed an FDA reporting deadline, and what were the consequences?
- How do you currently identify trends across multiple complaints?
- What percentage of your clinical specialists' time is spent on routine complaint documentation?

#### Industry Context
Medical device complaints range from minor usability issues to serious adverse events requiring immediate FDA notification. The 21 CFR 803 regulation mandates specific reporting timelines (24 hours for deaths, 10 days for serious injuries). Complaint coordinators must have clinical expertise to properly classify events, making this role both expensive and difficult to scale.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a medical device complaint management board with these columns: Complaint ID (text), Date Received (date), Product Line (dropdown: Surgical Robotics, Imaging Systems, Patient Monitors, Implantable Devices), Facility Name (text), Reporter Type (dropdown: Healthcare Professional, Patient, Manufacturer Employee), Event Description (long text), Severity Classification (status: Minor, Moderate, Serious, Death), FDA Reporting Required (checkbox), Investigation Status (status: New, In Progress, Clinical Review, Regulatory Review, Complete), Assigned Specialist (people), Investigation Due Date (date), Root Cause (long text), Corrective Action (long text). Add automation to notify FDA Compliance team when severity is 'Death' or 'Serious'. Create a dashboard view showing overdue investigations and complaint trends by product line."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Complaint Classification & Compliance Agent

**Agent Purpose:**  
Automatically processes medical device complaints, ensures regulatory compliance, and identifies safety trends.

**Triggers:**
- New complaint submission via form or email
- Investigation deadline approaching (3-day warning)
- Similar complaints reaching threshold (3 similar events in 30 days)
- Status change requiring regulatory review
- External data updates from field service or clinical teams

**Actions:**
- Auto-classify complaint severity based on clinical keywords and patterns
- Route to appropriate clinical specialist based on product expertise
- Generate draft FDA report if reportable event identified
- Send compliance notifications with specific deadlines
- Flag potential trends by analyzing complaint descriptions across product lines
- Update investigation status based on specialist input

**Data Required:**
- Product specifications and clinical indications
- Historical complaint database for pattern recognition
- Specialist expertise mapping by product line
- FDA reporting requirements and templates
- Customer facility information and contacts

**Autonomy Level:** Human-in-the-Loop
Agent handles initial classification and routing, but all regulatory reports and serious event determinations require clinical specialist approval before submission.

**Example Interaction:**
> A complaint form is submitted reporting that a surgical robot "jerked unexpectedly during a procedure, requiring conversion to open surgery." The agent immediately flags this as a "Serious" event requiring FDA reporting, assigns it to the robotics clinical specialist, sets a 24-hour notification deadline, and generates a draft MedWatch report. It also searches for similar "unexpected movement" complaints in the past 90 days, finding two related incidents at different facilities. The agent creates a trend analysis alert and notifies the robotics engineering team about potential systematic issues, all while ensuring the clinical specialist has everything needed to complete the regulatory filing on time.

---

### Use Case 2: Surgeon Onboarding & Clinical Competency Tracking

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
New surgeon onboarding for complex medical devices requires extensive training, credentialing, and competency verification. Each surgeon typically needs 10-20 hours of hands-on training, proctored cases, and ongoing competency assessments. Manual tracking of training progress, certification renewals, and clinical outcomes across hundreds of surgeons leads to compliance gaps, delayed go-lives, and inconsistent skill development.

#### The Solution
AI-powered training orchestration automatically schedules training sessions based on surgeon availability and device demand, tracks competency milestones, and analyzes clinical outcomes by surgeon to identify additional support needs. The platform integrates with hospital credentialing systems and automatically triggers refresher training when competency metrics decline.

#### The Outcome
Reduce surgeon time-to-competency from 90 days to 45 days. Increase training completion rates from 70% to 95%. Identify struggling surgeons 30 days earlier through outcome analysis. Scale onboarding capacity 3x without adding clinical specialists.

#### Discovery Questions
- How many new surgeons do you onboard annually across your device portfolio?
- What's your current time from initial training to independent procedure completion?
- How do you track ongoing competency and identify surgeons needing additional support?
- What percentage of trained surgeons are actively using your devices 12 months post-training?
- How do you correlate surgeon experience levels with clinical outcomes?

#### Industry Context
Surgeon adoption directly impacts device utilization and clinical outcomes. Hospital credentialing committees require documented competency before allowing independent device use. Training typically involves didactic sessions, hands-on lab time, and proctored live cases. Ongoing competency requirements vary by device complexity and institutional policies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a surgeon onboarding tracking board with columns: Surgeon Name (people), Hospital System (text), Specialty (dropdown: Cardiac Surgery, Orthopedics, Neurosurgery, General Surgery), Device Platform (dropdown: Surgical Robot, Imaging System, Ablation Device, Implant System), Training Status (status: Not Started, Didactic Complete, Lab Training, Proctored Cases, Certified, Refresher Needed), Certification Date (date), Certification Expires (date), Procedures Completed (numbers), Clinical Specialist Assigned (people), Competency Score (rating 1-5), Next Milestone (text), Training Hours Logged (numbers). Add automation to notify clinical specialist when certification expires in 30 days. Create timeline view showing training schedules and Kanban view for tracking surgeon pipeline by status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Surgeon Competency & Training Orchestration Agent

**Agent Purpose:**  
Automatically manages surgeon training programs and monitors ongoing clinical competency across device platforms.

**Triggers:**
- New surgeon registration for training program
- Training milestone completion
- Certification approaching expiration (30-day window)
- Clinical outcome data suggesting competency gap
- New device launch requiring existing surgeon certification

**Actions:**
- Schedule optimal training sessions based on surgeon calendar and lab availability
- Send personalized training reminders and prep materials
- Track competency progression and identify at-risk surgeons
- Generate competency reports for hospital credentialing committees
- Recommend refresher training based on outcome analysis
- Coordinate with clinical specialists for personalized support plans

**Data Required:**
- Surgeon profiles, specialties, and hospital affiliations
- Training curriculum requirements by device platform
- Clinical specialist availability and expertise mapping
- Procedure outcome data and quality metrics
- Hospital credentialing requirements and schedules

**Autonomy Level:** Fully Autonomous
Agent handles all scheduling, tracking, and reporting functions. Only escalates to humans when competency concerns are identified or special accommodations needed.

**Example Interaction:**
> Dr. Sarah Chen completes her robotic surgery lab training. The agent automatically updates her status to "Proctored Cases" and schedules her first proctored procedure based on her OR availability and clinical specialist coverage. It sends her personalized prep materials and case selection guidelines. After her third proctored case, the agent analyzes her procedural metrics against certification standards, determines she's ready for independent certification, and generates the competency report for the hospital's credentialing committee. It then schedules her 6-month follow-up assessment and sets up automated tracking of her first 20 independent cases to ensure continued competency.

---

### Use Case 3: Preventive Maintenance & Field Service Optimization

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device preventive maintenance requires complex scheduling across thousands of devices, coordinating field service engineers with hospital downtime windows while ensuring regulatory compliance and minimizing clinical disruption. Manual scheduling leads to emergency breakdowns, compliance violations, and field engineer utilization rates below 60%. Each unplanned service call costs 3x more than preventive maintenance.

#### The Solution
AI-powered maintenance orchestration predicts optimal service windows, automatically schedules preventive maintenance based on device usage patterns and hospital availability, and proactively identifies devices showing early failure indicators. The system optimizes field engineer routes and schedules to maximize utilization while ensuring compliance deadlines are met.

#### The Outcome
Increase field engineer utilization from 60% to 85%. Reduce emergency service calls by 40%. Achieve 99.5% preventive maintenance compliance. Cut service coordination overhead from 20 hours to 2 hours per week per service manager.

#### Discovery Questions
- How many medical devices do you have under service contracts across your territory?
- What's your current preventive maintenance compliance rate?
- How much advance notice do hospitals typically require for scheduled maintenance?
- What percentage of your service calls are emergency vs. planned maintenance?
- How do you currently optimize field engineer routes and schedules?

#### Industry Context
Medical devices require FDA-mandated preventive maintenance schedules to maintain safety and efficacy. Hospitals operate 24/7 with limited maintenance windows, typically during off-peak hours or planned downtime. Field service engineers are expensive, specialized resources requiring extensive training on complex medical equipment. Service contract compliance directly impacts customer satisfaction and renewal rates.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a preventive maintenance tracking board with columns: Device Serial Number (text), Hospital Name (text), Device Type (dropdown: MRI, CT Scanner, Surgical Robot, Patient Monitor, Ventilator), Last Service Date (date), Next Service Due (date), Service Interval (dropdown: 3 Month, 6 Month, Annual), Field Engineer (people), Service Status (status: Scheduled, In Progress, Complete, Overdue), Hospital Contact (text), Preferred Maintenance Window (text), Service Hours Required (numbers), Parts Required (long text), Compliance Status (status: Compliant, Warning, Overdue). Add automation to notify field engineer 14 days before service due date and escalate to service manager if overdue. Create calendar view for service scheduling and dashboard showing compliance rates by region."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Predictive Maintenance Orchestration Agent

**Agent Purpose:**  
Automatically schedules optimal maintenance windows and predicts equipment failures before they occur.

**Triggers:**
- Preventive maintenance due date approaching (30-day window)
- Device usage patterns indicating accelerated wear
- Environmental conditions affecting equipment performance
- Hospital maintenance window availability changes
- Field engineer schedule updates or availability changes

**Actions:**
- Analyze hospital schedules to identify optimal maintenance windows
- Auto-schedule preventive maintenance with hospital and field engineer coordination
- Predict equipment failures based on usage patterns and historical data
- Optimize field engineer routes for maximum efficiency
- Generate compliance reports and audit trails
- Escalate high-priority maintenance needs to service managers

**Data Required:**
- Device installation database with service history
- Hospital operational schedules and maintenance preferences  
- Field engineer locations, schedules, and expertise areas
- Device usage data and performance metrics
- Environmental monitoring data (temperature, humidity, power quality)

**Autonomy Level:** Fully Autonomous
Agent handles all routine scheduling and optimization. Only escalates when conflicts cannot be resolved or emergency situations arise.

**Example Interaction:**
> The agent detects that an MRI scanner at Regional Medical Center is showing increased helium consumption patterns, suggesting an impending quench risk. It immediately schedules an emergency service call, coordinates with the hospital's MRI manager to minimize scan disruptions, and dispatches the nearest qualified field engineer with appropriate replacement parts. Simultaneously, it reschedules three non-urgent maintenance appointments to accommodate the emergency call while ensuring compliance deadlines are still met. The agent generates an incident report and notifies the engineering team about the failure pattern for product improvement considerations.

---

### Use Case 4: Customer Health Scoring & Expansion Orchestration

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device Customer Success teams struggle to identify at-risk accounts and expansion opportunities across complex hospital systems with multiple decision-makers and lengthy procurement cycles. Manual account reviews consume 40% of CSM time while missing early warning signs of churn or competitive displacement. Value Analysis Committees require extensive clinical and economic data that's difficult to compile across disparate systems.

#### The Solution
AI-powered customer health scoring analyzes device utilization data, support ticket trends, training completion rates, and clinical outcomes to predict account risk and expansion readiness. The system automatically generates VAC-ready business cases with clinical evidence and economic justification, while identifying key stakeholders and optimal engagement timing.

#### The Outcome
Increase CSM capacity to manage 3x more accounts effectively. Improve expansion win rates from 25% to 45% through better timing and stakeholder targeting. Reduce churn by 60% through early intervention. Generate VAC-ready business cases in 2 hours vs. 2 weeks.

#### Discovery Questions
- How do your CSMs currently prioritize which accounts to focus on each quarter?
- What early indicators do you track that suggest an account might be at risk?
- How long does it typically take to prepare a business case for a Value Analysis Committee?
- What's your current expansion win rate when presenting new products to existing customers?
- How do you identify the right stakeholders for expansion opportunities in complex hospital systems?

#### Industry Context
Hospital purchasing decisions involve multiple stakeholders including clinicians, administrators, and Value Analysis Committees that scrutinize clinical evidence and economic outcomes. IDN relationships can span dozens of facilities with complex procurement processes. Device utilization rates directly correlate with customer satisfaction and expansion opportunities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a customer health scoring board with columns: Account Name (text), Health Score (rating 1-10), Risk Level (status: Green, Yellow, Red), Device Utilization Rate (numbers), Support Tickets (numbers), Training Completion % (numbers), NPS Score (numbers), Contract Renewal Date (date), Expansion Opportunity (dropdown: High, Medium, Low, None), CSM Assigned (people), Last Interaction Date (date), Next Touch Point (date), Key Stakeholder (text), VAC Presentation Status (status: Not Planned, In Preparation, Scheduled, Complete), Revenue at Risk ($), Expansion Potential ($). Add automation to notify CSM when health score drops below 6 or expansion opportunity reaches 'High' status. Create dashboard showing portfolio health overview and timeline view for scheduled interactions."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Customer Health & Expansion Intelligence Agent

**Agent Purpose:**  
Continuously monitors customer health indicators and identifies optimal expansion opportunities with automated business case generation.

**Triggers:**
- Monthly customer health score recalculation
- Device utilization dropping below threshold
- Support ticket volume spike detected
- Training completion rates declining
- Competitive intelligence indicating threat
- New product launch creating expansion opportunity

**Actions:**
- Calculate comprehensive health scores using multiple data sources
- Generate early warning alerts for at-risk accounts
- Identify expansion-ready accounts based on utilization and satisfaction metrics
- Auto-generate VAC presentation materials with clinical evidence
- Recommend optimal engagement strategies based on stakeholder analysis
- Create account review summaries with actionable insights

**Data Required:**
- Device utilization and performance metrics
- Support ticket history and resolution times
- Training records and competency assessments
- Customer survey responses and NPS data
- Competitive intelligence and market trends
- Hospital system organizational charts and decision-maker profiles

**Autonomy Level:** Human-in-the-Loop
Agent provides insights and recommendations, but CSMs make final decisions on account strategies and stakeholder engagement approaches.

**Example Interaction:**
> The agent identifies that St. Mary's Health System shows declining robotic surgery utilization (60% vs. 85% baseline) combined with increased support tickets related to surgeon scheduling conflicts. It flags this as a "Yellow" health risk and recommends immediate CSM intervention. Simultaneously, it notices their cardiac surgery department has high NPS scores and recently hired two new surgeons, creating an expansion opportunity for cardiac-specific robotic platforms. The agent generates a preliminary business case showing potential ROI based on their current case volumes and automatically schedules a stakeholder analysis to identify the optimal presentation strategy for their VAC.

---

### Use Case 5: Post-Market Surveillance & Clinical Outcome Tracking

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Medical device companies must maintain comprehensive post-market surveillance to monitor real-world device performance and clinical outcomes for regulatory compliance and product improvement. Data collection spans multiple sources including EMRs, device logs, patient registries, and clinical reports. Manual aggregation and analysis of this data is resource-intensive and often incomplete, missing critical safety signals or improvement opportunities.

#### The Solution
AI-powered surveillance platform automatically aggregates data from multiple sources, identifies adverse trend patterns, and generates regulatory reports. The system correlates device performance with clinical outcomes, automatically flagging potential safety issues and generating insights for product development teams. Integration with EMR systems provides real-world evidence for regulatory submissions and competitive positioning.

#### The Outcome
Reduce post-market surveillance workload by 70%. Identify safety signals 45 days earlier through automated pattern recognition. Generate real-world evidence reports 5x faster for regulatory submissions. Improve product development feedback loop with quantified clinical outcome data.

#### Discovery Questions
- How do you currently collect and analyze post-market clinical outcome data?
- What challenges do you face in accessing real-world evidence from hospital systems?
- How quickly can you identify and investigate potential safety signals across your device portfolio?
- What percentage of your regulatory submissions include real-world evidence data?
- How do you correlate device performance metrics with patient clinical outcomes?

#### Industry Context
FDA requires ongoing post-market surveillance for many medical devices to monitor safety and effectiveness in real-world use. Real-world evidence is increasingly important for regulatory submissions and competitive differentiation. Clinical outcome tracking helps demonstrate value to healthcare providers and supports reimbursement discussions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a post-market surveillance tracking board with columns: Study ID (text), Device Model (dropdown: Robot System A, Imaging Platform B, Monitor Series C), Clinical Indication (text), Number of Patients (numbers), Participating Sites (numbers), Study Status (status: Planning, Active, Analysis, Complete), Primary Endpoint (text), Safety Signal Detected (checkbox), Outcome Metric (numbers), Statistical Significance (dropdown: Significant, Not Significant, Pending), Regulatory Impact (dropdown: None, Label Update, Safety Communication, Recall), Principal Investigator (text), Data Collection % (numbers), Last Update Date (date). Add automation to notify regulatory team when safety signal is detected. Create dashboard showing study portfolio status and timeline view for regulatory milestones."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Post-Market Surveillance & Safety Intelligence Agent

**Agent Purpose:**  
Continuously monitors real-world device performance and automatically detects safety signals requiring regulatory action.

**Triggers:**
- New clinical outcome data uploaded from participating sites
- Device performance metrics exceeding predefined thresholds
- Adverse event reports requiring correlation analysis
- Regulatory milestone deadlines approaching
- Competitive device safety communications published

**Actions:**
- Aggregate and analyze multi-source clinical data
- Detect statistical anomalies indicating potential safety signals
- Generate automated safety signal reports for regulatory review
- Correlate device performance with patient outcomes
- Create real-world evidence summaries for regulatory submissions
- Alert clinical and regulatory teams to significant findings

**Data Required:**
- Device performance logs and utilization metrics
- EMR data feeds from participating hospitals
- Adverse event databases and complaint systems
- Clinical outcome registries and databases
- Regulatory reporting templates and requirements
- Competitive intelligence and benchmark data

**Autonomy Level:** Escalation-Based
Agent handles routine data analysis and pattern detection autonomously, but escalates all potential safety signals to clinical and regulatory experts for human review before any regulatory actions.

**Example Interaction:**
> The agent analyzes 6 months of surgical robot performance data from 200+ procedures across 15 hospitals and detects a 12% increase in conversion-to-open rates for a specific procedure type compared to the previous year. Cross-referencing with surgeon experience data, it identifies that this trend is isolated to surgeons with <50 procedures of experience on the platform. The agent generates a detailed analysis report showing the correlation and recommends enhanced training protocols for new users rather than a safety communication. It automatically schedules a review with the clinical affairs team and updates the post-market surveillance dashboard with findings and recommended actions.

---

### Use Case 6: GPO/IDN Relationship Management & Contract Optimization

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Managing relationships with Group Purchasing Organizations (GPOs) and Integrated Delivery Networks (IDNs) requires tracking complex contract terms, compliance requirements, and utilization commitments across hundreds of facilities. Manual contract management leads to missed rebate opportunities, compliance violations, and suboptimal contract renewals. Each GPO relationship can impact 500+ facilities with varying implementation timelines and success metrics.

#### The Solution
AI-powered GPO/IDN management platform automatically tracks contract performance, identifies utilization gaps, and optimizes pricing strategies based on competitive intelligence and market dynamics. The system provides early warnings for contract renewals, automatically calculates rebate opportunities, and generates facility-specific implementation plans for maximum penetration.

#### The Outcome
Increase contract compliance rates from 75% to 95%. Identify $2M+ in missed rebate opportunities annually. Reduce contract management overhead by 60%. Improve GPO contract renewal win rates through data-driven negotiations.

#### Discovery Questions
- How many GPO and IDN contracts do you currently manage across your portfolio?
- What's your typical contract compliance rate, and how do you track utilization commitments?
- How do you identify facilities within GPO networks that aren't meeting volume commitments?
- What percentage of available rebates do you currently capture across your contracts?
- How far in advance do you begin contract renewal preparations, and what data drives your strategy?

#### Industry Context
GPOs negotiate contracts on behalf of member hospitals to achieve volume discounts and standardization. IDNs are hospital networks that may have their own purchasing agreements. Contract terms often include volume commitments, market share requirements, and performance rebates. Successful GPO relationships can provide access to thousands of facilities but require dedicated management resources.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a GPO/IDN contract management board with columns: Organization Name (text), Contract Type (dropdown: GPO Primary, GPO Secondary, IDN Direct, Regional Network), Contract Start (date), Contract End (date), Portfolio Coverage (dropdown: Full Line, Surgical, Imaging, Critical Care), Volume Commitment ($), YTD Performance ($), Compliance % (numbers), Member Facilities (numbers), Penetrated Facilities (numbers), Rebate Tier (dropdown: Tier 1, Tier 2, Tier 3, None), Rebate Earned ($), Account Manager (people), Renewal Status (status: Secure, At Risk, Negotiating, Lost), Contract Value ($), Next Review Date (date). Add automation to notify account manager when compliance drops below 80% or contract renewal is due in 6 months. Create dashboard showing portfolio performance and map view of facility penetration by region."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** GPO Contract Intelligence & Optimization Agent

**Agent Purpose:**  
Maximizes GPO contract value through automated compliance monitoring and strategic renewal optimization.

**Triggers:**
- Monthly contract performance data updates
- Facility utilization dropping below commitment thresholds
- Contract renewal date approaching (12-month window)
- Competitive contract awards affecting market position
- New facility additions to GPO networks

**Actions:**
- Monitor real-time contract compliance across all GPO relationships
- Identify underperforming facilities and generate intervention strategies
- Calculate rebate opportunities and optimize pricing strategies
- Generate contract renewal recommendations based on market intelligence
- Create facility-specific penetration plans for maximum utilization
- Alert account managers to compliance risks and renewal opportunities

**Data Required:**
- GPO contract terms and performance metrics
- Facility-level purchase data and utilization trends
- Competitive pricing intelligence and market share data
- GPO member facility databases and contact information
- Historical contract negotiation outcomes and strategies
- Market access requirements and regulatory considerations

**Autonomy Level:** Human-in-the-Loop
Agent provides comprehensive analysis and recommendations, but account managers make final decisions on contract strategies and facility engagement approaches.

**Example Interaction:**
> The agent detects that Premier GPO contract performance is at 78% of volume commitment with 4 months remaining in the contract year, putting $500K in rebates at risk. It analyzes member facility data and identifies 12 facilities with low utilization that could bridge the gap. The agent generates facility-specific action plans, including optimal product mix recommendations and pricing strategies, then automatically schedules review meetings with the account team. It also begins contract renewal analysis, comparing current terms with competitive intelligence to recommend negotiation strategies for the upcoming renewal cycle.

---

### Use Case 7: Competitive Displacement Defense & Win-Back Campaigns

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device companies face constant competitive threats as hospitals evaluate alternatives during contract renewals or technology refreshes. Manual competitive intelligence gathering is incomplete and reactive, often missing early warning signs until opportunities are already lost. Win-back campaigns require extensive clinical and economic data compilation that typically takes weeks to develop, often too late to influence decisions.

#### The Solution
AI-powered competitive intelligence platform monitors multiple data sources to identify competitive threats early, automatically generates win-back materials with clinical evidence and ROI calculations, and orchestrates multi-touch campaigns across stakeholders. The system tracks competitive positioning and provides real-time recommendations for defensive strategies.

#### The Outcome
Increase win-back campaign success rates from 15% to 35%. Identify competitive threats 90 days earlier through automated intelligence gathering. Reduce win-back material preparation time from 3 weeks to 2 days. Improve competitive retention rates by 25% through proactive defense strategies.

#### Discovery Questions
- How do you currently identify when customers are evaluating competitive alternatives?
- What's your typical win rate when defending against competitive displacement?
- How long does it take to compile clinical evidence and economic justification for win-back campaigns?
- What percentage of lost accounts do you attempt to win back, and what's your success rate?
- How do you track competitive activity across your customer base?

#### Industry Context
Hospital technology evaluations typically involve 6-18 month cycles with extensive clinical and economic analysis. Value Analysis Committees require comprehensive comparisons including clinical outcomes, training requirements, and total cost of ownership. Competitive displacements can affect entire product portfolios, making early detection and response critical.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a competitive intelligence tracking board with columns: Account Name (text), Competitive Threat (dropdown: Evaluation Phase, RFP Issued, Vendor Finalist, Decision Pending), Competitor (dropdown: Company A, Company B, Company C, Multiple), Product Category (dropdown: Surgical Robotics, Imaging Systems, Patient Monitoring), Risk Level (status: Low, Medium, High, Critical), Threat Source (dropdown: Intelligence Report, Customer Feedback, Sales Team, Industry News), Detection Date (date), Decision Timeline (date), Win-Back Status (status: Not Started, Materials Prep, Campaign Active, Won, Lost), Assigned Team (people), Clinical Champion (text), Economic Justification ($), Campaign ROI (numbers). Add automation to escalate to sales director when risk level reaches 'Critical'. Create dashboard showing threat pipeline and win-back campaign performance metrics."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Competitive Defense & Intelligence Agent

**Agent Purpose:**  
Automatically detects competitive threats and orchestrates data-driven win-back campaigns with personalized stakeholder engagement.

**Triggers:**
- Competitive intelligence reports mentioning customer accounts
- Unusual support ticket patterns suggesting evaluation activities
- Industry publications announcing competitive wins
- Sales team reports of competitive activity
- Customer engagement patterns indicating evaluation phase

**Actions:**
- Monitor multiple intelligence sources for competitive threats
- Generate automated competitive analysis reports
- Compile clinical evidence and economic justification materials
- Orchestrate multi-stakeholder win-back campaigns
- Track campaign effectiveness and optimize messaging strategies
- Provide real-time competitive positioning recommendations

**Data Required:**
- Competitive intelligence databases and industry reports
- Customer account history and relationship mapping
- Clinical outcome data and comparative studies
- Economic analysis templates and ROI models
- Sales team activity reports and customer feedback
- Market research and competitive positioning studies

**Autonomy Level:** Human-in-the-Loop
Agent handles intelligence gathering and material preparation autonomously, but sales teams control stakeholder engagement and campaign execution strategies.

**Example Interaction:**
> The agent detects unusual patterns in support tickets from University Medical Center, including requests for device specifications and outcome data that typically indicate evaluation activities. Cross-referencing with competitive intelligence, it identifies that a major competitor recently announced a similar account win in the same health system. The agent immediately flags this as a "High" risk threat and begins compiling a competitive defense package including clinical outcomes, economic analysis, and training cost comparisons. It identifies key stakeholders from previous interactions and generates personalized talking points for each decision-maker, then alerts the account team with a complete action plan and recommended engagement timeline.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| 21 CFR 803 | FDA regulation requiring medical device adverse event reporting |
| Clinical Specialist | Expert who provides training and technical support for complex medical devices |
| Consignment Management | Inventory system where devices remain manufacturer-owned until used |
| GPO (Group Purchasing Organization) | Entity that negotiates contracts on behalf of member healthcare organizations |
| IDN (Integrated Delivery Network) | Network of hospitals and healthcare providers under unified management |
| In-servicing | Training provided to hospital staff on proper device usage and safety |
| Loaner Program | Temporary device provision during repairs or trial periods |
| NPS (Net Promoter Score) | Customer satisfaction metric tracking likelihood to recommend |
| Post-Market Surveillance | Ongoing monitoring of device safety and effectiveness after market approval |
| Proctored Case | Supervised procedure where experienced specialist oversees skill development |
| Service Agreement | Contract covering maintenance, repairs, and technical support |
| Surgeon Onboarding | Comprehensive training process to certify surgeons on device usage |
| VAC (Value Analysis Committee) | Hospital committee that evaluates technology purchases based on clinical and economic evidence |
| Device Utilization Tracking | Monitoring of how frequently and effectively devices are being used |
| Competitive Displacement Defense | Strategies to retain customers when competitors are being evaluated |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| Chief Medical Officer | Clinical oversight and quality outcomes | High - Sets clinical strategy |
| Value Analysis Committee Chair | Technology evaluation and approval | High - Final purchase decision |
| Department Chief (Surgery/Cardiology/etc.) | Clinical department leadership | High - Product selection influence |
| Biomedical Engineering Director | Technical evaluation and maintenance | Medium - Implementation requirements |
| Supply Chain Director | Contracting and vendor management | Medium - Operational oversight |
| Clinical Nurse Manager | Staff training and workflow integration | Medium - End-user adoption |
| Hospital Administrator | Budget oversight and strategic planning | High - Financial approval |
| Clinical Specialists (Internal) | Device training and competency oversight | Medium - Training effectiveness |
| Purchasing Manager | Contract administration and compliance | Low - Process execution |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| Clinical Affairs | Post-market surveillance and outcome data | Real-world evidence generation and regulatory support |
| Field Service | Maintenance scheduling and device performance | Predictive maintenance and uptime optimization |
| Sales | Account intelligence and competitive positioning | Territory expansion and competitive defense |
| Regulatory Affairs | Compliance monitoring and adverse event reporting | Automated regulatory submissions and audit preparation |
| Training/Education | Surgeon certification and competency programs | Scalable training delivery and outcome tracking |
| R&D/Product Development | Customer feedback and product improvement | Voice of customer analysis and feature prioritization |
| Marketing | Customer testimonials and case study development | Outcome-based marketing content and competitive positioning |
| Quality Assurance | Complaint investigation and corrective actions | Quality management system integration and trend analysis |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|--------------------------|
| Salesforce Health Cloud | "Healthcare CRM" | Limited medical device-specific functionality, lacks regulatory compliance features |
| Veeva CRM | "Life sciences specialist" | Strong for pharma, but limited medical device customer success capabilities |
| Microsoft Dynamics 365 | "Enterprise platform" | Generic solution lacking medical device industry workflows and compliance |
| ServiceNow | "Service management" | Strong for IT, but missing clinical specialist workflows and device-specific features |
| Custom-built solutions | "Tailored for our needs" | High maintenance costs, limited scalability, lacks AI capabilities |
| Excel/SharePoint combinations | "Cost-effective solution" | Manual processes, no automation, compliance risks, doesn't scale |
| Specialized medical device CRM | "Industry-specific" | Usually point solutions lacking integrated customer success workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "Our custom system handles medical device requirements" | "Custom systems require expensive maintenance and lack AI capabilities that can predict device failures and automate compliance reporting. What's your annual IT maintenance budget for custom solutions vs. expanding clinical specialist capacity?" |
| "We already use Salesforce/Veeva" | "Those are excellent sales tools, but medical device customer success requires specialized workflows like 21 CFR 803 compliance, surgeon competency tracking, and preventive maintenance scheduling. How much customization have you needed to handle device-specific processes?" |
| "Our regulatory team handles compliance manually" | "Manual compliance is a significant risk - one missed FDA deadline can result in Warning Letters. Our AI agents ensure 100% compliance while freeing your clinical specialists to focus on complex cases requiring human expertise." |
| "ROI is unclear for customer success technology" | "Medical device CS teams that implement AI-powered workflows typically see 40% reduction in complaint processing costs and 60% improvement in preventive maintenance compliance, directly impacting renewal rates and customer satisfaction scores." |
| "Training requirements seem extensive" | "Our Vibe platform allows you to build device-specific workflows in minutes using natural language - no coding required. Your clinical specialists can create the exact processes they need without IT dependency." |
| "Integration with EMR systems is complex" | "We handle EMR integration through secure APIs, ensuring HIPAA compliance while providing the clinical outcome data you need for post-market surveillance and competitive positioning." |

## Proof Points
*(To be populated with customer references)*

- Large surgical robotics manufacturer reduced complaint processing time by 75% while maintaining 100% FDA reporting compliance
- Multi-billion medical device company increased field service engineer utilization from 58% to 87% through AI-powered maintenance scheduling
- Leading cardiac device manufacturer improved surgeon certification rates by 40% using automated competency tracking
- Global imaging company identified $3.2M in missed GPO rebate opportunities through automated contract compliance monitoring
- Major orthopedic device maker reduced customer churn by 45% through predictive health scoring and proactive intervention
- International patient monitoring company achieved 99.8% preventive maintenance compliance across 5,000+ devices

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*