---
name: multi-phase-plan
description: On explicit request, sequence substantial work across coordinated phases or proposed PRs, recording dependencies, compatibility transitions, and delivery boundaries in one reusable plan.
---

# Multi-phase Plan

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use only when the user explicitly requests this workflow, through `{{INVOKE}}multi-phase-plan` or a clear request to use this specific skill. Do not select it automatically because a task is large or has dependencies. When requested, infer useful phase boundaries from the task and repository without fixed file counts.

The lead owns one plan for the task. If Figure-it-out or another workflow already has a suitable plan, add the needed sequencing there instead of creating a second artifact or restarting planning. Figure-it-out handles consequential unknowns and unusual coordination; this skill supplies phase structure. Do not invoke either solely because the other is active. Delegates execute assigned units without starting another planning workflow.

## Build a useful sequence

Inspect the relevant starting state, affected data shapes, callers, and contracts. State the outcome, scope, constraints, and observable finish condition. Organize phases around coherent outcomes and real dependencies, not arbitrary file or function quotas. Prefer phases that leave a coherent, usable state; identify intermediate states that cannot safely ship alone.

Keep a concise Markdown plan at the user-selected location, reuse the existing task plan, or use `.audit/<task-slug>-plan.md`. For each phase record its outcome, affected artifacts or contracts, prerequisites, completion evidence, and status. Note compatibility transitions and rollback needs when relevant. Describe proposed PR boundaries only when useful to the requested delivery; planning does not create, commit, or publish them.

Use the fewest phases that make dependencies and checks clear. Record important unknowns and resolve those that could invalidate the sequence before dependent work. Update the same plan when evidence changes dependencies, scope, or approach; do not replan at every follow-up, announce every small step, or create a separate log or review panel automatically.

## Respect scope and track results

For a planning-only request, deliver the plan and stop. For an authorized implementation task, continue through its existing workflow and record actual phase outcomes. Keep proposed checks distinct from observed results; unavailable verification remains a gap. Phase completion does not by itself demonstrate the overall finish condition.

Follow `{{GLOBAL_INSTRUCTIONS}}` for delegation, verification, and authorization. This skill does not itself require extra agents, tests, commits, PRs, or deployment.
