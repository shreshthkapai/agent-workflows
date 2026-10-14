---
name: principle-exhaust-the-design-space
description: "Compare approaches when a consequential design choice remains unresolved after inspecting existing patterns."
---

# Exhaust The Design Space

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this principle when inspection and the established codebase leave a consequential choice with multiple credible approaches. First check whether an existing pattern, a small sketch, or a focused experiment can resolve the question cheaply. If uncertainty remains, compare the options against concrete constraints such as correctness, compatibility, user experience, maintainability, and cost of change. Choose an exploration sized to the decision; several full prototypes are rarely needed. For routine implementation, clear bug fixes, or choices already determined by requirements, proceed directly. Surface unresolved tradeoffs to the lead or user when they exceed the authorized scope.
