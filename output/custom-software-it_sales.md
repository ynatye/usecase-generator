# Custom Software & IT Services × Sales Playbook

## Overview

Sales in custom software and IT services is consultative selling at its most complex. There's no fixed product to demo, no standard price list, and no simple ROI calculator. Sales teams must understand client business challenges, architect solutions, estimate costs, and navigate long buying cycles with multiple stakeholders — all while competing against firms who can undercut on price.

The Sales function typically spans business development (finding and qualifying opportunities), solution sales (architecting and selling solutions), proposal management (responding to RFPs and creating proposals), and account management (growing existing clients). At services firms, sales teams range from 5-50+ people, often with delivery leadership involved in major deals.

What makes this combination unique: IT services sales cycles are long (3-12 months) and solution-focused. Buyers evaluate team capability, methodology, and cultural fit — not just price. Trust is paramount. Existing clients are often the best source of growth. AI can accelerate research, improve proposals, and give better visibility into what works, but the human relationship remains central.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - Sales teams are expensive; productivity matters
   - Each deal requires significant research and customization
   - AI enables more pipeline coverage and better preparation
   
2. **Replace or Radically Augment Headcount** — HIGH RELEVANCE
   - Proposal writing, research, and data entry consume time
   - Sales professionals should spend time selling, not admin
   - AI as research assistant and writing co-pilot

3. **Consolidate Tech Stack with AI** — MEDIUM RELEVANCE
   - Sales uses many tools (CRM, proposals, research)
   - Integration gaps create manual work
   - Connected data improves insights

---

## Prioritized Use Cases

### 1. Opportunity Management & Pipeline
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
IT services sales cycles are long and complex. Opportunities involve multiple stakeholders, evolving requirements, and competitive dynamics. Generic CRMs don't capture the richness of services sales. Forecasting is unreliable because the data doesn't reflect reality.

**Solution**: 
monday.com CRM designed for services sales. Capture solution requirements, track stakeholder relationships, manage long cycles with appropriate milestones, and forecast based on meaningful signals.

**Vibe Prompt**:
```
Build an Opportunity Management app for IT services sales teams.

Purpose: Track services opportunities from lead through close with full context and accurate forecasting.

Key features:
- Opportunity board: Account, Opportunity name, Service type, Estimated value (TCV), Stage, Owner, Close date
- Services sales stages: Lead → Qualified → Discovery → Solution Design → Proposal → Negotiation → Contract → Won/Lost
- Solution scope: Services needed, Technologies, Team composition, Estimated duration
- Stakeholder mapping: Decision maker, Economic buyer, Champions, Blockers, Technical evaluators
- Competitive tracking: Known competitors, Their position, Our differentiation
- Milestone tracking: Key events (workshops, demos, references, final presentations)
- AI forecast scoring: Score based on activities, engagement, solution fit
- Revenue forecasting: Weighted pipeline by stage, Expected close timing
- Dashboard: Pipeline by stage, Forecast vs quota, Win rate, Average deal size, Cycle time

Include automations:
- When opportunity created, prompt for qualification criteria
- When stage advances, update probability and next actions
- When deal quiet for 14 days, prompt for activity
- Weekly forecast review to leadership
- When won/lost, trigger win/loss analysis
```

**Outcome**: 
- Better visibility into services pipeline
- More accurate forecasting
- Institutional knowledge captured
- Earlier warning on at-risk deals

**Discovery Questions**:
- "How accurate is your sales forecast? What would better accuracy mean?"
- "When a salesperson leaves, how much pipeline knowledge leaves with them?"
- "How do you track where you stand against competitors in a deal?"

**Industry-Specific Context**: 
Services sales cycles: 3-12+ months. "TCV" = Total Contract Value. "Discovery" is crucial — understanding client needs deeply. Stakeholder mapping is essential for complex deals.

---

### 2. Proposal & RFP Management
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Creating proposals and RFP responses is labor-intensive. Each requires understanding requirements, assembling the right content, pricing the solution, and coordinating multiple contributors. Teams work long hours on proposals, often reinventing content that exists somewhere.

**Solution**: 
monday.com proposal management with content library and AI assistance. Track RFP requirements, assemble responses efficiently, coordinate contributors, and use AI to accelerate drafting.

**Vibe Prompt**:
```
Build a Proposal & RFP Management app for IT services sales teams.

Purpose: Create winning proposals faster with content reuse, team coordination, and AI assistance.

Key features:
- Proposal board: Opportunity link, Proposal type (RFP/Proactive/SOW), Due date, Owner, Status
- Requirements parsing: Extract RFP requirements, Track response status for each
- Content library: Reusable proposal sections, Case studies, Bios, Differentiators — searchable
- AI content assist: Generate draft responses from requirements and content library
- Contributor coordination: Section assignments, Due dates, Review status
- Pricing integration: Effort estimates, Rates, Total pricing — with approval workflow
- Review workflow: Draft → Technical review → Leadership review → Pricing review → Final
- Version control: Track changes, Compare versions
- Dashboard: Active proposals, By stage, Win rate by type, Content reuse stats

Include automations:
- When proposal created, generate structure from requirements
- When section assigned, notify contributor with due date
- When draft complete, route to reviewers
- When pricing needs approval, route to approvers
- Post-submission: Schedule follow-up activities
```

**Outcome**: 
- 40-50% faster proposal creation
- Higher content reuse
- Better coordination among contributors
- More competitive proposals

**Discovery Questions**:
- "How long does it take to create a typical proposal?"
- "How much content do you reuse vs. create from scratch?"
- "How do you coordinate multiple contributors on proposals?"

**Industry-Specific Context**: 
RFP responses in IT services are often 50-200+ pages. "Content library" = reusable answers and materials. "Orals" or "final presentations" are often required after written proposals.

---

### 3. Solution & Pricing Development
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Pricing IT services is complex — estimating effort, selecting appropriate rates, structuring pricing models (T&M, fixed, hybrid), and ensuring profitability. Estimation varies by estimator. Margins erode when pricing is wrong.

**Solution**: 
monday.com solution and pricing tool that brings consistency. Estimate effort using historical data, apply appropriate rates, structure pricing, and ensure profitability targets are met.

**Vibe Prompt**:
```
Build a Solution & Pricing app for IT services sales and delivery teams.

Purpose: Create consistent, profitable pricing based on effort estimation and historical data.

Key features:
- Solution builder: Scope elements, Phase breakdown, Deliverables
- Effort estimation: Hours by role, AI-assisted estimation based on similar past projects
- Estimation templates: Standard effort for common project types
- Rate management: Standard rates, Client-specific rates, Discount bands
- Pricing models: T&M calculation, Fixed price, Hybrid, Outcome-based
- Margin calculation: Revenue, Cost (hours × cost rates), Margin, Margin %
- Pricing approval: When discount or margin below threshold, approval required
- Historical comparison: How does this estimate compare to similar projects?
- Dashboard: Proposals by margin, Estimation accuracy (actual vs estimated), Rate trends

Include automations:
- When effort entered, calculate pricing using applicable rates
- When margin below threshold, route for approval
- When similar historical project found, suggest reference
- When pricing approved, lock and store for comparison
- Post-project: Calculate actual vs estimated for calibration
```

**Outcome**: 
- More consistent estimation
- Protected margins through approval workflow
- Learning from historical actuals
- Faster pricing development

**Discovery Questions**:
- "How do you estimate effort for new deals? Is it consistent across estimators?"
- "How accurate are your estimates? Do you track actual vs estimated?"
- "What's your average margin? How much variance is there?"

**Industry-Specific Context**: 
"T&M" = Time & Materials (hours × rate). "Fixed price" = agreed total. "Margin target" varies by firm (typically 25-40% gross). "Cost rate" vs "bill rate" distinction matters.

---

### 4. Account Management & Expansion
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Existing clients are the best source of profitable growth — they already trust you. But account management is often reactive. Cross-sell opportunities are missed. Client relationships aren't systematically nurtured. Growth depends on individual relationship owners.

**Solution**: 
monday.com account management for strategic client growth. Track relationships, identify expansion opportunities, and systematically develop accounts.

**Vibe Prompt**:
```
Build an Account Management app for IT services sales teams.

Purpose: Systematically grow existing client relationships with proactive account planning.

Key features:
- Account overview: Client name, Industry, Relationship length, Total revenue, Current projects, Key contacts
- Account plan: Growth target, Strategies, Initiatives, Timeline
- Relationship mapping: Key contacts, Relationship owner, Last contact, Relationship health
- Opportunity radar: Potential opportunities by service/need, Likelihood, Timing
- Cross-sell tracking: Services not yet sold to this client, Relevance
- Client health: Project satisfaction, Relationship temperature, Risk flags
- Activity tracking: Meetings, Calls, Value-add touches
- White space analysis: Client's full potential vs current revenue
- Dashboard: Accounts by tier, Growth pipeline, At-risk accounts, Cross-sell opportunities

Include automations:
- When account plan due for review, notify account owner
- When relationship contact stale (90 days), prompt for outreach
- When project satisfaction drops, alert account owner
- When cross-sell opportunity identified, create sales activity
- Quarterly account review data compiled
```

**Outcome**: 
- Proactive account development
- More expansion opportunities identified
- Protected client relationships
- Systematic growth from existing clients

**Discovery Questions**:
- "What percentage of revenue comes from existing clients?"
- "Do you have formal account plans for key clients?"
- "How do you identify cross-sell and expansion opportunities?"

**Industry-Specific Context**: 
"Land and expand" model is typical. Client-for-life thinking. "White space" = potential services not yet sold. Account tiering (strategic, key, standard) guides investment.

---

### 5. Sales Intelligence & Research
**Relevance**: Medium-High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Effective services sales requires understanding client context — their business, challenges, technology landscape, and key players. Research takes time. When it's rushed, conversations suffer. Salespeople lack the context to have strategic discussions.

**Solution**: 
monday.com sales intelligence with AI-powered research. For each prospect and deal, compile relevant intelligence. AI researches continuously, surfaces insights, and helps prepare for conversations.

**Vibe Prompt**:
```
Build a Sales Intelligence app for IT services sales teams.

Purpose: Provide rich client context with AI-powered research and insight generation.

Key features:
- Company profile: AI-compiled company overview, Recent news, Technology investments, Key initiatives
- Executive profiles: Key contacts with background, Priorities, Connections
- Technology landscape: Tech stack, Recent changes, Modernization needs
- Industry context: Industry trends, Competitive dynamics, Regulatory changes
- AI insight generation: Based on research, Generate conversation starters, Talking points
- Trigger monitoring: News, Job changes, Earnings, Funding — relevant events
- Competitive intelligence: Competitive wins/losses at account, Competitor positioning
- Research library: Store research by account for reuse
- Dashboard: Accounts with recent triggers, Research coverage, Insight highlights

Include automations:
- When new opportunity created, generate research brief
- When trigger detected, alert account owner
- When meeting scheduled, generate prep brief
- Weekly intelligence digest for major accounts
- When executive change detected, notify and suggest outreach
```

**Outcome**: 
- Better-prepared sales conversations
- Proactive awareness of triggers
- Faster research with AI assistance
- Strategic selling vs. product pitching

**Discovery Questions**:
- "How much time do salespeople spend on research?"
- "How do you prepare for important meetings?"
- "How do you find out about opportunities at target accounts?"

**Industry-Specific Context**: 
Services selling requires business understanding, not just product knowledge. "Trigger events" = situations that create buying intent (new executive, funding, digital transformation announcement).

---

### 6. Win/Loss Analysis & Learning
**Relevance**: Medium  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
When deals close — won or lost — learning usually doesn't happen. Win celebrations don't examine what worked. Loss post-mortems are uncomfortable and avoided. Patterns remain hidden. The same mistakes repeat.

**Solution**: 
monday.com win/loss system capturing and analyzing outcomes. For every significant deal, document why it was won or lost. Identify patterns. Improve continuously.

**Vibe Prompt**:
```
Build a Win/Loss Analysis app for IT services sales leadership.

Purpose: Systematically capture and analyze deal outcomes to improve win rates.

Key features:
- Outcome capture: When opportunity closes, Record outcome, Primary reason, Contributing factors, Competitor (if known)
- Reason taxonomy: Price, Team/capabilities, Methodology, Relationship, Scope fit, References, Timing
- Client debrief: Track whether debrief conducted, Key feedback
- Pattern analysis: AI identifies trends across wins and losses
- Competitor performance: Win/loss record against specific competitors
- Segment analysis: Win rate by industry, Size, Service type
- Recommendations: AI suggests improvements based on patterns
- Dashboard: Win rate trends, Loss reasons, Competitor performance, Patterns

Include automations:
- When opportunity closed, prompt for win/loss analysis (required)
- When loss recorded, schedule debrief attempt
- Quarterly win/loss review with patterns
- When repeated loss reason detected, alert leadership
- Annual win/loss summary generated
```

**Outcome**: 
- Systematic learning from outcomes
- Patterns visible (not hidden)
- Improved win rate over time
- Data-driven sales improvement

**Discovery Questions**:
- "Do you track why you win and lose?"
- "What's your top reason for losing deals? Are you sure?"
- "Have you improved your win rate over time? How do you know?"

**Industry-Specific Context**: 
Services deals often lost on "intangibles" — team chemistry, methodology fit, references. Price is often blamed but rarely the real reason. Client debriefs are valuable but require relationship management.

---

## Industry Terminology Glossary

**T&M (Time & Materials)** — Billing model where client pays for hours worked at agreed rates.

**TCV (Total Contract Value)** — Total value of contract over its duration.

**ACV (Annual Contract Value)** — Annual revenue from a contract; useful for multi-year deals.

**Discovery** — Early sales stage focused on understanding client needs and challenges.

**Solution Selling** — Selling approach focused on solving client problems rather than pushing services.

**RFP (Request for Proposal)** — Formal solicitation from potential client requesting proposals.

**RFI (Request for Information)** — Preliminary inquiry to gather information before RFP.

**Orals** — Final presentation to client evaluation committee; often after written proposal.

**White Space** — Revenue potential in existing accounts not yet captured.

**Land and Expand** — Strategy of starting small with a client and growing the relationship over time.

---

## Typical Stakeholder Roles

**Primary Buyer: VP/Director of Sales**
- Title: VP Sales, Sales Director, Chief Revenue Officer
- Concerns: Revenue growth, forecast accuracy, sales productivity, win rate
- Decision driver: "Can we sell more and win more with our current team?"

**Technical Evaluator: Sales Operations / Enablement**
- Title: Sales Operations Manager, Sales Enablement Lead
- Concerns: Tool adoption, data quality, process efficiency
- Decision driver: "Will salespeople actually use this? Does it help them sell?"

**Executive Sponsor: CEO / Managing Partner**
- Title: CEO, Managing Partner, President
- Concerns: Revenue, profitability, market positioning
- Decision driver: "Will this help us grow the business?"

**Delivery Stakeholder: Delivery Leadership**
- Title: VP Delivery, Practice Leader
- Concerns: Deal quality, scope accuracy, margin protection
- Decision driver: "Will this improve the deals we win?"

**End Users:**
- Sales executives, Account managers, Pre-sales consultants, Delivery leads (on deals)

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Marketing** | Leads, Content, Case studies | Marketing integration |
| **Delivery/Operations** | Resource availability, Project handoff | Operations management |
| **Finance** | Pricing, Revenue recognition | Financial management |
| **HR** | Hiring for sold work | HR integration |
| **Product** | Solution components, Accelerators | Product management |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| CRM | Salesforce, HubSpot, Dynamics | Replace or augment |
| Proposal Management | Qvidian, Loopio, RFPIO | Replace |
| Sales Intelligence | ZoomInfo, LinkedIn Sales Navigator | Augment |
| Contract Management | DocuSign, Ironclad | Integrate |

**Positioning:**
- **vs. Salesforce**: "Salesforce is built for product sales with predictable cycles. Services sales is different — longer cycles, solution complexity, stakeholder depth. You need a platform flexible enough for consultative selling, not a product sales machine."
- **vs. Point Solutions**: "You have CRM for pipeline, a different tool for proposals, spreadsheets for pricing, and nothing connecting them. What if it was integrated?"
- **vs. Spreadsheets**: "Your proposals are copy-paste from old documents. Your pricing is in spreadsheets. Your win/loss data doesn't exist. You're running a sales organization on hope instead of data."

---

## Common Objections

**Objection**: "We have Salesforce."

**Response**: "Salesforce might be fine for pipeline tracking, but is it helping with proposals? Pricing? Account planning? Services sales has unique needs that generic CRM doesn't address. monday.com can augment Salesforce for what it doesn't do well — or replace it with something purpose-built."

---

**Objection**: "Sales is about relationships, not systems."

**Response**: "Absolutely — relationships are central. But relationships don't mean disorganized. Systems capture relationship knowledge so it doesn't walk out the door. They free salespeople from admin so they can spend time on relationships. The best relationship builders use the best tools."

---

**Objection**: "Our sales process is too unique."

**Response**: "Every services firm thinks they're unique — and they're partly right. That's why rigid systems fail. monday.com is flexible; you configure it for your process. We've seen many variations of services sales; let us show you how similar firms have configured it."

---

*Playbook Version: 1.0*  
*Industry: Custom Software & IT Services*  
*Department: Sales*  
*Last Updated: 2026-02-11*
