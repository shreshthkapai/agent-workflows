# Agent Workflows

Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack) skills for Claude Code, Codex, and Grok, with every subagent role routed to the model and subscription you choose.

## Install

You need Python 3.11 or newer and at least one of Claude Code, Codex, or Grok. Some playbook scripts also need `bun` or `node`.

```sh
git clone https://github.com/shreshthkapai/agent-workflows.git ~/agent-workflows
~/agent-workflows/install.py
```

The installer finds each CLI on your `PATH` and installs into all of them. Start a new session afterwards. Type `/workflow` (`$workflow` in Codex) before a task to run it through the workflow's playbooks, or run `aw skills always workflow` once to load the workflow into every session.

The skills call `aw` and `aw-run` from `~/.local/bin`, so add that directory to your `PATH` if the installer says it is missing.

Update:

```sh
cd ~/agent-workflows && git pull && aw install
```

The `nightly` branch carries skills that have not reached `main` yet, such as `/upstream`. Install it the same way from that branch, and the update command above follows it:

```sh
git clone -b nightly https://github.com/shreshthkapai/agent-workflows.git ~/agent-workflows
~/agent-workflows/install.py
```

To switch an existing checkout, run `cd ~/agent-workflows && git switch nightly && aw install`.

Remove everything the installer added. Your model and skill settings stay.

```sh
aw uninstall
```

## What the installer writes

- The skills to `~/.claude/skills`, `~/.codex/skills`, or `~/.grok/skills`.
- The `delegate` and `comment-sicko` agents to each CLI's `agents` directory.
- With the workflow always on, a marked block in `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or `~/.grok/AGENTS.md` that loads it into every session.
- `aw` and `aw-run` in `~/.local/bin`. `aw` links back to the checkout, so keep the checkout.
- For Claude Code with the workflow always on, an `Agent` entry in `permissions.deny` of `~/.claude/settings.json`, which turns off the Agent tool. `aw skills manual workflow` and uninstall remove it, unless you added it yourself.
- The model registry at `~/.config/agent-workflows/models.toml`, if you don't have one yet.

A rerun replaces only the files `aw` wrote. It stops before it overwrites a skill or agent it did not install, unless you pass `--force`. Other options are `--runtime codex` for one CLI, `--skills a,b` for a subset, and `--dry-run` to print the plan.

Grok also reads Claude Code's files. With both installed, Grok uses its own copies of the skills and agents. With the workflow always on, Grok loads its block from both instruction files.

## Choose models

Each pstack role, such as `bug_fix` or `arena_runners`, runs on the model you assign it. Each model belongs to one CLI, and that CLI's plan pays for the call. Each CLI's own model setting picks the main agent, so the registry does not list it.

```sh
aw models                                        # every role's model, effort, and speed
aw models set bug_fix opus:high                  # one role
aw models set arena_runners opus:high sol:high   # a panel runs one subagent per entry
```

An entry is `model`, `model:effort`, or `model:effort:fast`. Only Codex models have a fast tier. A list is a panel, one subagent per entry. A single-model role may instead be a `{ pool = [...] }` table, which runs one subagent per spawn and hands out its entries in turn, so `["sol", "sol", "opus"]` sends two of every three spawns to Codex. `aw-run` keeps the turn in `~/.local/state/agent-workflows/pool-turns.json`. A panel role stays a list, because its skill launches each seat with `--index`, which a pool rejects. `aw models set` rejects an unknown role, model, or effort and leaves the file unchanged. To add a model, edit `~/.config/agent-workflows/models.toml`. `/setup-pstack` walks you through every role.

```toml
budget = "large"            # effort for entries that name none: unlimited=max, large=xhigh, medium=high, small=medium

[models.opus]
provider = "claude"
model = "opus"
fallback = ["sol", "grok"]  # used when Claude is not installed or reports a usage limit

[roles]
judgment_prose = { pool = ["sol:high", "sol:high", "opus:high"] }
arena_runners = ["opus:high", "sol:high"]
```

The shipped registry works with any mix of plans. If a model's CLI is not installed, `aw-run` uses the first installed model in its `fallback` list.

## Choose auto or manual skills

The `workflow` skill is manual by default, as upstream pstack's `/poteto-mode` is. Type `/workflow` (`$workflow` in Codex) at the start of a task that needs rigor. To load it into every session instead, so every task follows its playbooks without a command:

```sh
aw skills always workflow      # adds the marked block to each CLI's global instructions
aw skills manual workflow      # removes it again
```

The always-on workflow adds about 5k tokens of instructions to every session and to every subagent it spawns, and it runs the full playbook even for small fixes.

The model loads an auto skill on its own when a task matches the skill's description, and each auto skill adds its one-line description to every session. A manual skill runs only when you invoke it, as `/name` in Claude Code and Grok or `$name` in Codex, or when a workflow step calls it.

```sh
aw skills                      # every skill and its mode
aw skills auto reflect         # the model may load it on its own
aw skills manual swarm arena   # only when invoked or called by the workflow
aw skills manual all           # every skill except the workflow, as in upstream
aw skills default swarm        # back to the package default (`all` works here too)
```

`aw skills` changes every installed CLI at once and saves your choices in `~/.config/agent-workflows/skills.toml`, so updates keep them. The package defaults are in `config/invocation.toml`.

## Check plan limits

`aw limits`, or `/limits` in a session (`$limits` in Codex), shows how much of each plan you have used and when each window resets. Claude and Codex report live numbers. Grok shows its allowance only inside the Grok CLI, so `aw limits` points you to Grok's `/usage`.

## Check upstream

`/upstream` (`$upstream` in Codex) summarizes what changed in pstack since this port last imported it. It lists new and removed skills, says what each changed skill gained, lost, or cut, and recommends which changes to pull. It also checks poteto's `plugins` fork. It only reports and never edits the port.

## Obsidian skills

`obsidian-markdown`, `obsidian-bases`, `json-canvas`, and `obsidian-cli` come unchanged from Steph Ango's [obsidian-skills](https://github.com/kepano/obsidian-skills). They write Obsidian notes, Bases, and Canvas files, and drive the Obsidian CLI. They are manual by default. To let the model load them on its own when you work in a vault:

```sh
aw skills auto obsidian-markdown obsidian-bases json-canvas obsidian-cli
```

## How a subagent reaches another provider

A skill looks up a role with `aw-run --resolve <role>`. In Codex or Grok, if the role's model belongs to that CLI, the lead spawns a native subagent with that model and effort. If not, it runs `aw-run <role> < brief.md`, which starts `claude -p`, `codex exec`, or `grok --prompt-file` in headless mode and returns the final message.

In Claude Code with the workflow always on, the Agent tool is off, so every subagent starts through `aw-run`, Claude roles included. A lead cannot reach for a built-in agent type that runs on Claude by default, and nothing runs without a role. The deny rule is in the user settings, so it applies to every Claude Code session, `claude-lite` included. Claude Code's built-in Explore and Plan agents are gone too, though plan mode still mentions them.

- `aw-run` tells each child that it is the lead's delegate, so the child does its task and does not start its own playbook. `--agent NAME` runs the child as another installed agent, as `no-comments` does with `comment-sicko`.
- `--shift -2` lowers effort two steps for routine work, and `--shift 1` raises it one step for the hardest work.
- `--read-only` runs Claude in plan mode and Codex and Grok in their read-only sandboxes.
- Writable Codex jobs enable network access within the `workspace-write` sandbox, including localhost servers and browser checks.
- No CLI runs with a permission or sandbox bypass flag.
- `aw-run` appends each call to `~/.local/state/agent-workflows/runs.jsonl` with its role, provider, model, effort, duration, and token usage.

## Upstream

`PORTING.md` lists every change from upstream. Commits `22880ab` and `c411450` are upstream verbatim, and `PORTING.md` says which one to diff a skill against to see its porting edits. Upstream's [guide](https://github.com/cursor/plugins/tree/main/pstack/docs/guide) explains the workflows. Its Cursor UI steps do not apply here.
