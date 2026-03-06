# Non-Profit & Charitable Organizations × Operations Playbook

## Overview

Operations in non-profit and charitable organizations is the backbone that enables mission delivery — managing programs, coordinating volunteers, tracking grants, ensuring compliance, and orchestrating the logistics of impact at scale. Unlike for-profit operations, non-profit ops teams must balance efficiency with mission fidelity, often under intense resource constraints and donor scrutiny. Every dollar saved on overhead is a dollar redirected toward the cause.

Non-profit operations teams typically span program management, volunteer coordination, facilities, fleet/logistics (for service-delivery orgs), and compliance/reporting. They report into a COO or VP of Operations, and in smaller organizations the Executive Director may wear this hat. The regulatory environment is complex — IRS 990 reporting, state charitable solicitation registrations, grant compliance (OMB Uniform Guidance for federal grants), and increasingly ESG/impact measurement frameworks like the Global Impact Investing Network (GIIN) IRIS+ metrics.

Scale varies enormously: from a 10-person community organization to global NGOs like World Vision or Habitat for Humanity with thousands of staff, tens of thousands of volunteers, and operations spanning dozens of countries. Regardless of size, the constant challenge is doing more with less — and proving impact to funders. Operations leaders are under pressure to professionalize processes, reduce administrative burden, and demonstrate that overhead ratios (watched closely by Charity Navigator and GuideStar/Candid) are well-managed.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Non-profits are judged by overhead ratios (program vs. admin spend). Doing more without hiring more ops staff directly increases mission delivery capacity. |
| 2 | Replace or Radically Augment Headcount | High | Chronic understaffing in ops roles — volunteer coordinators, grant compliance officers, logistics managers — means each person is stretched thin. AI augmentation is transformative. |
| 3 | Consolidate Tech Stack with AI | Medium-High | Non-profits accumulate fragmented tools (Salesforce NPSP, Bloomerang, VolunteerHub, spreadsheets) with limited IT budget. Consolidation reduces licensing costs and training burden. |

## Prioritized Use Cases

---

### Use Case 1: Grant Lifecycle Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Grant management is the lifeblood of non-profit funding, yet most organizations manage it through a patchwork of spreadsheets, shared drives, and email threads. A mid-size non-profit might manage 30-80 active grants simultaneously, each with unique reporting requirements, deliverable deadlines, spending restrictions, and compliance mandates. Missing a grant report deadline can trigger clawback provisions — literally losing funding already spent. The average grants manager spends 60% of their time on administrative tracking rather than relationship-building or program design. Federal grants under 2 CFR 200 (Uniform Guidance) require meticulous time-and-effort reporting, cost allocation plans, and sub-recipient monitoring that can overwhelm small teams.

#### The Solution
monday.com Work Management provides a comprehensive grant lifecycle board system. A master **Grant Pipeline Board** tracks every grant from prospect → LOI submitted → proposal in progress → submitted → awarded → active → closeout → archived. Connected boards link to **Grant Deliverables** (with status columns for draft/review/submitted/accepted), **Budget Tracking** (number columns for awarded amount, spent-to-date, remaining, with formulas for burn rate), and **Compliance Calendar** (date columns with automated reminders at 30/14/7 days before deadlines). The **Dashboard view** aggregates total funding pipeline, revenue by funder type (federal/state/foundation/corporate), and upcoming deadlines across all grants. Automations notify program directors when deliverables are due, escalate overdue items to the grants director, and trigger closeout checklists when grant end dates approach.

#### The Outcome
- 95% on-time grant report submission (up from ~70%)
- 40% reduction in grants administration time per grant
- Zero missed deadlines leading to clawback risk
- Real-time visibility into $X million funding pipeline
- Improved funder relationships through proactive communication

#### Discovery Questions
1. "How many active grants are you managing simultaneously, and what percentage are federal vs. foundation vs. corporate?"
2. "Have you ever missed a grant reporting deadline or had a compliance finding in an audit? What was the impact?"
3. "How do you currently track restricted vs. unrestricted spending across grants? Is your finance team confident in the cost allocation?"
4. "When a program officer at a foundation asks for a status update, how quickly can you pull that information together?"
5. "What happens when your grants manager goes on leave — does anyone else know where things stand?"

#### Industry Context
Non-profit grants come in many forms: government grants (federal, state, local) with the most stringent compliance; foundation grants (program officers expect relationship, reporting varies); corporate grants (often tied to employee engagement or CSR goals). Key terminology: LOI (Letter of Intent/Inquiry), RFP (Request for Proposal), MOUs (Memoranda of Understanding), sub-awards, indirect cost rate (negotiated with federal cognizant agency), match requirements (cash vs. in-kind), and CFDA numbers (Catalog of Federal Domestic Assistance). The shift toward trust-based philanthropy is changing reporting expectations — some funders are simplifying requirements, but federal compliance remains rigorous.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Grant Lifecycle Management system with four connected boards:
>
> **Board 1 — Grant Pipeline:** Columns: Grant Name (text), Funder Name (text), Funder Type (dropdown: Federal, State, Foundation, Corporate, Individual), Grant Amount Requested (numbers, currency USD), Grant Amount Awarded (numbers, currency USD), Status (status: Prospecting, LOI Submitted, Proposal In Progress, Submitted, Under Review, Awarded, Active, Closeout, Archived, Declined), Program Area (dropdown: Education, Health, Housing, Advocacy, Youth, Environment), Grant Start Date (date), Grant End Date (date), Program Director (people), Grants Manager (people), CFDA Number (text), Indirect Cost Rate (numbers, percentage), Match Required (checkbox), Match Amount (numbers, currency USD). Groups: Active Grants, Pipeline, Closed. Views: Table (default), Dashboard showing total pipeline value by status, funding by funder type pie chart, upcoming end dates timeline.
>
> **Board 2 — Grant Deliverables:** Columns: Deliverable Name (text), Connected Grant (connect to Grant Pipeline), Due Date (date), Status (status: Not Started, Drafting, In Review, Submitted, Accepted, Revision Needed), Responsible Person (people), Deliverable Type (dropdown: Narrative Report, Financial Report, Site Visit, Data Submission, Final Report), Notes (long text). Automations: When Due Date is 30 days away, notify Responsible Person. When Due Date is 7 days away and Status is not Submitted, notify Grants Manager and escalate. When Status changes to Submitted, notify Program Director.
>
> **Board 3 — Grant Budget Tracker:** Columns: Budget Line Item (text), Connected Grant (connect to Grant Pipeline), Budget Category (dropdown: Personnel, Fringe, Travel, Equipment, Supplies, Contractual, Other, Indirect), Budgeted Amount (numbers, currency USD), Spent to Date (numbers, currency USD), Remaining (formula: Budgeted minus Spent), Burn Rate % (formula: Spent divided by Budgeted times 100), Period (dropdown: Q1, Q2, Q3, Q4, Annual). Dashboard: total spend vs budget by grant, burn rate alerts for grants over 90% spent.
>
> **Board 4 — Compliance Calendar:** Columns: Task Name (text), Connected Grant (connect to Grant Pipeline), Due Date (date), Compliance Type (dropdown: Financial Report, Narrative Report, Audit, Site Visit, Drawdown Request, Time & Effort Certification, Subrecipient Monitoring), Status (status: Upcoming, In Progress, Complete, Overdue), Owner (people). Automations: When Due Date passes and Status is not Complete, change Status to Overdue and notify COO."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Grant Guardian
**Agent Purpose:** Proactively monitor grant compliance deadlines, spending patterns, and reporting requirements to prevent missed obligations and optimize grant performance.

**Triggers:**
- Daily scan of all active grants for upcoming deadlines (30/14/7/1 day windows)
- When grant spending exceeds 85% of budgeted amount for any line item
- When a deliverable status changes to "Revision Needed"
- Weekly Monday morning summary generation
- When a new grant is marked as "Awarded"

**Actions:**
- Generate deadline digest notifications grouped by urgency (overdue → due this week → due this month)
- Create draft compliance checklists for newly awarded grants based on funder type and grant terms
- Analyze spending patterns and flag potential budget overruns or underspending (which can also trigger compliance issues)
- Auto-generate grant closeout task lists 90 days before grant end date
- Compile cross-grant dashboards for board meetings, pulling data from all connected boards
- Escalate critical items (overdue reports, audit findings) to COO with context summary

**Data Required:**
- Grant Pipeline board (all grant details)
- Grant Deliverables board (reporting deadlines)
- Budget Tracker board (spending data)
- Compliance Calendar (regulatory deadlines)
- Integration with accounting system for real-time spend data (QuickBooks, Sage Intacct)

**Autonomy Level:** Human-in-the-Loop
Grant Guardian monitors and alerts autonomously but requires human approval for any external communications, report submissions, or budget modifications. It drafts but never sends.

**Example Interaction:**
> It's Monday morning and the Grants Director opens monday.com to find a Grant Guardian digest: "🚨 3 items need attention this week: (1) The HHS Community Health grant Q3 narrative report is due Friday — draft is at 60% in Google Docs, and Program Director Maria hasn't reviewed yet. I've sent her a reminder. (2) The Ford Foundation Youth Leadership grant has spent 92% of its Travel budget line with 4 months remaining — recommend requesting a budget modification or shifting to virtual programming. (3) New: The state DOE just posted an RFP for afterschool STEM programs (CFDA 84.287) with a March 15 deadline — this aligns with your Education program area. Want me to create a pipeline entry and draft a timeline?" The Grants Director responds "Yes, create the pipeline entry" and Grant Guardian instantly builds the item with all known details pre-populated and a proposal development timeline working backward from March 15.

---

### Use Case 2: Volunteer Management & Engagement

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Volunteers are the workforce multiplier for non-profits — many organizations rely on volunteers for 30-60% of their labor capacity. Yet managing them is chaotic: sign-ups come through email, a website form, walk-ins, and partner referrals. Scheduling is done in spreadsheets that break when shifts change. Background checks and onboarding paperwork get lost. No-show rates of 20-30% are common because there's no systematic reminder or engagement process. Volunteer coordinators (often a single person managing hundreds of volunteers) spend their days firefighting instead of building a sustainable volunteer program. And critically, most non-profits can't quantify volunteer hours for grant reporting or the value of volunteer labor (currently $31.80/hour per Independent Sector), leaving money and impact data on the table.

#### The Solution
monday.com Work Management creates an end-to-end volunteer management system. A **Volunteer Roster Board** captures all volunteer information: contact details, skills, availability, certifications, background check status, and engagement history. A connected **Volunteer Opportunities Board** lists upcoming shifts/events with required roles, skill requirements, and capacity limits. **monday.com Forms** enable self-service volunteer sign-up that feeds directly into the system. Automations handle the lifecycle: form submission → welcome email → onboarding checklist creation → background check tracking → assignment matching → shift reminders (3 days and 1 day before) → post-event feedback survey → thank you message. The **Dashboard** tracks total volunteer hours, volunteer retention rate, hours by program area, and the calculated dollar value of volunteer contributions for grant reporting.

#### The Outcome
- 50% reduction in volunteer coordinator administrative time
- 25% improvement in volunteer show-up rates through automated reminders
- Accurate volunteer hour tracking for grant reporting (potentially unlocking $100K+ in reportable match value)
- Improved volunteer retention through systematic engagement
- Self-service sign-up reducing intake processing from days to minutes

#### Discovery Questions
1. "How many active volunteers do you have, and what's your annual volunteer hour total? Do you track that number accurately?"
2. "What's your volunteer no-show rate, and how does that impact program delivery?"
3. "Do you currently count volunteer hours as in-kind match for any grants? How confident are you in those numbers?"
4. "What does your volunteer onboarding process look like — how long from sign-up to first shift?"
5. "How do you re-engage volunteers who haven't been active in 90+ days?"

#### Industry Context
Volunteer management in non-profits involves legal considerations (liability waivers, Volunteer Protection Act), HR-adjacent processes (background checks via Sterling or Checkr, especially for youth-serving orgs), and compliance requirements (volunteers working with vulnerable populations need specific clearances). Many organizations distinguish between episodic volunteers (one-time events), regular volunteers (weekly/monthly commitments), skilled/pro bono volunteers (professionals donating expertise), and board members (governance volunteers). The value of volunteer time is set annually by Independent Sector and is used for grant match calculations and Form 990 reporting.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Volunteer Management System with three connected boards:
>
> **Board 1 — Volunteer Roster:** Columns: Volunteer Name (text), Email (email), Phone (phone), Status (status: Prospect, Onboarding, Active, Inactive, Alumni), Skills (tags: Event Setup, Tutoring, Mentoring, Data Entry, Fundraising, Cooking, Driving, Translation, Medical, Legal, Marketing, Construction), Availability (dropdown: Weekday Mornings, Weekday Afternoons, Weekday Evenings, Weekend Mornings, Weekend Afternoons, Flexible), Background Check (status: Not Started, Submitted, Cleared, Expired), Background Check Expiry (date), Date Joined (date), Total Hours (numbers), Emergency Contact (text), T-Shirt Size (dropdown: XS, S, M, L, XL, XXL), Preferred Location (dropdown: Main Office, North Center, South Center, Mobile, Remote), Notes (long text). Groups: Active Volunteers, Onboarding, Inactive. Automations: When Background Check Expiry is 30 days away, notify volunteer coordinator. When Status changes to Active, send welcome email.
>
> **Board 2 — Volunteer Opportunities:** Columns: Opportunity Name (text), Date (date), Time Slot (dropdown: Morning 8-12, Afternoon 12-5, Evening 5-9, Full Day), Location (dropdown: Main Office, North Center, South Center, Mobile, Remote), Program Area (dropdown: Food Bank, Youth Mentoring, Housing, Education, Fundraising Event, Administrative), Volunteers Needed (numbers), Volunteers Confirmed (numbers), Skills Required (tags, same as roster), Description (long text), Coordinator (people), Status (status: Planning, Open for Sign-up, Full, In Progress, Completed, Cancelled). Automations: When Volunteers Confirmed equals Volunteers Needed, change Status to Full. When Date is 3 days away, notify all connected volunteers via email. When Status changes to Completed, create feedback survey items.
>
> **Board 3 — Volunteer Hours Log:** Columns: Volunteer (connect to Volunteer Roster), Opportunity (connect to Volunteer Opportunities), Date (date), Hours (numbers), Verified (checkbox), Program Area (mirror from Opportunity), Dollar Value (formula: Hours times 31.80), Notes (text). Dashboard: Total hours this month/quarter/year, dollar value of volunteer time, hours by program area, top volunteers leaderboard, retention rate (active vs. total)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Volunteer Matchmaker
**Agent Purpose:** Intelligently match volunteers to opportunities based on skills, availability, location preferences, and engagement history to maximize participation and satisfaction.

**Triggers:**
- When a new Volunteer Opportunity is created with Status "Open for Sign-up"
- When a new volunteer completes onboarding (Status → Active)
- Weekly scan for volunteers inactive for 60+ days
- When an opportunity is understaffed 48 hours before the event date
- When a volunteer cancels a confirmed shift

**Actions:**
- Analyze volunteer roster to find best-fit matches for open opportunities based on skills, availability, location, and past engagement patterns
- Send personalized invitation messages to matched volunteers with opportunity details
- Generate re-engagement outreach for inactive volunteers with personalized messaging ("We noticed you enjoyed tutoring events — we have one coming up!")
- When a volunteer cancels, immediately identify and invite replacement candidates
- Compile monthly volunteer impact reports with hours, dollar value, and program distribution
- Flag volunteers approaching milestone hours (50, 100, 250, 500) for recognition

**Data Required:**
- Volunteer Roster board (skills, availability, history)
- Volunteer Opportunities board (requirements, dates)
- Hours Log board (engagement patterns)
- Past feedback/satisfaction data

**Autonomy Level:** Escalation-Based
Volunteer Matchmaker sends invitations and reminders autonomously but escalates to the volunteer coordinator when: opportunities remain understaffed 24 hours before event, a volunteer has three consecutive no-shows, or when a skills gap means no suitable matches exist.

**Example Interaction:**
> The Volunteer Matchmaker detects that Saturday's Habitat for Humanity build day has only 8 of 20 needed volunteers. It cross-references the roster: "Found 15 active volunteers with Construction skills and Weekend Morning availability who haven't been engaged in the last 30 days. I've drafted personalized invitations for each — for example, James received: 'Hi James! We have a build day this Saturday at the Elm Street site, 8 AM-12 PM. Last time you helped with framing and the crew lead said your work was excellent. We'd love to have you back — spots are filling up!' Shall I send all 15 invitations?" The coordinator approves, and within 24 hours, 9 volunteers confirm — filling the roster.

---

### Use Case 3: Program Outcome Tracking & Impact Measurement

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every funder asks the same question: "What impact did our money create?" Yet most non-profits struggle to answer with data. Program outcomes are tracked in disconnected systems — case managers use one tool, education programs use another, and the development team manually compiles impact reports by emailing program directors and hoping they respond. The result: impact reports that take weeks to produce, are often based on estimates rather than data, and miss the storytelling opportunity that drives future funding. Meanwhile, the sector is shifting toward evidence-based practices and outcomes-focused funding (pay-for-success models, social impact bonds), making robust measurement not just nice-to-have but existential. The lack of a unified impact measurement system means non-profits can't demonstrate their theory of change with data — and that costs them funding.

#### The Solution
monday.com Work Management creates a unified **Program Outcomes Tracking** system. Each program gets a board with custom columns mapping to its logic model: inputs (resources deployed), activities (services delivered), outputs (units of service), and outcomes (measurable changes). A **Participant Tracking Board** follows individuals through program milestones using status columns that map to the program's theory of change. **monday.com Forms** enable frontline staff (case managers, teachers, counselors) to log service delivery data in real-time from mobile devices. Connected **Dashboard views** aggregate data across programs to show organization-wide impact: total participants served, services delivered, outcomes achieved, and cost-per-outcome metrics. Automations trigger data collection reminders, flag participants who are falling behind milestones, and compile quarterly impact summaries.

#### The Outcome
- Impact report generation reduced from 3 weeks to 2 days
- 90%+ data completeness from frontline staff (up from ~50%)
- Real-time visibility into program performance for leadership and board
- Cost-per-outcome metrics that strengthen grant proposals
- Data-driven program decisions: expand what works, adjust what doesn't

#### Discovery Questions
1. "Do you have a documented theory of change or logic model for your major programs? How do you track progress against it?"
2. "When your board asks 'how many people did we help and how did their lives improve?' — how long does it take to answer that?"
3. "Are any of your funders moving toward outcomes-based funding or pay-for-success models?"
4. "How do frontline staff currently capture service delivery data? Is it real-time or batch entry?"
5. "Can you currently calculate your cost-per-outcome for any program? Would that metric help in grant proposals?"

#### Industry Context
Impact measurement in non-profits follows frameworks like logic models (inputs → activities → outputs → outcomes → impact), IRIS+ metrics (standardized by GIIN), Social Return on Investment (SROI), and increasingly Results-Based Accountability (RBA). Key terms: outputs vs. outcomes (counting meals served vs. measuring reduced food insecurity), collective impact (multiple organizations working toward shared metrics), and evidence-based programs (programs with RCT or quasi-experimental evidence of effectiveness). Funders increasingly want "outcome harvesting" and contribution analysis, not just activity counts. GuideStar/Candid Platinum Seal requires published impact data.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Program Outcome Tracking system with three connected boards:
>
> **Board 1 — Program Portfolio:** Columns: Program Name (text), Program Area (dropdown: Education, Health, Housing, Workforce, Youth Development, Food Security, Legal Aid), Target Population (dropdown: Children, Youth, Adults, Seniors, Families, Veterans, Immigrants), Annual Budget (numbers, currency USD), Funding Sources (tags: Federal, State, Foundation, Corporate, Individual), Program Manager (people), Status (status: Planning, Active, Winding Down, Completed, Suspended), Annual Target Participants (numbers), Actual Participants YTD (numbers), Achievement Rate (formula: Actual divided by Target times 100), Cost Per Participant (formula: Budget divided by Actual), Primary Outcome Metric (text), Outcome Target (numbers), Outcome Actual (numbers). Groups: Active Programs, Pipeline, Completed. Dashboard: portfolio overview with participants served by program, budget allocation, achievement rates.
>
> **Board 2 — Participant Tracker:** Columns: Participant ID (text, auto-generate), Program (connect to Program Portfolio), Enrollment Date (date), Status (status: Referred, Enrolled, Active, Milestone 1, Milestone 2, Milestone 3, Completed, Dropped Out, Graduated), Case Manager (people), Services Received (tags: Counseling, Training, Housing Placement, Job Placement, Tutoring, Mentoring, Legal Aid, Food Assistance), Contact Attempts (numbers), Last Contact (date), Outcome Achieved (checkbox), Outcome Details (long text), Exit Date (date), Follow-up Status (status: Pending 3-Month, Pending 6-Month, Pending 12-Month, Completed, Lost to Follow-up). Automations: When Last Contact is more than 14 days ago and Status is Active, notify Case Manager. When Status changes to Completed, create follow-up items at 3, 6, and 12 months.
>
> **Board 3 — Service Delivery Log:** Columns: Participant (connect to Participant Tracker), Service Date (date), Service Type (dropdown: Individual Session, Group Session, Workshop, Home Visit, Phone Call, Referral, Assessment), Duration Minutes (numbers), Staff Member (people), Notes (long text), Program (mirror from Participant). Dashboard: services delivered this month, hours by service type, caseload per staff member, engagement trends."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Impact Analyst
**Agent Purpose:** Continuously analyze program data to surface insights, generate impact narratives, and alert leadership to programs that are exceeding or falling short of targets.

**Triggers:**
- Monthly program performance review (1st of each month)
- When any program's achievement rate drops below 70% of target
- When a funder requests an impact report
- Quarterly board meeting preparation (auto-scheduled)
- When a program reaches 90% or more of its outcome target

**Actions:**
- Generate monthly program performance scorecards comparing actuals to targets with trend analysis
- Draft funder-ready impact narratives combining quantitative data with qualitative stories from case notes
- Alert program managers when participant engagement drops or dropout patterns emerge
- Calculate and update cost-per-outcome metrics across programs
- Identify high-performing program elements for replication and underperforming areas needing intervention
- Compile board-ready impact dashboards with executive summaries

**Data Required:**
- Program Portfolio board (targets, budgets)
- Participant Tracker board (enrollment, milestones, outcomes)
- Service Delivery Log (activity data)
- Financial data for cost analysis

**Autonomy Level:** Human-in-the-Loop
Impact Analyst generates reports and alerts autonomously but requires human review before any data is shared externally (with funders, board, public). Program narratives are drafted for human editing.

**Example Interaction:**
> The Impact Analyst flags: "📊 Youth Workforce Program alert: 6-month outcomes data shows 78% job placement rate vs. 85% target. However, I found a pattern — participants who completed the mock interview module (Milestone 2) have a 94% placement rate, while those who skipped it have only 61%. Recommendation: Make mock interviews mandatory rather than optional. Also, I've drafted the Q3 narrative for the JPMorgan Chase funder report — it highlights the 23 participants placed in jobs averaging $18.50/hour, with a combined annual earnings impact of $890K. The draft includes two participant success stories pulled from case manager notes. Ready for your review."

---

### Use Case 4: Event & Fundraiser Operations

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Fundraising events — galas, walks/runs, auctions, golf tournaments — are critical revenue generators (often 20-40% of annual revenue) but operationally nightmarish. A single gala requires coordinating 50+ vendors, 100+ volunteers, 200+ auction items, 500+ attendees, sponsorship fulfillment, table assignments, AV setup, catering, and post-event follow-up. Most non-profits manage this in a combination of spreadsheets, email chains, and the event coordinator's memory. When that coordinator leaves, institutional knowledge walks out the door. Post-event, thank you letters take weeks, sponsorship fulfillment reports are late, and the team is too exhausted to capture lessons learned. The result: events that could net $500K end up netting $350K because of operational inefficiency, missed sponsorship deliverables, and poor donor follow-up.

#### The Solution
monday.com Work Management provides a templated **Event Operations System** that can be cloned for each event. A master **Event Planning Board** breaks the event into workstreams (venue, catering, entertainment, auction, sponsorship, marketing, volunteers, logistics) with timeline views showing the critical path. Connected boards manage **Sponsorship Tracking** (levels, commitments, deliverables, fulfillment status), **Auction Item Management** (donor, item description, value, minimum bid, winner, payment status), and **Attendee Management** (registration, table assignments, dietary restrictions, VIP status). Automations drive the timeline: trigger vendor follow-ups, send attendee confirmations, remind team of deadlines, and kick off post-event workflows (thank you emails within 48 hours, sponsorship fulfillment reports within 2 weeks, lessons learned session within 1 week).

#### The Outcome
- 30% reduction in event planning time through templated workflows
- 98% on-time sponsorship fulfillment (protecting future sponsorship revenue)
- Thank you communications sent within 48 hours vs. 3+ weeks
- Complete institutional knowledge capture — new staff can run recurring events from templates
- 15-20% improvement in event net revenue through better vendor management and reduced operational waste

#### Discovery Questions
1. "How many fundraising events do you run annually, and what percentage of your total revenue do they represent?"
2. "If your lead event coordinator left tomorrow, could someone else step in and run your signature gala?"
3. "How do you track sponsorship deliverables — do sponsors ever complain about missed commitments?"
4. "How quickly do thank you letters and tax receipts go out after an event?"
5. "Do you do a formal post-event debrief? How do you capture and apply lessons learned?"

#### Industry Context
Non-profit fundraising events have specific terminology: fund-a-need/paddle raise (live ask at galas), silent vs. live auction, sponsorship levels (presenting, platinum, gold, silver, bronze with specific deliverables), in-kind sponsorship, underwriting, table captains (donors who fill tables with prospects), and event committees (volunteer leadership). Tax receipt requirements are specific: donors must receive acknowledgment letters stating the fair market value of benefits received (dinner, entertainment) deducted from their contribution. The IRS requires written acknowledgment for donations over $250, and quid pro quo disclosure for events where donors receive benefits exceeding $75.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Event & Fundraiser Operations system with four connected boards:
>
> **Board 1 — Event Master Plan:** Columns: Task Name (text), Workstream (dropdown: Venue & Logistics, Catering, Entertainment, Auction, Sponsorship, Marketing, Volunteers, Registration, AV & Tech, Décor), Owner (people), Status (status: Not Started, In Progress, Blocked, Complete), Priority (status: Critical Path, High, Medium, Low), Due Date (date), Dependencies (dependency), Budget Line (numbers, currency USD), Actual Cost (numbers, currency USD), Variance (formula: Budget minus Actual), Notes (long text). Groups by workstream. Views: Timeline/Gantt view showing critical path, Table view for task management, Dashboard showing budget vs actual by workstream.
>
> **Board 2 — Sponsorship Tracker:** Columns: Sponsor Name (text), Contact Person (text), Email (email), Phone (phone), Sponsorship Level (dropdown: Presenting $50K, Platinum $25K, Gold $10K, Silver $5K, Bronze $2.5K, In-Kind), Amount Committed (numbers, currency USD), Amount Received (numbers, currency USD), Payment Status (status: Pledged, Invoiced, Partial, Paid), Deliverables (tags: Logo on Invite, Table Signage, Program Ad, Social Media Mention, Speaking Slot, VIP Reception, Banner Display), Deliverable Status (status: Pending, In Progress, Fulfilled), Year-over-Year (checkbox for returning sponsor), Relationship Owner (people), Notes (long text). Automations: When Amount Received equals Amount Committed, change Payment Status to Paid. When event date passes and Deliverable Status is not Fulfilled, escalate to event director.
>
> **Board 3 — Auction Items:** Columns: Item Name (text), Donor Name (text), Donor Contact (text), Category (dropdown: Experience, Travel, Sports, Art, Dining, Services, Luxury Goods, Packages), Fair Market Value (numbers, currency USD), Minimum Bid (numbers, currency USD), Auction Type (dropdown: Silent, Live), Item Number (numbers), Description (long text), Photo (files), Pickup Status (status: Pledged, Received, Displayed, Won, Picked Up), Winner Name (text), Winning Bid (numbers, currency USD), Payment Received (checkbox), Thank You Sent to Donor (checkbox). Dashboard: total FMV, items by category, received vs pledged.
>
> **Board 4 — Attendee Registry:** Columns: Attendee Name (text), Email (email), Ticket Type (dropdown: Individual $250, Couple $400, Table of 10 $2000, VIP $500, Comp), Table Number (numbers), Dietary Restrictions (dropdown: None, Vegetarian, Vegan, Gluten-Free, Kosher, Halal, Nut Allergy, Other), Payment Status (status: Registered, Paid, Comp, Cancelled), VIP (checkbox), Table Captain (connect to self), Thank You Sent (checkbox), Tax Receipt Sent (checkbox). Automations: When Payment Status changes to Paid, send confirmation email. Day after event, create thank you task for each attendee."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Event Command Center
**Agent Purpose:** Serve as the central coordinator for event operations, tracking every workstream, flagging risks, and ensuring no detail falls through the cracks.

**Triggers:**
- Daily check of all tasks with due dates in the next 7 days
- When any task Status changes to "Blocked"
- When sponsorship payment is overdue by more than 14 days
- 72 hours before event: final readiness check
- Day after event: trigger post-event workflow

**Actions:**
- Generate daily event countdown briefings ("12 days out: 4 tasks overdue, auction items 85% received, sponsorship 92% collected")
- When a task is blocked, identify the blocker and notify both the task owner and the dependency owner
- Draft follow-up emails for outstanding sponsorship payments
- Create post-event workflow: thank you emails, tax receipts, sponsorship fulfillment reports, lessons learned survey
- Compile event P&L comparing budgeted vs. actual across all workstreams
- Archive completed event as a template for next year with notes on what to change

**Data Required:**
- All four event boards (Master Plan, Sponsorship, Auction, Attendees)
- Email integration for automated communications
- Financial data for P&L reporting

**Autonomy Level:** Escalation-Based
Sends internal reminders and generates reports autonomously. Escalates to event director for: blocked critical-path items, sponsorship issues, budget overruns exceeding 10%, and any external communications.

**Example Interaction:**
> Three days before the annual gala, Event Command Center runs its readiness check: "🎯 Gala Readiness: 87% — here's what needs attention: (1) CRITICAL: AV company hasn't confirmed podium mic setup — I've emailed them twice, no response. Recommend calling Tony directly at 555-0142. (2) Auction: 47 of 52 items received. Missing: Lake house weekend (pledged by Board Member Sarah — I've drafted a reminder), wine tasting (vendor confirms delivery tomorrow), and three restaurant gift cards (not yet confirmed). (3) Seating: 8 attendees with no table assignment — 6 registered in the last 48 hours. I've created a suggested seating chart based on donor level and past table preferences. (4) Good news: Sponsorship revenue is at 104% of target — Gold sponsor Acme Corp upgraded to Platinum last week. All deliverables updated."

---

### Use Case 5: Board Governance & Meeting Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Non-profit boards are legally responsible for organizational governance, yet board management is typically a mess of email attachments, last-minute agenda changes, and action items that disappear into meeting minutes no one reads. Board packets — often 50-100 pages of financial statements, program reports, and strategic documents — are assembled manually and distributed late. Board committees (finance, governance, fundraising, program) operate in silos. Term tracking, conflict of interest disclosures, and board giving records are maintained in disparate spreadsheets. The board chair and ED spend hours preparing for meetings that could be streamlined. Worst case: governance failures (missed fiduciary duties, expired terms, undisclosed conflicts) create legal liability.

#### The Solution
monday.com Work Management creates a **Board Governance Hub**. A **Board Members Board** tracks all directors: term dates, committee assignments, attendance records, annual giving, conflict of interest disclosure status, and contact information. A **Board Meetings Board** manages the meeting lifecycle: agenda creation, document assembly (linked files), action item tracking with owners and deadlines, and minutes approval workflow. **Committee Boards** mirror this structure at the committee level. Automations remind board members of upcoming meetings, track document review completion, follow up on action items, and alert the governance committee when terms are expiring or disclosures are overdue.

#### The Outcome
- Board packet preparation reduced from 8 hours to 2 hours
- 100% compliance on conflict of interest disclosures and term tracking
- 85%+ action item completion rate (up from ~40%)
- Clear audit trail for governance decisions
- Improved board engagement through better preparation and follow-through

#### Discovery Questions
1. "How do you currently distribute board packets? How far in advance, and how often are they late?"
2. "What percentage of board action items actually get completed between meetings?"
3. "Are all your board members current on conflict of interest disclosures? How do you track terms and term limits?"
4. "How do committee recommendations flow to the full board? Is there a clear process?"
5. "Has your board ever faced a governance issue — expired terms, missing disclosures, unclear decision records?"

#### Industry Context
Non-profit governance is regulated by state nonprofit corporation laws and IRS requirements (Form 990 asks about governance practices). Key concepts: fiduciary duty (duty of care, loyalty, obedience), D&O insurance, parliamentary procedure (Robert's Rules), quorum requirements, conflict of interest policies (IRS best practice), board self-assessment, executive session (board meets without staff), and the distinction between governance (board) and management (staff). BoardSource is the leading resource. Many boards are moving toward consent agendas (routine items approved without discussion) to focus meeting time on strategic issues.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Board Governance Hub with two connected boards:
>
> **Board 1 — Board Members Directory:** Columns: Member Name (text), Title (text), Email (email), Phone (phone), Term Start (date), Term End (date), Term Number (dropdown: 1st Term, 2nd Term, 3rd Term), Committee Assignments (tags: Executive, Finance, Governance, Fundraising, Program, Audit), Officer Role (dropdown: Chair, Vice Chair, Treasurer, Secretary, Member At-Large, None), Annual Give/Get Target (numbers, currency USD), Amount Given YTD (numbers, currency USD), Give Status (status: On Track, Behind, Complete, Exempt), COI Disclosure (status: Current, Due, Overdue, Not Filed), COI Expiry Date (date), Meetings Attended YTD (numbers), Total Meetings YTD (numbers), Attendance Rate (formula: Attended divided by Total times 100), Status (status: Active, On Leave, Term Expiring, Emeritus). Automations: When Term End is 90 days away, notify Governance Committee Chair. When COI Expiry Date is 30 days away, send renewal reminder to member.
>
> **Board 2 — Board Meetings & Actions:** Columns: Meeting/Action Name (text), Type (dropdown: Full Board Meeting, Executive Committee, Finance Committee, Governance Committee, Fundraising Committee, Program Committee, Special Meeting, Action Item), Date (date), Status (status: Scheduling, Agenda Setting, Materials Due, Ready, In Session, Minutes Draft, Minutes Approved, Complete), Owner (people), Agenda Doc (files), Minutes Doc (files), Attendees (people), Quorum Met (checkbox), Key Decisions (long text), Connected Action Items (connect to self for sub-items). Groups: Upcoming Meetings, Action Items In Progress, Completed. Automations: When Date is 14 days away and Status is Scheduling, notify Owner to set agenda. When an Action Item due date passes and Status is not Complete, notify Owner and Board Chair."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Board Secretary AI
**Agent Purpose:** Streamline board meeting preparation, track governance compliance, and ensure action item follow-through between meetings.

**Triggers:**
- 14 days before any board or committee meeting
- When action item deadlines pass without completion
- Quarterly governance compliance scan
- When a board member's term is within 90 days of expiration
- Annual board self-assessment period

**Actions:**
- Generate draft meeting agendas based on standing items, pending action items, and committee reports due
- Compile board packets by pulling latest financial reports, program dashboards, and committee minutes into a single document
- Track and follow up on action items with graduated urgency (reminder → nudge → escalation to chair)
- Generate governance compliance dashboard: term status, COI disclosures, attendance rates, giving status
- Draft meeting minutes templates pre-populated with attendees, agenda items, and motions for real-time editing
- Alert governance committee to upcoming term expirations with renewal/recruitment timeline

**Data Required:**
- Board Members Directory (terms, committees, compliance)
- Board Meetings & Actions board
- Financial dashboards (for board packets)
- Program outcome dashboards (for board packets)

**Autonomy Level:** Human-in-the-Loop
Drafts agendas, minutes, and communications but requires ED or Board Chair approval before distribution. Sends internal reminders autonomously.

**Example Interaction:**
> Two weeks before the quarterly board meeting, Board Secretary AI messages the ED: "📋 Q1 Board Meeting Prep: Draft agenda ready for your review — includes 3 action items carried forward (facilities lease decision still pending from Finance Committee), Treasurer's report, and the strategic plan progress update. I've compiled the board packet: 62 pages including financial statements, program dashboards, and the investment policy revision from the Finance Committee. Board packet ready to distribute — want me to send it to all 15 members? Also noting: Board Member David Chen's 2nd term expires in April. Governance Committee should discuss renewal or begin recruitment at this meeting. I've added it to the agenda under Governance Report."

---

### Use Case 6: Donor Stewardship & Moves Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Development teams at non-profits are perpetually understaffed relative to their donor portfolios. A major gifts officer might manage 100-150 prospects, each requiring personalized cultivation: research, meetings, site visits, proposals, thank you calls, and ongoing engagement. Without a systematic moves management process, donors fall through the cracks — a major donor who gave $50K last year doesn't get a personal call for 8 months, and their renewal drops to $25K or zero. Mid-level donors ($1K-$10K) — often the highest-ROI segment — get almost no personal attention because the team is focused on major gifts. The data exists in the CRM (Salesforce NPSP, Bloomerang, Raiser's Edge) but the workflow management — who does what, when, and in what sequence — is where things break down.

#### The Solution
monday.com Work Management creates a **Moves Management Pipeline** that layers workflow on top of existing CRM data. Each major donor/prospect is tracked through cultivation stages: identification → qualification → cultivation → solicitation → stewardship → renewal. A connected **Stewardship Calendar Board** ensures systematic touchpoints: impact reports, personal calls, site visits, event invitations, and recognition moments. Automations drive the rhythm: new gift received → thank you call task created (due within 24 hours) → impact report scheduled (90 days) → renewal approach task created (60 days before anniversary). The **Dashboard** shows pipeline value, activity metrics per officer, stewardship completion rates, and donor retention trends.

#### The Outcome
- 15-20% improvement in major donor retention rate
- 30% more cultivation touches per donor (without additional staff)
- Systematic mid-level donor engagement for the first time
- Clear visibility into pipeline value and probability
- Reduced dependency on individual fundraisers' memory and personal systems

#### Discovery Questions
1. "What's your major donor retention rate year-over-year? How does it compare to the sector average of ~45%?"
2. "How many donors are in each gift officer's portfolio? Is there a formal moves management process?"
3. "When someone makes their first $1,000+ gift, what happens in the next 90 days? Is it systematic or ad hoc?"
4. "Do you have a mid-level donor program? How do you currently engage donors in the $1K-$10K range?"
5. "If a gift officer leaves, what happens to their donor relationships? How much information walks out the door?"

#### Industry Context
Fundraising terminology: moves management (systematic cultivation process, coined by David Dunlop at Cornell), LYBUNT/SYBUNT (Last/Some Year But Unfortunately Not This year — lapsed donor segments), donor pyramid (annual fund → mid-level → major gifts → planned giving), stewardship (post-gift relationship management), gift vehicles (outright gifts, pledges, DAFs, stock gifts, planned gifts/bequests), and wealth screening (tools like DonorSearch, iWave that estimate donor capacity). The sector benchmark for donor retention is approximately 45% overall and 60% for repeat donors (AFP Fundraising Effectiveness Project data). Every 1% improvement in retention is worth more than a 10% improvement in acquisition.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Donor Stewardship & Moves Management system with two connected boards:
>
> **Board 1 — Donor Pipeline:** Columns: Donor Name (text), Organization (text), Email (email), Phone (phone), Gift Officer (people), Stage (status: Identification, Qualification, Cultivation, Solicitation, Committed, Stewardship, Renewal), Capacity Rating (dropdown: $1M+, $500K-$1M, $100K-$500K, $50K-$100K, $25K-$50K, $10K-$25K, $5K-$10K, $1K-$5K), Last Gift Amount (numbers, currency USD), Last Gift Date (date), Lifetime Giving (numbers, currency USD), Ask Amount (numbers, currency USD), Ask Date (date), Likelihood (dropdown: Very Likely, Likely, Possible, Uncertain), Donor Type (dropdown: Individual, Foundation, Corporation, DAF), Interests (tags: Education, Health, Youth, Environment, Arts, Housing, General), Last Contact (date), Days Since Contact (formula: TODAY minus Last Contact), Next Action (text), Next Action Date (date), Notes (long text). Groups: Active Pipeline by stage. Views: Kanban by Stage, Dashboard showing pipeline value, activity metrics.
>
> **Board 2 — Stewardship Actions:** Columns: Action Name (text), Donor (connect to Donor Pipeline), Due Date (date), Type (dropdown: Thank You Call, Thank You Letter, Impact Report, Site Visit, Event Invitation, Recognition, Personal Meeting, Proposal, Holiday Card, Birthday Acknowledgment), Status (status: Scheduled, In Progress, Complete, Overdue, Cancelled), Owner (people), Notes (long text), Completed Date (date). Automations: When Due Date passes and Status is not Complete, change to Overdue and notify Owner and Development Director. When Status changes to Complete, update Last Contact on connected Donor Pipeline item. When a new item is created on Donor Pipeline, auto-create: Thank You Call (due 1 day), Impact Report (due 90 days), Renewal Approach (due 10 months)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Donor Concierge
**Agent Purpose:** Ensure no donor falls through the cracks by managing stewardship timelines, generating personalized outreach recommendations, and predicting donor behavior patterns.

**Triggers:**
- Daily scan for overdue stewardship actions
- When a gift is received (new or renewal)
- When Days Since Contact exceeds 60 for any pipeline donor
- Monthly donor retention analysis
- When a donor's giving anniversary approaches (30 days out)

**Actions:**
- Create immediate post-gift stewardship sequence (thank you call → letter → impact report → renewal approach)
- Flag at-risk donors based on engagement decline patterns (reduced giving, fewer event attendances, slower response times)
- Generate personalized outreach suggestions based on donor interests, giving history, and recent organizational milestones
- Compile gift officer portfolio reviews: activity metrics, pipeline value, stewardship completion rates
- Draft renewal proposals incorporating specific impact data tied to the donor's previous gift
- Alert development director to LYBUNT donors approaching 18-month lapse threshold

**Data Required:**
- Donor Pipeline board
- Stewardship Actions board
- Gift history from CRM integration
- Event attendance data
- Program outcome data (for impact personalization)

**Autonomy Level:** Human-in-the-Loop
Generates recommendations and drafts communications but never sends donor-facing messages without gift officer approval. Internal alerts and reminders are autonomous.

**Example Interaction:**
> Donor Concierge alerts the Major Gifts Officer: "🎯 Three donors need attention: (1) Margaret Williams ($50K annual donor, 3 years running) — giving anniversary is in 28 days. Last year she was particularly interested in the youth mentoring program — 23 mentees graduated this year with a 91% college enrollment rate. I've drafted a personalized impact report and renewal letter at $55K. (2) Tech Corp Foundation — no contact in 72 days. Their program officer, Lisa, just posted on LinkedIn about workforce development priorities. Perfect time for a check-in; I've drafted an email referencing your shared interest in workforce outcomes. (3) New: First-time $5K donor James Rivera gave online yesterday. No thank you call scheduled — I've created one for today. His DonorSearch profile suggests $100K+ capacity. Recommend qualifying for major gift cultivation."

---

### Use Case 7: Facilities & Asset Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Non-profits often operate multiple sites — community centers, offices, shelters, food pantries, thrift stores — with minimal facilities management infrastructure. Maintenance requests come in via sticky notes, hallway conversations, and group texts. Equipment inventories (vehicles, computers, kitchen equipment, program supplies) exist in someone's head or a dusty spreadsheet. When the van breaks down or the HVAC fails at the shelter, there's no system to track the issue, assign it, or follow up. Deferred maintenance accumulates until it becomes an emergency — and emergency repairs cost 3-5x more than planned maintenance. For organizations receiving government funding, asset management is also a compliance issue: federally funded equipment over $5,000 requires tracking under 2 CFR 200.

#### The Solution
monday.com Work Management creates a **Facilities Management System** with a **Maintenance Request Board** (form-based intake, priority triage, assignment, and tracking), an **Asset Inventory Board** (equipment details, purchase date, funding source, depreciation, maintenance schedule), and a **Preventive Maintenance Calendar** (scheduled maintenance tasks with automated reminders). Automations route maintenance requests to the appropriate person based on location and type, escalate overdue requests, and trigger preventive maintenance tasks on schedule.

#### The Outcome
- 60% reduction in emergency repair costs through preventive maintenance
- Complete asset inventory for compliance and insurance purposes
- Average maintenance request resolution time reduced from 5 days to 2 days
- Audit-ready equipment records for federal grant compliance
- Better resource allocation across multiple sites

#### Discovery Questions
1. "How many physical locations do you operate, and who manages facilities across sites?"
2. "How do staff currently report maintenance issues? What's the average time to resolution?"
3. "Do you have a complete inventory of equipment and assets? Is it current enough for an audit?"
4. "Have you ever had a compliance finding related to equipment tracking on federal grants?"
5. "What percentage of your maintenance is reactive (emergency) vs. planned (preventive)?"

#### Industry Context
Non-profit facilities management involves unique considerations: donated buildings may have deed restrictions, historic properties require preservation compliance, shelters and food service facilities must meet health department codes, and ADA compliance is mandatory. Asset tracking for federal grants follows 2 CFR 200.313 (equipment) and 200.314 (supplies), requiring physical inventories every two years and disposition procedures. Insurance requirements (liability, property, D&O, auto) vary by program type — youth-serving programs need higher liability limits. Many non-profits use deferred maintenance as an unofficial budget-balancing tool, creating growing capital needs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Facilities & Asset Management system with three connected boards:
>
> **Board 1 — Maintenance Requests:** Columns: Request Title (text), Submitted By (people), Location (dropdown: Main Office, North Community Center, South Shelter, Food Pantry, Thrift Store, Warehouse), Category (dropdown: Plumbing, Electrical, HVAC, Structural, Cleaning, Grounds, IT Equipment, Vehicles, Safety, Other), Priority (status: Emergency, High, Medium, Low), Status (status: Submitted, Assigned, In Progress, Waiting on Parts, Complete, Deferred), Assigned To (people), Date Submitted (date), Date Completed (date), Resolution Time Days (formula: Completed minus Submitted), Cost (numbers, currency USD), Photos (files), Notes (long text). Form: Maintenance Request Form with all input fields. Automations: When Priority is Emergency, immediately notify Facilities Manager and COO. When Status is Submitted for more than 2 days, escalate to Facilities Manager.
>
> **Board 2 — Asset Inventory:** Columns: Asset Name (text), Asset Tag Number (text), Category (dropdown: Vehicle, Computer, Furniture, Kitchen Equipment, Program Equipment, AV Equipment, HVAC, Other), Location (dropdown: same as Board 1), Purchase Date (date), Purchase Price (numbers, currency USD), Funding Source (dropdown: Operating, Federal Grant, State Grant, Foundation Grant, Donated), Grant Number (text), Condition (status: Excellent, Good, Fair, Poor, Out of Service), Last Inspection Date (date), Next Maintenance Due (date), Warranty Expiry (date), Assigned To (people), Disposal Status (status: Active, Pending Disposal, Disposed, Transferred), Serial Number (text). Automations: When Next Maintenance Due is 14 days away, create maintenance task on Board 1.
>
> **Board 3 — Preventive Maintenance Calendar:** Columns: Task Name (text), Asset (connect to Asset Inventory), Frequency (dropdown: Weekly, Monthly, Quarterly, Semi-Annual, Annual), Last Completed (date), Next Due (date), Assigned To (people), Status (status: Upcoming, Due, Overdue, Complete), Checklist (long text), Estimated Cost (numbers, currency USD). Automations: When Next Due arrives, change Status to Due and notify Assigned To. When Status changes to Complete, update Last Completed and calculate next Next Due based on Frequency."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Facilities Guardian
**Agent Purpose:** Monitor all facilities and assets proactively, ensuring preventive maintenance stays on schedule and emergency issues get rapid response.

**Triggers:**
- Daily scan for overdue maintenance requests and preventive maintenance tasks
- When an Emergency priority request is submitted
- Monthly asset condition review
- When warranty expiration dates approach (30 days)
- Quarterly compliance check for federally funded assets

**Actions:**
- Prioritize and route maintenance requests based on urgency, location, and available staff
- Generate preventive maintenance schedules and reminders with seasonal adjustments
- Compile asset inventory reports for grant audits and insurance renewals
- Track maintenance spending by location and category to identify cost trends
- Alert leadership to deferred maintenance items accumulating risk
- Generate annual capital needs assessment based on asset age and condition data

**Data Required:**
- All three facilities boards
- Vendor contact information
- Budget data for maintenance spending

**Autonomy Level:** Escalation-Based
Routes routine requests and sends reminders autonomously. Escalates emergency requests, budget overruns, and compliance issues to COO.

**Example Interaction:**
> Facilities Guardian alerts the COO: "🏢 Weekly facilities digest: (1) Emergency: North Community Center HVAC failed yesterday — I've contacted ACME Heating (our preferred vendor) and they can come tomorrow at 9 AM. Estimated repair: $2,800. The center's after-school program is using portable heaters meanwhile. (2) Preventive: 3 vehicle oil changes overdue by 2+ weeks — scheduled all three for this Thursday at Quick Lube. (3) Compliance: The DOL-funded laptops (12 units, Grant #DL-2024-089) are due for biennial physical inventory next month. I've created a checklist and scheduled it for March 15. (4) Trend: South Shelter plumbing costs are up 180% year-over-year — 6 repair calls in 3 months. Recommend a plumber assessment for potential pipe replacement ($8-12K) vs. continued reactive repairs."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| 990 (Form 990) | Annual IRS information return required of most tax-exempt organizations, disclosing finances, governance, and activities |
| Overhead Ratio | Percentage of total expenses spent on administration and fundraising vs. program delivery (watched by Charity Navigator) |
| In-Kind | Non-cash contributions — donated goods, services, or volunteer time |
| Restricted Funds | Donations designated by the donor for a specific purpose — legally cannot be used for other purposes |
| Unrestricted Funds | General operating support that can be used for any organizational purpose |
| Theory of Change | A comprehensive description of how and why a desired change is expected to happen in a particular context |
| Logic Model | A visual framework mapping inputs → activities → outputs → outcomes → impact |
| LYBUNT | Last Year But Unfortunately Not This year — donors who gave last year but haven't renewed |
| Moves Management | Systematic process of moving prospective donors through cultivation stages toward a gift |
| Fund-a-Need | Live fundraising appeal at an event where donors raise their paddles to give at specific levels |
| 2 CFR 200 | Federal Uniform Guidance governing grants to non-federal entities — sets rules for costs, audits, and administration |
| DAF | Donor Advised Fund — a charitable giving vehicle administered by a third party where donors receive immediate tax benefit |
| Capacity Building | Investments in organizational infrastructure (staff, systems, training) that strengthen the non-profit's ability to deliver its mission |
| Collective Impact | A framework for cross-sector collaboration where multiple organizations align around shared goals and metrics |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Executive Director / CEO | Overall organizational leadership, board liaison, public face | Decision-maker |
| Chief Operating Officer / VP Operations | Day-to-day operations, facilities, HR, compliance | Decision-maker |
| Director of Programs | Manages program delivery teams, outcomes tracking | Decision-maker (for program ops) |
| Grants Manager / Director | Grant writing, compliance, reporting | Influencer |
| Volunteer Coordinator / Manager | Recruitment, onboarding, scheduling, retention of volunteers | User / Influencer |
| Development Director / CDO | Fundraising strategy, major gifts, events, donor relations | Influencer |
| Finance Director / CFO | Budget management, audit, grant financial compliance | Decision-maker (budget) |
| Board Chair | Governance oversight, strategic direction | Decision-maker (governance) |
| Program Managers / Coordinators | Direct service delivery, data collection, participant management | User |
| Facilities Manager | Building maintenance, asset management, safety | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Finance | Grant budget tracking, cost allocation, audit preparation | Unified grant financial + program reporting |
| IT | Systems integration, data management, donor database | Tech stack consolidation, CRM integration |
| Marketing / Communications | Impact storytelling, annual reports, social media | Impact data feeds directly into donor communications |
| HR | Volunteer ↔ staff coordination, background checks, training | Unified people management across paid and volunteer workforce |
| Development / Fundraising | Grant applications, donor stewardship, event operations | Shared pipeline and impact data for proposals |
| Programs | Outcome data, participant tracking, service delivery | Operations provides the infrastructure programs need to deliver |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce NPSP | Donor CRM, heavily customized for fundraising | monday.com as the operational layer — workflow, project management, and cross-functional coordination that Salesforce doesn't do well |
| Bloomerang / Little Green Light | Simple donor management for small non-profits | monday.com replaces operational spreadsheets these tools can't handle |
| Asana / Trello | General project management, used ad hoc | monday.com offers superior reporting, automations, and forms — purpose-built for non-profit ops workflows |
| VolunteerHub / SignUpGenius | Point solutions for volunteer scheduling | monday.com consolidates volunteer management into the same platform as programs, events, and grants |
| Submittable / Fluxx | Grant management point solutions | monday.com provides broader operational context — grants connected to programs, budgets, and outcomes |
| Smartsheet | Spreadsheet-based project management | monday.com is more intuitive, better automations, and the AI/Vibe story is unmatched |
| Airtable | Flexible database, popular with non-profits | monday.com provides deeper workflow automation, better dashboards, and the enterprise path as orgs grow |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Salesforce for everything" | "Salesforce is great for donor data, but your operations team is living in spreadsheets alongside it. monday.com handles the workflows — grant compliance, event planning, volunteer coordination — that Salesforce was never designed for. They integrate seamlessly." |
| "We can't afford another tool — our overhead ratio is already scrutinized" | "That's exactly the point. monday.com reduces the operational cost of everything you do — one coordinator can now manage what used to take three. The tool cost is a fraction of the staff time it saves, and it directly improves your overhead ratio by making your admin team more efficient." |
| "Our staff isn't tech-savvy — they won't adopt it" | "monday.com is designed for non-technical users. Your volunteer coordinators and program managers will be productive in hours, not weeks. And with monday.com Forms, frontline staff just fill out a simple form — they never even have to see the board." |
| "We have too many legacy systems to switch" | "You don't have to switch anything on day one. monday.com integrates with Salesforce, QuickBooks, Google Workspace, and 200+ tools. Start with one pain point — say, grant compliance — prove the value, and expand from there." |
| "We need a non-profit discount" | "monday.com offers a non-profit program with significant discounts. And the ROI case is compelling: if this saves your grants manager 10 hours per week, that's $15K+ per year in recovered capacity — multiples of the subscription cost." |

## Proof Points
*(To be populated with customer references)*
- [Non-profit organizations using monday.com for operations management]
- [Grant compliance efficiency improvements]
- [Volunteer management at scale case studies]
- [Event operations streamlining examples]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
