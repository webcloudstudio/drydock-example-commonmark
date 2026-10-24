# FEATURE: ATX Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders CommonMark ATX headings. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md |
| Provides    | ATX heading parsing and rendering |
| Consumes    | commonmark |

## Purpose

Recognize ATX headings with one to six unescaped opening `#` characters, up to three leading spaces, and a space, tab, or end of line after the opening sequence. Strip permitted closing hashes and surrounding heading whitespace before parsing the content as inline text.

## Programmatic Acceptance

=== AC atx-headings-conformance ===
Intent: The executable passes every supplied example in the ATX headings section.
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
        "--pattern", "ATX headings",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC atx-headings-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 ATX heading rules.
- Preserve supplied scoring assets unchanged.
