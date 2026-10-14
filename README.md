# Agent Workflows

[pstack](https://github.com/cursor/plugins/tree/main/pstack), Lauren Tan's skills for Cursor, ported to Claude Code, Codex, and Grok. One model registry routes each role to whichever of those CLIs you have, so every call bills the subscription of the CLI that runs it.

## Install

Requires Python 3.11 or newer and at least one of Claude Code, Codex, or Grok. Some playbook scripts need `bun` or `node`.

```sh
git clone https://github.com/shreshthkapai/agent-workflows.git ~/agent-workflows
~/agent-workflows/install.py
```

The installer finds every CLI on your `PATH` and installs into each one:

- The skills to `~/.claude/skills`, `~/.codex/skills`, or `~/.grok/skills`.
- The `delegate` and `comment-sicko` agents to each CLI's `agents` directory.
- A marked block in `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or `~/.grok/AGENTS.md` that loads the `workflow` skill into every session, so tasks route to its playbooks without a command.
- `aw` and `aw-run` to `~/.local/bin`. `aw` links back to the checkout, so keep it.
- The model registry to `~/.config/agent-workflows/models.toml`, only when it does not exist yet.

Update with `git pull && aw install`. A rerun replaces only what `aw` installed, and stops before overwriting a skill or agent it did not install unless you pass `--force`. `aw install --runtime codex` installs into one CLI, `--skills a,b` installs a subset, and `--dry-run` prints the plan. `aw uninstall` removes everything `aw` installed and keeps your settings.

Grok also reads Claude Code's files, so with both installed it uses its own copies of the skills and agents and loads the workflow block from both instruction files.

## Skills: auto or manual

The `workflow` skill is always on. An auto skill loads on its own when the task matches its description. A manual skill runs only when you invoke it, as `/name` in Claude Code and Grok or `$name` in Codex, or when the workflow routes a step to it.

```sh
aw skills                      # every skill and its mode
aw skills auto reflect         # let the model load it on its own
aw skills manual swarm arena   # only when invoked or routed
aw skills default swarm        # back to the package default
```

Changes apply to every installed CLI at once and are saved to `~/.config/agent-workflows/skills.toml`, so updates keep them. Package defaults live in `config/invocation.toml`.

## Model routing

`~/.config/agent-workflows/models.toml` maps each pstack role to a model, and each model to the CLI that runs it. The main agent is not in it: each CLI's own model setting picks that.

```sh
aw models                                     # every role's model, effort, and speed
aw models set bug_fix opus:high               # one role
aw models set arena_runners opus:high sol:high   # a panel, one subagent per entry
```

`aw models set` checks the entry before saving it. Edit the file by hand to add models, or run `/setup-pstack` to be walked through every role.

```toml
budget = "large"          # starting effort: unlimited=max, large=xhigh, medium=high, small=medium

[models.opus]
provider = "claude"
model = "opus"
fallback = ["sol", "grok"]  # used when Claude is not installed or reports a usage limit

[roles]
judgment_prose = "opus"
arena_runners = ["opus", "sol"]
```

Use any mix of plans. A model whose CLI is not installed resolves to the first installed model in its `fallback` chain, so the shipped registry works with one, two, or all three CLIs.

Skills resolve a role with `aw-run --resolve <role>`. When the role's provider is the CLI you are in, the lead spawns a native subagent with that model and effort. Otherwise it runs `aw-run <role> < brief.md`, which runs `claude -p`, `codex exec`, or `grok --prompt-file` headless:

- A role entry can set its own effort and speed, as in `bug_fix = "sol:high"` or `how_explorer = "luna:xhigh:fast"`. Only Codex models have a fast tier. An entry without an effort uses `budget`.
- `--shift -2` lowers effort two steps for routine work, `--shift 1` raises it for the hardest.
- `--read-only` runs Claude in plan mode and Codex and Grok in their read-only sandboxes.
- No CLI runs with permission or sandbox bypass flags.
- Every call is appended to `~/.local/state/agent-workflows/runs.jsonl` with its role, provider, model, effort, duration, and usage, so you can check how the work splits between subscriptions.

## Plan limits

`/limits` (`$limits` in Codex), or `aw limits` in a shell, shows the live usage limits of each plan you have: each window's percent used and when it resets. Claude and Codex report live numbers. Grok shows its allowance only inside the Grok CLI, so `aw limits` points you to its `/usage`.

## Upstream

`PORTING.md` lists every substitution. Commit `0e257f7` is upstream verbatim, so `git diff 0e257f7 -- skills agents` shows each porting edit. Upstream's [guide](https://github.com/cursor/plugins/tree/main/pstack/docs/guide) explains the workflows. Its Cursor UI steps do not apply here.
