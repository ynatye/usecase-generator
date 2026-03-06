# Training × Creative & Design Playbook

## Overview

Creative & Design departments within training companies — including corporate L&D providers, e-learning publishers, professional development firms, and workforce upskilling organizations — are responsible for transforming subject matter expertise into visually compelling, pedagogically sound learning experiences. These teams produce everything from instructor-led training (ILT) slide decks and participant workbooks to fully interactive e-learning modules, microlearning videos, infographics, job aids, and immersive simulations. A mid-size training company may have 8–25 designers managing 40–80 concurrent course development projects across multiple modalities.

The creative pipeline in training is uniquely complex because every asset must satisfy both instructional design standards (ADDIE, SAM, Bloom's Taxonomy alignment) and brand/visual consistency across hundreds of deliverables. Regulatory compliance adds another layer — training for healthcare, finance, or safety must meet SCORM/xAPI packaging requirements, Section 508/WCAG accessibility standards, and industry-specific accuracy reviews. Creative teams coordinate heavily with SMEs, instructional designers, LMS administrators, and client stakeholders, making project visibility and version control critical.

Scale is a persistent challenge: training companies often operate with lean creative teams serving multiple business lines. A single instructional designer may juggle corporate compliance modules, leadership development courses, and technical certification programs simultaneously. Seasonal demand spikes (Q1 planning cycles, regulatory update windows) create bottlenecks that directly impact revenue recognition and client satisfaction scores.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Creative teams are chronically under-resourced relative to course development backlogs; scaling output without proportional headcount is the #1 need |
| 2 | Replace or Radically Augment Headcount | Medium-High | AI can handle templated asset production, first-draft storyboards, and accessibility checks — tasks currently consuming 30-40% of designer time |
| 3 | Consolidate Tech Stack with AI | Medium | Training creative teams typically span 6-10 tools (Articulate, Canva, Adobe CC, Trello, SharePoint, LMS, review tools) creating fragmentation |

## Prioritized Use Cases

---

### Use Case 1: Course Development Pipeline Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Training companies manage dozens of simultaneous course development projects, each moving through analysis, design, development, review, and deployment phases. Without centralized visibility, projects stall in SME review for weeks, creative resources get double-booked, and leadership can't forecast delivery dates. Most teams track this in spreadsheets or basic project tools that don't reflect the actual instructional design workflow — resulting in missed client deadlines and revenue deferrals of $50K–$200K per quarter.

#### The Solution
monday.com Work Management provides a purpose-built course development pipeline with custom statuses mirroring ADDIE/SAM phases, timeline views showing critical path across the entire portfolio, and workload views preventing designer overallocation. Dashboards surface bottleneck stages (e.g., "12 courses stuck in SME review > 5 days"), and automations escalate stalled items. Integration with file storage ensures all storyboards, style guides, and review feedback live alongside the project record.

#### The Outcome
- 35% reduction in average course development cycle time
- 90%+ on-time delivery rate (up from ~65%)
- Real-time portfolio visibility for client-facing teams
- $150K+ annual revenue recovered from eliminated delivery delays

#### Discovery Questions
1. "How many courses are in active development right now, and how do you track which phase each one is in?"
2. "When a course stalls in SME review, how long does it typically sit before someone notices?"
3. "How do you manage designer workload when you have seasonal spikes — like Q1 compliance updates hitting at the same time as new client onboarding?"
4. "What's your current on-time delivery rate, and what does a missed deadline cost you in terms of client relationship or revenue?"
5. "How do you handle scope creep mid-development — does your current system capture change requests and their impact on timelines?"

#### Industry Context
- **ADDIE:** Analysis, Design, Development, Implementation, Evaluation — the dominant instructional design framework
- **SAM (Successive Approximation Model):** Agile alternative to ADDIE, uses iterative prototyping
- Course development cycles typically run 4–16 weeks depending on modality
- SME (Subject Matter Expert) availability is the #1 bottleneck — they're borrowed from other departments
- Revenue recognition often tied to milestone delivery, so delays directly impact quarterly numbers

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a course development pipeline board. Columns: Course Title (text), Client (dropdown: Acme Corp, GlobalTech, HealthFirst, Internal), Modality (dropdown: E-Learning, ILT, Blended, Microlearning, Video), ADDIE Phase (status: Analysis, Design, Storyboard, Development, Alpha Review, Beta Review, QA, Gold Master, Deployed), Priority (status: Critical, High, Standard), Assigned Designer (people), SME Contact (text), Target Launch (date), Estimated Hours (numbers), Hours Consumed (numbers), SCORM Required (checkbox). Add automations: when ADDIE Phase changes to Alpha Review, notify SME Contact and assign a 5-day due date; when item is stuck in any Review phase for more than 5 days, notify the project manager and change Priority to Critical. Create a Timeline view grouped by Client, a Workload view by Assigned Designer, and a Dashboard with widgets showing: courses by ADDIE Phase (chart), overdue items (table), average cycle time by modality (chart), and workload distribution (chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CourseFlow Coordinator
**Agent Purpose:** Automatically monitor course development progress, detect bottlenecks, and proactively manage the pipeline to keep projects on track.

**Triggers:**
- Item stuck in any review phase for more than 3 business days
- Designer workload exceeds 40 allocated hours in a week
- Target Launch date is within 10 business days and ADDIE Phase is before Development
- New course request created via form submission
- Status changed to "Gold Master" (ready for deployment)

**Actions:**
- Send escalation notification to project manager with specific bottleneck details and suggested resolution
- Auto-redistribute workload by suggesting reassignment based on designer availability and skill match
- Generate a risk assessment summary for courses at risk of missing launch dates
- Create QA checklist items when course enters QA phase (accessibility check, SCORM validation, brand compliance, link verification)
- Notify client success team when course reaches Gold Master with deployment instructions
- Generate weekly pipeline health report with velocity metrics

**Data Required:**
- Course development board with complete phase tracking
- Designer capacity and skill profiles
- Client contract data with milestone deadlines
- Historical cycle time data by modality

**Autonomy Level:** Human-in-the-Loop
Bottleneck detection and notifications are fully autonomous. Workload reassignment suggestions require manager approval. Client-facing communications are drafted but require review before sending.

**Example Interaction:**
> On Tuesday morning, CourseFlow Coordinator detects that "HealthFirst Compliance Module 3" has been in SME Review for 4 business days with a target launch in 12 days. It sends the project manager a notification: "⚠️ HealthFirst Compliance Module 3 is at risk. SME review has exceeded the 3-day threshold, and the remaining phases (Development, Alpha, Beta, QA, Gold Master) typically require 14 days for e-learning. Suggested actions: (1) Escalate to HealthFirst's L&D Director for SME prioritization, (2) Begin development on approved sections while awaiting remaining SME feedback." Simultaneously, it notices designer Sarah Chen is at 45 hours next week and flags that her "GlobalTech Leadership Series" storyboard could shift to Marcus (currently at 28 hours) who has leadership development experience.

---

### Use Case 2: Creative Asset Review & Approval Workflow

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every training asset — from a single infographic to a 200-slide course deck — goes through multiple review cycles: instructional accuracy (SME), visual brand compliance (creative lead), accessibility compliance (508/WCAG reviewer), and client approval. Most teams manage this through email threads and shared drives, resulting in lost feedback, conflicting revision requests, version confusion ("Final_v3_REAL_final.pptx"), and 2–3 extra review rounds per asset. For a team producing 150+ assets per month, this wastes 200–400 hours annually in rework and coordination.

#### The Solution
monday.com Work Management creates a structured approval workflow where each asset moves through defined review stages with assigned reviewers, due dates, and consolidated feedback. File annotations and updates keep all versions tracked. Automations route assets to the correct reviewer based on type (e.g., compliance content → legal reviewer automatically), send reminders for pending reviews, and lock items from further editing once approved. Dashboards show approval velocity and reviewer bottleneck metrics.

#### The Outcome
- 50% reduction in review cycle time per asset
- Elimination of "wrong version" errors
- 200+ hours/year recovered from reduced rework and email coordination
- Clear audit trail for regulatory compliance documentation

#### Discovery Questions
1. "Walk me through what happens after a designer finishes a draft — who reviews it, in what order, and how does feedback get consolidated?"
2. "How often do you deal with conflicting feedback from different reviewers — say the SME wants one thing and the brand team wants another?"
3. "For compliance-sensitive content, how do you prove that the right people reviewed and approved each asset?"
4. "What percentage of your assets require more than two review rounds before approval?"
5. "How do you handle client feedback that contradicts your instructional design best practices?"

#### Industry Context
- Section 508 / WCAG 2.1 AA compliance is legally required for government training contracts and increasingly expected for corporate
- SCORM/xAPI packaging has specific technical requirements that must be validated before LMS deployment
- "Alpha review" = internal first look; "Beta review" = client/stakeholder review; "Gold Master" = final approved version
- Training companies often carry E&O (Errors & Omissions) insurance — proper review trails reduce liability exposure

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a creative asset review board. Columns: Asset Name (text), Parent Course (connect boards → Course Pipeline), Asset Type (dropdown: Slide Deck, E-Learning Module, Video, Infographic, Job Aid, Assessment, Facilitator Guide), Review Stage (status: Draft Complete, SME Review, Brand Review, Accessibility Review, Client Review, Revision, Approved, Published), Assigned Designer (people), Current Reviewer (people), Review Due Date (date), Revision Count (numbers), Feedback Summary (long text), Accessibility Score (dropdown: Pass, Conditional Pass, Fail, N/A), File (file column). Add automations: when Review Stage changes to SME Review, assign Current Reviewer to the linked course's SME and set Review Due Date to 3 days from now; when Review Stage changes to Approved, lock the status column and notify the designer; when Review Due Date has passed and Review Stage is not Approved, send reminder to Current Reviewer and notify project manager. Create a Kanban view grouped by Review Stage, and a Dashboard with: assets by review stage (chart), average review duration by asset type (chart), overdue reviews (table), revision count distribution (chart)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ReviewSync
**Agent Purpose:** Orchestrate the multi-stakeholder review process, consolidate feedback, detect conflicts, and ensure compliance checkpoints are never skipped.

**Triggers:**
- Designer marks asset as "Draft Complete"
- Reviewer submits feedback (update posted on item)
- Review Due Date approaching (1 day before)
- Multiple reviewers submit conflicting feedback on same asset
- Asset type is "E-Learning Module" and reaches Approved stage (triggers SCORM validation checklist)

**Actions:**
- Route asset to next reviewer in sequence based on asset type and compliance requirements
- Consolidate feedback from multiple reviewers into a single structured revision brief for the designer
- Flag conflicting feedback and suggest resolution based on priority hierarchy (compliance > instructional accuracy > brand > preference)
- Generate accessibility pre-check report analyzing text contrast ratios, alt-text presence, and reading level
- Create SCORM/xAPI validation checklist when e-learning assets reach final approval
- Produce weekly review velocity report showing average cycle time, bottleneck reviewers, and approval rates

**Data Required:**
- Asset review board with complete reviewer assignments
- Reviewer availability and specialization profiles
- Brand guidelines document (for automated brand checks)
- Accessibility standards checklist (WCAG 2.1 AA criteria)

**Autonomy Level:** Escalation-Based
Routing, reminders, and report generation are fully autonomous. Conflict resolution suggestions require designer/PM decision. Accessibility reports flag issues but human reviewer makes final pass/fail determination.

**Example Interaction:**
> ReviewSync receives feedback on "HealthFirst Hand Hygiene Infographic" from three reviewers. The SME says "Change '5 steps' to '7 steps' per updated WHO guidelines." The brand reviewer says "The blue gradient doesn't match our Q1 palette update." The accessibility reviewer flags "Contrast ratio on step 3 text is 3.8:1, needs 4.5:1 minimum." ReviewSync consolidates these into a structured brief: "Priority 1 (Compliance): Fix contrast ratio on step 3 — current 3.8:1, required 4.5:1. Priority 2 (Accuracy): Update from 5 to 7 steps per WHO 2025 guidelines — this will require layout restructure. Priority 3 (Brand): Update blue gradient to Q1 palette (#2B6CB0 → #3182CE). Note: The 5→7 step change will affect layout — recommend addressing all three in a single revision to avoid extra rounds."

---

### Use Case 3: Learning Asset Digital Asset Management (DAM)

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Training companies accumulate thousands of reusable assets — icons, stock photos, branded templates, character illustrations, video clips, audio narrations — scattered across shared drives, individual machines, Canva accounts, and Adobe libraries. Designers spend 2–4 hours per week searching for existing assets or recreating ones that already exist. When an asset is updated (e.g., brand refresh, product screenshot update), there's no reliable way to find and update every course that uses it. This fragmentation costs $30K–$60K/year in duplicated creative effort for a mid-size team.

#### The Solution
monday.com serves as the central asset registry, cataloging every reusable component with metadata (type, brand, topic, usage rights, expiration date, courses used in). Connected boards link assets to every course that references them, enabling cascade updates. AI-powered tagging suggests categories on upload. Dashboards show asset utilization rates, upcoming expirations (stock photo licenses), and brand compliance status across the library.

#### The Outcome
- 60% reduction in time spent searching for existing assets
- Elimination of duplicate asset creation ($30K–$60K/year saved)
- Instant identification of all courses affected by an asset update
- Automated license expiration tracking prevents legal exposure

#### Discovery Questions
1. "When a designer needs an icon or template, where do they look first — and how long does it typically take to find what they need or determine it doesn't exist?"
2. "After your last brand refresh, how did you identify all the courses and materials that needed updating?"
3. "Do you track stock photo or font license expirations? Has there ever been a compliance issue?"
4. "How much of your designers' time do you estimate is spent recreating assets that already exist somewhere in the organization?"

#### Industry Context
- Training companies may maintain 5,000–50,000+ reusable assets
- Brand refreshes typically happen annually and cascade across hundreds of deliverables
- Stock photo licenses (Getty, Shutterstock) have specific usage terms and expiration dates
- Character consistency is critical in narrative-based e-learning — using the wrong version of a character breaks learner immersion
- SCORM packages bundle assets internally, so updating a source asset doesn't automatically update deployed courses

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a learning asset library board. Columns: Asset Name (text), Thumbnail (file), Asset Type (dropdown: Icon, Illustration, Character, Photo, Video Clip, Audio, Template, Animation, Font, Brand Element), Topic Tags (tags), Brand Version (dropdown: Current, Legacy, Needs Update), License Type (dropdown: Owned, Stock Licensed, Creative Commons, Client Provided), License Expiration (date), Usage Count (numbers), Courses Used In (connect boards → Course Pipeline), Last Updated (date), File Location (link), Accessibility Compliant (checkbox), Designer Owner (people). Add automations: when License Expiration is within 30 days, notify Designer Owner and procurement team; when Brand Version changes to Needs Update, create notification for all connected Course items; when new item created, assign Topic Tags automatically based on Asset Name. Create a Gallery view showing Thumbnails grouped by Asset Type, a table view filtered to License Expiration within 60 days, and a Dashboard with: assets by type (chart), brand compliance status (pie chart), license expirations timeline (timeline), most-used assets top 20 (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AssetIntel
**Agent Purpose:** Intelligently manage the learning asset library — auto-tag uploads, detect duplicates, track usage, and proactively manage license compliance.

**Triggers:**
- New asset uploaded to the library board
- License Expiration date within 30 days
- Brand version marked as "Legacy" after a brand refresh announcement
- Designer searches for an asset (keyword entered in search column)
- Quarterly audit schedule (automated)

**Actions:**
- Auto-tag new assets with topic, style, color palette, and suggested categories based on image/file analysis
- Detect potential duplicates by comparing visual similarity and metadata against existing library
- Generate "cascade impact report" when a brand element changes — listing every course and asset affected
- Recommend existing assets when a designer describes what they need, reducing recreation
- Produce quarterly asset health report: unused assets, expired licenses, brand compliance gaps
- Flag assets approaching license limits (e.g., stock photos with impression caps)

**Data Required:**
- Complete asset library board with metadata
- Course development board (for usage tracking via connected boards)
- Brand guidelines with version history
- License agreements with terms and limits

**Autonomy Level:** Fully Autonomous
Auto-tagging, duplicate detection, and reporting run without human intervention. License renewal recommendations go to procurement for action. Brand cascade reports are generated automatically but remediation requires designer action.

**Example Interaction:**
> A designer uploads a new character illustration named "Dr. Sarah - Lab Coat - Pointing." AssetIntel auto-tags it: Type: Character, Topic: Healthcare/Laboratory, Style: Flat Vector, Palette: Corporate Blue. It then detects a similar existing asset: "Dr. Sarah - Lab Coat - Standing" uploaded 6 months ago and used in 4 courses. It notifies the designer: "Found related character asset 'Dr. Sarah - Standing' (used in HealthFirst Compliance Modules 1-4). Should this new pose be linked to the same character set for consistency tracking?" This ensures character continuity across the entire course catalog.

---

### Use Case 4: Template-Based Rapid Course Assembly

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
80% of training courses follow predictable structures — compliance modules have intro/policy/scenarios/assessment, software training has overview/navigation/task-walkthrough/practice, onboarding has welcome/culture/systems/role-specific. Yet designers build each from scratch, spending 15–25 hours on structural and template work before any custom content begins. For a team producing 40 courses/quarter, that's 600–1,000 hours spent on repetitive scaffolding — the equivalent of a full-time designer doing nothing but templates.

#### The Solution
monday.com with AI capabilities enables templatized course assembly. Course templates are stored as board templates with pre-built task structures, standard assets, and placeholder content. When a new course request comes in, the appropriate template auto-populates based on course type, modality, and client. AI assists in generating first-draft content outlines, placeholder text, and standard assessment questions that designers then customize. This transforms the designer role from "builder" to "editor and enhancer."

#### The Outcome
- 60% reduction in course scaffolding time (15–25 hours → 6–10 hours)
- Consistent structural quality across all courses
- Designers focus on high-value custom content and interaction design
- Capacity increase equivalent to 1.5 FTEs without hiring

#### Discovery Questions
1. "What percentage of your courses follow a standard structure — like compliance, software training, or onboarding templates?"
2. "How long does it typically take from 'new course request' to 'designer starts custom content work'?"
3. "Do you have standardized templates today, and if so, how often are they actually used versus designers starting from scratch?"
4. "If your designers could skip all the scaffolding and start directly on custom content and interaction design, what would that mean for your throughput?"

#### Industry Context
- Bloom's Taxonomy levels (Remember → Evaluate → Create) dictate assessment question types
- Compliance courses require specific legal language, attestation flows, and audit-ready completion tracking
- "Rapid authoring" tools (Articulate Rise, Lectora) have templates but don't connect to project management
- The industry standard is ~40 development hours per 1 hour of e-learning content

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a course template library board. Columns: Template Name (text), Course Type (dropdown: Compliance, Software Training, Onboarding, Leadership Development, Technical Certification, Soft Skills, Safety), Modality (dropdown: E-Learning, ILT, Blended, Microlearning, Video), Estimated Dev Hours (numbers), Standard Sections (long text), Required Assets (long text), Assessment Types (dropdown: Multiple Choice, Scenario-Based, Performance Checklist, Knowledge Check, Simulation), Bloom's Level Target (dropdown: Remember, Understand, Apply, Analyze, Evaluate, Create), Accessibility Requirements (status: Standard, Enhanced, Government), Times Used (numbers), Last Updated (date), Template Owner (people), Template File (file). Add automations: when a new item is created on the Course Pipeline board, suggest matching template based on Course Type and Modality; when Times Used reaches 10, notify Template Owner for review and optimization. Create a Gallery view grouped by Course Type, and a Dashboard with: templates by type (chart), usage frequency (bar chart), average dev hours saved per template (numbers widget), most popular templates (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CourseForge
**Agent Purpose:** Automatically assemble first-draft course structures from templates, generate placeholder content, and pre-populate standard elements so designers jump straight to customization.

**Triggers:**
- New course request submitted via intake form
- Course type and modality selected on a new item
- Client selects "rush delivery" priority
- Template updated (propagate changes to in-progress courses using that template)

**Actions:**
- Match incoming course request to optimal template based on type, modality, audience, and compliance requirements
- Generate complete course outline with section headers, learning objectives (aligned to Bloom's), and time allocations
- Pre-populate standard content blocks: welcome text, navigation instructions, assessment instructions, completion certificates
- Generate first-draft assessment questions appropriate to Bloom's level and topic
- Create the full task breakdown on the Course Pipeline board with estimated hours per section
- Alert designer with a "Course Assembly Complete" summary: "Template applied, 14 sections created, 8 standard assets attached, 12 placeholder assessment questions generated — ready for customization"

**Data Required:**
- Course template library with all standard structures
- Course intake form data (type, audience, objectives, client requirements)
- Historical course data for time estimation
- Assessment question bank by topic and Bloom's level

**Autonomy Level:** Human-in-the-Loop
Template matching and outline generation are autonomous. Generated content is always marked as "AI Draft — Requires ID Review." Assessment questions require instructional designer validation before inclusion. Client-specific customization requirements are flagged for human attention.

**Example Interaction:**
> A new course request arrives: "GlobalTech Annual Cybersecurity Awareness Training — E-Learning — 45 minutes — All Employees." CourseForge identifies the best match: Compliance E-Learning Template (used 23 times, avg satisfaction 4.6/5). It generates a complete structure: 7 sections (Welcome & Objectives, Phishing Awareness, Password Hygiene, Social Engineering, Data Handling, Incident Reporting, Assessment & Attestation), each with learning objectives mapped to Bloom's "Apply" level. It pre-populates 15 scenario-based assessment questions from the cybersecurity question bank, attaches 8 standard brand assets, and creates 18 tasks on the pipeline board with a total estimate of 42 hours. The assigned designer receives: "Course scaffolding complete. Focus areas for customization: GlobalTech-specific phishing examples (Section 2), their incident reporting portal screenshots (Section 6), and CEO welcome video placeholder (Section 1)."

---

### Use Case 5: Client Feedback & Revision Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Client feedback on training deliverables arrives through scattered channels — email threads, marked-up PDFs, Zoom call notes, LMS comments, and verbal requests. Creative teams spend significant time consolidating, deduplicating, and prioritizing feedback before acting on it. Worse, feedback gets lost, leading to client frustration ("I already told you about this in the last review cycle"). For a team managing 15–20 active clients, this coordination overhead consumes 10–15 hours/week and is the #1 source of client escalations.

#### The Solution
monday.com provides a centralized client feedback portal where all feedback — regardless of source — is captured as structured items linked to specific courses and assets. Clients can submit feedback directly through monday.com forms or a shared board view, eliminating email chains. Each feedback item tracks status (Received, Triaged, In Progress, Resolved, Verified), priority, and resolution details. Automations acknowledge receipt, route feedback to the right designer, and alert PMs when items are overdue.

#### The Outcome
- 70% reduction in feedback coordination time
- Zero lost feedback items (complete audit trail)
- Client satisfaction improvement from transparent status visibility
- 40% faster revision turnaround time

#### Discovery Questions
1. "When a client sends feedback on a draft, how does it get to the designer who needs to act on it?"
2. "Has a client ever escalated because feedback they provided was missed or not addressed?"
3. "How do you prioritize when multiple clients have revision requests at the same time?"
4. "Do your clients currently have any visibility into the status of their feedback, or do they have to ask?"

#### Industry Context
- Training clients often have 3–5 stakeholders reviewing content (L&D lead, compliance officer, department head, executive sponsor, legal)
- "Rounds" of revision are typically contractually limited (e.g., "2 rounds of revision included; additional rounds at $X/hour")
- Scope creep through feedback is the #1 margin killer in training companies
- Client feedback often reveals misalignment that happened during the analysis phase

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a client feedback tracker board. Columns: Feedback Item (text), Client (dropdown: Acme Corp, GlobalTech, HealthFirst, ManuCo), Course (connect boards → Course Pipeline), Asset Affected (connect boards → Asset Review), Feedback Source (dropdown: Email, Portal Form, Review Meeting, LMS Comment, Marked PDF), Priority (status: Critical, High, Medium, Low), Feedback Type (dropdown: Content Accuracy, Visual/Brand, Functionality, Accessibility, Scope Change), Revision Round (numbers), Status (status: Received, Triaged, In Progress, Resolved, Client Verified), Assigned Designer (people), Client Contact (text), Date Received (date), Date Resolved (date), Resolution Notes (long text). Add automations: when new item created, send acknowledgment email to Client Contact with expected response time; when Status is In Progress for more than 3 days, notify project manager; when Revision Round exceeds 2, flag as 'Out of Scope' and notify account manager; when Status changes to Resolved, notify Client Contact for verification. Create a table view grouped by Client, a Kanban view by Status, and a Dashboard with: open feedback by client (chart), average resolution time (numbers), feedback by type (pie chart), out-of-scope items (table)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FeedbackDigest
**Agent Purpose:** Capture, consolidate, and intelligently route client feedback while tracking revision scope and contract compliance.

**Triggers:**
- Email received from client stakeholder (via email integration)
- Form submission on client feedback portal
- Meeting notes posted with action items tagged
- Revision Round exceeds contractual limit
- Feedback item unresolved for more than 5 business days

**Actions:**
- Parse incoming feedback (email, form, notes) and create structured feedback items with auto-categorization
- Deduplicate feedback by comparing new items against existing open items for the same course
- Route feedback to the correct designer based on course assignment and feedback type
- Generate revision scope report when approaching contractual round limits
- Draft client status update emails summarizing all open feedback and current status
- Escalate stalled items with context to project manager

**Data Required:**
- Client feedback board with complete history
- Course pipeline board (for designer assignments)
- Client contract data (revision round limits, SLAs)
- Email integration for automated capture

**Autonomy Level:** Escalation-Based
Feedback capture, categorization, and routing are fully autonomous. Scope change flagging and client communications are drafted but require PM review. Contract enforcement decisions always escalate to account management.

**Example Interaction:**
> FeedbackDigest receives an email from HealthFirst's compliance officer: "The hand hygiene module needs to reflect the updated CDC guidelines from January. Also, can we change the background music? It's distracting." The agent creates two feedback items: (1) "Update CDC guidelines reference — Priority: Critical, Type: Content Accuracy, Round: 1" and (2) "Change background music — Priority: Low, Type: Visual/Brand, Round: 1." It routes #1 to the assigned SME reviewer and designer simultaneously (compliance-critical), and #2 to the designer only. It also checks: "Note — this is HealthFirst's 2nd round of feedback on Module 3. Contract allows 2 rounds. Next revision request will trigger out-of-scope notification to Account Manager."

---

### Use Case 6: Accessibility Compliance Automation

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Every training asset destined for government contracts, large enterprises, or public-facing use must meet WCAG 2.1 AA (and increasingly AAA) accessibility standards. Manual accessibility auditing — checking color contrast ratios, alt-text completeness, reading order, keyboard navigation, caption accuracy — takes 3–6 hours per e-learning module. With 20+ modules per quarter needing compliance verification, teams either dedicate a specialist (expensive) or skip thorough checks (risky — ADA lawsuits in training exceeded $2B in settlements industry-wide). Most teams do inconsistent spot-checks and hope for the best.

#### The Solution
monday.com serves as the accessibility compliance hub, with a structured checklist for every asset type mapped to WCAG criteria. AI-assisted pre-screening analyzes uploaded assets for common issues (contrast ratios, missing alt-text, reading level complexity) and generates a preliminary compliance report. Items that fail pre-screening are automatically flagged and routed to the accessibility specialist. Dashboards provide portfolio-wide compliance status for audit readiness.

#### The Outcome
- 50% reduction in manual accessibility audit time
- 100% of assets receive at least automated pre-screening (vs. spot-checks)
- Audit-ready compliance documentation at all times
- Reduced legal exposure from comprehensive coverage

#### Discovery Questions
1. "What percentage of your training content needs to meet formal accessibility standards — WCAG 2.1 AA or Section 508?"
2. "Do you have a dedicated accessibility reviewer, or is it part of someone's other responsibilities?"
3. "If you had to produce an accessibility compliance report for your entire portfolio today, how long would it take?"
4. "Have you or your clients ever faced an accessibility complaint or audit? What was the impact?"

#### Industry Context
- Section 508 applies to all federal government training contracts
- WCAG 2.1 AA is the current standard; AAA is aspirational but increasingly requested
- Common failures: insufficient color contrast (4.5:1 minimum for normal text), missing alt-text on images, non-sequential reading order, auto-playing media without controls
- VPAT (Voluntary Product Accessibility Template) documentation is required for many enterprise and government RFPs
- E-learning authoring tools (Articulate, Captivate) have built-in accessibility features but don't guarantee compliance

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an accessibility compliance tracker board. Columns: Asset Name (text), Course (connect boards → Course Pipeline), Asset Type (dropdown: E-Learning Module, Video, PDF, Slide Deck, Job Aid, Assessment), Compliance Standard (dropdown: WCAG 2.1 AA, WCAG 2.1 AAA, Section 508, None Required), Auto-Scan Result (status: Pass, Issues Found, Failed, Pending Scan), Manual Review Status (status: Not Started, In Review, Pass, Conditional Pass, Fail), Contrast Check (checkbox), Alt Text Check (checkbox), Reading Order Check (checkbox), Keyboard Navigation Check (checkbox), Caption Accuracy Check (checkbox), Issues Found (numbers), Issue Details (long text), Reviewer (people), Review Date (date), Remediation Due (date), VPAT Status (status: Not Needed, Draft, Complete). Add automations: when new asset is linked from Course Pipeline, set Compliance Standard based on Client's requirements; when Auto-Scan Result is Issues Found, assign to Reviewer and set Remediation Due to 5 days out; when all checkboxes are checked and Manual Review Status is Pass, update the source asset's Accessibility Compliant column. Create a table view filtered to Issues Found > 0, and a Dashboard with: compliance status by standard (chart), common issue types (pie chart), assets pending review (table), portfolio compliance percentage (numbers widget)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** A11yGuard
**Agent Purpose:** Automate accessibility pre-screening, maintain compliance documentation, and ensure no asset ships without meeting required standards.

**Triggers:**
- Asset uploaded or updated on Asset Review board
- Course enters "QA" phase on Course Pipeline
- Client contract specifies accessibility standard (new course setup)
- Quarterly compliance audit schedule
- WCAG standard updated (manual trigger for re-evaluation)

**Actions:**
- Run automated accessibility pre-screen on uploaded assets (contrast analysis, alt-text detection, reading level assessment)
- Generate preliminary compliance report with specific pass/fail per WCAG criterion
- Create remediation task list with specific instructions for each failed criterion
- Auto-populate VPAT template with test results and compliance status
- Generate portfolio-wide accessibility dashboard data
- Alert when assets are about to ship without completing accessibility review

**Data Required:**
- Asset review board with file attachments
- Compliance standard requirements per client/contract
- WCAG 2.1 criteria checklist database
- Historical remediation data (common fixes by asset type)

**Autonomy Level:** Human-in-the-Loop
Automated scanning and report generation are autonomous. All pass/fail determinations require human accessibility reviewer confirmation. VPAT documentation is auto-drafted but requires specialist sign-off before client delivery.

**Example Interaction:**
> A11yGuard scans the newly uploaded "ManuCo Safety Orientation Module" (WCAG 2.1 AA required per contract). The auto-scan identifies 4 issues: (1) Slide 7 header text contrast is 3.2:1 (needs 4.5:1) — "Change #8B8B8B to #595959 or darker," (2) Slides 12, 15, 23 missing alt-text on equipment photos, (3) Video segment at 4:32 has no captions for 18 seconds during machine noise, (4) Assessment drag-and-drop interaction has no keyboard alternative. It creates 4 remediation items, estimates 3 hours of fix time, and routes to the designer with: "3 quick fixes (contrast + alt-text + captions) and 1 interaction redesign needed. The drag-and-drop on the assessment needs a keyboard-accessible alternative — suggest converting to a matching dropdown exercise. Remediation due in 5 business days to maintain launch timeline."

---

### Use Case 7: Multi-Language & Localization Workflow

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Global training companies frequently localize courses into 5–20 languages. The localization workflow is nightmarish: extract text strings, send to translators, receive translations in varied formats, re-integrate into authoring tools, adjust layouts for text expansion (German is ~30% longer than English), re-record or source voiceovers, re-test, get local market approval. A single course localized into 10 languages generates 200+ coordination tasks. Most teams track this in spreadsheets, leading to missed strings, version mismatches, and launches delayed by weeks.

#### The Solution
monday.com manages the complete localization pipeline: each source course spawns language-specific sub-items tracking every localization task. Automations manage the handoff chain (extract → translate → review → integrate → QA → approve per language). Dashboards show completion status across all languages simultaneously, highlight bottleneck languages, and forecast delivery dates. Integration with translation management systems (TMS) can automate string extraction and re-integration.

#### The Outcome
- 40% reduction in localization project management overhead
- Parallel tracking of all target languages in a single view
- Automated handoff chains eliminate "waiting for someone to notice it's ready"
- Consistent quality through structured QA gates per language

#### Discovery Questions
1. "How many languages do you typically localize into, and how do you track the status of each language version?"
2. "What's your biggest localization bottleneck — translation turnaround, voiceover recording, layout adjustment, or QA?"
3. "When you launch a course update, how long does it take for all language versions to be updated?"
4. "Have you ever launched a localized version with missing translations or incorrect text because of a tracking gap?"

#### Industry Context
- Text expansion: German +30%, French +20%, Asian languages may be shorter but require different typography
- RTL (right-to-left) languages (Arabic, Hebrew) require complete layout mirroring
- Voiceover localization adds 2–4 weeks per language
- Machine translation (MT) + human post-editing is increasingly common for cost efficiency
- Cultural adaptation goes beyond translation — examples, scenarios, and imagery must be locally appropriate
- Common TMS tools: Smartling, Lokalise, Phrase, memoQ

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a localization tracking board using sub-items. Main item columns: Source Course (connect boards → Course Pipeline), Source Language (dropdown: English US, English UK), Target Languages (tags), Total Strings (numbers), Launch Deadline (date), Localization PM (people), Overall Status (status: Planning, In Progress, QA, Complete). Sub-item columns (one per language): Language (dropdown: Spanish, French, German, Portuguese, Japanese, Mandarin, Korean, Arabic, Italian, Dutch), Translation Status (status: Not Started, Extracting, Translating, Reviewing, Integrated, QA, Approved), Voiceover Status (status: N/A, Script Sent, Recording, Editing, Complete), Layout Adjusted (checkbox), Strings Translated (numbers), Translator (people), VO Artist (text), Language QA (people), Target Complete Date (date). Add automations: when Translation Status changes to Reviewing, notify Language QA; when all sub-items have Translation Status = Approved AND Voiceover Status = Complete or N/A, change main item Overall Status to Complete; when Target Complete Date has passed and Translation Status is not Approved, escalate to Localization PM. Create a table view with sub-items expanded, and a Dashboard with: languages by status (stacked bar chart), overdue languages (table), average localization cycle time by language (chart), overall completion percentage (progress bar)."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LocaleSync
**Agent Purpose:** Orchestrate multi-language localization workflows, track progress across all target languages, and proactively manage the translation-to-deployment pipeline.

**Triggers:**
- Source course marked as "Gold Master" (ready for localization)
- Translation file received from translator/TMS
- Voiceover recording delivered
- Target Complete Date approaching (3 days before)
- Source course updated after localization has begun

**Actions:**
- Auto-generate sub-items for each target language when localization kicks off, with pre-populated deadlines based on historical cycle times
- Track string completion percentages and forecast delivery dates per language
- Detect source course changes and flag impacted strings across all in-progress translations
- Coordinate voiceover scheduling based on translation completion (VO can't start until script is finalized)
- Generate localization status report for client showing all languages with completion percentages
- Alert when text expansion in a language exceeds layout thresholds (triggering design adjustment)

**Data Required:**
- Localization board with sub-items per language
- Source course content with extractable string counts
- Historical cycle time data per language and content type
- Translator/VO artist availability and rates

**Autonomy Level:** Human-in-the-Loop
Workflow orchestration, status tracking, and reporting are autonomous. Translation quality decisions require human reviewer. Source change impact assessments are flagged for PM decision on whether to halt or continue in-progress translations.

**Example Interaction:**
> The "GlobalTech Cybersecurity Awareness" course reaches Gold Master. LocaleSync auto-creates 8 language sub-items (Spanish, French, German, Portuguese, Japanese, Mandarin, Korean, Arabic) with deadlines staggered by historical cycle time: European languages at 10 business days, Asian languages at 14, Arabic at 16 (includes RTL layout adjustment). Three days later, the source course gets an emergency update — a phishing example URL was flagged as a real malicious domain. LocaleSync immediately identifies: "Source updated: 3 strings changed in Section 2. Impact: Spanish and French translations are past this section — retranslation needed for 3 strings. German is currently on Section 2 — translator notified to use updated source. Remaining 5 languages haven't reached Section 2 yet — updated source will be used automatically. Estimated delay: 1 day for Spanish/French, 0 for others."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| ADDIE | Analysis, Design, Development, Implementation, Evaluation — the standard instructional design framework |
| SAM | Successive Approximation Model — agile-style iterative instructional design approach |
| Bloom's Taxonomy | Framework for categorizing learning objectives by cognitive complexity (Remember → Create) |
| SCORM | Sharable Content Object Reference Model — technical standard for e-learning content packaging and LMS communication |
| xAPI (Tin Can) | Experience API — modern successor to SCORM, tracks learning experiences beyond the LMS |
| ILT | Instructor-Led Training — live, facilitator-delivered sessions (in-person or virtual) |
| SME | Subject Matter Expert — provides technical content accuracy review |
| LMS | Learning Management System — platform for deploying, tracking, and reporting on training |
| WCAG | Web Content Accessibility Guidelines — international standard for digital accessibility |
| Section 508 | U.S. federal law requiring accessible electronic and information technology |
| VPAT | Voluntary Product Accessibility Template — document declaring product accessibility conformance |
| Gold Master | Final approved version of a course, ready for deployment |
| Storyboard | Detailed blueprint of a course showing content, interactions, and navigation per screen |
| Rapid Authoring | Tools enabling fast course creation without programming (Articulate, Lectora, Captivate) |
| Microlearning | Short-form learning content (2-7 minutes) focused on a single objective |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Creative Director / Design Lead | Sets visual standards, approves brand consistency, manages design team capacity | Decision-maker |
| Instructional Designer (ID) | Designs learning experiences, writes storyboards, selects pedagogical approaches | Decision-maker / Influencer |
| Graphic Designer / Visual Designer | Creates visual assets, layouts, and UI for learning content | User |
| Multimedia Developer | Builds interactive elements, animations, video, and audio components | User |
| LMS Administrator | Manages content deployment, SCORM packaging, and learner tracking | Influencer |
| VP of Learning / Chief Learning Officer | Sets strategic direction, approves budgets, owns client relationships | Decision-maker |
| Project Manager | Manages timelines, client communication, and resource allocation | Influencer |
| QA Specialist | Tests functionality, accessibility, and content accuracy before deployment | User |
| Accessibility Specialist | Ensures all content meets WCAG/508 standards | Influencer |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Instructional Design | IDs write the content that Creative & Design brings to life — they're inseparable collaborators | Joint pipeline management, shared project boards, integrated review workflows |
| Sales & Business Development | Sells the courses that Creative builds — needs accurate capacity and timeline data | CRM integration for pipeline-to-production forecasting, proposal asset library |
| Technology / LMS Operations | Deploys what Creative produces — SCORM packaging, LMS configuration, technical QA | Integrated deployment workflow, automated SCORM validation |
| Client Success | Manages ongoing client relationships, channels feedback, drives renewals | Shared client feedback portal, satisfaction tracking, renewal impact data |
| Procurement | Manages vendor relationships for stock assets, translators, VO artists, freelancers | License tracking, vendor performance dashboards, budget management |
| Marketing | Creates external-facing content about training offerings — needs brand-consistent assets | Shared asset library, brand compliance tracking |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Asana / Wrike | Generic project management adapted for creative workflows | monday.com offers superior visual customization, better template flexibility, and native file management — purpose-built for creative production pipelines |
| Articulate 360 (Review) | Built-in review tool for Storyline/Rise content | Limited to Articulate content only; monday.com provides cross-tool, cross-asset review management for the entire portfolio |
| Frame.io / Filestage | Specialized media review and approval | Narrow focus on video/visual review; doesn't manage the broader production pipeline, resource allocation, or cross-project visibility |
| Trello | Simple kanban boards popular with small creative teams | Lacks the depth for multi-stage review workflows, workload management, dashboards, and automations needed at scale |
| Smartsheet | Spreadsheet-style project management | Functional but poor UX for creative teams; lacks visual views (Gallery, Kanban) and the flexibility designers expect |
| Notion | Wiki + lightweight project management | Good for documentation but lacks robust automation, workload management, and structured approval workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use our authoring tool's built-in review features" | Those tools only cover one slice — Articulate Review only works for Storyline/Rise content. You need cross-asset, cross-tool visibility for your entire portfolio. monday.com sits above your authoring tools as the orchestration layer. |
| "Our designers won't adopt another tool" | monday.com replaces 3-4 tools (Trello + spreadsheets + email threads + shared drives for tracking). Net tool reduction. Plus, visual views like Gallery and Kanban match how creative teams naturally think. |
| "We're too small for this level of process" | The smaller you are, the less room you have for waste. If a 10-person creative team saves 5 hours/week on coordination, that's a 3% capacity increase — equivalent to hiring a part-time designer. |
| "We need our budget for authoring tool licenses" | monday.com doesn't replace authoring tools — it makes your investment in them more productive. If your designers spend 30% of their time on coordination instead of creating, your authoring tool ROI is 30% lower than it should be. |
| "How is this different from a shared Google Drive with folders?" | A shared drive tells you where files are. monday.com tells you where every project is, who's working on what, what's overdue, what's waiting for review, and what's at risk — and it acts on that information automatically. |

## Proof Points
*(To be populated with customer references)*
- [Training companies using monday.com for creative production management]
- [E-learning companies scaling content output with workflow automation]
- [Organizations that improved accessibility compliance through structured workflows]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
