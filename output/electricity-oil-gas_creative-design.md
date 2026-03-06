# Electricity, Oil & Gas × Creative & Design Playbook

## Overview

Creative and Design teams within Electricity, Oil & Gas (E, O&G) companies operate in a uniquely regulated, safety-critical, and geographically distributed environment. Unlike consumer-facing creative departments, energy-sector creative teams focus heavily on technical illustration (pipeline schematics, refinery process diagrams, safety signage), regulatory compliance documentation (EPA, OSHA, FERC visual standards), investor relations materials, internal communications for field operations, and public-facing campaigns around sustainability, community impact, and energy transition narratives. These teams are often small — typically 5–20 people embedded within Corporate Communications, HSE (Health, Safety & Environment), or Marketing — yet they serve an outsized mandate spanning upstream exploration, midstream transportation, downstream refining, and renewable energy divisions.

The organizational structure typically places Creative & Design under a VP of Corporate Communications or Chief Marketing Officer, with dotted-line reporting to HSE for safety-related visual assets. In large integrated energy companies (ExxonMobil, Shell, TotalEnergies scale), there may be dedicated in-house agencies. In mid-market E&P (exploration & production) companies or utilities, the team is lean and relies heavily on external agencies and freelancers. The regulatory context is intense: NERC CIP standards for utilities, API standards for oil & gas, and increasingly ESG (Environmental, Social & Governance) reporting frameworks like SASB and TCFD require pixel-perfect compliance in visual communications.

The cost pressure is real. Energy companies are navigating the dual challenge of maintaining legacy fossil fuel operations while investing in energy transition (renewables, hydrogen, carbon capture). Creative teams are asked to do more with less — rebranding for energy transition, producing investor-grade ESG reports, creating multilingual safety training materials for global field operations, and managing digital asset libraries spanning decades of technical documentation. The opportunity for monday.com is to become the operational backbone that connects creative workflows to the broader enterprise, replacing fragmented tool chains of SharePoint, email-based approvals, and ad-hoc agency management.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Small creative teams serve massive, distributed energy operations across multiple business units, geographies, and languages — they need to multiply output without headcount |
| 2 | Consolidate Tech Stack with AI | Medium-High | Creative teams typically juggle 6-10 tools (Adobe Creative Cloud, SharePoint, email, DAM systems, proofing tools, agency portals) with no single source of truth |
| 3 | Replace or Radically Augment Headcount | Medium | AI-generated first drafts of safety signage, ESG report layouts, social media content, and technical documentation can reduce dependency on expensive specialized designers |

## Prioritized Use Cases

---

### Use Case 1: Regulatory & Safety Visual Asset Production Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Energy companies must produce thousands of safety-critical visual assets annually — OSHA-compliant signage, GHS (Globally Harmonized System) hazard labels, pipeline marker specifications, emergency response diagrams, and lockout/tagout (LOTO) procedure illustrations. Each asset must comply with strict regulatory standards (ANSI Z535, API RP 2003, NFPA 704), be translated into multiple languages for global field operations, and go through HSE review. Currently, requests come via email, approvals are manual, version control is nonexistent (designers store files locally or on unstructured SharePoint sites), and regulatory audits trigger panic-mode scrambles to locate current-version assets. A single non-compliant safety sign at a refinery can result in OSHA citations starting at $16,131 per violation.

#### The Solution
monday.com Work Management as the intake-to-delivery pipeline for all safety and regulatory visual assets. A dedicated board with columns for Asset Type (dropdown: signage, label, diagram, procedure illustration), Regulatory Standard (dropdown: OSHA, ANSI, GHS, API, NFPA), Language Requirements (multi-select: English, Spanish, French, Portuguese, Arabic, Mandarin), Facility/Site (connected board to master facility list), HSE Reviewer (people column), Compliance Status (status: Draft → HSE Review → Legal Review → Approved → Deployed), and Deployment Date (date). Automations route requests by regulatory standard to the appropriate designer and HSE reviewer. File columns with version tracking replace SharePoint chaos. Dashboard views show compliance gaps by facility.

#### The Outcome
60% reduction in asset production cycle time (from 3 weeks to 5 business days). 100% audit-readiness with centralized, version-controlled asset repository. Elimination of $200K+ annual risk exposure from non-compliant signage. 40% reduction in translation costs through templated multilingual workflows.

#### Discovery Questions
1. "How do field sites currently request new safety signage or updates to existing visual assets — is there a formal intake process or does it come through email and phone calls?"
2. "When OSHA or a state regulator conducts an inspection, how quickly can you produce documentation showing the current version and approval history of every safety sign at that facility?"
3. "How many languages do your safety materials need to support, and what's your current process for managing translations and ensuring regulatory compliance across all language versions?"
4. "What happened the last time a regulatory audit found a non-compliant or outdated safety asset in the field?"
5. "How do you currently track which regulatory standards (ANSI Z535, GHS, etc.) apply to each asset, and how do you ensure updates when standards are revised?"

#### Industry Context
OSHA's Hazard Communication Standard (HCS 2012, aligned with GHS Rev 3) requires specific label elements including signal words, hazard statements, pictograms, and precautionary statements. ANSI Z535 governs safety sign design including colors, formats, and symbol usage. In oil & gas specifically, API RP 2003 covers static electricity hazards, and NFPA 704 (the "fire diamond") is mandatory at facilities storing hazardous materials. Pipeline markers must comply with API 1109 and 49 CFR 195.410. Energy companies operating internationally must also comply with EU CLP regulation, Australia's WHS, and regional standards. The creative team must be expert in all of these — or have systems that enforce compliance automatically.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Safety & Regulatory Asset Production board for an energy company. Columns: Request Title (text), Asset Type (dropdown: Safety Sign, Hazard Label, Pipeline Marker, Emergency Diagram, LOTO Illustration, Process Schematic), Regulatory Standard (dropdown: OSHA/ANSI Z535, GHS/CLP, API, NFPA 704, DOT/49 CFR, ISO 7010), Priority (status: Urgent-Red, High-Orange, Standard-Blue, Low-Gray), Language Requirements (dropdown: English, Spanish, French, Portuguese, Arabic, Mandarin, German), Facility/Site (text), Requesting Department (dropdown: HSE, Operations, Maintenance, Engineering, Compliance), Assigned Designer (people), HSE Reviewer (people), Legal Reviewer (people), Status (status: New Request-Purple, In Design-Blue, HSE Review-Orange, Legal Review-Yellow, Approved-Green, Deployed to Field-Dark Green, Revision Needed-Red), Regulatory Compliance Check (status: Pending-Gray, Compliant-Green, Non-Compliant-Red), Source Files (file), Final Approved Asset (file), Translation Status (status: Not Required-Gray, In Translation-Blue, Translated-Green), Target Deploy Date (date), Actual Deploy Date (date). Automations: When Status is New Request and Regulatory Standard is OSHA/ANSI Z535, assign to specific designer and notify HSE Reviewer; When Status changes to Approved, notify Requesting Department and update Regulatory Compliance Check to Compliant; When Target Deploy Date is within 3 days and Status is not Approved, notify team lead. Views: Main Table, Kanban by Status, Calendar by Target Deploy Date, Dashboard showing assets by Regulatory Standard, Compliance status breakdown, overdue items, and monthly throughput."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ComplianceGuard Visual QA Agent
**Agent Purpose:** Automatically validate safety and regulatory visual assets against applicable standards before HSE review.

**Triggers:**
- When a designer moves an asset to "HSE Review" status
- When a new regulatory standard revision is published (manual trigger or scheduled check)
- When an existing approved asset is flagged for annual recertification review
- Daily scan for assets approaching deployment deadline without approval

**Actions:**
- Cross-reference asset metadata (regulatory standard, hazard class, language) against a compliance checklist database
- Flag missing required elements (e.g., GHS label missing precautionary statement, ANSI sign missing signal word)
- Generate a compliance pre-check report as a file attachment on the item
- Auto-reject and return to designer with specific deficiency notes if critical elements are missing
- Notify HSE reviewer with confidence score (High/Medium/Low) for approval readiness
- Escalate to Legal if asset involves new chemical classification or international deployment

**Data Required:**
- Regulatory standard reference database (ANSI Z535 elements, GHS label requirements, NFPA 704 specifications)
- Asset metadata from monday.com board columns
- Historical approval/rejection patterns for learning
- Integration with facility master list for site-specific requirements

**Autonomy Level:** Human-in-the-Loop
The agent performs automated pre-screening and generates compliance reports, but final approval always requires human HSE reviewer sign-off. Agent can auto-reject clearly non-compliant submissions but cannot auto-approve.

**Example Interaction:**
> A field operations manager at the Permian Basin facility submits a request for updated hydrogen sulfide (H2S) warning signs after a recent API standard revision. The ComplianceGuard agent immediately identifies this as an API RP 55-governed asset, cross-references the new standard requirements, and generates a specification sheet for the designer including required signal words ("DANGER"), hazard pictograms (skull and crossbones, exclamation mark), color specifications (red/white per ANSI Z535.4), and the specific H2S exposure limits that must appear on the sign.
>
> The designer completes the artwork and moves it to HSE Review. The agent scans the uploaded file's metadata and checklist, confirms all required elements are present, notes that the Spanish translation is pending (Permian Basin sites require bilingual signage), and generates a compliance report showing 92% readiness — flagging only the missing Spanish version. The HSE reviewer receives a notification: "Asset pre-screened: 1 item pending (Spanish translation). All regulatory elements verified against API RP 55 Rev. 2025." This reduces HSE review time from 2 hours to 15 minutes.

---

### Use Case 2: Energy Transition Brand & Campaign Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every major energy company is undergoing a brand evolution — from "oil company" to "energy company" to "energy transition leader." This requires coordinated creative campaigns across investor relations, government affairs, consumer marketing, employee communications, and community relations. Shell's "Powering Progress," BP's "Reimagining Energy," and TotalEnergies' rebrand from Total all represent multi-year, multi-million-dollar creative initiatives. Mid-market companies face the same pressure with a fraction of the budget. Creative teams are simultaneously maintaining legacy brand assets (upstream E&P campaigns, fuel retail signage) while developing entirely new visual identities for renewables, EV charging, hydrogen, and carbon capture divisions. Without centralized campaign management, brand inconsistency creeps in — the solar division uses different colors than corporate, investor presentations contradict sustainability reports, and regional offices create off-brand materials.

#### The Solution
monday.com Work Management as a campaign command center. A master Campaign Board with sub-items for individual deliverables, connected to a Brand Asset Library board and a Stakeholder Approval board. Columns include Campaign Name, Business Unit (dropdown: Upstream, Midstream, Downstream, Renewables, EV/Mobility, Hydrogen, Carbon Capture, Corporate), Target Audience (multi-select: Investors, Regulators, Consumers, Employees, Communities, Partners), Channel (multi-select: Print, Digital, Social, OOH, Investor Deck, Annual Report, Internal Portal), Brand Compliance Status, and Campaign Launch Date. Timeline views show overlapping campaigns, preventing message conflicts (e.g., a renewables campaign launching the same week as an upstream acquisition announcement). Dashboards provide executive visibility into creative output by business unit.

#### The Outcome
50% faster campaign launch cycles through parallel workstream management. Brand consistency score improvement from ~60% to 95%+ across all divisions. 30% reduction in agency spend through better brief management and fewer revision cycles. Single source of truth for energy transition messaging across all stakeholder audiences.

#### Discovery Questions
1. "How are you managing the creative workload of simultaneously maintaining your legacy energy brand while building new brand identities for renewables and energy transition initiatives?"
2. "When your CEO presents to investors about your net-zero commitments, how confident are you that the visual assets in that deck are consistent with what your sustainability team is publishing and what your consumer marketing team is running?"
3. "How many external agencies and freelancers support your creative needs, and how do you manage briefs, reviews, and approvals across those relationships?"
4. "Have you experienced any brand inconsistency incidents — for example, a regional office using outdated messaging or a new business unit creating off-brand materials?"
5. "What's your process for ensuring that creative campaigns align with regulatory requirements around environmental claims (FTC Green Guides, EU Green Claims Directive)?"

#### Industry Context
Energy transition branding is a minefield. "Greenwashing" accusations are a real risk — the FTC's Green Guides and the EU's proposed Green Claims Directive impose strict requirements on environmental marketing claims. ClientEarth's lawsuit against Shell's advertising demonstrates the legal exposure. Creative teams must balance aspirational messaging ("leading the energy transition") with defensible claims backed by actual emissions data. ESG reporting frameworks (GRI, SASB, TCFD, the new ISSB standards) each have specific requirements for how environmental data is visualized. The creative team must work closely with sustainability, legal, and investor relations to ensure visual communications are both compelling and defensible.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Energy Transition Campaign Management system. Board 1 — Campaign Master: Campaign Name (text), Business Unit (dropdown: Upstream E&P, Midstream, Downstream/Refining, Renewables/Solar/Wind, EV & Mobility, Hydrogen, Carbon Capture/CCUS, Corporate), Campaign Type (dropdown: Brand Awareness, Product Launch, ESG/Sustainability, Investor Relations, Regulatory/Government Affairs, Community Relations, Recruitment, Internal Comms), Target Audience (dropdown: Institutional Investors, Retail Investors, Regulators, Consumers, Employees, Local Communities, Partners/JV, Media), Lead Creative (people), Campaign Status (status: Briefing-Purple, Concept-Blue, Production-Orange, Legal Review-Yellow, Approved-Green, Live-Dark Green, Post-Mortem-Gray), Launch Date (date), End Date (date), Budget (numbers with $ prefix), Green Claims Review (status: Not Required-Gray, Pending Legal-Yellow, Approved-Green, Flagged-Red), Connected Deliverables (connect to Deliverables board). Board 2 — Campaign Deliverables: Deliverable Name (text), Parent Campaign (connect), Format (dropdown: Social Post, Video, Print Ad, OOH Billboard, Investor Deck, Annual Report Section, Microsite, Email Template, Internal Newsletter, Trade Show Booth, Press Kit), Dimensions/Specs (text), Assigned Designer (people), Status (status: Brief Received-Purple, In Design-Blue, Internal Review-Orange, Client/Stakeholder Review-Yellow, Final-Green, Deployed-Dark Green), Brand Compliance (status: Unchecked-Gray, Compliant-Green, Needs Revision-Red), Due Date (date), Files (file). Automations: When Campaign Status is Legal Review, notify legal team and set 3-day deadline; When Green Claims Review is Flagged, block Campaign Status from moving to Approved; When all connected Deliverables are Final, notify Campaign Lead. Views: Campaign Timeline (Gantt by Launch/End Date), Kanban by Status, Dashboard with campaigns by Business Unit, deliverable throughput, budget burn, and Green Claims compliance rate."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BrandGuard Energy Transition Agent
**Agent Purpose:** Monitor all creative output for brand consistency, green claims compliance, and messaging alignment across energy transition campaigns.

**Triggers:**
- When any deliverable moves to "Internal Review" status
- When a new campaign brief is created
- Weekly scan of all active campaigns for cross-campaign messaging conflicts
- When regulatory updates (FTC Green Guides, EU directives) are published (manual trigger)

**Actions:**
- Analyze campaign brief against brand guidelines and flag deviations
- Cross-reference environmental claims in deliverables against published ESG data and legal-approved claim library
- Detect messaging conflicts between simultaneous campaigns (e.g., upstream acquisition celebration vs. "phasing out fossil fuels" campaign)
- Generate brand consistency scores for each deliverable
- Auto-create legal review tasks when green claims are detected
- Produce weekly executive summary of creative output by business unit with compliance metrics

**Data Required:**
- Brand guidelines database (by business unit)
- Legal-approved environmental claims library
- Published ESG metrics (emissions, renewables capacity, etc.)
- Active campaign calendar
- Regulatory requirements database (FTC, EU, regional)

**Autonomy Level:** Escalation-Based
Agent flags potential issues and generates reports autonomously. Blocks campaign progression only when green claims are detected without legal pre-approval. All other flags are advisory — human creative directors make final decisions.

**Example Interaction:**
> The Renewables division submits a social media campaign with the headline "100% Clean Energy by 2035." The BrandGuard agent cross-references this claim against the company's published Science-Based Targets initiative (SBTi) commitment, which actually states "net-zero Scope 1 & 2 by 2050, 50% reduction by 2035." The agent flags the deliverable: "Environmental claim exceeds published commitment. Recommend revision to '50% Emissions Reduction by 2035' or obtain legal approval for aspirational framing. Reference: 2024 Sustainability Report, p.47." The agent simultaneously checks the brand guidelines and notes the Renewables division is using a green (#2ECC71) that's not in the approved corporate palette (#27AE60). Both issues are added as update comments on the item, and the status is automatically moved to "Needs Revision" with the Green Claims Review set to "Flagged."

---

### Use Case 3: Technical Illustration & Engineering Drawing Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies produce enormous volumes of technical illustrations — piping and instrumentation diagrams (P&IDs), process flow diagrams (PFDs), single-line electrical diagrams, well schematics, seismic cross-sections, and facility layout drawings. While the originals live in engineering tools (AutoCAD, Aveva, Bentley), the creative team is constantly asked to produce "presentation-ready" versions for board meetings, regulatory filings, investor presentations, and public consultations. These requests come ad-hoc, require security classification review (some diagrams are CFATS-regulated critical infrastructure information), and often need simplification for non-technical audiences. Currently, engineers email PDF exports to creative, who recreate them in Illustrator, send for review, get corrections, iterate — a process that takes weeks and produces dozens of email-lost file versions.

#### The Solution
monday.com as the request management and review workflow for technical illustration requests. A board with columns for Illustration Type (dropdown: P&ID, PFD, Well Schematic, Electrical Single-Line, Facility Layout, Seismic Section, Equipment Cutaway, Process Animation), Source Engineering System (dropdown: AutoCAD, Aveva E3D, Bentley OpenPlant, Petrel, custom), Security Classification (status: Public-Green, Internal-Blue, Confidential-Orange, CFATS/CII-Red), Requesting Department, Target Audience, Simplification Level (dropdown: Full Technical, Management Summary, Public/Investor, Regulatory Filing), and multi-stage approval workflow. Integration with cloud storage for large engineering files. Dashboard showing request backlog by classification level and department.

#### The Outcome
70% reduction in technical illustration turnaround time (from 3 weeks to 4 days). Zero security classification incidents through enforced review workflows. 50% reduction in revision cycles through structured briefs and in-platform markup. Annual savings of $150K+ in designer time previously spent chasing engineers for feedback.

#### Discovery Questions
1. "When your CEO needs a simplified version of a process flow diagram for an investor presentation, what's the current turnaround time from request to approved final asset?"
2. "How do you currently manage the security classification of technical illustrations — especially those involving critical infrastructure information subject to CFATS?"
3. "How many revision cycles does a typical technical illustration go through, and where does the review process break down?"
4. "What percentage of your creative team's time is spent on technical illustration versus strategic creative work like brand campaigns?"
5. "Have you ever had a security incident involving the wrong version of a classified diagram being shared externally?"

#### Industry Context
The Chemical Facility Anti-Terrorism Standards (CFATS) program, while sunsetted in 2023, established practices around Critical Infrastructure Information (CII) that many energy companies continue to follow. TSA Pipeline Security Directives impose similar requirements for pipeline facility information. FERC's Critical Energy/Electric Infrastructure Information (CEII) rules restrict sharing of certain utility diagrams. The creative team must understand these classifications because a "simplified" diagram that reveals too much facility detail could violate security requirements. P&IDs (Piping & Instrumentation Diagrams) follow ISA-5.1 symbology standards. Process engineers expect exact adherence to these symbols even in simplified versions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Technical Illustration Request Management board for an energy company. Columns: Request Title (text), Illustration Type (dropdown: P&ID Simplified, Process Flow Diagram, Well Schematic, Electrical Single-Line, Facility Layout, Seismic Cross-Section, Equipment Cutaway, Process Animation/Video, Infographic), Source System (dropdown: AutoCAD, Aveva E3D, Bentley OpenPlant, Schlumberger Petrel, OSIsoft PI, Manual/Scan, Other), Security Classification (status: Public-Green, Internal Only-Blue, Confidential-Orange, CFATS/CII/CEII-Red), Simplification Level (dropdown: Full Technical Detail, Engineering Management Summary, Executive/Board Level, Investor/Public, Regulatory Filing), Requesting Engineer (people), Requesting Department (dropdown: Operations, Engineering, Reservoir, Drilling, HSE, Investor Relations, Government Affairs, Legal), Assigned Illustrator (people), Security Reviewer (people), Technical Reviewer (people), Status (status: New Request-Purple, Source Files Received-Blue, In Production-Orange, Technical Review-Yellow, Security Review-Red, Final Approval-Green, Delivered-Dark Green), Source Files (file), Draft Versions (file), Approved Final (file), Due Date (date), Revision Count (numbers), Notes (long text). Automations: When Security Classification is CFATS/CII/CEII, automatically assign Security Reviewer from compliance team and block delivery until Security Review approved; When Status is Technical Review for more than 3 days, send reminder to Technical Reviewer; When Revision Count exceeds 3, notify creative team lead. Views: Main Table, Kanban by Status, Dashboard showing requests by Security Classification, average turnaround time, revision cycles by department, and workload per illustrator."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** TechViz Simplification Assistant
**Agent Purpose:** Auto-generate first-draft simplified technical illustrations from engineering source files with appropriate detail levels for target audiences.

**Triggers:**
- When a new illustration request is submitted with source files attached
- When Simplification Level is changed on an existing request
- When a Technical Reviewer rejects with specific markup notes

**Actions:**
- Analyze source engineering file metadata to identify diagram type and complexity
- Generate a simplified draft based on Simplification Level (strip unnecessary detail layers, adjust symbology for non-technical audiences)
- Apply security classification rules — automatically redact facility-specific identifiers for Public classification
- Create annotation layer highlighting areas requiring human designer attention
- Suggest appropriate ISA-5.1 symbol simplifications based on target audience
- Attach generated draft and specification notes to the item

**Data Required:**
- ISA-5.1 symbology reference database
- Security classification rules by facility and asset type
- Audience-specific simplification guidelines (what to show/hide for Investors vs. Regulators vs. Public)
- Integration with engineering document management system (Aveva, Bentley)

**Autonomy Level:** Human-in-the-Loop
Agent generates first drafts and recommendations but never delivers a technical illustration without human designer review and technical/security sign-off. Agent can auto-classify security level based on content detection but classification must be confirmed by security reviewer.

**Example Interaction:**
> An Investor Relations manager requests a simplified version of the new LNG terminal's process flow diagram for the Q3 earnings presentation. The source P&ID from Aveva E3D is a complex, multi-sheet document with 3,000+ components. The TechViz agent analyzes the source, identifies it as a liquefaction process train, and generates a board-level simplification showing only major process blocks (Feed Gas Treatment → Liquefaction → Storage → Loading) with key capacity figures. The agent flags: "Source file contains CEII-classified compressor station details. These have been automatically redacted for Investor/Public classification. Security review recommended." The illustrator receives a clean first draft that needs only aesthetic refinement rather than starting from scratch — cutting production time from 3 days to 4 hours.

---

### Use Case 4: ESG Report Design & Production Workflow

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Annual ESG (Environmental, Social & Governance) reports have become the single most complex creative deliverable in energy companies. A typical report is 100-200+ pages, contains hundreds of data visualizations, must comply with multiple reporting frameworks (GRI, SASB, TCFD, ISSB/IFRS S1/S2), requires input from 15-30 internal stakeholders across sustainability, finance, operations, legal, and HR, undergoes 5-8 review cycles, and must be published in multiple formats (interactive web, PDF, print) and languages. The creative team manages this alongside all their other work. Current process: sustainability team dumps content into a shared drive, creative designs in InDesign, reviews happen via printed PDFs with handwritten markups or scattered email comments, version conflicts are constant, and the final month before publication is pure chaos. Errors in ESG reports are not just embarrassing — they can trigger SEC scrutiny (with new climate disclosure rules) and investor lawsuits.

#### The Solution
monday.com as the ESG Report production management system. A master board with one item per report section/chapter, sub-items for individual data visualizations and charts. Columns: Section Name, Framework Alignment (multi-select: GRI, SASB, TCFD, ISSB, CDP, UN SDGs), Content Owner (people), Data Source (text), Designer Assigned (people), Content Status (status: Data Collection → Draft Copy → Design → Internal Review → Legal/Assurance Review → Final), Data Verification Status (status: Unverified → Verified by Source → Verified by Assurance), Reviewer Comments (long text), Files (file for each version). Connected board for the overall publication timeline with print/digital deadlines. Automations enforce sequential review gates — content can't go to design without verified data; design can't go to legal without content owner sign-off.

#### The Outcome
40% reduction in ESG report production cycle (from 5 months to 3 months). Zero data errors reaching publication through enforced verification workflows. 60% reduction in review cycle time through centralized, concurrent feedback. Compliance with SEC climate disclosure rules through auditable content trail.

#### Discovery Questions
1. "Walk me through your last ESG report production cycle — how many people were involved, how long did it take from kickoff to publication, and where were the biggest bottlenecks?"
2. "How do you currently ensure that every data point in your sustainability report is verified and traceable to its source — especially given the SEC's new climate disclosure requirements?"
3. "How many review cycles does a typical section go through, and how do you manage conflicting feedback from different stakeholders?"
4. "What's your process for ensuring the report complies with multiple reporting frameworks simultaneously — GRI, SASB, TCFD?"
5. "Have you ever had to issue a correction or restatement on an ESG report? What was the root cause?"

#### Industry Context
The SEC's Climate Disclosure Rules (adopted March 2024, implementation phased 2025-2027) require registrants to disclose climate-related risks, GHG emissions (Scope 1, 2, and for large accelerated filers, Scope 3), and climate targets. These disclosures will be subject to the same legal standards as financial statements — meaning errors in ESG reports could trigger securities fraud liability. The EU's Corporate Sustainability Reporting Directive (CSRD) imposes similar requirements for companies with EU operations. The International Sustainability Standards Board (ISSB) issued IFRS S1 and S2 in 2023, creating a global baseline. For energy companies, this means ESG reports are no longer "nice to have" marketing documents — they're regulated financial communications requiring the same rigor as annual reports.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an ESG Report Production Management system for an energy company. Board 1 — Report Sections: Section Title (text), Chapter (dropdown: Environmental/Climate, Social/Workforce, Governance, Energy Transition, Safety Performance, Community Impact, Supply Chain, Data Tables/Appendix), Framework Tags (dropdown: GRI, SASB, TCFD/ISSB, CDP, UN SDGs, SEC Climate Disclosure), Content Owner (people), Data Analyst (people), Assigned Designer (people), Legal Reviewer (people), External Assurance (people), Content Status (status: Data Collection-Purple, Draft Copy-Blue, In Design-Orange, Internal Review-Yellow, Legal Review-Red, Assurance Review-Pink, Final Approved-Green, Published-Dark Green), Data Verification (status: Unverified-Red, Source Verified-Yellow, Independently Verified-Green), Word Count (numbers), Data Visualizations Count (numbers), Content Draft (file), Design Draft (file), Final Approved (file), Due Date (date), Reviewer Feedback (long text). Board 2 — Publication Timeline: Milestone Name (text), Type (dropdown: Content Deadline, Design Freeze, Legal Sign-Off, Assurance Completion, Print Deadline, Web Launch, Press Release), Owner (people), Status (status: Not Started-Gray, In Progress-Blue, Complete-Green, At Risk-Red, Blocked-Purple), Date (date). Automations: Block Content Status from moving to In Design unless Data Verification is at least Source Verified; When Content Status changes to Legal Review, assign Legal Reviewer and set 5-day deadline; When all sections are Final Approved, notify Publication Timeline board to trigger print/web production. Views: Main Table, Timeline/Gantt view by Due Date, Dashboard with section completion by chapter, data verification status, framework coverage heatmap, and days-to-publication countdown."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG DataViz Quality Agent
**Agent Purpose:** Validate data visualizations in ESG reports against source data, ensure framework compliance, and flag inconsistencies before publication.

**Triggers:**
- When a designer uploads a design draft to any report section
- When source data is updated after a visualization has been designed
- Weekly integrity check across all sections during production period
- When External Assurance reviewer flags a data discrepancy

**Actions:**
- Compare numbers in data visualizations against verified source data columns
- Flag any discrepancy between visual representation and underlying data
- Check framework compliance (e.g., GRI requires specific disclosure numbers, SASB requires specific metrics by industry)
- Detect inconsistencies across sections (e.g., total emissions in Chapter 1 summary vs. detailed breakdown in Data Tables)
- Generate a "publication readiness" score for each section
- Create assurance-ready audit trail linking each data point to its verified source

**Data Required:**
- Verified source data from Data Analyst columns
- Framework requirements database (GRI Standards index, SASB Oil & Gas metrics, TCFD recommended disclosures)
- Previous year's published data for year-over-year consistency check
- SEC climate disclosure rule requirements

**Autonomy Level:** Human-in-the-Loop
Agent flags issues and generates reports but never modifies published data or design files. All discrepancies require human resolution. Agent blocks progression to Legal Review only when data discrepancies exceed materiality threshold.

**Example Interaction:**
> A designer uploads the "GHG Emissions Performance" page showing a 12% year-over-year reduction in Scope 1 emissions. The ESG DataViz agent cross-references the chart values against the verified data in the Data Tables section and discovers a discrepancy: the chart shows 4.2 million tCO2e but the data table shows 4.35 million tCO2e — a 3.5% variance. The agent flags: "CRITICAL: Scope 1 emissions discrepancy between Chapter 1 visualization (4.2M tCO2e) and Data Tables (4.35M tCO2e). This exceeds the 1% materiality threshold. SEC Climate Disclosure rules require consistent data across all report sections. Please resolve before Legal Review." The agent also notes: "GRI 305-1 disclosure requirement: ensure methodology description accompanies this visualization."

---

### Use Case 5: Digital Asset Management (DAM) & Brand Portal

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Energy companies accumulate massive libraries of visual assets over decades — facility photography (aerials, ground-level, construction progress), executive headshots, logo variants (by business unit, by region, vintage logos for historical use), maps, infographics, stock photography licenses, video footage, and the technical illustrations mentioned above. These assets are scattered across SharePoint sites, local drives, agency FTP servers, and individual designer machines. Finding the "approved current headshot of the CEO" or the "latest aerial photo of the Midland Basin operations" takes 30-60 minutes of searching and emailing. Worse, outdated or unapproved assets get used because people grab whatever they find first. Stock photography licenses expire without anyone tracking them, creating legal exposure. When an energy company acquires another company (frequent in the current consolidation wave), integrating their asset library is a nightmare.

#### The Solution
monday.com as a lightweight DAM and brand portal. A master Asset Library board with items for each asset or asset group. Columns: Asset Name, Category (dropdown: Photography, Logo/Brand Mark, Illustration, Infographic, Video, Icon Set, Template, Map, Chart/Data Viz), Business Unit, Approved Use (multi-select: External Marketing, Internal Comms, Investor Relations, Regulatory Filing, Social Media, Press/Media Kit), License Type (status: Owned-Green, Licensed/Expiring-Yellow, Licensed/Perpetual-Blue, Rights-Managed-Orange), License Expiry Date (date), Current Version (file), Previous Versions (file), Keywords (tags), Photographer/Creator (text). Automation alerts 30 days before license expiry. A "Brand Portal" view with filtered, read-only access for non-creative employees to self-serve approved assets.

#### The Outcome
90% reduction in asset search time (from 30+ minutes to under 3 minutes). Elimination of brand compliance violations from outdated asset usage. $50K+ annual savings from proactive license management (avoiding unintentional rights violations). Self-service brand portal reduces ad-hoc requests to creative team by 40%.

#### Discovery Questions
1. "If I asked five different people in your organization for the current approved version of your company logo, how many different versions would I get back?"
2. "How do you currently track stock photography and video licenses — and when was the last time you audited for expired licenses still in use?"
3. "How long does it typically take someone outside the creative team to find an approved asset they need — say, a facility photo for a presentation?"
4. "When you acquired [recent acquisition], how did you handle integrating their visual asset library into yours?"
5. "Do your regional offices or business units ever create their own visual assets outside of the creative team's oversight?"

#### Industry Context
Energy companies have unique DAM challenges. Facility photography often has security restrictions — aerial photos of refineries or LNG terminals may be restricted under TSA security directives. Environmental photography (wildlife near operations, habitat restoration) has specific usage rights tied to environmental impact agreements. Photography of indigenous community engagement requires cultural sensitivity and sometimes specific consent protocols. Historical assets (photos from the 1960s-1980s) may have asbestos or safety-practice imagery that's no longer appropriate for external use. M&A activity is frequent — the energy sector has seen 500+ deals per year in recent years — each bringing a new library of assets to integrate.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Digital Asset Management & Brand Portal for an energy company. Columns: Asset Name (text), Asset ID (auto-number with prefix 'DAM-'), Category (dropdown: Facility Photography, Executive Photography, Logo/Brand Mark, Technical Illustration, Infographic, Video/Animation, Icon Set, Template, Map/GIS, Chart/Data Visualization, Stock Image, Historical Archive), Business Unit (dropdown: Corporate, Upstream, Midstream, Downstream, Renewables, EV/Mobility, All), Security Classification (status: Public-Green, Internal-Blue, Restricted-Orange, Classified-Red), Approved Uses (dropdown: External Marketing, Internal Communications, Investor Presentations, Regulatory Filings, Social Media, Press Kit, Trade Shows, Website, All Approved Uses), License Type (status: Company Owned-Green, Licensed Perpetual-Blue, Licensed Expiring-Yellow, Rights Managed-Orange, Creative Commons-Purple), License Expiry (date), Photographer/Source (text), Location/Facility (text), Keywords (text), Brand Compliant (status: Current-Green, Legacy/Archive-Yellow, Deprecated-Red), Current File (file), Previous Versions (file), Last Used Date (date), Usage Count (numbers). Automations: When License Expiry is within 30 days, notify creative lead and legal; When Brand Compliant changes to Deprecated, notify all recent users; When Usage Count exceeds 50, flag as 'High Usage Asset' for priority updates. Views: Main Table, Gallery view grouped by Category (for visual browsing), Kanban by Security Classification, Dashboard showing total assets by category, expiring licenses, deprecated assets still in circulation, and most-used assets."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AssetFinder Intelligent Search Agent
**Agent Purpose:** Help employees across the organization find the right approved visual asset instantly through natural language queries.

**Triggers:**
- When an employee submits an asset request via form
- When a new presentation or document is created that references facility names or brand elements
- Manual invocation via chatbot interface
- When an unapproved asset is detected in use (integration with document management)

**Actions:**
- Parse natural language requests ("I need a recent aerial photo of our Gulf of Mexico platform for an investor presentation")
- Search the DAM board by keywords, facility, business unit, and approved uses
- Filter results by requester's security clearance level
- Return top 3-5 matching assets with usage rights summary
- If no approved asset exists, automatically create a request on the creative team's intake board
- Track asset usage for popularity analytics

**Data Required:**
- Full DAM board with keyword metadata
- Employee security clearance/department information
- Asset usage rights and license details
- Facility name/location database for matching

**Autonomy Level:** Fully Autonomous
Agent searches and returns results without human intervention. Creates intake requests automatically when no suitable asset is found. Cannot modify asset metadata or approve new assets.

**Example Interaction:**
> A Government Affairs manager types: "I need photos of our Permian Basin water recycling facility for a EPA stakeholder meeting next Tuesday." The AssetFinder agent searches the DAM, finds 12 matching assets from the Permian Basin, filters to 4 that show water recycling infrastructure, checks that all 4 are approved for "Regulatory Filings" use, verifies none are security-classified, and returns them in a gallery view with thumbnails, file sizes, and dates taken. The agent notes: "3 of these photos are from 2024. The facility was expanded in Q3 2025 — no post-expansion photography exists. I've created a photography request (DAM-4521) for updated facility images. In the meantime, these 2024 images are approved for use with the caveat that they pre-date the expansion."

---

### Use Case 6: Agency & Freelancer Management

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Energy company creative teams rely heavily on external agencies and freelancers — typically managing 5-15 agency relationships and 10-30 freelancers simultaneously. Agencies handle major campaigns (brand refresh, annual report design, video production), while freelancers fill specialized gaps (3D rendering of facilities, aerial drone photography, motion graphics). Managing these relationships involves scattered briefs (email), disconnected proofing (PDF markups, Figma comments, InVision — often all three for different agencies), inconsistent onboarding (NDAs, security clearances for facility access, brand guideline distribution), and opaque budget tracking (invoices arrive months after work, often exceeding quoted amounts). The procurement department demands vendor performance data that creative can't produce because everything is tracked informally.

#### The Solution
monday.com as the unified agency/freelancer management platform. A Vendor Board with items for each agency/freelancer, columns for Specialization, Contract Status, NDA Status, Security Clearance Level, Hourly/Project Rate, YTD Spend (formula column pulling from project boards), Performance Rating, and Connected Projects. A Project/Brief Board for each active engagement with columns for Brief Status, Deliverable Specs, Review Rounds (number), Budget vs. Actual, and integrated proofing via file columns with annotation. Automations enforce onboarding requirements (no project assignment without active NDA and completed security training for facility-access vendors).

#### The Outcome
35% reduction in agency management overhead. 20% improvement in project delivery timeliness through structured brief and review processes. Full procurement compliance with vendor performance data on demand. $100K+ annual savings from better budget tracking and scope management.

#### Discovery Questions
1. "How many external creative agencies and freelancers does your team manage, and what's the process for onboarding a new vendor — especially around NDAs and facility security clearances?"
2. "When procurement asks for vendor performance metrics — delivery timeliness, budget adherence, quality ratings — can you produce that data?"
3. "How do you currently manage creative briefs and review cycles with external agencies — is it all email, or do you use proofing tools?"
4. "Have you ever had a budget surprise from an agency — where the final invoice significantly exceeded the original scope?"
5. "What's your biggest bottleneck in working with external creative partners?"

#### Industry Context
Energy companies face unique vendor management challenges. Agencies and freelancers who work on facility-related content may need TWIC (Transportation Worker Identification Credential) cards for port facilities, TSA clearance for pipeline facilities, or company-specific security training. NDAs in the energy sector often include specific clauses around CII, CEII, and trade secrets related to proprietary technology (especially in upstream E&P). Insurance requirements are stringent — agencies doing on-site photography at refineries need specific liability coverage. Many energy companies have vendor diversity requirements (MBE, WBE, SDVOB) that creative teams must track and report on. Procurement increasingly requires competitive bidding even for creative services, adding complexity.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Agency & Freelancer Management system for an energy creative team. Board 1 — Vendor Registry: Company/Individual Name (text), Type (dropdown: Full-Service Agency, Specialized Agency, Freelance Designer, Freelance Photographer, Freelance Videographer, 3D/Rendering Specialist, Copywriter, Translation Service), Specialization (dropdown: Brand/Identity, Annual Report/ESG, Digital/Web, Video Production, Facility Photography, Technical Illustration, Motion Graphics, 3D Visualization, Translation/Localization), Contract Status (status: Active-Green, Pending Renewal-Yellow, Expired-Red, Prospect-Gray), NDA Status (status: Signed-Green, Pending-Yellow, Expired-Red, Not Required-Gray), Security Clearance (status: Not Required-Gray, TWIC Cleared-Green, Facility Access Approved-Blue, Pending-Yellow), Diversity Classification (dropdown: None, MBE, WBE, SDVOB, HUBZone, 8a, Other), Hourly Rate (numbers with $/hr), Day Rate (numbers with $/day), YTD Spend (numbers with $), Performance Rating (rating 1-5), Primary Contact (text), Contact Email (email), Portfolio Link (link), Insurance Expiry (date), Connected Projects (connect). Board 2 — Creative Briefs: Project Name (text), Vendor (connect to Vendor Registry), Brief Type (dropdown: Campaign, One-Off Deliverable, Ongoing Retainer, Photography Shoot, Video Production), Brief Status (status: Drafting-Purple, Sent to Vendor-Blue, In Production-Orange, In Review-Yellow, Revisions-Red, Approved-Green, Complete-Dark Green), Budget Quoted (numbers $), Budget Actual (numbers $), Budget Variance (formula), Review Rounds Used (numbers), Max Review Rounds (numbers), Deliverables (file), Brief Document (file), Due Date (date). Automations: When new Brief is created, check connected Vendor NDA Status — if Expired or Pending, block and notify; When Budget Actual exceeds Budget Quoted by 10%, alert creative director; When Insurance Expiry is within 30 days on any vendor, notify procurement. Views: Vendor Gallery view, Brief Kanban by Status, Dashboard with spend by vendor, budget variance trends, vendor performance ratings, diversity spend percentage, and active brief count."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorMatch Creative Sourcing Agent
**Agent Purpose:** Recommend the optimal agency or freelancer for new creative briefs based on specialization, past performance, availability, budget, and compliance status.

**Triggers:**
- When a new Creative Brief is created without a vendor assigned
- When a vendor declines or is unavailable for an assigned brief
- Quarterly vendor performance review (scheduled)

**Actions:**
- Analyze brief requirements (type, specialization, budget, timeline, security clearance needs)
- Score and rank available vendors from registry based on match criteria
- Check compliance status (NDA, insurance, security clearance) and flag any gaps
- Generate a shortlist of 3 recommended vendors with rationale
- Calculate projected cost based on vendor rates and brief scope
- Track vendor workload to avoid over-concentration

**Data Required:**
- Vendor Registry board with all metadata
- Historical brief data (performance, budget variance, delivery times)
- Current vendor workload (active briefs connected)
- Diversity spend targets from procurement

**Autonomy Level:** Human-in-the-Loop
Agent recommends but never assigns vendors autonomously. Creative director makes final vendor selection. Agent can flag compliance blockers that must be resolved before assignment.

**Example Interaction:**
> A creative manager creates a brief for aerial drone photography of the new offshore wind farm installation. The VendorMatch agent analyzes the requirements: specialization = Facility Photography, security clearance = Maritime/TWIC required, location = Gulf of Mexico, budget = $15,000-$25,000. The agent scans the registry and returns: "Recommended: (1) SkyView Energy Media — 4.8/5 rating, TWIC cleared, 6 prior offshore shoots, avg. budget variance +3%, available. (2) Gulf Coast Aerials — 4.5/5, TWIC cleared, 3 prior offshore shoots, avg. budget variance -2%, available. (3) HighAlt Studios — 4.7/5, TWIC pending (ETA 2 weeks), 12 onshore facility shoots but no offshore experience, available. Note: Diversity spend is at 18% vs. 25% target — HighAlt Studios is a certified SDVOB which would improve your diversity metrics."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| P&ID | Piping & Instrumentation Diagram — detailed diagram showing piping, equipment, and instrumentation in a process plant |
| PFD | Process Flow Diagram — simplified diagram showing major process steps and equipment |
| ANSI Z535 | American National Standards Institute safety sign and color standards |
| GHS | Globally Harmonized System of Classification and Labelling of Chemicals |
| NFPA 704 | "Fire diamond" — standard for identifying hazards of materials for emergency response |
| CFATS | Chemical Facility Anti-Terrorism Standards — DHS program for high-risk chemical facilities |
| CEII | Critical Energy/Electric Infrastructure Information — FERC-protected information |
| CII | Critical Infrastructure Information — protected under DHS programs |
| TWIC | Transportation Worker Identification Credential — required for unescorted access to secure maritime facilities |
| ESG | Environmental, Social & Governance — framework for corporate sustainability reporting |
| GRI | Global Reporting Initiative — international standards for sustainability reporting |
| SASB | Sustainability Accounting Standards Board — industry-specific disclosure standards |
| TCFD | Task Force on Climate-related Financial Disclosures — recommendations for climate risk reporting |
| ISSB | International Sustainability Standards Board — global baseline for sustainability disclosure (IFRS S1/S2) |
| ISA-5.1 | Instrumentation Symbols and Identification standard — defines symbols used in P&IDs |
| LOTO | Lockout/Tagout — safety procedure to ensure equipment is properly shut off during maintenance |
| E&P | Exploration & Production — upstream oil & gas activities |
| LNG | Liquefied Natural Gas — natural gas cooled to liquid form for transport/storage |
| CCUS | Carbon Capture, Utilization & Storage — technology to capture CO2 emissions |
| SBTi | Science Based Targets initiative — framework for corporate emission reduction targets |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| VP Corporate Communications | Oversees all brand, creative, and communications functions | Decision-maker for creative tools and processes |
| Creative Director | Leads creative team, sets design standards, manages agency relationships | Decision-maker for creative workflows |
| HSE Director | Owns safety compliance including visual safety assets | Influencer — mandates requirements for safety-related creative |
| Chief Sustainability Officer | Owns ESG reporting and energy transition narrative | Influencer — primary stakeholder for ESG report production |
| VP Investor Relations | Owns investor-facing communications and presentations | Influencer — high-urgency, high-visibility creative requests |
| Senior Graphic Designer | Executes design work, manages production workflows | User — daily operator of creative management tools |
| Brand Manager | Maintains brand guidelines and approves brand usage | User/Influencer — enforces brand compliance |
| Chief Marketing Officer | Strategic marketing direction, budget owner | Decision-maker — budget authority for creative tools |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| HSE (Health, Safety & Environment) | Primary requester of safety signage, training materials, procedure illustrations | Cross-sell: HSE incident management, training tracking, compliance workflows |
| Sustainability | Primary stakeholder for ESG reports, environmental photography, transition campaigns | Cross-sell: ESG data collection, materiality assessment workflows, stakeholder engagement |
| Investor Relations | High-priority requestor of presentations, annual report visuals, infographics | Cross-sell: IR event management, earnings prep workflow, shareholder engagement tracking |
| Government Affairs | Regulatory filings, public consultation materials, community impact visuals | Cross-sell: Regulatory tracking, government meeting management, permit workflows |
| IT | Digital asset storage, brand portal technology, security classification systems | Cross-sell: IT service management, asset management, security compliance |
| Procurement | Vendor/agency management, contract compliance, diversity reporting | Cross-sell: Vendor management, contract lifecycle management, procurement workflows |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Adobe Workfront | Creative project management, integrated with Creative Cloud | monday.com offers broader cross-departmental visibility; Workfront is siloed to creative team |
| Wrike | Project management with proofing capabilities | monday.com's flexibility and ease of use wins; Wrike is complex for non-creative stakeholders |
| Bynder / Canto / Brandfolder | Dedicated DAM solutions | monday.com won't replace enterprise DAM but serves as lightweight alternative for teams without DAM budget; integrates with existing DAM |
| SharePoint | Default file storage and collaboration | Universally disliked for creative workflows — easy displacement with structured boards and visual views |
| Asana | Work management for creative teams | monday.com's visual-first approach and automation depth win in demo; Asana lacks energy industry presence |
| Smartsheet | Spreadsheet-based project management | Common in energy sector but painful for creative workflows — monday.com's visual boards and file management are dramatically better |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Adobe Workfront for creative project management" | "Workfront is great for creative production, but it's a silo. Your HSE team, sustainability team, and IR team all request creative work — they won't use Workfront. monday.com gives them a self-service intake portal and gives you visibility into demand from all departments, not just what your creative team tracks." |
| "We need a real DAM, not a project management tool" | "Absolutely — for large-scale digital asset management, a dedicated DAM like Bynder makes sense. But most energy creative teams we work with don't have DAM budget approval yet. monday.com serves as a structured brand portal today and integrates with enterprise DAM solutions when you're ready to invest." |
| "Our security requirements are too strict for cloud tools" | "monday.com is SOC 2 Type II, ISO 27001, and HIPAA compliant. We support SSO/SAML, data residency in US/EU, and granular permissions. For CFATS/CEII-classified content, you'd keep that in your existing secure systems — monday.com manages the workflow and metadata, not the classified files themselves." |
| "We're too small a team to justify another tool" | "That's exactly why you need it. A 5-person creative team serving a $10B energy company can't afford to spend 30% of their time on project management overhead. monday.com automates intake, routing, approvals, and status reporting — giving you back 10+ hours per week to do actual creative work." |
| "We can't get budget for creative tools in an energy company" | "Frame it as operational efficiency and regulatory compliance. The safety signage workflow alone — ensuring OSHA compliance and audit-readiness — has a clear ROI. The ESG report workflow directly supports SEC climate disclosure requirements. This isn't a 'creative tool' budget request — it's a compliance and risk management investment." |

## Proof Points
*(To be populated with customer references)*
- [Energy sector creative/marketing team using monday.com]
- [ESG report production workflow case study]
- [Regulated industry brand management reference]
- [Cross-departmental creative intake automation example]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
