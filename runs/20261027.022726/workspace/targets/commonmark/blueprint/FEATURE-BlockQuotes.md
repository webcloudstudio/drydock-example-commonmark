# FEATURE: Block Quotes

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse nested block quotes and their continuation lines. |
| Depends On | FEATURE-Headings.md, FEATURE-CodeBlocks.md, FEATURE-HtmlBlocks.md, FEATURE-ReferenceDefinitions.md |
| Provides | block quote containers |
| Consumes | paragraph and thematic break blocks, heading blocks, code blocks, HTML blocks, reference definition map |

## Purpose and behavior

A block quote marker is `>` preceded by at most three spaces and optionally followed by one space of indentation. Parse its contents as blocks, allowing nested quotes and all available leaf blocks. Match continuation markers through the open block tree before looking for new blocks. An omitted marker is permitted only on a paragraph continuation line; it cannot lazily continue a code block or introduce another block. Blank lines separate adjacent quotes unless included with quote markers. Quotes can interrupt paragraphs, and definitions inside them enter the document-wide reference map.

Expose `parse_block_quote(lines)` from `commonmark_parser.block_quotes`. It returns `None` if the first line does not start a quote; otherwise it returns `(consumed, content_lines)`, where `content_lines` are the source lines belonging to the quote after removing the outer marker and its optional following space. The block parser recursively parses those lines and preserves the distinction between marked and lazy continuation for block precedence.

Examples involving lists or later inline features are exercised after those capabilities are integrated.

## Programmatic Acceptance

=== AC quote-markers ===
Intent: Consecutive marked lines form one quote and retain their contents for recursive block parsing.

from commonmark_parser.block_quotes import parse_block_quote

content = ["alpha\n", "beta\n"]
lines = ["> " + line for line in content] + ["\n"]
consumed, observed = parse_block_quote(lines)
assert consumed == len(content)
assert observed == content
=== END AC quote-markers ===

=== AC quote-lazy-continuation ===
Intent: An unmarked paragraph continuation remains inside its quote while a blank line terminates it.

from commonmark_parser.block_quotes import parse_block_quote

first = "alpha\n"
continuation = "beta\n"
lines = ["> " + first, continuation, "\n", "outside\n"]
consumed, observed = parse_block_quote(lines)
assert consumed == 2
assert observed == [first, continuation]
=== END AC quote-lazy-continuation ===

## User Acceptance

- None.

## Guardrails

- Preserve the document-wide reference map across container boundaries.
- Do not modify the supplied specification or conformance assets.
