---
name: principle-minimize-reader-load
description: "Improve code that is difficult to trace by clarifying ownership, state changes, and useful indirection."
---

# Minimize Reader Load

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Help a maintainer answer where important data comes from, what can change it, and which rule applies. Prefer clear names, narrow mutable state, explicit ownership, and a direct path from input to result. Put an invariant where it can be understood once and reused safely. Remove indirection when it merely forwards to one destination without clarifying meaning; keep it when it isolates a real boundary, names a concept, or makes change safer. Avoid arbitrary limits on files or layers: judge each one by whether it reduces or increases the reader’s work in this codebase.
