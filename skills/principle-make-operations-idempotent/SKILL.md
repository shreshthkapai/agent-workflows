---
name: principle-make-operations-idempotent
description: "Make retryable state-changing operations converge safely after repeats, retries, or partial failure."
---

# Make Operations Idempotent

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

For commands, jobs, and external mutations that may be retried, consider what happens after a repeated request or a partial failure. Where the operation can be repeated, use the appropriate reconciliation, deduplication, idempotency key, transaction, or compare-and-set mechanism so the system converges to the intended state. Match the mechanism to the operation and its contract; not every function needs retry logic. Treat locks and persisted state according to their actual ownership and liveness guarantees. Do not infer that a process is stale from a PID alone or automatically delete state whose ownership has not been established.
