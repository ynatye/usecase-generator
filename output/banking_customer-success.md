# Banking × Customer Success Playbook

## Overview

Customer Success in banking is a rapidly evolving function that sits at the intersection of relationship management, digital adoption, and revenue retention. Unlike SaaS-native Customer Success teams, banking CS functions often emerge from — or coexist with — traditional relationship management, client services, and account management structures. The function is responsible for ensuring clients (retail, commercial, or institutional) derive maximum value from the bank's product suite, driving adoption of digital channels, reducing churn, and identifying expansion opportunities.

In commercial and corporate banking, Customer Success teams typically manage portfolios of 50-200 clients per manager, tracking product utilization across treasury management, trade finance, lending, payments, and increasingly, digital banking platforms. Retail banking CS is more technology-driven, focusing on digital adoption metrics, NPS, complaint resolution workflows, and lifecycle marketing orchestration. The challenge is unique to banking: heavy regulation (KYC/AML, fair lending, privacy), product complexity (dozens of interconnected products with interdependencies), and legacy technology (core banking systems from the 1990s that make data extraction painful).

The strategic importance of Customer Success in banking has surged as competition intensifies from fintechs, neobanks, and big tech. Client acquisition costs in commercial banking average $3,000-$10,000 per relationship; in institutional banking, onboarding alone can cost $50,000+. Retention economics make Customer Success the highest-ROI function, yet most banks invest 10x more in sales than in post-sale client experience. The teams that do exist are often hamstrung by fragmented data across core banking, CRM, digital banking, and call center systems — spending more time assembling client views than actually engaging clients.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | CS teams managing 150+ client relationships each need automation to move from reactive to proactive engagement |
| 2 | Consolidate Tech Stack with AI | High | Client health data scattered across 6-10 systems (core banking, CRM, digital banking, call center, trade platform, treasury portal) |
| 3 | Replace or Radically Augment Headcount | Medium-High | AI can handle routine health checks, usage monitoring, and alert generation — freeing CSMs for strategic conversations |

## Prioritized Use Cases

---

### Use Case 1: Client Health Scoring & Early Warning System

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most banking CS teams discover client dissatisfaction when the client issues an RFP to competitors or moves a product to another bank — by then, it's too late. The signals were there: declining transaction volumes, reduced digital login frequency, increased support tickets, delayed fee payments, or failure to adopt new products after onboarding. But these signals live in separate systems: transaction data in the core banking platform, digital engagement in the online banking analytics tool, support tickets in ServiceNow, relationship notes in Salesforce. No single person or system connects these dots. The typical commercial banking CS team loses 8-12% of relationships annually, with 60% of departing clients showing warning signs 6-9 months before leaving.

#### The Solution
monday.com Work Management creates a unified Client Health Dashboard. A master board tracks each client relationship with columns: Client Name (text), Segment (dropdown: Large Corporate, Mid-Market, Small Business, Private Banking, Institutional), Relationship Manager (people), CS Manager (people), Products Active (dropdown multi-select: Treasury Management, Trade Finance, Commercial Lending, Payments/Cash Management, FX, Deposits, Cards, Digital Banking), Revenue TTM (numbers), Revenue Trend (dropdown: Growing >10%, Stable, Declining <10%, Declining >10%), Product Utilization Score (numbers 0-100), Digital Adoption Score (numbers 0-100), Support Ticket Trend (dropdown: Decreasing, Stable, Increasing, Spike), NPS/CSAT Score (numbers), Last Strategic Review Date (date), Health Status (status: Thriving, Healthy, Watch, At Risk, Critical), Risk Factors (long text), Action Plan (subitems with tasks, owners, and due dates). Automations trigger alerts when health indicators cross thresholds and create intervention workflows.

#### The Outcome
50% reduction in unexpected client attrition through early warning detection. Average 4.2-month advance warning before at-risk clients take action. 15% increase in client product adoption through proactive engagement triggered by health signals. CS team capacity effectively doubled through automated monitoring replacing manual health checks.

#### Discovery Questions
- How do you currently identify which client relationships are at risk, and how far in advance do you typically detect attrition signals?
- If I asked you right now which 20 clients are most likely to reduce their relationship in the next 6 months, how confident would you be in that list — and how long would it take to produce?
- How many systems does a CS manager need to access to build a complete picture of a single client's health?
- What's your current client attrition rate, and what percentage of departing clients showed warning signs that were missed or detected too late?
- Do your Relationship Managers and CS Managers share the same view of client health, or do they sometimes have conflicting assessments?

#### Industry Context
"Share of wallet" is the key banking metric — a client might use your bank for treasury management but a competitor for FX. Declining share of wallet often precedes full relationship loss. "Product penetration" (average products per client) correlates strongly with retention: clients with 4+ products have <5% annual attrition vs. 15%+ for single-product clients. "RFP risk" — when a client issues a formal request for proposal to competitors — is the most visible churn signal but by then win-back rates are only 30-40%.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Client Health Scoring Dashboard for a banking Customer Success team. Create a board called 'Client Health Monitor' with columns: Client Name (text), Client ID (text), Segment (dropdown: Large Corporate >$500M Revenue, Upper Mid-Market $100-500M, Lower Mid-Market $25-100M, Small Business <$25M, Private Banking, Institutional/FI), Industry (dropdown: Technology, Healthcare, Manufacturing, Energy, Real Estate, Retail, Financial Services, Professional Services, Other), Relationship Manager (people), CS Manager (people), Relationship Tier (dropdown: Platinum, Gold, Silver, Bronze), Active Products (dropdown multi-select: Treasury Management, Cash Management, Commercial Lending, Trade Finance, FX & Derivatives, Merchant Services, Commercial Cards, Deposits, Digital Banking Platform, Payroll, Escrow, Letters of Credit), Product Count (formula counting Active Products), Total Revenue TTM $K (numbers), Revenue vs Prior Year % (numbers), Product Utilization Score 0-100 (numbers), Digital Adoption Score 0-100 (numbers), Monthly Transaction Volume (numbers), Transaction Volume Trend (dropdown: Growing >15%, Growing 5-15%, Stable, Declining 5-15%, Declining >15%), Open Support Cases (numbers), CSAT Score (numbers), NPS Score (numbers), Last QBR Date (date), Days Since Last QBR (formula), Next QBR Scheduled (date), Contract Renewal Date (date), Days to Renewal (formula), Health Score (formula combining weighted factors), Health Status (status: Thriving, Healthy, Needs Attention, At Risk, Critical), Risk Factors (long text), Competitive Threat (dropdown: None Known, RFP Issued, Competitor Mentioned, Active Evaluation), Last Engagement Date (date), Engagement Frequency (dropdown: Weekly, Bi-Weekly, Monthly, Quarterly, Infrequent). Add subitems for action plans: Task (text), Owner (people), Due Date (date), Priority (status: Urgent, High, Medium), Status (status: To Do, In Progress, Done). Add automations: when Health Score drops below 50, change Health Status to 'At Risk' and notify CS Manager and RM. When Days Since Last QBR exceeds 120 and Segment is 'Large Corporate' or 'Upper Mid-Market', create action item 'Schedule QBR' and notify CS Manager. When Competitive Threat changes to 'RFP Issued' or 'Active Evaluation', change Health Status to 'Critical' and notify CS Manager, RM, and board owner immediately. When Revenue vs Prior Year % is less than -10, change Transaction Volume Trend consideration and notify CS Manager. Create Dashboard with: health distribution pie chart, at-risk clients table (filtered by Health Status), revenue at risk (sum of At Risk + Critical client revenue), QBR compliance tracker, product penetration by segment bar chart, and monthly health trend chart. Add Kanban view grouped by Health Status. Add Table view sorted by Health Score ascending (worst first) for triage meetings."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Client Health Sentinel
**Agent Purpose:** Continuously monitor client health indicators, detect early warning signals, and generate proactive intervention recommendations.

**Triggers:**
- Daily: scan for health score changes across all clients
- When any single health indicator crosses a predefined threshold (e.g., transaction volume drops >20% MoM)
- When support ticket count for a client exceeds 3 in a 30-day window
- When a client hasn't logged into digital banking for 30+ days
- Weekly on Monday: generate CS team priority list for the week
- 90 days before Contract Renewal Date

**Actions:**
- Calculate composite health scores using weighted indicators (revenue trend 30%, product utilization 25%, digital adoption 15%, support trend 15%, engagement recency 15%)
- Generate natural-language health alerts with specific diagnosis: "Acme Corp health declined from 72 to 58 this month. Primary drivers: (1) FX transaction volume down 35% — likely lost wallet share to competitor, (2) Two escalated support tickets on treasury platform connectivity"
- Create pre-populated action plan subitems with recommended interventions based on risk type (e.g., product disengagement → schedule product training; competitive threat → executive sponsor outreach)
- Produce weekly "Client Triage" briefing ranking the 10 clients needing most attention with specific recommended actions
- Generate renewal risk assessments 90 days out with win/loss probability and recommended retention strategy
- Track intervention effectiveness: did health scores improve after actions were taken?

**Data Required:**
- Core banking system (balances, transaction volumes, product holdings)
- Digital banking analytics (login frequency, feature adoption, session duration)
- CRM (relationship notes, meeting history, opportunity pipeline)
- Support ticketing system (ticket count, severity, resolution time, CSAT)
- Revenue/billing data (fees, interest income, FX revenue by client)

**Autonomy Level:** Escalation-Based
Health score calculation and alert generation are fully autonomous. Action plan recommendations are generated automatically but require CSM review before execution. Executive-level escalations (Critical status clients) are auto-routed to CS leadership with context but require human judgment on response.

**Example Interaction:**
> Monday morning, the Client Health Sentinel generates the weekly triage briefing for CSM Sarah Chen's portfolio of 120 commercial banking clients. "Priority 1: Meridian Manufacturing (Health: 45, down from 68). Three red flags detected: (a) Treasury management transaction volume declined 40% over 60 days — consistent with partial migration to another provider, (b) CFO declined last two QBR invitations, (c) New support escalation about API connectivity for their ERP integration. Recommended actions: (1) RM to schedule executive check-in with CFO — suggest discussing their upcoming acquisition and how our expanded capabilities could support integration, (2) Fast-track the API issue — assign senior technical resource, target resolution within 48 hours, (3) Prepare competitive analysis: if they're evaluating JP Morgan Treasury Services, highlight our superior API developer portal and real-time reporting. Priority 2: TechVenture Partners (Health: 52, stable but low). Single-product client (deposits only, $12M). Renewal in 87 days. Revenue potential: $180K annually if we capture their treasury management and FX needs. Recommended: Schedule product discovery session focused on their international expansion plans (mentioned in last RM call notes)."

---

### Use Case 2: Client Onboarding & Time-to-Value Orchestration

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking client onboarding is notoriously complex and slow. A commercial banking relationship can take 45-90 days to fully onboard due to KYC/AML requirements, credit underwriting, legal documentation, product setup across multiple systems, user provisioning for digital platforms, and training. The process involves 8-15 internal teams (KYC, Credit, Legal, Operations, Treasury Sales, Product Specialists, IT, Training) with dozens of handoffs. Clients frequently experience "onboarding fatigue" — by the time they're fully set up, initial enthusiasm has waned, key contacts have changed, and competitors have had months to counter-sell. Studies show that 30% of revenue leakage in commercial banking occurs during the first 12 months due to incomplete product activation.

#### The Solution
monday.com Work Management creates a structured onboarding orchestration system. A board template for each new client includes phases (groups): Pre-Onboarding, KYC & Compliance, Legal & Documentation, Product Setup, Technical Integration, Training & Enablement, Go-Live, and 90-Day Value Realization. Each phase contains specific tasks with columns: Task Name (text), Owner Team (dropdown: KYC, Credit, Legal, Ops, Treasury Ops, IT, Product, Training, CS), Assigned To (people), Predecessor Task (dependency), SLA Days (numbers), Start Date (date), Due Date (date), Status (status: Not Started, In Progress, Blocked, Complete), Blocker Description (long text), Client Action Required (checkbox), Client Contact (text), Documentation (files). A master "Onboarding Pipeline" board aggregates all active onboardings with health indicators. Automations trigger next-phase tasks when predecessors complete, escalate SLA breaches, and notify clients of required actions.

#### The Outcome
35% reduction in onboarding cycle time (from 75 days average to 49 days). 90% SLA compliance across internal teams (up from 62%). Client satisfaction with onboarding process improved from 3.2 to 4.5 (out of 5). 25% increase in first-year product activation rates through structured "time-to-value" tracking.

#### Discovery Questions
- What's your average commercial client onboarding time from signed agreement to full product activation, and how does that compare to your clients' expectations?
- Where are the biggest bottlenecks in your onboarding process — is it KYC, legal documentation, technical setup, or something else?
- How do you currently track onboarding progress across the 10+ internal teams involved, and how does the client experience the process?
- What percentage of products included in the initial deal are actually activated within the first 90 days?
- Have you ever lost revenue or a client relationship due to a poor onboarding experience?

#### Industry Context
KYC (Know Your Customer) requirements add 15-30 days to onboarding for corporate clients due to beneficial ownership verification, sanctions screening, and enhanced due diligence for high-risk clients. "Time-to-revenue" — how quickly a new client generates fee income — is a critical metric but rarely tracked systematically. The "implementation gap" (products sold but not activated) averages 20-35% in commercial banking. Fintechs and neobanks advertise same-day onboarding, creating pressure on traditional banks even in segments where regulatory requirements make this impossible.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Banking Client Onboarding Orchestrator. Create a board template called 'Client Onboarding - [Client Name]' with 8 groups representing phases: 1-Pre-Onboarding, 2-KYC & Compliance, 3-Legal & Documentation, 4-Product Setup, 5-Technical Integration, 6-Training & Enablement, 7-Go-Live, 8-90-Day Value Realization. In Group 1 (Pre-Onboarding), add items: Welcome Call Scheduled, Stakeholder Map Completed, Product Scope Confirmed, Onboarding Timeline Agreed, Internal Kickoff Completed. In Group 2 (KYC & Compliance): KYC Documentation Collected, Beneficial Ownership Verified, Sanctions Screening Complete, Risk Rating Assigned, Enhanced Due Diligence (if required), Compliance Approval Obtained. In Group 3 (Legal): Master Agreement Drafted, Legal Review Complete, Client Legal Review, Agreement Executed, Board Resolutions Collected. In Group 4 (Product Setup): each product as a subitem - Treasury Management Setup, Cash Management Accounts Opened, Digital Banking Platform Provisioned, Card Program Configured, Trade Finance Facilities Established, FX Trading Limits Set. In Group 5 (Technical Integration): API Credentials Issued, ERP Integration Configured, File Format Testing, Connectivity Testing, UAT Sign-Off. In Group 6 (Training): Admin User Training Scheduled, End User Training Delivered, Self-Service Resources Shared, Training Feedback Collected. In Group 7 (Go-Live): Production Cutover, First Transaction Verified, Client Go-Live Confirmation, Post-Go-Live Support Period. In Group 8 (90-Day): 30-Day Check-In, Product Utilization Review, 60-Day Health Check, Additional Product Discovery, 90-Day QBR Scheduled. All items have columns: Owner Team (dropdown: KYC, Credit, Legal, Operations, Treasury Ops, IT, Product Specialist, Training, Customer Success), Assigned To (people), SLA Days (numbers), Start Date (date), Due Date (date), Status (status: Not Started, In Progress, Blocked, Waiting on Client, Complete), Blocker (long text), Client Action Required (checkbox), Priority (dropdown: Critical Path, Standard, Nice-to-Have), Notes (long text), Documents (files). Add dependency connections between phases. Add automations: when all items in a group are 'Complete', notify CS Manager that phase is done and trigger next phase start dates. When any item is 'Blocked' for more than 2 business days, escalate to board owner. When Status is 'Waiting on Client' for more than 5 days, send reminder notification. Create a second board called 'Onboarding Pipeline' with one item per active onboarding: Client Name (text), Segment (dropdown), Products (dropdown multi-select), Onboarding Start Date (date), Target Go-Live Date (date), Current Phase (status: Pre-Onboarding, KYC, Legal, Product Setup, Tech Integration, Training, Go-Live, Post-Go-Live), Overall Health (status: On Track, Minor Delays, At Risk, Critical), Days Elapsed (formula), Days Remaining (formula), Blocked Items Count (numbers), CS Manager (people), RM (people), Expected Annual Revenue $K (numbers). Dashboard on Pipeline board: active onboardings by phase (funnel chart), average cycle time trend (line chart), SLA compliance by team (bar chart), blocked items requiring attention (table), and revenue pending activation (number widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Onboarding Orchestrator
**Agent Purpose:** Automate onboarding workflow progression, proactively identify bottlenecks, communicate status to clients, and ensure time-to-value targets are met.

**Triggers:**
- When a new client onboarding board is created from template
- When any task status changes
- Daily at 9 AM: scan all active onboardings for blockers and SLA risks
- When a task has been "In Progress" for longer than its SLA Days
- When all tasks in a phase are complete (trigger next phase)
- Weekly on Friday: generate client-facing status update

**Actions:**
- Auto-populate onboarding timeline based on product mix and client segment (Large Corporate = longer KYC SLA, Small Business = streamlined)
- Send daily internal digest to CS Manager: "3 active onboardings. Meridian Corp: KYC phase, on track. TechVenture: Legal phase, 2 days behind — Agreement execution awaiting client CFO signature. GlobalRetail: Product Setup, blocked — Treasury ops team hasn't provisioned cash management accounts (3 days overdue, SLA = 5 days)."
- Generate client-facing weekly status emails with professional formatting: completed milestones, current activities, upcoming client actions needed, and projected go-live date
- Predict go-live date slippage based on current velocity and historical patterns, adjusting timeline proactively
- Flag when critical path items are at risk and recommend resource reallocation or parallel processing options
- Post-go-live: auto-schedule 30/60/90-day check-in meetings and create agenda items based on product utilization data

**Data Required:**
- Onboarding board task data and status history
- Historical onboarding cycle times by segment and product mix (for prediction)
- Client contact information for automated communications
- Team capacity data for resource recommendations
- Product activation data from core banking (for post-go-live tracking)

**Autonomy Level:** Human-in-the-Loop
Workflow progression, reminder notifications, and internal digests are autonomous. Client-facing communications require CSM review before sending. Timeline adjustment recommendations require CSM approval. Escalations to senior leadership require CSM confirmation.

**Example Interaction:**
> The Onboarding Orchestrator detects that TechVenture Partners' onboarding has been in the Legal phase for 12 days (SLA: 10 days). It diagnoses the blocker: "Master Agreement execution pending — sent to client legal team 8 days ago, no response. Client contact: James Wong, Associate GC. This is the second follow-up needed." It drafts a professional follow-up email for the CSM to review: "Dear James, Following up on the Master Banking Agreement sent on Feb 7th. We're eager to move forward with TechVenture's treasury management setup — our team has completed all compliance and credit approvals and is ready to begin product configuration as soon as the agreement is executed. Would it be helpful to schedule a brief call to address any outstanding questions? We're targeting a March 15th go-live, and moving forward this week would keep us on track." It simultaneously alerts the RM: "Consider having your executive sponsor (their CEO, met at the initial pitch) nudge their legal team. Pattern match: 65% of legal delays >10 days resolve faster with executive-level engagement."

---

### Use Case 3: Quarterly Business Review (QBR) Preparation & Execution

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Quarterly Business Reviews are the cornerstone of commercial banking client relationships, yet preparing for them is a manual nightmare. A CSM preparing for a QBR typically spends 4-6 hours per client: pulling transaction data from the core banking system, extracting digital utilization metrics from the online banking platform, reviewing support ticket history in ServiceNow, checking product adoption status across multiple systems, gathering market intelligence, and assembling everything into a PowerPoint deck. With 15-25 QBRs per quarter, this consumes 60-150 hours — time that could be spent on strategic client engagement. The result is often a backward-looking data dump rather than a forward-looking strategic conversation.

#### The Solution
monday.com Work Management creates a QBR lifecycle board. Each QBR is tracked with columns: Client Name (text), Quarter (dropdown), QBR Date (date), CS Manager (people), RM (people), Client Attendees (long text), Preparation Status (status: Not Started, Data Collection, Deck Building, RM Review, Ready), Key Metrics Summary (long text), Product Adoption Status (long text), Open Issues (connected to support board), Growth Opportunities (long text), Risk Factors (long text), Strategic Recommendations (long text), Meeting Notes (long text), Action Items (subitems), Client Satisfaction Rating (numbers), Follow-Up Status (status). Automations trigger the preparation workflow 3 weeks before QBR date and track follow-up execution.

#### The Outcome
QBR preparation time reduced from 5 hours to 1.5 hours per client through automated data aggregation and template generation. QBR completion rate increased from 60% to 92% of Tier 1/2 clients. Client-reported QBR value rating improved from 3.1 to 4.4 out of 5. 40% increase in expansion opportunities identified during QBRs through systematic discovery question frameworks.

#### Discovery Questions
- How many QBRs does each CS manager conduct per quarter, and how much preparation time does each one require?
- What percentage of your strategic clients actually receive regular QBRs, and why do some fall through the cracks?
- How do your QBRs balance backward-looking reporting with forward-looking strategic discussion?
- After a QBR, how do you track the action items that were committed to — and what's the completion rate?
- Do your clients find your QBRs valuable, and how do you know?

#### Industry Context
"Strategic reviews" in banking range from formal QBRs for top-tier clients to annual check-ins for mid-market. The "share of wallet" conversation is critical: understanding what products the client uses with competitors and positioning for expansion. "Wallet sizing" — estimating a client's total banking needs — requires combining internal data with industry benchmarks. The most effective banking QBRs include peer benchmarking ("here's how your treasury operations compare to similar companies in your industry"), which requires data aggregation most banks can't do efficiently.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a QBR Management System for banking Customer Success. Create a board called 'QBR Tracker' with columns: Client Name (text), Client Segment (dropdown: Large Corporate, Upper Mid-Market, Lower Mid-Market, Small Business, Private Banking), Quarter (dropdown: Q1 2026, Q2 2026, Q3 2026, Q4 2026), QBR Date (date), Time (text), Location (dropdown: Client Site, Bank Office, Virtual, Hybrid), CS Manager (people), Relationship Manager (people), Product Specialist Needed (people), Client Primary Contact (text), Client Attendees (long text), Prep Status (status: Not Scheduled, Scheduling, Data Collection, Deck Building, Internal Review, Ready, Completed, Rescheduled, Cancelled), Revenue Current Quarter $K (numbers), Revenue Prior Quarter $K (numbers), Revenue QoQ Change % (formula), Products Active Count (numbers), Product Utilization Score (numbers), Digital Engagement Score (numbers), Open Support Issues (numbers), NPS/CSAT (numbers), Expansion Opportunities Identified (numbers), Expansion Revenue Potential $K (numbers), Strategic Themes (dropdown multi-select: Digital Transformation, International Expansion, M&A Activity, Cost Optimization, Working Capital, Risk Management, Sustainability/ESG, Regulatory Compliance), Meeting Notes (long text), Client Satisfaction with QBR (numbers 1-5), Deck Link (link), Recording Link (link). Create subitems for each QBR to track action items: Action Item (text), Owner (dropdown: Bank, Client, Joint), Assigned To (people), Due Date (date), Status (status: Open, In Progress, Complete, Cancelled), Notes (long text). Add automations: 21 days before QBR Date, change Prep Status to 'Data Collection' and notify CS Manager. When Prep Status changes to 'Internal Review', notify RM. When QBR is 'Completed', send automation to create next quarter's QBR item with same client details. When action item Due Date passes and Status is not 'Complete', notify Assigned To. Create Dashboard: QBR completion rate by segment (bar chart), upcoming QBRs calendar (timeline), action item completion rate (pie chart), average client QBR satisfaction score (number widget), expansion pipeline from QBRs (funnel), and overdue action items table. Add a Calendar view for scheduling visibility."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** QBR Autopilot
**Agent Purpose:** Automate QBR data aggregation, generate insight-rich preparation packages, draft talking points, and track post-QBR action item execution.

**Triggers:**
- 21 days before each QBR Date: initiate preparation workflow
- When Prep Status changes to "Data Collection"
- Day before QBR: generate final briefing
- Day after QBR: create follow-up workflow
- Weekly: scan for overdue QBR action items

**Actions:**
- Auto-generate QBR data package: pull revenue trends, product utilization metrics, transaction volumes, support ticket summary, digital adoption scores, and key relationship events from the past quarter
- Draft "Strategic Insights" section: identify patterns (e.g., "FX volume up 45% — likely tied to client's announced European expansion. Opportunity: offer hedging strategy review and introduce FX advisory team")
- Generate peer benchmarking snippets: "Your treasury management utilization is at 62nd percentile vs. similar-sized manufacturers. Companies at 80th+ percentile typically leverage [specific features] — suggest demo during QBR"
- Create discovery question recommendations based on client's industry news and strategic context
- Post-QBR: parse meeting notes to auto-create action items with owners and due dates
- Track action item execution and send weekly digests to owners with aging report

**Data Required:**
- Core banking (revenue, transaction volumes, product holdings)
- Digital banking analytics (login, feature usage, API calls)
- Support ticketing (case count, severity, CSAT by interaction)
- CRM (relationship notes, meeting history)
- Industry news feeds for client context
- Peer benchmark database (anonymized aggregate metrics)

**Autonomy Level:** Human-in-the-Loop
Data aggregation and draft generation are autonomous. All QBR materials require CSM review and customization. Action item creation from meeting notes requires CSM confirmation. Client-facing deliverables always require human approval.

**Example Interaction:**
> Three weeks before the Q1 QBR with GlobalManufacturing Inc., QBR Autopilot initiates preparation. It generates a data package: "Revenue: $285K this quarter (+12% QoQ, +8% YoY). Growth driver: Cash management fee income up 23% following implementation of virtual accounts in October. Product utilization: Treasury Management 78% (up from 65%), Trade Finance 45% (flat — 3 LCs opened vs capacity for 20+), FX 32% (declining — down from 48% two quarters ago). Red flag: FX decline may indicate wallet share loss." It drafts strategic talking points: "1. Celebrate cash management success — virtual accounts ROI story is compelling for their CFO. 2. Trade finance underutilization: client announced new Southeast Asia sourcing strategy in their Q3 earnings call — natural fit for our trade finance and supply chain finance capabilities. 3. FX decline: tactfully explore whether they've moved FX execution elsewhere or if underlying international revenue has shifted. Prepare competitive analysis if they mention specific competitors. 4. ESG angle: their sustainability report mentions Scope 3 supply chain emissions targets — our sustainable supply chain finance product could differentiate." It also notes: "Attendee suggestion: invite Head of Trade Finance Sales — client's procurement VP will likely attend given supply chain focus."

---

### Use Case 4: Product Adoption & Digital Enablement Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banks sell multi-product relationships but rarely track whether clients actually adopt and utilize what they've purchased. A corporate client signed up for treasury management with 15 modules — but 6 months later, they're using only 4. A digital banking platform was provisioned for 200 users, but only 35 have ever logged in. Payment file formats were configured but the client is still sending paper checks. This "adoption gap" represents both revenue risk (underutilized products are the first to be cut during client reviews) and missed revenue (features that drive fee income aren't being used). Most banks lack a systematic way to track adoption at the feature level and intervene when utilization stalls.

#### The Solution
monday.com Work Management creates a Product Adoption Tracker. A board tracks each client-product combination with columns: Client Name (text), Product (dropdown: Treasury Management, Cash Management, Digital Banking, Trade Finance, FX Platform, Commercial Cards, Merchant Services), Module/Feature (text), Provisioned Date (date), First Use Date (date), Days to First Use (formula), Active Users (numbers), Licensed Users (numbers), Adoption Rate % (formula), Monthly Transaction Volume (numbers), Volume Trend (dropdown: Growing, Stable, Declining, Dormant), Last Activity Date (date), Days Since Last Activity (formula), Adoption Stage (status: Provisioned, Activated, Engaged, Optimized, Dormant), Enablement Actions (subitems), CS Owner (people). Dashboards show adoption heat maps across the client portfolio, enabling CSMs to prioritize enablement efforts.

#### The Outcome
Average product utilization increased from 52% to 78% within 6 months of implementation. "Dormant product" rate reduced from 23% to 7%. Fee income per client increased 18% through feature-level adoption campaigns. Client retention improved as deeper product integration creates higher switching costs.

#### Discovery Questions
- Do you know, right now, what percentage of the product capabilities you've sold to your top 50 clients are actually being used?
- When a client isn't using a product they're paying for, how do you find out — and what's your intervention process?
- How do you measure digital adoption beyond just "they logged in" — do you track feature-level engagement?
- What's your process for driving adoption of new features or product enhancements across your existing client base?
- Have you ever lost revenue because a client canceled a product they were paying for but not using — where the real issue was lack of enablement rather than lack of need?

#### Industry Context
"Sticky products" in banking — those with highest switching costs — are treasury management, commercial cards, and integrated payables/receivables. "Thin products" like basic deposits and simple lending are easily movable. The CS strategy should focus on moving clients up the "stickiness ladder" by driving adoption of integrated, embedded products. Digital banking adoption is particularly critical as banks invest billions in platforms that only deliver ROI at scale. "Self-service deflection" — clients using digital tools instead of calling the bank — directly reduces operational costs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Product Adoption & Digital Enablement Tracker for banking. Create a board called 'Product Adoption Monitor' with columns: Client Name (text), Client Segment (dropdown: Large Corporate, Upper Mid-Market, Lower Mid-Market, Small Business), Product (dropdown: Treasury Management, Cash Management, Digital Banking Platform, Trade Finance Portal, FX Trading Platform, Commercial Cards Portal, Merchant Services Dashboard, Mobile Banking, API/Developer Portal, Reporting & Analytics Suite), Module or Feature (text), Provisioned Date (date), First Active Use Date (date), Days to First Use (formula), Licensed/Provisioned Users (numbers), Active Users Last 30 Days (numbers), Adoption Rate % (formula: Active/Licensed × 100), Monthly Transactions (numbers), Transactions vs Prior Month % (numbers), Last Activity Date (date), Days Inactive (formula), Adoption Stage (status: Provisioned - Not Activated, Activated - Exploring, Engaged - Regular Use, Optimized - Power User, Champion - Advocating, Dormant - No Activity 30+ Days, At Risk - Declining Usage), Adoption Target (numbers), On Track to Target (status: Ahead, On Track, Behind, Critical), CS Owner (people), Enablement Contact (people), Training Completed (checkbox), Training Date (date), Blockers (long text), Next Action (text), Next Action Due (date). Create subitems for enablement activities: Activity (text), Type (dropdown: Training Session, Webinar, Office Hours, Configuration Support, Best Practice Review, Executive Briefing, Peer Introduction), Date (date), Attendees (numbers), Outcome (long text), Status (status: Scheduled, Completed, Cancelled, Rescheduled). Add automations: when Days to First Use exceeds 30 and Adoption Stage is 'Provisioned', change to 'Dormant' and notify CS Owner with alert 'Client has not activated product — intervention needed'. When Adoption Rate drops below 25% and was previously above 50%, change On Track to 'Critical' and notify CS Owner. When Days Inactive exceeds 60, create action item 'Re-engagement outreach'. Create Dashboard: adoption rate distribution across portfolio (histogram), dormant products needing intervention (table), adoption by product type (bar chart), enablement activity pipeline (calendar), client adoption scorecards (leaderboard showing top and bottom clients), and days-to-first-use trend by product (line chart). Add a Kanban view grouped by Adoption Stage for pipeline management."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Adoption Accelerator
**Agent Purpose:** Monitor product adoption patterns, identify at-risk and underutilized products, generate personalized enablement recommendations, and automate re-engagement campaigns.

**Triggers:**
- Daily: scan for adoption stage changes and dormancy signals
- When a product is provisioned for a new client (new item created)
- When Active Users drops by >30% month-over-month
- When Days to First Use hits 14 days (early warning) and 30 days (intervention)
- Monthly: generate portfolio-wide adoption report
- When new product feature is released (manual trigger for adoption campaign)

**Actions:**
- Create personalized adoption playbooks based on client segment, industry, and product mix: "For mid-market manufacturers using Treasury Management, prioritize: (1) automated receivables matching, (2) cash positioning dashboards, (3) payment approval workflows"
- Generate re-engagement emails for dormant products with specific value propositions: "Your team provisioned our FX Trading Platform 45 days ago but hasn't placed a trade yet. Companies in your industry typically save 15-25bps on FX execution by moving from phone-based trading to our platform. Would a 30-minute walkthrough be helpful?"
- Identify adoption pattern correlations: "Clients who activate Cash Positioning within 14 days of Treasury Management provisioning have 3x higher 12-month retention. Meridian Corp hasn't activated it yet — prioritize."
- Create peer benchmarking insights: "Your digital banking adoption is at 35% (35 of 100 provisioned users). Similar-sized clients average 68%. Top adopters leverage SSO integration — has this been configured?"
- Schedule and track enablement activities (training sessions, office hours) automatically based on adoption gaps
- Generate monthly "Adoption Wins" report highlighting successes for CS team recognition and client case study development

**Data Required:**
- Digital banking platform usage analytics (logins, features used, transactions)
- Product provisioning records
- Client user directory (who was granted access)
- Training completion records
- Historical adoption patterns for benchmarking
- Product feature release calendar

**Autonomy Level:** Escalation-Based
Usage monitoring and insight generation are fully autonomous. Enablement activity recommendations are autonomous but scheduling requires CSM confirmation. Re-engagement emails are drafted but require CSM approval before sending. Product cancellation risk alerts are escalated to CS leadership.

**Example Interaction:**
> The Adoption Accelerator detects that Summit Healthcare Group activated their Commercial Cards Portal 21 days ago with 50 provisioned users. Current status: 8 users have logged in, 3 have completed their first expense report. It generates an analysis: "Summit Healthcare adoption is tracking at 16% (8/50 users) at Day 21. Benchmark for healthcare clients: 45% by Day 21. Likely blocker: based on login patterns (all 8 users are in the finance department), the clinical department heads may not have received login credentials or been informed about the program. Recommended actions: (1) Verify with client admin that all 50 user invitations were sent and received, (2) Schedule a 15-minute 'Admin Best Practices' session to help their card program administrator send targeted adoption emails to department heads, (3) Share the healthcare-specific expense policy template that accelerates adoption for clinical departments (this drove 40% adoption lift at similar clients). If no improvement by Day 35, escalate to RM for executive sponsor engagement." It drafts an email to the CS Manager with the full analysis and pre-written client communication options.

---

### Use Case 5: Voice of Client & Feedback Loop Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking clients provide feedback through dozens of channels — NPS surveys, CSAT ratings after support interactions, QBR discussions, relationship manager call notes, formal complaints, social media mentions, RFP responses, and advisory board sessions. This feedback is scattered across survey tools (Medallia, Qualtrics), CRM notes, complaint management systems, and email threads. No one has a unified view of what clients are saying, and patterns that could prevent churn or drive product improvement go undetected. When a product team asks "what are clients saying about our treasury platform?" the answer takes weeks to compile. Worse, clients feel unheard — they provide the same feedback repeatedly without seeing action, eroding trust.

#### The Solution
monday.com Work Management creates a Voice of Client (VoC) hub. A central board captures all feedback with columns: Client Name (text), Feedback Source (dropdown: NPS Survey, CSAT Survey, QBR, RM Notes, Support Interaction, Formal Complaint, Advisory Board, Social Media, Direct Email, Exit Interview), Date Received (date), Verbatim Feedback (long text), Sentiment (dropdown: Very Positive, Positive, Neutral, Negative, Very Negative), Category (dropdown: Product Functionality, User Experience, Pricing, Service Quality, Onboarding, Integration, Communication, Competitor Comparison), Product Referenced (dropdown), Actionable (checkbox), Action Owner (people), Action Status (status: New, Triaged, In Progress, Resolved, Communicated to Client, Closed), Resolution (long text), Client Informed (checkbox). Connected boards link to Product Backlog and Service Improvement initiatives, closing the loop between feedback and action.

#### The Outcome
Single source of truth for all client feedback across channels. Pattern detection identifying systemic issues 60% faster. Client "feedback loop closure" rate improved from 20% to 75% (clients informed of actions taken). Product team receives structured, prioritized client insight monthly instead of ad-hoc anecdotes. NPS improved 12 points through visible responsiveness.

#### Discovery Questions
- How do you currently aggregate client feedback from surveys, QBRs, support interactions, and relationship manager conversations?
- When a client raises the same concern for the third time, does your team know it's the third time — or does it feel like a new issue each time?
- How does client feedback make its way to your product and technology teams, and how long does that cycle take?
- Do your clients feel heard? How do you close the loop — telling them what you did with their feedback?
- What was the last systemic issue you identified from client feedback patterns, and how long did it take to detect?

#### Industry Context
Banking NPS scores average 20-35 (vs. 50+ for leading tech companies). "Complaint management" in banking is heavily regulated — regulators track complaint volumes, categories, and resolution times. However, complaints represent only 5-10% of actual client dissatisfaction; the rest exits silently. "Client Advisory Boards" (CABs) are common in commercial banking and produce rich qualitative feedback that's typically captured in meeting minutes and forgotten. The most sophisticated banks are moving toward "predictive dissatisfaction" — using behavioral data to detect unhappiness before clients articulate it.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Voice of Client (VoC) Hub for banking. Create a board called 'Client Feedback Central' with columns: Feedback ID (auto-number), Client Name (text), Client Segment (dropdown: Large Corporate, Upper Mid-Market, Lower Mid-Market, Small Business, Private Banking, Institutional), Feedback Source (dropdown: NPS Survey, Transactional CSAT, QBR Feedback, RM Call Notes, Support Case Feedback, Formal Complaint, Client Advisory Board, Social Media, Direct Email, Exit Interview, Product Review, Industry Event), Date Received (date), Feedback Type (dropdown: Praise, Suggestion, Concern, Complaint, Feature Request, Competitive Intel, General Comment), Verbatim (long text), Sentiment Score -5 to +5 (numbers), Category (dropdown: Product - Functionality, Product - Performance, Product - UX/UI, Service - Response Time, Service - Quality, Service - Availability, Pricing - Value, Pricing - Transparency, Onboarding - Speed, Onboarding - Communication, Integration - API, Integration - File Formats, Relationship - Communication, Relationship - Proactivity, Competitive - Feature Gap, Competitive - Pricing), Product Referenced (dropdown: Treasury Management, Cash Management, Digital Banking, Trade Finance, FX, Cards, Lending, Payments, General), Urgency (dropdown: Immediate - Client at Risk, High - Systemic Issue, Medium - Improvement Opportunity, Low - Nice to Have), Actionable (checkbox), Action Owner (people), Action Team (dropdown: Product, Engineering, Operations, Service, CS, Sales, Executive), Action Status (status: New, Triaged, Investigating, In Progress, Resolved, Communicated to Client, Closed - No Action, Closed - Actioned), Resolution Summary (long text), Client Loop Closed (checkbox), Loop Closed Date (date), Linked Product Backlog Item (link). Add automations: when Urgency is 'Immediate', notify CS leadership and RM instantly. When Sentiment Score is -4 or below, auto-flag for CS Manager review. When Action Status changes to 'Resolved', remind Action Owner to close the loop with client. When Client Loop Closed is checked, notify CS Manager. Create Dashboard: feedback volume trend by month (line chart), sentiment distribution (bar chart), top categories (pie chart), open action items by team (stacked bar), loop closure rate (progress widget), NPS trend (line chart), and urgent items requiring attention (table filtered by Urgency = Immediate or High and Status = New or Triaged). Add a Word Cloud view equivalent using category frequency data."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Client Voice Analyst
**Agent Purpose:** Aggregate, categorize, and analyze client feedback from all channels; identify patterns and systemic issues; generate actionable insights for product and service teams; and ensure feedback loop closure.

**Triggers:**
- When new feedback item is created (any source)
- Daily: scan for un-triaged feedback older than 48 hours
- Weekly: pattern analysis across all feedback from the past 7 days
- Monthly: generate comprehensive VoC report for leadership
- When Client Loop Closed remains unchecked 14 days after Action Status = "Resolved"

**Actions:**
- Auto-categorize incoming feedback by sentiment, category, product, and urgency using natural language analysis
- Detect patterns: "Treasury Management UX complaints have increased 140% this month — 8 clients mentioning 'dashboard load time.' Correlates with platform update deployed Feb 3rd. Recommend: escalate to Engineering as potential regression."
- Generate "signal strength" analysis: differentiate between one-off complaints and systemic issues by counting unique clients mentioning similar themes
- Create monthly VoC digest for product teams with prioritized themes, representative verbatims, and client impact quantification (total revenue of affected clients)
- Draft "loop closure" messages for CSMs: "Hi [Client], You mentioned in our October QBR that the payment approval workflow was cumbersome. I wanted to let you know we've released a streamlined 2-click approval process based on your feedback. [Link to feature update]"
- Identify "silent detractors" — clients who've stopped providing any feedback (no survey responses, declined QBRs) as a potential disengagement signal

**Data Required:**
- All feedback sources (survey tools, CRM notes, support system, complaint system)
- Client master data for segmentation and revenue context
- Product release calendar (to correlate feedback spikes with changes)
- Historical feedback data for trend analysis
- Client engagement history (to detect "gone silent" patterns)

**Autonomy Level:** Human-in-the-Loop
Feedback categorization and pattern detection are autonomous. Urgency escalations are autonomous. VoC report generation is autonomous but requires leadership review before distribution. Loop closure messages are drafted but require CSM personalization and approval. Product team recommendations require CS leadership endorsement.

**Example Interaction:**
> The Client Voice Analyst runs its weekly pattern analysis and identifies a cluster: "5 different mid-market clients have mentioned 'difficulty reconciling' or 'reconciliation issues' with Cash Management in the past 10 days — across 3 different feedback channels (2 support tickets, 2 QBR notes, 1 NPS comment). Combined revenue of affected clients: $1.2M. This is a new pattern — reconciliation complaints averaged 0.5 per week over the prior 3 months. Potential driver: the February 1st update to the MT940 statement format may have broken some clients' automated reconciliation workflows. Recommend: (1) Immediate: alert Cash Management product team and request investigation of MT940 format change impact, (2) Short-term: CS team to proactively reach out to all clients using automated reconciliation to check for issues before they contact us, (3) Medium-term: add reconciliation workflow testing to the product release QA checklist. Urgency: HIGH — if this is a format regression, it will generate increasing complaint volume as more clients run month-end reconciliation next week."

---

### Use Case 6: Client Expansion & Cross-Sell Orchestration

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The most profitable banking relationships are multi-product, yet most expansion happens through ad-hoc RM conversations rather than systematic identification and pursuit of cross-sell opportunities. A CS team might know that a treasury management client is manually processing international payments (prime FX cross-sell), or that a commercial lending client is growing rapidly (working capital opportunity), or that a cash management client just announced an acquisition (integration and expanded product needs). But this intelligence sits in meeting notes, email threads, and individual CSM knowledge. When a CSM leaves, the pipeline of expansion opportunities goes with them. Cross-sell rates in commercial banking average only 1.2 additional products per year despite most clients being suitable for 3-5 more.

#### The Solution
monday.com CRM functionality creates a systematic expansion pipeline. A board tracks opportunities: Client Name (text), Current Products (dropdown multi-select), Opportunity Product (dropdown), Opportunity Type (dropdown: Cross-Sell, Upsell, Expansion, Renewal Enhancement), Signal Source (dropdown: QBR Discussion, Usage Pattern, Client News, Industry Trend, RM Relationship, Support Interaction, Product Trigger), Estimated Annual Revenue (numbers), Probability (dropdown: 10%, 25%, 50%, 75%, 90%), Stage (status: Identified, Qualified, Discovery Meeting, Proposal, Negotiation, Won, Lost), CS Owner (people), RM Owner (people), Product Specialist (people), Target Close Date (date), Competitive Landscape (long text), Client Business Trigger (long text), Notes (long text). Automations create opportunities when product usage patterns or client events suggest expansion potential.

#### The Outcome
Cross-sell pipeline value increased 3x through systematic opportunity identification. Win rate on CS-originated opportunities: 45% (vs. 25% for cold-prospected deals). Average products per client increased from 3.2 to 4.8 within 18 months. CS team contribution to revenue growth: 35% of net new commercial banking revenue attributed to CS-identified expansion.

#### Discovery Questions
- What's your current cross-sell rate (additional products per client per year), and how does that compare to your target?
- When your CS team identifies an expansion opportunity, what's the handoff process to the RM or sales team?
- How do you systematically identify which existing clients are ready for additional products — is it data-driven or relationship-driven?
- Do you track the revenue impact of your CS team's cross-sell contributions, and are they incentivized for expansion?
- What's the typical conversion rate and cycle time for CS-originated expansion deals versus RM-prospected ones?

#### Industry Context
"Wallet share" is the holy grail metric — what percentage of a client's total banking needs does your bank capture? Most banks capture 20-35% of their commercial clients' total banking wallet. "Natural cross-sell paths" in banking: Treasury Management → FX → Trade Finance → Supply Chain Finance. Or: Commercial Lending → Cash Management → Commercial Cards → Merchant Services. "Trigger events" — M&A, IPO, international expansion, new leadership — create concentrated windows of opportunity that most banks miss because they're not systematically monitored.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Client Expansion Pipeline for banking CS. Create a board called 'CS Expansion Pipeline' with columns: Client Name (text), Client Segment (dropdown), Current Products (dropdown multi-select: Treasury Management, Cash Management, Commercial Lending, Trade Finance, FX, Commercial Cards, Merchant Services, Deposits, Digital Banking, Payroll, Escrow, Supply Chain Finance, Asset-Based Lending), Opportunity Product (dropdown: same list), Opportunity Type (dropdown: Cross-Sell New Product, Upsell Existing Product, Usage Expansion, Contract Enhancement, Renewal Upgrade), Signal Source (dropdown: QBR Discussion, Product Usage Pattern, Client Press Release/News, Industry Trend, RM Intelligence, Support Interaction, Competitor Displacement, Client Event/Trigger, Advisory Board, Digital Behavior Signal), Business Trigger (long text), Estimated Annual Revenue $K (numbers), Probability % (dropdown: 10%, 25%, 50%, 75%, 90%), Weighted Revenue $K (formula), Stage (status: Signal Detected, Qualified, Discovery Scheduled, Discovery Complete, Solution Design, Proposal Delivered, Negotiation, Won, Lost, Deferred), CS Owner (people), RM Owner (people), Product Specialist (people), Target Close Date (date), Days in Stage (formula), Competitive Alternative (text), Win/Loss Reason (long text), Notes (long text). Create subitems for next steps: Action (text), Owner (people), Due Date (date), Status (status). Add automations: when Stage changes to 'Qualified', notify RM Owner to align on approach. When Days in Stage exceeds 30 and Stage is 'Discovery Scheduled' or later, notify CS Owner to check progress. When Stage changes to 'Won', celebrate notification to team and auto-create onboarding board for the new product. When Stage changes to 'Lost', require Win/Loss Reason. Create Dashboard: pipeline by stage (funnel chart), pipeline value by product (bar chart), win rate by signal source (table), revenue won YTD (number widget), average cycle time by opportunity type (bar chart), top 10 opportunities by weighted revenue (table), and CS team leaderboard (pipeline generated per CSM). Add a Kanban view grouped by Stage for pipeline management meetings."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Expansion Intelligence Engine
**Agent Purpose:** Systematically identify cross-sell and upsell opportunities by analyzing product usage patterns, client news, and industry signals; generate qualified leads for the CS expansion pipeline.

**Triggers:**
- Weekly: analyze product utilization data across portfolio for expansion signals
- When client company appears in business news (M&A, expansion, leadership change, funding)
- When product adoption reaches "Optimized" stage (client ready for adjacent products)
- When a client's industry peers adopt a product the client doesn't have
- Monthly: generate "expansion readiness" scores for all clients
- When QBR notes mention competitor products or unmet needs

**Actions:**
- Score each client on "expansion readiness" using: product utilization maturity, relationship health, growth signals, and white space analysis (products they should have but don't)
- Generate opportunity recommendations with context: "Meridian Manufacturing: 92% Treasury Management utilization, growing international revenue per recent 10-K. Currently processing international payments through wire transfers at $35/wire. Cross-sell FX Platform: estimated 200 monthly international payments = $84K annual revenue opportunity. Natural conversation starter during upcoming QBR."
- Monitor trigger events from news feeds: "GlobalTech Corp announced acquisition of DataVault Inc. for $340M. Recommended actions: (1) Proactive outreach from RM — M&A integration creates demand for consolidated treasury, expanded cash management, and integration financing. (2) Estimated expansion: $150-250K annual revenue across 3 products."
- Create pre-qualified pipeline items with populated fields when confidence exceeds threshold
- Draft personalized outreach messages for CSMs: "Hi Sarah, I noticed your international payment volume has grown 40% this quarter — congratulations on the European expansion! I wanted to share how our FX platform could help reduce your currency conversion costs. Would you have 20 minutes next week?"
- Analyze win/loss patterns to improve future opportunity identification: "CS-originated FX opportunities from Treasury Management clients have a 62% win rate when the trigger is international payment volume growth, vs. 28% when the trigger is general relationship discussion. Focus on data-driven signals."

**Data Required:**
- Product utilization and transaction data (core banking)
- Client financial data and public filings
- Business news monitoring feeds
- Industry product adoption benchmarks
- Historical win/loss data for pattern analysis
- CRM relationship and meeting notes

**Autonomy Level:** Escalation-Based
Signal detection and opportunity scoring are fully autonomous. Pipeline item creation at "Signal Detected" stage is autonomous. Qualification and outreach recommendations require CSM review. All client communications require CSM approval. Won/Lost analysis is autonomous.

**Example Interaction:**
> The Expansion Intelligence Engine runs its weekly portfolio scan and identifies 12 expansion signals. Top priority: "DataFlow Analytics (Current products: Commercial Lending, Basic Deposits. Revenue: $95K/year. Health Score: 82). Signals: (1) Company blog post announces 'scaling to 500 employees by year-end' (currently 180), (2) Digital banking login frequency increased 3x in past month — admin user exploring payroll and HR payment features, (3) Peer comparison: 78% of similarly-sized tech companies in our portfolio use Cash Management + Commercial Cards. Recommended opportunity: Cash Management + Payroll + Commercial Cards bundle. Estimated revenue: $120K/year. Confidence: HIGH — growth signal + active digital exploration + peer benchmark all align. Suggested approach: CSM to mention during next check-in that we noticed increased digital banking engagement and offer a 'Growth Package' consultation. Warm intro to Cash Management specialist. Do NOT lead with payroll — let the cash management conversation naturally surface their payment pain points."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Share of Wallet | Percentage of a client's total banking needs captured by the bank |
| Product Penetration | Number of active products per client relationship |
| Time-to-Value | Duration from contract signing to client realizing measurable benefit |
| QBR (Quarterly Business Review) | Structured strategic review meeting with commercial banking clients |
| NPS (Net Promoter Score) | Client likelihood to recommend, scored -100 to +100 |
| CSAT (Customer Satisfaction) | Transactional satisfaction rating, typically 1-5 scale |
| KYC (Know Your Customer) | Regulatory requirement to verify client identity, ownership, and risk profile |
| AML (Anti-Money Laundering) | Regulations requiring banks to monitor for suspicious financial activity |
| Core Banking System | Primary technology platform managing accounts, transactions, and general ledger |
| Treasury Management | Suite of products for corporate cash flow, payments, and liquidity management |
| Wallet Sizing | Estimating a client's total banking needs across all providers |
| Sticky Products | Banking products with high switching costs (e.g., treasury management, commercial cards) |
| Self-Service Deflection | Client using digital tools instead of contacting the bank, reducing service costs |
| Implementation Gap | Products sold but not activated or fully deployed |
| Trigger Event | Client business event (M&A, expansion, leadership change) creating banking opportunity |
| RFP Risk | Client issuing a Request for Proposal to competitors — late-stage churn signal |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Head of Customer Success | CS strategy, team management, retention metrics, expansion targets | Decision-maker |
| Customer Success Manager (CSM) | Day-to-day client engagement, health monitoring, QBRs, adoption enablement | User (primary) |
| Relationship Manager (RM) | Senior client relationship ownership, deal origination, executive access | Decision-maker |
| Head of Client Experience | NPS/CSAT programs, journey mapping, service design | Influencer |
| Product Manager — Digital Banking | Digital platform features, adoption metrics, roadmap | Influencer |
| Head of Operations / Client Services | Onboarding execution, support delivery, SLA management | Influencer |
| Chief Client Officer / Head of Commercial Banking | P&L ownership, strategic client relationships | Decision-maker |
| Client Onboarding Manager | Onboarding process design and execution | User |
| Data & Analytics Lead | Client data infrastructure, reporting, predictive models | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales / Relationship Management | Joint client ownership, expansion pipeline handoff | Unified client lifecycle platform from prospect to advocate |
| Operations / Client Services | Onboarding execution, support delivery, SLA tracking | Connected onboarding and support workflows feeding health scores |
| Product & Technology | Feature requests from clients, digital adoption data | Closed feedback loop: client voice → product roadmap → adoption tracking |
| Marketing | Client communications, thought leadership, event invitations | Personalized client marketing driven by CS insights and adoption data |
| Risk & Compliance | KYC renewals, regulatory client communications | Coordinated client touchpoints preventing "compliance fatigue" |
| Finance | Revenue attribution, client profitability analysis | CS contribution to revenue growth tracking and incentive design |
| IT | System integrations, data infrastructure, API management | Data pipeline from core banking → CS platform for health scoring |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce Financial Services Cloud | CRM with financial services data model | monday.com is more flexible, faster to deploy, and better for workflow orchestration; Salesforce is heavy and expensive |
| Gainsight | Purpose-built CS platform | Strong for SaaS CS; weaker for banking's complex multi-product, multi-stakeholder relationships. monday.com offers broader workflow + project management |
| Totango | CS platform with health scoring | Similar to Gainsight — limited banking industry specialization. monday.com's flexibility handles banking's unique product complexity better |
| ChurnZero | CS platform focused on product adoption | Designed for SaaS product telemetry; doesn't handle banking's offline/relationship-driven signals |
| Excel/SharePoint | Default tool for most banking CS teams | Direct displacement — most banking CS teams are still in spreadsheets. monday.com is the natural first platform |
| ServiceNow | IT service management repurposed for client services | Strong for ticketing; weak for proactive CS, adoption tracking, and expansion pipeline. Complementary positioning |
| ClientSuccess | CS platform | Small vendor, limited enterprise banking deployments. monday.com offers broader platform play |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Salesforce for client management" | Salesforce is your CRM — it tracks relationships. But who tracks the 47-step onboarding process, the QBR preparation workflow, the product adoption campaigns, and the feedback loop? That's workflow orchestration, and that's where monday.com excels alongside your CRM. |
| "Our core banking system should handle client analytics" | Core banking handles transactions and accounting. It tells you WHAT happened. It doesn't tell you WHY a client's usage is declining, orchestrate the intervention, or track whether your team followed up. That's the CS operations layer monday.com provides. |
| "We're building a custom client health dashboard in-house" | How long has that project been running, and when will it be live? monday.com gives you a working health dashboard in weeks, not months. Start here, prove the value, then decide what's worth custom-building. |
| "CS is too relationship-driven for a software tool" | The best CSMs use tools to handle the operational overhead so they can focus MORE time on relationships. If your CSMs spend 5 hours preparing for a QBR instead of 1.5, that's 3.5 hours of relationship time you're losing to data wrangling. |
| "We need industry-specific client success software" | Industry-specific tools lock you into their workflows. Banking CS is evolving fast — you need a platform flexible enough to adapt as your CS model matures. monday.com lets you build exactly the workflows your team needs, and change them next quarter when you learn what works. |
| "Our CS team is too small to justify a platform" | That's exactly why you need one. A 5-person CS team managing 500 clients needs force-multiplication more than a 50-person team. Automation and visibility are how small teams punch above their weight. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for banking customer success transformation case studies]
- [Placeholder for commercial banking client retention improvement examples]
- [Placeholder for digital banking adoption acceleration references]
- [Placeholder for CS-driven revenue expansion case studies in financial services]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
