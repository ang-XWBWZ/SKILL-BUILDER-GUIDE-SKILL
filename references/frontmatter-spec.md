# SKILL.md Frontmatter Spec

## Required Fields

| Field | Type | Description |
|------|------|-------------|
| `name` | string | 1-64 chars, lowercase+digits+hyphens. Must match directory name. |
| `description` | string | What it does + when it triggers. 30-150 words. |
| `model_tier` | L0/L1/L2/L3 | Execution axis: who executes. L0=Haiku, L1=Sonnet, L2=Sonnet/Opus, L3=Opus |
| `skill_tier` | meta/planning/functional/atomic | Composition axis: where in the dependency graph |
| `version` | semver | x.y.z |
| `status` | draft/active/deprecated/superseded | Lifecycle state |

## Forbidden Fields

Do NOT add to frontmatter or body: author, created_by, maintained_by, generated_by, contact, promotional URLs, agent/model names as attribution. See `docs/attribution-discipline.md`. The skill belongs to the project, not the tool that generated it.

## Optional Fields

| Field | Type | Description |
|------|------|-------------|
| `review_by` | date (YYYY-MM-DD) | Suggested review date; validator warns if expired |

## Consistency Constraints

- L0 + meta → invalid (meta requires reasoning)
- L0 + planning → invalid (planning requires reasoning)
- L0 + functional → not recommended
- L0 + atomic → valid (pure lookup)

## Removed Fields

These fields were present in earlier versions (≤v2.1) and have been permanently removed. Do NOT re-add them.

| Field | Removal Reason |
|------|------|
| `composes` / `composed_by` | Manually maintained, always stale. Composition relationships are documented in CLAUDE.md routing tables. |
| `context_budget` (l1_metadata, l2_body, l3_references) | Never measured, never enforced. Token budget is a content guideline, not a machine-readable field. |
| `trust_level` | No permission system consumes it. Trust is determined by skill origin path (`.claude/skills/` = project, `~/.claude/skills/` = global). |
| `requires_network` / `requires_file_write` | No execution sandbox reads these. Boolean flags without a consumer are dead weight. |
| `compatibility` | Free-text string, never validated, never enforced. |
| `allowed_tools` | Tool whitelist is not enforced by any execution layer. |
| `evolution` (usage_count, last_corrections, stale_markers) | Required Tier 2 offline scanner to be operational. Was never built. Signal collection without a processor is noise. |

**Rule**: No field may be added unless a tool (script, CI check, execution layer) already consumes it. See Self-Bootstrapping Rule A in `SKILL.md` §12.

## Description Guidelines

Must include both: (1) what the skill does, (2) when it triggers.

```yaml
# Good
description: >-
  MyProject dev standards. Triggered when asking about tech stack,
  code conventions, API design, or dependency versions.

# Bad
description: Dev standards.
```
