---
name: reflect
description: Reflect on completed work in the current conversation to identify durable lessons and propose concrete improvements to existing skills. Use when the user explicitly requests reflection.
---

# Reflect

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use only when the user explicitly asks for reflection or lesson capture. Review completed work for reusable changes to existing skills. A successful task does not need a lesson: skip trivial, one-off, already-covered, or weakly supported observations.

Invoke `{{INVOKE}}reflect on this task` in the thread where the work happened. Installing or updating this skill does not itself execute reflection.

## Gather evidence and review independently

Default to the current conversation and artifacts already identified for the work. Build a compact factual brief for the reviewers covering the goal, actions, observed results, user corrections, dead ends, and constraints, with evidence pointers. No saved transcript or history search is required. Label missing or compacted context rather than reconstructing it as fact.

Read a saved transcript only when the user supplies it or explicitly requests that source, and only after identifying the exact relevant session. Do not discover or mine unrelated conversations. If invoked in a fresh thread without task context, request the relevant task summary or artifacts instead of searching history automatically.

Read `{{MODEL_REGISTRY}}`. Send the same evidence and candidate lesson scope to three independent, read-only reviewers with these lenses and role keys:

| Lens | Registry role |
| --- | --- |
| Judgment | `roles.reflect_judgment` |
| Tooling | `roles.reflect_tooling` |
| Divergent challenge | `roles.reflect_divergent` |

Resolve each role alias through the `models` table to obtain `model` and `reasoning_effort`. If a required default cannot be resolved, report the issue rather than inventing a replacement; complete explicit per-run overrides may supply the settings. Different effort levels alone do not make different model families.

Use general-purpose native agents with explicit model and reasoning settings, not preset roles that may pin different settings. Honor explicit per-run overrides; if the runtime cannot honor one, report the actual roster and the missing review without silently substituting. If the spawning interface supports `fork_turns`, use `fork_turns: "none"` and give each reviewer a self-contained brief. Launch the three reviews independently when capacity permits. Do not change global defaults or speed; speed follows the parent session.

Every reviewer must read `{{GLOBAL_INSTRUCTIONS}}` and `{{SKILLS_ROOT}}/reflect/SKILL.md` in full before starting, then execute only its assigned review lens. Pass the same global-read requirement to any native agent it spawns. Reviewers must spawn no agents, write no files, and inspect only the supplied task evidence and relevant skill files. If fewer than three reviews complete, identify the dropped lens and model; do not present the review as complete.

Ask every reviewer to return only evidence-backed candidates. For each, identify the exact existing skill and section, quote the observed trigger or failure, propose a concrete narrow edit, explain when the new instruction should apply, and state its tradeoffs. The judgment lens prioritizes durable quality lessons; the tooling lens looks for structural enforcement such as a helper or lint where suitable; the divergent lens challenges the framing and suggests a safer or simpler alternative. These are distinct perspectives over the same evidence, not permission to invent lessons.

## Synthesize proposals

As lead, inspect the cited evidence and synthesize the reviews using the current model; do not add a redundant judge. Classify each candidate as **Accepted**, **Rejected**, or **Backlog**, with a short evidence-based reason. Prefer one narrow improvement to an existing skill and avoid creating new skills for a single incident. Prefer structural enforcement over more global prose when it directly prevents a demonstrated repeat problem. Preserve existing activation, model, and global settings.

Prepare reviewable proposed edits first, as concise diffs or exact replacement text naming the target skill and section. Invoking this skill authorizes analysis and proposals, not applying them. Apply durable skill changes only after the user explicitly authorizes applying the lessons or chooses edits from the concrete proposal. Do not create tickets, send messages, or alter unrelated files. If the user authorizes edits, follow the skill-creator workflow and validate the changed skill structure; do not add or run tests unless the user requests testing or verification.

Report the actual reviewer models and efforts, accepted/rejected/backlog proposals with evidence and tradeoffs, any concrete edit text, and incomplete reviews. State clearly which files were actually changed; do not imply that a proposal was applied.
