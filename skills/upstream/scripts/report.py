#!/usr/bin/env python3
"""Report what changed in upstream pstack since the port's last verbatim import.

Usage: report.py [--port PATH] [--since REV]
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

CACHE = Path.home() / ".cache" / "agent-workflows" / "upstream" / "plugins.git"
SOURCES = {
    "cursor": ("https://github.com/cursor/plugins.git", ["main"]),
    "poteto": ("https://github.com/poteto/plugins.git", ["main", "pstack/*"]),
}
RENAMES = {"poteto-mode": "workflow", "poteto-help": "pstack-help", "poteto-agent": "delegate"}
DROPPED = {"make-bot-ui", "automations", "docs"}
IMPORT = re.compile(r"Import upstream pstack verbatim from cursor/plugins@([0-9a-f]+)")


def git(*args, repo=CACHE, check=True):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if check and result.returncode:
        sys.exit(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def sync():
    if not CACHE.exists():
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "-q", "--bare", "--filter=blob:none", SOURCES["cursor"][0], str(CACHE)], check=True)
    for name, (url, branches) in SOURCES.items():
        specs = [f"+refs/heads/{b}:refs/upstream/{name}/{b}" for b in branches]
        git("fetch", "-q", "--prune", "--filter=blob:none", url, *specs)


def port_checkout(explicit):
    if explicit:
        return Path(explicit).expanduser()
    aw = shutil.which("aw")
    if not aw:
        sys.exit("aw is not on PATH. Pass --port with the agent-workflows checkout.")
    return Path(aw).resolve().parents[1]


def area(path):
    """Map an upstream path to the port's unit: ('skill' | 'agent' | 'other', port name)."""
    parts = path.split("/")[1:]
    if parts[0] == "skills" and len(parts) > 2:
        return "skill", parts[1]
    if parts[0] == "agents" and len(parts) == 2:
        return "agent", parts[1].removesuffix(".md")
    return "other", "/".join(parts)


def words(rev, prefix):
    listing = git("ls-tree", "-r", "--name-only", rev, "--", prefix, check=False).split()
    return sum(len(git("show", f"{rev}:{p}", check=False).split()) for p in listing if p.endswith((".md", ".txt")))


def description(rev, skill):
    text = git("show", f"{rev}:pstack/skills/{skill}/SKILL.md", check=False)
    match = re.search(r"^description:\s*(.+)$", text, re.M)
    return match.group(1).strip().strip('"') if match else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="agent-workflows checkout (default: where `aw` links)")
    parser.add_argument("--since", help="upstream commit to compare from (default: the port's last import)")
    args = parser.parse_args()

    port = port_checkout(args.port)
    log = git("log", "--format=%H %s", repo=port)
    imports = [(sha, m.group(1)) for sha, _, subject in (l.partition(" ") for l in log.splitlines())
               if (m := IMPORT.search(subject))]
    if not imports and not args.since:
        sys.exit(f"No 'Import upstream pstack verbatim' commit in {port}. Pass --since.")
    port_import, base = imports[0] if imports else (None, args.since)
    base = args.since or base

    sync()
    head = "refs/upstream/cursor/main"
    base = git("rev-parse", base).strip()
    print(f"# Upstream pstack since {base[:7]}\n")
    print(f"Port checkout: {port}. Port import commit: {port_import[:7] if port_import else 'none'}.")
    print(f"Upstream cache: {CACHE}. Head: cursor/plugins@{git('rev-parse', '--short', head).strip()}.\n")

    print("## cursor/plugins commits\n")
    commits = git("log", "--date=short", "--format=- %h %ad %s", f"{base}..{head}", "--", "pstack").strip()
    print((commits or "None.") + "\n")

    print("## poteto/plugins branches\n")
    upstream_skills = set(git("ls-tree", "--name-only", head, "pstack/skills/").split())
    for ref in git("for-each-ref", "--format=%(refname)", "refs/upstream/poteto").split():
        tip = git("log", "-1", "--date=short", "--format=%h %ad %s", ref).strip()
        only = sorted(p.rsplit("/", 1)[1] for p in set(git("ls-tree", "--name-only", ref, "pstack/skills/").split()) - upstream_skills)
        print(f"- {ref.removeprefix('refs/upstream/poteto/')}: {tip}. Skills missing from cursor/plugins: {', '.join(only) or 'none'}.")
    print()

    changes = {}
    for line in git("diff", "--name-status", "-M", base, head, "--", "pstack").splitlines():
        status, *paths = line.split("\t")
        for path in paths:
            kind, name = area(path)
            changes.setdefault((kind, name), set()).add(status[0])

    print("## Changed units\n")
    print("| Kind | Upstream | Port | Change | Words before > after | Port has edits |")
    print("| --- | --- | --- | --- | --- | --- |")
    described = []
    for (kind, name), statuses in sorted(changes.items()):
        port_name = RENAMES.get(name, name)
        if kind == "skill":
            prefix, port_path = f"pstack/skills/{name}", f"skills/{port_name}"
        elif kind == "agent":
            prefix, port_path = f"pstack/agents/{name}.md", f"agents/{port_name}.md"
        else:
            prefix, port_path = f"pstack/{name}", None
        before, after = words(base, prefix), words(head, prefix)
        change = "added" if statuses == {"A"} else "removed" if statuses == {"D"} else "modified"
        if name.split("/")[0] in DROPPED:
            edits = "dropped in port"
        elif port_path is None:
            edits = "not ported"
        elif port_import:
            edits = "no" if subprocess.run(["git", "-C", str(port), "diff", "--quiet", port_import, "HEAD", "--", port_path]).returncode == 0 else "yes"
        else:
            edits = "unknown"
        print(f"| {kind} | {name} | {port_name if port_path else '-'} | {change} | {before} > {after} | {edits} |")
        if kind == "skill" and description(base, name) != description(head, name):
            described.append((name, description(base, name), description(head, name)))

    if described:
        print("\n## Description changes\n")
        for name, old, new in described:
            print(f"- {name}\n  - before: {old}\n  - after: {new}")

    print(f"\nRead a unit's diff with `git -C {CACHE} diff {base[:7]} {head} -- <upstream path>`, "
          f"and one commit with `git -C {CACHE} show <sha> -- pstack`.")


if __name__ == "__main__":
    main()
