# Advertising & Marketing × Sales Playbook

## Overview

Sales in advertising and marketing agencies is fundamentally different from product sales. There's no fixed product, no price list, and no simple feature comparison. Agency sales (often called "New Business" or "Business Development") is about selling capabilities, chemistry, and the promise of creative problem-solving. It's long-cycle, relationship-driven, and often frustrating.

The Sales function in agencies typically spans new business development (hunting new clients), pitch management (RFP responses and proactive pitches), partnership development (client referrals, agency partnerships), and expansion (growing existing clients into new services). At mid-to-large agencies, this function is usually a small dedicated team (2-10 people) supported by agency leadership who serve as closers.

What makes this combination unique: Agency sales cycles are long (3-12 months for major clients), the competition is often blind (you don't know who you're pitching against), and the "product" changes with every pitch. Win rates on RFPs are often 15-25%, making efficiency crucial. AI can accelerate research, personalize pitches, and give better visibility into what's working and what isn't.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - New business teams are always too small for the opportunity
   - Each pitch requires significant research and customization
   - AI enables more pitches, better research, and faster turnaround
   
2. **Replace or Radically Augment Headcount** — HIGH RELEVANCE
   - Pitch research, credential customization, and proposal writing consume time
   - BizDev professionals spend hours on research that AI could accelerate
   - Administrative tasks (tracking, follow-up) can be automated

3. **Consolidate Tech Stack with AI** — MEDIUM RELEVANCE
   - BizDev often uses a patchwork of CRM, spreadsheets, and email
   - Integration with marketing, case studies, and proposal tools is rare
   - One system connecting pipeline, content, and outcomes improves efficiency

---

## Prioritized Use Cases

### 1. New Business Pipeline & CRM
**Relevance**: High  
**Value Driver**: 2 (Consolidate Tech Stack)

**Pain Point**: 
Agency pipelines are opaque. Opportunities live in emails, heads, and scattered spreadsheets. Leadership asks "what's in the pipeline?" and gets a different answer every time. There's no systematic tracking of where opportunities came from, why they were won or lost, or what the realistic revenue forecast is.

**Solution**: 
monday.com CRM designed for agency new business. Track every opportunity from first touch to close, with stages that reflect agency sales reality (not product sales). Capture source, qualification criteria, and win/loss reasons. AI helps score and prioritize.

**Vibe Prompt**:
```
Build a New Business Pipeline app for agency business development teams.

Purpose: Track new business opportunities from awareness to close with full pipeline visibility.

Key features:
- Opportunity board: Prospect name, Industry, Company size, Source (Inbound/Referral/Outbound/RFP/Event), Estimated value (annual), Owner, Status
- Agency-specific stages: Awareness → Qualified → Intro Meeting → Chemistry → Pitch/Proposal → Negotiation → Won/Lost
- Contact management: Key contacts, Decision maker, Champion, Influencers, Meeting history
- Qualification criteria: Budget, Authority, Need, Timeline (BANT), Fit score
- AI lead scoring: Score based on fit criteria, engagement level, and historical patterns
- Activity tracking: Calls, emails, meetings, proposals — logged automatically where possible
- Win/loss tracking: When closed, capture outcome, reasons, and learnings
- Revenue forecasting: Weighted pipeline by stage and probability
- Dashboard: Pipeline by stage, By source, Forecast, Win rate, Average deal size, Velocity (time to close)

Include automations:
- When opportunity created, auto-score based on fit criteria
- When stage changes, notify team and update probability
- When no activity for 14 days, prompt owner
- When opportunity won/lost, prompt for win/loss analysis
- Weekly pipeline review email to leadership
```

**Outcome**: 
- Clear visibility into pipeline and forecast
- Better prioritization of opportunities
- Systematic learning from wins and losses
- Accountability for follow-up

**Discovery Questions**:
- "If I asked you right now what your new business pipeline looks like, how quickly could you answer with confidence?"
- "What's your win rate on pitches? Do you track it?"
- "When you lose a pitch, do you know why? Is that knowledge captured somewhere?"

**Industry-Specific Context**: 
Agency sales cycles: 3-6 months for mid-market, 6-12 months for enterprise. "Chemistry meeting" = client/agency compatibility assessment. "Pitch" = formal presentation of capabilities and proposed approach.

---

### 2. Pitch & Proposal Management
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
RFPs and pitches are resource-intensive. Each requires customized research, tailored credentials, a strategic approach, and often speculative creative work. Teams scramble to assemble materials, reinvent the wheel, and work late nights. The process is chaotic and stressful.

**Solution**: 
monday.com pitch management that brings structure to chaos. Track RFP requirements systematically, manage the pitch team's work, pull from existing assets (case studies, credentials), and use AI to accelerate research and drafting. Never miss a deadline or forget a requirement.

**Vibe Prompt**:
```
Build a Pitch & Proposal Management app for agency new business teams.

Purpose: Manage RFPs and pitches from intake to submission with team coordination and asset management.

Key features:
- Pitch intake: Opportunity link, RFP received date, Due date, Client, Industry, Requirements summary
- Requirements parsing: Extract and track all RFP requirements as checklist items
- Pitch team: Roles needed (Strategy Lead/Creative Lead/Account Lead/Production), Assigned team members
- Work plan: Tasks needed, Owners, Due dates, Status — working back from deadline
- Asset assembly: Case studies to include (pull from library), Credentials deck, Team bios, Pricing
- AI research assist: Company background, Industry trends, Competitive landscape, News monitoring
- AI drafting assist: Draft sections based on requirements and past successful pitches
- Review workflow: Draft → Internal review → Leadership review → Final
- Submission tracking: Submitted date, Confirmation, Follow-up scheduled
- Dashboard: Active pitches, By stage, Deadline countdown, Team workload, Asset reuse stats

Include automations:
- When pitch created, generate task template based on timeline and pitch type
- When requirement added, check for relevant case studies
- 48 hours before deadline, alert team of incomplete items
- When submitted, schedule follow-up reminders
- When pitch outcome known, update pipeline and prompt for debrief
```

**Outcome**: 
- More organized pitch process (less scrambling)
- Faster pitch assembly through asset reuse
- Better research with AI assistance
- Higher quality submissions

**Discovery Questions**:
- "How many pitches do you have active at any given time? How do you track them?"
- "When you start a new pitch, how much do you reuse vs. create from scratch?"
- "How much time does your team spend on pitch research?"

**Industry-Specific Context**: 
RFP = Request for Proposal (formal). RFI = Request for Information (early stage). "Spec creative" = speculative creative work done during pitch (controversial but common). "Pitch deck" = presentation for pitch meeting.

---

### 3. Credentials & Case Study Assembly
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Every pitch needs credentials — proof that you've done relevant work. But case studies are scattered, outdated, or missing key information. BizDev teams spend hours hunting for the right examples, then reformatting them for each pitch. The same case study gets recreated from scratch multiple times.

**Solution**: 
monday.com case study library integrated with pitch process. Maintain a searchable, always-current library of case studies with all necessary assets. AI recommends relevant case studies for each pitch based on industry, service type, and challenge.

**Vibe Prompt**:
```
Build a Credentials & Case Study Library app for agency new business teams.

Purpose: Maintain a searchable library of case studies and credentials for pitch assembly.

Key features:
- Case study database: Project name, Client, Industry, Service type, Challenge, Solution, Results, Assets (deck slides, images, video), Status (Draft/Approved/Needs Update)
- Taxonomy: Industry tags, Service tags, Capability tags, Results type (brand/performance/engagement)
- Search and filter: Find case studies by any combination of tags
- AI recommendations: Given pitch requirements, suggest most relevant case studies
- Version tracking: Multiple versions (long/short/one-pager), Last updated date
- Results database: Quantified results searchable across all case studies
- Client approval status: Can we name the client? Use specific results? Show creative?
- Quick export: Generate formatted case study slides for pitch deck
- Dashboard: Total case studies, By industry, By service, Recently updated, Update needed (flagged)

Include automations:
- When pitch created, AI suggests relevant case studies
- When case study >12 months old, flag for update
- When project wins award, prompt to update case study
- When client approval changes, update all affected versions
- Quarterly case study audit: What's missing by industry/service
```

**Outcome**: 
- Faster pitch assembly (minutes, not hours, to find case studies)
- Consistent, always-current case study library
- More relevant case studies in pitches (AI-matched)
- Never scramble for proof points again

**Discovery Questions**:
- "When you need a case study for a pitch, how long does it take to find the right one?"
- "How many of your case studies are current? How many need updates?"
- "Have you ever lost a pitch because you couldn't prove relevant experience?"

**Industry-Specific Context**: 
Case studies are the currency of agency pitches. "Credentials deck" = overview of agency experience. Client approval is often the bottleneck. Award wins significantly increase case study value.

---

### 4. Prospect Research & Intelligence
**Relevance**: High  
**Value Driver**: 1 (Replace/Augment Headcount)

**Pain Point**: 
Effective agency sales requires deep research — understanding the prospect's business, challenges, competitors, and decision-makers. This research is time-consuming and often shallow due to time pressure. Junior BizDev staff don't know what to look for; senior staff don't have time to do it.

**Solution**: 
monday.com prospect intelligence with AI-powered research. For each target company, automatically gather and synthesize relevant information. AI monitors news and triggers, suggests talking points, and identifies potential decision-makers.

**Vibe Prompt**:
```
Build a Prospect Intelligence app for agency business development teams.

Purpose: Systematically research and track target prospects with AI-powered intelligence gathering.

Key features:
- Target account board: Company name, Industry, Size, Priority tier, Owner, Status (Research/Outreach/Engaged/Opportunity)
- AI research profile: Auto-populated company overview, Recent news, Key executives, Marketing activities, Competitive landscape
- Stakeholder mapping: Key contacts, Roles, LinkedIn profiles, Relationship history
- Trigger monitoring: AI monitors for news, job changes, campaign launches, agency reviews — alerts when relevant
- Talking points generator: AI suggests personalized talking points based on company research
- Competitor watch: Track prospect's competitors and their agency relationships
- Engagement history: All touchpoints logged (emails, meetings, events)
- Dashboard: Accounts by tier, Research status, Recent triggers, Engagement activity

Include automations:
- When account added, AI generates initial research profile
- When trigger detected (news, agency review, key hire), alert owner
- When no engagement in 30 days, suggest outreach approaches
- Weekly intelligence digest: Key triggers across target accounts
- When opportunity created, link to research profile
```

**Outcome**: 
- Better research with less effort
- Proactive awareness of opportunities (triggers)
- More personalized, effective outreach
- Systematic approach to account targeting

**Discovery Questions**:
- "How much time does your team spend on prospect research? Is it thorough or rushed?"
- "How do you find out about agency reviews or opportunities in the market?"
- "When you reach out to a prospect, how personalized is your approach?"

**Industry-Specific Context**: 
"Agency review" = when a client is evaluating new agencies (major trigger). Trade publications (AdAge, Campaign, etc.) report reviews. LinkedIn is primary research tool for contacts. "Stakeholder mapping" = identifying all decision-makers and influencers.

---

### 5. Outbound Prospecting & Outreach
**Relevance**: Medium-High  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
Most agencies know they should do more proactive outreach but struggle to execute consistently. Cold outreach is uncomfortable, time-consuming, and often ineffective. When it is done, there's no system — random emails sent from personal inboxes with no tracking or follow-up.

**Solution**: 
monday.com outreach sequences integrated with prospect intelligence. Plan and execute personalized outreach campaigns, track responses, and manage follow-up systematically. AI helps personalize messages at scale.

**Vibe Prompt**:
```
Build an Outbound Prospecting app for agency business development teams.

Purpose: Plan, execute, and track outbound outreach campaigns with AI-powered personalization.

Key features:
- Campaign board: Campaign name, Target list, Theme/hook, Status (Planning/Active/Paused/Complete), Owner
- Target selection: Pull from prospect database by criteria, or upload list
- Sequence design: Multi-touch sequences (Email 1 → LinkedIn → Email 2 → Call), Timing between touches
- AI message drafting: Generate personalized outreach based on prospect research profile
- Message templates: Library of proven templates by industry/persona
- Execution tracking: Each prospect's status in sequence, Opens, Replies, Meetings booked
- Response handling: When reply received, categorize (Interested/Not Now/Not Interested) and route appropriately
- Performance analytics: Response rates by campaign, by message, by persona
- Dashboard: Active campaigns, Contacts in sequence, Response rates, Meetings booked, Pipeline generated

Include automations:
- When prospect added to campaign, generate personalized message for review
- When positive reply received, create opportunity and notify owner
- When sequence complete with no response, flag for alternative approach
- Weekly campaign performance report
- A/B test tracking for message variations
```

**Outcome**: 
- Consistent outbound activity (not feast-or-famine)
- Higher response rates through personalization
- Clear visibility into what's working
- Pipeline generation beyond RFPs and referrals

**Discovery Questions**:
- "How much of your new business comes from proactive outreach vs. inbound?"
- "When you do outbound, is it systematic or ad hoc?"
- "What's your response rate on cold outreach? Do you know?"

**Industry-Specific Context**: 
Agency outreach is typically relationship-focused, not transactional. Events, content, and thought leadership warm up cold outreach. "Always be helping" > "always be closing" for agency sales. LinkedIn is the primary channel.

---

### 6. Win/Loss Analysis & Learning
**Relevance**: Medium  
**Value Driver**: 3 (Scale Without Overhead)

**Pain Point**: 
When pitches end, the learning usually doesn't happen. Wins are celebrated; losses are forgotten. The patterns of why the agency wins and loses — pricing? capabilities? chemistry? — remain hidden. The same mistakes are repeated.

**Solution**: 
monday.com win/loss system that captures and analyzes outcomes. For every pitch, document the outcome and reasons. Over time, build a learning database that reveals patterns and improves future performance.

**Vibe Prompt**:
```
Build a Win/Loss Analysis app for agency business development and leadership.

Purpose: Systematically capture and analyze pitch outcomes to improve win rates.

Key features:
- Outcome capture: When opportunity closes, record Won/Lost, Primary reason, Secondary factors, Competitor (if known), Decision maker, Feedback verbatim
- Reason taxonomy: Pricing, Capabilities, Chemistry, Experience, Creative approach, References, Existing relationship, Timing
- Client debrief: Track whether debrief was requested, completed, key learnings
- Pattern analysis: AI identifies trends across wins and losses (e.g., "60% of losses cite pricing")
- Competitor tracking: How often do we win/lose against specific competitors?
- Recommendations: AI suggests improvements based on patterns
- Learning repository: Searchable database of all outcomes with learnings
- Dashboard: Win rate trends, Loss reasons breakdown, Competitor performance, Industry patterns, Learnings summary

Include automations:
- When opportunity closed, prompt for win/loss analysis (required before close)
- When loss recorded, schedule client debrief request
- Quarterly win/loss review: Generate summary report with patterns
- When pattern identified (e.g., repeated loss reason), alert leadership
- Annual win/loss presentation auto-generated
```

**Outcome**: 
- Systematic learning from every outcome
- Visibility into why you win and lose
- Actionable insights to improve win rate
- Reduced repetition of mistakes

**Discovery Questions**:
- "When you lose a pitch, do you know exactly why? Is it documented?"
- "What's your biggest reason for losing pitches? Are you sure?"
- "Do you see patterns across wins and losses, or is every outcome a surprise?"

**Industry-Specific Context**: 
Post-pitch debriefs from clients are valuable but rare; must be requested. "Competitive intelligence" includes knowing which agencies you tend to beat vs. lose to. Win rates vary widely by pitch type (RFP vs. referral vs. proactive).

---

## Industry Terminology Glossary

**RFP (Request for Proposal)** — Formal solicitation from a client seeking agency proposals; often competitive with multiple agencies invited.

**RFI (Request for Information)** — Preliminary inquiry to gather information before issuing an RFP; often used to narrow a long list.

**Chemistry Meeting** — Meeting to assess interpersonal and cultural fit between client and agency teams.

**Pitch** — Formal presentation of agency capabilities and approach to a prospective client.

**Credentials / Creds Deck** — Presentation showcasing agency experience, capabilities, and team.

**AOR (Agency of Record)** — Primary ongoing agency relationship; typically includes broad scope and retainer.

**Project Basis** — One-time engagement for specific scope; lower commitment than AOR.

**Spec Creative** — Speculative creative work produced during a pitch process (not all agencies do this).

**Procurement** — Client's purchasing function; often involved in RFP process and negotiation.

**MSA (Master Service Agreement)** — Overarching contract governing agency-client relationship.

---

## Typical Stakeholder Roles

**Primary Buyer: VP/Director of New Business**
- Title: VP Business Development, Director of New Business, Chief Growth Officer
- Concerns: Pipeline visibility, win rate improvement, team efficiency, forecast accuracy
- Decision driver: "Can I win more with the same team?"

**Technical Evaluator: BizDev Manager / Pitch Lead**
- Title: New Business Manager, Pitch Manager, BD Manager
- Concerns: Ease of use, research capabilities, time savings, integration with existing tools
- Decision driver: "Will this actually help me prepare better pitches faster?"

**Executive Sponsor: CEO / President**
- Title: CEO, President, Managing Director
- Concerns: Revenue growth, competitive positioning, client acquisition cost
- Decision driver: "Will we grow faster and win more premium clients?"

**Client Services Stakeholder: Account Leadership**
- Title: Group Account Director, Managing Director (Client Service)
- Concerns: Pitch team coordination, transition from pitch to account, cross-sell opportunities
- Decision driver: "Will this improve how we pitch and onboard new clients?"

**End Users:**
- BizDev team, Pitch teams (rotating cast), Account directors, Agency leadership

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Marketing** | Content for outreach, case studies, events | Marketing automation integration |
| **Account Services** | Expansion opportunities, referrals, case study input | Client relationship management |
| **Creative** | Pitch creative, spec work, case study assets | Creative workflow integration |
| **Operations** | Pitch resource allocation, project scoping | Resource management |
| **Strategy** | Pitch strategy, prospect research | Strategic planning tools |
| **Finance** | Pricing, profitability, revenue forecasting | Financial management |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| CRM | HubSpot, Salesforce, Pipedrive | Replace (especially for SMB/MM agencies) |
| Pitch Management | Notion, Google Docs, Spreadsheets | Full replacement |
| Research | LinkedIn Sales Navigator, ZoomInfo | Integrate; AI assistance augments |
| Outreach | Outreach.io, Salesloft, Lemlist | Replace or integrate |
| Case Studies | Notion, Sharepoint, scattered docs | Full replacement |

**Positioning:**
- **vs. Salesforce**: "Salesforce is built for product sales with short cycles and clear stages. Agency sales is different — longer cycles, relationship-driven, pitch-centric. You need a system that fits how agency sales actually works, not a generic CRM you'll never fully adopt."
- **vs. HubSpot**: "HubSpot is great for inbound-focused businesses. Agency BizDev is outbound, relationship-driven, and pitch-intensive. You need research tools, pitch management, and case study assembly that HubSpot doesn't offer."
- **vs. Spreadsheets**: "Your pipeline in a spreadsheet is invisible to leadership, impossible to forecast from, and loses all context when people leave. A real system compounds your learning over time."

---

## Common Objections

**Objection**: "We're a relationship business. Systems can't capture what we do."

**Response**: "Of course relationships matter. But relationships don't mean invisible processes. What happens to pipeline knowledge when your top BizDev person leaves? How do you know which relationships are actually turning into opportunities? A system captures and preserves relationship intelligence — it doesn't replace relationships."

---

**Objection**: "We don't do enough pitches to need a system."

**Response**: "That's the problem. You probably should be doing more proactive business development, but you don't have the infrastructure to support it. A system isn't just for managing what you do today — it's for scaling what you could do tomorrow."

---

**Objection**: "Our team won't use a CRM — we've tried."

**Response**: "Most CRMs fail in agencies because they're built for product sales. Nobody wants to fill in fields that don't matter. monday.com is different — it's flexible, so you design it for how you actually work. Plus, AI reduces the admin burden. What if the system worked for your team instead of against them?"

---

*Playbook Version: 1.0*  
*Industry: Advertising & Marketing*  
*Department: Sales*  
*Last Updated: 2026-02-11*
