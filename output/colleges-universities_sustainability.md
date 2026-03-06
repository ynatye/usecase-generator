# Colleges & Universities × Sustainability Playbook

## Overview

Sustainability departments in higher education have evolved from small, advisory offices into strategic functions that touch every corner of campus operations. At major research universities, the Office of Sustainability may oversee carbon neutrality commitments, STARS (Sustainability Tracking, Assessment & Rating System) reporting, campus-wide waste diversion programs, renewable energy procurement, sustainable transportation initiatives, and integration of sustainability into the curriculum. These teams typically report to a Chief Sustainability Officer or VP of Facilities/Administration and coordinate across dozens of departments — from dining services and procurement to facilities management and student affairs.

The regulatory and reputational landscape is intensifying. Many institutions have signed the Presidents' Climate Leadership Commitments (formerly the Carbon Commitment), pledging carbon neutrality by specific target dates (often 2035–2050). State mandates — like California's SB 1383 for organic waste diversion or Massachusetts' Leading by Example executive orders — add compliance pressure. Meanwhile, prospective students and faculty increasingly evaluate institutions on sustainability performance, making STARS Gold or Platinum ratings a competitive differentiator in admissions and recruitment.

Sustainability offices are chronically under-resourced relative to their mandate. A team of 3–8 professionals may be responsible for tracking thousands of data points across energy, water, waste, transportation, dining, procurement, and curriculum. They rely heavily on student interns, cross-departmental liaisons, and manual data collection — creating significant operational drag. The opportunity for monday.com is to become the central operating system that connects sustainability strategy to campus-wide execution.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Sustainability teams of 3-8 manage institution-wide programs across 50+ buildings, thousands of stakeholders, and dozens of reporting frameworks — with minimal budget growth |
| 2 | Replace or Radically Augment Headcount | Medium-High | Data collection for STARS, GHG inventories, and compliance reporting currently requires armies of student workers doing manual spreadsheet consolidation |
| 3 | Consolidate Tech Stack with AI | Medium | Teams cobble together SIMAP, utility portals, survey tools, spreadsheets, and project trackers — no single source of truth exists |

## Prioritized Use Cases

---

### Use Case 1: STARS Reporting & Accreditation Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
STARS (Sustainability Tracking, Assessment & Rating System) submissions require data across 63 credits in five categories: Academics, Engagement, Operations, Planning & Administration, and Innovation. Each credit has specific metrics, responsible parties, and documentation requirements. Most institutions spend 6–12 months gathering data from 20+ departments, chasing down liaisons, and reconciling conflicting numbers in sprawling spreadsheets. Missed deadlines mean delayed submissions, and inaccurate data risks rating downgrades — directly impacting institutional reputation and rankings like Princeton Review's Guide to Green Colleges.

#### The Solution
monday.com Work Management provides a centralized STARS Credit Tracker board with each credit as an item, grouped by category (AC, EN, OP, PA, IN). Columns include: Credit Name (text), Point Value (number), Responsible Department (dropdown), Data Liaison (people), Data Status (status: Not Started / In Progress / Under Review / Complete), Documentation (files), Due Date (date), Score (number), and Notes (long text). Dashboard views show completion percentage by category, overdue items, and projected total score. Automations notify liaisons 30/60/90 days before submission deadlines and escalate overdue credits to the CSO.

#### The Outcome
Reduce STARS reporting cycle from 8–12 months to 3–4 months. Eliminate data gaps that previously cost institutions 5–15 points. Enable real-time score projection so leadership can prioritize high-impact credits. Free up 500+ student worker hours per reporting cycle.

#### Discovery Questions
- "How many departments contribute data to your STARS submission, and what's your current process for tracking who's submitted what?"
- "What was your last STARS score, and were there credits where you know you left points on the table due to incomplete data?"
- "How long does your current reporting cycle take from kickoff to submission?"
- "Do you have a single place where all STARS documentation lives, or is it scattered across departments?"
- "How do you handle mid-cycle data updates when policies or programs change?"

#### Industry Context
AASHE (Association for the Advancement of Sustainability in Higher Education) administers STARS. Ratings range from Bronze to Platinum. Over 1,000 institutions participate. Reports are valid for 3 years. Version 3.0 is launching with revised credits. Institutions often benchmark against peer groups (e.g., Big Ten, Ivy League, state university systems). The STARS report is public — it's both an internal management tool and an external marketing asset.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a STARS Credit Tracking workspace in monday.com. Create a board called 'STARS 3.0 Credit Tracker' with groups for each STARS category: Academics (AC), Engagement (EN), Operations (OP), Planning & Administration (PA), and Innovation & Leadership (IN). Each item represents one STARS credit. Add columns: Credit Code (text), Credit Name (text), Max Points (number), Responsible Department (dropdown: Facilities, Dining, Procurement, Transportation, Academics, Student Affairs, HR, Finance, IT, Research, Communications), Data Liaison (people), Collection Status (status: Not Started, Awaiting Data, In Progress, Under Review, Complete, N/A), Documentation (files), Evidence Link (link), Due Date (date), Actual Score (number), Notes (long text), Last Updated (date). Create a Dashboard with: (1) a pie chart showing completion status across all credits, (2) a numbers widget showing projected total score (sum of Actual Score), (3) a battery widget showing % of credits marked Complete, (4) a table widget filtered to show overdue items (Due Date < today AND status not Complete). Add automations: when Status changes to 'Awaiting Data', notify the Data Liaison; when Due Date arrives and Status is not Complete, notify item creator and move Status to 'Overdue'; every Monday at 9am, send a summary of incomplete credits to the board owner."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** STARS Scout
**Agent Purpose:** Automatically track STARS credit progress, chase data liaisons, and project institutional rating.

**Triggers:**
- Weekly scheduled check every Monday at 8am
- When a credit's Due Date is within 14 days and Status is not Complete
- When a new data file is uploaded to any credit item
- When Status changes to "Under Review"
- Manual trigger by CSO for ad-hoc progress reports

**Actions:**
- Send personalized follow-up messages to Data Liaisons with outstanding credits, including specific data requirements and examples from last submission
- Analyze uploaded documentation against credit requirements and flag incomplete submissions
- Calculate projected STARS score based on current Actual Scores and estimate remaining points
- Generate weekly progress digest for the CSO showing credits completed this week, at-risk credits, and projected final rating
- Compare current progress against peer institution benchmarks (if available)
- Auto-populate Notes with data validation observations

**Data Required:**
- STARS credit requirements database (credit descriptions, required evidence, point allocations)
- Historical STARS submission data
- Department contact directory
- Integration with campus utility/energy management systems for auto-population of operational data

**Autonomy Level:** Human-in-the-Loop
Agent autonomously chases liaisons and validates data, but all final score entries and documentation approvals require CSO sign-off before submission to AASHE.

**Example Interaction:**
> It's Monday morning, and STARS Scout scans the Credit Tracker board. It finds that EN-6 (Assessing Sustainability Culture) is due in 12 days but still shows "Awaiting Data" — the Student Affairs liaison hasn't uploaded the campus sustainability literacy survey results. The agent sends a Slack-integrated notification: "Hi Dr. Martinez — EN-6 (Sustainability Culture Assessment) data is due Feb 28. We need the 2025 sustainability literacy survey results and response rate. Last cycle, this credit earned 1.5/2.0 points. The survey results file should include: sample size, response rate, mean scores by question category, and year-over-year comparison. Can you upload by Feb 24 to allow review time?" Simultaneously, the agent updates the projected score dashboard, noting that if EN-6 comes in at 1.5 again (vs. the 2.0 max), the institution's projected total is 72.3 — just 2.7 points short of Platinum. It flags this to the CSO with a note: "Recommend prioritizing AC-9 (Research) and OP-5 (Building Energy) where additional documentation could yield 4+ points."

---

### Use Case 2: Greenhouse Gas Inventory & Carbon Tracking

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Annual GHG inventories require collecting Scope 1 (direct emissions from campus boilers, fleet vehicles, refrigerants), Scope 2 (purchased electricity, steam, chilled water), and increasingly Scope 3 (commuting, business travel, procurement) data from 10+ sources — utility bills, fleet management logs, travel reimbursement systems, commuter surveys, and procurement records. Most institutions use SIMAP (Sustainability Indicator Management & Analysis Platform) for calculations but spend 200–400 hours per year on data collection alone. Manual entry errors cascade through emission factor calculations, producing unreliable trend data that undermines climate action planning.

#### The Solution
monday.com serves as the data staging and workflow layer between raw source data and SIMAP. A GHG Data Collection board organizes data requests by Scope and source, with columns for: Data Source (dropdown), Responsible Party (people), Reporting Period (date range), Raw Data (files), Data Status (status), Emission Factor (number), Calculated Emissions (formula), Verification Notes (long text). Automations trigger data requests quarterly (not just annually), creating a rolling collection cadence that distributes workload. Dashboard widgets visualize emissions trends by scope and source in real-time.

#### The Outcome
Reduce GHG inventory preparation time from 400 hours to under 100 hours annually. Shift from annual to quarterly data collection, enabling mid-year course corrections. Improve data accuracy by 30%+ through structured collection and automated validation. Enable real-time progress tracking toward carbon neutrality commitments.

#### Discovery Questions
- "What's your current process for collecting utility data across campus buildings — do you pull it manually from utility portals?"
- "How do you handle Scope 3 emissions like commuter travel and procurement? Is that even in scope for your current inventory?"
- "How many hours does your team spend on the annual GHG inventory, and who does the heavy lifting?"
- "Have you ever had your GHG data audited or third-party verified? How confident are you in the accuracy?"
- "What's your institution's carbon neutrality target date, and how do you track progress toward it?"

#### Industry Context
Most institutions use SIMAP (formerly Clean Air-Cool Planet's Campus Carbon Calculator) for GHG calculations. The GHG Protocol (WRI/WBCSD) provides the accounting framework. Scope 3 is increasingly expected — especially commuting (often the largest source) and purchased goods. Many institutions pursue third-party verification through organizations like the Climate Registry. Carbon neutrality pledges create board-level accountability for annual trend data.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'GHG Inventory Data Collection' board in monday.com. Groups: Scope 1 (Direct Emissions), Scope 2 (Purchased Energy), Scope 3 (Indirect/Value Chain). Items represent individual data sources (e.g., 'Natural Gas — Main Campus', 'Electricity — North Campus', 'Fleet Diesel', 'Refrigerant Losses', 'Employee Commuting', 'Business Air Travel', 'Purchased Goods'). Columns: Data Source Name (text), Source Category (dropdown: Stationary Combustion, Mobile Combustion, Fugitive Emissions, Purchased Electricity, Purchased Steam, Commuting, Business Travel, Waste, Procurement), Building/Fleet ID (text), Responsible Party (people), Reporting Quarter (dropdown: Q1, Q2, Q3, Q4), Fiscal Year (dropdown: FY2024, FY2025, FY2026), Raw Data File (files), Unit of Measure (dropdown: therms, kWh, gallons, miles, tons, kg), Quantity (number), Emission Factor (number), CO2e Metric Tons (formula: Quantity × Emission Factor / 1000), Data Quality (status: Estimated, Metered, Verified), Collection Status (status: Not Requested, Requested, Received, Validated, Complete), Notes (long text). Add automations: On the 1st of each quarter, create subitems for each data source requesting that quarter's data and notify Responsible Party; when Collection Status changes to 'Received', notify the Sustainability Analyst for validation. Create a Dashboard with: (1) stacked bar chart of CO2e by Scope and quarter, (2) numbers widget showing total annual CO2e, (3) chart showing year-over-year emissions trend, (4) table of outstanding data requests."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Carbon Pulse
**Agent Purpose:** Automate GHG data collection workflows, validate incoming data, and generate real-time emissions dashboards.

**Triggers:**
- First business day of each quarter (automated data request cycle)
- When a raw data file is uploaded to any GHG item
- When CO2e calculation exceeds ±20% of same-period prior year (anomaly detection)
- Monthly scheduled summary generation
- When all items in a Scope group reach "Complete" status

**Actions:**
- Generate and send quarterly data request emails to each Responsible Party with specific instructions (e.g., "Please upload natural gas bills for Main Campus, Jan–Mar 2026, in therms")
- Parse uploaded utility bills and extract consumption quantities (kWh, therms, gallons)
- Flag anomalies — e.g., if electricity consumption for a building drops 50% quarter-over-quarter, flag for investigation (meter error? renovation? data entry mistake?)
- Calculate running annual total and project year-end emissions against carbon neutrality glide path
- Generate quarterly GHG summary report with narrative context for leadership
- When all scopes are complete, prepare SIMAP import file

**Data Required:**
- Historical GHG inventory data (3+ years for trend analysis)
- Campus building directory with square footage and primary use
- Emission factors database (EPA eGRID for electricity, standard factors for fuels)
- Carbon neutrality commitment date and interim milestones
- Integration with utility data portals (where available via API)

**Autonomy Level:** Escalation-Based
Routine data collection and validation is fully autonomous. Anomalies exceeding 20% variance are escalated to the Sustainability Analyst. Final inventory sign-off requires CSO approval.

**Example Interaction:**
> Carbon Pulse receives an uploaded Excel file for Q3 electricity data from the Facilities energy manager. It parses the file and finds consumption for Harrison Science Building at 892,000 kWh — a 43% increase over Q3 last year (624,000 kWh). The agent flags this as an anomaly: "⚠️ Harrison Science Building Q3 electricity consumption is 43% above Q3 FY2025. Possible explanations: new lab equipment, extended operating hours, or data entry error. The emission impact is approximately +118 MTCO2e. Please verify the data and provide context." It updates the item status to "Needs Review" and adds a note. Meanwhile, it successfully validates 14 other building entries that fall within normal ranges, marks them "Validated," and updates the running Q3 total. The dashboard now shows the institution at 34,200 MTCO2e year-to-date — 2.1% above the glide path for carbon neutrality by 2040.

---

### Use Case 3: Campus Sustainability Action Plan Project Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Climate Action Plans (CAPs) and Sustainability Strategic Plans typically contain 50–100+ action items spanning 5–10 year horizons, assigned to dozens of departments. After the plan is published with great fanfare, implementation tracking falls apart within 6–12 months. Actions get siloed in department-specific spreadsheets, progress reporting is quarterly at best (and often annual), and there's no centralized view of which initiatives are on track, which are stalled, and where resources should be redirected. When the president or board asks "where are we on the Climate Action Plan?" the answer takes weeks to compile.

#### The Solution
monday.com Work Management serves as the CAP implementation hub. A master board maps every action item with columns for: Goal Area (dropdown: Energy, Transportation, Waste, Water, Procurement, Curriculum, Engagement), Action Item (text), Lead Department (dropdown), Responsible Person (people), Timeline (timeline), Status (status: Not Started, Planning, In Progress, Complete, Deferred), % Complete (number), Milestones (subitems), Budget Required (number), Budget Secured (number), CO2e Impact (number), Priority (dropdown: Quick Win, Strategic, Long-Term). A high-level Dashboard provides the "one-slide answer" for board meetings, showing overall plan completion, progress by goal area, and projected emissions reductions.

#### The Outcome
Transform the CAP from a static PDF into a living project portfolio. Enable quarterly board reporting in minutes instead of weeks. Surface stalled initiatives early so resources can be redirected. Connect individual actions to aggregate emissions impact, showing which initiatives are delivering the most carbon reduction per dollar invested.

#### Discovery Questions
- "When was your current Climate Action Plan or Sustainability Strategic Plan published, and how do you currently track implementation?"
- "How often does the board or president ask for a sustainability progress update, and how long does it take to compile?"
- "Are there action items in your plan that you know have stalled? What's blocking them?"
- "How do you prioritize between competing sustainability initiatives when budget is limited?"
- "Do you track the actual emissions reduction impact of each initiative, or just completion status?"

#### Industry Context
Most universities develop CAPs as part of their carbon neutrality commitment (Presidents' Climate Leadership Commitments). Plans typically cover Energy & Buildings, Transportation, Waste & Materials, Water, Food & Dining, Procurement, Curriculum & Research, and Community Engagement. AASHE recommends updating CAPs every 5 years. The plan is often developed through a participatory process with a Sustainability Committee or Council that includes faculty, staff, students, and administrators.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 'Climate Action Plan Tracker' in monday.com. Create groups for each goal area: Energy & Buildings, Transportation & Fleet, Waste & Materials, Water, Sustainable Procurement, Curriculum & Research, Campus Engagement, Governance & Planning. Each item is an action item from the CAP. Columns: Action ID (text, e.g., E-1, T-3), Action Description (text), Lead Department (dropdown: Facilities, Transportation, Dining, Procurement, Provost Office, Student Affairs, Finance, HR, IT, Communications), Responsible Person (people), Implementation Timeline (timeline), Status (status: Not Started, Planning, In Progress, On Hold, Complete, Deferred), Completion % (number), Priority Level (dropdown: Quick Win <1yr, Medium-Term 1-3yr, Long-Term 3-5yr, Transformational 5-10yr), Estimated Annual CO2e Reduction (number, in MTCO2e), Estimated Cost (number), Funding Status (status: Not Funded, Partially Funded, Fully Funded, Self-Funding), Funding Source (text), Notes (long text), Last Progress Update (date). Use subitems for milestones within each action. Create a Dashboard with: (1) a stacked bar chart showing action status by goal area, (2) a numbers widget for total estimated CO2e reduction from completed actions, (3) a chart showing funding status distribution, (4) a table filtered to 'On Hold' and 'Not Started' items sorted by CO2e Reduction (highest impact stalled items), (5) a battery widget showing overall CAP completion %. Add automations: if Last Progress Update is older than 90 days, change status to 'Needs Update' and notify Responsible Person; when Status changes to Complete, notify CSO."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Plan Pulse
**Agent Purpose:** Keep the Climate Action Plan alive by proactively tracking milestones, chasing owners, and generating leadership-ready progress reports.

**Triggers:**
- Monthly scheduled review (first Monday of each month)
- When any action item has no progress update in 90+ days
- When Status changes to "On Hold" or "Deferred"
- Quarterly board meeting preparation (triggered manually or by calendar)
- When a new fiscal year budget is approved

**Actions:**
- Send personalized monthly check-in messages to action owners requesting progress updates
- Identify "zombie" actions (no updates in 6+ months) and recommend to CSO: continue, restructure, or formally defer
- Generate quarterly board presentation summary: % complete by goal area, top 5 achievements this quarter, top 5 at-risk items, cumulative CO2e reduced
- When budget is approved, cross-reference funded vs. unfunded actions and recommend which "Not Funded" items could now proceed
- Calculate ROI (CO2e reduction per dollar invested) for completed actions and rank remaining items by projected ROI

**Data Required:**
- Climate Action Plan document with all action items and timelines
- Annual budget allocations by department
- GHG inventory data (for impact verification)
- Board meeting calendar

**Autonomy Level:** Human-in-the-Loop
Agent autonomously sends check-ins and generates reports, but recommendations to defer or restructure actions require CSO approval. Board-facing reports are generated as drafts for CSO review.

**Example Interaction:**
> Plan Pulse conducts its monthly review and identifies that Action T-4 ("Install 200 EV charging stations by 2028") has been in "Planning" status for 14 months with no progress update since August 2025. The agent messages the Transportation Director: "Hi James — Action T-4 (EV Charging Expansion) has been in Planning for 14 months. Current status shows 0 of 200 stations installed. This action is projected to reduce Scope 3 commuting emissions by 340 MTCO2e/year. Can you provide an update on blockers? Common issues I've seen: electrical infrastructure costs, parking lot prioritization, or vendor selection delays. If you need budget approval, I can flag this to the CSO with a cost-benefit summary." It also drafts a slide for the quarterly board deck: "Transportation Goal Area: 35% complete. Highlight: Bike-share program (T-2) exceeded ridership targets by 22%. At-Risk: EV charging (T-4) has stalled — recommend CSO intervention."

---

### Use Case 4: Sustainable Procurement & Vendor Compliance Tracking

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Sustainable procurement policies require tracking vendor sustainability certifications (Fair Trade, FSC, Energy Star, EPEAT, Green Seal), local sourcing percentages, minority/women-owned business spend, and Scope 3 procurement emissions — across thousands of purchase orders and hundreds of vendors. Procurement teams rarely have the bandwidth to enforce sustainability criteria, and sustainability offices lack visibility into purchasing decisions. STARS credits OP-11 (Sustainable Procurement) and OP-12 (Electronics Purchasing) require specific metrics that are nearly impossible to extract from ERP systems without manual analysis.

#### The Solution
monday.com CRM and Work Management combine to create a Sustainable Vendor Registry. Each vendor is an item with columns for: Vendor Name (text), Category (dropdown: Office Supplies, Lab Equipment, Food & Dining, Electronics, Furniture, Maintenance, Construction), Sustainability Certifications (tags: Fair Trade, FSC, Energy Star, EPEAT, Green Seal, B-Corp, LEED, Organic), Local (within 250 miles) (checkbox), Diversity Classification (dropdown: MBE, WBE, SDVOB, None), Annual Spend (number), Sustainability Score (number, 1-100), Contract Expiration (date), Compliance Status (status). A connected board links POs to vendors, tracking sustainable vs. conventional purchasing ratios.

#### The Outcome
Increase sustainable procurement spend from typical 15–25% to 40%+ within 2 years. Automate STARS procurement credit data collection. Give procurement officers real-time visibility into sustainability-preferred vendors. Reduce vendor qualification time from weeks to days.

#### Discovery Questions
- "Does your institution have a sustainable procurement policy, and how well is it actually enforced at the departmental level?"
- "How do you currently track which vendors hold sustainability certifications?"
- "What percentage of your total procurement spend would you classify as 'sustainable,' and how do you define that?"
- "When it comes time for STARS reporting, how do you pull procurement data — is it a manual process?"
- "Are there categories where sustainable alternatives are readily available but not being adopted? What's blocking adoption?"

#### Industry Context
Higher ed procurement is highly decentralized — individual departments often have purchasing authority, making policy enforcement difficult. Key frameworks include AASHE STARS procurement credits, the Sustainable Purchasing Leadership Council (SPLC) guidance, and EPA's Comprehensive Procurement Guidelines. P-card (purchasing card) transactions are particularly hard to track for sustainability compliance. Group purchasing organizations (GPOs) like E&I Cooperative and OMNIA Partners can negotiate sustainability requirements at scale.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'Sustainable Vendor Registry' board in monday.com. Groups: Office & General Supplies, Technology & Electronics, Food & Dining, Lab & Research, Furniture & Furnishings, Facilities & Maintenance, Professional Services. Each item is a vendor. Columns: Vendor Name (text), Primary Contact (people), Contract Value (number), Contract End Date (date), Sustainability Certifications (dropdown multi-select: Fair Trade, FSC, Energy Star, EPEAT, Green Seal, B-Corp, Organic, Rainforest Alliance, LEED, Cradle to Cradle), Local Vendor <250mi (checkbox), Diversity Status (dropdown: MBE, WBE, SDVOB, HUBZone, None), Sustainability Score (number, 0-100), Compliance Status (status: Preferred, Approved, Conditional, Under Review, Non-Compliant), Last Audit Date (date), Notes (long text), Spend YTD (number). Create a Dashboard with: (1) pie chart of spend by compliance status, (2) numbers widget showing % of total spend with 'Preferred' vendors, (3) chart showing certification distribution across vendors, (4) table of vendors with expired or missing certifications. Add automation: when Contract End Date is within 60 days, notify Procurement and Sustainability Office to review sustainability requirements before renewal."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Green Buyer
**Agent Purpose:** Proactively identify sustainable vendor alternatives, track certification compliance, and flag procurement decisions that conflict with sustainability policy.

**Triggers:**
- When a new purchase requisition exceeds $5,000 and the selected vendor has no sustainability certifications
- When a vendor's certification expires
- Monthly spend analysis (first of each month)
- When a new vendor is added to the registry without sustainability data
- STARS reporting cycle kickoff

**Actions:**
- Flag non-certified vendor selections and suggest certified alternatives from the registry
- Send certification renewal reminders to vendors 90 days before expiration
- Generate monthly sustainable procurement ratio report (sustainable spend / total spend by category)
- Auto-populate STARS OP-11 and OP-12 data fields from vendor registry and spend data
- Research and recommend new sustainable vendors for categories with low sustainable coverage
- Alert when departmental spending patterns deviate from sustainability policy

**Data Required:**
- Vendor registry with certification data
- ERP/procurement system purchase order data
- Sustainability certification databases (Energy Star, EPEAT, etc.)
- Institutional sustainable procurement policy document
- STARS credit requirements for OP-11 and OP-12

**Autonomy Level:** Escalation-Based
Routine certification tracking and reporting is autonomous. Vendor recommendations and policy violation flags are sent to Procurement Director for action. New vendor additions require human review.

**Example Interaction:**
> A Biology department lab manager submits a $12,000 purchase requisition for lab glassware from a vendor not in the sustainable registry. Green Buyer intercepts: "This PO is for Fischer Scientific (no sustainability certifications on file). Alternative: Karter Scientific (Green Seal certified, B-Corp) offers comparable borosilicate glassware at ~8% premium ($12,960). Your department's sustainable procurement ratio is currently 31% (target: 40%). Switching would bring it to 34%. Would you like me to route this to the Procurement Director for a sustainable sourcing review, or proceed with the original vendor?" The agent logs the decision either way for STARS reporting.

---

### Use Case 5: Campus Waste Diversion & Zero-Waste Program Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Zero-waste goals (common targets: 90% diversion by 2030) require tracking waste streams across dozens of buildings, dining halls, residence halls, labs, and event venues. Waste audits are labor-intensive (literally sorting trash by hand), contamination in recycling streams undermines diversion rates, and composting programs require coordination between dining services, custodial staff, and haulers. Most institutions can't answer basic questions like "what's our current diversion rate?" without waiting for quarterly hauler reports and manually calculating tonnage. Special waste streams — hazardous lab waste, e-waste, construction debris — have their own regulatory requirements.

#### The Solution
monday.com Work Management creates a Waste Management Operations Hub. One board tracks waste streams by building/zone with monthly tonnage inputs for landfill, recycling, compost, and special waste. Another board manages waste audit schedules, findings, and corrective actions. A third board tracks zero-waste initiatives (new bin stations, signage campaigns, dining hall composting expansion) as projects with timelines and owners. Dashboards calculate real-time diversion rates and visualize trends by building, stream, and month.

#### The Outcome
Achieve real-time diversion rate tracking instead of quarterly lag reporting. Identify contamination hotspots and target education campaigns. Reduce waste audit coordination time by 60%. Connect waste reduction initiatives to measurable diversion improvements. Provide STARS OP-18 (Waste Minimization & Diversion) data on demand.

#### Discovery Questions
- "What's your current campus-wide waste diversion rate, and how confident are you in that number?"
- "How often do you conduct waste audits, and what happens with the findings?"
- "Where are your biggest contamination problems — residence halls, dining, academic buildings?"
- "Do you have visibility into waste generation at the building level, or only campus-wide totals?"
- "How do you coordinate between custodial staff, dining services, and your waste hauler on contamination issues?"

#### Industry Context
Zero-waste is typically defined as 90% diversion from landfill. Key waste streams in higher ed: municipal solid waste (MSW), single-stream recycling, organic/compost (especially food waste from dining), construction & demolition (C&D), hazardous waste (lab chemicals), electronic waste, and universal waste (fluorescent bulbs, batteries). The EPA's WasteWise program and Post-Landfill Action Network (PLAN) are common partners. Many states have mandatory commercial composting laws (e.g., Vermont Act 148, California SB 1383).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 'Waste Diversion Tracker' board in monday.com. Groups by campus zone: North Campus, South Campus, Central Campus, Athletics, Residential, Dining Facilities. Each item is a building or venue. Columns: Building Name (text), Building Code (text), Primary Use (dropdown: Academic, Administrative, Residential, Dining, Athletics, Research Lab, Mixed-Use), Landfill Tons/Month (number), Recycling Tons/Month (number), Compost Tons/Month (number), Special Waste Tons/Month (number), Total Waste (formula: sum of all streams), Diversion Rate (formula: (Recycling + Compost + Special) / Total × 100), Target Diversion Rate (number, default 90), Status (status: On Track, At Risk, Below Target), Last Audit Date (date), Contamination Level (dropdown: Low <5%, Moderate 5-15%, High >15%), Notes (long text). Create a second board called 'Waste Audit Schedule' with items for each planned audit: Building (connect to Waste Tracker), Audit Date (date), Audit Lead (people), Status (status: Scheduled, In Progress, Complete, Cancelled), Findings Summary (long text), Contamination Rate (number), Top Contaminants (tags), Corrective Actions (subitems). Dashboard: (1) campus-wide diversion rate gauge, (2) bar chart of diversion rate by building, (3) trend line of monthly diversion rate over 12 months, (4) table of buildings below target diversion rate."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Zero Waste Watcher
**Agent Purpose:** Monitor waste diversion performance, coordinate audit follow-ups, and recommend targeted interventions for underperforming buildings.

**Triggers:**
- Monthly when new waste tonnage data is entered
- When any building's diversion rate drops below 50%
- After a waste audit is marked "Complete"
- When contamination level is updated to "High"
- Quarterly summary generation

**Actions:**
- Calculate and update diversion rates for all buildings when new data is entered
- After a waste audit, create corrective action subitems based on findings (e.g., "Install composting bins on 3rd floor", "Schedule recycling training for custodial staff")
- Identify the 5 lowest-performing buildings and generate targeted improvement plans
- When contamination is "High," notify custodial supervisor and create a signage/education campaign task
- Generate quarterly waste report for STARS OP-18 credit documentation
- Trend analysis: flag buildings where diversion rate has declined 3+ consecutive months

**Data Required:**
- Monthly waste tonnage by stream and building (from hauler reports)
- Waste audit records and contamination data
- Building occupancy and usage data
- Campus event calendar (events generate spike waste)
- Custodial staff assignments by building

**Autonomy Level:** Human-in-the-Loop
Data calculations and trend monitoring are autonomous. Corrective action plans are generated as recommendations for the Waste Reduction Coordinator to approve and assign. Signage and education campaign launches require sustainability office approval.

**Example Interaction:**
> Zero Waste Watcher processes March tonnage data and flags Whitman Residence Hall: diversion rate dropped from 42% to 28% — the third consecutive monthly decline. The agent analyzes audit history and finds the last waste audit was 8 months ago, with high contamination noted in recycling bins (food waste in single-stream). It generates a recommendation: "Whitman Hall diversion rate has declined 14 points over 3 months. Recommended actions: (1) Schedule waste audit within 2 weeks — creating task and assigning to next available auditor. (2) Deploy contamination education campaign — posters, bin toppers, and RA training session. (3) Consider adding compost bins to each floor kitchen — dining compost program saw 15% diversion improvement in Morrison Hall after similar deployment. Estimated cost: $2,400 for bins + signage." The corrective actions are created as subitems awaiting coordinator approval.

---

### Use Case 6: Sustainability Communications & Engagement Campaign Tracking

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Sustainability engagement requires reaching diverse audiences — students (who turn over every 4 years), faculty, staff, administrators, and community members — with campaigns around Earth Month, RecycleMania, Move-Out waste collection, energy competitions, sustainability pledge programs, and more. Events and campaigns are planned in email threads and personal to-do lists, social media posts aren't coordinated with events, and there's no way to measure whether engagement campaigns actually change behavior. STARS EN credits require documenting outreach programs, and most offices can't easily compile a comprehensive list of what they did all year.

#### The Solution
monday.com Work Management creates a Sustainability Engagement Hub. A Campaign Calendar board lists all events and campaigns with: Event Name (text), Type (dropdown: Competition, Workshop, Awareness Campaign, Volunteer Event, Speaker Series, Tabling), Target Audience (dropdown: Students, Faculty, Staff, All Campus, Community), Date (date/timeline), Lead (people), Status (status), Estimated Reach (number), Actual Attendance (number), Social Media Posts (subitems), Budget (number), STARS Credit (dropdown: EN-1 through EN-14). A content calendar connected board manages social posts, newsletter content, and web updates.

#### The Outcome
Coordinate 30–50+ annual sustainability events and campaigns from one place. Demonstrate engagement impact for STARS credits with actual attendance and reach data. Reduce planning time by 40% through templates and automations. Build institutional memory — when staff turns over, the playbook stays.

#### Discovery Questions
- "How many sustainability-related events or campaigns does your office run annually, and how do you plan them?"
- "Do you have metrics on engagement — attendance, participation rates, behavior change?"
- "How do you coordinate sustainability messaging across social media, newsletters, and website?"
- "When RecycleMania or Earth Month comes around, is it planned fresh each year or do you have templates?"
- "How do you document engagement activities for STARS reporting?"

#### Industry Context
Key higher ed sustainability engagement programs: RecycleMania (now the Campus Race to Zero Waste), AASHE conference, Campus Sustainability Month (October), Earth Month (April), Green Office/Lab certification programs, Eco-Rep/Sustainability Ambassador student programs, bike-to-campus challenges, energy reduction competitions between residence halls. Student engagement is critical but challenging due to 25% annual turnover.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'Sustainability Engagement Hub' board in monday.com. Groups by time period: Fall Semester, Spring Semester, Summer, Ongoing Programs. Items are events/campaigns. Columns: Event Name (text), Event Type (dropdown: Competition, Workshop, Speaker Event, Volunteer Day, Awareness Campaign, Tabling, Digital Campaign, Certification Program), Target Audience (dropdown: Undergrads, Grad Students, Faculty, Staff, All Campus, Community), Date/Period (timeline), Location (text), Lead Organizer (people), Supporting Team (people), Status (status: Ideation, Planning, Promotion, Live, Complete, Cancelled), Budget (number), Actual Spend (number), Expected Attendance (number), Actual Attendance (number), Social Media Impressions (number), Related STARS Credit (dropdown: EN-1 through EN-14), Post-Event Survey Link (link), Key Takeaways (long text). Use subitems for task checklists: venue booking, catering, speakers confirmed, promotional materials, social posts scheduled, post-event report. Create automations: 30 days before event date, change Status to 'Planning' and notify Lead; 7 days before, change to 'Promotion'; day after event, change to 'Complete' and prompt for Actual Attendance and Key Takeaways. Dashboard: (1) calendar view of all events, (2) numbers widget for total annual reach (sum of Actual Attendance), (3) bar chart of events by type, (4) pie chart of audience distribution."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Engage Engine
**Agent Purpose:** Streamline sustainability event planning, automate promotional workflows, and measure engagement impact across campaigns.

**Triggers:**
- When a new event item is created
- 30/14/7/1 days before event date (progressive planning prompts)
- When Status changes to "Complete"
- End of each semester (impact report generation)
- When a recurring annual event date approaches (template duplication)

**Actions:**
- When a new event is created, auto-populate a task checklist based on event type (e.g., Speaker Event template: confirm speaker, book room, create flyer, schedule social posts, arrange A/V, send RSVPs)
- Generate social media post drafts for each event (tailored by platform — Instagram, Twitter, campus newsletter)
- After event completion, send post-event survey to attendees and compile results
- Generate semester-end engagement impact report: total events, total attendance, engagement per dollar spent, STARS credit coverage
- For recurring events (e.g., Earth Month), duplicate last year's items as templates with updated dates

**Data Required:**
- Event history and attendance records
- Social media account access for post scheduling
- Campus event calendar for conflict checking
- STARS EN credit requirements
- Email/newsletter distribution lists

**Autonomy Level:** Human-in-the-Loop
Task checklist creation and reminder workflows are autonomous. Social media post drafts and survey creation require organizer approval before publishing. Impact reports are generated as drafts for CSO review.

**Example Interaction:**
> It's September 1st and Engage Engine detects that Campus Sustainability Month (October) is 30 days away. It duplicates last year's October campaign board as a template, updating all dates to 2026. It notifies the Engagement Coordinator: "October is Sustainability Month! I've created your campaign board based on last year's 12 events. Last year's highlights: Sustainability Fair (420 attendees), Dorm Energy Challenge (15% avg reduction, 8 halls participated), Faculty Research Showcase (85 attendees). Three items need immediate attention: (1) Keynote speaker — last year you booked Dr. Ayana Elizabeth Johnson in June, 4 months ahead. Want me to draft an outreach email? (2) Dorm Energy Challenge — last year's baseline data collection started Sept 15. I've created a task for Facilities to pull current meter readings. (3) Sustainability Fair vendor invitations — last year 23 of 30 invited vendors participated. I've pre-populated the vendor list from last year with contact info."

---

### Use Case 7: Transportation Demand Management & Commuter Survey Program

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Commuter transportation is often the single largest source of Scope 3 GHG emissions for universities — sometimes exceeding all building energy emissions combined. Sustainability offices are expected to track commuter mode split (drive alone, carpool, transit, bike, walk, remote), manage alternative transportation programs (bike share, transit pass subsidies, EV charging, carpool matching), and conduct annual commuter surveys to measure progress. The survey alone — design, distribution, analysis, reporting — can consume 200+ staff hours. Meanwhile, transportation programs operate in silos (parking manages permits, facilities manages bike racks, transit agency manages passes), and there's no holistic view of modal shift progress.

#### The Solution
monday.com Work Management connects all transportation programs in one workspace. A Transportation Programs board tracks each initiative (bike share, transit subsidy, EV charging, carpool platform, remote work policy) with status, participation metrics, and emissions impact. A Commuter Survey board manages the survey lifecycle: questionnaire design, distribution, response tracking, analysis, and reporting. Connected dashboards show mode split trends, program participation, and associated Scope 3 emissions.

#### The Outcome
Reduce commuter survey administration time by 50%. Consolidate all transportation program data for integrated reporting. Track modal shift in real-time through program participation data (not just annual surveys). Automate STARS OP-15 (Campus Fleet) and OP-16 (Commute Modal Split) data compilation.

#### Discovery Questions
- "Do you know your current commuter mode split, and when was it last measured?"
- "What alternative transportation programs do you offer, and how do you track participation across them?"
- "How do you conduct your commuter survey — is it centrally managed or does each department handle it differently?"
- "What's your biggest barrier to reducing drive-alone commuting — awareness, infrastructure, or policy?"
- "How do you calculate commuting-related GHG emissions for your inventory?"

#### Industry Context
Best practice is annual commuter surveys with 20%+ response rates. Key metrics: drive-alone rate (national university average ~50-60%), average commute distance, mode split by category (SOV, carpool, transit, bike, walk, remote). Programs: Universal Transit Pass (UPass), Bike Share (Zagster, BCycle), Guaranteed Ride Home, Carpool matching (RideAmigos, Luum), EV charging (ChargePoint, Blink). Many institutions participate in the National Transit Database for benchmarking.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'Transportation Programs Hub' board in monday.com. Groups: Active Programs, Planned Programs, Completed/Archived. Items are individual transportation initiatives. Columns: Program Name (text), Category (dropdown: Transit, Cycling, Carpool, EV, Pedestrian, Remote Work, Fleet, Parking Management), Program Lead (people), Launch Date (date), Status (status: Pilot, Active, Expanding, Paused, Complete), Annual Budget (number), Participants This Year (number), Participants Last Year (number), Growth Rate (formula: (This Year - Last Year)/Last Year × 100), Estimated Annual CO2e Avoided (number), STARS Credit (dropdown: OP-15, OP-16, OP-17), Notes (long text). Create a second board: 'Commuter Survey Manager' with items for each survey cycle. Columns: Survey Year (text), Survey Period (timeline), Target Population (number), Responses Received (number), Response Rate (formula), Drive Alone % (number), Carpool % (number), Transit % (number), Bike % (number), Walk % (number), Remote % (number), Average Commute Miles (number), Status (status: Design, Distribution, Collection, Analysis, Complete), Survey Link (link), Report (files). Dashboard: (1) bar chart of mode split trend over 3+ years, (2) numbers widget for current drive-alone rate, (3) chart showing program participation trends, (4) table of active programs with participation vs. budget (cost per participant)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Commute Coach
**Agent Purpose:** Manage transportation program performance tracking, automate commuter survey workflows, and identify opportunities to shift commuter behavior.

**Triggers:**
- Annual commuter survey launch date (typically September/October)
- When survey response rate milestone is reached (10%, 20%, target)
- Monthly program participation data update
- When a new EV charging station or bike rack is installed
- When drive-alone rate increases quarter-over-quarter

**Actions:**
- Generate survey reminder emails at 1-week, 2-week, and final-day milestones, segmented by audience (faculty, staff, students)
- Analyze survey results and auto-populate mode split fields with calculated percentages
- Compare current survey results to prior years and highlight statistically significant changes
- Calculate commuting GHG emissions using EPA emission factors and survey-derived VMT
- Recommend program investments based on cost-per-CO2e-avoided analysis (e.g., "Expanding transit subsidies from 50% to 75% is projected to shift 3% more commuters to transit at $420/MTCO2e avoided — more cost-effective than the EV program at $890/MTCO2e")
- Flag programs with declining participation for review

**Data Required:**
- Historical commuter survey data (3+ years)
- Program participation and cost data
- Campus employee/student directory for survey distribution
- EPA commuting emission factors
- Local transit schedules and routes

**Autonomy Level:** Human-in-the-Loop
Survey distribution and reminder workflows are autonomous. Analysis and recommendations are generated as reports for Transportation Coordinator and CSO review. GHG calculations are validated against SIMAP before official reporting.

**Example Interaction:**
> The fall commuter survey closes with 4,200 responses (22% response rate — up from 18% last year). Commute Coach processes the results overnight: "Survey Complete — Key Findings: Drive-alone rate decreased from 54% to 49% — the first time below 50%! Transit usage up from 18% to 22%, likely driven by the new UPass unlimited program launched in August. Cycling flat at 8% despite new bike lanes. Remote work up from 12% to 15%. Estimated commuting emissions: 18,400 MTCO2e (down 11% from last year). 🎉 Biggest win: UPass program. 📊 Recommendation: Cycling infrastructure is underperforming — consider a bike tune-up subsidy or e-bike lending library. 23% of respondents cited 'distance' as barrier to cycling; e-bikes address this. I've drafted the STARS OP-16 credit update with these numbers."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| STARS | Sustainability Tracking, Assessment & Rating System — the leading higher ed sustainability rating framework by AASHE |
| AASHE | Association for the Advancement of Sustainability in Higher Education |
| SIMAP | Sustainability Indicator Management & Analysis Platform — GHG calculator for higher ed |
| CAP | Climate Action Plan — institutional roadmap to carbon neutrality |
| MTCO2e | Metric Tons of Carbon Dioxide Equivalent — standard GHG measurement unit |
| Scope 1/2/3 | GHG emission categories: direct (1), purchased energy (2), indirect value chain (3) |
| Diversion Rate | Percentage of total waste diverted from landfill through recycling, composting, or reuse |
| Mode Split | Distribution of commuters across transportation modes (car, transit, bike, walk, remote) |
| EPEAT | Electronic Product Environmental Assessment Tool — green electronics standard |
| UPass | Universal Transit Pass — subsidized or free transit for students/employees |
| RecycleMania | Annual college recycling competition (now Campus Race to Zero Waste) |
| GHG Protocol | The international standard for corporate/institutional GHG accounting |
| Presidents' Climate Leadership Commitments | Formerly the American College & University Presidents' Climate Commitment (ACUPCC) |
| eGRID | EPA's Emissions & Generation Resource Integrated Database — regional electricity emission factors |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Sustainability Officer (CSO) | Leads sustainability strategy, reports to VP/Provost/President | Decision-maker |
| Sustainability Director/Manager | Day-to-day operations of sustainability office | Decision-maker |
| Sustainability Coordinator/Analyst | Data collection, reporting, program management | User/Influencer |
| VP of Facilities/Administration | Oversees buildings, energy, waste, grounds | Decision-maker |
| Director of Procurement | Purchasing policies and vendor management | Influencer |
| Director of Dining/Auxiliary Services | Food sourcing, dining waste, composting | Influencer |
| Director of Transportation/Parking | Fleet, commuter programs, parking policy | Influencer |
| Faculty Sustainability Committee Chair | Academic integration, research alignment | Influencer |
| Student Sustainability Board/Club | Student engagement, volunteer programs, advocacy | Influencer |
| President/Chancellor | Signs climate commitments, sets institutional priorities | Decision-maker (executive sponsor) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Facilities & Operations | Manages buildings, energy, waste, water — the operational backbone of sustainability | Primary cross-sell: facilities work management, maintenance tracking, energy dashboards |
| Procurement | Sustainable purchasing policy enforcement and vendor tracking | Cross-sell: CRM for vendor management, procurement workflow automation |
| IT | Technology for smart buildings, data systems, sustainability dashboards | Cross-sell: IT service management, project tracking for sustainability tech deployments |
| Finance | Budget allocation for sustainability initiatives, carbon offset purchasing | Cross-sell: budget tracking, grant management for sustainability funding |
| Student Affairs | Student engagement programs, residence life sustainability initiatives | Cross-sell: event management, student organization coordination |
| Communications/Marketing | Sustainability storytelling, annual reports, rankings promotion | Cross-sell: content calendar, campaign management |
| Provost/Academic Affairs | Curriculum integration, sustainability research, faculty engagement | Cross-sell: research project management, curriculum mapping |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SIMAP | GHG calculation engine — great at math, terrible at workflow and data collection | monday.com as the data collection/staging layer that feeds SIMAP; don't replace, complement |
| Utility Manager/EnergyCAP | Building energy tracking and utility bill management | monday.com can serve as the project management layer on top; energy data feeds into GHG boards |
| Smartsheet/Airtable | General project tracking used by some sustainability offices | Direct replacement with better dashboards, automations, and cross-department collaboration |
| iGrado/Cenergistic | Energy/sustainability consulting platforms (often bundled with services) | monday.com offers more flexibility and doesn't lock institutions into consulting contracts |
| Custom SharePoint/Excel | The most common "system" — shared drives and spreadsheets | Direct replacement; emphasize real-time dashboards vs. stale spreadsheets |
| Plan2Sustain | Sustainability action plan tracking tool | monday.com offers broader functionality beyond just plan tracking |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use SIMAP for our GHG inventory" | "SIMAP is excellent for calculations — but data collection is the bottleneck. monday.com streamlines the 200+ hours of gathering data from 10+ departments so SIMAP gets clean, timely inputs." |
| "Our team is only 3-4 people, we don't need a platform" | "That's exactly why you need one — your team of 4 coordinates sustainability across 50+ buildings and dozens of departments. monday.com extends your reach without adding headcount." |
| "We can't afford another software tool" | "What's the cost of a Sustainability Coordinator spending 400 hours on manual data collection? That's $15-20K in labor alone. monday.com pays for itself in one GHG inventory cycle." |
| "We need specialized sustainability software" | "Specialized tools do one thing well but create data silos. monday.com gives you STARS tracking AND GHG data collection AND CAP management AND procurement tracking in one connected workspace — plus it connects to every other department on campus." |
| "Our data is scattered across departments and we can't get people to use a new tool" | "That's the problem we solve. monday.com automations chase people for data so you don't have to. Departmental liaisons get simple, specific requests — not complex systems to learn." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder: Research university that streamlined STARS reporting]
- [Placeholder: University system that centralized GHG data collection]
- [Placeholder: College that improved waste diversion rates with data visibility]
- [Placeholder: Institution that consolidated sustainability project management]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
