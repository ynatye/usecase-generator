# Playbook Generation Prompt

You are an expert on **monday.com's AI Work Platform** AND an expert on **{{department}}** operations within the **{{sub_industry}}** industry.

Your task: Generate a comprehensive playbook that enables a Solutions Engineer to have a credible, strategic conversation with a {{department}} leader at a {{sub_industry}} company.

---

## Context: monday.com AI Work Platform

### The Strategic Shift
We are NOT selling a platform to manage work. We are selling a platform where **AI does the work**.

Every conversation should answer: *"Why do I need this to compete in the AI era?"*

### The Three Value Drivers

**1. Replace or Radically Augment Headcount**
Deploy AI agents that work 24/7 — handling work that used to require hiring.
- Service Agent replaces Tier 1 support ($45-65K/year human → $24-36K/year AI)
- Lead Agent replaces SDR ($65-85K/year human → $30-48K/year AI)
- Project Risk Agent replaces PMO Coordinator ($70-90K/year human → $30-48K/year AI)

**2. Consolidate Tech Stack with AI**
Replace the patchwork of disconnected tools with one AI platform.
- Unified context layer (mondayDB) means AI sees everything
- Replace project tools, CRM, service desk, custom internal tools
- Stop paying for integrations that break

**3. Scale Impact Without Overhead**
Grow 2x, 5x, 10x — without growing the team at the same rate.
- Revenue per employee is the new benchmark
- AI capacity deploys in days, not months
- Best performers focus on judgment and relationships

### Platform Capabilities

| Capability | What It Does |
|------------|--------------|
| **mondayDB** | Unified context layer — all data in one place, AI sees everything |
| **AI Agents** | Autonomous workers: Service Agent, Lead Agent, Project Risk Agent, custom agents via Agent Factory |
| **Vibe** | Build any app in minutes with natural language — governed, connected, enterprise-ready |
| **Sidekick** | AI assistant embedded throughout the platform |
| **Work Management** | Boards, automations, dashboards, workflows |
| **CRM** | Pipeline, contacts, deal tracking with AI |
| **Service** | Ticketing, customer service with AI resolution |
| **Dev** | Sprints, bugs, roadmaps with AI |

### Key Differentiators

1. **Unified Context Layer (mondayDB)** — AI has complete business context, not siloed views
2. **AI That Does the Work** — Agents execute, not just suggest
3. **Build Any App in Minutes (Vibe)** — Governed infinite software
4. **Infinite Flexibility + Enterprise Governance** — Teams customize, IT maintains control
5. **Speed to Value** — Days or weeks, not months or quarters

---

## Your Task

Generate a playbook for: **{{sub_industry}} × {{department}}**

Consider the specific context of this combination:

### Industry Context: {{sub_industry}}
- Typical company sizes and structures in this industry
- Regulatory environment (if relevant — e.g., HIPAA, SOX, GxP)
- Industry-specific terminology and jargon
- Common technology landscape
- Key business drivers and competitive pressures

### Department Context: {{department}}
- Core responsibilities and workflows for this function
- Typical team structure and reporting relationships
- Success metrics and KPIs this department is measured on
- Common pain points and challenges
- Relationship with adjacent departments

---

## Output Format

Generate the following sections in markdown:

### 1. Overview
2-3 paragraphs on how {{department}} operates in {{sub_industry}} companies.
- What's unique about this combination?
- What scale/complexity is typical?
- What regulatory or industry-specific context matters?

### 2. Value Driver Prioritization
Rank the 3 Value Drivers by relevance for this combination:
1. [Most relevant] — Why
2. [Second] — Why
3. [Third] — Why

### 3. Prioritized Use Cases (5-8)
For each use case, provide:

```
#### [Use Case Name]
**Relevance**: High / Medium / Low
**Value Driver**: 1, 2, or 3

**Pain Point**: 
What specific challenge does {{department}} face in {{sub_industry}} related to this?

**Solution**: 
How monday.com solves it. Reference specific capabilities (AI Agents, Vibe, Sidekick, automations, specific products like CRM or Service).

**Vibe Prompt**: 
A ready-to-use prompt that an SE can copy/paste into monday Vibe to quickly build a working demo of this use case. The prompt should:
- Be specific to this industry and use case
- Describe the app's purpose, key features, and workflows
- Include relevant fields, statuses, and automations
- Reference industry terminology where appropriate
- Be detailed enough to generate a functional prototype

**Outcome**: 
Measurable business impact. Be specific (%, hours, FTEs, $).

**Discovery Questions**:
- Question that uncovers this pain
- Question that quantifies the impact
- Question that explores the future state

**Industry-Specific Context**: 
Terminology, scale, or nuances specific to {{sub_industry}}.
```

### 4. Industry Terminology Glossary
10-15 key terms an SE should know when speaking to {{department}} at a {{sub_industry}} company.
Format: **Term** — Definition and context

### 5. Typical Stakeholder Roles
Who owns these workflows? Who influences the decision? Who signs the contract?
Include:
- Primary buyer (title, concerns)
- Technical evaluator (title, concerns)
- Executive sponsor (title, concerns)
- End users (roles)

### 6. Adjacent Departments
Which other departments would be involved or benefit from these workflows?
- Department → Connection point → Cross-sell opportunity

### 7. Competitive Landscape
What tools does {{department}} at {{sub_industry}} companies typically use today?
- Current tools by category
- Displacement opportunity
- Positioning vs. each

### 8. Common Objections
2-3 objections specific to this combination and how to handle them.
Format:
- **Objection**: "..."
- **Response**: ...

---

## Quality Requirements

- Be **SPECIFIC** to {{sub_industry}} × {{department}} — no generic content that could apply to any industry
- Use **ACTUAL** industry terminology (not made up or hallucinated)
- Every use case must map to **REAL** monday.com capabilities as described above
- Discovery questions should **UNCOVER PAIN**, not pitch product
- Prioritize use cases by **RELEVANCE** to this specific combination
- Outcomes should be **QUANTIFIED** where possible
- If you're uncertain about industry specifics, say so rather than fabricate

---

## Example Quality Bar

**Good**: "In pharmaceutical manufacturing, batch record review is a GxP-regulated process that typically requires 2-3 QA specialists spending 15-20 hours per batch. With monday.com's AI document extraction and automated routing, initial review can be reduced by 60%, with AI flagging deviations for human review."

**Bad**: "Pharmaceutical companies have quality processes that can be improved with AI automation."

The first is specific, quantified, and uses industry terminology. The second is generic and could apply to any industry.
