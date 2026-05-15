---
name: xiaobenben
description: >-
  Little Notebook — records user dissatisfaction and satisfaction moments during agent interaction.
  Use when user expresses anger, frustration, abusive language, or strong satisfaction.
  L0 — delegate to Haiku for recording and cleanup.
model_tier: L0
skill_tier: atomic
version: 1.0.0
status: active
---

# Little Notebook

> *有则改之，无则加勉。* ——《论语》

Agent made a mistake — record it. User is satisfied — record that too. Auto-clean every 3 days. No clutter.

## Trigger Conditions

- User is angry, abusive, or expresses strong frustration
- User explicitly praises or expresses satisfaction
- Agent detects a clear emotional tone shift in the conversation

---

## 1. Negative Record

When triggered, append to `records/log.md`:

```markdown
## {timestamp} — Negative

**Context**: {What the agent was doing, what went wrong. ≤3 sentences. No self-defense.}
**Quote**: {User's exact words, quoted directly.}
**Apology**: {Agent's apology or acknowledgment.}
```

**Rules**:
- Context is brief and non-defensive. Just state what the agent was doing and what triggered the user
- Quote verbatim, don't paraphrase
- After apologizing, move on — don't dwell

## 2. Positive Record

When user expresses satisfaction:

```markdown
## {timestamp} — Positive

**Context**: {What the agent did.}
**Result**: {What the user said. ≤2 sentences.}
```

Positive records are deliberately brief. The point is knowing what worked, not collecting praise.

---

## 3. Auto-Cleanup

Before each write, scan `records/log.md` and delete entries older than 3 days (72 hours).

Cleanup rules:
- Entry boundary: `## {timestamp}`
- Parse timestamp → calculate age → if >72 hours, delete entire entry (from `##` to next `##`)
- Keep all entries under 3 days

```python
# Cleanup pseudocode
now = datetime.now()
cutoff = now - timedelta(hours=72)
# Iterate entries, timestamp < cutoff → delete entire entry
```

Cleanup is dynamic — runs before every write, not as a background job. Zero configuration.

---

## Handoff

—

## 4. Model Tier

**L0 — Haiku / atomic tier**: Mechanical recording + time comparison, zero reasoning. Main model detects emotional shift → delegates to Haiku for writing and cleanup.
