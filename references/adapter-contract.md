# Runtime Adapter Contract

Use an adapter only after the portable project skill is complete. An adapter describes how one runtime consumes or installs the canonical content; it does not redefine the project’s rules.

## Location

Place adapter material under:

```text
.agents/adapters/{runtime}/
```

Keep the runtime name descriptive but neutral, for example `local-tool`, `hosted-assistant`, or a documented product identifier when the project intentionally supports one.

## Adapter responsibilities

- State the target runtime and the verified installation or discovery mechanism.
- Map its metadata or invocation format to the canonical skill path.
- Record any lossy translation or unsupported portable feature.
- Link back to the canonical `SKILL.md` rather than copying its procedure.

## Prohibited behavior

- Do not store the only copy of project rules in an adapter.
- Do not silently alter safety constraints, verification requirements, or skill boundaries.
- Do not claim automatic discovery or tool access without evidence from the target runtime.
- Do not add agent attribution, advertising, or unrelated runtime configuration.

## Minimal adapter note

```markdown
# {Runtime} adapter

Canonical source: `../../skills/{project}-{capability}/SKILL.md`
Installation: {verified command or manual step}
Known difference: {none, or precise translation/limitation}
```
