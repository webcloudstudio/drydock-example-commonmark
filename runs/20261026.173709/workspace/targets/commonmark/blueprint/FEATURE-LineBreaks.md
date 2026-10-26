# FEATURE: Hard and Soft Line Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses hard and soft line breaks in inline content. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | hard and soft line break parsing |
| Consumes    | commonmark executable |

## Purpose

Parse line endings within paragraphs and other inline-bearing blocks according to CommonMark 0.31.2.

## Behavior

- A line ending preceded by two or more spaces produces a hard line break when it occurs within a block, not at the block’s end.
- A backslash immediately before a line ending produces a hard line break under the same conditions.
- After a hard break, ignore leading spaces on the next line.
- A line ending that is not a hard break is a soft line break. Render it as a line ending.
- Remove spaces at the end of a line and at the beginning of the following line for soft breaks.
- Do not treat line endings inside code spans or HTML tags as hard or soft breaks.
- Do not produce a hard break from trailing spaces or a backslash at the end of a block.

## Programmatic Acceptance

=== AC inline-hard-soft-breaks ===
Intent: The executable passes the complete supplied conformance slice for hard and soft line breaks.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        f"{os.getcwd()}/commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "Hard line breaks|Soft line breaks",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-hard-soft-breaks ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Preserve the supplied scoring assets unchanged.
- Resolve block structure before inline structure.
