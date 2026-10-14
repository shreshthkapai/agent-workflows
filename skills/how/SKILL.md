---
name: how
description: "Trace how a code path or subsystem works and explain its callers, data flow, ownership, and architecture. Use for code walkthroughs and placement questions; use why for design history."
---

# How

Use this skill to explain existing behavior from the actual source. Before choosing tools or delegating, read {{RUNTIME_GUIDE}} for this runtime's invocation, tool, model, and capability rules.

Clarify the scope from the request and current context. Trace the relevant entry point through callers, callees, types, configuration, and side effects until the input-to-output path is concrete. Identify where state is owned and how it moves. Read source rather than relying on names or prior summaries.

For a narrow question, investigate directly. For a broad subsystem, split only into distinct slices when useful and permitted by the runtime and caller. Reconcile findings against the source.

Give a concise mental model with pointers to relevant files and symbols. Explain the flow and key abstractions; include a file map or gotchas only when they help the reader. Mark interpretation as inference. Critique architecture only when asked, ground each concern in the code, and do not change code unless the user also requested a change.
