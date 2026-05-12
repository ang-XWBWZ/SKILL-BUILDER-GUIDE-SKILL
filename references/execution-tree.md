# Execution Tree — Unified Task Decomposition & Execution Model

> *图难于其易，为大于其细。天下难事必作于易，天下大事必作于细。* ——《道德经》
> 复杂问题拆成小问题，每个小问题交给对的人。这就是执行树的全部智慧。

> **Load when**: Task contains multiple sub-goals, needs decomposition, delegation pattern selection, sub-agent dispatch, or non-convergence diagnosis. Referenced from `SKILL.md` §2.7 (L3 Routing Table).
>
> The execution tree unifies four concepts that are the same thing viewed from different angles: **pipeline** (lifecycle), **decomposition** (how the tree expands), **delegation** (who executes each node), **progressive loading** (what context each node loads).

---

## 1. Concept

```
Execution Tree = Pipeline(Lifecycle) + Decomposition(Expansion) + Delegation(Assignment) + Loading(Context)

Pipeline:   ANALYZE builds root → SCAN fills leaves → GENERATE outputs → VALIDATE verifies → CONFIRM closes
Decomposition: H-ADMC criteria → AND/OR/LEAF/CONDITION node types
Delegation:   L0→Haiku, L1→Sonnet, L2→Sonnet/Opus, L3→Opus (per-node assignment)
Loading:      L1 metadata → L2 body → L3 references → L4 scripts (per-node context scope)
```

Every task that meets ≥2 H-ADMC criteria produces an execution tree before execution begins. The tree is written down, user-reviewable, and recoverable (subtree replanning on failure).

---

## 2. When to Build a Tree

Apply H-ADMC criteria. If **any** condition is met, build an execution tree before acting:

1. **Multiple sub-goals** — task contains more than one distinct goal
2. **Mixed operation types** — requires both analysis and generation, or implementation and verification
3. **Cannot close in one pass** — cannot complete and verify within a single pass
4. **Risk isolation** — independent verification reduces overall risk
5. **Parallelism opportunity** — sub-tasks can run concurrently
6. **Contains L0 work** — non-trivial tasks almost always include L0 sub-tasks

**Cases NOT requiring a tree**: single goal, single-pass closure, pure reasoning without file/command operations.

---

## 3. Node Types

Every node in the execution tree has a type:

| Node Type | Semantics | When to Use |
|------|------|------|
| **AND** | All children must succeed. Fail if any child fails. | Mandatory sub-tasks — all required for completion |
| **OR** | At least one child must succeed. Try left-to-right (priority order). | Alternative approaches — first viable option wins |
| **LEAF** | Primitive task, directly executable. Has model_tier + skill assignment. | Single tool call or Agent() dispatch — cannot be further decomposed |
| **CONDITION** | Gate node. Evaluates a condition before children execute. | Precondition checks — branch selection depends on runtime state |

**Hard constraints**:
- Maximum depth = 5. Nodes at depth 5 are forced LEAF.
- Minimum LEAF granularity = 1 tool call (single Read, Write, Bash, Agent dispatch).
- AND nodes must have ≥2 children. OR nodes must have ≥2 children.

---

## 4. Node Annotation

Each node carries:

```
Node {
  task: string          // one-sentence description
  type: AND|OR|LEAF|CONDITION
  model_tier: L0|L1|L2|L3  // who executes
  skill: string|null    // assigned skill (null for compound nodes)
  references: [path]    // files to load for this node's context
  children: [Node]      // subtasks (empty for LEAF)
  dependencies: [id]    // dataflow: nodes whose outputs this node consumes
  verification: {       // done condition
    condition: string
    method: string
  }
}
```

---

## 5. Delegation Patterns (Tree Topologies)

### Pattern A: L0 Information Gathering (most common)

```
Root (L2): Understand requirement, determine what information is needed
  ├── [AND/LEAF L0] Locate files → code-map
  ├── [AND/LEAF L0] Read tech specs → dev
  ├── [AND/LEAF L0] Read existing code → extract patterns
  └── Main Model (L2): Integrate information, execute implementation
```

### Pattern B: Parallel L0 Batch

```
Root (L1): Decompose into N independent checks
  ├── [AND/LEAF L0] Check A  ∥
  ├── [AND/LEAF L0] Check B  ∥  (parallel — no data dependencies)
  ├── [AND/LEAF L0] Check C  ∥
  └── Main Model (L1): Collect results, output summary
```

### Pattern C: Complex Investigation

```
Root (L2): Analyze problem, locate clues
  ├── [AND/LEAF L0] Read key code files
  ├── [AND/LEAF L0] Check git log change history
  └── Main Model (L2): Synthesize evidence, diagnose root cause
```

---

## 6. Progressive Loading in the Tree

Each node loads only the context needed for its execution tier:

| Node Tier | Loads | Examples |
|:--:|------|------|
| **L0** (Haiku) | Target file paths only | Read a specific file, run a fixed command |
| **L1** (Sonnet) | L2 body of assigned skill + immediate dependencies | Generate a single skill file |
| **L2** (Sonnet/Opus) | L2 body + L3 references of assigned skill | Diagnose root cause across modules |
| **L3** (Opus) | Full skill system context | Architectural redesign |

Nodes at the same tree depth share the same "phase" but not necessarily the same skill. The tree structure determines what context is in scope — not a single global "load everything" decision.

---

## 7. Sub-Task Design Rules

Each sub-task must satisfy:

- **One goal** — unambiguous, not multi-intent
- **Clear input** — file paths, search patterns, commands to execute
- **Expected output** — return in C/B/U format (§8)
- **Verification condition** — what counts as "done"
- **Minimal dependencies** — as independent and parallelizable as possible

| Bad (vague, multi-goal) | Good (clear, single-goal) |
|--------------------------|----------------------------|
| "Analyze the business layer and fix issues" | "Read {filename}, extract all public method signatures, output as a list" |
| "Check service health status" | "Check if backend process is running, database is reachable, API responds 200" |

---

## 8. Sub-Agent Output Specification

Every sub-agent must return structured three-element output. Free-form narration is forbidden:

```
Conclusion:    One-sentence answer to the assigned goal
Basis:         Concrete evidence, observations, reasoning path
Uncertainty:   Risks, missing information, failure modes (write "None" if none)
```

### Main Agent Integration

After receiving sub-agent output, the main model does only three things:
1. Extract each sub-agent's conclusion
2. Identify conflicts or gaps
3. Decide: continue / re-decompose / complete

**The main model MUST NOT substitute sub-agent local reasoning.**

### Standard Dispatch Format

```
Agent(
  description: "3-5 word task description",
  model: "haiku",
  prompt: """
    【Task】What specifically to do
    【Files】List of file paths to read
    【Output Requirements】Return in Conclusion/Basis/Uncertainty format
  """
)
```

---

## 9. Subtree Recovery

When a node returns FAILURE:

1. Mark the node FAILURE — do NOT repeat the same execution
2. Return to the parent decomposition layer
3. Change task structure: different angle, different tool, different scope
4. Re-decompose and re-dispatch only the failed subtree
5. Preserve all SUCCESS nodes outside the affected subtree

If the same subtree fails twice after replanning → escalate to higher model tier.

---

## 10. Upgrade / Escalation

| Trigger Condition | Threshold | Action |
|-------------------|-----------|--------|
| User repeatedly dissatisfied | Same task, ≥2 rounds of corrections not passing | Package context, escalate to reasoning/top-tier model |
| Rework loops | Same code section modified ≥3 times, issue not converging | Stop modifying, re-analyze root cause |
| Issue not converging | 3 rounds of conversation, scope still not narrowing | Escalate to higher-tier model for re-diagnosis |

**Escalation Information Package**: original requirements + attempted solutions with failure reasons + current blocker + eliminated hypotheses.
