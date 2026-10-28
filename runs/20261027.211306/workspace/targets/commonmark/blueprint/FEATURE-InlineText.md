# FEATURE: Inline Text

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse ordinary inline text, escapes, character references, and soft line breaks. |
| Depends On | FEATURE-Lists.md |
| Provides | inline text parsing |
| Consumes | list block parsing, document reference map |

## Purpose and workflow

After the document block tree and reference map are complete, parse paragraph and heading text as inlines. A backslash escapes an ASCII punctuation character; otherwise it remains literal. Decode valid semicolon-terminated HTML5 named entities and valid decimal or hexadecimal numeric references under the specification's length and code-point rules. Replace invalid Unicode scalar values and U+0000 with U+FFFD. Unrecognized references remain text.

Represent ordinary text and soft line breaks in sequence. Remove spaces at the end of a soft-breaking line and at the beginning of the next line. Preserve the distinction between text parsing and literal contexts: escapes and references are not interpreted inside code spans, code blocks, autolinks, or raw HTML where the specification excludes them.

Expose `parse_inlines(source, references)` from `commonmark_parser.inlines`. It returns ordered inline nodes with `type` and, for text nodes, `literal`; a soft break has type `softbreak`. The reference map is supplied after block parsing, even where this increment does not use it.

Conformance integration executes the complete Backslash escapes, Entity and numeric character references, Soft line breaks, and Textual content sections after interacting inline capabilities exist.

## Programmatic Acceptance

=== AC inline-escape ===
Intent: Escaped ASCII punctuation becomes literal text without retaining the escape marker.

from commonmark_parser.inlines import parse_inlines

punctuation = "!"
nodes = parse_inlines("\\" + punctuation, {})
assert len(nodes) == 1
assert nodes[0].type == "text"
assert nodes[0].literal == punctuation
=== END AC inline-escape ===

=== AC inline-soft-break ===
Intent: A regular line ending separates text nodes with a soft break while retaining their text.

from commonmark_parser.inlines import parse_inlines

first = "alpha"
second = "beta"
nodes = parse_inlines(first + "\n" + second, {})
assert [node.type for node in nodes] == ["text", "softbreak", "text"]
assert nodes[0].literal == first
assert nodes[2].literal == second
=== END AC inline-soft-break ===

=== AC inline-numeric-reference ===
Intent: A valid numeric character reference decodes to the character designated by its input code point.

from commonmark_parser.inlines import parse_inlines

codepoint = 65
nodes = parse_inlines(f"&#{codepoint};", {})
assert len(nodes) == 1
assert nodes[0].type == "text"
assert nodes[0].literal == chr(codepoint)
=== END AC inline-numeric-reference ===

## User Acceptance

- None.

## Guardrails

- Complete block parsing and reference collection before inline parsing.
- Preserve supplied conformance assets unchanged.
- Do not invoke the full-suite entry point in this story's checks.
