# Skill Validation Protocol

Validate the portable core before adapting it to a runtime. Run the structural checker, then verify project claims against the target repository.

## V1 — Portable structure

The checker must confirm:

- The input is a skill directory or a directory containing skills.
- Each skill has `SKILL.md` with a closed frontmatter block.
- `name` and `description` use the strict portable frontmatter subset, and the name matches the directory.
- Relative Markdown links resolve.
- Production skills contain no unresolved `{placeholder}` values.

## V2 — Project layout

When validating a project root, confirm:

- `AGENTS.md` exists.
- `.agents/skills/` exists and contains at least one skill when the project claims to use skills.
- Canonical `.agents/...` paths listed as Markdown links or inline-code routing entries in `AGENTS.md` resolve.
- Runtime adapters are optional and do not replace canonical skills.

## V3 — Evidence checks

Verify the following with project files or commands, not generated prose:

| Claim | Evidence |
|---|---|
| Build/test command | Run it or inspect the declared task configuration. |
| Dependency/version | Read the active dependency manifest or lockfile. |
| Source path/API | Resolve the path and inspect the declaration. |
| Workflow/release rule | Read the project’s documented or automated source of truth. |

## Template exception

Reusable templates intentionally contain placeholders. Validate them with `--allow-placeholders`; never use that flag for a generated project skill.

## Delivery gate

Report structural failures as blockers. Report missing evidence as uncertainty. Do not claim that an unverified command, path, version, or runtime integration works.

## Automation coverage

Run tool regression tests, validate the source skill, validate the template library and nested project scaffold, then check local Markdown links across the repository. Keep the workflow in `.github/workflows/` so GitHub can discover it.
