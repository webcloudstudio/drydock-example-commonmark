# FEATURE: HTML Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses the seven kinds of CommonMark HTML blocks. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | HTML block parsing |
| Consumes    | commonmark executable |

## Purpose

Preserve raw HTML blocks in rendered output according to the seven start and end conditions in CommonMark 0.31.2.

## Behavior

- Recognize type 1 blocks beginning with `pre`, `script`, `style`, or `textarea`; types 2–5 beginning with comments, processing instructions, declarations, or CDATA; type 6 beginning with a listed block tag; and type 7 containing a complete open or closing tag on a line by itself.
- Apply each type’s end condition, including blank-line termination for types 6 and 7 and matching end markers for types 1–5. An unterminated block ends with its containing block or document.
- Allow up to three leading spaces. Types 1–6 may interrupt paragraphs; type 7 may not. Pass block contents through as raw HTML.

## Programmatic Acceptance

=== AC html-blocks ===
Intent: The implementation passes all supplied HTML block conformance examples.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "HTML blocks"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC html-blocks ===

## User Acceptance

- None.

## Guardrails

- Do not escape or otherwise rewrite raw HTML block contents.
- Do not modify supplied scoring assets.
- Do not invoke `sources/full_test.sh` from this scoped check.
