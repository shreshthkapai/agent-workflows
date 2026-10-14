# Porting pstack to Claude Code and Codex

The skills are [pstack](https://github.com/cursor/plugins/tree/main/pstack) verbatim, except where a passage needs Cursor. Commit `0e257f7` imports upstream unchanged, so `git diff 0e257f7 -- skills agents` is the full list of porting edits. Re-sync the same way: import upstream verbatim in one commit, then reapply these rules in the next.

## Rule

Keep every sentence that works in a terminal CLI. Change a passage only when it names a Cursor tool, path, product, model slug, or UI. Make the smallest edit that works in both Claude Code and Codex. Do not condense, soften, or restyle anything else. Keep upstream's voice: short declarative sentences, no long dashes, no mid-sentence colons.

## Substitutions

| Upstream (Cursor) | Port |
| --- | --- |
| `Task` tool, `Task` call, Task spawn | subagent, spawn a subagent. Native tool in the current CLI, `aw-run` for another provider, per the Subagents section of **poteto-mode** |
| `run_in_background: true` | in the background |
| `subagent_type: generalPurpose` | a general-purpose subagent |
| `subagent_type: "poteto-agent"` | the `poteto-agent` agent |
| readonly subagent | read-only subagent (`aw-run --read-only`, or a native read-only agent) |
| `environment: "cloud"`, cloud workers, `cloud_base_branch` | a local git worktree per worker, created from the named branch |
| Model slugs (`grok-*`, `claude-opus-*`, `composer-*`) and model families | the role's model from `aw-run --resolve <role>`. Families are providers: `claude` and `codex` |
| `~/.cursor/rules/pstack-models.mdc` and its role lines (`arena runners`) | `~/.config/agent-workflows/models.toml` and its roles (`arena_runners`) |
| "the Task tool rejects a slug" | the spawn or `aw-run` rejects the model |
| `AskQuestion` | ask the user, with the CLI's structured question tool when it has one |
| `create-skill` (Cursor built-in) | the CLI's `skill-creator` skill |
| Cursor transcripts, `~/.cursor/projects/<slug>/agent-transcripts` | Claude Code `~/.claude/projects/<slug>/*.jsonl`, Codex `~/.codex/sessions/YYYY/MM/DD/*.jsonl` |
| `~/.cursor/skills/`, `.cursor/skills/` | `~/.claude/skills/` or `~/.codex/skills/`; project `.claude/skills/` or `.agents/skills/` |
| Cursor restart, cloud-agent URL | CLI restart; a session id resumed with `claude --resume` or `codex resume` |
| Bugbot | review bots (Bugbot, Codex review, Claude review, and the like) |
| `/loop` | `/loop` in Claude Code. Codex has no `/loop`, so re-run the check each turn |
| fast slugs, fast mode | the CLI's fast speed tier. `aw-run` always runs at standard speed |
| `/skill-name` invocation | unchanged in Claude Code. Codex invokes the same skill as `$skill-name` |
| `icon`, `color`, `is_background` frontmatter | removed. Skill `name` is the kebab-case directory name |

Skills and plugins from other Cursor packages (`cursor-team-kit`'s `deslop`, `control-cli`, `control-ui`; Origin) stay named, marked as optional when installed. MCP references stay. Both CLIs support MCP.

## Removed

- `make-bot-ui`. It builds UI for Grok Bot webhooks.
- `automations/` and `docs/guide/`. They are Cursor automations and the Cursor UI guide.
