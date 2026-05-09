# Skill Builder — AI Agent Skills Creation Guide

> **Agent-Native Skill Architecture v3.0**
>
> **This project is a skill.** Deploy: `cp -r SKILL-BUILDER-GUIDE/ target/.claude/skills/skill-builder/`
>
> Primary audience: AI Agent. `SKILL.md`, `references/`, `scripts/` are agent-executable. `docs/` is human-facing.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What Is This?

A methodology for creating project-specific AI Agent Skills. Three pillars:

| # | Concept | One-Liner |
|:--:|------|--------|
| 1 | **Dual-Axis Model** | Execution (L0-L3) × Composition (meta/planning/functional/atomic) |
| 2 | **Progressive Disclosure** | L1 triggers → L2 body → L3 references on demand → L4 scripts zero-context |
| 3 | **L0 Delegation** | Mechanical tasks → Haiku (5-15x token savings) |

---

## Quick Start

```bash
# Validate this skill
python scripts/validate-skills.py .

# Validate template skills
python scripts/validate-skills.py templates/

# Health check
python scripts/check-skill-health.py .
```

> Human intro: [docs/quick-start.md](docs/quick-start.md)

---

## Structure

```
SKILL-BUILDER-GUIDE/              ← Deploy to .claude/skills/skill-builder/
├── SKILL.md                      ← L2: pipeline + methodology
├── agents/openai.yaml            ← L1: triggers
├── references/                   ← L3: deep methodology (on demand)
│   ├── delegation.md             ← H-ADMC, patterns, output standards, Plan Tree
│   ├── change-model.md           ← 4-layer architecture, call-chain, archive
│   ├── frontmatter-spec.md
│   ├── validation-protocol.md
│   ├── plan-tree-design.md
│   └── pipeline/                 ← Phase templates + examples
├── templates/                    ← Copy to other projects
├── scripts/                      ← Validation + health tools
└── docs/                         ← Human-facing
```

---

## Progressive Loading

```
L1: agents/openai.yaml            ← Always loaded (~100t)
L2: SKILL.md                      ← On trigger (~3500t)
L3: references/*.md               ← On demand (each ≤2000t)
L4: scripts/*.py                  ← Zero context execution
```

---

## License

MIT
