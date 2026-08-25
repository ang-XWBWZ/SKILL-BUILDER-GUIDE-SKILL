# Convention Evidence Guide

Use this reference while filling a project-conventions skill. Gather evidence before describing a pattern as a standard.

## Scan sequence

1. Read root documentation, active manifests, task configuration, and existing contributor rules.
2. Sample multiple source files from each meaningful area of the project.
3. Compare tests, configuration, and integration boundaries with implementation patterns.
4. Record dominant patterns, scoped exceptions, and evidence paths separately.
5. Ask the project owner to resolve conflicts between source inference and written policy.

## Useful evidence dimensions

| Concern | Inspect | Record |
|---|---|---|
| Entry boundary | Routes, commands, handlers, job registrations | Validation, errors, response/result shape |
| Core behavior | Services, use cases, domain modules | Dependencies, state boundaries, error policy |
| Persistence | Schema, queries, repositories, migrations | Ownership, transaction/consistency rules, pagination |
| Integrations | Clients, events, schedules, queues | Contract, timeout, retry, idempotency, observability |
| Tests | Test tree and task configuration | Test style, fixtures, isolation, expected commands |

## Record format

```text
Conclusion: {observed convention or exception}
Evidence:   {two or more paths, or a written owner rule}
Uncertainty:{scope, ambiguity, or "none"}
```

Never include secrets, internal tokens, or personally identifying production data in a skill example.
