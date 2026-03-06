# Investment Banking × Sales Playbook

## Overview

Sales within investment banking is a fundamentally different discipline from traditional B2B or B2C selling. Known internally as "coverage," the sales function in investment banking revolves around relationship-driven origination — identifying, cultivating, and converting advisory mandates (M&A, capital markets, restructuring) and financing transactions. Senior bankers (Managing Directors and Directors) maintain coverage of named accounts, often organized by industry verticals or geographic regions, and are compensated heavily on deal fees rather than recurring revenue. The sales motion is long-cycle, high-touch, and deeply consultative, with deal timelines spanning months to years.

Investment banking sales teams operate under intense competitive pressure. League table rankings (published by Dealogic, Refinitiv, Bloomberg) publicly quantify market share by deal volume, fees, and product type. Every pitch, every credential deck, every relationship touchpoint is a battle for mindshare with CFOs, treasurers, board members, and private equity sponsors. The cost of a lost mandate is measured in millions of dollars in foregone fees, making pipeline visibility, relationship intelligence, and coordination across coverage teams mission-critical.

Organizationally, the sales function intersects deeply with product groups (M&A, ECM, DCM, Leveraged Finance), industry groups, and capital markets desks. A single deal often requires coordination among 10-20 professionals across these groups. Managing this matrix — tracking pipeline, logging client interactions, coordinating pitches, and ensuring no relationship falls through the cracks — is where most banks still rely on a patchwork of spreadsheets, legacy CRM systems (often poorly adopted Salesforce instances), and tribal knowledge stored in senior bankers' heads.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Junior bankers spend 30-40% of time on pipeline tracking, CRM updates, and pitch logistics instead of deal execution |
| 2 | Consolidate Tech Stack with AI | High | Most banks run fragmented stacks: Salesforce (underutilized), DealCloud/Navatar, Excel trackers, shared drives for credentials — enormous integration tax |
| 3 | Scale Impact Without Overhead | Medium-High | Coverage teams need to cover more accounts per banker as fee pools compress and headcount freezes persist post-2023 layoffs |

## Prioritized Use Cases

---

### Use Case 1: Deal Pipeline & Mandate Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banks struggle with pipeline visibility across their coverage universe. Senior MDs track their deals in personal spreadsheets or in their heads. Leadership (Group Heads, Division Heads) lack a real-time view of active mandates, pipeline stages, and probability-weighted fee forecasts. Weekly pipeline meetings devolve into verbal updates because the CRM is perpetually stale. When a banker leaves, institutional knowledge of relationships and deal status walks out the door with them.

#### The Solution
monday.com CRM configured as a deal pipeline tracker with custom stages reflecting IB deal lifecycle: Initial Conversation → Pitch Scheduled → Pitch Delivered → Mandate Won → Engagement Letter Signed → Active Execution → Closed. Custom columns for estimated fee (retainer + success fee), deal type (M&A sell-side, M&A buy-side, IPO, follow-on, debt placement, restructuring), target/acquirer details, and competitive intelligence (which other banks are pitching). Dashboard views with probability-weighted fee pipeline by quarter, by industry group, and by coverage banker. mondayDB for querying historical deal data and win/loss patterns.

#### The Outcome
- 60-80% reduction in time spent on pipeline reporting
- Real-time fee forecast accuracy improving from ±40% to ±15%
- Zero knowledge loss on banker departures — full deal history preserved
- Leadership gains instant visibility into $500M+ pipeline without waiting for weekly meetings

#### Discovery Questions
1. "How do your MDs currently report pipeline to group heads — is it a weekly email, a meeting, or a system they log into?"
2. "When a managing director leaves or moves groups, how much pipeline intelligence do you estimate walks out the door?"
3. "How do you currently calculate probability-weighted fee forecasts across the division?"
4. "What's the adoption rate of your current CRM among senior bankers — are MDs actually logging their interactions?"
5. "How many active mandates does a typical coverage team juggle simultaneously, and how do they prioritize?"

#### Industry Context
In investment banking, "pipeline" doesn't mean leads — it means active advisory mandates and potential engagements worth $1M-$50M+ in fees each. Deal stages are non-linear; a pitch might go dormant for 6 months then reactivate when market conditions change. League table credit allocation (who gets credit for a deal) is deeply political and tracked meticulously. The SE should understand that IB "sales" is relationship-based origination, not transactional selling.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Investment Banking Deal Pipeline board. Columns: Deal Name (text), Client Company (text), Deal Type (dropdown: M&A Sell-Side, M&A Buy-Side, IPO, Follow-On Offering, Debt Placement, Leveraged Finance, Restructuring, Other Advisory), Stage (status: Initial Conversation, Pitch Scheduled, Pitch Delivered, Mandate Won, Engagement Letter Signed, Active Execution, Closed Won, Closed Lost, Dormant), Coverage Banker (people), Industry Group (dropdown: TMT, Healthcare, Industrials, FIG, Consumer & Retail, Energy & Power, Real Estate), Estimated Fee $M (numbers), Fee Probability % (numbers), Weighted Fee $M (formula: Estimated Fee × Probability), Fee Type (dropdown: Retainer Only, Success Fee Only, Retainer + Success, Monthly Advisory), Competing Banks (text), Last Client Touchpoint (date), Next Action (text), Next Action Date (date), Engagement Letter Status (status: Not Sent, Sent, Under Review, Signed). Add a Dashboard view with: total weighted pipeline by quarter (chart), pipeline by deal type (chart), pipeline by industry group (chart), top 10 deals by estimated fee (table), deals with no touchpoint in 30+ days (widget). Add a Kanban view grouped by Stage. Add an automation: when Last Client Touchpoint is more than 21 days ago and Stage is not Closed Won/Closed Lost/Dormant, notify the Coverage Banker 'Client touchpoint overdue — schedule follow-up.' Add another automation: when Stage changes to Mandate Won, notify the group channel and move to Engagement Letter Status = Not Sent."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pipeline Intelligence Agent
**Agent Purpose:** Automatically enrich, update, and analyze the deal pipeline to surface at-risk mandates and fee forecast anomalies.

**Triggers:**
- New deal item created on Pipeline board
- Weekly schedule (Monday 6 AM) for pipeline health scan
- When Last Client Touchpoint exceeds 30 days on active deals
- When Stage changes to any value
- Manual trigger by coverage banker requesting pipeline summary

**Actions:**
- Flag deals with stale touchpoints and generate recommended next actions based on deal type and stage
- Auto-calculate quarterly fee forecasts with confidence intervals and compare to prior week
- Generate weekly pipeline digest email per coverage group (deals won, deals lost, new opportunities, at-risk mandates)
- Cross-reference new deals against existing pipeline to identify potential conflicts of interest (same target company, competing mandates)
- Surface "dormant revival" opportunities — deals marked dormant 6+ months ago where market conditions have shifted (rate changes, sector M&A activity)
- Update probability scores based on historical win rates by deal type and stage duration

**Data Required:**
- Deal pipeline board data (all columns)
- Historical closed deals (won and lost) for pattern analysis
- Coverage banker activity logs
- Market data feeds (optional integration with Refinitiv/Bloomberg for sector activity signals)

**Autonomy Level:** Human-in-the-Loop
Auto-generates reports and flags risks, but all client outreach decisions and probability adjustments require banker approval. Conflict-of-interest flags escalate immediately to compliance and group head.

**Example Interaction:**
> On Monday morning at 6 AM, the Pipeline Intelligence Agent scans the entire TMT coverage group's pipeline. It identifies that the Acme Corp sell-side mandate ($2.8M estimated fee, currently in "Pitch Delivered" stage) has had no client touchpoint in 34 days. The agent creates a notification for the coverage MD: "Acme Corp engagement appears stalled — last contact was Dec 15 with CFO Lisa Park. Recommend scheduling a market update call; comparable transactions in SaaS vertical have increased 22% this quarter, providing a natural conversation opener."
>
> Simultaneously, the agent notices that a new deal was added — "Beta Inc. Buy-Side Advisory" — and cross-references it against active pipeline. It flags that another team is currently running a sell-side process for a company in Beta's acquisition target space, creating a potential conflict. The agent immediately notifies the Group Head and Compliance with details.
>
> The agent then generates the weekly TMT pipeline digest: "Pipeline: $47.2M weighted (up $3.1M WoW). 2 mandates won ($8.5M combined fee). 1 mandate lost to Goldman Sachs (Delta Corp IPO). 4 deals flagged at-risk due to stale engagement. Forecast confidence: 72%."

---

### Use Case 2: Pitch Book & Credentials Workflow

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Pitch book production is one of the most labor-intensive activities in investment banking. Junior bankers (analysts and associates) routinely work until 2-3 AM assembling pitch decks — pulling deal credentials, updating market data, formatting slides, and managing version control across multiple reviewers. A single pitch might go through 15-20 revision cycles. The coordination between the coverage team (who owns the relationship), the product group (who provides technical expertise), and the graphics/presentation team creates a logistical nightmare. Pitches are often assembled from scratch because there's no centralized, searchable repository of reusable content.

#### The Solution
monday.com Work Management as a pitch production workflow. Each pitch is a project with structured phases: Brief Received → Research & Data Pull → First Draft → MD Review → Client Customization → Final Review → Print/Send → Post-Pitch Debrief. Task assignments for each section of the pitch (credentials, market overview, valuation analysis, team bios, transaction structure). File management with version tracking. Timeline view for managing multiple concurrent pitches. Integration with shared drives for template libraries. Automated status notifications when sections are completed or reviews are needed.

#### The Outcome
- 40-50% reduction in pitch production time (from 40+ hours to 20-25 hours per pitch)
- Elimination of version control chaos — single source of truth for each pitch
- Reusable credentials library reduces "starting from scratch" syndrome
- Senior banker review cycles shortened from 3-4 days to 1-2 days with automated notifications
- Analyst/associate burnout reduction — reclaim 10-15 hours per week currently spent on coordination overhead

#### Discovery Questions
1. "How many pitches does a typical coverage team produce per month, and what's the average turnaround time from brief to delivery?"
2. "Do your analysts spend more time on actual analysis or on assembling and formatting pitch books?"
3. "When an MD requests changes at 11 PM, how does that cascade through the team — is there a system or is it emails and texts?"
4. "Do you have a centralized credentials database, or do analysts hunt through old pitch books to find relevant deal tombstones?"
5. "How often do pitches get delayed or miss deadlines due to coordination breakdowns between coverage and product groups?"

#### Industry Context
"Pitch book" (or "pitchbook") is the primary sales collateral in IB — typically a 30-80 page PowerPoint deck customized for a specific client meeting. "Credentials" (or "tombstones") are summaries of completed deals that demonstrate the bank's track record. The MD review cycle is sacred and unpredictable — an MD might request wholesale changes at midnight before a 9 AM meeting. "Staffing" a pitch means assigning analyst/associate resources, which is a constant source of contention when multiple deals compete for the same junior talent.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Pitch Book Production Tracker. Columns: Pitch Name (text), Target Client (text), Meeting Date (date), Deal Type (dropdown: M&A Advisory, ECM, DCM, Restructuring, General Capabilities, Sector Overview), Coverage MD (people), Product Group Lead (people), Assigned Analyst (people), Assigned Associate (people), Stage (status: Brief Received, Research & Data Pull, First Draft In Progress, MD Review, Revisions, Client Customization, Final QC, Ready to Print, Delivered, Post-Pitch Debrief), Priority (status: Standard, Rush 48hr, Rush 24hr, Emergency Same-Day), Sections Completed (progress tracking), Credentials Needed (numbers), Credentials Found (numbers), Draft Version (numbers), Last Updated (date), Link to Deck (link), Debrief Notes (long text). Create groups: Active Pitches, In Review, Completed This Month, Templates. Add a Timeline view showing pitch schedules with Meeting Date deadlines. Add automations: when Stage changes to 'MD Review', notify Coverage MD with 'Pitch ready for your review: {Pitch Name} for {Target Client} — meeting on {Meeting Date}.' When Meeting Date is 2 days away and Stage is not 'Ready to Print' or later, send urgent notification to all assigned people: 'URGENT: {Pitch Name} for {Target Client} is behind schedule — meeting in 2 days.' When Stage changes to 'Delivered', move item to Completed This Month group."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pitch Accelerator Agent
**Agent Purpose:** Automate credential retrieval, first-draft assembly, and review cycle management to dramatically reduce pitch production time.

**Triggers:**
- New pitch item created (Brief Received)
- Stage changes to "Research & Data Pull"
- Stage changes to "MD Review" (starts review timer)
- Meeting Date minus 48 hours (deadline check)
- Manual request: "Find credentials for [deal type] in [sector]"

**Actions:**
- Auto-search credentials database for relevant deal tombstones based on deal type, sector, and client profile; populate Credentials Found
- Generate first-draft pitch outline based on deal type template and client profile
- Track MD review cycle time; if review exceeds 24 hours, send gentle escalation
- Auto-assemble "market conditions" section with latest comparable transaction data and sector commentary
- When pitch is delivered, auto-create post-pitch debrief task and follow-up reminder for 48 hours later
- Compile weekly pitch production metrics: pitches completed, average production time, bottleneck analysis

**Data Required:**
- Historical pitch library and credentials database
- Deal pipeline data (for client context)
- Team availability/workload data
- Market data for comparable transactions

**Autonomy Level:** Human-in-the-Loop
Agent assembles and suggests; all content must be reviewed by assigned associate and approved by MD before client delivery. Credential matching is automated but analyst verifies relevance.

**Example Interaction:**
> A coverage MD creates a new pitch: "Gamma Industries — Sell-Side M&A Advisory" with a meeting date 5 business days out. The Pitch Accelerator Agent immediately searches the credentials database and finds 14 relevant industrials M&A transactions the bank completed in the last 3 years. It ranks them by relevance (same sub-sector, similar deal size, same geography) and populates the credentials section.
>
> The agent then generates a first-draft outline: executive summary, credentials (pre-populated), market overview (with latest industrial sector M&A volume data), preliminary valuation framework, and proposed transaction timeline. It assigns sections to the analyst and associate with suggested completion times based on the meeting date.
>
> When the MD hasn't reviewed the draft 28 hours after it was submitted, the agent sends a discreet notification: "Draft for Gamma Industries pitch is awaiting your review — meeting is in 3 days. The team is standing by for revisions."

---

### Use Case 3: Client Relationship Intelligence (Coverage CRM)

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banking relationships are the franchise. Yet most banks have abysmal CRM adoption — senior bankers view logging calls and meetings as beneath them, and the data that does exist is fragmented across Outlook calendars, personal contact lists, and expense reports. When a bank wants to answer basic questions like "Who in our firm has the strongest relationship with the CFO of Target Corp?" or "Which clients haven't we contacted in 90 days?", it requires manual detective work across multiple MDs' memories and assistants' calendars. This relationship intelligence gap costs banks mandates they should have won.

#### The Solution
monday.com CRM as a lightweight, banker-friendly relationship management system. Contact records linked to company accounts with relationship strength scoring. Activity logging that's frictionless — integration with Outlook/Gmail to auto-capture meetings and emails (with banker opt-in). Relationship mapping showing connections between bankers and client executives across the coverage universe. Dashboard showing "coverage gaps" — accounts with declining engagement, key contacts who've changed roles, and whitespace opportunities (clients using the bank for one product but not others).

#### The Outcome
- 3x improvement in CRM adoption through friction-free logging
- Identification of 15-20% more cross-sell opportunities per quarter through relationship mapping
- Zero "surprise" relationship lapses — proactive alerts on declining engagement
- New bankers ramp 50% faster with full relationship context at their fingertips
- Institutional relationship memory survives personnel changes

#### Discovery Questions
1. "If I asked your Group Head right now which clients haven't been contacted in 90 days, how quickly could they answer — and how confident would they be in the data?"
2. "When you're competing for a mandate, how do you determine which banker in your firm has the warmest path to the decision-maker?"
3. "How do you currently track when a key client contact changes roles — CFO moves to another company, new board member appointed?"
4. "What's your cross-sell motion look like? If your M&A team wins a mandate, how does the DCM team know to follow up on financing?"
5. "How do new MDs hired from competitor banks bring their relationships into your institutional memory?"

#### Industry Context
"Coverage" in IB means named-account responsibility — an MD "covers" specific companies or a sector. "Relationship mapping" tracks which bankers know which executives (CEO, CFO, Treasurer, Head of Corp Dev, Board members, PE sponsors). "Wallet share" means the percentage of a client's total banking fees that go to your bank. "Cross-sell" means introducing additional product groups (e.g., a client using M&A advisory starts using the bank for debt underwriting). IB relationship data is intensely political — MDs guard their relationships jealously.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Investment Banking Coverage CRM. Create two connected boards: 1) Client Companies board with columns: Company Name (text), Sector (dropdown: TMT, Healthcare, Industrials, FIG, Consumer & Retail, Energy & Power, Real Estate, Diversified), Sub-Sector (text), Company Size — Revenue $B (numbers), Public/Private (dropdown: Public, Private, PE-Backed, Family-Owned, Government), Coverage MD (people), Coverage Team (people), Relationship Tier (status: Tier 1 Strategic, Tier 2 Active, Tier 3 Opportunistic, Dormant), Last Touchpoint Date (date), Next Scheduled Meeting (date), Active Mandates (numbers), Historical Fee Revenue $M (numbers), Wallet Share Estimate % (numbers), Key Contacts (text). 2) Interaction Log board with columns: Date (date), Client Company (connect board), Contact Name (text), Contact Title (text), Interaction Type (dropdown: In-Person Meeting, Phone Call, Email, Conference/Event, Dinner, Deal-Related, Pitch Meeting), Banker (people), Notes (long text), Follow-Up Required (checkbox), Follow-Up Date (date), Follow-Up Owner (people). On the Client Companies board, add a Dashboard view with: clients by tier (chart), clients with no touchpoint in 60+ days (table), top 20 clients by historical fee revenue (chart), coverage gaps by sector (chart). Add automation on Interaction Log: when a new interaction is logged, update the Last Touchpoint Date on the connected Client Company. Add automation: when Last Touchpoint Date on Client Companies is more than 60 days ago and Relationship Tier is Tier 1 or Tier 2, notify Coverage MD: 'Relationship alert: {Company Name} has had no contact in 60+ days.'"

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Relationship Intelligence Agent
**Agent Purpose:** Continuously monitor and enrich client relationships, surface engagement risks, and identify cross-sell opportunities across the coverage universe.

**Triggers:**
- Daily scan at 7 AM for engagement anomalies
- New interaction logged on Interaction Log board
- Key contact role change detected (via news monitoring integration)
- Quarterly relationship health review (first Monday of quarter)
- Manual query: "Who has the best path to [Contact Name] at [Company]?"

**Actions:**
- Generate daily "Relationship Risk" alerts for Tier 1/2 accounts with declining engagement frequency
- Auto-detect cross-sell opportunities: when a client is active with one product group, flag potential for adjacent products based on peer company patterns
- Monitor news for client executive changes (CFO departures, new board appointments, PE acquisitions) and alert coverage teams
- Generate quarterly relationship health scorecards per coverage MD showing: accounts covered, engagement frequency, mandate conversion rate, wallet share trends
- Map relationship paths: "To reach [Target Contact], your best path is through [Banker A] who met them at [Event] on [Date]"
- Track "share of voice" — how often your bank is mentioned in client conversations vs. competitors

**Data Required:**
- Client Companies and Interaction Log boards
- Email/calendar integration (opt-in, metadata only)
- News feed for client company monitoring
- Historical deal and fee data
- Industry conference attendee lists

**Autonomy Level:** Escalation-Based
Routine monitoring and alerting is fully autonomous. Relationship recommendations and cross-sell suggestions are delivered to bankers for action. Executive change alerts auto-create follow-up tasks but don't initiate outreach.

**Example Interaction:**
> The Relationship Intelligence Agent detects that Global Logistics Corp (Tier 1 account, $12.3M in historical fees) has had zero logged interactions in the past 74 days. It cross-references this with news and discovers that Global Logistics just appointed a new CFO — Jennifer Walsh, previously CFO of TransPort Holdings. The agent searches relationship data and finds that MD Sarah Chen met Jennifer Walsh at the Industrials Conference in September and logged a positive interaction. The agent sends a notification: "🚨 Tier 1 Alert: Global Logistics Corp — 74 days with no contact. NEW CFO: Jennifer Walsh (formerly TransPort Holdings). Your best relationship path: Sarah Chen met Walsh at the September Industrials Conference. Recommend Sarah schedule an introductory meeting within 2 weeks. Cross-sell opportunity: Global Logistics uses us for M&A advisory but not debt capital markets — peer company FreightMax recently refinanced $2B through our DCM team."

---

### Use Case 4: League Table & Competitive Intelligence Tracker

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
League tables are the scoreboard of investment banking. Published quarterly by Dealogic, Refinitiv, and Bloomberg, they rank banks by deal count, deal volume, and fees across every product and geography. Every pitch references league table position, and every group head obsesses over rankings. Yet tracking competitive intelligence — who's winning which mandates, which banks are gaining or losing share, which bankers moved to competitors — is largely manual. Analysts spend hours scraping league table data, cross-referencing press releases, and building competitive positioning slides for pitches and management reporting.

#### The Solution
monday.com Work Management as a competitive intelligence hub. Board tracking competitor deal announcements with structured data: competitor bank, deal type, client, deal size, sector. League table position tracking over time with historical trending. Competitive threat board for tracking banker movements (departures to/arrivals from competitors). Dashboard combining internal pipeline data with external competitive data to show market share trends and positioning.

#### The Outcome
- 80% reduction in time spent manually compiling competitive intelligence
- Real-time league table position awareness without waiting for quarterly publications
- Proactive identification of competitive threats (banker poaching, mandate losses)
- Pitch books include current competitive positioning assembled in minutes, not hours
- Strategic hiring informed by competitor talent movements

#### Discovery Questions
1. "How long does it take your team to prepare the competitive landscape section of a pitch book today?"
2. "When a competitor wins a mandate you were pursuing, how do you capture and learn from that loss?"
3. "How do you track when senior bankers at competitor firms change roles — is that systematic or anecdotal?"
4. "How frequently does leadership review league table positioning, and what's the process for assembling that data?"
5. "Do you have a centralized place where anyone in the group can see recent competitor deal announcements in your sector?"

#### Industry Context
"League tables" are published rankings of banks by M&A advisory volume, equity underwriting, debt underwriting, etc. Banks obsess over league table position because clients use rankings to shortlist banks for mandates. "Bookrunner" credit means the bank led the deal. "League table credit" allocation has specific rules — full credit vs. shared credit depending on role. The SE should know that being #3 vs. #5 in a league table can mean the difference between getting invited to pitch or not.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Competitive Intelligence Tracker for investment banking. Create two boards: 1) Competitor Deal Flow board with columns: Announcement Date (date), Competitor Bank (dropdown: Goldman Sachs, Morgan Stanley, JP Morgan, Bank of America, Citi, Barclays, Deutsche Bank, UBS, Credit Suisse, Jefferies, Lazard, Evercore, Centerview, PJT Partners, Moelis, Other), Client Company (text), Deal Type (dropdown: M&A Sell-Side, M&A Buy-Side, IPO, Follow-On, Investment Grade Debt, High Yield Debt, Leveraged Loan, Restructuring), Deal Size $M (numbers), Sector (dropdown: TMT, Healthcare, Industrials, FIG, Consumer & Retail, Energy & Power, Real Estate), Our Bank's Role (status: Not Involved, Lost Mandate, Participated, Not Invited), Source (dropdown: Press Release, League Table, Market Intelligence, Relationship Feedback), Notes (long text). 2) Talent Movement board with columns: Banker Name (text), From Bank (text), To Bank (text), Title (dropdown: Analyst, Associate, VP, Director, MD, Group Head), Sector/Group (text), Date (date), Impact Assessment (status: High — Strategic Threat, Medium — Monitor, Low — Minimal Impact), Notes (long text). Add a Dashboard on the Competitor Deal Flow board with: deals by competitor (chart), deals by sector (chart), our win/loss rate by deal type (chart), monthly deal volume trend (chart), mandates we lost (filtered table). Add automation: when Our Bank's Role is 'Lost Mandate', create a notification to the Group Head: 'Competitive loss: {Client Company} {Deal Type} went to {Competitor Bank}. Schedule win/loss debrief.'"

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Market Intelligence Agent
**Agent Purpose:** Automatically track competitor deal activity, talent movements, and league table trends to keep the coverage team competitively informed.

**Triggers:**
- Daily morning scan (6 AM) for new deal announcements
- Weekly league table position update (Monday)
- When a new item is added to Talent Movement board
- When Our Bank's Role = "Lost Mandate" on any deal
- Manual query: "What's [Competitor Bank]'s recent activity in [Sector]?"

**Actions:**
- Scan financial news sources for deal announcements and auto-populate Competitor Deal Flow board
- Generate weekly competitive digest: key deals announced, mandate wins/losses, talent movements, league table shifts
- When a mandate is lost, auto-create a win/loss debrief task assigned to the coverage banker with suggested debrief questions
- Analyze talent movement patterns to identify competitor banks building or shrinking specific sector teams
- Generate pitch-ready competitive positioning slides pulling from the intelligence database
- Alert when a competitor bank has announced 3+ deals in a sector within 30 days (competitive surge signal)

**Data Required:**
- Competitor Deal Flow and Talent Movement boards
- Internal pipeline data for win/loss cross-reference
- Financial news feeds (press releases, industry publications)
- Historical league table data

**Autonomy Level:** Fully Autonomous (monitoring and data capture), Human-in-the-Loop (strategic recommendations)
Data collection, board updates, and alerting are fully automated. Strategic assessments and recommended responses are suggested to group heads for decision.

**Example Interaction:**
> The Market Intelligence Agent's morning scan detects three new deal announcements: Evercore is advising FinServ Corp on a $4.2B sale, Goldman Sachs is leading a $1.8B IPO for DataCloud Inc., and JP Morgan is bookrunning a $3B high yield offering for RetailMax. The agent auto-populates each entry on the Competitor Deal Flow board.
>
> It then cross-references: FinServ Corp was in our pipeline — we pitched them 4 months ago. The agent flags this as a "Lost Mandate" and creates a debrief task for the coverage MD: "FinServ Corp sell-side went to Evercore. We pitched in October — what happened? Suggested debrief areas: relationship depth, fee competitiveness, sector credential gap."
>
> The weekly digest notes: "Evercore has won 5 FIG sector mandates in the last 60 days, up from 1 in the prior period. They appear to be aggressively building FIG coverage. Recommend reviewing our FIG competitive positioning."

---

### Use Case 5: Deal Execution & Workstream Coordination

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Once a mandate is won, the real operational complexity begins. An M&A sell-side process involves dozens of parallel workstreams: data room preparation, management presentation drafting, buyer outreach, financial modeling, due diligence coordination, bid process management, and negotiation support. These workstreams involve 10-20+ internal professionals across coverage, M&A product, capital markets, legal, and compliance. Most banks coordinate this through email chains and status update spreadsheets maintained by the associate on the deal. When workstreams slip, the deal team often doesn't realize until it's too late — data room delays can push back buyer timelines and jeopardize deal momentum.

#### The Solution
monday.com Work Management for deal execution project management. Template-based deal setup (one click to create the full M&A sell-side workstream structure). Each workstream (data room, CIM drafting, buyer list, management presentation, financial model, legal review) has its own group with tasks, owners, dependencies, and deadlines. Gantt/Timeline view showing critical path. Automated alerts for overdue tasks and approaching deadlines. Status dashboards for deal team leads and senior bankers. Integration with document management for data room tracking.

#### The Outcome
- 30% reduction in deal execution timeline through better coordination
- Zero "surprise" delays — proactive alerts on workstream slippage
- Standardized deal execution playbook ensures consistent quality across teams
- Senior bankers get real-time deal status without interrupting the execution team
- New associates ramp faster with structured templates rather than learning by osmosis

#### Discovery Questions
1. "When you're running a sell-side process with 40 potential buyers, how do you track the status of each buyer's engagement — NDA signed, data room access, indication of interest received?"
2. "How do deal team leads currently know if a workstream is falling behind — is it in a system or does someone have to ask?"
3. "How long does it take to set up the project infrastructure for a new deal — all the trackers, timelines, and communication channels?"
4. "When multiple deals are running simultaneously, how do you manage resource conflicts — the same analyst staffed on three active deals?"
5. "What does your 'post-mortem' or lessons-learned process look like after a deal closes?"

#### Industry Context
"CIM" (Confidential Information Memorandum) is the marketing document for a company being sold. "Data room" (virtual data room or VDR) is the secure repository where buyer due diligence documents are housed — typically managed by platforms like Intralinks, Merrill DataSite, or Donnelley. "Process letters" are formal communications to potential buyers outlining bid deadlines and procedures. "Indication of Interest" (IOI) is a preliminary, non-binding offer. "Letter of Intent" (LOI) is a more formal, typically binding offer. Deal timelines in M&A typically run 4-9 months.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an M&A Sell-Side Deal Execution board. Create groups for each workstream: 1) Data Room Preparation, 2) CIM & Marketing Materials, 3) Buyer Outreach & Engagement, 4) Management Presentations, 5) Financial Analysis & Modeling, 6) Legal & Compliance, 7) Bid Process Management, 8) Closing & Post-Close. Columns across all groups: Task Name (text), Owner (people), Status (status: Not Started, In Progress, Under Review, Blocked, Complete), Priority (status: Critical Path, High, Medium, Low), Start Date (date), Due Date (date), Dependencies (dependency), Hours Estimated (numbers), Hours Actual (numbers), Notes (long text), Attachments (file). In the Buyer Outreach group, add additional columns: Buyer Company (text), Buyer Contact (text), NDA Status (status: Not Sent, Sent, Signed, Declined), Data Room Access (checkbox), IOI Received (checkbox), IOI Amount $M (numbers), LOI Status (status: Not Received, Under Review, Accepted, Rejected). Add a Timeline view showing all workstreams with dependencies. Add a Dashboard with: overall completion percentage, tasks overdue (count), tasks due this week (table), buyer funnel (NDA Signed → Data Room Access → IOI → LOI as a funnel chart), workstream health (status by group). Add automations: when Status is 'Blocked' on any Critical Path task, immediately notify deal team lead. When Due Date is tomorrow and Status is not 'Complete', notify Owner: 'Task due tomorrow: {Task Name}.'"

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Deal Execution Coordinator Agent
**Agent Purpose:** Monitor deal workstreams, flag blockers, manage buyer process tracking, and keep the deal team synchronized without manual status chasing.

**Triggers:**
- Daily scan at 7 AM for task status updates and overdue items
- When any task Status changes to "Blocked"
- When a buyer's IOI is received (IOI Received checkbox)
- When Dependencies are impacted by a task delay
- Weekly (Friday 5 PM) for deal status summary generation

**Actions:**
- Generate daily deal status email to deal team lead summarizing: tasks completed, tasks overdue, blockers, upcoming deadlines
- When a critical path task slips, automatically calculate downstream impact on dependent tasks and notify affected owners
- Track buyer engagement funnel: auto-update buyer stage counts and flag buyers who have data room access but haven't submitted IOI by deadline
- Generate buyer comparison matrix when multiple IOIs are received
- Create weekly deal committee memo draft with key metrics, milestones, and risk flags
- Monitor resource allocation: flag when an analyst's hours across active deals exceed 70 hours/week

**Data Required:**
- Deal Execution board (all workstreams)
- Resource allocation data (analyst/associate staffing)
- Buyer correspondence metadata
- Deal timeline milestones

**Autonomy Level:** Escalation-Based
Status monitoring, alerts, and report generation are autonomous. Task reassignment or deadline changes are recommended to deal team lead for approval. Buyer communications are never automated — always human-authored.

**Example Interaction:**
> The Deal Execution Coordinator detects that "Complete Management Presentation Draft" (Critical Path) was due yesterday and is still "In Progress." It traces the dependency chain: the management presentation must be finalized before buyer management meetings can be scheduled, which are currently set to begin in 10 days. The agent sends an alert: "⚠️ Critical Path Delay: Management Presentation Draft is 1 day overdue. This impacts: Buyer Management Meeting scheduling (currently set for Feb 28). If not completed by end of day Thursday, recommend pushing management meetings by 3-5 business days. Assigned to: James Park (Associate). Current workload: James is also staffed on the Beta Corp DCM deal — 62 hours logged this week."
>
> On Friday, the agent generates the weekly memo: "Project Aurora — Week 8 Summary. Buyer funnel: 45 NDAs signed, 38 data room access granted, 12 IOIs received (range: $850M-$1.1B), 0 LOIs yet. Key risk: 6 buyers with data room access have not submitted IOIs with 4 days to deadline. Recommend coverage MD follow-up calls to engaged-but-silent buyers. Overall: 73% of workstream tasks complete, 4 tasks overdue, 0 blocked."

---

### Use Case 6: Fee Tracking & Revenue Attribution

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banking fee economics are complex. A single deal might generate an advisory retainer, a success fee (percentage of deal value), an underwriting spread, and ongoing relationship revenue. Fees must be attributed across multiple groups — the coverage banker, the product specialist, and sometimes multiple industry groups — according to Byzantine internal credit-sharing agreements. Finance teams spend significant time reconciling fee estimates against actual payments, tracking fee installments, and producing revenue attribution reports for group heads. Disputes over league table credit and fee allocation are a perennial source of internal friction.

#### The Solution
monday.com Work Management with a structured fee tracking board. Each fee entry linked to the deal record with fields for gross fee, fee type (retainer, success, underwriting), payment schedule, and multi-party credit allocation. Automated calculation of revenue by group, by banker, by product type. Dashboard showing fee revenue trends, fee pipeline vs. actuals, and attribution breakdowns. Integration with the deal pipeline to automatically create fee tracking entries when mandates close.

#### The Outcome
- 70% reduction in fee reconciliation time for finance teams
- Transparent credit allocation reduces internal disputes
- Real-time revenue dashboards replace monthly manual reports
- Historical fee data enables more accurate fee estimation on new pitches
- Group heads can instantly see revenue attribution without waiting for finance

#### Discovery Questions
1. "How do you currently handle fee credit allocation when a deal involves multiple groups — is there a standard formula or is it negotiated deal-by-deal?"
2. "How long after a deal closes do you typically receive final fee payments, and how do you track installments?"
3. "When budgeting for next year, how accurate are your fee revenue projections based on current pipeline?"
4. "How often do internal disputes arise over league table credit or fee allocation, and how are they resolved?"
5. "Can your group heads see their real-time revenue position, or do they wait for monthly/quarterly finance reports?"

#### Industry Context
"Success fee" in M&A is typically 0.5-2% of deal value for large transactions. "Retainer" is a monthly fixed fee during the engagement (often $100K-$250K/month). "Underwriting spread" is the fee banks earn on securities issuance. "Credit allocation" is an internal process determining which group/banker gets revenue credit (important for compensation). "Run rate" refers to annualized fee revenue. League table credit rules vary by data provider.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an Investment Banking Fee Tracker board. Columns: Deal Name (text), Client Company (text), Deal Type (dropdown: M&A Advisory, ECM Underwriting, DCM Underwriting, Restructuring, Other Advisory), Deal Close Date (date), Gross Fee $M (numbers), Fee Type (dropdown: Success Fee, Retainer, Underwriting Spread, Retainer + Success, Consulting/Other), Payment Status (status: Estimated, Invoiced, Partial Payment, Fully Paid, Disputed, Written Off), Coverage Group Credit % (numbers), Product Group Credit % (numbers), Coverage Group Revenue $M (formula), Product Group Revenue $M (formula), Coverage MD (people), Product Lead (people), Invoice Date (date), Payment Due Date (date), Amount Received $M (numbers), Remaining Balance $M (formula), League Table Credit (dropdown: Full Credit, Shared Credit — Lead, Shared Credit — Co-Manager, No Credit), Fiscal Quarter (dropdown: Q1, Q2, Q3, Q4), Notes (long text). Add Dashboard with: total fee revenue by quarter (chart), revenue by deal type (chart), revenue by coverage group (chart), estimated vs. actual fees (comparison chart), outstanding receivables (table), top 10 fee-generating deals YTD (table). Add automation: when Payment Status changes to 'Fully Paid', calculate final revenue splits and notify Coverage MD and Product Lead: 'Fee received: {Deal Name} — {Gross Fee $M} total, your credit: {Coverage Group Revenue $M}.'"

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Revenue Analytics Agent
**Agent Purpose:** Automate fee reconciliation, forecast revenue, and provide transparent attribution reporting across coverage and product groups.

**Triggers:**
- Deal pipeline item moves to "Closed Won" stage (auto-create fee entry)
- Monthly revenue reconciliation schedule (1st business day)
- Payment received (Amount Received updated)
- Quarterly revenue review preparation (last week of quarter)
- Manual query: "What's our revenue run rate for [Group] this year?"

**Actions:**
- Auto-create fee tracking entries when deals close, pre-populated with estimated fees and standard credit splits
- Generate monthly revenue reconciliation: estimated vs. invoiced vs. received, aging receivables, collection forecasts
- Produce quarterly group P&L summaries with year-over-year comparisons
- Flag fee disputes early: when credit allocation percentages don't sum to 100% or when multiple groups claim lead credit
- Forecast full-year revenue based on closed deals + probability-weighted pipeline
- Generate league table submission data with proper credit allocation per provider rules

**Data Required:**
- Fee Tracker board
- Deal Pipeline board (for pipeline-to-fee linkage)
- Historical fee data for trending and benchmarking
- League table credit rules by data provider

**Autonomy Level:** Fully Autonomous (data processing), Human-in-the-Loop (dispute resolution)
Calculations, reports, and reconciliation are fully automated. Credit allocation disputes are flagged with recommended resolution but escalated to group heads for final decision.

**Example Interaction:**
> On the first business day of Q2, the Revenue Analytics Agent generates the quarterly summary: "Q1 Revenue: $127.4M (vs. $118.2M Q1 last year, +7.8%). Top contributing deal: Omega Corp sale — $18.5M fee. Advisory revenue: $89.2M. Underwriting revenue: $38.2M. Outstanding receivables: $14.7M across 6 deals (oldest: Delta Corp restructuring fee, 67 days outstanding — recommend follow-up). Full-year forecast: $485M based on closed + 60%-weighted pipeline ($571M if all active mandates convert)."
>
> The agent also flags: "Credit allocation issue detected on the RegionalBank Corp DCM deal. Both FIG Coverage (claiming 60%) and DCM Product (claiming 60%) have credit allocations that sum to 120%. Please resolve before quarter-end league table submission."

---

### Use Case 7: Analyst & Associate Staffing Optimization

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Junior banker staffing is a perennial pain point. Analysts and associates are shared resources across multiple deals and coverage teams. Staffing coordinators (or in smaller groups, the VP/Director managing the team) must balance workload, skill development, deal complexity, and banker preferences — often with imperfect information. Burnout is endemic: top performers get overstaffed because they're reliable, while others are underutilized. The staffing process is often conducted via email, Slack, and hallway conversations, with no systematic tracking of hours, utilization, or skill matching.

#### The Solution
monday.com Work Management as a staffing and resource management system. Board showing all active deals with junior banker assignments, estimated hours per deal, and actual hours logged. Utilization dashboard showing hours by person by week. Skill matrix tracking analyst/associate competencies (financial modeling, industry expertise, presentation skills) to improve matching. Request workflow: MDs submit staffing requests that flow through the staffing coordinator with visibility into current utilization before assignment.

#### The Outcome
- 25% more equitable workload distribution across junior bankers
- Reduced burnout-driven attrition (industry average: 80% analyst turnover in 2 years)
- Staffing decisions based on data rather than who shouts loudest
- Skill development tracked and intentional rather than accidental
- Staffing coordinator saves 10+ hours/week on manual coordination

#### Discovery Questions
1. "How does your staffing process work today — is there a dedicated staffing coordinator, or do MDs grab analysts directly?"
2. "Do you have visibility into how many hours each analyst is working across all their active deals?"
3. "How do you balance developing junior talent — giving them stretch assignments — with the pressure to staff experienced people on high-priority deals?"
4. "What's your analyst/associate retention rate, and how much of attrition do you attribute to workload management?"
5. "When three MDs all want the same analyst for their deals, how is that conflict resolved?"

#### Industry Context
"Staffing" in IB is the process of assigning analysts and associates to deal teams. "Utilization" is tracked in hours. A typical analyst works 80-100 hours/week during busy periods. "Staffing coordinator" is often a senior associate or VP responsible for managing the pool. "Lean staffing" means running deals with fewer junior bankers to improve economics, which increases per-person workload. "Two-year analyst program" is the standard track — most analysts leave after 2 years for private equity, business school, or other roles.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Junior Banker Staffing board. Columns: Banker Name (people), Title (dropdown: Analyst 1st Year, Analyst 2nd Year, Analyst 3rd Year, Associate 1st Year, Associate 2nd Year, Associate 3rd Year), Active Deals (connect to Pipeline board), Current Weekly Hours (numbers), Target Hours (numbers — default 65), Utilization % (formula: Current Weekly Hours / Target Hours × 100), Availability Status (status: Available, Moderately Loaded, At Capacity, Overloaded, On Vacation, On Leave), Skills (tags: Financial Modeling, DCF/LBO, Presentation Design, Data Room Management, Industry — TMT, Industry — Healthcare, Industry — FIG, Industry — Industrials, Industry — Consumer, Process Management, Client Facing), Performance Rating (status: Top Performer, Strong, Developing, New), Current Deal Assignments (long text), Notes (long text). Create a second board: Staffing Requests with columns: Requesting MD (people), Deal Name (text), Deal Type (dropdown), Estimated Hours/Week (numbers), Duration Weeks (numbers), Skills Required (tags), Priority (status: Critical, High, Medium, Low), Request Date (date), Staffing Coordinator Decision (status: Pending, Assigned, Waitlisted, Declined), Assigned Banker (people), Decision Notes (long text). Add Dashboard on main board: utilization heat map by person (chart), average hours by title (chart), bankers at capacity or overloaded (filtered view), skills coverage matrix (table). Add automation on Staffing Requests: when new request created, notify Staffing Coordinator. When Utilization % exceeds 120%, change Availability Status to 'Overloaded' and notify Staffing Coordinator: '{Banker Name} is at {Utilization %}% — review workload immediately.'"

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Staffing Optimizer Agent
**Agent Purpose:** Intelligently match staffing requests to available talent based on utilization, skills, development goals, and deal requirements.

**Triggers:**
- New staffing request submitted
- Weekly utilization review (Friday afternoon)
- When any banker's utilization exceeds 110%
- When a deal closes (freeing up junior banker capacity)
- Monthly development review (first Monday of month)

**Actions:**
- When a staffing request arrives, immediately generate top 3 candidate recommendations based on: availability, skill match, development goals, and recent workload history
- Flag workload imbalances: if any analyst exceeds 90 hours/week for 2 consecutive weeks, alert staffing coordinator and recommend redistribution
- Track skill development: ensure each analyst gets exposure to at least 3 different deal types per year
- Generate weekly staffing report: capacity outlook for next 2 weeks, upcoming deal closings that will free resources, new requests in queue
- When a deal closes, auto-update affected bankers' capacity and check if any waitlisted staffing requests can now be fulfilled
- Predict staffing crunches 2-3 weeks out based on deal timelines and generate early warnings

**Data Required:**
- Staffing board and Staffing Requests board
- Deal Pipeline board (for timeline and staffing needs)
- Historical staffing patterns and hours data
- Analyst/associate skill profiles and development goals

**Autonomy Level:** Human-in-the-Loop
Recommendations are generated automatically, but all staffing assignments require coordinator approval. Overload alerts are sent automatically; redistribution is recommended but not enacted without human decision.

**Example Interaction:**
> A TMT MD submits a staffing request: "Need a strong analyst for the TechStartup Inc. IPO — 35 hours/week for 8 weeks. Must have ECM experience and strong modeling skills." The Staffing Optimizer Agent scans the pool and recommends: "1) Alex Rivera — 52% utilized, has 2 prior IPO deals, rated 'Top Performer,' no conflicting deadlines in next 8 weeks. 2) Priya Sharma — 68% utilized, 1 prior IPO but strong modeling skills, currently developing ECM expertise per her development plan. 3) Marcus Chen — 45% utilized, no IPO experience but strongest modeler in the pool — this would be a development opportunity." The coordinator reviews, considers Priya's development goals, and assigns her with Alex as backup.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Coverage | Named-account responsibility — an MD "covers" specific companies or sectors |
| Mandate | Formal engagement to advise on a transaction (M&A, capital raise, etc.) |
| League Table | Published rankings of banks by deal volume, count, and fees |
| Pitch Book | Customized presentation deck used to win advisory mandates |
| Credentials / Tombstones | Summaries of completed deals demonstrating the bank's track record |
| CIM | Confidential Information Memorandum — marketing document for a company being sold |
| IOI | Indication of Interest — preliminary, non-binding offer from a potential buyer |
| LOI | Letter of Intent — more formal, typically binding offer |
| Bookrunner | Lead bank on a securities offering; receives primary league table credit |
| Wallet Share | Percentage of a client's total banking fees captured by your bank |
| Engagement Letter | Formal contract between bank and client establishing the advisory relationship |
| Success Fee | Fee contingent on deal completion, typically a percentage of transaction value |
| Data Room (VDR) | Secure virtual repository for due diligence documents |
| Sell-Side / Buy-Side | Whether you're advising the seller or the buyer in an M&A transaction |
| ECM / DCM | Equity Capital Markets / Debt Capital Markets — product groups for securities issuance |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Managing Director (MD) | Relationship owner, deal origination, client management | Decision-maker |
| Group Head | P&L owner for the coverage or product group | Decision-maker / Budget holder |
| Director / Executive Director | Deal execution oversight, junior talent management | Influencer / Champion |
| Vice President (VP) | Day-to-day deal management, process coordination | Influencer / User |
| Associate | Financial analysis, model building, pitch book production | User |
| Analyst | Data gathering, modeling support, presentation assembly | User |
| Chief Administrative Officer (CAO) | Operations, technology, infrastructure decisions | Decision-maker (for tools) |
| Staffing Coordinator | Resource allocation for junior bankers | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| PMO | Deal execution project management, resource allocation | Portfolio-level deal tracking and resource optimization |
| IT | Technology infrastructure, system integrations, data security | Platform deployment, API integrations with existing bank systems |
| Operations | Trade processing, client onboarding, compliance workflow | End-to-end deal lifecycle from origination through settlement |
| HR | Analyst/associate recruiting, retention, performance management | Staffing optimization, workload analytics, retention dashboards |
| Finance | Fee reconciliation, revenue reporting, budgeting | Revenue attribution, fee tracking, financial planning |
| Legal & Compliance | Conflict checks, engagement letters, regulatory filings | Compliance workflow automation, conflict-of-interest tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce (Financial Services Cloud) | Enterprise CRM — often mandated bank-wide but poorly adopted by bankers | monday.com CRM offers banker-friendly UX that drives actual adoption; can serve as working layer on top of Salesforce |
| DealCloud (Intapp) | Purpose-built IB deal management and CRM | Strong incumbent in mid-market IB; monday.com competes on flexibility, cost, and AI capabilities |
| Navatar (now Intapp) | Pipeline and relationship management for financial services | Legacy tool being sunset; natural migration opportunity |
| Dynamo | PE/VC deal management | Adjacent market; opportunity when IB teams work closely with PE clients |
| Excel / Spreadsheets | The universal IB tool for everything | monday.com replaces the "tracker spreadsheets" while preserving the analytical spreadsheets bankers love |
| Airtable | Flexible database for deal tracking | Lacks enterprise security, compliance, and scale required by banks |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Salesforce" | "Salesforce adoption in IB is notoriously low — typically 20-30%. monday.com can sit on top as the daily working layer that bankers actually use, syncing critical data back to Salesforce for enterprise reporting. You get adoption AND compliance." |
| "Our data is too sensitive for cloud tools" | "monday.com offers enterprise-grade security with SOC 2 Type II, ISO 27001, HIPAA compliance, and data residency options. Many financial institutions including banks are already on the platform. We can also discuss deployment options that meet your specific regulatory requirements." |
| "Bankers won't adopt another tool" | "That's exactly the problem we solve. monday.com's interface is intuitive enough that bankers use it without training. The key is reducing friction — auto-capture from email, mobile access for logging meetings in a taxi, and dashboards that replace the spreadsheets they're already maintaining." |
| "We need something purpose-built for IB" | "Purpose-built tools like DealCloud are rigid — they assume every bank's process is identical. monday.com gives you IB-grade workflows with the flexibility to match YOUR process, not a vendor's assumption of your process. Plus, our AI capabilities are evolving faster than any niche player." |
| "IT will never approve this" | "We work with IT security teams at major financial institutions daily. Our compliance certifications, API-first architecture, and admin controls are built for regulated industries. Let's bring your CISO into the conversation — we'll address every requirement." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for investment banking / financial services customer stories]
- [Placeholder for CRM adoption improvement metrics]
- [Placeholder for deal management efficiency case studies]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
