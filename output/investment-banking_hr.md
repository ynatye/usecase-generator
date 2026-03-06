# Investment Banking × HR Playbook

## Overview

Human Resources in investment banking operates under extraordinary pressure. The talent market for analysts, associates, VPs, directors, and managing directors is fiercely competitive, with top-tier banks like Goldman Sachs, Morgan Stanley, and JP Morgan constantly vying for the same pool of elite candidates from target schools. HR teams must manage grueling recruiting cycles (often beginning 18+ months before start dates), navigate complex compensation structures involving base salary, signing bonuses, stub bonuses, and year-end bonuses, and maintain compliance with regulations from FINRA, the SEC, the FCA, and other global financial regulators.

The organizational structure of an investment banking HR function typically includes specialized teams for campus recruiting, lateral hiring, compensation & benefits, learning & development (training programs, licensing/exam support), employee relations, and HRIS/people analytics. Headcounts range from 50-200+ HR professionals at bulge bracket firms supporting 5,000-50,000+ employees globally. HR must also manage the unique cultural dynamics of investment banking: 80-100 hour work weeks, high attrition (especially at the analyst-to-associate promote-or-leave inflection point), and increasing scrutiny around diversity, mental health, and work-life balance following high-profile incidents.

Regulatory burden is immense. Every banker must maintain FINRA Series 7, 63, and 79 licenses (in the US), undergo annual compliance training, complete mandatory continuing education, and be subject to background checks, U5 filings, and outside business activity (OBA) disclosures. HR is the operational backbone ensuring none of these lapse, which can result in regulatory action, fines, or reputational damage. The cost of a mis-hire at the VP+ level can exceed $1M when factoring in recruiter fees (typically 25-33% of first-year comp), onboarding time, and lost deal flow.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Campus recruiting coordination, onboarding logistics, and compliance tracking consume massive HR headcount that AI can dramatically reduce |
| 2 | Scale Impact Without Overhead | High | Managing global licensing, training, and performance reviews across thousands of bankers without proportional HR growth |
| 3 | Consolidate Tech Stack with AI | Medium-High | Banks use fragmented stacks (Workday, Greenhouse, SAP SuccessFactors, custom spreadsheets) that can be unified |

## Prioritized Use Cases

---

### Use Case 1: Campus Recruiting Command Center

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banks run campus recruiting programs targeting 20-50 "core" and "target" schools, managing thousands of applicants for a few hundred analyst seats. The process involves campus presentations, coffee chats, superdays (multi-round interview days), and offer management — all coordinated across recruiting teams, division heads, and interview panels. Recruiters spend 60%+ of their time on logistics: scheduling superdays, tracking candidate status across rounds, coordinating interviewer availability, and managing diversity pipeline metrics. A single superday for one division at one bank can involve 200+ candidates, 50+ interviewers, and 400+ individual interviews in a single day. Most banks still coordinate this via email chains and Excel trackers.

#### The Solution
monday.com Work Management as the central recruiting operations hub. Build a multi-board system: **Candidate Pipeline Board** (columns: Name, School, Division Preference, GPA, Status [Applied → Phone Screen → Superday → Offer → Accepted/Declined], Interviewer Assignments, Diversity Tags, Offer Details). **Superday Scheduling Board** (columns: Date, Division, Location, Interview Slots, Interviewer Names, Room Assignments, Candidate Assignments). **School Coverage Board** (columns: School Name, Tier, Event Dates, Campus Ambassadors, Application Volume, Conversion Rate). Use automations to move candidates through stages, notify interviewers of assignments, and flag scheduling conflicts. Dashboard views for real-time pipeline metrics, diversity breakdowns, and school-level conversion funnels.

#### The Outcome
Reduce campus recruiting coordination effort by 40-50%. Eliminate double-booking of interviewers during superdays. Real-time visibility into pipeline diversity metrics (historically compiled manually for quarterly reports). Faster offer turnaround — critical when competing banks make exploding offers within 24-48 hours.

#### Discovery Questions
- How many target schools do you recruit from, and how do you currently track candidate flow from each school through your pipeline?
- Walk me through your superday logistics — who coordinates interviewer assignments and how far in advance?
- How do you currently report on diversity metrics across your recruiting pipeline? Is it real-time or compiled quarterly?
- When a competing bank makes an offer to a candidate you're also pursuing, how quickly can you mobilize a counter-offer decision?
- What's your current tech stack for campus recruiting — ATS, scheduling tools, spreadsheets?

#### Industry Context
"Superday" is the investment banking term for final-round interviews, typically held on-site. "Target school" and "core school" refer to universities from which a bank actively recruits (e.g., Wharton, Harvard, Princeton for bulge brackets). "Exploding offers" are time-limited offers (24-72 hours) designed to pressure candidates into accepting before hearing from competitors. The recruiting cycle has shifted earlier — many banks now recruit rising juniors (sophomores) for summer analyst positions, meaning the pipeline is almost continuous year-round.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Campus Recruiting Command Center for an investment bank. Create three connected boards:
>
> Board 1 — 'Candidate Pipeline': Columns: Candidate Name (text), School (dropdown: Wharton, Harvard, Stanford, Columbia, NYU Stern, MIT, Princeton, Yale, Duke, Chicago Booth, other), Division Preference (dropdown: IBD, S&T, Research, AM, PWM), GPA (number), Status (status: Applied, Phone Screen Scheduled, Phone Screen Complete, Superday Invited, Superday Complete, Offer Extended, Offer Accepted, Offer Declined, Rejected), Recruiter Assigned (people), Diversity Tags (dropdown: Gender, URM, LGBTQ+, Veteran, First-Gen, None), Interview Score (number 1-5), Offer Amount (number), Notes (long text). Groups by: Division.
>
> Board 2 — 'Superday Scheduler': Columns: Superday Date (date), Division (dropdown: IBD, S&T, Research, AM, PWM), Location (dropdown: NYC HQ, London, Hong Kong, SF), Time Slot (text), Interviewer (people), Room (text), Candidate (connect to Board 1), Interview Type (dropdown: Technical, Behavioral, Case Study, Fit), Score (number). Groups by: Superday Date.
>
> Board 3 — 'Target School Tracker': Columns: School Name (text), Tier (status: Target, Core, Emerging), Region (dropdown: Northeast, Southeast, Midwest, West Coast, International), Campus Ambassador (people), Info Session Date (date), Application Deadline (date), Apps Received (number), Superday Invites (number), Offers Made (number), Offers Accepted (number), Conversion Rate (formula). Groups by: Tier.
>
> Automations: When Candidate Pipeline Status changes to 'Superday Invited', notify Recruiter Assigned. When Interview Score is entered on Superday Scheduler, update Candidate Pipeline Interview Score. When Status changes to 'Offer Accepted', create item in a 'New Hire Onboarding' board.
>
> Dashboard: Pipeline funnel chart (Applied → Accepted), Diversity breakdown pie chart, School conversion rate table, Division capacity vs. offers bar chart, Superday fill rate."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SuperdayOps Agent
**Agent Purpose:** Automatically coordinate superday logistics by matching candidates to interviewers based on division, availability, and diversity goals.

**Triggers:**
- Candidate status changes to "Superday Invited" on Pipeline Board
- New superday date created on Scheduler Board
- Interviewer marks themselves unavailable (status change)
- 48 hours before a superday date (scheduled)
- Manual trigger by recruiting coordinator

**Actions:**
- Auto-assign candidates to interview time slots based on division preference and interviewer availability
- Generate optimized interview schedules avoiding back-to-back slots for interviewers with conflicts
- Send calendar invites and prep packets to interviewers (candidate resume, interview guide, scorecard link)
- Flag scheduling conflicts and suggest alternatives
- Generate post-superday summary: scores by candidate, interviewer feedback completion rate, diversity pipeline metrics
- Escalate to recruiting lead when offer-decision deadline is <24 hours and feedback is incomplete

**Data Required:**
- Candidate Pipeline Board (candidate details, division, scores)
- Superday Scheduler Board (dates, slots, rooms)
- Interviewer calendar integration (Google Calendar/Outlook)
- Historical interview score data for calibration

**Autonomy Level:** Human-in-the-Loop
Scheduling assignments are auto-generated but require recruiting coordinator approval. Offer decisions always escalate to division heads. Diversity flagging is automatic but recommendations are advisory.

**Example Interaction:**
> The SuperdayOps Agent detects that 45 candidates have been moved to "Superday Invited" for the March 15th IBD superday in NYC. It cross-references interviewer availability from Outlook calendars and finds that 12 of 18 assigned MDs and VPs are available. It generates a draft schedule with 5 interview rounds per candidate across 3 rooms, flags that 2 interviewers have conflicts with a live deal closing, and suggests 2 alternates from the approved interviewer pool. The agent sends the draft schedule to the recruiting coordinator for approval, noting that the current candidate pool is 38% female (above the 35% target) and 22% URM (below the 25% target), recommending the team revisit 3 waitlisted URM candidates from the phone screen round. Once approved, it sends personalized calendar blocks and prep packets to all interviewers with candidate resumes and division-specific technical question banks.

---

### Use Case 2: FINRA Licensing & Compliance Tracker

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every registered representative at an investment bank must maintain active FINRA licenses (Series 7, 63, 79 for bankers; Series 3, 7, 55, 57 for traders). These require continuing education (CE) — both a Regulatory Element (computer-based training within 120 days of the 2nd, 5th, and 10th registration anniversaries) and a Firm Element (annual firm-designed training). Failure to complete CE on time triggers automatic license suspension, meaning the individual cannot legally conduct business. For a bank with 5,000 registered reps, tracking expiration dates, CE completion, and license status across multiple regulatory bodies (FINRA, SEC, FCA, MAS, SFC) is a massive operational burden. Many banks rely on compliance teams manually pulling reports from FINRA's Web CRD system and cross-referencing spreadsheets — a process prone to errors that can result in regulatory fines ($10K-$100K+ per violation) and reputational damage.

#### The Solution
monday.com Work Management as a centralized licensing compliance dashboard. **Licensing Board** with columns: Employee Name, Employee ID, Division, Registration Type (dropdown: Series 7, 63, 79, 24, 3, 55, 57, SIE), Registration Date, CE Regulatory Due Date (date, auto-calculated), CE Firm Element Due Date (date), CE Status (status: Current, Due Soon, Overdue, Suspended), Manager (people), Last Completion Date. Automations: 90-day, 60-day, 30-day, and 7-day advance notifications to employees and their managers. Status auto-changes to "Overdue" if completion date passes. Escalation to compliance officer if status remains "Overdue" for 48 hours. Dashboard showing compliance rates by division, upcoming expirations heat map, and historical completion trends.

#### The Outcome
Zero licensing lapses (from an average of 5-15 per year at mid-size banks). Eliminate 2-3 FTEs worth of manual tracking effort. Real-time compliance posture visible to Chief Compliance Officer. Audit-ready reporting generated in seconds instead of days.

#### Discovery Questions
- How many registered representatives do you have across all regulatory bodies, and who currently tracks their CE deadlines?
- Have you experienced any licensing lapses in the past 24 months? What was the cost — fines, business disruption, or both?
- How do you currently pull data from Web CRD, and how often do you reconcile it against your internal records?
- When a banker transfers between divisions (e.g., from S&T to IBD), how do you manage the licensing transition and new registration requirements?
- What's your process for the annual Firm Element training — design, distribution, tracking, and attestation?

#### Industry Context
Web CRD (Central Registration Depository) is FINRA's online system for managing broker-dealer registration. The Regulatory Element of CE is mandated by FINRA and delivered through a standardized computer-based program. The Firm Element is designed by each firm and must be tailored to the firm's products, services, and regulatory issues. A U5 filing is submitted when a registered rep leaves a firm, and any compliance issues are permanently recorded. Series 79 is specifically for investment banking representatives (required since 2009).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a FINRA Licensing & Compliance Tracker for an investment bank. Create a board called 'Licensing Compliance':
>
> Columns: Employee Name (text), Employee ID (text), Division (dropdown: IBD, S&T, Equity Research, Asset Management, Wealth Management, Operations, Compliance), Registration Type (dropdown: SIE, Series 3, Series 7, Series 24, Series 55, Series 57, Series 63, Series 66, Series 79, FCA Approved Person, MAS Licensed Rep), Registration Date (date), CE Regulatory Due Date (date), CE Firm Element Due Date (date), Completion Status (status: Current, Due in 90 Days, Due in 30 Days, Overdue, Suspended), Manager (people), Compliance Officer (people), Last CE Completion (date), Notes (long text).
>
> Groups: By Division (IBD, S&T, Research, AM, WM, Ops).
>
> Automations: When CE Regulatory Due Date is 90 days away, change Completion Status to 'Due in 90 Days' and notify employee. When 30 days away, change to 'Due in 30 Days' and notify employee + manager. When date passes without completion, change to 'Overdue' and notify Compliance Officer. When Overdue for 5 days, change to 'Suspended' and notify division head.
>
> Dashboard: Compliance rate gauge (% Current across all reps), Overdue items list widget, Upcoming expirations timeline (next 90 days), Division compliance comparison bar chart, Registration type breakdown pie chart."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ComplianceGuard Agent
**Agent Purpose:** Proactively monitor licensing compliance, predict at-risk employees, and automate CE completion follow-up.

**Triggers:**
- Daily scheduled scan of all licensing records at 6:00 AM
- Employee CE Regulatory Due Date enters 120-day window
- New employee added to Licensing Board (new hire or lateral transfer)
- Status changes to "Overdue"
- Quarterly compliance review date

**Actions:**
- Send personalized CE reminder emails with direct links to FINRA CE portal and estimated completion time
- Escalate overdue items through management chain (employee → manager → division head → CCO)
- Generate quarterly compliance report with risk scores by division
- Flag employees transferring divisions who need new registrations
- Create pre-populated U5 filing checklist when employee termination is detected
- Predict at-risk employees based on historical late-completion patterns

**Data Required:**
- Licensing Compliance Board
- HRIS integration (employee status, transfers, terminations)
- FINRA Web CRD data feed (if API available)
- Historical CE completion data

**Autonomy Level:** Escalation-Based
Reminders and status updates are fully autonomous. Escalations follow a defined chain. Suspension flags require compliance officer confirmation. U5 filing checklists are generated automatically but reviewed before submission.

**Example Interaction:**
> At 6:00 AM on Monday, the ComplianceGuard Agent scans 4,200 registered representative records. It identifies 23 employees whose CE Regulatory Element is due within 30 days, including 2 Managing Directors in IBD who have historically completed their CE in the final week. The agent sends tailored reminders: "Your Series 79 CE is due March 15. Based on your schedule, I recommend completing it this week — the module takes approximately 2 hours. [Link to FINRA CE portal]." For the 2 MDs flagged as at-risk, it also notifies their executive assistants and the division's compliance liaison. It generates a dashboard update showing IBD at 94% compliance (below the 98% firm target) and includes this in the weekly compliance digest sent to the CCO. When one MD's deadline passes without completion, the agent immediately notifies the CCO, updates the status to "Overdue," and drafts a temporary activity restriction memo pending completion.

---

### Use Case 3: Compensation Cycle Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banking compensation is the single most complex and politically sensitive HR process. Year-end bonus pools are allocated by division, then by group, then by individual — a cascading process involving CEO, COO, division heads, group heads, and HR compensation teams. The process typically runs November through January and involves: revenue attribution (which banker gets credit for which deals), peer rankings (stack ranking within cohorts), market benchmarking (matching competitor comp to retain talent), and final allocation decisions. At a bulge bracket bank, this involves individually pricing 3,000-10,000+ professionals, each with unique base, bonus (cash + deferred), sign-on amortization, and equity vesting schedules. HR comp teams spend 8-12 weeks managing this process through hundreds of spreadsheets emailed between division heads — creating version control nightmares, data leak risks, and audit concerns.

#### The Solution
monday.com Work Management as a secure compensation planning workspace. **Comp Cycle Board** with highly restricted permissions: Employee Name, Title/Level, Division, Group, Base Salary, Target Bonus, Proposed Bonus, Deferred Comp %, Equity Grant, Total Comp, YoY Change %, Peer Rank, Revenue Attribution (number), Manager Recommendation (long text), HR Review Status (status: Pending Manager Input, Under Review, Approved, Communicated). Mirror columns connecting to performance review data. Subitems for historical comp (prior 3 years). Automations for approval workflows: manager submits → HR reviews → division head approves → final sign-off. Locked columns prevent unauthorized edits. Audit trail via activity log. Dashboard showing pool allocation vs. budget, distribution curves, and pay equity analytics.

#### The Outcome
Compress comp cycle from 8-12 weeks to 4-6 weeks. Eliminate spreadsheet version chaos (average bank has 50-100 competing spreadsheet versions during comp season). Real-time pool tracking prevents over-allocation. Pay equity analytics built into the workflow rather than retroactive.

#### Discovery Questions
- How many compensation spreadsheets are typically in circulation during your year-end bonus process, and how do you manage version control?
- Walk me through the approval chain for an individual bonus decision — how many levels of approval, and where do bottlenecks occur?
- How do you currently handle revenue attribution disputes between bankers or groups who both claim credit for a deal?
- What's your process for benchmarking compensation against competitors — do you use McLagan, Heidrick & Struggles, or internal data?
- How do you ensure pay equity across gender and ethnicity during the compensation process? Is it proactive or a retroactive audit?

#### Industry Context
McLagan (now part of Aon) is the dominant compensation benchmarking firm for investment banking. "Deferred comp" refers to the portion of bonus paid in restricted stock or deferred cash that vests over 3-5 years (a post-2008 regulatory requirement). Revenue attribution is the process of assigning deal revenue to specific bankers — a politically charged exercise since bonuses are heavily tied to revenue production. "Street comp" refers to the market rate for a given role/level. Stack ranking places every individual in a cohort from top to bottom, directly influencing bonus allocation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Compensation Cycle Management workspace for an investment bank. Create a board called 'Year-End Comp Planning':
>
> Columns: Employee Name (text), Employee ID (text), Title (dropdown: Analyst 1, Analyst 2, Analyst 3, Associate 1, Associate 2, Associate 3, VP, Director/ED, Managing Director), Division (dropdown: IBD, S&T, Research, AM, PWM), Group (text), Base Salary (number, currency USD), Prior Year Bonus (number, currency), Revenue Attributed (number, currency), Peer Rank (number), Manager Proposed Bonus (number, currency), Deferred Percentage (number, %), Cash Bonus (formula), Deferred Amount (formula), Equity Grant Value (number, currency), Total Comp (formula), YoY Change % (formula), Manager Comments (long text), HR Review (status: Awaiting Manager, Manager Submitted, HR Reviewing, Division Head Review, Approved, Communicated), Reviewer (people).
>
> Groups: By Division, then subgroups by Title.
>
> Automations: When Manager submits (status changes to 'Manager Submitted'), notify HR Reviewer. When HR changes to 'Division Head Review', notify Division Head. When status changes to 'Approved', lock all number columns for that item. When all items in a group reach 'Approved', notify HR lead that division is complete.
>
> Dashboard: Total pool allocated vs. budget (number widget), Comp distribution by title (bar chart), YoY change distribution (chart), Division completion progress (battery widget), Pay equity analysis by gender (chart), Top 10 highest comp items (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CompAnalyst Agent
**Agent Purpose:** Accelerate compensation decisions by providing real-time benchmarking, equity analysis, and anomaly detection during the comp cycle.

**Triggers:**
- Manager submits a bonus recommendation (status change)
- Comp cycle kickoff date (scheduled, annually)
- Revenue attribution data is updated
- HR reviewer requests benchmarking analysis
- Pay equity flag detected (>15% variance within same title/division by demographic)

**Actions:**
- Compare proposed comp against historical data and peer benchmarks, flag outliers (>20% above/below median for title/division)
- Generate pay equity report highlighting gender and ethnicity-based disparities within each group
- Summarize manager comments and peer rankings into a one-paragraph recommendation brief for division heads
- Flag retention risks: employees whose proposed comp is below market by >10% AND who are in their 3rd+ year (flight risk window)
- Calculate pool utilization in real-time as managers submit recommendations
- Generate "what-if" scenarios: impact of adjusting pool allocation between groups

**Data Required:**
- Comp Planning Board (current cycle)
- Historical comp data (prior 3 years)
- External benchmarking data (McLagan reports)
- Employee demographics (for pay equity)
- Performance review scores

**Autonomy Level:** Human-in-the-Loop
All analysis and flags are advisory. The agent never approves or modifies comp decisions — it surfaces insights for human decision-makers. Equity flags are automatically escalated to HR and cannot be dismissed without documentation.

**Example Interaction:**
> During the December comp cycle, a Group Head in M&A submits bonus recommendations for 35 professionals. The CompAnalyst Agent immediately runs analysis and flags three issues: (1) A 3rd-year Associate ranked #2 in the group is proposed at $325K total comp, which is 18% below the McLagan median of $395K for top-quartile Associates in M&A — high retention risk given this is the typical lateral move window. (2) Female VPs in the group are proposed at an average 12% below male VPs of equivalent tenure and revenue production. (3) The group's total proposed pool ($14.2M) exceeds its allocated budget ($13.5M) by 5.2%. The agent presents these findings to the HR reviewer with specific recommendations: increase the Associate's bonus by $50K to match market, review the VP gender disparity with the Group Head before approval, and identify $700K in reductions to bring the pool in line (suggesting 3 lower-ranked individuals whose proposals exceed peer medians).

---

### Use Case 4: Lateral Hiring & Executive Onboarding

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Lateral hiring in investment banking is a high-stakes, high-cost process. Recruiting a senior banker (VP to MD level) typically involves executive search firms charging 25-33% of first-year compensation ($200K-$1M+ in fees), a 3-6 month search process, complex negotiations around guaranteed bonuses ("guarantees"), garden leave periods, non-compete/non-solicit provisions, and client transition planning. Once hired, onboarding a revenue-producing lateral requires rapid integration: system access, client introductions, deal team assignments, regulatory registrations, and cultural assimilation. The cost of a failed lateral hire (leaves within 18 months) can exceed $3-5M when factoring in fees, guaranteed comp, lost revenue, and client disruption. Yet most banks manage this through disconnected email threads between HR, the hiring manager, legal, compliance, and the search firm.

#### The Solution
monday.com Work Management for end-to-end lateral hiring and onboarding. **Lateral Search Board**: Columns: Position Title, Division, Group, Search Firm (dropdown), Fee Structure, Candidate Name, Current Firm, Current Title, Status (status: Identified, Outreach, Interview, Offer, Negotiation, Accepted, Garden Leave, Start Date Confirmed), Comp Package (subitems: base, guarantee Y1, guarantee Y2, equity, sign-on), Legal Review (status), Compliance Check (status), Non-Compete Expiry (date). **Lateral Onboarding Board**: Columns: New Hire Name, Start Date, 30/60/90 Day Milestones (subitems), System Access Checklist (subitems: Bloomberg, Dealogic, CapIQ, internal systems), Licensing Status, Client Transition Plan (connect board), Buddy/Mentor Assigned (people), Onboarding Status. Automations: When status changes to "Accepted," auto-create onboarding board items with pre-populated checklists. Notify IT, compliance, and facilities on hire confirmation.

#### The Outcome
Reduce time-to-productivity for lateral hires from 6+ months to 3-4 months. Track search firm ROI (fee vs. hire retention rate). Ensure zero compliance gaps during onboarding (FINRA registration, background check, U4 filing). Provide division heads real-time visibility into their hiring pipeline.

#### Discovery Questions
- How many lateral hires do you make annually at the VP+ level, and what's your average time from search kickoff to day-one?
- How do you currently track the status of candidates across multiple search firms simultaneously?
- What's your lateral hire retention rate at 12 and 24 months? Do you track the correlation between onboarding quality and retention?
- Walk me through the handoff from recruiting to onboarding — who owns the transition, and where do balls get dropped?
- How do you manage garden leave periods and non-compete tracking for incoming laterals from competitors?

#### Industry Context
"Garden leave" is a contractual period (typically 30-90 days) during which a departing banker must stay away from the new employer while still being paid by the old one. "Guaranteed bonus" (or "guarantee") is a contractually assured bonus for year 1-2 to compensate a lateral hire for forfeited deferred comp at their prior firm. A U4 filing is the registration form submitted to FINRA when a new registered representative joins a firm. "Client transition" refers to the process of a lateral hire bringing client relationships from their former firm — a legally sensitive process governed by non-solicit agreements and protocol letters.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Lateral Hiring & Onboarding tracker for an investment bank. Two boards:
>
> Board 1 — 'Lateral Search Pipeline': Columns: Position (text), Division (dropdown: IBD, S&T, Research, AM, PWM), Group (text), Seniority (dropdown: VP, Executive Director, Managing Director, Partner), Search Firm (dropdown: Heidrick & Struggles, Spencer Stuart, Russell Reynolds, Sheffield Haworth, Options Group), Fee % (number), Candidate Name (text), Current Firm (text), Current Title (text), Status (status: Sourced, Initial Outreach, First Meeting, Interview Round, Reference Check, Offer, Negotiation, Accepted, Garden Leave, Declined), Base Salary Offer (number, currency), Y1 Guarantee (number, currency), Y2 Guarantee (number, currency), Sign-On (number, currency), Deferred Buyout (number, currency), Total Package (formula), Non-Compete Expiry (date), Garden Leave End (date), Legal Approved (checkbox), Compliance Cleared (checkbox), Start Date (date), Hiring Manager (people), HR Lead (people). Groups by: Division.
>
> Board 2 — 'Lateral Onboarding': Columns: Employee Name (connect to Board 1), Start Date (date), Day 1 Checklist (subitems: Badge & building access, IT setup, Bloomberg terminal, Dealogic access, CapIQ, Internal deal database, Email & calendar, Compliance training scheduled), Week 1 Checklist (subitems: Meet division head, Meet group members, Review active deals, FINRA U4 filing submitted, Client transition plan drafted), 30-Day Milestone (subitems: First client meetings, Deal team assignments, Licensing exams scheduled), 60-Day Milestone (subitems: Client book review, Revenue pipeline established), 90-Day Milestone (subitems: Integration assessment, Manager feedback), Onboarding Status (status: Pre-Start, Week 1, Month 1, Month 2, Month 3, Complete), Buddy (people), Onboarding Score (number 1-10).
>
> Automations: When Search Pipeline status → 'Accepted', create connected item on Onboarding board with pre-filled checklists. When Garden Leave End date arrives, notify HR Lead and Hiring Manager. When onboarding subitem completed, update progress percentage."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LateralIntegration Agent
**Agent Purpose:** Ensure seamless lateral hire onboarding by proactively managing checklists, stakeholder coordination, and milestone tracking.

**Triggers:**
- New item created on Lateral Onboarding board
- Start date is 7 days away
- Checklist subitem not completed by target date
- 30/60/90-day milestone dates reached
- New hire marks first client meeting complete

**Actions:**
- Send pre-start welcome package with first-week schedule, team directory, and system access instructions
- Notify IT, facilities, compliance, and licensing teams with specific provisioning requirements
- Chase overdue onboarding tasks with escalation (employee → HR → hiring manager)
- Generate 30/60/90-day integration report for division head
- Flag at-risk onboardings (>20% of checklist items overdue)
- Schedule automatic check-in meetings between new hire and HR at day 30, 60, 90

**Data Required:**
- Lateral Onboarding Board
- Lateral Search Pipeline Board (comp details for context)
- IT provisioning system integration
- Calendar integration for scheduling

**Autonomy Level:** Fully Autonomous
Routine onboarding coordination runs without human intervention. Escalations follow defined rules. Integration reports are auto-generated and distributed. Only exception: if a new hire signals dissatisfaction during check-ins, the agent escalates to HR leadership immediately.

**Example Interaction:**
> Seven days before a new Managing Director starts in the Healthcare IBD group, the LateralIntegration Agent activates. It sends provisioning requests to IT (Bloomberg, Dealogic, CapIQ, internal deal database — specifying Healthcare sector data access), facilities (corner office per MD policy, building access badge), and compliance (U4 filing preparation, CE transfer from prior firm). It generates a personalized first-week schedule: Monday morning meeting with the Division Head, lunch with the Healthcare group, Tuesday meetings with active deal teams, Wednesday compliance orientation, Thursday client transition planning session with the group head. On Day 30, it compiles a report: 85% of onboarding tasks complete, 3 client meetings held, U4 filing processed, one flag — Bloomberg training not yet scheduled. It sends a reminder and cc's the hiring manager. At Day 90, it generates the integration assessment: the MD has been assigned to 4 active mandates, conducted 12 client meetings, and the hiring manager rates integration at 8/10. Report is filed and search firm performance is updated (successful placement).

---

### Use Case 5: Analyst/Associate Program Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks run structured 2-3 year analyst programs and 3-4 year associate programs that require intensive management: rotations between groups, performance reviews every 6 months, mentorship pairings, training program tracking (financial modeling boot camps, industry primers, presentation skills), and the critical promote-or-leave decision at the end of the analyst program. Program managers typically oversee 100-300 analysts across divisions, tracking each individual's rotation history, performance trajectory, training completion, and career preferences. The promote-to-associate decision involves input from every group head the analyst has rotated through, calibration sessions across divisions, and coordination with campus recruiting (to backfill departing analysts). Most program managers rely on a combination of Excel, email, and their own memory — creating single points of failure and inconsistent experiences.

#### The Solution
monday.com Work Management as the analyst/associate program platform. **Program Tracker Board**: Columns: Name, Class Year, Division, Current Group, Rotation History (subitems: Group, Duration, Manager, Performance Rating), Training Completion (subitems: Financial Modeling, Industry Primer, Presentation Skills, Excel Advanced, Compliance), Performance Score (number, average of rotation ratings), Promote Decision (status: On Track, At Risk, Promoted, Transitioning Out), Mentor (people), Next Rotation Date, Career Preference (long text). Automations: rotation reminders 2 weeks before end date, performance review triggers at 6-month marks, training deadline alerts. Dashboard: class performance distribution, rotation coverage by group, training completion rates, promote vs. transition rates by cohort.

#### The Outcome
Consistent program experience across 100-300 analysts regardless of division. Data-driven promote decisions instead of political/anecdotal ones. 15-20% improvement in analyst satisfaction scores (key for campus recruiting reputation). Zero missed rotation dates or training deadlines.

#### Discovery Questions
- How many analysts and associates are in your current program, and who manages the day-to-day operations of each cohort?
- How do you currently track rotation assignments — who decides which analyst goes to which group, and based on what criteria?
- What does your promote-to-associate calibration process look like? How many stakeholders provide input, and how is it aggregated?
- What training programs do your analysts go through, and how do you track completion and effectiveness?
- How do you measure analyst satisfaction with the program, and how does it compare to your competitor banks?

#### Industry Context
The analyst program is the primary entry point for undergraduates into investment banking. Analysts typically work 2-3 years before either being promoted to associate or leaving for private equity, hedge funds, or business school (the "exit opps"). Rotations allow analysts to experience different industry or product groups (e.g., Healthcare M&A, Leveraged Finance, Restructuring). The promote decision is often called "the third-year decision" and is one of the most consequential moments in a junior banker's career. "Staffing" in IB refers to the process of assigning analysts to deal teams — a constant balancing act between group needs, analyst development, and burnout prevention.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Analyst Program Management system for an investment bank. Create a board called 'Analyst Program Tracker':
>
> Columns: Analyst Name (text), Class Year (dropdown: 2024, 2025, 2026, 2027), Start Date (date), Division (dropdown: IBD, S&T, Research), Current Group (text), Current Rotation Start (date), Current Rotation End (date), Rotation Number (number), Performance Rating (number 1-5, average), Promote Status (status: On Track, Strong Performer, At Risk, Promoted to Associate, Transitioning Out), Mentor (people), Program Manager (people), Training Status (status: In Progress, Complete), Career Interest (long text).
>
> Subitems for Rotation History: Group Name (text), Duration (text), Supervising VP/MD (people), Rating (number 1-5), Feedback Summary (long text).
>
> Subitems for Training: Module Name (text), Completion Date (date), Score (number), Status (status: Not Started, In Progress, Complete, Overdue).
>
> Groups by: Class Year.
>
> Automations: 14 days before Current Rotation End, notify Program Manager to arrange next rotation. When all Training subitems status → Complete, change Training Status to Complete. Every 6 months from Start Date, create performance review reminder and notify current group's supervising VP. When Class Year is 3 and all rotations complete, change Promote Status to trigger calibration workflow.
>
> Dashboard: Class performance bell curve (chart), Rotation coverage heat map (which groups have capacity), Training completion by module (bar chart), Promote vs. transition rates by year (chart), Average performance by group (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProgramPulse Agent
**Agent Purpose:** Optimize analyst program operations by intelligently managing rotations, flagging at-risk analysts, and streamlining the promotion calibration process.

**Triggers:**
- Rotation end date approaching (14 days out)
- Performance rating submitted below 3.0
- 6-month review cycle date
- Analyst class approaching promote decision window
- Manual request from program manager

**Actions:**
- Recommend next rotation assignment based on analyst preferences, group capacity, and development gaps
- Flag analysts with declining performance trends (2+ consecutive ratings below prior average)
- Generate calibration prep packets: consolidated rotation feedback, training scores, peer comparisons, manager recommendations
- Identify "hidden gems" — analysts with strong technical scores but lower visibility due to group assignment
- Send weekly program digest to program manager: upcoming rotations, pending reviews, at-risk flags
- Track exit patterns and predict flight risk based on historical cohort data

**Data Required:**
- Analyst Program Tracker Board
- Group capacity/staffing data
- Historical cohort data (prior years' promote/exit rates)
- Training scores and certifications
- Deal staffing data (volume/intensity of work assigned)

**Autonomy Level:** Human-in-the-Loop
Rotation recommendations and at-risk flags are suggestions for program manager review. Calibration packets are auto-generated but reviewed before distribution to division heads. Exit predictions are shared only with program manager and HR leadership.

**Example Interaction:**
> Two weeks before the end of Q1 rotations, ProgramPulse reviews the 2025 analyst class (120 analysts across IBD). It identifies that the Restructuring group has 2 open rotation slots and 5 analysts have listed Restructuring as their top preference. The agent ranks the 5 by fit: (1) Sarah K. — rated 4.8 in Leveraged Finance, strong modeling skills, expressed interest in distressed situations; (2) James T. — rated 4.2 in M&A, completed advanced restructuring training module. It recommends Sarah and James for the slots, notes that the Technology group is overstaffed by 3 analysts and suggests redistributing. Separately, it flags that Analyst Michael R. has received 3.1 and 2.8 ratings in his last two rotations (down from 4.0 in his first), generating an alert to the program manager: "Declining performance — recommend 1:1 check-in. Historical pattern matches 72% of analysts who voluntarily departed in year 2." The program manager schedules the meeting.

---

### Use Case 6: Diversity, Equity & Inclusion (DEI) Pipeline Analytics

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banking has among the worst diversity statistics in financial services: women represent approximately 20-25% of MDs at most bulge brackets, and underrepresented minorities (URMs) are even lower at senior levels. Regulators (SEC, FCA) and institutional investors increasingly require diversity reporting. Banks face pressure from campus recruits who evaluate employer diversity before accepting offers. Yet most banks track diversity data in disconnected silos — recruiting has one dataset, HR has another, and neither connects to promotion or attrition data to show pipeline progression (or leakage). The result: banks can report point-in-time demographics but cannot answer "where in the pipeline are we losing diverse talent?" — the most important question.

#### The Solution
monday.com as a DEI analytics and pipeline tracking platform. **DEI Pipeline Board**: Connected views pulling from recruiting, headcount, promotion, and attrition data. Columns: Employee/Candidate ID, Gender, Ethnicity, Level, Division, Hire Date, Promotion Dates (subitems), Current Status (Active, Departed), Departure Reason (if applicable), Participation in ERGs/BRGs, Sponsorship Program Enrollment. Dashboard providing longitudinal pipeline analysis: representation at each level (Analyst → Associate → VP → Director → MD), conversion rates between levels by demographic, attrition rates by demographic and tenure, recruiting pipeline diversity vs. hiring diversity, and ERG participation correlation with retention. Automated quarterly reporting for regulatory submissions and board presentations.

#### The Outcome
First-ever end-to-end diversity pipeline visibility (not just snapshots). Identify specific "leakage points" where diverse talent exits. Data-driven sponsorship program targeting. Regulatory reporting automated from weeks to hours. Recruiting team can demonstrate pipeline diversity to campus candidates with real data.

#### Discovery Questions
- Can you currently trace a diverse candidate from campus recruiting through to their promotion to MD — or does the data live in separate systems?
- Where in your pipeline do you see the biggest drop-off in diverse representation — is it recruiting, mid-level attrition, or promotion rates?
- How do you currently produce diversity reports for your board, regulators, and external stakeholders? What's the manual effort involved?
- Do you have sponsorship or mentorship programs specifically for diverse talent? How do you measure their effectiveness?
- How do your ERG/BRG participation rates correlate with retention — is that something you've been able to analyze?

#### Industry Context
ERGs (Employee Resource Groups) and BRGs (Business Resource Groups) are identity-based employee communities common in banking (e.g., Women's Network, Black Professionals Network, Pride Network). Sponsorship programs pair diverse junior talent with senior leaders who actively advocate for their promotion — distinct from mentorship, which is advisory. The "broken rung" refers to the first promotion from individual contributor to manager, where women and URMs disproportionately fall off the pipeline. SEC Rule 10C-1 and Nasdaq's board diversity requirements have increased regulatory focus on diversity data.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a DEI Pipeline Analytics dashboard for an investment bank. Create a board called 'DEI Pipeline Tracker':
>
> Columns: Employee ID (text), Name (text), Gender (dropdown: Male, Female, Non-Binary, Prefer Not to Say), Ethnicity (dropdown: White, Black/African American, Hispanic/Latino, Asian, Two or More, Other, Prefer Not to Say), Level (dropdown: Analyst, Associate, VP, Director/ED, Managing Director), Division (dropdown: IBD, S&T, Research, AM, PWM, Operations, Technology), Hire Date (date), Hire Source (dropdown: Campus, Lateral, Internal Transfer), Promotion History (subitems: From Level, To Level, Date, Sponsorship Y/N), Current Status (status: Active, On Leave, Departed), Departure Date (date), Departure Reason (dropdown: Voluntary-Competitor, Voluntary-Industry Change, Voluntary-Personal, Involuntary, Retirement), ERG Membership (dropdown multi: Women's Network, Black Professionals, Hispanic/Latino Alliance, Asian Professionals, Pride, Veterans, None), Sponsorship Program (checkbox), Sponsor Name (people).
>
> Groups by: Level (Analyst through MD).
>
> Dashboard: Representation by level stacked bar chart (gender), Representation by level stacked bar chart (ethnicity), Promotion conversion rate by demographic (table), Attrition rate by demographic and tenure (chart), Pipeline flow Sankey diagram (Analyst→Associate→VP→Director→MD with dropout rates), ERG participation vs retention correlation (chart), Year-over-year diversity trend lines, Hiring source diversity breakdown (pie chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** EquityLens Agent
**Agent Purpose:** Continuously monitor diversity pipeline health, flag equity gaps, and generate actionable recommendations for HR and division leadership.

**Triggers:**
- Monthly scheduled analysis (1st of each month)
- Promotion cycle initiation
- Attrition event (employee departure recorded)
- Quarterly board reporting deadline (scheduled)
- ERG program enrollment changes

**Actions:**
- Generate monthly diversity dashboard with pipeline progression rates by demographic
- Flag promotion cycles where diverse candidate representation falls below division targets
- Alert HR when attrition of diverse employees exceeds baseline by >20% in any division
- Auto-generate quarterly board diversity report with year-over-year comparisons
- Recommend sponsorship program candidates based on performance, tenure, and demographic data
- Correlate ERG participation with retention and surface findings to DEI leadership

**Data Required:**
- DEI Pipeline Tracker Board
- Promotion decision records
- Exit interview data
- ERG membership records
- Performance review data
- Industry benchmarking data (McKinsey, Catalyst reports)

**Autonomy Level:** Escalation-Based
Monthly reports and dashboards are generated autonomously. Alerts during promotion cycles are sent to HR and division heads automatically. Recommendations for sponsorship candidates require HR review. Board reports are auto-drafted but reviewed by Chief Diversity Officer before distribution.

**Example Interaction:**
> On March 1st, the EquityLens Agent runs its monthly pipeline analysis across 6,200 employees. Key findings: (1) The VP-to-Director promotion rate for women in IBD was 14% last cycle vs. 22% for men — a 8-point gap that has widened from 5 points the prior year. The agent flags this to the IBD Division Head and CHRO with a recommendation to review the calibration methodology. (2) Black/African American analysts in S&T have a 35% 2-year attrition rate vs. 22% for the overall cohort — the agent recommends expanding the S&T sponsorship program and cross-references exit interview themes (most common: "lack of advancement visibility"). (3) The agent generates the Q1 board diversity report: overall representation improved 1.2 points at the analyst level but declined 0.5 points at MD level, with a net assessment of "pipeline building but senior conversion remains the critical gap." The report includes 3 specific action items with projected impact.

---

### Use Case 7: Employee Relations & Conduct Risk Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banking's high-pressure culture creates significant employee relations challenges: harassment complaints, bullying allegations, working hours violations (particularly post-2021 when Goldman's 13 first-year analysts published a survey documenting 95-hour weeks), substance abuse concerns, and conduct risk issues (personal trading violations, information barriers breaches, inappropriate client entertainment). HR's Employee Relations (ER) team must investigate each case thoroughly while maintaining strict confidentiality, complying with employment law across multiple jurisdictions, and coordinating with Legal and Compliance. Cases are often tracked in ad-hoc systems — email folders, secured spreadsheets, or outdated case management tools — making it difficult to identify patterns (e.g., a specific MD generating repeated complaints) or demonstrate to regulators that the firm has a robust ER framework.

#### The Solution
monday.com Work Management as a secure employee relations case management system. **ER Case Board** (maximum restriction permissions): Case ID (auto-number), Category (dropdown: Harassment, Discrimination, Bullying, Working Hours, Conduct Risk, Personal Trading, Information Barrier Breach, Substance Abuse, Whistleblower, Other), Reporter Type (dropdown: Self, Colleague, Manager, Hotline, Regulator), Division, Seniority of Subject, Date Reported, Investigator Assigned (people), Investigation Status (status: Intake, Under Investigation, Awaiting Witness Statements, Legal Review, Finding Issued, Closed-Substantiated, Closed-Unsubstantiated, Closed-Inconclusive), Severity (status: Low, Medium, High, Critical), Resolution (long text), Days Open (formula), Subitems for Investigation Steps: Action, Date, Responsible Party, Outcome. Automations: Escalate "Critical" severity to CHRO within 1 hour. Alert if case open >30 days without status update. Ensure no investigator is assigned to a case involving someone in their reporting line.

#### The Outcome
Pattern detection across ER cases (identify repeat offenders, systemic issues). Regulatory audit readiness — complete case history with timeline and documentation. Reduce average case resolution time by 25%. Demonstrate to board and regulators a mature, technology-enabled ER framework.

#### Discovery Questions
- How do you currently track employee relations cases from intake through resolution? Is there a single system of record?
- Have you been able to identify patterns across cases — for example, a disproportionate number of complaints from a specific division or about a specific individual?
- What's your average case resolution time, and where do investigations typically stall?
- How do you handle cross-jurisdictional cases — for example, a complaint involving a London-based MD and a New York-based analyst?
- When regulators audit your ER processes, how do you produce case histories and demonstrate systematic investigation?

#### Industry Context
"Information barrier" (or "Chinese wall") refers to the separation between divisions with access to material non-public information (MNPI) and those that don't. A breach is a serious regulatory violation. Personal trading policies at banks restrict employees from trading securities their firm is involved with. Working hours scrutiny intensified after Goldman Sachs's 2021 analyst survey and subsequent industry-wide reforms. The FCA's SM&CR (Senior Managers & Certification Regime) requires UK-based banks to document fitness and propriety assessments, making ER records directly relevant to regulatory compliance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Employee Relations Case Management system for an investment bank. Create a board called 'ER Case Tracker' with restricted permissions:
>
> Columns: Case ID (auto-number, prefix ER-), Date Reported (date), Category (dropdown: Harassment, Discrimination, Bullying/Intimidation, Working Hours Violation, Conduct Risk, Personal Trading Violation, Information Barrier Breach, Substance Abuse, Whistleblower Report, Retaliation, Other), Reporter Type (dropdown: Direct Report, Peer, Manager, Anonymous Hotline, External, Regulator Referral), Subject Division (dropdown: IBD, S&T, Research, AM, PWM, Operations, Technology, Other), Subject Seniority (dropdown: Analyst, Associate, VP, Director/ED, Managing Director, C-Suite), Jurisdiction (dropdown: US, UK, HK, Singapore, Germany, Multi-Jurisdiction), Severity (status: Low - Green, Medium - Yellow, High - Orange, Critical - Red), Investigator (people), Legal Counsel (people), Status (status: New, Intake Complete, Investigation Active, Witness Interviews, Legal Review, Finding Drafted, Finding Approved, Closed-Substantiated, Closed-Unsubstantiated, Closed-Inconclusive, Appealed), Resolution Summary (long text), Days Open (formula: TODAY minus Date Reported), Outcome Actions (dropdown multi: Written Warning, Final Warning, Termination, Training Required, No Action, Referred to Regulator, Policy Change).
>
> Subitems: Investigation Step (text), Date (date), Responsible (people), Notes (long text), Evidence Attached (file).
>
> Groups by: Status (Active Cases, Closed Cases).
>
> Automations: When Severity = Critical, immediately notify CHRO and General Counsel. When Days Open > 30 and Status not Closed, notify Investigator and HR Director. When Status changes to any 'Closed' option, notify Reporter Type (if not anonymous) that case is resolved. Weekly digest of open cases to HR leadership."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ConductWatch Agent
**Agent Purpose:** Detect patterns across employee relations cases, ensure investigation timelines are met, and generate compliance-ready reporting.

**Triggers:**
- New case created on ER Case Tracker
- Case open for >20 days without status change
- Multiple cases filed against the same subject (2+ in 12 months)
- Quarterly compliance reporting deadline
- Severity marked as "Critical"

**Actions:**
- Cross-reference new cases against historical data to identify repeat subjects or systemic patterns
- Generate investigation timeline and assign standard steps based on case category
- Send escalation alerts when deadlines are missed
- Produce quarterly ER summary: case volumes by category, average resolution time, substantiation rates, division hotspots
- Flag potential retaliation: if a reporter's performance review or compensation changes negatively within 6 months of filing
- Compile regulatory audit packages with complete case chronologies

**Data Required:**
- ER Case Tracker Board
- Historical ER data
- Performance review records (for retaliation detection)
- Compensation data (for retaliation detection)
- Organizational hierarchy data

**Autonomy Level:** Escalation-Based
Pattern detection and timeline monitoring are automatic. Escalations follow pre-defined severity-based rules. Retaliation flags require HR leadership review. Regulatory reports are auto-drafted but require General Counsel approval. The agent never makes disciplinary recommendations — it provides data and flags for human decision-makers.

**Example Interaction:**
> A new case is filed via the anonymous hotline alleging bullying by a Director in the Leveraged Finance group. The ConductWatch Agent creates the case, assigns it to the next available investigator based on rotation, and runs a pattern check. It discovers two prior cases involving the same Director in the past 18 months — one closed as unsubstantiated (harassment allegation) and one closed with a written warning (working hours violation for requiring analysts to work weekends without comp time). The agent escalates the case to "High" severity (pattern trigger: 3 cases in 18 months) and notifies the HR Director and Division Head. It generates an investigation plan with standard steps: intake interview with reporter (within 5 business days), subject notification (within 7 days), witness interviews (within 15 days), finding (within 30 days). Three weeks in, the agent detects the investigation has stalled at the witness interview stage and sends a follow-up to the investigator. Upon case closure, it updates the Director's ER profile and flags for the annual SM&CR fitness assessment.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Bulge Bracket | The largest, most prestigious global investment banks (Goldman Sachs, Morgan Stanley, JP Morgan, etc.) |
| Superday | Final round of interviews, typically held on-site with multiple back-to-back interviews |
| Garden Leave | Contractual period where a departing employee is paid but cannot work for a new employer |
| Guaranteed Bonus | Contractually assured bonus for 1-2 years offered to lateral hires to compensate for forfeited deferred comp |
| Deferred Compensation | Portion of bonus paid in restricted stock or deferred cash, vesting over 3-5 years |
| McLagan | Leading compensation benchmarking firm for financial services (now part of Aon) |
| Stack Ranking | Forced ranking of employees within a peer group from top to bottom, used for comp and promotion decisions |
| U4/U5 Filing | FINRA registration forms: U4 for joining a firm, U5 for departing |
| Web CRD | FINRA's Central Registration Depository — online system for managing broker-dealer registrations |
| Series 7/63/79 | FINRA licenses required for different banking activities (General Securities, State Law, Investment Banking) |
| Revenue Attribution | Assigning deal revenue credit to specific bankers — drives compensation |
| ERG/BRG | Employee/Business Resource Groups — identity-based employee communities |
| Information Barrier | Separation between divisions with MNPI and those without (aka "Chinese Wall") |
| SM&CR | FCA's Senior Managers & Certification Regime — UK regulatory framework for individual accountability |
| Broken Rung | The first promotion gap where women and minorities disproportionately fall behind |
| Street Comp | Market-rate compensation for a given role/level across the industry |
| Exit Opps | Career opportunities analysts pursue after their banking stint (PE, hedge funds, business school) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Human Resources Officer (CHRO) | Overall HR strategy, board reporting, culture | Decision-maker |
| Head of Compensation | Year-end bonus process, benchmarking, pay equity | Decision-maker |
| Head of Talent Acquisition | Campus and lateral recruiting strategy | Decision-maker |
| Analyst Program Manager | Day-to-day management of junior banker programs | Influencer/User |
| HR Business Partners | Embedded in divisions, bridge between HR and business | Influencer |
| Chief Compliance Officer (CCO) | Licensing, regulatory compliance, conduct risk | Decision-maker (for compliance tools) |
| Employee Relations Lead | Investigations, case management, conduct | User |
| Chief Diversity Officer | DEI strategy, pipeline analytics, ERG oversight | Influencer/Decision-maker |
| Division Head (e.g., Head of IBD) | Hiring decisions, compensation allocation, culture | Decision-maker |
| General Counsel | Employment law, investigation oversight | Decision-maker (for ER tools) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Compliance | Licensing, conduct risk, regulatory training | Unified compliance + HR platform for licensing/conduct |
| Finance | Compensation budgeting, headcount planning, P&L allocation | Connected comp planning and financial forecasting |
| Legal | Employment law, investigations, non-compete management | Integrated case management and contract tracking |
| IT | System provisioning, access management, HRIS | Automated onboarding provisioning workflows |
| Operations | Facilities, badge access, office space planning | Connected new hire logistics |
| Business Heads | Staffing, performance, hiring approvals | Manager self-service portals for HR requests |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Workday | Enterprise HRIS and HCM | monday.com won't replace core HRIS, but can sit on top for workflows Workday doesn't handle well (recruiting ops, comp cycle, program management) |
| Greenhouse / Lever | ATS for recruiting | monday.com can serve as the operational layer above ATS — coordination, scheduling, analytics that ATS tools lack |
| SAP SuccessFactors | Legacy enterprise HCM | Complex, expensive, slow to configure. monday.com offers agility for specific HR processes while SAP handles payroll/core HR |
| Excel/Google Sheets | The actual incumbent for comp cycles, tracking, analysis | Direct displacement — same flexibility with collaboration, automation, audit trails, and security |
| ServiceNow HR | HR service delivery | Often over-engineered for HR use cases. monday.com offers faster deployment and better UX |
| Custom Internal Tools | Bank-built solutions for specific processes | Aging, expensive to maintain, poor UX. monday.com modernizes without multi-year IT projects |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We use Workday for everything HR" | Workday is excellent for system-of-record HR — payroll, benefits, core employee data. But recruiting operations, comp cycle management, and program tracking require workflow agility that Workday wasn't designed for. monday.com sits alongside Workday, not replacing it, handling the operational processes your team currently runs in spreadsheets. |
| "Compensation data is too sensitive for a cloud platform" | monday.com offers enterprise-grade security: SOC 2 Type II, HIPAA capability, granular permissions down to column-level visibility, IP restrictions, and audit logs. Your comp spreadsheets emailed between 50 people are the actual security risk — monday.com is the more secure alternative. |
| "We're a regulated bank — we can't use external tools for compliance data" | monday.com is used by banks globally, meets regulatory requirements for data handling, and provides audit trails that spreadsheets can't. The question isn't whether a cloud tool meets your standards — it's whether your current spreadsheet-based process does. |
| "HR processes are too unique to each bank to standardize" | That's exactly why monday.com works — it's not a rigid HRIS. It's a flexible platform your HR team configures to match YOUR processes, not the other way around. No two banks' comp cycles work the same way, and monday.com adapts to that. |
| "Our HR team isn't technical enough to build this" | monday.com's no-code interface is designed for HR professionals, not developers. Vibe coding lets you describe what you want in plain English and get a working board. If your team can use Excel, they can use monday.com — but with automations, dashboards, and collaboration built in. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for financial services HR case studies]
- [Placeholder for enterprise recruiting operations examples]
- [Placeholder for compliance tracking references]
- [Placeholder for compensation cycle management stories]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
