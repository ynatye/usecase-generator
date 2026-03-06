# Electricity, Oil & Gas × PR & Communications Playbook

## Overview

PR & Communications teams in the electricity, oil & gas sector operate under intense public scrutiny, managing stakeholder relations across regulators, communities, investors, environmental groups, and the media. These teams are typically lean — often 10–30 people at a mid-to-large utility or E&P company — yet they bear outsized responsibility during crises like pipeline incidents, refinery explosions, oil spills, power outages, rate hike announcements, and environmental compliance violations. The stakes are existential: a poorly managed communications event can wipe billions in market capitalization, trigger regulatory action, and erode the social license to operate that every energy company depends on.

The regulatory and ESG landscape adds layers of complexity. Energy companies must navigate FERC, EPA, PHMSA, state PUCs, and international bodies like OPEC+ or the IEA, each with disclosure and reporting requirements that touch communications. The global energy transition — from fossil fuels to renewables — has made every press release, earnings call script, and social media post a potential flashpoint for greenwashing accusations or activist campaigns. PR teams must balance promoting decarbonization commitments with the reality of continued hydrocarbon operations, all while maintaining investor confidence.

Internally, these teams coordinate across upstream (exploration & production), midstream (pipelines, storage, LNG terminals), downstream (refining, distribution, retail), and increasingly, renewable energy divisions. They manage executive communications for C-suite leaders who testify before Congress, speak at CERAWeek, and engage with sovereign wealth funds. The volume of stakeholder touchpoints — community town halls, regulatory filings, investor days, ESG reports, media inquiries, and social media monitoring — far exceeds what traditional PR tools and manual processes can handle.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | PR teams are understaffed relative to the volume of stakeholder communications, regulatory disclosures, and crisis scenarios they must manage across multiple business units and geographies |
| 2 | Consolidate Tech Stack with AI | Medium-High | Energy PR teams typically juggle media monitoring tools (Meltwater, Cision), social listening platforms, internal wikis, approval workflows in email, and separate crisis management systems — all disconnected |
| 3 | Replace or Radically Augment Headcount | Medium | AI agents can handle routine media monitoring, first-draft press releases, social media responses, and regulatory disclosure tracking that currently consume junior staff bandwidth |

## Prioritized Use Cases

---

### Use Case 1: Crisis Communications Command Center

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
When a pipeline leak, refinery incident, or major grid outage occurs, PR teams have minutes — not hours — to respond. Today, crisis response is coordinated through frantic email chains, ad-hoc conference calls, and outdated crisis playbooks stored in SharePoint folders nobody can find. Approvals for public statements bounce between Legal, Operations, the CEO's office, and sometimes the board, with no visibility into where a draft stands. During the 2021 Texas grid crisis, energy companies that were slow to communicate faced Congressional hearings and billions in liability. Every hour of delayed response during a crisis costs an estimated $1.2M in reputational damage for large energy companies.

#### The Solution
A monday.com Work Management workspace configured as a real-time Crisis Communications Command Center. The board structure includes: **Incident Tracker** (status columns for severity level — Tier 1/2/3, incident type dropdown — spill, outage, explosion, regulatory, cyber — and geographic region), **Stakeholder Communication Queue** (subitems for each audience: media, regulators, community, employees, investors, elected officials), **Approval Pipeline** (people columns for Legal, Ops, Exec review with status automation), **Media Monitoring Feed** (integrated via API from Meltwater/Cision), and **Post-Incident Review** board. Timeline views show the cascade of communications against regulatory reporting deadlines (e.g., NRC 4-hour notification, EPA 24-hour report). Dashboards provide real-time status of all active incidents and pending approvals.

#### The Outcome
Crisis response time reduced from 4–6 hours to under 60 minutes. 100% approval audit trail for regulatory compliance. Elimination of "who approved what" confusion that has led to unauthorized statements. Post-incident reviews become structured data, building institutional crisis response muscle over time.

#### Discovery Questions
1. "Walk me through your last major incident — how did the communications response unfold in the first 2 hours? Where did bottlenecks occur?"
2. "How do you currently track which stakeholders have been notified and what messaging they received during a crisis?"
3. "When PHMSA or your state PUC requests documentation of your communications timeline post-incident, how painful is that process?"
4. "How many people need to approve a public statement before it goes out, and what's the average turnaround during a crisis?"
5. "Do you have different crisis communication templates for different incident types, or does your team start from scratch each time?"

#### Industry Context
Energy crises are uniquely high-stakes because they can involve physical harm, environmental damage, and regulatory consequences simultaneously. The National Response Framework and National Incident Management System (NIMS) provide federal crisis structure. PHMSA requires pipeline operators to notify the National Response Center within hours of incidents. State Public Utility Commissions (PUCs) may require real-time outage communications. The SE should understand ICS (Incident Command System) terminology and how PR fits into the Joint Information Center (JIC) structure during major events.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Crisis Communications Command Center for an energy company. Create a main board called 'Active Incidents' with these columns: Incident Name (text), Severity (dropdown: Tier 1 - Critical, Tier 2 - Major, Tier 3 - Minor), Incident Type (dropdown: Pipeline Leak, Refinery Incident, Grid Outage, Cybersecurity Breach, Environmental Violation, Regulatory Action), Region (dropdown: Northeast, Southeast, Gulf Coast, Midwest, West, International), Status (status: Detected, Assessing, Responding, Monitoring, Resolved, Post-Review), Incident Commander (people), PR Lead (people), Legal Reviewer (people), Exec Approver (people), Public Statement Status (status: Drafting, Legal Review, Exec Review, Approved, Published), Regulatory Notification Deadline (date), Regulatory Notification Status (status: Not Required, Pending, Submitted, Confirmed), Media Inquiries Count (numbers), Community Impact Level (dropdown: None, Low, Moderate, Severe), Timeline (timeline). Add subitems for each stakeholder communication: Audience, Channel, Message Status, Sent Date, Approved By. Create automations: when Severity is Tier 1, notify the entire PR team and Legal; when Public Statement Status changes to Legal Review, assign the Legal Reviewer and set a 1-hour due date; when Regulatory Notification Deadline is within 2 hours and Regulatory Notification Status is Pending, send urgent notification. Create a Dashboard with widgets: Active Incidents by Severity (chart), Pending Approvals (table), Average Response Time (numbers), Incidents by Region (map chart), Open Media Inquiries (count). Add a Kanban view grouped by Status and a Timeline view showing all active incidents."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Crisis Response Coordinator

**Agent Purpose:** Automatically detect incident signals, activate crisis communication protocols, draft initial stakeholder communications, and track regulatory notification deadlines in real-time.

**Triggers:**
- New item created in Active Incidents board (manual or API-fed from SCADA/OMS systems)
- Severity column changed to Tier 1 or Tier 2
- Regulatory Notification Deadline is within 2 hours and notification not yet submitted
- Media Inquiries Count exceeds threshold (e.g., >10 in 1 hour)
- Status changed to "Resolved" (triggers post-incident review)

**Actions:**
- Auto-populate crisis communication template based on Incident Type (selects appropriate holding statement, notification templates, and regulatory forms)
- Create subitems for all required stakeholder notifications based on Severity tier (Tier 1 = all audiences, Tier 3 = internal only)
- Draft initial holding statement using incident details, route to Legal for review
- Generate regulatory notification draft pre-populated with incident data, timeline, and geographic coordinates
- Send escalation notifications if approvals are not completed within SLA (30 min for Tier 1)
- Compile post-incident communications timeline report when Status moves to Post-Review

**Data Required:**
- Integration with SCADA/OMS for incident detection signals
- Media monitoring API feed (Meltwater, Cision)
- Regulatory notification templates and deadlines by jurisdiction
- Crisis communication playbook templates by incident type
- Organization directory for escalation paths

**Autonomy Level:** Human-in-the-Loop
Drafts and routes are automated; all external communications require human approval. Regulatory notifications are pre-populated but require sign-off. Internal escalations and notifications are fully autonomous.

**Example Interaction:**
> At 2:47 AM, the Crisis Response Coordinator agent detects a new Tier 1 item created via API integration from the pipeline SCADA system: a pressure anomaly on the 36-inch natural gas transmission line near Midland, TX. Within 90 seconds, the agent has activated the full crisis protocol: created 7 stakeholder communication subitems (media holding statement, PHMSA notification, Railroad Commission of Texas notification, community notification for Midland County, employee safety bulletin, investor relations alert, and elected officials briefing), assigned the on-call PR manager as lead, and drafted a holding statement reading: "We are aware of and responding to an operational event on our Permian Basin transmission infrastructure. Emergency response teams have been dispatched. There are no confirmed injuries at this time. We are coordinating with federal and state regulators and will provide updates as information becomes available."
>
> The agent flags that the PHMSA telephonic notification must be submitted within 1 hour for a Tier 1 gas transmission event and has pre-populated the NRC report form with pipeline segment ID, GPS coordinates, estimated volume, and weather conditions. The Legal Reviewer receives an urgent notification with a 20-minute approval SLA. Meanwhile, the agent has begun monitoring social media mentions of "Midland pipeline" and "gas leak Permian" and is logging incoming media inquiries with journalist name, outlet, and deadline into the Media Inquiries subitem tracker.

---

### Use Case 2: ESG & Sustainability Communications Hub

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies face relentless pressure to demonstrate credible ESG progress — from investors applying TCFD/SASB frameworks, regulators enforcing SEC climate disclosure rules, activists scrutinizing greenwashing, and communities demanding environmental justice. PR teams must coordinate ESG messaging across annual sustainability reports (often 200+ pages), earnings call scripts, investor presentations, social media campaigns, community engagement materials, and regulatory filings — all telling a consistent story. One inconsistency between what the CEO says at CERAWeek and what's in the CDP disclosure can trigger an SEC inquiry or activist short-seller report. Most energy PR teams manage this through email chains and shared drives, with no single source of truth for approved ESG messaging, data points, or commitments.

#### The Solution
A monday.com workspace serving as the ESG Communications Hub. **ESG Commitment Tracker** board with columns for: Commitment (text), Category (dropdown: Emissions Reduction, Renewable Capacity, Water Management, Community Investment, Workforce Diversity, Supply Chain, Biodiversity), Target Year (date), Baseline Year, Current Progress (numbers with %), Source Document (files), Approved Messaging (long text), Last Verified Date. **Content Calendar** board specifically for ESG communications: Publication (text), Channel (dropdown: Annual Report, Investor Deck, Press Release, Social Media, Website, Regulatory Filing, Community Meeting), Target Date, Status (Drafting, Fact-Check, Legal Review, Approved, Published), ESG Commitments Referenced (connect board to Commitment Tracker). **Stakeholder-Specific Messaging Matrix** with subitems mapping each ESG theme to investor language, community language, regulatory language, and employee language. Dashboards showing commitment progress, upcoming publications, and messaging consistency scores.

#### The Outcome
Single source of truth for all ESG claims and commitments, eliminating inconsistency risk. 60% reduction in time to produce sustainability report sections. Real-time visibility into which ESG commitments are being communicated to which audiences. Audit trail for SEC climate disclosure compliance. Proactive identification of messaging gaps before they become activist attack vectors.

#### Discovery Questions
1. "How do you ensure the emissions reduction numbers in your sustainability report match what your IR team tells analysts on the earnings call?"
2. "When the SEC's climate disclosure rules take effect, how confident are you that every public ESG claim your company has made can be substantiated with documentation?"
3. "How many hours does your team spend each year producing the sustainability report, and how much of that is chasing down data and approvals vs. actual writing?"
4. "Have you ever had an activist group or short-seller challenge a specific ESG claim your company made? How did you trace back to the original source?"
5. "How do you adapt ESG messaging for different audiences — what works for BlackRock doesn't work for a community town hall in Louisiana, right?"

#### Industry Context
The SEC's climate-related disclosure rules (adopted 2024) require registrants to disclose Scope 1 and 2 GHG emissions, climate-related risks, and transition plans. TCFD (Task Force on Climate-related Financial Disclosures) and SASB (Sustainability Accounting Standards Board) provide frameworks that investors expect energy companies to follow. CDP (formerly Carbon Disclosure Project) scores are tracked by institutional investors. The EU's CSRD (Corporate Sustainability Reporting Directive) adds requirements for companies with EU operations. "Greenwashing" litigation is rising — the FTC's Green Guides and state attorneys general are actively pursuing misleading environmental claims. SEs should understand the difference between Scope 1 (direct emissions), Scope 2 (purchased energy), and Scope 3 (value chain) emissions and why Scope 3 is so contentious for oil & gas companies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an ESG Communications Hub for an energy company. Create a board called 'ESG Commitments Registry' with columns: Commitment Name (text), Category (dropdown: Net Zero Target, Emissions Reduction, Renewable Capacity, Methane Reduction, Water Stewardship, Community Investment, Workforce DEI, Supply Chain Sustainability, Biodiversity, Just Transition), Scope (dropdown: Scope 1, Scope 2, Scope 3, Non-GHG), Target Year (date), Baseline Year (numbers), Baseline Value (numbers), Current Value (numbers), Progress Percentage (formula), Source Document (files), Approved Public Language (long text), Last Verified (date), Verification Status (status: Current, Needs Update, Under Review, Disputed), Owner (people). Create a connected board called 'ESG Content Calendar' with columns: Publication Title (text), Channel (dropdown: Sustainability Report, CDP Response, SEC Filing, Press Release, Investor Presentation, Social Media, Website, Community Meeting, Earnings Call Script), Target Publish Date (date), Status (status: Planning, Drafting, Data Verification, Legal Review, Exec Approval, Published), Writer (people), Reviewer (people), Connected Commitments (connect to ESG Commitments Registry), Audience (dropdown: Investors, Regulators, Community, Employees, Media, General Public). Add automations: when Verification Status changes to Needs Update, notify the Owner; when Content Calendar Status changes to Data Verification, check connected Commitments for any with Verification Status not Current and flag them; when Target Publish Date is within 1 week and Status is not Approved, escalate to Reviewer. Create a Dashboard showing: Commitments by Category (chart), Content Pipeline by Status (chart), Upcoming Publications (calendar), Overdue Verifications (table), Progress Toward Key Targets (battery widgets for top 5 commitments)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Messaging Guardian

**Agent Purpose:** Monitor all outgoing ESG communications for consistency with the approved commitments registry, flag potential greenwashing risks, and ensure data accuracy across all channels.

**Triggers:**
- New item created in ESG Content Calendar with connected commitments
- Content Calendar Status changes to "Drafting" or "Data Verification"
- ESG Commitments Registry item has Verification Status changed to "Needs Update" or "Disputed"
- Weekly scheduled scan of all Published content items
- External trigger: new SEC filing deadline approaching

**Actions:**
- Cross-reference ESG claims in draft content against Approved Public Language in the Commitments Registry; flag discrepancies
- Verify numerical claims (emissions figures, renewable capacity percentages) against Current Value in registry
- Generate consistency report comparing messaging across different channels for the same commitment
- Draft stakeholder-specific language variations (investor vs. community vs. regulatory) from the approved base messaging
- Alert PR lead when a commitment's progress has stalled but active communications still reference it as "on track"
- Pre-populate SEC disclosure sections with verified data from the registry

**Data Required:**
- ESG Commitments Registry (all fields)
- Published content archive with full text
- SEC filing templates and deadlines
- CDP questionnaire structure
- Company emissions data from operations/sustainability team

**Autonomy Level:** Escalation-Based
Consistency checks and flagging are fully autonomous. Language suggestions require human review. Any content modification or external publication requires explicit approval. Regulatory filing pre-population is draft-only with mandatory legal review.

**Example Interaction:**
> The ESG Messaging Guardian detects that a new press release draft in the Content Calendar references the company's "commitment to achieve net-zero Scope 1 and 2 emissions by 2040." It cross-references the ESG Commitments Registry and finds that the approved language reads "net-zero Scope 1 and 2 emissions by 2045" — the target year was updated last quarter following a board review, but the PR team is working from an outdated talking point. The agent immediately flags the discrepancy, attaches the board resolution document that changed the target, and suggests corrected language. It also runs a scan of the last 90 days of published content and identifies two social media posts and one investor presentation slide that still reference "2040," generating a remediation task list with links to each item and suggested corrections for each channel's audience.

---

### Use Case 3: Media Relations & Journalist Engagement Tracker

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy PR teams manage relationships with hundreds of journalists across trades (Oil & Gas Journal, Upstream, Power Engineering), business press (WSJ, FT, Bloomberg, Reuters), local media in operating regions, and increasingly, energy-focused substacks and podcasters. Most teams track journalist relationships in spreadsheets or individual Rolodexes, with no shared visibility into who last spoke to a reporter, what was said, which stories are in progress, and what angles specific journalists tend to pursue. When a Bloomberg reporter calls about a rumored acquisition or an environmental incident, the PR team scrambles to determine if anyone else has spoken to that reporter recently. Paid media monitoring tools (Cision, Meltwater) cost $50K–$150K/year but only track coverage — not the relationship context that determines whether a journalist will give you a fair hearing.

#### The Solution
monday.com CRM repurposed as a Media Relations CRM. **Journalist Database** board: Name, Outlet, Beat (dropdown: Upstream, Midstream, Downstream, Renewables, Policy/Regulatory, Financial, ESG/Climate, Local/Community), Region, Contact Info, Relationship Owner (people), Relationship Strength (dropdown: Champion, Warm, Neutral, Cold, Adversarial), Last Contact Date, Last Contact Notes (long text), Story Preferences (tags), Social Media Handle. **Active Stories** board: Story Topic, Journalist (connect to Journalist Database), Angle Assessment (dropdown: Positive, Neutral, Skeptical, Hostile), Deadline, Company Spokesperson, Key Messages Approved, Status (Pitched, In Progress, Published, Killed), Published Link, Sentiment Assessment. **Pitch Pipeline** board for proactive media outreach with timeline views showing editorial calendar alignment. **Media Coverage** board pulling in published articles with sentiment analysis. Dashboards showing relationship health by outlet, story pipeline, and coverage sentiment trends.

#### The Outcome
360-degree view of every journalist relationship across the PR team. 40% increase in proactive story placement through systematic pitch management. Elimination of "who talked to that reporter?" confusion. Data-driven understanding of which outlets and journalists are most/least favorable, enabling strategic media targeting.

#### Discovery Questions
1. "If a Wall Street Journal reporter called right now about your CEO, how quickly could you pull up every interaction your team has had with that reporter in the last year?"
2. "How do you decide which journalists to proactively pitch stories to? Is it systematic or based on individual PR team members' personal contacts?"
3. "What's your ratio of reactive vs. proactive media engagement? Most energy companies tell me it's 80/20 reactive — is that true for you?"
4. "When you have good news — a major renewable energy project milestone, a safety record achievement — how do you decide which outlets get exclusives vs. wide distribution?"
5. "How much are you spending on Cision and Meltwater, and does your team actually use them for relationship management or just clip tracking?"

#### Industry Context
Energy trade publications (Hart Energy, S&P Global Commodity Insights, Argus Media, ICIS) are highly influential with industry decision-makers. Wire services (Reuters, Bloomberg) move markets with energy coverage. Local media in operating regions (Houston Chronicle, Midland Reporter-Telegram, New Orleans Times-Picayune) shape community perception. Energy journalists tend to specialize deeply — a reporter covering LNG markets is a different person than one covering solar policy. The SE should understand that energy PR teams often have separate functions for financial communications (earnings, M&A) and operational communications (safety, community, environment).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Media Relations CRM for an energy company PR team. Create a board called 'Journalist Database' with columns: Journalist Name (text), Outlet (text), Beat (dropdown: Upstream Oil & Gas, Midstream/Pipelines, Downstream/Refining, Renewables/Clean Energy, Energy Policy & Regulation, Financial/M&A, ESG & Climate, Local/Community, General Business), Region (dropdown: US National, Gulf Coast, Northeast, West Coast, Midwest, Europe, Asia-Pacific, Middle East), Email (email), Phone (phone), Twitter/X Handle (text), Relationship Owner (people), Relationship Strength (status: Champion - Green, Warm - Yellow/Green, Neutral - Yellow, Cold - Orange, Adversarial - Red), Last Contact Date (date), Contact Notes (long text), Preferred Pitch Method (dropdown: Email, Phone, DM, In-Person), Key Topics of Interest (tags). Create a connected board called 'Story Tracker' with columns: Story Topic (text), Journalist (connect to Journalist Database), Outlet (mirror), Angle (dropdown: Favorable, Balanced, Skeptical, Hostile, Unknown), Story Status (status: Tipped, Pitched, Reporter Working, Draft Review Requested, Published, Killed, Spiked), Deadline (date), Spokesperson (people), Approved Key Messages (long text), Published URL (link), Sentiment Score (dropdown: Very Positive, Positive, Neutral, Negative, Very Negative), Revenue/Regulatory Impact (dropdown: High, Medium, Low, None). Add automations: when Last Contact Date in Journalist Database is more than 90 days ago and Relationship Strength is Champion or Warm, notify Relationship Owner to re-engage; when Story Status changes to Published, prompt for Sentiment Score entry; when a new item is created in Story Tracker, auto-populate Key Messages from the latest approved messaging document. Create a Dashboard with: Relationship Strength Distribution (pie chart), Stories by Status (bar chart), Coverage Sentiment Trend (line chart over time), Top 10 Most Engaged Journalists (table), Upcoming Deadlines (calendar widget)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Media Intelligence Analyst

**Agent Purpose:** Monitor media coverage mentioning the company, analyze sentiment and narrative trends, identify emerging stories before they break, and recommend proactive engagement strategies.

**Triggers:**
- New media mention detected via monitoring API integration (hourly scan)
- Story Tracker item Status changed to "Published"
- Scheduled daily briefing generation (6:00 AM local time)
- Journalist Database contact with "Adversarial" relationship publishes new energy story
- Keyword alert for company name, executive names, or key asset names in news feeds

**Actions:**
- Create new Story Tracker item from detected media mention with auto-populated journalist info, outlet, and preliminary sentiment assessment
- Generate daily media briefing summarizing overnight coverage, sentiment trends, and recommended responses
- Alert PR team when an adversarial journalist is working on a company-related story (detected via social media posts, source requests, or FOIA filings)
- Recommend proactive pitch opportunities based on trending energy topics that align with company strengths
- Update Relationship Strength scores based on coverage sentiment patterns over time
- Draft response recommendations for negative coverage with approved messaging templates

**Data Required:**
- Media monitoring API feed (Meltwater, Cision, or Google News API)
- Journalist Database with full relationship history
- Approved messaging library and key messages by topic
- Social media monitoring for journalist activity
- Company news archive for historical context

**Autonomy Level:** Escalation-Based
Media monitoring, sentiment analysis, and briefing generation are fully autonomous. Pitch recommendations and response strategies require PR team review. Any direct journalist outreach requires explicit human approval.

**Example Interaction:**
> At 5:45 AM, the Media Intelligence Analyst agent compiles the overnight briefing. It detects that Reuters published a story at 11 PM citing "sources familiar with the matter" suggesting the company is considering selling its Permian Basin assets. The agent identifies the reporter (Jennifer Hiller, Reuters Energy) from the Journalist Database — Relationship Strength: Warm, last contacted 3 weeks ago about a different story. The agent notes that two other outlets (Bloomberg, WSJ) have followed up with their own calls, logging 4 media inquiries in the Story Tracker overnight. It drafts a recommended holding statement, flags the IR team for market-open preparation, and recommends that the PR VP call Jennifer Hiller before 8 AM to maintain the relationship and provide context. The daily briefing also notes that an activist investor published a blog post yesterday criticizing the company's methane reduction timeline — the agent recommends a proactive social media post highlighting the company's recent EPA methane audit results.

---

### Use Case 4: Regulatory Communications & Government Affairs Tracker

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies engage with dozens of regulatory bodies simultaneously: FERC (Federal Energy Regulatory Commission), EPA, PHMSA (Pipeline and Hazardous Materials Safety Administration), DOE, NRC (for nuclear), state PUCs, state environmental agencies, county and municipal permitting authorities, and international bodies. Each has different filing requirements, comment periods, hearing schedules, and communication protocols. PR teams must coordinate messaging across all of these — ensuring what the company says to FERC doesn't contradict what it tells the Texas Railroad Commission, and that public statements align with regulatory filings. Missing a comment period deadline on a proposed rule can have multi-billion-dollar consequences. Most energy companies track regulatory proceedings through a patchwork of legal department spreadsheets, government affairs calendars, and individual knowledge.

#### The Solution
monday.com Work Management configured as a Regulatory Communications Tracker. **Active Proceedings** board: Docket Number (text), Regulatory Body (dropdown: FERC, EPA, PHMSA, DOE, NRC, State PUC, State Environmental, Local/Municipal, International), Proceeding Type (dropdown: Rulemaking, Rate Case, Permitting, Enforcement, Investigation, Comment Period, Compliance Filing), Status (status: Monitoring, Active Engagement, Filing Preparation, Filed, Awaiting Decision, Decided, Appeal), Impact Assessment (dropdown: Critical, Significant, Moderate, Low), Key Dates (timeline), Company Position (long text), Communications Implications (long text), Government Affairs Lead (people), PR Lead (people). **Filing Calendar** board with timeline views showing all upcoming deadlines across all regulatory bodies. **Testimony & Comments** board tracking draft preparation, legal review, and filing status. **Stakeholder Alignment Matrix** ensuring company positions are consistent across all proceedings. Dashboards showing the regulatory landscape at a glance with deadline alerts.

#### The Outcome
Zero missed regulatory filing deadlines. Consistent messaging across all regulatory engagements. 50% reduction in time PR spends coordinating with Legal and Government Affairs on regulatory communications. Real-time visibility into the regulatory landscape for executive decision-making. Audit trail demonstrating communications compliance.

#### Discovery Questions
1. "How many active regulatory proceedings is your company involved in right now? Can anyone on your team give me that number without checking multiple systems?"
2. "Has your company ever had a messaging inconsistency surface during a regulatory proceeding — say, a public statement that contradicted a filing position?"
3. "When a new EPA proposed rule drops that could affect your operations, what's the process for aligning Government Affairs, Legal, Operations, and PR on a response?"
4. "How do you track state-level regulatory developments across the 15-20 states where you operate? Is someone manually monitoring each PUC docket?"
5. "What happens when a rate case is pending and a journalist asks about your capital investment plans? How do you ensure PR doesn't get ahead of the regulatory filing?"

#### Industry Context
FERC regulates interstate electricity transmission and natural gas pipelines. State PUCs regulate retail electricity and gas rates. EPA enforces Clean Air Act, Clean Water Act, and RCRA requirements. PHMSA regulates pipeline safety. The current regulatory environment is dynamic: EPA methane rules, SEC climate disclosure, FERC transmission planning reform, IRA (Inflation Reduction Act) implementation, and state-level renewable portfolio standards all create communications challenges. "Regulatory risk" is a top-3 concern for energy company investors. SEs should understand the difference between a rate case (where a utility requests rate changes from a PUC) and a rulemaking (where a federal agency proposes new regulations).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Regulatory Communications Tracker for an energy company. Create a board called 'Active Regulatory Proceedings' with columns: Docket/Case Number (text), Proceeding Title (text), Regulatory Body (dropdown: FERC, EPA, PHMSA, DOE, NRC, SEC, State PUC - Texas, State PUC - California, State PUC - New York, State PUC - Other, State Environmental, Local Permitting, International), Proceeding Type (dropdown: Rulemaking, Rate Case, Permitting, Enforcement Action, Investigation, Compliance Filing, Comment Period, Certification, Interconnection), Impact Level (dropdown: Critical - >$100M, Significant - $10M-$100M, Moderate - $1M-$10M, Low - <$1M), Status (status: Monitoring, Preparing Response, Filed/Submitted, Awaiting Decision, Decision Received, Appeal, Closed), Key Deadline (date), Company Position Summary (long text), PR Implications (long text), Govt Affairs Lead (people), PR Lead (people), Legal Lead (people), Approved External Messaging (long text), Internal Only Notes (long text), Related Proceedings (connect board to self), Timeline (timeline). Create a 'Filing Calendar' board with: Filing Name (text), Connected Proceeding (connect to Active Regulatory Proceedings), Due Date (date), Filing Status (status: Not Started, Drafting, Internal Review, Legal Approved, Filed, Confirmed Receipt), Assigned To (people), Document (files). Add automations: when Key Deadline is within 14 days and Status is Monitoring, change Status to Preparing Response and notify all leads; when Filing Status changes to Filed, update connected Proceeding status; when Impact Level is Critical, add to executive briefing group. Create a Dashboard with: Proceedings by Regulatory Body (chart), Upcoming Deadlines Next 30 Days (table sorted by date), Critical Proceedings Status (battery), Filing Pipeline (funnel chart), Proceedings by Impact Level (pie chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Regulatory Radar

**Agent Purpose:** Monitor regulatory developments across federal and state agencies relevant to the company, flag new proceedings, track deadlines, and ensure cross-functional alignment on regulatory communications.

**Triggers:**
- Daily scan of FERC eLibrary, EPA Federal Register notices, PHMSA dockets, and state PUC filings
- Key Deadline within 30/14/7/3 days on any Active Proceeding
- New item created in Active Regulatory Proceedings (manual entry of newly discovered proceeding)
- Status change on any Critical or Significant proceeding
- Company mentioned in a regulatory filing by another party (e.g., intervenor comment)

**Actions:**
- Create new Active Regulatory Proceeding items from detected filings with auto-populated docket number, regulatory body, type, and key dates
- Generate deadline summary reports weekly for Government Affairs, Legal, and PR leadership
- Cross-reference new proceedings against existing company positions to identify potential conflicts
- Draft initial Company Position Summary and PR Implications based on proceeding details and historical company positions on similar matters
- Escalate when deadlines are at risk (filing preparation not started within defined lead times)
- Generate stakeholder-specific talking points when a regulatory decision is issued

**Data Required:**
- API access to regulatory filing systems (FERC eLibrary, Regulations.gov, state PUC e-filing portals)
- Company regulatory position archive
- Historical proceeding database
- Approved messaging library by regulatory topic
- Executive calendar for hearing preparation scheduling

**Autonomy Level:** Escalation-Based
Monitoring and deadline tracking are fully autonomous. Position summaries and talking point drafts require human review. Filing initiation requires explicit Government Affairs approval.

**Example Interaction:**
> The Regulatory Radar agent detects a new EPA proposed rule published in the Federal Register: "Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources: Oil and Natural Gas Sector Climate Review." It creates a new Active Regulatory Proceeding item, auto-categorizes it as Rulemaking with EPA, sets the Impact Level to Critical (based on keyword analysis matching "oil and natural gas" and "emissions standards"), and identifies the 60-day comment period deadline. It cross-references the company's existing methane reduction commitments from the ESG Commitments Registry and notes potential alignment opportunities. It drafts an initial PR Implications assessment: "High media interest expected. Company's voluntary methane pledge exceeds proposed standards — opportunity for proactive positioning. Recommend coordinating with API and industry trade groups on joint messaging. Risk: rule may include provisions affecting existing facilities not covered by voluntary pledge." The agent assigns the Government Affairs Lead, PR Lead, and Legal Lead and creates a Filing Calendar item for the comment submission with a draft-due date 30 days before the deadline.

---

### Use Case 5: Internal Communications & Employee Engagement Platform

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy companies employ workforces spread across corporate offices, trading floors, refineries, offshore platforms, pipeline rights-of-way, power plants, and retail locations. Reaching a roughneck on a Permian Basin drilling rig with the same corporate messaging that reaches a trader in Houston requires multi-channel communication strategies. Internal comms teams typically manage an intranet (often SharePoint), email newsletters, digital signage, town halls, and increasingly Yammer/Viva Engage — but have no unified system to plan, approve, distribute, and measure internal communications. Critical safety communications can get buried alongside benefits enrollment reminders. During M&A activity, regulatory investigations, or workforce reductions, the internal communications challenge becomes acute — employees hear rumors before official messaging reaches them.

#### The Solution
monday.com Work Management as an Internal Communications Command Center. **Content Calendar** board: Message Title, Category (dropdown: Safety, Operations, Corporate/M&A, Benefits/HR, Culture/Recognition, ESG/Sustainability, Training, Executive Communications), Target Audience (dropdown: All Employees, Corporate Only, Field Operations, Specific Region, Specific Business Unit, Leadership Only), Channels (dropdown multi-select: Email, Intranet, Digital Signage, Town Hall, Yammer, SMS/Text, Toolbox Talk, Shift Briefing), Priority (dropdown: Routine, Important, Urgent, Emergency), Publish Date, Status (Drafting, Review, Approved, Scheduled, Published, Measuring), Author (people), Approver (people), Engagement Metrics (numbers). **Town Hall & Event Manager** board tracking logistics, speaker preparation, Q&A management, and follow-up actions. **Employee Feedback Tracker** for capturing and acting on engagement survey results and open-door comments. Dashboards showing communication reach, channel effectiveness, and engagement trends.

#### The Outcome
Single pane of glass for all internal communications planning and execution. 30% improvement in employee awareness of key corporate initiatives (measured via pulse surveys). Elimination of conflicting messages reaching different employee populations. Safety communications prioritized and tracked separately from routine updates. Data-driven channel optimization based on actual engagement metrics.

#### Discovery Questions
1. "When you need to get an urgent safety message to every employee across all your operating locations, how long does it take from decision to delivery?"
2. "How do you know if a field worker on an offshore platform actually received and understood a critical operational update?"
3. "During your last major corporate announcement — a reorganization, acquisition, or earnings event — did employees hear about it from you first, or from the media?"
4. "How do you adapt messaging for your corporate employees vs. your field workforce? Same content in different formats, or fundamentally different messaging?"
5. "What's your current employee engagement score, and how much of the internal comms function is dedicated to measuring and improving it?"

#### Industry Context
Energy field workforces often lack corporate email access — communications must reach them through supervisors, digital signage in break rooms, toolbox talks (daily safety briefings before shifts), or SMS. Offshore workers may be on 14/14 or 28/28 rotations with limited connectivity. Refinery and plant workers operate in process safety environments where distraction management is critical — you can't just push notifications to personal phones during operating hours. Union workforces have additional communication considerations. The SE should understand that "toolbox talks" are a primary communication channel in upstream and downstream operations, typically 5-15 minute briefings at the start of each shift.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Internal Communications Management workspace for an energy company with a distributed workforce. Create a board called 'Internal Comms Calendar' with columns: Message Title (text), Category (dropdown: Safety Alert, Operational Update, Corporate Announcement, Benefits & HR, Culture & Recognition, ESG & Sustainability, Training & Development, Executive Message, Emergency/Crisis), Target Audience (dropdown: All Employees, Corporate/Office, Field Operations, Offshore Only, Refinery/Plant, Specific Region, Leadership Team), Distribution Channels (tags: Company Email, Intranet Post, Digital Signage, Town Hall, Yammer/Viva, SMS Alert, Toolbox Talk Script, Shift Briefing Card, Supervisor Cascade), Priority (status: Routine - Gray, Important - Blue, Urgent - Orange, Emergency - Red), Planned Date (date), Status (status: Idea, Drafting, Under Review, Approved, Scheduled, Published, Measuring), Author (people), Approver (people), Open Rate (numbers), Engagement Score (numbers), Feedback Received (numbers). Create a connected board called 'Town Halls & Events' with columns: Event Name (text), Date (date), Format (dropdown: In-Person, Virtual, Hybrid), Speaker (people), Audience Size Target (numbers), Actual Attendance (numbers), Q&A Items Captured (numbers), Follow-Up Actions (subitems with assignee and due date), Satisfaction Score (numbers), Recording Link (link). Add automations: when Priority is Emergency, skip review status and go directly to Approved with notification to all approvers; when Status changes to Published, prompt Author to enter engagement metrics after 48 hours; when Planned Date is within 3 days and Status is still Drafting, escalate to Approver. Create a Dashboard with: Content by Category (pie chart), Publishing Cadence (timeline), Average Engagement by Channel (bar chart), Upcoming Communications (table), Town Hall Attendance Trend (line chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Internal Comms Orchestrator

**Agent Purpose:** Automate multi-channel distribution of internal communications, adapt content for different workforce segments, and measure engagement to optimize future communications.

**Triggers:**
- Internal Comms Calendar item Status changes to "Approved"
- Emergency/Crisis category item created (immediate activation)
- Town Hall event date is within 48 hours (pre-event preparation)
- Engagement metrics fall below threshold for a published communication
- Monthly scheduled engagement analysis report

**Actions:**
- Auto-generate channel-specific versions of approved content (email version, digital signage version, toolbox talk script, SMS summary — each appropriately formatted and length-adjusted)
- Schedule distribution across all selected channels at optimal times (corporate email: 10 AM local, digital signage: shift change, SMS: for urgent only)
- Generate toolbox talk facilitator guides with discussion prompts and safety tie-ins for field communications
- Compile engagement reports by channel, audience segment, and content category
- Identify communication gaps (e.g., offshore workforce hasn't received any ESG updates in 30 days) and recommend catch-up content
- Draft follow-up communications for town hall Q&A items that weren't answered live

**Data Required:**
- Internal Comms Calendar with full content
- Employee directory with location, role type, and communication channel access
- Distribution platform APIs (email system, intranet CMS, digital signage network, SMS gateway)
- Historical engagement data by channel and audience
- Town Hall recordings and Q&A logs

**Autonomy Level:** Human-in-the-Loop
Content adaptation and scheduling are automated but require PR team review before distribution. Emergency communications follow an accelerated approval path. Engagement analysis and recommendations are fully autonomous. No content is distributed externally without explicit approval.

**Example Interaction:**
> The Internal Comms Orchestrator receives an approved communication: the company has reached a major safety milestone — 5 million consecutive work hours without a lost-time incident across Gulf Coast refining operations. The agent generates five versions: (1) a polished email for corporate employees with an executive quote and infographic, (2) a 3-slide digital signage rotation for refinery break rooms featuring the safety record and photos of the teams, (3) a toolbox talk script with 5 discussion prompts ("What does this milestone mean to you? What's one thing we do every day that keeps us safe?"), (4) an SMS alert for field supervisors: "🎉 5M hours LTI-free! Share the news at your next toolbox talk — script available on the intranet," and (5) a Yammer post encouraging employees to share their #SafetyStory. The agent schedules the email for 9 AM CT, the signage for shift-change rotation at 6 AM/6 PM, the SMS for 7 AM, and the Yammer post for 10 AM. It sets a reminder to collect engagement metrics in 48 hours.

---

### Use Case 6: Community Relations & Stakeholder Engagement Manager

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies operate in communities where they are often the largest employer, taxpayer, and environmental presence. Community relations involves managing relationships with local elected officials, school boards, environmental groups, landowners (especially for pipelines and wind/solar projects), indigenous communities (tribal consultation requirements under NHPA Section 106), and neighborhood associations near facilities. Each community has unique concerns — noise from compressor stations, flaring visibility, truck traffic from fracking operations, water usage, property values near transmission lines. Most companies track community engagement through individual community relations managers' personal notes and spreadsheets, with no corporate-wide visibility into community sentiment, commitments made, or issues escalating toward organized opposition. When a community group shows up at a PUC hearing to oppose a project, it's often the first time the PR team learns about simmering concerns.

#### The Solution
monday.com Work Management as a Community Relations Hub. **Community Stakeholder Database** board: Organization/Individual Name, Type (dropdown: Elected Official, Community Organization, Environmental Group, Landowner Group, Indigenous Nation/Tribe, School District, Business Association, Individual Resident, Media — Local), Region/Facility, Primary Concern (tags: Environment, Noise, Traffic, Property Values, Employment, Tax Revenue, Water, Health/Safety, Visual Impact, Cultural Heritage), Relationship Status (status: Supportive, Neutral, Concerned, Opposed, Litigating), Community Relations Manager (people), Last Engagement Date, Engagement Notes (long text). **Community Commitments Tracker**: Commitment Made (text), Made To (connect to Stakeholder Database), Date Made, Delivery Date, Status (Pending, In Progress, Delivered, Overdue, Disputed), Evidence of Delivery (files). **Community Events & Meetings** board: Event Type (Town Hall, Open House, School Visit, Community Benefit Distribution, Environmental Monitoring Tour, Tribal Consultation), Date, Attendees, Issues Raised (subitems), Follow-Up Actions. **Issues & Concerns** board tracking community concerns from detection to resolution with escalation paths.

#### The Outcome
Corporate-wide visibility into community sentiment across all operating regions. Zero broken community commitments (which destroy trust and create organized opposition). Early warning system for community concerns before they escalate to regulatory or legal challenges. Data-driven community investment strategy based on actual stakeholder feedback.

#### Discovery Questions
1. "When you're planning a new pipeline, plant expansion, or renewable project, how do you map the community stakeholders who will be impacted and their likely concerns?"
2. "Has your company ever made a commitment to a community — jobs, environmental mitigation, community benefit payments — that fell through the cracks? What was the consequence?"
3. "How do you track tribal consultation requirements for projects crossing indigenous lands? Is that managed by Legal, Community Relations, or both?"
4. "When a community group shows up at a PUC hearing to oppose one of your projects, is your community relations team surprised, or did they see it coming?"
5. "How do you measure the ROI of your community investment programs? Can you tie specific community engagement to smoother permitting or reduced opposition?"

#### Industry Context
NHPA Section 106 requires consultation with indigenous communities when federal actions (including FERC-jurisdicted projects) may affect cultural resources. NEPA (National Environmental Policy Act) requires community impact assessment for major projects. Many states have Community Benefit Agreements (CBAs) that formalize company commitments. The "social license to operate" concept is central to energy — even a legally permitted project can be delayed or canceled by sustained community opposition. Pipeline projects (e.g., Dakota Access, Mountain Valley) have been defined by community and indigenous opposition. Renewable projects increasingly face local opposition (NIMBY) over visual impact, land use, and wildlife concerns. SEs should understand that community relations in energy is not optional philanthropy — it's a core business function that directly impacts project timelines and costs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Community Relations Management workspace for an energy company. Create a board called 'Community Stakeholders' with columns: Stakeholder Name (text), Type (dropdown: Elected Official, Community Organization, Environmental Group, Landowner/Landowner Association, Indigenous Nation/Tribe, School District, Business Association, Faith Community, Individual Resident, Local Media), Associated Facility/Project (dropdown: [list major facilities]), Region (dropdown: [operating regions]), Primary Concerns (tags: Environmental Impact, Noise, Traffic, Property Values, Employment/Jobs, Tax Revenue, Water Usage/Quality, Health & Safety, Visual Impact, Cultural Heritage, Land Rights, Community Investment), Relationship Status (status: Strong Supporter - Green, Supportive - Light Green, Neutral - Yellow, Concerned - Orange, Opposed - Red, Litigating - Dark Red), Community Relations Manager (people), Last Engagement (date), Engagement Frequency Target (dropdown: Weekly, Monthly, Quarterly, Semi-Annual, Annual, As-Needed), Next Planned Engagement (date), Notes (long text). Create a connected board called 'Community Commitments' with columns: Commitment Description (text), Made To (connect to Community Stakeholders), Commitment Type (dropdown: Employment Target, Environmental Mitigation, Financial/Community Benefit, Infrastructure Improvement, Monitoring Program, Educational Program, Other), Date Committed (date), Delivery Deadline (date), Status (status: Pending, In Progress, Delivered, Verified, Overdue, Disputed), Responsible Team (people), Evidence (files), Value (numbers with $). Add automations: when Delivery Deadline is past and Status is not Delivered or Verified, mark as Overdue and escalate to VP Community Relations; when Last Engagement date is past the Engagement Frequency Target, notify Community Relations Manager; when Relationship Status changes to Opposed or Litigating, create an item in an escalation board and notify leadership. Create a Dashboard with: Stakeholders by Relationship Status (pie chart), Commitments by Status (bar chart), Overdue Commitments (table), Engagement Activity This Month (numbers), Regional Sentiment Map (chart grouped by region), Upcoming Engagements (calendar)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Community Pulse Monitor

**Agent Purpose:** Track community sentiment across operating regions, identify emerging concerns before they escalate, ensure community commitments are delivered on time, and recommend proactive engagement strategies.

**Triggers:**
- Community Commitment Delivery Deadline within 30/14/7 days
- Relationship Status changes to Concerned, Opposed, or Litigating
- Local media article mentioning company and community concern keywords detected
- Social media posts from community stakeholders mentioning company assets
- Monthly community sentiment analysis report schedule

**Actions:**
- Generate early warning alerts when multiple stakeholders in the same region shift from Neutral to Concerned within a 30-day period
- Create proactive engagement recommendations based on upcoming project milestones that may affect communities
- Draft community communication materials (town hall invitations, project update letters, FAQ documents) based on known stakeholder concerns
- Compile commitment delivery status reports and flag at-risk commitments with remediation recommendations
- Cross-reference new project proposals against existing stakeholder database to identify potential supporters and opponents
- Generate tribal consultation timeline and requirement checklists for new projects based on geographic and regulatory analysis

**Data Required:**
- Community Stakeholders database with full engagement history
- Community Commitments tracker
- Local media monitoring feeds for operating regions
- Social media monitoring for company and facility mentions
- Project pipeline data with geographic footprints
- Regulatory requirements database for community engagement (NHPA, NEPA, state-specific)

**Autonomy Level:** Human-in-the-Loop
Monitoring, analysis, and reporting are fully autonomous. Engagement recommendations and communication drafts require community relations manager review. All community-facing communications require human approval. Tribal consultation activities follow strict human-led protocols.

**Example Interaction:**
> The Community Pulse Monitor detects a pattern: in the last 3 weeks, three separate stakeholders in Jefferson County, TX — the Sierra Club local chapter, the Jefferson County Residents Association, and County Commissioner Patricia Williams — have all shifted from "Neutral" to "Concerned" in the Stakeholder Database. The common thread: the company's proposed expansion of the Port Arthur LNG export terminal. The agent correlates this with local media coverage showing increased community concern about air quality impacts and generates an alert to the Community Relations Manager for the Gulf Coast region. It recommends: (1) Schedule a community open house within 2 weeks, (2) Prepare updated air quality monitoring data from the existing facility to share, (3) Proactively reach out to Commissioner Williams for a private briefing before the next County Commissioners Court meeting, and (4) Review the Community Benefit Agreement to ensure all current commitments are on track — the agent notes that a commitment to fund air quality monitors at two local schools is showing as "In Progress" with the delivery deadline in 10 days.

---

### Use Case 7: Social Media Command Center & Reputation Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies on social media face a unique challenge: they're simultaneously promoting their brand, defending against activist campaigns, communicating during operational emergencies, engaging with investors, and recruiting talent — all on platforms where a single misstep can go viral. Oil & gas companies regularly face coordinated campaigns from climate activists, while utilities deal with customer outrage during rate hikes and outages. Most energy PR teams manage social media through a combination of Sprout Social or Hootsuite (for scheduling), separate monitoring tools, and manual processes for approval of any post that touches sensitive topics (which is nearly every post). The approval chain is so cumbersome that opportunities for real-time engagement are lost, and crisis response on social channels lags behind traditional media response.

#### The Solution
monday.com Work Management as a Social Media Command Center. **Content Calendar** board: Post Content (long text), Platform (dropdown: LinkedIn, X/Twitter, Facebook, Instagram, YouTube, TikTok), Campaign/Theme (dropdown: Brand, ESG/Sustainability, Safety, Recruitment, Investor Relations, Community, Crisis Response, Executive Thought Leadership), Approval Status (status: Draft, PR Review, Legal Review, Exec Review, Approved, Scheduled, Published), Scheduled Date/Time, Target Audience, Engagement Metrics (subitems: Impressions, Clicks, Shares, Comments, Sentiment). **Monitoring & Response** board: Detected Post/Mention, Platform, Sentiment (status: Positive, Neutral, Negative, Crisis), Category, Response Required (checkbox), Response Status, Assigned Responder, Approved Response. **Campaign Performance** board with dashboards showing engagement trends, sentiment analysis, and campaign ROI. Pre-approved response templates for common scenarios (outage complaints, activist posts, job inquiries).

#### The Outcome
50% faster social media response time during crises through pre-approved response templates and streamlined approval workflows. Unified content calendar across all platforms eliminating scheduling conflicts. Real-time sentiment monitoring replacing expensive standalone tools. Data-driven content strategy based on actual engagement metrics by theme and platform.

#### Discovery Questions
1. "How long does it take to get a social media post approved if it mentions anything related to emissions, rates, or an ongoing regulatory matter?"
2. "When climate activists coordinate a campaign against your company on Twitter, what's your response protocol? Do you engage, or go silent?"
3. "How do you manage the tension between your corporate social media presence and your CEO's personal LinkedIn where they post about energy transition topics?"
4. "During your last major outage or incident, how quickly were you posting updates on social media vs. issuing traditional press statements?"
5. "What's your social media tech stack right now, and how much are you spending on scheduling, monitoring, and analytics tools separately?"

#### Industry Context
Energy companies on social media face unique risks: Securities regulations limit what can be said about financial performance or M&A on social channels. FERC and SEC have specific guidelines about material information disclosure. Climate activist organizations (350.org, Greenpeace, Sunrise Movement) frequently target energy companies with coordinated social media campaigns. "Astroturfing" accusations arise when energy companies promote their positions through affiliated groups. Executive social media (especially LinkedIn) has become a primary channel for energy industry thought leadership and talent recruitment. SEs should understand that energy social media is more regulated and politically charged than in most industries.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Social Media Command Center for an energy company PR team. Create a board called 'Social Media Content Calendar' with columns: Post Content (long text), Platform (dropdown: LinkedIn, X/Twitter, Facebook, Instagram, YouTube, TikTok), Content Type (dropdown: Original Post, Share/Repost, Video, Infographic, Poll, Story/Reel, Thread, Executive Post), Campaign Theme (dropdown: Brand Awareness, Energy Transition/ESG, Safety Culture, Talent Recruitment, Investor Relations, Community Impact, Thought Leadership, Product/Service, Crisis Response), Sensitivity Level (dropdown: Low - Auto-Approve, Medium - PR Review, High - Legal Required, Critical - Exec Required), Approval Status (status: Draft, Content Review, Legal Review, Exec Approval, Approved, Scheduled, Published, Paused), Scheduled DateTime (date), Author (people), Approver (people), Platform-Specific Hashtags (text), Connected Campaign (connect board), Impressions (numbers), Engagement Rate (numbers), Sentiment (dropdown: Positive, Neutral, Mixed, Negative). Create a board called 'Social Monitoring & Response' with columns: Detected Content (long text), Platform (dropdown), Author/Account (text), Follower Count (numbers), Sentiment (status: Positive - Green, Neutral - Yellow, Negative - Orange, Crisis - Red), Category (dropdown: Customer Complaint, Activist Campaign, Media Inquiry, Investor Question, Job Seeker, Positive Mention, Misinformation, Troll), Response Required (status: Yes, No, Monitoring), Assigned Responder (people), Response Status (status: Pending, Drafting, Approved, Sent, Escalated), Response Content (long text), Response Time (numbers in minutes). Add automations: when Sensitivity Level is Critical, add Legal and Exec as approvers automatically; when Sentiment in Monitoring board is Crisis and Follower Count > 10000, immediately notify PR Director; when Scheduled DateTime is within 24 hours and Approval Status is not Approved, escalate. Create a Dashboard with: Posts by Platform (chart), Engagement Rate by Theme (bar chart), Response Time Average (number widget), Sentiment Distribution This Week (pie chart), Upcoming Scheduled Posts (table), Active Crisis Monitoring Items (filtered table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Social Sentinel

**Agent Purpose:** Monitor social media mentions of the company and key assets in real-time, assess sentiment and crisis potential, draft responses using pre-approved templates, and identify trending narratives before they peak.

**Triggers:**
- New mention detected via social monitoring integration (continuous)
- Mention volume spike (>200% above daily average within 1 hour)
- Negative sentiment mention from account with >50K followers
- Keyword detection for crisis terms (spill, leak, explosion, outage, contamination, death, injury, lawsuit)
- Scheduled daily social media briefing generation

**Actions:**
- Categorize and triage incoming mentions by sentiment, crisis potential, and response priority
- Draft responses for common scenarios using pre-approved template library (customer complaints, job inquiries, positive engagement)
- Generate real-time crisis alerts when mention volume or negative sentiment exceeds thresholds
- Identify coordinated campaign patterns (multiple accounts posting similar content within a short timeframe)
- Recommend content calendar adjustments when a planned post might conflict with a developing narrative
- Compile daily and weekly social performance reports with trending topic analysis

**Data Required:**
- Social media monitoring API feeds (all major platforms)
- Pre-approved response template library by scenario type
- Crisis communication protocols and escalation thresholds
- Executive social media account details and posting schedules
- Competitor social media activity feeds
- Historical social media engagement data

**Autonomy Level:** Human-in-the-Loop
Monitoring, categorization, and analysis are fully autonomous. Response drafts for low-risk positive mentions can be auto-posted after initial training period. All responses to negative mentions, media inquiries, and crisis-related content require human approval. Crisis alerts are fully autonomous with immediate escalation.

**Example Interaction:**
> At 3:15 PM, the Social Sentinel agent detects a mention volume spike: a Greenpeace Twitter/X account with 2.1M followers has posted a thread with aerial drone footage of what they claim is a "massive methane plume" from the company's Permian Basin operations, accompanied by #ClimateAccountability. Within 20 minutes, the thread has 3,400 retweets and 1,200 quote tweets. The agent immediately: (1) Creates a Crisis-level item in the Social Monitoring board, (2) Alerts the PR Director, VP Communications, and on-call Legal counsel, (3) Identifies that the aerial footage location matches the company's Reeves County facility, (4) Pulls the latest LDAR (Leak Detection and Repair) inspection report for that facility from the ESG Commitments Registry showing compliance, (5) Drafts a response: "We take methane emissions seriously. Our Reeves County facility passed its most recent LDAR inspection on [date] and operates within all EPA requirements. We're investigating this footage and will provide an update within 2 hours. Our methane intensity is [X]% below the industry average. Details: [link]." The agent also recommends pausing a scheduled LinkedIn post about the company's ESG report that was set for 4:00 PM, as it could appear tone-deaf given the developing situation.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Social License to Operate (SLO) | The ongoing acceptance of a company's operations by local communities and stakeholders — not a legal permit, but the informal community permission that enables operations |
| FERC | Federal Energy Regulatory Commission — regulates interstate electricity transmission and wholesale sales, natural gas pipelines and pricing |
| PHMSA | Pipeline and Hazardous Materials Safety Administration — federal agency regulating pipeline safety |
| PUC | Public Utility Commission — state-level regulatory body overseeing retail electric and gas rates and service quality |
| NRC | National Response Center — federal point of contact for reporting oil, chemical, radiological, biological, and etiological discharges |
| JIC | Joint Information Center — centralized communications hub during multi-agency incident response under NIMS/ICS |
| ICS | Incident Command System — standardized emergency management framework used across the energy industry |
| TCFD | Task Force on Climate-related Financial Disclosures — framework for climate risk reporting expected by institutional investors |
| SASB | Sustainability Accounting Standards Board — industry-specific ESG disclosure standards used by investors |
| CDP | Carbon Disclosure Project — global environmental disclosure system; CDP scores are tracked by institutional investors |
| LDAR | Leak Detection and Repair — regulatory requirement for monitoring and fixing fugitive emissions from oil & gas equipment |
| CERAWeek | The premier annual energy industry conference hosted by S&P Global in Houston — the "Davos of energy" |
| Flaring | Controlled burning of natural gas at production or processing sites — highly visible and politically sensitive |
| Rate Case | Formal regulatory proceeding where a utility requests approval to change its customer rates |
| CBA | Community Benefit Agreement — formal agreement between a company and community group specifying commitments in exchange for project support |
| Upstream | Exploration and production of oil and gas |
| Midstream | Transportation, storage, and wholesale marketing of crude/refined petroleum products and natural gas |
| Downstream | Refining, processing, and distribution of petroleum products and natural gas to end consumers |
| Toolbox Talk | Brief daily safety and operational briefing conducted at the start of work shifts in field operations |
| NHPA Section 106 | National Historic Preservation Act requirement for consultation with indigenous communities when federal actions may affect cultural resources |
| Greenwashing | Misleading claims about a company's environmental practices or the environmental benefits of a product or service |
| Scope 1/2/3 Emissions | Scope 1: Direct emissions from owned operations. Scope 2: Indirect emissions from purchased energy. Scope 3: All other indirect emissions in the value chain |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/SVP Communications | Owns corporate narrative, crisis communications strategy, executive positioning | Decision-maker |
| Director of Media Relations | Manages journalist relationships, press releases, media strategy | Decision-maker for media tools |
| Director of Community Relations | Manages community stakeholder engagement, social license to operate | Influencer — drives community-facing requirements |
| Manager of Internal Communications | Oversees employee communications across distributed workforce | Influencer — drives internal comms requirements |
| Director of Government Affairs | Coordinates regulatory and legislative engagement, political positioning | Influencer — drives regulatory tracking needs |
| ESG/Sustainability Communications Lead | Manages all ESG-related messaging and disclosures | Influencer — drives ESG content management needs |
| Social Media Manager | Manages social media presence, content calendar, community management | User — primary daily operator |
| VP/SVP Investor Relations | Manages financial communications, earnings materials, investor engagement | Decision-maker for financial comms tools (adjacent) |
| Chief Communications Officer (CCO) | Executive sponsor for all communications functions | Executive sponsor |
| General Counsel | Approves all external communications for legal and regulatory risk | Gatekeeper — approval authority |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Legal | Reviews all external communications for regulatory compliance; manages litigation hold communications | Cross-sell compliance workflow management; legal review automation |
| Government Affairs | Coordinates regulatory engagement messaging; testifies at hearings | Cross-sell regulatory proceeding tracker; hearing preparation workflows |
| Investor Relations | Financial communications, earnings materials, ESG investor engagement | Cross-sell IR workflow management; earnings process automation |
| Operations | Source of incident information, safety data, operational milestones | Cross-sell operations management; incident management integration |
| Human Resources | Employee engagement programs, recruitment marketing, workforce diversity communications | Cross-sell HR workflows; employee engagement tracking |
| Sustainability/ESG | Provides ESG data, targets, and progress for communications | Cross-sell ESG data management; sustainability reporting workflows |
| IT | Manages digital signage, intranet, and communications technology infrastructure | Cross-sell IT service management; digital workplace tools |
| Executive Office | CEO and C-suite communications, board communications, thought leadership | Cross-sell executive workflow management; board reporting |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Meltwater / Cision | Media monitoring and journalist databases | monday.com replaces the CRM/relationship management layer; monitoring feeds integrate via API; saves $50-150K/year in redundant seats |
| Sprout Social / Hootsuite | Social media scheduling and analytics | monday.com provides unified content calendar with approval workflows that social tools lack; integrate social scheduling via API |
| SharePoint/Confluence | Crisis playbook storage and internal wiki | monday.com replaces static document storage with live, actionable workflows with real-time status tracking |
| Staffbase / Poppulo | Internal communications platforms | monday.com provides planning, approval, and measurement workflow; can integrate with existing distribution tools rather than replace them |
| Salesforce (PR/Comms modules) | CRM-based media relations | monday.com offers better workflow flexibility, visual management, and significantly lower cost than Salesforce for PR use cases |
| Asana / Wrike | General project management for PR teams | monday.com offers superior customization, industry-specific templates, and AI capabilities that generic PM tools lack |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Meltwater/Cision for media management" | "Those tools are great for monitoring and database access, but they don't manage the workflow of how your team actually responds — the drafting, approval chains, and strategic planning. monday.com becomes the orchestration layer that makes those investments work harder. Most of our energy clients integrate rather than replace." |
| "Our crisis management process is too sensitive for a cloud platform" | "monday.com offers enterprise-grade security including SOC 2 Type II, HIPAA compliance capabilities, and granular permissions. Your crisis boards can be locked to specific team members with view-only access for leadership. The question is: is your current process — email chains and phone trees — actually more secure, or just less visible?" |
| "Our Legal department will never approve real-time communications tools" | "That's exactly why the approval workflow is built in. Legal gets visibility and control they don't have today — no communication goes out without their explicit approval in the system. It actually gives Legal more control, not less, plus an audit trail they'll love during regulatory inquiries." |
| "We're an energy company — our needs are too specialized for a general platform" | "That's the advantage of monday.com's flexibility — it adapts to your specific regulatory, operational, and stakeholder requirements rather than forcing you into a generic PR workflow. The Vibe coding capability means we can build energy-specific applications in minutes, not months." |
| "We can't put sensitive regulatory strategy information in a third-party tool" | "The regulatory tracker can be configured with permission levels — PR sees communications implications while sensitive legal strategy notes remain in your legal systems. The connect boards feature lets you reference proceedings without exposing privileged information." |
| "Our field workforce doesn't use computers — how does this help with internal comms?" | "monday.com is the planning and orchestration layer — you plan, approve, and track communications here, then distribute through whatever channels reach your field workers: digital signage integration, SMS gateway, supervisor cascade lists, and toolbox talk scripts. The measurement comes back into monday.com so you finally know what's actually reaching the field." |

## Proof Points
*(To be populated with customer references)*
- [Energy company using monday.com for crisis communications workflow]
- [Utility company managing regulatory communications through monday.com]
- [Oil & gas company consolidating PR tech stack with monday.com]
- [Energy company using monday.com for ESG reporting coordination]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
