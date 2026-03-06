# Non-Profit & Charitable Organizations × IT Playbook

## Overview

IT departments in non-profit and charitable organizations occupy a uniquely challenging position: they're expected to deliver enterprise-grade technology capabilities — cybersecurity, data management, systems integration, compliance — on budgets that are a fraction of their for-profit counterparts. The typical non-profit IT team is 1-5 people supporting 50-500 staff plus hundreds or thousands of volunteers, managing a sprawl of donated, discounted, and legacy systems.

Non-profit IT teams typically report to the COO, CFO, or in larger organizations, a CTO or VP of Technology. Their mandate covers infrastructure (cloud, on-prem, hybrid), application management (CRM, HR systems, program databases), cybersecurity (increasingly critical as non-profits hold sensitive donor and beneficiary data), data governance (especially for HIPAA-covered health services, FERPA for education, or PCI for payment processing), and end-user support. They're also increasingly asked to enable digital transformation — online fundraising, virtual programs, mobile-first field operations — without proportional budget increases.

The non-profit tech ecosystem is shaped by donated and discounted software (Microsoft 365 Non-profit, Google for Nonprofits, Salesforce NPSP, TechSoup marketplace), which creates a patchwork architecture. Integration is the perennial challenge: the donor CRM doesn't talk to the finance system, which doesn't talk to the program database, which doesn't talk to the volunteer management tool. IT leaders spend enormous energy maintaining integrations and manual data bridges instead of driving strategic value. Meanwhile, cybersecurity threats are rising — non-profits are attractive targets because they hold financial data, PII, and health information with relatively weak defenses.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Non-profit IT manages 15-30+ tools, many donated/discounted with limited integration. Consolidation reduces licensing, integration maintenance, and training costs dramatically. |
| 2 | Scale Impact Without Overhead | High | IT teams of 1-5 supporting entire organizations need force-multiplication. AI-powered self-service, automation, and monitoring let tiny teams deliver enterprise-grade support. |
| 3 | Replace or Radically Augment Headcount | Medium-High | Can't hire a full security team, DBA, and help desk — AI augmentation lets one IT generalist cover multiple specialist domains. |

## Prioritized Use Cases

---

### Use Case 1: IT Service Desk & Help Desk Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Non-profit IT teams are drowning in help desk requests that arrive through every channel: email, Slack/Teams messages, walk-ups, phone calls, and sticky notes on the IT person's monitor. There's no ticketing system (or one that nobody uses because it's too complex — often a donated Zendesk or Freshdesk instance that was never properly configured). Password resets, equipment requests, software access, and "the printer isn't working" all compete for attention with strategic projects. The IT director who should be planning a CRM migration is instead resetting passwords and troubleshooting someone's Zoom connection. Without tracking, there's no data on common issues, resolution times, or workload — which means no case for additional budget or headcount.

#### The Solution
monday.com Service provides a purpose-built **IT Help Desk** that staff actually use because it's intuitive. A **monday.com Form** captures requests (issue type, urgency, description, screenshot upload) and feeds them into a ticket board. Columns track: requester, category (hardware, software, access, network, security), priority (critical/high/medium/low), status (new/assigned/in progress/waiting on user/waiting on vendor/resolved/closed), assigned technician, SLA deadline, and resolution notes. Automations handle triage: password resets auto-assign to Tier 1, security incidents escalate immediately, new tickets notify the IT team channel. **Kanban view** gives the team a visual workflow. **Dashboard** tracks open tickets, average resolution time, tickets by category (identifying training needs), and SLA compliance.

#### The Outcome
- 70% of requests captured through self-service form (down from scattered channels)
- Average resolution time reduced from 3 days to 8 hours
- IT director reclaims 10+ hours/week from ad hoc interruptions
- Data-driven budget requests: "We resolved 847 tickets last quarter, 40% were password-related — here's the case for SSO"
- Staff satisfaction improvement through transparent ticket tracking

#### Discovery Questions
1. "How does your staff currently submit IT support requests? Is there a formal process or is it mostly Slack messages and walk-ups?"
2. "How many IT support staff do you have relative to total headcount? What's your ratio?"
3. "Do you know your average ticket resolution time? Can you identify your top 5 most common request types?"
4. "Have you ever tried a ticketing system that didn't stick? What went wrong?"
5. "When the board asks 'why do we need more IT budget?' — do you have data to support the case?"

#### Industry Context
Non-profit IT support is complicated by diverse user populations: full-time staff, part-time staff, volunteers (who may use personal devices), board members (who expect executive-level support), and sometimes program participants (computer labs, digital literacy programs). BYOD policies are common but rarely formalized. The tech skill level varies enormously — from digital-native development staff to program staff who struggle with email attachments. TechSoup provides discounted help desk tools (Zendesk, Freshdesk) but implementation support is limited, leading to high abandonment rates.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Help Desk system with one main board and a knowledge base:
>
> **Board 1 — IT Service Desk:** Columns: Ticket ID (auto-number), Subject (text), Requester (people), Requester Department (dropdown: Programs, Development, Finance, Operations, HR, Marketing, Executive, Volunteer, Board Member), Category (dropdown: Password/Access, Hardware, Software, Network/WiFi, Printer, Email, Security Incident, New Equipment Request, Software Installation, VPN/Remote Access, Phone System, Website, Database, Other), Priority (status: Critical, High, Medium, Low), Status (status: New, Assigned, In Progress, Waiting on User, Waiting on Vendor, Waiting on Parts, Resolved, Closed), Assigned To (people), SLA Deadline (date), Date Submitted (date), Date Resolved (date), Resolution Time Hours (formula), Description (long text), Resolution Notes (long text), Attachments (files), Satisfaction Rating (rating). Groups: Open Tickets, Waiting, Resolved This Week, Closed. Form: IT Support Request form with Subject, Description, Category, Priority (default Medium), Attachments. Automations: When form submitted, set Status to New and notify IT team channel. When Category is Security Incident, set Priority to Critical and notify IT Director immediately. When Category is Password/Access, auto-assign to Tier 1 tech. When Status is Resolved for 3 days with no response, change to Closed. Dashboard: Open tickets by priority, tickets by category pie chart, average resolution time trend, SLA compliance percentage, tickets per week trend."
>
> **Board 2 — IT Knowledge Base:** Columns: Article Title (text), Category (dropdown: same as Service Desk), Solution Steps (long text), Audience (dropdown: Staff Self-Service, IT Team, Volunteers), Last Updated (date), Author (people), Views (numbers), Helpful (numbers). Purpose: Common solutions staff can reference before submitting a ticket."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** IT Support Bot
**Agent Purpose:** Provide first-line IT support by auto-resolving common issues, intelligently routing complex tickets, and maintaining the knowledge base.

**Triggers:**
- When a new ticket is submitted via form
- When a ticket has been in "Waiting on User" status for 48+ hours
- When a ticket is marked Resolved (trigger satisfaction survey)
- Weekly analysis of ticket patterns
- When a Critical priority ticket is created

**Actions:**
- Analyze incoming ticket descriptions and suggest Knowledge Base solutions before assigning to a human
- Auto-resolve common requests: password reset instructions, WiFi connection guides, VPN setup steps — with links to knowledge base articles
- Intelligently categorize and prioritize tickets based on description keywords and requester context
- Route tickets to the appropriate technician based on category expertise and current workload
- Generate weekly IT metrics report: tickets opened/closed, categories, resolution times, emerging trends
- Identify knowledge gaps: when the same issue appears 5+ times without a KB article, draft one

**Data Required:**
- IT Service Desk board (all tickets)
- Knowledge Base board (solution articles)
- Staff directory (for requester context)
- System monitoring alerts (if integrated)

**Autonomy Level:** Escalation-Based
Auto-resolves Tier 0 issues (documented solutions), routes and categorizes all tickets autonomously, escalates Critical issues and unrecognized problems to IT Director.

**Example Interaction:**
> A program manager submits: "Can't access the shared drive from home — getting 'access denied' error." IT Support Bot responds within 60 seconds: "Hi Sarah! This is a common VPN issue. Here are two quick steps: (1) Make sure you're connected to the VPN — look for the shield icon in your taskbar. Here's our VPN guide: [link]. (2) If you're connected and still getting the error, your network password may have expired — try changing it at password.ourorg.org first. If neither of these works, I'll escalate to Alex on the IT team. Does this resolve your issue?" Sarah confirms the VPN was disconnected, ticket auto-resolves, and the knowledge base article's "helpful" counter increments.

---

### Use Case 2: Technology Asset & License Management

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Non-profit IT teams manage a chaotic mix of purchased, donated, and discounted software licenses — Microsoft 365 (donated via TechSoup), Google Workspace for Nonprofits (free), Salesforce (10 free NPSP licenses, then $36/user/month), Zoom (discounted), plus dozens of department-purchased SaaS tools that IT may not even know about (shadow IT). Hardware is equally messy: donated computers of varying ages, grant-funded equipment with tracking requirements, staff laptops, shared workstations, and mobile devices. Nobody knows exactly how many licenses they're paying for, which are actually being used, or when equipment warranties expire. The result: wasted spend on unused licenses ($10-30K/year at mid-size orgs), compliance risk on grant-funded equipment, security risk from unpatched/unmanaged devices, and IT scrambling when an employee leaves and nobody knows what systems they have access to.

#### The Solution
monday.com Work Management creates a comprehensive **Technology Asset Management** system. A **Hardware Inventory Board** tracks every device: type, serial number, assigned user, purchase date, warranty status, funding source (critical for grant compliance), condition, and OS/patch status. A **Software & License Board** tracks every application: vendor, license type (donated/paid/free), number of licenses, assigned users, renewal date, annual cost, and usage status. A connected **Employee Tech Profile Board** shows what each person has: devices assigned, software access, accounts to deprovision on departure. Automations alert IT when licenses are up for renewal (60 days out), warranties are expiring, or grant-funded equipment needs its biennial inventory check.

#### The Outcome
- $15-25K annual savings from eliminating unused software licenses
- Complete hardware inventory for grant compliance and insurance
- Employee offboarding checklist ensures no orphaned accounts (security risk reduction)
- License renewal planning prevents service interruptions
- Shadow IT visibility — finally know what the organization is actually using

#### Discovery Questions
1. "Do you have a complete inventory of all software your organization uses — including tools departments purchased on their own?"
2. "How do you manage TechSoup donations and Microsoft/Google non-profit licenses? Do you know your utilization rate?"
3. "When an employee leaves, what's the offboarding process for IT? How long does it take to deprovision all accounts?"
4. "Do you have grant-funded equipment that needs tracking for compliance? When was your last physical inventory?"
5. "Have you ever been surprised by an auto-renewal for a tool nobody uses anymore?"

#### Industry Context
Non-profit technology procurement is heavily influenced by TechSoup (the clearinghouse for donated and discounted technology — Microsoft, Google, Adobe, Salesforce, and hundreds of others). Organizations must validate their 501(c)(3) status for eligibility. Key licensing considerations: Microsoft 365 E1/Business Basic is donated (free), but E3/E5 is deeply discounted but not free; Salesforce offers 10 free Power of Us licenses; Google Workspace for Nonprofits is free for core; and many vendors offer 50-80% non-profit discounts. Shadow IT is rampant because departments adopt free-tier tools (Canva, Mailchimp, SurveyMonkey) without IT's knowledge. NIST Cybersecurity Framework adoption is increasingly expected by funders and cyber insurers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Technology Asset & License Management system with three connected boards:
>
> **Board 1 — Hardware Inventory:** Columns: Asset Tag (text), Device Type (dropdown: Laptop, Desktop, Tablet, Phone, Printer, Network Equipment, Server, Monitor, Projector, Other), Make/Model (text), Serial Number (text), Assigned To (people), Department (dropdown: Programs, Development, Finance, Operations, HR, Marketing, Executive, IT, Shared/Lab), Location (dropdown: Main Office, North Center, South Shelter, Remote, Storage), Status (status: Active, Spare, Repair, Decommissioned, Lost/Stolen), Purchase Date (date), Purchase Price (numbers, currency USD), Funding Source (dropdown: Operating Budget, Federal Grant, State Grant, Foundation Grant, TechSoup Donation, Corporate Donation, Individual Donation), Grant Number (text), Warranty Expiry (date), OS Version (text), Last Patched (date), Condition (status: Excellent, Good, Fair, Poor, End of Life), Notes (long text). Automations: When Warranty Expiry is 30 days away, notify IT Director. When Last Patched is more than 30 days ago, flag for patching. When Condition is End of Life, create disposition task.
>
> **Board 2 — Software & Licenses:** Columns: Application Name (text), Vendor (text), Category (dropdown: CRM/Donor Management, Finance/Accounting, HR/Payroll, Communication, Productivity, Security, Database, Design, Analytics, Program-Specific, Website, Email Marketing, Other), License Type (dropdown: Donated-TechSoup, Non-Profit Free Tier, Non-Profit Discounted, Paid Full Price, Open Source, Free Tier), Total Licenses (numbers), Licenses In Use (numbers), Utilization Rate (formula: In Use divided by Total times 100), Annual Cost (numbers, currency USD), Renewal Date (date), Auto-Renew (checkbox), Contract Owner (people), Department Owner (dropdown), SSO Integrated (checkbox), Data Classification (dropdown: Public, Internal, Confidential, Restricted), Notes (long text). Automations: When Renewal Date is 60 days away, notify Contract Owner and IT Director. When Utilization Rate is below 50%, flag for review. Dashboard: total annual software spend, licenses by type (donated vs paid), utilization rates, upcoming renewals.
>
> **Board 3 — Employee Tech Profile:** Columns: Employee Name (people), Department (dropdown), Start Date (date), Hardware Assigned (connect to Hardware Inventory), Software Access (connect to Software & Licenses), Email Account (text), VPN Access (checkbox), Admin Privileges (checkbox), Departure Date (date), Offboarding Status (status: Active, Offboarding In Progress, Complete), Offboarding Checklist (long text: device returned, email forwarded, passwords changed, accounts disabled, data backed up). Automations: When Departure Date is set, change Offboarding Status to In Progress and create offboarding task list. When all checklist items complete, change to Complete."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Tech Asset Guardian
**Agent Purpose:** Maintain real-time visibility into all technology assets and licenses, optimize spending, ensure compliance, and automate lifecycle management.

**Triggers:**
- Monthly license utilization review
- When a software renewal date is 60 days away
- When an employee departure date is set
- Quarterly grant-funded equipment compliance check
- When a new software request is submitted
- Weekly security patch compliance scan

**Actions:**
- Generate monthly software spend report with utilization analysis and cancellation/downgrade recommendations
- Create comprehensive employee offboarding checklists with all systems, devices, and accounts to deprovision
- Compare new software requests against existing tools to prevent duplicate purchases ("We already have Canva Pro — you don't need Adobe Express")
- Compile grant-funded equipment inventory reports for audit readiness
- Flag devices that are past end-of-life, unpatched, or missing from inventory
- Alert IT when TechSoup donation eligibility windows open for needed software

**Data Required:**
- Hardware Inventory board
- Software & Licenses board
- Employee Tech Profile board
- TechSoup account details
- Vendor contract documents

**Autonomy Level:** Human-in-the-Loop
Generates reports and recommendations autonomously. Requires IT Director approval for: license cancellations, hardware decommissioning, and access changes.

**Example Interaction:**
> Tech Asset Guardian's monthly report: "💻 Tech Portfolio Review — February 2026: (1) SAVINGS OPPORTUNITY: Mailchimp ($2,400/year) — only 2 of 5 licensed users sent campaigns in the last 90 days. Development team is using it but Programs and Marketing haven't logged in since October. Recommend downgrading to 2-seat plan, saving $1,440/year. (2) RENEWAL ALERT: Zoom Business renewal ($3,200) hits March 15 with auto-renew ON. Current utilization: 34 of 50 licenses active. Recommend right-sizing to 40 licenses, saving $640/year. (3) COMPLIANCE: 8 grant-funded laptops (DOJ Grant #2024-VW-113) need biennial physical inventory by April 30. I've created a verification checklist. (4) SHADOW IT DETECTED: I found 3 new SaaS tools being used by staff (Notion, Loom, Calendly free tier) — none have signed BAAs or data processing agreements. Flagging for security review."

---

### Use Case 3: Cybersecurity Incident Response & Compliance

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Non-profits are increasingly targeted by cybercriminals — they hold donor financial data, beneficiary PII (sometimes including health and immigration records), and have weaker defenses than commercial organizations. A 2024 NTEN survey found that 27% of non-profits experienced a cybersecurity incident in the prior year, yet only 34% had an incident response plan. The IT team (often 1-2 people) can't possibly maintain a SOC or dedicated security function. Meanwhile, cyber insurance carriers are requiring documented security policies, incident response plans, and evidence of basic controls (MFA, endpoint protection, backup procedures) as conditions of coverage. HIPAA, FERPA, PCI-DSS, and state privacy laws add compliance complexity depending on the organization's programs.

#### The Solution
monday.com Work Management creates a **Cybersecurity Management System**. A **Security Incident Board** provides a structured response workflow: detection → triage → containment → eradication → recovery → lessons learned, with severity levels that trigger appropriate escalation. A **Security Controls Board** tracks the organization's security posture: control name, status (implemented/partial/planned/not applicable), evidence, owner, and last review date — mapped to NIST CSF or CIS Controls. A **Compliance Calendar** tracks all security-related obligations: annual risk assessments, policy reviews, training deadlines, insurance renewals, and audit dates. Automations escalate high-severity incidents, remind control owners of review dates, and compile audit-ready documentation.

#### The Outcome
- Documented incident response capability (often required for cyber insurance)
- 80% reduction in time to compile audit/compliance documentation
- Clear ownership and accountability for security controls
- Audit-ready evidence for HIPAA, PCI, or state privacy requirements
- Reduced cyber insurance premiums through demonstrated security maturity

#### Discovery Questions
1. "Do you have a documented cybersecurity incident response plan? When was it last tested?"
2. "What compliance frameworks apply to your organization — HIPAA, FERPA, PCI, state privacy laws?"
3. "Do you have cyber insurance? What controls does your carrier require for coverage?"
4. "Is MFA enabled across all critical systems? What percentage of staff have completed security awareness training?"
5. "If you had a data breach involving donor financial information, could you execute your notification process within 72 hours?"

#### Industry Context
Non-profit cybersecurity is shaped by limited budgets, diverse user populations (staff, volunteers, board members on personal devices), and sensitive data (donor financials, beneficiary PII, health records, immigration status). Common frameworks: NIST Cybersecurity Framework (most accessible for non-profits), CIS Controls (prioritized, practical), and HIPAA Security Rule (for health services). Key threats: business email compromise (BEC — fake CEO asking finance to wire funds), ransomware, phishing targeting development staff (fake donor communications), and insider threats (volunteer access to sensitive data). TechSoup and organizations like the Global Cyber Alliance offer free security tools for non-profits.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Cybersecurity Management system with three connected boards:
>
> **Board 1 — Security Incident Tracker:** Columns: Incident ID (auto-number), Title (text), Date Detected (date), Reported By (people), Severity (status: Critical, High, Medium, Low), Category (dropdown: Phishing, Malware/Ransomware, Unauthorized Access, Data Breach, Lost/Stolen Device, BEC/Wire Fraud Attempt, Account Compromise, Insider Threat, Website Defacement, DDoS, Other), Status (status: Detected, Triaging, Contained, Eradicating, Recovering, Resolved, Post-Incident Review), Incident Commander (people), Affected Systems (tags: Email, CRM, Finance System, Website, File Server, Database, Network, Endpoint), Affected Data Types (tags: Donor PII, Financial Data, Beneficiary PII, Health Records, Employee Data, None), Number of Records Affected (numbers), Notification Required (checkbox), Notification Deadline (date), Containment Actions (long text), Root Cause (long text), Lessons Learned (long text), Insurance Claim Filed (checkbox). Automations: When Severity is Critical, immediately notify IT Director, COO, and Executive Director. When Notification Required is checked, create notification task with deadline. When Status changes to Resolved, create Post-Incident Review task due in 5 business days.
>
> **Board 2 — Security Controls Tracker:** Columns: Control Name (text), Framework (dropdown: NIST CSF, CIS Controls, HIPAA, PCI-DSS, Internal Policy), Control ID (text), Category (dropdown: Identify, Protect, Detect, Respond, Recover), Status (status: Fully Implemented, Partially Implemented, Planned, Not Applicable, Gap), Owner (people), Evidence (files), Last Review Date (date), Next Review Date (date), Risk Level if Missing (status: Critical, High, Medium, Low), Implementation Notes (long text), Remediation Plan (long text), Target Date (date). Groups: by Framework Category. Automations: When Next Review Date is 14 days away, notify Owner. Dashboard: security posture heat map showing controls by status, gaps by category, timeline to remediation.
>
> **Board 3 — Compliance Calendar:** Columns: Task Name (text), Compliance Area (dropdown: Cyber Insurance, HIPAA, PCI, Privacy Policy, Risk Assessment, Penetration Test, Security Training, Policy Review, Vendor Assessment, Backup Test, DR Test), Due Date (date), Frequency (dropdown: Annual, Semi-Annual, Quarterly, Monthly, One-Time), Status (status: Upcoming, In Progress, Complete, Overdue), Owner (people), Documentation (files), Notes (long text). Automations: When Due Date is 30 days away, notify Owner. When Status is Overdue, notify IT Director and COO."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Cyber Sentinel
**Agent Purpose:** Continuously monitor the organization's security posture, guide incident response, and maintain compliance documentation — serving as the virtual CISO that small non-profit IT teams can't afford to hire.

**Triggers:**
- When a security incident is reported (any severity)
- Daily scan for overdue security controls reviews
- Monthly compliance status assessment
- When cyber insurance renewal is 90 days away
- When a new compliance requirement is identified
- Quarterly security posture report generation

**Actions:**
- Guide incident response step-by-step: upon incident creation, generate a response checklist tailored to the incident category with containment steps, communication templates, and regulatory notification requirements
- Assess which data breach notification laws apply based on affected data types and records (state laws, HIPAA, etc.)
- Generate compliance dashboards showing security posture scores, gaps, and remediation timelines
- Compile cyber insurance renewal documentation: control evidence, incident history, training records
- Draft security policies and procedures based on NIST CSF controls
- Analyze incident patterns to recommend preventive investments

**Data Required:**
- Security Incident Tracker board
- Security Controls Tracker board
- Compliance Calendar board
- Staff training records
- System configuration data

**Autonomy Level:** Human-in-the-Loop
Generates guidance, reports, and documentation autonomously. All incident response actions, external communications, and policy decisions require IT Director approval. Never executes technical remediation — only recommends.

**Example Interaction:**
> A staff member reports a suspicious email. Cyber Sentinel activates: "🔒 Incident #47 created — Category: Phishing. Initial triage: (1) The email claims to be from your Executive Director requesting W-2 files for all employees. This is a classic BEC/W-2 phishing attack — very common in non-profits during tax season. (2) Immediate containment steps: Block the sender domain, send an all-staff alert (draft attached) warning about the email, check if anyone replied or clicked links. (3) If anyone sent data: This triggers state data breach notification requirements. For your 3 operating states (NY, CA, FL), notification deadlines are: NY — 'most expeditious time,' CA — 72 hours, FL — 30 days. I've created notification deadline tasks. (4) Post-incident: I recommend enabling external email banners ('This message is from outside the organization') — it's CIS Control 9.6 and currently listed as a gap in your controls tracker. Want me to draft the implementation plan?"

---

### Use Case 4: IT Project & Initiative Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Non-profit IT teams juggle multiple strategic projects alongside daily operations — CRM migrations, website redesigns, network upgrades, cloud transitions, new program launches requiring tech setup — with no formal project management. The IT director keeps a mental list of priorities that shifts weekly based on whoever is yelling loudest. Without project visibility, leadership doesn't understand why the CRM migration is taking 9 months instead of 3, or why the website hasn't been redesigned yet. Scope creep is endemic because there's no requirements process. Vendor management for implementations is ad hoc. And the "IT strategic plan" is a wish list in a document nobody reads, disconnected from actual execution.

#### The Solution
monday.com Work Management creates an **IT Project Portfolio** system. A master **IT Projects Board** tracks all initiatives: project name, sponsor, status, priority, timeline, budget, resource allocation, and strategic alignment. Each project can expand into a detailed **Project Plan Board** with phases, tasks, dependencies, and milestones on a **Timeline/Gantt view**. A **Vendor Management Board** tracks implementation partners, contracts, SLAs, and deliverables. The **Portfolio Dashboard** gives leadership a single view: what's in progress, what's planned, resource utilization, budget status, and strategic alignment. Automations flag at-risk projects (overdue milestones, budget overruns) and generate weekly status updates.

#### The Outcome
- Complete visibility into IT project portfolio for leadership
- 40% improvement in project on-time delivery through structured management
- Scope creep reduction through documented requirements and change management
- Resource conflict identification before it causes delays
- Strategic alignment — IT investments clearly connected to organizational priorities

#### Discovery Questions
1. "How many IT projects or initiatives are currently in progress? Can you list them all?"
2. "How do you prioritize when the ED wants a CRM migration and the Development Director wants a new website — at the same time?"
3. "Do you have an IT strategic plan? How is it connected to day-to-day project execution?"
4. "What's your biggest IT project failure or delay in the last 2 years? What caused it?"
5. "How do you communicate IT project status to leadership? Is it a formal process or ad hoc?"

#### Industry Context
Non-profit IT projects are uniquely challenging: budgets often come from restricted grants (can only spend on what was proposed), timelines must align with funder reporting periods, implementations must accommodate high staff turnover and volunteer populations, and the organization rarely has internal project management expertise. Common IT projects: CRM migration (Salesforce NPSP implementation is a 6-18 month initiative), website redesign (often Wordpress on donated hosting), Microsoft 365 or Google Workspace rollout, cybersecurity improvements (MFA, endpoint protection), data warehouse/BI implementation, and digital transformation of program delivery (telehealth, virtual tutoring, online intake). Implementation partners specializing in non-profit tech include Cloud for Good, Exponent Partners, and Heller Consulting.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Project Portfolio system with two connected boards:
>
> **Board 1 — IT Project Portfolio:** Columns: Project Name (text), Project Sponsor (people), IT Lead (people), Status (status: Proposed, Approved, Planning, In Progress, On Hold, Completed, Cancelled), Priority (status: Critical, High, Medium, Low), Strategic Goal (dropdown: Improve Security, Modernize Infrastructure, Enhance Donor Experience, Enable Programs, Reduce Costs, Compliance, Digital Transformation), Start Date (date), Target End Date (date), Actual End Date (date), Budget (numbers, currency USD), Spent to Date (numbers, currency USD), Budget Remaining (formula), Funding Source (dropdown: Operating, Capital, Grant-Funded, Donated Services), Phase (dropdown: Initiation, Planning, Execution, Testing, Deployment, Closeout), Risk Level (status: Green, Yellow, Red), Vendor (text), Dependencies (dependency), Description (long text), Success Criteria (long text). Groups: Active Projects, Pipeline, Completed. Views: Timeline/Gantt, Dashboard showing portfolio status, budget allocation, resource utilization, projects by strategic goal.
>
> **Board 2 — IT Project Tasks:** Columns: Task Name (text), Project (connect to Portfolio), Phase (dropdown: Initiation, Planning, Execution, Testing, Deployment, Closeout), Assigned To (people), Status (status: Not Started, In Progress, Blocked, Complete), Priority (status: Critical, High, Medium, Low), Due Date (date), Dependencies (dependency), Estimated Hours (numbers), Actual Hours (numbers), Notes (long text). Views: Timeline view with dependencies, Kanban by status. Automations: When Status changes to Blocked, notify IT Lead on connected project. When all tasks for a Phase are Complete, notify Project Sponsor."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** IT Portfolio Manager
**Agent Purpose:** Track all IT projects, surface risks before they become problems, and keep leadership informed with minimal manual effort from the IT team.

**Triggers:**
- Weekly project status review (every Monday)
- When any task changes to "Blocked" status
- When project spending exceeds 80% of budget
- When a milestone is overdue by more than 3 days
- Monthly portfolio health report generation

**Actions:**
- Generate weekly status updates for each active project, highlighting progress, risks, and upcoming milestones
- When a task is blocked, analyze dependencies and suggest resolution paths
- Flag resource conflicts when the same person is assigned to overlapping critical tasks across projects
- Compile monthly portfolio health reports for COO/ED: projects on track vs. at risk, budget utilization, strategic alignment
- When a project is proposed, estimate resource requirements based on similar past projects
- Track vendor deliverables against contract milestones and SLAs

**Data Required:**
- IT Project Portfolio board
- IT Project Tasks board
- Team capacity/availability
- Vendor contracts and SLAs

**Autonomy Level:** Human-in-the-Loop
Generates reports and risk alerts autonomously. Requires IT Director approval for: scope changes, budget reallocation, and vendor escalations.

**Example Interaction:**
> Monday morning, IT Portfolio Manager briefs the IT Director: "📊 Weekly IT Portfolio Status: 5 active projects. (1) CRM Migration (Salesforce → Phase 3 Data Migration): 🟡 YELLOW — data cleansing taking longer than planned. 12,000 of 45,000 donor records have merge conflicts. Recommend extending Phase 3 by 2 weeks and requesting volunteer data stewards from the Development team. (2) MFA Rollout: 🟢 GREEN — 87% of staff enrolled. Remaining 13% are primarily field staff — scheduled training sessions this week. (3) Website Redesign: 🔴 RED — Vendor missed wireframe delivery by 10 days, no communication in a week. Recommend escalation call with vendor project manager — I've drafted an email. (4) Network Upgrade - South Shelter: 🟢 GREEN — equipment ordered, installation scheduled March 1. (5) Budget alert: CRM Migration has spent $34K of $40K budget with 2 phases remaining. Recommend discussing contingency with CFO."

---

### Use Case 5: Technology Onboarding & Offboarding

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Non-profits have high turnover — the sector average is 19% annually, and some program roles turn over at 25-30%. Each new hire needs: a laptop provisioned, email account created, software installed and licensed, access granted to CRM/finance/program systems, VPN configured, phone set up, and training scheduled. Each departure requires the reverse: device collected, accounts disabled, email forwarded/archived, shared drive permissions revoked, and licenses reclaimed. When IT manages this from memory or a Word document checklist, things get missed — a departed employee's Salesforce login remains active for months, a new hire waits a week for email access. For organizations handling sensitive data (donor financials, beneficiary health records), failed offboarding creates real security and compliance risk.

#### The Solution
monday.com Work Management creates automated **Onboarding and Offboarding Workflows**. When HR creates a new hire (or connects to an HR system), an automation generates a complete **IT Onboarding Checklist**: every account, device, software, training, and access item as a sub-item with owner and deadline. The checklist is templated by role — a program manager gets different systems than a development officer. Status columns track completion, and automations remind IT staff of pending items and escalate when deadlines pass. **Offboarding** mirrors this: departure date triggers a security-focused checklist ensuring all access is revoked within 24 hours and devices are collected. Dashboards show onboarding/offboarding pipeline, completion rates, and average time-to-productivity.

#### The Outcome
- New hire productive on Day 1 (vs. Day 3-5 waiting for access)
- 100% offboarding completion rate — zero orphaned accounts
- IT onboarding time reduced from 4 hours to 45 minutes per hire through templates
- Audit-ready documentation of access provisioning and deprovisioning
- Consistent experience regardless of which IT staff member handles it

#### Discovery Questions
1. "What's your annual staff turnover rate? How many new hires and departures do you process per month?"
2. "When a new hire starts, how long until they have access to all the systems they need?"
3. "Can you confidently say that every departed employee has had all system access revoked within 24 hours?"
4. "Is your onboarding process documented, or does it depend on which IT person handles it?"
5. "Do volunteers get system access? How is that managed differently from staff?"

#### Industry Context
Non-profit workforce management is complex: full-time staff, part-time staff, AmeriCorps members (federal service program with specific IT requirements), interns, volunteers (some needing system access, some not), consultants, and board members each need different access levels. Many organizations operate on a fiscal year that creates batch hiring/departure cycles (especially grant-funded positions that start/end with grant periods). NIST SP 800-53 AC-2 (Account Management) and the CIS Controls framework both emphasize timely deprovisioning as a critical security control.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Technology Onboarding & Offboarding system:
>
> **Board — IT Onboarding & Offboarding:** Columns: Employee Name (text), Type (dropdown: New Hire Onboarding, Departure Offboarding, Role Change, Volunteer Access, Intern, AmeriCorps, Board Member), Department (dropdown: Programs, Development, Finance, Operations, HR, Marketing, Executive, IT), Role Title (text), Manager (people), Start/End Date (date), IT Assignee (people), Overall Status (status: Not Started, In Progress, Complete, Blocked), Hardware Status (status: Not Started, Ordered, Configured, Delivered, Collected), Account Status (status: Not Started, Created, Active, Disabled, Archived), Remote Access Needed (checkbox), Equipment Assigned (text), Email Account (text), Systems Access Required (tags: Email, CRM-Salesforce, Finance-QuickBooks, HR-Payroll, Shared Drive, VPN, Zoom, Slack-Teams, Program Database, Website CMS, Grant Management, Volunteer Portal), Training Scheduled (checkbox), Completion Date (date), Notes (long text).
>
> Groups: Active Onboarding, Active Offboarding, Completed.
>
> Automations: When a new item is created with Type 'New Hire Onboarding', auto-create sub-items: Provision laptop, Create email account, Set up VPN, Grant CRM access, Grant finance system access (if Finance dept), Schedule IT orientation, Create Zoom account, Add to Slack/Teams channels, Set up phone, Enroll in security training. When Type is 'Departure Offboarding', auto-create sub-items: Disable email account (due: departure date), Revoke VPN access (due: departure date), Disable CRM access (due: departure date), Collect laptop (due: departure date), Forward email to manager (due: departure date), Archive files (due: departure date + 3 days), Reclaim software licenses (due: departure date + 1 day), Remove from distribution lists (due: departure date). When Start/End Date is 5 days away and Overall Status is Not Started, notify IT Assignee urgently. Dashboard: active onboarding/offboarding by status, average completion time, systems access heatmap."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Access Lifecycle Manager
**Agent Purpose:** Automate and track the complete technology access lifecycle for every person in the organization — from first login to final deprovisioning.

**Triggers:**
- When a new onboarding or offboarding item is created
- When Start/End Date is 5 business days away and checklist is incomplete
- Daily scan for overdue onboarding/offboarding tasks
- When an employee's role changes
- Monthly orphaned account audit

**Actions:**
- Generate role-specific onboarding checklists based on department and position (a Development Associate gets Salesforce + Mailchimp; a Case Manager gets program database + HIPAA training)
- Track sub-item completion and send progressive reminders with escalation
- For offboarding, verify each account is disabled by checking status and generating a deprovisioning certification document
- Monthly orphaned account scan: cross-reference active accounts against current employee roster and flag discrepancies
- Compile quarterly access review reports for compliance (who has access to what, when was it last certified)
- When role changes occur, identify access that should be added and removed

**Data Required:**
- Onboarding & Offboarding board
- Employee Tech Profile board
- Software & Licenses board
- HR system integration (new hires, departures)

**Autonomy Level:** Escalation-Based
Creates checklists and sends reminders autonomously. Escalates overdue offboarding tasks (security risk) directly to IT Director and COO. Never disables accounts directly — creates verified tasks for IT staff.

**Example Interaction:**
> Access Lifecycle Manager detects a new onboarding entry: "👤 New hire: Maria Gonzalez, Program Manager — Youth Services. Start date: March 3 (5 business days). Based on the Program Manager role template: I've created 14 onboarding tasks including: laptop provisioning (I see 2 spare Dell Latitude 5540s in inventory — recommending Asset #LAP-089 which was reimaged last week), email, VPN, Salesforce (Program User license), case management database, Zoom, Teams, shared drive access to Youth Services folder, and HIPAA security training enrollment (required — Youth Services handles minor PII). I've assigned hardware tasks to Alex and account creation to Sam based on current workload. All tasks are due by March 3 EOD. Also: Maria will need a background check clearance uploaded before she gets database access to minor records — I've flagged this as a dependency."

---

### Use Case 6: Data Governance & Integration Management

**Relevance:** Medium-High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
The average mid-size non-profit uses 15-30 software tools, and the data lives in silos. Donor records are in Salesforce, financial data is in QuickBooks or Sage Intacct, program data is in a custom database or spreadsheets, volunteer data is in SignUpGenius or a spreadsheet, HR data is in a payroll system, and marketing data is in Mailchimp. When the ED asks "how many people did we serve last year and what did it cost per person?" — the IT team spends days pulling data from multiple systems, reconciling discrepancies, and building a manual report. Data quality is poor: duplicate donor records, inconsistent naming conventions, missing fields. There's no data dictionary, no single source of truth, and no governance framework. Integration attempts fail because they're built ad hoc and break when one system updates.

#### The Solution
monday.com Work Management creates a **Data Governance Hub**. A **Systems & Integration Map Board** documents every system in use: what data it holds, who owns it, how it connects to other systems, integration method (API, Zapier, manual export, monday.com native), and data refresh frequency. A **Data Quality Board** tracks known issues: duplicate records, incomplete fields, inconsistencies — with assigned owners and remediation timelines. A **Data Request Board** lets staff submit analytics requests through a form, which IT triages and fulfills (or points to self-service dashboards). monday.com's native integrations and API connect to the core stack, becoming the operational layer that bridges data silos.

#### The Outcome
- Documented data architecture — any team member can understand the data landscape
- 60% reduction in ad hoc data request turnaround time
- Systematic data quality improvement with tracked metrics
- Integration monitoring prevents silent failures
- Foundation for future data warehouse or BI implementation

#### Discovery Questions
1. "If the board asked for a unified view of participants served, volunteer hours, and cost-per-outcome — how long would it take to produce?"
2. "How many systems hold data about the same people (donors who are also volunteers who are also program participants)?"
3. "Do you have documented integrations between your systems, or are there manual data bridges (CSV exports, copy-paste)?"
4. "Who owns data quality in your organization? Is there a data governance policy?"
5. "Have you experienced an integration failure that went unnoticed for days or weeks?"

#### Industry Context
Non-profit data ecosystems typically center around a CRM (Salesforce NPSP, Bloomerang, Raiser's Edge NXT) as the donor system of record, with disconnected systems for programs, finance, HR, and communications. The rise of outcomes-focused funding is driving demand for integrated data — funders want to see the connection between investment and impact, which requires linking financial and program data. Common integration tools: Zapier (popular for non-technical teams), monday.com native integrations, MuleSoft (for Salesforce orgs), and increasingly APIs. The concept of a "constituent relationship management" approach (versus just donor CRM) recognizes that one person may be a donor, volunteer, event attendee, and program participant simultaneously — and they need a unified record.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Data Governance Hub with three connected boards:
>
> **Board 1 — Systems & Integration Map:** Columns: System Name (text), Vendor (text), Category (dropdown: CRM/Donor, Finance, HR/Payroll, Program Management, Volunteer Management, Marketing/Email, Website/CMS, Analytics/BI, Communication, Document Management, Other), Data Owner (people), Primary Data Types (tags: Donor Records, Financial Transactions, Participant Records, Volunteer Records, Employee Records, Program Outcomes, Email Lists, Website Analytics, Grant Records), Record Count (numbers), Data Classification (dropdown: Public, Internal, Confidential, Restricted-PII, Restricted-PHI), Integrates With (connect to self), Integration Method (dropdown: monday.com Native, API, Zapier, Manual Export/Import, No Integration), Integration Status (status: Active, Intermittent, Broken, Not Integrated), Last Data Sync (date), Annual Cost (numbers, currency USD), Contract Renewal (date), Notes (long text). Dashboard: visual system map, integration health, total tech spend.
>
> **Board 2 — Data Quality Tracker:** Columns: Issue Title (text), System (connect to Systems Map), Issue Type (dropdown: Duplicate Records, Missing Data, Inconsistent Format, Stale Data, Integration Error, Broken Link, Access Issue), Severity (status: Critical, High, Medium, Low), Status (status: Identified, Assigned, In Progress, Resolved, Accepted Risk), Owner (people), Estimated Records Affected (numbers), Remediation Plan (long text), Target Date (date), Date Resolved (date). Automations: When Severity is Critical, notify IT Director. Monthly summary of open issues.
>
> **Board 3 — Data Request Queue:** Columns: Request Title (text), Requester (people), Department (dropdown), Request Type (dropdown: Report, Dashboard, Data Export, Analysis, Integration Request, Data Correction), Priority (status: Urgent, High, Medium, Low), Status (status: Submitted, Triaging, In Progress, Ready for Review, Delivered, Self-Service Available), Assigned To (people), Due Date (date), Data Sources Needed (tags), Deliverable (files), Notes (long text). Form: Data Request Form. Automations: When form submitted, notify IT team. When Status changes to Delivered, notify Requester."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Data Steward AI
**Agent Purpose:** Monitor data health across all organizational systems, identify quality issues, and help staff access the data they need without always going through IT.

**Triggers:**
- Daily integration health check (are all active integrations syncing?)
- When a data request is submitted
- Monthly data quality scan
- When a system renewal date approaches (60 days)
- When integration status changes to "Broken" or "Intermittent"

**Actions:**
- Monitor integration sync times and alert when data hasn't refreshed on schedule
- Triage data requests: direct self-service requests to existing dashboards, route complex requests to IT
- Generate monthly data quality scorecards by system: completeness, accuracy, freshness
- When duplicates are detected, generate merge recommendations with confidence scores
- Map data lineage for compliance questions ("where does donor SSN data flow?")
- Compile system inventory and spend analysis for annual technology planning

**Data Required:**
- Systems & Integration Map board
- Data Quality Tracker board
- Data Request Queue board
- API access to monitored systems for health checks

**Autonomy Level:** Human-in-the-Loop
Monitors and reports autonomously. Requires IT approval for: data corrections, integration changes, and system access modifications.

**Example Interaction:**
> Data Steward AI flags: "📊 Data Health Alert: (1) INTEGRATION DOWN: Salesforce → Mailchimp sync hasn't run in 72 hours. Last sync: Friday 11 PM. 847 new donor records in Salesforce haven't been pushed to email lists. The marketing team's Tuesday newsletter will miss these contacts unless resolved today. I've identified the issue: Zapier trigger failed due to Salesforce API rate limit. Recommend re-running the sync during off-hours tonight. (2) DATA QUALITY: Monthly scan found 1,247 duplicate donor records in Salesforce (up from 1,102 last month). Top merge candidates: 340 records with matching email addresses but different name spellings. I've prepared a merge recommendation file — want me to create tasks for the data stewards? (3) SELF-SERVICE WIN: 4 data requests this month were resolved by pointing requesters to existing dashboards instead of building custom reports. Updated the self-service directory."

---

### Use Case 7: IT Budget & Vendor Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Non-profit IT budgets are chronically underfunded — the median non-profit spends 1-3% of operating budget on technology (vs. 5-8% in the private sector). Every dollar must be justified. Yet IT spending is often poorly tracked: subscription charges hit multiple credit cards and cost centers, donated software has hidden costs (implementation, training, customization), and vendor contracts auto-renew without review. The IT director can't easily answer "what's our total technology spend?" because it's scattered across operating budget, grant budgets, donated services, and departmental purchases. When budget season arrives, there's no data to make the case for investment — just anecdotes and anxiety.

#### The Solution
monday.com Work Management creates an **IT Budget & Vendor Management** system. A **Technology Budget Board** consolidates all IT spending: subscription costs, hardware purchases, consulting fees, training, and internal staff costs — categorized by type, funding source, and department. A connected **Vendor Management Board** tracks every technology vendor: contract terms, SLAs, renewal dates, satisfaction scores, and relationship owners. Automations alert IT before renewals, flag budget variances, and compile total cost of ownership views. The **Dashboard** provides the CFO and ED a single view of technology investment with year-over-year trends.

#### The Outcome
- Complete visibility into total technology spend (often reveals 20-30% more than expected)
- $10-20K annual savings from identified unused subscriptions and better vendor negotiations
- Proactive contract management — no more surprise auto-renewals
- Data-driven IT budget proposals that speak the CFO's language
- Vendor consolidation roadmap with clear ROI projections

#### Discovery Questions
1. "What's your total annual technology spend — including subscriptions purchased by individual departments?"
2. "How do you currently track vendor contracts and renewal dates?"
3. "When was the last time you renegotiated a technology contract? Do you benchmark pricing?"
4. "Do you have a technology reserve fund for unexpected needs (equipment failure, security incident)?"
5. "How do you make the case for IT investment to leadership? What data do you use?"

#### Industry Context
Non-profit technology budgeting must account for unique factors: TechSoup donation eligibility cycles, grant-funded technology with restricted spending rules, donated services (volunteer IT consultants, pro bono implementations) that have real value but no budget line, and the expectation that IT costs should be minimal because "we're a non-profit." The NTEN Community Benchmark study provides sector-specific technology spending benchmarks. Total Cost of Ownership (TCO) analysis is critical — a "free" Salesforce implementation may cost $50-150K in consulting, customization, and training over 3 years. Technology reserves (2-5% of budget set aside for emergencies) are a best practice but rarely implemented.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an IT Budget & Vendor Management system with two connected boards:
>
> **Board 1 — IT Budget Tracker:** Columns: Line Item (text), Category (dropdown: Software Subscriptions, Hardware, Consulting/Professional Services, Training, Telecommunications, Cloud/Hosting, Security, Internal Staff, Maintenance/Support, Other), Vendor (connect to Vendor Board), Funding Source (dropdown: Operating Budget, Federal Grant, State Grant, Foundation Grant, Donated/TechSoup, Capital Budget), Department Charged (dropdown: IT, Programs, Development, Finance, HR, Marketing, Operations, Organization-wide), Annual Budget (numbers, currency USD), Actual Spend YTD (numbers, currency USD), Remaining (formula: Budget minus Actual), Variance % (formula), Fiscal Year (dropdown: FY2025, FY2026, FY2027), Payment Frequency (dropdown: Monthly, Quarterly, Annual, One-Time), Notes (long text). Groups: by Category. Dashboard: total IT spend by category, budget vs actual trending, spend by funding source, spend by department.
>
> **Board 2 — Vendor Management:** Columns: Vendor Name (text), Category (dropdown: same as budget categories), Primary Contact (text), Contact Email (email), Contact Phone (phone), Contract Start (date), Contract End (date), Auto-Renew (checkbox), Notice Period Days (numbers), Cancellation Deadline (date, formula: Contract End minus Notice Period), Annual Value (numbers, currency USD), Non-Profit Discount (dropdown: TechSoup, Vendor Non-Profit Program, Negotiated, None, Free Tier), SLA Terms (long text), Satisfaction (rating), Relationship Owner (people), Contract Document (files), Last Review Date (date), Alternatives Evaluated (text), Notes (long text). Automations: When Cancellation Deadline is 30 days away, notify Relationship Owner and IT Director. When Last Review Date is more than 12 months ago, create vendor review task."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** IT Budget Optimizer
**Agent Purpose:** Maximize technology ROI by tracking every dollar, identifying savings opportunities, and building data-driven budget proposals.

**Triggers:**
- Monthly budget reconciliation (1st of each month)
- When vendor cancellation deadlines approach (30 days)
- Annual budget planning season
- When a new technology purchase request is submitted
- Quarterly spending trend analysis

**Actions:**
- Generate monthly IT spending report: actuals vs. budget by category with variance analysis
- Alert on upcoming vendor renewals with utilization data and alternative options
- Compile annual IT budget proposal with historical spend data, ROI analysis for proposed investments, and benchmark comparisons (NTEN data)
- When a new purchase is requested, check for existing tools that might serve the same purpose and compare TCO
- Identify TechSoup donation eligibility for needed software
- Generate board-ready technology investment summaries showing strategic alignment

**Data Required:**
- IT Budget Tracker board
- Vendor Management board
- Software & Licenses board (for utilization data)
- NTEN benchmark data
- TechSoup product catalog

**Autonomy Level:** Human-in-the-Loop
Generates reports and recommendations autonomously. Requires IT Director approval for: vendor communications, budget proposals, and purchase decisions.

**Example Interaction:**
> IT Budget Optimizer prepares for budget season: "📊 FY2027 IT Budget Analysis: Total FY2026 spend: $127,400 (2.1% of operating budget — below NTEN median of 3.2%). Key findings: (1) SAVINGS: We're paying $4,800/year for Asana (12 licenses) and $3,600/year for Trello (team plan) — both project management tools with overlapping function. If we consolidate to monday.com, we can eliminate both and save $8,400/year while gaining superior automation and integration. (2) INVESTMENT NEEDED: Cybersecurity spend is $3,200 (2.5% of IT budget) — dangerously low. Cyber insurance carrier will require MFA and endpoint protection by renewal in June. Recommended: Microsoft Defender for Endpoint via TechSoup ($0 for E3 license) + Duo MFA ($2,400/year non-profit pricing). Net increase: $2,400 but avoids $15K cyber insurance premium increase. (3) HIDDEN COST: I found 7 departmental SaaS subscriptions totaling $6,900/year that aren't in the IT budget — including a $2,400 Canva Pro subscription the marketing team purchased. Recommend centralizing all software procurement through IT."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| TechSoup | Global non-profit that provides donated and discounted technology products to qualified organizations |
| NPSP (Nonprofit Success Pack) | Salesforce's free package for non-profits — includes 10 licenses and donor management features |
| NTEN | Nonprofit Technology Enterprise Network — the professional association for non-profit technology leaders |
| 2 CFR 200 | Federal Uniform Guidance — governs equipment tracking, data management, and technology purchases made with federal grant funds |
| Shadow IT | Technology tools adopted by staff without IT department knowledge or approval |
| BEC (Business Email Compromise) | Phishing attack impersonating an executive to trick staff into transferring funds or sharing sensitive data |
| SSO (Single Sign-On) | Authentication method allowing users to access multiple applications with one set of credentials |
| MFA (Multi-Factor Authentication) | Security requiring two or more verification factors to access a system |
| TCO (Total Cost of Ownership) | Full cost of a technology investment including licensing, implementation, training, maintenance, and staff time |
| NIST CSF | National Institute of Standards and Technology Cybersecurity Framework — most commonly adopted security framework for non-profits |
| CIS Controls | Center for Internet Security's prioritized set of security best practices |
| HIPAA | Health Insurance Portability and Accountability Act — applies to non-profits providing health services |
| FERPA | Family Educational Rights and Privacy Act — applies to non-profits providing educational services |
| GuideStar/Candid | Charity information service — organizations register for technology donation eligibility verification |
| Digital Transformation | Adoption of digital technology to fundamentally change how services are delivered and operations run |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| CTO / VP of Technology / IT Director | Technology strategy, infrastructure, security, vendor management | Decision-maker |
| COO / VP Operations | Oversees IT in orgs without dedicated tech leadership | Decision-maker |
| CFO / Finance Director | IT budget approval, vendor contracts, grant compliance for tech purchases | Decision-maker (budget) |
| Executive Director / CEO | Strategic technology vision, board communication about tech investments | Decision-maker (strategic) |
| Systems Administrator / IT Generalist | Day-to-day infrastructure, help desk, account management | User / Implementer |
| Data Manager / Database Administrator | CRM management, data quality, reporting, integrations | User / Influencer |
| Program Directors | Technology requirements for program delivery, data collection needs | Influencer |
| Development Director | CRM and fundraising technology requirements | Influencer |
| Board Technology Committee | Governance oversight of technology risk and investment | Decision-maker (governance) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Operations | Facilities systems, asset management, process automation | Shared platform for all operational technology needs |
| Finance | Accounting system integration, grant-funded equipment tracking | Unified budget and vendor management |
| Development/Fundraising | CRM management, donor data quality, online giving platforms | Integrated donor ecosystem with better data quality |
| Programs | Program databases, outcome tracking, participant data systems | Consolidated program management on monday.com |
| HR | Onboarding/offboarding, payroll system, training management | Automated people lifecycle management |
| Marketing/Communications | Website, email marketing, social media tools | Tech stack consolidation and integration |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Salesforce NPSP | Free CRM for non-profits, dominant in donor management | monday.com doesn't replace Salesforce but replaces the operational tools around it — project management, IT service desk, vendor tracking |
| Jira Service Management | IT help desk, used by larger non-profit IT teams | monday.com Service is dramatically simpler to set up and use, with better cross-org visibility |
| Zendesk (donated via TechSoup) | Help desk, often adopted but poorly configured | monday.com provides help desk + project management + asset tracking in one platform — Zendesk only does tickets |
| Asana / Trello | Project management, widely adopted for simplicity | monday.com offers superior automation, forms, dashboards, and the AI/Vibe roadmap |
| Google Workspace (free for non-profits) | Productivity suite, Sheets used for everything | monday.com replaces the spreadsheets while integrating with Google Workspace |
| Airtable | Flexible database, popular for asset and data tracking | monday.com provides better workflow automation, service desk, and enterprise scalability |
| Freshdesk (TechSoup) | IT ticketing, donated but limited non-profit customization | monday.com is more intuitive and connects IT work to the rest of the organization |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already get most of our software for free or donated" | "Free doesn't mean zero cost — your team spends hours integrating, maintaining, and working around tools that don't talk to each other. monday.com consolidates multiple tools into one platform, reducing the hidden cost of your 'free' stack. And monday.com has a non-profit program with significant discounts." |
| "Our IT team is too small to implement another system" | "That's exactly why monday.com works — it's designed to be set up by non-technical users in hours, not months. Your program managers can build their own boards. IT gets out of the tool-building business and into strategic work." |
| "We can't justify technology spend — donors want money going to programs" | "Overhead that makes programs more effective isn't waste — it's leverage. If monday.com saves your grants manager 10 hours a week, that's $15K in recovered capacity going directly to mission delivery. Smart technology investment improves your overhead ratio, not hurts it." |
| "We're locked into Salesforce for everything" | "Salesforce is great for donor data — but your IT team is managing help desk tickets in email, tracking projects in spreadsheets, and doing vendor management on sticky notes. monday.com handles the operational workflows Salesforce was never designed for, and integrates natively with it." |
| "Our staff won't adopt something new" | "Non-profit staff adopt tools that make their lives easier. monday.com Forms mean frontline workers just fill out a simple form — they never see the complexity behind it. And with AI Vibe, you can build a custom app in minutes during a demo that solves their specific pain." |
| "We need to focus on security, not new tools" | "monday.com actually improves your security posture: SOC 2 Type II certified, HIPAA-eligible, with granular permissions and audit logs. Replacing spreadsheets with tracked workflows for access management and incident response is itself a security upgrade." |

## Proof Points
*(To be populated with customer references)*
- [Non-profit IT departments using monday.com for service desk and operations]
- [Technology asset management and compliance examples]
- [IT project portfolio management in resource-constrained environments]
- [Cybersecurity posture improvement through structured workflows]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
