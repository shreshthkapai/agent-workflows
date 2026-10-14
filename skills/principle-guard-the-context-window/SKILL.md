---
name: principle-guard-the-context-window
description: "Keep task context useful by reading selectively and summarizing large, bounded outputs."
---

# Guard The Context Window

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Read the files and output needed for the current decision, and bound searches or command output when the full result is not useful. Prefer authoritative artifacts, concise summaries, and pointers to exact locations over repeatedly loading large raw payloads. Keep frequently needed instructions available when appropriate, while avoiding redundant copies. Delegate only when the task’s existing policy and scope call for delegation; do not spawn agents simply to process screenshots, files, or large output. Manage context as a limited resource, but rely on the session’s supported summarization and continuation behavior rather than assuming it cannot be renewed.
