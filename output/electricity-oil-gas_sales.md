# Electricity, Oil & Gas × Sales Playbook

## Overview

Sales departments in the Electricity, Oil & Gas sector operate across a uniquely complex landscape that spans commodity trading, long-term supply contracts, retail energy sales, B2B industrial accounts, and increasingly, clean energy solutions selling. Unlike typical SaaS or product sales, energy sales teams negotiate contracts worth $10M–$500M+ with cycle times ranging from 6 months to 3+ years, involving intricate pricing mechanisms tied to commodity indices (WTI, Brent, Henry Hub, TTF), regulatory approvals, credit risk assessments, and multi-party joint venture structures.

The organizational structure varies significantly by segment. Upstream sales teams focus on commodity marketing — selling crude oil, natural gas, and NGLs to refiners, utilities, and trading houses. Midstream sales teams sell pipeline capacity, storage, and processing services under long-term transportation service agreements (TSAs). Downstream teams sell refined products (gasoline, diesel, jet fuel, petrochemicals) to distributors, fleet operators, and industrial consumers. Utility sales teams sell electricity and gas to residential, commercial, and industrial (C&I) customers, often through regulated rate structures. And the fastest-growing segment — new energy sales — sells solar PPAs, EV charging solutions, green hydrogen, and carbon credits to corporate buyers pursuing their own sustainability goals.

The industry is at an inflection point where traditional sales competencies (relationship management, contract negotiation, commodity pricing) must merge with new capabilities (sustainability consulting, energy-as-a-service models, carbon accounting, and bundled solution selling). Sales teams must simultaneously manage legacy hydrocarbon contract portfolios while building pipeline for clean energy products — often selling to the same customer's procurement team and sustainability team with fundamentally different value propositions. This dual mandate, combined with regulatory complexity, long sales cycles, and enormous deal values, makes structured sales management not just a productivity tool but a strategic imperative.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Sales teams must manage larger, more complex portfolios (traditional + clean energy) without proportional headcount growth; deal complexity is increasing faster than team size |
| 2 | Consolidate Tech Stack with AI | High | Sales data lives across ETRM systems, CRM (often legacy Salesforce or SAP), commodity trading platforms, and spreadsheet-based pricing models — no single view of the customer |
| 3 | Replace or Radically Augment Headcount | Medium-High | Complex proposal generation, contract analysis, and pricing optimization consume enormous sales engineering hours that AI can dramatically reduce |

## Prioritized Use Cases

---

### Use Case 1: Energy Sales Pipeline & Deal Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy sales cycles are long (6–36 months), high-value ($10M–$500M+), and involve multiple stakeholders across the customer organization (procurement, operations, legal, sustainability, C-suite). Sales reps manage 10–40 active opportunities simultaneously, each with unique pricing structures, contract terms, regulatory requirements, and competitive dynamics. Pipeline visibility is poor — leadership relies on monthly spreadsheet roll-ups that are stale by the time they're compiled. Deals stall without visibility: a $50M gas supply contract can sit in "legal review" for 3 months with no escalation because it fell off the pipeline report. Forecasting is notoriously inaccurate because traditional CRM tools don't capture the nuances of commodity-linked deal structures.

#### The Solution
monday.com CRM configured for energy sales: each deal tracks value (numbers columns for contract value, annual revenue, and volume in MMBtu, MWh, or barrels), stage (status: Prospecting, Qualification, Proposal, Negotiation, Regulatory Approval, Legal Review, Execution, Closed Won, Closed Lost), product type (dropdown: Crude Supply, Natural Gas, Power PPA, Pipeline Capacity, Refined Products, Green Hydrogen, Carbon Credits, Bundled Solution), customer segment (dropdown: Utility, Industrial C&I, Refiner, Petrochemical, Government, Corporate Offtaker), contract duration (numbers, years), pricing mechanism (dropdown: Fixed, Index-Linked, Collar, Hybrid), and key stakeholders (people columns for internal team + text for customer contacts). Automations trigger stage-appropriate actions: at "Proposal" stage, auto-assign pricing analyst; at "Legal Review" for 30+ days, escalate to VP Sales; at "Regulatory Approval," create linked regulatory tracking items.

#### The Outcome
95%+ pipeline visibility in real-time, replacing monthly spreadsheet compilations. 20% improvement in forecast accuracy through structured deal stage tracking with energy-specific milestones. 15% reduction in average sales cycle length by catching and escalating stalled deals automatically.

#### Discovery Questions
1. "How many active opportunities does a typical energy sales rep manage simultaneously, and what's the range of deal values and contract durations?"
2. "When leadership needs a pipeline readout, how long does it take to compile — and how confident are you in its accuracy when it's presented?"
3. "Have you lost a deal or had a significant delay because an opportunity stalled in a particular stage without anyone noticing?"
4. "How do you currently track the different pricing structures across your deals — fixed price, index-linked, collar structures — and how does that affect forecasting?"
5. "Are your traditional hydrocarbon sales and clean energy sales tracked in the same system, or are they managed separately?"

#### Industry Context
ETRM (Energy Trading and Risk Management) systems like Allegro, Openlink/ION, and RightAngle manage the financial and logistics side of energy trading but are not sales pipeline tools. Pricing mechanisms in energy are complex: index-linked contracts tie price to benchmarks like WTI (West Texas Intermediate crude), Henry Hub (US natural gas), TTF (Dutch natural gas), or regional power indices. Collar structures set price floors and ceilings. PPAs (Power Purchase Agreements) are long-term electricity offtake contracts critical for renewable energy project financing. C&I stands for Commercial & Industrial — the large-account segment for utilities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Energy Sales Pipeline and Deal Management CRM for an oil, gas, and power company. Create a board called 'Energy Sales Pipeline' with these columns: Deal Name (item name), Customer (text), Customer Segment (dropdown: Utility, Industrial C&I, Refiner, Petrochemical, Government Agency, Corporate Offtaker, Trading House, Distributor), Product Type (dropdown: Crude Oil Supply, Natural Gas Supply, Pipeline Capacity/TSA, Power PPA, Refined Products, LNG, Green Hydrogen, Carbon Credits, EV Charging, Bundled Energy Solution), Deal Stage (status: Prospecting, Qualification, Needs Analysis, Proposal/Pricing, Negotiation, Regulatory Review, Legal/Contract, Credit Approval, Execution, Closed Won, Closed Lost — color green for last two won stages, red for lost, yellow for middle), Contract Value ($M) (numbers), Annual Revenue ($M) (numbers), Volume (numbers — MMBtu, MWh, or barrels depending on product), Volume Unit (dropdown: MMBtu/day, MWh/year, Barrels/day, MW, Tons CO2e), Pricing Mechanism (dropdown: Fixed Price, WTI-Linked, Henry Hub-Linked, TTF-Linked, Power Index, Collar, Cost-Plus, Negotiated), Contract Duration (numbers, years), Start Date (date), Sales Rep (people column), Sales Engineer (people column), Pricing Analyst (people column), Customer Contacts (long text), Competitor (dropdown: Shell Trading, Vitol, Trafigura, BP, NextEra, Enel, Incumbent Utility, None Identified), Win Probability % (numbers), Weighted Value ($M) (formula: Contract Value × Win Probability), Stage Entry Date (date), Days in Stage (formula), Next Action (text), Region (dropdown: North America, Europe, Middle East, Asia-Pacific, Latin America). Create groups: 'Active Pipeline', 'Proposal Stage', 'Negotiation/Legal', 'Closed This Quarter', 'Lost/Deferred'. Add automations: when Deal Stage changes to Proposal/Pricing, assign Pricing Analyst from team; when Days in Stage exceeds 45 and stage is Negotiation or Legal, notify VP Sales with escalation alert; when Deal Stage changes to Closed Won, create linked items in 'Contract Management' board and send celebration notification to sales channel; when new deal is created, auto-populate region based on Sales Rep assignment. Create Dashboard: pipeline funnel by stage, weighted pipeline value by product type, deal velocity (average days per stage), top 10 deals by value table, won/lost ratio by product type, and monthly bookings trend chart."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Deal Pulse
**Agent Purpose:** Continuously monitors the energy sales pipeline, identifies at-risk deals, provides intelligent forecasting, and ensures no opportunity falls through the cracks in the complex, long-cycle energy sales process.

**Triggers:**
- Daily pipeline health scan at 7 AM
- When a deal has been in the same stage for more than the average duration for that stage
- When Win Probability drops below 30% on a deal over $25M
- Weekly forecast compilation every Friday
- When a competitive threat is identified (competitor column populated or updated)

**Actions:**
- Generate daily "deals to watch" briefing for each sales rep highlighting stalled opportunities, upcoming milestones, and competitive threats
- Produce weekly rolling forecast with confidence intervals based on historical stage conversion rates and current pipeline mix
- Draft deal strategy memos for high-value opportunities by analyzing customer segment patterns, competitor positioning, and historical win/loss data
- Alert leadership when pipeline coverage ratio falls below 3x target for any product type or region
- Auto-generate quarterly business review (QBR) slides pulling pipeline data, win rates, deal velocity, and product mix trends

**Data Required:**
- Energy Sales Pipeline board
- Historical closed deals for conversion rate analysis
- Commodity price feeds for index-linked deal valuation
- Customer account data for relationship mapping
- Competitor intelligence from public filings and industry news

**Autonomy Level:** Escalation-Based
Pipeline monitoring, alerting, and reporting are fully autonomous. Deal strategy recommendations are generated for rep review. Forecast adjustments require sales leadership approval before communicating to finance.

**Example Interaction:**
> On Tuesday morning, Deal Pulse flags that the $120M Midwestern Utility PPA opportunity has been in "Legal/Contract" stage for 52 days — 22 days beyond the average for PPA deals. The agent digs into the activity log and notes that no updates have been logged in 18 days. It generates an alert to VP Sales Maria Gonzalez: "Midwest Utility PPA ($120M, 15-year term) appears stalled in legal. Last activity: 18 days ago. Historical data shows that PPA deals exceeding 45 days in legal have a 35% higher loss rate. Recommendation: escalate to customer's VP Procurement and offer to conduct a joint legal session to resolve outstanding terms." Simultaneously, the agent updates the weekly forecast, adjusting this deal's probability from 65% to 45% based on the stall pattern, and recalculates the weighted pipeline — surfacing a $14M gap to quarterly target that the VP needs to address.

---

### Use Case 2: Contract Lifecycle Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies manage thousands of active contracts simultaneously: supply agreements, transportation service agreements (TSAs), tolling agreements, PPAs, storage contracts, and increasingly, carbon credit offtake agreements. Each has unique renewal dates, price escalation clauses, volume commitments (take-or-pay), and regulatory compliance requirements. Contract managers spend weeks preparing for renewal negotiations because they must manually gather performance data, pricing history, and compliance records from multiple systems. Missed renewal windows result in unfavorable auto-renewals or contract lapses that disrupt supply chains. Volume commitment breaches trigger take-or-pay penalties that can cost millions.

#### The Solution
monday.com as a Contract Lifecycle Management platform. Each contract is an item with: contract type, counterparty, effective date, expiration date, auto-renewal terms, annual value, volume commitment, pricing mechanism, key clauses (long text), renewal notice period, performance status (status), and assigned contract manager. Automations trigger renewal preparation workflows 120 days before expiration, alert on volume commitment thresholds, and escalate contracts approaching auto-renewal without active review. Dashboards show the entire contract portfolio by type, value, expiration timeline, and risk status.

#### The Outcome
Zero missed renewal windows — eliminating auto-renewal surprises and contract lapses. $5–15M annual savings from proactive renewal negotiations instead of reactive scrambles. 70% reduction in contract review preparation time through centralized data aggregation.

#### Discovery Questions
1. "How many active contracts does your sales organization manage, and what's the range of contract types and values?"
2. "Has your organization ever been caught by an auto-renewal clause or missed a renewal notification window?"
3. "When it's time to renegotiate a major contract, how long does it take to pull together the performance history, pricing data, and compliance records?"
4. "How do you track volume commitments and take-or-pay obligations across your contract portfolio?"
5. "Do you have a single view of all contracts expiring in the next 12 months, or does that require manual compilation?"

#### Industry Context
Take-or-pay clauses are standard in energy contracts — the buyer commits to purchasing a minimum volume (e.g., 50,000 MMBtu/day of natural gas) and must pay for that volume even if they don't take delivery. TSAs (Transportation Service Agreements) govern pipeline capacity commitments. Tolling agreements allow a third party to process feedstock through a facility for a fee. Auto-renewal clauses in energy contracts often have 90–180 day notice periods — miss the window and you're locked in for another term. ISDA (International Swaps and Derivatives Association) master agreements govern derivative and trading contracts.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Contract Lifecycle Management system for an energy sales organization. Create a board called 'Contract Portfolio' with columns: Contract Name (item name), Counterparty (text), Contract Type (dropdown: Supply Agreement, Transportation Service Agreement, Power Purchase Agreement, Tolling Agreement, Storage Agreement, Carbon Credit Offtake, ISDA Master, Distribution Agreement, EV Charging Agreement, Joint Venture), Effective Date (date), Expiration Date (date), Contract Duration (formula: years between dates), Auto-Renewal (checkbox), Renewal Notice Period (numbers, days), Renewal Notice Deadline (formula: Expiration minus Notice Period), Annual Value ($M) (numbers), Total Contract Value ($M) (numbers), Volume Commitment (numbers), Volume Unit (dropdown: MMBtu/day, MWh/year, Barrels/day, MW, Tons/year), Actual Volume YTD (numbers), Volume Compliance % (formula: Actual/Commitment × 100), Pricing Mechanism (dropdown: Fixed, Index-Linked, Collar, Cost-Plus, Tiered), Price Escalation (text — describe annual escalation terms), Key Clauses (long text), Performance Status (status: Performing, Under Review, At Risk, In Breach, Renewal Pending, Expired), Contract Manager (people column), Legal Contact (people column), Risk Rating (dropdown: Low, Medium, High, Critical). Create groups: 'Active — Performing', 'Renewal Pipeline (next 12 months)', 'Under Negotiation', 'Expired/Archived'. Add automations: when today is 120 days before Expiration Date, move to 'Renewal Pipeline' group and notify Contract Manager; when today is 30 days before Renewal Notice Deadline and Auto-Renewal is checked and Status is not 'Under Negotiation', send URGENT alert to Contract Manager and VP Sales; when Volume Compliance drops below 85%, change Risk Rating to High and notify sales rep; when contract moves to 'Expired/Archived', create a post-mortem subitem. Create Dashboard: contract expiration timeline (next 24 months), total portfolio value by contract type, volume compliance heat map, upcoming renewals table sorted by value, and risk distribution chart."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Contract Sentinel
**Agent Purpose:** Proactively manages the energy contract portfolio, ensuring no renewals are missed, volume commitments are tracked, and renewal negotiations are supported with data-driven intelligence.

**Triggers:**
- Daily scan for contracts approaching renewal notice deadlines
- When Volume Compliance drops below 90% for any contract
- 120 days before contract expiration (initiate renewal preparation)
- When commodity prices move significantly (>10% in 30 days), triggering pricing review for index-linked contracts
- Quarterly portfolio health review

**Actions:**
- Generate renewal preparation packages: contract summary, performance history, pricing analysis vs. market rates, customer relationship health, and recommended negotiation strategy
- Alert on take-or-pay risk: project month-end and year-end volume compliance based on current run rates and flag contracts likely to breach minimums
- Draft pricing comparison reports for renewal negotiations, benchmarking contract rates against current market indices
- Produce quarterly portfolio reports showing total contracted value, revenue at risk from upcoming expirations, and volume commitment health
- Recommend contract restructuring when market conditions have shifted significantly from original terms

**Data Required:**
- Contract Portfolio board
- Actual delivery/volume data from ETRM or SCADA systems
- Commodity price feeds (WTI, Henry Hub, power indices)
- Customer relationship data from CRM
- Market benchmarking data for comparable contracts

**Autonomy Level:** Human-in-the-Loop
Monitoring, alerting, and report generation are autonomous. Renewal strategies and pricing recommendations are generated for contract manager review. All contract decisions and counterparty communications require human approval.

**Example Interaction:**
> Contract Sentinel identifies that a 5-year natural gas supply agreement with PetroChem Industries ($45M/year, 80,000 MMBtu/day take-or-pay) expires in 140 days, and the 120-day renewal window just opened. The agent compiles a renewal package: over the contract term, the customer has averaged 92% volume compliance with two months dipping below 85%. Current contract pricing is Henry Hub + $0.35/MMBtu, but comparable recent contracts in the market are trading at Henry Hub + $0.42–$0.55/MMBtu. The agent recommends a renewal strategy: propose Henry Hub + $0.48 with a volume flexibility clause (75% minimum instead of 80%) as a concession, projecting $4.2M additional annual revenue. It identifies that PetroChem is also a prospect for the new green hydrogen pilot program, suggesting a bundled renewal approach. The package is routed to the account manager and VP Sales for review before the first renewal conversation.

---

### Use Case 3: Proposal & Pricing Engine

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy sales proposals are extraordinarily complex documents. A single gas supply proposal might include commodity pricing scenarios across 5 index options, transportation cost modeling, credit terms based on counterparty risk rating, regulatory compliance attestations, and volume-tier pricing structures. Pricing analysts spend 2–5 days building each proposal, pulling data from commodity price feeds, pipeline tariff databases, credit reports, and regulatory filings. When a customer asks for a pricing revision mid-negotiation, the cycle restarts. Errors in pricing proposals can cost millions — a misplaced decimal in a 10-year PPA can mean a $20M difference. Sales reps without dedicated pricing support lose competitiveness because they can't turn around proposals fast enough.

#### The Solution
monday.com as a Proposal & Pricing workflow engine. Proposal requests flow through a structured process: Request → Data Gathering → Pricing Modeling → Internal Review → Customer Presentation → Revision (if needed) → Final Approval. Each proposal item tracks product type, pricing scenarios, volume tiers, contract term options, credit requirements, and approval chain. Template-based Docs generate proposal documents with consistent formatting. Automations assign pricing analysts based on product type, escalate overdue proposals, and route approvals based on deal value thresholds.

#### The Outcome
60% reduction in proposal turnaround time — from 5 days to 2 days average. 90% reduction in pricing errors through structured templates and automated validation. Sales reps can respond to customer requests 3x faster, improving competitive positioning.

#### Discovery Questions
1. "How long does it take your team to produce a fully priced proposal for a major energy contract?"
2. "What's the revision cycle like — how many times does a typical proposal go back and forth before final approval?"
3. "Have you ever had a pricing error in a proposal that made it to the customer? What was the impact?"
4. "How many pricing analysts support your sales team, and are they a bottleneck in the sales process?"
5. "When a customer asks for a quick turnaround on a pricing revision — say, adding a collar structure or changing the volume tier — how fast can you deliver?"

#### Industry Context
Commodity pricing in energy involves complex structures: basis differentials (the price difference between a regional delivery point and the benchmark hub), swing provisions (the right to take more or less than the contracted volume within limits), and seasonal pricing adjustments. Credit risk assessment is critical — energy counterparties can default on contracts worth hundreds of millions. NAESB (North American Energy Standards Board) provides standard contract forms for gas transactions. Dodd-Frank regulations require certain derivative positions to be reported and may require margin.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Proposal and Pricing Engine for an energy sales team. Create a board called 'Proposal Pipeline' with columns: Proposal Name (item name), Customer (text), Linked Deal (connect boards to Energy Sales Pipeline), Product Type (dropdown: Natural Gas Supply, Crude Oil Supply, Power PPA, Pipeline Capacity, Refined Products, LNG, Green Hydrogen, Carbon Credits, Bundled Solution), Proposal Stage (status: Request Received, Data Gathering, Pricing Modeling, Internal Review, Pricing Committee, Customer Presentation, Revision Requested, Final Approval, Submitted, Won, Lost), Requested By (people — sales rep), Assigned Pricing Analyst (people), Due Date (date), Urgency (dropdown: Standard 5-day, Expedited 2-day, Emergency 24-hour), Volume Proposed (numbers), Volume Unit (dropdown: MMBtu/day, MWh/year, Barrels/day, MW), Contract Term (numbers, years), Pricing Scenarios (numbers — how many scenarios to model), Pricing Structure Requested (tags: Fixed, Index-Linked, Collar, Basis Differential, Seasonal, Tiered Volume, Take-or-Pay), Credit Tier (dropdown: Investment Grade, Sub-Investment Grade, Secured, Government, Not Assessed), Estimated Contract Value ($M) (numbers), Proposal Document (file column), Version Number (numbers), Revision Notes (long text). Create groups: 'New Requests', 'In Pricing', 'Under Review', 'With Customer', 'Completed'. Create a second board 'Pricing Committee Review' with columns: Proposal Link (connect boards), Deal Value ($M), Margin Analysis (long text), Risk Assessment (dropdown: Low, Medium, High, Requires Executive Approval), Committee Decision (status: Pending, Approved, Approved with Conditions, Rejected, Deferred), Conditions (long text). Add automations: when Proposal Stage changes to 'Request Received', auto-assign Pricing Analyst based on Product Type; when Due Date is tomorrow and stage is still Data Gathering or Pricing Modeling, send urgent alert; when Estimated Contract Value exceeds $50M, auto-create Pricing Committee Review item; when Stage changes to 'Revision Requested', increment Version Number and notify Pricing Analyst with Revision Notes. Create Dashboard: proposal pipeline by stage, average turnaround time by product type, pricing analyst workload, proposals by urgency, and win rate by pricing structure."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pricing Copilot
**Agent Purpose:** Accelerates the proposal and pricing process by automating data gathering, generating pricing scenarios, and performing quality checks — giving pricing analysts superpowers.

**Triggers:**
- When a new proposal request is created
- When a revision is requested on an existing proposal
- When commodity prices move significantly during an active proposal's development
- When a pricing committee review is pending and requires supporting analysis
- Daily workload balancing scan across pricing analysts

**Actions:**
- Auto-gather pricing inputs for new proposals: current commodity index levels, basis differentials, transportation tariffs, credit spreads for the customer's rating, and historical pricing for comparable deals
- Generate draft pricing scenarios based on requested structures, applying current market data and standard margin requirements
- Perform error checking on completed pricing models: validate formulas, flag outliers, cross-check against market rates, and verify unit conversions (MMBtu to MWh, barrels to tons)
- Produce pricing committee briefing packages with risk analysis, margin impact, and competitive positioning assessment
- Balance analyst workload by recommending reassignment when one analyst has 3+ active proposals while another has availability

**Data Required:**
- Proposal Pipeline board
- Real-time commodity price feeds
- Pipeline tariff and transportation cost databases
- Credit rating feeds (Moody's, S&P) for counterparties
- Historical proposal data for benchmarking and error detection
- Analyst capacity data

**Autonomy Level:** Human-in-the-Loop
Data gathering and draft scenario generation are autonomous. All pricing outputs require analyst review before internal submission. Pricing committee decisions are human-only. Error checking runs automatically but alerts rather than auto-corrects.

**Example Interaction:**
> A sales rep submits an expedited proposal request for a 3-year LNG supply contract with Asian Petrochemical Corp — 500,000 MMBtu/month, customer requesting both fixed price and JKM-linked pricing options. Pricing Copilot immediately pulls: current JKM spot and forward curve, shipping rates from the Gulf Coast to Asia, applicable export terminal fees, the customer's BBB+ credit rating and corresponding credit premium, and three comparable LNG deals closed in the last 6 months. Within 30 minutes, the agent generates two draft pricing scenarios: (1) Fixed at $12.45/MMBtu with annual 2.5% escalation, and (2) JKM-linked with a $1.85/MMBtu discount to spot plus a floor at $9.50 and cap at $16.00. The agent flags that the fixed-price scenario carries higher margin risk given current forward curve contango, and recommends the collar structure as the preferred option. Pricing analyst Tom Reeves reviews the model, adjusts the collar cap to $15.50 based on his market view, and routes to the pricing committee — a process that would have taken two full days completed in 3 hours.

---

### Use Case 4: Customer Account Intelligence & Relationship Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy sales relationships are deep, multi-threaded, and span decades. A single customer — say, a major utility — might simultaneously be a buyer of natural gas, a counterparty on a power swap, a partner in a joint venture, a customer for EV charging infrastructure, and a prospect for green hydrogen. These relationships are managed by different sales reps, tracked in different systems, and there's no 360-degree customer view. When the CEO of an energy company calls their counterpart, they should know the full picture — but assembling that picture requires calling four people and checking three systems. Worse, when a sales rep leaves, their relationship intelligence leaves with them.

#### The Solution
monday.com CRM as a Customer Account Intelligence hub. Each customer has a master account record connected to: all active contracts (Contract Portfolio board), all pipeline opportunities (Sales Pipeline board), key contacts and relationship map (subitems with role, influence level, last interaction date), meeting notes (Docs), account plan (Doc), customer's public financial and strategic information (long text), and cross-sell opportunities. Dashboards show the full customer 360: total revenue, product mix, contract expiration timeline, open opportunities, relationship health score, and recent interactions.

#### The Outcome
True 360-degree customer view reducing account intelligence gathering from hours to seconds. 25% increase in cross-sell revenue by systematically identifying multi-product opportunities. Zero "relationship amnesia" when sales reps turn over — all account intelligence persists in the system.

#### Discovery Questions
1. "If your CEO asked for a complete picture of your relationship with your top 5 customers — every contract, every opportunity, every key contact — how quickly could you produce it?"
2. "Do you have situations where different teams sell different products to the same customer without coordinating?"
3. "When a senior sales rep leaves, how much relationship intelligence and account history walks out the door with them?"
4. "How do you currently identify cross-sell opportunities — for example, an existing gas customer who might also be a prospect for your clean energy products?"
5. "What does your account planning process look like for strategic accounts?"

#### Industry Context
Energy customer relationships are uniquely complex because the same entity can be simultaneously a customer, supplier, partner, and competitor across different business lines. A major oil company might buy natural gas from a utility's production subsidiary while selling jet fuel to the utility's aviation division and partnering on a wind farm through a JV. Key account management (KAM) is critical in an industry where the top 20 customers often represent 60%+ of revenue. The energy transition is creating new cross-sell dynamics: every existing customer is also a potential customer for clean energy products.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Customer Account Intelligence hub for an energy sales organization. Create a board called 'Strategic Accounts' with columns: Account Name (item name), Account Tier (dropdown: Tier 1 Strategic, Tier 2 Major, Tier 3 Growth, Tier 4 Transactional), Industry Segment (dropdown: Utility, Refiner, Petrochemical, Industrial Manufacturer, Government/Municipal, Trading House, Airline, Fleet Operator, Real Estate/C&I, Tech Company), Region (dropdown: North America, Europe, Middle East, Asia-Pacific, Latin America), Annual Revenue from Account ($M) (numbers), Total Contracted Value ($M) (numbers), Products Sold (tags: Natural Gas, Crude, Power, Pipeline, Refined Products, LNG, Hydrogen, Carbon Credits, EV Charging), Active Contracts (connect boards to Contract Portfolio), Open Opportunities (connect boards to Sales Pipeline), Account Manager (people), Sales Engineer (people), Executive Sponsor (people), Last Executive Meeting (date), Relationship Health (status: Strong, Stable, At Risk, New, Dormant), Credit Rating (dropdown: AAA, AA, A, BBB, BB, B, Below B, Not Rated), Customer Net Zero Target (text — e.g., 'Net Zero by 2040'), Clean Energy Readiness (dropdown: Active Buyer, Exploring, Not Engaged), Account Plan (file/link), Notes (long text). Create subitems for Key Contacts: Name, Title, Role (dropdown: Economic Buyer, Technical Buyer, Champion, Influencer, Gatekeeper, End User), Relationship Owner (people — who on our team owns this relationship), Last Interaction (date), Sentiment (dropdown: Positive, Neutral, Cautious, Negative). Create groups: 'Tier 1 Strategic', 'Tier 2 Major', 'Tier 3 Growth', 'New Accounts'. Add automations: when Last Executive Meeting is more than 90 days ago for Tier 1 accounts, alert Executive Sponsor; when Clean Energy Readiness is 'Exploring' and no clean energy products in Products Sold or open pipeline, create cross-sell opportunity prompt; when Relationship Health changes to 'At Risk', notify Account Manager and their VP. Create Dashboard: total revenue by account tier, product penetration matrix (accounts × products), relationship health distribution, accounts with upcoming contract expirations, and cross-sell opportunity pipeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Account Radar
**Agent Purpose:** Maintains a living, intelligent picture of every strategic account, proactively identifying cross-sell opportunities, relationship risks, and competitive threats before they become problems.

**Triggers:**
- When customer-related news is published (earnings reports, leadership changes, M&A, sustainability announcements)
- When a key contact hasn't been engaged in 60+ days
- When a contract expires within 6 months and no renewal opportunity exists in the pipeline
- Monthly account health review cycle
- When a customer's peer/competitor announces an energy transition initiative

**Actions:**
- Generate customer intelligence briefings before executive meetings: recent news, financial performance, strategic initiatives, and recommended talking points
- Identify cross-sell opportunities by matching customer profiles and announced strategies with available products (e.g., "Customer announced Net Zero 2035 target → no green hydrogen opportunity in pipeline → recommend outreach")
- Alert on relationship decay: key contacts not engaged, account health declining, competitive threats emerging
- Produce account plan templates pre-populated with current contract landscape, revenue trajectory, and identified white space
- Track customer's announced capital plans and energy transition commitments to anticipate future buying needs

**Data Required:**
- Strategic Accounts board with key contacts
- Contract Portfolio and Sales Pipeline boards
- News feeds and SEC filings for customer intelligence
- Industry databases for peer benchmarking
- Customer's public sustainability reports and ESG disclosures

**Autonomy Level:** Escalation-Based
News monitoring, intelligence gathering, and cross-sell identification are autonomous. Outreach recommendations and competitive alerts are routed to the account manager. Executive meeting briefings are auto-generated but can be customized before distribution.

**Example Interaction:**
> Account Radar detects that Pacific Northwest Utility (Tier 1 account, $85M annual revenue) just published their 2026 Integrated Resource Plan, announcing plans to retire two coal plants by 2030, add 2 GW of renewable capacity, and invest in green hydrogen for peaking power. The agent immediately cross-references the current relationship: PNW Utility currently buys natural gas for 5 generating stations, has a 10-year TSA for pipeline capacity, and was recently pitched (but hasn't committed to) a solar PPA. The agent generates an opportunity brief: "PNW Utility's IRP creates three immediate sales opportunities: (1) Transitional gas supply for retired coal replacement — estimated 120,000 MMBtu/day incremental, (2) Green hydrogen offtake for peaking units — estimated 50 tons/day by 2029, (3) Expanded renewable PPA portfolio to meet 2 GW target. Recommended: executive-level meeting within 30 days. Talking points: position our bundled gas+hydrogen+PPA solution as a 'transition-in-a-box' package." The brief is routed to Account Manager Lisa Chang and Executive Sponsor SVP Tom Bradley.

---

### Use Case 5: Sales Forecasting & Revenue Planning

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy sales forecasting is uniquely challenging because revenue depends on both volume and commodity prices, both of which fluctuate. A pipeline of $500M in contracted revenue can swing $50M+ based on index price movements. Sales teams submit monthly forecasts via spreadsheets that don't account for price sensitivity, seasonal demand patterns, or contract-specific volume flexibility (swing rights). Finance and trading desks need accurate forecasts for hedging and capital allocation, but sales forecasts consistently miss by 15–25%. The disconnect between sales pipeline data, contracted volumes, and market price assumptions creates a forecasting black hole.

#### The Solution
monday.com dashboards and formulas that integrate pipeline, contracted revenue, and market assumptions into a unified forecast. Each deal and contract has structured pricing data (index, basis, fixed price, volume) that feeds into automated forecast calculations. Scenario boards model high/medium/low commodity price assumptions and their impact on revenue. Sales reps update probability-weighted pipeline data in real-time, and automated roll-ups produce forecasts that finance and trading can trust. Seasonal adjustment factors are built into the model based on historical delivery patterns.

#### The Outcome
Forecasting accuracy improves from 75–85% to 90–95% range. Finance and trading receive weekly automated forecasts instead of monthly manual submissions. Hedging decisions improve with better volume and timing visibility.

#### Discovery Questions
1. "How accurate is your current sales forecast — what's the typical variance between forecast and actual revenue?"
2. "How do you account for commodity price fluctuations in your revenue forecast?"
3. "Does your finance or trading team trust the sales forecast enough to base hedging decisions on it?"
4. "How do you handle seasonal demand variations in your forecast — do you have historical patterns built in?"
5. "How long does it take your team to produce a forecast update, and how often do you do it?"

#### Industry Context
In energy, "volume risk" and "price risk" compound. A gas marketer might have a contract for 100,000 MMBtu/day with swing rights of ±15% — meaning actual delivered volume can range from 85,000 to 115,000 MMBtu/day based on customer demand (often weather-driven). Price risk comes from index-linked contracts where the realized price depends on where the commodity settles. Hedging desks need sales forecasts to know what positions to take in the futures market. Mark-to-market (MTM) valuation of the contract book fluctuates daily with commodity prices.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Sales Forecasting and Revenue Planning system for an energy company. Create a board called 'Revenue Forecast' with columns: Revenue Source (item name), Source Type (dropdown: Contracted Fixed, Contracted Index-Linked, Pipeline Weighted, Spot/Transactional), Customer (text), Product (dropdown: Natural Gas, Crude, Power, Refined Products, LNG, Hydrogen, Carbon Credits, Other), Monthly Volume (numbers), Volume Unit (dropdown: MMBtu, MWh, Barrels, Tons), Price Assumption (numbers, $/unit), Monthly Revenue ($K) (formula: Volume × Price), Confidence Level (dropdown: Committed, Highly Probable, Probable, Possible, Upside), Probability % (numbers), Weighted Revenue ($K) (formula: Monthly Revenue × Probability), Seasonality Factor (numbers — multiplier, e.g., 1.3 for winter gas), Adjusted Revenue ($K) (formula: Weighted Revenue × Seasonality), Contract Reference (connect boards to Contract Portfolio), Deal Reference (connect boards to Sales Pipeline), Sales Rep (people), Region (dropdown). Create groups by month: Jan 2026, Feb 2026, Mar 2026, etc. (12 months). Create a second board 'Price Scenarios' with columns: Scenario Name (item name — Base Case, High, Low), Commodity (dropdown), Price Assumption (numbers), Probability Weight % (numbers). Add automations: when a deal in Sales Pipeline moves to Closed Won, auto-create Revenue Forecast items for each month of the contract; when commodity prices in Scenarios board change, trigger dashboard refresh notification. Create Dashboard: monthly revenue forecast stacked bar (Committed vs Probable vs Possible), forecast vs actual trend (leave actual blank for future months), revenue by product type, scenario impact analysis (base vs high vs low), and confidence distribution pie chart."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Forecast Engine
**Agent Purpose:** Produces accurate, dynamic revenue forecasts by synthesizing pipeline data, contract terms, commodity price movements, and seasonal patterns — giving finance and trading trustworthy numbers.

**Triggers:**
- Daily commodity price update at market close
- When a deal stage changes in the Sales Pipeline
- When a contract volume nomination changes
- Weekly forecast compilation (Friday 3 PM)
- When finance requests ad-hoc forecast scenario

**Actions:**
- Recalculate revenue forecast whenever underlying variables change (price, volume, probability, new deals)
- Generate weekly forecast report with variance analysis versus previous week and commentary on key movers
- Model scenario impacts when commodity prices move significantly (e.g., "If Henry Hub averages $4.50 instead of $3.80, Q2 revenue increases by $12.3M")
- Identify forecast risks: contracts with high volume swing exposure, large pipeline deals with low probability, seasonal demand uncertainty
- Produce monthly forecast vs. actual reconciliation with root cause analysis for significant variances

**Data Required:**
- Revenue Forecast board
- Sales Pipeline and Contract Portfolio boards
- Real-time commodity price feeds and forward curves
- Historical delivery data for seasonal pattern analysis
- Weather forecast data for demand-driven volume adjustments

**Autonomy Level:** Fully Autonomous for calculations and reporting. Human review required before forecasts are submitted to finance. Scenario analysis is on-demand from leadership.

**Example Interaction:**
> On Friday afternoon, Forecast Engine compiles the weekly forecast. It detects that Henry Hub natural gas prices jumped 18% this week due to a cold snap forecast, impacting 47 index-linked contracts in the portfolio. The agent recalculates: Q1 revenue forecast increases by $8.7M at current strip prices. However, it also flags that three large industrial customers with swing rights are likely to reduce takes (historical pattern shows industrial demand drops when prices spike above $5/MMBtu), partially offsetting the price benefit by an estimated $2.1M. Net impact: +$6.6M. The agent produces a one-page brief: "Weekly Forecast Update: +$6.6M to Q1 vs. last week. Key driver: Henry Hub +18%. Note: three C&I accounts flagged for potential volume reduction at current price levels. Recommend: coordinate with trading desk on short-term hedging opportunity for the incremental upside." The report is automatically shared with VP Sales and the Head of Gas Trading.

---

### Use Case 6: Sales Territory & Quota Management

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy sales territories are defined by complex combinations of geography, customer segment, product type, and sometimes regulatory jurisdiction (FERC-regulated vs. state-regulated). Territory assignments and quota allocation happen annually in a chaotic process involving spreadsheets emailed between sales VPs, regional directors, and finance. Mid-year territory adjustments (new hires, departures, market shifts) trigger weeks of manual rebalancing. Quota setting is especially contentious because it must account for contracted base revenue (renewals), commodity price assumptions, and new business targets — a level of complexity that simple CRM quota tools can't handle.

#### The Solution
monday.com as a Territory and Quota Management platform. Territory boards map each sales rep to their assigned accounts, geographies, products, and segments. Quota boards break down annual targets into quarterly and monthly components with separate tracks for contracted base, renewal, and new business. Dashboards show territory coverage, quota attainment, and whitespace (unassigned accounts or underserved segments). Scenario planning for annual quota setting allows leadership to model different allocation approaches.

#### The Outcome
Annual territory and quota planning process reduced from 6 weeks to 2 weeks. Real-time visibility into quota attainment and territory coverage. Mid-year adjustments completed in days instead of weeks.

#### Discovery Questions
1. "How do you currently define and assign sales territories — is it geographic, segment-based, product-based, or some combination?"
2. "How long does your annual territory and quota planning process take, and how many iterations does it go through?"
3. "When you need to adjust territories mid-year — say, a rep leaves or a major new account enters the market — how disruptive is that process?"
4. "How do you separate contracted base revenue from new business in your quota targets?"
5. "Do you have visibility into which territories are overserved versus which have whitespace opportunities?"

#### Industry Context
Energy sales territories often follow pipeline networks, power grid regions (ERCOT, PJM, MISO, CAISO), or basin geography. Regulated utilities have defined service territories that determine competitive dynamics. Quota setting must account for the "annuity" nature of energy contracts — a rep who closed a 10-year contract last year has a large contracted base that reduces their new business target. This makes energy quota allocation fundamentally different from SaaS or product sales quotas.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Sales Territory and Quota Management system for an energy company. Create a board called 'Territory Map' with columns: Territory Name (item name), Sales Rep (people), Region (dropdown: Northeast, Southeast, Midwest, Gulf Coast, Mountain West, Pacific, Texas/ERCOT, International), Customer Segment Focus (tags: Utility, Industrial C&I, Refiner, Government, Corporate), Product Focus (tags: Gas, Power, Crude, Refined, Clean Energy), Number of Accounts (numbers), Total Account Revenue ($M) (numbers), Whitespace Accounts (numbers — prospects in territory not yet engaged), Territory Score (formula: weighted composite of revenue + whitespace + growth potential). Create a second board 'Quota Tracker' with columns: Sales Rep (item name / people), Territory (connect boards to Territory Map), Annual Quota ($M) (numbers), Contracted Base ($M) (numbers — existing contracts renewing), Renewal Target ($M) (numbers), New Business Target ($M) (numbers), Q1 Target ($M) (numbers), Q1 Actual ($M) (numbers), Q1 Attainment % (formula), Q2 Target through Q4 Actual (repeat pattern), YTD Actual ($M) (formula: sum of quarterly actuals), YTD Attainment % (formula), Pipeline Coverage Ratio (formula: open pipeline value / remaining target), Commodity Price Adjustment ($M) (numbers — adjustment factor for index-linked contract valuation). Create groups in Territory Map: by Region. Create groups in Quota Tracker: 'On Track (>90%)', 'Watch (70-90%)', 'At Risk (<70%)'. Add automations: when YTD Attainment drops below 70%, move to 'At Risk' group and notify VP Sales; when Pipeline Coverage falls below 2x, alert sales rep; quarterly auto-archive actual numbers and reset current quarter actuals. Create Dashboard: territory map visualization, quota attainment leaderboard, pipeline coverage by rep, contracted base vs new business mix, and territory whitespace analysis."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Territory Optimizer
**Agent Purpose:** Ensures optimal territory coverage, fair quota allocation, and proactive identification of coverage gaps and rebalancing needs.

**Triggers:**
- Monthly territory health review
- When a sales rep joins or leaves the team
- When a major new account enters a territory (acquisition, expansion, regulatory change)
- Quarterly quota reforecast cycle
- When territory attainment variance exceeds 30% across comparable territories

**Actions:**
- Analyze territory balance: identify over/under-served territories based on account count, revenue, and growth potential
- Generate territory rebalancing proposals when team changes occur, minimizing customer disruption
- Produce quarterly quota adjustment recommendations based on commodity price changes, contract wins/losses, and market shifts
- Identify whitespace opportunities by territory: unengaged accounts, segments without coverage, emerging markets
- Create "territory playbooks" for new sales reps with account profiles, relationship history, and priority targets

**Data Required:**
- Territory Map and Quota Tracker boards
- Sales Pipeline and Contract Portfolio for revenue and pipeline data
- HR data for team changes
- Market data for territory growth potential assessment

**Autonomy Level:** Human-in-the-Loop
Territory analysis and recommendations are auto-generated. All territory and quota changes require VP Sales approval. Territory playbooks for new reps are auto-created but reviewed by regional directors.

**Example Interaction:**
> In April, Territory Optimizer detects that two Gulf Coast territory reps have radically different attainment levels: Sarah's territory is at 142% of Q1 target with a 5x pipeline coverage ratio, while Marcus's adjacent territory is at 67% with 1.2x coverage. The agent analyzes the root cause: two major refinery accounts in Marcus's territory delayed contract renewals due to their own M&A activity, while Sarah's territory benefited from an unplanned spot gas sale to a new LNG exporter. The agent recommends: (1) Temporarily shift two of Sarah's lower-priority prospect accounts to Marcus to improve his pipeline, (2) Adjust Marcus's Q2 quota downward by $3M to account for the deferred renewals (which are now expected in Q3), and (3) Assign a deal support resource to help Marcus accelerate the LNG exporter opportunity that's emerging in his territory. The recommendation includes projected impact on both reps' attainment trajectories for the rest of the year.

---

### Use Case 7: Competitive Intelligence & Win/Loss Analysis

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy sales teams compete against well-resourced rivals — Shell, BP, Vitol, NextEra, and dozens of regional players — but competitive intelligence is scattered and anecdotal. Sales reps know bits and pieces about competitor pricing and strategies from customer conversations, but there's no systematic capture or analysis. Win/loss reviews happen sporadically (if at all), and the lessons learned don't flow back to the broader team. When a competitor launches a new product or pricing strategy, it takes weeks for the sales organization to recognize the pattern and respond.

#### The Solution
monday.com as a Competitive Intelligence and Win/Loss tracker. Every closed deal (won or lost) includes structured competitive data: competitor(s) involved, competitor pricing (if known), reason for win/loss (dropdown + narrative), and customer feedback. A dedicated Competitive Intelligence board tracks competitor moves: pricing changes, product launches, M&A activity, key personnel changes, and strategic announcements. Dashboards analyze win rates by competitor, common loss reasons, and pricing competitiveness.

#### The Outcome
Structured win/loss data on 100% of closed deals, replacing anecdotal feedback. Competitive response time reduced from weeks to days through systematic intelligence tracking. 10–15% improvement in competitive win rate by applying lessons learned systematically.

#### Discovery Questions
1. "When you lose a deal to a competitor, do you have a structured process to understand why — or does it depend on the individual rep?"
2. "How quickly does your sales team learn when a competitor changes their pricing strategy or launches a new product?"
3. "Can you pull up your win rate against specific competitors right now? Do you know who you lose to most often and why?"
4. "How do competitive insights from one deal flow to other reps facing the same competitor in different territories?"
5. "Do you track competitor activity systematically, or does it come through the grapevine?"

#### Industry Context
The energy trading and sales landscape has distinct competitive tiers: supermajors (Shell, ExxonMobil, BP, TotalEnergies, Chevron), commodity traders (Vitol, Trafigura, Glencore, Mercuria), independent producers (EOG, Pioneer, Devon), utilities (NextEra, Duke, Southern), and renewable pure-plays (Ørsted, Enel Green Power). Competitive dynamics differ by product: gas and power markets are highly competitive with slim margins, while specialized products (LNG, hydrogen, carbon credits) offer more differentiation. Price transparency varies — gas and power have published indices, but basis differentials and credit terms create competitive differentiation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Competitive Intelligence and Win/Loss Analysis system for an energy sales team. Create a board called 'Win/Loss Register' with columns: Deal Name (item name), Customer (text), Product Type (dropdown: Gas, Power, Crude, Pipeline, Refined, LNG, Hydrogen, Carbon Credits, Bundled), Outcome (status: Won, Lost — Pricing, Lost — Product Fit, Lost — Relationship, Lost — Incumbent, Lost — Regulatory, No Decision), Competitor(s) (tags: Shell, BP, Vitol, Trafigura, NextEra, Enel, ExxonMobil, Duke Energy, Regional Player, None/Sole Source), Competitor Pricing (text — what we know), Our Pricing (text), Price Competitive? (dropdown: We Were Lower, Comparable, We Were Higher, Unknown), Deal Value ($M) (numbers), Win/Loss Reason — Primary (dropdown: Price, Relationship, Product Capability, Contract Flexibility, Credit Terms, Speed of Response, Technical Expertise, Brand/Reputation, Regulatory Advantage, Bundled Solution), Win/Loss Narrative (long text), Customer Feedback (long text), Lessons Learned (long text), Sales Rep (people), Date Closed (date), Region (dropdown). Create a second board 'Competitor Tracker' with columns: Competitor (item name), Intelligence Type (dropdown: Pricing Change, New Product, M&A Activity, Leadership Change, Strategy Shift, Market Entry, Market Exit, Partnership), Summary (long text), Source (dropdown: Customer Conversation, Public Filing, News, Industry Event, Sales Rep Intel, Partner), Reported By (people), Date Reported (date), Impact Assessment (dropdown: Low, Medium, High, Critical), Response Action (text), Validated (checkbox). Create groups in Win/Loss: 'This Quarter', 'Previous Quarter', 'Archive'. Create groups in Competitor Tracker: by competitor name. Add automations: when Outcome is any 'Lost' status, assign VP Sales for review and create a 'lessons learned' distribution notification to the team; when new high-impact Competitor Intelligence is added, notify all sales reps in the affected region/product. Create Dashboard: win rate by competitor, loss reason distribution, pricing competitiveness analysis, competitor activity timeline, and win rate trend by quarter."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Compete IQ
**Agent Purpose:** Systematically captures, analyzes, and distributes competitive intelligence, ensuring the sales team always knows what competitors are doing and how to win against them.

**Triggers:**
- When a deal is marked as Won or Lost
- When new competitor intelligence is logged
- When a competitor is mentioned in energy industry news
- Monthly competitive landscape review
- When a sales rep is entering a deal against a competitor they haven't faced before

**Actions:**
- Generate win/loss analysis reports identifying patterns: which competitors we beat, which beat us, and the most common differentiators
- Produce competitor battle cards automatically from accumulated intelligence: pricing tendencies, strengths, weaknesses, and winning strategies
- Monitor energy industry news for competitor moves and auto-create intelligence entries when relevant activity is detected
- Alert sales reps entering competitive situations with relevant battle card and recent win/loss context against that specific competitor
- Generate quarterly competitive landscape reports for sales leadership showing market share trends and strategic recommendations

**Data Required:**
- Win/Loss Register and Competitor Tracker boards
- Sales Pipeline for active competitive situations
- Energy industry news feeds
- Public filings (SEC 10-K, earnings calls) for major competitors
- Historical pricing and deal data

**Autonomy Level:** Fully Autonomous for monitoring and analysis. Battle card generation is auto-published. Strategic recommendations require sales leadership review.

**Example Interaction:**
> A sales rep logs a $35M power PPA loss to NextEra Energy, citing "pricing" as the primary reason — NextEra offered a PPA rate $2.50/MWh lower. Compete IQ immediately analyzes the broader pattern: this is the fourth PPA loss to NextEra in 6 months, all in the Southeast region, all with pricing gaps of $2–4/MWh. The agent identifies that NextEra's cost advantage likely stems from their ITC (Investment Tax Credit) monetization strategy and vertically integrated solar development. It updates the NextEra battle card with this insight and generates a strategic alert to VP Sales: "NextEra is systematically undercutting our PPA pricing in the Southeast. Analysis suggests a structural cost advantage of $2–3/MWh from tax credit optimization. Recommended response options: (1) Partner with a solar developer who can pass through ITC benefits, (2) Compete on contract flexibility and bundled services rather than price, or (3) Focus Southeast PPA efforts on segments where NextEra has less presence (municipal utilities, C&I rooftop)." The alert includes a map showing NextEra's recent wins and our win pattern for geographic analysis.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| PPA | Power Purchase Agreement — long-term contract to buy electricity at a set price, critical for renewable project financing |
| ETRM | Energy Trading and Risk Management — specialized software systems for managing commodity transactions |
| Henry Hub | Primary US natural gas pricing benchmark, located in Louisiana |
| WTI | West Texas Intermediate — primary US crude oil pricing benchmark |
| TTF | Title Transfer Facility — primary European natural gas pricing benchmark |
| JKM | Japan Korea Marker — primary Asian LNG pricing benchmark |
| Basis Differential | Price difference between a regional delivery point and the benchmark hub |
| Take-or-Pay | Contract clause requiring buyer to pay for minimum committed volume regardless of actual offtake |
| TSA | Transportation Service Agreement — contract for pipeline capacity |
| Swing Rights | Contractual flexibility to increase or decrease volume within defined limits |
| C&I | Commercial & Industrial — large-account customer segment for utilities and energy suppliers |
| ISDA | International Swaps and Derivatives Association — standard framework for derivative contracts |
| MTM | Mark-to-Market — daily valuation of contract book based on current market prices |
| Collar | Pricing structure with a price floor and ceiling, limiting both downside and upside exposure |
| ITC/PTC | Investment Tax Credit / Production Tax Credit — US tax incentives for renewable energy |
| FERC | Federal Energy Regulatory Commission — US regulator of interstate energy transmission |
| ERCOT | Electric Reliability Council of Texas — Texas electricity grid operator |
| PJM | PJM Interconnection — electricity grid operator covering 13 US states |
| IRP | Integrated Resource Plan — utility's long-term plan for meeting electricity demand |
| Vibe | monday.com's natural language app builder that generates boards, workflows, and apps from text prompts |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP/SVP of Sales / Commercial | Sets sales strategy, manages P&L, owns revenue targets | Decision-maker |
| Regional Sales Director | Manages territory teams, owns regional quota, approves deal structures | Decision-maker |
| Senior Sales Rep / Account Executive | Manages customer relationships, develops and closes deals | Influencer |
| Sales Engineer / Pricing Analyst | Builds pricing models, supports proposal development, technical credibility | Influencer |
| Contract Manager | Manages contract lifecycle, renewal negotiations, compliance | User |
| Head of Gas/Power/LNG Trading | Manages commodity risk, needs sales forecasts for hedging | Decision-maker (for pricing decisions) |
| VP Business Development | Identifies new markets, strategic partnerships, M&A opportunities | Influencer |
| Credit/Risk Manager | Assesses counterparty credit risk, approves deal terms | Influencer (can veto deals) |
| CFO / Head of Finance | Needs accurate revenue forecasts, approves large contract structures | Decision-maker (for major deals) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations | Fulfills what Sales sells — supply logistics, delivery scheduling, asset utilization | Operations management, delivery tracking |
| Finance | Revenue recognition, hedging coordination, credit risk, billing | Financial reporting, billing workflows |
| Legal | Contract drafting, regulatory compliance, dispute resolution | Legal matter management, contract workflow |
| Product & R&D | Develops new products that Sales brings to market; field feedback loop | Product development tracking, field trial management |
| Marketing | Brand positioning, demand generation, content for sales enablement | Marketing campaign management, lead tracking |
| Customer Success | Post-sale relationship management, upsell/cross-sell identification | Customer health scoring, renewal management |
| Trading/Risk | Hedges commodity exposure from Sales commitments, manages portfolio risk | Risk dashboard, position management |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce | Dominant CRM in enterprise, but energy-specific configuration is painful and expensive | monday.com CRM offers faster deployment, better UX, and energy-specific customization without $500K implementation projects |
| SAP CRM/S4HANA | Embedded in ERP-centric organizations, rigid and expensive to modify | monday.com provides the agile sales management layer on top of SAP back-end, complementing rather than replacing |
| Allegro / ION / RightAngle (ETRM) | Specialized trading and risk systems, not CRM or pipeline tools | monday.com complements ETRM by adding the sales pipeline, proposal management, and customer relationship layer that ETRM lacks |
| Microsoft Dynamics 365 | Often IT-mandated, but poor energy industry fit without heavy customization | monday.com offers superior no-code customization for energy-specific workflows with native Microsoft integrations |
| HubSpot | Strong for SMB/mid-market, but lacks the complexity handling for energy deal structures | monday.com handles multi-year, commodity-linked, multi-stakeholder deals that exceed HubSpot's data model |
| Custom/homegrown spreadsheets | The actual incumbent in most energy sales organizations — "we've always done it in Excel" | monday.com provides the structure, automation, and visibility of enterprise CRM with the flexibility and familiarity of spreadsheets |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Salesforce / SAP CRM" | "Many energy companies have CRM investments that their sales teams barely use because they weren't built for energy deal complexity. monday.com can serve as the agile working layer on top of your CRM — where reps actually manage their day-to-day pipeline — with integration flowing data back to your system of record." |
| "Our deals are too complex for a general-purpose tool" | "That's exactly why energy sales teams struggle with traditional CRM. monday.com's flexibility lets you model commodity-linked pricing, multi-year contract structures, and volume commitments natively. Show me the most complex deal structure you have — I'll build the tracking board in 10 minutes with Vibe." |
| "We need to integrate with our ETRM system" | "Absolutely — and monday.com has robust API and integration capabilities. The ETRM handles the financial and logistics side; monday.com handles the sales pipeline, customer relationships, and team collaboration that ETRM was never designed for. They're complementary, not competitive." |
| "Sales reps won't adopt another tool" | "Energy sales reps don't want another tool either. But they do want their proposals done faster, their pipeline visible, and their forecasts accurate without spending Friday afternoons in spreadsheets. monday.com's Vibe lets them describe what they need in plain language and get a working solution immediately. Adoption happens when the tool actually helps." |
| "Our data is commercially sensitive — deal pricing, customer terms" | "Understood. monday.com provides enterprise security: SOC 2 Type II, data encryption at rest and in transit, role-based permissions, and data residency options. You can control exactly who sees deal pricing versus pipeline status versus customer contacts." |

## Proof Points
*(To be populated with customer references)*
- [Energy trading company managing sales pipeline on monday.com]
- [Utility managing C&I sales and contract renewals on monday.com]
- [Renewable energy developer tracking PPA pipeline on monday.com]
- [Midstream company managing TSA sales and capacity on monday.com]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
