# FEATURE: Block Lists

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parses CommonMark lists, list items, nesting, continuation, and tightness. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leafs.md, FEATURE-Block-Quotes.md |
| Provides    | list parsing, list-item parsing, list tightness |
| Consumes    | executable commonmark, leaf block parsing, block quote parsing |

## Purpose

Implement bullet and ordered list containers and their list-item block content.

## Scope

Support bullet markers, ordered markers and start numbers, marker widths, indentation, nested lists, list interruption, lazy continuation, empty items, mixed block content, delimiter changes, blank-line handling, and tight versus loose rendering.

List-item parsing must compose with block quotes and all leaf blocks while preserving the list's marker type and tightness rules.

## Programmatic Acceptance

=== AC lists-conformance ===
Intent: The implementation passes every supplied conformance example owned by list items and lists.

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
        r"^(List items|Lists)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists-conformance ===

=== AC lists-interface ===
Intent: A bullet list is accepted through the executable interface.

import subprocess

source = "- one\n- two\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC lists-interface ===

=== AC lists-nested-input ===
Intent: Nested and ordered list input is accepted through the executable interface.

import subprocess

source = "1. one\n   - nested\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC lists-nested-input ===

## User Acceptance

- None.

## Guardrails

- Preserve list marker type, ordered start number, nesting, and tightness semantics.
- Do not treat thematic breaks as list items when CommonMark gives the thematic break precedence.
- Do not modify supplied conformance assets.
