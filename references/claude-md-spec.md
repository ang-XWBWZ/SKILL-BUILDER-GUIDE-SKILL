# CLAUDE.md Specification — Modular Architecture & Behavioral Constitution

> *目不能两视而明，耳不能两听而聪。* ——《荀子·劝学》
> A good guide for the agent is worth more than ten thousand lines of code.

> **Load when**: Phase 3 GENERATE — generating CLAUDE.md. Meta-skill reference, for the generating agent.
>
> CLAUDE.md serves two roles: (1) **behavior shaping** — how the agent treats the user; (2) **quick reference** — high-frequency project data, avoiding repeated L0 lookups.

---

## 1. Architecture: Fixed Skeleton + Optional Modules

```
CLAUDE.md (target 800-1500 tokens)
│
├── [Fixed] A. Project Identity       1-2 lines
├── [Fixed] B. Behavioral Constitution 7 rules
├── [Fixed] C. Skill Routing           Generated skill index
├── [Fixed] D. Quick Commands          build / run / test
│
├── [Default] M1. Tech Stack           Versions (from SCAN, always on)
├── [Optional] M2. Key Directories      5-10 dirs and their purposes
├── [Optional] M3. Architecture Overview Layer/data flow, 3-6 lines
├── [Optional] M4. Coding Constraints    Non-obvious rules
├── [Default] M5. Domain Glossary        Project-specific terms, always on
└── [Optional] M6. External Dependencies Upstream APIs / services / DBs
```

---

## 2. Fixed Skeleton Definition

### A. Project Identity

`# {project-name}` + one-line description: project type, core tech. No history, no team.

### B. Behavioral Constitution

Seven behavioral rules. Rules 1-4 from [Andrej Karpathy's observations on LLM coding pitfalls](https://x.com/karpathy/status/2015883857489522876); rules 5-7 are project behavioral norms:

| # | Rule | Meaning |
|---|------|---------|
| 1 | **Think Before Coding** | State assumptions explicitly. If uncertain, ask. If multiple interpretations exist, list them. If something is unclear, stop and name the confusion. |
| 2 | **Simplicity First** | Minimum code to solve the problem. No speculative features, no single-use abstractions, no error handling for impossible scenarios. |
| 3 | **Surgical Changes** | Touch only what you must. Match existing style. Remove only orphans your changes created. Every changed line traces to the user's request. |
| 4 | **Goal-Driven Execution** | Transform tasks into verifiable goals. "Fix the bug" → "Write a test that reproduces it, then make it pass." Multi-step tasks: state plan with verify checkpoints. |
| 5 | **Discover → Report** | Found something unexpected? Report it immediately. Don't silently skip or work around. |
| 6 | **Change → Test** | Changed code? Verify it. No bare modifications without running tests or checks. |
| 7 | **Complete → Archive** | Work done? Offer a change report. Don't leave dangling context for future sessions. |

These are cross-skill default behaviors. Every project's generated CLAUDE.md must include all 7 rules + the L0 Delegation rule. If the project has additional preferences, append one more (total ≤10 rules).

### C. Skill Routing

Auto-loaded skill table, populated from the ANALYZE skill plan. L0 skills annotated with `[delegate to Haiku]`.

Append the global skills awareness block at the end (≤100 words):

```markdown
### Global Skills

Project skills take priority, but don't forget globally installed skills (`~/.claude/skills/`).
Use `/skills` to list all available skills. Don't reimplement what a global skill already does.
```

### D. Quick Commands

Extracted from SCAN data: `package.json` scripts / `Makefile` targets / `pom.xml` plugins. Each command must be copy-paste executable, no placeholders. Delete rows with no corresponding item.

---

## 3. Optional Module Definitions

### M1. Tech Stack

**Default on**. Data already available from SCAN.

| Category | Technology | Version |

Version numbers require 100% accuracy (V3 semantic validation). Add/remove rows as needed.

### M2. Key Directories

**Trigger**: ≥3 top-level modules or ≥50 source files.

| Directory | Purpose |

5-10 directories, max 3 levels deep. Directory names extracted from SCAN directory tree.

### M3. Architecture Overview

**Trigger**: Complex projects (full-stack, microservices, multi-module).

Describe layering/data flow in prose, 3-6 lines. No ASCII art. Highlight non-standard design decisions.

### M4. Coding Constraints

**Trigger**: Non-obvious rules exist (naming exceptions, forbidden patterns, mandatory encapsulation layers, legacy compatibility requirements).

Each entry is a non-standard pattern discovered during SCAN or explicitly stated by the user. Generic conventions don't go here (those go in the dev skill).

### M5. Domain Glossary

**Default on for all projects**. 0-5 terms → mark "basic vocabulary, needs supplement"; ≥5 terms → mark "core vocabulary".

| Term | Meaning | Avoid |
|------|--------|-------|

List only project-specific terms. Generic technical terms don't belong here.

### M6. External Dependencies

**Trigger**: ≥3 external service/API dependencies.

| Dependency | Purpose | Config Location |

Config locations must point to files that actually exist in the project.

---

## 4. Module Selection Matrix (ANALYZE Phase Decision)

| Project Profile | Criteria | Enable Modules |
|---------|---------|---------|
| All projects | — | A, B, C, D, **M1**, **M5** |
| Medium project | ≥3 modules or ≥50 source files | + M2 |
| Complex backend / full-stack | Multi-module + multi-datasource | + M3 |
| Non-standard conventions | SCAN finds non-standard patterns | + M4 |
| Integration-heavy | ≥3 external dependencies | + M6 (stacks with M3) |

During ANALYZE, output module selection alongside the skill plan:

```
claude_md_modules: ["M1", "M2"]  // as needed
```

---

## 5. Data Source Mapping

Every field's data comes from earlier pipeline phases — never re-collected:

| Content | Data Source |
|------|---------|
| A. Project Identity | ANALYZE phase project analysis |
| B. Behavioral Constitution | Fixed template (7 rules) + user customization |
| C. Skill Routing | ANALYZE skill plan output |
| D. Quick Commands | SCAN — package.json / Makefile / pom.xml |
| M1. Tech Stack | SCAN — dependency config |
| M2. Key Directories | SCAN — directory tree |
| M3. Architecture Overview | SCAN — layer identification |
| M4. Coding Constraints | SCAN — compatibility patterns + user docs |
| M5. Domain Glossary | SCAN — code comments / documentation |
| M6. External Dependencies | SCAN — integration layer |

---

## 6. Validation Checklist (VALIDATE Phase)

- [ ] D. Quick Commands: every command copy-paste executable (no placeholders)
- [ ] C. Skill Routing: one-to-one match with generated skills
- [ ] M1. Version numbers: 100% match with SCAN results
- [ ] M2. Directory paths: exist in the project
- [ ] M6. Config location paths: exist
- [ ] Total tokens ≤1500
- [ ] Zero `{placeholder}` remnants
