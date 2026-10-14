---
name: authoring-a-skill
description: "Create or revise a native agent skill when the user requests reusable workflow guidance. Use the host's supported skill format and preserve the requested scope."
---

# Authoring a Skill

Read {{RUNTIME_GUIDE}} to identify the native skill format, available validation tools, and invocation settings. Inspect the target location and any existing skill before editing.

Write only guidance that changes decisions or improves the requested workflow. Keep the description specific about purpose and use, put operational instructions in the body, and add references or assets only when the skill needs them. Preserve the user's authorization and choose explicit or automatic invocation metadata according to their request.

Use a native skill-authoring workflow when it is installed and allowed by the caller's invocation policy. Do not create a shadow manual for it. Check every referenced path and validate the actual skill with the host's structural validator when available. Structural validation does not prove the guidance works.

Show the concrete draft before durable installation unless the user explicitly authorized that exact artifact and destination. Do not add tests, commits, or publication unless requested.
