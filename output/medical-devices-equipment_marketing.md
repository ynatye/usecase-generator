# Medical Devices & Equipment × Marketing Playbook

## Overview

Marketing in the medical devices and equipment industry operates within one of the most regulated and complex environments in healthcare. Marketing teams at medical device companies range from 15-75 professionals at mid-market companies ($100M-$1B revenue) to 200+ at enterprise organizations like Medtronic, Boston Scientific, or Abbott. These teams must navigate stringent FDA promotional guidelines, including fair balance requirements that mandate presenting both benefits and risks in marketing materials.

Marketing departments work closely with Medical/Legal/Regulatory (MLR) teams to ensure all promotional content undergoes rigorous review before publication. Every claim must be substantiated with clinical evidence, often requiring coordination with clinical affairs teams. The marketing process is uniquely complex due to the intersection of clinical evidence, regulatory compliance, and commercial objectives.

The department structure typically includes brand managers for specific product lines, digital marketing specialists who understand healthcare compliance, clinical marketing professionals who translate complex clinical data into compelling narratives, and field marketing teams who support trade shows like MEDICA, RSNA, and HIMSS. Success depends on managing long product development cycles (often 3-7 years), coordinating product launches with FDA clearance timing (510(k) or PMA), and building relationships with key opinion leaders (KOLs) and healthcare professionals (HCPs).

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|-------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | **High** | MLR review processes, competitive intelligence gathering, and clinical evidence synthesis require significant manual effort. AI agents can work 24/7 monitoring regulatory updates, analyzing competitor launches, and pre-reviewing content for compliance. |
| **Consolidate Tech Stack with AI** | **High** | Medical device marketing teams typically juggle 8-12 disparate systems: CRM (Salesforce), MLR review platforms, clinical trial databases, regulatory databases, marketing automation, trade show management, KOL management systems, and publication tracking tools. |
| **Scale Impact Without Overhead** | **Medium** | Long approval cycles and regulatory complexity limit how quickly teams can scale. However, once processes are optimized, teams can manage larger product portfolios and enter new markets without proportional headcount increases. |

## Prioritized Use Cases

---

### Use Case 1: MLR Review Process Automation

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
MLR (Medical/Legal/Regulatory) review cycles average 4-6 weeks for promotional materials, creating bottlenecks for product launches and campaign execution. Marketing teams spend 30-40% of their time managing review iterations, tracking approval status, and ensuring fair balance compliance. A single promotional piece might go through 8-12 review cycles with legal, regulatory, and clinical teams before approval. The manual process of ensuring FDA promotional guideline compliance across hundreds of materials annually consumes significant resources and delays time-to-market for critical campaigns.

#### The Solution
monday.com Work Management creates a unified MLR review workflow with automated routing, deadline tracking, and compliance checkpoints. Vibe can rapidly build custom review boards for different material types (sales aids, website content, trade show materials). AI agents can pre-screen content for common compliance issues, flag potential fair balance violations, and automatically route materials based on risk level and content type.

#### The Outcome
Reduce MLR review cycle time by 40-50% (from 6 weeks to 3-4 weeks). Eliminate 70% of manual status tracking and follow-up emails. Reduce compliance risk by standardizing review processes. Free up marketing team capacity equivalent to 2-3 FTE who can focus on strategic initiatives rather than process management.

#### Discovery Questions
1. "How many promotional materials do you put through MLR review annually, and what's your average cycle time?"
2. "What percentage of your marketing team's time is spent managing the review process versus creating content?"
3. "How do you currently ensure fair balance requirements are met across all your promotional materials?"
4. "What happens when FDA guidance changes - how quickly can you identify and update affected materials?"
5. "How do you track and measure the cost of delayed product launches due to MLR review bottlenecks?"

#### Industry Context
MLR review is the backbone of compliant medical device marketing. Teams must understand that any promotional claim requires clinical evidence substantiation and that fair balance (presenting risks alongside benefits) is mandatory for most promotional materials. The FDA's guidance on promotional materials is constantly evolving, requiring marketing teams to stay current on regulatory changes while managing complex approval workflows.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an MLR review management board with these columns: Material Name (text), Material Type (dropdown: Sales Aid, Website Content, Trade Show Material, Press Release, White Paper, Video Script), Submission Date (date), Review Stage (status: Submitted, Medical Review, Legal Review, Regulatory Review, Revision Required, Final Approval, Approved), Assigned Reviewer (people), Priority Level (dropdown: Routine, Urgent, Launch Critical), Fair Balance Required (checkbox), Clinical Evidence Referenced (text), Target Approval Date (date), Days in Review (formula), and Comments (long text). Add automation to notify the Marketing Manager when an item moves to 'Revision Required' and send reminder emails when reviews are overdue by 3 days. Create a Kanban view by Review Stage and a Timeline view showing all materials by Target Approval Date."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MLR Compliance Guardian

**Agent Purpose:**  
Automates pre-screening of promotional materials for FDA compliance issues and manages the MLR review workflow.

**Triggers:**
- New promotional material uploaded
- MLR review stage changes
- FDA guidance updates published
- Review deadline approaching (3 days prior)
- Material revision submitted

**Actions:**
- Scan content for potential fair balance violations
- Route materials to appropriate reviewers based on content type and risk level
- Generate compliance checklists specific to material type
- Send automated reminder notifications for overdue reviews
- Flag materials that may require clinical evidence updates
- Create summary reports of review bottlenecks for management

**Data Required:**
- FDA promotional guidelines database
- Historical MLR review patterns
- Clinical evidence repository
- Reviewer workload and availability
- Material classification taxonomy

**Autonomy Level:** Human-in-the-Loop
Pre-screening and routing happen automatically, but final compliance decisions require human review. Agent escalates complex or high-risk materials to senior reviewers.

**Example Interaction:**
> Marketing Manager Sarah uploads a new sales aid for the company's latest cardiac catheter. The MLR Compliance Guardian immediately scans the content and flags three potential issues: a benefit claim that may require additional clinical evidence, missing risk information for fair balance, and language that could be interpreted as off-label promotion. The agent automatically routes the material to Dr. Martinez in Medical Review (bypassing the usual queue since it's marked "Launch Critical"), generates a pre-review checklist highlighting the flagged issues, and schedules a follow-up reminder for 5 days. When Dr. Martinez approves the medical aspects but requests risk language updates, the agent notifies Sarah with specific guidance on FDA-compliant risk presentation and automatically moves the item to "Revision Required" with clear next steps.

---

### Use Case 2: KOL (Key Opinion Leader) Relationship Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Medical device companies maintain relationships with hundreds of KOLs across different therapeutic areas, tracking consulting agreements, speaking engagements, clinical trial participation, and publication collaborations. These relationships are managed across disconnected systems: Salesforce for basic contact info, separate databases for clinical trial investigators, legal systems for contract management, and manual spreadsheets for engagement tracking. Teams struggle to get a 360-degree view of KOL relationships, leading to compliance risks, missed collaboration opportunities, and inefficient resource allocation. Tracking publication strategies and clinical evidence generation from KOL partnerships requires manual coordination across multiple departments.

#### The Solution
monday.com consolidates all KOL management into a unified platform with integrated CRM capabilities. Connect KOL profiles with clinical trial databases, publication tracking, and compliance monitoring. AI agents can analyze KOL publication patterns, identify collaboration opportunities, and monitor compliance with industry guidelines around HCP engagement. Automated workflows ensure proper legal review of all KOL agreements and track disclosure requirements.

#### The Outcome
Increase KOL engagement effectiveness by 35% through better relationship visibility and coordination. Reduce compliance risks by centralizing disclosure tracking and automated alerts. Accelerate clinical evidence generation by identifying optimal KOL partnerships 3x faster. Eliminate duplicate contracting efforts that previously cost an estimated $200K annually in redundant legal fees.

#### Discovery Questions
1. "How many KOLs do you currently work with across your product portfolio, and how do you track the ROI of these relationships?"
2. "What systems are you using to manage KOL contracts, speaking engagements, and clinical trial participation?"
3. "How do you currently identify new KOL partnership opportunities, especially for emerging therapeutic areas?"
4. "What challenges do you face with disclosure requirements and compliance tracking for HCP relationships?"
5. "How effectively can you connect KOL insights back to your clinical evidence strategy and publication planning?"

#### Industry Context
KOL management is critical for medical device companies to build clinical evidence, gain regulatory insights, and establish market credibility. These relationships must comply with strict anti-kickback statutes and industry codes of conduct. KOLs serve multiple roles: clinical advisors, trial investigators, speakers, and advocates. Effective KOL programs require tracking engagement value, ensuring fair market value compensation, and maintaining transparency in all interactions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a KOL relationship management board with these columns: KOL Name (text), Specialty/Expertise (dropdown: Cardiology, Orthopedics, Neurology, Radiology, Surgery, Other), Institution (text), Contact Information (text), Relationship Tier (status: Strategic, Core, Developing, Inactive), Current Engagements (dropdown: Advisory Board, Clinical Trial, Speaking, Consulting, Publication Collaboration), Contract Status (status: Active, Pending, Expired, No Contract), Annual Engagement Value (numbers), Last Interaction Date (date), Next Planned Interaction (date), Compliance Status (status: Compliant, Review Required, Issue Flagged), Key Therapeutic Areas (multi-select), and Publications This Year (numbers). Add automation to send alerts when contracts are within 60 days of expiration and notify the compliance team when Annual Engagement Value exceeds $25,000. Create a board view filtered by Relationship Tier and a Dashboard view showing engagement metrics by therapeutic area."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** KOL Intelligence Orchestrator

**Agent Purpose:**  
Optimizes KOL relationships by analyzing engagement patterns, identifying opportunities, and ensuring compliance.

**Triggers:**
- New KOL profile created
- Contract expiration approaching (90 days)
- Publication activity detected
- Compliance threshold exceeded
- Clinical trial enrollment milestone reached

**Actions:**
- Analyze KOL publication patterns to identify collaboration opportunities
- Monitor competitive intelligence regarding KOL activities
- Generate compliance alerts for disclosure requirements
- Suggest optimal KOLs for new clinical trials based on expertise and availability
- Track ROI metrics for KOL engagements
- Automate meeting scheduling and follow-up reminders

**Data Required:**
- PubMed publication database
- Clinical trial registries
- Compliance regulations and thresholds
- Historical engagement effectiveness data
- Competitor KOL mapping

**Autonomy Level:** Human-in-the-Loop
Agent identifies opportunities and flags compliance issues automatically but requires human approval for high-value engagements and contract modifications.

**Example Interaction:**
> The KOL Intelligence Orchestrator notices that Dr. Jennifer Chen, a leading interventional cardiologist, has published three papers in the past six months on minimally invasive cardiac procedures - an area where the company is developing a new device. The agent cross-references her current engagement level (listed as "Developing"), checks her availability by analyzing recent speaking patterns, and identifies she hasn't worked with any direct competitors in this specific therapeutic area. It automatically flags her as a "High Opportunity" candidate for the upcoming clinical advisory board, estimates the potential value of engagement based on her publication impact scores, and generates a briefing document highlighting her recent research relevance. The agent then notifies the KOL Manager with specific talking points for the next outreach and pre-populates a contract request form based on her preferred engagement patterns from past interactions.

---

### Use Case 3: Product Launch Coordination with Regulatory Timing

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Medical device product launches must align with complex regulatory approval timelines (510(k) clearance or PMA approval), clinical evidence generation, manufacturing scale-up, and market access activities. A typical product launch involves 50+ stakeholders across R&D, clinical affairs, regulatory, manufacturing, sales, marketing, and market access teams. The failure to coordinate these activities results in delayed launches, missed market opportunities, and inefficient resource allocation. When regulatory approval timing shifts (which happens in 60% of device launches), the cascade of required adjustments across all launch activities creates chaos and typically delays market entry by 3-6 months.

#### The Solution
monday.com Work Management creates a unified product launch command center that automatically adjusts all dependent activities when regulatory milestones shift. Integration with regulatory databases provides real-time updates on approval status. AI agents can predict potential regulatory delays based on historical patterns and proactively suggest timeline adjustments. Cross-functional workflows ensure all teams stay aligned as launch dates evolve.

#### The Outcome
Reduce average product launch delays from 4.5 months to 1.2 months when regulatory timing changes. Improve launch readiness by ensuring 95% of pre-launch activities are completed on time. Increase first-year product revenue by 25% through faster time-to-market. Enable marketing teams to manage 40% more product launches with the same headcount through improved process efficiency.

#### Discovery Questions
1. "What's your average time from FDA clearance to commercial launch, and how often do regulatory delays impact your go-to-market timeline?"
2. "How many product launches is your marketing team managing simultaneously, and what's your biggest bottleneck?"
3. "When regulatory approval timing shifts, how long does it take your team to adjust all dependent marketing activities?"
4. "What percentage of your launches meet the original projected first-year revenue targets?"
5. "How do you currently coordinate launch activities between marketing, clinical affairs, and regulatory teams?"

#### Industry Context
Medical device launches are uniquely complex due to regulatory dependencies. Unlike other industries, marketing teams cannot predict launch timing with certainty until FDA approval is received. Launch preparation must balance readiness with the risk of investing in marketing activities for products that may face regulatory delays. Success requires maintaining launch momentum while adapting to regulatory reality.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a product launch coordination board with these columns: Launch Activity (text), Product Line (dropdown: Cardiac Devices, Orthopedic Implants, Diagnostic Equipment, Surgical Instruments), Responsible Team (dropdown: Marketing, Clinical Affairs, Regulatory, Sales, Manufacturing, Market Access), Activity Status (status: Not Started, In Progress, Pending Approval, Completed, Blocked), Regulatory Dependency (checkbox), FDA Submission Type (dropdown: 510k, PMA, De Novo, Not Applicable), Planned Start Date (date), Planned Completion Date (date), Actual Completion Date (date), Days Behind Schedule (formula), Risk Level (status: Low, Medium, High, Critical), Budget Allocated (numbers), and Launch Priority Tier (dropdown: Tier 1, Tier 2, Tier 3). Add automation to notify all dependent activities when a regulatory milestone status changes and send escalation alerts when activities are more than 5 days behind schedule. Create a Timeline view showing all activities by product line and a Dashboard showing launch readiness by percentage complete."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Launch Timeline Optimizer

**Agent Purpose:**  
Orchestrates product launch activities and automatically adjusts timelines when regulatory milestones change.

**Triggers:**
- FDA submission status update received
- Regulatory milestone date changed
- Launch activity marked as blocked or delayed
- New regulatory guidance published affecting product category
- Manufacturing readiness status updated

**Actions:**
- Automatically adjust all dependent activity timelines when regulatory dates shift
- Identify critical path bottlenecks and suggest resource reallocation
- Generate launch readiness reports with risk assessments
- Notify stakeholders of timeline changes with impact analysis
- Predict potential regulatory delays based on submission patterns
- Optimize resource allocation across multiple concurrent launches

**Data Required:**
- Historical regulatory approval timelines
- FDA database integration for real-time status updates
- Resource capacity and availability across teams
- Critical path dependencies for launch activities
- Market opportunity data for prioritization

**Autonomy Level:** Escalation-Based
Agent automatically adjusts non-critical timelines and resource allocation but escalates significant delays or budget implications to launch management team.

**Example Interaction:**
> The Launch Timeline Optimizer receives an automated update from the FDA database indicating that the 510(k) submission for the company's new cardiac stent has received a "More Information Needed" response, potentially delaying approval by 6-8 weeks. Within minutes, the agent analyzes the impact across 47 dependent launch activities, automatically pushes back non-critical milestones like sales training and promotional material printing, but flags three critical activities that can't be delayed: trade show booth reservations for TCT (which has a deadline), KOL advisory board meetings that need to happen pre-launch, and competitive intelligence gathering that should align with the new timeline. The agent sends a prioritized alert to Launch Manager Mike with specific recommendations: expedite the regulatory response (potentially reducing delay to 4 weeks), negotiate extended booth reservation deadlines, and shift KOL meetings to focus on market preparation rather than launch timing. It also automatically updates budget forecasts showing the revenue impact of the delay and suggests reallocating Q4 marketing spend to two other products that can now capture the market opportunity window.

---

### Use Case 4: Trade Show and Event Management (MEDICA/RSNA/HIMSS)

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device companies participate in 15-25 major trade shows annually, including MEDICA, RSNA, HIMSS, ACC, and specialty conferences. Each event requires coordination across multiple teams: booth design, product demonstrations, literature management, KOL speaker coordination, lead capture, and post-event follow-up. The manual process of managing these events consumes 2-3 FTE across marketing, events, and sales teams. Post-event lead qualification and follow-up often takes 6-8 weeks, during which hot prospects go cold. ROI measurement is inconsistent, making it difficult to optimize event portfolio and resource allocation.

#### The Solution
monday.com centralizes all trade show management with integrated workflows for pre-event planning, on-site execution, and post-event follow-up. AI agents can automatically qualify leads based on booth interactions, prioritize follow-up activities, and analyze event ROI patterns. Integration with CRM ensures seamless lead handoff to sales teams with complete interaction context.

#### The Outcome
Reduce trade show management overhead by 60%, freeing up equivalent of 1.5 FTE for strategic marketing activities. Accelerate post-event lead follow-up from 6-8 weeks to 2-3 days. Improve lead qualification accuracy by 40% through consistent AI-powered scoring. Increase trade show ROI by 30% through better event selection and resource optimization.

#### Discovery Questions
1. "How many trade shows does your marketing team manage annually, and what's your process for measuring ROI?"
2. "How long does it typically take to follow up with leads after major events like HIMSS or MEDICA?"
3. "What percentage of your annual marketing budget goes to trade shows, and how do you decide which events to prioritize?"
4. "How do you currently coordinate booth logistics, product demos, and KOL speaking engagements across multiple events?"
5. "What's your biggest challenge in converting trade show leads into qualified sales opportunities?"

#### Industry Context
Medical device trade shows are relationship-heavy events where clinical evidence, regulatory status, and product demonstrations drive purchasing decisions. Shows like MEDICA (world's largest medical trade fair) or RSNA (radiology) are make-or-break opportunities for product visibility. Success requires coordinating complex logistics while ensuring clinical accuracy in all product demonstrations and literature.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a trade show management board with these columns: Event Name (text), Event Date (date), Event Type (dropdown: Major Industry Show, Specialty Conference, Regional Event, Clinical Symposium), Booth Size (dropdown: 10x10, 20x20, 40x40, Island, Theater), Event Status (status: Planning, Booth Confirmed, Materials Ready, On-Site, Complete, ROI Analysis), Products Featured (multi-select), Assigned Event Manager (people), Budget Allocated (numbers), Actual Spend (numbers), Estimated Leads (numbers), Actual Leads (numbers), Qualified Leads (numbers), KOL Speakers (people), Pre-Show Meetings Scheduled (numbers), Post-Show Follow-up Status (status: Not Started, In Progress, 50% Complete, 75% Complete, Complete), and Event ROI (formula). Add automation to send reminders 30 days before each event for final logistics check and notify the sales team when leads are imported. Create a Calendar view of all events and a Dashboard showing ROI metrics by event type."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Trade Show Intelligence Engine

**Agent Purpose:**  
Optimizes trade show performance through automated lead management, ROI analysis, and event coordination.

**Triggers:**
- New lead captured at trade show
- Event registration opens for target shows
- Booth interaction data uploaded
- Post-event survey responses received
- Competitor activity detected at shared events

**Actions:**
- Automatically score and qualify leads based on booth interaction patterns
- Generate personalized follow-up email sequences based on products viewed
- Analyze competitor booth traffic and messaging strategies
- Recommend optimal event portfolio based on historical ROI data
- Coordinate cross-team logistics and deliverable tracking
- Create post-event performance reports with actionable insights

**Data Required:**
- Historical event performance and ROI data
- Lead scoring criteria specific to medical device sales cycles
- Competitor intelligence and activity patterns
- Product demonstration effectiveness metrics
- KOL availability and speaking preferences

**Autonomy Level:** Fully Autonomous
Agent handles routine lead scoring, follow-up sequences, and logistics coordination autonomously, escalating only high-value leads or significant budget variances.

**Example Interaction:**
> During HIMSS 2026, the Trade Show Intelligence Engine processes real-time booth interaction data and notices that Dr. Sarah Williams, CIO at Regional Medical Center, spent 12 minutes at the AI diagnostic imaging demo, downloaded two clinical evidence papers, and asked specific questions about PACS integration. The agent immediately scores her as a "Hot Lead" (95/100), cross-references her organization's recent $50M capital equipment procurement announcement, and identifies this as a perfect match for the company's enterprise imaging portfolio. Within 30 minutes of her booth visit, the agent automatically sends her a personalized follow-up email with case studies from similar health systems, schedules a suggested demo call in her calendar based on her preferred meeting times (scraped from her LinkedIn activity patterns), and alerts Account Manager James with a pre-written briefing that includes her specific technical questions, organizational context, and recommended talking points. The agent also flags that Regional Medical Center will be at two other trade shows this year where additional touchpoints could be valuable.

---

### Use Case 5: Clinical Evidence Marketing and Publication Strategy

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Medical device marketing teams must translate complex clinical trial data into compelling marketing messages while maintaining scientific accuracy and regulatory compliance. Clinical evidence is scattered across trial databases, publication tracking systems, regulatory submissions, and KOL research. Marketing teams struggle to identify which studies support specific marketing claims, track competitive clinical evidence, and coordinate with clinical affairs on publication strategies. The process of developing evidence-based marketing materials takes 8-12 weeks per campaign, with significant back-and-forth between marketing, clinical, and regulatory teams.

#### The Solution
monday.com creates a unified clinical evidence hub that connects trial data, publications, regulatory submissions, and marketing claims. AI agents can automatically monitor new publications, analyze competitive clinical evidence, and suggest marketing messages based on available data. Integration with PubMed and clinical trial registries provides real-time updates on relevant research.

#### The Outcome
Reduce evidence-based marketing material development time by 50% through centralized data access. Improve claim substantiation accuracy by 40% with automated evidence tracking. Increase marketing team's clinical literature review capacity by 3x through AI-powered analysis. Accelerate competitive response time from weeks to days when competitor clinical data becomes available.

#### Discovery Questions
1. "How do you currently track and organize clinical evidence to support your marketing claims?"
2. "What's your process for staying current on competitive clinical trial results and publications?"
3. "How long does it take to develop marketing materials that require clinical evidence substantiation?"
4. "How effectively can your marketing team interpret clinical data without constantly involving clinical affairs?"
5. "What percentage of your marketing claims require revision during MLR review due to evidence gaps?"

#### Industry Context
Clinical evidence is the foundation of all medical device marketing. Every promotional claim must be substantiated with peer-reviewed data, clinical trial results, or regulatory submissions. Marketing teams must understand statistical significance, clinical endpoints, and study design to create credible materials. The ability to quickly access and interpret clinical evidence directly impacts competitive positioning and campaign effectiveness.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a clinical evidence marketing board with these columns: Study/Publication Title (text), Study Type (dropdown: RCT, Case Series, Registry Study, Meta-Analysis, Real-World Evidence), Publication Status (status: Planning, Ongoing, Under Review, Published, Rejected), Publication Date (date), Journal Name (text), Primary Endpoint Met (checkbox), Statistical Significance (text), Marketing Claims Supported (long text), Competitive Relevance (dropdown: High, Medium, Low, None), Evidence Quality (status: Level 1, Level 2, Level 3, Not Suitable), MLR Approval Status (status: Not Required, Pending, Approved, Rejected), Supporting Materials Created (multi-select: Sales Aid, Website Content, Press Release, Conference Abstract), Responsible Clinical Lead (people), Marketing Lead (people), and Evidence Score (numbers). Add automation to notify the marketing team when new publications are marked as 'Published' and send alerts when competitive studies are marked as high relevance. Create a filtered view showing only published studies with marketing claims and a Dashboard tracking evidence pipeline by therapeutic area."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Clinical Evidence Synthesizer

**Agent Purpose:**  
Monitors, analyzes, and synthesizes clinical evidence to support marketing claims and competitive positioning.

**Triggers:**
- New publication detected in PubMed for relevant keywords
- Clinical trial results published for competitive products
- Marketing claim requiring evidence substantiation
- FDA guidance updates affecting clinical evidence standards
- KOL publishes research on relevant topics

**Actions:**
- Automatically screen new publications for marketing relevance
- Extract key clinical endpoints and statistical significance data
- Generate suggested marketing language based on study results
- Flag competitive clinical advantages or threats
- Create evidence summary briefs for marketing campaigns
- Monitor clinical trial registries for emerging competitive threats

**Data Required:**
- PubMed publication database access
- Clinical trial registry monitoring
- Competitive product intelligence
- FDA guidance on promotional claims
- Historical marketing claim performance

**Autonomy Level:** Human-in-the-Loop
Agent identifies and analyzes clinical evidence autonomously but requires human approval before suggesting marketing claims or flagging competitive threats.

**Example Interaction:**
> The Clinical Evidence Synthesizer monitors PubMed and detects a new randomized controlled trial published in JACC comparing minimally invasive cardiac procedures - directly relevant to the company's new transcatheter valve system. The agent automatically downloads the study, extracts key findings (30% reduction in procedure time, 15% fewer complications, 98% success rate), and cross-references these results with the company's clinical trial data. It identifies three potential marketing claims that could be substantiated by this external validation, generates draft language for each claim with appropriate statistical context, and flags that this study provides strong competitive differentiation against Boston Scientific's competing device (which showed only 8% reduction in complications in their pivotal trial). The agent creates a clinical evidence brief for Marketing Director Lisa, highlighting that this external validation could strengthen the upcoming European launch campaign and suggests prioritizing this evidence in KOL presentations at the upcoming EuroPCR conference. It also automatically schedules the study for MLR review and creates template sales aids incorporating the new evidence.

---

### Use Case 6: Sales Enablement Material Management and IFU Alignment

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Medical device sales teams require extensive training materials, clinical evidence summaries, competitive battle cards, and product specifications. These materials must align precisely with Instructions for Use (IFU) and regulatory labeling requirements. Marketing teams spend 25-30% of their time creating, updating, and managing sales enablement materials across multiple product lines. When regulatory labeling changes or new clinical evidence becomes available, updating all affected sales materials is a manual process that can take 6-8 weeks. Sales teams often use outdated materials, creating compliance risks and missed sales opportunities.

#### The Solution
monday.com centralizes all sales enablement materials with automated version control and IFU alignment tracking. AI agents can automatically identify when materials need updates based on regulatory changes or new clinical evidence. Integration with training platforms ensures sales teams always have access to current, compliant materials.

#### The Outcome
Reduce sales enablement material management time by 60%, freeing up marketing capacity for strategic initiatives. Decrease material update cycles from 6-8 weeks to 1-2 weeks. Improve sales team compliance by ensuring 98% of materials are current and aligned with IFU requirements. Increase sales team effectiveness through faster access to relevant, up-to-date clinical evidence.

#### Discovery Questions
1. "How many different sales enablement materials do you currently manage across your product portfolio?"
2. "What's your process for ensuring all sales materials remain aligned with IFU requirements when regulations change?"
3. "How do you currently distribute material updates to your global sales team?"
4. "What percentage of sales team questions could be answered with better access to current clinical evidence and competitive intelligence?"
5. "How do you measure the effectiveness of your sales enablement materials in driving revenue?"

#### Industry Context
IFU (Instructions for Use) alignment is critical for medical device sales materials. Any deviation between marketing materials and regulatory labeling creates compliance risks. Sales teams need both clinical depth and competitive intelligence to succeed in complex B2B healthcare sales cycles that often involve multiple stakeholders and long decision timelines.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a sales enablement material management board with these columns: Material Name (text), Material Type (dropdown: Sales Aid, Battle Card, Clinical Summary, Product Specification, Training Module, Case Study, ROI Calculator), Product Line (multi-select), Current Version (text), IFU Alignment Status (status: Aligned, Review Required, Out of Date, Not Applicable), Last Updated Date (date), Next Review Date (date), Responsible Marketing Manager (people), Clinical Review Required (checkbox), MLR Approval Status (status: Current, Expired, Not Required), Usage Analytics (numbers), Sales Team Rating (status: Excellent, Good, Needs Improvement, Not Rated), Distribution Status (status: Available, Pending Update, Withdrawn), and Download Count Last 30 Days (numbers). Add automation to send alerts when materials are 30 days past review date and notify sales teams when new materials are available. Create a Dashboard showing material usage by product line and a filtered view of materials requiring urgent updates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Sales Enablement Optimizer

**Agent Purpose:**  
Maintains current, compliant sales enablement materials and optimizes content based on usage patterns and effectiveness.

**Triggers:**
- IFU or regulatory labeling update received
- New clinical evidence published affecting product claims
- Sales team feedback submitted on material effectiveness
- Material download patterns indicate outdated content usage
- Competitive intelligence update requires battle card revision

**Actions:**
- Automatically flag materials requiring updates when regulations change
- Generate updated content suggestions based on new clinical evidence
- Analyze material usage patterns to identify gaps and opportunities
- Create personalized material recommendations for individual sales reps
- Monitor sales team questions to identify content needs
- Track material effectiveness correlation with sales outcomes

**Data Required:**
- IFU and regulatory labeling database
- Sales team usage analytics and feedback
- Clinical evidence repository
- Competitive intelligence updates
- Sales performance data by material type

**Autonomy Level:** Human-in-the-Loop
Agent identifies update needs and creates draft content automatically, but requires marketing approval before distributing updated materials to sales teams.

**Example Interaction:**
> The Sales Enablement Optimizer detects that the FDA has updated the 510(k) clearance language for the company's orthopedic spine system, requiring changes to promotional claims about surgical approach options. The agent immediately scans all sales enablement materials and identifies 12 items that reference the affected claims: 3 sales aids, 4 competitive battle cards, 2 clinical summaries, and 3 ROI calculators. It automatically flags these materials as "IFU Review Required" and generates specific revision recommendations for each, highlighting exactly which language needs updating and suggesting FDA-compliant alternatives based on the new clearance language. The agent then analyzes sales team usage data and prioritizes the updates based on download frequency - the orthopedic battle card used by 45 reps gets priority over the ROI calculator downloaded only 6 times last quarter. It sends Marketing Manager Jennifer a prioritized update plan with estimated effort for each material and suggests temporarily withdrawing the most problematic materials while updates are in progress. The agent also proactively creates a brief for the sales team explaining the regulatory change and how it affects their conversations with surgeons.

---

### Use Case 7: Digital Marketing Compliance and Social Media Management

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Medical device companies face unique challenges in digital marketing due to FDA regulations on social media, search advertising restrictions, and requirements for fair balance in online content. Marketing teams must navigate complex compliance requirements across LinkedIn, medical professional networks, conference websites, and digital advertising platforms. Content must be tailored for different audiences (HCPs vs. patients vs. investors) with appropriate risk/benefit information for each. Manual review and approval of digital content creates bottlenecks that slow campaign execution and reduce marketing agility in fast-moving digital channels.

#### The Solution
monday.com creates a unified digital marketing compliance platform with automated content review workflows and audience-specific approval processes. AI agents can pre-screen content for compliance issues, suggest fair balance language, and optimize content for different digital channels while maintaining regulatory requirements.

#### The Outcome
Reduce digital content approval cycles by 50% while maintaining compliance standards. Increase digital campaign launch speed by 3x through streamlined approval workflows. Improve social media engagement by 40% through better content optimization and audience targeting. Eliminate compliance violations in digital channels through automated screening and approval processes.

#### Discovery Questions
1. "What digital marketing channels do you currently use, and how do you ensure FDA compliance across platforms?"
2. "How long does it take to get approval for social media content or digital advertising campaigns?"
3. "What's your process for ensuring appropriate risk/benefit information in digital content for different audiences?"
4. "How do you currently measure the effectiveness of digital marketing while maintaining compliance requirements?"
5. "What percentage of your digital marketing efforts are delayed by compliance review processes?"

#### Industry Context
Digital marketing in medical devices requires balancing promotional effectiveness with regulatory compliance. Social media regulations are particularly complex, with different requirements for professional vs. patient audiences. The FDA's guidance on digital marketing continues to evolve, requiring marketing teams to stay current while maintaining compliant promotional strategies.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a digital marketing compliance board with these columns: Content Title (text), Content Type (dropdown: Social Media Post, Blog Article, Email Campaign, Digital Ad, Video Script, Webinar Content), Platform (multi-select: LinkedIn, Twitter, YouTube, Company Website, Medical News Sites), Target Audience (dropdown: HCP, Patients, Investors, General Public), Content Status (status: Draft, Compliance Review, MLR Review, Approved, Published, Rejected), Fair Balance Required (checkbox), Risk Information Included (checkbox), Clinical Claims Made (checkbox), Publication Date (date), Engagement Metrics (numbers), Compliance Risk Level (dropdown: Low, Medium, High), Responsible Content Creator (people), Approval Date (date), and Review Comments (long text). Add automation to notify compliance team when high-risk content is submitted and send alerts when published content needs periodic review. Create a Calendar view of all scheduled content and a Dashboard showing compliance metrics by platform."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Digital Compliance Navigator

**Agent Purpose:**  
Ensures all digital marketing content meets FDA compliance requirements while optimizing for audience engagement.

**Triggers:**
- New digital content submitted for review
- FDA guidance updates affecting digital marketing
- Social media engagement patterns indicate compliance concerns
- Content scheduled for publication approaching deadline
- Competitive digital activity detected requiring response

**Actions:**
- Pre-screen content for FDA compliance issues and fair balance requirements
- Generate audience-appropriate risk/benefit language suggestions
- Optimize content for platform algorithms while maintaining compliance
- Monitor published content for engagement patterns indicating potential issues
- Create compliance reports for regulatory review
- Suggest content improvements based on performance and compliance metrics

**Data Required:**
- Current FDA guidance on digital marketing and social media
- Audience segmentation and compliance requirements by platform
- Historical content performance and compliance correlation
- Competitive digital marketing intelligence
- Platform-specific algorithm and engagement data

**Autonomy Level:** Human-in-the-Loop
Agent provides automated compliance screening and optimization suggestions but requires human approval before publishing any content making medical claims.

**Example Interaction:**
> Marketing Specialist David submits a LinkedIn post announcing the company's new minimally invasive surgical robot, targeting orthopedic surgeons. The Digital Compliance Navigator immediately analyzes the content and flags two issues: the phrase "revolutionary outcomes" may require clinical evidence substantiation, and the post lacks appropriate fair balance information for HCP audiences. The agent suggests specific language modifications: replacing "revolutionary" with "clinically proven" (referencing the pivotal trial data), and adds a compliant risk statement appropriate for LinkedIn's character limits. It also generates three audience-optimized versions: one for surgeons (emphasizing clinical outcomes), one for hospital administrators (focusing on efficiency and ROI), and one for medical device industry professionals (highlighting technological innovation). The agent pre-populates the MLR review form with relevant clinical evidence citations and estimated reach metrics, then schedules the post for publication pending approval. When the post goes live, it continuously monitors engagement and alerts the team if comments require regulatory-compliant responses.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **510(k) Clearance** | FDA pathway for medical devices substantially equivalent to existing devices |
| **PMA (Premarket Approval)** | FDA's most stringent regulatory pathway for high-risk medical devices |
| **MLR Review** | Medical/Legal/Regulatory review process ensuring promotional compliance |
| **Fair Balance** | FDA requirement to present both benefits and risks in promotional materials |
| **KOL (Key Opinion Leader)** | Influential healthcare professionals who shape clinical practice |
| **HCP (Healthcare Professional)** | Doctors, nurses, and other clinical practitioners |
| **IFU (Instructions for Use)** | Official device labeling that must align with all promotional materials |
| **Claims Substantiation** | Clinical evidence required to support any promotional claim |
| **GPO/IDN** | Group Purchasing Organization/Integrated Delivery Network |
| **HEOR** | Health Economics Outcomes Research - data supporting value propositions |
| **CPT/HCPCS Codes** | Billing codes that affect reimbursement and market access |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **CMO/VP Marketing** | Strategic marketing direction, P&L responsibility | High - budget and strategy decisions |
| **Brand Manager** | Product-specific marketing campaigns and positioning | Medium - tactical execution |
| **Clinical Marketing Manager** | Clinical evidence translation and KOL relationships | Medium - clinical credibility |
| **Digital Marketing Manager** | Online channels, social media, digital advertising | Low - execution within compliance |
| **Field Marketing Manager** | Trade shows, regional events, sales support | Low - tactical support |
| **MLR Committee** | Promotional material compliance review | High - approval authority |
| **Clinical Affairs Director** | Clinical evidence generation and regulatory strategy | High - data and compliance |
| **Sales Leadership** | Revenue targets and market feedback | High - end customer influence |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Clinical Affairs** | Clinical evidence translation, trial planning | Joint AI agents for evidence management |
| **Regulatory Affairs** | Compliance review, submission coordination | Shared workflows for approval processes |
| **Sales** | Enablement materials, lead qualification | Integrated CRM and marketing automation |
| **Medical Affairs** | KOL relationships, scientific communications | Unified KOL management platform |
| **Market Access** | Reimbursement strategy, health economics | Shared value proposition development |
| **R&D** | Product development insights, clinical needs | Product launch coordination workflows |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Salesforce** | "CRM leader but lacks clinical evidence integration" | monday.com's unified clinical-commercial platform |
| **Veeva** | "Life sciences specific but expensive and rigid" | monday.com's flexibility and cost advantage |
| **Marketo** | "Marketing automation without regulatory compliance" | Built-in MLR workflows and compliance |
| **Concur/SAP** | "Complex enterprise systems requiring IT resources" | No-code simplicity with enterprise governance |
| **Custom Tools** | "Fragmented point solutions creating silos" | Unified platform eliminating data disconnection |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"We need life sciences-specific features"** | "monday.com's flexibility allows us to build medical device-specific workflows while maintaining the agility to adapt as regulations evolve. Our Vibe capability lets you create exactly what you need without vendor lock-in." |
| **"Regulatory compliance is too complex"** | "That's exactly why you need a platform that can adapt. Our MLR workflow templates and AI compliance screening provide structure while allowing customization for your specific regulatory requirements." |
| **"We already have Veeva/Salesforce"** | "The question isn't whether your current tools work - it's whether they're preparing you for the AI-driven future. monday.com doesn't just manage your processes; our AI agents do the work, giving you competitive advantage." |
| **"Clinical evidence management is too specialized"** | "Clinical evidence is data, and managing data is what monday.com excels at. Our platform connects your clinical data with marketing execution in ways specialized tools can't match." |

## Proof Points
*(To be populated with customer references)*

- Medical device company reduced MLR review cycles by 45% with automated compliance workflows
- Fortune 500 medical device manufacturer consolidated 8 marketing tools into monday.com platform
- European medical device company improved product launch coordination, reducing delays by 3.2 months average
- Orthopedic device company increased trade show ROI by 35% through AI-powered lead scoring and follow-up

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*