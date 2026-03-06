# Advertising & Marketing × HR Playbook

## Overview

Human Resources in advertising and marketing agencies operates under conditions unlike almost any other industry. The workforce is predominantly creative, young (median age 31), and mobile — average tenure at agencies is just 2.1 years, creating constant churn that HR must manage. Agencies range from boutique shops (20–50 people) to global holding company networks (WPP: 100,000+ employees, Publicis Groupe: 96,000+, Omnicom: 70,000+) with complex matrix structures spanning creative, media, strategy, account management, and production departments across dozens of offices worldwide.

The regulatory landscape for agency HR is complicated by the freelance-heavy workforce model. Agencies routinely staff 30–50% of project teams with freelancers, contractors, and gig workers — each with different labor classification rules (AB5 in California, IR35 in the UK), benefits obligations, and intellectual property considerations. DEI pressure is intense: holding companies publish annual diversity reports, and clients like Procter & Gamble and Unilever increasingly require diversity metrics in RFP responses. The "Great Resignation" hit agencies harder than most industries, with 2022–2024 turnover rates reaching 30%+ at many shops.

Agency HR teams are chronically under-resourced relative to the complexity they manage. A typical mid-market agency (200–500 people) might have 3–5 HR professionals handling recruiting, onboarding, benefits, performance management, L&D, compliance, and culture — while also managing relationships with 100+ active freelancers. The rise of remote/hybrid work has added another layer: agencies must now manage distributed creative teams across time zones while preserving the collaborative culture that's supposed to be their differentiator.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Tiny HR teams manage disproportionate complexity — AI can handle recruiting coordination, onboarding workflows, and compliance tracking that currently consume 60%+ of HR bandwidth |
| 2 | Scale Impact Without Overhead | Medium-High | Agencies are growing headcount globally without proportional HR growth — need to scale HR operations across regions without adding HR staff in each office |
| 3 | Consolidate Tech Stack with AI | Medium | HR tech stack in agencies is fragmented: ATS, HRIS, LMS, engagement surveys, freelancer management — often 6–8 disconnected systems |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Creative Talent Recruiting Pipeline

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Agencies are in a perpetual war for creative talent. Recruiting a senior art director or a programmatic media strategist takes 45–90 days, during which the agency is either overstaffing with expensive freelancers or under-delivering to clients. The recruiting process involves portfolio reviews (not just resumes), creative tests, culture-fit assessments, and often 4–6 interview rounds. HR teams manage this across multiple roles simultaneously in disconnected spreadsheets and email chains, while hiring managers in creative and media departments have zero visibility into pipeline status. Agencies lose top candidates to competitors because their process is too slow — a strong creative director gets 3–4 offers within two weeks.

#### The Solution
monday.com Work Management as a full recruiting pipeline. Every open role is tracked from requisition through offer acceptance, with structured stages for portfolio review, creative tests, and panel interviews. Hiring managers get real-time dashboards showing their pipeline without pinging HR. Automations handle interview scheduling reminders, candidate status updates, and offer approval workflows. Integration with LinkedIn and portfolio platforms (Behance, Dribbble) centralizes candidate profiles.

#### The Outcome
- 30% reduction in time-to-hire for creative roles (from 65 to 45 days average)
- 50% less HR time spent on status updates to hiring managers
- Zero candidates lost due to slow process (automated follow-ups within 24 hours)
- Complete recruiting analytics: source effectiveness, pipeline conversion rates, diversity metrics by stage

#### Discovery Questions
1. "What's your current time-to-hire for senior creative roles, and how many candidates do you lose to competitors during the process?"
2. "How do hiring managers — ECDs, group creative directors — currently get visibility into their recruiting pipeline?"
3. "How do you handle portfolio review as part of your hiring process — is it structured or ad hoc?"
4. "What percentage of your hires come from referrals versus job boards versus recruiters, and can you actually measure that?"
5. "How do you track diversity metrics through your recruiting funnel — do you know where underrepresented candidates drop off?"

#### Industry Context
Agency recruiting is portfolio-first, resume-second. A creative director's "book" (portfolio) matters more than their degree or employer list. This makes ATS systems designed for corporate recruiting (keyword matching, resume parsing) largely useless for creative roles. Agencies also recruit heavily from competitor agencies — "poaching" is the industry norm, and maintaining relationships with passive candidates is critical. Award shows (Cannes Lions, One Show, D&AD) serve as defacto recruiting events where agencies scout talent based on winning work.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Creative Talent Recruiting workspace for an advertising agency. Include:
> 1. **Open Roles** — columns: Role Title (text), Department (dropdown: Creative, Media, Strategy, Account, Production, Data/Analytics, Technology), Level (dropdown: Junior, Mid, Senior, Director, VP, C-Suite), Hiring Manager (people), Recruiter (people), Priority (status: Urgent, High, Normal, Backfill), Status (status: Requisition, Sourcing, Screening, Interviewing, Offer, Filled, On Hold, Cancelled), Location (dropdown: New York, Los Angeles, Chicago, London, Remote), Target Start Date (date), Days Open (formula: TODAY - creation date), Salary Range (text), Freelancer Covering (checkbox)
> 2. **Candidate Pipeline** — columns: Candidate Name (text), Linked Role (connect to Open Roles), Source (dropdown: Referral, LinkedIn, Recruiter, Job Board, Portfolio Site, Award Show, Boomerang), Stage (status: Applied, Portfolio Review, Phone Screen, Creative Test, Panel Interview, Culture Fit, Reference Check, Offer Extended, Offer Accepted, Declined), Portfolio Link (link), Recruiter Notes (long text), Interview Score (numbers 1-5), Diversity Tag (dropdown: Self-Identified, Not Provided), Days in Stage (formula)
> 3. **Interview Schedule** — columns: Candidate (connect to Candidate Pipeline), Interview Type (dropdown: Portfolio Review, Creative Test Debrief, Hiring Manager, Panel, Culture Fit, Executive), Interviewer(s) (people), Date/Time (date), Feedback Status (status: Pending, Submitted, Overdue), Feedback Score (numbers 1-5), Notes (long text)
>
> Automations: When Candidate Stage changes, notify Hiring Manager. When Feedback Status is 'Pending' for more than 48 hours, change to 'Overdue' and notify interviewer. When all Interview Feedback is submitted for a stage, notify Recruiter to advance candidate. Dashboard with pipeline funnel by role, time-in-stage analytics, source effectiveness, and diversity tracking."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** TalentScout
**Agent Purpose:** Accelerate creative recruiting by automating candidate screening, interview coordination, and pipeline management.

**Triggers:**
- New candidate added to pipeline (via form, email integration, or manual)
- Candidate stage change
- Interview feedback overdue (48+ hours)
- Weekly schedule: pipeline health report every Monday

**Actions:**
- Screen incoming applications against role requirements and flag top candidates for priority review
- Auto-schedule interview rounds based on interviewer availability and candidate preferences
- Send personalized candidate communication at each stage (acknowledgment, next steps, timeline)
- Generate weekly pipeline report for hiring managers with stage conversion rates
- Flag candidates stuck in any stage for more than the target duration
- Compile interview feedback summaries for hiring committee review

**Data Required:**
- Role requirements and ideal candidate profiles
- Interviewer calendars and availability
- Historical hiring data (time-to-hire, source effectiveness, conversion rates)
- Email templates for candidate communication

**Autonomy Level:** Human-in-the-Loop
Autonomous for scheduling, communications, and reporting. All hiring decisions (advance, reject, offer) require human approval.

**Example Interaction:**
> A senior copywriter application comes in via LinkedIn for the New York office. TalentScout reviews the application, identifies 5 years of agency experience (matches requirement), notes a Cannes Lion mention in the resume, and flags the candidate as "Priority — Strong Match." It auto-sends an acknowledgment email with a portfolio submission link, schedules a phone screen with the recruiter for the next available slot, and notifies the hiring manager (Group Creative Director): "New priority candidate for Sr. Copywriter — 5yr agency experience, Cannes Lion winner. Phone screen scheduled Thursday 2 PM. Portfolio link pending." When the portfolio arrives, it adds it to the candidate profile and pings the creative test coordinator to prepare the brief.

---

### Use Case 2: Freelancer & Contractor Workforce Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Agencies maintain a bench of 100–500+ freelancers who are staffed onto projects as needed. Managing this extended workforce is a nightmare: who's available, what are their rates, when do their contracts expire, are they properly classified (W-2 vs 1099 vs international contractor), do they have current NDAs and IP agreements? This information lives in individual producers' heads, scattered spreadsheets, and email chains. When a freelance motion designer is needed urgently for a pitch, it takes 2–3 days to identify, vet, and onboard someone — by which time the pitch is half over. Misclassification risk is real: the IRS and state agencies are aggressively auditing agencies for worker misclassification.

#### The Solution
monday.com Work Management as a centralized freelancer database and staffing platform. Every freelancer has a profile with skills, rates, availability, contract status, and performance ratings. Project staffing requests trigger automated matching against the talent pool. Contract expiration automations ensure no one works on expired agreements. Integration with accounting systems tracks spend against project budgets.

#### The Outcome
- Freelancer staffing time reduced from 2–3 days to 4 hours
- 100% compliance: no one works without current NDA, contract, and proper classification
- 20% cost savings through rate visibility and negotiation leverage
- Institutional knowledge preserved — freelancer capabilities and feedback don't leave when a producer leaves

#### Discovery Questions
1. "How many freelancers does your agency use in a typical month, and where does the information about their skills, rates, and availability live?"
2. "How do you ensure every freelancer has a current NDA, IP assignment, and valid contract before they start work?"
3. "If I asked you right now for a freelance motion designer who's worked with your agency before, is available next week, and charges under $750/day — how long would it take to answer?"
4. "How do you handle worker classification compliance — especially for freelancers who work 30+ hours/week for extended periods?"

#### Industry Context
The freelance economy is the backbone of agency staffing flexibility. During pitch season or peak campaign periods, agencies may double their effective workforce with freelancers. The "Hollywood model" of project-based assembly is becoming the norm. Key roles staffed freelance include: motion designers, editors, retouchers, copywriters, UX designers, developers, and media analysts. Platforms like Working Not Working, Free Agency, and Tongal are disrupting traditional freelance staffing, but agencies still largely rely on personal networks. California's AB5 law and similar legislation in other states has created significant compliance risk for agencies that over-rely on 1099 relationships.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Freelancer Workforce Management workspace for an advertising agency. Include:
> 1. **Freelancer Database** — columns: Name (text), Primary Skill (dropdown: Motion Design, Copywriting, Art Direction, UX/UI, Development, Video Editing, Retouching, Photography, Strategy, Media Planning, Production), Secondary Skills (dropdown multi-select), Day Rate (numbers with $), Location (text), Remote OK (checkbox), Availability (status: Available, On Assignment, Unavailable, Do Not Rehire), Last Engagement (date), Rating (numbers 1-5), NDA Status (status: Current, Expired, None), Contract Status (status: Active, Expired, Pending), Contract Expiry (date), Classification (dropdown: 1099, W-2, International Contractor, Corp-to-Corp), Portfolio Link (link), Notes (long text)
> 2. **Staffing Requests** — columns: Request Title (text), Project (text), Client (text), Skill Needed (dropdown - same as Primary Skill), Start Date (date), End Date (date), Budget per Day (numbers with $), Requestor (people), Priority (status: Urgent-24hr, High-48hr, Normal-1wk), Status (status: Open, Sourcing, Proposed, Confirmed, Active, Completed), Assigned Freelancer (connect to Freelancer Database)
> 3. **Engagement Tracker** — columns: Freelancer (connect to Freelancer Database), Project (text), Client (text), Start Date (date), End Date (date), Agreed Rate (numbers with $), Total Days (numbers), Total Cost (formula: rate × days), Invoice Status (status: Not Invoiced, Invoiced, Paid), Performance Rating (numbers 1-5), Would Rehire (checkbox), Feedback (long text)
>
> Automations: When Contract Expiry is within 30 days, notify HR and change Contract Status to 'Pending'. When Staffing Request is created with 'Urgent' priority, notify all producers. When Engagement ends, prompt requestor for Performance Rating. Dashboard with total freelance spend, top freelancers by rating, skill availability gaps, and compliance status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FreelanceMatchmaker
**Agent Purpose:** Instantly match staffing requests to the best available freelancers based on skills, rates, ratings, and compliance status.

**Triggers:**
- New staffing request created
- Freelancer availability status changes
- Contract expiration within 30 days
- Monthly schedule: workforce analytics report

**Actions:**
- Match staffing requests against freelancer database (skills, rate, availability, compliance)
- Rank matched freelancers by fit score (skill match + rating + rate fit + recency)
- Auto-send availability check to top 3 freelancer matches
- Flag compliance issues (expired NDA, classification risk for long engagements)
- Generate monthly freelancer spend report by department, project, and skill
- Identify freelancers approaching classification risk thresholds (hours/duration)

**Data Required:**
- Freelancer profiles with skills, rates, and ratings
- Current engagement data (who's on what project)
- Contract and compliance status
- Project budget information
- Labor classification rules by jurisdiction

**Autonomy Level:** Human-in-the-Loop
Autonomous for matching, outreach, and compliance flagging. Staffing confirmations and rate negotiations require human approval.

**Example Interaction:**
> A producer creates an urgent staffing request: "Need a senior motion designer for 3 weeks, Nike pitch, starting Monday. Budget: $800/day max." FreelanceMatchmaker scans the database, identifies 7 motion designers with 4+ star ratings and current contracts. It filters to 3 who are available: Sarah (rate $750, 4.8 stars, worked on last Nike pitch), Marcus (rate $800, 4.5 stars, available immediately), and Jin (rate $650, 4.2 stars, remote only). The agent sends availability confirmation requests to all three, prioritizing Sarah based on client familiarity and rating. It notes that Marcus's NDA expires in 10 days and flags for renewal. Within 2 hours, it reports back: "Sarah confirmed — available Monday. Rate: $750/day × 15 days = $11,250. Current NDA and contract valid through March. Shall I confirm the engagement?"

---

### Use Case 3: Employee Onboarding for Agency Roles

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Agency onboarding is notoriously chaotic. A new hire needs access to 15–20 tools (Creative Suite, Figma, Slack, project management, media platforms, DAM, time tracking, expense reporting), needs to be briefed on 5–10 active client accounts, and needs to understand agency culture and processes — all while their manager is probably in back-to-back client meetings. The average agency employee takes 4–6 weeks to become productive, and with 25–30% annual turnover, HR is constantly onboarding. Worse, different departments need different onboarding: a media buyer's first week looks nothing like a copywriter's. HR can't create bespoke onboarding for every role, so they default to a generic day-one orientation that leaves new hires to figure out the rest themselves.

#### The Solution
monday.com Work Management for role-specific onboarding workflows. Template boards for each department auto-generate when a new hire's start date is confirmed, with tasks assigned to HR, IT, the hiring manager, and the new hire themselves. Automations sequence tasks (IT provisioning must complete before tool training), send reminders, and track completion. A 30-60-90 day check-in workflow ensures new hires don't fall through the cracks.

#### The Outcome
- Time-to-productivity reduced from 6 weeks to 3 weeks
- 100% onboarding task completion (vs. ~70% with manual tracking)
- New hire satisfaction scores increase 25%+ (structured experience vs. chaos)
- HR saves 5 hours per new hire in coordination time

#### Discovery Questions
1. "How does your onboarding process differ between, say, a new art director and a new media planner — and is that difference intentional or ad hoc?"
2. "How many tools and platform accesses does a new hire need on day one, and how long does IT provisioning actually take?"
3. "What's your current time-to-productivity for new hires, and how do you even measure it?"
4. "How do you handle client account briefings for new hires — who's responsible, and does it happen consistently?"

#### Industry Context
Agency onboarding carries unique challenges: new hires often start mid-campaign and must get up to speed on live client work immediately. Unlike corporate environments with longer ramp periods, agencies bill clients for employee time — so unproductive time directly impacts profitability. The "buddy system" is common but inconsistent. Many agencies have adopted "first 100 days" programs influenced by agency consultants like Mirren and AAR Partners. The shift to hybrid work has made onboarding harder — new hires miss the osmotic learning of sitting near experienced colleagues.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an Employee Onboarding workspace for an advertising agency. Include:
> 1. **New Hire Tracker** — columns: Employee Name (text), Role (text), Department (dropdown: Creative, Media, Strategy, Account, Production, Data/Analytics, Technology, HR, Finance), Start Date (date), Manager (people), HR Contact (people), Buddy (people), Office (dropdown: New York, LA, Chicago, London, Remote), Onboarding Status (status: Pre-Start, Week 1, Week 2-4, 30-Day Check, 60-Day Check, 90-Day Check, Complete), Overall Progress (progress bar from subitems)
> 2. **Onboarding Tasks** (subitems of New Hire) — columns: Task (text), Category (dropdown: IT Setup, HR Admin, Department Training, Client Briefing, Tool Training, Culture, Compliance), Owner (people), Due Date (date), Status (status: Not Started, In Progress, Complete, Blocked), Priority (status: Day 1, Week 1, Month 1, Month 2-3), Notes (long text)
> 3. **Check-In Schedule** — columns: Employee (connect to New Hire Tracker), Check-In Type (dropdown: Day 1, Week 1, 30-Day, 60-Day, 90-Day), Scheduled Date (date), Conducted By (people), Status (status: Scheduled, Completed, Rescheduled, Missed), Employee Satisfaction (numbers 1-10), Notes (long text), Action Items (long text)
>
> Create template groups for each department (Creative onboarding template, Media onboarding template, etc.) with pre-populated tasks. Automations: When new hire is added, auto-generate department-specific task list from template. When Start Date is 7 days away, notify IT Setup tasks owners. When 30/60/90-day dates arrive, auto-create Check-In item. Dashboard showing onboarding completion by department, average time-to-completion, and satisfaction scores."

Note: Vibe builds apps/board/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OnboardingConcierge
**Agent Purpose:** Orchestrate the entire new hire onboarding journey, ensuring every task is completed on time and nothing falls through the cracks.

**Triggers:**
- New hire item created on tracker
- Start date is 7/3/1 days away
- Onboarding task overdue
- Check-in date arrives
- 90-day mark reached

**Actions:**
- Generate department-specific onboarding task list from templates
- Send welcome email to new hire with first-day logistics and pre-reading
- Coordinate IT provisioning requests with priority sequencing
- Send daily digest to manager with onboarding progress and blockers
- Schedule and remind for 30/60/90-day check-ins
- Compile onboarding effectiveness report (task completion, time-to-productivity, satisfaction)
- Identify and escalate blocked or overdue tasks

**Data Required:**
- Department-specific onboarding templates
- IT provisioning requirements by role
- Client account assignments
- Manager and buddy assignments
- Historical onboarding data for benchmarking

**Autonomy Level:** Fully Autonomous
Handles all coordination, communication, and tracking automatically. Escalates only when tasks are critically overdue or new hire flags concerns.

**Example Interaction:**
> Maria, a new Senior Media Planner, has a start date of March 3. Seven days before, OnboardingConcierge activates her onboarding: sends IT a provisioning request for Creative Cloud, The Trade Desk, DV360, Prisma, and Slack access; emails Maria's welcome packet with hybrid work policy, first-week schedule, and benefits enrollment links; notifies her manager (Media Director) and assigned buddy. On March 3, it sends Maria a morning message: "Welcome to [Agency]! Your desk is on Floor 3, near the Media team. Your buddy Jake will meet you in the lobby at 9 AM. Today's schedule: 9:30 HR orientation, 11:00 IT setup, 1:00 lunch with your team, 2:30 client briefing on the Honda account." Throughout week one, it tracks task completion and sends the Media Director a daily update: "Maria's onboarding: 8/12 Week 1 tasks complete. Pending: DV360 access (IT ticket open), Honda brand guidelines review. On track."

---

### Use Case 4: Performance Management & Creative Career Development

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Traditional annual performance reviews don't work in agencies. Creative work is subjective, project-based, and often team-credited. A junior art director might work on 15 campaigns in a year across 8 clients — how do you evaluate that holistically? Agencies struggle with: inconsistent review processes across departments, no structured career pathing (creatives hit a ceiling and leave), feedback that comes too late (annual reviews for quarterly project cycles), and managers who are too busy with client work to do reviews properly. The result: top talent leaves for competitors or goes client-side because they see no growth path.

#### The Solution
monday.com Work Management for continuous performance tracking tied to creative output. Each employee has a profile tracking project contributions, client feedback, skill development, and career goals. Quarterly reviews replace annual ones, with structured templates that balance creative quality, client impact, collaboration, and leadership. Career ladders are documented and visible, with clear criteria for advancement. Managers get automated reminders and pre-populated review data.

#### The Outcome
- 20% improvement in employee retention (top performers stay when they see growth paths)
- 90%+ review completion rate (vs. 60% with annual manual process)
- Managers save 3 hours per direct report per review cycle with pre-populated data
- Clear diversity metrics in promotion and development decisions

#### Discovery Questions
1. "How do you evaluate creative work in performance reviews — is there a structured rubric or is it subjective?"
2. "What does the career ladder look like for a junior copywriter versus a junior media planner — and is that documented anywhere?"
3. "What's your annual voluntary turnover rate, and when you do exit interviews, what are the top reasons people leave?"
4. "How do you ensure performance reviews are consistent across departments when an ECD and a VP of Media have completely different management styles?"

#### Industry Context
Agency career paths are notoriously unclear. The traditional trajectory (Junior → Mid → Senior → ACD → CD → GCD → ECD → CCO) exists in creative departments, but other departments lack structured ladders. "Titles are currency" in advertising — people negotiate title bumps as compensation. The industry's "up or out" culture drives talented mid-level people to leave for in-house roles that offer better work-life balance and clearer advancement. Agencies that invest in career development retain talent 2x longer than those that don't.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Performance & Career Development workspace for an advertising agency. Include:
> 1. **Employee Profiles** — columns: Name (text), Department (dropdown), Role (text), Level (dropdown: Junior, Mid, Senior, Associate Director, Director, VP, SVP, C-Suite), Manager (people), Start Date (date), Tenure (formula: years), Current Projects (connect to Projects board), Career Goal (long text), Last Review Date (date), Next Review Date (date), Overall Rating (numbers 1-5), Retention Risk (status: Low, Medium, High)
> 2. **Review Cycles** — columns: Employee (connect to Employee Profiles), Review Period (dropdown: Q1, Q2, Q3, Q4), Manager (people), Self-Assessment Status (status: Not Started, Submitted), Manager Assessment Status (status: Not Started, Drafted, Submitted), Calibration Status (status: Pending, Complete), Creative Quality Score (numbers 1-5), Client Impact Score (numbers 1-5), Collaboration Score (numbers 1-5), Leadership Score (numbers 1-5), Overall Rating (formula: average), Promotion Recommended (checkbox), Development Plan (long text)
> 3. **Career Ladders** — columns: Department (dropdown), Level (text), Title (text), Years Experience Typical (text), Core Competencies (long text), Technical Skills Required (long text), Leadership Expectations (long text), Compensation Band (text)
>
> Automations: When Next Review Date is 14 days away, create Review Cycle item and notify employee + manager. When Self-Assessment is submitted, notify manager. When Manager Assessment is 'Submitted' for all directs, trigger calibration meeting. Dashboard with review completion rates by department, rating distribution, retention risk heat map, and promotion pipeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CareerCoach
**Agent Purpose:** Support managers with performance data, ensure review completion, and identify retention risks before they become resignations.

**Triggers:**
- Review cycle initiation (quarterly)
- Self-assessment or manager assessment submitted
- Employee tenure milestone (1yr, 2yr, 3yr)
- Retention risk status changes to "High"

**Actions:**
- Pre-populate review forms with project contributions, client feedback, and skill development activities
- Send manager a "review prep packet" with direct report's quarter highlights
- Track review completion and send escalation reminders
- Analyze review patterns to identify retention risks (declining scores, stalled promotions)
- Generate department-level talent reports for leadership calibration
- Recommend development opportunities based on career goals and skill gaps

**Data Required:**
- Project assignment and contribution history
- Client feedback data
- Historical review scores
- Career ladder requirements
- Training and development catalog
- Industry benchmark compensation data

**Autonomy Level:** Human-in-the-Loop
Autonomous for data compilation, reminders, and pattern detection. All evaluation judgments and promotion decisions require human approval.

**Example Interaction:**
> It's Q1 review time. CareerCoach generates review prep packets for each manager. For James, a Media Director with 6 direct reports, the packet includes: "Direct report spotlight — Priya (Sr. Media Planner, 18 months tenure): Led 4 campaigns this quarter (Nike, Coca-Cola, Airbnb, Spotify). Client satisfaction scores: 4.5 avg. Completed Google Ads certification. Q4 rating: 4.2. Career goal: Associate Media Director within 12 months. Gap analysis: needs people management experience — consider having her mentor the new junior planner. Note: Priya's 2-year tenure mark is in 6 months (high-risk churn point for media planners). Recommend: discuss promotion timeline proactively."

---

### Use Case 5: DEI Tracking & Reporting

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Diversity, equity, and inclusion has moved from "nice to have" to business-critical in advertising. Major clients require DEI data in RFPs — P&G's "Brand Inclusion Standards" mandate diverse agency teams working on their brands. Holding companies publish annual DEI reports. But collecting, tracking, and reporting DEI data is manual and error-prone: HR pulls data from HRIS exports, massages it in Excel, and creates PowerPoint decks for leadership. There's no real-time visibility into diversity metrics by department, level, hiring pipeline, or promotion rates. Agencies can't identify where underrepresented talent drops off or stalls because the data doesn't exist in a usable form.

#### The Solution
monday.com Work Management for DEI program management and metrics tracking. Dashboards show real-time diversity metrics across dimensions (gender, race/ethnicity, LGBTQ+, disability, veteran status) broken down by department, level, and tenure. DEI initiative tracking connects programs to measurable outcomes. Recruiting pipeline diversity tracking identifies where underrepresented candidates drop off.

#### The Outcome
- Real-time DEI dashboards replace quarterly manual reports (saving 20+ hours per quarter)
- Identify and address pipeline leaks: pinpoint exactly where underrepresented candidates drop off
- RFP-ready DEI data available on demand (win more pitches)
- Measurable ROI on DEI initiatives tied to retention and promotion outcomes

#### Discovery Questions
1. "When a client RFP asks for your diversity data, how quickly can you produce accurate numbers — and how confident are you in them?"
2. "Do you know where in your recruiting funnel underrepresented candidates are dropping off?"
3. "How do you measure whether your DEI initiatives are actually moving the needle on representation and retention?"
4. "Can you break down your diversity data by department and level — for example, what does representation look like in creative leadership versus account management?"

#### Industry Context
The 4A's (American Association of Advertising Agencies) publishes annual diversity benchmarks. In 2024, the industry was approximately 68% white, with Black representation at 8.2% (vs. 13.6% US population) and Hispanic/Latino at 12.1% (vs. 19.1%). Leadership (VP+) is even less diverse. Clients are putting real teeth behind DEI requirements: some include diversity clauses in agency contracts with financial penalties. Agencies with strong DEI programs are winning disproportionate new business — it's a competitive advantage, not just compliance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a DEI Tracking & Reporting workspace. Include:
> 1. **Workforce Demographics Dashboard Board** — columns: Department (dropdown), Level Tier (dropdown: IC, Manager, Director, VP+, C-Suite), Total Headcount (numbers), Female % (numbers), Male % (numbers), Non-Binary % (numbers), Black % (numbers), Hispanic/Latino % (numbers), Asian % (numbers), White % (numbers), Two+ Races % (numbers), LGBTQ+ % (numbers), Disability % (numbers), Veteran % (numbers), Last Updated (date)
> 2. **DEI Initiatives** — columns: Initiative Name (text), Category (dropdown: Recruiting, Retention, Development, Culture, Community, Supplier Diversity), Owner (people), Status (status: Proposed, Active, Paused, Complete), Target Metric (text), Baseline (numbers with %), Current (numbers with %), Goal (numbers with %), Budget (numbers with $), Start Date (date), Target Completion (date), Impact Notes (long text)
> 3. **Pipeline Diversity Tracker** — columns: Quarter (dropdown), Role Level (dropdown), Total Applicants (numbers), Diverse Applicants % (numbers), Phone Screen % (numbers), Interview % (numbers), Offer % (numbers), Accepted % (numbers), Drop-Off Stage (text), Notes (long text)
>
> Dashboard with diversity by department and level heat map, initiative progress tracking, pipeline conversion by demographic, and year-over-year trends. Include comparison benchmarks row for 4A's industry averages."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DEI Insight Engine
**Agent Purpose:** Automate DEI data collection, surface actionable insights, and generate stakeholder-ready reports.

**Triggers:**
- Quarterly schedule: DEI metrics refresh
- New RFP flagged as requiring DEI data
- DEI initiative milestone reached
- Significant demographic shift detected (>2% change in any metric)

**Actions:**
- Pull and aggregate workforce demographic data from HRIS
- Generate department-level DEI scorecards with trend analysis
- Produce RFP-ready DEI summary with industry benchmark comparisons
- Identify retention risk patterns by demographic (e.g., higher turnover among Black employees at 18-month mark)
- Track DEI initiative progress against goals and flag off-track programs
- Generate board-ready annual DEI report with visualizations

**Data Required:**
- HRIS demographic data (anonymized and aggregated)
- Recruiting pipeline data by demographic
- Promotion and retention data by demographic
- Industry benchmark data (4A's, ANA)
- DEI initiative goals and progress metrics

**Autonomy Level:** Fully Autonomous
Data aggregation and reporting are fully automated. Sensitive findings (e.g., concerning demographic trends) are flagged to CHRO for action.

**Example Interaction:**
> The agency receives an RFP from Unilever that includes a mandatory DEI section. DEI Insight Engine auto-generates a customized DEI summary within minutes: "Agency DEI Profile (Q4 2025): Overall diversity: 47% people of color (vs. 4A's benchmark 32%). Creative department: 38% women in Director+ roles (up from 31% YoY). Active initiatives: Multicultural Creative Fellowship (12 fellows placed, 83% conversion to FTE), Black Leadership Accelerator (8 participants, 3 promoted). Pipeline diversity: 52% of interviewed candidates are from underrepresented groups. Areas of focus: Hispanic/Latino representation in Strategy department below benchmark — targeted recruiting program launched Q3." The report includes charts and is formatted for direct insertion into the RFP response.

---

### Use Case 6: Learning & Development for Emerging Platforms

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
The advertising landscape evolves faster than agencies can train their people. AI tools (Midjourney, DALL-E, ChatGPT), new platforms (TikTok Shop, Threads, Bluesky), emerging channels (CTV, retail media, DOOH), and new ad formats (interactive video, AR try-on, shoppable content) require constant upskilling. But L&D in agencies is ad hoc: a few people attend conferences, knowledge stays in silos, and there's no systematic way to assess skill gaps or track development. Junior staff learn by osmosis rather than structured training. The result: agencies pitch capabilities they can't consistently deliver because only 2–3 people actually know the platform.

#### The Solution
monday.com Work Management for a structured L&D program. Track skill inventories across the agency, identify gaps against client needs and industry trends, manage training programs from planning through completion, and measure impact. Learning paths are customized by role and career level. Certification tracking ensures the agency maintains platform partnerships (Google Partner, Meta Business Partner, TikTok Marketing Partner).

#### The Outcome
- Complete skill inventory across the agency — know exactly who knows what
- 40% increase in platform certification coverage
- Structured learning paths reduce time-to-competency for new platforms by 50%
- Agency can confidently pitch emerging platform capabilities backed by trained staff

#### Discovery Questions
1. "If a client asks 'How many of your media planners are certified on The Trade Desk?' — can you answer instantly?"
2. "How do you decide what training to invest in — is it reactive (client asks for TikTok expertise) or proactive?"
3. "What happens when one person on the team knows a platform deeply and they leave — how do you handle that knowledge risk?"
4. "How do you currently track whether training investments actually improve work quality or win rates?"

#### Industry Context
Platform certifications are table stakes for agency partnerships — Google, Meta, Amazon, and TikTok all have partner programs with certification requirements. Agencies that maintain partner status get early access to beta features, priority support, and co-marketing opportunities. The rise of AI in creative production (generative imagery, AI copywriting, automated media optimization) means agencies need to upskill their entire workforce, not just a dedicated AI team. The 4A's estimates that 65% of agency roles will require AI literacy by 2027.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Learning & Development workspace for an advertising agency. Include:
> 1. **Skill Inventory** — columns: Employee (people), Department (dropdown), Role (text), Core Skills (dropdown multi-select: Google Ads, Meta Ads, TikTok Ads, The Trade Desk, DV360, Programmatic, SEO, Content Strategy, AI/ML, Data Analytics, Creative Suite, Motion Design, UX/UI, Video Production, CTV, Retail Media), Skill Level (status per skill: Beginner, Intermediate, Advanced, Expert), Certifications (dropdown multi-select: Google Partner, Meta Blueprint, TikTok Academy, Amazon Ads, HubSpot), Cert Expiry Dates (date), Last Assessment (date)
> 2. **Training Programs** — columns: Program Name (text), Platform/Topic (dropdown), Format (dropdown: Online Course, Workshop, Conference, Mentorship, Hands-On Project), Duration (text), Cost per Person (numbers with $), Target Audience (dropdown multi-select: Creative, Media, Strategy, Account, All), Status (status: Planned, Enrolling, In Progress, Complete), Enrolled (numbers), Completed (numbers), Completion Rate (formula), Satisfaction Score (numbers 1-5)
> 3. **Certification Tracker** — columns: Employee (people), Certification (text), Platform (dropdown), Status (status: Not Started, In Progress, Certified, Expired), Earned Date (date), Expiry Date (date), Renewal Required (checkbox), Department (dropdown)
>
> Automations: When Certification Expiry is within 60 days, notify employee and manager. When new Training Program Status changes to 'Enrolling', notify target audience. Dashboard with certification coverage by platform, skill gap heat map by department, training completion rates, and L&D spend analysis."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SkillNavigator
**Agent Purpose:** Identify skill gaps, recommend training paths, and ensure the agency maintains competitive platform expertise.

**Triggers:**
- Quarterly skill gap analysis schedule
- New client win (assess team capabilities against client needs)
- Certification approaching expiration
- New platform/tool added to agency tech stack

**Actions:**
- Analyze skill inventory against current client roster and identify gaps
- Generate personalized learning recommendations by employee and role
- Track certification renewals and auto-enroll employees in renewal courses
- Produce quarterly L&D report for leadership (gaps, investments, ROI)
- Monitor industry trends and flag emerging skill needs (e.g., "retail media is growing — only 4 people certified")
- Match internal experts to mentorship opportunities

**Data Required:**
- Employee skill profiles and certification status
- Client roster and capability requirements
- Training catalog with costs and schedules
- Industry certification requirements
- Platform partner program requirements

**Autonomy Level:** Human-in-the-Loop
Autonomous for analysis, recommendations, and certification tracking. Training investments and mandatory programs require L&D manager approval.

**Example Interaction:**
> The agency wins a retail media account (Target's agency of record for Roundel). SkillNavigator immediately assesses the team: "Retail Media capability audit for Target AOR: Current certified staff: 2 (Amazon Ads certified only). Roundel-specific expertise: 0. Recommended actions: (1) Enroll media team leads in Roundel certification program (8-week course, $500/person, 5 recommended). (2) Transfer Sarah K. from Walmart Connect team — closest skill match. (3) Schedule knowledge-share session with our Amazon Retail team. Gap severity: HIGH — client onboarding in 6 weeks. Budget estimate: $4,500 for certifications + 40 hours internal training time."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| AOR (Agency of Record) | The primary agency handling a brand's advertising across all or specific channels |
| ECD (Executive Creative Director) | Top creative leader in an agency, reports to CCO |
| CCO (Chief Creative Officer) | Highest creative role, sets creative vision for the agency |
| Holding Company | Conglomerate that owns multiple agencies (WPP, Publicis, Omnicom, IPG, Dentsu, Havas) |
| Billable Utilization | Percentage of an employee's time that can be billed to clients — the core profitability metric |
| Book (Portfolio) | A creative professional's portfolio of work, the primary hiring criterion |
| Pitch | Competitive process where agencies present ideas to win new client business |
| Scope of Work (SOW) | Contractual definition of deliverables, timeline, and fees between agency and client |
| Retainer | Ongoing monthly fee arrangement (vs. project-based) for agency services |
| FTE (Full-Time Equivalent) | Standard measure of workforce size, including the freelancer-to-FTE ratio |
| 4A's | American Association of Advertising Agencies — the primary industry trade body |
| AB5 | California law (Assembly Bill 5) that tightened independent contractor classification rules |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief People Officer / CHRO | HR strategy, culture, DEI executive sponsor, talent retention | Decision-maker |
| VP of Talent / Head of HR | Day-to-day HR operations, policy, compliance, employee relations | Decision-maker |
| Talent Acquisition Lead | Recruiting strategy, employer branding, pipeline management | Influencer |
| HR Business Partner | Embedded HR support for specific departments or offices | User/Influencer |
| L&D Manager | Training programs, skill development, certification tracking | User/Influencer |
| DEI Director | Diversity strategy, metrics, ERG management, client DEI requirements | Influencer |
| Office Manager / Workplace Experience | Physical space, hybrid work logistics, perks, events | User |
| Chief Financial Officer | Headcount budget, freelancer spend, compensation bands | Decision-maker (budget) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Creative | Primary source of hiring demand, performance management complexity, and freelancer needs | Connect recruiting pipeline to project staffing — hire based on real-time capacity gaps |
| Finance | Headcount budgets, freelancer spend tracking, compensation benchmarking | Unified workforce cost dashboard covering FTEs + freelancers + benefits |
| Operations / Resource Management | Staff allocation, utilization tracking, capacity planning | Integrate HR data with resource management for complete workforce planning |
| IT | Tool provisioning, access management, security compliance | Automate IT provisioning as part of onboarding/offboarding workflows |
| Executive Leadership | Org design, culture, succession planning, DEI accountability | Leadership dashboards with talent health metrics, succession pipeline, DEI progress |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Greenhouse / Lever | ATS for recruiting pipeline | monday.com provides recruiting plus onboarding plus performance in one platform — eliminates the ATS silo |
| BambooHR / Lattice | Mid-market HRIS and performance management | monday.com offers greater flexibility and customization without rigid HR-specific workflows — agencies need creative role support, not corporate HR templates |
| Workday / SuccessFactors | Enterprise HRIS for large organizations | monday.com supplements (not replaces) enterprise HRIS with agile workflow automation — the layer between HRIS data and actual HR work |
| Culture Amp | Employee engagement and performance analytics | monday.com combines action management with insight — survey results connect to initiatives that are tracked to completion |
| Asana / Notion | General project management adapted for HR workflows | monday.com provides HR-specific automations, forms, and dashboards with better structure than generic tools |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have an HRIS — we don't need another HR tool" | "monday.com doesn't replace your HRIS — it's the workflow layer your HRIS doesn't provide. Your HRIS stores employee data; monday.com manages the work of HR: recruiting coordination, onboarding workflows, review cycles, DEI initiatives. Think of it as the operating system for how HR actually gets things done." |
| "Our HR team is too small to implement another system" | "That's exactly why you need it. When you have 3 HR people managing 400 employees + 200 freelancers, automation isn't a luxury — it's survival. Automating onboarding alone saves 5 hours per new hire. With 30% turnover, that's hundreds of hours per year back." |
| "Agency people hate process — they'll never adopt this" | "Agency people hate *unnecessary* process. They don't hate tools that save them time. When a hiring manager can see their recruiting pipeline without emailing HR, when a new hire's onboarding just *works*, when freelancer booking takes hours instead of days — that's not process, that's removing friction." |
| "We're an agency — our needs are unique and tools never fit" | "Exactly why monday.com's flexibility matters. Unlike rigid HRIS tools designed for corporate HR, monday.com adapts to agency realities: freelancer management, portfolio-based hiring, creative role career ladders, project-based performance reviews. You build the workflows that match how your agency actually works." |
| "We can't afford to track DEI — it's too sensitive and complex" | "You can't afford *not* to. Clients are requiring DEI data in RFPs — it's becoming a revenue question, not just an HR initiative. monday.com lets you track aggregated, anonymized metrics that satisfy client requirements and internal goals without exposing individual-level sensitive data." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for agency using monday.com for recruiting and talent management]
- [Placeholder for holding company standardizing HR workflows on monday.com]
- [Placeholder for mid-market agency managing freelancer workforce with monday.com]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
