# Phase 3: GENERATE — Create Skill Files

> *梓匠轮舆，能与人规矩，不能使人巧。* ——《孟子·尽心下》
> Generation isn't fill-in-the-blanks. It's translating what the scan saw into language a skill can use.

## Generation Rules

- **Executor**: Sonnet (L1)
- **Input**: Phase 1 skill plan + Phase 2 scan report + matching template
- **Output**: Skill files. Default output to `.claude/skills/{name}/` (auto-loaded), template/reference skills to `skills/{name}/` (not auto-loaded)

### Output Path Selection

| Target | Output Path | Notes |
|------|---------|------|
| Production project-specific skill | `.claude/skills/{name}/` | Auto-loaded + `/skill` command |
| Template/reference skill | `skills/{name}/` | Not auto-loaded, for methodology reference |

## Generation Prompt Template

```
Agent(
  description: "Generate {skill_type} skill files",
  model: "sonnet",
  prompt: """
    【Task】Generate project-specific {skill_type} skill files for {project_name}
    
    【Skill Plan】
    - Skill name: {skill_name}
    - Execution tier: {model_tier}
    - Composition tier: {skill_tier}
    - Rationale: {reason}
    
    【Code Scan Results】
    {scan_results}
    
    【Reference Template】
    {template_content}
    
    【Generation Requirements】
    1. Complete frontmatter per frontmatter-spec.md (including dual-axis fields)
    2. Trigger words extracted from project's actual terminology (5-15, covering action + query types)
    3. Tech stack table: actual versions from scan (no placeholders)
    4. Code examples: use actual scanned code snippets (sanitized)
    5. Related skills: use relative path references
    6. SKILL.md body ≤ 5000 tokens
    7. openai.yaml short_description labels model tier
    
    【Output Format】
    Complete SKILL.md content + complete openai.yaml content
  """
)
```

## Per-Skill-Type Generation Guidelines

### Standards Skill (dev)

- Tech stack table: actual versions from `package.json` / `pom.xml` / `requirements.txt`
- Layered architecture: customize four-layer structure from scan results (project may have 3 layers or no integration layer)
- Naming conventions: infer actual naming patterns from scan samples, provide 3+ concrete examples
- Compatibility patterns: record non-standard patterns found during scan and their reasons

### Code Map (code-map)

- Directory structure: use `find` / `tree` output, keep only key directories (≤3 levels deep)
- Quick lookup table: at least one specific file-match pattern per entry point
- Route mapping table: extract from route config files/annotations, list actual routes
- Component inventory: list ≥80% of top-level components/modules

### Change Model (change-model)

- Call chain template: use project's actual layer names (e.g., Controller→Service→Repository)
- Risk level definitions: adjust R0-R3 thresholds to fit the project (note: risk levels use R0-R3, execution tiers use L0-L3 — they are different)
- Archive path: check if `docs/changes/` already exists in the project; reuse if present
- Example: fill in one simple real change from the project as a worked example

### Delegation (delegation)

- L0 task catalog: expand with project-specific tasks (e.g., "check Maven dependency version")
- Dispatch format: keep generic format, add project-specific path/config examples

## Quick-Start Path

When the user says "quick start" / "先跑起来" / "just get me running", skip deep scan and validation. 3 steps, ≤5 minutes:

1. **Grab key data** — don't run full SCAN. Extract versions from package.json/pom.xml/go.mod, top 3 directory levels, find entry points
2. **Fill templates** — populate template placeholders with extracted data. Don't chase deep patterns
3. **Deliver + remind** — deliver generated files directly, with the note: "Validation skipped. Consider running `python scripts/validate-skills.py .claude/skills/{name} --semantic`"

Full decision logic: `references/decision-guide.md`.

## Handoff Section Generation

Each generated SKILL.md must include a `## Handoff` section at the end. Generation rules:

1. **Source**: Select the matching row from SKILL.md §1.5 Skill Chains table based on the current skill type
2. **Project-specific**: Replace `{project}-` prefix with the actual project name
3. **Discriminable conditions**: Trigger conditions must be measurable ("new files ≥3", not "if needed")
4. **Max 3 entries**: More than 3 suggests unclear skill boundaries
5. **Format**:

```markdown
## Handoff

After completing this skill, recommend the next skill based on output characteristics:

| Condition | Recommend |
|-----------|-----------|
| {measurable condition} | `{project}-{skill_name}` |
```

Full methodology: `references/skill-chain.md`.

## CLAUDE.md Generation

CLAUDE.md is generated alongside SKILL.md + openai.yaml. Specification: `references/claude-md-spec.md`. Ensure §C includes the global skills awareness block (≤100 words, see `references/global-skills-awareness.md`).

**Generation Prompt Template**:

```
Agent(
  description: "Generate CLAUDE.md",
  model: "sonnet",
  prompt: """
    【Task】Generate CLAUDE.md for {project_name}

    【Module Selection】{claude_md_modules} (decided during ANALYZE phase)

    【Data Sources】
    - Project identity: {analyze_result}
    - Skill plan: {skill_plan}
    - Quick commands: SCAN — {build_config_file}
    - Tech stack: SCAN — {dependency_config}
    - Directory structure: SCAN — {directory_tree}
    - Layer architecture: SCAN — {layer_identification}
    - Compatibility patterns: SCAN — {compatibility_patterns}
    - External dependencies: SCAN — {integration_layer}

    【Generation Requirements】
    1. Fixed skeleton A-D all filled in (project identity, behavioral constitution, skill routing, quick commands)
    2. Behavioral constitution: use the fixed 7 rules + project custom rules (if any)
    3. Quick commands extracted from SCAN package.json/Makefile/pom.xml, each copy-paste executable
    4. Optional modules filled per ANALYZE decision list; skip unselected modules
    5. All data from SCAN results, never re-collected
    6. Total tokens ≤1500
    7. Zero placeholder remnants

    【Output Format】Complete CLAUDE.md content
  """
)
```

**Module Selection Reference**:

| Project Profile | Enable Modules |
|---------|---------|
| All projects | M1, M5 (default) |
| ≥3 modules or ≥50 source files | + M2 |
| Full-stack / microservices / multi-module | + M3 |
| SCAN found non-standard patterns | + M4 |
| ≥3 external dependencies | + M6 |

## Quality Self-Check (synced with SKILL.md §2.4.1 Completeness Checklist)

After generation, before delivering to Phase 4 validation, Sonnet self-checks:

- [ ] All `{placeholder}` replaced with actual content
- [ ] Tech stack versions match scan results
- [ ] File path references use project's actual paths
- [ ] Trigger words exclude generic terms (like "develop", "modify") — use project-specific terms
- [ ] Dual-axis fields (model_tier, skill_tier) filled
- [ ] No forbidden fields (author/signature/contact/generated_by)
- [ ] Related skills use relative path references, pointing to existing directories
- [ ] SKILL.md body ≤ 5000 tokens
- [ ] Progressive loading: functional-tier skills have `references/` directory (if body >3000t)
- [ ] Model delegation: L0 skill body states "must delegate to Haiku"; L1 skills note L0 delegation points
- [ ] Naming disambiguation: risk levels use R0-R3, execution tiers use L0-L3
- [ ] Existing conventions: project's existing docs/changelogs/workflows either incorporated or explicitly replaced
- [ ] Loaded corresponding L3 reference before generating each skill type
- [ ] **CLAUDE.md**: Fixed skeleton A-D all filled
- [ ] **CLAUDE.md**: Module selection matches ANALYZE decision
- [ ] **CLAUDE.md**: Quick commands copy-paste executable, no placeholders
- [ ] **CLAUDE.md**: Tech stack versions 100% match SCAN results
- [ ] **CLAUDE.md**: Skill routing one-to-one with generated skills
- [ ] **CLAUDE.md**: Total tokens ≤1500
- [ ] **Handoff section**: Each generated SKILL.md includes `## Handoff`, recommendations match §1.5 Skill Chains
- [ ] **Handoff references**: Recommended skills in Handoff exist in the target project
