# Medical Devices & Equipment × PR & Communications Playbook

## Overview

PR & Communications in the medical devices industry operates in one of the most regulated and high-stakes environments. Teams manage complex dual audiences—healthcare professionals and patients—while navigating FDA regulatory requirements, clinical evidence standards, and patient safety protocols. The typical structure includes internal communications teams (3-15 people depending on company size), external PR agencies, regulatory communications specialists, and often dedicated crisis communications teams. Unlike other industries, every communication must balance commercial messaging with clinical evidence, patient safety considerations, and strict regulatory compliance including FDA off-label use guidance and Sunshine Act transparency requirements.

Medical device PR teams are uniquely challenged by regulatory timing constraints—product launches must align with FDA clearance milestones, clinical trial results require peer-reviewed publication strategies, and adverse event communications demand immediate, coordinated responses across multiple stakeholders. The department operates at the intersection of R&D timelines, regulatory affairs, clinical evidence generation, and commercial marketing, making it a critical orchestrator of company-wide communications strategies.

## Value Driver Mapping

| Value Driver | Relevance | Rationale |
|-------------|-----------|-----------|
| **Replace or Radically Augment Headcount** | **High** | PR teams spend 60-70% of time on manual media monitoring, report compilation, and regulatory compliance tracking—perfect for AI automation |
| **Consolidate Tech Stack with AI** | **High** | Typical setup: 8-12 tools (media monitoring, press release distribution, regulatory tracking, clinical evidence management, crisis comms platforms) |
| **Scale Impact Without Overhead** | **Medium** | Growth requires maintaining quality and compliance across expanding product portfolios and global markets without proportional team growth |

## Prioritized Use Cases

---

### Use Case 1: FDA Clearance & Product Launch Communications

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
FDA clearance timing is unpredictable, often creating 48-72 hour sprint windows for coordinated launch communications across KOLs, media, investors, and sales teams. Current manual processes lead to delayed announcements, inconsistent messaging, and missed market opportunities worth millions in first-mover advantage.

#### The Solution
monday.com Work Management with integrated timeline management, automated stakeholder notifications triggered by regulatory milestone updates, and Vibe-generated communication templates that automatically populate with product specs, clinical data, and regulatory language. Service for managing external agency coordination and approval workflows.

#### The Outcome
Reduce launch communication timeline from 5-7 days to 24-48 hours. Eliminate messaging inconsistencies across channels. Capture 15-20% more media coverage during critical launch window. ROI: $2-5M in accelerated market capture for Class II device launches.

#### Discovery Questions
- How long is your typical window from FDA clearance notification to market communication?
- What percentage of launch announcements miss optimal timing due to coordination delays?
- How many stakeholders need to approve messaging before public announcement?
- What's the cost of a delayed product launch announcement in your therapeutic area?
- How do you currently track competitor FDA submissions and clearances?

#### Industry Context
FDA 510(k) clearances can arrive with minimal warning. De Novo submissions have even less predictable timelines. Launch coordination must include clinical investigators, key opinion leaders, reimbursement teams, and international regulatory bodies. Sunshine Act considerations affect KOL engagement timing.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a regulatory communications launch board with columns: Product Name (text), FDA Submission Type (dropdown: 510k, PMA, De Novo), Submission Date (date), Expected Clearance (date), Actual Clearance (date), Launch Phase (status: Pre-submission, Under Review, Cleared-Pending Launch, Launched), Key Message (long text), Clinical Data Points (long text), KOL Contacts (people), Media Targets (text), Press Release Status (status: Draft, Medical Review, Legal Review, Approved, Distributed), Launch Priority (dropdown: High, Medium, Low). Add timeline view for launch planning and automations to notify the PR team when status changes to 'Cleared-Pending Launch' and send Slack notification to #product-launch channel with clearance details."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FDA Launch Orchestrator

**Agent Purpose:**  
Automatically coordinates and executes product launch communications the moment FDA clearance is received.

**Triggers:**
- FDA clearance status change to "Approved"
- Manual trigger from regulatory affairs team
- Integration webhook from FDA databases
- Calendar-based reminder for expected clearance dates
- Competitor clearance notifications

**Actions:**
- Generate personalized press releases using approved templates
- Send immediate notifications to all stakeholders with launch timeline
- Create KOL outreach sequences with clinical data talking points
- Schedule media briefing invitations
- Update investor relations materials with regulatory milestone
- Trigger social media compliance review workflow

**Data Required:**
- FDA submission database integration
- Approved messaging templates by product category
- KOL contact database with expertise mapping
- Media contact lists by therapeutic area
- Clinical trial results and outcomes database

**Autonomy Level:** Human-in-the-Loop
Critical medical device launches require final human approval for messaging, but agent pre-populates all templates and coordinates initial outreach automatically.

**Example Interaction:**
> At 3:47 PM on Tuesday, the FDA clears MedDevice Inc.'s new cardiac catheter. Within minutes, the Launch Orchestrator agent detects this through the FDA database integration, immediately generating a press release draft using the pre-approved template populated with the device's clinical trial results showing 23% reduction in procedure time. The agent sends instant Slack notifications to the CMO, Head of Cardiology Marketing, and Lead Clinical Investigator with the message: "FDA clearance confirmed - launch materials ready for review. Press release draft available, KOL outreach sequence prepared for 47 contacts, media briefing scheduled for Thursday 2 PM EST." By 5 PM, after quick human approval, 200+ stakeholders receive coordinated launch announcements, and the first media interviews are already scheduled for the following morning.

---

### Use Case 2: Clinical Trial Results Communication & Publication Strategy

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Clinical trial results communications require coordinating peer-reviewed publications, conference presentations, media announcements, and regulatory submissions—often across 6-18 month timelines. Manual tracking across multiple systems leads to missed publication opportunities, suboptimal conference presentation timing, and disconnected messaging between clinical and commercial communications.

#### The Solution
Unified mondayDB housing clinical trial data, publication timelines, conference deadlines, and media strategies. AI agents monitor journal submission status, conference abstract deadlines, and coordinate messaging across clinical investigators, KOLs, and commercial teams. Integration with ClinicalTrials.gov for automated updates.

#### The Outcome
Increase successful peer-reviewed publications by 30-40%. Optimize conference presentation timing for maximum commercial impact. Reduce clinical communications coordination time by 60%. Estimated value: $3-8M in improved commercial outcomes per major clinical study.

#### Discovery Questions
- How many clinical studies do you manage communications for annually?
- What percentage of your positive trial results make it to peer-reviewed publication within 12 months?
- How do you currently coordinate timing between journal publication and conference presentations?
- What's your strategy for maximizing media coverage of clinical evidence?
- How do you track competitive clinical trial communications in your space?

#### Industry Context
Major medical conferences (ACC, ESC, RSNA, AHA) have strict abstract deadlines 6+ months in advance. Peer-reviewed journals require embargo coordination. FDA requires clinical data in specific formats for regulatory submissions. KOL researchers have competing priorities and publication timelines.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a clinical publications management board with columns: Study Name (text), Primary Endpoint (text), Study Phase (status: Enrollment, Data Collection, Analysis, Results Available), Top-line Results (long text), Target Journal (dropdown: JACC, Circulation, NEJM, Lancet, Other), Submission Date (date), Review Status (status: Not Submitted, Under Review, Revisions Requested, Accepted, Published), Conference Target (dropdown: ACC, AHA, RSNA, ESC, MEDICA), Abstract Deadline (date), Presentation Date (date), Media Strategy (text), KOL Collaborators (people), Publication Priority (dropdown: High, Medium, Low). Include Gantt timeline view and automate email notifications to Clinical Affairs when review status changes to 'Accepted' with subject line containing study name and journal."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Clinical Evidence Coordinator

**Agent Purpose:**  
Orchestrates multi-channel clinical evidence communications from trial completion through commercial implementation.

**Triggers:**
- Clinical study status change to "Results Available"
- Journal submission status updates
- Conference abstract deadline reminders (90 days, 30 days, 7 days prior)
- Competitor clinical data publication detection
- Media inquiry about clinical evidence

**Actions:**
- Generate publication strategy recommendations based on study results
- Create conference abstract drafts using clinical data templates
- Schedule KOL co-author coordination meetings
- Prepare media materials aligned with journal embargo schedules
- Update sales training materials with new clinical evidence
- Generate competitive intelligence reports on similar studies

**Data Required:**
- Clinical trial management system integration
- Journal submission tracking
- Conference calendar and deadlines
- KOL collaboration history and expertise
- Historical publication success rates by journal/conference

**Autonomy Level:** Escalation-Based
Agent autonomously manages timelines and preparations, escalates to humans for strategic decisions on journal targeting and messaging approval.

**Example Interaction:**
> When the SUMMIT cardiac trial reports 15% reduction in major adverse cardiac events, the Clinical Evidence Coordinator immediately creates a publication roadmap: target NEJM for primary publication (submission deadline in 6 weeks), ACC conference abstract for late-breaking clinical trials session (deadline in 3 months), and coordinate with 12 co-investigating KOLs. The agent automatically schedules manuscript development meetings, prepares draft press materials under embargo, and alerts the commercial team about potential label expansion opportunities. Within 48 hours, the entire publication strategy is mapped, stakeholders are aligned, and execution is underway—what previously took 2-3 weeks of manual coordination.

---

### Use Case 3: Product Recall & Field Safety Notice Crisis Communications

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device recalls require immediate, coordinated communications across healthcare providers, patients, regulators (FDA), international bodies (Health Canada, EMA), media, investors, and internal teams. Manual processes during crisis situations lead to delayed notifications, inconsistent messaging, and regulatory compliance failures that can result in additional FDA enforcement actions.

#### The Solution
Pre-configured crisis communication templates integrated with monday.com's Service product for customer notification tracking, automated regulatory reporting workflows, and real-time stakeholder communication dashboards. Vibe-generated communication plans that auto-populate with device details, affected lot numbers, and required regulatory language.

#### The Outcome
Reduce crisis response time from 6-12 hours to 2-4 hours. Ensure 100% regulatory compliance with notification requirements. Minimize reputation damage through coordinated, transparent communications. Potential savings: $5-15M in reduced regulatory penalties and market impact per recall event.

#### Discovery Questions
- What's your current process for managing field safety notices and recalls?
- How do you track notification compliance across different regulatory jurisdictions?
- What percentage of healthcare providers acknowledge receipt of your safety communications?
- How long does it typically take to notify all stakeholders during a recall event?
- What systems do you use to coordinate with external counsel during crisis communications?

#### Industry Context
FDA requires customer notification within 24-48 hours for Class I recalls. International regulatory bodies have varying requirements. Healthcare providers must be notified through multiple channels. Patient notification may be required depending on device type and risk level. Legal counsel involvement is mandatory for most recall communications.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a crisis communications management board with columns: Incident ID (text), Product/Device Name (text), Recall Classification (dropdown: Class I, Class II, Class III, Field Correction), Risk Level (status: High, Medium, Low), Affected Lot Numbers (text), FDA Report Date (date), Customer Notification Required (checkbox), Media Response Required (checkbox), Stakeholder Groups (text), Notification Status (status: Not Started, In Progress, Completed), Legal Review (status: Pending, Approved, Escalated), Timeline Progress (progress), Key Messages (long text), Assigned Team (people). Add Kanban view by recall classification and automate immediate Slack notifications to #crisis-response channel when new incidents are created with High risk level."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Crisis Response Orchestrator

**Agent Purpose:**  
Immediately activates and coordinates all crisis communication protocols when product safety issues are identified.

**Triggers:**
- New recall/field safety notice creation
- Risk level escalation to "High"
- FDA communication received
- Customer complaint severity threshold reached
- Media inquiry about product safety

**Actions:**
- Generate regulatory notification drafts with required legal language
- Create customer communication materials by audience type
- Initiate stakeholder notification sequences (providers, distributors, patients)
- Schedule crisis team coordination calls
- Prepare holding statements for media inquiries
- Track notification delivery and acknowledgment rates

**Data Required:**
- Product distribution database with customer contacts
- Regulatory requirements by jurisdiction
- Approved crisis communication templates
- Legal team escalation protocols
- Historical recall communication performance data

**Autonomy Level:** Fully Autonomous
Given the time-critical nature of safety communications, agent operates autonomously with parallel human notification to ensure maximum speed.

**Example Interaction:**
> At 2:15 PM Friday, quality control identifies a potential software malfunction in cardiac monitoring devices that could affect alarm functionality. Within 3 minutes of the incident being logged, the Crisis Response Orchestrator activates the full recall protocol: generates FDA-compliant safety notice drafts, creates tailored communications for 847 healthcare facilities, initiates notification sequences for cardiology departments and biomedical engineering teams, schedules emergency management calls for 4 PM EST, and prepares media holding statements. By 3:30 PM, the first customer notifications are delivered, FDA preliminary report is submitted, and the crisis team is aligned on response strategy—providing a 4+ hour head start on what typically takes until Monday morning to coordinate.

---

### Use Case 4: KOL Media Placement & Sunshine Act Compliance

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Managing key opinion leader media relationships requires tracking Sunshine Act payment reporting, ensuring compliance with off-label communication guidelines, coordinating availability across multiple therapeutic conferences, and maintaining detailed records for regulatory audits. Current spreadsheet-based tracking leads to compliance violations, missed media opportunities, and inefficient KOL utilization.

#### The Solution
Integrated KOL relationship management within mondayDB that automatically tracks Sunshine Act payment thresholds, coordinates media availability, maintains compliance documentation, and optimizes KOL placement for maximum reach. CRM integration for payment tracking and automated regulatory reporting.

#### The Outcome
Increase KOL media placements by 35-50% while maintaining 100% Sunshine Act compliance. Reduce administrative time by 70%. Optimize KOL investment ROI by matching expertise to media opportunities. Estimated value: $2-4M annually in improved KOL program effectiveness.

#### Discovery Questions
- How many KOLs are in your current media program?
- What percentage of your Sunshine Act payments are related to communications activities?
- How do you currently track KOL availability for media opportunities?
- What compliance challenges do you face with KOL communications programs?
- How do you measure the effectiveness of KOL media placements?

#### Industry Context
Sunshine Act requires reporting of payments >$10 to healthcare providers. FDA guidance restricts off-label communication. KOLs often have competing obligations across multiple companies. Major conferences create concentrated media opportunity windows. Compliance violations can trigger FDA enforcement actions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a KOL media management board with columns: KOL Name (text), Medical Specialty (dropdown: Cardiology, Orthopedics, Neurosurgery, Radiology, Other), Institution (text), Media Experience (dropdown: Extensive, Moderate, Limited), Sunshine Act YTD Total (numbers), Payment Threshold Status (status: Under $10, Reportable, Approaching Limit), Available Conferences (text), Recent Media Placements (long text), Compliance Notes (text), Next Scheduled Appearance (date), Media Topics (text), Contact Preference (dropdown: Email, Phone, Agent), Contract Status (status: Active, Renewal Needed, Inactive). Add calendar view for scheduled appearances and automate notifications when Sunshine Act payments approach annual thresholds."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** KOL Compliance Manager

**Agent Purpose:**  
Maximizes KOL media impact while ensuring perfect regulatory compliance and payment tracking.

**Triggers:**
- New media opportunity identified
- Sunshine Act payment threshold approaching
- Conference speaker opportunity available
- KOL contract renewal deadline
- Competitive KOL activity detection

**Actions:**
- Match KOL expertise to media opportunities based on clinical experience
- Calculate Sunshine Act impact before approving new engagements
- Generate compliant talking points for specific therapeutic areas
- Schedule availability coordination with KOL representatives
- Create regulatory documentation for audit trail
- Monitor competitive KOL activities and opportunities

**Data Required:**
- KOL database with expertise, experience, and payment history
- Sunshine Act payment tracking system
- Media calendar and opportunity pipeline
- FDA compliance guidelines database
- Historical KOL placement effectiveness metrics

**Autonomy Level:** Human-in-the-Loop
Agent recommends optimal KOL matches and manages compliance tracking, with human approval required for high-value placements or compliance-sensitive situations.

**Example Interaction:**
> When Cardiology Today requests expert commentary on new TAVR outcomes data, the KOL Compliance Manager instantly analyzes the request against its database of 127 cardiology KOLs. It identifies three optimal candidates based on TAVR experience, media training level, and Sunshine Act payment status, noting that Dr. Stevens has $8,200 YTD payments (safe for a $2,000 engagement) and recent TAVR trial involvement. The agent pre-drafts compliant talking points avoiding off-label discussion, schedules availability calls with selected KOLs, and creates the documentation trail for Sunshine Act reporting—turning a typically week-long coordination process into same-day KOL placement.

---

### Use Case 5: Regulatory Milestone & Pipeline Communications

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device companies have 10-50 products in various stages of FDA review, requiring coordinated investor relations, employee communications, and market positioning updates. Manual tracking leads to missed investor communication opportunities, internal team misalignment, and competitive disadvantage during regulatory milestone announcements.

#### The Solution
Comprehensive pipeline tracking with automated stakeholder notifications, investor update generation, and competitive intelligence monitoring. Integration with ClinicalTrials.gov and FDA databases for real-time regulatory status updates. Automated generation of internal communications and investor materials.

#### The Outcome
Increase investor engagement during positive regulatory milestones by 40-60%. Improve internal team alignment on pipeline priorities. Reduce administrative communications workload by 50%. Estimated impact: $10-25M in market cap improvement through better investor communications.

#### Discovery Questions
- How many active FDA submissions do you currently have in your pipeline?
- What's your process for communicating regulatory milestones to investors?
- How do you keep internal teams updated on pipeline developments?
- What percentage of regulatory milestones result in formal investor communications?
- How do you track competitive regulatory activities in your therapeutic areas?

#### Industry Context
FDA review timelines are unpredictable but milestone-driven. Investor relations must balance disclosure requirements with competitive sensitivity. Internal teams need pipeline visibility for resource planning. Regulatory milestones significantly impact stock valuations for public medtech companies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a regulatory pipeline communications board with columns: Product Name (text), Indication (text), FDA Pathway (dropdown: 510k, PMA, De Novo, IDE), Current Stage (status: Pre-submission, Under Review, Additional Info Requested, Approved, Complete Response Letter), Expected Decision Date (date), Commercial Priority (dropdown: High, Medium, Low), Investor Material Status (status: Not Required, Draft, Approved, Published), Employee Communication (checkbox), Competitive Benchmark (text), Market Impact Estimate (numbers), Communication Lead (people), Last Update Date (date). Include timeline view for decision dates and automate investor relations team notifications when status changes to 'Approved' with high commercial priority."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Pipeline Communications Director

**Agent Purpose:**  
Orchestrates all stakeholder communications around regulatory pipeline developments and competitive intelligence.

**Triggers:**
- FDA submission status change
- Regulatory decision date approaching (30, 14, 7 days)
- Competitive regulatory announcement detected
- Investor request for pipeline update
- Internal pipeline review meeting scheduled

**Actions:**
- Generate investor presentation slides with regulatory timeline updates
- Create employee communication drafts with appropriate level of detail
- Update analyst consensus models with regulatory assumptions
- Monitor competitor regulatory activities and benchmark progress
- Prepare media materials for significant approvals
- Generate executive briefing materials for investor calls

**Data Required:**
- FDA database integration for real-time status updates
- Competitive intelligence platform connections
- Historical regulatory timeline analysis
- Investor communication preferences and schedules
- Internal stakeholder communication requirements

**Autonomy Level:** Escalation-Based
Agent autonomously maintains pipeline tracking and prepares communication materials, escalating to leadership for strategic decisions about timing and messaging.

**Example Interaction:**
> Three days before the expected FDA decision on CardioDevice Inc.'s next-generation heart valve, the Pipeline Communications Director detects unusual FDA activity suggesting an imminent decision. The agent immediately generates investor update materials showing the device's potential $200M market opportunity, creates employee communication drafts highlighting the R&D team's achievement, and prepares media materials emphasizing the clinical benefits demonstrated in trials. When the approval arrives early on Monday morning, the CEO has complete communication packages ready within hours, enabling immediate investor outreach, coordinated employee announcements, and strategic media placement—capturing maximum market impact from the regulatory milestone.

---

### Use Case 6: Medical Conference Press Coverage & Content Syndication

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Major medical conferences (MEDICA, RSNA, AHA) generate hundreds of potential media opportunities, but manual monitoring and content creation leads to missed coverage opportunities, delayed response to breaking clinical data, and inefficient resource allocation across multiple simultaneous events. Post-conference content syndication requires manual reformatting across multiple channels.

#### The Solution
AI-powered conference monitoring with automated content generation, real-time media opportunity alerts, and multi-channel content syndication. Integration with conference apps and medical news feeds for immediate response capabilities. Automated creation of conference recap materials and follow-up campaigns.

#### The Outcome
Increase conference media coverage by 50-70%. Reduce content creation time by 60%. Accelerate post-conference lead follow-up by 3-5 days. Estimated value: $1-3M annually in improved conference ROI and accelerated sales pipeline development.

#### Discovery Questions
- How many major medical conferences does your team cover annually?
- What percentage of relevant conference presentations do you currently capture for media outreach?
- How long does it take to create and distribute post-conference content?
- What's your strategy for competing for media attention during major conference weeks?
- How do you measure the ROI of conference communications investment?

#### Industry Context
Major conferences have 500-1,000+ presentations with clinical data. Media attention is concentrated during specific time windows. Breaking clinical data can shift competitive landscapes overnight. Post-conference lead follow-up timing is critical for sales conversion. International conferences require 24/7 monitoring across time zones.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a medical conference coverage board with columns: Conference Name (text), Date Range (date range), Key Sessions (text), Company Presentations (text), Competitive Sessions (text), Media Targets (text), Press Release Schedule (status: Not Planned, Scheduled, Distributed), Live Coverage Required (checkbox), Post-Conference Content (status: Not Started, In Progress, Complete), Lead Follow-up Status (status: Pending, Active, Complete), Content Pieces Created (numbers), Media Mentions (numbers), Priority Level (dropdown: High, Medium, Low), Coverage Team (people). Add calendar view for conference dates and automate notifications to marketing team when post-conference content is marked complete."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Conference Coverage Orchestrator

**Agent Purpose:**  
Maximizes media coverage and content creation opportunities during major medical conferences while monitoring competitive activities.

**Triggers:**
- Conference presentation schedules released
- Breaking clinical data announcements during conferences
- Media inquiry related to conference content
- Competitive presentation highlighting superior results
- Post-conference content syndication schedule

**Actions:**
- Generate press materials for company presentations based on clinical data
- Create real-time media alerts for breaking competitive announcements
- Draft post-conference content across multiple formats (blogs, social, newsletters)
- Schedule follow-up campaigns with qualified conference leads
- Monitor and analyze competitive messaging and clinical claims
- Generate conference ROI reports with media coverage metrics

**Data Required:**
- Conference program and presentation databases
- Real-time medical news feeds and social media monitoring
- Media contact lists by therapeutic area and geography
- Historical conference performance and ROI data
- Lead generation and CRM system integration

**Autonomy Level:** Fully Autonomous
Agent operates autonomously during conferences to ensure real-time response capabilities, with periodic human check-ins for strategic adjustments.

**Example Interaction:**
> During the American Heart Association Scientific Sessions, the Conference Coverage Orchestrator monitors 47 relevant presentations while tracking competitor activities. When Dr. Martinez presents groundbreaking TAVR outcomes data showing 30% better results than current standard of care, the agent immediately generates targeted press materials, alerts medical trade publications within 15 minutes, creates LinkedIn content for KOL amplification, and schedules follow-up interviews with 12 cardiothoracic surgeons who attended the session. By the end of the conference day, what typically would require a full week of manual effort has been executed in real-time, generating 8 media placements and 23 qualified leads for the sales team's immediate follow-up.

---

## Industry Terminology

| Term | Definition |
|------|-------------|
| **FDA 510(k)** | Premarket notification proving device is substantially equivalent to existing approved device |
| **PMA (Premarket Approval)** | Most stringent FDA review for Class III high-risk devices requiring clinical trials |
| **De Novo Classification** | FDA pathway for novel devices without predicate devices |
| **IDE (Investigational Device Exemption)** | Permission to use investigational device in clinical studies |
| **KOL (Key Opinion Leader)** | Influential clinicians who shape medical practice and device adoption |
| **Sunshine Act** | Federal law requiring disclosure of payments to healthcare providers |
| **Field Safety Notice** | Communication about device safety issues that don't require recall |
| **CDRH (Center for Devices and Radiological Health)** | FDA center responsible for medical device regulation |
| **Quality System Regulation (QSR)** | FDA manufacturing requirements for medical devices |
| **Adverse Event Reporting** | Required reporting of device-related injuries or malfunctions |
| **Clinical Endpoints** | Measurable outcomes used to evaluate device safety and effectiveness |
| **Predicate Device** | Existing approved device used as comparison for 510(k) submissions |
| **Labeling** | FDA-approved instructions, contraindications, and warnings for device use |
| **Post-Market Surveillance** | Ongoing monitoring of device performance after FDA approval |
| **Real-World Evidence (RWE)** | Data on device use from sources other than traditional clinical trials |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **VP Marketing/Communications** | Overall brand strategy and regulatory communications oversight | High - Budget authority and regulatory interface |
| **Director, Public Relations** | Media relations, crisis communications, conference coverage | High - External messaging and media relationships |
| **Regulatory Affairs** | FDA submission strategy, compliance communications | Critical - Controls regulatory messaging accuracy |
| **Clinical Affairs** | Clinical trial communications, KOL relationships | High - Provides clinical evidence for communications |
| **Medical Director** | Clinical content review, peer-reviewed publications | Critical - Ensures medical accuracy and compliance |
| **Legal Counsel** | Risk assessment, compliance review, crisis management | Critical - Approves all external communications |
| **Investor Relations** | Pipeline communications, milestone announcements | Medium - Focused on financial community |
| **Sales Training** | Field communications, competitive positioning | Medium - Implements commercial messaging |
| **Quality/Regulatory Compliance** | Adverse event communications, field safety notices | High - Drives safety-related communications |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Regulatory Affairs** | Joint submission strategy and regulatory milestone communications | Unified regulatory-commercial communication platform |
| **Clinical Affairs** | Clinical trial results, KOL coordination, publication strategy | Integrated clinical evidence management and amplification |
| **Sales/Marketing** | Commercial messaging alignment, competitive positioning | Single source of truth for clinical claims and competitive intelligence |
| **Quality/Manufacturing** | Product recall communications, field safety notices | Automated crisis communication protocols |
| **R&D** | Pipeline communications, innovation messaging | Technology transfer communication workflows |
| **Legal** | Compliance review, risk assessment for communications | Automated compliance tracking and review processes |
| **Customer Service** | Customer communications during recalls or safety events | Coordinated customer outreach and issue resolution |
| **International** | Global regulatory communications, multi-market launches | Localized communication templates and regulatory requirements |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|--------------------------|
| **Cision/PR Newswire** | Media distribution and monitoring | Replace with unified platform including regulatory compliance tracking |
| **Brandwatch/Mention** | Social media and web monitoring | Consolidate into single AI-powered monitoring and response platform |
| **Salesforce/HubSpot CRM** | Customer and KOL relationship management | Integrate PR/comms data with comprehensive stakeholder management |
| **Veeva Vault** | Regulatory document management | Extend beyond documents to include communication workflows and approval processes |
| **Clinical trial management systems** | Protocol and data management | Connect clinical evidence directly to communication strategy and execution |
| **Regulatory intelligence platforms** | Competitive and regulatory tracking | Integrate competitive intelligence with communication response automation |
| **Crisis communication platforms** | Emergency notification systems | Replace single-purpose tools with comprehensive crisis orchestration |
| **Conference management tools** | Event planning and coverage | Unified conference strategy, execution, and ROI measurement |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"FDA compliance is too complex for automation"** | "monday.com provides audit trails and approval workflows specifically designed for regulated industries. Our compliance templates are built with FDA requirements, and you maintain human oversight for all critical decisions while automating administrative tasks." |
| **"Our regulatory team won't trust AI with compliance content"** | "The AI assists with template generation and workflow management, not final compliance decisions. Your regulatory experts maintain full control over messaging while eliminating manual coordination tasks. Think of it as a regulatory-aware project manager, not a replacement for expertise." |
| **"We need specialized medical device PR expertise"** | "monday.com's flexibility allows you to build workflows that match your exact regulatory requirements and therapeutic area needs. You're not adapting to a generic tool—you're creating a platform that reflects your medical device expertise and compliance requirements." |
| **"Crisis communications are too time-sensitive for new platforms"** | "Speed is exactly why you need automation. Your crisis response improves when template generation, stakeholder notification, and compliance documentation happen instantly rather than manually. You get faster response times with better compliance documentation." |
| **"KOL relationships are too relationship-dependent for automation"** | "AI handles the administrative burden—payment tracking, compliance monitoring, availability coordination—so your team can focus on building better KOL relationships rather than managing spreadsheets and payment calculations." |
| **"We already have specialized medtech marketing tools"** | "monday.com integrates with your existing tools while providing the missing piece: unified communication orchestration. Keep your specialized clinical or regulatory tools, but coordinate all your communications through one intelligent platform." |

## Proof Points
*(To be populated with customer references)*

- [ ] Medical device manufacturer reducing FDA launch communication timeline by 60%
- [ ] Medtech company achieving 100% Sunshine Act compliance while increasing KOL program effectiveness  
- [ ] Class II device manufacturer improving clinical trial communication ROI by $5M+ annually
- [ ] Emergency recall response time reduction from 8 hours to 90 minutes
- [ ] 40% increase in conference media coverage through AI-powered content generation
- [ ] Integration success story with existing Veeva/clinical trial management systems
- [ ] Regulatory affairs team adoption and workflow improvement metrics
- [ ] Crisis communication response improvement during actual product recall event

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*