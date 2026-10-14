---
name: automate-me
description: "Turn a user's stated working preferences into a concise personal workflow skill, or revise an existing one. Use for explicit requests to capture or update working style."
---

# Automate Me

Use this skill only when asked to capture or revise working preferences. Read {{RUNTIME_GUIDE}} first to understand the available skill format, tools, and data boundaries.

Use evidence from the current conversation or history the user specifically supplied or authorized. Do not search broad private histories or assume a particular editor's transcript layout. Separate repeated, explicit preferences from one-off choices and your own inferences; preserve contradictions as uncertainty rather than turning them into rules.

Draft one concise skill for the requested scope. Check for an existing target and preserve useful, uncontradicted guidance when updating it. Use a native skill-authoring workflow only when it is installed and allowed by the caller's invocation policy. Do not duplicate that workflow's manual.

Show the concrete draft before durable installation unless the user explicitly authorized that exact output and destination. Make no memory, global configuration, commit, or publication changes beyond the requested artifact.
