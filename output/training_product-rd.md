# Training × Product & R&D Playbook

## Overview

Product & R&D teams in the training industry are responsible for designing, developing, and continuously improving learning experiences — from instructor-led training (ILT) curricula and eLearning modules to blended programs, micro-learning sequences, and certification pathways. These teams sit at the intersection of instructional design, learning technology, content production, and learner analytics. In mid-market and enterprise training companies, the Product & R&D function may include instructional designers, learning experience designers (LXDs), subject matter expert (SME) coordinators, QA specialists, multimedia producers, and product managers — often 15-60+ people depending on the catalog breadth.

The regulatory and market context is significant: training organizations serving regulated industries (healthcare, financial services, aviation) must align courseware with compliance frameworks like OSHA, HIPAA, FAA, or CE/CPE accreditation standards. Content development cycles are long (8-26 weeks for a full course), review gates are numerous, and version control across languages and modalities is a persistent challenge. Meanwhile, the market is rapidly shifting toward adaptive learning, AI-generated content, and skills-based credentialing — putting immense pressure on R&D teams to innovate faster without inflating headcount.

The typical tech stack includes an LMS (Cornerstone, Docebo, Absorb), authoring tools (Articulate 360, Adobe Captivate, Lectora), video platforms (Camtasia, Synthesia), and project management scattered across spreadsheets, Jira, and email threads. Fragmentation across these tools creates visibility gaps, delays handoffs, and makes it nearly impossible to get a portfolio-level view of the content pipeline.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Training orgs need to produce 2-3× more content to meet demand for digital, micro-learning, and localized programs — without proportionally growing the instructional design team |
| 2 | Replace or Radically Augment Headcount | Medium-High | AI can draft learning objectives, assessment items, storyboards, and even first-pass eLearning scripts — tasks that consume 40%+ of designer time |
| 3 | Consolidate Tech Stack with AI | Medium | Replacing fragmented project tracking (spreadsheets + Jira + email) with a unified content pipeline on monday.com eliminates handoff delays and version confusion |

## Prioritized Use Cases

---

### Use Case 1: Course Development Pipeline Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Most training companies manage their course development lifecycle across spreadsheets, shared drives, and disconnected PM tools. A single course goes through needs analysis → learning design → storyboarding → content development → SME review → QA → pilot → release — often 12+ handoff points. Without a unified pipeline, courses slip deadlines by 3-6 weeks on average, SME review cycles balloon (because reviewers don't know when content is ready), and leadership has zero real-time visibility into where the portfolio stands. When a client requests a custom course variant, there's no way to see which existing modules can be reused.

#### The Solution
monday.com Work Management as the single source of truth for the entire content development lifecycle. Each course is an item on a master **Course Pipeline board** with status columns mapping to ADDIE/SAM phases (Analysis, Design, Development, Implementation, Evaluation). Sub-items represent individual modules or lessons. **Timeline views** show development schedules with dependency tracking. **Automations** trigger SME review requests when a module moves to "Ready for Review," assign QA checklists when development completes, and notify stakeholders when pilot dates are confirmed. **Dashboards** provide portfolio-level views: courses by phase, overdue items, resource utilization by designer, and time-to-completion trends. **monday Docs** embedded in each course item hold the course design document, reducing context-switching to external tools.

#### The Outcome
- 30-40% reduction in course development cycle time through elimination of handoff delays
- 100% visibility into pipeline status for leadership without status meetings
- 50%+ reduction in missed SME review deadlines via automated notifications
- Reusable module identification saves 15-20% of development effort on new courses

#### Discovery Questions
1. "Walk me through what happens from the moment a new course is approved to when it goes live — how many tools and handoffs are involved?"
2. "When your VP of Product asks 'where do we stand on the Q3 course releases,' how long does it take to get an accurate answer?"
3. "How do you currently track SME review cycles? What's the average turnaround vs. your target?"
4. "Do you have visibility into which existing modules could be reused when building a new course, or does each project start from scratch?"
5. "What percentage of your courses miss their target release date, and what's the downstream revenue impact?"

#### Industry Context
Training companies often follow the **ADDIE model** (Analysis, Design, Development, Implementation, Evaluation) or the **SAM model** (Successive Approximation Model) for course development. SME (Subject Matter Expert) review is a critical bottleneck — SMEs are often external contractors or client-side experts who are unresponsive. The distinction between **ILT** (Instructor-Led Training), **VILT** (Virtual ILT), **eLearning**, and **blended** modalities matters because each has different development timelines and resource requirements. **SCORM** and **xAPI** compliance are non-negotiable for LMS-hosted content.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Course Development Pipeline board for a training company. Columns: Course Name (text), Course Code (text), Modality (dropdown: ILT, VILT, eLearning, Blended, Micro-learning), Target Audience (dropdown: Enterprise Clients, SMB Clients, Internal, Public Enrollment), Development Phase (status: Needs Analysis, Learning Design, Storyboarding, Content Development, SME Review, QA, Pilot, Released, Archived), Priority (status: Critical, High, Medium, Low), Assigned Designer (people), SME Reviewer (people), Target Release Date (date), Actual Release Date (date), Estimated Dev Hours (numbers), Actual Dev Hours (numbers), Language (dropdown: English, Spanish, French, German, Mandarin, Multi-language), Accreditation Required (checkbox), Module Count (numbers), Reusable Modules (numbers), Client/Sponsor (text), Revenue Impact (numbers). Create sub-items for individual modules with columns: Module Name, Module Type (dropdown: Lesson, Assessment, Activity, Simulation), Status, Assigned To, Due Date, Duration (minutes). Add automations: when Development Phase changes to SME Review, notify SME Reviewer and set due date to 5 business days out; when Development Phase changes to QA, create QA checklist sub-items (Content Accuracy, Accessibility Check, SCORM Compliance, Brand Compliance, Interactive Element Testing); when Target Release Date is within 7 days and Development Phase is not Released, notify Assigned Designer and manager. Create views: Timeline view grouped by Target Audience, Kanban view by Development Phase, Dashboard with widgets showing courses by phase (pie chart), overdue courses (table), average development time by modality (chart), designer workload (battery), and monthly release velocity (line chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CourseFlow Orchestrator
**Agent Purpose:** Automatically manage course development workflow transitions, chase SME reviewers, and flag at-risk courses before they miss deadlines.

**Triggers:**
- Course item moves to "SME Review" phase
- SME review due date passes without status change
- Course target release date is within 14 days and phase is earlier than QA
- New course item created from intake form
- Weekly schedule (Monday 8 AM) for portfolio health check

**Actions:**
- Send personalized SME review request with direct link to review materials and deadline
- Escalate overdue SME reviews: Day 1 reminder → Day 3 manager CC → Day 5 VP escalation with impact summary
- Auto-generate project timeline based on modality (eLearning = 16 weeks, ILT = 10 weeks, Micro-learning = 4 weeks) and populate milestone dates
- Analyze module library and recommend reusable modules based on topic tags and audience match
- Generate weekly portfolio status summary with at-risk courses, resource bottlenecks, and velocity metrics
- Create QA checklist items when course enters QA phase

**Data Required:**
- Course pipeline board with phase statuses and dates
- SME contact information and review history
- Module library with topic tags and reuse metadata
- Historical development timelines by modality

**Autonomy Level:** Human-in-the-Loop
The agent autonomously sends reminders, generates timelines, and produces status reports. Escalation beyond the first reminder requires human approval. Module reuse recommendations are suggestions, not automatic substitutions. Phase transitions beyond "SME Review → QA" require human confirmation.

**Example Interaction:**
> The CourseFlow Orchestrator detects that "Advanced Compliance Training for Financial Services v3.0" has been in SME Review for 6 days against a 5-day SLA. It sends a second reminder to the SME (Dr. Sarah Chen) with a note: "Hi Dr. Chen — the compliance module review is now 1 day overdue. The course has a hard release date of March 15 tied to a client contract renewal worth $240K ARR. Could you complete your review by Wednesday?" Simultaneously, it flags the course as "At Risk" on the portfolio dashboard and notifies the Product Director: "FYI — Advanced Compliance v3.0 is at risk. SME review overdue by 1 day. If review isn't completed by Wednesday, the QA phase will compress from 10 days to 7, which historically increases revision cycles by 40%. Recommend allocating backup SME Dr. Martinez."

---

### Use Case 2: AI-Assisted Instructional Design & Content Drafting

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Instructional designers spend 40-60% of their time on first-draft activities: writing learning objectives aligned to Bloom's Taxonomy, creating assessment items (multiple choice, scenario-based, matching), drafting storyboards, and writing facilitator guides. For a typical 8-hour eLearning course, the first draft alone takes 80-120 hours of designer time. With demand for content outpacing team capacity by 2-3×, training companies either miss market windows, deliver lower-quality content, or hire expensive contract designers at $85-150/hour. The bottleneck isn't creativity — it's the sheer volume of structured content that must be produced.

#### The Solution
monday.com with **AI Sidekick** and **monday Docs** for AI-assisted content creation integrated directly into the development pipeline. When a designer begins a new module, they use monday Docs with AI to generate first-draft learning objectives from a topic brief, create assessment question banks aligned to each objective, draft storyboard narratives with interaction prompts, and generate facilitator guide outlines. The AI output feeds directly into the pipeline item, so reviews and iterations happen in context. **Dashboards** track AI-assisted vs. manual development time, showing productivity gains. The designer's role shifts from "content creator" to "content curator and quality assurer."

#### The Outcome
- 50-60% reduction in first-draft creation time per module
- 2-3× increase in designer throughput without additional hires
- Estimated savings of $200K-500K/year in contract designer costs for a mid-size training company
- Consistent quality baseline — AI-generated content follows house style and Bloom's alignment rules

#### Discovery Questions
1. "How many instructional designers do you have, and how many courses are in your backlog right now?"
2. "What's the average cost to develop one hour of eLearning content, and how does that compare to your target?"
3. "Are you using any AI tools for content creation today? If so, how integrated are they with your workflow?"
4. "How much of your designers' time is spent on first drafts vs. creative and strategic work like learning experience design?"
5. "If you could double your content output without hiring, what would that mean for your pipeline and revenue?"

#### Industry Context
The industry benchmark for eLearning development is **100-160 hours of development per 1 hour of finished content** (for interactive eLearning). **Bloom's Taxonomy** is the standard framework for writing learning objectives (Remember, Understand, Apply, Analyze, Evaluate, Create). **Storyboarding** in this context means creating the narrative and interaction flow for each screen/slide of an eLearning module, not visual storyboarding. **Facilitator guides** are the instructor manuals for ILT/VILT delivery. **SCORM** (Sharable Content Object Reference Model) packaging is required for LMS deployment.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an AI-Assisted Content Development workspace for a training company. Board 1 — Content Requests: Columns: Request Title (text), Requesting Client (text), Topic Area (dropdown: Compliance, Technical, Leadership, Sales, Safety, Onboarding, Product, Soft Skills), Modality Requested (dropdown: eLearning, ILT, VILT, Micro-learning, Blended), Estimated Duration (numbers, in hours), Priority (status: Urgent, High, Medium, Low), Status (status: New Request, In Analysis, Approved, In Development, Complete), Assigned Designer (people), AI Assist Level (dropdown: Full Draft, Objectives Only, Assessment Only, Manual), Target Completion (date), Budget (numbers). Board 2 — Module Development: Columns: Module Title (text), Parent Course (connect to Board 1), Learning Objectives Count (numbers), Assessment Items Count (numbers), AI Draft Status (status: Not Started, AI Drafting, Designer Review, Approved), Storyboard Status (status: Not Started, AI Draft, Designer Editing, SME Review, Final), Development Hours Saved (numbers, formula comparing AI-assisted vs. benchmark), Notes (long text). Add automations: when a new request is approved on Board 1, create corresponding module items on Board 2 based on Estimated Duration (1 module per hour of content); when AI Draft Status changes to Designer Review, notify Assigned Designer; when all modules for a course reach Approved, update parent course status to Complete. Dashboard: AI productivity metrics — total hours saved (number widget), average draft-to-approval time (chart), modules completed per designer per month (chart), cost savings vs. contract designer rates (number widget calculated at $120/hour saved)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** InstructoBot
**Agent Purpose:** Generate first-draft instructional content (learning objectives, assessments, storyboards) from topic briefs, aligned to Bloom's Taxonomy and house style guidelines.

**Triggers:**
- New module item created on Module Development board
- Designer manually requests "Generate Draft" via button column
- Topic brief document is attached or updated on a module item
- Batch trigger: nightly processing of all modules in "Not Started" AI Draft Status

**Actions:**
- Analyze topic brief and generate 3-5 learning objectives per module aligned to appropriate Bloom's level
- Create 8-12 assessment items per module (mix of multiple choice, scenario-based, true/false, matching) with answer keys and distractor rationale
- Draft storyboard narrative for each screen (estimated 15-20 screens per hour of eLearning) with interaction type suggestions (click-to-reveal, drag-and-drop, branching scenario)
- Generate facilitator guide outline for ILT/VILT modules with timing, activities, and discussion prompts
- Flag content that may require SME validation (technical claims, regulatory references, statistics)
- Update module item with draft content in monday Docs and change AI Draft Status to "Designer Review"

**Data Required:**
- Topic brief (attached document or long text field)
- House style guide (tone, terminology, formatting standards)
- Bloom's Taxonomy alignment rules
- Historical module library for consistency and terminology reference
- Industry/domain-specific glossary for regulated content

**Autonomy Level:** Human-in-the-Loop
InstructoBot generates drafts autonomously but never publishes content without designer review. All AI-generated content is watermarked as "AI Draft — Requires Review" until a designer approves. The designer can accept, modify, or regenerate any section. Assessment items always require human validation before inclusion in final courseware.

**Example Interaction:**
> A designer creates a new module "Anti-Money Laundering Fundamentals — Module 3: Transaction Monitoring" with a 2-page topic brief attached. InstructoBot processes the brief overnight and by morning has generated: 4 learning objectives ("After completing this module, the learner will be able to: 1. Identify the three tiers of transaction monitoring thresholds per FinCEN guidelines [Understand], 2. Analyze transaction patterns to flag suspicious activity reports (SARs) [Analyze]..."), 10 assessment items including a branching scenario where the learner must decide whether to file a SAR based on a realistic transaction pattern, and an 18-screen storyboard with interaction suggestions. The storyboard includes a flag: "Screen 12 references $10,000 CTR threshold — verify this is current per 2026 FinCEN regulations (SME review recommended)." The designer opens the monday Doc, spends 90 minutes refining instead of the usual 6 hours drafting from scratch.

---

### Use Case 3: Learning Program Portfolio Dashboard

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training company executives and product leaders lack a single view of their entire learning portfolio. Course catalogs live in the LMS, development status in spreadsheets, financial performance in the ERP, and learner satisfaction data in survey tools. When the CEO asks "Which of our top 20 courses are due for a refresh, which are our fastest-growing programs, and where should we invest R&D budget next quarter?" — it takes a product manager 2-3 days to compile the answer from 4+ systems. Strategic decisions about what to build next are based on gut feel rather than data. Sunset decisions on underperforming courses are delayed because nobody has a clear picture of utilization vs. maintenance cost.

#### The Solution
monday.com **Dashboards** connected to a master **Learning Portfolio board** that aggregates data from across the organization. Each course/program is an item with metadata: launch date, last refresh date, modality, target audience, development cost, annual maintenance hours, enrollment numbers (synced from LMS via integration), NPS/satisfaction scores, revenue attribution, and competitive positioning. **Formula columns** calculate ROI (revenue ÷ total investment), refresh urgency (months since last update × enrollment volume), and growth rate. **Dashboard widgets** display portfolio health: revenue by program (bar chart), courses overdue for refresh (table filtered by age + enrollment), R&D investment allocation (pie chart), and NPS trends (line chart). **monday Docs** host quarterly portfolio review narratives.

#### The Outcome
- Executive portfolio questions answered in minutes instead of days
- Data-driven R&D prioritization increases revenue impact of new course investments by 20-30%
- Identification of underperforming courses for sunset saves 10-15% of maintenance budget
- Refresh cycle compliance improves from ~60% to 90%+ on-time

#### Discovery Questions
1. "How do you currently decide which courses to invest in developing next? What data informs that decision?"
2. "Can you tell me right now which of your courses have the highest ROI? How about the lowest?"
3. "How often do your courses get refreshed, and is that driven by a schedule or by complaints?"
4. "What's your annual content maintenance burden — hours and cost — and how fast is it growing?"
5. "If you could retire your bottom 10% of courses tomorrow with confidence, how much capacity would that free up?"

#### Industry Context
Training companies track **seat utilization** (enrolled vs. capacity), **completion rates**, **NPS** (Net Promoter Score for learner satisfaction), and **time-to-competency**. Course **shelf life** varies: compliance courses need annual refresh, technical courses refresh every 6-18 months, soft skills courses last 2-3 years. The **build vs. buy vs. license** decision is constant — should we develop in-house, commission from a third party, or license existing content? **Revenue models** include per-seat licensing, subscription, enterprise site licenses, and government/GSA contracts.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Learning Portfolio Management board for a training company's Product & R&D team. Columns: Program Name (text), Course Code (text), Modality (dropdown: eLearning, ILT, VILT, Blended, Micro-learning, Certification Path), Category (dropdown: Compliance, Technical, Leadership, Sales Enablement, Safety, Onboarding, Professional Development), Target Market (dropdown: Enterprise, SMB, Government, Higher Ed, Healthcare, Financial Services), Status (status: Active, In Development, Under Review, Sunset Planned, Archived), Launch Date (date), Last Refresh Date (date), Next Refresh Due (date), Annual Enrollments (numbers), Completion Rate % (numbers), Learner NPS (numbers), Annual Revenue (numbers), Development Cost (numbers), Annual Maintenance Hours (numbers), ROI (formula: Annual Revenue / Development Cost * 100), Refresh Urgency Score (formula: months since Last Refresh × Annual Enrollments / 1000), Competitive Alternatives (text), Product Owner (people), Module Count (numbers). Add automations: when Next Refresh Due is within 30 days and Status is Active, notify Product Owner and create refresh project item on Course Development Pipeline board; when Learner NPS drops below 30, flag item and notify VP Product; when Annual Enrollments are less than 50 and Status is Active for more than 12 months, suggest sunset review. Create Dashboard: Portfolio Overview with total active courses (number), total annual revenue (number), average NPS (number), courses needing refresh (table filtered by Refresh Urgency Score > 50), revenue by category (stacked bar), enrollment trends by quarter (line chart), ROI distribution (histogram), modality mix (pie chart), top 10 courses by revenue (leaderboard), bottom 10 courses by ROI (table for sunset candidates)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio Strategist
**Agent Purpose:** Continuously analyze the learning portfolio and generate actionable recommendations for investment, refresh, and sunset decisions.

**Triggers:**
- Weekly schedule (Friday 3 PM) for portfolio health analysis
- Enrollment data sync completes (from LMS integration)
- Learner NPS scores updated (from survey integration)
- New course reaches 6-month anniversary (maturity milestone)
- Quarterly trigger for comprehensive portfolio review

**Actions:**
- Generate weekly "Portfolio Pulse" report: top movers (enrollment growth/decline), NPS alerts, refresh urgency rankings
- Identify courses where enrollment is declining but maintenance cost is static — recommend sunset or refresh
- Analyze market trends and competitor catalogs to identify content gaps and recommend new course investments
- Calculate optimal refresh schedule based on enrollment volume, NPS trajectory, and regulatory change frequency
- Produce quarterly R&D investment recommendation: "Invest, Maintain, Sunset" classification for every active course with rationale
- Alert when a course's competitive position changes (new competitor offering, regulatory update)

**Data Required:**
- Learning Portfolio board (all metadata)
- LMS enrollment and completion data (via API integration)
- Learner satisfaction surveys (NPS, CSAT)
- Financial data (revenue, development costs, maintenance hours)
- Competitor catalog intelligence (manual or scraped)
- Regulatory update feeds for compliance-heavy domains

**Autonomy Level:** Escalation-Based
The agent produces all analyses and recommendations autonomously. Sunset recommendations require VP Product approval. New course investment recommendations are presented for review at quarterly portfolio meetings. Refresh scheduling is auto-generated but product owners can override. NPS crisis alerts (score < 20) trigger immediate escalation to VP Product.

**Example Interaction:**
> On Friday afternoon, Portfolio Strategist generates the weekly Pulse: "📊 Portfolio Pulse — Week of Feb 16: **Highlight:** 'Data Privacy Fundamentals for Healthcare' enrollments up 47% WoW following the new HHS guidance announcement. Recommend fast-tracking the advanced module currently in backlog (Est. $45K investment, projected $180K first-year revenue based on current trajectory). **Alert:** 'Legacy Project Management Basics v2.1' NPS dropped to 22 (from 38 last quarter) — learner comments cite 'outdated tools and screenshots.' Last refreshed 28 months ago. Recommend: either full refresh ($30K, 8 weeks) or sunset in favor of licensing PMI's updated content ($12K/year). **Sunset Candidate:** 'Introduction to Blockchain for Business' — 23 enrollments last quarter, down from 180 at launch. Market interest has shifted to applied AI courses. Maintenance costs exceed revenue by 3:1. Recommend archival."

---

### Use Case 4: SME Network & Review Workflow Management

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies rely heavily on Subject Matter Experts — often external contractors, client-side professionals, or academic advisors — to validate content accuracy. Managing a network of 50-200+ SMEs is chaotic: availability is tracked in someone's head or an outdated spreadsheet, review assignments are sent via email (and frequently lost), feedback arrives in inconsistent formats (tracked changes, email replies, verbal notes), and payment processing for contracted SMEs is manual. The result: SME review is the #1 bottleneck in course development, adding 2-4 weeks to timelines on average. When a key SME becomes unavailable, there's no easy way to find a qualified replacement.

#### The Solution
monday.com **CRM-style board** for the SME network plus a connected **Review Workflow board**. The SME Directory board tracks: name, expertise domains (multi-select), certifications, availability status, hourly rate, average review turnaround, quality rating, and total reviews completed. When a module needs SME review, an automation creates a review item on the Review Workflow board, matches it to available SMEs based on expertise tags, and sends the review request with materials and deadline. SMEs can respond directly via **monday Forms** or email integration. **Dashboards** show review pipeline status, SME utilization, and bottleneck analysis. **Automations** handle escalation chains and payment trigger notifications.

#### The Outcome
- 40-50% reduction in SME review cycle time through automated assignment and follow-up
- Complete visibility into SME network capacity and expertise coverage
- Elimination of "lost" review requests — 100% tracking from assignment to completion
- 25% reduction in SME-related project delays through proactive capacity planning

#### Discovery Questions
1. "How many SMEs do you work with, and how do you currently track their availability and expertise?"
2. "What's your biggest frustration with the SME review process today?"
3. "How often do SME delays push back your course release dates?"
4. "When an SME becomes unavailable mid-project, how do you find a replacement? How long does that take?"
5. "Do you have visibility into which SMEs consistently deliver quality reviews on time vs. those who don't?"

#### Industry Context
**SMEs** in training can be internal employees, external consultants, industry practitioners, or academic experts. They're typically paid per review ($500-2,000 per course review) or on retainer. **Technical accuracy review** vs. **instructional review** are different — the first checks content correctness, the second checks pedagogical effectiveness. Many training companies maintain **SME pools** organized by domain (e.g., cybersecurity SMEs, healthcare compliance SMEs, financial regulation SMEs). **Review cycles** typically allow 5-10 business days, but actual turnaround averages 12-18 days without active management.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an SME Network Management system for a training company. Board 1 — SME Directory: Columns: SME Name (text), Email (email), Company/Affiliation (text), Expertise Domains (tags: Compliance, Healthcare, Finance, Technology, Safety, Leadership, Manufacturing, Legal, Cybersecurity, Data Privacy), Certifications (text), Availability (status: Available, Busy, On Leave, Inactive), Hourly Rate (numbers), Average Turnaround Days (numbers), Quality Rating (rating 1-5), Total Reviews Completed (numbers), Last Review Date (date), Preferred Review Format (dropdown: Google Docs, Word Track Changes, monday Doc, Video Call), Contract Status (status: Active, Expired, Pending Renewal), Notes (long text). Board 2 — Review Assignments: Columns: Course/Module Name (text), Review Type (dropdown: Technical Accuracy, Instructional Design, Regulatory Compliance, Accessibility, Full Review), Assigned SME (connect to Board 1), Review Status (status: Pending Assignment, Materials Sent, In Review, Feedback Received, Revisions Applied, Approved), Date Assigned (date), Due Date (date), Date Completed (date), Turnaround Days (formula: Date Completed - Date Assigned), Materials Link (link), Feedback Document (file), Payment Status (status: Not Invoiced, Invoiced, Paid), Payment Amount (numbers). Add automations: when Review Status is Pending Assignment for more than 1 day, notify Product Manager; when Due Date is tomorrow and Review Status is still In Review, send reminder to SME; when Due Date passes and Review Status is not Feedback Received, escalate to manager; when Review Status changes to Approved, update SME's Total Reviews Completed and Last Review Date; when Review Status changes to Approved, change Payment Status to Not Invoiced. Dashboard: SME pipeline view — reviews in progress (battery), overdue reviews (table), SME utilization by domain (chart), average turnaround trend (line chart), top-performing SMEs (leaderboard by quality rating)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SME Matchmaker
**Agent Purpose:** Intelligently match courses to the best available SME based on expertise, availability, quality history, and turnaround performance.

**Triggers:**
- New review assignment item created with "Pending Assignment" status
- SME availability status changes to "Available"
- Review assignment overdue by more than 2 days (find replacement)
- Quarterly trigger for SME network health assessment

**Actions:**
- Score and rank available SMEs for each review based on: domain expertise match (40%), historical turnaround (25%), quality rating (25%), and recent workload (10%)
- Send top 3 SME recommendations to product manager for selection, or auto-assign if confidence score > 90%
- When an SME is unresponsive after 2 reminders, identify and suggest replacement SME with minimal ramp-up time
- Generate quarterly SME Network Health Report: coverage gaps by domain, SMEs approaching contract expiration, quality trend analysis
- Track SME feedback patterns to identify SMEs who need calibration (consistently too lenient or too harsh)

**Data Required:**
- SME Directory board (expertise, availability, performance metrics)
- Review Assignment history (turnaround, quality scores)
- Course metadata (domain, complexity level, regulatory requirements)
- SME contract details and payment history

**Autonomy Level:** Human-in-the-Loop
Auto-assignment only when confidence is very high (>90% match score and the SME has completed 5+ successful reviews in the domain). All other assignments are recommendations for the product manager. Replacement SME suggestions require human approval. Network health reports are fully automated.

**Example Interaction:**
> A new review assignment is created for "HIPAA Privacy Officer Certification — Module 7: Breach Notification Requirements." SME Matchmaker analyzes the module's domain tags (Healthcare, Compliance, Data Privacy, Legal) and searches the SME Directory. It returns: "Top 3 SME matches: 1. **Dr. Rachel Torres** (Healthcare Compliance, 4.8★, avg 4.2 days, available) — 96% match. She reviewed Modules 1-5 of this same certification and has deep HIPAA expertise. 2. **James Whitfield, JD** (Data Privacy Law, 4.5★, avg 6.1 days, available) — 82% match. Strong on breach notification specifically but hasn't reviewed this course before. 3. **Dr. Amir Patel** (Healthcare IT, 4.3★, avg 5.0 days, available next week) — 74% match. Good technical depth but less regulatory focus." The product manager selects Dr. Torres, and the agent auto-sends the review package with deadline.

---

### Use Case 5: Learner Feedback Loop & Course Iteration Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies collect learner feedback through post-course surveys, LMS analytics, instructor observations, and client feedback — but this data rarely flows back to the R&D team in a structured, actionable way. Survey results sit in SurveyMonkey, LMS completion data stays in the LMS, and instructor feedback comes via email. When Product & R&D does a course refresh, they're working from anecdotal evidence rather than systematic data. Courses that need urgent updates (because learners are failing a specific assessment at high rates, or NPS dropped after a platform update broke interactions) aren't caught until the next scheduled review.

#### The Solution
monday.com as the **Feedback Aggregation Hub** integrated with survey tools and LMS. A **Learner Feedback board** captures feedback items categorized by course, module, feedback type (content accuracy, UX/interaction, relevance, difficulty, accessibility), severity, and source. **Integrations** with survey platforms (SurveyMonkey, Typeform) and LMS (via API/Zapier) auto-create feedback items when NPS drops below threshold or completion rates fall. **Dashboards** show feedback heatmaps by course and module, trending issues, and correlation between feedback themes and business metrics. When enough feedback accumulates on a specific module, an **automation** triggers a refresh review.

#### The Outcome
- Continuous improvement loop: feedback-to-action cycle reduced from quarterly to weekly
- Early detection of course quality issues before they impact enrollments or renewals
- Data-driven refresh prioritization based on actual learner experience, not assumptions
- 15-20% improvement in learner NPS scores through responsive course updates

#### Discovery Questions
1. "How does learner feedback currently make its way back to your instructional designers?"
2. "Have you ever been surprised by a course's poor performance that you didn't catch early enough?"
3. "Can you correlate learner satisfaction data with specific modules or interactions within a course?"
4. "How do you prioritize which feedback to act on vs. which to file away?"
5. "What's the lag time between collecting feedback and making a course update based on it?"

#### Industry Context
**Level 1 evaluation** (Kirkpatrick Model) measures learner reaction/satisfaction — this is where NPS and post-course surveys live. **Completion rates** below 70% for voluntary courses signal engagement problems. **Assessment pass rates** below 80% on first attempt may indicate content clarity issues rather than learner capability. **xAPI** (Experience API) enables granular tracking of learner interactions (time per screen, interaction attempts, video replay rates) that SCORM cannot capture. The **Net Promoter Score** adapted for training typically asks: "How likely are you to recommend this course to a colleague?"

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Learner Feedback Aggregation board for a training Product & R&D team. Columns: Feedback ID (auto-number), Course Name (connect to Portfolio board), Module/Section (text), Feedback Source (dropdown: Post-Course Survey, LMS Analytics, Instructor Report, Client Feedback, Support Ticket, QA Review), Feedback Type (dropdown: Content Accuracy, Interaction/UX Issue, Difficulty Too High, Difficulty Too Low, Relevance Concern, Accessibility Issue, Technical Bug, Positive Feedback), Severity (status: Critical, High, Medium, Low, Enhancement), Verbatim Feedback (long text), Learner Segment (dropdown: Enterprise, SMB, Individual, Government), Date Received (date), Status (status: New, Under Review, Accepted, In Progress, Resolved, Won't Fix), Assigned To (people), Resolution Notes (long text), Resolution Date (date), Related Course NPS (numbers), Completion Rate at Time (numbers). Add automations: when 3+ feedback items of same Feedback Type exist for the same Course with Severity High or Critical, create a Course Refresh item on the Development Pipeline board and notify Product Owner; when Status changes to Resolved, notify original feedback source if available; weekly digest automation: every Monday, summarize new feedback items by course and type and send to Product team channel. Create Dashboard: Feedback heatmap — items by course × feedback type (table), feedback volume trend (line chart by week), resolution time average (number widget), open vs resolved (pie chart), top courses by feedback volume (bar chart), critical items needing attention (filtered table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Feedback Analyst
**Agent Purpose:** Automatically categorize, prioritize, and synthesize learner feedback into actionable insights for the R&D team.

**Triggers:**
- New feedback item created (from any source integration)
- Batch trigger: daily processing of new survey responses
- LMS alert: completion rate drops >10% for any course week-over-week
- LMS alert: assessment pass rate drops below 75% on any module
- Monthly trigger for comprehensive feedback synthesis

**Actions:**
- Auto-categorize feedback by type and severity using NLP analysis of verbatim comments
- Identify duplicate/related feedback items and cluster them into themes
- Generate weekly "Voice of the Learner" digest: top 5 themes, trending issues, sentiment trends, suggested actions
- When a feedback cluster reaches critical mass (5+ items on same topic), generate a mini-brief for the product team with impact analysis
- Correlate feedback themes with enrollment and NPS trends to quantify business impact
- Suggest specific content revisions based on feedback patterns (e.g., "Module 4 Screen 12-15 consistently cited as confusing — recommend restructuring the branching scenario")

**Data Required:**
- Learner Feedback board (all items)
- LMS analytics data (completion rates, assessment scores, time-on-task)
- Survey response data (raw and aggregated)
- Course Portfolio board (for correlation with business metrics)
- Historical feedback patterns for trend analysis

**Autonomy Level:** Fully Autonomous (for analysis) / Human-in-the-Loop (for actions)
All analysis, categorization, and reporting is fully automated. Content revision suggestions are recommendations only — designers decide what to act on. Critical alerts (completion rate crash, assessment failure spike) are sent immediately without waiting for human approval.

**Example Interaction:**
> Feedback Analyst processes 47 new survey responses for "Cybersecurity Awareness Training for Financial Services v4.0." It identifies a cluster: 12 respondents mentioned difficulty with the phishing simulation in Module 6, with comments like "the scenario was unrealistic — our email system doesn't look like that" and "the correct answer wasn't obvious because our company uses a different reporting process." The agent creates a synthesis: "📋 **Feedback Cluster Alert — Cybersecurity Awareness v4.0, Module 6: Phishing Simulation.** 12/47 respondents (26%) flagged relevance issues with the phishing exercise. Root cause analysis: the simulation uses a generic email client UI that doesn't match the learner's actual environment (most respondents are from enterprise clients using Outlook with Proofpoint). **Recommendation:** Create 3 variant simulations (Outlook+Proofpoint, Gmail+Google Workspace, Generic) and serve the appropriate version based on learner profile. **Impact:** Module 6 has the lowest completion rate in the course (71%) and the highest skip rate on the assessment question tied to this simulation. Fixing this could improve overall course NPS by an estimated 8-12 points."

---

### Use Case 6: Localization & Multi-Language Content Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Global training companies must deliver content in 5-20+ languages. Localization is typically managed through a combination of translation vendors, internal reviewers, and spreadsheet-based tracking. When the English source content is updated, there's no reliable system to flag which translations are now stale. Version mismatches between languages create compliance risks (a Spanish version of a compliance course still references a regulation that was updated in the English version 3 months ago). Coordinating translation workflows across multiple vendors, each with different turnaround times and quality levels, is a project management nightmare.

#### The Solution
monday.com as the **Localization Command Center**. A **Localization Tracking board** connects to the master Course Portfolio board. Each item represents a language variant of a course, with columns for: source language version, target language, translation vendor, translation status, in-country review status, QA status, and publication status. **Automations** trigger when the English source is updated: all connected language variants are flagged as "Stale — Needs Update" with the specific changes highlighted. **Timeline views** show localization schedules across all languages. **Integrations** with translation management systems (memoQ, Smartling) sync status updates. **Dashboards** display localization coverage (which courses are available in which languages), stale translation alerts, and vendor performance metrics.

#### The Outcome
- Zero stale translations in production — every source update triggers localization workflow
- 30% faster localization cycles through automated vendor coordination and parallel workflows
- Complete visibility into language coverage gaps for market expansion planning
- Vendor performance data enables better procurement decisions

#### Discovery Questions
1. "How many languages do you currently support, and how do you manage the translation workflow?"
2. "When you update a course in English, how do you ensure all other language versions get updated too?"
3. "Have you ever had a compliance issue because a translated version was out of date?"
4. "How do you track which translation vendor performs best for which language and domain?"
5. "What's your average time from English source update to all languages published?"

#### Industry Context
**Localization** in training goes beyond translation — it includes cultural adaptation (examples, scenarios, images), regulatory alignment (different compliance requirements by country), and format adaptation (date formats, currency, units). **In-country review** (ICR) is when a native speaker in the target market reviews the translation for accuracy and cultural fit. **Translation memory** (TM) tools reduce cost by reusing previously translated segments. **GILT** (Globalization, Internationalization, Localization, Translation) is the industry framework. Average cost: $0.15-0.30 per word for professional training content translation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Localization Management board for a training company. Columns: Course Name (connect to Portfolio board), Source Version (text, e.g., 'v4.2'), Target Language (dropdown: Spanish, French, German, Portuguese, Japanese, Mandarin, Korean, Arabic, Italian, Dutch, Polish, Hindi), Translation Vendor (dropdown: Vendor A, Vendor B, In-House, Pending Assignment), Word Count (numbers), Translation Status (status: Not Started, In Translation, Translated, In-Country Review, QA, Ready for Publishing, Published, Stale), Source Updated Date (date), Translation Start Date (date), Translation Due Date (date), ICR Reviewer (people), ICR Status (status: Not Needed, Pending, In Review, Approved, Changes Requested), QA Status (status: Not Started, Functional QA, Linguistic QA, Complete), Publication Date (date), Cost (numbers), Stale Flag (status: Current, Stale — Minor Update, Stale — Major Update), Change Description (long text). Add automations: when Source Version changes on connected Portfolio board, set Stale Flag to 'Stale — Major Update' on all connected language items and notify Translation Vendor; when Translation Status changes to In-Country Review, assign ICR Reviewer based on language and notify; when all language variants for a course reach Published status, update master course item with 'Fully Localized' tag; when Translation Due Date is past and status is not Translated or later, escalate to Localization Manager. Views: Timeline grouped by Target Language, Table filtered by Stale Flag, Dashboard with language coverage matrix (table: courses × languages), stale translation alerts (number widget), vendor performance comparison (chart: avg turnaround × quality by vendor), localization pipeline (Kanban by status), monthly cost by language (bar chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LocaleSync
**Agent Purpose:** Monitor source content changes, coordinate localization workflows, and ensure all language variants stay current and compliant.

**Triggers:**
- Source course version updated on Portfolio board
- Translation vendor marks delivery complete
- In-country reviewer completes review
- Weekly schedule: scan for stale translations older than 30 days
- New market launch announcement (new language required across catalog)

**Actions:**
- Analyze source content changes and classify update severity (minor: terminology/date update vs. major: new section/regulatory change)
- For minor updates, generate translation delta (only changed segments) and send to vendor with TM context
- For major updates, generate full retranslation brief with highlighted changes and compliance notes
- Coordinate parallel workflows: trigger all language translations simultaneously and track per-language progress
- Generate localization coverage gap report when new market is announced ("To launch in Japan, 47 of 120 courses need Japanese localization. Priority courses based on market demand: [ranked list]. Estimated cost: $285K. Timeline: 16 weeks for priority tier, 32 weeks for full catalog.")
- Alert when regulatory changes in a specific country may affect localized content (e.g., GDPR update affecting EU versions)

**Data Required:**
- Course Portfolio board with version tracking
- Localization Management board (all language variants)
- Translation memory systems (for delta analysis)
- Vendor contracts (rates, SLAs, language capabilities)
- Regulatory change feeds by country/region

**Autonomy Level:** Escalation-Based
Minor update workflows (terminology, dates) are fully automated through vendor. Major updates require Localization Manager review before vendor assignment. New language launches require VP Product approval. Regulatory alerts are informational — compliance team decides on action.

**Example Interaction:**
> The English source of "Global Anti-Bribery Compliance Training" is updated from v3.1 to v3.2. LocaleSync analyzes the diff: 2 screens updated with new UK Bribery Act 2026 amendment language (major for UK English variant), 1 example scenario changed (moderate for all languages), and 3 minor typo fixes (minor for all). It generates targeted workflows: "UK English variant: Major update — new regulatory language requires certified legal translation. Assigning to Vendor A (legal translation specialist). All other languages: Moderate update — 1 scenario change (342 words) + 3 minor fixes (28 words). Sending delta packages to respective vendors. Estimated cost: £2,100 (UK legal) + $1,850 (all others). Timeline: UK variant 10 days, others 5 days." It creates all workflow items, notifies vendors, and sets up tracking.

---

### Use Case 7: R&D Resource Capacity Planning

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training R&D teams juggle multiple concurrent projects with shared resources — instructional designers, multimedia producers, LMS administrators, and QA specialists. Without capacity planning, teams are either overloaded (leading to burnout and quality issues) or underutilized (wasting budget). When a new high-priority course is requested, the product manager can't quickly answer "Can we take this on? Who's available? What gets pushed?" Resource allocation is done through hallway conversations and gut feel, leading to uneven workloads, missed deadlines, and frustrated team members.

#### The Solution
monday.com **Workload view** and **Resource Planning board** connected to the Course Development Pipeline. Each team member's capacity is defined (e.g., 32 productive hours/week for a full-time designer, accounting for meetings and admin). Course items on the pipeline board have estimated effort by role (designer hours, multimedia hours, QA hours). The **Workload view** shows allocation by person and week, highlighting over-allocation in red. A **What-If Planning board** allows product managers to model scenarios: "If we add Course X to Q2, what happens to the existing schedule?" **Dashboards** display team utilization rates, capacity forecasts, and bottleneck analysis by role.

#### The Outcome
- Realistic project timelines based on actual capacity, not optimistic estimates
- 20-30% improvement in on-time delivery through proactive bottleneck identification
- Reduced designer burnout — overallocation caught before it causes problems
- Faster "can we take this on?" decisions — minutes instead of days

#### Discovery Questions
1. "How do you currently assess whether your team has capacity to take on a new course project?"
2. "What's your team's average utilization rate? Do you know, or is it a guess?"
3. "How often are your designers working on more projects than they should be?"
4. "When priorities shift mid-quarter, how do you rebalance workloads?"
5. "Have you lost team members due to burnout or overwork? What was the cost of replacing them?"

#### Industry Context
**Development ratios** in training: 1 hour of eLearning = 100-160 hours of development (interactive); 1 hour of ILT = 40-80 hours of development; 1 hour of video = 40-100 hours of production. **Instructional designers** typically manage 2-3 concurrent projects. **Multimedia producers** (video, animation, voiceover) are often the scarcest resource. **Seasonal demand** is real: many companies see development spikes in Q1 (new year budgets) and Q3 (pre-compliance deadline pushes). **Contractor augmentation** is common during peak periods.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Resource Capacity Planning system for a training R&D team. Board 1 — Team Roster: Columns: Team Member (people), Role (dropdown: Instructional Designer, Senior Instructional Designer, Multimedia Producer, LMS Administrator, QA Specialist, Project Manager, Contract Designer), Weekly Capacity Hours (numbers, default 32), Current Allocation % (formula from connected projects), Status (status: Available, Fully Allocated, Over-Allocated, On Leave, Contract — Available), Hourly Rate (numbers, for cost modeling), Skills (tags: eLearning, ILT, Video, Animation, Compliance, Technical, Assessment Design, Accessibility, SCORM/xAPI). Board 2 — Project Resource Needs: Columns: Project Name (connect to Course Pipeline board), Role Needed (dropdown matching Team Roster roles), Estimated Hours (numbers), Assigned To (connect to Team Roster), Start Week (date), End Week (date), Actual Hours (numbers), Utilization (formula: Actual/Estimated * 100), Priority (status: Critical, High, Medium, Low). Add automations: when Assigned To person's total allocated hours across all projects exceeds Weekly Capacity Hours × 1.1, flag as Over-Allocated on Team Roster and notify manager; when a new project is added to the Pipeline, create resource need items based on modality template (eLearning: Designer 120h, Multimedia 40h, QA 16h; ILT: Designer 60h, QA 8h). Create Workload view grouped by Assigned To showing weekly allocation. Dashboard: team utilization overview (battery widgets per person), capacity forecast next 8 weeks (stacked bar chart), over-allocated team members (alert table), utilization by role (bar chart), contractor spend (number widget), projects at risk due to resource constraints (filtered table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Capacity Planner
**Agent Purpose:** Continuously monitor team capacity, predict resource conflicts, and recommend optimal project scheduling and team allocation.

**Triggers:**
- New project added to Course Development Pipeline
- Team member status changes (leave, departure, new hire)
- Weekly schedule (Monday 7 AM) for capacity forecast
- Project timeline changes that affect resource needs
- Quarterly trigger for long-range capacity modeling

**Actions:**
- When new project is proposed, instantly model resource impact: "Adding this project would over-allocate Designer A by 15 hours in weeks 12-14. Options: 1) Delay Project X start by 2 weeks, 2) Bring in contract designer ($4,800), 3) Reduce scope of Project Y multimedia from 12 to 8 videos"
- Generate weekly capacity forecast highlighting upcoming bottlenecks 4-8 weeks out
- Recommend optimal project sequencing to maximize utilization while minimizing over-allocation
- Track actual vs. estimated hours and refine future estimates based on historical data
- Alert when utilization consistently exceeds 85% for any team member over 3+ weeks (burnout risk)
- Model hiring scenarios: "If we hire 1 Senior ID, we can absorb 3 additional projects per quarter and reduce contractor spend by $45K"

**Data Required:**
- Team Roster board (capacity, skills, rates)
- Project Resource Needs board (allocations)
- Course Development Pipeline (timelines, priorities)
- Historical project data (actual hours by role and modality)
- HR data (planned leave, open requisitions)

**Autonomy Level:** Human-in-the-Loop
All modeling and recommendations are presented as options — the product manager makes the final call. Burnout alerts are sent automatically. Contractor engagement recommendations require manager approval. The agent never moves project dates or reassigns people without human confirmation.

**Example Interaction:**
> On Monday morning, Capacity Planner delivers the weekly forecast: "🔮 **Capacity Forecast — Weeks 9-16:** ⚠️ **Bottleneck Alert:** Multimedia production hits 142% utilization in weeks 11-13. Three video-heavy courses overlap: 'Advanced Sales Negotiation' (16 videos), 'Cybersecurity Awareness v5' (12 videos), and 'New Hire Onboarding Refresh' (8 videos). **Options:** A) Delay Onboarding Refresh multimedia start by 3 weeks (low business impact — not due until Q3). B) Engage contract video producer for Cybersecurity project ($6,200, 2-week engagement). C) Convert 6 of the Sales Negotiation videos from live-action to screen-capture format (reduces multimedia hours by 40%, minimal quality impact per learner feedback on previous versions). **Recommendation:** Option C + A combined. This resolves the bottleneck completely, saves $6,200 in contractor costs, and only shifts Onboarding by 2 weeks (still ahead of deadline). Shall I update the schedules?"

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ADDIE | Analysis, Design, Development, Implementation, Evaluation — the classic instructional design framework |
| SAM | Successive Approximation Model — an agile alternative to ADDIE with iterative prototyping |
| ILT | Instructor-Led Training — in-person classroom delivery |
| VILT | Virtual Instructor-Led Training — live online delivery (Zoom, Teams, WebEx) |
| SCORM | Sharable Content Object Reference Model — technical standard for eLearning packaging and LMS communication |
| xAPI | Experience API (Tin Can) — next-gen tracking standard that captures granular learner interactions |
| LMS | Learning Management System — platform for hosting, delivering, and tracking training (Cornerstone, Docebo, Absorb) |
| LXD | Learning Experience Design — human-centered approach to designing holistic learning journeys |
| Bloom's Taxonomy | Framework for classifying learning objectives by cognitive level (Remember → Create) |
| SME | Subject Matter Expert — domain specialist who validates content accuracy |
| Storyboard | Screen-by-screen design document for eLearning, specifying content, interactions, and media |
| Kirkpatrick Model | Four-level training evaluation: Reaction, Learning, Behavior, Results |
| Micro-learning | Short, focused learning modules (3-7 minutes) designed for just-in-time consumption |
| Seat Utilization | Ratio of enrolled learners to available capacity in a course offering |
| CPE/CE | Continuing Professional Education / Continuing Education — credits required for professional certifications |
| Facilitator Guide | Instructor manual containing timing, activities, discussion prompts, and delivery notes |
| ICR | In-Country Review — native speaker review of localized content for accuracy and cultural fit |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/Director of Product & R&D | Portfolio strategy, R&D budget, team hiring, build-vs-buy decisions | Decision-maker |
| Senior Instructional Designer | Course architecture, learning strategy, quality standards | Influencer / Technical authority |
| Instructional Designer | Day-to-day content development, storyboarding, assessment creation | Primary user |
| Learning Experience Designer (LXD) | Learner journey mapping, interaction design, UX of learning | Influencer |
| Multimedia Producer | Video, animation, voiceover, interactive media production | User |
| Product Manager | Roadmap prioritization, stakeholder coordination, timeline management | Decision-maker |
| QA Specialist | Content accuracy, accessibility compliance, technical testing | User |
| LMS Administrator | Content publishing, SCORM/xAPI packaging, learner data management | User / Technical gatekeeper |
| SME Coordinator | Managing external expert network, scheduling reviews | User |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Sales | Sales team needs course demos, competitive positioning, and custom proposal content from R&D | CRM for sales pipeline + connected product boards for real-time catalog info |
| Marketing | Marketing promotes courses developed by R&D; needs launch calendars, screenshots, and descriptions | Work Management for coordinated launch campaigns |
| Operations | Operations handles delivery logistics (scheduling, LMS ops) that R&D designs for | Service for learner support tickets feeding back to R&D |
| Customer Success | CS collects client feedback and renewal signals that should drive R&D priorities | CRM + feedback loops to Portfolio board |
| HR | Internal training often shares the same R&D pipeline as external products | Work Management for unified content pipeline |
| Finance | Course development costs, revenue attribution, and ROI analysis all need R&D data | Dashboards connecting development cost to revenue |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Jira | Used by technical training teams for "content as code" workflows | monday.com is more accessible for non-technical IDs, better visual project management, superior dashboards |
| Asana | General task management adopted by smaller training teams | monday.com offers superior portfolio-level views, workload management, and automation depth |
| Smartsheet | Spreadsheet-familiar tool for traditional training PMs | monday.com offers modern UX, better collaboration features, and AI capabilities Smartsheet lacks |
| Wrike | Project management with proofing features for content teams | monday.com's flexibility (especially mondayDB + Vibe) enables custom workflows Wrike can't match |
| Airtable | Database-style tracking for content catalogs | monday.com combines Airtable's flexibility with proper PM features (timeline, workload, automations) |
| Notion | Documentation-heavy teams using it as a wiki + light PM | monday.com excels at structured workflows, automations, and reporting where Notion falls short |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Jira for our development pipeline" | "Jira is great for software sprints, but instructional design workflows have unique needs — ADDIE phases, SME review cycles, multi-modality tracking. monday.com gives your designers a tool built for *their* process, not adapted from engineering. Plus, we integrate with Jira if your tech content team wants to keep it." |
| "Our LMS has built-in project management" | "LMS project features track *delivery* — scheduling, enrollments, completions. They don't manage the *creation* pipeline — storyboarding, SME reviews, localization, resource capacity. monday.com fills the gap between 'we need this course' and 'it's live in the LMS.'" |
| "We need authoring tool integration, not just PM" | "Absolutely — monday.com integrates with your authoring tools through our API and Zapier. When an Articulate project is published, it can auto-update the pipeline status. The goal isn't to replace Articulate — it's to give you visibility across the *entire* workflow, not just the authoring step." |
| "Spreadsheets work fine for our small team" | "They work until they don't — and the breaking point is usually when you're scaling. When you go from 20 courses to 50, or add 3 languages, or onboard 5 new designers, spreadsheets become the bottleneck. monday.com scales with you and costs less than the productivity you're losing." |
| "We can't justify another tool cost" | "Let's quantify it: if your designers save 5 hours/week on status updates, handoff management, and searching for information, that's $15K-25K/year per designer in recovered productivity. For a 10-person team, you're looking at $150K-250K in value from a tool that costs a fraction of that." |

## Proof Points
*(To be populated with customer references)*
- Training companies using monday.com for content development pipeline management
- eLearning organizations that consolidated from Jira + spreadsheets to monday.com
- Multi-language training providers using monday.com for localization workflow
- Certification body managing accreditation workflows on monday.com

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
