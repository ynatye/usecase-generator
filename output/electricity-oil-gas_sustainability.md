# Electricity, Oil & Gas × Sustainability Playbook

## Overview

Sustainability departments in the electricity, oil & gas sector operate under extraordinary scrutiny. These teams are responsible for ESG (Environmental, Social, and Governance) reporting, carbon emissions tracking, decarbonization roadmaps, environmental compliance, and stakeholder communications around climate commitments. With the EU's CSRD (Corporate Sustainability Reporting Directive), SEC climate disclosure rules, and increasing pressure from institutional investors, sustainability is no longer a "nice-to-have" — it's a board-level mandate with real financial consequences.

In major energy companies, sustainability departments typically range from 20-80 professionals, often organized into sub-teams covering environmental compliance, ESG reporting & analytics, community relations, decarbonization strategy, and renewable energy transition. They sit at the intersection of operations, finance, legal, and communications — pulling data from across the enterprise to produce auditable reports for regulators, rating agencies (MSCI, Sustainalytics, CDP), and investors. The sheer complexity of tracking Scope 1, 2, and 3 emissions across upstream exploration, midstream pipelines, downstream refining, and retail operations makes this one of the most data-intensive sustainability functions in any industry.

The regulatory landscape is intense and evolving rapidly. From EPA greenhouse gas reporting and OSHA environmental standards in the US to the EU Emissions Trading System (ETS), TCFD recommendations, and the GHG Protocol, sustainability teams juggle dozens of overlapping frameworks. Many are also managing Just Transition initiatives, biodiversity impact assessments, and methane reduction programs — all while the company may still derive 80%+ of revenue from fossil fuels. The tension between operational reality and sustainability commitments creates unique challenges around data integrity, timeline management, and stakeholder trust.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | ESG data is scattered across EHS systems (Enablon, Sphera), ERP (SAP), SCADA, emissions monitoring, and dozens of spreadsheets — consolidation is existential |
| 2 | Scale Impact Without Overhead | High | Reporting requirements are exploding (CSRD, SEC, ISSB) but headcount is capped — teams must do 3× the reporting with the same staff |
| 3 | Replace or Radically Augment Headcount | Medium | Manual data collection from field operations, subsidiaries, and JV partners consumes thousands of hours annually that AI could reclaim |

## Prioritized Use Cases

---

### Use Case 1: ESG Data Aggregation & Reporting Hub

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Sustainability teams in energy companies spend 40-60% of their time collecting, cleaning, and reconciling data from disparate sources. Scope 1 emissions come from CEMS (Continuous Emissions Monitoring Systems), Scope 2 from utility invoices across hundreds of facilities, and Scope 3 from supply chain surveys that arrive in inconsistent formats. A single CDP questionnaire requires data points from 15+ internal systems. Errors discovered during third-party assurance (Deloitte, PwC) can delay filings and damage credibility with rating agencies.

#### The Solution
monday.com Work Management as the central ESG data orchestration layer. Each reporting framework (CDP, GRI, TCFD, SASB, SEC) gets a dedicated board with items representing each data point. Subitems track data sources, collection status, and validation steps. Integration with SAP for financial data, custom API connections for emissions monitoring data, and Forms for subsidiary/JV partner data submissions. Dashboard views aggregate completion rates across all frameworks. Timeline views show the critical path from data collection → validation → assurance → filing. mondayDB stores historical emissions factors and conversion coefficients for consistent year-over-year calculations.

#### The Outcome
60-70% reduction in data collection time. Single source of truth eliminates version control nightmares. Real-time visibility into reporting readiness reduces last-minute scrambles before filing deadlines. Audit trail satisfies third-party assurance requirements.

#### Discovery Questions
- How many different systems do you pull ESG data from today, and how much time does reconciliation take?
- Have you ever had a CDP or TCFD submission delayed because of data quality issues?
- How do you currently handle data collection from joint ventures and non-operated assets?
- What's your process when a third-party auditor flags a data discrepancy?
- How many FTEs are dedicated to data collection vs. actual sustainability strategy?

#### Industry Context
Energy companies often have complex ownership structures (operated vs. non-operated assets, joint ventures, minority stakes) that create equity-share vs. operational control debates for emissions accounting. Scope 3 Category 11 (use of sold products) is the elephant in the room — it's often 5-10× larger than Scope 1+2 combined for oil & gas companies. CDP scoring (A-list, B, C, D) directly impacts investor decisions and can move share prices.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an ESG Reporting Hub board. Columns: Reporting Framework (dropdown: CDP, GRI, TCFD, SASB, SEC Climate, EU Taxonomy), Data Point Name (text), Data Owner (people), Source System (dropdown: SAP, CEMS, Utility Invoices, Field Reports, Supply Chain Surveys, Manual Entry), Collection Status (status: Not Started, Requested, Received, Validated, Flagged, Approved), Value (numbers with unit label), Unit of Measure (dropdown: tCO2e, MWh, GJ, m³, tonnes, %, USD), Reporting Year (dropdown: 2024, 2025, 2026), Assurance Status (status: Not Required, Pending, In Review, Assured, Exception), Due Date (date), Notes (long text). Create subitems for tracking data source documentation and validation steps. Add a Dashboard view with widgets: completion rate by framework (pie chart), overdue items (table), data quality flags (numbers widget), timeline to filing deadlines. Add a Kanban view grouped by Collection Status. Add automations: when status changes to Flagged, notify the Data Owner and their manager; when all items in a group reach Approved status, notify the Sustainability Director; 3 days before Due Date, send reminder to Data Owner if status is not Validated or Approved."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Carbon Data Validator
**Agent Purpose:** Automatically validate incoming emissions data against historical baselines and flag anomalies before they reach assurance.

**Triggers:**
- When Collection Status changes to "Received" on any data point item
- When a new form submission arrives from a subsidiary or JV partner
- Weekly scheduled review of all "Validated" items for cross-framework consistency
- When Reporting Year changes (triggers re-baseline)

**Actions:**
- Compare submitted value against prior-year value and flag if variance exceeds ±15% with no documented explanation
- Cross-reference emissions factors against EPA/IPCC published tables and flag mismatches
- Auto-populate unit conversions (e.g., MWh → tCO2e using grid-specific factors)
- Generate a data quality scorecard for each reporting facility
- Escalate to Sustainability Director if >5 data points flagged in same facility (potential systemic issue)
- Create a summary update in the Notes column documenting the validation result

**Data Required:**
- Historical emissions data (prior 3 years)
- EPA/IPCC emissions factor tables
- Grid-specific electricity emissions factors (eGRID, IEA)
- Facility production volumes (for intensity metrics)

**Autonomy Level:** Human-in-the-Loop
Auto-validates and flags anomalies, but a human reviewer must approve before status moves to "Validated." Critical items (>25% variance or regulatory threshold breaches) require Sustainability Director sign-off.

**Example Interaction:**
> The Carbon Data Validator detects that the Permian Basin facility submitted Scope 1 emissions of 142,000 tCO2e for Q3, which is 28% higher than Q3 of the prior year (111,000 tCO2e). The agent checks production volumes and finds a 12% increase in throughput, which partially explains the rise but leaves a 16% unexplained gap. It flags the item, adds a note: "Variance partially explained by 12% production increase. Residual 16% gap unexplained — possible flaring event or equipment issue. Recommend review of CEMS data for September." It notifies the facility environmental engineer and the ESG reporting lead, creating a subitem for investigation with a 5-day deadline.

---

### Use Case 2: Decarbonization Roadmap & Target Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most major oil & gas companies have published net-zero or significant emissions reduction targets (e.g., 30% Scope 1+2 reduction by 2030, net-zero by 2050). But tracking progress against these multi-decade roadmaps across hundreds of initiatives — carbon capture projects, flaring reduction programs, methane detection campaigns, renewable energy investments, electrification of operations — is enormously complex. Leadership wants real-time dashboards showing whether the company is on track, but sustainability teams are manually updating Excel models quarterly, often discovering they're off-track too late to course-correct.

#### The Solution
monday.com Work Management for decarbonization portfolio management. A master board tracks all emission reduction initiatives with columns for estimated abatement (tCO2e/year), actual abatement, capex invested, status, timeline, and responsible business unit. Gantt/Timeline views show the critical path to interim targets (2025, 2028, 2030). Dashboard widgets display cumulative abatement vs. target trajectory, capex deployment rate, and initiative health by category (CCS, renewables, efficiency, methane, offsets). Subitems track milestones within each initiative. Automations alert leadership when cumulative tracked abatement falls below the trajectory required to hit the next interim target.

#### The Outcome
Real-time visibility into decarbonization progress replaces quarterly manual reporting. Early warning when trajectory diverges from targets. Portfolio optimization — quickly identify which initiatives deliver the most abatement per dollar and reallocate resources.

#### Discovery Questions
- How do you currently track progress against your published emissions reduction targets?
- When was the last time you discovered you were off-track on an interim target, and how much lead time did you have?
- How do you prioritize between competing decarbonization investments (CCS vs. renewables vs. efficiency)?
- Who in leadership gets regular updates on decarbonization progress, and in what format?
- How do you account for project delays or cancellations in your abatement projections?

#### Industry Context
The Science Based Targets initiative (SBTi) has specific requirements for oil & gas companies. Many companies set both absolute targets (reduce total emissions by X%) and intensity targets (reduce emissions per barrel of oil equivalent). Carbon capture and storage (CCS) projects have long lead times (5-10 years) and high uncertainty. Methane reduction is often the lowest-cost, highest-impact lever. The IEA Net Zero Roadmap is the benchmark many companies reference. Investor pressure from Climate Action 100+ directly influences target-setting.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Decarbonization Roadmap Tracker board. Columns: Initiative Name (text), Category (dropdown: Carbon Capture & Storage, Renewable Energy, Energy Efficiency, Methane Reduction, Electrification, Nature-Based Solutions, Offsets), Business Unit (dropdown: Upstream, Midstream, Downstream, Corporate, Renewables Division), Status (status: Planned, In Development, Under Construction, Operational, On Hold, Cancelled), Estimated Annual Abatement in tCO2e (numbers), Actual Annual Abatement in tCO2e (numbers), Capex Budget in USD millions (numbers), Capex Spent in USD millions (numbers), Start Date (date), Target Completion (date), Interim Target Year (dropdown: 2025, 2028, 2030, 2035, 2040, 2050), Risk Level (status: Low, Medium, High, Critical), Owner (people), Last Updated (date). Add subitems for milestones (FEED study, FID, permitting, construction start, commissioning). Create a Dashboard with: cumulative abatement bar chart by category, actual vs. target trajectory line chart (numbers widget), capex deployment donut chart, at-risk initiatives table, initiative count by status. Add Timeline view grouped by Category. Add automations: when Status changes to On Hold or Cancelled, recalculate cumulative abatement and notify Sustainability VP; when Target Completion passes and Status is not Operational, change Risk Level to Critical; monthly on the 1st, send a portfolio summary to the Chief Sustainability Officer."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Decarbonization Trajectory Analyst
**Agent Purpose:** Continuously monitor the portfolio of emission reduction initiatives and alert when the company risks missing interim targets.

**Triggers:**
- When any initiative's Status changes to On Hold, Cancelled, or has its Estimated Abatement reduced
- When Actual Abatement is updated for any initiative
- Monthly scheduled portfolio assessment
- When a new initiative is added

**Actions:**
- Recalculate cumulative projected abatement for each interim target year
- Compare against published target trajectory and flag gap (in tCO2e and % terms)
- Identify the top 3 "at risk" initiatives dragging the portfolio behind schedule
- Recommend reallocation: surface planned/early-stage initiatives that could be accelerated to close the gap
- Generate a one-page executive summary with RAG (Red/Amber/Green) status for each interim target
- Update a dedicated "Trajectory Health" item on the dashboard

**Data Required:**
- All initiative boards with abatement estimates and actuals
- Published company targets and interim milestones
- Historical emissions baseline
- Initiative cost curves (abatement per dollar)

**Autonomy Level:** Escalation-Based
Runs analysis autonomously. Generates reports and recommendations automatically. Escalates to Chief Sustainability Officer only when projected gap exceeds 10% of interim target or when a "Critical" risk item has no mitigation plan within 30 days.

**Example Interaction:**
> On the monthly assessment, the Decarbonization Trajectory Analyst calculates that with the Bayou CCS project delayed 18 months and the Gulf Coast flaring reduction program showing 40% less abatement than projected, the company's 2028 interim target of 15% Scope 1 reduction is now at risk — projected achievement is 11.2%. The agent creates an executive summary: "2028 Target: AMBER. Gap of 3.8 percentage points (≈ 890,000 tCO2e). Top risks: Bayou CCS delay (-520K tCO2e), Gulf Coast flaring underperformance (-370K tCO2e). Recommended accelerations: Eagle Ford methane detection expansion (potential +280K tCO2e, $12M capex, 18-month timeline) and Permian electrification Phase 2 (potential +340K tCO2e, $45M capex, 24-month timeline)." The summary is sent to the CSO and added to the board's updates.

---

### Use Case 3: Methane Leak Detection & Response (LDAR) Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The EPA's finalized methane rules (Subpart OOOOb/OOOOc) and the IRA's Methane Emissions Reduction Program impose steep fees ($900-$1,500 per metric ton) for facilities exceeding waste emissions thresholds. Companies operate thousands of well pads, compressor stations, and processing facilities requiring regular LDAR (Leak Detection and Repair) surveys. Tracking survey schedules, findings, repair timelines, and regulatory compliance across this fleet is a logistical nightmare — especially as OGI (Optical Gas Imaging), aerial surveys, and continuous monitoring technologies generate exponentially more data points than traditional Method 21 inspections.

#### The Solution
monday.com Work Management to orchestrate the entire LDAR lifecycle. A master board tracks every facility with survey schedule, last inspection date, next due date, and compliance status. When a leak is detected (from OGI, aerial survey, or continuous monitor), a new item is automatically created with location, component type, estimated emission rate, and severity. Automations enforce repair timelines (30 days for standard repairs, 15 days for major sources per EPA rules). Timeline views show the inspection schedule across all facilities. Dashboard widgets track leak count trends, repair completion rates, average time-to-repair, and estimated methane fee exposure.

#### The Outcome
Zero missed survey deadlines (avoiding $50K+ penalties per violation). 50% faster repair completion through automated prioritization and notifications. Complete audit trail for regulatory inspections. Real-time visibility into methane fee exposure drives proactive repair prioritization.

#### Discovery Questions
- How many facilities are in your LDAR program, and how do you currently track survey compliance?
- Have you ever received a notice of violation for missed LDAR deadlines?
- How are you integrating data from newer detection technologies (aerial, satellite, continuous monitors) with traditional OGI surveys?
- What's your current average time-to-repair, and how does that compare to regulatory deadlines?
- How do you estimate your exposure to the IRA methane fee?

#### Industry Context
LDAR is governed by 40 CFR Part 60 Subpart OOOOa/b/c. The EPA's Super Emitter Response Program allows third-party detection (satellites, flyovers) to trigger mandatory investigation within 15 days. Companies like ExxonMobil, Chevron, and BP have committed to zero routine flaring and near-zero methane intensity (<0.2%). Technologies like Bridger Photonics, Project Canary, and Kairos Aerospace provide aerial/continuous monitoring. The Methane Emissions Reduction Program fee escalates: $900/ton in 2024, $1,200 in 2025, $1,500 in 2026+.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Methane LDAR Management board. Columns: Facility Name (text), Facility ID (text), Region (dropdown: Permian, Eagle Ford, Marcellus, DJ Basin, Bakken, Gulf Coast, Midcon, Other), Facility Type (dropdown: Well Pad, Compressor Station, Processing Plant, Gathering Station, Tank Battery), Survey Method (dropdown: OGI, Method 21, Aerial, Satellite, Continuous Monitor), Last Survey Date (date), Next Survey Due (date), Survey Status (status: Compliant, Due Soon, Overdue, In Progress), Leak Found (status: Yes, No, Pending), Leak Severity (dropdown: Minor <1 kg/hr, Moderate 1-10 kg/hr, Major >10 kg/hr, Super Emitter >100 kg/hr), Component Type (dropdown: Valve, Connector, Flange, Pump Seal, Compressor Seal, Tank Hatch, Other), Estimated Emission Rate kg/hr (numbers), Repair Status (status: Open, Parts Ordered, Scheduled, Repaired, Verified, Delay Approved), Repair Deadline (date), Assigned Technician (people), Methane Fee Exposure USD (formula). Add subitems for repair documentation (photos, measurement before/after). Create Dashboard with: overdue facilities count, open leaks by severity bar chart, average time-to-repair numbers widget, total methane fee exposure, repair completion rate by region. Add automations: 7 days before Next Survey Due, notify field supervisor; when Leak Found = Yes and Leak Severity = Major or Super Emitter, immediately notify Environmental Director and set Repair Deadline to 15 days; when Repair Deadline passes and Repair Status is not Repaired or Verified, escalate to VP Operations; when Repair Status changes to Verified, update Survey Status to Compliant."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Methane Compliance Guardian
**Agent Purpose:** Proactively manage LDAR compliance deadlines and methane fee exposure across the facility fleet.

**Triggers:**
- Daily scan of all facilities for upcoming survey deadlines (7-day and 3-day warnings)
- When a new leak is detected (Leak Found = Yes)
- When a Super Emitter notification is received from a third party
- Weekly methane fee exposure calculation

**Actions:**
- Generate prioritized repair work orders based on emission rate × remaining days to deadline × fee exposure
- Auto-calculate methane fee exposure based on current leak inventory and emission rates
- Create investigation items when third-party Super Emitter notifications arrive (15-day response clock)
- Send weekly compliance scorecards to regional environmental managers
- Flag facilities approaching the waste emissions threshold that triggers methane fees
- Recommend survey schedule optimization based on historical leak frequency by facility type and age

**Data Required:**
- Facility database with survey schedules and compliance history
- EPA waste emissions thresholds by facility type
- Current methane fee rates
- Historical leak data for pattern analysis
- Third-party detection alerts (API integration)

**Autonomy Level:** Human-in-the-Loop
Creates and prioritizes work orders automatically. Calculates fee exposure autonomously. Requires human approval for: delay of repair extensions, regulatory reporting submissions, and reallocation of field crews between regions.

**Example Interaction:**
> The Methane Compliance Guardian detects that Compressor Station DJ-47 in the DJ Basin has an open Major leak (estimated 8.2 kg/hr) with only 4 days remaining on its 30-day repair deadline. The assigned technician marked it "Parts Ordered" 12 days ago but hasn't updated since. The agent sends an urgent notification: "⚠️ DJ-47 Major Leak — 4 days to deadline. Parts status unknown since Feb 5. Estimated fee exposure if not repaired: $43,200/month. Recommend dispatching backup crew from Wattenberg field office (2 techs available Thursday)." It simultaneously creates a subitem on the repair tracking board for the field supervisor to confirm parts arrival and schedule the repair crew.

---

### Use Case 4: Environmental Permit & Compliance Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
A single upstream oil & gas operation may hold 50+ environmental permits (air quality, water discharge, waste disposal, wetland mitigation, wildlife take). Each permit has unique conditions, monitoring requirements, reporting deadlines, and renewal timelines. Midstream and downstream operations add their own layers — Title V air permits for refineries can be hundreds of pages with dozens of specific conditions. Tracking all conditions across thousands of permits enterprise-wide is overwhelming. A single missed reporting deadline or violated condition can trigger enforcement actions, consent decrees, and reputational damage that dwarfs the cost of the underlying activity.

#### The Solution
monday.com Work Management as the permit compliance management system. Each permit is an item with columns for permit type, issuing agency, facility, key conditions, expiration date, and responsible person. Subitems track individual conditions and their monitoring/reporting requirements. Automations trigger reminders 90, 60, and 30 days before permit expiration for renewals. Status columns track condition compliance (Compliant, At Risk, Violation, Under Review). Dashboard views show enterprise-wide compliance status, upcoming renewals, and facilities with the most compliance flags. Forms allow field operators to submit condition monitoring data directly.

#### The Outcome
Zero missed permit renewal deadlines. Real-time compliance status replaces annual internal audits. Early warning system catches potential violations before they become enforcement actions. 70% reduction in time spent preparing for regulatory inspections.

#### Discovery Questions
- How many active environmental permits does your company hold, and where is that information stored today?
- When was the last time a permit condition was inadvertently violated, and what were the consequences?
- How do you prepare for unannounced regulatory inspections?
- What's your renewal process, and how far in advance do you typically start?
- How do new permit conditions from regulatory changes get communicated to field operations?

#### Industry Context
The EPA, state environmental agencies (TCEQ in Texas, COGCC in Colorado, PADEP in Pennsylvania), and local authorities all issue permits with overlapping requirements. Title V Operating Permits for major sources require annual compliance certifications. SPCC (Spill Prevention, Control, and Countermeasure) plans require regular reviews. NPDES (National Pollutant Discharge Elimination System) permits govern water discharges. The Clean Air Act's New Source Review (NSR) requirements can delay or block facility modifications if not properly managed.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Environmental Permit Tracker board. Columns: Permit Name (text), Permit Number (text), Permit Type (dropdown: Title V Air, Minor Source Air, NPDES Water, Stormwater, RCRA Waste, UIC Injection Well, Wetland, Wildlife Take, Spill Prevention, State Specific), Issuing Agency (dropdown: EPA, TCEQ, COGCC, PADEP, WVDEP, NDIC, State Other, Local), Facility (connect board: Facilities Master), Expiration Date (date), Renewal Status (status: Active, Renewal Filed, Under Review, Expired, Not Required), Compliance Status (status: Compliant, At Risk, Violation, Under Investigation, Resolved), Responsible Person (people), Last Audit Date (date), Next Report Due (date), Conditions Count (numbers), Conditions Met (numbers), Risk Score (formula: Conditions Met / Conditions Count × 100). Add subitems for each permit condition with: Condition Description (text), Monitoring Frequency (dropdown: Continuous, Daily, Weekly, Monthly, Quarterly, Annual), Last Monitored (date), Compliance (status), Evidence (files). Add Dashboard with: compliance rate gauge, permits expiring in 90 days table, violations count trend, compliance by permit type chart. Automations: 90 days before Expiration Date, create renewal task and notify Responsible Person; when any subitem Compliance changes to At Risk or Violation, notify Environmental Manager; weekly on Monday, send compliance summary to VP EHS."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Permit Compliance Sentinel
**Agent Purpose:** Monitor all environmental permit conditions and proactively alert when compliance is at risk.

**Triggers:**
- When a monitoring deadline approaches (auto-scans daily)
- When field data is submitted via form for condition monitoring
- When regulatory agency communications are received (manual input or email integration)
- 90 days before any permit expiration

**Actions:**
- Compare submitted monitoring data against permit limits and flag exceedances
- Generate pre-populated renewal applications based on current permit data
- Create compliance checklists for upcoming regulatory inspections based on permit conditions
- Alert when regulatory changes may affect existing permit conditions (based on Federal Register monitoring)
- Produce quarterly compliance summary reports for executive review
- Track and escalate permit conditions that have been "At Risk" for >30 days without resolution

**Data Required:**
- Complete permit database with all conditions
- Historical monitoring data for trend analysis
- Regulatory limit thresholds from each permit
- Federal Register and state regulatory update feeds

**Autonomy Level:** Escalation-Based
Routine monitoring checks and reminder generation are fully autonomous. Compliance status assessments require human confirmation. Any potential violation triggers immediate escalation to Environmental Manager with all supporting data packaged for review.

**Example Interaction:**
> The Permit Compliance Sentinel reviews the monthly CEMS data submission for Refinery Unit 12's Title V permit. The NOx emissions for February averaged 38.2 ppm against a permit limit of 40 ppm. While technically compliant, the agent flags this as "At Risk" because the 3-month rolling average (37.1, 39.4, 38.2 = 38.2 ppm) shows an upward trend. It creates an alert: "Refinery Unit 12 NOx trending toward Title V limit (95.5% of threshold). 3-month trend: +1.1 ppm/month. At current trajectory, exceedance projected in 6-8 weeks. Recommend: (1) inspect SCR catalyst, (2) review combustion tuning, (3) schedule maintenance window before Q2 turnaround." The alert goes to the refinery environmental engineer with a linked subitem for tracking corrective actions.

---

### Use Case 5: Scope 3 Value Chain Emissions Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
For oil & gas companies, Scope 3 emissions (especially Category 11: Use of Sold Products) represent 70-90% of total lifecycle emissions. Tracking and reporting these requires data from hundreds of customers, suppliers, and intermediaries. Many companies also need to address Scope 3 Category 1 (purchased goods and services), Category 4 (upstream transportation), and Category 6 (business travel). The data collection is largely manual — supplier questionnaires with <30% response rates, spend-based estimates with high uncertainty, and constant debates about methodology and allocation.

#### The Solution
monday.com Work Management to orchestrate Scope 3 data collection campaigns. A board for each material Scope 3 category. Supplier engagement boards track questionnaire distribution, response status, data quality scores, and follow-up actions. Forms for supplier data submission with built-in validation. Automations send reminders to non-respondents on a schedule. Dashboard views show response rates by category and supplier tier, data quality distribution, and estimated vs. actual emissions comparisons. Connected boards link supplier data to the master ESG Reporting Hub.

#### The Outcome
2× improvement in supplier response rates through systematic follow-up. Shift from 100% spend-based estimates to 40%+ supplier-specific data (higher accuracy, better ratings). Clear audit trail for methodology choices. 50% reduction in Scope 3 data collection cycle time.

#### Discovery Questions
- What percentage of your Scope 3 reporting currently uses supplier-specific data vs. spend-based estimates?
- How do you engage suppliers on emissions data, and what's your response rate?
- Which Scope 3 categories are most material for your company, and how confident are you in those numbers?
- How does your Scope 3 data feed into your net-zero target tracking?
- Are investors or rating agencies pushing for more granular Scope 3 disclosure?

#### Industry Context
The GHG Protocol Scope 3 Standard defines 15 categories. For oil & gas, Category 11 is calculated using product volumes and emissions factors — relatively straightforward but politically sensitive because it represents the emissions from burning the fuel you sell. CDP and SBTi increasingly require Scope 3 targets. The Oil & Gas Methane Partnership 2.0 (OGMP 2.0) provides a reporting framework specifically for methane across the value chain. IPIECA (the oil & gas industry association) publishes sector-specific Scope 3 guidance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Scope 3 Data Collection Manager board. Columns: Supplier/Partner Name (text), Scope 3 Category (dropdown: Cat 1 Purchased Goods, Cat 2 Capital Goods, Cat 3 Fuel & Energy, Cat 4 Upstream Transport, Cat 5 Waste, Cat 6 Business Travel, Cat 7 Commuting, Cat 9 Downstream Transport, Cat 11 Use of Sold Products, Cat 12 End-of-Life), Data Collection Method (dropdown: Supplier-Specific, Average Data, Spend-Based, Hybrid), Questionnaire Sent (date), Response Received (status: Not Sent, Sent, Reminded, Received, Incomplete, Verified), Data Quality Score (dropdown: 1-Very High, 2-High, 3-Medium, 4-Low, 5-Very Low), Emissions Estimate tCO2e (numbers), Confidence Level (dropdown: High ±10%, Medium ±25%, Low ±50%), Tier (dropdown: Tier 1 Strategic, Tier 2 Significant, Tier 3 Standard), Year (dropdown: 2024, 2025, 2026), Owner (people). Add subitems for individual data points within each supplier response. Dashboard with: response rate by category pie chart, data quality distribution, total Scope 3 by category bar chart, supplier engagement funnel. Automations: 14 days after Questionnaire Sent if Response Received is still Sent, change to Reminded and send follow-up; when Response Received changes to Received, notify Owner for verification; when Data Quality Score is 4 or 5, create improvement action item."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Scope 3 Engagement Orchestrator
**Agent Purpose:** Manage the full lifecycle of supplier emissions data collection, from outreach to verification, maximizing response rates and data quality.

**Triggers:**
- When a new data collection cycle is initiated (annual or quarterly)
- When a supplier response is received
- When reminder intervals are reached (14 days, 30 days, 45 days after send)
- When data quality issues are identified

**Actions:**
- Generate personalized questionnaires based on supplier type and Scope 3 category
- Analyze submitted data for completeness, internal consistency, and reasonableness vs. industry benchmarks
- Auto-calculate emissions using appropriate factors when supplier provides activity data
- Prioritize follow-up efforts based on materiality (emissions impact) × responsiveness
- Generate gap analysis reports showing which categories need better data
- Recommend methodology upgrades (e.g., shift from spend-based to average-data for top 20 suppliers)

**Data Required:**
- Supplier database with spend data, product categories, and contact information
- GHG Protocol emissions factor databases (DEFRA, EPA, ecoinvent)
- Prior year Scope 3 submissions for trend comparison
- Industry benchmark data for reasonableness checks

**Autonomy Level:** Human-in-the-Loop
Sends questionnaires and reminders autonomously. Performs initial data validation automatically. Flags anomalies for human review. Methodology changes and final verified numbers require sustainability analyst approval.

**Example Interaction:**
> The Scope 3 Engagement Orchestrator processes a response from TechnoValves Inc. (Tier 1 supplier, Category 1). The supplier reports 2,840 tCO2e for their products sold to the company, but the agent notices this is 62% lower than last year's figure despite procurement records showing a 5% increase in purchase volume. The agent flags this: "Data anomaly: TechnoValves reports 62% emissions reduction YoY with 5% volume increase. Possible explanations: (1) methodology change by supplier, (2) data error, (3) genuine efficiency improvement. Confidence: Low. Recommend requesting supporting documentation — specifically their methodology and any changes from prior year. Creating follow-up questionnaire focused on calculation methodology." It changes the Data Quality Score to 4 and creates a subitem tracking the methodology clarification request.

---

### Use Case 6: Sustainability Stakeholder Communications & Reporting Calendar

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy company sustainability teams manage an exhausting calendar of external communications: annual sustainability/ESG report, CDP questionnaire (due July), proxy statement ESG disclosures, SEC climate filings, investor day presentations, ESG rating agency questionnaires (MSCI, Sustainalytics, ISS), industry group reports (IPIECA, OGMP 2.0), community engagement events, and ad-hoc investor inquiries. Each has different deadlines, data requirements, approval chains, and audiences. Content often overlaps but can't simply be copy-pasted due to framework-specific requirements. Teams scramble from one deadline to the next with no unified view.

#### The Solution
monday.com Work Management as the sustainability communications command center. A master board tracks every publication/submission with its deadline, status, content requirements, and approval workflow. Connected boards link to the ESG data hub for content sourcing. Workload views ensure no team member is overloaded during peak reporting season (Q2-Q3). Document collaboration for draft reviews with approval automations. Templates for recurring publications speed up annual restarts.

#### The Outcome
No missed deadlines across all reporting frameworks. 30% faster publication cycles through templating and reuse. Clear visibility into team capacity during peak periods. Consistent messaging across all stakeholder channels.

#### Discovery Questions
- How many sustainability-related publications or submissions does your team produce annually?
- Do you have a unified calendar for all ESG reporting deadlines?
- How do you ensure consistent messaging across your sustainability report, CDP response, and investor presentations?
- What's your approval process, and where do bottlenecks typically occur?
- How do you handle ad-hoc ESG inquiries from investors or rating agencies?

#### Industry Context
CDP questionnaire responses are scored and publicly available — A-list companies get significant positive press. MSCI and Sustainalytics ratings directly influence ESG fund inclusion decisions. The Global Reporting Initiative (GRI) Oil & Gas Sector Standard provides specific disclosure requirements. TCFD is being absorbed into ISSB (IFRS S1/S2), creating a transition period where companies must track both. Many companies now produce separate "Climate Report" or "Energy Transition Report" documents alongside their sustainability report.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Sustainability Reporting Calendar board. Columns: Publication/Submission Name (text), Type (dropdown: Annual Report, CDP Questionnaire, SEC Filing, Rating Agency Response, Investor Presentation, Industry Report, Community Report, Ad-Hoc Inquiry), Framework (dropdown: GRI, TCFD, SASB, CDP, ISSB, SEC, EU CSRD, IPIECA, Custom), Audience (dropdown: Investors, Regulators, Rating Agencies, Public, Community, Industry Peers, Board), Draft Due (date), Review Due (date), Final Deadline (date), Status (status: Not Started, Drafting, Internal Review, Legal Review, Executive Approval, Published/Submitted), Lead Author (people), Reviewers (people), Approver (people), Data Dependencies (connect board: ESG Reporting Hub), Content Overlap (connect board: self — link related publications). Add subitems for individual sections/questions within each publication. Dashboard: timeline of all deadlines, status distribution chart, workload by team member, upcoming deadlines table. Automations: when Status changes to Internal Review, notify all Reviewers; when all subitem statuses are Complete and Status is Internal Review for 3+ days, nudge Reviewers; when Status changes to Published/Submitted, log completion date and notify team."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Narrative Coordinator
**Agent Purpose:** Ensure consistency and completeness across all sustainability publications by cross-referencing content and flagging gaps.

**Triggers:**
- When any publication's Status changes to "Drafting"
- When a draft section is uploaded or updated
- 30 days before Final Deadline if Status is still "Not Started"
- When a new ad-hoc inquiry is received

**Actions:**
- Cross-reference draft content against prior year publications for consistency
- Flag data points in drafts that differ from the ESG Reporting Hub (potential errors)
- Identify content reuse opportunities across publications (e.g., CDP answer → Sustainability Report section)
- Generate first-draft responses for rating agency questionnaires using existing published data
- Alert when a publication deadline conflicts with team member PTO or other deadlines
- Create a "key messages" consistency checklist across all active publications

**Data Required:**
- All prior year sustainability publications
- ESG Reporting Hub data
- Team calendar and availability
- Framework-specific requirement guides

**Autonomy Level:** Human-in-the-Loop
Generates draft content suggestions and consistency flags automatically. All published content requires human review and approval. Ad-hoc inquiry first drafts are generated for analyst editing before sending.

**Example Interaction:**
> The ESG Narrative Coordinator notices that the draft CDP Climate Change questionnaire (Section C6 - Emissions Data) reports total Scope 1 emissions of 12.4 million tCO2e, but the draft Annual Sustainability Report (page 47) states 12.1 million tCO2e. It flags: "Scope 1 discrepancy: CDP draft = 12.4M, Sustainability Report draft = 12.1M, ESG Hub verified figure = 12.4M. The Sustainability Report appears to use a draft figure from January. Recommend updating SR page 47 to match verified Hub data (12.4M tCO2e). Note: this will also affect the YoY reduction percentage on page 48 (currently states 4.7% reduction, corrected figure = 3.3% reduction)." The flag is assigned to the lead author of both publications.

---

### Use Case 7: Water Stewardship & Produced Water Management

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Oil & gas operations are water-intensive. Hydraulic fracturing can use 5-15 million gallons per well. Produced water volumes in mature fields like the Permian Basin exceed oil production volumes by 3-5×. Managing water sourcing, treatment, recycling, and disposal across hundreds of wells requires tracking permits, volumes, water quality data, disposal well capacity, recycling rates, and compliance with state regulations. Many companies have committed to reducing freshwater use and increasing produced water recycling — but tracking progress is manual and fragmented across field offices.

#### The Solution
monday.com Work Management for water lifecycle tracking. Boards track water sourcing (freshwater withdrawal permits and volumes), water use (per well, per facility), produced water handling (volumes, quality, destination), recycling operations (treatment facility throughput, quality output), and disposal (injection well volumes and capacity). Connected boards link water use to production data for intensity metrics. Dashboard views show freshwater withdrawal trends, recycling rates, disposal well capacity utilization, and compliance status.

#### The Outcome
Real-time water balance across all operations. 20% improvement in produced water recycling rates through better matching of supply and demand. Early warning on disposal well capacity constraints. Complete water stewardship reporting for CDP Water Security questionnaire.

#### Discovery Questions
- What percentage of your produced water is currently recycled vs. disposed?
- How do you track water sourcing permits and withdrawal limits?
- Have you experienced disposal well capacity constraints, and how did you manage them?
- What's your freshwater intensity target (gallons per BOE), and how do you track it?
- How does water management data flow into your sustainability reporting?

#### Industry Context
The Permian Basin produces roughly 15 billion barrels of water annually — more than oil. Seismicity concerns have led to disposal well restrictions in Oklahoma, Texas (RRC), and New Mexico. Produced water recycling is growing but requires treatment to remove TDS, hydrocarbons, and scaling compounds. CDP Water Security questionnaire scores are increasingly important. The CEO Water Mandate and Alliance for Water Stewardship (AWS) provide frameworks. Water stress mapping (WRI Aqueduct tool) helps prioritize stewardship efforts in high-risk basins.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Water Stewardship Tracker board. Columns: Facility/Well Name (text), Basin (dropdown: Permian, Eagle Ford, Marcellus, DJ Basin, Bakken, Haynesville, Other), Water Type (dropdown: Freshwater Sourced, Produced Water Generated, Produced Water Recycled, Produced Water Disposed, Treated Effluent), Volume in Barrels (numbers), Month (dropdown: Jan-Dec), Year (dropdown: 2024, 2025, 2026), Source/Destination (text), Permit Number (text), Permit Limit bbls/month (numbers), Utilization % (formula: Volume / Permit Limit × 100), Water Quality TDS mg/L (numbers), Recycling Status (status: Fresh Use, Collected, In Treatment, Treated-Ready, Recycled to Operations, Disposed), Responsible (people). Dashboard with: freshwater withdrawal trend line by month, recycling rate gauge (recycled / total produced × 100), disposal well utilization by basin, water intensity (bbls water / BOE produced), permit utilization heat map. Automations: when Utilization % exceeds 80%, notify Water Manager; when Recycling Status changes to Disposed and basin has available recycling capacity, flag as optimization opportunity; monthly summary sent to Sustainability team."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Water Balance Optimizer
**Agent Purpose:** Match produced water supply with recycling demand across operations to maximize recycling rates and minimize freshwater use and disposal costs.

**Triggers:**
- When new produced water volumes are reported
- When a frac crew schedules water needs for upcoming completions
- When disposal well utilization exceeds 85%
- Weekly optimization run

**Actions:**
- Calculate optimal produced water routing: which produced water streams should go to which recycling facilities based on volume, quality, distance, and timing
- Identify freshwater substitution opportunities where recycled water quality meets frac specifications
- Alert when disposal well capacity is approaching limits and recommend alternatives
- Track and project water balance for the next 30/60/90 days based on drilling schedule
- Generate water stewardship metrics for sustainability reporting

**Data Required:**
- Produced water volumes and quality by facility
- Recycling facility capacity and current throughput
- Drilling and completions schedule (frac water demand)
- Disposal well capacity and injection rate permits
- Water trucking/pipeline logistics data

**Autonomy Level:** Escalation-Based
Generates routing recommendations and optimization reports autonomously. Flags critical capacity issues for immediate human review. Requires operations manager approval before changing water routing or substituting recycled water for freshwater on active frac jobs.

**Example Interaction:**
> The Water Balance Optimizer identifies that the Wolfcamp A completions team has scheduled 3 wells requiring 12 million gallons of frac water over the next 21 days, currently planned to use 100% freshwater from the Pecos River allocation. Meanwhile, the Midland Recycling Facility has 8 million gallons of treated produced water meeting frac-quality specs, and two nearby well pads (Mustang 14H and Rattlesnake 7H) are producing 400,000 bbl/month of water currently being trucked 45 miles to disposal. The agent recommends: "Redirect Mustang 14H and Rattlesnake 7H produced water to Midland Recycling (15 miles closer than current disposal) → treat → supply 67% of Wolfcamp A frac water. Savings: $180K in freshwater costs, $95K in disposal trucking. Recycling rate improvement: +4.2 percentage points for Permian operations. Action needed: confirm recycled water quality specs with completions engineer."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| CEMS | Continuous Emissions Monitoring System — real-time stack gas measurement |
| CDP | Carbon Disclosure Project — global environmental disclosure platform |
| LDAR | Leak Detection and Repair — regulatory program for fugitive emissions |
| OGI | Optical Gas Imaging — infrared camera technology for detecting hydrocarbon leaks |
| TCFD | Task Force on Climate-related Financial Disclosures |
| Scope 1/2/3 | Direct emissions / indirect from purchased energy / all other value chain emissions |
| tCO2e | Tonnes of carbon dioxide equivalent — standard emissions unit |
| BOE | Barrel of Oil Equivalent — standard production unit |
| SBTi | Science Based Targets initiative — validates corporate climate targets |
| CSRD | Corporate Sustainability Reporting Directive (EU) |
| ETS | Emissions Trading System — cap-and-trade carbon market |
| TDS | Total Dissolved Solids — key water quality parameter |
| SPCC | Spill Prevention, Control, and Countermeasure plan |
| NPDES | National Pollutant Discharge Elimination System |
| FID | Final Investment Decision — project approval milestone |
| FEED | Front-End Engineering Design — pre-FID engineering phase |
| SCR | Selective Catalytic Reduction — NOx emissions control technology |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Sustainability Officer (CSO) | Enterprise sustainability strategy, board reporting, target-setting | Decision-maker |
| VP Environment, Health & Safety (EHS) | Operational compliance, permits, safety culture | Decision-maker |
| Director of ESG Reporting | Data collection, framework compliance, rating agency relations | Influencer / Champion |
| Environmental Engineers (Field) | Facility-level compliance, LDAR, monitoring | User |
| Sustainability Analysts | Data analysis, report drafting, benchmarking | User |
| Investor Relations | ESG communications to financial stakeholders | Influencer |
| General Counsel / Legal | Regulatory risk, disclosure liability | Decision-maker (veto) |
| Board Sustainability Committee | Governance, target approval, risk oversight | Ultimate decision-maker |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations | Source of emissions data, permit compliance execution | Operational dashboards, field data capture |
| Finance | Carbon pricing, capex for decarbonization, ESG-linked financing | Investment tracking, green bond compliance |
| Legal | Regulatory compliance, disclosure liability, permit management | Contract and permit management |
| IT | Data infrastructure, system integrations, cybersecurity for OT | Integration hub, data pipeline management |
| PR & Communications | External messaging, stakeholder engagement, crisis comms | Content management, campaign coordination |
| Procurement | Scope 3 supplier engagement, sustainable sourcing | Supplier management, RFP workflows |
| HR | Just Transition programs, diversity reporting, safety culture | Training management, workforce planning |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Enablon (Wolters Kluwer) | EHS + sustainability compliance | Complex, expensive, poor UX — monday.com as orchestration layer on top or partial replacement for reporting workflows |
| Sphera | Operational risk + ESG reporting | Heavy implementation, best for large enterprise — monday.com wins on speed to value and flexibility |
| Persefoni | Carbon accounting platform | Strong on Scope 1-3 calculation but weak on workflow orchestration — complementary or displacement for smaller teams |
| Watershed | Corporate climate platform | VC-funded, modern UX — but focused on calculation, not work management. monday.com owns the workflow |
| Excel/SharePoint | "System of record" for most sustainability teams | Direct displacement — monday.com replaces the spreadsheet chaos |
| Salesforce Net Zero Cloud | ESG within Salesforce ecosystem | Locked to Salesforce customers; monday.com is platform-agnostic and simpler |
| SAP Sustainability Control Tower | Integrated with SAP ERP | Requires deep SAP commitment; monday.com offers faster deployment alongside any ERP |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Enablon/Sphera for ESG" | Those are great for calculation and compliance — but your team still lives in spreadsheets for the actual work coordination. monday.com orchestrates the workflow around those systems, not replaces the calculation engine. |
| "ESG data is too sensitive for a general platform" | monday.com offers enterprise-grade security (SOC 2, ISO 27001, HIPAA-capable), granular permissions, and audit logging. Your ESG data is no more sensitive than the financial data already managed on the platform. |
| "We need specialized carbon accounting, not work management" | You're right that calculation needs domain tools. But 60% of your team's time isn't calculating — it's collecting data, chasing people, managing deadlines, and coordinating reviews. That's exactly what monday.com solves. |
| "Our sustainability team is too small to justify a new platform" | Small teams benefit the most — automation handles the coordination that would otherwise require 2-3 additional analysts. AI agents multiply your capacity without adding headcount. |
| "Regulatory requirements are too specific for a configurable platform" | That specificity is exactly why you need flexibility. Cookie-cutter tools can't adapt when SEC finalizes new rules or the EU CSRD scope expands. monday.com adapts in days, not months. |

## Proof Points
*(To be populated with customer references)*
- [Energy company using monday.com for ESG reporting coordination]
- [Utility managing permit compliance on monday.com]
- [Oil & gas company tracking decarbonization initiatives]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
