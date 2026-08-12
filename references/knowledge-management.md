# Project Knowledge Management

Use this guide when a project wants reusable conclusions from implementation, investigation, operations, or delivery work to remain discoverable after the original task closes. A knowledge area is not a second skill library: it stores durable project facts, decisions, patterns, and known limits that can be linked by AGENTS.md or a project skill.

## Keep three records distinct

| Record | Primary purpose | Source of truth | Do not use it for |
|---|---|---|---|
| Version control | Exact code and configuration evolution | Commit, branch, review, and diff history | Lifecycle status, acceptance narrative, or a knowledge catalogue |
| Delivery record | One bounded delivery’s dates, scope, decisions, evidence, and closure | Project-defined delivery-record location | Copying source diffs or accumulating general knowledge |
| Knowledge note | Reusable, stable project knowledge distilled from one or more sources | Project-defined knowledge area | A daily work log, private evidence dump, or substitute for source code |

Reference the exact version-control revision or diff from a delivery record instead of copying it. Reference a delivery record or source path from a knowledge note instead of restating its complete timeline.

## Choose a destination

Use only a destination confirmed during consultation:

1. An existing project knowledge base with known organization and access rules.
2. A new project documentation area explicitly authorized by the user; a portable default is a knowledge subdirectory under the project’s documentation root.
3. A user-provided external documentation location, linked from the canonical project instructions when agents can safely access it.
4. No knowledge capture for the current scope.

If delivery records and knowledge notes share a documentation root, keep them in distinct areas, for example:

~~~text
docs/
├── deliveries/
└── knowledge/
~~~

Do not create either directory merely because the builder was invoked. Do not place secrets, personal data, customer data, private endpoints, or copied production output in either area.

## Decide whether to capture

Capture a knowledge note only when the conclusion is likely to prevent future rediscovery or a repeated mistake. Good candidates include:

- A verified project convention, architectural boundary, or code path.
- A compatibility, data, security, or operational rule with a stable source.
- A resolved ambiguity that materially affects future implementation or verification.
- A reusable diagnostic, failure mode, recovery limitation, or acceptance pattern.

Do not capture a transient task status, a personal preference, a raw conversation, an unverified inference, or a source diff. Record “not captured” in the delivery closure when the project asked for a disposition but no durable knowledge was found.

## Write a knowledge note

Use [the knowledge-note template](../templates/knowledge-note-template.md). Each note should state:

1. The reusable conclusion and where it applies.
2. The source paths, revisions, delivery records, or owner decisions that support it.
3. Exceptions, uncertainty, and a refresh condition.
4. A concise action implication for future work.

Keep facts in their authoritative source. A note should point to the source rather than mirror a large schema, code listing, or record.

## Apply knowledge during construction

When consultation enables a knowledge area:

- Add the confirmed location and its update policy to AGENTS.md.
- Read relevant notes while building or refreshing project skills.
- Link a skill directly to the narrow knowledge note it needs; do not load the entire knowledge area by default.
- Add a knowledge-capture skill only when extraction is a recurring, bounded project responsibility.

Review knowledge notes after a structural refactor, toolchain change, contract change, incident, or contradicting evidence. Retire a note when its source no longer supports it.
