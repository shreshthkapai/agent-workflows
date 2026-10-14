---
name: performance
description: Measure and improve a requested performance problem by comparing the same workload before and after a focused change.
---

# Performance

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user asks to improve measured slowness, throughput, memory use, or responsiveness. It is available automatically for performance work and through {{INVOKE}}performance. Define the workload, metric, units, and relevant conditions before drawing conclusions. Capture a real baseline with available runtime measurements, traces, or profiles; include warm-up and repeat runs when they materially affect results.

Use evidence to identify the costly path, then make one focused change tied to a stated hypothesis. Re-run the same workload under comparable conditions and report the before and after values, change, variability, and artifact locations. Do not substitute theoretical estimates for measurements or claim a speedup smaller than the observed noise supports. If the request is diagnosis only, use runtime-forensics for a live system or trace-forensics for an existing capture rather than changing code.

Follow {{GLOBAL_INSTRUCTIONS}} and keep one primary workflow with only relevant supporting steps. For substantial, understood, bounded implementation, use one native worker. The brief must require reading {{GLOBAL_INSTRUCTIONS}} and this SKILL.md in full, and state file scope, starting state, constraints, expected artifact, and finish check; inspect the actual diff. Do not add cost-intensive infrastructure, dependencies, or unrelated tests without scope; follow the user's testing instructions and verify the actual workload or artifact.
