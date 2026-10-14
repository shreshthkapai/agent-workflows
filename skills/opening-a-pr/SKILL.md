---
name: opening-a-pr
description: "Prepare or open a pull request when the user asks for that delivery step. Inspect the real branch and diff, and report checks accurately."
---

# Opening a Pull Request

Read {{RUNTIME_GUIDE}} for supported Git hosting tools, authentication, and action limits. Inspect the current branch, target base, complete diff, and worktree before preparing delivery. Preserve unrelated user changes and confirm that the change forms a coherent reviewable unit.

Prepare a concise, accurate title and description that explain the user-visible change, relevant implementation context, checks actually run, and remaining gaps. Use the repository's existing conventions when they help reviewers. Do not claim checks passed based on prior self-report alone.

Commit, push, or create the pull request only when the user's request authorizes those steps and the required host tools are available. Avoid destructive resets, forced shared-history changes, or rebases unless specifically authorized. Do not merge, deploy, or monitor the request unless asked. When monitoring is requested, observe actual hosting checks and review status with available tools, follow the requested finish condition or time limit, and report blockers. Address feedback only within authorized scope. Report the branch, checks, and resulting pull request link when one was actually created.
