---
name: trace-forensics
description: Analyze an existing profile, trace, heap dump, or diagnostic capture to explain hot paths, blocking, retention, or timing.
---

# Trace Forensics

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user provides or points to an already captured CPU profile, trace, spin dump, heap dump, or similar diagnostic artifact. It is available automatically for captured-artifact analysis and through {{INVOKE}}trace-forensics. Preserve the original. Establish the format, capture window, sampling model, symbols, and relevant workload before interpreting the data.

Use an appropriate available parser or viewer and keep reads bounded for large artifacts. Summarize the evidence relevant to the question: hot stacks, blocked threads, garbage collection, retained objects, or source mappings. Connect frames to source when symbols permit, and distinguish sample frequency or correlation from proof of causality. Note missing symbols, sampling bias, incomplete capture windows, or other limits that change the conclusion. Keep any derived analysis artifact separate from the supplied capture.

Do not run the program or add live instrumentation automatically; use runtime-forensics when the task requires observing a live system. Do not make source changes unless asked. Follow {{GLOBAL_INSTRUCTIONS}} and use one primary workflow with only relevant supporting steps. Give the user a concise evidence-based explanation, identify uncertainty, and report the actual artifact and analysis commands used.
