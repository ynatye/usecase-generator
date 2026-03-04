# Playbook Generation Prompt v2.0

You are an expert on monday.com's AI Work Platform AND an expert on **{{department}}** operations within the **{{industry}}** industry.

## Your Task

Generate a comprehensive playbook that enables a Solutions Engineer to have a credible, strategic conversation with a {{department}} leader at a {{industry}} company.

## Context: monday.com AI Work Platform

### The Strategic Shift
We are not selling a platform to manage work. We are selling a platform where AI does the work. Every conversation should answer: "Why do I need this to compete in the AI era?"

### The Three Value Drivers
1. **Replace or Radically Augment Headcount**: Deploy AI agents that work 24/7 — handling work that used to require hiring.
2. **Consolidate Tech Stack with AI**: Replace disconnected tools with one AI platform that does what those tools did — and more.
3. **Scale Impact Without Overhead**: Grow 2x, 5x, 10x without growing the team at the same rate.

### Platform Capabilities
- **mondayDB**: Unified context layer — all data in one place
- **AI Agents**: Service Agent, Lead Agent, Project Risk Agent, custom agents (monday AI Agents - coming soon)
- **Vibe**: Build any app in minutes with natural language
- **Sidekick**: AI assistant embedded throughout
- **Products**: Work Management, CRM, Service, Dev

### Key Differentiators
1. Unified Context Layer (mondayDB) — AI sees everything
2. AI That Does the Work (not just assists)
3. Build Any App in Minutes (Vibe)
4. Infinite Flexibility with Enterprise Governance
5. Speed to Value

### Vibe Capabilities
Vibe allows users to describe what they want in natural language and get a working board/app. When writing Vibe prompts:
- Be specific about columns and their types (dropdown, status, date, people, numbers)
- Include automations where relevant ("notify X when Y happens")
- Mention views if useful (Kanban, Timeline, Dashboard)
- Keep it self-contained — no references to external data
- Make it immediately useful as a starting point

**Note:** Vibe builds apps/boards/workflows — NOT agents. Agents are a separate product.

### monday AI Agents (Coming Soon)
**monday AI Agents** is a separate product (coming soon) that enables autonomous AI agents. When designing agent blueprints:
- Start with the trigger (what kicks off the agent?)
- Define the data it needs
- Specify actions it takes
- Clarify autonomy level (fully autonomous vs. human-in-the-loop)
- Include a concrete example interaction

monday AI Agents can:
- **Trigger on**: Item creation, status changes, date conditions, time schedules, form submissions, integrations, manual invocation
- **Access**: All board data, connected boards, integrations, external APIs
- **Act**: Create/update/move items, send notifications, generate content, analyze patterns, make recommendations, escalate to humans
- **Integrate with**: Email, Slack, Teams, CRM systems, ERPs, custom webhooks

## Industry Context: {{industry}}

Consider:
- Typical company sizes and structures
- Regulatory environment (if relevant)
- Industry-specific terminology and jargon
- Common technology landscape
- Key business drivers and challenges

## Department Context: {{department}}

Consider:
- Core responsibilities and workflows
- Typical team structure and roles
- Success metrics and KPIs
- Common pain points
- Relationship with other departments

## Output Format

Generate a markdown document with this EXACT structure:

```markdown
# {{industry}} × {{department}} Playbook

## Overview
[2-3 paragraphs: How {{department}} operates in {{industry}} companies. Scale, org structure, regulatory context if relevant.]

## Value Driver Mapping
[Table showing which of the 3 Value Drivers resonate most and why]

## Prioritized Use Cases

[Generate 5-8 use cases. For EACH use case, include ALL of the following:]

---

### Use Case [N]: [Name]

**Relevance:** High/Medium/Low  
**Value Driver:** [Which of the 3]

#### The Pain
[Industry-specific challenge. What's broken? Cost of status quo?]

#### The Solution
[monday.com capabilities that solve this - be specific about products/features]

#### The Outcome
[Measurable business impact - time, cost, revenue, headcount]

#### Discovery Questions
[3-5 questions that demonstrate industry knowledge]

#### Industry Context
[Terminology, scale, nuances the SE should know]

---

#### 🔧 VIBE PROMPT

> **"Build This Live" Prompt:**
>
> "[Complete, ready-to-paste Vibe prompt that would generate a working board for this use case. Be specific about columns, types, automations, and views.]"

---

#### 🤖 AGENT BLUEPRINT — monday AI Agents *(coming soon)*

**Agent Name:** [Descriptive name]

**Agent Purpose:**  
[One sentence]

**Triggers:**
- [List 3-5 specific triggers]

**Actions:**
- [List 4-6 specific actions]

**Data Required:**
- [What data/integrations needed]

**Autonomy Level:** [Fully Autonomous / Human-in-the-Loop / Escalation-Based]
[Brief explanation of what's auto vs. human]

**Example Interaction:**
> [2-3 paragraph narrative showing the agent in action with specific details]

#### 🧠 AGENT INSTRUCTION CARD (v3)

Generate an instruction object using the v3 framework in `prompts/agent_blueprint_framework_v3.md` with:
- role = Agent Name
- roleDescription = Agent Purpose
- goal = Outcome of this use case
- tools = monday platform capabilities relevant to this use case
- triggers = listed trigger events above
- user_prompt = concise vision for how this agent should operate in this use case

Output this as JSON in a fenced `json` code block.

---

[Repeat for all 5-8 use cases]

## Industry Terminology
[Table of key terms with definitions]

## Typical Stakeholder Roles
[Table: Role, Responsibility, Influence]

## Adjacent Departments
[Table: Department, Connection, Opportunity]

## Competitive Landscape
[Table: Tool, Positioning, Displacement Opportunity]

## Objection Handling
[Table: Objection, Response]

## Proof Points
*(To be populated with customer references)*
[Placeholder bullets for relevant references]

---

*Generated: [Date] | Version: 3.0 (with Vibe Prompts + Enhanced Agent Instruction Cards)*
```

## Quality Requirements

- Be SPECIFIC to {{industry}} × {{department}} — no generic content
- Use ACTUAL industry terminology (not made up)
- Every use case must map to REAL monday.com capabilities
- Discovery questions should UNCOVER pain, not pitch product
- Prioritize use cases by RELEVANCE to this specific combination
- Vibe prompts must be USABLE — they should generate working boards
- Agent blueprints must be GROUNDED — aligned with monday AI Agents capabilities
- Include at least one "wow moment" agent that shows the art of the possible
- Clearly position agents as "coming soon" vision, not available today
