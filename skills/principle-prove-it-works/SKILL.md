---
name: principle-prove-it-works
description: "Verify completed work against the affected artifact and report what the evidence does and does not show."
---

# Prove It Works

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Choose checks that observe the actual behavior or artifact changed by the task. Inspect the diff and relevant output; exercise the affected path when practical and authorized. Compilation or a passing proxy check alone may not show that the user-visible result is correct. Use focused existing checks within the user’s testing authorization; add tests only when the user or applicable workflow authorizes them. Distinguish inspection from commands actually run. Report failed, unavailable, or inconclusive checks honestly, including any limits on what they establish. Do not treat a plan, tool output summary, or another agent’s self-report as evidence in place of the artifact.
