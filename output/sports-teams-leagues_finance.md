# Sports Teams & Leagues × Finance Playbook

## Overview
Finance organizations inside professional sports franchises and leagues operate at the intersection of player economics, venue operations, broadcast revenue, and partnership cash flows. They manage highly seasonal cash positions, balance player payroll under salary-cap or luxury-tax rules, and coordinate with league finance offices for revenue sharing and compliance reporting. Structures typically include a VP of Finance/CFO, controllers dedicated to team/league entities, revenue accounting squads, FP&A pods for game-day and partnership revenue, and treasury analysts managing credit facilities tied to media rights or stadium bonds.

Regulation and oversight are intense: collective bargaining agreements (CBAs) dictate allowable spending; leagues enforce cap submissions and escrow; municipal bonds or private equity partners demand transparent CapEx governance. Finance teams need near-real-time data from ticketing, merchandising, concessions, sponsorship CRMs, and player operations to answer ownership and league auditors quickly. monday.com provides the connective tissue to normalize these feeds, automate compliance-ready workflows, and give finance leaders auditable visibility without adding headcount.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Finance teams are lean and expected to absorb new compliance (luxury tax, NIL, private equity reporting) without adding controllers; automation offsets close and reporting work. |
| 2 | Consolidate Tech Stack with AI | Medium-High | Data lives across ticketing, POS, CRM, and league portals; mondayDB plus AI normalization reduces spreadsheet sprawl and brittle integrations. |
| 3 | Scale Impact Without Overhead | Medium | FP&A and treasury must support pop-up initiatives (global tours, arena renovations) and answer owners fast; workflows and AI Agents provide scalable governance layers. |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Cap & Payroll Compliance Control Tower

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Cap management teams juggle guaranteed contracts, incentives, two-way deals, and luxury-tax triggers. Data sits in separate spreadsheets maintained by legal, player personnel, and finance. Missing a conversion (e.g., Exhibit 10 bonus) can incur seven-figure penalties or lost roster flexibility.

#### The Solution
Use Work Management + mondayDB to centralize every player contract line item, tagged by cap year, exception type, and guarantee status. Integrate Sidekick to parse CBA clauses and auto-populate key dates. Autom automations alert finance when roster moves hit 90% cap threshold, while Dev blocks capture approvals from legal and basketball ops. Dashboards show real-time cap room vs. hard cap, exception balances, and escrow to the league.

#### The Outcome
Eliminate manual reconciliation cycles, cut compliance review time by 60%, and avoid luxury-tax overages by surfacing threshold breaches the same day they occur.

#### Discovery Questions
- How do you reconcile contract amendments from player personnel with the finance system of record today?  
- What’s the lead time you need to file updated cap sheets with the league office?  
- Which incentives or trade exceptions caused surprises last season?  
- How often does ownership request scenario modeling (injury hardship, mid-level exception, etc.)?  
- Where are you storing historical cap reporting for audits?

#### Industry Context
NBA, NHL, and MLS clubs reference exceptions (MLE, DP, TAM/GAM) that carry different amortization rules. Timing of player option decisions, buyouts, and league escrow holds must tie to payroll calendars, and moves often happen while teams are traveling.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'Cap & Payroll Control Tower' board. Groups: Current Season, Next Season, Future Assets. Columns: Player (People), Contract Type (Dropdown: Rookie, Vet Min, MLE, DP, TAM, Two-Way), Cap Hit (Numbers, 2 decimals), Cash Paid (Numbers), Guarantee % (Numbers), Key Dates (Timeline), Exception Consumed (Dropdown), Approval Status (Status with states Draft, Finance Review, League Submitted), Luxury Tax Impact (Formula), Attachment (Files). Automations: when Approval Status changes to Finance Review notify Legal, when Cap Hit pushes cumulative total above 90% of cap send alert to CFO, when Key Dates arrive create subitem for payment release. Views: Cap Summary Dashboard (chart + widgets), Timeline view by Key Dates, Kanban by Approval Status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Luxury Tax Sentinel  
**Agent Purpose:** Monitor roster and payroll updates to flag tax exposure early and generate league-ready memos.

**Triggers:**
- Player item created or Cap Hit updated  
- Exception Consumed dropdown changes  
- Key Date approaching within 10 days  
- Manual "Run Scenario" button  
- API ingest from roster management tool

**Actions:**
- Calculate projected tax bill vs. ownership thresholds  
- Draft memo summarizing move, CBA reference, and net cap effect  
- Update Dashboard widget notes  
- Notify CFO, GM, and league liaison via Workdocs comment  
- Create review subitems for legal sign-off

**Data Required:**
Contract master dataset, CBA parameters, luxury tax brackets, ownership policy thresholds, league submission templates.

**Autonomy Level:** Human-in-the-Loop — agent drafts analysis and alerts humans before filings.

**Example Interaction:**
> After a two-way contract is converted, the agent ingests the new cap hit, recomputes the apron exposure, and drafts a memo citing the Bi-Annual Exception. It pings finance leadership with a recommendation to waive a 10-day contract or apply for a hardship exception, attaching the pre-filled league form. Legal reviews within minutes instead of chasing spreadsheets overnight.

---

### Use Case 2: Game-Day Event P&L & Settlement

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Each home game or match generates dozens of revenue streams (ticketing, suites, parking, in-seat ordering) and expenses (staffing, security, temporary labor). Settling with promoters, concessionaires, or visiting teams can take 2–3 weeks and delay ownership reporting.

#### The Solution
Work Management board per event pulls ticketing exports via mondayDB sync, concessions data via API, and staffing costs from workforce tools. Automations spin up templated sub-items for revenue categories with Sidekick projecting expected vs. actual. Dashboards show per-cap spend, variable margin, and outstanding settlements. Finance uses monday CRM records to reconcile promoter invoices and track approval workflows through Service for vendor disputes.

#### The Outcome
Compress settlement timelines from weeks to days, surface negative-margin games instantly, and keep cash collections accurate for treasury planning.

#### Discovery Questions
- How are you consolidating feeds from Ticketmaster, SeatGeek, and POS before settlement?  
- What KPIs does ownership request within 24 hours of a game?  
- Where do promoter splits, guarantees, or make-goods get tracked?  
- How do you account for weather-driven staffing changes in real time?  
- Which partners need visibility into settlement status?

#### Industry Context
Major leagues often host non-team events (concerts, international friendlies) with custom settlement rules. Delayed settlements can violate promoter agreements and impact vendor float.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 'Game-Day P&L Hub'. Groups: Upcoming Events, In-Settlement, Closed. Columns: Event Name (Text), Date (Date), Opponent/Promoter (Text), Attendance Forecast (Numbers), Actual Attendance (Numbers), Ticket Revenue (Numbers, currency), Premium & Suites (Numbers), Concessions (Numbers), Parking (Numbers), Variable Labor Cost (Numbers), Net Margin % (Formula), Settlement Owner (People), Settlement Status (Status: Draft, In Review, Sent, Paid), Supporting Docs (Files), Notes (Long Text). Automations: when Settlement Status changes to Sent create follow-up task in CRM, auto-calc Net Margin from revenue/expense columns, reminder 48h post-event if Settlement Status not In Review. Views: Dashboard with revenue mix pie + per-cap KPIs, Calendar of events, Timeline of settlement stages."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Event Cash Closer  
**Agent Purpose:** Orchestrate post-event settlements and cash collection.

**Triggers:**
- Event moves to In-Settlement group  
- Supporting Docs uploaded  
- Settlement Status unchanged for 3 days  
- Payments received feed updated  
- Manual "Escalate" button

**Actions:**
- Compare actuals vs. forecast, highlight variance  
- Draft settlement summary email to promoter with attachments  
- Create receivable in finance system via integration  
- Schedule reminder for AR clerk  
- Notify VP Finance if variance exceeds threshold

**Data Required:**
Ticketing and POS exports, promoter contract terms, receivables ledger, approved cost rates.

**Autonomy Level:** Human-in-the-Loop — agent drafts communications and tasks, humans approve cash postings.

**Example Interaction:**
> After a derby match, the agent ingests sales feeds, notes concessions ran 12% below plan, prepares a settlement PDF, and posts an AR checklist. Finance reviews and sends within 12 hours, unlocking faster promoter payment and a clean variance brief for ownership.

---

### Use Case 3: Sponsorship Contract Revenue Assurance

**Relevance:** Medium-High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Sponsorship deals bundle cash, trade value, media inventory, and performance clauses. Finance relies on deal sheets from partnership sales and manual spreadsheets to recognize revenue. Missed deliverables delay billing, and auditors demand evidence tying fulfillment to invoicing.

#### The Solution
monday CRM records house each partnership deal; Finance board syncs guaranteed payments, in-kind valuations, activation schedules, and escalators. Sidekick parses contract PDFs to populate payment triggers. Automations tie completion of activation tasks (from Creative/Marketing boards) to revenue recognition items. Dashboards show earned vs. deferred revenue, and Service forms allow partnership managers to request billing adjustments with audit trails.

#### The Outcome
Reduce deferred-revenue true-ups, eliminate revenue leakage from unbilled activations, and give auditors a single fulfillment-to-cash record.

#### Discovery Questions
- How do you translate activation completion into journal entries today?  
- What percent of partnership value is trade inventory vs. cash?  
- Which clauses drive revenue holds or clawbacks?  
- How are finance and partnership ops sharing a single view of obligations?  
- Do auditors request sampling evidence mid-season?

#### Industry Context
Naming-rights and jersey patch deals span 10–20 years with CPI escalators, media make-goods, and hospitality credits. Accurate treatment affects credit facility covenants.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Spin up a 'Sponsorship Revenue Assurance' board. Groups: New Deals, In Fulfillment, Ready to Invoice, Audited. Columns: Partner (Connect to CRM Accounts), Contract Value (Numbers), Cash vs Trade % (Numbers), Payment Schedule (Timeline), Deliverable Tracker (Mirror from activation board), Recognition Status (Status: Deferred, Earned, On Hold), Invoice ID (Text), Variance Notes (Long Text), Owner (People), Supporting Contracts (Files). Automations: when Deliverable Tracker shows 100% complete move item to Ready to Invoice, auto-create Workdoc checklist for audit support, notify Controller if Recognition Status flips to On Hold. Views: Dashboard (earned vs deferred), Calendar of payment schedules, Gantt of activation windows."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Partnership Revenue Guardian  
**Agent Purpose:** Ensure contract fulfillment drives timely billing and compliant recognition.

**Triggers:**
- Deliverable completion updates from Creative boards  
- Payment Schedule date reached  
- Recognition Status manually set to On Hold  
- New contract uploaded  
- External ERP invoice sync

**Actions:**
- Generate revenue recognition entry suggestions  
- Draft invoice support package with attachments  
- Flag under-fulfilled obligations with risk score  
- Update dashboards with cash/trade split  
- Notify sponsorship VP of upcoming clawback risks

**Data Required:**
CRM contract metadata, activation tracker, ERP invoicing, trade valuation tables, auditor evidence library.

**Autonomy Level:** Human-in-the-Loop — controller validates entries before posting.

**Example Interaction:**
> When a jersey patch activation hits 95% completion, the agent prepares the revenue journal, cross-checks trade credits, and assembles a deliverable log for auditors. Finance reviews and posts within the same close cycle, preventing quarter-end crunch.

---

### Use Case 4: Stadium CapEx & Renovation Portfolio Management

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Arenas and training facilities constantly upgrade scoreboards, premium clubs, and security systems. Projects often involve public funding, league approvals, and dozens of vendors. Finance must monitor contingency drawdowns and verify expenses align with bond covenants.

#### The Solution
Use Work Management + Dev to run a CapEx portfolio board with mondayDB storing project budgets, funding sources (bond, ownership equity, partnership contribution), and vendor contracts. Automations alert when committed spend crosses stage gates. Dashboards combine Gantt timelines with cash curve forecasts. Service forms allow construction managers to submit change orders that route through finance and legal with required documentation.

#### The Outcome
Increase transparency with ownership and lenders, keep projects within cap, and speed reimbursement from public partners by maintaining auditable packages.

#### Discovery Questions
- What visibility does ownership expect on renovation ROI and payback?  
- Which funding sources (PSL, municipal bonds, league loans) require unique reporting formats?  
- How are change orders approved today?  
- Do you track sustainability credits or tax rebates tied to these projects?  
- How quickly can you produce cost-to-complete snapshots?

#### Industry Context
Projects often span off-seasons with immovable completion dates. League facility guidelines (e.g., NFL G-4 loans) require milestone certifications, and sustainability upgrades may chase LEED credits.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'Stadium CapEx Portfolio' board. Groups: Approved FY26, In Construction, Pending Closeout. Columns: Project Name (Text), Venue Area (Dropdown), Budget (Numbers), Committed Spend (Numbers), Forecast at Completion (Formula), Funding Source Mix (Dropdown multi-select), Start-End (Timeline), GC/Vendor (Text), Change Order Count (Numbers), Risk Rating (Status), Covenant Docs (Files), Finance Owner (People). Automations: when Risk Rating turns Red notify CFO and move to top, when Committed Spend exceeds 85% of Budget auto-create review subitem, monthly reminder to upload lender packet. Views: Timeline, Dashboard comparing budget vs. committed per project, Map view tagging venues if multi-location."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CapEx Compliance Steward  
**Agent Purpose:** Guard capital project spending against overruns and covenant breaches.

**Triggers:**
- Committed Spend updated  
- Change order submitted  
- Monthly lender packet due date  
- Sustainability credit milestone reached  
- Manual "Reforecast" command

**Actions:**
- Recalculate cost-to-complete and contingency remaining  
- Draft lender update with visuals  
- Recommend funding source reallocations  
- Notify procurement about vendor compliance gaps  
- Log required approvals in audit trail

**Data Required:**
Budget vs. actual feeds, contract library, lender covenant checklist, sustainability incentive schedules.

**Autonomy Level:** Human-in-the-Loop — finance reviews packets before distribution.

**Example Interaction:**
> Upon a $2M AV upgrade change order, the agent recalculates ROI, identifies a remaining PSL reserve to cover it, and produces an updated lender memo with variance commentary, cutting prep time from days to minutes.

---

### Use Case 5: League Revenue Share Reconciliation

**Relevance:** Medium-High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Leagues distribute national media, playoff, and merchandising revenues through complex formulas that depend on team performance, market size, and escrow. Teams must reconcile deposits vs. statements and ensure compliance with revenue-sharing reporting.

#### The Solution
mondayDB ingests league statement CSVs; finance boards map distributions to GL accounts and track adjustments or disputes. Autom automations flag variance thresholds, while dashboards show expected vs. received amounts by category (media, licensing, playoff). Link Service workflows to submit clarification tickets to league finance with complete audit logs.

#### The Outcome
Prevent missed distributions, accelerate dispute resolution, and keep leadership current on national cash flows that fund payroll.

#### Discovery Questions
- How do you validate league deposits match the statement line-by-line?  
- What turnaround time does the league expect on discrepancy questions?  
- Which categories (e.g., playoff shares, NBA unit credits) cause the most swings?  
- Do you forecast revenue share to drive in-season cash decisions?  
- How are supporting documents archived for audit?

#### Industry Context
Each league has bespoke revenue share math (NHL HRR, NFL G-4, MLS participation). Teams rely on these funds for mid-season trades or signings, so visibility matters.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Launch a 'League Distribution Reconciliation' board. Groups: Statements Received, In Review, Disputed, Cleared. Columns: Statement Period (Date), Category (Dropdown: Media, Licensing, Playoffs, Other), Amount Expected (Numbers), Amount Received (Numbers), Variance % (Formula), Supporting Statement (Files), League Contact (People), Dispute Ticket (Link), Status (Status: Open, Pending League, Resolved), Notes (Long Text). Automations: when Variance % > 2% change Status to Open and notify Controller, when Status becomes Resolved archive item after 30 days, weekly digest of outstanding disputes. Views: Dashboard variance waterfall, Calendar of statement periods, Table grouped by Category."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Revenue Share Reconciler  
**Agent Purpose:** Match league distribution statements to deposits and escalate variances automatically.

**Triggers:**
- Statement Period item created  
- Bank feed deposit imported  
- Variance % exceeds tolerance  
- Dispute ticket updated  
- Month-end close approaching

**Actions:**
- Auto-match deposits to statements  
- Draft variance explanation referencing league policy  
- Open Service ticket to league contact with attachments  
- Update cash forecast board  
- Notify CFO when variance resolved

**Data Required:**
League statements, bank feeds, GL accounts, league policy docs, contact list.

**Autonomy Level:** Human-in-the-Loop — agent preps reconciliations; finance approves before communicating externally.

**Example Interaction:**
> When a media distribution arrives short, the agent flags it, drafts an email citing clause references, and posts the impact to cash forecast dashboards. Finance approves and the ticket goes to the league the same day.

---

### Use Case 6: Seasonality-Aware Cash Flow Forecasting

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Cash swings wildly between off-season (when payroll and cap holds spike) and in-season (ticket and media cash hits). Finance teams juggle revolving credit lines, revenue share expectations, and CapEx draws without a unified view. Spreadsheet forecasting fails to ingest live sales/expense signals.

#### The Solution
Build a mondayDB-backed cash model combining ticketing forecasts, sponsorship payment schedules, payroll batches, and CapEx draw schedules. Use Work Management dashboards to visualize runway, while Sidekick generates narrative commentary for ownership decks. Automations trigger alerts when projected cash dips below thresholds, prompting treasury actions. Integrate Dev workspace for scenario modeling (injury exceptions, playoff runs) with snapshots saved for board meetings.

#### The Outcome
Improve covenant compliance, reduce revolver interest by timing draws precisely, and give ownership scenario transparency without manual deck building.

#### Discovery Questions
- What cadence do you update rolling 13-week cash forecasts?  
- Which inflows/outflows are hardest to predict (playoffs, revenue share timing, CapEx draws)?  
- How often does ownership request scenario narratives?  
- What systems (ticketing, ERP, payroll) feed your forecast today?  
- Where do you track revolver usage and covenant headroom?

#### Industry Context
Franchises often borrow against future media cash; covenants require look-forward visibility. Post-season success can add tens of millions unexpectedly, so dynamic modeling beats static spreadsheets.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Generate a 'Seasonality Cash Forecast' board. Groups: Base Plan, Playoff Scenario, Renovation Scenario. Columns: Week Start (Date), Cash In (Numbers), Cash Out (Numbers), Net Position (Formula), Driver (Dropdown: Ticketing, Sponsorship, Media, Payroll, CapEx, Debt), Source System (Dropdown), Probability (Numbers), Narrative (Long Text), Approval (Status), Treasury Owner (People). Automations: calculate Net Position, when Net Position falls below 0 trigger alert to Treasury Owner, monthly snapshot to Workdoc for ownership deck. Views: Dashboard with rolling cash curve, Calendar, Chart grouping by Driver."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Seasonality Maestro  
**Agent Purpose:** Maintain rolling cash forecasts and narrate variances for leadership.

**Triggers:**
- New inflow/outflow entry  
- Net Position dips below threshold  
- Ownership meeting date approaching  
- Scenario toggled  
- Revolver balance feed updated

**Actions:**
- Recalculate projections across scenarios  
- Draft exec summary with confidence levels  
- Recommend draw/repay actions on credit lines  
- Push alerts to CFO and treasury analyst  
- Update dashboard annotations with context

**Data Required:**
Ticketing projections, sponsorship payment schedules, payroll calendars, CapEx plans, credit facility details.

**Autonomy Level:** Human-in-the-Loop — agent advises but treasury executes draws.

**Example Interaction:**
> With playoff clinch probability rising, the agent layers incremental home games into the cash model, produces a memo recommending delayed revolver draw, and updates the board packet automatically.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Luxury Tax Apron | Spending ceiling that, once exceeded, triggers escalating tax payments and limits on roster moves. |
| CBA (Collective Bargaining Agreement) | Contract between league and players’ union governing payroll rules, benefits, and compliance reporting. |
| PSL (Personal Seat License) | Upfront fee granting rights to purchase season tickets; often finances stadium projects. |
| HRR / Basketball Related Income | League-defined revenue pools used to calculate revenue sharing or escrow. |
| Make-Good | Additional inventory or value delivered to sponsors when original commitments fall short. |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CFO / EVP Finance | Owns financial strategy, league reporting, covenants | Decision-maker |
| Controller / Director of Accounting | Manages close, audits, revenue recognition | Decision-maker |
| VP FP&A / Strategy | Builds forecasts, scenario modeling for ownership | Influencer |
| Treasurer / Cash Manager | Oversees liquidity, credit facilities, banking | Influencer |
| League Finance Liaison | Coordinates reporting between club and league | Influencer |
| Partnership Finance Manager | Bridges sponsorship sales and accounting | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Player Personnel / GM Office | Provides contract data, incentives, roster timing | Embed approval workflows and shared dashboards |
| Sponsorship & Partnerships | Supplies activation status and billing triggers | Align CRM + finance data for revenue assurance |
| Stadium / Venue Operations | Drives event costs, CapEx requests | Implement shared CapEx governance boards |
| Ticketing & Business Intelligence | Forecast attendance, pricing | Automate feeds into cash models |
| Legal & Compliance | Reviews contracts, filings | Use unified approval records for audits |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Excel/Google Sheets | Ad-hoc cap sheets, cash forecasts | Replace brittle manual work with relational mondayDB + automations |
| SAP/Oracle ERP | System of record for GL | Keep ERP but layer monday.com for workflows, approvals, and AI summarization |
| KORE Sponsorship | Activation tracking | Integrate data while using monday.com for finance workflows and revenue recognition governance |
| Smartsheet | Project tracking | monday.com delivers deeper automation, dashboards, AI agents, and native CRM/work management |
| Custom Access Databases | Legacy contract databases | Migrate schemas into mondayDB with audit trails and Sidekick parsing |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have the league’s cap tool." | monday.com layers approvals, automation, and cross-team collaboration on top of league systems, ensuring finance, legal, and ops see one version with audit trails. |
| "Our ERP controls recognition — we can’t replace it." | Keep ERP as the ledger; monday.com orchestrates upstream workflows, ensuring clean, validated data enters the ERP via integrations. |
| "Finance has no bandwidth to implement another platform." | Pre-built playbooks, Vibe prompts, and AI Agents jump-start boards; monday partners or SEs can import templates and connect data sources in days. |
| "Security is a concern with player contracts." | monday.com offers enterprise-grade security, granular permissions, SOC 2, and field-level protections so sensitive data stays restricted while workflows stay automated. |

## Proof Points
*(To be populated with customer references)*
- Placeholder

---

*Generated: 2026-02-23 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
