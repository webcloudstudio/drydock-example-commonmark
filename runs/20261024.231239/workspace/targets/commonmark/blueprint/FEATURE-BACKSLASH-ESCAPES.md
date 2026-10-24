# FEATURE: Backslash Escapes

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark backslash escapes and trailing-backslash hard breaks. |
| Depends On  | FEATURE-CLI.md, FEATURE-PARAGRAPHS.md |
| Provides    | inline backslash escapes, trailing-backslash hard breaks |
| Consumes    | commonmark |

## Purpose

Render a backslash followed by an ASCII punctuation character as that literal character. Preserve a backslash before any other character. In code spans, code blocks, autolinks, and raw HTML, backslashes remain literal. A backslash immediately before a line ending creates a hard break when the line continues within the same inline block.

## Behavior

- Parse escapes after block structure has been determined.
- Escape the resulting literal character for HTML text as needed.
- Render a trailing-backslash hard break as `<br />` followed by a line ending and the next line’s content.
- A trailing backslash at the end of a block remains literal.
- Do not interpret escapes inside code spans, code blocks, autolinks, or raw HTML.

## Programmatic Acceptance

=== AC backslash-escape-conformance ===
Intent: All supplied Backslash escapes examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Backslash escapes"],
    capture_output=True, text=True,
    env={**os.environ, "PYTHONPATH": f"{os.getcwd()}/sources"},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC backslash-escape-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep all supplied scoring assets unchanged.
