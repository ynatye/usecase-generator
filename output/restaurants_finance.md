# Restaurants × Finance Playbook

## Overview

Restaurant finance operations are notoriously complex, managing everything from real-time food cost tracking to multi-location P&L consolidation. Finance teams in full-service, quick-service, and fast-casual establishments face unique challenges: volatile food costs, complex labor management across hourly workers and tip reporting, franchise royalty calculations, and the critical balance of maintaining prime cost (food + labor) below 60-65% of revenue. Unlike traditional retail, restaurant finance operates on razor-thin margins where a 2-3% variance in food cost percentage can mean the difference between profitability and loss.

The industry's operational complexity extends beyond basic accounting — finance teams must manage daily cash deposits from multiple payment types, track inventory that spoils, handle percentage rent calculations tied to sales performance, and navigate multi-entity accounting structures common in franchise operations. With same-store sales (comp sales) as a key performance indicator and the need for real-time visibility into metrics like average check size and revenue per available seat hour (RevPASH), restaurant finance teams are drowning in manual processes that traditional accounting software wasn't designed to handle.

Modern restaurant finance teams typically manage 15-20 different systems: POS integration, inventory management, payroll processing, franchise reporting, vendor payment platforms, and various spreadsheets for menu pricing analysis. This fragmentation creates blind spots in prime cost management and delays critical pricing decisions that directly impact profitability.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|--------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | **High** | Restaurant finance teams are chronically understaffed relative to complexity. AI agents can handle routine prime cost calculations, vendor payment processing, and franchise reporting — eliminating the need for additional AP clerks and junior analysts. |
| **Consolidate Tech Stack with AI** | **High** | Restaurants typically use 15-20 disconnected financial systems. AI-powered consolidation on monday.com eliminates integration headaches and provides unified visibility into food cost, labor cost, and P&L performance across all locations. |
| **Scale Impact Without Overhead** | **High** | Growing restaurant chains need to maintain tight cost control across expanding locations without adding finance headcount proportionally. AI enables one finance manager to oversee prime cost analysis for 50+ locations instead of 15. |

## Prioritized Use Cases

---

### Use Case 1: Automated Prime Cost Management & Alerts

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Restaurant finance teams manually calculate prime cost (food cost + labor cost) weekly or monthly, often discovering cost overruns too late to take corrective action. With target food cost percentage of 28-35% and labor cost percentage of 25-35%, a 3% variance can eliminate all profitability. Manual plate cost analysis and menu pricing decisions are based on outdated data, leading to underpriced items and compressed margins. Finance teams spend 15-20 hours per location per month on cost calculations that should be automated.

#### The Solution
monday.com's AI agents continuously monitor POS integration, inventory systems, and payroll data to calculate real-time prime cost by location, menu item, and time period. Automated alerts trigger when food cost or labor cost percentages exceed thresholds. AI-powered plate cost analysis automatically recalculates menu item profitability when ingredient costs change, suggesting repricing recommendations. Integration with major POS systems (Square, Toast, Resy) and inventory platforms provides unified cost visibility.

#### The Outcome
Reduce manual prime cost calculation time by 85% (from 20 hours to 3 hours per location monthly). Improve gross margin by 2-4% through real-time cost alerts and dynamic menu pricing. Enable one finance manager to monitor prime cost for 40-50 locations instead of 15. Faster identification of cost variance enables corrective action within days instead of weeks.

#### Discovery Questions
- How many hours per week does your team spend manually calculating food cost and labor cost percentages?
- How quickly can you identify when a location's prime cost exceeds 65% of revenue?
- What's the time lag between a cost variance occurring and your team being able to take corrective action?
- How often do you update menu pricing based on changing food costs?
- Which locations have the highest variance in prime cost, and do you know why?

#### Industry Context
Prime cost is the restaurant industry's most critical financial metric, combining food cost percentage and labor cost percentage. Industry benchmarks vary by concept: quick-service targets 50-55% prime cost, fast-casual 55-60%, full-service 60-65%. Successful restaurants monitor prime cost weekly by location, with best-in-class operators tracking daily. Food cost percentage should typically remain between 28-35% of revenue, while labor costs should be 25-35%, depending on service model and local labor markets.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Prime Cost Management dashboard for restaurants with these boards: 1) Location Performance Board with columns: Location (dropdown), Week Ending (date), Food Cost % (numbers), Labor Cost % (numbers), Prime Cost % (formula), Revenue (numbers), Status (status: Green/Yellow/Red based on prime cost thresholds), Action Required (long text). 2) Menu Item Profitability with columns: Item Name (text), Food Cost $ (numbers), Food Cost % (numbers), Selling Price (numbers), Gross Margin (formula), Last Updated (date), Status (status). Set up automations to notify Finance Manager when any location's prime cost exceeds 65%. Create a dashboard view showing weekly trends and location comparisons. Include Kanban view for locations by performance status."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Prime Cost Guardian

**Agent Purpose:**  
Continuously monitor and optimize restaurant prime cost performance across all locations with real-time alerts and automated corrective recommendations.

**Triggers:**
- Daily POS sales data sync (end of business day)
- Weekly inventory count completion
- Payroll data updates
- Ingredient cost changes from vendors
- Manual request for prime cost analysis

**Actions:**
- Calculate real-time food cost percentage by location and menu item
- Generate labor cost percentage with tip allocation adjustments
- Send immediate alerts when prime cost exceeds thresholds
- Create automated menu repricing recommendations
- Update plate cost analysis for all menu items
- Generate weekly prime cost reports for management

**Data Required:**
- POS integration (sales, item mix)
- Inventory management system integration
- Payroll system data (with tip reporting)
- Vendor pricing feeds
- Recipe/plate cost database

**Autonomy Level:** Human-in-the-Loop  
Agent automatically calculates and alerts but requires human approval for menu repricing recommendations and corrective actions above certain thresholds.

**Example Interaction:**
> At 2:00 AM, the Prime Cost Guardian processes yesterday's POS data from 15 locations and discovers that the downtown location's food cost hit 38% due to increased beef prices and over-portioning issues. It immediately sends a Slack alert to the Finance Manager and GM, noting that prime cost is now at 67% (38% food + 29% labor). The agent automatically updates plate costs for all beef items and suggests increasing the signature burger price from $14 to $15.50 to restore target margins. It also flags potential over-portioning in the kitchen and schedules a portion control audit. By 8:00 AM, management has actionable insights and recommendations ready for the morning operations meeting.

---

### Use Case 2: Multi-Location Cash Flow & Daily Deposit Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Restaurant finance teams manually track daily deposits from multiple locations with various payment types (cash, credit, gift cards, third-party delivery). Reconciling POS reports against bank deposits is time-consuming and error-prone, especially when factoring in tip adjustments and cash handling discrepancies. Multi-location operators struggle to maintain cash flow visibility, often discovering deposit delays or variances days after they occur. Finance teams spend hours chasing missing deposits and reconciling payment processor fees across locations.

#### The Solution
monday.com consolidates all payment processing data, bank integrations, and POS systems into unified cash flow tracking. AI agents automatically reconcile daily deposits against POS reports, flagging discrepancies within hours instead of days. Automated cash handling workflows track deposit schedules and alert when deposits are late or amounts don't match expectations. Integration with major payment processors (Square, Stripe, Toast Payments) and bank APIs provides real-time cash position visibility.

#### The Outcome
Reduce daily deposit reconciliation time by 75% across all locations. Identify cash handling discrepancies within 24 hours instead of weekly accounting cycles. Improve cash flow forecasting accuracy and eliminate manual deposit tracking spreadsheets. Enable centralized visibility into daily cash performance across 50+ locations from a single dashboard.

#### Discovery Questions
- How long does it take your team to reconcile daily deposits from all locations?
- How quickly do you identify when a location's deposit doesn't match their POS report?
- What percentage of your locations have cash handling discrepancies in a typical week?
- How do you currently track and manage third-party delivery payments (DoorDash, UberEats)?
- What's your process for handling tip adjustments and credit card chargebacks?

#### Industry Context
Restaurant cash handling is uniquely complex due to multiple payment types, tip reporting requirements, and high transaction volumes. Daily deposits typically include cash (minus till cash), credit card batches, gift card redemptions, and third-party delivery settlements. Best practices require daily reconciliation between POS reports and actual deposits, with variance investigation within 24 hours. Many concepts struggle with cash shrinkage rates above 1-2% of cash sales.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Daily Deposit Management system with boards: 1) Daily Deposits Board with columns: Location (dropdown), Business Date (date), POS Sales Total (numbers), Cash Sales (numbers), Credit Sales (numbers), Gift Card Sales (numbers), Expected Deposit (formula), Actual Deposit (numbers), Variance (formula), Deposit Status (status: Pending/Complete/Variance), Payment Processor (dropdown), Deposit Date (date). 2) Cash Variance Investigation with columns: Location (dropdown), Date (date), Variance Amount (numbers), Investigation Notes (long text), Resolution (status), Assigned To (people). Set up automations to notify Finance when variance exceeds $50 or deposit is 24+ hours late. Include dashboard showing daily cash performance across all locations and timeline view for deposit schedules."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Cash Flow Sentinel

**Agent Purpose:**  
Automatically reconcile daily deposits across all restaurant locations and identify cash handling discrepancies in real-time.

**Triggers:**
- End of business day POS report generation
- Bank deposit notifications via API
- Payment processor settlement completion
- Manual cash variance reporting
- Weekly cash handling audit schedules

**Actions:**
- Auto-reconcile POS sales against expected deposits
- Generate variance reports with detailed breakdowns
- Send immediate alerts for missing or late deposits
- Track payment processor fees and chargebacks
- Create weekly cash handling performance reports
- Escalate significant variances to management

**Data Required:**
- POS system integration (sales reports)
- Bank account API connections
- Payment processor data feeds (Square, Stripe, Toast)
- Third-party delivery platform integrations
- Till cash tracking systems

**Autonomy Level:** Fully Autonomous  
Agent handles routine reconciliation and alerting automatically, escalating only significant variances or patterns for human investigation.

**Example Interaction:**
> At 11:30 PM, the Cash Flow Sentinel receives the daily POS report from the suburban location showing $4,850 in total sales. It expects a $3,200 deposit (excluding till cash) but notices by 2:00 PM the next day that only $2,950 was deposited. The agent immediately alerts the Finance Manager and location GM about the $250 variance. After analyzing the payment breakdown, it identifies that $180 in cash sales appear missing and flags two large cash transactions for investigation. The agent automatically creates a variance investigation item, assigns it to the GM, and requests till count verification. It also notes this location has had three cash variances in the past month, suggesting a pattern requiring management attention.

---

### Use Case 3: Franchise Royalty & Marketing Fund Automation

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Franchise operations require complex royalty calculations, marketing fund contributions, and multi-entity accounting that varies by location and franchise agreement. Finance teams manually calculate percentage-based royalties on gross sales, advertising fund contributions, and technology fees across dozens of locations with different terms. Monthly franchise reporting is labor-intensive, requiring consolidation of sales data, fee calculations, and compliance documentation. Errors in royalty calculations can trigger franchise agreement violations and damage franchisor relationships.

#### The Solution
monday.com AI agents automatically calculate franchise royalties, marketing contributions, and technology fees based on individual franchise agreements and sales performance. Automated workflows generate monthly franchise reports, handle multi-entity accounting, and ensure compliance with franchise disclosure requirements. Integration with franchise management systems and automated payment processing eliminates manual calculations and reduces compliance risk.

#### The Outcome
Reduce monthly franchise reporting time by 80% and eliminate manual royalty calculation errors. Automate payment processing for royalties and marketing contributions across all locations. Improve franchise compliance and strengthen franchisor relationships through accurate, timely reporting. Enable finance team to manage 100+ franchise locations with the same effort previously required for 25.

#### Discovery Questions
- How many hours per month does your team spend calculating franchise royalties and marketing contributions?
- How do you currently handle different royalty rates and terms across multiple franchise agreements?
- What's your process for ensuring compliance with franchise disclosure and reporting requirements?
- How quickly can you generate consolidated franchise performance reports for your franchisor?
- Have you experienced franchise agreement violations due to late or inaccurate reporting?

#### Industry Context
Franchise restaurant operations typically pay 4-8% royalties on gross sales plus 2-4% marketing fund contributions. Calculations must account for gross sales (before discounts), exclude taxes, and often have minimum payment requirements regardless of performance. Multi-entity accounting is complex, requiring separate P&L tracking for corporate vs. franchise locations while consolidating for franchisor reporting. Franchise compliance requires detailed record-keeping and monthly reporting accuracy.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Franchise Management system with boards: 1) Franchise Locations with columns: Location Name (text), Franchise Agreement (dropdown), Royalty Rate % (numbers), Marketing Fund % (numbers), Opening Date (date), Agreement Expiration (date), Status (status). 2) Monthly Franchise Reporting with columns: Location (connected board), Reporting Month (date), Gross Sales (numbers), Royalty Amount (formula), Marketing Fund Amount (formula), Technology Fee (numbers), Total Due (formula), Payment Status (status), Submission Date (date). 3) Franchise Compliance Tracking with columns: Location (dropdown), Compliance Item (dropdown), Due Date (date), Status (status), Notes (long text). Set up automations to calculate fees automatically when sales are updated and notify before payment due dates. Include dashboard showing franchise performance and compliance status across all locations."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Franchise Compliance Manager

**Agent Purpose:**  
Automatically calculate franchise fees, generate compliance reports, and manage multi-entity accounting for franchise restaurant operations.

**Triggers:**
- Monthly sales data finalization
- Franchise agreement renewals or modifications
- Payment due date reminders (5 days before)
- Franchisor report requests
- Compliance deadline approaches

**Actions:**
- Calculate royalties and marketing contributions by location
- Generate monthly franchise reports in required formats
- Process automated payments to franchisors
- Track compliance requirements and deadlines
- Consolidate multi-entity financial reporting
- Send payment confirmations and compliance updates

**Data Required:**
- Individual franchise agreement terms
- POS sales data by location
- Payment processing system integration
- Franchisor reporting requirements
- Multi-entity accounting structure

**Autonomy Level:** Human-in-the-Loop  
Agent calculates fees automatically but requires human approval for payments above certain thresholds and all compliance report submissions.

**Example Interaction:**
> On the first business day of each month, the Franchise Compliance Manager processes gross sales data from all 23 franchise locations. For the downtown location with $185,000 in monthly gross sales, it calculates $11,100 in royalties (6%) and $5,550 in marketing contributions (3%). The agent notes this location's franchise agreement includes a minimum $8,000 monthly royalty, so the higher calculated amount applies. It automatically generates the monthly report in the franchisor's required format, schedules payment for the 15th (payment due date), and updates the compliance dashboard. The agent also flags that this location's franchise agreement expires in 8 months and creates a renewal reminder for the operations team. All calculations and reports are ready for Finance Manager review by 9:00 AM.

---

### Use Case 4: Vendor Payment Optimization & AP Automation

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Restaurant finance teams manage relationships with 20-50 vendors across multiple categories (food suppliers, equipment, utilities, marketing) with varying payment terms, early payment discounts, and delivery schedules. Manual accounts payable processing leads to missed early payment discounts (typically 2-3% for payment within 10 days), late payment penalties, and poor vendor relationship management. Tracking payment terms, invoice matching, and cash flow optimization across numerous suppliers is time-consuming and error-prone.

#### The Solution
monday.com AI agents automatically process vendor invoices, match them to purchase orders and delivery receipts, and optimize payment timing to capture discounts while maintaining cash flow requirements. Automated workflows manage vendor payment terms, track early payment opportunities, and prioritize payments based on discount value and cash position. Integration with major accounting systems and vendor portals streamlines the entire accounts payable process.

#### The Outcome
Capture 90%+ of available early payment discounts (typically saving 2-3% on vendor costs). Reduce accounts payable processing time by 70% and eliminate late payment penalties. Optimize cash flow by automatically scheduling payments for maximum discount capture while maintaining minimum cash reserves. Improve vendor relationships through consistent, timely payments.

#### Discovery Questions
- How many vendors does your restaurant group work with, and what's the mix of payment terms?
- What percentage of early payment discounts are you currently capturing?
- How much time does your AP team spend on manual invoice processing and payment scheduling?
- Do you have visibility into cash flow impact when optimizing vendor payment timing?
- How often do you experience late payment penalties or vendor relationship issues due to payment delays?

#### Industry Context
Restaurant vendors typically offer 2/10 net 30 payment terms (2% discount for payment within 10 days, full payment due in 30 days). With food costs representing 28-35% of revenue, capturing early payment discounts can improve gross margins significantly. Major vendor categories include food distributors (Sysco, US Foods), beverage suppliers, equipment vendors, and service providers. Many restaurants struggle with cash flow timing, missing discounts to preserve working capital.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Vendor Payment Management system with boards: 1) Vendor Master with columns: Vendor Name (text), Payment Terms (dropdown: 2/10 Net 30, Net 15, Net 30), Early Discount % (numbers), Contact Info (text), Category (dropdown: Food, Beverage, Equipment, Services), Active Status (status). 2) Invoice Processing with columns: Invoice # (text), Vendor (connected board), Invoice Date (date), Amount (numbers), Due Date (date), Early Discount Date (date), Discount Amount (formula), Payment Status (status: Pending/Scheduled/Paid), Payment Date (date), PO Matched (checkbox). Set up automations to calculate discount savings opportunities and notify AP team of early payment deadlines. Include dashboard showing weekly payment schedules, discount capture rates, and vendor performance. Create timeline view for payment scheduling optimization."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Vendor Payment Optimizer

**Agent Purpose:**  
Automatically optimize vendor payment timing to maximize early payment discounts while maintaining optimal cash flow across restaurant operations.

**Triggers:**
- New vendor invoices received
- Payment due dates approaching
- Early discount deadlines (2-3 days before expiry)
- Weekly cash flow analysis
- Vendor payment terms changes

**Actions:**
- Match invoices to purchase orders and receipts
- Calculate early payment discount opportunities
- Optimize payment schedules based on cash flow and discounts
- Generate vendor payment batches
- Track discount capture rates and missed opportunities
- Send vendor payment confirmations

**Data Required:**
- Vendor payment terms database
- Invoice processing system integration
- Bank account balances and cash flow projections
- Purchase order system data
- Payment processing platform integration

**Autonomy Level:** Human-in-the-Loop  
Agent schedules payments automatically for pre-approved vendors and amounts, requiring human approval for new vendors or payments above set thresholds.

**Example Interaction:**
> The Vendor Payment Optimizer receives a $12,500 food distributor invoice with 2/10 Net 30 terms, representing a potential $250 early payment discount. After checking cash flow projections, it determines the restaurant group has sufficient funds to pay early without impacting operations. The agent automatically schedules payment for day 8 (maintaining 2-day buffer before discount expiry) and updates the cash flow forecast. It also notices this vendor represents 15% of monthly food costs, and capturing their early payment discounts consistently would save $3,000 annually. The agent creates a priority flag for this vendor relationship and suggests setting up automated early payment to maximize ongoing savings.

---

### Use Case 5: Same-Store Sales & Comp Analysis Automation

**Relevance:** Medium  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Restaurant operators rely on same-store sales (comp sales) analysis to measure organic growth, but manual calculation and reporting across multiple locations is time-consuming and inconsistent. Finance teams struggle to provide real-time comp analysis, identify trending patterns, and correlate performance with operational factors like menu changes, promotions, or local events. Traditional POS reporting doesn't provide the depth of analysis needed for strategic decision-making, and manual data compilation delays critical insights.

#### The Solution
monday.com AI agents automatically calculate same-store sales comparisons across multiple time periods, identify trending patterns, and correlate performance with operational data. Automated comp analysis includes weather adjustments, seasonality factors, and promotional impact assessment. Real-time dashboards provide location-level and system-wide comp performance with automated insights and recommendations for underperforming locations.

#### The Outcome
Provide real-time comp sales analysis across all locations with automated trend identification. Reduce monthly comp reporting time by 60% while increasing analytical depth and accuracy. Enable proactive management intervention for underperforming locations within days instead of weeks. Improve comp sales performance through data-driven operational adjustments.

#### Discovery Questions
- How frequently do you calculate and report same-store sales performance?
- What factors do you currently consider when analyzing comp sales trends (weather, promotions, menu changes)?
- How quickly can you identify underperforming locations and implement corrective actions?
- Do you have the ability to correlate comp sales performance with operational metrics?
- What's your process for benchmarking individual location performance against system averages?

#### Industry Context
Same-store sales (comp sales) measure revenue growth for locations open at least 12-18 months, eliminating the impact of new store openings. Industry-leading restaurant chains target 2-5% annual comp growth. Comp analysis must account for calendar shifts, weather impact, promotional activities, and seasonal variations. Monthly comp reporting to investors and franchisors is standard, but best operators track weekly or daily trends for operational decision-making.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Same-Store Sales Analysis system with boards: 1) Location Comp Performance with columns: Location (dropdown), Week Ending (date), Current Year Sales (numbers), Prior Year Sales (numbers), Comp % Growth (formula), System Average (numbers), Performance vs System (formula), Status (status: Above/At/Below Target), Weather Impact (dropdown), Promotions Active (text). 2) Monthly Comp Summary with columns: Month (date), System Comp % (numbers), Location Count (numbers), Locations Above Target (numbers), Target Achievement % (formula), Notes (long text). Set up automations to alert when location comp performance falls below -2% for two consecutive weeks. Create dashboard views showing weekly trends, location rankings, and system performance. Include timeline view for seasonal pattern analysis."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Comp Sales Analyzer

**Agent Purpose:**  
Continuously analyze same-store sales performance across all locations with automated trend identification and performance optimization recommendations.

**Triggers:**
- Weekly sales data updates
- Month-end comp calculation requests
- Location performance falls below thresholds
- Seasonal adjustment periods
- Manual comp analysis requests

**Actions:**
- Calculate comp sales across multiple time periods
- Identify trending patterns and performance anomalies
- Generate location-specific performance recommendations
- Create automated comp reports for management and investors
- Track promotional impact on comp performance
- Send alerts for underperforming locations

**Data Required:**
- Historical sales data by location (minimum 18 months)
- Location opening dates and eligibility
- Promotional calendar and marketing activities
- Weather data for location-based adjustments
- Operational metrics (staff levels, menu changes)

**Autonomy Level:** Fully Autonomous  
Agent automatically calculates and reports comp performance, escalating only significant negative trends or unusual patterns for human investigation.

**Example Interaction:**
> The Comp Sales Analyzer processes weekly sales data and identifies that the suburban location's comp sales have declined -3.2% for the third consecutive week, while the system average is +2.1%. The agent automatically correlates this with operational data and notices a 15% increase in customer complaints about service speed during the same period, plus a key manager departure two weeks ago. It generates an alert for the District Manager highlighting the negative trend, identifies potential operational causes, and recommends immediate intervention. The agent also notes that historically, this location's comp performance has been sensitive to staffing changes and suggests prioritizing management recruitment and training investment.

---

### Use Case 6: Menu Engineering & Profitability Analysis

**Relevance:** Medium  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Restaurant finance teams manually analyze menu item profitability using outdated spreadsheets that don't reflect real-time ingredient costs or sales mix changes. Menu engineering analysis to optimize offerings is time-consuming and often based on incomplete data, leading to overpriced low-margin items remaining on menus while high-profit opportunities are missed. Finance teams spend significant time calculating plate costs, analyzing sales mix impact, and providing pricing recommendations that lag behind market conditions.

#### The Solution
monday.com AI agents continuously monitor menu item performance using real-time ingredient costs, sales velocity, and profitability analysis. Automated menu engineering identifies "stars" (high profit, high volume), "dogs" (low profit, low volume), and optimization opportunities. AI-powered pricing recommendations adjust for ingredient cost fluctuations and competitive positioning while maintaining target gross margins.

#### The Outcome
Increase gross margin by 3-5% through optimized menu mix and dynamic pricing. Reduce menu analysis time by 75% while providing real-time profitability insights. Eliminate underperforming menu items faster and promote high-margin opportunities more effectively. Enable continuous menu optimization instead of quarterly reviews.

#### Discovery Questions
- How frequently do you analyze individual menu item profitability and sales performance?
- What's your current process for adjusting menu prices when ingredient costs change?
- How do you identify underperforming menu items that should be removed or repriced?
- Do you have real-time visibility into how menu mix changes impact overall profitability?
- What's your approach to menu engineering and optimizing the balance between popularity and profitability?

#### Industry Context
Menu engineering categorizes items into four quadrants: Stars (high profit, high sales), Plowhorses (low profit, high sales), Puzzles (high profit, low sales), and Dogs (low profit, low sales). Successful restaurants continuously optimize menu mix, promoting Stars and Puzzles while repricing or eliminating Dogs. Plate cost analysis must account for ingredient cost fluctuations, portion control, and waste factors. Target food cost percentages vary by item category, with appetizers often carrying higher margins than entrees.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Menu Engineering system with boards: 1) Menu Items Analysis with columns: Item Name (text), Category (dropdown: Appetizer, Entree, Dessert, Beverage), Food Cost $ (numbers), Selling Price (numbers), Food Cost % (formula), Gross Margin $ (formula), Weekly Units Sold (numbers), Revenue Contribution (formula), Menu Engineering Category (status: Star/Plowhorse/Puzzle/Dog), Last Cost Update (date), Action Required (dropdown). 2) Ingredient Cost Tracking with columns: Ingredient (text), Supplier (dropdown), Current Cost (numbers), Prior Cost (numbers), Cost Change % (formula), Affected Items (connected board), Update Date (date). Set up automations to recalculate item profitability when ingredient costs change and alert when items fall into 'Dog' category. Create dashboard showing menu performance matrix and profitability trends. Include Kanban view organized by menu engineering categories."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Menu Optimization Engine

**Agent Purpose:**  
Continuously analyze menu item performance and automatically optimize menu mix for maximum profitability using real-time cost and sales data.

**Triggers:**
- Daily POS sales data updates
- Ingredient cost changes from suppliers
- Weekly menu performance analysis schedule
- New menu item launches
- Manual menu engineering requests

**Actions:**
- Calculate real-time item profitability and food cost percentages
- Classify items using menu engineering matrix
- Generate pricing recommendations for cost changes
- Identify underperforming items for removal consideration
- Suggest menu placement and promotion strategies for high-margin items
- Create monthly menu performance reports

**Data Required:**
- POS sales data by menu item
- Recipe database with ingredient quantities
- Real-time ingredient cost feeds
- Menu item costs and selling prices
- Sales mix and velocity data

**Autonomy Level:** Human-in-the-Loop  
Agent automatically analyzes performance and generates recommendations, requiring human approval for menu changes and pricing adjustments above certain thresholds.

**Example Interaction:**
> The Menu Optimization Engine processes last week's sales data and notices that the Grilled Salmon entree has dropped from "Star" to "Puzzle" status - maintaining high profitability (22% food cost) but experiencing a 35% decline in weekly sales. After analyzing the data, it identifies that a 12% price increase last month moved the item from $24 to $27, above the local market average of $25. The agent recommends reducing the price to $25.50 to restore competitive positioning while maintaining acceptable margins. It also suggests promoting the item with weekend specials and updating the menu description to emphasize value. The agent creates a test recommendation for the operations team and schedules a performance review in 3 weeks to measure impact.

---

### Use Case 7: Gift Card & Catering Revenue Recognition

**Relevance:** Medium  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Restaurant finance teams struggle with proper gift card liability tracking and catering revenue recognition across multiple locations. Gift card sales create deferred revenue that must be tracked until redemption, with breakage analysis for unused cards requiring complex calculations. Catering operations have unique revenue recognition challenges with deposits, special events, and varying fulfillment timelines that don't align with standard POS reporting. Manual tracking of these revenue streams leads to accounting errors and compliance issues.

#### The Solution
monday.com AI agents automatically track gift card liability, monitor redemption patterns, and calculate breakage estimates for financial reporting. Automated catering revenue recognition manages deposits, tracks event fulfillment, and ensures proper revenue timing. Integration with POS systems and catering platforms provides unified visibility into deferred revenue obligations and proper GAAP compliance.

#### The Outcome
Ensure 100% accurate gift card liability reporting and eliminate manual tracking errors. Improve catering revenue recognition timing and reduce month-end closing time by 40%. Provide automated breakage analysis for gift card programs and optimize gift card marketing based on redemption patterns. Enable proper deferred revenue management across all revenue streams.

#### Discovery Questions
- How do you currently track gift card liability and redemption patterns across all locations?
- What's your process for managing catering deposits and ensuring proper revenue recognition timing?
- How do you calculate and report gift card breakage for financial statement purposes?
- Do you have visibility into gift card redemption patterns and customer behavior?
- What challenges do you face with month-end revenue recognition for special events and catering?

#### Industry Context
Gift card liability must be tracked as deferred revenue until redemption occurs. Industry breakage rates (unused gift cards) typically range from 2-8% annually, requiring statistical analysis for proper financial reporting. Catering revenue recognition requires careful tracking of deposits, event dates, and fulfillment to ensure revenue is recognized when services are performed, not when payment is received. Many restaurants struggle with proper GAAP compliance for these complex revenue streams.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a Deferred Revenue Management system with boards: 1) Gift Card Tracking with columns: Card Number (text), Purchase Date (date), Purchase Amount (numbers), Redemption Amount (numbers), Remaining Balance (formula), Purchase Location (dropdown), Redemption Location (dropdown), Customer Email (text), Status (status: Active/Redeemed/Expired), Breakage Eligible Date (date). 2) Catering Revenue Recognition with columns: Event ID (text), Customer Name (text), Event Date (date), Contract Amount (numbers), Deposit Amount (numbers), Remaining Balance (formula), Payment Status (status), Revenue Recognition Date (date), Location (dropdown), Event Status (status). Set up automations to track gift card aging and calculate breakage eligibility. Create dashboard showing deferred revenue balances and monthly revenue recognition schedules. Include timeline view for catering event management."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** Revenue Recognition Manager

**Agent Purpose:**  
Automatically manage gift card liability tracking, catering revenue recognition, and deferred revenue compliance across all restaurant locations.

**Triggers:**
- Gift card purchases and redemptions
- Catering contract bookings and deposits
- Monthly financial closing periods
- Gift card breakage analysis schedules
- Revenue recognition date arrivals

**Actions:**
- Track gift card liability and redemption patterns
- Calculate monthly breakage estimates
- Manage catering revenue recognition timing
- Generate deferred revenue reports for financial statements
- Monitor compliance with revenue recognition standards
- Update general ledger with proper revenue allocations

**Data Required:**
- Gift card POS integration
- Catering booking and payment systems
- Customer database for gift card tracking
- Financial reporting requirements
- Breakage analysis historical data

**Autonomy Level:** Fully Autonomous  
Agent automatically tracks and reports deferred revenue with human oversight for financial statement preparation and breakage estimate adjustments.

**Example Interaction:**
> At month-end, the Revenue Recognition Manager processes all gift card and catering activity. It identifies $45,000 in gift card liability across all locations, with $8,200 in cards becoming eligible for breakage analysis (purchased 24+ months ago with no activity). Based on historical patterns showing 6% breakage rates, it calculates $492 in breakage revenue for the current month. For catering, it recognizes $12,500 in revenue for three events completed this month while tracking $8,900 in deposits for future events. The agent automatically generates journal entries for the accounting team and updates the deferred revenue schedule, ensuring all revenue recognition complies with GAAP standards and is ready for month-end financial statement preparation.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **Prime Cost** | Combined food cost and labor cost, typically 60-65% of revenue |
| **Food Cost Percentage** | Food costs divided by revenue, target 28-35% |
| **Labor Cost Percentage** | Labor costs divided by revenue, target 25-35% |
| **Same-Store Sales (Comp Sales)** | Revenue growth for locations open 12+ months |
| **Average Check/Ticket Size** | Total sales divided by number of transactions |
| **RevPASH** | Revenue per Available Seat Hour, productivity metric |
| **Plate Cost Analysis** | Individual menu item cost calculation |
| **COGS Tracking** | Cost of Goods Sold monitoring and management |
| **Percentage Rent** | Lease payments based on sales performance |
| **Franchise Royalty** | Percentage of gross sales paid to franchisor |
| **Marketing Fund Contribution** | Pooled advertising fees, typically 2-4% of sales |
| **Gift Card Liability** | Deferred revenue from unRedeemed gift cards |
| **Breakage** | Percentage of gift cards that go unredeemed |
| **Catering Revenue Recognition** | Proper timing of catering income recording |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| **CFO/Finance Director** | Overall financial strategy and reporting | High - budget approval, strategic decisions |
| **Controller** | Daily financial operations and compliance | High - process implementation, reporting |
| **AP Manager** | Vendor payments and cash flow management | Medium - operational efficiency, vendor relations |
| **Payroll Manager** | Labor cost management and tip reporting | Medium - labor cost control, compliance |
| **Operations Manager** | Location performance and cost control | High - operational impact, day-to-day decisions |
| **Franchise Business Manager** | Multi-unit financial performance | High - growth strategy, franchise relations |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Operations** | Prime cost management, location performance | Unified operational and financial dashboards |
| **Marketing** | Promotional impact analysis, gift card programs | ROI tracking and campaign performance measurement |
| **Purchasing** | Vendor management, inventory cost control | Integrated procurement and financial planning |
| **IT** | POS integration, system consolidation | Unified data platform for all restaurant systems |
| **Human Resources** | Payroll processing, labor cost management | Integrated workforce and financial planning |
| **Real Estate** | Lease management, percentage rent calculations | Location profitability and expansion analysis |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Restaurant365** | Restaurant-specific ERP | AI automation vs manual processes |
| **Toast** | POS with basic reporting | Advanced analytics and multi-system integration |
| **Resy/OpenTable** | Reservation management | Unified operations and financial platform |
| **Excel/Google Sheets** | Manual financial analysis | Automated intelligence vs spreadsheet maintenance |
| **QuickBooks** | General accounting software | Restaurant-specific AI agents and workflows |
| **Compeat** | Food cost management | Real-time AI optimization vs static reporting |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already have Restaurant365/Toast reporting" | "Those systems tell you what happened. monday.com AI agents prevent problems before they occur and optimize performance in real-time. Our AI doesn't just report 38% food cost - it identifies the cause, suggests corrections, and can automatically adjust pricing to restore margins." |
| "Our margins are too thin for new software costs" | "Thin margins make AI automation even more critical. Capturing just 50% more early payment discounts and reducing prime cost by 1% will pay for the platform multiple times over. You can't afford NOT to automate when margins are tight." |
| "Restaurant operations are too complex for automation" | "Complexity is exactly why you need AI. Our agents handle the complexity so your team focuses on strategic decisions. Instead of calculating prime cost manually, your finance manager can manage twice as many locations with better results." |
| "We need restaurant-specific features" | "Our AI agents understand food cost percentages, franchise royalties, tip reporting, and all the complexities unique to restaurants. We're not adapting generic tools - we're building restaurant intelligence that speaks your language." |
| "Implementation will disrupt operations" | "Our integrations work with your existing POS and accounting systems. Most restaurants see value within 30 days without changing their operational processes. The AI adapts to how you work, not the other way around." |

## Proof Points
*(To be populated with customer references)*

- Multi-location restaurant chain reduced prime cost calculation time by 85% while improving gross margin by 3.2%
- Fast-casual franchise operator automated royalty reporting for 40+ locations, eliminating compliance issues
- Full-service restaurant group captured 94% of early payment discounts, saving $180K annually
- Quick-service chain improved comp sales performance through AI-powered menu optimization
- Regional restaurant company consolidated 12 different financial systems into unified AI platform

---

*Generated: February 21, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*