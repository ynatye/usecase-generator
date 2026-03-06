# Advertising & Marketing × Customer Success Playbook

## Overview

Customer Success within advertising and marketing companies serves two critical functions: managing client retention and expansion for the agency's own business, while also helping clients maximize the value of their marketing investments. In full-service agencies (Ogilvy, BBDO, Havas), CS teams bridge the gap between campaign delivery and business outcomes. In specialized agencies (media, creative, digital), CS focuses on demonstrating ROI and upselling additional services.

The operational reality of agency CS is relationship-intensive and data-fragmented. A typical CS team at a mid-size agency (150-400 employees) manages 40-80 active client relationships simultaneously, with contract values ranging from $50K annual retainers to $10M+ integrated programs. The average Customer Success Manager (CSM) owns 15-25 accounts, conducts monthly health checks, quarterly business reviews (QBRs), and annual strategic planning sessions. Success metrics blend traditional SaaS indicators (NPS, churn, expansion rate) with agency-specific measures (campaign performance, creative approval cycles, media efficiency).

The challenge is data silos: campaign performance lives in media platforms (Google, Meta, programmatic DSPs), creative metrics are tracked in project management tools, client satisfaction exists in survey tools, and renewal conversations happen in email. When a client asks "what's our blended ROI across all channels this year?" the answer requires manual compilation across 5-8 systems. Contract negotiations rely on spreadsheet analyses instead of real-time performance dashboards.

Regulatory considerations include data privacy (GDPR, CCPA affecting campaign targeting), industry-specific compliance (pharmaceutical advertising, financial services regulations), and increasing scrutiny on measurement accuracy post-iOS 14.5 and cookie deprecation.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | CS teams must manage exponentially growing client data complexity (multi-channel attribution, privacy-safe measurement, real-time optimization) without proportional headcount growth. |
| 2 | Replace or Radically Augment Headcount | High | Junior CS roles (data compilation, report building, health score calculation) are 60% manual tasks that AI can automate. |
| 3 | Consolidate Tech Stack with AI | Medium-High | CS teams typically use 8-12 separate platforms (CRM, project management, media platforms, survey tools, presentation software, Excel). |

## Prioritized Use Cases

---

### Use Case 1: Client Health Score & Churn Prevention Engine

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Customer Success Managers manually compile client health scores monthly from disparate data sources: campaign performance metrics, project delays, budget utilization, executive feedback, payment history, and meeting cadence. The "health score" is often a subjective gut check rather than a data-driven metric. By the time warning signs are visible (missed meetings, declining performance, budget cuts), it's too late for proactive intervention. CSMs spend 15-20 hours per month just calculating health scores across their portfolio instead of acting on insights. Churn blindsides leadership because there's no systematic early warning system.

#### The Solution
monday.com as an automated client health scoring engine pulling data from campaign performance APIs, project management boards, meeting calendars, and financial systems. Machine learning models identify patterns in historical churn data to weight risk factors. Real-time dashboards surface at-risk accounts with specific intervention recommendations. Automated workflows trigger escalation procedures when health scores drop below thresholds.

#### The Outcome
Reduce client churn by 25% through early intervention. Decrease manual health score compilation from 20 hours to 2 hours per CSM per month. Increase renewal rates by 15% through proactive account management. Provide leadership with real-time portfolio risk visibility.

#### Discovery Questions
- How do you currently calculate client health scores, and how often do you update them?
- What percentage of client churn could you have predicted 60-90 days in advance with better data?
- How much time does your CS team spend compiling client performance data versus acting on it?
- When was the last time a client cancellation surprised you — and what early warning signs did you miss in hindsight?
- Can you show me your current client health dashboard, or is it more of a spreadsheet exercise?

#### Industry Context
"Client health" in agencies encompasses campaign performance (ROAS, CPM, conversion rates), relationship health (meeting frequency, executive engagement, NPS scores), and business health (budget utilization, payment terms, contract compliance). "Churn" is measured by both client count and revenue retention. "Land and expand" strategies focus on growing existing client spend through additional services or channels. The "QBR" (Quarterly Business Review) is the formal check-in where health is assessed. "At-risk" indicators include budget cuts, executive turnover at the client side, performance declining below benchmarks, and reduced meeting frequency.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a client health scoring and churn prevention system for an advertising agency's Customer Success team. Board: Client Health Dashboard. Columns: Client Name (text), Account Owner (people), Contract Value (numbers, currency USD), Contract Renewal Date (date), Overall Health Score (numbers, 0-100), Churn Risk Level (status: Healthy, Watch, At-Risk, Critical), Last QBR Date (date), Next QBR Due (date), Campaign Performance Score (numbers, 0-100 based on blended ROAS/CPA vs targets), Relationship Score (numbers, 0-100 based on meeting frequency, NPS, executive engagement), Project Health Score (numbers, 0-100 based on on-time delivery, approval cycles, scope changes), Financial Health Score (numbers, 0-100 based on payment history, budget utilization, invoice disputes), Key Risk Factors (dropdown: Performance Decline, Executive Turnover, Budget Pressure, Competitor Activity, Internal Issues), Intervention Status (status: No Action, Outreach Scheduled, Meeting Booked, Recovery Plan Active, Escalated), Last Touch Date (date), Days Since Contact (formula), NPS Score (numbers, 0-10), Campaign Count Active (numbers), Revenue YTD (numbers, currency USD), Revenue Growth vs Prior Year (percentage), Renewal Probability (numbers, 0-100%). Automations: when Health Score drops below 70, change Churn Risk to At-Risk and notify Account Owner; when Days Since Contact >14 and Churn Risk is At-Risk or Critical, send urgent reminder; when Contract Renewal Date is <90 days and Health Score <60, create high-priority renewal strategy task. Dashboard: portfolio health distribution (pie chart), at-risk revenue amount (number widget), churn risk trend over 6 months (line chart), renewal pipeline by quarter (bar chart), average health score by CSM (table), intervention success rate (gauge)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ChurnGuard
**Agent Purpose:** Continuously monitor client health across multiple data sources, predict churn risk using pattern recognition, and trigger proactive intervention workflows.

**Triggers:**
- Daily health score recalculation (every morning 8 AM)
- Health score drop >10 points week-over-week
- Campaign performance decline >15% below target for 7+ days
- Meeting cancelled or postponed by client
- NPS score received below 7
- Contract renewal date approaching (180, 90, 60, 30 days out)
- Payment delay >10 days past terms

**Actions:**
- Pull performance data from ad platforms (Google Ads, Meta, DV360) and calculate weighted performance scores
- Analyze meeting calendar patterns and flag decreased engagement frequency
- Cross-reference churn patterns from historical data to identify high-risk combinations
- Generate specific intervention recommendations (performance deep-dive meeting, executive dinner, service audit, contract restructure)
- Create automated renewal preparation timelines with milestone check-ins
- Draft client-specific talking points for CSM outreach based on account history and risk factors

**Data Required:**
- Client health board
- Campaign performance APIs (Google, Meta, programmatic platforms)
- Calendar integration for meeting frequency analysis
- Historical churn data for pattern recognition
- Contract and financial data for renewal forecasting

**Autonomy Level:** Human-in-the-Loop
ChurnGuard calculates scores and identifies risks autonomously. All client-facing communications and intervention strategies require human review. Escalation to leadership is automatic for critical-risk accounts.

**Example Interaction:**
> ChurnGuard runs its Monday morning analysis and flags client "FastFashion Co" with a health score drop from 78 to 62. Key factors: campaign ROAS declined from 4.2x to 3.1x over 14 days (performance score: 55), last strategic meeting was 18 days ago (relationship score: 65), and two creative revisions were requested last week suggesting approval friction (project health: 72). ChurnGuard recommends: "Schedule performance optimization meeting within 48 hours. Prepare data showing competitive benchmarks (3.3x ROAS is above industry average for fashion). Consider audit of targeting parameters — iOS 14.5 impact may require attribution model adjustment. High priority: client CMO Jessica Chen has meeting with CEO Thursday (gleaned from past email patterns) — likely discussing agency performance." CSM Maria reviews, agrees with the assessment, and books the meeting that afternoon.

---

### Use Case 2: Multi-Channel Campaign Performance Aggregation

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Campaign performance data is scattered across 8-15 different platforms: Google Ads, Meta Ads Manager, LinkedIn Campaign Manager, TikTok Ads, programmatic DSPs, email platforms, CRM systems, and website analytics. Each has different naming conventions, attribution windows, and reporting formats. When clients ask "what's our blended performance across all channels?" CSMs spend hours exporting data, normalizing formats, and building custom Excel models. Reports are always 1-2 weeks behind due to manual compilation time. Different platforms credit the same conversion to different touchpoints, making reconciliation a nightmare.

#### The Solution
monday.com as the central performance aggregation hub with API integrations to all major platforms. Automated daily data pulls normalize naming conventions and attribution models. Pre-built dashboards show blended performance, channel contribution, and trend analysis. Automated anomaly detection flags performance changes requiring investigation.

#### The Outcome
Reduce campaign reporting compilation from 8 hours to 15 minutes. Provide clients with real-time performance dashboards. Increase data accuracy through automated reconciliation. Enable daily optimization decisions instead of weekly ones.

#### Discovery Questions
- How many different platforms do you need to log into to get a complete picture of a client's campaign performance?
- When a client asks for their "overall ROAS," how long does it take you to give them an accurate answer?
- How do you handle attribution conflicts when Google and Facebook both claim credit for the same conversion?
- What percentage of your CS team's time is spent compiling data versus analyzing it?
- How often do clients receive performance updates — daily, weekly, monthly, or only when they ask?

#### Industry Context
"Blended performance" combines metrics across all marketing channels into unified KPIs (blended ROAS, total cost per acquisition, cross-channel attribution). "Walled garden" platforms (Google, Meta, Amazon) use proprietary attribution models that don't align with third-party analytics. "View-through conversions" and "click-through conversions" have different attribution windows by platform. "MMM" (Marketing Mix Modeling) and "MTA" (Multi-Touch Attribution) are methodologies for crediting conversions across touchpoints. "Incrementality testing" measures true causation versus correlation. Post-iOS 14.5 and cookie deprecation have made attribution significantly more complex.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a multi-channel campaign performance aggregation system for an agency Customer Success team. Board: Campaign Performance Hub. Columns: Client Name (text), Campaign Name (text), Campaign Start (date), Campaign End (date), Total Budget (numbers, currency USD), Spend to Date (numbers, currency USD), Budget Utilization (formula: percentage), Google Ads Spend (numbers), Meta Spend (numbers), LinkedIn Spend (numbers), Programmatic Spend (numbers), Email Spend (numbers), Total Impressions (numbers), Total Clicks (numbers), Total Conversions (numbers), Blended CPA (formula: Total Spend / Conversions), Blended ROAS (formula: Revenue / Spend), Google ROAS (numbers), Meta ROAS (numbers), LinkedIn ROAS (numbers), Email ROAS (numbers), Revenue Attributed (numbers, currency USD), Top Performing Channel (formula based on ROAS), Performance vs Goal (status: Exceeding, On Track, Below Target, Significantly Below), Optimization Notes (long text), Data Last Updated (date), CSM Owner (people). Connected Board: Daily Performance (sub-items): Date (date), Platform (dropdown: Google, Meta, LinkedIn, TikTok, Programmatic, Email), Daily Spend (numbers), Daily Impressions (numbers), Daily Clicks (numbers), Daily Conversions (numbers), Daily CPA (formula), Daily ROAS (formula). Automations: when Blended CPA increases >20% day-over-day, notify CSM; when any platform ROAS drops below client target for 3 consecutive days, create optimization task; daily 9 AM data refresh from all connected platforms. Dashboard: spend by channel (pie chart), ROAS trend by channel (multi-line chart), budget pacing across all clients (bar chart), performance alerts summary (table), top 10 campaigns by ROAS (ranked table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DataFusion
**Agent Purpose:** Aggregate campaign performance from multiple advertising platforms, reconcile attribution discrepancies, and surface optimization opportunities through unified analytics.

**Triggers:**
- Daily data refresh schedule (9 AM, 1 PM, 5 PM)
- Campaign performance anomaly detected (>20% CPA increase, >15% ROAS decrease)
- Client requests performance update
- Budget pacing alert (>10% behind or ahead of schedule)
- Monthly performance report generation
- QBR preparation (auto-compile quarterly trends)

**Actions:**
- Pull daily performance data from all connected platforms via APIs (Google, Meta, LinkedIn, programmatic, email)
- Reconcile attribution discrepancies using weighted allocation models based on platform strength
- Calculate blended metrics (total ROAS, CPA, LTV) across all channels
- Identify optimization opportunities (budget reallocation recommendations, underperforming creative/audience combinations)
- Generate automated client performance summaries with key insights and recommended actions
- Flag campaigns requiring urgent attention due to performance degradation

**Data Required:**
- Campaign performance board
- Platform API integrations (Google Ads, Meta Ads, LinkedIn, etc.)
- Client goal definitions and performance benchmarks
- Historical performance data for trend analysis
- Budget and pacing targets per campaign

**Autonomy Level:** Fully Autonomous (data processing) + Human-in-the-Loop (recommendations)
DataFusion processes data and calculates metrics autonomously. Optimization recommendations and budget reallocation suggestions require CSM review before client communication.

**Example Interaction:**
> DataFusion's 9 AM analysis reveals that client "HomeDecor Plus" has a 22% CPA increase across their multi-channel campaign. Investigation shows: Google Ads CPA stable at $45, Meta CPA increased from $38 to $67 (primary driver), LinkedIn and email performing normally. Root cause analysis suggests Meta's recent iOS update affected attribution. DataFusion recommends: "Shift 20% of Meta budget to Google (stronger first-party data signal), increase email retargeting budget by $500/day to capture Meta traffic at lower CPA, and implement Meta Conversions API for better attribution tracking. Projected impact: restore blended CPA to $48 (vs current $55)." CSM reviews, approves the Google/email reallocation, and schedules a client call to discuss the Meta technical implementation.

---

### Use Case 3: Automated QBR Preparation & Client Insights

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Quarterly Business Reviews (QBRs) are the cornerstone of client relationships but require 12-15 hours of preparation per client. CSMs manually compile performance data, create custom PowerPoint presentations, research industry benchmarks, analyze competitive activity, and develop strategic recommendations. With 15-25 clients per CSM, that's 180-375 hours per quarter just in QBR prep — nearly half their time. QBRs are often delayed because of preparation overhead, which creates client dissatisfaction. The presentations are backward-looking data dumps rather than strategic insights.

#### The Solution
monday.com as an automated QBR preparation engine that continuously compiles client data, generates insights, and creates presentation-ready dashboards. AI-powered analysis identifies trends, benchmarks performance against industry standards, and suggests strategic recommendations. Template-driven but customizable reporting ensures consistency while allowing personalization.

#### The Outcome
Reduce QBR preparation time from 12 hours to 2 hours per client. Deliver QBRs on schedule 100% of the time. Increase QBR quality through data-driven insights and strategic recommendations. Enable CSMs to manage 35-40 clients instead of 15-25.

#### Discovery Questions
- How many hours does it currently take your team to prepare a comprehensive QBR presentation?
- What percentage of your QBRs happen on schedule versus being delayed due to preparation challenges?
- How do you benchmark your clients' performance against industry standards or competitors?
- What's the typical client reaction to your QBRs — do they see them as valuable strategic sessions or data reports?
- If you could eliminate most QBR prep work, how would your CSMs spend that time instead?

#### Industry Context
QBRs are formal quarterly meetings where agencies present campaign performance, strategic insights, market analysis, competitive intelligence, and recommendations for the next quarter. They're critical for renewal conversations and expansion opportunities. "Performance benchmarking" compares client results to industry averages by vertical, company size, and geographic market. "Competitive analysis" tracks competitor advertising strategies, creative approaches, and share of voice. "Strategic recommendations" suggest new channels, audience segments, creative approaches, or budget allocations based on performance data. QBRs often determine whether contracts are renewed, budgets are increased, or additional services are purchased.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an automated QBR preparation system for agency Customer Success teams. Board: QBR Master Dashboard (one item per client). Columns: Client Name (text), Industry Vertical (dropdown: E-commerce, B2B SaaS, Financial Services, Healthcare, Retail, CPG, Travel), Next QBR Date (date), QBR Status (status: Not Started, Data Compiled, Analysis Complete, Presentation Ready, Client Reviewed, QBR Complete), CSM Owner (people), Quarter Period (text: Q1 2024), Total Ad Spend This Quarter (numbers, currency USD), Blended ROAS This Quarter (numbers), Primary KPI Performance vs Target (percentage), Secondary KPI Performance vs Target (percentage), Performance vs Prior Quarter (percentage), Industry Benchmark Position (dropdown: Top 25%, Top 50%, Below Average, Well Below Average), Key Insights Generated (long text), Strategic Recommendations (long text), Competitive Intelligence (long text), Expansion Opportunities Identified (long text), Client Feedback/Questions from Last QBR (long text), Presentation Template Used (dropdown: Standard, E-commerce, B2B, Executive Summary), QBR Recording/Notes Link (link), Follow-Up Tasks Created (numbers). Sub-items for detailed metrics: Metric Name (text), Current Quarter Result (numbers), Prior Quarter Result (numbers), YoY Comparison (numbers), Industry Benchmark (numbers), Performance Rating (status: Exceeding, Meeting, Below, Concerning). Automations: 3 weeks before QBR Date, change status to Data Compiled and notify CSM; when all performance data is populated, auto-generate Key Insights based on performance patterns; 1 week before QBR, send reminder if status is not 'Presentation Ready'. Dashboard: upcoming QBRs (calendar view), QBR preparation pipeline (kanban by status), average client performance vs benchmarks (scatter plot), expansion opportunities pipeline (value summary)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** QBRGenius
**Agent Purpose:** Automate quarterly business review preparation by compiling performance data, generating strategic insights, and creating presentation-ready materials with minimal human intervention.

**Triggers:**
- QBR preparation schedule (3 weeks, 2 weeks, 1 week before QBR date)
- New quarterly data available (campaign platforms, industry benchmarks)
- Competitive intelligence update (competitor campaign changes, market shifts)
- Client requests interim performance review
- Performance anomaly during quarter requires QBR narrative update

**Actions:**
- Compile quarterly performance data across all channels and calculate key metrics
- Generate narrative insights explaining performance drivers (creative performance, audience optimization, seasonal trends, external factors)
- Research industry benchmarks and position client performance competitively
- Analyze competitor advertising activity and market share changes
- Identify expansion opportunities based on performance data and client business goals
- Create slide-ready charts and visualizations formatted for client presentation
- Draft strategic recommendations for next quarter based on performance trends and market analysis

**Data Required:**
- Campaign performance board (quarterly aggregation)
- Client account information and business goals
- Industry benchmark databases
- Competitive intelligence sources
- Historical QBR performance for trend analysis

**Autonomy Level:** Human-in-the-Loop
QBRGenius compiles data and generates insights autonomously. Strategic recommendations and competitive analysis require CSM review and customization before client presentation.

**Example Interaction:**
> Two weeks before the Q4 QBR for client "TechStartup Inc," QBRGenius compiles the quarterly analysis. Performance summary: $125K spend, 3.8x ROAS (up from 3.4x Q3), primary KPI (lead generation) 118% of target, secondary KPI (demo bookings) 95% of target. Industry benchmark: 3.2x average ROAS for B2B SaaS companies $10-50M revenue. Key insight: "Q4 performance driven by LinkedIn campaign optimization and new lookalike audiences from high-value customers. Google Ads performance declined in November (iOS attribution challenges) but recovered with GA4 enhanced conversions implementation." Competitive analysis: "Primary competitor InnovateCorp increased LinkedIn spend by 40% in Q4, targeting similar keywords. Recommend proactive budget increase to maintain share of voice." Strategic recommendations: "Expand LinkedIn to European markets (62% of website traffic from EMEA but 0% ad spend), test video creative formats (competitors seeing 35% higher engagement), and implement customer lifecycle campaigns for expansion revenue." CSM reviews, adjusts the European expansion timeline based on client's Q1 hiring plans, and finalizes the presentation.

---

### Use Case 4: Client Onboarding & Ramp Success Pipeline

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
New client onboarding at agencies is chaotic and manual. CSMs juggle 10-15 onboarding projects simultaneously, each with unique timelines, stakeholder requirements, and technical setups. Discovery calls happen without structured data capture, leading to misaligned expectations. Campaign launch delays are common because creative assets, tracking codes, and platform access get lost in email chains. The average onboarding takes 6-8 weeks when it should take 3-4. Poor onboarding experiences create immediate churn risk — 40% of client satisfaction issues trace back to onboarding problems.

#### The Solution
monday.com as a structured onboarding pipeline with templated workflows by service type (creative, media, integrated). Automated task sequences ensure no steps are missed. Stakeholder communication is centralized with client portal access for transparency. Success milestones and health checks identify at-risk onboardings before they derail.

#### The Outcome
Reduce onboarding timeline from 6-8 weeks to 3-4 weeks. Eliminate onboarding-related churn through systematic execution. Increase initial campaign performance by 20% through better setup. Enable CSMs to handle 25% more simultaneous onboardings.

#### Discovery Questions
- What's your average time from contract signature to first campaign launch?
- What percentage of onboarding projects hit their original launch date?
- How do you ensure no critical onboarding steps get missed across different service types?
- What's the most common reason for onboarding delays — client inputs, creative production, or technical setup?
- How do you measure onboarding success beyond just campaign launch?

#### Industry Context
"Onboarding" in agencies includes discovery (understanding client business, competitors, target audiences), technical setup (tracking implementation, platform access, creative briefing), stakeholder alignment (approval processes, communication cadences, reporting preferences), and launch preparation (campaign build, creative production, testing protocols). "Ramp" refers to the initial performance period where campaigns are optimized to full potential. "Time to value" measures how quickly clients see meaningful results. Poor onboarding creates "churn debt" — clients who'll leave within 6 months due to early negative experiences.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a client onboarding and ramp success pipeline for an agency Customer Success team. Board: Client Onboarding Pipeline. Columns: Client Name (text), Service Type (dropdown: Media Only, Creative Only, Integrated Campaign, Social Media, Influencer Marketing, SEO/Content), Contract Value (numbers, currency USD), Onboarding Start Date (date), Target Launch Date (date), Actual Launch Date (date), Days to Launch (formula), Onboarding Status (status: Discovery, Technical Setup, Creative Production, Platform Build, Testing, Launched, Ramp Complete), CSM Owner (people), Project Manager Assigned (people), Discovery Completion (percentage), Technical Setup Completion (percentage), Creative Assets Completion (percentage), Campaign Build Completion (percentage), Client Stakeholder Primary (text), Client Stakeholder Secondary (text), Approval Process Type (dropdown: Single Approver, Dual Approval, Committee Review, Legal + Marketing), Platform Access Status (status: Requested, Pending Client, Complete), Tracking Implementation (status: Not Started, In Progress, Testing, Live), First Campaign Performance (numbers: initial CPA/ROAS), Ramp Target Achieved (checkbox), Onboarding Health Score (formula based on timeline, completion rates, client communication), Risk Factors (dropdown: Slow Client Response, Technical Complications, Creative Revisions, Budget Changes, Internal Delays), Client Satisfaction Survey Score (numbers, 1-10). Sub-items for onboarding tasks: Task Name (text), Task Owner (people), Due Date (date), Completion Status (status), Notes (text). Automations: when new client added, auto-populate task list based on Service Type; when any task is >3 days overdue, notify CSM and Project Manager; when Onboarding Status reaches Launched, create 30-day ramp check-in task. Dashboard: onboarding pipeline by status (funnel chart), average days to launch by service type (bar chart), onboarding health scores (gauge), at-risk onboardings requiring attention (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OnboardBot
**Agent Purpose:** Orchestrate seamless client onboarding workflows, predict and prevent delays, and ensure optimal campaign ramp performance.

**Triggers:**
- New client contract signed (onboarding initiation)
- Task completion or delay (workflow progression)
- Client response received on discovery questionnaire
- Platform access granted or delayed
- Creative assets submitted for review
- Campaign launch completed (ramp monitoring begins)
- 30-day ramp milestone reached

**Actions:**
- Auto-populate service-specific onboarding task lists with realistic timelines
- Monitor task completion and proactively identify bottlenecks before they cause delays
- Generate client-specific discovery questions based on industry vertical and service type
- Track platform access requests and follow up on delays
- Monitor creative production timeline and flag potential revisions early
- Calculate onboarding health scores based on timeline adherence, client responsiveness, and completion quality
- Trigger ramp success monitoring post-launch with performance benchmarking

**Data Required:**
- Onboarding pipeline board
- Service-specific task templates
- Client account data and industry verticals
- Platform access requirements by advertising channel
- Historical onboarding performance for benchmarking

**Autonomy Level:** Human-in-the-Loop
OnboardBot manages task scheduling and progress tracking autonomously. Client communications and escalations require human review. Launch decisions always require CSM approval.

**Example Interaction:**
> A new client "EcoProducts" signs a $200K integrated campaign contract on Monday. OnboardBot immediately creates the onboarding pipeline item and populates 23 tasks across Discovery (8 tasks), Technical Setup (6 tasks), Creative Production (5 tasks), and Campaign Build (4 tasks). It schedules the discovery call for Thursday and sends the client a pre-work questionnaire about target audiences, competitive landscape, and past campaign performance. By Friday, OnboardBot flags that EcoProducts hasn't returned the questionnaire and suggests CSM outreach: "Client questionnaire delayed. Recommend proactive call — eco/sustainability brands often have complex audience segmentation that needs early discussion to avoid creative revision cycles." Week 2, OnboardBot notices Google Ads platform access is delayed (common with new advertiser accounts) and automatically escalates to Google rep while suggesting Meta and LinkedIn campaign builds proceed in parallel. Result: launch happens on schedule despite Google delay, with Google launching 3 days after other channels.

---

### Use Case 5: Contract Renewal & Expansion Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Contract renewals sneak up on CS teams because renewal preparation is manual and inconsistent. CSMs track renewal dates in spreadsheets, but preparation starts too late — often 30 days before expiration when it should begin 6 months out. Expansion conversations are reactive instead of proactive, triggered by client requests rather than strategic opportunities. Pricing negotiations rely on manual ROI calculations that take hours to compile. Leadership lacks visibility into the renewal pipeline, making revenue forecasting difficult and resource planning impossible.

#### The Solution
monday.com as the renewal and expansion pipeline with automated preparation workflows. Six-month renewal preparation sequences include performance compilation, ROI analysis, competitive benchmarking, and expansion opportunity identification. Success metrics and relationship health inform renewal probability and pricing strategy.

#### The Outcome
Increase renewal rate from 78% to 88% through systematic preparation. Grow average contract value by 25% through proactive expansion. Reduce renewal preparation time from 8 hours to 2 hours per client. Provide leadership with accurate revenue forecasting 12 months in advance.

#### Discovery Questions
- What percentage of your client contracts renew, and at what average price change?
- How far in advance do you start preparing for contract renewals?
- What's your process for identifying expansion opportunities — do you wait for clients to ask, or do you proactively suggest them?
- How do you calculate and present ROI to justify rate increases during renewals?
- Can your leadership accurately forecast renewal revenue 6-12 months out?

#### Industry Context
"Renewals" in agencies can be annual retainer agreements, project-based contracts with renewal options, or evergreen SOWs (Statement of Work) with termination clauses. "Expansion" means increasing contract value through additional services (adding social to a media retainer), increased spend (higher media budgets), or new divisions/brands. "Renewal probability" is calculated based on performance, relationship health, and market factors. "Price escalation" is common — agencies typically increase rates 5-15% annually to account for inflation and improved capabilities. "SOW" (Statement of Work) defines scope, pricing, and terms for agency services.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a contract renewal and expansion pipeline for an agency Customer Success team. Board: Renewal Pipeline. Columns: Client Name (text), Current Contract Value (numbers, currency USD), Contract Start Date (date), Contract End Date (date), Days to Renewal (formula), Renewal Status (status: Planning Phase, Performance Review, Proposal Developed, Client Discussion, Negotiating, Renewed, Lost, Extended), Renewal Probability (numbers, 0-100%), Proposed New Contract Value (numbers, currency USD), Contract Growth (formula: percentage increase), Renewal Type (dropdown: Standard, Expansion, Reduction, Restructure), Expansion Opportunities (long text), Key Stakeholder Client (text), Decision Timeline (date), Competitive Threats (dropdown: Budget Cuts, In-House Team, Competitor Pitch, Performance Issues, Executive Change, None Known), Performance Summary YTD (long text), ROI/Value Delivered (numbers: calculated ROAS, cost savings, lead value), Pricing Strategy (dropdown: Hold, Increase 5-10%, Increase 10-15%, Increase 15%+, Decrease), CSM Owner (people), Last Client Touch Date (date), Next Planned Touch (date), Renewal Meeting Scheduled (date), Contract Sent Date (date), Response Due Date (date). Sub-items for expansion opportunities: Service Area (dropdown: Social Media, Influencer, CRO, Email Marketing, SEO, Creative, Video Production), Opportunity Value (numbers, currency USD), Pitch Status (status), Client Interest Level (dropdown: High, Medium, Low, Not Discussed). Automations: when Days to Renewal hits 180, change status to Planning Phase and notify CSM; when Renewal Probability drops below 70%, notify CS leadership; when Contract End Date is <60 days and status is not Renewed/Extended, create urgent escalation task. Dashboard: renewal pipeline by quarter (bar chart), total renewal revenue at risk (number), expansion pipeline value (number), renewal rate by CSM (table), contract value growth trend (line chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RenewalRadar
**Agent Purpose:** Systematically manage contract renewal pipeline, identify expansion opportunities, and optimize renewal probability through data-driven preparation.

**Triggers:**
- Contract renewal milestone dates (180, 120, 90, 60, 30 days before expiration)
- Performance data update (monthly campaign results)
- Client health score change that affects renewal probability
- Competitive intelligence about client considering other agencies
- Expansion opportunity identified through performance analysis
- Renewal meeting completed (follow-up workflow activation)

**Actions:**
- Calculate comprehensive ROI metrics for renewal justification (revenue generated, cost savings, efficiency gains)
- Identify expansion opportunities based on performance data and client business growth
- Generate renewal preparation materials (performance summaries, competitive comparisons, strategic recommendations)
- Recommend pricing strategy based on performance delivery, market rates, and relationship strength
- Track renewal milestone completion and flag at-risk renewals for escalation
- Draft expansion opportunity pitches with business case and investment requirements

**Data Required:**
- Renewal pipeline board
- Campaign performance data for ROI calculation
- Client business information and growth indicators
- Competitive landscape and market pricing data
- Historical renewal success factors

**Autonomy Level:** Human-in-the-Loop
RenewalRadar manages timeline tracking and data compilation autonomously. Pricing strategies and client communications require CSM review. Renewal probability assessments are recommendations for human validation.

**Example Interaction:**
> It's January 15th and client "FashionForward" has a July 31st contract renewal (196 days out). RenewalRadar triggers the Planning Phase and compiles the performance summary: current $150K annual contract, YTD ROAS 4.2x (target 3.5x), customer acquisition cost down 28% from prior year, generated $1.8M in attributed revenue. Market analysis shows fashion retail agencies averaging 3.1x ROAS, positioning FashionForward performance in the top 20%. Expansion analysis identifies opportunities: email marketing ($2K/month - they're spending $15K on Klaviyo but performance could improve 35% with integrated strategy), influencer program ($5K/month - currently managing influencers in-house with poor ROI tracking), and TikTok advertising ($3K/month - strong organic presence but zero paid social). RenewalRadar recommends: "Propose $165K base retainer (+10% performance increase) plus $120K in expansion services. Total package $285K represents 90% growth but delivers estimated $400K+ in additional annual revenue. Strong renewal probability: 85%." CSM reviews, agrees with the base increase but suggests starting expansion conversation with just email marketing to avoid overwhelming the client.

---

### Use Case 6: Performance Anomaly Detection & Alert System

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Campaign performance issues are discovered too late because CSMs can't monitor all client accounts in real-time. By the time monthly reports surface a problem — CPA spike, ROAS decline, budget overspend — clients have lost money and trust is damaged. CSMs rely on periodic check-ins rather than continuous monitoring, so performance problems compound for weeks before detection. When issues are discovered, root cause analysis takes hours of manual investigation across multiple platforms.

#### The Solution
monday.com as a real-time performance monitoring system with intelligent anomaly detection. Machine learning models identify performance deviations, attribute them to likely causes, and trigger automated investigation workflows. Smart alerts filter noise and surface only actionable insights requiring human intervention.

#### The Outcome
Reduce campaign issue discovery time from weeks to hours. Prevent budget waste through immediate anomaly detection. Increase client satisfaction through proactive issue resolution. Reduce CSM manual monitoring time by 70%.

#### Discovery Questions
- How quickly do you typically discover when a client's campaign performance drops significantly?
- What percentage of performance issues are caught proactively versus client complaints?
- When you discover a performance problem, how long does it take to identify the root cause?
- How much client budget is typically wasted before performance issues are identified and fixed?
- Do your clients find out about campaign problems from you or from their own analytics?

#### Industry Context
"Performance anomalies" include CPA spikes, ROAS declines, impression drops, click-through rate changes, and budget pacing issues. "Root cause analysis" investigates whether anomalies stem from platform changes (algorithm updates, policy changes), competitive activity (bid increases, new entrants), seasonal factors, creative fatigue, or technical issues. "Attribution delays" mean performance data is often 24-72 hours behind reality. "Statistical significance" is required to separate normal variation from true performance changes. Machine learning can identify patterns humans miss in multi-variable campaign optimization.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a performance anomaly detection and alert system for agency Customer Success teams. Board: Performance Monitoring Dashboard. Columns: Client Name (text), Campaign Name (text), Alert Type (status: CPA Spike, ROAS Decline, Impression Drop, Budget Overspend, CTR Decline, Conversion Drop), Anomaly Severity (status: Low, Medium, High, Critical), Alert Triggered Date (date), Platform Affected (dropdown: Google Ads, Meta, LinkedIn, TikTok, Programmatic, Cross-Platform), Baseline Performance (numbers: normal CPA/ROAS), Current Performance (numbers), Performance Change (formula: percentage variance), Anomaly Duration (numbers: days), Probable Cause (dropdown: Platform Algorithm Change, Competitive Activity, Seasonal Factor, Creative Fatigue, Technical Issue, Budget Constraint, Audience Saturation), Investigation Status (status: New, Investigating, Root Cause Identified, Fix Implemented, Monitoring Recovery), CSM Assigned (people), Client Notified (checkbox), Estimated Budget Impact (numbers, currency USD), Resolution Timeline (date), Fix Description (long text), Performance Recovery Status (status: Not Started, In Progress, Partial Recovery, Full Recovery). Sub-items for investigation steps: Investigation Step (text), Assigned To (people), Findings (text), Status (status). Automations: when Alert Type is High or Critical, immediately notify CSM and create investigation task; when Anomaly Duration >3 days without investigation status change, escalate to CS leadership; when Performance Recovery Status reaches Full Recovery, send success notification and close alert. Dashboard: active alerts by severity (pie chart), alert volume trend (line chart), time to resolution by alert type (bar chart), budget impact prevented through early detection (number), platform anomaly frequency (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PerformanceGuard
**Agent Purpose:** Monitor campaign performance across all platforms, detect anomalies using statistical analysis, and provide intelligent root cause suggestions to accelerate resolution.

**Triggers:**
- Campaign performance data refresh (every 4 hours during business hours, daily overnight)
- Statistical anomaly detected (performance outside 2-3 standard deviations from baseline)
- Budget pacing alert (>15% ahead or behind schedule)
- Platform-specific notifications (Google/Meta algorithm updates, policy changes)
- Client-specific threshold breaches (custom KPI alerts per account)

**Actions:**
- Analyze performance data for statistical anomalies using machine learning models trained on historical patterns
- Cross-reference anomalies with external factors (platform updates, seasonality, competitive intelligence)
- Generate probable cause hypotheses ranked by likelihood based on similar historical incidents
- Create automated investigation checklists based on anomaly type and platform
- Calculate budget impact and provide urgency recommendations for CSM response
- Draft client communication templates with explanation and resolution timeline
- Monitor resolution effectiveness and update anomaly detection models

**Data Required:**
- Campaign performance board with historical data
- Platform change logs and algorithm update notifications
- Competitive intelligence feeds
- Seasonal performance baselines by client industry
- Resolution effectiveness data for model improvement

**Autonomy Level:** Fully Autonomous (detection) + Human-in-the-Loop (response)
PerformanceGuard detects anomalies and investigates probable causes autonomously. All client communications and campaign changes require human approval.

**Example Interaction:**
> PerformanceGuard detects that client "HomeGym Equipment" Facebook campaigns experienced a 45% CPA increase over the past 48 hours, from baseline $32 to current $46. Cross-analysis reveals: Google Ads performance unchanged, email marketing stable, website conversion rates normal. External factor check identifies no major platform updates or obvious seasonality. Competitive analysis shows 3 fitness equipment competitors increased Facebook spend 20-30% this week (possible bidding war). PerformanceGuard recommends: "Probable cause: competitive bidding pressure in fitness vertical post-New Year. Suggested investigation: analyze auction insights for impression share loss, review audience overlap with competitors, consider day-parting optimization to avoid peak competition hours. Estimated budget impact: $2,100 overspend if trend continues 7 days. Urgency: Medium - monitor 24h more before major changes." CSM investigates, confirms competitive pressure, and shifts 30% of Facebook budget to Google Ads where CPA remains stable, while preparing creative refresh to improve Facebook relevance scores.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ROAS | Return on Ad Spend — revenue generated divided by advertising spend |
| CPA | Cost Per Acquisition — advertising spend divided by number of conversions |
| LTV | Lifetime Value — total revenue a customer generates over their entire relationship |
| Blended Performance | Combined metrics across all marketing channels into unified KPIs |
| QBR | Quarterly Business Review — formal client meeting reviewing performance and strategy |
| Churn | Customer cancellation or contract non-renewal |
| NPS | Net Promoter Score — client satisfaction metric from -100 to +100 |
| SOW | Statement of Work — document defining project scope, timeline, and pricing |
| Health Score | Composite metric indicating client relationship and renewal probability |
| Attribution | Method of crediting conversions to marketing touchpoints |
| Incrementality | Measuring true causal impact of advertising versus correlation |
| Share of Voice | Brand's media presence relative to competitors |
| MMM | Marketing Mix Modeling — statistical approach to measure channel effectiveness |
| Walled Garden | Closed platforms (Google, Meta, Amazon) with proprietary data and attribution |
| Expansion Revenue | Additional revenue from existing clients through upselling or cross-selling |
| Retainer | Ongoing monthly fee for agreed scope of services |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/Director of Customer Success | CS strategy, team leadership, renewal/expansion goals | Decision-maker |
| Senior Customer Success Manager | Strategic client relationships, complex renewals, team mentoring | Decision-maker |
| Customer Success Manager | Day-to-day client management, performance monitoring, renewal execution | Primary User |
| Junior CSM / CS Analyst | Data compilation, report building, onboarding support | User |
| Account Director/Manager | Cross-functional client relationship, project oversight | Influencer |
| Data Analyst | Performance measurement, attribution modeling, benchmark research | User |
| Operations Manager | Process optimization, tool management, workflow design | Influencer |
| Revenue Operations | Forecasting, pricing strategy, renewal pipeline management | Decision-maker |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Account Management | Client relationship ownership, project delivery, scope management | Unified client management platform |
| Media Planning & Buying | Campaign strategy, platform management, performance optimization | Integrated performance dashboard |
| Creative Services | Asset production, approval workflows, performance creative iteration | Streamlined creative-performance feedback loops |
| Data & Analytics | Attribution modeling, measurement strategy, competitive analysis | Centralized data hub feeding CS insights |
| Finance | Contract management, billing, profitability analysis | Automated renewal and expansion financial modeling |
| New Business | Prospect nurturing, proposal development, competitive positioning | Leveraging client success stories for new business |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| HubSpot / Salesforce | CRM + Customer Success platform | Strong for contact management but weak on campaign performance integration and agency-specific workflows |
| ChurnZero / Gainsight | Purpose-built CS platforms | SaaS-focused, don't integrate with advertising platforms or understand agency success metrics |
| Tableau / Looker | Business intelligence and dashboards | Powerful for data visualization but require technical resources and don't provide workflow management |
| Google Analytics / Adobe Analytics | Web analytics and attribution | Great for website data but miss the operational CS workflows and multi-platform campaign aggregation |
| Asana / Notion | Work management and collaboration | Generic project management without CS-specific features or advertising platform integrations |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have a CRM that tracks customer health" | "Your CRM is great for contact management, but does it pull real-time campaign performance from Google, Meta, and LinkedIn to calculate health scores? We're not replacing your CRM — we're connecting your campaign data to your client relationships in one place." |
| "Performance data changes too quickly — daily dashboards won't help" | "That's exactly why you need automated monitoring instead of manual checks. When a client's Facebook CPA spikes 40% overnight, wouldn't you rather know at 9 AM with a suggested fix instead of discovering it in next week's report?" |
| "Our clients won't adopt another platform for reporting" | "They don't need to adopt anything — they get a dashboard link that shows their performance 24/7. No logins, no training. Most clients love having real-time visibility instead of waiting for monthly reports." |
| "We're too small to need this level of automation" | "Actually, smaller teams need automation more. When one CSM manages 20+ clients, you can't manually monitor performance across 60+ campaigns. Start with performance monitoring for your biggest client — you'll see the value immediately." |
| "Campaign performance is too complex for automated insights" | "We're not replacing your expertise — we're giving you better data faster. Instead of spending 2 hours diagnosing why a client's ROAS dropped, you get the probable cause in 10 minutes and spend your time fixing it." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for CS workflow transformation case study]
- [Placeholder for client churn reduction success story]
- [Placeholder for renewal rate improvement reference]
- [Placeholder for QBR automation efficiency gains]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*