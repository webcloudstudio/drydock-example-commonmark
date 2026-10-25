# FEATURE: Block Parsing

| Field       | Value |
|-------------|-------|
| Version     | 20261025 V1 |
| Description | Parses CommonMark block structure and collects document-wide link reference definitions. |
| Depends On  | ARCHITECTURE.md |
| Provides    | block parser, document reference map |

## Purpose

Given Markdown lines, identify blocks before inline parsing. Collect valid link reference definitions during block parsing so links can resolve anywhere in the document, including definitions inside containers.

## Behavior

Implement the block constructs defined by the CommonMark 0.31.2 specification: thematic breaks; ATX and setext headings; indented and fenced code blocks; HTML blocks; paragraphs and blank lines; block quotes, including lazy continuation; and lists, including nesting, continuation, empty items, and tight or loose rendering.

Block structure takes precedence over inline syntax. Parse and render the complete behavior in the assigned source sections, preserving literal code-block contents and raw HTML behavior. Reference definitions are document-wide, first-definition-wins, and do not render as visible blocks.

## Programmatic Acceptance

=== AC block-parsing-conformance ===
Intent: All supplied cases in the block parsing sections pass (the complete block capability slice).
Suite: scoped
Probe: --dump-tests
Probe Count: json

import subprocess
import sys

sections = (
    "Thematic breaks|ATX headings|Setext headings|Indented code blocks|"
    "Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|"
    "Blank lines|Block quotes|List items|Lists"
)
command = [
    sys.executable, "sources/spec_tests.py",
    "--program", "./commonmark",
    "--spec", "sources/spec.txt",
    "--pattern", sections,
]
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-parsing-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not modify the supplied conformance assets.
- Implement the specified CommonMark 0.31.2 behavior without using a public Markdown implementation.
