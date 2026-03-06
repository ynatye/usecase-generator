# Electricity, Oil & Gas × Procurement Playbook

## Overview

Procurement in Electricity, Oil & Gas (E, O&G) is one of the highest-spend, most complex procurement functions in any industry. A single upstream E&P company can manage $2-10B+ in annual procurement spend across categories as diverse as drilling rigs ($300K-$1M/day), subsea equipment, FPSO (Floating Production, Storage & Offloading) vessel charters, pipeline steel, rotating equipment (compressors, turbines, pumps), chemical feedstocks, oilfield services (Schlumberger, Halliburton, Baker Hughes), EPC (Engineering, Procurement & Construction) contracts, and now increasingly renewable energy equipment (wind turbines, solar panels, battery storage systems). For utilities, the spend profile shifts to transmission/distribution equipment (transformers, switchgear, conductors), generation fuel (natural gas, coal, uranium), renewable PPAs (Power Purchase Agreements), and vegetation management services.

The organizational structure typically features a Chief Procurement Officer (CPO) or VP Supply Chain reporting to the CFO or COO. Procurement is segmented by category: Capital Projects (CAPEX procurement for major projects — wells, plants, pipelines), Operations & Maintenance (MRO — Maintenance, Repair & Operations), Services (oilfield services, consulting, IT, facilities), and increasingly a dedicated Energy Transition/Renewables category. Teams are distributed globally — headquarters handles strategic sourcing and category management, while regional procurement hubs and on-site materials management teams handle tactical buying and logistics. In large IOCs (Integrated Oil Companies), procurement headcount can reach 500-2,000+.

The regulatory and compliance landscape is intense. The Foreign Corrupt Practices Act (FCPA) and UK Bribery Act require rigorous supplier due diligence, especially for operations in high-risk geographies (Middle East, West Africa, Central Asia). Sanctions compliance (OFAC, EU sanctions) adds complexity — procurement must screen suppliers against SDN (Specially Designated Nationals) lists for every transaction. Environmental regulations increasingly mandate sustainable procurement — Scope 3 emissions reporting under SEC climate disclosure rules means procurement must track supplier carbon intensity. Local content requirements in countries like Brazil (ANP regulations), Nigeria (NCDMB), and Norway (government expectations) mandate minimum percentages of local suppliers and workforce. This creates a procurement function that is as much about risk management and compliance as it is about cost optimization.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Energy procurement teams use 8-15 disconnected systems (SAP Ariba, Oracle, Coupa, homegrown databases, Excel trackers, email) creating massive data fragmentation and zero cross-category visibility |
| 2 | Scale Impact Without Overhead | High | Global procurement teams manage 5,000-50,000+ suppliers and $2-10B+ spend with constant pressure to reduce headcount while expanding scope (energy transition, ESG compliance, supply chain resilience) |
| 3 | Replace or Radically Augment Headcount | Medium-High | AI can automate 40-60% of tactical procurement activities — PO processing, supplier screening, contract extraction, spend analytics — freeing procurement professionals for strategic sourcing |

## Prioritized Use Cases

---

### Use Case 1: Supplier Qualification & Compliance Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies maintain Approved Vendor Lists (AVLs) with 5,000-50,000+ suppliers, each requiring qualification before any PO is issued. Qualification involves technical capability assessment (API certifications, ASME stamps, ISO 9001/14001/45001), financial health screening (Dun & Bradstreet, credit reports), HSE performance review (TRIR — Total Recordable Incident Rate, EMR — Experience Modification Rate), insurance verification (minimum $5-25M general liability for oilfield work), sanctions screening (OFAC, EU, UN sanctions lists), FCPA/anti-bribery due diligence (especially for agents and intermediaries in high-risk countries), and local content certification where applicable. This qualification must be renewed annually or biannually. Currently, most energy companies manage this through a combination of SAP SRM, spreadsheets, email, and manual document review. A single late or missed re-qualification can result in project delays (if a critical supplier is suspended) or compliance violations (if an unqualified supplier slips through).

#### The Solution
monday.com as the supplier qualification lifecycle management platform. A master Supplier Board with items for each supplier, columns for Supplier Name, Category (dropdown: Drilling Services, Completions, Production Equipment, Pipeline/Midstream, EPC Contractor, MRO Supplier, IT/Telecom, Professional Services, Renewables Equipment, Logistics/Marine), Risk Tier (status: Tier 1 Critical-Red, Tier 2 Strategic-Orange, Tier 3 Transactional-Blue, Tier 4 Spot Buy-Gray), Qualification Status (status: Qualified-Green, Conditional-Yellow, Pending Review-Orange, Suspended-Red, Blacklisted-Black), Technical Certifications (multi-select: API Q1, API Q2, ASME, ISO 9001, ISO 14001, ISO 45001, OHSAS, NACE, AWS), TRIR (number), EMR (number), Insurance Expiry (date), Sanctions Screening Date (date), FCPA Due Diligence Status (status), Local Content Certification (status), Financial Health Score (number), Connected POs/Contracts (connected board), and Qualification Expiry Date (date). Automations trigger re-qualification workflows 90 days before expiry, flag suppliers with TRIR above threshold, and block PO creation for suspended suppliers.

#### The Outcome
75% reduction in supplier qualification cycle time (from 8-12 weeks to 2-3 weeks). 100% compliance with sanctions screening and FCPA requirements through enforced workflows. Zero unauthorized supplier spend through automated AVL enforcement. $500K+ annual savings from reduced procurement team time on manual qualification tracking.

#### Discovery Questions
1. "How many suppliers are on your Approved Vendor List, and what's your current process for initial qualification and periodic re-qualification?"
2. "How quickly can you pull up the complete compliance file for any supplier — certifications, insurance, sanctions screening, FCPA due diligence, HSE metrics — if a regulator or auditor requests it?"
3. "Have you ever had a project delay because a critical supplier's qualification lapsed and you had to emergency re-qualify them?"
4. "How do you currently handle sanctions screening — is it a point-in-time check at onboarding, or do you screen against updated SDN lists regularly?"
5. "What's your process for tracking local content requirements and certifications for suppliers in countries like Brazil, Nigeria, or Norway?"

#### Industry Context
API (American Petroleum Institute) certification is the gold standard for oilfield equipment and service suppliers. API Q1 covers manufacturing quality management, API Q2 covers service supply chain quality management. ASME (American Society of Mechanical Engineers) stamps are required for pressure vessels and piping. TRIR (Total Recordable Incident Rate) is the primary HSE performance metric — most major operators require suppliers to have a TRIR below 1.0 (some below 0.5) to qualify. EMR (Experience Modification Rate) is a workers' compensation insurance metric — rates above 1.0 indicate worse-than-average safety performance. FCPA violations in the energy sector have resulted in some of the largest corporate fines in history (Petrobras-related fines exceeding $3.5B). The ISNetworld, Avetta (formerly PICS), and Veriforce platforms are industry-standard supplier prequalification databases that procurement teams reference but don't replace internal qualification processes.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Supplier Qualification & Compliance Management system for an energy company. Board 1 — Supplier Master Registry: Supplier Name (text), Supplier ID (auto-number with prefix 'SUP-'), Category (dropdown: Drilling & Well Services, Completions & Stimulation, Production Equipment, Pipeline & Midstream, EPC Contractor, MRO/Spare Parts, Chemicals & Catalysts, IT & Telecom, Professional Services, Marine & Logistics, Renewables Equipment, Environmental Services), Risk Tier (status: Tier 1 Critical-Red, Tier 2 Strategic-Orange, Tier 3 Preferred-Blue, Tier 4 Transactional-Gray), Qualification Status (status: Fully Qualified-Green, Conditionally Qualified-Yellow, Under Review-Orange, Suspended-Red, Blacklisted-Black), Country of Origin (text), Operating Regions (dropdown: North America, Latin America, Europe, Middle East, West Africa, Central Asia, Asia Pacific), Technical Certs (dropdown: API Q1, API Q2, ASME U/S/R, ISO 9001, ISO 14001, ISO 45001, NACE, AWS D1.1), TRIR (numbers), EMR (numbers), Insurance GL Amount (numbers with $), Insurance Expiry (date), OFAC Screening Date (date), OFAC Status (status: Clear-Green, Match Found-Red, Pending-Yellow), FCPA Due Diligence (status: Complete-Green, In Progress-Yellow, Not Started-Red, High Risk-Orange), Local Content Certified (status: N/A-Gray, Certified-Green, Pending-Yellow, Non-Compliant-Red), D&B Financial Score (numbers), Qualification Expiry (date), Primary Contact (text), Contact Email (email), Documents (file), Connected Contracts (connect). Automations: When Qualification Expiry is within 90 days, create re-qualification task and notify category manager; When TRIR exceeds 1.0, change Risk Tier to highlight and notify HSE; When OFAC Screening Date is older than 90 days, flag for re-screening; When Qualification Status changes to Suspended, notify all connected Contract owners. Views: Main Table, Kanban by Qualification Status, Map view by Operating Regions, Dashboard with qualification status breakdown, expiring qualifications next 90 days, TRIR distribution chart, sanctions screening currency, and spend by qualification tier."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SupplierShield Compliance Agent
**Agent Purpose:** Continuously monitor supplier compliance status and proactively manage qualification lifecycle to prevent lapses and compliance violations.

**Triggers:**
- Daily scan of all suppliers with qualifications expiring within 90 days
- When OFAC/EU sanctions lists are updated (weekly)
- When a supplier's insurance certificate is uploaded (verify coverage adequacy)
- When a new PO is created against any supplier (real-time qualification check)
- When negative news about a supplier is detected (integration with media monitoring)

**Actions:**
- Re-screen all active suppliers against updated sanctions lists and flag new matches
- Generate re-qualification packages (pre-populated forms based on existing data) and send to suppliers 90 days before expiry
- Validate uploaded insurance certificates against minimum coverage requirements by contract type
- Block PO creation and alert buyer when supplier is Suspended, Blacklisted, or has expired qualification
- Monitor supplier TRIR trends and flag deterioration patterns
- Generate monthly compliance dashboard report for CPO

**Data Required:**
- OFAC SDN list API, EU sanctions database, UN consolidated list
- ISNetworld/Avetta API for third-party HSE data
- D&B or CreditSafe API for financial health monitoring
- Supplier master registry data from monday.com
- Contract and PO boards for spend linkage

**Autonomy Level:** Escalation-Based
Agent autonomously screens sanctions lists, generates re-qualification packages, and blocks non-compliant POs. Suspends suppliers automatically only for confirmed sanctions matches (with immediate escalation to Legal). All other flags (HSE deterioration, financial concerns, FCPA issues) are escalated to category managers for human decision.

**Example Interaction:**
> On a routine weekly sanctions re-screening, the SupplierShield agent identifies that a Tier 2 oilfield services supplier operating in the Caspian region has a 78% name match to a newly added entity on the OFAC SDN list. The agent immediately flags the supplier as "OFAC Status: Match Found," changes Qualification Status to "Under Review," and generates an alert to the Legal/Compliance team: "URGENT: Potential sanctions match for SUP-2847 (Caspian Technical Services Ltd). 78% match to OFAC SDN Entity #42891. 3 active POs totaling $2.4M. Recommend immediate spend freeze pending enhanced due diligence. False positive probability: Medium — entity names are similar but registration countries differ (supplier: Kazakhstan, SDN entity: Russia). Legal review required within 24 hours." The agent simultaneously blocks any new POs against this supplier and notifies the 2 active project managers of the pending review.

---

### Use Case 2: Capital Project Procurement Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Major capital projects in E, O&G — a new drilling campaign, pipeline construction, refinery turnaround, LNG terminal, offshore platform, or renewable energy farm — involve hundreds to thousands of procurement line items worth $50M-$5B+. Each item follows a lifecycle: specification → requisition → RFQ/ITB (Invitation to Bid) → bid evaluation → award → PO → expediting → inspection → delivery → installation. For a single offshore platform, there might be 5,000+ procurement line items across structural steel, rotating equipment, electrical systems, instrumentation, subsea equipment, and marine services — each with different lead times (6 months for standard valves, 18+ months for large compressors, 24+ months for subsea Xmas trees). Current state: SAP MM handles PO processing, but project procurement teams track the critical path in Excel spreadsheets that are constantly out of date, vendor expediting happens via email, inspection status is tracked on whiteboards at fabrication yards, and the project director has no single view of procurement health. Late delivery of a single critical-path item can delay project startup by months, costing $1-5M+ per day in lost revenue.

#### The Solution
monday.com as the capital project procurement tracking and expediting layer on top of SAP/Oracle. A Project Procurement Board per major project with items for each major procurement package or equipment item. Columns: Package/Equipment Name, Package ID (linked to SAP PO), Category (dropdown: Rotating Equipment, Static Equipment, Piping/Valves, Electrical, Instrumentation/Controls, Structural Steel, Subsea, Marine, Civil, Renewables), Supplier (connected to Supplier Master), PO Value (numbers), Currency, Lead Time Weeks (numbers), Order Date (date), Required on Site (date), Committed Delivery (date), Forecast Delivery (date), Status (status: Specification-Purple, RFQ Issued-Blue, Bid Evaluation-Cyan, Awarded-Teal, On Order-Orange, In Fabrication-Yellow, Ready for Inspection-Pink, Inspection Complete-Light Green, Shipped-Green, Delivered-Dark Green, Installed-Black), Critical Path (checkbox), Risk Flag (status: On Track-Green, Watch-Yellow, At Risk-Orange, Critical-Red, Force Majeure-Purple), Expediting Notes (long text), and Inspection Reports (file). Timeline views show the procurement schedule against project milestones. Dashboard views highlight critical-path items at risk.

#### The Outcome
30% improvement in on-time delivery through proactive expediting triggered by automated risk flags. $10-50M+ savings per project from avoided delays (industry benchmark: 1 day delay on a major project = $1-5M). Single source of truth eliminating 20+ separate Excel trackers per project. Real-time executive visibility into procurement health across the project portfolio.

#### Discovery Questions
1. "On your last major capital project, how did procurement delays impact the overall project schedule — and what was the financial impact of those delays?"
2. "How does your project procurement team currently track thousands of line items across different suppliers, lead times, and delivery dates — is it a single system or multiple Excel trackers?"
3. "What's your expediting process when a critical-path supplier starts falling behind schedule — how quickly do you identify the risk and what's the escalation path?"
4. "How do you manage procurement across multiple simultaneous capital projects — do category managers have visibility into demand aggregation opportunities across projects?"
5. "When a force majeure event disrupts your supply chain (COVID, Suez Canal blockage, sanctions), how quickly can you assess the impact across all active projects?"

#### Industry Context
Capital project procurement in oil & gas follows the AACE (Association for the Advancement of Cost Engineering) classification system — Class 1 (detailed) through Class 5 (conceptual) estimates. Procurement lead times for major equipment are extreme: gas turbines (18-24 months), subsea Xmas trees (18-30 months), large-bore valves (12-18 months), FPSO hull conversion (24-36 months). Inspection is a critical stage — Third Party Inspection (TPI) agencies like Bureau Veritas, Lloyd's, DNV, and TÜV perform factory acceptance tests (FAT), hydrostatic tests, and dimensional inspections. The EPC (Engineering, Procurement, Construction) contract model means procurement often straddles the operator and the EPC contractor, creating interface management challenges. Materials Management involves tracking items through fabrication yards, ports, customs, laydown yards, and installation — each handoff is a potential delay point.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Capital Project Procurement Tracking system for an energy project. Columns: Package/Equipment Name (text), Package ID (text), Category (dropdown: Rotating Equipment-Compressors/Turbines/Pumps, Static Equipment-Vessels/Tanks/Heat Exchangers, Piping & Valves, Electrical-Transformers/Switchgear/Cable, Instrumentation & Controls, Structural Steel, Subsea Equipment, Marine/Offshore Services, Civil Works, Renewables-Turbines/Panels/Inverters, EPC Services), Supplier (text), PO Number (text), PO Value (numbers with $), Lead Time Weeks (numbers), Order Date (date), Required on Site Date (date), Supplier Committed Date (date), Current Forecast Date (date), Variance Days (formula: Forecast minus Required, show negative as green positive as red), Status (status: Specification-Purple, RFQ Issued-Blue, Bids Under Evaluation-Cyan, PO Awarded-Teal, In Fabrication-Orange, Factory Testing/FAT-Yellow, Ready for Shipment-Light Green, In Transit-Green, At Site-Dark Green, Installed & Commissioned-Black), Critical Path (status: Yes-Red, No-Gray), Risk Flag (status: On Track-Green, Monitor-Yellow, At Risk-Orange, Critical-Red, Force Majeure-Purple), Inspection Status (status: Not Required-Gray, Scheduled-Blue, In Progress-Orange, Passed-Green, Failed-Red, Waived-Yellow), Inspector (people), Expediting Contact (text), Last Expediting Update (date), Expediting Notes (long text), Shipping Documents (file), Inspection Reports (file). Automations: When Current Forecast Date exceeds Required on Site Date and Critical Path is Yes, set Risk Flag to Critical and notify project director; When Last Expediting Update is older than 14 days and Status is In Fabrication, remind procurement lead; When Inspection Status changes to Failed, immediately notify engineering and set Risk Flag to At Risk. Views: Main Table sorted by Required on Site Date, Timeline/Gantt showing Order Date to Forecast Date per item, Kanban by Status, Dashboard with procurement spend by category, on-time delivery rate, risk flag distribution, critical path items at risk, and overall project procurement health score."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProcurementPulse Project Expediting Agent
**Agent Purpose:** Proactively monitor capital project procurement schedules, predict delivery risks before they materialize, and automate expediting communications.

**Triggers:**
- Daily scan of all items where Current Forecast Date is within 30 days of Required on Site Date
- When a supplier updates delivery forecast (manual entry or integration)
- When Inspection Status changes to Failed
- Weekly supplier performance trend analysis
- When external supply chain disruption event is detected (news monitoring)

**Actions:**
- Calculate schedule risk score for each procurement package based on lead time, supplier history, and current status
- Generate automated expediting emails to suppliers for items trending behind schedule
- Create "procurement weather report" for weekly project review meetings
- Flag demand aggregation opportunities across concurrent projects (e.g., same valve type needed on 3 projects — negotiate volume discount)
- Predict potential delays based on supplier historical delivery performance patterns
- Auto-escalate to project director when critical-path items shift to "At Risk"

**Data Required:**
- Project procurement board data (all columns)
- Historical supplier delivery performance (on-time rate, average delay by equipment type)
- Project milestone schedule for impact assessment
- Parallel project procurement boards for aggregation opportunities
- Supply chain news feeds for disruption early warning

**Autonomy Level:** Escalation-Based
Agent sends routine expediting reminders and generates reports autonomously. Flags and escalates schedule risks but does not change PO terms, approve scope changes, or negotiate with suppliers. Human procurement lead handles all commercial decisions.

**Example Interaction:**
> The ProcurementPulse agent detects that the gas compression package (PO value: $12.5M, 18-month lead time) has been in "In Fabrication" status for 10 months but the supplier's last expediting update was 3 weeks ago. Based on historical data, this supplier's similar packages have averaged a 6-week delay at this fabrication stage. The agent generates an alert: "SCHEDULE RISK — GAS COMPRESSION PKG (PKG-0142): No supplier update in 21 days. Historical pattern suggests 85% probability of 4-8 week delay based on comparable packages from this supplier. Impact: This is a critical-path item. A 6-week delay shifts mechanical completion from Q3 to Q4, potentially impacting first gas by 45 days ($67.5M revenue impact at projected commodity prices). Recommended actions: (1) Schedule supplier factory visit within 5 business days, (2) Request detailed fabrication progress report with photos, (3) Identify mitigation options — expedited shipping, parallel commissioning activities." The agent simultaneously creates a task for the category manager and flags the item in the weekly project review dashboard.

---

### Use Case 3: Strategic Sourcing & Category Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Strategic sourcing in energy involves managing $100M-$1B+ spend categories through multi-year sourcing cycles. A single sourcing event for drilling services might involve 8-12 bidders, 500-page technical and commercial bid packages, 3-month evaluation periods, complex scoring matrices (technical capability 40%, HSE 25%, commercial 25%, local content 10%), and cross-functional evaluation teams (engineering, operations, HSE, procurement, legal, finance). Category managers juggle 5-10 active sourcing events simultaneously while managing existing supplier relationships, negotiating frame agreements, and tracking market intelligence (commodity prices, manufacturing capacity, geopolitical risks). The process is largely manual — RFP documents created in Word, bid evaluations in Excel with vlookups that break, approval workflows via email, and contract negotiations tracked in people's heads. Knowledge walks out the door when a category manager leaves.

#### The Solution
monday.com as the strategic sourcing workflow platform. A Sourcing Events Board with items for each active event. Columns: Event Name, Category, Estimated Annual Value (numbers), Event Type (dropdown: New Source, Re-bid, Contract Extension, Emergency Source, Reverse Auction), Event Stage (status: Category Analysis-Purple, Specification-Blue, Market Engagement-Cyan, RFQ/ITB Issued-Teal, Bid Evaluation-Orange, Negotiation-Yellow, Award Recommendation-Light Green, Contract Execution-Green, Onboarding-Dark Green), Lead Category Manager (people), Evaluation Team (multi-people), Bidder Count (numbers), Target Award Date (date), Savings Target % (numbers), Achieved Savings % (numbers), Connected Supplier Board, and Files (RFP docs, bid summaries, evaluation matrices). Sub-items for each bidder with scoring columns. Automations manage stage-gate approvals — event can't progress from Bid Evaluation to Negotiation without evaluation committee sign-off.

#### The Outcome
50% reduction in sourcing cycle time (from 6 months to 3 months average). 3-5% additional savings capture through better market analysis and competitive tension. Complete institutional knowledge preservation — sourcing rationale, market intelligence, and negotiation history retained for future cycles. 100% audit-compliant sourcing documentation.

#### Discovery Questions
1. "Walk me through a recent major sourcing event — how long did it take from category analysis to contract execution, and where were the biggest time sinks?"
2. "When a category manager leaves your organization, how much institutional knowledge — supplier relationships, market intelligence, negotiation history — walks out the door with them?"
3. "How do you currently manage bid evaluations with cross-functional teams — is everyone scoring in the same spreadsheet, or are you consolidating separate evaluations?"
4. "How confident are you in your spend analytics — can you quickly answer 'How much did we spend on rotating equipment last year across all business units and projects?'"
5. "What's your process for tracking market intelligence — commodity price trends, supplier capacity constraints, geopolitical supply chain risks — and feeding that into sourcing decisions?"

#### Industry Context
Energy procurement follows established sourcing methodologies — many companies use the Kraljic Matrix to segment spend into categories (Leverage, Strategic, Bottleneck, Non-Critical). Frame agreements (also called blanket POs, master service agreements, or call-off contracts) are common for recurring spend — a 3-year frame agreement with an oilfield services company might cover 200+ individual call-offs. Reverse auctions are used for commodity categories (chemicals, MRO, logistics) but not for complex technical categories. The International Association of Contract & Commercial Management (IACCM, now WorldCC) provides contract benchmarking data. TCO (Total Cost of Ownership) analysis is critical — the cheapest bid for a compressor might have 3x the maintenance cost over its lifecycle. Energy companies increasingly use "should-cost" models built on raw material indices (LME metals, OPIS chemicals) to benchmark bids.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Strategic Sourcing & Category Management system for energy procurement. Board 1 — Sourcing Events: Event Name (text), Event ID (auto-number 'SRC-'), Category (dropdown: Drilling Services, Well Completions, Production Equipment, Pipeline Construction, MRO/Spare Parts, Chemicals, Marine/Offshore, EPC Services, IT & Telecom, Professional Services, Renewables, Environmental Services, Logistics & Transportation), Estimated Annual Value (numbers with $), Event Type (dropdown: New Source, Competitive Re-bid, Contract Renewal, Emergency Source, Reverse Auction, Single Source Justification), Event Stage (status: Category Analysis-Purple, Develop Specification-Blue, Market Engagement-Cyan, RFQ/ITB Issued-Teal, Bid Receipt-Blue, Technical Evaluation-Orange, Commercial Evaluation-Yellow, Negotiation-Light Orange, Award Recommendation-Light Green, Approval-Green, Contract Execution-Dark Green, Supplier Onboarding-Black), Lead Category Manager (people), Evaluation Team (people), Bidders Invited (numbers), Bids Received (numbers), Savings Target % (numbers), Achieved Savings % (numbers), Savings $ (formula), Target Award Date (date), Actual Award Date (date), RFP Document (file), Evaluation Matrix (file), Award Recommendation (file), Contract (file), Risk Level (status: Low-Green, Medium-Yellow, High-Red). Board 2 — Bidder Evaluation: Bidder Name (text), Connected Sourcing Event (connect), Technical Score (numbers /100), HSE Score (numbers /100), Commercial Score (numbers /100), Local Content Score (numbers /100), Total Weighted Score (formula), Rank (numbers), Bid Amount (numbers $), TCO Analysis (numbers $), Recommendation (status: Recommended-Green, Shortlisted-Yellow, Not Recommended-Red, Disqualified-Black), Evaluator Notes (long text). Automations: When Event Stage changes to Technical Evaluation, notify all Evaluation Team members; When all Bidder Evaluations have Total Weighted Score populated, notify Lead Category Manager; When Achieved Savings is below Savings Target by 50%+, flag to procurement director. Views: Sourcing pipeline Kanban by Event Stage, Calendar by Target Award Date, Dashboard with total spend under sourcing, savings pipeline, event cycle times, active events by category, and category manager workload."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SourceIQ Market Intelligence Agent
**Agent Purpose:** Provide real-time market intelligence and should-cost analysis to support strategic sourcing decisions.

**Triggers:**
- When a new sourcing event is created (generate category market briefing)
- When bids are received (compare against should-cost benchmarks)
- Weekly market monitoring for active categories under sourcing
- When commodity price indices change by >5% (alert relevant category managers)

**Actions:**
- Generate category market briefing: supplier landscape, recent contract awards (public data), commodity price trends, capacity utilization estimates, geopolitical risk factors
- Build should-cost models using raw material indices (LME, OPIS, steel indices) and labor rate databases
- Compare received bids against should-cost benchmarks and flag outliers (both high and suspiciously low)
- Identify demand aggregation opportunities across business units and projects
- Track supplier financial health changes (credit rating downgrades, earnings warnings)
- Generate quarterly category performance reports (spend trends, savings achieved, supplier performance)

**Data Required:**
- Commodity price indices (LME, OPIS, Platts, Argus)
- Public contract award databases (government procurement portals, industry press)
- Supplier financial data (D&B, credit agencies)
- Historical sourcing event data from monday.com
- Internal spend data by category

**Autonomy Level:** Fully Autonomous
Agent gathers and analyzes market data, generates reports and benchmarks without human intervention. Does not make sourcing decisions, negotiate with suppliers, or modify contract terms — all outputs are advisory for category managers.

**Example Interaction:**
> A category manager creates a new sourcing event for subsea flexible pipe (estimated $85M, 3-year frame agreement). The SourceIQ agent generates a market briefing within 2 hours: "Subsea Flexible Pipe Market Update — Q1 2026: Global installed base growing 8% YoY driven by deepwater developments in Guyana, Brazil Pre-Salt, and West Africa. Key suppliers: TechnipFMC (42% market share), NOV/Flexibles (28%), Baker Hughes/Flexibles (18%), Prysmian (12%). Current lead times: 14-20 months (up from 10-14 months in 2024). Steel and polymer input costs have increased 12% YoY per LME/OPIS indices. Should-cost estimate: $3,200-$3,800/meter for 6-inch dynamic riser application. Recommendation: Issue RFQ to all 4 qualified suppliers; market tightness favors early engagement. Risk: TechnipFMC capacity is 90%+ utilized — consider qualifying a fifth supplier (Shawflex/Kanfit emerging capabilities). Comparable recent awards: Petrobras Pre-Salt PLSV campaign — $92M (TechnipFMC, 2025); Aker BP Yggdrasil — $67M (NOV, 2025)."

---

### Use Case 4: Contract Lifecycle Management (CLM)

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
A large energy company manages 5,000-20,000 active contracts simultaneously — frame agreements, call-off orders, EPC contracts, joint venture agreements, transportation service agreements, PPAs, and commodity supply contracts. Each has different terms, renewal dates, performance guarantees, liquidated damages clauses, force majeure provisions, and compliance obligations. Currently, contracts live in a mix of SAP, SharePoint, network drives, and (horrifyingly) desk drawers. Procurement can't easily answer basic questions: "Which contracts are expiring in the next 6 months?", "What's our total committed spend with Halliburton across all business units?", or "Which contracts have change-of-control provisions that are triggered by our pending acquisition?" Missing a contract renewal deadline means either losing negotiating leverage (auto-renewal at existing terms) or scrambling for emergency sourcing. Missing a performance milestone means failing to enforce liquidated damages, leaving millions on the table.

#### The Solution
monday.com as a contract portfolio management layer. A Contracts Board with items for each contract. Columns: Contract Title, Contract Number, Supplier (connected to Supplier Master), Contract Type (dropdown: Frame Agreement/MSA, Call-Off/Work Order, EPC/EPCM, Joint Venture, Transportation Service Agreement, PPA/Offtake, Commodity Supply, Lease, License/IP, NDA), Value (numbers), Currency, Start Date, End Date, Auto-Renewal (checkbox), Renewal Notice Period Days (numbers), Renewal Notice Deadline (formula: End Date minus Notice Period), Status (status: Draft-Purple, Under Negotiation-Blue, Pending Approval-Orange, Active-Green, Expiring Soon-Yellow, Expired-Red, Terminated-Black), Key Terms Summary (long text), Performance Guarantees (text), LD Provisions (text), Force Majeure Clause Type (dropdown), Owner/Category Manager (people), Legal Contact (people), Files (contract PDFs). Sub-items for amendments and change orders. Automations: alert owner at Renewal Notice Deadline, flag contracts expiring within 180 days, trigger re-sourcing workflow 12 months before end date for strategic contracts.

#### The Outcome
Zero missed renewal deadlines — automated alerts eliminate the #1 source of value leakage. $2-5M annual savings from proactive re-negotiation of expiring contracts. 80% faster contract retrieval during audits, disputes, and M&A due diligence. Complete portfolio visibility for CPO — total committed spend, expiring value, supplier concentration risk.

#### Discovery Questions
1. "In the last year, how many contract renewal deadlines did your team miss — and what was the financial impact of those missed deadlines?"
2. "If your CEO asked right now, 'What's our total contractual exposure to Supplier X across all business units,' how quickly could you answer?"
3. "During your last M&A transaction, how long did it take to identify all contracts with change-of-control provisions?"
4. "How do you currently track performance guarantees and liquidated damages — are you consistently enforcing LD provisions when suppliers underperform?"
5. "What's your process for managing contract amendments — how many amendments does a typical frame agreement accumulate over its lifecycle, and where do those amendments live?"

#### Industry Context
Energy contracts are uniquely complex. EPC contracts (FIDIC-based or bespoke) can be 1,000+ pages with detailed milestone payment schedules, performance bonds (typically 10-15% of contract value), retention provisions, back-charge mechanisms, and intricate change order management processes. Frame agreements in oilfield services typically have 3-year terms with 2×1-year options, annual price adjustment mechanisms tied to indices (IHS-CERA UCCI for capital costs, BLS PPI for services), and performance-based incentives/penalties. Joint Operating Agreements (JOAs) govern multi-party operations in oil & gas — AIPN (Association of International Petroleum Negotiators) model forms are commonly used. Power Purchase Agreements (PPAs) for renewable energy involve complex pricing structures (fixed, escalating, indexed, merchant tail), curtailment provisions, and interconnection requirements. Understanding these contract archetypes helps SEs position monday.com as a management layer that complements legal/ERP systems rather than replacing them.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Contract Lifecycle Management board for energy procurement. Columns: Contract Title (text), Contract Number (text), Supplier (text), Contract Type (dropdown: Master Service Agreement/Frame, Work Order/Call-Off, EPC/EPCM, Joint Operating Agreement, Transportation Service Agreement, Power Purchase Agreement, Commodity Supply Contract, Equipment Lease, Technology License, NDA/Confidentiality, Consulting Agreement), Business Unit (dropdown: Upstream, Midstream, Downstream, Renewables, Corporate, All), Category (dropdown: Drilling, Production, Pipeline, EPC, MRO, Chemicals, Marine, IT, Professional Services, Renewables, Logistics), Contract Value (numbers with $), Annual Value (numbers with $), Currency (dropdown: USD, EUR, GBP, BRL, NOK, AED, NGN), Start Date (date), End Date (date), Auto-Renew (status: Yes-Yellow, No-Gray), Renewal Notice Days (numbers), Renewal Notice Deadline (formula), Renewal Alert Status (status: Not Due-Gray, Alert Sent-Yellow, Action Required-Orange, Renewed-Green, Re-Sourcing-Blue), Status (status: Draft-Purple, Negotiation-Blue, Legal Review-Cyan, Pending Signatures-Orange, Active-Green, Expiring <180 Days-Yellow, Expiring <90 Days-Orange, Expired-Red, Terminated-Black), Owner/Category Manager (people), Legal Contact (people), Key Terms (long text), Performance Bond Value (numbers with $), LD Provisions (text), Price Adjustment Mechanism (dropdown: Fixed, CPI Indexed, UCCI Indexed, PPI Indexed, Commodity Linked, Annual Negotiation), Force Majeure Type (dropdown: Narrow/Named Perils, Broad/All Events, Market Standard), Contract Document (file), Amendments (file), Change Orders (file). Automations: When today equals Renewal Notice Deadline, notify Owner and set Renewal Alert to Action Required; 12 months before End Date for contracts >$5M, create re-sourcing task; When Status is Active and End Date has passed, change to Expired and alert Owner. Views: Main Table, Calendar by End Date, Kanban by Status, Dashboard with total portfolio value, contracts expiring next 6 months (by value), supplier concentration analysis, contracts by type, and renewal action items."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ContractIQ Portfolio Intelligence Agent
**Agent Purpose:** Proactively manage the contract portfolio — flagging risks, identifying optimization opportunities, and ensuring no value leakage from missed deadlines or unenforced terms.

**Triggers:**
- Daily scan for upcoming renewal deadlines and contract expirations
- When a supplier's financial health score changes significantly
- When commodity price index changes affect price adjustment mechanisms
- When a new regulation or sanctions update impacts existing contracts
- Monthly portfolio health review

**Actions:**
- Generate 90-day contract action calendar with prioritized renewal/re-sourcing recommendations
- Calculate price adjustment amounts based on index movements and notify category managers
- Flag contracts where LDs should be enforced based on supplier performance data from project boards
- Identify supplier concentration risk (single supplier >30% of category spend)
- Generate M&A impact analysis — scan all contracts for change-of-control, assignment, and consent provisions
- Produce annual contract portfolio report with savings opportunities

**Data Required:**
- Contract board data (all columns and files)
- Supplier performance data from project/expediting boards
- Commodity price indices for price adjustment calculations
- Supplier financial health monitoring data
- Regulatory/sanctions update feeds

**Autonomy Level:** Human-in-the-Loop
Agent generates alerts, analysis, and recommendations but never modifies contract terms, sends communications to suppliers, or makes renewal/termination decisions. All commercial actions require category manager approval.

**Example Interaction:**
> The ContractIQ agent's monthly portfolio review identifies an optimization opportunity: "CONTRACT OPTIMIZATION ALERT: You have 3 separate frame agreements with Baker Hughes across Upstream ($45M/yr), Midstream ($12M/yr), and Downstream ($8M/yr) business units — total $65M/yr. These contracts expire within 6 months of each other (Q2-Q3 2027). Recommendation: Consolidate into a single enterprise-wide frame agreement. Based on comparable consolidated awards in the sector, estimated savings from volume leverage: 8-12% ($5.2-$7.8M/yr). Action: Initiate consolidated sourcing event 18 months before earliest expiration (target: Q4 2025 — OVERDUE by 4 months). Risk: Supplier concentration increases if consolidated. Mitigation: Dual-source critical categories within the agreement." The agent creates a draft sourcing event and assigns it to the relevant category manager for review.

---

### Use Case 5: Sustainable Procurement & Scope 3 Emissions Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
SEC climate disclosure rules, the EU's CSRD, and investor pressure are forcing energy companies to measure and report Scope 3 emissions — the greenhouse gas emissions from their supply chain, which often represent 70-90% of a petroleum company's total emissions footprint. Procurement is ground zero for this challenge. Category managers must now collect emissions data from thousands of suppliers, most of whom have never measured their own carbon footprint. Simultaneously, companies are setting "sustainable procurement" targets — percentage of spend with suppliers who have SBTi-approved targets, percentage of renewable content in purchased materials, circular economy metrics, and supply chain human rights due diligence (EU CSDDD). Currently, sustainability teams send annual surveys to suppliers via email, get 20-30% response rates, manually enter data into spreadsheets, and produce reports 6 months out of date. Procurement has no real-time visibility into the carbon intensity of their supply chain decisions.

#### The Solution
monday.com as the sustainable procurement management platform. A Supplier Sustainability Board connected to the Supplier Master, with items for each strategic/Tier 1 supplier. Columns: Supplier Name, Category, Annual Spend, GHG Emissions Reported (numbers — tCO2e), Emissions Intensity (formula: emissions/spend), SBTi Status (status: Committed-Blue, Target Set-Green, No Commitment-Red), CDP Score (dropdown: A, A-, B, B-, C, C-, D, D-, F, Not Disclosed), Renewable Energy % (numbers), Sustainability Survey Status (status: Sent-Blue, Reminder Sent-Yellow, Received-Green, Overdue-Red), Survey Response (file), Sustainability Action Plan (file), Last Updated (date). A Procurement Decisions Board integrating carbon data — when evaluating bids, include a "Carbon Cost" column showing estimated Scope 3 impact. Dashboard showing total supply chain emissions by category, progress toward sustainable procurement targets, and supplier engagement rates.

#### The Outcome
Achieve 80%+ supplier sustainability data coverage (up from 20-30%). Real-time Scope 3 emissions estimates to support SEC/CSRD reporting. Procurement decisions incorporate carbon cost — enabling 10-15% reduction in supply chain emissions intensity. Complete audit trail for ESG assurance and regulatory compliance. Procurement team positioned as strategic partner to sustainability function.

#### Discovery Questions
1. "What's your current approach to collecting Scope 3 emissions data from your supply chain — and what response rate are you getting from suppliers?"
2. "Under the SEC climate disclosure rules, how are you planning to report Scope 3 emissions — and which categories are most material for your business?"
3. "Do your procurement evaluation criteria currently include any sustainability metrics, or is it still primarily technical capability, HSE, and price?"
4. "How are you tracking progress toward any sustainable procurement targets — percentage of suppliers with SBTi targets, percentage of spend with low-carbon suppliers?"
5. "Has any customer, investor, or regulator asked you specifically about your supply chain decarbonization strategy — and could you answer today?"

#### Industry Context
Scope 3 emissions are categorized into 15 categories by the GHG Protocol. For upstream oil & gas, the most material Scope 3 categories are typically Category 11 (Use of Sold Products — burning of produced oil/gas by end customers, representing ~80% of total emissions) and Category 1 (Purchased Goods & Services — supply chain emissions). For utilities, Category 3 (Fuel- and Energy-Related Activities) is critical. The SEC rules require disclosure of Scope 3 emissions for large accelerated filers if material or if the company has set a Scope 3 target. The EU CSRD and European Sustainability Reporting Standards (ESRS) require Scope 3 disclosure for all in-scope companies. CDP (formerly Carbon Disclosure Project) scores suppliers on climate disclosure quality — energy companies increasingly require key suppliers to disclose through CDP. SBTi (Science Based Targets initiative) provides the framework for credible emissions reduction targets — the SBTi Oil & Gas sector guidance has specific requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Sustainable Procurement & Scope 3 Tracking system for an energy company. Board 1 — Supplier Sustainability Profiles: Supplier Name (text), Connected to Supplier Master (connect), Category (dropdown: same as Supplier Master), Annual Spend (numbers $), Tier (dropdown: Tier 1 Strategic, Tier 2 Significant, Tier 3 Standard), GHG Emissions Reported tCO2e (numbers), Emissions Year (dropdown: 2024, 2025, 2026), Emissions Intensity (formula: emissions/spend * 1000000 = tCO2e per $M spend), SBTi Status (status: Committed-Blue, Near-Term Target Set-Green, Net-Zero Target Set-Dark Green, No Commitment-Red, Not Applicable-Gray), CDP Score (dropdown: A, A-, B, B-, C, C-, D, D-, F, Not Disclosed), Renewable Energy % of Operations (numbers), ISO 14001 Certified (status: Yes-Green, No-Red, In Progress-Yellow), Sustainability Survey (status: Not Sent-Gray, Sent-Blue, Reminder Sent-Yellow, Received-Green, Overdue-Red), Survey Response (file), Corrective Action Plan (file), Last Updated (date), Next Review (date). Board 2 — Scope 3 Emissions by Category: GHG Protocol Category (dropdown: Cat 1 Purchased Goods, Cat 2 Capital Goods, Cat 3 Fuel & Energy Activities, Cat 4 Upstream Transportation, Cat 5 Waste, Cat 6 Business Travel, Cat 7 Employee Commuting, Cat 11 Use of Sold Products, Cat 12 End-of-Life), Estimated Emissions tCO2e (numbers), Data Quality Score (status: Measured-Green, Calculated-Yellow, Estimated-Orange, Screened-Red), Methodology (text), Reporting Period (text), Owner (people). Automations: When Sustainability Survey is Sent and 30 days pass without response, set to Reminder Sent and notify supplier contact; When SBTi Status is No Commitment and Annual Spend exceeds $5M, flag for engagement; When Emissions Intensity exceeds category average by 50%, create corrective action item. Views: Main Table, Dashboard with total Scope 3 emissions by category, supplier SBTi commitment rate, CDP score distribution, emissions intensity by procurement category, survey response rate, and progress toward sustainable procurement KPIs."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CarbonLens Supply Chain Emissions Agent
**Agent Purpose:** Estimate, track, and reduce Scope 3 emissions across the procurement portfolio using supplier data, spend analytics, and emission factor databases.

**Triggers:**
- When a new PO is created (estimate Scope 3 impact)
- When supplier sustainability survey data is received (update emissions profiles)
- Monthly recalculation of portfolio-level Scope 3 estimates
- When emission factor databases are updated (DEFRA, EPA, ecoinvent)
- When a sourcing event enters bid evaluation (add carbon cost comparison)

**Actions:**
- Estimate Scope 3 emissions for individual POs using spend-based or activity-based emission factors
- Update supplier emissions profiles when new data is received
- Generate carbon cost comparisons for sourcing bid evaluations (e.g., "Bidder A's proposal generates estimated 2,400 tCO2e vs. Bidder B's 1,800 tCO2e — $72K shadow carbon cost difference at $40/tCO2e internal price")
- Identify top-20 suppliers by emissions contribution and generate engagement priority list
- Produce quarterly Scope 3 emissions report aligned with GHG Protocol methodology
- Flag data quality issues and recommend measurement improvements

**Data Required:**
- Spend data by supplier and category
- Emission factor databases (DEFRA, EPA, ecoinvent, EXIOBASE)
- Supplier-reported emissions data from sustainability surveys
- Internal carbon price (shadow carbon price for decision-making)
- GHG Protocol Scope 3 calculation methodology guidance

**Autonomy Level:** Fully Autonomous
Agent calculates estimates and generates reports without human intervention. Emissions estimates are advisory — they don't block procurement decisions but are surfaced alongside commercial and technical evaluations. Human sustainability team validates methodology and reviews quarterly reports before publication.

**Example Interaction:**
> During a competitive bid evaluation for chemical catalysts ($28M/yr spend), the CarbonLens agent adds a sustainability column to the evaluation: "Scope 3 Emissions Comparison — Bidder A (BASF): 4,200 tCO2e estimated (SBTi committed, CDP score A-, provided facility-specific data, emissions intensity: 150 tCO2e/$M). Bidder B (Regional Supplier): 6,800 tCO2e estimated (no SBTi, no CDP disclosure, estimate based on industry-average emission factors, confidence: Low). Bidder C (Johnson Matthey): 3,100 tCO2e estimated (SBTi net-zero target, CDP score A, ISO 14001 certified, 68% renewable energy, emissions intensity: 111 tCO2e/$M). Shadow carbon cost differential: Bidder C saves $148K/yr vs. Bidder B at $40/tCO2e internal carbon price. Note: Bidder B's estimate is low-confidence; recommend requiring facility-level data before final award." The category manager now has environmental impact data alongside technical and commercial scores.

---

### Use Case 6: MRO (Maintenance, Repair & Operations) Procurement Optimization

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
MRO procurement in energy is a $500M-$2B+ annual spend category characterized by high transaction volume (50,000-200,000+ POs/year), low individual PO values ($500-$50,000), extreme item diversity (500,000+ SKUs across catalogs), and critical operational impact (a $200 bearing delivered 2 days late can shut down a $10M/day production facility). Current state: operations technicians requisition parts via SAP, but emergency/unplanned maintenance drives 30-40% of MRO purchases outside normal procurement channels (p-card purchases, verbal orders, field purchases at local distributors). This "maverick spend" creates duplicate purchasing, inflated pricing, and zero visibility. Inventory management is equally chaotic — warehouses at remote facilities are either overstocked with obsolete parts or missing critical spares when a compressor fails at 2 AM.

#### The Solution
monday.com as an MRO procurement visibility and optimization layer. While transactional PO processing stays in SAP/Oracle, monday.com manages the strategic and exception-handling workflows. An MRO Optimization Board tracking: Category Spend Analysis (items per major MRO sub-category), Maverick Spend Tracking (purchases outside frame agreements), Supplier Consolidation Opportunities, Inventory Optimization Projects, and Emergency Purchase Authorizations. A Critical Spares Board tracking high-value/long-lead-time spares inventory across all sites, with automated reorder triggers. Dashboards showing MRO spend trends, maverick spend percentage, inventory health by site, and emergency purchase frequency.

#### The Outcome
15-25% reduction in MRO spend through supplier consolidation and maverick spend elimination. 50% reduction in emergency procurement situations through proactive critical spares management. $5-10M annual savings for a mid-large energy company. 90% reduction in procurement team time spent on tactical MRO transactions.

#### Discovery Questions
1. "What percentage of your MRO purchases happen outside your standard procurement process — p-card purchases, field buys, verbal orders — and do you have visibility into that spend?"
2. "How do you manage critical spare parts inventory across your facilities — do you know which spares you have, where they are, and when they need to be reordered?"
3. "What's the financial impact when an unplanned maintenance event requires an emergency spare part that's not in your warehouse — expedited shipping costs, production downtime?"
4. "How many MRO suppliers do you have, and have you assessed the opportunity to consolidate to fewer, strategically managed relationships?"
5. "Can you tell me right now how much you spent on MRO in the last 12 months, broken down by sub-category and site?"

#### Industry Context
MRO in energy is uniquely challenging because of the remote and hazardous operating environments. Offshore platforms can only receive deliveries via supply vessel or helicopter — logistics costs for a single emergency spare part delivery can exceed $50,000. Pipeline compressor stations in remote locations may be 4-6 hours from the nearest distributor. Refinery turnarounds (planned maintenance shutdowns every 3-5 years) create massive, predictable MRO demand spikes — a single turnaround can consume $50-100M in MRO materials over 4-6 weeks. CMMS (Computerized Maintenance Management Systems) like SAP PM, Maximo, or Hexagon EAM drive maintenance work orders that trigger MRO requisitions — integration between CMMS and procurement is critical. Bill of Materials (BOM) management for complex rotating equipment (e.g., GE Frame 7 gas turbine — 10,000+ parts) is a perpetual challenge.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an MRO Procurement Optimization system for an energy company. Board 1 — MRO Category Spend Dashboard: Category (dropdown: Bearings & Seals, Valves & Actuators, Electrical Components, Instrumentation, Filters & Strainers, Gaskets & Packing, Pipe Fittings & Flanges, Safety Equipment/PPE, Lubricants & Chemicals, Rotating Equipment Parts, HVAC, General Industrial), Annual Spend (numbers $), Number of Suppliers (numbers), Frame Agreement Coverage % (numbers), Maverick Spend % (numbers), Target Maverick % (numbers), Consolidation Opportunity (status: Identified-Blue, In Progress-Yellow, Complete-Green, None-Gray), Category Manager (people), Notes (long text). Board 2 — Critical Spares Inventory: Part Name (text), Part Number (text), Equipment (text), Facility/Site (text), Current Stock (numbers), Minimum Stock Level (numbers), Reorder Point (numbers), Reorder Quantity (numbers), Unit Cost (numbers $), Total Inventory Value (formula), Lead Time Weeks (numbers), Preferred Supplier (text), Stock Status (status: Adequate-Green, Below Reorder Point-Yellow, Critical Low-Red, Out of Stock-Black, Overstocked-Blue), Last Used Date (date), Last Ordered Date (date), Shelf Life Expiry (date). Board 3 — Emergency Purchase Authorizations: Request Description (text), Facility (text), Equipment Affected (text), Production Impact $/day (numbers), Requested By (people), Approved By (people), Status (status: Pending-Yellow, Approved-Green, Denied-Red, Delivered-Dark Green), Estimated Cost (numbers $), Actual Cost (numbers $), Expediting Premium (numbers $), Root Cause (dropdown: Inadequate Spare Stocking, Unexpected Failure, Supplier Default, Turnaround Scope Change, Other), Corrective Action (long text). Automations: When Current Stock falls below Reorder Point, create purchase requisition and notify buyer; When Emergency Purchase is approved and Estimated Cost exceeds $25K, notify procurement director; Monthly aggregate Emergency Purchase data and flag categories with 3+ emergencies. Views: Category spend table, Critical spares Kanban by Stock Status, Emergency log filtered by month, Dashboard with total MRO spend trend, maverick spend %, emergency purchase frequency and cost, inventory value by site, and categories with consolidation opportunities."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SpareGuard Predictive Inventory Agent
**Agent Purpose:** Predict critical spare parts demand, optimize inventory levels, and prevent production-impacting stockouts.

**Triggers:**
- When Current Stock reaches Reorder Point on any critical spare
- When maintenance work order is created in CMMS (integration) requiring specific parts
- Monthly demand forecasting cycle
- When a planned turnaround schedule is published (anticipate MRO demand spike)
- When a supplier advises of lead time increase or discontinuation

**Actions:**
- Generate automated purchase requisitions for reorder-point items with preferred supplier and optimal quantity
- Predict spare parts demand based on equipment runtime hours, maintenance history, and failure probability models
- Identify overstocked items (inventory value > 2x annual usage) for redistribution across sites or disposal
- Generate turnaround MRO material lists by cross-referencing equipment BOMs with planned maintenance scope
- Alert when a critical spare has no alternative supplier and lead time exceeds 12 weeks (single-point-of-failure risk)
- Produce monthly inventory health report with recommendations

**Data Required:**
- Critical spares board data (all columns)
- Equipment runtime hours and maintenance history (CMMS integration)
- Historical consumption patterns by part/site
- Turnaround schedules and scope documents
- Supplier lead time and availability data
- Equipment BOMs (Bills of Materials)

**Autonomy Level:** Escalation-Based
Agent generates purchase requisitions automatically for routine reorders within pre-approved parameters (value < $10K, approved supplier, standard lead time). Escalates to buyer for non-routine situations: new suppliers, values > $10K, expedited orders, or discontinued parts requiring engineering alternatives.

**Example Interaction:**
> The SpareGuard agent detects that the critical bearing set for the main gas compressor at the Delaware Basin processing plant has dropped to 1 unit remaining (minimum stock: 2, reorder point: 2). Simultaneously, the CMMS integration shows a preventive maintenance work order scheduled for this compressor in 6 weeks requiring this exact bearing set. The agent acts: "AUTO-REORDER GENERATED: Bearing set P/N GE-7FA-BRG-3102, Qty: 3 (2 replacement + 1 PM requirement). Preferred supplier: SKF Industrial, Lead time: 4 weeks, Unit cost: $8,400, Total: $25,200. NOTE: Total exceeds $10K auto-approval threshold — requires buyer approval. Context: PM work order #WO-82947 scheduled in 6 weeks requires 1 unit. Current stock (1) is insufficient for both PM and emergency buffer. If order is placed today, delivery in 4 weeks provides 2-week buffer before PM. RISK: If this compressor experiences unplanned failure before PM, production impact is $2.1M/day (facility processes 180 MMcf/d). Recommend buyer approval within 48 hours."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| AVL | Approved Vendor List — master list of qualified suppliers authorized for procurement |
| CAPEX | Capital Expenditure — spending on major projects and assets (drilling campaigns, plant construction) |
| OPEX | Operating Expenditure — recurring spending on operations and maintenance |
| MRO | Maintenance, Repair & Operations — consumable and spare parts for facility maintenance |
| EPC/EPCM | Engineering, Procurement & Construction / Engineering, Procurement & Construction Management |
| RFQ/ITB | Request for Quotation / Invitation to Bid — formal solicitation documents |
| PO | Purchase Order — formal order document committing to buy from a supplier |
| Frame Agreement/MSA | Master Service Agreement — long-term contract establishing terms for recurring purchases |
| Call-Off | Individual order placed against a frame agreement |
| TCO | Total Cost of Ownership — full lifecycle cost including purchase price, maintenance, operation, and disposal |
| TRIR | Total Recordable Incident Rate — safety metric (incidents per 200,000 work hours) |
| EMR | Experience Modification Rate — workers' compensation insurance metric (1.0 = industry average) |
| FCPA | Foreign Corrupt Practices Act — US law prohibiting bribery of foreign officials |
| OFAC | Office of Foreign Assets Control — administers US sanctions programs |
| SDN | Specially Designated Nationals and Blocked Persons List — OFAC sanctions list |
| FPSO | Floating Production, Storage & Offloading — vessel-based offshore production system |
| PPA | Power Purchase Agreement — contract for buying electricity from a generator |
| CMMS | Computerized Maintenance Management System (SAP PM, Maximo, Hexagon EAM) |
| BOM | Bill of Materials — list of all parts/components in a piece of equipment |
| P&ID | Piping & Instrumentation Diagram — standard technical drawing in process plants |
| LOTO | Lockout/Tagout — safety procedure for equipment isolation during maintenance |
| Scope 3 | GHG Protocol Category 3 emissions — indirect emissions from the value chain (supply chain + end use) |
| SBTi | Science Based Targets initiative — framework for credible corporate emission reduction targets |
| CDP | Carbon Disclosure Project — global disclosure system for environmental impact |
| UCCI | IHS-CERA Upstream Capital Costs Index — benchmark for oil & gas capital project costs |
| Kraljic Matrix | Strategic sourcing framework categorizing spend into Leverage, Strategic, Bottleneck, Non-Critical |
| NCDMB | Nigerian Content Development and Monitoring Board — enforces local content requirements |
| ANP | Agência Nacional do Petróleo (Brazil) — regulates local content in oil & gas |
| GHS | Globally Harmonized System — international chemical classification and labeling standard |
| ISNetworld | Industry-standard supplier prequalification and safety management platform |
| Turnaround | Planned maintenance shutdown of a refinery or plant — typically every 3-5 years, lasting 4-8 weeks |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Procurement Officer (CPO) | Strategy, policy, category management oversight, organizational direction | Decision-maker — ultimate authority on procurement tools and processes |
| VP Supply Chain | End-to-end supply chain including procurement, logistics, warehousing, materials management | Decision-maker — may be CPO's peer or superior |
| Category Manager | Strategic sourcing for specific spend categories, supplier relationship management, market intelligence | Influencer/User — daily operator who champions or blocks new tools |
| Procurement Director (CAPEX) | Manages procurement for major capital projects | Decision-maker for project procurement workflows |
| Procurement Director (OPEX/MRO) | Manages recurring operations procurement and MRO | Decision-maker for operational procurement workflows |
| Buyer/Purchasing Agent | Tactical execution — PO processing, expediting, supplier communication | User — high-volume daily user of procurement systems |
| Contracts Manager | Contract drafting, negotiation, lifecycle management | Influencer — owns contract workflows |
| Supplier Quality Manager | Supplier qualification, audits, performance management | Influencer — owns qualification workflows |
| Chief Sustainability Officer | ESG strategy, Scope 3 targets, sustainable procurement mandates | Influencer — increasingly drives procurement requirements |
| CFO | Budget oversight, financial controls, compliance | Decision-maker — budget authority, compliance mandate |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations/Production | Primary internal customer — generates requisitions, provides specifications, receives delivered materials | Cross-sell: Operations management, production optimization, turnaround planning |
| Engineering | Develops technical specifications for capital procurement, approves materials, manages MOC (Management of Change) | Cross-sell: Engineering project management, document control, MOC workflows |
| HSE | Sets supplier safety requirements, conducts supplier audits, reviews contractor performance | Cross-sell: HSE incident management, contractor safety management, audit tracking |
| Finance | Budget management, AP (accounts payable), financial controls, audit | Cross-sell: Finance operations, AP automation, budget management |
| Legal | Contract drafting and negotiation, compliance (FCPA, sanctions), dispute resolution | Cross-sell: Legal matter management, compliance tracking |
| Sustainability | Scope 3 data requirements, sustainable procurement targets, ESG reporting | Cross-sell: ESG data management, sustainability reporting workflows |
| IT | System integration (SAP, Oracle), data management, cybersecurity for supply chain | Cross-sell: IT project management, vendor management, cybersecurity compliance |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| SAP Ariba / SAP S/4HANA Procurement | End-to-end procure-to-pay, dominant in large energy companies | monday.com won't displace SAP for transactional P2P — position as the strategic/collaborative layer that makes SAP data actionable for category management, sourcing events, and compliance workflows |
| Coupa | Cloud procurement platform — BSM (Business Spend Management) | Similar to SAP — position monday.com for workflows that Coupa doesn't handle well: cross-functional collaboration, project procurement tracking, supplier qualification lifecycle |
| Oracle Procurement Cloud | ERP-integrated procurement for Oracle shops | Same positioning as SAP — monday.com fills the collaboration and visibility gaps |
| Jaggaer (formerly SciQuest) | Source-to-pay, strong in energy sector | Complex and expensive — monday.com offers faster time-to-value for specific workflow needs |
| ISNetworld / Avetta / Veriforce | Supplier prequalification databases | Not competitors — they're data sources. monday.com builds the workflow around their data (qualification lifecycle, approval routing, performance tracking) |
| Excel / SharePoint | Default tools for everything SAP doesn't cover | Easiest displacement — show the chaos of managing capital project procurement in Excel vs. monday.com visual boards with automations |
| Smartsheet | Spreadsheet-like project management | Common in energy — position monday.com's superior automation, integration, and visualization capabilities |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have SAP Ariba for procurement" | "SAP Ariba is excellent for transactional procure-to-pay — PO processing, invoice matching, catalog buying. But your strategic workflows — sourcing events, bid evaluations, supplier qualification lifecycle, capital project procurement tracking, contract renewal management — those are happening in Excel and email despite having Ariba. monday.com becomes the strategic collaboration layer that makes your SAP investment more valuable, not redundant." |
| "Procurement data is too sensitive for another cloud platform" | "Agreed — procurement data requires serious protection. monday.com is SOC 2 Type II, ISO 27001, and supports granular permissions so your category managers only see their categories. For FCPA-sensitive supplier due diligence, you control access at the column level. We also support data residency and SSO/SAML integration with your enterprise identity provider." |
| "We need a 'real' procurement system, not a project management tool" | "You're right that monday.com isn't a procure-to-pay system — and it shouldn't be. Your SAP/Oracle handles transactions. But ask your category managers where they actually spend their day: it's not in SAP. It's in Excel trackers for sourcing events, email chains for bid evaluations, and SharePoint for supplier documents. monday.com replaces that shadow IT, not your ERP." |
| "Our procurement process is too complex for a flexible tool" | "Complexity is exactly why you need monday.com. A rigid system forces you to work around it — which is why you end up in Excel. monday.com lets you build workflows that match YOUR process — whether that's a 12-stage sourcing event with cross-functional evaluation committees or a 3-step emergency purchase authorization. And when your process evolves, the tool evolves with it." |
| "We can't justify budget for a procurement tool right now" | "Let me reframe this. A single missed contract renewal deadline can cost $500K-$2M in lost negotiating leverage. A single capital project procurement delay costs $1-5M per day. A single FCPA violation averages $30M+ in fines. monday.com isn't a cost — it's risk mitigation with a procurement efficiency ROI on top. Most of our energy procurement customers achieve payback in under 6 months." |

## Proof Points
*(To be populated with customer references)*
- [Energy sector procurement team using monday.com for supplier management]
- [Capital project procurement tracking case study]
- [Contract lifecycle management implementation reference]
- [Sustainable procurement / Scope 3 tracking example]
- [MRO optimization case study in energy or heavy industry]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
