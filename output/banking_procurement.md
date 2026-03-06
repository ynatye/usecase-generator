# Banking × Procurement Playbook

## Overview

Procurement in banking is a uniquely complex function operating at the intersection of cost management, regulatory compliance, vendor risk management, and operational resilience. Banking procurement departments — often called Sourcing, Vendor Management, or Third-Party Risk Management (TPRM) — are responsible for managing thousands of vendor relationships that collectively represent billions in annual spend. A mid-size regional bank might manage 2,000-4,000 active vendor contracts; a large Tier 1 institution could have 10,000-15,000. The scope ranges from IT infrastructure and software licensing to professional services, facilities management, marketing agencies, and specialized financial data providers.

What makes banking procurement fundamentally different from procurement in other industries is the regulatory overlay. The OCC (Office of the Comptroller of the Currency), Federal Reserve, FDIC, and CFPB all have explicit guidance on third-party risk management. OCC Bulletin 2023-17 (updated from 2013-29) establishes a comprehensive framework requiring banks to conduct risk assessments, due diligence, and ongoing monitoring for all third-party relationships — with heightened requirements for "critical activities" that could cause significant harm to customers or the bank. Failure to comply can result in enforcement actions, consent orders, and material findings in regulatory examinations.

The procurement team in banking is therefore not just a cost center managing RFPs and purchase orders — it's a critical risk management function. Every vendor onboarding triggers a multi-stage due diligence process involving information security assessments (SOC reports, penetration testing results), financial viability reviews, business continuity plan evaluation, regulatory compliance verification, and often board-level reporting for critical vendors. The average time to onboard a new vendor in banking ranges from 60-120 days, creating significant friction for business units that need to move quickly. This tension between speed-to-value and regulatory rigor is the central challenge banking procurement teams face daily.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Vendor portfolio growing 10-15% annually while procurement/TPRM headcount stays flat; regulatory requirements intensifying |
| 2 | Consolidate Tech Stack with AI | High | Banks average 4-7 separate tools for procurement, vendor management, contract management, and risk assessment |
| 3 | Replace or Radically Augment Headcount | Medium-High | AI can automate risk assessments, contract reviews, and ongoing monitoring that currently require analyst headcount |

## Prioritized Use Cases

---

### Use Case 1: Third-Party Risk Management (TPRM) Lifecycle

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Banking regulators require comprehensive third-party risk management across the entire vendor lifecycle: planning, due diligence, contract negotiation, ongoing monitoring, and termination. Most banks manage this through a combination of spreadsheets, shared drives, email, and perhaps a GRC (Governance, Risk & Compliance) tool that's poorly adopted. The result is a fragmented process where risk assessments go stale, periodic reviews are missed, and the TPRM team spends more time chasing documentation than actually analyzing risk. When examiners ask "show me your ongoing monitoring for your top 50 critical vendors," the team scrambles for days to compile the evidence. With vendor portfolios growing and regulatory expectations intensifying (especially around fourth-party/concentration risk), the current manual approach is unsustainable.

#### The Solution
monday.com as the operational command center for TPRM. Build a Vendor Registry board with comprehensive risk metadata. Create automated workflows for risk assessment scheduling, document collection, review assignments, and escalation. Use dashboards to provide real-time visibility into TPRM program health — overdue assessments, upcoming reviews, risk distribution, and concentration analysis. Connect to the contract management system for term tracking and renewal alerts.

#### The Outcome
Reduce vendor risk assessment cycle time by 50%. Achieve 100% on-time completion of periodic vendor reviews. Create instant examiner-ready TPRM reporting. Free up 30-40% of TPRM analyst time from administrative tasks to focus on actual risk analysis. Eliminate "surprise" findings during regulatory examinations.

#### Discovery Questions
1. "When your OCC or state examiner last reviewed your third-party risk management program, what findings or recommendations did they have, and how confident were you in the completeness of your documentation?"
2. "How many vendors are currently classified as 'critical' under OCC 2023-17, and what does your ongoing monitoring process look like for each?"
3. "What's your current average time from vendor selection to fully onboarded and approved? How much of that time is the due diligence and approval process vs. actual implementation?"
4. "How do you currently track fourth-party risk — meaning the critical subcontractors and cloud providers your vendors depend on?"
5. "If I asked you right now for a complete risk profile of your top 20 vendors — risk tier, last assessment date, outstanding issues, contract expiration — how long would it take to compile?"

#### Industry Context
OCC Bulletin 2023-17 (Interagency Guidance on Third-Party Relationships) is the gold standard for banking TPRM. It requires banks to assess risk across multiple domains: strategic, operational, compliance, financial, cyber, concentration, and reputational. "Critical activities" receive heightened scrutiny — these include activities that could cause significant harm to consumers, significant financial loss, or significant operational disruption. Banks must also assess fourth-party risk (their vendors' vendors), particularly for cloud services and data processing. Board reporting on TPRM is expected, and examiners will test the program during every examination cycle.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Third-Party Risk Management (TPRM) board for a bank. Columns: Vendor Name (text), Vendor ID (auto-number), Risk Tier (dropdown: Critical, High, Moderate, Low), Service Category (dropdown: IT Infrastructure, Software/SaaS, Professional Services, Financial Data, Payment Processing, Outsourced Operations, Marketing, Facilities, Consulting, Staffing), Business Owner (people), TPRM Analyst (people), Inherent Risk Score (numbers: 1-25), Residual Risk Score (numbers: 1-25), Last Risk Assessment (date), Next Assessment Due (date), Assessment Frequency (dropdown: Quarterly, Semi-Annual, Annual, Biennial), Due Diligence Status (status: Not Started, In Progress, Under Review, Approved, Expired, Remediation Required), SOC Report Status (dropdown: SOC 2 Type II Current, SOC 2 Type I Current, SOC 1 Current, Pending, Not Applicable, Expired), Financial Viability (status: Strong, Adequate, Watch, Concern), BCP Tested (dropdown: Yes - Current Year, Yes - Prior Year, No, N/A), Concentration Risk Flag (checkbox), Fourth-Party Dependencies (long text), Contract Expiration (date), Annual Spend (numbers), Regulatory Findings (numbers), Open Issues (numbers), Documents (files). Automations: when Next Assessment Due is within 30 days notify TPRM Analyst and Business Owner; when Due Diligence Status changes to 'Expired' change Risk Tier label to red and notify TPRM Manager; when SOC Report Status changes to 'Expired' create action item for analyst; when Concentration Risk Flag is checked notify Chief Risk Officer. Views: Dashboard with risk tier distribution pie chart, overdue assessments count, vendors by category, upcoming renewals timeline, total annual spend by risk tier. Table view filtered to Critical vendors only. Calendar view by Next Assessment Due."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorShield Risk Monitor
**Agent Purpose:** Continuously monitor vendor risk indicators, automate assessment workflows, and ensure zero-gap TPRM compliance across the entire vendor portfolio.

**Triggers:**
- Vendor risk assessment due date approaching (30, 14, 7 days)
- SOC report expiration detected
- Vendor financial news alert (credit downgrade, lawsuit, data breach)
- New regulatory guidance published affecting TPRM requirements
- Quarterly TPRM board reporting cycle
- New vendor onboarding request submitted

**Actions:**
- Generate pre-populated risk assessment templates based on vendor tier and service category
- Send automated document collection requests to vendors with specific requirements lists
- Monitor vendor SOC report expiration dates and trigger renewal requests 60 days in advance
- Scan public sources for vendor risk signals (financial distress, security incidents, regulatory actions)
- Calculate and update inherent/residual risk scores based on assessment data
- Generate board-ready TPRM summary reports with risk distribution, trends, and exceptions
- Escalate overdue assessments through management chain (analyst → manager → CISO → CRO)

**Data Required:**
- Vendor contract and assessment history
- OCC 2023-17 risk assessment framework
- Vendor financial data and credit ratings
- Public news and regulatory action feeds
- SOC report repository and expiration tracking

**Autonomy Level:** Escalation-Based
Agent autonomously manages scheduling, reminders, document collection, and reporting. Risk score changes and assessment results require human analyst review. Critical risk escalations (vendor breach, financial distress) are immediately routed to TPRM Manager and CISO with recommended actions.

**Example Interaction:**
> On a Monday morning, VendorShield generates the weekly TPRM dashboard update. It flags three items requiring attention: (1) CoreBridge Data Processing, a critical vendor handling the bank's core banking system, has a SOC 2 Type II report expiring in 45 days — the agent has already sent an automated request to CoreBridge's compliance team for the updated report with a 30-day deadline. (2) A financial news scan detected that MidState Technology Solutions, a moderate-risk IT services vendor, was named in a class-action data breach lawsuit filed last Friday — the agent has elevated MidState's risk tier from Moderate to High, created an urgent assessment task for the TPRM analyst, and drafted a letter to MidState requesting a formal incident report and remediation plan. (3) Twelve vendor assessments are due this quarter, and the agent has pre-populated assessment templates for each based on their tier and service category, assigned them to analysts based on workload, and sent initial document requests to the vendors. The TPRM Manager opens her monday.com dashboard to find everything organized, prioritized, and in motion — no manual triage required.

---

### Use Case 2: Vendor Onboarding & Due Diligence Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Vendor onboarding in banking is notoriously slow — 60 to 120 days is typical, with some critical vendors taking 6+ months. The process involves multiple parallel workstreams: information security assessment, financial due diligence, legal contract review, regulatory compliance verification, business continuity evaluation, and often board or committee approval for critical vendors. These workstreams are typically managed by different teams with different timelines and no unified view of overall progress. Business line sponsors grow frustrated as their strategic initiatives stall waiting for vendor approval. The procurement team becomes the bottleneck everyone blames but nobody helps resource adequately.

#### The Solution
monday.com as a Vendor Onboarding Pipeline with clear stage gates, parallel workstream tracking, and automated routing. Build a pipeline board that visualizes every vendor onboarding in progress, with sub-items for each due diligence workstream. Use automations to trigger workstream kickoffs in parallel (not sequential) where possible. Create SLA tracking for each stage with automated escalation. Provide business sponsors with self-service status visibility to eliminate "where's my vendor?" inquiries.

#### The Outcome
Reduce average vendor onboarding time by 40% (from 90 days to 54 days) through parallel processing and bottleneck elimination. Achieve 100% visibility for business sponsors without procurement team status update effort. Reduce procurement team administrative overhead by 35%. Create data-driven insights into which stages are true bottlenecks for process improvement.

#### Discovery Questions
1. "What's your current average time from vendor selection to approved-and-operational, and how does that compare to what your business lines expect?"
2. "When a vendor onboarding is in progress, how does the business sponsor check status — do they call you, email you, or can they see it themselves?"
3. "Which stage of your onboarding process is the biggest bottleneck — is it InfoSec assessment, legal review, financial due diligence, or committee approval?"
4. "How many vendor onboardings do you have in flight at any given time, and how do you track them all?"
5. "Have you ever had a situation where a vendor was operationally deployed before all due diligence was complete, creating a compliance gap?"

#### Industry Context
Banking vendor due diligence is multi-dimensional. Information Security assessment typically involves reviewing the vendor's SOC 2 report, penetration testing results, data encryption practices, incident response plan, and compliance with the bank's information security standards. Financial due diligence examines the vendor's financial stability — audited financial statements, credit ratings, insurance coverage — to ensure they won't go bankrupt mid-contract. Legal review covers contract terms including data ownership, liability, indemnification, subcontracting restrictions, audit rights, and regulatory examination access. For vendors handling customer data, additional reviews may include GLBA compliance, privacy impact assessment, and data residency requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Onboarding Pipeline board for a bank. Main item columns: Vendor Name (text), Requesting Department (dropdown: Retail Banking, Commercial Banking, Wealth Management, IT, Operations, Marketing, HR, Finance, Risk, Compliance), Business Sponsor (people), Procurement Lead (people), Service Description (long text), Estimated Annual Spend (numbers), Risk Tier Preliminary (dropdown: Critical, High, Moderate, Low), Onboarding Status (status: Intake, Due Diligence, Contract Negotiation, Committee Review, Approved, Onboarded, Rejected, On Hold), Target Go-Live Date (date), Submission Date (date), Days in Pipeline (formula: TODAY minus Submission Date), SLA Status (status: On Track, At Risk, Overdue). Create sub-items for each due diligence workstream: Workstream Name (text — e.g., InfoSec Assessment, Financial Review, Legal/Contract, BCP Review, Compliance Check, Privacy Assessment), Workstream Owner (people), Workstream Status (status: Not Started, Awaiting Vendor Docs, In Review, Issues Found, Approved, Waived), Due Date (date), Documents (files), Notes (long text). Automations: when main item status changes to 'Due Diligence' create all sub-item workstreams from template; when all sub-item statuses are 'Approved' or 'Waived' change main status to 'Contract Negotiation'; when Days in Pipeline exceeds 60 notify Procurement Director; when sub-item status changes to 'Issues Found' notify Business Sponsor. Views: Kanban by Onboarding Status, Gantt/Timeline view showing parallel workstreams, Dashboard with average days by stage, vendors in pipeline count, bottleneck analysis chart, and SLA compliance rate."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OnboardExpress Pipeline Accelerator
**Agent Purpose:** Eliminate onboarding delays by proactively managing vendor document collection, workstream coordination, and bottleneck resolution.

**Triggers:**
- New vendor onboarding request submitted
- Vendor document upload received
- Workstream overdue by more than 5 business days
- Business sponsor requests status update
- Vendor fails to respond to document request within 10 business days

**Actions:**
- Analyze vendor service description and auto-assign preliminary risk tier based on service category matrix
- Generate customized due diligence questionnaire based on risk tier and service type
- Send automated document collection requests to vendors with specific checklists
- Track document receipt and completeness, sending reminders at 7 and 14 days
- Identify workstream bottlenecks and suggest parallel processing opportunities
- Generate real-time status summaries for business sponsor inquiries
- Predict onboarding completion date based on current velocity and historical data for similar vendors
- Escalate stalled workstreams with specific context to appropriate management level

**Data Required:**
- Vendor onboarding requirements matrix by risk tier and service category
- Historical onboarding data (timelines, bottlenecks, completion rates)
- Due diligence checklist templates
- Reviewer capacity and workload data
- Vendor contact information and communication history

**Autonomy Level:** Human-in-the-Loop
Agent manages all coordination, communication, and tracking autonomously. Risk tier assignments, due diligence findings, and onboarding approvals require human review and sign-off. The agent accelerates the process around human decision points.

**Example Interaction:**
> A Product Manager in Commercial Banking submits a request to onboard FinanceAI Corp, a vendor providing AI-powered credit analysis tools that will process commercial loan applications. OnboardExpress analyzes the service description — AI, credit decisions, customer financial data — and assigns a preliminary risk tier of "Critical" based on the risk matrix (handles customer data + influences credit decisions + AI/algorithmic risk). It generates a comprehensive due diligence package: enhanced InfoSec assessment (requiring penetration test results, AI model governance documentation, and data handling practices), financial review (3 years of audited financials given the vendor is a startup), legal review with specific AI liability and model bias clauses, and a fair lending compliance assessment. The agent sends FinanceAI Corp a detailed document request with clear deadlines, kicks off all five workstreams in parallel with appropriate reviewers, and notifies the Business Sponsor: "Your vendor onboarding for FinanceAI Corp has been initiated as a Critical-tier engagement. Five parallel due diligence workstreams are in progress. Estimated completion: April 15 based on similar Critical-tier onboardings averaging 78 days. I'll update you weekly or immediately if issues arise." Two weeks in, the agent detects that the InfoSec team hasn't started their review due to backlog. It escalates to the CISO with context: "FinanceAI Corp InfoSec assessment has been queued for 14 days. This is a Critical-tier vendor with a target go-live of April 30. Request prioritization to maintain timeline."

---

### Use Case 3: Contract Lifecycle Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Banking vendor contracts are complex documents laden with regulatory-specific provisions — audit rights, examination access clauses, data residency requirements, subcontracting restrictions, business continuity commitments, and indemnification terms mandated by banking regulations. Most banks manage contracts through a combination of a contract management tool (often underutilized), shared drives, and the institutional memory of the legal and procurement teams. When a contract comes up for renewal, the team scrambles to locate the document, review terms, assess vendor performance, and determine negotiation strategy — often with inadequate time. Auto-renewals trigger because nobody tracked the termination notice window. Unfavorable terms persist because nobody remembers why they were accepted. Spend creep occurs because nobody monitors consumption against contracted rates.

#### The Solution
monday.com as the operational layer for contract lifecycle management. Build a Contract Registry board with all critical terms, dates, and obligations tracked as structured data (not buried in PDF documents). Use automations to trigger renewal workflows 180 days before expiration for critical vendors and 90 days for others. Create connected boards linking contracts to vendor performance data, spend analytics, and TPRM assessments. Use dashboards to provide CFO and CPO visibility into contract portfolio health.

#### The Outcome
Eliminate 100% of unintended auto-renewals through proactive alert management. Capture $500K-$2M annually in improved contract terms through systematic negotiation preparation. Reduce contract review time by 40% through pre-organized term tracking. Achieve complete regulatory compliance for contract documentation requirements.

#### Discovery Questions
1. "In the last year, how many vendor contracts auto-renewed that you wish you had renegotiated or terminated?"
2. "When a contract is up for renewal, how far in advance does your team typically begin the review process — and is that enough time?"
3. "Can you easily pull up the key terms of any vendor contract right now — termination notice periods, audit rights, data handling provisions — without opening the actual document?"
4. "How do you currently connect vendor performance data to contract renewal decisions?"
5. "During your last regulatory examination, were examiners satisfied with your contract documentation for critical vendors — specifically around audit rights and examination access clauses?"

#### Industry Context
Banking regulators have specific expectations for vendor contracts. OCC 2023-17 requires that contracts for critical activities include: performance measures, right to audit, regulatory examination access, reporting requirements, BCP provisions, subcontracting restrictions, data ownership and handling, confidentiality, indemnification, insurance requirements, dispute resolution, termination provisions, and default remedies. Missing any of these clauses in a critical vendor contract can result in an examination finding. Additionally, the GLBA (Gramm-Leach-Bliley Act) imposes data protection requirements that must be contractually passed through to vendors handling customer information.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Contract Lifecycle Management board for a bank's vendor contracts. Columns: Vendor Name (connect to Vendor Registry board), Contract ID (auto-number), Contract Type (dropdown: Master Services Agreement, Statement of Work, Software License, SaaS Subscription, Professional Services, Outsourcing Agreement, Data Services, NDA, Amendment), Effective Date (date), Expiration Date (date), Auto-Renewal (dropdown: Yes - 1 Year, Yes - 2 Year, No), Termination Notice Period (dropdown: 30 Days, 60 Days, 90 Days, 180 Days, 365 Days), Termination Notice Deadline (date — formula: Expiration minus Notice Period), Contract Status (status: Active, Renewal In Progress, Negotiation, Pending Signature, Expired, Terminated, On Hold), Annual Value (numbers), Total Contract Value (numbers), Risk Tier (mirror from Vendor Registry), Business Owner (people), Procurement Lead (people), Legal Reviewer (people), Audit Rights Clause (checkbox), Examination Access Clause (checkbox), BCP Requirements (checkbox), Data Handling Terms (checkbox), Subcontracting Restrictions (checkbox), GLBA Compliance Clause (checkbox), Regulatory Clause Completeness (formula: count of checked regulatory clauses / 6), Contract Document (files), Renewal Decision (dropdown: Renew As-Is, Renew with Renegotiation, Competitive Bid, Terminate, Consolidate). Automations: when Termination Notice Deadline is within 30 days and Contract Status is 'Active' notify Procurement Lead and Business Owner urgently; when Expiration Date is within 180 days and Risk Tier is 'Critical' change status to 'Renewal In Progress'; when Regulatory Clause Completeness is less than 100% and Risk Tier is 'Critical' notify Legal Reviewer. Views: Timeline view of contract expirations, Dashboard with total contract value, upcoming expirations, regulatory clause compliance rate, contracts by type and risk tier, and spend distribution chart."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ContractIQ Lifecycle Manager
**Agent Purpose:** Proactively manage the entire contract lifecycle — from renewal preparation through negotiation support — ensuring zero missed deadlines and maximum value capture.

**Triggers:**
- Contract reaches renewal preparation window (180 days for Critical, 90 days for others)
- Termination notice deadline approaching (30 days warning)
- Vendor performance review completed (to inform renewal strategy)
- New regulatory guidance affecting contract requirements published
- Contract item status changed to "Renewal In Progress"

**Actions:**
- Generate renewal preparation package: contract summary, key terms, historical spend analysis, vendor performance scorecard, and market benchmarking data
- Identify missing regulatory clauses by comparing contract terms against current OCC requirements
- Recommend renewal strategy (renew, renegotiate, competitive bid, terminate) based on vendor performance, market conditions, and strategic alignment
- Draft negotiation talking points highlighting areas for improvement (pricing, SLAs, regulatory compliance gaps)
- Track termination notice deadlines and send escalating alerts (60, 30, 14, 7 days)
- Generate executive summary for contracts requiring committee or board approval
- Flag auto-renewal contracts approaching the decision point with risk-adjusted recommendations

**Data Required:**
- Contract terms and documents
- Vendor performance metrics and TPRM assessments
- Historical spend data and market rate benchmarks
- OCC 2023-17 contract requirements checklist
- Vendor relationship history and negotiation notes

**Autonomy Level:** Human-in-the-Loop
Agent prepares all renewal materials and recommends strategy autonomously. Renewal decisions, negotiation positions, and contract approvals require human sign-off. The agent ensures no deadline is missed and every decision is data-informed.

**Example Interaction:**
> ContractIQ detects that the bank's $4.2M annual contract with DataStream Analytics — a critical vendor providing market data feeds to the trading desk — enters its 180-day renewal window. The agent immediately generates a comprehensive renewal package: the contract summary shows a 3-year agreement with a 90-day termination notice window and 5% annual escalator; the spend analysis reveals actual usage has grown 22% year-over-year, exceeding contracted volumes and triggering overage charges totaling $380K last year; the vendor performance scorecard shows 99.7% uptime (meeting SLA) but 3 unresolved support tickets averaging 45 days to resolution; and the TPRM assessment (completed last quarter) shows Moderate risk with one open finding related to incomplete disaster recovery testing. The agent recommends "Renew with Renegotiation" and drafts talking points: (1) restructure pricing to accommodate volume growth and eliminate overage exposure — suggest tiered pricing with a cap, (2) add SLA penalties for support ticket resolution exceeding 72 hours, (3) require DR test completion and reporting within 60 days as a contract condition. It also flags that the current contract is missing the updated OCC examination access language required since the 2023 guidance update. The Procurement Lead reviews the package, adds two additional negotiation points, and enters the renewal meeting fully prepared — a process that previously took 3 weeks of manual preparation completed in minutes.

---

### Use Case 4: Procurement Request & Sourcing Pipeline

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Procurement requests in banking arrive through multiple channels — email, tickets, phone calls, hallway conversations with the CFO. There's no standardized intake process, making it impossible to see total demand, prioritize effectively, or identify consolidation opportunities. The same software category might be independently sourced by three different business units, each negotiating their own deal with different vendors. Without visibility into the pipeline, procurement can't provide strategic value — they're perpetually reactive, processing transactions rather than driving savings and risk reduction.

#### The Solution
monday.com as a Procurement Request Portal with structured intake forms, automated routing, and pipeline management. Build intake forms that capture business need, budget, timeline, and risk considerations upfront. Use automations to categorize requests, identify potential vendor consolidation opportunities, and route to appropriate procurement specialists. Create pipeline dashboards showing total demand, projected spend, and sourcing status.

#### The Outcome
Capture 100% of procurement demand through a single intake channel. Identify 10-15% savings opportunities through demand consolidation. Reduce procurement cycle time by 30% through standardized processes. Enable strategic category management with complete demand visibility.

#### Discovery Questions
1. "How do business units currently submit procurement requests — is there a single intake process, or does it vary?"
2. "Do you have visibility into total procurement demand across the organization, or do requests surface ad hoc?"
3. "In the last year, have you discovered that multiple business units were independently purchasing similar solutions from different vendors?"
4. "How do you currently prioritize procurement requests when demand exceeds your team's capacity?"

#### Industry Context
Banking procurement operates under additional constraints including concentration risk limits (regulators may question over-reliance on a single vendor), diversity and inclusion sourcing requirements (CRA-related), and heightened security scrutiny for any vendor touching customer data or financial systems. Many banks have category-specific procurement specialists (IT procurement, professional services procurement, facilities procurement) but lack an integrated view across categories. The rise of SaaS and fintech partnerships has dramatically increased the volume of technology procurement requests while shrinking the typical deal size — creating more transactions with less leverage.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Procurement Request Pipeline for a bank. Create an intake form with: Requester (people), Department (dropdown: Retail, Commercial, Wealth, IT, Operations, Marketing, HR, Finance, Risk, Compliance, Legal, Executive), Request Type (dropdown: New Vendor, Contract Renewal, Additional Services from Existing Vendor, Emergency/Sole Source, RFP/Competitive Bid), Category (dropdown: IT Hardware, Software/SaaS, Professional Services, Financial Data, Payment Processing, Facilities, Marketing Services, Staffing/Consulting, Office Supplies, Other), Description (long text), Business Justification (long text), Estimated Annual Value (numbers), Budget Approved (checkbox), Desired Start Date (date), Priority (dropdown: Critical - Regulatory Deadline, High - Revenue Impact, Medium - Operational, Low - Nice to Have), Data Classification (dropdown: Customer PII, Financial Data, Internal Only, Public). Board columns: Request ID (auto-number), Pipeline Stage (status: Submitted, Under Review, Sourcing, Evaluation, Negotiation, Approval, PO Issued, Complete, Rejected, On Hold), Procurement Specialist (people), Category Manager (people), Potential Vendors (text), Consolidation Opportunity (checkbox), Savings Identified (numbers), Days in Pipeline (formula), SLA Status (status: On Track, At Risk, Overdue). Automations: when form submitted notify Category Manager based on Category; when Estimated Annual Value > $100K require Category Manager approval before proceeding; when Data Classification is 'Customer PII' auto-flag for enhanced security review; when Consolidation Opportunity checked notify Strategic Sourcing Director. Views: Kanban by Pipeline Stage, Dashboard with request volume by department, projected spend in pipeline, savings identified YTD, and average cycle time by category."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SourceSmart Procurement Advisor
**Agent Purpose:** Analyze incoming procurement requests to identify savings opportunities, consolidation plays, and optimal sourcing strategies based on institutional data and market intelligence.

**Triggers:**
- New procurement request submitted
- Multiple requests in the same category within a 30-day window
- Contract renewal entering pipeline for existing vendor
- Quarterly strategic sourcing review cycle

**Actions:**
- Analyze new requests against existing vendor portfolio to identify consolidation opportunities
- Flag duplicate or similar purchases across departments
- Recommend sourcing strategy (sole source justification, competitive bid, piggyback on existing contract)
- Estimate market pricing based on historical data and benchmarks
- Identify preferred vendors in the bank's approved vendor list for the relevant category
- Generate category spend analysis for strategic sourcing reviews
- Draft RFP templates customized to the service category with banking-specific requirements

**Data Required:**
- Historical procurement data (vendors, categories, spend, timelines)
- Active vendor and contract registry
- Market rate benchmarks by category
- Department budget allocations and approval hierarchies

**Autonomy Level:** Human-in-the-Loop
Agent provides analysis and recommendations for all requests. Procurement specialists make sourcing decisions and manage vendor interactions. The agent surfaces opportunities that humans would miss due to information silos.

**Example Interaction:**
> The Risk department submits a procurement request for a new regulatory change management software platform, estimated at $200K annually. SourceSmart immediately cross-references the request against the vendor portfolio and recent procurement activity. It discovers: (1) the Compliance department purchased a similar regulatory tracking tool 8 months ago for $150K/year from a different vendor, (2) the Legal department has a pending request for contract analytics software that overlaps in functionality, and (3) the bank's existing GRC platform vendor offers a regulatory change module that could be added for $80K/year. The agent flags all three findings and recommends consolidating the three needs into a single RFP that could yield 30-40% savings through volume leverage while reducing the vendor portfolio. It drafts a consolidation proposal for the Strategic Sourcing Director, including a meeting request with the three department heads to align requirements.

---

### Use Case 5: Vendor Performance Management & Scorecard

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Banking regulators expect ongoing monitoring of vendor performance, not just point-in-time assessments. Yet most banks have no systematic way to track vendor performance beyond anecdotal feedback. SLA adherence data lives in IT monitoring tools. Service quality feedback lives in email threads. Cost performance data lives in finance systems. When it's time for a contract renewal or vendor review, the procurement team conducts a flurry of stakeholder interviews and data gathering that yields incomplete, subjective results. Poor-performing vendors continue to be renewed because nobody aggregated the evidence. High-performing vendors don't get recognized, missing opportunities to deepen strategic relationships.

#### The Solution
monday.com as a Vendor Performance Management platform. Build automated scorecards that aggregate performance data from multiple sources into a single vendor health view. Create structured feedback collection from business stakeholders. Use dashboards to identify performance trends, at-risk relationships, and top performers. Connect performance data to contract renewal workflows for evidence-based negotiation.

#### The Outcome
Establish objective, data-driven vendor performance baselines for 100% of critical vendors. Reduce vendor performance review preparation from weeks to hours. Improve vendor accountability through transparent, consistent measurement. Enable 15-20% improvement in vendor performance through systematic issue identification and remediation.

#### Discovery Questions
1. "Do you have a standardized vendor scorecard today, and if so, how consistently is it applied across your vendor portfolio?"
2. "When a business user has a problem with a vendor, how does that feedback reach the procurement team — and does it influence the next contract renewal?"
3. "Can you quickly identify your top 5 best-performing and bottom 5 worst-performing vendors based on objective data?"
4. "How do your vendor SLAs connect to actual monitoring — if a vendor misses an SLA, do you know about it in real-time, or at the quarterly review?"

#### Industry Context
OCC guidance requires banks to monitor vendor performance across several dimensions: quality of service, compliance with contract terms, financial condition, internal controls (via SOC reports), information security posture, business continuity readiness, and ability to meet regulatory requirements. For critical vendors, this monitoring should be continuous, not periodic. The concept of "vendor concentration risk" means that even high-performing vendors warrant scrutiny if the bank is overly dependent on them — what happens if they fail? Banks must also monitor for "subcontracting drift" — vendors increasingly outsourcing contracted activities to fourth parties without adequate notification.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Performance Scorecard board for a bank. Columns: Vendor Name (connect to Vendor Registry), Review Period (dropdown: Q1 2026, Q2 2026, Q3 2026, Q4 2026), Reviewer (people), Overall Score (numbers: 1-100), Service Quality (numbers: 1-100), SLA Compliance (numbers: 1-100), Responsiveness (numbers: 1-100), Cost Performance (numbers: 1-100), Innovation (numbers: 1-100), Compliance & Risk (numbers: 1-100), Performance Trend (status: Improving, Stable, Declining, New), Incidents This Period (numbers), SLA Breaches (numbers), Open Issues (numbers), Stakeholder Satisfaction (dropdown: Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied), Strengths (long text), Improvement Areas (long text), Action Items (long text), Escalation Required (checkbox), Files (files). Automations: when Overall Score below 60 notify Procurement Director and set Escalation Required; when Performance Trend is 'Declining' for 2 consecutive periods notify Category Manager; when review period changes create new scorecard items for all Critical and High-tier vendors. Views: Dashboard with average scores by vendor, trend charts over time, bottom performers table, score distribution histogram, and incidents/SLA breach tracking."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorPulse Performance Tracker
**Agent Purpose:** Continuously aggregate vendor performance signals from across the bank and generate real-time scorecards that feed into contract and relationship decisions.

**Triggers:**
- Quarterly scorecard review cycle begins
- SLA breach detected in monitoring systems
- Vendor incident ticket created in service management system
- Stakeholder feedback survey response received
- Contract renewal entering preparation window (connects performance to negotiation)

**Actions:**
- Aggregate SLA performance data from monitoring systems into scorecard metrics
- Collect and synthesize stakeholder feedback through automated survey distribution
- Calculate composite performance scores with weighted dimensions based on vendor tier
- Generate trend analysis comparing current period to historical performance
- Identify vendors with declining performance trajectories and recommend intervention
- Produce contract renewal performance summary linking scorecard data to negotiation strategy
- Flag vendors with consistently high scores for strategic partnership consideration

**Data Required:**
- SLA monitoring data from IT operations tools
- Service ticket/incident data from ITSM platform
- Historical scorecard data for trend analysis
- Stakeholder contact lists for feedback collection
- Contract terms and SLA definitions for compliance calculation

**Autonomy Level:** Fully Autonomous for data collection and scoring; Human-in-the-Loop for action decisions
Agent automatically collects data, calculates scores, identifies trends, and generates reports. Performance improvement actions, vendor escalations, and strategic recommendations require human approval.

**Example Interaction:**
> VendorPulse begins the Q1 2026 scorecard cycle for the bank's 47 Critical and High-tier vendors. For each vendor, it pulls the quarter's data: SLA compliance from the IT monitoring dashboard, incident ticket count and resolution times from ServiceNow, and distributes satisfaction surveys to 2-3 business stakeholders per vendor. Within 5 business days, 42 of 47 scorecards are complete (5 awaiting stakeholder responses — the agent sends reminders). The standout finding: Meridian Payment Systems, the bank's card processing vendor, has dropped from 88 to 71 over two consecutive quarters, driven by a spike in processing errors (SLA compliance dropped from 99.8% to 98.1%) and deteriorating support responsiveness (average ticket resolution increased from 4 hours to 18 hours). VendorPulse flags this as "Declining — Intervention Required," links the scorecard data to the upcoming contract renewal (8 months away), and recommends the Procurement team initiate a formal performance improvement plan now to establish leverage for renewal negotiations. It drafts a performance improvement letter citing specific data points and schedules a review meeting with the business owner and vendor relationship manager.

---

### Use Case 6: Spend Analytics & Category Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most banking procurement teams lack a comprehensive view of third-party spend. Data is fragmented across accounts payable systems, purchasing card programs, expense reports, and shadow IT subscriptions. Without visibility, procurement can't identify consolidation opportunities, negotiate volume discounts, or spot maverick spending (purchases made outside procurement channels). In banking, uncontrolled spend also creates unmanaged vendor relationships — and unmanaged vendor relationships create regulatory risk. Every dollar spent with an unapproved vendor is a potential compliance gap.

#### The Solution
monday.com as a Spend Analytics and Category Management dashboard. Build a centralized spend tracking system that aggregates data from AP, P-card, and subscription management tools. Create category management boards for strategic spend categories with spend targets, savings goals, and vendor strategy. Use dashboards to visualize spend patterns, identify outliers, and track savings achievement.

#### The Outcome
Achieve 100% spend visibility across procurement channels. Identify 8-12% savings opportunities through consolidation, renegotiation, and demand management. Reduce maverick spending by 60% through process visibility. Improve regulatory posture by linking spend to approved vendor registry.

#### Discovery Questions
1. "What percentage of your total third-party spend do you believe flows through your procurement process vs. being purchased directly by business units?"
2. "Can you quickly identify your top 20 vendors by spend and how that spend has trended over the past 3 years?"
3. "How do you currently identify and manage SaaS subscriptions and recurring technology spend across departments?"
4. "When your CFO asks for a breakdown of third-party spend by category, how long does it take to produce that analysis?"

#### Industry Context
Banking third-party spend is increasingly dominated by technology — SaaS subscriptions, cloud infrastructure, data services, and fintech partnerships. This creates unique challenges: subscriptions auto-renew, usage-based pricing makes costs unpredictable, and individual business units can purchase SaaS tools without procurement involvement (shadow IT). In banking, shadow IT isn't just a cost issue — it's a compliance issue. An unapproved SaaS tool processing customer data creates an unmanaged third-party relationship that violates OCC guidance. Category management for banking technology spend requires understanding not just cost but risk, data handling, and regulatory implications.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Spend Analytics & Category Management board for a bank. Columns: Category (dropdown: IT Infrastructure, Software/SaaS, Professional Services, Financial Data/Market Data, Payment Processing, Outsourced Operations, Facilities, Marketing, Staffing/Consulting, Office/Supplies, Travel, Insurance, Audit/Advisory), Annual Spend (numbers), Budget (numbers), Variance (formula: Spend minus Budget), Vendor Count (numbers), Contract Count (numbers), Avg Contract Value (formula: Annual Spend / Contract Count), Top Vendor (text), Top Vendor Spend % (numbers), Concentration Risk (status: Acceptable, Monitor, High), Savings Target (numbers), Savings Achieved (numbers), Savings Attainment (formula: Achieved / Target as %), Category Manager (people), Strategy (dropdown: Leverage, Strategic, Bottleneck, Routine — Kraljic matrix), Last Reviewed (date), Next Review (date), Notes (long text). Add a connected sub-board for individual vendor spend lines: Vendor Name (text), Monthly Spend (numbers), YTD Spend (numbers), Prior Year Spend (numbers), YoY Change (formula), Department (dropdown), Approved Vendor (checkbox), Contract in Place (checkbox). Automations: when Concentration Risk changes to 'High' notify Chief Procurement Officer; when Savings Attainment exceeds 100% notify Category Manager with celebration; when Approved Vendor is unchecked create flag for procurement review. Dashboard: total third-party spend, spend by category donut chart, savings achievement gauge, top 20 vendors by spend bar chart, YoY spend trend, maverick spend (unapproved vendor) total."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SpendLens Analytics Engine
**Agent Purpose:** Continuously analyze third-party spend patterns to surface savings opportunities, flag compliance risks, and support strategic category management decisions.

**Triggers:**
- Monthly AP data refresh
- New vendor spend line exceeding $50K without approved vendor flag
- Quarterly category management review cycle
- Annual budget planning cycle
- CFO or CPO spend report request

**Actions:**
- Aggregate and categorize spend data from AP, P-card, and subscription tracking systems
- Identify duplicate spend (same category, different vendors, different departments)
- Flag maverick spending (purchases from unapproved vendors or without contracts)
- Generate category spend reports with trend analysis and benchmarking
- Recommend consolidation opportunities based on vendor overlap analysis
- Calculate realized savings and forecast remaining savings pipeline
- Produce executive-ready spend dashboards and category strategy recommendations

**Data Required:**
- Accounts payable transaction data
- P-card/corporate card transaction data
- SaaS subscription management data
- Approved vendor registry
- Contract terms and pricing data
- Market benchmark pricing data

**Autonomy Level:** Fully Autonomous for analysis; Human-in-the-Loop for action
Agent automatically analyzes, categorizes, and reports on all spend data. Savings recommendations, vendor consolidation proposals, and maverick spending interventions require human approval.

**Example Interaction:**
> During the monthly analysis cycle, SpendLens identifies an anomaly: four separate departments (IT, Risk, Compliance, and Operations) are each paying for data analytics/visualization tools from three different vendors — Tableau, Power BI, and Looker — totaling $890K in annual spend. The IT department's enterprise Power BI license has capacity for 500 additional users but only 60% of seats are utilized. SpendLens generates a consolidation proposal: standardize on the existing enterprise Power BI license, migrate the 45 Tableau and 28 Looker users onto available Power BI seats, and negotiate a volume expansion with Microsoft for the incremental licenses needed. Projected savings: $520K annually (58% reduction) with an estimated 3-month migration timeline. The agent drafts the business case, identifies the stakeholders in each department who would need to approve the migration, and queues the proposal for the next Strategic Sourcing Committee meeting.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| TPRM | Third-Party Risk Management — comprehensive program for managing vendor/supplier risk |
| OCC 2023-17 | Interagency guidance on third-party relationships — the regulatory gold standard for banking vendor management |
| Critical Activity | Vendor service that could cause significant harm to consumers, financial loss, or operational disruption — triggers heightened due diligence |
| Fourth-Party Risk | Risk from your vendors' vendors — particularly cloud providers and subcontractors |
| Concentration Risk | Over-reliance on a single vendor or small number of vendors for critical services |
| SOC Report | System and Organization Controls report — independent assessment of vendor's internal controls (SOC 1, SOC 2 Type I/II) |
| GLBA | Gramm-Leach-Bliley Act — requires financial institutions to protect customer information, including when shared with vendors |
| Maverick Spending | Purchases made outside of established procurement channels, bypassing approval and vendor management processes |
| Kraljic Matrix | Strategic purchasing model categorizing spend into Leverage, Strategic, Bottleneck, and Routine quadrants |
| GRC | Governance, Risk & Compliance — category of tools used for enterprise risk management including vendor risk |
| Category Management | Strategic approach to procurement that groups similar purchases for volume leverage and vendor optimization |
| BCP | Business Continuity Plan — vendor's plan for maintaining service during disruption; banks must validate for critical vendors |
| RFP/RFI | Request for Proposal/Information — formal sourcing process documents |
| SLA | Service Level Agreement — contractual performance commitments (uptime, response time, resolution time) |
| Shadow IT | Technology purchased directly by business units without IT or procurement involvement |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Procurement Officer (CPO) | Oversees enterprise procurement strategy, vendor management, and spend optimization | Decision-maker |
| VP of Third-Party Risk Management | Leads the TPRM program, ensures regulatory compliance for all vendor relationships | Decision-maker |
| Category Manager | Manages strategic sourcing for assigned spend categories | Influencer/Decision-maker for category |
| Procurement Analyst/Specialist | Executes sourcing processes, manages vendor onboarding documentation | User (key champion) |
| Chief Risk Officer (CRO) | Ultimate accountability for enterprise risk including third-party risk | Decision-maker (executive sponsor) |
| Chief Information Security Officer (CISO) | Approves vendor information security assessments | Decision-maker (veto on security) |
| General Counsel / Chief Legal Officer | Reviews and approves vendor contract terms | Decision-maker (contract authority) |
| CFO / Finance Leadership | Controls spend budgets, approves major purchases | Decision-maker (budget authority) |
| Business Line Sponsor | Internal customer requesting vendor services | User/Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Largest procurement spend category; IT procurement often operates semi-independently | IT project management, asset management, and service desk workflows |
| Legal | Reviews all vendor contracts; manages regulatory compliance language | Legal matter management and contract workflow automation |
| Finance | Manages AP, budgets, and spend reporting that feeds procurement analytics | Financial planning, budget management, and AP automation workflows |
| Risk / Compliance | Owns enterprise risk framework that TPRM operates within | Enterprise risk management, regulatory change tracking, and audit management |
| Information Security | Conducts technical security assessments for all vendors handling sensitive data | Security operations, incident management, and vulnerability tracking |
| Operations | Major consumer of outsourced services and vendor-provided operational tools | Operations management, process tracking, and quality management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SAP Ariba / Coupa | Enterprise procurement suites — powerful but complex, expensive, and slow to implement | monday.com offers faster time-to-value, better user adoption, and flexibility for the TPRM workflows that rigid procurement suites handle poorly |
| ServiceNow VRM | Vendor Risk Management module within ServiceNow ecosystem | monday.com provides better cross-functional collaboration (procurement + legal + risk + business) and more intuitive workflow design without ServiceNow's complexity and cost |
| Archer (RSA) / MetricStream | GRC platforms with TPRM modules | These tools are powerful for risk professionals but poorly adopted by procurement and business users. monday.com complements or replaces the operational workflow layer with a tool people actually use |
| OneTrust / Prevalent | Specialized TPRM platforms with automated assessment capabilities | monday.com serves as the operational orchestration layer — managing the workflow around risk assessments rather than replacing the assessment tools themselves |
| Icertis / Agiloft | Contract Lifecycle Management platforms | monday.com handles the operational workflow of contract management (tracking, alerts, collaboration) at a fraction of the cost and implementation time |
| Excel / SharePoint | The default "system" in most mid-size banks | monday.com replaces the spreadsheet-and-email approach with structured, automated, auditable workflows — a massive leap for banks still managing TPRM manually |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have SAP Ariba / Coupa for procurement" | "Those are excellent transactional procurement tools, but they're weak on the risk management and cross-functional collaboration workflows that regulators increasingly demand. Banks need a platform where procurement, legal, risk, and InfoSec can collaborate on vendor lifecycle management — not just process purchase orders. monday.com fills the gap between your procurement suite and your GRC tool." |
| "Our GRC platform (Archer/ServiceNow) already handles vendor risk" | "GRC platforms are built for risk professionals, not for the procurement team, business sponsors, and vendors who need to participate in the process. Adoption is the #1 challenge in TPRM — if people don't use the tool, your risk program has gaps. monday.com provides the intuitive operational layer that drives adoption while feeding data to your GRC system of record." |
| "Banking regulators require specific TPRM capabilities — can monday.com meet those requirements?" | "monday.com serves as the operational workflow and collaboration layer for TPRM — managing assessments, tracking documentation, automating reminders, and providing reporting. It complements specialized risk assessment tools while ensuring the process around those assessments is complete, timely, and auditable. Banks that implement monday.com for TPRM workflows consistently report improved examination readiness." |
| "We need a contract management system, not a project management tool" | "Contract lifecycle management isn't about storing PDFs — it's about managing the workflow around contracts: renewals, approvals, performance connections, regulatory compliance tracking. monday.com manages the operational lifecycle that standalone CLM tools often miss — the human processes, cross-team coordination, and decision workflows that determine whether contracts serve the bank's interests." |
| "Our procurement team is too small to justify a platform investment" | "Small teams have the most to gain. A 5-person procurement team managing 3,000 vendor relationships can't afford manual processes — one missed renewal or expired SOC report creates regulatory risk. monday.com gives a small team enterprise-grade vendor management capabilities through automation, eliminating the administrative burden that prevents them from doing strategic work." |

## Proof Points
*(To be populated with customer references)*
- [Banking institution using monday.com for vendor risk management]
- [Financial services procurement team consolidating workflows]
- [Regulated industry achieving compliance improvements through automated vendor monitoring]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
