# Monorepo and Multi-Service Skills

Create a monorepo or multi-service skill when local changes routinely affect package boundaries, shared contracts, build graph, deployment ownership, or multiple independently released components.

## Evidence to collect

- Workspace/package graph and ownership boundaries.
- Shared library and generated-client dependencies.
- Build, test, lint, and affected-target commands.
- Versioning, publishing, and release coupling rules.
- Cross-service contracts, environments, and compatibility windows.

## Useful skill boundaries

| Signal | Candidate skill |
|---|---|
| Contributors need to find owners and affected packages | Repository map |
| Shared packages cause broad test/release decisions | Affected-change workflow |
| Services evolve contracts independently | API contract or integration trace |
| Releases require staged compatibility | Release runbook or migration procedure |

## Done definition

The skill should turn “what else is affected?” into a reproducible evidence process, without claiming a dependency graph is complete when the tooling cannot prove it.
