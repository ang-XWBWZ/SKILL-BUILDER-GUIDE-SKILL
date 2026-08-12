---
name: skill-builder
description: Create, repair, and expand portable project-specific agent skills. Use when designing a project skill system, migrating vendor-specific agent instructions, choosing skill boundaries, authoring AGENTS.md and .agents/skills content, adding domain guides or examples, or reviewing a skill library.
---

# Skill Builder

Create a small, evidence-based skill system that works as a project artifact before it is adapted for any particular agent runtime.

## Scope

Use this skill to design, migrate, review, or expand project-specific skills. Do not use it to manufacture a broad runtime integration claim or to replace project-owner decisions about authority, policy, or irreversible operations.

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

## Delivery order

Keep direct work ahead of process improvement: complete the single request, land and verify its implementation when applicable, and update required documentation before offering an optional process optimization suggestion. One verified friction signal is enough to suggest a small improvement, but never enough to change a project process without explicit authorization. See [the process-optimization guide](references/process-optimization.md).

## Procedure

### 0. Consult and confirm

At each initial or repeat activation, establish the user’s current operation before beginning an evidence scan, generation, copy, or overwrite. Read only enough existing project context to know whether a canonical skill system already exists; that orientation is not permission to generate.

If the user has not made the current operation clear, ask what they want to do now. Confirm the target boundary, desired maturity, and constraints that materially change scope, authority, compatibility, or acceptance. Ask whether a usable knowledge base exists, whether delivery records and reusable knowledge notes belong there, and what documentation destination to use if it does not. When the request already provides those facts, summarize the intent and proceed without redundant questions.

When AGENTS.md exists, assess it before drafting another one and ask whether to preserve, augment, merge, migrate, replace, or only assess it. Treat a repeat activation as a possible assessment, repair, extension, migration, review, or plan-only request. Preserve existing assets by default; do not regenerate or replace them solely because the builder was invoked again. Follow [the consultation protocol](references/consultation-protocol.md).

### 1. Establish the need

Inspect the repository, existing instructions, build commands, and user-provided conventions. Identify recurring work that benefits from project facts or a repeatable procedure. Avoid creating a skill for a one-off request or for knowledge already available from the runtime.

Use [the decision guide](references/decision-guide.md) to select a small initial set. Start with project context and add specialized skills only when their inputs, outputs, and boundaries are clear.

When recurring project work needs traceable scope, implementation, verification, and closure, select an iteration-management skill and read [traceable delivery guidance](references/iteration-management.md). Keep a full delivery record proportional to the work; do not impose it on a simple answer or low-risk edit without a project requirement.

### 2. Build an evidence pack

Collect only information that can be verified:

- Project purpose, technology, commands, and directories.
- Representative source patterns and existing human conventions.
- Interfaces, data boundaries, deployment constraints, and tests that affect the target task.
- Gaps or conflicting sources, marked as uncertainty rather than guessed facts.
- Existing project conventions for change records, delivery reports, approvals, retention, and recovery when the target work needs a traceable lifecycle.
- Existing documentation and knowledge-base locations, organization, access boundaries, refresh sources, and rules for delivery-record placement or knowledge capture.

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
7. A completion-report format when the skill produces a change, decision, or handoff.

For a change or analysis skill that has a delivery outcome, require the final report to state the result, actual changes or decision, acceptance and verification evidence, open work or uncertainty, and final status. When the project needs a full lifecycle record, create an iteration-management skill from [the focused example](templates/example-iteration-management/SKILL.md) and adapt the [delivery-record template](templates/iteration-record-template.md) to the project’s documented policy.

Move large schemas, domain rules, and worked examples into `references/`. Add a script only when a deterministic operation would otherwise be repeatedly reimplemented. Use [the frontmatter specification](references/frontmatter-spec.md) and [the evidence-review guide](references/evidence-review.md).

### 4. Write the shared entry point

Generate or augment `AGENTS.md` from verified project facts. Make it sufficient for an agent to begin ordinary work without rediscovering project identity, key locations, hard constraints, executable commands, knowledge and delivery-record locations, and the compact skill map. Keep it a router and high-frequency project guide, not a second skill library. Use [the AGENTS.md specification](references/agents-md-spec.md).

When an AGENTS.md already exists, preserve valid content and use the user-selected treatment: assess, augment, merge, migrate runtime-bound material, or explicitly replace exact targets. Do not create a competing entry point or overwrite it by default. Do not duplicate full procedures from `.agents/skills/` into `AGENTS.md`. Point to the canonical skill instead.

### 5. Add adapters last

Keep adapter material under `.agents/adapters/` and make the installation step explicit. Adapters may contain runtime-specific paths, UI metadata, or invocation syntax, but may not rewrite portable project rules without documenting the divergence. Follow [the adapter contract](references/adapter-contract.md).

### 6. Review evidence and confirm

Review generated instructions in the target project instead of applying a fixed structural gate. Confirm that the trigger, scope, project facts, procedure, evidence sources, and completion expectation are useful for the intended work. Check source paths, versions, APIs, commands, and actual outcomes against project evidence rather than trusting generated prose.

Use the local Markdown link checker after documentation changes when it is available in the guide repository:

```bash
python scripts/check-markdown-links.py .
```

It detects broken local documentation links only. Before delivery, update required documentation and state what was generated, what evidence supports it, and any unresolved uncertainty. Follow [the evidence-review guide](references/evidence-review.md).

For a completed delivery, report the actual result rather than a claimed completion: identify changes or the analysis decision, acceptance and verification evidence, open work or risk, and one final status. A full delivery record may be closed only when the project’s evidence and recovery gates are satisfied.

Use version control as the precise record of source change, a dated delivery record as the lifecycle record, and a separately managed knowledge note only for durable reusable conclusions. Follow [knowledge management guidance](references/knowledge-management.md).

### 7. Offer an optional process optimization suggestion

Only after the direct request, its implementation, and required documentation are complete, inspect the current delivery for a verified friction signal. At the low suggestion threshold of one signal, offer at most one concise recommendation. Do not create a task, skill, automation, or process change until the user or project owner explicitly authorizes it; use [the process-optimization guide](references/process-optimization.md) for the threshold and output format.

## Architecture rules

- Keep one canonical source: `.agents/skills/`.
- Separate universal behavior, project facts, and runtime adapters.
- Treat builder activation as a request for consultation, not automatic authorization to generate or overwrite.
- Keep exact version-control change history, dated delivery records, and reusable knowledge notes in their distinct project-defined locations.
- Prefer a few focused skills over a graph of overlapping instructions.
- Treat risk as a property of the action and evidence, not of a model label.
- Preserve existing project conventions unless the user explicitly asks to replace them.
- Keep process optimization suggestions post-delivery, evidence-based, and non-blocking.
- Keep local references one hop from `SKILL.md`; repair every relative link after moves.
- Never insert agent attribution, promotional links, or invented ownership metadata.

## Reference map

| Need | Read |
|---|---|
| Establish current user intent before scanning or generating | [consultation protocol](references/consultation-protocol.md) |
| Choose and maintain a project knowledge area | [knowledge-management guide](references/knowledge-management.md) |
| Choose an initial skill set | [decision guide](references/decision-guide.md) |
| Shape the root instruction file | [AGENTS.md specification](references/agents-md-spec.md) |
| Define portable frontmatter | [frontmatter specification](references/frontmatter-spec.md) |
| Split work and preserve evidence | [work decomposition](references/work-decomposition.md) |
| Compose related skills without duplication | [skill composition](references/skill-chain.md) |
| Make a platform adaptation | [adapter contract](references/adapter-contract.md) |
| Review intent, facts, and delivery evidence | [evidence-review guide](references/evidence-review.md) |
| Offer a low-threshold post-delivery improvement | [process-optimization guide](references/process-optimization.md) |
| Plan and close a traceable delivery | [iteration-management guide](references/iteration-management.md) |
| Build a domain-specific skill | [scenario guides](references/scenarios/) |

## Templates and examples

Start from [the portable skill skeleton](templates/skill-template.md) and [the AGENTS.md skeleton](templates/agents-md-template.md). Use the focused examples in `templates/` only after selecting a real need; they are patterns to adapt, not a mandatory bundle.

Use [the delivery-record template](templates/iteration-record-template.md) only for project work that needs a durable lifecycle record. Keep its naming, location, ownership, retention, and approval rules project-specific.

Use [the knowledge-note template](templates/knowledge-note-template.md) only when the project has selected a knowledge destination and a conclusion is reusable beyond its delivery.

## Handoff

Recommend a follow-up only when the current work exposes a measurable need: for example, add an API-contract skill when the project publishes a versioned interface, or a migration skill when a change modifies persistent data. A low-threshold process suggestion belongs after the direct delivery and is suggestion-only until explicitly approved. Otherwise, finish with the verified result instead of creating unnecessary skills.

## Verification

- [ ] Confirm the current operation, target boundary, maturity, and material constraints before generation.
- [ ] Confirm the knowledge destination, delivery-record placement, and knowledge-capture disposition before generating documentation that depends on them.
- [ ] Assess an existing AGENTS.md and apply only the user-selected preserve, augment, merge, migrate, or replacement scope.
- [ ] On repeat activation, preserve existing assets unless the user explicitly selects repair, extension, migration, or replacement scope.
- [ ] Review generated project skills against the current user intent and target-project evidence.
- [ ] Verify project facts against repository evidence before publishing.
- [ ] Confirm any runtime adapter in its target environment before claiming discovery or installation behavior.
- [ ] For a delivery outcome, report actual changes or decision, verification evidence, open work or risk, and final status.
- [ ] For a formal delivery record, verify its closure gate and sensitive-data review before marking it closed.
- [ ] Link exact code changes to version control and capture reusable knowledge separately only when the selected project policy requires it.
- [ ] If an optimization suggestion is included, confirm that delivery came first and that its single signal is documented.
