# Investment Banking × PR & Communications Playbook

## Overview

PR & Communications in investment banking is a uniquely constrained function operating at the intersection of reputation management, regulatory compliance, and deal confidentiality. Unlike corporate PR that proactively pitches stories, IB communications teams spend significant time on defensive positioning — managing media inquiries about pending transactions, responding to regulatory actions, navigating activist investor campaigns, and ensuring no material non-public information (MNPI) leaks through public channels. Every press release, social media post, and analyst quote must be vetted through legal and compliance before publication.

At bulge-bracket firms (Goldman Sachs, JP Morgan, Morgan Stanley), communications teams range from 30–80 professionals split across corporate communications, financial communications (earnings, investor relations), media relations, internal communications, digital/social media, and crisis management. Middle-market banks (Jefferies, Piper Sandler, William Blair) operate leaner teams of 5–15. The function typically reports to the CMO, General Counsel, or directly to the CEO depending on the firm's structure and how recently they've had a crisis.

The regulatory dimension is critical: SEC Regulation FD prohibits selective disclosure of material information, FINRA rules govern communications with the public, and securities laws create strict protocols around deal announcements. A premature leak about an M&A advisory engagement can blow up a $5B transaction. An ill-timed social media post by a junior banker can trigger a compliance investigation. PR & Communications serves as both megaphone and shield — amplifying the firm's thought leadership while protecting against reputational and regulatory risk.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | Growing content demands (thought leadership, social, ESG reporting) without proportional headcount increase |
| 2 | Consolidate Tech Stack with AI | Medium-High | Teams juggle media monitoring, CMS, social tools, and email — fragmented workflows slow crisis response |
| 3 | Replace or Radically Augment Headcount | Medium | AI can draft press releases, monitor media sentiment, and compile reports — freeing senior communicators for strategy |

The Three Value Drivers:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases

---

### Use Case 1: Crisis & Issues Management Command Center

**Relevance:** High
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
When a crisis hits an investment bank — a rogue trader incident, a regulatory enforcement action, a data breach, or a high-profile deal collapse — the communications team has minutes, not hours, to respond. Yet crisis response coordination typically happens through a chaotic mix of conference calls, email chains, text messages, and hastily shared Google Docs. There's no single view of: what's the current media narrative, what statements have been issued, who's approved what, what inquiries are outstanding, and who's speaking on background. Post-crisis reviews consistently find the same failures: slow initial response, inconsistent messaging across spokespeople, missed media inquiries, and poor coordination between communications, legal, compliance, and business leadership.

#### The Solution
monday.com as the crisis management command center. A pre-built crisis board template activates when triggered, with items for each workstream: media statement drafting, media inquiry tracking, spokesperson briefing, social media monitoring, internal communications, regulatory notification, and stakeholder outreach. Status columns track each workstream's progress. People columns assign owners. Timeline shows the critical path. Automations ensure legal and compliance approval gates are enforced before any external communication. A real-time dashboard shows crisis status at a glance. Post-crisis, the board becomes the documentation record for lessons learned.

#### The Outcome
Crisis response activation time reduced from 2+ hours to 15 minutes (template pre-built, roles pre-assigned). Zero unauthorized external communications during crisis (approval gates enforced). Complete audit trail for regulatory review. Post-crisis debrief has structured data instead of reconstructed email chains. Reputation damage minimized through faster, more coordinated response.

#### Discovery Questions
1. "Walk me through your last significant media crisis — how did the first 60 minutes unfold in terms of team coordination?"
2. "Do you have pre-built crisis playbooks with assigned roles, or does the team self-organize each time?"
3. "During a crisis, how do you ensure every external statement gets legal and compliance approval before release?"
4. "What's your process for tracking and responding to the flood of media inquiries that come in during a crisis?"
5. "After a crisis resolves, how do you conduct the post-mortem — is the communication timeline easy to reconstruct?"

#### Industry Context
Banking crises are uniquely high-stakes because they can trigger market reactions (stock price impact), regulatory scrutiny (SEC/OCC/Fed investigations), and customer flight (depositor concerns). The 2008 financial crisis, the LIBOR scandal, Wells Fargo fake accounts, and Credit Suisse's collapse are all case studies in how communications can accelerate or mitigate institutional damage. Reg FD implications mean that even crisis communications must be carefully calibrated to avoid selective disclosure. The "golden hour" principle applies: the first hour of crisis response often determines the narrative trajectory.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Crisis Management Command Center for an investment bank. Create a board called 'Crisis Response - [ACTIVE]' with these columns: Workstream (dropdown: Media Statement, Media Inquiries, Spokesperson Briefing, Social Media, Internal Comms, Regulatory Notification, Client Outreach, Executive Briefing, Legal Review), Owner (people), Status (status: Not Started, In Progress, Awaiting Approval, Approved, Published, Complete), Priority (status: Critical, High, Medium), Legal Approved (status: Pending, Approved, Changes Required, N/A), Compliance Approved (status: Pending, Approved, Changes Required, N/A), Deadline (date), Actual Completion (date), Channel (dropdown: Press Release, Media Statement, Background Brief, Social Media, Internal Email, Town Hall, Regulatory Filing, Client Letter), Target Audience (dropdown: Media, Employees, Regulators, Clients, Shareholders, General Public), Draft Content (long text), Approved Content (long text), Notes (long text). Add a group called 'Media Inquiry Tracker' with columns: Outlet (text), Reporter (text), Inquiry (text), Deadline (date), Response Status (status: Received, Drafting Response, Legal Review, Responded, Declined, No Comment), Assigned Spokesperson (people). Add automations: when Status changes to Awaiting Approval, notify Legal and Compliance reviewers. When both Legal Approved and Compliance Approved are Approved, change Status to Approved. When a new item is created in Media Inquiry Tracker, notify Head of Communications immediately. Create a Dashboard with: count of open workstreams by status, media inquiry response times, timeline of all actions taken (for post-crisis review), count of outstanding approvals. Create a Timeline view showing all workstream deadlines."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CrisisShield
**Agent Purpose:** Activate crisis protocols, monitor media sentiment in real-time, track inquiry response SLAs, and ensure no unapproved communications are released.

**Triggers:**
- Crisis board manually activated by Head of Communications
- Media inquiry volume exceeds threshold (5+ in 1 hour on same topic)
- Social media sentiment score drops below critical threshold
- Regulatory filing deadline approaching
- Spokesperson briefing not completed within 30 minutes of crisis activation

**Actions:**
- Activate crisis board from template with pre-assigned roles based on crisis type
- Generate initial holding statement draft based on crisis category and approved language library
- Track media inquiry SLAs and escalate approaching deadlines
- Monitor social media mentions and sentiment, flagging viral negative content
- Send real-time status updates to executive team
- Compile post-crisis timeline report with all actions, approvals, and outcomes

**Data Required:**
- Approved crisis response templates by scenario type
- Spokesperson roster with availability and topic expertise
- Media contact database with outlet/reporter profiles
- Social media monitoring feeds
- Legal/compliance approval workflows

**Autonomy Level:** Human-in-the-Loop
Crisis activation and holding statement drafts are autonomous. All external communications require explicit human approval. Media inquiry responses are drafted but never sent without spokesperson review. Sentiment monitoring and escalation alerts are fully autonomous.

**Example Interaction:**
> At 6:47 AM, a major financial news outlet breaks a story alleging the bank's involvement in a sanctions evasion scheme. CrisisShield detects the story through media monitoring and immediately activates the "Regulatory/Legal Crisis" board template. It assigns the General Counsel as crisis lead, the Head of Media Relations as spokesperson coordinator, and pre-populates a holding statement: "We are aware of the media report and are reviewing the allegations. [Bank] maintains robust compliance programs and takes all regulatory obligations seriously. We will provide further comment at the appropriate time." The statement is routed to Legal and Compliance for approval. Simultaneously, the agent begins tracking the 14 media inquiries that arrive within the first 30 minutes, prioritizing Bloomberg, Reuters, and the WSJ by deadline. It flags that two inquiries reference specific deal names — potential MNPI concern — and escalates those directly to the General Counsel.

---

### Use Case 2: Thought Leadership & Content Pipeline

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Investment banks compete aggressively for advisory mandates, and thought leadership is a critical differentiator. Clients choose advisors who demonstrate deep sector expertise through published research, conference presentations, media commentary, and digital content. Yet producing this content is painful: senior bankers have the expertise but no time to write, communications teams have writing skills but need banker input, and the approval process (compliance review under FINRA 2210 for communications with the public) adds weeks to publication timelines. The result: a backlog of half-written thought pieces, missed market moments, and inconsistent content quality across practice groups.

#### The Solution
monday.com as the content pipeline manager. Each content piece is an item with columns for topic, author (banker), ghostwriter (comms team), content type, target publication date, status, compliance review status, and distribution channels. Automations manage the workflow: interview scheduled → draft created → banker review → compliance review → design → publish → distribute. Calendar views show the editorial calendar. Dashboards track content output by practice group, pipeline health, and average time-to-publish. Templates standardize content formats (market commentary, sector outlook, deal perspective).

#### The Outcome
3x increase in published thought leadership content. Average time-to-publish reduced from 6 weeks to 2 weeks. Every practice group has a visible content pipeline. Compliance review bottleneck identified and addressed with dedicated reviewer assignment. Senior bankers spend 30 minutes on an interview instead of 5 hours struggling with a draft.

#### Discovery Questions
1. "How many thought leadership pieces did your firm publish last year across all practice groups, and how does that compare to competitors?"
2. "What's your current process for turning a banker's market insights into published content — is there a structured workflow or ad-hoc?"
3. "How long does compliance review typically take for external publications, and is that a bottleneck?"
4. "Do you have an editorial calendar that coordinates content across sectors, products, and regions?"
5. "How do you measure the impact of thought leadership on mandate generation or brand positioning?"

#### Industry Context
FINRA Rule 2210 governs all communications with the public by member firms, requiring pre-approval of certain content types. Compliance review isn't optional — it's regulatory. Content types in IB include: sector outlooks, M&A market commentary, capital markets updates, regulatory impact analyses, deal case studies (carefully anonymized), conference presentations, podcast appearances, and LinkedIn articles. The rise of LinkedIn as a business development channel has increased content volume expectations dramatically — MDs are now expected to maintain active professional profiles.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Thought Leadership Content Pipeline for an investment bank. Create a board called 'Content Pipeline' with these columns: Title (text), Content Type (dropdown: Market Commentary, Sector Outlook, Deal Perspective, Regulatory Analysis, Conference Presentation, Podcast, LinkedIn Article, Bylined Article, White Paper, Video), Practice Group (dropdown: M&A Advisory, Capital Markets, Leveraged Finance, Restructuring, Private Capital, Financial Sponsors), Author/SME (people), Ghostwriter (people), Target Publication Date (date), Status (status: Ideation, Interview Scheduled, Drafting, Banker Review, Compliance Review, Design, Ready to Publish, Published, Archived), Compliance Status (status: Not Submitted, Under Review, Approved, Changes Required, Approved with Conditions), Compliance Reviewer (people), FINRA Filing Required (status: Yes, No, TBD), Distribution Channels (dropdown: Website, LinkedIn, Email Newsletter, Wire Service, Media Pitch, Conference, Podcast Platform), Word Count Target (numbers), Actual Word Count (numbers), Priority (status: Flagship, Standard, Opportunistic), Related Deals or Events (text), Attachments (files). Add automations: when Status changes to Compliance Review, assign Compliance Reviewer and set 5-day SLA. When Compliance Status is Approved, change Status to Design. When Status changes to Published, notify Author/SME and practice group leadership. When Target Publication Date is within 7 days and Status is before Ready to Publish, notify Ghostwriter and Content Manager. Create a Dashboard with: content published this quarter vs. target (numbers widget), pipeline by status (funnel chart), content by Practice Group (bar chart), average time-to-publish (numbers widget), compliance review average turnaround (numbers widget). Create a Calendar view showing the editorial calendar. Create a Kanban view grouped by Status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ContentEngine IB
**Agent Purpose:** Identify content opportunities from market events, draft initial content from banker interviews, and manage the editorial pipeline to publication.

**Triggers:**
- Major market event detected (rate decision, significant M&A announcement, regulatory change)
- Content piece approaching publication deadline with incomplete status
- Banker interview completed (recording uploaded)
- Compliance review exceeding SLA
- Monthly content quota review

**Actions:**
- Generate content opportunity briefs based on market events mapped to practice group expertise
- Transcribe banker interviews and create structured first drafts
- Send automated reminders for content in review stages
- Compile monthly content performance report (views, engagement, leads attributed)
- Suggest content repurposing opportunities (e.g., white paper → 3 LinkedIn posts + podcast talking points)
- Flag trending industry topics where the firm has no planned content

**Data Required:**
- Market news feeds and event data
- Banker expertise profiles by sector and product
- Historical content performance metrics
- Compliance review rules and approved language library
- Editorial calendar and quotas by practice group

**Autonomy Level:** Human-in-the-Loop
Content opportunity identification and first draft generation are autonomous. All content requires banker review and compliance approval before publication. Reminder notifications are fully autonomous. Repurposing suggestions require editorial decision.

**Example Interaction:**
> The Federal Reserve announces an unexpected rate hold. ContentEngine IB immediately identifies this as a content opportunity for the Leveraged Finance, Capital Markets, and Real Estate practice groups. It creates three content items: a Leveraged Finance market commentary on financing implications, a Capital Markets perspective on issuance windows, and a Real Estate sector impact note. For each, it identifies the appropriate senior banker author, drafts a 2-paragraph pitch for their review, and proposes a 48-hour turnaround for maximum market relevance. It also notes that the firm published a rate outlook piece 3 months ago and suggests referencing it for continuity. Within an hour, two of the three bankers have approved their topics, and the ghostwriting team has interviews scheduled for the next morning.

---

### Use Case 3: Media Relations & Journalist Relationship Tracking

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banking media relations is relationship-driven — the same 200–300 financial journalists at Bloomberg, Reuters, WSJ, FT, CNBC, and sector-specific publications cover the industry. Knowing which reporter covers which sector, their publication patterns, their sentiment toward your firm, and their upcoming story angles is critical intelligence. Yet most banks manage media relationships through senior communicators' personal contact lists, fragmented CRM entries, and institutional memory. When a key communicator leaves, those relationships — and the intelligence — go with them. Meanwhile, tracking media coverage, share of voice, and sentiment is manual and retrospective.

#### The Solution
monday.com CRM adapted for media relationship management. Each journalist is a contact with fields for outlet, beat, coverage areas, key stories published, relationship status, preferred contact method, and interaction history. Connected boards link journalists to firm spokespeople and practice groups. Each media interaction (briefing, interview, pitch, inquiry) is logged as an activity. Dashboards show media coverage volume, sentiment trends, share of voice vs. competitors, and relationship health scores. Automations schedule regular relationship maintenance (quarterly check-ins with top-tier reporters).

#### The Outcome
Complete institutional memory of media relationships — survives personnel changes. Share of voice tracking enables competitive benchmarking. Proactive relationship management leads to more favorable coverage positioning. Media team efficiency increases 25% through structured interaction tracking vs. ad-hoc email management.

#### Discovery Questions
1. "If your Head of Media Relations left tomorrow, how much institutional knowledge about journalist relationships would walk out the door?"
2. "Do you currently track share of voice versus competitors like Goldman, JP Morgan, or Morgan Stanley in your target media outlets?"
3. "How do you decide which spokesperson to offer for a journalist briefing on a specific topic?"
4. "What's your cadence for proactive media outreach versus reactive inquiry response?"
5. "Can you quickly identify which journalists have covered your firm's deals in the last 12 months and what the sentiment was?"

#### Industry Context
Financial journalism operates on tight deadlines and deep source relationships. A Bloomberg reporter on the M&A beat may break 3–5 deal stories per week, sourcing from a network of bankers, lawyers, and communications professionals. Being a trusted source means getting the call for comment before publication — which is your opportunity to shape the narrative. The relationship between bank communications and financial media is symbiotic: reporters need sources and quotes; banks need coverage and positioning. Understanding each outlet's editorial focus (Bloomberg = speed, FT = analysis, WSJ = enterprise stories) is essential.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Media Relations Management system for an investment bank. Create a board called 'Media Contacts' with these columns: Journalist Name (text), Outlet (dropdown: Bloomberg, Reuters, Wall Street Journal, Financial Times, CNBC, New York Times, Barron's, Institutional Investor, The Deal, Mergermarket, Private Equity International, Other), Beat (dropdown: M&A, Capital Markets, Banking/Finance, Technology, Healthcare, Energy, Real Estate, Regulatory, General Business), Email (email), Phone (phone), Relationship Tier (dropdown: Tier 1 - Regular Contact, Tier 2 - Periodic Contact, Tier 3 - As Needed), Relationship Owner (people), Last Interaction Date (date), Next Planned Outreach (date), Sentiment Toward Firm (status: Positive, Neutral, Skeptical, Unknown), Key Recent Stories (long text), Preferred Contact Method (dropdown: Email, Phone, Text, Twitter DM), Notes (long text). Create a connected board called 'Media Interactions' with: Date (date), Journalist (connect to Media Contacts), Type (dropdown: Proactive Pitch, Reactive Inquiry, Background Brief, On-Record Interview, Off-Record Conversation, Event Meeting, Social Media Engagement), Topic (text), Spokesperson Used (people), Outcome (status: Story Published, Positive Mention, No Coverage, Negative Coverage, Pending, Declined), Story Link (link), Notes (long text). Add automations: when Last Interaction Date is more than 90 days ago for Tier 1 journalists, notify Relationship Owner to schedule outreach. When a new Media Interaction is logged, update Last Interaction Date on the journalist record. Create a Dashboard with: total interactions this month (numbers), interactions by type (pie chart), coverage sentiment distribution (chart), Tier 1 relationship health (table showing days since last contact), media coverage timeline."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MediaPulse
**Agent Purpose:** Monitor media coverage, maintain journalist relationship intelligence, and proactively identify media engagement opportunities.

**Triggers:**
- New article published mentioning the firm or competitors
- Tier 1 journalist contact dormant for 60+ days
- Major deal announcement (coordinate spokesperson availability)
- Quarterly media metrics reporting schedule
- Journalist beat change or outlet move detected

**Actions:**
- Parse daily media coverage and update sentiment scores, coverage volume, and share of voice metrics
- Generate journalist briefing cards before scheduled interactions (recent coverage, topics of interest, relationship history)
- Recommend spokesperson matches for incoming media inquiries based on topic expertise and journalist preferences
- Compile quarterly media performance report (coverage volume, sentiment, share of voice vs. competitors)
- Alert communications team when a journalist's coverage pattern shifts (new focus area, increased competitor coverage)
- Update journalist records when beat or outlet changes are detected

**Data Required:**
- Media monitoring feeds (Meltwater, Cision, or similar)
- Journalist database with historical interaction data
- Spokesperson profiles and topic expertise
- Competitor media coverage data
- Deal announcement calendar

**Autonomy Level:** Fully Autonomous for monitoring and reporting; Human-in-the-Loop for engagement recommendations
Media parsing, sentiment scoring, and reporting run without human intervention. Spokesperson recommendations and proactive outreach suggestions require communications team approval. No autonomous external communication with journalists.

**Example Interaction:**
> MediaPulse detects that Sarah Chen at the Wall Street Journal, a Tier 1 contact who typically covers technology M&A, has published three articles in the past week about healthcare M&A — a beat shift. The agent updates her journalist profile, cross-references with the firm's Healthcare M&A practice group, and suggests to the Media Relations Director: "Sarah Chen appears to be expanding into healthcare M&A coverage. She has a positive relationship history with the firm (8 interactions, 5 resulting in favorable coverage). Recommend scheduling a background briefing with Dr. James Walsh (Healthcare M&A MD) to establish the firm as a source on her new beat. Suggested topics based on her recent articles: healthcare AI acquisitions, pharma mega-mergers, and healthcare PE exit activity."

---

### Use Case 4: Deal Announcement & Transaction Communications

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Every completed M&A transaction, IPO, or debt offering represents a communications opportunity — and a compliance minefield. The deal announcement process involves coordinating between the bank's communications team, the client's PR team, legal counsel on both sides, and compliance. Timing is critical: announcements must align with market hours, SEC filing schedules, and client preferences. The press release must be precisely worded (no forward-looking statements without safe harbor language, accurate deal terms, correct client attribution). Yet the process is managed through email chains with version-controlled Word documents, leading to version confusion, missed approvals, and occasionally embarrassing errors in published releases (wrong deal value, misspelled client name).

#### The Solution
monday.com as the deal announcement workflow engine. Each deal announcement is an item with columns for deal name, deal type, target announcement date/time, client PR contact, legal reviewer, compliance reviewer, status, and all content versions. The workflow progresses through stages: Draft → Client Review → Legal Review → Compliance Review → Final Approval → Scheduled → Published. File columns maintain version history. Automations enforce approval gates and send reminders. A calendar view shows the announcement pipeline. Templates for different deal types (M&A, IPO, debt offering, restructuring) ensure no required elements are missed.

#### The Outcome
Announcement errors reduced to near-zero through structured review workflow. Time from deal close to announcement reduced by 40% through parallel review streams. Complete audit trail for every approval. Communications team can manage 3x more concurrent deal announcements without additional headcount. Client satisfaction improves with professional, timely announcements.

#### Discovery Questions
1. "How many deal announcements does your team manage in a typical quarter, and what's the coordination process with client PR teams?"
2. "Have you ever had an error in a published deal announcement — wrong terms, misspelling, premature release?"
3. "What's your average turnaround from deal close to published announcement, and is that competitive with your peers?"
4. "How do you manage the approval chain when legal, compliance, and the client all need to sign off on the same release?"
5. "Do you have standardized templates for different deal types, or does each announcement start from scratch?"

#### Industry Context
Deal announcements in investment banking are governed by securities law. Material transactions involving public companies require coordination with SEC filing timelines. Press releases about M&A transactions must carefully distinguish between signed and closed deals. Safe harbor language protects against forward-looking statement liability. The bank typically provides "tombstone" credit in announcements, and the positioning of this credit (sole advisor vs. joint advisor, positioning relative to other banks) is politically significant. Announcement timing — pre-market, post-market, or during trading hours — is strategically chosen based on expected market reaction.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Deal Announcement Management system for an investment bank. Create a board called 'Deal Announcements' with columns: Deal Name (text), Deal Type (dropdown: M&A Sell-Side, M&A Buy-Side, IPO, Follow-On Offering, Debt Offering, Restructuring, Private Placement, Joint Venture), Deal Value (numbers, USD), Client Name (text), Client PR Contact (text), Target Announcement Date (date), Target Announcement Time (dropdown: Pre-Market 7AM, Market Open 9:30AM, Midday, Post-Market 4PM, After Hours), Status (status: Intake, Drafting, Client Review, Legal Review, Compliance Review, Final Approval, Scheduled, Published, On Hold), Bank Role (dropdown: Sole Financial Advisor, Lead Financial Advisor, Joint Financial Advisor, Co-Manager, Bookrunner), Draft Version (numbers), Press Release Draft (files), Final Approved Version (files), Comms Lead (people), Legal Reviewer (people), Compliance Reviewer (people), Client Approved (status: Pending, Approved, Changes Requested), Legal Approved (status: Pending, Approved, Changes Required), Compliance Approved (status: Pending, Approved, Changes Required), Distribution Channels (dropdown: Wire Service, Website, Social Media, Email, All), SEC Filing Coordination Required (status: Yes, No), Notes (long text). Add automations: when Client Approved AND Legal Approved AND Compliance Approved all are Approved, change Status to Final Approval and notify Comms Lead. When Status changes to Client Review, notify Client PR Contact field via email. When Target Announcement Date is tomorrow and Status is not Scheduled or Published, send urgent alert to Comms Lead. Create a Dashboard with: announcements published this quarter (numbers), pipeline by status (funnel), deal value of pending announcements (sum), announcement timeline (calendar), average cycle time from Intake to Published. Create a Calendar view and a Kanban view grouped by Status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** AnnouncePro
**Agent Purpose:** Orchestrate deal announcement workflows, draft initial press releases from deal data, and ensure all approvals are completed before publication.

**Triggers:**
- New deal announcement request created
- Approval status change on any reviewer
- Target announcement date within 48 hours with incomplete approvals
- Deal terms update requiring press release revision
- Post-announcement media coverage to track

**Actions:**
- Generate initial press release draft from deal data template (deal type, value, parties, bank role)
- Route drafts through approval workflow with parallel streams where possible
- Track client PR team review status and send follow-up reminders
- Verify all required elements present (safe harbor language, regulatory disclaimers, accurate figures)
- Coordinate announcement timing with SEC filing schedule when required
- Compile post-announcement media coverage summary

**Data Required:**
- Deal data (type, value, parties, terms)
- Press release templates by deal type
- Required regulatory language library
- Client PR contact information
- Media monitoring feeds for post-announcement tracking

**Autonomy Level:** Human-in-the-Loop
Draft generation and workflow routing are autonomous. All content approvals require human review. Announcement timing and publication are human-controlled. Post-announcement media monitoring is fully autonomous.

**Example Interaction:**
> A senior VP in M&A notifies communications that Project Evergreen — a $3.4B acquisition of a healthcare services company — is closing tomorrow. AnnouncePro creates the announcement item, pulls the deal template for "M&A Sell-Side," and generates a first draft incorporating the deal value, party names, and the bank's role as sole financial advisor. It routes the draft simultaneously to legal (standard 24-hour review) and the client's PR team (via their designated contact), while flagging for Compliance that the target is a public company requiring SEC filing coordination. It sets the announcement for post-market (4:00 PM ET) aligned with the client's 8-K filing. When legal requests a change to the regulatory language, the agent updates the draft, re-routes to all reviewers with tracked changes highlighted, and recalculates the approval timeline — still on track for tomorrow's target.

---

### Use Case 5: Internal Communications & Employee Engagement

**Relevance:** Medium
**Value Driver:** Scale Impact Without Overhead

#### The Pain
Internal communications at investment banks face unique challenges: a globally distributed workforce across time zones (New York, London, Hong Kong, Mumbai), strict information barriers between advisory and trading divisions, a culture that undervalues "soft" communication, and high-pressure environments where employees barely read emails. Yet the need for effective internal comms is acute: regulatory changes affecting daily work, organizational restructurings, diversity & inclusion initiatives, technology migrations, and maintaining culture during remote/hybrid work. Most banks send internal newsletters that nobody reads, host town halls that only a fraction attend, and rely on managers to cascade critical information (which they often don't).

#### The Solution
monday.com as the internal communications planning and execution hub. Each communication is an item with columns for topic, audience segment, channel, approval status, publish date, and effectiveness metrics. Audience segmentation (by division, region, seniority, information barrier status) ensures the right messages reach the right people. Campaign boards manage multi-touch communications (e.g., a technology migration needs: announcement → FAQ → training schedule → go-live reminder → feedback collection). Dashboards track communication cadence, channel effectiveness, and coverage gaps.

#### The Outcome
Internal communication reach increases from ~30% to ~70% through multi-channel, segmented approach. No more compliance violations from sending deal-related updates across information barriers. Leadership has visibility into communication cadence and employee sentiment. Change management communications (technology, organizational) delivered systematically instead of ad-hoc.

#### Discovery Questions
1. "What's your estimated open rate for firm-wide internal communications, and how do you measure it?"
2. "How do you ensure information barrier compliance when sending internal communications — is it manual or systematic?"
3. "When you need to communicate a major organizational change, what's the cascade process from announcement to every affected employee?"
4. "How do you currently plan internal communications — is there an editorial calendar or is it reactive?"
5. "What's your biggest challenge in reaching front-office staff (bankers, traders) with internal messages?"

#### Industry Context
Information barriers (Chinese walls) in investment banking create unique internal communications challenges. The compliance team must review any communication that crosses divisional boundaries to ensure no MNPI leakage. Internal communications about deals-in-progress are restricted to involved parties. Town halls must be carefully scripted to avoid inadvertent disclosure. Employee engagement surveys in banking consistently show that front-office staff feel disconnected from corporate communications, while back-office staff feel overlooked in favor of revenue-generating divisions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Internal Communications Hub for an investment bank. Create a board called 'Internal Comms Calendar' with columns: Topic (text), Communication Type (dropdown: All-Hands Email, Town Hall, Newsletter, Intranet Post, Video Message, Manager Cascade, Team Briefing, Targeted Alert), Audience Segment (dropdown: Firm-Wide, Advisory Division, Capital Markets, Sales & Trading, Research, Corporate Functions, Region-Americas, Region-EMEA, Region-APAC, Leadership Only), Information Barrier Review Required (status: Yes, No, Completed), Author (people), Approver (people), Compliance Reviewer (people), Status (status: Planning, Drafting, Review, Approved, Scheduled, Sent, Cancelled), Publish Date (date), Channel (dropdown: Email, Intranet, Slack, Video Platform, In-Person, Multi-Channel), Priority (status: Routine, Important, Urgent, Mandatory Read), Estimated Reach (numbers), Actual Reach (numbers), Engagement Rate (numbers), Content (long text), Attachments (files). Add automations: when Information Barrier Review Required is Yes, Status cannot move past Drafting until Compliance Reviewer approves. When Publish Date is tomorrow and Status is not Approved, alert Author and Approver. When Status changes to Sent, prompt for Actual Reach and Engagement Rate entry after 48 hours. Create a Dashboard with: communications sent this month (numbers), reach by audience segment (chart), engagement rate trends (line chart), upcoming communications calendar, information barrier compliance rate. Create a Calendar view showing the full editorial calendar."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** InternalPulse
**Agent Purpose:** Plan, segment, and optimize internal communications while enforcing information barrier compliance.

**Triggers:**
- New internal communication scheduled
- Information barrier review required for cross-divisional message
- Major firm event (earnings, reorganization, regulatory change)
- Monthly engagement metrics review
- Communication scheduled for audience with known low engagement

**Actions:**
- Auto-classify communications by information barrier sensitivity
- Suggest optimal send times based on historical engagement data by audience segment
- Generate multi-channel distribution plan for high-priority messages
- Flag communications that may cross information barriers for compliance review
- Compile monthly internal communications effectiveness report
- Recommend content format adjustments based on audience engagement patterns

**Data Required:**
- Employee directory with division, region, and seniority data
- Information barrier group definitions
- Historical communication engagement metrics
- Internal events calendar
- Compliance rules for cross-divisional communications

**Autonomy Level:** Escalation-Based
Scheduling optimization and format suggestions are autonomous. Information barrier flagging triggers mandatory compliance review. Content approval always requires human sign-off. Distribution is autonomous once approved.

**Example Interaction:**
> The CHRO wants to announce a new parental leave policy firm-wide. InternalPulse classifies this as information-barrier-safe (no deal or trading content), suggests a multi-channel approach: CEO video message (high engagement with front-office), intranet FAQ page (reference), manager cascade brief (ensures team-level discussion), and targeted follow-up to HR business partners by region. Based on historical data, it recommends sending the CEO email on Tuesday at 8:00 AM ET / 1:00 PM GMT / 9:00 PM HKT for maximum global reach. It also notes that the last firm-wide policy communication had only 34% engagement and suggests adding an interactive element — a pulse survey asking employees to rate the policy — to boost read-through.

---

### Use Case 6: Social Media & Digital Presence Management

**Relevance:** Medium
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Investment banks are increasingly active on LinkedIn, Twitter/X, and occasionally Instagram (for recruiting and culture content). Yet social media in a regulated financial services environment is fraught with compliance risk. Every post that could be construed as investment advice, market commentary, or deal promotion must be pre-approved under FINRA 2210. Individual banker social media activity is technically subject to the same rules but practically impossible to monitor at scale. The communications team struggles to maintain a consistent posting cadence across firm accounts while managing the approval queue, tracking engagement metrics, and monitoring employee social activity for compliance violations.

#### The Solution
monday.com as the social media command center. A content calendar board manages all planned posts with columns for platform, content, visual assets, compliance status, scheduled publish date/time, and engagement metrics. Each post flows through: Draft → Compliance Review → Approved → Scheduled → Published. Connected boards track employee social media guidelines compliance. Dashboards show posting cadence, engagement metrics by platform and content type, and compliance review backlog. Templates for recurring content types (deal tombstones, thought leadership shares, recruiting posts) accelerate production.

#### The Outcome
Posting cadence increases 2x with same team size through workflow automation. 100% compliance pre-approval for firm account posts. Engagement metrics tracked systematically, enabling content optimization. Employee social media guidelines communicated and monitored. Brand consistency maintained across all platforms and regions.

#### Discovery Questions
1. "How many social media posts does your firm publish per week across all platforms, and what's the compliance review process?"
2. "Do you have a policy for individual banker social media activity, and how is it monitored?"
3. "What's your average turnaround time from social media content creation to publication, including compliance review?"
4. "How do you track social media engagement and ROI — is it systematic or ad-hoc?"
5. "Have you ever had a compliance issue related to social media — an employee post that needed to be taken down, for example?"

#### Industry Context
FINRA Rule 2210 classifies social media as either "correspondence" (one-to-one) or "institutional/retail communication" (one-to-many), with different review requirements. The SEC has issued guidance clarifying that social media posts by registered representatives are subject to the same rules as traditional advertising. LinkedIn is the primary professional platform for IB; Twitter/X is used for market commentary and news sharing; Instagram is emerging for employer branding and campus recruiting. Many banks use archiving tools (Smarsh, Global Relay) to capture social media activity for regulatory recordkeeping.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Social Media Management system for an investment bank. Create a board called 'Social Media Calendar' with columns: Post Title (text), Platform (dropdown: LinkedIn Company, LinkedIn Executive, Twitter/X, Instagram, YouTube, Facebook), Content Category (dropdown: Deal Tombstone, Thought Leadership, Market Commentary, Recruiting, Culture & ESG, Event Promotion, Award & Recognition, Industry News Share), Post Copy (long text), Visual Asset (files), Video Link (link), Hashtags (text), Author/Speaker (people), Compliance Status (status: Not Submitted, Under Review, Approved, Rejected, Revision Required), FINRA Classification (dropdown: Institutional Communication, Retail Communication, Correspondence, Not Applicable), Compliance Reviewer (people), Scheduled Date (date), Scheduled Time (dropdown: 8AM ET, 9AM ET, 12PM ET, 3PM ET, 5PM ET, Custom), Published (status: Pending, Published, Failed), Engagement - Impressions (numbers), Engagement - Likes (numbers), Engagement - Comments (numbers), Engagement - Shares (numbers), Engagement - Click-Through (numbers), Campaign (text). Add automations: when Content Category is Market Commentary or Deal Tombstone, auto-set FINRA Classification to Institutional Communication and assign Compliance Reviewer. When Compliance Status is Approved, change Published to Pending and schedule for Scheduled Date/Time. When Published changes to Published, prompt for engagement metrics after 72 hours. Create a Dashboard with: posts published this week (numbers), engagement by platform (bar chart), engagement by content category (chart), compliance review turnaround average (numbers), posting cadence trend (line chart), top performing posts (table sorted by engagement). Create a Calendar view showing the full social calendar."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SocialCompliance IB
**Agent Purpose:** Manage social media content pipeline, ensure regulatory compliance, and optimize engagement through data-driven scheduling.

**Triggers:**
- New social media post drafted
- Compliance review pending for >24 hours
- Engagement metrics imported (72 hours post-publication)
- Deal closing (trigger tombstone post creation)
- Executive LinkedIn post submitted for review

**Actions:**
- Generate tombstone post drafts from deal announcement data
- Route posts through FINRA-appropriate compliance review workflow
- Analyze engagement patterns and recommend optimal posting times by platform
- Flag employee social media activity that may violate firm guidelines
- Compile weekly social media performance report with competitive benchmarking
- Suggest content repurposing (thought leadership article → LinkedIn carousel + tweet thread)

**Data Required:**
- Deal announcement data for tombstone generation
- FINRA classification rules
- Historical engagement data by platform, content type, and posting time
- Employee social media policy guidelines
- Competitor social media activity for benchmarking

**Autonomy Level:** Human-in-the-Loop
Tombstone draft generation and scheduling recommendations are autonomous. All posts require human review and compliance approval. Employee social media monitoring flags are reviewed by compliance before any action. Performance reporting is fully autonomous.

**Example Interaction:**
> The Capital Markets team just closed a $1.2B IPO for a cybersecurity company. SocialCompliance IB pulls the published press release, generates a LinkedIn tombstone post with approved messaging ("Congratulations to [Client] on their successful IPO. [Bank] served as joint bookrunner."), attaches the standard tombstone graphic template with deal details populated, and routes to the Compliance reviewer with a note: "Institutional Communication — FINRA pre-approval required." It also generates a tweet-length version and an Instagram story graphic for the recruiting account. Based on engagement data, it schedules the LinkedIn post for Tuesday 9:00 AM ET (highest average engagement for deal tombstones) and the tweet for 30 minutes later. The compliance reviewer approves all three within 2 hours, and the posts are queued.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Reg FD | SEC Regulation Fair Disclosure — prohibits selective disclosure of material non-public information |
| MNPI | Material Non-Public Information — information that could influence an investor's decision, not yet publicly available |
| FINRA 2210 | FINRA rule governing communications with the public by member firms |
| Safe Harbor | Legal disclaimer protecting forward-looking statements in press releases from liability |
| Tombstone | A formal advertisement or social media post announcing a completed deal and the bank's role |
| Information Barrier (Chinese Wall) | Internal controls separating divisions to prevent MNPI leakage |
| Share of Voice | Metric measuring a firm's media coverage relative to competitors |
| Background Briefing | Off-the-record conversation with a journalist to provide context without direct attribution |
| Wire Service | News distribution service (BusinessWire, PR Newswire) used for press release distribution |
| 8-K Filing | SEC filing for material events, often coordinated with press release timing |
| Holding Statement | Pre-approved reactive statement used in early crisis response before full messaging is developed |
| Beat | A journalist's area of regular coverage (e.g., "M&A beat" or "banking regulation beat") |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Communications Officer (CCO) | Overall communications strategy, crisis management, executive positioning | Decision-maker |
| Head of Media Relations | Journalist relationships, media strategy, spokesperson coordination | Decision-maker (media) |
| Head of Internal Communications | Employee engagement, leadership messaging, change management comms | Decision-maker (internal) |
| Head of Digital/Social Media | Social media strategy, digital content, online brand management | Influencer |
| Financial Communications Director | Earnings communications, investor relations support, deal announcements | Decision-maker (financial comms) |
| Communications Compliance Officer | FINRA 2210 review, Reg FD compliance, social media policy enforcement | Decision-maker (compliance) |
| Chief Marketing Officer (CMO) | Brand strategy, marketing-communications alignment, thought leadership direction | Decision-maker (brand) |
| Managing Director (Business) | Subject matter expert for thought leadership, spokesperson for sector coverage | Influencer (content source) |
| General Counsel | Crisis communications legal review, press release approval, disclosure obligations | Decision-maker (legal) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Marketing | Brand strategy, event marketing, client communications, digital presence | Unified content pipeline and brand management platform |
| Legal | Press release approval, crisis management, regulatory disclosure | Integrated approval workflows reducing cycle time |
| Compliance | FINRA 2210 review, social media monitoring, Reg FD compliance | Streamlined compliance review with SLA tracking |
| HR | Employer branding, recruiting communications, internal engagement | Joint internal/external employer brand management |
| Sales & Trading | Market commentary content, social media thought leadership | Structured content creation from trading desk insights |
| Investor Relations | Earnings communications, shareholder messaging, analyst day coordination | Coordinated financial communications calendar |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Meltwater | Media monitoring and PR analytics | Strong for monitoring but poor for workflow management; doesn't manage content production or approvals |
| Cision | Media database and press release distribution | Distribution tool, not a workflow platform; no compliance review integration |
| Sprout Social / Hootsuite | Social media management and scheduling | Consumer-focused; lacks FINRA compliance workflows essential for financial services |
| Staffbase | Internal communications platform | Point solution for internal only; doesn't connect to external comms workflows |
| SharePoint / Confluence | Document collaboration for content drafting | Static document stores; no workflow automation, no compliance gates, no real-time dashboards |
| Email + Shared Drives | The actual incumbent | Fragmented, no audit trail, no workflow enforcement, crisis response is chaotic |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We use Meltwater/Cision for our PR needs" | "Those are excellent monitoring and distribution tools — keep using them. monday.com orchestrates the workflow around them: content production, approval chains, crisis coordination, and cross-functional collaboration that Meltwater can't do." |
| "Compliance will never approve another tool for communications" | "monday.com actually makes compliance easier — every FINRA review has an audit trail, every approval is documented, and nothing gets published without the right sign-offs. It solves the compliance documentation problem, not adds to it." |
| "Our team is too small to justify a platform" | "A small team with big responsibilities is exactly who benefits most. When you're managing deal announcements, crisis response, thought leadership, social media, and internal comms with 8 people, you need automation — not more headcount." |
| "We can't put sensitive deal information in a cloud tool" | "monday.com offers enterprise-grade security, SOC 2 Type II, SSO, and data residency options. The deal information in your communications workflow is already in the public domain or about to be. But we can absolutely design the workspace to handle pre-announcement sensitive data appropriately." |
| "Our bankers won't engage with communications processes" | "The banker touchpoint is minimal — a 20-minute interview that your team turns into thought leadership, or a draft review that takes 5 minutes on their phone. monday.com makes it easy for them to participate without disrupting their workflow." |

## Proof Points
*(To be populated with customer references)*
- [Placeholder for financial services communications team case studies]
- [Placeholder for crisis management platform implementation references]
- [Placeholder for regulated industry content management references]

---

*Generated: February 19, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
