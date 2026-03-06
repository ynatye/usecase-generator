# Banking × Sales Playbook

## Overview

Sales departments in banking institutions operate fundamentally differently from sales teams in other industries. In banking, "sales" encompasses relationship managers (RMs), business development officers (BDOs), loan officers, treasury management sales specialists, wealth advisors, and branch-based bankers — all selling complex financial products with long sales cycles, heavy regulatory oversight, and fiduciary obligations. The revenue model is relationship-based: a single commercial banking relationship might generate $500K+ annually across deposits, lending, treasury management, and capital markets products.

Banking sales organizations are typically structured by segment — Consumer/Retail (branch-based), Small Business, Middle Market ($10M-$500M revenue), Commercial & Industrial (C&I), Corporate/Large Corporate, and Specialty verticals (Healthcare, Real Estate, Technology, etc.). Each segment has distinct sales motions: retail is volume-driven with short cycles, middle market is relationship-driven with 6-12 month cycles, and corporate is team-based with multi-year strategic relationships. Most banks operate a "universal banker" or "portfolio management" model where RMs own a book of business and are responsible for deepening wallet share across all product lines.

The regulatory overlay on banking sales is substantial. Fair lending laws (ECOA, CRA) govern who can be sold to and how. UDAAP prohibits unfair sales practices. Reg O governs insider lending. Bank Secrecy Act (BSA) requires customer due diligence (CDD) and Know Your Customer (KYC) before onboarding. Compensation structures must comply with the Incentive Compensation Guidance (OCC 2010-27) to avoid encouraging excessive risk-taking — a direct response to the Wells Fargo fake accounts scandal. Sales leaders must balance growth targets with compliance obligations, making pipeline management, activity tracking, and deal governance uniquely complex.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | RMs spend 50-60% of time on non-selling activities (CRM data entry, credit memo prep, compliance documentation) — AI can reclaim selling hours |
| 2 | Consolidate Tech Stack with AI | High | Banks layer Salesforce, nCino, Abrigo, spreadsheets, and core banking queries — RMs toggle between 8+ systems daily |
| 3 | Replace or Radically Augment Headcount | Medium-High | AI can automate portfolio reviews, cross-sell identification, and credit analysis preparation that currently require junior analysts |

## Prioritized Use Cases

---

### Use Case 1: Commercial Banking Pipeline & Deal Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Commercial banking sales pipelines are managed across a patchwork of Salesforce (or a legacy CRM), nCino (loan origination), spreadsheets (call reports, portfolio reviews), email (deal discussions), and the core banking system (existing relationship data). A relationship manager handling a $200M portfolio with 40-60 commercial relationships spends 8-10 hours per week just updating systems and preparing for meetings. Pipeline visibility is poor: the Commercial Banking EVP asks "what's our Q2 pipeline?" and gets three different numbers from three different sources. Deal stages are inconsistent — one RM's "verbal commitment" is another's "preliminary interest." Critical information (pricing discussions, credit conditions, competitive threats) lives in RM notebooks and email threads, creating massive institutional risk when an RM leaves (taking $50-100M in relationships).

#### The Solution
monday.com CRM configured for commercial banking deal flow. A Commercial Pipeline board with columns: Opportunity Name (text), Company (text), Industry Vertical (dropdown: Healthcare, Real Estate, Manufacturing, Technology, Professional Services, Retail, Energy, Transportation), Relationship Manager (people), Deal Stage (status: Prospect → Initial Meeting → Needs Assessment → Proposal/Term Sheet → Credit Review → Credit Approval → Documentation → Closing → Booked — color-coded by probability), Product Mix (tags: C&I Lending, CRE Lending, Treasury Management, Deposits, Capital Markets, Interest Rate Derivatives, Trade Finance), Estimated Revenue (numbers with $), Loan Amount (numbers with $), Expected Close Date (date), Competitive Threat (dropdown: JPMorgan, BofA, Wells Fargo, Regional Competitor, Credit Union, Non-Bank Lender, None), Last Contact Date (date), Days Since Contact (formula), Next Action (text), Credit Risk Rating (dropdown following bank's internal scale). Dashboard provides segment-level pipeline views, weighted forecast, and RM activity metrics.

#### The Outcome
Single source of truth for the commercial pipeline — one number, not three. 30% reduction in RM administrative time. Institutional knowledge preserved in the system, not in RM heads. Weighted pipeline accuracy improved from ±40% to ±15%.

#### Discovery Questions
1. "When your Commercial Banking EVP asks for the Q2 pipeline forecast, how many systems does your team pull from, and how long does it take to get a confident number?"
2. "What happens to client relationships and pipeline data when a relationship manager leaves or retires?"
3. "How do your RMs currently track competitive intelligence on deals — who else is bidding, what terms are being offered?"
4. "What percentage of your RMs' time is spent on selling activities versus administrative tasks like CRM updates, call reports, and credit memo preparation?"
5. "How consistent are your deal stages across RMs — does 'verbal commitment' mean the same thing to everyone?"

#### Industry Context
Commercial banking deals are complex multi-product relationships. A single middle market client might have a $20M revolving credit facility, $5M in operating deposits, treasury management services (ACH, wire, lockbox, positive pay), an interest rate swap, and a corporate credit card program. Revenue is measured in "relationship profitability" — the sum of net interest income (spread on loans and deposits), fee income (treasury management, capital markets), and ancillary revenue. The credit approval process is a distinct workflow: RMs prepare credit memorandums that go through credit analysts, senior credit officers, and potentially a loan committee. Deal "closing" in banking means completing loan documentation (often 100+ pages prepared by legal), perfecting collateral, and booking the relationship on the core system.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Commercial Banking Pipeline board using monday.com CRM. Columns: Opportunity Name (text), Company Name (text), Industry Vertical (dropdown: Healthcare, Commercial Real Estate, Manufacturing, Technology, Professional Services, Retail & Consumer, Energy & Utilities, Transportation & Logistics, Agriculture, Government/Municipal), Relationship Manager (people), Team Lead (people), Deal Stage (status with labels: Prospect/Initial Meeting/Needs Assessment/Proposal-Term Sheet/Credit Review/Credit Approval/Documentation/Closing/Booked/Lost — color code green for Booked, red for Lost, yellow for Credit Review, blue for Proposal), Product Mix (tags: C&I Revolving Credit, C&I Term Loan, CRE Mortgage, CRE Construction, Treasury Management, Operating Deposits, Interest Rate Swap, Letters of Credit, SBA Lending, Equipment Finance), Total Loan Amount (numbers with $ prefix), Estimated Annual Revenue (numbers with $ prefix), Deposit Opportunity (numbers with $ prefix), Expected Close Date (date), Probability % (numbers), Weighted Revenue (formula: Annual Revenue × Probability), Competitive Threat (dropdown: JPMorgan Chase, Bank of America, Wells Fargo, US Bank, PNC, Truist, Regional Bank, Credit Union, Non-Bank Lender, Private Credit, None Identified), Last Contact Date (date), Days Since Contact (formula: TODAY minus Last Contact Date), Next Action (text), Next Action Date (date), Source (dropdown: Existing Client Expansion, Referral, COI-CPA/Attorney, Event, Cold Outreach, RFP, Inbound), Credit Risk Rating (dropdown: 1-Pass, 2-Pass, 3-Special Mention, 4-Substandard, 5-Doubtful). Group by Deal Stage. Create views: Kanban by Deal Stage showing Weighted Revenue, My Pipeline filtered by current user, Timeline view by Expected Close Date, Dashboard with total pipeline value, weighted forecast, deals by stage funnel chart, pipeline by industry vertical, RM leaderboard by weighted revenue, aging deals (>90 days no contact) list, and expected closings this month."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Deal Intelligence Agent
**Agent Purpose:** Proactively monitors the commercial banking pipeline, identifies at-risk deals, suggests next best actions, and generates relationship intelligence for RMs.

**Triggers:**
- Daily morning scan of all active pipeline deals
- When Days Since Contact exceeds 14 for any active deal
- When Expected Close Date passes without stage advancing to Closing/Booked
- When a new deal is created (to enrich with available data)
- Weekly scheduled pipeline health report

**Actions:**
- Identifies stale deals (no activity in 14+ days) and generates specific re-engagement recommendations
- Analyzes deal patterns to predict close probability more accurately than RM self-reporting
- When a new company is added, enriches with publicly available data (industry, revenue estimate, recent news)
- Generates weekly "RM Action List" — prioritized list of deals needing attention with specific recommended actions
- Flags deals where Expected Close Date has been pushed more than twice (potential zombie deals)
- Creates competitive intelligence summaries when a known competitor is identified on a deal

**Data Required:**
- Commercial Pipeline board with full deal history
- Historical win/loss data for pattern analysis
- Company enrichment data sources
- RM activity logs (meetings, calls, emails)
- Credit approval workflow data

**Autonomy Level:** Human-in-the-Loop
All analysis and recommendations are generated automatically. RM Action Lists are delivered but not enforced. Deal risk flags are visible to RMs and their managers. The agent never contacts clients or modifies deal stages — it advises the RM.

**Example Interaction:**
> Monday morning, the Deal Intelligence Agent delivers RM Sarah Chen's weekly action list: "📋 **Priority Actions This Week:** (1) 🔴 **Meridian Manufacturing — $15M C&I Revolver** — Last contact 23 days ago, currently in Proposal stage. Meridian's fiscal year ends March 31 — they'll need financing committed before then. Competitor: PNC submitted a term sheet last week (source: COI referral note from Feb 3). **Action: Call CFO Tom Rodriguez this week with revised pricing.** (2) 🟡 **Apex Healthcare Group — $8M CRE** — Credit Review stage for 18 days (avg cycle: 10 days). Credit analyst flagged questions on environmental Phase I for the medical office building. **Action: Follow up with credit analyst Maria Lopez on Phase I status; client may need to commission Phase II.** (3) 🟢 **Bright Logistics — $3M Treasury Management** — Needs Assessment complete. They're currently with Wells Fargo treasury. Their AP volume (2,400 checks/month) is ideal for our Integrated Payables solution. **Action: Schedule treasury management specialist demo this week; estimated fee income $48K annually.**"

---

### Use Case 2: Relationship Manager Activity & Call Reporting

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Regulators and auditors expect banks to maintain records of customer interactions — especially for commercial lending relationships. "Call reports" (documentation of client meetings and conversations) are a compliance requirement, not just a sales management tool. Yet most RMs despise call reporting: it takes 15-20 minutes per interaction to document in the CRM, and RMs average 8-12 client touchpoints per week. That's 2-4 hours of pure documentation. Many RMs fall behind, batch-entering call reports before month-end reviews, producing lower-quality records. Sales managers can't coach effectively because they lack visibility into RM activity patterns. When examiners request evidence of ongoing client monitoring (a BSA/AML requirement for commercial relationships), incomplete call reports create regulatory risk.

#### The Solution
monday.com Work Management with a streamlined Activity Tracking board. Columns: RM (people), Client Company (connect to Pipeline board), Contact Name (text), Activity Type (dropdown: In-Person Meeting, Phone Call, Video Call, Email, Event/Conference, Site Visit, Credit Review Meeting, Annual Review), Date (date), Duration (numbers in minutes), Summary (long text), Next Steps (text), Follow-Up Date (date), Products Discussed (tags matching product lines), Cross-Sell Opportunity Identified (checkbox), Compliance Flags (tags: KYC Update Needed, Financial Statements Due, Covenant Compliance Check, Site Visit Required). Quick-entry form for mobile RMs. AI Sidekick can generate call report summaries from brief bullet points. Dashboard shows activity metrics per RM, activity trends, and compliance coverage.

#### The Outcome
Call report completion time reduced from 15-20 minutes to 3-5 minutes with AI-assisted drafting. 95%+ call report compliance (up from ~60%). Sales managers gain real-time coaching visibility. Examiner requests for client monitoring evidence fulfilled in hours.

#### Discovery Questions
1. "What's your current call report completion rate, and how much time do your RMs spend on documentation versus selling?"
2. "When a regulator asks for evidence of ongoing client monitoring for a specific relationship, how quickly can you produce it?"
3. "How do your sales managers currently assess RM activity levels and coaching opportunities?"
4. "Have your RMs ever lost a deal because they forgot to follow up — and how would you even know if they did?"
5. "Do your RMs document interactions on the go, or do they batch-enter at the end of the week/month?"

#### Industry Context
"Call reports" in banking have regulatory significance beyond sales management. BSA/AML regulations require "ongoing customer due diligence" — banks must monitor commercial relationships for changes in business activity, ownership, or risk profile. Call reports serve as evidence of this monitoring. During safety and soundness examinations, examiners review call reports for the bank's largest commercial relationships to assess credit risk management practices. The OCC's Comptroller's Handbook on Commercial Lending specifically references relationship manager documentation as an element of sound credit risk management. Additionally, the Incentive Compensation Guidance requires banks to monitor sales activities for potential misconduct — call report data is one input to that monitoring.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an RM Activity & Call Report board for a commercial banking sales team. Columns: Activity ID (auto-number ACT-), Relationship Manager (people), Client Company (connect to Commercial Pipeline board), Contact Name (text), Contact Title (text), Activity Type (dropdown: In-Person Meeting, Phone Call, Video Conference, Email Exchange, Lunch/Dinner, Conference/Event, Site Visit, Credit Review Meeting, Annual Relationship Review, Prospect Cold Call), Activity Date (date), Duration Minutes (numbers), Meeting Summary (long text), Key Discussion Points (long text), Next Steps (text), Follow-Up Date (date), Products Discussed (tags: C&I Lending, CRE Lending, Treasury Management, Deposits, Wealth Referral, Insurance Referral, Capital Markets, SBA), Cross-Sell Opportunity (checkbox), Estimated Cross-Sell Revenue (numbers with $ prefix), Compliance Flags (tags: KYC Update Needed, Financial Statements Past Due, Covenant Check Required, Site Visit Overdue, Ownership Change Noted, Business Activity Change), Competitive Intelligence (long text). Create a quick-entry form with only: Client Company, Contact Name, Activity Type, Summary, Next Steps, Follow-Up Date, Products Discussed. Group by Relationship Manager. Create views: Calendar view by Activity Date, My Activities filtered by current user, Dashboard with activities per RM per week bar chart, activity type distribution, cross-sell opportunities identified this month, compliance flags requiring attention, follow-ups due this week, and RM activity trend over 12 weeks. Add automations: when Follow-Up Date is today notify RM; when Follow-Up Date is 3 days overdue notify RM and their manager; when Compliance Flag includes KYC Update Needed create item on Compliance board; weekly automation every Friday — if RM has fewer than 6 activities this week notify sales manager."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Call Report Copilot Agent
**Agent Purpose:** Helps RMs create comprehensive call reports from minimal input and ensures compliance documentation standards are met.

**Triggers:**
- When an RM creates a new activity item with a brief summary
- When Follow-Up Date arrives (reminder with context)
- Weekly scheduled compliance coverage check
- When meeting summary is less than 50 words (likely incomplete)

**Actions:**
- Expands brief RM notes into professional call report format (e.g., "Met with Tom, discussed line renewal, competitors offering 50bps less" → full structured summary)
- Auto-suggests Products Discussed tags based on meeting content
- Identifies compliance flags from meeting notes (e.g., mentions of ownership change → KYC Update Needed)
- Generates follow-up reminders with context from the last interaction
- Creates weekly "Coverage Gap Report" identifying clients who haven't been contacted in 30+ days
- Flags potential cross-sell opportunities based on discussion topics and product gaps

**Data Required:**
- Activity & Call Report board
- Commercial Pipeline board (for relationship context)
- Client product inventory (existing products per relationship)
- Historical call reports for relationship context continuity

**Autonomy Level:** Human-in-the-Loop
Drafts call reports for RM review and editing — never submits without RM confirmation. Auto-suggests tags and flags but RM must confirm. Compliance flag identification is automatic but human-verified. Follow-up reminders are automatic.

**Example Interaction:**
> RM Mike Torres returns from a lunch meeting and quickly enters: "Lunch with Jennifer Walsh CFO at Westfield Properties. Discussed CRE portfolio — they're acquiring 3 retail centers in Q2, need $45M construction financing. Current lender (Wells) is slow on approvals. Also mentioned looking at cash management for property management operations. Annual financials coming next week." The Call Report Copilot Agent expands this into a full call report: "**Meeting Summary:** Met with Jennifer Walsh, CFO of Westfield Properties LLC, for a relationship development lunch. **Key Discussion Points:** (1) Westfield is executing an expansion strategy with planned acquisition of three retail shopping centers in Q2 2026, requiring approximately $45M in construction/permanent financing. Current lender (Wells Fargo) has been slow on credit approvals, creating an opening for our bank. (2) Westfield manages 12 properties totaling ~1.2M sq ft and expressed interest in evaluating cash management solutions for their property management operations, including tenant payment processing and vendor disbursements. (3) Annual audited financial statements expected next week — Jennifer will send directly. **Products Discussed:** CRE Construction Lending, Treasury Management, Operating Deposits. **Cross-Sell Opportunity:** ✅ Yes — Treasury Management for property management operations (est. $65K annual fee income). **Compliance Flags:** Financial Statements Due (expecting delivery next week). **Recommended Next Steps:** (1) Request financials upon receipt, (2) Introduce Treasury Management specialist for property management demo, (3) Prepare preliminary term sheet for $45M construction facility." Mike reviews, makes minor edits, and saves in 2 minutes.

---

### Use Case 3: Treasury Management Sales Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Treasury management (TM) is one of the highest-margin, stickiest products in commercial banking — a company using your bank for cash management, payments, and liquidity solutions rarely switches. Yet TM sales are notoriously difficult to manage. The sales cycle is long (3-9 months), requires deep technical discovery (understanding the client's entire cash flow ecosystem), involves complex pricing (hundreds of individual service fees), and demands coordination between the TM sales specialist, the RM, implementation team, and product. TM pipelines are typically tracked in spreadsheets because CRM systems can't handle the product complexity. Implementation backlogs cause client frustration — a TM sale can take 3-6 months to fully implement after closing. Revenue recognition is delayed and unpredictable.

#### The Solution
monday.com CRM with a dedicated Treasury Management Pipeline board. Columns: Company (text), Relationship Manager (people), TM Specialist (people), Deal Stage (status: Discovery → Needs Analysis → Proposal → Pricing Approval → Contract → Implementation → Live — distinct from lending pipeline stages), Services Proposed (tags: Operating Account, Lockbox, ACH Origination, Wire Transfer, Positive Pay, Account Reconciliation, Integrated Payables, Commercial Card, Sweep/Investment, Merchant Services, FX, Liquidity Management), Monthly Transaction Volume (numbers), Estimated Monthly Fee Revenue (numbers with $), Annual Revenue (formula), Implementation Complexity (dropdown: Standard/Complex/Custom), Expected Go-Live Date (date), Competitive Incumbent (dropdown), Current Pain Points (long text), Proposal Document (file). Connected to an Implementation Tracking board for post-sale handoff. Dashboard shows TM pipeline by stage, estimated revenue, and implementation backlog.

#### The Outcome
Complete TM pipeline visibility for the first time (out of spreadsheets). RM-to-TM specialist coordination streamlined. Implementation backlog managed proactively — go-live dates tracked and communicated. 20% increase in TM cross-sell from better pipeline management and RM visibility into TM opportunities.

#### Discovery Questions
1. "How does your treasury management sales team currently track their pipeline — is it in your CRM, spreadsheets, or something else?"
2. "What's your average cycle time from TM discovery to go-live, and where are the biggest bottlenecks?"
3. "How well do your relationship managers and TM specialists coordinate on cross-sell opportunities?"
4. "What's your TM implementation backlog look like, and how does it affect client satisfaction and revenue realization?"
5. "How do you currently price TM proposals — is it standardized or does every deal require custom pricing approval?"

#### Industry Context
Treasury management (also called "cash management" or "transaction banking") is a critical fee income driver for commercial banks. Key products include: Lockbox (payment collection processing), ACH Origination (batch electronic payments), Positive Pay (check fraud prevention), Account Reconciliation (automated bank statement matching), Integrated Payables (consolidated AP processing), Commercial Card (purchasing/travel cards), Sweep Accounts (automated investment of idle balances), and Wire Transfers. TM relationships are measured by "analyzed fees" — a complex fee structure where clients earn an "earnings credit rate" (ECR) on deposit balances that offsets service charges. TM retention rates exceed 95% because switching costs are enormous (re-configuring all payment and collection systems).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Treasury Management Sales Pipeline board for a commercial bank. Columns: Company Name (text), Primary Contact (text), Contact Title (text), Relationship Manager (people), TM Sales Specialist (people), Deal Stage (status: Initial Discovery/Needs Analysis/Solution Design/Proposal Delivered/Pricing Approval/Contract Execution/Implementation/Live/Lost — green for Live, red for Lost, yellow for Pricing Approval, blue for Implementation), TM Services Proposed (tags: Operating Accounts, Lockbox-Retail, Lockbox-Wholesale, ACH Origination, ACH Collection, Wire Transfer-Domestic, Wire Transfer-International, Positive Pay, Account Reconciliation, Integrated Payables, Commercial Card-Purchasing, Commercial Card-Travel, Sweep-Money Market, Sweep-Repo, Zero Balance Accounts, Controlled Disbursement, Merchant Services, FX, Liquidity Management Portal), Company Annual Revenue (numbers with $ prefix), Monthly Transaction Volumes (numbers), Current Bank (dropdown: JPMorgan Treasury Services, BofA Global Transaction Services, Wells Fargo Treasury, Citi Treasury and Trade, US Bank Global Fund Services, PNC Treasury Management, Regional Bank, Multiple Banks), Current Pain Points (long text), Proposed Monthly Fees (numbers with $ prefix), Proposed ECR Offset (numbers with $ prefix), Net Monthly Revenue (formula: Fees minus ECR), Annual TM Revenue (formula: Net Monthly × 12), Implementation Complexity (status: Standard 30 days/Complex 60 days/Custom 90+ days — green/yellow/red), Expected Close Date (date), Expected Go-Live Date (date), Proposal Document (file), Notes (long text). Group by Deal Stage. Create views: Kanban by Deal Stage with Annual Revenue shown, My Deals filtered by TM Specialist, Implementation Queue filtered to Implementation stage sorted by Go-Live Date, Dashboard with total pipeline value, weighted forecast, pipeline by TM service type, deals by implementation complexity, monthly revenue run-rate chart, and top 10 deals list."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Treasury Management Cross-Sell Identifier Agent
**Agent Purpose:** Analyzes existing commercial banking relationships to identify treasury management cross-sell opportunities and generates qualified leads for TM specialists.

**Triggers:**
- Weekly scheduled scan of commercial relationship portfolio
- When a new commercial loan is booked (new relationship = TM opportunity)
- When a client's deposit balances change significantly (>20% increase suggests cash flow growth)
- When RM call reports mention cash management, payments, or treasury topics

**Actions:**
- Analyzes each commercial client's product inventory and identifies missing TM products
- Scores opportunities based on company size, industry, transaction volume potential, and existing wallet share
- Generates "TM Opportunity Cards" with recommended products, estimated revenue, and suggested discovery questions
- Routes opportunities to the appropriate TM specialist based on territory/segment
- Tracks conversion of identified opportunities through the TM pipeline
- Generates quarterly "TM Wallet Share Analysis" showing penetration rates by segment

**Data Required:**
- Commercial Pipeline/Relationship board (all client relationships)
- Client product inventory (existing TM services per client)
- Transaction volume data (ACH, wire, check volumes where available)
- Industry benchmarks for TM product usage by company size/industry
- Call Report board (for topic-based trigger)

**Autonomy Level:** Fully Autonomous for identification; Human-in-the-Loop for outreach
Automatically identifies and scores opportunities, creates opportunity cards, and routes to TM specialists. TM specialist decides whether and how to pursue. The agent never contacts clients directly.

**Example Interaction:**
> The TM Cross-Sell Agent runs its weekly scan and identifies 8 new opportunities. Top opportunity: "🎯 **High-Priority TM Opportunity — Cascade Construction Group** (Existing C&I client, $12M revolving facility, booked 14 months ago). Current TM products: Operating Account only. **Missing high-value products:** (1) **Positive Pay** — Construction companies are #1 target for check fraud. Cascade writes ~200 checks/month to subcontractors. Estimated fee: $350/month. (2) **ACH Origination** — Cascade has 85 employees paid via check. ACH payroll saves them $2/check in processing costs. Estimated fee: $200/month. (3) **Integrated Payables** — Subcontractor payments could be converted from check to virtual card, generating rebate revenue. Estimated: $800/month in interchange. **Total estimated new TM revenue: $16,200/year.** Suggested approach: RM Jake Williams has an annual review scheduled next week — add TM specialist to the meeting. Discovery question: 'How are you managing subcontractor payments today, and have you experienced any check fraud incidents?'" The TM specialist reviews and confirms she'll join the annual review.

---

### Use Case 4: Loan Pipeline & Credit Workflow Coordination

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The loan origination process in banking involves multiple handoffs: RM sources the deal → credit analyst underwrites → senior credit officer reviews → loan committee approves (for larger deals) → documentation team prepares closing docs → operations books the loan. Each handoff is a potential bottleneck and communication breakdown. RMs lose visibility once a deal enters the "credit black hole" — they don't know where their deal is in the approval process and can't give clients timely updates. Credit analysts are overwhelmed with 15-20 active credit memos at once, with no clear prioritization. Deals that sit in documentation for weeks after approval lose client goodwill and sometimes lose to faster competitors. Most banks use nCino or a legacy loan origination system (LOS) for the formal credit process, but the coordination layer around it is spreadsheets and email.

#### The Solution
monday.com Work Management as the coordination and visibility layer that wraps around the bank's existing LOS (nCino, Abrigo, etc.). A Loan Pipeline Tracker board with columns: Borrower (text), RM (people), Credit Analyst (people), Loan Type (dropdown: C&I Revolving, C&I Term, CRE Permanent, CRE Construction, SBA 7(a), SBA 504, Equipment Finance, Line of Credit), Loan Amount (numbers with $), Workflow Stage (status: RM Submitted → Credit Analysis → Senior Review → Loan Committee → Approved → Documentation → Closing → Booked), Days in Current Stage (formula), SLA Target Days (numbers), SLA Status (formula: On Track/Warning/Overdue), Expected Close Date (date), Client Commitment Date (date), Priority (dropdown: Standard/Expedited/Rush), Blockers (text), Documentation Checklist (sub-items). Dashboard provides real-time funnel visualization, SLA tracking, and bottleneck identification. Automations alert when SLA thresholds are breached.

#### The Outcome
End-to-end loan pipeline visibility for the first time. Average approval cycle time reduced 25% through bottleneck identification and SLA enforcement. Client communication improved — RMs always know deal status. Documentation backlog reduced through proactive tracking.

#### Discovery Questions
1. "Once your RM submits a credit request, how much visibility do they have into where it is in the approval process?"
2. "What's your average cycle time from credit submission to loan booking, and how much variance is there?"
3. "How do you prioritize the credit analyst queue — is it first-in-first-out, or do higher-priority deals get expedited?"
4. "How often do you lose deals to competitors because your internal approval process was too slow?"
5. "Do you have SLA targets for each stage of the credit process, and can you measure whether you're meeting them?"

#### Industry Context
Loan origination is the most process-heavy workflow in banking sales. A typical commercial loan requires: financial statement spreading (analyzing 3+ years of financials), cash flow analysis, collateral valuation, environmental due diligence (for real estate), covenant structuring, risk rating assignment, and regulatory reporting classification (Call Code, CRA designation). Larger deals ($5M+) typically require loan committee approval — a formal presentation by the credit analyst to senior management. Documentation is prepared by in-house or external counsel and can include dozens of agreements (credit agreement, security agreement, guaranty, mortgage, UCC filings, etc.). Banks increasingly use nCino (built on Salesforce) as their LOS, but nCino focuses on the formal credit process — not the sales-side coordination and communication that surrounds it.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Loan Pipeline Coordination board for a commercial banking sales team. Columns: Borrower Name (text), Loan Type (dropdown: C&I Revolving Credit, C&I Term Loan, Commercial Real Estate-Permanent, CRE-Construction, SBA 7a, SBA 504, Equipment Finance, Agricultural, Line of Credit-Unsecured), Loan Amount (numbers with $ prefix), Relationship Manager (people), Credit Analyst (people), Documentation Specialist (people), Workflow Stage (status: RM Submission/Credit Analysis/Senior Credit Review/Loan Committee/Approved-Pending Docs/Documentation Prep/Closing Scheduled/Booked/Declined/Withdrawn — green for Booked, red for Declined, grey for Withdrawn), Stage Entry Date (date), Days in Current Stage (formula: TODAY minus Stage Entry Date), SLA Target Days per Stage (numbers — default: Credit Analysis 7, Senior Review 3, Committee 5, Documentation 10), SLA Status (status: On Track/Warning/Overdue based on Days vs SLA), Client Commitment Date (date), Priority (status: Standard/Expedited/Rush — blue/yellow/red), Risk Rating (dropdown: 1 through 8), Collateral Type (dropdown: Real Estate, Equipment, Accounts Receivable, Inventory, Mixed, Unsecured), Blockers (text), Required Documents Checklist (sub-items: Financial Statements, Tax Returns, Personal Financial Statement, Business Plan, Appraisal, Environmental Phase I, Title Search, Insurance, Entity Documents, UCC Search — each with Received checkbox and Date Received), Notes (long text). Group by Workflow Stage. Create views: Kanban by Workflow Stage, My Deals filtered by RM, Credit Analyst Queue filtered by Credit Analyst, Documentation Queue filtered to Approved-Pending Docs and Documentation Prep stages, Dashboard with pipeline funnel chart, average days by stage, SLA compliance rate, overdue items requiring attention, pipeline by loan type, and weekly booking trend. Automations: when Days in Current Stage exceeds SLA Target change SLA Status to Overdue and notify assigned person; when Stage changes update Stage Entry Date to today; when all Required Documents sub-items are checked and Stage is RM Submission auto-advance to Credit Analysis; when Priority is Rush notify Credit Analyst and Senior Credit Officer immediately."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Loan Pipeline Accelerator Agent
**Agent Purpose:** Monitors the loan pipeline for bottlenecks, predicts delays, and orchestrates communication to keep deals moving through the credit process.

**Triggers:**
- Hourly SLA monitoring check during business hours
- When a deal enters a new stage (to set expectations)
- When Days in Current Stage exceeds 75% of SLA target (early warning)
- When a Blocker is added to any deal
- Daily morning pipeline summary generation

**Actions:**
- Generates daily "Pipeline Pulse" for the Chief Credit Officer — deals in queue, SLA compliance, aging items
- When SLA is at 75%, sends early warning to the assigned team member with remaining time
- Identifies patterns in bottlenecks (e.g., "Documentation stage averaging 15 days vs. 10-day SLA — capacity issue?")
- When a blocker is logged, suggests resolution steps and escalation paths
- Generates client-facing status updates for RMs to send (templated, professional communication)
- Tracks deal velocity trends over time and identifies systemic process improvements

**Data Required:**
- Loan Pipeline Coordination board
- Historical loan processing data (for benchmarking and prediction)
- Team capacity data (analyst caseloads)
- Calendar integration (loan committee meeting dates)

**Autonomy Level:** Escalation-Based
SLA monitoring and early warnings are fully automatic. Pipeline Pulse reports generated without approval. Escalation notifications sent to managers when SLA is breached. Client communication templates are generated but RM must send. Process improvement recommendations require management review.

**Example Interaction:**
> At 8:00 AM, the Loan Pipeline Accelerator delivers the daily Pipeline Pulse to Chief Credit Officer Karen Mitchell: "📊 **Pipeline Pulse — Feb 19, 2026.** Active deals: 47 ($312M). **SLA Status:** 38 On Track (81%), 6 Warning (13%), 3 Overdue (6%). **⚠️ Overdue items:** (1) Baxter Industries $8M C&I Term — Credit Analysis stage, Day 11 of 7-day SLA. Analyst: David Park (currently carrying 18 active files — highest in the team, avg is 12). Recommend: Reassign to Jennifer Cole (carrying 8 files). (2) Harbor View Properties $22M CRE Construction — Documentation stage, Day 16 of 10-day SLA. Blocker: Outside counsel hasn't delivered construction loan agreement draft. Action: Escalate to Documentation Manager. (3) Riverside Medical Group SBA 7(a) — Senior Review, Day 5 of 3-day SLA. Note: Senior Credit Officer Mark Thompson is out this week. Recommend: Route to alternate approver Lisa Wang. **📈 Trend:** Average credit analysis time has increased from 5.2 days to 7.8 days over the past month. Root cause appears to be volume increase (+22% deal flow) without proportional analyst staffing. Recommend discussing capacity at next management meeting."

---

### Use Case 5: Sales Performance & Incentive Compensation Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking sales compensation is uniquely complex. RMs earn base salary plus incentive compensation tied to multiple metrics: new loan production, deposit growth, fee income generation, relationship retention, portfolio quality (risk rating distribution), and cross-sell ratios. These metrics come from different systems (core banking, LOS, TM billing, CRM) and are typically compiled by finance or HR on a monthly or quarterly basis. RMs have no real-time visibility into their performance against goals — they find out whether they hit their targets weeks after the period ends. Sales managers spend days each month reconciling production reports. The OCC's Incentive Compensation Guidance (2010-27) requires banks to ensure compensation structures don't encourage excessive risk-taking, adding another layer of governance.

#### The Solution
monday.com Work Management as a sales performance dashboard and compensation tracker. An RM Scorecard board with columns: RM Name (people), Region/Team (dropdown), Loan Production YTD (numbers with $), Loan Production Goal (numbers with $), % to Goal Lending (formula), New Deposit Balances YTD (numbers with $), Deposit Goal (numbers with $), % to Goal Deposits (formula), Fee Income YTD (numbers with $), Fee Income Goal (numbers with $), Client Retention Rate (numbers with %), New Relationships Acquired (numbers), Cross-Sell Ratio (numbers), Portfolio Quality Score (numbers), Overall Performance Score (formula combining weighted metrics), Estimated Incentive Payout (formula), Payout Tier (status: Below Threshold/Tier 1/Tier 2/Tier 3/President's Club). Dashboard gives RMs a real-time "scoreboard" and sales managers a team performance view.

#### The Outcome
Real-time performance visibility — RMs know where they stand every day, not every quarter. Sales manager reporting reduced from 2 days to 2 hours per month. Performance coaching enabled by data, not gut feel. Compensation governance simplified through transparent, auditable tracking.

#### Discovery Questions
1. "How frequently do your RMs know where they stand against their performance goals — real-time, monthly, or quarterly?"
2. "How much time does your sales management team spend compiling performance reports each month?"
3. "How many different data sources feed into your incentive compensation calculations?"
4. "Have you ever had disputes or corrections to incentive payouts because of data reconciliation issues?"
5. "How do you ensure your compensation structure complies with the OCC Incentive Compensation Guidance?"

#### Industry Context
Banking sales compensation is governed by the Interagency Guidance on Sound Incentive Compensation Policies (2010), issued jointly by the OCC, Fed, FDIC, and OTS. This guidance requires that incentive compensation arrangements: (1) provide employees with incentives that appropriately balance risk and reward, (2) are compatible with effective controls and risk management, and (3) are supported by strong corporate governance. Banks must demonstrate that they monitor for potential gaming of incentive metrics. The Wells Fargo fake accounts scandal (2016) — where employees opened millions of unauthorized accounts to meet sales targets — is the cautionary tale that drives current regulatory scrutiny of banking sales incentives. SEs should be sensitive to this history and position any sales tracking tool as supporting compliance, not just driving production.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an RM Performance Scorecard board for a commercial banking sales team. Columns: Relationship Manager (people), Region (dropdown: Northeast, Southeast, Midwest, Southwest, West, National), Segment (dropdown: Middle Market, Commercial, Corporate, Specialty-Healthcare, Specialty-Real Estate, Specialty-Technology, Small Business), Loan Production YTD (numbers with $ prefix), Loan Production Annual Goal (numbers with $ prefix), Lending % to Goal (formula: Production/Goal×100 with % suffix), New Deposits YTD (numbers with $ prefix), Deposit Annual Goal (numbers with $ prefix), Deposits % to Goal (formula), Fee Income YTD (numbers with $ prefix), Fee Income Annual Goal (numbers with $ prefix), Fee % to Goal (formula), New Relationships Acquired (numbers), New Relationship Goal (numbers), Client Retention Rate % (numbers), Cross-Sell Ratio (numbers with 1 decimal), Portfolio Quality Score 1-5 (numbers — weighted average risk rating, lower is better), Overall Performance Index (formula: weighted average of all % to goals), Performance Tier (status: Below Threshold <75%/Tier 1 75-100%/Tier 2 100-125%/Tier 3 125-150%/President's Club 150%+ — red/yellow/green/blue/purple), Estimated Variable Comp (numbers with $ prefix), Last Updated (date). Group by Region. Create Dashboard with: team performance distribution chart, top 10 RMs leaderboard, production trend by month, % to goal by metric type, regional comparison, and President's Club tracker. Add automations: when Lending % to Goal reaches 100 notify RM with congratulations; when Overall Performance Index drops below 75 notify sales manager; update Last Updated to today when any metric column changes."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Performance Insight & Coaching Agent
**Agent Purpose:** Analyzes RM performance data, identifies trends and coaching opportunities, and generates personalized recommendations for sales managers.

**Triggers:**
- Weekly scheduled performance analysis (Monday mornings)
- When an RM's Overall Performance Index changes by more than 10% in either direction
- Monthly scheduled comprehensive team analysis
- On-demand trigger for individual RM deep-dive

**Actions:**
- Generates weekly "Performance Pulse" for each sales manager with team highlights and concerns
- Identifies RMs trending below goal with specific driver analysis ("Loan production is on track but deposit growth is 40% below target — potential coaching area")
- Benchmarks individual RM performance against peer group and historical trends
- Suggests specific coaching actions based on performance patterns
- Generates monthly compensation forecast so RMs know projected payout before period end
- Identifies potential compliance concerns (e.g., unusual spikes in production that might indicate risk)

**Data Required:**
- RM Performance Scorecard board
- Historical performance data (quarterly, annual trends)
- Pipeline data (leading indicators of future production)
- Activity/Call Report data (effort metrics)
- Peer benchmarks by segment and region

**Autonomy Level:** Human-in-the-Loop
All analysis and recommendations generated automatically. Performance alerts sent to managers automatically. Coaching suggestions are advisory — managers decide whether and how to act. Compliance concern flags are escalated to sales management and risk.

**Example Interaction:**
> Monday morning, the Performance Insight Agent delivers to Regional Manager Sarah Kim: "📊 **Southeast Region — Weekly Performance Pulse (Feb 17-21).** **🌟 Highlight:** RM Marcus Johnson closed $18M in CRE loans this week — now at 112% of annual lending goal (6 weeks ahead of pace). Strong TM cross-sell ratio of 3.2 (team avg: 2.1). **⚠️ Coaching Opportunity:** RM Diana Reeves — Lending at 89% to goal (on track) but deposit growth at only 52% (significantly behind). Analysis: Diana's last 8 closed deals have zero associated deposit relationships. She may be competing on rate alone without requiring operating account relationships. **Suggested coaching:** Review Diana's recent proposals to ensure deposit requirements are included in credit terms. This is also a risk consideration — loans without deposit relationships have lower retention. **📈 Team Trend:** Southeast region is #2 of 6 regions in overall production (up from #4 last quarter). Primary driver: 3 new healthcare specialty deals sourced through the hospital systems conference in January."

---

### Use Case 6: Client Onboarding & Account Opening Workflow

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
After a banking relationship is won, the onboarding process determines first impression. Commercial client onboarding involves: KYC/CDD documentation collection (articles of incorporation, beneficial ownership forms, tax IDs, board resolutions), account opening across multiple products (operating accounts, lending facilities, TM services), system setup (online banking enrollment, ACH templates, wire authorizations, positive pay configuration), and relationship team introductions (RM, TM specialist, credit analyst, service team). This process takes 30-90 days for a commercial relationship and involves 5-10 internal teams. Clients frequently express frustration: "I signed the loan documents three weeks ago but still can't access online banking." Dropped handoffs between sales and operations create a terrible experience at the most critical moment in the relationship. Banks lose 15-20% of expected relationship revenue in Year 1 due to incomplete product onboarding.

#### The Solution
monday.com Work Management with a Client Onboarding board. Columns: Client Company (text), RM (people), Onboarding Manager (people), Client Type (dropdown: Middle Market, Commercial, Corporate, Small Business), Products to Onboard (tags matching all products sold), Onboarding Stage (status: Documentation Collection → KYC/BSA Review → Account Opening → Product Setup → Testing → Training → Go-Live → Complete), Start Date (date), Target Completion Date (date), Days in Onboarding (formula), KYC Status (status: Pending/In Review/Approved/Issues), Sub-items for each product being onboarded with individual status tracking. Automations notify next team when their step is ready. Dashboard shows onboarding pipeline, average cycle time, and client experience metrics.

#### The Outcome
Onboarding cycle time reduced from 60 days to 30 days. Zero dropped handoffs between sales and operations. 95%+ product activation rate (all sold products actually set up). Client experience dramatically improved during the critical first 90 days.

#### Discovery Questions
1. "What's your average time from deal close to full product activation for a new commercial relationship?"
2. "How often do clients express frustration during onboarding — 'I signed up for treasury management but it's not set up yet'?"
3. "How many internal teams are involved in commercial client onboarding, and how do they coordinate handoffs?"
4. "What percentage of products sold are actually activated within 90 days of the relationship being booked?"
5. "How do you track KYC/BSA documentation collection during onboarding — is it a separate process or integrated?"

#### Industry Context
KYC (Know Your Customer) and CDD (Customer Due Diligence) requirements under the Bank Secrecy Act add significant complexity to banking client onboarding. The Beneficial Ownership Rule (31 CFR 1010.230) requires banks to collect and verify the identity of all individuals who own 25%+ of a legal entity. Enhanced Due Diligence (EDD) is required for higher-risk relationships. These requirements mean onboarding can't begin until compliance documentation is complete — creating a sequential dependency that extends timelines. The FinCEN Beneficial Ownership Information (BOI) reporting changes (2024-2025) have added further complexity. SEs should know that accelerating onboarding in banking requires integrating compliance requirements into the workflow, not working around them.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Commercial Client Onboarding board for a bank. Columns: Client Company (text), Primary Contact (text), Relationship Manager (people), Onboarding Manager (people), Client Segment (dropdown: Small Business, Middle Market, Commercial, Corporate), Onboarding Stage (status: Documentation Collection/KYC-BSA Review/Account Opening/Product Configuration/Testing-Validation/Client Training/Go-Live/Complete/On Hold — green for Complete, red for On Hold), Start Date (date), Target Completion Date (date), Days in Onboarding (formula), KYC Status (status: Documents Requested/Documents Received/Under Review/Approved/Issues Found — appropriate colors), BSA Risk Rating (dropdown: Low/Medium/High/Enhanced Due Diligence), Products to Activate (sub-items, each with: Product Name text, Setup Owner people, Setup Status status Pending/In Progress/Testing/Active/Blocked, Target Date date, Actual Activation Date date — products like: Operating Accounts, Online Banking, ACH Origination, Wire Transfer, Positive Pay, Lockbox, Commercial Card, Lending Facility, Interest Rate Swap, Remote Deposit, Mobile Banking), Client Satisfaction Score (numbers 1-10), Blockers (text), Notes (long text). Group by Onboarding Stage. Create views: Kanban by Stage, My Clients filtered by Onboarding Manager, Blocked Items filtered to items with On Hold status or sub-items with Blocked status, Dashboard with active onboardings count, average days to completion, product activation rate, KYC approval rate, blocked items requiring attention, and onboarding volume trend. Automations: when all sub-item Setup Status columns are Active change parent Onboarding Stage to Complete; when a sub-item Setup Status changes to Blocked notify Onboarding Manager and RM; when KYC Status changes to Approved auto-advance Onboarding Stage to Account Opening; when Days in Onboarding exceeds 45 notify Regional Manager."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Onboarding Orchestrator Agent
**Agent Purpose:** Manages the end-to-end client onboarding process, coordinating handoffs between teams and ensuring nothing falls through the cracks.

**Triggers:**
- When a deal on the Commercial Pipeline board moves to "Booked" stage (auto-creates onboarding item)
- When KYC status changes (to advance workflow)
- When a sub-item product setup is completed (to trigger next steps)
- Daily check for stalled onboardings (no progress in 3+ business days)
- When Target Completion Date is within 7 days and onboarding isn't near Complete

**Actions:**
- Auto-creates onboarding item with all products from the deal pre-populated as sub-items
- Assigns setup owners for each product based on product type and team routing rules
- Sends coordinated notifications to each team as their step becomes ready
- Generates weekly "Onboarding Status Report" for the client (via RM) showing progress
- Identifies and escalates stalled onboardings with root cause analysis
- Sends client welcome communication template to RM on Day 1
- Tracks and reports on-time completion rate and product activation metrics

**Data Required:**
- Client Onboarding board
- Commercial Pipeline board (for deal-to-onboarding handoff)
- Team assignment/routing rules (which team handles which product setup)
- KYC/BSA board (for compliance status)
- Historical onboarding data for benchmarking

**Autonomy Level:** Escalation-Based
Auto-creates onboarding items and assigns teams. Notifications and coordination are fully automatic. Client-facing communications are generated but sent by RM. Escalations for stalled onboardings go to the Onboarding Manager first, then Regional Manager if unresolved after 2 business days.

**Example Interaction:**
> RM Jason Park closes a new middle market relationship with Pacific Coast Distributors — $10M revolving credit, operating accounts, ACH origination, positive pay, online banking, and commercial card program. The Onboarding Orchestrator Agent automatically creates an onboarding item with 6 product sub-items, assigns setup owners (Lending Ops for the credit facility, Deposit Ops for accounts, TM Implementation for ACH/positive pay, Digital Banking for online access, Card Services for commercial card), sets a target completion date of 30 business days, and sends an introduction email template to Jason: "Congratulations on the Pacific Coast Distributors win! Here's their onboarding timeline and key milestones. Please forward the client welcome packet attached." Three days in, KYC review flags a beneficial ownership question — one owner at 24% (just under the 25% threshold, but EDD triggers at bank's discretion for the distribution industry). The agent alerts the Onboarding Manager: "⚠️ Pacific Coast Distributors — KYC flag: Owner David Chen at 24% beneficial ownership. Distribution industry is higher-risk for BSA. Recommend BSA Officer review for potential EDD requirement before proceeding. Onboarding paused at KYC stage."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| RM (Relationship Manager) | The primary sales and relationship contact for commercial banking clients, responsible for the full client relationship |
| Book of Business | An RM's portfolio of client relationships, measured by total loans, deposits, and fee income |
| Wallet Share | Percentage of a client's total banking needs captured by the bank (loans, deposits, TM, cards, wealth) |
| Call Report (Sales) | Documentation of client interactions — required for compliance and relationship monitoring |
| Credit Memorandum | Formal analysis document prepared by credit analyst recommending loan approval, including financial analysis and risk assessment |
| Loan Committee | Senior management body that approves larger loan requests (threshold varies by bank, typically $5-25M+) |
| Spread | The interest rate differential between what the bank pays for deposits and charges on loans — primary revenue driver |
| ECR (Earnings Credit Rate) | Rate applied to commercial deposit balances to offset treasury management service fees |
| Analyzed Fees | Treasury management fee structure where gross fees are reduced by ECR offset on deposit balances |
| KYC/CDD | Know Your Customer / Customer Due Diligence — BSA/AML requirements for client identification and risk assessment |
| Beneficial Ownership | Individuals who own 25%+ of a legal entity — must be identified and verified at account opening |
| Covenant | Contractual conditions in a loan agreement requiring the borrower to maintain certain financial metrics |
| Risk Rating | Bank's internal classification of credit risk for a borrower, typically 1-8 scale (1=lowest risk) |
| nCino | Leading cloud-based loan origination system for banks, built on Salesforce platform |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| EVP/Head of Commercial Banking | Overall commercial revenue targets, sales strategy, team management | Decision-maker |
| Regional/Market President | Geographic P&L ownership, local market strategy, community relationships | Decision-maker |
| Sales Manager/Team Lead | RM coaching, pipeline management, deal strategy, performance management | Key influencer |
| Relationship Manager | Client-facing sales and relationship management, deal origination | Primary user |
| Treasury Management Sales Specialist | TM product-specific sales, solution design, pricing | User |
| Chief Credit Officer | Credit policy, approval authority, portfolio risk management | Veto authority on credit |
| Head of Operations | Account opening, servicing, onboarding, operational efficiency | Influencer (onboarding) |
| BSA/AML Officer | Customer due diligence, transaction monitoring, regulatory compliance | Gatekeeper (onboarding) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Product & R&D | Sales surfaces customer needs; Product builds solutions — feedback loop is critical | Product feedback pipeline, feature request tracking |
| Marketing | Lead generation, campaign management, brand positioning for sales enablement | CRM, marketing automation, lead scoring |
| Operations | Post-sale servicing, account maintenance, client experience delivery | Service management, SLA tracking |
| Compliance/Risk | KYC onboarding, ongoing monitoring, sales practice oversight | Compliance workflow, examination readiness |
| IT | CRM/LOS administration, integrations, reporting infrastructure | IT Work Management for sales tool support |
| Finance | Compensation calculations, revenue recognition, profitability analysis | Financial reporting, compensation tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce Financial Services Cloud | Enterprise CRM for banking — dominant in large banks, expensive, complex | Mid-market banks priced out of Salesforce; faster deployment; business-user configurability vs. admin-dependent Salesforce |
| nCino | Loan origination system — strong for credit workflow but not sales management | Complementary positioning — monday.com for the sales side, nCino for credit process; coordination layer |
| Microsoft Dynamics 365 | CRM bundled with Microsoft ecosystem — common in banks using M365 | Superior UX and automation; faster time-to-value; better sales-specific workflows |
| Abrigo (Sageworks) | Credit analysis and portfolio risk management — compliance-focused | Different layer — monday.com for sales pipeline and coordination; Abrigo for credit analytics |
| Spreadsheets (Excel/Google Sheets) | Default pipeline tracking tool for most banking sales teams | Modern, automated, collaborative replacement with built-in workflow and governance |
| HubSpot | Growing CRM for smaller banks/credit unions — good marketing, limited banking features | More customizable for banking-specific workflows; better automation; portfolio management capabilities |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Salesforce — why would we add another tool?" | Many banks use Salesforce for the formal CRM record but struggle with the day-to-day workflow: pipeline coordination, activity tracking, onboarding management, and performance dashboards. monday.com CRM can replace Salesforce for mid-market banks, or complement it as the operational layer that makes Salesforce data actionable for RMs. |
| "Our RMs won't adopt another system — they barely use what we have" | That's exactly the problem monday.com solves. RMs don't use current tools because they're clunky and add work. monday.com is built for ease-of-use — mobile-first, quick entry, visual. When the tool actually saves RMs time (AI-assisted call reports, real-time performance visibility), adoption follows. |
| "We need to be on nCino for lending compliance" | Absolutely — nCino handles the formal credit process. monday.com is the coordination layer around nCino: pipeline management before credit submission, deal tracking across the RM workflow, TM sales pipeline, onboarding orchestration, and performance management. They're complementary, not competitive. |
| "How do you handle banking-specific compliance requirements for sales tracking?" | monday.com's permission controls, audit logs, and data governance features support banking compliance needs. Activity tracking supports BSA ongoing monitoring requirements. Performance dashboards help demonstrate incentive compensation governance (OCC 2010-27). SOC 2 Type II certification and encryption address security requirements. |
| "Our data can't leave the country / we need data residency" | monday.com offers data residency options and complies with data sovereignty requirements. We can discuss specific regulatory requirements for your charter type and jurisdiction. |
| "We tried a CRM project before and it failed — RMs went back to spreadsheets in 3 months" | That's a common story, and it usually fails for two reasons: (1) the tool added work without giving value back, and (2) it was rolled out all-at-once. monday.com succeeds because it's genuinely easier than spreadsheets (visual, automated, mobile), and we recommend starting with one high-value workflow (pipeline tracking) before expanding. Quick wins build adoption. |

## Proof Points
*(To be populated with customer references)*
- [Commercial bank using monday.com CRM for relationship management]
- [Financial institution that consolidated from spreadsheets to monday.com for pipeline tracking]
- [Banking client demonstrating improved sales performance visibility]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
