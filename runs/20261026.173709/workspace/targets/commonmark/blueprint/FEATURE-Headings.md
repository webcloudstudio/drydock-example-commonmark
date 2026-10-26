# FEATURE: Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses ATX and setext headings with their specified boundaries. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | ATX and setext heading parsing |
| Consumes    | commonmark executable |

## Behavior

An ATX heading begins with one to six unescaped `#` characters after at most three spaces. The opening run must be followed by a space, tab, or end of line. Strip leading and trailing spaces and tabs from its content before inline parsing. An optional closing run of unescaped `#` characters counts only when preceded by spaces or tabs and followed only by spaces or tabs. Empty ATX headings are valid; seven or more opening markers are not headings.

A setext heading consists of one or more paragraph-eligible lines followed by an underline of `=` or `-`, with no more than three leading spaces and optional trailing spaces or tabs. The underline determines level 1 or 2. Join the content lines with line endings and trim boundary spaces and tabs before inline parsing. Setext headings cannot be empty, interrupt a paragraph, or use content lines that begin another block construct. A setext underline takes precedence over interpreting the same dash line as a thematic break.

## Programmatic Acceptance

=== AC headings-conformance ===
Intent: The parser passes the complete supplied example slice for ATX and setext headings.
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
        "ATX headings|Setext headings",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC headings-conformance ===

## User Acceptance

- None.

## Guardrails

- Resolve block structure before inline structure.
- Do not invoke `sources/full_test.sh` from this scoped check.
- Keep all supplied scoring assets unchanged.
