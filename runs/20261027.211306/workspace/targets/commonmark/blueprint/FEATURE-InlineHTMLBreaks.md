# FEATURE: Inline HTML and Hard Breaks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize raw inline HTML and hard line breaks. |
| Depends On | FEATURE-InlineText.md, FEATURE-CodeSpans.md |
| Provides | inline HTML and hard break parsing |
| Consumes | inline text parsing, code span parsing |

## Purpose and workflow

Recognize the specification's open and closing tags, comments, processing instructions, declarations, and CDATA sections as raw inline HTML. Preserve valid raw HTML verbatim, including attribute contents. Text that does not match the grammar remains ordinary text.

A line ending preceded by at least two spaces or an unescaped backslash forms a hard break within an inline block. Do not create hard breaks inside code spans or HTML tags, or at the end of a block.

For direct incremental acceptance, expose `parse_inline_html_breaks(source)` from `commonmark_parser.inline_html_breaks`. It returns inline nodes. Raw HTML nodes expose `type` and `literal`; hard breaks have type `hardbreak`; ordinary text nodes expose `type` and `literal`.

## Programmatic Acceptance

=== AC inline-html-raw ===
Intent: A valid inline tag is preserved as a raw HTML node with its original spelling.

from commonmark_parser.inline_html_breaks import parse_inline_html_breaks

tag = '<custom data-value="sample">'
nodes = parse_inline_html_breaks(tag)
assert len(nodes) == 1
assert nodes[0].type == "html"
assert nodes[0].literal == tag
=== END AC inline-html-raw ===

=== AC inline-hard-breaks ===
Intent: Both specified hard-break forms create a break between text, while a trailing backslash remains text.

from commonmark_parser.inline_html_breaks import parse_inline_html_breaks

for source in ("first  \nsecond", "first\\\nsecond"):
    nodes = parse_inline_html_breaks(source)
    assert sum(node.type == "hardbreak" for node in nodes) == 1
source = "ending\\"
nodes = parse_inline_html_breaks(source)
assert all(node.type != "hardbreak" for node in nodes)
assert "".join(node.literal for node in nodes if node.type == "text") == source
=== END AC inline-hard-breaks ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 and do not use a public Markdown implementation.
- Complete mixed-section conformance checks belong to the later integration story.
