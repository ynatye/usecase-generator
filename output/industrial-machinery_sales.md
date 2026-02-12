# Industrial Machinery & Equipment × Sales Playbook

## Overview

Sales in industrial machinery and equipment is complex, technical, and high-stakes. Unlike transactional sales, industrial machinery deals involve long cycles (6-24 months), multiple stakeholders (engineering, operations, finance, executives), significant capital investment ($100K-$10M+), and often customization or configuration requirements. Sales teams must be part technical consultant, part business advisor, part relationship manager.

The Sales function typically spans direct sales (own salesforce selling to end customers), channel sales (working through distributors and dealers), application engineering (technical support for sales), and sales operations (quoting, forecasting, CRM). Teams range from 10-500+ depending on company size and go-to-market model.

What makes this combination unique: Industrial machinery sales requires deep technical knowledge — salespeople must understand applications, specifications, and competitive differentiation. Deals are won on total cost of ownership, not just price. After-market (parts, service) is often more profitable than equipment sales. Increasingly, "selling machinery" is becoming "selling outcomes" as IoT and servitization transform business models.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - Sales resources are expensive and scarce
   - Technical sales support is a bottleneck
   - AI enables salespeople to be more productive and self-sufficient
   
2. **Consolidate Tech Stack with AI** — HIGH RELEVANCE
   - Sales uses many disconnected tools (CRM, quoting, configurators, documents)
   - Integration gaps create manual work and errors
   - One platform connecting customer data, opportunities, and quotes improves efficiency

3. **Replace or Radically Augment Headcount** — MEDIUM RELEVANCE
   - Some sales tasks (proposal assembly, basic quoting, data entry) are automatable
   - Focus on augmentation to enable more selling time
   - AI as a "technical assistant" for salespeople

---

## Prioritized Use Cases

### 1. Opportunity Management & CRM
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
Industrial machinery sales cycles are long and complex. Opportunities involve multiple contacts, technical requirements, competitive situations, and milestone events. Generic CRMs don't capture the richness needed. Forecasting is unreliable because the data isn't there.

**Solution**: 
monday.com CRM designed for complex industrial sales. Capture technical requirements, track multiple stakeholders, manage long cycles with stage-appropriate milestones, and forecast based on meaningful signals, not gut feel.

**Vibe Prompt**:
```
Build an Opportunity Management app for industrial machinery sales teams.

Purpose: Track complex equipment sales opportunities from lead to close with full context and accurate forecasting.

Key features:
- Opportunity board: Account, Project name, Application, Estimated value, Products, Stage, Close date, Owner
- Industrial sales stages: Lead → Qualified → Application Review → Quote → Negotiation → Order → Won/Lost
- Technical requirements: Application details, Performance requirements, Environment, Integration needs
- Stakeholder mapping: Decision makers, Influencers, Technical evaluators, Procurement, Champions — with relationship status
- Competitive tracking: Known competitors, Their status, Competitive positioning
- Milestone tracking: Key events (site visit, demo, trial, proposal review) with dates
- AI forecast scoring: Score opportunities based on activity, engagement, and historical patterns
- Revenue forecasting: Weighted pipeline by stage, By product, By region
- Dashboard: Pipeline by stage, Forecast vs quota, Win rate, Average deal size, Cycle time

Include automations:
- When opportunity created, prompt for application requirements
- When stage advances, update probability and notify team
- When close date approaches, prompt for action
- Weekly forecast review for sales leadership
- When opportunity won/lost, trigger win/loss analysis
```

**Outcome**: 
- Better visibility into complex opportunities
- More accurate forecasting
- Earlier identification of at-risk deals
- Institutional knowledge captured (not in salesperson heads)

**Discovery Questions**:
- "How long is your average sales cycle? Does your CRM support that complexity?"
- "How accurate is your sales forecast? What would better accuracy mean for the business?"
- "When a salesperson leaves, how much opportunity knowledge walks out the door?"

**Industry-Specific Context**: 
Industrial sales cycles: 6-18 months typical, 24+ for major projects. Multiple stakeholders always involved. "Application" = specific use case and requirements. Site visits and demos are critical milestones.

---

### 2. Quotation & Proposal Management
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Creating quotes for industrial machinery is time-consuming and error-prone. Pricing is complex (base machine, options, accessories, freight, installation). Product configurations must be validated. Proposals require customization. Sales spends too much time on quote administration instead of selling.

**Solution**: 
monday.com quote management with configuration logic and proposal generation. Sales configures the product, pricing calculates automatically, proposals are generated from templates, and approvals are routed appropriately. AI assists with pricing optimization and proposal content.

**Vibe Prompt**:
```
Build a Quotation & Proposal app for industrial machinery sales teams.

Purpose: Create accurate quotes and professional proposals faster with configuration logic and automation.

Key features:
- Quote builder: Select products, Configure options, Add accessories, Calculate pricing (list, discount, net), Freight and installation estimates
- Configuration validation: Rules to prevent invalid combinations, Required options, Dependencies
- Pricing logic: List prices, Standard discounts, Volume discounts, Custom pricing (with approval)
- Multi-line quotes: Multiple machines or product lines in one quote
- AI pricing assist: Suggest discounts based on deal size, customer history, competitive situation
- Proposal generation: Generate formatted proposal documents from templates, Include technical specs, terms
- Approval workflow: Route for approval based on discount level, deal size, custom terms
- Quote versioning: Track revisions, Compare versions
- Dashboard: Quotes outstanding, Quote-to-order conversion, Average discount, Approval bottlenecks

Include automations:
- When configuration complete, validate and calculate pricing
- When discount exceeds threshold, route for approval
- When quote generated, create PDF and notify customer
- When quote expires, prompt salesperson
- Monthly quoting metrics report
```

**Outcome**: 
- 50% faster quote turnaround
- Fewer configuration errors
- Professional, consistent proposals
- Better discount control

**Discovery Questions**:
- "How long does it take to create a quote? How many people touch it?"
- "How often do configuration errors make it to customers?"
- "What's your quote-to-order conversion rate? Could better proposals improve it?"

**Industry-Specific Context**: 
Industrial quotes are complex: base machine, options, accessories, spare parts packages, installation, training. "Configuration rules" prevent invalid combinations. Approvals needed for discounts beyond standard.

---

### 3. Technical Application Support
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Industrial machinery sales requires technical support — salespeople need help sizing machines, selecting options, understanding applications. Application engineers are scarce and bottlenecked. Salespeople wait days for answers or guess and get it wrong.

**Solution**: 
monday.com technical support system with AI-powered application guidance. Salespeople submit application questions, AI suggests answers from knowledge base, and application engineers handle only complex cases. Build a learning system that gets smarter over time.

**Vibe Prompt**:
```
Build a Technical Application Support app for industrial machinery sales teams.

Purpose: Provide fast technical support for sales with AI-powered guidance and expert escalation.

Key features:
- Support request: Salesperson, Customer, Application description, Question type (Sizing/Selection/Application/Competitive), Urgency
- AI application guide: Based on request, suggest relevant application notes, sizing guides, past similar cases
- Knowledge base: Technical documents, Application notes, Case studies, FAQ — searchable and AI-accessible
- Expert queue: Requests requiring human expertise routed to application engineers
- Response tracking: Time to first response, Time to resolution, Resolution quality rating
- Learning capture: When new questions answered, add to knowledge base
- Proactive alerts: AI identifies applications that typically need support, Prompts salesperson
- Dashboard: Support requests by type, Resolution time, Self-service rate, Top question categories

Include automations:
- When request submitted, AI searches knowledge base and suggests answers
- If AI confidence high, provide immediate self-service response
- If AI confidence low, route to application engineer with AI suggestions
- When expert provides answer, prompt to update knowledge base
- Weekly support metrics to application engineering leadership
```

**Outcome**: 
- Faster answers for sales (hours, not days)
- Application engineers focus on complex cases
- Knowledge captured and grows over time
- Better technical support scales without adding headcount

**Discovery Questions**:
- "How long do salespeople wait for technical answers? What does that delay cost in deals?"
- "How much of your application engineers' time is spent on questions that have been answered before?"
- "When a new application question is answered, does that knowledge get captured?"

**Industry-Specific Context**: 
"Application engineering" = technical sales support for sizing, selection, application fit. Common questions: machine sizing, option selection, material compatibility, integration requirements.

---

### 4. Channel & Dealer Management
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Many industrial machinery companies sell through dealers and distributors. Managing the channel is complex: deal registration, territory management, co-selling, training, and performance tracking. Information flows poorly, and manufacturers often don't know about opportunities until it's too late to help.

**Solution**: 
monday.com partner portal and channel management. Dealers register opportunities, request support, and access resources. Manufacturers track channel pipeline, provide support, and manage performance. Everyone has visibility without endless phone calls and emails.

**Vibe Prompt**:
```
Build a Channel & Dealer Management app for industrial machinery sales teams.

Purpose: Manage dealer relationships, deal registration, and channel performance.

Key features:
- Dealer database: Dealer name, Territory, Products authorized, Tier/level, Primary contacts, Performance metrics
- Deal registration: Dealer submits opportunities for protection and support, Registration status (Pending/Approved/Protected)
- Channel pipeline: View dealer-registered opportunities, Support status, Expected close
- Support requests: Dealers request technical support, demo units, joint sales calls
- Resource library: Dealer access to marketing materials, technical documents, pricing
- Training tracking: Dealer certifications, Training completions, Expiring certifications
- Performance scorecard: Sales vs quota, Growth, Training completion, Support ticket quality
- Territory management: Assignments, Conflicts, Coverage gaps
- Dashboard: Channel pipeline, Deal registrations, Support queue, Performance by dealer

Include automations:
- When deal registered, auto-approve if within rules, Route exceptions for review
- When registration approved, notify dealer and internal team
- When dealer requests support, route to appropriate internal resource
- When certification expiring, notify dealer
- Monthly channel performance report
```

**Outcome**: 
- Better visibility into channel pipeline
- Faster deal registration and support
- Improved dealer relationships
- Data-driven performance management

**Discovery Questions**:
- "How do you manage deal registration today? How quickly do dealers get responses?"
- "Do you have visibility into what your dealers are working on?"
- "How do you identify high-performing vs. underperforming dealers?"

**Industry-Specific Context**: 
"Deal registration" = dealer claims an opportunity for protection/support. "Protected" = manufacturer won't sell direct. "Co-sell" = manufacturer and dealer sell together. "Tier" = dealer classification by volume/capability.

---

### 5. Installed Base & After-Market Sales
**Relevance**: Medium-High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
The equipment installed base is a goldmine for parts, service contracts, upgrades, and replacements. But many manufacturers don't know what's installed where, don't proactively market to the installed base, and miss renewal opportunities. After-market sales are reactive, not proactive.

**Solution**: 
monday.com installed base management connected to sales. Know what equipment is at each customer, track warranty/service contract status, and proactively pursue upgrade and replacement opportunities. AI identifies the best opportunities based on equipment age and customer behavior.

**Vibe Prompt**:
```
Build an Installed Base Sales app for industrial machinery sales teams.

Purpose: Track installed equipment and drive after-market sales (parts, service, upgrades, replacements).

Key features:
- Installed base registry: Customer, Site, Equipment (serial #, model), Install date, Warranty expiration, Service contract status
- Proactive opportunities: Upgrades available, Replacement due (based on age/usage), Service contract renewals
- AI opportunity scoring: Score installed base accounts by opportunity potential (age, usage, contract status)
- Campaign management: Target installed base segments for specific offers (upgrade campaigns, service promotions)
- Parts order history: Track parts purchases by customer/equipment
- Service contract sales: Quote and manage service contract renewals
- Competitive replacement: Track competitive equipment at accounts, Displacement opportunities
- Dashboard: Installed base by product, Contract coverage rate, Warranty expirations, Top opportunities

Include automations:
- When warranty expiring in 90 days, create service contract opportunity
- When equipment reaches replacement age, alert salesperson
- When upgrade announced, identify installed base targets
- Monthly installed base opportunity report
- AI digest: Top after-market opportunities this month
```

**Outcome**: 
- Proactive after-market sales (not just reactive)
- Higher service contract attach rates
- Better customer relationships through proactive service
- Increased parts and upgrade revenue

**Discovery Questions**:
- "Do you know what equipment is installed at each customer? Is it in your CRM?"
- "What's your service contract attach rate? How do you drive renewals?"
- "How do you identify upgrade and replacement opportunities?"

**Industry-Specific Context**: 
After-market often 30-50% of revenue, higher margin than equipment. "Attach rate" = % of equipment with service contracts. "Replacement cycle" varies by industry and equipment type.

---

### 6. Sales Performance & Analytics
**Relevance**: Medium  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Sales leadership lacks visibility into performance drivers. They see bookings but not the activities that lead to bookings. Coaching is based on gut feel, not data. Performance varies widely between reps, but the reasons aren't clear.

**Solution**: 
monday.com sales analytics connecting activities to outcomes. Track leading indicators (activities, pipeline), lagging indicators (bookings, revenue), and the conversion rates between them. AI identifies what top performers do differently and suggests improvements for others.

**Vibe Prompt**:
```
Build a Sales Performance Analytics app for industrial machinery sales leadership.

Purpose: Analyze sales performance from activities to outcomes with insights for coaching and optimization.

Key features:
- Activity tracking: Calls, visits, demos, proposals — logged by salesperson
- Pipeline metrics: Opportunities created, Advanced, Won/Lost — with conversion rates
- Bookings and revenue: Monthly/quarterly tracking, By rep, By product, By region
- Leading vs lagging indicators: Correlate activities to pipeline, Pipeline to bookings
- Performance comparison: Compare reps on common metrics, Identify top performer patterns
- AI performance insights: What differentiates top performers? What activities correlate with success?
- Coaching recommendations: AI-suggested focus areas for each rep
- Quota tracking: Progress vs quota, Forecast accuracy
- Dashboard: Team performance, Individual scorecards, Activity trends, Pipeline health, Conversion rates

Include automations:
- Weekly performance summary to each rep
- When rep's metrics decline, alert manager
- Monthly coaching report with AI recommendations
- Quarterly business review data auto-compiled
- Annual performance analysis
```

**Outcome**: 
- Data-driven performance management
- Earlier intervention for struggling reps
- Replicable best practices from top performers
- More accurate forecasting

**Discovery Questions**:
- "Do you know what activities your best reps do that others don't?"
- "How do you coach salespeople? Based on what data?"
- "What's the variance in performance between your best and average reps?"

**Industry-Specific Context**: 
Industrial sales metrics: opportunities, quotes, bookings, win rate, average deal size, cycle time. Activity metrics vary (site visits important in capital equipment). Territory/region performance is important.

---

## Industry Terminology Glossary

**OEM** — Original Equipment Manufacturer; sometimes the machinery company, sometimes their customer who integrates equipment into their own products.

**Distributor/Dealer** — Independent company that sells the manufacturer's products in a territory.

**Application Engineering** — Technical function supporting sales with sizing, selection, and application expertise.

**Installed Base** — Total equipment deployed at customer sites; source of after-market revenue.

**Service Contract** — Agreement for ongoing maintenance, repairs, parts; recurring revenue.

**Attach Rate** — Percentage of equipment sales that include service contracts or accessories.

**Lead Time** — Time from order to delivery; critical in capital equipment sales.

**TCO (Total Cost of Ownership)** — Full cost including purchase, operation, maintenance, energy; used in value selling.

**Capital Appropriation** — Customer's internal process to approve capital purchases; often lengthy.

**Turnkey** — Complete solution including installation, commissioning, and training.

---

## Typical Stakeholder Roles

**Primary Buyer: VP/Director of Sales**
- Title: VP Sales, Director of Sales, Chief Revenue Officer
- Concerns: Revenue growth, forecast accuracy, sales productivity, channel effectiveness
- Decision driver: "Can we sell more with the same team?"

**Technical Evaluator: Sales Operations / CRM Administrator**
- Title: Sales Operations Manager, CRM Administrator, Sales Enablement
- Concerns: Tool adoption, data quality, integration with existing systems, reporting
- Decision driver: "Will salespeople actually use this? Can we get the data we need?"

**Executive Sponsor: CEO / General Manager**
- Title: CEO, General Manager, President
- Concerns: Revenue, market share, sales efficiency, customer relationships
- Decision driver: "Will this help us grow and win against competition?"

**Channel Stakeholder: Channel Sales Director**
- Title: Director of Channel Sales, Partner Manager
- Concerns: Dealer management, deal registration, channel visibility
- Decision driver: "Can we manage our channel better and grow channel revenue?"

**End Users:**
- Sales representatives, Application engineers, Channel managers, Sales managers

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Product & R&D** | Product configurations, Custom requirements | Product development visibility |
| **Service** | Installed base, Service contracts, Field issues | Field service management |
| **Operations** | Order processing, Delivery scheduling | Order management |
| **Marketing** | Leads, Campaigns, Content | Marketing automation |
| **Finance** | Pricing, Credit, Revenue recognition | Financial management |
| **Manufacturing** | Availability, Lead times, Custom orders | Production planning |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| CRM | Salesforce, Microsoft Dynamics | Replace or augment |
| Configure-Price-Quote | Salesforce CPQ, Oracle CPQ, custom | Replace for simpler needs |
| Dealer Portal | Custom development, distributor platforms | Full replacement |
| Analytics | Tableau, Power BI, CRM reporting | Replace for sales analytics |
| Documents | SharePoint, file shares | Replace with integrated content |

**Positioning:**
- **vs. Salesforce**: "Salesforce is built for high-volume transactional sales. Industrial machinery sales is complex, technical, and long-cycle. You need a platform flexible enough to capture application requirements, manage long relationships, and handle technical sales support — without Salesforce's complexity and cost."
- **vs. Custom Systems**: "Your quoting system is 15 years old and held together with duct tape. Your dealer portal is a spreadsheet. Building custom is expensive and fragile. monday.com gives you modern capabilities you can configure yourself."
- **vs. Spreadsheets**: "Your forecast is a spreadsheet aggregation exercise every month. Your installed base is scattered across systems and heads. You're managing a multi-million dollar sales operation with tools from 1990."

---

## Common Objections

**Objection**: "We have Salesforce."

**Response**: "Salesforce can be great for core CRM, but is it handling your technical application support? Your dealer management? Your installed base? Industrial machinery sales has unique requirements that generic CRM doesn't address. monday.com can augment Salesforce for what it doesn't do well — or replace it entirely with something purpose-built for how you actually sell."

---

**Objection**: "Our salespeople won't adopt another tool."

**Response**: "Salespeople adopt tools that make them money. If the tool helps them find information faster, generate quotes faster, and close deals faster, they'll use it. If it's just CRM data entry, they won't. monday.com is designed to help salespeople sell, not to be a management surveillance system."

---

**Objection**: "Our business is too complex for a standard platform."

**Response**: "That complexity is exactly why you need a flexible platform. monday.com isn't a rigid application — it's a platform you configure for your business. Custom configurations, multi-line quotes, long sales cycles, channel management — we can handle it. Let us show you how similar companies have configured it."

---

*Playbook Version: 1.0*  
*Industry: Industrial Machinery & Equipment*  
*Department: Sales*  
*Last Updated: 2026-02-11*
