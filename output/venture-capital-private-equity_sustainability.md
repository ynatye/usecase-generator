# Venture Capital & Private Equity × Sustainability Playbook

## Overview

Sustainability teams in VC/PE firms operate at the nexus of financial performance and environmental/social impact, managing increasingly complex regulatory requirements and investor mandates. These teams typically range from 2-15 professionals depending on fund size, with responsibilities spanning ESG due diligence on new investments, portfolio company monitoring and improvement, regulatory compliance (SFDR, UNPRI), and impact measurement. The regulatory landscape has become particularly demanding with SFDR Article 8/9 classifications requiring detailed documentation and ongoing monitoring of sustainability commitments.

The role has evolved from "nice-to-have" ESG oversight to mission-critical operations that directly impact fund performance, investor relations, and regulatory compliance. Modern sustainability teams must coordinate across investment teams, portfolio companies, compliance, and investor relations while managing complex data collection processes, impact measurement frameworks (IRIS+, IMP), and stewardship activities. The scale of data management is enormous - tracking hundreds of KPIs across dozens of portfolio companies, managing TCFD climate risk assessments, and preparing comprehensive sustainability reports for LPs who increasingly demand transparency on ESG performance.

## Value Driver Mapping

| Value Driver | Relevance | Why It Resonates |
|-------------|-----------|------------------|
| **Replace or Radically Augment Headcount** | **High** | ESG data collection, monitoring, and reporting currently requires extensive manual work across analyst teams. AI can handle 24/7 portfolio company ESG monitoring, automated due diligence report generation, and continuous impact measurement |
| **Consolidate Tech Stack with AI** | **High** | Teams currently juggle 8-12 tools: ESG data vendors, survey platforms, carbon calculators, due diligence templates, reporting dashboards, and LP reporting tools. Single AI platform can replace most |
| **Scale Impact Without Overhead** | **High** | As funds grow AUM and portfolio size, sustainability monitoring complexity grows exponentially. AI enables managing 2x-5x more investments without proportional team growth |

## Prioritized Use Cases

---

### Use Case 1: Automated ESG Due Diligence & Risk Assessment

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
ESG due diligence currently requires 40-80 hours per deal, with analysts manually collecting data across 15+ ESG frameworks, conducting TCFD climate risk assessments, and preparing comprehensive reports. This creates bottlenecks during deal execution, inconsistent risk assessment quality, and delayed investment committee decisions. The manual process also increases greenwashing risk as inconsistencies in data collection and analysis can lead to misclassified investments under SFDR Article 8/9 requirements.

#### The Solution
monday.com AI agents automatically ingest target company data, conduct standardized ESG assessments using UNPRI frameworks, perform automated TCFD climate risk analysis, and generate comprehensive due diligence reports. The unified mondayDB context layer connects deal pipeline data with ESG assessments, enabling real-time risk scoring and automated escalation of high-risk investments.

#### The Outcome
- 70% reduction in due diligence time (from 60 to 18 hours per deal)
- 95% consistency in ESG risk assessment across all deals
- 50% faster investment committee decision-making
- Eliminated greenwashing risk through standardized SFDR classification

#### Discovery Questions
1. How many hours does your team currently spend on ESG due diligence per deal, and what's your typical deal flow?
2. How do you ensure consistency in ESG risk assessment across different investment teams and sectors?
3. What's your current process for TCFD climate risk assessment, and how do you integrate findings into investment decisions?
4. How are you managing SFDR Article 8/9 classification requirements and avoiding greenwashing risk?
5. What percentage of deals get delayed due to incomplete ESG due diligence?

#### Industry Context
ESG due diligence in VC/PE requires deep expertise in sector-specific risks, regulatory frameworks (SFDR, TCFD), and impact measurement methodologies. Teams must balance thoroughness with speed, as lengthy due diligence can kill competitive deals. The stakes are particularly high for Article 8/9 funds where misclassification can result in regulatory penalties and LP redemptions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an ESG Due Diligence tracking board with these columns: Deal Name (text), Target Company (text), Investment Team Lead (person), ESG Analyst (person), Due Diligence Stage (status: Not Started, Data Collection, Analysis, Risk Assessment, Report Draft, Final Review, Complete), ESG Risk Score (rating 1-5), Climate Risk Level (status: Low, Medium, High, Critical), SFDR Classification (dropdown: Article 6, Article 8, Article 9, Under Review), Key ESG Issues (long text), Mitigation Strategies (long text), Due Date (date), Hours Spent (numbers), and Status (status: On Track, At Risk, Delayed, Complete). Add a Timeline view for tracking deadlines and a Dashboard view showing ESG risk distribution. Set up automation to notify Investment Team Lead when ESG Risk Score is 4-5 or Climate Risk is Critical."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Due Diligence Agent

**Agent Purpose:**  
Autonomously conducts comprehensive ESG due diligence and generates standardized risk assessment reports for target investments.

**Triggers:**
- New deal added to pipeline with target company identified
- ESG due diligence stage changed to "Data Collection"
- Target company publicly files new sustainability/ESG reports
- Regulatory framework updates (SFDR, TCFD requirements)
- Manual invocation by investment team

**Actions:**
- Research target company's ESG policies, certifications, and track record
- Conduct automated TCFD climate risk assessment based on sector and geography
- Generate ESG risk score using UNPRI framework criteria
- Create preliminary SFDR Article 8/9 classification recommendation
- Identify sector-specific ESG red flags and mitigation opportunities
- Generate comprehensive due diligence report with executive summary

**Data Required:**
- Target company information (sector, geography, size)
- Public ESG data sources and regulatory databases
- Internal ESG risk assessment frameworks
- Historical due diligence reports for benchmarking

**Autonomy Level:** Human-in-the-Loop
Analysis and initial recommendations are fully automated, but final risk scores and SFDR classifications require analyst review and approval for regulatory compliance.

**Example Interaction:**
> The ESG Due Diligence Agent detects that TechCorp, a Series B SaaS company, has been added to the pipeline. It automatically begins data collection, identifying that TechCorp operates in a low-climate-risk sector but has no formal DEI policies and limited supplier ESG standards. The agent generates a preliminary risk score of 3/5, flags the governance gaps, and recommends specific due diligence questions about diversity metrics and supply chain sustainability. It creates a draft report highlighting that while the company could qualify for Article 8 with proper ESG enhancements, current state suggests Article 6 classification. The analyst reviews these findings, approves the recommendations, and uses the agent's analysis to structure investor discussions around ESG value creation opportunities.

---

### Use Case 2: Portfolio Company ESG KPI Monitoring & Improvement Tracking

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Monitoring ESG performance across 30-50 portfolio companies requires quarterly data collection via surveys, manual consolidation of different reporting formats, and creation of individual improvement roadmaps. This process takes 200+ hours per quarter, produces inconsistent data quality, and provides limited real-time insights for portfolio company support. LPs increasingly demand portfolio-level ESG performance dashboards, creating additional reporting burden.

#### The Solution
Centralized ESG monitoring platform with automated data collection from portfolio companies, standardized IRIS+ impact measurement, real-time ESG KPI dashboards, and AI-driven improvement recommendations. Integration with portfolio company systems enables continuous monitoring rather than quarterly snapshots.

#### The Outcome
- 80% reduction in quarterly monitoring time (from 200 to 40 hours)
- 100% data collection compliance across portfolio
- Real-time ESG performance insights and trend analysis
- Proactive portfolio company support through AI-recommended interventions

#### Discovery Questions
1. How many portfolio companies do you currently monitor for ESG performance, and what's your data collection process?
2. What percentage of your portfolio companies provide timely, complete ESG data each quarter?
3. How do you identify which portfolio companies need the most ESG support and intervention?
4. What ESG metrics do your LPs require in quarterly reports, and how long does report preparation take?
5. How do you track the ROI of ESG improvements across your portfolio?

#### Industry Context
Portfolio ESG monitoring is critical for SFDR compliance, LP reporting, and value creation. Different portfolio companies use different systems and metrics, making standardization challenging. The most successful funds view ESG monitoring as an active value creation tool, not just compliance reporting.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Portfolio ESG Monitoring board with these columns: Portfolio Company (text), Sector (dropdown: Tech, Healthcare, Financial Services, Consumer, Industrial), ESG Champion (person), Last Data Collection (date), Carbon Footprint tCO2e (numbers), Diversity Score % (numbers), Employee Satisfaction (rating 1-5), ESG Improvement Status (status: Excellent, On Track, Needs Attention, Critical), Priority ESG Issues (tags), Improvement Roadmap (long text), Next Review Date (date), LP Reporting Status (status: Complete, In Progress, Missing Data). Add a Dashboard view showing ESG performance across the portfolio and Kanban view grouped by ESG Improvement Status. Set up automation to notify ESG Champion when Next Review Date is approaching and when status changes to Critical."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Portfolio ESG Monitor

**Agent Purpose:**  
Continuously monitors ESG performance across portfolio companies and proactively identifies improvement opportunities and risks.

**Triggers:**
- Quarterly ESG data submission from portfolio companies
- ESG KPI threshold breaches (carbon footprint increase >20%, diversity score drop >10 points)
- Time-based triggers for regular portfolio reviews
- External ESG incidents or news about portfolio companies
- LP reporting deadlines approaching

**Actions:**
- Consolidate and validate ESG data across portfolio companies
- Calculate portfolio-level ESG performance metrics
- Identify portfolio companies requiring intervention or support
- Generate ESG improvement recommendations based on peer benchmarks
- Create automated LP reporting dashboards and summaries
- Alert team to regulatory compliance risks or opportunities

**Data Required:**
- Portfolio company ESG data feeds
- Industry benchmarking data
- Historical ESG performance trends
- LP reporting requirements and templates
- ESG improvement best practices database

**Autonomy Level:** Fully Autonomous
Routine monitoring, data consolidation, and reporting are fully automated. Human intervention only required for strategic ESG improvement decisions or LP communication.

**Example Interaction:**
> The Portfolio ESG Monitor detects that three portfolio companies in the industrial sector have reported 15-25% increases in carbon emissions this quarter, while peer companies show stable or declining emissions. It automatically benchmarks these companies against sector standards, identifies specific carbon reduction strategies that have worked for similar companies, and creates individualized improvement roadmaps. The agent generates alerts for the sustainability team highlighting this trend as a potential portfolio-level risk and recommends scheduling working sessions with the CFOs of these companies. It also updates the LP reporting dashboard to show the impact on portfolio-level net-zero commitments and suggests messaging for the next LP update.

---

### Use Case 3: SFDR Article 8/9 Compliance & Documentation Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
SFDR compliance requires maintaining detailed documentation for every investment decision, tracking sustainable investment percentages, and producing periodic reports. Teams currently use separate systems for investment tracking, ESG documentation, and regulatory reporting, creating version control issues and compliance gaps. Manual compliance checking increases risk of regulatory violations and potential penalties.

#### The Solution
Integrated SFDR compliance platform within monday.com that automatically tracks sustainable investment classifications, maintains required documentation, generates regulatory reports, and provides real-time compliance dashboards. AI continuously monitors classification accuracy and flags potential greenwashing risks.

#### The Outcome
- 100% SFDR compliance with automated documentation
- 90% reduction in regulatory reporting preparation time
- Zero compliance violations or reclassification requirements
- Streamlined fund marketing with verified sustainability claims

#### Discovery Questions
1. How are you currently tracking and documenting SFDR Article 8/9 investment criteria and decisions?
2. What percentage of your fund qualifies as sustainable investments, and how do you verify this classification?
3. How much time does your team spend on SFDR periodic reporting and regulatory documentation?
4. Have you had any challenges with SFDR compliance or requests for reclassification from regulators?
5. How do you ensure consistency between fund marketing materials and actual SFDR compliance data?

#### Industry Context
SFDR compliance is make-or-break for European funds and increasingly important for US funds raising from European LPs. The regulation requires extensive documentation that most funds handle manually, creating significant compliance risk. Wrong classifications can result in regulatory action and LP redemptions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an SFDR Compliance Management board with these columns: Investment Name (text), Fund (dropdown: Fund I, Fund II, Fund III), SFDR Classification (status: Article 6, Article 8, Article 9, Under Review, Reclassification Needed), Sustainable Investment % (numbers), Principal Adverse Impact Tracking (status: Compliant, Needs Review, Non-Compliant), Documentation Status (status: Complete, Missing Items, Under Review), Due Diligence Evidence (file), Periodic Review Date (date), Compliance Officer (person), Regulatory Risk Level (rating 1-5). Add a Dashboard view showing SFDR classification distribution and compliance status, plus a Calendar view for review dates. Set up automation to notify Compliance Officer 30 days before Periodic Review Date and when Regulatory Risk Level is 4-5."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SFDR Compliance Guardian

**Agent Purpose:**  
Ensures continuous SFDR compliance by monitoring investment classifications, maintaining documentation, and generating regulatory reports.

**Triggers:**
- New investment decision logged in system
- Changes to investment thesis or strategy
- SFDR regulation updates from regulatory feeds
- Periodic review date approaching
- External audit or regulatory inquiry received

**Actions:**
- Validate SFDR classification based on investment characteristics
- Generate and maintain required SFDR documentation packages
- Monitor sustainable investment percentage thresholds
- Create periodic regulatory reports and submissions
- Flag potential greenwashing risks or classification changes
- Update compliance dashboards and LP reporting materials

**Data Required:**
- Investment decision records and documentation
- ESG due diligence findings and ongoing monitoring data
- SFDR regulatory requirements and updates
- Fund classification criteria and thresholds
- Historical compliance audit trails

**Autonomy Level:** Escalation-Based
Routine compliance monitoring and documentation is fully automated, but classification changes or regulatory responses require human approval before submission.

**Example Interaction:**
> The SFDR Compliance Guardian continuously monitors the fund's Article 8 classification and detects that recent investments have reduced the sustainable investment percentage from 75% to 68%, approaching the minimum threshold. It automatically generates an alert to the compliance team, creates a detailed analysis showing which investments contributed to the decline, and recommends specific actions: either adjust the classification criteria for recent investments or consider reclassifying the fund to maintain compliance. The agent prepares draft documentation for both scenarios and schedules a compliance review meeting. When the team decides to adjust criteria for two investments based on enhanced ESG commitments, the agent updates all related documentation and regulatory filings automatically.

---

### Use Case 4: Impact Measurement & SDG Alignment Reporting

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Impact measurement using frameworks like IRIS+ and IMP requires extensive data collection, complex calculations, and manual SDG alignment mapping. Current process involves quarterly surveys to portfolio companies, manual data validation, and creation of impact reports that take 80+ hours per reporting period. Inconsistent measurement methodologies make it difficult to aggregate portfolio-level impact and demonstrate value to impact-focused LPs.

#### The Solution
Automated impact measurement platform using IRIS+ standards with direct portfolio company integrations, AI-powered SDG alignment analysis, and real-time impact dashboards. System automatically collects relevant metrics, applies appropriate measurement frameworks, and generates comprehensive impact reports.

#### The Outcome
- 85% reduction in impact reporting time (from 80 to 12 hours quarterly)
- Standardized impact measurement across entire portfolio
- Real-time impact tracking and trend analysis
- Enhanced LP confidence through transparent, consistent impact reporting

#### Discovery Questions
1. What impact measurement frameworks do you currently use, and how do you collect data from portfolio companies?
2. How do you map your investments to specific SDGs, and what evidence do you provide to LPs?
3. How much time does your team spend on impact measurement and reporting each quarter?
4. What challenges do you face in aggregating impact data across your portfolio?
5. How do your LPs evaluate the quality and credibility of your impact reporting?

#### Industry Context
Impact measurement is increasingly important for differentiation in the competitive VC/PE landscape. LPs, particularly institutional investors and sovereign wealth funds, require detailed impact reporting using recognized frameworks. The challenge is balancing measurement rigor with practical data collection from busy portfolio companies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an Impact Measurement Dashboard with these columns: Portfolio Company (text), Primary SDG (dropdown: SDG 1-17), Secondary SDGs (tags), IRIS+ Metrics Collected (tags), Impact Theme (dropdown: Climate, Education, Healthcare, Financial Inclusion, Economic Development), Social Impact Score (numbers), Environmental Impact Score (numbers), Measurement Status (status: Complete, In Progress, Incomplete, Validation Needed), Last Update (date), Impact Champion (person), LP Reporting Priority (rating 1-5). Add a Dashboard view showing impact distribution across SDGs and a Chart view for impact trend analysis. Set up automation to notify Impact Champion when Measurement Status is Incomplete for more than 30 days and when LP Reporting Priority is 4-5."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Impact Measurement Engine

**Agent Purpose:**  
Automatically measures and reports portfolio impact using IRIS+ standards and SDG alignment methodologies.

**Triggers:**
- New impact data received from portfolio companies
- Quarterly impact reporting deadlines
- Changes in portfolio company business models affecting impact
- LP requests for specific impact analysis
- Annual impact report preparation periods

**Actions:**
- Collect and validate impact data using IRIS+ framework standards
- Calculate portfolio-level impact metrics and trends
- Map investments to relevant SDGs with supporting evidence
- Generate automated impact reports and visualizations
- Benchmark portfolio impact against industry standards
- Create LP-ready impact summaries and presentations

**Data Required:**
- Portfolio company operational and financial data
- IRIS+ metric definitions and calculation methodologies
- SDG framework and alignment criteria
- Industry impact benchmarking data
- LP impact reporting requirements and preferences

**Autonomy Level:** Human-in-the-Loop
Data collection and calculation are fully automated, but impact narrative development and LP communication require human review and customization.

**Example Interaction:**
> The Impact Measurement Engine automatically processes quarterly data from a healthcare portfolio company and calculates that the company has provided affordable healthcare access to 45,000 additional patients this quarter, representing a 23% increase. It maps this to SDG 3 (Good Health and Well-being) and calculates the social impact score using IRIS+ methodologies. The agent compares this performance to healthcare industry benchmarks and identifies that this company is in the top decile for patient access expansion. It generates a detailed impact profile highlighting the company's contribution to portfolio-level SDG 3 achievement and prepares a summary for the upcoming LP report, noting that this single investment has reached 15% of the fund's total healthcare access target for the year.

---

### Use Case 5: Carbon Footprint Tracking & Net-Zero Portfolio Management

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Tracking carbon footprint across portfolio requires collecting Scope 1, 2, and 3 emissions data from dozens of companies using different measurement standards and tools. Current manual process takes 120+ hours quarterly, produces inconsistent data quality, and makes it difficult to track progress toward net-zero commitments. Many portfolio companies lack sophisticated carbon tracking capabilities, requiring extensive guidance and support.

#### The Solution
Integrated carbon tracking platform with automated data collection from portfolio companies, standardized carbon accounting methodologies, real-time emissions dashboards, and AI-recommended decarbonization strategies. System handles different company maturity levels from basic estimation to sophisticated Scope 3 tracking.

#### The Outcome
- 75% reduction in carbon tracking time (from 120 to 30 hours quarterly)
- 95% portfolio company participation in carbon reporting
- Clear net-zero pathway with milestone tracking
- Portfolio-level carbon reduction of 30% over 3 years through AI-recommended strategies

#### Discovery Questions
1. How do you currently track carbon footprint across your portfolio, and what percentage of companies provide complete data?
2. What net-zero commitments has your fund made, and how are you measuring progress?
3. How much support do your portfolio companies need to implement carbon tracking and reduction strategies?
4. What carbon accounting standards do you use, and how do you handle Scope 3 emissions tracking?
5. How important is carbon performance to your LPs, and what reporting do they require?

#### Industry Context
Net-zero commitments are becoming standard for institutional VC/PE funds, driven by LP requirements and regulatory pressure. The challenge is that portfolio companies often lack carbon tracking infrastructure, requiring funds to provide significant support and guidance. Carbon performance is increasingly linked to fund performance and LP retention.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Carbon Footprint Management board with these columns: Portfolio Company (text), Industry Sector (dropdown: Technology, Manufacturing, Services, Healthcare, Consumer), Carbon Baseline Year (date), Current Year Emissions tCO2e (numbers), Scope 1 Emissions (numbers), Scope 2 Emissions (numbers), Scope 3 Tracking Status (status: Not Started, In Progress, Partial, Complete), Net-Zero Target Year (date), Decarbonization Plan Status (status: Not Started, In Development, Approved, Implementation, Achieved), Last Carbon Update (date), Sustainability Lead (person), Reduction Progress % (numbers). Add a Dashboard view for portfolio carbon performance and Timeline view for net-zero targets. Set up automation to notify Sustainability Lead when Last Carbon Update is older than 90 days and when companies are off-track for net-zero targets."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Carbon Intelligence Agent

**Agent Purpose:**  
Tracks portfolio carbon performance and proactively recommends decarbonization strategies to achieve net-zero targets.

**Triggers:**
- New carbon data submitted by portfolio companies
- Monthly net-zero progress reviews
- Identification of companies exceeding carbon budgets
- Carbon reduction best practices identified in market
- LP requests for portfolio carbon performance analysis

**Actions:**
- Consolidate and validate carbon data across portfolio companies
- Calculate portfolio-level carbon performance against net-zero targets
- Identify highest-impact decarbonization opportunities
- Recommend specific carbon reduction strategies based on company profiles
- Generate carbon performance reports and trend analysis
- Alert team to companies requiring immediate carbon reduction support

**Data Required:**
- Portfolio company carbon emissions data (Scope 1, 2, 3)
- Industry carbon reduction benchmarks and best practices
- Net-zero commitment timelines and targets
- Carbon reduction technology and strategy databases
- LP reporting requirements for carbon performance

**Autonomy Level:** Fully Autonomous
Carbon tracking, analysis, and recommendation generation are fully automated. Human intervention only needed for strategic decisions about carbon reduction investments or portfolio company support.

**Example Interaction:**
> The Carbon Intelligence Agent detects that three manufacturing portfolio companies have reported 10-15% increases in carbon emissions this quarter due to production scale-up, threatening the fund's net-zero trajectory. It automatically analyzes the root causes, identifies that the increases are primarily Scope 2 emissions from increased energy usage, and researches renewable energy procurement options specific to each company's geography. The agent generates customized decarbonization recommendations including renewable energy contracts, energy efficiency upgrades, and carbon offset strategies. It calculates the cost and timeline for each option, models the impact on net-zero targets, and prepares a portfolio company engagement plan for the sustainability team to implement within 30 days.

---

### Use Case 6: Stewardship & Engagement Activity Management

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Managing stewardship activities across portfolio companies involves tracking board meetings, ESG engagement sessions, proxy voting, and collaborative engagement initiatives. Currently handled through spreadsheets and email chains, leading to missed follow-ups, inconsistent documentation, and difficulty demonstrating stewardship impact to regulators and LPs who increasingly scrutinize active ownership activities.

#### The Solution
Centralized stewardship platform tracking all engagement activities, automated follow-up scheduling, comprehensive documentation, and impact measurement of stewardship activities. Integration with calendar systems and portfolio company communication channels ensures complete activity tracking.

#### The Outcome
- 60% improvement in engagement follow-up consistency
- Complete stewardship activity documentation for regulatory compliance
- 40% increase in successful ESG improvement implementations through better tracking
- Streamlined UNPRI stewardship reporting and LP communication

#### Discovery Questions
1. How do you currently track and document stewardship activities across your portfolio?
2. What percentage of your ESG engagement recommendations actually get implemented by portfolio companies?
3. How do you measure the impact of your stewardship activities for UNPRI reporting?
4. What tools do you use to manage proxy voting and collaborative engagement initiatives?
5. How much time does stewardship documentation and reporting take each quarter?

#### Industry Context
Stewardship is a core requirement for UNPRI signatories and increasingly important for regulatory compliance. LPs evaluate funds based on stewardship effectiveness, not just activities. The key is demonstrating measurable impact from engagement efforts rather than just tracking activities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Stewardship Activities board with these columns: Portfolio Company (text), Engagement Type (dropdown: Board Meeting, ESG Discussion, Proxy Vote, Collaborative Engagement, Policy Advocacy), Engagement Date (date), Key Topics (tags), Attendees (people), Action Items (long text), Follow-up Date (date), Implementation Status (status: Proposed, Agreed, In Progress, Completed, Rejected), Impact Measurement (long text), UNPRI Category (dropdown: Strategy & Governance, Listed Equity, Fixed Income, Private Equity, Real Estate), Next Engagement (date). Add a Calendar view for scheduling engagements and Dashboard view showing stewardship impact. Set up automation to notify engagement owner 1 week before Follow-up Date and when Implementation Status changes to Completed."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Stewardship Coordinator

**Agent Purpose:**  
Manages comprehensive stewardship activities and ensures consistent follow-up on ESG engagement initiatives across the portfolio.

**Triggers:**
- Scheduled stewardship meetings or engagement deadlines
- Portfolio company ESG performance changes requiring engagement
- Regulatory or industry ESG issues affecting portfolio companies
- Annual UNPRI stewardship reporting periods
- Collaborative engagement opportunities identified

**Actions:**
- Schedule and coordinate stewardship meetings with portfolio companies
- Track implementation of ESG improvement commitments
- Generate stewardship impact reports and documentation
- Identify opportunities for collaborative engagement with other investors
- Maintain comprehensive records for UNPRI and regulatory reporting
- Create stewardship effectiveness analysis and recommendations

**Data Required:**
- Portfolio company ESG performance data
- Engagement history and outcomes
- Industry ESG issues and regulatory developments
- UNPRI stewardship reporting requirements
- Collaborative engagement opportunities database

**Autonomy Level:** Human-in-the-Loop
Meeting scheduling and documentation are automated, but engagement strategy and key decision communications require human oversight.

**Example Interaction:**
> The Stewardship Coordinator identifies that a portfolio company in the retail sector has missed its diversity targets for two consecutive quarters and schedules a stewardship discussion with the CEO and CHRO. It automatically prepares an engagement brief highlighting specific diversity improvement strategies that have worked for similar portfolio companies, draft action items with timelines, and follow-up milestones. After the meeting, it captures the agreed commitments (hire diversity-focused recruiting firm, implement unconscious bias training, set diverse interview panel requirements), schedules quarterly check-ins, and begins tracking implementation progress. The agent alerts the team when the company successfully implements the recruiting firm partnership ahead of schedule, documenting this as a positive stewardship outcome for UNPRI reporting.

---

### Use Case 7: ESG Data Collection & Validation from Portfolio Companies

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Collecting ESG data from portfolio companies involves managing multiple survey cycles, chasing non-responsive companies, validating data quality, and reconciling different reporting standards. Process requires 150+ hours quarterly across the team, with significant data quality issues and incomplete responses that compromise regulatory reporting and LP presentations.

#### The Solution
Automated ESG data collection platform with intelligent survey distribution, real-time response tracking, automated data validation, and escalation management for non-responsive companies. AI-powered data quality checking identifies inconsistencies and requests clarifications automatically.

#### The Outcome
- 80% reduction in data collection management time (from 150 to 30 hours quarterly)
- 95% portfolio company response rate through automated follow-up
- 90% improvement in data quality through AI validation
- Real-time ESG data availability for decision-making and reporting

#### Discovery Questions
1. How do you currently collect ESG data from portfolio companies, and what's your typical response rate?
2. How much time does your team spend chasing companies for incomplete or late ESG data submissions?
3. What data quality issues do you encounter, and how do you validate ESG metrics?
4. How do you handle different reporting standards and formats across portfolio companies?
5. What percentage of your ESG data collection process could be automated without losing quality?

#### Industry Context
ESG data collection is a massive operational challenge for funds with large portfolios. Portfolio companies often view ESG reporting as burdensome, leading to poor response rates and data quality. The key is balancing comprehensive data collection with minimal portfolio company burden while maintaining data integrity for regulatory compliance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an ESG Data Collection Management board with these columns: Portfolio Company (text), Survey Type (dropdown: Quarterly ESG, Annual Impact, Climate Data, DEI Metrics, Governance Review), Survey Sent Date (date), Response Due Date (date), Response Status (status: Not Sent, Sent, Partial Response, Complete, Overdue, Validated), Data Quality Score (rating 1-5), Missing Data Points (tags), Follow-up Count (numbers), Assigned Analyst (person), Portfolio Company Contact (person), Last Contact Date (date), Validation Status (status: Pending, Approved, Requires Clarification, Rejected). Add a Calendar view for due dates and Dashboard view showing collection progress. Set up automation to send follow-up when Response Status is Overdue for 7 days and notify Assigned Analyst when Data Quality Score is below 3."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ESG Data Orchestrator

**Agent Purpose:**  
Automates end-to-end ESG data collection process from portfolio companies with intelligent follow-up and data validation.

**Triggers:**
- Quarterly/annual ESG data collection cycles
- Data submission deadlines approaching
- Incomplete or low-quality data submissions received
- Portfolio company requests for data clarification
- Regulatory reporting deadlines requiring complete data

**Actions:**
- Distribute customized ESG surveys to portfolio companies
- Automatically follow up with non-responsive companies using escalation protocols
- Validate data quality and flag inconsistencies for review
- Request clarifications for missing or questionable data points
- Consolidate validated data into reporting-ready formats
- Generate data collection performance reports and bottleneck analysis

**Data Required:**
- Portfolio company contact information and preferences
- Historical ESG data for validation benchmarks
- Survey templates for different ESG metrics and frameworks
- Data quality rules and validation criteria
- Escalation protocols for non-responsive companies

**Autonomy Level:** Escalation-Based
Survey distribution, follow-up communications, and basic validation are fully automated. Human intervention required only for complex data quality issues or escalation to portfolio company executives.

**Example Interaction:**
> The ESG Data Orchestrator launches the quarterly ESG survey to 45 portfolio companies and begins tracking responses. After one week, it identifies 12 companies that haven't responded and automatically sends personalized follow-up emails based on each company's historical response patterns. For companies with previous late submissions, it escalates directly to CFO level; for typically responsive companies, it sends friendly reminders to sustainability contacts. When TechCorp submits data showing a 400% increase in carbon emissions, the agent flags this as highly unusual, cross-references with previous submissions and industry benchmarks, and automatically requests clarification with specific questions about methodology changes. It alerts the analyst to review the response personally and holds the data from regulatory reports until validation is complete.

---

### Use Case 8: DEI Metrics Tracking & Improvement Planning

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Tracking diversity, equity, and inclusion metrics across portfolio companies involves collecting sensitive data, ensuring privacy compliance, benchmarking against industry standards, and developing tailored improvement plans. Manual process is time-intensive and difficult to scale, while inconsistent measurement makes it challenging to demonstrate portfolio-level DEI progress to LPs and stakeholders.

#### The Solution
Comprehensive DEI tracking platform with automated data collection, privacy-compliant storage, industry benchmarking, and AI-generated improvement recommendations. System provides portfolio-level DEI analytics while maintaining individual company confidentiality and regulatory compliance.

#### The Outcome
- 70% reduction in DEI data management time
- Standardized DEI measurement across entire portfolio
- 25% average improvement in portfolio company DEI scores through targeted interventions
- Enhanced LP satisfaction through transparent DEI progress reporting

#### Discovery Questions
1. What DEI metrics do you currently track across your portfolio, and how do you collect this sensitive data?
2. How do you benchmark DEI performance and identify companies needing the most support?
3. What privacy and confidentiality requirements do you need to meet for DEI data handling?
4. How important is DEI performance to your LPs, and what reporting do they expect?
5. What challenges do you face in getting portfolio companies to engage seriously with DEI improvement initiatives?

#### Industry Context
DEI tracking has become critical for VC/PE funds, driven by LP requirements and regulatory pressure. The challenge is balancing comprehensive measurement with privacy requirements while providing meaningful support to portfolio companies. DEI performance is increasingly linked to fund marketing and LP retention, particularly for institutional investors.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a DEI Performance Tracking board with these columns: Portfolio Company (text), Industry Sector (dropdown), Employee Count Range (dropdown: <50, 50-200, 200-500, 500+), Leadership Diversity % (numbers), Board Diversity % (numbers), Overall Workforce Diversity % (numbers), Pay Equity Status (status: Compliant, Under Review, Gaps Identified, Improvement Plan), DEI Program Maturity (rating 1-5), Improvement Priority (status: Low, Medium, High, Critical), DEI Champion (person), Last Assessment Date (date), Next Review Date (date), Confidentiality Level (dropdown: Standard, High, Restricted). Add a Dashboard view showing portfolio DEI performance trends while maintaining company confidentiality. Set up automation to notify DEI Champion 30 days before Next Review Date and when Improvement Priority is High or Critical."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DEI Progress Navigator

**Agent Purpose:**  
Tracks DEI performance across the portfolio and generates tailored improvement strategies while maintaining strict data confidentiality.

**Triggers:**
- Annual DEI assessment cycles
- Quarterly DEI data updates from portfolio companies
- Significant changes in company leadership or board composition
- Industry DEI benchmarking data updates
- LP requests for portfolio DEI performance analysis

**Actions:**
- Collect and securely store DEI metrics with appropriate privacy controls
- Benchmark DEI performance against industry and peer standards
- Identify portfolio companies requiring DEI improvement support
- Generate customized DEI improvement recommendations and resources
- Track progress on DEI improvement initiatives across the portfolio
- Create aggregated DEI reports for LP communication while maintaining confidentiality

**Data Required:**
- Portfolio company DEI metrics and demographic data
- Industry DEI benchmarking standards
- DEI best practices and improvement strategy databases
- Privacy and confidentiality requirements for sensitive data
- LP DEI reporting requirements and expectations

**Autonomy Level:** Human-in-the-Loop
Data collection and analysis are automated, but DEI improvement strategies and portfolio company communications require human review to ensure cultural sensitivity and effectiveness.

**Example Interaction:**
> The DEI Progress Navigator processes annual DEI data and identifies that the portfolio's technology companies average 18% leadership diversity compared to 28% industry benchmark, indicating a significant gap. It automatically generates company-specific improvement recommendations: for early-stage companies, it suggests diverse hiring partnerships and unconscious bias training; for growth-stage companies, it recommends board diversity initiatives and mentorship programs. The agent creates a confidential portfolio DEI improvement plan highlighting that targeted interventions at five companies could bring the portfolio above industry average within 18 months. It prepares anonymized benchmark reports for LP communication while maintaining individual company confidentiality, and schedules quarterly progress reviews with portfolio company leaders who have committed to improvement initiatives.

---

## Industry Terminology

| Term | Definition |
|------|-------------|
| **ESG Due Diligence** | Systematic assessment of environmental, social, and governance risks and opportunities in potential investments |
| **UNPRI** | UN Principles for Responsible Investment - global framework for responsible investment practices |
| **SFDR** | Sustainable Finance Disclosure Regulation - EU regulation requiring transparency on sustainability risks and impacts |
| **IRIS+** | Impact measurement system providing standardized metrics for impact investing |
| **IMP** | Impact Management Project framework for measuring and managing impact |
| **TCFD** | Task Force on Climate-related Financial Disclosures - framework for climate risk reporting |
| **Article 8/9 Funds** | SFDR classification for funds promoting environmental/social characteristics (8) or sustainable investment objectives (9) |
| **Greenwashing** | Misleading claims about environmental benefits or sustainability of investments |
| **Impact Thesis** | Clear articulation of intended positive social/environmental outcomes from investments |
| **SDG Alignment** | Mapping investments to UN Sustainable Development Goals |
| **Stewardship** | Active engagement with portfolio companies to improve ESG performance |
| **Scope 1/2/3 Emissions** | Direct (1), indirect energy (2), and value chain (3) greenhouse gas emissions |
| **Net-Zero Portfolio** | Investment portfolio targeting carbon neutrality through emissions reduction and offsets |
| **Principal Adverse Impact** | Negative sustainability impacts that must be considered under SFDR |
| **Sustainability-Linked Financing** | Loans/bonds with terms tied to achievement of sustainability targets |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **Head of Sustainability/ESG** | Overall ESG strategy, LP relations, regulatory compliance | High - reports to Managing Partner |
| **ESG Analysts** | Data collection, due diligence, portfolio monitoring | Medium - supports investment decisions |
| **Portfolio Company Relations** | Engagement coordination, improvement planning | Medium - direct portfolio interface |
| **Compliance Officer** | Regulatory adherence, documentation, risk management | High - veto power on classifications |
| **Investment Partners** | ESG integration in deal evaluation and value creation | High - investment decision makers |
| **LP Relations** | Sustainability reporting, investor communications | Medium - stakeholder management |
| **Data Analysts** | ESG metrics, impact measurement, reporting systems | Low - technical support role |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|------------|-------------|
| **Investment Team** | ESG integration in deal sourcing and evaluation | Co-sell comprehensive deal management platform |
| **Portfolio Operations** | Value creation planning and portfolio company support | Expand into operational improvement tracking |
| **Compliance & Legal** | Regulatory requirements and documentation | Integrate regulatory workflow management |
| **Investor Relations** | LP reporting and stakeholder communication | Add LP communication and reporting tools |
| **Risk Management** | ESG risk assessment and monitoring | Consolidate all risk management activities |
| **Finance & Accounting** | Impact accounting and performance measurement | Connect ESG metrics to financial performance |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Sustainalytics/MSCI** | ESG data providers | "Why pay for data when you can have data + workflow + AI analysis?" |
| **Workiva/Certent** | ESG reporting platforms | "Replace static reporting with dynamic portfolio management" |
| **Diligent ESG** | Board-level ESG management | "Extend beyond boards to full portfolio operations" |
| **Bloomberg ESG** | Market data and analytics | "Move from market analysis to portfolio action" |
| **Custom Spreadsheets** | DIY tracking systems | "Graduate from spreadsheets to enterprise platform" |
| **Survey Tools (Qualtrics)** | Data collection only | "Why just collect data when AI can analyze and act on it?" |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"We have specialized ESG tools"** | "How much time do you spend moving data between systems? Our platform eliminates that overhead while adding AI capabilities your current tools lack." |
| **"ESG data is too sensitive for cloud platforms"** | "We provide enterprise-grade security with SOC 2 compliance. Your current email and survey tools likely have lower security standards than our platform." |
| **"Portfolio companies won't adopt another system"** | "They don't need to. Our system integrates with their existing workflows and actually reduces their reporting burden through automation." |
| **"We need industry-specific ESG expertise"** | "Our AI learns your specific frameworks and terminology. Plus you maintain full control over methodology while gaining operational efficiency." |
| **"ROI is unclear for ESG technology"** | "Calculate your team's time: 400+ hours quarterly on manual processes. Our platform reduces that by 75% while improving data quality and LP satisfaction." |
| **"Regulatory requirements are too complex"** | "That's exactly why you need automated compliance. Manual processes increase regulatory risk. Our platform ensures consistent documentation and reduces compliance errors." |

## Proof Points
*(To be populated with customer references)*

- Large North American PE fund reduced ESG due diligence time by 70% while improving consistency
- European VC fund achieved 100% SFDR compliance documentation through automated workflows  
- Impact-focused fund increased portfolio company ESG data collection rate from 60% to 95%
- Multi-billion fund consolidated 12 ESG tools into single AI-powered platform, saving $200K annually
- Sustainability team scaled from managing 25 to 60 portfolio companies without adding headcount

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*