# Telephony & Wireless × Customer Success Playbook

## Overview

Customer Success teams in the Telephony & Wireless industry operate in one of the most competitive and regulated landscapes, managing subscriber relationships across diverse segments from individual consumers to enterprise B2B accounts. These teams typically range from 50-500+ members in major carriers, organized into specialized pods: Consumer CS (handling individual subscribers), Business CS (SMB/enterprise accounts), Technical Support (network issues), Retention Teams (churn prevention), and Regulatory Affairs (FCC/PUC complaint management). The department serves as the critical bridge between network operations, billing systems, and subscriber satisfaction, operating 24/7 to maintain service levels that directly impact subscriber churn rates, NPS scores, and regulatory compliance.

The unique challenges of telecom Customer Success include managing complex multi-line family accounts, preventing bill shock scenarios, tracking network experience across diverse geographic coverage areas, orchestrating device upgrade journeys, and maintaining first-call resolution rates while handling everything from simple plan changes to complex enterprise SLA compliance issues. Success metrics center on subscriber churn management (targeting <2% monthly churn), customer health scoring based on usage patterns, NPS/CSAT tracking against telecom-specific benchmarks, and customer effort score (CES) optimization. Teams must also navigate the complex landscape of Mobile Number Portability (MNP) retention plays, roaming experience management, and proactive outage communication while driving adoption of self-service tools and managed services.

## Value Driver Mapping

| Value Driver | Relevance | Why It Matters |
|--------------|-----------|----------------|
| **Replace or Radically Augment Headcount** | **HIGHEST** | Customer Success in telecom requires 24/7 coverage across multiple languages and technical expertise levels. AI agents can handle routine inquiries, monitor subscriber health, and provide proactive interventions at scale. |
| **Consolidate Tech Stack with AI** | **HIGH** | CS teams juggle 8-15 systems (billing, CRM, network monitoring, loyalty platforms, device management). One AI platform that connects all systems and provides unified subscriber context is transformational. |
| **Scale Impact Without Overhead** | **MEDIUM-HIGH** | As carriers expand coverage areas and subscriber bases, CS teams need to maintain service quality without linear headcount growth. AI enables managing 2-5x more subscribers per CS rep. |

## Prioritized Use Cases

---

### Use Case 1: Subscriber Churn Prediction & Intervention

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Telecom companies lose 1.5-3% of subscribers monthly, with late-stage churn interventions having <15% success rates. Customer Success teams are reactive, only engaging when subscribers call to cancel or when basic triggers (missed payments) fire. Early churn indicators (declining usage patterns, network experience scores, customer effort increases) go undetected until too late. Manual analysis of subscriber health across millions of accounts is impossible, resulting in $200-500 annual revenue loss per churned subscriber.

#### The Solution
monday.com's AI agents continuously monitor subscriber health scores across usage patterns, billing interactions, network experience data, and support ticket sentiment. Sidekick analyzes patterns across similar subscriber cohorts to predict churn probability 30-90 days in advance. Automated workflows trigger personalized retention campaigns through CRM integration, while high-value subscribers generate immediate alerts for human intervention. mondayDB unifies data from billing systems, network monitoring, and CRM for complete subscriber context.

#### The Outcome
- 40-60% reduction in monthly churn rate through proactive intervention
- 3x increase in retention campaign success rates (45% vs 15%)
- 80% reduction in manual subscriber health analysis time
- $2-5M annual revenue retention per 100K subscriber base

#### Discovery Questions
1. What's your current monthly churn rate across consumer vs. business segments?
2. How many days advance notice do you typically get before a subscriber cancels?
3. What data sources do you use to identify at-risk subscribers today?
4. How do you prioritize which subscribers to focus retention efforts on?
5. What's the typical cost to acquire a new subscriber vs. retain an existing one?

#### Industry Context
Subscriber churn in telecom averages 1.8% monthly for postpaid, 4-6% for prepaid. High-value business accounts often have 12-24 month notice periods but early indicators appear 6+ months prior. Network experience scoring based on call drop rates, data speed tests, and coverage gaps is becoming a critical churn predictor. MNP (Mobile Number Portability) regulations require carriers to process transfers within hours, making proactive retention essential.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a subscriber churn management board with these columns: Subscriber ID (text), Account Type (dropdown: Consumer, SMB, Enterprise), Monthly Revenue (numbers), Churn Risk Score (rating 1-5), Last Network Experience Score (rating 1-5), Usage Trend (status: Increasing, Stable, Declining, Critical), Days Since Last Contact (numbers), Assigned CSM (people), Intervention Status (status: None, Email Sent, Call Scheduled, Retention Offer, Escalated), Next Action Date (date), and Notes (long text). Add an automation that when Churn Risk Score changes to 4 or 5, notify the Assigned CSM and set Intervention Status to 'Call Scheduled'. Create a high-priority dashboard view showing all subscribers with Churn Risk Score 4-5, and a timeline view for tracking intervention activities by CSM."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ChurnGuard AI

**Agent Purpose:**  
Continuously monitors subscriber health metrics and executes automated retention interventions before subscribers reach the decision to churn.

**Triggers:**
- Daily batch analysis of subscriber usage patterns and network experience scores
- Real-time billing system alerts (payment failures, plan downgrades)
- Support ticket creation with negative sentiment
- Network outage affecting subscriber's primary usage area
- Competitor promotion launch in subscriber's market

**Actions:**
- Calculate dynamic churn risk scores using ML models trained on historical data
- Automatically enroll high-risk subscribers in personalized retention email sequences
- Generate retention offers based on subscriber profile and competitive landscape
- Schedule proactive outbound calls for high-value at-risk accounts
- Alert specialized retention teams for enterprise accounts with contract renewal approaching
- Update subscriber health scores in CRM and trigger workflow automations

**Data Required:**
- Billing system integration (usage, payments, plan details)
- Network monitoring data (coverage, speed tests, outage reports)
- CRM integration (interaction history, preferences)
- Support ticket system (ticket volume, sentiment analysis)

**Autonomy Level:** Human-in-the-Loop
ChurnGuard operates autonomously for low-value subscribers (automated emails, standard retention offers) but escalates high-value accounts and complex enterprise situations to human CSMs for personal intervention.

**Example Interaction:**
> ChurnGuard AI detects that enterprise subscriber "TechCorp Solutions" has experienced three network outages in their primary office location over the past month, coinciding with a 40% decrease in data usage. The agent automatically calculates this as a high churn risk (4.5/5) due to network experience degradation. It immediately alerts the assigned enterprise CSM while simultaneously analyzing TechCorp's contract terms and usage patterns. ChurnGuard generates a proactive retention strategy recommending network optimization consultation and temporary service credits, then schedules a priority call for the next business day. The agent continues monitoring TechCorp's network experience hourly and will automatically escalate to the regional director if risk score reaches 5.0 or if the scheduled intervention doesn't occur within 48 hours.

---

### Use Case 2: Proactive Bill Shock Prevention

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Bill shock incidents (unexpected charges >$100 over normal billing) affect 8-12% of subscribers monthly, generating 25-40% of all customer service calls and driving significant churn. Current systems only alert customers after charges are incurred, leading to disputes, regulatory complaints (FCC), and negative NPS scores. Manual monitoring for unusual usage patterns across millions of subscribers is impossible, and basic threshold alerts are too simplistic for today's complex unlimited plans with throttling, roaming charges, and premium services.

#### The Solution
AI agents continuously monitor subscriber usage patterns in real-time, comparing current cycle usage against historical patterns and plan details. When usage anomalies are detected (international roaming activation, premium service charges, device hotspot overuse), automated workflows immediately notify subscribers via SMS/email before significant charges accrue. For business accounts, alerts go to account managers with detailed usage breakdown and optimization recommendations. mondayDB integrates billing, network usage, and plan configuration data for intelligent thresholds.

#### The Outcome
- 70-85% reduction in bill shock incidents and related customer service calls
- 90% decrease in billing dispute resolution time
- 50% improvement in post-bill CSAT scores
- 60% reduction in regulatory complaints related to unexpected charges

#### Discovery Questions
1. What percentage of your customer service calls are related to billing surprises?
2. How do you currently monitor for unusual usage patterns across your subscriber base?
3. What's the average cost to resolve a billing dispute from investigation to resolution?
4. How many FCC complaints do you receive monthly related to billing issues?
5. Do you have different bill shock thresholds for consumer vs. business accounts?

#### Industry Context
The FCC requires carriers to provide bill shock protection, but minimum compliance often means generic $100 thresholds. Modern unlimited plans have complex throttling, deprioritization, and premium service structures that create confusion. International roaming remains a major bill shock source, with single-day charges potentially exceeding $500. Enterprise accounts often have shared data pools across hundreds of lines, making usage tracking complex.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a bill shock prevention tracking board with columns: Subscriber ID (text), Account Type (dropdown: Consumer, Business, Enterprise), Current Cycle Usage (numbers), Historical Average Usage (numbers), Usage Variance % (formula), Alert Threshold (numbers), Last Alert Sent (date), Alert Type (dropdown: Data Overage, International Roaming, Premium Services, Hotspot Limit), Estimated Additional Charges (numbers), Alert Status (status: Monitoring, Warned, Critical, Resolved), CSR Assigned (people), and Customer Response (dropdown: Acknowledged, Reduced Usage, Plan Change, Disputed). Add automations: when Usage Variance % exceeds 150%, set Alert Status to 'Warned' and notify CSR Assigned; when Estimated Additional Charges exceed $75, set status to 'Critical' and create urgent task. Include a dashboard showing current high-risk subscribers and a timeline view of alert patterns by subscriber."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** BillGuard AI

**Agent Purpose:**  
Prevents bill shock incidents by monitoring usage patterns in real-time and proactively alerting subscribers before significant overage charges accrue.

**Triggers:**
- Hourly usage data feeds from network billing systems
- International roaming activation detection
- Premium service activation (music streaming, video services)
- Device hotspot usage exceeding normal patterns
- Multi-line family account usage concentration on single line

**Actions:**
- Calculate dynamic usage thresholds based on subscriber history and plan details
- Send immediate SMS/email alerts when usage anomalies are detected
- Automatically offer plan upgrade recommendations when beneficial
- Generate detailed usage breakdown reports for business account managers
- Create customer service tickets for complex billing scenarios requiring human intervention
- Track subscriber response to alerts and adjust threshold sensitivity

**Data Required:**
- Real-time network usage data (voice, text, data consumption)
- Billing system integration (plan details, current charges, payment history)
- Device and service activation logs
- Historical usage patterns and seasonal variations
- International roaming rate tables and partner network information

**Autonomy Level:** Fully Autonomous
BillGuard operates completely autonomously for standard bill shock scenarios, sending alerts and recommendations directly to subscribers. Only escalates to humans for complex enterprise accounts or when subscribers dispute the alerts.

**Example Interaction:**
> BillGuard AI detects that subscriber Maria Rodriguez, typically using 15GB monthly, has consumed 35GB in just 10 days while traveling internationally. The agent immediately recognizes this as international roaming (based on network logs) and calculates potential charges of $420 at current usage rate. BillGuard instantly sends Maria an SMS: "International roaming alert: You've used 35GB in Italy (usual: 15GB/month). At current rate, extra charges could reach $420. Reply STOP to disable data roaming, PLAN to see international options, or CONTINUE to proceed." Simultaneously, BillGuard logs the incident, updates Maria's risk profile, and prepares three follow-up actions: a plan optimization recommendation for frequent travelers, a courtesy credit approval for first-time roaming shock, and an escalation to human agents if charges exceed $500. The agent continues monitoring Maria's usage hourly until she returns to the US or responds to the alert.

---

### Use Case 3: Enterprise SLA Compliance Monitoring

**Relevance:** High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Enterprise B2B accounts have complex SLAs covering network uptime, data speeds, support response times, and service restoration. Manual SLA monitoring across hundreds of enterprise accounts is time-intensive and error-prone, with violations often discovered after customers raise complaints. Each SLA breach can trigger financial penalties ($5K-50K), contract renegotiations, and account churn risk. CS teams lack real-time visibility into SLA performance and struggle to provide proactive communication when service levels are at risk.

#### The Solution
AI agents continuously monitor network performance, support ticket response times, and service metrics against each enterprise account's specific SLA terms stored in mondayDB. Real-time integrations with network monitoring systems trigger immediate alerts when SLA thresholds are approached. Automated workflows generate executive summary reports, calculate penalty exposure, and create proactive communication templates for account managers. When SLA violations occur, agents automatically document incidents, calculate credits due, and route to appropriate stakeholders for resolution.

#### The Outcome
- 90% reduction in SLA violations discovered through customer complaints
- 75% decrease in time spent on manual SLA compliance reporting
- 60% improvement in proactive communication for at-risk service levels
- $500K-2M annual savings in avoided SLA penalties and account churn

#### Discovery Questions
1. How many enterprise accounts have specific SLA requirements beyond standard service terms?
2. What's your current process for monitoring SLA compliance across your B2B portfolio?
3. How often do you discover SLA violations after customers complain vs. proactively?
4. What's the average financial impact when an enterprise SLA is breached?
5. How do you currently calculate and approve SLA credits or penalties?

#### Industry Context
Enterprise SLAs in telecom typically include 99.9% network uptime, <20ms latency guarantees, 4-hour response times for priority issues, and 24-hour resolution for service-affecting problems. Large enterprises often have multiple locations with different service levels, managed services components, and complex escalation matrices. Regulatory requirements may mandate specific SLA terms for government or healthcare accounts.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an enterprise SLA monitoring board with columns: Account Name (text), Contract Value (numbers), SLA Tier (dropdown: Gold, Silver, Bronze), Network Uptime % (numbers), Response Time SLA Hours (numbers), Actual Avg Response Hours (numbers), Current Month Violations (numbers), YTD Violations (numbers), SLA Status (status: Compliant, At Risk, Violated, Under Review), Penalty Exposure (numbers), Account Manager (people), Last Executive Report (date), Next Review Date (date), and Escalation Level (dropdown: None, Account Manager, Regional Director, C-Suite). Add automations: when Network Uptime % drops below SLA threshold, set SLA Status to 'At Risk' and notify Account Manager; when violations exceed monthly threshold, escalate to Regional Director and create executive summary task. Create a dashboard showing all At Risk and Violated accounts, plus a timeline view for tracking SLA performance trends by account."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SLAWatch Pro

**Agent Purpose:**  
Continuously monitors enterprise SLA compliance across all performance metrics and automates violation prevention and incident management workflows.

**Triggers:**
- Real-time network performance metrics falling below SLA thresholds
- Support ticket response time delays for enterprise accounts
- Service restoration time approaching SLA limits
- Monthly SLA compliance calculation schedules
- Enterprise contract renewal dates approaching

**Actions:**
- Monitor network uptime, latency, and throughput against account-specific SLA terms
- Calculate real-time compliance metrics and penalty exposure
- Generate automated alerts to account managers when SLAs are at risk
- Create executive summary reports for monthly business reviews
- Automatically calculate and approve standard SLA credits
- Escalate complex violations to appropriate stakeholder levels
- Track competitor performance data for contract renewal discussions

**Data Required:**
- Network monitoring system integration (uptime, performance metrics)
- Support ticketing system (response times, resolution times)
- Contract management system (SLA terms, penalty structures)
- Account hierarchy and stakeholder contact information
- Historical performance data for trend analysis

**Autonomy Level:** Escalation-Based
SLAWatch operates autonomously for monitoring and standard reporting, but escalates to humans for SLA violations, penalty approvals exceeding preset limits, or when compliance issues could affect contract renewals.

**Example Interaction:**
> SLAWatch Pro detects that TechCorp's primary site has experienced 99.85% uptime this month (SLA requirement: 99.9%), putting them at risk of a $15K penalty. The agent immediately alerts account manager Sarah Chen while calculating the exact downtime minutes and financial exposure. SLAWatch automatically generates a proactive communication template explaining the situation and proposing a network optimization review. When a fiber cut causes an additional 3-hour outage, pushing uptime to 99.7%, the agent instantly escalates to the regional director, auto-approves the $15K SLA credit, creates an executive incident report, and schedules a C-level customer call within 4 hours. SLAWatch continues monitoring restoration efforts and provides real-time updates to all stakeholders until service is fully restored and compliance metrics return to acceptable levels.

---

### Use Case 4: Customer Health Scoring & Lifecycle Management

**Relevance:** High  
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
Customer Success teams lack unified view of subscriber health across the complex telecom ecosystem. Data lives in siloed systems: usage patterns in billing, satisfaction scores in survey platforms, support interactions in ticketing systems, payment history in finance systems, and network experience in operations tools. Manual compilation of customer health scores is time-consuming and inconsistent, preventing proactive lifecycle management from activation through retention to win-back campaigns. Without unified customer health visibility, CS teams react to problems instead of preventing them.

#### The Solution
mondayDB becomes the unified context layer for all subscriber data, automatically aggregating usage patterns, payment history, support interactions, network experience scores, and satisfaction metrics into dynamic customer health scores. AI agents continuously update health scores and trigger appropriate lifecycle actions: onboarding automation for new activations, engagement campaigns for declining usage, proactive support for network issues, and win-back campaigns for churned subscribers. Sidekick provides instant health score explanations and recommendations to CS reps during customer interactions.

#### The Outcome
- 85% improvement in customer health score accuracy through unified data
- 40% increase in proactive intervention success rates
- 60% reduction in time spent gathering customer context during support calls
- 50% improvement in customer lifecycle campaign conversion rates

#### Discovery Questions
1. How many different systems do your CS reps need to check to understand a customer's full situation?
2. What metrics do you currently use to define a "healthy" vs "at-risk" subscriber?
3. How often are customer health scores updated, and who maintains them?
4. What lifecycle stages do you actively manage beyond new subscriber onboarding?
5. How do you currently identify opportunities for customer expansion or upgrades?

#### Industry Context
Telecom subscriber lifecycles include activation (first 30 days), adoption (engagement with services), growth (plan upgrades, add-ons), retention (ongoing satisfaction), and potential win-back (post-churn re-engagement). Healthy subscribers typically show consistent usage patterns, low support contact frequency, on-time payments, and positive network experience scores. Multi-line family accounts and business accounts have complex health scoring due to multiple usage patterns and stakeholders.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a customer health scoring board with columns: Subscriber ID (text), Account Type (dropdown: Consumer, Family Plan, SMB, Enterprise), Health Score (rating 1-5), Usage Trend (status: Growing, Stable, Declining, Inactive), Payment Status (status: Current, Late, Failed, Collections), Support Tickets Last 90 Days (numbers), Network Experience Score (rating 1-5), Satisfaction Score NPS (numbers), Lifecycle Stage (dropdown: Activation, Adoption, Growth, Retention, Win-back), Last Engagement Date (date), Assigned CSM (people), Next Action (dropdown: None, Onboarding, Check-in, Intervention, Upgrade Offer), Action Due Date (date), and Notes (long text). Add automations: when Health Score drops to 2 or below, set Next Action to 'Intervention' and notify Assigned CSM; when Lifecycle Stage is 'Activation' and Last Engagement is >7 days ago, create onboarding follow-up task. Include a dashboard showing health score distribution and lifecycle stage funnel, plus individual CSM workload views."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** HealthSync AI

**Agent Purpose:**  
Continuously monitors and updates subscriber health scores while orchestrating automated lifecycle management campaigns across all customer touchpoints.

**Triggers:**
- Daily batch processing of usage, billing, and support data
- Real-time payment status changes
- Network experience score updates
- Support ticket creation or resolution
- Survey response submissions (NPS/CSAT)

**Actions:**
- Calculate dynamic health scores using ML models trained on subscriber behavior
- Automatically segment subscribers by lifecycle stage and health status
- Trigger personalized email campaigns based on health score changes
- Update CRM records with latest health metrics and recommended actions
- Generate priority lists for CS rep outreach based on health score urgency
- Route high-value declining accounts to specialized retention specialists
- Track campaign effectiveness and adjust health scoring models

**Data Required:**
- Billing system integration (usage patterns, payment history, plan details)
- Support system integration (ticket volume, resolution time, satisfaction)
- Network performance data (speed tests, coverage, outage impact)
- Survey platform integration (NPS, CSAT scores)
- Marketing automation system for campaign execution

**Autonomy Level:** Fully Autonomous
HealthSync operates autonomously for health score calculations and standard lifecycle campaigns, but generates alerts and recommendations for human CSMs when complex interventions are needed or high-value accounts show declining health.

**Example Interaction:**
> HealthSync AI processes overnight data and identifies that long-time subscriber Jennifer Park's health score has dropped from 4.2 to 2.8 over the past month. The analysis shows declining data usage (60% reduction), two recent support tickets about slow speeds, and a 6/10 response to the latest CSAT survey. HealthSync immediately categorizes Jennifer as "Retention Risk" and triggers a three-part intervention: an immediate email acknowledging her recent network concerns with a direct contact for technical support, a proactive network optimization check for her area, and a priority flag for her next customer service interaction. The agent simultaneously alerts Jennifer's assigned CSM with a summary of the health decline factors and suggests a personal outreach call within 48 hours. HealthSync continues monitoring Jennifer's engagement with the intervention emails and will escalate to a retention specialist if health score drops below 2.0 or if she doesn't respond within one week.

---

### Use Case 5: Automated Onboarding for Enterprise Accounts

**Relevance:** Medium-High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Enterprise B2B onboarding requires coordinating across multiple departments (Sales, Engineering, Customer Success, Finance) and takes 60-180 days for complex managed services implementations. Manual project management across dozens of enterprise accounts creates bottlenecks, missed deadlines, and inconsistent customer experiences. CS teams spend 40-60% of their time on project coordination instead of strategic account management. Complex onboarding involving network setup, device provisioning, managed services configuration, and user training requires expert oversight that doesn't scale efficiently.

#### The Solution
AI agents orchestrate enterprise onboarding workflows from contract signature through go-live, automatically coordinating tasks across departments via mondayDB integrations. Automated project timelines adjust based on service complexity, resource availability, and customer requirements. AI monitors onboarding milestones, identifies bottlenecks before they cause delays, and escalates issues to appropriate stakeholders. Standardized onboarding playbooks ensure consistent execution while allowing customization for unique enterprise requirements. Real-time customer portals provide visibility into onboarding progress and next steps.

#### The Outcome
- 50% reduction in average enterprise onboarding time
- 70% decrease in CS time spent on project coordination
- 90% improvement in onboarding milestone predictability
- 85% increase in customer satisfaction scores during onboarding phase

#### Discovery Questions
1. What's your typical enterprise onboarding timeline from contract to go-live?
2. How many departments are involved in complex enterprise implementations?
3. What percentage of enterprise onboardings encounter delays, and what are common causes?
4. How do you currently track onboarding progress across your enterprise pipeline?
5. What's the impact on customer satisfaction when onboarding timelines extend?

#### Industry Context
Enterprise telecom onboarding involves network design, site surveys, equipment installation, circuit provisioning, managed services configuration, security setup, user training, and go-live support. Large enterprise accounts often require multi-location rollouts, integration with existing IT infrastructure, and compliance with industry-specific regulations. Delays in enterprise onboarding directly impact customer time-to-value and can jeopardize contract renewals.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create an enterprise onboarding management board with columns: Account Name (text), Contract Value (numbers), Services Included (dropdown: Voice Only, Data Only, Managed Services, Full Suite), Onboarding Stage (status: Planning, Site Survey, Installation, Configuration, Testing, Training, Go-live, Complete), Start Date (date), Target Go-live (date), Actual Go-live (date), Days Remaining (formula), At Risk (status: On Track, Minor Delay, Major Delay, Blocked), Assigned PM (people), Engineering Lead (people), Installation Status (dropdown: Scheduled, In Progress, Complete, Issues), Customer Contact (text), Next Milestone (text), Milestone Date (date), and Customer Satisfaction (rating 1-5). Add automations: when Days Remaining is <14 and Onboarding Stage is not 'Testing' or later, set At Risk to 'Major Delay' and notify Assigned PM; when Installation Status changes to 'Issues', create urgent escalation task. Include timeline view showing all enterprise onboardings, dashboard with at-risk accounts, and individual PM workload views."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** OnboardOrchestrator AI

**Agent Purpose:**  
Automates enterprise onboarding project management by coordinating cross-departmental workflows and proactively identifying risks before they impact timelines.

**Triggers:**
- New enterprise contract signature requiring onboarding
- Onboarding milestone completion or delay notifications
- Resource availability changes affecting project timelines
- Customer requests for scope changes or timeline adjustments
- Technical issues during installation or configuration phases

**Actions:**
- Generate customized onboarding project plans based on services contracted
- Automatically assign resources and create task dependencies across departments
- Monitor project progress and update timeline predictions based on current status
- Send proactive alerts when milestones are at risk of missing target dates
- Coordinate customer communications and provide self-service progress portals
- Escalate complex technical issues to appropriate engineering specialists
- Generate executive status reports for high-value enterprise accounts

**Data Required:**
- Contract management system (services, timelines, stakeholder contacts)
- Resource scheduling system (engineering, installation, PM availability)
- Project tracking integration across Sales, Engineering, and Operations
- Customer portal system for progress visibility and communication
- Technical systems for installation status and configuration progress

**Autonomy Level:** Human-in-the-Loop
OnboardOrchestrator handles standard project coordination autonomously but escalates to human project managers for scope changes, major delays, complex technical issues, or customer escalations requiring strategic decision-making.

**Example Interaction:**
> OnboardOrchestrator AI receives notification that MegaCorp's enterprise contract has been signed for a full managed services implementation across 50 locations. The agent immediately creates a master project plan with 180-day timeline, identifies required resources (3 network engineers, 2 installation teams, 1 dedicated PM), and begins coordinating site surveys for the first 10 locations. When the site survey at Location 7 reveals unexpected infrastructure requirements that could delay installation by 3 weeks, OnboardOrchestrator automatically adjusts the overall timeline, reallocates resources to maintain other locations on schedule, generates a customer communication explaining the delay and mitigation steps, and escalates to the human PM for approval of additional engineering resources. The agent continues monitoring all 50 locations, providing daily progress updates to stakeholders and maintaining the revised go-live timeline while proactively identifying potential issues at upcoming locations based on similar infrastructure patterns.

---

### Use Case 6: Network Experience Scoring & Proactive Issue Resolution

**Relevance:** High  
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Network quality issues (slow data, dropped calls, poor coverage) drive 30-40% of customer service calls and are leading churn indicators. Traditional reactive support waits for customers to complain, missing opportunities for proactive intervention. Manual analysis of network performance data across millions of subscribers and thousands of cell towers is impossible at scale. CS teams lack visibility into network issues affecting their customers until complaint volume spikes, making recovery efforts more difficult and expensive.

#### The Solution
AI agents continuously monitor network performance metrics, device connectivity data, and usage patterns to calculate real-time Network Experience Scores for each subscriber. When experience degradation is detected, automated workflows trigger proactive outreach with explanations, resolutions, or service credits before customers call to complain. Integration with network operations enables automatic escalation of widespread issues, while individual device problems trigger targeted troubleshooting flows. Customer-facing communications provide transparency about network improvements and realistic expectations.

#### The Outcome
- 60% reduction in network-related customer service calls
- 70% improvement in customer satisfaction for network issue resolution
- 50% faster resolution of network problems through proactive identification
- 40% reduction in churn attributed to network quality issues

#### Discovery Questions
1. What percentage of your customer service calls are related to network quality issues?
2. How do you currently identify widespread network problems before customer complaints?
3. What network metrics do you track, and how often are they updated?
4. How long does it typically take to resolve individual vs. widespread network issues?
5. Do you provide proactive communication about network outages or improvements?

#### Industry Context
Network Experience Scoring combines call drop rates, data throughput speeds, connection establishment time, and geographic coverage quality. Rural vs. urban performance varies significantly, and different device types (smartphones, IoT, tablets) have different performance expectations. Network sharing agreements with other carriers can complicate issue resolution and customer communication.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a network experience monitoring board with columns: Subscriber ID (text), Location/Tower ID (text), Device Type (dropdown: Smartphone, Tablet, IoT Device, Hotspot), Network Experience Score (rating 1-5), Call Drop Rate % (numbers), Data Speed Mbps (numbers), Connection Issues Last 24h (numbers), Issue Type (dropdown: Coverage, Speed, Dropped Calls, No Service, Roaming), Status (status: Normal, Degraded, Critical, Under Investigation), Customer Notified (checkbox), Resolution ETA (date), Assigned Engineer (people), Escalation Level (dropdown: None, Local, Regional, Corporate), and Customer Impact Level (dropdown: Low, Medium, High, Enterprise). Add automations: when Network Experience Score drops below 3, set Status to 'Degraded' and create notification task; when issues affect >100 subscribers in same area, escalate to Regional level and notify all customers. Include a geographic dashboard showing network performance by location and a timeline view for tracking resolution progress."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** NetworkGuardian AI

**Agent Purpose:**  
Monitors network performance in real-time and proactively resolves subscriber experience issues before they impact satisfaction or drive support calls.

**Triggers:**
- Real-time network performance metric degradation
- Subscriber device connectivity issues or repeated connection failures
- Geographic clusters of performance problems indicating tower/infrastructure issues
- Scheduled network maintenance affecting subscriber areas
- New network outage reports from operations teams

**Actions:**
- Calculate individualized Network Experience Scores based on usage patterns and location
- Automatically send proactive notifications about network issues with expected resolution times
- Trigger device troubleshooting workflows for individual connectivity problems
- Escalate widespread issues to network operations with affected subscriber lists
- Generate service credit recommendations for customers experiencing extended issues
- Update customer profiles with network experience history for future reference
- Coordinate customer communications during planned maintenance or major outages

**Data Required:**
- Real-time network performance monitoring (tower metrics, throughput, connectivity)
- Device connectivity logs and performance data
- Geographic coverage maps and expected service levels by location
- Network operations ticketing system integration
- Customer location and usage pattern data

**Autonomy Level:** Fully Autonomous
NetworkGuardian operates autonomously for individual subscriber issues and standard proactive communications, but escalates to human network engineers for complex infrastructure problems or when customer impacts exceed predefined thresholds.

**Example Interaction:**
> NetworkGuardian AI detects that Tower ID 4782 serving downtown business district has experienced 40% degraded data speeds for the past 2 hours, affecting 347 subscribers including 23 enterprise accounts. The agent immediately calculates individual impact levels based on usage patterns, automatically sends personalized SMS notifications to affected consumers explaining the temporary speed reduction and estimated 4-hour resolution time. For enterprise accounts, NetworkGuardian generates detailed impact reports and alerts their dedicated account managers while automatically applying service credits per SLA terms. The agent escalates the infrastructure issue to network operations with priority ranking based on subscriber impact and continues monitoring resolution progress. When speeds return to normal, NetworkGuardian sends follow-up notifications confirming restoration and proactively schedules follow-up satisfaction surveys to measure recovery effectiveness. Throughout the incident, the agent logs all communications and impacts for future network planning and customer retention analysis.

---

### Use Case 7: Multi-Line Family Account Management

**Relevance:** Medium-High  
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Family accounts with 3-10+ lines create complex customer service scenarios involving multiple users, varied plan needs, device upgrade timing, bill allocation disputes, and parental controls management. CS reps struggle to quickly understand family account dynamics, usage patterns across lines, and decision-maker hierarchy during support calls. Manual tracking of individual line performance, upgrade eligibility, and usage optimization across thousands of family accounts prevents proactive account management and cross-selling opportunities.

#### The Solution
AI agents create unified family account profiles showing usage patterns, device status, plan optimization opportunities, and decision-maker preferences across all lines. Automated workflows identify upsell opportunities (adding lines, plan upgrades), coordinate device upgrade timing for maximum savings, and flag unusual usage patterns that might indicate unauthorized access or teen safety concerns. Intelligent routing ensures family account calls reach agents with full context about all lines and previous interactions with any family member.

#### The Outcome
- 45% reduction in average call handle time for family account inquiries
- 35% increase in successful cross-sell and upsell conversion rates
- 60% improvement in first-call resolution for multi-line issues
- 25% increase in family account retention through proactive management

#### Discovery Questions
1. What percentage of your subscriber base consists of family plans with 3+ lines?
2. How do you currently track relationships and decision-makers within family accounts?
3. What are common pain points when family account members call with different requests?
4. How do you identify opportunities to add lines or upgrade family plans?
5. What tools do you provide for family account management and parental controls?

#### Industry Context
Family plans typically include 2-10 lines with shared data pools, individual device payment plans, and complex billing arrangements. Primary account holders control plan changes and billing, but individual line users often contact CS for support. Usage patterns vary significantly across family members (teens vs. parents), creating optimization opportunities. Parental control and safety features are increasingly important selling points.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Create a family account management board with columns: Family Account ID (text), Primary Account Holder (text), Total Lines (numbers), Monthly Plan Cost (numbers), Total Data Usage GB (numbers), Usage Distribution (text), Upgrade Eligible Lines (numbers), Next Upgrade Date (date), Plan Optimization Opportunity (dropdown: Add Line, Upgrade Data, Downgrade, Device Protection), Estimated Savings (numbers), Account Health Score (rating 1-5), Teen/Child Lines (numbers), Parental Controls Active (checkbox), Last Contact Date (date), Contact Reason (dropdown: Billing, Support, Upgrade, Add Line), Assigned CSR (people), Next Action (text), and Family Satisfaction Score (rating 1-5). Add automations: when multiple lines become upgrade eligible within 30 days, create family upgrade consultation task; when usage distribution shows 80%+ on single line, suggest plan optimization. Include dashboard showing upgrade opportunities and family account health distribution, plus CSR workload view for family account specialists."

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** FamilyConnect AI

**Agent Purpose:**  
Optimizes multi-line family account management by analyzing usage patterns, coordinating upgrade timing, and identifying expansion opportunities across all family lines.

**Triggers:**
- Family account usage pattern changes indicating plan optimization needs
- Multiple lines approaching upgrade eligibility within same timeframe
- Unusual usage spikes on teen/child lines triggering safety concerns
- Family plan additions or changes in competitive market
- Billing disputes or questions related to multi-line charges

**Actions:**
- Analyze usage patterns across family lines to identify plan optimization opportunities
- Coordinate device upgrade timing to maximize family savings and trade-in values
- Generate family account summaries for customer service interactions
- Identify opportunities to add lines when usage suggests additional family members
- Monitor teen line usage patterns and alert for potential safety or overage issues
- Create personalized family plan recommendations based on collective usage trends
- Track family satisfaction across multiple touchpoints and service interactions

**Data Required:**
- Multi-line account structure and relationships
- Individual line usage patterns and preferences
- Device upgrade eligibility and trade-in values
- Family plan options and competitive landscape
- Parental control settings and teen line monitoring data

**Autonomy Level:** Human-in-the-Loop
FamilyConnect operates autonomously for usage analysis and standard recommendations, but requires human approval for significant plan changes, teen safety alerts, or complex billing dispute resolutions involving family dynamics.

**Example Interaction:**
> FamilyConnect AI analyzes the Johnson family account (5 lines) and identifies that three teenagers will be upgrade eligible within 6 weeks, while mom and dad have been on older unlimited plans for 2 years. The agent calculates that coordinating all upgrades simultaneously could save the family $340 through trade-in bonuses and new customer promotions, while upgrading their plan would add 5G access for only $15/month more. FamilyConnect generates a family upgrade consultation proposal and schedules a call with primary account holder Susan Johnson, providing the assigned family account specialist with detailed usage analysis showing why the timing is optimal. When Susan mentions during the call that her college-age daughter needs better coverage at her new school, FamilyConnect immediately suggests adding a sixth line during the upgrade process to maximize family discount benefits, ultimately presenting a complete family communication solution that increases monthly revenue by $65 while saving the family money through coordinated timing and promotional offers.

---

## Industry Terminology

| Term | Definition |
|------|------------|
| **Subscriber Churn Management** | Systematic approach to identifying, predicting, and preventing customer cancellations, typically measured monthly |
| **NPS/CSAT Tracking (Telecom Benchmarks)** | Net Promoter Score and Customer Satisfaction metrics compared against industry standards (telecom NPS average: 31) |
| **Customer Lifecycle Management** | Managing subscriber journey from activation→adoption→retention→win-back with targeted interventions |
| **Bill Shock Prevention** | Proactive monitoring and alerts to prevent unexpected charges exceeding normal billing patterns |
| **Network Experience Scoring** | Composite metric combining call quality, data speeds, coverage, and connectivity reliability |
| **Proactive Outage Notifications** | Automated customer communications about planned maintenance or unplanned service disruptions |
| **Plan Optimization Recommendations** | Data-driven suggestions for plan changes based on usage patterns and available options |
| **Device Upgrade Journeys** | Managed process for device replacement including eligibility, trade-ins, and migration |
| **Loyalty Program Management** | Rewards and retention programs designed to increase customer lifetime value and reduce churn |
| **Customer Health Scoring (Usage Patterns)** | Algorithmic assessment of account stability based on usage, payment, and engagement metrics |
| **Escalation Management (Regulatory Complaints)** | Process for handling FCC/PUC complaints requiring regulatory compliance and reporting |
| **Enterprise/B2B Onboarding** | Complex implementation process for business accounts involving multiple services and stakeholders |
| **Managed Services Adoption** | Encouraging enterprise customers to utilize additional IT and network management services |
| **Self-Service Adoption Tracking** | Measuring customer usage of automated tools, apps, and online account management |
| **First-Call Resolution Optimization** | Maximizing percentage of customer issues resolved without callbacks or transfers |
| **Customer Effort Score (CES)** | Metric measuring how easy it is for customers to get help or complete tasks |
| **Roaming Experience Management** | Monitoring and optimizing service quality when customers travel outside home network |
| **MNP Retention Plays** | Strategies to prevent customers from porting numbers to competitors (Mobile Number Portability) |
| **Multi-Line/Family Account Management** | Specialized handling of accounts with multiple connected lines and shared services |
| **Enterprise SLA Compliance Monitoring** | Tracking service level agreement performance for business customers with contractual guarantees |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| **VP/Director of Customer Success** | Strategic oversight, churn targets, team performance, budget management | High - sets priorities and resource allocation |
| **Customer Success Manager (Enterprise)** | Dedicated relationship management for high-value B2B accounts | High - directly impacts major account retention |
| **Customer Success Manager (Consumer)** | Portfolio management for consumer segments, proactive outreach campaigns | Medium - influences segment performance metrics |
| **Customer Support Manager** | Daily operations, agent performance, first-call resolution, ticket management | Medium - controls operational efficiency |
| **Retention Specialist** | Focused on churn prevention, win-back campaigns, high-risk account intervention | High - directly impacts churn metrics and revenue |
| **Technical Support Lead** | Network-related issue resolution, device troubleshooting, escalation management | Medium - affects technical satisfaction and resolution time |
| **Quality Assurance Manager** | Call monitoring, training programs, compliance with regulatory requirements | Medium - influences overall service quality |
| **Business Intelligence/Analytics Manager** | Data analysis, reporting, customer insights, performance dashboards | Medium - provides insights driving strategic decisions |

## Adjacent Departments

| Department | Connection | Opportunity |
|------------|------------|-------------|
| **Network Operations** | CS escalates service issues, receives outage notifications | Joint platform for proactive issue identification and customer communication |
| **Billing/Finance** | CS handles billing disputes, processes service credits and adjustments | Unified system for real-time billing issue resolution and credit approvals |
| **Sales** | CS manages account expansion, coordinates with new customer onboarding | Shared platform for lead generation from existing customer optimization |
| **Marketing** | CS provides customer feedback, coordinates retention campaigns | Integrated customer journey management from acquisition through retention |
| **Technical Support** | CS routes complex technical issues, receives resolution updates | Combined platform for seamless issue escalation and customer communication |
| **Regulatory Affairs** | CS reports compliance issues, manages regulatory complaint responses | Centralized system for tracking and responding to regulatory requirements |
| **Product Management** | CS provides feature requests and usage insights from customer interactions | Unified feedback loop for product development based on customer success data |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|-------------|-------------------------|
| **Salesforce Service Cloud** | Comprehensive CRM with telecom-specific features, strong integration capabilities | "Complex, expensive, requires extensive customization. monday.com provides telecom-specific AI agents out of the box with unified data layer." |
| **Zendesk** | Popular support ticketing system with basic automation | "Ticketing-focused, not built for proactive customer success. Our AI agents prevent issues before tickets are created." |
| **Gainsight** | Customer Success platform with health scoring and lifecycle management | "Expensive CS-only solution. monday.com consolidates CS with project management, CRM, and AI agents in one platform." |
| **Oracle CX** | Enterprise-grade customer experience suite with telecom industry focus | "Legacy system, slow implementation, limited AI capabilities. Our modern AI-first platform delivers value in weeks, not years." |
| **Microsoft Dynamics 365** | Integrated business applications including customer service | "Generic across industries, limited telecom specialization. Our AI agents understand telecom-specific workflows and terminology." |
| **Custom/In-House Solutions** | Proprietary systems built by telecom companies for specific needs | "High maintenance cost, limited scalability, no AI capabilities. Replace with modern AI-powered platform that evolves with your business." |

## Objection Handling

| Objection | Response |
|-----------|----------|
| **"Our existing CRM handles customer data fine"** | "CRMs store data, but they don't proactively act on it. Our AI agents continuously monitor subscriber health and take action before problems become churn. Can your current system predict and prevent churn 30-60 days in advance?" |
| **"We already have network monitoring tools"** | "Monitoring tools show you problems after they happen. Our NetworkGuardian AI identifies degraded experiences before customers call to complain, automatically communicating with affected subscribers and escalating infrastructure issues. It's proactive customer success, not reactive monitoring." |
| **"Our customer service metrics are already good"** | "Good metrics in telecom often mean you're successfully handling complaints. Our platform prevents those complaints from happening. Instead of measuring how well you resolve issues, measure how many issues you prevent entirely." |
| **"AI agents sound too automated for customer relationships"** | "Our agents handle the routine work so your team can focus on high-value relationships. Instead of spending time gathering subscriber context from 8 different systems, your CS reps get intelligent summaries and recommendations for every interaction. It's augmentation, not replacement." |
| **"Implementation would be too disruptive"** | "We integrate with your existing billing, network, and CRM systems without replacing them. Our AI agents work with your current tools while providing the unified view and proactive capabilities you're missing. Typical telecom deployment is 4-6 weeks for core functionality." |
| **"The cost doesn't justify the ROI"** | "A 1% churn reduction on 100K subscribers saves $2-5M annually. Our AI agents typically reduce churn by 2-3% while requiring 50-70% less manual effort from your team. The platform pays for itself in 3-6 months through churn prevention alone." |

## Proof Points
*(To be populated with customer references)*

- Major wireless carrier reduced monthly churn from 2.1% to 1.4% using AI-powered subscriber health monitoring
- Regional telecom decreased bill shock incidents by 75% through proactive usage monitoring and alerts
- Enterprise-focused carrier improved SLA compliance from 94% to 99.2% with automated monitoring and escalation
- Family plan specialist team increased cross-sell success rates by 40% using unified account intelligence
- Network operations partnership reduced network-related service calls by 60% through proactive issue identification
- Large carrier completed enterprise onboarding 45% faster using AI-orchestrated project management
- Customer success team managed 3x more subscribers per rep while improving satisfaction scores by 25%

---

*Generated: 2026-02-21 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*