# FEATURE: List Items and Lists

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines CommonMark bullet and ordered list parsing, nesting, and tightness behavior. |
| Depends On  | FEATURE-BLOCK-LEAF.md, FEATURE-BLOCK-QUOTES.md |
| Provides    | list parser |
| Consumes    | leaf block parser, block quote parser |

## Workflow

The parser recognizes bullet markers and ordered markers with up to three leading spaces and one to four following spaces. It supports nested lists, continuation paragraphs, lazy continuation, empty items, indented content, mixed block contents, delimiter changes, ordered starts, and tight or loose list rendering metadata. Lists and items follow CommonMark 0.31.2 marker, indentation, interruption, and blank-line rules.

## Programmatic Acceptance

Requires: executable=python3; scope=test

=== AC lists-structure ===
Intent: The implementation passes list marker, nesting, indentation, and continuation conformance examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(List items|Lists)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists-structure ===

=== AC lists-tightness ===
Intent: The implementation passes empty-item, delimiter, and tight-versus-loose list conformance examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(List items|Lists)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists-tightness ===

## User Acceptance

- None.

## Guardrails

- The parser does not treat thematic breaks as list items when both interpretations are possible.
- List tightness is derived from blank-line structure and contained blocks, not from output text.
