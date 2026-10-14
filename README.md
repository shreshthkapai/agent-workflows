# Agent Workflows

Fifty selectable workflow and principle skills adapted from [Lauren Tan's pstack](https://github.com/poteto/plugins/tree/74dd2291e8e37b12fd6dc49b2acbd655c6bdaf12/pstack), with installation adapters for Codex and Claude Code.

Choose individual skills. Installation defaults to manual invocation; automatically eligible workflows can be enabled individually. The package does not replace global instructions, change native agent profiles, install connectors, or publish anything.

## Choose and install

Requires Python 3.11 or newer. No Python packages, network access, or model calls are required by the installer. The optional decision-log helper requires a POSIX host because it uses file locking.

List the [complete catalog](CATALOG.md):

```sh
python3 install.py --list
```

Prepare a Codex installation with Arena and TDD automatic, and How manual:

```sh
python3 install.py --runtime codex --skills arena,tdd,how --auto arena,tdd --dry-run
python3 install.py --runtime codex --skills arena,tdd,how --auto arena,tdd
```

Install manual workflows for Claude Code:

```sh
python3 install.py --runtime claude --skills how,why,architect
```

Use `$how` in Codex and `/how` in Claude Code. `--skills all` selects all fifty, with manual invocation by default. `--auto` is an explicit list of selected, eligible skills; eleven workflows remain manual-only because their instructions require explicit requests. See the catalog for eligibility.

Personal destinations default to `$CODEX_HOME/skills` or `~/.codex/skills` for Codex, and `~/.claude/skills` for Claude Code. For a project or custom destination, pass `--dest`, for example `--dest .claude/skills` or `--dest .agents/skills`. Project guidance and the host's skill discovery rules still apply.

The installer writes selected skill folders and an `agent-workflows/` support directory beside the destination. It preserves existing global instructions and profiles. It refuses to overwrite existing skills or changed support instructions. Existing model choices in its support registry are preserved. To use another existing workflow registry, pass `--models PATH`.

## Runtime adaptation

Canonical skill files contain path and invocation placeholders. Run the installer rather than copying those templates directly. It resolves paths for the destination and emits the correct invocation metadata:

| Runtime | Manual invocation policy | Command |
| --- | --- | --- |
| Codex | `agents/openai.yaml`: `allow_implicit_invocation: false` | `$skill-name` |
| Claude Code | `SKILL.md` frontmatter: `disable-model-invocation: true` | `/skill-name` |

The runtime guide is loaded when a selected skill needs it. Installed manual skills do not activate because another workflow references them. Global/project instructions and explicit user directions take precedence.

The [model-role example](config/models.toml) leaves native model and effort settings unchanged. Configure supported choices deliberately. A registry entry does not establish model access. GPT model identifiers and Codex effort settings are not translated into Claude settings. Independent agents using the same model do not constitute a cross-family review.

This package uses each host's available native agent mechanism. It supplies no separate scheduler, cross-vendor model bridge, daemon, transcript database, or native skill-creator replacement.

## Compatibility and verification

See [compatibility notes](COMPATIBILITY.md) for what changed from the originals and which capabilities are optional. These are adaptations, not a claim that the original Cursor workflows run unchanged.

The [recorded configuration checks](VERIFICATION.md) distinguish structural validation and Codex discovery from model-backed workflow execution. Claude frontmatter and template rendering can be inspected without running a Claude model; that does not establish complete behavioral equivalence. Missing profilers, browsers, MCP sources, transcript access, model choices, or authentication must be reported by the workflow.

## Attribution and distribution

The [MIT license](LICENSE) and [attribution notice](NOTICE.md) retain Lauren Tan's copyright. [catalog.json](catalog.json) records the pinned upstream source for every skill. Unrelated skills and the maintainer's private configuration, conversations, credentials, and memory are excluded.

This directory is a local package ready for review and sharing. It has not been published to a repository or plugin directory. It installs standalone native skills; it is not a preconfigured marketplace plugin.
