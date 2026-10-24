# FEATURE: Backslash Escapes

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Implement backslash escapes of ASCII punctuation in text and expose a shared unescape helper for destinations, titles and info strings. |
| Depends On  | FEATURE-Code-Spans.md |
| Provides    | backslash escape inline rule, shared unescape helper |
| Consumes    | inline scanner loop |

## Purpose

Implement the Backslash escapes section of the spec.

## Rules

- A backslash followed by any ASCII punctuation character yields that character as plain text with no Markdown meaning, so it cannot start emphasis, a link, a code span, a heading, a list or a tag.
- A backslash followed by any other character is a literal backslash.
- A backslash at the end of a line is a hard break marker, handled by the line-breaks story.
- A backslash that is itself escaped leaves the next character unescaped.
- Backslash escapes are inert in code spans, code blocks, autolinks and raw HTML.
- The shared `unescape` helper applies the same rule to link destinations, link titles and fenced code info strings, and is reused by those stories.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Plain text nodes in the inline tree.

## Programmatic Acceptance

The Backslash escapes corpus section uses fenced code, links and definitions, so it is gated in the tabs story. The checks here are bounded.

=== AC escapes-punctuation-inert ===
Intent: An escaped asterisk prevents emphasis.

import subprocess

result = subprocess.run(["./commonmark"], input="\\*not emphasized*\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<em>") == 0
assert result.stdout.count("\\") == 0
=== END AC escapes-punctuation-inert ===

=== AC escapes-non-punctuation-literal ===
Intent: A backslash before a non-punctuation character is kept as a literal backslash.

import subprocess

text = "\\A\\a\\3"
result = subprocess.run(["./commonmark"], input=text + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert text in result.stdout
=== END AC escapes-non-punctuation-literal ===

=== AC escapes-block-markers ===
Intent: An escaped heading marker does not start a heading.

import subprocess

result = subprocess.run(["./commonmark"], input="\\# word\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h1>") == 0
assert result.stdout.count("<p>") == 1
=== END AC escapes-block-markers ===

=== AC escapes-inert-in-code-span ===
Intent: A backslash in a code span is not an escape.

import subprocess

content = "\\*"
result = subprocess.run(["./commonmark"], input="`" + content + "`\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert content in result.stdout
=== END AC escapes-inert-in-code-span ===

## User Acceptance

- None.

## Guardrails

- Never treat a backslash before a non-punctuation character as an escape.
- Never process escapes in code spans, code blocks, autolinks or raw HTML.
- Do not skip, filter or reinterpret corpus examples.
