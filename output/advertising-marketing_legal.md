# Advertising & Marketing × Legal Playbook

## Overview

Legal departments in advertising and marketing companies operate as the guardrails of an industry built on creative risk-taking. Agency legal teams (typically 2–8 attorneys at mid-market shops, 20–50+ at holding company level) manage an extraordinary breadth of legal work: client contracts and master service agreements (MSAs), talent agreements (actors, models, voiceover, influencers), music licensing, intellectual property clearance, advertising regulatory compliance (FTC, NAD, ASA), data privacy, employment law for a heavily freelance workforce, and increasingly, AI-related legal issues around generative content and synthetic media.

The pace is relentless. A single campaign launch might require clearance of 30+ assets across trademark, copyright, talent rights, music rights, regulatory claims, and platform-specific ad policies — all within days, not weeks. Legal bottlenecks are the number one cause of campaign launch delays. Creative teams resent legal review as a "creativity killer," while legal teams are drowning in volume with no systematic way to prioritize. The shift to always-on social media content has multiplied the volume of assets requiring legal review by 10x compared to a decade ago, while legal team sizes haven't grown proportionally.

Regulatory complexity is intensifying. The FTC's updated endorsement guidelines (2023) expanded disclosure requirements for influencer marketing and AI-generated content. GDPR, CCPA, and global privacy laws affect how agencies collect and use consumer data for targeting. Advertising self-regulatory bodies (NAD in the US, ASA in the UK) are more active than ever. And the rise of generative AI in creative production has opened entirely new legal frontiers: who owns AI-generated content? Can AI-generated images of people create likeness rights issues? How do you disclose AI-generated advertising? Most agency legal teams are building the plane while flying it.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Legal volume has grown 10x (social, influencer, AI) while team sizes are flat — need to process more with the same team |
| 2 | Replace or Radically Augment Headcount | Medium-High | AI can handle routine clearance checks, contract generation, and compliance screening — freeing attorneys for complex judgment calls |
| 3 | Consolidate Tech Stack with AI | Medium | Legal work tracked across email, shared drives, DocuSign, and spreadsheets — no unified matter management |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Creative Asset Legal Clearance & Approval Workflow

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every piece of creative that goes out the door — TV spots, digital ads, social posts, OOH, influencer content, email campaigns — needs legal clearance. At a typical mid-size agency, legal reviews 200–500+ assets per month. The current process: creative teams email assets to legal (or drop them in a shared folder), legal reviews when they can, sends feedback via email or redline, creative revises, legal re-reviews. There's no queue, no priority system, no SLA tracking, and no audit trail. Urgent requests ("we need clearance by 3 PM for a TikTok post") compete with complex reviews ("this TV script has 14 product claims that need substantiation"). Creative teams don't know where their asset is in the review queue, so they send follow-up emails — which consume more legal time. When a campaign launches with a legal issue, there's no way to trace what was reviewed, by whom, and what was approved.

#### The Solution
monday.com Work Management as a centralized legal clearance system. Every asset requiring legal review enters a structured queue with type classification, priority level, deadline, and assigned reviewer. Creative teams submit via forms with required information (asset type, claims made, talent used, music used, target markets). Automations route submissions based on type and urgency, track SLAs, and notify creative teams of status changes. A complete audit trail captures every review decision.

#### The Outcome
- Average clearance turnaround reduced from 5 days to 2 days
- Zero "lost" review requests — every submission tracked and visible
- 95% SLA compliance (vs. unmeasured currently)
- Complete audit trail for regulatory defense — know exactly what was reviewed and approved
- Creative team satisfaction with legal increases 40%+ (visibility eliminates frustration)

#### Discovery Questions
1. "How many creative assets does your legal team review per month, and what's the average turnaround time from submission to clearance?"
2. "When a creative team needs to know the status of their legal review, what do they do — and how much legal team time does that consume?"
3. "If the FTC or NAD challenged one of your ads, could you produce the legal review trail — who reviewed it, what was flagged, what was approved?"
4. "How do you prioritize legal reviews — does a Super Bowl spot get the same queue position as a social media post?"
5. "What percentage of campaign launch delays are caused by legal clearance bottlenecks?"

#### Industry Context
Advertising legal clearance covers multiple dimensions: (1) Substantiation — can claims be supported? (2) Trademark — does copy or visual infringe third-party marks? (3) Talent rights — are usage rights cleared for all media, markets, and duration? (4) Music — are sync licenses in place? (5) Regulatory — does the ad comply with FTC, NAD, FDA (pharma), TTB (alcohol), FCC (broadcast)? (6) Platform policies — does it meet Google, Meta, TikTok ad policies? Each dimension may require different expertise. Network clearance (for TV) adds another layer — ABC, CBS, NBC, and Fox each have their own standards and practices departments that review ads independently.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Legal Clearance & Approval workspace for an advertising agency. Include:
> 1. **Clearance Queue** — columns: Asset Name (text), Submission ID (auto-number with prefix: CLR-), Client (text), Campaign (text), Asset Type (dropdown: TV/Video, Digital Display, Social Post, Influencer Content, OOH, Print, Radio/Audio, Email, Website, Packaging), Submitted By (people), Submit Date (date), Deadline (date), Days Until Deadline (formula: deadline - today), Priority (status: Urgent-24hr, High-48hr, Standard-5day, Low), Assigned Reviewer (people), Review Status (status: Submitted, In Review, Revisions Requested, Revised-Resubmitted, Approved, Approved with Conditions, Rejected), Clearance Areas (dropdown multi-select: Claims/Substantiation, Trademark, Talent Rights, Music Rights, Regulatory, Platform Policy, Privacy/Data), SLA Met (checkbox), Approval Notes (long text)
> 2. **Review Checklist** (subitems of Clearance Queue) — columns: Check Area (text), Status (status: Clear, Issue Found, N/A), Finding (long text), Severity (status: Blocking, Must Fix Before Launch, Advisory, Clear), Reviewer (people)
> 3. **Talent & Rights Tracker** — columns: Asset (connect to Clearance Queue), Talent Name (text), Talent Type (dropdown: Actor, Model, Voiceover, Influencer, Music Artist, Photographer, Illustrator), Agreement Type (dropdown: Buyout, Licensed, SAG-AFTRA, Non-Union), Usage Rights (dropdown multi-select: TV, Digital, Social, OOH, Print, Radio, Experiential), Territory (dropdown multi-select: US, Canada, UK, EU, LATAM, APAC, Global), Usage Period (timeline), Expiry Date (date), Renewal Option (checkbox), Agreement Link (link)
>
> Automations: When asset is submitted with 'Urgent' priority, notify Legal Director immediately. When Review Status changes, notify Submitted By. When Deadline is tomorrow and status isn't 'Approved', escalate to Legal Director. When any Review Checklist item is 'Blocking', auto-set Priority to 'Urgent'. Dashboard with clearance queue by status, SLA performance, review volume by month, and bottleneck analysis by clearance area."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ClearanceBot
**Agent Purpose:** Triage incoming legal review requests, pre-screen for common issues, and manage the clearance queue to ensure SLA compliance.

**Triggers:**
- New asset submitted to Clearance Queue (via form)
- Deadline approaching (48hr, 24hr warnings)
- Review Status changes
- Daily queue health check (9 AM)

**Actions:**
- Auto-classify submission by clearance areas needed based on asset type and content description
- Pre-screen for common issues (superlative claims like "best" or "#1," competitor references, unsubstantiated health/performance claims)
- Assign reviewer based on clearance area expertise and current workload
- Track SLA countdown and send escalation notifications
- Generate daily queue summary for Legal Director (volume, aging, at-risk items)
- Compile weekly clearance metrics (volume, turnaround, SLA compliance, rejection rate)

**Data Required:**
- Clearance submission details (asset type, claims, talent, music)
- Reviewer expertise and availability
- Historical clearance data for turnaround benchmarking
- FTC/NAD guideline database for pre-screening rules
- Platform ad policy summaries

**Autonomy Level:** Human-in-the-Loop
Pre-screening and triage are automated; all legal clearance decisions require attorney review. Auto-escalation for SLA risk is autonomous.

**Example Interaction:**
> A creative team submits a social media video for Pepsi featuring a fitness influencer claiming the drink "boosts energy and performance." ClearanceBot triages the submission: Asset Type: Social Video → assigns to digital media reviewer. Pre-screen flags: (1) "Boosts energy" — potential FDA-regulated health claim requiring substantiation. (2) "Performance" — FTC endorsement guidelines apply since influencer is making efficacy claims. (3) Influencer content — requires FTC disclosure compliance check (#ad, #sponsored placement). (4) Pepsi trademark usage — verify brand guidelines compliance. The agent sets priority to "High" (health claim flag), assigns the senior regulatory attorney, and notifies the creative team: "Your Pepsi social video CLR-1847 has been received. Flagged areas: health claims, FTC endorsement compliance, trademark. Assigned to Maria (regulatory). Expected review: 48 hours. Note: health/performance claims may require substantiation documentation — please have available."

---

### Use Case 2: Client Contract & MSA Lifecycle Management

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Agency-client contracts are complex, bespoke documents that take weeks to negotiate. A Master Service Agreement (MSA) covers scope, fees, intellectual property ownership, confidentiality, indemnification, limitation of liability, termination rights, and increasingly, data processing terms and AI usage rights. Legal teams negotiate these with client procurement departments and outside counsel — a process involving 5–15 rounds of redlines over 4–8 weeks. Once signed, contracts are filed in a shared drive and effectively forgotten until renewal (or dispute). Nobody tracks key dates (renewal, termination notice periods), obligation compliance, or clause-level commitments. When a dispute arises ("the MSA says you owe us IP ownership of all campaign assets"), legal spends hours searching for the right version of the contract.

#### The Solution
monday.com Work Management for full contract lifecycle management. Every contract is tracked from negotiation through execution, compliance, and renewal. Key terms are extracted into structured fields for searchable, reportable data. Automations trigger renewal reviews, termination notice reminders, and obligation tracking. Integration with DocuSign handles execution workflow.

#### The Outcome
- Contract negotiation cycle reduced from 6 weeks to 3 weeks through structured workflow
- Zero missed renewal dates or termination notice deadlines
- Instant access to key contract terms without reading 40-page MSAs
- 50% reduction in outside counsel spend on routine contract reviews

#### Discovery Questions
1. "How many active client contracts does your legal team manage, and where do the executed versions live?"
2. "If I asked you right now what the termination notice period is for your top 5 clients, how quickly could you answer?"
3. "How do you track contract renewal dates — and have you ever missed a termination notice window?"
4. "What's your average contract negotiation cycle time, and how many rounds of redlines does a typical MSA go through?"
5. "How much do you spend on outside counsel for contract work that could potentially be handled with better templates and processes?"

#### Industry Context
Agency contracts have become increasingly client-favorable. Procurement departments at major brands (Procter & Gamble, Unilever, Coca-Cola) use standardized templates that heavily favor the client on IP, indemnification, and audit rights. The ANA's "contract compliance" initiative encourages advertisers to audit agency contracts annually. Key negotiation flashpoints: IP ownership (agencies want to retain underlying IP; clients want to own everything), indemnification scope (agencies resist unlimited indemnity for client-approved content), audit rights (clients want to audit fees and media; agencies want limitations), and AI clauses (who owns AI-generated content? can agencies use client data to train models?).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Contract Lifecycle Management workspace for an agency. Include:
> 1. **Contract Registry** — columns: Client Name (text), Contract Type (dropdown: MSA, SOW, Amendment, NDA, Data Processing Agreement, Influencer Agreement, Vendor Agreement), Contract ID (auto-number with prefix: AGR-), Effective Date (date), Expiration Date (date), Auto-Renewal (checkbox), Termination Notice Period (dropdown: 30 Days, 60 Days, 90 Days, 180 Days), Notice Deadline (formula: expiration - notice period), Assigned Attorney (people), Account Director (people), Status (status: Drafting, Internal Review, Client Negotiation, Pending Signature, Executed, Expired, Terminated), Contract Value (numbers with $), Document Link (link)
> 2. **Negotiation Tracker** — columns: Contract (connect to Contract Registry), Round Number (numbers), Date Sent (date), Sent By (dropdown: Agency, Client), Key Issues Open (long text), Issues Resolved (long text), Status (status: Drafting, Sent to Client, Client Redlines Received, Internal Review, Final), Days in Round (formula), Total Negotiation Days (formula)
> 3. **Key Terms Extract** — columns: Contract (connect to Contract Registry), IP Ownership (dropdown: Agency Retains, Client Owns All, Shared/Licensed, Custom), Indemnification Cap (text), Liability Cap (text), Audit Rights (dropdown: Unlimited, Annual with Notice, Limited Scope, None), Non-Compete (checkbox), Non-Compete Scope (text), AI Usage Rights (dropdown: Permitted, Restricted, Prohibited, Not Addressed), Data Processing Terms (dropdown: Included, Separate DPA, Not Addressed), Governing Law (text)
>
> Automations: When Notice Deadline is 30 days away, notify Legal and Account Director. When Negotiation round exceeds 10 business days, escalate. When Contract Status changes to 'Executed', auto-create Key Terms Extract item for attorney to complete. Dashboard with contract portfolio overview, negotiation pipeline, upcoming renewals/expirations calendar, and key terms comparison across clients."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ContractPilot
**Agent Purpose:** Manage the full contract lifecycle from negotiation through renewal, ensuring no deadlines are missed and key terms are always accessible.

**Triggers:**
- New contract created (negotiation initiated)
- Negotiation round exceeds time threshold
- Termination notice deadline approaching (90, 60, 30 days)
- Contract expiration approaching
- New SOW or amendment linked to existing MSA

**Actions:**
- Generate first draft from approved templates based on client tier and engagement type
- Track negotiation progress and flag stalled rounds
- Extract and catalog key terms upon execution
- Send renewal/expiration reminders to legal and account teams
- Generate contract comparison reports (how does this client's terms compare to portfolio norms?)
- Flag non-standard clauses that deviate from agency standard positions

**Data Required:**
- Contract templates by type and client tier
- Executed contract documents
- Key terms database
- Negotiation history
- Client relationship data (tier, revenue, strategic importance)

**Autonomy Level:** Human-in-the-Loop
Autonomous for tracking, reminders, and template generation. All legal review, negotiation decisions, and approval require attorney involvement.

**Example Interaction:**
> The account team initiates a new MSA for a Fortune 500 CPG company. ContractPilot generates a first draft from the enterprise MSA template, pre-populating known terms (standard agency IP position, $2M liability cap, mutual indemnification). The client's procurement team sends back redlines. ContractPilot catalogs the changes: "Round 1 — 14 substantive changes. Key issues: (1) Client requests full IP ownership including underlying creative elements (agency standard: client owns deliverables, agency retains underlying IP). (2) Unlimited indemnification (agency standard: capped at contract value). (3) Unrestricted audit rights with 5-day notice (agency standard: annual with 30-day notice). (4) New clause: prohibits agency use of generative AI on client work without written approval. Recommend: Accept #4 (becoming industry standard). Negotiate #1-3 per playbook. Similar client (Unilever) negotiation resolved in 4 rounds — historical redline attached for reference."

---

### Use Case 3: Influencer Agreement & Compliance Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Influencer marketing has exploded — but the legal infrastructure hasn't kept up. A single influencer campaign might involve 20–100 creators, each requiring individual agreements covering content deliverables, usage rights, exclusivity, FTC disclosure requirements, content approval workflows, and payment terms. These contracts are often managed by the influencer marketing team (not legal), using a mix of influencer platforms (CreatorIQ, Grin), email, and DMs. Legal only gets involved when something goes wrong — an influencer fails to disclose sponsorship, uses a competitor's product during an exclusivity period, or their content infringes a third-party copyright. The FTC's 2023 endorsement guidelines update made compliance more complex: disclosure must be "clear and conspicuous," not buried in hashtags, and the advertiser (agency's client) bears responsibility for influencer non-compliance.

#### The Solution
monday.com Work Management for end-to-end influencer agreement and compliance management. Every influencer engagement has a structured workflow from briefing through contracting, content approval, posting, and compliance verification. Standardized agreement templates are pre-populated based on deal type. FTC compliance checklists are embedded in the approval workflow. Usage rights tracking ensures content isn't used beyond licensed terms.

#### The Outcome
- 100% FTC disclosure compliance (vs. industry average of ~70%)
- Influencer contracting time reduced from 2 weeks to 3 days with standardized templates
- Zero usage rights violations (content archived when rights expire)
- Complete audit trail for every influencer engagement — FTC investigation-ready

#### Discovery Questions
1. "How many influencer agreements does your team manage per quarter, and what's the process for getting them executed?"
2. "How do you verify that influencers are complying with FTC disclosure requirements — is there a systematic check or is it spot-check based?"
3. "When an influencer's content usage rights expire, how do you ensure that content is taken down from all channels?"
4. "Have you had any FTC-related issues with influencer content, and what would your response process look like if the FTC sent an inquiry?"

#### Industry Context
The FTC issued 700+ warning letters to advertisers and influencers between 2021–2024 for inadequate disclosure. Penalties can reach $50,000+ per violation. The key compliance requirements: material connections must be disclosed "clearly and conspicuously" (not buried in hashtags or below the fold), disclosures must be in the same language as the endorsement, and the advertiser is responsible for monitoring influencer compliance. Platform-specific rules add complexity: Instagram requires branded content tags, TikTok has its own disclosure tools, and YouTube requires both verbal and visual disclosure. The SAG-AFTRA influencer agreement (2024) has added union considerations for certain creator tiers.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an Influencer Agreement & Compliance workspace. Include:
> 1. **Influencer Engagements** — columns: Influencer Name (text), Handle (text), Platform (dropdown: Instagram, TikTok, YouTube, Twitter/X, Twitch, Podcast, Multi-Platform), Campaign (text), Client (text), Engagement Type (dropdown: Paid Post, Gifting, Ambassador, Affiliate, Event Appearance), Fee (numbers with $), Content Deliverables (long text), Agreement Status (status: Briefing, Negotiating, Contracted, Active, Complete, Terminated), FTC Compliance Status (status: Pending Review, Compliant, Non-Compliant, Remediated), Usage Rights (dropdown: 30 Days, 90 Days, 6 Months, 1 Year, Perpetual, Buyout), Rights Expiry Date (date), Exclusivity (checkbox), Exclusivity Category (text), Exclusivity Period (timeline), Content Approval Required (checkbox)
> 2. **Content Submissions** — columns: Influencer (connect to Influencer Engagements), Content Type (dropdown: Photo, Video, Story, Reel, TikTok, Blog Post, Tweet, Live Stream), Submission Date (date), Post Date (date), Content Link (link), Legal Review (status: Pending, Approved, Revisions Required, Rejected), FTC Disclosure Present (checkbox), Disclosure Type (dropdown: #ad, #sponsored, Branded Content Tag, Verbal Disclosure, Partnership Label), Disclosure Visible (checkbox), Claims Made (long text), Notes (long text)
> 3. **Compliance Audit Log** — columns: Influencer (connect), Audit Date (date), Auditor (people), Disclosure Compliant (checkbox), Content Matches Brief (checkbox), Exclusivity Compliant (checkbox), Issues Found (long text), Remediation Required (long text), Remediation Status (status: N/A, Open, In Progress, Resolved)
>
> Automations: When Rights Expiry Date is 14 days away, notify marketing team to archive content. When FTC Disclosure Present is unchecked on any Content Submission, auto-flag as 'Non-Compliant' and alert legal. When Exclusivity Period ends, update influencer status. Dashboard with compliance rate, active engagements by platform, rights expiry calendar, and spend by influencer tier."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** InfluencerGuard
**Agent Purpose:** Ensure FTC compliance across all influencer engagements and manage the full lifecycle of influencer agreements and content rights.

**Triggers:**
- New influencer content submitted for review
- Content posted by influencer (link provided)
- Usage rights expiry approaching (30, 14, 7 days)
- Weekly compliance audit schedule
- Exclusivity violation alert (manual flag)

**Actions:**
- Review submitted content for FTC disclosure presence and placement
- Cross-reference content against brief to verify compliance with agreement terms
- Flag content with product claims that may require substantiation
- Track content rights and send takedown reminders when rights expire
- Monitor exclusivity compliance by checking influencer's public posts
- Generate campaign-level compliance report for client and legal review
- Compile FTC-ready audit documentation

**Data Required:**
- Influencer agreements and terms
- Content submissions and post links
- FTC disclosure guidelines and requirements
- Platform-specific disclosure rules
- Exclusivity terms and competitive category definitions

**Autonomy Level:** Escalation-Based
Autonomous for compliance checking and flagging. Escalates non-compliance to legal for remediation decisions. Content approval always requires human review.

**Example Interaction:**
> An influencer posts a TikTok for a skincare client. InfluencerGuard checks the posted content: Video reviewed — (1) FTC disclosure: "#ad" present but only in caption text, not visible in first 3 seconds of video per TikTok best practice. Recommendation: request verbal disclosure or opening text overlay. (2) Claims check: Influencer says "this cleared my acne in 2 weeks" — this is an efficacy claim that may require FDA consideration (OTC drug claim vs. cosmetic claim). Flagging to regulatory attorney. (3) Competitor product visible in background at 0:22 — exclusivity clause covers skincare category. Low risk but flagging for awareness. Remediation request sent to influencer marketing team: "Please ask @creator to add verbal disclosure ('partnered with [Brand]') and remove/reshoot scene with competitor product visible. Efficacy claim under legal review — may need to request content edit."

---

### Use Case 4: Intellectual Property Management & Trademark Clearance

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Agencies create intellectual property at massive scale — brand names, taglines, logos, campaign concepts, jingles, characters — and must ensure none of it infringes existing marks or rights. Trademark clearance for a new campaign tagline involves searching USPTO, international trademark databases, common law usage, and domain availability. A comprehensive search takes 1–2 weeks and costs $1,500–$5,000 through outside counsel. With agencies generating dozens of campaign concepts per month, the volume and cost of clearance is significant. Worse, IP ownership disputes between agencies and clients are increasingly common — the contract says one thing, but the practical reality of who contributed what to the creative is murky. Agencies also need to protect their own IP: proprietary methodologies, tools, and creative approaches that differentiate them.

#### The Solution
monday.com Work Management for IP tracking and trademark clearance workflow. Every creative asset with potential IP value is cataloged with ownership status, clearance history, and usage rights. Trademark clearance requests follow a structured workflow from initial search through legal opinion. IP ownership is tracked at the deliverable level, linked to contract terms. Agency proprietary IP (methodologies, tools, frameworks) is registered and monitored.

#### The Outcome
- Trademark clearance turnaround reduced from 2 weeks to 5 days
- Complete IP registry — know exactly what the agency owns vs. what clients own
- 30% reduction in outside counsel spend on clearance through better pre-screening
- Zero IP infringement incidents through systematic clearance workflow

#### Discovery Questions
1. "How do you currently handle trademark clearance for new campaign names and taglines — and what's the typical turnaround?"
2. "Do you have a registry of IP the agency has created and who owns it — could you pull that up right now?"
3. "How do you track the IP ownership split between agency and client on a campaign-by-campaign basis?"
4. "What's your annual spend on outside trademark counsel, and how much of that is for routine clearance versus complex disputes?"

#### Industry Context
IP ownership is one of the most contested areas in agency-client relationships. Historically, agencies retained significant IP (the "spec work" debate), but modern contracts increasingly assign all deliverable IP to clients. The rise of AI-generated content has created new questions: if an agency uses Midjourney to create visual concepts, who owns the output? (Current US copyright law is unsettled — AI-generated works may not be copyrightable.) Agencies are also grappling with "pitch IP" — creative concepts presented in pitches that they don't win. Industry practice varies on whether pitch work is compensated and who owns concepts presented but not selected.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an Intellectual Property Management workspace. Include:
> 1. **IP Registry** — columns: Asset Name (text), IP Type (dropdown: Trademark/Name, Tagline/Slogan, Logo/Visual Mark, Campaign Concept, Methodology/Framework, Software/Tool, Character/Mascot, Jingle/Music, Photography, Video Content), Owner (dropdown: Agency, Client, Shared, TBD/Disputed), Client (text), Campaign (text), Creation Date (date), Creator (people), Registration Status (dropdown: Not Registered, Application Filed, Registered, Lapsed), Registration Number (text), Jurisdictions (dropdown multi-select: US, EU, UK, Canada, Global), Contract Reference (connect to Contract Registry), Usage Rights Notes (long text)
> 2. **Trademark Clearance Requests** — columns: Proposed Mark (text), Mark Type (dropdown: Word Mark, Logo, Tagline, Domain, Sound Mark), Client (text), Requestor (people), Priority (status: Urgent, Standard), Preliminary Search Status (status: Not Started, In Progress, Clear, Potential Conflict, Conflict Found), Full Search Status (status: Not Needed, Ordered, In Progress, Clear, Risk Identified), Outside Counsel Assigned (text), Legal Opinion (dropdown: Clear to Use, Use with Modifications, Do Not Use, Conditional), Search Cost (numbers with $), Request Date (date), Completion Date (date), Turnaround Days (formula), Notes (long text)
> 3. **IP Disputes & Watch** — columns: Issue Name (text), Type (dropdown: Infringement Claim Against Agency, Agency Infringement Claim, Ownership Dispute, Cease & Desist), Opposing Party (text), Related IP (connect to IP Registry), Status (status: Monitoring, Active Dispute, Negotiating, Resolved, Litigated), Risk Level (status: Low, Medium, High, Critical), Assigned Attorney (people), Outside Counsel (text), Estimated Exposure (numbers with $), Resolution (long text)
>
> Automations: When Preliminary Search finds 'Potential Conflict', auto-escalate to full search. When Registration Status is 'Registered' and renewal date is 6 months away, remind legal. When new Trademark Clearance Request is 'Urgent', notify IP attorney immediately. Dashboard with IP portfolio summary, clearance pipeline, dispute tracker, and outside counsel spend."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** IPNavigator
**Agent Purpose:** Streamline trademark clearance, maintain the agency's IP registry, and flag potential infringement risks.

**Triggers:**
- New trademark clearance request submitted
- IP registration renewal approaching
- New campaign creative submitted for review (pre-screen for IP issues)
- Quarterly IP portfolio review schedule

**Actions:**
- Conduct preliminary trademark search using public databases (USPTO TESS, EUIPO)
- Pre-screen creative assets for potential trademark or copyright issues
- Flag similar marks in the registry to avoid internal conflicts
- Track clearance progress and outside counsel communications
- Monitor registration renewal dates and file reminders
- Generate quarterly IP portfolio report with valuation estimates

**Data Required:**
- IP registry with full asset details
- Trademark database access (USPTO, EUIPO)
- Contract terms for IP ownership provisions
- Outside counsel contact and billing information
- Creative asset database for cross-reference

**Autonomy Level:** Human-in-the-Loop
Autonomous for preliminary searches and monitoring. All legal opinions, registration decisions, and dispute responses require attorney review.

**Example Interaction:**
> The creative team proposes the tagline "Think Different. Act Bold." for a tech client campaign. IPNavigator conducts a preliminary search: "Preliminary Trademark Analysis — 'Think Different. Act Bold.' Findings: (1) HIGH RISK: 'Think Different' is a registered trademark of Apple Inc. (US Reg. #2,161,133, International Classes 9, 35, 42). While Apple's mark is for technology products/services and your use is in advertising, the mark is famous and likely to be protected across categories under dilution doctrine. (2) 'Act Bold' — no exact matches found. 3 similar marks in unrelated categories. Low risk. Recommendation: Do not proceed with 'Think Different' element. Consider alternatives: 'Think Forward. Act Bold.' or 'Dream Different. Act Bold.' — both clear in preliminary search. Full search recommended if client proceeds with alternative."

---

### Use Case 5: Advertising Regulatory Compliance Tracking

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Advertising regulations vary by industry, medium, geography, and product category — and they change constantly. An agency working across consumer goods, pharmaceuticals, financial services, and alcohol must navigate different regulatory frameworks for each. The FTC regulates advertising claims broadly; the FDA adds requirements for pharma and food; the TTB governs alcohol advertising; the FCC regulates broadcast; the FHA governs real estate advertising; and state attorneys general enforce their own rules. Add international markets (ASA in the UK, ARPP in France, ASCI in India) and the complexity multiplies. Legal teams maintain this knowledge in their heads and in scattered reference documents. When regulations change (like the FTC's 2023 endorsement update), there's no systematic way to identify which active campaigns are affected.

#### The Solution
monday.com Work Management for regulatory intelligence and compliance tracking. A regulatory database tracks requirements by product category, medium, and geography. Active campaigns are tagged with applicable regulations. When regulations change, automations identify affected campaigns and trigger compliance reviews. Compliance checklists are embedded in the creative clearance workflow.

#### The Outcome
- Zero regulatory violations through systematic compliance tracking
- 50% faster response to regulatory changes (identify affected campaigns within hours, not weeks)
- Structured compliance knowledge that doesn't walk out the door when an attorney leaves
- Client confidence: demonstrable compliance processes win and retain regulated industry clients

#### Discovery Questions
1. "When the FTC updated its endorsement guidelines in 2023, how did you identify which active campaigns needed to be reviewed for compliance?"
2. "How do you ensure that an ad for a pharmaceutical client meets FDA requirements while also complying with network broadcast standards?"
3. "If your agency took on a new alcohol brand client tomorrow, how quickly could your legal team get up to speed on TTB advertising regulations?"
4. "Do you have a systematic way to track regulatory requirements by product category, or does it depend on individual attorney expertise?"

#### Industry Context
The regulatory landscape for advertising is a patchwork. Key bodies: FTC (general advertising claims, endorsements, privacy), FDA (drug, medical device, food/supplement advertising), TTB (alcohol advertising), FCC (broadcast indecency, children's advertising — CARU), state AGs (state-level consumer protection), NAD (industry self-regulation through BBB), CARU (children's advertising self-regulation), and international equivalents. The trend is toward stricter enforcement: the FTC brought more advertising enforcement cases in 2023 than any year in the prior decade. AI-generated advertising is the newest frontier — the FTC has signaled that AI-generated content must be disclosed and that AI doesn't absolve advertisers of substantiation requirements.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Regulatory Compliance workspace. Include:
> 1. **Regulatory Database** — columns: Regulation/Guideline (text), Regulatory Body (dropdown: FTC, FDA, TTB, FCC, NAD, CARU, State AG, ASA-UK, ARPP-France, ASCI-India, EU-AVMSD, Platform Policy), Product Category (dropdown multi-select: General Consumer, Pharma/OTC, Food/Beverage, Alcohol, Financial Services, Automotive, Real Estate, Children's Products, Technology, Gambling), Medium (dropdown multi-select: TV/Broadcast, Digital, Social, Print, OOH, Radio, Podcast, Influencer, Email), Key Requirements (long text), Last Updated (date), Source Link (link), Internal Expert (people)
> 2. **Active Campaign Compliance** — columns: Campaign (text), Client (text), Product Category (dropdown), Markets (dropdown multi-select), Media Channels (dropdown multi-select), Applicable Regulations (connect to Regulatory Database), Compliance Status (status: Review Needed, Under Review, Compliant, Issue Found, Remediated), Assigned Reviewer (people), Last Reviewed (date), Notes (long text)
> 3. **Regulatory Updates** — columns: Update Title (text), Regulatory Body (dropdown), Effective Date (date), Summary (long text), Impact Assessment (status: High Impact, Medium Impact, Low Impact, Informational), Affected Campaigns (connect to Active Campaign Compliance), Action Required (long text), Status (status: New, Assessed, Actions Taken, Closed), Source Link (link)
>
> Automations: When new Regulatory Update is added with 'High Impact', notify all attorneys and affected campaign owners. When Active Campaign Compliance Status is 'Issue Found', block from clearance queue approval. Dashboard with compliance status by product category, regulatory update timeline, and attorney workload by specialty."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** RegWatch
**Agent Purpose:** Monitor regulatory changes, assess campaign impact, and ensure advertising compliance across all product categories and markets.

**Triggers:**
- New regulatory update added to database
- New campaign enters active status
- Quarterly compliance audit schedule
- FTC/NAD enforcement action published (manual feed)

**Actions:**
- Match new campaigns against applicable regulations based on product category, medium, and geography
- Generate compliance checklists tailored to each campaign's regulatory profile
- Assess impact of regulatory changes on active campaigns
- Surface relevant enforcement actions as precedent alerts ("NAD just challenged a claim similar to your client's")
- Compile regulatory briefing for new client onboarding (what rules apply to their category)
- Generate annual compliance audit report

**Data Required:**
- Regulatory database with current requirements
- Active campaign details (product category, claims, channels, markets)
- Enforcement action database (FTC, NAD, state AG)
- Industry news feeds for regulatory updates

**Autonomy Level:** Escalation-Based
Autonomous for monitoring and matching. Compliance assessments and remediation recommendations require attorney review.

**Example Interaction:**
> The FTC publishes new guidance on AI-generated testimonials in advertising (effective in 60 days). RegWatch scans the active campaign database: "FTC AI Testimonial Guidance — Impact Assessment. 7 active campaigns use AI-generated or AI-enhanced testimonials. HIGH IMPACT (3 campaigns): (1) Samsung — AI-generated user reviews in digital ads (must add disclosure). (2) L'Oréal — AI-enhanced before/after imagery (may constitute deceptive practice under new guidance). (3) Nike — AI avatar delivering product testimonial in CTV spot (requires 'AI-generated' disclosure). MEDIUM IMPACT (4 campaigns): Use AI in production but not in testimonial context. Recommended action: Schedule compliance review for 3 high-impact campaigns within 2 weeks. Prepare AI disclosure language templates for creative teams. Brief account directors on new requirements for client communication. Deadline: guidance effective April 15."

---

### Use Case 6: Legal Matter & Outside Counsel Management

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Agency legal teams handle a wide variety of matters — from routine NDAs to complex litigation — while also managing relationships with 5–15 outside counsel firms specializing in different areas (IP, employment, regulatory, litigation). There's no central system to track open matters, outside counsel assignments, budgets, or outcomes. Legal spend is tracked in accounting but not connected to matter details, making it impossible to assess cost-effectiveness or benchmark firms. When the General Counsel needs a status update on all open matters, it requires polling each attorney and compiling manually. Time-sensitive matters (cease and desist responses, discovery deadlines, regulatory filings) are tracked individually, with risk of deadline misses.

#### The Solution
monday.com Work Management as a legal matter management system. Every legal matter — from internal requests to external disputes — is tracked with structured metadata, timelines, assignments, and budgets. Outside counsel engagements are connected to matters with spend tracking. Automations enforce deadline management and status reporting.

#### The Outcome
- Complete visibility into all open legal matters in one dashboard
- Zero missed deadlines through automated tracking and escalation
- 20% reduction in outside counsel spend through budget tracking and firm benchmarking
- General Counsel gets real-time portfolio view without polling the team

#### Discovery Questions
1. "How many open legal matters does your team have at any given time, and is there a single place to see them all?"
2. "How do you track outside counsel spend — and can you tell me which firms are most cost-effective for which matter types?"
3. "How do you manage legal deadlines — court filing dates, regulatory response deadlines, statute of limitations?"
4. "When your General Counsel needs a status update on all open matters, how long does it take to compile?"

#### Industry Context
Agency legal departments operate as internal law firms serving multiple "clients" (departments, clients, executives). The shift toward in-house legal teams (vs. relying entirely on outside counsel) has increased the need for matter management. Typical outside counsel specialties for agencies: IP/trademark (Kilpatrick, Fish & Richardson), employment (Littler, Jackson Lewis), advertising regulatory (Venable, Davis & Gilbert), and litigation (varies). Legal operations — the practice of applying business operations principles to legal departments — is growing, with legal ops roles appearing at larger agencies and holding companies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Legal Matter Management workspace. Include:
> 1. **Matter Registry** — columns: Matter Name (text), Matter ID (auto-number with prefix: LGL-), Matter Type (dropdown: Contract Dispute, IP/Trademark, Employment, Regulatory, Compliance Advisory, Litigation, Corporate, M&A, Data Privacy, Real Estate), Client/Department (text), Assigned Attorney (people), Status (status: Open, Active, On Hold, Awaiting Response, Settled, Closed), Priority (status: Critical, High, Medium, Low), Opened Date (date), Target Close (date), Key Deadlines (date), Outside Counsel (text), Budget (numbers with $), Actual Spend (numbers with $), Budget Remaining (formula), Risk Assessment (status: Low, Medium, High, Critical), Outcome (dropdown: Favorable, Unfavorable, Settled, Withdrawn, Ongoing), Summary (long text)
> 2. **Deadline Tracker** (subitems) — columns: Deadline Description (text), Due Date (date), Owner (people), Status (status: Upcoming, Due Soon, Complete, Overdue), Days Until Due (formula), Court/Regulatory Filing (checkbox), Notes (long text)
> 3. **Outside Counsel Tracker** — columns: Firm Name (text), Specialty (dropdown), Primary Contact (text), Hourly Rate Range (text), Matter (connect to Matter Registry), Budget (numbers with $), YTD Spend (numbers with $), Invoice Status (status: Current, Overdue), Performance Rating (numbers 1-5), Notes (long text)
>
> Automations: When Deadline is 7 days away, alert Assigned Attorney. When Deadline is overdue, escalate to General Counsel. When Actual Spend exceeds 80% of Budget, alert attorney and GC. Dashboard with open matters by type and status, deadline calendar, outside counsel spend analysis, and matter aging report."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MatterManager
**Agent Purpose:** Track all legal matters, enforce deadline compliance, and optimize outside counsel management.

**Triggers:**
- New matter created
- Deadline approaching (14, 7, 3, 1 days)
- Outside counsel invoice received
- Monthly matter portfolio review schedule
- Matter budget threshold crossed (80%, 100%)

**Actions:**
- Generate matter intake form with required fields based on matter type
- Track all deadlines and send cascading reminders
- Match new matters to appropriate outside counsel based on specialty, rate, and performance
- Compile monthly matter portfolio report for General Counsel
- Track outside counsel spend against budgets and flag overruns
- Benchmark outside counsel performance across matters
- Archive closed matters with outcome data for institutional knowledge

**Data Required:**
- Matter details and history
- Deadline database
- Outside counsel directory with rates and performance history
- Budget and spend data
- Legal department capacity data

**Autonomy Level:** Fully Autonomous
All tracking, monitoring, and reporting automated. Escalates overdue deadlines and budget overruns. Matter decisions always require attorney judgment.

**Example Interaction:**
> A former employee files a wrongful termination claim. MatterManager creates matter LGL-0284, classifies it as Employment/Litigation, assigns it high priority, and recommends outside counsel: "Suggested firm: Jackson Lewis (employment specialty, used for 3 prior matters, avg rating 4.3/5, rate: $475-650/hr). Alternative: Littler (higher rate $550-750/hr but 4.8/5 rating on similar matters). Budget recommendation based on similar past matters: $35K-$75K depending on whether it settles or goes to hearing." It creates deadline subitems: response to demand letter (14 days), EEOC filing deadline tracking, and discovery deadlines. Weekly, it sends the GC a portfolio update: "32 open matters. 3 critical deadlines this week. Outside counsel YTD spend: $340K of $500K annual budget (68% at month 8 = on track). New: employment matter LGL-0284 — initial assessment memo due from outside counsel Friday."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| MSA (Master Service Agreement) | Overarching contract between agency and client governing the relationship |
| SOW (Scope of Work) | Document defining specific deliverables, timeline, and fees under the MSA |
| FTC (Federal Trade Commission) | US federal agency regulating advertising practices, endorsements, and consumer protection |
| NAD (National Advertising Division) | Industry self-regulatory body that reviews advertising claims (part of BBB National Programs) |
| CARU (Children's Advertising Review Unit) | Self-regulatory body for advertising directed at children under 13 |
| ASA (Advertising Standards Authority) | UK's independent advertising regulator |
| Substantiation | Requirement that advertising claims be supported by competent and reliable evidence |
| Clearance | Legal review process to approve creative content for publication |
| Talent Rights | Legal rights governing the use of a performer's name, likeness, and performance |
| SAG-AFTRA | Screen Actors Guild – American Federation of Television and Radio Artists (talent union) |
| Sync License | License to use a musical composition in synchronization with visual content |
| Master Use License | License to use a specific recording of a musical composition |
| IP Assignment | Transfer of intellectual property ownership from creator to another party |
| Work for Hire | Legal doctrine where IP created by employees or contractors belongs to the hiring party |
| Indemnification | Contractual obligation for one party to compensate the other for certain losses |
| Right of Publicity | Legal right to control commercial use of one's name, image, and likeness |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| General Counsel | Legal strategy, risk management, outside counsel oversight, executive advisory | Decision-maker |
| Senior Attorney / Associate GC | Complex matters, contract negotiation, litigation management | Decision-maker (within area) |
| Advertising Attorney | Creative clearance, FTC compliance, claims review | User/Influencer |
| IP Attorney | Trademark clearance, copyright, IP portfolio management | User/Influencer |
| Contracts Manager / Paralegal | Contract drafting, execution, filing, deadline tracking | User |
| Chief Creative Officer | Creative output — requires legal clearance, often pushes back on legal restrictions | Influencer |
| Head of Influencer Marketing | Manages influencer relationships, needs compliant agreements and workflows | User/Influencer |
| Chief Financial Officer | Legal budget, outside counsel spend, risk quantification | Decision-maker (budget) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Creative | Primary source of legal clearance requests — every asset needs review | Integrated clearance workflow reduces friction between creative and legal |
| Account Management | Client contract negotiations, scope change management | Connected contract lifecycle from SOW to billing |
| Influencer Marketing | Influencer agreements, FTC compliance, content approval | End-to-end influencer compliance from agreement to post verification |
| Media | Media vendor contracts, platform terms of service, data privacy | Media vendor agreement management and platform compliance tracking |
| HR | Employment law, contractor classification, non-compete agreements | Unified legal matter tracking across corporate and client-facing legal work |
| Finance | Legal budget tracking, outside counsel spend, billing disputes | Connected legal spend and matter management for budget optimization |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Clio / PracticePanther | Legal practice management for law firms | monday.com provides matter management plus cross-functional workflow (creative clearance, contract lifecycle) that pure legal tools don't address |
| Ironclad / ContractPodAi | Contract lifecycle management | monday.com offers broader workflow coverage — contracts plus clearance plus compliance plus matter management — vs. single-purpose CLM |
| DocuSign CLM | Contract management with e-signature | monday.com integrates with DocuSign for signatures while adding the surrounding workflow (negotiation tracking, compliance, renewals) |
| SharePoint / Shared Drives | Document storage for contracts and legal files | monday.com adds structure, workflow, and automation to document management — transforms static storage into active legal operations |
| Jira (adapted for legal) | Issue tracking adapted for legal matters | monday.com is designed for business users — attorneys adopt it more readily than developer-focused tools |
| Excel / Google Sheets | Tracking contracts, deadlines, and matters | monday.com replaces fragile, disconnected spreadsheets with automated, connected, auditable workflows |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "Our legal matters are too sensitive for a cloud platform" | "monday.com is SOC 2 Type II certified, HIPAA-eligible, and encrypts data at rest and in transit. Permission controls can restrict legal boards to only authorized personnel. Many law firms and legal departments use monday.com for matter management with full data security compliance." |
| "We only have 3 attorneys — we don't need a system" | "That's exactly why you need one. Three attorneys handling 500+ clearance requests, 50+ contracts, and dozens of open matters can't afford to lose time searching emails and shared drives. Automation handles the tracking so your attorneys can focus on legal judgment — the stuff only humans can do." |
| "Our attorneys won't adopt new technology" | "monday.com isn't asking attorneys to change how they practice law — it changes how the work gets to them and how they track it. Submissions come via forms (no more email hunting), deadlines are automated (no more calendar entries), and status is visible (no more 'where's my review?' emails). Most attorneys love it because it reduces interruptions." |
| "We use DocuSign/Ironclad for contracts — that's enough" | "DocuSign handles execution; it doesn't manage the 6-week negotiation, the key terms extraction, the renewal reminders, or the compliance tracking after signing. monday.com manages the entire lifecycle — the contract work that happens before and after the signature." |
| "Legal work is too nuanced for automation" | "Absolutely — and we're not automating legal judgment. We're automating the routing, tracking, and deadline management that surrounds legal judgment. Your attorneys still make every decision; they just spend less time on email triage and more time on actual legal work." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for agency using monday.com for creative legal clearance]
- [Placeholder for holding company managing contracts across agency network on monday.com]
- [Placeholder for legal team that reduced clearance turnaround time with monday.com]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
