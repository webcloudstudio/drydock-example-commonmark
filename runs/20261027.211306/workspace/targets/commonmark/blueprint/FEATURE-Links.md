# FEATURE: Links

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse inline and reference links using the completed document reference map. |
| Depends On | FEATURE-Emphasis.md, FEATURE-ReferenceDefinitions.md |
| Provides | link parsing |
| Consumes | document reference map, inline text parsing, code span parsing, emphasis parsing |

## Purpose and workflow

During the inline phase, recognize inline links and full, collapsed, and shortcut reference links. Resolve references against the completed document-wide map, using Unicode case folding and whitespace normalization for labels. The first matching definition wins.

Parse destinations and optional titles according to the specification, including balanced parentheses, angle-delimited destinations, escapes, character references, and the permitted whitespace. Apply the delimiter-stack link procedure: find the nearest active bracket opener, process emphasis within the link text, and deactivate earlier link openers after forming a link. Links cannot contain links. Code spans and other higher-precedence constructs retain their specified precedence.

For direct incremental acceptance, expose `parse_links(source, references)` from `commonmark_parser.links`. It returns a sequence of inline nodes. A link node exposes `type`, `destination`, `title`, and `children`; text nodes expose `type` and `literal`. The reference mapping uses normalized labels and values containing `destination` and `title`. This interface accepts already collected references and does not require later inline providers.

## Programmatic Acceptance

=== AC links-inline ===
Intent: Inline link parsing returns the supplied destination and title and retains the link text as children.

from commonmark_parser.links import parse_links

label = "label"
destination = "/destination"
title = "caption"
source = f'[{label}]({destination} "{title}")'
nodes = parse_links(source, {})
assert len(nodes) == 1
link = nodes[0]
assert link.type == "link"
assert link.destination == destination
assert link.title == title
assert len(link.children) == 1
assert link.children[0].type == "text"
assert link.children[0].literal == label
=== END AC links-inline ===

=== AC links-reference ===
Intent: Full, collapsed, and shortcut references resolve through the supplied normalized reference map.

from commonmark_parser.links import parse_links

label = "reference"
destination = "/target"
references = {label: {"destination": destination, "title": None}}
for source in (f"[visible][{label.upper()}]", f"[{label}][]", f"[{label}]"):
    nodes = parse_links(source, references)
    assert len(nodes) == 1
    assert nodes[0].type == "link"
    assert nodes[0].destination == destination
    assert nodes[0].title is None
=== END AC links-reference ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 and do not use a public Markdown implementation.
- Complete mixed-section conformance checks belong to the later integration story.
