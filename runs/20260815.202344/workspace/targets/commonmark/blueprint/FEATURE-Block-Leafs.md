# FEATURE: Block Leafs

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parses CommonMark leaf blocks and collects link reference definitions. |
| Depends On  | ARCHITECTURE.md |
| Provides    | leaf block parsing, link reference definitions |
| Consumes    | executable commonmark |

## Purpose

Implement the leaf-block portion of CommonMark block parsing before inline rendering.

## Scope

The parser handles:

- thematic breaks;
- ATX and setext headings;
- indented and fenced code blocks;
- HTML blocks;
- paragraphs and blank lines;
- link reference definitions, including normalization and first-definition precedence.

Leaf blocks must preserve raw inline content for later parsing. Code and raw HTML content must remain literal where required by the specification.

## Programmatic Acceptance

=== AC block-leafs-conformance ===
Intent: The implementation passes every supplied conformance example owned by leaf-block parsing.

import subprocess
import sys

pattern = (
    r"^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|"
    r"Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|Blank lines)$"
)
result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        "./commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        pattern,
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-leafs-conformance ===

=== AC block-leafs-interface ===
Intent: Leaf parsing remains reachable through the required executable interface.

import subprocess

source = "# heading\n\n    code\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC block-leafs-interface ===

=== AC block-leafs-reference-input ===
Intent: Link-reference-definition input is accepted through the executable interface.

import subprocess

source = "[label]: /destination\n\n[label]\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC block-leafs-reference-input ===

## User Acceptance

- None.

## Guardrails

- Build block structure before inline parsing.
- Do not modify `sources/spec.txt`, `sources/spec_tests.py`, `sources/cmark.py`, or `sources/normalize.py`.
- Do not interpret code blocks or HTML blocks as ordinary inline content.
