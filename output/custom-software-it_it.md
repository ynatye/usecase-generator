# Custom Software & IT Services × IT Playbook

## Overview

IT in custom software and IT services companies faces a unique irony: they're technology experts who serve external clients, yet internal IT is often neglected. The best engineers work on client projects, not internal systems. The focus is on billable work, not infrastructure. Yet internal IT is critical — it enables delivery, protects intellectual property, and increasingly differentiates the firm's capabilities.

The IT function typically spans infrastructure (networks, cloud, devices), development environment (dev tools, CI/CD, source control), security (data protection, access control, compliance), and internal systems (HRIS, finance, operations). At services firms, IT teams are small (3-20 people for a 500-person company) and compete with client work for attention.

What makes this combination unique: Services firms have sophisticated technical staff who have strong opinions about IT tools and often shadow IT their own solutions. Security is paramount — client data must be protected, and many clients audit vendor security. The consumerization of IT plus remote/hybrid work creates expectations for seamless experiences. AI is both an opportunity (internal efficiency) and a governance challenge (controlling how AI is used with client data).

---

## Value Driver Prioritization

1. **Consolidate Tech Stack with AI** — HIGHEST RELEVANCE
   - Services firms accumulate tools rapidly (client requirements, engineer preferences)
   - Each tool has cost, security, and support implications
   - AI can help rationalize and get value from fewer, smarter tools
   
2. **Scale Impact Without Overhead** — HIGH RELEVANCE
   - IT teams are understaffed relative to sophisticated user base
   - Self-service and automation essential
   - AI handles routine requests; IT focuses on strategic work

3. **Replace or Radically Augment Headcount** — MEDIUM RELEVANCE
   - Help desk and provisioning tasks are automatable
   - IT-savvy workforce reduces some support needs
   - AI as force multiplier for small IT teams

---

## Prioritized Use Cases

### 1. IT Service Management & Help Desk
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
IT support in services firms is tricky — users are tech-savvy and impatient, but issues are often complex (dev environment problems, client system access). Small IT teams get overwhelmed. Engineers bypass IT with workarounds that create security and support problems.

**Solution**: 
monday.com IT service desk with AI-powered triage and self-service. Handle routine requests automatically, route complex issues to the right specialist, and track everything. Build a knowledge base that reduces repeat requests.

**Vibe Prompt**:
```
Build an IT Service Desk app for IT services company IT teams.

Purpose: Manage IT requests from a tech-savvy workforce with AI-powered self-service and efficient escalation.

Key features:
- Request intake: Submitter, Project/client context, Issue type (Hardware/Software/Access/Dev Environment/Security/Other), Priority, Description
- AI triage: Auto-categorize, Search knowledge base for solutions, Suggest self-service resolutions
- Self-service options: Common issues (password reset, VPN, software install) with guided resolution
- Ticket board: Open tickets by status, Priority, Assigned technician, SLA status
- SLA tracking: Response time, Resolution time, By priority level
- Knowledge base: Solutions, How-tos, FAQs — searchable and AI-accessible
- Escalation: Route complex issues to appropriate specialist (infrastructure, security, dev environment)
- Dashboard: Open tickets, SLA compliance, Common issues, Self-service rate, Trends

Include automations:
- When ticket submitted, AI searches KB and suggests solutions
- If AI confidence high, offer self-service resolution
- When SLA at risk, escalate
- When issue resolved, prompt for knowledge base update
- Weekly IT metrics to leadership
```

**Outcome**: 
- Faster resolution for tech-savvy users
- Reduced ticket volume through self-service
- IT team focuses on complex issues
- Knowledge compounds over time

**Discovery Questions**:
- "How do engineers get IT help today? Is it efficient?"
- "What percentage of requests are the same issues over and over?"
- "How much of your IT team's time is spent on routine requests?"

**Industry-Specific Context**: 
Tech-savvy users expect fast, capable support. Common issues: dev environment setup, client system access, VPN/connectivity, software licensing. Engineers will shadow IT if official IT is too slow.

---

### 2. Development Environment & DevOps Support
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
Supporting development environments for diverse projects is challenging. Each client or project may have different requirements — languages, frameworks, cloud environments. Onboarding developers to new projects takes too long. Environment issues cause productivity loss.

**Solution**: 
monday.com dev environment management. Track environment requirements by project, manage onboarding/offboarding, maintain environment documentation, and track issues. Reduce time-to-productivity for developers on new projects.

**Vibe Prompt**:
```
Build a Development Environment Management app for IT services company IT teams.

Purpose: Manage development environment provisioning, documentation, and support across diverse projects.

Key features:
- Project environment registry: Project name, Tech stack, Cloud environment, Source control, CI/CD, Access requirements
- Onboarding checklist: By project, Standard steps to get developer productive
- Access provisioning: Track access grants (repos, cloud, client systems), Automate where possible
- Environment documentation: Setup guides, Troubleshooting, Architecture notes
- Issue tracking: Environment issues by project, Common problems
- Standardization opportunities: Identify patterns across projects, Recommend standard tooling
- Developer feedback: Capture friction points, Improvement suggestions
- Dashboard: Projects by tech stack, Access requests pending, Onboarding time trends, Common issues

Include automations:
- When developer assigned to project, generate onboarding checklist
- When access requested, route to appropriate approver
- When developer removed from project, generate offboarding checklist
- When environment issue reported, check for similar past issues
- Monthly dev environment health report
```

**Outcome**: 
- Faster developer onboarding to new projects
- Reduced environment-related productivity loss
- Better documentation and knowledge capture
- Visibility into tech stack diversity

**Discovery Questions**:
- "How long does it take to get a developer productive on a new project?"
- "How do you manage the diversity of environments across projects?"
- "How often do environment issues cause project delays?"

**Industry-Specific Context**: 
Each client project may have different requirements. "Polyglot" environments common (multiple languages, frameworks). Cloud environments vary (AWS, Azure, GCP, client-hosted). Client system access often requires VPN or special credentials.

---

### 3. Security & Access Management
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Services firms handle sensitive client data across many projects. Access control is complex — who has access to what client data? When projects end, is access revoked? Client security audits are stressful because access information is scattered.

**Solution**: 
monday.com access management for client data and systems. Track access by person and project, automate provisioning and deprovisioning, maintain audit trail, and ensure compliance with client security requirements.

**Vibe Prompt**:
```
Build a Security & Access Management app for IT services company IT and compliance teams.

Purpose: Manage access to client data and systems with proper controls and audit capabilities.

Key features:
- Client data registry: Client name, Data classification, Storage location, Security requirements, Access rules
- Access registry: Who has access to which client data/systems, Access level, Granted by, Grant date, Review date
- Project-based access: Link access to project assignment, Auto-flag for review when project ends
- Provisioning workflow: Request → Manager approval → Client approval (if required) → IT provisioning
- Deprovisioning triggers: Project end, Employee departure, Access expiration
- Access review: Periodic certification that access is still appropriate
- Audit trail: All access grants, revocations, and reviews logged
- Compliance dashboard: Security requirements by client, Access reviews due, Audit readiness
- Dashboard: Access by client, Reviews due, Recent changes, Compliance status

Include automations:
- When person assigned to project, initiate access request workflow
- When person removed from project, flag access for revocation
- When employee offboarded, generate complete access revocation checklist
- Quarterly access review: Managers certify team's access
- When client audit scheduled, generate audit-ready report
```

**Outcome**: 
- Clear access control for client data
- Automatic deprovisioning when projects end
- Audit-ready compliance documentation
- Reduced security risk

**Discovery Questions**:
- "When a project ends, how do you ensure all access is revoked?"
- "How would you answer a client who asks 'who has access to our data?'"
- "How do you handle client security audits?"

**Industry-Specific Context**: 
Client MSAs often include security requirements. SOC 2 Type II increasingly required. Access reviews mandated by some frameworks. "Need to know" principle for client data.

---

### 4. SaaS & Tool Management
**Relevance**: Medium-High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
Services firms accumulate tools rapidly — client requirements, engineer preferences, project experiments. Each tool has license cost, security implications, and support burden. Finance sees the cost; IT struggles to manage it; nobody knows what's actually being used.

**Solution**: 
monday.com SaaS management for visibility and governance. Track all tools, manage licenses, identify waste and overlap, and enforce procurement governance.

**Vibe Prompt**:
```
Build a SaaS & Tool Management app for IT services company IT and Finance teams.

Purpose: Manage the tool landscape with visibility into usage, cost, and compliance.

Key features:
- Tool inventory: Tool name, Category, Vendor, Owner, Annual cost, Renewal date, Security status
- License tracking: Total licenses, Assigned, Active users, Utilization %
- User assignments: Who has access to each tool, Department, Last login
- Cost allocation: Assign costs to projects, practices, overhead
- Procurement workflow: Request → Security review → Budget approval → Provisioning
- AI analysis: Identify overlap, Flag underutilization, Recommend consolidation
- Shadow IT detection: Flag tools discovered outside of governance
- Dashboard: Total spend, By category, Underutilized tools, Renewals upcoming, Consolidation opportunities

Include automations:
- When renewal in 30 days, review usage and notify owner
- When utilization drops below threshold, flag for review
- When new tool requested, route through approval
- When employee offboards, list tools requiring deprovisioning
- Monthly spend report to Finance and IT
```

**Outcome**: 
- Visibility into actual tool usage and cost
- Reduced waste through consolidation
- Governance without bureaucracy
- Better vendor management

**Discovery Questions**:
- "How many tools does your company use? Do you have an accurate count?"
- "What percentage of software licenses are actually being used?"
- "How do you decide whether to add a new tool?"

**Industry-Specific Context**: 
Dev tools proliferate (IDEs, testing, monitoring). Each practice may have specialized tools. Client projects sometimes require specific tools. Engineers have strong preferences.

---

### 5. AI Governance & Usage Policy
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
AI tools (ChatGPT, Copilot, etc.) are everywhere — but so is risk. Engineers use AI with client code in prompts. Client contracts may prohibit AI use. IP exposure is real. IT has no visibility or control, but outright bans are unenforceable and hurt productivity.

**Solution**: 
monday.com AI governance framework. Define approved tools and policies, track usage, enforce client-specific restrictions, and create a "front door" that enables safe AI adoption.

**Vibe Prompt**:
```
Build an AI Governance app for IT services company IT, legal, and delivery teams.

Purpose: Enable safe AI adoption while protecting client data and complying with contractual requirements.

Key features:
- Approved AI tools: Tool name, Approved use cases, Restrictions, Data policy (Never client data/Anonymized only/General guidance only)
- Client AI policies: Client name, AI permitted (Yes/No/With restrictions), Specific restrictions, Policy date
- Policy acknowledgment: Staff must acknowledge AI policy, Track completions
- AI request workflow: New tool request → Security → Legal → Approved or denied
- Usage guidelines: By use case (code assist, documentation, testing), Do's and don'ts
- Incident tracking: Potential violations, Investigation status
- Training tracking: AI training completions
- Dashboard: Approved tools, Policy compliance %, Clients with restrictions, Incidents

Include automations:
- When person assigned to client with AI restrictions, notify and require acknowledgment
- When new AI tool requested, route through approval
- Quarterly policy acknowledgment refresh
- When incident logged, notify Security and Legal
- Monthly AI usage report to leadership
```

**Outcome**: 
- Controlled AI adoption without productivity loss
- Protected client data and relationships
- Clear policy that's actually enforceable
- Visibility into AI usage across the firm

**Discovery Questions**:
- "Do you know how your engineers are using AI tools? With client code?"
- "Do any of your clients prohibit AI in their contracts?"
- "What's your current AI policy? How is it enforced?"

**Industry-Specific Context**: 
Client code in AI prompts is major risk. Some clients (financial, government) have strict prohibitions. IP ownership questions for AI-generated code. "Copilot" and similar tools are pervasive.

---

### 6. Infrastructure & Cloud Management
**Relevance**: Medium  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Services firms use cloud infrastructure for internal systems, development, and sometimes client projects. Costs grow, resources are underutilized, and security configurations vary. Nobody has a complete picture of what's running where.

**Solution**: 
monday.com cloud visibility connecting to cloud management. Track environments, costs, and security posture. Enable right-sizing and cost optimization.

**Vibe Prompt**:
```
Build a Cloud & Infrastructure Management app for IT services company IT teams.

Purpose: Manage cloud resources across environments with visibility into cost, security, and utilization.

Key features:
- Environment registry: Environment name, Cloud provider, Purpose (Internal/Development/Client), Owner, Cost center
- Resource tracking: VMs, containers, databases, storage — by environment
- Cost monitoring: Monthly cost by environment, By project, Trends
- Security posture: Configuration compliance, Vulnerabilities, Findings
- Optimization recommendations: Underutilized resources, Right-sizing opportunities
- Access control: Who can access which environments, Tracking
- Lifecycle management: Dev environments spun up/down, Expiration tracking
- Dashboard: Total cloud spend, By environment, Cost trends, Security findings, Optimization opportunities

Include automations:
- When cost exceeds threshold, alert owner
- When security finding detected, notify IT Security
- When dev environment inactive, prompt for shutdown or extension
- Monthly cloud cost report
- When optimization identified, create recommendation
```

**Outcome**: 
- Visibility into cloud usage and cost
- Cost optimization opportunities identified
- Improved security posture
- Better cloud governance

**Discovery Questions**:
- "Do you know how much you're spending on cloud? By project?"
- "How often do dev environments get left running after projects end?"
- "What's your cloud security posture? Do you have visibility?"

**Industry-Specific Context**: 
Multi-cloud common (AWS, Azure, GCP depending on client/project). Development environments proliferate. "Cloud waste" from forgotten resources is common. Client environments may need separation.

---

## Industry Terminology Glossary

**Shadow IT** — Technology used without IT department approval; common in services firms with tech-savvy workforce.

**DevOps** — Practices combining development and operations; includes CI/CD, infrastructure as code, etc.

**CI/CD** — Continuous Integration / Continuous Deployment; automated build and deploy pipelines.

**SOC 2** — Security certification demonstrating controls over security, availability, processing integrity, confidentiality, privacy.

**MSA (Master Service Agreement)** — Overarching contract with client; often includes security requirements.

**VPN** — Virtual Private Network; used for secure access to client systems.

**SSO (Single Sign-On)** — One login for multiple applications; security and convenience enabler.

**MDM (Mobile Device Management)** — Managing and securing mobile devices.

**Copilot** — AI coding assistant (GitHub Copilot and similar); governance challenge.

**Polyglot** — Using multiple programming languages/frameworks; common in diverse services environment.

---

## Typical Stakeholder Roles

**Primary Buyer: IT Director / VP of IT**
- Title: IT Director, VP Technology, Head of IT
- Concerns: Security, efficiency, supporting a demanding user base, cost management
- Decision driver: "Can I support more with less while keeping us secure?"

**Technical Evaluator: IT Manager / Systems Administrator**
- Title: IT Manager, DevOps Lead, Security Lead
- Concerns: Implementation complexity, integration, manageability
- Decision driver: "Does this fit our environment and actually solve problems?"

**Executive Sponsor: COO / CFO**
- Title: COO, CFO (often oversees IT at smaller firms)
- Concerns: Risk management, cost control, operational efficiency
- Decision driver: "Does this reduce our risk and control our costs?"

**Delivery Stakeholder: Delivery Leadership**
- Title: VP Delivery, Practice Leader
- Concerns: Developer productivity, project delivery, client security requirements
- Decision driver: "Does this help us deliver for clients?"

**End Users:**
- Developers, Consultants, Project managers, All staff

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Operations** | Project environments, Resource data | Operations integration |
| **HR** | Onboarding/offboarding, People data | HR integration |
| **Finance** | SaaS costs, Cloud costs | Financial management |
| **Delivery/Practices** | Dev environments, Security requirements | Practice management |
| **Legal** | Security compliance, AI policy | Compliance management |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| IT Service Desk | Jira Service Management, Freshservice | Replace |
| SaaS Management | Zylo, Torii | Replace |
| Access Management | Okta, Azure AD | Integrate |
| Cloud Management | CloudHealth, native tools | Augment with visibility |
| Documentation | Confluence, Notion | Integrate |

**Positioning:**
- **vs. Jira Service Management**: "Jira SM is built for IT departments in tech companies, but it doesn't connect to your operations, projects, or people. monday.com gives you service desk plus visibility into everything else that matters."
- **vs. Point Solutions**: "You have different tools for tickets, access management, SaaS tracking, and cloud costs. None of them connect. What if you could see the whole picture in one place?"
- **vs. Nothing/Manual**: "Your access control is spreadsheets, your tool inventory is guesswork, and your AI governance is wishful thinking. For a company that does IT services, that's a risk."

---

## Common Objections

**Objection**: "Our engineers will hate using another tool."

**Response**: "Engineers hate bad tools and bureaucracy. They like tools that work. monday.com is designed to be useful, not annoying. Self-service that actually works, fast answers to their questions, and AI that helps instead of getting in the way. The test isn't whether it's another tool — it's whether it makes their lives easier."

---

**Objection**: "We're an IT services company. We can build our own tools."

**Response**: "You could. But should you? Every hour your engineers spend building internal tools is an hour not billed to clients. Your clients pay for custom development; internal IT shouldn't be a custom project. Build for clients; buy for yourself."

---

**Objection**: "We're too small for formal IT governance."

**Response**: "Formal governance, maybe not. But you still need to know who has access to client data, what tools you're paying for, and how AI is being used. 'Small' doesn't mean 'no risk.' A lightweight system now prevents expensive problems later."

---

*Playbook Version: 1.0*  
*Industry: Custom Software & IT Services*  
*Department: IT*  
*Last Updated: 2026-02-11*
