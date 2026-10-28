# FEATURE: Paragraphs and Blank Lines

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Forms paragraph blocks and separates them with blank lines. |
| Depends On | FEATURE-Executable.md |
| Provides | paragraph block parsing |
| Consumes | commonmark |

## Behavior

`commonmark_parser.blocks.parse_blocks` returns a document whose paragraph nodes retain raw inline content in `literal`. A sequence of nonblank lines that does not start another block forms a paragraph. Remove initial and final spaces or tabs from the paragraph's raw content; remove leading indentation on continuation lines while preserving line endings and meaningful trailing spaces within the paragraph for later inline parsing. An indented continuation cannot start an indented code block in the middle of a paragraph.

Blank lines separate paragraphs and are ignored at document boundaries. Retain their role for later list tightness processing. The complete Paragraphs and Blank lines conformance sections run in the later conformance integration story once their interacting providers exist.

## Programmatic Acceptance

=== AC paragraph-blocks ===
Intent: Consecutive lines form one paragraph and a blank line separates the next paragraph while raw content remains available.

from commonmark_parser.blocks import parse_blocks

first = "alpha"
second = "beta"
third = "gamma"
document = parse_blocks(first + "\n" + second + "\n\n" + third + "\n")
assert len(document.children) == 2
assert all(node.kind == "paragraph" for node in document.children)
assert document.children[0].literal.splitlines() == [first, second]
assert document.children[1].literal.strip() == third
=== END AC paragraph-blocks ===

=== AC paragraph-whitespace ===
Intent: Paragraph boundaries discard surrounding blank lines and retain the text of an indented continuation.

from commonmark_parser.blocks import parse_blocks

first = "alpha"
second = "beta"
document = parse_blocks("\n  " + first + "\n    " + second + "\n\n")
assert len(document.children) == 1
assert document.children[0].kind == "paragraph"
assert document.children[0].literal.splitlines() == [first, second]
=== END AC paragraph-whitespace ===

## User Acceptance

- None.

## Guardrails

- Preserve raw inline content for the subsequent inline phase.
- Do not run the full-suite entry point in this story.
