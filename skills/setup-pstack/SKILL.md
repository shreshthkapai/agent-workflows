---
name: setup-pstack
description: Configure which models pstack uses per role and at what reasoning budget. Detects your available models and writes the shared model registry that overrides the skill defaults. Use for /setup-pstack, "configure pstack models", "pstack budget", or changing pstack's model choices.
disable-model-invocation: true
---

# Setup pstack

Write `~/.config/agent-workflows/models.toml`, the model registry that sets pstack's model per role. Claude Code, Codex, and Grok all read it, through `aw-run`.

## Steps

### 1. Detect available models

Detect only for the CLIs on `PATH`. Codex: run `codex debug models` and take the `slug` of each entry with `"visibility": "list"`, with its `supported_reasoning_levels`. Claude Code: the CLI accepts the aliases `opus`, `sonnet`, `haiku`, and `fable`, or a full model name. It has no listing command, so treat those aliases as detected and ask the user to paste any full name they want. Grok: run `grok models` and take each model id it lists. Never write a model you have not confirmed is available. The value `inherit` is always valid even though it is not a detected model.

### 2. Load current state

The default role-to-model mapping is the registry shape shown in step 5 below. If `~/.config/agent-workflows/models.toml` already exists, read it and treat its `budget` and its roles as the current choices. Otherwise start from those defaults. A role not in step 5, such as `how_critics`, is from a retired role. Drop it.

### 3. Budget, map, and confirm

**(a) Ask for a budget.** Ask with the CLI's structured question tool when it has one, otherwise in plain text. Offer these four options with these exact labels, and name the current budget when the registry records one. With no registry, say that `large` matches the skill defaults.

- `unlimited — max reasoning`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

**(b) Apply it.** The registry's `budget` sets the starting effort of every role, panel entries included, to `max`, `xhigh`, `high`, or `medium`, on the ladder `max` > `xhigh` > `high` > `medium` > `low`. All three CLIs accept every level on that ladder. An entry may set its own effort and speed as `model:effort` or `model:effort:fast`, which overrides the budget. Only Codex models have a fast tier. `aw-run` applies both. `inherit` does not change.

**(c) Show the roles and confirm.** Show every role with its model, provider, and effort at the chosen budget, marking any model not in the detected set as needing a choice. Also list each role step 2 dropped. Ask whether to accept as-is or change specific roles, offering the detected models plus `inherit` (the role runs on the parent session's model) as the options. For panel roles (`arena_runners`, `architect_runners`, `interrogate_reviewers`) the value is a list, and one subagent runs per entry, `inherit` entries included, so the list length sets the count. `arena_cross_judge_pool` is also a list, but Arena selects one value from it whose provider differs from the parent's when possible. `swarm_workers` is the default model for every worker unless a race or comparison assigns another model per arm.

Each model entry names its `provider`, `claude`, `codex`, or `grok`, and that CLI's subscription pays for every call on it. Show how many roles each provider carries so the user can balance the subscriptions. Each model also names a `fallback` list of models on other providers. `aw-run` resolves a model whose CLI is not installed to the first installed model in that list, and retries down the list when a provider reports a usage limit.

### 4. Validate

Every model written must be in the detected set. `inherit` always passes. Each `fallback` must name another model in the registry. If a chosen model is not available, stop and ask again. Then run `aw-run --resolve <role>` for every role and fix any error it prints.

### 5. Write the registry

Write `~/.config/agent-workflows/models.toml` with a `budget` line, one `[models.<name>]` table per model, and one line per role, using the role names the workflow skill uses. Overwrite the whole file so re-runs stay idempotent. Shape:

```toml
# pstack model configuration. One line per role. Delete a role to fall back to the skill default.
# "inherit" as a value: the role runs on the parent session's model. Inherit entries in a panel list still count toward its fan-out.
budget = "large"

[models.opus]
provider = "claude"
model = "opus"
fallback = ["sol", "grok"]

[models.sol]
provider = "codex"
model = "gpt-6.1-sol"
fallback = ["grok", "opus"]

[models.grok]
provider = "grok"
model = "grok-4.7"
fallback = ["sol", "opus"]

[roles]
feature_refactoring = "sol"
bug_fix = "sol"
perf_issue = "sol"
hillclimb = "sol"
judgment_prose = "opus"
hardest_tasks = "opus"
how_explorer = "sol"
how_explainer = "opus"
why_investigators = "sol"
why_synthesizer = "opus"
reflect_tooling = "sol"
reflect_judgment = "opus"
arena_runners = ["opus", "sol"]
arena_cross_judge_pool = ["opus", "sol"]
swarm_workers = "sol"
architect_runners = ["opus", "sol"]
interrogate_reviewers = ["opus", "sol"]
```

### 6. Confirm

Tell the user the registry was written and that it applies to the next spawn in every CLI. Re-running this skill updates it.

### 7. Offer a verification skill (optional)

Check whether the project has a way to drive the real app for proof (a `verify-*` skill, or an existing harness). If not, offer once: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work? I can generate one with /create-verification-skill." On yes, invoke `/create-verification-skill` (resolves wherever pstack is installed: project or user skills). On no, move on without pushing.

### 8. Offer a formal verification skill (optional)

Check whether the project already has a formal verification skill (a project skill that runs a model checker, a proof, or another verifier against the code). If not, offer once: "want a formal verification skill, so agents can prove a key property of your code holds in every case in scope, not only the cases tests reach? I can generate one with /create-formal-verification-skill." On yes, invoke `/create-formal-verification-skill` (resolves wherever pstack is installed: project or user skills). On no, move on without pushing.
