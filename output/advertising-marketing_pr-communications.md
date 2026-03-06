# Advertising & Marketing × PR & Communications Playbook

## Overview

PR & Communications departments within advertising and marketing companies occupy a dual role: they serve clients' external communications needs (earned media, crisis management, reputation building) while also managing the agency's own corporate communications and brand presence. In integrated agencies, PR teams work alongside creative, media, and digital departments to deliver holistic campaigns. In dedicated PR firms (Edelman, Weber Shandwick, BCW), PR *is* the core business.

The operational reality of PR in this industry is high-velocity, relationship-driven, and measurement-challenged. A mid-size PR agency manages 30-80 active client accounts simultaneously, each with ongoing media outreach programs, event calendars, spokesperson prep, and crisis readiness plans. Teams are typically organized by practice area (corporate, consumer, healthcare, technology, crisis) and client pod. The average PR account coordinator juggles 5-8 accounts, maintains relationships with 200+ media contacts, and pitches 15-30 stories per week.

Measurement has historically been PR's Achilles heel — the industry moved from AVE (Advertising Value Equivalency, now discredited) to the Barcelona Principles (outcomes-based measurement), but many teams still rely on clip counting and manual share-of-voice calculations. Regulatory considerations include FTC influencer disclosure rules, SEC Reg FD for public company clients, HIPAA for healthcare PR, and increasing state-level privacy laws affecting consumer communications.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | PR teams manage exponentially growing media landscapes (traditional + digital + social + podcasts + newsletters) with flat headcount. Need to monitor more, pitch more, measure more — without hiring more. |
| 2 | Replace or Radically Augment Headcount | High | Junior PR roles (media list building, clip monitoring, report compilation) are 70% manual tasks ripe for AI augmentation. |
| 3 | Consolidate Tech Stack with AI | Medium-High | PR teams typically use 5-8 separate tools (Cision, Meltwater, Muck Rack, CoverageBook, Excel, email, project management). |

## Prioritized Use Cases

---

### Use Case 1: Media Outreach & Pitch Tracking Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
PR account teams pitch dozens of stories per week across hundreds of journalist contacts. Pitches go out via personal email, with no centralized tracking of who was pitched, when, what angle, and the outcome. Two team members pitch the same journalist the same story. Follow-ups fall through the cracks. When a client asks "what outreach have you done this month?" the account lead spends hours reconstructing activity from email sent folders. Cision and Muck Rack track media contacts but don't manage the pitch workflow — they're databases, not pipelines.

#### The Solution
monday.com Work Management as a pitch pipeline with CRM-like functionality. Each pitch is an item flowing through stages (Draft → Approved → Sent → Follow-Up 1 → Follow-Up 2 → Placed/Passed/No Response). Connected boards link pitches to media contacts, client accounts, and coverage results. Automations schedule follow-ups and prevent duplicate outreach.

#### The Outcome
Increase pitch-to-placement conversion by 25% through systematic follow-up. Eliminate duplicate pitching. Generate instant client activity reports. Reduce weekly reporting prep from 3 hours to 15 minutes per account.

#### Discovery Questions
- How do you currently track which journalists have been pitched on a story, and what their response was?
- When two team members work the same client, how do you prevent duplicate pitches to the same outlet?
- How long does it take your team to compile a monthly media outreach report for a client?
- What's your pitch-to-placement ratio, and do you even have the data to calculate it?
- How do you decide when to stop following up with a journalist — gut feel or a systematic rule?

#### Industry Context
"Pitching" in PR means proactively contacting journalists, editors, producers, or influencers with story ideas on behalf of clients. A "pitch" can be an email, a phone call, a DM on Twitter/X, or increasingly a voice memo or video pitch. "Placement" means successfully getting a story published or aired. "Exclusives" are stories offered to one outlet first — managing exclusive windows is critical and errors destroy journalist relationships. The "media list" is the PR professional's most valuable asset — a curated database of contacts by beat, outlet, and relationship quality.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a media pitch tracking pipeline for a PR agency. Columns: Pitch Title (text), Client Account (connect board: Clients), Story Angle (long text), Target Journalist (text), Outlet (text), Media Tier (dropdown: Tier 1 National, Tier 2 Trade/Regional, Tier 3 Local/Blog, Tier 4 Digital/Podcast), Journalist Email (email), Pitch Status (status: Drafting, Internal Review, Approved, Sent, Follow-Up 1, Follow-Up 2, Placed, Passed, No Response, Killed), Pitch Date Sent (date), Follow-Up Due (date), Exclusive Offered (checkbox), Exclusive Window Expires (date), Pitched By (people), Coverage Link (link), Coverage Date (date), Sentiment (dropdown: Positive, Neutral, Mixed, Negative), Notes (long text). Automations: when Pitch Status changes to Sent, set Follow-Up Due to 3 business days later; when Follow-Up Due arrives and status is still Sent, change to Follow-Up 1 and notify Pitched By; when status is Follow-Up 2 for 5 days, change to No Response; when Exclusive Window Expires arrives, notify team 'Exclusive window closed — open for wide pitch.' Create Kanban view by Pitch Status, table view grouped by Client Account, and dashboard with: pitches sent this month by team member (bar chart), conversion rate by media tier (chart), pipeline by status (funnel), top performing story angles (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PitchFlow
**Agent Purpose:** Manage media pitch pipeline, automate follow-ups, prevent duplicate outreach, and provide real-time client reporting.

**Triggers:**
- New pitch item created
- Pitch status changes
- Follow-up due date arrives
- Journalist name entered that matches existing pitch in last 30 days (duplicate detection)
- Client requests activity report
- Weekly Monday morning digest schedule

**Actions:**
- Check for duplicate pitches (same journalist + same client within 30 days) and alert team
- Schedule and remind for follow-ups based on pitch stage
- Generate client activity reports: pitches sent, responses received, placements secured, pending follow-ups
- Track exclusive windows and alert when they expire
- Analyze pitch-to-placement ratios by journalist, outlet, and story angle to identify top-performing approaches
- Recommend optimal pitch timing based on historical response patterns per journalist

**Data Required:**
- Pitch tracking board
- Media contact database (connected board or Cision/Muck Rack integration)
- Client account board
- Historical pitch outcome data

**Autonomy Level:** Human-in-the-Loop
PitchFlow manages scheduling, reminders, and reporting autonomously. All outgoing pitches require human review and approval. Duplicate alerts are warnings, not blocks. Report generation is fully autonomous.

**Example Interaction:**
> It's Monday morning and PitchFlow generates the weekly digest for the "NovaTech" client account. "Last week: 12 pitches sent, 4 responses received (2 interested, 1 passed, 1 requesting more info), 1 placement confirmed (TechCrunch, publishing Wednesday). This week: 6 follow-ups due (3 today, 3 Thursday). Alert: Jamie pitched Sarah Chen at The Verge on the AI product launch — note that Marcus also has a pending pitch to Sarah for the CEO profile. Recommend consolidating into one touchpoint to avoid journalist fatigue." The account lead reviews and asks Marcus to hold his pitch until after the product launch story runs.

---

### Use Case 2: Earned Media Coverage Monitoring & Reporting

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
PR teams spend 2-4 hours daily monitoring media coverage across outlets for client mentions, competitor activity, and industry trends. Junior staff compile "clip reports" — screenshots, links, and summaries of coverage — into PowerPoint decks or PDFs for client distribution. Monthly and quarterly reports require calculating share of voice, sentiment analysis, reach estimates, and message pull-through (did the coverage include key messages?). This reporting is manual, inconsistent across accounts, and takes senior staff away from strategic work.

#### The Solution
monday.com as a coverage tracking hub where clips are logged with structured metadata (outlet, journalist, sentiment, key messages, reach). Connected to pitch tracking to close the loop on outreach effectiveness. Automated dashboards replace manual report compilation. Integration with monitoring tools (Meltwater, Cision) for clip ingestion.

#### The Outcome
Reduce daily monitoring compilation from 2 hours to 20 minutes. Eliminate monthly report creation (replaced by always-on dashboards). Provide clients with real-time coverage visibility. Free senior staff from reporting to focus on strategy.

#### Discovery Questions
- How many hours per week does your team spend compiling media coverage reports across all clients?
- Do your clients get real-time visibility into their coverage, or do they wait for weekly/monthly reports?
- How do you currently measure message pull-through — does coverage include the key messages you're trying to land?
- Can you show me how your share-of-voice calculation works today? How long does it take?
- What tools do you use for media monitoring, and how does that data flow into your reporting?

#### Industry Context
"Clips" or "clippings" are individual pieces of media coverage. "Share of voice" (SOV) measures a client's media presence relative to competitors — calculated by volume, reach, or prominence. "Message pull-through" assesses whether coverage includes the client's key talking points. "Barcelona Principles 3.0" (2020 update from AMEC) are the industry standard for measurement, emphasizing outcomes over outputs. "AVE" (Advertising Value Equivalency) — calculating what coverage would cost as advertising — is considered discredited but some clients still request it. "Impressions" or "reach" estimates the potential audience of a placement based on outlet circulation/traffic.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a media coverage tracking and reporting system for a PR agency. Board: Coverage Tracker. Columns: Headline (text), Client (connect board: Clients), Outlet Name (text), Media Type (dropdown: Print, Online, Broadcast TV, Broadcast Radio, Podcast, Social/Influencer, Newsletter), Outlet Tier (dropdown: Tier 1, Tier 2, Tier 3, Tier 4), Journalist (text), Publication Date (date), Coverage Link (link), Screenshot/Clip File (file), Sentiment (status: Positive, Neutral, Mixed, Negative), Key Message 1 Hit (checkbox), Key Message 2 Hit (checkbox), Key Message 3 Hit (checkbox), Spokesperson Quoted (dropdown: CEO, CTO, VP Marketing, VP Product, Other, None), Estimated Reach (numbers), Originated From (dropdown: Proactive Pitch, Inbound Request, Organic Mention, Event, Social), Connected Pitch (connect board: Pitches), Competitor Mention (checkbox), Coverage Summary (long text). Automations: when item created with Client connected, notify account team; weekly Friday summary of all coverage added that week grouped by client. Dashboard: coverage volume by week (line chart), sentiment breakdown (pie), message pull-through rate per key message (bar chart), coverage by media type (pie), top outlets (table), share of voice vs competitors (stacked bar chart by month), total estimated reach (number widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ClipBot
**Agent Purpose:** Automate media coverage ingestion, analysis, and client reporting to eliminate manual clip compilation.

**Triggers:**
- New coverage alert from monitoring integration (Meltwater/Cision webhook)
- Daily morning coverage digest schedule (7 AM per client timezone)
- Client report request
- Monthly/quarterly reporting schedule
- Competitor coverage spike detected (>3x normal daily volume)

**Actions:**
- Ingest coverage alerts, auto-populate metadata (outlet, journalist, media type, estimated reach)
- Analyze article text for sentiment and key message pull-through
- Match coverage to outgoing pitches for attribution
- Generate daily client coverage digest with summaries and highlights
- Build monthly coverage reports with SOV, sentiment trends, and message analysis
- Alert account teams to competitor coverage spikes or negative client coverage

**Data Required:**
- Coverage tracking board
- Client account board with key messages defined
- Pitch tracking board (for attribution)
- Meltwater/Cision API integration
- Competitor tracking definitions per client

**Autonomy Level:** Fully Autonomous
ClipBot processes all coverage automatically — ingestion, analysis, categorization, and reporting. Negative coverage alerts are immediate and automatic. Monthly reports auto-generate and can be client-shared directly.

**Example Interaction:**
> ClipBot detects a new article in Forbes mentioning client "GreenPath Energy" in a story about sustainable supply chain technology. It auto-logs the clip: Tier 1, Online, Positive sentiment, Key Message 1 ("AI-powered supply chain") confirmed present, Key Message 3 ("carbon reduction") confirmed present, Key Message 2 ("enterprise scalability") not mentioned. Estimated reach: 85M monthly visitors. ClipBot matches it to a pitch sent by account coordinator Priya two weeks ago and marks the pitch as "Placed." It adds the clip to the client's daily digest and flags it as a "highlight" for the monthly report. It also notices that competitor "LogiGreen" was mentioned in the same article and logs it in the competitor tracking view.

---

### Use Case 3: Crisis Communications Command Center

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
When a client crisis hits — product recall, executive scandal, data breach, social media firestorm — PR teams scramble. The "war room" runs on a chaotic mix of Slack channels, shared Google Docs, email chains, and conference calls. Stakeholder approvals on holding statements take hours because the review chain is unclear. Media inquiries pile up without tracking. Social listening happens on one screen while response drafting happens on another. Post-crisis, there's no structured record of what happened, what was said, and what was learned — making future crisis prep harder.

#### The Solution
monday.com as a pre-built crisis command center board activated when crisis hits. Structured workflows for media inquiry response, statement approval, stakeholder notification, and social monitoring. Templates for different crisis types (product, personnel, legal, cyber, social). Real-time dashboard showing inquiry volume, response times, and stakeholder approval status.

#### The Outcome
Reduce initial holding statement approval from hours to under 60 minutes. Track 100% of media inquiries with guaranteed response. Provide executive leadership with real-time crisis dashboard. Build institutional knowledge through post-crisis documentation.

#### Discovery Questions
- Walk me through the last significant client crisis your team managed — what was the biggest operational challenge?
- When a media inquiry comes in during a crisis, how do you track it, route it, and ensure a timely response?
- How long does it typically take to get a holding statement approved through your client's legal and executive chain?
- Do you have crisis playbook templates ready to go, or do you build the response framework from scratch each time?
- After a crisis is resolved, how do you capture lessons learned and update your crisis plans?

#### Industry Context
Crisis communications is the highest-stakes function in PR. Response windows have compressed from 24 hours (pre-social media) to under 60 minutes. A "holding statement" is the initial response acknowledging the situation without committing to specifics — it buys time while a full response is developed. "Dark sites" are pre-built web pages activated during crises. The "crisis tier" system (Tier 1: existential threat, Tier 2: significant reputation risk, Tier 3: localized issue) determines response level and stakeholder involvement. "Bridge" statements are transitional responses that connect the holding statement to the full response narrative.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a crisis communications command center board for a PR agency. Columns: Crisis Name (text), Client (connect board: Clients), Crisis Tier (status: Tier 1 - Critical, Tier 2 - Significant, Tier 3 - Localized), Crisis Type (dropdown: Product/Safety, Personnel/Executive, Legal/Regulatory, Cybersecurity, Social Media, Environmental, Financial, Activist/Political), Status (status: Monitoring, Active Response, Stabilizing, Resolved, Post-Mortem), Crisis Lead (people), Client Approver (text), Holding Statement (long text), Statement Status (status: Drafting, Internal Review, Client Legal Review, Client Exec Review, Approved, Distributed), Time to First Statement (formula: in hours from crisis start), Media Inquiries Count (numbers), Inquiries Responded (numbers), Response Rate (formula: Responded/Count as percentage), Social Sentiment Score (numbers, -100 to 100), Key Narrative (long text), Dark Site Status (status: Not Applicable, Ready, Activated, Deactivated), Crisis Start (date), Crisis Resolved (date). Sub-items for individual media inquiries: Journalist (text), Outlet (text), Question (text), Response Status (status: Received, Drafting Response, Pending Approval, Sent, Declined), Response Time (formula). Automations: when Crisis Tier is Tier 1, immediately notify agency leadership and client exec team; when Media Inquiry sub-item created, start response timer; when all sub-items are Sent or Declined, update Inquiries Responded count. Dashboard: active crises (number), avg response time (number), inquiry response rate (gauge), timeline of events (timeline view), media inquiry volume by hour (line chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CrisisOps
**Agent Purpose:** Orchestrate crisis response workflows, track media inquiries in real-time, and ensure no stakeholder communication falls through the cracks.

**Triggers:**
- Crisis board item activated (status changes to Active Response)
- New media inquiry logged
- Statement approval status change
- Social sentiment score drops below threshold
- 30-minute check-in intervals during active crisis
- Crisis resolved (trigger post-mortem workflow)

**Actions:**
- Activate crisis playbook template based on crisis type (auto-populate response checklist, stakeholder notification list, dark site activation)
- Route holding statement through approval chain and track time at each stage
- Log media inquiries with timestamps and auto-assign to available team members based on workload
- Generate 30-minute situation reports during active crisis: new inquiries, pending responses, sentiment movement, statement status
- Draft response suggestions based on crisis type and approved key messages (for human review)
- Create post-mortem document template with timeline, decisions, and lessons learned when crisis resolves

**Data Required:**
- Crisis command center board
- Client account board with crisis contacts and approval chains
- Pre-approved key messages and holding statement templates by crisis type
- Social monitoring integration
- Media contact database

**Autonomy Level:** Human-in-the-Loop (strict)
CrisisOps NEVER sends external communications autonomously. All statements, responses, and client-facing materials require human approval. CrisisOps manages workflow orchestration, tracking, and internal routing. During crisis, every action that touches external audiences requires human sign-off.

**Example Interaction:**
> At 2:15 PM, a crisis is activated for client "FreshFoods" — a social media post alleging contamination in a product line is going viral. CrisisOps immediately activates the "Product/Safety" playbook: populates the crisis checklist (confirm facts with client, draft holding statement, identify spokesperson, prepare FAQ), sends notification to agency crisis team and client VP Communications. By 2:25 PM, CrisisOps has a holding statement template pre-filled based on the crisis type and routes it to the account director. While the statement is in review, CrisisOps logs three incoming media inquiries (local TV, food trade publication, consumer news site) and assigns them to available team members. At 2:45 PM, CrisisOps generates its first situation report: "Statement in client legal review. 3 media inquiries received (0 responded — awaiting approved messaging). Social mentions: 2,400 in last 30 min, sentiment -67. Recommended action: expedite statement approval." The account director escalates, and the approved statement goes out at 3:10 PM — 55 minutes from crisis activation.

---

### Use Case 4: Influencer & KOL Relationship Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Influencer marketing has become a core PR function, but managing influencer relationships at scale is chaotic. PR teams maintain influencer lists in spreadsheets, track collaborations via email, negotiate rates through DMs, and manage content approval through text chains. FTC compliance (proper disclosure) requires monitoring every post, and many agencies have been caught when influencers forget #ad tags. Budget tracking across multiple influencer campaigns is fragmented. When a client asks "which influencers drove the best results last quarter?" the answer requires hours of manual compilation.

#### The Solution
monday.com as an influencer relationship management (IRM) platform. Each influencer is a contact with engagement rates, audience data, rates, and relationship history. Campaign boards connect influencers to specific activations with content approval workflows, posting schedules, and performance tracking. Compliance checklists ensure FTC disclosure on every deliverable.

#### The Outcome
Manage 3x more influencer relationships per team member. Achieve 100% FTC compliance tracking. Reduce influencer campaign setup from 2 weeks to 3 days. Provide clients with real-time campaign performance dashboards.

#### Discovery Questions
- How many influencer relationships does your team actively manage, and where does that information live?
- When onboarding a new influencer for a campaign, how long does the process take from identification to first post?
- How do you ensure every influencer post includes proper FTC disclosure?
- Can you quickly tell me which influencer drove the highest engagement rate on your last campaign?
- How do you manage content approval — does the client see every post before it goes live?

#### Industry Context
"KOL" (Key Opinion Leader) is the term used more in B2B and healthcare PR; "influencer" dominates consumer PR. Influencer tiers: mega (1M+ followers), macro (100K-1M), micro (10K-100K), nano (1K-10K). The FTC requires "clear and conspicuous" disclosure of material connections — #ad, #sponsored, or platform-native paid partnership labels. "Earned" influencer mentions (unpaid) vs. "paid" partnerships have different disclosure requirements. CPE (cost per engagement) and EMV (earned media value) are standard measurement metrics. "Whitelisting" allows brands to run paid ads through an influencer's social account — requiring content usage rights negotiation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an influencer relationship management system for a PR agency. Board 1 - Influencer Database: Influencer Name (text), Handle/Username (text), Platform (dropdown: Instagram, TikTok, YouTube, Twitter/X, LinkedIn, Podcast, Newsletter, Multiple), Follower Count (numbers), Avg Engagement Rate (numbers, percentage), Influencer Tier (dropdown: Mega 1M+, Macro 100K-1M, Micro 10K-100K, Nano 1K-10K), Niche/Category (dropdown: Beauty, Fashion, Tech, Food, Fitness, Travel, Parenting, Business, Gaming, Lifestyle), Contact Email (email), Agent/Manager (text), Rate Per Post (numbers, currency USD), Rate Per Story/Reel (numbers, currency USD), FTC Briefed (checkbox), Usage Rights (dropdown: Content Only, Whitelisting 30 Days, Whitelisting 90 Days, Perpetual, None Agreed), Past Campaigns (connect board: Campaigns), Performance Rating (rating), Relationship Owner (people), Notes (long text). Board 2 - Influencer Campaigns (connected): Campaign Name (text), Client (connect board: Clients), Influencers (connect board: Influencer Database), Content Type (dropdown: Feed Post, Story, Reel, TikTok, YouTube Video, Blog, Podcast Mention, Package), Content Status (status: Briefed, Content Submitted, Revisions Requested, Client Approved, Posted, Late), Posting Date (date), FTC Disclosure Verified (checkbox), Content Link (link), Impressions (numbers), Engagements (numbers), Cost (numbers), CPE (formula: Cost/Engagements). Automations: when Content Status changes to Posted and FTC Disclosure Verified is unchecked, send urgent notification 'FTC compliance check needed'; 2 days before Posting Date if Content Status is still Briefed, notify team 'Content overdue.' Dashboard: total campaign spend (number), avg CPE (number), influencers by tier (pie), content pipeline by status (funnel), top performers by engagement rate (bar chart), FTC compliance rate (gauge)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** InfluencerIQ
**Agent Purpose:** Manage influencer discovery, campaign coordination, compliance monitoring, and performance analysis at scale.

**Triggers:**
- New influencer campaign created
- Content status changes (submission, approval, posting)
- Posting date approaching with content not yet approved
- Influencer posts live content (webhook/monitoring)
- Monthly performance reporting schedule
- Client brief received requiring influencer recommendations

**Actions:**
- Recommend influencers from database based on campaign brief (niche, platform, budget, audience match)
- Track content approval workflow and send automated reminders
- Monitor posted content for FTC disclosure compliance (check for #ad, #sponsored, paid partnership label)
- Calculate real-time campaign CPE and compare to benchmarks
- Generate campaign wrap reports with ROI analysis per influencer
- Flag influencers with declining engagement rates or audience authenticity concerns

**Data Required:**
- Influencer database board
- Campaign board
- Social media API integrations for live performance data
- FTC compliance guidelines by platform
- Historical campaign performance for benchmarking

**Autonomy Level:** Human-in-the-Loop
InfluencerIQ recommends and reports autonomously. All influencer selection, content approvals, and client-facing deliverables require human sign-off. FTC compliance alerts are automatic and non-negotiable.

**Example Interaction:**
> The account team receives a brief from client "GlowSkin" for a summer skincare campaign: $50K budget, target Gen Z women, Instagram and TikTok focus. InfluencerIQ scans the database and returns 12 recommendations across tiers: 2 macro influencers ($8K-12K each, beauty niche, 4.2% avg engagement), 5 micro influencers ($2K-4K each, skincare-specific), and 5 nano influencers ($500-1K each, high engagement but smaller reach). For each, it shows past campaign performance with the agency, audience demographics overlap with GlowSkin's target, and available content windows. The team selects 8 influencers, and InfluencerIQ creates campaign items for each with briefing deadlines, content submission dates, and posting windows. It monitors the workflow, sends a reminder when one micro influencer hasn't submitted content 3 days before posting date, and after launch, generates a daily performance tracker showing live engagement metrics.

---

### Use Case 5: Event & Press Briefing Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
PR events — press conferences, product launches, media tours, press briefings, analyst days, and award submissions — are operationally complex. Media invite lists require careful curation (can't invite competing outlets to the same exclusive). RSVPs are tracked in spreadsheets. Day-of logistics (run of show, talking points, media kits, A/V requirements) live in separate documents. Post-event follow-up (thank-you notes, exclusive access, clip collection) is manual and often incomplete. The planning effort for a single major press event can consume a team of 3-4 for weeks.

#### The Solution
monday.com as the event command center with connected boards for the invite list, run of show, media kit checklist, logistics, and post-event follow-up. Templates for different event types. Automations manage RSVP tracking, reminder sequences, and post-event task assignment.

#### The Outcome
Reduce event planning overhead by 40% through templates and automation. Achieve 100% post-event follow-up (no journalist left unthanked). Centralize institutional knowledge of event best practices. Enable simultaneous management of 3-4 events without team burnout.

#### Discovery Questions
- How many media events or press briefings does your team manage per quarter?
- Walk me through your media invite and RSVP process — how do you manage conflicts between competing outlets?
- After an event, how do you ensure every attending journalist gets appropriate follow-up?
- Do you have standardized event templates, or does each event start from scratch?
- How do you share the run of show and talking points with client executives, and how late do changes come in?

#### Industry Context
"Press briefings" are smaller, intimate meetings (1-5 journalists) for deep-dive stories. "Press conferences" are large-format with open Q&A. "Media tours" involve bringing journalists to a facility. "Deskside briefings" are in-person meetings at the journalist's office. "Embargoed" events provide information before public announcement with an agreed publication date — violating embargo destroys trust. "Press kits" (now usually digital) contain fact sheets, executive bios, product specs, high-res images, and b-roll. "Award submissions" — entering clients for industry awards — is a significant PR activity requiring rigorous deadline and content management.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a PR event management system for a PR agency. Board 1 - Events: Event Name (text), Client (connect board: Clients), Event Type (dropdown: Press Conference, Product Launch, Media Tour, Press Briefing, Analyst Day, Awards Gala, Webinar, Deskside Series), Event Date (date), Location (text), Event Status (status: Planning, Invites Out, RSVP Tracking, Confirmed, Day-Of, Post-Event, Complete), Event Lead (people), Budget (numbers, currency USD), Actual Spend (numbers, currency USD), Expected Attendance (numbers), Confirmed Attendance (numbers), Run of Show Doc (file), Media Kit (file), Spokesperson (text), Talking Points Status (status: Drafting, Client Review, Approved), Embargo (checkbox), Embargo Lifts (date/time). Board 2 - Media Invites (connected to Events): Journalist Name (text), Outlet (text), Email (email), Invite Status (status: Not Sent, Invited, RSVP Yes, RSVP No, RSVP Maybe, No Response, Waitlisted), Outlet Conflict Group (dropdown: Group A, Group B, Group C, None — for managing competing outlets), Dietary/Access Needs (text), Post-Event Follow-Up Status (status: Not Started, Thank You Sent, Exclusive Offered, Story Placed, Complete), Assigned To (people). Automations: when Invite Status changes to RSVP Yes, increment Confirmed Attendance on parent event; 1 week before Event Date, notify Event Lead of journalists with No Response for re-pitch; when Event Status changes to Post-Event, create follow-up tasks for all RSVP Yes journalists. Dashboard: events pipeline by month (timeline), RSVP status breakdown (pie), confirmed vs target attendance (bar), upcoming events in next 30 days (calendar), post-event follow-up completion rate (gauge)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** EventOps
**Agent Purpose:** Manage PR event logistics, automate invite workflows, prevent outlet conflicts, and ensure complete post-event follow-up.

**Triggers:**
- New event created
- RSVP status changes
- Event date approaching (1 week, 3 days, 1 day)
- Embargo lift date/time reached
- Event status changes to Post-Event
- Outlet conflict detected (competing outlets in same invite batch)

**Actions:**
- Generate invite lists from media database based on event type, beat relevance, and outlet tier
- Flag outlet conflicts (e.g., WSJ and NYT both invited to an "exclusive" briefing) and suggest resolution
- Send RSVP reminder sequences (automated follow-ups at 7, 3, and 1 day before event)
- Generate day-of briefing packet: run of show, confirmed attendees with photos, talking point reminders
- Create post-event follow-up tasks for each attending journalist with suggested next steps
- Compile post-event report: attendance, coverage generated, ROI estimate

**Data Required:**
- Event board and media invite board
- Media contact database with outlet relationships
- Run of show documents and talking points
- Historical event performance data

**Autonomy Level:** Human-in-the-Loop
EventOps manages logistics and tracking autonomously. All journalist-facing communications (invites, follow-ups) require human review. Outlet conflict resolution requires human decision. Day-of changes require human approval.

**Example Interaction:**
> EventOps is managing a product launch event for client "TechWave" in three weeks. It generates an initial invite list of 45 journalists based on the tech beat, outlet tier (60% Tier 1, 30% Tier 2, 10% Tier 3 podcast/newsletter), and past TechWave coverage. It immediately flags a conflict: both The Wall Street Journal and Financial Times are on the list, but the client wants an "exclusive first look" — can't offer that to both. EventOps suggests: "Recommend offering WSJ the exclusive pre-event briefing (they covered TechWave's last funding round positively) and inviting FT to the general press conference with an offer of a post-event executive interview as added value." The account team agrees and adjusts the invite tiers. One week before the event, EventOps notes 12 journalists haven't responded and sends personalized re-pitch suggestions for each based on their coverage patterns.

---

### Use Case 6: Client Reporting & ROI Dashboard

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
PR agencies spend enormous time on client reporting — monthly activity reports, quarterly business reviews, annual program reviews. Each report is custom-built in PowerPoint or Keynote, requiring manual data compilation from multiple sources (coverage tracking, pitch activity, social metrics, event recaps). A single monthly report takes 4-6 hours per client. Across 30-50 clients, that's 120-300 hours per month — nearly two FTEs just building reports. Clients often receive these reports 2-3 weeks after month-end, making them backward-looking rather than actionable.

#### The Solution
monday.com dashboards that serve as always-on client reports. Connected data from pitching, coverage, events, and social monitoring feeds real-time dashboards shared with clients via guest access or scheduled PDF exports. Templates by program type ensure consistency while allowing customization.

#### The Outcome
Eliminate 80% of manual report creation effort. Shift from monthly backward-looking reports to real-time dashboards. Increase client satisfaction through transparency and timeliness. Repurpose 100+ hours/month of junior staff time from reporting to strategic work.

#### Discovery Questions
- How many hours per month does your team spend building client reports, and what does each report cost you in billable time?
- Do your clients receive coverage and activity data in real-time, or do they wait for monthly reports?
- What's the typical time gap between month-end and report delivery?
- Have you ever lost a client partly because they felt they lacked visibility into your team's activity?
- What would your team do with 100 extra hours per month if they weren't building reports?

#### Industry Context
PR agency reporting is a trust mechanism — clients can't "see" PR work the way they can see an ad. Reports prove activity and impact. The shift from "output" metrics (pitches sent, clips secured) to "outcome" metrics (brand awareness lift, purchase intent, share of voice change) reflects the Barcelona Principles. "QBR" (Quarterly Business Review) is the formal client presentation reviewing program performance. "Retainer utilization" reporting shows how staff hours are allocated against the fee. Many agencies now offer "client portals" — and building one on monday.com is a competitive differentiator.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a client PR reporting dashboard system on monday.com. Create a master dashboard per client that pulls from connected boards: Pitch Activity (pitches sent, response rate, placements secured — from Pitch board), Media Coverage (clip volume by week, sentiment breakdown, tier distribution, total reach — from Coverage board), Influencer Campaigns (active campaigns, CPE, content status — from Influencer board), Events (upcoming and recent events, attendance metrics — from Events board), Program Health (overall status, key milestones, next month priorities — from Account Management board). Widgets: total media placements this month (number), total estimated reach (number), share of voice trend (line chart comparing client vs 2 competitors over 6 months), coverage sentiment (pie chart), pitch conversion funnel (pitches → responses → placements), top 5 placements by reach (table), upcoming activities (timeline), key message pull-through rate (bar chart per key message). Add a 'Report Summary' text widget at the top for the account lead to add monthly narrative context. Enable guest access for client stakeholders with view-only permissions."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ReportGenius
**Agent Purpose:** Automate PR client reporting by compiling data across boards, generating narrative summaries, and delivering polished reports on schedule.

**Triggers:**
- Monthly reporting schedule (1st business day of each month)
- Quarterly Business Review prep (2 weeks before scheduled QBR)
- Client requests ad hoc report
- Significant coverage milestone reached (e.g., 100th placement)
- Year-end annual review schedule

**Actions:**
- Pull data from all connected boards (pitches, coverage, influencer, events) for the reporting period
- Calculate key metrics: coverage volume, SOV, sentiment, message pull-through, pitch conversion, influencer CPE
- Draft narrative summary highlighting top wins, challenges, and recommendations for next period
- Generate comparison to prior period and year-over-year trends
- Format into client-ready dashboard with visualizations
- Send draft to account lead for review before client distribution

**Data Required:**
- All connected PR activity boards (pitches, coverage, influencer, events)
- Client account board with program goals and KPIs
- Historical reporting data for trend analysis
- Competitor tracking data for SOV

**Autonomy Level:** Human-in-the-Loop
Data compilation and metric calculation are fully autonomous. Narrative summaries and recommendations are generated as drafts for account lead review. Client-facing delivery always requires human approval.

**Example Interaction:**
> It's March 1st and ReportGenius compiles the February report for client "UrbanFit." Data pull: 28 pitches sent (up 12% from Jan), 9 placements secured (32% conversion, above 25% benchmark), total estimated reach 42M, sentiment 89% positive, Key Message 1 ("AI personal training") appeared in 7 of 9 placements (78% pull-through). SOV vs. competitor Peloton: UrbanFit 18% (up from 14%), Peloton 35% (down from 38%). ReportGenius drafts the summary: "February was a strong month driven by the CES product launch. Key win: Wired feature drove 15M reach alone. Recommendation: capitalize on momentum with a follow-up media tour targeting health/wellness verticals where SOV is underrepresented." It sends the draft to the account director, who tweaks two sentences and approves for client delivery.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Pitch | Proactive outreach to a journalist with a story idea on behalf of a client |
| Placement | Successfully getting a story published or aired |
| Earned media | Coverage gained through PR efforts rather than paid advertising |
| SOV (Share of Voice) | Client's media presence relative to competitors, measured by volume, reach, or prominence |
| AVE | Advertising Value Equivalency — discredited metric estimating what coverage would cost as ad space |
| Barcelona Principles | AMEC's industry-standard framework for PR measurement (outcomes over outputs) |
| Message pull-through | Whether media coverage includes the client's key talking points |
| Embargo | Agreement that information shared with journalist won't be published until an agreed date/time |
| Holding statement | Initial crisis response acknowledging a situation without committing to specifics |
| Deskside | In-person briefing at the journalist's office |
| KOL | Key Opinion Leader — term for influencers, especially in B2B and healthcare contexts |
| Media kit / Press kit | Collection of materials (fact sheets, bios, images, b-roll) provided to journalists |
| Clip | Individual piece of media coverage |
| Dark site | Pre-built web page activated only during a crisis |
| Whitelisting | Allowing a brand to run paid ads through an influencer's social account |
| CPE | Cost Per Engagement — influencer metric dividing cost by total engagements |
| EMV | Earned Media Value — estimated value of influencer content based on engagement |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| SVP/EVP, PR or Communications Director | Sets PR strategy, manages senior client relationships, oversees practice areas | Decision-maker |
| VP/Group Director | Manages client account portfolio, team leadership, P&L responsibility | Decision-maker |
| Account Director / Senior Account Manager | Day-to-day client strategy and program management | Influencer/Decision-maker |
| Account Manager | Executes PR programs: pitching, media relations, event coordination | User |
| Account Coordinator / Associate | Junior execution: media list building, monitoring, clip reports, logistics | User |
| Digital/Social Director | Manages influencer programs, social content, digital PR | Influencer |
| Crisis Communications Lead | Runs crisis response for clients, maintains crisis preparedness | Decision-maker (during crisis) |
| Measurement & Analytics Manager | Responsible for reporting, ROI analysis, and campaign measurement | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Creative & Design | PR campaigns need creative assets — press kit design, social content, video | Unified content production workflow |
| Marketing / Media | Integrated campaigns combining earned (PR) with paid (media) and owned (content) | Holistic campaign management platform |
| HR | Internal communications, employer branding, executive visibility | Employee communications boards on same platform |
| Legal | Statement approvals, FTC compliance, contract review for influencers | Legal review workflow integrated into PR processes |
| Customer Success | Client onboarding, satisfaction tracking, renewal management | Client health dashboard incorporating PR performance |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Cision / PR Newswire | Media database + distribution + monitoring | Great for contacts/distribution but weak on workflow management. monday.com is the operational layer Cision can't provide. |
| Meltwater | Media monitoring + social listening + analytics | Strong monitoring but no project/workflow management. Integrates with monday.com via API. |
| Muck Rack | Journalist database + pitching + monitoring | Newer and popular but limited to media relations — doesn't cover events, influencer, crisis, or client reporting workflows. |
| CoverageBook | Coverage reporting tool | Single-purpose reporting tool. monday.com replaces it with always-on dashboards covering all PR activities. |
| Asana / Monday alternatives | Generic work management | Lack PR-specific workflows, media contact management, and coverage tracking. monday.com can be configured for PR-specific use while offering platform breadth. |
| Sprout Social / Hootsuite | Social media management + listening | Social-only. Don't cover earned media, events, or client reporting. |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Cision/Meltwater for everything" | "Those tools are excellent for media data — contacts, monitoring, distribution. But they don't manage your pitch workflow, event logistics, client reporting, or crisis response. monday.com is the operational hub where your team actually works, pulling Cision/Meltwater data in rather than forcing your team to live in a monitoring tool." |
| "PR is relationship-driven — you can't automate relationships" | "Absolutely. We're not automating the relationship — we're automating the admin around it. Your team spends hours on follow-up tracking, clip reports, and event logistics instead of building those relationships. We free up that time so they can do more of what they're great at." |
| "Our clients won't use another portal" | "They don't have to 'use' it — they just see a dashboard. It's a link they check when they want an update instead of emailing your team. Most clients love the transparency, and it reduces the 'just checking in on our report' emails by 80%." |
| "We're too small to need a platform — spreadsheets work fine" | "Spreadsheets work until they don't. The day a crisis hits and you need to track 30 media inquiries simultaneously, or a client asks for last quarter's coverage data in 10 minutes, spreadsheets become the bottleneck. Start with one workflow (pitch tracking or coverage reporting) and expand." |
| "We've tried project management tools before and our team didn't adopt them" | "The difference is building workflows your team actually uses — not forcing them into a generic task list. When pitch tracking gives them real-time conversion data and auto-generates the client report they'd spend 4 hours building, adoption happens because it saves them pain." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for PR agency workflow transformation case study]
- [Placeholder for media coverage monitoring modernization reference]
- [Placeholder for crisis communications readiness success story]
- [Placeholder for influencer campaign management reference]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
