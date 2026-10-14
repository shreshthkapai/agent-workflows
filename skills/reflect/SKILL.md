---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
disable-model-invocation: true
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Before fanning out, find this conversation's transcript. In Claude Code it lives in `~/.claude/projects/<slug>/`, where `<slug>` is the working directory with every `/` replaced by `-`. Do not glob across `~/.claude/projects/*/`. That crosses workspace boundaries and reads private chats from unrelated projects. Codex keeps every project's sessions under `~/.codex/sessions/YYYY/MM/DD/`, so check that the first line's `payload.cwd` is the working directory before reading further.

```bash
ls -t ~/.claude/projects/<slug>/*.jsonl ~/.claude/projects/<slug>/*/subagents/*.jsonl 2>/dev/null | head -10  # Claude Code
ls -t ~/.codex/sessions/*/*/*/*.jsonl 2>/dev/null | head -10  # Codex
```

That covers the Claude Code session (`<id>.jsonl`) and subagent (`<id>/subagents/<child>.jsonl`) layouts, and Codex's dated rollout files. For each candidate, `grep -l` a distinctive phrase from the conversation's opening user prompt. Take the file that contains it. If none matches, pass a tight digest of the session instead.

## 2. Spawn three reviewers in parallel

Spawn three general-purpose subagents at once, not read-only. Reviewers need MCP access to look up the tickets, chat threads, and observability traces the transcript references, and read-only modes can block MCP tools.

Each reviewer and the synthesizer name a role in `~/.config/agent-workflows/models.toml`. Resolve its model with `aw-run --resolve <role>` and spawn per the Subagents section of the **poteto-mode** skill. A role of `inherit` runs on the parent model. If the spawn or `aw-run` rejects the model, use the model's `fallback` and say so. Pick each subagent's reasoning level and fast or standard speed for the job, per the Subagents section of the **poteto-mode** skill.

| Lens | Role | Prompt template |
|---|---|---|
| Judgment | `reflect_judgment` | `references/judgment-reviewer.md` |
| Tooling | `reflect_tooling` | `references/tooling-reviewer.md` |
| Divergent | `reflect_judgment` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Reviewers return findings in their final message.

## 3. Synthesize

One general-purpose subagent on the `reflect_judgment` role, not read-only. It spot-verifies citations through MCP, and read-only modes can block MCP tools. Pass `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. It returns an Accepted / Rejected / Backlog list.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

File each Backlog item to your team's devex or backlog tracker without waiting. Only the Accepted list waits for approval.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to the CLI's `skill-creator` skill and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `skill-creator` and run its description-optimization loop.
- `new skill via skill-creator: <kebab-name>`: hand creation to `skill-creator`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
