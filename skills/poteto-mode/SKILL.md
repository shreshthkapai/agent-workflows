---
name: poteto-mode
description: "Route an explicitly requested task through the available pstack workflows and working principles. Use for {{INVOKE}}poteto-mode or when the user asks to work in this mode."
---

# Poteto Mode

Read {{GLOBAL_INSTRUCTIONS}} and {{RUNTIME_GUIDE}} before routing. Inspect the relevant entries in {{SKILLS_ROOT}} and match the user's actual outcome to one primary workflow. Add a supporting principle only when it changes a decision. Respect each skill's invocation policy and the user's stated scope.

This router helps select available guidance; it does not activate optional skills or override defaults in {{GLOBAL_INSTRUCTIONS}}. Do not assume a tool, model, plugin, command, or workflow is installed just because an upstream package mentions it. Use the runtime guide to interpret invocation and capability limits. Refer to a skill only if it is present and its policy permits use.

Apply the smallest workflow that fits. Keep the task's finish condition observable, preserve authorization boundaries, and do not add mandatory logs, delegation, design panels, tests, commits, pull requests, or other steps unless the selected workflow and user request call for them.
