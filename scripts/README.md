# Scripts — L4 Executables

Zero-context execution tools. No LLM dependency.

## validate-skills.py

Validates skill directory completeness: required files, frontmatter format, YAML parsing, model tier tags.

```bash
python validate-skills.py .              # Validate root skill
python validate-skills.py templates/     # Validate template skills
```

Dependency: `pip install pyyaml`

## check-skill-health.py

Offline health scan: cross-reference integrity, review_by expiration, token budget, forbidden frontmatter fields. No LLM calls — Haiku (L0) execution.

```bash
python check-skill-health.py .           # Health check root
python check-skill-health.py templates/  # Health check templates
python check-skill-health.py . --json    # JSON output
```

## package-skill.py

Package a skill directory as `.zip` archive for distribution.

```bash
python package-skill.py .                          # Package root skill
python package-skill.py templates/example-dev      # Package a template
```
