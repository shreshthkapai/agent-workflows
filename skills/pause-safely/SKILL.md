---
name: pause-safely
description: "Pause active work cleanly when the user asks to stop, go offline, or leave a resumable checkpoint. A request to keep working is not a pause."
---

# Pause Safely

Read {{RUNTIME_GUIDE}} for active operation and handoff capabilities. Treat an explicit pause as a stop request; if the user says to continue, keep working within the existing scope.

Finish the current safe, atomic step when practical, then start no new work. Preserve partial state and describe broken or incomplete artifacts honestly. Do not automatically kill processes or sibling agents, commit, revert, push, or open a pull request.

When resumption needs a handoff, write one concise note at a user- or project-designated durable path. Include the intent, current state, evidence and checks, running operations, gaps, relevant files, and the first useful next action. Do not assume temporary storage survives a restart. Avoid duplicating an existing decision trail.

Report where the work stopped and what remains. A pause is a checkpoint, not a claim of completion.
