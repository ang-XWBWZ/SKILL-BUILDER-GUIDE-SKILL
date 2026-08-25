# Skill Builder Guide

Maintain this repository as a portable guide for project-specific agent skills.

## Canonical contract

- Treat `AGENTS.md` and `.agents/skills/` as the cross-agent project contract described by this guide.
- Keep portable `SKILL.md` files independent of a particular vendor, model name, command syntax, or discovery mechanism.
- Put runtime-specific behavior only in an explicit adapter. Do not make an adapter the canonical source.
- Keep frontmatter limited to `name` and `description`; keep project facts in the body or references.

## Change discipline

- Inspect the affected guide, template, and evidence-review guidance before changing the architecture.
- Keep `SKILL.md` concise; move detailed domain material into a directly linked reference.
- Update every incoming link when moving or renaming a file.
- Add a template only when it represents a distinct recurring task with clear inputs, outputs, and verification.
- Keep examples generic and free of real credentials, project secrets, agent signatures, and promotional text.
- Place any process optimization suggestion after the direct request, implementation, and required documentation; one verified signal may suggest, but only explicit owner direction may change a process.
- Run relevant tool regression tests and the documentation link check after changing skills, templates, or layout guidance.

## Repository map

| Area | Purpose |
|---|---|
| `SKILL.md` | The portable skill-building workflow |
| `references/` | On-demand architecture, evidence-review, and domain guidance |
| `references/scenarios/` | Specialized guidance by project concern |
| `templates/` | Portable skill and entry-point patterns |
| `scripts/` | Local packaging and documentation-link utilities |
| `tests/` | Regression coverage for local packaging and link-checking utilities |
| `docs/` | Human-facing onboarding and migration material |

For source ownership and signature behavior, follow [the attribution discipline](docs/attribution-discipline.md).
