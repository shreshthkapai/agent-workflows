---
name: principle-subtract-before-you-add
description: "Simplify the affected area before adding behavior when existing complexity is proven unnecessary."
---

# Subtract Before You Add

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

When evolving an area, look for related complexity that can be removed before building on top of it. Remove a branch, wrapper, duplicate source of truth, or stale reference only when inspection shows it is unnecessary for current behavior and contracts. Preserve security checks, validation, and fallback behavior that protect real invariants. Avoid designing for speculative usage or adding guards beyond actual requirements, but retain runtime checks for inputs or state that can still be invalid. Keep subtraction within the requested scope and verify that the remaining behavior still meets the affected contract.
