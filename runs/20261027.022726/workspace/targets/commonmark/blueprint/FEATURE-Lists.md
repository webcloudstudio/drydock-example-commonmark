# FEATURE: Lists

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse CommonMark list items and list containers. |
| Depends On | FEATURE-BlockQuotes.md, FEATURE-ReferenceDefinitions.md, FEATURE-Headings.md, FEATURE-CodeBlocks.md, FEATURE-HtmlBlocks.md |
| Provides | list containers |
| Consumes | block quote containers, reference definition map, heading blocks, code blocks, HTML blocks |

## Purpose and behavior

Recognize bullet markers `-`, `+`, and `*`, and ordered markers of one to nine digits followed by `.` or `)`. A list groups consecutive items with the same bullet character or ordered delimiter. Its start number is that of its first ordered item.

Determine item content indentation from the marker width and following indentation, using the specification's special rules for an initial blank line and indented code. Match continuation indentation and allow lazy continuation only for paragraph continuation text. Parse nested blocks recursively, including quotes, lists, headings, code, HTML, and reference definitions. A thematic break takes precedence over a list marker. An empty item cannot interrupt a paragraph, and only an ordered item starting at one can interrupt one.

A list is loose when its items are separated by blank lines or an item directly contains blocks separated by a blank line; otherwise it is tight. Render paragraphs in loose items with paragraph tags and omit those tags for direct paragraphs in tight items.

Expose `parse_list_marker(line, paragraph_open=False)` from `commonmark_parser.lists`. It returns `None` for a line that cannot start an item; otherwise it returns a mapping with `kind`, `marker`, `start`, and `content_indent`. For bullets, `start` is `None`; for ordered markers it is the integer start value. `content_indent` is the number of indentation columns consumed before item content.

The complete List items and Lists sections and their inline interactions are exercised after all inline capabilities are integrated.

## Programmatic Acceptance

=== AC list-marker ===
Intent: An ordered marker reports its start value and the indentation needed for its content.

from commonmark_parser.lists import parse_list_marker

number = 7
marker = f"{number}."
prefix = marker + "  "
result = parse_list_marker(prefix + "item\n")
assert result is not None
assert result["kind"] == "ordered"
assert result["marker"] == marker
assert result["start"] == number
assert result["content_indent"] == len(prefix)
=== END AC list-marker ===

=== AC list-paragraph-interruption ===
Intent: Only an ordered marker starting at one may interrupt a paragraph.

from commonmark_parser.lists import parse_list_marker

assert parse_list_marker("1. item\n", paragraph_open=True) is not None
assert parse_list_marker("2. item\n", paragraph_open=True) is None
assert parse_list_marker("-\n", paragraph_open=True) is None
=== END AC list-paragraph-interruption ===

## User Acceptance

- None.

## Guardrails

- Follow the specification's block-tree continuation and precedence rules.
- Do not modify the supplied specification or conformance assets.
