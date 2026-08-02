# Quality Baseline

Use this baseline when reviewing the guide or a generated project skill library.

## Structural baseline

- Portable source uses `AGENTS.md` and `.agents/skills/`.
- Each generated skill has a valid `SKILL.md` whose directory matches its `name`.
- Portable frontmatter contains only `name` and `description`.
- Relative links resolve, and production skills contain no unresolved placeholders.
- Runtime-specific material is isolated in an optional adapter.

## Content baseline

- Descriptions state both an outcome and concrete trigger conditions.
- Skills distinguish scope from non-goals.
- Procedures name evidence, decision points, constraints, deliverables, and verification.
- Project commands, paths, versions, and contracts are verified rather than inferred.
- Examples contain no credentials, secrets, personal data, or attribution noise.
- Process optimization suggestions appear only after direct delivery and documentation; one verified signal may prompt a suggestion, while process change requires explicit owner approval.

## Library baseline

| Area | Expected coverage |
|---|---|
| Core project work | Conventions, orientation, feature delivery, debugging, tests |
| Boundary work | API contracts, integrations, data migrations, releases, security |
| Domain guidance | Backend, frontend, data, operations, security, multi-service |
| Maintenance | Structure validation, health signals, explicit adapter review |

## Review result format

```text
Pass:        {items proven by evidence}
Needs work:  {blocking issue or stale claim}
Uncertainty: {what cannot be verified in the current repository}
```
