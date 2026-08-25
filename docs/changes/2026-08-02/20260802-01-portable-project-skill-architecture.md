# Portable Project Skill Architecture

## WHY

- Problem: the guide treated one runtime’s directory, instruction file, metadata, and model terminology as the project-wide skill architecture.
- Desired outcome: project-specific skills can be authored once, stored in a portable canonical location, and adapted explicitly for any supported runtime.
- Constraints: preserve evidence-based guidance and avoid duplicated rules without binding usefulness to a fixed document shape.

## WHAT

| Concern | Change | Risk control |
|---|---|---|
| Canonical layout | Adopt `AGENTS.md` and `.agents/skills/` | Keep adapters optional and separate |
| Portable core | Limit frontmatter to `name` and `description` | Keep runtime-specific fields in explicit adapters |
| Architecture | Replace model-tier rules with capability and risk guidance | Keep authorization and verification explicit |
| Coverage | Add specialized scenario guides and focused examples | Give each a distinct scope and non-goal |
| Tooling | Keep narrow packaging and documentation-link utilities | Do not treat utility output as a skill-quality gate |

## HOW

- Rewrite the primary workflow, entry guide, templates, references, and quick start around the portable contract.
- Add `.agents/adapters/` as the only location for runtime-specific installation notes and metadata.
- Expand the template library with debugging, tests, API contracts, data migrations, releases, security, and feedback patterns.
- Add backend, frontend, data, operations, security, and multi-service authoring guides.

## EVIDENCE

- Run regression checks for changed utilities.
- Resolve all internal relative links and inspect active guidance for stale runtime-specific terminology.
- Remaining limitation: a target runtime adapter must still be verified in that runtime before it can claim installation or automatic discovery behavior.
