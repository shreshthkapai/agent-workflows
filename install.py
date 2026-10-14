#!/usr/bin/env python3
"""Install selected workflow skills with runtime-specific invocation metadata."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import tempfile


PACKAGE = Path(__file__).resolve().parent


def names(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def render(content, bindings):
    for key, value in bindings.items():
        content = content.replace("{{" + key + "}}", str(value))
    unresolved = re.findall(r"\{\{[A-Z_]+\}\}", content)
    if unresolved:
        raise ValueError("Unresolved template fields: " + ", ".join(sorted(set(unresolved))))
    return content


def skill_text(content, runtime, automatic):
    parts = content.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("Skill must start with YAML frontmatter")
    if runtime == "claude":
        frontmatter = parts[1].rstrip() + "\ndisable-model-invocation: "
        frontmatter += "false" if automatic else "true"
        return "---" + frontmatter + "\n---" + parts[2]
    return content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", choices=["codex", "claude"])
    parser.add_argument("--skills", help="Comma-separated skill names, or all; no selection by default")
    parser.add_argument("--auto", default="", help="Opt selected eligible skills into automatic invocation")
    parser.add_argument("--dest", type=Path, help="Skill directory; defaults to the runtime's personal skills")
    parser.add_argument("--models", type=Path, help="Use an existing workflow model-role registry")
    parser.add_argument("--list", action="store_true", help="List available skills and automatic-mode eligibility")
    parser.add_argument("--dry-run", action="store_true", help="Render and check the installation without writing")
    args = parser.parse_args()
    catalog = json.loads((PACKAGE / "catalog.json").read_text())
    entries = catalog["skills"]
    if args.list:
        for name, entry in entries.items():
            eligibility = "auto available" if entry["auto_supported"] else "manual only"
            print(f"{name:52} {entry['category']:10} {eligibility}")
        return
    if not args.runtime or not args.skills:
        parser.error("Choose --runtime and --skills, or use --list")
    selected = list(entries) if args.skills == "all" else list(dict.fromkeys(names(args.skills)))
    automatic = set(names(args.auto))
    unknown = (set(selected) | automatic) - set(entries)
    if unknown:
        parser.error("Unknown skills: " + ", ".join(sorted(unknown)))
    if not selected:
        parser.error("Select at least one skill")
    if automatic - set(selected):
        parser.error("Every --auto skill must also be selected with --skills")
    manual_only = [name for name in automatic if not entries[name]["auto_supported"]]
    if manual_only:
        parser.error("These workflows require explicit invocation: " + ", ".join(sorted(manual_only)))

    default_root = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    if args.runtime == "claude":
        default_root = Path.home() / ".claude"
    destination = (args.dest or default_root / "skills").expanduser().resolve()
    runtime_root = destination.parent
    support = runtime_root / "agent-workflows"
    host_instructions = runtime_root / ("AGENTS.md" if args.runtime == "codex" else "CLAUDE.md")
    existing_rules = runtime_root / "workflow-rules.md"
    models = args.models.expanduser().resolve() if args.models else support / "models.toml"
    if args.models and not models.is_file():
        parser.error("--models must name an existing file")
    bindings = {
        "GLOBAL_INSTRUCTIONS": host_instructions if host_instructions.is_file() else support / "instructions.md",
        "SKILLS_ROOT": destination,
        "MODEL_REGISTRY": models,
        "RUNTIME_GUIDE": support / "runtime.md",
        "WORKFLOW_RULES": existing_rules if existing_rules.is_file() else support / "workflow-rules.md",
        "INVOKE": "$" if args.runtime == "codex" else "/",
    }
    if destination.is_relative_to(PACKAGE) or PACKAGE.is_relative_to(destination):
        parser.error("Choose a destination outside the package source")

    support_sources = {
        "runtime.md": PACKAGE / "adapters" / args.runtime / "runtime.md",
        "instructions.md": PACKAGE / "runtime" / "instructions.md",
        "LICENSE": PACKAGE / "LICENSE",
        "NOTICE.md": PACKAGE / "NOTICE.md",
    }
    if not existing_rules.is_file():
        support_sources["workflow-rules.md"] = PACKAGE / "runtime" / "workflow-rules.md"
    if not args.models:
        support_sources["models.toml"] = PACKAGE / "config" / "models.toml"
    support_content = {name: render(path.read_text(), bindings) for name, path in support_sources.items()}
    conflicts = [str(destination / name) for name in selected if (destination / name).exists()]
    for name, content in support_content.items():
        target = support / name
        if target.exists() and target.read_text() != content:
            if name == "models.toml":
                continue  # Preserve the consumer's configured model choices.
            conflicts.append(str(target))
    if conflicts:
        parser.error("Existing files would be overwritten; preserved: " + ", ".join(conflicts))

    rendered = {}
    for name in selected:
        source = PACKAGE / "skills" / name
        content = render((source / "SKILL.md").read_text(), bindings)
        rendered[name] = skill_text(content, args.runtime, name in automatic)
        for path in source.rglob("*"):
            if path.is_symlink():
                parser.error("Skill source contains a symlink: " + str(path))
    overview = {
        "runtime": args.runtime,
        "destination": str(destination),
        "support": str(support),
        "models": str(models),
        "selected": {name: "auto" if name in automatic else "manual" for name in selected},
        "writes_global_instructions": False,
        "writes_agent_profiles": False,
        "dry_run": args.dry_run,
    }
    if args.dry_run:
        print(json.dumps(overview, indent=2))
        return

    destination.mkdir(parents=True, exist_ok=True)
    support.mkdir(parents=True, exist_ok=True)
    for name, content in support_content.items():
        target = support / name
        if not target.exists():
            with target.open("x") as output:
                output.write(content)
    for name in selected:
        source = PACKAGE / "skills" / name
        with tempfile.TemporaryDirectory(prefix=".workflow-install-", dir=destination) as temporary:
            staged = Path(temporary) / name
            shutil.copytree(source, staged)
            (staged / "SKILL.md").write_text(rendered[name])
            if args.runtime == "codex":
                agents = staged / "agents"
                agents.mkdir(exist_ok=True)
                policy = "true" if name in automatic else "false"
                (agents / "openai.yaml").write_text("policy:\n  allow_implicit_invocation: " + policy + "\n")
            else:
                # Codex metadata has no role in Claude skill discovery.
                metadata = staged / "agents" / "openai.yaml"
                if metadata.exists():
                    metadata.unlink()
                    if not any(metadata.parent.iterdir()):
                        metadata.parent.rmdir()
            staged.rename(destination / name)
    print(json.dumps(overview, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
