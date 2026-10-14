---
name: principle-foundational-thinking
description: "Shape core data and access paths before implementing logic or sequencing substantial work."
---

# Foundational Thinking

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Before writing logic, identify the central data shapes, who owns them, and the access paths the behavior needs. Choose structures that fit the actual reads, writes, and invariants, then let those choices simplify downstream code. Inspect the existing scaffold and reuse it where it serves the task. Add shared types, CI, linting, or test infrastructure only when there is a concrete need and later work benefits from it. Consider concurrency early: determine which actors can mutate the same state and use the repository’s isolation rules where they overlap. Avoid speculative architecture that closes options without solving a current requirement.
