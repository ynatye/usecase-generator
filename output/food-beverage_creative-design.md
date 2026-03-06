# Food & Beverage × Creative & Design Playbook

## Overview

Creative & Design departments in Food & Beverage companies are the visual engine behind every product that reaches a consumer's hand. Unlike creative teams in tech or professional services, F&B creative departments must produce tangible, physical outputs — packaging that must comply with regulatory requirements, photography that must accurately represent food products (within FTC guidelines), and brand assets that must work across channels from grocery shelf to Instagram to QSR menu boards. A mid-size F&B company with 200-500 SKUs across multiple brands might employ 8-25 in-house creatives (graphic designers, packaging designers, photographers, copywriters, production artists) supplemented by 3-8 external agencies handling brand campaigns, seasonal promotions, and specialty work.

The creative workflow in F&B is uniquely demanding because of the intersection of brand aspirations with regulatory constraints. Every piece of packaging must balance marketing appeal with FDA-mandated Nutrition Facts panels, allergen declarations, ingredient statements, and net weight specifications — all within finite physical space. A cereal box redesign isn't just a creative project; it's a legal, regulatory, and supply chain project with creative at the center. Meanwhile, the pace is relentless: seasonal packaging (holiday editions, back-to-school promotions), limited-time-offer SKUs, retailer-specific variants (Costco multipack packaging, club store displays), and constant reformulations that require packaging updates create a never-ending production queue.

The shift to digital-first marketing has compounded the workload. F&B creative teams now produce assets for e-commerce product detail pages (Amazon A+ Content, Walmart.com, Instacart), social media campaigns, influencer toolkits, digital coupons, retail media network ads (Kroger Precision Marketing, Walmart Connect, Amazon DSP), and direct-to-consumer websites — all while maintaining brand consistency across every touchpoint. The explosion of channels has outpaced headcount growth, leaving creative teams perpetually behind on requests, relying on ad-hoc prioritization, and struggling to maintain quality standards under volume pressure.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | SKU proliferation, channel explosion (e-comm, social, retail media), and seasonal velocity create 3-5x more creative requests than teams can handle at current headcount |
| 2 | Replace or Radically Augment Headcount | High | Production art tasks (resizing, versioning, retailer-specific adaptations) consume 40-60% of designer time; AI and automation can handle bulk production work |
| 3 | Consolidate Tech Stack with AI | Medium | Creative teams juggle project requests via email, asset management in DAM systems, proofing in separate tools, and production tracking in spreadsheets — monday.com unifies the creative workflow |

## Prioritized Use Cases

---

### Use Case 1: Creative Request Intake & Production Workflow

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
F&B creative teams are flooded with requests from every direction: Brand Marketing needs campaign assets, Product Development needs packaging for new launches, Sales needs retailer-specific sell sheets and planograms, Trade Marketing needs point-of-sale displays, E-Commerce needs product images and A+ Content, and Regional teams need localized versions. Requests arrive via email, Slack, hallway conversations, and "urgent" texts from VPs. There's no centralized intake, no standardized briefing, and no transparent prioritization. The result: creative directors spend 30-40% of their time triaging and negotiating priorities rather than directing creative work. Projects start without complete briefs, leading to revision cycles that double production time. And when the CEO's "quick favor" bumps a retailer deadline, nobody downstream knows until it's too late.

#### The Solution
monday.com as the single creative request intake and production management platform. A Creative Request Form captures structured briefs: requesting team, project type (packaging, digital ad, social media, sell sheet, POS display, photography, video), brand, SKU(s) affected, target audience, required deliverables with specifications (dimensions, file formats, retailer requirements), regulatory review needed (yes/no), launch date, and priority justification. Each request becomes a board item flowing through stages: Brief Review → Creative Assignment → Design → Internal Review → Stakeholder Approval → Regulatory Review (if applicable) → Production Art → Final Delivery. Workload views show designer capacity. Automations route requests based on type (packaging → packaging team, digital → digital team), flag requests missing required brief elements, and enforce SLA timelines. Dashboard views give leadership real-time visibility into request volume, throughput, and bottlenecks.

#### The Outcome
Reduce creative request-to-delivery cycle time by 35-45%. Eliminate "lost" requests and surprise priorities (currently 15-20% of requests lack proper tracking). Free creative directors from triage duty, recovering 10-15 hours per week for actual creative leadership. Achieve measurable throughput: track requests completed per designer per week and identify capacity constraints with data rather than gut feel. Enable the team to handle 30-40% more requests without headcount increase.

#### Discovery Questions
1. "How many creative requests does your team receive per week across all brands and channels, and how do those requests come in today?"
2. "What percentage of projects start without a complete creative brief, and how many revision cycles does a typical project go through?"
3. "How does your creative director currently decide what to work on next when everything is marked 'urgent' — is there a framework, or is it relationship-driven?"
4. "When a retailer-specific deadline conflicts with a brand campaign timeline, how is that resolved, and who makes the call?"
5. "Can you tell me right now, without checking, how many projects are in progress, how many are waiting to start, and which designer has the most bandwidth?"

#### Industry Context
F&B creative teams face unique volume drivers that other industries don't. SKU proliferation (flavor extensions, size variants, seasonal editions) multiplies packaging design work. Retailer requirements add complexity: Walmart's packaging specifications differ from Target's shelf-ready packaging requirements, which differ from Costco's club store display needs. Trade promotions (buy-one-get-one shelf tags, end-cap displays, coupon designs) run on 4-6 week cycles with hard retail deadlines. Private label design (for companies that also produce store brands) is a separate workstream with different brand guidelines. The SE should understand that F&B creative teams don't have the luxury of "taking time to get it right" — retail shelf resets and promotional windows are immovable deadlines.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Creative Request & Production Management system for a food and beverage company's creative team. Create a Creative Request Form with fields: Requester Name (people), Requesting Department (dropdown: Brand Marketing, Product Development, Sales, Trade Marketing, E-Commerce, Regional Marketing, Corporate Communications, R&D), Project Type (dropdown: Packaging - New Product, Packaging - Redesign, Packaging - Line Extension, Digital Ad Campaign, Social Media Assets, Sell Sheet/Sales Collateral, Point of Sale Display, Photography, Video, E-Commerce Content, Retailer-Specific, Event/Tradeshow, Other), Brand (dropdown with 5-6 brand names), SKU(s) Affected (text), Project Description (long text), Target Audience (text), Deliverables Needed (long text), Dimensions/Specs (text), File Format Required (dropdown multi-select: PDF, AI, PSD, PNG, JPG, TIFF, MP4, GIF), Retailer Requirements (dropdown: None, Walmart, Target, Costco, Kroger, Amazon, Other), Regulatory Review Required (dropdown: Yes - New Claims, Yes - Reformulation, Yes - New Market, No), Launch/Due Date (date), Priority Justification (long text). Create the main Creative Projects board populated from form submissions with additional columns: Project Status (status: Brief Review, Queued, In Progress, Internal Review, Stakeholder Review, Regulatory Review, Production Art, Final Delivery, On Hold, Cancelled), Assigned Designer (people), Creative Director Approval (status: Pending, Approved, Revisions Needed), Stakeholder Approval (status: Pending, Approved, Revisions Needed), Estimated Hours (numbers), Actual Hours (numbers), Complexity (dropdown: Simple - 2hr, Standard - 8hr, Complex - 24hr, Major - 40hr+). Add automations: when form submitted create item and notify Creative Director; when Project Status changes to Brief Review and Regulatory Review Required is Yes add Regulatory Review step; when Assigned Designer is empty for 2 days notify Creative Director; when Stakeholder Review is Revisions Needed move status back to In Progress and increment a Revision Count column; when all approvals are Approved move to Production Art. Create views: Default Table grouped by Status, Kanban by Status, Workload view by Assigned Designer, Timeline view by due dates, Dashboard with: requests this month by type, average cycle time, projects by brand, designer workload chart, overdue projects list, revision rate percentage."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BriefBot
**Agent Purpose:** Review incoming creative briefs for completeness, flag missing information, and auto-route to the right creative sub-team.

**Triggers:**
- New creative request form submitted
- Project status changed to "Brief Review"
- Manual trigger by Creative Director for brief quality check

**Actions:**
- Analyze brief against completeness checklist by project type (packaging briefs need different fields than social media briefs)
- Flag missing or vague brief elements and auto-request clarification from the requester
- Auto-assign complexity rating based on project type, deliverable count, and timeline
- Route to appropriate sub-team based on project type and current workload
- Check for conflicting deadlines with same brand/SKU projects already in progress
- Generate estimated timeline based on historical project data for similar project types

**Data Required:**
- Brief completeness checklists by project type
- Designer skill profiles and current workload
- Historical project data (cycle times by type and complexity)
- Active project schedule for conflict detection
- Brand guidelines availability status

**Autonomy Level:** Fully Autonomous for routing and flagging
BriefBot autonomously evaluates briefs and routes projects but never assigns priority (that's the Creative Director's call) or rejects requests. It surfaces information to help the CD make faster, better-informed decisions.

**Example Interaction:**
> Trade Marketing submits a request: "Need end-cap display for new BBQ sauce launch at Kroger. Due in 3 weeks." BriefBot analyzes and posts: "Brief Completeness: 45% — Missing: SKU numbers, display dimensions (Kroger standard or custom?), number of facings, flavor variants to feature, promotional pricing to include, photography assets (existing or new shoot needed?), Kroger co-op advertising guidelines. Also flagged: BBQ Sauce packaging redesign is currently in progress (Project #CR-847, due in 2 weeks) — recommend aligning end-cap display timeline with packaging final art. Requesting clarification from Trade Marketing on missing elements. Routed to: Packaging & POS sub-team. Estimated complexity: Standard (8hr) pending dimension confirmation. Suggested timeline: 12 business days from complete brief." The Creative Director sees a clean, actionable summary instead of a vague email thread.

---

### Use Case 2: Packaging Design & Artwork Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Packaging is the F&B creative team's bread and butter — and its biggest bottleneck. A single packaging project involves 10-20 distinct elements: front panel design, back panel layout, ingredient statement placement, Nutrition Facts panel, allergen declaration, UPC/barcode, net weight statement, manufacturing codes area, recycling symbols, certification marks (Organic, Non-GMO Project Verified, Kosher, Halal), brand story copy, usage instructions, and regulatory disclaimers. Each element has different owners (Design owns visual layout, Legal/Regulatory owns compliance elements, Marketing owns claims and copy, R&D owns nutrition data, Supply Chain owns manufacturing codes). Coordinating these stakeholders through email and shared drives leads to version control disasters — the wrong nutrition panel gets printed, an outdated allergen declaration ships, or a certification mark is placed incorrectly. A single packaging error can cost $100K-$500K in reprints and $1M+ if it triggers a recall.

#### The Solution
monday.com as the packaging artwork management system. Each packaging project is an item with structured phases: Design Concept → Layout → Content Population → Internal Review → Regulatory Review → Pre-Press → Print-Ready Approval. Subitems track every packaging element with its owner, status, and version. File columns store artwork versions with clear naming conventions. Approval workflows route packaging through Design → Marketing → Legal/Regulatory → Quality → final sign-off. A "Packaging Specifications" board maintains the master spec for each SKU: dieline dimensions, print method (flexo, litho, digital), substrate, color profiles (Pantone matching), and retailer-specific requirements. Automations prevent packaging from advancing to pre-press without all required regulatory approvals and ensure the most current Nutrition Facts data from R&D is referenced.

#### The Outcome
Reduce packaging design errors reaching print by 90% (from industry average of 5-8% error rate to <1%). Cut average packaging project timeline from 8-12 weeks to 5-7 weeks. Eliminate version control issues — single source of truth for current artwork. Save $200K-$1M annually in avoided reprints and recall-related packaging corrections. Enable the team to manage 50% more packaging projects through structured workflows vs. ad-hoc coordination.

#### Discovery Questions
1. "Walk me through a typical packaging project from design brief to print-ready file — how many people touch it, and how do you manage handoffs?"
2. "When was the last time a packaging error made it to print — what went wrong, and what did it cost to fix?"
3. "How do you ensure the Nutrition Facts panel, ingredient statement, and allergen declaration on packaging match the most current R&D formulation data?"
4. "How many versions of a packaging file typically exist before final approval, and how do you ensure everyone is reviewing the latest version?"
5. "When you have 15 packaging projects running simultaneously across different brands, how do you track which are on schedule and which are at risk of missing their print deadline?"

#### Industry Context
F&B packaging design is highly constrained. FDA mandates minimum font sizes, specific formatting for Nutrition Facts panels (the latest format requires updated Daily Values and the addition of "Added Sugars" line), and prominent allergen declarations. Packaging dielines (the structural template) vary by format: flexible pouches, rigid cartons, cans/bottles (with wrap labels or shrink sleeves), and multi-pack overwraps each have unique design constraints. Print production methods affect design: flexographic printing (most common for flexible packaging) has different color reproduction capabilities than lithographic or digital printing. Pantone color matching is critical for brand consistency — Coca-Cola red, Cadbury purple, and Tiffany blue are trademarked colors. SEs should know that "final artwork" in F&B means a technically production-ready file with correct color separations, trap settings, and dieline specifications — not just a pretty PDF.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Packaging Artwork Management system for a food and beverage creative team. Create a Packaging Projects board with columns: Project Name (text), Brand (dropdown), SKU (text), Packaging Format (dropdown: Flexible Pouch, Rigid Carton, Can/Bottle Label, Shrink Sleeve, Multi-Pack Overwrap, Display Shipper, Corrugated Case, Bag-in-Box), Project Type (dropdown: New Design, Redesign, Line Extension, Regulatory Update, Reformulation Update, Seasonal Variant, Retailer-Specific), Print Method (dropdown: Flexographic, Lithographic, Digital, Gravure), Design Status (status: Brief Received, Concept Development, Layout, Content Population, Internal Review, Regulatory Review, Pre-Press, Print-Ready, Approved for Print, At Printer), Designer (people), Design Reviewer (people), Regulatory Reviewer (people), Marketing Approver (people), Quality Approver (people), Final Approver (people), Design Approval (status: Pending, Approved, Revisions), Regulatory Approval (status: Pending, Approved, Revisions), Marketing Approval (status: Pending, Approved, Revisions), Quality Approval (status: Pending, Approved, Revisions), Print Deadline (date), Launch Date (date), Artwork Version (numbers starting at 1), Artwork File (files), Dieline File (files), Color Profile (dropdown: CMYK, CMYK + 1 Spot, CMYK + 2 Spot, Pantone Only), Substrate (text). Add subitems for packaging elements: Front Panel Design, Back Panel Layout, Nutrition Facts Panel, Ingredient Statement, Allergen Declaration, UPC/Barcode, Net Weight, Certification Marks, Brand Story Copy, Usage Instructions, Recycling Symbols, Manufacturing Code Area — each with Owner (people), Status (status: Not Started, In Progress, Review, Approved), and Source Document (files). Add automations: when all subitem statuses are Approved move Design Status to Internal Review; when Design Status changes to Regulatory Review notify Regulatory Reviewer; when any Approval is Revisions move Design Status back to Layout and increment Artwork Version; when ALL approvals are Approved change Design Status to Print-Ready; when Print Deadline is 14 days away and Design Status is before Pre-Press change to high priority and notify all approvers. Create a Timeline view showing all packaging projects by Print Deadline, a Dashboard with projects by status, average time per phase, projects at risk of missing print deadline, and projects by brand."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** PackCheck
**Agent Purpose:** Automatically review packaging artwork files against regulatory and brand compliance checklists before advancing to pre-press.

**Triggers:**
- Design Status changed to "Internal Review"
- New artwork file uploaded to a packaging project
- Manual trigger by designer requesting pre-flight check
- All subitems marked as Approved

**Actions:**
- Scan uploaded artwork for required regulatory elements: Nutrition Facts panel presence and formatting, allergen declaration placement and formatting, net weight statement, UPC barcode readability
- Cross-reference Nutrition Facts data against latest R&D formulation database to flag discrepancies
- Check brand compliance: logo placement, Pantone color codes, font usage against brand guidelines
- Verify retailer-specific requirements if Retailer-Specific project type (Costco Club Pack dimensions, Walmart shelf-ready packaging specs)
- Generate a "Pre-Flight Report" listing passed checks, warnings, and failures
- Auto-approve routine checks that pass and flag failures for human review

**Data Required:**
- Brand guidelines (logo specs, color palettes, typography rules)
- Current R&D formulation and nutrition data per SKU
- FDA packaging requirements checklist
- Retailer packaging specification documents
- Historical error database for pattern recognition

**Autonomy Level:** Human-in-the-Loop
PackCheck provides automated quality checking but never approves artwork for print. All findings are recommendations for human reviewers. It accelerates the review process by catching obvious errors before human eyes touch the file, reducing review cycles from 3-4 rounds to 1-2.

**Example Interaction:**
> Designer uploads v3 of the "Golden Harvest Honey Almond Granola" flexible pouch artwork. PackCheck runs its analysis in 2 minutes and posts: "Pre-Flight Report — 18 checks performed. PASS: 15 ✓ | WARNING: 2 ⚠️ | FAIL: 1 ❌. FAIL: Allergen declaration lists 'Contains: Wheat, Milk, Almonds' but current R&D formulation (updated Feb 12) also includes Soy (soybean oil added in reformulation). Allergen statement must include Soy. WARNING 1: Net weight font size appears to be 5.5pt — FDA minimum for this package size is 6pt. Please verify. WARNING 2: Pantone 7407C used for honey color accent differs from brand guideline specification of Pantone 7408C — intentional? All other checks passed: Nutrition Facts format compliant, UPC barcode meets GS1 readability spec, organic certification mark correctly placed, recycling symbols present." The designer catches the soy allergen omission before it reaches regulatory review — potentially avoiding a $300K reprint.

---

### Use Case 3: Digital Asset Management & Brand Consistency

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
F&B companies accumulate thousands of digital assets: product photography (hero shots, lifestyle images, ingredient close-ups), packaging artwork files, brand logos and marks, marketing campaign materials, social media templates, sell sheets, trade show booth graphics, and video content. These assets are scattered across designers' local drives, shared network folders, email attachments, agency Dropbox accounts, and maybe an underutilized DAM system. When a regional sales rep needs the latest product photo for a retailer presentation, they either can't find it, find an outdated version, or email the creative team (adding another request to the queue). When a new agency starts work, onboarding them with current assets takes weeks. Brand consistency suffers as teams use old logos, incorrect color values, and outdated product photography.

#### The Solution
monday.com as a lightweight digital asset library and distribution hub. A Brand Asset Library board catalogs all approved assets: asset type (product photo, logo, packaging file, template, video), brand, product/SKU, usage rights (internal only, approved for retail, approved for social, full distribution), file format, dimensions, creation date, expiration date (for seasonal or promotional assets), and the actual files. Views filter by brand, asset type, and usage rights. Connected to the creative production board, new approved assets are automatically added to the library when projects are completed. Automations flag assets approaching expiration, notify teams when updated versions are available, and enforce usage rights (preventing teams from using internal-only assets in external communications). A self-service request form lets non-creative teams find and request assets without emailing the creative team.

#### The Outcome
Reduce "asset request" emails to the creative team by 70% (currently 20-30 per week in a typical mid-size F&B company). Eliminate use of outdated assets in market-facing materials. Cut new agency onboarding time from 2-3 weeks to 2-3 days. Ensure brand consistency across all 15+ channels and touchpoints. Reclaim 5-10 hours per week of designer time currently spent fielding asset requests.

#### Discovery Questions
1. "If I asked five different people in your organization to send me your flagship product's hero image right now, how many different versions would I receive?"
2. "How do your field sales teams and regional marketers currently access approved creative assets — and how confident are you they're using the latest versions?"
3. "When you onboard a new agency, how long does it take to get them all the brand assets and guidelines they need?"
4. "How do you manage usage rights — for example, ensuring product photography licensed for US use only doesn't end up in European marketing materials?"
5. "How many times per week does someone on your creative team get an email asking 'Can you send me the latest [product/logo/image]?'"

#### Industry Context
F&B asset management is complicated by the sheer volume of SKU-level assets. A company with 300 SKUs needs product photography for each (often 4-6 shots: hero, lifestyle, ingredient, on-shelf, multi-pack, e-commerce white background), packaging artwork files in multiple formats (print-ready, web-optimized, retailer specification formats), and potentially ingredient/nutrition images for e-commerce. Seasonal and limited-edition products create assets with expiration dates. Retailer-specific requirements add variants: Amazon requires pure white background product images at minimum 1000x1000px, Walmart requires specific image dimensions for their product pages, and Instacart has its own image specs. Photography licensing adds another layer — images from photo shoots may have usage period limitations or geographic restrictions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Digital Asset Library for a food and beverage company. Create a Brand Assets board with columns: Asset Name (text), Asset Type (dropdown: Product Photography - Hero, Product Photography - Lifestyle, Product Photography - Ingredient, Product Photography - E-Commerce, Packaging Artwork - Print Ready, Packaging Artwork - Web, Logo - Primary, Logo - Secondary, Logo - Icon, Brand Guidelines, Sell Sheet, Social Media Template, Video - Commercial, Video - Social, POS Display Art, Trade Show Graphics), Brand (dropdown with brand names), Product/SKU (text), Usage Rights (dropdown: Internal Only, Approved for Retail, Approved for Social/Digital, Approved for Print Advertising, Full Distribution, Restricted - See Notes), File Format (tags: AI, PSD, PDF, PNG, JPG, TIFF, EPS, MP4, MOV, GIF), Dimensions/Resolution (text), Created Date (date), Expiration Date (date), Season (dropdown: Evergreen, Spring, Summer, Fall/Halloween, Holiday, Back to School, Super Bowl, Other), Status (status: Current, Approved, Needs Update, Expired, Archived), Uploaded By (people), Photographer/Creator (text), License Notes (long text), Asset File (files), Thumbnail Preview (files). Add a connected Asset Requests board with: Requester (people), Department (dropdown), Asset Description (text), Brand (dropdown), Product/SKU (text), Intended Use (dropdown: Retailer Presentation, Social Media Post, Email Campaign, Website, Print Ad, Trade Show, Internal Document, PR/Media Kit), Needed By (date), Request Status (status: Submitted, Found - Sent, Not Available - Creating, Not Available - Declined), Fulfilled By (people), Asset Link (connected board). Add automations: when Expiration Date is 30 days away notify Uploaded By and change Status to Needs Update; when Expiration Date passes change Status to Expired; when creative project marked as Final Delivery create new asset item in library; when Asset Request submitted auto-search library for matching Brand + Product and suggest matches to Fulfiller. Create views: Gallery view with Thumbnail Preview grouped by Brand, Table view filtered by Asset Type, Calendar view of expiration dates. Dashboard with: assets by brand, assets expiring this quarter, request volume by department, most-requested assets."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AssetFinder
**Agent Purpose:** Automatically fulfill asset requests by matching requests to the library, checking usage rights, and delivering approved assets — eliminating creative team involvement for routine asset needs.

**Triggers:**
- New asset request submitted via form
- Team member mentions needing an asset in item updates/comments
- New asset uploaded to library (proactively notify teams who recently requested similar assets)
- Weekly digest of most-accessed and most-requested assets

**Actions:**
- Search asset library matching brand, product/SKU, and intended use against usage rights
- Verify asset is current (not expired or flagged for update)
- Deliver matching assets directly to requester with download links and usage guidelines
- If no match found, create a creative request item with brief pre-populated from the asset request
- Track asset usage patterns to identify gaps in the library (most-requested assets that don't exist)
- Flag potential usage rights violations (e.g., internal-only asset referenced in an external-facing project)

**Data Required:**
- Complete asset library with metadata and usage rights
- Brand guidelines and usage rules
- Requester department and role (to verify access permissions)
- Creative request pipeline (to check if missing assets are already in production)

**Autonomy Level:** Fully Autonomous
AssetFinder independently searches, verifies, and delivers assets for requests that match existing library items with appropriate usage rights. Requests for assets that don't exist are automatically routed to creative intake. No human intervention needed for 70% of routine requests.

**Example Interaction:**
> A Regional Sales Manager in the Southeast submits an asset request: "Need current hero shots and sell sheet for Mountain Spring Sparkling Water — all flavors — for a Publix buyer meeting next Tuesday." AssetFinder searches the library and responds within 30 seconds: "Found 4 matching hero shots (Original, Lemon, Berry, Peach) — all current, approved for retail use. Sell sheet found but flagged: version dated October 2025, and the product line added a Mango flavor in January 2026. Delivering 4 hero shots now. For the sell sheet: (1) Existing sell sheet delivered for immediate use, (2) Created a creative request for updated sell sheet including Mango — estimated delivery: 3 business days. Also found: Publix-specific planogram from September 2025 — may be useful for your meeting. Want me to include it?"

---

### Use Case 4: Campaign & Promotional Asset Production

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
F&B companies run continuous promotional campaigns: seasonal launches (pumpkin spice everything in fall, grilling season in summer), holiday promotions, retailer-specific co-marketing programs (Kroger "Mega Events," Walmart "Rollback" features), new product launches, cause marketing tie-ins, and social media campaigns around food holidays (#NationalPizzaDay, #TacoTuesday). Each campaign requires dozens of creative assets across channels: in-store POS (shelf talkers, end-cap headers, floor graphics), digital ads (multiple sizes for programmatic display), social media (Instagram stories, TikTok formats, Facebook posts), email banners, website hero images, and retailer media network ads. Multiply by brands and SKUs, and a single campaign can require 50-200 individual asset deliverables. Without structured production workflows, campaigns miss deadlines, assets ship with inconsistent messaging, and the creative team burns out during peak seasons.

#### The Solution
monday.com as a campaign production management platform. A master Campaign board tracks all active and planned campaigns: campaign name, brands/products featured, campaign type, channels, launch dates, and overall status. Each campaign links to a Campaign Assets board where every required deliverable is an item: asset name, channel, dimensions, copy (connected to approved messaging), design status, and assigned designer. Templates pre-populate asset requirements by campaign type (a "New Product Launch" template automatically creates items for all standard deliverables). Automations enforce production schedules: asset deadlines cascade backward from campaign launch dates, dependency chains ensure creative doesn't start before copy is approved, and channel-specific review workflows route assets to the right approvers (social team reviews social assets, retail team reviews POS assets). Cross-campaign calendar views prevent resource conflicts.

#### The Outcome
Reduce campaign asset production time by 40% through templated workflows and parallel workstreams. Achieve 100% on-time delivery for retailer co-marketing deadlines (currently 70-80% at most companies). Eliminate duplicated effort when multiple campaigns share brand assets. Improve creative quality by giving designers more time per asset (less time on coordination). Enable 2-3x more campaigns per year without proportional headcount growth.

#### Discovery Questions
1. "How many concurrent promotional campaigns does your creative team typically support, and what does the asset volume look like for a major campaign?"
2. "When you launch a new product, do you have a standard checklist of all creative deliverables needed across channels — or is it rebuilt each time?"
3. "How often do campaign assets miss retailer deadlines, and what's the consequence when that happens?"
4. "How do you manage creative production for seasonal peaks — holiday season, for example — when everything is due at once?"
5. "When a campaign runs across multiple channels, how do you ensure visual and messaging consistency from the shelf to social media?"

#### Industry Context
F&B promotional calendars are driven by retailer planning cycles. Major retailers plan promotional periods 3-6 months in advance, and missing a submission window means missing the promotion entirely. Retailer-specific requirements add complexity: Kroger's "Mega Events" require specific POS dimensions and print specs, Target's seasonal endcaps have unique display configurations, and Costco's sampling program needs dedicated signage. Digital channels add volume but shorter lead times: a social media campaign for #NationalCookieDay might be planned 2 weeks out vs. 3 months for in-store POS. The creative team must manage both long-lead retail production and short-lead digital sprints simultaneously. Trade spending (manufacturer-funded promotions at retail) often exceeds advertising spending in F&B, making promotional asset production a significant business investment, not just a creative exercise.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Campaign Production Manager for a food and beverage creative team. Create a Campaigns board with columns: Campaign Name (text), Campaign Type (dropdown: New Product Launch, Seasonal Promotion, Retailer Co-Marketing, Limited Time Offer, Holiday, Brand Refresh, Cause Marketing, Social Media Campaign), Brands (tags), Products/SKUs (text), Channels (tags: In-Store POS, Digital Display Ads, Social Media, Email, Website, Retailer Media Network, DTC, PR/Media, Sampling/Events), Launch Date (date), End Date (date), Campaign Status (status: Planning, Brief Approved, In Production, Review, Live, Complete, Cancelled), Campaign Lead (people), Creative Lead (people), Total Assets Required (numbers), Assets Complete (numbers), Completion Percentage (formula), Budget (numbers in USD). Create a connected Campaign Assets board: Asset Name (text), Campaign (connected board), Channel (dropdown: Shelf Talker, End Cap Header, Floor Graphic, Banner Ad 728x90, Banner Ad 300x250, Banner Ad 160x600, Instagram Feed, Instagram Story, TikTok, Facebook Post, Email Header, Website Hero, Retailer Media Ad, Coupon, Sell Sheet, Video 15s, Video 30s), Dimensions (text), Copy/Messaging (long text), Assigned Designer (people), Asset Status (status: Waiting on Copy, Ready to Design, In Design, Internal Review, Client/Stakeholder Review, Revisions, Approved, Delivered), Due Date (date), Artwork File (files). Add automations: when new Campaign created from 'New Product Launch' template auto-create 20 standard asset items (3 POS formats, 4 digital ad sizes, 4 social formats, 2 email sizes, 2 website banners, 3 sell sheet formats, 2 video lengths); when Campaign Launch Date is set auto-calculate asset due dates (POS due 6 weeks before, digital due 3 weeks before, social due 1 week before); when asset copy column populated change Asset Status from Waiting on Copy to Ready to Design; when all assets in campaign are Approved update Campaign Status to Review. Create a Campaign Calendar view, a Workload view by designer across all campaigns, and a Dashboard showing: active campaigns by status, asset completion rate per campaign, upcoming deadlines, designer utilization across campaigns."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CampaignOps
**Agent Purpose:** Automate campaign setup, track cross-channel asset production, and proactively identify timeline risks before they become missed deadlines.

**Triggers:**
- New campaign created on Campaigns board
- Campaign Launch Date changed (recalculate all asset deadlines)
- Asset Status changed to "Revisions" (impact assessment on timeline)
- Daily check: any asset due within 5 days still in "Ready to Design" or earlier status
- Weekly: campaign health report generation

**Actions:**
- Auto-generate asset requirement lists based on campaign type and channels selected
- Calculate backward-scheduled deadlines for each asset based on channel lead times
- Monitor production velocity and flag campaigns at risk of missing launch date
- When an asset enters "Revisions," recalculate remaining timeline and alert if deadline is at risk
- Generate weekly Campaign Health Report: on-track vs. at-risk campaigns, designer bottlenecks, approval delays
- Suggest resource reallocation when one campaign is ahead and another is behind

**Data Required:**
- Campaign templates with standard asset lists by type
- Channel-specific lead time requirements (POS: 6 weeks, Digital: 3 weeks, Social: 1 week)
- Designer availability and current workload across all campaigns
- Historical campaign production data (actual vs. planned timelines)
- Retailer submission deadline database

**Autonomy Level:** Escalation-Based
Campaign setup and deadline calculation are fully autonomous. Risk flagging and health reports are autonomous. Resource reallocation is recommended, not executed — the Creative Director makes resourcing decisions. Deadline changes that impact retailer submissions escalate immediately.

**Example Interaction:**
> It's Monday morning and CampaignOps posts the weekly Campaign Health Report: "5 Active Campaigns — Summary: (1) 'Summer Grilling 2026' — ON TRACK ✅ — 34/42 assets complete, all POS assets delivered to retailers, digital ads in final review. (2) 'Mountain Spring Mango Launch' — AT RISK ⚠️ — 8/22 assets complete, 3 POS assets still in design with print deadline in 9 business days. Bottleneck: Designer Jake has 6 assets assigned across 3 campaigns this week. Recommendation: Reassign 2 social media assets (lower priority, flexible deadline) to Designer Maria (capacity available). (3) 'Back to School Lunchbox Promo' — BLOCKED 🔴 — 0/18 assets started, copy approval has been in 'Stakeholder Review' for 11 days. If copy isn't approved by Wednesday, the Kroger POS submission deadline will be missed. Escalating to Campaign Lead and Marketing VP." The Creative Director reviews the report over coffee and takes immediate action on the Mango launch bottleneck and the blocked lunchbox promo.

---

### Use Case 5: Photography & Video Production Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
F&B product photography is a specialized discipline — making food look appetizing while accurately representing the actual product (FTC requires that food photography in advertising not be "materially misleading"). Companies conduct multiple photo shoots per year: new product launches, seasonal campaigns, e-commerce refreshes, menu/recipe photography, lifestyle/brand imagery, and trade show materials. Each shoot involves extensive pre-production (shot list development, prop sourcing, food styling preparation), the shoot itself (often 1-3 days in a studio with a photographer, food stylist, prop stylist, and art director), and post-production (retouching, color correction, cropping for multiple formats). Managing all of this through email and spreadsheets results in missed shots, redundant shoots (because nobody knew a product was already photographed last quarter), and poor utilization of expensive studio time.

#### The Solution
monday.com as a photo/video production management platform. A master Shoots board tracks all planned and completed shoots: shoot name, type (product, lifestyle, recipe, video, UGC-style), studio/location, date(s), crew (photographer, food stylist, prop stylist, art director), associated campaigns/projects, and status. A connected Shot List board details every required shot: product/SKU, shot type (hero, lifestyle, ingredient detail, e-commerce white background, in-use), angle, props needed, food styling notes, and delivery format. Pre-production checklists ensure all products, props, and styling materials are procured before shoot day. Post-production tracking manages retouching status, format exports, and delivery to the asset library. Historical shoot data prevents redundancy: before requesting a new shoot, teams can search for existing photography.

#### The Outcome
Reduce per-shoot cost by 20-30% through better pre-production planning and eliminated redundant shoots. Maximize studio day productivity (capture 30-40% more usable shots per day). Ensure every SKU has current, multi-format photography available. Reduce post-production backlog from 3-4 weeks to 1 week through structured workflows. Create a searchable shoot history that prevents paying twice for the same shot.

#### Discovery Questions
1. "How many product photo shoots does your team conduct per year, and what does a typical shoot day cost all-in (studio, crew, food, props)?"
2. "Has your team ever booked a shoot only to discover the same product was already photographed recently — or conversely, launched a product and realized you don't have e-commerce photography ready?"
3. "How do you currently manage shot lists for a complex shoot — say, 50 products across multiple setups in a 2-day studio session?"
4. "What does your post-production workflow look like — how long from shoot day to final retouched images delivered in all needed formats?"
5. "How do you ensure food photography meets both creative standards and FTC accuracy requirements?"

#### Industry Context
Food photography has unique requirements. FTC regulations prohibit "materially misleading" food advertising — you can use visual enhancement techniques (glycerin for moisture look, motor oil as syrup substitute was common decades ago but is now generally avoided for advertised products), but the photography must reasonably represent what the consumer will receive. E-commerce photography has specific technical requirements by platform: Amazon requires pure white background (RGB 255,255,255), minimum 1000px on longest side, product filling 85% of frame. Studio day rates for food photography range from $3K-$15K depending on market and complexity. A skilled food stylist (essential for making food look appetizing under studio lights) bills $1,500-$3,000/day. These costs make efficient studio utilization a significant financial concern — wasted shoot days hit the budget hard.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Photo & Video Production Manager for a food and beverage creative team. Create a Shoots board with columns: Shoot Name (text), Shoot Type (dropdown: Product Photography, Lifestyle/Brand, Recipe/Editorial, Video - Commercial, Video - Social Content, E-Commerce, Packaging Reference, UGC-Style), Studio/Location (text), Shoot Date(s) (date range or timeline), Photographer (people or text), Food Stylist (text), Prop Stylist (text), Art Director (people), Associated Campaign (connected board), Associated Brand (dropdown), Shoot Status (status: Planning, Pre-Production, Shoot Day, Post-Production, Delivered, Cancelled), Estimated Cost (numbers in USD), Actual Cost (numbers in USD), Total Shots Planned (numbers), Total Shots Captured (numbers), Shots Delivered (numbers). Create a connected Shot List board: Shot Description (text), Shoot (connected board), Product/SKU (text), Shot Type (dropdown: Hero - Front, Hero - Angled, Lifestyle - In Use, Lifestyle - Flat Lay, Ingredient Close-Up, E-Commerce White BG, Recipe/Plated, Packaging Detail, Video B-Roll), Props Needed (long text), Food Styling Notes (long text), Background (dropdown: White, Dark, Wood, Marble, Lifestyle Set, Outdoor), Delivery Formats (tags: High-Res TIFF, Web JPG, E-Commerce PNG, Social Square, Social Vertical, Print CMYK), Shot Status (status: Planned, Captured, In Retouching, Retouched, Format Exports Done, Delivered to Library), Retoucher (people), Notes (long text), Final Files (files). Add automations: when Shoot Status changes to Pre-Production create pre-production checklist subitems (confirm products available, props sourced, food styling materials ordered, equipment reserved, call sheet sent); when Shot Status changes to Delivered to Library create new asset in Brand Assets board; when Shoot Date is 7 days away and any pre-production subitem incomplete notify Art Director. Create views: Calendar view of all shoots, Kanban of shot status, Dashboard with: shoots this quarter, cost per shoot trend, shots planned vs captured vs delivered funnel, post-production turnaround time."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ShootPlanner
**Agent Purpose:** Optimize photo shoot planning by consolidating product photography needs across campaigns, preventing redundant shoots, and maximizing studio day efficiency.

**Triggers:**
- New campaign created that requires photography
- New product launch timeline activated
- Quarterly shoot planning cycle initiated
- Asset request submitted for photography that doesn't exist in library

**Actions:**
- Aggregate all upcoming photography needs across campaigns and product launches
- Cross-reference against existing asset library to identify what's already shot and current
- Recommend consolidated shoot schedules (e.g., "3 campaigns need citrus product photography in March — combine into 1 shoot day instead of 3")
- Generate shot lists based on campaign deliverable requirements and platform-specific format needs
- Estimate shoot costs based on historical data and crew rates
- Create pre-production checklists with product procurement timelines for perishable items

**Data Required:**
- Campaign asset requirements with photography needs
- Existing asset library with shoot dates and currency status
- Product launch calendar
- Photographer/stylist availability and rates
- Studio availability calendar
- Historical shoot data (cost, shots per day by type)

**Autonomy Level:** Escalation-Based
Shoot consolidation recommendations and shot list generation are autonomous. Budget estimates and scheduling suggestions are provided for Art Director approval. The agent never books studios or crew — it provides optimized plans for human decision-making.

**Example Interaction:**
> ShootPlanner detects three upcoming photography needs: (1) Summer Grilling campaign needs lifestyle shots of BBQ sauce line, (2) E-Commerce team needs updated white-background shots for 12 condiment SKUs, and (3) New product launch needs hero photography for Chipotle Ranch dressing. It posts: "Shoot Consolidation Opportunity: All three needs involve condiment/sauce products. Recommendation: Book 1.5 studio days instead of 3 separate sessions. Day 1 AM: E-commerce white BG shots for 12 condiments (including new Chipotle Ranch) — estimated 3 hours at 4 shots/hour. Day 1 PM: Hero product shots for Chipotle Ranch launch — estimated 2 hours, 6 setups. Day 2 AM: Lifestyle grilling shots with BBQ sauce line — outdoor set, estimated 4 hours. Estimated savings vs. separate shoots: $4,200 (one setup/teardown, shared food stylist day). Note: Chipotle Ranch product samples must be available by April 1 — currently showing April 5 on the production calendar. Flagging Product Development to accelerate." The Art Director approves the plan, saving budget and a week of scheduling coordination.

---

### Use Case 6: Brand Guidelines & Template Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
F&B companies with multiple brands (common in mid-market and enterprise) maintain separate visual identity systems for each: logo usage rules, color palettes (primary, secondary, accent), typography hierarchies, photography style guides, packaging design systems, and tone of voice guidelines. These guidelines live in 40-80 page PDF documents that nobody reads, resulting in inconsistent brand execution — especially from non-creative teams who create their own materials (Sales presentations, HR recruitment collateral, investor decks). When brand guidelines are updated (after a brand refresh or acquisition), distributing the updates and ensuring old assets are retired is nearly impossible. The problem compounds with acquired brands that arrive with their own legacy guidelines, asset formats, and naming conventions.

#### The Solution
monday.com as a living brand guidelines hub. A Brand Standards board maintains the current visual identity for each brand: logo files with usage rules (minimum size, clear space, color variations), Pantone/CMYK/RGB/HEX color values, font files and typographic hierarchy, photography style references, and do's/don'ts. Connected template boards provide pre-approved, editable templates for common non-creative-team needs: presentation templates, one-pager templates, email signature graphics, and social media templates with locked design elements and editable content areas. Version control tracks guideline updates with change logs. Automations notify all stakeholders when guidelines are updated and flag assets in the library that may need updating.

#### The Outcome
Achieve 90%+ brand compliance across all departments (vs. typical 50-60% without structured guidelines). Reduce "rogue" off-brand materials created by non-creative teams. Cut brand guideline update distribution from weeks to hours. Enable non-designers to create on-brand materials independently, reducing creative team request volume by 20-30%. Streamline post-acquisition brand integration by having a structured system to onboard new brand identities.

#### Discovery Questions
1. "How many distinct brands does your creative team support, and does each have comprehensive, up-to-date brand guidelines?"
2. "When non-creative teams — Sales, HR, executives — need to create materials, do they use brand-compliant templates, or do they DIY?"
3. "When was the last time you updated your brand guidelines, and how did you distribute the updates across the organization?"
4. "How often do you discover off-brand materials in use — incorrect logos, wrong colors, unauthorized fonts — and what's the process for correcting them?"
5. "If you acquired a new brand tomorrow, how would you integrate their brand assets and guidelines into your systems?"

#### Industry Context
F&B brand management is uniquely complex because brands often span product categories with different visual needs. A beverage brand's identity must work on a 12oz can, a 2-liter bottle, a multipack, a fountain dispenser, a menu board, and a digital ad — each with different space constraints and viewing distances. Color accuracy is critical: a slight shift in a brand's signature color across packaging substrates (glossy carton vs. matte label vs. metallic can) creates perceived inconsistency on the shelf. Many F&B companies manage 3-8 brands, each with sub-brands or product lines (e.g., Original, Light, Zero, Flavored variants) that need visual differentiation while maintaining family resemblance. The SE should understand that brand guidelines in F&B aren't just about aesthetics — they're about shelf impact, consumer recognition, and premium positioning that supports pricing strategy.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Brand Guidelines Hub for a food and beverage company with multiple brands. Create a Brand Standards board with columns: Brand Name (dropdown), Asset Category (dropdown: Primary Logo, Secondary Logo, Icon/Favicon, Color Palette - Primary, Color Palette - Secondary, Typography - Headlines, Typography - Body, Photography Style, Illustration Style, Packaging Design System, Tone of Voice, Do's and Don'ts), Pantone Code (text), CMYK Values (text), RGB Values (text), HEX Code (text), Usage Rules (long text), Current Version (numbers), Last Updated (date), Updated By (people), Asset Files (files), Reference Images (files), Status (status: Current, Under Review, Deprecated). Create a connected Brand Templates board: Template Name (text), Brand (dropdown), Template Type (dropdown: PowerPoint Presentation, Google Slides, One-Pager/Sell Sheet, Social Media - Instagram, Social Media - LinkedIn, Email Signature, Business Card, Letterhead, Trade Show Banner, Product Spec Sheet, Recipe Card), Intended Users (dropdown: Creative Team, Sales, Marketing, HR, Executive, All), Template File (files), Instructions (long text), Download Count (numbers), Template Status (status: Current, Needs Update, Deprecated). Add automations: when Brand Standards Last Updated changes notify all teams via update; when Template Status changes to Needs Update notify Creative Lead; when any Brand Standards Status changed to Deprecated auto-flag assets in Brand Asset Library using same brand for review. Create views: Gallery view grouped by Brand Name showing visual assets, Table filtered by brand for quick reference. Dashboard with: brands overview, templates by type and usage, recently updated standards, deprecated items requiring action."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BrandGuard
**Agent Purpose:** Monitor creative output and organizational materials for brand compliance, flagging deviations before they reach market.

**Triggers:**
- New creative asset uploaded to any project board
- Packaging artwork moved to "Internal Review" status
- Quarterly brand compliance audit scheduled
- New employee onboarded in Marketing, Sales, or Communications departments

**Actions:**
- Compare uploaded assets against brand standards: logo usage, color values (within tolerance thresholds), typography, and photography style
- Generate brand compliance score (0-100) with specific deviation details
- Flag critical brand violations (wrong logo version, off-brand colors) vs. minor issues (suboptimal logo placement)
- For new employees, deliver brand orientation package with current guidelines and available templates
- Compile quarterly brand compliance report showing compliance trends by department and brand
- When brand guidelines are updated, identify all active projects and library assets that may need revision

**Data Required:**
- Brand standards database with all specifications
- Active project boards with uploaded creative assets
- Brand asset library with metadata
- Employee directory with department mapping
- Historical brand compliance audit data

**Autonomy Level:** Fully Autonomous for monitoring and flagging
BrandGuard independently scans and scores all creative output. It never modifies assets or blocks approvals — it provides compliance reports to creative directors and designers who make correction decisions. Critical violations trigger immediate alerts; minor issues are batched into weekly reports.

**Example Interaction:**
> BrandGuard runs a quarterly compliance scan and generates a report: "Q1 2026 Brand Compliance Report — 'Mountain Spring' Brand: Overall Score: 87/100. Issues: (1) 14 Sales presentations using deprecated 2024 logo (pre-refresh) — found in Southeast and Midwest regional folders. Sent individual notifications with updated logo download links. (2) 3 retailer sell sheets using Pantone 3145C instead of brand-specified Pantone 3155C — likely copy/paste error from template. Flagged for Creative Lead correction. (3) LinkedIn social posts consistently using brand font at wrong weight (Regular instead of specified Medium) — recommend updating social media template with correct font weight. (4) Positive: All packaging artwork and digital campaigns are 100% brand compliant. Recommendation: Schedule 30-minute brand refresh training for Sales teams in Southeast and Midwest regions — highest deviation rates."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Dieline | Structural template/outline of a packaging format showing cut lines, fold lines, and printable areas — the blueprint designers work within |
| Flexographic (Flexo) | Most common printing method for flexible packaging (pouches, bags, wrappers) using flexible relief plates — limited color gamut vs. lithography |
| Pantone Matching System (PMS) | Standardized color reproduction system using numbered swatches to ensure color consistency across substrates and printers |
| Trap/Trapping | Overlapping adjacent colors slightly in print files to prevent white gaps from press registration errors |
| Color Separation | Breaking a design into individual color plates (CMYK + spot colors) for the printing process |
| Substrate | The material being printed on — paperboard, film, foil, label stock — each has different ink absorption and color rendering |
| Shrink Sleeve | Printed plastic label that conforms to container shape through heat shrinking — allows 360° decoration on bottles and cans |
| Shelf-Ready Packaging (SRP) | Packaging designed to go directly from shipping case to retail shelf without repacking — increasingly required by major retailers |
| POS (Point of Sale) | In-store marketing materials: shelf talkers, end-cap displays, floor graphics, cooler stickers, and other retail-level signage |
| A+ Content | Amazon's enhanced product detail page format allowing rich media (images, comparison charts, brand story) beyond standard product listings |
| Hero Shot | Primary product photography showing the product at its most appealing — the "money shot" used in key placements |
| Food Styling | Specialized techniques for making food products look appetizing in photography — a distinct skill from general prop styling |
| Trade Dress | Overall visual impression of a product's packaging (shape, color scheme, layout) — protectable as intellectual property |
| Planogram | Retail shelf layout diagram showing exactly where products are placed — creative teams must design packaging to stand out within planogram context |
| Comp/Mock-up | Realistic rendering of how final packaging will look on shelf — used for internal review and retailer presentations before committing to print |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/Director of Creative | Oversees creative strategy, team, and output quality | Decision-maker |
| Creative Director | Day-to-day creative leadership, brand stewardship, project prioritization | Decision-maker/Key champion |
| Senior Packaging Designer | Lead packaging design, dieline expertise, print production knowledge | Key user/Technical evaluator |
| Digital Designer | Social media, web, e-commerce, and digital advertising assets | Key user |
| Production Artist | Final file preparation, versioning, retailer-specific adaptations, pre-press | High-volume user |
| VP of Marketing | Owns brand strategy, campaign planning, budget | Budget approver |
| Brand Manager | Manages individual brand P&L, approves creative for their brand | Stakeholder/Approver |
| Trade Marketing Manager | Plans and executes retailer-specific promotions and POS materials | Major requestor |
| E-Commerce Manager | Manages online product content, A+ Content, digital shelf | Growing requestor |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Marketing | Campaign briefs, brand strategy, messaging approval | Unified campaign-to-creative production workflow |
| Legal/Regulatory | Label compliance review, claims approval, trademark usage | Integrated packaging approval workflow |
| Sales | Sell sheets, retailer presentations, trade show materials | Self-service template portal reduces creative requests |
| R&D/Product Development | New product specs, nutrition data for packaging, formulation changes | Product development-to-packaging pipeline |
| Procurement/Supply Chain | Print vendor management, packaging material specs, production schedules | Packaging production timeline integration |
| E-Commerce | Product photography, A+ Content, digital shelf optimization | Digital asset production and distribution |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Asana | Popular creative project management | monday.com offers superior visual views (Gallery, Kanban), better file management, and the Vibe workflow builder that Asana lacks |
| Wrike | Enterprise creative workflow with proofing | monday.com provides comparable workflow with simpler UX, faster adoption, and broader cross-departmental utility beyond creative |
| Adobe Workfront | Enterprise creative operations (Adobe ecosystem) | monday.com is 60-70% less expensive, deploys in weeks vs. months, and isn't locked into the Adobe ecosystem |
| Bynder/Brandfolder | DAM (Digital Asset Management) | monday.com provides workflow + lightweight DAM in one platform; for heavy DAM needs, integrates with standalone DAM while providing the workflow layer these tools lack |
| Trello | Simple kanban for creative tasks | monday.com scales beyond Trello's limitations with timeline views, workload management, automations, and cross-board dependencies essential for F&B creative complexity |
| Notion | Documentation and lightweight project management | monday.com provides the structured workflow, automations, and reporting that creative production requires — Notion is better for knowledge management than production management |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Adobe Creative Cloud — we don't need another tool" | Adobe CC is where you *create* — monday.com is where you *manage* the creation. Your designers spend 30% of their time not designing: triaging requests, tracking approvals, chasing feedback, finding assets. monday.com gives them that time back by handling everything around the creative work so they can focus on the creative work. It integrates with Adobe CC, not replaces it. |
| "Our creative team is too small for a project management tool" | Small teams need this more, not less. With 5-8 creatives handling 200+ SKUs, you can't afford the overhead of email-based coordination. Every hour spent hunting for the right file version or chasing an approval is an hour not designing. monday.com pays for itself when it saves each designer 3-4 hours per week. |
| "We need a proper DAM, not a project management tool" | If you need heavy-duty DAM with AI tagging, automated format conversion, and CDN delivery, you're right — you need a DAM. But most mid-market F&B creative teams need organized asset storage with workflow attached. monday.com gives you that workflow + organized storage. And when you do invest in a full DAM, monday.com integrates with it and provides the production workflow that DAMs don't offer. |
| "Our designers don't want to learn another tool — they'll just keep using email" | The beauty of monday.com is that requesters fill out forms (no training needed) and designers see a clean board of their assignments. The alternative is 50 emails a day with "URGENT" in the subject line. We've seen creative teams go from resistant to evangelical in 2 weeks because the noise disappears. Start with intake forms — that alone transforms the experience. |
| "We have seasonal spikes that require contract/freelance designers — this adds onboarding friction" | Actually, it eliminates it. When a freelancer joins for holiday season production, they log into monday.com and immediately see their assignments, briefs, brand guidelines, templates, and deadlines — all in one place. Compare that to "here's a shared drive link and someone will email you the brief." monday.com makes freelancer onboarding take hours instead of days. |

## Proof Points
*(To be populated with customer references)*
- [F&B company using monday.com for creative production workflow]
- [CPG creative team managing packaging design on monday.com]
- [Food brand using monday.com for campaign asset production]
- [Multi-brand F&B company centralizing brand guidelines on monday.com]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
