# FEATURE: Setext Headings

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize setext headings in the block parsing phase. |
| Depends On | FEATURE-Paragraphs.md, FEATURE-ThematicBreaks.md |
| Provides | setext heading parsing |
| Consumes | paragraph block parsing, thematic break parsing |

## Purpose

Recognize a setext underline following eligible paragraph content and retain the heading's raw text for the later inline phase.

## Behavior

A nonempty paragraph may become a heading when its following line consists of one or more `=` or `-` characters, preceded by at most three spaces and followed only by spaces or tabs. The level is 1 for `=` and 2 for `-`. The paragraph may span multiple lines. Strip initial and final spaces and tabs from its raw content; do not interpret that content as inlines during block parsing.

An eligible underline takes precedence over a thematic break. An underline cannot turn a non-paragraph block or an empty paragraph into a heading. It cannot be a lazy continuation line of a containing block quote or list item. Four columns of indentation or internal whitespace disqualify an underline.

Expose `parse_setext(lines)` from `commonmark_parser.setext`. It accepts a sequence of raw paragraph lines followed by a candidate underline and returns `(level, raw_content)` for a valid heading or `None` otherwise. Container parsing is responsible for withholding lazy continuation lines from this interface.

## Programmatic Acceptance

=== AC setext-valid ===
Intent: Valid underlines convert nonempty multiline paragraph content into the corresponding heading while retaining its raw text.

from commonmark_parser.setext import parse_setext

first = "alpha"
second = "beta"
assert parse_setext([first, second, "==="]) == (1, first + "\n" + second)
assert parse_setext([first, "---"]) == (2, first)
=== END AC setext-valid ===

=== AC setext-invalid ===
Intent: An empty heading, excessive indentation, and internal underline whitespace do not form setext headings.

from commonmark_parser.setext import parse_setext

assert parse_setext(["", "==="]) is None
assert parse_setext(["alpha", "    ---"]) is None
assert parse_setext(["alpha", "= ="]) is None
=== END AC setext-invalid ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 and preserve block precedence over inline parsing.
- Complete mixed-feature section checks belong to the later conformance integration story.
