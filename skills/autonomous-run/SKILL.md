---
name: autonomous-run
description: Continue an authorized task independently toward a specified outcome, stopping condition, or limit when the user requests sustained execution and follow-through. Also use for explicit {{INVOKE}}autonomous-run requests.
---

# Autonomous Run

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Select automatically from the meaning of the request and current task context when the user delegates sustained, independent execution toward an outcome or stopping condition. Do not require specific words, phrases, or a statement about the user's availability. Explicit `{{INVOKE}}autonomous-run <task>` also applies. Discussing or configuring this workflow does not itself start a run, and an instruction to pause or stop takes precedence.

This changes how the existing task continues. Keep its scope, requested outcome, permissions, and model choices. The lead uses the matching task workflow and applicable global instructions, rather than starting a separate implementation or additional panel. Respect user-specified deadlines, budgets, iteration limits, and later steering.

## Define and drive completion

State the finish condition briefly from the request and existing context. Make it observable on the affected artifact: the original reproduction succeeds, specified behavior is present, or the requested measured result is achieved. Identify genuine missing requirements early; proceed with reversible authorized work and reasonable stated assumptions instead of asking routine implementation questions.

Work in useful increments. Form a hypothesis, make the smallest justified change, inspect the actual result, then continue toward the finish condition. Use the configured TDD and delegation rules when they apply. Do not weaken the finish condition, treat inconclusive evidence as success, or retain unrelated speculative changes. Preserve user edits.

For external progress such as an already-running command or CI result, prefer an available event-aware wait. Otherwise check at a sensible interval, not a busy loop. Waiting for an expected event is not a failed iteration. Do not add watcher agents or scheduled jobs by default.

After repeated attempts make no progress, reassess the cause and approach instead of repeating the same action. Continue other useful authorized work. If a real prerequisite, permission, missing input, unavailable capability, or explicit limit prevents completion, preserve progress and report exactly what remains. Difficulty alone is not a reason to stop.

## Handoff and stopping

Reuse an existing plan or keep a compact handoff note when a long run needs one. Record meaningful changes, checks, outcomes, and the next step; no per-tool diary is needed. This workflow does not automatically activate Show-me-your-work, its TSV trail, or its independent audit. Use those only under their configured request conditions.

When finished, report the result, actual verification, remaining limitations, and artifact paths, then end the turn. If the requested finish includes ending execution, use the available runner's normal completion mechanism. Do not kill the interactive CLI, terminal, or unrelated processes to simulate completion. A skill does not itself close an interactive session, provide a background daemon, or continue after the runtime stops.

Delegating continued execution does not authorize extra commits, publishing, deployment, testing, persistent goals, or global configuration changes. Follow the task's actual authorization and any active goal rules.
