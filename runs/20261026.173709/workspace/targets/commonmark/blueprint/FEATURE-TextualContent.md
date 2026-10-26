# FEATURE: Textual Content

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Renders unrecognized inline content as escaped text while preserving internal spaces. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | textual content rendering |
| Consumes     | commonmark executable |

## Purpose

Render inline characters that have no interpretation under CommonMark 0.31.2 as textual content.

## Behavior

- Escape text as required for safe HTML output while preserving its textual meaning.
- Preserve internal spaces verbatim.
- Leave Markdown constructs to their owning parser behavior; block structure takes precedence over inline structure.

## Programmatic Acceptance

=== AC inline-textual-content ===
Intent: The executable passes the complete supplied conformance slice for textual content.
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
        "Textual content",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-textual-content ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Preserve the supplied scoring assets unchanged.
- Resolve block structure before inline structure.
