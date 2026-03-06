# Investment Banking × Operations Playbook

## Overview

Operations in investment banking — often called "the back office" and increasingly "middle office" — is the engine that ensures every trade, settlement, and transaction flows accurately from execution to final booking. In bulge-bracket firms, Operations departments can number in the thousands, spanning trade support, settlements, reconciliations, corporate actions, collateral management, and regulatory reporting. At boutique and mid-market banks, leaner teams of 50–200 handle similar complexity with fewer bodies, making efficiency existential.

The regulatory environment is punishing. Basel III/IV capital requirements, Dodd-Frank, MiFID II, EMIR, and SEC Rule 15c3-3 all impose strict timelines, audit trails, and reporting obligations. T+1 settlement (now standard in the US as of 2024) has compressed what were already tight windows, and any break in the chain — a failed trade, an unmatched confirmation, a missed margin call — cascades into financial penalties, regulatory scrutiny, and reputational damage.

Investment banking Ops teams live in a world of legacy systems (Murex, Calypso, Summit, Broadridge), manual reconciliation spreadsheets, and constant firefighting. The pressure to modernize is immense, but the risk tolerance for disruption is near zero. monday.com enters not as a replacement for core trading systems, but as the orchestration layer that connects people, processes, and exceptions across fragmented technology stacks.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | IB Ops teams spend 40-60% of time on manual reconciliation, break resolution, and exception handling — tasks ripe for AI augmentation |
| 2 | Scale Impact Without Overhead | High | T+1 settlement and increasing trade volumes demand processing more with the same headcount |
| 3 | Consolidate Tech Stack with AI | Medium-High | Ops teams juggle 8-15 tools for trade lifecycle management; a unified orchestration layer reduces context-switching and license costs |

## Prioritized Use Cases

---

### Use Case 1: Trade Break & Exception Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Trade breaks — mismatches between front-office booking and back-office records, failed settlements, unmatched confirmations — consume 50%+ of Ops analyst time. In a typical mid-market IB, 200-500 breaks occur daily across equities, fixed income, and derivatives. Each break requires manual investigation: pulling data from multiple systems (OMS, clearing platforms, custodian portals), identifying root cause, coordinating with counterparties, and documenting resolution. Average resolution time is 4-8 hours per complex break, and aged breaks (>T+3) trigger regulatory escalation. Most teams track breaks in shared Excel files or email chains, creating zero visibility for management.

#### The Solution
monday.com Work Management serves as the central break management hub. Each break becomes an item with structured fields: trade ID (text), asset class (dropdown: Equities/Fixed Income/Derivatives/FX/Commodities), break type (status: Unmatched/Pricing Discrepancy/Settlement Fail/Missing Allocation/Incorrect SSI), severity (dropdown: P1-Critical/P2-High/P3-Medium/P4-Low), counterparty (text), notional value (numbers), break date (date), and assigned analyst (people). Automations route breaks by asset class and severity to specialized sub-teams. Dashboard views show real-time aging analysis, break trends by counterparty, and SLA compliance. mondayDB stores historical break data for pattern analysis.

#### The Outcome
- 60% reduction in average break resolution time (from 6 hours to 2.4 hours)
- 95% SLA compliance on T+1 break resolution (up from ~70%)
- Zero aged breaks beyond T+5 (regulatory threshold)
- 30% reduction in manual reconciliation headcount needs through automation
- Full audit trail for regulatory examination readiness

#### Discovery Questions
1. "How many trade breaks does your team process daily, and what's your current aging distribution — what percentage are resolved same-day vs. carried over?"
2. "When a break occurs, how many systems does an analyst typically need to access to identify root cause, and how long does that investigation take on average?"
3. "Do you have visibility today into break trends by counterparty or asset class, or does that require manual analysis?"
4. "What happens when a break ages past T+3 — is there an automated escalation process, or does someone need to flag it manually?"
5. "How do you currently report break metrics to senior management and regulators — is that a manual report-building exercise?"

#### Industry Context
Trade breaks are the bread and butter of IB Ops. The SE should understand that "breaks" aren't bugs — they're expected outcomes of a complex ecosystem where multiple parties (executing broker, prime broker, custodian, clearinghouse, counterparty) must independently agree on trade details. The shift to T+1 has made break resolution time-critical because there's essentially one business day to resolve before settlement failure. Key terms: DTC (Depository Trust Company), NSCC (National Securities Clearing Corporation), SSI (Standard Settlement Instructions), affirmation vs. confirmation, DTCC CTM/TradeSuite.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Trade Break Management system. Create a board called 'Trade Break Tracker' with these columns: Trade ID (text), Asset Class (dropdown: Equities, Fixed Income, Derivatives, FX, Commodities), Break Type (status with groups: Unmatched Trade, Pricing Discrepancy, Settlement Failure, Missing Allocation, Incorrect SSI, Duplicate Booking), Severity (dropdown: P1-Critical, P2-High, P3-Medium, P4-Low), Counterparty (text), Notional Value (numbers, USD), Break Detected Date (date), Target Resolution Date (date), Assigned Analyst (people), Resolution Status (status: New, Investigating, Pending Counterparty, Escalated, Resolved, Closed), Root Cause (dropdown: Front Office Error, Counterparty Mismatch, System Issue, SSI Change, Late Allocation, Market Data), Resolution Notes (long text). Add automations: when Break Type changes, if Severity is P1-Critical, notify the group and set Target Resolution Date to today; when Resolution Status is Pending Counterparty for more than 4 hours, change Severity to next level up; when Resolution Status changes to Resolved, move to Closed group after 24 hours. Create a Dashboard with widgets: break count by Asset Class (chart), aging analysis showing breaks by days outstanding (chart), resolution time trends (chart), SLA compliance percentage (numbers widget), breaks by Counterparty (table), P1 breaks currently open (table filtered view). Add a Kanban view grouped by Resolution Status, and a Timeline view showing break lifecycle from detection to resolution."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BreakBot — Trade Break Triage Agent
**Agent Purpose:** Automatically classify, prioritize, and route trade breaks while suggesting probable root causes based on historical patterns.

**Triggers:**
- New item created on Trade Break Tracker board (via integration with reconciliation system)
- Break ages past 4 hours without status change
- P1-Critical break detected
- Daily morning trigger at 6:30 AM ET to generate pre-market break summary
- Counterparty-specific break threshold exceeded (>5 breaks from same counterparty in 24 hours)

**Actions:**
- Auto-classify break type and severity based on trade attributes and historical patterns
- Suggest probable root cause with confidence score (e.g., "87% likely SSI change — counterparty updated SSIs on 2/15")
- Route to appropriate analyst based on asset class expertise and current workload
- Generate counterparty outreach email draft for unmatched trades
- Escalate to team lead when resolution SLA is at risk
- Compile daily break report with trend analysis and counterparty risk flags

**Data Required:**
- Historical break data (mondayDB) with resolution outcomes
- Counterparty SSI database
- Trade booking data (via API from OMS)
- Analyst availability and specialization mapping

**Autonomy Level:** Human-in-the-Loop
Auto-classifies and routes all breaks. Auto-generates counterparty communications as drafts. Requires human approval for: escalation to senior management, any communication with regulators, and resolution sign-off on breaks >$10M notional.

**Example Interaction:**
> At 7:15 AM ET, BreakBot processes the overnight reconciliation feed and identifies 47 new breaks. It auto-classifies each: 12 are tagged as "likely SSI changes" after cross-referencing counterparty SSI update logs, 8 as "late allocations" from a prime broker known for delayed feeds, 15 as standard pricing discrepancies within tolerance that it marks for auto-resolution, and 12 requiring manual investigation. It assigns analysts based on their asset class specialty and current queue depth — Sarah gets the fixed income breaks, Mike handles equities, and the derivatives breaks go to the specialist team.
>
> One break stands out: a $250M interest rate swap with Goldman Sachs shows a 15-basis-point pricing discrepancy. BreakBot flags it as P1-Critical, notes that this counterparty has had 3 similar breaks this month (pattern detected), and drafts an outreach email to Goldman's Ops team referencing the specific trade details and prior resolution precedents. It notifies the team lead and places the item at the top of the priority dashboard.
>
> By 9:00 AM, before the trading desk is fully active, 15 breaks have been auto-resolved, 20 are in active investigation with suggested root causes, and the team lead has a clean summary of the 12 items needing attention — with estimated resolution times based on historical averages for similar break types.

---

### Use Case 2: Settlement & Clearing Workflow Orchestration

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The post-trade settlement process involves a precise sequence of steps: trade confirmation → affirmation → matching → netting → settlement instruction delivery → funding → settlement. Each step has dependencies, deadlines, and multiple participants. With T+1, the entire chain must complete within one business day. Operations teams currently manage this across disparate systems — DTCC for clearing, SWIFT for messaging, custodian portals for settlement status — with no unified view of where each trade stands in the lifecycle. When volumes spike (earnings season, index rebalancing, market volatility events), the manual coordination breaks down, leading to failed settlements that cost $50-100 per fail in penalties plus opportunity cost of tied-up capital.

#### The Solution
monday.com orchestrates the end-to-end settlement workflow as a visual pipeline. Each trade flows through status groups representing lifecycle stages: Executed → Confirmed → Affirmed → Matched → Settled. Automations trigger status transitions based on time-based rules and integration feeds. A Timeline view shows the critical path for each settlement date. Dashboard widgets display real-time settlement rates, pending confirmations by counterparty, funding requirements by currency, and fail predictions. The system integrates with SWIFT/FIX message feeds to auto-update statuses and flag exceptions that need human intervention.

#### The Outcome
- 99.5% settlement rate (up from 97%, where each 1% improvement = millions in avoided fail charges)
- 70% reduction in manual status-checking across systems
- Real-time visibility into settlement pipeline for management and risk teams
- Proactive identification of at-risk settlements 4+ hours before deadline
- Capacity to handle 2x trade volume without additional headcount

#### Discovery Questions
1. "What's your current settlement fail rate, and can you quantify the direct cost of fails — both penalties and the capital impact of failed trades?"
2. "How many systems does your team access daily to track settlement status, and how much time is spent simply gathering status updates?"
3. "During high-volume periods like index rebalancing or triple witching, how does your team scale — do you rely on overtime, or do things simply slip?"
4. "Do you have a way to predict which trades are at risk of failing before the settlement deadline, or is it reactive?"
5. "How do you coordinate with your funding desk to ensure settlement accounts are properly funded across currencies?"

#### Industry Context
Settlement is where the rubber meets the road in IB Ops. The SE should know that T+1 (implemented May 2024 in the US) was a seismic shift — it halved the time available for post-trade processing. DTC settlement occurs via NSCC's Continuous Net Settlement (CNS) system. Bilateral OTC trades (derivatives, FX) settle differently, often through CLS for FX or LCH/CME for cleared derivatives. "Fails" are industry jargon for settlements that don't complete on the intended date — they're tracked, reported to regulators, and can trigger buy-in processes.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Settlement Pipeline Tracker. Create a board called 'Settlement Lifecycle' with columns: Trade ID (text), Settlement Date (date), Asset Class (dropdown: Equities, Fixed Income, Derivatives, FX, Structured Products), Counterparty (text), Notional/Quantity (numbers), Currency (dropdown: USD, EUR, GBP, JPY, CHF, CAD, AUD), Clearing Venue (dropdown: DTCC/NSCC, Euroclear, Clearstream, LCH, CME, Bilateral), Lifecycle Stage (status: Executed, Confirmed, Affirmed, Matched, Settling, Settled, Failed), Fail Risk Score (numbers, 1-100), Funding Status (status: Funded, Pending, Shortfall), Assigned Ops Analyst (people), Notes (long text). Create 5 groups matching lifecycle stages. Add automations: when a new item is created, set Lifecycle Stage to Executed; if Lifecycle Stage hasn't moved from Confirmed within 2 hours of Settlement Date, flag as high Fail Risk and notify team; when Lifecycle Stage changes to Failed, create a linked item on Trade Break Tracker board. Create a Dashboard with: settlement pipeline funnel (chart showing items at each stage), fail rate trend (line chart, weekly), pending settlements by counterparty (table), funding requirements by currency for today (numbers widgets), at-risk settlements table (filtered where Fail Risk > 70). Add Timeline view showing trades against their settlement dates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SettleGuard — Predictive Settlement Agent
**Agent Purpose:** Predict settlement failures before they occur and orchestrate preemptive actions to ensure on-time settlement.

**Triggers:**
- New trade enters settlement pipeline
- 4 hours before settlement deadline with trade still in pre-matched status
- Funding shortfall detected in any settlement currency
- Counterparty historically associated with late confirmations submits a trade
- Daily 5:00 AM ET pre-settlement risk scan

**Actions:**
- Calculate fail risk score based on: counterparty history, asset class complexity, time remaining, confirmation status, funding availability
- Send priority-ordered task list to Ops analysts each morning
- Auto-generate SWIFT confirmation reminder messages to counterparties
- Alert funding desk of currency-specific shortfalls with recommended amounts
- Create linked break items when settlements fail, pre-populated with context
- Generate end-of-day settlement report with metrics and next-day risk outlook

**Data Required:**
- Historical settlement data with fail/success outcomes (mondayDB)
- Real-time clearing system status feeds
- Counterparty confirmation behavior history
- Funding account balances by currency
- Market calendar (holidays, half-days by market)

**Autonomy Level:** Escalation-Based
Fully autonomous for risk scoring, alerting, and report generation. Auto-sends confirmation reminders to counterparties. Escalates to human for: funding reallocation decisions, counterparty escalation calls, and regulatory fail reporting.

**Example Interaction:**
> At 5:00 AM ET, SettleGuard runs its daily pre-settlement scan. It identifies 1,247 trades settling today, calculates risk scores for each, and surfaces 23 trades with fail risk >70%. The top concern: a block of 15 equity trades with a European counterparty that hasn't submitted affirmations — and this counterparty has a 12% historical late-affirmation rate. SettleGuard has already sent an automated reminder via SWIFT at 4:00 AM, and now creates a priority task for the London-based analyst to follow up by phone when European markets open.
>
> It also flags a JPY funding shortfall of ¥2.3B for today's settlements, calculates that the bank's Tokyo nostro account has sufficient balance but requires an internal transfer, and alerts the funding desk with the exact amount and deadline. The morning dashboard shows the team exactly what needs attention, in priority order, before the first settlement window opens at 8:00 AM ET.

---

### Use Case 3: Regulatory Reporting & Compliance Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banking Ops teams face a staggering regulatory reporting burden: CFTC swap data reporting, SEC Rule 606 order routing reports, CAT (Consolidated Audit Trail) submissions, MiFID II transaction reporting, EMIR trade reporting, Basel III/IV capital adequacy calculations, and dozens more. Each regulation has its own format, timeline, and submission mechanism. A single reporting failure can result in fines ranging from $50K to $50M+. Currently, regulatory reporting is a patchwork of automated feeds from trading systems, manual data extraction, Excel-based transformations, and manual submissions. Each regulatory change requires months of IT development to update reporting pipelines. Compliance teams have limited visibility into whether today's reports were submitted accurately and on time until after the fact.

#### The Solution
monday.com serves as the regulatory reporting orchestration and tracking layer. Each reporting obligation becomes a recurring item with defined workflows: data extraction → validation → transformation → submission → confirmation. Status columns track each stage with deadlines tied to regulatory timelines. Automations alert responsible teams when stages are approaching SLA limits. Dashboard views provide a real-time "regulatory scoreboard" showing compliance status across all obligations. When new regulations or amendments are published, they're tracked as projects with implementation milestones linked to affected reports.

#### The Outcome
- 100% on-time regulatory submission rate (zero late filings)
- 80% reduction in time spent on compliance status meetings (replaced by real-time dashboards)
- Proactive identification of at-risk reports 48+ hours before deadlines
- Complete audit trail of every reporting action for regulatory examination
- 50% faster implementation of new regulatory requirements through standardized workflows

#### Discovery Questions
1. "How many distinct regulatory reports does your Ops team produce, and what's the frequency for each — daily, weekly, monthly, quarterly?"
2. "Have you experienced any late or incorrect regulatory submissions in the past year, and what was the impact — financial penalties, regulatory scrutiny, or remediation costs?"
3. "When a new regulation is announced — like the recent CAT Phase 2e requirements — how long does it typically take your team to update your reporting processes?"
4. "Who has visibility into whether today's reports were all submitted correctly and on time? Is that a dashboard, or does someone need to manually check?"
5. "How do you manage the audit trail for regulatory submissions — if a regulator asked you to demonstrate your process for a specific report, how quickly could you produce that documentation?"

#### Industry Context
Regulatory reporting is non-negotiable and increasingly complex. The SE should understand that investment banks operate under multiple overlapping regulatory regimes depending on their jurisdiction and business lines. Key regulators: SEC, CFTC, FINRA, FCA, BaFin, ESMA. Key reporting frameworks: CAT (Consolidated Audit Trail), TRACE (Trade Reporting and Compliance Engine), EMIR/SFTR (EU), MAS (Singapore). The term "regtech" refers to technology specifically designed for regulatory compliance. Many banks have dedicated "regulatory change management" teams that track upcoming rule changes — this is a natural extension of the use case.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Reporting Tracker. Create a board called 'Regulatory Obligations Dashboard' with columns: Regulation Name (text), Report Name (text), Regulator (dropdown: SEC, CFTC, FINRA, FCA, ESMA, BaFin, MAS, OCC, Fed), Jurisdiction (dropdown: US, EU, UK, APAC, Global), Frequency (dropdown: Real-Time, Daily, Weekly, Monthly, Quarterly, Annual, Ad-Hoc), Submission Deadline (date), Data Source Systems (text), Report Owner (people), Backup Owner (people), Current Status (status: Not Started, Data Extracted, Validating, Transforming, Ready to Submit, Submitted, Confirmed, Late, Failed), Last Submission Date (date), Last Submission Result (status: Success, Partial, Failed, Pending Confirmation), Regulatory Change Flag (status: No Changes, Amendment Pending, New Requirement, Sunset), Notes (long text). Group items by Regulator. Add automations: when Current Status hasn't changed from Not Started and Submission Deadline is within 24 hours, notify Report Owner and their manager; when Current Status changes to Failed, create an item on an 'Incidents' board and notify compliance leadership; on the first of each month, create new items for all monthly reports with pre-populated deadlines. Create a Dashboard with: compliance scorecard (percentage on-time this month, quarter, year), upcoming deadlines in next 7 days (table), overdue items (filtered table, red highlight), submissions by regulator (chart), trend of late submissions over 12 months (line chart). Add Calendar view for deadline visualization."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RegWatch — Regulatory Compliance Agent
**Agent Purpose:** Monitor regulatory reporting deadlines, track completion status, and proactively prevent late or failed submissions.

**Triggers:**
- 48 hours before any regulatory submission deadline
- Report status changes to Failed or Late
- New regulatory amendment published (via RSS/API feed from regulatory bodies)
- Weekly Monday 7:00 AM compliance summary generation
- Quarterly regulatory examination preparation (30 days before quarter-end)

**Actions:**
- Send deadline countdown notifications with escalating urgency (48h → 24h → 4h → 1h)
- Auto-generate pre-submission validation checklist based on regulation requirements
- Create regulatory change impact assessment items when new rules are detected
- Compile quarterly compliance summary for senior management and board reporting
- Cross-reference submitted data against known validation rules and flag anomalies
- Generate examination-ready audit packages with full submission history and evidence trail

**Data Required:**
- Complete regulatory obligation inventory with deadlines and requirements
- Historical submission records and outcomes (mondayDB)
- Regulatory body RSS feeds or API endpoints for rule change alerts
- Report generation system status feeds
- Organizational chart for escalation routing

**Autonomy Level:** Human-in-the-Loop
Autonomous for monitoring, alerting, and report compilation. Requires human approval for: actual regulatory submissions, communications with regulators, and sign-off on compliance certifications.

**Example Interaction:**
> On Monday morning, RegWatch generates the weekly compliance outlook: 14 reports due this week across 4 regulators. It notes that the CFTC Large Trader Report (due Wednesday) has a data extraction step that typically takes 6 hours but hasn't started yet — it flags this as amber risk and assigns the responsible analyst with a "start by Tuesday 10 AM" recommendation based on historical processing times.
>
> Mid-week, RegWatch detects via its ESMA RSS feed that a new amendment to EMIR Refit reporting has been published with a 6-month implementation deadline. It automatically creates a regulatory change project with milestone dates, tags the compliance and technology teams, and pre-populates an impact assessment template noting which existing reports are affected based on keyword matching against the amendment text.

---

### Use Case 4: Corporate Actions Processing

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Corporate actions — dividends, stock splits, mergers, tender offers, rights issues, spin-offs — are among the most error-prone processes in IB Ops. A mid-size investment bank processes 500-2,000 corporate action events monthly. Each event requires: identification from multiple data sources (DTCC, Bloomberg, custodians), interpretation of complex terms, impact analysis across all affected positions, election processing (for voluntary events), entitlement calculation, and booking. Mandatory events like dividends seem simple but involve tax reclaim processing across dozens of jurisdictions. Voluntary events like tender offers have strict deadlines where a missed election means defaulting to unfavorable terms. Industry estimates suggest corporate actions processing errors cost the financial industry $1-3 billion annually.

#### The Solution
monday.com manages the corporate action lifecycle from announcement to completion. Each event is an item with structured data: event type (dropdown), ISIN/CUSIP (text), ex-date/record-date/pay-date (dates), affected positions (linked items), election deadline (date), election choice (status), processing status (status with stages). Automations enforce deadline-driven workflows: voluntary events auto-escalate as election deadlines approach, mandatory events auto-progress through processing stages. Dashboard views show upcoming events by type and deadline, positions at risk, and processing backlog. Integration with market data feeds auto-creates events from announcements.

#### The Outcome
- Zero missed voluntary election deadlines (currently 2-5 per quarter industry-wide)
- 50% reduction in corporate actions processing time through structured workflows
- 99.9% entitlement accuracy (reducing costly manual corrections)
- Complete audit trail for tax reclaim documentation
- Real-time visibility into upcoming events and their portfolio impact

#### Discovery Questions
1. "How many corporate action events does your team process monthly, and what's the split between mandatory and voluntary events?"
2. "Have you ever missed a voluntary corporate action election deadline, and what was the financial impact?"
3. "How do you currently track the lifecycle of a corporate action from announcement through to final booking — is that in a single system or spread across multiple?"
4. "For complex events like mergers with mixed consideration or multi-currency dividends, how much manual calculation is involved?"
5. "What's your process for cross-border tax reclaim on dividends — is that automated or manual, and how much revenue do you recover?"

#### Industry Context
Corporate actions are considered one of the highest-risk areas in IB Ops because errors directly impact client positions and P&L. The SE should know the difference between mandatory events (happen automatically — dividends, splits), mandatory with choice (default option unless client elects otherwise — some mergers), and voluntary events (client must actively elect — tender offers, rights issues). Key data vendors: DTCC (ISO 15022/20022 messages), Bloomberg CACT, ICE. The "scrubbing" process refers to cleaning and normalizing corporate action data from multiple sources into a golden record.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Corporate Actions Management system. Create a board called 'Corporate Actions Tracker' with columns: Event ID (text), Event Type (dropdown: Cash Dividend, Stock Dividend, Stock Split, Reverse Split, Merger, Tender Offer, Rights Issue, Spin-Off, Exchange Offer, Redemption, Name Change), Security Identifier (text — ISIN/CUSIP), Security Name (text), Issuer (text), Announcement Date (date), Ex-Date (date), Record Date (date), Pay Date (date), Election Deadline (date), Event Category (status: Mandatory, Mandatory with Choice, Voluntary), Processing Stage (status: Announced, Data Scrubbed, Positions Identified, Elections Pending, Elections Submitted, Entitlements Calculated, Booked, Reconciled, Closed), Affected Accounts (numbers — count), Total Position Exposure (numbers, USD), Election Choice (dropdown: Accept, Reject, Default, Cash, Stock, Mixed), Assigned Processor (people), Priority (dropdown: Critical, High, Standard, Low), Notes (long text). Group by Event Category. Add automations: when Election Deadline is within 48 hours and Elections Pending status, escalate to team lead and send urgent notification; when Processing Stage changes to Booked, auto-create reconciliation task due in 2 business days; when new item created with Event Category Voluntary, immediately assign to senior processor. Create Dashboard with: upcoming elections timeline (next 30 days), events by type distribution (pie chart), processing backlog by stage (bar chart), high-exposure events table (filtered by Total Position Exposure > $10M), daily processing metrics (items completed vs. target)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CorpActBot — Corporate Actions Intelligence Agent
**Agent Purpose:** Auto-scrub corporate action announcements, identify position exposure, recommend elections, and ensure zero missed deadlines.

**Triggers:**
- New corporate action announcement received from data feed
- Election deadline approaching (7 days, 48 hours, 24 hours, 4 hours)
- Position change in a security with an active corporate action
- Daily 6:00 AM reconciliation of processed events vs. pay-date settlements
- Discrepancy detected between multiple data sources for same event

**Actions:**
- Auto-create and populate corporate action items from announcement feeds
- Cross-reference event details across DTCC, Bloomberg, and custodian notifications to build golden record
- Calculate portfolio-wide exposure and affected account list
- Generate election recommendation with financial analysis (e.g., "Cash option yields 3.2% premium over stock at current price")
- Send escalating deadline reminders to portfolio managers for voluntary events
- Auto-book mandatory event entitlements after validation

**Data Required:**
- Corporate action data feeds (DTCC ISO 20022, Bloomberg CACT)
- Real-time position data across all accounts
- Historical corporate action outcomes and pricing data
- Client election preference profiles
- Tax treaty database for dividend withholding calculations

**Autonomy Level:** Human-in-the-Loop
Auto-scrubs and creates events, auto-calculates exposure, auto-books mandatory events (dividends, splits) after validation. Requires human approval for: voluntary election submissions, complex event interpretations (merger terms), and any manual booking adjustments.

**Example Interaction:**
> CorpActBot receives a DTCC announcement for a $2.50/share special dividend from a pharmaceutical company following an asset sale. Within minutes, it identifies 847 affected accounts across the firm's client base, calculates total entitlement of $4.2M, flags 23 accounts with non-standard tax treaties requiring manual withholding rate review, and creates the corporate action item fully populated with all details. It links the event to the settlement pipeline for the pay date and pre-creates the reconciliation task.
>
> For a voluntary tender offer received the same day, CorpActBot analyzes the offer terms ($45.00 cash per share vs. current market price of $42.30), generates an election recommendation summary showing the 6.4% premium, and immediately notifies the 12 portfolio managers with affected positions. It sets up a countdown dashboard showing days until election deadline and tracks which PMs have responded. Three days before deadline, it escalates to the PM's supervisor for any outstanding elections.

---

### Use Case 5: Client Onboarding & KYC Operations

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Onboarding a new institutional client for investment banking services is a 30-90 day odyssey involving KYC (Know Your Customer) documentation, AML (Anti-Money Laundering) screening, credit assessment, legal documentation (ISDA Master Agreements, CSAs, GMRAs), account setup across trading systems, and regulatory classification (MiFID categorization, Dodd-Frank entity classification). The process involves 10+ teams (Compliance, Legal, Credit, Ops, Technology, Front Office) and dozens of handoffs. Documents are tracked in email, shared drives, and disparate case management systems. Clients are frustrated by repeated requests for the same information, and front office is frustrated by the time-to-revenue delay. Incomplete onboarding also creates risk — trading with an improperly classified or screened counterparty can result in severe regulatory penalties.

#### The Solution
monday.com serves as the unified client onboarding orchestration platform. Each new client is a project with standardized phases: KYC Document Collection → Compliance Review → Credit Assessment → Legal Documentation → System Setup → UAT → Go-Live. Each phase has defined tasks, owners, SLAs, and dependencies. Document collection is managed through monday.com Forms with structured fields for required documents by entity type. Status automations track progress and flag bottlenecks. A client-facing portal (via monday.com WorkForms) allows clients to submit documents and check onboarding status, reducing "where are we?" inquiries.

#### The Outcome
- 40% reduction in average onboarding time (from 60 days to 36 days)
- 90% reduction in client "status check" inquiries through self-service portal
- 100% compliance with KYC documentation requirements (zero gaps at go-live)
- Cross-team visibility eliminates 80% of internal coordination meetings
- Standardized process ensures consistent experience regardless of client size or type

#### Discovery Questions
1. "What's your average time-to-revenue for a new institutional client — from initial agreement to first trade?"
2. "How many teams are involved in client onboarding, and is there a single owner or orchestrator of the end-to-end process?"
3. "How often do you discover KYC documentation gaps after a client has already started trading, and what's the remediation process?"
4. "Do your clients have visibility into their onboarding status, or do they rely on their relationship manager for updates?"
5. "When regulators examine your KYC processes, how easily can you demonstrate the complete documentation trail for a given client?"

#### Industry Context
KYC/AML in investment banking is far more complex than retail banking. Institutional clients are often complex legal structures — SPVs, fund-of-funds, sovereign wealth entities — requiring beneficial ownership analysis through multiple layers. FATCA and CRS add cross-border tax reporting obligations. The ISDA Master Agreement negotiation alone can take weeks for complex derivatives relationships. Key terms: UBO (Ultimate Beneficial Owner), PEP (Politically Exposed Person), SAR (Suspicious Activity Report), EDD (Enhanced Due Diligence), LEI (Legal Entity Identifier).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client Onboarding Management system for investment banking. Create a board called 'Client Onboarding Pipeline' with columns: Client Legal Name (text), Entity Type (dropdown: Corporation, Fund, SPV, Sovereign, Bank, Insurance, Pension), Jurisdiction of Incorporation (text), Relationship Manager (people), Onboarding Lead (people), Onboarding Phase (status: KYC Collection, Compliance Review, Credit Assessment, Legal Documentation, System Setup, UAT, Go-Live, Complete), KYC Status (status: Documents Requested, Partially Received, Under Review, Approved, Deficient), AML Screening Result (status: Clear, Flagged, Enhanced Due Diligence Required, Blocked), Credit Approval (status: Pending, Conditionally Approved, Approved, Declined), ISDA Status (status: Not Required, Drafting, Negotiation, Executed), Target Go-Live Date (date), Days in Pipeline (formula), Risk Rating (dropdown: Low, Medium, High, Critical), Priority (dropdown: Strategic, Standard, Expedited), Revenue Potential (numbers, USD annual), Notes (long text). Group by Onboarding Phase. Add automations: when KYC Status is Documents Requested for more than 14 days, notify RM to follow up with client; when AML Screening Result changes to Flagged, automatically assign to senior compliance officer; when all sub-statuses are complete, advance Onboarding Phase to next stage. Create a Dashboard with: pipeline funnel by phase (chart), average days by phase (bar chart), bottleneck identification (which phase has most items), onboardings completed this month vs. target, revenue potential in pipeline (sum)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OnboardIQ — Client Onboarding Orchestrator
**Agent Purpose:** Orchestrate multi-team client onboarding, eliminate bottlenecks, and ensure compliant, timely go-live for new institutional relationships.

**Triggers:**
- New client onboarding request submitted
- Document uploaded by client via WorkForm
- Any onboarding phase exceeds its SLA threshold
- Weekly Monday report generation for pipeline review
- Regulatory screening database update (sanctions list changes)

**Actions:**
- Auto-generate customized document checklist based on entity type and jurisdiction
- Route documents to appropriate review teams as they're received
- Cross-reference client entities against sanctions lists and PEP databases
- Generate daily bottleneck report highlighting longest-waiting items per phase
- Send client-friendly status update emails through RM
- Re-screen existing pipeline clients when sanctions lists are updated

**Data Required:**
- KYC document requirements matrix by entity type and jurisdiction
- Sanctions and PEP screening databases
- Credit policy thresholds and approval matrices
- ISDA negotiation templates and precedent library
- Trading system account creation requirements

**Autonomy Level:** Human-in-the-Loop
Auto-generates checklists, routes documents, sends reminders, and compiles reports. Requires human approval for: compliance determinations, credit decisions, legal document execution, and any client-facing communications.

**Example Interaction:**
> A new onboarding request comes in for a Cayman Islands-domiciled hedge fund. OnboardIQ immediately identifies this as a high-complexity onboarding: offshore jurisdiction requires Enhanced Due Diligence, fund structure requires look-through to beneficial owners, and the derivatives trading intent requires ISDA/CSA negotiation. It generates a customized 47-item document checklist, assigns the KYC collection to a specialist analyst experienced with fund structures, and sets milestone dates working backward from the requested go-live date.
>
> As documents trickle in over the next two weeks, OnboardIQ validates completeness in real-time, immediately flagging that the fund's administrator certificate is expired and the beneficial ownership declaration is missing one layer of the ownership chain. It drafts a specific follow-up request to the client (via the RM) listing exactly what's needed, avoiding the generic "please provide all outstanding documents" that typically generates confusion. The Compliance team gets documents for review the moment they're complete — no batching delay.

---

### Use Case 6: Margin & Collateral Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Margin and collateral management has become exponentially more complex post-2008. Uncleared Margin Rules (UMR) require initial margin posting for bilateral OTC derivatives. Variation margin must be exchanged daily. Each CCP (Central Counterparty) has different margin methodologies and eligible collateral schedules. A mid-size IB manages collateral across 5-15 CCPs and dozens of bilateral CSAs, each with unique terms for eligible collateral, haircuts, thresholds, and dispute resolution. The daily margin call process — receiving calls, agreeing amounts, identifying optimal collateral, instructing transfers, and reconciling — is a highly manual, time-pressured activity. Disputes over margin amounts can tie up hundreds of millions in excess collateral. Teams of 10-30 people manage this process using spreadsheets and legacy systems, with errors potentially causing regulatory breaches or excess capital consumption.

#### The Solution
monday.com provides a collateral management orchestration layer. Each margin relationship (CCP or bilateral) is tracked with daily call status, dispute tracking, and collateral inventory management. Dashboards show real-time collateral utilization, upcoming calls, dispute aging, and optimization opportunities. The system integrates with margin calculation engines to auto-populate expected call amounts and flags discrepancies for investigation. Collateral optimization views help identify the cheapest-to-deliver assets across all obligations.

#### The Outcome
- 95% of margin calls agreed within 1 hour (up from 60%)
- $50-200M reduction in excess collateral posted through optimization
- Zero regulatory breaches for late margin posting
- 50% reduction in margin disputes through proactive reconciliation
- Complete audit trail for UMR and EMIR margin compliance

#### Discovery Questions
1. "How many margin relationships do you manage — both cleared and bilateral — and what's the typical daily volume of margin calls?"
2. "What's your current margin dispute rate, and how long do disputes typically take to resolve?"
3. "Do you have a collateral optimization process, or do you tend to post cash as the path of least resistance?"
4. "How do you track eligibility and haircut schedules across different counterparties and CCPs — is that automated or maintained manually?"
5. "Have you ever had a regulatory concern about late margin posting, and what controls do you have to prevent that?"

#### Industry Context
Collateral management is one of the fastest-growing functions in IB Ops. UMR Phase 6 (2022) brought hundreds of additional buy-side firms into scope, dramatically increasing the volume of bilateral margin calls. Key concepts: Initial Margin (IM) vs. Variation Margin (VM), ISDA SIMM (Standard Initial Margin Model), CSA (Credit Support Annex), eligible collateral schedules, haircuts, thresholds, minimum transfer amounts. The "cheapest to deliver" optimization is critical — posting cash has zero haircut but high opportunity cost; posting government bonds has a small haircut but frees up cash for other uses.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Margin & Collateral Management system. Create a board called 'Daily Margin Calls' with columns: Counterparty/CCP (text), Relationship Type (dropdown: CCP Cleared, Bilateral CSA, Bilateral IM), Call Direction (status: We Owe, They Owe, No Call), Call Amount (numbers, USD), Expected Amount (numbers — from internal calc), Variance (formula: Call Amount - Expected Amount), Variance Threshold (status: Within Tolerance, Investigate, Dispute), Agreement Status (status: Pending, Agreed, Disputed, Partially Agreed), Collateral Type Posted (dropdown: Cash USD, Cash EUR, UST, Bunds, Gilts, Corporate Bonds, Equities), Transfer Status (status: Not Initiated, Instructed, Settled, Failed), Call Date (date), Settlement Deadline (date), Assigned Analyst (people), Dispute Notes (long text). Group by Relationship Type. Add automations: when Variance Threshold is Dispute, auto-create item on Disputes board and notify team lead; when Agreement Status is Pending and Settlement Deadline is within 2 hours, escalate urgently; when Transfer Status changes to Settled, move to Completed group. Create a second board 'Collateral Inventory' with: Asset Type, ISIN, Quantity, Market Value, Haircut %, Collateral Value (formula), Pledged To (text), Available (formula), Eligibility (tags for which CSAs accept it). Create Dashboard combining both boards: total collateral utilization, today's calls status overview, dispute aging chart, collateral composition pie chart, available vs. pledged bar chart."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CollateralIQ — Margin & Collateral Optimization Agent
**Agent Purpose:** Streamline daily margin call processing, optimize collateral allocation, and prevent margin-related regulatory breaches.

**Triggers:**
- Daily margin calls received from CCPs and counterparties (typically 6-8 AM ET)
- Variance between received call and internal calculation exceeds threshold
- Collateral transfer deadline approaching with unsettled instructions
- New CSA or CCP membership onboarded (update eligibility rules)
- End-of-month regulatory reporting deadline for margin compliance

**Actions:**
- Auto-compare received margin calls against internal calculations and flag variances
- Recommend optimal collateral allocation across all obligations (cheapest-to-deliver algorithm)
- Generate collateral transfer instructions for agreed calls
- Create and manage dispute items with supporting calculation details
- Produce daily margin summary report for treasury and risk management
- Alert on upcoming large calls based on market movement predictions

**Data Required:**
- Daily margin call feeds from CCPs and counterparties
- Internal margin calculation engine outputs
- Collateral inventory with real-time market values
- CSA/CCP eligibility schedules and haircut matrices
- Transfer instruction templates by settlement route

**Autonomy Level:** Human-in-the-Loop
Auto-compares calls, recommends collateral allocation, and generates transfer instructions as drafts. Requires human approval for: agreeing margin calls, initiating collateral transfers, and escalating disputes.

**Example Interaction:**
> At 6:30 AM ET, CollateralIQ processes the morning's margin calls: 23 calls from 8 CCPs and 15 bilateral counterparties totaling $1.2B in variation margin. It auto-matches 18 calls within tolerance and prepares agreement confirmations for analyst review. For 5 calls showing variances, it identifies probable causes: 2 are timing differences (counterparty used prior day's prices), 2 are legitimate calculation differences that warrant investigation, and 1 is a clear error where the counterparty appears to have included an expired trade.
>
> For the $1.2B in agreed calls, CollateralIQ runs its optimization algorithm and recommends posting $400M in US Treasuries (freeing up cash), $300M in cash EUR (lowest opportunity cost given current rates), and $500M in cash USD. It generates all transfer instructions and presents them for one-click approval. The analyst reviews, approves, and all instructions are sent within 45 minutes of call receipt — well within the regulatory deadline.

---

### Use Case 7: Operational Risk & Incident Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Operational risk events in IB Ops — trade booking errors, system outages, process failures, unauthorized transactions — must be captured, investigated, and reported per Basel III operational risk requirements. Most banks use heavyweight GRC (Governance, Risk, Compliance) platforms that are complex, slow to update, and underutilized by front-line staff. As a result, incidents are underreported, root cause analyses are superficial, and the same errors recur. Near-misses (events caught before impact) are rarely captured despite being the most valuable learning opportunities. The Ops risk team spends more time chasing incident reports from business lines than actually analyzing risk patterns.

#### The Solution
monday.com provides a lightweight, accessible incident management system that front-line staff actually use. Incident reporting via mobile-friendly Forms takes under 2 minutes. Each incident is automatically categorized, severity-assessed, and routed to the appropriate investigation team. Workflow automations enforce the investigation lifecycle: Report → Triage → Investigate → Root Cause → Remediation → Close. Dashboard analytics reveal patterns — recurring root causes, high-risk processes, temporal trends — enabling proactive risk management rather than reactive incident chasing.

#### The Outcome
- 3x increase in incident and near-miss reporting (better data = better risk management)
- 60% reduction in average investigation closure time
- Identification of systemic risk patterns previously invisible in siloed reports
- Regulatory-ready incident database for Basel III operational risk reporting
- Measurable reduction in recurring incidents through tracked remediation actions

#### Discovery Questions
1. "How do your front-line Ops staff currently report operational incidents — is it a quick process, or does the friction mean many incidents go unreported?"
2. "Can you identify your top 3 recurring operational risk themes, or would that require manual analysis to determine?"
3. "How do you track remediation actions from incident investigations — do you have confidence that agreed fixes are actually implemented?"
4. "When regulators ask about your operational risk framework, how do you demonstrate that it's a living process rather than a compliance checkbox?"
5. "Do you capture near-misses, and if so, how do you use that data to prevent actual incidents?"

#### Industry Context
Basel III requires banks to hold capital against operational risk, calculated using either the Standardized Approach or internal models. Better incident data can actually reduce required capital. The SE should understand the Basel event categories: Internal Fraud, External Fraud, Employment Practices, Clients/Products/Business Practices, Damage to Physical Assets, Business Disruption, Execution/Delivery/Process Management. The last category is most relevant to IB Ops. Key concepts: RCSA (Risk and Control Self-Assessment), KRI (Key Risk Indicator), loss event database, scenario analysis.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Operational Risk & Incident Management system. Create a board called 'Ops Risk Incidents' with columns: Incident ID (auto-number), Incident Title (text), Reported By (people), Report Date (date), Event Category (dropdown: Execution & Delivery, System Failure, Process Breakdown, Data Error, Unauthorized Activity, External Event, Near Miss), Basel Category (dropdown: Internal Fraud, External Fraud, Employment Practices, Clients Products Business Practices, Damage to Physical Assets, Business Disruption, Execution Delivery Process Management), Severity (dropdown: Critical — >$1M impact, High — $100K-$1M, Medium — $10K-$100K, Low — <$10K, Near Miss — No Impact), Financial Impact (numbers, USD), Business Line (dropdown: Equities, Fixed Income, Derivatives, FX, Prime Brokerage, Cross-Business), Investigation Status (status: Reported, Triaged, Under Investigation, Root Cause Identified, Remediation In Progress, Closed, Escalated to Risk Committee), Root Cause (dropdown: Human Error, System Deficiency, Process Gap, Third Party Failure, Market Conditions, Training Gap), Investigator (people), Remediation Owner (people), Target Close Date (date), Lessons Learned (long text). Add a Form for easy incident submission with only essential fields. Add automations: Critical severity auto-notifies Head of Ops Risk and assigns senior investigator; if Investigation Status unchanged for 7 days, escalate; when Remediation In Progress for >30 days, alert remediation owner's manager. Create Dashboard with: incidents by Event Category (bar chart), severity distribution (pie chart), monthly incident trend (line chart), open investigations aging (chart), top root causes (bar chart), financial impact summary (numbers widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RiskLens — Operational Risk Intelligence Agent
**Agent Purpose:** Analyze operational incidents for patterns, predict emerging risks, and ensure thorough investigation and remediation of all events.

**Triggers:**
- New incident reported via Form submission
- Investigation exceeds SLA timeframe
- Pattern detected: 3+ similar incidents within 30 days
- Monthly operational risk report generation
- Regulatory examination preparation (ad-hoc)

**Actions:**
- Auto-triage new incidents: classify severity, assign Basel category, route to investigator
- Detect patterns across incidents using historical data analysis (similar root causes, same process area, same time patterns)
- Generate investigation templates pre-populated with relevant historical precedents
- Compile monthly operational risk report with trend analysis and emerging risk flags
- Track remediation action completion and verify effectiveness (check if similar incidents recur post-fix)
- Prepare regulatory examination packages with complete incident histories and remediation evidence

**Data Required:**
- Historical incident database (mondayDB)
- Process taxonomy and control framework
- Organizational structure for routing and escalation
- Basel III operational risk reporting templates
- Remediation action tracking data

**Autonomy Level:** Escalation-Based
Fully autonomous for classification, routing, pattern detection, and reporting. Escalates to human for: severity determination on ambiguous events, root cause conclusions, and remediation plan approval.

**Example Interaction:**
> A new incident is reported: an analyst accidentally booked a FX forward with the wrong value date, discovered during end-of-day reconciliation. RiskLens auto-classifies it as "Execution & Delivery / Human Error / Medium severity" and estimates financial impact at $23K based on the one-day rate movement. It assigns investigation to the FX Ops team lead.
>
> But RiskLens also flags something the team might miss: this is the 4th value date error in FX forwards this quarter, all occurring on the same trading platform. It creates a pattern alert, links all 4 incidents, and recommends a systemic investigation into the platform's date-picker UX as a possible root cause. The cumulative financial impact of $87K across all 4 events justifies a system enhancement request, which RiskLens drafts and routes to the Technology team for assessment.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| T+1 | Trade date plus one business day — the standard settlement cycle for US securities |
| Break | A discrepancy between two records of the same transaction that must be resolved |
| Affirmation | The process by which an institutional investor confirms trade details to the executing broker |
| Nostro/Vostro | "Our account at your bank" / "Your account at our bank" — used in cash settlement |
| SSI | Standard Settlement Instructions — pre-agreed instructions for where/how to settle |
| ISDA | International Swaps and Derivatives Association — governs OTC derivatives documentation |
| CSA | Credit Support Annex — the collateral agreement under an ISDA Master Agreement |
| CCP | Central Counterparty — the clearinghouse that stands between buyer and seller |
| DTCC | Depository Trust & Clearing Corporation — the primary US clearing and settlement infrastructure |
| UMR | Uncleared Margin Rules — regulations requiring margin exchange for bilateral OTC derivatives |
| SIMM | Standard Initial Margin Model — ISDA's methodology for calculating bilateral initial margin |
| Corporate Action | Any event initiated by a company that affects its securities (dividends, splits, mergers) |
| Scrubbing | The process of cleaning and normalizing corporate action data from multiple sources |
| KYC/AML | Know Your Customer / Anti-Money Laundering — regulatory requirements for client identification |
| UBO | Ultimate Beneficial Owner — the natural person(s) who ultimately own or control a legal entity |
| GRC | Governance, Risk, and Compliance — the framework (and often the software category) for managing operational risk |
| CNS | Continuous Net Settlement — NSCC's system for netting and settling equity transactions |
| FIX | Financial Information eXchange — the standard messaging protocol for trade communication |
| Prime Broker | A bank providing bundled services (clearing, custody, financing) to hedge funds |
| Fail | A settlement that does not complete on the intended settlement date |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Head of Operations / COO | Overall Ops strategy, headcount, budget, regulatory relationships | Decision-maker |
| Head of Settlements | Manages the settlement team, owns fail rates and SLAs | Decision-maker for settlement tools |
| Head of Corporate Actions | Oversees CA processing, elections, entitlement accuracy | Decision-maker for CA workflows |
| Head of Collateral Management | Manages margin calls, collateral optimization, CSA compliance | Decision-maker for margin tools |
| Operational Risk Manager | Owns incident management, RCSA, Basel III OpRisk reporting | Influencer / Decision-maker for risk tools |
| Compliance / KYC Manager | Oversees client onboarding, AML screening, regulatory classification | Influencer |
| Head of Ops Technology | Responsible for Ops systems, integrations, and automation initiatives | Key influencer / Technical decision-maker |
| Front Office COO / Business Manager | Cares about time-to-market, trade support responsiveness | Influencer / Budget holder |
| CFO / Treasurer | Capital efficiency, collateral optimization, operational cost reduction | Executive sponsor |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Technology infrastructure, system integrations, API development for Ops tools | monday.com Dev product for Ops technology projects and change management |
| Risk Management | Market risk feeds into margin calculations, credit risk into client onboarding | Unified risk dashboard combining operational, market, and credit risk views |
| Compliance | KYC/AML screening, regulatory reporting, trade surveillance | Shared compliance workflow platform, cross-referencing Ops data with surveillance |
| Front Office (Trading) | Trade booking accuracy, allocation instructions, client communication | Connected workflows — trade booking triggers Ops processing automatically |
| Finance / Accounting | P&L reconciliation, regulatory capital reporting, cost allocation | Shared data for financial reporting, operational cost tracking |
| Legal | ISDA negotiations, regulatory interpretation, dispute resolution | Legal matter management integrated with onboarding and compliance workflows |
| Client Services | Client inquiries about positions, settlements, corporate actions | Self-service client portal reducing inquiry volume to Ops |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow | Enterprise workflow/ITSM, sometimes extended to Ops workflows | monday.com is faster to deploy, more flexible, better UX — ServiceNow is over-engineered for Ops orchestration |
| Broadridge | Core settlement and post-trade infrastructure | Not a replacement — monday.com orchestrates on top of Broadridge, adding visibility and exception management |
| SmartStream (TLM) | Reconciliation and exception management | monday.com provides broader workflow coverage; can replace TLM for exception tracking while adding project/process management |
| Appian / Pega | Low-code platforms used for Ops automation | monday.com offers faster time-to-value, lower TCO, and AI-native capabilities vs. complex BPM platforms |
| Jira | Sometimes used by Ops teams influenced by technology culture | monday.com is purpose-built for business users, not developers; much better for non-technical Ops staff |
| Excel / SharePoint | The incumbent for most Ops tracking | monday.com replaces the "shadow IT" spreadsheets with governed, auditable, collaborative workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We need purpose-built financial systems, not a general platform" | monday.com isn't replacing your Murex or Calypso — it's the orchestration layer that connects them. Your core systems process transactions; monday.com manages the exceptions, workflows, and human coordination those systems can't handle. Think of it as the connective tissue between your specialized tools. |
| "Regulators require specific systems of record" | monday.com serves as the workflow and tracking layer with full audit trails — your systems of record remain your golden source. The audit trail and governance capabilities in monday.com actually strengthen your regulatory posture by documenting the human decision-making process around exceptions. |
| "Our data is too sensitive for a cloud platform" | monday.com is SOC 2 Type II certified, ISO 27001 compliant, and offers data residency options. Many banks including several G-SIBs use monday.com for operational workflows. The sensitive trade data stays in your core systems — monday.com handles the metadata, status tracking, and workflow orchestration. |
| "We've invested heavily in our existing operations technology" | Those investments handle the 95% of straight-through processing. monday.com addresses the other 5% — the exceptions, escalations, and manual processes that consume 50% of your team's time. It's additive, not replacement, and deploys in weeks rather than the months-to-years your core systems require for changes. |
| "Our IT team needs to approve any new platform" | monday.com's API-first architecture, SSO/SAML support, and enterprise security controls are designed for IT governance requirements. We regularly pass bank technology risk assessments. Let's include your IT team early — they'll appreciate the reduced shadow IT risk vs. the current Excel-based processes. |

## Proof Points
*(To be populated with customer references)*
- [Major bank using monday.com for operational workflow management]
- [Financial services firm consolidating Ops tracking from Excel to monday.com]
- [Investment firm improving settlement SLAs with monday.com orchestration]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
