---
name: bug-fix
description: Correct an existing behavior that violates an intended result; reproduce the defect, trace its cause, and verify the same user-visible behavior after the fix.
---

# Bug Fix

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user asks to fix a defect in existing behavior. It is available automatically for bug fixes and through {{INVOKE}}bug-fix. First establish the intended and observed behavior from the request, contract, or existing evidence. Reproduce the issue at the affected surface when practical, then form a root-cause explanation supported by source and observations. Do not force destructive conditions or fake a reproduction; if it cannot be reproduced, state what was and was not established.

Use the TDD workflow only when the behavior is clear and a practical existing regression-test path applies. Otherwise follow the user's testing instructions and verify with a focused check against the affected artifact. Make the smallest root-cause correction, then repeat the same reproduction under comparable conditions and inspect relevant neighboring behavior. Never report a check as passed unless it ran and produced that result.

Follow {{GLOBAL_INSTRUCTIONS}}. Keep one primary workflow and add only relevant supporting steps. Handle small, sensitive, or algorithmically subtle fixes inline; use one native worker for substantial, understood, bounded implementation. The brief must require reading {{GLOBAL_INSTRUCTIONS}} and this SKILL.md in full, and state file scope, starting state, constraints, expected artifact, and finish check. Inspect the actual diff. Do not expand a fix into unrelated cleanup or behavior changes.
