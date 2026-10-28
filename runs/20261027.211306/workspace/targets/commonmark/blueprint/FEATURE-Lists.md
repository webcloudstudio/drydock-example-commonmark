# FEATURE: Lists

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse list containers and their items. |
| Depends On | FEATURE-BlockQuotes.md |
| Provides | list block parsing |
| Consumes | block quote parsing, paragraph block parsing, thematic break parsing, ATX heading parsing, setext heading parsing, indented code block parsing, fenced code block parsing, HTML block parsing, document reference map |

## Purpose and workflow

Recognize bullet markers `-`, `+`, and `*`, and ordered markers of one to nine digits followed by `.` or `)`. Apply the specification's indentation rules, including marker width, one to four columns of following indentation, items starting with blank lines or indented code, tab stops, and lazy paragraph continuations. A thematic break takes precedence over a list item. An item interrupting a paragraph must be nonempty and an ordered list must start at one.

Group adjacent items only when their marker types match, including the bullet character or ordered delimiter. Preserve an ordered list's first start number. Parse nested block content and collect reference definitions document-wide. A list is loose when its items are separated by blank lines or an item directly contains blocks separated by a blank line; otherwise it is tight. The renderer uses that property to determine paragraph wrappers.

Extend `commonmark_parser.blocks.parse_blocks(source)` to return list and item nodes in the block tree. A list node exposes `type` equal to `list`, ordered `children` of type `item`, `ordered` as a boolean, `start` as the ordered start number, and `tight` as a boolean. Paragraph children retain their unparsed `literal`.

The complete List items and Lists corpus sections are executed by conformance integration after inline providers exist.

## Programmatic Acceptance

=== AC list-items ===
Intent: Matching markers form one tight list with separate items whose paragraph text is preserved.

from commonmark_parser.blocks import parse_blocks

first = "alpha"
second = "beta"
document = parse_blocks("- " + first + "\n- " + second + "\n")
assert len(document.children) == 1
listing = document.children[0]
assert listing.type == "list"
assert listing.ordered is False
assert listing.tight is True
assert len(listing.children) == 2
assert all(item.type == "item" for item in listing.children)
assert [item.children[0].literal for item in listing.children] == [first, second]
=== END AC list-items ===

=== AC list-start-and-looseness ===
Intent: An ordered list retains its initial number and blank lines between items make it loose.

from commonmark_parser.blocks import parse_blocks

start = 4
first = "first"
second = "second"
document = parse_blocks(f"{start}. {first}\n\n5. {second}\n")
assert len(document.children) == 1
listing = document.children[0]
assert listing.type == "list"
assert listing.ordered is True
assert listing.start == start
assert listing.tight is False
assert [item.children[0].literal for item in listing.children] == [first, second]
=== END AC list-start-and-looseness ===

## User Acceptance

- None.

## Guardrails

- Parse blocks before inline content and preserve document-wide references.
- Preserve the supplied conformance assets unchanged.
- Do not invoke the full-suite entry point in this story's checks.
