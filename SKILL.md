---
name: skill-builder
description: >-
  AI Agent Skills creation methodology. Triggered when creating skill systems
  for projects, generating project-specific skills, understanding skill templates,
  model tier delegation, or validating skill accuracy. META skill — creates
  other skills as output. Deploy: copy this directory to .claude/skills/skill-builder/.
model_tier: L1
skill_tier: meta
version: 3.0.0
status: active
---

# Skill Builder — AI Agent Skills Creation Guide

> **Position**: meta tier skill. Output = new skill files (SKILL.md + openai.yaml), not business code.
>
> **Deployment**: `cp -r SKILL-BUILDER-GUIDE/ target-project/.claude/skills/skill-builder/` — then auto-loaded as `/skill-builder`.
>
> **Progressive loading**: This file is L2. Deep methodology in `references/` — loaded only when a phase or scenario triggers them (§2.7).

## Trigger Conditions

- Creating a skill system for a project
- "create skill" / "generate project-specific skill" / "skill template"
- "model tier" / "L0 delegation" / "skill validation"
- "openai.yaml" / "frontmatter spec"
- "how to decompose" / "delegation pattern"

---

## 1. Core Concepts

### 1.1 Dual-Axis Model

Every skill is defined on **two independent, orthogonal dimensions**:

| | Execution (model_tier) | Composition (skill_tier) |
|--|------|------|
| Question | Who executes? | Where in the dependency graph? |
| Values | L0 / L1 / L2 / L3 | meta / planning / functional / atomic |

**Execution**: L0=Haiku (mechanical) · L1=Sonnet (bounded) · L2=Sonnet/Opus (multi-step) · L3=Opus (architectural)

**Composition**: meta=creates skills · planning=task routing · functional=multi-step routines · atomic=single source

**Consistency**: L0+meta invalid · L0+planning invalid · L0+functional not recommended · L0+atomic valid

### 1.2 Model Tier Routing

| Tier | Cognitive Load | Model | Typical Tasks |
|:----:|---------|---------|---------|
| **L0** | Mechanical | Haiku | File lookup, info query, command exec, static tracing |
| **L1** | Bounded | Sonnet | Single-module changes, narrow search, bounded implementation |
| **L2** | Reasoning | Sonnet/Opus | Root cause diagnosis, cross-module implementation |
| **L3** | Strategic | Opus | Architectural decisions, security audits |

**Mandatory rule**: L0 tasks → Haiku. Main model executing L0 = 5-15x token waste.

| L0 Task | Example | Delegate To |
|---------|------|---------|
| File lookup | "Where is the entry file" | Haiku |
| Info query | "What framework version" | Haiku |
| Command exec | "Run deploy script" | Haiku |
| Mechanical edit | "Update version number" | Haiku |

**Upgrade triggers**: ≥2 correction rounds failed → upgrade model. Same code ≥3 modifications → stop, re-analyze. 3 rounds without narrowing → upgrade to re-diagnose.

### 1.3 Skill Type Catalog

| Skill Type | Execution | Composition | Required Sections | Template |
|---------|:--:|:--:|------|------|
| Standards (dev) | L1 | atomic | Tech stack, layered arch, code standards | `templates/example-dev/` |
| Code Map (code-map) | **L0** | atomic | Dir structure, quick lookup, routes | `templates/example-code-map/` |
| Workflow (workflow) | L1 | functional | Phase→input→steps→output, checklists | `templates/example-workflow/` |
| Change Model (change-model) | L1 | functional | WHY/WHAT/HOW/VALIDATION, call-chain check. **Implicit trigger**: at CONFIRM phase, Agent asks whether to generate a change report for the completed work. | `references/change-model.md` |
| Call-Chain (call-chain) | L1 | functional | Tracing method, type checking, final-call checklist | `templates/example-call-chain/` |
| Scripts (scripts) | L0 | atomic | Script inventory, execution flow, error handling | — |
| Delegation (delegation) | L1 | planning | Decomposition criteria, model routing | `references/delegation.md` |

### 1.4 Skill Selection

| Project Profile | Count | Combo |
|---------|:--:|---------|
| Small (bug fixes) | 2 | standards + workflow |
| Medium (new pages) | 3 | + code-map |
| Large (new modules) | 4 | + change-model |
| Complex (multi-service) | 5-6 | + call-chain + scripts + delegation |

| Scenario | Skills | Why |
|------|------|------|
| New hire onboarding | code-map + workflow | Project navigation + dev steps |
| Daily development | dev + code-map | Check conventions, locate files |
| Change release | change-model + call-chain | Structured report + chain verification |
| Issue investigation | call-chain + dev | Trace data flow, check conventions |

| Project Profile | Recommended Combo |
|---------|-------------|
| Simple frontend | dev + workflow |
| Complex frontend | dev + code-map + workflow |
| Simple backend | dev + workflow + scripts |
| Complex backend | dev + workflow + scripts + call-chain |
| Full-stack | dev + code-map + workflow + change-model + delegation |
| Microservices | dev + workflow + call-chain + change-model + delegation |

---

## 2. Execution Pipeline

The pipeline operates on an **Execution Tree** — the unified model that combines task decomposition (H-ADMC), execution assignment (delegation), and context loading (progressive disclosure). Each pipeline phase maps to a tree lifecycle stage: ANALYZE builds the root → SCAN fills the leaves → GENERATE produces output nodes → VALIDATE verifies → CONFIRM closes. Full specification: `references/execution-tree.md`.

### 2.1 Pipeline Overview

```
ANALYZE (L1) → SCAN (L0) → GENERATE (L1) → VALIDATE (L0) → CONFIRM (L1)
    │              │              │                │               │
  Skill plan   Code samples   Skill files    Validation     approved/revise
```

| Phase | Executor | Input | Output | Gate |
|------|:------:|------|------|------|
| ANALYZE | Sonnet (L1) | Project overview | Skill plan: `[{name, tier, reason}]` | **Pause for user confirmation** |
| SCAN | **Haiku (L0)** | Skill plan → codebase | Code samples per layer | All layers scanned |
| GENERATE | Sonnet (L1) | Scan results | SKILL.md + openai.yaml + references/ | 8 hard rules met |
| VALIDATE | **Haiku (L0)** | Generated files | Pass/Fail report | V1+V2 passed |
| CONFIRM | Sonnet (L1) | Validated skills | approved / revise / reject | User explicit response |

### 2.2 ANALYZE — Project Analysis

- **Executor**: Sonnet (L1). Analyze project type, tech stack, module structure, team size.
- **Output**: Skill plan in `[{name, skill_tier, model_tier, reason}]` format.
- **Gate**: Pause for user confirmation. Do NOT proceed to SCAN without approval.
- **Reference**: `references/pipeline/phase-0-example.md` — granularity benchmark (NestJS).

### 2.3 SCAN — Code Scanning

- **Executor**: Haiku (L0) — **must delegate**. Main model dispatches Haiku sub-agents; does NOT execute scan directly.
- **Output**: Code samples per layer with pattern identification.

| Layer | Scan Target | Record |
|------|---------|--------|
| API Layer | Route declarations, param validation, response wrapping | `{method}`, `{class/function name}` |
| Service Layer | Abstract interfaces, consistency management, param conversion | `{yes/no}`, `{method}` |
| Data Layer | ORM approach, query organization, pagination | `{framework}`, `{method}` |
| Integration Layer | Remote calls, message queues, scheduled tasks | `{list}`, `{config}` |
| Existing Conventions | Project's existing README, CHANGELOG, CONTRIBUTING, docs/, change logs | Document paths, format, and naming — generated skills must incorporate or explicitly replace these |
| Reusable Workflows | Repeated operations: build, deploy, test suites, data migration, code generation | Shell scripts, npm scripts, Makefile targets — evaluate for scripts/ skill or workflow automation |

- **Reference**: `references/pipeline/phase-2-scan.md` — project type → layer mapping.
- **Gate**: ☐ All scan sub-tasks dispatched to Haiku? ☐ Existing project conventions/documents detected? ☐ Reusable scripts/workflows identified?

### 2.4 GENERATE — Create Skill Files

- **Executor**: Sonnet (L1).
- **Output**: SKILL.md + openai.yaml → `.claude/skills/{name}/` (production) or `skills/{name}/` (template).

**Hard rules**:
1. Frontmatter: name, description, model_tier, skill_tier, version, status (`references/frontmatter-spec.md`)
2. Trigger words from project code: 5-15, action + query types
3. Actual version numbers from scan — no placeholders
4. Scanned code snippets, sanitized (IPs/passwords → `{placeholder}`)
5. Cross-reference related skills with relative paths
6. SKILL.md body ≤5000 tokens
7. Progressive loading: functional-tier skills (workflow, change-model, call-chain) MUST create `references/` for content exceeding the L2 body budget. If the skill body approaches 5000t, split detailed templates/methodologies into `references/`. Atomic-tier skills (dev, code-map, scripts) may omit references/ if the lookup table fits in the body.
8. Load methodology for the skill type: when generating a skill of type X, load the corresponding L3 reference first (`references/change-model.md` for change-model skills, `references/execution-tree.md` for delegation skills). The generated skill must reflect the current naming conventions and patterns from its reference.
9. Completeness checklist: before delivering generated skills, verify all items in §2.4.1.

**Language**: Concise English. Trigger words match project language.
**Reference**: `references/pipeline/phase-3-generate.md` — per-skill-type generation prompts.

**Naming disambiguation**: Risk levels in change-model skills use R0-R3 (not L0-L3, which are execution tiers). See `references/change-model.md` §3.2.

**Gate**: ☐ All 9 hard rules passed? ☐ Completeness checklist (§2.4.1) all ✅?

#### 2.4.1 Completeness Checklist

Before delivering generated skills, verify every item:

- [ ] **Progressive loading**: functional-tier skills (workflow, change-model, call-chain) have `references/` directory if body exceeds 3000 tokens
- [ ] **Model delegation**: L0 skills body states "must delegate to Haiku"; L1 skills note which sub-tasks delegate to L0
- [ ] **Naming disambiguation**: risk levels use R0-R3 (not L0-L3); execution tiers use L0-L3
- [ ] **Existing conventions**: project's existing docs, changelogs, workflows are either incorporated or explicitly replaced (not silently ignored)
- [ ] **Cross-references**: all relative paths resolve to existing files within the target project
- [ ] **Trigger words**: 5-15 per skill, project-specific (no generic terms like "develop" or "modify")
- [ ] **No placeholders**: every `{placeholder}` replaced with actual content from scan
- [ ] **Token budget**: each SKILL.md ≤5000 tokens

### 2.5 VALIDATE — Verify

- **Executor**: Haiku (L0) — **must delegate**.

```bash
python scripts/validate-skills.py .claude/skills/{name}
python scripts/validate-skills.py skills/{name}
```

| Layer | Pass Condition |
|--------|---------|
| V1 Format | Frontmatter complete, triggers ≥5, YAML valid, no forbidden fields |
| V2 Structure | Dual-axis consistent, skill references exist, relative paths correct |
| V3 Semantic | File paths ≥95%, method names ≥90%, version numbers 100% — run with `--semantic` |

**Acceptance criteria**:

| Declaration | Verification | Pass Rate |
|---------|---------|:---:|
| File paths | Glob/Read confirm existence | ≥95% |
| Method names | Grep source confirm | ≥90% |
| Version numbers | Read dependency config | 100% |

Below standard → must not publish. Verify with tools, not by trusting documents.
**Reference**: `references/validation-protocol.md` — full protocol.
**Gate**: ☐ V1+V2 passed? ☐ V3 semantic passed (if available)? ☐ Zero broken cross-references?

### 2.6 CONFIRM — User Approval

- **Executor**: Sonnet (L1).
- **Output**: `approved` | `revise({feedback})` | `reject`.

Confirm: version numbers match scan, standard patterns correct, user docs merged (user docs take precedence over scan). On revise: apply feedback, re-submit (max 2 rounds, then escalate).

**Gate**: ☐ User explicit response received? ☐ If this pipeline execution modified the project, change report offered to user? (Agent asks: "Generate a change report for this session?" — see `references/change-model.md`) ☐ Reusable workflows identified during SCAN offered for script/template archival?

### 2.7 L3 Routing Table

Load deeper methodology only when the corresponding phase or scenario triggers it:

| Scenario / Phase | Load | Content |
|------|------|------|
| Phase 1 ANALYZE | `references/pipeline/phase-0-example.md` | NestJS end-to-end example |
| Phase 2 SCAN | `references/pipeline/phase-2-scan.md` | Project type → layer mapping |
| Phase 3 GENERATE | `references/pipeline/phase-3-generate.md` | Per-skill-type generation prompts |
| Phase 4 VALIDATE | `references/validation-protocol.md` | V1/V2/V3 specs, pass rates |
| Filling frontmatter | `references/frontmatter-spec.md` | Required/forbidden/removed fields |
| Task decomposition, execution tree, delegation patterns | `references/execution-tree.md` | H-ADMC criteria, AND/OR/LEAF nodes, patterns A/B/C, C/B/U format |
| Change reports, archiving | `references/change-model.md` | 4-layer architecture, 8-item checklist, R0-R3 risk levels |

### 2.8 Deep Review (Optional Phase 6)

After CONFIRM, the user may request an independent quality evaluation of generated skills. This spawns a fresh agent in worktree isolation that evaluates: practical value, over-design, logical conflicts, development guidance, engineering stability. See `docs/evaluation-report-*.md` for evaluation rubric.

Trigger: user says "review the generated skills" / "evaluate the skill system" / "深度复核".

---

## 3. Deployment

### 3.1 Directory Structure

```
{skill-name}/
├── SKILL.md              # L2: Core body (≤5000 tokens)
├── agents/
│   └── openai.yaml       # L1: Trigger config (5-15 triggers)
├── references/           # L3: Deep reference, on demand
├── scripts/              # L4: Executables (zero context)
└── assets/               # Static resources
```

| Path | Use Case | Auto-Load |
|------|---------|:---:|
| `.claude/skills/{name}/` | Production project skills | ✅ |
| `skills/{name}/` | Template/methodology projects | ❌ |
| `~/.claude/skills/{name}/` | Global cross-project skills | ✅ |

Naming: `{project}-{type}`, lowercase, hyphen-separated. Dir name = skill name.

### 3.2 CLAUDE.md Integration

**Version A: `.claude/skills/` (Recommended — Auto-Load)**

```markdown
# {Project}
## Mandatory Delegation Rules
Main model must not execute L0 tasks. File ops → Haiku.

## Skills
> Auto-loaded from `.claude/skills/`, supports `/skill-name`.
| Skill | Execution | Composition | Purpose |
|------|:------:|:------:|------|
| {project}-dev | L1 | atomic | Tech stack, standards |
| {project}-code-map | **L0** | atomic | File location [Haiku] |
```

Routing table optional — skills auto-load. Include for documentation.

**Version B: `skills/` (Explicit Routing Required)**

```markdown
## Skill Routing Table (Required)
| Skill | Execution | Composition | Trigger |
|------|:------:|:------:|------|
| [dev](skills/{project}-dev/) | L1 | atomic | Tech stack, code standards |
```

### 3.3 Conflict Resolution

When multiple skill triggers overlap:

| Priority | Rule | Example |
|:--:|------|------|
| 1 | Project-specific > generic | `myproject-dev` over `example-dev` |
| 2 | Required > recommended | Explicit directive over suggestion |
| 3 | Exact match > broad match | "file location" → code-map, not dev |
| 4 | Active > deprecated | Skip superseded/deprecated skills |

---

## 4. Reference

### 4.1 Templates Index

| Template | Path |
|------|------|
| Standards (dev) | `templates/example-dev/` |
| Code Map (code-map) | `templates/example-code-map/` |
| Workflow (workflow) | `templates/example-workflow/` |
| Call-Chain (call-chain) | `templates/example-call-chain/` |
| Delegation (delegation) | `templates/example-delegation/` |
| SKILL.md skeleton | `templates/skill-template.md` |
| openai.yaml skeleton | `templates/openai-template.yaml` |
| Change report | `templates/change-model-template.md` |

Each template is a complete mini-skill (SKILL.md + openai.yaml + references/). Copy to `.claude/skills/` and customize.

### 4.2 Import Steps

```
① Analyze project (type, tech stack, team size) → ② Gap analysis (quick-select table in §1.4) → ③ Generate to `.claude/skills/` → ④ Validate + iterate
```

### 4.3 Conventions

**Versioning**: SemVer. Commit format: `feat|fix|docs(skills): {description}`.

**Security**: Sanitize code examples (secrets → `{placeholder}`). No reference skill may contain real project secrets. No agent signatures or promotional links in generated files.

**Maintenance**: Update skills on tech stack change, new module, workflow optimization, systematic errors. Validate after each change.

**Lifecycle**: `draft → active → deprecated → (removed)` or `superseded → replacement`.
