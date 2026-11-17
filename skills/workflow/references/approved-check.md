# Approved check

Run this before you call work done, and before it leaves the machine, whenever the work was built from something the user approved: a design or mockup, a spec, a plan, a list of steps, or their own words. The `aw-gate` hook pauses the first try of a `git push`, PR, release, publish, or deploy, and lets the same command through on a retry.

1. Collect the approved source as it stands now: the image, file, artifact, or the user's message. Never a brief, a summary, or your memory of it.
2. Collect the result in the same form. For a design, render or screenshot every view and state the source shows, in the source's own example situations. For anything else, the diff or the output.
3. Run a fresh checker with `aw-run swarm_workers --read-only`, or with `judgment_prose` when `swarm_workers` resolves to the model that built the work. Give it the paths to both sets and only this task: list every difference between the approved source and the result, view by view or item by item, including differences that look like improvements. Never pass your brief, your summary, or a delegate's report, so the checker cannot inherit a wrong belief about the source.
4. Show the user each approved view or item next to its result, in one place, side by side, with the checker's list and any difference you found yourself. Ask for the user's OK, on each difference when there are any. A difference the user has not approved is a bug. Fix it, or keep it only on their word.
5. Then report the work done, or retry the outgoing command. When nothing the user approved is involved, tell the user so and retry it.

Anything public, such as a PR or release description, puts each approved view next to its result under the same label, and names every difference the user approved.
