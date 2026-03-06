# Industrial Machinery & Equipment × Customer Success Playbook

## Overview

Customer Success in the industrial machinery and equipment sector operates at the intersection of complex, high-value capital equipment and long-term client relationships. These teams manage portfolios of customers who have invested anywhere from $50K to $50M+ in CNC machines, hydraulic presses, packaging lines, conveyor systems, turbines, and other heavy equipment. The post-sale relationship is paramount — machinery uptime directly impacts a customer's production output, revenue, and profitability, making Customer Success a strategic revenue function rather than a reactive support desk.

Organizationally, Customer Success in industrial machinery companies typically sits between Sales, Service/Field Engineering, and Parts & Aftermarket divisions. Teams range from 5-50 people depending on company size, and they manage everything from onboarding and commissioning support to ongoing health checks, spare parts consumption tracking, preventive maintenance scheduling, and contract renewals. The role is inherently technical — CSMs often have engineering backgrounds and must understand machine specifications, tolerance levels, and production environments.

Regulatory and compliance requirements add complexity. Equipment sold into food & beverage, pharmaceutical, or aerospace manufacturing must meet FDA, GMP, or AS9100 standards. Customer Success teams must track compliance documentation, calibration schedules, and audit readiness for their installed base. The shift toward Industry 4.0 — IoT-connected machinery with remote monitoring — is transforming CS from periodic check-ins to real-time, data-driven engagement, but most teams still rely on spreadsheets and tribal knowledge.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Installed base grows faster than CS headcount; each CSM manages 30-80 accounts with complex equipment portfolios |
| 2 | Replace or Radically Augment Headcount | Medium-High | Manual tracking of machine health, spare parts consumption, and renewal timelines consumes 60%+ of CSM time |
| 3 | Consolidate Tech Stack with AI | Medium | Teams cobble together ERP (SAP), CRM (Salesforce), IoT platforms, and spreadsheets — no single source of truth for customer health |

## Prioritized Use Cases

---

### Use Case 1: Installed Base & Machine Health Tracker

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most industrial machinery companies have no centralized view of their installed base. Customer Success managers juggle SAP records, serial number spreadsheets, commissioning documents, and field service reports to answer basic questions: "What machines does this customer have? When were they installed? What's their maintenance history? Are they due for an upgrade?" This fragmentation means CSMs spend 5-10 hours per week just assembling customer context before they can take action. Machines approaching end-of-life or running outside optimal parameters go unnoticed until the customer calls with a breakdown — turning a proactive relationship into a reactive firefight.

#### The Solution
monday.com Work Management with mondayDB as the backbone for an installed base registry. Each item represents a machine/asset with columns for serial number, model, installation date, warranty expiration, last service date, next PM due date, IoT health score (if available), customer site, and assigned CSM. Subitems track service history, parts replaced, and firmware versions. Dashboards roll up fleet health by customer, region, and product line. Automations trigger alerts when warranty is expiring (90/60/30 days), when PM is overdue, or when a machine hits a configurable age threshold for upgrade discussions.

#### The Outcome
CSMs gain a single pane of glass for their entire portfolio. Time spent assembling customer context drops by 70%. Proactive outreach on warranty renewals, upgrades, and PM scheduling increases by 3x. Aftermarket revenue (parts, service contracts, upgrades) grows 15-25% as no opportunity falls through the cracks.

#### Discovery Questions
1. "How do your CSMs currently track which machines each customer has in the field — is there a single system or multiple sources?"
2. "When a customer calls about a machine issue, how quickly can your team pull up the full service history and configuration?"
3. "What percentage of your warranty renewals or service contract renewals are you catching proactively vs. reactively?"
4. "Do you have visibility into machines approaching end-of-life or running outside recommended maintenance intervals?"
5. "How do you currently identify upsell opportunities — like a customer running a 10-year-old model that has a newer replacement?"

#### Industry Context
In industrial machinery, the "installed base" is the most valuable asset a company has — it's the foundation for aftermarket revenue (parts, service, upgrades), which often carries 40-60% gross margins vs. 20-30% on new equipment sales. Companies like Caterpillar, Komatsu, and DMG Mori have invested heavily in digital installed base management, but mid-market manufacturers ($100M-$2B revenue) typically lag far behind. Serial numbers, commissioning dates, and service records are scattered across ERP systems, field technician notebooks, and Excel files. The concept of "machine health score" is borrowed from IoT/predictive maintenance but can be simplified to a manual or semi-automated score based on age, service frequency, and operating conditions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Installed Base Tracker for an industrial machinery company's Customer Success team. Create a board called 'Installed Base Registry' with these columns: Customer Name (text), Machine Model (dropdown: CNC Lathe, CNC Mill, Hydraulic Press, Packaging Line, Conveyor System, Turbine Assembly, Custom), Serial Number (text), Installation Date (date), Warranty Expiration (date), Last Service Date (date), Next PM Due (date), Machine Health Score (numbers 1-100), Assigned CSM (people), Site Location (text), Contract Status (status: Active, Expiring Soon, Expired, No Contract), and Aftermarket Revenue YTD (numbers). Groups: organize by customer segments (Enterprise, Mid-Market, SMB). Add subitems for Service History with columns: Service Type (dropdown: Preventive Maintenance, Corrective Repair, Firmware Update, Calibration, Inspection), Date Completed (date), Technician (text), Parts Used (text), Cost (numbers). Create automations: (1) When Warranty Expiration is within 90 days, notify Assigned CSM and change Contract Status to 'Expiring Soon'; (2) When Next PM Due date arrives, create an item in a linked 'CS Action Items' board; (3) When Machine Health Score drops below 50, notify Assigned CSM. Add a Dashboard view with widgets: total machines by model (chart), machines by Contract Status (chart), upcoming warranty expirations (table), overdue PMs (table), and aftermarket revenue by customer (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Fleet Health Monitor
**Agent Purpose:** Continuously analyze the installed base to surface at-risk machines, proactive renewal opportunities, and upgrade recommendations.

**Triggers:**
- Machine Health Score updated below threshold (50)
- Warranty Expiration within 90 days
- Last Service Date exceeds 180 days with no scheduled PM
- New machine commissioned (item created)
- Quarterly installed base review schedule

**Actions:**
- Generate customer health summary combining machine age, service frequency, and contract status
- Create prioritized action items for CSMs (renewal outreach, PM scheduling, upgrade discussion)
- Draft personalized email templates referencing specific machine models and service history
- Flag accounts with declining health scores across multiple machines for escalation
- Recommend upgrade paths based on machine age and newer model availability
- Update Machine Health Score based on composite factors (age, service recency, operating hours)

**Data Required:**
- Installed base registry (serial numbers, models, dates)
- Service history records
- Contract and warranty data
- Product catalog with current models and upgrade paths
- IoT telemetry data (if available via integration)

**Autonomy Level:** Human-in-the-Loop
Automated health scoring and action item creation; CSM reviews and approves outreach. Escalation to CS leadership for accounts with 3+ machines in critical status.

**Example Interaction:**
> The Fleet Health Monitor detects that Apex Manufacturing has three CNC lathes — serial numbers AL-4420, AL-4421, and AL-4422 — all installed in 2019. Their warranty expired six months ago with no service contract renewal, and the last preventive maintenance was logged 14 months ago. The agent calculates a composite health score of 38/100 across the three machines and flags the account as "At Risk."
>
> It creates an action item for Sarah Chen, the assigned CSM: "Apex Manufacturing — 3x CNC Lathes overdue for service, no active contract. Recommended action: Schedule technical review, present service contract options, and discuss upgrade to the AL-5000 series (30% faster cycle times, predictive maintenance built-in). Estimated aftermarket opportunity: $180K."
>
> Sarah reviews the recommendation, adjusts the talking points based on her relationship knowledge, and approves the outreach. The agent drafts a personalized email referencing the specific machines, their installation dates, and the production improvements Apex could achieve with the upgrade, then queues it for Sarah's final review and send.

---

### Use Case 2: Service Contract & Warranty Renewal Pipeline

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Aftermarket service contracts are the lifeblood of industrial machinery profitability, yet renewal management is shockingly manual. CSMs track renewal dates in spreadsheets, set calendar reminders, and rely on memory to initiate outreach. With hundreds of contracts expiring at different times — each with different terms, coverage levels, and pricing tiers — renewals slip through the cracks. Industry benchmarks show that proactive renewal outreach 90+ days before expiration achieves 85%+ renewal rates, while reactive outreach (after expiration) drops to 40-50%. Every missed renewal is $10K-$500K in recurring revenue lost.

#### The Solution
monday.com CRM configured as a renewal pipeline. Each item represents a contract with columns for customer, contract type (Full Service, Parts Only, Extended Warranty, Calibration Agreement), contract value, start date, expiration date, renewal status (Not Started, Outreach Initiated, Proposal Sent, Negotiating, Renewed, Lost), assigned CSM, and linked machines from the installed base board. Automations create renewal action items 120/90/60/30 days before expiration, escalate to management if no activity within 14 days of creation, and move items through pipeline stages based on status changes. Timeline view shows all renewals on a Gantt chart for capacity planning.

#### The Outcome
Renewal capture rate increases from 65% to 85%+. CSMs manage 2x the renewal volume with the same headcount. Aftermarket recurring revenue becomes predictable and forecastable. Management gains real-time visibility into pipeline health without asking for status updates.

#### Discovery Questions
1. "What's your current service contract renewal rate, and how does that compare to your target?"
2. "How far in advance do your CSMs typically start renewal conversations — and is that consistent across the team?"
3. "When a contract expires without renewal, what's the typical revenue impact per contract?"
4. "Do you have visibility into which contracts are up for renewal in the next quarter without asking individual CSMs?"
5. "How do you handle multi-year contracts vs. annual renewals — is the process different?"

#### Industry Context
In industrial machinery, service contracts come in many flavors: Full Service Agreements (FSAs) covering all parts and labor, Parts-Only contracts, Extended Warranties beyond the standard 1-2 year period, Calibration Agreements for precision equipment, and Preventive Maintenance Agreements (PMAs). Pricing is typically based on machine complexity, age, and utilization. The "attach rate" — percentage of new machines sold with a service contract — is a key metric, typically 40-60% at point of sale but declining at each renewal cycle. Leading companies like Siemens and ABB have dedicated "installed base sales" teams, but most mid-market manufacturers rely on Customer Success or the field service organization to manage renewals alongside their other responsibilities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Service Contract Renewal Pipeline for an industrial equipment company. Create a board called 'Contract Renewals' with these columns: Customer Name (text), Contract Type (dropdown: Full Service Agreement, Parts Only, Extended Warranty, Calibration Agreement, Preventive Maintenance Agreement), Annual Contract Value (numbers), Contract Start Date (date), Expiration Date (date), Renewal Status (status: Not Started, Outreach Initiated, Proposal Sent, Negotiating, Renewed, Churned), Assigned CSM (people), Machines Covered (text), Renewal Probability (numbers as percentage), Risk Level (status: Low Risk, Medium Risk, High Risk, Critical), and Notes (long text). Groups: organize by quarter (Q1 2026, Q2 2026, Q3 2026, Q4 2026). Create automations: (1) When Expiration Date is 120 days away, change Renewal Status to 'Not Started' and notify Assigned CSM; (2) When Renewal Status is 'Not Started' for 14 days, notify CS Manager for escalation; (3) When Renewal Status changes to 'Renewed', move to 'Completed' group and create a celebration notification; (4) When Renewal Status changes to 'Churned', create an item in a 'Win-Back Tracker' board. Add a Dashboard with: total renewal pipeline value (numbers widget), renewal rate percentage (chart), renewals by status (pie chart), upcoming expirations by month (bar chart), and CSM performance (table showing renewal rate per person). Add a Timeline view to see all renewals on a Gantt chart."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Renewal Revenue Optimizer
**Agent Purpose:** Maximize service contract renewal rates by automating outreach timing, personalizing proposals, and predicting churn risk.

**Triggers:**
- Contract enters 120-day renewal window
- Customer submits a complaint or critical service ticket
- Machine health score drops for machines under contract
- Contract status unchanged for 14+ days
- Monthly renewal forecast review

**Actions:**
- Calculate renewal probability based on service history, complaint frequency, and engagement level
- Generate personalized renewal proposals with pricing options (same coverage, upgraded coverage, multi-year discount)
- Draft outreach emails referencing specific service events and value delivered during the contract period
- Escalate high-risk renewals to CS leadership with recommended save actions
- Create win-back campaigns for churned contracts after 90 days
- Update pipeline forecasts based on probability-weighted contract values

**Data Required:**
- Contract details (type, value, coverage, terms)
- Service history and ticket data
- Customer engagement metrics (meeting frequency, NPS scores)
- Pricing models and discount authorization levels
- Competitive intelligence on alternative service providers

**Autonomy Level:** Escalation-Based
Routine renewals (low-risk, standard terms) processed automatically with CSM notification. High-value or high-risk renewals escalated for human strategy. Pricing exceptions require manager approval.

**Example Interaction:**
> The Renewal Revenue Optimizer identifies that Global Plastics Corp has a $240K Full Service Agreement expiring in 105 days covering 12 injection molding machines. Over the past year, the contract delivered 8 preventive maintenance visits, 3 emergency repairs (all resolved within SLA), and $45K in parts at no additional cost to the customer. The agent calculates the "value delivered" at $385K — significantly exceeding the contract price.
>
> However, it also detects a risk signal: Global Plastics filed two complaints in the last quarter about technician response times. The agent assigns a renewal probability of 68% (below the 80% benchmark) and flags it as "Medium Risk."
>
> It generates a renewal package: (1) a "value delivered" summary showing $385K in service value for $240K, (2) a proposal with three options — standard renewal at $252K (5% increase), upgraded coverage with 4-hour response guarantee at $290K, and a 3-year lock-in at $228K/year, and (3) a recommended talk track addressing the response time concerns with a new regional technician hire. The package is queued for the CSM's review before outreach.

---

### Use Case 3: Customer Onboarding & Commissioning Tracker

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The first 90 days after a machinery purchase are critical — this is when the customer installs, commissions, tests, and begins production with their new equipment. A botched onboarding experience (late delivery, commissioning delays, inadequate training, missing documentation) sets the tone for the entire relationship and directly predicts contract renewal rates and referral willingness. Yet most machinery companies have no standardized onboarding process. CSMs, field engineers, and project managers coordinate via email chains, phone calls, and institutional memory. Each new machine order starts from scratch, and critical steps (safety certification, operator training, acceptance testing) are missed or delayed.

#### The Solution
monday.com Work Management with a templated onboarding workflow. Each new machine order triggers a pre-built project from a template with phases: Pre-Delivery (site preparation checklist, utility requirements, rigging coordination), Installation (mechanical setup, electrical connection, safety guarding), Commissioning (calibration, test runs, acceptance criteria validation), Training (operator training, maintenance training, documentation handoff), and Go-Live (first production run monitoring, 30/60/90-day check-ins). Each phase has tasks with owners, due dates, dependencies, and approval gates. A customer-facing portal (via monday WorkForms or shared views) gives the buyer visibility into progress without constant email updates.

#### The Outcome
Onboarding cycle time reduces by 30-40%. Customer satisfaction scores for the first 90 days increase by 25%. CSMs handle 50% more concurrent onboardings. Zero critical steps are missed thanks to templated checklists and automated reminders. Time-to-production for customers decreases, strengthening the reference and referral pipeline.

#### Discovery Questions
1. "Walk me through what happens after a customer signs the purchase order — who owns the onboarding, and how is it coordinated?"
2. "How many concurrent installations or commissionings is your team managing at any given time?"
3. "What are the most common causes of delays during machine installation and commissioning?"
4. "How do your customers get visibility into the status of their installation — do they have to call or email for updates?"
5. "Have you ever had a safety or compliance issue during commissioning that could have been caught with a better checklist process?"

#### Industry Context
Commissioning in industrial machinery is the process of verifying that installed equipment operates according to specifications. It includes mechanical alignment, electrical safety testing, hydraulic/pneumatic system validation, software/PLC programming verification, and production acceptance runs. For complex machines (5-axis CNC centers, robotic welding cells), commissioning can take 2-8 weeks on-site. The commissioning engineer is often different from the salesperson and CSM, creating handoff gaps. FAT (Factory Acceptance Test) and SAT (Site Acceptance Test) are standard industry milestones. Documentation deliverables include operation manuals, maintenance manuals, electrical schematics, spare parts lists, and certificates of conformity.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Customer Onboarding & Commissioning Tracker for an industrial machinery company. Create a board called 'Machine Onboarding Projects' with these columns: Customer Name (text), Machine Model (dropdown: CNC Lathe, CNC Mill, Hydraulic Press, Packaging Line, Conveyor System, Custom), Order Number (text), Order Value (numbers), Onboarding Phase (status: Pre-Delivery, Installation, Commissioning, Training, Go-Live, Complete), Assigned CSM (people), Field Engineer (people), Target Go-Live Date (date), Actual Go-Live Date (date), Days to Go-Live (formula), Customer Satisfaction (numbers 1-10), and Risk Flag (status: On Track, At Risk, Delayed, Blocked). Create 5 groups matching the phases. Add subitems for each phase: Pre-Delivery subitems (Site Survey Complete, Utility Requirements Confirmed, Rigging Scheduled, Foundation Prepared); Installation subitems (Machine Delivered, Mechanical Install Complete, Electrical Connected, Safety Guards Installed); Commissioning subitems (FAT Documentation Received, Calibration Complete, Test Runs Passed, SAT Signed Off); Training subitems (Operator Training Scheduled, Operator Training Complete, Maintenance Training Complete, Documentation Delivered); Go-Live subitems (First Production Run, 30-Day Check-In, 60-Day Check-In, 90-Day Check-In). Each subitem has: Owner (people), Due Date (date), Status (status: Not Started, In Progress, Complete, Blocked), Notes (text). Add automations: (1) When all subitems in a group are Complete, move item to next phase; (2) When any subitem is Blocked, change Risk Flag to 'Blocked' and notify CSM; (3) When Target Go-Live Date is within 7 days and phase is not 'Go-Live', change Risk Flag to 'At Risk'. Add a Dashboard showing: active onboardings by phase (chart), average days to go-live (numbers), at-risk projects (table), and customer satisfaction trend (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Onboarding Orchestrator
**Agent Purpose:** Automate onboarding project creation, monitor progress, predict delays, and ensure no commissioning step is missed.

**Triggers:**
- New machine order created in CRM/ERP
- Subitem status changes to "Blocked"
- Target Go-Live Date approaching with incomplete phases
- Customer submits question via WorkForm
- Weekly onboarding portfolio review

**Actions:**
- Auto-generate onboarding project from template with pre-populated customer/machine details
- Calculate realistic go-live timeline based on machine complexity and historical commissioning data
- Send proactive status updates to customers at phase transitions
- Detect bottleneck patterns (e.g., "electrical connection consistently delays commissioning by 5 days") and recommend schedule adjustments
- Create follow-up tasks for 30/60/90-day check-ins after go-live
- Compile commissioning documentation package for customer handoff

**Data Required:**
- Order details (machine model, configuration, customer site)
- Historical onboarding timelines by machine type
- Field engineer availability and scheduling
- Customer site requirements (utilities, rigging, access)
- Compliance requirements by industry/region

**Autonomy Level:** Human-in-the-Loop
Project creation and routine status updates automated. Delay detection and customer communications reviewed by CSM before sending. Escalation to project management for blocked items.

**Example Interaction:**
> A new order is placed: Precision Metals Inc. purchased two 5-axis CNC machining centers, model VMC-5000X, for delivery to their Akron, Ohio facility. The Onboarding Orchestrator automatically creates a project from the VMC-5000X template, populating it with customer details and the contracted delivery date of April 15.
>
> Based on historical data — VMC-5000X installations average 18 business days from delivery to SAT sign-off — the agent sets a target go-live of May 12 and back-calculates all phase milestones. It identifies that Precision Metals' facility requires 480V 3-phase power at the installation site and adds a pre-delivery task: "Confirm electrical capacity at customer site — VMC-5000X draws 45 kVA per unit."
>
> Two weeks into the project, the site survey reveals that the building's electrical panel needs an upgrade. The agent immediately recalculates the timeline, pushing go-live to May 26, notifies the CSM, and drafts a customer communication explaining the delay and the steps being taken. It also flags a pattern: "3 of the last 5 VMC-5000X installations encountered electrical capacity issues — recommend adding power assessment to the pre-sale site survey checklist."

---

### Use Case 4: Customer Health Score & Churn Prediction

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
In industrial machinery, losing a customer doesn't just mean losing one sale — it means losing decades of aftermarket revenue. A single enterprise customer might purchase $2M in equipment, then spend $300K-$500K annually on parts, service, and upgrades over a 15-20 year lifecycle. Yet most CS teams have no systematic way to assess customer health. CSMs rely on gut feel and personal relationships, which doesn't scale and doesn't survive CSM turnover. By the time a customer is visibly unhappy (complaining, not renewing, evaluating competitors), it's often too late to save the relationship.

#### The Solution
monday.com Work Management configured as a Customer Health Dashboard. Each customer is an item with a composite health score calculated from weighted inputs: service contract status (active/expired), recent service ticket sentiment, spare parts order frequency (declining orders = potential churn signal), engagement level (meeting frequency, event attendance, training participation), machine age/fleet health, NPS or CSAT scores, and payment behavior. The health score is visualized as a RAG (Red/Amber/Green) status. Automations trigger intervention workflows when scores drop below thresholds, and a "save playbook" board provides standardized recovery actions for each risk category.

#### The Outcome
At-risk accounts are identified 6+ months before churn, when intervention is still effective. CSM time is rebalanced from equal attention across all accounts to focused effort on at-risk and high-potential accounts. Customer retention rate improves by 10-15%. Revenue predictability increases as health scores correlate with renewal likelihood.

#### Discovery Questions
1. "If I asked you right now to rank your top 10 customers by health — not revenue, but relationship health — could you do it objectively?"
2. "When was the last time you lost a significant customer, and looking back, were there warning signs you missed?"
3. "How do you currently decide which accounts need the most attention this quarter?"
4. "Do your CSMs have access to service ticket data, parts ordering trends, and payment history in one place?"
5. "What happens when a CSM leaves — how much customer relationship context walks out the door?"

#### Industry Context
Customer churn in industrial machinery manifests differently than in SaaS. Customers don't "cancel" — they gradually disengage. Signs include: declining spare parts orders (they're buying from third-party suppliers), not renewing service contracts, reduced participation in user groups or training events, longer payment cycles, and purchasing competitors' equipment for new production lines while keeping existing machines. The concept of "land and expand" applies: the initial equipment purchase is the beachhead, and the goal is to become the standard for all production lines. Losing a customer to a competitor at a single plant often leads to losing the entire enterprise relationship over 3-5 years.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Customer Health Score Dashboard for an industrial machinery CS team. Create a board called 'Customer Health Tracker' with these columns: Customer Name (text), Account Tier (dropdown: Strategic, Enterprise, Mid-Market, SMB), Assigned CSM (people), Health Score (numbers 0-100), Health Status (status: Healthy, Watch, At Risk, Critical), Active Contracts (numbers), Contract Revenue (numbers), Machines in Fleet (numbers), Avg Machine Age (numbers in years), Parts Orders Last 12M (numbers), Parts Order Trend (status: Growing, Stable, Declining, Stopped), Last Engagement Date (date), Days Since Last Engagement (formula), NPS Score (numbers), Open Service Tickets (numbers), Payment Status (status: Current, 30 Days Late, 60+ Days Late), and Churn Risk (status: Low, Medium, High, Imminent). Groups: organize by Health Status (Healthy, Watch, At Risk, Critical). Create automations: (1) When Health Score drops below 60, change Health Status to 'At Risk' and notify Assigned CSM; (2) When Health Score drops below 30, change Health Status to 'Critical', notify CS Director, and create a 'Save Plan' item on linked board; (3) When Days Since Last Engagement exceeds 90, change to 'Watch' and create an outreach task; (4) When Parts Order Trend changes to 'Declining', add a flag and notify CSM. Add a Dashboard with: customer distribution by Health Status (pie chart), health score trend over time (line chart), top 10 at-risk accounts by revenue (table), average health score by tier (chart), and churn risk summary (numbers widgets)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Churn Sentinel
**Agent Purpose:** Detect early churn signals across the customer portfolio and orchestrate retention interventions before relationships deteriorate.

**Triggers:**
- Health score drops more than 15 points in a rolling 30-day period
- Parts ordering frequency declines 25%+ quarter-over-quarter
- Service contract expires without renewal initiation
- Customer misses two consecutive quarterly business reviews
- NPS response is detractor (0-6)

**Actions:**
- Analyze cross-data churn signals (parts, engagement, service, payment) and generate risk assessment
- Create prioritized save plans with specific actions tailored to the risk triggers
- Draft "check-in" communications that reference specific relationship milestones and value delivered
- Recommend executive sponsor engagement for strategic accounts
- Schedule QBR or site visit with proposed agenda based on identified issues
- Generate "voice of customer" report aggregating all touchpoints for CSM briefing

**Data Required:**
- Customer account data and contract history
- Parts ordering data (from ERP integration)
- Service ticket history and resolution metrics
- Engagement log (meetings, events, training attendance)
- NPS/CSAT survey responses
- Payment and AR aging data

**Autonomy Level:** Escalation-Based
Low-risk monitoring and alerting is fully automated. Save plan creation requires CSM review. Executive engagement recommendations escalated to CS leadership for approval.

**Example Interaction:**
> The Churn Sentinel detects a cluster of warning signals at TransPack Industries, a $4.2M account with 28 machines across three plants. Over the last quarter: parts orders dropped 40% (from $85K/quarter to $51K), two machines had service tickets closed as "customer declined recommended repair," and TransPack's procurement team requested a list of all spare part numbers "for internal records" — a classic signal they're sourcing parts from third-party suppliers.
>
> The agent generates a comprehensive risk report: "TransPack Industries — Churn Risk: HIGH. Primary indicators: parts revenue decline (-40% QoQ), declined repairs suggest budget constraints or dissatisfaction, parts list request suggests third-party sourcing evaluation. Estimated revenue at risk: $320K/year in aftermarket plus $1.8M in planned equipment expansion."
>
> It creates a save plan: (1) CSM to schedule urgent on-site visit within 2 weeks, (2) prepare TCO analysis showing risk of third-party parts on machine warranty and uptime, (3) propose a volume discount program for parts to counter third-party pricing, (4) escalate to VP of Sales for executive alignment on the equipment expansion opportunity. The plan is routed to the CSM and CS Director for immediate action.

---

### Use Case 5: Spare Parts Consumption & Reorder Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Spare parts are the annuity revenue stream of industrial machinery — consistent, high-margin, and predictable when managed well. But Customer Success teams often have no visibility into parts consumption patterns. When a customer's parts orders decline, it might mean the machine is running great (unlikely), they're sourcing from third parties (concerning), or they're reducing production (contextual). Conversely, a spike in parts orders could signal machine degradation that warrants a proactive service intervention. CSMs lack this intelligence because parts data lives in the ERP system, disconnected from the customer relationship context.

#### The Solution
monday.com Work Management integrated with the ERP system (SAP, Oracle, or similar) to surface parts consumption data at the customer level. Each customer's parts ordering profile is tracked with columns for: monthly parts spend, trailing 12-month trend, key consumable items (filters, belts, bearings, cutting tools), reorder alerts, and anomaly flags. Automations detect significant changes: 30%+ decline triggers a churn investigation task, 50%+ increase triggers a proactive service recommendation, and regular consumable reorders generate automated reminders to customers before they run out.

#### The Outcome
CSMs have data-driven conversations about parts and maintenance instead of generic check-ins. Proactive reorder reminders increase customer satisfaction and ensure uptime. Churn risk detection improves as declining parts orders are caught within 30 days. Parts revenue stabilizes and grows through better customer engagement.

#### Discovery Questions
1. "How visible is spare parts ordering data to your Customer Success team today?"
2. "If a customer's parts orders dropped 50% this quarter, would anyone notice — and how quickly?"
3. "Do your customers typically reorder consumable parts proactively, or do they wait until something breaks?"
4. "What percentage of your parts revenue do you estimate is lost to third-party suppliers or aftermarket alternatives?"
5. "Have you ever used parts consumption data to predict a machine failure before it happened?"

#### Industry Context
Spare parts in industrial machinery are categorized as: consumables (filters, lubricants, cutting inserts — regular replacement), wear parts (bearings, seals, belts — periodic replacement based on hours/cycles), and breakdown parts (motors, drives, controllers — replaced only on failure). OEMs typically price parts at 3-10x their manufacturing cost, creating an incentive for customers to seek alternatives. The "parts attach rate" — percentage of parts purchased from the OEM vs. third parties — is a critical metric. Companies like Sandvik and Trumpf use IoT data to offer "just-in-time" parts delivery based on actual wear, creating a competitive moat. For companies without IoT, ordering patterns are the best proxy for machine utilization and health.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Spare Parts Consumption Tracker for a machinery company's CS team. Create a board called 'Parts Consumption Monitor' with these columns: Customer Name (text), Account Tier (dropdown: Strategic, Enterprise, Mid-Market, SMB), Assigned CSM (people), Monthly Parts Spend (numbers), Trailing 12M Parts Revenue (numbers), QoQ Trend (status: Growing, Stable, Declining, Stopped), Top Consumable (text), Last Parts Order Date (date), Days Since Last Order (formula), Estimated Next Reorder (date), Anomaly Flag (status: Normal, Decline Alert, Spike Alert, No Orders), OEM Parts Attach Rate (numbers as percentage), and Action Required (status: None, Reorder Reminder, Churn Investigation, Service Recommendation). Groups: organize by Anomaly Flag (Normal, Decline Alert, Spike Alert, No Orders). Create automations: (1) When QoQ Trend changes to 'Declining', change Anomaly Flag to 'Decline Alert' and create a task for CSM; (2) When Days Since Last Order exceeds 90 for accounts with active machines, change to 'No Orders' and notify CSM; (3) When Monthly Parts Spend increases 50%+ from prior month, change to 'Spike Alert' and create service recommendation task. Add a Dashboard with: total parts revenue trend (line chart), customers by anomaly status (pie chart), top 10 declining accounts (table), parts attach rate distribution (histogram), and monthly revenue by account tier (bar chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Parts Intelligence Advisor
**Agent Purpose:** Transform spare parts consumption data into proactive customer engagement opportunities and revenue protection insights.

**Triggers:**
- Parts order received (new data from ERP integration)
- 90 days since last order for an active account
- Quarter-over-quarter decline exceeds 25%
- Consumable reorder interval exceeded (based on machine hours or calendar)
- Monthly parts revenue report generation

**Actions:**
- Analyze ordering patterns to identify consumption anomalies by customer and machine
- Generate proactive reorder reminders for consumables approaching replacement intervals
- Create churn investigation tasks when ordering patterns suggest third-party sourcing
- Recommend preventive service visits when parts consumption spikes indicate machine degradation
- Draft customer-specific parts utilization reports for QBR presentations
- Calculate and update OEM attach rate metrics per customer

**Data Required:**
- ERP parts ordering data (item, quantity, date, customer, machine serial)
- Machine specifications (consumable intervals, wear part lifecycles)
- Historical consumption baselines per machine model
- Customer account data and machine fleet information
- Third-party parts pricing benchmarks

**Autonomy Level:** Fully Autonomous (monitoring) / Human-in-the-Loop (outreach)
Data analysis, pattern detection, and internal alerting are fully automated. Customer-facing communications and churn investigations require CSM review and action.

**Example Interaction:**
> The Parts Intelligence Advisor processes the monthly order feed and flags Nordic Precision AB: their cutting insert orders for three VMC-3000 mills dropped from 240 units/quarter to 80 units. Simultaneously, their coolant filter orders remained steady — indicating the machines are still running but someone else is supplying the inserts.
>
> The agent estimates the revenue leakage at $18K/quarter ($72K annualized) and identifies the likely competitor: a third-party tooling distributor offering compatible inserts at 35% lower cost. It creates an action plan for the CSM: "Nordic Precision — cutting insert revenue declining. Recommend: (1) present TCO analysis showing OEM inserts last 22% longer per independent testing, (2) offer volume pricing tier for 200+ units/quarter at 20% discount, (3) highlight warranty implications of non-OEM consumables. Estimated save value: $72K/year."

---

### Use Case 6: Voice of Customer & NPS Program Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Industrial machinery companies know their products inside and out but often lack systematic customer feedback programs. When feedback does come, it arrives informally — through field technician conversations, trade show hallway chats, or angry phone calls. There's no structured way to capture, categorize, analyze, and act on customer sentiment. NPS surveys, when they exist, are managed via email with results sitting in a spreadsheet that nobody reviews. The result: product development doesn't hear about recurring field issues, CS doesn't know which accounts need attention, and Sales doesn't know which customers are promoters who could provide references.

#### The Solution
monday.com Work Management with WorkForms for NPS and CSAT surveys triggered at key moments: post-commissioning, post-service visit, annual relationship survey, and post-training. Survey responses flow into a "Voice of Customer" board with columns for customer, survey type, score, verbatim feedback, sentiment category (Product, Service, Support, Training, Parts), assigned owner, follow-up status, and resolution. Automations route detractors (NPS 0-6) to CSMs for immediate follow-up, flag promoters (NPS 9-10) for reference program outreach, and aggregate trends for product and service leadership.

#### The Outcome
Response rates increase 40% with automated, well-timed surveys. Detractor follow-up time drops from weeks to 24 hours. Product teams receive structured field intelligence instead of anecdotes. Reference pipeline grows as promoters are systematically identified. Customer retention improves as issues are caught and resolved faster.

#### Discovery Questions
1. "Do you currently run any structured customer feedback program — NPS, CSAT, or similar?"
2. "When a field technician hears negative feedback during a service visit, what happens with that information?"
3. "How does your product team learn about recurring field issues or feature requests from customers?"
4. "If I asked for your top 10 referenceable customers right now, could you provide that list with confidence?"
5. "What's the turnaround time from receiving negative feedback to resolving the issue and closing the loop with the customer?"

#### Industry Context
Customer feedback in industrial machinery differs significantly from B2B SaaS. The relationship spans years or decades, not months. Feedback touchpoints are less frequent but higher stakes — a negative experience during a $100K service visit carries more weight than a minor software bug. Key feedback moments include: Factory Acceptance Test (FAT), Site Acceptance Test (SAT), first production milestone, each major service intervention, and annual business reviews. Industry-specific surveys should ask about machine performance, uptime, service responsiveness, parts availability, technical support quality, and training effectiveness. Trade shows (IMTS, EMO, Hannover Messe) are critical feedback opportunities that most companies don't systematically capture.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Voice of Customer & NPS Management system for an industrial machinery company. Create a board called 'Voice of Customer' with these columns: Customer Name (text), Survey Type (dropdown: Post-Commissioning, Post-Service, Annual Review, Post-Training, Ad Hoc), NPS Score (numbers 0-10), NPS Category (status: Promoter, Passive, Detractor), Verbatim Feedback (long text), Sentiment Category (dropdown: Product Quality, Service Responsiveness, Parts Availability, Technical Support, Training, Pricing, Overall Relationship), Assigned Owner (people), Follow-Up Status (status: New, In Progress, Resolved, Closed), Resolution Notes (long text), Date Received (date), and Reference Candidate (checkbox). Groups: organize by NPS Category (Promoter, Passive, Detractor). Create automations: (1) When NPS Category is 'Detractor', notify Assigned Owner and CS Director immediately; (2) When NPS Category is 'Promoter' and Reference Candidate is checked, create item in 'Reference Pipeline' board; (3) When Follow-Up Status is 'New' for 48 hours on a Detractor, escalate to CS Director; (4) When a new response arrives, notify the Assigned CSM for the account. Add a Dashboard with: NPS distribution (pie chart), NPS trend over time (line chart), feedback by Sentiment Category (bar chart), open detractor follow-ups (table), and response rate by survey type (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Customer Voice Analyst
**Agent Purpose:** Analyze customer feedback at scale, detect emerging themes, and orchestrate closed-loop follow-up for every detractor response.

**Triggers:**
- New survey response submitted via WorkForm
- NPS score is 0-6 (detractor)
- Monthly/quarterly feedback analysis cycle
- Trade show or event feedback batch upload
- Keyword detection in verbatim feedback (e.g., "competitor," "switching," "unacceptable")

**Actions:**
- Categorize verbatim feedback by sentiment and topic using NLP analysis
- Generate detractor follow-up plans with context from account history
- Produce monthly "Voice of Customer" reports with trend analysis and emerging themes
- Identify promoters suitable for case studies, references, or user group participation
- Route product-related feedback to R&D with frequency and impact analysis
- Create executive summaries for QBR preparation using customer's own words

**Data Required:**
- Survey responses (scores and verbatim text)
- Customer account data and relationship history
- Service ticket history and resolution data
- Product roadmap for addressing reported issues
- Reference program criteria and existing reference customers

**Autonomy Level:** Fully Autonomous (analysis) / Human-in-the-Loop (follow-up actions)
Feedback categorization, trend analysis, and reporting are fully automated. Detractor follow-up plans and reference program outreach require CSM approval.

**Example Interaction:**
> After a quarterly survey cycle, the Customer Voice Analyst processes 142 responses. It identifies an emerging theme: 18% of respondents (up from 6% last quarter) mention "long wait times for technical support phone calls." Drilling deeper, the agent finds that 80% of these complaints come from customers in the Central time zone, correlating with a staffing gap during the 2-4 PM CT window when the East Coast team is winding down and the West Coast team is at lunch.
>
> The agent generates a "Voice of Customer Alert" report: "Emerging Issue — Technical Support Wait Times (Central Region). 26 customers affected, 4 are detractors, 2 are strategic accounts. Root cause hypothesis: staffing coverage gap 2-4 PM CT. Recommended actions: (1) Adjust support team scheduling to ensure coverage during gap, (2) CSMs for affected strategic accounts should proactively acknowledge the issue and communicate the fix, (3) monitor next quarter's results for improvement." The report is delivered to the CS Director and Support Operations Manager.

---

### Use Case 7: Quarterly Business Review (QBR) Automation

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
QBRs are the cornerstone of strategic customer relationships in industrial machinery, but preparing for them is a time black hole. CSMs spend 4-8 hours per QBR assembling data from multiple systems: pulling service history from the field service system, parts orders from the ERP, open tickets from the helpdesk, machine utilization data from IoT platforms, and contract details from the CRM. Then they manually create a PowerPoint deck, often copying the same template and manually updating numbers. With 15-30 QBRs per quarter per CSM, that's 60-240 hours — essentially 2-6 weeks of a CSM's quarter spent on deck preparation instead of strategic customer engagement.

#### The Solution
monday.com Work Management as the QBR command center. A "QBR Calendar" board tracks all upcoming reviews with columns for customer, date, attendees, prep status, deck status, and follow-up status. Automations pull data from connected boards (installed base, contracts, health scores, VoC) to auto-populate a QBR template. The CSM's role shifts from data assembly to insight curation — reviewing the auto-generated content, adding strategic commentary, and personalizing the narrative. Post-QBR, action items are automatically created and tracked.

#### The Outcome
QBR preparation time drops from 4-8 hours to 30-60 minutes per customer. CSMs conduct 2x more QBRs with better quality. Customers experience more data-driven, insightful reviews. Action items from QBRs are tracked to completion instead of forgotten in email threads. Strategic account coverage improves as the time barrier to QBRs is removed.

#### Discovery Questions
1. "How many QBRs does each CSM conduct per quarter, and how long does preparation take?"
2. "Where does the data for QBR presentations come from — how many systems does a CSM need to access?"
3. "After a QBR, how are action items tracked and followed up on?"
4. "Are your QBRs standardized across the team, or does each CSM have their own approach?"
5. "What percentage of your strategic accounts actually receive regular QBRs vs. what you'd like?"

#### Industry Context
In industrial machinery, QBRs (or "Business Reviews") are typically conducted with strategic accounts spending $500K+ annually or with active service contracts. The review covers: machine fleet status and utilization, service performance (response times, first-time fix rate, PM compliance), parts consumption and spend, open issues and resolutions, upcoming contract milestones, and technology roadmap updates. Unlike SaaS QBRs focused on adoption metrics, machinery QBRs center on uptime, productivity, and total cost of ownership. Key stakeholders include the customer's plant manager, maintenance director, and procurement team, alongside the supplier's CSM, service manager, and sometimes a product specialist.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a QBR Management System for an industrial machinery CS team. Create a board called 'QBR Calendar' with these columns: Customer Name (text), Account Tier (dropdown: Strategic, Enterprise, Mid-Market), QBR Date (date), QBR Quarter (dropdown: Q1, Q2, Q3, Q4), Assigned CSM (people), Prep Status (status: Not Started, Data Collection, Draft Ready, Review Complete, Presented), Customer Attendees (text), Internal Attendees (people), Key Topics (long text), Deck Link (link), Action Items Count (numbers), Follow-Up Status (status: Pending, In Progress, Complete), and Customer Satisfaction Rating (numbers 1-10). Groups: organize by quarter. Create a connected board called 'QBR Action Items' with: Action Item (text), Customer (connect to QBR Calendar), Owner (people), Due Date (date), Status (status: Open, In Progress, Complete, Overdue), Priority (status: High, Medium, Low), and Notes (long text). Automations: (1) 30 days before QBR Date, change Prep Status to 'Data Collection' and notify CSM; (2) When Prep Status changes to 'Presented', create subitems for standard follow-up tasks (Send recap, Create action items, Schedule next QBR); (3) When Action Item Due Date passes with status not 'Complete', change to 'Overdue' and notify Owner and CSM. Dashboard: upcoming QBRs this quarter (table), QBR completion rate by tier (chart), open action items by customer (chart), customer satisfaction ratings (chart), and CSM QBR workload (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** QBR Autopilot
**Agent Purpose:** Automate QBR data assembly, generate draft presentations, and ensure post-QBR action items are tracked to completion.

**Triggers:**
- QBR date is 30 days away (prep initiation)
- QBR date is 7 days away (final review reminder)
- QBR status changes to "Presented" (post-QBR workflow)
- Action item becomes overdue
- Quarterly QBR planning cycle begins

**Actions:**
- Pull customer data from installed base, contracts, health score, VoC, and parts boards to generate a QBR data package
- Draft QBR narrative sections: fleet summary, service performance, value delivered, recommendations, and roadmap
- Generate comparison metrics (this quarter vs. last quarter, vs. benchmark)
- Create post-QBR action items from meeting notes
- Send QBR recap email to customer attendees with action items and next steps
- Schedule the next QBR based on account tier cadence (Strategic: monthly, Enterprise: quarterly, Mid-Market: semi-annually)

**Data Required:**
- All connected boards (installed base, contracts, health scores, VoC, parts consumption)
- Service performance metrics (response time, first-time fix rate, PM compliance)
- Previous QBR notes and action items for comparison
- Product roadmap highlights relevant to the customer's fleet
- Industry benchmark data for contextualizing performance

**Autonomy Level:** Human-in-the-Loop
Data assembly and draft generation are automated. CSM reviews, customizes narrative, and adds strategic insights before presentation. Post-QBR action item creation from notes is automated but requires CSM validation.

**Example Interaction:**
> It's 30 days before the Q1 QBR with Hartwell Automotive. The QBR Autopilot pulls data across all systems and generates a comprehensive draft. Fleet summary: 45 machines across 3 plants, average age 4.2 years, fleet health score 78/100 (up from 72 last quarter). Service performance: 97% PM compliance (target: 95%), average emergency response time 3.8 hours (SLA: 4 hours), 2 warranty claims processed. Parts consumption: $125K this quarter ($118K last quarter, +6%). Customer health score: 82 (stable).
>
> The agent identifies two key talking points: (1) Hartwell's Plant 3 has three machines approaching their 5-year major overhaul milestone — estimated investment $180K, and (2) Hartwell's NPS score improved from 7 to 9 after resolving the calibration issue reported last quarter. It drafts a slide narrative: "Q1 highlights: Your fleet health improved 8% quarter-over-quarter, driven by our preventive maintenance program achieving 97% compliance. Looking ahead, we recommend planning the 5-year overhauls at Plant 3 to maintain this trajectory — let's discuss timing and budget."
>
> The CSM reviews the draft, adds context about Hartwell's upcoming production expansion plans (learned from a recent conversation), and presents a polished, data-rich QBR in half the usual preparation time.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Installed Base | The total number of machines/equipment a company has sold and deployed in the field |
| Commissioning | The process of verifying that installed equipment operates to specification |
| FAT (Factory Acceptance Test) | Testing performed at the manufacturer's facility before shipment |
| SAT (Site Acceptance Test) | Testing performed at the customer's facility after installation |
| PM (Preventive Maintenance) | Scheduled maintenance to prevent equipment failure |
| MTBF (Mean Time Between Failures) | Average time between machine breakdowns — key reliability metric |
| MTTR (Mean Time To Repair) | Average time to restore a machine to operation after failure |
| OEE (Overall Equipment Effectiveness) | Composite metric of availability × performance × quality |
| Aftermarket | Revenue from parts, service, and upgrades after the initial equipment sale |
| Attach Rate | Percentage of new equipment sales that include a service contract |
| Consumables | Parts that require regular replacement (filters, lubricants, cutting tools) |
| Wear Parts | Components that degrade over time (bearings, seals, belts) |
| TCO (Total Cost of Ownership) | Full lifecycle cost including purchase, operation, maintenance, and disposal |
| Uptime | Percentage of time a machine is operational and available for production |
| First-Time Fix Rate | Percentage of service calls resolved on the first visit |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/Director of Customer Success | Owns retention, expansion, and customer health metrics | Decision-maker |
| Customer Success Manager | Day-to-day account management, renewals, QBRs | Influencer / User |
| Field Service Manager | Oversees technician dispatch, service delivery, PM programs | Influencer |
| Aftermarket Sales Manager | Drives parts and service contract revenue | Decision-maker (aftermarket) |
| Parts Operations Manager | Manages parts inventory, pricing, and fulfillment | User |
| Director of Service Operations | Owns service P&L, SLAs, and operational efficiency | Decision-maker |
| VP of Sales | Owns new equipment revenue but cares about reference customers | Influencer |
| Plant Manager (Customer Side) | Owns production output, cares about uptime and TCO | Champion / Decision-maker |
| Maintenance Director (Customer Side) | Manages all equipment maintenance at the facility | Key User / Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales | CS provides account intelligence and expansion signals to Sales; warm handoffs for new equipment opportunities | Cross-sell new equipment based on fleet aging data |
| Field Service/Engineering | CS coordinates service delivery and captures field intelligence for customer health | Unified service + CS view improves customer experience |
| Parts & Aftermarket | CS monitors parts consumption as a health indicator; Parts team fulfills orders | Joint parts + service contract bundling |
| Product & R&D | CS channels field feedback and feature requests to product teams | Customer-informed product roadmap |
| Marketing | CS identifies reference customers, case study candidates, and user group participants | Customer advocacy and reference programs |
| Finance | CS forecasts renewal revenue; Finance tracks aftermarket P&L | Accurate recurring revenue forecasting |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce Service Cloud | Enterprise service management, often used for case/ticket management | monday.com offers simpler setup, better visual workflows; many machinery companies find Salesforce overbuilt for their CS needs |
| SAP CS/PM Modules | Integrated with ERP for service and plant maintenance | SAP modules are rigid and expensive to customize; monday.com provides a flexible customer-facing layer on top of SAP data |
| ServiceMax (PTC) | Field service management for equipment-centric companies | Focused on dispatch/work orders, not customer health; monday.com complements or replaces the CS layer |
| Gainsight | SaaS-oriented customer success platform | Designed for digital/SaaS; poor fit for industrial machinery's physical asset and field service model |
| Spreadsheets/Email | Default "tool" for most mid-market machinery CS teams | monday.com replaces the spreadsheet chaos with structured, automated workflows |
| HubSpot Service Hub | Growing in mid-market for service management | Less capable for complex asset tracking; monday.com's flexibility wins for equipment-centric workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "Our ERP (SAP/Oracle) already handles customer data" | ERP is your system of record for transactions, but it's not designed for proactive customer engagement. monday.com sits on top as your system of action — turning ERP data into CSM workflows, health scores, and automated outreach. |
| "Our CSMs prefer personal relationships over systems" | Absolutely — and the best CSMs should spend time building relationships, not assembling spreadsheets. monday.com frees up 10+ hours per week per CSM by automating data collection and prep work, so they can invest that time in the relationships that matter. |
| "We're too small to need a CS platform" | If you have more than 50 active customers and any aftermarket revenue, you're already losing money to missed renewals and reactive service. Companies your size typically find $200K-$500K in aftermarket revenue they're leaving on the table. |
| "We tried CRM before and adoption was low" | CRM adoption fails when the tool adds work without adding value. monday.com is different — automations reduce manual data entry, visual dashboards give CSMs instant portfolio visibility, and the interface is intuitive enough that teams adopt it within days, not months. |
| "We need something purpose-built for industrial equipment" | Purpose-built tools like ServiceMax are great for dispatch but terrible for the strategic CS layer. monday.com's flexibility lets you build exactly the workflows your team needs — installed base tracking, renewal pipelines, health scoring — without being locked into someone else's rigid process. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for industrial machinery Customer Success references]
- [Placeholder for aftermarket revenue growth case study]
- [Placeholder for renewal rate improvement metrics]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
