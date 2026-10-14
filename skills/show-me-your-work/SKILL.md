---
name: show-me-your-work
description: Explain and audit substantial work when the user asks how it was done or why consequential choices were made across a complex process. Skip narrow clarifications. Also use for explicit {{INVOKE}}show-me-your-work or decision-trail requests.
---

# Show Me Your Work

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

## When to use

Automatically select this skill only when the user asks for a retrospective account of the agent's work, such as "how did you do this?" or "why did you choose this approach?", and the requested explanation concerns a substantive multi-stage process or consequential tradeoffs needing an evidence-based account.

The question's scope matters. A small clarification about one line, command, term, or straightforward choice should receive a direct answer, even if the surrounding project is large. Do not activate for generic how/why questions about a subsystem, ordinary status updates, task completion alone, or every follow-up question.

Explicit `{{INVOKE}}show-me-your-work` requests remain available, including asking for a trail while a task is being performed. Without that request, do not start background TSV logging or an audit merely because a task is long or Figure-it-out is active.

Use one canonical local trail and one audit for the requested body of work. Reuse the report for follow-ups; repeat the audit only when the user asks or new evidence, a distinct substantial scope, or a material unresolved concern warrants it. The lead is the sole log writer; other agents may read but not edit the log.

## Retrospective account

Identify the work the user means from the current thread and referenced artifacts. Reuse an existing task log or plan when available. Explain the important steps, decisions, alternatives and tradeoffs, observed outcomes, and evidence gaps within the question's scope.

If there is no log, compile a retrospective trail only from supported facts in the thread and actual artifacts. Timestamp new rows as the time they are recorded and identify them as retrospective reconstruction; do not invent original event times or present reconstructed notes as a contemporaneous log. Separate recorded reasons from later inference. If the relevant context or execution evidence is unavailable, report the gap rather than inventing actions or claiming a complete audit. Do not scan unrelated conversation history.

## Create and append

For a qualifying retrospective account or an explicitly requested trail, use the user's requested path when supplied. Otherwise use `.audit/<task-slug>.tsv` relative to the current project. Do not overwrite an existing log, commit it, change `.gitignore`, or publish it. Keep a single canonical log for a task.

The exact tab-separated header is:

```text
ts	phase	decision	why	evidence	result
```

For an explicitly requested ongoing trail, append rows as material decisions and checkpoints occur. For a retrospective trail, append only supported decisions and outcomes relevant to the question. Avoid routine tool-call rows. Record actual paths and commands in `evidence`; distinguish observed results from planned checks. If an entry is wrong or later evidence changes it, append a correction that names the superseded entry.

Use the bundled helper, passing the filename first, then `phase`, `decision`, `why`, `evidence`, and `result` as positional arguments:

```sh
python3 "{{SKILLS_ROOT}}/show-me-your-work/scripts/log.py" .audit/task-slug.tsv planning "Check the current behavior first" "A baseline is needed to judge the change" "src/cart.py; python -m app" "Baseline observed: empty cart costs £5"
```

The helper supplies a UTC ISO 8601 timestamp, writes the header on first use, normalizes tabs and newlines inside cells, and prefixes spreadsheet-formula-like cells safely. It locks the log while checking the exact header and appending. If an existing file has a different header, stop and report the conflict; do not replace or repair it in place.

## Audit the record

For the requested account, compare every material claim in the trail with the available task evidence and actual artifacts. For an explicitly requested ongoing trail, perform this audit at handoff. Check that commands were executed before describing their results as observed, that paths point to the relevant artifacts, and that failures, corrections, and verification gaps remain visible. Current artifacts alone cannot prove what happened earlier; identify that limitation when execution evidence is absent.

Use the current session transcript only if its exact transcript is positively identified and available. Otherwise provide the reviewer a clearly labeled lead-authored digest of the goal, actions, results, corrections, dead ends, and constraints; do not imply that the digest is a complete transcript or search unrelated sessions to find one.

Have one independent, read-only audit reviewer inspect the log and referenced evidence. Read `{{MODEL_REGISTRY}}` and `{{RUNTIME_GUIDE}}` to resolve `roles.audit_reviewer` or the host adapter's legacy audit roles. Prefer an available reviewer from a different model family; if that requirement cannot be met, report the incomplete cross-family review. Do not invent a replacement or claim model diversity from independent agents alone. Honor per-run overrides and report the actual model and effort used.

Use a general-purpose native agent with explicit model and reasoning settings, not a preset role that may pin different settings. If the spawning interface supports `fork_turns`, use `fork_turns: "none"` and send a self-contained brief containing the task outcome, log path, referenced artifacts, checks actually run, observed outcomes, constraints, and known gaps. The reviewer must read `{{GLOBAL_INSTRUCTIONS}}` in full and this skill in full before starting, must pass that same global-read requirement to any native agent it spawns, and must spawn no agents or write files. Let speed follow the parent session.

Ask the reviewer only to check whether the log matches the supplied run evidence and artifacts, whether verification claims have evidence, and whether risky decisions or material gaps are missing. Label claims supported only by the lead-authored digest so they are not mistaken for independently observed execution. Do not ask it to redo the task or run tests without the user's explicit testing or verification request. If the model family cannot be determined, the runtime or capacity cannot supply the reviewer, or the review is incomplete, say so plainly; do not claim an independent or cross-family audit that did not happen.

Close with a short **Attention** section naming the actual reviewer model and concrete flags, or saying no material flags were found. Include unresolved evidence gaps. The lead remains responsible for the log and final claims.
