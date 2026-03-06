# Investment Banking × Creative & Design Playbook

## Overview

Creative and Design teams within investment banking institutions are the visual architects of deal-making. They produce the pitch books, credentials decks, market updates, tombstone announcements, and client-facing presentations that drive revenue generation. Unlike creative departments in consumer brands, IB creative teams operate under extreme time pressure — a Managing Director may request a 60-page pitch book with custom financial analysis, market comps, and deal structure diagrams by 7:00 AM the next morning. The output must be pixel-perfect, brand-compliant, and factually precise, because these materials go directly to C-suite executives and boards of directors making billion-dollar decisions.

The typical IB creative/design function includes presentation specialists (often called "deck production" or "graphics"), desktop publishing professionals, brand managers, and increasingly, digital content creators for the firm's thought leadership and marketing efforts. At bulge-bracket firms, this team may be 30-80+ people operating across time zones in a "follow-the-sun" model — New York hands off to London, London to Mumbai, Mumbai back to New York — ensuring 24/7 production capacity during peak deal periods. The team sits organizationally under Marketing, Corporate Communications, or sometimes directly under the COO, but their primary clients are the revenue-generating bankers.

The fundamental tension in IB creative is between quality and speed. Bankers expect agency-level design quality delivered in hours, not weeks. Production queues regularly hit 50-100+ active requests during peak periods (January for annual reviews, quarterly for market updates, and constantly for live deal materials). Without sophisticated workflow management, the team becomes a bottleneck — and when the pitch book is late, the MD doesn't blame the creative team's capacity constraints; they escalate to the COO. Managing this demand, maintaining quality, enforcing brand standards, and preventing burnout in a 24/7 operation is the central challenge.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Creative teams face exponentially growing demand as deal activity intensifies, but headcount budgets are flat — AI-powered workflows can multiply output capacity 2-3x |
| 2 | Replace or Radically Augment Headcount | High | Repetitive production tasks (template population, chart formatting, brand compliance checks) consume 40-60% of specialist time and are prime for AI augmentation |
| 3 | Consolidate Tech Stack with AI | Medium | Teams juggle request intake (email/Slack), project tracking (spreadsheets), asset management (shared drives), and production tools (PowerPoint, InDesign, Figma) — unified workflow reduces context-switching |

## Prioritized Use Cases

---

### Use Case 1: Pitch Book & Presentation Production Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Pitch book production is the lifeblood of investment banking creative teams. A typical bulge-bracket firm produces 2,000-5,000+ pitch books annually, each requiring custom financial analysis pages, market overview slides, credentials/tombstone pages, team biographies, and deal structure diagrams. Requests arrive via email, Slack, phone calls, and hallway conversations — there's no standardized intake process. Bankers provide incomplete briefs ("make it look like the Goldman deck we saw last week"), expect instant turnaround, and frequently change requirements mid-production.

The result is chaos: duplicate requests go undetected, priority conflicts arise when two MDs both claim their pitch is "the most important," resource allocation is done by whoever shouts loudest, and quality suffers when specialists rush to meet impossible deadlines. Production managers spend 30%+ of their time triaging requests, chasing bankers for missing information, and manually tracking job status in spreadsheets. The team has no visibility into total capacity utilization, making it impossible to push back on unrealistic timelines with data.

#### The Solution
monday.com Work Management as the centralized pitch book production pipeline. A standardized intake form captures: requesting banker, client name, presentation type (credentials pitch, live deal, market update, board presentation), page count estimate, required sections, financial data status, deadline, and priority justification. Each request flows through a structured pipeline: Intake → Brief Review → Resource Assignment → Production → Internal QC → Banker Review → Revisions → Final Delivery. People columns assign production specialists; timeline views show resource loading. Automations enforce minimum lead times by presentation type, auto-assign based on specialist expertise (financial charts vs. infographics vs. layout), and send deadline warnings. A Dashboard gives the Creative Director real-time visibility into queue depth, capacity utilization, turnaround times, and revision rates.

#### The Outcome
40% reduction in production cycle time through elimination of intake chaos. Data-driven capacity planning — Creative Director can demonstrate to COO exactly when the team is at 120% capacity and needs overflow support. 60% reduction in "incomplete brief" issues through mandatory intake fields. Banker satisfaction increases as they get real-time status visibility instead of emailing "where's my deck?" Priority conflicts resolved through transparent, data-backed queue management.

#### Discovery Questions
1. "How many presentation requests does your creative team handle per month, and what's the breakdown between pitch books, market updates, and deal materials?"
2. "When two Managing Directors both need their pitch books by tomorrow morning, how does your team decide who gets priority?"
3. "What percentage of production time is spent on revisions versus initial production — and are most revisions due to scope changes or quality issues?"
4. "How does your team currently track capacity — can you tell me right now what your utilization rate is this week?"
5. "Have you ever had a situation where a pitch was delayed because the creative team was overloaded? What was the business impact?"

#### Industry Context
Pitch books in investment banking serve specific purposes: "credentials decks" showcase the firm's deal experience to win mandates; "management presentations" are prepared for sell-side processes where the target company presents to potential buyers; "CIMs" (Confidential Information Memorandums) are comprehensive documents describing a company for sale; "board books" present strategic alternatives to client boards. The "follow-the-sun" production model leverages global teams across time zones. "Tombstones" are deal announcement graphics commemorating closed transactions — they serve as both marketing materials and attorney-verified deal records.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Pitch Book Production Pipeline. Create a board called 'Presentation Production Queue' with columns: Job Title (text), Requesting Banker (people), Banker Title (dropdown: Analyst, Associate, VP, Director, MD, Partner), Client Name (text), Presentation Type (dropdown: Credentials Pitch, Live Deal Materials, Management Presentation, CIM, Market Update, Board Presentation, Tombstone, Annual Review, Other), Estimated Pages (numbers), Priority (status: Standard 5-Day/Rush 48hr/Emergency Overnight), Stage (status: Intake/Brief Review/Resource Assignment/In Production/Internal QC/Banker Review/Revisions/Final Delivery), Assigned Specialist (people), QC Reviewer (people), Submission Date (date), Deadline (date), Delivery Date (date), Turnaround Days (formula), Revision Count (numbers), Brief Complete (checkbox), Financial Data Ready (checkbox), Files (file). Add automations: when new item created without Brief Complete checked, notify Requesting Banker 'Please complete brief before production begins'; when Priority is 'Emergency Overnight', notify Creative Director immediately; when Stage is 'Banker Review' for >24 hours, send reminder to Requesting Banker; when Revision Count exceeds 3, notify Creative Director. Create a Kanban view by Stage, a Timeline view showing all active jobs and specialist assignments, a Workload view by Assigned Specialist, and a Dashboard showing queue depth, average turnaround by type, revision rates, and capacity utilization."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pitch Production Orchestrator
**Agent Purpose:** Intelligently triage incoming presentation requests, optimize resource allocation, and predict capacity bottlenecks before they impact delivery.

**Triggers:**
- New presentation request submitted via intake form
- Specialist completes a job (triggers rebalancing check)
- Daily 6:00 AM capacity forecast
- Deadline within 24 hours with job not in QC or later stage

**Actions:**
- Analyze incoming request and auto-categorize complexity (Simple: template population; Medium: custom charts/layout; Complex: full custom design)
- Recommend optimal specialist assignment based on expertise match, current workload, and time zone coverage
- Generate daily capacity forecast: "Team is at 85% utilization today, 110% tomorrow — recommend activating Mumbai overflow for 3 standard jobs"
- Auto-detect incomplete briefs and send targeted follow-up questions to requesting banker
- Produce weekly production analytics for Creative Director: volume trends, turnaround benchmarks, revision drivers

**Data Required:**
- Specialist skill profiles (financial charting, infographics, layout, InDesign, PowerPoint)
- Historical job data for complexity estimation and turnaround benchmarking
- Specialist availability/calendar data
- Template library inventory

**Autonomy Level:** Human-in-the-Loop
Triage, categorization, and specialist recommendations are autonomous. Final resource assignment requires Production Manager approval. All overnight/emergency escalations notify Creative Director for confirmation.

**Example Interaction:**
> At 4:30 PM New York time, three new requests hit the queue simultaneously: (1) An MD in Healthcare M&A needs a 40-page credentials deck by 9:00 AM tomorrow, (2) A VP in TMT needs a market update by end of week, and (3) An Associate needs tombstone graphics for a closed deal — no rush. The Pitch Production Orchestrator analyzes: "Request #1: Complex — requires custom healthcare sector charts and recent deal tombstones. Recommend assigning to Senior Specialist [Name] for financial pages and routing infographics to London team for overnight completion. Request #2: Medium complexity — standard market update template with custom data. Queue for Thursday production. Request #3: Simple — template tombstone. Route to Mumbai team during their business hours." It auto-assigns and notifies all parties. The MD receives: "Your credentials deck is confirmed for 8:30 AM delivery. Senior Specialist [Name] will handle financial analysis pages; London team will complete market overview and credentials sections overnight."

---

### Use Case 2: Brand Compliance & Template Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banks invest millions in brand identity — precise color palettes, typography, chart styles, and layout standards that convey institutional credibility. Yet maintaining brand compliance across thousands of presentations produced annually is nearly impossible with manual processes. Bankers frequently modify templates themselves (changing fonts, using off-brand colors, inserting low-resolution logos), creating "Frankenstein decks" that go to clients bearing the firm's name but not its standards.

The template management challenge compounds the problem: firms may maintain 50-100+ master templates across product groups, regions, and presentation types. When the brand team updates the master template (new logo, updated color palette, revised disclaimers), propagating changes across all active templates and in-progress presentations is a months-long manual effort. During a rebrand, the creative team may spend 6-12 months converting legacy materials — all while continuing to produce new work at full speed.

#### The Solution
monday.com Work Management as the template governance and brand compliance tracking system. A template registry board catalogs every active template: template name, version, product group, last updated date, brand compliance status, and download link. When brand updates occur, automations create update tasks for each affected template, assign owners, and track completion. A brand compliance review workflow routes completed presentations through automated checks (via integration with brand compliance tools) and human QC review. Non-compliant elements are flagged with specific remediation instructions. Dashboard views show compliance rates by product group, template currency (% of templates on latest version), and common violation patterns.

#### The Outcome
95%+ brand compliance rate across all client-facing materials (up from estimated 60-70%). Template update propagation time reduced from months to weeks. Creative team spends 50% less time fixing brand violations after the fact. Brand team gains data-driven insight into which product groups need additional training or support.

#### Discovery Questions
1. "When your firm last updated its brand guidelines or logo, how long did it take to propagate the changes across all presentation templates?"
2. "What's your current process for ensuring a pitch book meets brand standards before it goes to a client?"
3. "How many master templates does your creative team maintain, and how do you version-control them?"
4. "Have you ever had an embarrassing situation where off-brand materials went to a high-profile client? How was it handled?"
5. "Do bankers ever create their own presentations outside of the official templates? How prevalent is that?"

#### Industry Context
Investment bank brand identity is a strategic asset — brand perception directly influences mandate wins. "Credentials sections" of pitch books are particularly brand-sensitive as they represent the firm's track record. Major IB rebrands (e.g., post-merger identity consolidation) are multi-year, multi-million-dollar projects. "Disclaimer pages" are legally required on all client-facing materials and must be current — an outdated disclaimer can create legal liability. Template hierarchies typically follow: Global Master → Regional Variant → Product Group Variant → Individual Presentation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Brand Compliance & Template Management system. Create a board called 'Template Registry' with columns: Template Name (text), Template ID (text), Product Group (dropdown: M&A, ECM, DCM, Leveraged Finance, Restructuring, Equity Research, Fixed Income, Corporate), Region (dropdown: Americas, EMEA, APAC, Global), Format (dropdown: PowerPoint, InDesign, Word, PDF), Current Version (text), Last Updated (date), Brand Compliant (status: Compliant/Update Needed/Under Review/Deprecated), Owner (people), Download Link (link), Change Log (long text). Create a connected board called 'Brand Compliance Reviews' with columns: Presentation Name (text), Submitting Team (dropdown), Reviewer (people), Submission Date (date), Review Status (status: Queued/In Review/Compliant/Violations Found/Remediated), Violations Found (numbers), Violation Types (dropdown multi-select: Color Palette, Typography, Logo Usage, Chart Style, Disclaimer, Layout, Image Quality), Remediation Notes (long text), Turnaround Hours (formula). Add automations: when a new Brand Update is published (separate trigger board), create Update Needed tasks for all affected templates; when Violations Found > 0, notify submitting team with remediation instructions; weekly compliance digest to Brand Director. Create a Dashboard showing compliance rates by product group, common violation types, template currency rates, and review turnaround times."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Brand Guardian Agent
**Agent Purpose:** Automatically scan presentations for brand compliance violations, recommend fixes, and maintain template version currency.

**Triggers:**
- Presentation uploaded for QC review
- Brand guidelines updated (triggers template audit)
- Monthly template currency audit
- New template created (triggers compliance validation)

**Actions:**
- Scan uploaded presentations against brand standards: verify color codes, fonts, logo placement, chart formatting, and disclaimer currency
- Generate violation report with specific slide numbers, violation types, and auto-suggested fixes
- Track template version currency and flag templates more than one version behind current brand standards
- Auto-generate brand compliance scorecards by product group for quarterly brand reviews
- Detect and flag "rogue templates" — presentations that don't match any registered template

**Data Required:**
- Current brand guidelines (color codes, fonts, logo specs, chart standards)
- Template registry with version history
- Disclaimer library with expiration dates
- Historical compliance data for trend analysis

**Autonomy Level:** Fully Autonomous (for scanning), Human-in-the-Loop (for remediation)
Brand scanning and violation detection are fully automated. The agent generates specific fix recommendations, but production specialists execute the changes. Deprecated templates are flagged but only archived with Brand Director approval.

**Example Interaction:**
> A Senior Associate in the DCM group uploads a 35-page bond issuance pitch book for QC review. The Brand Guardian Agent scans it in under 60 seconds and returns: "Brand Compliance Score: 78/100. 7 violations detected: (1) Slides 4, 12, 18: Using deprecated blue (#1B3A5C) instead of current brand blue (#1A2E4A) — likely copied from pre-2025 template. (2) Slide 8: Chart uses 5 colors but brand standard allows maximum 4 per chart — recommend consolidating smallest two categories. (3) Slides 1, 35: Disclaimer text is version 3.1, current is 3.4 — updated language required for SEC marketing rule compliance. (4) Slide 22: Logo appears at 85% minimum size — resize to 100%. All other elements compliant. Estimated remediation time: 25 minutes." The QC specialist clicks "Apply Auto-Fixes" for color corrections and disclaimer updates, then manually adjusts the chart and logo.

---

### Use Case 3: Digital Asset & Content Library Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Investment banking creative teams maintain vast libraries of reusable assets: deal tombstone graphics, sector overview slides, executive biography pages, market data charts, infographic templates, photography, and firm credential pages. These assets are typically scattered across shared drives, email archives, individual desktops, and legacy presentation files. When a banker needs "that great healthcare sector slide from the PharmaCo pitch last year," the creative team may spend 30-60 minutes searching — or worse, recreate it from scratch because nobody can find the original.

The problem intensifies with version control: the same chart may exist in 15 different presentations with slightly different data vintages, and there's no clear way to identify which is current. Photography licensing adds legal risk — using an expired stock image in a client presentation can result in licensing claims. And when a key deal closes, creating tombstone graphics and updating credentials across all relevant templates is a manual, error-prone process.

#### The Solution
monday.com Work Management as the asset library catalog and content management workflow. Each asset type gets a dedicated board: Tombstones, Sector Slides, Market Charts, Photography, Executive Bios, and Infographic Templates. Items include: asset name, category, sector, file (latest version), created date, last updated, source presentation, usage rights/license expiration, and tags for searchability. When a deal closes, an automation triggered from the deal pipeline creates a tombstone production task with pre-populated deal details. A content refresh workflow schedules quarterly updates for market data slides. Integration with digital asset management (DAM) tools syncs file versions.

#### The Outcome
Asset search time reduced from 30-60 minutes to under 5 minutes. Zero licensing violations through proactive expiration tracking. Tombstone production time cut by 60% through automated deal data population. Quarterly content refresh ensures all reusable assets contain current data. Creative team reclaims 10-15 hours per week previously spent searching for and recreating assets.

#### Discovery Questions
1. "If I asked your team to find a specific deal tombstone from 18 months ago, how long would it take and where would they look?"
2. "How do you currently track licensing and usage rights for stock photography and other licensed content?"
3. "When a major deal closes, what's the process for creating tombstone graphics and updating credentials across all relevant pitch templates?"
4. "How often are your reusable market overview and sector slides refreshed with current data?"
5. "Have you ever had a situation where outdated data in a reused slide made it into a client presentation? What was the impact?"

#### Industry Context
"Tombstones" in investment banking are graphic representations of completed deals — they serve as both marketing materials and credibility signals. A firm's "credentials" (list of completed transactions) are its most important competitive asset. "League tables" rank banks by deal volume/value and are fiercely competitive — creative teams produce custom league table graphics for pitch books. Market data slides typically include: sector indices, M&A volume trends, IPO windows, credit spread charts, and economic indicators. Photography in IB materials typically includes: executive headshots, office/facility imagery, and abstract financial imagery for covers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Digital Asset & Content Library system. Create a board called 'Deal Tombstones' with columns: Deal Name (text), Client (text), Transaction Type (dropdown: M&A, IPO, Follow-On, Debt Issuance, Restructuring, Fairness Opinion), Deal Value (numbers, USD), Close Date (date), Sector (dropdown: Healthcare, TMT, Industrials, Consumer, Energy, Financial Institutions, Real Estate), Tombstone Graphic (file), Status (status: Pending Design/In Production/Approved/Published), Designer (people), Template Used (text), League Table Eligible (checkbox). Create a board called 'Reusable Content Library' with columns: Asset Name (text), Asset Type (dropdown: Sector Slide, Market Chart, Infographic Template, Executive Bio, Office Photography, Stock Image, League Table, Cover Template), Sector (dropdown), File (file), Version (text), Created Date (date), Last Updated (date), Next Refresh Date (date), License Expiry (date), Usage Rights (dropdown: Unlimited, Limited, Expires), Tags (tags), Source Presentation (text), Created By (people). Add automations: when License Expiry is within 30 days, notify Brand Manager; when Next Refresh Date arrives, create refresh task and assign to content owner; when new Tombstone status changes to 'Published', trigger credentials update task. Create a Gallery view for visual asset browsing, and a Dashboard showing asset counts by type, upcoming license expirations, overdue refreshes, and tombstone production pipeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Asset Librarian Agent
**Agent Purpose:** Maintain a searchable, current, and compliant content library by automating asset cataloging, version control, and licensing management.

**Triggers:**
- Deal closes (triggers tombstone creation workflow)
- Quarterly content refresh cycle
- License expiration approaching (60, 30, 7 days)
- New asset uploaded (triggers cataloging)
- Search request from production team

**Actions:**
- Auto-generate tombstone task with pre-populated deal details when a deal closes on the deal pipeline board
- Catalog newly uploaded assets with auto-suggested tags, sector classification, and metadata
- Monitor license expirations and flag at-risk assets with renewal or replacement recommendations
- Execute quarterly audit: identify stale assets (not updated in 6+ months), orphaned files, and duplicate assets
- Power natural language asset search: "Find the TMT sector overview slide with 2025 M&A volume data"

**Data Required:**
- Deal pipeline data for tombstone auto-population
- Asset metadata and file storage
- License/usage rights database
- Historical usage data (which assets are used most frequently)

**Autonomy Level:** Fully Autonomous
Asset cataloging, license monitoring, and search are fully automated. Tombstone design tasks are created autonomously but require designer completion. Asset deprecation recommendations require Brand Manager approval before removal.

**Example Interaction:**
> A VP in the TMT group messages the creative team: "I need the latest semiconductor M&A activity chart for a pitch tomorrow." The Asset Librarian Agent searches the content library and responds within seconds: "Found 3 semiconductor M&A charts: (1) 'Global Semiconductor M&A Volume 2020-2025' — last updated January 2026, used in 12 recent pitches ⭐ Recommended. (2) 'Semiconductor M&A by Deal Size' — last updated November 2025, data slightly stale. (3) 'Semiconductor Cross-Border M&A Trends' — last updated September 2025, scheduled for Q1 refresh. Asset #1 is current and recommended. Download link attached. Note: Q4 2025 data was incorporated in the January refresh."

---

### Use Case 4: Creative Request Intake & SLA Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The single biggest source of friction between investment banking creative teams and their internal clients (bankers) is the request process. Without a structured system, requests arrive through every possible channel: emails with vague subjects ("need a deck"), Slack messages at 11 PM, verbal requests in elevators, and forwarded email chains with "can you make this pretty?" attached. Each request lacks standardized information, forcing the creative team into time-consuming back-and-forth to clarify requirements.

SLA management is equally broken. The creative team has no way to enforce or even track service level commitments. Standard requests that should take 5 business days are routinely marked "urgent" by bankers who have learned that everything gets done faster with an urgency flag. Without data on actual turnaround times, capacity utilization, and request patterns, the Creative Director cannot have an informed conversation with banking leadership about resource needs, realistic timelines, or demand management.

#### The Solution
monday.com Work Management with monday.com Forms as the single point of intake. A mandatory creative request form with conditional logic captures all essential information upfront: requester, deal/client context, presentation type, content requirements (with checkboxes for standard sections), data availability, deadline, and priority with business justification. Submissions auto-create items on the production board with SLA timelines calculated based on request type and priority. Traffic light status columns show SLA health (On Track / At Risk / Breached). Automations enforce SLA rules: standard requests get 5 business days, rush gets 48 hours (requires Director-level approval), emergency overnight requires MD sign-off. Monthly SLA reports provide data for capacity planning conversations.

#### The Outcome
100% of requests captured with complete information — eliminating "ghost requests" and incomplete briefs. SLA compliance tracked and reported: target 90%+ on-time delivery. 25% reduction in production time through upfront brief completeness. Data-driven capacity conversations with banking leadership: "In Q4, we received 340 requests against a capacity of 280 — here's the overflow impact." Banker satisfaction improves through transparency — they can see their request status in real time.

#### Discovery Questions
1. "What channels do creative requests currently come through — email, Slack, verbal, something else?"
2. "Do you have formal SLAs for different request types? If so, what's your current compliance rate?"
3. "What percentage of requests arrive with all the information your team needs to begin production immediately?"
4. "How do you currently handle the 'everything is urgent' problem — when every banker marks their request as top priority?"
5. "When budget season comes around, how do you justify headcount needs for the creative team? What data do you use?"

#### Industry Context
Investment banking operates in a hierarchy-driven culture where Managing Directors' requests take implicit priority regardless of formal SLA structures. The creative team must navigate this political reality while maintaining fair queue management. "Pitch season" (typically January-February for annual reviews and September-October for budget presentations) creates predictable demand spikes. The "follow-the-sun" model creates additional complexity — requests may be initiated in New York, partially completed in London, and finished in Mumbai, requiring clear handoff protocols.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Creative Request Intake & SLA Management system. Create a monday.com Form called 'Creative Request Form' with fields: Your Name (people picker), Your Title (dropdown: Analyst, Associate, VP, Director, MD, Partner), Department (dropdown: M&A, ECM, DCM, Leveraged Finance, Restructuring, Equity Research, Sales & Trading), Client Name (text), Request Type (dropdown: New Pitch Book, Pitch Book Update, Market Update, CIM, Tombstone, Infographic, One-Pager, Other), Required Sections (checkboxes: Cover, Table of Contents, Market Overview, Sector Analysis, Company Overview, Financial Analysis, Credentials/Tombstones, Team Bios, Appendix, Disclaimer), Estimated Pages (number), Financial Data Ready (yes/no), Priority (dropdown: Standard 5-Day, Rush 48hr, Emergency Overnight), Priority Justification (text, required if Rush or Emergency), Deadline (date), Additional Notes (long text), Reference Materials (file upload). Create a board called 'Creative SLA Tracker' connected to this form with additional columns: SLA Deadline (formula based on Priority and submission date), SLA Status (status: On Track/At Risk/Breached, auto-calculated), Assigned To (people), Stage (status: Queued/In Progress/QC/Client Review/Revisions/Delivered), Actual Delivery Date (date), SLA Met (checkbox, auto). Add automations: when Priority is 'Emergency Overnight', require MD approval before production begins; when SLA Status changes to 'At Risk', notify Production Manager; daily 8 AM summary of all At Risk and Breached items to Creative Director. Create a Dashboard showing SLA compliance rate, average turnaround by request type, request volume trends (weekly/monthly), and requester department breakdown."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Creative Traffic Controller
**Agent Purpose:** Manage the intake-to-delivery pipeline by validating requests, enforcing SLAs, and providing real-time status to requesters without creative team intervention.

**Triggers:**
- New request form submission
- SLA threshold approaching (50%, 75%, 90% of allotted time)
- Status update requested by banker (keyword detection in messages)
- Weekly analytics cycle

**Actions:**
- Validate incoming requests for completeness — auto-reply to banker with specific missing information if brief is incomplete
- Calculate and assign SLA deadline based on request type, priority, and current queue depth
- Respond to banker status inquiries with real-time updates: "Your Healthcare credentials deck is currently in QC review — estimated delivery by 3:00 PM today"
- Generate weekly demand analytics: request volume by department, priority distribution, SLA performance
- Predict capacity crunches based on incoming request patterns and flag to Creative Director 48 hours in advance

**Data Required:**
- Request form submissions with full metadata
- Production team capacity and schedule data
- Historical SLA performance data
- Banking team org chart (for priority validation)

**Autonomy Level:** Fully Autonomous
Request validation, SLA calculation, status responses, and analytics are fully automated. The agent doesn't make production decisions — it manages the administrative overhead around production.

**Example Interaction:**
> An Associate in the M&A group submits a creative request at 6:15 PM for a "New Pitch Book, Rush 48hr" for a healthcare credentials presentation. The Creative Traffic Controller processes the submission and responds within 2 minutes: "Thank you for your request. I've flagged two items that need attention before we can begin: (1) Financial Data Ready is marked 'No' — we'll need the data by 10:00 AM tomorrow to meet your 48-hour timeline. (2) You've selected 'Rush 48hr' priority — this requires Director-level approval per our SLA policy. I've sent an approval request to [Director Name]. Once both items are resolved, your SLA clock starts. Current queue position: #3 in Rush queue. Estimated delivery: Friday 6:00 PM, assuming brief completion by 10:00 AM tomorrow." The Associate immediately uploads the missing data, and the Director approves via mobile notification within 15 minutes.

---

### Use Case 5: Thought Leadership & Marketing Content Production

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Beyond deal-related materials, IB creative teams increasingly produce thought leadership content: market commentary reports, sector deep-dives, quarterly outlooks, podcast graphics, social media assets, event materials, and website content. This "always-on" content marketing requires a fundamentally different workflow than deal-driven pitch production — it involves editorial calendars, multi-stakeholder approval chains (Compliance, Legal, senior bankers as authors), and multi-format production (a single research piece may need to become a PDF report, a LinkedIn carousel, an email newsletter graphic, and a website banner).

The challenge is that thought leadership production competes for the same creative resources as deal-related work — and deal work always wins. Content calendars slip, quarterly reports publish late, and the firm's market presence suffers. Without a dedicated workflow, content production becomes reactive and inconsistent, undermining the firm's ability to build the brand awareness that drives mandate wins.

#### The Solution
monday.com Work Management as the content production and editorial calendar platform. A content calendar board manages the full pipeline: ideation, assignment, drafting, design, compliance review, legal review, approval, and publication. Each content piece tracks: topic, author (senior banker), ghostwriter, designer, target publication date, distribution channels, and format variants needed. Timeline views show the editorial calendar at a glance. Connected boards link to the design production queue so creative resources can be planned across both deal work and content work. Automations route compliance and legal reviews, track approval status, and trigger multi-format production when the master piece is approved.

#### The Outcome
Consistent content publication cadence — quarterly reports on time, every time. 30% increase in thought leadership output without additional headcount. Compliance review bottleneck eliminated through structured workflow (average review time from 5 days to 2 days). Creative resource planning across deal work and content work prevents conflicts. Marketing team gains visibility into pipeline for distribution planning.

#### Discovery Questions
1. "How does your firm currently manage the production pipeline for thought leadership content — research reports, market commentaries, and the like?"
2. "What's the typical timeline from content ideation to publication, and where are the biggest bottlenecks?"
3. "How do compliance and legal reviews factor into your content production timeline?"
4. "When a quarterly market report needs to become a LinkedIn post, an email graphic, and a website banner, how is that multi-format production managed?"
5. "How do you balance creative team capacity between deal-driven work and marketing content production?"

#### Industry Context
Investment bank thought leadership serves multiple purposes: establishing intellectual credibility with potential clients, maintaining relationships with existing clients, supporting recruiting (top talent wants to work at firms with market-leading insights), and regulatory positioning. Compliance review of marketing materials is mandatory under SEC marketing rules (Rule 206(4)-1) and FINRA communications rules. "Tombstone ads" in publications like The Wall Street Journal remain a traditional marketing channel. LinkedIn has become the dominant digital channel for IB thought leadership, with senior bankers as "author brands."

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Thought Leadership Content Production system. Create a board called 'Content Calendar' with columns: Content Title (text), Content Type (dropdown: Quarterly Market Report, Sector Deep-Dive, Market Commentary, Podcast Episode, Event Materials, Social Media Campaign, Newsletter, Website Feature), Author/SME (people), Ghostwriter (people), Designer (people), Target Publish Date (date), Stage (status: Ideation/Drafting/Design/Compliance Review/Legal Review/Final Approval/Published), Distribution Channels (dropdown multi-select: Website, LinkedIn, Email Newsletter, Client Portal, Print, Social Media), Format Variants Needed (dropdown multi-select: PDF Report, LinkedIn Carousel, Email Banner, Website Hero, Social Graphics, Video Thumbnail), Compliance Reviewer (people), Compliance Status (status: Not Submitted/Under Review/Approved/Changes Required), Legal Status (status: Not Submitted/Under Review/Approved/Changes Required), Final Approver (people), Notes (long text), Files (file). Add automations: when Stage changes to 'Compliance Review', assign Compliance Reviewer and set 48-hour deadline; when Compliance Status is 'Approved' and Legal Status is 'Approved', change Stage to 'Final Approval'; when Stage changes to 'Published', trigger multi-format production tasks for each selected Format Variant. Create a Timeline calendar view, and a Dashboard showing content pipeline by stage, compliance review turnaround, publication cadence (monthly), and content by type/channel."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Content Pipeline Agent
**Agent Purpose:** Orchestrate the end-to-end content production workflow from ideation through multi-format publication.

**Triggers:**
- New content item created in calendar
- Stage advancement (triggers next-stage tasks)
- Publication date approaching with content not in final stages
- Content published (triggers format variant production)

**Actions:**
- Generate production timeline based on content type template and target publish date
- Auto-route compliance and legal reviews with required materials packaged
- Create format variant production tasks when master content is approved (e.g., "Create LinkedIn carousel from Q1 Market Report — 10 slides, key data points extracted")
- Monitor publication cadence and alert if gaps exceed target frequency
- Generate monthly content performance summary for Marketing Director

**Data Required:**
- Content type templates with standard timelines
- Compliance and legal reviewer assignments
- Distribution channel specifications (image sizes, format requirements)
- Historical content performance data

**Autonomy Level:** Human-in-the-Loop
Workflow orchestration and task creation are autonomous. All content decisions (topic selection, messaging, design direction) require human creative input. Compliance and legal approvals are human gates that cannot be bypassed.

**Example Interaction:**
> The Content Pipeline Agent creates the Q2 2026 Market Outlook production plan: "Q2 Market Outlook — Target publish date: April 7, 2026. Production timeline generated: Week 1 (March 10-14): Author interview and data gathering. Week 2 (March 17-21): Ghostwriting first draft. Week 3 (March 24-28): Design and infographics. Week 4 (March 31-April 2): Compliance review (48hr SLA). April 3: Legal review. April 4: Final approval. April 7: Publication. Format variants to produce post-approval: (1) 24-page PDF report, (2) LinkedIn carousel (8 slides), (3) Email newsletter header graphic, (4) Website hero banner, (5) 3 social media pull-quote graphics. Assigned: [Ghostwriter], [Designer], [Compliance Reviewer]. All parties notified with deadlines."

---

### Use Case 6: Follow-the-Sun Production Handoff Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Many investment banking creative teams operate a "follow-the-sun" model with production centers in multiple time zones (typically New York, London, and Mumbai/Manila). This model is powerful in theory — 24-hour production capacity — but chaotic in practice. Handoffs between shifts are the critical failure point: incomplete context transfers, inconsistent quality standards, duplicated work, and the dreaded "it doesn't look like what I asked for" when the New York banker reviews work completed overnight in Mumbai.

Current handoff processes rely on email summaries, shared documents with notes, and morning standup calls. Information gets lost, nuances are misunderstood, and the team spends significant time each morning reconciling what was done overnight versus what was expected. For complex pitch books with specific banker preferences ("he likes the charts this way, not that way"), the loss of context across handoffs can result in full rework.

#### The Solution
monday.com Work Management as the structured handoff platform. Each active job has a detailed handoff log (updates section) with a standardized format: work completed, work remaining, specific instructions for next shift, banker preferences/quirks, and any blocking issues. Status columns show exactly which components of a presentation are complete vs. in progress vs. not started. File versioning tracks each shift's contributions. Automations trigger handoff notifications at shift boundaries (e.g., 5:00 PM NY → London picks up, 5:00 PM London → Mumbai picks up). A "Shift Dashboard" shows each production center their incoming work with full context.

#### The Outcome
Handoff-related rework reduced by 70%. Overnight production efficiency increases by 40% as teams receive clear, structured context. Banker satisfaction improves as "morning surprises" (unexpected overnight output) decrease. Production Manager gains visibility into cross-timezone workflow for the first time.

#### Discovery Questions
1. "Does your creative team operate across multiple time zones? If so, how do you manage work handoffs between shifts?"
2. "What's the most common cause of overnight rework — is it unclear instructions, quality inconsistency, or something else?"
3. "How do you capture and transfer banker-specific preferences across production shifts?"
4. "When a complex pitch book is being worked on across three time zones, who owns the overall quality and consistency?"

#### Industry Context
The follow-the-sun model originated in IB technology support but was adopted by creative teams to meet the industry's 24/7 demands. Production centers in India (Mumbai, Bangalore) and Philippines (Manila) offer cost advantages and English-language capability. Quality calibration across centers is an ongoing challenge — design sensibilities and presentation standards can vary culturally. "Night shift premiums" and "overnight desk" arrangements in onshore locations are alternatives to offshoring.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Follow-the-Sun Handoff Management system. Create a board called 'Shift Handoff Tracker' with columns: Job Reference (connect to Production Queue board), Current Shift Owner (people), Next Shift Owner (people), Handoff Time (date with time), Components Complete (dropdown multi-select: Cover, Market Overview, Financial Analysis, Credentials, Team Bios, Charts, Infographics, Layout, QC), Components In Progress (dropdown multi-select, same options), Components Not Started (dropdown multi-select, same options), Handoff Notes (long text), Banker Preferences (long text), Blocking Issues (long text), Handoff Quality Score (rating 1-5, rated by receiving shift), Files — Current Version (file). Add automations: at 5:00 PM EST, create handoff entries for all active jobs and notify London team; at 5:00 PM GMT, create handoff entries for Mumbai team; if Blocking Issues is not empty, notify Production Manager across all shifts; weekly summary of Handoff Quality Scores to Creative Director. Create a Dashboard showing active jobs by shift, handoff quality trends, rework rates by production center, and overnight completion rates."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Shift Handoff Agent
**Agent Purpose:** Ensure seamless production continuity across time zones by generating structured handoff packages and monitoring overnight quality.

**Triggers:**
- Shift boundary time (5:00 PM in each production center)
- Job assigned to overnight production
- Morning review period (receiving shift start)
- Handoff quality score below 3/5

**Actions:**
- Auto-generate structured handoff summary from job status, recent updates, and file version history
- Package banker preference notes from historical interactions on similar jobs
- Flag jobs requiring special attention (complex layouts, specific banker preferences, brand-sensitive materials)
- Monitor overnight work and compare against handoff instructions — flag deviations for morning review
- Aggregate handoff quality metrics for continuous improvement reporting

**Data Required:**
- Active job details and component-level status
- Banker preference history (accumulated from past jobs)
- Shift schedules and team assignments
- Historical handoff quality ratings

**Autonomy Level:** Fully Autonomous
Handoff documentation, notifications, and quality monitoring are fully automated. The agent surfaces information and flags issues but doesn't make production decisions.

**Example Interaction:**
> At 5:00 PM EST, the Shift Handoff Agent generates packages for 8 active jobs transitioning to the London team. For the highest-priority job — a 50-page Healthcare M&A credentials pitch due at 8:00 AM EST tomorrow — it generates: "Job #1247: Healthcare Credentials Pitch for [MD Name]. Status: 60% complete. Completed: Cover (approved), Market Overview (approved), Company profiles (3 of 5 done). Remaining for London shift: Complete 2 remaining company profiles (templates in Slide Master, data in attached Excel), begin Financial Analysis section (comps model attached — use standard bar chart format, NOT the waterfall chart style). ⚠️ BANKER NOTE: [MD Name] strongly prefers Gotham font for headers despite brand standard being Calibri — approved exception on file. Also prefers dark blue (#1A2B3C) chart backgrounds. Reference: Job #1189 from January for style precedent. Priority: Must be 90%+ complete before Mumbai handoff at 5 PM GMT. Blocking: None."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Pitch Book | Comprehensive presentation used to win advisory mandates — includes market analysis, credentials, and proposed deal strategy |
| CIM (Confidential Information Memorandum) | Detailed document describing a company for sale, distributed to potential buyers under NDA |
| Tombstone | Graphic representation of a completed deal, used in credentials sections and marketing |
| League Table | Industry ranking of banks by deal volume/value — produced by third parties (Bloomberg, Dealogic) and customized by creative teams |
| Credentials | The bank's track record of completed transactions, presented in pitch books to demonstrate capability |
| Management Presentation | Slide deck used by a company's management team to present to potential buyers in an M&A process |
| Follow-the-Sun | Production model utilizing teams in multiple time zones for 24-hour coverage |
| Board Book | Comprehensive package of materials prepared for board of directors meetings |
| Teaser | One-page anonymous summary of a company for sale, sent to prospective buyers before NDA execution |
| Comps (Comparable Analysis) | Financial analysis comparing similar companies or transactions — a core pitch book component |
| Football Field | Horizontal bar chart showing valuation ranges from different methodologies — iconic IB chart type |
| Waterfall Chart | Chart showing incremental positive/negative contributions to a total — common in bridge analyses |
| Red Herring / Preliminary Prospectus | Draft offering document filed with SEC, often designed by creative teams |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Creative Director / Head of Presentation Services | Overall creative operations, team management, brand standards | Decision-maker |
| Production Manager / Traffic Manager | Day-to-day workflow management, resource allocation, SLA tracking | Decision-maker/Champion |
| Brand Director / Manager | Brand standards, template governance, visual identity | Influencer |
| Chief Marketing Officer (CMO) | Marketing strategy, thought leadership direction, budget | Decision-maker |
| Chief Operating Officer (COO) | Operational efficiency, headcount decisions, vendor management | Decision-maker (budget) |
| Senior Presentation Specialist | Complex production, quality standards, mentoring junior staff | User/Influencer |
| Desktop Publishing Specialist | High-volume production, template work, formatting | User |
| Digital Content Producer | Website, social media, email marketing content | User |
| Managing Director (Banking) | Primary internal client, pitch book requester | Influencer (demand driver) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Investment Banking (all product groups) | Primary internal client — every pitch requires creative support | Production pipeline management extends banker-side into deal lifecycle |
| Marketing & Communications | Thought leadership, events, brand campaigns | Content calendar and campaign management on monday.com |
| Compliance | Marketing material review, advertising rules | Compliance review workflow streamlined on monday.com |
| IT / Technology | Production tools, DAM systems, infrastructure | IT service management and tool deployment on monday.com |
| Human Resources | Recruiting materials, employer branding, internal communications | Creative request management extends to internal brand |
| Legal | Disclaimer management, IP/licensing, trademark | Legal review workflow integrated into content production |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Workfront (Adobe) | Enterprise creative project management | monday.com offers equivalent workflow power with superior usability and faster deployment — Workfront implementations are notoriously complex |
| Asana / Wrike | Project management with creative workflow features | monday.com provides stronger visualization (Timeline, Workload views) critical for creative resource management |
| Bynder / Brandfolder | Digital Asset Management (DAM) | monday.com doesn't replace DAM but adds workflow orchestration — manage the process of creating, reviewing, and distributing assets |
| Templafy / Upslide | Presentation template management for Office | monday.com complements these tools by managing the workflow around template governance — which templates need updating, compliance tracking |
| Email / Slack / Spreadsheets | Status quo for many IB creative teams | Easiest displacement — demonstrate the cost of managing a 50-person 24/7 creative operation through email and spreadsheets |
| Jira | Used by some firms for creative ticketing | monday.com offers creative-team-friendly UX versus Jira's developer-oriented interface — creative teams adopt monday.com 3x faster |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "Our bankers won't fill out a form — they'll just email us anyway" | "That's exactly the problem we're solving. With monday.com Forms, the form is simpler and faster than writing an email — and bankers get real-time status updates they can't get via email. Most creative teams see 90%+ adoption within 60 days because bankers quickly learn that form submissions get faster turnaround than emails." |
| "We already have Workfront / Asana for this" | "Many creative teams start with those tools but hit limitations with financial services security requirements, complex approval chains, and the need for custom dashboards. monday.com offers enterprise-grade security with the flexibility to build exactly the workflow your team needs — without a 6-month implementation." |
| "Our offshore team uses different tools" | "monday.com's global accessibility and follow-the-sun handoff capabilities are a key differentiator. Instead of syncing between systems, every production center works in the same platform with structured handoff protocols. This is how you eliminate the overnight rework problem." |
| "This is just a project management tool — we need a creative-specific solution" | "monday.com is not just project management — it's a work operating system. With AI Agents, Vibe-built custom workflows, and deep automation, it becomes your creative operations platform. Let me show you the brand compliance and asset management capabilities that go far beyond task tracking." |
| "The bankers will resist any change to how they request work" | "The key insight is that bankers benefit immediately — they get real-time status visibility, faster turnaround from complete briefs, and no more 'where's my deck?' follow-ups. We position it as improved service to them, not a burden. The form takes 2 minutes vs. writing a detailed email." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for financial services creative team deployments]
- [Placeholder for 24/7 production operation workflow transformations]
- [Placeholder for brand compliance and template governance case studies]
- [Placeholder for creative SLA improvement metrics]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
