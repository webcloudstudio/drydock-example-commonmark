# FEATURE: Indented Code

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize indented code blocks and preserve their literal content. |
| Depends On | FEATURE-Paragraphs.md |
| Provides | indented code block parsing |
| Consumes | paragraph block parsing |

## Purpose

Identify indented code chunks during block parsing and retain their literal content for HTML rendering.

## Behavior

An indented code block consists of nonblank lines indented at least four columns, with intervening blank lines. Remove four columns of indentation from content lines, expanding tabs only as needed to determine indentation and preserving remaining content literally. Preserve interior blank lines and extra indentation; omit blank lines before or after the block. An indented code block cannot interrupt an open paragraph. A nonblank line with insufficient indentation ends the block.

Expose `parse_indented_code(lines, paragraph_open=False)` from `commonmark_parser.indented_code`. It accepts lines without line endings and returns `(content, consumed)` for a recognized block, with content lines terminated by newline, or `None` when no block starts. `consumed` counts the input lines belonging to the block and excludes trailing blank lines.

## Programmatic Acceptance

=== AC indented-code-content ===
Intent: Four-column indentation is removed while extra indentation and interior blank lines remain literal.

from commonmark_parser.indented_code import parse_indented_code

first = "alpha"
second = "  beta"
content, consumed = parse_indented_code(["    " + first, "", "    " + second, ""])
assert content == first + "\n\n" + second + "\n"
assert consumed == 3
=== END AC indented-code-content ===

=== AC indented-code-interruption ===
Intent: Indented code does not interrupt an open paragraph and ends before a less-indented nonblank line.

from commonmark_parser.indented_code import parse_indented_code

line = "    literal"
assert parse_indented_code([line], paragraph_open=True) is None
content, consumed = parse_indented_code([line, "outside"])
assert content == line[4:] + "\n"
assert consumed == 1
=== END AC indented-code-interruption ===

## User Acceptance

- None.

## Guardrails

- Preserve literal code content; do not parse it as inline Markdown.
- Complete mixed-feature section checks belong to the later conformance integration story.
