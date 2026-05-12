# Change Model — Structured Change Reports

> *前事之不忘，后事之师也。* ——《战国策·赵策一》
> 代码会变迁，但每一次变迁的理由不该被遗忘。

> **Load when (explicit)**: Generating change reports, DiffLogs, Release Notes, archiving change records, or performing call-chain checks.
> **Load when (implicit)**: Agent has completed a modification to the project and is entering the CONFIRM phase of any pipeline execution. Agent should ask: "Generate a change report for this session?"
> Referenced from `SKILL.md` §2.7 (L3 Routing Table).
>
> **Position**: Functional tier methodology. Transforms code changes into structured WHY/WHAT/HOW/VALIDATION reports, with call-chain checking and archival storage.

---

## 1. What Is Change Model

Change Model transforms raw code diffs into a four-layer structured document:

```
┌─────────────────────────────────────────┐
│  Layer 1: WHY — Change Context & Requirements   │
│  ├─ 1. Change Background                        │
│  └─ 2. Requirements Analysis                    │
├─────────────────────────────────────────┤
│  Layer 2: WHAT — Impact & Risk                 │
│  ├─ 3. Impact Analysis                          │
│  └─ 4. Risk Assessment                          │
├─────────────────────────────────────────┤
│  Layer 3: HOW — Design & Implementation        │
│  ├─ 5. Design Approach                          │
│  └─ 6. Implementation Mapping                   │
├─────────────────────────────────────────┤
│  Layer 4: VALIDATION — Verification & Delivery  │
│  ├─ 7. Call-Chain Check (pre-test)              │
│  ├─ 8. Test Verification                        │
│  └─ 9. Delivery & Rollback                      │
└─────────────────────────────────────────┘
```

### Problems Solved

| Problem | Change Model Solution |
|------|-------------------|
| Diff fragmentation | Organize by causal chain, not by file listing |
| Lack of behavioral abstraction | Make "condition → result" decision logic explicit |
| Hard for newcomers to understand | Four-layer structure: background → requirements → design → verification |
| AI cannot infer intent | Structured, machine-readable section design |
| Changes cannot be traced | Archival system: date-based + INDEX.md |
| Missing historical reports | Git analysis: auto-generate report skeleton from commit history |

### Distinction from Changelog

| Dimension | Change Model | Changelog |
|------|------------------------|-------------------|
| **Perspective** | Forward-looking: designed before changes | Retrospective: recorded after |
| **Granularity** | One report per requirement/task | One entry per commit/PR |
| **Content** | WHY→WHAT→HOW→VALIDATION causal chain | What changed |
| **Purpose** | Guide development, risk control | History tracking |

---

## 2. Layer 1: WHY — Change Context & Requirements

### 2.1 Change Background

```markdown
| Element | Description |
|------|------|
| **Requirement Source** | {requester/ticket number} |
| **Trigger Reason** | {why this change is needed} |
| **Desired Goal** | {what effect the change should achieve} |
```

**Guidelines**: Source specific and traceable. Reason clarifies "what the problem is". Goal verifiable.

### 2.2 Requirements Analysis

```
Input: {input params}

Judgment conditions:
- {condition 1} → {result 1}
- {condition 2} → {result 2}

Output: {output params}
```

**Guidelines**: Use "condition → result" format. Cover all business branches. Specify inputs/outputs explicitly.

---

## 3. Layer 2: WHAT — Impact & Risk

### 3.1 Impact Analysis

```markdown
| Dimension | Impact Description | Impact Level |
|------|----------|:--------:|
| **Upstream Callers** | {description} | None/Low/Med/High |
| **Downstream Dependencies** | {description} | None/Low/Med/High |
| **Database** | {tables involved} | — |
```

### 3.2 Risk Assessment

```markdown
| Risk Item | Level | Description | Mitigation |
|--------|:----:|------|----------|
| {risk name} | R0/R1/R2/R3 | {description} | {mitigation} |
```

**Risk Level Definitions** (R0-R3 — distinct from execution tiers L0-L3 in SKILL.md §2):

| Risk Level | Definition | Example |
|:----:|------|------|
| R0 | No external impact | Internal refactor, log optimization |
| R1 | Internal API change | New optional parameter, internal interface adjustment |
| R2 | External contract change | Interface signature change, response format change |
| R3 | Data/state migration | Database migration, config change |

---

## 4. Layer 3: HOW — Design & Implementation

### 4.1 Call Chain

```
{Caller}
  │ {Request method} {endpoint path}
  ▼
Interface Layer ({entry component})
  │ {business layer method}
  ▼
Business Layer ({business component})
  │ {business logic description}
  ▼
Data Layer ({data component})
  │ {query/persistence description}
  ▼
Database
```

### 4.2 Implementation Mapping

```markdown
| # | Operation | File Path | Change Description |
|:----:|:----:|----------|----------|
| 1 | ⭐/✏️ | `{path}` | {description} |
```

---

## 5. Call-Chain Checking Methodology

### 5.1 Core Objectives

| Objective | Description |
|------|------|
| Chain completeness | No breaks from entry point to endpoint |
| Type matching | Data types correctly passed at each link |
| Final call | SQL/API/message etc. final operation is correct |

### 5.2 Checking Procedure

```
Step 1: Identify the entry point
  ├─ API endpoint / page event / scheduled task / message consumption
  └─ Record input parameter types and validation rules

Step 2: Trace intermediate links
  ├─ Interface layer → Business layer → Data layer
  ├─ Record method signatures and return types at each link
  └─ Check whether types match

Step 3: Verify the final call
  ├─ SQL statement / external API / message queue / cache write
  └─ Check whether parameters are passed correctly

Step 4: Error handling check
  ├─ Are exceptions caught?
  └─ Are errors returned correctly?
```

### 5.3 Checklist

| # | Check Item | What to Check | Verification Method |
|:-:|--------|----------|----------|
| 1 | Entry parameters | Parameter types, required-field validation | Inspect interface definition |
| 2 | Parameter passing | Are parameters passed correctly across layers? | Trace method call chain |
| 3 | Type matching | Do input/output types match at each layer? | Compare type definitions |
| 4 | Null handling | Do optional fields have default values? | Inspect code logic |
| 5 | Final call | Are SQL/API/message parameters correct? | Inspect final implementation |
| 6 | Return handling | Is the return value assembled correctly? | Inspect return path |
| 7 | Exception handling | Are exceptions caught? | Inspect try-catch |
| 8 | Degradation logic | Is there a fallback on failure? | Inspect fallback |

### 5.4 When to Check

| Phase | Execute? | Notes |
|------|:--------:|------|
| After requirements analysis | ❌ | Not yet implemented |
| After coding | ✅ | **Must execute** |
| Before testing | ✅ | Ensure chain is correct before testing |
| Before launch | ✅ | Final verification |

### 5.5 Call-Chain Check Template

```markdown
### 7. Call-Chain Check

| Check Item | Status | Notes |
|--------|:----:|------|
| Entry validation | ✅/❌ | Parameter validation correct |
| Type check | ✅/❌ | Data types match |
| Final call | ✅/❌ | SQL/API call correct |

**Data Flow Verification**:
{Entry}
  → {Intermediate link 1}
  → {Intermediate link 2}
  → {Final call}
```

**Pass Condition**: All check items must be ✅.

---

## 6. Generating a Project-Specific Skill

### 6.1 Customization Items

| Customization | Description |
|--------|------|
| Section add/remove | Add or remove sections as needed |
| Risk levels | Adjust R0-R3 definitions to fit the project |
| Template format | Markdown / JSON / YAML |
| Trigger words | Project-specific change-related vocabulary |

### 6.2 Merging User Documentation

If the user provides an existing change report template or spec document, **the user's document takes precedence**:

1. Read the user's change report template/spec
2. Compare differences with this methodology
3. Use the user's document as baseline; supplement missing parts
4. Record differences for user confirmation

| Difference Type | Handling |
|----------|----------|
| User template has unique sections | Keep user sections, mark as project customization |
| User template is missing a layer | Suggest adding it |
| User has different risk level definitions | Use user's definitions |
| User uses different terminology | Keep user's terminology |

---

## 7. Archival System

### 7.1 Main Flow

```
Coding complete → Call-chain check → Test verification → Generate final report → Archive
```

### 7.2 Directory Structure

```
docs/changes/
├── INDEX.md              # Master index (by time + by type)
├── 2026-04-26/
│   ├── 20260426-01-add-filter-feature.md
│   └── 20260426-02-fix-login-timeout.md
└── 2026-04-27/
    └── 20260427-01-refactor-payment-module.md
```

Naming: `{YYYYMMDD}-{NN}-{short-description}.md`. Append only, sequential per day.

### 7.3 Archive Validation Checklist

- [ ] Complete four-layer structure (WHY / WHAT / HOW / VALIDATION)
- [ ] All call-chain check items ✅
- [ ] File paths verified against actual code
- [ ] Rollback plan explicit and executable
- [ ] No sensitive information
- [ ] INDEX.md updated

### 7.4 Timing

| Phase | Action |
|------|------|
| Before change | Create draft, fill WHY/WHAT |
| After coding | Fill HOW |
| Before testing | Fill VALIDATION (call-chain check) |
| After testing | Complete test results |
| Final | Archive |

### 7.5 Automation

The archival workflow (§7.1-7.4) can be automated via Git hook or CI. For implementation: analyze commit history with `git log --oneline`, generate the report skeleton from commit messages, and append to `docs/changes/INDEX.md`. No bundled scripts — integrate with the project's existing toolchain.
