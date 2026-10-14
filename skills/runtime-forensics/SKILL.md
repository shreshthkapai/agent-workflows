---
name: runtime-forensics
description: Diagnose a live process or system from observed CPU, memory, scheduling, leak, or glitch evidence without assuming a cause.
---

# Runtime Forensics

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user wants to diagnose a live leak, CPU spin, scheduling problem, intermittent glitch, or similar runtime behavior. It is available automatically for live-system diagnostics and through {{INVOKE}}runtime-forensics. Identify the process, workload, time window, and observable signal. Use available authorized profilers, traces, heap data, or logs to collect evidence from the running system, then narrow the responsible stack, retained-object chain, or scheduling path.

Keep observation minimally intrusive. Add instrumentation only when it is reversible and within the request, and remove instrumentation you introduced when finished. Do not hot-patch production or restart a system merely to prove a theory. A generally slow report does not by itself establish a CPU hot path. Tie conclusions to runtime observations and source locations; distinguish a confirmed explanation from alternatives and gaps. Report when live access or useful symbols are unavailable rather than inventing measurements.

Follow {{GLOBAL_INSTRUCTIONS}}. Use one primary workflow and only relevant supporting steps. This is diagnostic work: do not fix the source unless asked. For a supplied capture with no live diagnosis, use trace-forensics. Report actual commands and observations, and preserve user data and existing state.
