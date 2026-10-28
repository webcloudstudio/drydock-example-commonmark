# FEATURE: Fenced Code

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize fenced code blocks and their info strings. |
| Depends On | FEATURE-Paragraphs.md |
| Provides | fenced code block parsing |
| Consumes | paragraph block parsing |

## Purpose

Parse fenced code as a literal block, including its optional info string, for subsequent HTML rendering.

## Behavior

An opening fence has at least three consecutive backticks or tildes and at most three spaces of indentation. A backtick fence's info string cannot contain a backtick. Trim the info string's outer spaces and tabs. A closing fence uses the same character, at least the opening length, at most three spaces of indentation, and only spaces or tabs after the fence. If none is found, the block continues to the end of its containing block or document. Remove up to the opening indentation from each content line. Fenced code may interrupt a paragraph.

Preserve content literally. For HTML, decode applicable escapes and character references in the info string and use its first word as the `language-` class suffix; escape code and attribute content for HTML.

Expose `parse_fenced_code(lines)` from `commonmark_parser.fenced_code`. It accepts lines without line endings and returns `(content, info, consumed)` for a recognized block, or `None` if the first line is not an opening fence. Content lines carry newline terminators; `info` is the trimmed raw info string.

## Programmatic Acceptance

=== AC fenced-code-matching ===
Intent: A fence closes only with a sufficiently long matching delimiter and preserves intervening literal content.

from commonmark_parser.fenced_code import parse_fenced_code

literal = "alpha * beta"
content, info, consumed = parse_fenced_code(["```` lang", literal, "```", "````", "after"])
assert content == literal + "\n" + "```" + "\n"
assert info == "lang"
assert consumed == 4
=== END AC fenced-code-matching ===

=== AC fenced-code-unclosed ===
Intent: An unclosed fence consumes the remaining input and removes the opening indentation from content.

from commonmark_parser.fenced_code import parse_fenced_code

literal = "alpha"
content, info, consumed = parse_fenced_code(["  ~~~", "  " + literal])
assert content == literal + "\n"
assert info == ""
assert consumed == 2
assert parse_fenced_code(["``` invalid ` info"]) is None
=== END AC fenced-code-unclosed ===

## User Acceptance

- None.

## Guardrails

- Do not interpret code block content as inline Markdown.
- Complete mixed-feature section checks belong to the later conformance integration story.
