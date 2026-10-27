# FEATURE: Paragraphs and Thematic Breaks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parses paragraph, blank-line, and thematic-break block structure. |
| Depends On | ARCHITECTURE.md, FEATURE-CommandLine.md |
| Provides | paragraph and thematic break blocks |
| Consumes | parser foundation, commonmark |

## Purpose

Build paragraph and thematic-break nodes while preserving paragraph content for the later inline phase. Blank lines separate paragraphs and otherwise have no rendered block of their own.

## Behavior

Normalize line endings for parsing and replace U+0000 with U+FFFD. Treat tabs as advancing to four-column tab stops where indentation defines block structure, while retaining literal tabs in content where required.

Accumulate consecutive nonblank lines that do not start another applicable block as a paragraph. Strip initial and final spaces or tabs from its raw content and remove leading indentation on continuation lines according to the specification. Preserve internal line endings and content for inline parsing.

Recognize a thematic break after at most three spaces of indentation when a line contains at least three matching `*`, `-`, or `_` characters and otherwise only spaces or tabs. It may interrupt a paragraph. A setext underline takes precedence when that later heading capability applies; a thematic break takes precedence over a possible list item.

The complete corpus includes interactions with headings, containers, code, and inline constructs. The later line-break integration checks those interactions after their providers exist.

## Programmatic Acceptance

=== AC paragraph-block-tree ===
Intent: Block parsing preserves plain paragraph content and separates paragraphs at a blank line.

from commonmark_parser import parse_blocks

first = "alpha"
second = "beta"
document = parse_blocks(first + "\n\n" + second + "\n")
assert len(document.children) == 2
assert document.children[0].type == "paragraph"
assert document.children[0].raw_content == first
assert document.children[1].type == "paragraph"
assert document.children[1].raw_content == second
=== END AC paragraph-block-tree ===

=== AC thematic-break-block-tree ===
Intent: A valid thematic break interrupts an open paragraph and becomes its own block.

from commonmark_parser import parse_blocks

source = "alpha\n* * *\n"
document = parse_blocks(source)
assert len(document.children) == 2
assert document.children[0].type == "paragraph"
assert document.children[1].type == "thematic_break"
=== END AC thematic-break-block-tree ===

## User Acceptance

- None.

## Guardrails

- Preserve raw inline content until the inline phase.
- Do not modify the supplied conformance assets.
