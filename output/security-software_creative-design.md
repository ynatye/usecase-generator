# Security Software × Creative & Design Playbook

## Overview
Creative & Design teams in cybersecurity companies operate at the intersection of technical complexity and user experience. Unlike traditional design teams, they must translate sophisticated threat landscapes into intuitive security dashboards, create compelling threat visualization interfaces, and develop brand identities that convey trust and authority in a market where credibility is everything. These teams typically range from 5-25 designers across specializations: UI/UX for security products, brand/marketing creative, technical documentation design, and increasingly, dark mode interfaces optimized for SOC environments. They work closely with product, engineering, and sales teams, often under tight deadlines for product releases, conference booth designs (RSA, Black Hat), and compliance documentation that must be both accessible and technically accurate.

The regulatory landscape adds complexity — designs must accommodate GDPR, SOX, HIPAA, and industry-specific compliance requirements while maintaining usability. Creative teams are measured on user adoption of security tools, time-to-insight in threat dashboards, and the ability to make complex security concepts accessible to non-technical stakeholders through compelling visualizations and infographics.

## Value Driver Mapping
| Value Driver | Relevance | Why |
|---|---|---|
| **Replace or Radically Augment Headcount** | High | Design iteration cycles, asset creation, and compliance documentation consume massive hours. AI agents can handle routine design tasks, generate initial concepts, and maintain brand consistency 24/7. |
| **Consolidate Tech Stack with AI** | High | Teams juggle Figma, Adobe Creative Suite, project management tools, DAM systems, compliance tracking, and approval workflows. One AI platform eliminates context switching. |
| **Scale Impact Without Overhead** | Critical | Security companies grow rapidly but can't scale design teams linearly. AI enables 10 designers to output what traditionally required 30+ across all specializations. |

## Prioritized Use Cases

---

### Use Case 1: Threat Visualization Design Pipeline

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Security software companies need constant iteration on threat visualization designs — attack chain diagrams, security architecture visuals, and SOC dashboard interfaces. Design teams spend 60-70% of their time on repetitive layout adjustments, icon standardization, and compliance-approved color schemes rather than strategic UX innovation. Each new threat type requires new iconography, and every product update demands dashboard redesigns that can take weeks.

#### The Solution
monday.com AI Agents automate the design iteration pipeline. Agents trigger on product requirement updates, generate initial threat visualization concepts using brand guidelines stored in mondayDB, and create multiple dashboard layout variations. Vibe builds the design request workflow with automatic prioritization based on security severity and compliance deadlines.

#### The Outcome
Design iteration time reduces from 2-3 weeks to 2-3 days. Teams redirect 40+ hours weekly from repetitive tasks to strategic UX research and innovation. Threat visualization consistency improves across all security products.

#### Discovery Questions
- How long does your team currently spend iterating on SOC dashboard designs when new threat types emerge?
- What's your process for ensuring threat visualization consistency across different security products?
- How do you handle urgent design requests when critical vulnerabilities are discovered?
- What percentage of design time is spent on layout adjustments versus strategic UX work?
- How do you maintain dark mode design standards across all security interfaces?

#### Industry Context
SOC analysts work in low-light environments requiring specialized dark mode interfaces. Threat visualization must follow established security iconography standards (MITRE ATT&CK framework). Color coding for threat severity (red/amber/green) has regulatory implications and cannot be arbitrary.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a threat visualization design request board with these columns: Request Title (text), Threat Type (dropdown: Malware, Phishing, Insider Threat, APT, Vulnerability, Compliance), Priority (status: Critical, High, Medium, Low), Design Type (dropdown: Dashboard Layout, Attack Chain Diagram, Architecture Diagram, Infographic, Icon Set), Requester (people), Security Severity (dropdown: P0 Critical, P1 High, P2 Medium, P3 Low), Compliance Requirements (dropdown: SOX, HIPAA, GDPR, FedRAMP, None), Due Date (date), Design Assets (file), Stakeholder Approval (status: Pending, PM Approved, Security Approved, Compliance Approved, Final Approved), Designer (people), Completion Status (status: Backlog, In Progress, Design Review, Stakeholder Review, Complete). Add automation: when Completion Status changes to 'Complete', notify Requester and create follow-up task in Connected Board 'Asset Library Updates'. Create Kanban view grouped by Priority and Timeline view showing Due Date dependencies."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ThreatViz Design Assistant

**Agent Purpose:**  
Automatically generates initial threat visualization concepts and maintains design consistency across security product interfaces.

**Triggers:**
- New item created in Threat Visualization board with Priority "Critical" or "High"
- Product requirement document uploaded to connected board
- Security advisory published (via integration)
- Compliance deadline approaching (7 days out)
- Existing threat type updated in security database

**Actions:**
- Generate 3 initial dashboard layout concepts based on threat type
- Apply brand guidelines and dark mode standards automatically
- Create attack chain diagram wireframes with proper MITRE ATT&CK mapping
- Update security iconography library with new threat symbols
- Flag compliance conflicts in color schemes or layout requirements
- Assign to appropriate designer based on specialization and workload

**Data Required:**
- Brand guidelines repository (colors, typography, iconography)
- MITRE ATT&CK framework database
- Compliance requirement templates
- Historical design performance metrics
- Designer skillset and availability matrix

**Autonomy Level:** Human-in-the-Loop
Agent generates concepts and handles routine updates autonomously, but all final designs require human designer review before stakeholder presentation.

**Example Interaction:**
> A P0 critical vulnerability is discovered in a client's infrastructure. The security team updates the threat database at 2 AM. The ThreatViz Agent immediately triggers, recognizing this as a new APT variant requiring urgent dashboard visualization. It generates three dashboard concepts showing the attack progression, applies the company's dark mode security UI standards, creates appropriate threat severity color coding compliant with SOX requirements, and assigns the work to Sarah (the senior security UX designer) with a notification that includes all generated assets. By 7 AM when Sarah starts work, she has initial concepts ready for refinement instead of starting from scratch, reducing time-to-insight for the client's security team from days to hours.

---

### Use Case 2: Security Product Demo Environment Creation

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Sales teams need fresh demo environments for different prospect scenarios — financial services, healthcare, manufacturing — each requiring industry-specific threat simulations and compliance-appropriate interfaces. Design teams manually create dozens of demo variations, spending weeks building realistic-looking security scenarios that sales can actually demonstrate. Each prospect meeting may need customized dashboard mockups showing their specific threat landscape.

#### The Solution
monday.com creates a demo environment factory where Vibe builds the request workflow and AI Agents automatically generate industry-specific security demo environments. Agents pull real threat intelligence data, apply appropriate compliance overlays, and create realistic demo scenarios that sales teams can immediately deploy.

#### The Outcome
Demo environment creation time drops from 2-3 weeks to same-day delivery. Sales teams can demonstrate industry-specific security scenarios to 5x more prospects with the same design support. Revenue pipeline velocity increases as demos feel more relevant and credible to prospects.

#### Discovery Questions
- How many different demo environments does your sales team currently need for different industry prospects?
- What's the typical turnaround time when sales needs a customized security demo for a specific vertical?
- How do you ensure demo environments show realistic threat scenarios without exposing actual client data?
- What percentage of design team time goes toward supporting sales demo requests?
- How often do you need to update demo environments to reflect current threat landscapes?

#### Industry Context
Security sales cycles require credible demonstrations of threat detection and response. Demo environments must show realistic attack scenarios without using real threat data. Industry-specific compliance overlays (healthcare showing HIPAA, finance showing PCI-DSS) are essential for credibility.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a demo environment request board with these columns: Demo Name (text), Target Industry (dropdown: Financial Services, Healthcare, Manufacturing, Retail, Government), Sales Rep (people), Prospect Company (text), Demo Date (date), Threat Scenarios Needed (checklist: Phishing Campaign, Insider Threat, Ransomware, APT, Data Exfiltration, Supply Chain Attack), Compliance Overlay (dropdown: HIPAA, PCI-DSS, SOX, GDPR, FedRAMP, NIST), Demo Environment URL (link), Creation Status (status: Requested, Threat Data Sourcing, UI Customization, QA Testing, Ready for Demo), Design Assets (file), Sales Feedback (long text), Reuse Potential (dropdown: One-time, Template-worthy, Industry Standard). Add automation: when Demo Date is within 3 days, notify Design Team and Sales Rep. Create Dashboard view showing demo pipeline and success rates by industry."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DemoForge Security Environment Builder

**Agent Purpose:**  
Automatically generates industry-specific security product demo environments with realistic threat scenarios and appropriate compliance overlays.

**Triggers:**
- New demo request created with Demo Date within 10 days
- Sales opportunity reaches "Technical Demo" stage in CRM
- Existing demo environment scheduled for refresh (quarterly)
- New compliance requirement affects industry demos
- Threat intelligence update requires demo scenario updates

**Actions:**
- Generate realistic threat scenarios appropriate to target industry
- Apply correct compliance overlays and regulatory frameworks
- Create industry-specific dashboard mockups with relevant metrics
- Populate demo environment with anonymized but realistic data
- Generate demo script highlighting key security capabilities
- Schedule automatic demo environment refresh before expiration

**Data Required:**
- Threat intelligence feeds by industry vertical
- Compliance requirement databases (HIPAA, PCI-DSS, etc.)
- Historical demo performance and conversion data
- Industry-specific terminology and use case libraries
- Demo environment templates and asset repositories

**Autonomy Level:** Fully Autonomous
Agent handles complete demo environment creation from request to deployment, with human oversight only for quality assurance spot-checks.

**Example Interaction:**
> Sales rep Mark receives an inbound lead from a regional hospital system. He creates a demo request in monday.com for healthcare vertical, mentioning their concern about medical device security. DemoForge Agent immediately triggers, pulling the latest healthcare threat intelligence showing increased attacks on IoT medical devices. It generates a demo environment featuring a simulated hospital network with realistic medical device endpoints, populates it with HIPAA-compliant synthetic patient data, creates dashboard views showing IoMT security monitoring, and applies appropriate healthcare compliance overlays. The agent delivers a complete demo environment URL within 4 hours, including talking points about medical device vulnerability management, allowing Mark to schedule the demo for the next day instead of waiting weeks for design team availability.

---

### Use Case 3: Security Conference Booth Design Production

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Security conferences like RSA and Black Hat require extensive booth design coordination — graphics, demos, swag, digital displays, and literature. Creative teams coordinate across vendors, manage multiple approval cycles, track hundreds of design assets, and ensure brand consistency across all touchpoints. The process involves 15+ different tools and systems, with constant version control issues and missed deadlines.

#### The Solution
monday.com becomes the single source of truth for conference production. Vibe builds comprehensive project workflows tracking everything from booth graphics to demo station setups. AI Agents automatically coordinate vendor communications, track approval workflows, and ensure all assets meet brand guidelines and venue specifications.

#### The Outcome
Conference production cycle time reduces by 40%. Asset approval workflows accelerate from weeks to days. Zero missed booth setup deadlines or brand guideline violations. Single platform visibility eliminates coordination chaos across teams and vendors.

#### Discovery Questions
- How many security conferences does your company participate in annually, and what's the typical booth design budget?
- What's your current process for coordinating booth graphics, demos, and swag across multiple vendors?
- How do you track approval workflows for conference assets across legal, marketing, and executive stakeholders?
- What percentage of conference assets need last-minute revisions due to coordination issues?
- How do you ensure brand consistency across booth graphics, demo stations, and literature at events?

#### Industry Context
Security conferences are critical for brand positioning and lead generation. RSA and Black Hat booth locations can cost $100K+, making flawless execution essential. Security audiences are highly technical and skeptical, requiring credible demonstrations and materials that convey technical authority.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a security conference production board with these columns: Conference Name (text), Event Date (date), Booth Size (dropdown: 10x10, 10x20, 20x20, 30x30, Island), Production Manager (people), Budget (numbers), Asset Type (dropdown: Booth Graphics, Demo Stations, Literature, Swag, Digital Displays, Video Content), Asset Description (text), Vendor (text), Design Status (status: Concept, Design Review, Client Approval, Legal Approval, Production, Shipped, Installed), Due Date (date), Files (file), Approval Notes (long text), Cost (numbers), Venue Requirements (long text). Add automation: when Design Status changes to 'Production', notify Production Manager and Vendor. When Due Date is within 7 days and status is not 'Shipped', escalate to leadership team. Create Timeline view showing critical path and Dashboard view showing budget tracking by conference."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ConferenceCommand Production Orchestrator

**Agent Purpose:**  
Orchestrates end-to-end security conference booth production from initial planning through on-site installation.

**Triggers:**
- New conference added to annual event calendar
- Booth contract signed (via integration with procurement system)
- Vendor proposal received for any conference asset
- Design asset uploaded requiring approval workflow
- Critical path deadline approaching (5 days)

**Actions:**
- Generate comprehensive production timeline with critical path analysis
- Automatically request vendor proposals based on booth specifications
- Route design assets through appropriate approval workflows
- Track budget vs. actual spend with variance alerts
- Coordinate shipping logistics and venue delivery requirements
- Generate pre-event checklists and post-event performance reports

**Data Required:**
- Venue specification databases for major security conferences
- Approved vendor lists with capabilities and lead times
- Brand guidelines and approval workflow hierarchies
- Historical conference ROI and lead generation data
- Shipping and logistics coordination systems

**Autonomy Level:** Escalation-Based
Agent handles routine coordination and workflow management autonomously, escalating to humans for budget overages, missed deadlines, or vendor issues.

**Example Interaction:**
> Six months before RSA 2025, the ConferenceCommand Agent triggers when the booth contract is signed. It immediately generates a comprehensive production timeline, identifying that a 20x20 island booth requires graphics production to start 12 weeks out. The agent requests proposals from three approved booth vendors, creates design brief templates populated with conference specifications, and sets up approval workflows for graphics, demo equipment, and literature. As assets are created, it automatically routes them for legal review (scanning for compliance with conference exhibitor guidelines), brand approval, and executive sign-off. When the graphics vendor submits proofs, the agent tracks versions, manages revision cycles, and coordinates with venue logistics for delivery schedules. Two weeks before the event, it generates pre-show checklists and coordinates final shipments, ensuring nothing falls through the cracks in the complex multi-vendor production process.

---

### Use Case 4: Compliance Documentation Design Automation

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Security companies must produce extensive compliance documentation — SOC 2 reports, FedRAMP documentation, HIPAA compliance guides, ISO 27001 materials. Design teams spend enormous time formatting these documents, creating compliance flowcharts, and ensuring visual consistency across hundreds of pages. Each audit cycle requires documentation updates that can consume weeks of design time for what is essentially formatting work.

#### The Solution
monday.com AI Agents automatically format compliance documentation using approved templates, generate process flowcharts from text descriptions, and maintain visual consistency across all compliance materials. Vibe builds the documentation workflow with automatic routing to appropriate stakeholders for review and approval.

#### The Outcome
Compliance documentation production time reduces by 70%. Design teams redirect from formatting work to strategic brand and product design. Audit preparation cycles accelerate, reducing compliance costs and time-to-market for security products.

#### Discovery Questions
- How many different compliance frameworks does your company need to maintain documentation for?
- What's the typical timeline and resource allocation for preparing compliance audit materials?
- How do you ensure visual consistency across SOC 2 reports, security whitepapers, and compliance guides?
- What percentage of design team time goes toward formatting compliance documents versus strategic design work?
- How do you handle urgent compliance documentation requests during audit periods?

#### Industry Context
Security companies face multiple overlapping compliance requirements (SOC 2, FedRAMP, ISO 27001, HIPAA). Documentation quality reflects on company credibility and can impact sales cycles. Audit timelines are non-negotiable and require rapid documentation updates.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a compliance documentation board with these columns: Document Title (text), Compliance Framework (dropdown: SOC 2, FedRAMP, ISO 27001, HIPAA, PCI-DSS, NIST CSF), Document Type (dropdown: Report, Policy, Procedure, Flowchart, Checklist, Training Material), Assigned Writer (people), Assigned Designer (people), Content Status (status: Planning, Writing, Design Review, Legal Review, Compliance Review, Final Approval, Published), Audit Deadline (date), Priority (status: Critical, High, Medium, Low), Page Count (numbers), Template Used (dropdown: Standard Report, Executive Summary, Technical Guide, Process Flow, Checklist), Stakeholder Reviewers (people), Files (file), Review Notes (long text). Add automation: when Audit Deadline is within 14 days, notify all stakeholders and escalate to compliance team lead. Create Dashboard view showing audit preparation progress and Timeline view for critical path management."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ComplianceDoc Formatting Engine

**Agent Purpose:**  
Automatically formats and visualizes compliance documentation while maintaining brand consistency and regulatory requirements.

**Triggers:**
- New compliance document uploaded in draft format
- Document template updated requiring format propagation
- Audit deadline approaching with incomplete documentation
- Regulatory framework updated requiring documentation refresh
- Stakeholder requests document revision or formatting changes

**Actions:**
- Apply appropriate document templates based on compliance framework
- Generate process flowcharts from text procedure descriptions
- Ensure visual consistency across document families
- Create executive summary layouts with key compliance metrics
- Format technical appendices with proper citation standards
- Generate final PDF packages ready for audit submission

**Data Required:**
- Approved document templates for each compliance framework
- Brand guidelines and formatting standards library
- Regulatory requirement databases with current standards
- Historical audit feedback and required improvements
- Stakeholder approval hierarchies and review cycles

**Autonomy Level:** Human-in-the-Loop
Agent handles formatting and visual design autonomously, but all compliance content and technical accuracy requires human expert review.

**Example Interaction:**
> The compliance team uploads a 45-page SOC 2 Type II draft report three weeks before the audit deadline. ComplianceDoc Agent immediately triggers, recognizing this as a SOC 2 document requiring specific formatting standards. It applies the approved SOC 2 template, generates process flowcharts from the written control descriptions, ensures all headings follow the correct hierarchy, formats the evidence appendices with proper indexing, and creates executive summary layouts highlighting key control effectiveness metrics. The agent identifies sections requiring design attention (complex process flows, risk matrices), assigns them to appropriate designers, and generates a formatted draft for stakeholder review within 2 hours instead of the usual 2-3 days. This acceleration allows the compliance team to focus on content accuracy and control testing results rather than document formatting logistics.

---

### Use Case 5: Dark Mode UI Design System Management

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Security products require sophisticated dark mode interfaces optimized for SOC environments and low-light operations. Design teams must maintain parallel design systems (light and dark), ensure accessibility compliance, and test contrast ratios across dozens of components. Changes to the design system require propagation across multiple products, often manually updated by different designers leading to inconsistencies.

#### The Solution
monday.com becomes the single source of truth for dark mode design system components. Vibe builds the component library workflow with automated testing and approval processes. AI Agents automatically propagate design system updates across all security products and flag accessibility issues.

#### The Outcome
Design system consistency improves across all security products. Component update propagation time reduces from weeks to hours. Accessibility compliance automated, reducing legal risk and improving SOC analyst usability.

#### Discovery Questions
- How many security products currently use your dark mode design system, and how do you maintain consistency?
- What's your process for updating UI components across multiple security tools when the design system changes?
- How do you test accessibility compliance for dark mode interfaces used in SOC environments?
- What challenges do you face with contrast ratios and color accessibility in security dashboards?
- How do you handle design system updates when multiple product teams are on different release cycles?

#### Industry Context
SOC analysts work in dimly lit environments requiring specialized dark interfaces. Security tools run 24/7 with high information density requiring careful attention to visual hierarchy and accessibility. WCAG compliance is essential for enterprise security sales.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a dark mode design system board with these columns: Component Name (text), Component Type (dropdown: Button, Input Field, Dashboard Widget, Alert/Notification, Navigation, Data Table, Chart/Graph, Modal), Design Status (status: Concept, Design Review, Accessibility Testing, Development Ready, In Production), Designer (people), Accessibility Score (numbers), Color Contrast Ratio (text), Products Using (checklist: Threat Detection, SIEM Platform, Vulnerability Manager, Compliance Dashboard, SOC Console), Last Updated (date), Figma Link (link), Code Implementation (link), Testing Notes (long text), Approval Status (status: Pending, Design Approved, Accessibility Approved, Engineering Approved, Released). Add automation: when Accessibility Score is below 4.5, notify Designer and Accessibility Lead. Create Dashboard view showing component adoption across products and Timeline view for design system roadmap."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DarkMode System Guardian

**Agent Purpose:**  
Maintains consistency and accessibility compliance across dark mode design system components in security products.

**Triggers:**
- New component added to design system library
- Existing component modified or updated
- Accessibility standards updated (WCAG guidelines)
- Product team requests design system component
- Automated accessibility scan detects compliance issues

**Actions:**
- Validate color contrast ratios for SOC environment visibility
- Generate accessibility compliance reports for each component
- Propagate approved component updates to all affected products
- Flag design inconsistencies across security product interfaces
- Create component usage analytics and adoption reports
- Generate design system documentation updates automatically

**Data Required:**
- Complete component library with design specifications
- Accessibility standards database (WCAG, SOC usability guidelines)
- Product implementation tracking across security tools
- Usage analytics from deployed security interfaces
- Designer workflow and approval hierarchies

**Autonomy Level:** Fully Autonomous
Agent handles component validation, accessibility testing, and propagation autonomously, with human oversight only for major design system architectural changes.

**Example Interaction:**
> A designer updates the alert notification component to improve threat severity visualization, changing the red warning color to be more visible in low-light SOC environments. DarkMode System Guardian immediately triggers, running accessibility tests to ensure the new color meets WCAG contrast requirements against dark backgrounds. It validates the color change doesn't break existing alert hierarchies across five security products, generates updated component specifications, and automatically pushes the changes to design system documentation. The agent identifies that the Vulnerability Manager product uses a custom alert variant and flags this for design review, ensuring system consistency. Within minutes, all product teams have access to the updated component with complete accessibility compliance documentation, rather than discovering inconsistencies weeks later during development cycles.

---

### Use Case 6: Security Awareness Campaign Asset Creation

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Security companies must create extensive educational content — phishing simulation graphics, security awareness training materials, threat briefing presentations, and customer education resources. Design teams manually create hundreds of assets for different audiences (technical, executive, end-user), often recreating similar content with slight variations for different client industries or threat types.

#### The Solution
monday.com AI Agents automatically generate security awareness campaign assets based on current threat intelligence, customize content for different audience types, and create industry-specific variations. Vibe builds the campaign workflow with automatic stakeholder reviews and approval processes.

#### The Outcome
Security awareness content creation scales 5x without adding headcount. Campaign delivery time reduces from months to weeks. Content relevance improves through real-time threat intelligence integration.

#### Discovery Questions
- How many security awareness campaigns does your company produce annually for clients and internal use?
- What's your process for customizing security awareness content for different industries or audience types?
- How do you ensure security awareness materials reflect current threat landscapes and attack methods?
- What percentage of design time goes toward creating educational content versus product interface design?
- How do you measure the effectiveness of security awareness campaigns and iterate on design approaches?

#### Industry Context
Security awareness is critical for customer retention and compliance. Content must balance accessibility with technical accuracy. Different industries require tailored threat scenarios (healthcare phishing vs. financial fraud vs. manufacturing espionage).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a security awareness campaign board with these columns: Campaign Name (text), Target Audience (dropdown: Technical Staff, Executives, End Users, IT Administrators), Industry Focus (dropdown: Healthcare, Finance, Manufacturing, Retail, Education, Generic), Threat Focus (checklist: Phishing, Social Engineering, Ransomware, Insider Threats, Physical Security, Password Security), Content Type (checklist: Email Graphics, Poster Design, Training Slides, Video Assets, Interactive Content, Infographics), Campaign Status (status: Planning, Content Creation, Design Review, Stakeholder Approval, Production, Deployed), Campaign Manager (people), Designer (people), Due Date (date), Budget (numbers), Asset Files (file), Performance Metrics (long text), Reuse Potential (dropdown: Campaign-Specific, Template-Worthy, Industry Standard). Add automation: when Campaign Status changes to 'Deployed', create follow-up task for performance analysis in 30 days. Create Dashboard view showing campaign pipeline and Kanban view grouped by Target Audience."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AwarenessCraft Campaign Generator

**Agent Purpose:**  
Automatically generates industry-specific security awareness campaign assets based on current threat intelligence and audience requirements.

**Triggers:**
- New security awareness campaign request created
- Threat intelligence update indicates emerging attack vector
- Quarterly campaign refresh schedule triggers
- Client requests custom awareness materials
- Campaign performance data suggests content updates needed

**Actions:**
- Generate industry-specific phishing simulation graphics
- Create threat briefing presentations with current attack examples
- Customize security awareness posters for different audience types
- Generate interactive training content with scenario variations
- Create executive summary materials for awareness campaign ROI
- Update existing campaigns when new threat intelligence emerges

**Data Required:**
- Current threat intelligence feeds and attack trend data
- Industry-specific security incident databases
- Audience persona profiles and communication preferences
- Historical campaign performance and engagement metrics
- Brand guidelines and compliance requirements for educational content

**Autonomy Level:** Human-in-the-Loop
Agent generates initial campaign concepts and assets autonomously, with human review required for accuracy of security content and final stakeholder approval.

**Example Interaction:**
> Threat intelligence indicates a new business email compromise (BEC) attack targeting healthcare CFOs using COVID-related financial relief themes. The AwarenessCraft Agent triggers, recognizing this as a healthcare-specific threat requiring immediate awareness campaign updates. It generates a series of assets: phishing simulation emails using realistic COVID relief language, executive briefing slides showing BEC attack progression in healthcare contexts, poster designs for hospital break rooms warning about financial fraud attempts, and interactive training modules where users identify BEC red flags in healthcare scenarios. The agent customizes messaging for different healthcare roles (administrators, clinical staff, executives) and generates industry-specific statistics showing BEC impact on healthcare organizations. Within hours, the security awareness team has a complete campaign package ready for deployment, allowing rapid response to emerging threats rather than weeks of manual asset creation.

---

## Industry Terminology
| Term | Definition |
|---|---|
| **SOC (Security Operations Center)** | 24/7 facility monitoring organization's security posture with specialized dark-mode interfaces |
| **SIEM (Security Information and Event Management)** | Platform aggregating security data requiring complex dashboard visualization |
| **Threat Visualization** | Graphical representation of attack chains, threat landscapes, and security metrics |
| **Attack Chain Diagram** | Visual mapping of multi-stage cyber attack progression from initial compromise to data exfiltration |
| **MITRE ATT&CK Framework** | Standardized taxonomy of adversary tactics and techniques used in threat visualizations |
| **Dark Mode UI** | Interface design optimized for low-light SOC environments with high contrast and reduced eye strain |
| **Threat Intelligence** | Data about current and emerging security threats used to inform defensive strategies |
| **IoMT (Internet of Medical Things)** | Connected medical devices requiring specialized security interface design |
| **Zero Trust Architecture** | Security model requiring intuitive visualization of user access and data flow |
| **Incident Response** | Process requiring rapid information visualization and stakeholder communication materials |

## Typical Stakeholder Roles
| Role | Responsibility | Influence |
|---|---|---|
| **VP Creative/Design** | Strategic design vision, team leadership, cross-functional alignment | High - Budget and resource allocation |
| **Senior Security UX Designer** | SOC interface design, threat visualization, user research with security analysts | High - Product usability and adoption |
| **Brand/Marketing Creative Lead** | Brand consistency, conference materials, customer-facing collateral | Medium - Brand positioning and sales support |
| **Technical Documentation Designer** | Compliance materials, security architecture diagrams, training content | Medium - Customer onboarding and compliance |
| **Creative Operations Manager** | Workflow efficiency, vendor coordination, project management | High - Team productivity and delivery |
| **Accessibility/Compliance Specialist** | WCAG compliance, regulatory documentation design | Medium - Legal risk and enterprise sales |

## Adjacent Departments
| Department | Connection | Opportunity |
|---|---|---|
| **Product Management** | Requires UX design for security product features and roadmap visualization | Expand into product strategy and user research workflows |
| **Sales Engineering** | Needs demo environments, customer presentation materials, and technical diagrams | Create automated demo generation and sales collateral systems |
| **Marketing** | Collaborates on brand materials, website design, and conference presence | Unify creative operations across brand and product design teams |
| **Compliance/Legal** | Requires formatted documentation, process diagrams, and regulatory materials | Automate compliance documentation production and approval workflows |
| **Customer Success** | Needs training materials, onboarding guides, and support documentation | Scale educational content creation and customer communication design |

## Competitive Landscape
| Tool | Positioning | Displacement Opportunity |
|---|---|---|
| **Figma + Project Management Tools** | "Design collaboration is separate from project workflow" | "One platform for design workflow AND creative operations management" |
| **Adobe Creative Cloud + Multiple PM Tools** | "Creative tools don't integrate with business processes" | "Creative work flows seamlessly into business outcomes and approvals" |
| **Asana/Monday Classic + Creative Tools** | "Generic project management doesn't understand design workflows" | "Built for creative teams with design-specific AI automation" |
| **Digital Asset Management Systems** | "Asset storage is separate from creative production workflow" | "Assets, production, and approval workflows unified with AI orchestration" |
| **Slack + File Sharing + Approval Tools** | "Communication and approval workflows are fragmented" | "Context-aware AI manages entire creative process from brief to delivery" |

## Objection Handling
| Objection | Response |
|---|---|
| "Our design tools (Figma, Adobe) are industry standard" | "We integrate with your creative tools — this is about workflow orchestration and AI automation around them. Keep your design tools, eliminate the chaos around them." |
| "Designers need creative freedom, not process overhead" | "AI agents handle the operational overhead so designers can focus on creative strategy. Less time managing approvals means more time designing." |
| "Security design has unique requirements that generic tools can't handle" | "That's exactly why you need security-specific AI agents that understand threat visualization, SOC interfaces, and compliance requirements." |
| "We can't risk AI making mistakes with security-sensitive materials" | "Agents handle workflow automation and initial concepts — humans always review security content. AI accelerates iteration, doesn't replace expertise." |
| "Our current project management setup works fine" | "Fine isn't competitive when your peers are scaling design output 5x with AI. This is about market differentiation, not fixing broken processes." |

## Proof Points
*(To be populated with customer references)*
- [ ] Mid-market security software company scaling design team output 3x during rapid growth phase
- [ ] Enterprise cybersecurity vendor reducing conference production cycle time by 40% with automated workflows
- [ ] Security awareness training company scaling content creation 5x without adding headcount
- [ ] SOC platform provider improving design system consistency across multiple security products
- [ ] Compliance-focused security vendor reducing audit documentation preparation time by 70%

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*