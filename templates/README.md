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
| [example-iteration-management](example-iteration-management/) | Plan, record, verify, and close consequential delivery work |
| [example-knowledge-capture](example-knowledge-capture/) | Distill verified reusable knowledge into a separate knowledge area |
| [example-feedback-capture](example-feedback-capture/) | Turn recurring feedback into bounded project improvements |
| [example-process-optimization](example-process-optimization/) | Offer one evidence-backed post-delivery improvement suggestion |

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
| [iteration-record-template.md](iteration-record-template.md) | Record scope, work, evidence, risk, and closure for a delivery |
| [knowledge-note-template.md](knowledge-note-template.md) | Record reusable project knowledge with evidence and refresh conditions |
| [project-scaffold](project-scaffold/) | Copy a minimal `AGENTS.md` + `.agents/` layout |

## Use

```bash
cp -R templates/example-api-contract/. my-project/.agents/skills/my-project-api-contract/
```

Replace illustrative facts with target-project evidence, then review the resulting trigger, scope, procedure, evidence sources, and completion expectation in the target project. Use [the evidence-review guide](../references/evidence-review.md); do not treat a fixed template shape as proof that a skill will trigger or perform well.

The delivery-record template is an output artifact, not a canonical skill. Copy and adapt it only when the target project needs traceable delivery records; keep project-specific storage, naming, approvals, and retention in the target project.

The knowledge-note template is a separate output artifact. Use it only after the target project selects an existing or approved new knowledge destination; do not use it as a delivery log or source-diff copy.
