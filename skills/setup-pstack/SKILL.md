---
name: setup-pstack
description: "Propose or update portable per-role model settings for this package. Use when the user asks to configure its model choices or runtime settings."
---

# Setup pstack

Use this skill to configure role-based model choices without assuming one host's settings format. Read {{RUNTIME_GUIDE}} and inspect {{MODEL_REGISTRY}} before proposing values; use the runtime guide to locate authoritative host settings and availability information.

First inspect the current configuration and identify the roles the package actually uses. Inherit host defaults where the user has not chosen a model. Present any unresolved role choices and propose only models confirmed as available by the host; registry entries alone do not prove access. Do not infer that an old alias, provider, or role type is available here.

When applying an authorized change, preserve unrelated settings and edit only the concrete configuration surface supported by the runtime. Avoid replacing a whole native config file or creating a second override layer without a demonstrated need. If a requested role or model cannot be represented, explain the limitation and offer the closest supported option.

Report the destination, changed role mappings, and any roles left on defaults. Do not claim a setting applies across sessions or runtimes unless the host documents that behavior.
