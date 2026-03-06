# Advertising & Marketing × Sales Playbook

## Overview

Sales teams in advertising and marketing agencies operate in one of the most relationship-driven, high-velocity environments in B2B services. A mid-size agency (50–500 employees) typically runs a sales org of 5–30 people spanning Business Development Representatives (BDRs), Account Executives (AEs), and New Business Directors, all supported by pitch coordinators, RFP specialists, and sales operations analysts. Revenue cycles are project-based and retainer-based, with deal sizes ranging from $50K campaign engagements to $10M+ AOR (Agency of Record) relationships. The sales pipeline is inherently lumpy — a single RFP win can represent 20% of annual revenue.

The regulatory environment is lighter than financial services but increasingly complex: data privacy (GDPR, CCPA) affects what agencies can promise in pitches, and procurement-driven RFP processes at Fortune 500 clients demand SOC 2 compliance documentation, D&I reporting, and sustainability commitments alongside creative credentials. Agencies must track not just pipeline but also conflict checks (can't pitch Pepsi if you hold Coca-Cola), team availability for pitch staffing, and win/loss forensics that inform positioning.

The fundamental challenge for agency sales teams is that every deal is a custom proposal. Unlike SaaS where you demo a product, agencies sell ideas, teams, and capabilities — which means the sales process is deeply cross-functional, requiring creative, strategy, media, and production teams to collaborate on pitches. This makes pipeline visibility, resource coordination, and institutional knowledge critical competitive advantages.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Replace or Radically Augment Headcount | High | Pitch coordination, RFP responses, and proposal assembly consume 30-40% of senior sales time — AI agents can draft, assemble, and quality-check proposals |
| 2 | Scale Impact Without Overhead | High | Agencies need to pursue more pitches without proportionally growing sales headcount; AI-powered pipeline management and pitch automation enable this |
| 3 | Consolidate Tech Stack with AI | Medium-High | Agency sales teams typically juggle Salesforce/HubSpot, Google Slides, Slack, email, and spreadsheets for pipeline — monday.com unifies workflow with CRM |

## Prioritized Use Cases

---

### Use Case 1: Unified New Business Pipeline & Pitch Tracker

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Agency new business teams track opportunities across email threads, spreadsheets, Salesforce (poorly configured), and the head of new business's memory. When a CMO reaches out about a potential AOR review, the information lives in someone's inbox. Conflict checks require manually cross-referencing the client list. Pipeline reviews happen in PowerPoint decks that are outdated the moment they're created. The CEO asks "what's our pipeline?" and gets three different numbers from three different people. Win rates are tracked retroactively (if at all), and there's no institutional memory of why deals were lost.

#### The Solution
monday.com CRM configured specifically for agency new business: a pipeline board with stages reflecting the agency pitch process (Lead Identified → Conflict Check → Chemistry Meeting → RFP Received → Pitch Team Assembled → Credentials Submitted → Tissue Session → Final Pitch → Decision Pending → Won/Lost). Custom columns for estimated annual revenue, contract type (AOR/Project/Retainer), industry vertical, conflict status, pitch team members, and competitive set. Dashboards showing pipeline by stage, expected revenue by quarter, win rate by vertical, and pitch team utilization. Automations for conflict check alerts, stage-based notifications, and stale deal flagging.

#### The Outcome
Single source of truth for pipeline — 100% visibility for leadership without asking. Conflict checks reduced from days to seconds. Win/loss data captured systematically, enabling pattern analysis. Pipeline accuracy improves 40-60% vs. spreadsheet tracking. Pitch team allocation visible, preventing over-commitment.

#### Discovery Questions
1. "How do you currently track what's in your new business pipeline — and how confident are you in that number right now?"
2. "When a potential conflict comes up, how long does it take to verify whether you can pursue an opportunity?"
3. "After a pitch loss, how do you capture and share what you learned with the broader team?"
4. "How do you decide which opportunities to pursue vs. pass on — is there a formal go/no-go process?"
5. "How many pitches is your team running simultaneously right now, and do you have visibility into who's staffed on what?"

#### Industry Context
Agency new business is unique because deals aren't just "closed" — they're "won" through a multi-stage pitch process that can take 3-6 months. The "chemistry meeting" is a critical early stage where the agency meets the client to assess mutual fit. "Tissue sessions" are interim creative reviews. AOR (Agency of Record) deals are the holy grail — multi-year retainers worth millions. Conflict management is legally and ethically critical: holding a competing account can disqualify an agency immediately. The "competitive set" (which other agencies are pitching) dramatically affects strategy.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an agency new business pipeline tracker. Create a board called 'New Business Pipeline' with these columns: Deal Name (text), Prospect Company (text), Industry Vertical (dropdown: CPG, Tech, Financial Services, Healthcare, Retail, Automotive, Entertainment, QSR, Travel, Luxury, Other), Estimated Annual Revenue (numbers, in dollars), Contract Type (dropdown: AOR, Project, Retainer, Hybrid), Pipeline Stage (status: Lead Identified, Conflict Check, Chemistry Meeting, RFP Received, Pitch Team Assembled, Credentials Submitted, Tissue Session, Final Pitch, Decision Pending, Won, Lost, Declined to Pitch), Conflict Status (status: Clear, Potential Conflict, Conflict Confirmed, Waiver Requested), Lead Source (dropdown: Inbound, Referral, Consultant/Search Firm, Existing Relationship, Event/Conference, Cold Outreach), Pitch Lead (people), Pitch Team (people), Expected Decision Date (date), Competitive Set (long text), Go/No-Go Decision (status: Pending, Go, No-Go), Win/Loss Reason (long text). Add automations: when Conflict Status changes to Potential Conflict, notify the Head of New Business; when Pipeline Stage changes to Won, send a celebration notification to the #wins channel; when Expected Decision Date is more than 7 days past and Pipeline Stage is Decision Pending, notify the Pitch Lead. Create a Kanban view grouped by Pipeline Stage, a Dashboard view showing pipeline value by stage (chart), win rate by quarter (chart), and deals by Industry Vertical (chart), and a Timeline view showing pitch timelines by Expected Decision Date."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** New Business Intelligence Agent
**Agent Purpose:** Automatically enrich pipeline entries, flag conflicts, and generate pitch preparation briefs.

**Triggers:**
- New item created in Pipeline board
- Prospect Company field updated
- Pipeline Stage changes to "RFP Received"
- Weekly scheduled digest (Monday 8 AM)
- Manual trigger by Pitch Lead

**Actions:**
- Auto-populate Industry Vertical and company details by researching the prospect
- Cross-reference Prospect Company against current client list and flag conflicts
- Generate a "Pitch Prep Brief" with prospect's recent news, marketing spend data, competitive landscape, and key stakeholders
- Create a win/loss analysis summary when deal moves to Won or Lost
- Send weekly pipeline digest to leadership with movement, risks, and recommended actions
- Alert when a deal has been in the same stage for more than the average duration

**Data Required:**
- Current client list (for conflict checks)
- Company research APIs (Clearbit, LinkedIn, press databases)
- Historical win/loss data from past deals
- Industry benchmarking data for revenue estimates

**Autonomy Level:** Human-in-the-Loop
The agent enriches data and generates recommendations autonomously but requires human approval for conflict determinations (too legally sensitive to automate fully) and go/no-go recommendations. All generated briefs are drafts that Pitch Leads review.

**Example Interaction:**
> A BDR logs a new lead: "Acme Consumer Products - potential AOR review." The New Business Intelligence Agent immediately springs into action, researching Acme's recent marketing activity, current agency roster, and estimated marketing spend ($45M annually across brand and performance). Within minutes, it populates the deal record with industry vertical (CPG), estimated annual revenue ($3.2M based on typical CPG AOR fee structures), and key contacts.
>
> The agent then runs a conflict check against the current client roster and flags a potential issue: "⚠️ Potential Conflict: You currently hold BrightClean Detergents (CPG/Household). Acme Consumer Products competes directly in the household cleaning category. Recommend legal review before proceeding." The Head of New Business receives an instant notification and can make the call.
>
> When the opportunity progresses to RFP Received, the agent generates a comprehensive Pitch Prep Brief: Acme's last three years of campaign work, their CMO's public statements about brand strategy, recent earnings call mentions of marketing investment, and a competitive set analysis showing which agencies are likely also pitching based on industry relationships.

---

### Use Case 2: RFP Response & Proposal Assembly Workflow

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
When an RFP lands, it triggers a fire drill. The new business director reads through a 40-page document, identifies requirements, and starts emailing department heads for inputs: case studies from creative, methodology decks from strategy, bios from the proposed team, rate cards from finance, compliance docs from legal, and D&I statistics from HR. Each person responds on their own timeline (or doesn't). The pitch coordinator lives in a spreadsheet tracking who owes what, sending increasingly desperate follow-up emails. Proposal assembly happens in the final 48 hours in a Google Slides deck where version control is a prayer. Senior leaders review at the last minute and request changes that cascade through 200 slides. The agency submits — exhausted — and then can't remember three months later what they actually proposed.

#### The Solution
monday.com Work Management as the RFP response command center. A templated project board auto-created when a deal reaches "RFP Received" stage, with pre-populated tasks for every standard RFP section (Agency Overview, Team Bios, Case Studies, Methodology, Pricing, Compliance, D&I, Sustainability). Each task assigned to the responsible department with deadline driven by the submission date. A content library board storing approved case studies, bios, boilerplate language, and compliance docs — searchable and version-controlled. Automations notify owners, escalate overdue items, and track completion percentage. Dashboards show real-time readiness across all active RFPs. Integration with Google Workspace/Office 365 for document collaboration.

#### The Outcome
RFP response time reduced by 35-50%. Pitch coordinator role shifts from "chasing people" to "quality assurance." Proposal quality improves through standardized components and proper review cycles. Institutional knowledge preserved — every proposal archived and searchable for future pitches. Parallel RFP management becomes feasible (agencies typically cap at 3-4 simultaneous pitches due to coordination overhead; this raises the ceiling to 6-8).

#### Discovery Questions
1. "Walk me through what happens in the first 24 hours after you receive an RFP — who does what?"
2. "How many hours per week does your pitch coordinator spend chasing people for content?"
3. "Do you have a centralized library of approved case studies, bios, and boilerplate — or does everyone recreate from scratch?"
4. "How many RFPs can you realistically run simultaneously before quality drops?"
5. "After you submit a proposal, can you easily find what you proposed six months later if the client comes back?"

#### Industry Context
Agency RFPs are uniquely complex because they require both operational content (team structure, pricing, process) and creative content (spec work, strategic thinking, campaign concepts). The "tissue session" is a mid-process client check-in where the agency presents early thinking — it's essentially a pitch within the pitch. "Spec work" (speculative creative done for the pitch) is controversial in the industry but increasingly expected by clients. Rate cards in agencies are complex: different roles (SVP Creative Director vs. Junior Designer) have different rates, and clients often negotiate blended rates. D&I and sustainability sections have gone from "nice to have" to "required" in Fortune 500 RFPs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an RFP response management system. Create a board called 'RFP Response Tracker' with columns: RFP Name (text), Client (text), Submission Deadline (date), Response Status (status: Intake, Requirements Analysis, Content Collection, Assembly, Internal Review, Final QA, Submitted), RFP Lead (people), Pitch Team (people), Overall Completion (progress tracking). Create a connected board called 'RFP Task Breakdown' with columns: Task Name (text), RFP Section (dropdown: Agency Overview, Team & Staffing, Case Studies, Methodology & Approach, Strategic Response, Spec Creative, Pricing & Rate Card, Compliance & Legal, D&I Report, Sustainability, Technology & Tools, References), Owner (people), Due Date (date), Task Status (status: Not Started, In Progress, In Review, Approved, Blocked), Priority (status: Critical Path, High, Medium, Low), Content Source (text), Notes (long text). Add automations: when a new item is created on RFP Response Tracker, auto-create a task breakdown from a template with all standard sections; when Task Status on any RFP Task is Blocked, notify the RFP Lead immediately; when Due Date is tomorrow and Task Status is Not Started, send urgent reminder to Owner; when all tasks in an RFP reach Approved, change Response Status to Final QA. Create a content library board called 'Pitch Content Library' with columns: Content Name (text), Content Type (dropdown: Case Study, Team Bio, Methodology, Boilerplate, Compliance Doc, Rate Card Template, D&I Report, Sustainability Report), Industry Vertical (dropdown), Last Updated (date), Owner (people), File (files), Version (numbers). Create a Dashboard showing completion percentage across all active RFPs, overdue tasks by owner, and a timeline of upcoming submission deadlines."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RFP Assembly Agent
**Agent Purpose:** Automatically parse RFP requirements, match them to existing content, and draft proposal sections.

**Triggers:**
- New RFP document uploaded to an item
- RFP Section task moved to "In Progress"
- Manual trigger: "Draft this section"
- 72 hours before submission deadline (final check)
- Content Library item updated (re-match against active RFPs)

**Actions:**
- Parse uploaded RFP document and auto-create task breakdown with section-by-section requirements
- Match RFP requirements against Pitch Content Library and suggest best-fit case studies, bios, and boilerplate
- Draft first-pass responses for standard sections (Agency Overview, Methodology, Compliance) using approved content
- Flag non-standard requirements that need custom responses and assign to appropriate SMEs
- Generate a "Compliance Checklist" ensuring every stated requirement has a mapped response
- 72 hours before deadline: audit all sections, flag gaps, and send status report to RFP Lead

**Data Required:**
- Pitch Content Library (all approved content)
- Historical proposals (for language and approach patterns)
- RFP document (PDF/Word parsing capability)
- Team availability and bio database
- Current rate cards and pricing models

**Autonomy Level:** Escalation-Based
The agent drafts and suggests autonomously but escalates for: pricing decisions (always human), case study selection for competitive pitches (strategic choice), and any section flagged as "Custom/Strategic" in the RFP requirements. Standard compliance and boilerplate sections can be auto-populated with human review at the end.

**Example Interaction:**
> A 52-page RFP arrives from GlobalBev Corp for a digital AOR review. The RFP Assembly Agent parses the document within minutes and creates 18 task items in the RFP Task Breakdown board, each mapped to a specific RFP requirement. It highlights three non-standard requirements: "Provide your agency's approach to AI-generated content governance," "Detail your carbon offset program for production shoots," and "Include a 90-day onboarding plan with named team members."
>
> For the 12 standard sections, the agent pulls matching content from the library: three relevant CPG case studies (ranked by recency and relevance), pre-approved methodology language, and the latest compliance documentation. It drafts first-pass responses, noting where content was sourced and confidence level. For the "Team & Staffing" section, it cross-references the proposed team's current workload and flags: "⚠️ Sarah Chen (proposed Strategy Lead) is staffed on 2 other active pitches with overlapping timelines. Consider alternative: James Park (available, similar vertical experience)."
>
> With 72 hours to go, it runs a final audit: "16 of 18 sections complete. Missing: AI Content Governance (assigned to Legal, overdue by 1 day) and 90-Day Onboarding Plan (assigned to Account Director, in progress). Pricing section flagged for SVP review — proposed blended rate is 12% above last successful CPG pitch."

---

### Use Case 3: Sales Forecasting & Revenue Planning for Agency Finance

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Agency revenue forecasting is notoriously unreliable. Unlike SaaS with recurring revenue, agencies deal with project-based work (unpredictable timing), retainer clients who may expand or contract scope quarterly, pitch pipeline that converts at wildly different rates by vertical, and "surprise" revenue from existing client expansions that nobody tracked. The CFO builds forecasts in Excel, the Head of New Business gives gut-feel pipeline probabilities, and existing account growth is tracked by individual AEs who update spreadsheets monthly (or don't). Q4 is always a scramble because half the pipeline slipped, two retainer clients cut budgets, but three organic expansions weren't in the forecast. The result: revenue surprises (both positive and negative) that make resource planning nearly impossible.

#### The Solution
monday.com dashboards connecting new business pipeline (with weighted probability), existing account health tracking (retainer value, expansion signals, risk flags), and project-based revenue recognition. A unified revenue board that auto-calculates weighted pipeline + confirmed retainer revenue + project backlog. Automations that prompt AEs to update account status monthly, flag at-risk retainers (declining scope, delayed renewals), and surface expansion opportunities. Historical conversion data by stage and vertical feeding more accurate probability weighting. Integration with accounting systems for actuals vs. forecast tracking.

#### The Outcome
Forecast accuracy improves from ±30% to ±10-15%. At-risk retainer revenue identified 60-90 days earlier, enabling save plays. Hidden expansion revenue surfaced and tracked. Resource planning (hiring, freelancer budgeting) aligned to realistic revenue projections. CFO and CEO get real-time revenue visibility without assembling data from five sources.

#### Discovery Questions
1. "How accurate was your revenue forecast last quarter — and where did the biggest surprises come from?"
2. "Do you have visibility into which existing accounts are at risk of reducing scope or churning?"
3. "How do you weight pipeline probability — is it consistent across the team or individual gut feel?"
4. "When an existing client wants to expand scope, how does that get captured in the forecast?"
5. "How far ahead can you confidently forecast — one quarter? Two?"

#### Industry Context
Agency revenue has three streams: retainer revenue (predictable monthly fees, usually 12-month contracts), project revenue (one-off engagements with defined scope and timeline), and new business pipeline (future potential). "Organic growth" from existing clients is often the largest revenue source but the least tracked. "Scope creep" — where agencies do more work than contracted — is endemic and represents both a margin risk and an expansion opportunity. "Utilization rate" (percentage of billable hours vs. available hours) is the key profitability metric. Agency finance teams track "revenue per head" as a core KPI, typically targeting $200K-$350K depending on agency type and seniority mix.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an agency revenue forecasting system. Create a board called 'Revenue Forecast' with columns: Revenue Source (dropdown: New Business Pipeline, Existing Retainer, Project Revenue, Organic Expansion), Client Name (text), Account Owner (people), Monthly Revenue Value (numbers, in dollars), Annual Contract Value (numbers, in dollars), Revenue Probability (numbers, percentage), Weighted Revenue (formula: Monthly Revenue Value × Revenue Probability / 100), Revenue Status (status: Confirmed, High Confidence, Medium Confidence, Low Confidence, At Risk, Lost), Contract Start Date (date), Contract End Date (date), Renewal Status (status: Auto-Renew, In Negotiation, At Risk, Churned, Not Applicable), Expansion Pipeline (numbers, in dollars), Notes (long text). Create a connected board called 'Account Health Tracker' with columns: Client Name (text), Account Owner (people), Retainer Value (numbers, monthly dollars), Client Satisfaction (status: Thriving, Stable, Needs Attention, At Risk, Critical), Last QBR Date (date), Next Renewal Date (date), Scope Change Trend (status: Expanding, Stable, Contracting), Risk Factors (long text), Expansion Opportunities (long text), NPS Score (numbers). Add automations: when Client Satisfaction changes to At Risk, notify Account Owner and Head of Sales immediately; when Next Renewal Date is 90 days away, create a renewal prep task; when Revenue Status changes to At Risk, update the Revenue Forecast weighted probability to 25%; on the 1st of every month, remind all Account Owners to update their account health status. Create a Dashboard with: total weighted pipeline by quarter (chart), confirmed vs. forecast revenue by month (chart), at-risk revenue requiring attention (number widget), revenue by source type (pie chart), and year-over-year comparison (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Revenue Intelligence Agent
**Agent Purpose:** Continuously monitor account health signals and pipeline movement to produce accurate, real-time revenue forecasts.

**Triggers:**
- Monthly forecast cycle (1st of month)
- Account Health status changes
- Pipeline deal stage changes
- Contract renewal dates approaching (90/60/30 days)
- Manual request for forecast snapshot

**Actions:**
- Analyze historical conversion rates by pipeline stage and vertical to auto-weight probabilities
- Monitor account health indicators and predict churn risk based on engagement patterns
- Generate monthly forecast report comparing current projections vs. prior month and vs. actuals
- Flag accounts with declining engagement (fewer updates, stale QBR dates, scope reduction signals)
- Identify expansion opportunities based on client growth patterns and comparable accounts
- Produce quarterly board-ready revenue presentation with variance analysis

**Data Required:**
- Pipeline board with stage history and timestamps
- Account health tracker with longitudinal data
- Historical actuals from accounting system integration
- Client engagement signals (email frequency, meeting cadence, project volume)
- Industry benchmarks for retainer renewal rates

**Autonomy Level:** Human-in-the-Loop
Forecast generation and risk flagging are autonomous. Probability adjustments are suggested but require AE confirmation. Churn risk alerts are sent automatically, but save play strategies are recommendations that the Account Owner decides on.

**Example Interaction:**
> On March 1st, the Revenue Intelligence Agent generates the monthly forecast. It analyzes 47 accounts and 12 active pipeline deals. Key findings: "Q2 forecast is $4.2M weighted (down $380K from last month). Primary drivers: MegaRetail retainer renewal at risk — no QBR in 4 months, last two scope requests declined, recommend immediate executive outreach. Offsetting upside: TechStart organic expansion likely — they've briefed 3 new projects in 6 weeks, pattern matches pre-expansion behavior of similar mid-market tech clients. Recommend proactive proposal for expanded retainer."
>
> The agent also flags a pipeline anomaly: "Your win rate on Financial Services pitches has dropped from 35% to 15% over the last 4 quarters. Current pipeline includes 2 FinServ deals weighted at 35%. Suggest reviewing competitive positioning in this vertical or adjusting probability weighting to reflect actual performance."

---

### Use Case 4: Client Prospecting & Lead Qualification Automation

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Agency BDRs spend 60-70% of their time on research and qualification rather than actual outreach. Before reaching out to a prospect, they need to understand the company's current agency roster, recent campaign work, marketing leadership changes, budget signals from earnings calls, and industry challenges. This research is manual — scrolling LinkedIn, reading AdAge, checking agency spy sites, and piecing together a picture. When they do reach out, the messaging is often generic because there wasn't time to personalize at scale. The Head of New Business wants 50 qualified outreach attempts per week; the BDR team delivers 15 because research eats their day.

#### The Solution
monday.com CRM with AI-powered prospecting workflows. A prospect research board where BDRs log target companies and AI agents auto-enrich with agency roster data, recent marketing activity, leadership changes, and industry context. Lead scoring based on signals like "recently changed CMO" (high intent), "in AOR review" (highest intent), "expanding into new markets" (growth signal). Automated outreach sequences with personalized messaging generated from research data. Pipeline handoff workflows from BDR qualification to AE relationship.

#### The Outcome
BDR research time reduced by 70% — from 45 minutes per prospect to under 15 minutes. Outreach volume triples without additional headcount. Personalization quality actually improves because AI-enriched data is more comprehensive than manual research. Lead-to-meeting conversion rate improves 25-40% due to better targeting and messaging.

#### Discovery Questions
1. "How long does it take your BDRs to research a prospect before reaching out?"
2. "What signals tell you a company is likely to be in or approaching an agency review?"
3. "How personalized are your outreach messages — and does personalization actually affect your response rates?"
4. "Do you track which prospecting channels and messaging approaches convert best?"
5. "What's your current lead-to-meeting conversion rate, and where do you think you're losing people?"

#### Industry Context
"Agency reviews" are the lifeblood of new business — when a brand puts its agency relationship up for competitive bid. Reviews are often triggered by CMO changes, declining business performance, or agency relationship fatigue (average agency tenure is 3-5 years). "Search consultants" (firms like AAR Partners, Pile & Company) often manage the review process. "Credentials presentations" (or "creds decks") are the agency's portfolio — curated by vertical and capability. The "inbound vs. outbound" mix varies: top agencies get 70%+ inbound from reputation; mid-market agencies rely heavily on outbound prospecting.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me an agency prospecting and lead qualification system. Create a board called 'Prospect Research Pipeline' with columns: Company Name (text), Industry Vertical (dropdown: CPG, Tech, Financial Services, Healthcare, Retail, Automotive, Entertainment, QSR, Travel, Luxury, Telecom, Other), Estimated Marketing Spend (numbers, in dollars), Current Agency Roster (long text), CMO/Marketing Lead (text), Lead Score (numbers, 1-100), Lead Status (status: New, Researching, Qualified, Outreach Scheduled, Contacted, Meeting Set, Disqualified), Intent Signals (dropdown multi-select: CMO Change, AOR Review Announced, New Product Launch, Market Expansion, M&A Activity, Declining Performance, Budget Increase, None Detected), BDR Owner (people), Research Notes (long text), Last Contact Date (date), Next Action Date (date), Outreach Channel (dropdown: Email, LinkedIn, Phone, Event, Referral, Search Consultant), Source (dropdown: AdAge, LinkedIn, Industry Event, Consultant Referral, Press Coverage, Inbound). Add automations: when Lead Score exceeds 75, change Lead Status to Qualified and notify the BDR Owner; when Next Action Date is today, send reminder to BDR Owner; when Lead Status changes to Meeting Set, create a connected item in New Business Pipeline board; when Intent Signals includes 'AOR Review Announced', set Lead Score to 90 and mark as urgent. Create a Dashboard showing prospects by vertical (pie chart), leads by status (funnel chart), BDR activity metrics (outreach attempts vs. meetings set), and lead score distribution."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Prospect Intelligence Agent
**Agent Purpose:** Automatically research, enrich, and score prospective clients to accelerate BDR outreach.

**Triggers:**
- New company added to Prospect Research Pipeline
- Weekly industry news scan (Monday 6 AM)
- Intent signal detected from monitoring sources
- Manual trigger: "Research this company"
- Monthly re-score of all active prospects

**Actions:**
- Research company and auto-populate marketing spend estimates, current agency relationships, and key contacts
- Monitor industry press for review announcements, CMO changes, and budget signals
- Generate personalized outreach messaging based on prospect's specific situation and pain points
- Score and re-score leads based on accumulating signals
- Create prospect briefing document before scheduled meetings
- Identify lookalike companies based on successful conversions (vertical, size, signal pattern)

**Data Required:**
- Industry press feeds (AdAge, Campaign, Marketing Week, PRWeek)
- LinkedIn company and people data
- Agency relationship databases
- Company financial data for spend estimation
- Historical conversion data for scoring model

**Autonomy Level:** Escalation-Based
Research, enrichment, and scoring run fully autonomously. Outreach message drafts are generated but require BDR review before sending. High-priority signals (active AOR review) escalate immediately to Head of New Business for strategic decision on pursuit.

**Example Interaction:**
> The Prospect Intelligence Agent's weekly scan picks up an AdAge article: "FreshFoods Inc. Initiates Creative Agency Review, Reportedly Dissatisfied with Current AOR." Within minutes, the agent creates a new prospect record with auto-populated data: FreshFoods Inc., estimated $28M annual marketing spend, current AOR is Creativity Partners (held for 6 years), new CMO hired 4 months ago from a DTC brand (signal: likely wants digital-first approach). Lead score: 95.
>
> The agent drafts a personalized outreach message referencing the agency's relevant QSR/Food case studies and positions the agency's digital transformation capabilities — directly aligned with what a DTC-background CMO would value. It also identifies the search consultant managing the review (Pile & Company) and notes the agency's existing relationship with a partner there. The BDR receives a complete briefing: "FreshFoods is high-priority. Here's the draft outreach for the CMO's LinkedIn, the consultant contact path, and three relevant case studies to lead with."

---

### Use Case 5: Sales & Creative Collaboration for Pitch Development

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
The biggest friction point in agency sales isn't the sales process — it's the handoff between sales and creative/strategy teams. When a pitch is greenlit, the new business team needs to brief the creative department, align on strategy, coordinate spec work timelines, manage tissue sessions with the client, and ensure the final pitch tells a cohesive story. This coordination happens across Slack channels, email threads, and in-person hallway conversations. Creative teams resent being "voluntold" for pitches that weren't communicated well. Strategy teams start work without clear client context. The pitch deck comes together in a chaotic 72-hour sprint where sales, creative, strategy, and production are all editing the same Google Slides deck simultaneously with conflicting feedback. The resulting pitch is often good despite the process, not because of it.

#### The Solution
monday.com Work Management as the pitch collaboration hub. A pitch project board with clear phases (Brief Development → Strategy → Creative Development → Tissue Prep → Refinement → Final Pitch Assembly → Rehearsal → Pitch Day). Workload management showing creative team availability across pitches and client work. Structured brief templates that capture client context, competitive landscape, and strategic direction. Integrated feedback loops with approval workflows for each pitch component. Timeline views showing critical path dependencies (strategy must be approved before creative begins, creative must be approved before pitch deck assembly).

#### The Outcome
Pitch preparation time reduced by 25-30%. Creative team satisfaction improves — clear briefs, realistic timelines, visible priorities. Pitch quality improves through structured process rather than heroic last-minute efforts. Ability to run more simultaneous pitches without burning out the creative team. Post-pitch retrospectives captured systematically, improving win rates over time.

#### Discovery Questions
1. "How would your creative team describe the pitch briefing process — would they say they get what they need to do great work?"
2. "What's the typical timeline from pitch greenlight to pitch day, and where do the bottlenecks usually hit?"
3. "How do you manage creative team workload when they're balancing pitches with existing client work?"
4. "When multiple teams contribute to a pitch deck, how do you ensure strategic coherence?"
5. "After a pitch, do you do formal retrospectives — and do the learnings actually change how you pitch next time?"

#### Industry Context
"Spec work" is original creative work produced specifically for a pitch — often the most expensive and time-consuming pitch element. Agencies debate whether to invest heavily in spec (impressive but costly) or focus on strategic thinking (efficient but less flashy). A "tissue session" is an interim client meeting where the agency shares early-stage thinking to get directional feedback before investing in finished creative. "Chemistry meetings" test cultural fit between agency and client teams. The "pitch team" typically includes a senior leader (gravitas), strategy lead (thinking), creative lead (ideas), account lead (relationship), and sometimes a media/digital specialist. "Pitch theater" refers to the production value of the presentation itself — agencies are known for elaborate setups, custom environments, and memorable stunts during final pitches.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a pitch collaboration workspace. Create a board called 'Pitch Projects' with columns: Pitch Name (text), Client (text), Pitch Date (date), Pitch Phase (status: Brief Development, Strategy, Creative Development, Tissue Prep, Refinement, Final Assembly, Rehearsal, Pitch Day, Post-Mortem), Pitch Lead (people), Strategy Lead (people), Creative Lead (people), Account Lead (people), Budget (numbers, in dollars), Priority (status: Tier 1 Must-Win, Tier 2 Strong Pursuit, Tier 3 Opportunistic), Spec Work Scope (dropdown: Full Campaign, Key Visual + Concept, Strategic Only, No Spec), Team Capacity Check (status: Green, Yellow, Red). Create a connected board called 'Pitch Tasks' with columns: Task (text), Phase (mirror from Pitch Projects), Owner (people), Due Date (date), Status (status: Not Started, In Progress, Internal Review, Client Feedback, Approved, Blocked), Dependencies (dependency), Deliverable Type (dropdown: Strategic Brief, Creative Brief, Concept Boards, Storyboards, Pitch Deck Section, Budget/Pricing, Competitive Analysis, Case Studies, Rehearsal Notes). Add automations: when all tasks in a Phase reach Approved, advance the Pitch Phase to the next stage; when a task is Blocked, immediately notify the Pitch Lead; 3 days before Pitch Date, send final checklist reminder to entire pitch team; when Pitch Phase changes to Post-Mortem, create a retrospective survey item. Create a workload view showing team members across all active pitches, and a Timeline view showing pitch milestones and dependencies."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pitch Orchestrator Agent
**Agent Purpose:** Manage pitch timelines, coordinate cross-functional teams, and ensure nothing falls through the cracks during high-stakes pitches.

**Triggers:**
- Pitch Phase changes (each transition triggers next-phase setup)
- Task blocked or overdue
- Tissue session scheduled (prep required)
- 48 hours before any major milestone
- Daily pitch standup digest (8 AM)

**Actions:**
- Auto-generate phase-specific task lists when pitch advances (e.g., entering Creative Development creates tasks for concept development, mood boards, storyboards, and internal review)
- Send daily pitch digest to team: what's due today, what's blocked, what's on track
- Flag resource conflicts when team members are over-allocated across pitches and client work
- Generate tissue session prep document summarizing work completed and key discussion points
- Create pitch day checklist and run sheet (who presents what, tech setup, backup plans)
- After pitch: generate retrospective summary and distribute survey to pitch team

**Data Required:**
- Pitch Tasks board with all deliverables and timelines
- Team workload data across all boards (pitches + client work)
- Historical pitch data for timeline benchmarking
- Client meeting notes and feedback from tissue sessions

**Autonomy Level:** Fully Autonomous (for coordination); Human-in-the-Loop (for content decisions)
Task creation, reminders, conflict flagging, and status reporting run automatically. Content-related decisions (creative direction, strategy pivots, spec work scope) always require human judgment. The agent orchestrates the process; humans drive the substance.

**Example Interaction:**
> It's Tuesday morning and the agency has two active pitches: TechGiant (Tier 1, pitch Friday) and EcoBeauty (Tier 2, pitch in 3 weeks). The Pitch Orchestrator sends the daily digest: "🔴 TechGiant Pitch (3 days out): 2 of 12 tasks overdue — Storyboard Revisions (Creative: Mark, due yesterday) and Pricing Final (Finance: Lisa, due yesterday). Pitch deck is 70% assembled. Rehearsal scheduled Thursday 2 PM — confirm AV setup. ⚠️ Resource conflict: Mark is also assigned to EcoBeauty concept boards due Thursday — recommend reassigning EcoBeauty to Alex (available, briefed on the brand)."
>
> The Pitch Lead reviews and approves the reassignment. The agent updates both boards, notifies Alex with context, and adjusts the EcoBeauty timeline. It then generates the TechGiant tissue session recap for the team: "Client feedback from last week's tissue: loved the strategic platform, want to see it pushed further in digital executions. CMO specifically asked for more data-driven personalization examples. Recommend adding the DataDriven Retail case study to the deck."

---

### Use Case 6: Win/Loss Analysis & Competitive Intelligence System

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most agencies track wins loudly and losses quietly. When a pitch is lost, there's a brief postmortem email ("they went with a bigger agency" or "it came down to chemistry"), and then everyone moves on. Nobody systematically tracks why deals are won or lost, which competitors keep winning in which verticals, what pricing patterns lead to success, or how the agency's pitch process correlates with outcomes. The Head of New Business has anecdotal knowledge ("we always lose to OmniAgency in automotive") but no data to support strategic decisions about which pitches to pursue, how to differentiate, or where to invest.

#### The Solution
monday.com board dedicated to win/loss tracking. Every completed deal (won, lost, or declined) gets a detailed post-mortem entry: outcome, decision factors (ranked), competitor analysis, pricing comparison, team feedback, and client feedback (when available). Dashboards showing win rate by vertical, by deal size, by competitor, and by pitch team composition. Quarterly competitive intelligence reports auto-generated from accumulated data. Pattern recognition surfacing actionable insights: "Win rate doubles when we include spec creative" or "We lose 80% of deals where the incumbent is invited to re-pitch."

#### The Outcome
Data-driven pursuit decisions — stop wasting resources on low-probability pitches. Competitive positioning sharpened based on actual win/loss patterns. Pitch process improvements driven by evidence rather than opinion. Over 12 months, win rate typically improves 5-10 percentage points as the agency learns from its own data.

#### Discovery Questions
1. "When you lose a pitch, how do you capture what happened — and does that information ever influence future decisions?"
2. "Do you know your win rate by industry vertical — and has that changed over time?"
3. "Which competitors do you encounter most often, and do you know your head-to-head record against them?"
4. "Have you ever declined to pitch something you should have, or pursued something you shouldn't have? How do you make that call?"
5. "If I asked your creative team and your strategy team why you lost the last three pitches, would they give the same reasons?"

#### Industry Context
In advertising, "the competitive set" isn't just who you're pitching against — it shapes your entire strategy. Knowing that the client is also talking to a digital-first agency vs. a traditional creative shop changes how you position. "Chemistry" is often cited as a win/loss factor but is hard to systematize — it typically means the personal connection between senior leaders. "Search consultants" sometimes provide post-pitch feedback, which is gold for learning. The industry rule of thumb is a 25-33% win rate for invited pitches — agencies that consistently beat this are doing something systematically right.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a win/loss analysis tracker. Create a board called 'Win/Loss Analysis' with columns: Pitch Name (text), Client (text), Industry Vertical (dropdown: CPG, Tech, Financial Services, Healthcare, Retail, Automotive, Entertainment, QSR, Travel, Luxury, Telecom, Other), Deal Value (numbers, annual dollars), Outcome (status: Won, Lost, Declined to Pitch, Client Cancelled Review), Primary Win/Loss Reason (dropdown: Creative Strength, Strategic Thinking, Chemistry/Fit, Pricing, Digital Capabilities, Incumbent Advantage, Specialist Expertise, Team Composition, Agency Reputation, D&I/Sustainability, Other), Secondary Factors (long text), Winning Agency (text), Competitive Set (long text), Included Spec Work (status: Yes Full, Yes Limited, No), Pitch Team Lead (people), Client Decision Maker (text), Search Consultant (text), Feedback Source (dropdown: Client Direct, Search Consultant, Industry Intel, Internal Assessment Only), Decision Date (date), Pitch Date (date), Pricing vs Market (dropdown: Above Market, At Market, Below Market, Unknown), Lessons Learned (long text), Action Items (long text). Add automations: when Outcome is set, notify Head of New Business to schedule debrief; when a new Loss is recorded, auto-create follow-up tasks for competitive analysis update and team feedback collection. Create a Dashboard with: overall win rate by quarter (chart), win rate by Industry Vertical (chart), head-to-head record vs top 5 competitors (table widget), win/loss reasons distribution (pie chart), average deal value won vs lost (chart), and spec work correlation with wins (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Competitive Intelligence Agent
**Agent Purpose:** Analyze win/loss patterns, monitor competitive activity, and generate actionable intelligence for pitch strategy.

**Triggers:**
- New win/loss entry completed
- Quarterly analysis cycle (1st of quarter)
- Competitive mention detected in industry press
- Pre-pitch request: "What do we know about [competitor]?"
- Go/no-go decision point on pipeline deal

**Actions:**
- Analyze win/loss data and generate pattern reports (what's working, what's not, by vertical/size/competitor)
- Maintain competitor profiles with recent wins, positioning, known strengths/weaknesses
- Generate pre-pitch competitive briefing when a competitive set is identified
- Recommend go/no-go based on historical probability given the specific vertical, deal size, and competitive set
- Produce quarterly "State of New Business" report with trends, insights, and strategic recommendations
- Alert when a competitor wins in a vertical where the agency has been investing

**Data Required:**
- Win/Loss Analysis board (complete historical data)
- Industry press monitoring feeds
- Competitor agency websites and case study pages
- Pipeline board for context on active pursuits
- Industry benchmarks for win rates

**Autonomy Level:** Fully Autonomous
All analysis, monitoring, and report generation runs without human intervention. Recommendations are advisory — humans make the strategic decisions about which pitches to pursue and how to position.

**Example Interaction:**
> The Head of New Business is evaluating whether to pursue a $2M Healthcare AOR opportunity. She triggers the agent: "What are our odds on this one?" The Competitive Intelligence Agent responds: "Based on your last 8 Healthcare pitches: win rate is 25% (2/8). Key pattern: both wins were mid-market clients ($1-3M) where you led with digital transformation strategy. Both losses to agencies with dedicated healthcare practices. The competitive set includes MedComms Agency (they've won 4 of the last 6 healthcare reviews under $5M — your toughest competitor in this vertical) and GeneralAgency (weaker healthcare credentials, likely included for procurement diversity). Recommendation: Pursue. Your win probability is approximately 30% given the mid-market size and digital focus. Key differentiator should be your integrated tech + creative capability — something MedComms lacks. Suggest staffing Dr. Sarah Kim (ex-pharma strategist) as pitch lead to counter the specialist positioning."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| AOR (Agency of Record) | Primary agency relationship — typically a multi-year retainer covering a broad scope of services |
| Pitch | The formal presentation and competition process where agencies vie for a client's business |
| RFP (Request for Proposal) | Formal document from a prospective client outlining requirements and evaluation criteria for agency selection |
| RFI (Request for Information) | Preliminary inquiry — less formal than RFP, used to shortlist agencies before the formal pitch |
| Tissue Session | Mid-pitch meeting where the agency presents work-in-progress to the client for directional feedback |
| Chemistry Meeting | Early-stage meeting to assess cultural and interpersonal fit between agency and client teams |
| Spec Work | Speculative creative work produced for a pitch — not paid, done to demonstrate capability |
| Search Consultant | Third-party firms (e.g., AAR Partners, Pile & Company) hired by clients to manage agency reviews |
| Creds Deck | Credentials presentation — the agency's portfolio and capabilities overview |
| Competitive Set | The group of agencies pitching for the same piece of business |
| Blended Rate | Weighted average hourly rate across the proposed team (mixes senior and junior rates) |
| Retainer | Ongoing monthly fee for a defined scope of work (vs. project-based billing) |
| Scope Creep | Work performed beyond the contracted scope — a major margin risk for agencies |
| Organic Growth | Revenue expansion from existing clients (vs. new business wins) |
| Billings | Total media and production spend managed by the agency (different from agency revenue/fees) |
| SOW (Statement of Work) | Detailed document defining deliverables, timelines, and fees for a specific engagement |
| QBR (Quarterly Business Review) | Structured review meeting between agency and client to assess performance and plan ahead |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Growth Officer / Head of New Business | Owns pipeline, pitch strategy, and win rate | Decision-maker for go/no-go and pitch investment |
| New Business Director | Day-to-day pipeline management, prospect outreach, pitch coordination | Decision-maker for pursuit tactics |
| Business Development Representative (BDR) | Outbound prospecting, lead qualification, initial outreach | Influencer — feeds the top of funnel |
| Pitch Coordinator / New Business Manager | Logistics, content assembly, timeline management for active pitches | Influencer — operational backbone |
| CEO / Managing Director | Pitch presenter (gravitas), final sign-off on pricing and resource allocation | Decision-maker for major pursuits |
| CFO / Finance Director | Revenue forecasting, pricing approval, resource budgeting | Decision-maker for financial commitments |
| Chief Creative Officer | Creative pitch leadership, spec work approval, talent allocation | Decision-maker for creative investment |
| Chief Strategy Officer | Strategic direction, client insight, pitch narrative | Decision-maker for positioning and approach |
| Account Director / AE | Existing client relationships, organic growth, account health | Influencer — owns retention revenue |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Creative & Design | Creative teams produce pitch materials, spec work; sales coordinates their involvement | Work Management for creative workflows, resource planning, asset management |
| Marketing (Agency's own) | Agency marketing generates inbound leads, case studies, thought leadership | Marketing workflows for the agency's own brand campaigns |
| Operations | Resource allocation, utilization tracking, staffing across pitches and client work | Capacity planning, resource management dashboards |
| Finance | Pricing, rate cards, revenue recognition, profitability analysis | Financial reporting, automated invoicing, margin tracking |
| HR | Recruiting (agencies have high turnover), team bios, D&I reporting for RFPs | Talent pipeline, onboarding, compliance reporting |
| IT | Tech stack for pitches (prototyping, demo environments), martech capabilities | IT project management, vendor management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce | Enterprise CRM — agencies often have poorly configured instances | monday CRM is simpler, faster to configure for agency sales cycles; agencies don't need enterprise CRM complexity |
| HubSpot | Marketing/sales automation — popular with smaller agencies | monday.com offers broader work management + CRM in one platform; agencies need project management alongside pipeline |
| Pipedrive | Simple pipeline management — used by agencies wanting lightweight CRM | monday CRM matches simplicity but adds cross-functional collaboration that Pipedrive lacks |
| Google Sheets / Excel | The incumbent "system" for most agency pipeline tracking | Any structured tool wins here — monday.com adds automation, visibility, and collaboration |
| Workamajig / Advantage | Agency-specific project management + accounting | Niche and outdated UX; monday.com is more modern, flexible, and integrable |
| Asana / Wrike | Project management for pitch coordination | monday.com combines PM + CRM in one platform; agencies can track pipeline and pitch projects together |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Salesforce for pipeline" | "How well does Salesforce handle the pitch coordination side — task management, creative team workflows, resource allocation? Most agencies we work with find CRM is just one piece; the real challenge is connecting pipeline to the cross-functional pitch process. monday.com does both." |
| "Our pipeline is too relationship-based for a CRM" | "That's exactly why you need a system — relationship-based means institutional knowledge lives in people's heads. When your Head of New Business leaves, so does your pipeline intelligence. monday.com captures the context alongside the deal data." |
| "We're too small / we don't have enough deals to justify a system" | "If you're running even 5-10 pitches a year, each one represents significant revenue. The question isn't volume — it's win rate. Even a 5% improvement in win rate on $500K average deal size pays for the platform many times over." |
| "Our creative team won't use another tool" | "They don't have to live in it. The Vibe prompts and automations mean the system comes to them — notifications in Slack, tasks auto-created, briefs pre-populated. They interact with it naturally through the tools they already use." |
| "We've tried project management tools for pitches before and adoption died" | "Adoption fails when the tool adds work without removing it. monday.com replaces email chains, spreadsheets, and status meetings. When the pitch coordinator stops sending 'where is your content?' emails because the board shows it automatically, adoption follows." |

## Proof Points
*(To be populated with customer references)*
- [Agency case studies with new business process improvements]
- [Win rate improvement metrics from structured pitch management]
- [Revenue forecasting accuracy improvements]
- [BDR productivity gains from AI-assisted prospecting]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
