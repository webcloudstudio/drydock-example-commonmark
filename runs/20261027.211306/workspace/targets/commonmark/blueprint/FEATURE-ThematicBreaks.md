# FEATURE: Thematic Breaks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognizes thematic break blocks and their precedence. |
| Depends On | FEATURE-Paragraphs.md |
| Provides | thematic break parsing |
| Consumes | paragraph block parsing |

## Behavior

Extend `commonmark_parser.blocks.parse_blocks` to produce nodes whose `kind` is `thematic_break`. A thematic break has up to three spaces of indentation and at least three matching `-`, `_`, or `*` markers, with only spaces or tabs between and after them. Different marker characters or other content make the line ineligible.

A thematic break may interrupt a paragraph. A valid setext underline takes precedence when it follows eligible paragraph content; a thematic break takes precedence over a list item interpretation. The setext and list stories complete those interactions. The complete Thematic breaks section runs in the later conformance integration story.

## Programmatic Acceptance

=== AC thematic-break-recognition ===
Intent: Matching marker runs form thematic breaks and interrupt an existing paragraph.

from commonmark_parser.blocks import parse_blocks

text = "alpha"
document = parse_blocks(text + "\n* * *\n")
assert len(document.children) == 2
assert document.children[0].kind == "paragraph"
assert document.children[0].literal.strip() == text
assert document.children[1].kind == "thematic_break"
=== END AC thematic-break-recognition ===

=== AC thematic-break-invalid ===
Intent: A line with mixed markers remains paragraph content instead of forming a thematic break.

from commonmark_parser.blocks import parse_blocks

source = "*-_"
document = parse_blocks(source + "\n")
assert len(document.children) == 1
assert document.children[0].kind == "paragraph"
assert document.children[0].literal.strip() == source
=== END AC thematic-break-invalid ===

## User Acceptance

- None.

## Guardrails

- Do not run the full-suite entry point in this story.
