# Colleges & Universities × PR & Communications Playbook

## Overview

Public Relations and Communications departments in higher education institutions serve as the primary voice of the university to the outside world — managing media relations, crisis communications, alumni engagement messaging, donor stewardship narratives, and institutional branding across an extraordinarily diverse set of stakeholders. Unlike corporate PR teams, university communications must navigate shared governance structures, academic freedom considerations, and the unique challenge of representing a community of tens of thousands of students, faculty, researchers, and staff — each with their own stories and sometimes conflicting interests.

These departments typically report to the Vice President of University Relations or the Chief Communications Officer, and range from lean 5-person teams at small liberal arts colleges to 50+ person operations at flagship research universities with dedicated sub-teams for media relations, social media, internal communications, crisis management, research communications, and government/community affairs. They operate in a 24/7 news cycle where a single student protest, Title IX investigation, or faculty controversy can dominate national headlines within hours. The rise of social media has amplified this pressure exponentially — prospective students, parents, and donors now form impressions through TikTok and Reddit threads long before they read an official press release.

Regulatory and reputational considerations are paramount. FERPA restricts what can be disclosed about students, Clery Act requirements mandate timely crime reporting, and Title IX communications require legal precision. Accreditation bodies scrutinize institutional integrity, and state legislatures increasingly tie funding to public perception metrics. The communications team must balance transparency with legal constraints, institutional pride with honest acknowledgment of challenges, and proactive storytelling with reactive crisis management — all while operating on budgets that rarely keep pace with the expanding digital landscape.

## Value Driver Mapping

| Priority | Value Driver | Relevance | Why |
|----------|-------------|-----------|-----|
| 1 | Scale Impact Without Overhead | High | University PR teams manage exponentially more channels (social, web, email, media, internal, government affairs) with flat or declining budgets — AI-powered content scaling is transformative |
| 2 | Replace or Radically Augment Headcount | Medium-High | Routine content production (event announcements, faculty spotlights, research summaries) consumes 60%+ of team capacity that could be redirected to strategic communications |
| 3 | Consolidate Tech Stack with AI | Medium | Most university PR teams cobble together Cision/Meltwater, Hootsuite/Sprout Social, email platforms, CMS systems, and spreadsheets — consolidation reduces cost and fragmentation |

## Prioritized Use Cases

---

### Use Case 1: Media Relations & Press Coverage Tracking

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
University media relations teams manually track hundreds of journalist relationships, pitch stories via email with no systematic follow-up, and compile press clipping reports using expensive services like Cision or Meltwater that cost $30K-$80K annually. When a crisis hits, there's no centralized view of which reporters are covering the story, what angle they're taking, or who from the institution has spoken to them. The VP of Communications asks "how many earned media hits did we get this quarter?" and the answer takes a week of manual compilation. Meanwhile, research breakthroughs that could generate national coverage go unpitched because the team is buried in reactive work.

#### The Solution
monday.com Work Management as the central media relations hub: a **Media Contacts Board** (journalist name, outlet, beat, relationship owner, last contact date, sentiment rating), a **Pitch Tracker Board** (story angle, target journalists, pitch status, follow-up dates, coverage secured), a **Press Coverage Board** (article URL, outlet, reach/impressions, sentiment, topic tags, faculty quoted), and a **Media Inquiry Board** for inbound requests with SLA tracking. Dashboards aggregate earned media value, coverage by college/department, and journalist engagement trends. AI Sidekick summarizes coverage patterns and suggests pitch angles based on trending topics.

#### The Outcome
40% reduction in time spent compiling media reports. 25% increase in proactive story pitches. Elimination of $50K+ annual media monitoring tool costs. Real-time crisis media tracking during breaking events. Clear ROI reporting to university leadership on communications team impact.

#### Discovery Questions
1. "When your president asks for a media coverage report for the Board of Trustees meeting, how long does it take to compile and how confident are you in the numbers?"
2. "How do you currently track which journalists have relationships with which faculty members, and has a reporter ever been pitched the same story by two different people in your office?"
3. "During your last campus crisis — whether it was a safety incident, a controversial speaker, or a Title IX issue — how quickly could you see which media outlets were covering it and what angle they were taking?"
4. "What percentage of your team's time goes to reactive media inquiries versus proactive storytelling about research, student success, or institutional achievements?"
5. "How do you currently measure the ROI of your media relations efforts for budget justification to the provost or VP of University Relations?"

#### Industry Context
Higher ed media relations operates differently from corporate PR. Faculty are independent voices who may speak to media without coordination. Student newspapers operate with First Amendment protections. Research embargoes (especially in STEM and medical fields) require precise timing coordination with journals like Nature or JAMA. Land-grant universities have public records obligations. Athletics communications often operates as a separate entity. The "town-gown" relationship means local media coverage carries outsized weight.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Media Relations Management system for a university communications office. Create four connected boards:
>
> 1. **Media Contacts**: columns for Contact Name (text), Outlet (text), Beat/Coverage Area (dropdown: Higher Ed, Local News, Science/Research, Politics, Sports, Business, Technology, National), Contact Type (dropdown: Reporter, Editor, Producer, Freelancer, Blogger/Influencer), Email (email), Phone (phone), Relationship Owner (people), Relationship Strength (rating 1-5), Last Contact Date (date), Notes (long text), Region (dropdown: Local, State, Regional, National, International).
>
> 2. **Story Pitches**: columns for Story Headline (text), Story Type (dropdown: Research Breakthrough, Student Success, Faculty Achievement, Institutional Milestone, Event Preview, Opinion/Thought Leadership, Data/Report Release), Target Journalists (connect to Media Contacts), Pitch Status (status: Drafting, Ready to Send, Pitched, Follow-up Needed, Interested, Published, Passed), Pitch Date (date), Follow-up Date (date), College/Department (dropdown: Arts & Sciences, Engineering, Business, Medicine, Education, Law, Nursing, Athletics, Administration), Embargo Date (date), Supporting Assets (files), Assigned To (people), Priority (status: Urgent, High, Normal, Low).
>
> 3. **Press Coverage**: columns for Headline (text), Outlet (text), Reporter (connect to Media Contacts), URL (link), Publication Date (date), Reach/Impressions (numbers), Sentiment (status: Positive, Neutral, Negative, Mixed), Coverage Type (dropdown: Feature, Brief Mention, Quote, Op-Ed, Broadcast Segment, Podcast, Social), Related Pitch (connect to Story Pitches), College/Department (dropdown), Faculty Quoted (text), Topic Tags (tags).
>
> 4. **Media Inquiries**: columns for Reporter (connect to Media Contacts), Inquiry Topic (text), Date Received (date), Deadline (date), Assigned To (people), Status (status: New, Researching, Response Drafted, Approved, Sent, Declined), Response Time (formula), Sensitivity Level (status: Routine, Elevated, Crisis, Legal Review Required).
>
> Add automations: when Pitch Status changes to 'Pitched,' set Follow-up Date to 5 business days later. When a Media Inquiry is created, notify the assigned person. When Sensitivity Level is 'Crisis' or 'Legal Review Required,' notify the VP of Communications. Create a Dashboard with: total coverage this month vs. last, coverage by sentiment, top outlets, pitches sent vs. coverage secured ratio, average media inquiry response time, and coverage by college/department."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** MediaWatch
**Agent Purpose:** Automatically track, categorize, and analyze media coverage of the university across all channels and alert the team to emerging stories.

**Triggers:**
- Daily scheduled scan at 7:00 AM, 12:00 PM, and 5:00 PM
- When a Media Inquiry item is created with Sensitivity Level "Crisis"
- When a new item is added to Press Coverage board manually
- When Pitch Status changes to "Published"
- Weekly on Monday morning for trend analysis

**Actions:**
- Create new Press Coverage items from monitored RSS feeds and Google Alerts with auto-populated sentiment, outlet, and reach fields
- Generate daily media briefing summary document for the CCO with top stories, sentiment trends, and recommended responses
- Flag negative or crisis-level coverage and create corresponding Media Inquiry items with pre-populated context
- Auto-link new coverage to existing Story Pitches based on topic matching
- Produce weekly earned media value report with quarter-over-quarter comparisons
- Alert the crisis communications lead when coverage volume on a single topic exceeds normal thresholds by 3x

**Data Required:**
- RSS feeds from target media outlets, Google Alerts integration, social media monitoring feeds
- Historical coverage data for trend baselines
- University spokesperson directory and expertise areas
- Crisis communications protocols and escalation trees

**Autonomy Level:** Human-in-the-Loop
Automated for coverage tracking, categorization, and routine reporting. Human approval required for crisis-level alerts, sentiment classification of sensitive stories, and any external response recommendations.

**Example Interaction:**
> At 7:15 AM on a Tuesday, MediaWatch completes its morning scan and creates three new items on the Press Coverage board: a positive feature in the Chronicle of Higher Education about the university's new AI research center, a neutral mention in the local newspaper about a campus construction project, and a developing story on Inside Higher Ed about a Title IX complaint. The agent auto-tags sentiment, links the AI research story to the pitch that was sent last week, and calculates estimated reach.
>
> For the Title IX story, MediaWatch flags it as "Elevated" sensitivity, creates a Media Inquiry item assigned to the crisis communications lead, and sends a Slack notification to the CCO with a summary: "Developing story on IHE re: Title IX complaint in Athletics. Moderate reach (~85K monthly visitors). No university comment included yet. Recommend coordinating with General Counsel before any response. Related coverage: none found in last 30 days." The CCO reviews and escalates to the VP of University Relations.
>
> By Friday, MediaWatch generates a weekly summary showing 12 new press mentions, 73% positive sentiment (up from 68% last week), the AI research center story generating 340K impressions — the highest-performing earned media hit of the month. It recommends pitching a follow-up angle on student involvement in the research.

---

### Use Case 2: Crisis Communications Command Center

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
When a campus crisis strikes — an active shooter situation, a hazing death, a data breach, a Title IX scandal, or a controversial speaker protest — the communications team scrambles. There's no single source of truth for who's saying what, which statements have been approved, what's been posted to which channels, or who from leadership has been briefed. The CCO is texting the president's office while the social media manager is monitoring Twitter while the media relations director is fielding calls from CNN — all using different tools and none with a shared view. Post-crisis reviews consistently reveal gaps: a statement went out without legal review, a social media post contradicted the official position, or a key stakeholder wasn't notified. In the worst cases, these failures become the story.

#### The Solution
A monday.com **Crisis Command Board** activated on-demand with pre-built templates: Status columns tracking each crisis phase (Monitoring, Active Response, De-escalation, Resolution, Post-Mortem), a **Statements & Approvals Board** with legal/leadership sign-off workflows, a **Channel Distribution Board** tracking what's been posted where (website, social, email, media, internal), a **Stakeholder Notification Board** (Board of Trustees, legislators, donors, parents, faculty senate, student government), and a real-time **Situation Update Board** for the incident command team. Automations enforce approval chains and track SLAs. Dashboards provide the CCO with a single-pane crisis view.

#### The Outcome
60% faster initial response time during crises. Zero unapproved statements reaching external audiences. Complete audit trail for post-crisis review and legal protection. Coordinated multi-channel messaging with no contradictions. Reduced reputational damage through faster, more consistent crisis response.

#### Discovery Questions
1. "Walk me through what happens in the first 60 minutes when a serious campus incident occurs — who gets called, how are statements drafted and approved, and where does the coordination happen?"
2. "Have you ever had a situation where a social media post or statement went out before it was fully approved, or where two different university representatives gave contradicting information?"
3. "How do you currently track which stakeholders — Board members, legislators, major donors, parents — have been notified during a crisis, and in what order?"
4. "After your last crisis, what did the post-mortem reveal about gaps in your communications response process?"
5. "How many different tools and channels does your team touch during an active crisis, and is there a single dashboard where the president or provost can see the current status?"

#### Industry Context
Higher ed crises are uniquely complex. Clery Act requires timely warnings for campus safety threats. FERPA restricts student information disclosure even during crises. Title IX investigations have specific communication requirements. Campus police, student affairs, general counsel, and government relations all have roles. Media descend on campus physically. Student social media spreads information (and misinformation) faster than official channels. Board of Trustees members may receive calls from donors or legislators before they've been briefed. Congressional inquiries may follow high-profile incidents.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Crisis Communications Command Center for a university. Create five connected boards:
>
> 1. **Crisis Incidents**: columns for Incident Name (text), Crisis Type (dropdown: Campus Safety, Student Death/Injury, Title IX/Sexual Assault, Data Breach/Cyber, Faculty Misconduct, Athletics Scandal, Protest/Free Speech, Natural Disaster, Financial/Audit, Public Health), Severity Level (status: Level 1 - Monitor, Level 2 - Elevated, Level 3 - Major, Level 4 - Critical), Phase (status: Detection, Assessment, Active Response, De-escalation, Recovery, Post-Mortem), Incident Commander (people), Start Date/Time (date), Resolution Date (date), Summary (long text), Legal Hold (checkbox).
>
> 2. **Statements & Messaging**: columns for Statement Title (text), Related Incident (connect to Crisis Incidents), Audience (dropdown: Media, Students, Parents, Faculty/Staff, Board of Trustees, Donors/Alumni, Government/Legislators, General Public), Channel (dropdown: Website, Email, Social Media, Press Release, Media Statement, Internal Memo, Emergency Alert), Draft (long text), Status (status: Drafting, Legal Review, Leadership Review, Approved, Published, Revised), Author (people), Legal Approved By (people), Leadership Approved By (people), Published Date/Time (date), URL (link).
>
> 3. **Stakeholder Notifications**: columns for Stakeholder Group (dropdown: President's Cabinet, Board of Trustees, State Legislators, Major Donors, Faculty Senate, Student Government, Parents via Email, Media Contacts, Accreditors, Partner Institutions), Contact Person (text), Notification Method (dropdown: Phone Call, Email, Text, In-Person Briefing), Status (status: Pending, In Progress, Completed, Unable to Reach, Follow-up Needed), Assigned To (people), Notified At (date), Notes (long text), Related Incident (connect to Crisis Incidents).
>
> 4. **Media Activity**: columns for Outlet (text), Reporter (text), Inquiry/Coverage (dropdown: Inbound Inquiry, On-Campus Crew, Published Story, Social Post, Broadcast Mention), Topic/Angle (text), Deadline (date), Response Status (status: No Response, Statement Provided, No Comment, Interview Scheduled, Interview Completed), Assigned To (people), Sentiment (status: Positive, Neutral, Negative, Unknown), Related Incident (connect to Crisis Incidents).
>
> 5. **Situation Updates (Log)**: columns for Timestamp (date), Update (long text), Source (dropdown: Campus Police, Student Affairs, General Counsel, Government Relations, Social Media Monitor, Media Relations, President's Office, External), Reported By (people), Related Incident (connect to Crisis Incidents), Action Required (checkbox), Action Assigned To (people).
>
> Add automations: when Crisis Severity is Level 3 or 4, automatically notify the entire crisis team. When a Statement Status moves to 'Legal Review,' notify the General Counsel contact. When all Stakeholder Notifications for an incident are 'Completed,' update the Incident phase. When a new Media Activity item is 'Inbound Inquiry' with deadline within 2 hours, mark as urgent. Create a Dashboard showing: active incidents by severity, statement approval pipeline, stakeholder notification completion percentage, media inquiry response times, and a timeline of situation updates."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CrisisCoordinator
**Agent Purpose:** Orchestrate crisis communications workflows, ensure no stakeholder notification is missed, and maintain a real-time single source of truth during active incidents.

**Triggers:**
- When a new Crisis Incident is created at Severity Level 2+
- When a Situation Update is logged with "Action Required" checked
- When a media inquiry deadline is within 1 hour and response status is still "No Response"
- Every 30 minutes during an active Level 3-4 crisis
- When all stakeholder notifications for a group are completed

**Actions:**
- Auto-populate Stakeholder Notification board with the appropriate contact list based on crisis type and severity level
- Generate draft holding statements based on crisis type templates and current situation updates
- Send escalation alerts when media deadlines approach without responses
- Compile and distribute situation update summaries to the incident command team every 30 minutes during active crises
- Track and flag any inconsistencies between published statements across different channels
- Generate post-crisis communications audit report with timeline, response metrics, and lessons learned

**Data Required:**
- Crisis communications playbook templates by incident type
- Stakeholder contact directories with preferred notification methods
- University statement templates and boilerplate language
- Legal communication guidelines and FERPA/Clery requirements
- Historical crisis response data for benchmarking

**Autonomy Level:** Escalation-Based
Agent handles logistics (notifications, scheduling, tracking, reminders) autonomously. All external-facing content requires human approval. Agent drafts but never publishes statements. Escalates immediately when detecting potential legal, FERPA, or Clery implications.

**Example Interaction:**
> At 2:47 PM, a campus safety incident is logged as a Level 3 crisis — a suspicious package found in the main library. CrisisCoordinator immediately activates the crisis template, creating 23 stakeholder notification items pre-assigned based on the "Campus Safety" protocol. It drafts an initial holding statement: "The university is aware of a security situation at [Library]. Campus police are on scene and working with local law enforcement. The building has been evacuated as a precaution. Updates will be provided as information becomes available."
>
> The statement is routed to General Counsel and the VP of Communications for approval. Simultaneously, the agent creates Media Activity items for the three local TV stations that typically cover campus incidents and flags them as likely to send crews. It sends a reminder to the media relations director: "Based on past incidents, expect calls from WXTV, KRNL, and the Daily Tribune within 15 minutes."
>
> At 3:15 PM, the situation is resolved — package was a forgotten backpack. CrisisCoordinator drafts an all-clear statement, routes it for approval, and once published, begins closing out stakeholder notifications. By 4:00 PM, it generates a response report: "Initial detection to first public statement: 8 minutes. All Board members notified within 22 minutes. Three media inquiries handled within deadline. No contradictory messaging detected across channels."

---

### Use Case 3: Research Communications & Faculty Expertise Pipeline

**Relevance:** High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Major research universities produce hundreds of published papers, grant awards, and discoveries monthly, but the communications team can only write stories about a fraction. Faculty expertise goes untapped because there's no searchable database connecting reporters' questions to the right professor. When a national event happens — a pandemic, an election, a natural disaster — the media team scrambles to identify which faculty can speak authoritatively. Meanwhile, the provost is pushing for higher national research rankings, which depend partly on public visibility of research output. The gap between research activity and public storytelling represents millions in lost reputational value.

#### The Solution
monday.com boards to manage the **Faculty Expertise Directory** (name, department, research areas, media training status, past media appearances, availability), a **Research Story Pipeline** (publication alerts, grant awards, discovery milestones tracked from initial tip to published story), and a **Rapid Response Roster** for connecting journalists with faculty experts on trending topics. AI Sidekick matches incoming media requests with faculty expertise profiles. Integration with the university's research administration system surfaces new grants and publications automatically.

#### The Outcome
3x increase in research stories produced annually. 50% faster journalist-to-expert matching for breaking news. Measurable increase in university's share of voice in research media coverage. Faculty satisfaction with communications support increases. Stronger positioning for national rankings and donor engagement.

#### Discovery Questions
1. "How many peer-reviewed publications does your university produce annually, and what percentage of those get any kind of public-facing story or press release?"
2. "When a major news event happens and journalists call asking for an expert on climate science, election law, or infectious disease, how quickly can you identify and connect the right faculty member?"
3. "Do you have a faculty expertise database, and if so, when was it last updated and how confident are you that it reflects current research interests?"
4. "How do you currently learn about significant research milestones — new grants, publications in high-impact journals, patent filings — and is that process proactive or do you find out after the fact?"
5. "Has your institution ever missed a major media opportunity because you couldn't identify or reach the right faculty expert quickly enough?"

#### Industry Context
Research universities are measured by publications, citations, grants, and public impact. The NSF Higher Education Research and Development (HERD) survey ranks institutions by research expenditures. Media visibility of research directly influences prospective graduate student recruitment, donor giving to research funds, and federal grant competitiveness. Faculty are independent operators — they may publish groundbreaking work and never tell the communications office. Some faculty are media-trained and eager; others are brilliant researchers who need coaching. Embargo management for journals like Nature, Science, Cell, and NEJM requires precise timing coordination.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Research Communications Pipeline for a university PR office. Create three connected boards:
>
> 1. **Faculty Expertise Directory**: columns for Faculty Name (text), Title/Rank (dropdown: Assistant Professor, Associate Professor, Full Professor, Distinguished Professor, Department Chair, Dean, Endowed Chair), Department (dropdown with 20+ departments), College (dropdown), Research Areas (tags), Media Training (status: Trained, Scheduled, Needs Training, Declined), Media Comfort Level (rating 1-5), Past Media Appearances (numbers), Languages Spoken (tags), Headshot on File (checkbox), Bio Updated (date), Email (email), Phone (phone), Availability Notes (long text), Featured Expert Areas (text — what reporters should call them about).
>
> 2. **Research Story Pipeline**: columns for Story Title (text), Faculty Lead (connect to Faculty Expertise Directory), Research Type (dropdown: Journal Publication, Grant Award, Patent Filed, Discovery/Breakthrough, Conference Presentation, Book Published, Industry Partnership, Student Research), Source Journal/Funder (text), Embargo Date (date), Story Status (status: Tip Received, Evaluating, Assigned to Writer, Drafting, Faculty Review, Final Edit, Published, Killed), Writer (people), Target Publish Date (date), Story Angle (long text), Newsworthiness Score (rating 1-5), Distribution Channels (dropdown: Press Release, Website Feature, Social Only, Media Pitch, Video, Podcast, All Channels), College (dropdown), Impact Metrics (long text).
>
> 3. **Rapid Response Roster**: columns for Topic (text), Triggered By (text — what event/news prompted this), Date Needed (date), Matching Faculty (connect to Faculty Expertise Directory), Outreach Status (status: Identifying Experts, Faculty Contacted, Available, Scheduled, Completed, No Match Found), Media Outlet Requesting (text), Deadline (date), Talking Points (long text), Outcome (dropdown: Interview Completed, Quoted in Article, Op-Ed Published, Declined, Missed Deadline).
>
> Add automations: when a Research Story Pipeline item is created, auto-assign a Newsworthiness Score notification to the editorial lead. When Embargo Date is tomorrow, notify the writer and social media team. When a Rapid Response item deadline is within 4 hours and status is still 'Identifying Experts,' escalate to the media relations director. Create a Dashboard with: stories published this month by college, pipeline by status, faculty engagement stats (most quoted, most available), rapid response success rate, and stories by research type."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** ResearchSpotlight
**Agent Purpose:** Automatically surface newsworthy research, match faculty expertise to media opportunities, and draft initial story angles to accelerate the research-to-publicity pipeline.

**Triggers:**
- Daily scan of university research administration RSS feed for new grants >$500K and publications in high-impact journals
- When a Rapid Response Roster item is created
- When a trending news topic matches a faculty research area tag
- Weekly on Wednesday for upcoming embargo dates in the next 7 days
- When a Faculty Expertise Directory profile hasn't been updated in 12+ months

**Actions:**
- Create new Research Story Pipeline items from detected publications/grants with pre-populated story angles and newsworthiness scores
- Match incoming Rapid Response requests to faculty expertise profiles and rank by media readiness + research relevance
- Draft 2-3 story angle options for high-scoring research items based on the publication abstract and current news trends
- Send faculty profile update requests annually with pre-filled forms
- Generate monthly "Research Communications Impact Report" showing stories published, media hits generated, and faculty engagement metrics

**Data Required:**
- University research administration system feed (grants, publications, patents)
- Journal impact factor database for newsworthiness scoring
- Faculty expertise profiles and media training records
- Trending news topics from media monitoring
- Historical story performance data (which angles generated most coverage)

**Autonomy Level:** Human-in-the-Loop
Agent surfaces, scores, and drafts but never publishes or contacts faculty/media directly. Editorial team makes final decisions on which stories to pursue and which experts to recommend. Agent can send automated profile update reminders to faculty.

**Example Interaction:**
> ResearchSpotlight detects a new $2.3M NIH grant awarded to Dr. Sarah Chen in the School of Public Health for a study on air quality impacts on childhood asthma in urban communities. The agent creates a Research Story Pipeline item with a Newsworthiness Score of 4/5, noting: "Strong local angle (study sites include three neighborhoods within 10 miles of campus), timely (EPA regulatory changes in the news), and photogenic (involves community health workers and monitoring equipment)." It suggests three angles: (1) local health impact story for regional media, (2) environmental justice angle for national outlets, (3) student researcher involvement for alumni magazine.
>
> The agent checks Dr. Chen's profile: media-trained, comfort level 4/5, three previous media appearances, and fluent in Mandarin (useful for international outlets). It flags that the Chronicle of Higher Education ran a story about NIH grant trends last week and suggests pitching this as a follow-up example. The editorial lead reviews, assigns a writer, and the story is published two weeks later, generating coverage in the local newspaper, a regional NPR affiliate, and a health policy blog — all tracked automatically in the Press Coverage board.

---

### Use Case 4: Social Media Content Calendar & Engagement Management

**Relevance:** High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
University social media teams manage 10-20+ accounts across platforms (Instagram, TikTok, LinkedIn, X/Twitter, Facebook, YouTube, Threads) for the central university brand plus individual colleges, athletics, admissions, and alumni relations. Content planning happens in spreadsheets, approval workflows live in email threads, and there's no unified view of what's being posted when across the institution. During key periods — admissions yield season, homecoming, commencement, giving day — the volume is overwhelming. Student workers (who often run the most engaging accounts) turn over every 1-2 years, losing institutional knowledge. Meanwhile, the Dean of Engineering just posted something from the college account that contradicts the university's messaging on AI ethics, and nobody caught it until a student screenshot went viral.

#### The Solution
monday.com as the university's **Social Media Command Center**: a **Content Calendar Board** with multi-platform scheduling, approval workflows, and asset management; a **Campaign Board** for coordinated pushes (admissions, giving day, homecoming); an **Engagement Tracking Board** for monitoring performance metrics and trending conversations; and a **Brand Governance Board** for ensuring decentralized accounts stay on-message. Views include a Calendar view for editorial planning, a Kanban view for content production workflow, and dashboards for cross-platform analytics.

#### The Outcome
30% reduction in content production cycle time. Zero off-brand posts from decentralized accounts. 20% increase in engagement rates through data-driven content optimization. Seamless onboarding for student social media workers. Unified reporting across all institutional social accounts.

#### Discovery Questions
1. "How many social media accounts does your institution manage centrally, and how many are run by individual colleges, departments, or units — and do you have visibility into what they're posting?"
2. "What does your content approval process look like today, and have you ever had a post go live that shouldn't have — wrong timing, off-brand messaging, or an accidental publish?"
3. "During your biggest social media moments — yield season for admissions, giving day, commencement — how do you coordinate content across platforms and accounts to avoid overlap or conflicting messages?"
4. "How do you handle student worker turnover on your social team, and how much institutional knowledge walks out the door each May at graduation?"
5. "Can you currently see cross-platform performance data in one place, or do you pull reports from each platform's native analytics separately?"

#### Industry Context
Higher ed social media is uniquely complex. Prospective students live on TikTok and Instagram; parents are on Facebook; donors and Board members are on LinkedIn; journalists monitor X/Twitter. Each audience requires different tone, format, and content. Athletics accounts may have more followers than the main university account. Student-run accounts are often the most authentic and engaging but hardest to govern. UGC (user-generated content) from students is gold but requires FERPA consideration. Algorithmic changes on any platform can crater reach overnight, making diversification essential. Giving Day campaigns require real-time social coordination across dozens of accounts.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a University Social Media Command Center. Create four connected boards:
>
> 1. **Content Calendar**: columns for Post Title (text), Platform (dropdown: Instagram, TikTok, LinkedIn, X/Twitter, Facebook, YouTube, Threads, Multiple), Account (dropdown: Main University, Admissions, Alumni, Athletics, College of Engineering, College of Business, College of Arts & Sciences, Student Life, Research, President's Office), Content Type (dropdown: Photo, Video/Reel, Carousel, Story, Live, Thread, Poll, Link Share), Caption/Copy (long text), Visual Assets (files), Scheduled Date/Time (date), Status (status: Ideation, Drafting, Design Needed, In Review, Approved, Scheduled, Published, Rejected), Creator (people), Approver (people), Campaign (connect to Campaigns board), Hashtags (text), Target Audience (dropdown: Prospective Students, Current Students, Parents, Alumni, Donors, Faculty/Staff, Community, Media).
>
> 2. **Campaigns**: columns for Campaign Name (text), Campaign Type (dropdown: Admissions Yield, Giving Day, Homecoming, Commencement, Research Showcase, Enrollment, Brand Awareness, Recruitment, Event Promotion), Start Date (date), End Date (date), Lead (people), Platforms (dropdown: All, Instagram+TikTok, LinkedIn+X, Facebook+Instagram, Custom), Key Messages (long text), Status (status: Planning, Content Creation, Active, Completed, Analyzing), Budget (numbers), Goal Metric (text), Actual Result (text).
>
> 3. **Engagement Tracker**: columns for Post (connect to Content Calendar), Platform (mirror), Impressions (numbers), Reach (numbers), Engagements (numbers), Engagement Rate (formula), Clicks (numbers), Shares (numbers), Comments (numbers), Saves (numbers), Video Views (numbers), Best Performing (checkbox), Notes (long text), Date Published (date).
>
> 4. **Brand Governance**: columns for Account Name (text), Platform (dropdown), Account Owner (people), Last Audit Date (date), Compliance Status (status: Compliant, Minor Issues, Major Issues, Not Audited), Bio Matches Template (checkbox), Logo/Avatar Current (checkbox), Link in Bio Updated (checkbox), Content Tone Aligned (status: On Brand, Needs Guidance, Off Brand), Notes (long text), Next Audit Date (date).
>
> Add automations: when Content Status moves to 'In Review,' notify the Approver. When a post is 'Rejected,' notify the Creator with the Approver's notes. When Scheduled Date is today and Status is still 'In Review,' send urgent alert. When Brand Governance Next Audit Date is today, create an audit task. Create a Dashboard with: content calendar (calendar view), posts by platform and status, top performing posts this month, campaign performance, engagement rate trends, and brand compliance overview across all accounts."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** SocialPulse
**Agent Purpose:** Optimize university social media by analyzing performance patterns, suggesting content ideas, and flagging brand governance issues across decentralized accounts.

**Triggers:**
- Daily at 9:00 AM to pull previous day's engagement metrics
- When a new Campaign is created (to suggest content ideas)
- When Brand Governance compliance changes to "Off Brand" or "Major Issues"
- Weekly on Friday for performance summary
- When engagement on any post exceeds 3x the account average (viral detection)

**Actions:**
- Pull engagement data from platform APIs and populate Engagement Tracker items
- Generate weekly "Top 5 Performers" report with analysis of why they worked (format, timing, topic, caption style)
- Suggest 10 content ideas for the upcoming week based on trending topics, university calendar events, and historical high performers
- Flag decentralized account posts that deviate from brand guidelines based on tone, visual, and messaging analysis
- Alert team when a post is going viral with recommended amplification actions
- Generate monthly cross-platform analytics report comparing this month vs. previous month and year-over-year

**Data Required:**
- Social media platform API access (Instagram Graph, TikTok, LinkedIn, X, Facebook, YouTube)
- University academic calendar and events feed
- Brand guidelines document (visual and messaging)
- Historical post performance data
- Trending topics and hashtag data

**Autonomy Level:** Human-in-the-Loop
Agent pulls data, analyzes, and recommends autonomously. Never posts or schedules content directly. Brand governance flags are recommendations that humans must review and act on. Content suggestions are ideas, not mandates.

**Example Interaction:**
> On Friday morning, SocialPulse generates the weekly social performance report. It identifies that a student-created TikTok about "things professors say" posted from the main university account received 2.1M views — 47x the average. The agent creates an alert: "Viral content detected. Recommend: (1) reshare to Instagram Reels by EOD, (2) tag the student creator for UGC credit, (3) pitch a series concept — 'Things They Say at [University]' — for the content calendar."
>
> It also flags that the College of Business account posted a recruitment ad using the old logo and a tagline that was retired 18 months ago. The Brand Governance item is updated to "Major Issues" with a note: "Old visual identity assets detected. Recommend reaching out to the college's communications coordinator for updated brand toolkit." The social media director reviews and sends a friendly email to the business school's marketing team with the current assets.

---

### Use Case 5: Internal Communications & Campus Announcements

**Relevance:** Medium-High
**Value Driver:** Replace or Radically Augment Headcount

#### The Pain
Internal communications in higher ed is notoriously fragmented. The provost's office sends emails, HR sends emails, student affairs sends emails, the president sends emails — and nobody coordinates timing, tone, or frequency. Faculty complain about "email fatigue" while simultaneously claiming they never heard about a major policy change. Staff in facilities and dining services may not even have regular email access. During major transitions — a new strategic plan, a tuition increase announcement, a leadership change — the lack of coordinated internal communications erodes trust and fuels rumor mills. Town halls are poorly attended, and the campus intranet that was rebuilt three years ago is already outdated and rarely visited.

#### The Solution
monday.com **Internal Communications Hub**: an **Announcements Board** tracking every institutional communication with audience segmentation, timing coordination, and channel selection; a **Town Hall & Events Board** managing preparation, speaker coordination, Q&A collection, and follow-up; an **Employee Newsletter Board** managing content curation, production workflow, and distribution; and a **Change Communications Board** for major initiatives requiring multi-phase messaging plans. Calendar views prevent email pile-ups on the same day. Dashboards show open rates, reach, and engagement by audience segment.

#### The Outcome
40% reduction in "I didn't know about that" complaints from faculty and staff. Coordinated announcement scheduling eliminates email pile-ups. 25% increase in town hall participation through better promotion and follow-up. Clear measurement of internal communications effectiveness for the first time.

#### Discovery Questions
1. "How many different offices or individuals can send mass communications to faculty and staff, and is there any central coordination of timing or messaging?"
2. "When you announced your last major policy change — new remote work policy, tuition increase, organizational restructuring — how did you learn it was being misunderstood or hadn't reached key audiences?"
3. "What's your open rate on internal emails, and do you have any way to reach staff who don't sit at desks — facilities, dining services, campus safety?"
4. "How do you currently prepare for and follow up on town halls or all-hands meetings, and what happens to the questions that don't get answered live?"
5. "If the president wanted to know 'did our message about the strategic plan actually land with faculty,' could you answer that with data?"

#### Industry Context
Universities have uniquely complex internal audiences: tenured faculty (who may ignore administrative communications on principle), adjunct faculty (who feel disconnected), exempt and non-exempt staff (different communication needs), student employees, and graduate teaching/research assistants who are simultaneously students and employees. Shared governance means faculty senate must be consulted on certain topics before announcements. Union contracts may dictate how certain communications are handled. Campus culture often values informal communication networks (department hallway conversations, faculty listservs) over official channels.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build an Internal Communications Hub for a university. Create four connected boards:
>
> 1. **Announcements Tracker**: columns for Subject (text), Sending Office (dropdown: President, Provost, HR, Student Affairs, Finance & Admin, IT, Research, DEI, Facilities, Communications), Audience (dropdown: All Employees, Faculty Only, Staff Only, Leadership/Chairs, Specific College, Student Employees, Union Members), Channel (dropdown: Email, Intranet, Digital Signage, Department Meetings, Newsletter, All-Hands, Physical Posting, SMS/Text), Scheduled Send Date (date), Status (status: Drafting, In Review, Approved, Scheduled, Sent, Cancelled), Priority (status: Routine, Important, Urgent, Emergency), Content (long text), Approved By (people), Open Rate (numbers), Click Rate (numbers), Feedback Received (long text).
>
> 2. **Town Halls & Forums**: columns for Event Name (text), Type (dropdown: Presidential Town Hall, Provost Forum, HR Benefits Open Enrollment, Budget Briefing, Strategic Plan Update, Department All-Hands, Emergency Briefing), Date (date), Location (text), Virtual Link (link), Presenters (people), Pre-Submitted Questions (long text), Attendance Count (numbers), Recording Link (link), Follow-Up Status (status: Pending, Summary Drafted, Summary Sent, All Questions Answered), Key Takeaways (long text), Action Items (long text).
>
> 3. **Newsletter Pipeline**: columns for Issue Date (date), Theme (text), Articles (subitems — each with: Headline, Author, Status, Word Count, Due Date), Design Status (status: Not Started, In Progress, Final Review, Ready), Distribution Status (status: Pending, Sent, Analyzing), Open Rate (numbers), Top Article (text), Editor (people).
>
> 4. **Change Communications**: columns for Initiative Name (text), Change Type (dropdown: Policy Change, Org Restructuring, System Migration, Benefits Change, Strategic Plan, Leadership Transition, Budget/Financial, DEI Initiative), Phase (status: Pre-Announcement, Soft Launch, Full Announcement, Reinforcement, Steady State), Stakeholder Groups (tags), Key Messages (long text), FAQ Document (files), Spokesperson (people), Timeline Start (date), Timeline End (date), Resistance Level (status: Low, Medium, High, Critical), Feedback Channel (text).
>
> Add automations: when two Announcements are scheduled for the same day to the same audience, alert the communications coordinator. When a Town Hall Follow-Up Status is 'Pending' for more than 3 business days, send a reminder. When Change Communications Resistance Level is 'High' or 'Critical,' notify the CCO. Create a Dashboard with: announcements calendar view, open rates by sending office, town hall attendance trends, change initiative status overview, and newsletter engagement over time."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CampusVoice
**Agent Purpose:** Coordinate internal university communications to prevent message fatigue, optimize timing, and ensure no audience segment is overlooked.

**Triggers:**
- When a new Announcement is created and scheduled within 24 hours of another announcement to the same audience
- When a Town Hall is 3 days away (to begin prep workflow)
- When Change Communications Resistance Level changes to "High" or "Critical"
- Weekly on Monday to generate the week's internal communications schedule
- Monthly on the 1st for communications effectiveness report

**Actions:**
- Flag scheduling conflicts and suggest alternative send times based on historical open rate data by day of week and time
- Generate town hall preparation checklist (pre-submitted questions compiled, talking points drafted, tech check scheduled, recording setup confirmed)
- Draft FAQ documents for change communications initiatives based on the initiative description and common question patterns
- Compile weekly "communications calendar" showing all planned messages across all offices
- Produce monthly internal communications scorecard with open rates, reach, and engagement trends by audience segment
- Recommend audience segmentation adjustments when open rates for a segment drop below benchmarks

**Data Required:**
- Email platform analytics (open rates, click rates by audience segment)
- University HR system for employee categorization
- Academic calendar for scheduling optimization
- Historical communications performance data
- Change management best practices knowledge base

**Autonomy Level:** Human-in-the-Loop
Agent coordinates, flags, and drafts but all communications go through human approval. Scheduling conflict alerts are informational — humans decide whether to reschedule. FAQ drafts are starting points for human refinement.

**Example Interaction:**
> CampusVoice detects that HR has scheduled a benefits enrollment reminder for Tuesday at 10 AM, and the Provost's office has scheduled a strategic plan update email for Tuesday at 10:30 AM — both targeting "All Employees." The agent creates a flag: "Scheduling conflict detected. Two all-employee emails within 30 minutes on Tuesday. Historical data shows Tuesday 10 AM has a 34% open rate, but sending two messages within an hour drops the second message's open rate to 18%. Recommendation: Move the benefits reminder to Wednesday 10 AM (historical open rate: 37% for HR messages) or combine into a single digest."
>
> The communications coordinator reviews, contacts both offices, and the benefits email is moved to Wednesday. CampusVoice automatically updates the weekly communications calendar and sends the revised schedule to all office communications liaisons.

---

### Use Case 6: Alumni & Donor Communications Pipeline

**Relevance:** Medium-High
**Value Driver:** Scale Impact Without Overhead

#### The Pain
University advancement and communications teams struggle to coordinate donor-facing storytelling. The communications office writes stories about institutional achievements while advancement wants donor-specific impact narratives. Gift officers need talking points for meetings but the latest "impact report" is six months old. During capital campaigns ($500M-$2B targets), the volume of donor communications — cultivation emails, event invitations, stewardship reports, naming opportunity updates — overwhelms the team. There's no systematic way to ensure that a donor who gave $5M to the engineering building sees the story about the research breakthrough that happened in "their" building. The disconnect between storytelling and fundraising costs real dollars.

#### The Solution
monday.com connecting the communications and advancement workflows: a **Donor Communications Board** tracking all donor-facing content with segmentation by giving level, interest area, and relationship stage; a **Impact Stories Board** mapping institutional stories to donor interests and gift designations; a **Campaign Communications Board** for capital campaign messaging across phases (quiet phase, public phase, celebration); and an integration layer that connects story production to the donor CRM to ensure the right stories reach the right donors at the right time.

#### The Outcome
2x increase in donor-relevant content production. Personalized impact communications for major donors ($100K+) without additional headcount. 15% improvement in donor retention rates through better stewardship communications. Streamlined capital campaign communications across all phases.

#### Discovery Questions
1. "How closely do your communications and advancement teams coordinate today, and when a great institutional story is published, does it systematically reach the donors who would care most about it?"
2. "For your major donors — the $100K+ annual givers or $1M+ lifetime donors — how personalized are the impact communications they receive, and who produces that content?"
3. "During your last capital campaign or giving day, how did you coordinate messaging across the communications office, advancement, and individual gift officers?"
4. "Can you currently connect a donor's giving designation — say, a scholarship fund in the College of Education — to the stories being produced about scholarship recipients and Education faculty achievements?"
5. "How do you measure whether your donor communications actually influence giving behavior, and can you attribute any gift to a specific story or communication?"

#### Industry Context
Higher ed advancement operates on relationship cycles measured in years or decades. A major gift prospect may be cultivated for 5-10 years before making a transformational commitment. Stewardship — showing donors their impact — is critical to retention and upgrade potential. CASE (Council for Advancement and Support of Education) standards guide reporting. Named giving opportunities (buildings, professorships, scholarships) require ongoing recognition. Planned giving (bequests, charitable remainder trusts) requires sensitive, long-term communications. Annual giving solicitations compete with every other nonprofit in donors' mailboxes. University foundations may be legally separate entities with their own communications needs.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Donor Communications Pipeline connecting the university communications office with advancement. Create three connected boards:
>
> 1. **Donor Communications**: columns for Communication Title (text), Type (dropdown: Impact Report, Thank You, Event Invitation, Campaign Update, Newsletter, Stewardship Report, Naming Recognition, Annual Fund Appeal, Planned Giving, Holiday/Seasonal), Audience Segment (dropdown: Trustees, Major Donors $1M+, Leadership Donors $100K+, Mid-Level $10K+, Annual Fund, Young Alumni, Parents, Corporate Partners, Foundation Partners), Interest Area (dropdown: Unrestricted, Athletics, Scholarships, Research, College of Engineering, College of Business, College of Arts & Sciences, Libraries, Student Life, Capital Projects), Channel (dropdown: Direct Mail, Email, Video, In-Person Briefing, Gift Officer Talking Points, Magazine, Social, Event), Status (status: Concept, Drafting, Review, Advancement Approval, Comms Approval, Production, Distributed), Scheduled Date (date), Writer (people), Gift Officer Contact (people), Related Stories (connect to Impact Stories).
>
> 2. **Impact Stories**: columns for Story Title (text), Story Type (dropdown: Scholarship Recipient, Research Breakthrough, Faculty Achievement, Building/Facility, Student Success, Community Impact, Innovation/Startup, Alumni Achievement), Department/College (dropdown), Gift Designation Connection (text — which funds/gifts does this story relate to), Story URL (link), Story Status (status: Identified, Interviewing, Drafting, Published, Repurposed for Donors), Photos/Video (files), Key Quote (text), Impact Metrics (text — quantifiable outcomes), Writer (people), Donor Touchpoint Potential (status: High, Medium, Low).
>
> 3. **Campaign Communications**: columns for Campaign Name (text), Campaign Phase (status: Quiet Phase, Public Launch, Active Fundraising, Celebration/Closing), Message (text), Audience (dropdown), Channel (dropdown), Scheduled Date (date), Gift Officer Toolkit Included (checkbox), Status (status: Planning, In Production, Approved, Deployed, Analyzing), Results (long text), Goal Amount (numbers), Raised to Date (numbers).
>
> Add automations: when an Impact Story is published and has 'High' Donor Touchpoint Potential, create a Donor Communication item for the relevant segment. When a Donor Communication is 'Distributed,' notify the gift officer contact. When Campaign Phase changes, trigger the next batch of scheduled communications. Create a Dashboard with: donor communications by segment and type, impact story production pipeline, campaign fundraising progress, communications distributed this quarter, and gift officer toolkit status."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** DonorStory
**Agent Purpose:** Automatically match institutional stories to donor interests and generate personalized impact communications at scale.

**Triggers:**
- When a new Impact Story is published with "High" Donor Touchpoint Potential
- Monthly on the 15th to generate stewardship content suggestions for major donors
- When a new major gift ($100K+) is recorded (to initiate stewardship communications sequence)
- Quarterly for campaign communications calendar planning
- When a gift officer requests talking points for an upcoming donor meeting

**Actions:**
- Match new stories to donor interest areas and giving designations, creating personalized communication items
- Draft personalized impact paragraphs for major donors connecting their specific gift to institutional outcomes
- Generate gift officer talking points for donor meetings with relevant recent stories, metrics, and appreciation language
- Create quarterly stewardship report drafts for top 50 donors with personalized content based on their giving portfolio
- Suggest optimal communication timing based on donor engagement history and giving patterns
- Flag donors who haven't received a non-solicitation touchpoint in 90+ days

**Data Required:**
- Donor CRM data (giving history, designations, interests, relationship manager)
- Published institutional stories and their topic tags
- University outcomes data (student success metrics, research metrics, building utilization)
- Gift officer calendar and meeting schedules
- Historical donor communication engagement data

**Autonomy Level:** Human-in-the-Loop
Agent drafts and recommends; all donor-facing communications require human review and advancement approval before distribution. Gift officer talking points are suggestions, not scripts. Stewardship reports are drafts for human personalization.

**Example Interaction:**
> A new Impact Story is published about three first-generation college students who graduated with honors, all supported by need-based scholarships. DonorStory identifies 47 donors who have given to scholarship funds, segments them by giving level, and creates tailored communication items. For the $2M scholarship endowment donor, it drafts a personal note: "Dear Margaret, the three students featured in this story were all supported by the Chen Family Scholarship — the fund you and David established in 2019. Since its creation, the fund has supported 31 students, with a 94% graduation rate and average GPA of 3.6. Two of this year's graduates are heading to medical school." For annual fund scholarship donors, it creates a group email with the story link and aggregate impact data. Gift officers for the top 10 scholarship donors receive talking point cards for their next meetings.

---

### Use Case 7: Government & Community Relations Communications

**Relevance:** Medium
**Value Driver:** Consolidate Tech Stack with AI

#### The Pain
University government relations and community affairs generate significant communications needs that often operate in silos from the main PR team. Legislative session tracking, testimony preparation, community meeting materials, economic impact reports, and town-gown relationship management all require content that aligns with institutional messaging but addresses distinct audiences. When a state legislator questions the university's budget, the government relations team needs data-driven talking points within hours. When neighbors complain about a new construction project, community relations needs a response that aligns with the official project communications. These workflows are tracked in individual email inboxes and personal spreadsheets, creating risk and inefficiency.

#### The Solution
monday.com boards for **Legislative Tracking** (bills, committee hearings, university position, talking points, testimony status), **Community Engagement** (neighborhood meetings, development project updates, partnership initiatives, feedback tracking), and **Government Communications** (official correspondence, testimony drafts, economic impact talking points, elected official relationship management). Connected to the main communications boards for message alignment and shared asset access.

#### The Outcome
50% faster response to legislative inquiries with pre-built talking points. Coordinated community communications during campus development projects. Complete audit trail of government communications for compliance. Aligned messaging across all external audiences.

#### Discovery Questions
1. "When a state legislator or their staff contacts you with a question about university funding, research, or policy, how quickly can you provide data-driven talking points?"
2. "How do you currently coordinate messaging between government relations, community affairs, and the central communications team to ensure consistency?"
3. "During legislative session, how do you track which bills affect the university, what your official position is, and what communications have gone out to which legislators?"
4. "How do you manage community relations around campus construction or expansion projects, and is that communications coordinated with the main PR team?"

#### Industry Context
Public universities are directly accountable to state legislatures for funding. Even private universities have significant government relations needs (federal research funding, student financial aid policy, tax-exempt status, zoning). Town-gown relationships are perennial — noise complaints, parking, property tax exemptions, and development impact are constant issues. Many universities have formal government relations offices that lobby at state and federal levels. Economic impact studies ($X billion contribution to the state economy, X,000 jobs) are key talking points but need regular updating. FOIA/public records requests add complexity for public institutions.

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "Build a Government & Community Relations Communications tracker for a university. Create three connected boards:
>
> 1. **Legislative Tracker**: columns for Bill/Issue (text), Legislative Body (dropdown: US Congress, State Senate, State House, City Council, County Board), Bill Number (text), Status (status: Introduced, In Committee, Floor Vote, Passed, Signed, Vetoed, Died), University Impact (status: Positive, Neutral, Negative, Mixed, Monitoring), University Position (dropdown: Support, Oppose, Neutral, Monitor, Amend), Key Legislators (text), Talking Points (long text), Testimony Status (status: Not Needed, Drafting, Submitted, Delivered), Government Relations Lead (people), Communications Lead (people), Session/Year (text), Related Communications (connect to Government Communications).
>
> 2. **Community Engagement**: columns for Initiative (text), Type (dropdown: Neighborhood Meeting, Development Project Update, Partnership Announcement, Community Event, Complaint/Issue Response, Economic Impact Report), Community/Neighborhood (text), Date (date), Status (status: Planning, Scheduled, Completed, Follow-up Needed, Closed), Attendees/Reach (numbers), Key Concerns Raised (long text), Action Items (long text), Lead (people), Related Project (text), Sentiment (status: Positive, Neutral, Negative, Mixed), Follow-up Communications (connect to Government Communications).
>
> 3. **Government Communications**: columns for Subject (text), Type (dropdown: Letter to Legislator, Testimony, Talking Points, Economic Impact Brief, Federal Grant Report, Policy Response, Community Newsletter, FOIA Response), Recipient/Audience (text), Status (status: Drafting, Legal Review, Leadership Approval, Sent/Published, Filed), Date Sent (date), Author (people), Approved By (people), Related Legislative Item (connect to Legislative Tracker), Related Community Item (connect to Community Engagement), Files (files).
>
> Add automations: when a Bill Status changes to 'In Committee' and University Impact is 'Negative,' alert the government relations and communications leads. When a Community Engagement item has 'Follow-up Needed' for more than 5 business days, send a reminder. When Testimony Status moves to 'Drafting,' create a linked Government Communications item. Create a Dashboard with: active legislative items by position and status, community engagement calendar, government communications pipeline, and legislative session activity summary."

Note: Vibe builds apps/boards/workflows — NOT agents.

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** CivicConnect
**Agent Purpose:** Monitor legislative activity relevant to higher education, generate talking points, and ensure coordinated government and community communications.

**Triggers:**
- Daily scan of state and federal legislative tracking feeds for higher-education-related bills
- When a new Community Engagement item is created with Type "Complaint/Issue Response"
- When a legislator's office contacts the university (new Government Communications item with Type "Policy Response")
- Weekly during legislative session for status summary
- When University Impact assessment changes to "Negative"

**Actions:**
- Create new Legislative Tracker items from detected bills with auto-populated impact assessment and relevant talking points
- Generate data-driven talking points pulling from the university's economic impact data, enrollment statistics, and research expenditure figures
- Draft response templates for community complaints based on complaint type and previous successful responses
- Compile weekly legislative session briefing for the VP of Government Relations and CCO
- Flag when community sentiment on a topic trends negative across multiple engagement items
- Cross-reference government communications with central PR messaging to flag potential inconsistencies

**Data Required:**
- State and federal legislative tracking feeds (LegiScan or similar)
- University economic impact data and institutional research statistics
- Community engagement history and sentiment data
- Central communications messaging frameworks and approved talking points
- Contact directory for legislators and their staff

**Autonomy Level:** Escalation-Based
Agent monitors and drafts autonomously. All external communications to legislators, community members, or media require human approval. Impact assessments are recommendations for human confirmation. Talking points are drafts, never sent directly.

**Example Interaction:**
> CivicConnect detects that State Senate Bill 1247, "Higher Education Accountability and Transparency Act," has been introduced and moved to the Education Committee. The agent creates a Legislative Tracker item, assesses the impact as "Negative" based on provisions requiring line-item budget disclosure and performance-based funding metrics, and drafts initial talking points: "Our university contributes $4.2B annually to the state economy and supports 28,000 jobs. Current reporting already exceeds proposed requirements under HB 892 (2024). Performance metrics as defined in SB 1247 don't account for research mission institutions..." The government relations director reviews, refines the points, and uses them in a call with the bill's sponsor's chief of staff the next day.

---

## Industry Terminology

| Term | Definition |
|------|-----------|
| Earned Media | Media coverage obtained through PR efforts rather than paid advertising |
| AVE (Advertising Value Equivalency) | Controversial metric estimating what earned media coverage would cost if purchased as advertising — many PR professionals now prefer "earned media value" or impression-based metrics |
| Clery Act | Federal law requiring universities to disclose campus crime statistics and issue timely warnings |
| FERPA | Family Educational Rights and Privacy Act — restricts disclosure of student education records |
| Title IX | Federal civil rights law prohibiting sex discrimination, including sexual harassment/assault, with specific communication implications |
| Shared Governance | Decision-making model where faculty, administration, and sometimes students share authority — impacts what can be communicated and when |
| Town-Gown Relations | The relationship between a university and the surrounding community |
| Yield Season | Spring period when admitted students decide where to enroll — intense communications and marketing period (April 1 - May 1) |
| CASE | Council for Advancement and Support of Education — professional organization setting standards for communications, alumni relations, and fundraising |
| Embargo | Agreement with a journal or news outlet to hold a story until a specific date/time |
| UGC | User-Generated Content — content created by students, alumni, or fans rather than the institution |
| SOV (Share of Voice) | Percentage of total media coverage in a category attributed to the university vs. peer institutions |
| Giving Day | Annual 24-hour fundraising event requiring intense coordinated communications across all channels |
| FOIA | Freedom of Information Act — public universities must respond to public records requests, including communications |

## Typical Stakeholder Roles

| Role | Responsibility | Influence |
|------|---------------|-----------|
| Chief Communications Officer (CCO) / VP of University Relations | Overall communications strategy, crisis management, leadership messaging | Decision-maker |
| Director of Media Relations | Journalist relationships, press releases, media inquiries, research storytelling | Decision-maker for media strategy |
| Director of Digital/Social Media | Social media strategy across platforms, digital content, web presence | Decision-maker for digital |
| Director of Internal Communications | Faculty/staff communications, town halls, employee newsletter | Influencer |
| Director of Government Relations | Legislative affairs, community relations, government communications | Influencer (separate budget) |
| University President / Chancellor | Ultimate spokesperson, sets institutional tone and priorities | Executive sponsor |
| Provost | Academic messaging, research communications priorities, faculty affairs | Key stakeholder |
| VP of Advancement / Development | Donor communications, campaign messaging, alumni relations | Key stakeholder (shared budget interest) |
| General Counsel | Legal review of sensitive communications, FERPA/Clery compliance | Gatekeeper |
| Director of Athletics Communications (SID) | Athletics media relations, often largest social following | Independent operator |
| College/Department Communications Leads | Decentralized communicators within academic units | Users (brand governance targets) |

## Adjacent Departments

| Department | Connection | Opportunity |
|-----------|-----------|-------------|
| Marketing (Admissions/Enrollment) | Shared brand assets, content overlap, prospective student audience | Unified content management platform, brand governance across marketing and PR |
| Advancement / Development | Donor storytelling, impact narratives, campaign communications | Integrated story-to-donor pipeline (Use Case 6) |
| IT | Website CMS management, digital infrastructure, cybersecurity incident communications | Unified digital platform, incident communications integration |
| Student Affairs | Student crisis response, student organization communications, campus life content | Crisis communications coordination, student story pipeline |
| Athletics | Media relations, social media (often largest following), broadcast partnerships | Brand alignment, social media governance, shared media contacts |
| Human Resources | Employee communications, benefits messaging, recruitment marketing | Internal communications coordination (Use Case 5) |

## Competitive Landscape

| Tool | Positioning | Displacement Opportunity |
|------|------------|------------------------|
| Cision / PR Newswire | Media database, press release distribution, media monitoring | Expensive ($30K-$80K/year), limited workflow. monday.com replaces the tracking/workflow layer; may still need distribution |
| Meltwater | Media intelligence, social listening, analytics | High cost, analytics-focused but poor workflow. monday.com handles the action layer |
| Sprout Social / Hootsuite | Social media management, scheduling, analytics | Good at publishing but poor at cross-team coordination and approval workflows. monday.com adds the collaboration layer |
| Asana / Trello | Generic project management for content calendars | Lack media relations, crisis management, and analytics features. monday.com provides industry-specific capability |
| Salesforce (via Advancement) | Donor CRM with some communications features | Complex, expensive, and not built for content production. monday.com bridges CRM data with content workflows |
| Slack / Teams | Real-time communication during crises | Great for chat, terrible for structured workflow, tracking, and audit trails. monday.com provides the system of record |

## Objection Handling

| Objection | Response |
|-----------|----------|
| "We already use Cision/Meltwater for media relations" | "Those are great for media databases and monitoring, but where do your workflows live? Pitching, follow-up, coverage tracking, and crisis response coordination all happen in email and spreadsheets. monday.com is the operational layer that makes those tools more effective — and may replace some of their functionality entirely." |
| "Our crisis communications plan is in a binder/shared drive" | "A plan in a document is a starting point. But when a crisis actually hits at 2 AM, can your team activate it in real-time — assigning tasks, tracking approvals, coordinating across channels, and notifying stakeholders — from their phones? That's what a live crisis command center does." |
| "We're a small team and can't learn another tool" | "That's exactly why this matters. A 5-person team managing 15 social accounts, media relations, crisis comms, and internal communications needs force multiplication, not more manual work. The teams that adopt this typically save 10-15 hours per week on reporting alone." |
| "Our decentralized model means colleges do their own communications" | "Which is exactly the challenge — and the opportunity. monday.com gives you visibility into decentralized communications without centralizing control. Brand governance dashboards show you what's happening across all accounts, and shared content calendars prevent conflicting messages, while colleges keep their autonomy." |
| "We can't justify the budget — our administration always cuts communications first" | "That's often because communications can't demonstrate ROI. With systematic tracking of media coverage, donor communications impact, social engagement, and crisis response metrics, you can show leadership exactly what the team delivers — and what would be lost. Data-driven budget justification is the first win." |

## Proof Points
*(To be populated with customer references)*
- [University communications office consolidating media relations and social media management]
- [Higher ed institution using monday.com for crisis communications coordination]
- [University advancement team integrating donor communications with storytelling pipeline]

---

*Generated: February 18, 2026 | Version: 2.0 (with Vibe Prompts + Agent Blueprints)*
