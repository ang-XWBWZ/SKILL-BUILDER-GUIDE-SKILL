# Evidence Review for Project Skills

Review a generated project skill in its actual project context. Do not use a fixed document shape, directory pattern, or successful script run as evidence that a skill will trigger well or help complete work.

## R0 — Current intent

Before scanning, generating, copying, or overwriting, establish manually that:

- The current operation and target boundary are known: initialize, assess, repair, extend, migrate, review, or plan.
- The desired maturity and definition of done are known, or a user-authorized low-impact assumption is recorded.
- Material scope, authority, compatibility, and acceptance questions are resolved or explicitly retained as open.
- A repeat activation identifies existing canonical assets and preserves them unless the user selected an exact change scope.
- An existing `AGENTS.md` has a selected preserve, augment, merge, migrate, replace, or assess-only disposition.
- The knowledge destination, delivery-record placement, and reusable-knowledge capture disposition are known before generating dependent documentation.

Use [the consultation protocol](consultation-protocol.md). A conversation requires conversational evidence; no document checker can establish it.

## R1 — Project facts and useful instructions

Review the generated material with the project sources open. Confirm that:

- Each skill has a distinct trigger, outcome, scope boundary, and procedure proportionate to its work.
- `AGENTS.md` gives enough verified project map, hard constraints, commands, documentation locations, and routes to begin ordinary work.
- Frontmatter stays within the portable `name` and `description` convention, while project facts live in the body or direct references.
- Referenced source paths, APIs, versions, commands, policies, and skill routes resolve in the target project.
- A command, test, or operational claim is supported by observed output or an authoritative project source.
- Unknown facts remain explicit uncertainty rather than becoming invented instructions.

The repository’s [Markdown link checker](../scripts/README.md#check-markdown-linkspy) can find broken local documentation links. It checks links only; it does not establish instruction quality, runtime activation, or delivery success.

## R2 — Delivery evidence

For a compact completion report, confirm that result, actual changes or decision, evidence, open items, and final status are present.

For a full delivery record, review that:

- Scope, acceptance conditions, and work items have a confirmed or unresolved disposition.
- The record date and dated lifecycle entries are present.
- Verification entries record actual results; failed, skipped, and inapplicable checks are not presented as passed.
- Exact code or configuration changes link to version-control evidence instead of copied source diffs.
- Plan-versus-actual differences, open work, risk, and recovery limits have a conclusion.
- The final state agrees with the evidence, and the record does not include secrets or unnecessary sensitive output.

## R3 — Knowledge capture

When knowledge capture is enabled, review that a note is stored in the selected knowledge area, is reusable and scoped, cites its evidence, states a boundary or exception, and includes a refresh trigger. A delivery with no durable conclusion should record that no knowledge note was created and why.

## Reporting limits

Treat missing intent or material evidence as a blocker. Treat facts that could not be checked as uncertainty. Do not claim that an unobserved command, path, version-control change, knowledge note, runtime integration, or delivery closure works.

Run regression tests for any remaining utilities that changed, and use the local Markdown link checker for documentation changes. These are narrow tool checks, not quality gates for generated skills.
