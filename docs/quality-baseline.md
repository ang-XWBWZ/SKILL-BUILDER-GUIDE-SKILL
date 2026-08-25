# Quality Baseline

Use this baseline when reviewing the guide or a generated project skill library.

## Portable convention

- Portable source uses `AGENTS.md` and `.agents/skills/`.
- Each generated skill uses `SKILL.md`, and its directory aligns with its `name`.
- Portable frontmatter contains only `name` and `description`.
- Relative links resolve, and production skills contain no unresolved placeholders.
- Runtime-specific material is isolated in an optional adapter.

## Content baseline

- The guide consults for current operation, target boundary, maturity, and material constraints before scanning or generating.
- The guide consults for an existing knowledge base, delivery-record placement, reusable-knowledge capture, and the treatment of an existing AGENTS.md.
- Repeat activation preserves existing skill assets unless the user selects a specific repair, extension, migration, or replacement scope.
- Descriptions state both an outcome and concrete trigger conditions.
- Skills distinguish scope from non-goals.
- Procedures name evidence, decision points, constraints, deliverables, and verification.
- Project commands, paths, versions, and contracts are verified rather than inferred.
- Change and analysis skills with delivery outcomes report the actual result, evidence, open work or risk, and final status.
- When a project uses delivery records, closure is supported by actual verification evidence and a conclusion for plan differences, recovery, and unresolved work.
- Version control holds exact source changes; delivery records hold dates and lifecycle evidence; reusable knowledge notes are maintained separately in a selected knowledge area.
- AGENTS.md contains enough verified project map, constraints, commands, knowledge/record locations, and routing facts to start ordinary work.
- Examples contain no credentials, secrets, personal data, or attribution noise.
- Process optimization suggestions appear only after direct delivery and documentation; one verified signal may prompt a suggestion, while process change requires explicit owner approval.

## Library baseline

| Area | Expected coverage |
|---|---|
| Core project work | Conventions, orientation, feature delivery, debugging, tests |
| Boundary work | API contracts, integrations, data migrations, releases, security |
| Delivery governance | Proportionate completion reporting and traceable iteration records |
| Knowledge continuity | Selected knowledge area and evidence-backed reusable knowledge capture |
| Domain guidance | Backend, frontend, data, operations, security, multi-service |
| Maintenance | Evidence review, documentation-link checking, explicit adapter review |

## Review result format

```text
Pass:        {items proven by evidence}
Needs work:  {blocking issue or stale claim}
Uncertainty: {what cannot be verified in the current repository}
```
