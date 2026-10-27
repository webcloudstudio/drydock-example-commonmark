# FEATURE: Reference Definitions

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Collect document-wide link reference definitions during block parsing. |
| Depends On | FEATURE-ParagraphsAndBreaks.md |
| Provides | reference definition map |
| Consumes | paragraph and thematic break blocks |

## Purpose and behavior

When a paragraph closes, parse consecutive definitions at its beginning and retain any remaining paragraph text. Definitions do not interrupt an existing paragraph. Apply the specification's label, destination, title, whitespace, indentation, and line-ending grammar. A definition can occur in a container and affects the entire document.

Normalize labels by Unicode case folding, trimming spaces, tabs, and line endings, and collapsing internal runs of those characters to one space. Preserve the first definition for each normalized label. Destinations and titles use the specified escape and character-reference rules.

Expose `collect_definitions(text, definitions)` from `commonmark_parser.references`. It updates the supplied document-wide dictionary in place and returns the unconsumed paragraph text. Dictionary values are `(destination, title)` pairs, with `None` for an omitted title. The caller invokes it when closing a paragraph in document order.

The later link and image stories exercise the reference-definition examples through the executable, including definitions inside containers and definitions appearing after uses.

## Programmatic Acceptance

=== AC reference-first-definition ===
Intent: Matching labels share one document-wide entry and the earliest definition wins.

from commonmark_parser.references import collect_definitions

first = "/first"
second = "/second"
definitions = {}
collect_definitions("[Foo Bar]: " + first + "\n", definitions)
collect_definitions("[foo  bar]: " + second + "\n", definitions)
assert len(definitions) == 1
assert next(iter(definitions.values())) == (first, None)
=== END AC reference-first-definition ===

=== AC reference-remainder ===
Intent: Closing a paragraph removes its initial definition while retaining subsequent paragraph content.

from commonmark_parser.references import collect_definitions

destination = "/target"
remainder = "ordinary content\n"
definitions = {}
observed = collect_definitions("[label]: " + destination + "\n" + remainder, definitions)
assert observed == remainder
assert len(definitions) == 1
assert next(iter(definitions.values())) == (destination, None)
=== END AC reference-remainder ===

## User Acceptance

- None.

## Guardrails

- Definitions are document-wide and the first matching definition takes precedence.
- Do not modify the supplied specification or conformance assets.
