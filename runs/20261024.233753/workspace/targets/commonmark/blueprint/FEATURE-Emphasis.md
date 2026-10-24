# FEATURE: Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark emphasis and strong emphasis. |
| Depends On  | ARCHITECTURE.md |
| Provides    | emphasis, strong emphasis |

## Purpose

Parse emphasis and strong emphasis in inline content according to CommonMark 0.31.2, including delimiter-run rules, nesting, and ambiguity resolution.

## Programmatic Acceptance

=== AC emphasis-conformance ===
Intent: The implementation passes every supplied example in the “Emphasis and strong emphasis” section.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        "./commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "Emphasis and strong emphasis",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC emphasis-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow the supplied CommonMark 0.31.2 specification.
- Do not use a public Markdown implementation as the parser.
- Keep supplied conformance assets under `sources/` unchanged.
