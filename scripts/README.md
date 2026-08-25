# Local utilities

These Python-standard-library utilities support distribution and documentation maintenance. They do not assess whether a skill will activate correctly or produce a useful outcome. Use [the evidence-review guide](../references/evidence-review.md) for that judgment.

## `package-skill.py`

Package a canonical skill directory for distribution:

```bash
python scripts/package-skill.py .agents/skills/acme-api-contract dist
```

The command creates `dist/` when it does not exist. The output directory must be outside the source skill directory.

## `check-markdown-links.py`

Check local Markdown links across a repository, guide, or template library:

```bash
python scripts/check-markdown-links.py .
```

External URLs, anchors, and links inside fenced examples are ignored.
