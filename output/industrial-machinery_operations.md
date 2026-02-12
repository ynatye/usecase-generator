# Industrial Machinery & Equipment × Operations Playbook

## Overview

Operations in industrial machinery and equipment manufacturing is the backbone of a business where complexity is the norm, not the exception. Unlike consumer goods manufacturing with standardized, high-volume production runs, industrial machinery operations must orchestrate **engineer-to-order (ETO)**, **make-to-order (MTO)**, and **make-to-stock (MTS)** production models—often simultaneously within the same facility.

The Operations function in this industry spans manufacturing operations (machining, fabrication, assembly, quality control), supply chain (raw materials, castings, components, logistics), and plant operations (facilities, maintenance, EHS). At mid-to-large industrial machinery companies, this organization can range from 150-1,500+ employees across multiple manufacturing sites, service depots, and dealer networks globally.

What makes this combination unique: Industrial machinery has extraordinarily long Bills of Materials (BOMs)—a single piece of equipment might have 5,000-50,000 parts. Lead times for critical components (castings, motors, gearboxes) can extend 12-26 weeks. Customer specifications frequently change after order placement. And the equipment itself often requires commissioning, installation supervision, and ongoing field service support. The opportunity for AI is enormous: tame BOM complexity, predict material shortages before they halt production, optimize shop floor scheduling in real-time, and connect the factory floor to field service operations.

---

## Value Driver Prioritization

1. **Scale Impact Without Overhead** — HIGHEST RELEVANCE
   - Industrial machinery companies face massive variability in order volume and complexity
   - Same operations team must handle a $50K standard unit and a $5M custom system
   - AI enables handling 2-3x order complexity without proportional headcount growth
   
2. **Replace or Radically Augment Headcount** — HIGH RELEVANCE
   - Production planning and scheduling consumes significant engineering resources
   - Work order management and shop floor coordination is heavily manual
   - Quality documentation and NCR processing requires dedicated personnel
   
3. **Consolidate Tech Stack with AI** — MEDIUM RELEVANCE
   - Most operations teams run ERP (SAP, Oracle, Epicor), MES, spreadsheets, and tribal knowledge
   - Integration gaps between systems create blind spots
   - Consolidation is attractive but must integrate with existing ERP/MRP backbone

---

## Prioritized Use Cases

### 1. Production Planning & Shop Floor Scheduling
**Relevance**: High  
**Value Driver**: 1 (Scale Without Overhead)

**Pain Point**: 
Production planning in industrial machinery is extraordinarily complex. A single machine may have 500+ operations across machining, fabrication, welding, assembly, electrical, testing, and painting. Work centers have different capacities, skills, and tooling. Material availability constantly shifts as supplier deliveries slip. Customer engineering changes arrive mid-production. Most planners rely on ERP-generated schedules that are outdated within hours, supplemented by spreadsheets and whiteboard scheduling. When priorities conflict, tribal knowledge determines sequencing—knowledge that walks out the door when experienced planners retire.

**Solution**: 
monday.com Work Management as a visual production scheduling layer on top of ERP. AI-powered scheduling that accounts for work center capacity, material availability, tooling constraints, and customer priorities. Real-time schedule updates when disruptions occur. Vibe app for shop floor supervisors to report progress and flag blockers.

**Vibe Prompt**:
```
Build a Production Scheduling app for industrial machinery manufacturing.

Purpose: Visual production scheduling across work centers with real-time status tracking, constraint management, and AI-powered optimization.

Key features:
- Work order board: Work Order #, Sales Order, Customer, Machine model, Quantity, Required date, Priority (Standard/Rush/Critical)
- Visual Gantt/timeline view across work centers: Machining, Fabrication, Welding, Assembly, Electrical, Paint, Test
- Operation-level tracking: Each work order has sub-items for individual operations with estimated hours, assigned work center, scheduled start/end
- Resource view: Work center capacity (hours available vs scheduled), Operator skills matrix, Tooling availability
- Material status integration: Traffic light showing material availability (Green=in stock, Yellow=in transit, Red=not ordered/late)
- Constraint detection: AI flags scheduling conflicts, material shortages, capacity overloads
- Engineering change integration: Link to ECN/ECO items affecting work orders
- Shop floor status updates: Simple status workflow per operation (Queued → In Setup → Running → QC Hold → Complete)
- Dashboard: Schedule adherence %, Work center utilization, On-time delivery forecast, Bottleneck work centers, Past-due operations

Include automations:
- When material status turns Red, notify Planner and Purchasing with affected work orders
- When operation completed, auto-start next operation if no constraints
- When work order priority = Critical, highlight in red across all views
- Daily digest to Production Manager: Today's starts, Yesterday's completions, At-risk work orders
- When actual hours exceed estimated by >20%, flag for review and log variance
- When customer required date approaches (<5 days) and work order not in final operations, escalate to Operations Director
```

**Outcome**: 
- Improve schedule adherence by 20-30%
- Reduce expediting costs (overtime, premium freight) by 25%
- Enable production planners to handle 40% more work orders without additional headcount
- Reduce time spent in daily scheduling meetings by 50%

**Discovery Questions**:
- "How many work orders are you managing at any given time? How many planners does that require?"
- "When a critical customer order comes in, how long does it take to understand the impact on your existing schedule?"
- "What happens when a key material delivery slips by two weeks? How do you re-plan?"
- "How much of your production knowledge lives in spreadsheets or people's heads?"

**Industry-Specific Context**: 
Work center = a manufacturing resource (machine, assembly station, work area). Routing = the sequence of operations to produce a part. Constraint = any factor limiting throughput (materials, capacity, tooling, skills). "Tribal knowledge" = undocumented expertise that experienced planners carry—a major risk as workforce ages out.

---

### 2. Engineering Change Order (ECO) Management
**Relevance**: High  
**Value Driver**: 1 (Scale Without Overhead)

**Pain Point**: 
Engineering changes are constant in industrial machinery. A customer requests a modification. Engineering discovers a design flaw. A supplier discontinues a component. Each change triggers a cascade: update the BOM, revise drawings, modify routings, adjust material orders, notify production, update documentation. A typical machine builder processes 50-500 ECOs per month. The coordination burden is immense—changes slip through cracks, production builds to old specs, parts are ordered incorrectly, and documentation lags reality.

**Solution**: 
monday.com workflow for ECO intake, impact assessment, cross-functional review, and implementation tracking. AI-powered impact analysis that identifies all affected BOMs, work orders, and purchase orders. Automated routing to stakeholders based on change type and affected products.

**Vibe Prompt**:
```
Build an Engineering Change Order (ECO) Management app for industrial machinery manufacturing.

Purpose: Manage the full lifecycle of engineering changes from request through implementation with impact tracking and cross-functional coordination.

Key features:
- ECO intake form: Title, Description, Change type (Design/Process/Material/Supplier/Documentation), Urgency (Standard/Expedite/Emergency), Requested by, Reason (Customer request/Cost reduction/Quality issue/Supplier change/Regulatory)
- AI-powered impact assessment suggesting: Affected part numbers, Affected BOMs (parent assemblies), Open work orders using affected parts, Open POs for affected parts, Affected drawings/documents, Required effectivity point
- Affected items sub-board: Part numbers, Current rev, New rev, Change description, Status
- Multi-level approval workflow: Engineering → Manufacturing Engineering → Production Planning → Purchasing → Quality → Final Approval
- Effectivity management: Serial number, Work order, or Date effectivity
- Implementation tracking: Tasks for BOM update, Drawing release, Routing update, PO modification, Floor notification, Inventory disposition
- Red-line/mark-up attachments for drawing changes
- Status workflow: Draft → Impact Assessment → Under Review → Approved → Implementation → Closed
- Dashboard: Open ECOs by type/age, Average cycle time, ECOs by product line, Implementation backlog, Emergency changes this month

Include automations:
- On submit, AI auto-populate impact assessment with affected items
- Route to approvers based on change type and affected product lines
- When ECO affects open work orders, immediately notify Production Planning
- When approval granted, auto-generate implementation task list based on change type
- When implementation task completed, update status and notify next task owner
- 48 hours before target effectivity date, alert if implementation tasks incomplete
- Weekly summary to Engineering Manager: New ECOs, Aging ECOs, Cycle time trends
```

**Outcome**: 
- Reduce ECO cycle time by 40-50%
- Eliminate "build to wrong revision" quality escapes
- Decrease engineering hours spent on change coordination by 30%
- Improve traceability for regulatory and customer audits

**Discovery Questions**:
- "How many engineering changes do you process per month? How long does a typical change take from request to implementation?"
- "What happens when production builds to an old revision? How often does that occur?"
- "How do you know which work orders or purchase orders are affected by a change?"
- "When a customer asks for the change history on a specific serial number, how long does it take to compile?"

**Industry-Specific Context**: 
ECO/ECN = Engineering Change Order/Notice. BOM = Bill of Materials. Effectivity = when a change takes effect (serial number, work order, or date). Red-line = marked-up drawing showing changes. Disposition = what to do with existing inventory of obsoleted parts.

---

### 3. Non-Conformance Report (NCR) & CAPA Management
**Relevance**: High  
**Value Driver**: 2 (Replace/Augment Headcount)

**Pain Point**: 
Quality issues are inevitable in complex machinery manufacturing. When parts don't meet spec, when welds fail inspection, when assembly doesn't fit—each requires documentation, investigation, disposition, and corrective action. A busy manufacturing site might process 100-500 NCRs per month. Quality engineers spend 50% of their time on paperwork rather than root cause analysis. Patterns across NCRs are missed because data lives in scattered systems. When the same defect recurs, it takes weeks to connect the dots.

**Solution**: 
monday.com quality workflow for NCR intake (including Vibe mobile app for shop floor reporting), AI-powered classification and routing, investigation tracking with AI-suggested root causes, CAPA management with effectiveness verification. AI pattern detection identifies recurring issues before they become systemic.

**Vibe Prompt**:
```
Build a Non-Conformance & CAPA Management app for industrial machinery manufacturing quality teams.

Purpose: Capture quality issues from the shop floor, manage investigation and disposition, track corrective actions, and identify patterns.

Key features:
- NCR intake form (mobile-friendly): Date discovered, Discovered by, Part number, Work order, Quantity affected, Defect type (Dimensional/Surface finish/Weld/Assembly/Electrical/Functional), Description, Photos
- AI-powered classification: Severity (Critical/Major/Minor), Category auto-suggested based on description
- Disposition workflow: MRB (Material Review Board) queue for Critical/Major items
- Disposition options: Use as-is, Rework, Scrap, Return to supplier, Concession request to customer
- Investigation section: Root cause (5 Whys template), Contributing factors, Evidence attachments
- AI suggestion panel: Similar past NCRs with their root causes and resolutions
- CAPA section: Corrective actions, Preventive actions, Owner, Due date, Effectiveness criteria, Verification date
- Cost tracking: Rework hours, Scrap cost, Supplier chargeback, Customer credit
- Pattern detection dashboard: NCRs by defect type/part number/work center/supplier/operator, Trend charts, Pareto analysis
- Status workflow: Reported → Under Investigation → MRB Review → Disposition Decided → Rework In Progress → Verification → Closed

Include automations:
- On creation, auto-assign to Quality Engineer based on defect type
- When severity = Critical, immediately notify Quality Manager and stop work order
- When similar NCRs detected (3+ same part/defect in 30 days), alert Quality Manager with pattern analysis
- When disposition = Return to supplier, auto-create supplier corrective action request
- When rework complete, schedule verification inspection
- Monthly summary to Operations Director: NCR volume, Cost of quality, Top defect types, Supplier quality trends
```

**Outcome**: 
- Reduce NCR processing time by 40%
- Decrease repeat defects by 25% through pattern detection
- Reduce cost of quality by 15-20%
- Free quality engineers to focus on prevention vs. paperwork

**Discovery Questions**:
- "How many NCRs do you process monthly? What does your quality team spend most of their time on?"
- "When you see the same defect multiple times, how quickly do you identify the pattern?"
- "What's your current cost of quality—rework, scrap, warranty, returns?"
- "How do you track corrective actions to ensure they actually prevent recurrence?"

**Industry-Specific Context**: 
NCR = Non-Conformance Report. MRB = Material Review Board (cross-functional team that decides disposition). CAPA = Corrective and Preventive Action. "Use as-is" = accept the deviation without rework. "Concession" = customer approval to ship out-of-spec product.

---

### 4. Supplier Performance & Material Management
**Relevance**: High  
**Value Driver**: 3 (Consolidate Tech Stack)

**Pain Point**: 
Industrial machinery supply chains are deep and complex. A single machine might source components from 200+ suppliers across multiple tiers. Critical items (castings, motors, specialty steel) have long lead times and limited sources. Supplier performance varies wildly—and when a supplier fails, production stops. Most companies track supplier data across ERP (orders/receipts), QMS (quality issues), spreadsheets (scorecards), and email (communications). Assembling a complete supplier picture takes hours. Identifying supply risks before they become crises is nearly impossible.

**Solution**: 
monday.com as supplier management hub: supplier scorecards with AI-calculated risk ratings, material shortage early warning, delivery performance tracking, quality incident correlation. Integration with ERP for order/receipt data. Vibe app for receiving to flag issues at dock.

**Vibe Prompt**:
```
Build a Supplier Performance & Material Management app for industrial machinery manufacturing.

Purpose: Centralize supplier management, track delivery and quality performance, identify risks, and manage critical material status.

Key features:
- Supplier master: Company name, Supplier code, Primary contact, Categories (Castings/Steel/Motors/Electronics/Hydraulics/Fasteners/etc.), Qualification status, Last audit date
- Supplier scorecard: On-time delivery %, Quality acceptance rate (incoming inspection), Responsiveness rating, Price competitiveness, Overall score (weighted), Risk rating (Low/Medium/High/Critical)
- AI risk monitoring: Analyzes delivery trends, quality patterns, and external signals to flag suppliers trending toward risk
- Material status board: Part number, Description, Supplier, PO#, Promised date, Current status, Quantity open, Work orders waiting
- Critical material alerts: AI identifies parts with demand but insufficient supply/PO coverage
- Receiving integration: Log receipts, flag quantity discrepancies, trigger incoming inspection
- Supplier quality incidents: Link to NCRs, SCARs (Supplier Corrective Action Requests), returns
- Alternate supplier mapping: Primary/Secondary/Tertiary suppliers for supply chain resilience
- Dashboard: Suppliers by risk level, Material shortages impacting production, Delivery performance trends, Open SCARs, Spend by supplier

Include automations:
- When on-time delivery drops below 85% for 3 months, increase risk rating and notify Purchasing Manager
- When incoming inspection fails, auto-create NCR and link to supplier record
- When material promised date slips, recalculate impact on work orders and notify Planning
- When no PO exists for material needed within lead time, alert Buyer
- When supplier risk = Critical, require approval for new POs
- Weekly digest to Supply Chain Manager: At-risk suppliers, Material shortages, Top issues
```

**Outcome**: 
- Reduce supply disruptions by 40% through early warning
- Improve supplier on-time delivery by 15% through accountability
- Consolidate supplier data from 4+ systems into one view
- Enable proactive supplier development vs. reactive firefighting

**Discovery Questions**:
- "When you have a supplier quality issue, how long does it take to see their complete history—delivery, quality, communications?"
- "How many supply disruptions did you experience last year? What was the production impact?"
- "How do you identify which suppliers are trending toward problems before they fail?"
- "Where does your supplier data live today? How many systems does someone need to check?"

**Industry-Specific Context**: 
SCAR = Supplier Corrective Action Request. Incoming inspection = quality check on received materials. Lead time = time from order to receipt. "Sole source" = only one qualified supplier—a major risk. Tier 2/3 suppliers = suppliers to your suppliers.

---

### 5. Work Order Traveler & Shop Floor Documentation
**Relevance**: Medium-High  
**Value Driver**: 2 (Replace/Augment Headcount)

**Pain Point**: 
Every work order in industrial machinery manufacturing requires documentation that travels with the job: operation sequences, drawing references, quality checkpoints, material lists, labor tracking. This "traveler" is often a paper packet or a collection of PDFs and spreadsheets. Operators hunt for the right revision of drawings. Inspectors fill out paper forms that get manually entered into systems. When something goes wrong, reconstructing the history of a work order is archaeological work.

**Solution**: 
Digital work order traveler in monday.com with all documentation, instructions, and quality checks accessible on tablets at each work center. AI-assisted documentation that auto-populates standard information, captures labor time, and logs inspection results. Paperless shop floor that maintains complete traceability.

**Vibe Prompt**:
```
Build a Digital Work Order Traveler app for industrial machinery shop floor operations.

Purpose: Provide operators with a digital traveler containing all work order information, capture real-time labor and quality data, eliminate paper on the shop floor.

Key features:
- Work order header: WO#, Part number, Description, Quantity, Customer, Required date, Current operation, BOM revision, Drawing revision
- Operation list: Sequence, Operation name, Work center, Estimated hours, Status, Actual hours, Operator, Completion timestamp
- Document links: Drawing PDF (current revision), Operation instructions, Setup sheets, Inspection criteria
- Labor capture: Clock in/out per operation, Operator ID (badge scan or login), Automatic time calculation
- Quality checkpoints: Inspection prompts at designated operations, Dimensional checks with tolerances, Pass/Fail with notes, Attach photos of defects or measurements
- Material consumption: BOM components for this operation, Actual usage tracking, Variance flagging
- Notes and alerts: Special customer requirements, Engineering notes, Safety warnings
- Status workflow per operation: Not Started → In Setup → Running → Inspection → Complete → Moved to Next
- Historical view: Complete audit trail of all operations, times, inspectors, and results
- Dashboard for supervisors: Operations in progress by work center, Labor efficiency, Quality holds, Operator productivity

Include automations:
- When operation clocked in, display relevant drawing and instructions
- When inspection fails, create NCR and hold work order
- When operation complete, auto-advance to next operation and notify
- When actual hours exceed estimate by >25%, alert supervisor
- When all operations complete, route to final QC and shipping
- Daily report to Production Manager: Completed work orders, Efficiency by work center, Quality holds
```

**Outcome**: 
- Eliminate paper travelers and manual data entry (save 2-4 hours per work order)
- Reduce drawing revision errors by 90%
- Improve labor tracking accuracy for job costing
- Complete traceability for customer audits and warranty claims

**Discovery Questions**:
- "How do operators get work instructions and drawings today? How do you ensure they have the right revision?"
- "How much time do clerks spend entering labor and inspection data from paper into your systems?"
- "When a customer asks for documentation on a specific serial number, how long does it take to compile?"
- "What's your current visibility into real-time work order status on the shop floor?"

**Industry-Specific Context**: 
Traveler = documentation packet that accompanies a work order through production. Work center = manufacturing resource. Operation = a single step in the routing. Job costing = tracking actual costs (labor, materials) against estimates for each job.

---

### 6. Equipment Maintenance & CMMS
**Relevance**: Medium  
**Value Driver**: 3 (Consolidate Tech Stack)

**Pain Point**: 
Industrial machinery manufacturing requires extensive capital equipment—CNC machines, welding robots, paint booths, cranes, test systems. Unplanned downtime is enormously costly—not just the repair, but the ripple effects through the production schedule. Most companies have CMMS systems (Computerized Maintenance Management Systems), but they're often poorly maintained, disconnected from production scheduling, and focused on reactive rather than predictive maintenance. Maintenance data lives in CMMS, downtime impact lives in ERP, and tribal knowledge about equipment quirks lives in veteran technicians' heads.

**Solution**: 
monday.com as maintenance management hub that connects equipment health to production impact. PM schedules integrated with production planning. Work request capture from operators. AI-powered predictive maintenance signals. Knowledge capture from experienced technicians.

**Vibe Prompt**:
```
Build an Equipment Maintenance Management app for industrial machinery manufacturing facilities.

Purpose: Manage preventive and corrective maintenance, track equipment reliability, connect maintenance to production impact.

Key features:
- Equipment master: Asset ID, Name, Type (CNC/Welding/Assembly/Test/Material handling), Location, Manufacturer, Model, Serial, Install date, Criticality (A/B/C)
- Preventive maintenance schedules: Task name, Frequency (hours/days/cycles), Last completed, Next due, Estimated duration, Required skills, Parts needed
- Work request capture: Requester, Equipment, Issue description, Urgency (Standard/Urgent/Emergency), Photos
- Work order board: WO#, Equipment, Type (PM/CM/Project), Assigned technician, Status, Scheduled date, Parts required
- Parts inventory: Spare parts linked to equipment, Min stock level, Reorder point, Vendor
- Downtime tracking: Start time, End time, Reason code (Mechanical/Electrical/Operator error/Setup/Parts wait), Production impact (lost hours)
- Equipment history: Complete log of all maintenance, failures, parts replaced
- AI predictive signals: Flag equipment trending toward failure based on maintenance history, downtime patterns, age
- Knowledge base: Equipment-specific troubleshooting guides, lessons learned, tribal knowledge capture
- Dashboard: Equipment availability %, PM compliance, Mean time between failures, Downtime by reason, Maintenance backlog, Parts stock alerts

Include automations:
- When PM due within 3 days, create work order and notify assigned technician
- When emergency work request created, immediately alert Maintenance Supervisor and Production Planning
- When downtime logged on critical equipment, calculate production impact and notify Operations Director
- When same failure occurs 3x in 60 days, flag for root cause investigation
- When parts used, decrement inventory and auto-reorder if below min
- Weekly summary to Plant Manager: Availability by equipment, PM compliance, Top downtime drivers
```

**Outcome**: 
- Improve equipment availability by 5-10%
- Reduce unplanned downtime by 20-30%
- Improve PM compliance to 95%+
- Capture maintenance knowledge before experienced technicians retire

**Discovery Questions**:
- "What's your current equipment availability? How much unplanned downtime do you experience?"
- "How connected is your maintenance scheduling to production planning?"
- "When a critical machine goes down, how long does it take to diagnose and repair? How much of that is parts waiting?"
- "How much of your maintenance knowledge lives in people's heads vs. documented systems?"

**Industry-Specific Context**: 
CMMS = Computerized Maintenance Management System. PM = Preventive Maintenance. CM = Corrective Maintenance. Criticality = importance of equipment to production (A=critical, B=important, C=support). MTBF = Mean Time Between Failures. OEE = Overall Equipment Effectiveness.

---

### 7. Order-to-Ship Visibility & Customer Portal
**Relevance**: Medium  
**Value Driver**: 1 (Scale Without Overhead)

**Pain Point**: 
Industrial machinery customers demand visibility into their orders. Where is my machine in production? When will it ship? What's the status of the engineering submittals? Most companies field these questions via email and phone, with customer service reps manually looking up status in ERP, production schedules, and engineering systems. This is labor-intensive, error-prone, and frustrating for customers who expect real-time visibility.

**Solution**: 
Customer-facing portal built with Vibe that provides real-time order status, milestone tracking, document access (submittals, test reports, manuals), and communication—all without customer service rep intervention. Internal dashboard gives CSRs complete visibility when intervention is needed.

**Vibe Prompt**:
```
Build a Customer Order Portal app for industrial machinery manufacturers.

Purpose: Provide customers with self-service order visibility and document access, while giving internal teams complete customer context.

Key features:
- Customer-facing portal (external access):
  - Order list: Customer's active orders with status summary
  - Order detail: Order #, Machine model/configuration, Key milestones (Order received → Engineering → Production → Test → Ship), Current status, Expected ship date
  - Milestone detail: Completed milestones with dates, Upcoming milestones with forecasts, Delay notifications with explanations
  - Document portal: Drawings for approval, Submittal packages, Test reports, Manuals, Certifications
  - Communication: Request information, Ask questions, Approve documents—all logged
- Internal view (full features):
  - Complete production detail behind each milestone
  - Customer communication history
  - Open issues and risks
  - Related orders and history
- AI-powered status updates: Auto-generate customer-friendly status summaries from production data
- Alert management: Proactive notification to customers when milestones complete or delays occur
- Dashboard for Customer Service: Orders requiring attention, Overdue milestones, Document approvals waiting, Customer questions pending

Include automations:
- When milestone completed in production, update customer portal and optionally notify customer
- When expected ship date changes, notify customer and log reason
- When customer submits question through portal, route to appropriate internal team
- When document uploaded for customer approval, notify customer
- When customer approves document, log approval and notify Engineering
- Daily digest to Customer Service Manager: Delayed orders, Pending customer items, Open questions
```

**Outcome**: 
- Reduce customer inquiry volume by 50-60%
- Improve customer satisfaction through proactive communication
- Free customer service reps to handle exceptions vs. routine status checks
- Accelerate document approvals through portal-based workflow

**Discovery Questions**:
- "How do customers get updates on their orders today? How many calls/emails does that generate?"
- "What percentage of customer inquiries could be self-served if they had portal access?"
- "How do you handle customer document approvals—drawings, submittals, test results?"
- "When orders are delayed, how proactive are you in communicating to customers?"

**Industry-Specific Context**: 
Submittals = documentation package sent to customer for approval before production (drawings, specs, certifications). FAT = Factory Acceptance Test (test at manufacturer's facility before shipment). Commissioning = installation and startup at customer site.

---

## Industry Terminology Glossary

**BOM (Bill of Materials)** — Hierarchical list of all parts, sub-assemblies, and materials required to manufacture a product. In industrial machinery, BOMs can have 5,000-50,000 line items.

**ETO/MTO/MTS** — Engineer-to-Order (custom design for each order), Make-to-Order (standard product built after order), Make-to-Stock (build to inventory). Most industrial machinery companies operate in multiple modes.

**Work Order** — Authorization to produce a specific quantity of parts or products. Contains routing, BOM, and production instructions.

**Routing** — Sequence of operations (manufacturing steps) required to produce a part, including work centers, estimated times, and tooling.

**Work Center** — A production resource—can be a machine (CNC), a station (assembly bench), or an area (welding cell).

**ECO/ECN** — Engineering Change Order/Notice. Formal process to modify product design, process, or documentation.

**NCR** — Non-Conformance Report. Documentation of a quality defect or deviation from specification.

**CAPA** — Corrective and Preventive Action. Root cause analysis and action plan to prevent recurrence.

**MRP (Material Requirements Planning)** — System that calculates material needs based on demand, BOM, and inventory. Generates purchase requisitions and work orders.

**Lead Time** — Time from order placement to receipt (for purchased items) or work order release to completion (for manufactured items).

**Shop Floor** — The production area where manufacturing takes place.

**Traveler** — Documentation packet that accompanies a work order through production, containing drawings, instructions, and inspection requirements.

**Commissioning** — The process of installing, testing, and starting up equipment at the customer's site.

**Aftermarket** — Business related to spare parts, field service, maintenance, and upgrades after initial equipment sale.

**OEM** — Original Equipment Manufacturer. The company that designs and manufactures the equipment.

---

## Typical Stakeholder Roles

**Primary Buyer: VP/Director of Operations**
- Title: VP Manufacturing Operations, Director of Plant Operations, VP Supply Chain
- Concerns: On-time delivery, production efficiency, quality costs, capacity utilization, capital avoidance
- Decision driver: "Can I deliver more machines without more people or more problems?"

**Technical Evaluator: Manufacturing/Production Manager**
- Title: Production Manager, Manufacturing Engineering Manager, Planning Manager
- Concerns: Schedule adherence, work order management, shop floor visibility, planner productivity
- Decision driver: "Will this make my planners and supervisors more effective?"

**Executive Sponsor: COO or General Manager**
- Title: COO, General Manager, SVP Operations
- Concerns: Profitability, customer delivery, operational scalability, competitive positioning
- Decision driver: "Does this enable our growth strategy without proportional cost growth?"

**IT Stakeholder: Manufacturing IT or ERP Admin**
- Title: IT Director, ERP Administrator, Manufacturing Systems Manager
- Concerns: Integration with ERP/MRP, data integrity, support burden, user adoption
- Decision driver: "Can this integrate with our systems without becoming another silo?"

**End Users:**
- Production Planners/Schedulers, Shop Floor Supervisors, Quality Engineers, Buyers/Purchasing Agents, Manufacturing Engineers, Maintenance Technicians

---

## Adjacent Departments

| Department | Connection Point | Cross-Sell Opportunity |
|------------|------------------|------------------------|
| **Engineering** | ECO management, BOM accuracy, drawings | PLM workflows, project management |
| **Purchasing/Procurement** | Material availability, supplier performance | Vendor management, RFQ workflows |
| **Quality** | NCR/CAPA, inspection, audits | Full QMS, customer complaints |
| **Field Service** | Commissioning, warranty, spare parts | Service management, technician dispatch |
| **Sales** | Order entry, delivery promises | monday CRM, quote-to-order |
| **Finance** | Job costing, WIP tracking, inventory | Project accounting, cost analysis |

---

## Competitive Landscape

**Current Tools:**
| Category | Common Tools | Displacement Opportunity |
|----------|--------------|--------------------------|
| ERP/MRP | SAP, Oracle, Epicor, Infor, Microsoft Dynamics | Integration point, not replacement |
| Production Scheduling | ERP modules, Preactor, Schedlyzer, spreadsheets | High displacement potential for visual scheduling |
| QMS | ETQ, MasterControl, spreadsheets | Full replacement for mid-market |
| CMMS | Maximo, Fiix, eMaint, spreadsheets | Full replacement for SMB |
| Project Management | MS Project, Smartsheet, spreadsheets | Full replacement |
| Shop Floor Data Collection | MES, paper, spreadsheets | Vibe apps for data capture |

**Positioning:**
- **vs. ERP add-ons**: "Your ERP is the system of record. We're the system of action—the visual, flexible layer where humans and AI collaborate to manage exceptions and make decisions."
- **vs. Spreadsheets**: "Same flexibility, but with connected data, audit trails, and AI. Stop emailing schedule spreadsheets that are outdated before they arrive."
- **vs. Point Solutions**: "One platform for scheduling, quality, maintenance, and customer visibility—instead of 5 disconnected systems."

---

## Common Objections

**Objection**: "We have SAP/Oracle/Epicor. Why would we add another system?"

**Response**: "We're not replacing your ERP—it's your system of record for transactions. But what about the visual scheduling that's still in spreadsheets? The ECO tracking that happens in email? The supplier scorecards in Access databases? monday.com handles the workflows your ERP wasn't designed for, while integrating with ERP data so you have one picture of operations."

---

**Objection**: "Our operations are too complex for a general-purpose platform."

**Response**: "That's exactly the point. Your operations are too complex for rigid point solutions. monday.com gives you a flexible platform where you can model YOUR specific workflows—whether that's ETO scheduling with 500-operation routings or MTS kanban replenishment. Plus, Vibe lets you build custom apps in minutes for the unique challenges no off-the-shelf product addresses."

---

**Objection**: "We tried implementing better planning tools before. Our people just went back to spreadsheets."

**Response**: "That's because most tools force people to change how they work. monday.com works the way your people already think—visual, flexible, intuitive. We've seen 90%+ adoption rates because it's easier to use than the spreadsheets. And with mobile access, your shop floor can engage directly instead of waiting for data entry."

---

**Objection**: "How do you integrate with our MRP for material availability and production orders?"

**Response**: "We have native integrations with major ERPs and a flexible API for custom integration. Most customers start with a one-way sync—pulling work order and material status from ERP into monday.com for visual planning and execution tracking. Over time, you can add write-back for status updates. The key is that monday.com becomes the engagement layer while ERP remains the transactional system."

---

*Playbook Version: 1.0*  
*Industry: Industrial Machinery & Equipment*  
*Department: Operations*  
*Last Updated: 2026-02-11*
