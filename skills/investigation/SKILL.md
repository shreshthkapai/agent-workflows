---
name: investigation
description: Explain existing code or system behavior by tracing source, callers, data, and state; use for read-only questions about where or why behavior occurs.
---

# Investigation

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user asks how existing code behaves, where a value or decision comes from, which paths call a component, or why an observed result occurs. It is available automatically for those questions and through {{INVOKE}}investigation.

Keep the work read-only. Start at the narrowest relevant entry point, then trace callers, data transformations, state ownership, control flow, and configuration only as far as needed to answer. Read the actual source and cite file and line locations; use provided history or runtime evidence when the question depends on it. Separate observed facts from inference, especially when explaining why a choice was made.

Give a direct answer with the evidence that supports it and state material gaps. Do not change code merely because the investigation exposes a defect; report the finding separately. In a large repository, a native explorer can help with genuinely independent slices, but do not force delegation or fan out a narrow question. For a retrospective of substantial work already performed, use show-me-your-work when requested instead.

Follow {{GLOBAL_INSTRUCTIONS}}. The requested outcome sets scope: use one primary workflow and only relevant supporting steps, not every available workflow.
