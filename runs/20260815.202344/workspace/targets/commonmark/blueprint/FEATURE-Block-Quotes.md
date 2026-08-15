# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parses nested CommonMark block quotes with lazy continuation and contained blocks. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leafs.md |
| Provides    | block quote parsing |
| Consumes    | executable commonmark, leaf block parsing |

## Purpose

Implement block quote containers and their interaction with leaf blocks.

## Scope

Support block quote markers with optional indentation, nested quotes, empty quotes, blank lines, separation of consecutive quotes, lazy paragraph continuation, and contained headings, paragraphs, code blocks, thematic breaks, HTML blocks, references, and lists.

Block quote parsing must preserve the distinction between marker-required lines and lazy continuation lines.

## Programmatic Acceptance

=== AC block-quotes-conformance ===
Intent: The implementation passes every supplied conformance example owned by block quotes.

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
        r"^Block quotes$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes-conformance ===

=== AC block-quotes-interface ===
Intent: A block quote document is accepted through the executable interface.

import subprocess

source = "> quoted text\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC block-quotes-interface ===

=== AC block-quotes-nested-input ===
Intent: Nested block quote input is accepted through the executable interface.

import subprocess

source = "> > nested\n> continuation\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC block-quotes-nested-input ===

## User Acceptance

- None.

## Guardrails

- Preserve lazy continuation semantics.
- Do not allow unmarked block constructs to become quoted unless the specification permits laziness.
- Do not modify supplied conformance assets.
