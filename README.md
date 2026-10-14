# Agent Workflows

[pstack](https://github.com/cursor/plugins/tree/main/pstack), Lauren Tan's skills for Cursor, ported to Claude Code and Codex. One model registry routes each role to either CLI, so every call bills the subscription of the CLI that runs it.

## Install

Requires Python 3.11 or newer. Some playbook scripts need `bun` or `node`.

```sh
python3 install.py --list
python3 install.py --runtime claude --skills all --dry-run
python3 install.py --runtime claude --skills all
python3 install.py --runtime codex --skills all
```

Each install writes:

- The selected skills to `~/.claude/skills` or `~/.codex/skills` (`--dest` for another directory).
- The `delegate` and `comment-sicko` agents to `~/.claude/agents` or `~/.codex/agents`.
- `aw-run` to `~/.local/bin`.
- The model registry to `~/.config/agent-workflows/models.toml`, only when it does not exist yet.

Invocation defaults live in `config/invocation.toml`. The `workflow` skill is always on: the installer adds a marked block to `~/.claude/CLAUDE.md` or `~/.codex/AGENTS.md` that loads it into every session, so tasks route to its playbooks without a command. The skills in its `auto` list load on their own when relevant. Every other skill is manual, invoked as `/name` in Claude Code and `$name` in Codex. `--auto name,...` replaces the auto list for one install. `--force` replaces installed copies, and `--uninstall` removes them and the block. Skills reference each other by relative path, so install `workflow` together with the skills it routes to.

## Model routing

`~/.config/agent-workflows/models.toml` maps each pstack role to a model, and each model to the CLI that runs it. Edit it by hand or with `/setup-pstack`.

```toml
budget = "large"          # starting effort: unlimited=max, large=xhigh, medium=high, small=medium

[models.opus]
provider = "claude"
model = "opus"
fallback = "sol"          # retried on when Claude reports a usage limit

[roles]
judgment_prose = "opus"
arena_runners = ["opus", "sol"]
```

Skills resolve a role with `aw-run --resolve <role>`. When the role's provider is the CLI you are in, the lead spawns a native subagent with that model and effort. Otherwise it runs `aw-run <role> < brief.md`, which runs `claude -p` or `codex exec` headless:

- `--shift -2` lowers effort two steps for routine work, `--shift 1` raises it for the hardest.
- `--read-only` runs Claude in plan mode and Codex in its read-only sandbox.
- Neither CLI runs with permission or sandbox bypass flags.
- Every call is appended to `~/.local/state/agent-workflows/runs.jsonl` with its role, provider, model, effort, duration, and usage, so you can check how the work splits between subscriptions.

## Upstream

`PORTING.md` lists every substitution. Commit `0e257f7` is upstream verbatim, so `git diff 0e257f7 -- skills agents` shows each porting edit. Upstream's [guide](https://github.com/cursor/plugins/tree/main/pstack/docs/guide) explains the workflows. Its Cursor UI steps do not apply here.
