# Colleges & Universities × HR Playbook

## Overview

Human Resources departments in higher education operate in one of the most complex employment environments in any industry. A mid-size university employs 3,000–15,000 people across radically different employment categories: tenured and tenure-track faculty (governed by academic freedom protections and faculty handbooks), non-tenure-track lecturers and adjuncts (often part-time, sometimes unionized), classified staff (custodial, facilities, administrative — often under state civil service rules at public institutions), professional staff (exempt employees in administrative roles), graduate assistants (simultaneously students and employees), student workers (federal work-study and institutional), postdoctoral researchers, and medical residents at academic medical centers. Each category has different hiring processes, compensation structures, benefits eligibility, performance review cycles, and termination procedures.

University HR departments typically include functional areas for talent acquisition, compensation and classification, benefits administration, employee relations, training and organizational development, HR information systems (HRIS), payroll, and often a dedicated academic HR unit that handles faculty appointments, promotion and tenure processes, and sabbatical tracking. Public universities add layers of state employment law, civil service commission rules, and legislative reporting requirements. The HR team at a large university might number 50–120 professionals managing an employee population where annual turnover among staff reaches 15–25%, faculty searches take 6–12 months, and a single tenure review file can be 500+ pages.

Compliance demands are intense: Title IX, Title VII, ADA, FLSA, FMLA, state labor laws, EEOC reporting, ACA tracking for adjunct/part-time employees, visa sponsorship (H-1B, J-1) for international faculty, and collective bargaining agreements for unionized employees. Many universities are their region's largest employer, making HR decisions ripple through entire communities. The combination of employment complexity, regulatory burden, and lean staffing makes university HR departments perpetually stretched.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | HR teams are undersized for the complexity they manage; AI can handle administrative burden that consumes 60%+ of HR time |
| 2 | Scale Impact Without Overhead | High | Growing institutions add employees without proportionally growing HR; need to serve more people with same team |
| 3 | Consolidate Tech Stack with AI | Medium | Universities run fragmented HR systems (Banner HR, PeopleAdmin, Cornerstone, paper forms) that don't talk to each other |

## Prioritized Use Cases

---

### Use Case 1: Faculty Recruitment & Search Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Faculty hiring is the most consequential and time-consuming recruitment process in higher education. A single tenure-track search takes 6–12 months, involves a search committee of 3–7 faculty members, requires posting on discipline-specific job boards (HigherEdJobs, Chronicle, discipline listservs), generates 50–300 applications per position, demands compliance with affirmative action and equal opportunity requirements (documented at every stage), and culminates in on-campus interviews costing $3,000–$10,000 per finalist. HR coordinates 30–80 simultaneous faculty searches annually but has minimal visibility into where each search stands. Search committee chairs forget to submit required EEO documentation. Candidates fall through the cracks during the review process. The Dean's office calls HR weekly asking "Where are we on the Chemistry hire?" and no one has a real-time answer. Meanwhile, losing a top candidate because the approval chain took too long costs the department a year — searches operate on the academic calendar, and missing the hiring cycle means waiting until next fall.

#### The Solution
monday.com Work Management as the faculty search command center. Each open search is an item on a master recruitment board with status tracking through every phase: Position Approval → Job Posting → Application Review → Long List → Short List → On-Campus Interviews → Offer → Acceptance → Onboarding. Sub-items track individual candidates through the pipeline. Columns capture EEO data, search committee composition (with diversity requirements), interview schedules, reference check status, and approval chain progress. Automations route approval requests, remind search chairs of pending actions, and flag searches that stall. Dashboards show the Dean and Provost every active search, its stage, and any bottlenecks. Integration with the applicant tracking system (PeopleAdmin/PageUp) or direct form intake for applications.

#### The Outcome
- Real-time visibility across all active faculty searches for Deans and Provost
- 30% reduction in time-to-hire for faculty positions (from 9 months to 6 months)
- 100% EEO documentation compliance (automated checkpoints prevent advancement without required documentation)
- Reduced candidate dropout from slow processes

#### Discovery Questions
1. "How many faculty searches do you manage simultaneously, and what's your average time from posting to accepted offer?"
2. "How do you currently ensure search committees complete all required EEO documentation before advancing candidates?"
3. "When a Dean asks 'Where are we on the Biology search?', how long does it take to get an accurate answer?"
4. "Have you ever lost a top faculty candidate because your internal approval process was too slow?"
5. "How do you track the diversity composition of your applicant pools and short lists across all searches?"

#### Industry Context
Faculty recruitment follows the academic calendar: positions post in September-November, applications close in December-January, interviews happen in January-March, and offers go out in March-April for fall starts. Failed searches (no suitable candidate found) waste an entire year. Affirmative Action Plans require documenting outreach efforts, applicant pool demographics, and reasons for non-selection. OFCCP audits can request detailed hiring records. Spousal/partner accommodation ("dual career" hiring) is a major factor in recruiting to non-metro locations. International faculty require H-1B sponsorship with PERM labor certification — a complex, time-sensitive immigration process. Tenure-track hiring decisions effectively represent $3M–$5M lifetime institutional commitments.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Faculty Search Management System for a university HR department. Create a board called 'Faculty Searches AY 2026-27' with columns: Position Title (text), Department (dropdown: list major departments), College/School (dropdown), Search Committee Chair (people), HR Liaison (people), Position Type (dropdown: 'Tenure-Track', 'Tenured', 'Non-Tenure Track', 'Visiting', 'Clinical', 'Research'), Rank (dropdown: 'Assistant Professor', 'Associate Professor', 'Full Professor', 'Lecturer', 'Instructor'), Search Phase (status: 'Position Approval', 'Posting Active', 'Application Review', 'Long List', 'Short List', 'Phone/Video Interviews', 'Campus Visits', 'Reference Checks', 'Offer Pending Approval', 'Offer Extended', 'Offer Accepted', 'Failed Search', 'On Hold'), Posting Date (date), Application Deadline (date), Target Start Date (date), Total Applicants (numbers), Diverse Applicants Percent (numbers), Short List Count (numbers), Campus Visit Dates (date), EEO Report Filed (checkbox), Search Committee Diversity Met (checkbox), Budget Authorized (numbers), Salary Offer (numbers), H-1B Sponsorship Needed (checkbox), Dual Career Accommodation (checkbox), Search Plan (files), Notes (long text). Add automations: when Search Phase changes to 'Short List' and EEO Report Filed is unchecked, block phase change and notify HR Liaison; when Application Deadline arrives, notify Search Committee Chair to begin review; when Search Phase is unchanged for 21 days, notify HR Liaison and Dean's office; when Offer Accepted, create onboarding items on connected board. Create views: Kanban by Search Phase; Dashboard with searches by college, phase distribution, average time per phase, and diversity metrics; Timeline showing all searches from posting to target start date; Table filtered to 'Stalled' (no phase change in 21+ days)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Faculty Search Orchestrator
**Agent Purpose:** Manages the end-to-end faculty search process, ensures compliance at every stage, and keeps searches moving on the academic calendar.

**Triggers:**
- When a new search is created (Position Approval phase)
- When Search Phase changes (any transition)
- When a search has been in the same phase for more than 14 days
- When Application Deadline arrives
- Weekly: scan all active searches for compliance gaps and timeline risks

**Actions:**
- Generates phase-specific checklists for search committee chairs (what's needed to advance)
- Verifies EEO documentation completeness before allowing phase transitions
- Calculates applicant pool diversity metrics and flags pools that don't meet institutional targets
- Sends calendar-aware alerts ("You're 3 weeks past your application deadline with no long list — if you don't advance by March 1, you risk missing the hiring cycle")
- Drafts campus visit itineraries based on department templates and availability
- Generates comparative candidate summary matrices for search committee deliberation
- Monitors H-1B processing timelines for international candidates and flags deadlines

**Data Required:**
- Faculty search board data
- Institutional Affirmative Action Plan targets by department
- Academic calendar and search cycle benchmarks
- H-1B processing timeline data
- Historical search data (time per phase, success rates)

**Autonomy Level:** Human-in-the-Loop
Reminders, checklists, and timeline calculations are autonomous. Compliance flags block phase transitions until HR reviews. Candidate communications, offer letters, and any external-facing documents require HR Director approval.

**Example Interaction:**
> The Faculty Search Orchestrator notices that the Computer Science tenure-track search has been in the "Campus Visits" phase for 28 days with no movement. It checks the board and sees that two of three finalist visits are complete, but the third hasn't been scheduled. It sends a message to the search committee chair: "Your third finalist campus visit hasn't been scheduled, and we're now past March 15. Based on historical data, offers extended after April 1 have a 40% lower acceptance rate because top candidates are fielding competing offers. Can we schedule this visit within the next 10 days?" It also flags to the Dean's office that competing offers may be a factor and recommends pre-authorization of a competitive startup package to accelerate the offer once a finalist is selected. Separately, it notes that the selected finalist is an international candidate requiring H-1B sponsorship and calculates: "If offer accepted by April 15, PERM filing must begin by May 1 to ensure fall start. HR immigration team has been notified."

---

### Use Case 2: Employee Onboarding & Offboarding Workflow

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
University onboarding is exponentially more complex than corporate onboarding because of the diversity of employee types. A new tenure-track faculty member needs: appointment letter, I-9 verification, benefits enrollment, office/lab space assignment, IT account provisioning, library access, parking permit, key/card access, course assignments, committee assignments, faculty handbook acknowledgment, and enrollment in new faculty orientation. A new classified staff member has a completely different checklist: civil service paperwork, union orientation, probationary period tracking, and different benefits tiers. Student workers need FERPA training and work-study verification. Graduate assistants need tuition waiver processing and health insurance enrollment. No two employee categories onboard the same way — and HR coordinates with IT, Facilities, Parking, the hiring department, Payroll, and Benefits for every single hire. With 500–2,000 new hires per year, the manual coordination through email chains is unsustainable. New employees show up on day one without an email account, office keys, or payroll setup because someone in the chain dropped the ball.

#### The Solution
monday.com Work Management with templated onboarding workflows by employee type. When a new hire is confirmed, the appropriate template (faculty, staff, student worker, graduate assistant, postdoc) automatically generates a task board with all required actions, responsible parties, and due dates relative to the start date. Each department (IT, Facilities, Parking, Benefits, Payroll) sees only their tasks but updates feed a unified status view. Automations notify each team when their tasks are unblocked (e.g., IT gets notified to create the email account once HR confirms the hire in the HRIS). The hiring manager sees a real-time onboarding progress tracker. Offboarding uses the same approach in reverse: exit interview, equipment return, access revocation, benefits termination, final paycheck.

#### The Outcome
- 100% of new employees have all access, equipment, and accounts on day one
- 50% reduction in HR coordinator time spent on onboarding coordination
- Zero missed compliance steps (I-9, FERPA training, benefits enrollment deadlines)
- Consistent onboarding experience regardless of which HR coordinator is assigned

#### Discovery Questions
1. "How many new employees do you onboard annually, and how many different employee categories do you manage?"
2. "How often do new hires arrive on day one without their email account, office access, or payroll setup?"
3. "How do you coordinate between HR, IT, Facilities, and the hiring department during onboarding?"
4. "What's your I-9 compliance rate — are you ever completing them after the 3-day deadline?"
5. "How does offboarding work, particularly for access revocation when someone leaves?"

#### Industry Context
I-9 compliance is critical — federal law requires completion within 3 business days of employment start. Benefits enrollment windows are typically 30 days from hire date. At public universities, classified staff may have a 6-12 month probationary period with structured check-ins. Faculty onboarding includes mentoring assignments, tenure clock start dates, and startup package disbursement schedules. International employees require additional documentation (visa verification, SSN application, tax treaty forms). FERPA training is mandatory for anyone with access to student records. Background checks (criminal, education verification, sometimes credit) must clear before start date. Union-represented employees have specific orientation requirements per CBA.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Employee Onboarding System for a university. Create a board called 'New Employee Onboarding' with columns: Employee Name (text), Employee Type (dropdown: 'Faculty - Tenure Track', 'Faculty - Non-Tenure Track', 'Professional Staff', 'Classified Staff', 'Graduate Assistant', 'Postdoctoral Researcher', 'Student Worker'), Department (dropdown), Hiring Manager (people), HR Coordinator (people), Start Date (date), Onboarding Status (status: 'Pre-Arrival', 'Week 1', 'Month 1', 'Probation', 'Complete'), I-9 Complete (checkbox), Background Check (status: 'Pending', 'Clear', 'Flagged'), Benefits Enrolled (checkbox), Benefits Deadline (date), IT Account Created (checkbox), Building Access (checkbox), Parking Permit (checkbox), Office/Space Assigned (checkbox), FERPA Training (checkbox), Required Trainings Complete (checkbox), Orientation Attended (checkbox), Visa Type (dropdown: 'N/A', 'H-1B', 'J-1', 'TN', 'OPT', 'Other'), Union (dropdown: 'None', 'AFSCME', 'AAUP', 'UAW', 'SEIU', 'Other'), Payroll Active (checkbox), Day-One Readiness (formula: count of checkboxes checked / total checkboxes), Notes (long text). Create sub-items for each onboarding task with: Task (text), Responsible Team (dropdown: 'HR', 'IT', 'Facilities', 'Parking', 'Benefits', 'Payroll', 'Department', 'Training'), Due Date (date), Status (status: 'Pending', 'In Progress', 'Complete', 'Blocked'). Add automations: when a new item is created with Employee Type 'Faculty - Tenure Track', create sub-items from faculty onboarding template; when Start Date is 14 days away and I-9 Complete is unchecked, notify HR Coordinator urgently; when all sub-items are Complete, change Onboarding Status to 'Complete'. Create views: Dashboard with onboarding pipeline (chart), day-one readiness scores, overdue tasks by team, and upcoming start dates; Kanban by Onboarding Status; Calendar view by Start Date."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Onboarding Concierge
**Agent Purpose:** Orchestrates multi-department onboarding workflows, ensures no task is missed, and provides new employees and hiring managers with proactive status updates.

**Triggers:**
- When a new hire is added to the onboarding board
- Daily: scan all in-progress onboardings for overdue tasks
- When Start Date is 30, 14, 7, and 1 day(s) away
- When any onboarding task status changes
- When I-9 Complete remains unchecked within 2 days of Start Date

**Actions:**
- Generates the complete onboarding task list based on employee type, department, and union status
- Sends personalized welcome packets to new employees with pre-arrival checklists
- Notifies each responsible team (IT, Facilities, Parking) of their tasks with specific deadlines
- Escalates overdue tasks to the team supervisor (not just the assignee)
- Generates daily "Start Date Approaching" reports for HR coordinators showing readiness status
- Creates 30/60/90-day check-in reminders for hiring managers
- Handles offboarding in reverse: generates exit checklist, coordinates access revocation across all systems

**Data Required:**
- Onboarding board data
- Employee type-specific task templates
- Department contact information
- HRIS data for employee records
- Benefits enrollment deadlines and plan information
- Visa/immigration status and processing timelines

**Autonomy Level:** Escalation-Based
Task generation, reminders, and status tracking are fully autonomous. I-9 compliance alerts escalate to HR Director. Benefits enrollment issues escalate to Benefits Manager. Visa-related delays escalate to HR immigration specialist.

**Example Interaction:**
> A new assistant professor in Biology is set to start August 15. On August 1 (14 days out), the Onboarding Concierge runs a readiness check and finds: IT account ✅, Building access ✅, Office assigned ✅, Lab space ❌ (facilities hasn't confirmed), Parking permit ❌ (not requested), I-9 ❌ (new hire is relocating from another state — needs in-person verification), Benefits enrollment ❌ (packet sent but not returned), FERPA training ❌ (scheduled for orientation Aug 12). The agent sends the Facilities team an urgent request about lab space confirmation, pings the new hire directly: "Welcome to UState! Quick reminder — please bring your I-9 documents (passport or driver's license + Social Security card) to HR on your first day. Also, your benefits enrollment form is due by September 14 — would you like to schedule a benefits consultation call before you arrive?" It notifies the hiring manager: "Your new faculty member is 65% ready for day one. Two items need your attention: lab space (Facilities) and parking (not yet requested). I've escalated lab space — can you submit the parking request today?"

---

### Use Case 3: Promotion & Tenure (P&T) Process Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The promotion and tenure process is the most high-stakes, procedurally complex workflow in university HR. A single P&T case involves: the candidate assembling a dossier (CV, teaching evaluations, research publications, service record, external letters), the department committee review, the department chair recommendation, the college P&T committee review, the Dean's recommendation, the university P&T committee review, the Provost's recommendation, and the Board of Trustees final decision. Each level has specific deadlines, required document formats, and evaluation criteria. The process runs September through May and involves 50–150 cases annually at a large university. HR tracks these cases through spreadsheets, email, and physical file folders. Files go missing. Deadlines are missed. External review letters arrive late. A procedural error at any stage can result in a grievance, lawsuit, or AAUP sanction. HR staff spend hundreds of hours manually routing files, tracking deadlines, and chasing missing documents.

#### The Solution
monday.com Work Management to digitize the entire P&T workflow. Each candidate is an item that progresses through defined review stages. Sub-items track required documents (dossier components, external letters, committee votes, recommendation letters at each level). Automations route files to the next review level when the current level is complete, send deadline reminders to committee chairs, and flag cases where required documents are missing. Secure file storage for sensitive dossier materials with permission controls. Dashboards show the Provost's office the status of every case across all colleges. Timeline views show the full P&T calendar with stage-by-stage deadlines.

#### The Outcome
- Zero procedural errors in P&T cases (automated compliance checks at each stage)
- 40% reduction in HR administrative time managing the P&T process
- Complete audit trail for every case (grievance-proof documentation)
- Real-time visibility for Provost on all cases across the institution

#### Discovery Questions
1. "How many P&T cases do you manage annually, and how much HR staff time does the process consume?"
2. "Have you ever had a procedural error in a P&T case that led to a grievance or legal challenge?"
3. "How do you currently track external review letters — when they're requested, from whom, and whether they've arrived?"
4. "How does the Provost currently see the status of all P&T cases across colleges?"
5. "How do you ensure that committee recommendations and supporting documentation are complete before advancing to the next level?"

#### Industry Context
Tenure decisions are effectively permanent employment commitments — a denied tenure case can result in litigation costing $500K+. AAUP (American Association of University Professors) guidelines establish procedural standards. External review letters (typically 5-7 from peer scholars at other institutions) are confidential and legally sensitive. CBA provisions (at unionized institutions) specify exact timelines and procedures. "Tenure clock" typically runs 6 years from appointment. Extensions (for parental leave, medical leave, COVID) must be tracked precisely. Some institutions have "up or out" policies where denied tenure cases result in a terminal one-year contract. The P&T process is under increasing scrutiny for bias — tracking demographic data on outcomes is critical for equity analysis.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Promotion & Tenure Tracking System for a university. Create a board called 'P&T Cases AY 2026-27' with columns: Candidate Name (text), Department (dropdown), College (dropdown), Current Rank (dropdown: 'Assistant Professor', 'Associate Professor', 'Clinical Assistant', 'Research Assistant', 'Lecturer'), Action Requested (dropdown: 'Tenure', 'Promotion to Associate', 'Promotion to Full', 'Tenure + Promotion', 'Promotion - Non-Tenure Track'), Tenure Clock Year (numbers), Review Stage (status: 'Dossier Preparation', 'External Letters', 'Department Committee', 'Department Chair', 'College Committee', 'Dean', 'University Committee', 'Provost', 'Board', 'Complete - Approved', 'Complete - Denied', 'Withdrawn'), Stage Deadline (date), Dossier Complete (checkbox), External Letters Received (numbers), External Letters Required (numbers), Department Vote (text), Department Chair Recommendation (dropdown: 'Positive', 'Negative', 'Split'), College Committee Recommendation (dropdown: 'Positive', 'Negative', 'Split'), Dean Recommendation (dropdown: 'Positive', 'Negative'), University Committee Recommendation (dropdown: 'Positive', 'Negative', 'Split'), Provost Recommendation (dropdown: 'Positive', 'Negative'), Procedural Compliance (status: 'Compliant', 'Issue Flagged', 'Under Review'), HR Case Manager (people), Dossier (files), Confidential Letters (files), Committee Minutes (files), Notes (long text). Add automations: when Review Stage changes, update Stage Deadline based on institutional P&T calendar; when External Letters Received is less than External Letters Required and Stage Deadline is within 14 days, notify HR Case Manager; when Review Stage advances and Dossier Complete is unchecked, block advancement and notify HR; when Review Stage reaches 'Complete - Approved', send congratulations notification. Create views: Kanban by Review Stage; Dashboard with cases by college, stage distribution, approval rates, and timeline compliance; Calendar showing all stage deadlines."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Tenure Track Guardian
**Agent Purpose:** Manages the procedural integrity of every P&T case, ensures deadlines are met, and provides an unbreakable audit trail.

**Triggers:**
- When a new P&T case is added to the board
- When Review Stage changes (any transition)
- When Stage Deadline is within 14, 7, and 3 days
- When External Letters Received changes
- Weekly during P&T season (September–May): comprehensive compliance scan

**Actions:**
- Validates that all required documents are present before allowing stage transitions
- Tracks external review letter status (requested, received, overdue) and sends follow-up requests
- Generates stage-specific checklists for committee chairs (required actions, evaluation criteria, deadlines)
- Creates a procedural compliance audit log for every action taken on every case
- Produces anonymized aggregate reports on P&T outcomes by department, gender, and race/ethnicity for equity analysis
- Alerts HR Director immediately if any procedural deviation is detected
- Generates Board of Trustees summary dossiers for final approval

**Data Required:**
- P&T board data (all case details)
- Institutional P&T policy and calendar
- CBA provisions (if applicable) for unionized faculty
- Historical P&T outcome data for equity analysis
- External reviewer contact database

**Autonomy Level:** Human-in-the-Loop
Reminders, checklists, and audit logging are autonomous. Procedural compliance flags require HR Director review before the case can advance. Any communication with P&T candidates goes through the department chair (never direct from the system). Equity analysis reports go to the Provost's office for review before distribution.

**Example Interaction:**
> The Tenure Track Guardian detects that Dr. Park's tenure case in the English Department has received only 3 of 5 required external review letters, and the Department Committee deadline is in 18 days. Two letters were requested 8 weeks ago from reviewers at peer institutions but haven't arrived. The agent sends a reminder to the department chair: "Dr. Park's external letters: 3 of 5 received. Outstanding: Prof. Williams (UC Berkeley, requested Oct 1) and Prof. Nakamura (Michigan, requested Oct 3). Per policy, the department committee cannot convene without at least 5 letters. Recommend follow-up with both reviewers this week. If either is unable to complete, you'll need to identify a replacement reviewer — which adds approximately 4-6 weeks. Shall I draft follow-up emails?" It simultaneously logs this interaction in the audit trail and flags the case as "At Risk — External Letters" on the dashboard.

---

### Use Case 4: Position Management & Classification

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Universities manage thousands of positions across dozens of job classifications — each with specific pay grades, minimum qualifications, and reporting structures. When a department wants to create a new position, reclassify an existing one, or modify a job description, the process involves multiple approvals (department head → Dean/VP → HR Classification → Budget Office → sometimes Provost or President). At public universities, state civil service rules add another layer. HR classification specialists spend enormous time reviewing job descriptions against classification standards, conducting salary equity analyses, and ensuring FLSA exemption status is correct. The process takes 4–12 weeks, frustrating departments that need to hire. Meanwhile, position data lives in Banner/PeopleSoft, organizational charts are maintained manually in Visio or PowerPoint, and no one has a real-time view of institutional headcount, vacancies, or position budget.

#### The Solution
monday.com Work Management for position lifecycle management. A position management board tracks every position from creation through classification, approval, posting, filling, and eventual vacancy. Columns capture classification details (pay grade, FLSA status, job family, EEO category), reporting relationships, budget source, and approval status. When a department submits a position request via form, it automatically routes through the approval chain with all required information. Classification specialists use the board to track their review queue and turnaround times. Dashboards show institutional headcount, vacancy rates, positions pending classification, and budget impact.

#### The Outcome
- 50% reduction in position classification turnaround time (from 8 weeks to 4 weeks)
- Real-time institutional headcount and vacancy visibility for leadership
- Standardized position request process across all departments
- Automated FLSA compliance checks during classification

#### Discovery Questions
1. "How many position actions (new, reclassification, modification) do you process annually?"
2. "What's your average turnaround time for a position classification, and what causes delays?"
3. "How do you maintain your institutional org chart, and how current is it?"
4. "How does your VP for Finance/CFO currently see total headcount and vacancy data?"
5. "Have you ever had an FLSA misclassification issue, and how do you currently verify exemption status?"

#### Industry Context
CUPA-HR (College and University Professional Association for Human Resources) provides salary survey data that drives higher ed compensation benchmarking. Public universities must comply with state classification systems (e.g., state civil service job classifications). FLSA exemptions in higher ed have specific nuances: the "teacher" exemption applies broadly to faculty, but instructional staff who primarily perform non-teaching duties may not qualify. The DOL has historically scrutinized higher ed for FLSA violations among adjuncts, postdocs, and administrative staff. Position budgeting ties to the annual budget cycle — new positions typically require inclusion in the next fiscal year budget unless funded by grants or gifts.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Position Management System for a university HR department. Create a board called 'Position Management' with columns: Position Number (text), Position Title (text), Department (dropdown), College/Division (dropdown), Supervisor Position (connect boards), Action Type (dropdown: 'New Position', 'Reclassification', 'Title Change', 'Reporting Change', 'Elimination'), Employee Category (dropdown: 'Faculty', 'Professional Staff', 'Classified Staff', 'Temporary', 'Student'), Pay Grade (dropdown: grades G1-G20), Salary Range Min (numbers), Salary Range Mid (numbers), Salary Range Max (numbers), FLSA Status (dropdown: 'Exempt', 'Non-Exempt'), EEO Category (dropdown), FTE (numbers), Funding Source (dropdown: 'Operating', 'Grant', 'Gift', 'Auxiliary', 'Mixed'), Annual Cost (numbers), Classification Status (status: 'Submitted', 'Under Review', 'Pending Comp Analysis', 'Pending Budget Approval', 'Approved', 'Rejected', 'On Hold'), Requested By (people), HR Classifier (people), Date Submitted (date), Date Completed (date), Turnaround Days (formula), Job Description (files), Classification Rationale (long text), Budget Approval (checkbox). Add automations: when Action Type is 'New Position' and Classification Status changes to 'Approved', create a connected item on the Faculty Searches or Staff Recruitment board; when Date Submitted is more than 30 days ago and Classification Status is 'Under Review', escalate to HR Director; when FTE changes, recalculate Annual Cost. Create views: Dashboard with positions by action type, average turnaround days, positions by division, and budget impact; Table filtered to 'Under Review' for classification queue; Kanban by Classification Status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Classification Accelerator
**Agent Purpose:** Streamlines position classification by pre-analyzing job descriptions, suggesting classifications, and managing the approval workflow.

**Triggers:**
- When a new position request is submitted (form or item creation)
- When a job description file is uploaded
- When Classification Status is unchanged for more than 10 business days
- Monthly: analyze classification queue metrics and identify process bottlenecks
- When CUPA-HR salary data is updated (annual)

**Actions:**
- Pre-screens job descriptions against classification standards and suggests pay grade, FLSA status, and EEO category
- Conducts automated salary equity analysis comparing proposed salary to internal peers and CUPA-HR benchmarks
- Routes approvals sequentially through the chain with escalation if any approver doesn't respond within 5 business days
- Generates classification rationale documentation for HR classifier review
- Flags potential FLSA misclassification risks based on job duty analysis
- Produces monthly classification metrics report (volume, turnaround, backlog)

**Data Required:**
- Position management board data
- Institutional classification standards and pay grade structures
- CUPA-HR salary survey data
- FLSA exemption criteria and DOL guidance
- Historical classification decisions for consistency checks

**Autonomy Level:** Human-in-the-Loop
Pre-screening, routing, and metrics are autonomous. Classification recommendations require HR classifier confirmation. FLSA determinations must be reviewed by HR Director. Budget impact assessments require CFO approval for positions over $100K.

**Example Interaction:**
> The Biology Department submits a request for a new "Research Data Scientist" position. The Classification Accelerator analyzes the job description and recommends: Pay Grade G14 ($78,000–$102,000), FLSA Exempt (professional exemption — primary duties involve advanced data analysis requiring specialized knowledge), EEO Category 2 (Professional). It runs a CUPA-HR benchmark and notes: "Median salary for 'Data Scientist' at doctoral institutions is $95,400. The proposed salary of $85,000 is at the 35th percentile — may be below market for competitive recruitment. Recommend midpoint ($90,000) or above." It also flags: "You have an existing 'Senior Research Analyst' classification at G13 in the Chemistry Department with 70% duty overlap. Consider whether this new position should be classified consistently or differentiated based on the machine learning requirement." The HR classifier reviews the recommendation, adjusts the grade to G15 based on the ML specialization, and approves. The system automatically routes to Budget Office for funding confirmation.

---

### Use Case 5: Leave Management & FMLA/ADA Compliance Tracking

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Universities manage complex leave programs across multiple employee categories — each with different accrual rates, types, and eligibility rules. Faculty have sabbaticals (one semester at full pay or one year at half pay, typically after 6 years), research leaves, and course release arrangements. Staff have vacation, sick, personal, and FMLA leave, with different accrual rates for classified vs. professional employees. Graduate assistants may have limited leave. Public universities must comply with state leave laws (which vary enormously). FMLA tracking is particularly complex: determining eligibility (1,250 hours worked, 12 months employed, 50+ employees within 75 miles — the last criterion is tricky for multi-campus institutions), tracking intermittent leave, and managing the return-to-work process. ADA accommodation requests require an interactive process with documentation. HR manages all of this through spreadsheets and email, creating significant compliance risk — an FMLA violation can result in personal liability for HR professionals.

#### The Solution
monday.com Work Management for centralized leave tracking and compliance. A leave case board where each leave request becomes an item with type, eligibility verification, approval status, duration tracking, and return-to-work management. FMLA cases include detailed tracking of entitlement used (480 hours), intermittent leave usage, and medical certification deadlines. ADA cases track the interactive process steps, accommodation requests, and implementation. Automations enforce deadlines (FMLA designation within 5 business days, medical certification within 15 days), alert when entitlement is running low, and manage the return-to-work process. Sabbatical tracking uses a separate board showing the full faculty sabbatical cycle.

#### The Outcome
- 100% FMLA/ADA procedural compliance (automated deadline enforcement)
- 60% reduction in leave administration time through automation
- Real-time leave balance and usage visibility for supervisors and HR
- Complete audit trail for every leave case (litigation protection)

#### Discovery Questions
1. "How many FMLA cases do you manage annually, and how do you track intermittent leave usage?"
2. "How do you currently determine FMLA eligibility for employees at satellite campuses or multi-location positions?"
3. "What's your ADA interactive process look like, and how do you document it?"
4. "How do faculty sabbatical requests flow from department through Provost approval?"
5. "Have you ever had a leave-related compliance issue or legal claim?"

#### Industry Context
FMLA provides 12 weeks unpaid leave for qualifying events; universities also often have paid parental leave policies and paid medical leave exceeding FMLA minimums. Many public universities have separate sick leave banks and catastrophic leave programs. Faculty sabbaticals are governed by institutional policy and often require a post-sabbatical service commitment (typically one year). The ADA interactive process requires good-faith engagement with the employee to identify reasonable accommodations — documentation of this process is critical in litigation. Workers' compensation intersects with FMLA when injuries occur. Multi-campus universities face complex FMLA eligibility calculations. Tenure-clock extensions for qualifying leaves add another tracking dimension.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Leave Management & Compliance Tracker for university HR. Create a board called 'Leave Cases' with columns: Employee Name (text), Employee ID (text), Employee Type (dropdown: 'Faculty', 'Professional Staff', 'Classified Staff', 'Graduate Assistant'), Department (dropdown), Leave Type (dropdown: 'FMLA - Continuous', 'FMLA - Intermittent', 'ADA Accommodation', 'Sabbatical', 'Medical Leave', 'Parental Leave', 'Personal Leave', 'Military Leave', 'Workers Comp', 'Bereavement'), Case Status (status: 'Request Received', 'Eligibility Review', 'Approved', 'Active', 'Return to Work', 'Closed', 'Denied'), HR Case Manager (people), Supervisor (people), FMLA Eligible (checkbox), FMLA Hours Used (numbers), FMLA Hours Remaining (numbers), Leave Start Date (date), Expected Return Date (date), Actual Return Date (date), Medical Cert Received (checkbox), Medical Cert Due Date (date), Designation Notice Sent (checkbox), Designation Due Date (date), ADA Interactive Process (status: 'N/A', 'Initiated', 'Meeting Scheduled', 'Accommodation Identified', 'Implemented', 'Follow-up'), Accommodation Details (long text), Documentation (files), Notes (long text). Add automations: when Case Status changes to 'Request Received', set Designation Due Date to 5 business days from today; when Medical Cert Due Date is within 3 days and Medical Cert Received is unchecked, notify HR Case Manager urgently; when FMLA Hours Remaining falls below 40, notify HR Case Manager and Supervisor; when Expected Return Date is within 7 days, create 'Return to Work' checklist items. Create views: Dashboard with active cases by type, FMLA entitlement usage chart, overdue compliance actions, and cases by department; Table filtered to compliance deadline items; Calendar view of expected return dates."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Leave Compliance Sentinel
**Agent Purpose:** Ensures every leave case meets federal, state, and institutional compliance requirements with zero missed deadlines.

**Triggers:**
- When a new leave case is created
- When compliance deadlines approach (Designation Notice, Medical Certification, Response deadlines)
- When FMLA hours usage changes (intermittent leave tracking)
- Daily: scan all active cases for overdue actions
- When Expected Return Date arrives

**Actions:**
- Automatically determines FMLA eligibility based on employee data (hire date, hours worked, location)
- Generates required notices (Eligibility Notice, Designation Notice, Rights & Responsibilities) with correct deadlines
- Tracks intermittent FMLA usage and calculates remaining entitlement in real-time
- Manages the ADA interactive process: schedules meetings, documents discussions, tracks accommodation implementation
- Generates return-to-work checklists with fitness-for-duty certification requirements
- Creates monthly compliance reports for HR Director showing case volumes, compliance rates, and risk areas
- Flags cases approaching the 12-week FMLA limit for transition planning

**Data Required:**
- Leave case board data
- HRIS employee data (hire date, hours worked, location, employment status)
- FMLA eligibility criteria and institutional leave policies
- ADA interactive process requirements
- State-specific leave law requirements

**Autonomy Level:** Escalation-Based
Eligibility determinations, notice generation, and deadline tracking are autonomous. ADA accommodation decisions require HR Director involvement. Leave denials require HR Director and legal counsel review. Any case involving potential litigation risk is immediately escalated.

**Example Interaction:**
> An employee in the Admissions Office requests FMLA leave for a serious health condition. The Leave Compliance Sentinel immediately runs eligibility: employed 3 years ✅, 1,250+ hours in past 12 months ✅, works at main campus (5,000+ employees within 75 miles) ✅. It generates the Eligibility Notice (due to employee within 5 business days) and Rights & Responsibilities notice, sets the medical certification deadline (15 calendar days from notice), and notifies the HR Case Manager: "New FMLA case — eligible. Notices generated and ready for your review before sending. Medical certification due by March 5. Supervisor has been notified of the employee's approved leave status (without medical details, per HIPAA)." Two weeks later, the employee requests intermittent leave (2 hours, 3x per week for physical therapy). The agent recalculates: "At 6 hours/week intermittent usage, this employee's 480-hour FMLA entitlement will be exhausted in approximately 80 weeks — well within the 12-month period. Current usage: 42 hours (8.75%). Tracking intermittent absences automatically."

---

### Use Case 6: Employee Relations Case Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
University employee relations teams handle a constant flow of complaints, grievances, disciplinary actions, workplace investigations, and conflict mediations. Cases range from performance improvement plans (PIPs) for underperforming staff to Title IX complaints involving faculty, union grievances under CBAs with strict procedural timelines, harassment allegations requiring formal investigations, and workplace safety concerns. Each case type has different procedures, timelines, documentation requirements, and escalation paths. At unionized institutions, grievance procedures specify exact response deadlines — miss one and the university may default. Employee relations specialists manage 30-80 active cases simultaneously, tracked in confidential spreadsheets or sometimes paper files. There's no systematic way to identify patterns (e.g., a department with 5x the complaint rate) or ensure procedural consistency.

#### The Solution
monday.com Work Management with strict permission controls for confidential employee relations case tracking. Each case is an item with classification, involved parties, investigation status, timeline milestones, and resolution. CBA-governed grievances have automated deadline tracking that accounts for business days and specific contract timelines. Investigation workflows follow a structured template: intake → preliminary assessment → investigation plan → witness interviews → findings → recommendation → resolution. Pattern analytics dashboards (anonymized) show case volumes by type, department, and outcome — helping HR leadership identify systemic issues.

#### The Outcome
- Zero missed grievance deadlines (critical for union relations)
- Consistent investigation procedures across all case types
- Pattern identification enables proactive intervention in problem areas
- Complete, organized case files for legal proceedings when needed

#### Discovery Questions
1. "How many employee relations cases do you manage annually, and what's the breakdown by type?"
2. "How do you currently track CBA grievance deadlines, and have you ever missed one?"
3. "Can you identify which departments or managers generate the most complaints?"
4. "How do you ensure investigation procedures are consistent across different HR generalists?"
5. "How do you manage the confidentiality requirements while still enabling oversight and pattern analysis?"

#### Industry Context
University employee relations is complicated by tenure protections (terminating a tenured faculty member requires extraordinary circumstances and extensive due process), CBA grievance procedures (often involving multi-step processes with union representation), Title IX requirements (mandatory reporting, investigation timelines, and due process for respondents), and shared governance norms. Progressive discipline for classified staff follows civil service procedures at public institutions. Academic freedom claims complicate disciplinary actions involving faculty speech or research. Clery Act requires timely reporting of certain incidents. State whistleblower protections apply to employees reporting waste, fraud, or abuse.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Employee Relations Case Management System for a university. Create a board called 'Employee Relations Cases' (set board permissions to restrict access to HR Employee Relations team only). Columns: Case Number (auto-number), Case Type (dropdown: 'Performance Issue', 'Grievance - CBA', 'Harassment Complaint', 'Discrimination Complaint', 'Workplace Conflict', 'Policy Violation', 'Title IX', 'Whistleblower', 'Workplace Safety', 'Other'), Confidentiality Level (status: 'Standard', 'Sensitive', 'Highly Sensitive'), Complainant Department (dropdown), Respondent Department (dropdown), Assigned Investigator (people), Date Received (date), Investigation Status (status: 'Intake', 'Preliminary Assessment', 'Active Investigation', 'Witness Interviews', 'Findings Draft', 'Management Review', 'Resolution', 'Closed', 'Referred to Legal'), Next Deadline (date), Deadline Type (text), Resolution Type (dropdown: 'Substantiated - Action Taken', 'Unsubstantiated', 'Mediated', 'Withdrawn', 'Referred', 'Ongoing Monitoring'), Grievance Step (dropdown: 'N/A', 'Step 1 - Informal', 'Step 2 - Written', 'Step 3 - Hearing', 'Step 4 - Arbitration'), CBA Deadline (date), Days Open (formula: today minus Date Received), Documentation (files), Case Summary (long text). Add automations: when CBA Deadline is within 3 days and Investigation Status is not 'Resolution' or 'Closed', send urgent alert to Assigned Investigator and HR Director; when Days Open exceeds 60 and Investigation Status is 'Active Investigation', notify HR Director; when Case Type is 'Title IX', auto-assign to Title IX coordinator. Create views: Dashboard with cases by type (anonymized), average days to resolution, open cases by investigator, and department heat map; Table filtered to 'Grievance - CBA' showing all CBA deadlines; Kanban by Investigation Status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Case Timeline Enforcer
**Agent Purpose:** Ensures every employee relations case meets procedural deadlines, maintains documentation standards, and identifies institutional patterns.

**Triggers:**
- When a new case is created
- When any deadline is within 5, 3, and 1 business day(s)
- When Investigation Status changes
- When a CBA grievance is filed (immediate trigger for deadline calculation)
- Monthly: pattern analysis across all cases

**Actions:**
- Calculates all applicable deadlines based on case type and CBA provisions (accounting for business days, holidays)
- Generates investigation plan templates based on case type and complexity
- Sends deadline alerts with escalating urgency to investigator and HR Director
- Produces anonymized quarterly reports showing case patterns by department, type, and outcome
- Flags departments with statistically significant complaint rates for proactive intervention
- Generates case closure summaries with all required documentation checklists

**Data Required:**
- Employee relations board data
- Collective bargaining agreement deadline provisions
- Title IX procedural requirements
- Institutional policies on progressive discipline, harassment, and discrimination
- Historical case data for pattern analysis

**Autonomy Level:** Human-in-the-Loop
Deadline calculations and alerts are autonomous. Investigation plans are generated for investigator review. Pattern analysis reports are reviewed by HR Director before distribution. All case determinations require human decision-making — the agent supports but never decides outcomes.

**Example Interaction:**
> A Step 2 grievance is filed by the AFSCME union on behalf of a custodial employee alleging unjust discipline. The Case Timeline Enforcer immediately calculates CBA deadlines: management response to Step 2 grievance is due within 10 business days (by March 3). It creates a case with all CBA-mandated steps pre-populated, assigns it to the senior employee relations specialist, and generates a checklist: "Step 2 Grievance Filed: (1) Acknowledge receipt to union steward within 2 business days ✅ auto-sent, (2) Gather relevant documentation (performance records, incident reports, witness statements) by Feb 25, (3) Schedule Step 2 meeting with employee, union steward, and supervisor by Feb 27, (4) Issue written response by March 3." It also runs a quick pattern check: "This is the 4th grievance from the Facilities Services department this academic year — 2.5x the institutional average. Previous grievances: 2 substantiated, 1 unsubstantiated. Consider recommending supervisory training for Facilities management."

---

### Use Case 7: Training & Professional Development Tracking

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Universities require extensive mandatory training across the workforce: Title IX awareness, FERPA compliance, cybersecurity awareness, Clery Act reporting, hazardous materials handling (for lab workers), defensive driving (for fleet vehicle users), blood-borne pathogens (for healthcare workers), and DEI training. Additionally, professional development programs include supervisory training for new managers, leadership academies for emerging leaders, and faculty development workshops. HR is responsible for tracking completion across thousands of employees with different requirements based on role, department, and job function. Current tracking lives in the LMS (Cornerstone, Blackboard) for online courses, but in-person workshops, conference attendance, and certification renewals are tracked in spreadsheets. Compliance audits reveal gaps that create institutional liability. Supervisors can't easily see which of their employees are out of compliance.

#### The Solution
monday.com Work Management as the central training compliance dashboard that aggregates data from the LMS and tracks additional development activities. Each employee's training requirements are mapped based on their role and department. A compliance board shows completion status across all mandatory trainings with automated reminders for renewals. A professional development board tracks workshop attendance, conference participation, certification progress, and development goals. Supervisors get a team dashboard showing their employees' compliance status and development activities.

#### The Outcome
- 95%+ mandatory training compliance rate (up from 70-80%)
- Automated renewal tracking eliminates expired certifications
- Supervisor visibility into team compliance without HR manually generating reports
- Development activity tracking supports annual performance review conversations

#### Discovery Questions
1. "What mandatory trainings are required across your workforce, and what's your current compliance rate?"
2. "How do you track which employees need which trainings based on their role?"
3. "How do supervisors currently know if their team members are up to date on required training?"
4. "Do you track professional development activities beyond mandatory compliance training?"
5. "How do you handle training requirements that change — for example, when a new state mandate adds a training requirement?"

#### Industry Context
Title IX training is mandatory for all employees and typically must be renewed annually. FERPA training is required for anyone accessing student records. Clery Act requires Campus Security Authorities (CSAs) to understand reporting obligations. Lab safety training (OSHA compliance) is critical for research institutions. IRB training (CITI certification) is required for researchers working with human subjects. Many states require sexual harassment prevention training with specific content and duration requirements. Accreditors may ask for evidence of systematic professional development programs. Faculty development often falls under the Provost's office rather than HR, creating coordination challenges.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Training Compliance & Development Tracker for university HR. Create a board called 'Training Compliance' with columns: Employee Name (text), Employee ID (text), Department (dropdown), Employee Type (dropdown), Supervisor (people), Training Name (text), Training Category (dropdown: 'Title IX', 'FERPA', 'Cybersecurity', 'Clery Act', 'Lab Safety', 'Hazmat', 'Blood-borne Pathogens', 'Defensive Driving', 'DEI', 'Supervisory', 'IRB/CITI', 'ADA Awareness', 'Other Mandatory', 'Professional Development'), Required (checkbox), Completion Status (status: 'Not Started', 'In Progress', 'Completed', 'Expired', 'Exempt'), Completion Date (date), Expiration Date (date), Renewal Cycle Months (numbers), Next Due Date (date), Delivery Method (dropdown: 'Online - LMS', 'In-Person Workshop', 'Conference', 'Webinar', 'Self-Study'), Certificate (files), Notes (long text). Add automations: when Expiration Date is within 30 days and Completion Status is 'Completed', change status to 'Expired' notification sent to employee and supervisor; when Next Due Date arrives, change Completion Status to 'Not Started' and notify employee; quarterly, generate compliance report for HR Director. Create views: Dashboard with compliance rate by training category, overdue trainings by department, completion trend over time; Table filtered to 'Expired' or 'Not Started' where Required is checked (non-compliant employees); Team view grouped by Supervisor."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Compliance Training Tracker
**Agent Purpose:** Ensures all employees complete required training on time and identifies compliance gaps before they become audit findings.

**Triggers:**
- When a new employee is added (onboarding integration)
- When an employee's role or department changes (triggers new training requirements)
- When training completion dates approach expiration
- Monthly: institutional compliance rate scan
- When a new mandatory training requirement is added

**Actions:**
- Automatically assigns required trainings based on employee type, department, and job function
- Sends personalized training reminders with direct links to LMS courses
- Generates non-compliance reports by department for supervisors and HR
- Calculates institutional compliance rates by training category for accreditation reporting
- Identifies employees with role changes who need new training assignments
- Produces annual professional development summaries for performance review season

**Data Required:**
- Training compliance board data
- HRIS employee data (role, department, hire date)
- LMS completion data (integration with Cornerstone/Canvas/Blackboard)
- Training requirement matrix by role/department
- Accreditation requirements for training documentation

**Autonomy Level:** Fully Autonomous
Training assignments, reminders, and compliance reporting run without human intervention. New mandatory training requirement additions require HR Director confirmation before mass-assignment.

**Example Interaction:**
> The Compliance Training Tracker runs its monthly scan and finds that the Chemistry Department has a 58% compliance rate on Lab Safety training — the lowest on campus and below the 90% institutional target. It drills down: 12 of 29 lab-eligible employees have expired certifications, including 3 Principal Investigators whose OSHA-required training expired 60+ days ago. It sends the department chair a summary: "12 Chemistry employees have expired Lab Safety training. This creates OSHA compliance risk — particularly for the 3 PIs whose labs would be non-compliant during an inspection. The next available in-person Lab Safety refresher is March 15. I've pre-registered all 12 employees and sent them calendar invitations. Please confirm these registrations or provide alternatives for anyone unavailable on March 15." It simultaneously alerts the Environmental Health & Safety office and adds this to the HR Director's monthly compliance report.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Tenure | Permanent employment status for faculty, granted after a probationary period (usually 6 years), providing strong protection against termination |
| Tenure Track | Probationary period for faculty leading toward a tenure decision; "tenure-track assistant professor" is the typical entry point |
| P&T | Promotion and Tenure — the formal review process for faculty career advancement |
| Adjunct | Part-time, non-tenure-track faculty hired on a per-course or semester basis |
| Classified Staff | Non-exempt, often unionized employees in defined civil service job classifications (custodial, clerical, technical) |
| Professional Staff | Exempt administrative employees not covered by civil service or faculty governance |
| CBA | Collective Bargaining Agreement — the contract between the university and a labor union |
| AAUP | American Association of University Professors — sets standards for academic governance and faculty rights |
| CUPA-HR | College and University Professional Association for Human Resources — provides salary surveys and HR benchmarking data |
| FERPA | Family Educational Rights and Privacy Act — protects student education records; training required for all with access |
| Title IX | Federal law prohibiting sex-based discrimination in education; requires institutional compliance infrastructure |
| Sabbatical | Extended leave (typically one semester at full pay or one year at half pay) for faculty research and professional renewal |
| Faculty Handbook | Institutional document governing faculty rights, responsibilities, and procedures — functions as an employment contract |
| Shared Governance | Model where faculty participate in institutional decision-making through senates and committees |
| H-1B | Non-immigrant visa category for specialty occupation workers; universities are cap-exempt for H-1B petitions |
| PERM | Program Electronic Review Management — DOL process for employer-sponsored permanent residency (green card) |
| I-9 | Employment Eligibility Verification form required for all new hires within 3 business days |
| Clery Act | Federal law requiring campus crime reporting and security policy disclosure |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CHRO / VP for Human Resources | Leads HR strategy, labor relations, and compliance | Decision-maker |
| Provost / VP Academic Affairs | Oversees faculty HR matters (appointments, P&T, sabbaticals) | Decision-maker (faculty HR) |
| Associate VP for HR | Day-to-day HR operations management | Decision-maker / Champion |
| Director of Employee Relations | Manages complaints, grievances, investigations, and labor relations | Influencer |
| Director of Compensation & Classification | Manages job classifications, pay structures, and FLSA compliance | Influencer |
| HR Business Partners / Generalists | Embedded HR support for specific colleges or divisions | User / Champion |
| Benefits Manager | Administers health insurance, retirement, leave programs | User |
| Title IX Coordinator | Manages Title IX compliance, investigations, and training | Influencer |
| Union Representatives | Represent employee interests in CBA negotiations and grievances | External Influencer |
| Deans & Department Chairs | Initiate faculty searches, P&T cases, and position requests | User / Decision-maker (within unit) |
| CFO / VP for Finance | Approves position budgets and compensation changes | Decision-maker |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| PMO | HR initiatives (ERP implementation, benefits open enrollment) are PMO projects | Cross-board visibility between HR projects and institutional project portfolio |
| IT | HRIS management, system integrations, employee provisioning | IT manages the systems HR depends on; shared workflow for onboarding tech access |
| Finance | Payroll, position budgeting, compensation cost modeling | Budget boards connected to position management for real-time fiscal impact |
| Legal / General Counsel | Employee relations cases, grievance arbitration, compliance guidance | Case management integration for escalated employee relations matters |
| Academic Affairs | Faculty appointments, P&T, sabbaticals, workload | Faculty HR processes bridge HR and Academic Affairs constantly |
| Diversity, Equity & Inclusion | Affirmative action plans, climate surveys, bias training | DEI initiatives tracked alongside HR compliance and training programs |
| Facilities | Space allocation for new hires, office moves, workplace safety | Onboarding coordination and workplace accommodation implementation |
| Research Administration | Postdoc employment, graduate assistant appointments, visa sponsorship | Research employee HR needs are specialized and high-volume |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| PeopleAdmin / PageUp | Higher ed-specific applicant tracking and position management | monday.com provides broader workflow management beyond just applicant tracking; can integrate with or replace manual processes around PeopleAdmin |
| Banner HR (Ellucian) | Core HRIS/ERP — system of record for employee data, payroll, benefits | monday.com doesn't replace Banner but solves the workflow, tracking, and collaboration gaps Banner can't fill (P&T tracking, case management, onboarding coordination) |
| Workday HCM | Modern cloud HR platform replacing Banner at some institutions | Workday excels at transactions; monday.com excels at processes (searches, P&T, investigations) that require collaboration and workflow |
| Cornerstone OnDemand | Learning management and talent management | monday.com can serve as the compliance dashboard aggregating LMS data with non-LMS training tracking |
| ServiceNow HR | IT-centric HR service delivery | monday.com is more user-friendly for non-technical HR teams and easier to configure without IT dependency |
| Spreadsheets / Email | The actual incumbent for most university HR processes | monday.com replaces error-prone manual tracking with automated, auditable workflows |
| Interfolio | Faculty-specific: search, review, and dossier management | Interfolio is strong for P&T dossiers but lacks the broader HR workflow capabilities; monday.com can manage the full process while Interfolio handles document assembly |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Banner/Workday for HR" | "Banner and Workday are your system of record — they're great at storing employee data and running payroll. But do they manage your faculty search process? Track your P&T cases? Coordinate onboarding across 6 departments? monday.com handles the workflows and collaboration that your HRIS wasn't designed for." |
| "HR data is sensitive — we can't put it in another system" | "Absolutely right to be cautious. monday.com offers enterprise-grade security (SOC 2 Type II, HIPAA-eligible), granular board-level permissions, and audit logging. Your employee relations board can be restricted to only the ER team. We can configure access controls that are actually more restrictive than your current spreadsheet-based tracking." |
| "Our union will object to new tracking systems" | "This isn't surveillance — it's actually better for employees and unions. Automated grievance deadline tracking protects employee rights by ensuring the university never misses a response deadline. Transparent onboarding checklists mean new employees actually get what they need on day one. The union should welcome a system that enforces procedural compliance." |
| "We don't have budget for this" | "What does a single FMLA compliance violation cost? A failed faculty search that wastes a year? An accreditation finding on inadequate training documentation? University HR departments spend millions in hidden costs from manual, error-prone processes. monday.com's license cost is a fraction of one avoided legal settlement." |
| "HR staff are too busy to learn a new system" | "That's exactly the point — your team is drowning in manual tracking. The implementation starts with your highest-pain process (often onboarding or faculty searches) and automates the administrative work that's consuming your time. Most HR teams see 20-30% time savings within 90 days of launch on their first use case." |
| "We need something higher-ed specific, not generic" | "monday.com is a platform you configure to match your exact processes — your P&T stages, your CBA grievance steps, your position classification workflow. The boards we build will use your terminology, your deadlines, and your approval chains. It's not a generic template; it's your processes, digitized and automated." |

## Proof Points
*(To be populated with customer references)*
- [University HR department managing faculty search processes]
- [Higher ed institution tracking P&T cases on monday.com]
- [University using monday.com for employee onboarding coordination]
- [College/university managing training compliance across workforce]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
