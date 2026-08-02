# Phase 0 — Project Analysis Example

Use this phase to choose a minimal skill set from verified project signals.

## Example project profile

- A TypeScript service with a web API, persistent storage, and automated tests.
- Several modules maintained by more than one contributor.
- Existing build and test commands in the package manifest.
- A public API consumed by another application.

## Evidence-backed plan

```text
Candidate: project-context
Why: contributors repeatedly need locations for modules, tests, and commands.

Candidate: project-feature-delivery
Why: changes repeat the same implementation and verification loop.

Candidate: project-api-contract
Why: the service exposes a supported interface to another application.

Deferred: project-data-migration
Why: persistent schema changes are not yet recurring; add it when the first migration needs a rehearsed procedure.
```

## Required output

For each candidate, record:

| Field | Example evidence |
|---|---|
| Trigger | Public endpoint, versioned schema, or recurring repository question |
| Inputs | Manifest, source paths, existing tests, owner rules |
| Output | Map, verified change, contract record, or runbook |
| Verification | Commands, links, tests, or review gate |
| Non-goals | Nearby work owned by a different skill |

Ask the project owner to confirm additions that materially change workflow, authority, or maintenance burden.
