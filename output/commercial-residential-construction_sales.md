# Commercial & Residential Construction × Sales Playbook

## Overview

Sales teams in commercial and residential construction companies operate in one of the most relationship-driven, long-cycle, and high-stakes selling environments in any industry. Unlike SaaS or retail, construction sales involves multi-month to multi-year pursuit cycles, six- to nine-figure deal values, and complex stakeholder webs spanning owners, developers, architects, general contractors, subcontractors, and public agencies. The "sale" is often not a traditional purchase order but a bid won, a specification earned, or a negotiated contract within a competitive procurement process.

Construction sales organizations typically include estimators (who price work), business development executives (who cultivate relationships and identify pursuits), proposal managers (who assemble bid packages), and account managers (who maintain existing client relationships). In general contractors and design-build firms, headcount ranges from 5–15 in mid-market firms to 50+ in ENR Top 400 companies. In building products and materials manufacturers, sales teams mirror traditional B2B structures but must navigate the specification chain—where architects and engineers specify products that contractors purchase.

The construction sales cycle is uniquely challenging: projects are announced 6–18 months before bidding, bids are due on hard deadlines with no extensions, win rates average 15–25% on competitive bids, and a single lost pursuit can represent millions in foregone revenue. CRM adoption in construction is notoriously low—most firms rely on spreadsheets, Outlook contacts, and the institutional memory of veteran business developers who've spent decades building relationships.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | BD teams are small relative to the opportunity volume; they need to pursue more projects, respond to more RFPs, and manage more relationships without hiring proportionally |
| 2 | Replace or Radically Augment Headcount | High | AI can automate bid/no-bid analysis, proposal generation, estimating support, and competitive intelligence—tasks that consume 40%+ of BD time |
| 3 | Consolidate Tech Stack with AI | Medium-High | Teams juggle Dodge/CMD for project leads, spreadsheets for pipeline, Outlook for relationship management, and shared drives for proposals—fragmented and inefficient |

## Prioritized Use Cases

---

### Use Case 1: Construction Project Pipeline & Pursuit Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Construction BD teams track active pursuits across a chaotic landscape: project leads from Dodge Data & Analytics, ConstructConnect, or BidClerk arrive daily; owners issue RFQs with hard deadlines; pre-qualification packages must be submitted months before bidding; and team assignments for estimating, proposal writing, and presentation prep need coordination. Most firms manage this in spreadsheets or basic CRMs that don't understand construction's unique sales stages (Lead → Qualification → Pre-Qualification → Invited to Bid → Estimating → Bid Submitted → Shortlisted → Award → Contract). Leadership has no real-time visibility into pursuit volume, win rate trends, or resource allocation across active bids.

#### The Solution
monday.com CRM customized for construction pursuits with **Status columns** mapping the construction bid lifecycle (Lead Identified → Go/No-Go Review → Pre-Qual Submitted → RFP/ITB Received → Estimating → Bid Submitted → Interview/Presentation → Awarded → Lost → No Bid), **Numbers columns** for Estimated Project Value, Bid Amount, Margin %, and Probability, **People columns** for BD Lead, Estimator, and Proposal Manager, **Date columns** for Bid Due Date, Pre-Qual Deadline, and Interview Date, **Dropdown columns** for Project Type (Commercial, Residential, Industrial, Infrastructure, Mixed-Use), Delivery Method (Design-Bid-Build, Design-Build, CM at Risk, IPD), and Client Type (Private, Public, P3). **Automations** trigger go/no-go review requests, assign estimating resources, and send deadline reminders. **Dashboards** show weighted pipeline value, win rate by project type, and resource utilization.

#### The Outcome
360° pipeline visibility replacing spreadsheets. 20% improvement in win rate through better bid selectivity (go/no-go discipline). Zero missed bid deadlines. 30% more pursuits managed per BD executive through automation.

#### Discovery Questions
1. "How many active pursuits does your BD team manage at any given time, and how do you track their status?"
2. "What does your go/no-go process look like—is it structured or more gut-feel?"
3. "When a bid deadline approaches, how do you ensure estimating, proposal, and executive review all happen on time?"
4. "What's your win rate on competitive bids, and do you track it by project type or delivery method?"
5. "How does your leadership team get pipeline visibility today—do they have a real-time view or rely on weekly meetings?"

#### Industry Context
Construction pursuits follow a unique lifecycle that standard CRMs (Salesforce, HubSpot) don't natively support. The "go/no-go" decision is a critical discipline—bidding everything wastes estimating resources (an average commercial estimate takes 80–200 hours). Pre-qualification is often required 3–6 months before bid day. Public projects follow strict procurement rules (lowest responsive, responsible bidder), while private projects involve relationship-based selection. Delivery methods fundamentally change the sales process—Design-Build involves selling design capability, while Design-Bid-Build is pure price competition. SEs should understand that "closing" in construction means winning an award, which then requires contract negotiation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Construction Project Pursuit Pipeline using monday.com CRM. Columns: Project Name (text), Owner/Client (text), Client Type (dropdown: Private Developer, Public Agency, Institutional, P3/PPP), Project Type (dropdown: Commercial Office, Retail, Multifamily Residential, Single Family, Industrial/Warehouse, Healthcare, Education, Hospitality, Infrastructure, Mixed-Use), Delivery Method (dropdown: Design-Bid-Build, Design-Build, CM at Risk, CMAR/GMP, IPD, Negotiated), Estimated Project Value (numbers, USD), Bid Amount (numbers, USD), Target Margin Percent (numbers), Win Probability (numbers, percentage), Pursuit Stage (status: Lead Identified, Go/No-Go Review, Pre-Qual Submitted, RFP Received, Estimating In Progress, Internal Review, Bid Submitted, Shortlisted, Interview/Presentation, Awarded, Contract Negotiation, Lost, No-Bid), BD Lead (people), Lead Estimator (people), Proposal Manager (people), Project Location (text), Pre-Qual Deadline (date), Bid Due Date (date), Interview Date (date), Award Expected (date), Source (dropdown: Dodge, ConstructConnect, Referral, Repeat Client, Cold Outreach, Public Notice), Competitors Known (text), Key Relationships (text), Go/No-Go Score (numbers). Add subitems for pursuit action items. Automations: (1) When stage changes to 'Go/No-Go Review,' notify BD Director and create a go/no-go scorecard subitem; (2) 7 days before Bid Due Date, send escalation to BD Lead and Estimator; (3) When stage changes to 'Awarded,' notify executive team and create contract negotiation checklist; (4) When stage changes to 'Lost,' prompt for loss reason entry. Views: Main Table grouped by Pursuit Stage, Kanban by Stage, Timeline view showing bid deadlines, Dashboard with weighted pipeline value (number), win rate trend (chart), pursuits by project type (pie), monthly bid volume (bar), and upcoming deadlines (list widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PursuitPilot
**Agent Purpose:** Optimize bid selectivity, automate deadline management, and maximize win rate through data-driven pursuit recommendations.

**Triggers:**
- New project lead added to pipeline
- Pursuit stage changes
- Bid deadline within 14/7/3/1 days
- Monthly win/loss analysis schedule
- Go/No-Go review requested

**Actions:**
- Score new project leads against historical win criteria (project type, client relationship, size, location, delivery method) and recommend Go or No-Go with rationale
- Generate pursuit timelines with milestone deadlines (pre-qual, site visit, estimating start, internal review, bid submission)
- Compile win/loss analysis monthly: trends by project type, client, estimator, margin, and competitive landscape
- When a pursuit is marked "Lost," prompt for structured loss reason and add to historical database
- Alert when estimating resources are over-allocated (>3 concurrent bids per estimator)
- Pre-populate pursuit details from Dodge/ConstructConnect data when available

**Data Required:**
- Pursuit Pipeline board (all columns)
- Historical win/loss data (2+ years)
- Estimator availability and workload
- Client relationship history
- Competitive bid results (when available from public bid openings)

**Autonomy Level:** Human-in-the-Loop
Lead scoring and deadline management are autonomous. Go/No-Go recommendations are advisory—BD Director makes final call. Win/loss reports are auto-generated but reviewed before distribution. Stage transitions require human action.

**Example Interaction:**
> A new project lead arrives from Dodge: "Lakewood Mixed-Use Development, $45M, Design-Build, Private Developer (Greystone Properties)." PursuitPilot analyzes it: "Recommendation: GO. Score: 82/100. Rationale: (1) We've won 3 of 4 previous Design-Build mixed-use pursuits in this size range. (2) Greystone Properties is a repeat client—we completed their Riverdale project in 2024 (satisfied, on-time). (3) We have estimating capacity available next month. (4) Similar project type to our strongest reference: The Meridian ($52M, completed 2025). Risk: Competitor Brasfield & Gorrie has an existing relationship with Greystone's new VP of Development. Suggest: BD Lead Sarah contact Greystone's project manager Jim Torres (relationship from Riverdale) within 48 hours." The BD Director reviews, approves the pursuit, and PursuitPilot auto-creates the pursuit timeline and assigns resources.

---

### Use Case 2: Proposal & Bid Package Assembly

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Construction proposals are complex, high-stakes documents: qualifications packages, project approach narratives, team resumes, relevant experience matrices, safety records (EMR, TRIR), bonding capacity letters, schedule commitments, and pricing. A typical commercial bid response is 50–150 pages assembled under extreme time pressure (often 2–3 weeks from RFP to submission). Proposal managers spend 60%+ of their time hunting for content—searching past proposals for boilerplate, requesting updated resumes from project managers, chasing subcontractor pricing, and reformatting for each client's unique submission requirements. Version control is a nightmare, and last-minute changes cascade through the document.

#### The Solution
monday.com Work Management with a **Proposal Assembly board** tracking every component of each bid package: Section (Qualifications, Approach, Team, Experience, Safety, Schedule, Pricing), Status (Not Started, Drafting, Review, Final, Submitted), Owner, Due Date, and linked files. **monday AI** generates first-draft narratives based on project details and past proposal content. **Templates** standardize proposal structures by delivery method. **Automations** trigger section assignments when a pursuit enters "Estimating" stage, send review reminders, and compile completion checklists. **Document collaboration** enables real-time editing with version history.

#### The Outcome
50% reduction in proposal assembly time. Consistent proposal quality across all pursuits. Zero missed submission components. AI-generated first drafts saving 8–12 hours per proposal.

#### Discovery Questions
1. "How many proposals does your team produce per month, and what's the average assembly time?"
2. "Where does your proposal content live—is there a central library or do you copy from past proposals?"
3. "How do you handle version control when multiple people are editing the same proposal simultaneously?"
4. "What's the most painful part of proposal assembly—content creation, information gathering, or formatting?"
5. "Have you ever submitted a proposal with outdated team resumes, missing sections, or incorrect project references?"

#### Industry Context
Construction proposals vary dramatically by delivery method. Design-Bid-Build: primarily price-focused (sealed bid). Design-Build: qualifications-based selection (QBS) with heavy emphasis on team, approach, and relevant experience. CM at Risk: negotiations with GMP pricing. Public projects often use weighted scoring (e.g., 40% qualifications, 30% approach, 30% price). The SF330 form is standard for federal AE selections. Many firms maintain "pursuit libraries" of past proposals but struggle to keep content current. SEs should understand that proposal managers in construction are specialized roles—not generic marketing coordinators.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Proposal & Bid Package Assembly system for a construction company. Main board - Proposal Tracker: Proposal Name (text), Linked Pursuit (connect board: Pursuit Pipeline), Client (text), Delivery Method (dropdown: Design-Bid-Build, Design-Build, CM at Risk, IPD), Submission Deadline (date), Proposal Manager (people), Overall Status (status: Kickoff, In Progress, Internal Review, Executive Review, Final Assembly, Submitted, Won, Lost), Submission Method (dropdown: Online Portal, Physical Delivery, Email, Both). Create groups for each proposal section with items: Cover Letter (status, owner, due), Executive Summary (status, owner, due), Company Qualifications (status, owner, due), Project Approach/Methodology (status, owner, due), Team Organization & Resumes (status, owner, due), Relevant Experience Matrix (status, owner, due), Safety Record & EMR (status, owner, due), Project Schedule (status, owner, due), Subcontractor List (status, owner, due), Bonding & Insurance (status, owner, due), Pricing/Cost Proposal (status, owner, due), Appendices (status, owner, due). Each item has: Section Status (status: Not Started, Content Gathering, First Draft, Review, Revision, Final), Section Owner (people), Content Due Date (date), Review Due Date (date), Reviewer (people), Source Document (file), Final Version (file), Notes (text). Automations: (1) When linked pursuit reaches 'RFP Received,' auto-create proposal board from template; (2) 3 days before Content Due Date, remind Section Owner; (3) When all sections reach 'Final,' change Overall Status to 'Final Assembly' and notify Proposal Manager; (4) Day of Submission Deadline at 8 AM, send final checklist to Proposal Manager. Dashboard: Active proposals by status, section completion heatmap, days until deadline, workload by Proposal Manager."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProposalForge
**Agent Purpose:** Accelerate proposal creation by generating first-draft content, managing the assembly timeline, and ensuring completeness.

**Triggers:**
- New proposal created from pursuit stage change
- Section status changes to "Content Gathering"
- Content Due Date approaching (3 days, 1 day)
- All sections reach "Final" status
- RFP document uploaded for analysis

**Actions:**
- Parse uploaded RFP documents and auto-populate submission requirements, evaluation criteria, and key dates
- Generate first-draft narratives for Project Approach sections using project details and past proposal content
- Auto-populate team resumes from a people database with relevant project experience highlighted
- Build Relevant Experience matrices by matching project type, size, and client type to completed projects
- Generate submission checklists based on RFP requirements and flag missing items
- Compile final proposal PDF with consistent formatting and page numbering

**Data Required:**
- Proposal Assembly board
- Pursuit Pipeline board (linked)
- Past proposal content library
- Employee resume database
- Completed projects database
- Safety records (EMR, TRIR, DART rates)

**Autonomy Level:** Human-in-the-Loop
First-draft generation and content population are autonomous. All content requires human review and editing before finalization. RFP parsing and requirement extraction are autonomous. Final assembly requires Proposal Manager sign-off.

**Example Interaction:**
> An RFP arrives for a $28M healthcare clinic (Design-Build). ProposalForge parses the 45-page RFP and extracts: "Evaluation criteria: Technical Approach (35%), Team Qualifications (25%), Relevant Experience (20%), Price (20%). Submission: 5 hard copies + USB, due March 5 by 2:00 PM local time. Required sections: SF330-equivalent qualifications, narrative approach (max 10 pages), 5 comparable projects, resumes for 8 key personnel, LEED documentation approach, safety plan." It auto-creates the proposal board with all sections, assigns default owners based on past healthcare proposals, and generates: (1) A first-draft approach narrative emphasizing the firm's healthcare experience; (2) A pre-populated experience matrix with 5 healthcare projects ranked by relevance; (3) Formatted resumes for suggested key personnel with healthcare project highlights. The Proposal Manager reviews, edits, and advances each section—cutting assembly time from 120 hours to 60.

---

### Use Case 3: Subcontractor & Supplier Bid Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
General contractors rely on subcontractor and supplier pricing to assemble competitive bids. A typical commercial project requires 15–30 trade packages (concrete, structural steel, mechanical, electrical, plumbing, drywall, roofing, etc.), each requiring solicitation, scope clarification, and leveling. Bid invitations go out to 3–8 subs per trade via email; pricing trickles in over days—often arriving in the final hours before bid deadline. Estimators manually level bids in spreadsheets, comparing scope inclusions/exclusions across inconsistent formats. Missing or late sub bids force last-minute phone scrambles. The process is chaotic, error-prone, and high-pressure.

#### The Solution
monday.com Work Management with a **Sub Bid Management board** for each pursuit: Trade Package (group), Invited Subcontractors (items), Bid Status (Invited, Acknowledged, Questions Submitted, Bid Received, Leveled, Selected, Declined), Contact Info, Bid Amount, Scope Notes, Inclusions/Exclusions, Addenda Acknowledged, Bonding Capacity. **Forms** standardize sub bid submissions. **Automations** send bid invitations, reminders, and addenda notifications. **Dashboards** show coverage by trade (which trades have adequate bid coverage vs. gaps). **monday AI** assists with bid leveling by identifying scope discrepancies.

#### The Outcome
95% sub bid coverage by trade (up from 75%). 60% reduction in last-minute phone chasing. Standardized bid leveling replacing inconsistent spreadsheets. Complete audit trail for bid selection decisions.

#### Discovery Questions
1. "How many subcontractor bids do you solicit and manage for a typical project?"
2. "What's your process when a critical trade—like mechanical or electrical—has only one sub bid on bid day?"
3. "How do you level sub bids today—is it spreadsheets, and how do you handle scope discrepancies?"
4. "Do subcontractors submit bids in a standard format, or does every sub send something different?"
5. "How often do you discover after bid submission that a sub's price excluded a scope item you assumed was included?"

#### Industry Context
Subcontractor management is the heart of general contractor estimating. The "bid day" experience is legendary in construction—estimators fielding phone calls, faxes (yes, still), and emails in the final hours, making million-dollar decisions under extreme time pressure. Scope leveling (ensuring apples-to-apples comparison) is where mistakes happen: a mechanical sub excludes controls, another includes them, and the $200K difference isn't caught until construction. Pre-qualification of subs (safety records, bonding, references) adds another layer. SEs should understand that this isn't "vendor management"—it's a real-time competitive exercise that directly determines whether the GC wins or loses the project.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Subcontractor Bid Management system for a general contractor's estimating team. Create a template board that gets duplicated per project. Groups represent trade packages: Concrete & Foundations, Structural Steel, Mechanical (HVAC), Electrical, Plumbing, Fire Protection, Drywall & Framing, Roofing, Glazing/Curtainwall, Elevators, Sitework, Landscaping, Painting, Flooring, Specialties. Each item is an invited subcontractor with columns: Company Name (text), Contact Name (text), Email (email), Phone (phone), Bid Status (status: Invited, Acknowledged, RFI Submitted, Bid Received, Leveled, Selected, Alternate, Declined, No Response), Bid Amount (numbers, USD), Alternates/VE Offered (text), Scope Inclusions (long text), Scope Exclusions (long text), Addenda Acknowledged (checkbox for each addendum: Add 1, Add 2, Add 3, Add 4, Add 5), Bonding Capacity Confirmed (checkbox), Insurance Current (checkbox), EMR (numbers), Prequalified (checkbox), Bid Document (file), Notes (long text), Leveling Rank (numbers). Automations: (1) When item created, send bid invitation email with project docs link; (2) 3 days and 1 day before project bid deadline, send reminder to all subs with status not 'Bid Received'; (3) When addendum is issued (manually triggered), notify all invited subs; (4) When Bid Status changes to 'Selected,' notify sub and create subcontract initiation task. Create a form for subcontractors to submit their bids directly. Dashboard: Bid coverage by trade (how many bids received vs invited per group), total low bids by trade, trades with single/no coverage (alert), bid receipt timeline."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BidDay Commander
**Agent Purpose:** Manage subcontractor bid solicitation, track coverage, level incoming bids, and ensure no trade gaps on bid day.

**Triggers:**
- New pursuit enters "Estimating" stage (creates sub bid board from template)
- Subcontractor submits bid via form
- Bid deadline countdown (7, 3, 1 day, 4 hours, 1 hour)
- Addendum issued on project
- Trade package has zero bids within 48 hours of deadline

**Actions:**
- Auto-create sub bid board from template and pre-populate invited subs from the prequalified subcontractor database by trade and region
- When bids arrive, extract key data (price, scope notes, exclusions) and populate columns
- Flag scope discrepancies between bids in the same trade: "Sub A includes controls; Sub B excludes—$180K delta"
- Generate bid day coverage report: green/yellow/red status by trade
- When a trade has zero coverage 48 hours before deadline, auto-send additional invitations from the sub database and alert the Lead Estimator
- After award, generate subcontractor selection summary with rationale for each trade

**Data Required:**
- Sub Bid Management board (per project)
- Prequalified subcontractor database (by trade and region)
- Project scope documents and specifications
- Historical sub pricing data for reasonableness checks

**Autonomy Level:** Human-in-the-Loop
Bid solicitation, reminder sending, and coverage reporting are autonomous. Bid leveling generates recommendations but estimators make final selections. Scope discrepancy flags are advisory. Additional sub invitations for gap trades require estimator approval.

**Example Interaction:**
> It's 48 hours before bid day for the Lakewood Mixed-Use project. BidDay Commander generates a coverage report: "Trade Coverage Status — 12 of 15 trades GREEN (2+ bids). YELLOW: Fire Protection (1 bid from Apex Fire, $340K). RED: Elevators (0 bids received, 3 invited). Curtainwall (0 bids, 2 invited)." For the RED trades, it pulls from the sub database: "3 additional elevator subs available in the region: ThyssenKrupp (prequalified), KONE (prequalified), Midwest Elevator (not prequalified—EMR 1.4, above threshold). Recommend inviting ThyssenKrupp and KONE immediately." The Lead Estimator approves, and invitations go out within minutes with a "priority response requested" flag.

---

### Use Case 4: Client Relationship & Account Management (CRM)

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Construction is a relationship business. The most successful BD executives maintain deep relationships with repeat clients—developers, facility owners, institutional buyers—built over years and even decades. But this relationship intelligence lives in individual heads, Outlook contacts, and scattered notes. When a senior BD executive retires or leaves, the company loses irreplaceable client knowledge. There's no system connecting relationship history to project outcomes, tracking touchpoint frequency, or identifying accounts going cold. Leadership can't answer: "Which of our top 20 clients haven't we spoken to in 90 days?" or "What's our repeat business rate with Greystone Properties?"

#### The Solution
monday.com CRM with **Account boards** tracking key clients: Company Name, Industry Segment (Private Developer, Public Agency, Healthcare System, University, Corporate, etc.), Key Contacts (with roles and relationship strength), Relationship Owner (BD Lead), Last Touchpoint Date, Touchpoint Type (Meeting, Call, Event, Jobsite Visit, Golf/Dinner), Historical Projects (linked), Total Revenue History, Active Pursuits (linked), Win Rate with Client, Account Health Score. **Automations** alert when key accounts go "cold" (no touchpoint in 60/90 days). **monday AI** prepares pre-meeting briefings from account history. **Dashboards** show account portfolio health, repeat client revenue, and relationship coverage.

#### The Outcome
100% key account coverage (no "orphaned" relationships). 25% increase in repeat client revenue through proactive engagement. Institutional memory preserved when BD executives transition. Data-driven account planning replacing gut feel.

#### Discovery Questions
1. "What percentage of your revenue comes from repeat clients vs. new business?"
2. "If your top BD executive left tomorrow, how much client relationship knowledge would walk out the door?"
3. "How do you track touchpoints with key clients—is there a system or is it all in people's heads?"
4. "Can your VP of BD quickly see which major clients haven't been contacted in the last quarter?"
5. "When you're preparing for a client meeting, how do you pull together the history—past projects, issues, preferences?"

#### Industry Context
Repeat business rates in construction range from 40–70% for top firms—making client retention the highest-ROI activity. Construction relationships are multi-level: you need connections with the owner's VP of Construction, project managers, facility directors, and procurement. Relationship transitions are critical: when a client's PM moves to a new company, that's a new opportunity. Industry events (AGC conventions, ULI meetings, local ABC chapters) are key relationship venues. SEs should understand that "CRM" in construction means relationship management, not lead generation—the most valuable "leads" are existing clients with new projects.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Construction Client Relationship CRM using monday.com CRM. Board 1 - Client Accounts: Company Name (text), Account Tier (status: Platinum, Gold, Silver, Bronze, Prospect), Industry Segment (dropdown: Private Developer, Public Agency, Healthcare System, University/Education, Corporate/Owner-Occupant, Hospitality, Industrial, Retail/Mixed-Use), Headquarters Location (text), BD Owner (people), Backup BD (people), Annual Construction Spend Estimate (numbers, USD), Our Revenue Last 3 Years (numbers), Win Rate with Client (numbers, percentage), Repeat Business Rate (numbers, percentage), Last Touchpoint (date), Touchpoint Count YTD (numbers), Account Health (status: Thriving, Healthy, Needs Attention, At Risk, Cold), Key Decision Makers (long text), Preferences & Notes (long text), Active Pursuits (connect board: Pursuit Pipeline), Completed Projects (connect board: Project History). Board 2 - Touchpoint Log: Client (connect board: Client Accounts), Contact Person (text), Touchpoint Type (dropdown: In-Person Meeting, Phone Call, Video Call, Industry Event, Jobsite Visit, Lunch/Dinner, Golf, Holiday Gift, Conference), Date (date), BD Team Member (people), Summary (long text), Follow-Up Required (checkbox), Follow-Up Date (date), Follow-Up Owner (people). Automations: (1) When Last Touchpoint on Client Account exceeds 60 days, change Account Health to 'Needs Attention'; (2) At 90 days, change to 'At Risk' and notify VP of BD; (3) When new Touchpoint Log entry created, update Last Touchpoint and increment Touchpoint Count on Client Account; (4) When Follow-Up Required is checked, create reminder for Follow-Up Owner on Follow-Up Date. Dashboard: Account health distribution, revenue by account tier, touchpoint frequency by BD team member, accounts at risk list, upcoming follow-ups, repeat vs new business revenue trend."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RelationshipRadar
**Agent Purpose:** Proactively manage construction client relationships, prevent account attrition, and maximize repeat business through data-driven engagement.

**Triggers:**
- Account Health changes to "Needs Attention" or "At Risk"
- Client company announces new project (via news monitoring)
- Key contact changes roles or companies (LinkedIn monitoring)
- Quarterly account review schedule
- Pre-meeting preparation request

**Actions:**
- Generate weekly relationship digest: accounts needing attention, upcoming follow-ups, and suggested touchpoints
- Prepare pre-meeting briefings: client history, past projects (successes and issues), open pursuits, key contacts, and suggested talking points
- When a client company announces a new project, alert BD Owner with project details and suggest pursuit action
- Track key contact movements: if a client PM moves to a new company, create a new prospect entry and alert BD
- Generate quarterly account scorecards: revenue trend, win rate, touchpoint frequency, and recommended actions
- Identify cross-sell opportunities: "Client has only used us for commercial—they just announced a residential project"

**Data Required:**
- Client Accounts board
- Touchpoint Log board
- Pursuit Pipeline board (linked)
- Project History board
- Industry news feeds (Dodge, ENR, local business journals)

**Autonomy Level:** Escalation-Based
Monitoring, alerting, and briefing generation are fully autonomous. Outreach recommendations require BD Owner action. Account Health changes based on touchpoint data are autonomous. Quarterly scorecards are auto-generated but reviewed by VP of BD before sharing with account teams.

**Example Interaction:**
> RelationshipRadar's weekly digest: "3 accounts need attention this week. (1) Meridian Health System — Platinum account, no touchpoint in 78 days. They have a $60M campus expansion in early planning (source: Dodge alert Feb 12). Suggest: BD Lead Tom schedule lunch with VP of Facilities Mike Rearden this week. (2) Greystone Properties — Gold account, last touchpoint was Lakewood project award celebration in December. Their new VP of Development (Jennifer Park, started Jan 15) has not been introduced to our team. Suggest: Introductory meeting with Jennifer—she previously worked at Hines where we had no relationship. (3) Riverdale School District — Silver account, bond measure passed in November for $120M in school construction. No pursuit created yet. Suggest: Pre-qualification package for upcoming Phase 1 projects." Tom reviews, schedules the Meridian lunch, and asks his coordinator to set up the Greystone introduction.

---

### Use Case 5: Estimating & Preconstruction Workflow

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Estimating is the engine of construction sales. Chief Estimators manage teams of 3–15 estimators who must simultaneously develop detailed cost estimates for multiple pursuits, each requiring plan review, quantity takeoffs, material pricing, labor productivity analysis, subcontractor coordination, and risk assessment. Estimates for commercial projects can take 100–300 hours. The workflow is sequential and bottleneck-prone: takeoff before pricing, pricing before markup, markup before executive review. Most teams track estimate progress in spreadsheets or the estimating software itself (which doesn't have workflow management). The Chief Estimator has no visibility into which estimates are on track, which are behind, or where resource conflicts exist.

#### The Solution
monday.com Work Management for **Estimating Workflow**: boards tracking each estimate's phases (Plan Review → Quantity Takeoff → Material Pricing → Sub Pricing Coordination → Labor Analysis → Risk/Contingency → Markup → Executive Review → Final Compilation → Submission). **People columns** assign estimators to specific CSI divisions. **Timeline views** show overlapping estimates and resource conflicts. **Workload views** ensure no estimator is overloaded. **Automations** advance phases, trigger reviews, and flag bottlenecks. **Subitems** break estimates into CSI divisions (03 Concrete, 05 Metals, 09 Finishes, etc.).

#### The Outcome
25% faster estimate turnaround through parallel workstreams. Zero missed internal review milestones. Real-time visibility for Chief Estimator into all active estimates. Better resource allocation across concurrent pursuits.

#### Discovery Questions
1. "How many estimates does your team produce simultaneously, and how does the Chief Estimator track progress?"
2. "What's your average estimate turnaround time from RFP receipt to bid submission?"
3. "How do you handle resource conflicts when multiple estimates need the same senior estimator?"
4. "Where do bottlenecks typically occur in your estimating process—takeoff, sub coordination, or executive review?"
5. "When the CEO reviews an estimate before submission, how much context do they have on the assumptions and risks?"

#### Industry Context
Construction estimating follows CSI MasterFormat divisions (Division 01–49), providing a standardized structure for organizing costs. Estimating software (Sage Estimating, ProEst, HCSS HeavyBid, Beck Technology DESTINI) handles the math but not the workflow. The Chief Estimator role is critical—they allocate resources, set markup strategy, and make final bid recommendations. Executive review (by CEO or President) typically happens the morning of bid day, where final markup decisions are made based on competitive intelligence, capacity needs, and strategic importance. SEs should understand that the estimate IS the product in construction sales—its accuracy directly determines profitability.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an Estimating Workflow Management board for a construction company. Groups represent active estimates (one group per project). Items within each group represent estimating phases: Plan Review & Scope Analysis, Quantity Takeoff (with subitems per CSI Division: 03-Concrete, 04-Masonry, 05-Metals, 06-Wood, 07-Thermal/Moisture, 08-Openings, 09-Finishes, 22-Plumbing, 23-HVAC, 26-Electrical, 31-Earthwork, 32-Exterior), Material Pricing, Subcontractor Bid Coordination (link to Sub Bid board), Labor Productivity Analysis, General Conditions & Prelims, Risk Assessment & Contingency, Markup & Fee Strategy, Internal Review, Executive Review, Final Compilation, Submission. Columns per item: Phase Status (status: Not Started, In Progress, Review, Complete, Blocked), Assigned Estimator (people), Start Date (date), Due Date (date), Hours Estimated (numbers), Hours Actual (numbers), Confidence Level (status: High, Medium, Low), Notes (long text), Attachments (file). Board-level columns: Project Name (text), Linked Pursuit (connect board: Pursuit Pipeline), Bid Due Date (date), Estimate Value (numbers, USD), Chief Estimator (people). Automations: (1) When all Quantity Takeoff subitems reach 'Complete,' advance to Material Pricing; (2) When Executive Review is needed, notify CEO with 24-hour advance warning; (3) When any phase is 'Blocked,' notify Chief Estimator immediately. Views: Main Table, Timeline view showing all active estimates overlapping, Workload view by estimator, Dashboard with active estimate count, hours remaining by project, estimator utilization, and approaching deadlines."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** EstimateOps
**Agent Purpose:** Coordinate estimating workflows across concurrent pursuits, optimize resource allocation, and ensure timely, accurate bid delivery.

**Triggers:**
- New pursuit enters "Estimating" stage
- Phase status changes on any active estimate
- Estimator workload exceeds threshold (>50 hours/week allocated)
- Executive Review deadline approaching
- Bid Due Date countdown milestones

**Actions:**
- Auto-create estimating workflow board from template when pursuit enters estimating stage, with CSI division subitems based on project scope
- Generate daily estimating status report for Chief Estimator: progress by project, blockers, and resource conflicts
- Flag when an estimator is assigned to overlapping phases across projects and suggest reallocation
- Prepare executive review package: estimate summary, key assumptions, risk factors, margin recommendation, competitive intelligence
- Track actual hours vs. estimated hours per phase and build historical benchmarks for future planning
- When a phase is blocked, identify the dependency and notify the responsible party

**Data Required:**
- Estimating Workflow board
- Pursuit Pipeline board (linked)
- Estimator availability and skills matrix
- Historical estimate data (hours, accuracy, win rates by estimator)
- Sub Bid Management board (linked for sub pricing status)

**Autonomy Level:** Human-in-the-Loop
Workflow creation and status tracking are autonomous. Resource allocation recommendations require Chief Estimator approval. Executive review packages are auto-compiled but reviewed by Chief Estimator before distribution. Markup and fee recommendations are advisory only.

**Example Interaction:**
> EstimateOps detects a resource conflict: "Alert: Senior Estimator David Chen is assigned to executive review phases for two projects on the same day (March 3). Lakewood Mixed-Use bid due March 4, Meridian Health Clinic bid due March 5. Lakewood is 85% complete; Meridian is 72% complete. Recommend: Advance Lakewood executive review to March 2 (all predecessor phases are complete). This frees David for Meridian on March 3. Chief Estimator approval needed." The Chief Estimator approves, and EstimateOps reschedules the Lakewood executive review, notifies the CEO of the updated time, and adjusts all downstream milestones.

---

### Use Case 6: Win/Loss Analysis & Sales Performance Intelligence

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most construction companies know their win rate as a rough percentage but can't answer: "Why do we win?" "Why do we lose?" "Which project types are most profitable to pursue?" "Which estimators produce the most competitive bids?" Win/loss data is scattered across emails, debriefing notes (if they happen), and the memories of BD executives. Post-bid debriefings with clients are inconsistent—sometimes the BD lead calls, sometimes nobody does. Without systematic analysis, firms repeat the same mistakes: pursuing bad-fit projects, underpricing structural work, or over-investing in public sector bids where price always wins.

#### The Solution
monday.com Work Management with a **Win/Loss Intelligence board** populated when pursuits reach terminal stages (Awarded/Lost/No-Bid). Columns: Project Name, Final Stage, Win/Loss Reason (dropdown: Price, Relationships, Qualifications, Schedule, Safety Record, Team, Scope Understanding, Competitor Strength, Client Preference, Other), Winning Competitor, Winning Bid Amount (for public bid openings), Our Bid Amount, Margin Bid, Debrief Completed (checkbox), Debrief Notes, Lessons Learned. **monday AI** identifies patterns across win/loss data. **Dashboards** show win rates by project type, delivery method, client segment, estimator, and BD lead. Trend analysis over time.

#### The Outcome
Structured win/loss database replacing anecdotal knowledge. Data-driven bid selectivity improving win rate by 5–10 percentage points. Identification of strongest and weakest pursuit segments. Continuous improvement in pricing strategy and competitive positioning.

#### Discovery Questions
1. "What's your win rate, and can you break it down by project type, size, or delivery method?"
2. "Do you conduct post-bid debriefings with clients—and if so, what do you do with that information?"
3. "Can you identify patterns in your losses—are there project types or competitors where you consistently lose?"
4. "How does your pricing strategy evolve over time—is it based on data or intuition?"
5. "When you win, do you know why the client chose you over the competition?"

#### Industry Context
Public construction bid openings are transparent—competitors' prices are read aloud and published. This creates a unique data source for competitive intelligence. Private bids are opaque—you rarely learn competitors' pricing. Post-award debriefings are standard practice in public procurement but rare in private. Construction win rates vary dramatically: 15–20% is typical for competitive hard-bid work, 30–50% for negotiated/relationship work. SEs should understand that improving bid selectivity (choosing WHICH projects to pursue) often has more impact than improving proposal quality.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Win/Loss Analysis & Sales Intelligence system for a construction company. Board: Win/Loss Register. Columns: Project Name (text), Linked Pursuit (connect board: Pursuit Pipeline), Final Outcome (status: Won, Lost on Price, Lost on Qualifications, Lost on Relationships, Lost - Other, No-Bid, Withdrawn), Project Type (mirror from pursuit), Delivery Method (mirror from pursuit), Client Type (mirror from pursuit), Estimated Project Value (numbers, USD), Our Bid Amount (numbers, USD), Winning Bid Amount (numbers, USD, for public bids), Bid Spread Percentage (formula: (Our Bid - Winning Bid) / Winning Bid * 100), Winning Competitor (text), BD Lead (people), Lead Estimator (people), Margin Bid (numbers, percentage), Primary Win/Loss Reason (dropdown: Price Competitiveness, Client Relationship, Team Qualifications, Relevant Experience, Schedule Commitment, Safety Record, Innovation/Approach, Competitor Incumbent, Scope Understanding, Political/Preference), Secondary Reason (same dropdown), Client Debrief Completed (checkbox), Debrief Date (date), Debrief Notes (long text), Lessons Learned (long text), Actionable Changes (long text). Automations: (1) When pursuit reaches 'Awarded' or 'Lost,' auto-create entry in Win/Loss Register; (2) 1 week after loss, remind BD Lead to complete client debrief; (3) Monthly, trigger summary report generation. Dashboard: Overall win rate (number widget), win rate by project type (bar chart), win rate by delivery method (pie), win rate by estimator (bar), average bid spread on losses (number), win/loss trend over 12 months (line chart), top loss reasons (bar chart), wins by BD Lead (pie), revenue won YTD vs target (progress bar)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** WinRate Analyst
**Agent Purpose:** Transform win/loss data into actionable strategic insights, improve bid selectivity, and continuously optimize sales performance.

**Triggers:**
- New win or loss entry created
- Client debrief completed
- Monthly analysis schedule
- Quarterly strategic review preparation
- Go/No-Go review requested (to provide historical context)

**Actions:**
- Analyze win/loss patterns and generate monthly intelligence report: trending win rate, strongest/weakest segments, estimator performance, competitive landscape
- When a Go/No-Go review is requested, provide historical context: "We've pursued 8 similar projects in the last 2 years—won 2, lost 4 on price, no-bid 2. Average bid spread on losses: 6.2%"
- Identify emerging patterns: "Win rate on healthcare Design-Build has increased from 20% to 45% over 12 months—recommend increasing pursuit investment in this segment"
- Flag strategic misalignment: "We're spending 40% of estimating hours on public hard-bid work where our win rate is 12%—below the 15% threshold for profitability"
- Compile competitive intelligence from public bid openings: pricing trends by competitor, market share shifts

**Data Required:**
- Win/Loss Register board
- Pursuit Pipeline board (linked, historical)
- Estimating hours data
- Public bid opening results
- Industry benchmarks for win rates

**Autonomy Level:** Fully Autonomous
Data analysis, pattern identification, and report generation are fully autonomous. Strategic recommendations are advisory—VP of BD and CEO make strategic decisions. Go/No-Go context is automatically surfaced during reviews.

**Example Interaction:**
> WinRate Analyst's monthly report: "February 2026 Analysis — Win Rate: 28% (up from 22% in January). Key insights: (1) We won 3 of 4 Design-Build pursuits this month, all in healthcare—this is now our strongest segment. (2) We lost both public hard-bid pursuits by 8%+ margin—recommend reducing public sector pursuit volume. (3) Estimator Maria Lopez has the highest win rate at 38% (11 of 29 career bids). She was assigned to all 3 healthcare wins. Recommendation: Assign Maria to upcoming Meridian Health System pursuit. (4) Competitor Turner Construction has won 3 of the last 5 pursuits we've competed against them—all on qualifications, not price. We need to strengthen our team presentations when competing against Turner. Action item created for BD Director."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| GC | General Contractor — the prime contractor who manages the overall construction project |
| Sub / Subcontractor | Specialty trade contractor (mechanical, electrical, concrete, etc.) hired by the GC |
| BD | Business Development — the sales function in construction companies |
| RFP / RFQ / ITB | Request for Proposal / Request for Qualifications / Invitation to Bid — procurement solicitation types |
| Design-Bid-Build | Traditional delivery: owner hires architect, then bids construction separately |
| Design-Build | Single entity provides both design and construction; sold on qualifications |
| CM at Risk / CMAR | Construction Manager at Risk — hybrid delivery with GMP (Guaranteed Maximum Price) |
| GMP | Guaranteed Maximum Price — cost ceiling in CMAR contracts |
| IPD | Integrated Project Delivery — collaborative contract with shared risk/reward |
| Pre-Qualification | Screening process where contractors demonstrate capability before being invited to bid |
| Bid Leveling | Comparing subcontractor bids on equal scope basis (apples-to-apples) |
| CSI MasterFormat | Standardized classification system for construction specs and costs (Divisions 01–49) |
| EMR | Experience Modification Rate — insurance metric reflecting safety performance (1.0 = average) |
| TRIR | Total Recordable Incident Rate — OSHA safety metric |
| Takeoff | Quantity measurement from construction drawings (counts, lengths, areas, volumes) |
| Markup | The fee, overhead, and contingency added to direct costs to determine bid price |
| ENR Top 400 | Engineering News-Record's annual ranking of the largest US contractors |
| Hard Bid | Competitive sealed-bid process where lowest price typically wins |
| Negotiated Work | Projects awarded through relationship and qualifications rather than low bid |
| Bonding | Surety bonds guarantee contractor performance; capacity limits how much work a contractor can take |
| SF330 | Standard Form 330 — federal qualifications statement for AE (architecture/engineering) selections |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP of Business Development | Sets BD strategy, manages key accounts, oversees go/no-go decisions | Decision-maker |
| Chief Estimator | Manages estimating team, sets pricing strategy, recommends final bid amounts | Decision-maker |
| CEO / President | Final bid approval, markup decisions, strategic client relationships | Decision-maker |
| Proposal Manager | Assembles bid packages, manages proposal content and deadlines | Influencer |
| Senior Estimator | Develops detailed cost estimates for assigned projects | User |
| BD Executive / Account Manager | Cultivates client relationships, identifies pursuits, leads presentations | User |
| Preconstruction Manager | Coordinates between estimating, operations, and design teams during pursuit | Influencer |
| Marketing Coordinator | Supports proposal production, maintains qualifications content | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations / Project Management | Hands off won projects for execution; provides past performance data for proposals | Project execution tracking, closeout documentation, lessons learned |
| Finance | Bonding capacity, insurance, cash flow projections for bids, margin analysis | Financial dashboard integration, bonding capacity tracking |
| HR | Team resumes for proposals, safety training records, EMR management | People database for proposal auto-population |
| Marketing | Brand collateral, case studies, website project pages, award submissions | Content management, client-facing materials |
| Legal | Contract review, risk assessment, insurance requirements | Contract management, compliance tracking |
| IT | CRM infrastructure, estimating software, plan management | Tech stack consolidation |
| Product & R&D | New product information for specification support, BIM objects | Product launch coordination, specification tools |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce | Enterprise CRM not built for construction bid lifecycle | Lacks construction-specific stages, delivery methods, and sub bid management; monday.com's flexibility lets you build the exact construction CRM workflow without expensive customization |
| Procore | Construction management platform (mainly operations) | Procore's preconstruction module is limited; CRM is bolt-on. monday.com offers stronger workflow automation and AI capabilities |
| BuildingConnected | Subcontractor bid management (owned by Autodesk) | Point solution for sub bids only; doesn't cover full BD pipeline, proposals, or client relationships |
| Cosential / Unanet | AEC-specific CRM for proposals and BD | Niche, expensive, dated UX; lacks AI, modern automations, and platform breadth |
| HubSpot | Inbound marketing CRM | Wrong paradigm for construction—construction sales is relationship-based and bid-driven, not inbound-funnel |
| Spreadsheets (Excel/Google Sheets) | The dominant "tool" in construction sales | No automation, no collaboration, no audit trail, no dashboards. monday.com replaces the spreadsheet chaos |
| Dodge / ConstructConnect | Project lead databases (data sources, not CRM) | Complementary, not competitive—these feed leads INTO monday.com. Integration opportunity |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Procore" | "Procore excels at construction operations—once you've won the project. monday.com handles everything BEFORE the win: pursuit pipeline, proposals, estimating workflow, sub bid management, and client relationships. They're complementary—and we integrate with Procore for the handoff." |
| "Our estimators won't use anything besides their estimating software" | "We're not replacing Sage or ProEst—we're managing the workflow AROUND estimating. Who's assigned to which estimate, what phase are they in, when is executive review, are sub bids coming in? That's what's in spreadsheets today, and that's what monday.com replaces." |
| "Construction sales is all relationships—you can't put relationships in software" | "You're right that relationships are everything. That's exactly why you need to protect them. When your top BD exec retires, those relationships shouldn't retire with them. monday.com preserves the institutional memory: who knows who, when you last talked, what projects you've done together." |
| "We only have 3-4 BD people—we don't need a platform" | "With only 3-4 people, you can't afford to waste any effort. How many hours per week do they spend on proposal assembly, chasing sub bids, or searching for past project info? monday.com gives those hours back for actual relationship building and business development." |
| "We tried a CRM before and nobody used it" | "Traditional CRMs fail in construction because they're built for B2B SaaS funnels, not construction bid lifecycles. When the stages, terminology, and workflows don't match how you actually sell, people revert to spreadsheets. monday.com lets you build YOUR process—your stages, your go/no-go criteria, your proposal workflow. It fits you, not the other way around." |
| "Bid day is too chaotic for a system—we just need phones and spreadsheets" | "Bid day is chaotic BECAUSE of the spreadsheets. Imagine seeing real-time sub bid coverage by trade, automated reminders to non-responsive subs, and instant scope discrepancy flags—all without picking up the phone. monday.com doesn't slow down bid day; it makes it manageable." |

## Proof Points
*(To be populated with customer references)*
- General contractors using monday.com for pursuit pipeline and BD management
- Construction companies managing estimating workflows and sub bid coordination
- AEC firms tracking client relationships and proposal assembly
- References from ENR-ranked contractors leveraging monday.com for sales operations

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
