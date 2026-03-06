# Broadcasting × Sales Playbook

## Overview

Broadcasting sales teams operate in a complex, fast-paced environment managing both traditional linear TV/radio advertising and rapidly growing digital revenue streams. These teams typically range from 15-50 people at local stations to 200+ at major networks, structured around upfront/scatter market cycles, local vs national sales divisions, and increasingly, cross-platform digital teams. The sales organization must navigate audience guarantees, make-goods, inventory management across multiple dayparts and platforms, while managing rate cards that fluctuate based on CPM/CPP pricing models.

The regulatory environment requires compliance with FCC guidelines, especially around political ad sales requirements for equal time and disclosure. Broadcasting sales teams face intense pressure to monetize shrinking linear audiences while building new digital revenue streams, managing programmatic advertising demands, and creating compelling sponsorship packages that span traditional broadcast and digital properties. Success hinges on maximizing revenue per available minute while maintaining advertiser relationships through challenging audience measurement transitions and fragmented viewing habits.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|-------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | ✅ **HIGH** | Traffic coordinators, proposal generators, and make-good managers can be largely automated. AI agents can handle routine advertiser communications, inventory optimization, and compliance tracking 24/7. |
| **Consolidate Tech Stack with AI** | ✅ **HIGH** | Broadcasting sales teams juggle 8-12 disconnected tools: traffic systems, CRM, Nielsen data, programmatic platforms, billing systems, and proposal generators. One AI platform can replace most while adding intelligence. |
| **Scale Impact Without Overhead** | ✅ **MEDIUM** | During high-demand periods (elections, upfronts), teams need to process 3-5x normal volume without proportional staffing increases. AI agents enable this scaling. |

## Prioritized Use Cases

---

### Use Case 1: Automated Traffic Order Processing & Optimization

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Traffic coordinators spend 60-70% of their time manually processing advertiser changes, checking inventory conflicts, and optimizing spot placement across dayparts. A single political advertising surge can create 200+ daily change orders, each requiring manual verification against FCC compliance rules and existing advertiser conflicts. This creates bottlenecks, errors in billing, and missed revenue opportunities when premium inventory goes unsold due to processing delays.

#### The Solution
monday AI Agents automatically process traffic orders, check inventory availability in real-time, optimize spot placement based on CPM targets and audience delivery goals, and flag compliance issues before they become problems. The system integrates with existing traffic software while adding intelligent automation and conflict resolution. Sidekick provides instant answers on inventory availability and suggests optimal placement strategies.

#### The Outcome
- 75% reduction in traffic coordinator manual workload
- 40% faster order processing during high-volume periods
- 25% improvement in inventory utilization through AI optimization
- Eliminate $50K+ annual make-good costs from placement errors

#### Discovery Questions
- "How many traffic coordinators do you have, and what percentage of their time is spent on manual order processing versus strategic optimization?"
- "During political seasons or upfronts, how does your team handle the 3-5x increase in daily change orders?"
- "What's your current make-good rate, and how often are placement errors causing revenue clawbacks?"
- "How quickly can you provide inventory availability responses to agency requests?"
- "What happens when your traffic system goes down during a high-volume period?"

#### Industry Context
Traffic operations are the nerve center of broadcasting sales, managing the complex intersection of inventory, pricing, and advertiser requirements. Traffic coordinators typically earn $45-65K annually, making automation highly cost-effective. During political seasons, stations can see daily order volume increase by 400-500%, creating serious operational strain.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a traffic order management board with columns: Order ID (text), Advertiser (text), Agency (text), Campaign Name (text), Flight Dates (date range), Daypart (dropdown: Morning Drive, Midday, Afternoon Drive, Prime Time, Late Night, Weekend), Spots Per Week (numbers), Rate (currency), Total Value (formula: spots × weeks × rate), Status (status: New, Processing, Approved, Conflicts, On-Air, Complete), Traffic Coordinator (people), Priority Level (dropdown: Standard, Rush, Political), Compliance Notes (long text), Make-Good Required (checkbox). Add automations to notify traffic team when new orders arrive, alert managers for orders over $10K, and create follow-up tasks when conflicts are detected. Include a Kanban view by Status, Timeline view for flight scheduling, and Dashboard view showing weekly revenue pipeline and conflict resolution metrics."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Traffic Flow Optimizer

**Agent Purpose:**  
Automatically process, validate, and optimize traffic orders while ensuring compliance and maximizing revenue.

**Triggers:**
- New traffic order submission via integration or form
- Inventory changes from programming department
- Advertiser modification requests
- Political filing deadline approaches
- Make-good request initiated

**Actions:**
- Validate order details against inventory availability
- Check for advertiser conflicts and separation requirements
- Optimize spot placement based on CPM/CPP targets
- Generate compliance documentation for political ads
- Create make-good recommendations when delivery falls short
- Update traffic system with approved placements

**Data Required:**
- Real-time inventory from traffic system
- Rate card data and pricing rules
- Advertiser category conflicts matrix
- FCC political advertising requirements
- Historical performance data for optimization

**Autonomy Level:** Human-in-the-Loop  
Agent automatically processes standard orders and optimizes placement, but escalates high-value orders (>$25K), political ads, or orders with complex conflicts to traffic managers for final approval.

**Example Interaction:**
> A major automotive advertiser submits a $75K flight for the upcoming month with specific daypart requirements. The Traffic Flow Optimizer immediately checks inventory across all requested dayparts, identifies that Tuesday 6-7pm slots conflict with an existing auto advertiser (separation rules), and automatically suggests alternative high-performing slots in the same daypart. It calculates that shifting 3 spots to Wednesday 6-7pm actually improves projected delivery by 12% based on historical audience data. The agent flags this for human review due to the high dollar value, sends a notification to the traffic manager with optimization recommendations, and prepares the conflict resolution documentation. Within 10 minutes of submission, the advertiser receives a counter-proposal that maintains their goals while maximizing station revenue and compliance.

---

---

### Use Case 2: Intelligent Upfront & Scatter Proposal Generation

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Account executives spend 15-20 hours per week creating advertiser proposals, pulling data from Nielsen, rate cards, competitive analysis, and historical performance across multiple systems. During upfront season, this becomes unmanageable with 50-100 proposals needed weekly. Proposals often lack real-time pricing optimization, competitive insights, and cross-platform bundle opportunities, resulting in 30-40% lower win rates and extended sales cycles.

#### The Solution
AI agents automatically generate sophisticated proposals by pulling real-time audience data, analyzing competitive positioning, optimizing cross-platform bundles, and calculating the most competitive CPM/CPP pricing. The system learns from won/lost feedback to improve proposal quality over time. Vibe creates custom proposal templates for different advertiser categories, while Sidekick helps AEs customize messaging and positioning in real-time during client meetings.

#### The Outcome
- 80% reduction in proposal preparation time
- 45% improvement in upfront proposal win rates
- 60% faster turnaround on scatter market responses
- $200K+ annual revenue increase from better cross-platform bundling

#### Discovery Questions
- "How long does it take your AEs to create a comprehensive upfront proposal, and what systems do they have to pull from?"
- "What percentage of your upfront proposals include cross-platform digital components, and how do you price those bundles?"
- "How quickly can you respond to scatter market opportunities, especially when agencies need same-day turnaround?"
- "Do your AEs have real-time access to competitive pricing intelligence when building proposals?"
- "What's your current proposal-to-close ratio in upfront vs scatter markets?"

#### Industry Context
Upfront season (typically May-July for broadcast, earlier for cable) represents 60-75% of annual revenue for most broadcasters. AEs need to create compelling proposals that demonstrate audience reach, competitive value, and cross-platform amplification. Scatter market operates year-round with much shorter decision cycles, requiring rapid response capabilities.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an upfront proposal tracker with columns: Proposal ID (text), Advertiser (text), Agency (text), Campaign Budget (currency), Target Demo (dropdown: Adults 18-49, Adults 25-54, Women 18-34, Men 18-49, Adults 35-64), Proposal Value (currency), Win Probability (dropdown: 25%, 50%, 75%, 90%), Status (status: Draft, Submitted, Under Review, Negotiating, Won, Lost), AE Owner (people), Submission Date (date), Decision Deadline (date), Cross-Platform Bundle (checkbox), Digital Component Value (currency), Competitive Threats (text), Next Steps (text). Add automations to alert AEs 3 days before deadlines, notify sales managers for proposals over $100K, and create follow-up tasks for lost opportunities. Include Kanban view by Status, Calendar view for deadlines, and Dashboard showing proposal pipeline value, win rates by AE, and cross-platform attachment rates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Proposal Intelligence Engine

**Agent Purpose:**  
Generate data-driven, competitive proposals optimized for upfront and scatter market opportunities.

**Triggers:**
- RFP received from agency or direct advertiser
- Competitive intelligence update detected
- New inventory becomes available for target demo
- Pricing strategy changes approved
- Follow-up deadline for pending proposal reached

**Actions:**
- Analyze RFP requirements and match to available inventory
- Generate pricing recommendations based on market conditions
- Create cross-platform bundle suggestions
- Pull competitive analysis and positioning
- Generate customized presentation materials
- Calculate audience delivery projections

**Data Required:**
- Real-time Nielsen or audience measurement data
- Current rate cards and pricing flexibility rules
- Competitive pricing intelligence
- Historical win/loss data by advertiser category
- Digital inventory and performance metrics
- Cross-platform audience overlap data

**Autonomy Level:** Human-in-the-Loop  
Agent generates complete proposal drafts with pricing and positioning recommendations, but AEs review and customize messaging before client presentation. Fully autonomous for standard scatter market responses under $25K.

**Example Interaction:**
> A major retail chain's agency sends an RFP for a $500K upfront buy targeting women 25-54 during morning and evening dayparts. The Proposal Intelligence Engine immediately analyzes the request, identifies that this advertiser typically responds well to lifestyle programming contexts, and discovers that two competitors are also likely bidding based on recent market activity. The agent generates a proposal featuring a cross-platform bundle that includes traditional morning show placements, targeted digital video placements, and a social media amplification component. It calculates that bundling digital at 20% of the linear buy creates a compelling CPM story while increasing total proposal value. The system flags that this advertiser has historically valued audience quality over pure reach, so it emphasizes affluent viewer composition and shopping behavior data. Within 30 minutes, the AE has a complete proposal draft with competitive positioning, pricing rationale, and custom presentation slides ready for review and customization.

---

---

### Use Case 3: Political Ad Sales Compliance & Revenue Optimization

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Political advertising creates complex compliance requirements around equal time, lowest unit rates, and disclosure documentation. Managing political inventory separately from commercial inventory while maximizing revenue requires constant manual oversight. During election cycles, stations can receive 100+ political requests daily, each requiring compliance validation, rate verification, and inventory coordination. Non-compliance penalties can reach $500K+ per violation, making manual processes extremely risky.

#### The Solution
AI agents automatically validate political advertising requests against FCC requirements, calculate correct lowest unit rates, manage equal time obligations, and optimize political inventory placement to maximize revenue while maintaining compliance. The system generates all required documentation, tracks disclosure requirements, and alerts managers to potential compliance issues before they occur.

#### The Outcome
- 90% reduction in compliance violations and associated penalties
- 35% improvement in political advertising revenue through better inventory optimization
- 70% reduction in manual compliance documentation time
- Eliminate $200K+ annual compliance consulting costs

#### Discovery Questions
- "How do you currently manage political advertising compliance, and how many people are dedicated to this during election cycles?"
- "What's your process for calculating and validating lowest unit rates for political advertisers?"
- "How do you track and manage equal time obligations when candidates request access?"
- "Have you ever faced FCC compliance issues or penalties related to political advertising?"
- "How do you balance maximizing political revenue with maintaining commercial advertiser relationships?"

#### Industry Context
Political advertising represents 10-40% of annual revenue in election years for many broadcasters, especially local stations. FCC compliance is non-negotiable, with detailed record-keeping requirements and public file obligations. Political advertisers have rights to lowest unit rates and reasonable access that can disrupt commercial inventory management.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a political advertising compliance tracker with columns: Request ID (text), Candidate/Organization (text), Office Sought (text), Request Date (date), Flight Dates (date range), Requested Spots (numbers), Rate Class Offered (dropdown: LUR Class 1, LUR Class 2, LUR Class 3, Fixed), Rate Per Spot (currency), Total Value (formula), Equal Time Triggered (checkbox), Compliance Status (status: Under Review, Approved, Rejected, Documentation Pending), Reason for Rejection (text), Documentation Complete (checkbox), Public File Updated (checkbox), Sales Rep (people). Add automations to alert compliance manager when political requests are received, notify general manager for any rejections, and create deadline reminders for public file updates. Include Calendar view for flight dates, Dashboard for political revenue tracking and compliance metrics, and Kanban view by compliance status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Political Compliance Guardian

**Agent Purpose:**  
Ensure FCC compliance while optimizing political advertising revenue and managing equal time obligations.

**Triggers:**
- Political advertising request received
- Equal time request submitted
- New political candidate filing detected
- Rate class changes affecting political pricing
- Public file update deadline approaching

**Actions:**
- Validate political advertiser eligibility and classification
- Calculate correct lowest unit rates for requested time periods
- Check for equal time implications and notify affected candidates
- Generate required compliance documentation
- Update public inspection files automatically
- Optimize placement to maximize revenue within compliance rules

**Data Required:**
- Current rate cards and commercial pricing by class
- Political advertising request history
- Equal time tracking database
- FCC compliance rule database
- Public file management system integration
- Candidate filing information

**Autonomy Level:** Escalation-Based  
Agent handles routine compliance validation and documentation automatically but escalates any equal time triggers, unusual requests, or potential compliance issues to the compliance manager for review.

**Example Interaction:**
> A mayoral candidate submits a request for 20 spots during morning drive time, two weeks before the election. The Political Compliance Guardian immediately calculates the lowest unit rate based on commercial rates paid during the same time period, determines this triggers equal time obligations for the three other declared mayoral candidates, and generates notices that must be sent within 7 days. The agent checks that the candidate's committee is properly registered, validates the ad content meets disclosure requirements, and prepares all documentation for the public file. It flags that granting this request would bump a commercial advertiser who paid a higher rate, calculating the revenue impact at $3,200. The system notifies the compliance manager and sales manager simultaneously, providing a complete analysis and recommended response within minutes of receiving the request. The agent also proactively generates equal time notices for the other candidates and schedules public file updates to maintain compliance.

---

---

### Use Case 4: Cross-Platform Audience & Revenue Analytics

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Sales teams struggle to provide unified analytics across linear TV, digital video, streaming, radio, and social platforms. Agencies demand cross-platform audience deduplication, reach curves, and attribution analysis, but data lives in separate silos requiring manual aggregation. Creating comprehensive post-campaign reports takes 8-12 hours per campaign, limiting the team's ability to handle larger advertiser portfolios and provide strategic insights that command premium pricing.

#### The Solution
AI agents automatically aggregate audience data across all platforms, perform deduplication analysis, calculate true cross-platform reach, and generate sophisticated attribution reports. The system learns advertiser preferences for reporting formats and automatically delivers customized insights. Sidekick enables sales teams to answer complex audience questions instantly during client meetings, while automated reporting increases portfolio capacity without adding headcount.

#### The Outcome
- 85% reduction in post-campaign reporting time
- 50% increase in advertiser portfolio capacity per AE
- 30% improvement in cross-platform upsell attachment rates
- $300K+ incremental revenue from data-driven optimization insights

#### Discovery Questions
- "How long does it take to produce a comprehensive post-campaign report that includes all your platforms?"
- "Can you currently provide deduplicated reach analysis across linear and digital for your advertisers?"
- "What percentage of your campaigns include cross-platform components, and how do you measure incremental reach?"
- "How do agencies respond when you can't provide unified attribution analysis across all touchpoints?"
- "What insights could you provide to advertisers if you had real-time cross-platform performance data?"

#### Industry Context
Cross-platform measurement is becoming table stakes as advertisers demand proof of incremental reach and attribution. Nielsen's measurement evolution and the rise of streaming viewership require broadcasters to provide unified analytics or lose business to digital-native competitors who excel at data presentation.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a cross-platform campaign analytics dashboard with columns: Campaign Name (text), Advertiser (text), Flight Dates (date range), Linear TV Impressions (numbers), Digital Video Impressions (numbers), Streaming Impressions (numbers), Radio Impressions (numbers), Social Impressions (numbers), Total Gross Impressions (formula), Deduplicated Reach (numbers), Frequency (numbers), Cross-Platform Lift (percentage), Linear CPM (currency), Digital CPM (currency), Blended CPM (formula), Campaign Value (currency), Report Status (status: In Progress, Ready for Review, Delivered, Needs Follow-up), Account Executive (people), Next Report Due (date). Add automations to alert AEs when campaigns complete and reports are ready, notify managers for campaigns over $50K, and schedule follow-up meetings based on performance. Include Dashboard view with reach/frequency charts, Timeline view for campaign scheduling, and performance comparison views by platform mix."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Cross-Platform Intelligence Hub

**Agent Purpose:**  
Aggregate, analyze, and report unified audience metrics across all advertising platforms.

**Triggers:**
- Campaign flight dates complete
- New audience data available from measurement partners
- Advertiser requests custom analysis
- Performance threshold alerts triggered
- Scheduled reporting deadline reached

**Actions:**
- Aggregate impression and audience data from all platforms
- Perform cross-platform deduplication analysis
- Calculate reach, frequency, and incremental lift metrics
- Generate automated performance reports and insights
- Create optimization recommendations for future campaigns
- Update advertiser performance databases

**Data Required:**
- Linear TV audience measurement (Nielsen, Comscore)
- Digital video analytics (DFP, programmatic platforms)
- Streaming platform performance data
- Radio measurement data
- Social media analytics and insights
- Advertiser campaign goals and KPIs

**Autonomy Level:** Fully Autonomous  
Agent automatically generates and delivers standard performance reports, but escalates campaigns with unusual performance patterns or significant optimization opportunities to account teams for strategic follow-up.

**Example Interaction:**
> A regional automotive dealer's month-long campaign across TV, digital, and radio just completed. The Cross-Platform Intelligence Hub automatically pulls performance data from all measurement sources, performs deduplication analysis showing that the campaign reached 68% of the target market with an average frequency of 4.2 - exceeding the 65% reach goal. The agent discovers that streaming video placements drove 23% higher website visit rates compared to linear TV, and radio provided critical frequency building at 40% lower cost per point. It generates a comprehensive report showing $47,000 in campaign value delivered a 4.8x ROAS based on tracked vehicle sales, and recommends shifting 15% more budget to streaming components in future flights. The report is automatically formatted to match the dealer's preferred style, includes competitive benchmarking data, and is delivered within 2 hours of campaign completion. The agent also schedules a follow-up meeting and prepares talking points for the AE about optimization opportunities for the next quarter's campaigns.

---

---

### Use Case 5: Programmatic Advertising Integration & Yield Optimization

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Managing programmatic advertising alongside direct sales creates inventory conflicts, pricing inconsistencies, and revenue optimization challenges. Sales teams often don't have real-time visibility into programmatic performance, leading to underselling premium inventory or creating conflicts with guaranteed advertisers. Manual floor price adjustments and yield optimization require constant attention but lack data-driven insights, leaving 15-25% revenue on the table.

#### The Solution
AI agents continuously optimize programmatic floors based on demand patterns, audience quality, and direct sales inventory requirements. The system automatically adjusts pricing and availability to maximize total revenue across both direct and programmatic channels while preventing conflicts with guaranteed campaigns. Real-time dashboards give sales teams programmatic insights to inform direct sales conversations.

#### The Outcome
- 20% improvement in programmatic revenue through dynamic optimization
- 95% reduction in inventory conflicts between direct and programmatic sales
- 40% improvement in programmatic fill rates during premium dayparts
- Save 10+ hours weekly on manual programmatic management

#### Discovery Questions
- "What percentage of your inventory is currently available for programmatic advertising?"
- "How do you manage potential conflicts between programmatic and directly sold campaigns?"
- "Do your AEs have visibility into programmatic performance when planning direct sales campaigns?"
- "How often do you adjust programmatic floor prices, and what data drives those decisions?"
- "What's your current programmatic fill rate during your most valuable dayparts?"

#### Industry Context
Programmatic advertising represents 15-30% of digital revenue for most broadcasters, with growing pressure to include premium inventory. Balancing programmatic yield with direct sales relationships requires sophisticated inventory management and pricing strategies that many stations handle manually.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a programmatic yield optimization tracker with columns: Date (date), Daypart (dropdown: Early Morning, Morning Drive, Midday, Afternoon Drive, Prime Access, Prime Time, Late Night), Available Inventory (numbers), Programmatic Floor Price (currency), Fill Rate (percentage), Average Winning CPM (currency), Revenue Generated (currency), Direct Sales Conflicts (numbers), Yield Index vs Target (percentage), Optimization Action (dropdown: Increase Floor, Decrease Floor, Hold Price, Block Inventory), Performance vs Yesterday (percentage), Account Manager (people). Add automations to alert when fill rates drop below 85%, notify managers when floors need adjustment, and create daily performance summaries. Include Dashboard view with yield trends and performance metrics, Calendar view for optimization scheduling, and comparison charts for direct vs programmatic performance."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Programmatic Yield Maximizer

**Agent Purpose:**  
Optimize programmatic advertising revenue while preventing conflicts with direct sales inventory.

**Triggers:**
- Programmatic auction performance data updated
- Direct sales campaign booked affecting available inventory
- Fill rate drops below performance thresholds
- Competitive pricing intelligence updates
- New premium inventory becomes available

**Actions:**
- Adjust programmatic floor prices based on demand patterns
- Block or release inventory based on direct sales priority
- Optimize audience targeting parameters for better yields
- Generate performance reports and optimization recommendations
- Alert sales teams to programmatic opportunities
- Update inventory availability across all sales channels

**Data Required:**
- Real-time programmatic auction data and performance
- Direct sales inventory commitments and priorities
- Audience measurement and quality metrics
- Competitive programmatic pricing intelligence
- Historical performance and optimization results

**Autonomy Level:** Fully Autonomous  
Agent continuously optimizes programmatic settings within approved parameters, but escalates significant pricing changes or inventory decisions to sales managers when direct sales implications exceed $10K in potential impact.

**Example Interaction:**
> During morning drive time, the Programmatic Yield Maximizer detects that demand for automotive advertising has increased 40% compared to last week, with CPMs averaging $12 higher than current floor prices. The agent analyzes direct sales commitments and confirms that 60% of morning drive inventory remains available for programmatic after fulfilling guaranteed campaigns. It automatically increases floor prices by 15% for automotive categories while maintaining current pricing for other verticals. Within 30 minutes, programmatic revenue increases 28% with fill rates maintaining at 92%. The agent notices this pattern coincides with a major auto show announcement and proactively suggests to the sales team that similar adjustments be made for evening drive inventory. It also flags this trend for the automotive account executive, suggesting outreach to local dealers about premium inventory availability at competitive programmatic rates. The optimization generates an additional $3,400 in revenue that day while maintaining all direct sales commitments.

---

---

### Use Case 6: Make-Good Management & Audience Guarantee Tracking

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Tracking audience delivery against guarantees across hundreds of active campaigns requires constant manual monitoring and reconciliation. When campaigns under-deliver, creating appropriate make-goods that satisfy advertisers while minimizing revenue impact takes significant time and expertise. Many stations react to delivery issues too late, requiring expensive make-goods that could have been prevented with proactive optimization during the campaign flight.

#### The Solution
AI agents continuously monitor campaign delivery against audience guarantees, automatically identify under-delivery risks before campaigns complete, and generate optimal make-good solutions when needed. The system proactively suggests campaign optimizations to prevent shortfalls and learns from historical make-good patterns to improve future campaign planning and inventory allocation.

#### The Outcome
- 60% reduction in make-good costs through proactive optimization
- 90% faster make-good proposal generation and approval
- 35% improvement in advertiser satisfaction scores
- Eliminate 15+ hours weekly of manual delivery tracking

#### Discovery Questions
- "What percentage of your campaigns require make-goods, and what's the average cost impact?"
- "How quickly can you identify when a campaign is tracking behind delivery guarantees?"
- "What's your process for determining appropriate make-good inventory and pricing?"
- "How often do delivery issues surprise you at the end of a campaign flight?"
- "Do you have visibility into delivery pacing issues across all your active campaigns simultaneously?"

#### Industry Context
Audience guarantees are fundamental to broadcasting sales, with most campaigns including delivery commitments that must be met or made good. Make-goods typically cost 15-30% more than the original inventory value due to premium placement requirements and inventory constraints.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a campaign delivery monitoring board with columns: Campaign Name (text), Advertiser (text), Flight Dates (date range), Guaranteed Impressions (numbers), Delivered Impressions (numbers), Delivery Percentage (formula: delivered/guaranteed*100), Pacing Status (status: On Track, At Risk, Behind, Over-Delivered), Days Remaining (formula), Required Daily Delivery (formula), Make-Good Required (checkbox), Make-Good Value (currency), Proposed Solution (long text), Approval Status (status: Pending, Approved, Rejected), Account Executive (people), Traffic Coordinator (people), Next Review Date (date). Add automations to alert AEs when campaigns fall below 90% delivery pace, notify traffic when make-goods are approved, and escalate to managers for high-value make-goods. Include Dashboard view with delivery performance metrics, Timeline view for campaign pacing, and alerts for at-risk campaigns."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Delivery Guardian

**Agent Purpose:**  
Monitor campaign delivery performance and proactively prevent under-delivery through optimization and make-good management.

**Triggers:**
- Daily delivery data updated from traffic system
- Campaign pacing falls below target thresholds
- Campaign flight completes requiring final reconciliation
- Make-good inventory becomes available
- Advertiser delivery inquiry received

**Actions:**
- Calculate delivery pacing against guaranteed impressions
- Identify campaigns at risk of under-delivery
- Generate proactive optimization recommendations
- Create make-good proposals with optimal inventory selection
- Update delivery tracking and reconciliation reports
- Notify stakeholders of delivery status and actions needed

**Data Required:**
- Real-time campaign delivery data from traffic systems
- Audience measurement data for delivered impressions
- Available make-good inventory across all dayparts
- Historical make-good costs and advertiser preferences
- Campaign guarantee terms and delivery requirements

**Autonomy Level:** Human-in-the-Loop  
Agent automatically tracks delivery and generates optimization recommendations, but requires human approval for make-good proposals over $5K or campaign modifications affecting other advertisers.

**Example Interaction:**
> A major restaurant chain's $85K campaign is tracking at 87% delivery pace with 6 days remaining in the flight. The Delivery Guardian identifies that maintaining current pacing would result in 8% under-delivery, requiring approximately $12,000 in make-good inventory. The agent analyzes available spots and discovers that shifting 4 remaining spots from afternoon drive to morning drive would improve delivery efficiency by 15% due to stronger audience performance, potentially eliminating the shortfall. It also identifies that weekend breakfast programming has over-performed for this advertiser category, suggesting 3 additional weekend spots could close any remaining gap at minimal cost. The agent generates a proposal showing both the optimization plan and a backup make-good package using premium morning inventory, calculates the cost impact of each approach, and alerts the account executive with recommendations. The proactive intervention prevents the under-delivery, maintains the advertiser relationship, and saves $12,000 in make-good costs while actually improving overall campaign performance.

---

---

### Use Case 7: Sponsorship Package Development & Management

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Creating comprehensive sponsorship packages that span multiple platforms, events, and content streams requires coordinating across programming, digital, events, and sales teams. Package development is often manual and reactive, missing opportunities to create premium offerings that command higher CPMs. Tracking sponsorship performance and ROI across multiple touchpoints lacks standardization, making renewal conversations difficult and pricing optimization challenging.

#### The Solution
AI agents analyze content calendars, audience data, and advertiser preferences to automatically generate compelling sponsorship packages. The system tracks performance across all sponsorship elements, provides real-time ROI analysis, and suggests package optimizations for renewals. Vibe creates standardized sponsorship tracking and billing workflows, while automated reporting demonstrates value to sponsors throughout the partnership.

#### The Outcome
- 45% increase in sponsorship package values through better optimization
- 70% faster package development and proposal creation
- 80% improvement in sponsorship renewal rates through better performance tracking
- Create 2-3x more sponsorship opportunities per sales person

#### Discovery Questions
- "What percentage of your revenue comes from sponsorship packages versus traditional spot advertising?"
- "How long does it take to develop a comprehensive sponsorship package proposal?"
- "Do you have standardized processes for tracking and reporting sponsorship performance?"
- "How effectively can you demonstrate ROI to sponsors across all package elements?"
- "What prevents you from creating more premium sponsorship opportunities?"

#### Industry Context
Sponsorship packages typically command 20-40% premium CPMs compared to spot advertising and create stronger advertiser relationships. Successful packages integrate content, digital, events, and social elements but require significant coordination and tracking to execute effectively.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a sponsorship package management board with columns: Package Name (text), Sponsor (text), Package Value (currency), Start Date (date), End Date (date), Package Type (dropdown: Event, Content Series, Seasonal, Sports, News), Linear Components (text), Digital Components (text), Event Components (text), Social Components (text), Performance Metrics (text), Package Status (status: Development, Proposed, Negotiating, Active, Complete), Renewal Probability (dropdown: 25%, 50%, 75%, 90%), Account Executive (people), Next Milestone (date), ROI Delivered (percentage). Add automations to alert AEs 30 days before package end dates, notify managers for packages over $50K, and create renewal discussion tasks. Include Timeline view for package scheduling, Dashboard for performance metrics and renewal pipeline, and Kanban view by package status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Sponsorship Architect

**Agent Purpose:**  
Design, optimize, and track comprehensive sponsorship packages that maximize advertiser value and revenue.

**Triggers:**
- New sponsorship inquiry received
- Content programming schedule updated
- Event calendar changes affecting packages
- Sponsorship performance metrics available
- Renewal deadline approaching

**Actions:**
- Analyze advertiser objectives and match to available opportunities
- Generate comprehensive package proposals with multiple touchpoints
- Track performance across all package elements
- Calculate ROI and prepare performance reports
- Identify upsell and renewal opportunities
- Optimize package components based on performance data

**Data Required:**
- Content programming schedules and audience projections
- Event calendar and attendance/viewership data
- Digital platform analytics and engagement metrics
- Sponsor objectives and success metrics
- Historical sponsorship performance data

**Autonomy Level:** Human-in-the-Loop  
Agent generates package concepts and tracks performance automatically, but requires sales team input for final package design and sponsor relationship management.

**Example Interaction:**
> A regional healthcare system expresses interest in wellness-focused sponsorship opportunities. The Sponsorship Architect analyzes the content calendar and identifies a perfect alignment: the morning show's health segment, weekend wellness programming, digital health content, and the upcoming community health fair. The agent designs a 6-month package including title sponsorship of morning health segments (3x/week), branded content integration in weekend programming, sponsored articles on the website, social media promotion, and premium presence at the health fair. It calculates audience reach across all components showing 89% coverage of adults 35-64 in the market, with an estimated 24 branded touchpoints per viewer. The system generates performance tracking for website engagement, social metrics, event attendance, and audience delivery, projecting an integrated campaign value of $125K with clear ROI measurement. The agent prepares presentation materials highlighting the healthcare system's community leadership positioning and creates a custom reporting dashboard that will track performance monthly, automatically generating renewal discussions based on achieved metrics.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **Upfront** | Annual advance selling period (typically May-July) where 60-75% of inventory is sold at guaranteed rates |
| **Scatter Market** | Year-round inventory sales outside of upfront commitments, typically at higher rates with shorter lead times |
| **CPM/CPP** | Cost Per Thousand impressions / Cost Per Point - standard broadcast pricing metrics |
| **Make-Goods** | Free advertising provided when campaigns under-deliver on guaranteed audience levels |
| **Daypart** | Programming time segments (Morning Drive, Prime Time, etc.) with distinct audience characteristics and pricing |
| **Rate Card** | Published pricing structure by daypart, season, and audience demographic |
| **Traffic Orders** | Scheduling instructions for when and how often advertisements should air |
| **Inventory Management** | Process of allocating available commercial time across advertisers and revenue opportunities |
| **Cross-Platform Bundles** | Advertising packages that span multiple channels (linear TV, digital, radio, streaming) |
| **Programmatic Advertising** | Automated buying and selling of advertising inventory through technology platforms |
| **Audience Guarantees** | Contractual commitments to deliver specific audience levels or provide make-goods |
| **Political Ad Sales** | Advertising sales to political candidates with special FCC compliance requirements |
| **LUR (Lowest Unit Rate)** | FCC requirement that political advertisers receive the lowest rate charged to commercial advertisers |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **General Sales Manager** | Overall sales strategy, team management, revenue accountability | High - Final decision maker |
| **Local Sales Manager** | Direct sales team, local advertiser relationships, inventory allocation | High - Day-to-day operations |
| **National Sales Manager** | Agency relationships, network/national advertiser sales | High - Large revenue deals |
| **Account Executives** | Direct advertiser relationships, proposal development, campaign management | Medium - Revenue generation |
| **Traffic Manager** | Inventory management, order processing, compliance, scheduling | Medium - Operations critical |
| **Research Director** | Audience measurement, competitive analysis, market insights | Medium - Data and insights |
| **Digital Sales Manager** | Cross-platform packages, programmatic advertising, digital revenue | Growing - Future revenue |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Programming** | Content scheduling affects inventory and audience delivery | Real-time coordination for better yield optimization |
| **News** | Breaking news creates inventory disruptions and opportunities | Automated alerts for high-value inventory changes |
| **Promotions** | Marketing campaigns require coordination with sales packages | Integrated campaign tracking and performance |
| **Engineering** | Technical capabilities affect digital/streaming revenue potential | Cross-platform technical integration opportunities |
| **Accounting** | Billing, reconciliation, and revenue recognition processes | Automated billing and make-good processing |
| **Legal/Compliance** | Political advertising, FCC requirements, contract terms | Automated compliance monitoring and documentation |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|--------------------------|
| **WideOrbit** | Industry-standard traffic and sales system | Complement with AI layer rather than replace |
| **Matrix/Marketron** | Sales CRM and proposal tools | Replace with unified AI-driven proposal generation |
| **Nielsen** | Audience measurement and analytics | Enhance with cross-platform unification and insights |
| **Salesforce** | Generic CRM adapted for broadcasting | Replace with industry-specific AI solutions |
| **Excel/Manual Processes** | Proposal creation, reporting, tracking | Complete replacement with automated workflows |
| **Programmatic Platforms** | Google DFP, The Trade Desk, etc. | Integrate and optimize rather than replace |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"Our traffic system integration is too complex"** | "We integrate with existing systems rather than replace them - adding an AI layer that enhances WideOrbit/Matrix without disrupting operations." |
| **"Political advertising compliance is too specialized"** | "Our AI agents are specifically trained on FCC political advertising requirements and can ensure compliance better than manual processes." |
| **"We need industry-specific features not generic tools"** | "Our platform adapts to broadcasting workflows - from daypart optimization to make-good management to cross-platform bundling." |
| **"ROI is hard to measure in media sales"** | "We track specific metrics: time saved per proposal, make-good cost reduction, compliance violation prevention, and revenue optimization gains." |
| **"Our sales team won't adopt new technology"** | "The AI does the heavy lifting behind the scenes - AEs see better proposals faster, not more complexity in their daily workflow." |
| **"Upfront season timing is too critical to risk"** | "Implementation includes parallel testing during scatter periods, with full deployment after upfront validation." |

## Proof Points
*(To be populated with customer references)*

- [ ] Local broadcaster reducing political compliance violations by 90%
- [ ] Network achieving 45% improvement in upfront proposal win rates
- [ ] Regional group saving $200K annually in make-good costs through predictive optimization
- [ ] Station increasing cross-platform attachment rates by 60% with automated bundling
- [ ] Broadcasting company scaling sales capacity 3x without additional headcount
- [ ] Major market station eliminating 80% of manual proposal preparation time

---

*Generated: 2026-02-20 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*