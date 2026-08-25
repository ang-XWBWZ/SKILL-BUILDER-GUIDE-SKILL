# Backend API Skills

Create a backend-specific skill when agents repeatedly need to preserve a service boundary, not merely when the repository contains a backend.

## Good candidates

| Repeated concern | Skill boundary | Evidence to collect |
|---|---|---|
| New or changed endpoints | API contract | OpenAPI/schema source, route declarations, consumers, contract tests |
| Cross-layer behavior | Integration trace | Entry handler, service/use case, persistence/client, error path |
| Background workers or events | Event workflow | Producer, schema, consumer, retry/idempotency behavior |
| Operational behavior | Release runbook | Health checks, dashboard/query, rollback commands, on-call rule |

## Authoring notes

- Use the project’s real layer names; do not assume controller/service/repository architecture.
- Document defaults, validation, error semantics, authorization, and idempotency when they affect callers.
- Separate internal implementation patterns from supported external contract rules.
- Put endpoint inventories and large schemas in `references/`, not the primary skill body.

## Done definition

The generated skill should let an agent identify the authoritative contract, affected consumers, compatible change path, and concrete verification without guessing framework behavior.
