# Medical Devices & Equipment × Product & R&D Playbook

## Overview

Product & R&D teams in the medical devices industry operate under the most stringent regulatory framework in any vertical, where design controls (21 CFR 820.30) dictate every aspect of product development from concept to commercial release. These teams typically manage complex, multi-year development cycles involving hardware, software (including SaMD - Software as a Medical Device), and combination products, all while adhering to ISO 13485 quality systems and building comprehensive Design History Files (DHF). The department bridges engineering, clinical affairs, regulatory, and quality functions, often managing portfolios ranging from Class I devices requiring minimal regulatory oversight to Class III devices requiring PMA (Premarket Approval) with extensive clinical data.

The organizational structure typically includes design engineers, software developers following IEC 62304 software lifecycle processes, clinical research professionals managing 510(k) submissions and De Novo pathways, regulatory specialists handling technical files for EU MDR compliance, and quality engineers conducting design verification/validation (V&V) activities. Teams must navigate predicate device analysis for 510(k) pathways, conduct FMEA (Failure Mode Effects Analysis) and comprehensive risk management per ISO 14971, and ensure usability engineering compliance with IEC 62366 — all while managing biocompatibility testing protocols per ISO 10993 and preparing for notified body submissions in international markets.

Scale varies dramatically from startup teams of 5-10 people developing single devices to enterprise R&D organizations with hundreds of engineers managing multiple product lines simultaneously. Regardless of size, all teams face the same fundamental challenge: maintaining perfect traceability and documentation while accelerating time-to-market in an increasingly competitive landscape where regulatory delays can cost millions in lost revenue and competitive positioning.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|-------------|-----------|-----------------|
| **Replace or Radically Augment Headcount** | **HIGH** | Regulatory documentation, DHF maintenance, and V&V execution are resource-intensive but perfect for AI automation. A single AI agent can replace 2-3 FTEs in documentation roles. |
| **Consolidate Tech Stack with AI** | **HIGH** | Teams typically juggle 8-15 disconnected tools (PLM, EQMS, clinical data systems, regulatory databases). AI consolidation eliminates integration overhead and data silos. |
| **Scale Impact Without Overhead** | **MEDIUM** | While headcount scaling matters, the bigger win is accelerating regulatory timelines and reducing compliance risk through AI-powered process optimization. |

## Prioritized Use Cases

---

### Use Case 1: Intelligent Design History File (DHF) Management

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
DHF compilation for FDA submissions requires tracking hundreds of design inputs/outputs, verification/validation protocols, design reviews, and design transfer documentation across multiple product variants. Teams spend 40-60 hours per device manually assembling DHFs, with high risk of missing critical traceability links that can delay FDA approval by 6-12 months. A single missing V&V report or incorrect design control reference can trigger a Complete Response Letter, costing $2-5M in delays.

#### The Solution
monday.com Work Management with custom boards for design control traceability, automated DHF compilation workflows via Vibe-built applications, and AI agents that continuously validate completeness against 21 CFR 820.30 requirements. Sidekick AI reviews all documentation for regulatory compliance gaps and automatically flags missing elements before submission deadlines.

#### The Outcome
Reduce DHF compilation time from 50 hours to 8 hours per device. Eliminate 90% of regulatory submission delays due to documentation gaps. Enable 1 FTE to manage DHFs for 3x more devices while improving submission quality scores by 40%.

#### Discovery Questions
1. How many FTEs are currently dedicated to DHF compilation and maintenance across your device portfolio?
2. What percentage of your 510(k) submissions receive Complete Response Letters due to documentation issues?
3. How do you currently ensure traceability between design inputs and verification protocols across design changes?
4. What's the average cost impact when a regulatory submission is delayed by incomplete design controls documentation?
5. How many different systems do you use to manage design controls, and how do you maintain traceability across them?

#### Industry Context
DHF management is the backbone of FDA compliance but represents pure overhead that scales exponentially with device complexity. Teams managing combination products or SaMD often maintain separate DHFs for hardware and software components, multiplying documentation burden. The shift to EU MDR has added technical file requirements that mirror but don't align with DHF structure, creating dual documentation paths.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Design History File tracker with these columns: Design Control ID (text), Design Input Description (long text), Design Output Document (file), Verification Protocol (file), Validation Protocol (file), Design Review Status (status: Not Started, In Progress, Complete, Approved), V&V Status (status: Planning, Executing, Complete, Passed, Failed), Risk Analysis Reference (text), DHF Section (dropdown: Inputs, Outputs, Verification, Validation, Reviews, Transfer, Changes), Regulatory Pathway (dropdown: 510k, De Novo, PMA, EU MDR), Device Component (dropdown: Hardware, Software, Biocompatible Material, Packaging), Traceability Links (text), and Owner (people). Add automation to notify quality team when V&V Status changes to Failed. Create a Kanban view grouped by DHF Section and a Timeline view showing verification/validation schedules. Include a dashboard showing DHF completeness percentage by regulatory pathway."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DHF Compliance Guardian

**Agent Purpose:**  
Continuously monitor design control documentation and ensure 21 CFR 820.30 compliance across all active device development projects.

**Triggers:**
- New design input or output document uploaded
- Design change request submitted
- V&V protocol completion
- Design review scheduled or completed
- 30 days before regulatory submission deadline

**Actions:**
- Auto-populate traceability matrices between design inputs and outputs
- Generate compliance gap reports highlighting missing design controls
- Create draft V&V protocols based on design inputs and risk analysis
- Update DHF section completeness scores in real-time
- Escalate critical compliance gaps to quality and regulatory teams
- Generate regulatory submission checklists based on device classification

**Data Required:**
- Design control documentation repository
- Regulatory pathway requirements database
- Historical V&V protocols and results
- Risk management files (ISO 14971)
- Predicate device analysis data for 510(k) pathways

**Autonomy Level:** Human-in-the-Loop
Agent autonomously monitors and flags issues but requires human review for all regulatory-critical decisions and document approvals.

**Example Interaction:**
> The DHF Compliance Guardian detects that a new software module has been added to a Class II SaMD device currently in the verification phase. It automatically cross-references the design input against existing V&V protocols, identifies that no software unit testing protocol exists for the new module per IEC 62304 requirements, and creates a high-priority task for the software quality engineer. The agent then generates a draft verification protocol template based on the device's existing software lifecycle documentation and flags the potential impact on the planned 510(k) submission timeline. It escalates to the regulatory lead with a risk assessment showing that the missing protocol could delay submission by 6 weeks if not addressed within 10 days.

---

### Use Case 2: Automated Risk Management and FMEA Orchestration

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
ISO 14971 risk management requires continuous FMEA analysis across design changes, with risk control verification for every identified hazard. Teams manually update risk matrices, track risk control effectiveness, and maintain risk-benefit analyses for clinical evaluation reports. This process typically requires 2-3 dedicated risk engineers per product line, with FMEA sessions consuming 20-30 hours per design iteration. Risk file preparation for regulatory submissions takes an additional 40-60 hours per device.

#### The Solution
AI-powered risk analysis that automatically identifies potential failure modes based on design inputs, generates FMEA worksheets with severity/occurrence/detection scoring, and continuously monitors risk control implementation status. Vibe-built risk management boards integrate with design control workflows, while AI agents automatically update risk assessments when design changes occur and flag new hazards requiring analysis.

#### The Outcome
Reduce FMEA analysis time by 70% while improving hazard identification completeness by 50%. Enable risk engineers to manage 2x more products while reducing risk file preparation from 50 hours to 12 hours per regulatory submission. Improve risk control verification tracking, reducing post-market safety issues by 30%.

#### Discovery Questions
1. How many risk engineers do you currently have, and how many products does each manage?
2. What percentage of your post-market safety issues could have been identified during design-phase FMEA?
3. How long does it take to update your risk management file when a design change occurs?
4. Do you use software tools for FMEA analysis, or is it primarily spreadsheet-based?
5. How do you ensure risk control verification is completed before design transfer to manufacturing?

#### Industry Context
Risk management is often the bottleneck in device development, especially for combination products where software, hardware, and biological risks must be assessed separately and holistically. The shift from ISO 14971:2007 to 2019 added risk-benefit analysis requirements that many teams struggle to quantify objectively. Software risk analysis per IEC 62304 adds another layer of complexity for SaMD developers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an ISO 14971 Risk Management tracker with columns: Hazard ID (text), Hazard Description (long text), Hazardous Situation (long text), Harm (long text), Severity Score (rating 1-5), Occurrence Score (rating 1-5), Detection Score (rating 1-5), Risk Priority Number (formula: Severity × Occurrence × Detection), Risk Acceptability (status: Acceptable, ALARP, Unacceptable), Risk Control Measures (long text), Residual Risk Level (dropdown: Negligible, Low, Medium, High), Verification Status (status: Not Started, In Progress, Complete, Verified), Device Component (dropdown: Hardware, Software, User Interface, Packaging, Labeling), Regulatory Impact (dropdown: 510k Required, PMA Impact, Post-Market Surveillance), Owner (people), and Due Date (date). Add automations to notify when RPN exceeds 50 and when verification is overdue. Create views for unacceptable risks, pending verifications, and software-specific hazards. Include dashboard showing risk distribution and verification completion rates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FMEA Intelligence Engine

**Agent Purpose:**  
Continuously analyze design changes for new failure modes and automatically maintain comprehensive risk management files per ISO 14971.

**Triggers:**
- Design input or output document updated
- New component added to bill of materials
- User interface design changes
- Software code commits (for SaMD)
- Supplier change notifications
- Post-market feedback received

**Actions:**
- Auto-generate potential failure mode scenarios based on design changes
- Calculate risk priority numbers and flag unacceptable risks
- Create verification protocol templates for new risk control measures
- Update residual risk assessments after control implementation
- Generate risk-benefit analysis summaries for clinical evaluation
- Cross-reference predicate device FMEA data for 510(k) pathways

**Data Required:**
- Component specifications and supplier data
- Historical failure mode databases
- Post-market surveillance reports
- Predicate device risk analyses
- Clinical literature on device-related adverse events
- IEC 62304 software risk classification data

**Autonomy Level:** Human-in-the-Loop
Agent identifies and assesses risks autonomously but requires human validation for all risk acceptability decisions and control measure selection.

**Example Interaction:**
> When a design engineer updates the specifications for a cardiac catheter tip material, the FMEA Intelligence Engine automatically analyzes the change against historical biocompatibility data and identifies three new potential failure modes: thrombogenicity risk due to surface texture changes, mechanical failure under cyclic loading, and potential for particulate generation. It generates initial severity and occurrence scores based on similar devices in its database, creates verification protocol templates for each risk control measure, and flags the need for updated biocompatibility testing per ISO 10993. The agent then calculates the impact on the overall device risk profile and recommends whether the change requires a new 510(k) submission based on FDA predicate device analysis guidelines.

---

### Use Case 3: Clinical Trial and 510(k) Submission Pipeline Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Clinical investigation management involves coordinating multiple study sites, tracking patient enrollment, managing adverse event reporting, and preparing clinical data for 510(k) submissions or PMA applications. Teams use separate systems for clinical data management, regulatory tracking, and submission preparation, creating data silos and manual reconciliation work. Clinical study reports often require 100-200 hours to compile from disparate data sources.

#### The Solution
Unified clinical operations platform built on monday.com with integrated patient enrollment tracking, adverse event management, and automated clinical study report generation. AI agents monitor study progress against enrollment targets, flag potential FDA inspection issues, and automatically populate 510(k) clinical summaries from study databases.

#### The Outcome
Reduce clinical study report preparation time from 150 hours to 30 hours. Improve study enrollment timeline predictability by 40% through AI-powered site performance analytics. Eliminate 80% of clinical data transcription errors in regulatory submissions while reducing overall submission preparation time by 50%.

#### Discovery Questions
1. How many clinical studies are you typically running simultaneously, and across how many sites?
2. What's your current average timeline from last patient out to 510(k) submission?
3. How many different systems do you use to manage clinical data, and how do you ensure data integrity across them?
4. What percentage of your FDA interactions involve clinical data adequacy questions?
5. How do you currently track and report adverse events across multiple study sites?

#### Industry Context
Clinical operations for medical devices are often less standardized than pharma, with many companies running smaller, single-arm studies focused on safety and substantial equivalence rather than efficacy. The shift toward real-world evidence and post-market studies adds complexity to traditional clinical trial management approaches.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Clinical Investigation Management system with columns: Study ID (text), Device Name (text), Study Type (dropdown: Pivotal, Post-Market, Real-World Evidence, Feasibility), Regulatory Pathway (dropdown: 510k, De Novo, PMA, EU Clinical Investigation), Study Phase (status: Planning, IRB Review, Enrollment, Follow-up, Analysis, Report), Primary Endpoint (long text), Target Enrollment (numbers), Current Enrollment (numbers), Enrollment Progress (formula: Current/Target × 100), Sites Active (numbers), Principal Investigator (people), Study Coordinator (people), Adverse Events Reported (numbers), Serious Adverse Events (numbers), FDA Communication (dropdown: None Required, Pre-Sub Planned, Meeting Requested, Complete), Submission Target Date (date), and Clinical Report Status (status: Not Started, Drafting, Review, Complete). Add automations to alert when enrollment falls behind targets and when SAEs are reported. Create dashboard showing enrollment trends, AE rates by study, and submission timeline progress."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Clinical Operations Orchestrator

**Agent Purpose:**  
Automate clinical study monitoring, adverse event processing, and regulatory submission preparation for device clinical investigations.

**Triggers:**
- New patient enrollment
- Adverse event report submitted
- Study milestone reached
- FDA communication received
- Enrollment target timeline missed
- Clinical data lock achieved

**Actions:**
- Generate weekly enrollment performance reports by site
- Auto-classify adverse events by severity and device relationship
- Create draft clinical study report sections from database queries
- Flag potential FDA inspection risks based on data patterns
- Generate 510(k) clinical summary templates
- Update regulatory submission timelines based on study progress

**Data Required:**
- Clinical database (EDC system integration)
- Adverse event reporting system
- Site performance metrics
- Regulatory correspondence tracking
- Predicate device clinical data
- FDA guidance document library

**Autonomy Level:** Escalation-Based
Fully autonomous for routine monitoring and reporting, with automatic escalation for safety issues, regulatory inquiries, and submission-critical decisions.

**Example Interaction:**
> The Clinical Operations Orchestrator detects that enrollment at the lead clinical site has dropped 60% below target for the past three weeks. It automatically analyzes enrollment patterns across all sites, identifies that two sites are consistently outperforming targets while three are underperforming. The agent generates a site performance report highlighting the enrollment gap and its impact on the planned 510(k) submission timeline, recommending either adding two additional sites or extending the enrollment period by 8 weeks. It then drafts communication templates for the clinical team to send to underperforming sites and creates a revised submission timeline showing the impact of each option on market launch dates.

---

### Use Case 4: Design Transfer and Manufacturing Handoff Orchestration

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Design transfer from R&D to manufacturing requires comprehensive documentation packages including manufacturing specifications, quality control procedures, process validation protocols, and training materials. Teams manually compile transfer packages containing 200-500 documents, with high risk of version control errors and missing specifications that can delay manufacturing startup by 3-6 months. Manufacturing teams often receive incomplete packages, requiring multiple iterations and engineering consultation.

#### The Solution
AI-powered design transfer orchestration that automatically compiles manufacturing packages from design history files, validates completeness against transfer checklists, and creates manufacturing-ready documentation. Vibe-built transfer management boards track package completion status across multiple products while AI agents ensure all design controls are properly translated into manufacturing specifications.

#### The Outcome
Reduce design transfer package preparation time from 120 hours to 25 hours per product. Eliminate 85% of manufacturing startup delays due to incomplete documentation. Enable seamless handoffs with 95% first-pass manufacturing success rate while reducing engineering support requirements during production startup by 60%.

#### Discovery Questions
1. How many products are you currently transferring to manufacturing annually, and what's the average timeline?
2. What percentage of manufacturing startups require additional engineering support due to incomplete transfer documentation?
3. How do you currently ensure all design changes are reflected in manufacturing specifications?
4. What's the typical cost of manufacturing delays caused by design transfer issues?
5. How many revisions of design transfer packages do you typically need before manufacturing acceptance?

#### Industry Context
Design transfer is often the hidden bottleneck where innovative R&D work stalls in manufacturing translation. The complexity increases exponentially for combination products, where separate manufacturing processes for drug, device, and software components must be coordinated while maintaining sterility and performance requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Design Transfer Management board with columns: Product Name (text), Transfer Phase (status: Planning, Documentation, Review, Manufacturing Validation, Complete), Documentation Package (file), Manufacturing Specifications (file), Quality Control Procedures (file), Process Validation Protocol (file), Training Materials (file), Completeness Score (formula calculating percentage complete), Manufacturing Site (dropdown: Site A, Site B, Site C, Contract Manufacturer), Manufacturing Engineer (people), Quality Engineer (people), R&D Lead (people), Transfer Target Date (date), Manufacturing Startup Date (date), Engineering Support Hours (numbers), First Pass Success (checkbox), and Issue Log (long text). Add automations to notify manufacturing team when packages are ready for review and alert when transfer dates are at risk. Create timeline view for transfer scheduling and dashboard showing transfer success metrics and engineering support requirements."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Transfer Package Intelligence

**Agent Purpose:**  
Automatically generate comprehensive design transfer packages and ensure seamless R&D to manufacturing handoffs.

**Triggers:**
- Design freeze milestone reached
- Manufacturing transfer requested
- Design change during transfer process
- Manufacturing validation failure
- Quality control specification update
- New manufacturing site selection

**Actions:**
- Auto-compile design transfer documentation from DHF
- Generate manufacturing specification templates from design outputs
- Create quality control procedures based on design verification protocols
- Validate package completeness against regulatory requirements
- Generate manufacturing training materials from design documentation
- Update transfer timelines based on manufacturing capacity

**Data Required:**
- Complete design history file
- Manufacturing capability data by site
- Quality system procedures templates
- Historical transfer success metrics
- Supplier qualification status
- Regulatory manufacturing requirements

**Autonomy Level:** Human-in-the-Loop
Autonomously compiles and validates packages but requires human approval for all manufacturing specifications and quality procedures before transfer.

**Example Interaction:**
> When an R&D team completes design verification for a new surgical instrument, the Transfer Package Intelligence agent automatically extracts all relevant documentation from the DHF and begins compiling the manufacturing package. It identifies that the device requires specialized coating application available only at Site B, updates the transfer timeline to account for Site B's current capacity, and generates manufacturing specifications that translate the design requirements into process parameters. The agent then creates quality control procedures based on the verification protocols, highlights that one material supplier needs requalification for the new coating process, and recommends starting supplier qualification immediately to avoid delaying the manufacturing startup by 6 weeks.

---

### Use Case 5: Regulatory Intelligence and Submission Tracking

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Regulatory teams must track multiple simultaneous FDA submissions across different pathways (510(k), De Novo, PMA), monitor changing guidance documents, and maintain correspondence with multiple regulatory agencies for global submissions. Teams manually track submission status, prepare response letters, and monitor regulatory intelligence across multiple sources. A single regulatory professional typically manages 5-10 submissions simultaneously, with high risk of missing critical deadlines or guidance updates.

#### The Solution
Centralized regulatory operations platform with AI-powered guidance monitoring, automated submission tracking, and intelligent correspondence management. AI agents continuously scan FDA databases for relevant guidance updates, automatically populate submission templates, and generate regulatory strategy recommendations based on predicate device analysis and pathway optimization.

#### The Outcome
Enable regulatory professionals to manage 2x more submissions while reducing response letter preparation time by 60%. Improve submission quality through AI-powered completeness checking, reducing FDA additional information requests by 40%. Accelerate regulatory decision-making through real-time intelligence on pathway strategies and competitive approvals.

#### Discovery Questions
1. How many regulatory professionals do you have, and how many submissions does each manage simultaneously?
2. What percentage of your submissions receive additional information requests from FDA?
3. How do you currently monitor changes to FDA guidance documents that affect your products?
4. What's the average timeline from submission to FDA clearance for your 510(k) submissions?
5. How do you track and manage submissions to international regulatory bodies like EU notified bodies?

#### Industry Context
Regulatory complexity has increased exponentially with EU MDR implementation, FDA's increasing scrutiny of software devices, and emerging requirements for cybersecurity and AI/ML submissions. Teams must navigate multiple pathways while maintaining global regulatory strategy alignment and competitive intelligence.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Regulatory Submission Tracker with columns: Submission ID (text), Product Name (text), Regulatory Pathway (dropdown: 510k, De Novo, PMA, EU CE Mark, Health Canada, PMDA Japan), Submission Type (dropdown: Initial, Amendment, Response Letter, Annual Report), Submission Date (date), FDA Review Clock Days (numbers), Target Decision Date (date), Current Status (status: Pre-Submission, Under Review, Additional Info Requested, Decision Pending, Approved, Denied), Regulatory Agency (dropdown: FDA, EU Notified Body, Health Canada, TGA), Regulatory Lead (people), Submission Package (file), Correspondence Log (long text), Additional Information Requests (numbers), Predicate Devices (text), Competitive Intelligence (long text), and Revenue Impact (numbers). Add automations to alert when review clock approaches deadlines and when additional information is requested. Create dashboard showing approval timelines by pathway, success rates, and revenue pipeline by submission status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Strategy Navigator

**Agent Purpose:**  
Continuously monitor regulatory landscape changes and optimize submission strategies for fastest market access.

**Triggers:**
- New FDA guidance document published
- Competitive device approval announced
- Submission deadline approaching
- Additional information request received
- International regulatory requirement change
- Predicate device recall or safety notice

**Actions:**
- Scan FDA databases for relevant guidance updates and impact analysis
- Generate regulatory pathway recommendations based on device characteristics
- Auto-populate submission templates with product-specific data
- Create competitive intelligence reports on similar device approvals
- Generate response letter drafts for FDA additional information requests
- Update global submission timelines based on regulatory changes

**Data Required:**
- FDA guidance document database
- Competitive device approval database
- Submission history and success metrics
- Product classification and predicate device analysis
- International regulatory requirement databases
- Clinical and performance testing data

**Autonomy Level:** Human-in-the-Loop
Autonomously monitors and analyzes regulatory intelligence but requires human validation for all strategic decisions and regulatory submissions.

**Example Interaction:**
> The Regulatory Strategy Navigator detects that FDA has published new draft guidance on cybersecurity for connected medical devices that affects the company's upcoming 510(k) submission for a wireless patient monitoring system. It automatically analyzes the guidance requirements against the current submission package, identifies three gaps in cybersecurity documentation, and generates a revised submission timeline that includes time for additional cybersecurity testing. The agent then researches recent similar device approvals to understand how other companies have addressed the new requirements, creates a gap analysis report for the regulatory team, and recommends whether to proceed with the current submission or wait for cybersecurity updates to avoid an additional information request that could delay approval by 90 days.

---

### Use Case 6: Software Lifecycle Management for SaMD Devices

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Software as a Medical Device (SaMD) development requires adherence to IEC 62304 software lifecycle processes, with rigorous configuration management, verification testing, and risk analysis for each software version. Teams manage separate tools for version control, bug tracking, verification testing, and regulatory documentation, creating integration complexity and traceability gaps. Software risk classification changes require comprehensive impact analysis across multiple regulatory submissions.

#### The Solution
Integrated SaMD lifecycle management platform that connects code repositories with regulatory documentation, automated verification test execution, and real-time risk classification updates. AI agents monitor code changes for regulatory impact, automatically generate software requirements traceability, and maintain IEC 62304 compliance documentation throughout the development lifecycle.

#### The Outcome
Reduce software verification documentation time by 50% while improving traceability between requirements and test cases by 90%. Enable software teams to maintain IEC 62304 compliance across 3x more product versions while reducing regulatory review preparation from 40 hours to 8 hours per software release.

#### Discovery Questions
1. How many software-enabled devices do you have in your portfolio, and how many software releases per year?
2. What tools do you currently use for software configuration management and how do they integrate with regulatory documentation?
3. How do you currently maintain traceability between software requirements and verification test cases?
4. What percentage of your software releases require regulatory review, and how long does that process take?
5. How do you assess software risk classification changes and their impact on regulatory pathway requirements?

#### Industry Context
SaMD regulation is rapidly evolving, with FDA's recent guidance on AI/ML devices and EU MDR software classification requirements creating new compliance burdens. Many traditional medical device companies lack software expertise and struggle to adapt hardware-focused quality systems to software development methodologies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a SaMD Lifecycle Management board with columns: Software Item ID (text), Software Version (text), IEC 62304 Class (dropdown: A, B, C), Risk Classification (dropdown: Non-Medical, Healthcare, Medical), Software Requirements (long text), Architecture Design (file), Detailed Design (file), Verification Status (status: Not Started, In Progress, Passed, Failed), Validation Status (status: Not Started, In Progress, Passed, Failed), Configuration Management (dropdown: Under Development, Released, Maintained, Discontinued), Regulatory Impact (checkbox), Change Control Record (text), Problem Resolution Status (status: Open, Under Investigation, Resolved, Closed), Release Notes (long text), and Software Developer (people). Add automations to notify when verification fails and when regulatory review is required. Create Kanban view by verification status and timeline view for release planning. Include dashboard showing software risk distribution and verification completion rates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SaMD Compliance Monitor

**Agent Purpose:**  
Continuously ensure IEC 62304 compliance throughout software development lifecycle and automate regulatory impact assessment.

**Triggers:**
- Code commit to regulated software repository
- Software requirements change
- Verification test execution
- Risk classification update
- Problem report filed
- Software release candidate created

**Actions:**
- Auto-assess regulatory impact of code changes
- Generate software requirements traceability matrices
- Update IEC 62304 documentation based on development activities
- Flag potential cybersecurity vulnerabilities requiring risk analysis
- Create verification test protocols based on requirements changes
- Generate software lifecycle process compliance reports

**Data Required:**
- Source code repository and commit history
- Software requirements specifications
- Verification and validation test results
- Risk management file data
- Problem resolution database
- Regulatory submission history for software changes

**Autonomy Level:** Fully Autonomous
Operates autonomously for routine compliance monitoring and documentation with escalation only for high-risk changes or compliance violations.

**Example Interaction:**
> When a software developer commits code that modifies the alarm handling function in a Class C SaMD patient monitoring device, the SaMD Compliance Monitor automatically analyzes the change against IEC 62304 requirements and identifies that the modification affects safety-critical functionality. It generates an updated software requirements traceability matrix showing the impact on three related requirements, flags the need for additional verification testing of alarm timing and escalation logic, and creates a regulatory change assessment indicating that the modification requires FDA notification per the company's 510(k) submission. The agent then generates verification test protocols specifically targeting the alarm functionality changes and schedules the tests in the development timeline, ensuring compliance documentation is updated before the software release.

---

### Use Case 7: Usability Engineering and Human Factors Integration

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
IEC 62366 usability engineering requirements demand comprehensive user research, use-related risk analysis, and human factors validation testing throughout device development. Teams often treat usability engineering as a late-stage compliance activity rather than integrated design input, leading to costly design changes and delayed submissions. Usability testing coordination across multiple user groups and use environments requires significant project management overhead.

#### The Solution
Integrated usability engineering platform that embeds human factors analysis into design control workflows, automates user testing scheduling and data collection, and maintains continuous traceability between use-related risks and design decisions. AI agents analyze user testing data for safety patterns and automatically update use-related risk analysis based on testing results.

#### The Outcome
Integrate usability engineering into 100% of design decisions while reducing human factors validation time by 40%. Improve use-related risk identification by 60% through AI-powered user behavior analysis while reducing late-stage design changes by 70% through early usability integration.

#### Discovery Questions
1. At what stage in your development process do you typically begin formal usability engineering activities?
2. How many use-related risk analysis updates do you perform per product, and what triggers those updates?
3. What percentage of your design changes result from human factors testing findings?
4. How do you currently coordinate usability testing across different user groups and clinical environments?
5. How do you ensure traceability between use-related risks and design control documentation?

#### Industry Context
Usability engineering has evolved from nice-to-have to FDA-required, especially for home-use devices and complex software interfaces. The shift toward patient-operated devices and remote monitoring has made human factors validation critical for regulatory approval and commercial success.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Usability Engineering Management system with columns: Use Scenario ID (text), User Group (dropdown: Physician, Nurse, Patient, Caregiver, Technician), Use Environment (dropdown: Hospital, Clinic, Home, Ambulance, Emergency), Use-Related Risk (long text), Risk Severity (dropdown: Catastrophic, Critical, Marginal, Negligible), User Interface Element (text), Design Control Link (text), Usability Test Status (status: Planned, Recruiting, Testing, Analysis, Complete), Test Participants (numbers), Success Rate (percentage), Use Errors Observed (numbers), Close Calls (numbers), Risk Control Measures (long text), Validation Status (status: Not Started, In Progress, Passed, Failed), IEC 62366 Section (dropdown: 5.1 User Interface, 5.2 User Training, 5.3 Use Environment), and HF Engineer (people). Add automations to alert when use errors exceed thresholds and when validation fails. Create dashboard showing use error trends, success rates by user group, and risk control effectiveness."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Human Factors Insight Engine

**Agent Purpose:**  
Continuously analyze user interaction data and predict use-related risks before they become safety issues.

**Triggers:**
- User interface design change
- New user group identified
- Usability test session completed
- Use error reported during testing
- Post-market use error complaint received
- Design control documentation updated

**Actions:**
- Auto-generate use scenarios based on device functionality and user groups
- Analyze usability testing data for safety signal patterns
- Update use-related risk analysis based on testing results
- Generate risk control recommendations based on observed use errors
- Create usability validation protocols for new design iterations
- Cross-reference post-market data with pre-market usability predictions

**Data Required:**
- Usability testing session recordings and data
- Use-related risk analysis database
- Post-market surveillance reports
- User interface specifications
- Competitive device usability studies
- Clinical workflow analysis data

**Autonomy Level:** Human-in-the-Loop
Autonomously analyzes data and identifies patterns but requires human validation for all risk assessments and design recommendations.

**Example Interaction:**
> During usability validation testing for a new insulin delivery device, the Human Factors Insight Engine analyzes video recordings of 50 user sessions and identifies a pattern where 15% of patients consistently skip the priming step when changing insulin cartridges. The agent cross-references this behavior against the use-related risk analysis and identifies that skipped priming could result in under-delivery of insulin, a potentially critical safety issue. It automatically generates a risk assessment showing the potential clinical impact, creates design recommendations for making the priming step more prominent in the user interface, and updates the use-related risk analysis with quantified data on the frequency and severity of this use error. The agent then flags this finding for immediate design team review and recommends additional testing with modified interface designs.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **Design Controls (21 CFR 820.30)** | FDA regulation requiring systematic design and development procedures including inputs, outputs, reviews, verification, validation, transfer, and changes |
| **DHF (Design History File)** | Comprehensive compilation of records demonstrating that design controls were followed throughout device development |
| **V&V (Verification and Validation)** | Verification confirms design outputs meet inputs; validation ensures device meets user needs and intended use |
| **510(k) Submission** | FDA premarket submission demonstrating substantial equivalence to legally marketed predicate device |
| **PMA (Premarket Approval)** | FDA's most stringent premarket review for Class III devices requiring clinical data for safety and effectiveness |
| **De Novo Classification** | FDA pathway for novel devices without appropriate predicate, establishing new device classification |
| **SaMD (Software as a Medical Device)** | Software intended for medical purposes without being part of hardware medical device |
| **IEC 62304** | International standard for software lifecycle processes for medical device software |
| **ISO 14971** | International standard for risk management application to medical devices |
| **FMEA (Failure Mode Effects Analysis)** | Systematic method for evaluating potential failure modes and their effects |
| **ISO 10993** | International standard for biological evaluation of medical devices (biocompatibility) |
| **IEC 62366** | International standard for usability engineering application to medical devices |
| **EU MDR** | European Union Medical Device Regulation replacing Medical Device Directive |
| **Technical File** | Documentation package required for EU MDR compliance demonstrating device safety and performance |
| **GSPR (General Safety and Performance Requirements)** | Essential requirements that medical devices must meet under EU MDR |
| **Notified Body** | EU-designated organization that assesses medical device conformity for CE marking |
| **Design Input/Output** | Requirements that form basis of device design (inputs) and results of design effort (outputs) |
| **Design Review** | Systematic examination of design results to evaluate capability to meet requirements |
| **Design Transfer** | Activities ensuring device design is correctly translated into production specifications |
| **Predicate Device** | Legally marketed device used for substantial equivalence comparison in 510(k) submissions |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **R&D Director** | Overall product development strategy, resource allocation, portfolio prioritization | High - Budget authority and strategic direction |
| **Design Engineer** | Device design, specifications, design controls execution | Medium - Technical decision-making |
| **Regulatory Affairs Manager** | FDA submissions, regulatory strategy, compliance oversight | High - Approval pathway decisions |
| **Quality Engineer** | Design verification/validation, quality system compliance | Medium - Process and compliance gatekeeping |
| **Clinical Affairs Director** | Clinical studies, clinical data generation, physician relationships | Medium - Clinical strategy and study design |
| **Software Engineer** | SaMD development, IEC 62304 compliance, cybersecurity | Medium - Technical implementation |
| **Risk Management Engineer** | ISO 14971 compliance, FMEA, risk-benefit analysis | Medium - Risk assessment and control |
| **Human Factors Engineer** | Usability engineering, IEC 62366 compliance, user testing | Low-Medium - User interface optimization |
| **Manufacturing Engineer** | Design transfer, production specifications, process validation | Medium - Manufacturing feasibility |
| **Project Manager** | Timeline management, resource coordination, milestone tracking | Medium - Schedule and resource optimization |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Quality Assurance** | Design controls oversight, regulatory compliance | Integrated quality management, automated compliance monitoring |
| **Manufacturing** | Design transfer, production specifications | Seamless design-to-manufacturing handoffs, DFM integration |
| **Clinical Affairs** | Clinical study execution, physician feedback | Unified clinical operations, automated study reporting |
| **Regulatory Affairs** | Submission preparation, agency interactions | Integrated regulatory intelligence, automated submission tracking |
| **Marketing** | Market requirements, competitive analysis | Voice-of-customer integration, competitive intelligence automation |
| **Sales** | Customer feedback, market needs | Real-time customer input integration, sales enablement automation |
| **Service/Support** | Post-market performance, complaint handling | Post-market surveillance automation, complaint trending analysis |
| **Supply Chain** | Component sourcing, supplier management | Supplier risk management, component change impact analysis |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Arena PLM** | Traditional product lifecycle management | Limited AI capabilities, poor cross-functional integration |
| **Veeva Vault QualityDocs** | Document management for life sciences | No AI agents, expensive per-user licensing |
| **MasterControl** | Quality management system | Legacy interface, limited workflow automation |
| **Greenlight Guru** | Medical device-specific QMS | Narrow focus, lacks cross-departmental visibility |
| **Omnify Empower** | Design controls and risk management | Limited scalability, no AI-powered insights |
| **Jama Connect** | Requirements management | Point solution, doesn't integrate with broader workflows |
| **TestRail** | Test case management | Testing-only focus, no regulatory workflow integration |
| **Smartsheet** | Project management with some compliance features | Generic solution, lacks medical device-specific capabilities |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We're locked into our current PLM system" | "monday.com integrates with existing PLM systems while adding AI capabilities they lack. Start with specific workflows like DHF management or risk analysis where current tools underperform." |
| "Regulatory requires validated systems" | "monday.com supports 21 CFR Part 11 compliance and validation packages. Many medical device companies have successfully validated monday.com for regulated workflows." |
| "Our team doesn't have time to learn new tools" | "Vibe builds workflows in minutes using natural language. Teams can replicate existing processes quickly, then enhance with AI capabilities over time." |
| "We need medical device-specific features" | "Our Vibe platform builds any medical device workflow you need. Plus AI agents automate device-specific processes like FMEA analysis and DHF compilation that generic tools can't handle." |
| "What about data security and compliance?" | "Enterprise-grade security with SOC 2, HIPAA compliance capabilities, and data residency options. Many medical device companies trust monday.com with their most sensitive development data." |
| "AI can't replace human expertise in regulated environments" | "AI agents augment expert decisions rather than replacing them. They handle time-consuming documentation and analysis while experts focus on strategic and safety-critical decisions." |
| "We have too many products to migrate" | "Start with new product launches or highest-value workflows. Prove ROI on a subset before expanding. Migration can be phased over multiple quarters." |

## Proof Points
*(To be populated with customer references)*

- **Fortune 500 Medical Device Company:** Reduced DHF compilation time by 65% while improving regulatory submission quality scores
- **SaMD Startup:** Achieved IEC 62304 compliance for 3 software products with 50% fewer resources than traditional approaches  
- **Combination Product Developer:** Streamlined clinical operations across 8 simultaneous studies with 40% improvement in study timeline predictability
- **Class III Device Manufacturer:** Accelerated design transfer process by 60% while eliminating manufacturing startup delays
- **Multi-National Device Company:** Consolidated 12 separate quality and regulatory tools into unified AI-powered platform
- **Emerging Growth Company:** Scaled from 2 products to 8 products without adding regulatory or quality headcount

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*