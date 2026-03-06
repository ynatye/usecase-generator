# Training × PMO Playbook

## Overview

The Training industry — encompassing corporate training providers, e-learning platforms, professional development firms, and certification bodies — relies heavily on project-based delivery. Whether designing a multi-module leadership development curriculum for a Fortune 500 client or rolling out a compliance training program across 30,000 employees, training organizations operate through structured engagements that mirror classic project and program management disciplines. PMO teams in training companies serve as the operational backbone, coordinating instructional designers, facilitators, LMS administrators, client success managers, and subject matter experts across dozens of concurrent programs.

A typical mid-sized training company may run 40-80 active client engagements simultaneously, each with distinct timelines, resource requirements, deliverable milestones, and client review cycles. The PMO must track everything from needs analysis through design, development, pilot delivery, revision, full rollout, and post-training evaluation (Kirkpatrick Levels 1-4). Complexity multiplies when programs span multiple modalities — instructor-led training (ILT), virtual instructor-led training (VILT), self-paced e-learning, blended learning, and microlearning — each with different production workflows and resource needs.

Regulatory and certification pressures add another layer. Training organizations serving healthcare, financial services, or government clients must ensure curricula meet specific accreditation standards (e.g., IACET CEUs, CPE credits, CME requirements). The PMO must track certification compliance, version control on regulated content, and audit trails — all while maintaining the agility to respond to client change requests that are endemic to custom training engagements.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Training PMOs manage exponentially more programs as clients demand blended/digital delivery, but headcount stays flat |
| 2 | Replace or Radically Augment Headcount | Medium-High | Project coordinators spend 60%+ of time on status chasing, resource scheduling, and manual reporting — all automatable |
| 3 | Consolidate Tech Stack with AI | Medium | PMOs typically cobble together Smartsheet/MS Project + LMS + Sharepoint + email — fragmented and expensive |

## Prioritized Use Cases

---

### Use Case 1: Multi-Program Portfolio Dashboard

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training PMOs lack a single view of all active client engagements. Program managers maintain individual spreadsheets or MS Project files, making it impossible to see cross-program resource conflicts, at-risk timelines, or revenue recognition milestones at the portfolio level. Weekly status meetings consume 4-6 hours just to compile updates, and leadership still gets stale data. When a key instructional designer is double-booked across three programs, no one knows until a deadline is missed.

#### The Solution
monday.com Work Management with a portfolio-level workspace. Each client engagement is a board with standardized phases (Needs Analysis → Design → Development → Pilot → Revision → Rollout → Evaluation). A master dashboard aggregates all programs with filters by client, modality, phase, risk level, and PM owner. Timeline views show cross-program dependencies and resource allocation. Status automations flag programs that haven't been updated in 48+ hours. Dashboard widgets display revenue pipeline by program phase, resource utilization heat maps, and milestone completion rates.

#### The Outcome
60% reduction in status meeting time. Real-time portfolio visibility for leadership. Early detection of resource conflicts (2+ weeks earlier than manual tracking). 25% improvement in on-time program delivery through proactive risk identification.

#### Discovery Questions
1. "How many active client training programs are you managing concurrently right now, and how do you get a single view across all of them?"
2. "When a senior instructional designer is needed on three programs simultaneously, how quickly does that conflict surface?"
3. "What does your weekly status reporting process look like — how many hours does it take to compile?"
4. "Have you ever had a program go red because a dependency in another program wasn't visible?"
5. "How do you currently track the revenue recognition milestones tied to program delivery phases?"

#### Industry Context
Training companies typically measure program health against the ADDIE model (Analysis, Design, Development, Implementation, Evaluation) or SAM (Successive Approximation Model). Programs can range from 2-week rapid development sprints to 18-month enterprise rollouts. Revenue is often milestone-based: 30% at design approval, 40% at pilot delivery, 30% at full rollout sign-off. Understanding this billing cadence is critical because PMO reporting directly ties to cash flow.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Training Program Portfolio Management system in monday.com. Create a board called 'Active Programs' with these columns: Program Name (text), Client (dropdown: list of clients), Program Manager (people), Phase (status with labels: Needs Analysis, Design, Development, Pilot, Revision, Rollout, Evaluation, Complete), Modality (dropdown: ILT, VILT, E-Learning, Blended, Microlearning), Start Date (date), Target Completion (date), Risk Level (status: Green, Yellow, Red), Revenue Value (numbers in $), Billing Milestone (status: Not Started, Design Approved, Pilot Delivered, Rollout Complete, Invoiced), Resource Hours Remaining (numbers), Last Updated (date). Add a Timeline view showing all programs on a Gantt-style timeline. Create a Dashboard with widgets: program count by phase (chart), programs by risk level (chart), total revenue by billing milestone (numbers), resource utilization summary (table), and overdue programs list (filtered table showing programs where Target Completion < today and Phase != Complete). Add automations: when Phase changes notify the Program Manager, when Last Updated is more than 2 days ago set Risk Level to Yellow, when Risk Level changes to Red notify the PMO Director."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio Pulse Agent
**Agent Purpose:** Continuously monitor all training programs and proactively surface risks, resource conflicts, and milestone deadlines before they become problems.

**Triggers:**
- Daily at 8:00 AM — full portfolio scan
- When any program's Phase status changes
- When Risk Level is changed to Red
- When Target Completion date is within 5 business days
- When Resource Hours Remaining drops below 20% of original estimate

**Actions:**
- Generate a daily portfolio health summary with programs by risk tier, upcoming milestones, and resource alerts
- Detect resource double-booking by cross-referencing People columns across all active programs and flag conflicts
- Auto-escalate programs that haven't had a phase transition in 2x the expected duration for that phase
- Notify finance team when a program hits a billing milestone (phase change = invoice trigger)
- Create a weekly leadership brief summarizing portfolio velocity, completion rate, and forecast revenue

**Data Required:**
- All active program boards with standardized phase columns
- Resource allocation data (People columns across boards)
- Historical phase duration benchmarks
- Client contract milestones and billing terms

**Autonomy Level:** Human-in-the-Loop
Auto-generates reports and flags risks; escalation notifications require PM acknowledgment before client communication.

**Example Interaction:**
> On Monday morning, the Portfolio Pulse Agent scans 52 active training programs. It identifies that Sarah Chen, a senior instructional designer, is assigned to the Acme Corp leadership program (entering Development phase) and the GlobalBank compliance program (already in Development). Both programs need her for 30+ hours/week over the next three weeks. The agent sends a resource conflict alert to the PMO Director with a recommendation: "Reassign the GlobalBank storyboarding tasks to Marcus Rivera (currently at 60% utilization) or negotiate a 2-week timeline extension with GlobalBank." Simultaneously, it notices that the MedTech onboarding program has been in Pilot phase for 18 days against a 10-day benchmark. It flags this as amber risk and asks the PM: "The MedTech pilot is 80% over expected duration. Should I escalate to the client success manager or extend the timeline?"

---

### Use Case 2: Instructional Design Workflow Pipeline

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The content development lifecycle in training companies is notoriously chaotic. An instructional designer receives a brief, creates a storyboard, gets SME review, revises, builds in the authoring tool (Articulate, Captivate, etc.), gets client review, revises again — often 3-5 review cycles. Without a structured pipeline, work sits in email inboxes waiting for review. A single compliance training module that should take 3 weeks takes 7 because of review bottlenecks. Project coordinators spend their days chasing people for feedback, manually tracking which module is at which stage, and fielding "where are we?" questions from clients.

#### The Solution
monday.com Work Management as the content production pipeline. Each training module is an item flowing through statuses: Brief Received → Storyboard Draft → SME Review → Storyboard Approved → Build → QA → Client Review → Revisions → Final Approval → Published. Subitems track individual assets (videos, interactions, assessments). File columns hold design documents and review feedback. Automations send review reminders after 48 hours, escalate stalled items after 72 hours, and notify PMs when modules clear client review. A Kanban view gives designers a visual workflow; a Timeline view shows the production schedule.

#### The Outcome
40% reduction in content development cycle time. 70% fewer "where is this?" status inquiries. 90% reduction in review bottleneck time through automated reminders. Clear capacity planning — PMO can see designer workload at a glance and balance assignments.

#### Discovery Questions
1. "Walk me through what happens from the moment a client approves a training design brief to when the finished module is published — how many handoffs are there?"
2. "How long does a typical review cycle take, and how much of that is waiting for feedback versus actual revision work?"
3. "When a client asks 'where is Module 3?', how long does it take someone to find the answer?"
4. "How do you currently balance workload across your instructional design team — do you have visibility into who has capacity?"
5. "What percentage of projects require more than 3 rounds of client revision, and what triggers those extra rounds?"

#### Industry Context
Instructional design follows structured methodologies (ADDIE, SAM, Action Mapping) but the actual production process is highly collaborative and iterative. Content typically goes through storyboard (usually in Word/PowerPoint), development (in tools like Articulate Storyline, Rise, Adobe Captivate, or Lectora), and QA/review cycles. Each module might contain 15-40 slides/screens with interactions, assessments, and media. A single e-learning course might comprise 8-12 modules. Understanding the distinction between "storyboard review" (content accuracy) and "build review" (functionality/UX) is important — they involve different reviewers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Content Development Pipeline in monday.com. Create a board called 'Module Production Pipeline' with columns: Module Name (text), Program (connect board to Active Programs), Assigned Designer (people), Modality (dropdown: E-Learning, Video, ILT Materials, Assessment, Job Aid), Status (status: Brief Received, Storyboard Draft, SME Review, Storyboard Approved, Build, QA, Client Review, Revisions, Final Approval, Published), Priority (status: Urgent, High, Normal, Low), Due Date (date), Estimated Hours (numbers), Actual Hours (numbers), Review Round (numbers, default 1), Storyboard File (file), Build File (file), Review Feedback (long text), SME Reviewer (people), Client Reviewer (people). Add subitems for individual assets within each module (videos, interactions, assessments). Create a Kanban view grouped by Status. Add a Timeline view for production scheduling. Add automations: when Status changes to SME Review notify SME Reviewer, when item stays in SME Review for more than 2 days send reminder to SME Reviewer, when Status changes to Client Review notify Client Reviewer and Program Manager, when Status changes to Published update the connected Program board phase. Create a Dashboard with: modules by status (chart), average cycle time by modality (chart), designer workload (table showing count of active modules per designer), overdue modules (filtered list)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Content Flow Optimizer
**Agent Purpose:** Eliminate bottlenecks in the instructional design pipeline by predicting delays, auto-nudging reviewers, and optimizing designer assignments.

**Triggers:**
- When any module enters a review status (SME Review or Client Review)
- When a module has been in the same status for more than the average duration for that status
- Daily scan of all in-progress modules
- When a new module is created (Brief Received)
- When Review Round exceeds 3

**Actions:**
- Send personalized review reminders with context ("Module 4 of the Acme Leadership program needs your SME review — here's the storyboard link")
- Predict completion dates based on historical cycle times for similar modality/complexity modules
- Recommend designer assignment for new modules based on current workload, skill match (modality expertise), and availability
- Flag modules exceeding 3 review rounds for PM intervention with analysis of revision patterns
- Auto-generate weekly production velocity reports (modules completed, average cycle time, bottleneck analysis)

**Data Required:**
- Historical module production data (cycle times by status, modality, designer)
- Designer skill profiles and current assignments
- Client review SLA commitments
- Program timeline dependencies

**Autonomy Level:** Escalation-Based
Autonomously sends reminders and generates reports. Recommends designer assignments for PM approval. Escalates excessive review rounds to PM with suggested actions.

**Example Interaction:**
> The Content Flow Optimizer notices that Module 6 of the NovaChem safety training has been in Client Review for 4 days — 2x the average for this client. It checks the client reviewer's pattern and sees they typically review on Tuesdays and Thursdays. It sends a gentle reminder: "Hi Dr. Patel — Module 6 (Hazardous Materials Handling) is ready for your review. The full rollout is scheduled for March 15, and we'll need 5 business days for revisions after your feedback. Would you be able to review by Thursday?" It also alerts the PM: "NovaChem Module 6 review is at risk. If feedback isn't received by Thursday, the March 15 rollout date may need to shift by 3-5 days. Shall I draft an email to the client project sponsor?"

---

### Use Case 3: Training Resource & Facilitator Scheduling

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies must coordinate facilitators, venues (physical or virtual), equipment, and materials across dozens of delivery events monthly. A facilitator might deliver ILT sessions for three different clients in a week, each requiring different prep materials, travel arrangements, and technology setups. When a client reschedules a session, the ripple effects — facilitator availability, venue rebooking, material reprinting — are managed through email chains and personal calendars. Double-bookings happen. Facilitators show up without the right materials. Venue conflicts surface the day before delivery.

#### The Solution
monday.com Work Management for resource and facilitator scheduling. A "Delivery Calendar" board tracks every training session with columns for facilitator, client, program, venue/platform, date/time, session type, prep status, and materials checklist. A "Facilitator Availability" board shows each trainer's schedule, certifications, and subject matter expertise. Timeline views show facilitator utilization across the month. Automations trigger prep checklists 5 days before each session, send facilitator confirmation 48 hours out, and alert the PMO when a facilitator is booked above 80% capacity in a given week.

#### The Outcome
Zero double-bookings (down from 2-3/month). 50% reduction in scheduling coordination time. 95% facilitator prep completion rate (up from ~70%). Better facilitator utilization — identify underutilized trainers and redistribute workload.

#### Discovery Questions
1. "How many training delivery events do you coordinate per month, and how many facilitators are involved?"
2. "When a client reschedules a training session, what does the rebooking process look like — how many people need to be notified and how many things need to change?"
3. "Have you ever had a facilitator double-booked or show up to a session without the right materials? What was the impact?"
4. "How do you match facilitators to sessions — is it just availability, or do you factor in expertise, client relationships, and certifications?"
5. "What's your current facilitator utilization rate, and do you have visibility into it?"

#### Industry Context
Training delivery logistics are complex. ILT sessions require venue booking (corporate training rooms, hotel conference facilities, or client sites), AV equipment, printed materials, and often catering. VILT requires platform setup (Zoom, Teams, WebEx), breakout room configuration, virtual whiteboard prep, and tech checks. Facilitators often need specific certifications to deliver certain programs (e.g., certified DiSC facilitator, certified Lean Six Sigma trainer). Travel time between client sites must be factored into scheduling. Cancellation and rescheduling policies vary by client contract.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Facilitator Scheduling & Delivery Management system in monday.com. Create a board called 'Training Delivery Calendar' with columns: Session Name (text), Client (dropdown), Program (connect board to Active Programs), Facilitator (people), Session Date (date), Start Time (text), End Time (text), Delivery Mode (dropdown: ILT, VILT, Hybrid), Venue/Platform (text), Prep Status (status: Not Started, Materials Ready, Tech Checked, Fully Prepped), Materials Checklist (checkbox: Slides Updated, Handouts Printed, Assessments Ready, Tech Tested), Travel Required (checkbox), Travel Booked (checkbox), Session Status (status: Scheduled, Confirmed, Delivered, Cancelled, Rescheduled). Create a second board called 'Facilitator Roster' with columns: Name (people), Certifications (tags), Subject Areas (tags), Max Weekly Hours (numbers), Home Location (text), Availability Notes (long text). Add a Timeline view on the Delivery Calendar showing sessions across the month by Facilitator. Create a Calendar view filtered by week. Add automations: 5 days before Session Date set Prep Status to Not Started and notify Facilitator, 2 days before Session Date if Prep Status is not Fully Prepped notify PMO coordinator, when Session Status changes to Cancelled notify all connected people. Create a Dashboard with: sessions this month by Delivery Mode (chart), facilitator utilization (sessions per facilitator this month), upcoming sessions needing prep (filtered list where Prep Status != Fully Prepped and Session Date is within 7 days)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Scheduling Concierge Agent
**Agent Purpose:** Intelligently manage facilitator scheduling, prevent conflicts, optimize assignments, and ensure every session is fully prepped.

**Triggers:**
- When a new training session is created
- When a session date is changed (rescheduled)
- When a session is cancelled
- 5 days before any session date
- When a facilitator's availability changes

**Actions:**
- Recommend the best facilitator for a new session based on availability, certification match, subject expertise, client history, and travel minimization
- Detect and alert on scheduling conflicts before they're confirmed
- Auto-generate prep checklists customized by delivery mode and program type
- Cascade rescheduling impacts — identify all downstream effects when a session moves
- Send facilitator briefing packets 3 days before each session (client context, participant list, materials links, venue/platform details)

**Data Required:**
- Facilitator Roster board (certifications, availability, location)
- Training Delivery Calendar (all scheduled sessions)
- Client preferences and history
- Program materials repository links

**Autonomy Level:** Human-in-the-Loop
Recommends facilitator assignments; PMO coordinator confirms. Autonomously sends prep reminders and briefing packets. Escalates conflicts immediately.

**Example Interaction:**
> A new 3-day leadership workshop is added for Deloitte, scheduled for March 10-12 in Chicago. The Scheduling Concierge scans the Facilitator Roster: "Three facilitators are certified for this program. Maria Lopez is available but based in Boston (travel required). James Park is in Chicago but has a VILT session on March 11. Priya Sharma is available and in Chicago — recommended as primary. Shall I assign Priya and send her the client brief?" The PMO confirms. Three days before the session, the agent sends Priya a complete briefing: participant list (18 senior managers), room setup requirements (U-shape, 2 flip charts), materials links, and a note: "Deloitte prefers real-world case studies over theoretical frameworks — their L&D director mentioned this in the last engagement debrief."

---

### Use Case 4: Client Engagement & Feedback Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies live and die by client satisfaction and repeat business. After each training delivery, feedback is collected — participant evaluations (Level 1 Kirkpatrick), post-training assessments (Level 2), and sometimes behavioral change surveys (Level 3). This data lives in SurveyMonkey, Google Forms, the LMS, or paper forms. PMOs manually compile satisfaction scores, NPS, and qualitative feedback into client reports. When it's time for a quarterly business review (QBR) with a client, the PM spends days pulling data from five different sources. Trends across programs are invisible — no one knows which facilitators consistently score highest or which program designs generate the most complaints.

#### The Solution
monday.com as the central client engagement hub. A "Client Feedback Tracker" board captures post-delivery evaluations with columns for program, session, facilitator, overall satisfaction score, NPS, key themes, and action items. Automations pull scores from integrated survey tools. Dashboards show satisfaction trends by client, program, facilitator, and modality over time. A "Client Relationship" board tracks engagement history, contract value, renewal dates, and expansion opportunities. QBR preparation becomes a dashboard export rather than a manual compilation exercise.

#### The Outcome
80% reduction in QBR preparation time (from 2 days to 2 hours). Real-time satisfaction visibility across all clients. Data-driven facilitator coaching — identify who needs support. 15% improvement in contract renewal rates through proactive relationship management.

#### Discovery Questions
1. "After a training session is delivered, walk me through how participant feedback gets collected, compiled, and reported back to the client."
2. "How long does it take to prepare for a Quarterly Business Review with a major client?"
3. "Do you have visibility into satisfaction trends across programs — for example, can you quickly see if a particular program design is consistently underperforming?"
4. "How do you currently track the health of your client relationships — renewal dates, expansion opportunities, at-risk accounts?"
5. "When a participant gives negative feedback, how quickly does that information reach someone who can act on it?"

#### Industry Context
The Kirkpatrick Model is the industry standard for training evaluation: Level 1 (Reaction — did they like it?), Level 2 (Learning — did they learn?), Level 3 (Behavior — are they applying it?), Level 4 (Results — business impact). Most training companies excel at Level 1 collection but struggle with Levels 2-4. NPS for training programs typically ranges 30-60 for good providers. Client contracts are often annual with quarterly or semi-annual QBRs. The renewal cycle is the lifeblood of training revenue — losing a major client engagement can mean $200K-$2M in lost annual revenue.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client Feedback & Engagement Tracker in monday.com. Create a board called 'Session Feedback Tracker' with columns: Session (connect board to Training Delivery Calendar), Program (text, mirror from connected board), Client (dropdown), Facilitator (people, mirror from connected board), Delivery Date (date, mirror), Response Rate (numbers as %), Overall Satisfaction (numbers, 1-5 scale), NPS Score (numbers, -100 to 100), Key Positive Themes (tags), Key Improvement Areas (tags), Action Items (long text), Action Owner (people), Action Status (status: Open, In Progress, Resolved). Create a second board called 'Client Relationships' with columns: Client Name (text), Primary Contact (text), Contract Value (numbers in $), Contract Start (date), Renewal Date (date), Engagement Health (status: Thriving, Stable, At Risk, Critical), Programs Active (numbers), Lifetime Satisfaction Avg (numbers), Last QBR Date (date), Next QBR Date (date), Expansion Opportunities (long text). Add automations: when a new feedback item is created with Overall Satisfaction below 3.5 notify PMO Director and tag as At Risk, 30 days before Renewal Date on Client Relationships notify account manager. Create a Dashboard with: average satisfaction by client (chart), satisfaction trend over time (chart), NPS distribution (chart), facilitator performance comparison (chart), upcoming renewals in 90 days (filtered table), open action items (filtered list)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Client Pulse Agent
**Agent Purpose:** Monitor client satisfaction continuously and proactively identify at-risk relationships before renewal conversations.

**Triggers:**
- When new feedback scores are logged
- When Overall Satisfaction drops below 3.5 on any session
- 60 days before any client renewal date
- When 3+ action items from feedback are overdue
- Weekly digest every Monday

**Actions:**
- Analyze feedback trends and generate a satisfaction trajectory for each client (improving, stable, declining)
- Alert account managers when a client's rolling 90-day satisfaction average drops below historical baseline
- Auto-generate QBR slide decks pulling satisfaction data, program delivery stats, and action item resolution rates
- Recommend proactive outreach when feedback signals indicate potential churn risk
- Compile facilitator performance insights for coaching conversations

**Data Required:**
- Session Feedback Tracker (all historical feedback)
- Client Relationships board (contract terms, renewal dates)
- Training Delivery Calendar (delivery history)
- Facilitator Roster (for performance correlation)

**Autonomy Level:** Escalation-Based
Autonomously tracks trends and generates reports. Escalates at-risk clients to account managers with recommended actions. QBR deck generation is automatic; PM reviews before sending to client.

**Example Interaction:**
> The Client Pulse Agent detects that Meridian Healthcare's last three training sessions scored 3.2, 3.4, and 3.1 — a downward trend from their historical average of 4.2. It analyzes the feedback themes and finds a pattern: "Participants consistently mention 'outdated case studies' and 'too theoretical, not enough hands-on practice.' These themes appeared in 78% of recent feedback." It alerts the account manager: "Meridian Healthcare satisfaction is declining. Recommend scheduling a curriculum refresh meeting before the April QBR. Their contract renewal is in June — current trajectory puts renewal confidence at 60%. Suggested talking points: updated industry case studies, more simulation-based exercises, and a pilot of the new microlearning reinforcement modules."

---

### Use Case 5: Learning Program ROI & Impact Reporting

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Training companies are increasingly expected to demonstrate the business impact of their programs beyond "participants liked it." Clients want Kirkpatrick Level 3-4 data: are participants applying the skills? Is there measurable business impact? But collecting, analyzing, and presenting this data is enormously labor-intensive. A single ROI report for a major program can take a consultant 40+ hours to compile — pulling LMS completion data, pre/post assessment scores, manager surveys, business metrics, and weaving it into a compelling narrative. Most training companies simply don't do it because they can't afford the analyst time.

#### The Solution
monday.com as the impact measurement hub. A "Program Impact Tracker" board captures metrics at each Kirkpatrick level with automated data collection where possible. Pre/post assessment scores flow in from LMS integrations. Manager survey results are captured via monday forms. Business metrics (productivity, quality, safety incidents, etc.) are logged quarterly. Dashboards automatically calculate learning gain, application rates, and correlate with business outcomes. Report templates auto-populate with program-specific data, reducing the 40-hour report to a 4-hour review-and-refine process.

#### The Outcome
90% reduction in ROI report creation time. Ability to produce impact reports for 5x more programs (previously only done for top 3 clients). Stronger renewal conversations backed by data. Premium pricing justification — companies that prove ROI can charge 20-30% more.

#### Discovery Questions
1. "How many of your client programs currently have Kirkpatrick Level 3 or Level 4 measurement in place?"
2. "When a client asks 'what was the ROI of the training we bought?' — what does your response process look like?"
3. "How much analyst or consultant time goes into creating a single impact report?"
4. "Do you believe your inability to consistently prove training ROI has cost you renewals or upsells?"
5. "If you could produce compelling impact reports for every program, not just your top clients, how would that change your competitive positioning?"

#### Industry Context
Training ROI measurement is a known industry pain point. The ATD (Association for Talent Development) reports that fewer than 15% of training programs are measured at Kirkpatrick Level 3 (Behavior) and fewer than 5% at Level 4 (Results). Jack Phillips' ROI Methodology adds a Level 5 (ROI calculation). The formula: ROI = ((Benefits - Costs) / Costs) × 100. Training companies that can consistently demonstrate ROI differentiate themselves dramatically. Common business metrics for ROI include: time to competency, error rates, customer satisfaction scores, safety incident rates, employee retention, and sales performance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Program Impact & ROI Tracker in monday.com. Create a board called 'Program Impact Tracker' with columns: Program Name (connect board to Active Programs), Client (dropdown), Evaluation Level (status: Level 1 - Reaction, Level 2 - Learning, Level 3 - Behavior, Level 4 - Results, Level 5 - ROI), Participant Count (numbers), Pre-Assessment Average (numbers as %), Post-Assessment Average (numbers as %), Learning Gain (formula: Post minus Pre), Application Rate (numbers as %, from manager surveys), Business Metric Name (text), Baseline Value (numbers), Post-Training Value (numbers), Improvement Percentage (formula), Program Cost (numbers in $), Estimated Business Value (numbers in $), ROI Percentage (formula: (Business Value minus Cost) divided by Cost times 100), Data Collection Status (status: Not Started, Surveys Sent, Data Collected, Analysis Complete, Report Delivered), Report Due Date (date). Add a form for managers to submit 90-day post-training observations (application frequency, skill demonstration, performance impact on 1-5 scale). Create a Dashboard with: average learning gain by program type (chart), ROI distribution across programs (chart), programs by evaluation level achieved (chart), data collection pipeline (programs by Data Collection Status), top 10 ROI programs (table sorted by ROI Percentage)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Impact Analyst Agent
**Agent Purpose:** Automate the collection, analysis, and reporting of training program impact data across all Kirkpatrick levels.

**Triggers:**
- 30 days after program rollout completion (trigger Level 2 data collection)
- 90 days after completion (trigger Level 3 manager surveys)
- 180 days after completion (trigger Level 4 business metric collection)
- When all data points for a program are collected (trigger report generation)
- When Report Due Date is within 10 days

**Actions:**
- Auto-send manager surveys at the 90-day mark with pre-populated participant lists and program context
- Calculate learning gain, application rates, and correlate with available business metrics
- Generate draft impact reports with data visualizations, narrative summaries, and ROI calculations
- Identify statistically significant patterns across programs (e.g., "Blended programs show 34% higher application rates than e-learning only")
- Recommend data collection strategies when business metrics are missing or incomplete

**Data Required:**
- LMS data (completion rates, assessment scores)
- Manager survey responses
- Business metric baselines and post-training measures
- Program cost data
- Historical impact data for benchmarking

**Autonomy Level:** Human-in-the-Loop
Autonomously sends surveys and collects data. Generates draft reports for consultant review. ROI calculations are flagged for human validation before sharing with clients.

**Example Interaction:**
> The Impact Analyst Agent processes 90-day data for the Apex Manufacturing safety training program. It compiles: "Level 2 — Average pre-assessment: 62%, post-assessment: 89% (learning gain: 27 points). Level 3 — Manager survey (82% response rate): 73% of participants demonstrating new safety behaviors consistently. Level 4 — Safety incidents in trained departments dropped from 14/quarter (baseline) to 6/quarter (post-training). Estimated annual savings: $340,000 in incident-related costs. Program cost: $85,000. ROI: 300%." It generates a 12-page impact report draft and sends it to the consultant: "Draft ready for your review. Notable: the ROI is significantly above benchmark (typical safety training ROI: 150-200%). Recommend highlighting this in the QBR as a case for expanding to remaining 4 manufacturing sites."

---

### Use Case 6: Change Request & Scope Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training engagements are notorious for scope creep. A client signs a contract for a 5-module e-learning program, then asks to add a video component, expand to 7 modules, translate into Spanish, and "can we also do a facilitator guide?" Each change request requires effort estimation, timeline impact assessment, cost recalculation, and formal approval. Without a structured process, changes get absorbed informally — destroying margins. PMs either say yes to everything (and lose money) or push back awkwardly (and lose client trust). The PMO has no visibility into how much scope creep is eroding profitability across the portfolio.

#### The Solution
monday.com with a "Change Request" board connected to program boards. Each CR is an item with: description, requested by, impact assessment (hours, cost, timeline), approval status, and connection to the original program. Automations route CRs through an approval workflow: PM estimates impact → client reviews → finance approves margin impact → PM implements. Dashboards show total CRs by program, margin impact of approved changes, and pending requests. This creates a professional, transparent process that actually strengthens client relationships.

#### The Outcome
30% reduction in scope creep-driven margin erosion. Professional change management process improves client trust. Full visibility into the real cost of client changes. Data for future proposal pricing — know what extras clients typically request.

#### Discovery Questions
1. "When a client says 'can we also add X to the program?' — what happens next? Is there a formal change request process?"
2. "What percentage of your training programs end up significantly over the original scope?"
3. "How do you estimate the cost and timeline impact of a change request — and how long does that estimation take?"
4. "Have you ever analyzed how much margin you've lost to untracked scope changes across your portfolio?"
5. "How do your project managers feel about pushing back on client requests? Is the process awkward or formalized?"

#### Industry Context
In training, scope creep is endemic because client stakeholders often evolve their understanding of what they need during the project. Common change requests include: additional modules, new audience segments, translation/localization, additional modalities (adding ILT to an e-learning project), accessibility remediation (WCAG compliance), and custom branding. The industry average for scope creep is 15-25% above original contract value — but only about half of that is formally captured and billed. The rest is "absorbed."

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Change Request Management system in monday.com. Create a board called 'Change Requests' with columns: CR Title (text), Program (connect board to Active Programs), Requested By (text), Request Date (date), Description (long text), Impact — Hours (numbers), Impact — Cost (numbers in $), Impact — Timeline Days (numbers), Original Program Value (numbers in $, mirror from connected board), CR as % of Original (formula: Cost divided by Original Program Value times 100), Approval Status (status: Submitted, PM Estimated, Client Reviewed, Finance Approved, Approved, Rejected, Withdrawn), Approved By (people), Implementation Status (status: Not Started, In Progress, Complete), Priority (status: Critical, High, Normal). Add automations: when a new CR is created notify PM and set Approval Status to Submitted, when Approval Status changes to PM Estimated notify client contact, when Approval Status changes to Finance Approved and Impact Cost is above $5000 notify VP of Delivery, when Implementation Status changes to Complete notify Requested By. Create a Dashboard with: total CRs this quarter by program (chart), total approved CR value vs. rejected (numbers), CR margin impact (sum of approved CR costs), average CR processing time (from Submitted to Approved), pending CRs requiring action (filtered table by Approval Status)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Scope Guardian Agent
**Agent Purpose:** Manage change requests efficiently, estimate impacts accurately, and protect program margins while maintaining client satisfaction.

**Triggers:**
- When a new Change Request item is created
- When a CR has been in any approval status for more than 3 business days
- When total approved CRs for a program exceed 20% of original contract value
- Weekly summary every Friday

**Actions:**
- Auto-estimate effort and timeline impact based on CR type and historical data from similar changes
- Generate client-facing CR summaries with professional impact statements
- Alert finance when cumulative CRs on a program cross margin thresholds (10%, 20%, 30%)
- Suggest alternative approaches that might meet client needs with less scope impact
- Compile weekly CR digest for PMO leadership showing portfolio-wide scope creep trends

**Data Required:**
- Historical change requests with actual effort data
- Program budgets and margin targets
- Client contract terms (included vs. excluded scope)
- Pricing benchmarks by change type

**Autonomy Level:** Human-in-the-Loop
Auto-generates estimates and recommendations; PM reviews and adjusts before presenting to client. Margin alerts go directly to finance without PM gatekeeping.

**Example Interaction:**
> A client submits a request to translate the 8-module compliance program into Spanish and Portuguese. The Scope Guardian Agent analyzes: "Historical data shows translation projects average 12 hours per module for text extraction, translation review, and LMS rebuild. Estimated impact: 192 hours, $28,800, +3 weeks to timeline. This would bring total CRs on this program to 31% of original contract value ($93,000). Recommendation: propose a Phase 2 engagement for localization rather than absorbing into current scope. This protects margin and creates a new revenue opportunity. Draft Phase 2 proposal attached." The PM reviews the recommendation and presents a professional proposal to the client — turning scope creep into upsell.

---

### Use Case 7: Vendor & Freelancer Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Training companies frequently rely on a network of freelance instructional designers, voiceover artists, video producers, graphic designers, translators, and SMEs. Managing this extended workforce is chaotic — assignments tracked in email, invoices in spreadsheets, quality reviews in shared drives, and rate cards in someone's head. When a project needs a specific resource (e.g., a voiceover artist who speaks Mandarin with medical terminology experience), finding the right person takes hours of searching through contact lists. Onboarding a new freelancer takes weeks because nobody documented the process.

#### The Solution
monday.com as the freelancer management hub. A "Vendor Roster" board catalogs all freelancers with skills, rates, availability, quality ratings, and specializations. A "Freelance Assignments" board tracks active and completed work with deliverables, deadlines, approval status, and payment status. Automations send assignment briefs, collect deliverables, route for QA review, and trigger payment processing upon approval. Searchable tags make finding the right specialist instant.

#### The Outcome
75% faster freelancer matching for new assignments. Standardized onboarding process (2 days vs. 2 weeks). Complete visibility into freelancer spend and quality. Better rate negotiation backed by utilization data.

#### Discovery Questions
1. "How many freelancers or contract resources do you work with regularly, and how do you find the right person for a specific assignment?"
2. "Where do you track freelancer assignments, deliverables, and payment status today?"
3. "When you need a specialist — say, a voiceover artist who can do medical content in Spanish — how long does it take to find one?"
4. "How do you evaluate freelancer quality over time? Can you quickly see who your top performers are?"
5. "What does your freelancer onboarding process look like — NDAs, style guides, tool access, payment setup?"

#### Industry Context
The training industry has a uniquely large freelance ecosystem. Typical freelancer categories include: instructional designers ($75-150/hr), e-learning developers ($60-120/hr), voiceover artists ($250-500/finished hour of audio), video producers ($100-200/hr), graphic designers ($50-100/hr), translators ($0.15-0.25/word), and subject matter experts ($150-400/hr). Many training companies operate with a 40-60% freelance workforce ratio. Quality control is critical — a poorly designed module reflects on the training company, not the freelancer. Most freelancers work on a project/deliverable basis rather than hourly.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Freelancer Management System in monday.com. Create a board called 'Vendor Roster' with columns: Name (text), Email (email), Role Type (dropdown: Instructional Designer, E-Learning Developer, Voiceover Artist, Video Producer, Graphic Designer, Translator, SME, Other), Specializations (tags: Healthcare, Finance, Tech, Manufacturing, Leadership, Compliance, Safety, Sales), Languages (tags), Hourly Rate (numbers in $), Quality Rating (rating 1-5), Total Assignments (numbers), Last Assignment Date (date), NDA Status (status: Not Sent, Sent, Signed), Onboarding Status (status: New, In Progress, Active, Inactive), Portfolio Link (link), Notes (long text). Create a second board called 'Freelance Assignments' with columns: Assignment Name (text), Freelancer (connect board to Vendor Roster), Program (connect board to Active Programs), Deliverable Description (long text), Due Date (date), Budget (numbers in $), Actual Cost (numbers in $), Deliverable Status (status: Briefed, In Progress, Submitted, In Review, Revision Needed, Approved, Paid), Quality Score (rating 1-5), Deliverable Files (file), Review Notes (long text). Add automations: when Deliverable Status changes to Approved notify finance for payment processing, when Deliverable Status changes to Approved update Quality Rating on connected Vendor Roster item, when Due Date is tomorrow and Deliverable Status is not Submitted notify freelancer. Create a Dashboard with: active freelancers by role type (chart), spend by role type this quarter (chart), average quality rating by freelancer (table), overdue deliverables (filtered list), top 10 freelancers by quality rating (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Talent Matchmaker Agent
**Agent Purpose:** Instantly match project needs with the best available freelance talent and manage the assignment lifecycle end-to-end.

**Triggers:**
- When a PM creates a new freelance assignment request
- When a deliverable is submitted (route to QA)
- When a freelancer assignment is overdue
- Monthly vendor roster review
- When a new freelancer is added to the roster

**Actions:**
- Search the vendor roster and recommend top 3 freelancers for any assignment based on skills, availability, rate, quality history, and past program experience
- Auto-generate assignment briefs with program context, brand guidelines, deliverable specs, and deadline
- Route submitted deliverables to the appropriate QA reviewer based on content type
- Track freelancer reliability metrics (on-time delivery rate, revision frequency) and flag declining performers
- Auto-initiate onboarding workflow for new freelancers (NDA, style guide, tool access, payment setup)

**Data Required:**
- Vendor Roster (skills, rates, availability, quality history)
- Active assignments and historical assignment data
- Program requirements and brand guidelines
- QA reviewer assignments by content type

**Autonomy Level:** Human-in-the-Loop
Recommends freelancer matches; PM selects and confirms. Autonomously manages briefs, reminders, and QA routing. Payment processing requires finance approval.

**Example Interaction:**
> A PM needs a voiceover artist for 6 modules of pharmaceutical sales training — must understand medical terminology and have a warm, authoritative tone. The Talent Matchmaker searches the roster: "Top 3 matches: 1) Jennifer Walsh — 4.8 quality rating, 23 previous pharma assignments, $350/finished hour, available next week. 2) Michael Torres — 4.6 rating, 12 pharma assignments, $300/finished hour, available in 2 weeks. 3) Sarah Kim — 4.9 rating, 8 pharma assignments, $400/finished hour, available next week but has a scheduling note about limited March availability." The PM selects Jennifer. The agent sends her a complete brief with script samples, pronunciation guide for drug names, tone reference from the client's brand guidelines, and the delivery schedule.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ADDIE | Analysis, Design, Development, Implementation, Evaluation — the foundational instructional design methodology |
| SAM | Successive Approximation Model — an agile alternative to ADDIE with iterative design-develop-review cycles |
| ILT | Instructor-Led Training — traditional classroom delivery |
| VILT | Virtual Instructor-Led Training — live online sessions via Zoom, Teams, WebEx |
| Kirkpatrick Model | 4-level training evaluation framework: Reaction, Learning, Behavior, Results |
| Level 1-4 | Kirkpatrick evaluation levels (see above) |
| ROI (Phillips) | Jack Phillips' Level 5 — calculates financial return on training investment |
| CEU | Continuing Education Unit — standardized measure of participation in accredited programs |
| LMS | Learning Management System — platform for delivering and tracking e-learning (e.g., Cornerstone, Docebo, Absorb) |
| SCORM | Sharable Content Object Reference Model — technical standard for e-learning interoperability |
| xAPI (Tin Can) | Experience API — modern learning data standard replacing SCORM |
| Storyboard | Detailed blueprint of an e-learning module showing screen-by-screen content, interactions, and narration |
| Authoring Tool | Software for creating e-learning content (Articulate Storyline, Rise, Adobe Captivate, Lectora) |
| Blended Learning | Combining multiple modalities (e.g., ILT + e-learning + job aids) in a single program |
| Microlearning | Short, focused learning units (2-5 minutes) designed for just-in-time consumption |
| SME | Subject Matter Expert — provides content expertise during curriculum development |
| Needs Analysis | Systematic process to identify training gaps, audience, and business objectives before design begins |
| Action Mapping | Cathy Moore's methodology focusing on business goals and practice activities over information delivery |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP of Delivery / COO | Oversees all program delivery operations, PMO, and resource allocation | Decision-maker |
| PMO Director | Manages project managers, portfolio oversight, process standardization | Decision-maker |
| Program/Project Manager | Owns individual client engagements end-to-end | Influencer/User |
| Resource Manager | Coordinates facilitator and freelancer scheduling across programs | User |
| ID Team Lead | Manages instructional design staff and content quality standards | Influencer |
| Head of Client Success | Owns client relationships, renewals, and satisfaction | Influencer |
| Finance Controller | Manages program budgets, freelancer payments, and revenue recognition | Influencer |
| Operations Coordinator | Handles logistics, scheduling, materials, and vendor management | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales | Sales needs visibility into delivery capacity for accurate proposal timelines | CRM for pipeline management connected to PMO capacity |
| HR | Internal L&D for staff development mirrors client-facing delivery processes | Same board structures for internal training management |
| Creative & Design | Produces visual assets, branding, and media for training content | Creative project management boards |
| IT | Manages LMS infrastructure, authoring tool licenses, and integrations | IT project tracking and service desk |
| Finance | Budget tracking, invoicing, freelancer payments, revenue recognition | Financial reporting dashboards |
| Marketing | Case studies from successful programs, thought leadership content | Marketing campaign management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Smartsheet | Popular for training project tracking, Gantt charts | monday.com offers better UX, automations, and dashboards; Smartsheet feels like "spreadsheets with lipstick" |
| Microsoft Project | Enterprise PMO standard, complex scheduling | Overkill for most training companies; monday.com is more accessible and collaborative |
| Asana | Lightweight task management, popular with creative teams | Lacks the portfolio-level dashboards and CRM capabilities training PMOs need |
| Wrike | Mid-market project management with proofing | monday.com's flexibility and app marketplace offer more customization for training workflows |
| Monday.com + Teamwork | Some training companies use Teamwork for client project management | Show monday.com can handle both internal PMO and client-facing project visibility |
| Spreadsheets (Excel/Sheets) | Still the #1 "tool" for many training PMOs | Easy migration story; show the automation and dashboard value immediately |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Smartsheet and it works fine" | "Smartsheet handles scheduling well, but training PMOs need more — client feedback tracking, freelancer management, resource optimization, and cross-program dashboards in one place. Let me show you what a unified training operations hub looks like." |
| "Our processes are too custom for an off-the-shelf tool" | "That's actually where monday.com shines — it's not off-the-shelf, it's a platform you configure to match YOUR processes. Every training company runs differently. Let me build your exact workflow right now." |
| "Our project managers will resist changing tools" | "We see this a lot in training companies. The key is starting with ONE pain point — usually the portfolio dashboard. When PMs see that status meetings get 60% shorter, adoption follows naturally." |
| "We need something that integrates with our LMS" | "monday.com integrates with all major LMS platforms through our integration marketplace and API. We can pull completion data, assessment scores, and enrollment numbers directly into your project boards." |
| "We can't justify the cost for our team size" | "Consider the cost of one missed deadline, one double-booked facilitator, or one lost client renewal because you couldn't demonstrate program impact. Training PMOs typically see ROI within 3 months through time savings alone." |

## Proof Points
*(To be populated with customer references)*
- Training companies managing 50+ concurrent programs on monday.com
- Facilitator scheduling optimization case studies
- Content development pipeline efficiency improvements
- Client QBR preparation time reduction examples

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
