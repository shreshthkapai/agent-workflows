---
name: tdd
description: Fix a bug with a clear intended behavior and a practical existing regression-test path by demonstrating a failing test before the fix and a passing test afterward. Also use for explicit {{INVOKE}}tdd or test-driven bug-fix requests.
---

# TDD Bug Fix

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use for explicit `{{INVOKE}}tdd` requests, or automatically for a bug-fix implementation task that meets the criteria below. The user's request to enable automatic TDD provides standing authorization for the focused regression test and relevant nearby test runs within that bug fix. Respect any later instruction to skip tests or limit execution.

## Automatic use

Use automatically when the intended behavior is clear, the defect has a narrow observable reproduction, and the existing local test setup provides a practical path to a meaningful failing test. Briefly identify that check before starting; no separate confirmation is needed.

Keep the work focused:

- Skip automatic TDD for read-only investigations, review reports, prose changes, or tasks without a clear bug to fix.
- Do not force a test requiring a new harness, substantial unrelated fixtures, brittle mocks, slow external infrastructure, or uncontrolled production state. Use the fallback below and explain the limit.
- Use one focused regression path per distinct bug or behavior. Reuse the check as work continues rather than repeatedly starting TDD or adding duplicate tests at each phase.
- Automatic TDD authorizes the focused regression work, not unrelated coverage expansion or an automatic full-suite run. It does not grant permission for external writes or changes outside the task.

Explicit `{{INVOKE}}tdd fix this bug` remains available even when automatic selection would skip the task. Assess practicality honestly and explain a fallback if a useful failing test cannot be demonstrated.

Follow applicable global engineering and code-delegation instructions. This skill does not prescribe additional agents or override model settings. If implementation is delegated, include this skill's full-read requirement and the focused test scope in the worker brief. The agent implementing the fix owns the failing-before and passing-after evidence; the lead checks that evidence and the actual changes before declaring completion.

## Workflow

1. Identify the intended behavior, observed failure, affected path, and smallest useful reproduction. Trace the defect to its root cause.
2. Choose the narrowest practical executable check, preferably using the existing unit, component, integration, or regression-test setup. Do not build a new harness merely to satisfy this workflow.
3. Write the smallest test expressing the intended behavior before changing production code. Avoid coupling it to incidental implementation details.
4. Run that test against the unfixed implementation. Confirm it fails for the bug's intended reason. If it passes or fails because of setup, imports, or another unrelated problem, correct the reproduction before editing production code. Do not claim failing-before evidence until it has been observed.
5. Make the smallest production change that fixes the underlying defect while preserving nearby contracts.
6. Rerun the same regression test and confirm it passes. If it still fails, investigate rather than weakening the assertion.
7. Run focused adjacent checks when the changed behavior warrants them. Keep validation proportional to the affected scope rather than automatically running a full suite.

## When a test is impractical

Before changing production code, explain why a useful regression test is unavailable or disproportionate. Examples include brittle mocks, substantial unrelated fixtures, slow external infrastructure, production-only state, or nondeterministic reproduction.

Use the closest practical executable check, such as a targeted command, script, browser reproduction, or integration scenario. Capture before-and-after evidence where possible. Do not force a poor test or claim a manual check is an automated regression test. If the failure cannot be reproduced or the result remains inconclusive, report that limit explicitly.

## Guardrails

- Do not change expected results to accommodate incorrect behavior or weaken existing assertions unless the intended behavior genuinely changed.
- Keep the regression check focused on the reported defect; avoid unrelated coverage expansion or broad fixture churn.
- For flaky failures, control the triggering conditions where practical and state any remaining nondeterminism.
- Preserve unrelated work. If the fix already exists, do not destructively undo it to manufacture failing-before evidence; use an isolated reproduction when practical, or explain that the original failure was not demonstrated.

## Report

Report the changed behavior, root cause, regression-check location, exact commands run, observed failure before the fix, passing result afterward, and any adjacent validation. State clearly when failing-before evidence or final verification was unavailable or inconclusive.
