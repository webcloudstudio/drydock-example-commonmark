# FEATURE: Escapes and Character References

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses backslash escapes and valid HTML character references in inline content. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | inline escapes and character reference parsing |
| Consumes    | commonmark executable |

## Purpose

Implement CommonMark inline backslash escapes and entity and numeric character references.

## Behavior

- Backslash-escape any ASCII punctuation character; preserve a backslash before other characters. A backslash before a line ending is a hard break, except at the end of a block.
- Decode valid HTML5 named entities, decimal references of one to seven digits, and hexadecimal references of one to six digits. Require a terminating semicolon.
- Replace invalid Unicode code points and U+0000 with U+FFFD. Escape decoded characters as required for safe HTML rendering.
- Do not interpret escapes or references inside code spans or code blocks. Entity references cannot supply characters used as block-structure markers.

## Programmatic Acceptance

=== AC escapes-and-character-references ===
Intent: The implementation passes all supplied backslash escape and character reference conformance examples.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern",
     "Backslash escapes|Entity and numeric character references"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC escapes-and-character-references ===

## User Acceptance

- None.

## Guardrails

- Keep block parsing ahead of inline parsing.
- Do not modify supplied scoring assets or invoke `sources/full_test.sh` from this scoped check.
