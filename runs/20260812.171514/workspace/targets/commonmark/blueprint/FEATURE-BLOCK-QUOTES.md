# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines nested CommonMark block quote parsing and lazy continuation behavior. |
| Depends On  | FEATURE-BLOCK-LEAF.md |
| Provides    | block quote parser |
| Consumes    | leaf block parser |

## Workflow

The parser recognizes block quote markers with up to three leading spaces, optionally followed by a space. It supports empty quotes, nested quotes, quoted headings, paragraphs, lists, code blocks, blank lines, and lazy continuation lines. Block quote boundaries follow CommonMark 0.31.2 consecutiveness and interruption rules.

## Programmatic Acceptance

Requires: executable=python3; scope=test

=== AC block-quotes-basic ===
Intent: The implementation passes basic and nested block quote conformance examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Block quotes)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes-basic ===

=== AC block-quotes-continuation ===
Intent: The implementation passes block quote laziness, blank-line, and contained-structure examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Block quotes)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes-continuation ===

## User Acceptance

- None.

## Guardrails

- The parser performs block parsing before inline parsing.
- The implementation does not use a public Markdown implementation.
