# FEATURE: Headings

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parses ATX and setext heading blocks and preserves their inline content. |
| Depends On | FEATURE-ParagraphsAndBreaks.md |
| Provides | heading blocks |
| Consumes | paragraph and thematic break blocks |

## Purpose

Recognize both CommonMark heading forms as block structure before parsing their contents as inlines.

## Behavior

An ATX heading begins after at most three spaces of indentation with one to six unescaped `#` characters followed by whitespace or end of line. Its level is the opening run length. Remove leading and trailing spaces or tabs and an eligible closing `#` run preceded by whitespace. ATX headings may interrupt paragraphs and may be empty.

A setext heading consists of paragraph-eligible lines followed by an underline of `=` or `-` characters, with at most three spaces of indentation and only trailing spaces or tabs. The underline determines level one or two. It converts the preceding paragraph content into a heading, takes precedence over a thematic break where both interpretations apply, and cannot be a lazy continuation in a container. Preserve the trimmed heading text for inline parsing.

The heading sections include inline and other block interactions unavailable at this stage. The later line-break integration exercises the complete sections once all parser capabilities exist.

## Programmatic Acceptance

=== AC atx-heading-block ===
Intent: Block parsing records an ATX heading's level and raw content for the inline phase.

from commonmark_parser import parse_blocks

content = "alpha"
document = parse_blocks("## " + content + "\n")
assert len(document.children) == 1
assert document.children[0].type == "heading"
assert document.children[0].level == 2
assert document.children[0].raw_content == content
=== END AC atx-heading-block ===

=== AC setext-heading-block ===
Intent: A setext underline converts the preceding paragraph into a heading.

from commonmark_parser import parse_blocks

content = "alpha"
document = parse_blocks(content + "\n---\n")
assert len(document.children) == 1
assert document.children[0].type == "heading"
assert document.children[0].level == 2
assert document.children[0].raw_content == content
=== END AC setext-heading-block ===

## User Acceptance

- None.

## Guardrails

- Parse heading contents as inlines only after block structure and reference definitions are complete.
- Do not modify the supplied conformance assets.
