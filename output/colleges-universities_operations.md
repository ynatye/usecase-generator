# Colleges & Universities × Operations Playbook

## Overview

Operations in higher education institutions encompasses the sprawling physical, logistical, and administrative infrastructure that keeps a college or university functioning — from facilities management and campus safety to dining services, transportation, space allocation, and environmental compliance. Unlike corporate operations, university operations must serve a uniquely diverse set of stakeholders: students, faculty, staff, administrators, visitors, alumni, and surrounding communities. The operational complexity rivals that of a small city, with a typical mid-size university managing 50-200+ buildings, 5,000-30,000+ daily occupants, $50-500M+ in annual operating budgets, and regulatory obligations spanning ADA accessibility, fire safety, environmental compliance, Title IX, and Clery Act reporting.

Operations departments in higher education are typically led by a Vice President for Administration, a Chief Operating Officer, or an Associate VP of Facilities & Operations. The org structure usually includes Facilities Management (building maintenance, grounds, custodial), Space Planning & Utilization, Campus Safety & Emergency Management, Dining & Auxiliary Services, Transportation & Parking, Environmental Health & Safety, and increasingly, Sustainability Operations. These teams are chronically under-resourced — deferred maintenance backlogs at U.S. colleges and universities exceed $112 billion nationally, and operations staff-to-building ratios have deteriorated as institutions face enrollment declines and budget pressures.

The regulatory and compliance context is intense. Universities must comply with OSHA, EPA, ADA, local fire codes, state building codes, Clery Act (campus safety reporting), Title IX (facilities related to gender equity), and increasingly, state-level sustainability mandates. Many are also subject to accreditation reviews that scrutinize operational infrastructure. Public universities face additional transparency requirements around procurement, budgeting, and capital project management. The operational challenge is compounded by the academic calendar — buildings go from 80% occupancy to 10% between semesters, creating unique demand patterns unlike any commercial real estate operation.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Operations teams are managing growing campus complexity with flat or shrinking budgets — AI can help 50 staff members operate like 150 |
| 2 | Consolidate Tech Stack with AI | High | Universities run a patchwork of legacy systems (CMMS, space management, EH&S, parking, dining) — consolidation onto a modern platform eliminates data silos and license costs |
| 3 | Replace or Radically Augment Headcount | Medium-High | Routine work order triage, space scheduling, compliance tracking, and report generation consume thousands of staff hours annually that AI can reclaim |

## Prioritized Use Cases

---

### Use Case 1: Facilities Work Order Management & Predictive Maintenance

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The average university receives 10,000-50,000+ maintenance work orders per year — everything from "the toilet in Jameson Hall is leaking" to "the HVAC system in the science building is failing." Most institutions manage these through outdated CMMS (Computerized Maintenance Management Systems) like TMA Systems, SchoolDude (now Brightly), or even paper-based systems. Work orders get lost in email queues, priority triage is inconsistent, skilled trades staff spend 30-40% of their day on paperwork and scheduling rather than actual repairs, and deferred maintenance compounds because there's no data-driven approach to prioritization. A single HVAC failure in a research building can destroy $500K+ in experimental samples. A burst pipe during winter break — when buildings are minimally monitored — can cause $2M+ in damage.

#### The Solution
monday.com Work Management as a modern work order platform. Incoming requests (from students, faculty, staff via monday Forms, email integration, or QR codes on buildings) are automatically categorized, prioritized, and routed to the appropriate trade team. Boards track every work order through its lifecycle: Submitted → Triaged → Assigned → In Progress → Completed → Verified. Dashboard views give operations leadership real-time visibility into work order volume by building, trade type, priority, and age. Connected boards track asset histories so that repeat issues trigger preventive maintenance reviews. AI Sidekick identifies patterns — "Building X has had 14 HVAC calls in 6 months, suggesting a systemic issue rather than spot repairs."

#### The Outcome
- 50% reduction in average work order completion time through intelligent routing and prioritization
- 35% decrease in emergency maintenance incidents through pattern detection and preventive intervention
- Elimination of "lost" work orders — 100% tracking from submission to completion
- $500K-2M annual savings from preventing catastrophic failures through early detection
- Improved campus satisfaction scores — facilities responsiveness is typically the #1 operational complaint on student surveys

#### Discovery Questions
1. "How many work orders does your facilities team process per month, and what percentage are resolved within your target SLA?"
2. "What system do you currently use for work order management — and what's the biggest frustration your team has with it?"
3. "When a building system fails overnight or over break, how quickly does your team find out? Have you experienced costly failures due to delayed detection?"
4. "How do you currently prioritize between a broken elevator in the student center and a flickering light in an office — is there a consistent framework?"
5. "What's your estimated deferred maintenance backlog, and how do you decide what to address each budget cycle?"

#### Industry Context
The concept of "deferred maintenance" is the silent crisis of higher education operations. APPA (the Association of Physical Plant Administrators) estimates that the average institution has a deferred maintenance backlog equal to 5-10% of its total plant replacement value. Every dollar of deferred maintenance today becomes $4 of repair cost in five years. The Facilities Condition Index (FCI) — the ratio of deferred maintenance to current replacement value — is the standard metric. An FCI above 0.10 is considered "poor." Many public universities are above 0.15. Operations leaders need data to make the case to trustees and state legislatures for capital investment.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Facilities Work Order Management system for a university. Create a board called 'Facilities Work Orders' with columns: Work Order ID (auto-number), Submitted By (text), Contact Email (email), Building (dropdown: Science Hall, Student Center, Library, Admin Building, Residence Hall A, Residence Hall B, Athletics Complex, Arts Center, Engineering Building, Dining Hall, Parking Garage), Floor/Room (text), Category (dropdown: HVAC, Plumbing, Electrical, Structural, Custodial, Grounds, Elevator, Fire Safety, ADA Compliance, IT Infrastructure, Other), Priority (status: Emergency, Urgent, Standard, Low, Scheduled), Assigned Trade (dropdown: HVAC Technician, Plumber, Electrician, General Maintenance, Custodial, Grounds Crew, Elevator Specialist, External Contractor), Assigned To (people), Status (status: Submitted, Triaged, Assigned, In Progress, Awaiting Parts, Completed, Verified, Cancelled), Date Submitted (date), Target Completion (date), Actual Completion (date), Estimated Cost (numbers, currency), Actual Cost (numbers, currency), Description (long text), Resolution Notes (long text), Photos (files), Satisfaction Rating (numbers, 1-5). Create groups: 'Emergency — Active', 'Urgent — This Week', 'Standard Queue', 'Scheduled Maintenance', 'Completed This Month'. Add automations: when Priority is 'Emergency', immediately notify the Facilities Director and on-call supervisor; when Status changes to 'Completed', send satisfaction survey to Submitted By email; when Status is 'Assigned' for more than 48 hours without changing, escalate to supervisor; when a Building has more than 5 open work orders, flag for Facilities Director review. Add a Kanban view by Status. Add a Dashboard with: Open Work Orders by Building (bar chart), Work Orders by Category (pie chart), Average Resolution Time (number widget), Emergency vs Standard ratio (line chart over time), Overdue Work Orders list (filtered where Target Completion < today and Status is not Completed), and Monthly Volume trend."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Campus Maintenance Dispatcher
**Agent Purpose:** Automatically triages, prioritizes, and routes incoming work orders while identifying patterns that signal systemic building issues requiring preventive intervention.

**Triggers:**
- New work order submitted via form, email, or QR code scan
- Work order SLA at risk (approaching target completion without progress)
- Same building receives 5+ work orders in a 30-day window for the same category
- Daily morning digest at 7 AM for operations supervisor
- Weather alert integration (freeze warnings trigger pipe check protocols)

**Actions:**
- Analyzes work order description to auto-categorize (HVAC, plumbing, electrical, etc.) and assign initial priority based on keywords, building criticality, and historical patterns
- Routes to appropriate trade team based on category, current workload balancing, and technician proximity/specialization
- Generates "Building Health Alert" when repeat issues suggest systemic problems (e.g., "Science Hall has had 8 plumbing work orders in 4 weeks — all in the north wing. Recommend pipe infrastructure assessment.")
- Creates preventive maintenance schedules based on asset age, work order history, and manufacturer recommendations
- Estimates completion time and cost based on similar historical work orders
- Generates weekly operations report for VP of Administration with volume trends, SLA performance, and budget utilization

**Data Required:**
- Work order submission data (forms, email parsing)
- Building and room inventory with asset data
- Technician schedules, skills, and current assignments
- Historical work order data for pattern analysis
- Weather API integration for proactive alerts
- Building automation system data (if available — temperature, humidity sensors)

**Autonomy Level:** Escalation-Based
Standard work order triage and routing are fully automated. Emergency work orders are auto-dispatched but also alert human supervisors. Preventive maintenance recommendations require human approval before scheduling. Budget expenditures above $5,000 require director authorization.

**Example Interaction:**
> At 2:47 AM on a January night, the building automation system in the Chemistry Research Building shows a rapid temperature drop in the third-floor laboratory wing. The Campus Maintenance Dispatcher creates an emergency work order: "Potential HVAC failure — Chemistry Building 3rd floor. Temperature dropped from 68°F to 52°F in 90 minutes. Risk: Active research experiments and chemical storage require temperature-controlled environment." The agent immediately pages the on-call HVAC technician (Mike Torres), notifies the Facilities Director, and cross-references the building's maintenance history — discovering that the same air handling unit was repaired twice in the past 4 months. The agent adds a note: "AHU-3C has had 3 service calls since October. Recommend full unit replacement assessment." It also automatically notifies the Chemistry Department's lab manager so they can check sensitive experiments. Mike arrives at 3:15 AM and finds a failed compressor. The agent updates the work order status, creates a follow-up item for unit replacement evaluation, and logs the estimated emergency repair cost of $8,500 for budget tracking.

---

### Use Case 2: Campus Space Utilization & Scheduling

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Space is the most expensive and scarce resource on any college campus. A typical university has 2-5 million gross square feet, yet classroom utilization averages only 35-45% (rooms sit empty more than half the time). Meanwhile, departments fight over lab space, study rooms are impossible to book, and the Registrar's office spends weeks each semester manually fitting 3,000+ course sections into 200+ classrooms. Most institutions use legacy scheduling systems (25Live, Ad Astra, or CollegeNET) that don't integrate with facilities data, lack real-time occupancy information, and can't optimize for energy savings. The space management team often has no visibility into how spaces are actually used vs. how they're scheduled.

#### The Solution
monday.com Work Management for space request, allocation, and utilization tracking. A master Space Inventory board catalogs every room on campus with capacity, equipment, ADA accessibility, technology, and scheduling availability. Connected boards manage space requests (from departments, student organizations, event planners), room scheduling, and utilization analytics. Dashboards visualize utilization by building, room type, time block, and day of week — revealing optimization opportunities. Integration with occupancy sensors (where available) provides actual vs. scheduled utilization data.

#### The Outcome
- 20-30% improvement in classroom utilization through data-driven scheduling
- $2-10M avoided in new construction costs by better using existing space
- 90% reduction in space request processing time (from 2 weeks to same-day)
- Energy savings from identifying and de-scheduling underutilized buildings during off-peak periods
- Reduced departmental conflict through transparent, data-driven space allocation

#### Discovery Questions
1. "What's your average classroom utilization rate, and how confident are you in that number?"
2. "How long does it take to process a space request from a department or student organization, and what does that workflow look like?"
3. "When the Registrar builds the course schedule each semester, how much is manual vs. automated?"
4. "Do you have occupancy sensor data, and if so, does it integrate with your scheduling system?"
5. "Has your institution postponed or avoided a new building because you were able to improve utilization of existing space?"

#### Industry Context
The Society for College and University Planning (SCUP) recommends a target classroom utilization of 67% (40 hours/week in a 60-hour scheduling window) and a seat occupancy of 67%. Most institutions are well below these benchmarks. The "space arms race" — where every department wants to control more square footage regardless of actual need — is a perennial challenge. Progressive institutions are moving toward "space charging" models where departments are allocated costs based on the space they control, creating financial incentives for efficient utilization. The Facilities Condition Assessment (FCA) and Space Utilization Study are two foundational operational assessments that inform capital planning.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Campus Space Utilization and Scheduling system for a university. Create a board called 'Campus Space Inventory' with columns: Room ID (text), Building (dropdown: Science Hall, Student Center, Library, Admin Building, Residence Hall A, Residence Hall B, Athletics Complex, Arts Center, Engineering Building, Dining Hall), Floor (dropdown: Basement, 1, 2, 3, 4, 5), Room Type (dropdown: Classroom, Lecture Hall, Laboratory, Seminar Room, Study Room, Office, Conference Room, Auditorium, Studio, Computer Lab, Maker Space), Capacity (numbers), ADA Accessible (status: Yes, No, Partial), Technology Level (dropdown: Basic, Standard AV, Advanced AV, Smart Classroom, Specialized Lab), Square Footage (numbers), Assigned Department (dropdown: Shared/Registrar, Biology, Chemistry, Engineering, Business, Arts, Computer Science, None), Weekly Scheduled Hours (numbers), Utilization Rate (numbers, percentage), Condition Rating (status: Excellent, Good, Fair, Poor), Last Renovation (date), Notes (long text). Create a connected board called 'Space Requests' with: Requestor Name (text), Department/Organization (text), Request Type (dropdown: Course Scheduling, Event, Meeting, Study Group, Research, Special Project), Preferred Room Type (dropdown, same as above), Capacity Needed (numbers), Date(s) Needed (date), Time Block (dropdown: Morning 8-12, Afternoon 12-5, Evening 5-10, Full Day, Multi-Day), Technology Requirements (dropdown: None, Projector, Video Conference, Lab Equipment, Recording, Streaming), Status (status: Submitted, Under Review, Approved, Denied, Waitlisted, Cancelled), Assigned Room (text), Approved By (people), Conflict Flag (status: None, Time Conflict, Capacity Issue, Equipment Mismatch), Notes (long text). Add automations: when Space Request is submitted, check for room availability and auto-assign if a clear match exists; when Conflict Flag is detected, notify the Space Planning team; when Utilization Rate on inventory board drops below 25%, flag room for review. Add Dashboard: Utilization by Building (bar chart), Room Type Availability This Week (summary), Pending Requests count, Utilization Heatmap by Day/Time (table widget with color coding), and Underutilized Rooms list (filtered to below 30% utilization)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Space Optimizer
**Agent Purpose:** Analyzes campus space utilization data, automatically matches space requests to optimal rooms, and identifies opportunities to improve utilization and reduce costs.

**Triggers:**
- New space request submitted
- Semester scheduling period begins (4 months before each semester)
- Weekly utilization report cycle every Monday
- Occupancy sensor data shows significant variance from scheduled use
- New building or renovation project proposed (triggers utilization analysis to justify need)

**Actions:**
- Auto-matches space requests to available rooms based on capacity, technology, accessibility, location preference, and current utilization (prioritizing underutilized spaces)
- Generates semester-level room optimization recommendations for the Registrar: "Moving BIOL 201 from the 300-seat lecture hall to the 150-seat room saves $12,000/semester in energy costs and opens the larger room for high-demand events"
- Identifies "ghost bookings" — scheduled spaces that sensor data shows are consistently empty — and notifies the booking department
- Creates utilization trend reports by building, showing where investment is needed vs. where space is surplus
- Generates capital planning data: "Based on utilization trends, the campus needs 3 additional seminar rooms and has surplus capacity in large lecture halls. Recommend converting Lecture Hall C to four breakout rooms."
- Calculates energy cost per occupied hour for each building, identifying efficiency opportunities

**Data Required:**
- Room inventory with specifications
- Course scheduling data from Student Information System (Banner, PeopleSoft, Workday Student)
- Occupancy sensor data (where available)
- Event scheduling calendars
- Energy consumption data by building (from BMS or utility meters)
- Historical utilization trends

**Autonomy Level:** Human-in-the-Loop
Routine space request matching is automated for standard requests. Complex scheduling (multi-room events, recurring research reservations) requires planner approval. Capital planning recommendations are generated as proposals for the Space Committee. The agent never cancels or reassigns existing bookings without human authorization.

**Example Interaction:**
> As the Spring 2026 semester approaches, the Space Optimizer analyzes the Registrar's preliminary course schedule against the room inventory. It identifies 47 scheduling inefficiencies: 12 courses placed in rooms where capacity exceeds enrollment by more than 100% (wasting large rooms on small classes), 8 rooms scheduled below 20% utilization on Fridays (a common pattern as faculty avoid Friday classes), and 3 lab conflicts where two departments are double-booked. The agent generates an optimization report: "By implementing the suggested 47 adjustments, the university can: (1) Free up 3 large lecture halls for 15+ hours/week for events and special programming, (2) Close the Engineering Building's second floor on Fridays, saving an estimated $8,200/month in HVAC and lighting costs, (3) Resolve all 3 lab conflicts without requiring any class time changes." The Space Planning team reviews the recommendations, approves 41 of 47 (rejecting 6 due to faculty proximity preferences), and implements the changes before the schedule is published.

---

### Use Case 3: Capital Project & Construction Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Universities manage complex capital portfolios — new buildings, major renovations, infrastructure upgrades, and deferred maintenance projects — often worth $50-500M+ in active construction at any given time. Project management for capital construction is typically handled through a combination of Primavera/MS Project (for contractors), spreadsheets (for budget tracking), email (for communication), and paper files (for compliance documentation). The VP of Facilities juggles 15-30 active projects with different contractors, architects, timelines, and budgets. Change orders are the bane of university construction — averaging 10-15% of project cost — and are often poorly tracked. Board of Trustees reporting requires manual compilation that takes days each quarter.

#### The Solution
monday.com Work Management as a capital project portfolio management platform. Each project is tracked on a master portfolio board with connected sub-boards for individual project phases, milestones, budgets, change orders, RFIs (Requests for Information), submittals, and compliance documents. Timeline and Gantt views provide portfolio-level visibility. Budget tracking columns show original budget, approved changes, actual spend, and projected final cost. Automations alert project managers when milestones are at risk, budgets exceed thresholds, or contractor submissions are overdue.

#### The Outcome
- 30% reduction in project reporting time through automated dashboard generation
- 15% fewer change order surprises through early detection of scope creep indicators
- Real-time portfolio visibility for VP and Board of Trustees — no more month-old data
- Improved contractor accountability through transparent milestone and submission tracking
- Compliance documentation in one place for audits and accreditation

#### Discovery Questions
1. "How many active capital projects are you managing simultaneously, and what's the total value of your construction portfolio?"
2. "How do you currently track project budgets, and how quickly do you know when a project is trending over budget?"
3. "What does your Board of Trustees reporting process look like for capital projects — how long does it take to compile?"
4. "How do you manage change orders — is there a formal approval workflow, and can you see cumulative change order impact in real-time?"
5. "When you have an accreditation visit or state audit, how easily can you produce the compliance documentation for capital projects?"

#### Industry Context
University capital projects are uniquely complex because of the approval chain: projects typically require approval from department leadership, the Provost's office, the VP of Administration, the President, and the Board of Trustees — and often the state legislature for public institutions. The procurement process is also heavily regulated, with public universities required to follow state procurement laws (competitive bidding, MBE/WBE requirements, prevailing wage compliance). "Soft costs" (architecture, engineering, permits, project management) typically add 25-35% on top of construction costs. The American Council on Education (ACE) recommends that institutions spend at least 2.5% of replacement value annually on maintenance and renewal — most spend less than 1.5%.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Capital Project Portfolio Management system for a university. Create a board called 'Capital Projects Portfolio' with columns: Project Name (text), Project ID (text), Project Type (dropdown: New Construction, Major Renovation, Infrastructure Upgrade, Deferred Maintenance, Technology Upgrade, Sustainability Retrofit), Building/Location (text), Project Manager (people), Architect/Engineer Firm (text), General Contractor (text), Phase (status: Planning, Design, Bidding, Construction, Punch List, Closeout, Complete), Original Budget (numbers, currency), Approved Change Orders (numbers, currency), Current Budget (numbers, formula: Original + Changes), Actual Spend to Date (numbers, currency), Budget Variance (numbers, formula: Current Budget - Actual Spend), Percent Complete (numbers, percentage), Start Date (date), Original End Date (date), Projected End Date (date), Schedule Variance Days (numbers), Funding Source (dropdown: State Appropriation, Bond Issue, Donor Gift, Reserves, Federal Grant, Mixed), Board Approval Status (status: Not Required, Pending, Approved), Compliance Status (status: Current, Issue Flagged, Audit Required), Risk Level (status: Low, Medium, High, Critical), Notes (long text). Create groups: 'Active Construction', 'In Design', 'In Planning', 'Recently Completed', 'On Hold'. Add a Timeline/Gantt view showing all projects. Create a connected board called 'Change Orders' with: Project (connected), CO Number (text), Description (long text), Requested By (dropdown: Contractor, Architect, University, Regulatory), Cost Impact (numbers, currency), Schedule Impact Days (numbers), Status (status: Submitted, Under Review, Approved, Denied), Approved By (people), Date Submitted (date), Date Resolved (date). Add automations: when Budget Variance goes negative (over budget), change Risk Level to High and notify VP of Facilities; when Schedule Variance exceeds 30 days, notify Project Manager and VP; when Change Order is submitted, notify Project Manager for review; when Phase changes to 'Complete', create closeout checklist subtasks. Add Dashboard: Portfolio Budget Summary (total Original Budget, total Actual Spend, total Variance), Projects by Phase (bar chart), Budget Variance by Project (bar chart, sorted worst to best), Change Order Volume and Value trend, Schedule Performance (on-time vs delayed count), and At-Risk Projects list."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Capital Project Sentinel
**Agent Purpose:** Monitors all active capital projects for budget, schedule, and compliance risks, generates Board-ready reports, and predicts project outcomes based on early indicators.

**Triggers:**
- Weekly project update cycle every Monday at 9 AM
- Change order submitted on any project
- Monthly budget reconciliation from finance system
- Board of Trustees meeting scheduled (triggers report generation 2 weeks prior)
- Contractor milestone deadline approaching (7 days, 3 days, 1 day)

**Actions:**
- Generates weekly "Red/Yellow/Green" status report for every active project based on budget variance, schedule variance, and compliance status
- Predicts final project cost by analyzing change order velocity (rate of change orders per month) and comparing to historical patterns for similar project types
- Compiles Board of Trustees capital report automatically: project photos (from files column), financial summary, schedule overview, risk items, and upcoming milestones
- Flags compliance gaps: missing permits, expired contractor insurance, overdue inspection certifications
- Analyzes change order patterns across the portfolio to identify systemic issues (e.g., "3 of 4 projects with Contractor X have experienced 15%+ change orders — consider procurement review")
- Generates contractor performance scorecards based on schedule adherence, change order history, quality metrics, and communication responsiveness

**Data Required:**
- Project management boards with budget and schedule data
- Change order history
- Finance system integration for actual spend data
- Contractor documentation (insurance, permits, certifications)
- Historical project completion data for benchmarking
- Photo/document uploads for progress tracking

**Autonomy Level:** Escalation-Based
Status calculations, report generation, and compliance flag detection are fully automated. Risk escalations are automated but response decisions are human. Budget reforecasts are generated as recommendations for the Project Manager to validate. Board reports are auto-generated but require VP review before distribution.

**Example Interaction:**
> The Capital Project Sentinel generates its weekly portfolio update and flags the new Science Research Building ($45M project) as "Yellow — trending to Red." The analysis: construction is 6 weeks into a 24-month schedule, but the change order velocity is concerning — 3 change orders totaling $380K in the first 6 weeks. Based on historical patterns for similar research building projects, the agent projects that if the current change order rate continues, the project will exceed its budget by 12-18% ($5.4-8.1M). The agent recommends: "(1) Schedule a scope review meeting with the architect and GC to identify root causes of early changes, (2) Consider a design audit — 2 of 3 change orders stem from coordination issues between MEP and structural drawings, which suggests incomplete design documents, (3) Benchmark: Our last two research buildings had 80% of change orders occur in the foundation and structural phases — if we can resolve design coordination now, we may prevent the majority of future changes." The VP of Facilities reviews the alert and schedules an emergency project review meeting, using the agent's analysis as the meeting agenda.

---

### Use Case 4: Environmental Health & Safety (EH&S) Compliance Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Universities are complex regulatory environments — they house chemical laboratories, biological research facilities, radiation sources, asbestos-containing buildings, industrial kitchens, athletic facilities, and performing arts venues, each with distinct safety and compliance requirements. The EH&S team (often just 3-8 people at mid-size institutions) must track chemical inventories, lab safety inspections, fire safety compliance, OSHA incident reports, hazardous waste disposal, radiation safety, biosafety protocols, and ADA compliance across hundreds of facilities. Most manage this through paper inspection forms, disconnected spreadsheets, and filing cabinets full of compliance records. When a state inspector arrives unannounced, the scramble to locate documentation can take days. Non-compliance fines range from $5,000 to $500,000+, and a serious incident can trigger lawsuits, accreditation review, and reputational damage.

#### The Solution
monday.com Work Management as a centralized EH&S compliance platform. Boards track inspection schedules, findings, corrective actions, incident reports, chemical inventories, and training compliance. Each regulatory domain (fire safety, lab safety, environmental, ADA) has a structured workflow from inspection through remediation. Automations ensure that inspection schedules are never missed, corrective actions are tracked to completion, and compliance documentation is always audit-ready. Dashboards give the EH&S Director real-time compliance status across the entire campus.

#### The Outcome
- 100% on-time inspection completion (up from ~75%)
- 60% faster corrective action resolution through automated tracking and escalation
- Audit-ready documentation available instantly (vs. days of compilation)
- $200K-1M annual avoided fines and legal costs through proactive compliance
- Reduced institutional liability and improved safety culture

#### Discovery Questions
1. "How many regulatory inspection types does your EH&S team manage, and how do you currently track inspection schedules and findings?"
2. "When a state or federal inspector arrives, how long does it take to produce the compliance documentation they request?"
3. "What's your corrective action close-out rate — do you have visibility into how many findings from past inspections are still open?"
4. "How do you track chemical inventories across research laboratories, and is that data accessible in an emergency?"
5. "Has your institution ever faced compliance fines or near-misses, and what would it be worth to eliminate that risk?"

#### Industry Context
The "Right-to-Know" laws (OSHA Hazard Communication Standard) require universities to maintain Safety Data Sheets (SDS) for every chemical on campus and make them accessible to any employee within minutes. The EPA's Resource Conservation and Recovery Act (RCRA) governs hazardous waste management with strict generator status rules that can change based on monthly waste volume. Universities with research reactors or radiation sources must comply with NRC (Nuclear Regulatory Commission) requirements. The Clery Act requires disclosure of campus safety statistics. All of this creates a compliance web that is impossible to manage manually at scale.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Environmental Health & Safety Compliance system for a university. Create a board called 'EH&S Compliance Tracker' with columns: Inspection/Requirement Name (text), Regulatory Domain (dropdown: Fire Safety, Lab Safety, Chemical Hygiene, Radiation Safety, Biosafety, Environmental/EPA, OSHA, ADA Accessibility, Food Safety, Clery Act), Building (dropdown: Science Hall, Student Center, Library, Admin Building, Residence Hall A, Residence Hall B, Athletics Complex, Arts Center, Engineering Building, Dining Hall, Research Center), Frequency (dropdown: Daily, Weekly, Monthly, Quarterly, Semi-Annual, Annual, Biennial, As-Needed), Last Inspection Date (date), Next Due Date (date), Inspector (people), Status (status: Current, Due Soon, Overdue, In Remediation, Non-Compliant), Findings Count (numbers), Open Corrective Actions (numbers), Risk Level (status: Low, Medium, High, Critical), Documentation (files), Notes (long text). Create a connected board called 'Corrective Actions' with: Finding Description (long text), Source Inspection (connected to Compliance Tracker), Building (mirror), Regulatory Domain (mirror), Severity (status: Minor, Moderate, Major, Critical), Assigned To (people), Due Date (date), Status (status: Open, In Progress, Awaiting Parts/Vendor, Verification Needed, Closed), Evidence of Correction (files), Closed Date (date), Days Open (formula: today - creation date). Create groups on Compliance Tracker: 'Overdue — Immediate Attention', 'Due This Month', 'Current — On Schedule', 'Annual Reviews'. Add automations: when Next Due Date is 14 days away, notify Inspector; when Next Due Date passes without status update, move to 'Overdue' group and notify EH&S Director; when all Corrective Actions for an inspection are 'Closed', change parent Status to 'Current'; when Severity is 'Critical', immediately notify EH&S Director and VP of Administration. Add Dashboard: Compliance Status by Domain (bar chart), Overdue Items count (number widget, red), Open Corrective Actions by Building (bar chart), Average Days to Close Corrective Actions (number widget), Upcoming Inspections This Month (list), and Compliance Rate percentage (Current / Total × 100)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Compliance Guardian
**Agent Purpose:** Proactively manages the university's EH&S compliance calendar, tracks corrective actions to completion, and ensures audit-readiness at all times.

**Triggers:**
- Inspection due date approaching (30, 14, 7, 1 day reminders at escalating urgency)
- Corrective action past due date
- New regulatory requirement published (manual entry or RSS from regulatory agencies)
- Incident report filed (triggers investigation workflow)
- External inspection announced or detected (e.g., state fire marshal notification)

**Actions:**
- Generates monthly compliance calendar with all upcoming inspections, certifications, and training renewals
- Creates inspection checklists pre-populated with building-specific requirements (e.g., lab safety checklist includes chemical inventory verification for science buildings, food safety checklist includes temperature log review for dining facilities)
- Tracks corrective actions with automated escalation: Day 1 → assigned to responsible party; Day 7 → reminder; Day 14 → escalate to department head; Day 21 → escalate to EH&S Director; Day 30 → escalate to VP
- Generates "Audit Ready Report" on demand — a complete compliance package for any building or regulatory domain showing current status, recent inspections, open items, and documentation
- Identifies regulatory trends: "Fire safety findings have increased 40% in residence halls this semester — recommend targeted fire safety awareness campaign"
- Maintains running compliance score by building and department for leadership visibility

**Data Required:**
- Inspection schedule database with regulatory frequencies
- Historical inspection records and findings
- Corrective action tracking data
- Chemical inventory system integration
- Training records (who has completed required safety training)
- Building inventory with hazard classifications

**Autonomy Level:** Escalation-Based
Scheduling, reminders, and checklist generation are fully automated. Corrective action tracking and escalation follow predetermined rules automatically. Compliance reports are auto-generated. Decisions about remediation approach, budget allocation for corrections, and regulatory responses require human judgment.

**Example Interaction:**
> It's October, and the Compliance Guardian generates the monthly compliance report. It flags that 3 research labs in the Chemistry Building are overdue for their quarterly chemical hygiene inspections by 12 days. The agent has already sent reminders to the assigned inspector (Dr. Martinez, the departmental safety officer) at days 7 and 14 with no response. It now escalates to the EH&S Director with context: "Chemistry Building Labs 301, 305, and 312 are overdue for quarterly chemical hygiene inspections. Dr. Martinez (assigned inspector) has not responded to two reminders. Historical context: Lab 305 had 3 findings on the last inspection (improper chemical storage, expired SDS binder, and blocked emergency shower access). Given the open findings and overdue status, recommend prioritizing Lab 305 and assigning a backup inspector. Note: The state DEP conducted a surprise inspection at State University last month focused on chemical hygiene — our region may be in a heightened inspection cycle." The EH&S Director reassigns the inspections to a staff member with Chemistry lab expertise, and the agent generates the pre-populated inspection checklists including carry-forward items from the previous inspection's findings.

---

### Use Case 5: Campus Event & Move Management Operations

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
University operations teams support hundreds of events per year — from orientation week and homecoming to guest lectures, career fairs, concerts, athletic events, and commencement. Each event requires coordination across multiple operations teams: facilities (setup, teardown, cleaning), IT (AV, networking), campus safety (traffic, security), dining (catering), and parking (event permits, shuttle routes). Currently, event operations are managed through email chains that grow to 50+ messages, with no single person having visibility into all operational requirements. Move management (department relocations, furniture installations, lab setups) follows a similar pattern. The result: forgotten setup requirements, conflicting resource allocations, and exhausted operations staff.

#### The Solution
monday.com Work Management as an event operations coordination hub. Each event is an item on a master board, with connected sub-items or linked boards for each operational requirement (facilities, IT, safety, dining, parking). Event request forms capture all operational needs upfront. Automations route requirements to the appropriate teams, track preparation progress, and flag conflicts (same crew needed for two events simultaneously). Timeline views show operations leadership the full event calendar with resource loading.

#### The Outcome
- 60% reduction in event coordination email volume
- Zero "forgotten requirements" through standardized intake and checklists
- 40% improvement in setup crew utilization through conflict detection and load balancing
- 75% faster event operations approval process
- Improved campus experience — events run smoothly, reflecting well on the institution

#### Discovery Questions
1. "How many events does your operations team support per month, and who currently coordinates the operational requirements?"
2. "What's the most complex event you manage annually, and what does the coordination process look like?"
3. "Have you ever had an event where a critical operational requirement was missed — AV not set up, catering not delivered, parking not arranged?"
4. "How do you handle resource conflicts when multiple events need the same setup crew or equipment on the same day?"
5. "How far in advance do event organizers need to submit requests, and is there a standard intake process?"

#### Industry Context
Commencement is the "Super Bowl" of university operations — a single event that requires coordination of venues, staging, audiovisual, catering for thousands, parking for 10,000+ vehicles, security, accessibility accommodations, livestreaming, and contingency plans for weather. Move management is the "silent workload" — every summer, universities relocate departments, install new lab equipment, reconfigure spaces, and prepare for the fall semester in a compressed 10-12 week window. The operations team essentially rebuilds parts of the campus every year.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Campus Event Operations Management system for a university. Create a board called 'Event Operations' with columns: Event Name (text), Event Type (dropdown: Academic Conference, Student Activity, Athletic Event, Commencement, Orientation, Career Fair, Guest Lecture, Concert/Performance, Board Meeting, Community Event, Department Move), Event Date (date), Setup Date (date), Teardown Date (date), Location (dropdown: Student Center Ballroom, Main Quad, Athletics Stadium, Auditorium, Library Atrium, Dining Hall, Arts Center Theater, Engineering Courtyard, Multiple Locations), Expected Attendance (numbers), Event Organizer (text), Organizer Contact (email), Operations Coordinator (people), Status (status: Requested, Planning, Approved, Setup In Progress, Active, Teardown, Complete, Cancelled), Facilities Needs (dropdown multi: Tables, Chairs, Staging, Podium, Tent, Signage, Power Drops, Cleaning), IT/AV Needs (dropdown multi: Projector, Sound System, Microphones, Video Recording, Livestream, WiFi Boost, Display Screens), Safety Needs (dropdown multi: Security Officers, Traffic Control, EMT Standby, Crowd Management, Metal Detectors), Catering (status: Not Needed, Requested, Confirmed, Delivered), Parking Plan (status: Not Needed, Standard, Event Permits Required, Shuttle Service, Road Closures), Budget (numbers, currency), Setup Crew Assigned (people), Notes (long text). Create groups: 'This Week', 'Next Week', 'This Month', 'Future Events', 'Completed'. Add automations: when Status changes to 'Approved', create subtask items for each operational need (facilities setup, AV setup, safety briefing, catering confirmation, parking coordination); when Setup Date is 3 days away and any subtask is incomplete, notify Operations Coordinator; when two events on the same date require the same Setup Crew, flag conflict and notify Operations Director. Add Timeline view showing all events. Add Dashboard: Events This Month (count), Events by Type (pie chart), Resource Utilization calendar view, Upcoming Events requiring setup this week (list), and Budget vs Actual spend."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Event Ops Coordinator
**Agent Purpose:** Orchestrates multi-team event operations by automatically routing requirements, detecting resource conflicts, and ensuring every event detail is covered from request through teardown.

**Triggers:**
- New event request submitted via form
- Event date is 2 weeks away (triggers operations planning phase)
- Resource conflict detected between events
- Setup date is 48 hours away (final readiness check)
- Event marked as "Complete" (triggers teardown and post-event workflow)

**Actions:**
- Parses event request form and automatically creates operational subtasks for each team (facilities, IT, safety, dining, parking) with pre-populated requirements based on event type and venue
- Detects resource conflicts across concurrent events and suggests alternatives (different crew assignment, staggered setup times, equipment substitution)
- Generates setup instruction sheets for facilities crew based on event requirements and venue specifications
- Sends automated reminders to all contributing teams at 2 weeks, 1 week, 3 days, and 1 day before event
- Creates post-event review items capturing feedback, actual attendance, issues encountered, and lessons learned
- Optimizes summer move schedule by sequencing department relocations to minimize disruption and maximize crew efficiency

**Data Required:**
- Event request data
- Venue specifications (capacity, equipment, layout options)
- Crew schedules and availability
- Equipment inventory (tables, chairs, AV equipment, staging)
- Historical event data for similar event type planning
- Academic calendar for scheduling context

**Autonomy Level:** Human-in-the-Loop
Standard event operations routing and reminders are automated. Resource conflict resolution recommendations require Operations Coordinator approval. High-profile events (commencement, board meetings) require director-level review of all operational plans. Budget approvals above threshold require human sign-off.

**Example Interaction:**
> The Student Activities office submits an event request for a spring concert on the Main Quad — expected attendance 3,000, requiring staging, sound system, lighting, security (8 officers), EMT standby, food truck parking permits, and road closures. The Event Ops Coordinator processes the request and immediately flags three issues: (1) The Athletics Department has a home baseball game the same afternoon with shared parking lots — suggests implementing a split parking plan with shuttle service from the overflow lot, (2) The sound system requested exceeds the university's noise ordinance limits for the Main Quad after 9 PM — suggests either a hard stop at 9 PM or relocating to the Athletics Stadium which has higher noise thresholds, (3) The requested setup time conflicts with a facilities crew already assigned to a conference teardown in the Student Center — suggests starting setup 2 hours later or pulling crew from the evening shift. The agent generates a comprehensive operations plan with all requirements, assigned teams, timeline, and a weather contingency option (move to the Student Center Ballroom if rain probability exceeds 60%). The Operations Coordinator reviews, adjusts the parking plan, approves the 9 PM hard stop, and confirms the staggered crew schedule.

---

### Use Case 6: Energy Management & Sustainability Operations

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Universities are under intense pressure to reduce carbon footprints — many have signed the Presidents' Climate Leadership Commitments (formerly the American College & University Presidents' Climate Commitment) pledging carbon neutrality by 2030 or 2050. Energy costs represent 15-25% of a university's operating budget ($5-50M+ annually), yet most institutions lack granular visibility into energy consumption patterns. Building-level metering may exist, but the data sits in building management systems (BMS) that don't connect to operational decision-making. Operations teams know that certain buildings are energy hogs but can't quantify the impact of specific interventions (scheduling changes, equipment upgrades, behavioral programs). Sustainability reporting is a manual quarterly ordeal that pulls data from utility bills, BMS exports, and spreadsheets.

#### The Solution
monday.com Work Management for sustainability project tracking combined with energy dashboard integration. A Sustainability Initiatives board tracks all energy and environmental projects with timelines, budgets, and measured impact. Connected boards manage utility data, carbon accounting, sustainability certifications (LEED, STARS, etc.), and compliance with institutional climate commitments. Automations flag buildings exceeding energy baselines, track renewable energy generation, and generate sustainability reports for leadership and accreditation bodies.

#### The Outcome
- 10-20% energy cost reduction through data-driven operational decisions
- Automated sustainability reporting saving 40+ hours per quarter
- Clear ROI tracking for green investments (LED retrofits, solar installations, HVAC upgrades)
- Progress toward climate commitments tracked transparently for stakeholders
- STARS (Sustainability Tracking, Assessment & Rating System) reporting streamlined

#### Discovery Questions
1. "What are your institution's carbon reduction commitments, and how are you tracking progress against them?"
2. "Do you have building-level energy metering, and does that data inform operational decisions like scheduling or HVAC setpoints?"
3. "How long does it take to compile your annual sustainability report, and what's the data collection process?"
4. "What's your biggest energy expense — and do you have visibility into what's driving it at the building level?"
5. "Have you quantified the ROI on past sustainability investments (LED retrofits, solar, etc.) to build the case for future ones?"

#### Industry Context
The AASHE STARS rating system is the dominant sustainability assessment framework for higher education — institutions are rated Bronze, Silver, Gold, or Platinum based on performance across academics, engagement, operations, planning, and innovation. STARS is used for peer benchmarking and is increasingly cited in college rankings. Energy Performance Contracting (EPC) is a popular financing mechanism where energy savings pay for capital improvements — but it requires robust baseline energy data and measurement/verification (M&V) protocols. Many universities are also pursuing "green revolving funds" where energy savings are reinvested in future sustainability projects.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Energy Management and Sustainability Operations system for a university. Create a board called 'Sustainability Initiatives' with columns: Initiative Name (text), Category (dropdown: Energy Efficiency, Renewable Energy, Water Conservation, Waste Reduction, Transportation, Carbon Offsets, Behavior Change, Green Building), Building/Campus Area (text), Status (status: Proposed, Approved, In Progress, Completed, Ongoing, Deferred), Project Lead (people), Start Date (date), Target Completion (date), Budget (numbers, currency), Actual Cost (numbers, currency), Estimated Annual Savings (numbers, currency), Actual Annual Savings (numbers, currency), ROI Period Years (numbers), Carbon Impact Tons CO2e (numbers), Funding Source (dropdown: Operating Budget, Green Revolving Fund, Grant, Donor, Energy Performance Contract), STARS Category (dropdown: OP-1 Emissions Inventory, OP-5 Building Energy, OP-6 Clean Energy, OP-21 Water Use, OP-22 Rainwater), Notes (long text). Create a connected board called 'Building Energy Tracker' with: Building Name (text), Square Footage (numbers), Primary Use (dropdown: Academic, Research, Residential, Administrative, Athletics, Dining, Mixed), Annual kWh (numbers), Annual Therms (numbers), Annual Water Gallons (numbers), Energy Use Intensity EUI (numbers, kBTU/sqft), EUI Baseline Year (numbers), Current vs Baseline Percent (numbers), ENERGY STAR Score (numbers, 1-100), Solar Installed kW (numbers), Monthly Utility Cost (numbers, currency), Last Audit Date (date), Efficiency Rating (status: Leader, On Track, Below Average, Poor). Add automations: when EUI exceeds baseline by 15%, flag building and notify Energy Manager; when Initiative Status changes to 'Completed', prompt for Actual Annual Savings data entry; when Monthly Utility Cost exceeds previous month by 20% for any building, create investigation work order. Add Dashboard: Total Carbon Emissions vs Target (gauge chart), Energy Cost by Building (bar chart), Initiatives by Status (pie chart), Cumulative Savings from Completed Initiatives (number widget), EUI Improvement Trend (line chart), and Green Revolving Fund balance and ROI."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Green Campus Analyst
**Agent Purpose:** Monitors campus energy consumption, tracks sustainability initiative progress, and generates compliance reports for climate commitments and STARS certification.

**Triggers:**
- Monthly utility bill data imported
- Building energy consumption exceeds baseline threshold
- STARS reporting deadline approaching (annual)
- Sustainability initiative milestone reached
- Quarterly sustainability committee meeting (generates progress report 1 week prior)

**Actions:**
- Analyzes monthly energy data to identify anomalies: buildings using more energy than expected based on occupancy, weather, and season
- Generates building energy report cards: EUI comparisons, peer benchmarking within the campus portfolio, and trending
- Calculates ROI for completed sustainability projects using actual savings data vs. investment
- Compiles STARS reporting data automatically from operational boards, generating pre-filled submission worksheets
- Identifies high-impact efficiency opportunities: "Replacing the HVAC system in the Library (built 1972) would reduce energy consumption by an estimated 35% based on comparable retrofits — payback period: 4.2 years"
- Tracks progress toward institutional carbon neutrality commitment with projected timeline based on current trajectory

**Data Required:**
- Utility billing data (electricity, natural gas, water)
- Building management system data (where API available)
- Weather data for degree-day normalization
- Building inventory with age, type, and systems data
- Sustainability initiative boards
- STARS framework requirements

**Autonomy Level:** Fully Autonomous (for analysis and reporting), Human-in-the-Loop (for recommendations)
Data analysis, anomaly detection, and report generation are fully automated. Capital investment recommendations, operational changes (HVAC setpoint adjustments, scheduling changes), and STARS submissions require human review and approval.

**Example Interaction:**
> The Green Campus Analyst processes January's utility data and identifies that the Engineering Building's electricity consumption spiked 42% compared to January of the previous year, despite similar weather patterns and no increase in scheduled occupancy. The agent cross-references with the work order system and discovers that a temporary chiller was installed in December for a research project but was never removed after the project completed — it's been running 24/7 for 6 weeks. The agent creates an urgent maintenance work order: "Temporary chiller in Engineering Building Room 104 appears to still be operational 6 weeks after the associated research project (PI: Dr. Chen, Project: Thermal Dynamics Study) ended on December 15. Estimated unnecessary energy cost: $14,200 for the 6-week period. Recommend immediate shutdown and removal." It also flags this as a process improvement opportunity: "Consider adding 'temporary equipment decommissioning' as a standard checklist item when research projects close."

---

### Use Case 7: Emergency Preparedness & Continuity Planning

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Universities must prepare for a wide range of emergencies: severe weather, active threats, building evacuations, pandemic responses, infrastructure failures, and hazardous material incidents. Emergency preparedness involves maintaining building-specific evacuation plans, conducting drills, training building coordinators, managing emergency supplies, and updating continuity plans — all while meeting Clery Act and OSHA requirements. Most institutions store emergency plans in PDF documents on shared drives that haven't been updated in years. Building coordinator lists are out of date (people change roles, new buildings are added). When an actual emergency occurs, the operations team scrambles to find the right plan, contact the right people, and coordinate the response.

#### The Solution
monday.com Work Management as an emergency preparedness management platform. A master Emergency Plans board tracks every building's emergency plan status, last update, assigned building coordinator, and drill history. Connected boards manage emergency supplies inventory, training compliance, incident response workflows, and post-incident reviews. Automations ensure that plans are reviewed annually, building coordinator assignments are current, and drill schedules are maintained. During an actual emergency, a pre-built incident response board can be activated with pre-assigned roles, communication checklists, and escalation protocols.

#### The Outcome
- 100% of building emergency plans current and accessible (up from ~60%)
- Annual drill completion rate at 100% across all buildings
- 50% faster emergency response activation through pre-built incident boards
- Clery Act compliance documentation always audit-ready
- Building coordinator turnover managed proactively (vs. discovering gaps during emergencies)

#### Discovery Questions
1. "When was the last time every building's emergency plan was reviewed and updated? Are you confident they're all current?"
2. "Do you have a current list of building emergency coordinators for every building, and how do you manage turnover?"
3. "When you conduct an emergency drill, how do you track participation, document the outcome, and capture lessons learned?"
4. "During your last actual emergency or weather event, what worked well and what revealed gaps in your preparedness?"
5. "How do you currently compile your Clery Act emergency response documentation for the Annual Security Report?"

#### Industry Context
The Clery Act requires institutions to have emergency response and evacuation procedures, test them at least annually, and publicize them. FEMA's Higher Education Emergency Management program provides frameworks. The National Incident Management System (NIMS) and Incident Command System (ICS) are the standard frameworks for emergency response in higher education. Most universities require designated staff to complete FEMA ICS-100, ICS-200, and ICS-700 training. The challenge is that emergency management is typically a collateral duty for operations staff — they do it in addition to their regular facilities responsibilities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Emergency Preparedness Management system for a university. Create a board called 'Emergency Preparedness' with columns: Building Name (text), Building Type (dropdown: Academic, Residential, Administrative, Research, Athletics, Dining, Library, Mixed), Building Coordinator Name (text), Coordinator Contact (email), Coordinator Training Status (status: Current, Expiring Soon, Expired, Not Assigned), Emergency Plan Status (status: Current, Under Review, Needs Update, Overdue), Plan Last Updated (date), Plan Next Review (date), AED Location (text), Emergency Supply Kit (status: Stocked, Needs Resupply, Missing), Last Drill Date (date), Next Drill Date (date), Drill Type (dropdown: Fire Evacuation, Severe Weather Shelter, Active Threat Lockdown, Hazmat Evacuation, Earthquake), Drill Compliance (status: Completed, Scheduled, Overdue, Not Scheduled), Occupancy Capacity (numbers), Special Hazards (dropdown multi: Chemical Lab, Radiation, Biological, High Voltage, Confined Spaces, Pool, Commercial Kitchen, None), Accessibility Notes (long text), Notes (long text). Create groups: 'Overdue — Action Required', 'Current — On Schedule', 'Residential Buildings', 'Academic Buildings', 'Support Facilities'. Add automations: when Plan Next Review date is 30 days away, notify Building Coordinator and EH&S team; when Coordinator Training Status changes to 'Expired', immediately notify Operations Director; when Next Drill Date passes without Drill Compliance changing to 'Completed', move to 'Overdue' group; when a new building is added, create checklist subtasks for: assign coordinator, develop emergency plan, stock supplies, schedule initial drill. Add Dashboard: Building Compliance Overview (percentage with current plans), Drill Completion Rate (this year), Coordinator Training Status distribution, Overdue Items list, and Next 30 Days drill and review calendar."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Emergency Readiness Monitor
**Agent Purpose:** Ensures every building on campus has current emergency plans, trained coordinators, and completed drills — proactively managing the compliance calendar that protects campus safety.

**Triggers:**
- Building coordinator role change detected (HR integration or manual update)
- Emergency plan review date approaching (60, 30, 14 days)
- Drill schedule date approaching
- Severe weather forecast detected (triggers readiness verification for affected buildings)
- Annual Clery Act reporting deadline (triggers documentation compilation)

**Actions:**
- Maintains a living dashboard of campus-wide emergency preparedness status with building-by-building drill-down
- Detects coordinator vacancies when HR data shows role changes and creates urgent assignment tasks
- Generates annual Clery Act emergency response documentation package from drill records, plan updates, and training completions
- Sends seasonal readiness reminders: hurricane season prep (coastal campuses), winter storm protocols, severe thunderstorm season
- Creates post-drill review items capturing participation rates, issues observed, and improvement actions
- Generates training compliance reports showing which staff need ICS/NIMS refresher courses

**Data Required:**
- Building inventory with coordinator assignments
- Emergency plan documents and review dates
- Drill schedule and completion records
- Training records (ICS-100, ICS-200, ICS-700 certifications)
- HR data for personnel change detection
- Weather API for severe weather alerts
- Emergency supply inventory

**Autonomy Level:** Escalation-Based
Schedule management, reminders, and reporting are fully automated. Coordinator reassignment recommendations require Operations Director approval. Emergency plan content updates require EH&S review. During actual emergencies, the agent activates pre-built response boards but humans make all response decisions.

**Example Interaction:**
> In March, the Emergency Readiness Monitor generates a seasonal readiness assessment as severe weather season approaches. It identifies 4 buildings where tornado shelter procedures haven't been drilled since the previous spring. It also flags that the new Biomedical Research Center (opened in January) doesn't have an emergency plan or assigned building coordinator yet. The agent creates a priority task list: "(1) Schedule severe weather shelter drills for Science Hall, Student Center, Residence Hall B, and the Arts Center within the next 3 weeks. (2) URGENT: Biomedical Research Center has no emergency plan — given the presence of BSL-2 biological materials and chemical labs, this requires an expedited plan development. Recommend assigning Dr. Sarah Park (department safety officer) as interim building coordinator and scheduling a plan development meeting this week. (3) Advisory: Building coordinator for the Library (Tom Henderson) retired last month — position shows as vacant. Recommend assigning interim coordinator from library staff." The Operations Director approves all three recommendations, and the agent automatically creates calendar events for the drills and plan development meetings.

---

### Use Case 8: Fleet & Transportation Operations

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
University transportation operations manage campus shuttle buses, maintenance vehicles, groundskeeping equipment, delivery trucks, and often a motor pool for staff/faculty use. A mid-size university may operate 20-80 vehicles, each requiring insurance, registration, maintenance scheduling, fuel tracking, and driver authorization. Most institutions manage fleet operations through spreadsheets and paper logs — vehicle maintenance is tracked by mileage stickers on dashboards, fuel purchases are reconciled from credit card statements, and driver authorization is managed through paper forms in filing cabinets. When a vehicle breaks down, there's no easy way to see its maintenance history. When an audit asks for fleet costs by department, it takes weeks to compile.

#### The Solution
monday.com Work Management for fleet lifecycle management. Each vehicle is an item on a Fleet Inventory board with maintenance schedules, cost tracking, assignment history, and compliance status. Connected boards manage maintenance work orders, fuel logs, driver authorization, and trip requests. Automations trigger maintenance reminders based on mileage or time intervals, flag expired registrations or insurance, and generate cost allocation reports by department.

#### The Outcome
- 25% reduction in vehicle downtime through proactive maintenance scheduling
- Accurate department-level fleet cost allocation for the first time
- Zero compliance gaps (expired registration, lapsed insurance, unauthorized drivers)
- 20% fleet cost reduction through utilization analysis (right-sizing the fleet)
- Eliminated paper logs and manual reconciliation

#### Discovery Questions
1. "How many vehicles does your university operate, and how do you currently track maintenance, fuel, and costs?"
2. "Can you tell me right now what the total fleet cost was last fiscal year, broken down by department?"
3. "How do you manage vehicle reservations and driver authorization — is it a paper-based process?"
4. "Have you ever had a vehicle break down that could have been prevented with better maintenance scheduling?"
5. "Do you know which vehicles in your fleet are underutilized and could be eliminated to save costs?"

#### Industry Context
University fleet operations are subject to state vehicle regulations, DOT requirements for shuttle buses (CDL drivers, vehicle inspection schedules, hours-of-service for applicable vehicles), and institutional insurance requirements. Many public universities are also subject to state fleet management mandates including alternative fuel requirements and fleet reduction targets. The "motor pool" model — shared vehicles reserved by department — is more cost-effective than department-owned vehicles but requires a reservation and tracking system that most institutions don't have.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Fleet & Transportation Management system for a university. Create a board called 'University Fleet' with columns: Vehicle ID (text), Vehicle Type (dropdown: Shuttle Bus, Cargo Van, Pickup Truck, Sedan, SUV, Golf Cart, Grounds Equipment, Specialty), Make/Model (text), Year (numbers), License Plate (text), VIN (text), Assigned Department (dropdown: Motor Pool, Facilities, Grounds, Athletics, Campus Safety, Dining, Mail Services), Current Mileage (numbers), Status (status: Active, In Maintenance, Reserved, Out of Service, Retired), Insurance Expiry (date), Registration Expiry (date), Last Maintenance (date), Next Maintenance Due (date or mileage trigger), Fuel Type (dropdown: Gasoline, Diesel, Electric, Hybrid, Propane), Annual Fuel Cost (numbers, currency), Annual Maintenance Cost (numbers, currency), Total Cost of Ownership (numbers, currency), Condition (status: Excellent, Good, Fair, Poor, Replace), Assigned Driver (people), Notes (long text). Create a connected board called 'Fleet Maintenance Log' with: Vehicle (connected), Service Type (dropdown: Oil Change, Tire Rotation, Brake Service, Transmission, Engine, Electrical, Body/Paint, DOT Inspection, Other), Date (date), Mileage at Service (numbers), Cost (numbers, currency), Vendor (text), Next Service Due (text), Performed By (dropdown: In-House, External Vendor), Notes (long text). Add automations: when Insurance Expiry or Registration Expiry is 30 days away, notify Fleet Manager; when Next Maintenance Due date arrives, create maintenance work order; when a vehicle's Annual Maintenance Cost exceeds 50% of its current value, flag for replacement review; when Status changes to 'Out of Service', notify assigned department. Add Dashboard: Fleet Size by Type (pie chart), Active vs Out of Service count, Total Fleet Costs by Department (bar chart), Upcoming Maintenance schedule, Vehicles Approaching Replacement (filtered list by Condition = Poor or Replace), and Monthly Fuel Cost trend."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Fleet Operations Manager
**Agent Purpose:** Manages the complete vehicle lifecycle from acquisition through disposal, optimizing maintenance schedules, costs, and fleet composition.

**Triggers:**
- Vehicle mileage update (manual entry or telematics integration)
- Maintenance due date or mileage threshold reached
- Insurance or registration expiration approaching (60, 30, 14 days)
- Monthly cost reconciliation from fuel cards and maintenance invoices
- Annual fleet review cycle (generates right-sizing analysis)

**Actions:**
- Schedules preventive maintenance based on manufacturer recommendations, mileage, and seasonal factors (winterization, AC service)
- Tracks total cost of ownership per vehicle and flags when repair costs suggest replacement
- Generates department cost allocation reports monthly (fuel + maintenance + insurance + depreciation)
- Analyzes motor pool utilization to identify underused vehicles that could be eliminated (e.g., "Van #7 has been used 6 days in the last 90 — annual cost is $4,800. Recommend reallocation or disposal.")
- Creates trip/reservation management for motor pool vehicles with automatic driver authorization verification
- Generates annual fleet plan with replacement schedule, budget projections, and alternative fuel transition recommendations

**Data Required:**
- Vehicle inventory and specifications
- Maintenance records and vendor data
- Fuel card transaction data
- Driver authorization database
- Reservation/trip logs
- Insurance and registration documents
- Telematics data (if available — GPS, mileage, idle time)

**Autonomy Level:** Escalation-Based
Maintenance scheduling, cost tracking, and compliance monitoring are fully automated. Vehicle replacement recommendations require Fleet Manager and budget authority approval. New vehicle acquisitions require procurement process. Driver authorization checks are automated but violations are escalated to safety officer.

**Example Interaction:**
> The Fleet Operations Manager runs its monthly analysis and presents a finding to the Fleet Manager: "The Grounds Department operates 4 pickup trucks. Analysis of GPS and trip data shows that Truck #12 (2018 F-150, 89,000 miles) has averaged only 3.2 trips per month over the past 6 months, compared to 18-22 trips for the other three trucks. Meanwhile, the Facilities Department has been submitting motor pool reservations 2-3 times per week for similar-capacity vehicles. Recommendation: Transfer Truck #12 from Grounds to the Motor Pool — this eliminates $680/month in Grounds Department fleet costs while reducing Motor Pool reservation conflicts by an estimated 40%. Additionally, Truck #12 is approaching its 90,000-mile service interval — recommend completing the major service before transfer. Estimated cost: $1,200." The Fleet Manager approves the transfer, and the agent automatically updates department allocations, schedules the service, and notifies both departments of the change.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| FCI (Facilities Condition Index) | Ratio of deferred maintenance cost to current replacement value — key metric for building portfolio health |
| EUI (Energy Use Intensity) | Energy consumption per square foot per year (kBTU/sf) — standard building energy efficiency metric |
| APPA | Association of Physical Plant Administrators — the professional organization for higher ed facilities management |
| SCUP | Society for College and University Planning — professional org covering space planning and capital development |
| STARS | Sustainability Tracking, Assessment & Rating System — AASHE's higher ed sustainability certification |
| Clery Act | Federal law requiring campus safety reporting, emergency procedures, and crime statistics disclosure |
| CMMS | Computerized Maintenance Management System — software for work order and asset management |
| BMS/BAS | Building Management System / Building Automation System — controls HVAC, lighting, and building systems |
| Deferred Maintenance | Maintenance work that has been postponed, typically due to budget constraints — the #1 operational challenge in higher ed |
| FTE | Full-Time Equivalent — standard staffing metric used in budget justifications |
| Capital Project | Major construction or renovation project, typically funded outside the operating budget |
| Change Order | A modification to a construction contract that changes scope, cost, or schedule |
| SDS | Safety Data Sheet — required documentation for every chemical on campus per OSHA |
| ICS | Incident Command System — standardized emergency management framework (FEMA/NIMS) |
| Title IX | Federal law prohibiting sex discrimination in education — has facilities implications (locker rooms, restrooms, housing) |
| Motor Pool | Shared vehicle fleet available for reservation by any department |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP of Administration / COO | Overall operational leadership, budget authority, reports to President | Ultimate decision-maker for operations tools |
| Associate VP of Facilities | Day-to-day facilities operations, maintenance, and capital projects | Key decision-maker and champion |
| Director of Facilities Management | Manages maintenance staff, work orders, and building operations | Primary user and influencer |
| Director of Campus Safety | Emergency management, safety compliance, Clery Act reporting | Decision-maker for safety/compliance tools |
| EH&S Director | Environmental health, lab safety, chemical management, regulatory compliance | Decision-maker for compliance tools |
| Space Planning Manager | Room scheduling, space utilization, allocation decisions | Key user for space management |
| Sustainability Officer | Carbon reduction, energy management, STARS reporting | Champion for sustainability tools |
| University Registrar | Course scheduling (drives classroom utilization) | Influencer — provides scheduling data |
| CIO / Director of IT | Technology infrastructure supporting operations | Influencer — integration requirements |
| CFO / VP of Finance | Budget allocation for operations, capital planning | Decision-maker for budget justification |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT / Technology | Operations depends on building technology (BMS, access control, AV); IT manages network and computing infrastructure | Connected boards for technology-dependent maintenance, shared asset management |
| Finance / Budget | Operations is the largest non-personnel budget line; capital projects require finance oversight | Budget tracking, cost allocation, and capital planning dashboards |
| HR / Human Resources | Operations employs large hourly/trade workforce; safety training compliance overlaps | Workforce scheduling, training tracking, and compliance management |
| Academic Affairs / Registrar | Course scheduling drives classroom utilization; faculty space requests flow through operations | Integrated space scheduling and classroom technology management |
| Student Affairs / Housing | Residential life depends on facilities for building maintenance and renovations | Residential maintenance work orders, housing turnover management |
| Marketing / Communications | Campus appearance impacts recruitment; sustainability achievements are marketing assets | Sustainability reporting for external communications |
| Procurement | Operations is the largest purchaser of goods and services; capital projects involve complex procurement | Vendor management, purchase order tracking, and contract management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SchoolDude / Brightly (Siemens) | Dominant higher ed CMMS and work order system | Legacy UX, limited analytics, no AI — monday.com offers modern experience with superior reporting and automation |
| TMA Systems | Enterprise-grade CMMS for large universities | Expensive, complex, slow to implement — monday.com is faster to deploy and more user-friendly |
| 25Live / CollegeNET | Dedicated higher ed space scheduling | Single-purpose tools that don't connect to facilities operations — monday.com unifies space + operations |
| Ad Astra | Academic scheduling optimization | Strong at course scheduling but doesn't extend to operations — monday.com bridges the gap |
| Planon | Integrated workplace management for large institutions | Enterprise pricing and complexity unsuitable for mid-market institutions — monday.com scales down elegantly |
| Spreadsheets & Paper | The honest reality for most mid-size institutions | Any structured system is an upgrade; monday.com's ease of use overcomes the "we've always done it this way" barrier |
| ServiceNow | IT service management expanding into facilities | IT-centric design doesn't fit facilities workflows — monday.com is more intuitive for operations teams |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have SchoolDude/TMA for work orders — why would we switch?" | Those are excellent work order systems, but they're single-purpose. Your operations team needs work orders AND space management AND capital projects AND compliance tracking AND sustainability reporting — all connected. monday.com replaces the 5-6 disconnected tools with one platform, and adds AI capabilities none of those legacy tools offer. |
| "Our operations staff aren't tech-savvy — they won't adopt a new system" | That's exactly why monday.com works for operations teams. The interface is visual, intuitive, and works on mobile — your trade technicians can update work orders from their phones. No training manuals needed. And the AI agent handles the complexity behind the scenes so your team just sees simple, clear tasks. |
| "We don't have the budget for new software" | Let's calculate: a single prevented HVAC failure saves $50-500K. Improving classroom utilization by 10% can defer a $20M building project. Reducing emergency maintenance by 20% saves staff overtime. The platform pays for itself within the first avoided incident. And consolidating 4-5 existing tool licenses may actually reduce your total software spend. |
| "Higher ed procurement takes 18 months and requires an RFP" | For institutions under procurement thresholds (often $25-50K), you can pilot with a department or division. Start with one high-pain use case (work orders or compliance tracking), prove the value, and then expand through a formal procurement process backed by measured ROI. |
| "Our data is too sensitive — student records, safety information" | monday.com is SOC 2 Type II certified, GDPR compliant, and offers enterprise security features. We're not storing student PII — we're managing operational workflows. Many universities already trust monday.com with similar data, and the platform supports role-based access so sensitive compliance data is only visible to authorized users. |
| "We need integration with Banner/PeopleSoft/Workday for student and HR data" | monday.com's open API and integration marketplace support connections with major higher ed systems. For common integrations, pre-built connectors exist. For complex integrations, the API is well-documented and your IT team or a certified partner can build custom connections. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for universities using monday.com for operations management]
- [Placeholder for higher ed institutions that improved facilities efficiency with monday.com]
- [Placeholder for campus operations teams that consolidated tools onto monday.com]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
