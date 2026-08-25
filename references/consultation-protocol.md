# Consultation Before Skill Construction

Use this protocol whenever the skill builder is first activated for a project or activated again after a prior skill-building session. Its purpose is to establish the user’s current goal before an evidence scan, generation, copy, or overwrite begins.

The protocol is runtime-neutral. Keep the current consultation state in the active conversation or a project-owned delivery record when one is warranted; do not add session state, approval flags, or conversation history to portable SKILL.md frontmatter.

## Activation gate

~~~text
Activation
  → read-only orientation of known canonical files, when a target project is known
  → consultation
  → intent summary confirmed or materially complete
  → evidence scan and approved operation
~~~

Read only enough to determine whether AGENTS.md, .agents/skills/, or related project instructions already exist. This orientation must not become a deep evidence scan or an implied authorization to generate.

Before generation, copying, or overwrite, establish:

1. The current operation: initialize, assess, repair, extend, migrate, review, or plan only.
2. The desired outcome and target boundary: a whole library, named skill, template, adapter, or documentation.
3. The requested maturity: baseline, focused, or comprehensive.
4. Constraints that materially affect scope, authority, compatibility, or the definition of done.
5. The knowledge and documentation destination: an existing usable knowledge base, an approved new documentation area, or a project-provided location.
6. The treatment of any existing AGENTS.md: preserve, augment, merge, migrate, or assess only.

If the current request already supplies these facts, summarize the intended operation and proceed without redundant questions. If a missing fact can change the generated result, ask before continuing.

## Opening question

When activation is broad, ambiguous, or only repeats a prior trigger, ask one concise opening question before any generation:

~~~text
What would you like to do with this project’s skill system now: initialize it,
assess the current library, repair it, extend a named capability, migrate it,
review it, or plan the next change?
~~~

Ask no more than three targeted follow-up questions at once. Prefer questions that resolve a concrete decision over a generic interview.

## Knowledge and documentation consultation

Ask whether the project has a usable knowledge base and, if so, record its location, access boundary, and organization rules. Then ask two independent disposition questions:

1. Should delivery or iteration records be stored in that knowledge base, or in a separate delivery-record area?
2. Should reusable knowledge distilled from completed work be added to that knowledge base?

Do not infer that a delivery record is reusable knowledge. By default, keep high-churn delivery evidence separate from durable knowledge notes, even when both live under the same documentation root.

If no usable knowledge base exists, ask whether the user wants to create a documentation area in the project. If not, ask for the team’s dedicated documentation location. Do not create a `docs/` directory, a knowledge area, or external documentation content until the user selects the destination.

Use [knowledge management guidance](knowledge-management.md) for destination choices and [traceable delivery guidance](iteration-management.md) for delivery-record placement.

## Existing AGENTS.md consultation

When AGENTS.md already exists, read it before drafting another one and classify it as adequate canonical guidance, incomplete canonical guidance, legacy/runtime-bound guidance, or conflicting guidance.

Ask the user to choose the treatment whenever a change is needed:

- Preserve and assess only.
- Augment the existing file with verified missing project facts.
- Merge a proposed delta while retaining existing rules that remain valid.
- Migrate runtime-bound material into an explicit adapter and keep the portable project contract in AGENTS.md.
- Replace exact sections or the entire file only with explicit approval and a stated preservation or migration plan.

Do not create a second competing entry point. Follow [the AGENTS.md specification](agents-md-spec.md) to judge whether the file is operationally sufficient.

## Maturity choices

Use these neutral choices when the user has not specified the desired depth:

| Level | Outcome |
|---|---|
| Baseline | A minimal canonical entry point and the smallest evidence-backed skill set for immediate use. |
| Focused | A named capability or bounded set of skills with project facts, verification, and required references. |
| Comprehensive | A repository-wide evidence scan, a deliberately selected skill library, relevant templates or helpers, and a documented evidence review. |

The user may choose another level or describe an outcome directly. Do not treat comprehensive as the default.

## Initial construction

When no canonical project skill system exists:

1. Ask for the current operation and desired outcome.
2. Confirm the target project and maturity if they are not already clear.
3. Confirm the knowledge or documentation destination and the intended treatment of delivery records and extracted knowledge.
4. Identify only the constraints that affect safe generation.
5. State a compact intent summary, then begin the evidence pack.

Do not create a broad default library merely because a user invoked the builder.

## Repeat activation

Treat an existing AGENTS.md, .agents/skills/ directory, prior delivery record, or repeated builder request as a possible re-entry. First state the read-only orientation, then ask the user to choose the operation when it is not explicit.

Default to preservation. Do not regenerate, replace, or expand existing skills solely because the builder was invoked again. Distinguish these user choices:

- Assess: report the current library and gaps without changing it.
- Repair: correct an identified defect while preserving the approved boundary.
- Extend: add or improve a named capability without rewriting unrelated skills.
- Migrate: change canonical layout or runtime adaptation only with an explicit migration scope.
- Regenerate or replace: identify exact targets and obtain explicit approval before overwriting.

When the user asks to continue a previously described change, restate the known scope and ask only about unresolved choices or any broadened scope.

## Intent summary and gate

Before the evidence scan, keep a concise summary in the active delivery:

~~~text
Operation:  initialize / assess / repair / extend / migrate / review / plan
Target:     project, skill, template, adapter, or document boundary
Maturity:   baseline / focused / comprehensive / user-defined
Preserve:   existing assets to retain, or “none known”
AGENTS.md:  preserve / augment / merge / migrate / replace / not present
Knowledge:  existing location and rules, new project area, external location, or not requested
Records:    separate location, knowledge-base location, or not requested
Capture:    reusable knowledge extraction enabled / disabled / undecided
Done when:  observable result and verification expectation
Open:       material question, constraint, or explicit assumption
~~~

Do not generate until this summary is confirmed by the user or materially complete from the user’s explicit request. Record an unresolved low-impact assumption; ask the owner before assuming a fact that changes scope, compatibility, authority, or acceptance.

## Verification

Use [the evidence-review guide](evidence-review.md) to examine whether the consultation gate was satisfied. Do not claim that a document check proves the user’s intent was confirmed.
