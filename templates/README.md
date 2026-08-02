# Portable templates and examples

Copy a focused example into `.agents/skills/`, rename its directory to `{project}-{capability}`, then replace illustrative facts with verified project evidence. The files are portable cores; add a runtime adapter only after its integration is known.

## Core patterns

| Example | Focus |
|---|---|
| [example-dev](example-dev/) | Capture project conventions and implementation constraints |
| [example-code-map](example-code-map/) | Navigate modules, entry points, and commands |
| [example-workflow](example-workflow/) | Deliver a feature with decision points and verification |
| [example-bug-investigation](example-bug-investigation/) | Reproduce, isolate, fix, and prove a regression fix |
| [example-test-strategy](example-test-strategy/) | Select meaningful test coverage and evidence |
| [example-feedback-capture](example-feedback-capture/) | Turn recurring feedback into bounded project improvements |

## Boundary and operations patterns

| Example | Focus |
|---|---|
| [example-api-contract](example-api-contract/) | Change and verify an API contract safely |
| [example-call-chain](example-call-chain/) | Trace a request, event, or data flow end to end |
| [example-data-migration](example-data-migration/) | Plan, execute, and verify persistent-data changes |
| [example-release-runbook](example-release-runbook/) | Release, observe, and roll back safely |
| [example-security-review](example-security-review/) | Review security-sensitive boundaries before change |
| [example-delegation](example-delegation/) | Split evidence-gathering work without vendor coupling |

## Skeletons

| File | Use |
|---|---|
| [skill-template.md](skill-template.md) | Start a portable `SKILL.md` |
| [agents-md-template.md](agents-md-template.md) | Start the root `AGENTS.md` |
| [adapter-template.md](adapter-template.md) | Document a verified runtime adaptation |
| [change-model-template.md](change-model-template.md) | Record WHY / WHAT / HOW / VALIDATION for a change |
| [project-scaffold](project-scaffold/) | Copy a minimal `AGENTS.md` + `.agents/` layout |

## Use

```bash
cp -R templates/example-api-contract/. my-project/.agents/skills/my-project-api-contract/
python scripts/validate-skills.py my-project/.agents/skills/my-project-api-contract
```

For a reusable template library, placeholders are allowed. Generated project skills must have no unresolved placeholders.
