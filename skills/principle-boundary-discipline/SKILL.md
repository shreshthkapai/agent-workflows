---
name: principle-boundary-discipline
description: "Place validation where untrusted inputs or runtime-dependent invariants enter the system."
---

# Boundary Discipline

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Validate and normalize data at external boundaries such as CLI arguments, configuration, network messages, and persisted input. Keep established internal invariants clear so every consumer does not repeat the same check. Do not assume all internal code is trustworthy: asynchronous state, mutable shared data, partial failures, or violated contracts may still need runtime validation. Keep business logic independent of framework wiring when that makes the behavior easier to reason about, but do not split code into pure helpers without a concrete benefit. Place each check where its input can actually be invalid and where failures can be handled meaningfully.
