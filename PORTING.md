# Porting pstack to Claude Code, Codex, and Grok

The skills are [pstack](https://github.com/cursor/plugins/tree/main/pstack) verbatim, except where a passage needs Cursor. Commit `22880ab` imports upstream unchanged, so `git diff 22880ab -- skills agents` is the full list of porting edits. Commit `c411450` re-imports the skills that changed up to cursor/plugins@d457567, without the skills upstream added, so diff those skills against `c411450` instead. Re-sync the same way: import upstream verbatim in one commit, then reapply these rules in the next.

## Rule

Keep every sentence that works in a terminal CLI. Change a passage only when it names a Cursor tool, path, product, model slug, or UI. Make the smallest edit that works in Claude Code, Codex, and Grok. Do not condense, soften, or restyle anything else. Keep upstream's voice: short declarative sentences, no long dashes, no mid-sentence colons.

## Substitutions

| Upstream (Cursor) | Port |
| --- | --- |
| `Task` tool, `Task` call, Task spawn | subagent, spawn a subagent. Native tool in the current CLI, `aw-run` for another provider, per the Subagents section of **workflow** |
| `run_in_background: true` | in the background |
| `subagent_type: generalPurpose` | a general-purpose subagent |
| `subagent_type: "poteto-agent"` | the `delegate` agent |
| readonly subagent | read-only subagent (`aw-run --read-only`, or a native read-only agent) |
| `environment: "cloud"`, cloud workers, `cloud_base_branch` | a local git worktree per worker, created from the named branch |
| Model slugs (`grok-*`, `claude-opus-*`, `composer-*`) and model families | the role's model from `aw-run --resolve <role>`. Families are providers: `claude`, `codex`, and `grok` |
| `~/.cursor/rules/pstack-models.mdc` and its role lines (`arena runners`) | `~/.config/agent-workflows/models.toml` and its roles (`arena_runners`) |
| "the Task tool rejects a slug" | the spawn or `aw-run` rejects the model |
| `AskQuestion` | ask the user, with the CLI's structured question tool when it has one |
| `create-skill` (Cursor built-in) | the CLI's `skill-creator` skill |
| Cursor transcripts, `~/.cursor/projects/<slug>/agent-transcripts` | Claude Code `~/.claude/projects/<slug>/*.jsonl`, Codex `~/.codex/sessions/YYYY/MM/DD/*.jsonl`, Grok `~/.grok/sessions/<encoded-cwd>/<session-id>/chat_history.jsonl` |
| `~/.cursor/skills/`, `.cursor/skills/` | `~/.claude/skills/`, `~/.codex/skills/`, or `~/.grok/skills/`; project `.claude/skills/`, `.agents/skills/`, or `.grok/skills/` |
| Cursor restart, cloud-agent URL | CLI restart; a session id resumed with `claude --resume`, `codex resume`, or `grok --resume` |
| Bugbot | review bots (Bugbot, Codex review, Claude review, and the like) |
| `/loop` | `/loop` in Claude Code and Grok. Codex has no `/loop`, so re-run the check each turn |
| fast slugs, fast mode | the CLI's fast speed tier. A role entry marks it as `model:effort:fast`, which `aw-run` applies to Codex models |
| `/skill-name` invocation | unchanged in Claude Code and Grok. Codex invokes the same skill as `$skill-name` |
| `icon`, `color`, `is_background` frontmatter | removed. Skill `name` is the kebab-case directory name |

Skills and plugins from other Cursor packages (`cursor-team-kit`'s `deslop`, `control-cli`, `control-ui`; Origin) stay named, marked as optional when installed. MCP references stay. All three CLIs support MCP.

## Renamed

The workflow is manual by default, as upstream's `poteto-mode` is, and `aw skills always workflow` loads it into every session. `poteto-mode` is `workflow`, `poteto-agent` is `delegate`, and `poteto-help` is `pstack-help`. Passages that told the user to start a task with `/poteto-mode` now name `/workflow`, or the always-on setting. Upstream text otherwise keeps its wording.

## Added

- `obsidian-markdown`, `obsidian-bases`, `json-canvas`, and `obsidian-cli`, manual skills copied unchanged from kepano/obsidian-skills@3ccff53. They are not pstack, so `git diff 22880ab -- skills` also shows them as added. Update them by copying the newer upstream folders over these.
- `limits` and `upstream`, manual skills with no upstream counterpart. `upstream` reports what changed in pstack since the last `Import upstream pstack verbatim` commit.
- `delegate`, and the workflow's Playbooks section, say a delegate does its task itself, and that playbooks and subagent spawns are the lead's. Upstream relies on Cursor subagents being unable to act as leads. Here a native subagent or an `aw-run` child read the always-on workflow and ran playbooks.

## Removed

- `make-bot-ui`. It builds UI for Grok Bot webhooks.
- `automations/` and `docs/guide/`. They are Cursor automations and the Cursor UI guide.
