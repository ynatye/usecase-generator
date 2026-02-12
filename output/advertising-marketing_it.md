# Advertising & Marketing × IT Playbook

## Overview

IT in advertising and marketing agencies exists in a unique tension: supporting a creative, fast-moving workforce that resists standardization while maintaining security, reliability, and increasingly complex technology stacks. Unlike IT in traditional enterprises, agency IT must enable rather than constrain — because the product is creativity, and friction kills ideas.

The IT function in agencies typically spans infrastructure (networks, hardware, cloud services), applications (creative tools, business systems, DAM), security (client data protection, IP security), and emerging tech (AI tools, automation, martech). At mid-to-large agencies, IT teams are often lean (5-20 people for a 500-person agency) and heavily reliant on managed services and contractors.

What makes this combination unique: Agency IT manages a constantly shifting tool landscape — new creative software, client-mandated platforms, emerging AI tools — while protecting highly sensitive client data (unreleased campaigns, product launches, M&A comms). The workforce expects consumer-grade experiences but generates enterprise-grade security requirements. AI presents both opportunity (efficiency gains) and risk (IP exposure, shadow AI usage).

---

## Value Driver Prioritization

1. **Consolidate Tech Stack with AI** — HIGHEST RELEVANCE
   - Agency tech stacks are notoriously fragmented (20-50+ tools is common)
   - Each tool has its own license cost, security profile, and support burden
   - AI can replace or augment multiple point solutions with fewer, smarter tools
   
2. **Scale Impact Without Overhead** — HIGH RELEVANCE
   - IT teams are chronically understaffed relative to the workforce they support
   - Ticket volumes grow with agency size; headcount doesn't keep pace
   - AI automation can handle routine requests and first-line support

3. **Replace or Radically Augment Headcount** — MEDIUM RELEVANCE
   - Some IT functions (help desk, provisioning, access management) are highly automatable
   - Resistance may exist to fully replacing roles, but augmentation is welcomed
   - AI enables 1 IT person to do the work of 2-3

---

## Prioritized Use Cases

### 1. IT Service Desk & Request Management
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
IT help desks in agencies are overwhelmed. Creative professionals expect instant support (a crashed workstation can delay a client deadline), but most issues are repetitive: password resets, software access requests, "how do I do X?" questions. Senior IT staff spend hours on tier-1 issues instead of strategic work.

**Solution**: 
monday.com IT service desk with AI-powered triage and self-service. Sidekick handles common questions directly, suggests solutions from knowledge base, and auto-routes complex issues to the right specialist. Track SLAs, visualize ticket trends, and identify systemic issues before they become crises.

**Vibe Prompt**:
```
Build an IT Service Desk app for advertising agency IT teams.

Purpose: Manage IT requests and incidents with AI-powered triage, self-service, and SLA tracking.

Key features:
- Request intake form: Submitter name, Department, Issue type (Access Request/Hardware Issue/Software Issue/How-To Question/Security Incident/Other), Urgency, Description, Screenshots
- AI triage: Auto-categorize, suggest solutions from knowledge base, route to appropriate specialist
- Self-service resolution: For common issues (password reset, VPN setup, software install), provide step-by-step guides or automated actions
- Ticket board: Open tickets by status (New/In Progress/Waiting on User/Resolved), assigned tech, SLA status
- SLA tracking: Time to first response, Time to resolution, by priority level
- Knowledge base integration: Link solutions to tickets, suggest articles to users
- Hardware inventory link: Show user's devices when ticket opened
- Dashboard: Open tickets by type/priority, SLA compliance %, Common issues this week, Ticket volume trends, Top requesters

Include automations:
- On submit, AI suggests solution from knowledge base; if confidence >80%, offer self-service resolution
- Auto-assign based on issue type (hardware → hardware tech, software → applications team)
- When ticket opened >24h with no response, escalate and notify IT Manager
- When resolved, send satisfaction survey
- Weekly report to IT Director: Volume, SLA compliance, Top issue categories
```

**Outcome**: 
- Reduce ticket volume by 30-40% through AI self-service
- Improve average resolution time by 50%
- Free senior IT staff from tier-1 issues
- Better visibility into systemic problems

**Discovery Questions**:
- "How many IT tickets do you handle per month? What percentage are the same issues over and over?"
- "What's your current average resolution time? What should it be?"
- "How much time do your senior IT people spend on basic help desk work?"

**Industry-Specific Context**: 
Creative professionals are notoriously impatient with IT. Downtime directly impacts billable work. Common agency-specific issues: Adobe CC license problems, render farm access, file storage permissions, VPN for remote shoots.

---

### 2. Software License & SaaS Management
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
Agencies are drowning in SaaS. Marketing teams bought one tool, creative bought another, accounts bought a third — all doing overlapping things. Finance sees costs but can't see value. IT sees security risks but can't enforce governance. Licenses are unused, duplicate, or shadow-purchased.

**Solution**: 
monday.com SaaS management with full visibility into what tools exist, who uses them, what they cost, and whether they're compliant. AI identifies overlap, flags underutilization, and recommends consolidation. Integration with SSO and expense systems for automatic discovery.

**Vibe Prompt**:
```
Build a SaaS Management app for advertising agency IT and Finance teams.

Purpose: Track all software/SaaS tools, manage licenses, identify waste and overlap, and enforce governance.

Key features:
- Software inventory: Tool name, Category (Creative/Productivity/PM/Analytics/Finance/Other), Vendor, Contract owner, Annual cost, Billing cycle, Renewal date, SSO integrated (Y/N), Security review status
- License tracking: Total licenses, Assigned licenses, Active users (last 30 days), Utilization %
- User assignments: Who has access to each tool, Department, Last login date
- Cost allocation: Assign tool costs to departments/clients
- AI analysis: Identify overlap (multiple tools doing similar things), Flag underutilized licenses, Recommend consolidation
- Procurement workflow: Request new tool → Security review → Budget approval → Provisioning
- Shadow IT detection: Flag tools discovered outside of IT governance
- Dashboard: Total SaaS spend, Spend by category, Underutilized tools (>30% unused licenses), Renewals next 90 days, Consolidation opportunities

Include automations:
- When renewal in 30 days, notify contract owner and IT Manager to review
- When utilization drops below 50%, flag for review
- When new tool requested, route through security and budget approval
- When user leaves agency, list all tools requiring deprovisioning
- Monthly spend report to Finance and IT leadership
```

**Outcome**: 
- Reduce SaaS spend by 15-25% through utilization visibility
- Eliminate shadow IT risk
- Never miss a renewal (avoid auto-renewal surprises)
- Enable data-driven tool consolidation decisions

**Discovery Questions**:
- "How many SaaS tools does the agency use? Do you know the exact number?"
- "What percentage of your software licenses are actually being used?"
- "When's the last time you discovered a tool someone was paying for that IT didn't know about?"

**Industry-Specific Context**: 
Agencies typically use: Adobe CC, Figma, Sketch, After Effects (creative); Slack, Teams, Google Workspace (collaboration); various project management; specialized tools for media, analytics, social. "Shadow IT" is rampant because creatives want tools NOW.

---

### 3. Client Data Security & Access Management
**Relevance**: High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Agencies handle highly sensitive client data — unreleased product images, confidential strategies, embargoed announcements. Access control is often ad-hoc: "Add them to the Dropbox folder." When someone leaves, revoking access is manual and error-prone. One leak can end a client relationship and create legal liability.

**Solution**: 
monday.com access management for client data. Track who has access to what client materials, automate provisioning based on project assignment, automate deprovisioning when projects end or people leave. Maintain audit trail for compliance. AI flags unusual access patterns.

**Vibe Prompt**:
```
Build a Client Data Access Management app for advertising agency IT and compliance teams.

Purpose: Control and audit access to sensitive client materials, ensuring security and compliance.

Key features:
- Client data inventory: Client name, Data classification (Public/Internal/Confidential/Restricted), Storage location (Google Drive/Dropbox/S3/DAM), Sensitivity notes
- Access registry: Who has access to which client data, Access level (View/Edit/Admin), Granted by, Granted date, Expires (if applicable)
- Project-based access: Link access to project assignments; when project ends, flag for review
- Access request workflow: Request → Manager approval → IT provisioning → Granted with audit log
- Deprovisioning triggers: When person leaves project, leaves agency, or on specific date
- Audit log: All access grants, revocations, and data access events
- AI anomaly detection: Flag unusual access patterns (bulk downloads, access outside normal hours, access by off-boarded users)
- Compliance dashboard: Access reviews due, Overdue reviews, Recent access changes, Anomaly alerts

Include automations:
- When person assigned to project, send access request for standard client data locations
- When person removed from project, flag all client data access for review
- When employee offboarded, generate complete access revocation checklist
- Quarterly access review: Notify managers to certify their team's access is appropriate
- Alert Security team when anomaly detected
```

**Outcome**: 
- Eliminate orphaned access (no more ex-employees with data access)
- Pass client security audits with confidence
- Respond to "who has access to X?" in seconds, not hours
- Prevent data leaks through early anomaly detection

**Discovery Questions**:
- "When someone leaves a project or the agency, how do you revoke their access to client data?"
- "Have you ever been audited by a client on data security? How did it go?"
- "How quickly could you tell me everyone who has access to your biggest client's confidential materials?"

**Industry-Specific Context**: 
Many clients require MSAs with specific security requirements. Embargoed data (product launches, M&A, earnings) requires strict "need to know" access. NDA tracking is related but separate.

---

### 4. Hardware Asset Management
**Relevance**: Medium-High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Creative professionals need powerful hardware — MacBook Pros, high-end displays, render workstations. IT manages hundreds of devices across offices, home workers, and production sets. Tracking what exists, where it is, when it's due for refresh, and whether it's secure is a full-time job (or more).

**Solution**: 
monday.com hardware inventory with lifecycle tracking. Know what you have, where it is, who's using it, and when it needs attention. AI predicts hardware failures based on age and support tickets. Automate refresh cycles and procurement.

**Vibe Prompt**:
```
Build a Hardware Asset Management app for advertising agency IT teams.

Purpose: Track all hardware assets through their lifecycle, from procurement to disposal.

Key features:
- Asset inventory: Asset tag, Type (Laptop/Desktop/Monitor/Tablet/Phone/Peripheral), Make/Model, Serial number, Assigned to, Location, Purchase date, Warranty expiration, Status (Active/Storage/Repair/Disposed)
- User assignment: Who has what devices, Assignment history, Acknowledgment signed
- Lifecycle tracking: Expected lifespan (e.g., 3 years for laptops), Refresh eligibility date, Depreciation schedule
- Procurement workflow: Request → Budget approval → Order → Receive → Configure → Deploy
- Maintenance log: Repairs, upgrades, issues per device
- AI predictions: Flag devices likely to fail based on age, model history, and ticket patterns
- Offboarding checklist: Devices to collect when employee leaves
- Dashboard: Total assets by type, Assets due for refresh, Warranty expirations, Assets in repair, Missing/unaccounted devices

Include automations:
- When device purchased, create asset record from PO data
- When assigned to user, send acknowledgment form and update inventory
- 90 days before refresh date, notify IT Manager and budget owner
- When ticket opened for device, link to asset record and update health score
- When employee offboarding, generate device return checklist
```

**Outcome**: 
- Know exactly what hardware you have and where it is
- Reduce emergency hardware purchases through planned refresh cycles
- Improve support efficiency by linking tickets to asset history
- Never lose track of a $3,000 laptop again

**Discovery Questions**:
- "How many hardware devices does your IT team manage? Do you have an accurate count?"
- "How do you know when a device needs to be replaced? Is it reactive or proactive?"
- "When someone leaves, how do you ensure all devices are returned?"

**Industry-Specific Context**: 
Agencies typically Mac-heavy. Creative workstations are expensive ($5K-$15K). Remote and hybrid work complicates device management. Production equipment (cameras, drives) may or may not be IT-managed.

---

### 5. AI Governance & Shadow AI Prevention
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
AI tools are proliferating — ChatGPT, Midjourney, DALL-E, countless others. Creative teams are using them (often with client data in prompts), but IT has no visibility or control. Client contracts may prohibit AI use. Security risks are real. Yet outright banning AI means losing competitive advantage.

**Solution**: 
monday.com AI governance framework: approved tools, usage policies, client-specific restrictions, and tracking. Enable safe AI adoption with guardrails. AI-powered monitoring flags potential policy violations. Create a "front door" so people use sanctioned tools instead of shadow AI.

**Vibe Prompt**:
```
Build an AI Governance app for advertising agency IT, legal, and operations teams.

Purpose: Enable safe AI adoption while preventing shadow AI usage and policy violations.

Key features:
- Approved AI tools registry: Tool name, Approved use cases, Restrictions, Data allowed (Never client data/Anonymized only/General guidance only), Training provided (Y/N), SSO integrated
- Client AI policies: Client name, AI permitted (Yes/No/With restrictions), Specific restrictions (e.g., no generative images), Policy effective date
- Usage logging: Track who uses approved tools, when, for which projects (opt-in/integrated where possible)
- AI request workflow: Request to use new AI tool → Legal review → Security review → Approved or denied with rationale
- Policy acknowledgment: Staff must acknowledge AI policy; track completions
- Incident log: Log potential violations for investigation
- Training tracking: Who has completed AI training
- Dashboard: Approved tools, Requests pending, Policy compliance %, Clients with AI restrictions, Recent incidents

Include automations:
- When new AI tool requested, route to Legal and Security for parallel review
- When client AI policy updated, notify all staff assigned to that client
- Quarterly AI policy refresh: Re-send acknowledgment to all staff
- When incident logged, notify IT Security and Legal
- Monthly AI usage report to leadership
```

**Outcome**: 
- Enable AI adoption without risking client relationships or data
- Full visibility into AI tool usage across the agency
- Defend against shadow AI through "front door" governance
- Clear policy framework that's enforceable

**Discovery Questions**:
- "Do you know what AI tools your staff are using right now? With client data?"
- "Do any of your clients have contractual restrictions on AI use?"
- "What's your current AI policy? How is it enforced?"

**Industry-Specific Context**: 
Client IP in AI prompts is a major risk. Some clients (pharma, financial) have strict AI prohibitions. Copyright implications of AI-generated content are evolving. "Shadow AI" = unauthorized use of AI tools.

---

### 6. Vendor & Technology Onboarding
**Relevance**: Medium  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Every new vendor, tool, or platform requires IT involvement: security review, contract review, integration assessment, provisioning. With agencies constantly adopting new tools and working with new vendors, the backlog is endless. Projects stall waiting for IT approvals.

**Solution**: 
monday.com vendor/tech onboarding workflow that standardizes the process, automates routing, and tracks everything in one place. AI pre-screens for common security issues. Clear SLAs so requesters know what to expect.

**Vibe Prompt**:
```
Build a Vendor & Technology Onboarding app for advertising agency IT and procurement.

Purpose: Streamline the process of evaluating and onboarding new vendors and technology tools.

Key features:
- Request intake: Requester, Vendor/tool name, Purpose, Data involved (None/Internal only/Client data), Urgency, Budget (if known)
- Security review checklist: SOC 2 report, Data encryption, Access controls, GDPR compliance, Penetration test results
- AI pre-screen: Based on request details, flag likely issues and suggest security questions
- Review workflow: Request → IT Security → Legal (if contracts) → Budget → Approval
- Contract tracking: Link vendor agreements, expiration dates, renewal terms
- Integration assessment: APIs available, SSO compatible, Integration effort estimate
- Status tracking with SLAs: 5 business days for standard review, 2 days for expedited
- Dashboard: Requests in progress, Requests by status, Average review time, Blocked requests, Recently approved

Include automations:
- On submit, AI pre-screens and auto-assigns to appropriate reviewer
- When security review complete, auto-advance to next stage
- If SLA at risk, escalate to IT Manager
- When approved, trigger provisioning workflow
- Weekly status update to all pending requesters
```

**Outcome**: 
- Cut vendor onboarding time by 40%
- Clear expectations for requesters (no more black hole)
- Consistent security review standards
- Audit trail for compliance

**Discovery Questions**:
- "How long does it typically take to get a new tool approved and provisioned?"
- "Do you have a consistent security review process, or does it vary by who's involved?"
- "How often do projects stall waiting for IT approvals?"

**Industry-Specific Context**: 
Agencies evaluate new tools constantly — client requirements, competitive pressure, creative desires. "Security questionnaire" often required by enterprise clients. SOC 2 Type II is the common compliance standard for SaaS vendors.

---

## Industry Terminology Glossary

**Shadow IT** — Technology or software used without IT department knowledge or approval. Rampant in agencies due to creative autonomy culture.

**Creative Cloud** — Adobe's suite of creative applications (Photoshop, Illustrator, Premiere, After Effects, etc.). The foundation of most agency creative work.

**DAM (Digital Asset Management)** — System for storing, organizing, and retrieving creative assets. Examples: Bynder, Brandfolder, Canto.

**SSO (Single Sign-On)** — Authentication system allowing one login for multiple applications. Security and convenience enabler.

**SOC 2** — Security certification for SaaS vendors demonstrating controls over security, availability, processing integrity, confidentiality, and privacy.

**Render Farm** — Cluster of computers used for rendering video, 3D, or visual effects. Requires significant IT management.

**Martech** — Marketing technology: tools for automation, analytics, CRM, etc.

**VPN** — Virtual Private Network for secure remote access. Essential for hybrid work.

**MDM (Mobile Device Management)** — Software to manage and secure mobile devices (phones, tablets).

**Endpoint** — Any device connecting to the agency network (laptops, phones, tablets).

---

## Typical Stakeholder Roles

**Primary Buyer: IT Director / Head of IT**
- Title: IT Director, Director of Technology, Head of IT, VP Technology
- Concerns: Security, efficiency, cost management, supporting the business without being a bottleneck
- Decision driver: "Can I do more with my limited team while keeping us secure?"

**Technical Evaluator: IT Manager / System Administrator**
- Title: IT Manager, Systems Administrator, Technical Lead
- Concerns: Implementation complexity, integration with existing systems, daily manageability
- Decision driver: "Will this actually make my job easier or add another system to manage?"

**Executive Sponsor: COO or CFO**
- Title: COO, CFO (often oversees IT at mid-size agencies)
- Concerns: Cost control, risk management, operational efficiency
- Decision driver: "Does this reduce our risk and pay for itself?"

**Security Stakeholder: InfoSec / Compliance (if exists)**
- Title: Security Manager, Compliance Officer (often IT Director wears this hat)
- Concerns: Client data protection, compliance, audit readiness
- Decision driver: "Does this improve our security posture?"

**End Users:**
- All agency staff (for service desk), Hiring managers (for onboarding), Department heads (for software requests)

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Operations** | Tooling, process systems | Unified operational platform |
| **Creative** | Creative tools, DAM, hardware | Creative workflow management |
| **Finance** | Software costs, budgeting | Financial management integration |
| **HR** | Onboarding, offboarding, training | HRIS integration, HR workflows |
| **Legal** | Contracts, compliance, data policies | Contract management, policy tracking |
| **All Departments** | Service desk, access requests | Self-service and automation |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| IT Service Desk | Jira Service Management, Freshservice, Zendesk | Full replacement |
| Asset Management | Snipe-IT, Jamf (Mac), InTune | Replace or integrate |
| SaaS Management | Zylo, Torii, Blissfully | Full replacement |
| Access Management | Okta, Azure AD | Integrate (not replace) |
| Security Tools | Various | Integrate for visibility |

**Positioning:**
- **vs. Jira Service Management**: "Jira is built for IT departments in tech companies. We're built for agencies where IT serves creative people who have zero patience for enterprise software."
- **vs. Spreadsheet Asset Tracking**: "You've outgrown Excel. When you have 300 devices across 100 people in 3 offices plus work-from-home, you need a real system."
- **vs. Enterprise IT Tools**: "You're not an enterprise, and you don't have enterprise IT budgets or staff. You need powerful without complex."

---

## Common Objections

**Objection**: "We already use Jira for IT tickets."

**Response**: "Jira's great for engineering teams but overkill for agency IT, and it doesn't connect to the rest of the agency's work. What if your IT tickets, projects, resources, and assets were all in one platform? No more copying data between systems, no more 'IT uses that tool and everyone else uses this one.'"

---

**Objection**: "We're too small for this. We manage IT in spreadsheets and it's fine."

**Response**: "It's fine until it isn't — until you fail a client security audit, or you discover shadow AI everywhere, or a departing employee walks out with client data access. A simple system now prevents expensive problems later. And with AI handling routine requests, your small IT team punches above its weight."

---

**Objection**: "Our IT team is too busy to implement another tool."

**Response**: "Exactly. Your IT team is too busy because they don't have tools working for them. monday.com is designed for quick implementation — weeks, not months — and the AI capabilities mean you start saving time immediately on routine requests. What's the cost of staying too busy?"

---

*Playbook Version: 1.0*  
*Industry: Advertising & Marketing*  
*Department: IT*  
*Last Updated: 2026-02-11*
