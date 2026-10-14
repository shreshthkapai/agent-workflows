---
name: principle-redesign-from-first-principles
description: "Integrate a requirement into an existing design without layering on avoidable special cases."
---

# Redesign From First Principles

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

When a new requirement meets an existing design, consider the clean end state as if the requirement had been known from the start. Read the affected flow and trace its callers, data, and contracts before deciding what should change. Then implement that design incrementally within the authorized scope, so each edit remains reviewable. Carry the change through relevant types, consumers, and documentation, while preserving compatibility where the task or external users require it. A clean redesign is a way to reason about the target; it does not imply a broad rewrite or permission to change unrelated behavior.
