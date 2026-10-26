# FEATURE: Code Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses indented and fenced code blocks as literal content. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | indented and fenced code block parsing |
| Consumes    | commonmark executable |

## Behavior

An indented code block contains one or more nonblank lines with at least four spaces of indentation, with four spaces removed from each content line. Blank lines may separate chunks within the block; trim blank lines at its boundaries. An indented code block cannot interrupt a paragraph. Preserve additional indentation and trailing spaces in its content. A tab can satisfy indentation according to four-column tab stops.

A fenced code block opens with at least three consecutive backticks or tildes after at most three spaces of indentation. The info string is optional; trim its boundary spaces and tabs. A backtick fence's info string cannot contain a backtick. Close only with a fence of the same character, at least as long as the opener, preceded by at most three spaces and followed only by spaces or tabs. Remove up to the opener's indentation from content lines. An unclosed fence extends to the end of its containing block or document. Fence contents are literal and are not parsed as inline Markdown.

Render the first word of a nonempty info string as the `language-` class on the code element, with HTML escaping as required by the examples.

## Programmatic Acceptance

=== AC code-blocks-conformance ===
Intent: The parser passes the complete supplied example slice for indented and fenced code blocks.
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
        "Indented code blocks|Fenced code blocks",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC code-blocks-conformance ===

## User Acceptance

- None.

## Guardrails

- Code block contents are literal and are not parsed as inline Markdown.
- Do not invoke `sources/full_test.sh` from this scoped check.
- Keep all supplied scoring assets unchanged.
