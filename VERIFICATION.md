# Recorded configuration checks

Checked on 2026-10-14 with the local Codex CLI. These observations describe this package snapshot; they are not claims of complete workflow behavior or model quality.

| Check | Observation |
| --- | --- |
| Native `quick_validate.py` on all canonical skills | 50 passed |
| Native validator on the additional installed Codex skills | 12 passed |
| Template rendering through `install.py --dry-run` | All 50 rendered for Codex and all 50 for Claude; manual by default |
| Rendered YAML headers | 100 host-specific headers inspected; names and manual metadata matched |
| Claude auto metadata for eligible skills | `disable-model-invocation: false` rendered for eligible auto selections |
| Installer and bundled Python helper syntax | Parsed successfully |
| Default model-role TOML | Parsed successfully |
| Existing personal configuration and skills | All 84 tracked files retained their original content hashes |
| Installed optional skill references | Resolved paths; no unexpanded placeholders |
| Ordinary `codex debug prompt-input` | Additional 12 skills absent from automatic discovery |

## Failed and limited observations

The first optional-skill validation attempt failed because Claude's `disable-model-invocation` field was present in canonical frontmatter. Codex's validator rejected it. Canonical files now omit that field; the Claude renderer emits it only for Claude output. Final native validation passed.

An explicit `$how` prompt through `codex debug prompt-input` did not inject the skill body. That command builds startup context without running a model turn, so this observation does not establish failed or successful turn-time skill invocation. The distinction is explained in the invocation-pipeline comments in the [Codex issue discussion](https://github.com/openai/codex/issues/40600). Manual invocation support is documented in [Codex skills](https://learn.chatgpt.com/docs/build-skills).

No model-backed workflow, live multi-model panel, new test suite, GitHub publication, or Claude model run was performed. Claude output was rendered and structurally inspected; full Claude Code discovery and behavior remain unverified. Use the supplied compatibility notes and report missing runtime capabilities honestly.
