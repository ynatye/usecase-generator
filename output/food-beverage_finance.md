# Food & Beverage × Finance Playbook

## Overview

Finance departments in Food & Beverage companies operate at the intersection of razor-thin margins, massive supply chain complexity, and volatile commodity markets. Whether it's a $500M mid-market snack producer or a $50B global CPG conglomerate like General Mills or Mondelēz, Finance teams must manage intricate cost structures where raw material inputs (flour, sugar, cocoa, dairy, oils, packaging) represent 40-60% of revenue and fluctuate daily on commodity exchanges. COGS management, trade spend optimization, and margin analysis by SKU/channel/customer are existential capabilities—a 1% margin improvement on a $2B revenue base is $20M straight to EBITDA.

F&B Finance organizations typically include FP&A (Financial Planning & Analysis), Controllership/Accounting, Treasury, Tax, Internal Audit, and increasingly, Revenue Growth Management (RGM) or Commercial Finance teams embedded with Sales. Headcounts range from 30-50 in mid-market companies to 500+ in global enterprises. The CFO is under constant pressure from the CEO and board to improve forecasting accuracy (commodity volatility makes this notoriously difficult), accelerate close cycles (many F&B companies still take 8-12 business days), optimize working capital (inventory carrying costs in cold-chain and perishable goods are enormous), and provide real-time visibility into profitability by product, customer, and channel.

The regulatory landscape includes SOX compliance for public companies, FDA cost reporting for government contracts, IFRS/GAAP complexities around inventory valuation (FIFO vs. weighted average in environments with spoilage and expiration), transfer pricing for multinational operations, and increasingly, ESG/sustainability financial reporting (Scope 3 emissions in supply chain, food waste costs). F&B Finance teams are drowning in manual processes—reconciling trade spend deductions, managing hundreds of vendor invoices, forecasting demand-driven financials, and producing the granular profitability analytics that the business demands.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | F&B Finance teams spend 60-70% of time on manual data gathering, reconciliation, and reporting—AI can automate the grunt work and free analysts for strategic insight |
| 2 | Scale Impact Without Overhead | High | As F&B companies grow through acquisition (a dominant growth strategy), Finance must absorb new entities without proportional headcount increases |
| 3 | Consolidate Tech Stack with AI | Medium-High | F&B Finance stacks are fragmented across ERP, EPM, trade management, commodity hedging, and BI tools—consolidation reduces cost and integration burden |

## Prioritized Use Cases

---

### Use Case 1: Trade Spend Management & Deduction Tracking

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Trade spend—the promotional funds, slotting fees, volume rebates, and markdown allowances that F&B companies pay to retailers—typically represents 15-25% of gross revenue, making it the second-largest line item after COGS. A $1B F&B company may spend $150M-$250M annually on trade promotions. Yet most companies cannot accurately track, reconcile, or measure ROI on this spend. Retailer deductions arrive as cryptic line items on remittance statements, often 60-90 days after the promotion ran. Finance teams employ 5-15 "deduction analysts" who manually match deductions to promotions, dispute invalid deductions (15-30% of deductions are invalid or duplicative), and reconcile against accruals. The average company writes off 2-5% of trade spend as unresolved—that's $3M-$12.5M in pure margin leakage for a $1B company. Trade promotion management (TPM) systems like Exceedra or AFS exist but cost $500K-$2M to implement and still require heavy manual reconciliation.

#### The Solution
monday.com Work Management as a trade spend tracking and deduction resolution system. A **Promotion Calendar Board** tracking every trade promotion: Promotion Name (text), Retailer/Customer (dropdown: Walmart, Kroger, Costco, Target, Albertsons, etc.), Brand/Product Line (dropdown), Promotion Type (dropdown: BOGO, Temporary Price Reduction, Shipper Display, Slotting Fee, Volume Rebate, MDF, Scan-Back, Bill-Back), Start Date (date), End Date (date), Committed Spend (numbers, USD), Actual Spend (numbers, USD), Variance (formula), Incremental Volume Target (numbers, cases), Actual Incremental Volume (numbers), ROI (formula: incremental revenue / actual spend), Status (status: Planned/Active/Closed/Reconciled), Sales Owner (people), Finance Owner (people). A connected **Deduction Resolution Board**: Deduction ID (text), Invoice Number (text), Retailer (dropdown), Amount (numbers), Deduction Reason Code (dropdown: Promotion, Shortage, Damage, Pricing, Freight, Unsupported), Linked Promotion (connect to Promotion Calendar), Status (status: New/Under Review/Approved/Disputed/Escalated/Written Off), Age (formula: days since created), Resolution (dropdown), Analyst (people).

#### The Outcome
Recover 30-50% of previously written-off deductions ($1M-$6M annually for a $1B company). Reduce deduction resolution cycle from 45 days to 15 days. Provide real-time trade spend ROI visibility to commercial teams. Cut deduction analyst headcount needs by 40% through automation of matching and routing.

#### Discovery Questions
1. "What percentage of your gross revenue goes to trade spend, and can you tell me the ROI on your top 10 promotions last year?"
2. "How many people on your Finance team work on deduction resolution, and what's the average time from deduction receipt to resolution?"
3. "What percentage of retailer deductions do you ultimately write off as unresolvable—and what does that represent in dollar terms?"
4. "Walk me through what happens when a $50,000 deduction hits from Walmart—how does your team determine if it's valid?"
5. "Do your Sales and Finance teams have a shared view of promotion performance, or do they operate from different data sets?"

#### Industry Context
Trade spend in F&B is uniquely complex because of the power dynamic with retailers. Companies like Walmart, Kroger, and Costco dictate promotion mechanics and take deductions unilaterally. Deduction reason codes vary by retailer and are often vague ("promotional allowance" could mean 10 different things). Bill-back vs. scan-back vs. off-invoice promotions each have different reconciliation workflows. TPO (Trade Promotion Optimization) is a hot topic—AI-driven promotion planning that predicts lift by retailer/product/promotion type. Revenue Growth Management (RGM) teams increasingly own trade strategy but lack real-time data from Finance on actual vs. planned spend.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a trade spend management system for a food and beverage company. Create a board called 'Promotion Calendar' with columns: Promotion ID (auto-number), Promotion Name (text), Retailer (dropdown: Walmart, Kroger, Costco, Target, Albertsons-Safeway, Publix, Ahold Delhaize, Club Channel, Convenience Channel, Other), Brand (dropdown: Brand A Snacks, Brand B Beverages, Brand C Bakery, Brand D Frozen), Product Line (dropdown), Promotion Type (dropdown: BOGO, Temporary Price Reduction, Shipper Display, End Cap, Slotting Fee, Volume Rebate, MDF Co-Marketing, Scan-Back, Bill-Back, Off-Invoice), Start Date (date), End Date (date), Planned Spend (numbers, USD), Actual Spend (numbers, USD), Spend Variance (formula: actual minus planned), Baseline Volume (numbers, cases), Incremental Volume Target (numbers, cases), Actual Incremental Volume (numbers, cases), Lift Percentage (formula), Trade ROI (formula: incremental revenue divided by actual spend), Status (status: Planned/Submitted/Active/Complete/Reconciled/Disputed), Sales Owner (people), Finance Owner (people), Accrual Posted (checkbox), Notes (long text). Create a connected board called 'Deduction Tracker' with columns: Deduction ID (text), Invoice Reference (text), Retailer (dropdown, same as above), Deduction Amount (numbers, USD), Deduction Date (date), Reason Code (dropdown: Promotion Allowance, Shortage, Damage, Pricing Error, Freight Allowance, New Item Fee, Unsupported-No Backup, Duplicate, Other), Linked Promotion (connect to Promotion Calendar), Assigned Analyst (people), Status (status: New/Under Review/Valid-Approved/Disputed/Escalated to Sales/Written Off/Recovered), Days Open (formula: today minus deduction date), Resolution Amount (numbers), Resolution Date (date), Dispute Notes (long text). Add automations: when a new deduction is created, auto-assign to analyst based on retailer; when Days Open exceeds 30, change status to Escalated and notify Finance Manager; when Promotion Status changes to Complete, check for unmatched deductions and alert Finance Owner; when Deduction status is Written Off and amount exceeds $10000, require Finance Director approval. Create a Dashboard with: total trade spend by retailer (pie chart), promotion ROI by type (bar chart), open deductions by age bucket (chart: 0-15 days, 16-30, 31-60, 60+), write-off trending monthly (line chart), top 10 promotions by ROI (table), deduction recovery rate (number widget percentage), total spend vs budget by quarter (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** TradeReconciler AI
**Agent Purpose:** Automatically match retailer deductions to promotions, identify invalid deductions for dispute, and provide real-time trade spend ROI analytics.

**Triggers:**
- New deduction batch imported (weekly retailer remittance processing)
- Deduction unresolved for 20+ days
- Promotion end date passed (trigger reconciliation)
- Monthly close cycle initiated
- Deduction flagged as potential duplicate (amount + retailer + date match)

**Actions:**
- Auto-match incoming deductions to promotions using retailer, date range, amount, and product code fuzzy matching (80%+ match rate target)
- Flag unmatched deductions for manual review with suggested possible promotion matches ranked by confidence score
- Identify potential invalid deductions (amount exceeds promotion commitment, deduction taken outside promotion window, duplicate deduction)
- Generate dispute packages with supporting documentation (promotion agreement, POS data, shipment records) for invalid deductions
- Calculate real-time promotion ROI as deductions are resolved and actual spend is confirmed
- Produce monthly trade spend variance reports comparing planned vs. actual by retailer and promotion type

**Data Required:**
- Promotion Calendar board, Deduction Tracker board
- Retailer remittance/deduction files (EDI 812 or CSV imports)
- Promotion agreements/contracts (document links)
- Shipment and POS data for volume verification
- Historical deduction patterns by retailer for anomaly detection

**Autonomy Level:** Human-in-the-Loop
Deduction matching (high confidence >90%), duplicate detection, and reporting are fully autonomous. Dispute initiation, write-off decisions, and promotion accrual adjustments require analyst or manager approval.

**Example Interaction:**
> Monday morning: the weekly deduction batch from Kroger arrives—247 line items totaling $1.8M. The TradeReconciler agent processes the batch in minutes. It auto-matches 198 deductions (80%) to active or recently completed promotions with high confidence. Of the remaining 49, it identifies 12 as likely duplicates of previously resolved deductions (same amount, same store, same week), flags 8 as taken outside the valid promotion window (deduction date is 3 weeks after promotion end), and routes 29 to the appropriate analyst with suggested promotion matches ranked by confidence.
>
> For the 12 suspected duplicates, it generates dispute packages with side-by-side comparisons of the original and duplicate deductions, totaling $67,000 in potential recovery. It sends these to the analyst for one-click dispute submission. For the 8 out-of-window deductions ($43,000), it pulls the promotion agreement showing the valid dates and prepares dispute letters.
>
> By Tuesday, the analyst has reviewed and approved 18 of 20 auto-generated disputes and resolved 22 of the 29 manual matches. The agent updates the Promotion Calendar with actual spend figures and recalculates ROI for 15 recently completed promotions. The Finance Director's dashboard now shows real-time trade spend tracking: $42.3M YTD against a $45M plan, with a 3.2:1 average promotion ROI and a 78% deduction recovery rate (up from 62% last year).

---

### Use Case 2: Financial Close Process Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The monthly financial close in F&B companies is a complex, time-pressured process involving 150-400 discrete tasks across Accounting, FP&A, Tax, Treasury, and business unit controllers. F&B-specific complexities include inventory valuation with spoilage/expiration adjustments, intercompany eliminations for multi-plant operations, trade spend accrual true-ups, commodity hedge mark-to-market entries, co-manufacturing reconciliations, and slotting fee amortization. Most F&B companies take 8-12 business days to close, with a goal of reaching 5-day close. The process is managed through a combination of Excel checklists, email chains, and shared drives. Bottlenecks are invisible until they cause delays—a single late journal entry from one plant can hold up the consolidated P&L. Controllers spend 60% of close week chasing status updates rather than reviewing quality.

#### The Solution
monday.com Work Management as a close management platform. A **Close Calendar Board** with every close task as an item: Task Name (text), Task Owner (people), Reviewer (people), Business Unit/Entity (dropdown: Corporate, Plant A, Plant B, Plant C, International), Task Category (dropdown: Subledger Close, Journal Entries, Reconciliations, Accruals, Intercompany, Consolidation, Reporting, Flux Analysis), Due Date (date), Due Time (text), Dependency (connect to predecessor tasks), Status (status: Not Started/In Progress/Under Review/Complete/Blocked), Completion Date (date), Variance to Due (formula), Attachments (files for workpapers), Period (dropdown: month). **Automations** enforce dependencies: downstream tasks can't start until predecessors complete. Blocked tasks auto-notify the blocker's manager. **Dashboard** shows real-time close progress: percentage complete, tasks by status, overdue items, critical path highlighting.

#### The Outcome
Reduce close cycle from 10 business days to 6 business days. Eliminate 80% of "status chasing" communication (4-6 hours per controller per close). Identify bottlenecks in real-time rather than retrospectively. Achieve 100% close task documentation for SOX compliance. Enable continuous improvement by tracking close-over-close cycle time trends.

#### Discovery Questions
1. "How many business days does your monthly close currently take, end-to-end, and what's your target?"
2. "How many discrete tasks are in your close checklist, and how do you track their completion today?"
3. "What's the biggest bottleneck in your close process—the task that most often holds everything else up?"
4. "How much time do your controllers spend chasing status updates during close week versus actually reviewing entries?"
5. "For SOX purposes, can you demonstrate that every close task was completed, reviewed, and approved with timestamps and documentation?"

#### Industry Context
F&B close processes have unique complexity drivers: inventory is perishable with expiration-based write-down rules, requiring physical inventory counts and system-to-physical reconciliations. Trade spend accruals must be trued up against actual deductions (see Use Case 1). Commodity hedging positions require mark-to-market adjustments under ASC 815. Co-manufacturing and co-packing arrangements require complex intercompany accounting. Seasonal demand patterns mean close complexity varies by month (Q4 holiday season close is significantly more complex). Multi-currency transactions are common for companies sourcing ingredients globally.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a financial close management system for a food and beverage company. Create a board called 'Monthly Close Tracker' with columns: Task ID (auto-number), Task Name (text), Task Owner (people), Reviewer-Approver (people), Entity (dropdown: Corporate Consolidated, Plant A Chicago, Plant B Dallas, Plant C Atlanta, International UK, International Canada), Category (dropdown: Subledger Close - AP, Subledger Close - AR, Subledger Close - Inventory, Journal Entries, Account Reconciliations, Accruals - Trade Spend, Accruals - Compensation, Intercompany Eliminations, Commodity Hedge MTM, Consolidation, Management Reporting, Flux Analysis, Tax Provision), Close Day Due (dropdown: Day 1, Day 2, Day 3, Day 4, Day 5, Day 6, Day 7, Day 8, Day 9, Day 10), Due Date (date), Dependency - Predecessor (connect to same board), Status (status: Not Started/In Progress/Under Review/Approved/Complete/Blocked/N-A), Completion Timestamp (date), Workpaper Attached (checkbox), SOX Control (checkbox), Review Notes (long text), Variance Explanation (long text). Add subitems for sub-tasks within major tasks. Add automations: when a predecessor task status changes to Complete, notify the dependent task owner that they can begin; when status is still Not Started on the Due Date, change to Blocked and notify the task owner plus their manager; when all tasks for an Entity reach Complete, notify the Corporate Controller; when SOX Control is checked and Workpaper Attached is not checked and Status is Complete, flag as non-compliant. Create a Dashboard with: overall close progress percentage (number widget), tasks by status (pie chart), overdue tasks list (table), close progress by entity (stacked bar), close progress by day (timeline/gantt showing planned vs actual), average days to close trending (line chart, last 12 months), blocked tasks requiring attention (table with owner and dependency info). Add a Gantt/Timeline view showing task dependencies and critical path."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CloseCommand Orchestrator
**Agent Purpose:** Manage the monthly financial close process end-to-end, enforcing deadlines, resolving bottlenecks, and ensuring audit-ready documentation.

**Triggers:**
- Close cycle initiated (1st business day after period end)
- Task due date approaching (same-day morning notification)
- Task status changed to Blocked
- All predecessor tasks for a dependent task completed
- Close Day milestone reached (end of each close day)

**Actions:**
- Auto-generate the monthly close task list from the master template, adjusting dates for the specific month and carrying forward any open items from prior close
- Send targeted morning briefings to each task owner listing their tasks due today and any new dependencies unlocked
- Detect critical path bottlenecks in real-time and send escalation notifications to controllers and the CFO
- Generate end-of-day close status reports showing completed vs. planned, highlighting at-risk items
- Verify SOX compliance gates: flag any completed SOX-control tasks missing workpaper attachments or reviewer sign-off
- Post-close: generate close retrospective report comparing planned vs. actual timelines by entity and category, identifying improvement opportunities

**Data Required:**
- Monthly Close Tracker board (master template + current period)
- Task dependency map
- Historical close performance data (cycle times by task, entity)
- SOX control matrix (which tasks are SOX-relevant)
- Calendar/schedule data for task owners (availability during close)

**Autonomy Level:** Fully Autonomous with Escalation
Task generation, notifications, dependency management, status reporting, and SOX compliance checking are fully autonomous. Extending deadlines, waiving dependencies, and approving journal entries require human authorization.

**Example Interaction:**
> It's Day 3 of the January close. The CloseCommand agent's morning briefing reports: 68% of tasks complete (ahead of the 60% Day 3 target), but flags two critical items. First, the Plant B inventory reconciliation (a Day 2 task) is still In Progress due to a physical count discrepancy of $180K in packaging materials. This is blocking the consolidated inventory valuation and the COGS flash. The agent has already notified the Plant B Controller and the Corporate Inventory Manager, providing the specific discrepancy detail.
>
> Second, the trade spend accrual true-up is blocked because the Kroger deduction file hasn't been received yet (it's typically available by Day 2). The agent checks historical patterns and notes that Kroger's file was late in 3 of the last 12 months, always arriving by Day 4. It recommends the analyst proceed with an estimated accrual using historical averages and post a true-up entry when the file arrives, flagging this recommendation to the Senior Accountant for approval.
>
> By end of Day 3, the agent generates the daily status report for the CFO: 72% complete, two items at risk but mitigated, projected close completion on Day 6 (target: Day 7). The CFO reviews the one-page summary in 2 minutes instead of attending a 30-minute status call.

---

### Use Case 3: Capital Expenditure (CapEx) Request & Tracking

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
F&B companies are capital-intensive, investing heavily in production line expansions, packaging equipment, cold storage facilities, warehouse automation, and food safety infrastructure. Annual CapEx budgets range from $20M-$500M+ depending on company size. The CapEx request and approval process is typically managed through email chains, Word documents, and Excel spreadsheets with no standardized workflow. Engineers submit capital requests with inconsistent financial justifications, approvals stall in email inboxes (average approval cycle: 6-8 weeks), and post-approval tracking is almost non-existent—Finance often doesn't know if a $2M approved project is on budget until the invoices come in. 30-40% of approved CapEx is not spent within the fiscal year (underspend), while critical projects are delayed waiting for approval.

#### The Solution
monday.com Work Management as a CapEx lifecycle management platform. A **CapEx Request Board** with: Project Name (text), Requesting Plant/BU (dropdown), Category (dropdown: Production Line - New, Production Line - Upgrade, Packaging Equipment, Cold Storage, Warehouse/Logistics, Food Safety/Compliance, IT Infrastructure, Facility Maintenance, Sustainability/Energy), Total Estimated Cost (numbers), NPV (numbers), IRR (numbers, percentage), Payback Period (numbers, months), Strategic Priority (dropdown: Growth, Efficiency, Compliance/Mandatory, Sustainability), Requestor (people), Sponsor (people), Finance Reviewer (people), Approval Status (status: Draft/Submitted/Finance Review/VP Approval/CFO Approval/Board Approval/Approved/Rejected/On Hold), Approval Thresholds tied to amount (<$100K=VP, <$500K=CFO, >$500K=Board). A connected **CapEx Spend Tracking Board** tracking actual spend against approved budget with PO references, invoice amounts, and variance analysis.

#### The Outcome
Reduce CapEx approval cycle from 6-8 weeks to 2-3 weeks. Achieve 90%+ CapEx utilization (vs. 60-70% typical). Provide real-time CapEx budget vs. actual visibility to the CFO. Standardize financial justification quality across all requests.

#### Discovery Questions
1. "What's your total CapEx budget this year, and what percentage of last year's approved CapEx was actually spent?"
2. "Walk me through the approval process for a $500K production line upgrade—how many approvers, how long does it take?"
3. "How do you track actual spending against approved CapEx projects—do you have real-time visibility or do you reconcile quarterly?"
4. "When you have more CapEx requests than budget, how do you prioritize—is there a standardized scoring framework?"
5. "Have you ever had a CapEx project significantly exceed its approved budget before Finance became aware?"

#### Industry Context
F&B CapEx is driven by several industry-specific factors: production line changeovers for new product launches (SKU proliferation drives frequent equipment modifications), FDA/USDA compliance upgrades (e.g., FSMA-mandated preventive controls equipment), cold chain infrastructure for temperature-sensitive products, sustainability investments (energy-efficient refrigeration, waste reduction, water recycling), and automation to address labor shortages. Many projects require phased spending across fiscal years. Lease vs. buy decisions are common for expensive equipment like aseptic filling lines ($5M-$20M). Post-implementation OEE (Overall Equipment Effectiveness) validation is critical but rarely tracked.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a capital expenditure request and tracking system for a food and beverage manufacturer. Create a board called 'CapEx Requests' with columns: Project ID (auto-number), Project Name (text), Requesting Plant-BU (dropdown: Plant A Chicago, Plant B Dallas, Plant C Atlanta, Distribution Network, Corporate IT, R&D Center), Category (dropdown: New Production Line, Line Upgrade-Retrofit, Packaging Equipment, Cold Storage-Refrigeration, Warehouse Automation, Food Safety Compliance, IT Infrastructure, Facility Maintenance, Sustainability-Energy, Fleet-Vehicles), Total Estimated Cost (numbers, USD), Annual Operating Savings (numbers, USD), NPV at 10 Percent (numbers, USD), IRR (numbers, percentage), Payback Period Months (numbers), Strategic Alignment (dropdown: Revenue Growth, Cost Reduction, Compliance-Mandatory, Sustainability ESG, Safety, Quality Improvement), Requestor (people), VP Sponsor (people), Finance Business Partner (people), Business Case Document (files), Approval Status (status: Draft/Submitted/Finance Review/VP Review/CFO Review/Board Review/Approved/Rejected/Deferred), Approval Date (date), Target Completion Date (date), Budget Year (dropdown: FY26, FY27, FY28), Priority Rank (numbers). Create a connected board called 'CapEx Spend Tracker' with columns: Project (connect to CapEx Requests), PO Number (text), Vendor (text), Description (text), PO Amount (numbers, USD), Invoice Amount (numbers, USD), Payment Date (date), Running Total Spent (formula), Budget Remaining (formula), Percent Spent (formula), Status (status: PO Issued/Received/Invoiced/Paid/Closed). Add automations: when CapEx Request Approval Status changes to Submitted, if Total Estimated Cost is under 100000 assign to VP Review, if between 100000 and 500000 assign to CFO Review, if over 500000 assign to Board Review; when Running Total Spent on Spend Tracker exceeds 80% of approved budget, notify Finance Business Partner; when all Spend Tracker items for a project are Closed, mark the CapEx Request as Complete. Create a Dashboard with: total CapEx budget vs committed vs spent (gauge chart), spend by category (pie chart), approval pipeline status (funnel), top 10 projects by budget (table with spend progress bars), monthly spend curve actual vs plan (line chart), projects over budget (table filtered to variance > 0)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CapExNavigator
**Agent Purpose:** Streamline capital expenditure lifecycle from request through post-implementation tracking, ensuring financial rigor and budget discipline.

**Triggers:**
- New CapEx request submitted
- Approval status unchanged for 5+ business days (stale approval)
- Project spend reaches 50%, 80%, and 100% of approved budget
- Quarter-end approaching (trigger CapEx forecast refresh)
- Project target completion date approaching (30 days prior)

**Actions:**
- Validate CapEx request completeness (all financial metrics calculated, business case attached, sponsor assigned) before routing to approval
- Auto-route to appropriate approval chain based on amount thresholds
- Send approval reminders and escalate stale requests to the approver's manager
- Generate quarterly CapEx forecast reports comparing approved vs. committed vs. spent vs. forecast-to-complete
- Flag projects trending over budget (>10% variance) with root cause analysis request to project owner
- Post-completion: generate ROI validation report comparing actual NPV/IRR against business case projections

**Data Required:**
- CapEx Requests board, Spend Tracker board
- ERP purchase order and invoice data
- Approved budget by BU and category
- Historical project performance (actual vs. budgeted spend and timeline)
- Asset depreciation schedules

**Autonomy Level:** Human-in-the-Loop
Request validation, routing, reminders, and reporting are fully autonomous. All approval decisions, budget reallocation, and project scope changes require human authorization.

**Example Interaction:**
> The VP of Manufacturing at Plant A submits a $1.2M CapEx request for a new high-speed packaging line to support a product launch in Q3. The CapExNavigator agent validates the submission: NPV is positive ($340K), IRR is 18% (above the 12% hurdle rate), payback is 22 months, and the business case document is attached. It routes the request to CFO Review (amount > $500K) and Board Review.
>
> The CFO reviews and approves within 3 days. The request moves to board queue. The agent notices the board doesn't meet for 3 weeks and flags the timeline risk to the CFO: "Project needs equipment ordered by March 15 to meet Q3 launch. Board meeting is March 20. Recommend email ballot or delegated authority." The CFO approves via delegated authority.
>
> Over the next 4 months, the agent tracks spending: $280K PO for the packaging machine, $95K for installation, $45K for electrical work. When the running total hits $840K (70% of budget) with significant line items still pending (conveyor integration, commissioning), the agent projects total spend at $1.35M—12.5% over budget. It alerts the Finance Business Partner with a detailed variance breakdown and requests a revised forecast from the project manager. The overage is identified (steel price increases on custom conveyor) and a budget amendment is submitted through the standard approval flow.

---

### Use Case 4: Budget Planning & Rolling Forecasts

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Annual budget planning in F&B companies is a 3-4 month marathon involving hundreds of stakeholders across plants, business units, and functions. FP&A teams collect budget inputs through emailed Excel templates, consolidate manually (often 50-100 spreadsheets), reconcile discrepancies, iterate through 4-6 revision cycles, and produce the final budget package for board approval. The process consumes 30-50% of FP&A's annual capacity. Worse, the resulting budget is outdated within 90 days due to commodity price movements, demand shifts, and competitive dynamics. Rolling forecasts (monthly or quarterly reforecasts) are the answer, but most F&B Finance teams don't have the bandwidth to run a rigorous rolling forecast on top of the annual budget—they're too busy with the close and ad-hoc requests. EPM tools (Anaplan, Adaptive Insights) solve this technically but cost $200K-$1M+ and require 6-12 months to implement.

#### The Solution
monday.com Work Management as a budget planning coordination and rolling forecast management platform. A **Budget Planning Board** managing the annual process: Budget Line Item (text), Business Unit (dropdown), Plant (dropdown), Category (dropdown: Revenue, COGS - Raw Materials, COGS - Packaging, COGS - Labor, COGS - Overhead, SG&A, Trade Spend, R&D, CapEx), Budget Owner (people), Draft Amount (numbers), Revision 1 (numbers), Revision 2 (numbers), Final Approved (numbers), Status (status: Not Started/Draft Submitted/Under Review/Approved/Locked), Due Date (date), FP&A Reviewer (people), Notes (long text). A **Rolling Forecast Board** with monthly columns showing forecast vs. actual by category and BU, with variance analysis and commentary. **Dashboard** showing budget-to-actual variance by BU, commodity cost impact, and forecast accuracy trending.

#### The Outcome
Reduce annual budget cycle from 14 weeks to 8 weeks. Enable monthly rolling forecasts without additional FP&A headcount. Improve forecast accuracy from ±15% to ±5% through more frequent reforecasting. Provide CFO with real-time budget variance visibility rather than quarterly surprises.

#### Discovery Questions
1. "How long does your annual budget process take end-to-end, and how many revision cycles do you go through?"
2. "How many Excel spreadsheets does your FP&A team consolidate during budgeting—and how many hours go into reconciling them?"
3. "Do you currently run rolling forecasts, and if so, how frequently and how much FP&A time does each cycle consume?"
4. "What's your typical budget-to-actual variance by the end of Q1—and how much of that is driven by commodity prices versus volume?"
5. "If a major customer like Walmart changes an order forecast mid-year, how quickly can your Finance team model the P&L impact?"

#### Industry Context
F&B budgeting is uniquely challenging because 40-60% of COGS (raw materials) is driven by volatile commodity markets. Sugar, cocoa, dairy, wheat, and oil prices can swing 20-40% in a year. Demand planning is complex with seasonal patterns (ice cream in summer, baking products in Q4), promotional lifts, and new product launches. Many F&B companies budget at the SKU × customer × period level for revenue and the ingredient × plant × period level for COGS, creating massive data volumes. Transfer pricing between plants and entities adds another layer. Companies with acquisition-driven growth often have disparate budgeting processes across legacy entities that need harmonization.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a budget planning coordination system for a food company. Create a board called 'Annual Budget Planning' with columns: Budget Category (dropdown: Net Revenue, COGS Raw Materials, COGS Packaging, COGS Direct Labor, COGS Manufacturing Overhead, Gross Profit, Trade Spend, Sales and Marketing, R&D, G&A, EBITDA, CapEx, Working Capital), Business Unit (dropdown: Snacks Division, Beverages Division, Bakery Division, International, Corporate), Plant-Location (dropdown), Budget Owner (people), FP&A Analyst (people), Prior Year Actual (numbers, USD), Current Year Forecast (numbers, USD), Budget Draft v1 (numbers, USD), Budget Draft v2 (numbers, USD), Budget Final (numbers, USD), YoY Change Percent (formula), Status (status: Template Sent/Draft Due/Submitted/In Review/Approved/Locked), Draft Due Date (date), Assumptions-Notes (long text). Create a second board called 'Monthly Rolling Forecast' with columns: Month (dropdown: Jan through Dec), Category (dropdown, same as above), Business Unit (dropdown, same), Budget (numbers), Prior Forecast (numbers), Current Forecast (numbers), Actual (numbers), Budget Variance (formula), Forecast Variance (formula), Commentary (text), Confidence (status: High/Medium/Low), Updated By (people), Last Updated (date). Add automations: when Budget Status is still Template Sent 3 days before Draft Due Date, remind Budget Owner; when all Budget items for a BU are Approved, notify the CFO; when Actual exceeds Budget by more than 10 percent on Rolling Forecast, flag as attention needed. Create a Dashboard with: total company P&L summary budget vs forecast vs actual (table), variance by BU (bar chart), COGS composition budget vs actual (stacked bar), forecast accuracy trend by month (line chart), budget completion status by BU (progress bars), top 10 variance items requiring commentary (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ForecastPilot
**Agent Purpose:** Automate budget coordination workflows and generate rolling forecast updates using actuals data, reducing FP&A manual effort by 50%.

**Triggers:**
- Annual budget cycle kicked off (auto-generate templates and assignments)
- Budget draft due date approaching (3-day, 1-day, overdue reminders)
- Monthly actuals available (close complete signal)
- Commodity price index updated (weekly)
- Significant demand forecast change from Sales/Operations

**Actions:**
- Auto-populate budget templates with prior year actuals, current year forecast, and calculated growth rates as starting points
- Track budget submission status and send targeted reminders to late submitters with escalation to their VP
- After monthly close, auto-update the Rolling Forecast board with actuals and calculate variances
- Generate variance commentary drafts for items >5% off budget, using prior month patterns and known drivers
- Model commodity cost impact scenarios when prices move >5% (e.g., "Cocoa is up 12% → estimated $2.3M COGS impact on Bakery Division")
- Produce monthly CFO forecast package with executive summary, key variances, and updated full-year outlook

**Data Required:**
- Annual Budget Planning board, Monthly Rolling Forecast board
- ERP/GL actuals data (monthly export)
- Commodity price feeds (CME, ICE)
- Sales demand forecast from S&OP process
- Historical forecast accuracy data for calibration

**Autonomy Level:** Human-in-the-Loop
Template generation, reminder workflows, actuals updating, and variance calculations are fully autonomous. Forecast adjustments, assumption changes, and executive reporting require FP&A analyst review.

**Example Interaction:**
> It's the 8th business day of February. The January close just completed, and actuals are loaded. The ForecastPilot agent auto-updates the Rolling Forecast board with January actuals across all BUs and categories. It immediately identifies three significant variances: (1) Snacks Division raw material COGS is $800K over budget due to a 15% palm oil price spike. (2) Beverages Division revenue is $1.2M under budget due to a delayed Walmart promotional program. (3) G&A is $300K under budget due to a hiring freeze impact.
>
> For each variance, the agent generates commentary drafts: "Palm oil spot prices averaged $1,180/MT in January vs. $1,025/MT budgeted (+15.1%). Impact: $800K unfavorable COGS. Hedging position covers 60% of Q1 volume; unhedged exposure at current prices would add $1.4M impact in Feb-Mar. Recommendation: Extend hedge coverage and evaluate reformulation options." The FP&A analyst reviews, refines the commentary, and approves. The agent compiles the monthly CFO package with a revised full-year outlook: EBITDA now forecast at $48.2M vs. $50.0M budget, with identified mitigation actions worth $1.1M.

---

### Use Case 5: Accounts Payable Automation & Vendor Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
F&B companies process enormous volumes of vendor invoices—raw material suppliers (dairy farms, grain elevators, flavor houses), packaging vendors, co-manufacturers, logistics providers, equipment maintenance companies, and ingredient brokers. A mid-size F&B company processes 2,000-5,000 invoices per month; large enterprises process 20,000+. AP teams manually key invoices, perform 3-way matching (PO → receipt → invoice), chase approvals, manage early payment discounts (2/10 net 30 terms that are frequently missed, costing 36% annualized), handle vendor inquiries, and ensure compliance with vendor payment terms that vary widely (ingredient suppliers often demand net 15; equipment vendors allow net 60). AP staff-per-invoice ratios in F&B are often 1:500-1:800 monthly, leading to backlogs, missed discounts, duplicate payments (1-3% of AP spend), and strained vendor relationships.

#### The Solution
monday.com Work Management as an AP workflow and exception management platform. An **Invoice Processing Board** with: Invoice Number (text), Vendor Name (dropdown from vendor master), Invoice Date (date), Amount (numbers), PO Reference (text), 3-Way Match Status (status: Auto-Matched/Discrepancy/No PO), Category (dropdown: Raw Materials, Packaging, Co-Manufacturing, Logistics, Maintenance, Utilities, Services, Other), Approver (people), Approval Status (status: Pending/Approved/Rejected/On Hold), Payment Due Date (date), Early Discount Available (checkbox), Discount Deadline (date), Payment Status (status: Scheduled/Paid/Void), AP Clerk (people). A connected **Vendor Scorecard Board** tracking on-time delivery, quality ratings, invoice accuracy, and payment performance.

#### The Outcome
Capture 90%+ of early payment discounts (vs. typical 40-50%), saving $500K-$2M annually. Reduce duplicate payments to near-zero. Cut invoice processing cycle from 12 days to 4 days. Free up 2-3 AP FTEs through automation of matching and routing.

#### Discovery Questions
1. "How many invoices does your AP team process per month, and what's the average cost to process a single invoice?"
2. "What percentage of your vendors offer early payment discounts, and how often do you actually capture them?"
3. "When was the last time you discovered a duplicate payment—and how was it found?"
4. "How long does it take from invoice receipt to payment, and where in that process do invoices typically get stuck?"
5. "How do you evaluate vendor performance beyond just price—delivery reliability, invoice accuracy, quality consistency?"

#### Industry Context
F&B AP has unique characteristics: commodity-based invoices often have price adjustments based on market indices (e.g., dairy invoices adjusted to CME Class III milk prices), requiring verification against contract formulas. Co-manufacturing invoices include yield reconciliations (actual vs. expected output from provided ingredients). Logistics invoices require rate verification against contracted lane rates. Many F&B companies use consignment inventory models with suppliers, requiring complex settlement calculations. Vendor consolidation is a major initiative—reducing from 500+ suppliers to 200-300 through strategic sourcing, but this requires tracking and justification.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an accounts payable workflow and vendor management system for a food and beverage company. Create a board called 'Invoice Processing' with columns: Invoice ID (auto-number), Vendor Name (dropdown: list of top 30 vendors by spend), Invoice Number (text), Invoice Date (date), Invoice Amount (numbers, USD), PO Number (text), Receipt Confirmed (checkbox), Three Way Match (status: Auto Matched/Price Variance/Quantity Variance/No PO/No Receipt), Variance Amount (numbers), Category (dropdown: Raw Materials, Packaging Materials, Co-Manufacturing, Freight and Logistics, Equipment Maintenance, Utilities, Professional Services, Contract Labor, Ingredients-Flavors, Other), Cost Center (dropdown: Plant A, Plant B, Plant C, Distribution, Corporate, R&D), Approver (people), Approval Status (status: Auto-Approved/Pending Approval/Approved/Rejected/On Hold), Early Pay Discount (dropdown: None, 1 Percent 10 Net 30, 2 Percent 10 Net 30, 2.5 Percent 15 Net 45), Discount Deadline (date), Payment Due Date (date), Payment Status (status: Not Scheduled/Scheduled/Paid/Void), AP Processor (people), Notes (text). Create a connected board called 'Vendor Scorecard' with: Vendor Name (text), Category (dropdown), Annual Spend (numbers), Invoice Volume Monthly (numbers), On Time Delivery Percent (numbers), Quality Rating (numbers, 1-5), Invoice Accuracy Percent (numbers), Average Payment Days (numbers), Contract Expiration (date), Strategic Tier (status: Strategic/Preferred/Approved/Under Review), Primary Contact (text), Notes (long text). Add automations: when Three Way Match is Auto Matched and Invoice Amount is under 5000, auto-set Approval Status to Auto-Approved; when Discount Deadline is 3 days away and Approval Status is still Pending, send urgent notification to Approver; when Payment Status changes to Paid, update the Vendor Scorecard with payment timing; when any invoice from same vendor with same amount appears within 30 days, flag as potential duplicate. Create a Dashboard with: total AP outstanding (number), invoices by match status (pie chart), aging by payment due (chart: current, 1-30, 31-60, 61-90, 90+), early pay discount capture rate (gauge), processing cycle time trend (line chart), top 20 vendors by spend (table), duplicate payment alerts (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PayStream Automator
**Agent Purpose:** Automate invoice processing, maximize early payment discount capture, prevent duplicate payments, and maintain vendor performance scorecards.

**Triggers:**
- New invoice received (email, EDI, or manual entry)
- 3-way match discrepancy detected
- Early payment discount deadline approaching (5-day and 2-day warnings)
- Potential duplicate invoice detected (same vendor + amount + ±5 days)
- Monthly vendor scorecard update cycle

**Actions:**
- Auto-extract invoice data from PDF/email using OCR and match to PO and receiving records
- Route matched invoices under threshold ($5K) for auto-approval; route exceptions to appropriate approver based on cost center and amount
- Prioritize discount-eligible invoices in approval queue with deadline urgency flags
- Block potential duplicate invoices and present side-by-side comparison to AP clerk for verification
- Generate weekly AP aging report and cash requirement forecast for Treasury
- Update vendor scorecards monthly with invoice accuracy, payment timing, and dispute frequency metrics

**Data Required:**
- Invoice Processing board
- ERP purchase order and goods receipt data
- Vendor master with payment terms and contract pricing
- Bank payment files for reconciliation
- Historical invoice data for duplicate detection patterns

**Autonomy Level:** Human-in-the-Loop
Invoice extraction, PO matching, auto-approval (under threshold), duplicate detection, and reporting are autonomous. Exception approvals, vendor disputes, and payment scheduling require human authorization.

**Example Interaction:**
> A batch of 127 invoices arrives Monday morning from the weekend email queue. The PayStream agent extracts data from each invoice and begins 3-way matching. Results: 89 invoices auto-match perfectly (70%)—of these, 52 are under $5K and auto-approved. The remaining 37 matched invoices are routed to approvers by cost center. 23 invoices have price variances (commodity-adjusted pricing from dairy and grain suppliers)—the agent compares invoice prices against CME index-based contract formulas and determines 18 are within tolerance; the other 5 show overcharges totaling $12,400 and are flagged for dispute. 11 invoices have no PO (rush orders) and are routed to department heads. 4 invoices are flagged as potential duplicates.
>
> The agent also identifies 8 invoices with 2/10 net 30 discount terms where the discount deadline is within 5 days. It sends priority notifications to the 3 approvers who hold these invoices, calculating the total discount at risk: $4,200. All 8 are approved within 24 hours. Treasury is notified to schedule early payment, capturing the full discount. Over the month, the agent's discount capture rate is 94%—up from 45% before implementation—representing $38K in savings this month alone.

---

### Use Case 6: Commodity Cost Tracking & Hedge Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Commodity cost volatility is the single biggest financial risk for most F&B companies. A cereal manufacturer might use 200M pounds of wheat, 50M pounds of sugar, and 30M pounds of cocoa annually. A 10% price increase in wheat alone can impact EBITDA by $5-15M. Finance and Procurement teams must monitor commodity markets, manage hedging programs (futures, options, forward contracts), track hedge effectiveness for ASC 815 compliance, forecast ingredient cost scenarios, and communicate cost exposure to the C-suite. Most mid-market F&B companies manage this through spreadsheets and broker reports, with no centralized view of exposure, coverage, and mark-to-market positions. Even companies with commodity risk management (CRM) systems like CTRM (Commodity Trading and Risk Management) platforms find them expensive, complex, and disconnected from FP&A workflows.

#### The Solution
monday.com Work Management as a commodity exposure and hedge tracking hub. A **Commodity Dashboard Board** with: Commodity (dropdown: Wheat, Corn, Sugar, Cocoa, Palm Oil, Dairy - Class III, Soybean Oil, Natural Gas, Diesel, Packaging - Corrugated, Packaging - PET Resin), Annual Volume Requirement (numbers), Current Spot Price (numbers), Budget Price (numbers), Budget Exposure (formula: volume × budget price), Current Exposure (formula: volume × spot price), Variance (formula), Hedged Percentage (numbers), Hedged Price (numbers), Hedge Instrument (dropdown: Futures, Options, Forward Contract, None), Broker (text), Contract Expiry (date). A connected **Hedge Position Board** tracking individual contracts with mark-to-market values.

#### The Outcome
Provide real-time commodity exposure visibility (vs. quarterly spreadsheet updates). Improve hedge coverage monitoring to prevent gaps. Reduce commodity-driven EBITDA surprises by 60%. Enable scenario modeling for procurement negotiation and pricing decisions.

#### Discovery Questions
1. "What are your top 5 commodity exposures by dollar value, and what percentage of each is currently hedged?"
2. "How do you currently track your hedge positions—and can your CFO see the total exposure picture in real time?"
3. "When cocoa prices spiked 40% last year, how quickly could your Finance team model the full P&L impact and evaluate response options?"
4. "How do you ensure ASC 815 hedge accounting compliance—is effectiveness testing manual or automated?"
5. "How connected are your commodity forecasts to your demand forecast—when Sales projects a volume increase, does Procurement automatically know to increase hedge coverage?"

#### Industry Context
F&B commodity hedging varies significantly by company size and sophistication. Large CPG companies have dedicated commodity risk teams; mid-market companies often rely on the CFO and a broker. Common hedge instruments include CME futures (wheat, corn, sugar, dairy), ICE futures (cocoa, coffee), OTC forward contracts with suppliers (locking prices for 3-12 months), and options strategies (caps/collars for budget certainty with upside participation). ASC 815 requires documenting hedge effectiveness through regression analysis or dollar-offset methods. "Basis risk" (the difference between the hedged commodity index and the actual ingredient purchased) is a constant challenge—hedging CME wheat doesn't perfectly hedge the price of the specific flour grade used in production.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a commodity cost tracking and hedge management system for a food company. Create a board called 'Commodity Exposure Dashboard' with columns: Commodity (dropdown: Hard Red Winter Wheat, Corn, Sugar No 11, Cocoa, Palm Oil, Soybean Oil, Milk Class III, Natural Gas, Diesel, Corrugated Packaging, PET Resin, Aluminum Cans), Annual Volume (numbers with unit label), Unit (dropdown: bushels, pounds, metric tons, gallons, MMBtu, tons), Budget Price Per Unit (numbers, USD), Current Spot Price (numbers, USD), Price Change YTD Percent (formula), Annual Budget Cost (formula: volume times budget price), Current Annual Cost at Spot (formula: volume times spot), Unhedged Exposure (formula), Hedged Percent Q1 (numbers), Hedged Percent Q2 (numbers), Hedged Percent Q3 (numbers), Hedged Percent Q4 (numbers), Average Hedged Price (numbers), Hedge Savings or Cost (formula: hedged price minus spot times hedged volume), Primary Supplier (text), Risk Level (status: Low/Moderate/High/Critical), Last Updated (date). Create a connected board called 'Hedge Positions' with: Position ID (text), Commodity (connect to Exposure Dashboard), Instrument Type (dropdown: CME Future, ICE Future, OTC Forward, Call Option, Put Option, Collar), Broker-Counterparty (text), Contract Volume (numbers), Strike-Fixed Price (numbers), Expiration Date (date), Mark to Market Value (numbers, USD), Margin Posted (numbers), Effectiveness Test Result (numbers, percentage), Status (status: Open/Expired/Settled/Rolled), Settlement Amount (numbers). Add automations: when Hedged Percent for any quarter drops below 50 and Risk Level is High, notify CFO and VP Procurement; when a Hedge Position expiration is 30 days away, notify the commodity manager to evaluate roll or settlement; when spot price moves more than 5 percent from budget price, change Risk Level to High. Create a Dashboard with: total commodity exposure heat map (table color-coded by risk), hedged vs unhedged by commodity (stacked bar), price trend vs budget (line chart for top 5 commodities), total hedge P&L (number widget), quarterly coverage summary (table), upcoming expirations next 60 days (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CommodityShield Analyst
**Agent Purpose:** Continuously monitor commodity markets, track hedge effectiveness, and provide real-time exposure analysis and scenario modeling for Finance leadership.

**Triggers:**
- Daily commodity price feed update (market close)
- Spot price moves >3% in a single day for any tracked commodity
- Hedge position approaching expiration (30-day warning)
- Quarterly hedge effectiveness testing due
- New volume forecast received from S&OP/demand planning

**Actions:**
- Update spot prices daily and recalculate exposure, coverage gaps, and mark-to-market positions
- Generate price alert notifications when commodities breach threshold levels (±5%, ±10%, ±15% from budget)
- Produce weekly commodity exposure summary for CFO with price movements, coverage status, and P&L impact
- Model "what-if" scenarios: "If cocoa stays at current levels through Q4, EBITDA impact is -$3.2M; if it returns to budget level, impact is +$1.1M"
- Calculate ASC 815 hedge effectiveness ratios and flag positions that may fail effectiveness testing
- Recommend hedge actions when coverage drops below policy minimums (e.g., "Q3 wheat coverage is 35% vs. 70% policy minimum—recommend purchasing 1.2M bushels of September futures at current price of $6.42/bu")

**Data Required:**
- Commodity Exposure Dashboard and Hedge Positions boards
- Commodity price feeds (CME, ICE, broker feeds)
- Volume forecasts from demand planning/S&OP
- Hedge policy parameters (minimum coverage by quarter, maximum tenor)
- Historical price data for effectiveness testing and scenario modeling

**Autonomy Level:** Human-in-the-Loop
Price monitoring, exposure calculations, reporting, and effectiveness testing are fully autonomous. All hedge execution recommendations require CFO or Treasury approval.

**Example Interaction:**
> At 4:30 PM ET, commodity markets close. The CommodityShield agent updates all positions: cocoa has spiked 8% today on reports of Côte d'Ivoire crop disease, hitting $9,200/MT—the highest level in 3 months. The agent immediately triggers an alert to the CFO and VP Procurement: "ALERT: Cocoa spot +8% today ($9,200/MT vs. $7,800 budget). Current Q2-Q4 cocoa coverage: 45%. Unhedged exposure at current spot: $4.7M above budget. Recommended action: Secure additional Q3 coverage of 500 MT via OTC forward or CME July futures."
>
> The agent generates a scenario analysis: (1) If cocoa stabilizes at $9,200: full-year COGS impact +$6.1M, EBITDA impact -$6.1M (before hedges), -$3.4M (net of existing hedges). (2) If cocoa retreats to $8,500 (analyst consensus): net impact -$1.8M. (3) If cocoa continues to $10,000: net impact -$5.2M. The CFO reviews the scenarios during an emergency 15-minute call with Treasury and Procurement, approves hedging 300 MT of Q3 exposure via forward contracts, and defers 200 MT pending next week's crop report. The agent logs the decision and creates a follow-up reminder for next Friday.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| COGS | Cost of Goods Sold — direct costs of producing food products (ingredients, packaging, labor, overhead) |
| Trade Spend | Promotional funds paid to retailers (coupons, slotting fees, volume rebates, display allowances) |
| SKU | Stock Keeping Unit — unique product identifier (e.g., 12oz can of Brand X Cola, 24-pack) |
| CPG | Consumer Packaged Goods — industry category including food, beverages, personal care, household products |
| RGM | Revenue Growth Management — strategic discipline optimizing price, promotion, mix, and trade for profitable growth |
| TPM/TPO | Trade Promotion Management / Optimization — systems and processes for planning and measuring trade spend effectiveness |
| EBITDA | Earnings Before Interest, Taxes, Depreciation, and Amortization — primary profitability metric in F&B |
| ASC 815 | Accounting Standards Codification 815 — US GAAP standard governing derivative and hedge accounting |
| 3-Way Match | AP process of matching purchase order, goods receipt, and vendor invoice before payment approval |
| CME | Chicago Mercantile Exchange — primary exchange for agricultural and food commodity futures trading |
| OEE | Overall Equipment Effectiveness — manufacturing metric measuring availability × performance × quality |
| S&OP | Sales & Operations Planning — cross-functional process aligning demand forecast, production plan, and financials |
| Co-Manufacturing | Outsourced production where a third-party manufacturer produces products to the brand owner's specifications |
| FSMA | Food Safety Modernization Act — FDA regulation impacting supply chain documentation and traceability costs |
| Basis Risk | Risk that a hedge instrument doesn't perfectly offset the price movement of the actual commodity purchased |
| EPM | Enterprise Performance Management — budgeting, forecasting, and financial planning software category (Anaplan, Adaptive) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CFO | Overall financial strategy, board reporting, capital allocation, risk management | Ultimate decision-maker |
| VP FP&A | Budgeting, forecasting, management reporting, business performance analysis | Decision-maker for planning tools |
| Controller / VP Accounting | Financial close, general ledger, SOX compliance, audit management | Decision-maker for close and AP tools |
| Treasurer | Cash management, debt facilities, commodity hedging, foreign exchange | Decision-maker for treasury/hedge tools |
| Director of Trade Finance | Trade spend tracking, deduction management, promotion ROI analysis | Key champion for trade spend tools |
| Revenue Growth Management Lead | Pricing strategy, promotion optimization, mix management | Influencer, data consumer |
| AP Manager | Invoice processing, vendor payments, 3-way matching | User/Champion for AP automation |
| Financial Analyst (FP&A) | Budget modeling, variance analysis, ad-hoc reporting | Daily user |
| Plant Controller | Plant-level financial management, cost accounting, inventory valuation | User for close and CapEx tools |
| Internal Audit Director | SOX testing, process controls, fraud detection | Influencer (compliance requirements) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Procurement / Supply Chain | Commodity purchasing, vendor management, contract negotiation | Joint commodity tracking and vendor scorecard deployment; AP automation that bridges Procurement and Finance |
| Sales / Commercial | Trade spend planning, promotion execution, revenue forecasting | Connected trade promotion management linking Sales planning to Finance reconciliation |
| Operations / Manufacturing | Production costing, CapEx execution, labor planning | Plant-level financial dashboards; CapEx tracking that connects Engineering requests to Finance approval |
| IT | ERP integrations (SAP, Oracle, JDE), data infrastructure, tool consolidation | Tech stack consolidation; monday.com as the workflow layer on top of ERP |
| HR | Compensation budgeting, headcount planning, labor cost forecasting | Integrated workforce cost planning connecting HR headcount plans to Finance budgets |
| R&D / Product Development | New product costing, ingredient cost modeling, margin analysis for innovation pipeline | Stage-gate innovation tracking with embedded financial analysis |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Anaplan / Adaptive Insights (Workday) | Enterprise planning and forecasting (EPM) | monday.com won't replace core EPM modeling but can own the budget coordination workflow, rolling forecast tracking, and cross-functional planning collaboration that EPM tools handle poorly |
| SAP / Oracle ERP (Finance modules) | Core financial system of record (GL, AP, AR, FA) | Complement, not compete—monday.com sits on top as the workflow and exception management layer; automates what falls between ERP transactions |
| Exceedra / AFS / Blacksmith TPM | Trade promotion management | Strong displacement candidate for mid-market—monday.com provides 70% of TPM capability at 20% of the cost and implementation time |
| Coupa / SAP Ariba | Procurement and AP automation | Compete on usability for mid-market AP workflows; large enterprises may keep Coupa for P2P but use monday.com for exception management and vendor scorecards |
| Excel / Google Sheets | Default "tool" for budgeting, forecasting, trade tracking, CapEx management | Primary displacement target—most F&B Finance processes still run on spreadsheets despite ERP investments |
| BlackLine | Financial close management | Direct competitor for close management use case; monday.com wins on flexibility, price (BlackLine is $200K+), and time-to-value |
| Kyriba / GTreasury | Treasury management and commodity risk | Complement for large enterprises; potential displacement for mid-market treasury workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We have SAP/Oracle for all our Finance processes" | "SAP and Oracle are incredible systems of record—they process transactions. But the workflows *around* those transactions—chasing budget approvals, managing the close checklist, resolving trade deductions, tracking CapEx spend—that's where teams lose hundreds of hours to email and Excel. monday.com is the orchestration layer that makes your ERP investment work harder." |
| "We're implementing Anaplan for planning" | "Great choice for complex financial modeling. Anaplan excels at the *math*—driver-based models, scenario analysis, allocations. monday.com excels at the *process*—coordinating 50 budget owners, tracking who's submitted, managing revision cycles, and connecting the approved plan to execution tracking. Many companies use both." |
| "Finance data is too sensitive for a work management tool" | "Absolutely—data security is non-negotiable. monday.com offers enterprise-grade security (SOC 2 Type II, ISO 27001, GDPR), role-based permissions, audit trails, and data residency options. You control exactly who sees what. And the data we're managing—workflow status, approvals, task tracking—is operational data, not raw financial data. The GL stays in your ERP." |
| "We already spent $500K on a TPM system that nobody uses" | "That's actually the perfect argument for our approach. Complex, purpose-built systems fail when adoption fails. monday.com's strength is that people *actually use it*—intuitive interface, no 6-month implementation, works the way your team already thinks. Start with deduction tracking in weeks, prove ROI, then expand. Don't repeat the shelfware mistake." |
| "Our close process is fine—we close in 10 days" | "Ten days is common, but it means your leadership team is making decisions for 10 business days each month without current financials. What if you could close in 5-6 days? That's 4-5 extra days of data-driven decision-making per month, 50+ days per year. And beyond speed, close management gives you auditability—every task, every approver, every timestamp documented for SOX." |

## Proof Points
*(To be populated with customer references)*
- [Food & Beverage company using monday.com for financial planning or close management]
- [CPG company that consolidated trade spend tracking onto a work management platform]
- [Manufacturing company with documented AP automation ROI]
- [Mid-market company that replaced Excel-based budgeting with monday.com]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
