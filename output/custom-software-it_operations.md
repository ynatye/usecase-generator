# Custom Software & IT Services × Operations Playbook

## Overview

Operations in custom software and IT services companies is the engine that delivers on promises. Unlike product companies with fixed offerings, services businesses sell time, expertise, and outcomes — making operational excellence the difference between profit and loss. Every hour matters; every resource decision has margin implications.

The Operations function typically spans project delivery (managing client engagements), resource management (staffing projects with the right people), practice operations (supporting service lines), and operational excellence (utilization, efficiency, profitability). At services firms (100-5,000+ employees), operations teams range from 5-50+ people depending on company size and delivery model.

What makes this combination unique: Services businesses live and die by utilization (percentage of time billed). The challenge is matching talent to projects while maintaining quality, managing client expectations, and keeping people from burning out. Unlike product businesses, you can't inventory your product — every hour not sold is gone forever. AI can optimize resource allocation, predict project issues, and give real-time visibility into the metrics that matter.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - Services businesses must grow revenue without proportional overhead growth
   - Operations teams are lean relative to delivery staff
   - AI enables operations to manage more people and projects with the same team
   
2. **Replace or Radically Augment Headcount** — HIGH RELEVANCE
   - Resource management, status collection, and reporting are time-intensive
   - Operations staff can shift from administrative tasks to strategic work
   - AI automates routine coordination

3. **Consolidate Tech Stack with AI** — MEDIUM RELEVANCE
   - Services companies use many tools (PSA, time tracking, HRIS, finance)
   - Integration gaps create manual reconciliation
   - One platform reduces overhead

---

## Prioritized Use Cases

### 1. Resource Management & Staffing
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Finding the right person for each project is a constant challenge. Who has the right skills? Who's available? Who's already burned out? Staffing decisions are made in silos, often based on relationships rather than data. The result: suboptimal matches, over-allocation, and utilization gaps.

**Solution**: 
monday.com resource management with skills matching and availability tracking. See who's available with what skills, match to project needs, and balance workload across the team. AI suggests optimal staffing and predicts conflicts.

**Vibe Prompt**:
```
Build a Resource Management app for IT services operations teams.

Purpose: Match talent to projects based on skills, availability, and capacity while optimizing utilization.

Key features:
- People database: Name, Role (Developer/Consultant/Architect/PM/Analyst), Skills (taggable), Certification, Seniority, Cost rate, Bill rate, Manager
- Skills matrix: Skills by person, Proficiency levels, Certifications, Skill gaps
- Availability view: Allocated hours vs available hours, By person, By week
- Project staffing: Each project shows required roles/skills, Assigned people, Hours allocated, Date range
- AI matching: When a role needed, Suggest best-fit people based on skills + availability + past performance
- Utilization dashboard: Target (e.g., 75-80%) vs Actual, By person, By team, By practice
- Conflict detection: Flag over-allocation (>100%), Flag underutilization (<50%)
- Bench management: Track people without assignments, Skills available, Time until next engagement
- Dashboard: Current utilization, Bench hours, Skills in demand, Staffing requests pending, Capacity forecast

Include automations:
- When project staffing request created, AI suggests top candidates
- When utilization >100%, alert resource manager and person's manager
- When person on bench >2 weeks, alert resource manager
- Weekly utilization report to practice leaders
- When skill gap identified across projects, flag for training/hiring
```

**Outcome**: 
- Improved utilization (significant revenue impact)
- Better project outcomes through right-fit staffing
- Reduced burnout through balanced allocation
- Faster staffing decisions

**Discovery Questions**:
- "What's your current utilization rate? What would a 5-point improvement mean in revenue?"
- "How do you match people to projects? How much time does that take?"
- "How often are people over-allocated? Under-utilized?"

**Industry-Specific Context**: 
Utilization target typically 70-85% for consulting; varies by role (PMs lower, developers higher). "Bench" = people without client work. "Chargeability" = another term for utilization.

---

### 2. Project Delivery & Health Monitoring
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
With dozens or hundreds of concurrent projects, operations struggles to maintain visibility. Status is collected manually (if at all), problems surface late, and interventions come after damage is done. Leadership asks "how are our projects doing?" and gets different answers depending on who's asked.

**Solution**: 
monday.com project portfolio with automated health monitoring. Real-time status based on actual data (time, milestones, client feedback), AI-powered risk detection, and proactive alerting before projects go red.

**Vibe Prompt**:
```
Build a Project Portfolio Health app for IT services operations teams.

Purpose: Monitor all client projects with automated health scoring and early risk detection.

Key features:
- Project board: Client, Project name, Type (T&M/Fixed Price/Managed Services), PM, Status, Health score, Revenue
- Health scoring: Automated based on budget burn vs completion, Milestone adherence, Resource stability, Client feedback
- AI risk detection: Predict projects likely to have issues based on patterns
- Milestone tracking: Key milestones, Planned vs actual dates, Variance
- Budget tracking: Contracted value, Recognized revenue, Estimate to complete, Margin
- Issue log: Project issues with severity, Owner, Resolution status
- Client satisfaction: Feedback scores, CSAT tracking
- Drill-down: Click to see project details, Team, Timeline, Financials
- Dashboard: All projects by health, Revenue at risk, Milestones this week, Client satisfaction trends

Include automations:
- When health score drops, alert PM and delivery manager
- When milestone missed, update health and log issue
- When budget burn exceeds threshold, alert operations
- Weekly portfolio summary to leadership
- When client feedback negative, escalate to account manager
```

**Outcome**: 
- Real-time visibility into project health
- Earlier intervention on troubled projects
- Reduced write-offs and margin erosion
- Improved client satisfaction

**Discovery Questions**:
- "How do you know which projects are in trouble? How early do you find out?"
- "What percentage of your projects are profitable? Do you know in real-time?"
- "How much time does operations spend collecting status?"

**Industry-Specific Context**: 
Project types: T&M (Time & Materials), Fixed Price, Managed Services. Each has different margin dynamics. "ETC" = Estimate to Complete. "Revenue at risk" = revenue from troubled projects.

---

### 3. Time Tracking & Revenue Recognition
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
Time tracking is the lifeblood of services businesses — it drives billing, utilization, and project costing. But getting people to track time accurately and on time is an eternal struggle. Late timesheets delay billing and create bad data.

**Solution**: 
monday.com time tracking integrated with projects and people. Easy entry, reminders for overdue time, approval workflow, and direct connection to billing and revenue recognition.

**Vibe Prompt**:
```
Build a Time Tracking & Billing app for IT services operations teams.

Purpose: Capture time accurately, approve it efficiently, and connect to billing.

Key features:
- Time entry: By person, By project/task, Date, Hours, Billable (Y/N), Description
- Multiple entry methods: Daily log, Weekly timesheet, Timer, Quick entry
- Approval workflow: Submitted → PM approval → Client approval (if required) → Approved
- Overdue tracking: Flag missing timesheets, Escalate if not submitted
- Billable vs non-billable: Categorize time, Track reasons for non-billable
- Rate management: Person rates, Project-specific rates, Client rates
- Billing integration: Generate billing data from approved time
- Revenue recognition: Track recognized vs billed vs collected
- Dashboard: Time submitted this week, Pending approvals, Overdue timesheets, Billable %, Revenue summary

Include automations:
- Daily reminder for time entry
- Monday reminder for previous week's time
- When time submitted, route to PM for approval
- When time overdue, escalate to manager
- Weekly utilization report based on submitted time
```

**Outcome**: 
- More accurate, timely time tracking
- Faster billing cycles
- Better utilization data
- Reduced revenue leakage

**Discovery Questions**:
- "What percentage of time is submitted on time? What does late time cost you?"
- "How much of your time is billed vs. written off?"
- "How do you ensure you're capturing all billable time?"

**Industry-Specific Context**: 
"Timesheet compliance" = getting people to submit time on time. "Billable utilization" = hours billed to clients ÷ available hours. "Write-off" = time worked but not billed.

---

### 4. Profitability & Margin Management
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Services profitability is complex — project margins depend on who's staffed, how many hours, and at what rates. Finance sees top-line revenue but project-level profitability is murky. Unprofitable projects are discovered too late to fix.

**Solution**: 
monday.com profitability tracking connecting projects, resources, and time. Real-time margin visibility by project, client, and practice. AI identifies margin erosion patterns and predicts at-risk projects.

**Vibe Prompt**:
```
Build a Project Profitability app for IT services finance and operations teams.

Purpose: Track project margins in real-time and identify profitability risks early.

Key features:
- Project financials: Contract value, Revenue recognized, Cost (hours × cost rates), Gross margin, Margin %
- Real-time cost tracking: Hours logged × person's cost rate = running cost
- Margin tracking: Planned margin vs actual margin, Trend over project life
- AI margin prediction: Predict final margin based on current trajectory
- Client profitability: Aggregate all projects for client, Total relationship margin
- Practice profitability: Margins by service line/practice
- Margin drivers: Why is this project profitable/unprofitable? (staffing, scope, rates)
- Variance analysis: Planned vs actual, Root cause capture
- Dashboard: Portfolio margin, Projects by margin tier, At-risk projects, Client profitability ranking

Include automations:
- When margin drops below threshold, alert PM and operations
- When project closes, calculate final margin and prompt for lessons
- Weekly margin summary to practice leaders
- Monthly profitability review for leadership
- When margin pattern detected (repeated issues), alert operations leadership
```

**Outcome**: 
- Real-time visibility into project profitability
- Earlier intervention on margin erosion
- Better pricing and scoping informed by data
- Improved overall portfolio margin

**Discovery Questions**:
- "Do you know right now which projects are making money and which are losing money?"
- "When you discover a project is unprofitable, is there still time to do something?"
- "What's your average project margin? What would improving it by 2 points mean?"

**Industry-Specific Context**: 
Services margins typically 25-40% gross; varies by service type. Fixed price projects have higher margin risk than T&M. "Margin erosion" = profitability declining over project life.

---

### 5. Operational Reporting & KPIs
**Relevance**: Medium-High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Operations produces reports for many stakeholders — leadership wants utilization and margin, practice heads want team performance, PMs want project status. Creating these reports is time-consuming, and they're often stale by distribution.

**Solution**: 
monday.com automated reporting and dashboards. Self-service access for stakeholders, scheduled reports auto-generated, and AI insights that highlight what matters.

**Vibe Prompt**:
```
Build an Operations Reporting app for IT services leadership.

Purpose: Automate operational reporting and provide self-service access to KPIs.

Key features:
- Dashboard library: Executive dashboard, Practice dashboards, PM dashboards, Finance dashboard
- Key metrics: Utilization, Revenue, Margin, Backlog, Client satisfaction, On-time delivery
- Report templates: Weekly ops report, Monthly practice review, Quarterly business review
- AI narrative generation: Generate executive summary from data
- Scheduled distribution: Auto-generate and email reports on schedule
- Self-service access: Stakeholders view their dashboards anytime
- Trend analysis: Metrics over time, Comparison to targets
- Drill-down: Click metrics to see underlying data
- Dashboard: Report usage, Metric trends, Alerts

Include automations:
- Weekly ops summary auto-generated Monday morning
- Monthly practice reports generated and distributed
- When metric breaches threshold, alert relevant leader
- Quarterly data auto-compiled for business review
- AI insight digest: Key observations this week
```

**Outcome**: 
- Significant reduction in report creation time
- Always-current metrics
- Self-service reduces ad-hoc requests
- Operations focuses on improvement, not reporting

**Discovery Questions**:
- "How much time does operations spend creating reports?"
- "How quickly can you answer 'what's our utilization right now?'"
- "Do stakeholders wait for reports, or can they get information themselves?"

**Industry-Specific Context**: 
Key services metrics: utilization, revenue, margin, backlog, client satisfaction, employee satisfaction. Metrics vary by practice and role type. "Backlog" = contracted work not yet delivered.

---

### 6. Practice & Service Line Management
**Relevance**: Medium  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Services companies are often organized into practices or service lines (e.g., cloud, data, applications). Each practice has its own pipeline, delivery, and people — but cross-practice coordination is weak. Practices compete for resources instead of collaborating.

**Solution**: 
monday.com practice management giving practice leaders visibility into their business while enabling cross-practice coordination. Track practice performance, manage capacity, and identify collaboration opportunities.

**Vibe Prompt**:
```
Build a Practice Management app for IT services practice leaders.

Purpose: Give practice leaders visibility into their business while enabling cross-practice coordination.

Key features:
- Practice dashboard: Revenue, Margin, Utilization, Backlog, Pipeline, Headcount — by practice
- Practice roster: People in practice, Skills, Utilization, Performance
- Practice projects: All projects by practice, Health, Margin
- Resource sharing: Requests to/from other practices, Loans in progress
- Capacity planning: Practice capacity vs demand, Hiring needs
- Skills development: Skills gaps in practice, Training needs, Career development
- Practice pipeline: Opportunities by practice, Win rate
- Cross-practice opportunities: Projects needing multiple practices, Collaboration tracker
- Dashboard: Practice comparison, Resource sharing balance, Skill coverage, Pipeline by practice

Include automations:
- When practice utilization drops below target, alert practice leader
- When resource request made, notify practice resource manager
- Monthly practice performance report
- When skill gap identified, suggest training or hiring
- Quarterly practice planning data auto-compiled
```

**Outcome**: 
- Practice leaders have business visibility
- Better cross-practice resource sharing
- Data-driven practice planning
- Improved overall firm utilization

**Discovery Questions**:
- "How do practice leaders see their business? Do they have dashboards?"
- "How well do practices share resources? Is it collaborative or competitive?"
- "How do you plan capacity and hiring by practice?"

**Industry-Specific Context**: 
Practices = service lines (cloud, data, security, etc.). "Practice leader" = typically P&L responsibility. "Cross-staffing" = using people from other practices. Practices often have different margin profiles.

---

## Industry Terminology Glossary

**Utilization** — Billable hours ÷ available hours. The most important efficiency metric in services.

**T&M (Time & Materials)** — Billing model where client pays for hours worked at agreed rates.

**Fixed Price** — Billing model with agreed total price regardless of hours (higher margin risk).

**Managed Services** — Ongoing service delivery (often monthly) for recurring revenue.

**Bench** — Staff without client assignments; represents cost without revenue.

**Backlog** — Contracted work not yet delivered; forward revenue indicator.

**Chargeability** — Another term for utilization (how much time is chargeable to clients).

**Practice** — Service line or capability area (e.g., cloud, data, security, applications).

**PSA (Professional Services Automation)** — Software category for services operations.

**Write-off** — Time worked but not billed to clients.

---

## Typical Stakeholder Roles

**Primary Buyer: VP/Director of Operations or Delivery**
- Title: VP Operations, Director of Delivery, COO
- Concerns: Utilization, delivery quality, profitability, operational efficiency
- Decision driver: "Can I manage more with the same team while improving delivery?"

**Technical Evaluator: Operations Manager / Resource Manager**
- Title: Operations Manager, Resource Manager, Delivery Manager
- Concerns: Ease of use, integration with existing systems, team adoption
- Decision driver: "Will this actually make resource management and reporting easier?"

**Executive Sponsor: CEO / Managing Partner**
- Title: CEO, Managing Partner, President
- Concerns: Revenue growth, margin improvement, client satisfaction, employee retention
- Decision driver: "Will this help us grow profitably?"

**Finance Stakeholder: CFO / Finance Director**
- Title: CFO, Finance Director, Controller
- Concerns: Revenue recognition, profitability, forecasting, billing accuracy
- Decision driver: "Can I trust the financial data?"

**End Users:**
- Resource managers, Project managers, Practice leaders, Finance team

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Sales** | Pipeline for capacity planning, Deal handoff | CRM integration |
| **HR** | People data, Skills, Capacity | HR and talent management |
| **Finance** | Billing, Revenue recognition, Profitability | Financial management |
| **IT** | Systems, Integrations | IT operations |
| **Practice Teams** | Projects, Resources, Skills | Practice management |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| PSA | Kantata (Mavenlink), Planview, Deltek | Replace |
| Resource Management | Resource Guru, Float, custom | Full replacement |
| Time Tracking | Harvest, Toggl, PSA modules | Replace or integrate |
| Project Management | Jira, Asana, custom | Replace for services context |
| Reporting | Excel, Power BI, Tableau | Replace for operational reports |

**Positioning:**
- **vs. Kantata/Planview**: "Enterprise PSA is expensive and complex. Implementation takes months; adoption takes years. monday.com gives you the same capabilities — resource management, project delivery, profitability — at a fraction of the cost and complexity."
- **vs. Spreadsheets**: "Your utilization report is a weekly exercise in spreadsheet assembly. Your resource management is in people's heads. You're running a multi-million dollar services business with tools from 1990."
- **vs. Point Solutions**: "You have Harvest for time, Float for resources, Asana for projects, and Excel for everything else. None of them talk to each other. What if it was all connected?"

---

## Common Objections

**Objection**: "We have a PSA system already."

**Response**: "How's adoption? How much does it actually get used? Most PSA implementations are shelfware — too complex, too rigid. monday.com isn't a monolithic PSA; it's a flexible platform you can configure for how you actually work. Start with the pain points your PSA doesn't solve."

---

**Objection**: "We're too small for formal operations."

**Response**: "Every services company needs resource management, project visibility, and profitability tracking — even small ones. The question is: do you have it? If utilization lives in someone's head and profitability is a quarterly surprise, you need a system. Small doesn't mean unsophisticated."

---

**Objection**: "Consultants won't use another tool."

**Response**: "Consultants won't use bad tools. They will use tools that make their jobs easier — finding information, tracking time without hassle, seeing project health. The key is keeping it simple and making it valuable. monday.com is designed for people who are allergic to admin."

---

*Playbook Version: 1.0*  
*Industry: Custom Software & IT Services*  
*Department: Operations*  
*Last Updated: 2026-02-11*
