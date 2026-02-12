# Use Case Generator PRD
## Scaling SE Expertise Across Every Industry × Department Combination

**Product Owner:** Eduardo Ynaty, VP Solutions Engineering  
**Status:** Draft  
**Created:** 2026-02-09  
**Last Updated:** 2026-02-09

---

## Executive Summary

monday.com's SE team faces a unique challenge: they sell to **every industry** and **every department**. Unlike vertical SaaS companies where SEs can deeply specialize, our SEs must credibly discuss:
- Supply chain optimization with a Manufacturing COO
- Campaign performance with a Media Agency CMO
- Sprint velocity with a FinTech VP Engineering
- Compliance workflows with a Healthcare CISO

This is 149 sub-industries × 15 departments = **2,235 potential conversations**, each requiring industry-specific context, terminology, pain points, and value propositions.

**The Use Case Generator** solves this by creating on-demand, AI-generated playbooks for any Industry × Department combination — grounded in monday.com's Value Framework and enhanced with industry-specific context.

---

## Problem Statement

### The Challenge

1. **Breadth vs. Depth Trade-off**: SEs can't be experts in 2,235 combinations
2. **Generic Playbooks Fall Flat**: "Project management best practices" doesn't resonate with a Pharmaceutical R&D Director the same way it resonates with an Ad Agency Operations Lead
3. **Credibility Gap**: Enterprise buyers expect vendors to understand *their* world — industry terminology, regulatory context, typical org structures, common pain points
4. **Ramp Time**: New SEs take months to build enough contextual knowledge to have strategic conversations
5. **Inconsistent Quality**: Some SEs have deep expertise in certain verticals; others don't — customer experience varies

### The Opportunity

With AI, we can generate **contextually-rich, industry-specific playbooks** that give any SE the foundation to have a credible strategic conversation — not by replacing their expertise, but by providing a starting point they can build on.

### Success Looks Like

> An SE gets assigned a call with the **VP of Operations at a Pharmaceutical company** tomorrow. Today, they've never sold into Pharma. Tonight, they generate a playbook that gives them:
> - The 5-8 most relevant use cases for Ops in Pharma
> - Industry-specific terminology (GxP, batch records, CMO/CDMO, etc.)
> - Discovery questions that demonstrate understanding
> - Pain points unique to this combination
> - How monday.com's AI capabilities map to Pharma Ops challenges
>
> Tomorrow, they walk into the call with enough context to be credible — and enough curiosity to learn more.

---

## User Personas

### Primary: Solutions Engineer (Direct SE)

**Context:** Paired with AEs, responsible for technical win in opportunities across all industries and segments.

**Jobs to Be Done:**
- Prepare for discovery calls with unfamiliar industry/department combinations
- Build credibility quickly with domain-specific language and examples
- Identify the most relevant use cases to demo
- Ask discovery questions that uncover real pain

**Current Workaround:** Google the industry, ask colleagues on Slack, wing it, or avoid diving deep.

### Secondary: Partner Solutions Engineer

**Context:** Enables partners to sell monday.com; needs to train partners on industry-specific positioning.

**Jobs to Be Done:**
- Create enablement content for partners in specific verticals
- Provide partners with talk tracks and discovery frameworks
- Scale partner technical readiness without 1:1 sessions

### Secondary: SE Leadership / Enablement

**Context:** Responsible for SE readiness and performance across the org.

**Jobs to Be Done:**
- Ensure consistent quality of SE conversations across all verticals
- Reduce ramp time for new SEs
- Identify gaps in industry coverage and prioritize enablement

---

## Product Vision

### Phase 1: Use Case Generator (MVP)
Generate playbooks for **Industry × Department** combinations on demand.

### Phase 2: Customer Context Layer
Add **Customer-specific context** — company size, tech stack, known pain points, stakeholder map — for deal-specific playbooks.

### Phase 3: Living Playbooks
Playbooks that improve over time based on SE feedback, win/loss data, and customer outcomes.

---

## Functional Requirements

### FR1: Generate Playbook for Industry × Department

**Description:** Given a sub-industry and department, generate a comprehensive playbook document.

**Inputs:**
- Sub-Industry (from 149 options)
- Department (from 15 options)

**Output:** Markdown document containing:

```
# [Sub-Industry] × [Department] Playbook

## Overview
Brief context on how [Department] operates in [Sub-Industry] companies.
Industry scale, typical org structure, regulatory context if relevant.

## Value Driver Mapping
Which of the 3 Value Drivers resonate most for this combination:
1. Replace or Radically Augment Headcount
2. Consolidate Tech Stack with AI
3. Scale Impact Without Overhead

## Prioritized Use Cases (5-8)
For each use case:
- **Use Case Name**
- **Relevance**: High/Medium/Low
- **Value Driver**: Which of the 3 this maps to
- **Pain Point**: Industry-specific challenge
- **Solution**: monday.com capabilities (specific products, AI features)
- **Outcome**: Measurable business impact
- **Discovery Questions**: 3-5 questions to uncover this pain
- **Industry Context**: Terminology, scale, nuances

## Industry Terminology
Key terms an SE should know when speaking to this audience.
Definitions and context for jargon.

## Typical Stakeholder Roles
Who owns these workflows? Who influences? Who signs?

## Adjacent Departments
Which other departments would be involved or benefit?
Cross-sell and land-expand opportunities.

## Competitive Landscape
What tools does this Industry × Department typically use today?
Displacement opportunities and positioning.

## Objection Handling
Common objections specific to this combination and responses.

## Proof Points
Relevant customer references, case studies, or analogous wins.
(Note: May be populated manually or from reference database)
```

**Acceptance Criteria:**
- [ ] Playbook is generated in < 60 seconds
- [ ] Output is stored as monday.com doc in designated workspace
- [ ] Content is specific to the Industry × Department combination (not generic)
- [ ] Value Framework (3 Value Drivers) is consistently applied
- [ ] Industry terminology is accurate and relevant

---

### FR2: Batch Generation

**Description:** Generate multiple playbooks in a single command.

**Commands:**
```bash
# Generate all MVP combinations (4 industries × 6 departments = 24)
usecase generate --all-mvp

# Generate all departments for one industry
usecase generate --industry="Pharmaceuticals"

# Generate all industries for one department
usecase generate --department="Operations"

# Generate everything (149 × 15 = 2,235) - with rate limiting
usecase generate --all --confirm
```

**Acceptance Criteria:**
- [ ] Batch generation handles rate limiting (Claude API, monday.com API)
- [ ] Progress is displayed in terminal
- [ ] Failed generations are logged and can be retried
- [ ] Existing docs are not overwritten unless --force flag is used

---

### FR3: Status Tracking

**Description:** Track which combinations have been generated.

**Commands:**
```bash
# Update status matrix doc in monday.com
usecase status

# Quick terminal output
usecase list
usecase list --department=Marketing
usecase list --industry="Banking"
```

**Status Matrix Doc:**
```markdown
# Use Case Generation Status
Last updated: 2026-02-09

## MVP Coverage (4 × 6 = 24)
| Sub-Industry | Ops | IT | Mktg | Prod | Sales | PMO |
|--------------|-----|-----|------|------|-------|-----|
| Advertising & Marketing | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| Custom Software & IT | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Management Consulting | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Industrial Machinery | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

**Generated**: 6 / 24 (25%)

## Full Matrix Summary
- Total combinations: 2,235
- Generated: 6
- Pending: 2,229
```

---

### FR4: Playbook Search & Retrieval

**Description:** Quickly find and access existing playbooks.

**Commands:**
```bash
# Search for a playbook
usecase find "pharma" "ops"
# Returns: "Pharmaceuticals × Operations" - Created 2026-02-01
# Link: https://monday.com/docs/...

# Open in browser
usecase open "Pharmaceuticals" "Operations"
```

---

### FR5: Regeneration with Feedback

**Description:** Regenerate a playbook with additional context or corrections.

**Commands:**
```bash
# Regenerate with additional context
usecase regenerate "Pharmaceuticals" "Operations" \
  --context="Focus more on GxP compliance workflows"

# Regenerate with updated prompt template
usecase regenerate "Pharmaceuticals" "Operations" --use-latest-prompt
```

---

## Non-Functional Requirements

### NFR1: Quality
- Generated content must be **specific and actionable**, not generic filler
- Industry terminology must be **accurate** (not hallucinated)
- Use cases must map to **actual monday.com capabilities**
- Discovery questions must be **relevant and insightful**

### NFR2: Performance
- Single playbook generation: < 60 seconds
- Batch generation: Handle rate limiting gracefully
- Status updates: < 5 seconds

### NFR3: Maintainability
- Prompt templates stored as separate files (easy to iterate)
- Configuration in JSON (easy to update industries/departments)
- Logs for debugging failed generations

### NFR4: Security
- API keys stored in environment variables, not code
- monday.com docs created in designated workspace only
- No customer data in prompts or outputs

---

## Information Architecture

### Workspace Structure

```
Workspace: SE Playbooks (ID: 12661971)
├── Folder: Industry × Department Playbooks
│   ├── Advertising & Marketing × Operations
│   ├── Advertising & Marketing × IT
│   ├── Advertising & Marketing × Marketing
│   ├── ...
│   └── Waste Treatment × Sustainability
├── Folder: Meta
│   ├── Use Case Matrix Status
│   ├── Generation Log
│   └── Feedback & Improvements
└── Folder: Templates & Prompts (reference only)
    ├── Current Prompt Template
    └── Value Framework Reference
```

### Naming Convention

**Document Title:** `[Sub-Industry] × [Department]`  
**Examples:**
- `Pharmaceuticals × Operations`
- `Banking × IT`
- `Advertising & Marketing × Creative & Design`

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLI Tool (Python)                        │
├─────────────────────────────────────────────────────────────────┤
│  Commands: generate, status, list, find, open, regenerate      │
└───────────────────────────┬─────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  Config       │   │  Claude API   │   │  monday.com   │
│  (JSON)       │   │  (Reasoning)  │   │  API (Docs)   │
├───────────────┤   ├───────────────┤   ├───────────────┤
│ - Industries  │   │ - Prompt      │   │ - Create doc  │
│ - Departments │   │   template    │   │ - Update doc  │
│ - Workspace   │   │ - Context     │   │ - List docs   │
│ - MVP list    │   │   injection   │   │ - Search      │
└───────────────┘   └───────────────┘   └───────────────┘
```

### File Structure

```
usecase-generator/
├── usecase.py              # CLI entry point
├── config.json             # Industries, departments, settings
├── prompts/
│   ├── playbook.md         # Main generation prompt
│   ├── value_framework.md  # Value Framework context (injected)
│   └── examples/           # Few-shot examples for quality
│       ├── pharma_ops.md
│       └── software_it.md
├── lib/
│   ├── claude.py           # Claude API wrapper
│   ├── monday.py           # monday.com API wrapper
│   ├── generator.py        # Core generation logic
│   └── status.py           # Status tracking
├── tests/
│   └── test_generator.py
└── README.md
```

---

## Prompt Engineering

### Core Prompt Structure

The prompt is the heart of quality. It should:

1. **Set the role:** You are an expert on monday.com AND this industry/department
2. **Inject context:**
   - Value Framework (3 Value Drivers, differentiators)
   - monday.com capabilities (products, AI features)
   - Industry knowledge (from general knowledge + any injected context)
3. **Define output format:** Structured markdown per the playbook template
4. **Provide quality guardrails:**
   - "Be specific, not generic"
   - "Use actual industry terminology"
   - "Every use case must map to a real monday.com capability"
   - "Discovery questions should uncover pain, not pitch product"

### Prompt Template (Enhanced from MVP)

```markdown
You are an expert on monday.com's AI Work Platform AND an expert on 
{{department}} operations within the {{sub_industry}} industry.

## Your Task
Generate a comprehensive playbook that enables a Solutions Engineer 
to have a credible, strategic conversation with a {{department}} leader 
at a {{sub_industry}} company.

## Context: monday.com AI Work Platform

### The Strategic Shift
We are not selling a platform to manage work. We are selling a platform 
where AI does the work. Every conversation should answer: "Why do I 
need this to compete in the AI era?"

### The Three Value Drivers
1. **Replace or Radically Augment Headcount**: Deploy AI agents that 
   work 24/7 — handling work that used to require hiring.
2. **Consolidate Tech Stack with AI**: Replace disconnected tools with 
   one AI platform that does what those tools did — and more.
3. **Scale Impact Without Overhead**: Grow 2x, 5x, 10x without growing 
   the team at the same rate.

### Platform Capabilities
- **mondayDB**: Unified context layer — all data in one place
- **AI Agents**: Service Agent, Lead Agent, Project Risk Agent, custom agents
- **Vibe**: Build any app in minutes with natural language
- **Sidekick**: AI assistant embedded throughout
- **Products**: Work Management, CRM, Service, Dev

### Key Differentiators
1. Unified Context Layer (mondayDB) — AI sees everything
2. AI That Does the Work (not just assists)
3. Build Any App in Minutes (Vibe)
4. Infinite Flexibility with Enterprise Governance
5. Speed to Value

## Industry Context: {{sub_industry}}
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
[Playbook template structure as defined in FR1]

## Quality Requirements
- Be SPECIFIC to {{sub_industry}} × {{department}} — no generic content
- Use ACTUAL industry terminology (not made up)
- Every use case must map to REAL monday.com capabilities
- Discovery questions should UNCOVER pain, not pitch product
- Prioritize use cases by RELEVANCE to this specific combination
- Include competitive context where known
```

---

## MVP Scope

### In Scope (MVP)

| Feature | Priority | Notes |
|---------|----------|-------|
| `generate <industry> <department>` | P0 | Core functionality |
| `generate --all-mvp` | P0 | 4 industries × 6 departments = 24 |
| `status` | P1 | Update matrix doc |
| `list` | P1 | Terminal output |
| Config file with all 149 industries, 15 departments | P0 | |
| Enhanced prompt with Value Framework | P0 | |
| monday.com doc creation | P0 | |
| Basic error handling and logging | P1 | |

### MVP Industries (4)
1. Advertising & Marketing
2. Custom Software & IT Services
3. Management Consulting
4. Industrial Machinery & Equipment

### MVP Departments (6)
1. Operations
2. IT
3. Marketing
4. Product & R&D
5. Sales
6. PMO

### Out of Scope (MVP)

| Feature | Phase | Notes |
|---------|-------|-------|
| Customer context layer | Phase 2 | Company size, tech stack, stakeholders |
| SE feedback mechanism | Phase 2 | Upvote/downvote, suggest edits |
| Proof point integration | Phase 2 | Pull from reference database |
| Regeneration with feedback | Phase 2 | |
| Search/find commands | Phase 2 | |
| Competitive intelligence injection | Phase 2 | |
| Win/loss data integration | Phase 3 | |

---

## Success Metrics

### MVP Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| Playbook quality (SE rating) | 4+ / 5 | Survey 10 SEs after using playbooks |
| Time to prepare for unfamiliar call | -50% | Before/after comparison |
| SE adoption | 50% of SEs use within 30 days | Usage tracking |
| Playbooks generated | 24 MVP + 50 on-demand | Count |

### Long-term Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Technical win rate (unfamiliar verticals) | +10% | CRM data |
| SE ramp time reduction | -30% | Time to first solo call |
| Playbook coverage | 500+ combinations | Status matrix |
| SE contribution (feedback, edits) | 20% of playbooks improved | Edit tracking |

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| AI generates generic/unhelpful content | Medium | High | Strong prompt engineering, few-shot examples, quality review |
| Industry terminology is inaccurate | Medium | High | SE review process, feedback mechanism, iteration |
| SEs don't adopt the tool | Medium | Medium | Socialize early, involve SEs in design, make it easy |
| monday.com API rate limits | Low | Medium | Rate limiting in code, batch processing |
| Claude API costs | Low | Low | Monitor usage, batch efficiently |

---

## Open Questions

1. **How do we validate quality at scale?** 
   - Manual review of first 24?
   - SE feedback loop?
   - Spot-check random samples?

2. **How do we handle industries with heavy regulation?**
   - Healthcare (HIPAA), Finance (SOX/PCI), Government (FedRAMP)
   - Should prompts include regulatory context?
   - Do we need legal review for compliance-adjacent content?

3. **How do we incorporate customer-specific context (Phase 2)?**
   - Pull from CRM?
   - SE input before generation?
   - Integration with deal workspace?

4. **How do we keep playbooks current?**
   - monday.com capabilities change
   - Industry dynamics shift
   - Regeneration schedule? Version tracking?

5. **Should this be a CLI or a monday.com app?**
   - CLI is faster to build
   - monday.com app would have better discoverability and adoption
   - Could CLI be Phase 1, app be Phase 2?

---

## Appendix A: Full Industry List (149)

<details>
<summary>Click to expand</summary>

1. Advertising & Marketing
2. Custom Software & IT Services
3. Management Consulting
4. Colleges & Universities
5. Industrial Machinery & Equipment
6. Banking
7. Non-Profit & Charitable Organizations
8. Commercial & Residential Construction
9. Investment Banking
10. Electricity, Oil & Gas
11. Food & Beverage
12. Training
13. HR & Staffing
14. Pharmaceuticals
15. Research & Development
16. Building Materials
17. Architecture, Engineering & Design
18. Financial Software
19. Freight & Logistics Services
20. Medical & Surgical Hospitals
21. Business Intelligence (BI) Software
22. Membership Organizations
23. Accounting Services
24. Broadcasting
25. Apparel & Accessories Retail
26. Healthcare Software
27. Grocery Retail
28. Electronics
29. Local Government
30. Restaurants
31. Medical Devices & Equipment
32. Telephony & Wireless
33. Photography Studio
34. Security Software
35. Customer Relationship Management (CRM) Software
36. Credit Cards & Transaction Processing
37. Venture Capital & Private Equity
38. Home Improvement & Hardware Retail
39. Publishing
40. Gambling & Gaming
41. Multimedia, Games & Graphics Software
42. Sports Teams & Leagues
43. K-12 Schools
44. Chemicals & Related Products
45. State Government
46. Internet Service Providers & Web Hosting
47. Travel Agencies & Services
48. Religious Organizations
49. Information & Document Management
50. Plastic, Packaging & Containers
51. Flowers, Gifts & Specialty Stores
52. Fitness & Dance Facilities
53. Data Collection & Internet Portals
54. Drug Stores & Pharmacies
55. Civil Engineering Construction
56. Lending & Brokerage
57. Enterprise Resource Planning (ERP) Software
58. Department Stores & Superstores
59. Medical Specialists
60. Furniture
61. Security Products & Services
62. Human Resources Software
63. Airlines & Air Services
64. Automobile Dealers
65. Lodging & Resorts
66. Content & Collaboration Software
67. Physicians Clinics
68. Engineering Software
69. Test & Measurement Equipment
70. Convenience Stores & Gas Stations
71. Telecommunication Equipment
72. Repair Services
73. Sporting & Recreational Equipment Retail
74. Office Products Retail & Distribution
75. Oil & Gas Exploration & Services
76. Mental Health & Rehabilitation Facilities
77. Supply Chain Management (SCM) Software
78. Elderly Care Services
79. Textiles & Apparel
80. Waste Treatment & Recycling
... (remaining 69 to be added from source data)

</details>

---

## Appendix B: Full Department List (15)

### Tier 1: Top Departments (6)
1. Operations
2. IT
3. Marketing
4. Product & R&D
5. Sales
6. PMO

### Tier 2: Important Departments (6)
7. HR
8. Finance
9. Legal
10. Creative & Design
11. Procurement
12. PR & Communications

### Tier 3: Stakeholder Departments (3)
13. Security & Infosec
14. Sustainability
15. Customer Success

---

## Appendix C: Example Playbook Output

See `prompts/examples/pharma_ops.md` for a reference example of expected quality.

---

*Document Version: 1.0*  
*Next Review: After MVP completion*
