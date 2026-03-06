# Commercial & Residential Construction × Procurement Playbook

## Overview

Procurement in commercial and residential construction is one of the most complex, high-stakes purchasing functions in any industry. Unlike manufacturing procurement where you buy the same components repeatedly, construction procurement is project-based: every building requires a unique bill of materials, and procurement teams must source, negotiate, and schedule delivery of thousands of line items — from structural steel and concrete to finish materials like countertops, fixtures, and flooring — all synchronized to a construction schedule that shifts constantly.

A mid-market general contractor or developer might manage $50M–$500M in annual procurement spend across 5–20 simultaneous projects. The procurement team (typically 3–15 people depending on firm size) handles subcontractor procurement (trade buyouts), material purchasing, equipment rental, and vendor qualification. They navigate volatile commodity markets (lumber prices can swing 30% in a quarter), long lead times (custom curtain wall systems: 16–24 weeks; electrical switchgear: 20–30 weeks), and complex compliance requirements (Buy America provisions, LEED material sourcing, prevailing wage vendor certifications).

The regulatory environment adds layers of complexity. Government-funded projects require Davis-Bacon Act compliance for labor and Buy American/Buy America material sourcing. LEED and green building certifications mandate specific material documentation (EPDs, HPDs, VOC content certificates). Bonding requirements mean subcontractors must provide performance and payment bonds, often managed through the procurement workflow. Insurance certificate tracking (COIs) is a perpetual administrative burden — every vendor and subcontractor needs current certificates on file before they can step onto a job site.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Consolidate Tech Stack with AI | High | Procurement data lives in spreadsheets, email, ERPs, estimating software, and filing cabinets — no single system tracks the full procurement lifecycle from bid to delivery to payment |
| 2 | Replace or Radically Augment Headcount | High | Manual tasks like COI tracking, bid tabulation, submittal logging, and PO status follow-ups consume 40–60% of procurement staff time |
| 3 | Scale Impact Without Overhead | Medium-High | As firms take on more projects, procurement teams don't scale linearly — they need to handle 30% more spend with the same headcount |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Subcontractor Bid Management & Trade Buyout Tracker

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Trade buyout — the process of soliciting bids from subcontractors for each trade (electrical, plumbing, HVAC, drywall, painting, etc.) — is the single most impactful procurement activity. A commercial project might have 30–50 trade packages, each requiring 3–5 competitive bids. That's 90–250 bid solicitations per project, managed through email, phone calls, and Excel spreadsheets. Procurement managers spend hours creating bid comparison spreadsheets ("bid tabs"), chasing non-responsive subcontractors, and ensuring bid scopes are truly apples-to-apples. A 1% improvement in buyout savings on a $100M project is $1M to the bottom line.

#### The Solution
A Trade Buyout board on monday.com for each project. Items represent individual trade packages (CSI divisions). Columns track scope of work, budget estimate, invited bidders (connected to a Subcontractor Database board), bid due date, received bids (with amounts), bid tab status, awarded subcontractor, contract status, and savings vs. budget. Subitems represent individual bidders within each trade. Automations send bid invitations, reminder emails before due dates, and notifications when bids are received. Dashboard shows buyout progress, total committed cost vs. budget, and savings by trade.

#### The Outcome
Buyout cycle time reduced by 35% through automated bid solicitation and follow-up. Average of 4.2 bids received per trade vs. previous 2.8, increasing competitive tension and saving 2–4% on total subcontractor costs. Complete visibility into buyout status across all projects — leadership can see committed vs. uncommitted spend in real-time.

#### Discovery Questions
1. "How many trade packages does a typical project have, and how many bids do you target per trade?"
2. "What's your current process for creating bid comparisons — manual spreadsheets, or do you have a tool?"
3. "How do you track which subcontractors were invited, which responded, and which declined?"
4. "What percentage of your subcontractor invitations result in actual bids? What's the main reason subs don't bid?"
5. "Can you tell me right now, across all active projects, what your total committed subcontractor cost is vs. budget?"

#### Industry Context
In construction, the general contractor's profit margin is often 3–8% on a project. Subcontractor costs represent 70–80% of total project cost. So the buyout process — getting the best price from qualified subcontractors — has an outsized impact on profitability. The difference between a good buyout and a mediocre one can be the difference between a profitable project and a loss. Trade buyouts are organized by CSI MasterFormat divisions (Division 03: Concrete, Division 09: Finishes, Division 23: HVAC, etc.).

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Trade Buyout Tracker board for a construction company's procurement team. Columns: Project (connect board to Projects Master), CSI Division (dropdown: 02 - Existing Conditions, 03 - Concrete, 04 - Masonry, 05 - Metals, 06 - Wood/Plastics/Composites, 07 - Thermal & Moisture Protection, 08 - Openings, 09 - Finishes, 10 - Specialties, 11 - Equipment, 12 - Furnishings, 13 - Special Construction, 14 - Conveying Equipment, 21 - Fire Suppression, 22 - Plumbing, 23 - HVAC, 26 - Electrical, 27 - Communications, 28 - Electronic Safety, 31 - Earthwork, 32 - Exterior Improvements, 33 - Utilities), Trade Package Name (text), Scope Description (long text), Budget Estimate (numbers with $ prefix), Bid Due Date (date), Number of Invitations Sent (numbers), Number of Bids Received (numbers), Low Bid Amount (numbers with $ prefix), Awarded Amount (numbers with $ prefix), Savings vs Budget (formula: Budget Estimate - Awarded Amount), Savings Percentage (formula), Awarded Subcontractor (connect board to Subcontractor Database), Buyout Status (status: Scope Development, Bidding, Bid Review, Negotiation, Awarded, Contract Issued, Contract Executed), Contract Status (status: Drafting, Under Review, Executed, Amended), Bonding Required (checkbox), Bond Received (checkbox), Notes (long text). Use subitems for individual bidders: Subcontractor Name (connect board), Bid Amount (numbers with $), Bid Date (date), Scope Exceptions (text), Bid Status (status: Invited, Reminder Sent, Received, No Bid, Under Review, Shortlisted, Declined). Add automations: when Bid Due Date is 3 days away send reminder to all invited subs with Status 'Invited'; when subitem Bid Status changes to Received update parent Number of Bids Received; when Buyout Status changes to Awarded notify project manager and estimating team. Create a Dashboard with: total buyout savings vs budget (numbers widget), buyout completion percentage by project (progress bar), trades still in bidding (filtered table), and a chart showing savings by CSI division."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BuyoutIQ

**Agent Purpose:** Optimize the trade buyout process by analyzing bid data, identifying scope gaps, recommending qualified subcontractors, and predicting savings opportunities.

**Triggers:**
- New trade package created on Buyout Tracker board
- Bid received from subcontractor (subitem status change)
- Bid Due Date arrived with fewer than 3 bids received
- Buyout Status changed to "Bid Review"
- Weekly Monday morning scan of all active buyouts

**Actions:**
- When a new trade package is created, query the Subcontractor Database and recommend 5–8 qualified bidders based on trade specialty, project location, past performance ratings, current workload, and bonding capacity
- Auto-generate bid invitation package from scope description, project details, and standard bid form template
- When bids are received, auto-populate a bid comparison (bid tab) normalizing for scope exceptions and alternates
- Flag scope gaps: identify items in the budget estimate that aren't covered by any received bid
- When fewer than 3 bids received by due date, identify additional subcontractors to invite and extend the deadline recommendation
- After award, generate a contract checklist: insurance requirements, bonding, safety program, schedule constraints

**Data Required:**
- Subcontractor Database with trade classifications, location, bonding capacity, past project history, and performance ratings
- Project budget breakdown by CSI division
- Historical bid data for market rate benchmarking
- Scope of work documents and specifications
- Prequalification requirements by project type

**Autonomy Level:** Human-in-the-Loop
Recommends subcontractors and generates bid tabs automatically, but procurement manager reviews and approves all invitations and award recommendations. The agent never communicates pricing information between bidders.

**Example Interaction:**
> A new $45M mixed-use project needs to buy out Division 23 (HVAC). The procurement manager creates the trade package with a $4.2M budget estimate. BuyoutIQ queries the Subcontractor Database, filters for mechanical contractors within 50 miles with bonding capacity above $5M and at least 3 completed projects over $3M. It recommends 7 subcontractors, ranking them by composite score: past performance (40%), price competitiveness on previous bids (30%), current backlog (20%), and safety record (10%).
>
> The procurement manager approves 6 of the 7 (declining one due to a past dispute) and the agent generates personalized bid invitations with the scope package. By bid day, 4 responses are in. The agent generates a bid tab: Contractor A: $4.05M (no exceptions), Contractor B: $3.87M (excludes controls), Contractor C: $4.15M (includes 2-year warranty), Contractor D: $3.92M (excludes test & balance). It highlights: "Contractor B's low bid excludes controls — estimated value $180K. Adjusted bid: $4.05M, tying Contractor A. Contractor D excludes T&B — estimated value $45K. Adjusted bid: $3.97M. Recommendation: negotiate with Contractors B and D on inclusions before award decision."

---

### Use Case 2: Insurance Certificate (COI) & Compliance Tracking

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Every subcontractor and vendor that steps onto a construction job site must provide a current Certificate of Insurance (COI) meeting the general contractor's minimum coverage requirements. A typical project has 30–60 subcontractors and vendors, each with policies that expire on different dates throughout the year. The procurement or risk management team manually tracks hundreds of COIs in spreadsheets, chases renewals via email, and verifies coverage limits against contract requirements. One lapsed COI that goes unnoticed can expose the general contractor to millions in liability. It's the most tedious, high-stakes administrative task in construction procurement.

#### The Solution
A COI Compliance Tracker on monday.com. Each item represents a vendor/subcontractor with columns for company name, trade, project(s), general liability limit, auto liability limit, workers' comp limit, umbrella/excess limit, policy expiration dates, COI document upload, and compliance status. Automations send renewal reminders 60, 30, and 14 days before expiration. Status columns flag compliant, expiring soon, expired, and non-compliant vendors. Dashboard shows compliance rates across all projects with drill-down capability.

#### The Outcome
100% COI compliance rate maintained across all active projects (vs. industry average of 75–85%). Procurement staff time on COI tracking reduced by 70% — from ~15 hours/week to ~4 hours/week. Zero instances of uninsured subcontractors on job sites, eliminating a major liability exposure.

#### Discovery Questions
1. "How many active vendor and subcontractor COIs are you tracking across all projects right now?"
2. "Who is responsible for COI tracking — procurement, risk management, project managers, or admin staff?"
3. "How do you currently know when a COI is about to expire? Have you ever discovered an expired COI after the fact?"
4. "What are your minimum insurance requirements, and do they vary by trade or project type?"
5. "Has your company ever faced a claim where a subcontractor's insurance was lapsed or insufficient?"

#### Industry Context
Construction is one of the highest-liability industries. General contractors typically require subcontractors to carry $1M–$2M general liability per occurrence, $2M–$5M aggregate, $1M auto liability, statutory workers' compensation, and often $5M–$10M umbrella coverage. Additional insured endorsements naming the GC, owner, and lender are standard requirements. OCIP (Owner Controlled Insurance Programs) and CCIP (Contractor Controlled Insurance Programs) on large projects add another layer of complexity.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a COI Compliance Tracker board for a construction company. Columns: Company Name (text), Trade/Category (dropdown: General Contractor, Electrical, Plumbing, HVAC, Concrete, Steel, Drywall, Painting, Roofing, Flooring, Landscaping, Excavation, Fire Protection, Elevator, Supplier, Equipment Rental, Professional Services), Projects (connect board to Projects Master — allow multiple), Primary Contact (text), Contact Email (email), General Liability - Per Occurrence (numbers with $ prefix), General Liability - Aggregate (numbers with $ prefix), Auto Liability (numbers with $ prefix), Workers Comp (dropdown: Statutory, Waived - Sole Proprietor, Pending), Umbrella/Excess (numbers with $ prefix), GL Expiration (date), Auto Expiration (date), WC Expiration (date), Umbrella Expiration (date), Additional Insured Endorsement (checkbox), Waiver of Subrogation (checkbox), COI Document (file), Compliance Status (status: Compliant, Expiring <30 Days, Expiring <14 Days, Expired, Non-Compliant, Under Review), Minimum Requirements Met (status: Yes, No - GL Below Minimum, No - Missing WC, No - Missing AI Endorsement, No - Multiple Issues), Last Verified (date), Notes (long text). Add automations: when any expiration date is 60 days away send email to Contact Email requesting renewal; repeat at 30 days and 14 days with escalating urgency; when any expiration date passes change Compliance Status to Expired and notify project manager and risk manager; when COI Document updated change Last Verified to today and set status to Under Review. Create a Dashboard with: compliance rate percentage (numbers widget), vendors by compliance status (pie chart), expirations in next 30 days (table), non-compliant vendors by project (filtered table), and total number of active vendors tracked (numbers widget)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** COI Sentinel

**Agent Purpose:** Automate the entire COI lifecycle — collection, verification, renewal tracking, and compliance enforcement — eliminating manual follow-up and ensuring zero-gap coverage.

**Triggers:**
- New subcontractor/vendor added to COI Tracker board
- COI Document uploaded or updated
- Expiration date within 60/30/14/0 days
- New project assignment added to a vendor (connected board update)
- Daily morning scan for any compliance gaps
- Subcontractor mobilization date approaching (from project schedule)

**Actions:**
- When a new vendor is added, auto-send a COI request email with the company's minimum requirements and a link to upload their certificate
- When a COI is uploaded, parse the document to extract coverage limits, expiration dates, and endorsements — auto-populate the corresponding columns
- Compare extracted limits against minimum requirements and flag deficiencies with specific shortfalls ("GL per occurrence: $500K — minimum required: $1M")
- Send automated renewal reminders at 60, 30, and 14 days with escalating language
- When a COI expires, immediately notify the project superintendent and procurement manager and add the vendor to a "Site Access Restricted" list
- Generate weekly compliance report for risk management showing overall compliance rate, upcoming expirations, and persistent non-compliance issues
- When a vendor is assigned to a new project, verify that their current COI meets that project's specific requirements (which may differ from the standard minimums)

**Data Required:**
- Minimum insurance requirements by project type and trade
- Vendor contact information and communication history
- Project-specific insurance requirements (owner mandated, OCIP/CCIP details)
- COI documents for OCR/parsing
- Project schedules for mobilization date awareness

**Autonomy Level:** Escalation-Based
Fully autonomous for reminders, document parsing, and compliance flagging. Escalates to procurement manager when: coverage limits are below minimums (requires vendor negotiation), a vendor has been non-compliant for 30+ days (requires enforcement decision), or project-specific requirements conflict with standard minimums.

**Example Interaction:**
> On Tuesday morning, the COI Sentinel runs its daily scan and identifies 4 items requiring attention. First, ABC Electrical's general liability policy expires in 12 days — this is their third reminder. The agent escalates: "ABC Electrical (active on 3 projects) GL expiring Feb 28. Two prior reminders sent (Jan 20, Feb 5) with no response. Recommend: call their office directly or contact their insurance agent (Progressive Commercial, policy #EL-4429871). If not renewed by Feb 25, they must be restricted from all job sites."
>
> Second, a new COI was uploaded by Delta Plumbing. The agent parses it: GL $2M/$4M ✓, Auto $1M ✓, WC Statutory ✓, Umbrella $5M ✓, Additional Insured ✓, Waiver of Subrogation ✗. "Delta Plumbing COI is 90% compliant. Missing: Waiver of Subrogation endorsement. This is required on the Meridian Heights project (owner requirement). Action: request updated COI with WoS endorsement." The agent auto-sends an email to Delta's contact explaining the specific missing endorsement.
>
> Third, a new subcontractor (Garcia Landscaping) was just assigned to the Hartwell Station project. The agent checks: Garcia has a valid COI on file but with $500K GL per occurrence. Hartwell Station requires $1M minimum for all trades. "Garcia Landscaping GL coverage ($500K) is below Hartwell Station minimum ($1M). Cannot mobilize until coverage is increased. Notifying procurement manager and project superintendent."

---

### Use Case 3: Purchase Order & Material Procurement Tracking

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Construction material procurement involves thousands of individual purchase orders across a project lifecycle. A $30M commercial building might generate 500–1,000 POs for everything from structural steel to door hardware. Procurement teams track these in a mix of accounting software (which handles the financial side but not the logistics) and spreadsheets (which track delivery schedules but don't connect to budgets). The result: materials arrive late because nobody flagged the 20-week lead time early enough, materials arrive at the wrong site because the PO didn't specify the delivery location clearly, and budget overruns go unnoticed until the monthly accounting reconciliation.

#### The Solution
A Purchase Order Tracker on monday.com integrated with (or replacing) spreadsheet-based tracking. Items represent individual POs with columns for PO number, vendor, project, cost code, description, amount, tax, shipping, total, status (Requisition → Approved → Ordered → Acknowledged → Shipped → Received → Invoiced → Paid), delivery date, actual delivery date, and variance. Connected to the project budget board for real-time cost tracking. Automations flag late deliveries, budget overruns, and unapproved POs.

#### The Outcome
Material delivery delays reduced by 40% through proactive lead-time tracking and automated vendor follow-up. Budget overrun detection moved from monthly (accounting reconciliation) to real-time — procurement catches cost issues within 24 hours. Complete PO audit trail for project closeout and dispute resolution.

#### Discovery Questions
1. "How many purchase orders does a typical project generate over its lifecycle?"
2. "What system do you use today for PO tracking — is it your accounting software, spreadsheets, or something else?"
3. "How do you connect PO costs to your project budget in real-time? Or does that reconciliation happen monthly?"
4. "What's your most common material delivery problem — late deliveries, wrong quantities, wrong site, or damaged goods?"
5. "What's your PO approval workflow — who can issue a PO, and what dollar thresholds require additional approval?"

#### Industry Context
In construction, materials represent 20–30% of total project cost (with subcontractors covering the other 70–80% including their own materials and labor). But material procurement has an outsized impact on schedule — a late delivery of structural steel can delay the entire project by weeks, costing $50K–$100K+ per day in delay damages (liquidated damages in the contract). Long-lead items must be identified during preconstruction and ordered months before they're needed on site.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Purchase Order Tracker board for a construction company. Columns: PO Number (text, auto-generate format: PO-2026-0001), Project (connect board to Projects Master), Vendor (connect board to Vendor Database), Cost Code (dropdown organized by CSI: 03-3000 Cast-in-Place Concrete, 05-1200 Structural Steel, 08-1100 Metal Doors & Frames, 09-2900 Gypsum Board, 09-6500 Resilient Flooring, 22-0000 Plumbing, 23-0000 HVAC, 26-0000 Electrical — include 20+ common codes), Description (text), Quantity (numbers), Unit (dropdown: EA, LF, SF, CY, TON, LS, HR), Unit Price (numbers with $ prefix), Subtotal (formula: Quantity × Unit Price), Tax (numbers with $ prefix), Shipping (numbers with $ prefix), Total (formula: Subtotal + Tax + Shipping), Budget Line Amount (numbers with $ prefix), Variance (formula: Total - Budget Line Amount), Status (status: Requisition, Pending Approval, Approved, Ordered, Vendor Acknowledged, In Production, Shipped, Received, Partial Delivery, Invoiced, Paid, Cancelled), Requested By (people), Approved By (people), Date Requested (date), Date Ordered (date), Expected Delivery (date), Actual Delivery (date), Delivery Variance Days (formula: Actual - Expected), Delivery Location (text), Receiving Confirmation (file - photo), Invoice Number (text), Invoice Amount (numbers with $ prefix), PO Document (file), Notes (long text). Add automations: when Status is Requisition and Total > $10,000 require approval from Procurement Manager; when Status is Requisition and Total > $50,000 require VP approval; when Expected Delivery is 3 days away and Status is not Shipped notify procurement and site superintendent; when Actual Delivery date entered, if Delivery Variance > 5 days flag as late and log to Vendor Performance board; when Invoice Amount differs from Total by > 5%, flag for review. Create Dashboard: total PO spend by project vs budget (bar chart), POs by status (pie chart), late deliveries this month (table), cost code spend breakdown (chart), and pending approvals (filtered table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ProcureGuard

**Agent Purpose:** Monitor the entire purchase order lifecycle, predict delivery risks, enforce budget controls, and optimize vendor performance across all projects.

**Triggers:**
- New PO requisition created
- Expected Delivery date within 7 days with no shipment confirmation
- PO Total exceeds budget line by any amount
- Vendor acknowledgment not received within 48 hours of order
- Monthly vendor performance review cycle
- Invoice received that doesn't match PO amount

**Actions:**
- Validate new POs against remaining budget by cost code — block or flag if spend exceeds budget
- When a PO is ordered, auto-send to vendor with standardized terms and conditions and request acknowledgment
- Track delivery: if 7 days before expected delivery with no shipping confirmation, auto-email vendor requesting status update
- When materials are received, prompt superintendent for receiving confirmation (photo + quantity verification)
- Match incoming invoices against POs — flag discrepancies (quantity, price, unauthorized charges)
- Generate monthly vendor scorecard: on-time delivery rate, price accuracy, quality issues, responsiveness
- Identify long-lead items from specifications during preconstruction and create procurement timeline with order-by dates

**Data Required:**
- Project budgets by cost code
- Vendor database with contact information and historical performance
- Construction schedule for delivery coordination
- Material specifications from project documents
- Standard terms and conditions templates
- Invoice data from accounting system

**Autonomy Level:** Escalation-Based
Auto-validates budgets and sends vendor communications. Blocks POs that exceed budget (requires procurement manager override). Auto-matches invoices but escalates discrepancies > 5% for human review. Vendor performance reports are informational — vendor qualification decisions remain with procurement leadership.

**Example Interaction:**
> A project engineer submits a PO requisition for $28,000 of structural steel connections from a specialty fabricator. ProcureGuard checks: Cost Code 05-1200 (Structural Steel) has a remaining budget of $31,500. This PO would leave only $3,500 — a 90% budget consumption alert. The agent flags: "Warning: this PO will consume 89% of remaining steel connection budget. Remaining after approval: $3,500. Historical average for this cost code at this project stage: $12,000 remaining. Recommend reviewing with estimator before approval."
>
> The procurement manager reviews and approves, noting that the remaining connections are covered under the steel subcontractor's scope. ProcureGuard sends the PO to the fabricator and receives acknowledgment within 6 hours. Three weeks later, with delivery expected in 4 days, no shipping confirmation has been received. The agent emails the fabricator: "PO-2026-0247: 28 structural steel connections expected delivery March 15. Please confirm shipping status and provide tracking information." The fabricator responds that 22 of 28 pieces are ready to ship, with 6 delayed 5 days due to a galvanizing backlog. ProcureGuard updates the PO status to "Partial Delivery" and alerts the superintendent: "6 steel connections delayed to March 20. Affected areas: Level 3 East Wing. Review construction schedule impact."

---

### Use Case 4: Subcontractor Prequalification & Vendor Database

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Before a subcontractor can bid on a project, most reputable general contractors require prequalification — verifying the sub's financial stability, bonding capacity, safety record (EMR — Experience Modification Rate), licensing, references, and past project experience. This information is collected via lengthy questionnaires (often 10–20 pages), reviewed by procurement and safety teams, and filed... somewhere. When it's time to bid a new project, nobody can quickly answer: "Which qualified mechanical contractors in the Phoenix area can bond a $5M project and have an EMR below 1.0?"

#### The Solution
A Subcontractor Prequalification Database on monday.com. Each item represents a subcontractor with comprehensive columns covering company info, trade classifications, geographic coverage, financial data, bonding capacity, safety metrics (EMR, OSHA recordable rates), licensing, certifications (MBE, WBE, DBE, HUBZone, Veteran-Owned), insurance status, and performance ratings from past projects. Intake forms allow subcontractors to self-register and submit prequalification data. Status tracks from Application → Under Review → Conditionally Approved → Fully Qualified → Suspended → Disqualified.

#### The Outcome
Prequalification review time reduced from 2–3 hours per subcontractor to 30 minutes through standardized intake and automated scoring. Bid invitation lists generated in minutes instead of hours. 25% increase in qualified bidder pool through proactive outreach to diverse and emerging contractors. Complete audit trail for prequalification decisions — critical for government contract compliance.

#### Discovery Questions
1. "How many subcontractors are in your current database, and how do you maintain it?"
2. "What's your prequalification process — is it standardized, or does it vary by project or project manager?"
3. "How do you currently find new subcontractors when you need to expand your bidder pool for a specific trade or geography?"
4. "Do you track subcontractor safety metrics (EMR, incident rates) as part of your prequalification?"
5. "Are diversity goals (MBE/WBE/DBE participation) a factor in your subcontractor selection? If so, how do you track them?"

#### Industry Context
The EMR (Experience Modification Rate) is the construction industry's primary safety metric for prequalification. An EMR below 1.0 indicates better-than-average safety performance; above 1.0 indicates worse. Many GCs won't prequalify a subcontractor with an EMR above 1.2. On government projects, disadvantaged business enterprise (DBE) participation goals (typically 10–30% of contract value) require the GC to document outreach and utilization of certified diverse subcontractors.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Subcontractor Prequalification Database board. Columns: Company Name (text), Primary Trade (dropdown: same CSI divisions as Buyout board), Secondary Trades (dropdown - multi-select), Geographic Coverage (dropdown multi-select: Northeast, Southeast, Midwest, Southwest, West, Pacific Northwest, National), Primary Contact (text), Phone (phone), Email (email), Years in Business (numbers), Annual Revenue Range (dropdown: <$1M, $1M-$5M, $5M-$10M, $10M-$25M, $25M-$50M, $50M-$100M, $100M+), Bonding Capacity - Single (numbers with $ prefix), Bonding Capacity - Aggregate (numbers with $ prefix), EMR - Current Year (numbers), EMR - Prior Year (numbers), OSHA Recordable Rate (numbers), Licenses (text), License Expiration (date), Diversity Certifications (dropdown multi-select: MBE, WBE, DBE, HUBZone, SDVOSB, 8(a), None), Union/Non-Union (dropdown: Union, Non-Union, Both), Qualification Status (status: Application Received, Under Review, Conditionally Qualified, Fully Qualified, Probation, Suspended, Disqualified), COI Status (connect board to COI Tracker), Last Qualified Date (date), Requalification Due (date), Performance Rating (rating 1-5), Number of Projects Completed (numbers), References (long text), Prequalification Documents (file), Notes (long text), Qualification Score (numbers - calculated composite). Add automations: when Requalification Due date is 60 days away email the subcontractor with renewal form link; when EMR Current Year exceeds 1.2 change Status to Under Review and notify Safety Director; when new application received via form assign to Prequalification Reviewer. Create a Dashboard: total qualified subs by trade (bar chart), qualification status distribution (pie chart), average EMR by trade (chart), diversity certification breakdown (pie chart), and subs requiring requalification in next 90 days (table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SubQual Analyzer

**Agent Purpose:** Score and prioritize subcontractor prequalification applications, maintain the qualified vendor database, and match qualified subs to bid opportunities.

**Triggers:**
- New prequalification application submitted via form
- EMR or financial data updated on an existing subcontractor record
- New trade package created on any project's Buyout Tracker board
- Requalification due date approaching (90 days)
- Annual requalification cycle (January)

**Actions:**
- Score prequalification applications using weighted criteria: financial stability (25%), safety record (25%), bonding capacity (20%), experience relevance (15%), references (10%), diversity certification (5%)
- Auto-generate a qualification summary report with risk flags for reviewer
- When a new trade package is created, query the database and generate a ranked list of qualified bidders for that trade, location, and project size
- Monitor EMR changes: if a qualified sub's EMR exceeds threshold, trigger requalification review
- Send annual requalification reminders with pre-populated forms showing last year's data for update
- Track diversity participation across projects and flag when DBE goals are at risk

**Data Required:**
- Prequalification application data
- Historical project performance records
- Financial statements (or Dun & Bradstreet data)
- OSHA safety data and EMR history
- Diversity certification databases (state/federal)
- Project requirements (bonding minimums, safety requirements, diversity goals)

**Autonomy Level:** Human-in-the-Loop
Auto-scores and generates recommendations, but all qualification decisions require procurement manager approval. Auto-generates bidder lists but procurement manager finalizes invitations. Disqualification recommendations require VP approval.

**Example Interaction:**
> A new prequalification application arrives from Apex Mechanical Systems, a mid-size HVAC contractor in Georgia. SubQual Analyzer processes the submission: 12 years in business ✓, $18M annual revenue ✓, $8M single-project bonding ✓, EMR 0.87 ✓ (below 1.0 — strong safety), 3 completed projects over $5M ✓, OSHA recordable rate 2.1 ✓ (below industry average of 3.0), licensed in GA/FL/SC/NC ✓, no diversity certifications noted.
>
> The agent generates a composite score of 84/100 and a summary: "Apex Mechanical Systems — recommended for CONDITIONAL QUALIFICATION. Strengths: strong safety record, adequate bonding, relevant experience. Flags: (1) No financial statements provided — request CPA-reviewed financials for projects above $3M, (2) References list only 2 of 3 required contacts — request third reference. Upon resolution, recommend FULL QUALIFICATION for HVAC projects up to $8M in the Southeast region." It assigns the application to the prequalification reviewer with the summary attached.

---

### Use Case 5: Long-Lead Item Tracking & Procurement Schedule

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
In construction, certain materials and equipment have lead times measured in months, not weeks: custom curtain wall systems (16–24 weeks), electrical switchgear (20–30 weeks), elevators (26–40 weeks), structural steel (12–20 weeks), custom millwork (10–16 weeks). If procurement doesn't identify and order these items early enough, the entire construction schedule slips. The cost of a one-week project delay on a $50M commercial building can exceed $100K in carrying costs, liquidated damages, and lost revenue. Yet many firms identify long-lead items informally — the experienced project manager remembers, but the new one doesn't.

#### The Solution
A Long-Lead Item Tracker on monday.com connected to the project schedule. Items represent materials or equipment with lead times exceeding a threshold (e.g., 8 weeks). Columns track item, specification section, estimated lead time, required on-site date (from construction schedule), order-by date (calculated: on-site date minus lead time minus buffer), vendor, status, and dependencies. Timeline views align procurement milestones with construction milestones. Automations alert procurement when order-by dates are approaching and escalate when they're missed.

#### The Outcome
Zero schedule delays attributable to late material procurement (vs. industry average: 25% of delays are material-related). Procurement starts 8–12 weeks earlier on critical items. Project managers have complete visibility into long-lead procurement status without asking procurement for updates.

#### Discovery Questions
1. "How do you currently identify long-lead items at the start of a project — is it a formal process or does it rely on experience?"
2. "Have you ever had a project delayed because a long-lead item was ordered too late?"
3. "What are the top 5 materials or equipment that consistently have the longest lead times in your projects?"
4. "How do you coordinate between the project schedule and procurement timing — is it integrated or manual?"
5. "When commodity lead times spike unexpectedly (as they did during COVID supply chain disruptions), how quickly does your team adapt?"

#### Industry Context
Post-COVID, construction lead times remain elevated and volatile. Electrical transformers that previously took 12 weeks now take 40–52 weeks. HVAC equipment lead times have doubled. Firms that systematically track and communicate lead times gain a significant competitive advantage — they deliver projects on time while competitors explain delays. The AGC (Associated General Contractors) publishes quarterly construction outlook surveys that track material availability and lead time trends.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Long-Lead Item Tracker board for a construction company. Columns: Project (connect board to Projects Master), Item Name (text), Specification Section (text, e.g., 08 44 13 - Glazed Curtain Wall), Category (dropdown: Structural Steel, Curtain Wall/Glazing, Elevators/Escalators, Electrical Switchgear, Transformers, Generators, HVAC Equipment, Fire Suppression, Custom Millwork, Specialty Doors, Specialty Flooring, Kitchen Equipment, AV Equipment, Custom Fixtures), Vendor/Manufacturer (text), Estimated Lead Time - Weeks (numbers), Required On-Site Date (date), Buffer - Weeks (numbers, default 2), Order-By Date (formula: Required On-Site Date minus Lead Time Weeks minus Buffer Weeks — convert to date), Submittal Required (checkbox), Submittal Status (status: Not Started, In Preparation, Submitted, Under Review, Approved, Approved as Noted, Revise & Resubmit), Shop Drawing Status (status: same options), PO Status (connect board to PO Tracker), Procurement Status (status: Identified, Submittal Phase, Ready to Order, Ordered, In Production, Shipped, Received, Installed), Estimated Cost (numbers with $ prefix), Actual Cost (numbers with $ prefix), Risk Level (status: Low - On Track, Medium - Watch, High - At Risk, Critical - Delayed), Responsible PM (people), Notes (long text). Add automations: when Order-By Date is 14 days away and Procurement Status is still Identified or Submittal Phase, escalate to Procurement Manager and Project Manager; when Procurement Status changes to Ordered record the date; when Required On-Site Date is 30 days away and Procurement Status is not Shipped or later, set Risk Level to High. Create a Timeline view showing order-by dates and on-site dates on the same timeline as construction milestones. Dashboard with: items by risk level (pie chart), items by procurement status (bar chart), upcoming order-by dates in next 30 days (table), and delayed items (filtered table)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** LeadTime Oracle

**Agent Purpose:** Predict and monitor material lead times, identify procurement risks before they impact the schedule, and maintain a living lead-time intelligence database.

**Triggers:**
- New project created on Projects Master board (kicks off long-lead identification)
- Construction schedule milestone dates updated
- Order-By Date within 21 days with item not yet ordered
- Vendor provides updated lead time that differs from estimate by > 2 weeks
- Weekly market intelligence scan for supply chain alerts

**Actions:**
- At project kickoff, scan specifications and auto-generate a preliminary long-lead item list based on historical lead time data
- Calculate order-by dates using current market lead times (not just specification estimates) and flag aggressive schedules
- Monitor supply chain news (steel tariffs, port delays, manufacturer shutdowns) and alert procurement when relevant items may be affected
- When a vendor provides a lead time longer than estimated, recalculate the schedule impact and notify the project manager with options: expedite (cost?), resequence work, or accept delay
- Maintain a lead-time intelligence database: actual lead times by item category, vendor, and region — updated with every project's data
- Generate monthly "Supply Chain Risk Report" for leadership showing items at risk across all projects

**Data Required:**
- Project specifications and schedules
- Historical lead time data by item category and vendor
- Supply chain news feeds and industry publications (AGC, ENR, supply chain alerts)
- Vendor communication logs with quoted lead times
- Market pricing indexes for key materials (steel, copper, lumber)

**Autonomy Level:** Fully Autonomous
All monitoring, alerting, and reporting is automated. The agent does not place orders or commit to vendors — it surfaces intelligence and recommendations for procurement team action.

**Example Interaction:**
> A new 12-story office building project is created. LeadTime Oracle scans the specifications and identifies 23 potential long-lead items. It cross-references with its lead time database: "Based on current market conditions (Q1 2026), the following 5 items are CRITICAL PATH: (1) Electrical switchgear — current lead time: 28 weeks — must order by March 15 for October 1 need-date; (2) Passenger elevators (3 units) — current lead time: 36 weeks — must order by February 28 for November 15 need-date ⚠️ ORDER-BY DATE IN 9 DAYS; (3) Curtain wall system — current lead time: 22 weeks — must order by April 10..."
>
> The agent immediately escalates the elevator procurement: "URGENT: Elevator order-by date is February 28 (9 days). Current status: submittal still in architect review. If submittal approval takes the typical 10 business days, the order-by date will be missed by 1 week, delaying elevator installation by 1 week and potentially impacting substantial completion. Recommendation: (1) Contact architect to expedite elevator submittal review (target: 5 business days), (2) Contact elevator manufacturers to confirm current lead time and explore expediting options, (3) If submittal cannot be expedited, evaluate resequencing interior finishes on floors 9-12 to absorb 1-week delay."

---

### Use Case 6: Submittal & Shop Drawing Management

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Before most construction materials can be ordered, the contractor must submit product data, shop drawings, and samples to the architect/engineer for approval — a process called "submittals." A typical commercial project has 300–800 submittals, each requiring preparation, transmission, architect review (typically 10–15 business days), response tracking, and resubmission if rejected. Procurement can't issue POs until submittals are approved. Managing this in spreadsheets and email means lost submittals, missed resubmission deadlines, and procurement delays that cascade into schedule delays.

#### The Solution
A Submittal Log on monday.com tracking every submittal from specification identification through final approval. Items represent individual submittals with columns for spec section, description, subcontractor/vendor, required date, submitted date, architect response (Approved / Approved as Noted / Revise & Resubmit / Rejected), response date, review duration, resubmission tracking, and linked PO. Automations remind the architect's office when review is overdue, notify the subcontractor when revisions are needed, and alert procurement when approvals are received so POs can be issued.

#### The Outcome
Architect review turnaround improved by 20% through automated follow-up (architects' offices respond faster when reminded consistently). Zero "lost" submittals. Procurement issues POs within 48 hours of submittal approval vs. previous 1–2 week lag. Complete submittal log for project closeout documentation.

#### Discovery Questions
1. "How many submittals does a typical project generate, and who manages the submittal log?"
2. "What's your average architect review turnaround time, and does it meet your expectations?"
3. "How do you currently track resubmissions — do you know how many submittals are on their second or third review cycle?"
4. "Has a delayed submittal ever held up a material order that impacted your construction schedule?"
5. "Do you use Procore or another platform for submittals, or is it managed in-house?"

#### Industry Context
Submittals are governed by the project specifications (typically CSI Section 01 33 00 — Submittal Procedures). The architect's review is a contractual obligation with defined turnaround times (typically 10–15 business days per AIA A201 General Conditions). "Revise and Resubmit" (R&R) responses restart the clock, potentially adding weeks to the procurement timeline. On large projects, a dedicated submittal coordinator may manage this full-time. The submittal log is a contractual document that becomes part of the project record.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Submittal Log board for construction procurement. Columns: Submittal Number (text, auto-format: SUB-001), Project (connect board to Projects Master), Spec Section (text, e.g., 09 65 00), Spec Section Title (text, e.g., Resilient Flooring), Description (text), Submittal Type (dropdown: Product Data, Shop Drawings, Samples, Mock-Up, Test Reports, Certificates, Design Data, Manufacturer Instructions), Responsible Subcontractor (connect board to Sub Database), Required By Date (date), Date Submitted to Architect (date), Architect Response (status: Pending Review, Approved, Approved as Noted, Revise & Resubmit, Rejected, Not Required), Architect Response Date (date), Review Duration - Days (formula: Response Date - Submitted Date), Resubmission Number (numbers, default 0), Resubmission Date (date), Final Approval Date (date), Linked PO (connect board to PO Tracker), Procurement Status (status: Awaiting Submittal, Submittal In Review, Approved - Ready to Order, Ordered), Priority (status: Critical Path, High, Normal, Low), Submittal Document (file), Architect Markups (file), Notes (long text). Add automations: when Date Submitted is 15+ business days ago and Architect Response is Pending Review, send follow-up email to architect contact; when Architect Response changes to Approved or Approved as Noted, notify Procurement Manager 'Submittal approved — ready to issue PO'; when Architect Response is Revise & Resubmit, notify Responsible Subcontractor with markup file; when Priority is Critical Path and review exceeds 10 days, escalate to Project Manager. Create Dashboard: submittals by response status (pie chart), average review duration trend (line chart), overdue reviews (table), critical path submittals (filtered table), and resubmission rate (percentage widget)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SubmittalFlow Manager

**Agent Purpose:** Orchestrate the submittal process from specification identification through final approval, ensuring zero missed deadlines and seamless handoff to procurement.

**Triggers:**
- Project specifications uploaded (generate initial submittal list)
- Subcontractor assigned to a trade (assign submittal responsibility)
- Submittal document uploaded by subcontractor
- Architect response received
- Review duration exceeds contractual limit (10 or 15 business days)
- Submittal approved — trigger procurement action

**Actions:**
- Parse project specifications to generate preliminary submittal register (list of required submittals by spec section)
- Assign submittal preparation responsibility to subcontractors based on trade package assignments
- When subcontractor uploads a submittal, auto-package it with required coversheet (project name, spec section, contractor info) and transmit to architect
- Track review duration and send polite follow-up at day 10, firm follow-up at day 15, escalation to project manager at day 20
- When "Revise & Resubmit" received, extract architect's comments from markup, generate a clear revision checklist for the subcontractor, and set a 5-business-day resubmission deadline
- Upon final approval, immediately notify procurement team and update the linked long-lead item or PO tracker

**Data Required:**
- Project specifications (for submittal register generation)
- Architect/engineer contact information and contractual review periods
- Subcontractor assignments by trade
- Submittal coversheet templates
- Connected boards: PO Tracker, Long-Lead Item Tracker

**Autonomy Level:** Escalation-Based
Auto-transmits submittals and sends follow-ups. Escalates to project manager when review periods are exceeded by 5+ business days. Does not make submittal content decisions — only manages the process workflow.

**Example Interaction:**
> GreenLeaf Flooring, the resilient flooring subcontractor for the Meridian Heights project, uploads their product data submittal for Spec Section 09 65 00 (luxury vinyl tile). SubmittalFlow Manager auto-generates the coversheet, assigns submittal number SUB-247, packages it as a PDF, and transmits it to the architect's office (Thompson Design Associates) with a tracking link.
>
> Ten business days pass with no response. The agent sends a polite follow-up: "Reminder: Submittal SUB-247 (Resilient Flooring, Spec 09 65 00) for Meridian Heights was submitted February 5. Contractual review period: 10 business days. Please provide your review at your earliest convenience." On day 15, a firmer follow-up goes out. On day 17, the architect responds: "Approved as Noted — see markup for color selection clarification."
>
> The agent immediately updates the board, attaches the markup, notifies the procurement manager ("SUB-247 approved — LVT product data approved as noted. Ready to issue PO to GreenLeaf Flooring. Architect note: confirm color 'Weathered Oak 4523' availability before ordering"), and updates the Long-Lead Item Tracker to show the submittal phase is complete for this item.

---

### Use Case 7: Vendor Performance Scorecard & Strategic Sourcing

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Construction firms make millions of dollars in purchasing decisions each year based on relationships, habit, and price — but rarely on data. When a subcontractor delivers late, provides poor quality, or is difficult to work with, that information lives in the project manager's head, not in a system. The next project manager invites the same underperforming sub because they don't know better. Conversely, high-performing vendors don't get rewarded with more work because nobody tracks their excellence systematically.

#### The Solution
A Vendor Performance Scorecard system on monday.com that aggregates data from other procurement boards (PO Tracker, Buyout Tracker, COI Tracker, Submittal Log). At project closeout (or periodically), project managers rate vendors on delivery timeliness, quality, safety, responsiveness, and change order management. These scores aggregate into an overall vendor rating visible on the Subcontractor Database. Dashboards show top performers, underperformers, and trends.

#### The Outcome
Data-driven vendor selection improves project outcomes: firms using performance scorecards report 15% fewer quality issues and 20% fewer schedule delays attributable to subcontractors. High-performing vendors receive more bid invitations, strengthening the relationship. Underperformers are identified and managed proactively — before the next project repeats the same problems.

#### Discovery Questions
1. "When a subcontractor performs poorly on a project, how does that information reach the person inviting them to bid on the next project?"
2. "Do you have a formal vendor rating system, or is it based on institutional knowledge?"
3. "How do you reward your best-performing subcontractors and vendors?"
4. "At project closeout, do you conduct a formal review of vendor performance?"
5. "If I asked you to rank your top 3 and bottom 3 subcontractors by trade, could you do it with data — or would it be gut feel?"

#### Industry Context
In construction, the GC-subcontractor relationship is symbiotic but often adversarial. Good subcontractors are scarce — in a hot market, subs choose which GCs to work with. Data showing that a GC values performance (and rewards it with preferred bidder status) is a competitive advantage in attracting the best trade partners. Some progressive firms are moving toward "strategic sourcing" models borrowed from manufacturing, where long-term relationships replace project-by-project bidding for certain trades.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Vendor Performance Scorecard board. Columns: Vendor/Subcontractor (connect board to Sub Database), Project (connect board to Projects Master), Trade (mirror from Sub Database), Evaluation Period (dropdown: Project Closeout, Annual Review, Incident-Based), Evaluator (people), Evaluation Date (date), Delivery Timeliness (rating 1-5), Quality of Work (rating 1-5), Safety Performance (rating 1-5), Responsiveness/Communication (rating 1-5), Change Order Management (rating 1-5), Punch List Performance (rating 1-5), Overall Score (formula: average of all ratings), Recommendation (status: Preferred Vendor, Approved, Conditional, Probation, Do Not Use), Strengths (long text), Improvement Areas (long text), Incidents/Issues (long text), Supporting Documentation (file). Add automations: when Overall Score < 2.5 notify Procurement Director; when Overall Score > 4.5 update Sub Database record to 'Preferred' status; at project substantial completion create new scorecard items for all active subcontractors on that project. Create Dashboard: average vendor score by trade (bar chart), score distribution (histogram), top 10 vendors (table sorted by score), vendors on probation or Do Not Use (filtered table), and score trends over time for repeat vendors (line chart)."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** VendorIQ Analyst

**Agent Purpose:** Aggregate vendor performance data from across all procurement systems, generate actionable insights, and recommend vendor strategies for upcoming projects.

**Triggers:**
- Project reaches Substantial Completion milestone
- Vendor delivery variance exceeds 5 days (PO Tracker data)
- Quality issue or safety incident logged against a vendor
- New project entering buyout phase (bidder list recommendation)
- Quarterly vendor strategy review cycle

**Actions:**
- Auto-generate project closeout scorecard pre-populated with objective data: delivery on-time rate (from PO Tracker), change order count (from project board), safety incidents (from safety board), submittal resubmission rate (from Submittal Log), COI compliance history (from COI Tracker)
- Send scorecard to project manager for subjective ratings (quality, responsiveness, overall)
- Aggregate scores across projects to maintain a running vendor rating — weighted by project size and recency
- When a new project enters buyout, generate a "Recommended Bidders" report for each trade based on composite vendor scores, availability, and project match
- Identify vendors trending downward (3 consecutive declining scores) and recommend procurement manager intervention
- Generate quarterly "Vendor Strategy Report": top performers to deepen relationships with, underperformers requiring corrective action, and market gaps where the firm needs to develop new vendor relationships

**Data Required:**
- All procurement boards: PO Tracker, Buyout Tracker, COI Tracker, Submittal Log
- Safety incident records
- Change order data
- Project schedules and milestones
- Subcontractor Database

**Autonomy Level:** Fully Autonomous
All data aggregation and reporting is automated. Recommendations are advisory — procurement leadership makes all vendor qualification decisions. The agent never communicates directly with vendors about performance ratings.

**Example Interaction:**
> The Meridian Heights project reaches Substantial Completion. VendorIQ Analyst auto-generates scorecards for all 34 subcontractors on the project, pre-populated with data: "Delta Plumbing — Delivery On-Time Rate: 92% (11 of 12 deliveries on time), Change Orders: 2 ($18,500 — 1.2% of contract), Safety Incidents: 0, Submittal Resubmissions: 1 of 4 submittals required resubmission, COI Compliance: 100% current." It sends this to the PM for subjective ratings.
>
> After collecting all 34 scorecards, the agent generates a project summary: "Top Performers: Delta Plumbing (4.6/5), Apex Mechanical (4.5/5), Summit Electrical (4.4/5). Underperformers: Pacific Drywall (2.3/5 — chronic quality issues, 3 punchlist callbacks), Metro Painting (2.8/5 — 4 late deliveries, unresponsive to schedule changes). Recommendation: Add Delta and Apex to Preferred Vendor list. Place Pacific Drywall on Probation with mandatory improvement plan before next bid invitation."

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Trade Buyout | Process of soliciting and awarding subcontracts for each trade/discipline on a construction project |
| CSI MasterFormat | Standardized numbering system for organizing construction specifications into 50 divisions |
| Bid Tab (Bid Tabulation) | Side-by-side comparison spreadsheet of all bids received for a trade package |
| COI (Certificate of Insurance) | Document proving a contractor carries required insurance coverage |
| EMR (Experience Modification Rate) | Safety metric comparing a contractor's workers' comp claims to industry average; below 1.0 = better than average |
| Submittal | Product data, shop drawings, or samples sent to the architect for approval before procurement |
| Shop Drawings | Detailed fabrication drawings prepared by a subcontractor or manufacturer for architect review |
| Long-Lead Item | Material or equipment requiring extended ordering lead time (typically 8+ weeks) |
| Liquidated Damages (LDs) | Contractually agreed daily penalty for late project completion |
| AIA A201 | Standard form of General Conditions for construction contracts |
| Davis-Bacon Act | Federal law requiring prevailing wage rates on government-funded construction projects |
| Buy American / Buy America | Federal requirements that materials on government projects be domestically manufactured |
| EPD (Environmental Product Declaration) | Document reporting the environmental impact of a building material (required for LEED) |
| Prevailing Wage | Government-mandated minimum wage rates for construction workers by trade and region |
| Performance Bond | Surety bond guaranteeing a subcontractor will complete their work per contract terms |
| Payment Bond | Surety bond guaranteeing a subcontractor will pay their suppliers and workers |
| OCIP/CCIP | Owner or Contractor Controlled Insurance Programs — consolidated insurance for entire project |
| GMP (Guaranteed Maximum Price) | Contract type where the contractor guarantees the project won't exceed a set price |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Procurement Officer / VP of Procurement | Strategic procurement direction, vendor relationships, policy | Decision-maker for tools and process |
| Procurement Manager | Day-to-day procurement operations, buyout management, PO approval | Primary user and champion |
| Purchasing Agent / Buyer | Material POs, vendor communication, delivery tracking | Heavy daily user |
| Estimator / Preconstruction Manager | Creates budgets and scopes that procurement executes against | Influencer — defines what needs to be bought |
| Project Manager | Owns project delivery including procurement timeline alignment | Influencer — drives urgency and priorities |
| CFO / Controller | Financial controls, budget authorization, payment processing | Decision-maker for spend thresholds |
| Risk Manager | Insurance and bonding compliance, safety prequalification | Influencer — defines compliance requirements |
| Superintendent | On-site material receiving, quality verification | End user — receives what procurement orders |
| Subcontractor / Vendor | Provides bids, materials, and services | External stakeholder managed through procurement |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Project Management | Procurement serves project schedules; PM provides need-dates and priorities | Integrated project boards with procurement milestones |
| Estimating / Preconstruction | Creates the budgets and scopes that procurement buys against | Connected budget-to-actuals tracking |
| Finance / Accounting | Processes PO payments, manages cash flow against procurement commitments | PO-to-invoice matching, cash flow forecasting |
| Safety | Defines subcontractor safety requirements (EMR, training, site-specific plans) | Safety prequalification integration |
| Legal | Reviews subcontracts, manages disputes, oversees bonding | Contract management workflow |
| Field Operations | Receives materials, verifies quality, manages subcontractor work | Receiving confirmation and quality tracking |
| Creative & Design | Needs procurement for print vendors, signage fabricators | Vendor management for creative suppliers |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Procore | Construction PM with procurement module (bid management, invoicing) | Procore's procurement features are basic — bid management without strategic sourcing, vendor performance, or long-lead tracking. monday.com offers deeper procurement workflow |
| CMiC / Sage 300 CRE | Construction ERP with procurement/AP | ERPs handle financial transactions but have poor user experience, no visual workflows, and limited collaboration. monday.com layers on top for workflow management |
| PlanHub / BuildingConnected | Bid solicitation platforms for subcontractor procurement | Single-purpose bid tools that don't manage the full procurement lifecycle. monday.com manages bid through delivery through closeout |
| Smartsheet | Spreadsheet-based tracking used by many construction firms | Familiar but limited: no native bid management, no vendor database, weak automations. monday.com offers purpose-built construction procurement workflows |
| Textura (Oracle) | Payment management for construction | Focused narrowly on payment processing, not procurement workflow. Complementary, not competitive |
| Viewpoint Vista | Construction ERP | Similar to CMiC/Sage — strong accounting, weak workflow. monday.com excels at the collaborative, visual procurement management that ERPs lack |
| Excel/Google Sheets | Still the dominant "tool" for construction procurement tracking | The real competitor. monday.com replaces the fragmented spreadsheet ecosystem with a connected, automated, visual system |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Procore for procurement" | "Procore handles bid invitations and invoicing, but what about strategic sourcing, vendor performance tracking, long-lead item management, and COI compliance automation? Our customers use monday.com for the procurement intelligence layer that Procore doesn't provide." |
| "Our ERP handles purchasing" | "Your ERP processes transactions — POs, invoices, payments. But does it help you decide WHICH vendor to use, track their performance, manage submittals, or forecast procurement risks? monday.com adds the strategic procurement workflow layer that complements your ERP." |
| "Procurement in construction is too complex for a platform tool" | "That's exactly why you need a flexible platform. Unlike rigid procurement software, monday.com adapts to YOUR process — whether you're a $50M regional GC or a $500M national builder. We've seen firms build their exact workflow in weeks, not months." |
| "Our procurement people won't learn a new system" | "If they can use Excel, they can use monday.com — it's more intuitive and saves them hours of manual tracking. The biggest win: procurement managers stop spending 40% of their time on status updates and COI chasing, and spend it on strategic sourcing that saves real money." |
| "We don't have budget for another tool" | "What's the cost of one delayed project because a long-lead item was ordered late? Or one uninsured subcontractor incident? Or 3% worse buyout results because you couldn't compare enough bids? monday.com typically pays for itself within 2 projects through procurement savings and risk avoidance." |

## Proof Points
*(To be populated with customer references)*
- [General contractor that improved buyout savings by X% using centralized bid management]
- [Developer that achieved 100% COI compliance across all projects]
- [Builder that reduced long-lead procurement delays to zero]
- [Construction firm that saved $X through vendor performance-driven sourcing]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
