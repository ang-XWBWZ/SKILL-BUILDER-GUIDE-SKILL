---
name: skill-chain
description: Skill Chain methodology — defining handoff relationships between skills for chain activation. A pattern, not a requirement.
model_tier: L3
skill_tier: meta
version: 1.0.0
status: active
---

# Skill Chain Methodology

> *辅车相依，唇亡齿寒。* ——《左传》
> Skills that know about each other get used together.

## Core Principle

A skill's output is often the natural entry point for another skill. Chain activation > isolated summoning. But chains are suggestions, not obligations — the human always chooses.

## Handoff Definition

Each SKILL.md may include a `## Handoff` section at the end:

```markdown
## Handoff

After completing this skill, recommend the next skill based on output characteristics:

| Condition | Recommend |
|-----------|-----------|
| {measurable condition} | `{project}-{skill-name}` |
```

### Handoff Rules

1. **Conditions must be discriminable** — "new files ≥3", not "if needed"
2. **Recommendations must be specific** — `{project}-code-map`, not "a code-map type skill"
3. **Max 3 recommendations** — more than 3 signals unclear skill boundaries
4. **Avoid long cycles** — A→B→A is fine (different entry contexts). A→B→C→A is not
5. **Explain why** — "This change touched 3 modules, consider running change-model to archive"

## Chain Patterns

### Pattern A: Sequential

```
dev → code-map → workflow → change-model → call-chain
```

For new project setup, generating skills in dependency order.

### Pattern B: Hub-and-Spoke

```
         ┌→ code-map
dev ─────┤
         └→ workflow → change-model
```

dev is the hub; branch based on output characteristics.

### Pattern C: Feedback Loop

```
change-model → call-chain → (discovery) → change-model
```

Validation finds new issues, loops back to analysis.

## Interaction with Pipeline

- **Full pipeline**: Skill Chain written into Handoff during GENERATE phase (hard rule 11)
- **Quick-start path**: Chain relationships implicit in the chosen skill set, added during FILL
- **VALIDATE**: Checks that Handoff-referenced skills exist in the target project

## Metrics (aspirational)

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Chain activation rate | ≥60% | Skill B triggered after Skill A completes |
| Isolated activation rate | ≤30% | Skill triggered directly, no chain followed |
| Chain completion rate | ≥80% | Chained skills successfully completed |
