---
name: feature
description: Implement requested new or changed product behavior by inspecting its user flow, acceptance conditions, and affected data model.
---

# Feature

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user requests new behavior or a product capability change. It is available automatically for feature work and through {{INVOKE}}feature. Inspect the affected flow, acceptance conditions, data shape, and existing contracts before choosing an implementation. Prefer the smallest design that clearly models the behavior, and trace relevant callers and consumers so the change fits existing interfaces.

Use Arena only for a consequential unresolved choice with credible alternatives, not as a routine feature step. For UI work, use the installed Impeccable guidance when it applies; do not make it a requirement for backend work. Follow {{GLOBAL_INSTRUCTIONS}}: keep one primary workflow, handle small or sensitive changes inline, and use one native worker for substantial, understood, bounded implementation. The brief must require reading {{GLOBAL_INSTRUCTIONS}} and this SKILL.md in full, and state file scope, starting state, constraints, expected artifact, and finish check; inspect the actual diff.

Verify the actual user flow and relevant state or edge cases with available tools and the user's testing instructions. Do not add tests by default, create unrelated harnesses, or treat compilation alone as proof of the requested behavior. Keep discovered bugs separate from feature scope. Do not automatically run Interrogate or Reflect, or create a PR, commit, or publish the change.
