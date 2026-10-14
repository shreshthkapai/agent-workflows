# Portable operational rules

Installed invocation metadata and the user’s directions control activation. This document describes conditional behavior, not permission to activate every referenced skill. Read `{{RUNTIME_GUIDE}}` to interpret model roles and native agent settings for the chosen host. Referenced task skills may be absent in a selective installation; use available capabilities directly and report missing specialized steps instead of installing or enabling them automatically.

# Workflow rules

These are the detailed rules referenced by the global instruction file. Read only the sections relevant to the current action:

- Task routing or invocation questions: Task workflows and Workflow skills.
- Implementation delegation: Code delegation.
- Concurrent writers: Parallel writers.
- Arena, Interrogate, Reflect, or decision-trail reviewer model selection: Model roles.

User directions take precedence. These rules preserve the existing workflow configuration; consulting them does not activate every workflow.

## Code delegation

These rules apply when acting as the lead agent. Explicit user directions and workflow-specific delegation, such as Arena, take precedence over this default.

- For substantial implementation work with an understood design, a clear finish condition, and a bounded edit scope, delegate to one native `worker` subagent. Announce the delegated scope briefly.
- Handle small edits, unresolved architectural decisions, and work requiring subtle algorithmic or concurrency reasoning directly in the lead session.
- Give the worker the task, relevant file pointers, constraints, and finish condition, including the requirement to read `{{GLOBAL_INSTRUCTIONS}}` in full. Use its configured model and reasoning effort; let its speed follow the parent session.
- Include the starting state, assigned edit scope and output location, expected artifact, and known verification limits in the brief. If the scope or design must expand, the worker reports the evidence to the lead before expanding it.
- Use one implementation worker at a time for a task. Avoid duplicate delegation and concurrent edits to the worker's assigned files. Workers implement their assigned scope themselves without spawning agents.
- The lead owns the result: inspect the actual changes and verify the affected behavior before declaring completion. If the worker fails or its result needs substantial rework, take over directly.

## Parallel writers

- Before launching concurrent writers, give each its own Git worktree, isolated checkout, or separate patch/proposal output. Do not let them write into the same target checkout; readonly reviewers may share the same artifact.
- Give competing writers equivalent starting states, including relevant uncommitted changes. Identify the base and any exclusions explicitly; a worktree created from HEAD alone does not include working-tree edits.
- Confine writes to assigned locations and avoid concurrent operations on shared Git references. The lead inspects each actual diff and applies the selected result sequentially while preserving unrelated user changes.
- If implementation isolation is unavailable, use separate patches or proposals and report what was not executed. Clean up only task-created artifacts and worktrees after preserving the selected result and evidence.

## Model roles

- `{{MODEL_REGISTRY}}` is the shared model-role registry for Arena, Interrogate, Reflect, and decision-trail audits. Read it when spawning one of those workflows and resolve its role aliases through the models table. This is workflow data consumed by the skills; native implementation settings remain in the referenced worker profile.
- Explicit per-run model choices take precedence over workflow defaults. Use general-purpose native agents when supplying model and reasoning overrides; preset profiles can pin conflicting values. If the spawning interface exposes `fork_turns`, use `fork_turns: "none"` with overrides and a self-contained brief.
- Let speed inherit from the parent session. Report the actual model and effort used, and any rejected setting or missing reviewer; do not silently substitute models or claim a review that did not happen.

## Task workflows

- For code and system work, the lead selects the workflow that matches the requested outcome and reads its skill in full. These skills support automatic selection and explicit `{{INVOKE}}skill-name` requests. Prefer one primary workflow with relevant supporting steps; do not launch every workflow or reread it for every follow-up.
- The user's scope is authoritative. A diagnosis or explanation request does not authorize source fixes. Delegates perform their assigned steps without starting nested task workflows or spawning additional agents.

| Requested outcome | Skill |
| --- | --- |
| Explain existing behavior without changing code | `{{SKILLS_ROOT}}/investigation/SKILL.md` |
| Correct a defect and repeat its reproduction | `{{SKILLS_ROOT}}/bug-fix/SKILL.md` |
| Improve measured performance against a baseline | `{{SKILLS_ROOT}}/performance/SKILL.md` |
| Diagnose a live runtime signal | `{{SKILLS_ROOT}}/runtime-forensics/SKILL.md` |
| Analyze an existing captured profile or trace | `{{SKILLS_ROOT}}/trace-forensics/SKILL.md` |
| Implement new or changed behavior | `{{SKILLS_ROOT}}/feature/SKILL.md` |
| Restructure while preserving behavior | `{{SKILLS_ROOT}}/refactoring/SKILL.md` |
| Settle a question with a small permitted experiment | `{{SKILLS_ROOT}}/prototype/SKILL.md` |
| Match a visual reference or preserve appearance | `{{SKILLS_ROOT}}/visual-parity/SKILL.md` |

## Workflow skills

- When the user's intent is sustained, independent execution of an identified task toward an outcome or stopping condition, read `{{SKILLS_ROOT}}/autonomous-run/SKILL.md` and use its finish-condition and handoff rules. Infer intent from context without requiring particular keywords or phrases. Explicit invocation also works. Reuse the task's existing workflow, avoid routine confirmation questions, and stop with an honest result or real blocker report; continued execution does not expand scope or create a background runtime.
- For genuinely complex, unusual, or cross-cutting work needing coordinated phases or unresolved dependencies, read `{{SKILLS_ROOT}}/figure-it-out/SKILL.md` and use one reusable plan. Skip routine work and narrow clarifications; do not restart planning at every phase or follow-up.
- Multi-phase plan remains installed but explicit-only. Read `{{SKILLS_ROOT}}/multi-phase-plan/SKILL.md` only when the user explicitly requests that workflow. Figure-it-out continues to support automatic planning under its own criteria and must not automatically invoke Multi-phase plan. When explicitly used together, reuse one plan; a planning-only request does not authorize implementation or PR creation.
- Use `{{SKILLS_ROOT}}/show-me-your-work/SKILL.md` when the user asks how substantial work was done or why consequential choices were made across a complex process, or explicitly requests a decision trail. Small clarifications get a direct answer. Do not auto-create TSV logs or launch trail audits merely because a task is long or Figure-it-out is active; label retrospective reconstruction and evidence gaps honestly.
- Use `{{SKILLS_ROOT}}/reflect/SKILL.md` only when the user explicitly requests reflection. Prepare concrete improvement proposals; apply durable skill changes only when the user authorizes them.
- Arena supports explicit requests and automatic use by the lead for consequential unresolved decisions with credible alternatives. Read `{{SKILLS_ROOT}}/arena/SKILL.md` and apply its criteria and repetition limits before an automatic run; ordinary difficulty alone is insufficient.
- TDD supports explicit requests and automatic use for bug-fix implementation with clear intended behavior and a practical existing regression-test path. Read `{{SKILLS_ROOT}}/tdd/SKILL.md` and apply its criteria. The user's automatic-TDD preference authorizes focused regression tests and relevant nearby checks for those fixes; respect any later limits or instruction to skip testing.
- Interrogate remains explicit-only. Automatic workflows do not authorize unrelated testing, committing or publishing artifacts, or changing global configuration.
