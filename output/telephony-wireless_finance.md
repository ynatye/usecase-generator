# Telephony & Wireless × Finance Playbook

## Overview

Finance teams in telephony and wireless companies operate in one of the most complex financial environments across all industries. Unlike traditional businesses, telecom finance must navigate intricate revenue models spanning postpaid/prepaid subscribers, wholesale partnerships, roaming agreements, and infrastructure investments. These teams manage massive scale — often millions of subscribers generating billions in revenue through dozens of revenue streams including service plans, device sales, interconnect fees, roaming charges, and regulatory compliance costs.

The regulatory landscape adds significant complexity, with teams managing multi-jurisdiction tax compliance, Universal Service Fund (USF) contributions, E-911 fees, and spectrum licensing costs that can run into billions. Finance must also balance enormous CapEx investments in network infrastructure (towers, 5G rollouts, fiber) against OpEx operational costs, while maintaining precise revenue recognition under ASC 606 for contract modifications and device subsidies. The rise of MVNOs, wholesale partnerships, and infrastructure sharing agreements has created additional layers of revenue sharing and settlement complexity.

Modern telecom finance teams typically operate with 15-50 professionals across revenue assurance, billing operations, financial planning & analysis (FP&A), tax, and regulatory compliance. They must deliver monthly closes within days while managing thousands of vendor relationships, processing millions of interconnect billing records, and maintaining real-time visibility into ARPU trends, churn impact, and subscriber lifetime value across multiple product lines and geographic markets.

## Value Driver Mapping

| Value Driver | Relevance | Why It Resonates |
|-------------|-----------|------------------|
| **Replace or Radically Augment Headcount** | **High** | Revenue assurance, interconnect billing, and regulatory compliance require armies of analysts to process TAP/RAP files, validate roaming settlements, and ensure billing accuracy across millions of transactions daily |
| **Consolidate Tech Stack with AI** | **Medium-High** | Finance teams juggle 10-15 systems: billing platforms, revenue assurance tools, interconnect clearing, tax engines, FP&A software, BI tools — AI can unify these workflows |
| **Scale Impact Without Overhead** | **High** | Network expansion, 5G rollouts, and subscriber growth create exponential data complexity, but finance headcount can't scale at the same rate due to margin pressure |

## Prioritized Use Cases

---

### Use Case 1: Revenue Assurance & Leakage Detection

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Revenue assurance teams manually analyze millions of CDRs (call detail records), billing system outputs, and network data to identify revenue leakage. This process requires 5-10 FTEs working around the clock to detect billing discrepancies, unbilled usage, and system errors that can cost carriers $50-200M annually. Traditional rules-based systems create thousands of false positives, while sophisticated leakage patterns go undetected.

#### The Solution
monday AI Agents continuously monitor billing accuracy by analyzing CDR patterns, comparing network usage to billing records, and identifying revenue leakage in real-time. The system uses mondayDB to unify network, billing, and customer data, while AI agents automatically investigate discrepancies, categorize issues, and escalate high-value leakage to human analysts. Vibe-built dashboards provide real-time visibility into revenue assurance metrics.

#### The Outcome
Reduce revenue leakage by 40-60%, eliminate 80% of manual CDR analysis, and redeploy 3-5 revenue assurance analysts to strategic initiatives. Typical telecom carriers recover $10-30M annually in previously undetected leakage.

#### Discovery Questions
- How many CDRs does your billing system process monthly, and what percentage requires manual review?
- What's your estimated revenue leakage percentage, and how do you currently detect billing system errors?
- How many FTEs are dedicated to revenue assurance, and what's their biggest time sink?
- Do you have real-time visibility into interconnect billing accuracy, or do discrepancies surface weeks later?
- What percentage of your revenue assurance alerts turn out to be false positives?

#### Industry Context
Revenue assurance in telecom is uniquely complex due to real-time usage rating, complex tariff structures, and interconnect billing with hundreds of carriers. Unlike other industries, every call, text, and data session must be accurately rated and billed, with errors potentially affecting regulatory compliance and partner relationships.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Revenue Assurance Command Center with these components: a 'Leakage Alerts' board with columns for Alert ID (auto-number), Alert Type (dropdown: CDR Mismatch, Billing Error, Interconnect Discrepancy, Usage Not Billed, System Failure), Severity (dropdown: Critical, High, Medium, Low), Amount Impact (currency), Network Element (text), Customer Segment (dropdown: Postpaid, Prepaid, Enterprise, Roaming), Investigation Status (status: Open, In Progress, Resolved, False Positive), Assigned Analyst (people), Date Detected (date), Resolution Date (date), and Root Cause (long text). Add automations to notify the Revenue Assurance Manager when Critical alerts are created, and auto-assign alerts based on Alert Type. Include a dashboard view showing daily leakage trends, alert volume by type, and resolution time metrics. Add a timeline view for tracking investigation progress."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Revenue Leakage Detective

**Agent Purpose:**  
Continuously monitor billing accuracy and automatically detect revenue leakage across all network elements and customer segments.

**Triggers:**
- New CDR batch processing completion
- Billing system cycle completion
- Interconnect settlement file arrival
- Network element alarm generation
- Weekly ARPU variance detection

**Actions:**
- Analyze CDR-to-bill matching accuracy
- Compare network usage counters to billing records
- Flag unbilled usage patterns
- Investigate interconnect settlement discrepancies
- Generate leakage impact assessments
- Escalate critical issues to analysts

**Data Required:**
- CDR feeds from network elements
- Billing system outputs
- Interconnect TAP/RAP files
- Network usage counters
- Customer account data
- Historical leakage patterns

**Autonomy Level:** Human-in-the-Loop  
Agent automatically detects and investigates potential leakage but escalates findings above $10K impact or when manual validation is needed.

**Example Interaction:**
> The Revenue Leakage Detective processes overnight CDR files and discovers that 12,000 international calls to premium destinations were rated at domestic rates due to a tariff table error. It calculates the revenue impact at $89,000, creates a critical alert, assigns it to the senior revenue assurance analyst, and automatically updates the billing system to prevent future occurrences. The agent continues monitoring similar patterns and identifies that this issue affects three other rate plans, expanding the total impact to $340,000. It escalates to the Revenue Assurance Manager with a detailed root cause analysis and recommended corrective actions.

---

### Use Case 2: Interconnect Billing & Settlement Automation

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Interconnect billing requires processing thousands of TAP (Transferred Account Procedure) and RAP (Returned Account Procedure) files monthly from roaming and settlement partners. Finance teams spend 3-5 FTEs manually validating these files, identifying discrepancies, raising disputes, and managing settlement processes. Partner billing cycles are often misaligned, creating cash flow timing issues and requiring extensive reconciliation work.

#### The Solution
monday AI Agents automatically process TAP/RAP files, validate interconnect charges against rate agreements, identify billing disputes, and manage the entire settlement workflow. The system integrates with clearing houses and partner systems, automatically generating dispute files and tracking resolution status. mondayDB provides unified visibility across all interconnect relationships.

#### The Outcome
Automate 85% of interconnect billing validation, reduce settlement cycle times from 45 to 15 days, and redeploy 2-3 FTEs to strategic carrier negotiations. Improve cash flow through faster dispute resolution and eliminate 90% of manual TAP/RAP processing.

#### Discovery Questions
- How many interconnect partners do you settle with monthly, and what volume of TAP/RAP files?
- What percentage of your interconnect billing requires manual dispute resolution?
- How long is your average settlement cycle, and what creates the biggest delays?
- Do you have real-time visibility into your interconnect payables and receivables?
- What's your current process for validating roaming charges against negotiated rates?

#### Industry Context
Interconnect settlement is unique to telecommunications, involving complex file formats (TAP3.12), clearing house relationships, and international carrier agreements. The process requires deep knowledge of GSM/UMTS/LTE roaming protocols and regulatory compliance across multiple jurisdictions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Interconnect Settlement Management system with a 'Partner Settlements' board containing: Settlement ID (auto-number), Partner Name (dropdown with major carriers), Settlement Period (date range), TAP Files Received (number), RAP Files Processed (number), Total Charges (currency), Disputed Amount (currency), Settlement Status (status: Processing, Validation, Dispute, Approved, Paid), File Validation (status: Pending, Pass, Fail, Partial), Dispute Count (number), Due Date (date), Payment Date (date), and Assigned Processor (people). Create automations to notify finance team when disputes exceed $50K and alert the CFO when settlements are overdue by 30+ days. Add a dashboard showing monthly settlement volumes, dispute trends, and aging analysis. Include a Kanban view for tracking settlement workflow stages."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Interconnect Settlement Processor

**Agent Purpose:**  
Automatically process, validate, and settle interconnect billing with roaming and wholesale partners.

**Triggers:**
- TAP/RAP file arrival from partners
- Settlement due date approaching
- Dispute response received
- Rate agreement updates
- Monthly settlement cycle initiation

**Actions:**
- Validate TAP/RAP file formats and content
- Compare charges against rate agreements
- Identify billing discrepancies and disputes
- Generate dispute files (RAP format)
- Calculate settlement amounts
- Update partner settlement tracking

**Data Required:**
- Interconnect rate agreements
- TAP/RAP file feeds
- Partner contact information
- Historical settlement patterns
- Clearing house interfaces
- Currency exchange rates

**Autonomy Level:** Fully Autonomous  
Agent handles standard validation and settlement processes automatically, escalating only disputes above $100K or technical validation failures.

**Example Interaction:**
> The Interconnect Settlement Processor receives 47 TAP files from Vodafone UK representing £2.3M in roaming charges. It automatically validates file structures, compares rates against the interconnect agreement, and identifies £89K in overcharges for premium SMS services. The agent generates a RAP dispute file, updates the settlement tracking board with disputed amounts, and notifies the Wholesale Finance Manager. Simultaneously, it processes clean settlements totaling £2.21M, initiates payment approval workflows, and schedules automatic reconciliation once payment is confirmed. The entire process completes in 12 minutes versus the previous 4-hour manual validation cycle.

---

### Use Case 3: ARPU Forecasting & Subscriber Revenue Analytics

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
ARPU (Average Revenue Per User) forecasting requires analyzing millions of subscriber records across multiple segments (postpaid, prepaid, enterprise), service plans, device types, and geographic regions. Finance teams manually build complex models to predict ARPU trends, churn impact, and revenue forecasts for monthly board reports. The process requires 2-3 weeks of analyst time and lacks real-time visibility into subscriber behavior changes.

#### The Solution
AI agents continuously analyze subscriber usage patterns, billing data, and market trends to generate real-time ARPU forecasts by segment. The system identifies early churn indicators, predicts revenue impact of promotional campaigns, and automatically updates financial models as new data arrives. Vibe-built dashboards provide executive visibility into key metrics.

#### The Outcome
Generate ARPU forecasts in hours versus weeks, improve forecast accuracy by 25-35%, and enable real-time revenue optimization decisions. Finance teams can focus on strategic analysis rather than data compilation.

#### Discovery Questions
- How do you currently calculate and forecast ARPU across different subscriber segments?
- What's your typical forecast accuracy for quarterly ARPU predictions?
- How quickly can you identify and quantify the impact of subscriber behavior changes?
- Do you have real-time visibility into ARPU trends by geography, plan type, or device?
- What percentage of your FP&A time is spent on data gathering versus analysis?

#### Industry Context
ARPU is the primary KPI for telecom investors and directly impacts company valuation. Unlike other industries, ARPU must account for complex factors like device subsidies, plan migrations, usage-based billing, and regulatory fee pass-throughs that can significantly distort simple revenue-per-customer calculations.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an ARPU Analytics Dashboard with a 'Subscriber Segments' board including: Segment ID (auto-number), Segment Name (dropdown: Postpaid, Prepaid, Enterprise, MVNO), Current ARPU (currency), Prior Month ARPU (currency), ARPU Change % (percentage), Subscriber Count (number), Total Revenue (currency), Churn Rate % (percentage), New Activations (number), Plan Migration Impact (currency), Device Subsidy Impact (currency), Forecast Next Month (currency), Forecast Confidence (dropdown: High, Medium, Low), Last Updated (date), and Analyst Owner (people). Add automations to alert the CFO when any segment ARPU drops >5% month-over-month and notify FP&A when forecast confidence falls below Medium. Include a dashboard with ARPU trend lines, segment comparison charts, and churn correlation analysis. Create a timeline view for monthly ARPU progression tracking."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ARPU Forecast Engine

**Agent Purpose:**  
Continuously analyze subscriber data to generate accurate ARPU forecasts and identify revenue optimization opportunities.

**Triggers:**
- Daily subscriber billing cycle completion
- Monthly plan change processing
- Churn event detection
- New promotional campaign launch
- Quarterly forecast cycle initiation

**Actions:**
- Calculate real-time ARPU by segment and geography
- Analyze subscriber usage patterns and trends
- Predict churn probability and revenue impact
- Model promotional campaign effects on ARPU
- Update financial forecasting models
- Generate variance analysis reports

**Data Required:**
- Subscriber billing records
- Usage data by service type
- Plan change history
- Churn event data
- Promotional campaign parameters
- Market competitive intelligence

**Autonomy Level:** Escalation-Based  
Agent automatically generates forecasts and identifies trends, escalating significant variances (>3% ARPU change) or unusual patterns to human analysts for validation.

**Example Interaction:**
> The ARPU Forecast Engine detects that postpaid ARPU dropped 2.3% week-over-week due to increased subscriber migrations from unlimited plans to limited data plans. It analyzes the trend across 12 markets and predicts a $47M quarterly revenue impact if the trend continues. The agent updates the monthly forecast models, creates alerts for affected markets, and recommends targeted retention campaigns for high-value subscribers showing migration signals. It also identifies that competitor pricing changes in 3 key markets are driving the migrations and suggests pricing response strategies based on historical elasticity models.

---

### Use Case 4: Regulatory Fee & Tax Compliance Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Telecom companies face complex regulatory compliance across multiple jurisdictions, managing USF contributions, E-911 fees, state excise taxes, sales taxes, and federal regulatory fees. Each jurisdiction has different calculation methods, filing deadlines, and audit requirements. Finance teams use 5-8 different systems to calculate, validate, and file these fees, often requiring 2-3 FTEs dedicated solely to regulatory compliance.

#### The Solution
monday AI platform consolidates all regulatory fee calculations, automatically applies current rates, validates filings against historical patterns, and manages submission deadlines. AI agents monitor regulatory changes, update fee calculations, and ensure compliance across all jurisdictions. Integration with tax engines and government filing systems automates the entire workflow.

#### The Outcome
Consolidate regulatory compliance into single platform, reduce compliance FTE requirements by 60%, eliminate filing errors, and ensure 100% on-time submissions. Automatic regulatory change monitoring prevents costly compliance violations.

#### Discovery Questions
- How many different regulatory fees and taxes do you calculate monthly across all jurisdictions?
- What systems do you currently use for USF, E-911, and state tax calculations?
- How do you stay current with regulatory fee rate changes across different states?
- What's your process for validating regulatory fee calculations before filing?
- How many compliance-related audits or penalties have you faced in the past two years?

#### Industry Context
Telecommunications regulatory compliance is uniquely complex due to federal (FCC), state (PUC), and local jurisdiction requirements. Unlike other industries, telecom must contribute to universal service funds, emergency services, and accessibility programs while managing complex interstate/intrastate revenue allocation rules.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Compliance Center with a 'Fee Calculations' board containing: Filing Period (date), Jurisdiction (dropdown: Federal-USF, Federal-E911, Federal-TRS, plus all 50 states), Fee Type (dropdown: USF, E-911, Excise Tax, Sales Tax, Regulatory Fee), Revenue Base (currency), Fee Rate (percentage), Calculated Fee (currency), Filing Status (status: Pending, Calculated, Validated, Filed, Paid), Due Date (date), Filing Date (date), Confirmation Number (text), Assigned Compliance Officer (people), Validation Notes (long text), and Audit Trail (long text). Create automations to alert compliance team 14 days before filing deadlines, escalate to CFO when fees exceed budget by 10%, and notify legal when filing confirmations aren't received within 3 days. Add a dashboard showing compliance status by jurisdiction, fee trends, and aging reports. Include a calendar view for tracking all filing deadlines."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Compliance Monitor

**Agent Purpose:**  
Automatically calculate, validate, and file all regulatory fees and taxes across multiple jurisdictions while monitoring compliance deadlines.

**Triggers:**
- Monthly billing cycle completion
- Regulatory rate change notifications
- Filing deadline approaching (14 days)
- Revenue threshold changes
- Audit request received

**Actions:**
- Calculate regulatory fees using current rates
- Validate calculations against historical patterns
- Prepare filing documents and forms
- Submit filings to regulatory agencies
- Track confirmation receipts
- Monitor rate change notifications

**Data Required:**
- Revenue by jurisdiction and service type
- Current regulatory fee rates
- Historical filing patterns
- Regulatory agency contact information
- Compliance calendar and deadlines
- Audit trail requirements

**Autonomy Level:** Human-in-the-Loop  
Agent automatically calculates and prepares filings but requires human approval before submission to regulatory agencies, especially for amounts exceeding historical norms.

**Example Interaction:**
> The Regulatory Compliance Monitor processes monthly revenue data and calculates USF contributions totaling $12.7M across all eligible services. It notices the contribution rate increased 0.3% from the previous quarter and validates calculations against FCC guidelines. The agent prepares Form 499 filings, generates supporting schedules, and flags a 15% increase in contribution base due to new enterprise customer additions. It creates approval workflows for the tax director and schedules automatic filing upon approval. Simultaneously, it identifies that three state jurisdictions have updated their E-911 fee rates and recalculates those obligations, ensuring all deadlines are met with accurate filings.

---

### Use Case 5: Device Subsidy & Installment Plan Accounting

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Device financing programs require complex accounting under ASC 606, tracking device subsidies, installment plan receivables, and revenue recognition timing across thousands of device transactions monthly. Finance teams manually reconcile device inventory, subsidy costs, customer payment plans, and revenue recognition schedules. This process requires 2-4 FTEs and creates month-end closing delays.

#### The Solution
AI agents automatically track device transactions from point of sale through full revenue recognition, managing ASC 606 compliance for bundled service contracts, calculating subsidy amortization, and reconciling installment receivables. The system integrates with retail systems, billing platforms, and general ledger to ensure accurate device program accounting.

#### The Outcome
Automate 90% of device accounting processes, accelerate month-end close by 3-5 days, and ensure ASC 606 compliance without manual intervention. Reduce device accounting FTE requirements by 75%.

#### Discovery Questions
- What percentage of your device sales involve financing or installment plans?
- How do you currently handle ASC 606 revenue recognition for bundled device/service contracts?
- What's your process for tracking device subsidy costs and amortization?
- How do you reconcile device receivables with billing system installment tracking?
- What percentage of your month-end close delays relate to device program accounting?

#### Industry Context
Telecom device accounting is uniquely complex due to bundled device/service contracts requiring allocation of transaction prices between components. Unlike retailers selling devices outright, carriers must navigate complex revenue recognition rules while managing subsidy programs that impact cash flow and profitability metrics.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Device Finance Tracking system with a 'Device Transactions' board including: Transaction ID (auto-number), Customer Account (text), Device Model (dropdown with popular models), Device IMEI (text), Sale Date (date), Device List Price (currency), Customer Down Payment (currency), Installment Amount (currency), Installment Term (number), Subsidy Amount (currency), Service Plan Bundle (dropdown), ASC 606 Allocation (currency), Revenue Recognition Status (status: Initial, In Progress, Complete), Monthly Recognition Amount (currency), Remaining Balance (currency), Payment Status (status: Current, 30 Days, 60 Days, 90+ Days, Default), Assigned Accountant (people), and Accounting Notes (long text). Add automations to alert collections when accounts become 60+ days past due, notify accounting team when monthly recognition batches complete, and escalate to finance manager when subsidy costs exceed budget thresholds. Include dashboard views for device program profitability, aging analysis, and ASC 606 compliance tracking."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Device Finance Accountant

**Agent Purpose:**  
Automatically handle all accounting aspects of device financing programs including ASC 606 compliance, subsidy tracking, and receivables management.

**Triggers:**
- New device sale transaction
- Monthly installment payment received
- Payment delinquency detected
- Month-end close initiation
- Device return or exchange processed

**Actions:**
- Calculate ASC 606 transaction price allocation
- Record device subsidy and amortization schedules
- Process monthly revenue recognition entries
- Update installment receivables balances
- Generate aging reports and collection alerts
- Reconcile device program profitability

**Data Required:**
- Device catalog with pricing and costs
- Customer financing agreements
- Payment transaction history
- Service plan bundling rules
- ASC 606 allocation methodologies
- General ledger account mappings

**Autonomy Level:** Fully Autonomous  
Agent handles routine device accounting automatically but escalates unusual transactions (high-value devices, complex bundles, early terminations) for human review.

**Example Interaction:**
> The Device Finance Accountant processes 2,847 new iPhone transactions from the weekend sales promotion, automatically calculating ASC 606 allocations between device and service components based on standalone selling prices. It records $3.2M in device subsidy costs, establishes 24-month revenue recognition schedules for bundled contracts, and updates installment receivables for $8.7M in financed amounts. The agent identifies that 34 customers exceeded normal subsidy limits and flags these for credit review. It generates month-end device program reports showing 18% margin improvement compared to prior month and alerts the finance team that device subsidy accruals are tracking 12% below budget due to higher-than-expected customer down payments.

---

### Use Case 6: 5G Investment ROI & Infrastructure Fund Management

**Relevance:** Medium-High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
5G network investments require tracking billions in CapEx across thousands of sites, managing complex ROI calculations that account for coverage, capacity, and revenue impact over multi-year periods. Finance teams manually compile data from network planning, construction, and operations systems to analyze investment performance and justify continued funding to boards and investors.

#### The Solution
AI agents continuously monitor 5G deployment progress, track site-level investment costs, analyze usage and revenue data to calculate real ROI metrics, and provide predictive analytics for future investment decisions. The system integrates with network planning tools, construction management, and billing systems for comprehensive investment tracking.

#### The Outcome
Real-time visibility into 5G investment performance, automated ROI reporting for board presentations, and data-driven investment optimization that can improve ROI by 15-25%. Enable infrastructure investment scaling without proportional increase in finance analytical resources.

#### Discovery Questions
- What's your current 5G CapEx run rate, and how do you track ROI at the site level?
- How do you correlate 5G coverage investments with subscriber acquisition and ARPU impact?
- What systems do you use to track network construction costs and timeline performance?
- How do you justify continued 5G investment to your board and investor community?
- What percentage of your finance team's time is spent on infrastructure investment analysis?

#### Industry Context
5G infrastructure investments represent the largest CapEx cycle in telecom history, with carriers spending $50-200B globally. Unlike previous technology transitions, 5G ROI depends on new revenue streams (enterprise, IoT, edge computing) that don't exist yet, making traditional ROI models inadequate.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 5G Investment Tracker with a 'Site Deployments' board containing: Site ID (auto-number), Market Name (dropdown), Site Address (location), Site Type (dropdown: Macro, Small Cell, Indoor, Edge), Investment Amount (currency), Construction Status (status: Planning, Permitting, Construction, Testing, Live), Go-Live Date (date), Monthly Capex Spend (currency), Subscriber Coverage Added (number), Data Traffic GB/Month (number), Revenue Attribution (currency), ROI % (percentage), Payback Period Months (number), Project Manager (people), Construction Vendor (dropdown), and Performance Notes (long text). Create automations to alert executives when site deployments are 30+ days behind schedule, notify finance when site costs exceed budget by 15%, and update ROI calculations monthly when traffic data refreshes. Add dashboard views showing investment progress by market, ROI rankings, and payback period analysis."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Infrastructure Investment Analyzer

**Agent Purpose:**  
Continuously analyze 5G infrastructure investments to optimize ROI and inform strategic deployment decisions.

**Triggers:**
- New site construction milestone completion
- Monthly traffic and revenue data refresh
- Quarterly investment review cycle
- Site performance threshold breaches
- Board reporting deadline approaching

**Actions:**
- Calculate site-level ROI and payback periods
- Analyze subscriber and traffic impact by site
- Identify underperforming investment areas
- Generate investment optimization recommendations
- Prepare executive dashboards and reports
- Model future deployment scenarios

**Data Required:**
- Site construction costs and timelines
- Network traffic and performance metrics
- Subscriber location and usage data
- Revenue attribution by coverage area
- Competitive coverage analysis
- Construction vendor performance data

**Autonomy Level:** Escalation-Based  
Agent automatically tracks and analyzes investment performance but escalates significant ROI variances or strategic implications to finance leadership for decision-making.

**Example Interaction:**
> The Infrastructure Investment Analyzer processes monthly network data and identifies that 23 recently deployed 5G sites in suburban markets are generating 40% higher data traffic than projected, resulting in 18-month payback periods versus the 24-month target. It correlates this performance with work-from-home trends and recommends accelerating similar deployments in comparable markets. Conversely, it flags 8 urban sites with lower-than-expected performance due to delayed enterprise customer activations and suggests reallocating $12M in planned investment to suburban markets. The agent generates a board presentation showing overall 5G ROI improvement to 22% versus 18% business case assumptions and provides scenario models for optimizing the remaining $400M deployment budget across markets.

---

## Industry Terminology

| Term | Definition |
|------|-------------|
| **ARPU** | Average Revenue Per User - key profitability metric calculated monthly by subscriber segment |
| **Revenue Assurance** | Process of ensuring all network usage is accurately billed and revenue leakage is minimized |
| **Interconnect Billing** | Settlement process for calls/data between different carriers, using TAP/RAP file formats |
| **TAP/RAP Files** | Transferred Account Procedure / Returned Account Procedure - standard formats for roaming billing |
| **USF** | Universal Service Fund - federal contribution required from all telecom providers |
| **E-911** | Enhanced 911 services fee collected to fund emergency response infrastructure |
| **ASC 606** | Revenue recognition accounting standard affecting bundled device/service contracts |
| **ASC 842** | Lease accounting standard impacting tower and site lease arrangements |
| **CapEx vs OpEx** | Capital versus Operating expense allocation for network infrastructure investments |
| **MVNO** | Mobile Virtual Network Operator - companies using carrier infrastructure without owning it |
| **Spectrum Amortization** | Depreciation of spectrum license costs over useful life (typically 10-15 years) |
| **CPGA** | Cost Per Gross Add - customer acquisition cost metric including subsidies and marketing |
| **Churn** | Rate of subscriber cancellations, directly impacting revenue and ARPU forecasts |
| **Roaming Settlement** | Revenue sharing agreements for subscribers using partner networks |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **CFO** | Strategic financial leadership, investor relations, board reporting | High - Final authority on financial strategy |
| **Finance Director** | Day-to-day finance operations, team management, process optimization | High - Operational decision maker |
| **Revenue Assurance Manager** | Billing accuracy, leakage detection, system controls | Medium-High - Critical for revenue protection |
| **FP&A Manager** | Forecasting, budgeting, ARPU analysis, investor reporting | High - Key advisor to CFO |
| **Tax/Regulatory Manager** | Compliance, filing, regulatory fee calculations | Medium - Specialized expertise required |
| **Billing Operations Manager** | Customer billing, dispute resolution, payment processing | Medium - Operational efficiency focus |
| **Treasury Manager** | Cash management, interconnect settlements, working capital | Medium - Cash flow optimization |
| **Controller** | Financial reporting, accounting standards (ASC 606/842), audit | High - Technical accounting authority |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|------------|-------------|
| **Network Operations** | CapEx investment tracking, infrastructure ROI analysis | Unified platform for network investment financial analysis |
| **Customer Care** | Billing dispute resolution, refund processing, bad debt | Integrated customer financial view for dispute resolution |
| **Revenue Management** | Pricing optimization, promotional impact analysis | Combined pricing and financial impact modeling |
| **Regulatory Affairs** | Compliance reporting, regulatory fee validation | Streamlined regulatory compliance workflow |
| **Procurement** | Vendor payment automation, contract management | Integrated supplier payment and performance tracking |
| **Sales Operations** | Commission tracking, CPGA analysis, subscriber forecasting | Unified subscriber acquisition cost and revenue analysis |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **SAP/Oracle ERP** | "Legacy ERP that can't handle telecom complexity" | AI-powered telecom-specific workflows with better user experience |
| **Subex Revenue Assurance** | "Point solution that doesn't integrate with other systems" | Unified platform replacing multiple specialized tools |
| **Vertex Tax Engine** | "Tax-only solution without workflow management" | Complete regulatory compliance platform with AI validation |
| **Tableau/Power BI** | "Static reporting that requires constant manual updates" | Real-time AI-powered analytics with automated insights |
| **Custom In-House Systems** | "Technical debt that requires expensive maintenance" | Modern AI platform with no-code flexibility |
| **Excel/Spreadsheets** | "Manual processes that don't scale" | Automated workflows with enterprise governance |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"We have SAP for financial management"** | "SAP handles general accounting, but telecom needs specialized workflows for revenue assurance, interconnect billing, and regulatory compliance that SAP doesn't address. Our AI agents complement SAP with telecom-specific automation." |
| **"Our revenue assurance tool works fine"** | "Point solutions create data silos. Our platform unifies revenue assurance with billing, finance, and operations data, enabling AI to detect patterns that single-purpose tools miss." |
| **"Regulatory compliance is too complex for automation"** | "That's exactly why AI is essential. Our agents stay current with rate changes, validate calculations, and ensure filing deadlines are met automatically - reducing compliance risk, not increasing it." |
| **"We need specialized telecom expertise"** | "Our platform is built specifically for telecom finance, with deep understanding of ASC 606, interconnect billing, ARPU analytics, and regulatory compliance. This isn't generic workflow software." |
| **"Implementation would disrupt critical processes"** | "We use phased rollouts starting with non-critical processes like reporting and analytics, then gradually automate operational workflows. You control the pace of change." |

## Proof Points
*(To be populated with customer references)*

• Major US carrier reduced revenue leakage by $47M annually using AI-powered revenue assurance
• Regional operator automated 90% of interconnect settlement processing, reducing cycle time from 30 to 5 days
• Wireless carrier improved ARPU forecast accuracy by 31% with real-time subscriber analytics
• MVNO eliminated regulatory compliance violations using automated fee calculation and filing
• Telecom operator reduced device accounting FTE requirements by 60% while improving ASC 606 compliance

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*