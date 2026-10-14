---
name: unslop
description: Improve prose when drafting or revising replies, explanations, documentation, PR descriptions, or agent instructions. Use when clarity, concision, or formulaic AI wording needs attention.
---

# Unslop

Read `{{RUNTIME_GUIDE}}` for host-specific invocation, agent, model, and capability rules.

Use judgment to apply these guidelines when prose would benefit from clearer, more natural wording. Automatic invocation is allowed; explicit `{{INVOKE}}unslop` requests also apply. Keep a short, clear reply short. Use the current agent and model.

## Write and edit

- State the concrete action, mechanism, result, or decision. Replace vague claims with supported details. Do not invent measurements, sources, examples presented as facts, or certainty to make writing stronger.
- Prefer familiar words and direct verbs. Remove filler, promotional claims, generic conclusions, repeated explanations, and canned openings or closings.
- Preserve meaning, intended tone, qualifications, citations, and the user's voice. Keep uncertainty that reflects the evidence; trim redundant hedging.
- Give paragraphs a clear purpose. Split sentences that make the reader backtrack, and vary their length naturally. Use active voice when naming the actor helps.
- Avoid forced contrasts, decorative metaphors, arbitrary groups of three, synonym cycling, and inflated claims of importance. Say the point directly.
- Answer without reflexive praise or agreement. Express a reasoned view when the task calls for one; do not manufacture opinions or personal experiences.
- Use headings, lists, tables, and emphasis when they help the reader navigate or compare information. Avoid repetitive labels and excessive formatting. Choose punctuation for clarity rather than applying blanket bans on dashes, parentheses, colons, or quotation styles.
- Keep established technical terms when precision matters. Explain unfamiliar terms when useful rather than replacing them with vague wording.

For new prose, apply the guidelines while drafting. For an editing request, revise the supplied text and check that the result retains its meaning. Before returning it, check for unsupported claims, padding, and unclear sentences. A concise answer does not need an additional rewrite or separate review agent.

## Scope

Edit prose only. Preserve exact quotations, code, commands, identifiers, paths, and structured data unless the user asks to change them. Follow required templates and the user's formatting preferences.

For existing files, edit only the prose within the requested task. Do not expand a writing request into unrelated code changes, repository cleanup, skill edits, or external publishing.
