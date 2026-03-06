# Medical Devices & Equipment × Sales Playbook

## Overview

Medical device sales teams operate in one of the most complex B2B environments, where multi-year capital equipment cycles intersect with critical patient care decisions. Sales teams must navigate intricate stakeholder ecosystems including surgeons, biomedical engineers, value analysis committees (VACs), and group purchasing organizations (GPOs) while maintaining strict compliance with AdvaMed Code of Ethics and Sunshine Act reporting requirements. The average hospital capital equipment sale can take 18-36 months and involve 8-15 decision makers.

Sales organizations typically structure around territories covering hospital systems, ambulatory surgery centers (ASCs), and physician offices, with specialized roles including clinical specialists who provide deep product expertise and procedure-specific training. The shift toward value-based care has intensified focus on reimbursement outcomes (CPT/HCPCS/DRG codes), while competitive pressures drive sophisticated loaner kit management, consignment inventory tracking, and increasingly, rep-less/self-service models for routine procedures. Success depends on managing complex product portfolios across multiple procurement channels while maintaining clinical relationships and demonstrating measurable patient outcomes.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|--------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | **HIGH** | Clinical specialists, territory managers, and inside sales teams are expensive and scarce. AI agents can handle routine territory management, compliance tracking, and initial prospect qualification 24/7. |
| **Consolidate Tech Stack with AI** | **HIGH** | Sales teams juggle CRM, sample tracking, loaner management, compliance reporting, competitive intelligence, and territory planning tools. One AI platform that connects all data and automates workflows eliminates integration overhead. |
| **Scale Impact Without Overhead** | **MEDIUM** | As device portfolios expand and territories grow, traditional 1:1 rep coverage becomes unsustainable. AI enables territory expansion without proportional headcount increases. |

## Prioritized Use Cases

---

### Use Case 1: GPO Contract & IDN Sales Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Managing GPO contracts across integrated delivery networks (IDNs) requires tracking dozens of contract terms, pricing tiers, rebate structures, and compliance requirements simultaneously. Sales teams lose deals when they can't quickly identify which GPO contracts apply to specific health systems, what pricing is available, and how close they are to volume commitments. Manual tracking in spreadsheets leads to missed rebate opportunities and contract violations.

#### The Solution
monday.com's unified data layer consolidates all GPO contracts, IDN memberships, and sales activity in one platform. AI agents automatically flag contract opportunities, calculate rebate potentials, and alert sales teams when accounts approach volume thresholds. Vibe builds custom contract management workflows that integrate with CRM data and purchasing systems.

#### The Outcome
- 40% reduction in contract compliance errors
- 25% increase in rebate capture rates
- 60% faster response time to GPO RFP opportunities
- Eliminate 2-3 FTE roles in contract administration

#### Discovery Questions
- How many GPO contracts do you currently manage, and how do you track pricing across different member tiers?
- When was the last time you missed a rebate opportunity because you weren't tracking volume commitments accurately?
- How do you currently identify which health systems belong to which GPOs when planning territory strategy?
- What percentage of your deals involve navigating dual-source or sole-source contract restrictions?
- How do you ensure your sales team knows the latest contract terms when they're in front of a VAC presentation?

#### Industry Context
GPO penetration exceeds 90% of US hospitals, with Premier, Vizient, and HealthTrust controlling ~70% of the market. IDNs often belong to multiple GPOs, creating complex overlapping contract scenarios. Sales teams must understand tier pricing (based on hospital size/volume), committed vs. non-committed contracts, and rebate structures that can impact deal profitability by 15-30%.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a GPO Contract Management board with these columns: GPO Name (dropdown: Premier, Vizient, HealthTrust, Other), Contract Number (text), Product Category (dropdown: Surgical Devices, Imaging Equipment, OR Equipment, Laboratory, Other), Start Date (date), End Date (date), Contract Type (dropdown: Committed, Non-committed, Dual Source, Sole Source), Member Tier (dropdown: Tier 1, Tier 2, Tier 3, Tier 4), Contract Value (numbers in millions), Rebate Rate (percentage), Volume Commitment (numbers), Current Volume (numbers with progress bar), Territory Manager (people), Contract Status (status: Active, Renewal Pending, Expired, Under Review). Add a Timeline view to show contract renewals coming up. Create automation: when Current Volume reaches 80% of Volume Commitment, notify Territory Manager and send alert to contracts team. Add Dashboard view showing total contract value by GPO and rebate opportunities."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** GPO Contract Intelligence Agent

**Agent Purpose:**  
Automatically monitors GPO contract performance, identifies opportunities, and manages compliance across all territories.

**Triggers:**
- New sales opportunity created in CRM
- Contract volume threshold reached (75%, 90%, 100%)
- GPO contract expiration approaching (90, 60, 30 days)
- New GPO RFP published
- Account changes GPO membership status

**Actions:**
- Pull relevant contract terms and pricing for sales opportunities
- Calculate rebate potentials and contract positioning
- Generate VAC presentation materials with contract-compliant pricing
- Alert territory managers to contract opportunities and risks
- Update contract performance dashboards
- Flag accounts approaching volume commitments

**Data Required:**
- CRM sales data and opportunity pipeline
- GPO membership databases and contract terms
- Historical purchase volumes by account
- Competitive pricing intelligence

**Autonomy Level:** Human-in-the-Loop  
Agent identifies opportunities and generates recommendations, but requires human approval for contract commitments and pricing proposals.

**Example Interaction:**
> Territory Manager Sarah receives an alert: "Cleveland Clinic opportunity flagged - Premier Tier 2 contract available with 15% additional rebate if you reach $2.3M volume commitment. Current volume: $1.8M. Recommendation: Bundle OR table with surgical lights to hit threshold. Draft VAC presentation attached with compliant pricing." Sarah reviews the recommendation, adjusts the bundle configuration, and uses the auto-generated presentation materials for her VAC meeting the following week, ultimately closing a $2.1M deal that triggers Premier rebates for the entire region.

---

---

### Use Case 2: OR/Procedural Sales & Surgeon Preference Card Management

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Managing surgeon preference cards and OR-specific sales requires deep clinical knowledge and constant relationship maintenance. Each surgeon has specific product preferences, procedure variations, and decision-making patterns. Sales teams spend 60%+ of their time on administrative tasks - updating preference cards, tracking product usage, and coordinating with OR staff - rather than building relationships and driving new technology adoption.

#### The Solution
AI agents continuously monitor OR schedules, track surgeon preferences, and automatically coordinate product availability for procedures. The platform integrates with hospital systems to update preference cards in real-time and identifies opportunities for product upgrades or new technology introductions based on procedure patterns and clinical outcomes data.

#### The Outcome
- 50% reduction in administrative time for territory managers
- 30% increase in surgeon engagement time
- 25% improvement in preference card accuracy
- 40% faster new product adoption cycles

#### Discovery Questions
- How many surgeons do your reps manage preference cards for, and how often do these change?
- What percentage of your rep's time is spent on administrative coordination vs. clinical relationship building?
- How do you currently identify opportunities to introduce new technology to surgeons?
- When surgeons request product changes, how quickly can you update systems and coordinate with OR staff?
- How do you track which products are driving better clinical outcomes to support competitive positioning?

#### Industry Context
Surgeon preference cards are critical documents that specify exactly which products, sizes, and configurations are required for each procedure type. Changes require coordination between sales reps, OR staff, biomedical engineers, and purchasing. The average orthopedic surgeon performs 15-20 different procedure types with unique preference requirements. Successful reps become extensions of the clinical team, understanding not just products but procedural workflows.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Surgeon Preference Management board with columns: Surgeon Name (people), Specialty (dropdown: Orthopedic, Cardiovascular, Neurosurgery, General Surgery, Other), Hospital System (text), Procedure Type (text), Product Category (dropdown: Implants, Instruments, Disposables, Capital Equipment), Current Product (text), Preference Status (status: Confirmed, Under Review, Change Requested, Trial Pending), Last Updated (date), Usage Volume (numbers), Clinical Outcomes Score (rating 1-5), Competitive Threat Level (dropdown: Low, Medium, High), Next Review Date (date), Territory Manager (people). Add Kanban view organized by Preference Status. Create automation: when Preference Status changes to 'Change Requested', notify Territory Manager and create follow-up task due in 2 days. Add Dashboard showing preference card changes by month and competitive threat analysis."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OR Intelligence Agent

**Agent Purpose:**  
Proactively manages surgeon relationships and preference cards while identifying clinical opportunities.

**Triggers:**
- OR schedule changes detect new procedures
- Preference card modification requests
- Clinical outcome data updates
- Competitive product usage detected
- Surgeon performance metrics change

**Actions:**
- Update preference cards across hospital systems
- Coordinate product availability with OR staff
- Generate clinical outcome reports for surgeons
- Identify technology upgrade opportunities
- Schedule preference card review meetings
- Track competitive threats and displacement opportunities

**Data Required:**
- OR scheduling systems integration
- Clinical outcomes databases
- Product usage tracking from hospital systems
- Surgeon performance metrics

**Autonomy Level:** Escalation-Based  
Agent handles routine preference card updates automatically, escalates clinical discussions and competitive threats to human reps.

**Example Interaction:**
> Dr. Martinez, a high-volume spine surgeon, submits a preference card change request for cervical fusion procedures. The OR Intelligence Agent immediately updates the preference across all hospital systems where Dr. Martinez operates, coordinates with OR managers to ensure product availability for his next three scheduled procedures, and notices the change involves switching from a competitor's product. The agent flags this as a competitive win, generates a case study based on Dr. Martinez's clinical outcomes with the new product, and suggests targeting two other spine surgeons in the territory who perform similar procedures. Territory rep Mike receives a summary with talking points and clinical data ready for his next surgeon visits.

---

---

### Use Case 3: Clinical Specialist Support & Product Trial Management

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Clinical specialists are expensive, specialized resources who provide deep product training and procedure support. Managing their schedules across multiple territories, coordinating product trials, and tracking clinical outcomes requires significant administrative overhead. Trials often extend longer than planned due to poor coordination, and valuable clinical insights get lost without systematic capture and analysis.

#### The Solution
AI agents optimize clinical specialist deployment by predicting procedure schedules, coordinating product trials, and automatically capturing clinical feedback. The platform manages trial timelines, tracks clinical outcomes, and generates insights that accelerate product adoption decisions while maximizing specialist utilization across territories.

#### The Outcome
- 35% improvement in clinical specialist utilization
- 50% reduction in trial cycle times
- 60% better capture of clinical insights
- 25% increase in successful product adoptions

#### Discovery Questions
- How many clinical specialists do you have, and how do you optimize their deployment across territories?
- What's your average product trial duration, and how often do trials extend beyond planned timelines?
- How do you currently capture and analyze clinical feedback from product trials?
- What percentage of product trials result in successful adoptions vs. competitive losses?
- How do you identify which clinical specialists should support which types of procedures or accounts?

#### Industry Context
Clinical specialists often have advanced degrees (MSN, PhD) and deep procedural expertise that commands $150K+ salaries plus travel expenses. They're essential for complex product launches, competitive conversions, and training on new techniques. The average clinical specialist covers 8-12 territories and may support 200+ procedures per quarter across different specialties.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Clinical Trial Management board with columns: Trial ID (auto-number), Product Name (text), Hospital System (text), Principal Surgeon (people), Clinical Specialist Assigned (people), Trial Start Date (date), Planned End Date (date), Actual End Date (date), Trial Status (status: Planning, Active, Extended, Completed, Cancelled), Trial Type (dropdown: New Product Launch, Competitive Conversion, Technique Training, Outcome Study), Case Volume Target (numbers), Cases Completed (numbers with progress bar), Clinical Outcomes (rating 1-5), Feedback Summary (long text), Competitive Products Used (text), Adoption Decision (dropdown: Pending, Approved, Rejected, Extended Trial), Commercial Opportunity (numbers in thousands), Next Action (text), Region (dropdown). Add Timeline view for trial planning and Dashboard for adoption rates by product. Create automation: when Actual End Date passes and Adoption Decision is empty, notify Clinical Specialist and Territory Manager with high priority."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Clinical Excellence Agent

**Agent Purpose:**  
Orchestrates clinical specialist deployment and captures insights from product trials to accelerate adoption decisions.

**Triggers:**
- New product trial requests submitted
- OR schedules indicate procedures using trial products
- Clinical feedback forms completed
- Trial timelines approaching milestones
- Competitive displacement opportunities identified

**Actions:**
- Schedule clinical specialist support based on procedure calendars
- Generate trial protocols and outcome tracking forms
- Collect and analyze clinical feedback data
- Create adoption recommendations with supporting evidence
- Coordinate trial extensions or transitions to commercial use
- Generate clinical case studies and competitive intelligence

**Data Required:**
- OR scheduling and case volume data
- Clinical specialist calendars and expertise areas
- Product trial protocols and outcome measures
- Surgeon feedback and clinical results

**Autonomy Level:** Human-in-the-Loop  
Agent manages scheduling and data collection autonomously, requires human review for adoption recommendations and clinical interpretations.

**Example Interaction:**
> A new robotic surgery system trial begins at Metro Health System with Dr. Johnson. The Clinical Excellence Agent automatically schedules clinical specialist Emma for the first three procedures based on Dr. Johnson's OR calendar, creates outcome tracking forms specific to robotic procedures, and monitors case progression. After 15 cases, the agent analyzes clinical data showing 20% reduction in procedure time and improved patient outcomes, generates an adoption recommendation with financial projections, and identifies two other surgeons in the health system who could benefit from similar technology. Emma receives a complete trial summary with talking points for the adoption meeting, leading to a $1.2M capital equipment purchase.

---

---

### Use Case 4: Sunshine Act Compliance & AdvaMed Code Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Sunshine Act reporting requires detailed tracking of all payments, gifts, meals, and consulting arrangements with healthcare professionals. Manual tracking across multiple touchpoints (meals, speaker programs, consulting agreements, samples) leads to compliance violations, audit risks, and administrative burden. The AdvaMed Code of Ethics adds additional complexity with specific requirements for educational events, research funding, and business courtesies.

#### The Solution
AI agents automatically capture all interactions with healthcare providers, categorize payments according to Sunshine Act requirements, and ensure AdvaMed Code compliance before any spending occurs. The platform integrates with expense systems, event management, and consulting agreements to provide real-time compliance monitoring and automated reporting.

#### The Outcome
- 95% reduction in compliance violations
- 80% time savings in Sunshine Act reporting
- Eliminate dedicated compliance FTE roles
- Zero audit findings in regulatory reviews

#### Discovery Questions
- How do you currently track and report payments to healthcare professionals for Sunshine Act compliance?
- What percentage of your compliance violations are due to incomplete or inaccurate payment tracking?
- How much time does your team spend on quarterly compliance reporting vs. selling activities?
- How do you ensure AdvaMed Code compliance for events, meals, and consulting arrangements?
- What would happen to your business if you failed a Sunshine Act audit?

#### Industry Context
The Sunshine Act requires reporting of payments over $10 to healthcare professionals, with penalties up to $1M for non-compliance. The AdvaMed Code of Ethics provides industry-specific guidelines for interactions with healthcare providers. Companies must track thousands of interactions across sales teams, clinical specialists, and marketing events while maintaining detailed records for potential audits.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Compliance Tracking board with columns: Healthcare Professional (people), NPI Number (text), Payment Date (date), Payment Type (dropdown: Meals, Speaking Fees, Consulting, Research, Travel, Other), Payment Amount (numbers currency), Event Description (text), Business Purpose (text), AdvaMed Category (dropdown: Educational, Research, Business Courtesy, Other), Pre-approval Status (status: Pending, Approved, Rejected, Not Required), Territory Manager (people), Reporting Period (dropdown: Q1, Q2, Q3, Q4), Submission Status (status: Draft, Submitted, Accepted, Under Review), Compliance Notes (long text), Risk Level (dropdown: Low, Medium, High). Add Dashboard showing payments by type and quarter, plus compliance status overview. Create automation: when Payment Amount exceeds $500, change Risk Level to 'High' and notify compliance team. Add second automation: when Reporting Period deadline approaches and Submission Status is 'Draft', send urgent reminder to Territory Manager."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Compliance Guardian Agent

**Agent Purpose:**  
Ensures 100% Sunshine Act compliance and AdvaMed Code adherence across all healthcare provider interactions.

**Triggers:**
- New payment or interaction with healthcare provider
- Expense report submissions containing provider interactions
- Speaking or consulting agreement created
- Educational event planned with provider attendance
- Monthly compliance reporting deadlines

**Actions:**
- Categorize payments according to Sunshine Act requirements
- Verify AdvaMed Code compliance before approving interactions
- Generate quarterly compliance reports automatically
- Flag high-risk interactions for legal review
- Create audit trails for all provider interactions
- Send pre-approval notifications for threshold payments

**Data Required:**
- Healthcare provider databases with NPI numbers
- Expense systems and payment records
- Event management and speaker bureau data
- Legal agreements and consulting contracts

**Autonomy Level:** Fully Autonomous  
Agent handles routine compliance tracking and reporting automatically, escalates only high-risk situations requiring legal review.

**Example Interaction:**
> Sales rep Tom submits an expense report including dinner with Dr. Smith ($85) and conference travel for Dr. Williams ($1,200). The Compliance Guardian Agent immediately categorizes the dinner as "business courtesy" under AdvaMed guidelines, flags the travel payment as requiring pre-approval due to amount, verifies Dr. Williams' NPI number, and generates the appropriate Sunshine Act reporting entries. The agent automatically submits the compliant data to the quarterly report and alerts the legal team about the travel payment for approval. Tom receives confirmation that his expenses are compliant, while the legal team gets a summary requiring their review before final processing.

---

---

### Use Case 5: Territory Management & Account Intelligence

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Territory managers juggle hundreds of accounts across hospitals, ASCs, and physician offices with limited visibility into purchasing patterns, decision-making cycles, and competitive threats. Manual account research and relationship mapping consume significant time, while opportunities get missed due to inadequate account intelligence. Traditional CRM systems don't capture the complex stakeholder relationships and buying processes unique to healthcare.

#### The Solution
AI agents continuously gather account intelligence from multiple data sources, map stakeholder relationships, and predict purchasing opportunities. The platform monitors hospital system changes, leadership transitions, and competitive activity while automatically prioritizing accounts based on opportunity size and competitive positioning.

#### The Outcome
- 40% increase in qualified opportunities identified
- 50% improvement in territory coverage efficiency
- 30% better account prioritization accuracy
- 25% reduction in competitive losses due to early intelligence

#### Discovery Questions
- How many accounts does each territory manager cover, and how do they prioritize their time?
- How do you currently identify new opportunities within existing accounts?
- What percentage of competitive losses could have been prevented with earlier intelligence?
- How do you track stakeholder changes across complex health system hierarchies?
- What's your process for identifying expansion opportunities in current accounts?

#### Industry Context
Medical device territories often span 200+ accounts including hospital systems, ASCs, and physician practices. Account complexity increases with integrated delivery networks where purchasing decisions involve multiple facilities and stakeholder groups. Territory managers must understand organizational charts, budget cycles, and competitive landscapes while maintaining relationships across clinical, administrative, and purchasing functions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Territory Intelligence board with columns: Account Name (text), Account Type (dropdown: Hospital System, ASC, Physician Office, GPO), Annual Revenue Potential (numbers currency), Current Products (text), Competitive Products (text), Key Contacts (people column - multiple), Decision Maker Primary (people), Budget Cycle (dropdown: Calendar Year, Fiscal Year Oct, Fiscal Year Jul), Last Purchase Date (date), Next Opportunity Timeline (text), Competitive Threat Level (dropdown: Low, Medium, High, Critical), Account Priority (dropdown: Tier 1, Tier 2, Tier 3), Territory Manager (people), Last Activity Date (date), Next Action Required (text). Add Map view showing account locations by priority tier. Create automation: when Last Activity Date is more than 30 days ago and Account Priority is 'Tier 1', notify Territory Manager and create follow-up task. Add Dashboard showing pipeline by account tier and competitive threat analysis."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Territory Intelligence Agent

**Agent Purpose:**  
Continuously monitors territory accounts and surfaces opportunities, threats, and relationship insights for maximum territory productivity.

**Triggers:**
- Account leadership changes detected
- New purchasing announcements or RFPs
- Competitive activity intelligence received
- Budget cycle milestones approaching
- Relationship mapping updates needed

**Actions:**
- Research and update account profiles automatically
- Map stakeholder relationships and influence patterns
- Identify expansion opportunities within accounts
- Monitor competitive threats and market changes
- Prioritize account activities based on opportunity scoring
- Generate territory planning recommendations

**Data Required:**
- Hospital system databases and organizational charts
- Purchase history and contract information
- Competitive intelligence and market research
- Relationship mapping and contact databases

**Autonomy Level:** Human-in-the-Loop  
Agent gathers intelligence and generates insights autonomously, requires human validation for relationship strategies and account prioritization.

**Example Interaction:**
> The Territory Intelligence Agent detects that Metro Health System has announced a new CNO and that their cardiac surgery program is expanding with two new OR suites opening in Q3. The agent automatically researches the new CNO's background, identifies her previous product preferences from her last hospital, updates the account stakeholder map, and calculates the revenue opportunity for the new ORs ($2.8M potential). Territory manager Lisa receives an alert with a complete intelligence briefing, suggested talking points for the new CNO, and a recommended approach for positioning their cardiac surgery products. Lisa schedules meetings with both the new CNO and cardiac surgery director, ultimately securing preferred vendor status for the new ORs.

---

---

### Use Case 6: Competitive Intelligence & Conversion Strategy

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device markets are intensely competitive with frequent product launches, pricing changes, and strategic shifts. Sales teams struggle to stay current on competitive intelligence while developing effective displacement strategies. Manual competitive research and win/loss analysis provide limited insights, while opportunities for competitive conversion get missed due to inadequate market intelligence.

#### The Solution
AI agents continuously monitor competitive activity, analyze win/loss patterns, and generate conversion strategies based on clinical outcomes, pricing intelligence, and stakeholder preferences. The platform identifies vulnerable competitive accounts and provides tactical guidance for displacement campaigns while tracking conversion success rates.

#### The Outcome
- 60% improvement in competitive intelligence accuracy
- 45% increase in competitive conversion rates
- 35% reduction in time to develop displacement strategies
- 25% improvement in win rates against key competitors

#### Discovery Questions
- How do you currently gather and analyze competitive intelligence across your territories?
- What percentage of your current business was won from competitive displacement vs. new accounts?
- How do you identify accounts that might be vulnerable to competitive conversion?
- What's your success rate when directly targeting competitor's installed base?
- How do you track and analyze win/loss reasons to improve competitive positioning?

#### Industry Context
Medical device competition often centers on clinical outcomes, total cost of ownership, and surgeon preference rather than simple price comparisons. Competitive intelligence must encompass product features, clinical studies, reimbursement implications, and relationship factors. Successful competitive conversions require deep understanding of why customers chose competitors initially and what would motivate them to switch.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Competitive Intelligence board with columns: Account Name (text), Current Competitor (dropdown: Medtronic, J&J, Stryker, Abbott, Boston Scientific, Other), Competitive Product (text), Contract End Date (date), Relationship Strength (dropdown: Strong, Medium, Weak, Unknown), Clinical Champion (people), Vulnerability Factors (text), Conversion Opportunity Score (numbers 1-10), Our Advantage (text), Conversion Strategy (long text), Action Steps (text), Territory Manager (people), Next Review Date (date), Conversion Status (status: Identified, Qualified, Active Campaign, Won, Lost), Revenue Potential (numbers currency). Add Kanban view by Conversion Status and Calendar view for contract end dates. Create automation: when Contract End Date is within 6 months and Conversion Status is 'Identified', move to 'Qualified' and notify Territory Manager. Add Dashboard showing conversion pipeline and win rates by competitor."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Competitive Warfare Agent

**Agent Purpose:**  
Systematically identifies competitive vulnerabilities and orchestrates strategic conversion campaigns across territories.

**Triggers:**
- Competitive contract expiration approaching
- Clinical outcomes data favoring our products
- Competitor pricing changes detected
- Customer satisfaction issues with competitive products
- New clinical evidence published

**Actions:**
- Identify vulnerable competitive accounts based on multiple factors
- Generate conversion strategies with tactical playbooks
- Monitor competitive pricing and positioning changes
- Analyze win/loss patterns to refine approaches
- Coordinate conversion campaigns across clinical and commercial teams
- Track conversion success rates and ROI

**Data Required:**
- Competitive pricing and contract databases
- Clinical outcomes and research studies
- Customer satisfaction and relationship data
- Win/loss analysis historical data

**Autonomy Level:** Escalation-Based  
Agent identifies opportunities and generates strategies automatically, escalates to human teams for campaign execution and relationship management.

**Example Interaction:**
> The Competitive Warfare Agent detects that Regional Medical Center's five-year contract with Competitor X expires in eight months, and recent clinical studies show 15% better outcomes with our product line. The agent analyzes the account history, identifies that their clinical champion Dr. Peterson has published research on outcome improvement, and generates a conversion strategy focused on clinical excellence rather than price. Territory manager Sarah receives a detailed playbook including Dr. Peterson's research interests, suggested clinical study proposals, and a timeline for relationship building activities. Sarah implements the strategy, engages Dr. Peterson in a clinical outcomes study, and ultimately converts the account to a three-year exclusive contract worth $4.2M annually.

---

---

### Use Case 7: Sample & Demo Device Tracking

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Managing sample and demo device inventory across territories requires tracking location, condition, expiration dates, and availability while ensuring compliance with FDA regulations and internal controls. Lost or expired samples represent direct revenue loss, while inadequate tracking creates compliance risks. Manual inventory management systems fail to provide real-time visibility across field teams.

#### The Solution
AI agents track all sample and demo devices in real-time, predicting demand patterns and optimizing distribution. The platform automates compliance reporting, alerts for expiration dates, and coordinates device returns while providing territory managers with instant visibility into available inventory for customer demonstrations.

#### The Outcome
- 50% reduction in expired sample write-offs
- 70% improvement in sample availability for customer requests
- 85% time savings in inventory management
- 100% compliance with FDA sample tracking requirements

#### Discovery Questions
- How many sample and demo devices do you manage across your field organization?
- What percentage of samples expire before being used, and what's the financial impact?
- How do territory managers currently request and track demo device availability?
- What compliance requirements do you have for sample tracking and reporting?
- How often do you lose sales opportunities due to unavailable demo equipment?

#### Industry Context
Medical device samples and demo equipment can be worth thousands of dollars per unit and require strict FDA traceability. Territory managers often manage $50K+ in sample inventory while coordinating with clinical specialists who carry additional demo equipment. Sample tracking must meet FDA requirements while supporting complex sales cycles that may require multiple demonstrations across different stakeholders.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Sample & Demo Tracking board with columns: Device ID (auto-number), Product Name (text), Serial Number (text), Device Type (dropdown: Sample, Demo Unit, Loaner, Trial), Current Location (text), Assigned To (people), Account Name (text), Status (status: Available, In Use, Maintenance, Expired, Lost), Acquisition Date (date), Expiration Date (date), Last Used Date (date), Condition (dropdown: Excellent, Good, Fair, Needs Maintenance), Value (numbers currency), Territory (dropdown), Next Maintenance Due (date), Return Date Required (date). Add Timeline view for maintenance schedules and Map view for device locations. Create automation: when Expiration Date is within 30 days and Status is not 'Expired', notify device owner and manager. Add second automation: when Return Date Required passes and Status is still 'In Use', escalate to high priority. Add Dashboard showing inventory value by territory and expiration tracking."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Inventory Optimization Agent

**Agent Purpose:**  
Maximizes sample and demo device utilization while ensuring compliance and minimizing inventory costs.

**Triggers:**
- Sample or demo device requests from field teams
- Expiration dates approaching (30, 15, 5 days)
- Device return dates exceeded
- Maintenance schedules due
- Inventory levels below optimal thresholds

**Actions:**
- Optimize device distribution based on demand patterns
- Automate compliance reporting for FDA requirements
- Coordinate device maintenance and calibration schedules
- Alert field teams to expiring inventory
- Track device utilization rates and ROI
- Generate inventory optimization recommendations

**Data Required:**
- Device inventory databases with serial numbers and specifications
- Territory demand patterns and historical usage
- Maintenance schedules and device condition records
- Compliance requirements and reporting templates

**Autonomy Level:** Human-in-the-Loop  
Agent manages routine tracking and optimization autonomously, requires human approval for high-value device movements and compliance submissions.

**Example Interaction:**
> Territory manager Mike receives a request from Springfield Hospital for a demo of the new surgical robot. The Inventory Optimization Agent immediately checks availability, identifies that the nearest demo unit is 200 miles away but will be available after a procedure at City Medical next Tuesday. The agent automatically coordinates the transfer, schedules transportation, ensures all maintenance is current, and books the demo for Thursday morning. Mike receives confirmation with all logistics handled, while the agent tracks the demo through completion and coordinates return to optimal inventory location for the next territory request.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **GPO (Group Purchasing Organization)** | Organizations that negotiate contracts on behalf of member hospitals to achieve volume discounts |
| **IDN (Integrated Delivery Network)** | Health systems that own multiple hospitals, clinics, and care facilities |
| **VAC (Value Analysis Committee)** | Hospital committees that evaluate new products and technologies for adoption |
| **CPT/HCPCS/DRG** | Medical coding systems that determine reimbursement rates for procedures and products |
| **ASC (Ambulatory Surgery Center)** | Outpatient facilities for surgical procedures not requiring overnight stays |
| **Surgeon Preference Cards** | Detailed specifications of products and instruments required for each surgeon's procedures |
| **Clinical Specialist** | Advanced clinical professionals who provide product training and procedure support |
| **Loaner Kit** | Surgical instrument sets provided temporarily for specific procedures |
| **Consignment Inventory** | Product inventory owned by manufacturer but located at customer facility |
| **Sunshine Act/Open Payments** | Federal law requiring disclosure of payments to healthcare providers |
| **AdvaMed Code of Ethics** | Industry guidelines governing interactions between device companies and healthcare providers |
| **Rep-less/Self-Service Model** | Sales approach where routine products don't require sales representative involvement |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| **Chief Medical Officer (CMO)** | Clinical strategy and physician relations | High - Sets clinical priorities |
| **Value Analysis Committee Chair** | Lead product evaluation and adoption decisions | High - Final approval authority |
| **Biomedical Engineering Director** | Technical evaluation and maintenance oversight | High - Technical veto power |
| **Purchasing Director** | Contract negotiation and vendor management | Medium - Price and terms focus |
| **OR Director** | Surgical services operations and efficiency | Medium - Operational feasibility |
| **Department Chair (Surgery)** | Specialty-specific clinical leadership | High - Clinical champion role |
| **CFO** | Financial approval for capital expenditures | High - Budget approval authority |
| **Materials Management** | Inventory and supply chain optimization | Low - Process implementation |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Clinical Affairs** | Manages product trials and clinical evidence | Partner for competitive differentiation through clinical outcomes |
| **Marketing** | Develops product positioning and sales tools | Collaborate on competitive intelligence and market analysis |
| **Training/Education** | Clinical specialist development and certification | Scale training delivery through AI-powered learning platforms |
| **Supply Chain** | Manages inventory, distribution, and logistics | Optimize sample/demo management and inventory visibility |
| **Regulatory Affairs** | Ensures compliance with FDA and international regulations | Automate compliance tracking and reporting processes |
| **Customer Service** | Handles post-sale support and technical issues | Integrate service data to identify upsell and retention opportunities |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|------------------------|
| **Salesforce** | General CRM platform lacking medical device specifics | Replace with industry-specific workflows and AI automation |
| **Veeva CRM** | Life sciences focused but complex and expensive | Offer simpler, more intuitive platform with better AI capabilities |
| **Territory Management Spreadsheets** | Manual tracking with no automation or insights | Complete digital transformation with real-time intelligence |
| **Sample Tracking Systems** | Point solutions without integration to sales process | Consolidate into unified platform with AI optimization |
| **Compliance Software** | Standalone tools requiring manual data entry | Automated compliance with integrated sales workflow |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"We already have Veeva CRM"** | "Veeva handles basic CRM, but can it automatically optimize your clinical specialist schedules, predict GPO contract opportunities, and ensure 100% Sunshine Act compliance? Our AI agents work 24/7 to do the work your reps currently do manually." |
| **"Medical device sales is too complex for automation"** | "That's exactly why AI is so powerful here. The complexity of GPO contracts, VAC processes, and compliance requirements is where AI excels. Our platform doesn't replace clinical relationships - it eliminates administrative burden so your reps can focus on what matters: clinical outcomes and physician relationships." |
| **"Our reps need face-to-face relationships"** | "Absolutely - and our platform gives them more time for those relationships by handling all the administrative work automatically. Instead of spending 60% of their time updating preference cards and tracking samples, they can spend that time with surgeons and clinical teams." |
| **"We can't risk compliance violations"** | "Our AI agents actually reduce compliance risk by ensuring 100% accuracy in Sunshine Act reporting and AdvaMed Code compliance. Human error in manual tracking is your biggest compliance risk - AI eliminates that." |
| **"ROI is hard to measure in medical device sales"** | "We track specific metrics: reduced compliance violations, improved sample utilization, faster trial cycles, and increased territory coverage. Our customers typically see 25-40% productivity gains within six months." |

## Proof Points
*(To be populated with customer references)*

- [ ] Large orthopedic device company achieving 40% reduction in compliance violations
- [ ] Cardiovascular device manufacturer improving clinical specialist utilization by 35%
- [ ] Surgical instrument company increasing competitive conversion rates by 45%
- [ ] Medical technology company reducing sample write-offs by 50%
- [ ] Device manufacturer scaling territory coverage without adding headcount

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*