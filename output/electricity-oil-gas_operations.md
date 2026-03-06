# Electricity, Oil & Gas × Operations Playbook

## Overview

Operations in the electricity, oil & gas sector is the backbone of energy delivery — encompassing upstream exploration and production (E&P), midstream transportation and storage, downstream refining and distribution, and power generation and grid management. This is one of the most operationally complex industries on Earth, with operations teams managing assets spread across continents, often in extreme environments (deepwater platforms, remote pipeline corridors, desert drilling sites, offshore wind farms), under intense regulatory scrutiny from agencies like PHMSA, EPA, FERC, NERC, and their international equivalents. A single operational failure — a well blowout, pipeline rupture, refinery explosion, or grid blackout — can result in billions in damages, environmental catastrophe, and loss of life.

Operations departments in energy companies typically represent 60-75% of total headcount and are organized around asset types: production operations (well management, reservoir engineering), pipeline operations (integrity management, SCADA monitoring), plant operations (refinery, processing plant, power plant management), and field operations (maintenance, inspection, construction). The operational technology (OT) environment is heavily instrumented — millions of sensors generating real-time data on pressure, temperature, flow rates, vibration, and emissions — but the work management layer that coordinates human response to this data is often shockingly manual. Operators still rely on paper-based permits, Excel-tracked maintenance schedules, and radio communications for critical safety workflows.

The industry is also in the midst of a massive energy transition. Traditional oil & gas operators are diversifying into renewables (solar, wind, hydrogen, carbon capture), creating operational complexity as they manage legacy hydrocarbon assets alongside new clean energy portfolios. Simultaneously, the workforce is aging — 50% of energy sector workers are eligible for retirement within 10 years — creating an urgent need to capture institutional knowledge and enable less experienced operators to perform at higher levels with technology assistance.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Aging workforce crisis — 50% retirement-eligible within decade. Need to enable junior operators to perform senior-level work with AI assistance. Field coordination roles are ripe for automation. |
| 2 | Scale Impact Without Overhead | High | Managing increasingly diverse asset portfolios (hydrocarbons + renewables) without proportional headcount growth. Need to do more with existing teams across geographically dispersed operations. |
| 3 | Consolidate Tech Stack with AI | Medium-High | Operations teams juggle 15-20 disconnected systems (CMMS, SCADA, ERP, GIS, permit systems, Excel). Unified workflow layer reduces friction and error rates in safety-critical processes. |

## Prioritized Use Cases

---

### Use Case 1: Integrated Maintenance Management & Turnaround Planning

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Maintenance is the single largest controllable cost in energy operations — typically 30-40% of operational expenditure. Energy companies manage three types of maintenance: routine/preventive (scheduled inspections, calibrations), corrective (break-fix), and major turnarounds (planned shutdowns of entire facilities for overhaul, typically every 3-5 years). A refinery turnaround involves 3,000-10,000 workers, 50,000+ work orders, $50-500M in spend, and 20-45 day execution windows where every day of overrun costs $1-5M in lost production. Planning a turnaround takes 12-18 months and involves coordinating maintenance planners, engineers, procurement, contractors, safety teams, and environmental compliance — typically across SAP PM, Primavera P6, Excel spreadsheets, and email. The disconnect between these systems means scope creep, missed dependencies, and budget overruns are the norm, not the exception. Industry data shows 40% of turnarounds exceed budget and 50% exceed schedule.

#### The Solution
Build a comprehensive Maintenance & Turnaround Management system in monday.com Work Management. For routine maintenance, create boards tracking preventive maintenance schedules, work order generation, technician assignment, parts availability, and completion documentation. For turnarounds, build a multi-board system: Scope Management (approved work list with engineering justification), Work Package Planning (bundled work orders with resource requirements), Resource Scheduling (craft labor allocation across timeline), Procurement Tracking (long-lead items, vendor coordination), Safety Planning (permits, hazard assessments, emergency response), and Daily Execution Tracking (progress by area/unit, issues log, schedule updates). Use Timeline views for critical path visualization. Connect to procurement boards for material availability. Build Dashboards showing turnaround progress against plan, cost tracking, safety metrics, and resource utilization.

#### The Outcome
Reduce turnaround planning labor by 35% through structured workflow and template reuse. Improve turnaround schedule adherence from 50% to 75% through better dependency tracking and daily progress visibility. Decrease turnaround cost overruns by 20% through real-time scope management and procurement coordination. Reduce routine maintenance backlog by 25% through improved work order tracking and technician scheduling. Capture institutional knowledge in structured turnaround templates for future planning cycles.

#### Discovery Questions
1. "When was your last major turnaround, and how did actual cost and duration compare to the original plan? What were the primary drivers of any variance?"
2. "How many different systems do your maintenance planners use to manage a turnaround — and where does critical information fall through the cracks between those systems?"
3. "What does your preventive maintenance compliance rate look like — what percentage of scheduled PM work orders get completed on time versus deferred?"
4. "How do you currently handle scope changes during turnaround execution — is there a formal process, or do additions get verbally approved and tracked after the fact?"
5. "With your experienced planners and operators approaching retirement, how are you capturing their turnaround planning knowledge for the next generation?"

#### Industry Context
Turnarounds (also called shutdowns or outages in power generation) are the highest-stakes operational events in energy. Key terminology: "work list" (approved scope), "work packages" (bundled work orders by unit/area), "craft labor" (skilled trades — welders, pipefitters, electricians, scaffolders), "hot work" (welding/cutting requiring special permits), "tie-ins" (connections to existing systems during shutdown), "mechanical completion" (all physical work done), "commissioning" (testing and startup). SAP Plant Maintenance is the dominant CMMS but is widely disliked for its rigidity and poor UX. Primavera P6 handles scheduling but doesn't connect well to execution tracking. The gap between planning tools and field execution is where failures occur.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Turnaround & Maintenance Management system. Create a board called 'Turnaround Work List' with columns: Work Order ID (text), Unit/Area (dropdown: CDU, VDU, FCC, Reformer, Hydrotreater, Utilities, Offsites, Tank Farm), Equipment Tag (text), Work Description (long text), Work Type (dropdown: Inspection, Repair, Replacement, Modification, Cleaning, Catalyst Change), Priority (status: Safety Critical, Production Critical, Reliability, Deferrable), Engineering Justification (long text), Estimated Hours (numbers), Estimated Cost ($K) (numbers), Craft Requirements (dropdown multi-select: Pipefitter, Welder, Electrician, Instrument Tech, Scaffolder, Insulator, Millwright, Crane Operator), Material Status (status: Not Required, On Order, Received, In Warehouse), Contractor (dropdown), Work Package (text), Approved (checkbox), Scope Change (checkbox), Execution Status (status: Not Started, In Progress, Complete, Punch List, Cancelled). Add subitems for task breakdown: Task Description (text), Predecessor Task (text), Duration Hours (numbers), Assigned Crew (people), Status (status: Waiting, In Progress, Complete, Blocked), Safety Permit Required (dropdown: None, Hot Work, Confined Space, LOTO, Excavation, Working at Height). Create a connected 'Daily Progress Tracker' board: Date (date), Unit/Area (dropdown), Planned Work Orders Today (numbers), Completed Work Orders (numbers), Carry-Over Items (numbers), Issues/Delays (long text), Safety Incidents (numbers), Manpower On-Site (numbers), Weather Impact (status: None, Minor Delay, Major Delay, Work Stopped). Create a 'Routine Maintenance' board: Equipment Tag (text), Equipment Type (dropdown: Pump, Compressor, Heat Exchanger, Valve, Instrument, Electrical, Rotating Equipment), PM Frequency (dropdown: Weekly, Monthly, Quarterly, Semi-Annual, Annual), Last PM Date (date), Next PM Due (date), Assigned Technician (people), PM Status (status: Scheduled, In Progress, Complete, Overdue, Deferred), Deferral Reason (text), Condition Notes (long text). Dashboard with: Turnaround Progress (S-curve chart: planned vs actual), Cost Tracking (budget vs actual by unit), Work Completion Rate by Area (bar chart), Safety Metrics (incidents, permits issued, near-misses), Resource Utilization (craft labor planned vs actual), PM Compliance Rate (gauge), Overdue PMs (filtered table). Automations: When Next PM Due is today, create work order and notify technician. When PM Status is 'Overdue' for 7 days, escalate to Maintenance Supervisor. When turnaround work order status changes to 'Complete', move to QC inspection queue. When Scope Change checkbox is checked, route to Turnaround Manager for approval and add to change log."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Turnaround Command Agent
**Agent Purpose:** Optimize turnaround execution by tracking progress against plan, identifying schedule risks, and coordinating resource reallocation in real-time.

**Triggers:**
- Daily progress data entered for any unit/area
- Work order status changed to 'Blocked' or 'Cancelled'
- Scope change request submitted
- Material delivery status changed (delayed/received)
- Daily 5 AM pre-shift briefing generation (scheduled)

**Actions:**
- Generate daily turnaround status report comparing actual progress to baseline plan — highlight units behind schedule with root cause and recovery options
- When work is blocked, analyze downstream dependencies and calculate schedule impact — recommend resource reallocation from ahead-of-schedule areas
- Track scope change cumulative impact on budget and schedule — alert Turnaround Manager when cumulative changes exceed 10% threshold
- Monitor material delivery tracking and flag work packages at risk due to material delays — suggest work sequence reordering
- Generate pre-shift briefing packages for each area supervisor: today's planned work, safety permits required, resource assignments, critical path items, weather considerations
- Compile lessons-learned database from daily issues for post-turnaround review

**Data Required:**
- Baseline turnaround schedule (planned dates, durations, dependencies)
- Real-time work order status updates from field supervisors
- Material procurement and delivery tracking
- Craft labor availability and allocation
- Weather forecast data
- Historical turnaround performance data

**Autonomy Level:** Escalation-Based
Daily reports and pre-shift briefings are fully automatic. Resource reallocation recommendations require Area Supervisor approval. Scope change impact assessments are auto-generated but require Turnaround Manager authorization. Schedule recovery plans are suggested but human-decided. No physical operations changes without human approval — this is a safety requirement.

**Example Interaction:**
> It's Day 8 of a 30-day refinery turnaround. The Turnaround Command Agent generates the 5 AM briefing: "Overall progress: 28% complete vs. 30% planned (0.6 days behind). Critical path impact: CDU tube bundle replacement is 1.5 days behind due to crane availability conflict. Recommendation: Redirect Crane #3 from Tank Farm area (2 days ahead of schedule) to CDU starting today. This recovers 1 day. Remaining 0.5 days recoverable by authorizing weekend overtime for pipefitting crew (est. cost: $45K, within contingency). Scope change tracker: 12 additions approved ($340K cumulative, 8.5% of original scope — approaching 10% threshold). Material alert: replacement heat exchanger for VDU arriving 2 days late from vendor — work package VDU-017 rescheduled, no critical path impact. Safety: Zero recordable incidents through Day 7. Today's permit requirements: 14 hot work, 6 confined space, 3 LOTO. Weather: Clear, high of 85°F, no restrictions."

---

### Use Case 2: Permit to Work & Safety Management System

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Permit to Work (PTW) systems are the primary safety control mechanism in energy operations. Every task that involves potential hazards — hot work (welding, cutting), confined space entry, lockout/tagout (LOTO), excavation, working at height, electrical isolation — requires a formal permit with hazard assessment, risk controls, and authorized signatures. A large refinery or production platform may process 200-500 permits daily. The process is overwhelmingly paper-based in most operations: permits are handwritten, physically carried to the work site, signed by multiple parties (issuing authority, performing authority, area authority), and filed in cabinets. This creates critical problems: permits get lost, simultaneous work conflicts aren't detected (hot work adjacent to confined space entry = explosion risk), isolation certificates aren't properly cross-referenced, and audit trails are incomplete. Paper-based PTW was a contributing factor in multiple major incidents including Piper Alpha and Texas City.

#### The Solution
Digitize the entire Permit to Work process in monday.com. Create a PTW board with permit types (hot work, confined space, LOTO, excavation, working at height, electrical, radiography), hazard assessment checklists (as subitems), isolation requirements, simultaneous operations (SIMOPS) conflict detection, multi-level authorization workflows, time-bounded validity, and close-out procedures. Use automations for conflict detection — when a new hot work permit is requested, automatically check for active confined space or gas-testing permits in the same area. Build connected boards for isolation certificates, gas test records, and safety observations. Create real-time Dashboards showing active permits by area, pending authorizations, expired permits requiring close-out, and safety statistics.

#### The Outcome
Eliminate paper-based permit processes, reducing permit issuance time from 45 minutes to 10 minutes. Detect 100% of simultaneous operations conflicts automatically (vs. 60-70% manual detection rate). Achieve complete digital audit trail for regulatory compliance. Reduce permit-related safety incidents by 40% through better hazard visibility and conflict detection. Enable remote authorization for non-safety-critical permits, reducing supervisor bottlenecks.

#### Discovery Questions
1. "Is your Permit to Work process currently paper-based, partially digital, or fully electronic — and what are the biggest pain points your supervisors and operators experience with it?"
2. "How do you currently detect simultaneous operations conflicts — for example, if someone is requesting hot work in the same area where a confined space entry is active?"
3. "What happened at your last regulatory audit of your PTW records — were there findings related to incomplete documentation, unauthorized work, or expired permits?"
4. "How many permits does your facility process on a peak day, and what's the average time from permit request to work commencement?"
5. "Have you had any safety incidents in the past 2 years where the permit to work process was identified as a contributing factor?"

#### Industry Context
PTW systems are mandated by OSHA (US), HSE (UK), and equivalent regulators globally. The hierarchy of permits typically includes: Cold Work Permit (general non-hazardous), Hot Work Permit (ignition sources), Confined Space Entry Permit, LOTO (Lockout/Tagout) for energy isolation, Excavation Permit, Working at Height Permit, Electrical Permit, and Radiography Permit. Each has specific hazard assessments and control requirements. "SIMOPS" (Simultaneous Operations) management is critical — ensuring that conflicting activities don't occur in the same area. Isolation management — ensuring equipment is properly de-energized and locked out — is one of the most life-critical processes. "Gas Free" certification is required before hot work or confined space entry, typically requiring instrument readings of LEL (Lower Explosive Limit), O2, and H2S levels.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Permit to Work & Safety Management system. Create a board called 'Active Permits' with columns: Permit Number (auto-number), Permit Type (dropdown: Hot Work, Confined Space Entry, LOTO/Isolation, Excavation, Working at Height, Electrical Work, Radiography, Cold Work/General), Work Description (long text), Location/Area (dropdown: Unit 1, Unit 2, Unit 3, Tank Farm, Offsites, Utilities, Pipe Rack, Control Room Area), Specific Equipment (text), Requesting Supervisor (people), Issuing Authority (people), Performing Authority (people), Area Authority (people), Status (status: Draft, Pending Hazard Assessment, Pending Authorization, Active, Suspended, Closed, Expired, Rejected), Valid From (date), Valid Until (date), Time Valid From (text), Time Valid Until (text), Shift (dropdown: Day, Night), SIMOPS Check (status: Clear, Conflict Detected, Override Approved), Risk Level (status: Low, Medium, High, Critical), Gas Test Required (checkbox), Gas Test Status (status: Not Required, Pending, Passed, Failed). Add subitems for hazard controls: Hazard (text: Fire/Explosion, Toxic Exposure, Fall, Engulfment, Electrocution, Crush/Strike, Oxygen Deficiency), Control Measure (text), Responsible Person (people), Verified (checkbox). Create a connected 'Isolation Certificates' board: Certificate Number (text), Equipment Isolated (text), Isolation Method (dropdown: Valve Closure, Blind/Spade, Electrical Disconnect, LOTO Lock), Isolation Point ID (text), Isolated By (people), Verified By (people), Status (status: Active, Released), Associated Permits (connect to Active Permits). Create a 'Safety Observations' board: Date (date), Observer (people), Location (text), Observation Type (dropdown: Unsafe Act, Unsafe Condition, Good Practice, Near Miss), Description (long text), Severity (status: Low, Medium, High, Critical), Corrective Action (text), Assigned To (people), Action Status (status: Open, In Progress, Closed). Dashboard with: Active Permits by Area (chart), Permits by Type (pie chart), SIMOPS Conflict Log (table), Permit Processing Time (average), Safety Observation Trends (chart), Open Corrective Actions (filtered table), Expired Permits Requiring Close-Out (alert table). Automations: When Permit Status is 'Active' and current time exceeds Valid Until, change status to 'Expired' and notify Issuing Authority. When new Hot Work permit is created in any area, check for active Confined Space permits in same area — if found, set SIMOPS Check to 'Conflict Detected' and notify both Issuing Authorities. When Safety Observation Severity is 'Critical', immediately notify Operations Manager and HSE Lead. When all hazard control subitems are verified, auto-advance permit to 'Pending Authorization'."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Safety Sentinel Agent
**Agent Purpose:** Monitor permit-to-work activities in real-time, detect hazardous conflicts, and ensure 100% safety compliance across operations.

**Triggers:**
- New permit request created
- Permit status changed to 'Active'
- Permit validity period expired
- Safety observation logged with severity 'High' or 'Critical'
- Shift change (scheduled every 12 hours)
- Gas test results entered

**Actions:**
- Perform automated SIMOPS conflict analysis when any permit is requested — check all active permits in the same area and adjacent areas for hazardous combinations (hot work + gas release, confined space + overhead crane work, etc.)
- Generate shift handover safety briefing: all active permits by area, permits expiring this shift, pending authorizations, active isolations, open safety observations
- Monitor permit expiry in real-time and escalate if work continues beyond permit validity window
- Analyze safety observation trends and identify emerging risk patterns (e.g., increasing near-misses in a specific area may indicate systemic issue)
- Cross-reference isolation certificates with active permits to ensure no work proceeds on equipment that has been de-isolated
- Generate weekly safety performance report with leading indicators (observations submitted, permits processed, conflicts detected) and lagging indicators (incidents, near-misses)

**Data Required:**
- Active permit database with location and time data
- Facility area maps with adjacency relationships
- Isolation certificate status
- Gas test results
- Safety observation history
- Shift schedules and personnel assignments
- Weather data (wind direction affects hot work near hydrocarbon areas)

**Autonomy Level:** Escalation-Based
SIMOPS conflict detection is automatic and blocks permit progression until resolved. Permit expiry alerts are automatic. Shift briefing generation is automatic. No permit can be auto-approved — all permits require human authorization (regulatory requirement). Safety observation escalations for critical severity are immediate and automatic. Trend analysis recommendations require HSE Manager review.

**Example Interaction:**
> At 2:15 PM, a field supervisor submits a Hot Work permit request for welding on a pipeline section in Area 3. The Safety Sentinel Agent immediately runs SIMOPS analysis and detects two conflicts: (1) An active Confined Space Entry permit exists for a vessel 15 meters away in the same area — the welding could create an ignition source near the open vessel, and (2) A pipeline depressurization activity is scheduled to begin in 30 minutes in the adjacent Area 2, which could release hydrocarbons downwind of the proposed hot work location. The agent blocks the permit with a clear explanation: "SIMOPS CONFLICT DETECTED. Two active hazards identified within proximity. Conflict 1: CSE Permit #247 active at Vessel V-302 (15m distance). Conflict 2: Scheduled depressurization in Area 2 at 14:45 — prevailing wind direction SW would carry any gas release toward proposed hot work location. Recommendation: Defer hot work until CSE is complete AND depressurization activity concluded and area gas-tested clear. Escalated to Area Authority and HSE for review." This automated detection potentially prevents a catastrophic incident that manual review might have missed.

---

### Use Case 3: Production Operations & Well Management Dashboard

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Production operations in oil & gas involve managing hundreds to thousands of wells, each with unique characteristics — production rates, water cut, gas-oil ratio, artificial lift systems, chemical treatment programs, and regulatory compliance requirements. Production engineers and operators struggle to maintain visibility across their well portfolios. Data sits in SCADA systems (real-time flow rates), production accounting databases (allocated volumes), reservoir engineering tools (decline curves, models), and field operator reports (wellsite observations). Identifying production optimization opportunities — wells underperforming their potential, chemical treatments that need adjustment, artificial lift systems requiring maintenance — requires manually correlating data across these systems. A production engineer responsible for 200+ wells simply cannot review each one daily. Deferred production (the gap between what wells could produce and what they actually produce) typically runs 10-20% of total production capacity, representing millions in lost revenue.

#### The Solution
Build a Production Operations Dashboard in monday.com. Each well is an item with key performance metrics: current production rate, target rate, variance, water cut, operating status, last intervention date, next scheduled maintenance, regulatory compliance status, and optimization opportunities. Use connected boards for well intervention planning (workovers, stimulations, artificial lift changes), chemical treatment tracking, and regulatory reporting. Create automated exception-based workflows — instead of reviewing every well daily, the system flags wells that have deviated from expected performance beyond configurable thresholds. Build Dashboards showing field-level production performance, deferred production waterfall, intervention pipeline, and compliance status.

#### The Outcome
Reduce deferred production by 15-25% through faster identification and resolution of well performance issues. Enable production engineers to effectively manage 2x more wells through exception-based workflows. Decrease regulatory compliance findings by 80% through automated tracking and alert systems. Reduce well intervention planning time by 40% through structured workflows and historical performance data access. Capture operational knowledge in structured formats accessible to new engineers.

#### Discovery Questions
1. "How many wells does each production engineer or foreman manage, and how do they currently prioritize which wells need attention on any given day?"
2. "What's your estimated deferred production as a percentage of total capacity, and what's your process for identifying and resolving the causes?"
3. "How many different systems does a production engineer need to access to get a complete picture of a single well's performance and history?"
4. "When a well starts declining faster than expected, how quickly does someone notice — and what's the typical response time from detection to intervention?"
5. "How do you currently track regulatory compliance across your well portfolio — state reporting deadlines, emissions monitoring, mechanical integrity tests?"

#### Industry Context
Key production metrics: BOPD (barrels of oil per day), MCFD (thousand cubic feet per day of gas), water cut (% water in produced fluids), GOR (gas-oil ratio), flowing tubing pressure (FTP), casing pressure. Artificial lift methods include rod pumps (beam pumps), ESPs (electric submersible pumps), gas lift, and plunger lift — each with different failure modes and optimization parameters. "Decline curve analysis" predicts future production based on historical trends. "Base decline" is the natural production decrease from existing wells; "adds" from new wells and interventions must offset base decline to maintain production. Regulatory requirements include monthly production reporting to state agencies (Texas Railroad Commission, Oklahoma Corporation Commission, etc.), emissions monitoring (EPA Subpart W), and mechanical integrity testing (MIT) for injection wells.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Production Operations & Well Management system. Create a board called 'Well Portfolio' with columns: Well Name (text), API Number (text), Field/Lease (dropdown), Well Type (dropdown: Oil Producer, Gas Producer, Water Injector, Gas Injector, Disposal, Shut-In, P&A), Operator Status (status: Producing, Shut-In Mechanical, Shut-In Economic, Intermittent, Workover, P&A In Progress, Regulatory Hold), Artificial Lift Type (dropdown: Rod Pump, ESP, Gas Lift, Plunger Lift, Natural Flow, Jet Pump), Current Oil Rate BOPD (numbers), Target Oil Rate BOPD (numbers), Production Variance % (formula: (Current-Target)/Target × 100), Current Gas Rate MCFD (numbers), Water Cut % (numbers), Flowing Tubing Pressure PSI (numbers), Casing Pressure PSI (numbers), Last Well Test Date (date), Next Scheduled Maintenance (date), Production Engineer (people), Field Operator (people), Last Intervention (text), Last Intervention Date (date), Regulatory Compliance (status: Current, Due Soon, Overdue, Not Applicable), Notes (long text). Create a connected 'Well Interventions' board: Well (connect to Portfolio), Intervention Type (dropdown: Workover, Stimulation/Frac, Artificial Lift Change, Chemical Treatment Adjustment, Tubing Repair, Casing Repair, Recompletion, Plug Back), Justification (long text), Estimated Cost ($K) (numbers), Expected Production Gain BOPD (numbers), Payout Days (formula: Cost / (Gain × Oil Price / 1000)), Priority (status: Urgent Safety, High ROI, Medium, Low/Deferred), Status (status: Proposed, AFE Approved, Scheduled, Rig Assigned, In Progress, Complete, Evaluating Results), Scheduled Date (date), Actual Completion Date (date), Actual Cost ($K) (numbers), Actual Production Gain BOPD (numbers), Contractor (dropdown). Create a 'Chemical Treatment Tracker' board: Well (connect), Chemical Type (dropdown: Corrosion Inhibitor, Scale Inhibitor, Paraffin Solvent, Demulsifier, Biocide, H2S Scavenger, Surfactant), Application Method (dropdown: Continuous Injection, Batch Treatment, Squeeze), Dosage Rate (text), Supplier (dropdown), Monthly Cost ($) (numbers), Last Treatment Date (date), Next Treatment Due (date), Effectiveness (status: Effective, Declining, Needs Change, Under Evaluation). Dashboard with: Field Production Summary (total oil, gas, water by field), Production Variance Top 10 Underperformers (bar chart), Deferred Production Waterfall (chart: mechanical, electrical, weather, planned, regulatory), Intervention Pipeline by Type and Status (chart), Intervention ROI Tracker (table: estimated vs actual gains), Regulatory Compliance Calendar (upcoming deadlines), Chemical Treatment Spend (chart by type). Automations: When Production Variance exceeds -15%, change well status highlight and notify Production Engineer. When Next Scheduled Maintenance date is within 7 days, create notification. When Regulatory Compliance is 'Due Soon' (30 days), notify engineer and create compliance task. When Intervention Status changes to 'Complete', trigger 30-day post-intervention production evaluation reminder."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Production Optimization Agent
**Agent Purpose:** Continuously monitor well portfolio performance, identify optimization opportunities, and recommend interventions ranked by ROI.

**Triggers:**
- Daily production data update (scheduled, morning)
- Well production rate drops more than 15% from 7-day average
- ESP or rod pump runtime anomaly detected (frequent shutdowns)
- New well test results entered
- Monthly production review (scheduled)

**Actions:**
- Analyze daily production data across entire well portfolio and generate exception report: wells with unusual declines, water cut increases, pressure changes, or artificial lift anomalies
- For each flagged well, generate diagnostic summary with probable causes ranked by likelihood (e.g., "ESP performance degradation: 70% probable based on increasing motor temperature and declining pump efficiency")
- Recommend interventions with ROI calculations: estimated cost, expected production gain, payout period, and comparison against alternative actions
- Generate monthly field performance report: production vs. plan, deferred production categorized by cause, intervention results vs. predictions, and optimization opportunities pipeline
- Track chemical treatment effectiveness and recommend dosage adjustments or product changes when performance degrades
- Flag regulatory compliance deadlines 30 and 7 days in advance with required actions

**Data Required:**
- Daily production volumes by well (SCADA or production accounting integration)
- Well test history and performance trends
- Artificial lift system parameters (pump cards, ESP performance curves)
- Historical intervention results and costs
- Chemical treatment history and lab results
- Regulatory compliance calendar
- Oil and gas price data for ROI calculations

**Autonomy Level:** Human-in-the-Loop
Production exception alerts and diagnostic reports are fully automatic. Intervention recommendations are suggestions requiring engineer review and AFE approval. Chemical treatment adjustments require operator confirmation. Regulatory compliance alerts are automatic. No physical well operations changes without human authorization.

**Example Interaction:**
> Monday morning, 6 AM. The Production Optimization Agent delivers the daily briefing to the field production engineer responsible for 180 wells across 3 fields: "Portfolio Summary: 165 producing, 8 shut-in, 4 workover, 3 regulatory hold. Total production: 4,250 BOPD vs. 4,600 target (-7.6%). Exception Wells (5): (1) Well A-47: Oil rate dropped 35% overnight (82→53 BOPD). Casing pressure increased 40 PSI. Probable cause: tubing leak above packer — 85% confidence. Recommend: Pull tubing for inspection. Est. cost: $45K. If confirmed and repaired, expect full rate recovery. Payout: 12 days at current oil price. (2) Well B-112: Gradual decline over 14 days, now 22% below target. Water cut increased from 45% to 62%. Probable cause: water channeling from nearby injection well. Recommend: Review injection pattern and consider diverter treatment. (3-5) [similar diagnostics]. Top Optimization Opportunity: Wells C-15, C-18, and C-22 are gas-lifting at suboptimal rates based on valve performance curves. Adjusting injection rates could recover estimated 45 BOPD aggregate. Zero cost intervention — field operator can adjust during normal rounds."

---

### Use Case 4: Pipeline Integrity & Compliance Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Pipeline operators manage thousands of miles of infrastructure under intense regulatory scrutiny from PHMSA (Pipeline and Hazardous Materials Safety Administration) in the US and equivalent agencies globally. Integrity management requires tracking inline inspections (ILI/"smart pig" runs), external corrosion surveys (ECDA), pressure tests, coating surveys, cathodic protection readings, anomaly assessments, repair scheduling, and regulatory reporting — across pipeline segments that may span multiple states and regulatory jurisdictions. The data volume is staggering: a single ILI run generates data on thousands of anomalies (metal loss, dents, cracks) that must be assessed, prioritized, and addressed within regulatory timeframes. Pipeline integrity engineers manage this through a combination of specialized integrity software (Pipesak, PODS, GeoFields), GIS systems, and inevitably — Excel spreadsheets for tracking repair schedules and compliance deadlines. Missed deadlines or inadequate documentation result in PHMSA enforcement actions, consent decrees, and fines that can reach millions of dollars. More critically, integrity failures cause pipeline ruptures with catastrophic environmental and safety consequences.

#### The Solution
Build a Pipeline Integrity Management system in monday.com to serve as the operational workflow layer above specialized integrity databases. Create boards for anomaly tracking (each anomaly is an item with location, severity, assessment method, repair deadline, assigned engineer), dig program management (planned excavations to inspect and repair anomalies), ILI run planning and execution, cathodic protection survey scheduling, and regulatory compliance tracking. Use Timeline views for multi-year integrity plans. Connect to location data for geographic visualization. Build Dashboards showing anomaly inventory by severity, repair completion rates, upcoming regulatory deadlines, and inspection schedule adherence.

#### The Outcome
Achieve 100% regulatory deadline compliance through automated tracking and escalation. Reduce integrity assessment turnaround time by 30% through structured workflows. Improve dig program efficiency by 20% through optimized scheduling and coordination. Maintain complete audit trail for all integrity decisions — critical for regulatory defense. Enable integrity managers to handle 40% more pipeline miles through exception-based management.

#### Discovery Questions
1. "How do you currently track the lifecycle of a pipeline anomaly — from ILI detection through assessment, repair scheduling, excavation, and close-out?"
2. "Have you received any PHMSA warning letters, notices of probable violation, or consent decrees related to integrity management documentation or timeline compliance?"
3. "How do you manage your dig program — scheduling excavations, coordinating land access, tracking completion, and documenting findings?"
4. "What happens when an integrity engineer leaves the company — how much institutional knowledge about specific pipeline segments walks out the door?"
5. "How many pipeline miles does each integrity engineer manage, and is their workload sustainable with current tools?"

#### Industry Context
PHMSA regulations (49 CFR 192 for gas, 49 CFR 195 for hazardous liquids) require operators to maintain Integrity Management Programs (IMPs) for pipelines in High Consequence Areas (HCAs). Inline inspection (ILI) tools ("smart pigs") detect metal loss, dents, cracks, and geometry anomalies. Anomalies are assessed using ASME B31G (for corrosion) or other engineering methods to determine if they require immediate repair, scheduled repair, or monitoring. "Dig programs" are organized excavation campaigns to expose and inspect/repair identified anomalies. Cathodic protection (CP) systems prevent external corrosion — readings must be taken at test points along the pipeline, typically annually. The "Maximum Allowable Operating Pressure" (MAOP) determines the safety margin for each pipeline segment.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Pipeline Integrity & Compliance Management system. Create a board called 'Anomaly Tracker' with columns: Anomaly ID (text), Pipeline Segment (dropdown), Mile Post / Station (text), ILI Run Date (date), Anomaly Type (dropdown: Metal Loss - External, Metal Loss - Internal, Dent, Crack, Lamination, Geometry, Weld Anomaly), Depth % Wall Thickness (numbers), Length (inches) (numbers), Width (inches) (numbers), Assessment Method (dropdown: ASME B31G, Modified B31G, RSTRENG, Level 2 FEA, Direct Assessment), Calculated Failure Pressure PSI (numbers), MAOP PSI (numbers), Safety Factor (formula: Failure Pressure / MAOP), Severity (status: Immediate - Repair Within 60 Days, 1-Year - Repair Within 365 Days, Monitored - Reassess Next ILI, Acceptable), Response Deadline (date), Repair Status (status: Assessment Pending, Repair Scheduled, Land Access Pending, Excavated, Repaired, Documented, Closed), Assigned Engineer (people), Notes (long text). Create a connected 'Dig Program' board: Dig ID (text), Anomaly (connect to Anomaly Tracker), Pipeline Segment (mirror), Location (text), Land Owner (text), Land Access Status (status: Not Contacted, In Negotiation, Approved, Denied - Reroute), Scheduled Date (date), Excavation Contractor (dropdown), Dig Status (status: Planned, Land Access Confirmed, Crew Mobilized, Excavated, Inspection Complete, Repair Complete, Backfilled, Restored, Documented), Field Findings (long text), Actual Wall Thickness (numbers), Repair Method (dropdown: Composite Sleeve, Steel Sleeve, Cut-Out & Replace, Grinding, Weld Repair, No Repair Required), Cost ($K) (numbers). Create a 'Compliance Calendar' board: Requirement (text), Regulation Reference (text), Pipeline Segment (dropdown), Frequency (dropdown: Annual, 3-Year, 5-Year, 7-Year, 10-Year, Event-Triggered), Last Completed (date), Next Due (date), Responsible Person (people), Status (status: Current, Due Within 90 Days, Due Within 30 Days, Overdue), Documentation Link (link). Dashboard with: Anomaly Inventory by Severity (pie chart), Repair Completion vs. Deadlines (bar chart), Dig Program Progress (Gantt/timeline), Overdue Items (filtered alert table), Compliance Calendar Next 90 Days (table), ILI Schedule (timeline), CP Survey Completion Rate (gauge). Automations: When Response Deadline is within 30 days and Repair Status is still 'Assessment Pending', escalate to Integrity Manager. When all digs in a segment are 'Documented', trigger segment integrity reassessment. When Compliance Next Due is within 90 days, change status to 'Due Within 90 Days' and notify Responsible Person. When Severity is 'Immediate', send urgent notification to Integrity Manager and Operations VP."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pipeline Integrity Watchdog Agent
**Agent Purpose:** Ensure zero missed regulatory deadlines and optimize dig program efficiency across the pipeline network.

**Triggers:**
- New ILI data uploaded (bulk anomaly import)
- Anomaly response deadline approaching (T-60, T-30, T-14, T-7 days)
- Dig program status changes
- Compliance calendar item due within 90 days
- Monthly integrity program review (scheduled)

**Actions:**
- When new ILI data is imported, auto-categorize anomalies by severity using ASME B31G calculations and set response deadlines per regulatory requirements
- Generate prioritized dig program schedule optimizing for: regulatory deadline compliance, geographic clustering (minimize mobilization costs), land access status, and seasonal constraints (ground conditions)
- Send tiered escalation alerts for approaching deadlines: 60 days → engineer notification, 30 days → manager alert, 14 days → VP notification with action plan required
- Compile monthly integrity program status report: anomaly inventory trends, repair completion rates, compliance calendar status, and budget tracking
- After dig completion, compare field findings to ILI predictions and track assessment accuracy for continuous improvement
- Generate regulatory submission packages compiling all required documentation for annual PHMSA reporting

**Data Required:**
- ILI anomaly data (vendor reports)
- Pipeline attribute data (diameter, wall thickness, MAOP, material grade)
- Land access records and owner contact information
- Contractor availability and mobilization costs
- Weather and ground condition data (seasonal planning)
- Regulatory requirement database by jurisdiction

**Autonomy Level:** Escalation-Based
Anomaly categorization and deadline calculation are automatic but require engineer verification for non-standard cases. Dig program schedule optimization is a recommendation requiring manager approval. Escalation alerts are fully automatic and cannot be suppressed. Regulatory submission packages are auto-compiled but require Integrity Manager sign-off before filing.

**Example Interaction:**
> A new ILI run on a 120-mile natural gas transmission line has been completed. The vendor delivers data containing 847 reported anomalies. The Pipeline Integrity Watchdog Agent processes the data overnight: it categorizes 3 anomalies as "Immediate" (repair within 60 days — metal loss exceeding 80% wall thickness), 18 as "1-Year" (significant but not imminent), 126 as "Monitored" (reassess at next ILI), and 700 as "Acceptable" (within safe operating limits). For the 3 immediate anomalies, it generates urgent notifications to the integrity engineer and VP of Operations with locations, assessment details, and recommended repair methods. It then optimizes a dig program for the 21 anomalies requiring near-term repair: "Recommended dig sequence groups repairs into 4 geographic clusters, reducing mobilization costs by estimated $180K. Cluster 1 (MP 23-28): 2 immediate + 3 one-year anomalies — recommend prioritizing, land access confirmed for all 5 locations. Estimated schedule: 12 field days. Cluster 2 (MP 55-62): 1 immediate + 4 one-year — land access pending for 2 locations, agent has initiated contact workflow."

---

### Use Case 5: Environmental Compliance & Emissions Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy operations face an unprecedented convergence of environmental regulatory pressure. EPA's Subpart W (greenhouse gas reporting), Subpart OOOOa/b/c (methane emissions from oil and gas), state-level emissions regulations, Clean Water Act permits, air quality permits, spill reporting requirements, and emerging ESG disclosure mandates (SEC climate rules, EU CSRD) create a compliance web that's nearly impossible to manage manually. A mid-size E&P company might have 500+ individual environmental permits across its operations, each with unique monitoring, reporting, and renewal requirements. Emissions events (flaring, venting, equipment leaks detected through LDAR programs) require documentation within hours. Environmental fines in the energy sector exceeded $1 billion in 2024. Beyond fines, environmental non-compliance increasingly triggers investor concern, insurance premium increases, and social license challenges. The workforce managing this compliance is small relative to the scope — environmental teams of 5-15 people managing compliance for hundreds of facilities.

#### The Solution
Build an Environmental Compliance & Emissions Management system in monday.com. Create boards for permit tracking (every active permit with conditions, monitoring requirements, reporting deadlines, and renewal dates), emissions event logging (flaring, venting, releases with volume calculations and regulatory notification requirements), LDAR (Leak Detection and Repair) program management (component inventory, inspection schedules, leak findings, repair tracking), spill and release reporting (immediate notification workflows, investigation, remediation tracking), and ESG data aggregation (Scope 1/2/3 emissions roll-up for disclosure). Automate deadline tracking, regulatory notification workflows, and reporting package compilation.

#### The Outcome
Achieve 100% permit compliance through automated deadline tracking. Reduce environmental reporting preparation time by 50% through structured data collection. Decrease time from emissions event to regulatory notification from hours to minutes. Maintain audit-ready documentation at all times. Enable environmental teams to manage 50% more permits per person through workflow automation.

#### Discovery Questions
1. "How many active environmental permits does your organization maintain, and how do you currently track compliance conditions, monitoring requirements, and renewal deadlines across all of them?"
2. "When an unplanned emissions event occurs — say, an equipment malfunction causing a flaring event — what's your current process from detection to regulatory notification, and how long does it typically take?"
3. "How are you preparing for the SEC climate disclosure rules and EPA's enhanced methane regulations — do you have the data infrastructure to report Scope 1 and 2 emissions accurately?"
4. "How does your LDAR program currently work — how do you schedule inspections, track identified leaks, manage repair deadlines, and compile reports?"
5. "How much time does your environmental team spend each month on routine compliance reporting versus proactive environmental improvement?"

#### Industry Context
Key regulations: EPA Subpart W (GHG reporting for petroleum and natural gas systems), OOOOa/b/c (New Source Performance Standards for methane), LDAR (Leak Detection and Repair under Method 21 or OGI camera surveys), Title V air permits (major source operating permits), NPDES permits (water discharge), SPCC plans (Spill Prevention, Control, and Countermeasure). Methane emissions reduction is the industry's top environmental priority — the Inflation Reduction Act introduced a methane fee starting at $900/ton in 2024, rising to $1,500/ton by 2026. LDAR programs require regular surveys of equipment components (valves, flanges, connectors, pump seals) using Method 21 organic vapor analyzers or optical gas imaging (OGI) cameras. Detected leaks must be repaired within regulatory timeframes (typically 15-30 days). ESG reporting frameworks (GRI, SASB, TCFD) are becoming mandatory rather than voluntary.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Environmental Compliance & Emissions Management system. Create a board called 'Permit Registry' with columns: Permit Number (text), Permit Type (dropdown: Title V Air, Minor Source Air, NPDES Water, Stormwater, UIC Injection, Waste Generator, Spill Prevention, State-Specific), Facility (dropdown), Issuing Agency (dropdown: EPA, State DEQ, Army Corps, Railroad Commission), Issue Date (date), Expiration Date (date), Renewal Application Deadline (date), Status (status: Active, Renewal Pending, Expired, Revoked, Under Modification), Key Conditions Summary (long text), Monitoring Requirements (long text), Reporting Frequency (dropdown: Monthly, Quarterly, Semi-Annual, Annual, Event-Based), Next Report Due (date), Responsible Person (people), Compliance Status (status: In Compliance, Minor Finding, Major Finding, Under Investigation). Create a connected 'Emissions Events' board: Event ID (auto-number), Facility (dropdown), Event Type (dropdown: Planned Flaring, Unplanned Flaring, Venting, Equipment Leak, Process Upset, Emergency Release), Start DateTime (date), End DateTime (date), Duration Hours (numbers), Volume Released (numbers), Units (dropdown: MCF, BBL, Tons, Lbs), Compound (dropdown: Methane, VOCs, H2S, CO2, SO2, Particulate), Cause (dropdown: Equipment Failure, Process Upset, Maintenance Activity, Emergency, Startup/Shutdown), Regulatory Notification Required (checkbox), Notification Deadline (date), Notification Sent (checkbox), Notification Agency (dropdown), Report Filed (checkbox), Corrective Action (long text). Create an 'LDAR Program' board: Component ID (text), Facility (dropdown), Equipment Type (dropdown: Valve, Flange, Connector, Pump Seal, Compressor Seal, PRV, Open-Ended Line), Service (dropdown: Gas, Light Liquid, Heavy Liquid), Last Inspection Date (date), Next Inspection Due (date), Inspection Method (dropdown: Method 21 OVA, OGI Camera), Inspector (people), Reading PPM (numbers), Leak Detected (checkbox), Leak Status (status: No Leak, Leak Found - Repair Scheduled, First Attempt Repair, Delay of Repair Approved, Repaired - Resurvey Pending, Repaired - Confirmed, Replacement Scheduled), Repair Deadline (date), Repair Date (date). Dashboard with: Permit Compliance Overview (gauge), Upcoming Permit Deadlines (table next 90 days), Emissions Events by Type and Facility (chart), Monthly Emissions Trend (line chart), LDAR Leak Rate by Facility (bar chart), Open Leaks Requiring Repair (filtered table), Regulatory Notifications Pending (alert table). Automations: When Renewal Application Deadline is 120 days away, create renewal task and notify Responsible Person. When Emissions Event has Regulatory Notification Required checked, immediately notify Environmental Manager and set Notification Deadline. When LDAR Leak Detected is checked, calculate Repair Deadline (30 days) and notify maintenance. When any Compliance Status changes to 'Major Finding', alert Environmental Director and Legal."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Environmental Compliance Guardian Agent
**Agent Purpose:** Ensure zero missed environmental deadlines, automate emissions event response, and compile regulatory reports.

**Triggers:**
- New emissions event logged
- Permit deadline approaching (T-120, T-90, T-30 days)
- LDAR leak detected
- Regulatory reporting period ending
- Monthly ESG data compilation (scheduled)

**Actions:**
- When emissions event is logged, determine all applicable reporting requirements (federal, state, local), set notification deadlines, and generate pre-populated notification forms for environmental staff to review and submit
- Track LDAR repair compliance: alert when repair deadline approaching, escalate overdue repairs, compile leak rate statistics by component type and facility for regulatory reporting
- Generate automated regulatory reports by compiling data from emissions events, LDAR findings, and monitoring records into required formats
- Compile monthly Scope 1 emissions roll-up across all facilities using emissions event data, continuous monitoring data, and engineering calculations
- Send tiered permit deadline escalations: 120 days → initiate renewal, 90 days → manager check, 30 days → VP alert
- Analyze emissions trends and identify facilities with increasing leak rates or frequent unplanned events for targeted improvement programs

**Data Required:**
- Permit database with conditions and deadlines
- Emissions event records with volume and compound data
- LDAR component inventory and inspection history
- Continuous emissions monitoring data (CEMS where applicable)
- Regulatory reporting templates and requirements by jurisdiction
- Weather data (for emissions dispersion context)

**Autonomy Level:** Escalation-Based
Deadline alerts and regulatory notification preparation are fully automatic. Report compilation is automatic but requires environmental manager review before submission. LDAR repair escalations are automatic. Emissions calculations use approved engineering methods but require engineer verification for non-standard events. No regulatory filings are submitted without human approval.

**Example Interaction:**
> At 3:42 AM, a compressor station experiences an unplanned shutdown, resulting in a venting event. The field operator logs the event in the Emissions Events board: methane release, estimated 15 MCF over 45 minutes. The Environmental Compliance Guardian Agent immediately activates: "EMISSIONS EVENT ALERT — Compressor Station #7. Unplanned methane vent: 15 MCF / 45 min. Regulatory analysis: (1) EPA Subpart W — must be included in annual GHG report, no immediate notification required. (2) State DEQ — event exceeds 10 MCF threshold, notification required within 24 hours. Pre-populated notification form attached — Environmental Manager review required before 3:42 AM tomorrow. (3) IRA Methane Fee calculation: estimated fee exposure $12,750 at current $1,500/ton rate. (4) Corrective action needed: compressor failure root cause investigation required per Subpart OOOOb. Investigation task created and assigned to Maintenance Engineer, due within 30 days." By 7 AM when the Environmental Manager checks their dashboard, all notification requirements are identified, forms are drafted, and the compliance clock is clearly visible.

---

### Use Case 6: Contractor & Vendor Management for Field Operations

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy operations rely heavily on contractors — from well servicing crews and pipeline construction teams to specialized inspection companies and environmental consultants. A mid-size operator may manage 200+ active contractor relationships with thousands of individual workers on site at any given time. Contractor management encompasses pre-qualification (safety records, insurance, certifications), work scope coordination, safety orientation tracking, daily check-in/out, performance monitoring, invoice verification, and compliance documentation. The ISNetworld and Veriforce platforms handle pre-qualification but don't manage day-to-day field operations. Work scopes are often loosely defined, leading to scope disputes and cost overruns. Contractor safety performance directly impacts the operator's TRIR (Total Recordable Incident Rate), but tracking contractor safety metrics across dozens of companies and hundreds of work sites is manual and lag-indicator-driven. When a contractor's insurance expires or a safety certification lapses, the operator may not know until an incident or audit reveals it.

#### The Solution
Build a Contractor & Vendor Management system in monday.com. Create boards for contractor registry (pre-qualification status, insurance tracking, safety metrics), active work order management (scope, schedule, budget, progress), field personnel tracking (orientation status, certifications, site access), performance scoring (safety, quality, timeliness, cost), and invoice management (work verification, approval workflow). Automate insurance expiry alerts, certification renewal tracking, and performance-based requalification triggers. Build Dashboards showing contractor performance rankings, active work orders by contractor, spend tracking, and compliance status.

#### The Outcome
Reduce contractor compliance gaps by 90% through automated insurance and certification tracking. Decrease work order scope disputes by 50% through structured scope documentation. Improve contractor safety performance by 20% through visible performance scoring and accountability. Reduce invoice processing time by 40% through automated verification workflows. Enable operations teams to manage 30% more concurrent contractor activities.

#### Discovery Questions
1. "How many active contractors do you currently manage across your operations, and what does your pre-qualification and ongoing compliance verification process look like?"
2. "When was the last time you discovered a contractor's insurance or safety certification had lapsed while they had active personnel on your sites?"
3. "How do you currently track contractor safety performance — and does that data influence future contract awards?"
4. "What's your process for verifying contractor invoices against actual work completed — and how often do you encounter discrepancies?"
5. "How do you ensure that every contractor worker on your sites has completed required safety orientation and possesses current certifications?"

#### Industry Context
ISNetworld, Veriforce, and Avetta are the dominant contractor pre-qualification platforms in energy — they verify insurance, safety statistics (EMR, TRIR, DART), training programs, and compliance. However, they don't manage operational workflows. EMR (Experience Modification Rate) is an insurance metric reflecting a company's claims history (1.0 = average; lower = better). TRIR (Total Recordable Incident Rate) measures injuries per 200,000 work hours. Operators typically require contractors to meet minimum thresholds (e.g., EMR < 1.0, TRIR < 2.0). "Man-camp" facilities house contract workers at remote field locations. "Day rate" vs. "turnkey" contracting models create different cost management challenges. Hot-tapping, hydrostatic testing, pigging, and other specialized services require contractors with specific certifications and equipment.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Contractor & Vendor Management system. Create a board called 'Contractor Registry' with columns: Company Name (text), ISNetworld ID (text), Service Category (dropdown: Well Servicing, Pipeline Construction, Inspection Services, Environmental Services, Electrical, Instrumentation, Civil/Earthwork, Transportation, Crane/Heavy Lift, Scaffolding, Insulation, Painting/Coating), Pre-Qualification Status (status: Approved, Conditional, Pending Review, Suspended, Disqualified), Insurance Expiry Date (date), Insurance Status (status: Current, Expiring <60 Days, Expired), General Liability Limit ($M) (numbers), Workers Comp EMR (numbers), Company TRIR (numbers), Last Safety Audit Date (date), Performance Score (numbers: 0-100), Contract Status (status: Active MSA, Expired, Negotiating, No Contract), Primary Contact (text), Phone (text), Notes (long text). Create a connected 'Active Work Orders' board: WO Number (text), Contractor (connect to Registry), Scope Description (long text), Facility/Location (dropdown), Work Type (dropdown: Maintenance, Construction, Inspection, Environmental, Emergency, Turnaround), Start Date (date), End Date (date), Estimated Cost ($K) (numbers), Actual Cost ($K) (numbers), Cost Variance % (formula), Status (status: Drafted, Approved, In Progress, Complete - Pending Verification, Invoiced, Closed, Disputed), Field Supervisor (people), Quality Rating (status: Exceeds, Meets, Below, Unacceptable), Safety Incidents on WO (numbers), Completion % (numbers). Create a 'Contractor Personnel' board: Worker Name (text), Contractor (connect to Registry), Role (dropdown: Supervisor, Foreman, Operator, Technician, Laborer, Inspector, Engineer), Safety Orientation Status (status: Not Started, Scheduled, Complete, Expired), Orientation Expiry Date (date), Certifications (text: list of active certs), Site Access (status: Approved, Pending Orientation, Suspended, Revoked), Current Work Order (connect to Active WOs). Dashboard with: Contractor Performance Rankings (table sorted by score), Insurance Compliance Status (pie chart), Active Work Orders by Contractor (bar chart), Spend vs Budget (chart), Safety Incidents by Contractor (bar chart), Personnel on Site Today (number), Expiring Certifications (alert table next 30 days). Automations: When Insurance Expiry Date is within 60 days, change Insurance Status to 'Expiring' and notify contractor and Procurement. When Insurance is 'Expired', change Pre-Qualification Status to 'Suspended' and notify all active WO supervisors. When Orientation Expiry Date passes, change Site Access to 'Suspended'. When Work Order status changes to 'Complete', trigger verification checklist and invoice approval workflow. When Safety Incidents > 0 on any WO, notify HSE Manager and flag for Performance Score review."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Contractor Oversight Agent
**Agent Purpose:** Ensure contractor compliance, track performance, and prevent unqualified personnel from accessing operational sites.

**Triggers:**
- Insurance or certification expiry date approaching (T-60, T-30, T-7 days)
- New contractor personnel added to a work order
- Work order completed (triggers performance evaluation)
- Safety incident reported involving contractor
- Monthly contractor performance review (scheduled)

**Actions:**
- Monitor all contractor insurance and certification dates — send renewal reminders at 60 days, warnings at 30 days, and auto-suspend pre-qualification at expiry
- When new personnel are assigned to a work order, verify orientation status and certifications against work type requirements — block site access assignment if requirements not met
- After work order completion, generate performance evaluation request to field supervisor with structured scoring criteria (safety, quality, timeliness, cost management)
- Calculate rolling contractor performance scores based on recent work order evaluations, safety metrics, and compliance history
- Generate monthly contractor performance report ranking all active contractors and flagging underperformers for contract review
- When safety incident involves a contractor, immediately compile contractor's performance history, active personnel count, and insurance status for incident review team

**Data Required:**
- Contractor insurance and certification data
- Work order history and evaluations
- Safety incident records
- Personnel orientation and certification records
- ISNetworld/Veriforce data (integration)
- Invoice and payment history

**Autonomy Level:** Escalation-Based
Insurance/certification monitoring and alerts are fully automatic. Pre-qualification suspension on expiry is automatic (safety requirement). Personnel access blocking for unqualified workers is automatic. Performance score calculation is automatic. Contract renewal/termination decisions require Procurement and Operations Management approval.

**Example Interaction:**
> The Contractor Oversight Agent detects that Precision Pipeline Services' general liability insurance expires in 14 days. They currently have 3 active work orders across 2 facilities with 28 personnel on site. The agent has already sent reminders at 60 and 30 days with no updated certificate received. It now sends an urgent escalation: "CRITICAL — Precision Pipeline Services insurance expires Feb 28. 3 active WOs, 28 personnel on-site. No renewal certificate received despite 2 prior reminders. Action required: (1) Contact Precision's insurance contact (Sarah Miller, 555-0142) for immediate proof of renewal. (2) If not received by Feb 26, all work orders will be suspended and personnel site access revoked per company policy. (3) Contingency: backup contractors identified for each active WO — recommend initiating standby notification to Atlas Construction (Performance Score: 92, available capacity confirmed)." The operations manager can see the full picture and make an informed decision about whether to grant a brief extension or initiate the transition to backup contractors.

---

### Use Case 7: Emergency Response & Incident Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy operations face emergency scenarios ranging from well control events and pipeline ruptures to refinery fires, chemical releases, and natural disasters affecting facilities. Emergency response requires immediate coordination across operations, HSE, management, regulators, contractors, and potentially emergency services. Most operators maintain Emergency Response Plans (ERPs) as static documents that are exercised annually in tabletop drills but are difficult to execute under real-time pressure. When an actual emergency occurs, the response often relies on phone trees, radio communications, and ad hoc coordination. Critical information — who's on site, what hazardous materials are involved, which regulatory agencies need notification, what mutual aid agreements are in place — must be assembled quickly under extreme stress. Post-incident investigation (using methods like TapRooT, SCAT, or the "5 Whys") generates findings and corrective actions that too often sit in binders rather than driving systemic improvements.

#### The Solution
Build an Emergency Response & Incident Management system in monday.com. Create an Emergency Response activation board with pre-configured incident types (well control, pipeline release, fire/explosion, chemical release, severe weather, security threat), automatic notification cascades based on incident severity and type, real-time status tracking during response, resource deployment tracking, and regulatory notification checklists. Build connected boards for incident investigation (root cause analysis, evidence collection, witness statements), corrective action tracking (assigned actions with deadlines and verification), and drill/exercise management (scheduling, evaluation, improvement tracking). Create Dashboards for incident trends, corrective action completion rates, and drill compliance.

#### The Outcome
Reduce emergency notification time from 30+ minutes to under 5 minutes through automated cascade notifications. Ensure 100% of required regulatory notifications are made within mandated timeframes. Improve incident investigation completion from 60% to 95% through structured workflows. Increase corrective action close-out rate from 70% to 95% through automated tracking and escalation. Build institutional emergency response capability through drill documentation and lessons learned.

#### Discovery Questions
1. "When was the last time you activated your emergency response plan for a real incident — and what worked well versus what could have been better about the coordination?"
2. "How quickly can you assemble your incident command team and establish communication when an emergency occurs at 2 AM at a remote location?"
3. "After an incident investigation is completed and corrective actions are identified, what's your close-out rate — and how do you ensure the same type of incident doesn't recur?"
4. "How do you currently manage your emergency drill program — frequency, realism, evaluation, and improvement tracking?"
5. "Do you have a systematic way to analyze incident trends across your operations to identify systemic issues versus one-off events?"

#### Industry Context
Emergency response in energy follows Incident Command System (ICS) principles with defined roles: Incident Commander, Operations Section Chief, Planning Section Chief, Logistics Section Chief, Finance/Admin Section Chief. Well control incidents are classified by severity (kick → underground blowout → surface blowout). Pipeline releases trigger National Response Center (NRC) notification requirements. OSHA's Process Safety Management (PSM) standard requires incident investigation within 48 hours of certain events. The "Swiss Cheese Model" (James Reason) is widely used to understand how multiple barrier failures align to cause incidents. Leading indicators (near-miss reporting, safety observations, audit findings) are considered more valuable than lagging indicators (TRIR, severity rates) for predicting and preventing incidents.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Emergency Response & Incident Management system. Create a board called 'Incident Log' with columns: Incident ID (auto-number), Date/Time (date), Facility/Location (dropdown), Incident Type (dropdown: Well Control Event, Pipeline Release, Fire/Explosion, Chemical/Gas Release, Vehicle Accident, Fall/Struck-By, Equipment Failure, Environmental Spill, Severe Weather, Security Incident), Severity (status: Level 1 - Minor/Near-Miss, Level 2 - Moderate, Level 3 - Serious, Level 4 - Major/Catastrophic), Description (long text), Immediate Actions Taken (long text), Injuries (numbers), Fatalities (numbers), Environmental Impact (status: None, Minor, Moderate, Significant), Estimated Damage ($K) (numbers), Incident Commander (people), Investigation Status (status: Pending, Investigation Team Assigned, Investigation In Progress, Draft Report, Final Report, Closed), Investigation Lead (people), Root Cause Category (dropdown: Human Error, Equipment Failure, Procedural Gap, Design Deficiency, External Factor, Management System Failure), Regulatory Notifications Required (text), Notifications Complete (checkbox). Add subitems for corrective actions: Action Description (text), Action Type (dropdown: Immediate, Short-Term, Long-Term, Systemic), Assigned To (people), Due Date (date), Status (status: Open, In Progress, Complete, Verified, Overdue), Verification Method (text), Verified By (people). Create a connected 'Emergency Response Activation' board: Incident (connect to Log), ICS Role (dropdown: Incident Commander, Operations Chief, Planning Chief, Logistics Chief, Safety Officer, Public Information Officer, Liaison), Assigned Person (people), Activated Time (date), Status (status: Activated, On Scene, Released), Communication Log (long text). Create a 'Drills & Exercises' board: Exercise Name (text), Type (dropdown: Tabletop, Functional, Full-Scale), Scenario (long text), Facility (dropdown), Scheduled Date (date), Status (status: Planning, Scheduled, Completed, Report Issued), Participants (people), Evaluator (people), Findings (long text), Improvement Actions (text). Dashboard with: Incident Trends by Type (line chart over time), Severity Distribution (pie chart), Corrective Action Completion Rate (gauge), Open Corrective Actions by Age (bar chart), Investigation Timeline Compliance (percentage within 48h), Drill Schedule Compliance (chart), Near-Miss Reporting Rate Trend (line chart). Automations: When Severity is Level 3 or 4, immediately notify Operations VP, HSE Director, and Legal. When new incident is created, auto-populate regulatory notification checklist based on Incident Type. When Corrective Action Due Date passes and Status is not Complete, change to 'Overdue' and escalate to Investigation Lead and HSE Manager. When Investigation Status is 'Pending' for more than 48 hours, alert HSE Director."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Emergency Response Coordinator Agent
**Agent Purpose:** Automate emergency notification cascades, track response activities in real-time, and ensure post-incident follow-through.

**Triggers:**
- New incident logged with severity Level 2+
- Emergency Response Activation board updated
- Investigation deadline approaching (48-hour OSHA requirement)
- Corrective action due date approaching
- Quarterly incident trend analysis (scheduled)

**Actions:**
- When incident is logged, immediately determine notification requirements based on type and severity — activate pre-defined notification cascade (phone, text, email to ICS team members and regulatory contacts)
- During active emergency, maintain real-time status dashboard and communication log — prompt ICS roles for status updates every 30 minutes
- After incident stabilization, auto-create investigation template with required elements (evidence checklist, witness statement forms, timeline template) and assign investigation team with 48-hour deadline
- Track all corrective actions across all incidents — send weekly summary to HSE leadership showing open items, overdue items, and completion trends
- Generate quarterly incident trend analysis: patterns by type, location, time of day, root cause category — identify systemic issues requiring management attention
- Compile annual regulatory incident reports by aggregating data across all facilities

**Data Required:**
- Emergency contact lists and notification cascades by facility and incident type
- ICS team rosters and alternates
- Regulatory notification requirements by incident type and jurisdiction
- Historical incident data for trend analysis
- Corrective action database
- Drill schedule and evaluation records

**Autonomy Level:** Escalation-Based
Notification cascades for Level 3-4 incidents are immediate and automatic — no human gate (speed is critical in emergencies). Communication log prompts during active response are automatic. Investigation task creation is automatic. Corrective action tracking and escalation are automatic. Trend analysis is auto-generated but requires HSE leadership review and action planning.

**Example Interaction:**
> A field operator reports a pipeline pressure drop and suspected release at a remote pipeline station at 10:47 PM. They log the incident as "Pipeline Release, Level 3 - Serious." The Emergency Response Coordinator Agent activates within seconds: it sends simultaneous notifications to the on-call Incident Commander, Operations Manager, Pipeline Integrity Engineer, Environmental Manager, and HSE Director via phone call, text, and email. It populates the Emergency Response Activation board with the ICS structure, pre-identifies regulatory notification requirements (NRC notification within 1 hour if volume exceeds reportable quantity, state agency notification within 2 hours, PHMSA telephonic report within 2 hours), and starts a response timeline. As the IC arrives on scene and confirms a release, the agent updates the dashboard: "IC confirms release from 12-inch gas line. Estimated volume: 5 MMCF. Area secured, isolation in progress. NRC notification REQUIRED — deadline: 11:47 PM tonight. Pre-populated NRC report form attached — Environmental Manager review and submit." The agent tracks every action on a real-time timeline that becomes the official incident chronology for the investigation and regulatory reporting.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| BOPD | Barrels of Oil Per Day — standard production measurement |
| MCFD | Thousand Cubic Feet per Day — standard gas production measurement |
| TRIR | Total Recordable Incident Rate — injuries per 200,000 work hours |
| EMR | Experience Modification Rate — insurance safety metric (1.0 = average) |
| LDAR | Leak Detection and Repair — regulatory program for fugitive emissions |
| ILI / Smart Pig | Inline Inspection tool that travels through pipelines detecting anomalies |
| MAOP | Maximum Allowable Operating Pressure — regulatory pressure limit for pipelines |
| Turnaround | Planned shutdown of a facility for maintenance and inspection |
| SCADA | Supervisory Control and Data Acquisition — real-time monitoring system |
| PTW | Permit to Work — formal safety authorization for hazardous activities |
| LOTO | Lockout/Tagout — energy isolation safety procedure |
| SIMOPS | Simultaneous Operations — managing concurrent activities safely |
| ESP | Electric Submersible Pump — artificial lift method for wells |
| HCA | High Consequence Area — populated or environmentally sensitive area near pipelines |
| NRC | National Response Center — federal notification point for hazardous releases |
| PSM | Process Safety Management — OSHA standard for high-hazard facilities |
| LEL | Lower Explosive Limit — minimum concentration for ignition |
| OGI | Optical Gas Imaging — infrared camera technology for methane detection |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP of Operations | Overall operational performance, safety, production targets | Decision-maker |
| Operations Manager (Field/Plant) | Day-to-day facility management, production optimization | Decision-maker / Champion |
| Maintenance Manager | Maintenance strategy, turnaround planning, reliability | Decision-maker for maintenance tech |
| HSE Director | Safety programs, regulatory compliance, incident investigation | Decision-maker (veto on safety) |
| Pipeline Integrity Manager | Pipeline inspection, anomaly assessment, compliance | Influencer / Budget holder |
| Environmental Manager | Permits, emissions, spill response, ESG reporting | Influencer |
| Production Engineer | Well optimization, artificial lift, intervention planning | End user / Champion |
| Field Supervisor/Foreman | Daily crew management, permit issuance, contractor oversight | End user |
| Reliability Engineer | Equipment failure analysis, predictive maintenance | Influencer |
| VP of IT / Digital | Technology strategy, OT/IT convergence, digital transformation | Budget holder |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | OT/IT convergence, SCADA integration, digital transformation | monday.com as the work management layer connecting OT data to human workflows |
| Finance | CAPEX/OPEX budgeting, AFE approvals, contractor invoice processing | Connected financial approval workflows from field to finance |
| Procurement | Vendor management, material purchasing, contract negotiation | Integrated procurement workflows from maintenance planning through PO issuance |
| HR | Safety training compliance, workforce planning, contractor orientation | Training management and compliance tracking |
| Legal | Regulatory compliance, incident litigation, environmental liability | Incident documentation and corrective action tracking for legal defense |
| Product & R&D (Engineering) | Facility design, modification projects, technology evaluation | Project management for engineering modifications and capital projects |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SAP PM / S4HANA | Enterprise CMMS — the "system of record" for maintenance | Universally despised UX. monday.com as the planning and coordination layer while SAP handles transactions. Don't try to replace SAP — complement it. |
| Maximo (IBM) | Asset management for large-scale operations | Similar to SAP — powerful but rigid and user-hostile. monday.com handles the collaborative workflow that Maximo can't. |
| Primavera P6 (Oracle) | Project scheduling for turnarounds and capital projects | Scheduling engine stays; monday.com replaces the Excel layer around P6 for daily execution tracking and communication. |
| Intelex / Enablon / Cority | EHS management (safety, environmental, compliance) | Specialized but siloed. monday.com can serve as the workflow engine while connecting to EHS data, or replace for smaller operators. |
| Excel / SharePoint | The actual dominant "tool" for most operational workflows | Universal pain — everyone knows Excel doesn't scale for multi-user field operations. monday.com is the natural evolution. |
| ServiceNow | IT-focused workflow, expanding to operational technology | IT-centric DNA doesn't resonate with field operations teams. monday.com's visual, flexible interface is more adopted by non-IT users. |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We can't put operational data in the cloud — SCADA/OT security concerns" | monday.com manages the *work management* layer — human workflows, scheduling, compliance tracking — not OT control systems. It complements your SCADA environment by organizing the human response to OT data. Enterprise security (SOC 2 Type II, ISO 27001) meets energy industry standards. |
| "We already have SAP/Maximo for maintenance" | Exactly — and your teams still use Excel because SAP/Maximo is too rigid for collaborative planning. monday.com is the missing layer between your CMMS transactions and how people actually coordinate work. We integrate with SAP, not replace it. |
| "Our field crews don't use computers" | monday.com's mobile app works offline in remote locations and syncs when connectivity returns. Field supervisors update work orders from tablets on the wellpad. The interface is visual and intuitive — no SAP training required. |
| "Energy companies have different compliance requirements" | We work with regulated industries across sectors and understand the need for audit trails, access controls, and data retention. Our platform supports the governance requirements of energy operations while being dramatically easier to configure than specialized compliance tools. |
| "We tried [tool] before and adoption failed" | Adoption fails when tools are imposed top-down without matching how people actually work. monday.com succeeds because it adapts to your existing workflows rather than forcing you into a vendor's process model. Start with one painful workflow (e.g., permit tracking), prove value, then expand. |
| "Our turnaround planning is too complex for a work management tool" | We're not replacing Primavera for CPM scheduling. We're replacing the 47 Excel spreadsheets, 200 emails per day, and 3 SharePoint sites that surround your P6 schedule. The daily execution, progress tracking, issue management, and resource coordination layer is where monday.com transforms turnaround management. |

## Proof Points
*(To be populated with customer references)*
- [Energy companies using monday.com for operations management]
- [Oil & gas operators that improved turnaround execution with workflow tools]
- [Pipeline operators that achieved regulatory compliance through digital management]
- [Energy companies that reduced contractor management overhead]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
