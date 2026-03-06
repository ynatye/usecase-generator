# Advertising & Marketing × Procurement Playbook

## Overview

Procurement in advertising and marketing agencies and holding companies operates under intense pressure to manage vendor sprawl, negotiate competitive rates with media suppliers, production houses, freelancers, and technology platforms, while maintaining compliance with client pass-through billing requirements. The department typically sits within Finance or Operations and manages anywhere from dozens to thousands of vendor relationships depending on agency size — from boutique shops with 50 vendors to holding companies like WPP or Publicis managing 10,000+ global supplier relationships.

The advertising procurement function is uniquely complex because spend is often "pass-through" — clients reimburse media buys and production costs, but the agency must still negotiate, contract, and manage those vendors. This creates a dual accountability: procurement must satisfy both internal margin targets and client transparency requirements. Regulatory frameworks like SOX compliance (for publicly traded holding companies), GDPR (for data vendors), and increasingly ESG reporting on supply chain diversity add layers of complexity.

Procurement teams in this industry are typically lean (3-15 people even at large agencies), relying heavily on spreadsheets, email chains, and legacy systems like SAP Ariba or Coupa. The pace of advertising — campaigns launching in weeks, not quarters — means procurement often becomes a bottleneck, with creative teams bypassing formal processes to meet deadlines. This "maverick spend" can represent 20-40% of total vendor expenditure at poorly governed agencies.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Procurement teams juggle SAP, spreadsheets, email, and contract management tools — a unified platform eliminates context-switching and brings visibility |
| 2 | Replace or Radically Augment Headcount | High | Small procurement teams can't keep pace with vendor onboarding volume; AI can automate intake, compliance checks, and renewals |
| 3 | Scale Impact Without Overhead | Medium-High | As agencies win new clients, vendor volume scales but procurement headcount doesn't — need to scale processes without hiring |

## Prioritized Use Cases

---

### Use Case 1: Vendor Onboarding & Compliance Automation

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Onboarding a new vendor — freelance photographer, production studio, media partner — takes 2-4 weeks at most agencies. Procurement manually collects W-9s, insurance certificates, NDAs, diversity certifications, and banking details via email. Documents get lost, follow-ups fall through, and creative teams start working with unapproved vendors out of urgency. Compliance gaps create audit risk, especially for publicly traded holding companies under SOX requirements. A single missing insurance certificate on a production shoot can expose the agency to six-figure liability.

#### The Solution
monday.com Work Management with Forms, automations, and document management. A vendor onboarding board captures all required documentation via a structured intake form. Status columns track each compliance requirement (W-9: ✅, Insurance: ⏳, NDA: ❌). Automations trigger reminders when documents are missing or expiring. Dashboard views give procurement leaders real-time visibility into onboarding pipeline and compliance status. monday AI Sidekick can review uploaded documents and flag discrepancies.

#### The Outcome
Reduce vendor onboarding time from 2-4 weeks to 3-5 business days. Eliminate maverick spend by making approved vendor lookup instant. Achieve 100% compliance documentation before any PO is issued. Save 15-20 hours/week of manual follow-up per procurement coordinator.

#### Discovery Questions
1. "How many new vendors does your agency onboard per month, and what percentage start work before procurement has fully vetted them?"
2. "When's the last time an audit flagged a compliance gap on a vendor — and what did that cost you?"
3. "How do your creative teams currently find out if a vendor is already approved and in good standing?"
4. "What happens when a vendor's insurance certificate expires mid-engagement?"
5. "How much time does your team spend chasing documents via email each week?"

#### Industry Context
In advertising, "vendors" span an enormous range: freelance creatives, stock footage libraries, print production houses, media owners (TV networks, digital publishers), research firms, event venues, talent agencies, and technology platforms. Each category has different compliance requirements. Production vendors need insurance and safety certifications; media vendors need credit terms and rebate agreements; freelancers need W-9s and IP assignment clauses. The SE should understand that "vendor management" in advertising is fundamentally different from manufacturing procurement.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Onboarding & Compliance Tracker for an advertising agency. Create a board with these columns: Vendor Name (text), Vendor Category (dropdown: Freelancer, Production House, Media Partner, Technology Platform, Research Firm, Event/Venue, Talent Agency, Other), Primary Contact (text), Email (text), Onboarding Status (status: New Request, Documents Pending, Under Review, Approved, Rejected), W-9/Tax Form (status: Not Received, Received, Verified), Insurance Certificate (status: Not Received, Received, Verified, Expired), NDA Status (status: Not Sent, Sent, Signed), Diversity Certification (status: N/A, Pending, Certified), Insurance Expiry Date (date), Assigned Reviewer (people), Client Association (dropdown: list of 10 client names), Notes (long text). Add automations: when Onboarding Status changes to 'Documents Pending', notify Assigned Reviewer; when Insurance Expiry Date arrives, change Insurance Certificate to 'Expired' and notify Assigned Reviewer; when all compliance statuses are 'Verified' or 'Signed', change Onboarding Status to 'Approved'. Create a Kanban view grouped by Onboarding Status and a Dashboard with widgets showing: vendors by category (pie chart), compliance completion rate (battery), vendors with expiring insurance in next 30 days (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorGuard
**Agent Purpose:** Autonomously manage vendor compliance lifecycle from onboarding through renewal, ensuring zero compliance gaps.

**Triggers:**
- New vendor request submitted via form
- Insurance Expiry Date within 30 days
- Weekly compliance audit schedule (Monday 9 AM)
- New PO created referencing unapproved vendor
- Vendor status changed to "Under Review"

**Actions:**
- Send personalized onboarding document request emails to vendors with specific checklists based on Vendor Category
- Parse uploaded documents (W-9, insurance certificates) and extract key fields (coverage amounts, expiration dates, tax IDs)
- Flag discrepancies (e.g., insurance coverage below $1M minimum, expired documents)
- Auto-approve vendors meeting all criteria; escalate edge cases to procurement reviewer
- Generate weekly compliance summary report with risk scores
- Block PO creation for unapproved vendors and notify requesting team with ETA for approval

**Data Required:**
- Vendor onboarding board data
- Document uploads (PDFs, images)
- PO/purchasing board integration
- Company compliance policy thresholds (minimum insurance levels, required certifications by vendor category)

**Autonomy Level:** Human-in-the-Loop
Auto-approves vendors meeting 100% of standard criteria. Escalates to human reviewer when: coverage amounts are borderline, documents are ambiguous, vendor category is new/unusual, or diversity certification claims need verification.

**Example Interaction:**
> A creative director submits a vendor request form for "Luminous Studios," a video production house needed for a pharmaceutical client's campaign shoot next month. VendorGuard immediately creates an onboarding item, identifies the vendor category as "Production House," and sends Luminous Studios a tailored email requesting: general liability insurance (minimum $2M for pharma client work), workers' comp certificate, signed NDA with IP assignment clause, W-9, and safety compliance documentation.
>
> Three days later, Luminous uploads their documents. VendorGuard parses the insurance certificate and flags that their general liability coverage is $1M — below the $2M threshold required for pharma client engagements. It updates the status to "Under Review," notifies the procurement coordinator with a summary: "Luminous Studios GL coverage is $1M, pharma client requires $2M minimum. All other documents verified. Recommend requesting updated COI before approval." The procurement coordinator reaches out, Luminous provides an updated certificate, VendorGuard re-verifies, and changes status to "Approved" — all within 5 business days, with zero email chains to manage.

---

### Use Case 2: Media Vendor Rate Card Management & Negotiation Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Advertising agencies negotiate rates with hundreds of media vendors (TV networks, digital publishers, OOH companies, radio stations, podcast networks) across multiple markets. Rate cards are received as PDFs, Excel files, or emails, then manually entered into spreadsheets. When a media buyer needs current rates for a campaign plan, they either dig through email or ask procurement — creating delays. Historical negotiation data lives in individual buyers' inboxes, making it impossible to benchmark rates year-over-year or leverage volume across clients. Agencies leave 10-15% savings on the table simply because negotiation intelligence isn't centralized.

#### The Solution
monday.com Work Management as a centralized rate card and negotiation database. Each media vendor has an item with rate card attachments, negotiated rates by format/market, contract terms, and negotiation history logged in updates. Number columns track CPM/CPP benchmarks by media type. Formula columns calculate year-over-year rate changes. A connected board tracks active negotiations with stages (Request Sent, Counter Received, Final Terms, Signed). Dashboards provide real-time market rate intelligence across all vendors.

#### The Outcome
Centralize 100% of media vendor rate intelligence in one searchable platform. Reduce rate card lookup time from 30+ minutes to under 2 minutes. Enable data-driven negotiations saving 8-12% on media buys through historical benchmarking. Eliminate 5-10 hours/week of procurement time spent fielding "what's the rate for X?" questions.

#### Discovery Questions
1. "How do your media buyers currently access vendor rate cards when planning a campaign?"
2. "Can you tell me right now what your average CPM was across digital video vendors last quarter versus the same quarter last year?"
3. "When you're negotiating with a media vendor, how do you know what rates you've gotten from them historically — or what competing vendors charge?"
4. "How often do different buying teams negotiate with the same vendor without knowing about each other's deals?"
5. "What would it mean for your agency if every media buyer had instant access to your full negotiation history?"

#### Industry Context
Media buying is the largest cost center in advertising — agencies manage billions in media spend. Rate negotiations happen constantly: upfront season (May-June for TV), quarterly for digital, ongoing for programmatic. Key metrics include CPM (cost per thousand impressions), CPP (cost per rating point), and share-of-voice. The SE should know that "rate card" rates are always negotiable, and agencies' leverage comes from aggregating client spend. Terms like "make-goods" (free ads to compensate for underdelivery), "added value" (bonus placements), and "volume commitments" are standard vocabulary.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Media Vendor Rate Card Management system for an advertising agency. Create a main board called 'Media Vendor Directory' with columns: Vendor Name (text), Media Type (dropdown: Linear TV, Connected TV/Streaming, Digital Display, Digital Video, Social Media, OOH/Billboard, Radio, Podcast, Print), Market (dropdown: National, Top 10 DMAs, Regional, Local), Primary Contact (text), Current Rate Card (file), Base CPM (number), Negotiated CPM (number), Discount % (formula: (Base CPM - Negotiated CPM) / Base CPM * 100), Contract End Date (date), Volume Commitment (number, in dollars), YoY Rate Change % (number), Relationship Owner (people), Last Negotiation Date (date), Notes (long text). Create a connected board called 'Active Negotiations' with columns: Vendor (connected to Vendor Directory), Negotiation Stage (status: Preparing, RFP Sent, Proposal Received, Counter-Offer, Final Terms, Signed, Stalled), Target CPM (number), Current Offer (number), Gap to Target (formula), Client(s) (dropdown), Deadline (date), Negotiator (people). Add automations: when Contract End Date is 60 days away, create item in Active Negotiations board and notify Relationship Owner; when Negotiation Stage changes to 'Signed', update Negotiated CPM in Vendor Directory. Create a Dashboard with: average CPM by Media Type (chart), negotiation pipeline by stage (chart), contracts expiring in next 90 days (table), top 10 vendors by spend (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RateIntel
**Agent Purpose:** Automatically parse incoming rate cards, benchmark against historical data, and generate negotiation briefs with recommended target rates.

**Triggers:**
- New rate card document uploaded to vendor item
- Contract renewal date within 60 days
- New negotiation item created
- Monthly market benchmark report schedule (1st of month)
- Media buyer queries rate information via Sidekick

**Actions:**
- Parse uploaded rate card PDFs/Excel files and extract rates by format, daypart, and market into structured columns
- Compare new rates against historical data and flag increases above 5% threshold
- Generate negotiation brief with: historical rates, competitive benchmarks, volume leverage analysis, and recommended target CPM
- Create market benchmark reports summarizing rate trends across vendor categories
- Recommend vendor substitutions when rates exceed benchmarks by >15%
- Alert procurement when multiple teams are negotiating with the same vendor simultaneously

**Data Required:**
- Media vendor directory board
- Active negotiations board
- Historical rate card uploads (2+ years)
- Campaign spend data by vendor (from billing/finance systems)
- Industry benchmark data (optional integration with MediaOcean or SQAD)

**Autonomy Level:** Escalation-Based
Fully autonomous for rate card parsing, benchmarking, and report generation. Escalates to human for: negotiation strategy recommendations (provides data, human decides), vendor relationship issues, and contract approvals.

**Example Interaction:**
> NBCUniversal sends their Q3 2026 upfront rate card via email. RateIntel detects the new document, parses it, and extracts CPMs across primetime, late night, sports, and streaming (Peacock) inventory. It compares against Q3 2025 rates and flags: primetime CPM increased 12% YoY (above the 5% threshold), while Peacock streaming CPM decreased 8%. RateIntel generates a negotiation brief: "NBCU primetime rates up 12% vs. last year, but your agency's total NBCU spend increased 22%. Recommend countering at +4% max, leveraging volume growth. Peacock rates are trending favorably — consider shifting 15% of linear budget to streaming for better value. Three other agencies in our benchmark data achieved primetime CPMs 9% below NBCU's card rate this quarter." The procurement negotiator walks into the meeting armed with data, not guesses.

---

### Use Case 3: Freelancer & Contractor Management Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Advertising agencies rely heavily on freelancers — designers, copywriters, editors, developers, strategists — especially during peak campaign periods. A mid-size agency might engage 200-500 freelancers per year. Procurement manages contracts and payments, but the actual hiring happens across dozens of creative directors and project managers, each with their own "little black book" of preferred freelancers. There's no centralized freelancer database, no rate standardization, and no visibility into total freelancer spend. When tax season arrives, generating 1099s becomes a nightmare. When a key freelancer becomes unavailable, finding a replacement with the right skills takes days.

#### The Solution
monday.com Work Management as a freelancer talent management and procurement system. A master Freelancer Directory board captures skills, rates, availability, performance ratings, and compliance status. A connected Engagements board tracks active and past assignments with rates, hours, deliverables, and client billing codes. Forms allow hiring managers to submit freelancer requests that route to procurement for rate approval. Dashboards provide spend analytics by department, skill category, and individual freelancer. Automations enforce rate caps and compliance requirements before engagement begins.

#### The Outcome
Build a searchable freelancer database accessible to all hiring managers, reducing "sourcing" time from days to minutes. Standardize freelancer rates by skill category, saving 10-20% on freelancer spend through rate governance. Ensure 100% compliance with tax documentation (W-9, 1099 eligibility) before engagement. Provide real-time freelancer spend visibility to finance for accurate client billing and margin management.

#### Discovery Questions
1. "If a creative director needed a senior motion graphics freelancer available next Monday, how long would it take to find and onboard one?"
2. "Do you know your total freelancer spend across the agency right now — broken down by department and skill category?"
3. "How do you currently ensure that freelancer rates are consistent — that one CD isn't paying $150/hour for the same skill another CD gets at $80/hour?"
4. "What's your 1099 process like at year-end? How confident are you that every freelancer has current tax documentation?"
5. "Have you ever had a project delayed because a freelancer's availability changed and there was no backup?"

#### Industry Context
Freelancers are the lifeblood of advertising. During "pitch season" or major campaign launches, agencies can temporarily increase their workforce by 30-50% through freelancers. Day rates vary wildly: a junior designer might charge $300/day while a senior creative director commands $2,500+/day. The industry uses terms like "day rate" (not hourly), "buyout" (full rights to work product), "usage" (licensing fees for talent/content), and "kill fee" (payment for canceled work). The SE should understand that agencies bill freelancer time back to clients with markup (typically 15-25%), so accurate tracking directly impacts profitability.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Freelancer Management System for an advertising agency. Create a board called 'Freelancer Directory' with columns: Freelancer Name (text), Email (text), Phone (text), Skill Category (dropdown: Copywriting, Art Direction, Graphic Design, Motion Graphics, Video Editing, Photography, Illustration, UX/UI Design, Web Development, Strategy, Production, Social Media, Other), Seniority (dropdown: Junior, Mid, Senior, Expert), Day Rate (number), Rate Tier (status: Below Standard, Standard, Above Standard, Premium), Availability (status: Available, Engaged, Unavailable, Do Not Rehire), Portfolio Link (link), W-9 Status (status: Not Received, Current, Expired), Average Rating (number, 1-5), Total Engagements (number), Last Engaged Date (date), Notes (long text). Create a connected board called 'Freelancer Engagements' with columns: Freelancer (connected to Directory), Project/Campaign (text), Client (dropdown), Hiring Manager (people), Department (dropdown: Creative, Production, Digital, Strategy, Content), Start Date (date), End Date (date), Days Booked (number), Agreed Day Rate (number), Total Cost (formula: Days Booked × Agreed Day Rate), Client Billing Code (text), Engagement Status (status: Requested, Approved, Active, Completed, Invoiced, Paid), Rating (number, 1-5), Deliverables (long text). Add automations: when Engagement Status is 'Requested' and Day Rate exceeds Rate Tier 'Premium', notify procurement for approval; when Engagement Status changes to 'Completed', prompt Hiring Manager for rating; when rating is submitted, update Average Rating on Freelancer Directory. Create Dashboard with: total freelancer spend by month (chart), spend by department (pie chart), top 20 freelancers by total billings (table), freelancers with expiring W-9s (table), average day rate by skill category (chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** TalentMatch
**Agent Purpose:** Match freelancer requests to the best-fit available talent, enforce rate governance, and predict capacity needs.

**Triggers:**
- New freelancer request form submitted
- Freelancer availability status changed to "Available"
- Active engagement approaching end date (5 days before)
- Monthly capacity forecast schedule
- Day rate entered above skill category benchmark

**Actions:**
- Match incoming requests against Freelancer Directory by skill, seniority, availability, rating, and rate — return top 3 recommendations with rationale
- Flag rate discrepancies ("This request is for $2,000/day for Senior Copywriting; your agency benchmark is $1,400/day. Three 4.5+ rated freelancers are available at standard rate.")
- Predict upcoming capacity gaps based on active engagements ending and known project pipelines
- Auto-generate 1099 eligibility reports at year-end with spend totals and tax documentation status
- Send re-engagement nudges to high-rated freelancers when their skill category is in demand
- Calculate freelancer utilization patterns and recommend "preferred freelancer" designations

**Data Required:**
- Freelancer Directory and Engagements boards
- Project/campaign timeline data
- Rate benchmarks by skill category and market
- Tax documentation records
- Client billing rate cards (for margin calculation)

**Autonomy Level:** Human-in-the-Loop
Recommends freelancer matches and flags rate issues autonomously. Human approves final selection and any rate exceptions. Fully autonomous for reporting, 1099 preparation, and capacity forecasting.

**Example Interaction:**
> A producer submits a request: "Need senior motion graphics freelancer for 10 days starting Feb 24, pharmaceutical client, budget $18,000." TalentMatch searches the directory and finds 7 senior motion graphics freelancers. It filters to 4 who are available and have pharma experience (tagged from previous engagements). It ranks them: "#1: Alex Chen — 4.8 rating, 12 prior engagements, day rate $1,600 (within budget), completed 3 pharma campaigns with excellent feedback. #2: Sarah Kim — 4.6 rating, 8 engagements, day rate $1,700 (within budget), pharma experience includes animated MOA videos. #3: Marcus Wright — 4.9 rating, 20 engagements, day rate $2,000 (over budget by $2,000 total), agency's most experienced pharma freelancer." The producer sees the recommendations, selects Alex, and the engagement is created with one click — procurement is notified, compliance is auto-verified (W-9 current), and the client billing code is pre-populated.

---

### Use Case 4: RFP & Pitch Procurement Coordination

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
When agencies pitch for new business, procurement plays a critical supporting role: sourcing research subscriptions, booking pitch rooms and travel, contracting specialty consultants, procuring props and prototypes for presentations, and managing NDA processes with potential subcontractors. Pitch timelines are brutally compressed — often 4-6 weeks from brief to presentation. Procurement receives urgent, often incomplete requests from pitch teams who are working around the clock. Without a structured process, procurement becomes either a bottleneck (slowing the pitch) or is bypassed entirely (creating compliance and cost issues). Post-pitch, there's rarely a reconciliation of what was spent versus budgeted, leading to "pitch cost" being a black box.

#### The Solution
monday.com Work Management with a dedicated Pitch Procurement board connected to the agency's new business pipeline. Each pitch gets a procurement workspace with categorized request items (Research, Travel, Consultants, Production, Technology, Venue), budget tracking, approval workflows, and timeline dependencies linked to pitch milestones. Automations notify procurement when a pitch moves to "Active" stage, pre-populating standard procurement tasks. Post-pitch, the board becomes a cost reconciliation record.

#### The Outcome
Reduce pitch procurement turnaround from days to hours with structured intake and pre-populated templates. Track 100% of pitch costs, enabling accurate new business ROI calculations. Eliminate post-pitch "surprise invoices" through real-time budget tracking. Free up 8-12 hours per pitch of procurement coordination time through automation and self-service.

#### Discovery Questions
1. "How many new business pitches does your agency run per quarter, and what's the average procurement spend per pitch?"
2. "When a pitch team needs something urgently — research, travel, a specialty consultant — how does that request reach procurement?"
3. "After a pitch is won or lost, do you reconcile actual costs against the pitch budget? How long does that take?"
4. "Have you ever had a pitch delayed because procurement couldn't turn around a vendor contract fast enough?"
5. "Do you know what your cost-per-pitch is — and how that differs between wins and losses?"

#### Industry Context
New business pitches are existential for advertising agencies — winning a major account can mean $10-50M+ in annual revenue. Agencies typically invest $50K-$500K per pitch in direct costs (research, travel, production, consultants) plus millions in opportunity cost (senior talent pulled from billable work). "Chemistry meetings," "credentials presentations," "tissue sessions" (interim creative reviews), and "the shootout" (final pitch day) are key milestones. Pitch consultants (like Pile & Company or AAR Partners) often mediate the process. The SE should understand the emotional intensity and time pressure of pitches.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Pitch Procurement Tracker for an advertising agency. Create a board called 'Pitch Procurement' with columns: Pitch Name (text), Prospect/Client (text), Pitch Stage (status: Briefed, Active, Submitted, Won, Lost, Declined), Pitch Lead (people), Pitch Date (date), Overall Budget (number), Spent to Date (formula summing connected items), Remaining Budget (formula: Overall Budget - Spent to Date), Procurement Status (status: Not Started, In Progress, All Fulfilled, Reconciled). Create a connected sub-items structure with: Request Item (text), Category (dropdown: Research/Data, Travel & Logistics, Consultants/Experts, Production/Prototyping, Technology/Tools, Venue/Events, Other), Vendor (text), Estimated Cost (number), Actual Cost (number), Variance (formula: Actual - Estimated), Priority (status: Critical Path, High, Standard), Request Status (status: Requested, Sourcing, PO Issued, Delivered, Invoiced, Paid), Requested By (people), Needed By Date (date). Add automations: when Pitch Stage changes to 'Active', create standard procurement checklist sub-items (Research subscription check, Travel pre-approval, NDA template prep); when Needed By Date is 2 days away and status is still 'Requested', escalate to procurement manager; when Pitch Stage changes to 'Won' or 'Lost', change Procurement Status to 'Reconciled' prompt. Create Dashboard with: total pitch spend by quarter (chart), spend by category (pie chart), budget vs. actual by pitch (grouped bar chart), active pitch procurement items by priority (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PitchOps
**Agent Purpose:** Orchestrate all procurement activities for new business pitches, ensuring nothing falls through the cracks under time pressure.

**Triggers:**
- New pitch item created or moved to "Active" stage
- Procurement request submitted by pitch team member
- Pitch date within 2 weeks and open procurement items exist
- Pitch stage changed to "Won" or "Lost"
- Budget threshold exceeded (>80% of allocated budget)

**Actions:**
- Auto-generate standard procurement checklist when pitch goes active (tailored by pitch size: S/M/L)
- Route procurement requests to appropriate specialists (travel → admin, research → procurement, consultants → pitch lead for approval)
- Send daily "pitch procurement status" digest to pitch lead showing: fulfilled items, pending items, at-risk items (needed-by date approaching)
- Alert procurement manager when pitch budget exceeds 80% with spend breakdown
- Generate post-pitch cost reconciliation report within 48 hours of pitch completion
- Archive pitch procurement data for benchmarking future pitch budgets

**Data Required:**
- New business pipeline board (pitch stages, dates, budgets)
- Pitch procurement board (requests, costs, vendors)
- Vendor directory (for rapid sourcing)
- Historical pitch cost data (for budget benchmarking)
- Travel booking system integration (optional)

**Autonomy Level:** Escalation-Based
Autonomous for checklist generation, status updates, reminders, and reporting. Escalates to humans for: budget approval over thresholds, vendor selection for specialty needs, and post-pitch strategic decisions.

**Example Interaction:**
> The agency enters "Pitch: Rivian Electric Vehicles" into the new business pipeline and moves it to "Active" with a $150K budget and 5-week timeline. PitchOps immediately generates a procurement checklist: EV industry research subscriptions (Gartner, McKinsey Automotive), travel for factory tour (4 people, Detroit), sustainability consultant for green messaging validation, prototype production for experiential concept, and pitch room AV setup. It pre-populates estimated costs from historical benchmarks: "Based on 3 similar automotive pitches in the last 18 months, average procurement spend was $127K. Your $150K budget provides 18% contingency." As the pitch progresses, PitchOps sends the pitch lead a daily digest: "3 of 8 procurement items fulfilled, 2 in progress, 3 not started. Critical path alert: sustainability consultant not yet contracted — needed by Feb 28 for tissue session. Recommend: Dr. Sarah Miller (used in Patagonia pitch, rate: $3,500/day) or GreenStory Consulting ($2,800/day, new vendor — would need 3-day onboarding)."

---

### Use Case 5: Software & SaaS License Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Advertising agencies are notorious for SaaS sprawl. A typical mid-to-large agency subscribes to 80-200+ software tools: creative suites (Adobe), project management, DAM systems, analytics platforms, social listening tools, programmatic DSPs, CRM, collaboration tools, stock media subscriptions, font licenses, and dozens of niche point solutions. Each department procures tools independently — media buys Moat, creative buys Figma, strategy buys Brandwatch. Procurement has no consolidated view of what's subscribed, what's overlapping, who's actually using it, and when renewals hit. Shadow IT is rampant. Annual SaaS spend at a 500-person agency can easily exceed $3-5M, with 20-30% waste from unused licenses, duplicate tools, and missed cancellation windows.

#### The Solution
monday.com Work Management as a SaaS license management hub. A master Software Inventory board captures every tool with: vendor, category, department owner, license count, cost, renewal date, contract terms, and utilization notes. Connected boards track Renewal Pipeline (upcoming renewals with negotiation stages) and New Software Requests (intake, evaluation, approval workflow). Dashboards visualize total SaaS spend, renewals by month, cost by department, and potential consolidation opportunities.

#### The Outcome
Achieve 100% visibility into SaaS portfolio — every tool, every license, every cost. Reduce SaaS spend by 15-25% through consolidation, unused license recovery, and proactive renewal negotiation. Eliminate surprise auto-renewals by triggering review processes 90 days before renewal. Establish governance that prevents shadow IT and duplicate tool purchases.

#### Discovery Questions
1. "If I asked you to list every software subscription your agency pays for, how long would it take — and how confident would you be it's complete?"
2. "How many times in the past year has someone discovered the agency was paying for two tools that do essentially the same thing?"
3. "What's your process when a tool auto-renews and nobody's using it anymore? How quickly do you catch that?"
4. "When a department wants to buy a new tool, is there a formal request and approval process, or do they just expense it?"
5. "Do you know your per-employee SaaS cost — and how it compares to industry benchmarks?"

#### Industry Context
Advertising agencies adopt technology voraciously because staying current is a competitive advantage — clients expect agencies to be ahead of the curve on MarTech, AdTech, and creative technology. This creates a "try everything" culture that's expensive to manage. Key tool categories include: Creative Production (Adobe CC, Figma, Sketch), Media Planning & Buying (MediaOcean, Prisma, The Trade Desk), Analytics (Google Analytics, Tableau, Datorama), Social (Sprout Social, Brandwatch, Hootsuite), Project Management (existing tools monday.com can consolidate!), DAM (Bynder, Brandfolder), and AI tools (Jasper, Midjourney, various). Enterprise license agreements (ELAs) with vendors like Adobe are significant line items.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a SaaS License Management System for an advertising agency. Create a board called 'Software Inventory' with columns: Tool Name (text), Vendor (text), Category (dropdown: Creative Production, Media & Advertising, Analytics & Data, Social Media, Project Management, DAM & Asset Management, Collaboration, CRM & Sales, Finance & Accounting, HR & People, AI & Automation, Security, Other), Department Owner (dropdown: Creative, Media, Strategy, Account Management, Production, IT, Finance, HR, All Agency), License Type (dropdown: Per Seat, Per Team, Enterprise, Flat Fee, Usage-Based), Number of Licenses (number), Active Users (number), Utilization Rate (formula: Active Users / Number of Licenses × 100), Monthly Cost (number), Annual Cost (formula: Monthly Cost × 12), Contract Start (date), Renewal Date (date), Auto-Renew (status: Yes, No), Contract Terms (dropdown: Monthly, Annual, Multi-Year), Cancellation Notice Period (dropdown: 30 Days, 60 Days, 90 Days, None), Review Status (status: Active & Needed, Active Under Review, Consolidation Candidate, Scheduled for Cancellation, Cancelled), Notes (long text). Add automations: when Renewal Date is 90 days away, change Review Status to 'Active Under Review' and notify Department Owner; when Utilization Rate falls below 50%, add a flag label 'Low Usage Alert'; when Review Status changes to 'Scheduled for Cancellation', notify IT and Finance. Create Dashboard with: total annual SaaS spend (number widget), spend by category (pie chart), upcoming renewals next 90 days (table), low utilization tools (filtered table where Utilization Rate < 50%), spend by department (bar chart), month-over-month spend trend (line chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** StackOptimizer
**Agent Purpose:** Continuously monitor SaaS portfolio health, identify waste, prevent surprise renewals, and recommend consolidation opportunities.

**Triggers:**
- Renewal date within 90 days on any tool
- New software request submitted
- Monthly SaaS audit schedule (1st of each month)
- Utilization rate drops below 50% on any tool
- New expense report filed with unrecognized software vendor name

**Actions:**
- Generate renewal briefs 90 days before expiration with: usage data, cost trend, competitive alternatives, and renewal negotiation recommendations
- Evaluate new software requests against existing inventory ("You already have Brandwatch which covers 80% of this use case — schedule a demo of their new features before purchasing a separate tool")
- Produce monthly SaaS audit report: total spend, new additions, cancellations, utilization changes, consolidation opportunities, projected 12-month cost
- Flag expense reports containing potential shadow IT purchases and route to procurement for evaluation
- Calculate "cost per active user" across all tools and benchmark against industry standards
- Recommend consolidation plays ("Your agency uses Asana, Trello, AND Basecamp across departments — consolidating to monday.com would save $142K/year and improve cross-team visibility")

**Data Required:**
- Software Inventory board
- SSO/identity provider data for actual usage (Okta, Azure AD integration)
- Expense reports (for shadow IT detection)
- New software request board
- Vendor pricing databases (for competitive benchmarking)

**Autonomy Level:** Human-in-the-Loop
Autonomous for monitoring, reporting, and flagging. Recommends actions but requires human approval for: cancellation decisions, new purchases, and consolidation initiatives. Fully autonomous for sending renewal reminders and utilization alerts.

**Example Interaction:**
> During the monthly audit, StackOptimizer identifies that the agency is paying for three stock photography subscriptions: Getty Images ($4,200/mo, 89% utilization), Shutterstock ($2,800/mo, 34% utilization), and Adobe Stock ($1,200/mo, 12% utilization). It generates a consolidation recommendation: "Stock media analysis: Getty is your primary source (890 downloads/mo). Shutterstock is used mainly by the social team (340 downloads/mo) — Getty's social media license tier would cover this for $800/mo additional. Adobe Stock has 12% utilization (14 downloads/mo) — likely purchased as part of Adobe CC bundle, verify if cancellable separately. Recommended action: upgrade Getty to enterprise tier (+$800/mo), cancel Shutterstock (-$2,800/mo), investigate Adobe Stock terms. Net savings: $2,000/mo ($24,000/year). Shall I draft cancellation notices and Getty upgrade request?"

---

### Use Case 6: Client Pass-Through Billing Reconciliation

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
A significant portion of agency procurement is "pass-through" — expenses incurred on behalf of clients (media buys, production costs, talent fees, travel) that are billed back to the client with or without markup. Reconciling what was procured, what the agency paid, and what was billed to the client is a manual, error-prone process involving procurement, finance, and account management. Discrepancies between vendor invoices and client billing lead to revenue leakage (agency absorbs costs that should be billed), client disputes, and audit findings. At a large agency, pass-through billing can represent 60-70% of total revenue, making accuracy critical.

#### The Solution
monday.com Work Management connecting procurement, finance, and account management in a single reconciliation workflow. Each procurement item carries client billing metadata: client name, job number, billing status, markup rate, and invoice reference. Automations flag discrepancies between vendor invoice amounts and client billing amounts. Monthly reconciliation dashboards highlight unbilled pass-throughs, margin leakage, and outstanding vendor payments.

#### The Outcome
Reduce pass-through billing errors by 90%, recovering 2-5% in previously leaked revenue. Cut monthly reconciliation time from 5+ days to 1 day through automation. Provide real-time visibility into pass-through margins by client and category. Eliminate client billing disputes caused by incomplete or inaccurate pass-through documentation.

#### Discovery Questions
1. "What percentage of your agency's revenue is pass-through versus fee-based, and how confident are you in the accuracy of pass-through billing?"
2. "How long does your monthly reconciliation process take between procurement, finance, and account management?"
3. "When's the last time you discovered a vendor invoice that was never billed back to the client — and how much was it?"
4. "How do you currently track markup rates by client, and do different clients have different pass-through terms?"
5. "If a client audits their billing, how quickly can you produce supporting documentation for every line item?"

#### Industry Context
Pass-through billing is governed by AAAA (4A's) standard terms and individual client contracts. Most clients now require "transparent" billing where they see actual vendor costs and agree markup rates in advance (typically 0-17.65%, with 17.65% being the historical "standard commission"). Clients increasingly demand audit rights, and major advertisers (P&G, Unilever) conduct regular agency audits through firms like MediaLink or FirmDecisions. "Sequential liability" clauses mean agencies may not have to pay vendors until they receive payment from clients — but this varies by contract. The SE should understand that pass-through accuracy is both a financial and relationship issue.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Pass-Through Billing Reconciliation board for an advertising agency. Create a board with columns: Vendor Name (text), Invoice Number (text), Invoice Date (date), Invoice Amount (number), Client (dropdown: list of major clients), Job/Project Number (text), Billing Category (dropdown: Media, Production, Talent & Licensing, Travel, Research, Technology, Other), Markup Rate % (number), Client Billing Amount (formula: Invoice Amount × (1 + Markup Rate / 100)), Billing Status (status: Pending Review, Approved for Billing, Billed to Client, Client Paid, Disputed, Write-Off), Vendor Payment Status (status: Not Due, Approved, Paid), Date Billed to Client (date), Date Client Paid (date), Days Outstanding (formula: TODAY - Date Billed), Account Manager (people), Reconciliation Notes (long text), Variance Flag (status: OK, Under-billed, Unbilled, Disputed). Add automations: when Invoice Amount is entered but Billing Status remains 'Pending Review' for 5 days, notify Account Manager; when Client Billing Amount minus Invoice Amount minus expected markup exceeds $100, set Variance Flag to 'Under-billed'; create a monthly summary automation that groups items by Client and Billing Category. Create Dashboard with: total pass-through by client (bar chart), unbilled items over 30 days (filtered table), billing status breakdown (pie chart), margin by category (chart), monthly pass-through volume trend (line chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BillReconciler
**Agent Purpose:** Automatically match vendor invoices to client billing, flag discrepancies, and ensure zero revenue leakage on pass-through costs.

**Triggers:**
- New vendor invoice uploaded or created
- Client billing cycle (monthly, per client schedule)
- Invoice age exceeds 14 days without billing action
- Client payment received
- Quarterly audit preparation schedule

**Actions:**
- Match incoming vendor invoices to client job numbers and auto-populate billing metadata
- Calculate correct billing amount based on client-specific markup agreements
- Flag mismatches: unbilled invoices, incorrect markup application, duplicate invoices, invoices exceeding approved PO amounts
- Generate client-ready billing summaries with supporting documentation links
- Produce quarterly audit-ready reports by client with complete invoice-to-billing chain
- Alert account management when client payments are 30+ days overdue on pass-through items

**Data Required:**
- Procurement/vendor invoice board
- Client contract terms (markup rates, billing cycles, audit requirements)
- Job/project numbering system
- Accounts receivable data
- Historical billing data for pattern matching

**Autonomy Level:** Human-in-the-Loop
Auto-matches invoices to jobs and calculates billing amounts. Flags discrepancies for human review. Generates reports autonomously. Requires human approval before any client-facing billing is issued.

**Example Interaction:**
> A $47,000 invoice arrives from a video production house for the "Acme Corp Q2 Brand Campaign" shoot. BillReconciler matches it to Job #ACM-2026-0142, identifies the client contract specifies 0% markup on production (pass-through at cost), and creates a billing line item for $47,000. It then cross-references the original PO: the approved production budget was $42,000. It flags the $5,000 overage: "Production invoice exceeds PO by $5,000 (11.9%). Possible causes: overtime shoot day, additional deliverables, or rate increase. Action needed: Account Manager to review with client before billing. Supporting docs attached: original PO, vendor invoice, production schedule showing 1 added shoot day." The account manager reviews, confirms the extra day was client-approved via email, and authorizes billing — BillReconciler updates the record with the approval documentation for audit trail.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Pass-through | Costs incurred on behalf of a client and billed back, typically at cost or with agreed markup |
| Maverick spend | Purchases made outside formal procurement processes |
| Rate card | Published pricing from media vendors, typically negotiable |
| CPM | Cost per thousand impressions — standard media buying metric |
| Day rate | Standard freelancer pricing unit in advertising (not hourly) |
| Kill fee | Payment owed to a vendor/freelancer when work is canceled after commitment |
| Make-good | Free media placement provided by a vendor to compensate for underdelivery |
| SOW | Statement of Work — defines vendor deliverables, timelines, and costs |
| MSA | Master Service Agreement — umbrella contract governing vendor relationship |
| PO | Purchase Order — formal authorization for vendor to proceed with work |
| Buyout | Full rights transfer for creative work; eliminates ongoing usage fees |
| Sequential liability | Contract clause where agency pays vendor only after receiving client payment |
| 4A's | American Association of Advertising Agencies — industry trade body that sets standard contract terms |
| Shadow IT | Software/tools purchased by departments without procurement knowledge or approval |
| ELA | Enterprise License Agreement — volume licensing deal with software vendors |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Procurement Officer / Head of Procurement | Sets procurement strategy, vendor governance, and cost optimization targets | Decision-maker |
| Procurement Manager | Day-to-day vendor management, contract negotiation, compliance monitoring | Decision-maker (operational) |
| CFO / Finance Director | Approves major contracts, sets budget constraints, oversees pass-through billing accuracy | Decision-maker (financial) |
| COO / Chief Operating Officer | Oversees agency operations including procurement as a function | Influencer |
| Creative Director | Primary "customer" of procurement for freelancer and production vendor sourcing | Influencer (demand driver) |
| Head of Media | Major procurement stakeholder for media vendor rates and contracts | Influencer |
| IT Director | Manages technology procurement, SaaS governance, and vendor integrations | Influencer (technology) |
| Account Director | Manages client billing including pass-through reconciliation | User |
| Producer | Day-to-day user of procurement for production-related vendor needs | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Finance | Pass-through billing, vendor payments, budget management | Unified vendor-to-billing workflow across procurement and finance |
| Creative & Design | Freelancer sourcing, production vendor management, tool procurement | End-to-end freelancer lifecycle from request to payment |
| Media | Rate card management, media vendor negotiations, buying platform procurement | Integrated media vendor intelligence and negotiation tracking |
| IT | SaaS management, technology procurement, vendor security reviews | Consolidated technology governance and license optimization |
| Operations | Process efficiency, office vendor management, facility procurement | Agency-wide operational procurement hub |
| Legal | Contract review, NDA management, compliance documentation | Connected contract management with procurement workflows |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SAP Ariba | Enterprise procurement suite — complex, expensive, designed for manufacturing | Too heavy for agency culture; monday.com offers agility and user adoption that Ariba can't match in creative environments |
| Coupa | Cloud procurement platform — strong in P2P automation | Overkill for most agencies; monday.com provides procurement functionality within a platform teams already use for project management |
| Procurify | Mid-market procurement — purchase orders and spend management | Point solution; monday.com offers broader value across procurement, project management, and collaboration |
| Spreadsheets (Excel/Sheets) | The actual incumbent in 80% of agency procurement teams | Zero automation, no real-time visibility, version control nightmares — monday.com is the structured, automated upgrade |
| Vendor management point solutions (Gatekeeper, Beeline) | Specialized vendor or freelancer management | Fragmented approach; monday.com consolidates vendor management with procurement workflow in one platform |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use SAP/Coupa for procurement" | "Those are powerful tools for manufacturing and retail procurement. But in advertising, where you're managing freelancers, media rates, and pitch procurement alongside traditional vendor management, you need a platform that's flexible enough for creative teams to actually adopt. monday.com can complement your existing system for the 80% of procurement activity that lives in spreadsheets and email today." |
| "Procurement isn't strategic enough to justify a new tool" | "At most agencies, procurement manages pass-through billing that represents 60-70% of revenue, freelancer costs that represent 30%+ of project budgets, and SaaS spend that's growing 20%+ annually. That's not back-office — that's a P&L lever. The question isn't whether procurement deserves a tool; it's how much you're leaving on the table without one." |
| "Our procurement team is too small to adopt new software" | "That's exactly the point — a 5-person procurement team managing 500 vendors and $50M in spend can't scale with email and spreadsheets. monday.com automates the repetitive work (onboarding checklists, renewal reminders, compliance tracking) so your small team can focus on negotiation and strategy." |
| "Creative teams won't follow procurement processes" | "They will if the process is as easy as filling out a form and getting a response in hours, not days. The reason creative teams bypass procurement is friction, not rebellion. monday.com removes the friction with intuitive forms, instant status visibility, and automation that makes procurement feel like a service, not a checkpoint." |
| "We can't share vendor rate information across clients due to confidentiality" | "monday.com's permission structure lets you control exactly who sees what. Rate benchmarks can be anonymized (averages, ranges) while keeping specific client-vendor terms restricted to authorized users. You get the intelligence benefits without the confidentiality risk." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for advertising holding company procurement transformation]
- [Placeholder for mid-size agency freelancer management case study]
- [Placeholder for SaaS consolidation ROI example]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
