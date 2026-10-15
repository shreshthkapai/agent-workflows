---
name: upstream
description: Summarizes what changed in upstream pstack (cursor/plugins, and poteto's plugins fork) since this port last imported it. New and removed skills, and what each changed skill gained, lost, or cut. Use for /upstream.
disable-model-invocation: true
---

# Upstream

Report only. Do not edit the port. Re-syncing follows `PORTING.md` in the port checkout, and only when the user asks.

1. Run `python3 scripts/report.py` from this skill's directory. It fetches upstream into a cache and prints the commits, poteto's fork branches, a table of changed units with word counts, and description changes. It compares against the port's last `Import upstream pstack verbatim` commit. Pass `--since <rev>` when the user names another starting point.
2. Read each changed skill's and agent's diff with the command the report prints. Read the commit messages too (`git show <sha> --stat` and the body), since they state the intent.
3. Run `aw skills` to see which changed skills are auto. A changed description on an auto skill changes when the model loads it, so call that out.

## Reply

- One line with the commit count, date range, and upstream head.
- **New skills.** Name, what it does, and whether the port lacks it.
- **Removed skills.**
- **Changed skills.** One line each. Say what changed in behavior, and label it as one of new capability, rule change, cut or shortened, reworded, or fix. Give the word delta from the report. Group skills that one commit changed the same way.
- **poteto's fork.** Branches and any skills cursor/plugins lacks. Say "nothing new" when the report shows none.
- **Skipped.** Upstream files the port does not carry (docs, plugin manifests, README), in one line.
- **Worth pulling.** Your judgment of which changes the port should take. Mark the units where the report shows `Port has edits: yes`, because a re-sync must reapply those porting edits.
