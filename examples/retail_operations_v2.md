# Retail × Operations Playbook

## Overview

Operations in retail is the heartbeat of the business — orchestrating the complex dance of inventory, stores, warehouses, workforce, and customer fulfillment. Retail Ops leaders manage thin margins (2-5% net) while juggling unpredictable demand, labor challenges, and omnichannel complexity. Every inefficiency hits the bottom line directly.

**Typical Scale:**
- Large retailers (Walmart, Target, Home Depot): 1,000+ stores, 100K+ employees, complex supply chains
- Mid-market retailers: 50-500 stores, regional footprint, growing omnichannel
- Specialty/boutique retailers: 5-50 stores, often founder-led, resource-constrained

**Key Pressures:**
- Labor costs rising, availability shrinking (retail's #1 challenge)
- Omnichannel expectations: buy online, pick up in store (BOPIS), same-day delivery
- Inventory distortion: $1.9T global problem (overstock + out-of-stocks)
- Margin compression from e-commerce competition
- Sustainability and supply chain transparency demands

**Operational Reality:** Retail ops runs on razor-thin margins. A 1% improvement in labor efficiency or inventory accuracy can mean millions in profit. They need tools that are fast to deploy, easy for store teams to use, and don't require IT projects.

---

## Value Driver Mapping

| Value Driver | Resonance | Why |
|--------------|-----------|-----|
| **Replace or Radically Augment Headcount** | 🔥🔥 Highest | Labor is 10-15% of revenue and the biggest pain point. AI that reduces manual work, automates scheduling, or handles customer inquiries is gold. |
| **Consolidate Tech Stack with AI** | 🔥 High | Retailers have fragmented systems: WMS, POS, scheduling, task management, communication. Consolidation reduces cost and complexity. |
| **Scale Impact Without Overhead** | 🔥 High | Growing store count or channels without proportionally growing ops team. "Do more with the same" resonates deeply. |

---

## Prioritized Use Cases

---

### Use Case 1: Store Task Management & Execution

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Retail stores drown in tasks: planogram resets, price changes, promotional setups, safety checks, cleaning protocols, inventory counts. Tasks come from corporate, district managers, and store needs — often via email, printouts, or disconnected apps. Store managers spend hours assigning and tracking work. Tasks fall through cracks. Execution is inconsistent across locations. Corporate has no visibility into what actually got done.

#### The Solution
monday.com as a unified task management platform for retail ops: corporate pushes tasks to stores, store managers assign to associates, completion is tracked with photo verification, dashboards show execution rates by store/region. Mobile-first for floor associates. Automations escalate incomplete tasks.

#### The Outcome
- 95%+ task completion rate (up from 70-80%)
- Store managers save 5-8 hours/week on administrative task tracking
- Corporate gains real-time visibility into field execution
- Consistent customer experience across all locations

#### Discovery Questions
1. "How do tasks from corporate get to your stores today? How do store managers know what to prioritize?"
2. "What's your task completion rate across stores? How do you know if a planogram reset actually happened?"
3. "How much time do your store managers spend on administrative work vs. being on the floor with customers?"
4. "When you launch a promotion, how confident are you that every store executed it correctly on day one?"
5. "Do you have visibility gaps between what corporate directs and what stores actually do?"

#### Industry Context
Retailers use various task tools: Reflexis, Zipline, Legion, or homegrown solutions. "Planogram" is the visual layout of products on shelves. "Resets" are major shelf reorganizations. Compliance is tracked for brand standards, safety (OSHA), and promotional execution. District Managers (DMs) oversee 8-15 stores each.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Store Task Management board for retail operations. Columns: Task Name, Task ID (auto-number), Task Type (dropdown: Planogram Reset, Price Change, Promotional Setup, Safety/Compliance, Inventory, Cleaning, Training, Ad Hoc), Priority (status: Critical, High, Medium, Low), Store (dropdown — will populate with store list), Assigned To (people), Due Date (date), Status (status: Not Started, In Progress, Blocked, Complete, Verified), Completion Photo (files), Verified By (people), Source (dropdown: Corporate, District Manager, Store), and Notes (long text). Add automations: when Due Date is today and Status is Not Started, notify Store Manager; when Status changes to Complete, notify District Manager for verification; when Priority is Critical and not complete by Due Date, escalate to Regional Director. Create a Kanban view by Status, a Dashboard showing completion rate by store, and a Calendar view for due dates."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Store Execution Agent

**Agent Purpose:**  
Ensure every store task gets completed on time by intelligently assigning work, sending reminders, verifying completion, and escalating issues — so store managers can focus on customers, not checklists.

**Triggers:**
- New task created (from corporate or district)
- Task due date approaching (24 hours, 4 hours, 1 hour)
- Task marked complete (trigger verification)
- Task overdue
- Store opens (daily task push)

**Actions:**
- Auto-assign tasks based on associate role, skills, and current workload
- Send mobile push notifications to assigned associates
- Escalate approaching-due tasks to store manager
- When marked complete: Check for required photo, flag if missing
- Verify completion: Use image recognition to confirm planogram matches template
- Generate daily store scorecard: Tasks complete, overdue, compliance rate
- Compile weekly execution report for district/regional leadership

**Data Required:**
- Task board (all tasks)
- Store list with org hierarchy (region → district → store)
- Associate roster with roles and schedules
- Planogram templates (for visual verification)
- Historical completion data

**Autonomy Level:** Escalation-Based
- Task assignment and reminders: Fully autonomous
- Photo verification: Agent flags issues, human confirms
- Task creation: Corporate/DM creates, agent distributes

**Example Interaction:**
> *Tuesday 6 AM — Corporate creates a task: "Spring Promotional Endcap Setup" due Thursday for all 200 stores.*
>
> The Store Execution Agent distributes the task to each store, automatically assigning to the Visual Merchandising Lead (or Store Manager if no VM role). Each associate receives a mobile notification with instructions and planogram images.
>
> By Wednesday evening, 187 stores show "Complete" with photos. 13 stores are "Not Started."
>
> Agent sends escalation to the 3 District Managers covering those 13 stores:
> *"⚠️ Execution Alert: 'Spring Promotional Endcap' due tomorrow. 13 stores not started: [list]. Please follow up. Current completion: 93.5%."*
>
> Thursday 9 AM: Agent compiles report: "Spring Endcap: 98% complete (196/200). 4 stores missed deadline — flagged for DM review."

---

---

### Use Case 2: Workforce Scheduling & Labor Optimization

**Relevance:** Highest  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Retail scheduling is a nightmare: balancing labor budgets, employee availability, skill requirements, and fluctuating traffic. Managers spend 6-10 hours per week building schedules. Call-outs create last-minute scrambles. Overstaffing wastes labor dollars; understaffing hurts customer experience and sales. Many retailers still use spreadsheets or clunky legacy systems.

#### The Solution
monday.com for workforce scheduling with smart automation: demand forecasting integration suggests optimal staffing, employees submit availability via forms, scheduling templates speed creation, shift swap workflows handle changes, and dashboards track labor cost vs. budget. Integrations with POS for traffic data and HRIS for employee records.

#### The Outcome
- 50% reduction in scheduling time for managers (6 hours → 3 hours)
- 2-4% labor cost savings through better alignment with demand
- Reduced call-out chaos with automated shift swap and fill processes
- Employee satisfaction: predictable schedules, easy swap requests

#### Discovery Questions
1. "How long does it take your store managers to build the weekly schedule? What tool do they use?"
2. "How do you handle call-outs? What happens when someone doesn't show up?"
3. "Are your labor costs aligned with traffic patterns? Do you have visibility into overstaffing or understaffing?"
4. "How do employees request time off or swap shifts? Is that process smooth?"
5. "What percentage of your labor budget variance comes from scheduling inefficiency vs. other factors?"

#### Industry Context
Labor is 10-15% of retail revenue — the single largest controllable expense after cost of goods. Retailers use WFM (Workforce Management) tools like Kronos (UKG), Legion, Reflexis. "Labor model" defines hours needed per sales volume. "Demand forecast" predicts traffic. Fair workweek laws in some cities require advance schedule notice.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Workforce Scheduling board for retail stores. Columns: Employee Name (people), Role (dropdown: Sales Associate, Cashier, Stock Associate, Supervisor, Keyholder, Manager), Week Of (date), Monday Shift, Tuesday Shift, Wednesday Shift, Thursday Shift, Friday Shift, Saturday Shift, Sunday Shift (all time range or text), Total Hours (formula), Max Hours (number), Availability Notes (text), Status (status: Draft, Published, Confirmed), and Store (dropdown). Add a separate Shift Swap board with: Requesting Employee, Original Shift Date, Original Shift Time, Swap With (people), Status (status: Requested, Approved, Denied), and Manager Approval (people). Add automations: when Total Hours exceeds Max Hours, highlight and notify manager; when schedule Status changes to Published, notify all employees on the schedule; when Shift Swap Status changes to Requested, notify Store Manager. Create a Calendar view showing shifts by employee."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Smart Scheduler Agent

**Agent Purpose:**  
Dramatically reduce scheduling effort by auto-generating optimized schedules based on demand forecasts, employee availability, skills, and labor budget — while handling the chaos of shift swaps and call-outs.

**Triggers:**
- Weekly scheduling cycle begins (e.g., every Wednesday for next week)
- Employee submits availability or time-off request
- Shift swap requested
- Call-out reported
- Demand forecast updated

**Actions:**
- Generate draft schedule: Match labor hours to forecasted demand, respect availability, balance hours fairly, comply with labor rules (min hours between shifts, max consecutive days)
- Flag conflicts: "Maria requested Tuesday off but is the only closer available"
- Auto-approve shift swaps if both employees are qualified and hours balance
- When call-out reported: Identify qualified available employees, send shift-fill requests, track responses
- Calculate labor cost projection vs. budget, flag variances
- Post-week analysis: Actual vs. scheduled hours, labor efficiency, overtime

**Data Required:**
- Employee roster with roles, skills, availability, max hours
- Demand forecast (from POS traffic data or manual input)
- Labor budget by store/week
- Labor law rules (state/local requirements)
- Historical scheduling patterns

**Autonomy Level:** Human-in-the-Loop
- Schedule generation: Agent creates draft, manager reviews/adjusts/publishes
- Shift swaps: Agent auto-approves if rules met, flags exceptions
- Call-out fill: Agent sends requests, employee accepts, manager notified

**Example Interaction:**
> *Wednesday 8 AM — Weekly scheduling cycle for Store #147.*
>
> The Smart Scheduler Agent pulls next week's sales forecast (up 15% due to promotion), current employee availability (2 associates out on PTO), and labor budget ($12,400).
>
> Agent generates draft schedule:
> - Total hours: 340 (within budget)
> - Coverage: All peak hours staffed at forecast levels
> - Flags: "Saturday PM shift: Only 1 closer available. Recommend cross-training backup."
>
> Store Manager Sarah reviews the draft, makes 2 tweaks, and publishes. All 14 employees receive notification with their schedules.
>
> Friday 6 AM: Associate Jake calls out sick for his 10 AM shift.
> Agent identifies 3 available qualified associates, sends texts:
> *"Shift available: Today 10 AM - 6 PM at Store #147. Reply YES to accept."*
>
> Associate Mike replies YES. Agent confirms the fill, updates schedule, notifies Sarah:
> *"✅ Call-out filled: Jake's shift covered by Mike. No manager action needed."*

---

---

### Use Case 3: Inventory & Replenishment Tracking

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Inventory distortion costs retailers $1.9 trillion globally — both overstock (markdowns, waste) and out-of-stocks (lost sales). Store associates do manual shelf scans. Replenishment is reactive. Shrinkage (theft, damage, administrative error) erodes margins. Inventory data is often siloed between WMS, POS, and ERP — nobody has a real-time accurate view.

#### The Solution
monday.com as an inventory visibility and action layer: out-of-stock alerts trigger replenishment tasks, shrinkage investigations are tracked, cycle count schedules are managed, and dashboards show inventory health by store/category. Integrations pull data from WMS/ERP; monday becomes the action and workflow layer.

#### The Outcome
- 20-30% reduction in out-of-stocks through faster replenishment response
- Shrinkage reduced by systematic investigation and tracking
- Cycle count compliance: 100% on schedule
- Single view of inventory actions and issues across stores

#### Discovery Questions
1. "How do you currently identify out-of-stocks? How long does it take to replenish once you know?"
2. "What's your shrinkage rate? How do you investigate and address it?"
3. "How confident are you in your inventory accuracy? When was your last wall-to-wall count?"
4. "Do your store associates have visibility into what's in the backroom vs. what should be on the shelf?"
5. "Is inventory data siloed across systems, or do you have a single source of truth?"

#### Industry Context
"Perpetual inventory" is the theoretical count based on receipts and sales. "Shrink" is the gap between perpetual and actual (typically 1-3% of sales). "Cycle counts" are partial physical counts done regularly. "PI" (Physical Inventory) is a full wall-to-wall count. "OOS" = Out of Stock. "DOS" = Days of Supply. Retailers use WMS (Manhattan, Blue Yonder) and inventory optimization tools (Relex, o9).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an Inventory Issues board for retail operations. Columns: Issue ID (auto-number), Store (dropdown), Issue Type (dropdown: Out of Stock, Low Stock, Overstock, Shrinkage, Damage, Cycle Count Variance), Product/SKU (text), Category (dropdown: Apparel, Electronics, Home, Food, Health & Beauty, Other), Quantity Variance (number), Dollar Impact (number with $), Reported By (people), Assigned To (people), Status (status: Identified, Investigating, Action Taken, Resolved, Escalated), Root Cause (dropdown: Theft, Vendor Error, Receiving Error, System Error, Damage, Unknown), Resolution Notes (long text), and Evidence/Photos (files). Add automations: when Issue Type is Shrinkage and Dollar Impact > $500, notify Loss Prevention; when Status is Identified for more than 48 hours, escalate to District Manager; weekly on Monday, create summary report of open issues. Create a Dashboard showing issues by type, dollar impact by store, and shrinkage trends."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Inventory Health Agent

**Agent Purpose:**  
Proactively monitor inventory health across all stores, identify problems before they impact sales, trigger replenishment actions, and track shrinkage investigations to resolution.

**Triggers:**
- Inventory level drops below threshold (real-time from WMS/POS integration)
- Cycle count variance detected
- Shrinkage flag from POS (high-risk transaction patterns)
- Daily inventory health scan (6 AM)
- Weekly shrinkage review cycle

**Actions:**
- Out-of-stock detected: Create replenishment task, assign to stock associate, set priority based on item velocity
- Low stock alert: Notify store manager with days-of-supply remaining
- Cycle count variance: Create investigation item, attach data, assign to inventory lead
- Shrinkage analysis: Correlate transaction patterns, identify high-risk items/times, recommend LP focus areas
- Generate weekly inventory health scorecard by store: Fill rate, shrink rate, count accuracy
- Trend analysis: "Store #42 has 3x average shrink in Electronics — investigate"

**Data Required:**
- Inventory data (WMS/ERP integration)
- POS transaction data (sales, returns, voids)
- Product master (SKU, category, velocity, cost)
- Store list and hierarchy
- Historical shrinkage and variance data

**Autonomy Level:** Escalation-Based
- Alerts and task creation: Fully autonomous
- Replenishment tasks: Auto-created, store executes
- Shrinkage investigations: Agent flags and assigns, LP/manager investigates

**Example Interaction:**
> *Thursday 6:15 AM — Daily inventory scan for Store #89.*
>
> The Inventory Health Agent identifies:
> - 3 SKUs at zero on-hand with sales velocity >10/day (critical OOS)
> - 1 SKU with 47-unit variance from last cycle count ($612 impact)
> - Electronics category shrink trending 40% above average this month
>
> Agent takes action:
> - Creates 3 "Urgent Replenishment" tasks assigned to morning stock crew: "Pull from backroom: SKU #4421, #4422, #4450 — high velocity OOS"
> - Creates investigation item for the 47-unit variance, assigns to Inventory Lead Maria
> - Sends alert to Loss Prevention: "Store #89 Electronics shrink alert: 40% above average. High-risk SKUs: [list]. Recommend camera review and associate awareness."
>
> Store Manager gets morning summary:
> *"📦 Store #89 Inventory Health — Feb 12*
> *Critical OOS: 3 (tasks created)*
> *Variance investigations: 1 open*
> *⚠️ Electronics shrink flagged — LP notified*
> *Overall fill rate: 94.2%"*

---

---

### Use Case 4: New Store Opening & Remodel Management

**Relevance:** Medium-High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Opening a new store involves hundreds of tasks across real estate, construction, merchandising, hiring, training, IT setup, marketing, and compliance. Coordination happens across spreadsheets, email, and disconnected teams. Critical path items slip. Stores open late or with incomplete execution. Remodels disrupt existing operations with poor coordination.

#### The Solution
monday.com as the command center for new store openings and remodels: standardized playbook templates, cross-functional task ownership, milestone tracking, dependency management, and executive visibility dashboards. Each store opening is a "project" with clear phases, owners, and go/no-go gates.

#### The Outcome
- On-time store openings: 95%+ (vs. industry average 70-80%)
- Reduced coordination overhead: single source of truth for all teams
- Repeatable playbook: each opening is smoother than the last
- Executive confidence: clear visibility into pipeline and risks

#### Discovery Questions
1. "How many new stores are you opening this year? What about remodels?"
2. "Walk me through your new store opening process. How many tasks? How many teams involved?"
3. "What percentage of your stores open on time and fully ready? What causes delays?"
4. "How do you currently coordinate between real estate, construction, merchandising, HR, and IT?"
5. "Do you have a standardized playbook, or does each opening reinvent the wheel?"

#### Industry Context
NSO = New Store Opening. "Grand opening" is the public launch. "Soft opening" tests operations before grand opening. "Fixturing" is installing shelves, racks, displays. "Merchandise flow" is the process of receiving and placing initial inventory. Typical NSO timeline: 6-18 months depending on format (small format faster, large format longer).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a New Store Opening board for retail operations. Columns: Store Name, Store Number, Location (text), Format (dropdown: Full Size, Small Format, Outlet, Pop-Up), Target Open Date (date), Actual Open Date (date), Status (status: Site Selection, Lease Negotiation, Permitting, Construction, Fixturing, Merchandising, Staffing, Training, Soft Open, Grand Open, Complete), Project Manager (people), Phase (dropdown: Pre-Construction, Construction, Pre-Opening, Opening, Post-Opening), Budget (number with $), Spend to Date (number with $), Days to Open (formula), Risk Level (status: Green, Yellow, Red), and Key Risks (long text). Add a linked board for Tasks with: Task Name, Phase, Owner (people), Due Date, Status, Predecessor Task, and Notes. Add automations: when Target Open Date is within 60 days and Status is before 'Merchandising', flag as at-risk; when Status changes, notify Project Manager and Regional VP. Create a Timeline view showing all openings, and a Dashboard with openings by status, budget vs. spend, and at-risk stores."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Store Opening Coordinator Agent

**Agent Purpose:**  
Orchestrate the complex, cross-functional process of opening new stores by tracking hundreds of tasks, identifying risks early, keeping all teams aligned, and ensuring nothing falls through the cracks.

**Triggers:**
- New store opening project created
- Task status updated
- Task due date approaching (7 days, 3 days, 1 day)
- Task overdue
- Milestone date reached
- Weekly status review cycle

**Actions:**
- Initialize project from playbook template (auto-create all tasks with default timelines)
- Assign tasks based on role (construction tasks → facilities team, hiring → HR, etc.)
- Track dependencies: If Task A slips, auto-adjust Task B-Z timelines
- Send proactive reminders to task owners
- Flag critical path risks: "Construction permit delayed — will impact fixturing start"
- Generate weekly status report: Tasks complete, upcoming, at-risk
- Conduct go/no-go assessment: "28 days to open. 12 tasks incomplete. Recommend: Delay soft open by 1 week or add resources."

**Data Required:**
- NSO playbook template (standard tasks, durations, dependencies)
- Store opening board (all active projects)
- Task board (linked)
- Team directory with roles
- Historical data (average task durations, common delay causes)

**Autonomy Level:** Human-in-the-Loop
- Task creation and assignment from playbook: Fully autonomous
- Reminders and escalations: Fully autonomous
- Timeline adjustments: Agent recommends, PM approves
- Go/no-go decision: Agent provides data, leadership decides

**Example Interaction:**
> *January 15 — New store approved: Store #203, Suburban Mall Location, Target Open: April 15 (90 days).*
>
> Store Opening Coordinator Agent initializes project:
> - Creates 147 tasks from playbook template across 6 phases
> - Auto-assigns based on role matrix (Construction → Mike, HR → Lisa, Merchandising → Regional VM Team, etc.)
> - Calculates critical path: Permit approval (Jan 30) → Construction (Feb 1 - Mar 15) → Fixturing (Mar 16-25) → Merchandise (Mar 26 - Apr 5) → Training (Apr 6-12) → Soft Open (Apr 13)
>
> *February 5 — Permit approval task still showing "In Progress" (5 days overdue).*
>
> Agent sends alert to Project Manager and Construction Lead:
> *"🚨 Critical Path Risk: Store #203 permit approval overdue by 5 days. Current impact: Construction start delayed to Feb 6. If permit not received by Feb 10, recommend pushing Target Open Date. What's the blocker?"*
>
> *Weekly Status Report (Feb 12):*
> *"Store #203 — 62 days to open*
> *✅ Complete: 23 tasks | 🔄 In Progress: 18 | ⏳ Upcoming: 106*
> *⚠️ At Risk: Permit (5 days late), HVAC contractor (start date TBD)*
> *📊 Confidence: Yellow — recoverable if permit clears this week"*

---

---

### Use Case 5: Vendor & Supplier Coordination

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Retail operations depend on vendors: product suppliers, fixture vendors, service providers (cleaning, security, maintenance), logistics partners. Coordination is fragmented — purchase orders in one system, delivery tracking in another, quality issues in email, service requests via phone. When a vendor underperforms, there's no systematic tracking. When a delivery is late, store scrambles.

#### The Solution
monday.com as a vendor coordination hub: track deliveries, manage service requests, log quality issues, monitor vendor performance scorecards, and automate routine communications. Vendors can access a portal to update status and receive tasks.

#### The Outcome
- 30% reduction in vendor-related fire drills
- Vendor performance visibility: data-driven decisions on renewals
- Faster issue resolution: systematic tracking vs. email chaos
- Reduced stockouts from late deliveries: proactive alerts

#### Discovery Questions
1. "How many vendors do you work with regularly? How do you communicate with them?"
2. "When a delivery is late or a shipment has quality issues, what's the process?"
3. "Do you have visibility into vendor performance over time? Can you tell me your top 3 and bottom 3 vendors right now?"
4. "How do store managers request maintenance or services? How long does it take?"
5. "Have you ever had a major disruption because of vendor issues you didn't see coming?"

#### Industry Context
Retailers work with hundreds of vendors: product suppliers (brands), private label manufacturers, fixture/display vendors, logistics (3PLs), and service providers. "ASN" = Advance Ship Notice (delivery pre-alert). "PO" = Purchase Order. "Chargebacks" are penalties for vendor compliance failures (late delivery, labeling errors). Vendor scorecards track OTIF (On-Time In-Full), quality, and compliance.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Vendor Management board for retail operations. Columns: Vendor Name, Vendor Type (dropdown: Product Supplier, Fixture/Display, Logistics/3PL, Maintenance, Cleaning, Security, Other), Primary Contact (text), Contact Email (email), Contract End Date (date), Status (status: Active, Under Review, Probation, Terminated), Performance Score (number 1-100), Last Review Date (date), Notes (long text). Add a linked Delivery Tracking board with: PO Number, Vendor, Expected Delivery Date, Actual Delivery Date, Store/DC (dropdown), Status (status: Ordered, Shipped, In Transit, Delivered, Delayed, Issue), Quantity Ordered, Quantity Received, Variance, and Issue Notes. Add a linked Service Requests board with: Request Type (dropdown: Maintenance, Cleaning, Fixture Repair, Emergency), Store, Vendor, Requested Date, Completed Date, Status, and Feedback. Add automations: when Delivery Status is Delayed, notify Ops Manager; when Contract End Date is within 90 days, notify Procurement. Create a Dashboard showing vendor performance scores, deliveries by status, and service request completion times."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Vendor Performance Agent

**Agent Purpose:**  
Monitor vendor performance in real-time, flag issues proactively, track delivery accuracy, and provide data-driven recommendations for vendor decisions — ensuring supply chain reliability.

**Triggers:**
- Delivery date approaching (2 days out: check for ASN)
- Delivery received (calculate OTIF)
- Quality issue reported
- Service request overdue
- Monthly vendor review cycle
- Contract renewal approaching (90 days)

**Actions:**
- Track OTIF (On-Time In-Full) for every vendor, every delivery
- Alert when delivery is expected but no ASN received: "PO #4521 due in 2 days — no ship confirmation from Vendor X"
- When delivery received: Compare to PO, calculate variance, auto-create issue if short or damaged
- Calculate rolling vendor performance scores: OTIF, quality rate, response time
- Flag underperformers: "Vendor Y OTIF dropped to 72% (threshold: 90%). Recommend review."
- Pre-renewal analysis: "Contract renewing in 60 days. Performance: 88%. Issues: 3 quality claims ($4,200). Recommendation: Negotiate improvement terms."

**Data Required:**
- Vendor master list
- Purchase orders and delivery tracking
- Quality issue log
- Service request history
- Contract terms and dates
- Historical performance data

**Autonomy Level:** Escalation-Based
- Performance tracking: Fully autonomous
- Issue flagging: Fully autonomous
- Vendor decisions (terminate, renew): Agent recommends, humans decide

**Example Interaction:**
> *Tuesday 7 AM — Vendor Performance Agent runs daily delivery check.*
>
> Identifies:
> - 3 deliveries expected today: Vendor A (ASN confirmed ✓), Vendor B (ASN confirmed ✓), Vendor C (no ASN)
> - 2 deliveries received yesterday: Vendor A (OTIF ✓), Vendor D (15 units short)
>
> Agent actions:
> - Sends alert to Vendor C: "Delivery PO #7832 expected today. Please confirm shipment status."
> - Creates shortage item for Vendor D: "PO #7801 — 15 units short ($340). Assigned to Vendor Manager for follow-up."
> - Updates Vendor D rolling OTIF: Dropped from 94% to 91%
>
> *Monthly Vendor Review (Feb 1):*
>
> Agent generates report:
> *"📊 Vendor Performance Summary — January*
> *Top Performers: Vendor A (98% OTIF), Vendor E (97% OTIF)*
> *Watch List: Vendor D (91% OTIF, declining), Vendor G (2 quality issues)*
> *Contract Renewals: Vendor B (Mar 15), Vendor H (Apr 1)*
> *Recommendation: Schedule review with Vendor D; prepare negotiation brief for Vendor B renewal."*

---

---

### Use Case 6: Customer Feedback & Issue Resolution

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Customer complaints come from everywhere: in-store, call center, social media, email, online reviews. There's no unified view. Store managers don't see feedback about their location. Issues fall through cracks. Trends aren't identified until they become PR crises. Responding to Google/Yelp reviews is inconsistent.

#### The Solution
monday.com as a customer feedback command center: aggregate feedback from all sources, route issues to appropriate stores/teams, track resolution, identify trends, and manage review responses. Dashboards show sentiment by store, category, and time.

#### The Outcome
- 100% of customer issues tracked and closed
- 50% faster resolution time with clear ownership
- Trend identification: catch problems early (e.g., cleanliness complaints at Store X)
- Improved online ratings through consistent review response

#### Discovery Questions
1. "Where does customer feedback come from today? Do you have a unified view?"
2. "When a customer complains about a specific store, does the store manager hear about it?"
3. "How quickly do you respond to Google or Yelp reviews? Who owns that?"
4. "Have you ever been surprised by a systemic issue that customers were complaining about for weeks?"
5. "How do you measure customer satisfaction at the store level?"

#### Industry Context
NPS (Net Promoter Score) is a common metric. "VOC" = Voice of Customer. Review platforms (Google, Yelp, industry-specific) significantly impact foot traffic. Social listening tools monitor Twitter, Facebook, Instagram. Many retailers use Medallia, Qualtrics, or SMG for customer feedback.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Customer Feedback board for retail operations. Columns: Feedback ID (auto-number), Customer Name (text), Contact Info (email), Store (dropdown), Feedback Source (dropdown: In-Store, Phone, Email, Google Review, Yelp, Social Media, Survey), Category (dropdown: Product Quality, Service, Cleanliness, Wait Time, Pricing, Staff Behavior, Other), Sentiment (status: Positive, Neutral, Negative), Summary (text), Full Feedback (long text), Assigned To (people), Status (status: New, In Progress, Resolved, Closed, Escalated), Resolution Notes (long text), Response Sent (checkbox), and Date Received (date). Add automations: when Sentiment is Negative and Source is Google Review or Yelp, notify Store Manager and Marketing immediately; when Status is New for more than 24 hours, escalate; when Status changes to Resolved, send thank-you email to customer (if email provided). Create a Dashboard showing feedback by sentiment, store, and category, plus trends over time."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Customer Voice Agent

**Agent Purpose:**  
Ensure no customer feedback goes unaddressed by aggregating input from all channels, routing issues to the right teams, drafting responses, and surfacing trends before they become crises.

**Triggers:**
- New feedback received (any channel)
- Negative review posted on Google/Yelp
- Issue unresolved for >24 hours (negative) or >48 hours (neutral)
- Weekly trend analysis cycle
- Store NPS drops below threshold

**Actions:**
- Categorize and sentiment-score incoming feedback
- Route to appropriate owner (store issue → store manager, product issue → merchant team)
- For public reviews: Draft response, send for manager approval, post after approval
- For direct complaints: Suggest resolution based on similar past issues
- Analyze trends: "Cleanliness complaints at Store #52 up 200% this month"
- Generate weekly customer voice report: Sentiment trends, top issues, standout stores

**Data Required:**
- Customer feedback board (all channels)
- Store list with managers
- Integration with review platforms (Google Business, Yelp API)
- Social listening integration (optional)
- Historical resolution data and response templates

**Autonomy Level:** Human-in-the-Loop
- Categorization and routing: Fully autonomous
- Response drafts: Agent writes, human approves before posting
- Trend alerts: Fully autonomous
- Customer compensation decisions: Human only

**Example Interaction:**
> *Saturday 3 PM — New 1-star Google review for Store #77:*
> *"Terrible experience. Waited 20 minutes for help while employees chatted. Never coming back."*
>
> Customer Voice Agent instantly:
> - Creates feedback item: Store #77, Source: Google, Category: Service/Wait Time, Sentiment: Negative
> - Notifies Store Manager immediately
> - Drafts response: "We're so sorry to hear about your experience. This isn't the service we strive for. Our store manager will be reaching out, and we'd love the chance to make this right. Please contact us at [email] or call [number]."
> - Sends draft to Store Manager for review/edit
>
> Store Manager tweaks slightly, approves. Response posts within 2 hours.
>
> *Weekly Report (Feb 12):*
> *"📢 Customer Voice Summary — Week of Feb 5*
> *Total Feedback: 342 | Positive: 58% | Neutral: 27% | Negative: 15%*
> *⚠️ Trend Alert: 'Wait time' complaints up 45% vs. last week (primarily Stores #77, #82)*
> *🌟 Standout: Store #41 — 12 positive reviews mentioning 'helpful staff'*
> *Response Rate: 94% within 24 hours"*

---

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **BOPIS** | Buy Online, Pick Up In Store |
| **Shrink/Shrinkage** | Inventory loss from theft, damage, or errors (typically 1-3% of sales) |
| **Planogram** | Visual diagram showing product placement on shelves |
| **Comp/Comps** | Comparable store sales — year-over-year performance |
| **OTIF** | On-Time In-Full — vendor delivery performance metric |
| **WFM** | Workforce Management — scheduling and labor tools |
| **WMS** | Warehouse Management System |
| **POS** | Point of Sale — the checkout system |
| **SKU** | Stock Keeping Unit — unique product identifier |
| **DM** | District Manager — oversees multiple stores |
| **LP** | Loss Prevention — theft/shrink prevention team |
| **ASN** | Advance Ship Notice — vendor notification of incoming shipment |
| **DOS** | Days of Supply — how long current inventory will last |
| **Fill Rate** | Percentage of demand met by available inventory |
| **NSO** | New Store Opening |
| **Markdown** | Price reduction to clear inventory |

---

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|----------------|-----------|
| **VP/SVP Operations** | Overall store operations strategy | Decision maker |
| **Director, Store Operations** | Day-to-day operations leadership | Key buyer |
| **Regional VP/Director** | P&L for a region (50-150 stores) | Influential |
| **District Manager** | Oversees 8-15 stores | Implementer, feedback source |
| **Store Manager** | Single store P&L and team | End user |
| **Director, Workforce Planning** | Labor strategy and scheduling | Key buyer for WFM |
| **VP Supply Chain** | Inventory and logistics | Adjacent buyer |
| **Director, Loss Prevention** | Shrink reduction | Stakeholder |

---

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Supply Chain/Logistics** | Inventory, replenishment, DC operations | Expand from store ops into supply chain visibility |
| **Merchandising** | Planograms, assortment, pricing | Task execution and compliance tracking |
| **HR** | Hiring, training, employee engagement | Workforce scheduling connects to HRIS |
| **Marketing** | Promotions, signage, campaigns | Promotional execution tracking |
| **Real Estate** | New stores, remodels, closures | Project management |
| **IT** | POS, WMS, integrations | Technology partner for integrations |

---

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Reflexis (Zebra)** | Task management + WFM for retail | Complex, expensive, slow to implement. monday.com is faster, more flexible, better UX |
| **Zipline** | Retail communication and task management | Strong in comms, but limited workflow. monday.com offers broader platform |
| **Legion** | AI-powered workforce management | Point solution for scheduling. monday.com is broader platform play |
| **Kronos/UKG** | Enterprise WFM | Expensive, complex. monday.com can complement or replace for smaller retailers |
| **Asana/Monday competitors** | General work management | monday.com has retail-specific templates and better ops workflows |
| **Spreadsheets** | The default | Huge displacement opportunity — millions of retailers still on Excel |

**Key Differentiator:** Most retail ops tools are point solutions — one for tasks, one for scheduling, one for inventory. monday.com is a unified platform that can replace or consolidate multiple tools while being fast to deploy and easy for frontline workers to use.

---

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Reflexis/Zipline" | "Many retailers use both — monday.com for the workflows Reflexis can't handle quickly. Or, let's talk about what it would take to simplify to one platform. What's your renewal timeline?" |
| "Our store associates aren't tech-savvy" | "That's exactly why UX matters. monday.com is mobile-first and consumer-grade simple. Associates who use Instagram can use monday. Let me show you the mobile experience." |
| "We need to integrate with our POS/WMS/ERP" | "Absolutely — no retail tool works in isolation. monday.com has robust APIs and pre-built integrations. We can connect to your existing systems so data flows automatically." |
| "We're a lean team and don't have time to implement" | "You don't need a 6-month IT project. Vibe lets you build a working task management system in minutes. Let's try it — what's a workflow that's painful right now?" |
| "How do you handle thousands of stores?" | "monday.com scales to enterprise. We have retail customers with 1,000+ locations. The architecture handles it, and we can talk about enterprise features like permissions, SSO, and governance." |

---

## Proof Points

*(To be populated with customer references)*

- **[Retailer Name]** — Reduced store task completion time by 40% and improved execution consistency across 500 stores
- **[Retailer Name]** — Cut scheduling time by 60% while improving labor cost alignment with traffic
- **[Retailer Name]** — Consolidated 4 tools into monday.com, saving $300K annually and reducing training complexity

---

*Generated: 2026-02-12 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
