# Knowledge, Delivery, and Entry-Point Governance

## WHY

- Problem: the guide did not explicitly separate exact version-control history, dated delivery records, and reusable project knowledge. It also did not make knowledge-destination choices or existing AGENTS.md treatment part of the builder consultation.
- Desired outcome: target projects choose where knowledge lives before generation; iteration records preserve delivery chronology and link to Git revisions; reusable conclusions live in a separate knowledge area; AGENTS.md becomes an operational entry point rather than a minimal marker file.
- Constraints: do not create a documentation directory or knowledge base without user direction; do not overwrite an existing AGENTS.md by default; preserve portable canonical skills and isolate runtime-specific material in adapters.

## WHAT

| Concern | Change | Risk control |
|---|---|---|
| Source history | Make version control the exact code/configuration-change authority | Delivery records link to revisions, reviews, or diffs instead of copying them |
| Delivery lifecycle | Add record date, dated implementation trail, and version-control evidence to the delivery template | Commit timestamps do not replace delivery chronology |
| Knowledge capture | Add a selected, separately managed knowledge area, note template, and focused example | Capture only verified reusable conclusions; retain a no-capture disposition otherwise |
| Consultation | Ask about knowledge-base availability, delivery-record placement, knowledge capture, and existing AGENTS.md treatment | Do not infer a destination or overwrite scope |
| AGENTS.md | Define sufficient operational content | Keep full procedures in skills and detailed knowledge in the selected area |

## HOW

- Add project knowledge-management guidance and a knowledge-note template alongside a focused knowledge-capture skill example.
- Update iteration guidance and templates to distinguish Git evidence, dated delivery evidence, and knowledge notes.
- Extend Step 0 consultation, evidence collection, evidence review, decision guidance, AGENTS.md specification, scaffold, and onboarding.
- Describe the operational content of AGENTS.md without reducing it to a fixed-section gate.

## EVIDENCE

- Review the source guide, examples, and nested project scaffold against the documented operational-content expectations.
- Check local Markdown links after documentation updates.
- Remaining limitation: destination selection, documentation access, retention, and AGENTS.md merge decisions require target-project evidence and user direction.
