# FEATURE: Autolinks and Raw HTML

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark autolinks and raw HTML. |
| Depends On  | ARCHITECTURE.md |
| Provides    | URI autolinks, email autolinks, inline raw HTML |

## Purpose

Parse URI and email autolinks and inline raw HTML tags, comments, declarations, processing instructions, and CDATA according to CommonMark 0.31.2.

## Programmatic Acceptance

=== AC autolinks-and-raw-html-conformance ===
Intent: The implementation passes every supplied example in the “Autolinks” and “Raw HTML” sections.
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
        "Autolinks|Raw HTML",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC autolinks-and-raw-html-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow the supplied CommonMark 0.31.2 specification.
- Preserve raw HTML as specified; do not escape valid raw HTML constructs.
- Do not use a public Markdown implementation as the parser.
- Keep supplied conformance assets under `sources/` unchanged.
