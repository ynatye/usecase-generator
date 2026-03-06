# Investment Banking × Procurement Playbook

## Overview

Procurement in investment banking operates under intense regulatory scrutiny and fiduciary obligation. Unlike traditional corporate procurement, IB procurement teams source highly specialized services — legal counsel for M&A transactions, financial data terminals (Bloomberg, Refinitiv), research subscriptions, due diligence providers, virtual data room (VDR) platforms, and technology infrastructure for trading floors. The function sits at the intersection of cost management and operational enablement, where a delayed contract can stall a billion-dollar deal.

Investment banks typically structure procurement within a centralized shared-services model, often reporting into the CFO or COO organization. Teams range from 15–60 professionals at bulge-bracket firms (Goldman Sachs, JP Morgan, Morgan Stanley) to 5–15 at middle-market banks (Jefferies, Piper Sandler, Houlihan Lokey). Category managers specialize in verticals: technology, professional services, market data, facilities, and contingent labor. Spend under management can exceed $2–5B annually at top-tier firms.

Regulatory frameworks — including SOX compliance, OCC/FCA vendor risk management guidelines, and third-party risk management (TPRM) requirements from the Fed's SR 13-19 — impose rigorous vendor due diligence, ongoing monitoring, and documentation obligations. Every vendor relationship must be classified by criticality, and concentration risk must be tracked. Procurement here isn't just about savings; it's about institutional risk management.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Vendor onboarding and TPRM documentation consume massive analyst hours — automatable with AI |
| 2 | Consolidate Tech Stack with AI | Medium-High | Banks run fragmented procurement stacks (Ariba, Coupa, Ivalua) alongside spreadsheets and email-driven approvals |
| 3 | Scale Impact Without Overhead | Medium | Growing regulatory requirements demand more vendor oversight without proportional headcount increases |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Third-Party Risk Management (TPRM) Lifecycle

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Regulators (OCC, Fed, FCA) require banks to classify every vendor by risk tier, conduct initial due diligence, and perform ongoing monitoring (annual reviews for critical vendors, biennial for others). At a bulge-bracket firm with 3,000+ active vendors, the TPRM team spends 60–70% of their time chasing questionnaires, reviewing SOC 2 reports, tracking insurance certificates, and updating risk scores. Missed reviews trigger audit findings — and audit findings in banking trigger board-level attention.

#### The Solution
monday.com Work Management as the TPRM command center. Each vendor is an item with structured fields: risk tier (Critical/High/Medium/Low dropdown), review due date, SOC 2 expiry, insurance certificate expiry, data access classification, business continuity plan status, and fourth-party dependency flags. Automations trigger review workflows 90 days before due dates. Dashboards surface overdue reviews, concentration risk by category, and regulatory exam readiness. Forms enable business units to submit new vendor requests with pre-populated risk assessment questions. mondayDB stores historical assessment data for trend analysis.

#### The Outcome
50–60% reduction in TPRM analyst time on administrative tasks. Zero overdue vendor reviews at next regulatory exam. Risk committee gets real-time dashboard instead of quarterly spreadsheet. Audit prep time cut from 3 weeks to 3 days.

#### Discovery Questions
1. "How many active vendor relationships do you manage, and what percentage are classified as critical or high-risk under your TPRM framework?"
2. "When your OCC/Fed examiner asks for a list of all critical vendors with current due diligence status, how long does it take to produce that report?"
3. "What's your current process when a vendor's SOC 2 report expires — is there an automated escalation, or does someone manually track it?"
4. "Have you experienced any audit findings related to third-party risk management in the last two exam cycles?"
5. "How do you currently track fourth-party concentration risk — for example, if multiple critical vendors rely on the same cloud provider?"

#### Industry Context
SR 13-19 (Federal Reserve) and OCC Bulletin 2013-29 establish the regulatory framework for third-party risk management in US banking. The UK's FCA has similar requirements under SS2/21. Critical vendors — those whose failure could disrupt bank operations — require the most rigorous oversight. Fourth-party risk (your vendor's vendors) is an emerging regulatory focus. Examiners specifically look for: risk tiering methodology, due diligence completeness, ongoing monitoring cadence, and board reporting.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Third-Party Risk Management system for an investment bank. Create a board called 'Vendor Risk Registry' with these columns: Vendor Name (text), Risk Tier (dropdown: Critical, High, Medium, Low), Category (dropdown: Technology, Market Data, Professional Services, Facilities, Contingent Labor), Primary Contact (text), Contract Value (numbers, USD), Data Access Classification (dropdown: PII, Material Non-Public Info, Public Only, No Data Access), SOC 2 Status (status: Current, Expiring Soon, Expired, Not Required), SOC 2 Expiry Date (date), Insurance Certificate Expiry (date), Last Review Date (date), Next Review Due (date), Review Status (status: Not Started, In Progress, Under Review, Complete, Overdue), Business Continuity Plan (status: Verified, Pending, Not Submitted), Fourth-Party Dependencies (text), Risk Score (numbers), Assigned Analyst (people), Business Unit Owner (people), Regulatory Classification (dropdown: OCC Critical, OCC Significant, OCC Minimal, FCA Material). Add automations: when Next Review Due is within 90 days and Review Status is Not Started, change Review Status to In Progress and notify Assigned Analyst. When SOC 2 Expiry Date is within 60 days, notify Assigned Analyst and change SOC 2 Status to Expiring Soon. When SOC 2 Expiry Date has passed, change SOC 2 Status to Expired and notify Business Unit Owner. Create a Dashboard view with: widget showing count of vendors by Risk Tier, chart of Review Status distribution, table of all Overdue items, pie chart of vendors by Category, numbers widget showing total contract value under management. Create a Kanban view grouped by Review Status. Add a form called 'New Vendor Request' with fields: Vendor Name, Category, Estimated Contract Value, Data Access Classification, Business Justification (long text), Requesting Business Unit (dropdown: M&A Advisory, Capital Markets, Sales & Trading, Research, Corporate Functions)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** TPRM Sentinel
**Agent Purpose:** Automate vendor risk assessment intake, flag overdue reviews, and generate regulatory-ready risk reports.

**Triggers:**
- New vendor request form submitted
- Review due date within 90 days
- SOC 2 or insurance certificate expiry within 60 days
- Quarterly regulatory reporting schedule
- Manual trigger by TPRM analyst for ad-hoc assessment

**Actions:**
- Auto-classify vendor risk tier based on contract value, data access, and business criticality inputs
- Generate pre-populated due diligence questionnaire based on risk tier
- Send escalation notifications to business unit owners for overdue vendor responses
- Compile quarterly TPRM summary report with vendor counts by risk tier, overdue reviews, and concentration analysis
- Flag fourth-party concentration risks when multiple critical vendors share dependencies
- Update risk scores based on completed assessment data

**Data Required:**
- Vendor contract database (contract values, terms, categories)
- SOC 2 and insurance certificate tracking data
- Organizational hierarchy for escalation routing
- Regulatory classification rules (OCC/FCA thresholds)

**Autonomy Level:** Human-in-the-Loop
Risk tier auto-classification is suggested but requires analyst approval. Escalation notifications and report generation are fully autonomous. Final risk score changes on critical vendors require sign-off.

**Example Interaction:**
> TPRM Sentinel detects that DataVault Corp, a Critical-tier vendor providing virtual data room services for M&A transactions, has a SOC 2 Type II report expiring in 45 days. The agent automatically sends a renewal request to DataVault's compliance contact, creates a review task assigned to Senior Analyst Maria Chen, and flags the item on the Risk Committee dashboard. It also notes that DataVault hosts on AWS — the same infrastructure used by three other Critical vendors — and adds a fourth-party concentration warning to the next quarterly report.
>
> Two weeks later, when DataVault submits their updated SOC 2 report, the agent parses the report summary, updates the expiry date, recalculates the risk score (incorporating zero findings), and notifies Maria that her review task now has all required documentation attached. The entire cycle — which previously took 15+ email exchanges and 3 weeks — completes in 4 days with 2 human touchpoints.

---

### Use Case 2: Deal-Linked Procurement Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every M&A or capital markets transaction requires procurement of deal-specific services: legal advisors (typically $2–10M per deal), financial printers, virtual data rooms, fairness opinion providers, environmental consultants, and sometimes specialized industry experts. These purchases are time-critical — a delayed VDR setup can push back a deal timeline. Yet most banks track deal-linked procurement through email chains between bankers and procurement, leading to duplicate vendor engagements, missed volume discounts across concurrent deals, and zero visibility into deal-related spend until quarter-end.

#### The Solution
monday.com Work Management board linking procurement activities to deal codes. Each deal gets a group; items represent vendor engagements with columns for vendor name, service type, estimated cost, actual cost, engagement status, PO number, and banker requester. Connected boards link to the deal pipeline. Automations route new engagement requests through approval workflows based on spend thresholds ($50K, $250K, $1M). Timeline views show vendor engagement duration against deal milestones. Dashboard aggregates deal-linked spend by category, enabling volume discount negotiations.

#### The Outcome
Full visibility into deal-linked procurement spend (typically 15–25% of total non-comp expenses). 10–15% cost reduction through consolidated vendor negotiations across concurrent deals. Banker satisfaction increases as procurement response time drops from 3–5 days to same-day. Audit trail satisfies SOX requirements for deal expense documentation.

#### Discovery Questions
1. "When a managing director needs a virtual data room set up for a new deal, what's the typical turnaround time from request to access?"
2. "Do you have visibility into how many concurrent deals are using the same legal counsel or VDR provider at any given time?"
3. "How do you currently reconcile deal-specific vendor costs against deal P&L at deal close?"
4. "What's your approval workflow for deal-linked engagements above $250K — is it automated or email-based?"
5. "Have you been able to leverage volume across concurrent deals when negotiating with repeat vendors like financial printers or data room providers?"

#### Industry Context
Deal-linked procurement is unique to investment banking and represents a significant, often poorly managed spend category. Legal fees alone on a mid-market M&A deal run $3–8M. VDR costs (Intralinks, Datasite, Firmex) scale with page count and user seats. Financial printing (Toppan Merrill, Donnelley) is time-critical for SEC filings. Understanding the deal lifecycle (pitch → mandate → execution → close) is essential — procurement needs shift dramatically at each phase.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Deal-Linked Procurement Tracker for an investment bank. Create a board called 'Deal Procurement' with these columns: Deal Code (text), Deal Name (text), Vendor (text), Service Type (dropdown: Legal Counsel, Virtual Data Room, Financial Printer, Fairness Opinion, Environmental Consultant, Industry Expert, Accounting Advisor, Other), Engagement Status (status: Requested, Approved, Engaged, In Progress, Complete, Cancelled), Estimated Cost (numbers, USD), Actual Cost (numbers, USD), Variance (formula), PO Number (text), Requesting Banker (people), Approval Status (status: Pending, Approved, Rejected), Spend Threshold (dropdown: Under $50K, $50K-$250K, $250K-$1M, Over $1M), Engagement Start (date), Engagement End (date), Deal Stage (dropdown: Pitch, Mandate Won, Execution, Closing, Post-Close). Add automations: when Spend Threshold is '$250K-$1M', notify Head of Procurement for approval. When Spend Threshold is 'Over $1M', notify CFO and Head of Procurement. When Engagement Status changes to Complete, prompt for Actual Cost entry. Create a Dashboard with: total deal-linked spend (numbers widget), spend by Service Type (chart), spend by Deal Stage (chart), table of all active engagements sorted by cost descending, vendor frequency analysis. Create a Timeline view showing engagement durations grouped by Deal Code. Add a form called 'Deal Vendor Request' with: Deal Code, Deal Name, Service Type, Estimated Cost, Urgency (dropdown: Standard, Expedited, Emergency), Business Justification (long text), Preferred Vendor (text, optional)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DealSpend Optimizer
**Agent Purpose:** Match deal procurement requests with preferred vendors, identify volume consolidation opportunities, and accelerate approvals.

**Triggers:**
- New Deal Vendor Request form submitted
- Multiple concurrent deals engaging same vendor category
- Deal stage transition (mandate → execution triggers procurement planning)
- Monthly spend aggregation schedule
- Engagement cost exceeds estimate by >15%

**Actions:**
- Recommend preferred vendors based on historical performance, pricing, and current capacity
- Flag volume consolidation opportunities when 3+ concurrent deals need the same service category
- Auto-route approval workflows based on spend thresholds
- Generate deal P&L procurement summary at deal close
- Alert procurement team when engagement costs trend above estimate
- Create vendor engagement checklist based on service type

**Data Required:**
- Deal pipeline data (deal codes, stages, timelines)
- Historical vendor performance and pricing
- Approval hierarchy and spend thresholds
- Active engagement data across all deals

**Autonomy Level:** Escalation-Based
Vendor recommendations and consolidation flags are autonomous. Approval routing follows pre-set rules. Cost overrun alerts escalate to procurement manager. Final vendor selection always requires human decision.

**Example Interaction:**
> A managing director submits an emergency VDR request for Project Atlas, a $2B acquisition. DealSpend Optimizer immediately checks current VDR engagements and finds that Datasite is already provisioned for two other active deals (Project Beacon and Project Crown). The agent recommends Datasite with a note: "Volume discount opportunity — negotiating a 3-deal bundle could save $45K based on Datasite's tiered pricing. Current turnaround for existing clients: 4 hours vs. 24 hours for new setup." It simultaneously routes the $180K engagement for Head of Procurement approval and pre-populates the PO request with standard terms from the last Datasite engagement. The MD has VDR access by end of day.

---

### Use Case 3: Market Data & Terminal License Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Market data is typically the second-largest non-compensation expense for investment banks, running $500M–$2B annually at bulge-bracket firms. Bloomberg Terminal licenses alone cost $24K–$27K per seat per year, and banks manage thousands of seats. Add Refinitiv, FactSet, S&P Capital IQ, PitchBook, Preqin, and dozens of niche data providers — and you have a sprawling, opaque cost base. Seats go unused when employees leave or change roles. License true-ups are negotiated annually with incomplete utilization data. Procurement teams lack real-time visibility into who's using what.

#### The Solution
monday.com as the market data license management hub. Each license is an item with columns for provider, product, seat holder, department, cost per seat, utilization tier (Heavy/Moderate/Light/Inactive), contract renewal date, and budget center. Connected boards link to employee directory data. Automations flag inactive seats (no login in 30+ days), upcoming renewals (90 days out), and budget threshold alerts. Dashboards provide real-time views of total market data spend, cost per desk, utilization rates, and renewal calendar. mondayDB enables historical trend analysis for negotiation preparation.

#### The Outcome
Typically 8–15% reduction in market data spend through seat reclamation and utilization-based negotiations. Full visibility into $500M+ spend category. Renewal negotiations backed by actual utilization data rather than vendor-provided reports. Audit-ready documentation of license allocation.

#### Discovery Questions
1. "How many Bloomberg Terminal and Refinitiv Eikon seats do you currently manage, and what's your process for tracking utilization?"
2. "When a banker or analyst leaves the firm, how quickly is their market data access reclaimed and reallocated?"
3. "During your last Bloomberg enterprise license negotiation, did you have granular utilization data by desk and function to support your position?"
4. "What's your estimated market data spend per revenue-generating headcount, and how does that compare to your target?"
5. "Do you currently have a single view of all market data subscriptions across the firm, or is it managed by category?"

#### Industry Context
Market data procurement is a specialized discipline within banking. Bloomberg's pricing model (enterprise vs. per-seat, with terminal vs. B-PIPE vs. SAPI tiers) requires deep understanding to negotiate effectively. The "Bloomberg tax" is a common complaint — the product is essential but pricing is opaque. Refinitiv (now LSEG) competes aggressively on price. FactSet and S&P Capital IQ serve overlapping but distinct use cases. Understanding which roles genuinely need which data products (a DCF analyst needs different tools than a sales trader) is key to optimization.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Market Data License Management system for an investment bank. Create a board called 'Market Data Licenses' with these columns: Provider (dropdown: Bloomberg, Refinitiv, FactSet, S&P Capital IQ, PitchBook, Preqin, Dealogic, MSCI, Moody's, Other), Product Tier (text), Seat Holder (people), Employee ID (text), Department (dropdown: M&A Advisory, Leveraged Finance, Equity Capital Markets, Debt Capital Markets, Sales & Trading, Research, Risk Management, Corporate Functions), Desk (text), Annual Cost Per Seat (numbers, USD), Utilization Level (status: Heavy, Moderate, Light, Inactive, Vacant), Last Login Date (date), Contract Renewal Date (date), Budget Center (text), License Type (dropdown: Enterprise, Named User, Concurrent). Add automations: when Utilization Level changes to Inactive, notify Procurement Analyst and Department Head. When Contract Renewal Date is within 90 days, create renewal task and notify Category Manager. When Seat Holder is cleared (employee departure), change Utilization Level to Vacant. Create a Dashboard with: total annual market data spend (numbers widget), spend by Provider (pie chart), utilization distribution (chart), count of Inactive and Vacant seats, cost per department (bar chart), renewal timeline (timeline widget). Create a Table view filtered to Inactive seats only for reclamation review."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DataSpend Analyst
**Agent Purpose:** Monitor market data license utilization, identify savings opportunities, and prepare negotiation intelligence for renewals.

**Triggers:**
- Monthly utilization data import
- Seat holder departure notification from HR system
- Contract renewal 120 days out
- Quarterly spend review schedule
- New seat request submitted

**Actions:**
- Analyze utilization patterns and flag seats below threshold for reclamation
- Generate renewal negotiation brief with utilization data, competitive alternatives, and recommended position
- Auto-reallocate vacant seats to pending requests based on priority queue
- Calculate cost-per-user metrics by department for budget reviews
- Identify cross-provider redundancies (e.g., users with both Bloomberg and Refinitiv)
- Produce monthly market data spend report with trend analysis

**Data Required:**
- Login/utilization data from each provider (API or manual import)
- HR employee status feed
- Contract terms and renewal dates
- Department budget allocations
- Historical spend data for trend analysis

**Autonomy Level:** Human-in-the-Loop
Utilization flagging and reporting are autonomous. Seat reclamation recommendations require procurement manager approval. Renewal negotiation briefs are generated automatically but strategy decisions are human-driven.

**Example Interaction:**
> DataSpend Analyst's monthly scan reveals 47 Bloomberg Terminal seats with zero logins in 45+ days across the firm. It cross-references with HR data and finds 12 are former employees whose seats were never reclaimed (annual savings: $312K), 18 are in Research where a recent reorganization shifted analysts to FactSet, and 17 are in Corporate Functions where Bloomberg access may be unnecessary. The agent creates a reclamation review board, assigns each case to the relevant department procurement liaison, and calculates total potential savings of $1.15M annually. It also notes that the Bloomberg enterprise renewal is in 4 months and flags this utilization data as critical negotiation leverage.

---

### Use Case 4: Vendor Onboarding & KYV (Know Your Vendor)

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Onboarding a new vendor at an investment bank takes 4–12 weeks due to mandatory KYV (Know Your Vendor) checks — essentially the vendor equivalent of KYC. Requirements include: beneficial ownership verification, sanctions screening (OFAC, EU, UK), adverse media checks, financial stability assessment, insurance verification, data security questionnaire (often 100+ questions), regulatory license verification, and conflicts of interest review. The process involves procurement, compliance, legal, information security, and the requesting business unit — each with their own review steps. Email-based coordination creates bottlenecks, lost documents, and frustrated bankers who need the vendor yesterday.

#### The Solution
monday.com as the vendor onboarding workflow engine. Each onboarding is an item progressing through status stages: Request Submitted → Compliance Screening → InfoSec Review → Legal Review → Risk Classification → Approved → Active. Subitems track individual checklist items (sanctions check, insurance verification, etc.). File columns store submitted documents. People columns assign reviewers from each function. Automations enforce sequential gating (InfoSec can't start until Compliance clears) and SLA tracking (auto-escalate if any stage exceeds 5 business days). Forms enable standardized intake. Dashboards show pipeline, bottlenecks, and average onboarding time.

#### The Outcome
Onboarding time reduced from 8 weeks average to 3 weeks. Bottleneck visibility enables process improvement (typically Legal review is the chokepoint). 100% documentation compliance — no vendor goes active without all checks complete. Banker satisfaction improves as they can track onboarding progress in real-time.

#### Discovery Questions
1. "What's your average vendor onboarding time from initial request to approved status, and what's the longest it's taken?"
2. "How many functional teams are involved in vendor due diligence, and how do you coordinate handoffs between them?"
3. "Have you ever had a situation where a vendor was engaged before onboarding was complete because the deal timeline couldn't wait?"
4. "What's your current sanctions screening process — is it automated through a tool like World-Check, or manual?"
5. "How do you handle the tension between banker urgency and compliance thoroughness during vendor onboarding?"

#### Industry Context
KYV in investment banking mirrors KYC in rigor. Beneficial ownership must be traced to ultimate beneficial owners (UBOs) — particularly important post-FinCEN's Corporate Transparency Act. Sanctions screening must cover OFAC's SDN list, EU consolidated list, and UK sanctions. Adverse media screening looks for legal actions, regulatory penalties, and reputational risks. The InfoSec review is often the most time-consuming element, especially for technology vendors with data access. Banks that engage vendors before completing KYV face severe regulatory consequences.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Onboarding & KYV Workflow for an investment bank. Create a board called 'Vendor Onboarding Pipeline' with these columns: Vendor Name (text), Requesting Business Unit (dropdown: M&A Advisory, Capital Markets, Sales & Trading, Research, Risk Management, Corporate Functions), Urgency (dropdown: Standard, Expedited, Critical-Deal-Linked), Onboarding Stage (status: Request Submitted, Compliance Screening, InfoSec Review, Legal Review, Risk Classification, Approved, Active, Rejected), Compliance Reviewer (people), InfoSec Reviewer (people), Legal Reviewer (people), Risk Analyst (people), Stage Start Date (date), SLA Deadline (date), Days in Current Stage (formula), Sanctions Check (status: Pending, Clear, Flagged), Adverse Media (status: Pending, Clear, Flagged), Beneficial Ownership (status: Pending, Verified, Escalated), Insurance Verified (status: Pending, Verified, Expired), InfoSec Score (numbers), Overall Risk Rating (dropdown: Critical, High, Medium, Low), Documents Received (files). Add subitems for checklist: OFAC Screening, EU Sanctions Check, UBO Verification, SOC 2 Review, Insurance Certificate, Data Security Questionnaire, Regulatory License Check, Conflicts Review. Add automations: when Onboarding Stage changes to Compliance Screening, assign Compliance Reviewer and set SLA Deadline to 5 business days. When all compliance subitems are complete, move to InfoSec Review. When Days in Current Stage exceeds 5, notify the assigned reviewer's manager. When Onboarding Stage changes to Approved, notify Requesting Business Unit. Create a Dashboard with: average onboarding time (numbers widget), pipeline by stage (funnel chart), SLA compliance rate (chart), bottleneck analysis by stage (bar chart showing average days per stage). Create a Kanban view grouped by Onboarding Stage."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** KYV Fast-Track
**Agent Purpose:** Accelerate vendor onboarding by automating screening steps, chasing outstanding documents, and predicting bottlenecks.

**Triggers:**
- New vendor onboarding request submitted
- Document uploaded to onboarding record
- SLA deadline approaching (2 days remaining)
- Stage idle for 3+ business days
- Vendor flagged in sanctions or adverse media screening

**Actions:**
- Run automated sanctions screening against OFAC/EU/UK lists and update status
- Send document request reminders to vendors with specific missing items listed
- Predict total onboarding time based on vendor category and historical data
- Auto-escalate stalled stages to department managers
- Generate onboarding summary report when all stages complete
- Flag potential conflicts of interest by cross-referencing vendor with active deal parties

**Data Required:**
- Sanctions databases (OFAC SDN, EU, UK) via API
- Vendor submission documents
- Historical onboarding timelines by vendor category
- Active deal party lists for conflicts checking
- Reviewer availability and workload data

**Autonomy Level:** Escalation-Based
Sanctions screening and document reminders are fully autonomous. Flagged items (sanctions hit, adverse media) immediately escalate to compliance with all context. Stage progression requires reviewer sign-off. Conflicts of interest findings escalate to legal.

**Example Interaction:**
> A new VDR vendor request comes in tagged Critical-Deal-Linked. KYV Fast-Track immediately initiates sanctions screening (clear in 2 minutes), sends the data security questionnaire to the vendor's compliance contact, and assigns reviewers from Compliance, InfoSec, and Legal simultaneously (parallel processing for Critical requests, vs. sequential for Standard). It predicts 12 business days to completion based on the Technology vendor category average and notifies the requesting MD with a tracker link. When the vendor's questionnaire response arrives 3 days later, the agent parses key fields, flags that the vendor uses a sub-processor in a restricted jurisdiction, and escalates specifically to InfoSec with the relevant clause highlighted.

---

### Use Case 5: Contract Lifecycle Management for Banking Agreements

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banks maintain thousands of vendor contracts ranging from multi-year Bloomberg enterprise agreements to short-term deal-specific engagements. Contract management is typically fragmented across procurement (commercial terms), legal (legal terms and regulatory clauses), and business units (relationship management). Key risks include: auto-renewal of unfavorable contracts, missed termination windows, non-compliant regulatory clauses (particularly around data residency and audit rights), and inconsistent terms across similar vendor categories. Most banks rely on a mix of contract management tools, shared drives, and institutional memory — which walks out the door with employee turnover.

#### The Solution
monday.com as the centralized contract repository and lifecycle manager. Each contract is an item with columns for vendor, contract type, effective date, expiry date, auto-renewal flag, termination notice period, annual value, key terms summary, regulatory clause compliance status, and document storage. Automations trigger termination window alerts (notice period + 30 days buffer), annual review assignments, and regulatory clause audits. Connected boards link contracts to vendor risk profiles. Dashboards show expiring contracts, total committed spend, auto-renewal exposure, and regulatory compliance status.

#### The Outcome
Zero missed termination windows (typically saving 5–10% of total vendor spend from avoided unwanted auto-renewals). Regulatory clause compliance auditable in real-time. Contract negotiation cycle time reduced 30% through template and historical terms visibility. Single source of truth eliminates the "who has the latest version" problem.

#### Discovery Questions
1. "In the last 12 months, how many vendor contracts auto-renewed that you would have preferred to renegotiate or terminate?"
2. "When a regulator asks about data residency or audit rights clauses across your vendor portfolio, how quickly can you produce that information?"
3. "How do you currently track termination notice periods — is there a system alert, or does someone maintain a spreadsheet?"
4. "What's your process for ensuring new contracts include all required regulatory clauses before execution?"
5. "How do you leverage historical contract terms when negotiating renewals with existing vendors?"

#### Industry Context
Banking contracts require specific regulatory clauses that general CLM tools often don't template for: data residency requirements (critical post-Schrems II for EU data), regulator audit rights (OCC/Fed must be able to examine critical vendors), business continuity and disaster recovery commitments, data breach notification timelines (often stricter than statutory minimums), and subcontractor approval rights. The termination notice window is particularly critical — Bloomberg contracts, for example, have specific cancellation windows, and missing them locks in another year at $24K+ per seat.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Contract Lifecycle Management system for an investment bank. Create a board called 'Vendor Contracts' with these columns: Vendor Name (text), Contract Type (dropdown: Master Services Agreement, Statement of Work, Enterprise License, Subscription, NDA, Data License, Consulting Engagement), Effective Date (date), Expiry Date (date), Auto-Renewal (status: Yes, No), Termination Notice Period (dropdown: 30 Days, 60 Days, 90 Days, 180 Days, 365 Days), Termination Window Opens (date), Annual Value (numbers, USD), Total Contract Value (numbers, USD), Status (status: Draft, Under Review, Active, Expiring Soon, Expired, Terminated), Regulatory Clauses Compliant (status: Yes, Partial, No, Not Reviewed), Data Residency Clause (status: Included, Missing, N/A), Audit Rights Clause (status: Included, Missing, N/A), Business Continuity Clause (status: Included, Missing, N/A), Contract Owner (people), Legal Reviewer (people), Contract Document (files), Key Terms Summary (long text). Add automations: when today equals Termination Window Opens date, notify Contract Owner and Procurement Manager. When Expiry Date is within 120 days, change Status to Expiring Soon and create renewal review task. When Regulatory Clauses Compliant is Partial or No, notify Legal Reviewer. Create a Dashboard with: total annual committed spend (numbers widget), contracts expiring next 90 days (table), auto-renewal exposure (sum of Annual Value where Auto-Renewal is Yes and expiring within 180 days), regulatory compliance status distribution (pie chart), contracts by type (chart). Create a Calendar view showing expiry dates and termination windows."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ContractGuard IB
**Agent Purpose:** Monitor contract lifecycles, ensure regulatory clause compliance, and prevent costly auto-renewals.

**Triggers:**
- Termination window opening (notice period before expiry)
- New contract uploaded for review
- Regulatory clause audit scheduled (quarterly)
- Contract value exceeding budget threshold
- Vendor risk tier change affecting contract terms

**Actions:**
- Scan new contracts for required regulatory clauses and flag missing items
- Generate termination/renewal recommendation based on vendor performance, market alternatives, and utilization data
- Compile renewal negotiation brief with historical terms, market benchmarks, and current utilization
- Auto-generate regulatory compliance report for exam preparation
- Alert when contract terms conflict with updated regulatory requirements
- Track and report on total committed spend vs. budget

**Data Required:**
- Contract documents (for clause scanning)
- Regulatory clause requirements library
- Vendor performance data
- Market benchmark pricing data
- Budget allocation data

**Autonomy Level:** Human-in-the-Loop
Clause scanning and compliance flagging are autonomous. Renewal recommendations are generated but require procurement manager decision. Termination decisions always require human approval. Regulatory reports are auto-generated but reviewed before submission.

**Example Interaction:**
> ContractGuard IB detects that the Refinitiv enterprise data license ($4.2M annually) has a termination window opening in 15 days, with a 180-day notice period required for the contract expiring in 195 days. The agent pulls utilization data showing 23% of Refinitiv Eikon seats are inactive, compiles competitive pricing from recent FactSet and Bloomberg proposals, and generates a renewal brief recommending a 15% seat reduction and 8% rate decrease. It flags that the current contract is missing an updated data residency clause required under the firm's new EU data governance policy. The brief is delivered to the Category Manager for Market Data with a clear recommendation: "Serve termination notice now to create negotiation leverage — you can always rescind if terms are agreed."

---

### Use Case 6: Procurement Request Intake & Approval Workflow

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Procurement requests in investment banking come from dozens of sources — MDs needing deal services urgently, IT requesting software licenses, facilities ordering equipment, and research subscribing to data feeds. Without a standardized intake, requests arrive via email, Slack, phone calls, and hallway conversations. This creates: no audit trail, inconsistent data capture, approval bottlenecks (the CFO's inbox is the approval queue), duplicate requests across divisions, and no spend forecasting capability. The procurement team spends 30% of their time on intake administration rather than strategic sourcing.

#### The Solution
monday.com Forms as the universal procurement intake portal. Conditional logic routes requests by category and spend threshold to appropriate approval chains. Each request becomes a trackable item with full lifecycle visibility: Submitted → Under Review → Approved → PO Issued → Delivered → Invoiced → Closed. Automations enforce approval matrices (category-specific approvers, spend-threshold escalation). Dashboards give leadership real-time visibility into procurement pipeline, cycle times, and spend commitments. Integration with ERP for PO generation.

#### The Outcome
100% of procurement requests captured with standardized data. Approval cycle time reduced from 5–7 days to 1–2 days. Procurement team reallocates 30% of admin time to strategic sourcing. Spend visibility enables proactive budget management. Full audit trail satisfies SOX requirements.

#### Discovery Questions
1. "What percentage of your procurement requests come through a formal system versus email or ad-hoc channels?"
2. "How many approval layers does a typical $100K procurement request go through, and what's the average cycle time?"
3. "Have you experienced situations where different business units independently procured the same or similar services?"
4. "How do you currently forecast upcoming procurement spend for budget planning?"
5. "What's the biggest source of frustration for your internal stakeholders when they need to procure something?"

#### Industry Context
Investment banking procurement approval matrices are typically complex: different thresholds for deal-linked vs. operational spend, different approvers by category (technology vs. professional services vs. market data), and different urgency tracks (standard vs. deal-critical). SOX compliance requires documented approval chains for all material purchases. The culture of MD autonomy ("I need this for my deal, just make it happen") often conflicts with procurement controls — the intake system must balance speed with governance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Procurement Request Intake system for an investment bank. Create a board called 'Procurement Requests' with columns: Request ID (auto-number), Requester (people), Department (dropdown: M&A Advisory, Capital Markets, Sales & Trading, Research, Risk Management, IT, Facilities, Corporate Functions), Category (dropdown: Technology, Professional Services, Market Data, Facilities, Contingent Labor, Deal Services, Other), Description (text), Estimated Spend (numbers, USD), Spend Type (dropdown: One-Time, Recurring Annual, Multi-Year), Urgency (dropdown: Standard, Expedited, Deal-Critical), Status (status: Submitted, Under Review, Approved, Rejected, PO Issued, Delivered, Invoiced, Closed), Approver 1 (people), Approver 1 Decision (status: Pending, Approved, Rejected), Approver 2 (people), Approver 2 Decision (status: Pending, Approved, Rejected), Budget Code (text), PO Number (text), Preferred Vendor (text), Business Justification (long text), Attachments (files). Add automations: when form submitted and Estimated Spend is under $50K, assign Approver 1 as Category Manager. When Estimated Spend is $50K-$500K, assign Approver 1 as Category Manager and Approver 2 as Head of Procurement. When Estimated Spend exceeds $500K, add CFO as Approver 2. When both approvers approve, change Status to Approved. When Urgency is Deal-Critical, notify all approvers immediately. Create a Dashboard with: total pending requests (count), average approval cycle time, spend pipeline by category (chart), requests by status (funnel), monthly spend commitments (bar chart). Add a form called 'New Procurement Request' with all relevant fields and conditional logic for category-specific questions."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProcureBot IB
**Agent Purpose:** Triage incoming procurement requests, suggest vendors, flag duplicates, and accelerate approvals.

**Triggers:**
- New procurement request form submitted
- Request pending approval for >2 business days
- Similar request submitted within 30 days (potential duplicate)
- Monthly spend threshold approaching budget limit
- Quarter-end rush (increased volume period)

**Actions:**
- Auto-categorize requests and route to appropriate approval chain
- Flag potential duplicate requests with links to existing ones
- Suggest preferred vendors based on category, historical spend, and performance ratings
- Send approval reminders with escalation after SLA breach
- Generate weekly procurement pipeline summary for leadership
- Predict monthly spend commitments based on pipeline

**Data Required:**
- Historical procurement requests and outcomes
- Preferred vendor database by category
- Approval matrix rules
- Budget allocation by department
- Vendor performance ratings

**Autonomy Level:** Fully Autonomous for routing and reminders; Human-in-the-Loop for vendor suggestions and duplicate flagging
All approval decisions remain with designated approvers. The agent accelerates the process but never approves spend.

**Example Interaction:**
> Three separate requests arrive within a 2-hour window: the M&A team needs a data analytics consultant for Project Delta, the Capital Markets team needs a data analytics consultant for a market study, and Research needs a data scientist contractor. ProcureBot IB flags all three as potential consolidation candidates, noting that Accenture (preferred vendor for analytics consulting) offered volume pricing in Q3. It creates a consolidated view, notifies the Category Manager for Professional Services, and suggests: "Consider a single SOW with Accenture covering all three engagements — estimated savings of $85K based on their tiered rate card." Meanwhile, it routes each request through the appropriate approval chain so nothing is delayed pending the consolidation decision.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| TPRM | Third-Party Risk Management — framework for assessing and monitoring vendor risk |
| KYV | Know Your Vendor — due diligence process analogous to KYC for vendor onboarding |
| SOC 2 | Service Organization Control Type 2 — audit report on a vendor's security controls |
| SR 13-19 | Federal Reserve guidance on third-party risk management for banking organizations |
| OCC Bulletin 2013-29 | OCC's risk management guidance for third-party relationships |
| VDR | Virtual Data Room — secure platform for sharing deal documents (Intralinks, Datasite) |
| UBO | Ultimate Beneficial Owner — the natural person who ultimately owns or controls a vendor entity |
| OFAC | Office of Foreign Assets Control — administers US sanctions programs |
| SDN List | Specially Designated Nationals list — OFAC's list of sanctioned entities and individuals |
| Auto-Renewal | Contract clause that automatically extends the agreement unless notice is given within a specified window |
| Category Manager | Procurement specialist focused on a specific spend category (technology, professional services, etc.) |
| Spend Under Management | Total vendor spend that procurement actively manages and negotiates |
| Fourth-Party Risk | Risk arising from your vendor's reliance on their own critical vendors |
| B-PIPE | Bloomberg's real-time data feed product (alternative to full Terminal) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Procurement Officer (CPO) | Strategic sourcing, vendor portfolio management, cost optimization | Decision-maker |
| Head of Third-Party Risk | TPRM framework, regulatory compliance, vendor risk oversight | Decision-maker (risk) |
| Category Manager | Manages specific spend categories, negotiates contracts, vendor relationships | Influencer/Decision-maker (within category) |
| Procurement Analyst | Operational processing, data analysis, reporting, vendor onboarding coordination | User |
| Chief Financial Officer (CFO) | Budget approval, cost management, financial controls | Decision-maker (spend approval) |
| Chief Operating Officer (COO) | Operational efficiency, shared services oversight | Influencer |
| Managing Director (Business) | End-user of procured services, deal-linked procurement requester | Influencer (demand driver) |
| Chief Information Security Officer (CISO) | Vendor InfoSec assessment, data security requirements | Decision-maker (security) |
| General Counsel / Legal | Contract review, regulatory clause compliance, vendor disputes | Decision-maker (legal terms) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Technology vendor management, software licensing, infrastructure procurement | Joint tech stack consolidation, shared vendor management for SaaS |
| Legal | Contract review and negotiation, regulatory clause requirements | Integrated CLM workflow, compliance automation |
| Finance | Budget management, invoice processing, spend reporting | End-to-end procure-to-pay visibility |
| Compliance | Vendor sanctions screening, regulatory reporting, TPRM oversight | Unified vendor risk and compliance dashboard |
| Operations | Facilities management, business continuity, vendor performance monitoring | Shared vendor performance management |
| HR | Contingent labor procurement, staffing agency management | Contingent workforce management platform |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SAP Ariba | Enterprise procurement suite, strong in manufacturing/CPG | Over-engineered for banking-specific needs; rigid workflows don't accommodate deal-linked procurement urgency |
| Coupa | Cloud procurement with spend management focus | Good for operational procurement but lacks TPRM depth; doesn't handle banking regulatory requirements natively |
| Ivalua | Flexible procurement platform | Strong but expensive; implementation cycles of 12+ months frustrate fast-moving banking teams |
| ServiceNow VRM | Vendor risk management module | Point solution that doesn't connect commercial and risk workflows; yet another portal for business users |
| OneTrust | Third-party risk and privacy management | Compliance-focused but doesn't handle procurement workflow or commercial terms |
| Spreadsheets + Email | The actual incumbent in most banks | Fragmented, no audit trail, zero automation, institutional knowledge loss with turnover |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Ariba/Coupa for procurement" | "Those are great for PO processing and catalogs. But how are you managing TPRM workflows, deal-linked procurement, and market data licensing? Most banks run those in spreadsheets alongside their procurement suite. monday.com fills that operational gap." |
| "Our compliance team won't approve a new tool for vendor risk" | "monday.com doesn't replace your GRC system — it orchestrates the workflow between compliance, legal, InfoSec, and procurement. The data stays in your systems of record; monday.com manages the process and visibility layer." |
| "We need enterprise-grade security for banking" | "monday.com is SOC 2 Type II certified, supports SSO/SAML, offers data residency options, and serves major financial institutions. We can walk through the security architecture with your CISO." |
| "The procurement team is too small to justify a new tool" | "That's exactly the point — with 15 people managing $2B in spend, you need automation and AI to scale. Every hour your analysts spend chasing SOC 2 reports is an hour not spent on strategic sourcing." |
| "Bankers won't adopt another system" | "The banker-facing surface is a simple intake form — they submit a request and track status. They don't need to learn a new tool. The complexity is on the procurement side, where your team actually wants the structure." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for financial services procurement case studies]
- [Placeholder for TPRM implementation references]
- [Placeholder for market data management references]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
