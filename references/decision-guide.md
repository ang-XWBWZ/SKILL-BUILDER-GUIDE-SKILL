---
name: decision-guide
description: Decision tree methodology for choosing which skills to generate for a project, based on project scope, AI autonomy expectations, and existing documentation.
model_tier: L3
skill_tier: meta
version: 1.0.0
status: active
---

# Decision Guide — Skill Initialization Methodology

> *知人者智，自知者明。* ——《道德经》
> The right skill, at the right time, for the right project.

> **Load when**: ANALYZE phase — deciding which skills to generate for a project.
> **Principle**: The guide asks questions. The human answers. No presets.

---

## 1. Three Decision Questions

### Question 1: What's your project scope?

| Answer | Signal |
|------|------|
| Quick fixes / solo prototype | Single module, ≤2 people, short-term |
| Ongoing product / small team | 2-5 modules, 2-5 people, no end date |
| Multi-module / multi-service / handoff needed | 5+ modules, multiple data sources, team turnover |

### Question 2: How autonomous should the AI be?

| Answer | Meaning |
|------|------|
| Passive lookup only | Answer questions, don't suggest |
| Independent within a module | Understand context, operate autonomously within module boundaries |
| Cross-module analysis, proactive reporting | Alert on cross-module impacts without being asked |

### Question 3: Do you have existing conventions documented?

| Answer | Meaning |
|------|------|
| No, extract from code | Full SCAN, infer conventions from source |
| Yes, use them | User docs take priority, SCAN fills gaps |

---

## 2. Answers → Natural Skill Set

No preset combos. The agent recommends a skill list based on the answer combination, and explains why to the human.

### Derivation Logic (for the agent)

```
Decision:
  dev — every project needs it (tech stack + code conventions)
  code-map — recommended when scope > "solo prototype"
  workflow — recommended when autonomy > "passive"
  change-model — recommended when autonomy = "cross-module"
  call-chain — multi-service + cross-module autonomy
  delegation — team >1 or cross-module autonomy
  CLAUDE.md modules — per claude-md-spec.md §4 matrix
```

### Output Format

```
Based on your answers, I suggest generating these skills:

  {project}-dev — {rationale}
  {project}-code-map — {rationale} (or: not recommended, because...)
  ...

OK? Or adjust as you like.
```

---

## 3. Quick-Start vs Full Pipeline

The human can say "quick start" or "full pipeline" at any time:

| Choice | Meaning |
|------|------|
| "Quick start" | Skip deep scan and validation. Deliver in ≤5 min. Can re-run VALIDATE later |
| "Full pipeline" | ANALYZE→SCAN→GENERATE→VALIDATE→CONFIRM, all five phases |

Neither is presumed better. Quick-start makes sense for prototypes; full pipeline for production. Let the human choose.

---

## 4. Ongoing Extension

Skill generation isn't a one-time event. As the project evolves, offer to add skills:

```
"Your project now has a message queue — add call-chain?"
"New team member joining — add code-map?"
```

The agent asks proactively during the CONFIRM phase.
