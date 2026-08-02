# Phase 3 — Generate Portable Skills

Transform the approved plan and evidence scan into canonical files under `.agents/skills/`.

## Output path

```text
.agents/skills/{project}-{capability}/
├── SKILL.md
├── references/       # only when detailed material is needed
├── scripts/          # only when a deterministic helper is justified
└── assets/           # only when output assets are reusable
```

Generate or update the root `AGENTS.md` alongside the skills, using the current routing table and verified commands.

## Generation rules

1. Use only `name` and `description` in portable frontmatter.
2. Replace generic wording with project vocabulary, paths, commands, and boundaries supported by the scan.
3. State scope, non-goals, inputs, procedure, constraints, deliverable, and verification.
4. Keep detailed samples and schemas in a directly linked reference.
5. Keep adapters separate and add them only after runtime behavior is verified.
6. Leave no placeholder in a generated production skill.
7. Add a handoff only when it points to an existing skill under a measurable condition.

## Quality self-check

- [ ] Description states outcome and trigger.
- [ ] Every claimed command, path, and version has evidence.
- [ ] Relative links resolve.
- [ ] Existing project conventions are preserved or an approved replacement is documented.
- [ ] `AGENTS.md` routes only to existing canonical skills.
- [ ] Runtime-specific metadata is absent from the portable core.
