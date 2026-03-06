# Banking × Finance Playbook

## Overview

Finance departments within banking institutions occupy a uniquely complex position — they are the financial stewards of organizations whose entire business *is* finance. Unlike Finance teams in other industries that support a core business, bank Finance departments must navigate dual mandates: managing the institution's own profitability, capital adequacy, and liquidity while simultaneously complying with some of the most rigorous regulatory reporting frameworks in existence (Basel III/IV, CCAR, DFAST, IFRS 9, CECL).

A mid-to-large bank's Finance function typically encompasses Financial Planning & Analysis (FP&A), Treasury/ALM, Regulatory Reporting, Tax, Accounts Payable/Receivable, and Financial Control. These teams range from 50–500+ people depending on asset size, with significant portions dedicated purely to regulatory compliance. The CFO organization in a top-50 bank may manage $5–15M in annual technology spend just for finance-specific tools.

The modern bank Finance department is under intense pressure to accelerate close cycles, automate regulatory filings, and provide real-time business intelligence to the C-suite — all while managing legacy systems (many still running on mainframe-era general ledgers), reconciling across dozens of subsidiaries and legal entities, and preparing for ever-evolving regulatory requirements like climate risk disclosures and digital asset accounting.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Bank Finance teams are bloated with manual reconciliation, regulatory prep, and journal entry processing staff — AI can automate 40-60% of these tasks |
| 2 | Consolidate Tech Stack with AI | High | Banks typically run 8-15 finance tools (Hyperion, Anaplan, BlackLine, Workiva, SAP, custom GL systems) creating fragmented workflows and data silos |
| 3 | Scale Impact Without Overhead | Medium-High | Regulatory demands keep growing (new Basel IV rules, ESG disclosures, crypto accounting) but Finance headcount budgets are flat or shrinking |

## Prioritized Use Cases

---

### Use Case 1: Regulatory Reporting Workflow Orchestration

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banks submit 50-200+ regulatory reports per quarter across jurisdictions (Fed, OCC, FDIC, ECB, PRA, local regulators). Each report — Call Reports (FFIEC 031/041), FR Y-9C, CCAR submissions — requires data from 10-20 source systems, multiple review cycles, sign-offs from Controllers, and tight deadlines with severe penalties for late or inaccurate filing. Most banks manage this through a chaotic mix of spreadsheets, emails, and SharePoint trackers. A single missed data feed can cascade into a late filing and potential regulatory action.

#### The Solution
monday.com Work Management as the orchestration layer for the entire regulatory reporting lifecycle. Each report becomes a structured workflow with dependencies: data extraction → validation → reconciliation → draft preparation → review cycles → sign-off → submission → evidence archival. Use mondayDB for storing report metadata, deadlines, and submission history. Dashboards provide real-time visibility into report status across all jurisdictions. Automations trigger alerts when data feeds are late, reviews are overdue, or deadlines are approaching.

#### The Outcome
- 30-40% reduction in time spent on regulatory reporting coordination
- Zero missed filing deadlines through automated escalation
- Complete audit trail for examiner inquiries
- Real-time CFO dashboard showing regulatory compliance posture across all entities

#### Discovery Questions
1. "How many distinct regulatory reports do you file per quarter, and across how many jurisdictions?"
2. "Walk me through what happens when a data feed from your GL or risk system is late for a Call Report — how do you track the downstream impact?"
3. "During your last regulatory exam, how quickly could you produce evidence of your reporting controls and review processes?"
4. "What's your current ratio of FTEs dedicated to regulatory reporting versus strategic finance work?"
5. "Have you ever had a restatement or late filing, and what was the root cause?"

#### Industry Context
Call Reports (FFIEC 031/041/051) are quarterly filings required by FDIC-insured institutions. FR Y-9C is the Federal Reserve's consolidated financial statement for bank holding companies. CCAR (Comprehensive Capital Analysis and Review) is the annual stress test for banks with >$100B in assets. Each has rigid schedules, prescribed formats, and penalties for errors. The OCC can issue Matters Requiring Attention (MRAs) for reporting deficiencies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Report Tracker board. Columns: Report Name (text), Regulator (dropdown: Fed, OCC, FDIC, ECB, PRA, State), Filing Frequency (dropdown: Daily, Weekly, Monthly, Quarterly, Annual), Legal Entity (dropdown), Due Date (date), Data Extraction Status (status: Not Started, In Progress, Complete, Issue), Data Validation Status (status: Not Started, In Progress, Pass, Fail), Draft Status (status: Not Started, Drafting, Under Review, Final), Sign-Off (people), Submission Status (status: Pending, Submitted, Acknowledged), Filing Evidence (file), Days Until Due (formula). Create groups by quarter: Q1 2026, Q2 2026, Q3 2026, Q4 2026. Add automations: when Data Extraction Status is 'Issue', notify Sign-Off person; when Days Until Due < 5 and Submission Status is 'Pending', send urgent notification to group; when Submission Status changes to 'Submitted', move to 'Completed' group. Add a Dashboard with: filing status breakdown (pie chart), upcoming deadlines (calendar view), overdue items (table widget filtered by past due), completion rate by regulator (bar chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RegWatch Filing Sentinel
**Agent Purpose:** Monitor regulatory reporting workflows and proactively identify risks to on-time, accurate filing.

**Triggers:**
- Daily at 7:00 AM — scan all reports due within 14 days
- When Data Extraction Status changes to "Issue"
- When any report's due date is within 3 business days and status is not "Final"
- When a new regulatory circular or amendment is published (via integration)
- Manual trigger by Controller for ad-hoc status check

**Actions:**
- Generate daily filing risk report summarizing all at-risk submissions
- Automatically escalate to VP of Financial Control when data feeds are >24 hours late
- Create remediation tasks when validation checks fail, pre-populated with error details
- Cross-reference filing calendar against holiday schedules to flag compressed timelines
- Generate examiner-ready audit trail document on demand
- Notify legal entity controllers of their specific upcoming obligations

**Data Required:**
- Regulatory filing calendar (all jurisdictions)
- GL/sub-ledger data feed status from ETL systems
- Historical filing data (past submissions, restatements)
- Staff calendar/availability
- Regulatory update feeds (OCC bulletins, Fed guidance)

**Autonomy Level:** Human-in-the-Loop
All filing decisions and sign-offs remain with authorized personnel. Agent handles monitoring, alerting, task creation, and report generation autonomously. Escalation to humans for any data discrepancy or deadline risk.

**Example Interaction:**
> At 7:15 AM on March 12, RegWatch identifies that the FR Y-9C data extraction from the commercial lending sub-ledger has not completed — it's now 18 hours past the expected arrival time. The agent immediately creates a high-priority task assigned to the Data Operations team, cross-references the issue against the filing timeline (due March 31), and calculates that any delay beyond 48 hours will compress the review cycle below the minimum 5-day threshold required by internal policy.
>
> The agent notifies Sarah Chen (VP, Financial Control) via monday.com and flags the item on the CFO dashboard. It also checks whether last quarter's Y-9C had similar data feed issues (it did — caused by a batch job timeout) and includes this context in the notification. When the data finally arrives 6 hours later, the agent automatically updates the status, recalculates the timeline, and confirms the review cycle is back within policy thresholds.

---

### Use Case 2: Month-End & Quarter-End Close Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The financial close process at a bank is extraordinarily complex. A typical month-end close involves 200-500+ discrete tasks across sub-ledger reconciliation, intercompany eliminations, journal entry processing, accruals, fair value adjustments, and management reporting — often across 10-50 legal entities. Most banks target a 5-7 business day close but frequently run 10-15 days due to bottlenecks, unresolved reconciliation breaks, and manual handoffs. Each day of delayed close costs the FP&A team visibility into actual performance and delays board reporting.

#### The Solution
monday.com Work Management to orchestrate the entire close checklist with task-level dependencies, ownership, and deadlines. Each close period is templated with predecessor/successor relationships (can't post consolidating entries until all entity-level closes are complete). Status automations flag bottlenecks in real-time. Integration with BlackLine or manual reconciliation trackers feeds completion data. The CFO and Controller get a single dashboard showing close progress across all entities with drill-down capability.

#### The Outcome
- Reduce close cycle from 10-15 days to 5-7 days
- 50% reduction in close-related emails and status meetings
- Real-time visibility into close bottlenecks across all legal entities
- Standardized close procedures that survive staff turnover

#### Discovery Questions
1. "How many business days does your month-end close currently take, and what's your target?"
2. "Where do the bottlenecks typically occur — is it reconciliation breaks, late journal entries, or approval delays?"
3. "How do you currently track close task completion across your legal entities?"
4. "What happens when a key person is out during close — how much institutional knowledge is at risk?"
5. "How much time does your Controller spend in status meetings during close versus actually resolving issues?"

#### Industry Context
Bank closes are more complex than typical corporate closes due to: fair value accounting for trading books (ASC 820), loan loss provisioning (CECL/IFRS 9), derivative valuations, intercompany funding transfers, and multi-currency consolidation. The "sub-ledger to GL" reconciliation alone can involve 50+ reconciliation points. Many banks use BlackLine for reconciliation but still track the overall close process manually.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Month-End Close Tracker board. Columns: Task Name (text), Category (dropdown: Sub-Ledger Recon, Journal Entries, Intercompany, Consolidation, Reporting, Accruals, Fair Value, Tax), Legal Entity (dropdown), Owner (people), Predecessor Task (connect boards), Due Date (date), Completion Date (date), Status (status: Not Started, In Progress, Blocked, Under Review, Complete), Blocker Description (text), Priority (dropdown: Critical Path, Standard, Optional), Days Variance (formula: Completion Date minus Due Date). Create groups: Pre-Close, Day 1-2, Day 3-4, Day 5-6, Day 7+, Post-Close. Add automations: when Status is 'Blocked', notify the board owner and create a subitems for blocker resolution; when all items in a group are 'Complete', notify Controller; when Completion Date is empty and Due Date is today, change Priority to 'Critical Path'. Add Dashboard with: close progress by entity (stacked bar), critical path items (filtered table), daily completion trend (line chart), blocked items (table widget), overall close percentage (number widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CloseBot Orchestrator
**Agent Purpose:** Actively manage the financial close by tracking dependencies, identifying bottlenecks, and coordinating across teams to hit close targets.

**Triggers:**
- Close period begins (triggered by calendar or manual start)
- Every 2 hours during active close — progress sweep
- When any task Status changes to "Blocked"
- When a task's Due Date passes without completion
- When all predecessor tasks for a task are marked "Complete"

**Actions:**
- Automatically notify task owners when their predecessors are complete ("You're unblocked — Sub-Ledger Recon for Entity 4 is done, you can begin consolidation entries")
- Generate twice-daily close status summary for Controller and CFO
- Identify and highlight the current critical path — which incomplete tasks are blocking the most downstream work
- When a task is blocked, automatically assign resolution to the blocker owner and set a 4-hour SLA
- Compare current close pace against historical averages and flag if trending late
- Post final close completion notification with cycle-time metrics

**Data Required:**
- Close task checklist with dependencies
- Historical close data (prior 12 months)
- Staff assignments and availability
- Sub-ledger reconciliation completion feeds
- Journal entry posting confirmations from GL

**Autonomy Level:** Escalation-Based
Agent manages notifications, status tracking, and reporting autonomously. Escalates to Controller for any blocked items unresolved after 4 hours and to CFO if close is trending >1 day behind target.

**Example Interaction:**
> On Day 3 of the March close, CloseBot detects that the derivatives fair value adjustment for the London entity hasn't started, despite its predecessor (counterparty confirmation reconciliation) being completed 6 hours ago. The agent notifies James Park (Treasury Accounting Manager) that he's unblocked and his task is now on the critical path — 4 downstream consolidation tasks depend on it. Simultaneously, CloseBot updates the CFO dashboard to show the London entity is trending 0.5 days behind. When James completes the adjustment 3 hours later, CloseBot automatically triggers the consolidation team and recalculates: the close is back on track for Day 6 completion, matching last quarter's pace.

---

### Use Case 3: Budget & Forecast Cycle Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Annual budgeting and quarterly re-forecasting in banking is a massive cross-functional exercise. The FP&A team must collect inputs from every business line (Retail Banking, Commercial Banking, Wealth Management, Capital Markets), consolidate across legal entities, model NII (Net Interest Income) scenarios based on rate assumptions, incorporate credit loss projections, and align with strategic plan targets — all within compressed timelines. Business line heads submit budget templates late, challenge allocations, and request multiple revision cycles. The process typically takes 3-4 months for the annual plan and involves hundreds of email threads, version-conflicted spreadsheets, and contentious review meetings.

#### The Solution
monday.com Work Management to orchestrate the budget cycle end-to-end: template distribution → business line input collection → FP&A consolidation → management review → revision cycles → board approval. Each business line has a structured intake form for their budget submissions. Automations track which units have submitted, flag overdue inputs, and manage revision request workflows. Dashboards show real-time budget cycle progress and key metrics (total expense budget, variance to prior year, headcount plan).

#### The Outcome
- Reduce annual budget cycle from 3-4 months to 6-8 weeks
- Eliminate version control chaos across 20+ business line submissions
- Real-time CFO visibility into budget cycle progress
- Structured revision process with full audit trail

#### Discovery Questions
1. "How long does your annual budget cycle take from kickoff to board approval?"
2. "How many distinct business units submit budget inputs, and what's your on-time submission rate?"
3. "How do you currently manage budget revision requests — is there a structured process or is it ad-hoc?"
4. "What's the biggest source of friction between FP&A and the business lines during planning?"
5. "How many versions of the budget deck exist by the time it reaches the board?"

#### Industry Context
Bank budgeting is uniquely complex because revenue is driven by macro factors (interest rates, credit spreads, fee income) that require scenario modeling. NII (Net Interest Income) — the spread between interest earned on assets and paid on liabilities — is the largest revenue component and is highly sensitive to rate curves. Banks must also budget for credit provisions (expected losses under CECL), which adds a probabilistic modeling layer. The CFO must align the operating plan with regulatory capital requirements (CET1 ratios) and stress test results.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Budget Cycle Tracker board. Columns: Business Unit (dropdown: Retail Banking, Commercial Banking, Wealth Management, Capital Markets, Treasury, Operations, Technology, Corporate Functions), Budget Owner (people), Submission Deadline (date), Submission Status (status: Not Started, Draft Submitted, Under Review, Revision Requested, Approved), Total Expense Budget (numbers with $), Headcount Plan (numbers), Variance to Prior Year % (numbers), Revenue Forecast (numbers with $), FP&A Reviewer (people), Revision Notes (long text), Approval Status (status: Pending, CFO Review, Board Ready, Approved). Create groups: Annual Budget 2027, Q2 Reforecast, Q3 Reforecast. Add automations: when Submission Deadline is today and Submission Status is 'Not Started', send notification to Budget Owner; when Submission Status changes to 'Draft Submitted', assign FP&A Reviewer; when Approval Status changes to 'CFO Review', notify CFO. Add Dashboard: submission progress (pie chart), total expense by business unit (bar chart), headcount plan summary (number widgets), variance analysis (table widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PlanPulse Budget Coordinator
**Agent Purpose:** Orchestrate budget and forecast cycles by tracking submissions, managing revision workflows, and providing FP&A with real-time cycle intelligence.

**Triggers:**
- Budget cycle kickoff (manual trigger or calendar-based)
- Daily at 9 AM during active budget cycle — submission status check
- When any business unit submits budget input (status change)
- When FP&A requests a revision
- 48 hours before any submission deadline

**Actions:**
- Send personalized reminder to business unit heads with outstanding submissions, including their specific template and prior year actuals for reference
- Auto-generate consolidation summary when all inputs are received
- Track revision cycles — which units have been asked to revise, how many rounds, reasons
- Generate weekly budget cycle status report for CFO
- Flag material variances (>10% vs. prior year) for FP&A review
- Create comparison view: submitted budget vs. strategic plan targets vs. prior year

**Data Required:**
- Budget calendar and deadlines
- Prior year actuals by business unit
- Strategic plan targets
- Submission templates
- Historical cycle-time data

**Autonomy Level:** Human-in-the-Loop
Agent manages tracking, reminders, and report generation autonomously. All budget decisions, approvals, and revision requests are made by FP&A team and CFO.

**Example Interaction:**
> Three weeks into the annual budget cycle, PlanPulse identifies that Commercial Banking and Capital Markets haven't submitted their draft budgets — both are 5 days past deadline. The agent sends a tailored reminder to each division head, attaching their pre-populated template with prior year actuals and noting that 6 of 8 divisions have already submitted. It also alerts the FP&A lead that the consolidation milestone is at risk if inputs aren't received within 48 hours. When Commercial Banking submits the next morning, PlanPulse flags that their expense budget is 18% above prior year — primarily driven by a new digital lending initiative — and routes it to the FP&A analyst with the variance highlighted for review.

---

### Use Case 4: Accounts Payable & Vendor Invoice Processing

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banks process thousands of vendor invoices monthly — from technology vendors (core banking systems, Bloomberg terminals, market data feeds), professional services (audit, legal, consulting), facilities, and operational suppliers. The AP process involves invoice receipt → coding to correct GL account and cost center → three-way matching (PO, receipt, invoice) → multi-level approval → payment scheduling. Many banks still have significant manual touchpoints: AP clerks manually key invoice data, chase approvals via email, and reconcile vendor statements in spreadsheets. Invoice exceptions (mismatched amounts, missing POs, incorrect coding) create bottlenecks that delay payments, strain vendor relationships, and risk late payment penalties.

#### The Solution
monday.com Work Management with Forms for invoice intake (or integration with invoice scanning tools). Each invoice becomes a tracked item with structured approval workflows based on amount thresholds and cost center routing. Automations handle approval routing (< $10K → Manager, $10K-$100K → Director, >$100K → VP + Controller), escalation for overdue approvals, and payment scheduling notifications. Dashboard provides AP team real-time visibility into invoice pipeline, aging, and exception rates.

#### The Outcome
- 50-60% reduction in invoice processing time
- Near-zero late payment penalties through automated escalation
- Real-time visibility into AP aging and cash flow impact
- Reduced AP headcount by 2-3 FTEs through automation

#### Discovery Questions
1. "How many vendor invoices do you process monthly, and what's your current average processing time?"
2. "What percentage of invoices hit exceptions — mismatches, missing POs, coding errors?"
3. "How do you currently route invoices for approval, and what's the average approval cycle time?"
4. "Have you quantified the cost of late payment penalties or missed early payment discounts?"
5. "How many FTEs are dedicated to AP processing versus AP analysis and vendor management?"

#### Industry Context
Banks are major consumers of technology and professional services — a mid-size bank may have 500-1,000 active vendors. Key vendor categories include core banking system providers (FIS, Fiserv, Jack Henry), market data (Bloomberg, Refinitiv), audit firms (Big 4), and legal counsel. Many bank contracts include complex fee structures (tiered pricing, volume-based fees, pass-through costs) that make three-way matching particularly challenging. SOX controls require documented approval trails for all expenditures.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Invoice Tracker board. Columns: Vendor Name (text), Invoice Number (text), Invoice Date (date), Amount (numbers with $), GL Account (dropdown: Technology, Professional Services, Facilities, Market Data, Operations, Other), Cost Center (dropdown), PO Number (text), Three-Way Match (status: Matched, Partial Match, Exception), Approver (people), Approval Status (status: Pending, Approved, Rejected, Escalated), Payment Date (date), Payment Status (status: Scheduled, Paid, On Hold), Exception Reason (dropdown: Amount Mismatch, Missing PO, Incorrect Coding, Duplicate, Other), Days in Queue (formula). Create groups: Pending Approval, Approved - Awaiting Payment, Paid, Exceptions. Add automations: when Amount < 10000 assign to Manager group for approval; when Amount > 100000 assign to VP and Controller; when Days in Queue > 5 and Approval Status is 'Pending', change to 'Escalated' and notify finance director; when Three-Way Match is 'Exception', move to Exceptions group. Add Dashboard: invoice volume by month (bar chart), aging analysis (pie chart), exception rate (number widget), total pending AP (number widget), top 10 vendors by spend (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** InvoiceIQ Processor
**Agent Purpose:** Automate invoice intake, validation, and routing while proactively resolving exceptions and optimizing payment timing.

**Triggers:**
- New invoice received (form submission or email integration)
- When Three-Way Match status is "Exception"
- Daily at 6 AM — scan for approval bottlenecks
- When payment terms are approaching (early discount windows)
- Weekly — vendor statement reconciliation check

**Actions:**
- Auto-extract invoice data (vendor, amount, date, line items) and populate board fields
- Perform three-way match against PO database and receiving records
- Route to correct approver based on amount threshold and cost center rules
- For exceptions: identify likely cause, suggest resolution, and assign to AP specialist
- Flag early payment discount opportunities (e.g., "2/10 net 30 — save $4,200 if paid by Friday")
- Generate weekly AP aging report and cash flow impact analysis

**Data Required:**
- Vendor master database
- Purchase order system
- Receiving/goods receipt records
- GL account mapping rules
- Payment terms by vendor
- Approval authority matrix

**Autonomy Level:** Escalation-Based
Agent handles data extraction, matching, and routing autonomously. Exceptions with clear resolution paths (e.g., rounding differences <$5) are auto-resolved. Material exceptions and all payment decisions require human approval.

**Example Interaction:**
> InvoiceIQ receives a $287,000 invoice from Accenture for core banking migration consulting. It auto-extracts the details, matches against PO #CB-2026-0445, and identifies a $12,000 discrepancy — the invoice includes travel expenses not covered in the PO. The agent creates an exception item, attaches the original PO and invoice, and routes it to the AP Specialist with a note: "Travel expenses ($12K) appear to be pass-through costs per contract amendment #3 — verify against amended SOW." Simultaneously, it routes the remaining $275,000 to the VP of Technology Finance and Controller for approval per the >$100K threshold. The agent also flags that paying within 7 days qualifies for a 1.5% early payment discount, saving $4,305.

---

### Use Case 5: Capital Expenditure & Project Cost Tracking

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banks invest heavily in capital projects — core system modernizations, branch renovations, data center migrations, regulatory technology implementations. These multi-million-dollar projects span 1-3 years, involve complex capitalization rules (ASC 350-40 for internal-use software), and require precise tracking of labor hours, vendor costs, and overhead allocations for proper GAAP treatment. Finance teams struggle to get timely, accurate project cost data from PMO and Technology teams, leading to capitalization errors, surprise budget overruns, and audit findings. Most banks track CapEx in spreadsheets disconnected from the project management systems, creating reconciliation nightmares.

#### The Solution
monday.com Work Management integrated with the PMO's project boards. Each capital project has a financial tracking view with budget vs. actual spend, labor hour capitalization tracking, vendor milestone payments, and monthly accrual calculations. Finance can view project costs in real-time without chasing project managers for updates. Automations flag when projects exceed budget thresholds (90%, 100%, 110%) and when capitalization criteria need reassessment.

#### The Outcome
- Single source of truth for project financial data across Finance and PMO
- Eliminate monthly CapEx reconciliation meetings (2-3 hours/month saved per project)
- Proactive budget overrun detection instead of quarter-end surprises
- Clean capitalization records for external audit

#### Discovery Questions
1. "How many active capital projects do you currently have, and what's the total CapEx budget?"
2. "How do you currently track project costs — is it integrated with your project management tool or separate?"
3. "When was the last time you had an audit finding related to software capitalization or CapEx classification?"
4. "How do you handle the ASC 350-40 stage assessment — who determines when a project moves from preliminary to application development?"
5. "What's your current process for monthly CapEx accruals — how accurate are they versus actuals?"

#### Industry Context
Banks are among the largest CapEx spenders in financial services, particularly on technology modernization. A top-50 US bank may spend $500M-$2B annually on technology alone, with 30-50% capitalized. ASC 350-40 (Internal-Use Software) governs capitalization of development costs: only application development stage costs qualify, while preliminary project stage and post-implementation costs must be expensed. Cloud computing arrangements (ASC 350-40-15-4A) add further complexity. Getting this wrong leads to earnings restatements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Capital Project Financial Tracker board. Columns: Project Name (text), Project ID (text), Project Stage (dropdown: Preliminary, Application Development, Post-Implementation), Sponsor (people), Total Budget (numbers with $), Spend to Date (numbers with $), Budget Consumed % (formula), Monthly Spend (numbers with $), Capex vs Opex Classification (dropdown: CapEx - Hardware, CapEx - Software Dev, CapEx - Vendor, OpEx - Cloud, OpEx - Maintenance, Mixed), Capitalized Amount (numbers with $), Expensed Amount (numbers with $), Vendor (text), Next Milestone Payment (date), Accrual Amount (numbers with $), Finance Owner (people), Audit Status (status: Not Reviewed, In Review, Cleared, Finding). Create groups by portfolio: Core Banking, Digital Channels, Risk & Compliance, Infrastructure, Branch Network. Add automations: when Budget Consumed % > 90, notify Sponsor and Finance Owner; when Project Stage changes, notify Finance Owner to reassess capitalization; when Audit Status is 'Finding', create linked task for remediation. Add Dashboard: total CapEx by portfolio (bar chart), budget vs actual (stacked bar), capitalization split (pie chart), projects at risk (filtered table where Budget Consumed > 90%), monthly burn rate trend (line chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CapTrack Financial Analyst
**Agent Purpose:** Monitor capital project financials, ensure proper capitalization treatment, and provide proactive budget intelligence to Finance leadership.

**Triggers:**
- Monthly close — aggregate all project costs for the period
- When project stage changes (impacts capitalization eligibility)
- When any project exceeds 85% of budget
- When new vendor invoices are coded to CapEx projects
- Quarterly — pre-audit capitalization review

**Actions:**
- Calculate monthly capitalization vs. expense split based on project stage and cost type
- Generate monthly CapEx accrual entries for Controller review
- Flag projects where capitalization treatment may need reassessment (e.g., project delays, scope changes)
- Create budget variance analysis with root cause commentary
- Produce quarterly CapEx report for board Finance committee
- Alert when a project's cloud computing costs may trigger ASC 350-40-15-4A reclassification

**Data Required:**
- Project management data (milestones, stages, team assignments)
- Vendor invoices and milestone payment schedules
- Labor hour tracking (capitalized vs. expensed)
- GL postings for project cost centers
- Prior period capitalization schedules

**Autonomy Level:** Human-in-the-Loop
Agent generates calculations and recommendations; all capitalization decisions and journal entries require Controller or VP of Financial Control sign-off.

**Example Interaction:**
> During the October close, CapTrack identifies that the "Core Banking Migration — Phase 2" project has shifted from Application Development to a partial Post-Implementation stage for two modules that went live on October 15. The agent recalculates the capitalization split: $1.2M in October labor hours should be split — $840K capitalized (for modules still in development) and $360K expensed (for live modules now in maintenance). It generates the draft journal entries, attaches supporting documentation (go-live confirmation, updated project plan), and routes to the Controller for review. It also flags that total project spend is at 92% of budget with 3 months remaining, recommending a budget revision request.

---

### Use Case 6: Intercompany Transaction Reconciliation

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Large banks operate through dozens of legal entities — domestic subsidiaries, international branches, broker-dealer affiliates, insurance entities, and special purpose vehicles. Every internal transaction (funding transfers, service charges, shared cost allocations, derivative hedges) must be recorded identically in both entities. In practice, timing differences, FX translation, and booking errors create thousands of intercompany reconciliation breaks each month. Resolving these breaks is one of the most labor-intensive activities during close — a team of 5-15 people may spend the entire close period chasing discrepancies across entities, often across time zones.

#### The Solution
monday.com Work Management as the intercompany break tracking and resolution platform. Each reconciliation break becomes a tracked item with counterparty entity, amount, suspected cause (timing, FX, booking error), and resolution owner. Automations assign breaks to the appropriate entity controller, set SLAs for resolution, and escalate unresolved items. Dashboard shows break volume and dollar amount by entity pair, aging, and trend over time. Integration with the GL or reconciliation tool feeds breaks automatically.

#### The Outcome
- 40-50% faster intercompany break resolution
- Real-time visibility into break volume and aging across all entity pairs
- Reduced close-period overtime for reconciliation teams
- Clear accountability with SLA tracking and escalation

#### Discovery Questions
1. "How many legal entities do you consolidate, and how many intercompany transaction pairs do you reconcile monthly?"
2. "What's your current average time to resolve an intercompany break?"
3. "What are the most common root causes — timing differences, FX, booking errors, or something else?"
4. "How many FTEs are dedicated to intercompany reconciliation during close?"
5. "Do you have standing intercompany balances that never seem to get resolved?"

#### Industry Context
Regulation W limits transactions between a bank and its affiliates. Section 23A of the Federal Reserve Act restricts covered transactions to 10% of capital for any single affiliate and 20% for all affiliates combined. Intercompany pricing must be at arm's length per transfer pricing regulations. Large banks may have 50-100+ legal entities requiring quarterly intercompany elimination entries for consolidated financial statements. The complexity increases dramatically for international banks dealing with multiple currencies and regulatory regimes.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Intercompany Reconciliation Tracker board. Columns: Break ID (autonumber), Entity A (dropdown), Entity B (dropdown), Transaction Type (dropdown: Funding Transfer, Service Charge, Cost Allocation, Derivative Hedge, Revenue Share, Other), Amount Discrepancy (numbers with $), Currency (dropdown: USD, EUR, GBP, JPY, CHF), Root Cause (dropdown: Timing, FX Translation, Booking Error, Missing Entry, Classification, Unknown), Entity A Contact (people), Entity B Contact (people), Resolution Owner (people), Status (status: New, Investigating, Pending Counterparty, Resolved, Write-Off Approved), Resolution Date (date), SLA Days (formula), Aging Bucket (formula-based: Current, 1-30 days, 31-60, 61-90, 90+), Resolution Notes (long text). Create groups: Current Month Breaks, Prior Month Carryover, Long-Standing (>90 days). Add automations: when Status is 'New', assign Resolution Owner based on higher-amount entity; when SLA Days > 5 and Status is not 'Resolved', escalate to entity Controllers; when Root Cause is 'Booking Error', create linked correcting entry task. Dashboard: break volume trend (line chart), breaks by entity pair (heat map table), dollar amount by root cause (bar chart), aging distribution (pie chart), resolution rate (number widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ICRecon Matcher
**Agent Purpose:** Automate intercompany break detection, root cause analysis, and resolution tracking to accelerate the reconciliation process.

**Triggers:**
- Daily during close period — ingest new reconciliation breaks from GL feed
- When a break remains unresolved past SLA
- When counterparty entity responds with resolution input
- Monthly — generate standing balance report
- Quarterly — pre-consolidation intercompany review

**Actions:**
- Auto-categorize break root cause based on patterns (timing breaks cluster around month-end, FX breaks correlate with rate movements)
- Match offsetting breaks across entity pairs that may net to zero
- Generate resolution instructions for common break types (e.g., "Timing break: Entity B needs to post JE for $145K funding transfer dated 3/29")
- Escalate long-standing breaks (>60 days) to VP of Financial Control with impact analysis
- Produce monthly intercompany break report with trend analysis and root cause concentration
- Flag potential Regulation W concerns when affiliate transaction volumes approach limits

**Data Required:**
- GL trial balances by legal entity
- Intercompany transaction logs
- FX rate tables
- Historical break patterns
- Regulation W limits and current utilization

**Autonomy Level:** Escalation-Based
Agent auto-categorizes, matches, and generates resolution instructions. All actual journal entries and write-off approvals require human authorization. Escalates regulatory-threshold issues immediately.

**Example Interaction:**
> During the February close, ICRecon ingests 347 intercompany breaks totaling $23.4M across 18 entity pairs. The agent immediately identifies that 89 breaks ($8.2M) are timing differences from month-end funding transfers that will self-resolve when Entity B posts their entries (expected Day 2 of close). It auto-resolves 34 FX breaks ($1.1M) that are within the $500 materiality threshold after translation adjustment. For the remaining 224 breaks, it assigns resolution owners based on the entity-pair responsibility matrix and sets SLAs. It flags 12 long-standing breaks from December ($3.7M between the broker-dealer subsidiary and the bank) for Controller attention, noting they've been carried for 3 months and may impact the Q1 regulatory filing.

---

### Use Case 7: Financial Policy & SOX Controls Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banks maintain hundreds of financial policies and SOX control procedures — from journal entry authorization matrices to bank reconciliation policies to financial reporting control narratives. These documents must be reviewed annually, tested quarterly, and updated whenever processes change. Internal Audit and external auditors (Big 4) request evidence of control operation throughout the year. Most Finance teams manage this through shared drives full of outdated Word documents, email-based review workflows, and spreadsheet control matrices. Finding the current version of a policy or the latest test results for a specific control during an audit is a time-consuming treasure hunt.

#### The Solution
monday.com Work Management as the centralized policy and controls repository. Each policy and SOX control is a board item with structured metadata: owner, review frequency, last review date, next review date, test results, and linked evidence. Automations trigger review cycles, assign testers, and escalate overdue items. Auditors get read-only dashboard access showing control status across all processes. The complete history of reviews, tests, and updates is captured in the activity log.

#### The Outcome
- Auditor-ready control documentation available on demand
- 30% reduction in audit preparation time
- Zero overdue policy reviews through automated scheduling
- Single source of truth replacing scattered SharePoint/shared drive documents

#### Discovery Questions
1. "How many SOX controls does your Finance organization own, and how do you currently track testing?"
2. "How much time does your team spend preparing for quarterly SOX testing and annual audit walkthroughs?"
3. "When an auditor asks for the current version of a policy and its last review date, how quickly can you produce it?"
4. "Have you had any SOX findings related to control documentation or evidence gaps?"
5. "How do you ensure policy updates are communicated to and acknowledged by all affected staff?"

#### Industry Context
SOX Section 404 requires management assessment of internal controls over financial reporting (ICFR). Banks also face OCC/Fed supervisory expectations for Operational Risk Management (OCC 2011-12). Key Finance controls include: segregation of duties in AP/journal entry processing, bank reconciliation controls, financial reporting review procedures, and model validation governance. Material weaknesses or significant deficiencies in ICFR can impact stock price, regulatory standing, and management credibility.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a SOX Controls & Policy Tracker board. Columns: Control ID (text), Control Description (long text), Process Area (dropdown: Journal Entries, Reconciliations, Financial Reporting, AP/Disbursements, Revenue Recognition, Consolidation, Tax, Payroll), Control Type (dropdown: Preventive, Detective, Manual, Automated, IT General), Owner (people), Testing Frequency (dropdown: Monthly, Quarterly, Semi-Annual, Annual), Last Test Date (date), Next Test Date (date), Test Result (status: Pass, Pass with Exception, Fail, Not Tested), Tester (people), Evidence Link (link), Policy Document (file), Risk Rating (dropdown: High, Medium, Low), Remediation Status (status: N/A, Open, In Progress, Closed). Create groups: Financial Reporting Controls, Transaction Processing Controls, IT General Controls, Entity Level Controls. Add automations: when Next Test Date is within 14 days, assign Tester and notify; when Test Result is 'Fail', create remediation task and notify Control Owner and Internal Audit; when Last Test Date is updated, auto-calculate Next Test Date. Dashboard: control testing status (pie chart), overdue tests (filtered table), fail/exception trend (line chart), controls by process area (bar chart), remediation tracking (status breakdown)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ControlGuard Compliance Manager
**Agent Purpose:** Ensure all Finance SOX controls and policies are tested on schedule, evidence is current, and audit readiness is maintained year-round.

**Triggers:**
- 14 days before any control test due date — initiate testing cycle
- When Test Result is changed to "Fail" or "Pass with Exception"
- When a policy review date is approaching (30 days prior)
- Quarterly — comprehensive controls health check
- When auditor requests are received (manual trigger)

**Actions:**
- Generate testing assignment with specific test procedures and prior period evidence for reference
- Track tester progress and escalate overdue testing to Control Owner after 5 business days
- When a control fails, automatically create remediation plan template with timeline and assign to Control Owner
- Compile auditor-ready control package on demand (control description, test procedures, results, evidence)
- Monitor for process changes that might require control updates (triggered by policy change notifications)
- Generate quarterly SOX dashboard summary for CFO and Audit Committee

**Data Required:**
- SOX control matrix
- Test procedures and prior results
- Policy documents and review history
- Audit finding history
- Process change notifications

**Autonomy Level:** Human-in-the-Loop
Agent manages scheduling, assignments, and reporting. All test results, policy approvals, and remediation sign-offs require human authorization.

**Example Interaction:**
> ControlGuard identifies that 12 controls are due for Q1 testing in the next two weeks. It generates testing assignments for each, attaching the specific test procedure, last quarter's workpaper for reference, and the names of process owners to interview. When the journal entry authorization control (SOX-FIN-004) test reveals that 2 of 25 sampled entries lacked proper dual authorization, the agent immediately creates a remediation item, classifies it as a "Pass with Exception," notifies the VP of Financial Control, and drafts a preliminary root cause analysis (the two exceptions occurred during a week when the backup approver was on leave without a designated alternate). It recommends updating the delegation of authority policy to require standing alternates.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| NII (Net Interest Income) | The difference between interest earned on assets (loans, securities) and interest paid on liabilities (deposits, borrowings) — the primary revenue driver for most banks |
| CECL | Current Expected Credit Losses — the FASB accounting standard (ASC 326) requiring banks to estimate lifetime expected losses on financial assets at origination |
| CCAR | Comprehensive Capital Analysis and Review — the Federal Reserve's annual assessment of capital adequacy and planning for large bank holding companies |
| CET1 Ratio | Common Equity Tier 1 capital ratio — the key regulatory capital metric measuring a bank's core equity capital against risk-weighted assets |
| Call Report | Quarterly FFIEC report (forms 031/041/051) filed by all FDIC-insured institutions reporting financial condition and income |
| FR Y-9C | Federal Reserve consolidated financial statement for bank holding companies with >$3B in total assets |
| ASC 350-40 | GAAP guidance on accounting for costs of computer software developed or obtained for internal use, governing CapEx vs. OpEx treatment |
| Three-Way Match | AP control procedure matching purchase order, goods receipt, and vendor invoice before payment authorization |
| SOX 404 | Sarbanes-Oxley Section 404 requiring management assessment and auditor attestation of internal controls over financial reporting |
| ALM | Asset-Liability Management — the practice of managing risks arising from mismatches between a bank's assets and liabilities (interest rate, liquidity, FX) |
| Intercompany Elimination | Accounting entries that remove the effect of transactions between entities within the same consolidated group |
| MRA | Matter Requiring Attention — a regulatory finding that requires corrective action by bank management |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CFO | Overall financial strategy, board reporting, regulatory relationship | Decision-maker |
| Controller / Chief Accounting Officer | Financial reporting integrity, close management, SOX compliance | Decision-maker |
| VP of Financial Control | Day-to-day accounting operations, policy enforcement | Decision-maker / Influencer |
| Head of FP&A | Budgeting, forecasting, business line financial support | Influencer |
| Head of Regulatory Reporting | Filing accuracy and timeliness across all jurisdictions | Influencer |
| Treasury / ALM Manager | Funding, liquidity management, interest rate risk | Influencer |
| AP Manager | Invoice processing, vendor payments | User |
| Financial Analyst / Senior Accountant | Close tasks, reconciliations, journal entries | User |
| Internal Audit Director | SOX testing oversight, control effectiveness assessment | Influencer |
| Head of Tax | Tax provisioning, regulatory tax filings, transfer pricing | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Technology project cost tracking, GL system integrations, SOX IT general controls | Joint CapEx tracking and IT financial management solution |
| Legal | Regulatory compliance coordination, contract financial terms review | Combined regulatory and legal matter tracking |
| Operations | Operational cost allocation, shared services billing | Operational efficiency and cost management platform |
| Risk | Credit loss provisioning inputs, stress test data, model governance | Integrated risk-finance data workflows |
| PMO | Project budgets flow to CapEx tracking, resource cost allocation | Unified project and financial management |
| HR | Headcount planning, compensation accruals, benefits accounting | Workforce planning integrated with financial planning |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Workiva | SEC/regulatory filing and reporting platform | monday.com handles upstream workflow orchestration; Workiva remains for final filing format — but monday.com can replace the coordination layer |
| BlackLine | Financial close and reconciliation automation | BlackLine excels at recon matching but lacks project/workflow management — monday.com orchestrates the broader close process |
| Anaplan / Adaptive | Enterprise planning and budgeting | Complex modeling stays in planning tools; monday.com manages the budget *cycle* (collection, review, approval) and feeds consolidated data |
| Trintech Cadency | Financial close management | Narrowly focused on close — monday.com provides broader Finance ops coverage plus cross-department visibility |
| ServiceNow | GRC and controls management | Enterprise IT-centric; monday.com is more intuitive for Finance users and faster to deploy |
| Excel/SharePoint | "Default" for everything | The #1 competitor — monday.com replaces the chaotic mix of spreadsheets, email chains, and shared drives |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have BlackLine/Workiva for financial close" | "Those are excellent for what they do — reconciliation matching and regulatory filing formatting. What they don't do is orchestrate the 300+ human tasks, dependencies, and handoffs that make up your close process. monday.com sits on top as the workflow layer, making your existing tools more effective." |
| "Our data is too sensitive for a cloud platform" | "monday.com is SOC 2 Type II certified with enterprise-grade security, data encryption at rest and in transit, and configurable data residency. We serve major financial institutions globally. We can do a security review with your CISO team." |
| "Finance teams need specialized tools, not generic work management" | "Your specialized tools handle the calculations — GL posting, recon matching, planning models. But the *process* around those tools — who does what, by when, with what approvals — that's workflow management. That's where your team is drowning in emails and spreadsheets." |
| "We're in the middle of a core banking transformation — can't add more tools" | "That's exactly when you need workflow orchestration most. Your transformation project itself needs CapEx tracking, milestone management, and cross-team coordination. monday.com can be the operating system for the transformation." |
| "How does this integrate with our GL and financial systems?" | "monday.com integrates via API with major ERP and financial systems. For banks, we typically connect via middleware (MuleSoft, Workato) or direct API to pull status data — not replace your system of record, but provide the workflow layer your existing systems lack." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for banking Finance team references]
- [Placeholder for financial close cycle time improvements]
- [Placeholder for regulatory reporting workflow wins]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
