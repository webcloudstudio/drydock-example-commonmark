# FEATURE: ATX Headings

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognizes ATX heading blocks and retains their inline source. |
| Depends On | FEATURE-Paragraphs.md |
| Provides | ATX heading parsing |
| Consumes | paragraph block parsing |

## Behavior

Extend `commonmark_parser.blocks.parse_blocks` to produce `heading` nodes with a numeric `level` and raw inline content in `literal`. An opening run contains one through six unescaped `#` characters, preceded by at most three spaces and followed by whitespace or the end of the line. The level is the opening run's length. Remove leading and trailing spaces or tabs from the content. An optional closing run of unescaped `#` characters is removed only when preceded by whitespace and followed solely by whitespace or the end of the line. Headings may be empty and may interrupt paragraphs.

Retain heading content for the subsequent inline phase. The complete ATX headings section runs in the later conformance integration story after interacting providers exist.

## Programmatic Acceptance

=== AC atx-heading-level ===
Intent: A valid opening run produces the corresponding heading level and retains its content for inline parsing.

from commonmark_parser.blocks import parse_blocks

content = "alpha"
document = parse_blocks("### " + content + " ###\n")
assert len(document.children) == 1
assert document.children[0].kind == "heading"
assert document.children[0].level == 3
assert document.children[0].literal == content
=== END AC atx-heading-level ===

=== AC atx-heading-interruption ===
Intent: An ATX heading interrupts a paragraph and a marker without required separating whitespace stays in paragraph content.

from commonmark_parser.blocks import parse_blocks

first = "alpha"
heading = "beta"
invalid = "#gamma"
document = parse_blocks(first + "\n# " + heading + "\n" + invalid + "\n")
assert len(document.children) == 3
assert document.children[0].kind == "paragraph"
assert document.children[0].literal.strip() == first
assert document.children[1].kind == "heading"
assert document.children[1].level == 1
assert document.children[1].literal == heading
assert document.children[2].kind == "paragraph"
assert document.children[2].literal.strip() == invalid
=== END AC atx-heading-interruption ===

## User Acceptance

- None.

## Guardrails

- Preserve heading content for inline parsing.
- Do not run the full-suite entry point in this story.
