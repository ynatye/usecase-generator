# Electricity, Oil & Gas × Customer Success Playbook

## Overview

Customer Success in the electricity, oil & gas sector operates at the intersection of complex service delivery, regulatory obligations, and long-term relationship management. For utilities, "customers" range from residential ratepayers and commercial accounts to large industrial consumers and municipalities. For oil & gas companies, "customers" include refineries, petrochemical plants, trading counterparties, government fuel purchasers, and retail fuel distributors. The definition of "success" varies dramatically: utilities must manage regulated service obligations, rate cases, and customer satisfaction scores that influence regulatory proceedings, while oil & gas companies manage contract compliance, product quality specs, and supply reliability for mission-critical energy deliveries.

Customer Success departments in energy companies typically range from 15-100+ people depending on segment. Utility customer success teams handle everything from key account management for C&I (commercial and industrial) customers, to demand-side management (DSM) program enrollment, to outage communications, to billing dispute resolution. Oil & gas customer success teams focus on contract management, supply reliability, product quality assurance, logistics coordination, and commercial relationship development. Both segments face a transformational moment: the energy transition is reshaping customer expectations, creating new product categories (renewable energy credits, carbon offsets, EV charging, distributed energy), and requiring CS teams to become trusted energy advisors rather than transactional account managers.

The regulatory dimension is unique to this industry. Utility customer satisfaction metrics (J.D. Power scores, PSC complaint rates) can directly influence rate case outcomes — regulators may deny rate increases if customer service is poor. Oil & gas supply contracts often have force majeure clauses, quality specifications (API gravity, sulfur content, BTU content), and delivery obligations that, if breached, trigger significant financial penalties. Customer Success must navigate these contractual and regulatory constraints while building relationships that drive retention, upsell, and advocacy in an increasingly competitive energy marketplace.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Energy transition creates dozens of new products/programs to manage per customer, but CS headcount is flat — teams must handle 3× the complexity |
| 2 | Consolidate Tech Stack with AI | High | Customer data lives across CIS (Customer Information Systems), OMS (Outage Management), billing, CRM, and field service — CS teams toggle between 6+ systems |
| 3 | Replace or Radically Augment Headcount | Medium-High | Key account management for top industrial customers requires deep analysis that currently consumes senior CS managers' time — AI can handle data synthesis |

## Prioritized Use Cases

---

### Use Case 1: Key Account Health Monitoring & Risk Detection

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies' top 50-200 accounts often represent 40-70% of revenue. For utilities, losing a major industrial customer to a competitive retail energy provider (in deregulated markets) or to on-site generation/microgrids can mean millions in lost revenue. For oil & gas suppliers, a key refinery customer switching feedstock suppliers can cost $50-200M annually. Yet CS teams typically monitor account health through quarterly business reviews and gut feel — they discover dissatisfaction when the customer is already evaluating alternatives or has filed a regulatory complaint.

#### The Solution
monday.com CRM + Work Management for a unified account health scoring system. Each key account gets a dedicated board with health score components: contract compliance (delivery performance, quality scores), engagement metrics (meeting frequency, executive sponsor contact, event attendance), financial trends (volume trends, payment patterns, margin trajectory), satisfaction signals (survey scores, complaint history, NPS), and strategic alignment (participation in new programs, pilot willingness). Automations trigger alerts when composite health scores drop below thresholds. Dashboard views give CS leadership a portfolio-level view of account health distribution.

#### The Outcome
6-month early warning on at-risk accounts (vs. discovering at contract renewal). 15% improvement in key account retention rates. Proactive intervention saves 2-3 accounts annually worth $10-50M each. CS managers spend time on strategy, not data gathering.

#### Discovery Questions
- How do you currently assess the health of your top accounts — is there a formal scoring model or is it relationship-based?
- When was the last time you were surprised by a key account leaving or significantly reducing volume?
- What signals would you look for if you could monitor account health in real-time?
- How do you track engagement touchpoints (meetings, calls, events) across your key accounts?
- In deregulated markets, how do you compete against retail energy providers or on-site generation alternatives?

#### Industry Context
In deregulated electricity markets (Texas ERCOT, PJM, NYISO), C&I customers can switch retail providers relatively easily — contract terms are typically 1-3 years. In regulated markets, large industrial customers increasingly invest in on-site generation, microgrids, or pursue "direct access" options. Oil & gas supply contracts may be 1-10 years with annual volume commitments and price adjustment mechanisms (index-based, formula-based). J.D. Power Business Electric Utility Satisfaction Study benchmarks utility CS performance. Customer switching in deregulated gas markets is measured by state PUCs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Key Account Health Dashboard board. Columns: Account Name (text), Account Tier (dropdown: Platinum, Gold, Silver), Industry Segment (dropdown: Manufacturing, Government/Municipal, Commercial Real Estate, Retail Chain, Data Center, Refinery, Petrochemical, Pipeline, Distributor), Annual Revenue USD (numbers), Contract Expiration (date), Account Manager (people), Executive Sponsor (people), Delivery Performance Score 0-100 (numbers), Quality Score 0-100 (numbers), Engagement Score 0-100 (numbers), Financial Health Score 0-100 (numbers), Satisfaction Score 0-100 (numbers), Composite Health Score (formula: average of all scores), Health Status (status: Healthy, Watch, At Risk, Critical, Champion), Last QBR Date (date), Next QBR Due (date), Open Issues Count (numbers), Active Programs (text), Renewal Probability % (numbers). Add subitems for individual health score change events with date and notes. Dashboard with: health distribution donut chart, at-risk accounts table sorted by revenue, composite health trend by quarter, renewal timeline with health color coding, revenue at risk numbers widget. Automations: when Composite Health Score drops below 60, change Health Status to At Risk and notify CS Director; when Contract Expiration is within 180 days and Health Status is not Healthy or Champion, create renewal risk item and notify VP Sales; when Last QBR Date is more than 100 days ago, send reminder to Account Manager."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Account Pulse Monitor
**Agent Purpose:** Continuously synthesize signals from across the business to maintain real-time account health scores and surface early warning indicators.

**Triggers:**
- When any account health component score is updated
- When a customer complaint or service ticket is created
- When delivery or quality data is updated from operations systems
- Daily scan for engagement decay (no touchpoints in 30+ days)
- When contract enters 12-month renewal window

**Actions:**
- Recalculate composite health score and flag significant changes (>10 point drop)
- Analyze patterns across health components to identify root cause of decline
- Generate account intelligence briefs before scheduled QBRs (key metrics, trends, talking points, risk areas)
- Recommend specific intervention actions based on which health components are declining
- Create proactive outreach tasks when engagement scores decay
- Surface cross-sell opportunities when health scores are strong and contract renewal is approaching

**Data Required:**
- CRM activity logs (meetings, emails, calls)
- Billing and volume data from CIS
- Delivery and quality records from operations
- Customer satisfaction surveys and NPS data
- Complaint and service ticket history
- Contract terms and renewal dates

**Autonomy Level:** Human-in-the-Loop
Health score calculations and trend analysis are fully autonomous. Alert generation is automatic. Recommended actions and outreach suggestions require CS manager review and approval before execution. QBR briefing documents are auto-generated but reviewed by the account manager before the meeting.

**Example Interaction:**
> The Account Pulse Monitor detects that MidWest Plastics (Platinum account, $18M annual revenue, contract expires in 8 months) has experienced a 22-point drop in composite health score over 60 days. Breaking down the components: Delivery Performance dropped from 94 to 78 (three late deliveries of natural gas liquids in January), Engagement Score dropped from 85 to 55 (no executive touchpoints since November, missed the last scheduled QBR), and Satisfaction Score dropped from 80 to 65 (two unresolved billing disputes). The agent generates an alert: "🚨 MidWest Plastics — CRITICAL. Revenue at risk: $18M. Root cause analysis: delivery failures triggered dissatisfaction, compounded by engagement gap and unresolved billing issues. Recommended actions: (1) Schedule executive apology call within 48 hours — delivery VP + CS Director, (2) Expedite billing dispute resolution — escalate to billing supervisor, (3) Offer dedicated logistics coordinator for next 90 days, (4) Schedule QBR within 2 weeks with custom reliability improvement plan. Renewal risk: HIGH without immediate intervention."

---

### Use Case 2: Contract Lifecycle & Compliance Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy contracts are among the most complex commercial agreements in any industry. A single gas supply contract may include volume commitments (take-or-pay clauses), price adjustment mechanisms (Henry Hub index + basis differential + transport adder), quality specifications (BTU content, H2S limits, moisture content), delivery point obligations, force majeure provisions, credit/collateral requirements, and regulatory compliance clauses. Utilities have tariff-based agreements with regulatory riders, demand response commitments, and renewable energy credit obligations. CS teams are responsible for ensuring compliance on both sides — yet contract details often live in legal's document management system, disconnected from the operational reality of daily delivery and service.

#### The Solution
monday.com Work Management + CRM for contract lifecycle management. Each contract is an item with key commercial terms extracted into structured columns. Subitems track individual obligations (volume commitments, quality specs, reporting requirements). Automations monitor compliance: flag when delivered volumes fall below take-or-pay minimums, alert when quality test results approach specification limits, remind when periodic reporting is due. Timeline views show contract expirations across the portfolio. Connected boards link contracts to account health boards and billing systems.

#### The Outcome
Zero missed contractual obligations. 40% reduction in contract disputes through proactive compliance monitoring. 3-month earlier start on renewal negotiations (instead of scrambling at expiration). Clear visibility into portfolio-level exposure (total take-or-pay obligations, weighted average contract duration, expiration clustering).

#### Discovery Questions
- Where do your contract terms live today, and how does the CS team access them during day-to-day account management?
- Have you ever had a contract dispute that could have been prevented with better monitoring?
- How do you track take-or-pay or minimum volume commitment compliance throughout the contract year?
- What's your process for initiating renewal negotiations, and how far in advance do you typically start?
- How do you handle mid-contract price adjustments or index resets?

#### Industry Context
Take-or-pay clauses in gas supply contracts typically require the buyer to purchase 80-90% of contracted volumes or pay a penalty. Basis differentials (the price difference between Henry Hub and the delivery point) can swing $0.50-$2.00/MMBtu and significantly impact contract economics. Quality specifications vary by end use — pipeline quality gas has different specs than LNG feedstock or petrochemical feedstock. FERC (Federal Energy Regulatory Commission) regulates interstate gas transport tariffs. Power Purchase Agreements (PPAs) for renewables have unique structures (fixed price, escalating price, merchant tail).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Contract Lifecycle Manager board. Columns: Contract Name (text), Account (connect board: Key Accounts), Contract Type (dropdown: Gas Supply, Power Purchase Agreement, Fuel Supply, Transport/Capacity, Retail Energy, Demand Response, Renewable Energy Credits, Storage, NGL Supply), Status (status: Draft, In Negotiation, Active, Expiring Soon, Expired, Terminated, Renewed), Effective Date (date), Expiration Date (date), Auto-Renewal (checkbox), Notice Period Days (numbers), Annual Volume Commitment (numbers), Volume Unit (dropdown: MMBtu, MWh, Barrels, Gallons, Tonnes), Price Mechanism (dropdown: Fixed, Index + Basis, Formula, Market, Regulated Tariff), Take-or-Pay % (numbers), YTD Volume Delivered (numbers), YTD Compliance % (formula: YTD Volume / pro-rated commitment × 100), Contract Value Annual USD (numbers), Quality Specs (long text), Key Obligations (long text), Account Manager (people), Legal Contact (people), Risk Rating (status: Low, Medium, High). Add subitems for individual obligations with due dates and compliance status. Dashboard: expiring contracts timeline (next 12 months), take-or-pay compliance gauge by contract, total portfolio value, contract type distribution, risk rating breakdown. Automations: when Expiration Date is within 180 days, change Status to Expiring Soon and notify Account Manager + Legal; when YTD Compliance % drops below Take-or-Pay %, alert Account Manager; monthly on the 15th, send portfolio compliance summary to VP Commercial."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Contract Compliance Watchdog
**Agent Purpose:** Monitor all active contracts for compliance risks and alert CS teams before obligations are missed.

**Triggers:**
- When delivery/volume data is updated (daily or weekly feed)
- When quality test results are recorded
- When a periodic reporting obligation comes due
- When contract enters notice period window for auto-renewal decisions
- Monthly portfolio compliance review

**Actions:**
- Calculate running compliance percentage against volume commitments and project end-of-year position
- Flag quality test results within 10% of specification limits (early warning before breach)
- Generate compliance scorecards for each contract showing obligations met/at-risk/missed
- Alert when auto-renewal deadline approaches with a recommendation (renew, renegotiate, terminate)
- Identify contracts where actual pricing has diverged significantly from market (opportunity to renegotiate)
- Create renewal preparation packages with historical performance data, pricing analysis, and recommended terms

**Data Required:**
- Contract terms database
- Delivery and volume tracking data (from SCADA, nomination systems, or billing)
- Quality test results from lab/field
- Market pricing data (Henry Hub, power indices, commodity benchmarks)
- Historical contract performance

**Autonomy Level:** Human-in-the-Loop
Compliance calculations and alerts are fully autonomous. Renewal recommendations are generated but require commercial manager approval. Any external communication (to customer or legal) must be human-initiated. Auto-renewal decisions always require explicit human confirmation.

**Example Interaction:**
> The Contract Compliance Watchdog reviews the Gulf Coast Petrochemical gas supply contract (36-month term, 500,000 MMBtu/month take-or-pay at 85%). Through month 8, the customer has only taken 78% of committed volumes on average. The agent calculates: "At current pace, Gulf Coast Petrochem will finish the year at 78% vs. 85% take-or-pay threshold. Projected shortfall: 420,000 MMBtu. Estimated deficiency payment: $1.26M at contract price of $3.00/MMBtu. However, the customer's Q4 seasonal pattern typically increases 15-20% — if Q4 hits 90%, annual compliance reaches 82.5%, still 2.5% short. Recommend: (1) Schedule commercial review with Gulf Coast procurement team, (2) Offer Q3-Q4 volume flexibility package to help them optimize inventory, (3) Consider proposing a contract amendment reducing annual commitment by 5% in exchange for 2-year extension. Early intervention preserves the $18M annual relationship."

---

### Use Case 3: Customer Onboarding & Service Activation

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Onboarding a new commercial or industrial energy customer is a multi-week, multi-department process. For utilities: new service applications, meter installation, rate schedule selection, demand response enrollment, billing setup, and IT system provisioning. For oil & gas suppliers: credit approval, contract execution, logistics setup (pipeline nominations, truck scheduling, terminal access), quality specifications alignment, invoicing configuration, and emergency contact protocols. CS teams coordinate across 5-8 departments, manually tracking progress in email and spreadsheets. Delays frustrate customers and push back revenue recognition. For large accounts, poor onboarding sets a negative tone for the entire relationship.

#### The Solution
monday.com Work Management for standardized onboarding workflows. Template boards for each customer type (residential, commercial, industrial, wholesale) with pre-populated tasks, dependencies, and SLA timelines. Each department's tasks are assigned to the right team with clear due dates. Automations advance the workflow when predecessor tasks complete. Customer-facing Forms collect required information upfront. Status updates flow to the Account Manager and customer automatically. Dashboard views show onboarding pipeline, average cycle time, and bottleneck identification.

#### The Outcome
40% reduction in onboarding cycle time. Zero dropped handoffs between departments. Customer visibility into their onboarding progress builds trust from day one. Standardized process ensures nothing is missed (reducing billing errors and service issues in the first 90 days).

#### Discovery Questions
- What's your current average time to onboard a new commercial/industrial customer?
- Where do handoff failures most commonly occur during onboarding?
- How does the customer experience the onboarding process — do they have visibility into progress?
- What percentage of billing issues in the first 90 days are caused by onboarding errors?
- How do you handle onboarding for customers with complex multi-site or multi-product requirements?

#### Industry Context
Utility service activation is regulated — there are mandated timelines for meter installation and service connection. ERCOT market onboarding for retail electric providers involves Electronic Data Interchange (EDI) transactions (814 enrollment, 867 usage data). Gas nominations require coordination with interstate pipelines (Nomination Cycles: Timely, Evening, Intraday). Large industrial customers may require load studies, transformer upgrades, and interconnection agreements that can take months. Credit review for wholesale energy customers involves ISDA Master Agreements and credit annexes.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Customer Onboarding Workflow board. Columns: Customer Name (text), Account Type (dropdown: Residential, Small Commercial, Large Commercial, Industrial, Wholesale, Retail Energy), Service Type (dropdown: Electric, Natural Gas, NGL, Crude Oil, Refined Products, Renewable Energy, Multi-Commodity), Onboarding Stage (status: Intake, Credit Review, Contract Execution, System Setup, Logistics Configuration, Meter/Connection, Testing & Validation, Go-Live, Post-Go-Live Review), Start Date (date), Target Go-Live (date), Actual Go-Live (date), Cycle Time Days (formula: Actual Go-Live - Start Date), Account Manager (people), Onboarding Coordinator (people), Priority (status: Standard, Expedited, Strategic), Blockers (text), Customer Satisfaction (dropdown: Very Satisfied, Satisfied, Neutral, Dissatisfied, Not Surveyed). Create groups for each onboarding stage. Add subitems for each task within the stage: Credit application submitted, Credit approved, Contract drafted, Contract signed, CIS account created, Billing configured, Pipeline nominations set up, Terminal access provisioned, Emergency contacts registered, First delivery scheduled, 30-day check-in, 90-day review. Dashboard: onboarding pipeline by stage (funnel), average cycle time trend, active onboardings by Account Manager workload, blocked items table, customer satisfaction distribution. Automations: when all subitems in a stage are done, advance Onboarding Stage to next status; when a subitem is overdue by 2+ days, notify the Onboarding Coordinator; when Onboarding Stage changes to Go-Live, send welcome email template to customer; 30 days after Go-Live, create 30-day check-in task for Account Manager."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Onboarding Accelerator
**Agent Purpose:** Proactively identify and resolve onboarding bottlenecks to ensure every customer hits their target go-live date.

**Triggers:**
- When a new customer onboarding item is created
- When any subtask becomes overdue
- When a blocker is added to an onboarding item
- Daily scan of all active onboardings for risk assessment
- When Onboarding Stage changes

**Actions:**
- Assess onboarding risk by comparing current progress to target timeline and flagging items falling behind
- Identify the critical path and highlight which tasks are blocking go-live
- Send personalized nudges to task owners when their items are approaching deadline
- Recommend task resequencing when dependencies allow parallel execution
- Generate weekly onboarding status reports for CS leadership
- Create post-mortem analysis after go-live comparing actual vs. planned timelines by task

**Data Required:**
- Onboarding board with all tasks and dependencies
- Historical onboarding data for benchmarking (average duration per task by customer type)
- Team member availability/workload
- Customer communication preferences

**Autonomy Level:** Human-in-the-Loop
Risk assessments and internal nudges are automatic. Customer-facing communications require Account Manager approval. Escalation to department heads for blocked tasks is automatic after 48 hours. Post-mortem reports are auto-generated but reviewed by Onboarding Coordinator before distribution.

**Example Interaction:**
> The Onboarding Accelerator reviews the onboarding for Apex Chemical Corp (Industrial customer, $6M annual contract, target go-live March 15). It's February 19 and the onboarding is in "Logistics Configuration" stage, but credit review took 12 days instead of the planned 5 (due to complex ISDA negotiation). Pipeline nominations haven't started yet (normally takes 10 business days). The agent calculates: "Apex Chemical is 7 days behind schedule. Critical path: Pipeline nominations (10 days) + Testing (3 days) = 13 business days minimum = March 10 at earliest if nominations start today. Target go-live March 15 is achievable but has zero buffer. Risk: MEDIUM. Actions taken: (1) Sent priority notification to Pipeline Scheduling team with all required nomination data pre-populated, (2) Scheduled testing resources for March 10-12, (3) Alerted Account Manager that March 15 go-live requires nominations to begin by EOD today. Recommendation: inform customer of potential 3-5 day delay as contingency to manage expectations."

---

### Use Case 4: Energy Transition Product & Program Enrollment

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The energy transition is creating a proliferation of new products and programs that CS teams must sell into and manage: renewable energy programs (green tariffs, community solar), demand response/demand flexibility, EV charging solutions, energy efficiency rebates, distributed energy resource (DER) interconnection, battery storage programs, carbon offset products, and renewable energy certificates (RECs). Each has unique eligibility requirements, enrollment processes, and ongoing management needs. CS teams were built to manage traditional energy supply — now they're expected to be consultative advisors across a dozen new product categories without additional headcount.

#### The Solution
monday.com CRM + Work Management for energy transition product management. A product catalog board defines all available programs with eligibility criteria, enrollment processes, and value propositions. Account boards track which customers are enrolled in which programs, their participation status, and upsell opportunities. Automations match customer profiles (usage patterns, facility type, location) to eligible programs and create outreach recommendations. Dashboard views show program enrollment rates, revenue from new products, and CS team effectiveness by program.

#### The Outcome
3× increase in energy transition program enrollment. Each CS manager effectively sells and manages 12+ products instead of 3-4. $2-5M in new product revenue from proactive matching. Customers view the company as a trusted energy transition partner, increasing retention.

#### Discovery Questions
- How many energy transition products or programs do you currently offer to commercial/industrial customers?
- How do CS teams currently identify which customers are good candidates for which programs?
- What's your enrollment rate for programs like demand response or renewable energy — and where do customers drop off?
- Are your CS teams compensated or measured on energy transition product adoption?
- How do you train CS teams on the technical details of new programs quickly enough to sell them?

#### Industry Context
Green tariffs allow large customers to procure renewable energy through their utility (Google, Microsoft, Amazon have all used these). Community solar programs are growing rapidly in states with enabling legislation. FERC Order 2222 opens wholesale markets to DER aggregations. Demand response programs (PJM, ISO-NE, CAISO) pay customers to reduce load during peak events — participation requires enrollment, baseline calculation, and performance measurement. RECs and carbon offset markets add complexity with vintage, certification (Green-e), and additionality requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Energy Transition Program Manager board. Columns: Account Name (connect board: Key Accounts), Program (dropdown: Green Tariff, Community Solar, Demand Response, EV Charging, Energy Efficiency Rebates, DER Interconnection, Battery Storage, Carbon Offsets, REC Purchases, Microgrid, Virtual PPA), Eligibility Status (status: Eligible, Pre-Qualified, Enrolled, Active Participant, Opted Out, Ineligible), Enrollment Date (date), Annual Program Value USD (numbers), Customer Facility Type (dropdown: Office, Manufacturing, Warehouse, Data Center, Retail, Hospital, Campus, Multi-Site), Peak Demand kW (numbers), Annual Usage MWh (numbers), Account Manager (people), Enrollment Stage (status: Identified, Outreach, Proposal Sent, Under Review, Signed, Onboarding, Active, Renewal), Program Performance (status: Exceeding, On Track, Below Target, At Risk), Notes (long text). Add subitems for enrollment tasks (eligibility verification, proposal creation, contract execution, technical setup, first event/delivery). Dashboard: enrollment funnel by program, program revenue by type, account coverage heat map (accounts × programs), CS team performance by enrollment count, program adoption rate trends. Automations: when a new account is added to Key Accounts board, auto-check eligibility against all programs and create recommended outreach items; when Enrollment Stage changes to Active, schedule 30-day performance review; when Program Performance drops to At Risk, notify Account Manager and Program Director."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Energy Transition Matchmaker
**Agent Purpose:** Automatically match customer profiles to eligible energy transition programs and generate personalized recommendations.

**Triggers:**
- When a new customer is added or customer profile data is updated
- When a new program is launched or eligibility criteria change
- Quarterly portfolio review of all accounts for new opportunities
- When a customer expresses interest in sustainability (captured in meeting notes or CRM)

**Actions:**
- Analyze customer profile (usage, facility type, location, peak demand, sustainability goals) against all program eligibility criteria
- Generate personalized program recommendation packages with ROI estimates
- Create outreach tasks for CS managers with talking points and customer-specific value props
- Track program adoption across the portfolio and identify underserved segments
- Recommend optimal program bundles (e.g., demand response + EV charging + green tariff for large commercial)
- Flag regulatory deadlines that affect program eligibility (e.g., community solar enrollment windows)

**Data Required:**
- Customer profile data (usage, demand, facility type, location)
- Program catalog with eligibility criteria and economics
- Utility rate schedules for ROI calculations
- Market pricing for RECs, carbon offsets, demand response
- Regulatory calendar for enrollment windows

**Autonomy Level:** Human-in-the-Loop
Eligibility matching and recommendation generation are automatic. ROI estimates are generated but flagged as "preliminary — verify with customer data." Outreach to customers requires CS manager review and initiation. Program enrollment decisions always require customer and CS manager confirmation.

**Example Interaction:**
> The Energy Transition Matchmaker runs its quarterly scan and identifies that Consolidated Distribution Centers (Gold account, 12 warehouse locations across Texas and Oklahoma, 45,000 MWh annual usage, 8.2 MW peak demand) is currently enrolled only in the green tariff program but is eligible for 4 additional programs. The agent creates a recommendation package: "Consolidated Distribution — Untapped Opportunity: $340K annual value. (1) Demand Response: 8 sites in ERCOT qualify for 4CP demand response — estimated $180K/year in transmission cost savings. (2) EV Charging: 6 sites have fleet vehicles transitioning to EV per their 2025 sustainability report — managed charging program eligible. (3) Energy Efficiency: Lighting retrofit rebates available for 4 older facilities — estimated $85K in rebates + $120K annual savings. (4) Battery Storage: 2 sites with high demand charges qualify for peak shaving — estimated $75K annual savings with 7-year payback." The package is assigned to the Account Manager with suggested outreach timing before the next QBR.

---

### Use Case 5: Outage & Service Disruption Communication Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
When a pipeline ruptures, a refinery has an unplanned shutdown, a power plant trips offline, or a winter storm causes widespread outages, Customer Success teams become the frontline of crisis communications. They must quickly identify which customers are affected, assess impact severity, communicate proactively (before customers call to complain), provide estimated restoration times, coordinate with operations on real-time status, and manage the post-event follow-up. For utilities, state public utility commissions track outage communication performance and penalize poor response. For oil & gas, supply disruptions can trigger force majeure notices and contract penalty clauses. Yet most CS teams manage disruption communications through email chains and frantic phone calls.

#### The Solution
monday.com Work Management for structured disruption response. When an event occurs, a template board is instantiated with all affected customers auto-populated (connected from the account/contract boards). Columns track impact severity, communication status, customer response, and resolution. Automations trigger initial notifications to affected customers based on impact level. Timeline views show escalation paths. Post-event, the board becomes the basis for root cause analysis, customer follow-up, and contract compliance documentation (force majeure notices, delivery shortfall tracking).

#### The Outcome
90% of affected customers receive proactive notification before they call in. Average customer response time reduced from hours to minutes. Complete documentation trail for regulatory and contractual compliance. Post-event customer satisfaction scores improve 30%+ through professional communication management.

#### Discovery Questions
- How do you currently identify which customers are affected when a supply disruption or outage occurs?
- What's your average time from event detection to customer notification?
- How do you handle the coordination between operations (who knows what's happening) and CS (who talks to customers)?
- Have you faced regulatory scrutiny or contract penalties due to communication failures during disruptions?
- What does your post-event customer recovery process look like?

#### Industry Context
NERC reliability standards require utilities to report certain outage events. State PUCs measure SAIDI (System Average Interruption Duration Index) and SAIFI (System Average Interruption Frequency Index). The 2021 Texas Winter Storm Uri exposed massive communication failures — customers had no information for days. Oil & gas force majeure declarations require specific contractual processes and timelines. Pipeline SCADA systems detect disruptions in real-time but data rarely flows to CS systems automatically. PHMSA (Pipeline and Hazardous Materials Safety Administration) requires specific notification protocols for pipeline incidents.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Service Disruption Response board. Columns: Event Name (text), Event Type (dropdown: Planned Outage, Unplanned Outage, Supply Disruption, Quality Issue, Pipeline Incident, Weather Event, Cyber Incident, Force Majeure), Severity (status: Minor, Moderate, Major, Critical), Start Time (date with time), Estimated Resolution (date with time), Actual Resolution (date with time), Affected Area/System (text), Total Affected Customers (numbers), Customer Name (connect board: Key Accounts), Impact Level (dropdown: Full Interruption, Partial Reduction, Quality Degradation, Delayed Delivery, Financial Impact Only), Communication Status (status: Not Notified, Initial Notice Sent, Update Sent, Resolution Notice Sent, Follow-Up Complete), Customer Response (status: No Response, Acknowledged, Concerned, Escalated, Complaint Filed, Regulatory Notice), Revenue Impact USD (numbers), Force Majeure Applicable (checkbox), Account Manager (people), Ops Liaison (people), Notes (long text). Add subitems for each communication touchpoint (timestamp, channel, message, response). Dashboard: active events map, affected customer count, communication completion rate, average notification time, customer sentiment distribution, post-event follow-up queue. Automations: when new event is created with Severity Critical, immediately notify all Account Managers for affected accounts; when Estimated Resolution is updated, auto-send update to all customers with Communication Status not Follow-Up Complete; when Actual Resolution is logged, create post-event review task for each affected account; when Force Majeure Applicable is checked, create legal notification task with 24-hour deadline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Disruption Response Commander
**Agent Purpose:** Orchestrate customer communications during service disruptions, ensuring every affected customer is notified promptly and consistently.

**Triggers:**
- When a new disruption event is created
- When event severity is escalated
- When estimated resolution time is updated by operations
- Every 2 hours during active Critical/Major events
- When event is resolved

**Actions:**
- Auto-identify all affected customers based on event location/system and populate the response board
- Prioritize customer notification order by account tier and impact severity
- Generate tailored notification messages for each impact level (template + specific details)
- Track notification delivery and flag customers who haven't been reached after 30 minutes
- Compile real-time status reports for CS leadership showing communication coverage
- Generate force majeure notification drafts for legal review when applicable
- Create post-event customer recovery plan with timeline and assigned follow-up actions

**Data Required:**
- Customer-to-infrastructure mapping (which customers are on which pipeline/circuit/system)
- Account contact information and preferred communication channels
- Contract terms for affected customers (force majeure clauses, SLAs)
- Operations real-time status feeds
- Historical disruption data for pattern analysis

**Autonomy Level:** Escalation-Based
Customer identification and notification drafting are automatic. Initial notifications for non-Critical events can be sent autonomously. Critical event communications, force majeure declarations, and regulatory notifications require human approval. Post-event recovery plans are auto-generated but require CS Director review.

**Example Interaction:**
> A compressor station failure on the Katy-Beaumont pipeline segment is detected at 2:14 PM. The Disruption Response Commander immediately queries the infrastructure mapping and identifies 14 affected customers (3 Platinum, 5 Gold, 6 Silver) receiving natural gas through this segment. Within 3 minutes, it generates tailored notifications: Platinum accounts receive a direct call script for their Account Manager ("Apex Refining — full supply interruption expected 6-12 hours. Alternative supply from Eagle Ford lateral may be available in 4 hours. Ops team deploying portable compression."), Gold accounts receive detailed email notifications, Silver accounts receive SMS + email. It creates the response board, sets 2-hour update cadence, and flags two contracts with force majeure notice requirements (24-hour contractual deadline). By 2:20 PM — 6 minutes after detection — all 14 customers have tailored notifications queued, 3 Platinum account managers have been called, and legal has received force majeure draft notices.

---

### Use Case 6: Voice of Customer (VOC) & Feedback Loop Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies collect customer feedback from multiple channels: J.D. Power surveys, internal CSAT/NPS surveys, regulatory complaint filings (PUC complaints), billing inquiries, field service feedback, QBR notes, social media, and direct account manager observations. But this feedback rarely gets synthesized into actionable intelligence. Survey results go to marketing, complaints go to legal, QBR notes stay in the account manager's head, and PUC filings trigger reactive firefighting. Nobody has the full picture of what customers actually think, and systemic issues persist because feedback loops are broken.

#### The Solution
monday.com Work Management as the VOC aggregation and action platform. All feedback channels feed into a central board where each piece of feedback is categorized by theme (billing, reliability, communication, pricing, new products, service quality), sentiment, customer tier, and region. Automations route feedback to the appropriate department for action. Dashboard views show trending themes, sentiment trends, and resolution rates. Connected boards link feedback to specific account health scores and product improvement backlogs.

#### The Outcome
Systemic issues identified 60% faster through pattern recognition. Customer feedback directly drives product/service improvements with clear traceability. PUC complaint rate decreases 25% through proactive issue resolution. Account managers have complete feedback history before every customer interaction.

#### Discovery Questions
- How many channels do you currently collect customer feedback from, and where does it all end up?
- Can you quickly tell me the top 3 complaints from your largest customers over the past 6 months?
- How does customer feedback influence product development or service improvement decisions?
- What's your process when a customer files a PUC complaint — is it reactive or do you see it coming?
- How do you close the loop with customers who provide feedback?

#### Industry Context
J.D. Power utility satisfaction studies are industry benchmarks — scores influence brand perception and regulatory relationships. PUC complaint rates are publicly reported and tracked by regulators. In deregulated markets, customer satisfaction directly affects churn. NPS benchmarks for utilities are typically 15-35 (low compared to other industries). The American Customer Satisfaction Index (ACSI) ranks utilities among the lowest-scoring industries. Voice of Customer programs are increasingly mandated by utility regulators as part of rate case proceedings.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Voice of Customer Hub board. Columns: Feedback ID (auto-number), Customer Name (connect board: Key Accounts), Feedback Source (dropdown: NPS Survey, CSAT Survey, J.D. Power, PUC Complaint, Billing Inquiry, QBR Notes, Social Media, Email, Phone Call, Field Service, Executive Escalation), Date Received (date), Theme (dropdown: Billing Accuracy, Pricing, Reliability, Outage Communication, Customer Service, New Products, Contract Terms, Sustainability Programs, Digital Experience, Field Service Quality), Sentiment (status: Very Positive, Positive, Neutral, Negative, Very Negative), Verbatim (long text), NPS Score (numbers), Account Tier (mirror from connected account), Region (dropdown), Action Required (status: No Action, Under Review, Action Planned, In Progress, Resolved, Closed), Action Owner (people), Resolution Notes (long text), Days to Resolution (formula). Dashboard: sentiment trend by month, theme distribution bar chart, top issues by frequency, NPS trend, PUC complaint count, resolution time distribution, feedback by source. Automations: when Sentiment is Very Negative and Account Tier is Platinum or Gold, immediately notify CS Director; when Theme is PUC Complaint, create linked item in regulatory response board with 48-hour deadline; when 10+ items share the same Theme in 30 days with Negative sentiment, create systemic issue alert."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Customer Insight Synthesizer
**Agent Purpose:** Analyze incoming customer feedback to detect patterns, generate insights, and recommend systemic improvements.

**Triggers:**
- When new feedback items are added
- Weekly pattern analysis across all feedback
- When a feedback theme exceeds a frequency threshold (10+ in 30 days)
- Monthly executive insight report generation
- When NPS drops below threshold for any segment

**Actions:**
- Categorize incoming feedback by theme and sentiment automatically (NLP analysis of verbatim text)
- Identify emerging patterns (e.g., billing complaints spike after rate change, reliability concerns cluster in specific region)
- Generate root cause hypotheses with supporting data
- Create systemic improvement recommendations linked to specific feedback clusters
- Produce monthly "Customer Voice" executive reports with trends, insights, and recommended actions
- Close the feedback loop by generating personalized follow-up messages for resolved issues

**Data Required:**
- All feedback board data
- Account profile and history data
- Billing and service records for context
- Historical feedback data for trend comparison
- Industry benchmark data (J.D. Power, ACSI)

**Autonomy Level:** Human-in-the-Loop
Feedback categorization and pattern detection are automatic. Insight reports are auto-generated for CS Director review. Systemic improvement recommendations require management approval before action. Customer follow-up messages are drafted but require CS manager review before sending.

**Example Interaction:**
> The Customer Insight Synthesizer detects a pattern: 23 negative feedback items in the past 3 weeks all mention "estimated bills" or "meter reading" issues, concentrated in the Southwest region. Cross-referencing with billing data, it finds that a smart meter firmware update in the region caused 340 meters to stop transmitting reads, forcing the billing system to generate estimated bills for 2 consecutive months. The agent creates a systemic issue alert: "Root Cause Identified: SW Region Smart Meter Firmware Issue → Estimated Bills → Customer Dissatisfaction. Scope: 340 accounts, 23 complaints (6.8% complaint rate — 4× normal). Impact: $12K in estimated billing adjustments likely needed. Recommended Actions: (1) IT to prioritize firmware patch — ETA? (2) Proactive outreach to all 340 affected accounts before next billing cycle, (3) Auto-credit $25 billing adjustment for affected accounts, (4) Monitor for PUC complaint filings. Customer message draft: 'We identified a technical issue that caused your recent bills to be estimated. The issue has been resolved, and your next bill will reflect actual usage. We've applied a $25 credit for the inconvenience.'"

---

### Use Case 7: Customer Energy Analytics & Advisory Platform

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Large energy customers increasingly expect their supplier to be an energy advisor, not just a commodity provider. They want usage analytics, cost optimization recommendations, benchmark comparisons against similar facilities, peak demand management strategies, and energy transition roadmaps. But CS teams don't have the tools or time to generate customized analytics for each account. Energy consultants charge $50-200K for the analysis that CS teams should be providing as a value-added service to retain and grow key accounts. Without advisory capabilities, energy companies compete solely on price — a race to the bottom.

#### The Solution
monday.com Work Management + Dashboards as the customer advisory delivery platform. Each key account has an analytics board with usage trends, cost breakdown, demand profile, efficiency benchmarks, and optimization recommendations. Templates standardize the analysis framework while allowing customization. Subitems track recommended actions and customer adoption. Quarterly analytics packages are generated semi-automatically and delivered through QBRs. Dashboard views help CS teams identify which accounts would benefit most from advisory engagement.

#### The Outcome
CS conversations shift from reactive service to proactive advisory — increasing customer stickiness. Key account retention improves 20% as customers value the strategic partnership. Advisory services create upsell pipeline for energy transition products. CS team positioned as trusted energy advisors, not commodity account managers.

#### Discovery Questions
- What analytics or insights do your largest customers ask for most frequently?
- Do you currently provide energy advisory services, or is that outsourced to consultants?
- How would your CS team's role change if they could deliver data-driven insights at every customer interaction?
- What would it mean for retention if customers saw you as their strategic energy advisor?
- How do you currently benchmark customer usage against industry peers or efficient facilities?

#### Industry Context
Energy-as-a-Service (EaaS) models are emerging where the energy company provides holistic energy management, not just commodity supply. Utility key account programs at companies like Duke Energy, Exelon, and Southern Company include dedicated engineering support for large C&I customers. In oil & gas, Chevron and BP's commercial teams provide market intelligence and hedging advisory to key customers. The DOE's Better Buildings program provides benchmarking data. ENERGY STAR Portfolio Manager is the standard for commercial building energy benchmarking.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Customer Energy Advisory board. Columns: Account Name (connect board: Key Accounts), Facility Name (text), Facility Type (dropdown: Office, Manufacturing, Warehouse, Data Center, Retail, Hospital, Campus, Refinery, Processing Plant), Annual Usage MWh or MMBtu (numbers), Annual Energy Cost USD (numbers), Cost per Unit (formula), Energy Use Intensity (numbers with label kBtu/sqft or equivalent), Industry Benchmark (numbers), Performance vs Benchmark % (formula), Peak Demand kW (numbers), Load Factor % (numbers), Top Recommendation (text), Estimated Annual Savings USD (numbers), Recommendation Status (status: Identified, Presented, Accepted, In Progress, Implemented, Declined), Advisory Engagement (status: Not Started, Initial Analysis, QBR Delivered, Ongoing Monitoring, Champion), Account Manager (people), Last Analysis Date (date). Add subitems for individual recommendations (rate optimization, demand management, efficiency measures, renewable procurement, contract restructuring). Dashboard: total savings opportunity pipeline, implementation success rate, customer engagement by tier, savings delivered vs. identified, advisory engagement funnel. Automations: quarterly, flag accounts where Last Analysis Date is >100 days for refresh; when Estimated Annual Savings exceeds $50K and Recommendation Status is Identified, prioritize for next QBR; when Recommendation Status changes to Implemented, update savings counter and notify CS Director."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Energy Advisory Analyst
**Agent Purpose:** Generate personalized energy analytics and optimization recommendations for key accounts, enabling CS teams to deliver consultative value.

**Triggers:**
- When new usage data is loaded for an account (monthly or quarterly)
- When an account's QBR is scheduled (14 days before)
- When energy market prices change significantly (>15% from baseline)
- When a customer's usage pattern changes notably (>20% month-over-month)

**Actions:**
- Generate facility-level energy profiles with usage trends, demand patterns, and cost breakdowns
- Benchmark performance against industry averages and identify efficiency gaps
- Produce customized recommendation packages (rate optimization, demand management, efficiency, renewables)
- Calculate ROI for each recommendation with payback periods
- Draft QBR presentation slides with data, insights, and recommendations
- Alert when market conditions create time-sensitive opportunities (e.g., favorable PPA pricing, demand response event revenue)

**Data Required:**
- Customer usage data (interval data preferred, monthly minimum)
- Utility rate schedules and tariff structures
- Industry benchmarking databases
- Market pricing data (wholesale energy, RECs, demand response)
- Facility characteristics (square footage, operating hours, equipment)

**Autonomy Level:** Human-in-the-Loop
Analysis generation and benchmarking are automatic. Recommendation packages are generated for CS manager review and customization before customer delivery. Market opportunity alerts are sent to CS managers for evaluation. All customer-facing materials require human review.

**Example Interaction:**
> Ahead of the Q1 QBR with DataVault Hosting (Platinum account, 5 data center facilities, $4.2M annual energy spend), the Energy Advisory Analyst generates a comprehensive package: "DataVault Q1 Advisory Summary: (1) Facility DC-3 in Dallas is operating at PUE 1.82, 22% above industry best practice (1.5). Root cause analysis suggests cooling inefficiency — recommend hot/cold aisle containment retrofit. Estimated savings: $340K/year, 14-month payback. (2) Current ERCOT retail contract expires in 6 months — wholesale forward prices are 18% below the current contract rate. Recommend early renewal negotiation or switch to indexed pricing. Potential savings: $630K/year. (3) DC-1 and DC-2 have suitable rooftop area for 2.4 MW combined solar — with current ITC incentives, estimated payback of 6 years and $380K/year savings thereafter. (4) All 5 facilities qualify for ERCOT 4CP demand response — estimated transmission savings of $520K/year. Total opportunity: $1.87M in annual savings — a 44% reduction in energy cost." The package is formatted as a QBR deck draft and assigned to the Account Manager for review 7 days before the meeting.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| C&I | Commercial and Industrial — large non-residential energy customers |
| CIS | Customer Information System — utility billing and account management platform |
| OMS | Outage Management System — tracks and manages power outages |
| SAIDI | System Average Interruption Duration Index — utility reliability metric |
| SAIFI | System Average Interruption Frequency Index — utility reliability metric |
| Take-or-Pay | Contract clause requiring minimum volume purchase or penalty payment |
| Basis Differential | Price difference between a reference hub and a delivery point |
| Henry Hub | Primary US natural gas pricing benchmark (Louisiana) |
| ERCOT | Electric Reliability Council of Texas — Texas power grid operator |
| 4CP | Four Coincident Peak — ERCOT demand charge methodology |
| Force Majeure | Contractual clause excusing performance during extraordinary events |
| PUC/PSC | Public Utility Commission / Public Service Commission — state regulators |
| PPA | Power Purchase Agreement — long-term renewable energy contract |
| REC | Renewable Energy Certificate — tradable proof of renewable generation |
| NGL | Natural Gas Liquids — ethane, propane, butane extracted from natural gas |
| API Gravity | Oil density measurement — higher = lighter/more valuable |
| MMBtu | Million British Thermal Units — standard natural gas pricing unit |
| PUE | Power Usage Effectiveness — data center efficiency metric |
| EaaS | Energy-as-a-Service — holistic energy management business model |
| ISDA | International Swaps and Derivatives Association — standard contract framework |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/Director of Customer Success | Strategy, team management, key account oversight | Decision-maker |
| Key Account Manager | Relationship management for top-tier customers | Influencer / Champion |
| Commercial/Contract Manager | Contract negotiations, pricing, commercial terms | Decision-maker |
| Director of Customer Operations | Service delivery, billing, operational customer touchpoints | Influencer |
| Energy Advisor/Consultant | Technical analysis, energy optimization recommendations | User |
| Customer Service Manager | Contact center operations, complaint resolution | User |
| VP Commercial/Sales | Revenue targets, growth strategy, new product go-to-market | Decision-maker |
| Regulatory Affairs Manager | PUC relations, compliance, rate case preparation | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales | Pipeline handoff, account expansion, new product go-to-market | CRM for unified customer lifecycle management |
| Operations | Supply reliability, outage management, field service | Operational dashboards, customer-facing status portals |
| Finance | Revenue forecasting, billing, credit management | Financial workflow automation, billing dispute resolution |
| Legal | Contract management, regulatory compliance, force majeure | Contract lifecycle management |
| Marketing | Customer communications, program promotion, brand management | Campaign management, customer segmentation |
| IT | System integrations (CIS, OMS, SCADA), digital customer experience | Integration hub, portal development |
| Sustainability | Energy transition products, carbon reporting, stakeholder comms | Program management, customer advisory content |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce Energy & Utilities Cloud | CRM + industry-specific modules | Expensive, complex implementation. monday.com CRM + Work Management delivers faster with more flexibility for unique energy workflows |
| SAP CRM / S/4HANA | Integrated with utility billing/ERP | Requires massive SAP ecosystem buy-in. monday.com works alongside SAP for workflow and CS orchestration |
| Oracle Utilities (CCB/C2M) | Customer care and billing | Core billing system, not a CS workflow tool. monday.com adds the work management layer Oracle lacks |
| Microsoft Dynamics 365 | General CRM with some utility customizations | Good CRM but weak on work management and energy-specific workflows. monday.com's board flexibility wins |
| Gainsight | Customer success platform | Built for SaaS, not energy. Lacks industry-specific features and the work management depth energy CS needs |
| Spreadsheets + Email | The status quo for most energy CS teams | Direct displacement — the most common "competitor" |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We have Salesforce/SAP for customer management" | Those handle CRM records — but where does the actual work of managing customers happen? The QBR prep, disruption coordination, onboarding tasks, program enrollment? That's what monday.com orchestrates. |
| "Our CIS is the system of record for customers" | Absolutely — and it should remain so. monday.com doesn't replace CIS; it's the work management layer where CS teams coordinate all the activities that CIS can't handle. |
| "Energy customer management is too specialized" | That's exactly why you need a flexible platform. Rigid industry tools can't adapt to energy transition products, new regulations, or changing customer expectations. monday.com adapts as fast as your market changes. |
| "Our CS team is too small for a platform investment" | Small CS teams can't afford inefficiency. Every hour saved from manual tracking is an hour spent on customer relationships. AI agents multiply your team's capacity for advisory and proactive management. |
| "We need integrations with our SCADA/OMS/billing systems" | monday.com's API and integration framework connects to any system with an API. We regularly integrate with utility-specific platforms — the flexibility means you're not locked into one vendor's ecosystem. |

## Proof Points
*(To be populated with customer references)*
- [Utility using monday.com for key account management]
- [Energy company managing customer onboarding workflows]
- [Power company coordinating outage communications]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
