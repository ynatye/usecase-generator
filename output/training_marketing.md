# Training × Marketing Playbook

## Overview

Marketing departments in training organizations serve a uniquely complex mandate: they must simultaneously market the training company itself (B2B brand awareness, lead generation, thought leadership) while also supporting the marketing of individual training programs, certifications, and learning products to diverse audiences — corporate L&D buyers, individual learners, HR leaders, and channel partners. Unlike SaaS marketing where the product is relatively static, training marketing teams must continuously promote a rotating catalog of hundreds or thousands of courses, programs, and certifications, each with different target personas, pricing, and seasonal relevance.

Training company marketing teams typically range from 5-20 people in mid-market firms, encompassing content marketing, demand generation, digital marketing, events/webinars, partner marketing, and product marketing. The team operates at the intersection of sales enablement and product development — they need deep understanding of learning outcomes to create compelling messaging, while also driving measurable pipeline. The challenge is compounded by the industry's shift from in-person to digital delivery, which has dramatically expanded the competitive landscape from regional players to global e-learning platforms.

Key regulatory considerations include CAN-SPAM and GDPR for email marketing, FTC guidelines for testimonials and outcome claims (especially in professional certification marketing), and accessibility requirements (WCAG) for marketing content that represents inclusive learning brands. Continuing education units (CEU/CPE) marketing must comply with accreditation body guidelines. The training industry also faces unique credibility challenges — marketing must balance aspiration with realistic outcome promises to avoid the perception of "diploma mill" tactics.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Marketing must promote hundreds of programs across multiple channels simultaneously; automation and AI-generated content are essential to scale without proportional headcount |
| 2 | Replace or Radically Augment Headcount | High | Small teams (5-20 people) handle B2B demand gen, program marketing, content creation, events, and partner enablement — AI can draft content, analyze performance, and automate campaigns |
| 3 | Consolidate Tech Stack with AI | Medium-High | Marketing teams typically run 10-15+ tools (MAP, CMS, social scheduling, webinar, analytics, SEO, email, design) creating data silos and integration headaches |

## Prioritized Use Cases

---

### Use Case 1: Program & Course Launch Campaign Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies launch 20-50+ new programs, courses, and certifications annually. Each launch requires a coordinated campaign: landing pages, email sequences (awareness → nurture → enrollment), social media content, webinar promotion, partner enablement kits, paid ad creative, and sales enablement materials. Campaign management lives across multiple tools — tasks in Asana, emails in HubSpot, social in Hootsuite, design in Figma, approvals in email threads. No one has a single view of "where does the AI Ethics Certification launch stand?" Deadlines slip because dependencies aren't visible — the email sequence can't launch without the landing page, which is waiting on testimonial approval from legal. With 30+ active campaigns at any time, things constantly fall through cracks.

#### The Solution
Build a **monday.com Work Management** Campaign Command Center. Create a master Campaign board with: Program Name (connect to Program Catalog board), Campaign Type (dropdown: New Launch, Re-Launch, Seasonal Push, Certification Window, Event-Tied), Target Persona (dropdown: L&D Directors, HR Leaders, Individual Learners, Channel Partners, C-Suite), Launch Date (date), Campaign Owner (people), Status (status: Planning, Content Creation, Review/Approval, Scheduled, Live, Post-Analysis), Budget (numbers), Projected Enrollments (numbers), Actual Enrollments (numbers), ROI (formula). Create subitems for every deliverable: landing page, email sequence (3-5 emails), social posts (8-12), paid ad creative (3-5 variations), webinar registration page, partner toolkit, sales one-pager, blog post. Each subitem has its own status, assignee, due date, and approval status. Use **Timeline view** for cross-campaign coordination, **automations** for approval routing and deadline alerts, and **Dashboards** for marketing leadership visibility.

#### The Outcome
Reduce campaign launch time from 6 weeks to 3 weeks through parallel workstream visibility. Eliminate missed deliverables with automated dependency tracking. Enable marketing leadership to see all active campaigns, resource allocation, and performance in a single dashboard. Increase campaign output by 40% without adding headcount.

#### Discovery Questions
1. "How many program launches or marketing campaigns does your team run concurrently? Where do you track all the moving pieces?"
2. "When was the last time a campaign deliverable was missed or launched late because of a dependency nobody saw coming?"
3. "How do you coordinate between content writers, designers, email marketers, and the program team for a single launch?"
4. "What's your approval workflow — how many people need to review and approve before something goes live?"
5. "After a campaign ends, do you systematically analyze what worked and apply those learnings to the next launch?"

#### Industry Context
Training program launches are time-sensitive — certification windows have enrollment deadlines, seasonal programs (back-to-school leadership development) have narrow marketing windows, and event-tied programs (pre-conference workshops) must be promoted in sync with event marketing. Unlike SaaS product launches that happen quarterly, training companies may have weekly launch cadences for new course additions to their catalog. The proliferation of microlearning and on-demand content has increased the volume of "products" that need marketing while decreasing the marketing investment justified per product — making efficiency critical.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Campaign Command Center with two connected boards. Board 1 — Campaigns: Campaign Name (text), Program (connect to Programs board), Campaign Type (dropdown: New Program Launch, Re-Launch, Seasonal Promotion, Certification Window, Event-Tied, Partnership), Target Persona (dropdown: L&D Directors, HR Leaders, Individual Learners, Channel Partners, C-Suite, Industry-Specific), Launch Date (date), End Date (date), Campaign Owner (people), Status (status: Ideation, Planning, Content Creation, Review & Approval, Scheduled, Live, Post-Analysis, Complete), Total Budget (numbers), Spent to Date (numbers), Budget Remaining (formula), Target Enrollments (numbers), Actual Enrollments (numbers), Enrollment Conversion Rate (formula), Pipeline Generated (numbers), Revenue Attributed (numbers), Channel Mix (tags: Email, Social-Organic, Social-Paid, Webinar, Blog, PPC, Partner, Direct Mail). Add subitems for deliverables: each with Deliverable Name (text), Type (dropdown: Landing Page, Email, Social Post, Paid Ad, Blog, Webinar, Partner Kit, Sales Enablement, Video, Infographic), Assignee (people), Due Date (date), Status (status: Not Started, Drafting, In Review, Approved, Scheduled, Published), Reviewer (people). Board 2 — Campaign Calendar: mirror key fields from Board 1 for calendar visualization. Automations: when Campaign Status moves to Content Creation, create standard subitem deliverable set based on Campaign Type; when subitem Status changes to In Review, notify Reviewer; 2 days before Launch Date with any subitem not Approved, alert Campaign Owner; when Campaign Status moves to Live, trigger enrollment tracking. Dashboard: active campaigns by status (chart), campaigns by persona (pie), total budget vs spend (numbers), enrollment targets vs actuals (chart), upcoming launches this month (timeline), campaign ROI ranking (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CampaignPilot Agent
**Agent Purpose:** Orchestrate multi-channel campaign execution, identify bottlenecks before they cause delays, and generate performance insights.

**Triggers:**
- New campaign item created (auto-generates deliverable subitems based on type)
- Any deliverable subitem past due date
- 5 days before campaign launch date
- Campaign moved to "Live" status
- Campaign moved to "Post-Analysis" status

**Actions:**
- Generate standard deliverable checklist based on campaign type and target persona
- Daily scan for at-risk deliverables (approaching deadline, dependencies incomplete) and alert campaign owner
- Create launch readiness report 5 days before launch: what's done, what's pending, what's blocked
- When campaign goes live, set up enrollment tracking dashboard and daily performance monitoring
- Generate post-campaign analysis report: enrollment vs target, cost per enrollment, best-performing channel, recommendations for next campaign
- Suggest optimal launch timing based on historical enrollment patterns by persona and program type

**Data Required:**
- Historical campaign performance data (enrollments, conversion rates, spend)
- Program catalog with pricing and enrollment capacity
- Content calendar and team availability
- Email marketing platform performance metrics
- Social media engagement data

**Autonomy Level:** Human-in-the-Loop
Autonomous for monitoring, alerting, and analysis generation. Requires human approval for content creation, budget allocation changes, and launch/pause decisions.

**Example Interaction:**
> Five days before the "Advanced Data Analytics Certification" launch, the CampaignPilot Agent generates a readiness report: "Launch Readiness: 🟡 78%. Complete: Landing page (live), email sequence 1-3 of 5 (approved), social posts (8/12 scheduled), paid ad creative (approved). At Risk: Email 4 (enrollment deadline reminder) — still in drafting, assigned to Mark who is also working on 2 other campaigns this week. Blocker: Testimonial video from Beta cohort participant — waiting on legal approval since Monday. Recommendation: Reassign Email 4 to Sarah (she has bandwidth) and escalate testimonial approval to marketing director. Historical note: Data Analytics programs perform 23% better with video testimonials — worth the push."

---

### Use Case 2: Content Marketing & Thought Leadership Pipeline

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Training companies live and die by thought leadership — L&D buyers choose training providers they trust as domain experts. This requires a constant stream of blog posts, whitepapers, industry reports, webinars, podcast episodes, and social content. A typical content calendar demands 8-12 blog posts, 2-4 whitepapers/guides, 4-6 webinars, and 40-60 social posts per month. Content marketing teams of 2-4 people can't sustain this volume while maintaining quality and industry specificity. Subject matter experts (trainers, consultants) have knowledge but no time to write. Content ideas are scattered across Slack messages, meeting notes, and individual notebooks. SEO strategy is disconnected from content planning.

#### The Solution
Create a **monday.com Work Management** Content Pipeline board. Track: Content Title (text), Content Type (dropdown: Blog Post, Whitepaper, E-book, Case Study, Webinar, Podcast, Infographic, Video, Social Series, Industry Report), Topic Cluster (dropdown mapped to SEO pillars), Target Keyword (text), Search Volume (numbers), Difficulty Score (numbers), Funnel Stage (dropdown: Awareness, Consideration, Decision), Target Persona (dropdown), Subject Matter Expert (people), Writer (people), Editor (people), Status (status: Idea, Approved, Outline, Draft, Review, Final Edit, Designed, Published, Promoted), Publish Date (date), Distribution Channels (tags), Performance — Views (numbers), Performance — Leads (numbers), Performance — Shares (numbers). Use **automations** to move content through the pipeline, notify reviewers, and trigger promotion workflows upon publishing. **monday AI** assists with content brief generation and outline creation.

#### The Outcome
Increase content output by 60% with the same team size through streamlined workflows and AI-assisted creation. Align 100% of content to SEO strategy with topic cluster tracking. Reduce content production cycle from 3 weeks to 10 days. Build a searchable content library that prevents duplicate topic creation.

#### Discovery Questions
1. "How many pieces of content does your team produce monthly, and what's the bottleneck — ideation, writing, review, or design?"
2. "How do you ensure your content aligns with SEO strategy? Is there a feedback loop between search performance and content planning?"
3. "How do you capture expertise from your trainers and consultants? Do they contribute to content, or is that entirely on the marketing team?"
4. "When you publish a blog post, what's the promotion workflow? Is it systematic or ad hoc?"
5. "Can you tell me which content piece generated the most leads last quarter, and why?"

#### Industry Context
Training industry content marketing must demonstrate genuine expertise — L&D buyers are sophisticated and can detect generic content immediately. High-performing training company content includes: original research reports (e.g., "State of Leadership Development 2026"), methodology deep-dives that showcase proprietary frameworks, client success stories with measurable outcomes, and expert commentary on industry trends (skills gaps, AI in learning, DEI training evolution). Webinars double as lead generation and product demonstration — a 60-minute webinar on "Designing Microlearning for Gen Z Workforces" simultaneously positions the company as an expert and previews their training methodology.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Content Marketing Pipeline board with: Content Title (text), Content Type (dropdown: Blog Post, Whitepaper, E-book, Case Study, Webinar, Podcast Episode, Infographic, Video, Social Media Series, Industry Report, Email Newsletter), Topic Cluster (dropdown: Leadership Development, Technical Skills, Compliance Training, DEI & Inclusion, Digital Transformation, Learning Technology, Employee Experience, Certification & Credentialing, AI in Learning, Remote Workforce), Target Keyword (text), Monthly Search Volume (numbers), Keyword Difficulty (numbers), Funnel Stage (dropdown: Top-Awareness, Mid-Consideration, Bottom-Decision), Target Persona (dropdown: L&D Director, HR VP, Individual Learner, CEO/C-Suite, Training Manager, Channel Partner), Subject Matter Expert (people), Writer/Creator (people), Editor (people), Designer (people), Status (status: Idea Submitted, Approved, Brief Created, Outline Done, First Draft, SME Review, Editorial Review, Final Edit, Design/Layout, Published, Promoted), Word Count Target (numbers), Publish Date (date), Distribution Channels (tags: Blog, LinkedIn, Twitter, Email Newsletter, Partner Network, Paid Promotion, YouTube, Podcast), CTA Type (dropdown: Free Resource Download, Webinar Registration, Demo Request, Course Enrollment, Newsletter Signup), Leads Generated (numbers), Page Views (numbers), Social Shares (numbers), Backlinks (numbers). Automations: when Status changes to SME Review, notify Subject Matter Expert with 3-day deadline; when Status changes to Published, create promotion subitem tasks (LinkedIn post, email inclusion, social scheduler); when content Idea Submitted, auto-notify editorial lead for approval within 48 hours; monthly trigger to flag content older than 12 months for refresh review. Dashboard: content by status (Kanban), publishing calendar (Timeline), content performance (top 10 by leads — table), output by type (pie chart), topic cluster coverage (chart showing gaps), monthly publishing velocity (trend chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ContentEngine Agent
**Agent Purpose:** Accelerate content production by generating briefs, identifying topic gaps, and optimizing content for SEO and conversion.

**Triggers:**
- New content idea submitted
- Content status moves to "Brief Created" (auto-generates outline)
- Published content reaches 30-day mark (performance review)
- Monthly schedule for topic gap analysis
- Quarterly schedule for content refresh audit

**Actions:**
- Generate content briefs with target keyword, competitive analysis, suggested headings, and key points based on topic cluster strategy
- Create first-draft outlines incorporating SME talking points and SEO requirements
- Analyze published content performance and recommend optimization (title changes, CTA adjustments, internal linking)
- Monthly topic gap analysis: compare existing content against target keyword list and identify missing pieces
- Quarterly content refresh: flag outdated statistics, broken links, and declining-traffic content for updates
- Suggest content repurposing opportunities (blog → infographic → social series → webinar)

**Data Required:**
- SEO tool data (keyword rankings, search volume, difficulty)
- Website analytics (traffic, conversions, bounce rates by content)
- Competitor content analysis
- SME expertise profiles (who knows what topics)
- Historical content performance data

**Autonomy Level:** Human-in-the-Loop
Autonomous for analysis, brief generation, and performance monitoring. Requires human review for all content before publication and strategic topic decisions.

**Example Interaction:**
> The ContentEngine Agent runs its monthly topic gap analysis: "Topic Cluster: AI in Learning — Current coverage: 12 pieces (strong on awareness, weak on decision-stage content). Gap identified: No case studies or ROI calculators for AI-powered training. Competitor analysis shows 3 top competitors published AI training ROI content in the last 60 days, averaging 2,400 shares. Recommendation: (1) Create 'AI Training ROI Calculator' interactive tool (high lead-gen potential), (2) Publish case study with FinanceCorp AI training deployment results, (3) Webinar: 'Measuring AI Training Impact — Beyond Completion Rates.' Estimated combined lead potential: 180-250 MQLs based on similar content performance."
>
> The marketing director approves all three. The agent generates detailed briefs for each, assigns them based on writer expertise and current workload, and sets deadlines aligned with the next certification window marketing push.

---

### Use Case 3: Event & Webinar Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies rely heavily on events and webinars for lead generation and brand building — hosting 50-100+ webinars and participating in 10-20 industry events annually. Each webinar involves speaker coordination, content preparation, registration page creation, promotional email sequences, social promotion, rehearsals, live production, recording, post-event follow-up, attendee scoring, and content repurposing. Event management for conferences requires booth logistics, speaking submissions, meeting scheduling, collateral production, and post-event lead processing. All of this is managed across spreadsheets, project management tools, email, and the webinar platform itself. Attendee data sits in the webinar tool, disconnected from the CRM, causing delayed follow-up and lost leads.

#### The Solution
Deploy **monday.com Work Management** for end-to-end event and webinar management. Create boards for: Webinar Calendar (master schedule with all planned webinars), Webinar Production (detailed checklist for each webinar's deliverables), Conference & Event Tracker (external events with logistics), and Post-Event Pipeline (attendee follow-up and lead processing). Key columns for Webinar Production: Webinar Title (text), Topic (dropdown), Speaker (people), Date/Time (date), Status (status: Ideation, Approved, In Production, Promotion, Rehearsal Complete, Live, Post-Event, Complete), Registration Target (numbers), Actual Registrations (numbers), Attendance Rate (formula), Recording Published (checkbox), Follow-up Sequence Sent (checkbox). **Automations** trigger promotional sequences at T-minus 3 weeks, 2 weeks, 1 week, and 1 day; post-event triggers drive follow-up emails and CRM updates.

#### The Outcome
Increase webinar output from 4/month to 8/month without additional event staff. Achieve 95% on-time post-event follow-up (within 24 hours). Improve registration-to-attendance rates by 15% through systematic promotional workflows. Reduce event logistics coordination time by 50%.

#### Discovery Questions
1. "How many webinars does your team produce monthly, and what's the biggest operational bottleneck?"
2. "What happens to webinar attendee data after the event? How quickly does it get to sales for follow-up?"
3. "How do you decide which industry conferences to attend or sponsor? Is there a systematic ROI evaluation?"
4. "When a webinar gets 500 registrations but only 150 attend, what's your re-engagement strategy for the no-shows?"
5. "Do you repurpose webinar content — blog posts, social clips, email content — or does the recording just sit on YouTube?"

#### Industry Context
Webinars serve a dual purpose in training marketing: they generate leads AND demonstrate the training company's delivery capabilities. A well-executed webinar essentially is the product demo — prospects experience the company's presentation quality, expertise, and engagement style firsthand. "Masterclass" style webinars (free 60-minute sessions on hot topics) are the highest-converting lead generation tactic for most training companies, with conversion rates 3-5x higher than gated content downloads. Industry events like ATD (Association for Talent Development), Learning Technologies, and DevLearn are critical for enterprise relationship building.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Webinar & Event Management system with two boards. Board 1 — Webinar Production: Webinar Title (text), Topic Category (dropdown: Leadership, Technical Skills, Compliance, DEI, Learning Tech, AI in L&D, Industry Trends, Product Demo, Customer Spotlight), Format (dropdown: Solo Presentation, Panel Discussion, Masterclass, Workshop, Fireside Chat, Customer Case Study), Speaker (people), Co-Presenter/Guest (text), Target Audience (dropdown: L&D Directors, HR Leaders, Individual Learners, Partners, Enterprise Prospects), Date & Time (date), Duration (dropdown: 30min, 45min, 60min, 90min), Platform (dropdown: Zoom Webinar, GoTo Webinar, ON24, Teams Live), Status (status: Ideation, Approved, Script/Deck Creation, Promotion Active, Rehearsal Scheduled, Rehearsal Complete, Day-Of, Live, Post-Production, Complete), Registration Page URL (text), Registration Target (numbers), Actual Registrations (numbers), Attendees (numbers), Attendance Rate (formula: Attendees/Registrations*100), Recording URL (text), Recording Published (checkbox), Leads Generated (numbers), Promotional Budget (numbers), Campaign Owner (people). Add subitems for checklist: Create Registration Page, Write Promotional Emails (3), Design Social Graphics, Schedule Social Posts, Speaker Prep Call, Rehearsal, Day-Of Tech Check, Send Follow-up Email, Publish Recording, Create Blog Recap, Cut Social Clips. Board 2 — Conference & Events: Event Name (text), Type (dropdown: Conference, Trade Show, Workshop, Meetup, Sponsorship), Location (text), Dates (date range), Our Role (dropdown: Attendee, Speaker, Exhibitor, Sponsor, Host), Budget (numbers), Staff Attending (people), Speaking Submissions (status), Booth Reserved (checkbox), Collateral Needed (tags), Meetings Scheduled (numbers), Leads Collected (numbers), ROI Score (numbers). Automations: 21 days before webinar Date, change Status to Promotion Active and trigger email subitem; 1 day after webinar, create follow-up subitems; when Attendance Rate is below 40%, flag for review; when Recording Published is checked, trigger social clip creation task. Dashboard: webinars this quarter (calendar), registrations vs attendance trend (chart), webinars by topic (pie), upcoming events (timeline), total leads from events (numbers), average attendance rate (numbers)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** EventOps Agent
**Agent Purpose:** Automate webinar production workflows, optimize promotional timing, and maximize post-event lead conversion.

**Triggers:**
- New webinar item created (generates production checklist)
- T-minus 21 days to webinar (promotional workflow activation)
- Webinar status changes to "Live" (real-time monitoring)
- T-plus 1 day after webinar (post-event follow-up sequence)
- Monthly schedule for webinar program performance review

**Actions:**
- Auto-generate production checklist subitems based on format and audience type
- Optimize promotional email send times based on historical open rate data by persona
- Monitor registration velocity and recommend budget adjustments (increase paid promotion if below target at T-minus 7)
- Generate post-webinar attendee segments: engaged (asked questions, stayed full session), passive (attended but no interaction), no-shows
- Draft personalized follow-up emails for each segment with recording link and relevant next steps
- Create content repurposing task list: blog recap, 3 social clips, email newsletter feature, quote graphics

**Data Required:**
- Webinar platform registration and attendance data
- Email marketing performance metrics
- CRM contact records for attendee matching
- Historical webinar performance benchmarks
- Social media engagement data for promotional posts

**Autonomy Level:** Escalation-Based
Autonomous for checklist generation, promotional scheduling, and attendee segmentation. Sends follow-up email drafts for human review. Escalates budget increase recommendations to marketing director.

**Example Interaction:**
> The EventOps Agent monitors the "Designing AI-Ready Workforce Training" masterclass, scheduled for next Thursday. At T-minus 7, it reports: "Registration Status: 312 of 500 target (62%). Registration velocity has slowed — only 18 new registrations in the last 3 days vs. 35/day the previous week. Recommendations: (1) Send 'Last Chance' email to unconverted opens from Email 2 (estimated 450 recipients), (2) Boost LinkedIn promoted post budget by $200 (currently pacing at 2.1x ROAS), (3) Ask speaker to share personal LinkedIn post — speaker-shared posts drive 3x more registrations than brand posts. Estimated impact: +80-120 additional registrations."
>
> Post-webinar, the agent segments 287 attendees: 94 "highly engaged" (asked questions or downloaded resources), 138 "passive attendees," and 55 "early dropoffs." It also identifies 213 no-shows. It drafts four tailored follow-up emails, creates CRM tasks for the 94 highly engaged contacts, and generates a blog recap outline from the webinar transcript.

---

### Use Case 4: Lead Management & Marketing-Sales Handoff

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Training companies generate leads across many channels: webinar registrations, whitepaper downloads, free course trials, event badge scans, website demo requests, partner referrals, and inbound inquiries. Lead quality varies wildly — an individual learner downloading a free guide is very different from a VP of L&D requesting a corporate training proposal. Marketing automation platforms (HubSpot, Marketo) score leads but the scoring models are generic and don't account for training-specific signals (company training budget size, number of employees to train, industry vertical, certification requirements). The handoff to sales is sloppy — leads sit in marketing automation too long, or get thrown over the wall to sales without context, resulting in wasted outreach and frustrated prospects.

#### The Solution
Use **monday.com CRM** integrated with Work Management for lead management. Create a Lead Pipeline board with: Lead Name (text), Company (text), Title (text), Source (dropdown: Webinar, Content Download, Free Trial, Event, Demo Request, Partner Referral, Inbound, PPC), Industry (dropdown), Company Size (dropdown: SMB <500, Mid-Market 500-5000, Enterprise 5000+), Estimated Training Need (dropdown: <50 learners, 50-500, 500-5000, 5000+), Interest Area (tags: Leadership, Technical, Compliance, DEI, Custom), Lead Score (numbers), Engagement History (long text), Status (status: New, MQL, Nurturing, SQL, Handed to Sales, Opportunity, Won, Lost, Disqualified), Assigned SDR (people), Last Touch (date), Next Action (text), Days in Stage (formula). **Automations** route leads based on company size and interest area, trigger nurture sequences for low-score leads, and create CRM opportunities when leads qualify.

#### The Outcome
Reduce lead response time from 48 hours to 2 hours for high-intent leads. Increase MQL-to-SQL conversion by 25% through better scoring and nurture. Eliminate lead leakage — 100% of leads tracked from source to outcome. Give sales reps full engagement context before their first outreach.

#### Discovery Questions
1. "How long does it take for a hot lead — say, a demo request — to get a response from your sales team?"
2. "What signals do you use to determine if a lead is marketing-qualified? Are training-specific signals (budget, learner count, compliance needs) factored in?"
3. "How do you nurture leads who aren't ready to buy yet? Is there a systematic nurture program or do they just go into a newsletter?"
4. "When sales follows up on a marketing lead, what context do they have? Do they know which webinars the person attended, what content they downloaded?"
5. "Can you trace a closed deal back to the original marketing touchpoint? What's your marketing attribution model?"

#### Industry Context
Training industry sales cycles vary dramatically by segment: individual learner purchases are transactional (minutes to days), while enterprise training contracts can take 3-12 months with multiple stakeholders (L&D, HR, Procurement, Legal, executive sponsor). High-value leads often emerge from "engagement signals" unique to training: completing a free course module (demonstrates serious interest), attending multiple webinars on the same topic (building business case), or downloading ROI calculators (procurement stage). The most valuable leads are companies going through transformations (mergers, digital transformation, regulatory changes) that create urgent, large-scale training needs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Lead Management Pipeline board with: Lead Name (text), Email (email), Company (text), Title (text), Phone (phone), Lead Source (dropdown: Webinar, Content Download, Free Course Trial, Conference/Event, Demo Request, Partner Referral, Inbound Form, PPC/Paid, Social Media, Cold Outreach Response), Industry (dropdown: Technology, Healthcare, Financial Services, Manufacturing, Retail, Government, Education, Professional Services, Energy, Non-Profit, Other), Company Size (dropdown: 1-100, 101-500, 501-2000, 2001-10000, 10000+), Estimated Learner Count (dropdown: Under 50, 50-200, 200-1000, 1000-5000, 5000+), Training Interest (tags: Leadership Development, Technical Skills, Compliance & Regulatory, DEI & Inclusion, Sales Training, Customer Service, Onboarding, Custom Program, Certification), Lead Score (numbers), Lead Grade (status: A-Hot, B-Warm, C-Nurture, D-Low Priority, F-Disqualified), Status (status: New, Contacted, Engaged, MQL, SQL, Opportunity Created, Handed to Sales, Won, Lost, Disqualified, Nurture), Assigned To (people), First Touch Date (date), Last Engagement (date), Days Since Last Touch (formula), Next Action (text), Next Action Date (date), Engagement Summary (long text), Deal Value Estimate (numbers). Automations: when Lead Source is Demo Request and Company Size is 501+, set Grade to A-Hot and immediately notify enterprise SDR; when Status is MQL for more than 7 days without activity, send reminder to Assigned To; when Lead Score exceeds 80, auto-change Status to SQL; when Grade is C-Nurture, add to automated email nurture sequence; when Status changes to Handed to Sales, create connected item on Sales Pipeline board with all engagement history. Create Kanban view grouped by Status, Table view sorted by Lead Score, and Dashboard: leads by source (chart), leads by status (funnel), average days to SQL (numbers), lead volume trend (chart), top performing sources by conversion rate (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LeadQualifier Agent
**Agent Purpose:** Automatically score, enrich, and route leads based on training-specific qualification criteria and engagement signals.

**Triggers:**
- New lead created from any source
- Lead engagement event (webinar attendance, content download, page visit)
- Lead idle for 14+ days without status change
- Lead score crosses SQL threshold (80+)
- Daily schedule for lead health check

**Actions:**
- Enrich lead with company data (industry, size, recent news, training-related job postings)
- Calculate training-specific lead score based on: company size × interest alignment × engagement depth × recency × source quality
- Route A-Hot leads immediately to appropriate SDR with context summary
- Draft personalized outreach suggestions for SDRs based on lead's engagement history
- Identify "dormant high-potential" leads (high company fit, low recent engagement) and recommend re-engagement campaigns
- Weekly lead pipeline health report: new leads, conversion rates by source, aging leads, recommendations

**Data Required:**
- CRM and marketing automation lead data
- Website analytics (page visits, content downloads)
- Webinar attendance and engagement data
- Company enrichment data (LinkedIn, Clearbit, ZoomInfo)
- Historical conversion data by lead source and industry

**Autonomy Level:** Escalation-Based
Autonomous for scoring, routing, and enrichment. Sends outreach drafts for SDR review. Escalates unusual patterns (lead volume spike, conversion rate drop) to marketing director.

**Example Interaction:**
> A new lead comes in: Sarah Chen, VP of Learning & Development at MedDevice Corp (4,200 employees), downloaded the "Compliance Training ROI Calculator" and registered for next week's "FDA Audit Readiness" webinar. The LeadQualifier Agent scores her: "Lead Score: 92/100 (A-Hot). Signals: VP-level title (+20), company size 4,200 (+15), healthcare/medical device industry (+10), compliance interest aligns with our strongest programs (+15), two high-intent actions within 48 hours (+20), ROI calculator = procurement-stage signal (+12). Company context: MedDevice Corp announced FDA warning letter last month — likely urgent compliance training need. Routing to Marcus (Healthcare vertical SDR) with suggested outreach: Reference the FDA warning letter sensitively, offer complimentary compliance gap assessment, mention 3 similar medical device clients."

---

### Use Case 5: Brand Asset & Creative Production Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training company marketing teams produce enormous volumes of creative assets: course promotional graphics, social media visuals, email templates, presentation decks, brochures, case study PDFs, infographics, video thumbnails, booth graphics, partner co-branded materials, and program-specific collateral. A 10-person marketing team may handle 200+ creative requests per month. Requests come in via email, Slack, verbal asks, and formal briefs (inconsistently). Designers are constantly context-switching between urgent "I need this by EOD" requests and strategic brand projects. Asset versioning is chaotic — three people have different "final" versions of the leadership program brochure. Brand consistency suffers as non-designers create off-brand materials using old templates.

#### The Solution
Build a **monday.com Work Management** Creative Production workflow. Create a Creative Requests board with: Request Title (text), Requester (people), Request Type (dropdown: Social Media Graphic, Email Template, Presentation Deck, Brochure/PDF, Infographic, Video Thumbnail, Event Collateral, Partner Co-Brand, Course Promotional, Ad Creative), Program/Campaign (connect board), Priority (status: Urgent-24hr, High-3 days, Standard-1 week, Low-2 weeks), Brand Guidelines (dropdown: Use Standard Template, Custom Design Required, Partner Co-Brand Template), Dimensions/Specs (text), Copy Provided (checkbox), Status (status: New Request, In Queue, Designing, Internal Review, Revisions, Final Approval, Delivered), Assigned Designer (people), Due Date (date), Revision Count (numbers), Final Asset (file). Use intake **forms** for standardized requests, **automations** for priority-based routing and SLA tracking, and a **Workload view** to balance designer capacity.

#### The Outcome
Reduce average creative turnaround from 5 days to 2 days for standard requests. Eliminate "drive-by" requests — 100% of creative work flows through the standardized intake. Cut revision cycles by 40% with structured briefs. Give marketing leadership visibility into creative team capacity and output.

#### Discovery Questions
1. "How many creative requests does your design team handle per month, and how do those requests come in?"
2. "When a sales rep needs a custom one-pager for a prospect meeting tomorrow, what happens? How often does this occur?"
3. "Where do finalized brand assets live, and how confident are you that everyone is using the latest version?"
4. "How do you prioritize creative requests when everything is 'urgent'?"
5. "Do you have standardized templates that non-designers can use for basic needs, or does everything require a designer?"

#### Industry Context
Training companies face unique creative challenges: they must produce visually distinct materials for potentially hundreds of programs while maintaining overall brand consistency. Each program may have its own visual identity (color palette, imagery style) within the master brand. Course catalog updates require batch asset production (updating 50+ course thumbnails when branding changes). Partner co-branding is common — creating jointly-branded materials for channel partners, corporate clients who want custom-branded training portals, and accreditation bodies. The rise of social-first marketing means the volume of required assets has exploded — a single webinar promotion now needs 10+ social graphics across platforms.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Creative Production Management system with an intake form and main board. Intake form fields: Request Title, Requester Name (auto-fill), Request Type (dropdown: Social Media Graphic Set, Email Template, Presentation Deck, Brochure/PDF, Infographic, Video Thumbnail, Event/Booth Collateral, Partner Co-Brand, Course Promotional Set, Ad Creative Set, Brand Template Update), Related Campaign (connect), Priority (dropdown: Urgent-24hrs, High-3 business days, Standard-1 week, Low-2 weeks), Description & Context (long text), Copy/Text Provided (long text), Dimensions & Specs (text, with helper text showing common sizes), Brand Template (dropdown: Standard Brand, Program-Specific, Partner Co-Brand, Custom), Reference/Inspiration Links (text), Due Date. Board columns: all form fields plus Assigned Designer (people), Status (status: New Request, Queued, In Progress, Internal Review, Revisions Needed, Revision In Progress, Final Approval, Delivered, On Hold), Estimated Hours (numbers), Actual Hours (numbers), Revision Count (numbers), Final Asset (file), Approval (status: Pending, Approved, Rejected). Automations: when form submitted with Priority Urgent, immediately notify design lead and senior designer; when Status changes to Internal Review, notify Requester for feedback with 24-hour deadline; when Revision Count exceeds 2, notify design lead for scope review; when all items assigned to a designer exceed 20 estimated hours for the week, flag capacity issue. Create Kanban view grouped by Status, Workload view by Assigned Designer, and Dashboard: requests by type (pie), average turnaround time (numbers), requests by status (chart), designer workload (workload widget), revision rate (numbers), requests per week trend (chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CreativeOps Agent
**Agent Purpose:** Streamline creative request intake, optimize designer workload, and ensure brand consistency across all assets.

**Triggers:**
- New creative request submitted via form
- Request deadline approaching with status still "Queued" or "In Progress"
- Revision count exceeds 2 on any request
- Weekly schedule for capacity planning report
- New brand guideline update published

**Actions:**
- Validate incoming requests for completeness (flag missing copy, unclear specs, no reference provided)
- Auto-assign to designer based on request type expertise, current workload, and priority
- Detect similar past requests and suggest reusing/adapting existing assets
- Alert design lead when capacity exceeds 120% for any designer
- Generate weekly creative production report: completed, in progress, overdue, revision rates by requester
- When brand guidelines update, flag all active requests for compliance check

**Data Required:**
- Designer expertise profiles and capacity calendars
- Historical creative request data (turnaround times, revision patterns)
- Brand asset library with tagging
- Request intake form submissions
- Campaign calendar for proactive capacity planning

**Autonomy Level:** Human-in-the-Loop
Autonomous for intake validation, assignment, and reporting. Requires designer review for all creative output and design lead approval for priority overrides.

**Example Interaction:**
> A creative request comes in: "Need social media graphics for the new Cybersecurity Awareness Training launch — LinkedIn, Twitter, Instagram, and Facebook sizes. Urgent — launching in 2 days." The CreativeOps Agent checks: "⚠️ Incomplete request: No copy provided, no program-specific visual direction, no campaign board linked. Similar request found: Cybersecurity Fundamentals launch from October — 12 social graphics in brand template. Recommendation: Adapt October assets with updated program name and dates (estimated 2 hours vs. 6 hours for net-new). Auto-populated copy from the program description on the catalog board. Assigned to Jamie (social graphics specialist, current capacity: 75% this week). Jamie — please confirm the adapted approach works before starting from scratch."

---

### Use Case 6: Partner & Channel Marketing Enablement

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Many training companies sell through channel partners — resellers, consulting firms, HR technology vendors, and corporate training aggregators. Partner marketing requires co-branded materials, partner-specific landing pages, joint webinar coordination, MDF (Market Development Fund) tracking, and partner communication campaigns. Marketing teams create these materials manually for each partner, leading to inconsistency and delays. Partners complain they don't have the right materials to sell effectively. MDF spending is tracked in spreadsheets with no visibility into ROI. Partner marketing requests sit in email inboxes for weeks because there's no formal intake process.

#### The Solution
Create a **monday.com Work Management** Partner Marketing Hub. Build boards for: Partner Directory (partner profiles, tier, co-marketing agreement details), Partner Marketing Requests (intake form for co-branded materials, joint campaigns, event support), MDF Tracker (budget allocation, spend tracking, ROI measurement), and Partner Content Library (approved assets by partner tier with version control). Key columns on Partner Marketing Requests: Partner Name (connect to Directory), Request Type (dropdown: Co-Branded Collateral, Joint Webinar, Co-Authored Content, Event Support, Social Campaign, Case Study, Custom Landing Page), Partner Tier (mirror from Directory), MDF Approved (checkbox), Budget (numbers), Status (status), Assigned Marketer (people), Due Date (date). **Automations** route requests based on partner tier (Platinum partners get 24-hour response, Standard gets 1-week SLA).

#### The Outcome
Reduce partner marketing request fulfillment from 2 weeks to 3 days. Achieve 100% MDF utilization tracking with ROI measurement. Increase partner-sourced leads by 30% through better enablement. Standardize co-branding while allowing tier-appropriate customization.

#### Discovery Questions
1. "How many channel partners actively co-market with you, and what percentage of your revenue comes through partners?"
2. "When a partner asks for co-branded materials, what's the process and how long does it take?"
3. "How do you track Market Development Fund allocation and spending? Can you tie MDF spend to partner-sourced pipeline?"
4. "Do partners have self-service access to approved marketing materials, or does every request go through your team?"
5. "What's your biggest partner marketing complaint — and what would fix it?"

#### Industry Context
Training industry channel partnerships are complex: a technology consulting firm might resell training programs, a corporate university might white-label courseware, and an HR tech vendor might integrate training offerings into their platform. Each partner type needs different marketing support. The training industry's shift to digital delivery has enabled global partnerships — a US training company can partner with a UK HR consultancy to deliver compliance training across Europe, but this requires localized marketing materials (language, regulatory context, pricing). Partner-sourced deals in training typically close 20-30% faster than direct because of the trusted advisor relationship.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Partner Marketing Hub with three connected boards. Board 1 — Partner Directory: Partner Name (text), Company (text), Partner Tier (status: Platinum, Gold, Silver, Registered), Partner Type (dropdown: Reseller, Consulting Firm, Technology Vendor, Corporate University, Training Aggregator, Industry Association), Region (dropdown), Primary Contact (people/text), Partner Since (date), Annual Revenue Through Partner (numbers), Co-Marketing Agreement (file), MDF Allocation (numbers), MDF Remaining (formula), Programs Licensed to Sell (tags), Partner Marketing Contact (text). Board 2 — Partner Marketing Requests: Request Title (text), Partner (connect to Board 1), Partner Tier (mirror), Request Type (dropdown: Co-Branded Collateral, Joint Webinar, Co-Authored Blog, Event Support, Social Campaign Kit, Case Study, Custom Landing Page, Email Template, Video, Partner Toolkit Update), MDF Funded (checkbox), Budget (numbers), Description (long text), Brand Assets Provided (file), Status (status: Submitted, Approved, In Production, Partner Review, Revisions, Delivered), Assigned Marketer (people), Due Date (date), SLA Target (formula based on Tier). Board 3 — MDF Tracker: Partner (connect), Activity (text), MDF Amount (numbers), Status (status: Planned, Approved, Spent, Reconciled), Invoice/Receipt (file), Leads Generated (numbers), Pipeline Generated (numbers), ROI (formula). Automations: when Partner Tier is Platinum and request submitted, set SLA to 24 hours and notify senior partner marketer; when MDF Remaining drops below 20%, notify partner manager; when Request Status changes to Partner Review, notify Partner Marketing Contact with 48-hour feedback deadline. Dashboard: requests by partner tier (chart), MDF utilization by partner (table), partner-sourced pipeline (numbers), requests by type (pie), SLA compliance rate (numbers)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PartnerMarketing Agent
**Agent Purpose:** Accelerate partner enablement by automating co-branded material creation, MDF tracking, and partner communication.

**Triggers:**
- New partner marketing request submitted
- Partner tier upgrade or downgrade
- MDF quarterly allocation reset
- Partner inactive for 60+ days (no requests, no leads)
- Monthly schedule for partner marketing performance report

**Actions:**
- Auto-generate co-branded material drafts by merging partner brand assets with pre-approved templates
- Track MDF spend against allocation and forecast quarterly burn rate
- Identify inactive partners and recommend re-engagement campaigns
- Generate monthly partner marketing scorecard: leads generated, pipeline influenced, MDF ROI by partner
- Suggest joint marketing opportunities based on partner expertise alignment with upcoming program launches
- Create partner marketing toolkits for new program launches (co-branded one-pager, email templates, social copy)

**Data Required:**
- Partner brand guidelines and logo files
- Co-marketing agreement terms and MDF allocations
- Partner-sourced lead and pipeline data from CRM
- Program launch calendar
- Partner engagement history (requests, events, content)

**Autonomy Level:** Human-in-the-Loop
Autonomous for MDF tracking, reporting, and toolkit generation from templates. Requires human approval for co-branded materials, partner communications, and MDF allocation changes.

**Example Interaction:**
> The PartnerMarketing Agent notices that TechConsult Partners (Gold tier) hasn't submitted any marketing requests in 75 days, despite having $15,000 in unused MDF allocation for Q1. It also sees that TechConsult's top-selling program (Data Analytics certification) has a major update launching next month. The agent drafts a re-engagement message: "Hi TechConsult team — noticed you have $15K in Q1 MDF available (expires March 31). With the Data Analytics 3.0 certification launching February 28, this is a great opportunity for a joint webinar or targeted email campaign to your client base. We've pre-built a co-branded launch kit (attached draft) that just needs your logo and client list. Want to schedule a 30-minute planning call this week?" It routes this to the partner marketing manager for review and send.

---

### Use Case 7: Marketing Analytics & Attribution Dashboard

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Training company marketing data is scattered across 8-15 tools: Google Analytics for web traffic, HubSpot for email and leads, LinkedIn for social performance, Google Ads for PPC, Zoom for webinar data, CRM for pipeline, the LMS for free trial conversions, and spreadsheets for everything else. Building a marketing performance report requires manually pulling data from each source, reconciling metrics that don't align (HubSpot lead counts don't match CRM), and spending 2-3 days per month on reporting instead of marketing. Attribution is nearly impossible — did that $200K enterprise deal come from the webinar they attended, the whitepaper they downloaded, or the conference where they met the sales rep? Without attribution, marketing can't defend budget requests or optimize spend.

#### The Solution
Build a **monday.com Work Management** Marketing Analytics Hub. Create boards for: Monthly KPI Tracker (key metrics updated weekly/monthly), Campaign Performance (connected to campaign board with results data), Channel Performance (aggregate metrics by marketing channel), and Attribution Tracker (connecting marketing touchpoints to closed deals). Key columns: Channel (dropdown), Monthly Spend (numbers), Leads Generated (numbers), MQLs (numbers), SQLs (numbers), Opportunities (numbers), Revenue Attributed (numbers), Cost Per Lead (formula), Cost Per MQL (formula), CAC (formula), ROI (formula). Use **Dashboards** to create executive-ready marketing scorecards updated in near-real-time. **monday AI** can analyze trends and surface insights.

#### The Outcome
Reduce monthly reporting time from 3 days to 3 hours. Enable real-time marketing performance visibility for leadership. Implement multi-touch attribution showing full buyer journey. Make data-driven budget allocation decisions based on channel ROI.

#### Discovery Questions
1. "How long does it take your team to produce the monthly marketing report? How much of that is manual data gathering?"
2. "If your CEO asked 'What marketing channel drives the most revenue?' — could you answer with confidence?"
3. "How do you decide where to allocate marketing budget? Is it based on historical data, gut feel, or last year's plan?"
4. "When was the last time you killed a marketing program because the data showed it wasn't working? How did you make that decision?"
5. "How do you measure the impact of thought leadership content — is it just vanity metrics (views, shares) or do you track downstream pipeline?"

#### Industry Context
Training industry marketing attribution is particularly challenging because of long, multi-touch buyer journeys. An enterprise L&D buyer might: (1) discover the company through a Google search, (2) download a whitepaper, (3) attend 3 webinars over 2 months, (4) meet the team at a conference, (5) request a demo, (6) go through a 4-month procurement process, and (7) close a $500K annual contract. Traditional first-touch or last-touch attribution vastly misrepresents which marketing activities drove the deal. Training companies also have a unique attribution challenge with free trials — a learner who completes a free course module and then requests enterprise pricing represents a bottom-of-funnel conversion that started as a product-led growth motion.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build me a Marketing Analytics Dashboard Hub with two boards. Board 1 — Channel Performance Tracker (updated monthly): Channel (dropdown: Email Marketing, Organic Social, Paid Social - LinkedIn, Paid Social - Facebook, PPC - Google, PPC - Bing, Webinars, Content/SEO, Events & Conferences, Partner Marketing, Free Trials, Direct/Referral), Month (date), Budget Spent (numbers), Impressions (numbers), Clicks (numbers), CTR (formula), Leads Generated (numbers), Cost Per Lead (formula), MQLs (numbers), SQLs (numbers), MQL-to-SQL Rate (formula), Opportunities Created (numbers), Revenue Attributed (numbers), ROI (formula: Revenue/Spend), Notes (text). Board 2 — Campaign Attribution: Deal Name (connect to CRM), Deal Value (numbers), Close Date (date), First Touch Channel (dropdown), First Touch Date (date), Key Touch Points (tags: Webinar, Whitepaper, Event, Demo, Free Trial, Partner Referral, Blog), Touch Count (numbers), Days First Touch to Close (formula), Primary Attribution Channel (dropdown), Attribution Notes (long text). Dashboard: monthly spend vs revenue (dual-axis chart), leads by channel (stacked bar), cost per lead by channel (bar chart), MQL-to-SQL conversion by channel (chart), top 10 deals with attribution (table), budget allocation vs results (scatter plot), quarterly trend (line chart), channel ROI ranking (table sorted by ROI)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MarketingInsights Agent
**Agent Purpose:** Automate marketing data aggregation, identify performance trends, and recommend budget optimization.

**Triggers:**
- Weekly schedule (Monday AM) for performance snapshot
- Monthly schedule (1st of month) for comprehensive analysis
- Campaign completion (moved to "Complete" status)
- Significant metric deviation (>20% change week-over-week)
- Quarterly schedule for budget reallocation recommendation

**Actions:**
- Aggregate weekly metrics from connected data sources and update Channel Performance board
- Generate weekly performance snapshot: top/bottom performing channels, notable trends, action items
- When a campaign completes, calculate full-funnel metrics and generate performance summary
- Detect anomalies (sudden traffic drops, conversion rate changes, cost spikes) and alert marketing director
- Quarterly budget optimization recommendation based on channel ROI analysis and trend projections
- Map buyer journey touchpoints for closed deals and calculate multi-touch attribution weights

**Data Required:**
- Google Analytics / website data
- Marketing automation platform (HubSpot/Marketo) metrics
- CRM pipeline and closed deal data
- Advertising platform data (Google Ads, LinkedIn Ads)
- Webinar platform attendance and registration data
- Social media analytics

**Autonomy Level:** Human-in-the-Loop
Fully autonomous for data aggregation, trend analysis, and anomaly detection. Requires marketing director review for budget reallocation recommendations and strategic decisions.

**Example Interaction:**
> The MarketingInsights Agent's monthly report reveals: "February Performance Summary: Total spend: $45,200. Total leads: 892 (up 12% MoM). Best performing channel: Webinars (ROI: 8.2x, up from 6.1x — driven by the AI in L&D masterclass series). Underperforming: PPC Google (ROI: 1.3x, down from 2.1x — CPC increased 34% due to competitive bidding on 'compliance training' keywords). Recommendation: Shift $3,000/month from Google PPC compliance keywords to LinkedIn Sponsored Content targeting HR VPs in regulated industries — similar audience, 40% lower CPL based on Q4 test. Also: Free trial channel generated 45 SQLs this month (highest ever) but isn't receiving dedicated marketing budget. Recommend allocating $5,000/month to free trial promotion — estimated 2.5x pipeline increase based on current conversion rates."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| L&D | Learning & Development — corporate function responsible for employee training and skill building |
| LMS | Learning Management System — platform for hosting and delivering training content |
| CEU/CPE | Continuing Education Units / Continuing Professional Education — credits for maintaining professional certifications |
| SCORM | Standard for e-learning content packaging and LMS interoperability |
| Courseware | Packaged training content including modules, assessments, and supporting materials |
| Blended Learning | Training approach combining online/digital delivery with live (virtual or in-person) sessions |
| Microlearning | Short, focused learning modules (typically 3-10 minutes) designed for just-in-time skill building |
| ILT / vILT | Instructor-Led Training / Virtual Instructor-Led Training |
| MDF | Market Development Funds — budget allocated to channel partners for co-marketing activities |
| White-labeling | Customizing training content or platform with a client's branding |
| Learner Journey | The complete path a learner takes from enrollment through completion and certification |
| NPS (Learner) | Net Promoter Score measured from training participants to gauge satisfaction and likelihood to recommend |
| Seat License | Pricing model based on number of learner accounts provisioned in an LMS |
| Content Library | Catalog of available training courses and programs, often organized by topic and skill level |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP of Marketing / CMO | Marketing strategy, budget allocation, brand positioning | Decision-maker |
| Director of Demand Generation | Lead generation, pipeline targets, marketing-sales alignment | Decision-maker / Influencer |
| Content Marketing Manager | Thought leadership, blog, whitepapers, SEO strategy | Influencer / User |
| Digital Marketing Manager | Website, paid media, social, email campaigns | User |
| Event / Webinar Manager | Webinar production, conference participation, event logistics | User |
| Partner Marketing Manager | Channel enablement, co-marketing, MDF management | User |
| Marketing Operations / Analyst | Marketing tech stack, analytics, reporting, automation | Influencer / User |
| Creative Director / Designer | Brand guidelines, visual content, design production | User |
| VP of Sales | Pipeline expectations, lead quality feedback, marketing-sales SLA | Influencer |
| Chief Learning Officer | Content direction, program strategy, brand authenticity | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales | Lead handoff, pipeline reporting, sales enablement | CRM integration for closed-loop attribution and lead management |
| Product & R&D | Program launches, feature marketing, product-led growth | Connected boards for launch coordination and free trial optimization |
| Operations | Client success stories, delivery quality metrics for testimonials | Shared boards for case study pipeline and reference management |
| Customer Success | Renewal marketing, upsell campaigns, NPS for testimonials | Connected data for customer marketing and expansion campaigns |
| HR | Employer brand, recruitment marketing, internal training promotion | Shared content calendar and employer brand asset management |
| IT | Marketing tech stack management, website infrastructure, data integrations | Software license management and analytics data pipeline |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| HubSpot | All-in-one marketing platform (MAP + CMS + CRM) | monday.com complements or replaces HubSpot's project management gaps. For companies without HubSpot, monday CRM + Work Management provides unified marketing operations without MAP lock-in |
| Asana | Marketing team project management | Asana lacks CRM, intake forms with the same depth, and cross-department visibility. monday.com unifies marketing ops with sales pipeline and company-wide workflows |
| Wrike | Creative and marketing work management | Similar positioning but monday.com offers superior CRM integration, more intuitive UI, and broader platform (Service, Dev) for cross-functional use cases |
| Trello | Simple kanban for marketing tasks | Trello doesn't scale — no automations, no dashboards, no formulas. monday.com handles the complexity of multi-campaign, multi-channel marketing operations |
| Airtable | Flexible database for marketing tracking | Powerful but requires significant setup and technical skill. monday.com provides purpose-built marketing templates with no-code automation |
| Notion | Content planning and documentation | Great for wikis, poor for workflow automation. No native automations, dashboards, or CRM capabilities |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use HubSpot for everything" | "HubSpot is excellent for email automation and lead nurturing, but how are you managing the operational side — campaign coordination, creative production, content pipeline, event logistics? Most marketing teams use HubSpot for execution but need a work management layer above it for planning and coordination. monday.com integrates natively with HubSpot." |
| "We need a dedicated marketing project management tool" | "That's exactly what this is — but unlike standalone PM tools, monday.com also connects to your CRM pipeline, gives leadership cross-department visibility, and scales across your entire organization. You're not buying a marketing tool — you're buying a platform that starts with marketing and grows." |
| "Our team is too small for another tool" | "A 10-person marketing team running 30+ campaigns across 5 channels is exactly who benefits most. The automation alone — routing creative requests, triggering campaign checklists, alerting on deadlines — replaces the coordination overhead that's eating your team's strategic time." |
| "We can't prove marketing ROI anyway" | "That's the problem we're solving. By connecting your campaign board to your pipeline board, every deal traces back to marketing touchpoints. You'll walk into budget conversations with data, not guesses. And yes, the multi-touch attribution is built in." |
| "Switching costs are too high" | "Start with one use case — campaign management or content pipeline — and prove value in 2 weeks. Import your existing data, connect your current tools via integrations, and run the new system alongside the old for a month. Low risk, high upside." |

## Proof Points
*(To be populated with customer references)*
- [Training company marketing team efficiency case study]
- [Campaign management consolidation success story]
- [Marketing-sales alignment improvement metrics]
- [Partner marketing enablement ROI example]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
