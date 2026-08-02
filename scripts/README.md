# Validation scripts

Both tools use only the Python standard library and validate the portable core rather than a particular agent runtime.

## `validate-skills.py`

Validate one skill or a directory that contains direct skill children:

```bash
python scripts/validate-skills.py .agents/skills
python scripts/validate-skills.py .agents/skills/acme-api-contract
python scripts/validate-skills.py .agents/skills --project-root .
python scripts/validate-skills.py templates --allow-placeholders
```

It checks frontmatter, portable field usage, names, relative links, placeholders, and (when requested) the `AGENTS.md` + `.agents/skills/` project layout.

Use `--allow-name-mismatch` only for a source package that will be installed under its canonical skill directory name; generated project skills must keep their directory and `name` identical.

## `check-skill-health.py`

Report non-blocking maintenance signals:

```bash
python scripts/check-skill-health.py .agents/skills
python scripts/check-skill-health.py templates --allow-placeholders
```

## `package-skill.py`

Package a canonical skill directory for distribution:

```bash
python scripts/package-skill.py .agents/skills/acme-api-contract dist
```
