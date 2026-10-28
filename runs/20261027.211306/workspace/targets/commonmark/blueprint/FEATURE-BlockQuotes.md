# FEATURE: Block Quotes

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse block quote containers and their continuation lines. |
| Depends On | FEATURE-Paragraphs.md, FEATURE-ThematicBreaks.md, FEATURE-ATXHeadings.md, FEATURE-SetextHeadings.md, FEATURE-IndentedCode.md, FEATURE-FencedCode.md, FEATURE-HTMLBlocks.md, FEATURE-ReferenceDefinitions.md |
| Provides | block quote parsing |
| Consumes | paragraph block parsing, thematic break parsing, ATX heading parsing, setext heading parsing, indented code block parsing, fenced code block parsing, HTML block parsing, document reference map |

## Purpose and workflow

During block parsing, recognize a block quote marker after at most three spaces of indentation. The marker is `>` with at most one following space of indentation consumed; handle tabs using the specification's four-column tab stops. Add a block quote container to the document tree and parse its contents as blocks.

Continue open quote containers when their markers are present. A missing marker is permitted only for paragraph continuation text under the specification's laziness rule. A blank line without a marker closes the quote; an explicitly marked blank line remains inside it. Nest quotes recursively and close unmatched containers before starting a new block. Definitions found inside a quote contribute to the document-wide reference map.

For direct verification, expose `parse_blocks(source)` from `commonmark_parser.blocks`. It returns a document node whose `children` are ordered block nodes. Nodes expose `type`, `children`, and, for paragraphs, `literal` containing their unparsed inline source. A quote node has type `block_quote`, and a paragraph node has type `paragraph`. This interface exposes the block tree before inline parsing.

The complete Block quotes corpus section includes interactions with lists and inline parsing. The conformance integration story executes that complete section after those providers exist.

## Programmatic Acceptance

=== AC block-quote-lazy ===
Intent: A marked paragraph and its unmarked continuation belong to the same quote and retain their source text.

from commonmark_parser.blocks import parse_blocks

first = "alpha"
second = "continuation"
document = parse_blocks("> " + first + "\n" + second + "\n")
assert len(document.children) == 1
quote = document.children[0]
assert quote.type == "block_quote"
assert len(quote.children) == 1
paragraph = quote.children[0]
assert paragraph.type == "paragraph"
assert paragraph.literal.splitlines() == [first, second]
=== END AC block-quote-lazy ===

=== AC block-quote-nesting ===
Intent: Nested quote markers produce nested containers, and an unmarked blank line ends the quote.

from commonmark_parser.blocks import parse_blocks

inside = "inside"
outside = "outside"
document = parse_blocks("> > " + inside + "\n\n" + outside + "\n")
assert len(document.children) == 2
outer, paragraph = document.children
assert outer.type == "block_quote"
assert len(outer.children) == 1
inner = outer.children[0]
assert inner.type == "block_quote"
assert inner.children[0].type == "paragraph"
assert inner.children[0].literal == inside
assert paragraph.type == "paragraph"
assert paragraph.literal == outside
=== END AC block-quote-nesting ===

## User Acceptance

- None.

## Guardrails

- Parse block structure before parsing inline content.
- Preserve the supplied conformance assets unchanged.
- Do not invoke the full-suite entry point in this story's checks.
