---
name: principle-fix-root-causes
description: "Debug a reproduced failure by tracing its cause before changing code or state."
---

# Fix Root Causes

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

When practical, reproduce the reported failure and follow the relevant inputs, state changes, and control flow until the cause is supported by evidence. Fix that cause within the requested scope, then repeat the same observation to verify the behavior. A guard is appropriate when it enforces a real contract or handles a valid failure mode; do not add one solely to hide a symptom. For restart-related failures, inspect persisted state as well as code. Investigate nearby patterns only when evidence or task scope justifies it; one bug report does not authorize a repository-wide cleanup.
