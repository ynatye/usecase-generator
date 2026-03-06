# Colleges & Universities × Product & R&D Playbook

## Overview

Product & R&D within higher education encompasses a broad range of functions: educational technology (EdTech) development, learning management system (LMS) customization, student information system (SIS) enhancements, mobile app development, research computing platforms, and digital campus infrastructure. Unlike commercial software companies, university product teams must balance the needs of multiple constituencies — students, faculty, administrators, alumni, and accrediting bodies — while operating under tight budget constraints and lengthy governance cycles.

Most universities have centralized IT departments that house product and development teams, but increasingly, individual colleges and departments spin up their own digital initiatives — from custom research portals to department-specific scheduling tools. This creates a fragmented landscape where dozens of parallel development efforts lack coordination, leading to duplicated work, inconsistent user experiences, and technical debt. Teams range from 5-person agile squads at small liberal arts colleges to 100+ developer organizations at large research universities (R1/R2 institutions).

Regulatory context is significant: FERPA (Family Educational Rights and Privacy Act) governs student data, WCAG/Section 508 mandates accessibility compliance, and HECVAT (Higher Education Community Vendor Assessment Toolkit) shapes vendor evaluation. Product teams must navigate these requirements while also responding to rapid shifts in pedagogy — hybrid learning, micro-credentials, competency-based education — that demand new digital capabilities on compressed timelines.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | University product teams are chronically understaffed relative to the breadth of digital initiatives demanded by faculty, students, and administrators. Scaling delivery without proportional headcount growth is critical. |
| 2 | Consolidate Tech Stack with AI | High | Fragmented tools across departments (Jira here, Trello there, spreadsheets everywhere) create visibility gaps and slow cross-team collaboration on shared platforms. |
| 3 | Replace or Radically Augment Headcount | Medium | Adjunct/contract developers and student workers cycle frequently; automating repeatable processes (QA checklists, deployment tracking, documentation) reduces dependency on transient labor. |

## Prioritized Use Cases

---

### Use Case 1: EdTech Product Roadmap & Governance

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
University product teams juggle requests from academic affairs, student services, enrollment management, and individual faculty members — all with competing priorities. Without a centralized roadmap visible to stakeholders, the same feature gets requested through three different channels, governance committees lack data to prioritize, and product leaders spend 30%+ of their time in status meetings instead of building. Many institutions still manage roadmaps in PowerPoint decks that go stale within days of a committee meeting.

#### The Solution
monday.com Work Management with a multi-tier roadmap structure: **Strategic Roadmap board** (semester/annual view for provost and CIO-level governance), **Product Backlog board** (epics and features with weighted scoring — RICE or WSJF), and **Sprint Boards** per team. Connected dashboards roll up status automatically. Intake forms allow any department to submit requests that flow into a triage workflow. Status automations notify governance committee members when items move between stages.

#### The Outcome
- 60% reduction in redundant feature requests through centralized intake
- Governance committees make decisions in half the time with real-time dashboards
- Product leaders reclaim 8-10 hours/week from status reporting
- Full audit trail for accreditation reviews showing decision rationale

#### Discovery Questions
1. "How do faculty and department heads currently submit requests for new digital tools or features — and how many channels does that come through?"
2. "When your CIO or provost asks for a status update on the digital transformation portfolio, how long does it take to assemble that view?"
3. "How do you currently prioritize competing requests from academic affairs vs. enrollment vs. student life?"
4. "Have you ever had an accreditation review ask about your technology governance process?"
5. "How many parallel product/development efforts are happening across campus that aren't centrally tracked?"

#### Industry Context
University governance is committee-driven — Faculty Senate, IT Governance Committee, Student Technology Fee Committee. Decisions move slowly (often semester-aligned). Product teams must present clear data to these bodies. "Shared governance" means faculty have real veto power over technology decisions that affect pedagogy. Accreditation bodies (SACSCOC, HLC, MSCHE, etc.) increasingly evaluate institutional technology planning as part of reviews.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an EdTech Product Roadmap system with three connected boards. Board 1 — 'Strategic Roadmap': columns for Initiative Name (text), Strategic Theme (dropdown: Student Experience, Operational Efficiency, Research Excellence, Enrollment Growth, Accessibility & Compliance), Semester Target (dropdown: Fall 2026, Spring 2027, Summer 2027, AY 2027-28), Executive Sponsor (people), Status (status: Proposed, Approved, In Progress, Delivered, Deferred), Budget Estimate (numbers with $ prefix), and a link column to the Product Backlog. Board 2 — 'Product Backlog': columns for Feature Name (text), Parent Initiative (connect to Strategic Roadmap), Requesting Department (dropdown: Academic Affairs, Enrollment Management, Student Life, Research Office, Athletics, Financial Aid, Alumni Relations, Facilities), RICE Score (formula or numbers), Priority Tier (status: P0 Critical, P1 High, P2 Medium, P3 Low), Sprint Assignment (connect to Sprint Board), Assigned Team (people), and FERPA Impact (dropdown: Yes - Student PII, Yes - Directory Info, No). Board 3 — 'Sprint Board': columns for Story (text), Parent Feature (connect to Backlog), Story Points (numbers), Sprint (dropdown: Sprint 1 through Sprint 12), Assignee (people), Status (status: To Do, In Dev, Code Review, QA, Staging, Done), and Accessibility Reviewed (checkbox). Add automations: when a form submission creates an item on the Backlog, set status to 'Triage' and notify the product owner; when all stories in a feature are Done, update the Backlog item to 'Complete'. Create a Dashboard with widgets: roadmap timeline by semester, backlog by requesting department (chart), sprint velocity (numbers), and items blocked (filtered list)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** GovBot — Governance Intelligence Agent
**Agent Purpose:** Automatically prepares governance committee briefing packets by synthesizing roadmap status, backlog priorities, and sprint progress into executive summaries.

**Triggers:**
- Scheduled: Every Monday at 8 AM before weekly IT Governance meeting
- On-demand: When a governance committee member requests a briefing
- Status change: When any Strategic Roadmap item moves to "Deferred" (flags for committee review)
- Date-based: 2 weeks before each semester's governance review meeting

**Actions:**
- Generates executive summary document with status of all active initiatives, risks, and decisions needed
- Creates comparison view of resource allocation vs. strategic theme priorities
- Flags backlog items that have been in "Triage" for more than 2 weeks without prioritization
- Sends personalized briefing to each committee member highlighting items relevant to their division
- Recommends priority adjustments based on RICE score changes and dependency analysis
- Archives previous briefing for audit trail

**Data Required:**
- Strategic Roadmap board (all columns)
- Product Backlog board (request volume, RICE scores, department distribution)
- Sprint Board (velocity trends, completion rates)
- Calendar integration for meeting dates
- Committee member roles and division affiliations

**Autonomy Level:** Human-in-the-Loop
GovBot drafts all materials autonomously but requires product director sign-off before distribution. Committee decisions are recorded manually; GovBot then updates roadmap status based on recorded decisions.

**Example Interaction:**
> On Monday morning, GovBot scans the Strategic Roadmap and finds that the "Unified Student Portal" initiative has slipped from its Spring 2027 target — only 3 of 8 features are in progress, and 2 are blocked by an API dependency on the legacy SIS. GovBot generates a briefing noting the risk, calculates that reallocating 2 developers from the lower-priority "Alumni Engagement Dashboard" could recover the timeline, and flags this trade-off for the IT Governance Committee.
>
> The briefing lands in Dr. Patel's (VP of Student Affairs) inbox with a personalized note: "The Student Portal directly impacts your division's retention KPI. It's currently at risk. Today's committee agenda item #3 covers the resource reallocation proposal." Dr. Patel arrives at the meeting prepared, the committee approves the reallocation in 10 minutes instead of the usual 45-minute debate, and GovBot immediately updates both initiatives' timelines on the roadmap.

---

### Use Case 2: Learning Platform Release Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Universities running homegrown LMS extensions, custom integrations (LTI tools), or institution-specific student apps face complex release management challenges. Development, QA, staging, and production environments must be coordinated across multiple teams. Many institutions use a patchwork of Jira, Confluence, GitHub Issues, and email threads — leading to releases that break in production because a critical integration test was missed, or a FERPA-sensitive data flow wasn't reviewed. A single botched LMS release during midterms can affect 30,000+ students simultaneously.

#### The Solution
monday.com Dev product for end-to-end release management: **Release Board** tracking each release with linked feature items, environment status columns (Dev → QA → Staging → Prod), and integrated approval gates. **Bug Tracking Board** with severity classification aligned to university impact tiers (Tier 1: All students affected, Tier 2: Single college, Tier 3: Cosmetic). GitHub/GitLab integration syncs PR status. Automations enforce that no item moves to "Production" without completed accessibility review and FERPA data classification checkboxes.

#### The Outcome
- Zero missed compliance gates in releases (FERPA review, accessibility check, security scan)
- 40% faster release cycles by eliminating manual status chasing across tools
- Single source of truth replaces 4-5 disconnected tools
- Post-incident review data automatically captured for continuous improvement

#### Discovery Questions
1. "Walk me through your last LMS or student app release — how many tools and handoffs were involved from code commit to production?"
2. "Have you ever had a release go out without a completed FERPA or accessibility review? What happened?"
3. "How do you currently track which features are in which environment?"
4. "When a production bug is reported by a student or faculty member, how does it get from the help desk to the development team?"
5. "How do you coordinate releases that touch multiple systems — say, LMS, SIS, and the student portal simultaneously?"

#### Industry Context
University academic calendars create hard deadlines — you do NOT push a risky release during finals week or enrollment periods. "Code freezes" aligned to the academic calendar are standard practice. LTI (Learning Tools Interoperability) is the integration standard for LMS ecosystems. Most universities run Canvas, Blackboard, D2L Brightspace, or Moodle as their core LMS, with custom extensions layered on top. HECVAT assessments are required for any tool touching student data.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Learning Platform Release Management system. Board 1 — 'Release Pipeline': columns for Release Name (text), Version Number (text), Target Date (date), Release Manager (people), Academic Calendar Check (status: Safe Window, Caution - Exam Period, Blocked - Finals/Enrollment), Environment Status (status: Development, QA, Staging, Production, Rolled Back), FERPA Review (status: Not Started, In Review, Approved, N/A), Accessibility Audit (status: Not Started, In Progress, Passed, Failed - Remediation Needed), Security Scan (status: Pending, Clean, Issues Found), Features Included (connect to Feature Board), and Bugs Fixed (connect to Bug Board). Board 2 — 'Bug Tracker': columns for Bug Title (text), Reported By (dropdown: Student, Faculty, Staff, Automated Monitor), Impact Tier (dropdown: Tier 1 - All Students, Tier 2 - Single College/Dept, Tier 3 - Minor/Cosmetic), System Affected (dropdown: LMS, SIS, Student Portal, Mobile App, Research Portal, Integration Layer), Steps to Reproduce (long text), Assigned To (people), Status (status: New, Triaging, In Fix, In QA, Resolved, Won't Fix), and Linked Release (connect to Release Pipeline). Add automations: when Release Environment Status changes to 'Staging', check if FERPA Review and Accessibility Audit are both 'Approved' — if not, move status back and notify Release Manager with 'Compliance gate not met'; when a Tier 1 bug is created, immediately notify the dev lead and CTO. Create a Dashboard with: releases by status (chart), open bugs by tier (chart), upcoming releases on timeline, and a compliance scorecard showing % of releases passing all gates."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ReleaseGuard — Compliance & Calendar Agent
**Agent Purpose:** Ensures every release passes compliance gates and respects the academic calendar before promotion to production.

**Triggers:**
- Status change: When any release moves toward "Staging" or "Production"
- Date-based: Daily check of releases scheduled within the next 7 days
- Item creation: When a new Tier 1 bug is filed
- Schedule: Weekly release readiness digest every Thursday

**Actions:**
- Blocks environment promotion if FERPA, accessibility, or security gates are incomplete — creates checklist of missing items
- Cross-references release target dates against the academic calendar (finals, enrollment, commencement) and warns if conflict detected
- Generates release notes draft by aggregating feature descriptions and bug fixes from linked items
- Escalates Tier 1 bugs to CTO and creates incident response timeline
- Sends faculty/student impact assessment for releases affecting LMS during active courses
- Archives release retrospective data for continuous improvement metrics

**Data Required:**
- Release Pipeline board (all columns)
- Bug Tracker board (severity, status, system)
- Academic calendar (integration or reference board)
- GitHub/GitLab integration for PR and build status
- Help desk system for post-release incident correlation

**Autonomy Level:** Escalation-Based
ReleaseGuard autonomously enforces calendar and compliance gates (hard blocks). For judgment calls — like whether a Tier 2 bug warrants delaying a release — it escalates to the Release Manager with a recommendation and supporting data.

**Example Interaction:**
> It's Thursday afternoon. ReleaseGuard runs its weekly readiness check and finds Release v4.2 is scheduled for next Tuesday — but next Tuesday is the first day of Spring midterms. ReleaseGuard immediately flags the conflict: "⚠️ Release v4.2 targets March 3 — Midterm Exam Week begins. Recommend rescheduling to March 10 (post-midterms). 2 of 3 compliance gates are approved; Security Scan still pending." The Release Manager sees the alert, agrees to push the date, and ReleaseGuard automatically updates the timeline and notifies all stakeholders.

---

### Use Case 3: Research Computing Project Portfolio

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Research universities manage hundreds of concurrent funded research projects, many requiring custom computing infrastructure, data pipelines, or specialized software development. The Office of Research, individual PIs (Principal Investigators), and central IT all have overlapping needs but disconnected tracking. Grant-funded projects have strict reporting requirements (NSF, NIH, DOE) including how computing resources are allocated. PIs submit ad-hoc requests via email; IT teams lose track of commitments; and when grant reporting season arrives, no one can easily show how development hours mapped to funded projects.

#### The Solution
monday.com Work Management as a Research Computing Portfolio hub: **Grant-Linked Project Board** connecting each development effort to its funding source, PI, and reporting deadlines. **Resource Allocation Board** showing developer time allocation across projects with capacity planning. **Infrastructure Request Board** for HPC (High-Performance Computing) cluster provisioning, data storage, and cloud resource requests. Dashboards provide the Office of Research with real-time views of resource utilization by grant, enabling accurate effort reporting to federal agencies.

#### The Outcome
- Accurate grant effort reporting generated in minutes instead of weeks of manual reconstruction
- 35% improvement in developer utilization through visible capacity planning
- PI satisfaction increases as request status becomes transparent
- Audit-ready documentation of computing resource allocation by funding source

#### Discovery Questions
1. "When NSF or NIH asks for a progress report on computing resource utilization for a funded project, how do you compile that data?"
2. "How do PIs currently request development support or computing resources — and how long does it typically take to fulfill those requests?"
3. "Do you have visibility into how your development team's time is split across grant-funded vs. institutional projects?"
4. "Have you ever had a grant audit where you couldn't easily document how computing resources were allocated?"
5. "How many concurrent research computing projects is your team supporting right now, and is that number growing?"

#### Industry Context
Federal grant compliance (2 CFR 200 - Uniform Guidance) requires institutions to track effort and resource allocation with precision. NSF requires annual project reports; NIH has quarterly progress reporting for large grants. PIs operate with significant autonomy — they control their grant budgets and expect responsive service. HPC clusters, research data storage (petabyte-scale), and cloud computing (AWS GovCloud, Azure for Research) are common infrastructure. IRB (Institutional Review Board) approval may be needed if research computing touches human subjects data.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Research Computing Project Portfolio. Board 1 — 'Research Projects': columns for Project Title (text), Principal Investigator (people), Co-PIs (people), Funding Agency (dropdown: NSF, NIH, DOE, DOD, Private Foundation, Institutional, Unfunded), Grant Number (text), Grant Period (timeline), Total Award (numbers with $), Computing Budget Allocation (numbers with $), Status (status: Proposal, Active, No-Cost Extension, Closeout, Archived), Next Report Due (date), Compliance Status (status: Current, Due Soon, Overdue), and Development Effort (connect to Resource Board). Board 2 — 'Resource Allocation': columns for Developer (people), Project Assignment (connect to Research Projects), Week Of (date), Hours Allocated (numbers), Hours Actual (numbers), Task Description (text), Billable to Grant (checkbox), and Effort Category (dropdown: Software Development, Data Pipeline, Infrastructure, Consulting, Documentation). Board 3 — 'Infrastructure Requests': columns for Request Title (text), Requesting PI (connect to Research Projects), Type (dropdown: HPC Cluster Time, Cloud Resources, Data Storage, GPU Allocation, Software License, Custom Development), Specifications (long text), Priority (status: Urgent - Grant Deadline, High, Standard, Low), Status (status: Submitted, Under Review, Provisioning, Active, Decommissioned), and Monthly Cost (numbers with $). Add automations: when Next Report Due is within 14 days, notify PI and research computing lead; when an Infrastructure Request is submitted, auto-assign to the infrastructure team lead. Create a Dashboard with: active projects by funding agency (chart), developer hours by project (chart), infrastructure costs by grant (chart), and upcoming report deadlines (calendar widget)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** GrantTrack — Research Effort Reporter
**Agent Purpose:** Automatically compiles grant-compliant effort and resource utilization reports from project and time tracking data.

**Triggers:**
- Date-based: 21 days before each grant report deadline
- On-demand: When a PI or research administrator requests an effort summary
- Status change: When a project moves to "Closeout" (triggers final report compilation)
- Schedule: Monthly summary of computing resource utilization across all grants

**Actions:**
- Compiles developer effort hours by grant, formatted per agency requirements (NSF, NIH templates)
- Flags discrepancies between allocated and actual effort (e.g., developer billed 40 hours to a grant but only 20 hours of tasks logged)
- Generates infrastructure cost allocation reports broken down by grant number
- Sends draft report to PI for review and approval before submission
- Archives finalized reports with timestamps for audit readiness
- Alerts when a grant is approaching its computing budget ceiling (80% threshold)

**Data Required:**
- Research Projects board (grant numbers, periods, budgets)
- Resource Allocation board (actual hours, task descriptions)
- Infrastructure Requests board (costs, allocation)
- Grant agency reporting templates (configured per agency)
- University fiscal calendar for cost period alignment

**Autonomy Level:** Human-in-the-Loop
GrantTrack drafts all reports autonomously but requires PI sign-off before finalization. Budget threshold alerts are sent automatically. Any discrepancies are flagged for human review — never auto-corrected.

**Example Interaction:**
> Dr. Chen's NSF grant (Award #2345678) has its annual report due in 3 weeks. GrantTrack compiles the data: 4 developers contributed 1,847 hours across the year (development of a genomics data pipeline), HPC cluster usage totaled $47,200, and cloud storage for the research dataset cost $12,800. GrantTrack notices that one developer logged 200 hours to the project but only 160 hours have task descriptions — it flags this for Dr. Chen: "40 hours on this grant lack task documentation. Please have Dr. Vasquez add descriptions before I finalize the NSF report." Dr. Chen forwards the note, descriptions are added, and GrantTrack produces a clean report matching NSF's required format.

---

### Use Case 4: Accessibility Compliance Program Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Every digital product a university creates or procures must meet WCAG 2.1 AA accessibility standards (Section 508 compliance, and increasingly ADA Title II requirements). With dozens of web properties, mobile apps, and third-party integrations, accessibility testing is a massive, ongoing effort. Most universities have 1-2 dedicated accessibility specialists trying to cover hundreds of digital assets. Audit backlogs stretch months. When a student files an OCR (Office for Civil Rights) complaint, the scramble to remediate is painful, expensive, and public.

#### The Solution
monday.com Work Management as an Accessibility Program hub: **Digital Asset Inventory Board** cataloging every web property, app, and tool with its current audit status and VPAT (Voluntary Product Accessibility Template) rating. **Audit Workflow Board** tracking each accessibility audit from scoping through testing, remediation, and re-testing. **Remediation Tracker** connecting issues found to development sprints. Automations schedule recurring re-audits and escalate overdue remediations. Dashboards give the university's ADA/504 coordinator real-time portfolio visibility.

#### The Outcome
- Complete inventory of digital assets with accessibility status (often a first for the institution)
- 50% reduction in audit cycle time through structured workflow replacing ad-hoc processes
- Proactive remediation reduces OCR complaint risk
- Accreditation evidence: documented, systematic approach to digital accessibility

#### Discovery Questions
1. "How many digital properties does the university maintain — websites, apps, LMS integrations — and do you have a complete inventory?"
2. "What happens today when a student or faculty member reports an accessibility barrier? How long does remediation take?"
3. "Have you ever had an OCR complaint or a state audit related to digital accessibility?"
4. "How do you currently track which third-party tools have current VPATs?"
5. "Is your accessibility team able to keep up with the audit backlog, or are some properties going years without review?"

#### Industry Context
The DOJ's 2024 ADA Title II ruling explicitly requires public universities to meet WCAG 2.1 AA. Private institutions face similar requirements under Section 504 and institutional policy. VPATs (Voluntary Product Accessibility Templates) are the standard format for vendors to report accessibility compliance. OCR complaints can result in resolution agreements mandating systemic changes with federal oversight. Common testing tools include WAVE, axe, JAWS, NVDA, and VoiceOver. The EDUCAUSE accessibility community and the IAAP (International Association of Accessibility Professionals) set best practices.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Digital Accessibility Compliance Program. Board 1 — 'Digital Asset Inventory': columns for Asset Name (text), URL (text), Type (dropdown: Website, Web Application, Mobile App, LMS Integration, Third-Party Tool, Kiosk/Digital Signage), Owner Department (dropdown: list of university departments), Product Owner (people), Last Audit Date (date), Next Audit Due (date), WCAG Level (status: Not Assessed, A, AA, AAA, Non-Compliant), VPAT Available (status: Current, Outdated, Missing, N/A - Internal), Critical Issues Count (numbers), and Risk Level (status: Low, Medium, High, Critical). Board 2 — 'Audit Workflow': columns for Asset Being Audited (connect to Inventory), Auditor (people), Audit Type (dropdown: Full WCAG 2.1, Partial - New Features, VPAT Review, User Complaint Investigation), Start Date (date), Target Completion (date), Status (status: Scoping, Testing, Report Draft, Remediation Plan, Re-Testing, Closed), Issues Found (numbers), Critical Issues (numbers), and Remediation Deadline (date). Board 3 — 'Remediation Tracker': columns for Issue Description (text), WCAG Criterion (text, e.g., '1.4.3 Contrast'), Severity (status: Critical - Blocks Access, Major - Significant Barrier, Minor - Inconvenience), Source Audit (connect to Audit Workflow), Assigned Developer (people), Sprint (dropdown), Status (status: Open, In Fix, Verification, Closed, Accepted Risk), and Affected Users (dropdown: Screen Reader Users, Keyboard Only, Low Vision, Cognitive, Motor). Add automations: when Next Audit Due is within 30 days, create a new item on Audit Workflow and notify the accessibility lead; when a Critical issue is open for more than 14 days, escalate to the CIO. Create a Dashboard with: asset inventory by WCAG level (pie chart), audit pipeline timeline, open remediation by severity (chart), and overdue items list."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** A11yWatch — Accessibility Compliance Monitor
**Agent Purpose:** Proactively monitors digital asset accessibility status and ensures remediation stays on track.

**Triggers:**
- Schedule: Weekly scan of all digital assets approaching audit due dates
- Status change: When any remediation item has been "Open" for more than 10 days
- Item creation: When a new accessibility complaint is filed
- Date-based: Monthly compliance summary for ADA/504 coordinator

**Actions:**
- Sends audit scheduling reminders with pre-populated scope based on last audit findings
- Escalates critical unremediated issues with impact assessment ("This login page issue affects all 25,000 students using screen readers")
- Generates monthly compliance dashboard report for university leadership
- Tracks VPAT expiration dates for third-party tools and notifies procurement team when renewals need updated VPATs
- Creates remediation task items from audit findings with auto-assigned WCAG criterion tags
- Maintains audit trail documentation formatted for OCR response if needed

**Data Required:**
- Digital Asset Inventory board (all assets, audit dates, WCAG levels)
- Audit Workflow board (findings, timelines)
- Remediation Tracker board (issue status, severity)
- University enrollment data (for impact calculations)
- Vendor VPAT repository

**Autonomy Level:** Escalation-Based
A11yWatch handles all monitoring, reminders, and report generation autonomously. When a critical accessibility issue affects a high-traffic asset (>1,000 daily users), it escalates directly to the CIO with a recommended remediation timeline. All OCR-related actions require human approval.

**Example Interaction:**
> A11yWatch's weekly scan flags that the main university website's WCAG audit expired 45 days ago, and a new complaint was filed by a student using a screen reader who can't navigate the course registration page. A11yWatch immediately: (1) creates an expedited audit item with "User Complaint Investigation" type, (2) pulls the last audit's findings to see if navigation was a known issue (it was — marked "Minor" and deprioritized), (3) escalates to the accessibility lead and CIO: "Prior audit flagged navigation issues as Minor but new complaint suggests impact is greater than assessed. Recommend emergency remediation — this is a registration-critical page during enrollment period." The team fixes the issue in 3 days, and A11yWatch documents the entire timeline for the OCR response file.

---

### Use Case 5: Student-Facing Application Development Pipeline

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Developing student-facing applications (mobile apps, self-service portals, chatbots) requires coordination between UX designers, developers, student affairs stakeholders, and actual students (for usability testing). Many university product teams struggle with the user research → design → development pipeline because feedback loops are slow — students are hard to recruit for testing during busy academic periods, and design decisions get made without adequate student input. The result: apps students don't actually use, wasting scarce development resources.

#### The Solution
monday.com Work Management as the full application development lifecycle hub: **User Research Board** tracking student feedback sessions, usability tests, and survey results. **Design Board** managing UI/UX iterations with file columns for mockups and design system components. **Development Board** with sprint tracking connected to the Research and Design boards so developers always have context on WHY features were specified. Student feedback forms feed directly into the Research board. Dashboards show the pipeline from insight → design → build → launch.

#### The Outcome
- 3× faster user research → implementation cycle
- Student usability test participation tracked and incentive budgets managed in one place
- Design decisions linked to specific student feedback (audit trail)
- App adoption rates increase 25-40% when built on validated student insights

#### Discovery Questions
1. "How do you currently gather student feedback on digital tools — and how does that feedback reach your development team?"
2. "What's the typical time from a UX insight to a shipped feature in your student-facing apps?"
3. "Do your designers and developers work from the same system, or do handoffs happen through separate tools?"
4. "How do you recruit students for usability testing, and do you track participation and incentives?"
5. "What's the adoption rate of your most recent student-facing app or feature launch?"

#### Industry Context
Student demographics and tech expectations vary enormously — community college students skew older and mobile-first; elite research university students expect consumer-grade UX. Student Government Associations (SGAs) often have formal roles in technology governance. Universal Design for Learning (UDL) principles should inform all student-facing development. "Digital equity" is a growing concern — not all students have the same device access. The EDUCAUSE Student Experience project provides benchmark data on student technology expectations.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Student App Development Pipeline. Board 1 — 'User Research': columns for Research Title (text), Research Type (dropdown: Usability Test, Survey, Focus Group, Analytics Review, Accessibility Audit, Contextual Inquiry), Student Segment (dropdown: Undergraduate, Graduate, Online/Distance, International, Transfer, First-Generation), Number of Participants (numbers), Date Conducted (date), Key Findings (long text), Researcher (people), Linked Feature (connect to Design Board), Status (status: Planning, Recruiting, In Progress, Analysis, Complete), and Files (file column for recordings/notes). Board 2 — 'Design Pipeline': columns for Feature Name (text), Research Backing (connect to User Research), Designer (people), Design Phase (status: Wireframe, Mockup, Prototype, User Validation, Final Spec, Handoff), Mockup Files (file column), Accessibility Check (checkbox), Student Approval (status: Pending, Approved, Needs Revision), and Dev Handoff Date (date). Board 3 — 'Development Sprints': columns for Story (text), Design Spec (connect to Design Pipeline), Developer (people), Sprint (dropdown), Story Points (numbers), Status (status: Ready, In Dev, Code Review, QA, UAT with Students, Done), Platform (dropdown: iOS, Android, Web, Cross-Platform), and Launch Date (date). Add automations: when a User Research item is completed, notify the design lead; when Design Phase moves to 'Handoff', create linked item on Development Sprints; when UAT status is set, notify the student testing coordinator. Create a Dashboard with: research pipeline (timeline), design status (chart), sprint burndown (chart), and feature journey from research to launch (connected view)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** StudentVoice — Insight-to-Feature Connector
**Agent Purpose:** Ensures student feedback systematically flows into product decisions and that no research insight gets lost.

**Triggers:**
- Status change: When a User Research item moves to "Complete"
- Schedule: Bi-weekly digest of unlinked research findings (insights not yet connected to features)
- Form submission: When students submit feedback via embedded forms
- Date-based: Start of each semester (reviews what was promised to students vs. delivered)

**Actions:**
- Analyzes completed research findings and suggests which existing features or backlog items they relate to
- Creates design pipeline items from validated research insights with pre-populated context
- Sends semester-start "promise vs. delivery" report comparing features students were told about vs. what shipped
- Tags recurring themes across multiple research studies (e.g., "mobile navigation" mentioned in 4 separate studies)
- Notifies SGA technology committee when student-requested features are shipped

**Data Required:**
- User Research board (findings, segments, status)
- Design Pipeline board (features, research links)
- Development Sprints board (ship dates, status)
- Student feedback form submissions
- Prior semester feature announcements

**Autonomy Level:** Fully Autonomous
StudentVoice operates independently for analysis, synthesis, and notifications. It does not make prioritization decisions — it surfaces patterns and connections for product managers to act on.

**Example Interaction:**
> Three separate usability studies over the past semester all mention difficulty finding financial aid status on the student portal. StudentVoice identifies the pattern: "📊 'Financial aid visibility' appears as a pain point in 3/5 recent studies across Undergraduate, Graduate, and First-Generation segments. No current backlog item addresses this. Recommend creating a feature request." It auto-creates a Design Pipeline item titled "Financial Aid Status — Improved Visibility" with links to all three research studies and a summary of specific student quotes. The product manager reviews it Monday morning and fast-tracks it into the next sprint.

---

### Use Case 6: Technical Debt & Legacy System Modernization Tracking

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Universities are notorious for technical debt — legacy systems built on aging frameworks (classic ASP, ColdFusion, aging Java EE) that are maintained by a single developer who "knows where all the bodies are buried." When that person retires or leaves, institutional knowledge vanishes. Meanwhile, modernization efforts compete with new feature requests for the same scarce developer hours. Without a structured approach to tracking and prioritizing technical debt, institutions lurch from crisis to crisis — patching 15-year-old integrations instead of building modern solutions.

#### The Solution
monday.com Work Management with a dedicated **Technical Debt Registry Board**: each legacy system cataloged with age, maintainer, risk score, and modernization plan. **Modernization Roadmap Board** connecting debt items to funded modernization projects. Risk scoring formula weighs factors like: single maintainer (bus factor), years since last major update, compliance gaps, and number of dependent systems. Dashboards visualize the institution's overall technical health portfolio for CIO-level conversations.

#### The Outcome
- Complete inventory of technical debt with quantified risk scores for the first time
- Data-driven modernization prioritization replaces "whoever yells loudest"
- "Bus factor" risks identified and mitigated through cross-training plans linked to each system
- CIO can present a multi-year modernization business case backed by real data

#### Discovery Questions
1. "If your longest-tenured developer left tomorrow, which systems would be at risk?"
2. "How many systems in your portfolio are running on frameworks or platforms that are end-of-life or approaching it?"
3. "How do you currently decide which legacy systems to modernize first?"
4. "What percentage of your development team's time goes to maintaining existing systems vs. building new capabilities?"
5. "Has a legacy system failure ever disrupted a critical university process like enrollment, grading, or financial aid disbursement?"

#### Industry Context
Common legacy systems in higher ed: Banner (Ellucian) for ERP/SIS, PeopleSoft, Colleague (Datatel), homegrown registration systems, aging content management systems. "ERP modernization" is a top-5 priority at most institutions — and a multi-year, multi-million dollar effort. The shift to cloud-native and SaaS reduces some debt but creates new integration challenges. Student data migrations between legacy and modern systems are extraordinarily complex due to historical data spanning decades.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Technical Debt & Modernization Tracker. Board 1 — 'Technical Debt Registry': columns for System Name (text), Description (long text), Primary Technology (dropdown: Java EE, .NET Framework, ColdFusion, Classic ASP, PHP 5.x, Python 2.x, COBOL, PL/SQL, Custom Scripting, Modern - No Debt), Year Deployed (numbers), Primary Maintainer (people), Backup Maintainer (people), Bus Factor (formula: if Backup is empty then 'CRITICAL - Single Person' else 'Covered'), Dependent Systems Count (numbers), Last Major Update (date), Years Since Update (formula), Data Sensitivity (dropdown: FERPA - Student PII, Financial - GLBA, Research - IRB, Public Only), Compliance Gaps (long text), Risk Score (formula combining bus factor, age, dependencies, sensitivity — scale 1-100), and Modernization Status (status: Not Planned, Assessment, Funded, In Progress, Complete, Accepted Risk). Board 2 — 'Modernization Roadmap': columns for Project Name (text), Legacy System (connect to Debt Registry), Target Architecture (dropdown: Cloud-Native SaaS, Microservices, API-First Rebuild, Vendor Migration, Wrapper/Integration, Retirement), Estimated Effort (dropdown: Small < 500hrs, Medium 500-2000hrs, Large 2000-5000hrs, XL > 5000hrs), Funding Source (dropdown: IT Operating, Capital Project, Grant-Funded, Vendor Partnership, Unfunded), Project Lead (people), Status (status: Planning, In Progress, Testing, Migration, Post-Migration Support, Complete), and Timeline (timeline). Add automations: when Risk Score exceeds 75, notify CIO and tag as 'Critical Risk'; when Primary Maintainer changes and Backup is empty, set Bus Factor alert. Create a Dashboard with: risk score distribution (chart), systems by technology age (chart), modernization roadmap (timeline), and bus factor alerts (filtered list of Critical items)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DebtHunter — Technical Risk Intelligence Agent
**Agent Purpose:** Continuously monitors the institution's technical debt portfolio and alerts leadership to emerging risks before they become crises.

**Triggers:**
- HR integration: When a developer listed as Primary or Backup Maintainer submits a resignation or retirement notice
- Schedule: Monthly risk score recalculation across all systems
- Status change: When a dependent system has an outage (flags all connected legacy systems)
- Date-based: Annual comprehensive risk review for CIO's technology plan

**Actions:**
- Recalculates risk scores monthly incorporating new data (outages, maintainer changes, new compliance requirements)
- When a maintainer departure is detected, immediately generates a knowledge transfer plan and cross-training timeline
- Creates "what if" scenario analyses: "If System X goes down, here are the 7 systems affected and estimated recovery time"
- Generates annual technical debt report for CIO with total estimated modernization cost and recommended priority sequence
- Flags when vendor end-of-support dates approach for underlying platforms (e.g., ColdFusion EOL announcements)

**Data Required:**
- Technical Debt Registry (all columns)
- Modernization Roadmap (project status, timelines)
- HR system integration (employee status changes)
- Incident management system (outage history)
- Vendor support lifecycle databases

**Autonomy Level:** Escalation-Based
DebtHunter operates autonomously for monitoring and analysis. Maintainer departure alerts go directly to the CIO and affected project leads. Modernization recommendations require human decision-making.

**Example Interaction:**
> DebtHunter's monthly scan detects that the legacy student billing integration — a ColdFusion application from 2009 with a risk score of 89 — just lost its backup maintainer (transferred to another department). The primary maintainer is 2 years from retirement. DebtHunter escalates: "🚨 Student Billing Integration risk score increased from 78 to 95. Now single-maintainer with retirement timeline. This system feeds Financial Aid, Bursar, and Housing. Recommend: (1) immediate cross-training plan — estimated 160 hours, (2) fund modernization assessment in Q3, (3) document all integration points now while institutional knowledge is available." The CIO reviews and approves all three recommendations in the next IT leadership meeting.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| LMS | Learning Management System — platform for course content delivery (Canvas, Blackboard, Brightspace, Moodle) |
| SIS | Student Information System — core system for enrollment, grades, transcripts (Banner, PeopleSoft, Colleague) |
| LTI | Learning Tools Interoperability — standard for integrating external tools with an LMS |
| FERPA | Family Educational Rights and Privacy Act — federal law protecting student education records |
| HECVAT | Higher Education Community Vendor Assessment Toolkit — standardized security/privacy questionnaire for vendors |
| WCAG | Web Content Accessibility Guidelines — international standard for web accessibility |
| VPAT | Voluntary Product Accessibility Template — vendor document reporting Section 508/WCAG compliance |
| HPC | High-Performance Computing — clustered computing resources for research workloads |
| PI | Principal Investigator — lead researcher on a funded grant project |
| IRB | Institutional Review Board — committee overseeing research involving human subjects |
| OCR | Office for Civil Rights (US Dept of Education) — enforces disability and civil rights in education |
| R1/R2 | Carnegie Classification designating "very high" or "high" research activity universities |
| ERP | Enterprise Resource Planning — institution-wide administrative system (Banner, PeopleSoft) |
| EDUCAUSE | Primary professional association for higher education IT leaders |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Information Officer (CIO) | Overall technology strategy and budget | Decision-maker |
| VP for Information Technology | Operational oversight of IT organization | Decision-maker |
| Director of Enterprise Applications | Manages SIS, ERP, LMS platforms | Decision-maker for core systems |
| Director of Research Computing | Manages HPC, research infrastructure | Decision-maker for research IT |
| Product Manager (Digital Experiences) | Owns student-facing digital product roadmap | Influencer / Recommender |
| Application Development Manager | Leads development teams | Influencer |
| UX/Accessibility Lead | Ensures digital experiences meet standards | Influencer / Gate-keeper |
| IT Governance Committee Chair (often Provost or VP) | Approves strategic technology investments | Decision-maker |
| Faculty Technology Committee | Represents faculty interests in tech decisions | Influencer (veto power on pedagogy) |
| Student Government Technology Rep | Student voice in technology planning | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| IT Operations | Runs infrastructure that Product builds on | Infrastructure management, incident tracking |
| Enrollment Management | Primary consumer of student-facing applications | CRM for admissions, enrollment funnel tracking |
| Academic Affairs | Drives pedagogical technology requirements | Curriculum planning, faculty support workflows |
| Student Affairs | Owns student experience outside classroom | Student engagement platforms, housing management |
| Office of Research | Funds and oversees research computing | Grant management, compliance reporting |
| Finance & Administration | Budget approval and procurement | Vendor management, license tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Jira / Atlassian Suite | De facto standard for software development in higher ed IT | monday.com Dev offers simpler onboarding, better cross-functional visibility (non-technical stakeholders can actually use it), and eliminates the Jira-for-devs + Trello-for-PMs split |
| ServiceNow | IT Service Management expanding into project management | monday.com is more agile, lower cost, faster to configure; ServiceNow's strength is ITSM, not product development |
| Smartsheet | Popular in PMO and project-oriented university teams | monday.com offers superior automation, integrations, and the AI/agents roadmap that Smartsheet lacks |
| Asana | Used by some smaller university teams for task management | monday.com's multi-product platform (Work, Dev, CRM, Service) provides broader value across the institution |
| GitHub Projects | Basic project management for dev teams already on GitHub | monday.com provides the governance, portfolio, and stakeholder layers that GitHub Projects completely lacks |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Jira for our development work." | "Jira is great for your developers, but how do your governance committees, PIs, and department stakeholders get visibility? monday.com gives your technical team the dev workflow they need while giving stakeholders a view they can actually understand — without maintaining two systems." |
| "We're locked into our ERP vendor's project tools." | "ERP-bundled tools are designed for ERP workflows, not product development. monday.com integrates with Banner/PeopleSoft via APIs while giving your product teams a modern, flexible workspace. Many universities use both." |
| "Our budget is controlled by committee — we can't move fast on new tools." | "That's exactly why centralized visibility matters. monday.com gives your governance committee real-time portfolio data instead of stale PowerPoints. We've seen committees make faster, more confident decisions when they have a live dashboard. The tool actually accelerates your governance process." |
| "FERPA compliance concerns with cloud tools." | "monday.com provides enterprise security controls, SOC 2 Type II compliance, data residency options, and role-based access that maps to FERPA requirements. We can complete your HECVAT assessment and work with your CISO on data handling protocols." |
| "We have student workers who change every semester." | "monday.com's intuitive interface means new student workers get productive in hours, not weeks. Automations capture institutional knowledge in the workflow itself — when a student worker leaves, the process knowledge stays." |

## Proof Points
*(To be populated with customer references)*
- [University with large EdTech team using monday.com for product development]
- [Research university using monday.com for cross-departmental project portfolio]
- [Institution that consolidated from Jira + Trello + Smartsheet to monday.com]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
