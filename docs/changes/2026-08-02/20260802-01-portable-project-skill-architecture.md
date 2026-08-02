# Portable Project Skill Architecture

## WHY

- Problem: the guide treated one runtime’s directory, instruction file, metadata, and model terminology as the project-wide skill architecture.
- Desired outcome: project-specific skills can be authored once, stored in a portable canonical location, and adapted explicitly for any supported runtime.
- Constraints: preserve evidence-based guidance, avoid duplicated rules, and retain a validator that runs without third-party Python packages.

## WHAT

| Concern | Change | Risk control |
|---|---|---|
| Canonical layout | Adopt `AGENTS.md` and `.agents/skills/` | Keep adapters optional and separate |
| Portable core | Limit frontmatter to `name` and `description` | Validate unsupported fields as errors |
| Architecture | Replace model-tier rules with capability and risk guidance | Keep authorization and verification explicit |
| Coverage | Add specialized scenario guides and focused examples | Give each a distinct scope and non-goal |
| Tooling | Rebuild validation around real input shapes | Test a single skill, library, and project layout |

## HOW

- Rewrite the primary workflow, entry guide, templates, references, and quick start around the portable contract.
- Add `.agents/adapters/` as the only location for runtime-specific installation notes and metadata.
- Expand the template library with debugging, tests, API contracts, data migrations, releases, security, and feedback patterns.
- Add backend, frontend, data, operations, security, and multi-service authoring guides.

## VALIDATION

- Run syntax compilation for the rewritten Python scripts.
- Run portable validation and health checks against the template library and scaffold sample.
- Resolve all internal relative links and check that active guidance has no stale runtime-specific terminology.
- Remaining limitation: a target runtime adapter must still be verified in that runtime before it can claim installation or automatic discovery behavior.
