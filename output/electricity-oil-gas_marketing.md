# Electricity, Oil & Gas × Marketing Playbook

## Overview

Marketing departments in the electricity, oil, and gas sector operate in one of the most complex and scrutinized communications environments in any industry. Unlike consumer brands where marketing's primary job is demand generation, energy marketing teams must simultaneously manage brand reputation (often under activist and regulatory pressure), communicate complex technical offerings to sophisticated B2B buyers (utilities selling wholesale power, E&P companies marketing acreage, midstream firms marketing pipeline capacity), support retail customer programs (for regulated utilities with millions of ratepayers), and navigate the industry's existential brand challenge: positioning as responsible energy providers during the global energy transition.

The typical energy marketing organization is lean relative to the company's revenue—a $10B utility might have a marketing team of 30–60 people, while a similar-sized tech company would have 300+. These teams are organized around Corporate Communications & Brand, Digital Marketing & Customer Engagement (for utilities with retail customers), B2B Marketing & Business Development Support (for upstream, midstream, and merchant power), Regulatory & Public Affairs Communications, Sustainability & ESG Communications, and Internal Communications. They manage relationships with 10–20 agencies (creative, PR, digital, regulatory communications, government affairs) and must coordinate messaging across audiences that often have conflicting interests: shareholders want profit, regulators want reliability, environmentalists want decarbonization, communities want jobs, and employees want purpose.

Regulatory constraints add unique complexity. Utility marketing spend is often recoverable through rate cases only if it meets "public benefit" criteria (energy efficiency education, safety awareness, storm preparedness). Oil & gas companies face greenwashing scrutiny from the FTC, SEC (climate disclosure rules), and activist groups that monitor every sustainability claim. Pipeline companies communicate with FERC, state PUCs, landowners, and environmental groups simultaneously during permitting processes. Every public statement carries legal, regulatory, and reputational risk—making marketing in this sector a high-stakes, low-margin-for-error discipline.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Lean marketing teams must manage complex multi-audience campaigns, agency relationships, and regulatory communications without headcount growth |
| 2 | Consolidate Tech Stack with AI | Medium-High | Marketing teams juggle 15–25 tools (CMS, DAM, social management, analytics, email, project management) with limited integration |
| 3 | Replace or Radically Augment Headcount | Medium | AI can augment content production, analytics, and campaign optimization—critical when one person covers three roles |

## Prioritized Use Cases

---

### Use Case 1: Multi-Audience Campaign Management & Orchestration

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
A single energy company initiative—say, a new renewable energy program—requires coordinated campaigns targeting 5+ distinct audiences: retail customers (enrollment marketing), commercial/industrial customers (different value proposition), regulators (compliance communications), media (press strategy), investors (ESG narrative), and internal employees (culture alignment). Each audience requires different messaging, different channels, different approval chains, and different success metrics. Today, the marketing team manages this across email threads, shared drives, and disconnected project trackers. A campaign manager for the renewable program might have 40+ deliverables tracked in a spreadsheet with no visibility into dependencies, agency deliverable status, or regulatory review bottlenecks. When the VP of Marketing asks "where are we on the renewable program launch?"—the answer takes 2 days to assemble.

#### The Solution
monday.com Work Management provides a unified campaign orchestration platform. A Campaign Hub board for each major initiative tracks all deliverables across audiences with columns for audience segment, channel (digital, print, direct mail, social, earned media, regulatory filing), deliverable type, creative agency, status, approval chain, regulatory review status, launch date, and budget. Sub-boards for each audience segment contain detailed production workflows: creative brief → first draft → legal review → regulatory review → revision → final approval → production → launch. Automations route deliverables through the correct approval chain based on audience and channel (e.g., anything customer-facing in a regulated utility automatically goes to regulatory affairs). Dashboards show campaign readiness by audience, deliverable completion percentage, approval bottlenecks, and budget allocation vs. spend.

#### The Outcome
50% reduction in campaign coordination time. Launch timelines compressed by 3 weeks through parallel workstream management. Zero regulatory compliance gaps in customer-facing materials. Real-time campaign status eliminates "where are we?" fire drills.

#### Discovery Questions
1. "When you launch a major initiative that touches multiple audiences—customers, regulators, investors, media—how do you coordinate the messaging and timing across all those streams?"
2. "How many deliverables does a typical multi-audience campaign involve, and how do you track them today?"
3. "What's your regulatory review process for customer-facing communications—how long does it take, and what happens when it creates a bottleneck?"
4. "When your CMO or VP asks for campaign status, how quickly can you give them an accurate answer?"
5. "Have you ever launched a customer communication that hadn't completed regulatory review—or delayed a launch because you lost track of an approval?"

#### Industry Context
In regulated utilities, customer communications are literally regulated—the Public Utility Commission (PUC) may require pre-approval of marketing materials for rate-funded programs (energy efficiency, demand response, low-income assistance). Oil & gas companies face SEC scrutiny on sustainability marketing claims (SEC Climate Disclosure Rule, FTC Green Guides). SEs should understand that "regulatory review" in energy marketing isn't optional polish—it's a legal requirement that can delay campaigns by weeks if not planned for. The platform must make regulatory review a first-class workflow step, not an afterthought.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Multi-Audience Campaign Orchestration Hub with: (1) Campaign Master Board — columns: Campaign Name (text), Initiative (dropdown: Renewable Program Launch, Rate Case Communications, Storm Season Preparedness, Brand Refresh, ESG Report Launch, Energy Efficiency Program, Safety Campaign), Target Audience (dropdown: Residential Customers, Commercial/Industrial, Regulators/PUC, Media/Press, Investors/Analysts, Employees, Community/Landowners), Channel (dropdown: Digital Ads, Email, Direct Mail, Social Media, Earned Media/PR, Website, Regulatory Filing, Internal Comms, Events, Bill Insert), Deliverable Type (dropdown: Creative Brief, Ad Copy, Landing Page, Press Release, Regulatory Filing, Social Content, Video, Email Template, Fact Sheet, FAQ, Talking Points), Agency (dropdown: Creative Agency, PR Agency, Digital Agency, In-House), Status (status: Briefing, Drafting, Legal Review, Regulatory Review, Revision, Final Approval, In Production, Live, Complete), Owner (people), Reviewer (people), Regulatory Approval Required (checkbox), Regulatory Status (status: Not Required, Pending Submission, Under Review, Approved, Revisions Requested), Target Launch Date (date), Actual Launch Date (date), Budget (numbers, USD). Populate with 12 sample deliverables for a 'Clean Energy Program Launch' spanning residential email, C&I fact sheet, PUC filing, press release, social media series, investor deck update, employee announcement, community FAQ, digital ads, landing page, bill insert, and media talking points. (2) Approval Workflow Board — columns: Deliverable (connect to Master), Review Stage (status: Legal, Regulatory, Brand, Executive), Reviewer (people), Submitted Date (date), Due Date (date), Decision (status: Pending, Approved, Revisions Required, Rejected), Comments (long text). Automation: when Regulatory Approval Required is checked and Status changes to Legal Review complete, auto-create item in Approval Workflow with Review Stage = Regulatory. Dashboard: campaign readiness gauge by audience segment, deliverables by status (stacked bar), regulatory review pipeline, timeline view showing all launch dates, budget allocation by channel."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Campaign Orchestrator
**Agent Purpose:** Proactively manage multi-audience campaign timelines, detect bottlenecks, and ensure regulatory review compliance for all customer-facing materials.

**Triggers:**
- New campaign deliverable created with Target Launch Date
- Deliverable status unchanged for 3+ business days
- Regulatory review item overdue or approaching deadline
- Campaign launch date within 10 business days with deliverables not in "Final Approval" or later
- New initiative added to Campaign Master Board

**Actions:**
- Generate campaign timeline with reverse-scheduled milestones based on launch date, factoring in standard review durations (Legal: 3 days, Regulatory: 10 days, Executive: 2 days)
- Detect deliverables at risk of missing launch date and alert campaign manager with specific bottleneck identification
- Flag any customer-facing deliverable missing the "Regulatory Approval Required" checkbox (safety net for compliance)
- Generate weekly Campaign Status Digest for VP of Marketing showing all active campaigns, readiness scores, and at-risk items
- When regulatory revisions are requested, auto-create revision tasks and recalculate downstream timelines
- Identify message consistency gaps: compare key claims across audience-specific deliverables within the same campaign

**Data Required:**
- Campaign Master Board with all deliverables
- Approval Workflow Board
- Standard review duration benchmarks by review type
- Regulatory requirements matrix (which audiences/channels require PUC/legal review)
- Historical campaign data for timeline estimation

**Autonomy Level:** Human-in-the-Loop
Timeline generation and risk alerts are autonomous. Regulatory compliance flags (missing review checkboxes) are autonomous safety nets. Message consistency analysis provides recommendations for human review. All communications to external stakeholders (agencies, regulators) require human approval.

**Example Interaction:**
> Two weeks before the Clean Energy Program launch, the Campaign Orchestrator runs its daily readiness scan. It identifies that the PUC regulatory filing is still in "Under Review" (submitted 12 days ago, typical turnaround is 15 business days), but the residential email campaign and digital ads—which reference the same program terms—are scheduled to go live in 10 days.
>
> The agent alerts the campaign manager: "Risk: Residential email and digital ads for Clean Energy Program reference tariff terms that are pending PUC approval. If PUC requests revisions to program terms, these materials will need rework. Recommendation: (1) Prepare alternate versions with generic language as contingency, (2) Contact regulatory affairs for PUC timeline update, (3) Consider 5-day launch delay buffer for customer-facing materials while proceeding with internal comms and media backgrounders on schedule."
>
> The campaign manager decides to prepare contingency versions. The agent creates duplicate deliverable items tagged "Contingency — Generic Terms" and routes them through an expedited review workflow.

---

### Use Case 2: Agency & Creative Production Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy marketing teams rely heavily on external agencies—most companies work with 5–15 agencies (creative, PR, digital, media buying, regulatory communications, government affairs, multicultural marketing). Managing agency deliverables, feedback cycles, budgets, and performance across this ecosystem is a full-time job that nobody has. Briefs go out via email, feedback happens in tracked-changes documents, version control lives in shared drives (or doesn't), and budget tracking is reconciled quarterly when invoices arrive. A typical frustration: the creative agency delivers a brand campaign concept, the marketing team provides feedback, the agency revises—but the regulatory communications agency (who needs to adapt the campaign for ratepayer communications) doesn't see the updated creative for 3 weeks because nobody thought to loop them in. Meanwhile, the brand team has spent $40K of the $50K creative budget without anyone realizing it until the invoice arrives.

#### The Solution
monday.com Work Management serves as the agency-facing production management platform. An Agency Management board tracks all agency relationships with contract details, retainer amounts, budget allocation, and performance scores. A Creative Production board manages every deliverable across agencies with columns for project, agency, deliverable type, brief status, draft versions, feedback rounds, approval status, and deadline. Agencies are granted guest access to their relevant boards—they update deliverable status, upload drafts for review, and receive feedback directly in the platform. Budget tracking boards capture estimated vs. actual costs per project and per agency with running totals against annual retainers and project budgets. Automations notify downstream agencies when upstream deliverables are approved (e.g., when brand creative is approved, auto-notify regulatory comms agency to begin adaptation).

#### The Outcome
35% reduction in creative production cycle time. Agency-to-agency handoff delays eliminated through automated notifications. Real-time budget visibility prevents overruns—average 15% budget savings. Version control issues eliminated (single source of truth for all creative assets).

#### Discovery Questions
1. "How many agencies do you work with, and how do you manage the flow of briefs, deliverables, and feedback across all of them?"
2. "When one agency's deliverable is a dependency for another agency's work, how do you manage that handoff today?"
3. "How do you track creative production budgets against retainers or project budgets—in real-time, or when invoices arrive?"
4. "Have you experienced version control problems—someone working from an outdated creative brief or brand asset?"
5. "What does your agency performance evaluation process look like? Is it structured or more anecdotal?"

#### Industry Context
Energy companies often have agency relationships that span decades—the PR agency that handles crisis communications during pipeline incidents, the regulatory comms firm that's navigated 20 rate cases. These relationships are deep and political. SEs should position the platform as enhancing (not threatening) these relationships by making collaboration smoother and reducing the "whose fault was the delay?" finger-pointing. Guest access for agencies is a key feature—agencies appreciate structured workflows because it reduces their internal overhead too. Note: some energy companies require agencies to sign NDAs and data handling agreements before platform access—build this into the onboarding workflow.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Agency & Creative Production Management system with: (1) Agency Registry Board — columns: Agency Name (text), Specialty (dropdown: Creative/Brand, PR/Communications, Digital/Performance, Media Buying, Regulatory Comms, Government Affairs, Multicultural, Research/Insights), Contract Type (dropdown: Retainer, Project-Based, Hybrid), Annual Budget (numbers, USD), Spent YTD (numbers, USD), Remaining (formula), Primary Contact (text), Account Lead Internal (people), Contract End Date (date), Performance Score (numbers, 1-5), NDA Status (status: Active, Expired, Pending), Status (status: Active, On Hold, Under Review, Terminated). (2) Creative Production Board — columns: Project Name (text), Campaign (dropdown), Agency (connect to Registry), Deliverable Type (dropdown: Brand Concept, Ad Creative, Video, Photography, Copy/Messaging, Landing Page, Email Design, Social Content, Print Collateral, Regulatory Adaptation, Translation), Brief Status (status: Drafting, Sent, Acknowledged, Questions, In Production), Current Version (numbers), Draft File (files), Feedback (long text), Feedback Round (numbers), Approval Status (status: In Review, Revisions Requested, Approved, Killed), Approver (people), Deadline (date), Estimated Cost (numbers), Actual Cost (numbers), Downstream Agency (connect to Registry, for handoff). Automation: when Approval Status changes to Approved and Downstream Agency is not empty, notify Downstream Agency contact and create task on their queue. When Spent YTD exceeds 80% of Annual Budget on Agency Registry, notify Account Lead. (3) Budget Tracker Dashboard: spend by agency (bar), budget utilization gauge per agency, project cost estimate vs actual scatter plot, monthly spend trend line. Add guest access configuration note for agency collaborators."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Production Maestro
**Agent Purpose:** Optimize agency production workflows, prevent budget overruns, and ensure seamless handoffs between agencies working on interconnected deliverables.

**Triggers:**
- New creative brief sent to agency (Brief Status = Sent)
- Agency hasn't acknowledged brief within 48 hours
- Deliverable deadline within 5 business days and status not "In Review" or later
- Approval granted on deliverable with downstream agency dependency
- Actual Cost uploaded that changes budget utilization above threshold
- Monthly budget reconciliation (1st of each month)

**Actions:**
- Track brief-to-delivery cycle time by agency and deliverable type, building performance benchmarks
- Send escalating reminders for unacknowledged briefs and overdue deliverables
- Auto-trigger downstream agency workflows when upstream approvals complete, including sharing approved assets
- Generate budget alerts: "Creative Agency A has used 82% of annual retainer with 4 months remaining. At current run rate, you'll exceed budget by $65K."
- Produce quarterly Agency Performance Report: delivery timeliness, revision rates, budget adherence, and internal satisfaction scores
- Identify production pattern inefficiencies: "Video projects average 4.2 feedback rounds (industry benchmark: 2.5). Consider implementing detailed video briefs to reduce revision cycles."

**Data Required:**
- Agency Registry and Creative Production boards
- Budget tracking data
- Historical deliverable data (12+ months) for benchmarking
- Calendar integration for deadline management
- Agency contact information for notifications

**Autonomy Level:** Escalation-Based
Production tracking, reminders, and benchmark analysis are fully autonomous. Budget alerts are autonomous. Downstream agency notifications require brief human confirmation (one-click approve). Agency performance reports are generated autonomously for internal review—never shared externally without approval.

**Example Interaction:**
> The Production Maestro detects that the PR agency has been assigned a press release for the Q3 earnings announcement with a deadline 8 business days away, but the brief hasn't been acknowledged after 36 hours. It sends a gentle reminder to the PR agency contact: "Brief for Q3 Earnings Press Release sent March 5 — please confirm receipt and timeline."
>
> Simultaneously, the agent notices that the approved brand campaign creative (finished by the Creative Agency yesterday) has a downstream dependency: the Regulatory Comms Agency needs to adapt the visual identity for bill insert communications. It auto-notifies the Regulatory Comms Agency: "Brand campaign creative approved — assets available for regulatory adaptation. Bill insert deliverable deadline: April 15. Brief and approved files attached." It also creates a new production item on the Regulatory Comms Agency's queue.
>
> During month-end reconciliation, the agent flags: "Digital Agency has submitted $28K in additional charges for 'scope additions' not tracked in Production Board. Recommend requesting itemized breakdown and creating corresponding project items for audit trail."

---

### Use Case 3: Energy Transition & ESG Communications Program

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every major energy company is navigating the energy transition—and marketing/communications is ground zero for the narrative war. Companies must communicate decarbonization commitments, renewable investments, and ESG progress to investors (who increasingly tie capital allocation to ESG scores), regulators (who set emissions reporting requirements), customers (who want clean energy options), employees (who want to work for responsible companies), and activists (who scrutinize every claim for greenwashing). The challenge: these audiences need different messages, but those messages must be internally consistent. When the CEO tells investors "we're investing $5B in renewables" but the operations team's website still prominently features fossil fuel production, it becomes a PR crisis. Currently, ESG communications are managed by 2–3 people using document trackers and email chains, with no systematic way to ensure message consistency across the 15+ channels and audiences they touch weekly.

#### The Solution
monday.com Work Management creates an ESG Communications Command Center. A master ESG Narrative Board tracks every key claim, commitment, and data point the company has publicly stated—with columns for claim text, source document, verification status, last verified date, applicable audiences, and channels where it's been published. A Content Calendar board manages all ESG-related communications across channels (sustainability report sections, investor presentations, website content, social posts, press releases, employee newsletters, regulatory filings) with timeline views showing the cadence and dependencies. A Claims Verification board connects marketing claims to underlying data sources (emissions data, renewable capacity, investment figures) with automatic flagging when source data is updated (triggering review of dependent communications). Dashboards show the ESG content pipeline, claim verification status, and channel coverage by audience.

#### The Outcome
100% message consistency across audiences (single source of truth for all ESG claims). Zero greenwashing risk incidents (automated claim verification). 40% reduction in ESG report production time. Proactive narrative management replaces reactive crisis response.

#### Discovery Questions
1. "How do you ensure that sustainability claims made in your investor presentation are consistent with what's on your website, in your sustainability report, and in customer communications?"
2. "When your emissions data gets updated or a renewable project milestone changes, how quickly do you update all the public-facing communications that reference it?"
3. "Has your company ever been challenged on a sustainability claim—by media, activists, or regulators—and how did you verify the accuracy of your communications?"
4. "How many people on your team touch ESG communications, and how do they coordinate with the sustainability/ESG data team?"
5. "What's your process for producing the annual sustainability report—how long does it take, and what are the biggest bottlenecks?"

#### Industry Context
Greenwashing accusations can be devastating—Shell, BP, TotalEnergies, and major utilities have all faced legal challenges and reputational damage over sustainability marketing claims. The SEC Climate Disclosure Rule (finalized 2024) requires specific, auditable climate-related disclosures. The EU's Corporate Sustainability Reporting Directive (CSRD) affects energy companies with European operations. FTC Green Guides are being updated with stricter requirements for environmental marketing claims. SEs should understand that ESG communications in energy isn't "nice-to-have marketing"—it's a legal, regulatory, and financial risk management function. The CMO and General Counsel are equally invested in this workflow.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an ESG Communications Command Center with: (1) ESG Claims Registry Board — columns: Claim ID (auto-number), Claim Text (long text, e.g. 'Committed to net-zero Scope 1 & 2 emissions by 2040'), Category (dropdown: Emissions Reduction, Renewable Investment, Community Impact, Workforce Diversity, Safety, Water/Waste, Biodiversity), Source Document (dropdown: Sustainability Report, 10-K Filing, Investor Presentation, CEO Speech, Press Release, Website), Data Source Owner (people), Verification Status (status: Verified, Pending Verification, Needs Update, Retired), Last Verified Date (date), Next Review Date (date), Applicable Audiences (tags: Investors, Regulators, Customers, Media, Employees, Community), Published Channels (tags: Website, Sustainability Report, Investor Deck, Press Release, Social Media, Annual Report, Regulatory Filing), Risk Level (status: Low, Medium, High). Populate with 8 sample claims: net-zero target, renewable capacity, emissions reduction %, community investment $, workforce diversity stats, safety record, water reduction target, methane reduction commitment. (2) ESG Content Calendar Board — columns: Content Piece (text), Type (dropdown: Report Section, Press Release, Blog Post, Social Post, Investor Slide, Email Newsletter, Video, Infographic, Regulatory Filing, Website Update), Audience (dropdown), Channel (dropdown), Linked Claims (connect to Claims Registry), Author (people), Status (status: Planning, Drafting, Data Verification, Legal Review, Design, Final Approval, Published), Publish Date (date), Review Deadline (date). (3) Claims Verification Tracker — columns: Claim (connect to Registry), Data Point (text), Current Value (text), Source System (dropdown: Emissions Database, Financial System, HR System, Operations Data, Third-Party Audit), Last Updated (date), Updated By (people), Change Description (long text), Dependent Content Items (connect to Content Calendar). Automation: when Data Point value changes, flag all Dependent Content Items for review and notify Authors. When Verification Status is Pending for >30 days, escalate to Data Source Owner. Dashboard: claims by verification status (donut), content pipeline timeline, channel coverage heat map by audience, upcoming publication dates."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Narrative Guardian
**Agent Purpose:** Ensure consistency and accuracy of all ESG communications by cross-referencing claims against verified data and flagging inconsistencies before publication.

**Triggers:**
- New content item created that links to ESG claims
- ESG data point updated in Claims Verification Tracker
- Content item moves to "Legal Review" or "Final Approval" stage
- Quarterly ESG data refresh cycle
- External event: media inquiry or activist report mentioning the company's ESG claims

**Actions:**
- Cross-reference content drafts against Claims Registry to verify all ESG statements match current verified claims
- Flag discrepancies: "Draft press release references '45% emissions reduction' but Claims Registry shows verified figure is '42.3% as of Q2 2025'"
- When source data changes, identify all published content containing outdated figures and create update tasks
- Generate pre-publication consistency check: compare new content against all other recent ESG communications for message alignment
- Produce quarterly ESG Communications Audit: all active claims, verification status, channel coverage gaps, and upcoming renewal dates
- Monitor external sources (news alerts, social media) for challenges to company ESG claims and create rapid response briefs

**Data Required:**
- ESG Claims Registry with all verified claims
- Content Calendar with linked claims
- Claims Verification Tracker with source data
- Published content archive (website, reports, filings)
- External monitoring feeds (media, social, regulatory)

**Autonomy Level:** Human-in-the-Loop
Consistency checking and discrepancy flagging are autonomous. Data change notifications and content update task creation are autonomous. Pre-publication checks are generated autonomously for human review—content is never published or modified without human approval. External monitoring alerts are flagged for PR/comms team response.

**Example Interaction:**
> The ESG Narrative Guardian detects that the sustainability team has updated the Scope 1 emissions figure in the verification tracker: the 2025 number is finalized at 2.1 million metric tons CO2e, down from the preliminary estimate of 2.3 million that was used in the Q3 investor presentation.
>
> The agent immediately identifies 7 content items referencing the old figure: the investor presentation (published), the sustainability report draft (in progress), two website pages, a customer email about clean energy, and a regulatory filing. It creates prioritized update tasks: "Sustainability Report — Section 2.4: Update Scope 1 figure from '~2.3M MT' to '2.1M MT CO2e (verified).' Note: This is a favorable update (8.7% improvement) — recommend highlighting in narrative." For the already-published investor presentation, it flags: "Q3 Investor Deck slide 14 shows preliminary estimate. Recommend footnote update for next quarterly deck or errata notice if materially different per SEC guidance."
>
> The communications director reviews, approves the update tasks, and adds a note: "Use this as a positive narrative — accelerated reduction ahead of plan. Draft social media content to announce."

---

### Use Case 4: Retail Customer Program Marketing (Utilities)

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Regulated utilities manage 10–30 customer programs simultaneously: energy efficiency rebates, demand response, time-of-use rate enrollment, electric vehicle charging programs, community solar, low-income assistance (LIHEAP), weatherization, smart thermostat programs, green power purchasing, and more. Each program has its own marketing budget (often mandated by the PUC), enrollment targets, regulatory reporting requirements, creative assets, and channel mix. A marketing team of 5–10 people is responsible for all of it—which means each person manages 3–6 programs, each with quarterly campaigns, seasonal adjustments, and constant reporting to regulatory affairs on spend and enrollment metrics. The result: cookie-cutter marketing, missed enrollment targets, and PUC scrutiny over whether ratepayer-funded marketing dollars are being spent effectively.

#### The Solution
monday.com Work Management and monday.com CRM combine to create a Program Marketing Management system. A Program Portfolio board tracks all active customer programs with enrollment targets, marketing budgets, YTD spend, enrollment progress, channel performance, and regulatory reporting deadlines. Each program has a linked Campaign Board with deliverables, channels, A/B tests, and performance metrics. monday.com CRM tracks customer segments and enrollment leads, with automations that trigger follow-up campaigns based on customer actions (started enrollment but didn't complete, participated in one program but eligible for another). Dashboards provide real-time program performance: enrollment vs. target, cost-per-enrollment by channel, and marketing spend vs. PUC-approved budget—with automatic alerts when spending pace is off track.

#### The Outcome
20% increase in program enrollment rates through targeted, data-driven campaigns. 30% reduction in cost-per-enrollment through channel optimization. 100% on-time regulatory reporting on marketing spend and program performance. Marketing team manages 2x more programs without headcount increase.

#### Discovery Questions
1. "How many active customer programs does your marketing team support, and how many people are dedicated to program marketing?"
2. "How do you track enrollment progress against targets for each program—and how quickly can you adjust campaigns when a program is behind?"
3. "What does your regulatory reporting process look like for program marketing spend—is it automated or manually assembled?"
4. "Do you do cross-program marketing—identifying customers in one program who are eligible for another?"
5. "How do you measure cost-per-enrollment by channel, and how does that inform your budget allocation?"

#### Industry Context
Utility customer programs are often funded through rider charges on customer bills—meaning the marketing budget is ratepayer money subject to PUC oversight. Underspending means leaving enrollment targets unmet (and potentially returning funds). Overspending triggers PUC scrutiny. Marketing effectiveness directly impacts the utility's regulatory standing and future program approvals. SEs should understand that "enrollment" in utility parlance is equivalent to "conversion" in traditional marketing—but with regulatory reporting attached to every dollar spent. Programs like demand response and time-of-use rates are becoming critical for grid management as renewable penetration increases, making marketing's role in driving adoption a genuine operational need, not just a brand exercise.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Utility Customer Program Marketing Manager with: (1) Program Portfolio Board — columns: Program Name (text), Category (dropdown: Energy Efficiency, Demand Response, EV/Electrification, Renewable/Green Power, Low-Income Assistance, Smart Home, Rate Programs, Weatherization), Enrollment Target (numbers), Current Enrollment (numbers), Enrollment % (formula), Marketing Budget Approved (numbers, USD), Marketing Spend YTD (numbers, USD), Budget Utilization % (formula), Cost Per Enrollment (formula), PUC Reporting Deadline (date), Program Manager (people), Status (status: Active, Ramping Up, Seasonal Pause, Under PUC Review, Completed). Populate with 8 programs: Home Energy Audit Rebate, Smart Thermostat Program, TOU Rate Enrollment, Community Solar, EV Charger Rebate, Low-Income Weatherization, Commercial Demand Response, Green Power Choice. (2) Campaign Tracker Board (per program, use one as example) — columns: Campaign Name (text), Program (connect to Portfolio), Channel (dropdown: Direct Mail, Email, Digital Ads, Social Media, Bill Insert, IVR/Phone, Community Event, Partner Channel, Website), Audience Segment (dropdown: Residential-All, Residential-Low Income, Residential-EV Owner, Commercial-Small, Commercial-Large, Industrial), Start Date (date), End Date (date), Budget (numbers), Spend (numbers), Impressions (numbers), Clicks (numbers), Enrollments (numbers), Cost Per Enrollment (formula), A/B Variant (text), Status (status: Planning, Live, Paused, Complete, Killed). Automation: when Budget Utilization % exceeds 90% on Portfolio Board, notify Program Manager; when Enrollment % is below 50% and we're past midpoint of program year, flag as At Risk. Dashboard: enrollment progress gauges by program, cost-per-enrollment comparison by channel (bar), budget utilization vs enrollment achievement scatter plot, seasonal enrollment trend lines."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Program Performance Optimizer
**Agent Purpose:** Monitor program enrollment and marketing performance in real-time, recommend campaign adjustments, and automate PUC regulatory reporting.

**Triggers:**
- Weekly performance scan (every Monday at 8:00 AM)
- Enrollment rate drops below projected pace for any program
- Campaign cost-per-enrollment exceeds benchmark by >25%
- PUC reporting deadline within 30 days
- New customer enrollment data imported (integration with CIS/billing system)

**Actions:**
- Analyze enrollment trends by program and project end-of-year attainment based on current pace
- Identify underperforming channels and recommend budget reallocation: "Community Solar email CPE is $45 vs digital ads at $22. Recommend shifting $15K from email to digital for Q3."
- Detect cross-program opportunities: "8,400 Smart Thermostat Program participants are eligible for TOU Rate Enrollment but haven't been targeted. Recommended: trigger cross-enrollment email campaign."
- Auto-generate PUC quarterly marketing report: spend by channel, cost-per-enrollment, enrollment vs target, and narrative summary
- Identify seasonal enrollment patterns and recommend campaign timing adjustments based on historical data
- Flag budget pacing issues: "EV Charger Rebate program has spent 78% of marketing budget but achieved only 45% of enrollment target. Recommend efficiency review before additional spend."

**Data Required:**
- Program Portfolio and Campaign Tracker boards
- Customer enrollment data (CIS/billing system integration)
- Historical campaign performance (12+ months)
- Customer segmentation data for cross-program targeting
- PUC reporting templates and requirements

**Autonomy Level:** Human-in-the-Loop
Performance analysis and recommendations are autonomous. PUC report drafts are generated autonomously for human review and approval before submission. Budget reallocation recommendations require program manager approval. Cross-program campaign recommendations require marketing lead approval before execution.

**Example Interaction:**
> During its Monday performance scan, the Program Performance Optimizer identifies that the Community Solar program is tracking at 62% of enrollment pace needed to hit the annual target of 15,000 subscribers. It analyzes channel performance and finds: email campaigns are generating enrollments at $52 each (above the $35 benchmark), while a small-budget social media test achieved $18 per enrollment but was paused after the test period.
>
> The agent recommends: "Community Solar enrollment is at risk. Recommended actions: (1) Reactivate social media campaign with $25K incremental budget from underutilized email allocation. Projected: 1,389 additional enrollments at $18 CPE. (2) Launch cross-program campaign targeting 12,000 Green Power Choice subscribers who indicated interest in solar during enrollment. Estimated conversion: 8-12% = 960-1,440 enrollments at near-zero incremental acquisition cost. (3) Schedule community event push for May-August when solar interest peaks historically (43% of annual enrollments in Q2-Q3)." The program manager approves all three recommendations and the agent creates the corresponding campaign items.

---

### Use Case 5: Crisis & Reputation Communications Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies face crisis communications scenarios that other industries rarely encounter: pipeline leaks or explosions, refinery incidents, power outages affecting millions, oil spills, wildfire liability (see: PG&E), dam failures, and cyberattacks on grid infrastructure. When a crisis hits, the communications team has minutes—not hours—to activate a coordinated response across media relations, social media, customer communications, government/regulatory notifications, employee communications, community outreach, and investor relations. Today, most energy companies have crisis communications plans in binders (or PDFs) that were last updated 18 months ago. The actual coordination happens through frantic phone calls, group texts, and email chains. Post-incident analysis consistently finds that communications gaps—delayed customer notifications, inconsistent media statements, missed regulatory filing deadlines—caused as much reputational damage as the incident itself.

#### The Solution
monday.com Work Management provides a digital Crisis Communications Command Center that activates from a pre-built template. When a crisis is declared, a one-click activation creates a populated board with all required response actions organized by stakeholder audience and timeline (0–2 hours: regulatory notification, employee safety alert, social media monitoring; 2–8 hours: media holding statement, customer notification, executive talking points; 8–24 hours: detailed press release, community outreach, investor communication). Each action has a pre-assigned owner (from the crisis team roster), required approvals, regulatory deadlines, and template content. Status columns track completion in real-time. A War Room dashboard shows response progress across all audiences, identifies overdue actions, and provides a chronological response log for post-incident review and regulatory documentation.

#### The Outcome
Crisis response activation time reduced from hours to minutes. Zero missed regulatory notification deadlines (PHMSA 1-hour rule for pipeline incidents, NERC 24-hour rule for grid events). Consistent, approved messaging across all channels. Complete audit trail for post-incident regulatory review and litigation support.

#### Discovery Questions
1. "When was the last time your crisis communications plan was activated—and what worked well vs. what fell through the cracks?"
2. "How quickly can your team get an approved holding statement to media and a notification to affected customers after a significant incident?"
3. "What are your regulatory notification deadlines for different incident types, and have you ever come close to missing one?"
4. "After an incident, how do you compile the communications timeline for regulatory review or litigation—is it documented in real-time or reconstructed after the fact?"
5. "Do you conduct crisis communications drills, and if so, what's the biggest gap you've identified?"

#### Industry Context
Pipeline operators must notify the National Response Center within 1 hour of a significant release (PHMSA regulations). Electric utilities must report grid disturbances to NERC within 24 hours (and to DOE within 6 hours for major events). Nuclear facilities have NRC notification requirements measured in minutes. Beyond regulatory requirements, the court of public opinion moves at social media speed—a single viral video of a pipeline leak or black smoke from a refinery reaches millions before the company issues its first statement. SEs should understand that crisis communications in energy isn't theoretical—these companies WILL face incidents, and the quality of their communications response directly impacts regulatory outcomes, litigation exposure, and license to operate.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Crisis Communications Command Center with: (1) Crisis Response Template Board — columns: Action Item (text), Audience (dropdown: Regulators, Media, Customers, Employees, Community, Investors, Government Officials, Board of Directors), Timeline (dropdown: Immediate 0-2hr, Near-Term 2-8hr, Same Day 8-24hr, Ongoing 24hr+), Priority (status: Critical, High, Medium), Owner Role (dropdown: VP Comms, Media Relations Lead, Social Media Manager, Customer Comms, Government Affairs, Investor Relations, Employee Comms, Legal), Assigned To (people), Status (status: Not Started, Drafting, Legal Review, Approved, Sent/Published, N/A), Regulatory Deadline (checkbox), Deadline Time (text), Approval Required From (people), Template Content (long text), Actual Completion Time (date), Channel (dropdown: Phone Call, Email, Press Release, Social Media, Website Banner, Text/SMS, IVR Message, Regulatory Portal, Internal Portal, Town Hall). Populate with 20 template items: NRC/PHMSA Regulatory Notification (Immediate), Employee Safety Alert (Immediate), Social Media Monitoring Activation (Immediate), Media Holding Statement (Immediate), Customer Service Script Update (0-2hr), Executive Talking Points (0-2hr), Government Official Notification (0-2hr), Website Incident Banner (0-2hr), Detailed Press Release (2-8hr), Customer Email Notification (2-8hr), Community Hotline Activation (2-8hr), Investor Relations Q&A (2-8hr), Employee Town Hall Scheduling (2-8hr), Social Media Response Protocol (2-8hr), Detailed Media Q&A (8-24hr), Community Meeting Scheduling (8-24hr), Regulatory Detailed Report (8-24hr), Board Communication (8-24hr), Ongoing Media Monitoring Dashboard (Ongoing), Post-Incident Review Scheduling (Ongoing). (2) Crisis Log Board — columns: Timestamp (date with time), Entry Type (dropdown: Decision, Communication Sent, Media Inquiry, Regulatory Contact, Stakeholder Feedback, Status Update), Description (long text), Author (people), Supporting Document (files). Dashboard: response progress by audience (progress bars), overdue items (red flags), timeline of completed actions, team workload distribution."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Crisis Response Activator
**Agent Purpose:** Instantly activate crisis communications playbooks, enforce regulatory notification deadlines, and maintain a real-time response log for audit purposes.

**Triggers:**
- Manual crisis activation trigger (one-click by VP Comms or designated crisis lead)
- Integration trigger: incident reported in safety management system
- Regulatory notification deadline approaching (countdown timer)
- Social media monitoring detects spike in brand mentions with negative sentiment
- Media inquiry logged without an approved response available

**Actions:**
- Instantiate crisis response board from template, assign owners from on-call roster, and set all timeline-based deadlines
- Send immediate notifications to all crisis team members with role assignments and first-priority actions
- Track regulatory notification deadlines with countdown timers and escalating alerts (30 min, 15 min, 5 min before deadline)
- Auto-populate template content (holding statements, customer notifications) with incident-specific details from the crisis declaration
- Maintain chronological crisis log by auto-logging every status change, communication sent, and decision made
- Generate real-time War Room dashboard showing response progress across all audiences
- Post-crisis: compile complete response timeline, communications archive, and regulatory submission log for legal and compliance review

**Data Required:**
- Crisis Response Template board
- Crisis team roster with on-call schedule
- Regulatory deadline matrix by incident type
- Template content library (holding statements, customer notification templates, media Q&A frameworks)
- Social media monitoring integration
- Safety/incident management system integration

**Autonomy Level:** Escalation-Based
Board activation, team notification, and deadline tracking are fully autonomous. Template content pre-population is autonomous (but all content requires human approval before external release). Regulatory deadline escalation alerts are autonomous and will notify progressively senior leaders as deadlines approach. Crisis log maintenance is fully autonomous. No external communications are sent without human approval.

**Example Interaction:**
> At 3:47 AM, the safety management system reports a natural gas release at a compressor station in rural Oklahoma. The Crisis Response Activator instantly creates the crisis response board, identifies the on-call crisis team (weekend rotation), and sends push notifications: "CRISIS ACTIVATED — Natural gas release at Compressor Station 14, Oklahoma. Report to virtual war room. VP Comms: approve holding statement by 4:15 AM. Regulatory Lead: PHMSA notification due by 4:47 AM (1-hour deadline)."
>
> The agent pre-populates template content: the media holding statement reads "[Company] is responding to a natural gas release at our facility in [County], Oklahoma. Emergency response teams are on site. There are no reported injuries at this time. We are working with local emergency services and will provide updates as information becomes available." The VP Comms reviews, adjusts one sentence, approves at 4:08 AM. The agent logs: "4:08 AM — Media holding statement approved by [VP name]. Ready for release."
>
> At 4:32 AM—15 minutes before the PHMSA deadline—the regulatory notification hasn't been marked complete. The agent escalates: "URGENT: PHMSA 1-hour notification deadline is 4:47 AM. Regulatory notification not yet confirmed. Escalating to General Counsel." The regulatory lead confirms submission at 4:41 AM—6 minutes before deadline. The agent logs the timestamp and begins tracking the next wave of response actions.

---

### Use Case 6: Brand & Digital Asset Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies undergoing transformation—rebranding after mergers, pivoting messaging toward clean energy, updating visual identity for the energy transition—accumulate massive libraries of digital assets: logos, photography (facilities, employees, renewables), video content, infographics, templates, brand guidelines, and approved messaging frameworks. These assets live across shared drives, agency servers, individual laptops, and outdated DAM systems that nobody likes using. When a regional marketing manager in Texas needs an approved photo of the company's wind farm for a customer event, they can't find it—so they either use an outdated version, pull something from Google Images, or email corporate requesting help (which takes 3 days). Meanwhile, the brand team just spent $200K on a photography shoot and the images are sitting on the photographer's delivery drive.

#### The Solution
monday.com Work Management serves as a lightweight DAM (Digital Asset Management) and brand governance platform. An Asset Library board catalogs all approved brand assets with columns for asset type (logo, photo, video, template, icon), category (brand identity, facilities, people, renewable energy, safety, community), usage rights (internal only, customer-facing, media/press, social media, all uses), format, resolution, expiration date (for time-limited rights), and the actual files. A Brand Guidelines board documents current standards: approved colors, fonts, logo usage rules, messaging frameworks, and approved boilerplate copy. A Request Board allows field marketing teams to request assets (with approval workflow for sensitive materials). Automations alert the brand team when assets are approaching rights expiration and when new assets are uploaded by agencies for cataloging.

#### The Outcome
75% reduction in asset search time. Zero brand compliance violations from unauthorized asset usage. $100K+ annual savings by maximizing utilization of commissioned photography and video. Brand consistency maintained across 10+ regional offices and agency partners.

#### Discovery Questions
1. "Where do your approved brand assets live today—and how confident are you that people in the field are using the right versions?"
2. "When you commission photography or video, how do you ensure those assets get distributed and used across the organization?"
3. "Have you ever found outdated logos, wrong brand colors, or unauthorized images in customer-facing materials?"
4. "How does your field marketing team access brand assets—is it self-service or do they go through corporate?"
5. "Do you track usage rights and expiration dates for commissioned assets like photography and stock images?"

#### Industry Context
Energy companies undergoing energy transition are rebranding aggressively—adding green to color palettes, featuring renewable assets in hero photography, updating taglines from "powering America" to "powering America's future." This creates a dual-asset challenge: maintaining both legacy brand assets (for ongoing operations communications) and new brand assets (for transformation narrative). Many energy companies also have strict photography policies at facilities (no photos showing certain equipment configurations, security-sensitive locations, or proprietary processes). Brand governance in energy is more than aesthetics—it's security and compliance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Brand & Digital Asset Management system with: (1) Asset Library Board — columns: Asset Name (text), Asset Type (dropdown: Logo, Photography, Video, Infographic, Template, Icon/Illustration, Stock Image, Brand Guidelines Doc), Category (dropdown: Brand Identity, Facilities, People/Culture, Renewable Energy, Safety, Community, Products/Services, Executive/Leadership, Events), Usage Rights (status: All Uses, Customer-Facing Only, Internal Only, Media/Press Only, Restricted-Approval Required), Format (tags: JPG, PNG, SVG, PDF, MP4, PSD, AI, DOCX, PPTX), Resolution (dropdown: Web-72dpi, Print-300dpi, 4K Video, Source File), File (files), Thumbnail (files), Uploaded By (people), Upload Date (date), Rights Expiration (date), Photographer/Agency (text), Tags (tags), Download Count (numbers), Status (status: Active, Under Review, Archived, Expired Rights). Populate with 10 sample assets: Primary Logo, Horizontal Logo White, Wind Farm Hero Photo, Solar Array Aerial, CEO Headshot, Safety Team Photo, Brand Guidelines PDF, Customer Email Template, Social Media Template Pack, Facility B-Roll Video. (2) Asset Request Board — columns: Requester (people), Department (dropdown), Need Description (long text), Asset Type Needed (dropdown), Usage (dropdown: Customer Event, Presentation, Social Media, Website, Print, Regulatory Filing), Deadline (date), Fulfilled By (people), Assets Provided (connect to Library), Status (status: New, Searching, Fulfilled, Cannot Fulfill). Automation: when Rights Expiration is within 30 days, notify Brand Team Lead; when new File uploaded to Library, set Status to Under Review and notify brand manager. Dashboard: asset library by category (donut), most requested asset types (bar), assets expiring this quarter, request fulfillment time average."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Brand Asset Librarian
**Agent Purpose:** Organize, tag, and surface brand assets intelligently while enforcing usage rights and maintaining brand compliance.

**Triggers:**
- New asset file uploaded to Asset Library
- Asset request submitted via Request Board
- Rights Expiration date within 30 days
- Quarterly brand audit (scan published materials for compliance)
- Search query from field marketing team

**Actions:**
- Auto-tag uploaded assets based on image/video content analysis (identify: renewable energy, facility type, people, safety equipment)
- Match asset requests against library using semantic search and suggest top-3 matching assets
- Flag assets approaching rights expiration and recommend renewal or replacement
- Generate quarterly Brand Compliance Report: asset usage statistics, most common request types, gaps in library coverage
- Identify asset gaps: "No approved photography of Battery Storage Facility — 4 requests in last quarter went unfulfilled. Recommend commissioning shoot."
- Archive outdated assets (pre-rebrand materials) while maintaining access for historical/legal purposes

**Data Required:**
- Asset Library board with all files and metadata
- Asset Request board with historical requests
- Brand Guidelines board for compliance checking
- Usage analytics (download counts, request patterns)

**Autonomy Level:** Human-in-the-Loop
Asset tagging and search recommendations are autonomous. Rights expiration alerts are autonomous. Library gap analysis and recommendations are generated for brand team review. Asset archival recommendations require human approval. No assets are deleted—only archived.

**Example Interaction:**
> A regional marketing manager in Houston submits an asset request: "Need high-resolution photos of our renewable energy operations for a customer advisory board presentation next week. Specifically interested in wind and solar." The Brand Asset Librarian searches the Asset Library and responds within seconds: "Found 3 matching assets: (1) Wind Farm Hero Photo — 300dpi, all uses approved, uploaded Oct 2025. (2) Solar Array Aerial — 300dpi, customer-facing approved, uploaded Jan 2026. (3) Offshore Wind Construction — 72dpi web only (not suitable for presentation). Recommendation: Assets 1 and 2 meet your needs. Note: we don't currently have approved photography of our newest solar facility (commissioned Q4 2025). Consider requesting a shoot — 3 other teams have made similar requests this quarter."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Ratepayer | Customer of a regulated utility whose rates are set by the PUC — marketing spend on their behalf is scrutinized |
| PUC / PSC | Public Utility Commission / Public Service Commission — state regulators that approve utility rates and programs |
| Rate Case | Regulatory proceeding where a utility requests approval for rates, programs, and associated marketing budgets |
| Rider | Line item on a utility bill funding a specific program (e.g., energy efficiency rider) — marketing for rider-funded programs must demonstrate effectiveness |
| Energy Transition | The global shift from fossil fuels to renewable energy — the defining narrative challenge for energy marketing |
| Greenwashing | Making misleading claims about environmental practices — legally and reputationally devastating in energy |
| ESG | Environmental, Social, and Governance — reporting framework increasingly important for investor relations and corporate reputation |
| IRP | Integrated Resource Plan — utility's long-term plan for meeting electricity demand, often the basis for marketing clean energy investments |
| Demand Response | Programs that incentivize customers to reduce electricity use during peak periods — marketing drives enrollment |
| TOU | Time-of-Use rates — pricing that varies by time of day, requiring customer education marketing |
| FERC | Federal Energy Regulatory Commission — regulates interstate energy commerce |
| PHMSA | Pipeline and Hazardous Materials Safety Administration — regulates pipeline safety, including incident notification requirements |
| Community Solar | Program allowing customers to subscribe to a share of a solar project — heavily marketed to customers without suitable rooftops |
| License to Operate | The implicit social contract that allows energy companies to operate — maintained through community relations and responsible communications |
| E-ISAC | Electricity Information Sharing and Analysis Center — sector-specific cybersecurity threat intelligence (relevant for crisis comms) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CMO / VP of Marketing | Overall marketing strategy, brand, and communications | Decision-maker |
| Director of Communications | Corporate comms, media relations, crisis communications | Decision-maker (comms) |
| Director of Digital Marketing | Digital channels, website, social media, email marketing | Decision-maker (digital) |
| VP of Government & Regulatory Affairs | Regulatory relationships, PUC filings, government communications | Influencer (regulatory) |
| Sustainability / ESG Director | ESG reporting, sustainability narrative, climate communications | Influencer (ESG) |
| Customer Program Manager | Utility customer program marketing and enrollment | User / Budget holder |
| Brand Manager | Brand identity, asset management, creative standards | User |
| Regional Marketing Manager | Field marketing execution in specific territories | User |
| General Counsel | Legal review of all public communications, especially ESG claims | Influencer (legal) |
| Investor Relations Director | Financial and ESG communications to investment community | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Customer Operations / Contact Center | Marketing campaigns drive call volume; contact center needs current program details and messaging | Customer service workflow management, knowledge base management, customer feedback tracking |
| Sustainability / ESG | Marketing communicates sustainability commitments; ESG team provides data | ESG data management, sustainability report production workflow, stakeholder engagement tracking |
| Government & Regulatory Affairs | Marketing materials require regulatory review; regulatory team communicates with PUCs and legislators | Regulatory filing management, stakeholder relationship management, legislative tracking |
| Sales / Business Development | Marketing supports B2B sales for wholesale, commercial, and industrial customers | CRM, sales enablement content management, proposal generation workflows |
| IT | Marketing depends on IT for website, digital platforms, analytics, and data infrastructure | Digital project management, MarTech stack management, data analytics workflows |
| HR / Internal Communications | Marketing and internal comms coordinate on employer brand, culture campaigns, and employee engagement | Employee engagement campaigns, internal newsletter management, EVP content |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Asana / Wrike | Project management for marketing teams | Good for task management but weak on the unique compliance, regulatory review, and crisis management workflows energy marketing requires. Win on configurability for regulated industries and integrated dashboards |
| Salesforce Marketing Cloud | Enterprise marketing automation | Over-engineered and expensive for energy marketing teams. Campaign orchestration, not operational marketing management. Position monday.com for the operational layer (production, approvals, asset management) alongside or replacing SFMC for program marketing |
| Sprinklr / Hootsuite | Social media management | Niche tools for one channel. Energy marketing needs cross-channel campaign orchestration including non-digital channels (bill inserts, community events, regulatory filings). Win on unified workflow across all channels |
| Bynder / Brandfolder | Digital Asset Management | Dedicated DAM tools are expensive ($50K–$150K/year) and solve only asset storage. monday.com provides asset management PLUS production workflow, approval chains, and request management in one platform |
| Adobe Workfront | Creative production management | Strong for creative teams but complex and expensive. Energy marketing teams need production management PLUS regulatory compliance workflow, crisis management, and program marketing—broader scope than Workfront addresses |
| Spreadsheets & Email | The true incumbent | The real competitor. Most energy marketing teams manage campaigns, budgets, and program performance in Excel with email-based approvals. Win by demonstrating the cost of manual tracking: missed deadlines, budget overruns, compliance gaps, and the 2-day "where are we?" report assembly |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We're a small marketing team—we don't need a platform" | "That's exactly why you need one. A team of 8 managing 25 customer programs, 12 agency relationships, and crisis readiness can't afford to waste time on status meetings and spreadsheet reconciliation. monday.com gives each person the visibility to manage 3x more without working 3x harder." |
| "Our regulatory review process is too complex for a project tool" | "We've seen that regulatory review is often the biggest bottleneck in energy marketing—and the most dangerous to leave unstructured. monday.com lets you build the exact regulatory approval workflow your PUC requires, with audit trails that satisfy compliance teams and automations that prevent anything from going public without proper review." |
| "We already use [Salesforce / HubSpot] for marketing" | "Those are great for marketing automation—sending emails, tracking leads, managing customer journeys. But who manages the production of the content, the agency relationships, the regulatory approvals, the crisis communications playbook? That operational layer is where monday.com fits—upstream of your automation tools, making sure the right content gets created, approved, and delivered on time." |
| "Our agency handles most of our marketing execution" | "All the more reason you need visibility. When 5 agencies each manage a piece of your marketing and none of them can see what the others are doing, you get inconsistent messaging, duplicated effort, and budget surprises. monday.com gives your agencies a shared workspace (with guest access) while giving you real-time visibility into everything they're producing." |
| "We can't justify another software cost in a rate case" | "The question for the PUC isn't 'did you buy software?'—it's 'are you spending ratepayer marketing dollars effectively?' monday.com helps you demonstrate exactly that: lower cost-per-enrollment, higher program participation rates, and complete audit trails showing every dollar spent. Most utilities find the efficiency gains more than cover the platform cost—and the improved regulatory reporting actually strengthens your rate case position." |

## Proof Points
*(To be populated with customer references)*
- Utility companies using monday.com for customer program marketing
- Energy companies managing brand transformation initiatives
- Companies with complex agency ecosystems using monday.com for production management
- [Placeholder for specific customer stories and metrics]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
