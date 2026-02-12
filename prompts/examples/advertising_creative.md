# Advertising × Creative Playbook

## Overview

Creative departments are the engine of advertising agencies — they transform client briefs into campaigns that move audiences. Unlike in-house creative teams, agency creatives operate under relentless time pressure, juggling multiple clients with competing deadlines, each with different brand guidelines, approval workflows, and feedback styles. A mid-sized agency creative department might touch 50-100 active projects simultaneously across 15-30 clients.

The Creative function typically spans concept development (creative directors, art directors, copywriters), production (designers, motion graphics, video editors, studio artists), and creative operations (traffic managers, project managers, resource managers). At agencies ranging from boutiques to holding company networks, this organization can range from 10 to 500+ creatives, often across multiple offices and time zones.

What makes this combination unique: The tension between "creative genius" and "operational efficiency" is constant. Creatives resist process because it feels like it kills creativity — yet without process, agencies bleed money on scope creep, endless revision cycles, and missed deadlines. The opportunity for AI is massive: automate the operational burden (versioning, resizing, status updates, resource tracking) so creatives can focus on the work itself. The agencies that figure this out will produce better work faster — and that's the only sustainable competitive advantage in advertising.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - Agencies are under constant fee pressure; clients expect more deliverables for the same (or less) money
   - Headcount is the #1 cost driver, but creative talent is scarce and expensive
   - AI enables more output per creative — the difference between a profitable and unprofitable account
   
2. **Replace or Radically Augment Headcount** — HIGH RELEVANCE
   - Production tasks (resizing, versioning, trafficking) consume junior creative time
   - Traffic management and status reporting are labor-intensive coordination roles
   - AI can handle asset generation, version control, and project status — freeing humans for ideation

3. **Consolidate Tech Stack with AI** — MEDIUM RELEVANCE
   - Creative teams use fragmented tools (Adobe Creative Cloud, Figma, Frame.io, Asana, Slack, DAM systems)
   - Context gets lost across tools; finding the "right" version of an asset is a daily struggle
   - Consolidation is attractive but must integrate with Adobe ecosystem (non-negotiable)

---

## Prioritized Use Cases

### 1. Creative Brief Intake & Kickoff Automation
**Relevance**: High  
**Value Driver**: 2 (Scale Without Overhead)

**Pain Point**: 
Creative briefs arrive in every format — emails, Word docs, Slack messages, verbal requests in hallways. Incomplete briefs cause rework; the #1 creative complaint is "we didn't know that was a requirement." At a typical agency, 30-40% of revision cycles trace back to unclear briefs. Each kickoff meeting is 30-60 minutes of people in a room (at fully-loaded rates of $150-300/hour) asking questions that should have been answered upfront.

**Solution**: 
Vibe app for standardized brief intake with mandatory fields based on project type. AI analyzes briefs for completeness, flags missing information, and auto-suggests timeline based on scope. Automated kickoff package generation with creative references, brand guidelines, and prior campaign assets pulled from DAM. Sidekick summarizes lengthy briefs into creative-friendly one-pagers.

**Vibe Prompt**:
```
Build a Creative Brief Intake app for advertising agency account and creative teams.

Purpose: Standardize how creative briefs are submitted, ensure completeness, and automate kickoff preparation.

Key features:
- Brief submission form with dynamic fields based on Project Type (Campaign, Social Content, Video, Print, Digital Banner, OOH)
- Required fields: Client, Brand, Project name, Objective, Target audience, Key message, Mandatories, Budget range, Deliverables list, Due date
- Optional fields: Competitive context, Prior campaign links, Tone/manner references, Legal/compliance notes
- AI completeness checker that scores brief (1-10) and flags missing critical information
- AI-suggested timeline based on deliverable count and complexity
- Automated kickoff package: pulls brand guidelines doc, recent campaign assets, and creates meeting agenda
- Status workflow: Draft → Submitted → Under Review → Clarification Needed → Approved → In Production
- Link to Creative Project (creates project when brief approved)
- Dashboard: Briefs pending review, Average completeness score by account team, Time from brief to kickoff

Include automations:
- On submit, AI scores completeness and notifies Creative Director if score < 7
- If required fields missing, return to submitter with specific questions
- When brief approved, auto-create Creative Project with deliverables as sub-items
- Notify creative team leads when new brief assigned to their discipline
- Weekly digest to Account Directors: Briefs submitted, Rejected for incompleteness, Average time-to-approval
```

**Outcome**: 
- Reduce revision cycles caused by brief issues by 50%
- Cut kickoff meeting prep time by 70%
- Eliminate "lost" briefs and verbal requests
- Increase creative satisfaction (less "why didn't anyone tell me?")

**Discovery Questions**:
- "How do creative briefs get to your team today? How many different channels?"
- "What percentage of your revision cycles trace back to unclear or incomplete briefs?"
- "How much time does your team spend preparing for and attending kickoff meetings?"

**Industry-Specific Context**: 
"Mandatories" = required elements (logo placement, legal copy, tagline). "Tone and manner" = the creative style/feeling. Briefs often come from Account teams, not clients directly. "Kickoff" = meeting where creative and account align on the brief before work begins.

---

### 2. Asset Production & Version Control
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
A single campaign can generate hundreds of assets across formats, sizes, and languages. A digital campaign might need 50+ banner sizes, each with multiple CTA variants. Junior designers spend 60-70% of their time on mechanical production (resizing, reformatting, version updates) rather than actual design. Version control is chaotic — "final_v3_REAL_FINAL_updated.psd" is a meme because it's painfully true.

**Solution**: 
monday.com for asset tracking with automated versioning. AI Blocks for auto-generation of size variants from master designs. Clear status workflows from concept through production to delivery. Integration with Adobe Creative Cloud and DAM for file management. Sidekick generates asset specs and naming conventions.

**Vibe Prompt**:
```
Build an Asset Production Tracker for advertising agency creative and studio teams.

Purpose: Track all creative assets from concept through final delivery, with version control and production status.

Key features:
- Asset item fields: Asset name, Campaign, Client, Asset type (Static/Video/Audio/HTML5), Format/size, Platform (Meta, Google, TikTok, Print, OOH), Language, Version number
- Master asset linking: Connect size variants to master design
- Version history: Track all versions with thumbnails, upload date, who uploaded, change notes
- Status workflow: Briefed → In Design → Internal Review → Client Review → Revisions → Approved → In Production → Delivered
- Review feedback capture: Comments linked to specific versions
- Specs panel: Dimensions, file format, max file size, platform requirements
- Bulk operations: Update status for multiple related assets
- Delivery checklist: File naming, format verification, platform specs
- Dashboard: Assets by status, Assets per campaign, Production velocity, Revision rounds per asset, Assets pending review

Include automations:
- When master asset approved, auto-create child items for all required sizes
- When new version uploaded, increment version number and notify reviewers
- When all assets in campaign = Delivered, notify Account Manager
- If asset in "Client Review" > 3 days, send reminder to Account team
- When asset rejected, require revision notes before status change
- Daily production report: Assets completed yesterday, Assets due today, Overdue items
```

**Outcome**: 
- Reduce production time per asset by 40% through templatization
- Eliminate version confusion and "wrong file" delivery errors
- Free junior designers to do actual design work (increase creative capacity 30%)
- Improve on-time delivery rate by tracking bottlenecks

**Discovery Questions**:
- "How many assets does a typical campaign require? How many size variants?"
- "What percentage of your junior designers' time goes to mechanical production vs. actual design?"
- "When was the last time the wrong version of a file went to a client or publisher?"

**Industry-Specific Context**: 
"Master" = the primary design from which variants are created. "Trafficking" = the process of delivering final assets to media publishers. Asset specs vary wildly by platform (Meta, Google, TikTok all have different requirements). "Studio" = the production team that handles mechanical work.

---

### 3. Creative Review & Approval Workflow
**Relevance**: High  
**Value Driver**: 2 (Scale Without Overhead)

**Pain Point**: 
Creative review is a black hole. Work goes in, feedback trickles out over days (or weeks). Feedback arrives in emails, PDFs with markup, Slack threads, and Post-it notes from in-person reviews. Consolidating and reconciling conflicting feedback takes hours. Multiple stakeholders (client brand team, legal, agency creative director) have different priorities, and the creative team is stuck mediating. Average campaign sees 3-5 revision rounds; 2 should be the norm.

**Solution**: 
Centralized review workflow with role-based feedback routing. Clients and stakeholders provide feedback in-context on the actual assets. AI summarizes and consolidates feedback, flags conflicting direction. Clear revision tracking shows what changed between versions. Approval thresholds and escalation paths for stalled reviews.

**Vibe Prompt**:
```
Build a Creative Review & Approval app for advertising agency creative, account, and client stakeholders.

Purpose: Centralize creative feedback, streamline approvals, and reduce revision cycles.

Key features:
- Review request form: Link to assets (image/video preview), Requested reviewers, Review type (Internal/Client/Legal), Due date, Context notes
- Reviewer roles: Creative Director, Account Lead, Client Brand Manager, Client Legal, Media Agency
- In-context feedback: Comments tied to specific assets and timestamps (for video)
- Feedback status per reviewer: Pending → Reviewed → Approved / Changes Requested
- AI feedback consolidation: Summarize all feedback into actionable revision list, flag conflicts
- Conflict resolution workflow: When reviewers disagree, escalate to decision-maker
- Revision tracking: Side-by-side comparison of versions, change log
- Approval workflow: All required approvers must approve before status = Approved
- SLA tracking: Time in review by stage, reviewers who are bottlenecks
- Dashboard: Reviews pending by project, Average review cycle time, Approval rate by reviewer, Revision rounds per campaign

Include automations:
- When review requested, notify all reviewers with due date
- 24 hours before due date, remind reviewers who haven't responded
- When all feedback received, AI generates consolidated revision brief
- When conflict detected, notify Account Lead to resolve
- When approved, update Asset status and notify production team
- When review overdue by 48 hours, escalate to Account Director
- Weekly report: Campaigns stuck in review, Slowest reviewers, Average cycle time trend
```

**Outcome**: 
- Reduce average revision rounds from 4 to 2
- Cut time-in-review by 50%
- Eliminate "lost" feedback and conflicting direction
- Improve client satisfaction through transparent process

**Discovery Questions**:
- "How many rounds of revisions does a typical campaign go through? What's the target?"
- "How does client feedback reach your creative team today? How many channels?"
- "When you have conflicting feedback from different stakeholders, how is that resolved?"

**Industry-Specific Context**: 
"Internal review" = agency-side review before showing client. "Rounds" = complete cycles of feedback and revision. "Legal review" = compliance check for claims, disclaimers, rights. Large clients often have brand guardians who police consistency. Review bottlenecks are the #1 cause of missed deadlines.

---

### 4. Resource Management & Capacity Planning
**Relevance**: High  
**Value Driver**: 2 (Scale Without Overhead)

**Pain Point**: 
Creative resource management is chaos. Work is assigned based on who's "less busy" (a guess), who did the last project for that client (tribal knowledge), or who's sitting closest (convenience). Some creatives are overloaded while others have capacity. Senior talent gets pulled into production work because no one knows who's available. Utilization tracking is manual and inaccurate — and profitability depends on it.

**Solution**: 
monday.com resource management with real-time capacity visibility. Skills-based assignment matching creative type (conceptual vs. production) to project needs. Utilization dashboards showing billable vs. non-billable time. AI-powered workload balancing and conflict detection. Integration with time tracking for accurate utilization.

**Vibe Prompt**:
```
Build a Creative Resource Management app for advertising agency creative directors, resource managers, and producers.

Purpose: Manage creative team capacity, assign work intelligently, and optimize utilization.

Key features:
- Team roster: Name, Role (CD, ACD, AD, Designer, Copywriter, Motion), Skills/specialties, Billable target %, Home office
- Project assignments: Link team member to projects with allocated hours, start/end dates, role on project
- Capacity view: Calendar/Gantt showing each person's assignments over time
- Availability calculator: Total hours - assigned hours = available capacity by day/week
- Skills matching: Tag projects with required skills, surface matches when assigning
- Conflict detection: Alert when person is over-allocated (>100%) or has overlapping deadlines
- Utilization tracking: Billable hours, Non-billable hours, PTO, Utilization % vs. target
- Request workflow: Producers request resources, Resource Manager approves/assigns
- Bench report: Who has capacity in the next 2 weeks
- Dashboard: Team utilization this week/month, Over-allocated team members, Under-utilized talent, Skills gaps on active projects

Include automations:
- When new project created, suggest team members based on client history + skills + availability
- When allocation would cause over-utilization, alert Resource Manager
- When utilization drops below 60% for a team member, flag for attention
- When PTO approved, block capacity and recalculate project allocations
- Weekly capacity report to Creative Directors: Team utilization, Who's overloaded, Who has capacity
- Monthly utilization summary to Finance: Billable %, By team, By client
```

**Outcome**: 
- Increase billable utilization by 10-15%
- Reduce burnout and turnover from chronic over-allocation
- Match senior talent to senior work (protect margins)
- Enable data-driven staffing decisions

**Discovery Questions**:
- "How do you know who has capacity right now? How confident are you in that picture?"
- "What's your target utilization rate? How close do you get to it?"
- "When was the last time a senior creative got pulled into production work because of a resource crunch?"

**Industry-Specific Context**: 
"Utilization" = billable hours / available hours. Target is typically 70-80% for creatives. "Bench" = people without assigned work. CD = Creative Director, ACD = Associate CD, AD = Art Director. Holding companies track utilization obsessively; independents often don't (and suffer for it).

---

### 5. Campaign Timelines & Milestone Tracking
**Relevance**: Medium-High  
**Value Driver**: 2 (Scale Without Overhead)

**Pain Point**: 
Campaign timelines are complex — multiple workstreams (concept, design, copy, production, media) with dependencies, client milestones, media deadlines, and internal checkpoints. Timelines live in spreadsheets or Gantt charts that are out of date the moment they're created. When one thing slips, the cascade isn't visible until it's a crisis. Traffic managers spend hours updating status across systems.

**Solution**: 
monday.com Work Management for integrated campaign timelines with dependencies. Workstream views for each discipline. Automated status rollup from tasks to milestones to campaign level. AI predicts timeline risk based on historical patterns. Real-time dashboards for account teams and clients.

**Vibe Prompt**:
```
Build a Campaign Timeline Manager for advertising agency account, creative, and production teams.

Purpose: Plan, track, and visualize campaign timelines with dependencies and milestone tracking.

Key features:
- Campaign setup: Client, Campaign name, Launch date, Workstreams (Concept, Design, Copy, Video, Digital Production, Print Production)
- Milestone items: Name, Date, Type (Internal Checkpoint, Client Presentation, Client Approval, Media Deadline, Launch), Owner
- Task items linked to milestones: Task name, Assignee, Estimated hours, Start/end dates, Dependencies
- Timeline/Gantt view showing all workstreams and dependencies
- Critical path highlighting: Show which tasks directly impact launch date
- Status rollup: Task status → Milestone status → Campaign status
- Dependency management: When task slips, auto-calculate impact on dependent items
- AI risk prediction: Flag campaigns likely to miss milestones based on current velocity
- Client-facing view: Simplified timeline for client visibility (hide internal tasks)
- Dashboard: Campaigns by status, Milestones due this week, At-risk campaigns, Overdue tasks

Include automations:
- When task marked complete, check if milestone can be completed
- When milestone slips, recalculate downstream dependencies and notify stakeholders
- 1 week before media deadline, verify all assets on track
- When campaign at risk (AI flag), alert Account Director and Creative Director
- Daily standup digest: What's due today, What's overdue, What's blocked
- Client weekly update: Auto-generate status summary with milestone progress
```

**Outcome**: 
- Reduce missed deadlines by 60%
- Eliminate "surprise" timeline crunches through early warning
- Cut status reporting time by 80% (automated vs. manual)
- Improve client confidence through transparency

**Discovery Questions**:
- "How do you track campaign timelines today? How often are they accurate?"
- "When a task slips, how quickly do you see the downstream impact?"
- "How much time do your traffic managers or producers spend on status reporting?"

**Industry-Specific Context**: 
"Traffic" = the function that manages workflow and deadlines (in some agencies, this is "Project Management"). "Media deadline" = the non-negotiable date when assets must be delivered to publishers. "Workstream" = a discipline or track within a campaign. Critical path management is essential — not all tasks are equal.

---

### 6. Client Feedback & Communication Hub
**Relevance**: Medium  
**Value Driver**: 3 (Consolidate Tech Stack)

**Pain Point**: 
Client communication is scattered across email threads, Slack channels, Zoom recordings, and meeting notes. When a new team member joins the account, getting them up to speed takes weeks. Finding "what did the client say about X?" means searching multiple systems. Important decisions get buried. Clients repeat themselves because the agency doesn't seem to remember prior conversations.

**Solution**: 
monday.com as client communication hub. Meeting notes automatically logged with action items extracted. Email integration capturing key threads. AI-powered search across all client communications. Decision log for important direction. Client preferences and feedback patterns surfaced for new team members.

**Vibe Prompt**:
```
Build a Client Communication Hub for advertising agency account teams.

Purpose: Centralize all client communications, decisions, and feedback in one searchable location.

Key features:
- Client profile: Company name, Brand(s), Key contacts (with roles, preferences, communication style notes), Relationship history
- Communication log: Date, Type (Email, Meeting, Call, Slack), Participants, Summary, Attachments
- AI meeting notes: Upload recording or notes, AI extracts summary, decisions, and action items
- Decision log: Key decisions with date, context, who decided, implications
- Feedback patterns: AI analysis of client feedback trends (what do they consistently like/dislike?)
- Action items: Tasks generated from meetings with assignee, due date, linked to source
- Search: Full-text search across all communications
- Client preferences: Captured learnings (e.g., "CMO hates blue," "Always present concepts as three options")
- Onboarding view: Summary for new team members joining the account
- Dashboard: Recent communications, Open action items, Upcoming meetings, Relationship health score

Include automations:
- When meeting notes uploaded, AI extracts action items and creates tasks
- When email forwarded to board, AI summarizes and logs
- When decision logged, notify relevant team members
- Weekly digest to Account Lead: Communications this week, Open actions, Decisions made
- When new team member added to account, generate onboarding summary
- If no communication logged in 2 weeks, alert Account Director
```

**Outcome**: 
- Cut new team member onboarding time by 50%
- Eliminate "we discussed this already" client frustration
- Ensure action items don't fall through cracks
- Build institutional memory that survives team turnover

**Discovery Questions**:
- "When a new team member joins an account, how long does it take them to get up to speed?"
- "Where do client decisions get documented? How easy are they to find later?"
- "Have you ever had a client frustrated because the agency 'forgot' a prior conversation?"

**Industry-Specific Context**: 
Agency-client relationships are long-term (multi-year) and complex. Institutional memory is a competitive advantage. "Account" = the client relationship as a whole. Key contacts change frequently on both sides. Handoffs (when team members leave) are high-risk moments.

---

### 7. Creative Brief-to-Insight AI Assistant
**Relevance**: Medium  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Before concepting, creatives need to understand the audience, competitive landscape, and cultural context. This research is often rushed or skipped due to time pressure. Junior strategists spend hours compiling decks that creatives skim. When research does happen, insights get lost between strategy and creative handoff. The result: concepts that miss the mark, requiring more revision cycles.

**Solution**: 
AI-powered insight generation from briefs. When a brief is submitted, Sidekick automatically researches target audience, competitive creative examples, cultural trends, and platform best practices. Generates a creative starter pack with inspiration and guardrails. Creatives get context without waiting for strategy decks.

**Vibe Prompt**:
```
Build a Creative Insight Generator for advertising agency strategy and creative teams.

Purpose: Automatically generate audience insights, competitive context, and creative inspiration from briefs.

Key features:
- Insight request linked to Creative Brief
- AI research modules:
  - Target audience profile: Demographics, psychographics, media habits, cultural tensions
  - Competitive creative scan: Recent campaigns from competitors with links and analysis
  - Platform best practices: What's working on the target platforms (Meta, TikTok, YouTube)
  - Cultural context: Relevant trends, moments, memes related to the category
  - Brand voice check: Summary of client's brand guidelines and recent work
- Insight summary: One-page creative starter with key takeaways
- Inspiration gallery: Curated examples (can be manually added by strategists)
- Guardrails: Things to avoid based on client history, competitive similarity, cultural sensitivity
- Feedback loop: Creatives rate insight usefulness to improve future generation
- Link to Creative Brief and Campaign
- Dashboard: Insights generated, Usefulness ratings, Most referenced examples

Include automations:
- When Creative Brief approved, auto-generate insight package
- Notify creative team when insight package ready
- When creative team requests additional research, add to insight request
- Weekly summary to Strategy Lead: Insights generated, Usefulness scores, Gaps identified
```

**Outcome**: 
- Reduce creative concepting ramp-up time by 40%
- Increase concept relevance (fewer "off-brief" ideas)
- Free strategists from repetitive research compilation
- Build institutional knowledge base of what works

**Discovery Questions**:
- "How do creatives get context before they start concepting? How long does that take?"
- "What percentage of first-round concepts are on-brief vs. need significant redirection?"
- "Where does competitive and cultural research live? Is it reusable?"

**Industry-Specific Context**: 
"Concepting" = the ideation phase of creative development. "Strategy" = the planning function that defines what to say (vs. creative which defines how to say it). "Platform" = where the creative will run (Meta, TikTok, YouTube, etc.). Insight-to-execution gap is a perennial agency challenge.

---

## Industry Terminology Glossary

| Term | Definition |
|------|------------|
| **Brief** | The document that initiates creative work, defining objectives, audience, deliverables, and constraints. The starting point for everything. |
| **Concepting** | The ideation phase where creatives develop campaign ideas and directions before production. |
| **Rounds** | Cycles of creative review and revision. "Three rounds" means three submissions with feedback between each. |
| **Traffic** | The function (or person) responsible for managing workflow, deadlines, and routing of creative work. Also called "Project Management" at some agencies. |
| **Mandatories** | Required elements that must appear in creative (logo placement, legal copy, tagline, disclaimers). Non-negotiable. |
| **Tone and Manner** | The stylistic direction for creative — how it should feel (e.g., "warm and approachable" vs. "bold and disruptive"). |
| **Utilization** | Percentage of a creative's time that is billable to clients. Target is typically 70-80%. |
| **Master** | The primary design file from which format/size variants are created. |
| **Trafficking** | The process of delivering final assets to media publishers or platforms. |
| **DAM** | Digital Asset Management — the system for storing, organizing, and retrieving creative files. |
| **AOR** | Agency of Record — the primary agency responsible for a client's advertising. |
| **Holding Company** | Large conglomerates that own multiple agencies (WPP, Omnicom, Publicis, IPG, Dentsu). |
| **Scope Creep** | When project requirements expand beyond the original brief without corresponding budget/timeline adjustment. |
| **Media Deadline** | The non-negotiable date when assets must be delivered to publishers to run on schedule. |
| **Deck** | A presentation, typically in PowerPoint or Keynote format. "Creative deck" = presentation of campaign concepts. |

---

## Typical Stakeholder Roles

**Primary Buyer: Chief Creative Officer or VP Creative**
- Title: CCO, VP of Creative, Executive Creative Director (ECD)
- Concerns: Creative quality, talent retention, winning awards, protecting creative time from operational burden
- Decision driver: "Will this help my team make better work, or just add process?"

**Technical Evaluator: Director of Creative Operations / Head of Production**
- Title: Director of Creative Ops, VP Production, Studio Director
- Concerns: Efficiency, utilization tracking, tool consolidation, production bottlenecks
- Decision driver: "Will this actually get adopted, or will creatives route around it?"

**Executive Sponsor: CEO or President**
- Title: CEO, President, Managing Director
- Concerns: Profitability (utilization × rate), client retention, competitive differentiation
- Decision driver: "Does this improve margins without compromising the work?"

**Financial Stakeholder: CFO or Director of Finance**
- Title: CFO, Finance Director, Controller
- Concerns: Billable utilization, project profitability, time tracking accuracy
- Decision driver: "Can we actually track where time goes and bill for it?"

**End Users:**
- Creative Directors, Art Directors, Copywriters, Designers, Motion Designers, Studio Artists, Traffic Managers, Producers, Account Managers

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Account Management** | Brief intake, client communication, timeline management | Client relationship management, project profitability tracking |
| **Strategy/Planning** | Brief development, research, insights | Research repository, campaign effectiveness tracking |
| **Media** | Asset specs, trafficking deadlines, platform requirements | Media plan tracking, cross-channel campaign management |
| **Production** | Video shoots, photo shoots, external vendor management | Production project management, vendor/freelancer management |
| **Finance** | Time tracking, utilization, project profitability | Resource costing, project financials, billing |
| **New Business** | Pitch timelines, credentials management, case studies | Pitch tracking CRM, case study library |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| Project Management | Asana, Monday (current), Wrike, Basecamp, Notion | Consolidate + add AI |
| Review & Approval | Frame.io, Ziflow, MediaValet, email/PDFs | Full replacement |
| Resource Management | Float, Resource Guru, Kantata, spreadsheets | Full replacement |
| Time Tracking | Harvest, Toggl, Clockify | Integration (keep or replace) |
| DAM | Bynder, Brandfolder, Canto, Dropbox | Integration, not replacement |
| Creative Tools | Adobe Creative Cloud, Figma | Integration, not replacement |

**Positioning:**
- **vs. Asana/Basecamp**: "Those are task lists. You need workflow intelligence — from brief to delivery, with AI that actually understands creative process."
- **vs. Frame.io**: "Great for video review. But your campaigns are more than video. One platform for all asset types, all feedback, all approvals."
- **vs. Spreadsheet-based resource management**: "You're making million-dollar staffing decisions based on data that's wrong the moment it's entered. Real-time capacity visibility changes everything."
- **vs. Point solutions**: "Your creatives use 6 tools before lunch. Every tool switch is a context switch. One platform means creative energy goes into the work, not the tools."

---

## Common Objections

**Objection**: "Creatives hate process tools. They'll never use it."

**Response**: "That's exactly why we focus on eliminating process, not adding it. The goal isn't for creatives to spend time in a tool — it's for them to spend less time on everything except the actual creative work. When resizing, versioning, and status updates happen automatically, creatives get what they actually want: more time to make things. We've seen adoption spike when teams realize the tool is on their side."

---

**Objection**: "We already use Monday/Asana for project tracking."

**Response**: "Project tracking is table stakes. The question is: what happens to all the context between tasks? Brief insights, client feedback patterns, version history, resource availability — in most setups, that's scattered across email, Slack, and tribal knowledge. monday.com's AI layer connects all of it, so decisions are informed and work doesn't get repeated. It's not about tracking work — it's about the AI actually doing work."

---

**Objection**: "Our clients have their own tools and processes we have to follow."

**Response**: "Totally normal — and a reason to have your own source of truth. You adapt outputs to client systems, but your internal operations need to work for you. Most agencies run two layers: client-facing (whatever the client wants) and internal (what actually helps you deliver). monday.com is the internal engine. Export views, sync data, generate reports in whatever format clients need — but your team operates on a system designed for how agencies actually work."

---

*Playbook Version: 1.0*  
*Industry: Advertising*  
*Department: Creative*  
*Last Updated: 2026-02-10*
