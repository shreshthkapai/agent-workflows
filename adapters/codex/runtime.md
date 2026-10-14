# Codex runtime adapter

Load this guide once when needed and reuse it through the task; another supporting skill is not a reason to reread it.

Invocation metadata controls selection. Manual skills use `agents/openai.yaml` with `policy.allow_implicit_invocation: false`; request them with `$skill-name`. Automatically eligible skills may be enabled individually. A skill reference in another workflow does not override that policy.

Read the actual applicable global and project instructions. `{{GLOBAL_INSTRUCTIONS}}` is the existing host instruction file when present, otherwise this package's scoped guidance. For delegation, parallel writers, routing, or panel roles, read the corresponding sections of `{{WORKFLOW_RULES}}`.

## Native agents and model choices

Use Codex's available native agent tools; this package installs no second scheduler. The lead owns design, scope, synthesis, and actual verification. Use one implementation worker for understood bounded work when the host provides one; otherwise use an available general-purpose agent or implement directly and report the limitation. Inspection-only reviewers receive an explicit no-writes/no-spawning brief; claim sandbox enforcement only when the tool actually provides it.

Resolve role aliases from `{{MODEL_REGISTRY}}` when a workflow needs a panel. The registry is workflow data, not `config.toml`. A model or effort of `inherit` means leave that override unset and use native configured defaults. Missing optional roles also use native defaults, with the actual choice reported. Do not silently replace an unavailable explicit choice. Read any configured implementation profile rather than assuming its model.

Use a generic native agent when supplying supported model/effort overrides, avoiding profiles that pin conflicting values. If the API supports `fork_turns`, explicit overrides require `fork_turns: "none"` and a self-contained brief. Speed follows the host. Report the actual model and effort; configured intent alone is not execution evidence.

For decision-trail audits, use `roles.audit_reviewer` when present; existing registries may instead have `audit_for_sol_or_luna` and `audit_for_astra`. Use a verified lead family to resolve those. If no compatible reviewer can be selected, report an incomplete audit. Same-model independent reviews must not be described as cross-family reviews.

## Capabilities

Use only available and authorized tools and positively identified transcripts. Missing connectors, authentication, profiling tools, or transcript access remain explicit gaps. Do not install dependencies or search private session storage automatically. The log helper requires a POSIX host with Python and file locking.

Completing a skill ends its work or turn; it does not close an interactive CLI, start a daemon, create a persistent goal, or survive a stopped runtime. Preserve the caller's finish condition and limits.
