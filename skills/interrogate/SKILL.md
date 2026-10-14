---
name: interrogate
description: Independently review a code change with several models, then synthesize evidence-backed findings about correctness and code quality. Use only for an explicit {{INVOKE}}interrogate or Interrogate review request.
---

# Interrogate

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Run only when the user explicitly requests Interrogate, such as `{{INVOKE}}interrogate the fix you just made` or "use Interrogate to review this branch." Produce a review report. Do not apply fixes, refactor code, commit changes, or publish review comments as part of this workflow.

## Review models

Read `{{MODEL_REGISTRY}}` and launch one independent native subagent for each alias in `roles.interrogate_reviewers`. Resolve aliases through the `models` table to obtain `model` and `reasoning_effort`. If a required default cannot be resolved, report the issue rather than inventing a replacement; complete explicit per-run overrides may supply the settings.

Different reasoning settings do not constitute different model families. Report the actual roster and its diversity accurately. The lead session synthesizes the findings using its current model; no additional judge is required.

Honor explicit per-run overrides. Use general-purpose native agents with explicit model and reasoning settings rather than preset roles that pin conflicting settings. If the spawning tool exposes `fork_turns`, use `fork_turns: "none"` when supplying overrides and give each reviewer a self-contained brief. Speed follows the parent session. Do not change global model, speed, or agent defaults.

If the runtime cannot honor a requested model or effort, report the limitation without silently substituting. Continue with available reviewers when useful, recording failures and the actual roster. With fewer than two completed independent reviews, report that the multi-review comparison is incomplete.

## Establish the scope and intent

- An explicit diff, commit, PR, or file selection takes precedence.
- For "the fix you just made," use conversation context to identify the fix, then inspect the actual code and changes. Context identifies the target; it is not evidence that the implementation is correct. Exclude unrelated working-tree changes.
- For a branch review, identify the appropriate base and review changes from the merge base. Include relevant staged, unstaged, and untracked changes only when they belong to the requested scope.
- For an older fix, resolve the referenced commit or artifact and follow the surrounding code needed to understand it. If the target cannot be established, request the missing identifier rather than guessing.

State the scope and intended behavior briefly, including any unresolved assumptions. Collect one shared diff or code snapshot and relevant context paths so every reviewer starts from the same changes. Use file pointers for large artifacts rather than duplicating full transcripts. Reviewers may follow callers, callees, types, and existing checks to substantiate findings.

## Independent review

Launch reviewers together when capacity permits. Give every reviewer the same scope, intent, artifact pointers, constraints, rubric below, and required finding format. Do not assign different personas or show other reviewers' findings.

Include these instructions in every reviewer task:

- Before starting work, read `{{GLOBAL_INSTRUCTIONS}}` and `{{SKILLS_ROOT}}/interrogate/SKILL.md` in full and follow applicable repository instructions. Execute only the assigned review scope. Pass the same global-read requirement to any native agent you spawn.
- Do not spawn agents. Review only: do not modify files, apply fixes, commit, or perform external writes. Use a read-only sandbox when the runtime supports one.
- Trace suspected issues through actual code. Report concrete evidence and conditions under which the problem occurs. Do not invent defects to fill a quota; a review with no substantiated findings is valid.
- Do not add or run tests unless the user has explicitly requested testing or verification. Inspect existing checks and evidence, and clearly distinguish inspection from executed verification.
- Return findings to the lead without writing a separate report file.

Apply the following lenses where relevant:

- **Correctness and regressions:** intended behavior, edge cases, error paths, state transitions, concurrency, retries, and idempotency.
- **Root cause:** whether a fix restores the underlying contract or hides an invariant violation. Inspect the surrounding execution path.
- **Structure and data model:** ownership, module boundaries, validation at entry points, clear types, and integration with existing patterns.
- **Complexity and maintainability:** unnecessary branches, wrappers, duplicate helpers, obsolete compatibility paths, and simplifications that remove moving parts. Explain concrete maintenance costs; avoid cosmetic nits and speculative abstractions.
- **Security:** substantiate input-to-sink paths, authorization gaps, or exposed secrets. Keep sensitive values out of the report.
- **Verification evidence:** whether existing checks cover the changed behavior and failure cases. Missing evidence is a gap, not proof of a bug.

For each finding, provide a concise title, location, impact or severity, evidence or execution path, triggering conditions, and a suggested correction or simplification. Separate demonstrated defects from optional improvements and uncertain concerns.

## Lead synthesis and report

Inspect the relevant code behind material findings yourself. Deduplicate reports of the same underlying issue and record which reviewers raised them. Agreement supports confidence but does not establish correctness; a well-supported finding from one reviewer still matters. Resolve disagreements from evidence and label remaining uncertainty.

Categorize findings with a brief rationale:

- **Act on:** substantiated correctness, security, regression, or material maintainability problems within the task's goals.
- **Consider:** worthwhile improvements whose benefit depends on tradeoffs.
- **Noted:** valid observations with low immediate impact.
- **Dismissed:** unsupported, incorrect, cosmetic, or missing-context findings, with the reason.

Return the report in chat by default. Include scope and intent, the actual reviewer models and efforts, prioritized actionable findings with file references, other material categories, agreement or disagreement, and verification limits. Empty categories may be omitted. Do not claim approval solely because several reviewers agreed or found nothing.

Write a Markdown document only when the user requests one. Use the requested path; if they ask for a document without a path, choose a sensible local location and report it. The lead writes the synthesized report, not separate reviewer reports. Record incomplete reviews plainly. Remove only temporary artifacts created for this review.
