---
name: refactoring
description: Restructure code while preserving its existing observable behavior and contracts.
---

# Refactoring

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the requested outcome is a code or module restructure without a behavior change. It is available automatically for refactoring and through {{INVOKE}}refactoring. Establish the current contract and observable outputs first, then identify the module or data shape the change should clarify. Make small, reviewable structural edits and update internal callers, configuration references, and string-based references as needed.

Check whether a symbol or interface has external consumers before changing or removing it; preserve public compatibility unless the request explicitly changes the contract. Compare the refactored artifact's behavior with its prior behavior using existing checks or focused observations appropriate to the task. Compilation by itself does not demonstrate behavioral preservation. Follow the user's testing instructions; do not require a new test suite or harness.

Follow {{GLOBAL_INSTRUCTIONS}}. Keep one primary workflow and only relevant supporting steps. Handle small or sensitive refactors inline; use one native worker for substantial, understood, bounded work. The brief must require reading {{GLOBAL_INSTRUCTIONS}} and this SKILL.md in full, and state file scope, starting state, constraints, expected artifact, and finish check; inspect the actual diff. Keep newly discovered bugs or feature changes outside the refactor unless the user expands scope. Preserve user changes and do not automatically revert work.
