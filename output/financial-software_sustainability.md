# Financial Software × Sustainability Playbook

## Overview

Financial software companies are facing unprecedented regulatory pressure to integrate sustainability metrics across their entire technology stack. With CSRD (Corporate Sustainability Reporting Directive) mandating detailed ESG disclosures and TCFD (Task Force on Climate-related Financial Disclosures) requiring climate risk assessments, sustainability teams are drowning in manual data collection, fragmented reporting systems, and endless stakeholder coordination. These teams are expected to deliver real-time ESG insights while managing carbon accounting, sustainable finance product development, and regulatory compliance—all with lean headcount and disconnected tools.

Monday.com's AI Work Platform transforms sustainability operations from reactive compliance exercises into proactive strategic advantages. By deploying AI agents that work 24/7 to automate GHG Protocol calculations, streamline SASB reporting, and orchestrate cross-functional ESG initiatives, financial software companies can scale their sustainability impact without scaling their teams. Our unified mondayDB creates a single source of truth for all sustainability data—from Scope 1/2/3 emissions to green bond allocations—while AI agents handle the heavy lifting of data validation, stakeholder updates, and regulatory submissions.

The strategic shift is clear: instead of hiring more sustainability analysts to manage spreadsheets, deploy intelligent agents that continuously monitor, analyze, and act on sustainability data across your entire financial software ecosystem.

## Value Driver Mapping

| Value Driver | Sustainability Application | Traditional Approach | monday.com AI Approach |
|--------------|---------------------------|---------------------|------------------------|
| **Replace/Augment Headcount** | ESG Data Collection & Validation | Manual data gathering, Excel reconciliation, quarterly scrambles | AI agents continuously collect, validate, and reconcile ESG data across all systems 24/7 |
| **Consolidate Tech Stack** | Fragmented Reporting Tools | Separate tools for GHG Protocol, TCFD, SASB, EU Taxonomy, CSRD | Single platform with AI-powered workflows for all sustainability frameworks |
| **Scale Without Overhead** | Stakeholder Engagement | Email chains, status meetings, manual progress tracking | Automated stakeholder updates, AI-generated progress reports, intelligent escalation |

## Prioritized Use Cases

### 1. **Automated GHG Protocol Reporting & Carbon Accounting**

**Relevance:** 9/10 - Mandatory for CSRD compliance and investor reporting  
**Value Driver:** Replace/Augment Headcount + Consolidate Tech Stack  

**The Pain:** Sustainability teams spend 60-80 hours quarterly collecting Scope 1/2/3 emissions data from dozens of sources, manually validating calculations, and reconciling discrepancies. Carbon accounting requires constant monitoring of energy usage, supply chain emissions, and financed emissions—currently done through error-prone spreadsheets and fragmented vendor tools.

**The Solution:** Deploy AI agents that automatically collect emissions data from facilities management systems, cloud providers, travel platforms, and supply chain partners. Agents validate GHG Protocol calculations in real-time, flag anomalies, and generate compliant reports. Vibe builds custom carbon accounting workflows that adapt to your specific emission sources and calculation methodologies.

**The Outcome:** Reduce quarterly reporting time from 80 hours to 8 hours. Achieve real-time carbon footprint visibility. Eliminate calculation errors and compliance gaps. Free sustainability analysts to focus on reduction strategies instead of data entry.

**Discovery Questions:**
- How many hours does your team spend on quarterly GHG Protocol reporting?
- Which Scope 3 categories are most challenging to track and calculate?
- How many different systems do you pull emissions data from?
- What's your current carbon data validation process?

**Industry Context:** With CSRD requiring detailed Scope 3 reporting and SEC climate disclosure rules looming, manual carbon accounting is becoming impossible. Financial software companies with complex supply chains and cloud infrastructure need automated solutions.

**VIBE PROMPT:** *"Build a carbon accounting board that tracks Scope 1/2/3 emissions with columns for: Emission Source (dropdown), GHG Category (formula), Monthly Usage (numbers), Emission Factor (formula), CO2e Calculated (formula), Validation Status (status), Data Source (text), Last Updated (date). Include views for: Current Month Dashboard, Annual Rollup, Scope 3 Detail, Validation Required. Add automations to alert when data is 30+ days old or when calculated emissions exceed 10% variance from previous period."*

**AGENT BLUEPRINT:** *Carbon Calculation Agent - Triggers on new usage data upload, automatically applies appropriate emission factors, validates calculations against GHG Protocol standards, flags anomalies for human review, generates monthly emission summaries, updates stakeholder boards, escalates to sustainability manager if data gaps exceed 7 days.*

### 2. **CSRD & EU Taxonomy Compliance Automation**

**Relevance:** 10/10 - Mandatory for EU operations and global financial software companies  
**Value Driver:** Replace/Augment Headcount + Scale Without Overhead  

**The Pain:** CSRD requires reporting on 1,178 data points across environmental, social, and governance metrics. Sustainability teams are manually mapping activities to EU Taxonomy criteria, collecting evidence for "Do No Significant Harm" assessments, and coordinating with legal, finance, and operations teams across time zones. The complexity is overwhelming small sustainability teams.

**The Solution:** AI agents orchestrate the entire CSRD compliance process—automatically mapping business activities to EU Taxonomy criteria, collecting required evidence from across the organization, tracking compliance status, and generating draft disclosures. Vibe creates dynamic compliance dashboards that adapt as regulations evolve.

**The Outcome:** Transform 6-month compliance sprints into continuous, automated processes. Achieve 95% data point completion 3 months before deadlines. Reduce legal review cycles from weeks to days through consistent, structured submissions.

**Discovery Questions:**
- What percentage of your revenue is currently EU Taxonomy aligned?
- How many people are dedicated to CSRD compliance?
- Which CSRD data points are most difficult to collect?
- How do you currently track "Do No Significant Harm" assessments?

**Industry Context:** CSRD applies to all large EU companies and non-EU companies with significant EU operations. Financial software companies must prove their technology enables sustainable finance, making taxonomy alignment crucial for competitive positioning.

**VIBE PROMPT:** *"Build a CSRD compliance board with columns for: Data Point ID (text), CSRD Requirement (long text), Responsible Team (people), Collection Status (status), Evidence Attached (file), EU Taxonomy Mapping (formula), DNSH Assessment (status), Review Status (status), Deadline (date). Include views for: Overdue Items, By Data Point Category, Team Workload, Executive Summary. Add automations to send weekly reminders for overdue items and escalate to executive team if >20% of items are behind schedule within 60 days of deadline."*

**AGENT BLUEPRINT:** *CSRD Compliance Agent - Triggers on approaching deadlines or status changes, automatically requests updates from responsible teams, validates collected evidence against CSRD requirements, generates compliance reports, identifies gaps and risks, escalates critical issues to sustainability director, maintains audit trail for all activities.*

### 3. **Sustainable Finance Product Development Pipeline**

**Relevance:** 9/10 - Critical for revenue growth and competitive differentiation  
**Value Driver:** Scale Without Overhead + Consolidate Tech Stack  

**The Pain:** Financial software companies are rushing to launch ESG-focused products—green bonds, sustainable investment analytics, climate risk modeling—but sustainability teams lack visibility into product development timelines, regulatory alignment, and market readiness. Product teams work in silos, creating compliance gaps and missed opportunities.

**The Solution:** Create unified sustainable finance product pipelines where AI agents monitor regulatory changes, assess product compliance gaps, coordinate cross-functional teams, and track time-to-market metrics. Agents automatically flag when new regulations impact existing products or create new market opportunities.

**The Outcome:** Accelerate sustainable product launches by 40%. Ensure 100% regulatory compliance at launch. Identify new market opportunities within days of regulatory announcements. Improve product-sustainability team collaboration efficiency.

**Discovery Questions:**
- How many sustainable finance products are in your development pipeline?
- What's your average time-to-market for ESG-focused features?
- How do you currently track regulatory impact on product development?
- Which regulatory changes have caught you off-guard recently?

**Industry Context:** Demand for sustainable finance technology is exploding—green bonds hit $500B annually, ESG assets exceed $30T globally, and regulatory requirements are accelerating. Financial software companies must innovate rapidly while maintaining compliance.

**VIBE PROMPT:** *"Build a sustainable product pipeline board with columns for: Product Name (text), Development Stage (status), Sustainability Lead (person), Product Manager (person), Regulatory Requirements (tags), Compliance Status (status), Target Launch (timeline), Revenue Impact (numbers), ESG Metrics Supported (tags), Market Research (file). Include views for: Launch Timeline, Compliance Gaps, Revenue Pipeline, Regulatory Impact. Add automations to notify teams when regulations change that affect their products and escalate to exec team if compliance gaps aren't addressed within 30 days."*

**AGENT BLUEPRINT:** *Sustainable Product Agent - Triggers on regulatory updates or milestone changes, automatically assesses compliance impact on products in pipeline, updates stakeholder groups, generates competitive analysis reports, identifies new product opportunities based on regulatory trends, escalates high-impact regulatory changes to product leadership team.*

### 4. **ESG Investment Analysis & Due Diligence Automation**

**Relevance:** 8/10 - Core capability for investment firms using financial software  
**Value Driver:** Replace/Augment Headcount + Consolidate Tech Stack  

**The Pain:** Investment teams request ESG analysis for 100+ companies quarterly, requiring manual data collection from multiple ESG rating agencies, financial reports, and news sources. Sustainability analysts spend weeks creating investment committee presentations, often working with stale data and inconsistent methodologies.

**The Solution:** AI agents automatically aggregate ESG data from rating agencies (MSCI, Sustainalytics, S&P), financial filings, and news sources for any requested company. Agents apply consistent ESG scoring methodologies, identify material ESG risks, and generate standardized investment analysis reports with real-time data.

**The Outcome:** Reduce ESG due diligence time from 2 weeks to 2 hours per company. Increase analysis quality through consistent methodologies and real-time data. Scale ESG coverage to 10x more companies without additional headcount.

**Discovery Questions:**
- How many companies do you analyze for ESG factors quarterly?
- Which ESG data providers do you currently use?
- What's your typical turnaround time for ESG investment analysis?
- How do you ensure consistency across different analysts' ESG evaluations?

**Industry Context:** EU SFDR and other regulations require detailed ESG disclosures for investment products. Asset managers need scalable ESG analysis capabilities to maintain competitive advantage and regulatory compliance.

**VIBE PROMPT:** *"Build an ESG investment analysis board with columns for: Company Name (text), Ticker Symbol (text), Analysis Request Date (date), Analyst Assigned (person), ESG Score Calculated (numbers), Environmental Rating (rating), Social Rating (rating), Governance Rating (rating), Material ESG Risks (tags), Data Sources Used (tags), Analysis Status (status), Report Generated (file). Include views for: Pending Analysis, By Analyst Workload, High-Risk Companies, Completed Reports. Add automations to assign new requests based on analyst availability and alert investment team when high-risk ESG issues are identified."*

**AGENT BLUEPRINT:** *ESG Analysis Agent - Triggers on new analysis requests, automatically collects ESG data from configured sources, applies standardized scoring methodology, identifies material ESG risks based on industry/geography, generates formatted analysis reports, updates investment committee dashboard, escalates significant ESG risk changes for existing holdings.*

### 5. **Climate Risk Assessment & Scenario Planning (WOW MOMENT)**

**Relevance:** 10/10 - Mandatory for TCFD compliance and risk management  
**Value Driver:** Replace/Augment Headcount + Scale Without Overhead  

**The Pain:** Financial software companies must model climate risks across physical (floods, hurricanes) and transition (carbon pricing, stranded assets) scenarios for TCFD reporting. Current approaches involve expensive consultants, static Excel models, and annual updates that quickly become outdated. Risk teams lack real-time climate data integration.

**The Solution:** Deploy AI agents that continuously monitor climate data feeds, economic indicators, and policy changes to update risk models in real-time. Agents run automated scenario analyses (1.5°C, 2°C, 3°C+ warming), calculate financial impacts across portfolios, and generate dynamic risk reports. The "wow moment": agents proactively alert when climate events or policy changes materially impact specific investments or business operations.

**The Outcome:** Transform annual static risk assessments into continuous, dynamic monitoring. Identify climate risks weeks before competitors. Reduce consultant costs by 80%. Provide real-time risk insights to executives and investors.

**Discovery Questions:**
- How do you currently model physical and transition climate risks?
- What's your process for updating climate scenario assumptions?
- How quickly can you assess climate risk impact on new investments?
- Which climate events have surprised your risk models recently?

**Industry Context:** Central banks and regulators are mandating climate stress testing. Financial institutions need dynamic risk models that can adapt to rapidly changing climate and policy landscapes.

**VIBE PROMPT:** *"Build a climate risk assessment board with columns for: Asset/Investment (text), Physical Risk Exposure (rating), Transition Risk Exposure (rating), Scenario Analyzed (dropdown: 1.5C/2C/3C+), Financial Impact ($), Risk Score (formula), Last Updated (date), Data Sources (tags), Mitigation Actions (text), Risk Trend (status). Include views for: High-Risk Portfolio, Scenario Comparison, Risk Trend Analysis, Executive Dashboard. Add automations to recalculate risk scores when new climate data arrives and alert risk committee when any asset moves to 'High Risk' category."*

**AGENT BLUEPRINT:** *Climate Risk Agent - Triggers on new climate data, policy announcements, or portfolio changes, automatically updates risk models across all scenarios, calculates financial impact on specific assets, identifies emerging risk patterns, generates early warning alerts for material risk changes, updates executive dashboards, escalates significant portfolio-level risk shifts to CRO within 24 hours.*

### 6. **Stakeholder ESG Reporting & Communications**

**Relevance:** 8/10 - Essential for investor relations and customer retention  
**Value Driver:** Scale Without Overhead + Consolidate Tech Stack  

**The Pain:** Sustainability teams field hundreds of ESG questionnaires annually from investors, customers, and rating agencies—each with different formats, deadlines, and requirements. Manual responses lead to inconsistencies, missed deadlines, and frustrated stakeholders. Teams spend 40% of their time on reporting instead of actual sustainability initiatives.

**The Solution:** AI agents maintain a centralized ESG knowledge base and automatically respond to common stakeholder requests using pre-approved content. Agents identify question patterns, suggest response improvements, and ensure consistency across all communications. Custom stakeholder portals provide real-time access to ESG metrics and reports.

**The Outcome:** Reduce response time for ESG questionnaires from weeks to days. Achieve 100% consistency in ESG communications. Free sustainability teams to focus on strategy instead of reporting administration.

**Discovery Questions:**
- How many ESG questionnaires do you complete annually?
- What's your average response time for investor ESG requests?
- How do you ensure consistency across different ESG communications?
- Which stakeholders request the most detailed ESG information?

**Industry Context:** ESG questionnaire volume is increasing 30% annually as investors and customers demand more detailed sustainability information. Automation is essential for scalability.

**VIBE PROMPT:** *"Build an ESG communications board with columns for: Stakeholder Name (text), Request Type (dropdown), Questions Received (file), Response Deadline (date), Assigned To (person), Response Status (status), ESG Topics Covered (tags), Response Quality Score (rating), Follow-up Required (checkbox), Final Response (file). Include views for: Urgent Deadlines, By Stakeholder Type, Response Quality Tracking, Completed Requests. Add automations to assign requests based on team capacity and send deadline reminders 3 days before due date."*

**AGENT BLUEPRINT:** *ESG Communications Agent - Triggers on new stakeholder requests or approaching deadlines, automatically drafts responses using approved content library, identifies question patterns for content updates, ensures response consistency, tracks completion rates, escalates delayed responses to sustainability manager, maintains stakeholder communication history.*

### 7. **Supply Chain ESG Monitoring & Vendor Assessment**

**Relevance:** 9/10 - Critical for Scope 3 reporting and risk management  
**Value Driver:** Replace/Augment Headcount + Consolidate Tech Stack  

**The Pain:** Financial software companies rely on hundreds of vendors and suppliers, each requiring ESG assessment for Scope 3 reporting and risk management. Manual vendor surveys have low response rates, inconsistent data quality, and annual refresh cycles that miss emerging risks. Procurement teams lack ESG visibility for vendor decisions.

**The Solution:** AI agents continuously monitor vendor ESG performance through public data sources, news monitoring, and automated surveys. Agents score vendor ESG risk, identify supply chain hotspots, and alert procurement teams to emerging issues. Integration with procurement systems ensures ESG factors influence vendor selection and contracting.

**The Outcome:** Achieve 90% vendor ESG data coverage (vs. 30% typical). Identify supply chain ESG risks 6 months earlier. Improve Scope 3 data accuracy by 60%. Integrate ESG factors into all procurement decisions.

**Discovery Questions:**
- How many vendors do you currently assess for ESG performance?
- What's your vendor ESG survey response rate?
- How do you identify emerging ESG risks in your supply chain?
- Does procurement consider ESG factors in vendor selection?

**Industry Context:** CSRD requires detailed Scope 3 reporting, making supply chain ESG data essential. Companies with poor supply chain visibility face compliance and reputational risks.

**VIBE PROMPT:** *"Build a vendor ESG assessment board with columns for: Vendor Name (text), Business Category (dropdown), Annual Spend ($), ESG Risk Score (rating), Environmental Score (numbers), Social Score (numbers), Governance Score (numbers), Last Assessment (date), Data Quality (status), Risk Alerts (status), Procurement Contact (person). Include views for: High-Risk Vendors, Assessment Schedule, Spend Analysis, Risk Alerts. Add automations to trigger reassessments annually and alert procurement when vendor risk scores increase significantly."*

**AGENT BLUEPRINT:** *Supply Chain ESG Agent - Triggers on vendor data updates or risk threshold changes, continuously monitors vendor ESG performance through public sources, updates risk scores based on new information, identifies supply chain risk patterns, alerts procurement to high-risk vendors, generates supplier engagement recommendations, escalates critical supply chain risks to sustainability and procurement leadership.*

## Industry Terminology

| Term | Definition | monday.com Application |
|------|------------|------------------------|
| **CSRD** | Corporate Sustainability Reporting Directive - EU regulation requiring detailed ESG disclosures | Automated compliance tracking and reporting workflows |
| **TCFD** | Task Force on Climate-related Financial Disclosures - Framework for climate risk reporting | Climate risk assessment and scenario planning boards |
| **GHG Protocol** | Global standard for measuring and managing greenhouse gas emissions | Carbon accounting automation with Scope 1/2/3 tracking |
| **EU Taxonomy** | Classification system for environmentally sustainable economic activities | Product development pipeline with taxonomy alignment tracking |
| **SASB** | Sustainability Accounting Standards Board - Industry-specific ESG metrics | Sector-specific ESG reporting templates and automations |
| **SFDR** | Sustainable Finance Disclosure Regulation - EU transparency rules for financial products | Investment ESG analysis and product compliance tracking |
| **ISSB** | International Sustainability Standards Board - Global ESG reporting standards | Unified ESG reporting framework with automated updates |
| **CDP** | Carbon Disclosure Project - Global environmental disclosure system | Automated CDP response generation and submission tracking |
| **SBTi** | Science Based Targets initiative - Framework for corporate climate commitments | Carbon reduction target tracking and progress monitoring |
| **DNSH** | Do No Significant Harm - EU Taxonomy requirement to avoid environmental damage | Risk assessment workflows with automated DNSH verification |

## Typical Stakeholder Roles

| Role | Responsibilities | monday.com Value Proposition |
|------|------------------|------------------------------|
| **Chief Sustainability Officer (CSO)** | Overall ESG strategy, stakeholder engagement, regulatory compliance | Executive dashboard with real-time ESG metrics and automated reporting |
| **Sustainability Manager** | Day-to-day ESG program execution, data collection, vendor coordination | Workflow automation, stakeholder management, progress tracking |
| **ESG Analyst** | Data analysis, report preparation, metric calculation | Automated data collection, AI-powered analysis, standardized reporting |
| **Climate Risk Manager** | Physical and transition risk assessment, scenario modeling | Dynamic risk models, automated scenario analysis, early warning systems |
| **Sustainable Finance Lead** | Green product development, taxonomy compliance, investor relations | Product pipeline management, regulatory tracking, investor communications |
| **Carbon Accountant** | GHG inventory, emission calculations, verification | Automated carbon accounting, real-time emission tracking, validation workflows |
| **Sustainability Consultant** | External expertise, compliance guidance, best practices | Collaborative workspaces, knowledge management, process standardization |

## Adjacent Departments

| Department | Collaboration Points | monday.com Integration Benefits |
|------------|----------------------|--------------------------------|
| **Risk Management** | Climate risk, ESG risk integration, regulatory compliance | Unified risk dashboards, automated risk updates, cross-functional visibility |
| **Product Development** | Sustainable product features, ESG integration, customer requirements | Product-sustainability alignment, regulatory impact tracking, feature prioritization |
| **Finance** | Carbon accounting, ESG investments, sustainability budgets | Financial impact tracking, ROI analysis, budget management integration |
| **Legal/Compliance** | Regulatory interpretation, disclosure review, policy development | Regulatory change tracking, compliance workflow automation, audit trail maintenance |
| **Procurement** | Vendor ESG assessment, sustainable sourcing, supply chain risk | Vendor management integration, ESG scoring automation, procurement workflow alignment |
| **Marketing** | ESG communications, sustainability messaging, stakeholder engagement | Content approval workflows, stakeholder communication tracking, brand consistency |
| **IT/Security** | Data management, system integration, security compliance | Secure data sharing, system automation, IT workflow integration |

## Competitive Landscape

| Competitor | Strengths | Weaknesses | monday.com Advantage |
|------------|-----------|------------|----------------------|
| **Workiva** | Strong compliance focus, regulatory expertise | Complex implementation, limited AI capabilities | AI-first approach, faster deployment, intuitive interface |
| **Spherics** | Specialized ESG platform, deep sustainability knowledge | Single-purpose tool, requires integration | Unified work platform, consolidates entire tech stack |
| **Sustainability Cloud (Salesforce)** | CRM integration, established ecosystem | Limited sustainability focus, complex customization | Purpose-built for work management, AI agents coming soon |
| **SAP Sustainability Control Tower** | Enterprise integration, comprehensive data model | Heavy implementation, high cost | Agile deployment, transparent pricing, user-friendly design |
| **Enablon (Wolters Kluwer)** | Mature EHS platform, regulatory compliance | Legacy architecture, limited modern UX | Modern platform, AI-powered automation, collaborative workflows |
| **Consultancies (Big 4)** | Deep expertise, custom solutions | High cost, long timelines, ongoing dependency | Self-service platform, immediate value, internal capability building |

## Objection Handling

| Objection | Response Strategy |
|-----------|------------------|
| **"We need specialized ESG expertise, not a general work platform"** | "monday.com provides the automation and workflow foundation while your sustainability expertise drives the strategy. Our AI agents handle the operational heavy lifting—data collection, calculations, reporting—so your experts can focus on analysis and decision-making. Think of us as your sustainability operations team that never sleeps." |
| **"Our current ESG tools are working fine"** | "The question isn't whether your current tools work—it's whether they can scale to meet upcoming regulatory requirements. CSRD alone requires 1,178 data points. Can your current setup handle 10x more data collection and reporting without 10x more headcount? Our AI agents scale infinitely without additional FTEs." |
| **"ESG is too specialized for a platform approach"** | "Every sustainability process involves coordination: collecting data from multiple teams, validating information, updating stakeholders, meeting deadlines. These are workflow challenges that monday.com excels at, enhanced by AI agents that understand ESG requirements. You get both the collaboration benefits and the domain expertise." |
| **"We can't afford another platform implementation"** | "You can't afford NOT to automate. Calculate the cost of your team spending 60+ hours on quarterly reporting, managing hundreds of vendor ESG assessments manually, and missing regulatory deadlines. Our AI agents pay for themselves by replacing just 0.5 FTE worth of manual work. Implementation is weeks, not months." |
| **"Our data is too sensitive for a cloud platform"** | "Financial software companies already trust monday.com with sensitive data. We offer enterprise-grade security, SOC 2 compliance, and flexible deployment options. Your ESG data is actually less sensitive than your financial data—and gets shared with multiple external stakeholders anyway." |
| **"AI agents sound too experimental for critical compliance work"** | "AI agents handle the operational tasks—data collection, calculations, status updates—while humans maintain control over strategy and compliance decisions. Agents escalate exceptions and maintain complete audit trails. You get the automation benefits with human oversight for peace of mind." |

## Proof Points

**Customer Success Stories:**
- [Insert specific financial software company case study with quantified results]
- [Insert sustainability team ROI metrics and time savings]
- [Insert regulatory compliance success story with timeline improvements]

**Platform Metrics:**
- [Insert monday.com platform adoption statistics in financial services]
- [Insert AI agent beta program results and customer feedback]
- [Insert sustainability-specific template usage and success metrics]

**Third-Party Validation:**
- [Insert analyst reports on work platform market in sustainability]
- [Insert industry awards or recognition for ESG capabilities]
- [Insert integration partnerships with ESG data providers]

*Generated: 2026-02-20 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*