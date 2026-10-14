#!/usr/bin/env python3
"""Install pstack skills, agents, the model registry, and aw-run for Claude Code or Codex."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

PACKAGE = Path(__file__).resolve().parent
SKILLS = PACKAGE / "skills"
AGENTS = PACKAGE / "agents"
HOME = Path.home()
REGISTRY = Path(os.environ.get("XDG_CONFIG_HOME", HOME / ".config")) / "agent-workflows" / "models.toml"
BIN = HOME / ".local" / "bin" / "aw-run"
CODEX_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
MANUAL = re.compile(r"^disable-model-invocation:\s*(true|false)\s*\n", re.M)


def frontmatter(text):
    if not text.startswith("---\n") or "\n---" not in text[4:]:
        raise ValueError("missing YAML frontmatter")
    end = text.index("\n---", 4) + 1
    return text[4:end], text[end:]


def manual_default(name):
    match = MANUAL.search(frontmatter((SKILLS / name / "SKILL.md").read_text())[0])
    return bool(match) and match.group(1) == "true"


def render_skill(text, runtime, manual):
    head, body = frontmatter(text)
    head = MANUAL.sub("", head)
    if runtime == "claude" and manual:
        head += "disable-model-invocation: true\n"
    if runtime == "codex":  # Codex's validator rejects keys outside its own set.
        head = "".join(line for line in head.splitlines(keepends=True)
                       if line.split(":", 1)[0] in CODEX_KEYS or line.startswith((" ", "\t")))
    return "---\n" + head + body


def render_agent(text, runtime):
    if runtime == "claude":
        return text
    head, body = frontmatter(text)
    fields = dict(re.findall(r"^(name|description):\s*(.+)$", head, re.M))
    body = body.split("---", 1)[1].strip() + "\n"
    return (f"name = {json.dumps(fields['name'])}\n"
            f"description = {json.dumps(fields['description'])}\n"
            f"developer_instructions = {json.dumps(body)}\n")


def plan(args):
    available = sorted(path.name for path in SKILLS.iterdir() if (path / "SKILL.md").is_file())
    selected = available if args.skills == "all" else list(dict.fromkeys(filter(None, map(str.strip, args.skills.split(",")))))
    automatic = set(filter(None, map(str.strip, args.auto.split(","))))
    unknown = (set(selected) | automatic) - set(available)
    if unknown:
        raise SystemExit("Unknown skills: " + ", ".join(sorted(unknown)))
    if automatic - set(selected):
        raise SystemExit("Every --auto skill must also be selected with --skills")
    root = HOME / ".claude" if args.runtime == "claude" else Path(os.environ.get("CODEX_HOME", HOME / ".codex"))
    skills_dir = (args.dest or root / "skills").expanduser().resolve()
    suffix = ".md" if args.runtime == "claude" else ".toml"
    files = {}
    for name in selected:
        manual = manual_default(name) and name not in automatic
        files[skills_dir / name] = ("skill", name, manual)
    for agent in sorted(AGENTS.glob("*.md")):
        files[root / "agents" / (agent.stem + suffix)] = ("agent", agent, None)
    files[REGISTRY] = ("registry", PACKAGE / "config" / "models.toml", None)
    files[BIN] = ("bin", PACKAGE / "bin" / "aw-run", None)
    return files


def install(files, runtime, force):
    conflicts = [str(path) for path, (kind, source, _) in files.items()
                 if path.exists() and kind != "registry" and not force
                 and not (kind == "bin" and path.read_bytes() == source.read_bytes())]
    if conflicts:
        raise SystemExit("Existing files would be overwritten (pass --force): " + ", ".join(conflicts))
    for path, (kind, source, manual) in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if kind == "skill":
            with tempfile.TemporaryDirectory(prefix=".pstack-", dir=path.parent) as temporary:
                staged = Path(temporary) / source
                shutil.copytree(SKILLS / source, staged)
                skill = staged / "SKILL.md"
                skill.write_text(render_skill(skill.read_text(), runtime, manual))
                if runtime == "codex":
                    (staged / "agents").mkdir(exist_ok=True)
                    policy = "false" if manual else "true"
                    (staged / "agents" / "openai.yaml").write_text(f"policy:\n  allow_implicit_invocation: {policy}\n")
                if path.exists():
                    shutil.rmtree(path)
                staged.rename(path)
        elif kind == "agent":
            path.write_text(render_agent(source.read_text(), runtime))
        elif kind == "registry":
            if not path.exists():  # Preserve the user's model choices.
                shutil.copyfile(source, path)
        else:
            shutil.copyfile(source, path)
            path.chmod(0o755)


def uninstall(files):
    for path, (kind, *_ ) in files.items():
        if kind == "skill" and path.is_dir():
            shutil.rmtree(path)
        elif kind == "agent" and path.is_file():
            path.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", choices=["claude", "codex"])
    parser.add_argument("--skills", help="comma-separated skill names, or all")
    parser.add_argument("--auto", default="", help="selected skills the model may invoke on its own")
    parser.add_argument("--dest", type=Path, help="skill directory; defaults to the runtime's personal skills")
    parser.add_argument("--list", action="store_true", help="list skills and their default invocation")
    parser.add_argument("--dry-run", action="store_true", help="print the plan without writing")
    parser.add_argument("--force", action="store_true", help="replace installed copies of these skills and agents")
    parser.add_argument("--uninstall", action="store_true", help="remove the selected skills and the agents")
    args = parser.parse_args()
    if args.list:
        for path in sorted(SKILLS.iterdir()):
            if (path / "SKILL.md").is_file():
                print(f"{path.name:52} {'manual' if manual_default(path.name) else 'auto'}")
        return
    if not args.runtime or not args.skills:
        parser.error("choose --runtime and --skills, or use --list")
    files = plan(args)
    if args.dry_run:
        for path, (kind, _, manual) in files.items():
            note = ("manual" if manual else "auto") if kind == "skill" else kind
            print(f"{'remove' if args.uninstall else 'write'} {path} ({note})")
        return
    if args.uninstall:
        uninstall(files)
    else:
        install(files, args.runtime, args.force)
    print(f"{'Removed' if args.uninstall else 'Installed'} {sum(k == 'skill' for k, *_ in files.values())} skills for {args.runtime}")


if __name__ == "__main__":
    main()
