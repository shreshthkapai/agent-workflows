#!/usr/bin/env python3
"""Append one locked, timestamped decision row to a task TSV log."""

from __future__ import annotations

import argparse
import fcntl
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


HEADER = b"ts\tphase\tdecision\twhy\tevidence\tresult"
CELL_BREAKS = re.compile(r"[\t\r\n]+")
FORMULA_PREFIXES = "=+-@"


def cell(value: str) -> str:
    """Keep a value on one TSV line and protect spreadsheet formula prefixes."""
    value = CELL_BREAKS.sub(" ", value)
    first_nonspace = value.lstrip()[:1]
    if first_nonspace and first_nonspace in FORMULA_PREFIXES:
        value = "'" + value
    return value


def append_row(path: Path, fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    row = "\t".join(fields).encode("utf-8") + b"\n"

    # Lock the log inode itself so concurrent calls serialize header creation
    # and appends without a separate lock file becoming part of the audit trail.
    with path.open("a+b") as stream:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        stream.seek(0)
        first_line = stream.readline()
        if first_line:
            if first_line.endswith(b"\r\n"):
                first_line = first_line[:-2]
            elif first_line.endswith(b"\n"):
                first_line = first_line[:-1]
            if first_line != HEADER:
                raise ValueError(
                    f"refusing to append: {path} has an incompatible TSV header"
                )

        stream.seek(0, os.SEEK_END)
        size = stream.tell()
        if size == 0:
            stream.write(HEADER + b"\n")
        else:
            stream.seek(-1, os.SEEK_END)
            has_final_newline = stream.read(1) == b"\n"
            stream.seek(0, os.SEEK_END)
            if not has_final_newline:
                stream.write(b"\n")
        stream.write(row)
        stream.flush()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Append one timestamped decision row to an exact-schema TSV log."
    )
    parser.add_argument("filename", help="TSV log path")
    parser.add_argument("phase")
    parser.add_argument("decision")
    parser.add_argument("why")
    parser.add_argument("evidence")
    parser.add_argument("result")
    args = parser.parse_args()

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )
    fields = [
        timestamp,
        *(
            cell(value)
            for value in (
                args.phase,
                args.decision,
                args.why,
                args.evidence,
                args.result,
            )
        ),
    ]

    try:
        append_row(Path(args.filename), fields)
    except (OSError, ValueError) as exc:
        print(f"log.py: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
