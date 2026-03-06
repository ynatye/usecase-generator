# Colleges & Universities × Customer Success Playbook

## Overview

In higher education, "Customer Success" doesn't carry a traditional SaaS label — but the function exists under names like Student Success, Enrollment Management, Student Retention, Academic Advising, and Student Experience. These teams are laser-focused on ensuring students persist from enrollment through graduation (and beyond into alumni engagement). The "customer" is the student, and "churn" is dropout — an outcome that costs institutions $15,000–$50,000+ in lost tuition per student and devastates completion rates that increasingly drive state funding formulas and rankings.

Student success operations at mid-to-large universities involve dozens of touchpoints: academic advising, early alert systems, tutoring centers, financial aid counseling, mental health referrals, career services, first-year experience programs, and transfer student support. These functions typically span multiple divisions — Academic Affairs, Student Affairs, Enrollment Management — creating coordination challenges. A student struggling in calculus, missing financial aid deadlines, and skipping meals may be flagged by three different systems (LMS, financial aid portal, dining card) without anyone connecting the dots. The institution that connects those signals saves that student.

The data-driven student success movement has grown dramatically, fueled by predictive analytics platforms (Civitas/Watermark, EAB Navigate, Starfish/Hobsons) and completion-based funding models in 35+ states. Yet many institutions still rely on fragmented interventions — an advisor here, a tutor there — without systematic workflow management. The gap isn't analytics (knowing who's at risk) but operations (ensuring the right intervention reaches the right student at the right time). This is where monday.com fills a critical void: not replacing the predictive engine, but operationalizing the response.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Advisor-to-student ratios of 1:300-800 mean institutions must systematically scale interventions without proportionally scaling staff |
| 2 | Replace or Radically Augment Headcount | High | Manual early alert triage, case management follow-ups, and retention campaign coordination consume advisor time that should be spent in student meetings |
| 3 | Consolidate Tech Stack with AI | Medium | Student success tech stacks include SIS, LMS, EAB/Starfish, CRM, advising schedulers, tutoring platforms, and survey tools — all disconnected |

## Prioritized Use Cases

---

### Use Case 1: Early Alert Intervention Workflow Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Early alert systems (faculty flag students showing warning signs — absences, poor grades, disengagement) generate hundreds or thousands of alerts per semester. The alert fires, but then what? At most institutions, alerts land in an inbox or a basic queue. There's no systematic triage, assignment, escalation, or follow-up tracking. An alert for a first-generation freshman failing chemistry and an alert for a senior missing one elective class get treated the same. Advisors manually sort through alerts, attempt outreach via email (often ignored), and have no visibility into whether other staff are also reaching out to the same student. Result: alert fatigue, duplicated effort, and students falling through the cracks.

#### The Solution
monday.com Work Management transforms early alerts from notifications into managed workflows. An Early Alert Triage board receives alerts (via form, integration, or manual entry) with columns: Student Name (text), Student ID (text), Alert Source (dropdown: Faculty, LMS Auto-Flag, Financial Aid, Residence Life, Athletics), Alert Type (dropdown: Academic Performance, Attendance, Financial, Behavioral, Mental Health), Risk Level (status: Low, Moderate, High, Critical), Assigned Advisor (people), Intervention Status (status: New, Contacted — No Response, Meeting Scheduled, Intervention In Progress, Resolved, Escalated), Intervention Type (dropdown: Email Outreach, Phone Call, In-Person Meeting, Referral — Tutoring, Referral — Counseling, Referral — Financial Aid, Academic Plan Revision), Response Timeline (timeline), Notes (long text), Follow-Up Date (date). Automations route alerts based on risk level and student population (e.g., Critical → immediate assignment + text notification to advisor; athletics alerts → Athletic Academic Advisor).

#### The Outcome
Reduce average time from alert to first student contact from 5–7 days to under 48 hours. Ensure 100% of high/critical alerts receive documented follow-up (vs. typical 60–70%). Eliminate duplicate outreach through centralized visibility. Track intervention outcomes to identify which approaches work for which student populations.

#### Discovery Questions
- "How many early alerts does your institution generate per semester, and what's your current process for triaging and responding to them?"
- "What percentage of early alerts result in documented advisor-student contact within the first week?"
- "Do you have visibility into whether multiple staff members are reaching out to the same student from different alerts?"
- "How do you prioritize alerts — is a first-year student flagged for academic performance treated differently than a senior?"
- "Can you currently track whether an intervention (tutoring referral, advising meeting) actually improved the student's outcome?"

#### Industry Context
Early alert systems are mandated or strongly encouraged by most accreditors and state systems. Common platforms: Starfish (Hobsons), EAB Navigate/SSC, Beacon (Civitas/Watermark), and homegrown SIS-based systems. The challenge is universally the same: alert generation outpaces response capacity. Research shows that the speed of intervention matters — students contacted within 48 hours of an alert are 2.5x more likely to utilize support services. Many institutions report 30–40% of alerts receive no documented follow-up.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an 'Early Alert Triage & Response' board in monday.com. Groups by risk level: Critical (Immediate Action), High Risk, Moderate Risk, Low Risk. Each item is an individual alert. Columns: Student Name (text), Student ID (text), Student Email (email), Student Phone (phone), Academic Program (dropdown: populate with 15-20 common programs like Business, Engineering, Nursing, Education, Liberal Arts, Sciences, Fine Arts, Pre-Med, Computer Science, Communications, Psychology, Sociology, Criminal Justice, Biology, Chemistry), Class Year (dropdown: Freshman, Sophomore, Junior, Senior, Graduate), First-Generation (checkbox), Alert Source (dropdown: Faculty Report, LMS Grade Alert, Attendance System, Financial Aid Hold, Residence Life Report, Self-Referral, Athletics Compliance), Alert Category (dropdown: Academic Performance, Chronic Absence, Financial Risk, Behavioral Concern, Mental Health, Engagement Decline), Risk Score (number, 1-100), Assigned Advisor (people), Current Status (status: New, Outreach Attempted, Contact Made, Meeting Scheduled, Intervention Active, Resolved — Improved, Resolved — Withdrawn, Escalated), Intervention Type (dropdown: Email/Text Outreach, Phone Call, In-Person Meeting, Tutoring Referral, Counseling Referral, Financial Aid Consultation, Academic Plan Modification, Dean of Students Referral), First Contact Date (date), Days to Contact (formula: First Contact Date - creation date), Follow-Up Date (date), Outcome Notes (long text), Linked Referrals (connect board). Add automations: When item created with Risk Score >80, assign to Senior Advisor group and send immediate notification; when Status is 'New' for more than 2 days, send reminder to Assigned Advisor; when Follow-Up Date arrives, notify Assigned Advisor; when Status changes to 'Resolved', move to completed group. Dashboard: (1) numbers widget showing total open alerts, (2) bar chart of alerts by category, (3) average Days to Contact metric, (4) pie chart of intervention types used, (5) table of alerts in 'New' status >3 days (aging alerts)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Student Shield
**Agent Purpose:** Intelligently triage incoming early alerts, coordinate multi-touch interventions, and track outcome patterns to improve institutional response effectiveness.

**Triggers:**
- When a new early alert item is created
- When Status remains "New" for 24 hours (Critical) or 48 hours (High)
- When a student has 3+ alerts within a 30-day period (pattern detection)
- Weekly summary generation (Monday mornings)
- When Status changes to "Resolved" (outcome tracking)

**Actions:**
- Auto-calculate risk score based on alert category + student demographics (first-gen, freshman, financial aid recipient = higher risk multiplier)
- Route alerts to appropriate advisor based on student's academic program and advisor caseload balance
- When a student has multiple active alerts, consolidate into a single "case" with a coordinated intervention plan and assign a lead advisor
- Send progressive outreach messages: email at 0 hours, text at 24 hours, phone prompt to advisor at 48 hours for unresponsive students
- Track resolution patterns and generate monthly insight report: "Tutoring referrals resolved 73% of academic performance alerts within 4 weeks; counseling referrals resolved 61% of engagement decline alerts"
- Flag students who were "Resolved" but generated a new alert within 30 days (recurring risk)

**Data Required:**
- Student Information System (SIS) data: demographics, enrollment status, GPA, financial aid status, first-generation flag
- LMS gradebook and activity data (for academic alert correlation)
- Advisor assignment roster and caseload data
- Historical intervention outcome data
- Student contact information directory

**Autonomy Level:** Escalation-Based
Triage scoring, advisor routing, and initial outreach messages are fully autonomous. Multi-alert case creation notifies the advisor for review. Mental health and behavioral alerts always include Dean of Students notification. Withdrawal-risk escalations require advisor confirmation before Dean involvement.

**Example Interaction:**
> A chemistry professor submits an early alert for Maria Santos (Student ID: 20243891), a first-generation sophomore pre-nursing major. The alert notes: "Missed 4 of last 6 labs, midterm grade D+, stopped participating in study groups." Student Shield calculates a risk score of 87 (academic performance alert + first-gen + nursing prerequisite course = high stakes). It checks for other active alerts and finds a financial aid hold flagged 2 weeks ago (unpaid balance of $1,200). The agent creates a consolidated case: "Maria Santos — Multi-Factor Risk. Academic: Failing CHEM 201 (nursing prerequisite, must earn C+ to progress). Financial: $1,200 balance hold. Combined risk score: 92." It assigns her primary advisor (Dr. Kim, pre-nursing track) as lead and notifies the Financial Aid office. Automated outreach: a text message — "Hi Maria, this is the Student Success Center. We noticed you might be having a tough semester. We'd love to help — can we set up a 15-minute chat this week? Reply YES and we'll send scheduling options." Simultaneously, the agent schedules a follow-up task for Dr. Kim if Maria doesn't respond within 48 hours.

---

### Use Case 2: Advisor Caseload & Outreach Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Academic advisors at most institutions manage caseloads of 300–800+ students with minimal tooling beyond email, calendar, and the SIS. They're expected to conduct proactive outreach campaigns (registration reminders, degree audit check-ins, career exploration nudges), respond to early alerts, manage drop-in and scheduled appointments, document meeting notes, and track student progress — all while being evaluated on metrics like contact rates, persistence rates, and graduation timelines. Most advisors spend 40–60% of their time on administrative tasks (scheduling, note-taking, data entry) rather than actual advising conversations. There's no systematic way to ensure every student in a caseload receives appropriate touchpoints each semester.

#### The Solution
monday.com Work Management creates an Advisor Command Center. Each advisor gets a personalized board (or filtered view) of their caseload. Students are items with columns: Student Name (text), Student ID (text), Program (dropdown), Class Year (dropdown), GPA (number), Credits Completed (number), Credits Remaining (number), Registration Status (status: Registered, Not Registered, Partial), Last Advisor Contact (date), Days Since Contact (formula), Risk Flags (tags: Academic Probation, Financial Hold, First-Gen, Transfer, Undeclared), Next Action (dropdown: Registration Outreach, Degree Audit Review, Career Conversation, Graduation Application, General Check-In), Priority (status: Urgent, This Week, This Month, Routine). Automations power systematic outreach campaigns: pre-registration, all students with >30 days since contact get a check-in prompt, probation students get weekly follow-up tasks.

#### The Outcome
Increase advisor-student contact rate from typical 40–60% to 85%+ per semester. Reduce administrative time per student interaction by 30 minutes. Ensure no student goes an entire semester without advisor contact. Enable data-driven caseload balancing based on risk factors rather than alphabetical assignment.

#### Discovery Questions
- "What's the average advisor-to-student ratio in your institution, and how do advisors manage their caseloads today?"
- "What percentage of your students have at least one documented advisor interaction per semester?"
- "How do advisors track which students they've contacted and which are overdue for outreach?"
- "Do you have a proactive outreach cadence, or is advising mostly reactive (students come when they have a problem)?"
- "How much time do advisors spend on scheduling, note-taking, and data entry versus actual advising?"

#### Industry Context
NACADA (National Academic Advising Association) recommends advisor-to-student ratios of 1:300 or lower for effective advising; many institutions exceed 1:500. The shift from "prescriptive" advising (telling students which courses to take) to "proactive" or "intrusive" advising (reaching out before problems escalate) requires systematic workflow support. Key metrics: contact rates, appointment show rates, DFW rates (D grades, failures, withdrawals) in advised students, time-to-degree, and persistence rates. Case management approaches borrowed from social work are gaining traction.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an 'Advisor Caseload Manager' board in monday.com. Groups by student risk tier: Critical — Immediate Outreach, High Priority — This Week, Standard — This Month, On Track — Routine. Each item is a student. Columns: Student Name (text), Student ID (text), Email (email), Phone (phone), Major/Program (dropdown: list 15 programs), Minor (text), Class Year (dropdown: Freshman, Sophomore, Junior, Senior, 5th Year, Graduate), Current GPA (number), Cumulative GPA (number), Credits Earned (number), Credits to Graduation (number), Expected Graduation (date), Assigned Advisor (people), Last Contact Date (date), Days Since Contact (formula: TODAY - Last Contact Date), Contact This Semester (number), Risk Flags (tags: Academic Probation, Financial Hold, First-Gen, Transfer Student, Undeclared Major, DFW Alert, Attendance Warning, Pell Eligible), Next Action Needed (dropdown: Registration Advising, Degree Audit Review, Major Declaration, Career Exploration, Graduation Application, Academic Recovery Plan, General Check-In, Tutoring Follow-Up), Action Priority (status: Urgent, High, Normal, Low), Last Meeting Notes (long text), Referrals Made (tags: Tutoring, Counseling, Career Services, Financial Aid, Disability Services, Writing Center). Automations: when Days Since Contact > 30 and Risk Flags contains 'Academic Probation', move to Critical group and notify Advisor; when Registration Period starts (set date), create batch outreach tasks for all students not yet registered; every Monday, send Advisor a summary of their top 10 priority students. Dashboard: (1) numbers widget for total caseload and % contacted this semester, (2) pie chart of risk flag distribution, (3) bar chart of days since contact distribution, (4) table of students with Days Since Contact >45 (lost contact list), (5) advisor comparison chart showing contact rates by advisor."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Advising Autopilot
**Agent Purpose:** Automate routine advisor workflows, generate proactive outreach campaigns, and ensure no student falls through the caseload cracks.

**Triggers:**
- Start of registration period (campaign trigger)
- When Days Since Contact exceeds 30 for any student
- When a student's GPA drops below 2.0 (academic standing threshold)
- When a student has 0 credits registered for next semester within 2 weeks of deadline
- Daily morning briefing for each advisor

**Actions:**
- Generate daily advisor briefing: "Good morning, Dr. Williams. You have 3 critical students needing outreach today, 2 appointments scheduled, and 47 students still unregistered for Spring. Top priority: James Chen (GPA dropped from 3.1 to 1.8 this semester — schedule academic recovery meeting)."
- Draft personalized outreach emails/texts for registration campaigns, incorporating each student's specific situation (e.g., "You need CHEM 201 next semester for your nursing track — sections are filling up")
- After each advising meeting, prompt advisor for quick-entry notes (structured: topics discussed, action items, referrals, follow-up date) and auto-update student record
- Identify caseload imbalances: "Advisor Martinez has 42 high-risk students vs. team average of 28. Recommend redistributing 8 undeclared majors to Advisor Park (currently at 19 high-risk)."
- Generate end-of-semester outcome report: contact rates, persistence rates for contacted vs. non-contacted students, DFW rate trends

**Data Required:**
- Student Information System data (enrollment, grades, credits, holds)
- Advisor assignment roster
- Academic calendar (registration dates, add/drop deadlines)
- Appointment scheduling system data
- Historical persistence/retention data

**Autonomy Level:** Human-in-the-Loop
Daily briefings and outreach drafts are autonomous. Actual email/text sends require advisor approval (one-click confirm). Caseload rebalancing recommendations go to Director of Advising. Academic recovery plan suggestions are drafts for advisor customization.

**Example Interaction:**
> Registration for Fall 2026 opens in 5 days. Advising Autopilot scans Dr. Williams' caseload of 380 students and finds 127 have not yet met with their advisor for registration advising. It segments them: 23 are first-year students (highest priority — they need guidance on course selection), 18 have prerequisite issues that could block enrollment, 86 are on-track upper-class students. The agent generates three email campaigns: (1) First-year — personalized messages referencing each student's intended major and suggesting specific courses: "Hi Aisha, as a declared Biology major, you'll want to register for BIO 202 and CHEM 201 this fall — both are prerequisites for your junior-year labs. I have openings Tuesday and Thursday this week for a 15-minute registration session. Book here: [link]" (2) Prerequisite issues — flagging specific problems: "Hi Marcus, I noticed you haven't completed MATH 151 yet, which is required for your Engineering courses next year. Let's discuss your options — I have some ideas. [Book link]" (3) Upper-class — lighter touch: "Hi Sarah, registration opens Monday! Your degree audit looks great — you're on track for May 2027 graduation. Reach out if you need help, otherwise happy registering! [link]" The drafts are queued for Dr. Williams to review and send with one click.

---

### Use Case 3: Student Retention Campaign & At-Risk Cohort Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Retention is the single most important financial and academic metric for most institutions. Losing a student costs $15,000–$50,000+ in direct tuition revenue, plus financial aid that could have been reallocated. National retention rates hover around 75% first-year to second-year (lower at open-access institutions). Institutions know which demographic factors correlate with attrition (first-generation, Pell-eligible, commuter, undeclared major, part-time) but struggle to operationalize retention campaigns at scale. A Dean of Students might identify 400 at-risk freshmen but has no system to ensure each receives a coordinated series of interventions throughout the year — welcome week outreach, 3-week check-in, midterm grade review, financial aid renewal reminder, spring registration nudge, and re-enrollment confirmation.

#### The Solution
monday.com Work Management creates a Retention Campaign Engine. A board tracks at-risk cohorts (e.g., "Fall 2026 First-Year At-Risk") with each student as an item. Subitems represent scheduled intervention touchpoints throughout the year. Columns on items: Student Name, Cohort Tags (dropdown multi: First-Gen, Pell, Commuter, Part-Time, Undeclared), Predicted Retention Probability (number, from predictive model), Intervention Track (dropdown: High-Touch, Moderate, Light Touch), Campaign Status (status). Automations trigger touchpoints at predetermined intervals, create tasks for advisors/success coaches, and track completion. Dashboards show cohort retention rates in real-time compared to targets and prior years.

#### The Outcome
Increase first-year retention by 3–5 percentage points (worth $500K–$2M+ annually at a mid-size institution). Ensure systematic, equitable delivery of retention interventions regardless of which advisor a student is assigned to. Build longitudinal data on which interventions drive retention for which populations. Reduce "summer melt" (admitted students who never show up) by 15–25%.

#### Discovery Questions
- "What's your current first-year retention rate, and what's your target?"
- "Do you run structured retention campaigns, or is retention more of a general institutional goal without specific workflows?"
- "How do you identify at-risk students — is it data-driven (predictive models) or intuition-based?"
- "Can you ensure that every identified at-risk student receives a consistent set of interventions throughout the year?"
- "What happens over the summer between first and second year — do you have a 'summer melt' prevention strategy?"

#### Industry Context
Retention metrics are central to: (1) State funding formulas — 35+ states use performance-based funding tied to completion, (2) U.S. News rankings — 4.5% weight on first-year retention, (3) Accreditation — regional accreditors require retention/completion data, (4) Financial sustainability — net tuition revenue depends on retaining enrolled students. Key approaches: EAB's Student Success Collaborative, Civitas Learning's predictive analytics, Trellis Company's student financial wellness research, and NSSE (National Survey of Student Engagement) data for identifying engagement gaps.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 'Retention Campaign Tracker' board in monday.com. Groups by cohort: Fall 2026 First-Year, Fall 2026 Transfer Students, Returning Sophomores At-Risk, Financial Risk Cohort. Each item is a student. Columns: Student Name (text), Student ID (text), Email (email), Cohort Tags (tags: First-Gen, Pell Eligible, Commuter, Part-Time, Undeclared Major, Transfer, International, Student-Athlete, Working 20+ hrs), Predicted Retention Score (number, 0-100), Intervention Track (dropdown: High-Touch — weekly, Moderate — biweekly, Light Touch — monthly), Assigned Success Coach (people), Campaign Status (status: Active, Engaged, Non-Responsive, Withdrawn, Retained — Enrolled for Next Term), Current GPA (number), Midterm Flags (number, count of D/F midterm grades), Financial Aid Status (dropdown: Complete, Incomplete — Missing Docs, Hold, Not Applied), Housing Status (dropdown: On-Campus, Off-Campus, Commuter), Engagement Score (number — based on event attendance, org involvement, facility usage), Notes (long text). Use subitems for scheduled touchpoints: Welcome Week Check-In (week 1), 3-Week Pulse (week 3), Midterm Review (week 8), Registration Nudge (week 10), Financial Aid Renewal (week 12), Spring Confirmation (week 15), Summer Bridge (June), Re-Enrollment Confirmation (August). Each subitem: Touchpoint Name (text), Scheduled Date (date), Completed (checkbox), Method (dropdown: Email, Text, Phone, In-Person, Event), Response (dropdown: Engaged, No Response, Declined), Notes (long text). Automations: when a touchpoint's Scheduled Date arrives and Completed is unchecked, notify Assigned Success Coach; when 3+ consecutive touchpoints show 'No Response', change Campaign Status to 'Non-Responsive' and escalate to Director; when student registers for next semester, change Campaign Status to 'Retained'. Dashboard: (1) gauge showing cohort retention rate (% with Status 'Retained'), (2) bar chart of touchpoint completion rates, (3) funnel showing Active → Engaged → Retained conversion, (4) table of Non-Responsive students for immediate action, (5) comparison chart: retention rate by cohort tag."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Retention Radar
**Agent Purpose:** Orchestrate year-long retention campaigns, detect disengagement signals early, and maximize the probability that at-risk students persist.

**Triggers:**
- When a new student cohort is loaded at semester start
- When a scheduled touchpoint date arrives
- When a student's GPA drops below 2.0 at midterm
- When 2+ consecutive touchpoints are marked "No Response"
- When a student drops a course (enrollment change detected)
- End-of-semester retention analysis

**Actions:**
- At semester start, auto-assign students to intervention tracks based on risk score: >70 = High-Touch, 40-70 = Moderate, <40 = Light Touch
- Generate touchpoint outreach messages personalized to each student's situation and timing (e.g., 3-week pulse: "How are your first few weeks going? Have you found your study spots and connected with your professors?")
- When a student becomes "Non-Responsive" after 3 touchpoints, escalate with a recommended in-person strategy: "Jordan hasn't responded to 3 outreach attempts. He's a commuter, first-gen, working part-time. Recommend: have his BIOL 101 professor invite him to office hours (warm handoff), or send a peer mentor from his residence to connect."
- Detect compounding risk: "Student has D at midterm + financial aid incomplete + no campus event attendance → risk score increased from 62 to 89. Moving to High-Touch track."
- Generate weekly retention dashboard email to VP of Student Success: enrolled count, at-risk count, non-responsive count, withdrawn count, intervention effectiveness metrics

**Data Required:**
- Student demographic and enrollment data from SIS
- Predictive retention model scores (from EAB, Civitas, or institutional model)
- LMS engagement data (login frequency, assignment submissions)
- Campus card/ID swipe data (dining, library, gym usage as engagement proxy)
- Financial aid status data
- Course enrollment and withdrawal data

**Autonomy Level:** Escalation-Based
Routine touchpoint scheduling and outreach messages are autonomous. Non-responsive escalations route to Success Coach for personalized intervention. Course withdrawal alerts notify both advisor and Dean of Students. Withdrawal processing requires human confirmation.

**Example Interaction:**
> It's week 8 (midterm) and Retention Radar processes midterm grade reports for the Fall 2026 First-Year cohort of 420 at-risk students. It identifies 67 students with one or more D/F midterm grades. Cross-referencing engagement data, it flags 12 students as "compounding risk" — poor grades AND low campus engagement AND financial concerns. For one student, Tyler Brooks: "⚠️ Tyler Brooks — Risk Score escalated from 58 to 91. Midterm D in MATH 101, F in ENGL 101. Has not swiped campus card in dining hall in 3 weeks (was averaging 10x/week in September). Financial aid file shows missing verification documents — aid disbursement on hold. He was responsive to Week 3 text check-in but did not show for Week 5 scheduled meeting. Recommend: (1) Immediate Success Coach outreach via personal phone call. (2) Flag financial aid for proactive document support outreach. (3) Connect with Residence Life to check welfare. This student matches the profile of 78% of students who withdrew mid-semester last year." The agent creates coordinated tasks for all three offices and schedules a case conference for Friday.

---

### Use Case 4: New Student Onboarding & Orientation Program Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
New student onboarding involves coordinating dozens of tasks across 6–12 weeks: housing selection, meal plan enrollment, placement testing, orientation registration, immunization compliance, financial aid acceptance, course registration, ID card pickup, technology account setup, parking permits, disability services registration, and more. Each task is owned by a different department, each has its own deadline and communication channel, and students (especially first-generation) are overwhelmed by the volume and complexity. Institutions track completion through enrollment deposits and housing contracts but often lack visibility into whether students have completed all pre-enrollment tasks — leading to chaotic first weeks and preventable "summer melt" (10–20% of confirmed students who never arrive).

#### The Solution
monday.com Work Management creates a New Student Onboarding Pipeline. Each incoming student is an item tracked through an onboarding checklist. Columns: Student Name (text), Student Type (dropdown: First-Year, Transfer, International, Graduate), Deposit Paid (checkbox), Housing Selected (checkbox), Meal Plan Selected (checkbox), Orientation Registered (checkbox), Placement Tests Complete (checkbox), Immunizations Submitted (checkbox), Financial Aid Accepted (checkbox), Courses Registered (checkbox), ID Card Activated (checkbox), IT Accounts Set Up (checkbox), Onboarding Completion % (formula: count of checked items / total), Status (status: Admitted, Deposited, Partially Complete, Fully Onboarded, Melted/Withdrawn). Automations send reminders for incomplete tasks and escalate students with low completion percentages.

#### The Outcome
Reduce summer melt by 15–25% through proactive outreach to students with incomplete onboarding tasks. Cut Welcome Week chaos by ensuring 90%+ of students arrive fully onboarded. Give cross-departmental visibility into onboarding bottlenecks (e.g., 200 students haven't submitted immunizations 2 weeks before move-in). Free up Orientation staff from manual checklist tracking.

#### Discovery Questions
- "How many onboarding tasks does a new student need to complete between admission and the first day of classes?"
- "What's your summer melt rate — the percentage of deposited students who never show up?"
- "Do you have a single view of each student's onboarding completion, or does each department track their piece separately?"
- "What's your biggest onboarding bottleneck — is there a task that consistently holds students up?"
- "How do you identify students who are falling behind on onboarding tasks and intervene before they melt?"

#### Industry Context
Summer melt is a well-documented phenomenon, particularly affecting low-income and first-generation students. Research by Ben Castleman (UVA) shows that personalized text/nudge campaigns can reduce melt by 7–12 percentage points. The FAFSA completion challenge compounds the issue — students who haven't completed FAFSA verification by July often don't enroll. Key partners: Admissions, Financial Aid, Registrar, Housing, Health Services, IT, Orientation, Student Accounts. Many institutions use CRM tools (Slate, Salesforce) for admissions but lose workflow visibility post-deposit.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 'New Student Onboarding Tracker' board in monday.com. Groups: Fall 2026 First-Year, Fall 2026 Transfer, Fall 2026 International, Fall 2026 Graduate. Each item is an admitted student. Columns: Student Name (text), Student ID (text), Email (email), Phone (phone), Student Type (dropdown: First-Year, Transfer, International, Graduate), Home State (text), First-Generation (checkbox), Enrollment Deposit (status: Not Paid, Paid, Waived), Housing Application (status: Not Started, Submitted, Assigned, N/A), Meal Plan (status: Not Selected, Selected, N/A), Orientation (status: Not Registered, Registered, Attended), Placement Testing (status: Not Started, Scheduled, Complete, Exempt), Immunization Records (status: Not Submitted, Partial, Complete, Waiver Filed), FAFSA/Financial Aid (status: Not Filed, Filed — Incomplete, Verification Needed, Complete — Awarded), Course Registration (status: Not Started, Partial, Full Schedule), Student ID (status: Not Activated, Activated), IT Accounts (status: Not Created, Created, Activated), Parking Permit (status: Not Needed, Applied, Issued), Onboarding Score (formula: count completed items as percentage), Overall Status (status: At Risk, In Progress, Nearly Complete, Fully Onboarded), Assigned Counselor (people), Last Outreach (date), Notes (long text). Automations: if Enrollment Deposit is 'Paid' but Onboarding Score <25% after 30 days, move to At Risk and notify Counselor; if FAFSA status is 'Verification Needed' for >14 days, send financial aid reminder and notify FA office; 2 weeks before orientation, if Orientation status is 'Not Registered', send urgent reminder. Dashboard: (1) gauge showing overall onboarding completion rate, (2) bar chart of completion rate by task (which tasks are bottlenecks), (3) numbers widget: total admitted, deposited, fully onboarded, at risk, (4) pie chart by student type, (5) table of At Risk students sorted by Onboarding Score (lowest first)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Onboarding Navigator
**Agent Purpose:** Guide each incoming student through the onboarding journey, proactively removing friction points and preventing summer melt.

**Triggers:**
- When a new student deposits and enters the onboarding pipeline
- Weekly scan of all students with Onboarding Score <50% (every Wednesday)
- When a specific task has been incomplete for 14+ days
- 30/14/7 days before orientation date
- When financial aid status changes to "Verification Needed"

**Actions:**
- Send personalized welcome message upon deposit with a visual onboarding checklist and deadlines
- Generate weekly progress nudges tailored to each student's remaining tasks: "Hey Maria! You're 60% done with onboarding. Next up: submit your immunization records (due July 15) and register for orientation (spots filling fast!). Here's your personalized to-do list: [link]"
- When FAFSA verification is pending, send step-by-step instructions with common document examples and link to financial aid office scheduling
- Flag students showing melt indicators: deposit paid but 0 tasks completed after 3 weeks, or sudden cessation of portal logins
- Connect at-risk students with peer ambassadors from similar backgrounds (first-gen → first-gen mentor, transfer → transfer mentor)
- Generate daily department dashboards: "Housing: 78% of deposited students have submitted applications. 342 students have not — here's the list with contact info."

**Data Required:**
- Admissions CRM data (deposit status, student demographics)
- Housing, dining, health services, registrar system APIs or manual data feeds
- Financial aid status data
- Orientation registration system
- Student portal login activity

**Autonomy Level:** Human-in-the-Loop
Automated nudge messages and progress tracking are autonomous. Melt-risk escalations go to Enrollment Manager for personal outreach. Peer ambassador assignments are recommended and require counselor confirmation.

**Example Interaction:**
> It's July 3rd — 6 weeks before Fall move-in. Onboarding Navigator flags 89 deposited first-year students with Onboarding Score below 40%. It segments them: 34 haven't selected housing (critical — assignment deadline is July 15), 52 have incomplete financial aid files, 41 haven't registered for orientation (last session is July 20). For Jayden Williams (first-gen, Pell-eligible, from rural Georgia): Onboarding Score 25% — only deposit paid and IT accounts created. "Jayden hasn't selected housing, registered for orientation, submitted immunizations, or completed FAFSA verification. He logged into the student portal twice in May but hasn't returned since. Melt probability: High. Recommend: personal phone call from Admissions counselor who recruited him. Talking points: (1) Housing deadline is July 15 — walk him through the portal. (2) His FAFSA needs a signed tax transcript — explain exactly how to request from IRS. (3) Orientation has 3 remaining sessions — register him on the call if possible. I've drafted a text message as first touch: 'Hi Jayden! This is the Student Success team at [University]. We're excited you're joining us this fall! Looks like you have a few things to wrap up before move-in. Can I help? Reply YES and I'll call you today.'"

---

### Use Case 5: Student Success Case Management & Referral Tracking

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
When a student needs help beyond academic advising — mental health counseling, food insecurity support, disability accommodations, financial emergency aid, career coaching, or legal services — the referral process is fragmented. An advisor identifies the need, perhaps sends an email to the relevant office, and hopes for the best. There's rarely a closed-loop system: did the student actually schedule a counseling appointment? Did they receive emergency financial aid? Did disability services process their accommodation letter? Students in crisis often need help from 3–4 offices simultaneously, and nobody is tracking the complete picture. Advisors feel helpless because they can't follow up on referrals they've made.

#### The Solution
monday.com Work Management creates a Student Support Referral Hub. When an advisor identifies a need, they create a referral item (or subitem linked to the student's main record). Columns: Student Name (text), Referring Staff (people), Referral Type (dropdown: Counseling/Mental Health, Financial Emergency, Disability Services, Tutoring/Academic Support, Career Services, Food Pantry, Housing Insecurity, Legal Services, Health Services), Receiving Office (dropdown), Urgency (status: Routine, Urgent, Emergency), Referral Status (status: Submitted, Acknowledged, Appointment Scheduled, In Progress, Completed, Student Declined, No Show), Date Submitted (date), Date Acknowledged (date), Date Resolved (date), Time to Resolution (formula), Notes (long text), Follow-Up Needed (checkbox). The receiving office updates the status (without sharing confidential details), closing the feedback loop.

#### The Outcome
Achieve closed-loop referral tracking — advisors know whether their referrals resulted in student action. Reduce referral-to-appointment time from 7–14 days to 2–3 days. Identify systemic capacity issues (e.g., counseling center has a 3-week waitlist). Enable holistic student support by giving authorized staff a complete view of services engaged. Generate data for resource allocation decisions.

#### Discovery Questions
- "When an advisor refers a student to counseling or financial aid, is there a way to track whether the student actually followed through?"
- "How do you handle students who need support from multiple offices simultaneously — is anyone coordinating the overall case?"
- "Do you know your average wait time for student counseling appointments? For disability accommodation processing?"
- "How do you identify systemic capacity issues — like when the counseling center is overwhelmed?"
- "Is there a case management approach for your highest-need students, or is it more ad hoc?"

#### Industry Context
Holistic student support (sometimes called "integrated care" or "case management") is a growing movement in higher ed. Organizations like NASPA (Student Affairs Administrators in Higher Education) and the Jed Foundation promote coordinated care models. FERPA (Family Educational Rights and Privacy Act) governs data sharing — referral tracking can share status updates without sharing clinical/counseling details. Basic needs insecurity (food, housing, financial) affects 30–45% of students (Hope Center research). Counseling center demand has surged 30–40% post-pandemic, creating waitlist crises at many institutions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a 'Student Support Referral Hub' in monday.com. Groups by service type: Academic Support, Mental Health & Counseling, Financial Support, Basic Needs (Food/Housing), Disability Services, Career Services, Health Services. Each item is a referral. Columns: Student Name (text), Student ID (text), Referring Staff (people), Referring Department (dropdown: Academic Advising, Faculty, Residence Life, Athletics, Financial Aid, Dean of Students, Self-Referral), Referral Type (dropdown: Tutoring, Writing Center, Supplemental Instruction, Counseling — Individual, Counseling — Group, Crisis Intervention, Emergency Financial Aid, Textbook Assistance, Food Pantry, Housing Emergency, Disability Accommodation, Career Coaching, Resume Review, Health Services, Legal Services), Receiving Office (people), Urgency (status: Routine, Priority, Urgent, Emergency), Referral Status (status: Submitted, Acknowledged by Office, Student Contacted, Appointment Scheduled, Service In Progress, Completed, Student Declined, Student No-Show, Waitlisted), Date Submitted (date), Date Acknowledged (date), Date First Appointment (date), Date Resolved (date), Days to Acknowledge (formula), Days to Resolution (formula), Referral Notes — Advisor (long text), Status Notes — Receiving Office (long text), Follow-Up Required (checkbox), Follow-Up Date (date), FERPA Consent (checkbox). Automations: when Urgency is 'Emergency', immediately notify Receiving Office via Slack/email AND Dean of Students; if Referral Status is 'Submitted' for >2 business days, escalate to Receiving Office manager; when Status changes, notify Referring Staff; when Follow-Up Date arrives, prompt Referring Staff to check in with student. Dashboard: (1) numbers widget for total open referrals, (2) bar chart of referrals by type (demand visibility), (3) average Days to Acknowledge by office (service level tracking), (4) pie chart of referral outcomes (completed vs. declined vs. no-show), (5) trend line of referral volume by month (capacity planning)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Care Connector
**Agent Purpose:** Ensure every student referral is acknowledged, acted on, and followed up — closing the loop between referring advisors and receiving offices.

**Triggers:**
- When a new referral is created
- When Referral Status has been "Submitted" for 48 hours without acknowledgment
- When a student has 3+ active referrals (multi-service coordination needed)
- When Status changes to "Student No-Show" or "Student Declined"
- Monthly capacity analysis report

**Actions:**
- Upon referral creation, send structured notification to receiving office with student context (non-clinical): "Referral from Dr. Kim (Academic Advising) for Maria Santos — Counseling, Priority. Student is a first-year pre-nursing major experiencing academic distress and possible anxiety. FERPA consent on file."
- Track acknowledgment SLA: if unacknowledged after 48 hours, escalate to office director with volume context ("Counseling Center has 12 unacknowledged referrals — possible capacity issue")
- When a student has 3+ active referrals, recommend a case conference: "Jordan Taylor has active referrals to Counseling, Financial Aid, and Disability Services. Recommend a coordinated case conference — creating calendar invite for all involved staff."
- When student declines or no-shows, notify referring advisor with suggested re-engagement approach: "Maria declined the counseling referral. Common reasons at this stage: stigma, schedule conflict, or feeling 'not bad enough.' Suggested approach: normalize the service, offer telehealth option, or connect with a peer who has used the service."
- Generate monthly capacity report: referral volume by service, average wait times, service utilization trends, offices approaching capacity

**Data Required:**
- Referral records and status updates
- Office capacity data (appointment slots available, current waitlist length)
- Student consent and FERPA authorization status
- Advisor and office staff directories
- Historical referral outcome data

**Autonomy Level:** Escalation-Based
Notifications, SLA tracking, and capacity reporting are fully autonomous. Case conference recommendations require advisor approval. Re-engagement strategies after declined referrals are suggestions only. Emergency referrals always include Dean of Students in the notification chain.

**Example Interaction:**
> Care Connector processes the monthly capacity report for November and identifies a critical trend: counseling center referrals are up 45% over October (midterm stress period), and average Days to First Appointment has increased from 4 to 11 days. Three emergency referrals this month waited 3+ days for acknowledgment. The agent generates an alert to the VP of Student Affairs: "⚠️ Counseling Center Capacity Alert. November referrals: 89 (up 45% from October's 61). Average wait for first appointment: 11 days (target: <5). Three emergency-priority referrals experienced delayed acknowledgment. Current counselor-to-student ratio: 1:1,800 (IACS recommends 1:1,000-1,500). Recommendations: (1) Activate group counseling sessions for common presenting concerns (anxiety, academic stress) to increase throughput. (2) Engage TimelyCare or similar telehealth vendor for overflow. (3) Train advisors in Mental Health First Aid to provide initial support while students wait. Budget estimate for telehealth overflow: $15,000-25,000 for spring semester." The report includes a trend chart and is formatted for the VP's weekly leadership meeting.

---

### Use Case 6: Alumni Engagement & Post-Graduation Outcome Tracking

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Post-graduation outcome tracking is increasingly required by accreditors, state systems, and federal reporting (Graduate Employment data, First Destination Survey). Career services and alumni offices need to track where graduates go — employment, graduate school, military, volunteer service — and the data collection is miserable. First Destination Surveys have average response rates of 40–60%, leaving large gaps. Alumni engagement after graduation is managed by Advancement/Development offices focused on fundraising, creating a disconnect with Career Services focused on outcomes data. Meanwhile, faculty want to know where their students end up (for program review and accreditation) but can't access the data easily.

#### The Solution
monday.com CRM serves as a Graduate Outcomes & Alumni Engagement tracker. Each graduate is a contact with columns: Name, Graduation Year, Degree (dropdown), Major (dropdown), First Destination (dropdown: Employed Full-Time, Employed Part-Time, Graduate School, Military, Volunteer Service, Still Seeking, Unknown), Employer/Institution (text), Job Title (text), Salary Range (dropdown), Location (text), Survey Responded (checkbox), LinkedIn Connected (checkbox), Alumni Event Attendance (number), Giving History (dropdown: Non-Donor, Annual Donor, Major Donor), Engagement Score (number), Last Contact (date). Automations trigger survey reminders at 6 months, 1 year, and 5 years post-graduation.

#### The Outcome
Increase First Destination Survey response rate from 50% to 75%+ through multi-channel automated outreach. Provide real-time outcome dashboards by program for accreditation and program review. Connect career outcomes data with alumni engagement for targeted re-engagement. Give departments actionable data on where their graduates work (for curriculum relevance, industry partnerships, and recruitment).

#### Discovery Questions
- "What's your current First Destination Survey response rate, and how do you collect the data?"
- "How do you track alumni career outcomes beyond the first job — is there a longitudinal view?"
- "Is there connection between your Career Services outcomes tracking and your Advancement/alumni engagement team?"
- "Do academic departments have access to outcome data for their graduates, and do they use it for program improvement?"
- "How do you leverage alumni as mentors, speakers, or employer contacts for current students?"

#### Industry Context
NACE (National Association of Colleges and Employers) publishes First Destination Survey standards and benchmarks. Knowledge rate (% of graduates with known outcomes) is the key metric — NACE recommends 65%+ for reliable data. Methods: surveys, LinkedIn scraping, National Student Clearinghouse (for graduate school enrollment), state wage matching (UI records). Accreditors (ABET, AACSB, CCNE) increasingly require outcome data for program accreditation. The connection between career outcomes and alumni giving is well-documented — graduates who feel their degree "paid off" are 3x more likely to donate.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a 'Graduate Outcomes Tracker' board in monday.com (CRM-style). Groups by graduation year: Class of 2026, Class of 2025, Class of 2024, Alumni 5+ Years. Each item is a graduate. Columns: Graduate Name (text), Student ID (text), Email — Personal (email), Email — Institutional (email), Phone (phone), LinkedIn URL (link), Graduation Year (dropdown), Degree Level (dropdown: Associate, Bachelor's, Master's, Doctorate, Certificate), Major (dropdown: list 20 common programs), Minor (text), First Destination Status (dropdown: Employed Full-Time, Employed Part-Time, Graduate/Professional School, Military, Fellowship/Volunteer, Entrepreneur, Still Seeking, Not Seeking, Unknown), Employer/Institution Name (text), Job Title (text), Industry (dropdown: list 15 industries), Salary Range (dropdown: <$30K, $30-45K, $45-60K, $60-80K, $80-100K, $100K+, Not Reported), Location — City (text), Location — State (dropdown), Survey Status (status: Not Sent, Sent, Reminder Sent, Completed, Bounced, Opted Out), Survey Response Date (date), Data Source (dropdown: Survey, LinkedIn, Faculty Report, Employer Verification, NSC, Self-Report), Knowledge Rate Flag (checkbox — checked if outcome is known), Alumni Engagement Score (number), Last Contact Date (date), Notes (long text). Automations: 3 months post-graduation, create survey outreach task; if Survey Status is 'Sent' for 14 days, change to 'Reminder Sent' and trigger follow-up email; when First Destination is populated, check Knowledge Rate Flag. Dashboard: (1) knowledge rate gauge (% with known outcomes), (2) pie chart of first destination distribution, (3) bar chart of outcomes by major, (4) salary range distribution chart, (5) geographic heat map data (state distribution), (6) numbers widget: total graduates, known outcomes, response rate."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Outcome Oracle
**Agent Purpose:** Maximize graduate outcome knowledge rate through multi-channel data collection and generate program-level insights for accreditation and improvement.

**Triggers:**
- 90 days post-graduation (initial outreach campaign)
- When Survey Status has been "Sent" for 14 days (reminder cycle)
- When knowledge rate for any major drops below 50%
- Annual accreditation data request
- When a graduate updates their LinkedIn profile

**Actions:**
- Deploy multi-wave survey campaigns: email at 90 days, text at 104 days, phone outreach list generated at 120 days for non-responders
- For non-responders, search LinkedIn for career updates and pre-populate fields (subject to verification)
- Generate program-level outcome reports for department chairs: "Computer Science Class of 2025: 87% knowledge rate. 72% employed (median salary $68,000, top employers: Google, Deloitte, local startups). 18% graduate school. Employment rate exceeds NACE benchmark by 8%."
- Flag programs with concerning outcomes (e.g., "Art History: 45% still seeking at 6 months — recommend Career Services targeted support for current seniors")
- Cross-reference outcome data with curriculum changes to identify correlations: "Programs that added required internship saw 12% higher employment rates"
- Compile NACE-format First Destination report automatically

**Data Required:**
- Graduate records from Registrar
- Survey response data
- LinkedIn API or manual search data
- National Student Clearinghouse enrollment data
- State wage record match data (where available)
- NACE benchmark data
- Accreditation reporting templates

**Autonomy Level:** Human-in-the-Loop
Survey deployment and reminder automation is autonomous. LinkedIn data pre-population requires Career Services verification before finalizing records. Program-level insight reports are drafts for Dean/Department Chair review. Accreditation reports require Director sign-off.

**Example Interaction:**
> The accreditation self-study for the College of Engineering is due in 3 months. Outcome Oracle generates a comprehensive employment outcome report for all Engineering programs (Mechanical, Electrical, Civil, Computer, Chemical) for the past 5 graduating classes. "Engineering Graduate Outcomes FY2021–FY2025: Overall knowledge rate: 82% (above NACE 65% benchmark). 5-year employment rate at graduation: 74% (national engineering average: 70%). Median starting salary: $72,000 (up 8% over 5 years). Top employers: Lockheed Martin (12 hires), local utilities (8), Raytheon (7). Graduate school rate: 19%. Concerning: Chemical Engineering employment rate dropped from 78% to 61% over 3 years — recommend industry advisory board review. Strength: Computer Engineering salary grew 22% (fastest of all programs). Data source: 68% survey, 22% LinkedIn, 10% employer verification." The report is formatted to match ABET Criterion 4 requirements and includes data tables ready for the self-study document.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Retention Rate | Percentage of students who return for the next academic year (typically measured first-year to second-year) |
| Persistence Rate | Percentage of students who continue enrollment at any institution (not just the original one) |
| Summer Melt | Phenomenon where admitted, deposited students fail to enroll — typically 10-20% at less selective institutions |
| DFW Rate | Percentage of students earning D, F, or Withdrawal in a course — a key academic risk indicator |
| SAP | Satisfactory Academic Progress — federal financial aid eligibility requires maintaining minimum GPA and completion rate |
| First Destination | A graduate's primary activity within 6 months of graduation (employment, grad school, etc.) — per NACE standards |
| Early Alert | Faculty or system-generated notification that a student is showing academic or behavioral warning signs |
| Intrusive Advising | Proactive advising approach where advisors reach out to students rather than waiting for students to seek help |
| EAB Navigate | Major student success platform providing predictive analytics and advising tools (Education Advisory Board) |
| Starfish | Student success/early alert platform by Hobsons — widely used for faculty referrals and advising |
| NACE | National Association of Colleges and Employers — sets standards for career services and outcome reporting |
| SIS | Student Information System — the core enrollment, grades, and records database (Banner, PeopleSoft, Workday Student) |
| LMS | Learning Management System — course content and grade platform (Canvas, Blackboard, D2L Brightspace) |
| FERPA | Family Educational Rights and Privacy Act — federal law governing student data privacy and sharing |
| Knowledge Rate | Percentage of graduates for whom career outcome data is known (NACE recommends 65%+) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/AVP of Student Success | Oversees retention strategy, advising, student support services | Decision-maker |
| VP of Enrollment Management | Owns admissions funnel, retention metrics, financial aid strategy | Decision-maker |
| Dean of Students | Student conduct, crisis response, basic needs support | Decision-maker/Influencer |
| Director of Academic Advising | Manages advisor teams, caseload assignments, advising technology | Decision-maker |
| Director of Career Services | Graduate outcomes, employer relations, career programming | Influencer |
| Director of Financial Aid | Aid packaging, FAFSA completion, emergency aid programs | Influencer |
| Director of Retention/Student Success | Data analysis, retention initiatives, at-risk student programs | Influencer/User |
| Academic Advisor/Success Coach | Direct student contact, caseload management, referrals | User (primary daily user) |
| Director of Institutional Research | Retention/completion data, predictive analytics, accreditation reporting | Influencer |
| Provost | Academic affairs oversight, faculty engagement in student success | Decision-maker (executive sponsor) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT | Manages SIS, LMS, and student success technology integrations | Cross-sell: IT project management, system integration workflows |
| Financial Aid | Financial holds and aid incomplete are top retention barriers | Cross-sell: financial aid processing workflow, FAFSA completion campaigns |
| Residence Life | Residential advisors are front-line observers of student distress | Cross-sell: incident reporting, roommate conflict resolution, programming management |
| Academic Departments | Faculty are primary early alert sources and curriculum owners | Cross-sell: department project management, curriculum mapping, program review |
| Marketing/Communications | Student communications, retention messaging, brand perception | Cross-sell: campaign management, content calendars for student communications |
| Institutional Research | Data warehouse, predictive models, accreditation reporting | Cross-sell: reporting workflows, data governance, survey management |
| Alumni Relations/Advancement | Post-graduation engagement, fundraising, mentorship programs | Cross-sell: CRM for alumni, event management, giving campaign workflows |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| EAB Navigate (SSC) | Market-leading student success platform — predictive analytics + advising tools | monday.com complements (not replaces) the analytics layer by managing intervention workflows. For institutions without EAB budget, monday.com can serve as the operational layer. |
| Starfish (Hobsons) | Early alert and advising platform — strong faculty referral workflow | monday.com offers broader workflow capabilities beyond just alerts; Starfish lacks project management for retention campaigns |
| Civitas Learning (Watermark) | Predictive analytics focused — strong on modeling, weaker on workflow | monday.com is the action layer that operationalizes Civitas predictions into managed interventions |
| Salesforce (Education Cloud) | CRM for enrollment + student lifecycle — powerful but complex and expensive | monday.com is faster to deploy, more intuitive for advisors, and far less expensive. Better for mid-market institutions that can't afford Salesforce implementation. |
| Slate (Technolutions) | Dominant admissions CRM — strong pre-enrollment, weak post-enrollment | monday.com extends the student journey past enrollment where Slate stops — onboarding, retention, advising |
| Spreadsheets/Email | The most common "system" for caseload management and campaign tracking | Direct replacement — emphasize automation, visibility, and accountability |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have EAB Navigate/Starfish for student success" | "EAB/Starfish tells you WHO is at risk. monday.com ensures the right intervention reaches that student and tracks whether it worked. They're complementary — analytics + operations." |
| "FERPA means we can't share student data across a platform" | "monday.com supports role-based permissions so each office sees only what they're authorized to see. Referral status ('acknowledged,' 'in progress') can be shared without sharing clinical or academic details. Your FERPA officer can configure access controls." |
| "Our advisors won't adopt another tool" | "Advisors are drowning in admin work — 40-60% of their time is non-advising tasks. monday.com reduces that burden with automated outreach, structured notes, and caseload dashboards. Show them the daily briefing and they'll see it saves time, not adds it." |
| "We're a small institution, we don't need this level of sophistication" | "Small institutions actually benefit most — you have fewer staff covering the same student needs. monday.com lets a team of 5 advisors systematically manage 2,000 students the way a team of 15 would manually." |
| "Student success is about relationships, not software" | "Absolutely — and the software exists to protect more time for relationships. When an advisor spends 30 minutes tracking down whether a student followed through on a counseling referral, that's 30 minutes not spent in a student conversation. monday.com handles the tracking so advisors can focus on the human connection." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder: University that improved retention rates using structured intervention tracking]
- [Placeholder: Community college that reduced summer melt with onboarding automation]
- [Placeholder: Institution that achieved closed-loop referral tracking across student services]
- [Placeholder: Career services office that increased First Destination Survey response rates]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
