---
name: why
description: "Investigate the evidence behind a design choice, regression, threshold, or historical behavior. Use for motivation and tradeoffs; use how for current runtime behavior."
---

# Why

Use this skill to explain why a code path may have been shaped as it was. Before using tools or accessing history, read {{RUNTIME_GUIDE}} for this runtime's capabilities, invocation rules, and data-access limits.

Anchor the question in the relevant files, symbols, and history. Search a proportionate set of sources that are actually available and authorized, such as version history, linked reviews or issues, project documents, observability, or user-provided context. Follow relevant citations far enough to verify them. Do not require every source category or parallel investigators.

Separate direct evidence from inference. Tie claims about intent to a specific commit, review, issue, document, event, or comment. Code can show what happens, but its shape alone does not prove why. Report contradictions and distinguish a source that was unavailable, searched with no relevant result, or not searched. A null search is not proof that no event occurred.

Present the strongest evidence, reasonable interpretations, competing explanations when material, and unresolved gaps. Do not write to external systems. If the answer informs a requested change, state the evidence-backed constraints and risks for that change.
