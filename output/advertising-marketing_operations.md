# Advertising & Marketing × Operations Playbook

## Overview

Operations in advertising and marketing agencies is the backbone that keeps creative chaos organized. Unlike traditional manufacturing operations, agency ops manages intangible deliverables — campaigns, creative assets, media buys — where timelines are compressed, scope creeps constantly, and client demands shift daily.

The Operations function in agencies typically spans resource management (matching talent to projects), project delivery (timelines, milestones, reviews), financial operations (estimates, budgets, reconciliation), and production/traffic (asset routing, versioning, delivery). At mid-to-large agencies (100-1,000+ employees), this organization is often split between centralized Ops leadership and embedded project managers/producers within account teams.

What makes this combination unique: Agencies sell time and ideas — both of which are hard to track and easy to waste. The average agency runs at 55-65% utilization (billable hours ÷ available hours), leaving massive room for improvement. Operations leaders battle resource conflicts, scope creep, and the eternal question: "Are we actually making money on this client?" AI can automate resource matching, predict project overruns before they happen, and give real-time visibility into profitability.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - Agencies are under constant pressure to do more with less
   - Clients demand more deliverables, faster turnaround, same (or lower) fees
   - AI enables handling 20% more work without adding headcount
   
2. **Replace or Radically Augment Headcount** — HIGH RELEVANCE
   - Traffic management, status reporting, and resource scheduling consume hours
   - Project coordinators spend 60%+ of time on admin, not strategic work
   - AI can automate routine coordination, freeing PMs for client relationships

3. **Consolidate Tech Stack with AI** — MEDIUM RELEVANCE
   - Most agencies use 5-10 tools: project management, time tracking, resource planning, finance, DAM
   - Integration gaps create manual reconciliation and data silos
   - One platform that handles multiple functions reduces overhead

---

## Prioritized Use Cases

### 1. Resource Management & Capacity Planning
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Finding the right person for a project is a daily struggle. Who's available? Who has the right skills? Who's already overloaded? Most agencies manage this in spreadsheets or the heads of a few key people. When they get it wrong, projects suffer (wrong skills) or people burn out (overallocation).

**Solution**: 
monday.com resource management with AI-powered matching. See real-time availability across the agency, match skills to project needs, and get AI recommendations when conflicts arise. Predict capacity crunches 2-4 weeks out so leadership can make proactive decisions (hire contractors, push timelines, decline work).

**Vibe Prompt**:
```
Build a Resource Management app for advertising agency operations.

Purpose: Match talent to projects, track utilization, and predict capacity crunches before they happen.

Key features:
- People database: Name, Role (Creative Director/Designer/Copywriter/Strategist/Producer/Developer), Skills (taggable), Hourly rate (internal cost), Department, Manager
- Availability calendar: Show allocated hours vs available hours per person per week
- Project staffing board: Each project shows required roles, assigned people, hours allocated, date range
- AI matching: When a role is needed, suggest best-fit people based on skills + availability + past project types
- Utilization dashboard: Target (e.g., 75%) vs Actual by person/team/department
- Capacity forecast: 4-week forward view showing predicted over/under capacity by role type
- Conflict detection: Flag when someone is >100% allocated
- Contractor pool: Track freelancers with their rates, availability, and specialties
- Dashboard: Agency utilization this week/month, Roles at capacity, People under 50% utilized, Projects understaffed

Include automations:
- When utilization >100%, notify Resource Manager and person's manager
- When a project is created, suggest staffing based on similar past projects
- Weekly forecast email to Ops Director showing capacity risks
- When contractor engaged, create onboarding checklist
- Daily sync of time entries to update actual vs planned hours
```

**Outcome**: 
- Increase agency utilization from 60% to 70%+ (significant revenue impact)
- Reduce time spent on resource scheduling by 50%
- Prevent burnout by catching overallocation early
- Better project outcomes through right-fit staffing

**Discovery Questions**:
- "What's your current agency utilization rate? What would a 10-point improvement mean in revenue?"
- "How do you decide who works on what project? How much time does that take?"
- "When's the last time a project suffered because you had the wrong people on it?"

**Industry-Specific Context**: 
Utilization = billable hours ÷ available hours. Industry benchmark is 65-75%. "Bench" = people without project assignments. "Over-servicing" = delivering more hours than scoped/billed.

---

### 2. Project Profitability & Financial Operations
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Most agencies don't know if a project is profitable until it's over — and by then it's too late. They estimate hours, track actuals (sometimes), but rarely reconcile in real-time. Result: some projects subsidize others, and no one knows which ones until the quarterly P&L review.

**Solution**: 
monday.com project financials with real-time profitability tracking. Connect time entries to project budgets automatically. AI flags projects trending toward overrun before they hit the wall. Dashboard shows project-level and client-level profitability so leadership can intervene early or have scope conversations with clients.

**Vibe Prompt**:
```
Build a Project Profitability app for advertising agency finance and operations.

Purpose: Track project budgets vs actuals in real-time and identify profitability issues before they become problems.

Key features:
- Project financial card: Estimated hours by role, Estimated revenue, Actual hours to date, Actual cost (hours × internal rate), Projected final hours (based on % complete), Projected margin
- Budget burn tracking: Visual showing budget consumed vs project completion %
- AI early warning: Flag projects where burn rate exceeds completion rate
- Client profitability rollup: Aggregate all projects for a client to show total relationship profitability
- Scope change tracking: Log changes with associated hours/revenue adjustments
- Invoice tracking: Link invoices to projects, track collected vs outstanding
- Rate card management: Standard rates by role, client-specific rates
- Dashboard: Projects by margin (green/yellow/red), Clients by profitability, Revenue forecast this month/quarter, At-risk projects requiring attention

Include automations:
- When actual hours reach 80% of estimate with <70% complete, alert PM and Ops Director
- When scope change logged, prompt for estimate adjustment
- Weekly profitability summary to Finance Director
- When project completes, calculate final margin and log for benchmarking
- Monthly client profitability report to Account Director
```

**Outcome**: 
- Identify at-risk projects 2-3 weeks earlier
- Improve average project margin by 5-10 points
- Enable data-driven scope conversations with clients
- Reduce "surprise" write-offs at project close

**Discovery Questions**:
- "Do you know right now which projects are making money and which are losing money?"
- "How often do projects go over budget? How do you find out?"
- "What's your average project margin? What would improving it by 5 points mean to the agency?"

**Industry-Specific Context**: 
AGI (Agency Gross Income) = revenue minus pass-through costs. Margin typically calculated on AGI. "Write-off" = hours worked but not billed. "Over-service" = delivering more than contracted (intentional or not).

---

### 3. Campaign Trafficking & Asset Delivery
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Getting the right creative assets to the right destinations on time is a logistical nightmare. A single campaign might have 50+ assets (different sizes, versions, languages) going to 10+ publishers/platforms, each with their own specs. Traffic coordinators manually track versions, specs, delivery confirmations — and a single mistake can mean a missed flight date or wrong creative running.

**Solution**: 
monday.com trafficking workflow with AI-powered spec checking. Track every asset version, automate spec validation against publisher requirements, manage delivery confirmations, and maintain a complete audit trail. AI catches common errors (wrong dimensions, file size exceeded, missing required elements) before assets go out the door.

**Vibe Prompt**:
```
Build a Campaign Trafficking app for advertising agency operations.

Purpose: Manage creative asset delivery across multiple publishers and platforms with version control and spec compliance.

Key features:
- Campaign board: Campaign name, Client, Flight dates, Status (In Production/Trafficking/Live/Complete)
- Asset inventory per campaign: Asset name, Format (display/video/social/print), Dimensions, File size, Version number, Final approved (Y/N)
- Publisher/platform tracking: Publisher name, Specs (dimensions, file type, max size, aspect ratios), Due date, Delivery method, Confirmation status
- AI spec checker: Upload asset → auto-validate against publisher requirements → flag violations
- Version control: Track all versions of each asset, link to approval history
- Delivery log: When delivered, To whom, Confirmation received, Traffic sheet sent
- Revision tracking: When client requests changes, log revision round with notes
- Dashboard: Campaigns trafficking this week, Assets pending delivery, Spec violations to fix, Late deliveries, Publisher performance (how often they confirm)

Include automations:
- When asset uploaded, run AI spec check and flag issues
- 48 hours before flight date, verify all assets delivered and confirmed
- When publisher confirms receipt, update status automatically
- When creative team marks final, move to Ready for Traffic
- Send daily trafficking summary to Traffic Manager: What's going out, What's at risk
```

**Outcome**: 
- Reduce trafficking errors by 80%
- Cut trafficking coordination time by 40%
- Eliminate missed flight dates
- Free traffic coordinators for higher-value work

**Discovery Questions**:
- "How many assets do you traffic in a typical month? How many people manage that?"
- "What happens when the wrong creative runs? What's the cost — in time, in client trust?"
- "How do you currently validate assets meet publisher specs?"

**Industry-Specific Context**: 
"Trafficking" = routing creative assets to publishers/platforms. "Flight date" = when campaign goes live. "Traffic sheet" = specifications document sent with assets. "Specs" = technical requirements (dimensions, file size, format, etc.).

---

### 4. Project Status & Client Reporting
**Relevance**: Medium-High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Status reports eat hours. Every week, project managers manually compile updates from multiple sources, format them for clients, and send them out. Account teams spend hours in "status check" meetings that could be an email. When clients ask "where are we?", it takes 20 minutes to assemble the answer.

**Solution**: 
monday.com dashboards that generate status reports automatically. Real-time project status visible to clients (where appropriate) or exportable as formatted reports. AI generates executive summaries from project data. Reduce status meetings from 1 hour to 15 minutes.

**Vibe Prompt**:
```
Build a Project Status & Reporting app for advertising agency operations and account management.

Purpose: Automate status reporting and give real-time visibility into project progress for internal teams and clients.

Key features:
- Project status board: Project name, Client, Phase (Discovery/Strategy/Creative/Production/Launch), Overall status (On Track/At Risk/Blocked), Key milestones, Current activities
- Milestone tracking: Milestone name, Due date, Status (Not Started/In Progress/Complete/Delayed), Owner
- Blocker/risk log: Issue description, Impact, Owner, Resolution date, Escalated (Y/N)
- Activity feed: Auto-log key actions (status changes, approvals, deliveries, comments)
- AI status summary: Generate executive summary from project data (what happened this week, what's next, any risks)
- Client-facing view: Filtered dashboard clients can access directly
- Report export: One-click PDF generation with agency branding
- Meeting prep: AI-generated talking points for status meetings
- Dashboard: All projects by status, At-risk projects, Overdue milestones, Client projects summary

Include automations:
- Every Friday, generate AI status summary and email to PM for review
- When milestone delayed, update overall status and notify Account Director
- When blocker logged, start escalation timer (if not resolved in 48h, escalate)
- When status changes from On Track to At Risk, notify stakeholders
- Monthly client summary: Aggregate all projects for a client into single report
```

**Outcome**: 
- Reduce status reporting time by 60-70%
- Eliminate "what's the status?" email chains
- Earlier visibility into at-risk projects
- Improved client confidence through transparency

**Discovery Questions**:
- "How many hours per week do your PMs spend on status reporting?"
- "When a client asks for a status update, how quickly can you provide it?"
- "Have you ever been surprised by a project going off track?"

**Industry-Specific Context**: 
WIP (Work in Progress) meetings = internal status reviews. "Account team" = client-facing staff. "Traffic light status" = green/yellow/red indicators.

---

### 5. SOW & Estimate Management
**Relevance**: Medium  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Creating accurate estimates and scopes of work is time-consuming and inconsistent. Different people estimate differently. Historical data exists but isn't leveraged. Result: some projects underscoped (lose money), others overscoped (lose the pitch). And once the SOW is signed, tracking against it is manual.

**Solution**: 
monday.com estimate builder with AI-powered suggestions based on historical data. Enter project type and parameters; AI suggests hours by role based on similar past projects. Track SOW against actuals automatically. Build a learning system that gets smarter with every completed project.

**Vibe Prompt**:
```
Build an Estimate & SOW Management app for advertising agency operations and business development.

Purpose: Create accurate project estimates, manage SOWs, and track scope throughout project lifecycle.

Key features:
- Estimate builder: Project type (campaign, website, brand identity, etc.), Deliverables checklist, Hours by role, Rate by role, Total cost, Target margin, Sell price
- AI estimate assist: Based on project type and parameters, suggest hours from similar past projects
- SOW template library: Standard templates by project type, customizable
- Scope tracker: Link SOW to project, track hours vs SOW by role/deliverable
- Change order management: Log scope changes, get approval, adjust SOW
- Version history: Track all estimate/SOW versions and changes
- Win/loss tracking: Log whether estimates won, lost, or were negotiated
- Benchmarking database: Actual hours vs estimated, by project type
- Dashboard: Estimates in progress, Win rate by project type, Average variance (actual vs estimated), Change orders this month

Include automations:
- When estimate created for a project type, pull historical average and suggest
- When project completes, calculate variance and feed into benchmark database
- When scope change requested, create change order template and notify Account Director
- Alert if estimate variance history suggests under-scoping risk
- Monthly estimating accuracy report to Ops Director
```

**Outcome**: 
- Improve estimate accuracy by 20-30%
- Reduce time to create estimates by 40%
- Win more pitches with better-calibrated pricing
- Build institutional knowledge that survives staff turnover

**Discovery Questions**:
- "How accurate are your estimates? Do you track estimated vs actual hours?"
- "How long does it take to put together an estimate for a new project?"
- "Do different people estimate the same project differently?"

**Industry-Specific Context**: 
SOW = Scope of Work. "Estimate" in agency context includes hours by discipline, rates, and often assumptions/exclusions. "Change order" = formal scope amendment. Retainer vs project billing models.

---

### 6. Vendor & Freelancer Management
**Relevance**: Medium  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Agencies rely heavily on freelancers and vendors (production houses, photographers, developers, printers). Managing this extended workforce is chaotic: who's available, what are their rates, how good are they, are their contracts current, are they paid? Each PM maintains their own "little black book."

**Solution**: 
monday.com vendor/freelancer database with performance tracking, contract management, and payment tracking. AI recommends best-fit freelancers based on project needs, availability, and past performance. Centralize the "little black book" so knowledge isn't lost when PMs leave.

**Vibe Prompt**:
```
Build a Vendor & Freelancer Management app for advertising agency operations.

Purpose: Centralize freelancer/vendor relationships, track performance, and manage contracts and payments.

Key features:
- Vendor database: Company/individual name, Type (freelancer/production company/photographer/developer/printer/other), Specialties, Day rate/hourly rate, Location, Contact info, Portfolio link
- Contract tracking: Contract on file (Y/N), Contract expiration, NDA on file, Insurance verified
- Performance ratings: Quality (1-5), Timeliness (1-5), Communication (1-5), Value (1-5), Overall rating, Comments/notes
- Assignment history: Projects worked on, Hours, Spend, Ratings from each PM
- AI recommendation: When a role/specialty is needed, suggest top-rated available vendors
- Invoice tracking: Invoices submitted, Approved, Paid, Outstanding
- Availability calendar: Mark vendor availability for upcoming periods
- Dashboard: Active vendors this month, Spend by vendor, Top-rated by specialty, Contracts expiring soon, Invoices pending approval

Include automations:
- When new vendor added, send contract and NDA for signature
- When contract expires in 30 days, alert Ops Manager
- When project completes, prompt PM to rate vendor
- When invoice submitted, route to PM for approval then to Finance
- Monthly vendor spend report to Finance Director
```

**Outcome**: 
- Reduce time finding the right freelancer by 60%
- Improve vendor quality through centralized ratings
- Eliminate compliance risk (contracts, insurance)
- Never lose institutional knowledge when PMs leave

**Discovery Questions**:
- "How do your PMs find freelancers today? How much time does that take?"
- "What happens when a PM leaves? Does their vendor knowledge leave with them?"
- "How do you track whether a freelancer delivered quality work?"

**Industry-Specific Context**: 
"Day rate" = standard rate for a full day of work. IR35/W-2 considerations for regular freelancers. "Production company" = external company for video/photo shoots. "Retoucher" = specialist for image editing.

---

## Industry Terminology Glossary

**AGI (Agency Gross Income)** — Revenue minus pass-through costs (media, production, etc.). The "real" revenue agencies use to measure performance.

**Utilization** — Billable hours divided by available hours. Industry benchmark is 65-75%. The single most important efficiency metric for agencies.

**Billable Hours** — Hours that can be charged to a client (vs. internal meetings, admin, business development).

**Over-Service** — Delivering more hours than scoped/billed. A profitability killer.

**Write-Off** — Hours worked but not billed. Sometimes intentional (goodwill), sometimes accidental (scope creep).

**Scope Creep** — When project requirements expand beyond the original SOW without formal change order.

**SOW (Scope of Work)** — Document defining project deliverables, timelines, and fees.

**Retainer** — Ongoing monthly fee for a set scope of services (vs. project-based billing).

**Traffic/Trafficking** — Routing creative assets to media destinations (publishers, platforms, etc.).

**Flight Date** — When a campaign goes live.

**WIP (Work in Progress)** — Active projects being worked on but not yet completed/billed.

**Rate Card** — Standard hourly rates by role/seniority level.

---

## Typical Stakeholder Roles

**Primary Buyer: VP/Director of Operations**
- Title: VP Operations, Director of Project Management, COO (at smaller agencies)
- Concerns: Utilization, profitability, resource efficiency, process standardization
- Decision driver: "Can I do more work without adding headcount?"

**Technical Evaluator: Project Management Lead**
- Title: Director of PM, Senior Producer, Head of Traffic
- Concerns: Ease of use, adoption by PMs, reporting flexibility, integration with existing tools
- Decision driver: "Will my PMs actually use this?"

**Executive Sponsor: Managing Director / Agency CEO**
- Title: Managing Director, President, CEO
- Concerns: Agency profitability, client satisfaction, competitive differentiation
- Decision driver: "Does this help us win more and lose less?"

**Finance Stakeholder: Finance Director / Controller**
- Title: Director of Finance, Controller, CFO
- Concerns: Revenue recognition, project profitability, accurate forecasting
- Decision driver: "Can I see real-time financials, not month-old data?"

**End Users:**
- Project Managers, Producers, Traffic Coordinators, Account Managers, Resource Managers

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Creative** | Asset management, versioning, reviews | Creative workflow management, DAM integration |
| **Account/Client Services** | Client reporting, status updates | Client portal, relationship management |
| **Media** | Trafficking, flight dates, spend tracking | Media planning and buying workflow |
| **Strategy/Planning** | Project briefs, research tracking | Strategic planning workflow |
| **Finance** | Billing, revenue recognition, P&L | Financial management integration |
| **HR** | Resource capacity, skills tracking | HRIS integration, talent management |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| Project Management | Workfront, Asana, Basecamp, Wrike | Full replacement |
| Resource Management | Float, Resource Guru, Forecast | Full replacement or integration |
| Time Tracking | Harvest, Toggl, Clockify | Replace or integrate |
| Agency-Specific | Productive, Kantata (Mavenlink), Scoro | Full replacement |
| Finance | Workamajig, FunctionFox | Replace for project finance; integrate with accounting |
| Spreadsheets | Excel/Sheets for everything | Full replacement |

**Positioning:**
- **vs. Workfront**: "Workfront was built for marketing operations, not agency operations. We're built for how agencies actually work — flexible enough for creative chaos, structured enough for profitability."
- **vs. Spreadsheets**: "You can't scale Excel. When you're managing 50 projects across 15 clients with 40 people, spreadsheets become a liability."
- **vs. Kantata/Productive**: "Those are complex enterprise tools with enterprise implementation timelines. We're powerful enough for your needs and live in 2 weeks, not 6 months."

---

## Common Objections

**Objection**: "Our processes are too unique. No tool works for agencies."

**Response**: "That's exactly why we're not selling you a rigid system. monday.com is a platform you can shape to your process — not the other way around. And with Vibe, you can build custom workflows in minutes. Let us show you how other agencies have configured it for their unique needs."

---

**Objection**: "We've tried project management tools before. People don't adopt them."

**Response**: "Adoption fails when tools are too complex or don't fit how people actually work. monday.com is designed to be intuitive — people actually enjoy using it. And our AI Sidekick reduces the admin burden that makes people resent PM tools. What if your PMs spent less time updating statuses because the system updated itself?"

---

**Objection**: "We already have tools for this. We use Harvest, Float, and Asana."

**Response**: "Right — three tools that don't talk to each other. Your people are copying data between systems, and you're paying for three tools instead of one. What if you could consolidate? One platform for projects, resources, time, and finance — with AI connecting the dots you currently connect manually."

---

*Playbook Version: 1.0*  
*Industry: Advertising & Marketing*  
*Department: Operations*  
*Last Updated: 2026-02-11*
