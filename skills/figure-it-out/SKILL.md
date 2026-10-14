---
name: figure-it-out
description: Plan and carry out genuinely complex, unusual, or cross-cutting work requiring coordinated phases and unresolved dependencies when a narrow workflow is insufficient. Reuse one proportionate plan. Also use for explicit {{INVOKE}}figure-it-out requests.
---

# Figure It Out

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

The lead may use this workflow automatically when the task needs coordinated phases, unresolved dependencies, or sequencing of consequential unknowns that a straightforward approach cannot handle well. Use judgment; a long file list, many tool calls, or an unfamiliar detail alone is insufficient.

Skip routine edits, clear bounded fixes, ordinary explanations, and narrow clarification questions. Explicit `{{INVOKE}}figure-it-out` requests remain available. If the user asks only for a plan, produce the plan without starting implementation.

Create one plan for the task and reuse it through follow-ups. Update that plan when evidence materially changes the approach; do not restart the workflow or create a new plan for every phase or question. Delegates execute their assigned units rather than starting a nested planning workflow.

## Frame and plan

1. State the desired outcome, scope, constraints, risks, assumptions, and observable finish condition. Inspect the relevant repository or artifact and note its baseline before changing it.
2. Identify the riskiest unknowns and investigate those first. Before implementation, create a reviewable Markdown plan sized to the task, with the outcome, constraints, risks, finish condition, and a phase table listing each phase's output and completion check. Use `.audit/<task-slug>-plan.md` in the current project by default, or the path the user requests. Keep the plan current if evidence materially changes the scope, sequence, or finish condition; log why it changed.
3. Keep brief progress and decision notes in the same plan, including material choices, their reasons, observed checks, and evidence pointers. Creating this plan does not activate Show-me-your-work, create a separate TSV log, or launch an audit reviewer. Use that skill only for a qualifying retrospective request or an explicit request to keep a trail.

Let evidence change the plan. Keep notes about meaningful decisions, checkpoints, failed hypotheses, and results; do not record every tool call. Keep user changes and unrelated files intact. Revert only changes isolated to this task when a failed attempt needs cleanup.

## Work in verifiable units

For each phase, state the working hypothesis, make the smallest useful change, inspect its effect on the real affected surface, and update the plan with the evidence and outcome. Choose checks that fit the risk and the user's instructions; do not force tests or build a new harness merely to follow this workflow. Distinguish inspection, executed checks, and unverified assumptions.

Follow `{{GLOBAL_INSTRUCTIONS}}`, including its code-delegation rule for substantial, understood, bounded implementation work. The lead keeps ownership of framing and design, inspects delegated changes, and is responsible for the final result. Give any worker a bounded brief, file pointers, constraints, finish condition, and the required global-instructions read.

Do not require `{{INVOKE}}how`, `{{INVOKE}}why`, `{{INVOKE}}architect`, `{{INVOKE}}poteto-mode`, or principle skills. For consequential unresolved decisions with credible alternatives, the lead may use Arena after reading `{{SKILLS_ROOT}}/arena/SKILL.md` and applying its automatic-use criteria and repetition limits. Do not treat every phase as a reason for another Arena run. For a bug-fix unit meeting the configured TDD criteria, read `{{SKILLS_ROOT}}/tdd/SKILL.md` and use its focused regression workflow; do not manufacture tests for unrelated units. Interrogate remains explicit. Do not start unrelated investigation, scan other session transcripts, or commit, push, or deploy as an automatic phase.

## Close out

At meaningful phase boundaries and at completion, update the plan's progress notes with actual commands, paths, observations, and outcomes. If the user requested a separate decision trail, follow Show-me-your-work's append-only format and audit rules for that trail. Otherwise do not create or audit a separate log automatically.

Report the plan and material changes briefly, then label the finish condition **VERIFIED**, **NOT VERIFIED**, or **INCONCLUSIVE**. Give the evidence for that label and name any remaining risk, incomplete phase, or check that could not be performed. A planned check is not evidence that it passed.
