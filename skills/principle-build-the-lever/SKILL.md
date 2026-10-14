---
name: principle-build-the-lever
description: "Use a small reusable tool when it materially improves repeatability, correctness, or review of the work."
---

# Build The Lever

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Before repetitive or fragile manual work, check whether existing commands, scripts, generators, or project tools already handle it. Add a small reusable helper only when it materially improves repeatability, correctness, or reviewability enough to justify maintaining it. Keep the helper safe and limited to the actual task; a one-off edit does not automatically need a script, framework, or new file. Use the helper to verify the same observable result a reviewer cares about, and inspect its output. Keep durable tooling changes within the user’s scope; this principle does not require a commit or publication.
