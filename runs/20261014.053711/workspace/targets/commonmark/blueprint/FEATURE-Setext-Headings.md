# FEATURE: Setext Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse setext headings, including multiline content and the precedence and laziness exclusions. |
| Depends On  | FEATURE-Block-Quotes.md |
| Provides    | setext heading block |
| Consumes    | paragraph block, thematic break block |

## Purpose

Implement the Setext headings section of the spec.

## Rules

- A setext heading is one or more lines of paragraph text followed by an underline of `=` (level 1) or `-` (level 2) characters, with up to three spaces of indentation and only trailing spaces or tabs after. The underline cannot contain internal spaces.
- The text lines must be such that, without the underline, they would form a paragraph. The first line has at most three spaces of indentation.
- The underline applies to the whole accumulated paragraph, so multiple lines become one heading. The heading content is the paragraph's raw text with leading and trailing spaces and tabs removed, parsed as inlines. Trailing spaces or a backslash on the last content line are not a hard break.
- An underline of dashes takes precedence over a thematic break reading of the same line when it follows paragraph text. Without paragraph text it is a thematic break. A setext heading cannot be empty, so `====` alone is a paragraph.
- The underline cannot be a lazy continuation line of a container: after a quote or list item, an unmarked underline does not underline the container's paragraph.
- Link reference definitions already extracted from the paragraph's start do not become heading text.

## Reads

- Lines handed to the block engine; the open paragraph.

## Writes

- Heading nodes of level 1 or 2 in the block tree.

## Programmatic Acceptance

The corpus section has examples that use lists, so it is gated in the lists story. The checks here are bounded.

=== AC setext-both-levels ===
Intent: Equals underlines give h1 and dash underlines give h2.

import subprocess

equals = subprocess.run(["./commonmark"], input="Foo *bar*\n=========\n", capture_output=True, text=True)
dashes = subprocess.run(["./commonmark"], input="Foo *bar*\n---------\n", capture_output=True, text=True)
print(equals.stdout)
print(dashes.stdout)
assert equals.returncode == 0
assert dashes.returncode == 0
assert equals.stdout.count("<h1>") == 1
assert dashes.stdout.count("<h2>") == 1
assert equals.stdout.count("<em>") == 1
=== END AC setext-both-levels ===

=== AC setext-multiline-content ===
Intent: Several paragraph lines before the underline become one heading with no paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="Foo\nBar\n---\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h2>") == 1
assert result.stdout.count("<p>") == 0
=== END AC setext-multiline-content ===

=== AC setext-underline-beats-thematic-break ===
Intent: Dashes after paragraph text make a heading, not a thematic break.

import subprocess

result = subprocess.run(["./commonmark"], input="Foo\n---\nbar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h2>") == 1
assert result.stdout.count("<hr />") == 0
assert result.stdout.count("<p>") == 1
=== END AC setext-underline-beats-thematic-break ===

=== AC setext-sequence-with-thematic-breaks ===
Intent: Dashes with no preceding paragraph are thematic breaks, mixed with two setext headings and a paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="---\nFoo\n---\nBar\n---\nBaz\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<hr />") == 1
assert result.stdout.count("<h2>") == 2
assert result.stdout.count("<p>") == 1
=== END AC setext-sequence-with-thematic-breaks ===

=== AC setext-underline-limits ===
Intent: Four spaces of indentation or internal spaces disqualify the underline.

import subprocess

for source in ("Foo\n    ---\n", "Foo\n= =\n"):
    result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h1>") == 0
    assert result.stdout.count("<h2>") == 0
    assert result.stdout.count("<p>") == 1
=== END AC setext-underline-limits ===

=== AC setext-not-lazy-in-quote ===
Intent: An unmarked underline after a quote paragraph does not make a heading inside the quote.

import subprocess

result = subprocess.run(["./commonmark"], input="> foo\nbar\n===\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h1>") == 0
assert result.stdout.count("<blockquote>") == 1
assert result.stdout.count("<p>") == 1
=== END AC setext-not-lazy-in-quote ===

=== AC setext-quote-then-thematic-break ===
Intent: Dashes after a quote without a marker are a thematic break outside the quote.

import subprocess

result = subprocess.run(["./commonmark"], input="> Foo\n---\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 1
assert result.stdout.count("<hr />") == 1
assert result.stdout.count("<h2>") == 0
=== END AC setext-quote-then-thematic-break ===

=== AC setext-empty-is-paragraph ===
Intent: An underline with no content line is not a heading.

import subprocess

result = subprocess.run(["./commonmark"], input="\n====\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h1>") == 0
assert result.stdout.count("<p>") == 1
=== END AC setext-empty-is-paragraph ===

## User Acceptance

- None.

## Guardrails

- A setext underline must never act through lazy continuation.
- A setext heading must never be empty.
- Do not skip, filter or reinterpret corpus examples.
