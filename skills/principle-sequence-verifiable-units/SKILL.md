---
name: principle-sequence-verifiable-units
description: "Break substantial multi-step work into coherent checkpoints that can be checked before continuing."
---

# Sequence Verifiable Units

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

For a migration, sweep, or multi-part change, choose checkpoints that are meaningful and easy to review. Check a unit before building further on it when that catches failures cheaply, but do not demand a test after every line or mechanical edit. Preserve the intended order of the workflow, including an expected failing test in a red-to-green fix. Use intermediate checks that match the state of that phase and finish with checks for the requested outcome. Commits, rebases, stacked changes, and pull-request ordering are delivery choices, not requirements of this principle.
