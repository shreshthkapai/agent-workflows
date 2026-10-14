---
name: arena
description: Compare credible competing approaches for consequential, unresolved design or implementation decisions where choosing poorly would be costly and direct investigation cannot settle the tradeoff. Also use for explicit {{INVOKE}}arena or approach comparison requests.
---

# Arena

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use Arena when the user explicitly asks for a comparison, or when the lead judges that a consequential decision meets the automatic-use criteria below.

Invoke explicitly as `{{INVOKE}}arena <task>` or "use Arena for this." Explicit requests do not need to meet the automatic-use criteria. Respect a user's instruction to avoid Arena or additional agents.

## Automatic use

The lead may initiate Arena without asking permission when all of these hold:

- There is an unresolved choice between at least two credible approaches, with materially different designs or tradeoffs.
- Choosing poorly could cause substantial rework or affect important correctness, performance, ownership, or compatibility constraints. Examples include a costly architectural boundary, a major migration strategy, or competing concurrency designs.
- Existing context and focused inspection leave a genuine tradeoff; reading the code or a cheap permitted observation would not adequately settle it.
- The comparison has a bounded artifact and concrete success criteria within the user's task.

Before spawning, briefly announce the decision being compared and why independent candidates are useful. Choose design sketches or proposals when those can settle the decision; build full competing implementations only when their behavior is needed to choose.

Keep use proportional:

- Skip routine edits, mechanical refactors, familiar patterns, obvious fixes, wording choices, and questions answerable by direct investigation. Task size or difficulty alone is not a trigger.
- Normally make one automatic Arena run per task. An additional run needs a materially distinct consequential decision or new evidence that invalidates the earlier framing; state that reason before launching. Do not repeat a settled comparison merely for reassurance.
- Only the lead initiates automatic runs. Candidates, judges, and other delegates must not start nested Arena runs.
- Keep the default two runners and one judge. Add candidates only for an explicit request or an additional credible approach that the comparison needs; explain the expansion.
- Reuse the comparison's result as work continues. Arena selection alone does not authorize tests; a bug-fix task may independently qualify under the user's configured TDD policy. Automatic selection does not authorize external actions or edits beyond the user's task.

## Model roles

- Read `{{MODEL_REGISTRY}}`. Default to two candidate agents using `roles.arena_runner` and one judge using `roles.arena_judge`; resolve each alias through the `models` table to obtain `model` and `reasoning_effort`.
- If a required default cannot be resolved, report the configuration issue rather than inventing a replacement. A complete explicit per-run override may supply the missing settings.
- These settings apply only to this Arena run. Do not change the user's global Codex model or subagent defaults.
- Respect model or reasoning-effort choices the user gives for a particular run. If the subagent tool cannot honor a requested setting, report that and do not silently substitute another model.
- Use native general-purpose native agents with explicit model and reasoning settings, rather than preset worker or reviewer roles that pin conflicting settings. If the spawning tool exposes `fork_turns`, use `fork_turns: "none"` when supplying overrides and provide a self-contained task brief with file pointers.

## Frame and run candidates

1. Identify the requested artifact, goal, constraints, and what a useful result must satisfy. Build a short evaluation rubric with three to six concrete criteria from that intent.
2. Give every candidate the same task brief and relevant context. Give each candidate a distinct output location. Candidates should not see or discuss one another's work and must not spawn more agents.
3. For code changes, use a separate worktree or isolated checkout per candidate with equivalent starting states. Include relevant uncommitted changes in that state; a checkout of HEAD alone omits them. Identify the base and any exclusions before launching. Candidates must not edit the shared target checkout or manipulate shared Git references concurrently. If isolation is unavailable, ask candidates for separate patch files or proposals and report what was not executed. For design-only work, use separate proposal files.
4. Include this instruction in every candidate and judge task: read `{{GLOBAL_INSTRUCTIONS}}` and `{{SKILLS_ROOT}}/arena/SKILL.md` in full before starting, then execute only the assigned candidate or judge scope. Pass the same global-read requirement to any native agent spawned from that task.
5. Launch all candidates together with the resolved runner model and effort. Ask each for its artifact and a short rationale naming the main alternative it rejected.

If a candidate fails, record the failure and compare the completed artifacts. With fewer than two usable candidates, report that the comparison is incomplete; do not present a sole candidate as a comparative winner.

## Judge and synthesis

After all candidates finish, launch one judge with the resolved judge model and effort. Give it the rubric and candidate outputs labeled neutrally, without the candidates' reasoning-effort settings. Ask it to score each criterion, identify tradeoffs, and recommend a base. The judge must not edit candidate artifacts or the target checkout.

Read every candidate yourself as well. Use the judge's comparison as evidence, then select the strongest base. Graft compatible ideas only when they improve the result; do not average designs that conflict. Apply the selected synthesis to the user's target checkout while preserving unrelated work.

Check the synthesized result against the requested finish condition. Report the actual runner and judge models and efforts, chosen base, useful grafts, rejected alternatives, verification evidence, and anything left unverified. Clean up only temporary worktrees and files created for this Arena run.
