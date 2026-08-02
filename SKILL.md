---
name: skill-builder
description: Create, repair, and expand portable project-specific agent skills. Use when designing a project skill system, migrating vendor-specific agent instructions, choosing skill boundaries, authoring AGENTS.md and .agents/skills content, adding domain guides or examples, or validating a skill library.
---

# Skill Builder

Create a small, evidence-based skill system that works as a project artifact before it is adapted for any particular agent runtime.

## Scope

Use this skill to design, migrate, validate, or expand project-specific skills. Do not use it to manufacture a broad runtime integration claim or to replace project-owner decisions about authority, policy, or irreversible operations.

## Canonical output

Treat the following as the portable source of truth:

```text
{project}/
├── AGENTS.md
└── .agents/
    ├── skills/
    │   └── {project}-{capability}/
    │       ├── SKILL.md
    │       ├── references/       # load only when needed
    │       ├── scripts/          # deterministic helpers, when justified
    │       └── assets/           # reusable output assets, when justified
    └── adapters/                 # optional runtime-specific installation notes/config
```

`AGENTS.md` is the short project entry point. `.agents/skills/` contains the durable, portable instructions. An adapter may copy, link, or translate those files for a runtime, but it must not become the only source of project knowledge.

Do not promise automatic discovery, slash commands, model names, or tool syntax unless the target runtime is known and its adapter documents the behavior.

## Procedure

### 1. Establish the need

Inspect the repository, existing instructions, build commands, and user-provided conventions. Identify recurring work that benefits from project facts or a repeatable procedure. Avoid creating a skill for a one-off request or for knowledge already available from the runtime.

Use [the decision guide](references/decision-guide.md) to select a small initial set. Start with project context and add specialized skills only when their inputs, outputs, and boundaries are clear.

### 2. Build an evidence pack

Collect only information that can be verified:

- Project purpose, technology, commands, and directories.
- Representative source patterns and existing human conventions.
- Interfaces, data boundaries, deployment constraints, and tests that affect the target task.
- Gaps or conflicting sources, marked as uncertainty rather than guessed facts.

Use [work decomposition](references/work-decomposition.md) for parallel or multi-step investigations. Match work to available capabilities such as inspection, implementation, review, or external coordination; never hard-code a vendor model tier.

### 3. Author the portable core

Keep `SKILL.md` concise and imperative. Its frontmatter contains only `name` and `description`; put runtime-specific metadata in an adapter. The description must say both what the skill does and the situations that should trigger it.

For every project skill, include only the sections that help an agent act correctly:

1. Scope and non-goals.
2. Required project facts or inputs.
3. Ordered procedure with decision points.
4. Evidence and safety constraints.
5. Deliverable and verification criteria.
6. Optional handoff to another project skill when a measurable condition is met.

Move large schemas, domain rules, and worked examples into `references/`. Add a script only when a deterministic operation would otherwise be repeatedly reimplemented. Use [the frontmatter specification](references/frontmatter-spec.md) and [the validation protocol](references/validation-protocol.md).

### 4. Write the shared entry point

Generate `AGENTS.md` from verified project facts. Keep it a router, not a second skill library. Include project identity, non-negotiable constraints, executable commands, and a compact skill map. Use [the AGENTS.md specification](references/agents-md-spec.md).

Do not duplicate full procedures from `.agents/skills/` into `AGENTS.md`. Point to the canonical skill instead.

### 5. Add adapters last

Keep adapter material under `.agents/adapters/` and make the installation step explicit. Adapters may contain runtime-specific paths, UI metadata, or invocation syntax, but may not rewrite portable project rules without documenting the divergence. Follow [the adapter contract](references/adapter-contract.md).

### 6. Validate and confirm

Run the repository validator against either a single skill or the `.agents/skills/` directory. Verify links, frontmatter, names, placeholders, and the project layout. For claims about source paths, versions, APIs, or commands, verify against the target repository rather than trusting generated prose.

```bash
python scripts/validate-skills.py .agents/skills --project-root .
python scripts/check-skill-health.py .agents/skills
```

Use `--allow-placeholders` only for reusable templates. Before delivery, state what was generated, what evidence supports it, and any unresolved uncertainty.

## Architecture rules

- Keep one canonical source: `.agents/skills/`.
- Separate universal behavior, project facts, and runtime adapters.
- Prefer a few focused skills over a graph of overlapping instructions.
- Treat risk as a property of the action and evidence, not of a model label.
- Preserve existing project conventions unless the user explicitly asks to replace them.
- Keep local references one hop from `SKILL.md`; repair every relative link after moves.
- Never insert agent attribution, promotional links, or invented ownership metadata.

## Reference map

| Need | Read |
|---|---|
| Choose an initial skill set | [decision guide](references/decision-guide.md) |
| Shape the root instruction file | [AGENTS.md specification](references/agents-md-spec.md) |
| Define portable frontmatter | [frontmatter specification](references/frontmatter-spec.md) |
| Split work and preserve evidence | [work decomposition](references/work-decomposition.md) |
| Compose related skills without duplication | [skill composition](references/skill-chain.md) |
| Make a platform adaptation | [adapter contract](references/adapter-contract.md) |
| Validate structure and claims | [validation protocol](references/validation-protocol.md) |
| Build a domain-specific skill | [scenario guides](references/scenarios/) |

## Templates and examples

Start from [the portable skill skeleton](templates/skill-template.md) and [the AGENTS.md skeleton](templates/agents-md-template.md). Use the focused examples in `templates/` only after selecting a real need; they are patterns to adapt, not a mandatory bundle.

## Handoff

Recommend a follow-up only when the current work exposes a measurable need: for example, add an API-contract skill when the project publishes a versioned interface, or a migration skill when a change modifies persistent data. Otherwise, finish with the verified result instead of creating unnecessary skills.

## Verification

- [ ] Validate generated project skills with the portable validator and project-layout check.
- [ ] Verify project facts against repository evidence before publishing.
- [ ] Confirm any runtime adapter in its target environment before claiming discovery or installation behavior.
