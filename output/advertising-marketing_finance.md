# Advertising & Marketing × Finance Playbook

## Overview

Finance departments in advertising and marketing companies manage one of the most complex financial models in professional services. Agency revenue comes through multiple streams — retainers (monthly fees for ongoing service), project fees, commissions (percentage of media spend), performance bonuses, and production markups — each with different recognition rules, margin profiles, and billing cycles. A mid-market agency ($50–200M revenue) typically has a finance team of 8–15 people managing billing for 50–200 active clients, while holding company networks (WPP, Publicis, Omnicom) manage billions in client billings through shared service centers.

The financial complexity is amplified by pass-through costs. When an agency buys $10M in media for a client, that spend flows through the agency's books as both revenue and cost — inflating top-line numbers and requiring careful gross-revenue vs. net-revenue accounting. Production costs (video shoots, talent fees, music licensing, photography) are similarly pass-through but with markup. Finance teams must track: agency fees (the real margin), media billings (pass-through), production costs (mixed margin), and third-party vendor payments — all while managing cash flow timing gaps where agencies often pay vendors before clients pay them.

Regulatory and compliance pressures are mounting. ASC 606 revenue recognition standards have complicated how agencies account for long-term contracts. Tax treatment of international campaigns crossing multiple jurisdictions, transfer pricing between agency entities in different countries, and withholding tax on talent fees create layers of complexity. Auditors scrutinize client billing accuracy, and agencies face margin compression as clients demand more transparency — the ANA's "media transparency" investigations have made fee structures a boardroom topic. Finance teams are expected to provide real-time profitability insights while running on spreadsheets and legacy ERP systems.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Agency finance teams spend 50-60% of time on manual billing, reconciliation, and reporting — AI can handle the mechanical work |
| 2 | Scale Impact Without Overhead | Medium-High | Agencies adding clients and revenue without proportional finance headcount growth — need to scale financial operations efficiently |
| 3 | Consolidate Tech Stack with AI | Medium | Finance data trapped across ERP, billing systems, timesheet tools, project management, and Excel — no single source of truth |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Client Profitability Tracking & SOW Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Agency CFOs are flying blind on client profitability. A client may look profitable on paper (high retainer fee) but be hemorrhaging margin through scope creep, over-servicing, and untracked out-of-scope requests. The typical agency has no real-time view of profitability at the client level — it requires pulling data from the ERP (revenue), timesheet system (labor costs), and project management tool (deliverables), then reconciling in Excel. By the time finance identifies an unprofitable client, 2–3 months of margin have already been lost. Scope of Work (SOW) management is particularly painful: SOWs define deliverables and fees, but actual work frequently exceeds the SOW — and nobody tracks the overage until billing time.

#### The Solution
monday.com Work Management as the SOW and profitability tracking hub. Each client SOW is a structured item with defined deliverables, allocated hours, fee structure, and actual spend tracking. Time entries (integrated from timesheet tools) automatically feed into profitability calculations. Dashboards show real-time margin by client, flagging clients below target profitability. Automations alert account directors when out-of-scope work exceeds a threshold, enabling proactive client conversations about scope changes.

#### The Outcome
- Real-time client profitability visibility (vs. 60-day lag with manual processes)
- 15% margin improvement on under-performing accounts through early intervention
- 90% reduction in scope creep losses through automated out-of-scope tracking
- SOW renewal preparation time cut from 2 weeks to 2 days with historical data at fingertips

#### Discovery Questions
1. "How quickly can you tell me the current profitability of your top 10 clients — real margin, not just revenue?"
2. "How do you track when teams are doing work that falls outside the SOW — and how much revenue do you estimate you're leaving on the table from untracked out-of-scope work?"
3. "When it's time to renegotiate a client SOW, what data do you bring to the table — and how long does it take to compile?"
4. "What's your target margin by client tier, and what percentage of your clients are currently below that threshold?"
5. "How do you handle the cash flow gap between when you pay production vendors and when the client pays you?"

#### Industry Context
Agency profitability varies dramatically by client and service type. Strategy and consulting work commands 40–60% margins; creative production is 25–35%; media buying is 3–5% of media spend (but high volume); and production management is often near breakeven after vendor costs. The industry standard blended margin target is 15–20% operating margin. The "agency of record" model is giving way to project-based engagements, making profitability tracking more important but also more complex. Client procurement departments increasingly demand fee transparency, open-book billing, and benchmarking against industry norms.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Client Profitability & SOW Management workspace for an advertising agency. Include:
> 1. **Client SOWs** — columns: Client Name (text), SOW Period (timeline), Revenue Type (dropdown: Retainer, Project, Commission, Hybrid), Total SOW Value (numbers with $), Monthly Retainer (numbers with $), Allocated Hours (numbers), Hourly Rate Blended (numbers with $), Status (status: Draft, Active, Renewal, Expired), Account Director (people), Finance Contact (people), Auto-Renewal (checkbox), Renewal Date (date)
> 2. **SOW Deliverables** — subitems: Deliverable Name (text), Category (dropdown: Strategy, Creative, Media, Production, Analytics, Social), Allocated Hours (numbers), Actual Hours (numbers), Utilization % (formula: actual/allocated × 100), Fee Allocated (numbers with $), Status (status: Not Started, In Progress, Delivered, Out of Scope), Over/Under Hours (formula: actual - allocated)
> 3. **Client P&L** — columns: Client (connect to Client SOWs), Month (date), Gross Revenue (numbers with $), Pass-Through Revenue (numbers with $), Net Revenue (numbers with $), Labor Cost (numbers with $), Direct Costs (numbers with $), Gross Margin (formula), Gross Margin % (formula), Target Margin % (numbers with %), Variance to Target (formula), Profitability Status (status: Above Target, On Target, Below Target, Critical)
>
> Automations: When SOW Deliverable Utilization % exceeds 110%, change status to 'Out of Scope' and notify Account Director. When Client P&L Margin % drops below Target for 2 consecutive months, alert CFO. When Renewal Date is 90 days away, create renewal task. Dashboard with client profitability ranking, margin trend by month, scope creep heat map, and SOW renewal timeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MarginGuard
**Agent Purpose:** Continuously monitor client profitability and proactively alert stakeholders when accounts drift below target margins.

**Triggers:**
- Weekly profitability refresh (every Monday)
- SOW deliverable hours exceed 100% of allocation
- New time entries logged against client
- Client P&L Margin % drops below target threshold
- SOW renewal date within 90 days

**Actions:**
- Calculate real-time client margin from revenue, labor, and direct cost data
- Identify and quantify out-of-scope work (hours beyond SOW allocation)
- Generate weekly client profitability summary for CFO
- Alert account directors when specific clients approach margin thresholds
- Produce SOW renewal brief with historical utilization, margin data, and recommended pricing adjustments
- Flag cash flow risks (large vendor payments pending with delayed client billing)

**Data Required:**
- SOW terms and deliverable allocations
- Timesheet data by client and employee
- Revenue and billing data from ERP
- Vendor cost and pass-through data
- Employee cost rates (loaded with benefits and overhead)

**Autonomy Level:** Escalation-Based
Autonomous for monitoring, calculations, and reporting. Escalates margin alerts to account directors and CFO. Does not modify client billing or SOW terms.

**Example Interaction:**
> MarginGuard's Monday morning report flags a problem: "⚠️ Margin Alert — Samsung account: Q1 target margin 22%, current actual 11.3%. Root cause: Creative team has logged 340 hours against a 200-hour SOW allocation for the Galaxy S26 campaign — 170% utilization. Estimated out-of-scope value: $42,000 at blended rate. Additionally, 3 vendor invoices ($87K total) are awaiting client approval, creating a $87K cash flow gap. Recommended actions: (1) Schedule scope discussion with Samsung procurement — data attached. (2) Submit change order for 140 additional hours. (3) Escalate vendor payment approvals. Account Director notified."

---

### Use Case 2: Vendor & Production Cost Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
A single campaign can involve 20–50 vendors: production companies, directors, editors, music houses, talent agencies, stock photo/footage libraries, post-production facilities, translation services, and more. Each vendor has different payment terms (Net 15, Net 30, Net 60), different invoicing formats, and different markup structures. Agency producers issue purchase orders, vendors deliver and invoice, finance reconciles POs against invoices against deliverables — and it's all done manually. A mid-size agency processes 500–1,000 vendor invoices per month. Discrepancies between PO amounts and invoice amounts are common (overages, additional revisions, rush fees), and reconciliation eats enormous finance team bandwidth. Meanwhile, cash flow suffers because agencies typically pay vendors on Net 30 but don't bill clients until the work is delivered and approved.

#### The Solution
monday.com Work Management for end-to-end vendor and production cost tracking. Each production job has a cost estimate, approved POs, and linked invoices. Producers create estimates in monday.com, finance approves POs, and invoice reconciliation happens against the structured data. Automations flag discrepancies between PO and invoice amounts, track payment status, and manage approval workflows. Integration with accounting systems syncs payment data.

#### The Outcome
- 70% reduction in invoice reconciliation time
- Zero unauthorized vendor spend (PO approval workflow enforced)
- Cash flow visibility: know exactly what's owed to vendors and when
- 10% cost savings through vendor consolidation insights and rate benchmarking

#### Discovery Questions
1. "How many vendor invoices does your finance team process monthly, and what percentage require manual reconciliation due to discrepancies?"
2. "How do you currently track the journey from production estimate to purchase order to vendor invoice to client billing?"
3. "What's your average accounts payable cycle, and how often do you pay vendor rush fees because invoices sat in an approval queue?"
4. "Can you easily see which vendors you're spending the most with — and whether you're getting the best rates?"

#### Industry Context
Production costs are the largest variable expense in advertising. A single TV commercial can cost $500K–$5M+ in production. Digital production is lower per unit but higher in volume — an agency might produce 500+ digital assets per month. The rise of in-house production studios at agencies (to improve margins) has shifted some vendor spend to internal departments, creating new internal cost allocation challenges. Key vendor categories: production companies (film/video), post-production, music/sound, talent (actors, models, voiceover), photography, CGI/VFX, translation/localization, and print production.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Vendor & Production Cost Management workspace. Include:
> 1. **Production Jobs** — columns: Job Name (text), Job Number (auto-number with prefix: PROD-), Client (text), Campaign (text), Producer (people), Estimated Cost (numbers with $), Approved Budget (numbers with $), Actual Cost (numbers with $), Variance (formula: actual - approved), Variance % (formula), Status (status: Estimating, Approved, In Production, Wrap, Billing, Closed), Start Date (date), Delivery Date (date)
> 2. **Purchase Orders** — columns: PO Number (auto-number with prefix: PO-), Production Job (connect to Production Jobs), Vendor Name (text), Vendor Category (dropdown: Production Co, Post/Edit, Music/Sound, Talent, Photography, CGI/VFX, Translation, Print, Other), PO Amount (numbers with $), Payment Terms (dropdown: Net 15, Net 30, Net 45, Net 60, Prepayment Required), Approval Status (status: Draft, Submitted, Approved, Rejected), Approved By (people), Invoice Received (checkbox), Invoice Amount (numbers with $), Invoice Variance (formula: invoice - PO amount), Payment Status (status: Not Due, Due, Paid, Overdue, Disputed)
> 3. **Vendor Directory** — columns: Vendor Name (text), Category (dropdown), Primary Contact (text), Email (email), Payment Terms (dropdown), YTD Spend (numbers with $), Average Job Rating (numbers 1-5), Preferred Status (checkbox), W-9 on File (checkbox), Insurance Current (checkbox), Last Used (date)
>
> Automations: When PO Amount exceeds $10K, require VP approval. When Invoice Variance exceeds 10% of PO, flag for review and notify Finance. When Payment Status is 'Due' and payment terms are met, trigger payment batch. Dashboard with vendor spend by category, PO vs invoice variance trends, cash flow forecast, and top vendors by spend."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CostController
**Agent Purpose:** Automate vendor invoice reconciliation, enforce PO compliance, and provide real-time production cost visibility.

**Triggers:**
- New vendor invoice received (email integration or form submission)
- PO created or updated
- Invoice amount differs from PO amount by >5%
- Payment due date approaching (3 days out)
- Monthly schedule: vendor spend analysis

**Actions:**
- Match incoming invoices to POs using job number and vendor name
- Flag discrepancies between PO and invoice amounts with variance detail
- Route high-value POs through approval workflow based on amount thresholds
- Generate weekly cash flow forecast based on pending payables and receivables
- Produce monthly vendor spend report with consolidation recommendations
- Track vendor insurance and W-9 compliance, flagging expired documents

**Data Required:**
- Purchase order database
- Vendor invoices (parsed from email or uploaded)
- Production job budgets and actuals
- Vendor directory with terms and compliance status
- Client billing schedule

**Autonomy Level:** Human-in-the-Loop
Autonomous for matching, flagging, and reporting. Payment approvals and dispute resolution require human sign-off.

**Example Interaction:**
> An invoice arrives from Red Brick Post-Production for $24,500 against PO #PO-2847 for $18,000 (the Samsung Galaxy edit). CostController auto-matches the invoice to the PO, identifies a $6,500 overage (36% variance), and pulls the PO notes which mention "base edit only — additional revisions TBD." The agent creates a variance review item: "Invoice variance: $6,500 over PO. Likely cause: additional revision rounds (common for Samsung — 3 prior jobs averaged 28% overage). Options: (1) Approve variance and add to client billing, (2) Negotiate with vendor, (3) Dispute. Historical context: Red Brick's average variance is 22% — this is above their norm. Routed to Producer for review, cc'd Finance." It also updates the production job's actual cost and flags the impact on client margin.

---

### Use Case 3: Revenue Forecasting & Pipeline Visibility

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Agency revenue forecasting is notoriously inaccurate. Revenue comes from multiple unpredictable sources: new business pitches (binary outcomes with 15–25% win rates), client scope expansions (timing uncertain), project work (variable), and retainer renewals (usually reliable but not guaranteed). The CFO builds forecasts by polling department heads who estimate based on gut feel and Outlook calendar reviews. Finance has no real-time pipeline visibility — they find out about new client wins or losses when the account team mentions it in a meeting, sometimes weeks after the fact. This makes cash flow planning, hiring decisions, and capacity management reactive rather than strategic.

#### The Solution
monday.com CRM integrated with Work Management for end-to-end revenue pipeline management. New business pitches are tracked from lead through proposal, pitch, decision, and onboarding. Existing client revenue is forecasted based on SOW terms, renewal probability, and expansion signals. Automations capture pipeline changes in real-time, and AI-powered forecasting suggests probability-weighted revenue projections. Finance dashboards combine pipeline revenue with contracted revenue for complete forecast visibility.

#### The Outcome
- Revenue forecast accuracy improves from ±25% to ±10%
- Real-time pipeline visibility eliminates "surprise" revenue events
- Hiring and capacity decisions made 60 days earlier based on forward-looking revenue data
- Cash flow planning becomes proactive rather than reactive

#### Discovery Questions
1. "How accurate are your quarterly revenue forecasts — and what's the typical variance between forecast and actual?"
2. "When a major pitch is won or lost, how quickly does finance find out — and how does that lag affect your planning?"
3. "How do you factor new business pipeline probability into your revenue forecasts?"
4. "What data sources feed into your revenue forecast today, and how much manual compilation is required?"
5. "How do you plan headcount and capacity when you don't know which new clients will land in 90 days?"

#### Industry Context
Agency revenue is uniquely cyclical and lumpy. Q4 is typically the highest-revenue quarter (holiday campaigns), while Q1 is often soft (annual budget resets, client reviews). New business "pitch season" peaks in January–March as brands issue RFPs for the year ahead. The shift from retainer to project-based work has made forecasting harder — retainer clients provide predictable baseline revenue, while project work creates volatility. The "magic number" for agency growth is 20% new business revenue replacing natural client attrition of 10–15% annually.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Revenue Forecasting & Pipeline workspace for an agency. Include:
> 1. **New Business Pipeline** — columns: Opportunity Name (text), Prospect/Client (text), Service Type (dropdown: Full Service AOR, Creative AOR, Media AOR, Project, Consulting, Production), Estimated Annual Revenue (numbers with $), Win Probability % (numbers), Weighted Revenue (formula: annual rev × probability), Stage (status: Lead, Qualification, RFI, RFP, Chemistry Meeting, Pitch, Decision, Won, Lost), BD Lead (people), Pitch Date (date), Decision Date (date), Revenue Start Date (date), Competitive Situation (dropdown: Sole Source, 2-Way, 3-Way, 4+), Incumbent Agency (text)
> 2. **Contracted Revenue** — columns: Client (text), SOW Type (dropdown: Retainer, Project, Hybrid), Annual Contracted Value (numbers with $), Monthly Revenue (numbers with $), Contract End Date (date), Renewal Probability (dropdown: 90%+, 70-90%, 50-70%, Below 50%), At-Risk Flag (checkbox), Growth Opportunity (numbers with $), Account Director (people)
> 3. **Revenue Forecast** — columns: Month (date), Contracted Revenue (numbers with $), Pipeline Revenue Weighted (numbers with $), Total Forecast (formula), Actual Revenue (numbers with $), Variance (formula), Forecast Accuracy (formula: 1 - |variance|/forecast × 100)
>
> Automations: When Pipeline Stage changes to 'Won', auto-create Contracted Revenue entry. When Contract End Date is 120 days away and Renewal Probability is below 70%, alert CFO. When At-Risk Flag is checked, notify finance and account leadership. Dashboard with revenue forecast waterfall (contracted + pipeline + growth), pipeline by stage, forecast vs actual trend, and client renewal calendar."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RevenueRadar
**Agent Purpose:** Provide real-time revenue forecasting by synthesizing pipeline, contracted, and at-risk revenue data.

**Triggers:**
- Pipeline stage change (any opportunity)
- Contract renewal date within 120 days
- Monthly forecast compilation schedule
- At-risk flag triggered on any client
- Actual revenue data entered (month-end close)

**Actions:**
- Calculate probability-weighted pipeline revenue based on stage and historical win rates
- Generate monthly and quarterly revenue forecasts combining all revenue streams
- Identify at-risk revenue (contract expirations, declining SOW utilization, client satisfaction signals)
- Produce forecast vs. actual variance analysis with explanations
- Send weekly revenue pulse to CFO with key changes (new wins, losses, forecast adjustments)
- Model scenario forecasts (best case, base case, worst case) for planning

**Data Required:**
- New business pipeline data with stage history
- Contracted revenue and SOW terms
- Historical win rates by service type and deal size
- Client satisfaction and renewal data
- Industry seasonal patterns

**Autonomy Level:** Fully Autonomous
All monitoring, calculations, and reporting are automated. Escalates significant forecast changes (>10% swing) and at-risk accounts to CFO.

**Example Interaction:**
> RevenueRadar's weekly pulse to the CFO: "Revenue Radar — Week of Feb 17. Net forecast change: +$180K/month. Key movements: (1) Nike AOR pitch moved to 'Decision' stage — $3.2M annual, 60% probability, weighted +$160K/mo. Decision expected March 1. (2) Johnson & Johnson contract renewal: flagged as 70-90% probability (was 90%+ last month) — hearing budget cuts in their marketing org. At-risk revenue: $85K/mo. (3) Three project wins closed: total $420K. Q2 forecast: $14.2M (base case), up from $13.8M last week. Scenario range: $12.8M (worst) to $15.6M (best). Cash flow note: March payroll + Q1 vendor payments = $4.2M outflow in first two weeks — ensure AR collections are on track."

---

### Use Case 4: Agency Billing & Invoice Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Billing in agencies is a special kind of hell. Each client has different billing terms: some are billed monthly retainer plus actuals, others are project-based with milestone payments, others are commission on media spend, and many are a combination. A single client invoice might include: retainer fee, out-of-scope hours at blended rates, media placement costs with commission, production costs with markup, and reimbursable expenses. Finance teams spend days each month compiling billing data from timesheets, media buy reports, production job trackers, and expense reports. Late billing is endemic — agencies routinely leave 5–10% of billable revenue on the table because billing doesn't happen promptly. And when invoices go out with errors, client payment disputes add another 30–60 days to the collection cycle.

#### The Solution
monday.com Work Management for billing workflow automation. Each client's billing terms are codified in a billing template. Monthly billing cycles auto-generate billing worksheets that pull time, media, production, and expense data into a structured pre-bill review. Account directors approve pre-bills, finance generates invoices, and the system tracks through to payment. Automations flag missing timesheets, unbilled deliverables, and overdue receivables.

#### The Outcome
- Billing cycle compressed from 15 business days to 5 business days
- 5–8% revenue recovery from previously unbilled work
- 40% reduction in invoice disputes through pre-bill accuracy checks
- DSO (Days Sales Outstanding) reduced by 10–15 days through faster billing

#### Discovery Questions
1. "How many business days does it take from month-end to get all client invoices out the door?"
2. "What percentage of your billable hours or deliverables do you estimate goes unbilled each month?"
3. "How often do client invoice disputes delay payment — and what are the most common dispute reasons?"
4. "How many different billing models do you manage across your client portfolio — and does each require a different billing process?"

#### Industry Context
Agency billing models are evolving. The traditional commission model (15% of media spend) has largely been replaced by fee-based billing, but remnants persist. "Labor-based" billing (hourly or FTE rates × hours worked) requires accurate timesheet compliance — an industry-wide struggle where 20–30% of timesheets are submitted late or inaccurate. "Value-based" billing (fixed fees for outcomes) is growing but requires even more sophisticated profitability tracking. The ANA's transparency initiative has pushed agencies toward "open book" billing where clients can audit every line item.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Client Billing & Invoicing workspace. Include:
> 1. **Billing Schedule** — columns: Client (text), Billing Model (dropdown: Monthly Retainer, Project Milestone, Commission on Spend, Hourly/Labor, Hybrid), Billing Day (dropdown: 1st, 5th, 10th, 15th, Last Day), Payment Terms (dropdown: Net 15, Net 30, Net 45, Net 60), Currency (dropdown: USD, GBP, EUR, CAD, AUD), Account Director (people), Finance Owner (people), PO Required (checkbox), Client PO Number (text)
> 2. **Monthly Pre-Bills** — columns: Client (connect to Billing Schedule), Billing Month (date), Retainer Amount (numbers with $), Billable Hours (numbers), Hours Revenue (numbers with $), Media Billings (numbers with $), Media Commission (numbers with $), Production Pass-Through (numbers with $), Production Markup (numbers with $), Expenses (numbers with $), Total Pre-Bill (formula: sum all revenue), Status (status: Compiling, Ready for Review, AD Approved, Invoice Sent, Paid, Disputed), Review Notes (long text)
> 3. **AR Tracker** — columns: Invoice Number (text), Client (text), Invoice Date (date), Due Date (date), Amount (numbers with $), Amount Paid (numbers with $), Balance Due (formula), Days Outstanding (formula: TODAY - due date), Status (status: Current, 1-30 Past Due, 31-60 Past Due, 61-90 Past Due, 90+ Past Due, Disputed, Written Off), Collection Notes (long text), Last Contact Date (date)
>
> Automations: When Billing Day arrives, auto-create Pre-Bill item and notify Finance Owner to compile. When Pre-Bill Status is 'Ready for Review', notify Account Director. When AR Days Outstanding exceeds payment terms, change status and notify Account Director. Dashboard with monthly billing summary, AR aging report, DSO trend, and unbilled work alerts."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BillBot
**Agent Purpose:** Automate billing compilation, pre-bill review, and accounts receivable tracking to eliminate billing delays and revenue leakage.

**Triggers:**
- Monthly billing date for each client
- Time and expense data submitted for billing period
- Pre-bill approved by account director
- Invoice payment received
- AR aging thresholds crossed (30, 60, 90 days)

**Actions:**
- Compile billing data from timesheets, media reports, production jobs, and expenses into pre-bill format
- Flag missing timesheets or incomplete data that would delay billing
- Calculate billing amounts based on each client's unique billing model
- Generate pre-bill summary for account director review
- Track invoice delivery and payment status
- Send collection reminders at aging thresholds (customized by client relationship tier)
- Identify patterns in late payments and recommend collection strategies

**Data Required:**
- Client billing terms and SOW details
- Timesheet data by client and employee
- Media spend reports with commission calculations
- Production job costs and markups
- Expense reports allocated to clients
- Payment history

**Autonomy Level:** Human-in-the-Loop
Autonomous for compilation and tracking. Pre-bill review and collection escalation require account director approval (client relationship sensitivity).

**Example Interaction:**
> It's February 3 — billing day for the P&G account. BillBot compiles the January pre-bill: Retainer: $125,000. Billable hours: 47 additional hours at $250 blended = $11,750. Media billings: $2.3M with 3% commission = $69,000. Production: $340K pass-through + 15% markup = $51,000. Expenses: $4,800. Total pre-bill: $601,550. BillBot flags one issue: "⚠️ 3 creatives haven't submitted timesheets for Jan 27-31. Estimated missing hours: 24 (based on project assignments). Impact: potential $6,000 unbilled. Recommend: notify creatives for immediate timesheet submission before sending pre-bill to Account Director." It also notes: "P&G's December invoice ($578K) was paid on Feb 1 — 32 days (within Net 30 + grace). Current AR balance: $0. Collection risk: Low."

---

### Use Case 5: Budget Planning & Resource Allocation

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Annual budget planning at agencies is an exercise in structured guesswork. The CFO must project revenue (dependent on client retention and new business wins), plan headcount (the largest cost at 55–65% of revenue), allocate departmental budgets, and set profit targets — all while the CEO wants to invest in growth and the holding company wants margin expansion. The process takes 6–8 weeks, involves dozens of spreadsheet versions, and the final budget is outdated within 90 days. Monthly budget-to-actual variance analysis is similarly painful: pulling data from multiple systems, allocating shared costs, and explaining variances consumes 2–3 days per month. Meanwhile, department heads overspend because they have no visibility into their budget consumption until finance tells them (weeks later).

#### The Solution
monday.com Work Management for dynamic budget planning and real-time spend tracking. Department budgets are structured with line items that automatically update as expenses are logged. Budget-to-actual dashboards give department heads self-service visibility. Quarterly reforecasting is streamlined with pre-populated templates. Approval workflows ensure spend requests go through proper channels.

#### The Outcome
- Budget planning cycle reduced from 8 weeks to 4 weeks
- Monthly variance reporting automated (real-time vs. 3-day manual process)
- Department heads make informed spending decisions with real-time budget visibility
- 10% reduction in discretionary spend through transparency and accountability

#### Discovery Questions
1. "How long does your annual budget planning process take, and how many versions of the budget spreadsheet exist by the time it's approved?"
2. "How quickly can a department head see how much of their budget they've spent — and how much is committed but not yet invoiced?"
3. "How do you handle mid-year budget adjustments when you win a major new client or lose one?"
4. "What's your current process for expense approvals — and how often do you discover overspend after the fact?"

#### Industry Context
Agency financial planning is uniquely tied to headcount because labor is the product. A 10-person team represents roughly $1.5–2.5M in fully loaded cost (depending on seniority and location). Hiring decisions are revenue decisions — adding a team before the revenue is contracted burns margin, but waiting until revenue is confirmed means you can't staff the work. This "chicken and egg" problem is the defining challenge of agency financial planning. Holding companies set margin targets (typically 15–18% operating margin) that agencies must hit regardless of revenue fluctuations, creating pressure to manage costs dynamically.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Budget Planning & Expense Tracking workspace. Include:
> 1. **Annual Budget** — columns: Department (dropdown: Creative, Media, Strategy, Account, Production, Technology, HR, Finance, Marketing/BD, Executive), Category (dropdown: Salaries, Freelancers, Software/Tools, Travel, Training, Office/Facilities, Production, Marketing, Other), Q1 Budget (numbers with $), Q2 Budget (numbers with $), Q3 Budget (numbers with $), Q4 Budget (numbers with $), Annual Budget (formula: sum), YTD Actual (numbers with $), YTD Variance (formula: actual - budget pro-rated), Variance % (formula), Budget Owner (people)
> 2. **Spend Requests** — columns: Request Title (text), Department (dropdown), Category (dropdown), Amount (numbers with $), Requestor (people), Justification (long text), Urgency (status: Planned, Urgent, Emergency), Approval Status (status: Submitted, Manager Approved, Finance Approved, Rejected), Approver (people), Budget Impact (text), PO Number (text), Date Needed (date)
> 3. **Monthly Actuals** — columns: Department (dropdown), Month (date), Revenue Allocated (numbers with $), Total Spend (numbers with $), Salary Cost (numbers with $), Freelancer Cost (numbers with $), Tool/Software Cost (numbers with $), Travel (numbers with $), Other (numbers with $), Margin (formula), Budget Variance (formula)
>
> Automations: When Spend Request Amount exceeds $5K, require Finance approval. When Monthly Actuals Variance exceeds 10% over budget, alert CFO and Budget Owner. Dashboard with budget vs. actual by department, spending trend by category, approval pipeline, and margin tracker."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BudgetIQ
**Agent Purpose:** Provide real-time budget intelligence, automate variance analysis, and enable proactive financial planning.

**Triggers:**
- Monthly close: actual data available
- Spend request submitted
- Budget variance exceeds threshold (10%)
- Quarterly reforecast schedule
- New client win or loss impacting revenue plan

**Actions:**
- Compile monthly budget-to-actual analysis with variance explanations
- Route spend requests through appropriate approval chain based on amount and category
- Generate quarterly reforecast recommendations based on YTD trends
- Model revenue impact scenarios (client win/loss) on budget and headcount plan
- Send department heads weekly budget consumption updates
- Flag departments trending toward overspend with 60-day lookahead

**Data Required:**
- Approved annual budget by department and category
- Actual expense data from accounting system
- Revenue data and client portfolio changes
- Headcount plan and salary data
- Historical spending patterns

**Autonomy Level:** Fully Autonomous
Automated analysis and reporting. Spend approval routing follows predefined rules. Budget modifications require CFO approval.

**Example Interaction:**
> January close is complete. BudgetIQ compiles the analysis: "January Budget Report: Total agency spend: $4.1M vs. $3.9M budget (+$200K, +5.1%). Key variances: Creative department +$120K (freelancer overspend due to Samsung pitch staffing — expected to normalize). Technology +$65K (unbudgeted AI tool licenses — Midjourney Enterprise, Runway ML). Revenue is $4.8M vs. $4.5M budget (+$300K) driven by Coca-Cola project upside. Net margin: 17.1% vs. 15.4% budget. Recommendation: Technology overspend likely recurring — recommend Q2 reforecast adds $195K for AI tools across all departments. Creative freelancer spend should be reviewed against pitch calendar to anticipate future spikes."

---

### Use Case 6: Media Reconciliation & Financial Controls

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Media reconciliation — matching what was planned, what was bought, what was delivered, and what was billed — is the most labor-intensive finance process in advertising. A single media campaign might involve placements across 15 platforms (Google, Meta, TikTok, programmatic DSPs, CTV, DOOH, print, radio), each with different billing formats, currency, and timing. Media buyers track in their planning tools, platforms report in their dashboards, vendors invoice on their own schedules, and finance must reconcile everything. Discrepancies are rampant: makegoods (compensation for under-delivery), rate adjustments, added value placements, and billing errors. At scale, agencies process millions of dollars in media billings monthly with 3–5% discrepancy rates — meaning $30K–$50K per million must be reconciled.

#### The Solution
monday.com Work Management for media reconciliation workflow. Each media buy has a planned cost, actual platform spend, vendor invoice, and client billing — all tracked in a connected structure. Automations flag discrepancies exceeding thresholds, route makegoods for approval, and track resolution. Dashboards show reconciliation status and outstanding discrepancies.

#### The Outcome
- Media reconciliation cycle reduced from 45 days to 15 days
- 80% of discrepancies auto-flagged before they become billing errors
- Complete audit trail for every media dollar from plan to billing
- Finance team reclaims 40+ hours per month from manual reconciliation

#### Discovery Questions
1. "How long does your media reconciliation cycle take — from campaign delivery to final billing reconciliation?"
2. "What's your typical discrepancy rate between planned media cost and actual invoiced amount?"
3. "How do you track makegoods and added value placements — and do they get properly credited in client billing?"
4. "Could you survive a client billing audit right now — is there a clear trail from media plan to invoice?"

#### Industry Context
The ANA's 2023 programmatic transparency study found that only 36 cents of every programmatic dollar reaches the consumer as a working impression. The rest goes to tech fees, data fees, and non-transparent markups. Agencies are under enormous pressure to account for every media dollar. "Media auditing" firms like Ebiquity and FirmDecisions conduct annual audits for major advertisers, examining agency billing practices. Clean reconciliation is both a client retention tool and a compliance necessity.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Media Reconciliation workspace. Include:
> 1. **Media Buys** — columns: Campaign (text), Client (text), Platform (dropdown: Google Ads, Meta, TikTok, The Trade Desk, DV360, Amazon, CTV/Streaming, DOOH, Print, Radio, Other Programmatic), Flight Dates (timeline), Planned Spend (numbers with $), Actual Platform Spend (numbers with $), Vendor Invoice Amount (numbers with $), Client Billed Amount (numbers with $), Plan vs Actual Variance (formula), Invoice vs Actual Variance (formula), Reconciliation Status (status: Pending, In Progress, Reconciled, Discrepancy, Escalated), Media Buyer (people), Finance Owner (people)
> 2. **Discrepancy Log** — columns: Media Buy (connect to Media Buys), Discrepancy Type (dropdown: Over-Delivery, Under-Delivery, Rate Difference, Makegood, Added Value, Billing Error, Currency Adjustment), Amount (numbers with $), Explanation (long text), Resolution (dropdown: Credit Issued, Makegood Scheduled, Rate Adjusted, Write Off, Disputed), Resolution Status (status: Open, In Progress, Resolved), Owner (people)
>
> Automations: When Plan vs Actual Variance exceeds 5%, auto-create Discrepancy Log entry. When Reconciliation Status is 'Pending' for more than 30 days, escalate. Dashboard with total media under management, reconciliation progress, discrepancy by platform, and outstanding amounts."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MediaReconciler
**Agent Purpose:** Automate media spend reconciliation by matching planned, actual, invoiced, and billed amounts across platforms.

**Triggers:**
- Campaign flight end date reached
- Vendor media invoice received
- Platform spend report imported
- Monthly reconciliation deadline approaching

**Actions:**
- Match platform spend reports to planned media buys
- Flag discrepancies exceeding threshold (5% or $500, whichever is greater)
- Categorize discrepancies automatically (over/under-delivery, rate change, etc.)
- Generate reconciliation summary by client for billing review
- Track makegood commitments and verify delivery
- Produce monthly media audit report with platform-level detail

**Data Required:**
- Media plans with planned spend by platform
- Platform spend reports (API or manual import)
- Vendor invoices
- Client billing data
- Historical discrepancy patterns by platform

**Autonomy Level:** Human-in-the-Loop
Autonomous for matching and flagging. Discrepancy resolutions and makegood negotiations require human approval.

**Example Interaction:**
> Campaign flight for Coca-Cola's Q4 digital campaign ends. MediaReconciler pulls spend data from 6 platforms and begins reconciliation. Google Ads: planned $450K, actual $447K — within tolerance ✅. Meta: planned $380K, actual $395K — 3.9% over, auto-categorized as "over-delivery" (CPM came in lower than planned, more impressions served). The Trade Desk: planned $220K, invoiced $235K — $15K discrepancy flagged. Agent notes: "Invoice includes $15K for data segment fees not in original plan. Verify with media team if approved." TikTok: planned $150K, delivered $118K — under-delivery flagged. "32K under-delivery. Recommend requesting makegood. TikTok historically offers 120% of shortfall in added value." Summary sent to finance: "5 of 6 platforms reconciled. 2 items need review. Total planned: $1.6M. Total actual: $1.58M. Net variance: -$20K (1.3%)."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| SOW (Scope of Work) | Contractual document defining deliverables, fees, and terms between agency and client |
| Retainer | Monthly fee arrangement for ongoing agency services |
| Commission | Percentage of media spend paid to agency (historically 15%, now typically 2–5%) |
| Pass-Through | Costs paid by agency on behalf of client (media, production) that are billed back at cost |
| Markup | Percentage added to pass-through costs as agency revenue (typically 10–20% on production) |
| DSO (Days Sales Outstanding) | Average number of days to collect payment after invoicing |
| Blended Rate | Average hourly rate across agency team assigned to a client |
| Billable Utilization | Percentage of employee hours that are billed to clients |
| ASC 606 | Accounting standard for revenue recognition on long-term contracts |
| Makegood | Compensation (usually additional media) for under-delivery against a media buy |
| WIP (Work in Progress) | Unbilled work that has been performed but not yet invoiced |
| Gross Revenue | Total billings including pass-through (media, production) |
| Net Revenue | Agency fees and commissions only — the true measure of agency size |
| ANA | Association of National Advertisers — the major client-side industry body |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CFO | Financial strategy, margin targets, investor/holding company reporting | Decision-maker |
| VP of Finance / Controller | Day-to-day financial operations, billing, close, compliance | Decision-maker |
| Billing Manager | Client invoicing, pre-bill preparation, AR management | User/Influencer |
| Financial Analyst | Profitability analysis, forecasting, budget variance | User |
| Accounts Payable Manager | Vendor payments, PO management, expense reconciliation | User |
| Account Director | Client billing approval, SOW management, scope negotiations | Influencer |
| Head of Media | Media billing, reconciliation oversight, vendor terms | Influencer |
| CEO / Managing Director | P&L accountability, growth investment decisions, margin targets | Decision-maker |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Account Management | SOW management, client billing approval, scope change requests | Connect client-facing SOW management to financial tracking — single source of truth |
| Media | Media planning, buying, and reconciliation data | Automate media spend reconciliation — media data feeds directly into financial tracking |
| Production | Vendor management, production cost tracking, PO management | End-to-end production cost management from estimate to invoice to client billing |
| HR | Headcount planning, salary costs, freelancer spend | Unified workforce cost view — FTEs + freelancers + benefits = true labor cost per client |
| New Business / BD | Pipeline, pitch costs, revenue forecasting | Revenue pipeline visibility feeds directly into financial forecasting |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Maconomy (Deltek) | Agency-specific ERP for financial management | monday.com provides the workflow and collaboration layer that Maconomy lacks — complements ERP for day-to-day financial operations while Maconomy handles GL |
| Workamajig | All-in-one agency management (PM + finance) | monday.com is more flexible and modern — Workamajig is rigid and dated; monday.com integrates with best-of-breed finance tools rather than forcing a monolithic approach |
| Productive.io | Agency profitability and resource management | monday.com offers broader platform capabilities (CRM, Service, Dev) while matching Productive's profitability tracking through customization |
| Excel / Google Sheets | The incumbent for everything in agency finance | monday.com replaces the 15 spreadsheets that run agency finance with automated, connected, auditable workflows — the spreadsheet killer |
| Sage Intacct | Cloud financial management | Complementary — Sage handles accounting; monday.com handles the workflow, approvals, and collaboration around financial processes |
| FunctionFox | Simple agency time tracking and project costing | monday.com provides comprehensive work management that includes time tracking plus project management, billing, and resource management |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have an ERP (Maconomy/NetSuite/Sage) — we don't need another financial tool" | "Your ERP is the system of record — we're the system of action. ERPs are great at storing financial data; they're terrible at managing the workflows that produce that data. Pre-bill review, PO approvals, budget requests, reconciliation — that's all happening in email and spreadsheets today. monday.com automates those workflows and feeds clean data to your ERP." |
| "Financial data is too sensitive for a collaboration platform" | "monday.com provides enterprise-grade security — SOC 2 Type II, HIPAA-eligible, data encryption at rest and in transit. Permission controls ensure only authorized users see financial data. Most agencies already have client-facing data in monday.com — financial data gets the same protection." |
| "Our billing is too complex and unique for a standard tool" | "That's exactly why monday.com works — it's not a standard tool with rigid workflows. Your retainer + commission + markup + pass-through billing model gets built exactly the way you need it. Custom columns, formulas, and automations match your specific billing rules." |
| "We've tried automating billing before — it always breaks" | "Billing automation fails when it's all-or-nothing. monday.com doesn't try to replace your accountant — it automates the compilation and workflow (gathering data, routing approvals, flagging discrepancies) while humans still review and approve. The 80% of billing that's mechanical gets automated; the 20% that needs judgment stays human." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for agency using monday.com for client profitability tracking]
- [Placeholder for holding company standardizing financial workflows across agencies]
- [Placeholder for mid-market agency that reduced billing cycle time with monday.com]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
