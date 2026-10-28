# FEATURE: Images

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse inline and reference images and derive plain-text descriptions. |
| Depends On | FEATURE-Links.md |
| Provides | image parsing |
| Consumes | link parsing |

## Purpose and workflow

Recognize inline, full, collapsed, and shortcut reference images using the link destination, title, and reference rules. Image descriptions may contain links and nested images. Render the description's plain textual content as the HTML `alt` attribute, without inline formatting tags; escape attribute values as required.

For direct incremental acceptance, expose `parse_images(source, references)` from `commonmark_parser.images`. It returns inline nodes. An image node exposes `type`, `destination`, `title`, and `alt`, where `alt` is the plain text of its parsed description. Reference mappings use normalized labels and values containing `destination` and `title`.

## Programmatic Acceptance

=== AC images-inline ===
Intent: An inline image retains its destination and title and extracts the plain text of its description.

from commonmark_parser.images import parse_images

label = "picture"
destination = "/image"
title = "caption"
nodes = parse_images(f'![{label}]({destination} "{title}")', {})
assert len(nodes) == 1
image = nodes[0]
assert image.type == "image"
assert image.destination == destination
assert image.title == title
assert image.alt == label
=== END AC images-inline ===

=== AC images-reference ===
Intent: Reference images resolve the supplied definition and omit emphasis markup from alt text.

from commonmark_parser.images import parse_images

label = "picture"
destination = "/image"
references = {label: {"destination": destination, "title": None}}
nodes = parse_images(f"![*{label}*][{label}]", references)
assert len(nodes) == 1
assert nodes[0].type == "image"
assert nodes[0].destination == destination
assert nodes[0].title is None
assert nodes[0].alt == label
=== END AC images-reference ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 and do not use a public Markdown implementation.
- Complete mixed-section conformance checks belong to the later integration story.
