# Credit Cards & Transaction Processing × Sales Playbook

## Overview

Sales teams in the Credit Cards & Transaction Processing industry operate in a complex ecosystem of merchants, financial institutions, and technology providers. These organizations range from global card networks (Visa, Mastercard) to payment processors (Stripe, Square, Adyen) to acquiring banks and ISOs. Sales teams typically manage multiple channels including direct merchant acquisition, ISO/agent partnerships, enterprise deals, and ISV/platform integrations.

The sales process involves long cycles for enterprise merchants, complex pricing negotiations (interchange-plus models), technical integration requirements, and regulatory compliance considerations. Sales reps must navigate RFP processes, competitive displacement scenarios, and value-added services upselling while managing processing volume commitments and maintaining relationships across the payment ecosystem.

Modern payment sales increasingly focus on embedded payments, API-first developer sales, and vertical-specific solutions, requiring sales teams to be both technically savvy and industry-specialized across sectors like healthcare, restaurants, and e-commerce.

## Value Driver Mapping

| Value Driver | Relevance | Why |
|---|---|---|
| **Replace or Radically Augment Headcount** | High | Sales teams spend 60-70% of time on administrative tasks: RFP responses, competitive research, pricing calculations, ISO partner management, and deal tracking |
| **Consolidate Tech Stack with AI** | High | Payment sales teams juggle 8-15 tools: CRM, proposal tools, pricing calculators, competitive intel, partner portals, compliance tracking, and commission systems |
| **Scale Impact Without Overhead** | Very High | Payment processing is volume-driven; scaling merchant acquisition and partner channels without proportional headcount growth is critical for margin expansion |

## Prioritized Use Cases

---

### Use Case 1: AI-Powered Merchant Acquisition Pipeline

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Sales reps spend 40+ hours per week manually researching prospects, qualifying merchant potential, and tracking outreach across multiple channels. With thousands of potential merchants and limited sales headcount, only 15-20% of qualified prospects receive meaningful follow-up. ISO partners complain about lack of support for their pipeline.

#### The Solution
monday.com AI Agents automatically research merchant prospects, score them based on processing volume potential, track multi-channel outreach, and maintain ISO partner pipeline visibility. Vibe builds custom merchant qualification workflows in minutes, while mondayDB provides unified context across all touchpoints.

#### The Outcome
60% reduction in manual research time, 3x increase in qualified prospect coverage, 40% improvement in merchant acquisition conversion rates, and 2.5x growth in ISO partner satisfaction scores.

#### Discovery Questions
- How many potential merchants are in your pipeline that never get proper follow-up?
- What percentage of your time is spent on prospect research versus actual selling?
- How do you currently support your ISO partners' merchant acquisition efforts?
- What's your average time from initial contact to merchant onboarding?
- How do you track processing volume commitments across your pipeline?

#### Industry Context
Merchant acquisition is the lifeblood of payment processors. Sales teams must balance direct acquisition with ISO/agent channel management, often juggling hundreds of prospects across different risk profiles and processing volumes. Success requires understanding merchant categories, seasonal patterns, and competitive positioning.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a merchant acquisition pipeline board with columns: Merchant Name (text), Industry Vertical (dropdown: Restaurant, Retail, E-commerce, Healthcare, Professional Services), Est Monthly Volume (numbers), ISO/Agent Partner (people picker), Lead Source (dropdown: Direct, Partner, Referral, Inbound), Status (status: Cold Lead, Qualified, Proposal Sent, Technical Review, Contract Review, Closed-Won, Closed-Lost), Last Contact Date (date), Next Action (text), Risk Level (dropdown: Low, Medium, High), Pricing Model (dropdown: Interchange Plus, Flat Rate, Custom), Priority (dropdown: Hot, Warm, Cold). Add automation to notify assigned salesperson when status changes to 'Qualified' and create timeline view showing deal progression by month."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Merchant Acquisition Agent

**Agent Purpose:**  
Automatically research, score, and nurture merchant prospects while managing ISO partner pipelines.

**Triggers:**
- New lead entry from any source (form, integration, manual)
- 7 days since last contact with qualified prospect
- Processing volume estimate updates
- ISO partner requests for pipeline support
- Competitive displacement opportunities identified

**Actions:**
- Research merchant online presence and estimate processing volume
- Score prospects based on industry, size, and fit criteria
- Generate personalized outreach sequences
- Update ISO partners on their referred merchants
- Create competitive battle cards for specific deals
- Schedule follow-up reminders based on merchant response patterns

**Data Required:**
- CRM integration for prospect data
- Industry databases for merchant research
- ISO partner contact information
- Competitive intelligence feeds
- Processing volume benchmarks by industry

**Autonomy Level:** Human-in-the-Loop  
Agent handles research and scoring autonomously, presents recommendations for sales rep approval before taking action on outreach or ISO partner communication.

**Example Interaction:**
> A new restaurant lead comes in from an ISO partner. The agent immediately researches the merchant's online presence, estimates they process $50K monthly based on location and reviews, creates a customized proposal highlighting restaurant-specific features like tip adjustment and offline capability, notifies both the assigned sales rep and ISO partner with next steps, and schedules a follow-up reminder in 3 business days. When the merchant doesn't respond, the agent analyzes similar successful deals and suggests alternative outreach approaches.

---

### Use Case 2: RFP Response Automation & Competitive Intelligence

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Enterprise RFP responses consume 40-80 hours per response, often requiring input from multiple teams (sales, product, legal, compliance). Sales teams simultaneously juggle 5-10 RFPs, leading to rushed responses and lost opportunities. Competitive intelligence is fragmented across sales reps' personal knowledge and outdated battle cards.

#### The Solution
monday.com AI Agents automatically populate RFP responses using historical successful proposals, maintain real-time competitive intelligence, and coordinate cross-functional input. Vibe creates RFP tracking workflows that ensure no deadlines are missed while maintaining proposal quality and compliance requirements.

#### The Outcome
75% reduction in RFP response time, 50% increase in RFP win rate, 100% on-time submission rate, and ability to pursue 3x more opportunities with the same team.

#### Discovery Questions
- How many RFPs does your team handle simultaneously?
- What's your current win rate on RFP responses?
- How often do you miss RFP deadlines due to workload?
- Who needs to review RFP responses before submission?
- How do you stay current on competitive positioning and pricing?

#### Industry Context
Payment processing RFPs are complex documents covering pricing, technical capabilities, compliance, and integration requirements. Enterprise merchants often run lengthy evaluation processes with multiple vendors, making response quality and speed critical differentiators.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an RFP tracking board with columns: RFP Name (text), Client/Prospect (text), Est Deal Value (numbers), Submission Deadline (date), Status (status: Received, In Progress, Review, Submitted, Won, Lost), Lead Sales Rep (people picker), Supporting Teams (people picker multiple), RFP Category (dropdown: Payment Processing, Gateway, POS, Mobile, Enterprise), Competitive Situation (text), Win Probability (dropdown: 25%, 50%, 75%, 90%), Technical Requirements (text), Compliance Needs (text), Next Milestone (date), Review Notes (text). Add automations to notify teams 48 hours before deadline and create dashboard view showing RFP pipeline value and win rates by category."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RFP Response Agent

**Agent Purpose:**  
Automatically draft RFP responses using best practices and coordinate cross-functional review processes.

**Triggers:**
- New RFP document uploaded
- RFP deadline approaching (48-hour warning)
- Competitive intelligence updates relevant to active RFPs
- Technical requirements changes in active proposals
- Review feedback submitted by legal/compliance teams

**Actions:**
- Parse RFP requirements and map to product capabilities
- Generate initial response drafts using successful templates
- Identify knowledge gaps requiring SME input
- Coordinate review schedules across teams
- Update competitive positioning based on latest intelligence
- Track proposal versions and maintain audit trails

**Data Required:**
- Historical winning RFP responses
- Product capability matrices
- Competitive intelligence database
- Compliance requirement templates
- Team calendars for review coordination

**Autonomy Level:** Human-in-the-Loop  
Agent drafts responses autonomously but requires sales rep review before submission. Escalates to humans for non-standard requirements or competitive situations.

**Example Interaction:**
> A large retailer submits an RFP for payment processing services. The agent immediately parses 200+ requirements, identifies that 85% can be answered from existing templates, flags 12 items requiring product team input, generates a preliminary response highlighting the company's retail-specific capabilities, schedules review meetings with legal and compliance teams, and creates a timeline ensuring 3 days before deadline completion. It also identifies that Square is likely competing and surfaces relevant competitive battle cards.

---

### Use Case 3: ISO/Agent Partner Channel Management

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Managing hundreds of ISO partners and agents requires constant communication, training, deal support, and performance tracking. Partner portals are disconnected from CRM systems, leading to poor visibility into partner-generated pipeline. Commission disputes and partner onboarding consume significant time.

#### The Solution
monday.com provides unified partner relationship management with automated partner scorecards, deal registration workflows, and commission tracking. AI Agents proactively support partners with lead nurturing, training reminders, and performance insights.

#### The Outcome
300% increase in partner-generated revenue, 50% reduction in partner support time, 90% faster partner onboarding, and 2x improvement in partner satisfaction scores.

#### Discovery Questions
- How many ISO partners and agents do you currently manage?
- What percentage of your revenue comes through partners versus direct sales?
- How do you track partner performance and commission calculations?
- What's your biggest challenge in supporting partner success?
- How long does it take to onboard new partners?

#### Industry Context
ISO/agent networks are critical distribution channels for payment processors. These partners range from individual sales agents to large ISOs with hundreds of merchants. Managing this ecosystem requires balancing support, incentives, and oversight while maintaining compliance with card network regulations.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a partner management board with columns: Partner Name (text), Partner Type (dropdown: ISO, Agent, Referral Partner), Status (status: Active, Onboarding, Inactive, Terminated), Territory (dropdown: Northeast, Southeast, Midwest, Southwest, West, National), Monthly Volume (numbers), Partner Tier (dropdown: Platinum, Gold, Silver, Bronze), Last Training Date (date), Compliance Status (status: Current, Needs Review, Expired), Assigned Partner Manager (people picker), Commission Rate (numbers), YTD Merchants Boarded (numbers), Pipeline Value (numbers), Next Check-in (date), Performance Notes (text). Add automations to notify partner managers when compliance expires in 30 days and create dashboard showing partner performance metrics by tier and territory."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Partner Success Agent

**Agent Purpose:**  
Automatically nurture ISO/agent relationships and optimize partner channel performance.

**Triggers:**
- New partner onboarding started
- Partner performance metrics change significantly
- Training certification expires within 30 days
- Partner submits deal registration
- Commission dispute flagged

**Actions:**
- Send personalized performance reports to partners
- Schedule training sessions for underperforming partners
- Generate commission statements and resolve disputes
- Identify cross-selling opportunities for partners
- Create territory optimization recommendations
- Escalate high-value partner issues to managers

**Data Required:**
- Partner performance metrics and merchant volume
- Training completion records
- Commission calculation rules
- Territory assignments and performance
- Partner communication preferences

**Autonomy Level:** Fully Autonomous  
Agent handles routine partner communications, training reminders, and performance reporting without human intervention. Escalates only disputes or unusual situations.

**Example Interaction:**
> A Gold-tier ISO partner hasn't submitted any new deals in 45 days. The agent analyzes their historical patterns, identifies this as unusual, sends a personalized check-in message with performance comparison, schedules a training refresher on new product features, and alerts their partner manager. Simultaneously, it identifies that neighboring Silver partners are performing well and suggests territory adjustments. When the ISO responds that they're facing competitive pressure, the agent immediately provides updated battle cards and schedules a joint sales call with their biggest prospect.

---

### Use Case 4: Enterprise Deal Management & Pricing Optimization

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Enterprise payment deals involve complex pricing models (interchange-plus, custom rates), lengthy sales cycles, multiple stakeholders, and intricate integration requirements. Sales teams use separate tools for pricing calculations, technical specifications, legal review, and deal tracking, creating disconnected processes and lost deals.

#### The Solution
monday.com unifies enterprise deal management with automated pricing optimization, stakeholder tracking, and integration planning. AI Agents monitor deal progression, identify bottlenecks, and suggest pricing adjustments based on competitive intelligence and win/loss analysis.

#### The Outcome
30% faster deal closure, 25% improvement in deal margins through better pricing, 90% reduction in pricing errors, and 40% increase in enterprise deal win rates.

#### Discovery Questions
- What's your average enterprise deal cycle time?
- How do you calculate custom pricing for large merchants?
- Who are the typical stakeholders involved in enterprise decisions?
- What percentage of enterprise deals get stuck in legal or technical review?
- How do you track processing volume commitments and contract compliance?

#### Industry Context
Enterprise payment deals can range from $100K to $10M+ in annual processing fees. These deals require custom pricing models, integration planning, risk assessment, and often involve multiple buyer stakeholders (CFO, CTO, procurement, operations). Competitive pressure is intense with multiple rounds of negotiations.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an enterprise deals board with columns: Deal Name (text), Merchant/Company (text), Deal Value (numbers), Merchant Category (dropdown: E-commerce, Retail, Healthcare, Financial Services, Government), Sales Stage (status: Discovery, Qualification, Proposal, Negotiation, Legal Review, Technical Review, Closed-Won, Closed-Lost), Primary Contact (people picker), Decision Makers (people picker multiple), Pricing Model (dropdown: Interchange Plus, Flat Rate, Custom Hybrid), Processing Volume Commitment (numbers), Integration Complexity (dropdown: Simple, Standard, Complex), Competitive Situation (text), Close Date (date), Contract Terms (text), Risk Level (dropdown: Low, Medium, High), Next Action (text), Legal Status (status: Pending, In Review, Approved). Add automations to alert when deals haven't progressed in 14 days and create timeline view for deal pipeline forecasting."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Enterprise Deal Agent

**Agent Purpose:**  
Optimize enterprise deal progression and pricing while coordinating complex stakeholder requirements.

**Triggers:**
- Deal stage progression or stagnation for 7+ days
- Pricing proposal requested
- Competitive intelligence updates affecting active deals
- Integration requirements change
- Legal or compliance review needed

**Actions:**
- Calculate optimal pricing based on volume, risk, and competitive factors
- Track stakeholder engagement and identify missing decision makers
- Generate integration timelines and resource requirements
- Monitor competitive threats and adjust positioning
- Escalate stalled deals with specific recommendations
- Coordinate legal and technical review processes

**Data Required:**
- Historical pricing and margin data
- Competitive pricing intelligence
- Integration complexity matrices
- Win/loss analysis by deal characteristics
- Stakeholder mapping and influence patterns

**Autonomy Level:** Human-in-the-Loop  
Agent provides pricing recommendations and process optimization autonomously but requires approval for pricing changes above certain thresholds or strategic positioning shifts.

**Example Interaction:**
> A $2M annual processing deal with a healthcare company has been in "Negotiation" stage for 3 weeks. The agent analyzes similar healthcare deals, identifies that HIPAA compliance features weren't prominently featured in the proposal, suggests pricing adjustments based on their processing volume commitment, identifies that the CFO hasn't been directly engaged, and recommends a compliance-focused executive briefing. It also alerts the sales rep that a competitor recently won a similar healthcare deal with specific terms that could influence the negotiation.

---

### Use Case 5: API-First & Developer-Led Sales Automation

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Developer-led sales require technical content creation, API documentation management, and tracking developer engagement across multiple touchpoints (GitHub, Stack Overflow, developer portals). Sales teams struggle to identify high-intent developers and provide appropriate technical nurturing without engineering involvement.

#### The Solution
monday.com AI Agents monitor developer activity, automatically generate technical content, and score developer leads based on API usage patterns. Vibe creates developer journey tracking that connects technical engagement to commercial opportunities.

#### The Outcome
3x increase in developer-to-customer conversion, 60% reduction in engineering time spent on sales support, 50% faster time from API signup to first transaction, and 200% growth in embedded payments adoption.

#### Discovery Questions
- How many developers sign up for your APIs monthly?
- What's your conversion rate from API signup to paying customer?
- How do you identify which developers are most likely to convert?
- What percentage of your engineering time is spent supporting sales activities?
- How do you track developer engagement across different touchpoints?

#### Industry Context
Modern payment companies increasingly rely on developer-first sales motions, especially for embedded payments and platform integrations. Developers often evaluate APIs before involving commercial stakeholders, making technical marketing and sales alignment critical.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a developer leads board with columns: Developer/Company (text), API Usage Level (dropdown: Sandbox, Light Production, Heavy Production), Integration Type (dropdown: E-commerce, Mobile App, SaaS Platform, Marketplace), Primary API Products (text), Signup Date (date), Last API Call (date), Lead Score (numbers), Commercial Intent (status: Low, Medium, High, Enterprise), Sales-Qualified (status: No, Yes, Contacted, Meeting Set), Assigned Rep (people picker), Technical Stack (text), Company Size (dropdown: Startup, SMB, Mid-Market, Enterprise), Use Case (text), Next Technical Touchpoint (date), Conversion Stage (status: Evaluation, Integration, Testing, Production, Customer). Add automation to alert sales reps when API usage increases 300% week-over-week and create dashboard tracking developer funnel metrics."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Developer Success Agent

**Agent Purpose:**  
Identify high-intent developers and automate technical sales support to accelerate API-to-customer conversion.

**Triggers:**
- Developer API usage patterns change significantly
- Integration reaches production environment
- Developer submits support tickets indicating scaling needs
- Time-based nurturing sequences (30, 60, 90 days post-signup)
- Competitor integration identified in developer stack

**Actions:**
- Score developer leads based on usage patterns and company profiles
- Generate personalized technical content and integration guides
- Alert sales reps to high-intent developer activities
- Create automated technical email sequences
- Identify upsell opportunities based on API usage growth
- Connect developers with appropriate technical resources

**Data Required:**
- API usage analytics and patterns
- Developer profile and company information
- Technical documentation engagement metrics
- Integration completion rates by use case
- Competitive API adoption signals

**Autonomy Level:** Fully Autonomous  
Agent handles developer scoring and nurturing autonomously, only escalating to sales reps when commercial qualification thresholds are met.

**Example Interaction:**
> A fintech startup developer increases API call volume from 100 to 5,000 daily over two weeks while integrating payment acceptance. The agent immediately scores them as "High Commercial Intent," researches their company (Series A, $50M GMV projected), generates a personalized integration optimization guide, alerts the assigned sales rep, and schedules automated technical check-ins. When their usage hits production levels, the agent triggers a commercial qualification sequence and suggests pricing discussions based on their transaction volume trajectory.

---

### Use Case 6: Cross-Border & Multi-Currency Sales Optimization

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Cross-border payment sales require understanding complex currency regulations, local payment preferences, competitive landscapes in multiple regions, and integration with regional banking systems. Sales teams struggle to scale internationally without region-specific expertise and localized sales processes.

#### The Solution
monday.com centralizes multi-region sales processes with localized workflows, automated compliance tracking, and region-specific competitive intelligence. AI Agents provide real-time currency impact analysis and regional opportunity prioritization.

#### The Outcome
2x faster international market entry, 40% improvement in cross-border deal conversion, 50% reduction in compliance-related delays, and ability to manage 3x more regions with same headcount.

#### Discovery Questions
- Which international markets are you currently targeting?
- How do you handle currency fluctuation impact on pricing?
- What compliance requirements vary by region in your sales process?
- How do you prioritize international opportunities?
- What percentage of your pipeline is cross-border business?

#### Industry Context
Cross-border payments involve complex regulations, currency considerations, and local market dynamics. Success requires understanding regional payment preferences (SEPA, local banking systems), compliance requirements (PCI, local data protection), and competitive positioning in each market.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a cross-border sales board with columns: Opportunity Name (text), Target Region (dropdown: Europe, Asia-Pacific, Latin America, Middle East, Africa), Primary Currency (dropdown: EUR, GBP, JPY, AUD, CAD, Others), Deal Value USD (numbers), Local Deal Value (numbers), Merchant Category (text), Regional Compliance Status (status: Compliant, Needs Review, Pending Approval), Local Payment Methods (text), Currency Risk Level (dropdown: Low, Medium, High), Regional Competition (text), Local Partner Required (status: Yes, No, Identified), Sales Stage (status: Discovery, Qualification, Local Approval, Contract, Closed), Regional Sales Rep (people picker), Compliance Officer (people picker), Go-Live Date (date), Integration Complexity (dropdown: Standard, Custom, Regional Requirements). Add automations to notify compliance team when new regions are added and create currency conversion dashboard for deal valuations."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Global Expansion Agent

**Agent Purpose:**  
Optimize cross-border sales by providing regional intelligence and automated compliance guidance.

**Triggers:**
- New international opportunity identified
- Currency exchange rates change significantly (>5%)
- Regional compliance requirements update
- Local competitive intelligence changes
- Cross-border integration milestone reached

**Actions:**
- Research regional payment preferences and market dynamics
- Calculate currency-adjusted pricing and risk assessments
- Identify required local partnerships and compliance needs
- Generate region-specific competitive positioning
- Track regulatory changes affecting cross-border sales
- Optimize opportunity prioritization based on regional factors

**Data Required:**
- Regional compliance databases and requirements
- Currency exchange rate feeds and volatility data
- Local competitive intelligence by region
- Regional payment method adoption rates
- Cross-border transaction success rates

**Autonomy Level:** Escalation-Based  
Agent provides regional intelligence and recommendations autonomously but escalates currency risk above thresholds and compliance questions to regional experts.

**Example Interaction:**
> A European e-commerce company requests payment processing for expansion into Brazil. The agent immediately identifies Brazil requires local acquiring partnerships, researches Pix payment method adoption (80% of digital payments), calculates USD pricing with BRL hedging options, flags LGPD compliance requirements, identifies three potential local partners, and estimates 4-6 month integration timeline. It also surfaces that a competitor recently won a similar deal with specific local partnership terms that could inform the proposal strategy.

---

### Use Case 7: Value-Added Services Upsell Intelligence

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Sales teams miss upselling opportunities for fraud protection, analytics, reporting, and other value-added services because they lack visibility into merchant usage patterns and pain points. Upselling requires technical product knowledge and timing that individual reps can't effectively manage across hundreds of accounts.

#### The Solution
monday.com AI Agents monitor merchant transaction patterns to identify upsell opportunities, automatically generate service recommendations based on usage analytics, and track upsell campaign effectiveness across the customer base.

#### The Outcome
4x increase in value-added services attach rate, $500K additional ARR from existing customers, 60% improvement in upsell conversation success rate, and 2x faster identification of expansion opportunities.

#### Discovery Questions
- What value-added services do you currently offer beyond basic processing?
- How do you identify which merchants would benefit from additional services?
- What's your current attach rate for fraud protection or analytics services?
- How do you track merchant usage patterns to identify expansion opportunities?
- What percentage of revenue growth comes from existing customer expansion?

#### Industry Context
Payment processors typically offer fraud protection, advanced analytics, reporting dashboards, chargeback management, and industry-specific tools. These services have higher margins than basic processing and improve customer retention, making them critical for profitability and competitive differentiation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a customer upsell tracking board with columns: Merchant Name (text), Current Services (text), Monthly Processing Volume (numbers), Chargeback Rate (numbers), Fraud Indicators (dropdown: Low, Medium, High), Upsell Opportunity (dropdown: Fraud Protection, Advanced Analytics, Reporting Plus, Chargeback Management, Industry Tools), Opportunity Value (numbers), Recommendation Confidence (dropdown: High, Medium, Low), Last Upsell Attempt (date), Customer Success Manager (people picker), Sales Rep (people picker), Implementation Complexity (dropdown: Simple, Standard, Complex), Merchant Satisfaction (dropdown: High, Medium, Low), Contract Renewal Date (date), Upsell Status (status: Identified, Pitched, Negotiating, Closed-Won, Closed-Lost), ROI Demonstration (text). Add automation to flag merchants with chargeback rates >1% for fraud protection upsell and create dashboard showing upsell pipeline value by service type."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Upsell Intelligence Agent

**Agent Purpose:**  
Automatically identify and prioritize value-added service opportunities based on merchant behavior patterns.

**Triggers:**
- Monthly merchant analytics review
- Chargeback or fraud rates exceed thresholds
- Processing volume growth indicates scaling needs
- Contract renewal approaching (90 days prior)
- Competitor value-added service adoption detected

**Actions:**
- Analyze transaction patterns for service fit indicators
- Generate ROI calculations for recommended services
- Create personalized upsell presentations with merchant data
- Schedule optimal timing for upsell conversations
- Track merchant satisfaction correlation with service adoption
- Identify at-risk accounts that need additional services for retention

**Data Required:**
- Merchant transaction analytics and patterns
- Chargeback and fraud rate data
- Service adoption rates and success metrics
- Competitive intelligence on value-added services
- Customer satisfaction and retention data

**Autonomy Level:** Human-in-the-Loop  
Agent identifies opportunities and generates recommendations autonomously but requires sales rep approval before initiating customer outreach.

**Example Interaction:**
> A restaurant client's processing volume grew 200% over six months but their chargeback rate increased to 1.8%. The agent identifies this pattern, calculates that fraud protection would save them $15K annually, generates a presentation showing similar restaurant success stories, estimates implementation would take 2 weeks, and recommends timing the conversation after their busiest season ends. It also flags that their POS integration could benefit from advanced analytics and schedules a joint presentation covering both opportunities with projected ROI of $25K annually.

---

## Industry Terminology

| Term | Definition |
|---|---|
| **Merchant Acquisition** | Process of signing new businesses to accept payment processing services |
| **ISO/MSP** | Independent Sales Organization/Member Service Provider - third-party sales channels |
| **Interchange Plus** | Pricing model where merchant pays interchange fees plus a markup |
| **Processing Volume** | Total dollar amount of transactions processed by a merchant |
| **Acquiring Bank** | Financial institution that processes payment card transactions for merchants |
| **Payment Facilitator (PayFac)** | Service that simplifies merchant onboarding and processing |
| **Gateway Integration** | Technical connection between merchant systems and payment networks |
| **PCI Compliance** | Payment Card Industry security standards for handling card data |
| **Chargeback** | Transaction reversal initiated by cardholder through their bank |
| **MDR (Merchant Discount Rate)** | Fee charged to merchant for processing card transactions |
| **BaaS (Banking-as-a-Service)** | Platform providing banking services through APIs |
| **Cross-Border Processing** | Handling payments between different countries/currencies |
| **Embedded Payments** | Payment capabilities built directly into software platforms |
| **Vertical Solutions** | Industry-specific payment products (healthcare, restaurants, etc.) |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|---|---|---|
| **VP Sales** | Overall revenue targets and sales strategy | High - budget authority |
| **Sales Director** | Regional/channel sales management | High - process decisions |
| **Enterprise Sales Rep** | Large merchant acquisition and management | Medium - day-to-day execution |
| **Channel Manager** | ISO/partner relationship management | Medium - channel strategy |
| **Sales Engineer** | Technical sales support and integration guidance | Medium - solution design |
| **Inside Sales Rep** | Lead qualification and small merchant acquisition | Low - tactical execution |
| **Sales Operations** | Process, tools, and performance analytics | High - operational decisions |
| **Revenue Operations** | Cross-functional revenue process optimization | High - strategic decisions |

## Adjacent Departments

| Department | Connection | Opportunity |
|---|---|---|
| **Product** | Feature requests, competitive intelligence | Joint customer meetings, roadmap input |
| **Marketing** | Lead generation, content creation | Campaign optimization, sales enablement |
| **Customer Success** | Account expansion, retention | Upsell identification, renewal coordination |
| **Risk/Underwriting** | Merchant approval, pricing guidance | Deal structure optimization, risk assessment |
| **Implementation** | Technical onboarding, integration support | Realistic timeline setting, customer expectations |
| **Legal/Compliance** | Contract review, regulatory requirements | Enterprise deal support, international expansion |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|---|---|---|
| **Salesforce + Custom Tools** | "All-in-one platform vs. fragmented point solutions" | Consolidation story, AI capabilities |
| **HubSpot + Spreadsheets** | "Enterprise scalability vs. SMB limitations" | Advanced workflow needs, reporting gaps |
| **Microsoft Dynamics + Partners** | "Integrated AI platform vs. complex integrations" | Implementation complexity, limited AI |
| **Pipedrive + Manual Processes** | "Intelligent automation vs. manual work" | Time savings, competitive intelligence |
| **Custom-Built Solutions** | "Maintained platform vs. technical debt" | Development resources, feature velocity |

## Objection Handling

| Objection | Response |
|---|---|
| **"We already have Salesforce"** | "Salesforce manages data - we deploy AI that does the work. Show me how Salesforce automatically researches prospects and generates RFP responses." |
| **"Our sales process is too complex"** | "Complex processes benefit most from AI. Let's map your RFP workflow and show how we eliminate 75% of the manual work while maintaining quality." |
| **"We need industry-specific features"** | "We build custom workflows in minutes with Vibe. What payment-specific processes can't you configure in other platforms?" |
| **"ROI is unclear for sales tools"** | "Payment sales is time-sensitive. Show me your current RFP response time vs. your win rate. We typically see 3x ROI within 6 months." |
| **"Integration complexity concerns"** | "We integrate with payment industry tools out-of-box. Most implementations are live within 30 days vs. 6+ months for enterprise solutions." |

## Proof Points
*(To be populated with customer references)*

- Payment processor increased merchant acquisition by 300% while reducing sales headcount
- Global payment company reduced RFP response time from 2 weeks to 3 days
- ISO network improved partner satisfaction scores by 2.5x through automated support
- Enterprise payment solution provider achieved 40% higher win rates on competitive deals
- Cross-border payment company expanded to 5 new regions with same sales team size

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*