# Banking × Operations Playbook

## Overview

Operations in banking is the backbone that keeps the financial system functioning — processing millions of transactions daily, managing regulatory compliance workflows, overseeing branch and back-office functions, and ensuring that every wire transfer, loan disbursement, account opening, and trade settlement happens accurately, on time, and within regulatory guardrails. Banking operations teams range from hundreds of people at regional banks to tens of thousands at global institutions like JPMorgan Chase, Bank of America, or HSBC. The function encompasses payment processing, trade operations, loan operations, deposit operations, treasury operations, reconciliation, and exception management.

The regulatory burden on banking operations is immense. Teams must comply with Basel III/IV capital requirements, BSA/AML (Bank Secrecy Act/Anti-Money Laundering) regulations, KYC (Know Your Customer) mandates, SOX (Sarbanes-Oxley) controls, FDIC requirements, OCC examination standards, and consumer protection rules (TILA, RESPA, ECOA). Every process must be auditable, every exception documented, and every SLA tracked. A single compliance failure can result in multi-million dollar fines, consent orders, or reputational damage that takes years to recover from.

The industry is under tremendous pressure to modernize. Legacy core banking systems (Fiserv, FIS, Jack Henry) process transactions but were never designed for workflow visibility, cross-functional collaboration, or intelligent automation. Operations leaders are caught between the need to reduce cost-per-transaction (industry benchmark: $0.50-$3.00 depending on transaction type), improve processing speed (same-day ACH, real-time payments), maintain iron-clad compliance, and somehow innovate — all while facing headcount pressure and a shrinking talent pool willing to work in operations roles. The rise of fintech competitors who process at 10x speed with 10% of the headcount is an existential threat to traditional banking operations models.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Banking operations is one of the most labor-intensive functions in any industry; a mid-size bank may have 500-2,000 ops staff doing highly repetitive, rules-based work |
| 2 | Scale Impact Without Overhead | High | Transaction volumes grow 10-15% annually but headcount budgets are flat or declining; every new product/regulation adds operational complexity |
| 3 | Consolidate Tech Stack with AI | Medium-High | Banks average 30-50 internal systems; ops teams toggle between core banking, workflow tools, compliance platforms, email, and spreadsheets |

## Prioritized Use Cases

---

### Use Case 1: Exception & Break Management Workflow

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banking operations revolves around exceptions — transactions that don't process cleanly and require human intervention. Wire transfers with missing beneficiary information, ACH returns, NSF items, reconciliation breaks, failed trade settlements, and compliance holds generate thousands of exceptions daily at a mid-size bank. Each exception requires an analyst to investigate, contact the relevant party (branch, customer, counterparty), resolve the issue, and document the resolution for audit purposes. Most banks manage exceptions in a combination of core banking queues, shared email inboxes, and Excel tracking sheets. There's no visibility into exception aging, no workload balancing, and no pattern detection. A single unresolved exception can cascade — a failed wire can trigger a compliance escalation, a customer complaint, and a regulatory inquiry.

#### The Solution
monday.com Work Management as the exception management command center. Each exception is an item with columns for: exception type (dropdown: Wire Exception, ACH Return, NSF, Reconciliation Break, Settlement Fail, Compliance Hold, Other), source system, transaction reference number, dollar amount, customer/account number, assigned analyst, priority (based on dollar amount and age), SLA deadline, status (New, Investigating, Pending External, Resolved, Escalated), resolution code, and resolution notes. Automations enforce SLAs: exceptions over $100K are auto-assigned to senior analysts, items approaching SLA deadline trigger escalation notifications, and resolved items are archived with full audit trail. Dashboards show real-time exception volumes, aging, and analyst productivity.

#### The Outcome
Average exception resolution time decreases by 40%. SLA compliance improves from 75% to 95%+. Analyst capacity increases by 30% as workload balancing eliminates bottlenecks. Audit preparation time drops by 80% — every exception has a documented trail. Pattern detection surfaces systemic issues (e.g., "Branch #42 generates 3x more wire exceptions than average — training needed").

#### Discovery Questions
1. "How many exceptions does your operations team process daily, and what's the breakdown by type?"
2. "What does your current exception tracking look like — is there a single system, or is it a mix of queues, email, and spreadsheets?"
3. "When a regulator asks to see how you handled a specific exception from six months ago, how long does it take to pull that documentation?"
4. "How do you balance workload across analysts when exception volumes spike — say, at month-end or after a system migration?"
5. "Are you able to identify patterns in exceptions — like a specific branch, product, or counterparty that generates disproportionate issues?"

#### Industry Context
Exception management is the "hidden factory" of banking operations. Industry studies estimate that 5-15% of all banking transactions generate some form of exception requiring manual intervention. At a bank processing 500,000 transactions per day, that's 25,000-75,000 exceptions daily. The cost per exception ranges from $5 for simple items (NSF decisions) to $200+ for complex ones (wire investigations, compliance holds). SLAs are typically: wire exceptions within 2 hours, ACH returns by next business day, reconciliation breaks within 3 business days, and compliance holds per regulatory requirements (24-72 hours). The OCC and FDIC specifically examine exception management processes during bank examinations, making documentation and audit trails non-negotiable.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Exception Management System for a bank's operations team. Create a board called 'Operations Exceptions' with these columns: Exception ID (text auto-numbered), Exception Type (dropdown: Wire Exception, ACH Return, ACH Exception, NSF/Overdraft, Reconciliation Break, Settlement Failure, Compliance Hold, Check Exception, Loan Funding Exception, Other), Source System (dropdown: Core Banking, Wire Platform, ACH Processor, Trading System, Reconciliation Tool, Manual Entry), Transaction Reference (text), Dollar Amount (numbers), Customer/Account (text), Branch/Unit (dropdown with branch numbers), Assigned Analyst (people), Priority (status: Critical-$100K+, High-$25K+, Medium-$5K+, Low-Under $5K), SLA Deadline (date with time), Status (status: New, Investigating, Pending External Info, Escalated to Manager, Resolved, Closed), Resolution Code (dropdown: Corrected & Reprocessed, Returned to Originator, Customer Contacted & Resolved, Compliance Cleared, Write-Off Approved, Duplicate-Merged, System Error Fixed), Resolution Notes (long text), Date Created (date), and Date Resolved (date). Groups: organize by Status. Create automations: (1) When new item created with Dollar Amount over 100000, set Priority to 'Critical' and assign to Senior Analyst group; (2) When SLA Deadline is within 1 hour and Status is not Resolved or Closed, notify Assigned Analyst and Operations Manager; (3) When Status changes to 'Resolved', calculate resolution time and log it; (4) When Status is 'New' for more than 30 minutes, notify Assigned Analyst. Add Dashboard: exceptions by type (pie chart), open exceptions aging (bar chart by hours), daily exception volume trend (line chart), SLA compliance rate (numbers widget), analyst workload distribution (chart), and resolution time by type (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Exception Triage Engine
**Agent Purpose:** Automatically categorize, prioritize, route, and suggest resolutions for operations exceptions based on pattern recognition and historical data.

**Triggers:**
- New exception item created (from system integration or manual entry)
- Exception approaching SLA deadline (configurable threshold)
- Exception dollar amount exceeds escalation threshold
- Pattern detection: same exception type from same source exceeds threshold in 24 hours
- Daily/weekly exception trend analysis

**Actions:**
- Auto-categorize exceptions based on transaction data and route to appropriate specialist
- Suggest resolution based on similar past exceptions (matching type, source, and dollar range)
- Calculate dynamic priority based on dollar amount, customer tier, age, and regulatory sensitivity
- Escalate to management when SLA breach is imminent with context and recommended action
- Detect anomalous exception patterns (volume spikes, new exception types, concentrated sources) and alert leadership
- Generate end-of-day exception report with volumes, resolutions, SLA performance, and open items

**Data Required:**
- Transaction data from core banking and payment systems
- Historical exception database with resolution codes and times
- Customer tier/priority information
- SLA rules by exception type
- Analyst skills matrix and current workload
- Regulatory requirements by exception category

**Autonomy Level:** Escalation-Based
Auto-categorization and routing are fully automated. Resolution suggestions are advisory (analyst confirms). Dollar-amount exceptions above $500K require manager review. Pattern alerts are informational and sent to leadership.

**Example Interaction:**
> At 2:15 PM, the wire processing system generates 47 exceptions in a 15-minute window — all outgoing international wires to correspondent banks in Southeast Asia, all failing with "beneficiary account validation error." Under normal conditions, the bank processes 3-5 wire exceptions per hour.
>
> The Exception Triage Engine immediately detects the anomaly: "ALERT — Wire exception volume spike: 47 exceptions in 15 minutes (baseline: 3-5/hour). All share common attributes: international wires, APAC corridor, beneficiary validation failure. Likely cause: correspondent bank system outage or SWIFT format change. Total value at risk: $12.4M across 47 transactions."
>
> The agent holds all 47 exceptions in a single batch rather than distributing to individual analysts, assigns them to the International Wire specialist team, and drafts an inquiry to the correspondent bank's operations desk. It also creates an escalation item for the Wire Operations Manager and notifies the Treasury team of potential end-of-day settlement exposure. Within 30 minutes, the correspondent bank confirms a format change — the agent updates all 47 exceptions with the root cause and recommended fix, and the specialist team reprocesses the batch in under an hour instead of the 4-6 hours individual processing would have taken.

---

### Use Case 2: Regulatory & Compliance Task Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking operations is drowning in compliance obligations. Every regulatory change, examination finding, audit recommendation, and internal policy update generates compliance tasks that must be tracked, assigned, completed, and evidenced. A mid-size bank may have 200-500 open compliance action items at any time, spanning BSA/AML program enhancements, OCC/FDIC examination commitments (MRAs — Matters Requiring Attention, MRIAs — Matters Requiring Immediate Attention), SOX control testing, fair lending monitoring, and internal audit findings. These are tracked in — predictably — spreadsheets, shared drives, and email threads. When the regulators come back for a follow-up examination, the scramble to prove that every commitment was met is a multi-week fire drill involving dozens of people.

#### The Solution
monday.com Work Management as the compliance action tracking system. Each compliance item has columns for: regulatory source (OCC, FDIC, Fed, State, Internal Audit, BSA/AML, SOX), finding/requirement description, severity (MRIA, MRA, Observation, Recommendation), assigned owner, department, due date, status (Not Started, In Progress, Evidence Gathering, Under Review, Complete, Overdue), evidence attachments (files column), reviewer, review status, and linked regulatory reference. Automations send reminders at 30/14/7 days before due date, escalate overdue items to the Chief Compliance Officer, and prevent status changes to "Complete" without evidence attached. Board templates exist for common examination types, and a Calendar view shows all deadlines across the organization.

#### The Outcome
Compliance teams gain real-time visibility into the status of every regulatory commitment. Examination preparation time drops from weeks to hours. Zero items are missed or forgotten — automated escalation ensures accountability. Evidence gathering is centralized, eliminating the "where's the proof?" scramble. Regulators see a well-organized, trackable compliance program, which directly improves examination ratings.

#### Discovery Questions
1. "How do you currently track regulatory commitments and examination findings — is there a single system or is it distributed?"
2. "During your last OCC/FDIC examination, how long did it take to pull together evidence that previous findings were remediated?"
3. "How many open MRAs or MRIAs do you have right now, and are you confident every one has an owner and a timeline?"
4. "When a new regulation is issued, how does the operational impact assessment and task creation process work?"
5. "What happens when a compliance deadline is missed — how quickly is leadership made aware?"

#### Industry Context
Regulatory examinations are the highest-stakes events in banking operations. The OCC (for national banks), FDIC (for state-chartered banks), and Federal Reserve (for bank holding companies) conduct examinations annually or more frequently for banks with issues. Examination findings are categorized: MRIA (Matters Requiring Immediate Attention) are the most serious — failure to remediate can lead to enforcement actions, consent orders, or even charter revocation. MRAs (Matters Requiring Attention) are significant but less urgent. Banks also face state regulatory examinations, BSA/AML reviews by FinCEN, consumer compliance examinations, and annual internal/external audits. The CAMELS rating system (Capital, Asset quality, Management, Earnings, Liquidity, Sensitivity) determines a bank's regulatory standing — and operational compliance directly impacts the "M" (Management) rating.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Compliance Tracker for a bank's operations and compliance team. Create a board called 'Compliance Action Items' with these columns: Item ID (text), Regulatory Source (dropdown: OCC, FDIC, Federal Reserve, State Regulator, BSA/AML-FinCEN, SOX, Internal Audit, External Audit, Fair Lending, CRA), Finding Description (long text), Severity (status: MRIA, MRA, Observation, Recommendation, Self-Identified), Department (dropdown: Operations, BSA/AML, Lending, Deposit Ops, Wire Ops, Treasury, IT, Compliance), Assigned Owner (people), Backup Owner (people), Due Date (date), Status (status: Not Started, In Progress, Evidence Gathering, Under Review, Complete, Overdue, Extension Requested), Evidence (files), Reviewer (people), Review Status (status: Not Reviewed, Under Review, Approved, Returned for Rework), Regulatory Reference (text), Examination Date (date), and Completion Notes (long text). Groups: organize by Severity (MRIA, MRA, Observation, Recommendation). Create automations: (1) 30 days before Due Date, notify Assigned Owner and Backup Owner; (2) 7 days before Due Date, notify Assigned Owner, Backup Owner, and Department Head; (3) When Due Date passes and Status is not 'Complete', change to 'Overdue' and notify Chief Compliance Officer; (4) When Status changes to 'Complete' and Evidence column is empty, revert to 'Evidence Gathering' and notify owner; (5) When Review Status changes to 'Approved', change Status to 'Complete'. Dashboard: open items by severity (pie chart), items by department (bar chart), timeline of upcoming deadlines (Gantt), overdue items (table with red highlighting), completion trend over time (line chart), and MRIA/MRA aging (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Compliance Guardian
**Agent Purpose:** Monitor compliance deadlines, verify evidence completeness, generate examination-ready reports, and proactively surface regulatory changes that may create new obligations.

**Triggers:**
- New compliance item created
- Item due date within 30/14/7 days
- Item status changes to "Overdue"
- Evidence uploaded for review
- Regulatory bulletin or guidance published (external monitoring)
- Examination notification received

**Actions:**
- Validate evidence completeness against finding requirements (e.g., "this MRIA requires policy update + training records + test results — you have 2 of 3")
- Generate examination preparation packages grouping all items by source with evidence summaries
- Draft status update reports for Board of Directors and regulatory committees
- Monitor regulatory news feeds for new guidance that may impact open commitments
- Create new compliance items when regulations change, pre-populated with department, estimated effort, and suggested timeline
- Track cross-dependencies between compliance items and flag when one delayed item impacts others

**Data Required:**
- Compliance action items database
- Regulatory examination reports and correspondence
- Evidence documents and attachments
- Regulatory news/guidance feeds (OCC bulletins, FDIC Financial Institution Letters, Fed Supervision releases)
- Organizational structure and responsibility matrix
- Historical examination results and remediation timelines

**Autonomy Level:** Human-in-the-Loop
Monitoring, alerting, and report generation are automated. Evidence validation is advisory. New compliance item creation from regulatory changes requires CCO review and approval. Examination preparation packages require legal and compliance sign-off.

**Example Interaction:**
> The Regulatory Compliance Guardian detects that the OCC has published Bulletin 2026-04, updating guidance on third-party risk management for banking organizations. It cross-references the bank's current compliance obligations and identifies three impacts: (1) the existing third-party vendor assessment process needs updating to include AI/technology vendor categories, (2) the Board reporting template for third-party risk needs a new AI-specific section, and (3) two existing MRAs related to vendor management may need revised remediation plans.
>
> The agent creates three new compliance items — one for each impact — with the regulatory reference, suggested department assignments (Vendor Management, Compliance, and Board Secretary), and recommended due dates based on the bulletin's effective date (90 days). It also flags the two existing MRAs for review: "OCC Bulletin 2026-04 may change the remediation standard for MRA #2024-17 (Vendor Due Diligence) and MRA #2025-03 (Ongoing Monitoring). Recommend legal review of whether current plans meet updated guidance."
>
> The CCO reviews the auto-generated items, adjusts ownership and timelines, and approves. The bank is proactively addressing the new guidance before the next examination — a posture regulators explicitly reward.

---

### Use Case 3: Account Opening & Onboarding Operations

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Opening a bank account is deceptively complex from an operations perspective. A single retail account opening involves: identity verification (CIP — Customer Identification Program), OFAC screening, CDD (Customer Due Diligence), beneficial ownership determination (for business accounts), risk rating, document collection, system setup in the core banking platform, debit card issuance, online banking enrollment, regulatory disclosures, and welcome communications. For commercial accounts, add UBO (Ultimate Beneficial Ownership) verification, entity documentation, board resolutions, multi-signer setup, cash management services configuration, and treasury onboarding. A commercial account opening can involve 15-30 discrete tasks spanning 3-5 departments and take 5-15 business days. Most banks track this via email chains between branches, operations, compliance, and treasury — with no centralized visibility into where each application stands.

#### The Solution
monday.com Work Management with templated onboarding workflows by account type. Each account application is an item with columns for: application type (Retail, Small Business, Commercial, Treasury Management), applicant name, entity type, assigned processor, branch/originator, application date, target completion date, KYC/CDD status, OFAC screening status, documentation status, core system setup status, overall status, and risk rating. Subitems represent individual tasks with owners and dependencies. Automations enforce sequencing (can't proceed to core setup until KYC is approved), send status updates to the originating branch, and escalate items stalled for more than 24 hours. WorkForms capture initial application data from branches, eliminating the "email a PDF" workflow.

#### The Outcome
Account opening cycle time reduces by 50% (commercial accounts from 10 days to 5 days). Operations staff handles 40% more applications with the same headcount. Branches have real-time visibility into application status without calling operations. Compliance documentation is complete and audit-ready from day one. Customer experience improves dramatically — faster onboarding, fewer "we need one more document" callbacks.

#### Discovery Questions
1. "How long does it take to fully open and activate a commercial bank account from application to first transaction?"
2. "How many people and departments are involved in a typical account opening, and how do they coordinate?"
3. "What's the biggest bottleneck in your account opening process — is it documentation, KYC/CDD, system setup, or something else?"
4. "When a branch banker asks 'where's my customer's application,' how do they get that answer?"
5. "How many account applications are you processing per month, and is that volume growing?"

#### Industry Context
The Bank Secrecy Act requires all banks to have a Customer Identification Program (CIP) that verifies the identity of every person opening an account. For individuals, this means collecting name, date of birth, address, and ID number, then verifying against government databases. For businesses, the CDD Rule (effective 2018) requires identifying and verifying beneficial owners who own 25%+ or have significant control. OFAC (Office of Foreign Assets Control) screening must be performed against the SDN (Specially Designated Nationals) list before opening any account. The FinCEN Beneficial Ownership Rule (updated 2024-2025) expanded reporting requirements further. Account opening is also a key BSA/AML control point — the initial risk rating determines ongoing monitoring intensity. Banks that get this wrong face severe penalties: USAA was fined $140M in 2022 for BSA/AML failures related to inadequate onboarding controls.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Account Opening Operations Tracker for a bank. Create a board called 'Account Opening Pipeline' with these columns: Application ID (text), Account Type (dropdown: Personal Checking, Personal Savings, Small Business, Commercial Operating, Commercial Lending, Treasury Management, Trust, IRA/Retirement), Applicant/Entity Name (text), Originating Branch (dropdown with branch names/numbers), Branch Contact (people), Assigned Processor (people), Application Date (date), Target Completion Date (date), KYC/CDD Status (status: Not Started, Documents Requested, Under Review, Enhanced Due Diligence Required, Approved, Declined), OFAC Screening (status: Pending, Clear, Potential Match-Review Required, Blocked), Beneficial Ownership (status: N/A-Individual, Collected, Verification In Progress, Verified, Incomplete), Risk Rating (status: Low, Medium, High, Prohibited), Documentation Status (status: Incomplete, Complete, Under Review), Core System Setup (status: Not Started, In Progress, Complete, Error), Overall Status (status: Received, Processing, Pending Compliance, Approved-Setting Up, Active, Declined, Withdrawn), and Notes (long text). Groups: organize by Overall Status. Add subitems for the task checklist: ID Verification (people, status, date), OFAC Screen (people, status, date), CDD Review (people, status, date), Beneficial Ownership Verification (people, status, date), Document Collection (people, status, date), Risk Rating Assignment (people, status, date), Core System Entry (people, status, date), Card/Online Banking Setup (people, status, date), Welcome Package Sent (people, status, date), Branch Notification (people, status, date). Automations: (1) When Application Date is set and Target Completion not set, auto-set Target to +5 business days for retail, +10 for commercial; (2) When KYC/CDD Status changes to 'Approved', change Core System Setup to 'Not Started' and notify processor; (3) When Overall Status is 'Processing' for more than 48 hours, notify Assigned Processor and Operations Manager; (4) When all subitems are Complete, change Overall Status to 'Active' and notify Branch Contact. Dashboard: applications by status (funnel chart), average cycle time by account type (chart), applications by branch (bar chart), pending compliance reviews (table), and daily/weekly volume trend (line chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Account Opening Accelerator
**Agent Purpose:** Streamline account opening by automating document verification, compliance checks, and multi-department coordination to reduce cycle time and ensure regulatory compliance.

**Triggers:**
- New account application submitted via WorkForm or created manually
- Document uploaded to application
- KYC/CDD review completed
- Application stalled (no status change in 24 hours)
- OFAC screening returns potential match

**Actions:**
- Auto-populate application checklist based on account type (retail vs. commercial vs. treasury)
- Validate document completeness against account type requirements and flag missing items
- Route application to appropriate specialist (standard KYC for low-risk, enhanced due diligence for high-risk)
- Generate branch status updates at key milestones without manual notification
- Compile compliance documentation package for audit readiness
- Identify and flag potential duplicate applications or existing customer relationships

**Data Required:**
- Application data (entity type, account type, applicant details)
- Document requirements matrix by account type
- Customer database for duplicate detection
- OFAC/SDN screening results
- KYC/CDD policy rules and risk rating criteria
- Branch and processor assignment rules

**Autonomy Level:** Human-in-the-Loop
Document completeness checks and status notifications are automated. All compliance decisions (KYC approval, risk rating, OFAC match resolution) require human review and sign-off. Declined applications require manager approval.

**Example Interaction:**
> A branch banker submits a commercial account opening for Westfield Distribution LLC via WorkForm. The Account Opening Accelerator creates the application, identifies it as a Commercial Operating account, and generates the full 14-step checklist. It immediately runs an existing customer check and finds that Westfield Distribution's principal, Mark Chen, has a personal account at the bank — flagging this as an existing relationship opportunity.
>
> The agent validates the submitted documents: Articles of Organization (✓), EIN confirmation (✓), Operating Agreement (✓), beneficial ownership form (✓ — identifies Mark Chen at 70% and Sarah Chen at 30%), driver's licenses for both owners (✓ for Mark, ✗ missing for Sarah). It immediately notifies the branch: "Missing document: government-issued photo ID for Sarah Chen (30% beneficial owner). All other documents received. Application will proceed to OFAC screening for Mark Chen; Sarah's screening pending ID receipt."
>
> OFAC screening for Mark Chen returns clear. The agent routes the application to the CDD team with a pre-populated risk assessment: "Low-medium risk. Domestic LLC, distribution industry (no elevated risk indicators), two beneficial owners, both US persons. Recommend standard CDD." The CDD analyst reviews and approves within 2 hours. Meanwhile, Sarah's ID arrives, OFAC clears, and the agent advances the application to core system setup — all within the same business day. The branch receives automated updates at each milestone.

---

### Use Case 4: Loan Operations & Funding Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Loan operations is one of the most complex workflows in banking. From application through underwriting, approval, documentation, closing, funding, and boarding — a single commercial loan touches 8-12 people across sales, credit, operations, legal, compliance, and treasury. The average commercial loan takes 30-60 days to close, and operational delays are the #1 source of customer dissatisfaction. Loan ops teams track progress in a mix of the Loan Origination System (LOS), email, and shared spreadsheets. When the CFO asks "how many loans are in the pipeline and what's the expected funding this month," the answer requires hours of manual aggregation. When a loan closes late because someone forgot to order the flood determination or the title search, the borrower and the lending officer both lose confidence in the bank.

#### The Solution
monday.com Work Management as the loan operations dashboard, sitting alongside (not replacing) the LOS. Each loan is an item with columns for: loan type, borrower, loan amount, lending officer, processor, underwriter, target closing date, actual closing date, stage (Application, Processing, Underwriting, Approval, Documentation, Closing, Funding, Boarded), document checklist status, conditions status, and days in current stage. Subitems track every operational task with dependencies: title search, flood determination, appraisal ordered/received, UCC filing, environmental review, credit memo, approval documentation, closing package preparation, wire instructions, and boarding in the core system. Automations flag stalled loans, enforce task sequencing, and provide real-time pipeline visibility.

#### The Outcome
Loan closing cycle time reduces by 20-30%. Zero loans miss closing because of forgotten operational tasks. Pipeline visibility enables accurate funding forecasts without manual aggregation. Lending officers spend less time chasing operations for status updates. Borrower satisfaction improves as the process feels organized and predictable.

#### Discovery Questions
1. "What's your average time from loan approval to funding, and how much of that is operational processing vs. waiting?"
2. "How does your lending team currently get visibility into where a loan stands in the operations pipeline?"
3. "What are the most common causes of loan closing delays — is it appraisals, documentation, title, or internal processing?"
4. "How do you track and clear conditions (pre-closing and post-closing) — is there a system or is it manual?"
5. "If I asked for a real-time snapshot of your loan pipeline — number of loans, total dollar amount, and expected funding dates — how quickly could you produce that?"

#### Industry Context
Loan operations in banking is governed by extensive regulations. Residential mortgages must comply with TILA-RESPA (Loan Estimate and Closing Disclosure timing requirements), HMDA reporting, fair lending rules, and QM (Qualified Mortgage) standards. Commercial loans have looser regulatory requirements but greater complexity — multi-property collateral, environmental reviews (Phase I/II), UCC searches and filings, title insurance, flood determinations (mandatory per SFHA requirements), and covenant documentation. The Loan Origination System (Encompass, nCino, Abrigo, or similar) handles regulatory compliance and document generation, but operational workflow management — who does what, when, and is it done — typically falls to spreadsheets and email. SBA loans add another layer: SBA authorization, SBA-specific forms (1919, 1920), and SBA review timelines that are largely outside the bank's control.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Loan Operations Pipeline Tracker for a bank. Create a board called 'Loan Operations Pipeline' with these columns: Loan Number (text), Loan Type (dropdown: Commercial Real Estate, C&I Line of Credit, C&I Term Loan, SBA 7(a), SBA 504, Construction, Residential Mortgage, HELOC, Consumer), Borrower Name (text), Loan Amount (numbers), Lending Officer (people), Processor (people), Underwriter (people), Application Date (date), Target Closing Date (date), Actual Closing Date (date), Stage (status: Application Received, Processing, In Underwriting, Credit Committee, Approved-Conditions, Documentation, Pre-Closing, Closing, Funding, Boarded), Days in Stage (formula), Conditions Status (status: Outstanding, Partially Cleared, All Cleared), Priority (status: Normal, Expedited, Past Target Date), and Pipeline Notes (long text). Groups: organize by Stage. Add subitems as an operational checklist: Title Search Ordered (status, date, people), Title Search Received (status, date), Flood Determination (status, date), Appraisal Ordered (status, date, people), Appraisal Received (status, date), Environmental Review (status, date), UCC Search (status, date), Insurance Verification (status, date), Credit Memo Complete (status, date, people), Committee Approval (status, date), Loan Documents Prepared (status, date, people), Closing Scheduled (status, date), Wire Instructions Confirmed (status, date), Funding Complete (status, date), Core System Boarded (status, date). Automations: (1) When Days in Stage exceeds 5, change Priority to 'Expedited' and notify Processor; (2) When Target Closing Date is within 7 days and Stage is not 'Pre-Closing' or later, notify Processor and Lending Officer; (3) When all condition subitems are Complete, change Conditions Status to 'All Cleared'; (4) When Stage changes to 'Funding', notify Treasury for wire preparation. Dashboard: pipeline by stage (funnel chart), total pipeline dollar amount (numbers widget), average days to close by loan type (chart), loans past target date (table), and weekly funding forecast (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Loan Ops Navigator
**Agent Purpose:** Monitor the loan pipeline, predict bottlenecks, ensure no operational step is missed, and provide real-time pipeline intelligence to lending leadership.

**Triggers:**
- New loan enters operations pipeline
- Loan stalls in a stage for more than configurable threshold
- Target closing date within 10 business days
- Condition or task completed (subitem status change)
- Weekly pipeline review schedule
- Appraisal or title search overdue

**Actions:**
- Generate prioritized daily task list for each processor based on pipeline urgency and closing dates
- Predict closing date based on current stage, loan type, and historical cycle times
- Identify bottlenecks and recommend acceleration actions (e.g., "order appraisal rush" or "escalate title search")
- Create weekly pipeline report with dollar-weighted stage analysis and funding forecasts
- Track and alert on post-closing conditions (items due after funding that are often forgotten)
- Compile closing checklist verification — ensuring every required document and condition is addressed before scheduling closing

**Data Required:**
- Loan pipeline data (amounts, types, stages, dates)
- Historical closing timelines by loan type and processor
- Third-party vendor status (title companies, appraisers, environmental firms)
- Conditions lists from underwriting/credit approval
- Treasury funding calendar and wire cut-off times
- Regulatory timing requirements (TRID disclosure periods, flood determination timelines)

**Autonomy Level:** Human-in-the-Loop
Pipeline monitoring, bottleneck detection, and reporting are automated. Task prioritization is advisory. Closing readiness verification requires processor confirmation. Funding authorization requires treasury approval.

**Example Interaction:**
> It's Monday morning, and the Loan Ops Navigator generates a priority report for the operations team. This week: 14 loans targeting Friday closing with a combined value of $28.7M. The agent identifies three at-risk closings:
>
> Loan #2026-0847 (CRE, $4.2M, Metro Office Properties): Appraisal was ordered 18 days ago but not received. Based on historical data, CRE appraisals average 14 business days. The agent recommends: "Contact appraiser for status. If delayed, consider rush fee ($500) or discuss closing date extension with borrower. Impact: Friday closing at risk."
>
> Loan #2026-0851 (C&I, $1.8M, Greenfield Services): All conditions cleared except insurance verification. The agent notes: "Insurance certificate requested from borrower's agent 5 days ago, no response. Recommend: processor call agent directly. This is a 15-minute task blocking a $1.8M closing."
>
> Loan #2026-0855 (SBA 7(a), $750K, Bella's Bakery): SBA authorization received, but the TRID Closing Disclosure hasn't been sent — and regulations require 3 business days before closing. The agent flags: "TRID CD must be sent TODAY for Friday closing. Alerting processor and compliance."
>
> Each alert includes the specific action needed, the person responsible, and the consequence of inaction. The operations manager reviews the dashboard and assigns follow-ups in under 10 minutes.

---

### Use Case 5: Reconciliation & Settlement Operations

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Reconciliation is the plumbing of banking operations — unglamorous but absolutely critical. Every day, banks must reconcile their internal records against external sources: Fed/correspondent bank statements, ATM/debit card settlement files, ACH batches, wire transfer logs, general ledger sub-accounts, and intercompany transfers. A mid-size bank performs 50-200 reconciliations monthly, each involving matching thousands of transactions and investigating discrepancies ("breaks"). Reconciliation analysts spend 70%+ of their time on matching (which should be automated) and only 30% on investigating actual breaks. Most banks use a combination of Excel, legacy reconciliation tools (BlackLine, Trintech), and manual processes. The risk of unreconciled accounts is severe: a $2M reconciliation break that goes uninvestigated could mask fraud, operational errors, or system failures.

#### The Solution
monday.com Work Management as the reconciliation operations tracker. Each reconciliation is an item with columns for: account/reconciliation name, type (Nostro, DDA, GL, Card Settlement, ACH, Wire, Intercompany), frequency (Daily, Weekly, Monthly), assigned analyst, status (Not Started, In Progress, Matched, Breaks Identified, Under Investigation, Complete, Certified), due date, break count, break dollar amount, completion date, and certifier. Subitems represent individual breaks requiring investigation. Automations enforce deadlines, escalate overdue reconciliations, and prevent certification without break resolution. The board doesn't replace the reconciliation matching tool — it manages the workflow around it.

#### The Outcome
Reconciliation completion rate improves from 85% to 99%+ on-time. Break resolution time decreases by 50% with structured investigation workflows. Audit and examination preparation becomes trivial — complete history of every reconciliation and break resolution. Management gains real-time visibility into which reconciliations are complete, which have outstanding breaks, and which are at risk.

#### Discovery Questions
1. "How many reconciliations does your team perform monthly, and what percentage are completed on time?"
2. "When breaks are identified, what's the average time to investigate and resolve them?"
3. "How do you currently track reconciliation completion and break status — is it in the reconciliation tool, a separate tracker, or both?"
4. "Has your bank ever had a regulatory finding related to untimely or incomplete reconciliations?"
5. "What's the largest reconciliation break your team has dealt with, and how was it discovered?"

#### Industry Context
Bank reconciliation is a fundamental internal control required by banking regulators. Nostro reconciliations (correspondent bank accounts) must be performed daily for active accounts. General ledger reconciliations are typically monthly. Card settlement reconciliations (Visa/Mastercard settlement files vs. core banking) are daily. The OCC's Comptroller's Handbook explicitly requires banks to have "effective reconciliation processes" as part of internal controls. SOX Section 404 requires management to certify the effectiveness of internal controls, and reconciliation is a primary control for financial statement accuracy. "Stale items" — unresolved breaks older than 30/60/90 days — are a common examination finding and can result in MRAs. Leading practices include dual-review certification (analyst completes, manager certifies) and aging-based escalation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Reconciliation Operations Tracker for a bank. Create a board called 'Reconciliation Management' with these columns: Reconciliation Name (text), Account/GL Number (text), Reconciliation Type (dropdown: Nostro/Correspondent, DDA Control, General Ledger, Card Settlement, ACH Settlement, Wire Settlement, Intercompany, ATM, Suspense Account), Frequency (dropdown: Daily, Weekly, Monthly, Quarterly), Assigned Analyst (people), Certifier (people), Period (text, e.g. 'Jan 2026'), Due Date (date), Status (status: Not Started, In Progress, Matching Complete, Breaks Under Investigation, Pending Certification, Certified, Overdue), Break Count (numbers), Break Dollar Amount (numbers), Stale Items Count (numbers, breaks >30 days), Completion Date (date), and Certification Date (date). Groups: organize by Reconciliation Type. Add subitems for each break: Break Description (text), Break Amount (numbers), Break Date (date), Investigation Status (status: New, Investigating, Root Cause Identified, Resolved, Escalated), Root Cause (dropdown: Timing Difference, Processing Error, System Error, Fraud Suspected, Duplicate Entry, Missing Entry, Other), Resolution Notes (long text), Resolved Date (date), and Resolved By (people). Automations: (1) When Due Date arrives and Status is not 'Certified', change to 'Overdue' and notify Operations Manager; (2) When Status changes to 'Pending Certification' and Break Count is greater than 0, notify Certifier with break details; (3) When all break subitems are Resolved, update Break Count to 0 and notify Analyst; (4) When any break subitem Investigation Status is 'New' for more than 48 hours, notify Assigned Analyst. Dashboard: reconciliation completion rate (percentage widget), overdue reconciliations (table, red), break aging (chart: 0-7, 8-14, 15-30, 30+ days), total outstanding break dollars (numbers widget), completion by type (stacked bar), and analyst workload (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Reconciliation Intelligence Hub
**Agent Purpose:** Monitor reconciliation completion, investigate break patterns, predict issues, and ensure every reconciliation is completed, reviewed, and certified on time.

**Triggers:**
- New reconciliation period begins (based on frequency schedule)
- Reconciliation due date approaching (3 days, 1 day)
- Break identified during reconciliation
- Break aging exceeds 30 days (stale item threshold)
- Monthly reconciliation performance review

**Actions:**
- Auto-create reconciliation items for each new period based on the master schedule
- Analyze break patterns across periods (recurring breaks suggest systemic issues)
- Prioritize breaks by dollar amount and age for analyst investigation
- Generate "stale items" report for management and audit with root cause analysis
- Produce monthly reconciliation scorecard with completion rates, break statistics, and trend analysis
- Flag reconciliations where break volume or dollar amounts significantly deviate from historical norms

**Data Required:**
- Master reconciliation schedule (account list, frequencies, assignments)
- Historical reconciliation results (completion rates, break counts, resolution times)
- Transaction data for break investigation context
- GL balances and sub-ledger details
- Regulatory requirements for reconciliation timing by account type

**Autonomy Level:** Fully Autonomous (scheduling and monitoring) / Human-in-the-Loop (break investigation)
Period creation, deadline monitoring, and pattern analysis are automated. Break investigation assistance is advisory. Certification always requires human sign-off. Fraud-suspected breaks immediately escalate to BSA/AML and management.

**Example Interaction:**
> The Reconciliation Intelligence Hub detects an unusual pattern in the ACH Settlement reconciliation: the daily break count has averaged 12 items ($45K) over the past two weeks, compared to the historical average of 2-3 items ($8K). Drilling into the break details, the agent identifies that 80% of the new breaks involve ACH credits from a single originator — a payroll processing company.
>
> The agent generates an alert: "ACH Settlement — Anomalous Break Pattern. Break volume increased 4x over 14 days. Root cause hypothesis: payroll originator (PayRight Solutions) may have changed their file format or batch timing, causing matching failures. Breaks are all timing-related (credits posted T+1 instead of same-day). Recommended actions: (1) Contact PayRight Solutions operations to confirm format/timing change, (2) Update matching rules if confirmed, (3) Resolve 14-day backlog of breaks as timing differences once root cause confirmed."
>
> The analyst confirms the hypothesis — PayRight migrated to a new processing platform two weeks ago — updates the matching rules, and clears the 168 accumulated breaks in one batch. Without the pattern detection, each break would have been investigated individually, consuming approximately 30 analyst-hours.

---

### Use Case 6: BSA/AML Operations & Suspicious Activity Monitoring

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
BSA/AML (Bank Secrecy Act/Anti-Money Laundering) operations is one of the most resource-intensive functions in banking. Banks must monitor every customer transaction for suspicious activity, file SARs (Suspicious Activity Reports) with FinCEN within 30 days of detection, maintain a comprehensive CTR (Currency Transaction Report) filing program for cash transactions over $10,000, conduct enhanced due diligence on high-risk customers, and screen all transactions against OFAC sanctions lists. A mid-size bank's BSA team may review 500-2,000 transaction monitoring alerts per month, of which 10-20% result in SAR filings. The remainder are false positives that still require documentation of the investigation and rationale for clearing. BSA teams are chronically understaffed — experienced BSA analysts command premium salaries, and the work is detail-intensive with zero tolerance for errors. A single missed SAR filing can result in millions in fines.

#### The Solution
monday.com Work Management as the BSA/AML case management workflow layer. Each alert from the transaction monitoring system becomes an item with columns for: alert type (Structuring, Unusual Activity, OFAC Hit, High-Risk Customer Review, CTR Filing, 314(b) Request), customer name, account, alert date, assigned analyst, investigation status (New, Under Investigation, Escalated to BSA Officer, SAR Decision Pending, SAR Filed, Cleared-No SAR, Closed), investigation deadline, SAR filing deadline (if applicable), investigation narrative, and supporting documentation. Automations enforce the 30-day SAR filing deadline, balance analyst workloads, and ensure no alert goes uninvestigated. Dashboards provide the BSA Officer with real-time program metrics.

#### The Outcome
Alert investigation time decreases by 30% with structured workflows and historical case reference. SAR filing deadline compliance reaches 100%. BSA team capacity increases by 25% through workload balancing and automation of routine tasks. Regulatory examination readiness improves — every investigation is fully documented with clear audit trail. False positive documentation time drops significantly with standardized clearing templates.

#### Discovery Questions
1. "How many transaction monitoring alerts does your BSA team review monthly, and what's the SAR conversion rate?"
2. "Have you ever come close to or missed a SAR filing deadline?"
3. "How do you currently track BSA cases — is it in the transaction monitoring system, a separate case management tool, or spreadsheets?"
4. "What's your average investigation time per alert, and how does that vary between simple false positives and complex SAR cases?"
5. "During your last BSA/AML examination, what findings or recommendations did the examiners make about your investigation process?"

#### Industry Context
The BSA/AML regulatory framework is the most consequential compliance obligation in banking. FinCEN requires banks to file SARs within 30 calendar days of detecting suspicious activity (60 days if no suspect is identified). CTRs must be filed within 15 calendar days of a cash transaction exceeding $10,000. Banks must have a risk-based BSA/AML program that includes: a system of internal controls, independent testing, a designated BSA officer, and training. Transaction monitoring systems (Actimize, Verafin, SAS, Oracle Financial Crime) generate alerts based on rule-based and machine learning models, but the investigation is manual. The "alert-to-SAR" pipeline is examined intensely by regulators — they review case files, investigation quality, timeliness, and the decision rationale for both SARs and cleared alerts. Consent orders related to BSA/AML failures are among the most publicized and costly in banking (TD Bank: $3B fine in 2024, Capital One: $390M, Deutsche Bank: $186M).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a BSA/AML Case Management Tracker for a bank's compliance operations. Create a board called 'BSA/AML Case Management' with these columns: Case ID (text), Alert Type (dropdown: Structuring, Unusual Activity, Rapid Movement of Funds, OFAC Screening Hit, High-Risk Customer Review, CTR Exception, 314(b) Request, Law Enforcement Subpoena, Internal Referral), Customer Name (text), Account Number(s) (text), Alert Source (dropdown: Transaction Monitoring System, Manual Referral, Law Enforcement, Internal Audit, Regulatory Exam), Alert Date (date), Assigned Analyst (people), Investigation Status (status: New, Under Investigation, Additional Info Requested, Escalated to BSA Officer, SAR Decision Pending, SAR Filed, Cleared-No SAR Warranted, Closed), Investigation Deadline (date), SAR Filing Deadline (date), SAR Number (text), Investigation Narrative (long text), Supporting Documents (files), Suspicious Amount (numbers), Risk Level (status: Low, Medium, High, Critical), and Reviewer/BSA Officer (people). Groups: organize by Investigation Status. Create automations: (1) When SAR Filing Deadline is within 5 days and SAR Number is empty and Investigation Status is not 'Cleared', notify BSA Officer urgently; (2) When Investigation Status is 'New' for more than 48 hours, notify Assigned Analyst and BSA Officer; (3) When Investigation Status changes to 'SAR Filed', log SAR Number and filing date; (4) When Alert Date is set, auto-calculate Investigation Deadline (Alert Date + 25 days) and SAR Filing Deadline (Alert Date + 30 days). Dashboard: open cases by status (pie chart), cases approaching SAR deadline (table, sorted by urgency), monthly SAR filing volume (bar chart), average investigation time (numbers widget), analyst caseload distribution (chart), and alert-to-SAR conversion rate (percentage widget)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BSA Case Accelerator
**Agent Purpose:** Streamline BSA/AML alert investigation by providing historical context, suggesting investigation paths, and ensuring no filing deadline is missed.

**Triggers:**
- New alert ingested from transaction monitoring system
- Investigation deadline approaching (10 days, 5 days, 2 days)
- SAR filing deadline approaching
- Customer appears in multiple open cases
- Monthly BSA program metrics review

**Actions:**
- Enrich new alerts with customer history (prior SARs, CTRs, previous alerts and dispositions)
- Suggest investigation focus areas based on alert type and historical patterns
- Generate investigation narrative templates pre-populated with transaction details and customer context
- Flag cases where the same customer or account appears across multiple alerts (link related cases)
- Produce monthly BSA program dashboard for BSA Officer and Board reporting
- Track and report on examiner commitments related to BSA/AML findings

**Data Required:**
- Transaction monitoring alerts and underlying transaction data
- Customer profile and account information
- Historical SAR and CTR filings
- Previous case investigations and dispositions
- OFAC/SDN list and screening results
- FinCEN advisories and guidance
- 314(b) information sharing requests and responses

**Autonomy Level:** Human-in-the-Loop (all investigation and filing decisions require human review)
Alert enrichment and narrative drafting are automated. Investigation paths are advisory only. SAR/no-SAR decisions require BSA analyst investigation and BSA Officer sign-off. OFAC hits require immediate human review. No autonomous filing or clearing of alerts.

**Example Interaction:**
> A new alert arrives: Customer John Martinez, personal checking account, flagged for "Structuring — Cash Deposits Below $10K Threshold." The transaction monitoring system identified 14 cash deposits of $9,200-$9,800 over the past 45 days totaling $134,600.
>
> The BSA Case Accelerator enriches the alert: "Customer Profile: John Martinez, account opened 2019, occupation listed as 'restaurant owner.' Prior alerts: 1 (June 2024, Unusual Activity — cleared, no SAR — reason: legitimate business deposits consistent with declared occupation). Prior CTRs: 3 in 2025. Related accounts: business checking for 'Martinez Family Restaurant LLC' — shows declining card payment revenue over same 45-day period, potentially explaining shift to cash deposits."
>
> The agent drafts an investigation template: "The declining card revenue concurrent with increased cash deposits is notable. Potential explanations: (1) POS system change driving more cash transactions, (2) seasonal shift to cash-heavy catering/events, or (3) commingling of funds from undisclosed business activity. Recommended investigation steps: (1) Review deposit slip images for source documentation, (2) Compare cash deposit patterns to restaurant's known operating hours, (3) Check business account for corresponding expense patterns, (4) Consider customer interview if patterns remain unexplained."
>
> The analyst uses this framework to conduct the investigation efficiently, documents the findings, and makes the SAR/no-SAR determination — all within the 30-day window and with a comprehensive, examiner-ready case file.

---

### Use Case 7: Operational Risk & Incident Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking operations generates a steady stream of incidents — system outages, processing errors, fraud events, vendor failures, and near-misses — that must be captured, investigated, root-caused, and reported. Operational risk management requires tracking these incidents for Basel III/IV operational risk capital calculations, regulatory reporting, and internal risk committee reviews. Most banks below the top 20 manage operational risk incidents in spreadsheets or basic ticketing systems that don't connect to the workflows where incidents actually occur. The result: underreporting of incidents (because logging them is painful), poor root cause analysis (because there's no structured process), and recurring incidents (because lessons learned aren't systematically captured or acted upon).

#### The Solution
monday.com Work Management as the operational risk incident tracker, connected to the operational workflows where incidents originate. Each incident is an item with columns for: incident type (Processing Error, System Outage, Fraud Event, Vendor Failure, Regulatory Breach, Data Error, Security Incident), severity (Critical, High, Medium, Low), financial impact, affected customers, root cause category, business line, assigned investigator, status (Reported, Investigating, Root Cause Identified, Remediation in Progress, Closed, Monitoring), remediation actions, and lessons learned. Automations enforce investigation timelines, escalate high-severity incidents to the Chief Risk Officer, and generate Board-level risk reports.

#### The Outcome
Incident reporting rates increase as the logging process becomes frictionless (directly from operational boards). Root cause analysis completion improves from 40% to 90%+. Recurring incidents decrease as lessons learned drive process improvements. Board and regulatory reporting is automated rather than manually compiled. Operational risk capital calculations are better supported with comprehensive incident data.

#### Discovery Questions
1. "How does your bank currently capture and track operational risk incidents — is there a formal process?"
2. "What percentage of operational incidents do you estimate actually get reported and documented?"
3. "When the same type of incident recurs, do you have a systematic way to identify the pattern and address the root cause?"
4. "How do you produce the operational risk reports for your Board and risk committee?"
5. "Has your bank experienced an operational loss event that surprised leadership because it wasn't visible in your risk reporting?"

#### Industry Context
Basel III/IV requires banks to hold capital against operational risk losses. The Standardized Measurement Approach (SMA) uses a combination of historical loss data and business indicators to calculate operational risk capital. Banks must maintain a comprehensive operational loss database, and regulators examine the completeness and accuracy of this data. Operational risk events are categorized per Basel: Internal Fraud, External Fraud, Employment Practices, Clients/Products/Business Practices, Damage to Physical Assets, Business Disruption/System Failures, and Execution/Delivery/Process Management. The last category — execution and process management — is the most common in banking operations and includes: transaction capture errors, failed mandatory reporting, negligent loss of client assets, and vendor/outsourcing failures. The OCC's Heightened Standards (12 CFR 30, Appendix D) require large banks to have comprehensive operational risk management frameworks.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Operational Risk & Incident Management system for a bank. Create a board called 'Operational Risk Incidents' with these columns: Incident ID (text), Incident Type (dropdown: Processing Error, System Outage, Fraud Event-Internal, Fraud Event-External, Vendor/Third-Party Failure, Regulatory Breach, Data/Privacy Incident, Physical Security, Business Disruption, Near Miss), Basel Category (dropdown: Internal Fraud, External Fraud, Employment Practices, Clients Products Business Practices, Physical Asset Damage, Business Disruption System Failure, Execution Delivery Process Management), Severity (status: Critical, High, Medium, Low), Date Discovered (date), Date Occurred (date), Business Line (dropdown: Retail Banking, Commercial Banking, Wealth Management, Treasury, Payments, Mortgage, Operations), Financial Impact (numbers), Customers Affected (numbers), Description (long text), Root Cause Category (dropdown: Process Failure, System Error, Human Error, Vendor Failure, External Event, Policy Gap, Training Gap), Assigned Investigator (people), Status (status: Reported, Investigating, Root Cause Identified, Remediation In Progress, Closed, Monitoring), Remediation Actions (long text), Lessons Learned (long text), and Reported to Regulator (checkbox). Groups: organize by Severity. Automations: (1) When Severity is 'Critical', immediately notify CRO, COO, and Compliance; (2) When Status is 'Reported' for more than 24 hours, notify Assigned Investigator; (3) When Financial Impact exceeds $100K, set Reported to Regulator flag and notify Legal; (4) When Status changes to 'Closed' and Lessons Learned is empty, revert to 'Remediation In Progress'. Dashboard: incidents by type (bar chart), monthly incident trend (line chart), total financial impact (numbers widget), open incidents by severity (pie chart), root cause distribution (chart), and incidents by business line (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Operational Risk Sentinel
**Agent Purpose:** Detect operational risk patterns, ensure incident investigation completeness, and generate risk intelligence for leadership and regulatory reporting.

**Triggers:**
- New incident reported
- Incident severity is Critical or High
- Financial impact exceeds threshold ($50K, $100K, $500K)
- Similar incident type recurs within 30 days
- Quarterly operational risk report due

**Actions:**
- Classify incidents by Basel category and suggest root cause investigation areas
- Detect recurring incident patterns and recommend systemic remediation
- Generate quarterly operational risk reports with trend analysis, loss summaries, and key risk indicators
- Cross-reference incidents with compliance findings to identify control weaknesses
- Draft regulatory notifications for reportable events
- Create remediation tracking items with milestones and accountability

**Data Required:**
- Incident database (current and historical)
- Basel categorization taxonomy
- Control framework documentation
- Regulatory reporting thresholds and requirements
- Business line organizational structure
- Compliance findings and examination results

**Autonomy Level:** Human-in-the-Loop
Incident classification and pattern detection are automated. Root cause suggestions are advisory. Regulatory notifications require legal and compliance review. Risk reports require CRO sign-off before distribution.

**Example Interaction:**
> The Operational Risk Sentinel detects a pattern: over the past 60 days, there have been 7 incidents classified as "Processing Error" in the Wire Operations unit — up from an average of 1-2 per quarter. Five of the seven involve international wires where the intermediary bank field was populated incorrectly, causing delays and one instance of misdirected funds ($47K, since recovered). Total financial impact: $3,200 in wire fees and compensation, plus an estimated 40 analyst-hours in investigation and remediation.
>
> The agent generates a risk intelligence brief: "Emerging Risk — International Wire Processing Errors. Root cause analysis across 7 incidents reveals: (1) 5 of 7 errors occurred during the 2-6 PM shift when junior analysts process the majority of international wires, (2) the intermediary bank lookup in the wire platform requires manual entry from a static PDF reference list last updated 8 months ago, (3) two correspondent banking relationships changed intermediary requirements in Q4 2025 that were not reflected in the reference list.
>
> Recommended remediation: (1) Update intermediary bank reference list immediately and establish quarterly review cadence, (2) Implement four-eyes review for international wires over $25K, (3) Request wire platform vendor to add intermediary bank validation against SWIFT directory, (4) Provide targeted training to 2-6 PM shift on international wire processing. Estimated risk reduction: 80%+ of similar errors prevented."
>
> The CRO reviews the brief, approves the remediation plan, and the agent creates four tracked action items with owners and deadlines. The pattern — invisible when incidents were tracked individually — is now a managed risk with accountability.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ACH | Automated Clearing House — electronic funds transfer network for direct deposits, bill payments, and batch transactions |
| BSA/AML | Bank Secrecy Act / Anti-Money Laundering — federal regulations requiring banks to detect and report suspicious activity |
| SAR | Suspicious Activity Report — filed with FinCEN when a bank detects potentially criminal activity |
| CTR | Currency Transaction Report — filed for cash transactions exceeding $10,000 |
| KYC/CDD | Know Your Customer / Customer Due Diligence — identity verification and risk assessment requirements |
| OFAC | Office of Foreign Assets Control — administers sanctions programs; banks must screen all transactions |
| SDN List | Specially Designated Nationals list — OFAC's list of blocked persons and entities |
| Nostro Account | A bank's account held at a correspondent bank in a foreign currency (used for international transactions) |
| Reconciliation Break | A discrepancy between two records that should match (internal vs. external, GL vs. sub-ledger) |
| SLA | Service Level Agreement — contractual processing time commitments |
| LOS | Loan Origination System — software managing the loan application through funding process |
| TRID | TILA-RESPA Integrated Disclosure — rules governing timing and content of mortgage disclosures |
| CAMELS Rating | Regulatory rating system: Capital adequacy, Asset quality, Management, Earnings, Liquidity, Sensitivity |
| MRA | Matter Requiring Attention — regulatory examination finding requiring corrective action |
| MRIA | Matter Requiring Immediate Attention — urgent regulatory finding requiring immediate remediation |
| Core Banking System | The central system processing transactions and maintaining customer accounts (Fiserv, FIS, Jack Henry) |
| Wire Transfer | Real-time, irrevocable electronic funds transfer between banks (Fedwire, SWIFT) |
| Basel III/IV | International regulatory framework for bank capital, liquidity, and risk management |
| OCC | Office of the Comptroller of the Currency — primary regulator for national banks |
| FinCEN | Financial Crimes Enforcement Network — administers BSA and collects SARs/CTRs |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Operations Officer (COO) | Owns all banking operations functions, P&L, and transformation agenda | Decision-maker |
| VP/SVP of Operations | Manages day-to-day operations teams (deposits, loans, wires, reconciliation) | Decision-maker |
| BSA Officer | Responsible for the bank's BSA/AML compliance program | Decision-maker (BSA) |
| Chief Risk Officer (CRO) | Owns operational risk framework, capital allocation, and risk reporting | Influencer / Decision-maker |
| Chief Compliance Officer (CCO) | Oversees regulatory compliance across all functions | Decision-maker (compliance) |
| Operations Manager | Front-line management of operations analysts and processors | Influencer / User |
| Operations Analyst | Processes exceptions, reconciliations, account openings, and investigations | Primary User |
| Internal Audit Director | Tests operational controls and reports findings to the Board | Influencer |
| CIO/CTO | Owns technology stack including core banking and integration platforms | Decision-maker (technology) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Operations depends on IT for core banking, integrations, and system reliability | Joint operations + IT workflow for incident management and change control |
| Compliance | Operations executes many compliance requirements; Compliance sets the rules | Unified compliance task tracking across both functions |
| Lending/Credit | Loan operations is the execution arm of the lending function | End-to-end loan lifecycle visibility from origination through servicing |
| Retail Banking (Branches) | Branches originate transactions that operations processes | Branch-to-operations handoff workflows (account openings, wire requests) |
| Treasury | Treasury manages the bank's liquidity and funding; Operations executes wire transfers and settlements | Real-time settlement and funding coordination |
| Finance | Finance depends on reconciled, accurate operational data for financial reporting | Automated reconciliation feeds into financial close process |
| HR | Operations has high headcount and turnover; HR manages staffing and training | Workforce planning and training tracking for operations teams |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| ServiceNow | Enterprise workflow automation, strong in IT operations | Overbuilt and expensive for banking operations; requires heavy implementation. monday.com delivers 80% of the value at 20% of the cost and time. |
| Appian/Pega | Business process management (BPM) platforms popular in banking | Powerful but require developer resources to configure; monday.com's no-code approach empowers operations teams directly. |
| Spreadsheets/Email | The de facto "system" for exception tracking, reconciliation management, and compliance tasks at most mid-size banks | monday.com replaces spreadsheet chaos with structured, auditable workflows — critical for regulatory compliance. |
| nCino | Banking-specific platform focused on lending and account opening | Strong in lending workflow but limited to front-office; doesn't address back-office operations, reconciliation, or BSA. monday.com covers the full operations spectrum. |
| BlackLine/Trintech | Financial close and reconciliation automation | Purpose-built for reconciliation matching but poor at the workflow layer (who, what, when). monday.com complements or replaces the workflow management layer. |
| Verafin/Actimize | Transaction monitoring and BSA/AML case management | Excellent at alert generation but case management workflows are often rigid. monday.com provides a flexible workflow layer on top of the monitoring system. |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We can't put bank data in a cloud platform — regulatory risk" | monday.com is SOC 2 Type II certified, supports data encryption at rest and in transit, and is used by hundreds of financial institutions. We can configure data handling to meet your information security policies, and sensitive data like account numbers can be tokenized or excluded. |
| "Our core banking system should handle all of this" | Core banking systems are transaction engines — they're brilliant at processing but terrible at workflow management, collaboration, and visibility. monday.com doesn't replace your core; it's the orchestration layer that makes your operations team more effective around the core. |
| "We already have ServiceNow/Appian" | Those are powerful enterprise platforms that require IT resources to configure and maintain. monday.com empowers your operations managers to build and modify workflows themselves, in days not months. Many banks use both — enterprise platforms for IT, monday.com for business operations. |
| "Our examiners want to see purpose-built compliance tools" | Examiners care about outcomes: are you tracking commitments? Are deadlines met? Is there an audit trail? monday.com delivers all of this with clear documentation. Several banks have successfully demonstrated monday.com-based compliance tracking during examinations. |
| "We need on-premise deployment" | We understand the sensitivity. monday.com's enterprise plan offers advanced security controls, SSO, audit logs, and compliance certifications. For specific regulatory requirements, let's discuss your security team's needs — most banks find that cloud controls meet or exceed their on-premise environment. |
| "Operations staff won't adopt another tool" | That's a valid concern — tool fatigue is real. monday.com succeeds because it's intuitive (minimal training needed) and it removes work rather than adding it. When analysts see their exception queue organized, their reconciliations tracked, and their status updates automated, adoption follows naturally. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for banking operations efficiency case study]
- [Placeholder for compliance tracking success story]
- [Placeholder for loan operations cycle time improvement]
- [Placeholder for reconciliation management reference]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
