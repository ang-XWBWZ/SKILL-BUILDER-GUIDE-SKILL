# Data and Migration Skills

Create a data-migration skill before persistent changes become routine or risky. Treat schemas, stored records, backfills, imports, retention, and state transitions as separate from ordinary feature edits.

## Evidence checklist

- Authoritative schema and migration history.
- Data ownership, volume, retention, and privacy constraints.
- Active application versions and rollout compatibility.
- Backup, restore, rehearsal, and post-run validation capabilities.
- Idempotency, failure recovery, and monitoring evidence.

## Required decisions

| Decision | Why it matters |
|---|---|
| Expand/contract or one-step change | Determines mixed-version safety |
| Online, offline, or staged execution | Determines availability and approval needs |
| Idempotent behavior | Determines retry and repair safety |
| Recovery path | Determines whether rollback is real or only forward repair |
| Validation invariant | Determines when the migration is actually complete |

## Done definition

The skill must make authorization, recovery limits, data validation, and compatible rollout explicit. It must never imply that destructive actions are safe by default.
