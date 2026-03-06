# Architecture, Engineering & Design × Sales
## monday.com SE Playbook

### Industry Context

The Architecture, Engineering & Design (AEC) industry operates on relationship-driven business development cycles that can span months or years. Unlike traditional product sales, AEC "sales" is really business development focused on pursuit management, where principals and partners personally cultivate client relationships and lead capture efforts for high-value projects. The industry relies heavily on qualification processes like SF330s, go/no-go decision frameworks, and teaming arrangements with subconsultants and joint venture partners.

AEC firms face increasing pressure to improve hit rates on pursuits while managing lean BD teams that juggle multiple opportunities across government and private sectors. The shift toward design-build delivery methods and integrated project delivery has created more complex teaming requirements, while digital transformation demands better pipeline visibility and capture planning. Success depends on maintaining strong relationships with repeat clients who generate 60-80% of revenue, while systematically pursuing new opportunities through platforms like FedBizOpps and SAM.gov.

The department must balance relationship maintenance with systematic pursuit management, often struggling with fragmented tools for tracking client touchpoints, proposal deadlines, teaming partner coordination, and post-award project handoffs. With principals spending significant time on BD activities, efficiency gains in pipeline management and proposal coordination directly impact billable utilization and firm profitability.

### Department Profile
- **Typical Team Size:** 3-12 (varies by firm size: 2-3 in small firms, 8-12 in large firms)
- **Key Stakeholders:** Principals/Partners, BD Directors, Proposal Coordinators, Marketing Managers, Project Managers (for handoffs)
- **Core KPIs:** Hit rate (%), Pipeline value, Proposal win percentage, Repeat client revenue %, Time to shortlist, BD cost per win, Client satisfaction scores, Backlog months
- **Common Tools Replaced:** Excel spreadsheets, CRM systems (Salesforce, HubSpot), SharePoint, standalone proposal tools, email chains for team coordination

---

### Use Cases

#### Use Case 1: Government Pursuit Pipeline Management
**Pain Point:** BD teams lose track of opportunities across multiple government platforms (FedBizOpps, SAM.gov, state portals) with inconsistent go/no-go processes and missed pre-proposal conference deadlines.
**monday.com Solution:** Automated opportunity tracking board that pulls from government feeds, standardized go/no-go scoring matrix with stakeholder input, and milestone tracking for each pursuit phase.
**Key Boards/Workflows:** Government Opportunities board with custom fields for NAICS codes, set-aside categories, estimated fees; Go/No-Go Scoring board with weighted criteria; Pursuit Timeline board with automated deadline notifications.
**Vibe Prompt:** "Create a government contract pursuit tracker that monitors FedBizOpps and state opportunities for architectural and engineering services, with automated go/no-go scoring based on our past performance, team capacity, and client relationships, plus milestone tracking from opportunity identification through proposal submission."
**Agent Blueprint:** AI agent that monitors government opportunity feeds, automatically populates opportunity details, scores against firm criteria, sends stakeholder notifications for go/no-go decisions, and creates pursuit timelines with key deadlines.
**Value Driver:** Consolidate Tech Stack with AI
**Estimated Impact:** 25% reduction in missed opportunities, 15% improvement in pursuit hit rate through better qualification

#### Use Case 2: Teaming Partner & Subconsultant Coordination
**Pain Point:** Managing relationships and coordination with dozens of teaming partners and subconsultants across multiple pursuits, leading to missed teaming agreements and duplicated outreach efforts.
**monday.com Solution:** Centralized partner database with capability matrices, pursuit-specific teaming boards, and automated coordination workflows for teaming agreements and joint venture formations.
**Key Boards/Workflows:** Partner Capability Matrix with certifications and past performance; Active Teaming board linking partners to specific pursuits; Teaming Agreement Tracker with legal milestone management.
**Vibe Prompt:** "Build a teaming partner management system for AEC pursuits that tracks partner capabilities, certifications, and availability across multiple opportunities, with automated workflows for teaming agreement development and joint venture coordination for large government contracts."
**Agent Blueprint:** AI agent that matches optimal teaming partners based on opportunity requirements, tracks partner availability across pursuits, automates teaming agreement templates, and monitors joint venture compliance requirements.
**Value Driver:** Scale Impact Without Overhead
**Estimated Impact:** 40% faster teaming partner identification, 30% reduction in BD coordinator time spent on partner coordination

#### Use Case 3: Client Relationship & Repeat Business Management
**Pain Point:** Lost visibility into client touchpoints across multiple project teams leads to missed repeat opportunities and weakened client relationships that generate 60-80% of firm revenue.
**monday.com Solution:** Comprehensive client relationship dashboard tracking all touchpoints, project performance metrics, and systematic follow-up workflows to identify repeat opportunities.
**Key Boards/Workflows:** Client Master Database with project history and key contacts; Client Touchpoint Tracker logging all interactions; Repeat Opportunity Pipeline with relationship scoring.
**Vibe Prompt:** "Create a client relationship management system for architectural firms that tracks all client interactions across projects, monitors client satisfaction and project performance, and identifies repeat business opportunities based on relationship strength and upcoming client needs."
**Agent Blueprint:** AI agent that aggregates client touchpoints from project teams, analyzes client communication patterns to identify relationship risks, generates automated follow-up reminders, and scores repeat opportunity potential based on project history and satisfaction data.
**Value Driver:** Replace or Radically Augment Headcount
**Estimated Impact:** 20% increase in repeat client revenue, equivalent to 0.5 FTE BD coordinator through automated relationship management

#### Use Case 4: RFP/RFQ Response Coordination
**Pain Point:** Proposal development involves coordinating inputs from multiple technical leads, managing compliance matrices, and meeting tight deadlines while maintaining quality and consistency across responses.
**monday.com Solution:** Proposal management boards with automated task assignments, compliance tracking, and version control for collaborative proposal development with real-time status visibility.
**Key Boards/Workflows:** RFP Response Tracker with compliance matrix integration; Proposal Task Assignment with technical lead responsibilities; Document Version Control with automated backup and review cycles.
**Vibe Prompt:** "Design a proposal response management system for engineering consultants that breaks down RFP requirements into assignable tasks, tracks compliance against solicitation requirements, manages document versions and reviews, and ensures on-time submission with quality control checkpoints."
**Agent Blueprint:** AI agent that parses RFP documents to extract requirements and create task assignments, monitors compliance matrix completion, tracks document versions and reviewer feedback, and sends escalation alerts for missed deadlines.
**Value Driver:** Consolidate Tech Stack with AI
**Estimated Impact:** 35% reduction in proposal development time, 50% fewer compliance errors, improved proposal quality scores

#### Use Case 5: Capture Planning for Major Pursuits
**Pain Point:** Large pursuits ($10M+) require months of capture planning but lack systematic approaches to intelligence gathering, relationship mapping, and competitive positioning.
**monday.com Solution:** Comprehensive capture planning workspace with intelligence tracking, stakeholder mapping, and competitive analysis workflows integrated with opportunity timeline management.
**Key Boards/Workflows:** Capture Intelligence board tracking client meetings and competitive intel; Stakeholder Influence Map with relationship scoring; Capture Activity Timeline with milestone tracking and budget management.
**Vibe Prompt:** "Build a capture planning system for major AEC pursuits that tracks client intelligence gathering, maps stakeholder relationships and influence, monitors competitive positioning, and manages capture activities and budgets leading up to RFP release."
**Agent Blueprint:** AI agent that consolidates capture intelligence from team inputs, analyzes stakeholder relationship patterns, tracks competitor activities and win themes, and optimizes capture resource allocation based on opportunity scoring.
**Value Driver:** Scale Impact Without Overhead
**Estimated Impact:** 15% improvement in large pursuit win rate, $200K+ annual value per major win gained

#### Use Case 6: SF330 and Qualification Management
**Pain Point:** Managing multiple active SF330 submissions and maintaining current qualifications across team members while tracking which qualifications apply to specific opportunities.
**monday.com Solution:** Automated SF330 management system tracking submittal deadlines, team qualifications, and opportunity-specific requirements with centralized document repository.
**Key Boards/Workflows:** SF330 Submittal Tracker with agency-specific requirements; Team Qualifications Database with expiration tracking; Opportunity-Qualification Matching board.
**Vibe Prompt:** "Create an SF330 and qualification management system for government AEC contracts that tracks active submittals by agency, monitors team member certifications and qualifications, and matches appropriate qualifications to specific opportunities while maintaining current documentation."
**Agent Blueprint:** AI agent that monitors SF330 submission deadlines, tracks team qualification renewals, automatically matches relevant qualifications to opportunities, and generates alerts for expiring certifications or missing qualifications.
**Value Driver:** Replace or Radically Augment Headcount
**Estimated Impact:** Equivalent to 0.3 FTE administrative time savings, 90% reduction in missed SF330 deadlines

#### Use Case 7: Fee Proposal Development & Pricing Strategy
**Pain Point:** Developing competitive yet profitable fee proposals requires coordination across technical disciplines while maintaining pricing consistency and competitive intelligence tracking.
**monday.com Solution:** Fee development workspace with historical pricing data, competitor analysis, and collaborative pricing workflows with approval hierarchies and sensitivity analysis.
**Key Boards/Workflows:** Project Pricing Database with historical multipliers; Competitor Fee Intelligence tracker; Fee Proposal Review board with approval workflows and pricing rationale documentation.
**Vibe Prompt:** "Design a fee proposal development system for AEC firms that leverages historical project pricing data, tracks competitive fee intelligence, enables collaborative pricing across disciplines, and manages fee proposal approvals with pricing rationale and sensitivity analysis."
**Agent Blueprint:** AI agent that analyzes historical pricing patterns for similar projects, monitors competitive fee intelligence, suggests optimal pricing strategies based on opportunity factors, and tracks proposal pricing success rates for continuous improvement.
**Value Driver:** Consolidate Tech Stack with AI
**Estimated Impact:** 12% improvement in fee proposal win rate, 8% increase in average project profitability

#### Use Case 8: Pipeline Reporting & BD Performance Analytics
**Pain Point:** Partners lack real-time visibility into BD pipeline health, pursuit progress, and team performance metrics needed for strategic decision-making and resource allocation.
**monday.com Solution:** Executive BD dashboard with automated reporting on pipeline value, hit rates, team performance, and predictive analytics for revenue forecasting.
**Key Boards/Workflows:** Executive Pipeline Dashboard with real-time metrics; BD Performance Tracker with individual and team KPIs; Revenue Forecast Model with pipeline probability weighting.
**Vibe Prompt:** "Build a business development analytics dashboard for AEC firm leadership that provides real-time pipeline visibility, tracks BD team performance metrics, and generates revenue forecasts based on pursuit probability and historical win rates."
**Agent Blueprint:** AI agent that aggregates BD data across all pursuits, generates automated executive reports, identifies performance trends and risks, and provides predictive revenue modeling based on pipeline health and historical performance patterns.
**Value Driver:** Scale Impact Without Overhead
**Estimated Impact:** 25% improvement in BD resource allocation efficiency, 15% better revenue predictability for strategic planning

---

### Discovery Questions

1. "How do you currently track and qualify opportunities from government sources like FedBizOpps or SAM.gov, and what percentage of your pursuits come from government versus private clients?"

2. "Walk me through your go/no-go decision process – who's involved, what criteria do you use, and how do you ensure you're not chasing opportunities that don't fit your capabilities or strategic goals?"

3. "How do you manage relationships with teaming partners and subconsultants across multiple active pursuits, and what challenges do you face in coordinating joint venture agreements?"

4. "What's your current process for maintaining relationships with past clients and identifying repeat business opportunities – and what percentage of your revenue comes from repeat versus new clients?"

5. "How do you coordinate proposal development when RFPs come in, especially managing inputs from multiple technical disciplines while ensuring compliance and meeting tight deadlines?"

6. "For your largest opportunities, do you have a formal capture planning process, and how do you track competitive intelligence and stakeholder relationships during the pre-RFP phase?"

7. "How do you currently manage SF330 submittals and team qualifications, and have you ever missed opportunities due to expired certifications or overlooked qualification requirements?"

### Competitive Positioning

**vs. Salesforce/Traditional CRM:** monday.com's project-centric approach aligns naturally with AEC pursuit management, whereas traditional CRM systems are built for transactional sales cycles that don't match the complex, relationship-driven, proposal-heavy nature of AEC business development. Monday.com's visual workflow management and collaboration features better support the team-based nature of pursuit management.

**vs. Specialized AEC CRM (Deltek, NewStar):** While these tools offer industry-specific features, monday.com provides superior user experience, faster implementation, and better integration with modern collaboration tools. The AI capabilities and automation features in monday.com can provide equivalent functionality at a lower cost and complexity, with better adoption rates due to intuitive interface design.

**vs. Excel/SharePoint combinations:** monday.com eliminates the version control issues, limited collaboration capabilities, and manual update requirements that plague spreadsheet-based BD management systems. Automated workflows, real-time visibility, and integrated communication features provide substantial productivity gains over manual tracking systems.

**Key differentiator:** monday.com's ability to connect BD activities with project delivery creates seamless handoffs from pursuit to execution, providing end-to-end visibility that purpose-built BD tools cannot match.

### ROI Framework

**Primary Metrics:**
- **Hit Rate Improvement:** Baseline hit rate × improvement percentage × average project value × annual pursuit volume
- **Time Savings:** Hours saved per pursuit × hourly BD cost × annual pursuit volume  
- **Repeat Client Revenue:** Current repeat percentage × increase × total annual revenue

**Sample Calculation (50-person firm):**
- Current hit rate: 20% on 50 annual pursuits averaging $500K
- 15% hit rate improvement = 1.5 additional wins = $750K additional revenue
- 25% BD time savings on 200 hours/pursuit = 2,500 hours × $150/hour = $375K value
- 5% increase in repeat client revenue on $25M annual = $1.25M additional revenue
- **Total Annual Value:** $2.375M vs. monday.com investment of ~$50K = 47:1 ROI

**Supporting Metrics:**
- Reduction in missed opportunities and deadlines
- Improved proposal quality scores and client satisfaction
- Better resource allocation and capacity utilization
- Enhanced competitive positioning through better intelligence

### Quick Wins

1. **Government Opportunity Dashboard (Week 1):** Set up automated tracking of opportunities from FedBizOpps and state portals with basic filtering and notification workflows. Immediate visibility improvement for BD teams.

2. **Client Touchpoint Tracker (Week 1):** Deploy simple client interaction logging system with automated follow-up reminders. Quick wins in relationship management and repeat opportunity identification.

3. **Proposal Deadline Management (Week 2):** Implement RFP response timeline tracking with automated milestone notifications and team task assignments. Immediate reduction in missed deadlines and improved coordination.

4. **Teaming Partner Database (Week 3):** Create centralized partner capability matrix with search and filtering functionality. Fast improvement in teaming partner identification and coordination efficiency.