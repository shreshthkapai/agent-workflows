---
name: principle-migrate-callers-then-delete-legacy-apis
description: "Update in-scope internal callers before removing an obsolete API when compatibility permits."
---

# Migrate Callers Then Delete Legacy Apis

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

When replacing an internal API, inventory its callers and identify any external consumers or compatibility promises. Update the internal callers that are within scope, then remove the old path only when no required consumer depends on it and the migration can be delivered coherently. Retain an adapter or migration period when a public contract, staged rollout, or user requirement calls for it. Update checks to reflect the intended contract, but do not delete behavior tests merely because they exercise the old implementation. Keep any staged migration reversible and report callers or dependencies that cannot be safely changed in this task.
