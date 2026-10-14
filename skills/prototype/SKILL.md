---
name: prototype
description: Build a small, bounded experiment or sketch for a requested prototype or to resolve empirical uncertainty within an authorized task.
---

# Prototype

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use this workflow when the user asks for a sketch or prototype, or when a small reversible experiment within the authorized task can answer an empirical question better than speculation. It is available automatically when that experiment is useful and through {{INVOKE}}prototype. State the question and what observation would count as a useful answer before building. Keep the experiment isolated in an appropriate scratch area, with a scope and stopping point proportional to the question.

Create the minimum working artifact that can produce evidence. A small number of variants may help compare a real tradeoff, but do not force multiple implementations. Observe actual runtime, rendering, or timing when relevant, under comparable conditions. Report findings, limitations, a recommendation when supported, the artifact location, and whether it is throwaway. Do not promote, ship, or publish the prototype beyond the request, or add expensive infrastructure or an unrelated test harness.

Follow {{GLOBAL_INSTRUCTIONS}} and use one primary workflow with only relevant supporting steps. For a UI prototype, respect the selected theme and use installed Impeccable guidance when appropriate; do not introduce an unrequested redesign or replace the existing stack. Small experiments can be done inline; use one native worker only for substantial, understood, bounded implementation. The brief must require reading {{GLOBAL_INSTRUCTIONS}} and this SKILL.md in full, and state file scope, starting state, constraints, expected artifact, and finish check; inspect the actual diff.
