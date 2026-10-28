# FEATURE: Autolinks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize URI and email autolinks in inline content. |
| Depends On | FEATURE-InlineText.md, FEATURE-CodeSpans.md |
| Provides | autolink parsing |
| Consumes | inline text parsing, code span parsing |

## Purpose and workflow

Recognize angle-delimited absolute URI autolinks with a scheme of two to 32 permitted ASCII characters and no forbidden URI characters. Recognize email autolinks using the specification's email grammar. The visible label is the enclosed text; an email destination adds the `mailto:` scheme. Backslash escapes do not operate inside an autolink. Encode destinations and escape HTML when rendering, and respect code-span precedence.

For direct incremental acceptance, expose `parse_autolinks(source)` from `commonmark_parser.autolinks`. It returns inline nodes. An autolink node exposes `type`, `destination`, and `label`; ordinary text nodes expose `type` and `literal`.

## Programmatic Acceptance

=== AC autolinks-uri ===
Intent: A valid angle-delimited URI becomes a link with the supplied URI as destination and label.

from commonmark_parser.autolinks import parse_autolinks

uri = "https://example.test/path"
nodes = parse_autolinks(f"<{uri}>")
assert len(nodes) == 1
assert nodes[0].type == "link"
assert nodes[0].destination == uri
assert nodes[0].label == uri
=== END AC autolinks-uri ===

=== AC autolinks-email-and-invalid ===
Intent: An email autolink receives the mail scheme, while an angle-delimited URI containing a space remains text.

from commonmark_parser.autolinks import parse_autolinks

address = "person@example.test"
nodes = parse_autolinks(f"<{address}>")
assert len(nodes) == 1
assert nodes[0].type == "link"
assert nodes[0].destination == "mailto:" + address
assert nodes[0].label == address
source = "<https://example.test/a b>"
nodes = parse_autolinks(source)
assert all(node.type == "text" for node in nodes)
assert "".join(node.literal for node in nodes) == source
=== END AC autolinks-email-and-invalid ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 and do not use a public Markdown implementation.
- Complete mixed-section conformance checks belong to the later integration story.
