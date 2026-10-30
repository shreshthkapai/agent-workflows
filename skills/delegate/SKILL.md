---
name: delegate
description: Hands the task in its arguments to the `delegate` role's model (Codex by default) as the lead of its own headless session, so the work bills that model's plan, then checks what it changed. Use for /delegate.
disable-model-invocation: true
---

# Delegate

Another model does the task in the arguments, and you check its work. Spend as little of your own context on it as you can. You don't run a playbook for the task. The child does.

1. **Brief.** Write it to a file in your scratch directory. Put in the task as the user typed it, the working directory, and any directive from this session that bears on the task. End with "Leave your changes uncommitted. Do not commit, push, or open a PR." unless the task asks for one of those. Don't read code or plan the task first.
2. **Run.** Start `aw-run delegate --lead --out <file> < <brief>` as a background shell job. Add `--read-only` when the task asks for no edits. `--lead` lets the child run the workflow itself instead of acting as a helper. Tell the user it started and on which model, from `aw-run --resolve delegate`, then keep working with them. If another delegate is still writing in the same checkout, start this one now only when the two tasks touch different files. Otherwise start it when the first exits.
3. **Check.** When the job exits, read the out file, `git status`, and `git diff`. Rerun the checks the report says passed. Don't take the report's word.
4. **Report.** Say in your own words what changed, what you verified, and anything wrong or missing. If it needs a fix bigger than a line, start one fresh delegate the same way, with the original task, the report, and the fix in its brief, then check and report again.

If `aw-run` fails, report its error. Don't do the task yourself.
