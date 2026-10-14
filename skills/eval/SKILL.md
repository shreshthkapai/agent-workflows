---
name: eval
description: "Evaluate how a bounded prompt, skill, or structure change affects agent behavior before adopting it. Use when the user explicitly requests an evaluation."
---

# Eval

Use this skill for an explicitly requested, bounded behavior evaluation. Read {{RUNTIME_GUIDE}} for available models, isolation options, transcript access, and execution limits. Define the behavior under study and a short rubric before running candidates.

Give candidates the same realistic user prompt and equivalent isolated environments that differ only in the intended variant. Keep evaluation framing, rubric, labels, and comparison cues out of candidate-visible files and prompts. Use sanitized neutral labels. Have one judge assess outputs blind to variant labels with the same rubric and pass; choose judge and candidate roles only from capabilities confirmed by the runtime. Note model-family overlap or other limits that weaken the comparison.

Review actual artifacts and positively identified transcripts when available. Self-reports do not prove which guidance was read or applied. If transcripts are unavailable, state that verification gap rather than scanning unrelated private histories.

Summarize the setup, evidence, judge result, disagreements, and limits. An evaluation informs a decision; it does not automatically promote a variant or change live configuration.
