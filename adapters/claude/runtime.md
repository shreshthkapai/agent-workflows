# Claude Code runtime adapter

Load this guide once when needed and reuse it through the task; another supporting skill is not a reason to reread it.

Manual skills use `disable-model-invocation: true` in YAML frontmatter and are requested with `/skill-name`. Automatically eligible skills may be enabled individually. Codex's `agents/openai.yaml` does not control Claude invocation. References from another workflow do not enable manual skills automatically.

Read the actual applicable global and project `CLAUDE.md` instructions. `{{GLOBAL_INSTRUCTIONS}}` is the existing host file when present, otherwise this package's scoped guidance. Read relevant sections of `{{WORKFLOW_RULES}}` for operational rules; native host settings and user directions prevail over Codex-oriented role names in that document.

## Native agents and model choices

Use available Claude Code native general-purpose or inspection agents and a scoped brief. The lead owns design, scope, synthesis, and verification. One bounded implementation delegate is enough by default; small or unresolved work remains with the lead. Workers do not spawn agents. An inspection-only brief is an instruction, not proof of an enforced filesystem sandbox.

Resolve aliases in `{{MODEL_REGISTRY}}`, which is custom workflow data, not native Claude settings. `inherit` leaves native model and effort overrides unset. Missing optional roles use native defaults and must be reported. Preserve configured choices; do not translate GPT model names or Codex reasoning levels into supposedly equivalent Claude settings. Confirm actual supported model IDs and effort controls before applying overrides.

Codex profile names such as `worker` or `default` describe roles here; use a suitable available Claude agent. Conditional `fork_turns` instructions apply only to interfaces exposing that parameter; Claude's agent API may expose different controls. Use file pointers and self-contained briefs with the required instruction and workflow reads. Report the actual model and effort when exposed, or label them unknown.

Audit reviewers use `roles.audit_reviewer` when configured. With an inherited model, an independent review can use a separate agent but is not automatically a different model family. Report that limitation. If a workflow requires cross-family review and the host cannot supply it, report an incomplete review rather than claiming the requirement passed. Multi-model panels need supported configured models; this package does not provide a bridge to another vendor.

## Capabilities

History analysis uses the current thread or specifically supplied and authorized transcripts. It assumes no Cursor transcript directory and does not scan private global history. MCP sources, GitHub tools, browsers, profilers, authentication, and native skill-authoring plugins are optional capabilities; report unavailable pieces. The provided log helper requires a POSIX host with Python and file locking.

End-of-task completion does not terminate the interactive CLI or create a persistent background runtime. Preserve user limits and honest completion or blocker reports.
