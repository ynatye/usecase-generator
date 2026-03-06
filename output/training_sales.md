# Training × Sales Playbook

## Overview

Sales teams in training companies are responsible for selling learning programs, courseware licenses, certification packages, and custom training engagements to corporate buyers, government agencies, educational institutions, and individual learners. Unlike SaaS sales where the product is self-evident, training sales requires consultative selling — understanding the buyer's skill gaps, compliance requirements, workforce development goals, and preferred delivery modalities before proposing a solution. The sales cycle ranges from 2 weeks (catalog course licenses) to 6-12 months (enterprise custom training partnerships worth $500K-$5M+).

Training company sales teams typically range from 5-50+ reps depending on the organization's size and market focus. They're segmented by territory, vertical (healthcare, financial services, manufacturing, tech), deal size (SMB vs. enterprise), or channel (direct vs. partner/reseller). Key roles include Account Executives (AEs), Business Development Representatives (BDRs), Solution Architects (who customize training proposals), and Channel/Partner Managers. The sales process is heavily proposal-driven: RFPs (Requests for Proposal) are common in government and large enterprise deals, requiring detailed scope documents, pricing models (per-seat, per-course, enterprise license, subscription), and compliance attestations.

The competitive landscape is fierce — training companies compete against internal L&D departments ("build vs. buy"), other training vendors, eLearning marketplaces (Udemy Business, Coursera for Business, LinkedIn Learning), and increasingly, AI-generated content. Differentiation comes from industry expertise, accreditation/certification authority, customization capability, delivery flexibility, and measurable learning outcomes. Sales teams that can articulate ROI (reduced time-to-competency, compliance risk reduction, employee retention) win over those selling on features alone.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Training sales teams need to handle growing pipeline complexity (more products, modalities, verticals) without proportional headcount growth — especially proposal generation and pipeline management |
| 2 | Replace or Radically Augment Headcount | Medium-High | AI can draft proposals, RFP responses, ROI calculators, and follow-up sequences — tasks consuming 30-40% of AE time |
| 3 | Consolidate Tech Stack with AI | Medium | Replacing disconnected CRM, proposal tools, CPQ, and spreadsheet pricing with a unified system eliminates errors and accelerates deal velocity |

## Prioritized Use Cases

---

### Use Case 1: Training Sales Pipeline & Deal Management (CRM)

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies often outgrow their CRM or never properly implement one. Deals are tracked in spreadsheets, email threads, and the sales manager's memory. The complexity is unique to training: a single deal might involve multiple courses, multiple delivery modalities (ILT + eLearning bundle), custom content development, ongoing subscription licensing, and multi-year renewal terms. Generic CRMs (even Salesforce) require heavy customization to capture training-specific deal attributes like seat counts by course, delivery schedules, accreditation requirements, and trainer availability. Without a purpose-fit system, forecasting is unreliable, deal handoffs to delivery are messy, and renewals fall through the cracks.

#### The Solution
monday.com **CRM** configured for training sales. Each deal is an item with training-specific columns: courses included (connected to the product catalog board), total seat count, delivery modality mix, custom content scope, contract type (one-time, subscription, multi-year), accreditation requirements, and estimated delivery dates. **Sales pipeline views** (Kanban by stage: Prospect → Discovery → Proposal → Negotiation → Closed Won/Lost) provide visual pipeline management. **Automations** trigger proposal creation when a deal moves to "Proposal" stage, schedule follow-ups based on deal stage duration, and alert renewal managers 90 days before contract expiration. **Dashboards** display pipeline value by stage, win rate by vertical, average deal cycle by product type, and rep performance metrics. **Sub-items** track individual line items within complex deals.

#### The Outcome
- 100% pipeline visibility — no more deals tracked in spreadsheets or email
- 20-30% improvement in forecast accuracy through structured deal tracking
- 15% faster deal cycles through automated follow-ups and stage-based workflows
- Zero missed renewals — automated alerts 90/60/30 days before expiration
- Clean handoff to delivery team with all deal details in one place

#### Discovery Questions
1. "Walk me through a typical deal from first contact to signed contract — how many tools does that touch?"
2. "How accurate was your last quarter's sales forecast? What caused the variance?"
3. "When a deal closes, how does the delivery team learn what was sold? How often are there misunderstandings?"
4. "What percentage of your revenue comes from renewals, and how do you track renewal dates today?"
5. "Can you tell me right now your total pipeline value by vertical? How long would it take to pull that number?"

#### Industry Context
Training sales deals are uniquely complex because they bundle **products** (courses), **services** (customization, facilitation), **technology** (LMS access), and **ongoing support** (content updates, help desk). Pricing models include: **per-seat** (most common for catalog courses), **per-course license** (flat fee for unlimited seats within a company), **subscription** (annual access to a catalog), **custom development** (project-based pricing), and **enterprise agreements** (multi-year, multi-product bundles). **Seat utilization** is a key metric — if a client buys 500 seats but only 200 are used, renewal is at risk. Government deals often require **GSA Schedule** pricing or response to formal **RFPs** through platforms like SAM.gov.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Training Sales CRM on monday.com. Board 1 — Deals Pipeline: Columns: Deal Name (text), Company Name (text), Primary Contact (text), Contact Email (email), Contact Phone (phone), Vertical (dropdown: Healthcare, Financial Services, Manufacturing, Technology, Government, Education, Retail, Energy, Professional Services, Other), Deal Stage (status: New Lead, Qualification, Discovery, Proposal Sent, Negotiation, Legal Review, Closed Won, Closed Lost, On Hold), Deal Type (dropdown: Catalog License, Custom Development, Enterprise Agreement, Subscription, Blended Bundle, Government RFP), Total Deal Value (numbers), Annual Recurring Value (numbers), Number of Seats (numbers), Courses Included (connect to Product Catalog board), Delivery Modality (dropdown: eLearning Only, ILT Only, VILT Only, Blended, Full Catalog Access), Custom Content Required (checkbox), Custom Content Scope (long text), Contract Term (dropdown: One-Time, 1 Year, 2 Year, 3 Year), Contract Start Date (date), Contract End Date (date), Renewal Date (date), Assigned AE (people), BDR Source (people), Deal Source (dropdown: Inbound, Outbound, Referral, Partner, RFP, Event, Website), Close Probability (numbers), Expected Close Date (date), Competitors (text), Loss Reason (dropdown: Price, Competitor, Internal Build, No Budget, Timing, No Decision), Notes (long text). Add sub-items for individual line items: Course Name, Seats, Unit Price, Total, Delivery Date. Automations: when Deal Stage changes to Proposal Sent, create proposal item on Proposals board and notify AE; when Deal Stage is Negotiation for more than 14 days, notify sales manager; when Deal Stage changes to Closed Won, create delivery project on Delivery board, notify delivery team, and move to Won archive group; when Renewal Date is 90 days away, create renewal opportunity and notify Account Manager; when Deal Stage changes to Closed Lost, require Loss Reason before saving. Views: Kanban by Deal Stage, Chart view of pipeline value by stage, Table filtered by My Deals (current user). Dashboard: total pipeline value (number), deals by stage (funnel chart), pipeline by vertical (stacked bar), average deal size trend (line chart), win rate by deal type (chart), rep leaderboard by revenue closed (leaderboard), deals closing this month (filtered table), renewal pipeline next 90 days (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DealPilot
**Agent Purpose:** Monitor deal health, predict at-risk deals, automate follow-ups, and ensure no opportunity falls through the cracks.

**Triggers:**
- Deal stage unchanged for longer than stage-specific threshold (Discovery: 10 days, Proposal: 7 days, Negotiation: 14 days)
- Expected close date passes without stage change
- New lead created (from form, integration, or manual entry)
- Weekly schedule (Monday 7 AM) for pipeline health review
- Renewal date approaching (90, 60, 30 days)

**Actions:**
- Send personalized follow-up email drafts to AE based on deal stage and last activity
- Score deal health based on: stage velocity, engagement signals, deal size vs. historical win rates, and competitor presence
- Generate weekly pipeline review summary for sales manager: new deals, stalled deals, at-risk deals, deals expected to close this week
- Create renewal opportunity 90 days before expiration with pre-populated details from original deal
- When a deal is marked Closed Lost, analyze loss reason patterns and generate monthly win/loss report
- For stalled deals, suggest next best action: "Deal has been in Negotiation 18 days. Similar deals that stalled here had 60% higher close rate when AE offered a pilot program. Recommend proposing a 30-seat pilot."

**Data Required:**
- Deals Pipeline board (all deal data)
- Activity/communication log (emails, calls, meetings)
- Historical win/loss data for pattern analysis
- Product catalog with pricing
- Competitor intelligence

**Autonomy Level:** Human-in-the-Loop
DealPilot drafts follow-ups and recommendations but AEs decide when to send. Renewal opportunity creation is automatic. Pipeline reports are fully autonomous. Deal health scoring is informational — it doesn't change deal stages or assignments without human approval.

**Example Interaction:**
> DealPilot flags a deal in Monday's pipeline review: "⚠️ **At-Risk Deal: 'National Healthcare Corp — Compliance Training Bundle' ($380K, 2-year).** Stage: Negotiation (Day 22 — threshold is 14 days). Last activity: email from AE to procurement on Feb 3, no response. Risk factors: 1) Legal review not yet started despite procurement engagement, 2) Competitor Skillsoft identified in discovery notes, 3) Budget cycle ends March 31 — only 40 days remaining. **Recommended actions:** 1) AE to call VP of L&D directly (bypass procurement delay), 2) Offer early-sign incentive: 10% discount if contract signed by March 15, 3) Send case study from similar healthcare organization (Memorial Health Systems — 94% compliance rate improvement). Draft follow-up email attached."

---

### Use Case 2: Proposal & RFP Response Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Training companies spend enormous time on proposals and RFP responses. A typical enterprise proposal takes 15-25 hours to create: scoping the training program, selecting appropriate courses, defining customization requirements, building a delivery schedule, creating a pricing model, writing the executive summary, and assembling compliance documentation. For government RFPs, the effort balloons to 40-80+ hours with strict formatting requirements, mandatory attachments, and evaluation criteria matrices. Most of this content is repetitive — 60-70% of any proposal uses standard language, course descriptions, company qualifications, and case studies. Yet each proposal is rebuilt from scratch because there's no centralized content library or templatized workflow.

#### The Solution
monday.com **Work Management** for proposal workflow combined with **monday Docs** and **AI** for content generation. A **Proposal Tracker board** manages every active proposal: deal connected, due date, assigned writer, review stages (draft → internal review → executive approval → client delivery), and status. **monday Docs** house the proposal with AI-assisted content generation — pulling standard sections from a content library, generating customized executive summaries based on deal data, and drafting ROI projections from industry benchmarks. **Automations** create proposal items when deals move to "Proposal" stage, assign reviewers based on vertical expertise, and track revision cycles. A **Content Library board** stores reusable components: company overviews, course descriptions, case studies, compliance statements, and bio templates.

#### The Outcome
- 50-60% reduction in proposal creation time (from 20+ hours to 8-10 hours)
- 3× more proposals delivered per month without additional headcount
- Consistent proposal quality — every proposal includes the right case studies, compliance language, and pricing structure
- 15-20% improvement in proposal win rate through better personalization and faster turnaround

#### Discovery Questions
1. "How many proposals or RFP responses does your team produce per month, and what's the average time per proposal?"
2. "Do you have a centralized library of reusable proposal content, or does each rep start from scratch?"
3. "How often do you miss RFP deadlines or submit lower-quality proposals because of time pressure?"
4. "What's your current proposal win rate, and how does it vary between rushed vs. well-crafted proposals?"
5. "Who reviews proposals before they go out, and how long does the review cycle take?"

#### Industry Context
Training company proposals must address: **needs analysis** (how the vendor will assess skill gaps), **curriculum design** (course selection and customization approach), **delivery plan** (schedule, modality, trainer assignments), **evaluation methodology** (Kirkpatrick levels, ROI measurement), **pricing** (often complex with per-seat, development fees, and ongoing costs), and **qualifications** (certifications, insurance, past performance). Government RFPs follow strict structures: **Technical Volume**, **Management Volume**, **Past Performance Volume**, **Cost Volume**. Evaluation criteria are weighted (e.g., Technical 40%, Cost 30%, Past Performance 30%). **LPTA** (Lowest Price Technically Acceptable) vs. **Best Value** procurement methods change the proposal strategy entirely.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Proposal Management system for a training sales team. Board 1 — Active Proposals: Columns: Proposal Name (text), Connected Deal (connect to Deals Pipeline), Client Company (mirror from deal), Proposal Type (dropdown: Standard Proposal, Government RFP, RFI Response, Custom Development Scope, Renewal Proposal, Partner Proposal), Due Date (date), Assigned Writer (people), Subject Matter Reviewer (people), Executive Approver (people), Proposal Status (status: Not Started, Gathering Info, Drafting, Internal Review, Revisions, Executive Approval, Final QA, Submitted, Won, Lost), Draft Link (link to monday Doc), Version (numbers), Total Proposed Value (numbers), Courses Included (numbers), Custom Content Pages (numbers), Estimated Hours to Complete (numbers), Actual Hours (numbers), Submission Method (dropdown: Email, Portal Upload, Physical Mail, Online Platform), Win/Loss Result (status: Pending, Won, Lost, No Decision), Debrief Notes (long text). Board 2 — Content Library: Columns: Content Block Name (text), Category (dropdown: Company Overview, Course Description, Case Study, Compliance Statement, Team Bio, Methodology, Evaluation Framework, Technology Overview, Pricing Template, Terms & Conditions), Industry Applicability (tags: Healthcare, Finance, Government, Manufacturing, Technology, All), Last Updated (date), Content (long text or Doc link), Owner (people), Usage Count (numbers). Automations: when Deal Stage changes to Proposal Sent on Deals board, create Proposal item on Active Proposals with pre-filled client info; when Proposal Status changes to Internal Review, notify Subject Matter Reviewer with due date 2 days out; when Proposal Status changes to Executive Approval, notify Executive Approver; when Due Date is 3 days away and status is before Final QA, escalate to sales manager; when Win/Loss Result is set, update connected deal stage. Dashboard: active proposals (number), proposals by status (Kanban), average time to complete (number), win rate by proposal type (chart), proposals due this week (table), writer workload (battery), content library usage (top blocks by usage count)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProposalForge
**Agent Purpose:** Accelerate proposal creation by auto-generating first drafts from deal data, content library, and industry-specific templates.

**Triggers:**
- New proposal item created on Active Proposals board
- Writer requests "Generate Draft" via button column
- RFP document uploaded (PDF/Word) to proposal item
- Content Library block updated (triggers refresh of proposals using that block)
- Deal data changes that affect an in-progress proposal

**Actions:**
- Parse RFP documents and extract: requirements list, evaluation criteria, mandatory sections, page limits, and submission instructions — create checklist sub-items for each requirement
- Generate first-draft proposal by assembling relevant Content Library blocks, customized with deal-specific data (company name, seat count, courses, pricing)
- Write customized executive summary based on: client's industry challenges (from discovery notes), proposed solution, expected outcomes, and ROI projection
- Generate ROI calculation based on industry benchmarks: "For a [500-person] healthcare organization, monday.com projects [X]% reduction in compliance training costs and [Y] hours saved annually based on similar implementations"
- Identify content gaps: "This RFP requires a Cybersecurity certification reference — no matching case study found in Content Library. Flagging for manual input."
- Format final proposal per submission requirements (page limits, section numbering, required attachments checklist)

**Data Required:**
- Active Proposals board (deal data, requirements)
- Content Library board (all reusable blocks)
- Deals Pipeline (discovery notes, client details)
- Industry benchmark data for ROI calculations
- Historical proposal win/loss data for optimization
- RFP document (when applicable)

**Autonomy Level:** Human-in-the-Loop
ProposalForge generates drafts and recommendations but never submits proposals without human review. All generated content is marked "AI Draft" until writer approves. RFP parsing is fully automated. ROI calculations include assumptions that must be reviewed. Executive summaries require AE validation of key claims.

**Example Interaction:**
> An RFP arrives from the Department of Veterans Affairs for a comprehensive cybersecurity awareness training program. ProposalForge parses the 47-page RFP document in minutes and creates: "📄 **RFP Analysis Complete — VA Cybersecurity Training.** Extracted 23 mandatory requirements, 8 evaluation criteria (Technical: 45%, Past Performance: 30%, Cost: 25% — Best Value procurement). Key requirements: 1) SCORM-compliant eLearning for 180,000 employees, 2) FedRAMP-authorized LMS hosting, 3) Quarterly content updates for 3 years, 4) Section 508 accessibility compliance, 5) CUI handling certification. **Content Library matches:** Company Overview (DoD version) ✅, Cybersecurity course descriptions ✅, Section 508 compliance statement ✅, FedRAMP documentation ❌ (NEED: verify current authorization status), Past Performance (VA Medical Center training contract 2024) ✅, CUI handling policy ❌ (NEED: create new). **Draft generated:** 34 of 47 required sections populated. 2 sections need manual input. Estimated completion from this point: 12 hours (vs. estimated 65 hours from scratch)."

---

### Use Case 3: Training Product Catalog & CPQ (Configure-Price-Quote)

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Training companies have complex product catalogs — dozens to hundreds of courses, each available in multiple modalities, seat-count tiers, customization levels, and bundling options. Pricing varies by: volume (seat-count breaks), contract term (1-year vs. multi-year discounts), delivery modality (ILT costs more than eLearning), customization scope, and customer segment (government vs. commercial). Reps currently price deals using outdated spreadsheets, tribal knowledge, or by asking the finance team — introducing errors, inconsistency, and delays. A "simple" quote for a 10-course blended bundle with customization can take 2-3 days to produce. Discount approvals are informal (Slack messages to the VP of Sales), leading to margin erosion with no audit trail.

#### The Solution
monday.com as an integrated **Product Catalog + CPQ system**. A **Product Catalog board** lists every course/program with: standard pricing by modality, seat-count tier breaks, minimum order quantities, customization pricing formulas, and available bundles. When an AE builds a deal, they connect courses from the catalog to the deal item. **Formula columns** auto-calculate deal value based on seats × pricing tier, apply bundle discounts, and add customization line items. A **Quote Generator** (via monday Docs template or Vibe-built app) produces client-ready quotes. **Approval automations** route discounts exceeding thresholds (e.g., >15% requires Director approval, >25% requires VP approval) through a structured workflow. **Dashboards** track discount trends, average deal margins, and pricing exception frequency.

#### The Outcome
- Quote generation reduced from 2-3 days to 30 minutes
- Pricing consistency across all reps — no more "gut feel" discounting
- Structured discount approval with full audit trail
- 5-8% margin improvement through elimination of unnecessary discounting
- Reps spend time selling, not calculating prices

#### Discovery Questions
1. "How do your reps currently determine pricing for a complex, multi-course deal?"
2. "How consistent is pricing across your sales team? Would two reps quote the same deal differently?"
3. "What's your discount approval process today? Is there an audit trail?"
4. "How long does it take to generate a client-ready quote, and how often do quotes contain errors?"
5. "Do you know your average deal margin? Has it been trending up or down?"

#### Industry Context
Training pricing models include: **Per-Seat licensing** ($50-500/seat depending on content depth and accreditation), **Enterprise licenses** (unlimited seats for $50K-500K+/year), **Development fees** ($15,000-100,000+ for custom content), **Subscription/catalog access** ($100-300/user/year for catalog libraries), and **Facilitation fees** ($2,000-5,000/day for instructor-led delivery). **Bundling** is strategic — packaging eLearning + ILT + certification often yields 20-30% higher deal values than à la carte. **GSA Schedule pricing** for government contracts requires strict adherence to published price lists with Most Favored Customer protections.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Product Catalog & Quoting system for a training company. Board 1 — Product Catalog: Columns: Course/Program Name (text), Course Code (text), Category (dropdown: Compliance, Technical, Leadership, Safety, Sales Enablement, Professional Development, Custom), Available Modalities (tags: eLearning, ILT, VILT, Blended, Micro-learning), eLearning Price Per Seat (numbers), ILT Price Per Seat (numbers), VILT Price Per Seat (numbers), Blended Price Per Seat (numbers), Tier 1 Break (numbers, seats ≥50: 10% off), Tier 2 Break (numbers, seats ≥200: 20% off), Tier 3 Break (numbers, seats ≥500: 30% off), Custom Development Add-On (numbers, per hour), Minimum Seats (numbers), Accreditation (tags: CPE, CE, SHRM, PMI, CompTIA, OSHA, None), Duration Hours (numbers), Languages Available (tags), Active (checkbox), Description (long text). Board 2 — Quotes: Columns: Quote Number (auto-number with prefix Q-), Connected Deal (connect to Deals Pipeline), Client Name (mirror), Prepared By (people), Quote Date (date), Valid Until (date), Line Items (connect to Product Catalog, multiple), Total List Price (formula), Discount % (numbers), Discount Reason (dropdown: Volume, Multi-Year, Strategic Account, Competitive, Bundle, Partner), Discount Approval Status (status: Not Needed, Pending Approval, Approved, Rejected), Approver (people), Final Quote Price (formula: Total List Price × (1 - Discount%)), Contract Term (dropdown: One-Time, 1 Year, 2 Year, 3 Year), Multi-Year Discount (formula: 5% for 2yr, 10% for 3yr), Payment Terms (dropdown: Net 30, Net 45, Net 60, Quarterly, Annual Upfront), Quote Status (status: Draft, Pending Approval, Approved, Sent to Client, Accepted, Expired, Revised), Quote Document (file). Sub-items for line items: Course Name, Modality, Seats, Unit Price, Tier Discount, Line Total, Custom Scope Notes. Automations: when Discount % exceeds 15, set Approval Status to Pending and notify Sales Director; when Discount % exceeds 25, notify VP Sales; when Quote Status changes to Approved, generate PDF quote (or notify AE to send); when Valid Until date passes and status is Sent to Client, notify AE to follow up or extend; when Quote is Accepted, update Deal Stage to Closed Won. Dashboard: quotes in pipeline (number), average discount % trend (line chart), quotes by status (pie chart), average deal margin (number), top courses quoted (bar chart), approval queue (table filtered by Pending), quote-to-close conversion rate (number)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** QuoteWizard
**Agent Purpose:** Auto-generate optimized quotes based on deal requirements, suggest upsell bundles, and enforce pricing governance.

**Triggers:**
- AE requests quote generation from deal item (button click)
- Deal moves to "Proposal" stage and no quote exists
- Client requests pricing modification on existing quote
- Quarterly trigger: refresh catalog pricing and update active quotes

**Actions:**
- Analyze deal requirements (courses, seats, modality, term) and auto-generate quote with optimal pricing tier applied
- Suggest upsell opportunities: "Client is buying 3 compliance courses separately. Bundling with the Compliance Suite saves them 15% and increases deal value by $12K — plus adds stickiness with 2 additional courses."
- Calculate and present multi-year scenarios: "1-Year: $180K | 2-Year: $342K (5% savings) | 3-Year: $486K (10% savings + priority support included)"
- Flag pricing anomalies: "This quote's per-seat price is 22% below your average for Healthcare Compliance courses. Historical data shows similar deals closed at $285/seat. Consider adjusting."
- Route discount approvals with context: "AE requesting 20% discount on $240K deal. Justification: competitive pressure from Skillsoft. Historical win rate at this discount level: 78%. At standard pricing: 45% win rate. Margin impact: -$48K. Recommendation: approve with 18% counter-offer."
- Track quote expiration and auto-generate renewal quotes for expiring contracts

**Data Required:**
- Product Catalog board (pricing, tiers, bundles)
- Deals Pipeline (requirements, competitor info)
- Historical pricing data (win rates by discount level)
- Quote history (for pattern analysis)
- Margin and cost data from finance

**Autonomy Level:** Human-in-the-Loop
Quote generation and bundle suggestions are automatic but AE reviews before sending. Discount approvals follow the structured workflow — the agent provides recommendations but humans approve. Pricing anomaly flags are informational. Catalog price updates require finance approval.

**Example Interaction:**
> An AE clicks "Generate Quote" on a deal for Meridian Manufacturing — 400 seats across 5 safety training courses (OSHA Compliance, Lockout/Tagout, Hazmat Handling, Confined Spaces, Fall Protection), blended delivery, 2-year term. QuoteWizard generates: "📋 **Quote Q-2847 — Meridian Manufacturing.** Tier 2 pricing applied (200+ seats = 20% discount). Blended modality includes 2 ILT days per course (10 total) + eLearning access. **Line items:** OSHA Compliance (400 seats × $180 = $72,000)... **Subtotal: $324,000.** Multi-year discount (2-year, 5%): -$16,200. **Total: $307,800 ($384.75/seat/year).** 💡 **Upsell Recommendation:** Meridian's manufacturing vertical typically purchases 'Workplace Ergonomics' and 'Emergency Response' within 12 months of initial safety purchase (68% attach rate among similar accounts). Adding these 2 courses now at bundled pricing would be $412,650 total (vs. $478,800 if purchased separately later) — saves the client $66K and increases your deal by 34%. Shall I generate the expanded quote?"

---

### Use Case 4: Sales Enablement & Competitive Intelligence Hub

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training sales reps need deep knowledge across dozens of industries, hundreds of courses, and a constantly shifting competitive landscape. New hires take 6-9 months to reach full productivity because the information is scattered: product details in the LMS, competitive intel in someone's Google Drive, case studies in marketing's folder, and pricing in a spreadsheet. Even tenured reps struggle to keep up when new courses launch, pricing changes, or a competitor introduces a new offering. When a rep walks into a discovery call with a pharmaceutical company and doesn't know the difference between GxP and GMP training requirements, they lose credibility instantly. The training sales manager spends 10+ hours/week answering the same questions from different reps.

#### The Solution
monday.com as a **Sales Enablement Hub** — a centralized, searchable knowledge base connected to the sales pipeline. A **Competitive Intelligence board** tracks competitors (Skillsoft, LinkedIn Learning, Coursera, GP Strategies, etc.) with positioning, pricing, strengths, weaknesses, and displacement strategies. A **Sales Playbook board** organizes by vertical: key challenges, relevant courses, discovery questions, objection handlers, and case studies. **monday Docs** host detailed battle cards that are linked to deal items by vertical. **AI Sidekick** allows reps to query the knowledge base: "What do I need to know about selling compliance training to healthcare companies?" Automations keep content fresh — when a competitor's pricing changes or a new course launches, relevant boards and docs are flagged for update.

#### The Outcome
- New rep ramp time reduced from 6-9 months to 3-4 months
- 10+ hours/week saved for sales managers (fewer repetitive questions)
- Reps enter discovery calls with industry-specific credibility
- Competitive win rate improves 10-15% through better positioning

#### Discovery Questions
1. "How long does it take a new sales rep to become fully productive? What's the biggest barrier?"
2. "Where does your competitive intelligence live today? Can any rep access it quickly before a call?"
3. "How do you ensure reps are up-to-date when new courses launch or pricing changes?"
4. "What's the cost of a rep walking into a meeting unprepared for the client's industry?"
5. "How often does your team lose deals because a competitor positioned better — not because their product was better?"

#### Industry Context
Key competitors in the training market: **Skillsoft/Percipio** (large eLearning library, enterprise focus), **LinkedIn Learning** (breadth play, integrated with LinkedIn), **Coursera for Business/Coursera for Government** (university-branded content, credentials), **Udemy Business** (marketplace model, broad but variable quality), **GP Strategies** (custom training, government/defense), **NIIT** (IT and enterprise training), **Infopro Learning** (managed learning services). Differentiation often comes down to: **depth vs. breadth** (specialist vs. generalist), **customization capability**, **accreditation authority**, **delivery flexibility**, and **measurable outcomes**.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Sales Enablement Hub for a training company. Board 1 — Competitive Intelligence: Columns: Competitor Name (text), Website (link), Market Position (dropdown: Direct Competitor, Adjacent, Emerging Threat, Partner-Competitor), Primary Verticals (tags: Healthcare, Finance, Government, Manufacturing, Technology, Education, All), Product Type (tags: eLearning Library, Custom Training, Managed Learning, Certification, Blended), Pricing Model (text), Estimated Price Range (text), Key Strengths (long text), Key Weaknesses (long text), Displacement Strategy (long text), Recent News (long text), Last Updated (date), Owner (people), Threat Level (status: High, Medium, Low), Win Rate Against (numbers, percentage). Board 2 — Sales Playbooks by Vertical: Columns: Vertical Name (text), Industry Overview (long text), Key Challenges (long text), Relevant Courses (connect to Product Catalog), Discovery Questions (long text), Common Objections & Responses (long text), Case Studies (connect to Case Study board), Regulatory Context (long text), Key Buyer Personas (long text), Competitive Positioning (long text), Last Updated (date), Owner (people). Board 3 — Case Studies: Columns: Case Study Name (text), Client Industry (dropdown), Client Size (dropdown: SMB, Mid-Market, Enterprise, Government), Courses/Solutions Used (tags), Results/Metrics (long text), Quote/Testimonial (long text), Document Link (link), Approved for External Use (checkbox), Date Published (date). Automations: when a deal is Closed Won with a new vertical, notify playbook owner to update with new reference; when Competitive Intelligence Last Updated is older than 30 days, remind Owner to refresh; when new course is added to Product Catalog, notify all Playbook Owners to check relevance. Dashboard: competitive landscape overview (table sorted by Threat Level), playbook freshness (table showing Last Updated with conditional coloring), case study coverage by vertical (chart), most-referenced competitors in lost deals (chart), enablement content usage stats."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SalesCoach
**Agent Purpose:** Provide real-time competitive and industry intelligence to reps before calls, and continuously update the enablement hub with market insights.

**Triggers:**
- AE has a meeting scheduled (calendar integration) with a prospect in a specific vertical
- Deal moves to Discovery stage (prep needed)
- Competitor mentioned in deal notes or loss reason
- Weekly schedule: scan industry news for competitive intelligence updates
- New rep onboarded (trigger 30-day enablement sequence)

**Actions:**
- Generate pre-call briefing 1 hour before scheduled meeting: client industry context, relevant courses, competitive positioning (if competitor known), suggested discovery questions, and relevant case studies
- When competitor is identified in a deal, auto-generate battle card: side-by-side comparison, displacement talking points, and historical win/loss data against that competitor
- Scan industry news weekly and update Competitive Intelligence board with pricing changes, product launches, acquisitions, and leadership changes
- For new reps, generate daily "Learn This Today" micro-briefings covering one vertical or product per day for the first 30 days
- Analyze win/loss patterns and update playbooks: "Healthcare deals where we led with compliance ROI had a 67% win rate vs. 41% when we led with technology features. Updating Healthcare Playbook discovery sequence."

**Data Required:**
- Competitive Intelligence board
- Sales Playbooks board
- Case Studies board
- Deals Pipeline (meeting schedules, deal notes, win/loss data)
- Calendar integration (upcoming meetings)
- Industry news feeds (RSS, Google Alerts)
- Product Catalog (for course recommendations)

**Autonomy Level:** Fully Autonomous (for research and briefings) / Human-in-the-Loop (for playbook updates)
Pre-call briefings and competitive news scanning are fully automated. Playbook content updates are generated as recommendations — the playbook owner reviews and approves. Battle cards are auto-generated but flagged for review if based on limited data (<5 competitive encounters).

**Example Interaction:**
> At 8 AM, SalesCoach sends AE Jamie a pre-call briefing: "📞 **Pre-Call Brief — 9:00 AM with Apex Financial Group.** **Industry:** Financial Services (Banking Division, 8,000 employees). **Context:** Post-2025 SEC cybersecurity disclosure rules are driving increased demand for security awareness training in banking. Apex recently reported a $2.3M fine for BSA/AML training deficiencies (public record, Jan 2026). **Recommended lead:** Compliance cost reduction — our AML training program reduced similar fines by 89% at [Case Study: Pacific National Bank]. **Competitor alert:** Apex currently uses KnowBe4 for security awareness. Displacement strategy: KnowBe4 is strong on phishing simulation but weak on regulatory compliance training (AML, BSA, GLBA). Position our breadth: security awareness + regulatory compliance in one platform vs. two vendors. **Discovery questions:** 1) 'After the BSA fine, how has your compliance training program changed?' 2) 'Are your security awareness and regulatory compliance training programs managed by the same team or different teams?' 3) 'What's the cost of maintaining two separate training vendors vs. consolidating?' **Relevant courses:** AML Fundamentals, BSA Compliance Suite, Cybersecurity Awareness for Financial Services, GLBA Privacy Training."

---

### Use Case 5: Partner & Reseller Channel Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Many training companies sell through partners: consulting firms that bundle training with transformation projects, technology vendors that include training with product sales, industry associations that offer training to members, and regional resellers that sell into markets the training company doesn't cover directly. Managing this channel is chaotic — partner deal registration happens via email, there's no visibility into the partner pipeline, co-marketing activities are tracked informally, and commission calculations are done in spreadsheets at quarter-end. Partners feel unsupported, deals conflict between direct and channel sales, and the training company has no idea which partners are actually productive vs. which are just registered.

#### The Solution
monday.com **CRM** configured as a **Partner Portal**. A **Partner Directory board** tracks all partners: type (consulting, technology, association, reseller), certification level, territory, active deal count, historical revenue, and commission tier. A **Partner Deal Registration board** captures partner-sourced deals with conflict-check automations (does this deal overlap with a direct sales opportunity?). **Partner Enablement board** tracks co-marketing activities, training certifications for partner sales reps, and content shared. **Dashboards** show partner contribution to pipeline, partner productivity rankings, deal registration-to-close conversion, and commission forecasts. Partners can access their own boards via **monday.com guest access** for self-service deal registration and pipeline visibility.

#### The Outcome
- Complete visibility into partner pipeline — no more surprise deals or conflicts
- 40% faster deal registration-to-approval cycle
- Partner productivity insights drive better investment decisions (invest in top partners, exit non-productive ones)
- Commission accuracy — automated calculations eliminate quarter-end spreadsheet chaos
- Partners feel supported → more engaged → more revenue

#### Discovery Questions
1. "What percentage of your revenue comes through partners, and is that growing or shrinking?"
2. "How do partners register deals today, and how do you check for conflicts with your direct pipeline?"
3. "Can you rank your partners by productivity right now? How long would that analysis take?"
4. "How do you calculate and communicate partner commissions? How often are there disputes?"
5. "What's the biggest complaint you hear from your partners about working with you?"

#### Industry Context
Training channel models include: **Referral partners** (lead referral for commission, typically 10-15%), **Resellers** (buy at discount, sell at market price, 20-40% margin), **White-label partners** (rebrand and deliver as their own, 40-60% margin), **OEM/embedded** (training bundled into another product), and **Association partnerships** (co-branded programs for members). **Channel conflict** — when a partner and a direct rep are both pursuing the same account — is a persistent headache. **Deal registration** (first-to-register gets protection) is the standard mechanism. **Partner tiers** (Silver/Gold/Platinum) with escalating benefits and requirements are common.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Partner Channel Management system for a training company. Board 1 — Partner Directory: Columns: Partner Company (text), Partner Type (dropdown: Consulting, Technology Vendor, Association, Regional Reseller, White-Label, Referral), Partner Tier (status: Registered, Silver, Gold, Platinum), Primary Contact (text), Contact Email (email), Territory (dropdown: North America, EMEA, APAC, LATAM, Global), Verticals Served (tags: Healthcare, Finance, Government, Manufacturing, Technology, Education), Certified Reps (numbers), Active Deals (numbers), YTD Revenue (numbers), Lifetime Revenue (numbers), Commission Rate (numbers, percentage), Contract Start Date (date), Contract End Date (date), Partner Manager (people), Status (status: Active, Inactive, Prospect, Suspended), Last Activity Date (date), Performance Rating (rating 1-5), Notes (long text). Board 2 — Partner Deal Registration: Columns: Registration ID (auto-number PDR-), Partner (connect to Directory), Client Company (text), Client Contact (text), Estimated Deal Value (numbers), Expected Close Date (date), Courses/Products (connect to Product Catalog), Registration Date (date), Registration Status (status: Submitted, Under Review, Approved, Rejected — Conflict, Expired), Conflict Check (status: Clear, Conflict Detected, Override Approved), Conflicting Direct Deal (connect to Deals Pipeline), Deal Stage (status: Registered, Active Pursuit, Proposal, Negotiation, Closed Won, Closed Lost), Actual Revenue (numbers), Commission Earned (formula: Actual Revenue × Partner Commission Rate), Commission Status (status: Not Earned, Pending, Approved, Paid), Notes (long text). Automations: when new registration is submitted, auto-check Deals Pipeline for matching Client Company — if match found, set Conflict Check to Conflict Detected and notify Channel Manager; when Registration Status is Approved and no activity for 90 days, set to Expired; when Deal Stage changes to Closed Won, calculate commission and notify finance; when Partner's Active Deals count exceeds tier threshold, suggest tier upgrade to Partner Manager. Views: Partner leaderboard by YTD Revenue, Deal registrations Kanban by status, Commission tracker table. Dashboard: partner revenue contribution (pie chart vs. direct), top 10 partners by revenue (leaderboard), deal registration pipeline (funnel), commission forecast (number), partner activity trend (line chart), conflict rate (percentage), partner tier distribution (pie chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ChannelGuard
**Agent Purpose:** Automate deal registration processing, detect channel conflicts, track partner health, and optimize channel investment.

**Triggers:**
- New partner deal registration submitted
- Partner deal stage changes
- Partner inactive for 60+ days
- Monthly schedule: partner health and commission report
- New direct deal created that matches a registered partner deal

**Actions:**
- Instantly check new registrations against direct pipeline and existing partner registrations for conflicts (company name fuzzy matching + contact matching)
- Auto-approve registrations with no conflicts and partner in good standing (Gold/Platinum tier, no disputes in 12 months)
- Generate monthly partner scorecard: deal volume, win rate, average deal size, time-to-close, commission earned, engagement score
- Identify underperforming partners (registered >6 months, <$10K revenue) and recommend action: additional enablement, tier downgrade, or exit
- Calculate commissions and generate payment recommendation for finance
- Detect patterns: "Partners who complete our Advanced Sales Certification close 34% larger deals. 12 Silver-tier partners haven't completed it — recommend targeted outreach."

**Data Required:**
- Partner Directory board
- Deal Registration board
- Deals Pipeline (for conflict checking)
- Historical partner performance data
- Commission rate tables by tier
- Partner training/certification records

**Autonomy Level:** Escalation-Based
Conflict-free registrations for Gold/Platinum partners are auto-approved. All conflict cases require Channel Manager review. Commission calculations are auto-generated but require finance approval for payment. Partner exit recommendations require VP Sales approval.

**Example Interaction:**
> A new deal registration comes in from TechBridge Consulting (Gold partner): "Zenith Healthcare — Compliance Training Suite, $185K." ChannelGuard checks in 3 seconds: "✅ **Registration PDR-0847 Auto-Approved.** No conflict detected — 'Zenith Healthcare' not found in direct pipeline (checked company name, domain zenithhealth.org, and contacts). TechBridge Consulting: Gold tier, 14 successful closes in past 12 months, no disputes. Commission rate: 20% ($37,000 if closed). **Note:** Zenith Healthcare is in the Healthcare vertical — sending TechBridge our updated HIPAA Training battle card and the Memorial Health Systems case study to support their pursuit."

---

### Use Case 6: Client Engagement & Renewal Intelligence

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
For subscription and multi-year training contracts, renewal is where the money is — acquiring a new client costs 5-7× more than retaining one. But training companies often don't know a renewal is at risk until the client ghosts the renewal conversation. The signals are there but invisible: declining seat utilization (they bought 500 seats but only 200 are logging in), dropping completion rates, no new course purchases after the initial sale, support tickets increasing. These data points live in different systems (LMS, support desk, CRM) and nobody is connecting the dots. By the time sales re-engages, the client has already evaluated alternatives.

#### The Solution
monday.com as a **Client Health & Renewal Dashboard** connecting deal data, utilization metrics, and engagement signals. Each active client is an item on a **Client Health board** with: contract details, utilization metrics (synced from LMS), engagement score (composite of utilization, support interactions, training completions, and expansion purchases), renewal date, renewal probability, and assigned Account Manager. **Automations** trigger health check workflows when utilization drops below 60%, schedule QBR (Quarterly Business Review) prep 2 weeks before review dates, and escalate at-risk renewals. **Dashboards** display client health across the portfolio: green/yellow/red status, upcoming renewals with risk scores, and revenue-at-risk calculations.

#### The Outcome
- Early warning on at-risk renewals — 90+ days before expiration, not 30
- Net retention rate improvement from ~85% to 92%+ through proactive engagement
- Data-driven QBR conversations that demonstrate value and identify expansion opportunities
- Revenue-at-risk visibility for accurate forecasting

#### Discovery Questions
1. "What's your current net retention rate, and how does it compare to your target?"
2. "How do you know when a client is at risk of churning? What signals do you track?"
3. "Do you conduct QBRs with your clients? How do you prepare for them?"
4. "What data do you wish you had when walking into a renewal conversation?"
5. "What's the revenue impact when you lose a top-20 client?"

#### Industry Context
**Net Revenue Retention (NRR)** above 100% means existing clients are expanding faster than they're churning — the gold standard. Training companies track **seat utilization** (active users / licensed seats), **completion rates** (courses finished / courses started), **adoption breadth** (how many different courses are being consumed), and **expansion velocity** (time to second purchase). **QBRs** (Quarterly Business Reviews) are the primary retention mechanism — structured reviews of training impact, utilization, and future needs. **Health scores** typically weight: utilization (40%), engagement (25%), support (15%), expansion (20%).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Client Health & Renewal Management system for a training company. Columns: Client Name (text), Account Manager (people), Contract Value (numbers), Contract Start (date), Contract End (date), Renewal Date (date), Licensed Seats (numbers), Active Users (numbers), Utilization Rate (formula: Active Users / Licensed Seats × 100), Courses Purchased (numbers), Courses Active (numbers), Completion Rate (numbers, percentage), Last Login Date (date), Days Since Last Activity (formula), Support Tickets Open (numbers), Support Tickets Total (numbers), Last QBR Date (date), Next QBR Date (date), Expansion Revenue (numbers), Health Score (formula: weighted composite), Health Status (status: Healthy, Monitor, At Risk, Critical), Renewal Probability (dropdown: Very Likely, Likely, Uncertain, Unlikely, Lost), Renewal Value (numbers), Risk Factors (long text), Action Plan (long text), NPS Score (numbers), Champion Contact (text), Executive Sponsor (text). Add automations: when Utilization Rate drops below 60%, change Health Status to Monitor and notify Account Manager with suggested re-engagement actions; when Utilization Rate drops below 40%, change to At Risk and notify Sales Director; when Renewal Date is 90 days away, create renewal opportunity on Deals Pipeline and schedule QBR prep task; when Health Status is Critical for more than 14 days, escalate to VP Sales; when NPS Score drops below 30, create urgent action item. Create Dashboard: portfolio health overview (number widgets for Healthy/Monitor/At Risk/Critical counts), revenue by health status (stacked bar), upcoming renewals next 90 days with health color (table), utilization trend across portfolio (line chart), top at-risk accounts by revenue (sorted table), NPS distribution (histogram), Account Manager performance by retention rate (chart), revenue at risk (number widget summing At Risk + Critical contract values)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RetentionRadar
**Agent Purpose:** Continuously monitor client health signals, predict churn risk, and orchestrate proactive retention interventions.

**Triggers:**
- LMS data sync completes (daily: utilization, completions, logins)
- Support ticket created or resolved for a client
- Client health score drops below threshold (Monitor: <70, At Risk: <50)
- QBR date approaching (14 days before)
- Renewal date approaching (120, 90, 60, 30 days)

**Actions:**
- Calculate daily health scores from multi-source data and update client board
- When health score drops, generate specific diagnosis: "Utilization dropped from 78% to 52% in 30 days. Analysis: 3 of 5 licensed courses show <20% activity — likely these courses have been completed by most users and no new content has been assigned. Recommendation: propose course refresh or catalog expansion."
- Generate QBR prep package: utilization report, completion metrics, ROI summary, recommended discussion topics, expansion opportunities, and risk factors
- Predict churn probability 120 days out based on: utilization trajectory, engagement patterns, support sentiment, and historical patterns from similar accounts
- Orchestrate "save plays" for at-risk accounts: schedule executive touch, prepare value demonstration, identify champion within client organization, and draft re-engagement messaging
- After successful renewal, analyze what worked and update retention playbook

**Data Required:**
- Client Health board (all fields)
- LMS utilization and completion data (API integration)
- Support ticket system (volume, sentiment, resolution time)
- Deals Pipeline (original deal details, expansion history)
- QBR history and notes
- NPS/CSAT survey responses
- Historical churn data for predictive modeling

**Autonomy Level:** Escalation-Based
Health score updates and QBR prep are fully automated. At-risk alerts trigger notification chains but don't initiate client outreach without AM approval. Churn predictions are informational — the AM decides the response. Save play orchestration creates the plan; humans execute it.

**Example Interaction:**
> RetentionRadar detects a concerning pattern at Pinnacle Insurance Group ($420K annual contract, renewal in 87 days): "🚨 **Churn Risk Alert — Pinnacle Insurance Group.** Health Score dropped from 72 → 48 in 6 weeks. **Diagnosis:** 1) Active users down 35% (likely post-annual-enrollment period, but steeper decline than expected), 2) Zero new course activations in 60 days (they purchased 12 courses but only use 7 actively), 3) 4 support tickets opened in past 30 days (up from avg 1/month) — 2 related to LMS SSO issues, 2 about outdated content in Regulatory Module 3. 4) NPS dropped from 62 to 38 at last survey. **Churn Probability: 45% (up from 12% last quarter).** **Recommended Save Play:** 1) Immediate: Resolve SSO tickets within 48 hours (escalate to Tier 2 support), 2) This week: AM call to L&D Director — acknowledge content issue, commit to Module 3 refresh by March 30, 3) Within 14 days: Executive sponsor outreach (VP Sales → Pinnacle VP HR) — relationship reinforcement, 4) QBR in 21 days: Present utilization analysis showing $180K in unrealized value from 5 unused courses — offer activation workshop, 5) Renewal conversation: Propose 2-year renewal at 8% discount with content refresh commitment and dedicated CSM. **Revenue at risk: $420K.**"

---

### Use Case 7: BDR Outbound Prospecting & Lead Management

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
BDR teams in training companies struggle with prospecting efficiency. They need to identify companies with training needs (new regulations, rapid growth, digital transformation, compliance failures), craft relevant outreach (not generic "do you need training?" emails), and manage multi-touch sequences across email, phone, and LinkedIn. Without a systematic approach, BDRs waste time on unqualified prospects, send generic messages that get ignored, and can't track which outreach sequences perform best. The average BDR books 8-12 meetings per month when the target is 15-20. The pipeline suffers and AEs blame marketing for "bad leads" while BDRs blame the product for being "hard to pitch."

#### The Solution
monday.com **CRM** for lead management combined with **AI** for intelligent prospecting. A **Prospecting board** captures target accounts with enrichment data: company size, industry, recent news (regulatory changes, growth announcements, compliance incidents), current training vendor, and estimated training spend. **AI-assisted sequences** generate personalized outreach based on prospect triggers: "We noticed your industry just got hit with new EPA regulations — here's how 200 similar companies are handling the training requirement." **Automations** manage multi-touch cadences: email → wait 3 days → LinkedIn connect → wait 5 days → phone call → wait 7 days → final email. **Dashboards** track BDR activity metrics, conversion rates by sequence, and pipeline contribution.

#### The Outcome
- 40-50% increase in BDR meeting bookings through personalized, trigger-based outreach
- 3× improvement in email response rates (personalized vs. generic)
- Complete activity tracking — every touch documented, no leads lost
- Data-driven sequence optimization: double down on what works, kill what doesn't

#### Discovery Questions
1. "How do your BDRs currently identify and prioritize target accounts?"
2. "What's your BDR team's average meetings booked per month, and what's the target?"
3. "Are your outreach sequences personalized to the prospect's industry and situation, or mostly template-based?"
4. "How do you track which outreach sequences and messages perform best?"
5. "What percentage of BDR-sourced leads convert to qualified opportunities?"

#### Industry Context
Training company prospecting is often **trigger-based**: new regulation (OSHA updates, SEC rules, HIPAA changes), company growth (hiring surge = onboarding need), M&A activity (culture integration training), digital transformation (upskilling/reskilling), compliance failures (public fines or incidents), and leadership changes (new CHRO often reviews training programs). **Intent signals** — companies searching for training-related keywords, downloading compliance guides, attending industry conferences — are gold for BDRs. **Account-based marketing (ABM)** is increasingly common for enterprise training sales.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a BDR Prospecting System for a training company. Board 1 — Target Accounts: Columns: Company Name (text), Website (link), Industry (dropdown: Healthcare, Financial Services, Manufacturing, Technology, Government, Energy, Retail, Professional Services, Education, Other), Company Size (dropdown: 50-200, 201-500, 501-1000, 1001-5000, 5001-10000, 10000+), Estimated Training Budget (dropdown: <$100K, $100K-500K, $500K-$1M, >$1M), Key Contact Name (text), Contact Title (text), Contact Email (email), Contact LinkedIn (link), Account Priority (status: Tier 1, Tier 2, Tier 3), Prospecting Trigger (dropdown: New Regulation, Rapid Growth, M&A, Compliance Incident, Digital Transformation, Vendor Displacement, Contract Expiration, No Trigger), Trigger Details (long text), Current Training Vendor (text), Assigned BDR (people), Outreach Status (status: Not Started, Sequence Active, Responded, Meeting Booked, Qualified Out, Not Interested), Sequence Type (dropdown: Regulatory Trigger, Growth Trigger, Competitive Displacement, Cold Outreach, Referral Follow-Up), Touch Count (numbers), Last Touch Date (date), Next Touch Date (date), Meeting Date (date), Notes (long text). Automations: when Outreach Status changes to Sequence Active, set Next Touch Date to today + 1; when Touch Count reaches 6 with no response, change Outreach Status to Qualified Out; when Meeting Date is set, change Outreach Status to Meeting Booked and create deal item on Pipeline board; automated cadence: on Next Touch Date, remind BDR of scheduled touch with suggested action (email/call/LinkedIn based on sequence step). Dashboard: accounts by outreach status (funnel), BDR activity leaderboard (touches per week), meetings booked this month (number), response rate by sequence type (chart), pipeline value from BDR-sourced leads (number), accounts by trigger type (pie chart), touch-to-meeting conversion rate (number)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProspectPulse
**Agent Purpose:** Identify high-value prospecting triggers, generate personalized outreach, and optimize BDR cadences based on response data.

**Triggers:**
- Daily schedule: scan news feeds for prospecting triggers (regulatory changes, compliance fines, growth announcements)
- New target account added to Prospecting board
- Prospect responds to outreach (email reply detected)
- Weekly schedule: sequence performance analysis
- BDR requests outreach draft for a specific account

**Actions:**
- Scan industry news and regulatory feeds to identify companies with active training triggers: "New OSHA silica dust rule affects 2.3M workers in construction — here are 50 construction companies in our target list that need updated safety training"
- Generate personalized outreach emails based on prospect's trigger, industry, and role: tailored subject lines, pain-specific opening, relevant course mention, and clear CTA
- Analyze response data and recommend sequence adjustments: "The 'Regulatory Trigger' sequence has 18% response rate for healthcare but only 4% for manufacturing. Manufacturing prospects respond better to 'peer comparison' messaging — updating template."
- Auto-enrich new target accounts with company news, LinkedIn updates, and estimated training spend
- When a prospect responds, analyze sentiment and recommend next action: positive response → book meeting, objection → provide handle, information request → send relevant content

**Data Required:**
- Target Accounts board
- Industry news and regulatory feeds
- Email/outreach analytics (open rates, response rates)
- Company enrichment data (LinkedIn, news, public records)
- Historical sequence performance data
- Product Catalog (for course matching to triggers)

**Autonomy Level:** Human-in-the-Loop
Trigger identification and account enrichment are fully automated. Outreach drafts are generated but BDR reviews and sends. Sequence optimization recommendations require BDR manager approval before updating templates. Sentiment analysis is informational — BDR decides the response.

**Example Interaction:**
> ProspectPulse's morning scan identifies a trigger: "🎯 **Prospecting Trigger Detected:** The FDA published new 21 CFR Part 11 amendments yesterday, expanding electronic records requirements for pharmaceutical manufacturers. Impact: ~400 pharma companies need to update their GxP compliance training within 180 days. **Action:** I've identified 23 pharma companies on your Tier 1 and Tier 2 target lists. Draft outreach generated for top 10 by estimated training budget. Sample for BDR Sarah: **Subject:** '21 CFR Part 11 changes — is your GxP training current?' **Body:** 'Hi Dr. Patterson — yesterday's FDA amendment to 21 CFR Part 11 expands electronic records requirements that directly affect your manufacturing validation training program. When Novartis faced similar regulatory updates in 2024, they retrained 3,200 employees in 90 days using our GxP Compliance Suite — beating the deadline by 60 days. Could we spend 15 minutes discussing how [Company] is planning to address the new requirements? I have a compliance gap checklist that might be useful regardless.' Shall I add these accounts to the active sequence?"

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ILT | Instructor-Led Training — in-person classroom delivery, highest cost but highest engagement |
| VILT | Virtual Instructor-Led Training — live online sessions via Zoom/Teams/WebEx |
| eLearning | Self-paced digital learning modules, typically SCORM-packaged for LMS delivery |
| Blended Learning | Combination of modalities (e.g., eLearning + ILT + coaching) |
| Seat License | Permission for one user to access a course or catalog — primary pricing unit |
| Enterprise Agreement | Multi-year, multi-product contract typically with unlimited or high seat counts |
| CPQ | Configure, Price, Quote — the process of assembling a deal-specific proposal with accurate pricing |
| RFP | Request for Proposal — formal procurement process common in government and large enterprise |
| GSA Schedule | General Services Administration pricing for U.S. government purchases |
| QBR | Quarterly Business Review — structured client meeting to review value and plan ahead |
| NRR | Net Revenue Retention — measures whether existing clients are growing (>100%) or shrinking (<100%) |
| LMS | Learning Management System — platform hosting and tracking training delivery |
| CPE/CE | Continuing Professional Education / Continuing Education credits |
| SME | Subject Matter Expert — domain specialist for content validation |
| Seat Utilization | Active users divided by licensed seats — key renewal health indicator |
| LPTA | Lowest Price Technically Acceptable — government procurement method where lowest price wins |
| Best Value | Government procurement method weighing technical merit, past performance, and cost |
| White-Label | Partner rebrands and delivers training as their own product |
| ABM | Account-Based Marketing — targeted approach focusing resources on specific high-value accounts |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/Director of Sales | Revenue targets, team structure, compensation, pricing authority | Decision-maker |
| Account Executive (AE) | Full-cycle deal management, discovery through close | Primary user — deal owner |
| Business Development Rep (BDR) | Prospecting, lead qualification, meeting booking | User — top of funnel |
| Solution Architect / Sales Engineer | Custom solution design, technical proposal sections, demos | Influencer — technical authority |
| Channel/Partner Manager | Partner recruitment, enablement, deal registration | User — channel deals |
| Sales Operations | CRM administration, forecasting, commission calculation, reporting | Power user — data |
| Sales Enablement Manager | Training reps, maintaining playbooks, competitive intelligence | User — content owner |
| Revenue Operations | Cross-functional alignment of sales, marketing, and CS | Influencer — process |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Product & R&D | Sales needs product roadmap visibility and customer feedback channel to R&D | Connected boards: deal requests feeding product pipeline |
| Marketing | Marketing generates leads and content that sales uses; sales provides market intelligence back | CRM + marketing automation integration for lead nurture |
| Operations / Delivery | Sales hands deals off to delivery; delivery issues feed back to client health | Work Management for seamless deal-to-delivery transition |
| Customer Success | CS manages ongoing client relationships; renewal signals feed sales pipeline | CRM for unified client view across sales and CS |
| Finance | Commission calculations, deal margin analysis, pricing governance | Dashboards connecting deal data to financial reporting |
| HR | Internal training sales reps need onboarding and ongoing enablement | Work Management for sales enablement programs |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce | Industry-standard CRM — but requires heavy customization for training sales workflows | monday.com CRM is simpler to configure, faster to deploy, and cheaper. Training-specific fields and workflows work out-of-the-box with Vibe configuration. Best for <100-person sales teams not locked into Salesforce ecosystem. |
| HubSpot | Strong for SMB training companies — good marketing integration | monday.com offers more flexibility for complex training pricing models, better project management handoff to delivery, and superior automation depth for multi-product deals |
| Pipedrive | Simple pipeline tool for small teams | monday.com scales better as the team grows, offers portfolio-level reporting, and connects sales to delivery/operations |
| Outreach / SalesLoft | BDR sequence tools — excellent for outreach automation | monday.com with AI can handle sequencing for smaller teams; for larger BDR operations, it integrates with Outreach/SalesLoft while managing the broader pipeline |
| Proposify / PandaDoc | Proposal and document generation | monday.com Docs + Vibe-built quote tools replace these for most training companies, with the advantage of being integrated directly into the CRM workflow |
| Spreadsheets (Google Sheets/Excel) | "Free" but fragile — common for pricing, forecasting, and commission tracking | monday.com eliminates version control nightmares, enables real-time collaboration, and provides automated dashboards that spreadsheets can't match |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Salesforce" | "Salesforce is powerful but expensive and complex for training companies. Your team likely has fields and workflows that don't fit your business — custom course bundles, modality pricing, seat-count tiers. monday.com CRM gives you a training-native pipeline in weeks, not months. And if you're committed to Salesforce for enterprise reporting, monday.com integrates as your sales team's daily driver while syncing deal data back to SFDC." |
| "We're too small for a CRM" | "You're not too small — you're at the perfect stage. Implementing a CRM when you have 5 reps and 50 deals is 10× easier than when you have 20 reps and 500 deals. monday.com CRM literally takes a day to set up. The cost of not having pipeline visibility is invisible until you miss your number." |
| "Our sales process is too custom for a standard CRM" | "That's exactly why monday.com works — it's not a standard CRM. It's a flexible platform you can configure to match *your* process. Multi-modality pricing? Custom development scoping? Partner deal registration? We build it the way you work, not force you into our workflow." |
| "We need integration with our LMS for utilization data" | "Absolutely — monday.com integrates with major LMS platforms via API, Zapier, or Make. We pull utilization data into the client health board so your AMs see renewal risk signals without logging into the LMS. It actually becomes *more* useful than the LMS's own reporting because you're correlating utilization with deal data." |
| "We can't justify the cost with our margins" | "Training companies operate on thin margins — that's exactly why sales efficiency matters. If your AEs save 5 hours/week on admin and close 1 additional deal per quarter because of better pipeline management, that's $50K-200K in incremental revenue. monday.com CRM pays for itself with the first deal it helps you not lose." |

## Proof Points
*(To be populated with customer references)*
- Training companies using monday.com CRM for sales pipeline management
- eLearning companies that improved win rates with structured proposal workflows
- Training organizations managing partner channels on monday.com
- Companies tracking client health and renewal risk on monday.com dashboards

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
