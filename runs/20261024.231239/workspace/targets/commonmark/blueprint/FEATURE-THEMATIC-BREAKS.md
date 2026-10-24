# FEATURE: Thematic Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders CommonMark thematic breaks. |
| Depends On  | FEATURE-CLI.md |
| Provides    | Thematic break parsing and rendering |
| Consumes    | commonmark |

## Purpose

Recognize a thematic break as a line with up to three leading spaces, at least three matching `-`, `_`, or `*` characters, and optional spaces or tabs between and after those characters. Render each thematic break as an HTML thematic break.

## Programmatic Acceptance

=== AC thematic-breaks-conformance ===
Intent: The executable passes every supplied example in the Thematic breaks section.
Suite: scoped
Probe: --dump-tests
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program", "./commonmark",
        "--spec", "sources/spec.txt",
        "--pattern", "Thematic breaks",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC thematic-breaks-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 thematic-break rules.
- Preserve supplied scoring assets unchanged.
