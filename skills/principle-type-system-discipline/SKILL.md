---
name: principle-type-system-discipline
description: "Use types to represent meaningful states, variants, and schema relationships in typed code."
---

# Type System Discipline

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Model distinct states and variants so the compiler can help callers handle the cases that matter. Prefer one authoritative representation over contradictory fields or duplicated schemas, and use exhaustive matching where the language supports it. Parse untrusted or runtime data before treating it as a trusted domain type. Types cannot prove every runtime-dependent fact: retain checks for external input, mutable state, and other invariants the compiler cannot establish. Evaluate branded primitives, casts, and assertions by the actual confusion or failure risk they create; neither branding every primitive nor banning every cast is a goal.
