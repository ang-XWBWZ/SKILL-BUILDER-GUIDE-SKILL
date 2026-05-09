# Skill Builder Guide — Dev-Time Routing

> **This file routes development work on the skill-builder skill itself.** For the skill specification, see `SKILL.md`.

---

## Mandatory Rules

Main model must not execute L0 tasks. File ops, lookups, script exec → Haiku.

---

## Dev-Time References

When modifying this skill, load the relevant reference:

| Working On | Load |
|------|------|
| Pipeline spec (phases, gates, rules) | `SKILL.md` |
| Delegation methodology (H-ADMC, patterns, output standards) | `references/delegation.md` |
| Change model methodology (4-layer, call-chain, archive) | `references/change-model.md` |
| Plan Tree design | `references/plan-tree-design.md` |
| Frontmatter field specifications | `references/frontmatter-spec.md` |
| Validation protocol and acceptance criteria | `references/validation-protocol.md` |
| Pipeline phase templates and examples | `references/pipeline/` |
| Template skills (example-*) | `templates/` |
| Validation scripts | `scripts/` |

---

## Maintainer Rules (Self-Bootstrapping)

**Rule A — Consumer Before Field**: No frontmatter field added unless a tool (script, CI) consumes it. Dead fields rot into false claims.

**Rule B — Migrate Must Delete**: Content moves A→B → completely removed from A. No restatements. Links only.

**Rule C — Quarterly Structure Audit**: Check for duplicate content, broken cross-references, dead frontmatter fields. Fix or remove.

---

## Project Structure

```
SKILL-BUILDER-GUIDE/          ← This is a skill (deploy to .claude/skills/)
├── SKILL.md                  ← L2: pipeline + methodology (routing center)
├── agents/openai.yaml        ← L1: trigger config
├── references/               ← L3: deep methodology (on demand)
├── templates/                ← Copy to other projects
├── scripts/                  ← L4: validation tools
└── docs/                     ← Human-facing (quick-start, changes)
```
