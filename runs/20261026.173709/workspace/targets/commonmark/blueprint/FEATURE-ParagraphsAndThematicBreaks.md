# FEATURE: Paragraphs and Thematic Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses paragraphs, blank lines, tabs, and thematic breaks. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | paragraph and thematic break parsing |
| Consumes    | commonmark executable |

## Behavior

A paragraph is a sequence of nonblank lines that cannot be interpreted as another block type. Its raw content joins those lines with line endings; remove leading indentation on the first line and trailing spaces or tabs at the block boundary. Preserve line boundaries for inline parsing. Blank lines separate blocks and are ignored at document boundaries.

A thematic break has up to three spaces of indentation and at least three matching `-`, `_`, or `*` markers, optionally separated and followed by spaces or tabs. No other characters may occur. Recognize thematic breaks without requiring surrounding blank lines, including when they interrupt a paragraph. A setext underline takes precedence when a line of dashes could be either a thematic break or an underline. A thematic break takes precedence over a list item when both interpretations are possible.

Tabs remain literal in text. Where indentation defines block structure, treat tabs as advancing to four-column tab stops. Preserve internal tabs in code content for the code block parser.

## Programmatic Acceptance

=== AC paragraphs-and-thematic-breaks ===
Intent: The parser passes the complete supplied example slice for paragraphs and thematic breaks.
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
        "Paragraphs|Thematic breaks|Tabs|Blank lines",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC paragraphs-and-thematic-breaks ===

## User Acceptance

- None.

## Guardrails

- Resolve block structure before inline structure.
- Do not invoke `sources/full_test.sh` from this scoped check.
- Keep all supplied scoring assets unchanged.
