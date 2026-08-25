# Phase 2 — Evidence Scan

Scan the target repository before writing project facts into a skill. Separate observations from inferences.

## Scan targets

| Concern | Inspect | Record |
|---|---|---|
| Project shape | Root tree, workspace config, package manifests | Components, entry points, ownership boundaries |
| Commands | Task runners, CI, Makefiles, scripts | Exact command and expected evidence |
| Implementation patterns | Representative source and tests | Common convention and named exceptions |
| Contracts | Schemas, API specs, client code, events | Consumers, compatibility boundaries, validation source |
| Data and operations | Migrations, deployment config, runbooks | Safety controls, rollback, environment differences |

## Evidence record

```text
Conclusion: {direct finding}
Evidence:   {paths, commands, and observed patterns}
Uncertainty:{blind spot or "none"}
```

## Rules

- Read enough samples to distinguish a convention from an accident.
- Redact secrets and personal data from any saved example.
- Do not modify project files during a scan unless the task explicitly includes a change.
- Stop and seek owner direction when a source is ambiguous or accessing it requires new authority.
