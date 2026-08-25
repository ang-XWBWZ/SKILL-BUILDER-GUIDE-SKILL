# Evidence Review Replaces Structural Gates

## WHY

- Problem: fixed-format skill checkers were being treated as an activation and accuracy gate, although they only measured document shape and could add avoidable, contradictory repair loops.
- Desired outcome: skill construction remains guided by direct user consultation and target-project evidence, with no claim that a passed structural script proves useful activation or delivery.
- Constraints: retain portable frontmatter conventions and local documentation-link maintenance without turning either into a quality gate.

## WHAT

| Concern | Change | Risk control |
|---|---|---|
| Fixed-format gate | Remove the two skill checkers | Do not replace them with another mandatory template-shape check |
| Guidance | Add an evidence-review guide | Review intent, project facts, delivery evidence, and uncertainty in context |
| Automation | Keep only packaging/link utility tests and local Markdown link checking | State the narrow scope of each utility explicitly |
| Onboarding | Replace validator commands and success claims in guides and CI | Do not equate a script result with activation or accuracy |

## HOW

- Delete the fixed-format skill checkers with their tests and workflow steps.
- Reframe the main workflow, quick start, templates, and AGENTS.md contract around conversational consultation and evidence review.
- Preserve source-history, delivery-record, and knowledge-capture distinctions introduced by the delivery-governance work.

## EVIDENCE

- `python -B -m unittest discover -s tests -v`: 3 utility regression tests passed.
- `python -B scripts/check-markdown-links.py .`: 68 Markdown files checked; 0 broken local links.
- Remaining limitation: whether a skill triggers and helps on a real request must be established through actual use and project evidence, not inferred from a document shape.
