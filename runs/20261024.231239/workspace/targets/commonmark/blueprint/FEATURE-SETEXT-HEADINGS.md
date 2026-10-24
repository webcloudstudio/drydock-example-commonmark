# FEATURE: Setext Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders CommonMark setext headings. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md, FEATURE-ATX-HEADINGS.md |
| Provides    | Setext heading parsing and rendering |
| Consumes    | commonmark |

## Purpose

Recognize setext headings formed by paragraph text followed by an underline of `=` or `-` characters, with up to three leading spaces and optional trailing spaces or tabs. Parse the accumulated heading content as inline text. Where an underline could be either a setext heading or a thematic break, apply CommonMark precedence and context rules.

## Programmatic Acceptance

=== AC setext-headings-conformance ===
Intent: The executable passes every supplied example in the Setext headings section.
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
        "--pattern", "Setext headings",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC setext-headings-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 setext heading rules.
- Preserve supplied scoring assets unchanged.
