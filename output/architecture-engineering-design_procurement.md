# Architecture, Engineering & Design × Procurement
## monday.com SE Playbook

### Industry Context

Architecture, Engineering & Design (AEC) firms operate in a project-driven environment where procurement decisions directly impact project delivery, profitability, and client satisfaction. Unlike traditional procurement departments, AEC "procurement" is highly decentralized and deeply integrated with project workflows. Principals, project managers, and office managers typically handle purchasing decisions, from subconsultant selection to software licensing, often without formal procurement processes or dedicated staff.

The industry's procurement challenges are unique: subconsultant selection requires technical expertise evaluation, not just cost comparison; software licensing involves complex enterprise agreements with vendors like Autodesk, Adobe, and Bluebeam that must align with project needs and headcount fluctuations; office buildouts and equipment purchases must support creative workflows and collaboration; and insurance procurement (E&O, General Liability, Cyber) requires specialized coverage understanding. Most firms struggle with vendor prequalification, maintaining preferred vendor lists, tracking subconsultant agreements across projects, and managing the complex web of relationships between prime contracts, subconsultant agreements, and vendor relationships.

The trend toward larger, more complex projects and integrated project delivery methods (IPD, design-build) has intensified procurement complexity. Firms need systems that can handle both traditional purchasing and the sophisticated vendor relationship management required for successful project delivery, all while maintaining the flexibility and speed that AEC project timelines demand.

### Department Profile
- **Typical Team Size:** 0-2 dedicated procurement staff (most firms have none); purchasing distributed across 5-15 decision makers
- **Key Stakeholders:** Principals, Project Managers, Office Managers, IT Directors, Finance/Accounting, HR for benefits procurement
- **Core KPIs:** Subconsultant selection cycle time, software license utilization rates, vendor payment terms, insurance coverage gaps, office lease cost per SF, equipment uptime
- **Common Tools Replaced:** Excel spreadsheets, email chains, SharePoint folders, QuickBooks vendor management, separate systems for subconsultant prequalification

---

### Use Cases

#### Use Case 1: Subconsultant Selection & Onboarding
**Pain Point:** Project teams spend 2-4 weeks per project manually reaching out to structural, MEP, civil, landscape, and lighting consultants, comparing qualifications via email, and managing complex teaming agreements. No centralized system tracks consultant performance, availability, or prequalification status across projects.

**monday.com Solution:** Integrated subconsultant database with automated RFQ workflows, qualification tracking, and project-specific teaming dashboards. Performance data from previous projects automatically influences future selection decisions.

**Key Boards/Workflows:** 
- Subconsultant Database (contact info, specialties, prequalification status, performance ratings)
- Project RFQ Board (automated consultant outreach, proposal comparison, selection tracking)
- Teaming Agreement Tracker (contract status, insurance certificates, scope coordination)

**Vibe Prompt:** "Create a system to manage our structural, MEP, civil, landscape, and lighting subconsultant selection for each new project, including automated RFQ distribution, proposal comparison, and performance tracking from past projects"

**Agent Blueprint:** AI agent monitors project pipeline and proactively identifies subconsultant needs based on project type, automatically distributes RFQs to prequalified consultants, analyzes proposals against project requirements, and recommends optimal teaming combinations based on past performance data and current availability.

**Value Driver:** Replace or Radically Augment Headcount

**Estimated Impact:** Reduce subconsultant selection time by 60% (from 3 weeks to 1 week), improve subconsultant performance by 25% through data-driven selection, eliminate 40+ hours/month of manual coordination across project teams.

#### Use Case 2: Software License Portfolio Management
**Pain Point:** Managing Autodesk Enterprise agreements, Adobe Creative Cloud licenses, Bluebeam seats, and 20+ other software tools across fluctuating headcount and project needs. No visibility into license utilization, renewal dates, or cost optimization opportunities.

**monday.com Solution:** Centralized software asset management with usage analytics, renewal automation, and cost optimization recommendations based on actual utilization data.

**Key Boards/Workflows:**
- Software License Inventory (all licenses, seats, renewal dates, costs per user)
- Usage Analytics Dashboard (utilization rates, inactive licenses, optimization opportunities)
- Renewal Management Board (upcoming renewals, budget approvals, vendor negotiations)

**Vibe Prompt:** "Help me track and optimize all our software licenses including Autodesk, Adobe, Bluebeam, and others - I need to see utilization rates, manage renewals, and identify cost savings opportunities"

**Agent Blueprint:** AI agent continuously monitors software usage patterns, identifies underutilized licenses for reallocation or cancellation, automatically initiates renewal processes with budget approvals, and provides cost optimization recommendations based on project pipeline and headcount forecasts.

**Value Driver:** Consolidate Tech Stack with AI

**Estimated Impact:** Reduce software costs by 15-25% through optimization, eliminate 20 hours/month of manual license tracking, achieve 95% license utilization efficiency, automate 80% of routine renewal processes.

#### Use Case 3: Office Buildout & FF&E Management
**Pain Point:** Office relocations, expansions, and buildouts involve coordinating dozens of vendors (architects, contractors, furniture dealers, IT installers) while managing TI allowances, FF&E budgets, and project timelines. No centralized tracking leads to budget overruns and schedule delays.

**monday.com Solution:** Integrated office project management system tracking all vendors, budgets, timelines, and deliverables from lease negotiation through move-in.

**Key Boards/Workflows:**
- Office Project Master (timeline, budget, stakeholders, approvals)
- Vendor Coordination Board (all trades, contracts, schedules, deliverables)
- FF&E Tracking (furniture, fixtures, equipment procurement and installation)

**Vibe Prompt:** "Create a system to manage our office buildout project including coordinating contractors, furniture vendors, IT installation, and tracking our TI allowance and FF&E budget"

**Agent Blueprint:** AI agent orchestrates complex office project workflows, automatically updates stakeholders on progress, identifies potential scheduling conflicts, manages budget tracking against TI allowances, and coordinates final inspections and move-in logistics.

**Value Driver:** Scale Impact Without Overhead

**Estimated Impact:** Reduce office project delivery time by 30%, eliminate budget overruns through real-time tracking, save 50+ hours of project coordination per office project, improve vendor performance through structured feedback.

#### Use Case 4: Technology Hardware Procurement & Management
**Pain Point:** Procuring and managing high-performance workstations, plotters, 3D printers, and specialized equipment across multiple office locations. No standardized specs, inconsistent vendor relationships, and reactive maintenance approaches lead to productivity losses.

**Vibe Prompt:** "Set up a system to manage our technology equipment including workstation specs, plotter maintenance schedules, 3D printer supplies, and vendor relationships across our offices"

**monday.com Solution:** Equipment lifecycle management system with standardized configurations, preventive maintenance scheduling, and centralized vendor relationship management.

**Key Boards/Workflows:**
- Equipment Inventory (all devices, specs, locations, warranty status)
- Maintenance Schedule (preventive maintenance, service contracts, downtime tracking)
- Procurement Standards (approved vendors, standard configurations, cost benchmarks)

**Agent Blueprint:** AI agent monitors equipment performance and usage patterns, automatically schedules preventive maintenance, identifies replacement needs based on lifecycle analysis, and maintains optimal inventory levels for consumables like plotter paper and 3D printer materials.

**Value Driver:** Replace or Radically Augment Headcount

**Estimated Impact:** Reduce equipment downtime by 40%, standardize 90% of technology purchases, eliminate 25 hours/month of manual maintenance coordination, achieve 20% cost savings through consolidated purchasing.

#### Use Case 5: Insurance & Professional Services Procurement
**Pain Point:** Managing complex insurance renewals (E&O, General Liability, Cyber, Workers Comp) and professional service contracts (legal, accounting, HR) requires specialized knowledge and careful coordination with project requirements and firm growth.

**monday.com Solution:** Insurance and professional services management system with automated renewal workflows, coverage gap analysis, and vendor performance tracking.

**Key Boards/Workflows:**
- Insurance Portfolio (all policies, coverage amounts, renewal dates, claims history)
- Professional Services Tracker (legal, accounting, HR vendors and contracts)
- Compliance Dashboard (certificate tracking, coverage requirements by project)

**Vibe Prompt:** "Help me manage all our insurance policies including E&O, General Liability, and Cyber insurance, plus track our relationships with legal, accounting, and HR service providers"

**Agent Blueprint:** AI agent monitors insurance coverage against project requirements, automatically initiates renewal processes with coverage analysis, tracks professional service vendor performance, and ensures compliance with client and project-specific insurance requirements.

**Value Driver:** Consolidate Tech Stack with AI

**Estimated Impact:** Reduce insurance costs by 10-15% through better coverage optimization, eliminate gaps in professional liability coverage, save 30 hours/year on renewal management, improve vendor service quality through performance tracking.

#### Use Case 6: Vendor Prequalification & Performance Management
**Pain Point:** Each project team independently vets vendors without leveraging firm-wide knowledge. No systematic approach to vendor prequalification, performance evaluation, or preferred vendor list maintenance leads to inconsistent quality and missed opportunities.

**monday.com Solution:** Comprehensive vendor management system with standardized prequalification workflows, performance scorecards, and firm-wide vendor intelligence sharing.

**Key Boards/Workflows:**
- Vendor Master Database (all vendors, capabilities, prequalification status, contacts)
- Prequalification Workflow (standardized evaluation criteria, document collection, approval process)
- Performance Scorecards (project-by-project vendor evaluation, aggregate performance metrics)

**Vibe Prompt:** "Create a vendor management system that tracks all our subconsultants and vendors, manages prequalification requirements, and captures performance feedback from our project teams"

**Agent Blueprint:** AI agent standardizes vendor evaluation across all project teams, automatically updates vendor performance scores based on project feedback, identifies high-performing vendors for preferred status, and flags underperforming vendors for review or removal.

**Value Driver:** Scale Impact Without Overhead

**Estimated Impact:** Improve vendor quality by 30% through systematic selection, reduce project risks through better vendor vetting, create 25% time savings in vendor selection, build institutional knowledge that survives staff turnover.

#### Use Case 7: Project-Specific Procurement Coordination
**Pain Point:** Large projects require coordinating procurement activities across multiple disciplines, tracking sole source justifications, managing vendor deliverables, and ensuring all purchases align with project budgets and schedules. Manual coordination leads to delays and budget overruns.

**monday.com Solution:** Project-specific procurement dashboard integrating all purchasing activities with project schedules, budgets, and deliverable tracking.

**Key Boards/Workflows:**
- Project Procurement Dashboard (all project purchases, status, budgets, timelines)
- Sole Source Justification Tracker (documentation, approvals, cost analysis)
- Vendor Deliverables Management (schedules, quality control, acceptance tracking)

**Vibe Prompt:** "Set up project-specific procurement tracking for our large projects to coordinate all purchases, manage vendor deliverables, and ensure everything stays on budget and schedule"

**Agent Blueprint:** AI agent coordinates complex project procurement workflows, automatically tracks purchases against project budgets, manages vendor deliverable schedules, ensures proper documentation for sole source purchases, and provides early warnings for potential delays or overruns.

**Value Driver:** Replace or Radically Augment Headcount

**Estimated Impact:** Reduce project procurement coordination time by 50%, improve on-time delivery by 35%, eliminate budget overruns through real-time tracking, enhance project profitability by 5-10% through better procurement management.

---

### Discovery Questions

1. "How do you currently select and manage subconsultants for your projects? What's your typical timeline from RFQ to signed teaming agreement?"

2. "Can you walk me through your software license management? How do you handle Autodesk Enterprise agreements and track utilization across your teams?"

3. "When you're planning an office move or expansion, who coordinates all the vendors and how do you track your TI allowance and FF&E budget?"

4. "How do you ensure your technology equipment stays operational across all offices? Who manages maintenance schedules and vendor relationships?"

5. "What's your process for insurance renewals and ensuring you have proper coverage for different project types?"

6. "How do project teams share knowledge about vendor performance? Do you maintain preferred vendor lists?"

7. "For large projects, how do you coordinate all procurement activities and ensure everything stays on budget and schedule?"

### Competitive Positioning

**vs. Traditional Procurement Software (SAP Ariba, Coupa):** monday.com understands AEC's project-centric, relationship-driven procurement model. While enterprise platforms focus on transactional purchasing, monday.com excels at managing the complex vendor relationships, subconsultant teaming, and project-specific coordination that drives AEC success.

**vs. AEC-Specific Tools (Procore, Autodesk Construction Cloud):** monday.com provides comprehensive procurement management beyond construction administration. While AEC tools focus on project delivery, monday.com handles the full spectrum from office management to subconsultant relationships to equipment lifecycle management.

**vs. Spreadsheets & Email:** monday.com transforms scattered, siloed procurement activities into coordinated workflows with institutional memory, automated processes, and firm-wide visibility. The AI capabilities provide intelligence and optimization impossible with manual approaches.

**Key Differentiator:** monday.com's flexibility allows AEC firms to model their unique procurement workflows while providing the structure and automation needed to scale effectively. The platform grows with the firm and adapts to changing project demands.

### ROI Framework

**Cost Savings Metrics:**
- Software license optimization: 15-25% annual savings on software costs
- Insurance procurement: 10-15% savings through better coverage analysis
- Equipment purchasing: 20% savings through standardization and consolidated buying
- Vendor negotiation: 5-10% improvement in vendor terms through performance data

**Time Savings Metrics:**
- Subconsultant selection: 60% reduction (from 3 weeks to 1 week per project)
- License management: 20 hours/month saved on manual tracking
- Office project coordination: 50+ hours saved per buildout project
- Equipment maintenance: 25 hours/month saved on coordination

**Risk Reduction:**
- Vendor performance improvement: 25-30% through systematic selection
- Insurance coverage gaps: 90% reduction through automated compliance tracking
- Project procurement delays: 35% improvement in on-time delivery
- Equipment downtime: 40% reduction through preventive maintenance

**Revenue Impact:**
- Project profitability improvement: 5-10% through better procurement management
- Faster project delivery: 2-4 week reduction in overall project timelines
- Enhanced client satisfaction through reduced vendor-related issues

### Quick Wins

**Week 1: Subconsultant Database Setup**
Create a centralized database of all current subconsultants with contact information, specialties, and basic performance ratings. Import existing vendor lists and begin standardizing information.

**Week 1: Software License Inventory**
Audit and catalog all current software licenses, seats, and renewal dates. Set up automated alerts for upcoming renewals and begin tracking utilization patterns.

**Week 1: Equipment Asset Register**
Create an inventory of all office equipment, workstations, plotters, and specialized tools with warranty information and maintenance schedules.

**Week 1: Insurance Policy Dashboard**
Consolidate all insurance policies, renewal dates, and coverage amounts into a single dashboard with automated renewal reminders and certificate tracking.