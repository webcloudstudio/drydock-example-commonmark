# FEATURE: Reference Definitions

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Collect link reference definitions for document-wide inline resolution. |
| Depends On | FEATURE-Paragraphs.md |
| Provides | document reference map |
| Consumes | paragraph block parsing |

## Purpose

Extract definitions from closing paragraphs and make the resulting map available after block parsing, before inline parsing begins.

## Behavior

At paragraph closure, parse consecutive valid reference definitions at the beginning of the accumulated paragraph text. A definition has a valid nonempty label, colon, destination and optional title as specified in CommonMark 0.31.2, including allowed line endings, escapes and indentation. A definition cannot interrupt a paragraph. Remove recognized definitions from visible paragraph content; preserve any remaining text.

Normalize labels by Unicode case folding, trimming leading and trailing spaces, tabs and line endings, and collapsing internal runs of those characters to one space. Match normalized source labels, not their parsed inline representation. Retain the first definition for each normalized label in document order. Definitions found within containers contribute to the same document-wide map.

Expose `extract_definitions(text, references)` from `commonmark_parser.references`. It processes the beginning of a closing paragraph, updates the supplied mutable map in place, and returns remaining paragraph text. Map values are `(destination, title)`, with `None` for an absent title. Destination and title values have CommonMark escapes and character references resolved.

## Programmatic Acceptance

=== AC references-first-definition ===
Intent: Definitions are removed from paragraph content, labels match case insensitively, and the first matching definition wins.

from commonmark_parser.references import extract_definitions

destination = "/first"
references = {}
remaining = extract_definitions("[Alpha]: " + destination + "\n[alpha]: /second\n", references)
assert remaining == ""
assert references["alpha"] == (destination, None)
=== END AC references-first-definition ===

=== AC references-remainder ===
Intent: A valid leading definition leaves subsequent paragraph text intact, while a malformed definition remains visible.

from commonmark_parser.references import extract_definitions

destination = "/target"
visible = "ordinary text\n"
references = {}
remaining = extract_definitions("[Label]: " + destination + "\n" + visible, references)
assert remaining == visible
assert references["label"] == (destination, None)
invalid = "[missing]:\n"
assert extract_definitions(invalid, {}) == invalid
=== END AC references-remainder ===

## User Acceptance

- None.

## Guardrails

- Collect definitions across the entire document before resolving inline references.
- Complete mixed-feature section checks belong to the later conformance integration story.
