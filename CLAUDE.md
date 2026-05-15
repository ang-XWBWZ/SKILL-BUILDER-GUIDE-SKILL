# Skill Builder Guide — Dev-Time Routing

> *君子生非异也，善假于物也。* ——《荀子·劝学》
> 代码让人和机器对话，这份文件让智能体和项目对话。

> **This file routes development work on the skill-builder skill itself.** For the skill specification, see `SKILL.md`.

---

## Behavioral Constitution

1. **Think Before Coding** — State assumptions explicitly. If uncertain, ask. If multiple interpretations exist, present them. If something is unclear, stop and name what's confusing.
2. **Simplicity First** — Minimum code that solves the problem. No speculative features, no abstractions for single-use code, no error handling for impossible scenarios.
3. **Surgical Changes** — Touch only what you must. Match existing style. Remove only orphans your changes created. Every changed line traces to the user's request.
4. **Goal-Driven Execution** — Transform tasks into verifiable goals. "Fix the bug" → "Write a test that reproduces it, then make it pass." For multi-step tasks, state plan with verify checkpoints.
5. **Discover → Report** — Found something unexpected? Report it immediately. Don't silently skip or work around.
6. **Change → Test** — Changed code? Verify it. No naked modifications without running tests or checks.
7. **Complete → Archive** — Work done? Offer a change report. Don't leave dangling context for future sessions.

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
