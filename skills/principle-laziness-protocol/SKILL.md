---
name: principle-laziness-protocol
description: "Choose the smallest complete change when extending, simplifying, or refactoring existing code."
---

# Laziness Protocol

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Start from the user’s requested outcome and find the smallest complete change that achieves it. Prefer removing complexity that is demonstrably unnecessary before adding layers, wrappers, or new state. Keep abstractions that express a real domain concept, isolate likely change, or improve reuse; line count, file count, and a fixed depth are not goals by themselves. Trace where a proposed value comes from and whether an existing path already solves the need before threading it through more layers. Preserve unrelated user work and guards required by the contract. Make the change easy to inspect and maintain.
