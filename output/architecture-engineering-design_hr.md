# Architecture, Engineering & Design × HR
## monday.com SE Playbook

### Industry Context

The Architecture, Engineering & Design (AEC) industry operates in a complex regulatory environment where professional licensure, continuing education, and design expertise are paramount. HR departments in AEC firms face unique challenges managing a workforce that includes licensed professionals (PEs, RAs, LEED APs), intern architects completing AXP hours, and design talent across multiple disciplines. The industry's project-based nature creates fluctuating staffing needs, while stringent professional development requirements (AIA CEUs, PE PDHs) demand careful tracking and compliance management.

Studio culture remains central to AEC firms, where collaborative design processes like charrettes, pin-ups, and design crits define the work environment. HR must balance maintaining this creative culture while managing the business realities of professional liability, licensure reciprocity across states, and the competitive talent market. The industry's emphasis on portfolio-based hiring, long intern development periods (typically 3-4 years for AXP completion), and the transition from intern architect to licensed professional creates complex career progression pathways that HR must navigate.

The AEC industry faces ongoing challenges with diversity and inclusion, historically being a homogeneous field that's actively working to broaden its talent pipeline. HR departments must manage recruitment strategies that attract diverse talent while ensuring candidates meet the technical and professional requirements inherent to design and engineering roles. Multi-office coordination, project team assembly based on specialized skills, and the management of both creative and technical personnel add layers of complexity to traditional HR functions.

### Department Profile
- **Typical Team Size:** 2-8 professionals (varies by firm size: 50-500+ total employees)
- **Key Stakeholders:** Design principals, project managers, office managing partners, NCARB/state licensing coordinators, recruitment agencies specializing in AEC talent
- **Core KPIs:** Time-to-fill specialized positions, licensure compliance rates, AXP completion rates, retention of licensed professionals, studio culture satisfaction scores, continuing education compliance, diversity metrics
- **Common Tools Replaced:** Excel spreadsheets for licensure tracking, separate AXP hour logging systems, disparate recruiting platforms, manual continuing education tracking, paper-based performance reviews, separate project staffing tools

---

### Use Cases

#### Use Case 1: AXP Hour Tracking & Licensure Pathway Management
**Pain Point:** Intern architects must complete 3,740 AXP hours across six experience areas, with complex NCARB reporting requirements. Manual tracking leads to lost records, delayed ARE exam eligibility, and frustrated interns who can't see their progress clearly.
**monday.com Solution:** Automated AXP hour tracking with approval workflows, progress visualization, and NCARB reporting integration. Supervisors can validate hours, track experience area distribution, and monitor intern development milestones.
**Key Boards/Workflows:** AXP Progress Tracker board with intern profiles, experience area columns, supervisor approval automation, progress charts, and ARE exam eligibility alerts.
**Vibe Prompt:** "Create an AXP hour tracking system for our intern architects that automatically calculates progress toward licensure, sends reminders for hour logging, and alerts supervisors when validation is needed. Include visual progress bars for each of the six experience areas."
**Agent Blueprint:** An AI agent that monitors AXP hour entries, validates completeness, sends automated reminders to interns and supervisors, flags potential issues with hour distribution, and generates NCARB-ready reports. The agent could also predict licensure timeline based on current progress and suggest experience area adjustments.
**Value Driver:** Replace or Radically Augment Headcount
**Estimated Impact:** Reduces HR administrative time by 15 hours/month per intern, improves licensure timeline predictability by 25%, increases intern retention through better visibility into career progression.

#### Use Case 2: Professional Licensing Compliance & Renewal Management
**Pain Point:** Managing PE, RA, and LEED AP renewals across multiple states with varying PDH/CEU requirements. Missing renewals can halt project work and create liability issues. Manual tracking of continuing education credits is error-prone and time-intensive.
**monday.com Solution:** Centralized licensing database with automated renewal reminders, continuing education credit tracking, and compliance reporting. Integration with AIA, NCEES, and NCARB systems for seamless record management.
**Key Boards/Workflows:** Professional Licensing Dashboard with license status columns, renewal timeline automation, CEU/PDH credit tracking, and compliance alert system.
**Vibe Prompt:** "Build a professional licensing management system that tracks all our architects' and engineers' licenses, automatically reminds them about renewals 90 days in advance, logs their continuing education credits, and generates compliance reports for each state we practice in."
**Agent Blueprint:** An AI agent that monitors licensing databases, sends personalized renewal reminders based on state requirements, validates continuing education submissions, flags potential compliance issues, and maintains reciprocity records for multi-state practice. The agent could also recommend relevant training programs based on license requirements.
**Value Driver:** Consolidate Tech Stack with AI
**Estimated Impact:** Prevents 95% of missed renewals, reduces compliance-related work stoppage by 80%, consolidates 3-5 separate tracking systems into one platform.

#### Use Case 3: Studio Culture & Employee Experience Optimization
**Pain Point:** Maintaining design studio culture across multiple offices while tracking employee satisfaction, design crit participation, and creative development opportunities. Traditional surveys don't capture the nuanced aspects of design culture and collaborative creativity.
**monday.com Solution:** Studio culture dashboard tracking design crit participation, project collaboration scores, creative initiative involvement, and cultural health metrics. Automated pulse surveys with design-specific questions and peer feedback mechanisms.
**Key Boards/Workflows:** Studio Culture Health board with employee engagement tracking, design crit scheduling, mentorship pairing, and cultural event planning automation.
**Vibe Prompt:** "Create a studio culture tracking system that monitors how our architects and designers participate in design crits, collaborate on projects, and engage with our creative initiatives. Include ways to schedule pin-ups and track mentorship relationships between senior designers and junior staff."
**Agent Blueprint:** An AI agent that analyzes participation patterns in design crits and collaborative activities, identifies employees who may be disconnected from studio culture, suggests optimal mentorship pairings based on skills and personalities, and recommends interventions to strengthen creative collaboration.
**Value Driver:** Scale Impact Without Overhead
**Estimated Impact:** Improves employee satisfaction scores by 20%, increases design crit participation by 30%, reduces turnover of creative talent by 15%.

#### Use Case 4: Specialized Talent Acquisition & Portfolio-Based Hiring
**Pain Point:** Recruiting licensed professionals and specialized design talent requires portfolio review, technical skill assessment, and cultural fit evaluation. The process is lengthy, involves multiple stakeholders, and often loses candidates to competitors with faster hiring processes.
**monday.com Solution:** Portfolio-based candidate tracking with automated skill matching, interview coordination, and collaborative evaluation workflows. Integration with AEC-specific job boards and professional networks.
**Key Boards/Workflows:** Candidate Pipeline board with portfolio review stages, skill assessment automation, interviewer coordination, and hiring decision workflows.
**Vibe Prompt:** "Set up a hiring process for architects and engineers that tracks candidate portfolios, coordinates design reviews with our principals, schedules technical interviews, and manages the entire hiring pipeline from application to offer. Include ways to score portfolios and track which candidates are reviewing at each stage."
**Agent Blueprint:** An AI agent that screens portfolios based on project types and design quality, matches candidates to open positions based on technical skills and experience, coordinates complex interview schedules with busy design principals, and provides hiring recommendations based on comprehensive evaluation data.
**Value Driver:** Replace or Radically Augment Headcount
**Estimated Impact:** Reduces time-to-hire by 35%, improves candidate experience scores by 40%, increases offer acceptance rates by 25%.

#### Use Case 5: Continuing Education & Professional Development Planning
**Pain Point:** AIA CEUs, PE PDHs, and LEED maintenance requirements vary by individual and change over time. Coordinating group training, tracking individual progress, and ensuring compliance across diverse professional requirements is overwhelming for HR teams.
**monday.com Solution:** Personalized professional development tracking with automated compliance monitoring, training recommendation engine, and group learning coordination. Integration with professional organizations and training providers.
**Key Boards/Workflows:** Professional Development board with individual learning plans, compliance tracking automation, training coordination, and skills development monitoring.
**Vibe Prompt:** "Create a professional development system that tracks each employee's continuing education requirements based on their licenses, suggests relevant training opportunities, coordinates group learning sessions, and ensures everyone stays compliant with their professional obligations."
**Agent Blueprint:** An AI agent that creates personalized learning plans based on individual license requirements and career goals, recommends relevant training programs and conferences, coordinates group learning opportunities, and proactively identifies compliance risks before they become issues.
**Value Driver:** Consolidate Tech Stack with AI
**Estimated Impact:** Increases continuing education compliance rates to 100%, reduces training coordination time by 50%, improves employee skill development satisfaction by 45%.

#### Use Case 6: Project Team Assembly & Skills Matching
**Pain Point:** Assembling project teams requires matching specialized skills (sustainable design, historic preservation, structural analysis) with project requirements while balancing workload across offices and ensuring proper licensure coverage.
**monday.com Solution:** Skills inventory with automated team assembly recommendations, workload balancing algorithms, and project-specific expertise matching. Real-time capacity planning and resource optimization.
**Key Boards/Workflows:** Project Staffing board with skills matrix, workload visualization, team assembly automation, and capacity planning dashboards.
**Vibe Prompt:** "Build a project staffing system that matches our architects and engineers to projects based on their specialized skills, current workload, and license requirements. Include ways to visualize team capacity across our offices and automatically suggest optimal project team compositions."
**Agent Blueprint:** An AI agent that analyzes project requirements and matches them with available talent, optimizes team compositions for skill diversity and workload balance, predicts project staffing needs based on pipeline data, and recommends strategic hiring or contractor engagement based on capacity analysis.
**Value Driver:** Scale Impact Without Overhead
**Estimated Impact:** Improves project team efficiency by 30%, reduces over-staffing by 20%, increases optimal skill utilization by 40%.

#### Use Case 7: Diversity & Inclusion Initiative Management
**Pain Point:** The AEC industry's historical homogeneity requires active diversity initiatives, but tracking progress, measuring impact, and coordinating inclusive practices across studios and project teams is complex and often inconsistent.
**monday.com Solution:** Comprehensive D&I tracking with recruitment analytics, advancement monitoring, inclusive culture measurement, and initiative impact assessment. Automated reporting and intervention recommendations.
**Key Boards/Workflows:** Diversity Initiative board with recruitment tracking, advancement monitoring, inclusive culture metrics, and intervention planning automation.
**Vibe Prompt:** "Create a diversity and inclusion tracking system that monitors our recruiting efforts across different demographic groups, tracks advancement opportunities for underrepresented employees, measures inclusive culture indicators, and helps us coordinate D&I initiatives across all our studio locations."
**Agent Blueprint:** An AI agent that analyzes recruitment and advancement data for bias patterns, monitors inclusive culture indicators through sentiment analysis and participation metrics, recommends targeted interventions to improve diversity outcomes, and generates comprehensive D&I progress reports for leadership review.
**Value Driver:** Scale Impact Without Overhead
**Estimated Impact:** Increases diverse hiring by 25%, improves inclusion scores by 35%, reduces bias-related turnover by 30%.

#### Use Case 8: Internship Program & Design Competition Coordination
**Pain Point:** Managing architecture internship programs, summer design competitions, charrette events, and academic partnerships requires extensive coordination between HR, design principals, and external institutions. Traditional methods lack visibility and integration.
**monday.com Solution:** Comprehensive internship and competition management with academic partner coordination, event planning automation, and talent pipeline development. Portfolio collection and evaluation workflows.
**Key Boards/Workflows:** Internship Program board with academic partnerships, competition coordination, portfolio evaluation, and talent development tracking.
**Vibe Prompt:** "Set up an internship program management system that coordinates with architecture schools, manages summer design competitions, tracks intern portfolio development, and helps us build relationships with academic partners. Include ways to schedule design charrettes and coordinate with faculty advisors."
**Agent Blueprint:** An AI agent that manages relationships with architecture schools, coordinates internship placements and competition entries, evaluates portfolio submissions using design quality metrics, schedules complex multi-stakeholder events, and tracks long-term talent pipeline development from academic partnerships.
**Value Driver:** Replace or Radically Augment Headcount
**Estimated Impact:** Increases internship program efficiency by 50%, improves academic partnership ROI by 40%, enhances long-term talent pipeline quality by 35%.

---

### Discovery Questions

1. "How do you currently track AXP hours and ensure your intern architects stay on track for licensure? What happens when someone falls behind or has gaps in their experience areas?"

2. "Walk me through your process for managing professional license renewals across different states. How do you ensure no one misses a renewal deadline, and what systems do you use to track continuing education credits?"

3. "How do you maintain your studio's design culture across multiple offices? What methods do you use to measure employee engagement in creative activities like design crits and collaborative projects?"

4. "When you're hiring architects or engineers, how do you evaluate portfolios and coordinate the complex interview process with your design principals? What's your biggest bottleneck in specialized talent acquisition?"

5. "How do you assemble project teams and match specialized skills to project requirements? Do you have visibility into who's available, their current workload, and their specific expertise areas?"

6. "What systems do you use to track diversity and inclusion metrics, and how do you measure the success of your D&I initiatives across different studios and project teams?"

7. "How do you coordinate your internship programs and design competitions with academic partners? What's your process for managing these relationships and tracking long-term talent pipeline development?"

### Competitive Positioning

**monday.com wins against alternatives by offering:**

**vs. Excel/Manual Systems:** Real-time collaboration, automated workflows, and visual project tracking eliminate the error-prone manual processes that plague licensure and compliance management in AEC firms.

**vs. Generic HR Platforms (Workday, BambooHR):** Deep customization capabilities allow for AEC-specific workflows like AXP hour tracking, portfolio-based hiring, and studio culture management that generic platforms cannot accommodate.

**vs. AEC-Specific Tools (Newforma, Deltek):** monday.com provides the flexibility to adapt to unique firm cultures and processes while offering superior user experience and visual project management that resonates with design-oriented professionals.

**vs. Separate Point Solutions:** Consolidates multiple specialized systems (NCARB tracking, continuing education management, recruitment platforms) into one unified platform, reducing training overhead and improving data consistency.

**Unique Value:** The visual, design-friendly interface appeals to architects and designers, while the platform's flexibility allows firms to maintain their unique studio culture and processes rather than forcing standardization.

### ROI Framework

**Metrics and Calculations:**

**Administrative Time Savings:**
- AXP tracking: 15 hours/month per intern × $50/hour × number of interns
- License renewal management: 8 hours/month per licensed professional × $60/hour × licensed staff count
- Professional development coordination: 20 hours/month × $55/hour

**Risk Mitigation:**
- Prevented license lapses: $50,000 average cost per incident (project delays, legal complications)
- Compliance violations avoided: $25,000 average regulatory penalty
- Improved retention: $75,000 average replacement cost for licensed professional

**Productivity Gains:**
- Faster hiring: 35% reduction in time-to-hire × $150/day opportunity cost per open position
- Optimized project staffing: 20% reduction in over-staffing costs
- Improved team efficiency: 30% productivity gain on optimally-staffed projects

**Typical ROI Calculation for 100-person AEC firm:**
- Platform cost: $24,000/year
- Administrative time savings: $156,000/year
- Risk mitigation: $75,000/year (conservative estimate)
- Productivity gains: $200,000/year
- **Total ROI: 1,700% within first year**

### Quick Wins

1. **AXP Hour Dashboard (Week 1):** Set up visual tracking for all intern architects showing progress toward licensure eligibility. Immediate transparency improves satisfaction and reduces HR inquiry volume by 60%.

2. **License Renewal Alert System (Week 1):** Create automated reminders for all professional licenses with 90/60/30-day advance notifications. Prevents emergency renewal situations and project work stoppages.

3. **Portfolio-Based Candidate Tracking (Week 1):** Implement candidate pipeline with portfolio review stages and collaborative evaluation workflows. Streamlines hiring process immediately and improves candidate experience.

4. **Continuing Education Credit Tracker (Week 1):** Deploy simple credit logging system with compliance status visualization. Provides immediate visibility into professional development requirements and compliance status across all licensed staff.