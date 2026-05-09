# Workflow Skill Customization Guide

## Where to Extract Workflow Information

| Source | What to Extract |
|------|------|
| CI/CD config (`.github/workflows/`, `Jenkinsfile`) | Deploy steps, test stages, approval gates |
| Contributing docs (`CONTRIBUTING.md`) | PR process, branch naming, review requirements |
| Package scripts (`package.json`, `Makefile`) | Build, test, lint, deploy commands |
| Team wiki / Notion / Confluence | Release checklist, environment setup |
| Git history (`git log --oneline`) | Commit conventions, branch patterns |

## Customization Checklist

When generating a project-specific workflow skill:

- [ ] Each workflow step maps to a real project file or command
- [ ] Branch naming convention is verified against actual branches
- [ ] Deploy steps are verified against CI config
- [ ] Rollback steps reference real commands or scripts
- [ ] Duration estimates match team experience
- [ ] Checklist items cover the most common failure modes

## Example: Extracting from a Real Project

```
Source: package.json scripts
  "build" → compiles TypeScript
  "test" → runs Jest with coverage
  "lint" → ESLint + Prettier
  "deploy" → pushes to staging

Generated workflow step:
  | 3 | Build & Test | npm run build && npm test | Build passes, all tests green |
```
