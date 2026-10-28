# FEATURE: HTML Blocks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize and preserve the seven kinds of raw HTML block. |
| Depends On | FEATURE-Paragraphs.md |
| Provides | HTML block parsing |
| Consumes | paragraph block parsing |

## Purpose

Identify raw HTML blocks during block parsing and preserve their input without inline interpretation.

## Behavior

Recognize starts after at most three spaces of indentation using the seven CommonMark 0.31.2 categories: `pre`, `script`, `style`, or `textarea`; comments; processing instructions; declarations; CDATA; the specified block-level tag names; and complete standalone opening or closing tags. The first five categories end at their respective closing condition, including the entire closing line. The last two end before a blank line. All end at the containing block or document boundary if no earlier end applies. Category 7 cannot interrupt a paragraph; categories 1–6 can. Starts inside an already open HTML block do not change its end condition.

Expose `parse_html_block(lines, paragraph_open=False)` from `commonmark_parser.html_blocks`. It accepts lines without line endings and returns `(raw_content, consumed)` for a recognized block, or `None` when no block starts. Each consumed input line is represented in `raw_content` with a newline terminator. The caller supplies only lines within the current container.

## Programmatic Acceptance

=== AC html-block-termination ===
Intent: A comment block preserves its lines through the line containing its closing marker.

from commonmark_parser.html_blocks import parse_html_block

lines = ["<!-- alpha", "", "beta -->", "outside"]
raw, consumed = parse_html_block(lines)
assert raw == "\n".join(lines[:3]) + "\n"
assert consumed == 3
=== END AC html-block-termination ===

=== AC html-block-paragraph ===
Intent: A standalone custom tag cannot interrupt a paragraph, while a block-level tag can and ends before a blank line.

from commonmark_parser.html_blocks import parse_html_block

tag = "<custom>"
assert parse_html_block([tag], paragraph_open=True) is None
lines = ["<div>", "literal", "", "outside"]
raw, consumed = parse_html_block(lines, paragraph_open=True)
assert raw == "\n".join(lines[:2]) + "\n"
assert consumed == 2
=== END AC html-block-paragraph ===

## User Acceptance

- None.

## Guardrails

- Preserve raw HTML block content without escaping or inline parsing.
- Complete mixed-feature section checks belong to the later conformance integration story.
