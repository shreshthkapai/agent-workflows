---
name: architect
description: "Shape a design before implementation when requirements or system boundaries make the code shape consequential. Use for explicit architecture and design requests; ordinary small edits do not need this workflow."
---

# Architect

Use this skill when a design deliverable will help settle a non-trivial implementation shape. Read {{RUNTIME_GUIDE}} first for available tools, models, invocation policy, and limits.

Start from the caller's intended use, acceptance conditions, core data and types, existing contracts, and affected callers. Inspect the relevant code directly when it exists. For an existing system, trace ownership and boundaries before proposing a new shape.

Describe a design with the caller-facing example, data model or type sketch, signatures, module responsibilities, and important failure or edge cases. Compare a small number of coherent alternatives when the choice has real consequences; explain the selected shape and its tradeoffs. Avoid routine multi-model reviews or nested workflows unless requested and supported.

Treat design as the deliverable by default. If the user asks to implement too, keep the design and code within that scope. Honor an explicit review checkpoint before proceeding. If implementation evidence invalidates the design, surface the mismatch and revise the shape instead of accumulating special cases.
