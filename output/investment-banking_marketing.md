# Investment Banking × Marketing Playbook

## Overview

Marketing within investment banking operates in a uniquely constrained environment where brand reputation, regulatory compliance, and relationship-driven deal origination intersect. Unlike consumer-facing industries, investment banking marketing focuses on thought leadership, deal tombstones, league table positioning, and cultivating relationships with C-suite executives and boards of directors. The marketing function typically sits within a broader Corporate Communications or Business Development group, often with 15–50 professionals in bulge-bracket firms and 3–10 in middle-market boutiques.

Investment banking marketing teams must navigate strict SEC, FINRA, and MiFID II regulations governing how they communicate capabilities, track records, and forward-looking statements. Every piece of collateral — from pitch books to press releases to conference sponsorship materials — requires compliance review. This creates enormous bottlenecks: a single credentials deck can take 2–3 weeks to move through legal and compliance before it reaches a managing director's hands.

The competitive landscape is fierce. Banks differentiate on sector expertise, deal experience, and relationship depth. Marketing's role is to arm bankers with compelling, up-to-date credentials, position the firm in industry rankings (Dealogic, Refinitiv, Bloomberg league tables), and generate awareness among target companies considering M&A, IPOs, or debt issuance. The shift toward digital channels — LinkedIn, webinars, proprietary research portals — is accelerating, but most firms still rely heavily on manual, relationship-driven processes.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Credential deck production, pitch book assembly, and deal tracking are extremely labor-intensive — often requiring junior analysts to spend 20+ hours per week on manual updates |
| 2 | Scale Impact Without Overhead | High | Marketing teams are small relative to the revenue they support; banks need to cover more sectors and geographies without proportional headcount growth |
| 3 | Consolidate Tech Stack with AI | Medium-High | Teams juggle Dealogic, PitchBook, Capital IQ, CRM systems, SharePoint, and design tools — a unified platform reduces context-switching and data silos |

## Prioritized Use Cases

---

### Use Case 1: Automated Credentials Deck & Pitch Book Assembly

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Building credentials decks (also called "cred decks" or "pitch books") is one of the most time-consuming activities in IB marketing. Analysts manually pull deal tombstones from internal databases, cross-reference league table rankings, update sector expertise slides, and format everything into client-specific presentations. A single customized pitch book can take 15–25 hours. When a managing director requests a deck for a Tuesday morning meeting on Friday afternoon, the marketing team works through the weekend. Banks with 10+ sector coverage groups may produce 200+ unique decks per quarter.

#### The Solution
monday.com Work Management serves as the central pitch book request and production pipeline. Each request is an item with structured fields: target company, sector, deal type (M&A, ECM, DCM, restructuring), managing director, deadline, compliance status. A connected mondayDB stores the firm's deal tombstone library — every closed transaction with date, value, role (lead left, co-manager, advisor), sector tags, and geography. When a request comes in, monday AI Agents pull relevant tombstones, rank them by relevance to the target, and auto-generate a draft deck outline. Vibe-built workflows manage the compliance review queue with automated routing based on content type and jurisdiction. Dashboards show production velocity, bottleneck stages, and turnaround times.

#### The Outcome
Pitch book production time reduced from 15–25 hours to 3–5 hours. Weekend work for marketing analysts drops by 70%. Managing directors get fresher, more relevant credentials with sector-specific deal highlights. Compliance review cycles shrink from 5 days to 2 days through structured routing and pre-approved template libraries.

#### Discovery Questions
1. "How many credentials decks does your marketing team produce per quarter, and what's the average turnaround time from request to delivery?"
2. "When a managing director needs a customized pitch book for a specific sector or deal type, how does that request flow through your team today?"
3. "How do you currently maintain your deal tombstone database, and how often does stale or missing data cause rework?"
4. "What percentage of your marketing team's time is spent on pitch book production versus strategic initiatives like thought leadership or brand positioning?"
5. "How does compliance review fit into your pitch book workflow, and where do bottlenecks typically occur?"

#### Industry Context
Investment banks organize coverage by industry sectors (TMT, Healthcare, Industrials, FIG, Natural Resources, etc.) and product groups (M&A, Leveraged Finance, Equity Capital Markets, Debt Capital Markets). Marketing must understand this matrix to build relevant credentials. "Tombstones" are standardized deal summaries showing the bank's role — these are the currency of credibility in IB. League tables from Dealogic, Refinitiv, and Bloomberg rank banks by deal volume and value; positioning in these tables is a critical marketing KPI.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Pitch Book Production Pipeline board. Columns: Request Name (text), Requesting MD (people), Target Company (text), Sector (dropdown: TMT, Healthcare, Industrials, FIG, Energy, Consumer, Real Estate), Deal Type (dropdown: M&A Advisory, ECM, DCM, Leveraged Finance, Restructuring), Priority (status: Urgent/High/Standard), Status (status: Requested, Tombstones Pulled, Draft In Progress, Compliance Review, MD Review, Final, Delivered), Deadline (date), Assigned Analyst (people), Compliance Reviewer (people), Turnaround Days (formula), Notes (long text). Create groups: New Requests, In Production, Compliance Queue, Ready for Delivery, Completed. Add automations: when Status changes to Compliance Review, notify Compliance Reviewer and assign due date 2 days out; when Priority is Urgent, notify team channel; when Status changes to Delivered, calculate Turnaround Days. Add views: Kanban by Status, Timeline view by Deadline, Dashboard with widgets for Average Turnaround Time, Decks by Sector pie chart, Production Volume by Month bar chart, Compliance Bottleneck counter."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DealDeck Assembler
**Agent Purpose:** Automatically assembles draft credentials decks by matching deal tombstones to pitch book requests based on sector, deal type, geography, and recency.

**Triggers:**
- New pitch book request item created with sector and deal type populated
- Managing director tags a request as "Urgent"
- Weekly scheduled run to refresh tombstone relevance scores
- Status changes to "Tombstones Pulled" (triggers draft outline generation)

**Actions:**
- Queries mondayDB tombstone library for matching deals (sector + deal type + geography filters)
- Ranks tombstones by relevance score (recency, deal size, role prominence)
- Generates draft deck outline with recommended tombstone selection and ordering
- Creates sub-items for each deck section (Cover, Firm Overview, Sector Credentials, Selected Tombstones, Team Bios)
- Notifies assigned analyst with draft outline and recommended content
- Flags any tombstones older than 18 months for review

**Data Required:**
- mondayDB: Complete deal tombstone library with structured fields (date, value, role, sector, geography, status)
- Integration: PitchBook or Capital IQ API for market data enrichment
- Integration: Internal CRM for relationship context on target company

**Autonomy Level:** Human-in-the-Loop
The agent assembles and recommends; the analyst reviews, customizes for the specific client context, and the MD gives final approval. Compliance review remains human-driven.

**Example Interaction:**
> On Monday morning, Managing Director Sarah Chen creates a pitch book request for a $2B healthcare services M&A target. She tags it as "High" priority with a Wednesday deadline. The DealDeck Assembler immediately queries the tombstone library, finding 23 relevant healthcare M&A transactions the firm advised on in the past 3 years. It ranks them by deal size and recency, selecting the top 8 for the credentials section. It also pulls the firm's current Dealogic ranking in Healthcare M&A (#4 by deal count, #6 by value) and flags that the team recently closed a comparable transaction — a $1.8B physician practice management platform acquisition.
>
> The agent generates a draft outline with six sections, assigns them as sub-items to marketing analyst James, and posts a summary: "Draft outline ready — 8 tombstones selected, league table data current as of Q4 2025. Note: Two selected tombstones are pending final close confirmation." James reviews, swaps one tombstone for a more relevant regional deal, and moves the item to "Draft In Progress." The deck is in compliance review by Tuesday afternoon.

---

### Use Case 2: League Table Tracking & Competitive Intelligence Dashboard

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks obsess over league table rankings — they're the scoreboard of the industry. Marketing teams manually track the firm's position across multiple providers (Dealogic, Refinitiv, Bloomberg), across dozens of categories (by product, sector, geography, deal size), and across time periods. This data informs everything from pitch books to press releases to partner compensation discussions. Currently, a junior analyst spends 10–15 hours per week pulling league table data, reformatting it, and distributing updates. When rankings shift, the team scrambles to update all active pitch materials.

#### The Solution
A monday.com dashboard system centralizes league table data. mondayDB stores historical rankings across all providers and categories. Automated integrations pull weekly snapshots from Dealogic and Refinitiv APIs. Vibe-built dashboards display real-time rankings with trend lines, competitive positioning heat maps, and alerts when the firm moves up or down in key categories. Items track each ranking category with historical performance, competitive gaps, and linked pitch materials that reference that ranking. When a ranking changes, automations flag all active pitch books that cite the old data.

#### The Outcome
League table tracking effort reduced from 15 hours/week to 2 hours/week. Pitch books always reference current rankings (eliminating the embarrassing scenario of presenting outdated data to a prospect). Senior bankers get weekly competitive intelligence briefings auto-generated from the dashboard. Marketing can proactively identify ranking improvement opportunities (e.g., "We need two more mid-market healthcare deals to move from #6 to #4 in Dealogic").

#### Discovery Questions
1. "How many league table categories do you actively track, and across how many data providers?"
2. "When your firm's ranking changes in a key category, how quickly does that update propagate to active pitch materials?"
3. "How do you currently communicate competitive positioning insights to your coverage teams and senior leadership?"
4. "Have you ever presented outdated league table data to a client? What was the impact?"
5. "How do you identify opportunities to improve your rankings — for example, targeting deal types that would move you up in specific categories?"

#### Industry Context
League tables rank banks by deal volume and value within specific product/sector/geography categories. Rankings are updated quarterly (sometimes monthly) by Dealogic, Refinitiv (formerly Thomson Reuters), and Bloomberg. Banks strategically pursue certain deals partly to improve league table positioning. A bank's ranking directly impacts its ability to win mandates — CFOs and boards want "top-5" advisors. The phrase "league table credit" refers to how a deal is attributed across co-advisors, which is a contentious and carefully tracked metric.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a League Table Tracker board. Columns: Category Name (text), Provider (dropdown: Dealogic, Refinitiv, Bloomberg), Product (dropdown: M&A, ECM, DCM, Leveraged Finance, Restructuring), Sector (dropdown: All, TMT, Healthcare, Industrials, FIG, Energy, Consumer), Geography (dropdown: Global, Americas, EMEA, APAC, US), Current Rank (numbers), Previous Rank (numbers), Rank Change (formula: Previous Rank minus Current Rank), Deal Count (numbers), Deal Value $M (numbers), #1 Competitor (text), Gap to #1 (numbers), Period (dropdown: Q1 2026, Q4 2025, Q3 2025, Full Year 2025), Last Updated (date), Linked Pitch Books (connect board). Create groups by Provider: Dealogic Rankings, Refinitiv Rankings, Bloomberg Rankings. Add automations: when Current Rank changes, notify marketing lead and flag all connected Pitch Book items for update; weekly recurring item to pull fresh data. Dashboard with: Ranking Trend chart (line chart by quarter), Heat Map table of all categories, Improvement Opportunities widget (categories where gap to next rank is small), Competitive Comparison bar chart."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LeagueWatch Analyst
**Agent Purpose:** Monitors league table movements, identifies competitive threats and opportunities, and auto-updates all dependent marketing materials.

**Triggers:**
- Weekly scheduled data refresh from league table providers
- Manual trigger when new quarterly rankings are published
- When a new deal closes (to project ranking impact)
- When a pitch book is created that references league table data

**Actions:**
- Pulls latest ranking data and updates mondayDB records
- Compares current vs. previous rankings, generates movement alerts
- Identifies pitch books referencing outdated rankings and creates update tasks
- Generates weekly competitive intelligence summary for distribution
- Projects ranking impact of pipeline deals (e.g., "If we close the $3B TMT deal, we move from #5 to #3 in Americas TMT M&A")
- Flags categories where the firm is within 1–2 deals of moving up a rank

**Data Required:**
- Dealogic, Refinitiv, Bloomberg API access or data feeds
- Internal deal pipeline data (for projection modeling)
- Connected Pitch Book Production board (for material updates)

**Autonomy Level:** Fully Autonomous (data updates and alerts) / Human-in-the-Loop (ranking projections shared for strategic review)
Data pulls and alert generation are fully automated. Strategic recommendations (e.g., "pursue this deal type to improve ranking") are flagged for human review.

**Example Interaction:**
> On the first Monday of Q1 2026, LeagueWatch detects that the firm dropped from #3 to #5 in Dealogic's Global Healthcare M&A rankings. It immediately sends an alert to the Healthcare coverage group head and the marketing team lead. It identifies 7 active pitch books that cite the #3 ranking and creates update tasks for each. It also analyzes the gap: "Two additional deals totaling $1.5B+ would restore #3 ranking. Currently, three Healthcare M&A mandates in pipeline totaling $4.2B — if two close in Q1, projected rank improves to #2." The marketing team updates materials within hours instead of discovering the change weeks later.

---

### Use Case 3: Event & Conference Management Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks sponsor and attend 50–100+ industry conferences annually (J.P. Morgan Healthcare Conference, Goldman Sachs Communacopia, sector-specific events). Each event requires coordinating speaker submissions, attendee lists, meeting scheduling (often 30–50 one-on-one meetings per conference), branded materials, follow-up campaigns, and ROI tracking. Marketing teams manage this across spreadsheets, email threads, and disconnected calendar systems. The most painful part: scheduling back-to-back 30-minute meetings between bankers and target companies at conferences, which currently involves weeks of email ping-pong.

#### The Solution
monday.com Work Management provides an end-to-end conference management system. Each conference is a high-level item with sub-items for every task: speaker submissions, booth logistics, attendee registration, meeting scheduling, collateral production, follow-up actions. A connected CRM board tracks target companies and their conference attendance history. Vibe-built meeting scheduler workflows allow bankers to rank their target meetings; marketing then orchestrates scheduling with automated conflict detection. Post-event, automations trigger follow-up sequences and ROI tracking based on meetings-to-mandates conversion.

#### The Outcome
Conference preparation time reduced by 40%. Meeting scheduling for major conferences drops from 3 weeks to 4 days. Post-event follow-up completion rate increases from 45% to 90%. Marketing can demonstrate conference ROI by tracking the pipeline from "conference meeting" to "mandate won," justifying $500K–$2M annual conference budgets.

#### Discovery Questions
1. "How many industry conferences does your firm participate in annually, and how do you decide which ones to sponsor versus attend?"
2. "Walk me through how you schedule banker-to-company meetings at a major conference — what does that process look like today?"
3. "After a conference, how do you track follow-up actions and measure whether the event generated pipeline?"
4. "How do you currently coordinate across coverage groups when multiple bankers want meetings with the same company at an event?"
5. "What's your total annual spend on conferences, and how do you justify that investment to leadership?"

#### Industry Context
Major IB conferences are critical deal origination venues. The J.P. Morgan Healthcare Conference (January, San Francisco) alone generates billions in deal flow. Banks host "non-deal roadshows" (NDRs) to introduce management teams to investors. Conference meetings are typically 30-minute slots in hotel suites, scheduled back-to-back from 7 AM to 7 PM. "Fireside chats" and panel participation establish thought leadership. Conference sponsorship tiers ($50K–$500K) determine booth size, speaking slots, and meeting room access.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Conference Management board. Columns: Conference Name (text), Date Range (date), Location (text), Sector Focus (dropdown: TMT, Healthcare, Industrials, FIG, Energy, Consumer, Cross-Sector), Sponsorship Tier (dropdown: Platinum, Gold, Silver, Attendee Only), Sponsorship Cost (numbers with $ prefix), Status (status: Planning, Registered, Materials Ready, Active, Post-Event, Closed), Event Lead (people), Speaker Submissions (numbers), Meetings Scheduled (numbers), Meetings Completed (numbers), Follow-ups Sent (numbers), Pipeline Generated $M (numbers), Mandates Won (numbers), ROI (formula: Pipeline Generated divided by Sponsorship Cost). Create groups: Upcoming Events, Active Events, Post-Event Follow-up, Completed. Sub-items for each conference: individual tasks (Submit Speaker, Book Travel, Produce Collateral, Schedule Meetings, Send Follow-ups). Add automations: 30 days before conference date, change Status to Planning and notify Event Lead; when Status changes to Post-Event, create follow-up tasks for each meeting completed; weekly reminder on open follow-ups. Dashboard: Conference Calendar (timeline), ROI by Conference (bar chart), Meetings-to-Mandates Funnel, Annual Spend vs Pipeline Generated, Upcoming Deadlines widget."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ConferenceConnect Scheduler
**Agent Purpose:** Automates conference meeting scheduling by matching banker priorities with target company availability and resolving conflicts across coverage groups.

**Triggers:**
- Conference item status changes to "Planning" (T-30 days)
- Bankers submit meeting priority rankings
- Target company confirms or declines meeting request
- Schedule conflicts detected between coverage groups

**Actions:**
- Collects meeting priority lists from all participating bankers
- Cross-references target company attendance confirmations
- Generates optimized meeting schedule minimizing conflicts and maximizing priority fulfillment
- Sends meeting invitations with room assignments and time slots
- Resolves double-booking conflicts by escalating to coverage group heads
- Post-event: creates follow-up items for each completed meeting with context notes

**Data Required:**
- Banker meeting priority rankings (integrated form)
- Conference attendee list and company participation data
- Historical meeting data (previous conferences)
- CRM relationship data for context enrichment

**Autonomy Level:** Human-in-the-Loop
Agent generates optimized schedule; senior bankers review and approve. Conflict resolution between groups requires human arbitration.

**Example Interaction:**
> Three weeks before the annual Healthcare conference, ConferenceConnect collects priority lists from 12 participating bankers. Managing Director Tom requests meetings with 8 companies; VP Lisa has 6 targets, with 3 overlapping Tom's list. The agent detects conflicts, proposes a schedule where Tom takes the $5B+ targets (aligned with his coverage) and Lisa takes the mid-market ones. It identifies that two target companies haven't confirmed attendance yet and creates reminder outreach tasks. The final schedule — 47 meetings across 3 days — is generated in 4 hours instead of the usual 3 weeks of email coordination.

---

### Use Case 4: Thought Leadership Content Pipeline

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks differentiate through intellectual capital — sector research, market outlook reports, deal trend analyses. Marketing teams coordinate content production across 20–30 senior bankers who are supposed to contribute but rarely have time. The result: content calendars with 60% of planned pieces never published, outdated market commentary that sits in draft for months, and missed opportunities to position the firm's expertise during market events (e.g., publishing M&A outlook after everyone else already has). The content approval chain — banker draft → marketing edit → compliance review → legal sign-off → publishing — adds weeks of latency.

#### The Solution
monday.com Work Management provides a content pipeline with structured workflows for each content type (market commentary, sector outlook, deal analysis, bylined article, social media post). Each content piece flows through defined stages with SLA timers and escalation automations. AI Agents assist with first-draft generation based on banker input and market data. Compliance pre-screening happens in parallel rather than sequentially. A content calendar dashboard shows planned, in-progress, and published pieces across all sectors, with gap analysis highlighting sectors with low content output.

#### The Outcome
Content publication rate increases from 40% to 80% of planned pieces. Time from concept to publication drops from 6 weeks to 2 weeks. The firm publishes timely market commentary within 48 hours of major market events (vs. 2–3 weeks previously). LinkedIn engagement for banker-authored content increases 3x due to consistent posting cadence.

#### Discovery Questions
1. "How many thought leadership pieces does your firm aim to publish per quarter, and what percentage actually get published on time?"
2. "What's the biggest bottleneck in your content production process — is it getting bankers to write, compliance review, or something else?"
3. "When a major market event happens — a large M&A deal, regulatory change, or market disruption — how quickly can you publish commentary?"
4. "How do you measure the impact of your thought leadership on deal origination and brand positioning?"
5. "Do your bankers actively post on LinkedIn? How does marketing support their social media presence?"

#### Industry Context
Investment banking thought leadership includes sector outlook reports, M&A trend analyses, capital markets updates, and regulatory impact assessments. Senior bankers (MDs, Partners) are expected to be "visible" in their sectors through published commentary and conference speaking. Compliance review of content is mandatory — FINRA Rule 2210 governs communications with the public, and MiFID II has specific requirements for research distribution. "Bylined articles" in publications like Financial Times, WSJ, or trade journals carry significant prestige.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Thought Leadership Pipeline board. Columns: Content Title (text), Author/Banker (people), Content Type (dropdown: Market Commentary, Sector Outlook, Deal Analysis, Bylined Article, LinkedIn Post, White Paper, Podcast), Sector (dropdown: TMT, Healthcare, Industrials, FIG, Energy, Consumer, Cross-Sector), Status (status: Ideation, Banker Drafting, Marketing Edit, Compliance Review, Legal Review, Approved, Published, Killed), Target Publish Date (date), Actual Publish Date (date), Days in Pipeline (formula), Compliance Reviewer (people), Marketing Editor (people), Distribution Channels (dropdown multi-select: Website, LinkedIn, Email, Press, Conference), Engagement Metrics (numbers), Pipeline Attributed $M (numbers). Create groups: Q1 2026 Content, Q2 2026 Content, Evergreen Content, Reactive/Market Events. Add automations: when Status is Banker Drafting for more than 7 days, send reminder to Author; when Status changes to Compliance Review, notify Compliance Reviewer with 3-day SLA; when Status changes to Published, log Actual Publish Date and calculate Days in Pipeline; if any item stuck in same status for 14+ days, escalate to marketing lead. Dashboard: Content Calendar (timeline), Publication Rate gauge (published vs planned), Average Days in Pipeline, Content by Sector distribution, Bottleneck Analysis (items per stage)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ThoughtLeader Ghostwriter
**Agent Purpose:** Generates first drafts of thought leadership content based on banker talking points, market data, and the firm's proprietary deal experience.

**Triggers:**
- New content item created with banker and topic assigned
- Major market event detected (M&A announcement, regulatory change, earnings season)
- Banker submits voice memo or bullet points via integrated form
- Content item has been in "Ideation" for more than 5 days without a draft

**Actions:**
- Generates first draft based on banker's input, recent market data, and firm's deal history in the relevant sector
- Formats content according to firm's style guide and compliance-safe language patterns
- Pre-screens draft against common compliance red flags (forward-looking statements, performance claims, competitor references)
- Suggests distribution strategy based on content type and target audience
- Creates social media derivative content (LinkedIn post summary, tweet thread) from long-form pieces

**Data Required:**
- Banker input (talking points, voice memos, or prior published content)
- Market data feeds (deal activity, market indices, regulatory filings)
- Internal deal database for proprietary insights
- Firm style guide and compliance language guidelines

**Autonomy Level:** Human-in-the-Loop
Agent generates drafts and suggestions; banker reviews for accuracy and voice, marketing edits for polish, compliance reviews for regulatory adherence. All publishing decisions are human-made.

**Example Interaction:**
> Healthcare MD Sarah records a 3-minute voice memo about trends she's seeing in physician practice management M&A after attending a conference. ThoughtLeader Ghostwriter transcribes the memo, cross-references it with the firm's 6 recent healthcare services transactions and Dealogic data showing 40% YoY increase in physician practice M&A volume. It generates a 1,200-word market commentary draft, a 200-word LinkedIn summary, and flags two sentences that compliance will likely question ("unprecedented growth" and a forward-looking market size projection). Sarah reviews, adds a personal anecdote from the conference, and approves. The piece is in compliance review within 24 hours instead of sitting in her "to-do" pile for 3 weeks.

---

### Use Case 5: Alumni & Relationship Network Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banking is a relationship business. Former colleagues who leave for corporate roles become potential clients — a VP who joins a company as CFO is a warm lead for advisory mandates. Banks lose track of alumni movements, fail to leverage warm introductions, and miss signals that a former colleague is now in a position to hire advisors. Marketing's role in maintaining these relationships (event invitations, newsletters, holiday outreach) is manual and inconsistent. Most firms have no systematic way to track the "alumni to client" pipeline.

#### The Solution
monday.com CRM combined with Work Management tracks the firm's alumni network. Each alumni contact has a profile with current role, company, last interaction, relationship strength score, and potential mandate triggers (e.g., new CFO appointment → possible M&A advisory need). Automations monitor for role changes (via LinkedIn Sales Navigator integration) and trigger outreach workflows. Marketing runs structured nurture campaigns — quarterly newsletters, exclusive event invitations, annual dinners — with engagement tracking. When an alumni moves to a target company in a C-suite or board role, an alert goes to the relevant coverage banker.

#### The Outcome
Alumni-sourced deal introductions increase by 50%. Marketing reduces manual effort on alumni tracking by 80%. The firm captures "warm leads" that were previously invisible — identifying 15–20 high-value alumni role changes per quarter that lead to introductory meetings. Alumni event attendance rates improve from 25% to 45% through personalized, targeted invitations.

#### Discovery Questions
1. "How do you currently track where your former colleagues and alumni end up after leaving the firm?"
2. "Can you think of a recent example where a former colleague moved to a company that later became a client? Was that connection made proactively or by chance?"
3. "What kind of alumni engagement programs does your firm run — events, newsletters, outreach?"
4. "How do your bankers learn about executive movements at companies they cover — is it systematic or ad hoc?"
5. "If a former VP joins a $5B company as CFO, how quickly would the right coverage banker know about it?"

#### Industry Context
The "revolving door" in investment banking creates a massive alumni network — bulge-bracket banks have 10,000+ alumni in corporate roles globally. Key movements to track: CFO appointments (buy-side advisory), CEO changes (strategic review potential), board appointments (governance and M&A committees), and PE/VC moves (sponsor relationships). "Warm introductions" through alumni connections have a significantly higher mandate conversion rate than cold outreach. Many banks run formal alumni programs, but most are marketing-light (annual dinner, holiday card).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Alumni Network Tracker using monday CRM. Columns: Contact Name (text), Current Company (text), Current Title (text), Departure Year (numbers), Last Role at Firm (text), Coverage Group (dropdown: TMT, Healthcare, Industrials, FIG, Energy, Consumer), Relationship Owner (people), Last Interaction (date), Relationship Score (status: Hot, Warm, Cool, Cold), Mandate Potential (status: High, Medium, Low, None), Company Revenue $M (numbers), Recent Role Change (checkbox), Notes (long text), LinkedIn URL (link). Create groups: C-Suite Alumni, VP/Director Alumni, Associate Alumni, Board Appointments. Add automations: when Recent Role Change is checked, notify Relationship Owner and relevant coverage group; if Last Interaction is more than 6 months ago, change Relationship Score to Cool; quarterly reminder to review and update all contacts. Dashboard: Alumni Map (by company size and mandate potential), Relationship Health distribution, Recent Movers list, Alumni-to-Mandate Pipeline, Engagement Activity timeline."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AlumniPulse Monitor
**Agent Purpose:** Tracks alumni career movements and triggers proactive outreach when former colleagues land in mandate-relevant positions.

**Triggers:**
- LinkedIn Sales Navigator detects role change for tracked alumni
- Quarterly scheduled review of all alumni contacts
- News alert mentioning alumni name + company in deal context
- Alumni engagement event (opened email, attended webinar, clicked newsletter)

**Actions:**
- Updates alumni profile with new role, company, and title
- Scores mandate potential based on role level, company size, and sector alignment
- Alerts relevant coverage banker with context: "Former VP John Smith just became CFO of MedTech Corp ($3B revenue, Healthcare sector — your coverage)"
- Generates personalized outreach draft for the covering banker
- Adds alumni to relevant nurture campaign based on new role
- Tracks outreach-to-meeting-to-mandate conversion

**Data Required:**
- LinkedIn Sales Navigator integration
- Internal HR/alumni database
- Coverage model (which bankers cover which companies/sectors)
- CRM deal pipeline data

**Autonomy Level:** Escalation-Based
Routine updates are automated. High-value alerts (C-suite moves to large companies) are escalated to senior bankers with recommended actions. Outreach is always human-sent.

**Example Interaction:**
> AlumniPulse detects that former Associate Director Maria Gonzalez, who left the firm in 2023, has been appointed CFO of a $4B industrial manufacturing company. The agent cross-references with the Industrials coverage model and identifies Managing Director Robert Kim as the covering banker. It sends Robert an alert: "Maria Gonzalez (Industrials group, 2019-2023) appointed CFO at Apex Industrial Holdings ($4.2B revenue, 12 facilities). She previously worked on 3 deals with you. Recommend: congratulatory outreach + lunch meeting to discuss their strategic priorities." Robert sends a personal note that afternoon, leading to an advisory conversation about a potential acquisition the company is considering.

---

### Use Case 6: Brand & PR Monitoring for Deal Announcements

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
When the firm announces a closed deal, marketing needs to coordinate tombstone creation, press release drafting, league table notification, website update, social media announcement, and internal communications — often within hours. Simultaneously, marketing monitors competitor deal announcements to update competitive positioning. This reactive work is currently managed through email chains, ad hoc Slack messages, and a shared spreadsheet that nobody consistently updates. Missed or delayed announcements erode brand positioning.

#### The Solution
monday.com Work Management provides a Deal Announcement Playbook — a templated workflow that triggers when a deal closes. Each announcement follows a standardized checklist: press release → compliance review → league table notification → tombstone creation → website update → social media → internal email. Automations ensure nothing falls through the cracks. A parallel board monitors competitor announcements via news feed integrations, automatically categorizing them by sector, deal type, and size, feeding into the competitive intelligence dashboard.

#### The Outcome
Deal announcement turnaround drops from 5 business days to 1 business day. Zero missed announcements (previously 10–15% of deals had delayed or missing marketing coverage). Competitive monitoring becomes systematic rather than ad hoc, with marketing producing weekly competitor activity summaries automatically.

#### Discovery Questions
1. "When a deal closes, what's the process for coordinating the public announcement across all channels?"
2. "How often do deal announcements get delayed because of bottlenecks in the approval chain?"
3. "How do you currently track competitor deal activity, and how does that intelligence flow to your coverage teams?"
4. "Has a delayed announcement ever cost you league table credit or competitive positioning?"

#### Industry Context
Deal announcements in investment banking follow strict protocols. Tombstone ads (historically placed in newspapers, now primarily digital) formalize the bank's role. League table providers require notification within specific windows to receive credit. Press releases must be coordinated with the client company. Confidentiality is paramount — premature disclosure can violate securities laws and damage client relationships.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Deal Announcement Tracker board. Columns: Deal Name (text), Client Company (text), Deal Type (dropdown: M&A, IPO, Follow-On, Debt Issuance, Leveraged Buyout, Restructuring), Deal Value $M (numbers), Bank Role (dropdown: Lead Left, Joint Bookrunner, Co-Manager, Advisor, Sole Advisor), Close Date (date), Announcement Status (status: Pending Close, Drafting PR, Compliance Review, Client Approval, Published, Complete), Press Release (file), Tombstone Created (checkbox), League Tables Notified (checkbox: Dealogic, Refinitiv, Bloomberg), Website Updated (checkbox), Social Media Posted (checkbox), Internal Comms Sent (checkbox), Lead Banker (people), Marketing Lead (people). Create groups: Pending Announcements, In Progress, Published This Month, Archive. Add automations: when Close Date arrives, create announcement checklist sub-items automatically; when all checkboxes are checked, move to Complete; if any checkbox unchecked after 5 business days from Close Date, escalate to Marketing Lead. Dashboard: Announcement Pipeline (timeline), Completion Rate gauge, Average Announcement Turnaround, Deals by Type pie chart."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DealWire Publisher
**Agent Purpose:** Orchestrates the end-to-end deal announcement process from close to full publication across all channels.

**Triggers:**
- Deal item status changes to "Closed" in deal tracking board
- Compliance approves press release draft
- Client company issues their own announcement (detected via news monitoring)
- League table submission deadline approaching

**Actions:**
- Generates draft press release from deal data (parties, value, role, sector context)
- Creates tombstone graphic template with deal details
- Submits league table notifications to Dealogic, Refinitiv, and Bloomberg
- Drafts social media posts (LinkedIn, Twitter) for firm and banker accounts
- Sends internal announcement email to relevant coverage and product groups
- Updates firm website deal page and sector credentials

**Data Required:**
- Deal database (all transaction details)
- Press release templates and compliance-approved language
- League table submission portals and credentials
- Social media publishing access
- Website CMS access

**Autonomy Level:** Human-in-the-Loop
Drafts are auto-generated; compliance and client approval gates are human. Publishing only occurs after explicit human approval.

**Example Interaction:**
> The Industrials M&A team closes a $2.8B acquisition advisory. DealWire immediately generates a press release draft using the deal terms, populates the tombstone template, and pre-fills league table submission forms for all three providers. It posts the draft to the compliance review queue with a note: "Client announcement expected Thursday 8 AM — our PR should be ready to publish within 2 hours." Compliance reviews and approves by Wednesday evening. Thursday at 8:15 AM, the client issues their press release. DealWire detects it, notifies the marketing lead, and within 30 minutes, the firm's announcement goes live across all channels — website, LinkedIn, league table portals, and internal email.

---

### Use Case 7: RFP & Beauty Contest Response Management

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
When a company invites banks to compete for a mandate (a "beauty contest" or "bake-off"), marketing supports the response with credentials, case studies, team bios, and presentation materials. These RFP responses are high-stakes — winning a single mandate can generate $5–50M in fees. Yet the response process is chaotic: bankers request materials last-minute, prior responses aren't cataloged for reuse, and teams recreate content that already exists elsewhere. A typical beauty contest response requires 40–60 hours of collective effort across banking, marketing, and compliance.

#### The Solution
monday.com Work Management provides a structured RFP response workflow. A content library board stores reusable components — team bios, sector credentials, methodology descriptions, case studies, compliance-approved language blocks. Each RFP response is managed as a project with tasks, owners, deadlines, and dependencies. AI Agents search the content library for relevant components, assembling a first draft response that the team then customizes. Post-submission tracking monitors outcomes (win/loss) and captures feedback for continuous improvement.

#### The Outcome
RFP response assembly time reduced from 60 hours to 20 hours. Content reuse rate increases from 15% to 60%. Win rate improves by 10–15% through more polished, consistent, and timely responses. Marketing builds an institutional knowledge base that gets smarter with each response.

#### Discovery Questions
1. "How many competitive pitches or beauty contests does your firm participate in per quarter?"
2. "When you're assembling a pitch response, how much time is spent finding and reformatting content that already exists somewhere in the firm?"
3. "Do you track your win/loss rate on competitive mandates, and do you capture post-mortem feedback on what worked and what didn't?"
4. "How do you ensure consistency in how your firm's capabilities and track record are presented across different pitch responses?"

#### Industry Context
A "beauty contest" (or "bake-off") is when a company invites 3–5 banks to pitch for an advisory mandate. Each bank presents their credentials, sector expertise, valuation perspectives, and proposed deal team. These are high-stakes, relationship-defining events — the winning bank earns fees and deepens the client relationship for future mandates. Marketing's role is to ensure the presentation materials are compelling, current, and compliant. Common beauty contest materials include: credentials deck, case studies of comparable transactions, team bios, sector research, and a preliminary valuation framework.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an RFP & Beauty Contest Response board. Columns: Opportunity Name (text), Client Company (text), Mandate Type (dropdown: M&A Sell-Side, M&A Buy-Side, IPO, Debt Financing, Restructuring, Fairness Opinion), Estimated Fee $M (numbers), Competing Banks (text), Pitch Date (date), Status (status: Received, Content Assembly, Draft Review, Compliance Review, Rehearsal, Submitted, Won, Lost), Lead Banker (people), Marketing Support (people), Response Components (dropdown multi-select: Credentials Deck, Team Bios, Case Studies, Valuation Preview, Sector Research, Methodology, References), Content Reuse % (numbers), Hours Invested (numbers), Outcome (status: Won, Lost, Withdrawn, Pending), Win/Loss Reason (long text). Create groups: Active RFPs, Submitted — Awaiting Decision, Won, Lost — Lessons Learned. Sub-items for each RFP: individual content components with owners and deadlines. Add automations: when new RFP created, generate standard task checklist from template; 48 hours before Pitch Date if Status is not Submitted, escalate to Lead Banker; when Outcome changes to Won or Lost, prompt for Win/Loss Reason. Dashboard: Active RFPs timeline, Win Rate gauge, Average Response Time, Hours per RFP trend, Content Reuse Rate, Fee Pipeline from active pitches."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PitchPerfect Assembler
**Agent Purpose:** Searches the firm's content library to assemble first-draft RFP responses, matching relevant credentials, case studies, and team bios to the specific opportunity.

**Triggers:**
- New RFP item created with mandate type and sector populated
- Content component sub-items created (each triggers a library search)
- Banker adds specific requirements or client context to the RFP item
- Deadline approaching with incomplete components flagged

**Actions:**
- Searches content library for relevant credentials, case studies, and team bios matching the mandate type, sector, and deal size
- Assembles first-draft response document with recommended components
- Highlights gaps where no relevant content exists (triggers creation tasks)
- Compares current response against previous winning submissions for similar mandates
- Calculates content reuse percentage and estimates remaining hours
- Post-submission: logs outcome and captures learnings for future responses

**Data Required:**
- Content library board with tagged, searchable components
- Historical RFP responses with outcomes
- Team bio database (current, compliance-approved)
- Deal tombstone library for credentials

**Autonomy Level:** Human-in-the-Loop
Agent assembles and recommends; bankers customize for the specific client relationship context. Final review and submission are always human-driven.

**Example Interaction:**
> A $6B consumer products company invites the firm to pitch for a sell-side M&A mandate. PitchPerfect immediately searches the content library: it finds 4 relevant consumer M&A tombstones, identifies the team bio for the Consumer MD who covered this company historically, and locates a case study from a comparable $4B consumer sell-side two years ago. It flags a gap: no recent consumer sector outlook piece exists. It creates a task for the ThoughtLeader Ghostwriter to generate a market commentary. The first-draft response — 80% assembled from library components — is ready for banker review within 4 hours. The team spends their time on the custom valuation perspective and client-specific messaging rather than hunting for existing content.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Tombstone | Standardized deal summary showing the bank's advisory or underwriting role, used in credentials and advertising |
| League Table | Rankings of investment banks by deal volume and value, published by Dealogic, Refinitiv, and Bloomberg |
| Beauty Contest / Bake-Off | Competitive pitch process where multiple banks present to win an advisory mandate |
| Credentials Deck / Cred Deck | Presentation showcasing the bank's deal experience, sector expertise, and team for a specific opportunity |
| Pitch Book | Comprehensive presentation combining credentials, market analysis, and preliminary valuation for a prospective client |
| Mandate | Formal engagement to advise on a transaction (M&A, IPO, debt issuance, etc.) |
| Coverage Group | Sector-focused banking team (e.g., TMT, Healthcare) responsible for client relationships in that industry |
| Product Group | Transaction-type focused team (M&A, ECM, DCM, Leveraged Finance) providing execution expertise |
| NDR (Non-Deal Roadshow) | Marketing event where a company's management presents to investors without an associated securities offering |
| League Table Credit | Attribution of a deal to a bank in league table rankings; depends on role and provider methodology |
| Bulge Bracket | Largest global investment banks (Goldman Sachs, J.P. Morgan, Morgan Stanley, etc.) |
| Middle Market / Boutique | Smaller advisory firms specializing in mid-sized transactions or specific sectors |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Marketing Officer / Head of Marketing | Overall brand strategy, budget allocation, team leadership | Decision-maker |
| Director of Marketing Communications | Content strategy, thought leadership, PR coordination | Decision-maker (for marketing tools) |
| Credentials & Pitch Book Manager | Oversees deck production, tombstone library, quality control | Key Influencer / Primary User |
| Marketing Analyst / Associate | Produces credentials decks, manages data, coordinates events | Primary User |
| Head of Compliance (Marketing) | Reviews all external communications for regulatory adherence | Gatekeeper / Veto Power |
| Managing Director (Coverage) | Requests pitch books, provides content input, approves final materials | Internal Customer / Influencer |
| Chief Operating Officer | Oversees operational efficiency, technology investments | Budget Approver |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales / Coverage Banking | Primary internal customer for marketing materials; deal origination tracking | CRM integration for relationship and pipeline management |
| Compliance & Legal | Mandatory review of all external communications | Workflow automation to reduce review bottlenecks |
| IT | Systems integration, data management, security requirements | Platform consolidation opportunity |
| Product Groups (M&A, ECM, DCM) | Content contributors, expertise source for thought leadership | Cross-board collaboration and content workflows |
| Human Resources | Alumni tracking, recruitment marketing, employer brand | Alumni network management integration |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Pitchbook + Capital IQ / S&P | Data and research platforms for deal sourcing and analysis | monday.com doesn't replace data sources but centralizes workflow around them; integration opportunity |
| Seismic / Highspot | Sales enablement and content management for pitch materials | monday.com provides broader workflow management with content library capabilities built in |
| Salesforce | CRM for relationship and pipeline tracking | monday CRM is more flexible for IB's unique relationship-driven model; faster to customize |
| SharePoint / Confluence | Document storage and collaboration | monday.com adds structured workflow, automation, and visibility that static document stores lack |
| Custom internal tools | Banks often build bespoke pitch book and league table tools | monday.com replaces maintenance burden with configurable, no-code platform |
| Bloomberg Terminal | Financial data, news, analytics | Complementary — monday.com orchestrates work; Bloomberg provides market data |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We're too regulated — we need purpose-built compliance tools" | monday.com's structured workflows actually strengthen compliance by creating auditable approval chains, enforcing review gates, and ensuring nothing bypasses the process. Unlike email-based approvals, every action is logged and traceable. |
| "Our bankers won't adopt another tool" | monday.com sits behind the scenes for bankers — they submit requests via simple forms and get delivered materials. The heavy lifting happens in marketing's workflow. Bankers see faster turnaround, not a new tool to learn. |
| "We already have Salesforce for CRM" | Salesforce is great for structured sales pipelines, but IB relationships are nuanced — they span alumni networks, conference interactions, and coverage models. monday CRM flexibly models these relationship types alongside marketing workflows in one platform. |
| "Our IT security requirements are extremely strict" | monday.com is SOC 2 Type II certified, GDPR compliant, and supports enterprise SSO, data residency controls, and granular permissions — meeting the security bar for financial institutions including banks. |
| "Pitch book production is too specialized for a general platform" | That's exactly why monday.com's flexibility matters — you configure it to match your exact process (sectors, deal types, approval chains) without the rigidity of a one-size-fits-all pitch book tool. Plus, AI capabilities accelerate the assembly process. |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for financial services marketing automation case studies]
- [Placeholder for investment banking credentials management examples]
- [Placeholder for content pipeline acceleration metrics]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
