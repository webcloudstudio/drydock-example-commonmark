# FEATURE: Code Spans

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse literal inline code delimited by matching backtick runs. |
| Depends On | FEATURE-InlineText.md |
| Provides | code span parsing |
| Consumes | inline text parsing |

## Purpose and workflow

Extend `commonmark_parser.inlines.parse_inlines(source, references)` to recognize an opening backtick run and the next closing run of exactly the same length. Unmatched runs remain ordinary text. Normalize line endings inside a matched span to spaces. If the normalized content begins and ends with a space and is not entirely spaces, remove exactly one space from each end. Preserve all other content literally, including backslashes and character reference syntax.

Code spans bind more tightly than emphasis and link brackets. Their precedence relative to raw HTML and autolinks follows the specification when those providers are integrated. Return a node of type `code` with its normalized content in `literal`.

The complete Code spans corpus section is executed by conformance integration after interacting inline providers exist.

## Programmatic Acceptance

=== AC code-span-literal ===
Intent: Matching backtick runs yield a code node that preserves its literal content.

from commonmark_parser.inlines import parse_inlines

content = "literal &amp; text"
nodes = parse_inlines("`" + content + "`", {})
assert len(nodes) == 1
assert nodes[0].type == "code"
assert nodes[0].literal == content
=== END AC code-span-literal ===

=== AC code-span-normalization ===
Intent: A matched span converts its line ending to a space and removes one paired surrounding space.

from commonmark_parser.inlines import parse_inlines

first = "alpha"
second = "beta"
nodes = parse_inlines("` " + first + "\n" + second + " `", {})
assert len(nodes) == 1
assert nodes[0].type == "code"
assert nodes[0].literal.split(" ") == [first, second]
=== END AC code-span-normalization ===

=== AC code-span-unmatched ===
Intent: An unmatched opening run remains literal text.

from commonmark_parser.inlines import parse_inlines

source = "`unclosed"
nodes = parse_inlines(source, {})
assert len(nodes) == 1
assert nodes[0].type == "text"
assert nodes[0].literal == source
=== END AC code-span-unmatched ===

## User Acceptance

- None.

## Guardrails

- Do not interpret escapes or character references inside code spans.
- Preserve supplied conformance assets unchanged.
- Do not invoke the full-suite entry point in this story's checks.
