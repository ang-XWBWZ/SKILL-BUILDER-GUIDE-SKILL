# Maintenance Roadmap

Maintain the guide through evidence from real project-skill creation, not through speculative framework additions.

## Near-term checks

1. Run the portable validator and health scan after changes to templates, scripts, or layout rules.
2. Exercise the project scaffold in a representative repository and record only reproducible improvements.
3. Review every adapter separately whenever its target runtime changes.

## Candidate additions

Add a new scenario guide or example only after it meets all of the following:

- It represents a repeated project concern not covered by the current library.
- Its trigger, inputs, output, and verification are materially different from an existing skill.
- Its advice can be grounded in evidence rather than generic slogans.
- It can remain portable, with runtime details isolated to an adapter.

## Refresh triggers

Review a generated project skill after a structural refactor, command/toolchain change, contract change, migration incident, release issue, security finding, or repeated user correction.

## Retirement

Merge or remove a skill when its trigger overlaps another skill, its workflow disappears, or its project facts cannot be maintained. Keep the change visible in repository history rather than preserving stale live instructions.
