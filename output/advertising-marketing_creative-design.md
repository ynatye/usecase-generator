# Advertising & Marketing × Creative & Design Playbook

## Overview

Creative and Design departments are the revenue engine of advertising agencies — the teams that produce the actual work clients pay for. These departments encompass art directors, copywriters, designers, motion graphics artists, video editors, retouchers, UX/UI designers, and production artists, typically organized under an Executive Creative Director (ECD) or Chief Creative Officer (CCO). At a mid-market agency (200–500 people), the creative department represents 35–45% of total headcount. At large holding company networks, creative teams span thousands of practitioners across global offices.

The creative process in advertising is uniquely pressurized. Teams work on multiple client accounts simultaneously, each with different brand guidelines, approval chains, and deadlines. A single campaign might require 50–200+ individual assets across formats: TV scripts, digital banners (15+ sizes), social content (platform-specific), OOH, print, email, website landing pages, and presentation decks. The "always-on" content model — where brands need daily social posts, reactive content, and real-time marketing — has increased creative output volume by 5–10x over the past decade without proportional headcount growth. Creative teams are perpetually over-capacity.

The industry is in the midst of a generative AI revolution. Tools like Midjourney, DALL-E, Runway, and Adobe Firefly are transforming ideation, comp creation, and even final asset production. But adoption is uneven and legally uncertain — questions around copyright, client approval of AI-generated work, and creative integrity remain unresolved. Meanwhile, creative departments still struggle with fundamental workflow problems: lost files, unclear feedback, version control nightmares, asset management chaos, and the perennial frustration of creative briefs that arrive incomplete or change mid-production. These operational inefficiencies cost agencies 20–30% of creative capacity.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Creative output demands have grown 5-10x while headcount is flat — teams must produce more without burning out |
| 2 | Consolidate Tech Stack with AI | Medium-High | Creative workflow spans 8-12 tools (Figma, Adobe CC, DAM, review tools, PM tools, Slack, email) with no unified thread |
| 3 | Replace or Radically Augment Headcount | Medium | AI-assisted ideation, asset versioning, and production can multiply individual creative output by 3-5x |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Campaign Creative Production Workflow

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
A campaign goes from brief to launch through a complex, multi-stage workflow: briefing → concepting → internal review → client presentation → revisions → production → asset adaptation → final approval → trafficking/delivery. At every stage, work gets stuck. Briefs arrive incomplete ("the client will fill in the details later"). Internal reviews take 3 days because the CD is in back-to-back meetings. Client feedback comes via email, marked-up PDFs, Slack messages, and phone calls — all captured inconsistently. Asset adaptation (taking a hero concept and producing 40 format variations) is tedious and error-prone. Nobody has a real-time view of where the campaign stands across all deliverables. The result: missed deadlines, last-minute fire drills, and burned-out creatives.

#### The Solution
monday.com Work Management as the end-to-end creative production hub. Each campaign is a high-level item with connected deliverables, each deliverable has a structured workflow with stages, assignments, deadlines, and approval gates. Creative briefs are submitted via standardized forms (no more incomplete briefs). Review and approval workflows route to the right approvers with SLA tracking. Dashboards show real-time campaign status across all deliverables, and automations handle the handoffs between stages.

#### The Outcome
- Campaign production cycle time reduced by 25–30%
- Zero incomplete briefs (form validation ensures required fields)
- Internal review bottlenecks exposed and resolved through SLA tracking
- Real-time visibility eliminates 80% of "where's my project?" status requests
- Creative team capacity effectively increases 15–20% through eliminated waste

#### Discovery Questions
1. "Walk me through a campaign from brief to delivery — how many handoffs, tools, and approval steps are involved?"
2. "What percentage of your creative briefs arrive complete with everything the team needs to start work?"
3. "How do your creatives currently know what they should be working on today — and how much time do they spend figuring that out?"
4. "When a campaign is running late, how early do you know — and what's the escalation process?"
5. "How many asset formats and variations does a typical campaign require, and how do you track completion across all of them?"

#### Industry Context
The creative production process in advertising is fundamentally different from software development or marketing operations. It's non-linear — creative work goes through ideation cycles that can't be forced into rigid sprint frameworks. Feedback is subjective ("make it feel more premium") and iterative. The "two-week sprint" doesn't map to a world where a client can request fundamental direction changes after seeing the first round. Successful creative workflow tools must accommodate creative flexibility while providing operational structure. The rise of "versioning" — adapting hero assets into dozens of format-specific variations — has created a production volume problem that's fundamentally operational, not creative.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Campaign Creative Production workspace for an advertising agency. Include:
> 1. **Campaign Tracker** — columns: Campaign Name (text), Client (text), Brand (text), Campaign Type (dropdown: Integrated, Digital Only, Social, TV/Video, Print/OOH, Experiential), Creative Director (people), Account Lead (people), Brief Date (date), Presentation Date (date), Launch Date (date), Status (status: Briefing, Concepting, Internal Review, Client Presentation, Revisions, Production, Adaptation, Final Approval, Live, Archived), Priority (status: Tier 1-Flagship, Tier 2-Standard, Tier 3-Maintenance), Budget (numbers with $), Timeline (timeline)
> 2. **Deliverables** (subitems of Campaign) — columns: Deliverable Name (text), Format (dropdown: TV :30, TV :15, Digital Banner Set, Social IG Feed, Social IG Story, Social TikTok, Social Facebook, YouTube Pre-Roll, OOH Billboard, OOH Transit, Print Full Page, Print Half Page, Email, Landing Page, Presentation Deck), Assigned Creative (people), Status (status: Not Started, In Progress, Internal Review, Client Review, Revisions, Final Art, Approved, Delivered), Due Date (date), Review Round (numbers), File Link (link), Notes (long text)
> 3. **Creative Briefs** — columns: Campaign (connect to Campaign Tracker), Client Objective (long text), Target Audience (long text), Key Message (long text), Mandatory Elements (long text), Brand Guidelines Link (link), Tone & Voice (dropdown: Playful, Premium, Bold, Warm, Professional, Edgy, Minimalist), Deliverables Required (long text), Budget (numbers with $), Timeline (timeline), Brief Status (status: Draft, Complete, Approved), Submitted By (people), Approved By (people)
>
> Automations: When Creative Brief Status changes to 'Approved', create Campaign Tracker item and auto-generate Deliverable subitems from the deliverables list. When Deliverable Status changes to 'Internal Review', notify Creative Director. When all Deliverables are 'Approved', change Campaign Status to 'Live'. When any Deliverable is past Due Date and not 'Approved', alert Account Lead and CD. Dashboard with campaign pipeline by status, deliverable completion rates, workload by creative, and deadline risk view."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CampaignPulse
**Agent Purpose:** Orchestrate campaign production workflow, track deliverables across formats, and surface bottlenecks before they cause deadline misses.

**Triggers:**
- New creative brief approved
- Deliverable status changes
- Deadline approaching (5 days, 2 days, same day)
- Daily campaign health check (9 AM)
- Review round exceeds 3 (potential scope creep)

**Actions:**
- Auto-generate deliverable list from brief requirements with format-appropriate deadlines
- Assign creatives based on skill match and current workload
- Track review cycle count and flag excessive revisions
- Send daily production digest to CD and account lead with at-risk items
- Identify workflow bottlenecks (e.g., "3 campaigns stuck in Internal Review — CD bandwidth issue")
- Generate weekly capacity report showing creative workload distribution

**Data Required:**
- Creative brief details and deliverable requirements
- Creative team skills and current assignments
- Historical production timelines by deliverable type
- Review and approval SLA targets
- Client feedback history

**Autonomy Level:** Human-in-the-Loop
Autonomous for scheduling, tracking, and alerting. Creative assignments and priority calls require CD approval.

**Example Interaction:**
> A new Nike holiday campaign brief is approved with 47 deliverables across 12 formats. CampaignPulse auto-generates the deliverable list with format-specific deadlines (video assets get 2 extra weeks vs. static), assigns creatives based on the Nike team roster and current workload: "Assigned: Sarah (art direction — 62% utilized, worked on last 3 Nike campaigns), Marcus (copy — 71% utilized, Nike brand voice expert), Jin (motion — 45% utilized, available for video). Potential issue: Deliverable volume exceeds team capacity by ~30 hours in weeks 3-4. Recommend: (1) Pull in freelance production artist for banner adaptations, or (2) shift 3 social deliverables to week 5 if launch date permits. Account lead notified for client timeline discussion."

---

### Use Case 2: Creative Review, Feedback & Approval Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Creative review and approval is where campaigns go to die slowly. A single piece of creative might need approval from: the creative director (internal), the account director (internal), the client brand manager, the client marketing director, and sometimes the client's legal team. Feedback comes through every possible channel — email threads, Slack messages, commented PDFs, phone calls, hallway conversations, and Post-it notes on printouts. Creative teams spend hours consolidating contradictory feedback from multiple stakeholders. Version control is a constant problem: "Did you see v7 or v7_final or v7_final_FINAL_revised?" And because there's no structured approval trail, approved work sometimes gets re-opened ("I know we approved that but my boss now wants to change the headline").

#### The Solution
monday.com Work Management for centralized creative review and approval. Every asset has a defined approval workflow with sequential or parallel review stages. Feedback is captured in-context (comments on the item, not scattered across channels). Version history is tracked automatically. Approval is recorded with timestamp and approver — creating an audit trail that prevents re-opening closed decisions. Client-facing approval views give clients a clean interface without exposing internal workflow.

#### The Outcome
- Review cycle time reduced by 40% through structured feedback consolidation
- Zero version confusion (single source of truth for current version)
- Approval audit trail eliminates "we never approved that" disputes
- Creative team saves 5–8 hours per week previously spent chasing and consolidating feedback
- Client satisfaction increases through professional review experience

#### Discovery Questions
1. "How do creative teams currently receive feedback — and how much time do they spend consolidating input from multiple sources?"
2. "What's your version control situation — honestly — and how often does the wrong version get sent to a client or published?"
3. "Has a client ever disputed that they approved a piece of creative — and could you prove the approval?"
4. "How many approval stages does a typical campaign asset go through, and where do the biggest delays occur?"

#### Industry Context
Creative approval in advertising involves deeply subjective judgment. "I'll know it when I see it" is a real client feedback pattern. The challenge is creating structure without stifling the creative process. Agencies have tried dedicated proofing tools (Ziflow, Frame.io for video, Filestage) but these create yet another silo. The ideal solution integrates proofing into the production workflow so feedback, approval, and status tracking happen in one place. Client-side approval is particularly challenging because agency tools must be intuitive enough for non-technical marketing managers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Creative Review & Approval workspace. Include:
> 1. **Review Queue** — columns: Asset Name (text), Campaign (text), Client (text), Asset Type (dropdown: Key Visual, Video, Digital Banner, Social Post, Copy Deck, Presentation, Print Layout), Current Version (numbers), File/Preview Link (link), Creator (people), Review Stage (status: Internal CD Review, Internal Account Review, Client Review Round 1, Client Review Round 2, Client Review Round 3, Legal Review, Final Approval), Reviewer (people), Submitted for Review (date), Review Deadline (date), Days in Review (formula), Feedback Status (status: Awaiting Feedback, Feedback Received, Revisions In Progress, No Changes Needed), Approval Status (status: Pending, Approved, Approved with Changes, Rejected, Revisions Required)
> 2. **Feedback Log** (subitems) — columns: Feedback From (people), Feedback Date (date), Feedback Type (dropdown: Copy Change, Visual Change, Strategic Direction, Technical Fix, Legal Requirement, Client Preference), Feedback Detail (long text), Priority (status: Must Change, Should Change, Nice to Have, FYI), Addressed (checkbox), Addressed In Version (numbers)
> 3. **Approval Records** — columns: Asset (connect to Review Queue), Approver (people), Approval Stage (dropdown), Decision (dropdown: Approved, Approved with Conditions, Revisions Required, Rejected), Date (date), Conditions/Notes (long text), Digital Signature (checkbox)
>
> Automations: When asset is submitted for review, notify Reviewer with deadline. When Review Deadline passes without approval, escalate to CD and Account Director. When all feedback items are 'Addressed', auto-advance to next review stage. When Approval Status is 'Approved' at final stage, notify production team to begin adaptation. Dashboard with review pipeline, average review turnaround by stage, feedback volume trends, and bottleneck analysis."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FeedbackFusion
**Agent Purpose:** Consolidate, organize, and prioritize creative feedback from multiple stakeholders into actionable revision lists.

**Triggers:**
- Feedback submitted on any review item (comment, subitem, or update)
- Review deadline approaching with no feedback received
- Multiple conflicting feedback items detected
- Asset moved to "Revisions In Progress"

**Actions:**
- Consolidate feedback from multiple reviewers into a single prioritized revision list
- Detect and flag contradictory feedback (e.g., "make the logo bigger" vs. "reduce brand prominence")
- Categorize feedback by type and priority automatically
- Generate a revision brief for the creative team with clear action items
- Track which feedback has been addressed in which version
- Alert when revision rounds exceed typical thresholds (indicating brief or direction issues)

**Data Required:**
- All feedback submissions across channels
- Historical feedback patterns by client (what they typically focus on)
- Brand guidelines for reference
- Review stage workflow and approver chain

**Autonomy Level:** Fully Autonomous
Feedback consolidation and organization is automated. Flags conflicts for CD resolution. Does not make creative judgments.

**Example Interaction:**
> The Toyota campaign key visual is in Client Review Round 2. Three stakeholders provide feedback: Brand Manager says "Love the direction, just make the car color match the new Lunar Blue — hex #1B3A5C." Marketing Director says "The headline needs more urgency — something about limited time." Legal says "Add required EPA fuel economy disclosure — minimum 6pt font." FeedbackFusion consolidates: "Toyota KV v3 — Revision Brief: 3 items from 3 reviewers. (1) MUST CHANGE [Legal]: Add EPA fuel economy disclosure, min 6pt. (2) MUST CHANGE [Brand]: Update car color to Lunar Blue #1B3A5C. (3) SHOULD CHANGE [Marketing]: Revise headline for urgency — current: 'The All-New Camry.' Suggested direction: time-limited language. Note: No conflicting feedback this round. Items 1-2 are mechanical; item 3 requires creative judgment — routing to copywriter with CD awareness."

---

### Use Case 3: Creative Resource Management & Workload Balancing

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Creative departments are chronically over-assigned. An art director might be staffed on 6 accounts simultaneously, with each account team assuming they have full access. There's no visibility into actual workload — resource managers (if the agency even has one) use spreadsheets or whiteboards to track assignments, but these are always outdated. The result: top talent gets overloaded while junior creatives are underutilized, deadlines are missed because nobody realized the designer was triple-booked, and creative quality suffers from context-switching across too many projects. Burnout is the industry's dirty secret — creative department turnover at agencies averages 30%+ annually.

#### The Solution
monday.com Work Management for creative resource planning and workload management. Every creative team member has a capacity profile. Project assignments are tracked against capacity, with visual workload views showing who's over/under-utilized. Resource requests from account teams go through a structured intake process. Automations flag overallocation and suggest rebalancing.

#### The Outcome
- Creative utilization balanced within 10% of target (vs. wild variance currently)
- Burnout reduction: no creative exceeds 110% capacity for more than 1 week without escalation
- 20% increase in effective creative output through better workload distribution
- Junior creative development improves through intentional assignment to stretch projects
- Freelancer needs identified 2 weeks in advance (vs. emergency staffing)

#### Discovery Questions
1. "How do you currently track what each creative is working on — and can you tell me right now who's overloaded and who has capacity?"
2. "How do account teams request creative resources, and how often do competing requests create conflicts?"
3. "What's your creative department turnover rate, and how much of that do you attribute to workload issues?"
4. "How do you decide when to bring in freelancers — is it proactive or reactive?"
5. "How do you ensure junior creatives get development opportunities alongside production work?"

#### Industry Context
Resource management in creative agencies is fundamentally different from other industries because creative work requires "focus time" — the deep, uninterrupted thinking time that produces great ideas. A creative with 8 hours of assignments across 4 clients doesn't have 8 productive hours — they have maybe 5 after accounting for context-switching costs. Industry best practice is to cap creative utilization at 75–80% to allow for ideation time, internal projects, and the inevitable fire drill. The concept of "billable utilization" (time billed to clients) versus "productive utilization" (time doing meaningful work) is a constant tension. Agency resource management tools like Teamwork, Float, and Resource Guru have emerged but rarely integrate with the creative production workflow.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Creative Resource Management workspace. Include:
> 1. **Creative Team Roster** — columns: Name (people), Role (dropdown: ECD, GCD, CD, ACD, Senior Art Director, Art Director, Junior Art Director, Senior Copywriter, Copywriter, Junior Copywriter, Senior Designer, Designer, Motion Designer, Video Editor, Retoucher, Production Artist, UX/UI Designer), Specialty (dropdown multi-select: Branding, Digital, Social, Video/Motion, Print, Experiential, UX, Packaging), Weekly Capacity Hours (numbers, default 40), Target Utilization % (numbers, default 80%), Current Utilization % (formula from assignments), Status (status: Available, Fully Booked, Overloaded, On Leave, Freelance), Office (dropdown)
> 2. **Resource Assignments** — columns: Creative (connect to Team Roster), Campaign/Project (text), Client (text), Role on Project (text), Hours per Week (numbers), Start Date (date), End Date (date), Priority (status: Primary, Secondary, Support), Assigned By (people), Timeline (timeline)
> 3. **Resource Requests** — columns: Request Title (text), Client (text), Campaign (text), Skill Needed (dropdown), Seniority (dropdown: Junior, Mid, Senior, Director), Hours Needed (numbers), Start Date (date), Duration (dropdown: 1 Week, 2 Weeks, 1 Month, 2-3 Months, Ongoing), Requestor (people), Priority (status: Critical, High, Normal), Status (status: Submitted, Reviewing, Assigned, Waitlisted, Declined, Freelance Needed), Assigned Creative (connect to Team Roster), Notes (long text)
>
> Automations: When Creative Current Utilization exceeds 100%, change status to 'Overloaded' and alert resource manager. When Resource Request is 'Critical', notify CD immediately. When resource has no assignments ending in next 2 weeks, flag as 'Upcoming Availability'. Create workload view: Timeline view showing all assignments by creative, with color-coded utilization. Dashboard with team utilization heat map, overloaded/underutilized creatives, upcoming capacity gaps, and freelancer forecast."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CreativeCapacity
**Agent Purpose:** Optimize creative team utilization by matching resource requests to available talent and proactively identifying capacity issues.

**Triggers:**
- New resource request submitted
- Assignment start/end dates changing
- Weekly capacity planning (Friday afternoon)
- Creative utilization exceeds threshold (100%)
- Creative leave request approved

**Actions:**
- Match resource requests against available creatives (skill, seniority, current utilization)
- Generate weekly capacity forecast (2-week and 4-week lookahead)
- Identify overloaded creatives and suggest rebalancing options
- Forecast freelancer needs based on upcoming demand vs. capacity
- Track utilization trends and flag creatives at burnout risk (>100% for 3+ consecutive weeks)
- Recommend junior creative stretch assignments when appropriate projects arise

**Data Required:**
- Team roster with skills and capacity
- Current and planned assignments
- Resource request pipeline
- Historical utilization data
- Freelancer database for overflow planning
- Leave calendar

**Autonomy Level:** Human-in-the-Loop
Autonomous for analysis and recommendations. Resource assignments and priority decisions require CD or resource manager approval.

**Example Interaction:**
> Friday capacity report: "Creative Team Capacity — Week of Feb 24. 🔴 Overloaded (3): Sarah (Art Director, 124% — Nike + Samsung + Coca-Cola overlap), Marcus (Copywriter, 115% — 4 active briefs), Aiko (Motion Designer, 108% — two video deadlines same week). 🟡 At Capacity (8): [list]. 🟢 Available (4): Tom (Jr. Art Director, 55%), Lisa (Designer, 60%), Raj (Jr. Copywriter, 45%), Mika (Production Artist, 40%). Recommendations: (1) Move Samsung banner adaptations from Sarah to Tom (junior stretch opportunity, Sarah reviews). Saves Sarah 12 hours. (2) Delay Coca-Cola social brief by 3 days to reduce Marcus's week peak. (3) Aiko's overload requires freelance motion support — recommend booking Jordan (freelance, $650/day, available). Freelancer forecast: 2 additional freelance weeks needed in March based on pipeline. Submit staffing request?"

---

### Use Case 4: Digital Asset Management & Brand Asset Library

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Agency creative teams are drowning in files. A single campaign generates hundreds of assets: source files (PSD, AI, INDD, AE, Premiere), exports (JPG, PNG, MP4, GIF), client logos (multiple versions), photography (raw and retouched), stock assets (licensed with specific usage terms), and final deliverables. These live across Google Drive, Dropbox, local drives, email attachments, and agency servers. Finding the right file — the correct version of the client logo with the right background color for digital use — can take 30 minutes. Worse, creatives recreate assets that already exist because they can't find them. Stock photo licenses expire without anyone tracking them, creating legal exposure. And when a creative leaves the agency, their locally stored files often go with them.

#### The Solution
monday.com Work Management as the creative asset orchestration layer, connecting to existing storage (Google Drive, Dropbox, DAM systems) while providing searchable metadata, version tracking, and license management. Each asset has structured metadata: client, campaign, format, usage rights, license expiry, and source file location. Automations alert when licenses expire and when assets need refreshing.

#### The Outcome
- Asset search time reduced from 30 minutes to 2 minutes
- Zero recreated assets (everything findable through structured search)
- Complete license compliance (no expired stock used in live campaigns)
- Creative onboarding time cut in half (new hires can self-serve brand assets)
- Institutional creative knowledge preserved when team members leave

#### Discovery Questions
1. "If I needed the latest version of [client] logo, approved for digital use, with transparent background — how long would it take you to find it?"
2. "How do you track stock photo and music licenses — and are you confident every licensed asset in live campaigns has current rights?"
3. "When a creative leaves the agency, what happens to the files on their local machine?"
4. "How much time do you estimate creatives spend looking for existing assets versus creating new work?"

#### Industry Context
Digital Asset Management (DAM) is a $5B+ market, with agencies using tools like Bynder, Brandfolder, Canto, and MediaValet. But DAM adoption at agencies is often partial — the system exists but nobody uses it consistently because it's disconnected from the production workflow. The key insight: asset management must be integrated into how creatives already work, not an additional step. Brand portals — client-facing asset libraries — are increasingly expected as part of agency service, creating both an asset management need and a revenue opportunity.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Creative Asset Library workspace. Include:
> 1. **Asset Registry** — columns: Asset Name (text), Client (text), Campaign (text), Asset Type (dropdown: Logo, Photography, Illustration, Video, Motion Graphics, Icon Set, Typography, Template, Brand Guidelines, Stock Asset, Audio/Music), Format (dropdown: PSD, AI, INDD, FIGMA, AE, PRPROJ, JPG, PNG, SVG, MP4, MOV, GIF, WAV, MP3, PDF), File Link (link), Current Version (numbers), Created By (people), Creation Date (date), Last Updated (date), Usage Rights (dropdown: Unlimited, Client Campaign Only, Time-Limited, Territory-Limited, Single Use), License Expiry (date), Tags (text), Status (status: Current, Archived, Expired Rights, Needs Update)
> 2. **Brand Asset Kits** — columns: Client (text), Brand (text), Kit Name (text), Kit Contents (long text), Primary Logo (link), Secondary Logo (link), Color Palette (text), Typography (text), Brand Guidelines (link), Last Updated (date), Kit Owner (people), Status (status: Current, Needs Update, Under Revision)
> 3. **License Tracker** — columns: Asset (connect to Asset Registry), License Type (dropdown: Royalty-Free, Rights-Managed, Editorial Only, Creative Commons, Custom License, Music Sync, Talent Release), Source (dropdown: Getty, Shutterstock, Adobe Stock, iStock, Unsplash, Custom Photography, Music Library, Direct License), License Number (text), Start Date (date), Expiry Date (date), Usage Scope (long text), Cost (numbers with $), Renewal Required (checkbox), Status (status: Active, Expiring Soon, Expired, Renewed)
>
> Automations: When License Expiry is 30 days away, notify creative team and account manager. When License Status is 'Expired', change Asset Status to 'Expired Rights' and send alert. When new campaign is created, auto-link relevant Brand Asset Kit. Dashboard with asset library overview, expiring licenses, brand kit status, and most-used assets."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AssetKeeper
**Agent Purpose:** Maintain the creative asset library, track licenses, and ensure creatives always have access to current, properly licensed assets.

**Triggers:**
- New asset uploaded or registered
- License expiry approaching (60, 30, 14 days)
- New campaign created (auto-assemble relevant assets)
- Quarterly asset library audit schedule
- Creative searches for an asset (manual query)

**Actions:**
- Auto-tag new assets with metadata based on file name, client folder, and content analysis
- Monitor license expirations and send renewal reminders
- Flag assets in live campaigns with expiring licenses
- Generate brand asset kits for new campaigns (assemble logos, guidelines, templates)
- Identify duplicate assets and recommend consolidation
- Produce quarterly asset library health report (total assets, license compliance, usage patterns)

**Data Required:**
- Asset file metadata and storage locations
- License agreements and terms
- Client brand guidelines
- Campaign asset usage data
- Stock photo/music library account information

**Autonomy Level:** Fully Autonomous
Asset management, tagging, and monitoring run automatically. License renewal decisions and brand kit updates require creative team approval.

**Example Interaction:**
> AssetKeeper's monthly license alert: "⚠️ 7 licenses expiring in next 30 days. CRITICAL (in live campaigns): (1) Getty Image #1284759 (hero photography, Samsung Galaxy campaign) — expires Feb 28. Used in: 12 active digital banners, 3 social posts. Estimated renewal: $2,400 for 1-year digital extension. (2) Musicbed Track 'Velocity' (Nike video campaign) — sync license expires March 5. Used in: YouTube pre-roll (currently running). Renewal: $3,800. LOW RISK (not in active campaigns): 5 stock images from past campaigns — recommend archive, not renewal (saves $1,200). Action needed: Samsung and Nike renewals require immediate attention to avoid campaign disruption. Renewal requests created and assigned to respective account teams."

---

### Use Case 5: Creative Brief Management & Strategy-to-Creative Handoff

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The creative brief is the most important document in advertising — and it's consistently done poorly. A survey by the Association of National Advertisers found that only 36% of creatives feel they receive "excellent" briefs. Common problems: briefs arrive incomplete (missing target audience data, competitive context, or mandatories), briefs change after work has started (scope creep's origin story), multiple stakeholders contribute conflicting inputs, and there's no feedback loop on brief quality. Bad briefs waste creative time — teams start work, hit a wall when they realize the brief is ambiguous, and either guess (risking rework) or delay (missing deadlines) while they chase clarification. The handoff from strategy/account to creative is where campaigns lose their first week.

#### The Solution
monday.com Work Management for structured creative brief intake and management. Standardized brief templates ensure completeness, with required fields that can't be submitted blank. Brief approval workflows ensure strategy and account alignment before creative work begins. Briefs are versioned and change-controlled — any modification after approval triggers a change request with impact assessment. A brief quality feedback loop lets creative teams rate briefs, driving improvement over time.

#### The Outcome
- 95%+ brief completeness at submission (vs. ~60% currently)
- Zero "surprise" brief changes — all modifications tracked with impact assessment
- Creative kickoff happens 3 days faster (no more chasing missing information)
- Brief quality scores improve 30%+ through feedback loop
- Strategy-to-creative handoff becomes a structured, reliable process

#### Discovery Questions
1. "What percentage of creative briefs arrive with everything the team needs to start work — honestly?"
2. "How often do briefs change after creative work has started, and what's the impact when that happens?"
3. "Is there a feedback mechanism where creative teams can flag brief quality issues back to strategy and account?"
4. "How do you handle conflicting inputs from multiple stakeholders during the briefing process?"

#### Industry Context
The creative brief has been advertising's most discussed and least solved problem for decades. Agency models vary: some have dedicated strategic planners who write briefs, others rely on account managers, and some have the creative team write their own briefs. The best practice is a structured brief template with mandatory fields: business objective, target audience, key insight, single-minded proposition, mandatories, tone, and deliverables. The IPA (Institute of Practitioners in Advertising) has published extensive research showing that brief quality is the #1 predictor of campaign effectiveness.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Creative Brief Management workspace. Include:
> 1. **Brief Intake** — columns: Brief Title (text), Client (text), Brand (text), Brief Author (people), Brief Type (dropdown: Campaign Brief, Content Brief, Adaptation Brief, Reactive Brief, Pitch Brief), Business Objective (long text), Target Audience (long text), Key Insight (long text), Single-Minded Proposition (long text), Mandatory Elements (long text), Tone & Voice (dropdown), Deliverables Required (long text), Budget (numbers with $), Timeline (timeline), Reference/Inspiration Links (long text), Competitive Context (long text), Success Metrics (long text), Brief Status (status: Draft, Strategy Review, Account Approved, CD Accepted, In Progress, Complete), Completeness Score (formula: count of filled fields / total fields × 100)
> 2. **Brief Change Requests** — columns: Original Brief (connect to Brief Intake), Change Description (long text), Reason for Change (dropdown: Client Direction Change, New Information, Scope Expansion, Scope Reduction, Timeline Change, Budget Change), Requested By (people), Impact Assessment (long text), Impact on Timeline (dropdown: No Impact, 1-3 Days, 1 Week, 2+ Weeks), Impact on Budget (dropdown: No Impact, Minor Increase, Significant Increase, Decrease), Status (status: Requested, Under Review, Approved, Rejected), Approved By (people)
> 3. **Brief Quality Tracker** — columns: Brief (connect to Brief Intake), Rated By (people), Clarity Score (numbers 1-5), Completeness Score (numbers 1-5), Inspiration Score (numbers 1-5), Actionability Score (numbers 1-5), Overall Score (formula: average), Comments (long text), Common Issues (dropdown multi-select: Vague Objective, Missing Audience Data, No Competitive Context, Conflicting Mandatories, Unrealistic Timeline, Unclear Success Metrics)
>
> Automations: When Brief Completeness Score is below 80%, prevent status change to 'CD Accepted' and notify author of missing fields. When Brief Change Request is submitted after 'In Progress', notify CD with impact assessment. Quarterly brief quality report auto-generated from tracker. Dashboard with brief pipeline, average quality scores by author, common issues trends, and brief-to-creative turnaround."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BriefGenius
**Agent Purpose:** Ensure creative briefs are complete, aligned, and actionable before creative work begins — and track brief quality for continuous improvement.

**Triggers:**
- New brief submitted for review
- Brief completeness below threshold
- Brief change request submitted after creative work starts
- Monthly brief quality analysis schedule

**Actions:**
- Validate brief completeness and flag missing required fields
- Cross-reference brief against brand guidelines for consistency
- Identify vague language and suggest more specific alternatives
- Assess change request impact on timeline and budget
- Generate monthly brief quality report with trends and recommendations
- Recommend brief improvements based on historical quality scores

**Data Required:**
- Brief template requirements
- Brand guidelines for each client
- Historical brief quality scores
- Creative team feedback
- Campaign timeline and resource data

**Autonomy Level:** Human-in-the-Loop
Autonomous for validation, flagging, and reporting. Brief approval and change request decisions require human judgment.

**Example Interaction:**
> An account manager submits a brief for a new Spotify campaign. BriefGenius reviews: "Brief Completeness: 72% (below 80% threshold). Missing fields: (1) Target Audience — says 'millennials' without psychographic detail or behavioral data. Suggestion: 'Music-streaming millennials aged 25-34, urban, who discover new artists weekly and share playlists socially.' (2) Competitive Context — empty. Spotify competes with Apple Music, YouTube Music, Amazon Music, and Tidal. At minimum, include how the campaign differentiates. (3) Success Metrics — says 'increase brand awareness.' Suggestion: specify measurement (brand lift study target, social engagement benchmarks, streaming metrics). Brief cannot advance to CD until these fields are complete. Notification sent to account manager with specific suggestions."

---

### Use Case 6: AI-Assisted Creative Production & Asset Versioning

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
The most tedious work in creative departments is asset adaptation and versioning — taking an approved hero concept and producing dozens of format variations (15 banner sizes, 6 social formats, multiple language versions). This work requires skill but minimal creativity, and it consumes 30–40% of production artist time. Meanwhile, the ideation process itself is becoming AI-augmented but unstructured: creatives use Midjourney, DALL-E, and ChatGPT informally for mood boards, concept exploration, and copy variations, but there's no process to track AI usage, manage prompts, or ensure compliance with client AI policies (some clients prohibit AI-generated content entirely).

#### The Solution
monday.com Work Management for AI-assisted creative workflow management. Track AI tool usage by project and client (respecting client AI policies). Manage the versioning pipeline from hero to adapted formats with clear task assignment and status tracking. Store and share effective AI prompts as a team knowledge base. Automate the versioning checklist (specs, brand compliance, format validation) to ensure consistency.

#### The Outcome
- Asset versioning time reduced by 50% through structured workflow and AI assistance tracking
- 100% compliance with client AI usage policies (tracked and enforced)
- Shared AI prompt library accelerates ideation across the team
- Quality consistency across all format variations through automated checklist

#### Discovery Questions
1. "How much of your creative team's time goes to asset adaptation and versioning versus original creative work?"
2. "How are your creatives currently using AI tools — and do you have visibility into which projects use AI-generated content?"
3. "Do any of your clients have policies around AI usage in their creative work, and how do you track compliance?"
4. "If a creative discovers a great AI prompt that produces amazing results, how do they share that with the team?"

#### Industry Context
The advertising industry is split on generative AI. Some agencies (like WPP) have embraced it fully, building proprietary AI tools and training teams. Others are cautious, driven by client restrictions and copyright concerns. Key legal issues: AI-generated images may not be copyrightable (per US Copyright Office guidance); AI training data may include copyrighted works (pending litigation: Getty v. Stability AI); and some clients explicitly prohibit AI-generated content in their brand guidelines. The pragmatic middle ground: AI for ideation and comps (not final delivery) and AI for production efficiency (versioning, adaptation) rather than original creation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an AI-Assisted Creative & Versioning workspace. Include:
> 1. **Versioning Pipeline** — columns: Hero Asset (text), Campaign (text), Client (text), Total Versions Needed (numbers), Versions Completed (numbers), Completion % (formula), Assigned Production Artist (people), Status (status: Pending Hero Approval, Versioning In Progress, QC Review, Complete), Due Date (date), Hero File Link (link), Version Specs Sheet (link)
> 2. **Version Checklist** (subitems) — columns: Format/Size (text), Dimensions (text), Platform (dropdown: Google Display, Meta, Instagram, TikTok, LinkedIn, Twitter/X, YouTube, Email, OOH, Print), Status (status: Not Started, In Progress, QC Pass, QC Fail, Delivered), Assigned (people), File Link (link), Brand Compliance (checkbox), Spec Compliance (checkbox), Notes (long text)
> 3. **AI Usage Tracker** — columns: Project (text), Client (text), AI Tool Used (dropdown: Midjourney, DALL-E, Adobe Firefly, Runway, ChatGPT, Claude, Stable Diffusion, Other), Usage Type (dropdown: Ideation/Moodboard, Comp/Concept, Copy Exploration, Image Generation, Video/Motion, Production Assist), Client AI Policy (status: AI Permitted, AI Restricted, AI Prohibited, No Policy), Output Used in Final (dropdown: Yes-Disclosed, Yes-Modified, No-Ideation Only), Prompt (long text), Creative (people), Date (date), Notes (long text)
>
> Automations: When Client AI Policy is 'AI Prohibited' and Output Used in Final is 'Yes', immediately alert legal and CD. When all Version Checklist subitems are 'QC Pass', update pipeline status to 'Complete'. Dashboard with versioning progress by campaign, AI usage by tool and type, client AI policy compliance, and production capacity."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VersionEngine
**Agent Purpose:** Streamline asset versioning workflows and ensure AI usage compliance across all creative projects.

**Triggers:**
- Hero asset approved (ready for versioning)
- AI tool usage logged on any project
- Client AI policy violation detected
- Version QC failure
- Weekly versioning capacity report

**Actions:**
- Auto-generate version checklist from campaign format requirements
- Track versioning progress and flag items falling behind schedule
- Monitor AI usage against client policies and alert on violations
- Compile AI usage report for client transparency (when required)
- Build team AI prompt library from logged successful prompts
- Generate weekly production capacity report (versioning hours remaining vs. available)

**Data Required:**
- Campaign format requirements and specs
- Client AI usage policies
- AI tool usage logs
- Production team capacity
- Brand guidelines for QC validation

**Autonomy Level:** Escalation-Based
Autonomous for workflow management and compliance monitoring. AI policy violations escalated immediately to CD and legal. QC decisions require human review.

**Example Interaction:**
> The Coca-Cola summer campaign hero visual is approved. VersionEngine generates the versioning checklist: 42 formats needed (15 digital banners, 8 social formats, 6 email sizes, 5 OOH sizes, 4 print sizes, 4 presentation formats). It assigns production artists based on capacity: "Maria: 18 formats (banner specialist, 65% utilized). Tom: 14 formats (social expert, 55% utilized). Overflow: 10 formats — recommend freelance production artist for 2 days." During production, it detects that Tom used Adobe Firefly to generate background extension for a wide-format OOH adaptation. It checks the Coca-Cola AI policy: "ALERT: Coca-Cola policy restricts AI-generated content in final deliverables. Tom's Firefly usage on CocaCola_OOH_48sheet is flagged. Routing to CD for review — options: (1) manually recreate the background extension, (2) request client waiver for AI-assisted production (not generation)."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ECD (Executive Creative Director) | Senior creative leader overseeing multiple accounts and teams |
| CCO (Chief Creative Officer) | Highest creative role at an agency, sets creative vision |
| ACD (Associate Creative Director) | Mid-senior creative leader, typically manages a team on specific accounts |
| Art Director | Visual creative — responsible for the look, feel, and visual storytelling |
| Copywriter | Written creative — responsible for headlines, body copy, scripts, and messaging |
| Comp (Comprehensive Layout) | A realistic mockup of how the final piece will look |
| Hero Asset | The primary creative execution from which other formats are adapted |
| Versioning/Adaptation | Creating format-specific variations of a hero asset |
| Trafficking | The process of delivering final creative files to media platforms or publishers |
| Deck | Presentation document (usually for client creative presentations) |
| Tissue Session | Early-stage creative review where rough concepts are shared for direction (before polishing) |
| Round (Review Round) | One cycle of creative submission → feedback → revision |
| Kill Fee | Payment to talent or vendors when work is cancelled after engagement |
| Spec Work | Creative work done without guaranteed compensation (e.g., during a pitch) |
| Retouching | Post-production image editing (color correction, compositing, skin retouching) |
| DAM (Digital Asset Management) | System for storing, organizing, and retrieving creative files |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Creative Officer (CCO) | Agency creative vision, quality standards, creative culture | Decision-maker |
| Executive Creative Director (ECD) | Creative direction for assigned accounts, team leadership | Decision-maker |
| Group Creative Director (GCD) | Leads creative teams on specific account groups | Decision-maker/Influencer |
| Associate Creative Director (ACD) | Hands-on creative leadership, mentors junior team | Influencer |
| Head of Creative Operations / Traffic | Production workflow, resource management, timeline enforcement | Influencer |
| Creative Producer | Production logistics, vendor management, budget tracking | User/Influencer |
| Studio Manager | Production artist team management, versioning workflow | User |
| Head of Design | Design system standards, brand consistency, design team development | Influencer |
| Director of Technology / Creative Technologist | AI tools, creative tech stack, innovation | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Account Management | Brief creation, client feedback relay, timeline management | Connected brief-to-delivery workflow eliminates handoff gaps |
| Strategy / Planning | Creative briefs, campaign strategy, audience insights | Strategy insights flow directly into brief templates and creative direction |
| Media | Format requirements, platform specs, delivery deadlines | Media specs auto-populate creative deliverable requirements |
| Production | Video shoots, photography, print production, vendor management | End-to-end production workflow from concept through final delivery |
| Legal | Creative clearance, IP, talent rights, claims substantiation | Integrated legal review within the creative approval workflow |
| Technology / Development | Interactive creative, website builds, app experiences | Dev handoff for digital creative with specs and assets |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Asana | Work management for creative teams | monday.com matches creative workflow capability and adds CRM, Service, and Dev for cross-agency use — one platform vs. Asana for creative + other tools for everything else |
| Wrike | Creative project management with proofing | monday.com offers equal creative workflow plus broader agency use cases — avoids creative team using one tool while rest of agency uses another |
| Notion | Flexible workspace for creative briefs and docs | monday.com provides structured workflow automation that Notion's database approach can't match — automations, SLAs, and real-time dashboards |
| Frame.io | Video review and collaboration | Specialized tool — monday.com integrates with Frame.io while providing the surrounding production workflow; eliminates silo between video review and project management |
| Ziflow / Filestage | Creative proofing and approval | Specialized proofing tools that create another silo — monday.com provides proofing context within the production workflow |
| Basecamp | Simple project management for small teams | monday.com scales to agency complexity while maintaining simplicity — Basecamp lacks the structure for multi-format campaign production |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "Creatives hate project management tools — they'll rebel" | "Creatives hate bad project management tools — ones that add work without removing pain. monday.com removes their pain: no more searching for files, no more 'where's my feedback?' emails, no more being triple-booked without anyone knowing. When the tool makes their life easier, creatives adopt it enthusiastically." |
| "Creative work can't be put into a linear workflow — it's not an assembly line" | "Totally agree — and monday.com isn't forcing creative work into a linear process. The ideation and creative thinking stay fluid. What gets structured is the operational wrapper: intake, routing, feedback consolidation, version tracking, and delivery. The creative magic happens inside that structure, not constrained by it." |
| "We already have Figma/Adobe CC/Frame.io — why add another tool?" | "Those are creation tools — they're where creative work gets made. monday.com is the orchestration layer — it manages which work gets made, by whom, by when, with what feedback, and through what approvals. It integrates with your creative tools; it doesn't replace them." |
| "Our CD manages everything in their head — it works fine" | "Until they're on vacation, or sick, or leave the agency. What's in one person's head is a single point of failure, not a system. monday.com captures that institutional knowledge so the team operates regardless of who's in the office." |
| "We tried a PM tool before and people stopped using it after 2 months" | "That usually happens when the tool adds administrative overhead without clear payoff. monday.com's automations do the admin work: statuses update from connected tools, notifications go out automatically, dashboards self-populate. When the tool runs itself, people keep using it." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for creative agency using monday.com for campaign production workflow]
- [Placeholder for agency that improved creative utilization with monday.com resource management]
- [Placeholder for agency managing multi-format asset production at scale with monday.com]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
