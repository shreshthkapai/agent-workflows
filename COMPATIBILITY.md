# Compatibility

The Markdown skill structure is supported by Codex and Claude Code, but invocation metadata, agent APIs, model controls, global instruction files, and transcript/tool availability differ. The installer handles file paths and invocation metadata; the runtime guides handle capability and model interpretation. Runtime limitations remain visible.

Official references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [Claude Code agents](https://code.claude.com/docs/en/sub-agents).

## Additional optional workflows

All twelve are manual by default, including those whose meaning could support automatic selection if a consumer opts in.

| Skill | Original host assumptions | Adapted behavior |
| --- | --- | --- |
| how | Cursor Task agents, model aliases, prompt references | Source-backed explanation with optional bounded native exploration |
| why | Cursor MCP discovery, seven investigators and transcript assumptions | Available authorized evidence; facts, inference, contradictions and coverage gaps |
| architect | Mandatory How/Arena composition and implementation after design | Scoped design; implementation only within the actual request |
| automate-me | Cursor history locations, create-skill, automatic PR delivery | Current or specifically authorized history; concrete preference draft before durable changes |
| setup-pstack | `~/.cursor/rules/pstack-models.mdc`, always-applied overrides | Existing portable registry and verified native model capabilities |
| typescript-best-practices | Mostly language guidance, with cross-skill references and blanket rules | Version-aware TypeScript guidance; preserves valid casts and runtime checks |
| poteto-mode | Cursor wrapper and mandatory skill chains | Optional router respecting the installed catalog, invocation policies and scope |
| authoring-a-skill | Cursor create-skill and automatic PR | Optional native authoring workflow, with structural checks and scoped installation |
| eval | Cursor candidate agents and transcript storage | Equivalent isolated environments, blinded common judging, available execution evidence |
| session-pickup | Cursor transcripts/cloud handoffs and inherited claims | Supplied or authorized handoff checked against current artifacts |
| pause-safely | Cursor restart/compaction and automatic WIP commit | Intent-based pause and durable handoff; no automatic commit or process termination |
| opening-a-pr | deslop, babysit, automatic publication after other playbooks | Requested PR delivery; bounded monitoring only when authorized |

No whole workflow required exclusion: the purposes are portable, while these original integration details are omitted. The original external Cursor tools are not bundled, installed, or emulated.

## Existing workflows and principles

The package includes the previously adapted seven workflows, eleven task/continuation/planning workflows, and twenty principles. Portable paths replace account-specific paths. Runtime guides resolve native spawning and model roles. The defaults are selective and proportionate: no mandatory full-stack read, arbitrary file quotas, automatic PR creation, recurring review panels, or implied permission for unrelated tests and configuration changes.

Existing personal invocation settings are not rewritten when the additional skills are installed. Consumers choose their own installed subset. Package installation itself defaults to manual invocation.

## Capability limits

- Model panels require native delegation. A partial panel or same-model review is reported accurately. Cross-family review requires supported configured model choices; Claude Code receives no automatic access to GPT models from this package.
- Model/effort inheritance leaves native settings untouched. The actual agent setting may depend on host configuration and profiles; it must be reported rather than inferred from a registry alone.
- Transcript-based evidence needs a positively identified available transcript. A lead-authored digest is labeled and cannot independently prove execution history.
- Git hosting, observability, analytics, browser drivers, profilers, and native creator plugins are optional. Missing capabilities produce gaps rather than invented results or automatic installations.
- The provided logging helper uses POSIX `fcntl` locking. Native Windows requires a suitable logging alternative; the instructions and ordinary installer do not depend on that helper unless a trail is requested.
- Ending a task does not close the interactive CLI or create persistent background execution.

Structural validation, rendering, policy inspection, and Codex discovery are configuration checks. Live workflow behavior and full Claude Code execution have not been established by those checks.
