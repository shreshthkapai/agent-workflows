---
name: principle-separate-before-serializing-shared-state
description: "Prevent concurrent writers from racing by separating ownership or enforcing real synchronization."
---

# Separate Before Serializing Shared State

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Identify the files, branches, records, or objects that concurrent actors may mutate. Prefer independent work areas and owned outputs when actors can produce separate results, then combine them at a deliberate boundary. If one shared mutable object is a real requirement, use an enforced mechanism such as a lock, transaction, compare-and-set, or single-writer sequence appropriate to its storage. Instructions to take turns do not provide mutual exclusion. Follow repository and task isolation rules, and verify that the chosen mechanism actually covers the conflicting writes and failure cases.
