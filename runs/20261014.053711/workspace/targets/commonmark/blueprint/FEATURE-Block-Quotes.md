# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse block quotes with marker handling, lazy continuation and the blank-line consecutiveness rule. |
| Depends On  | FEATURE-HTML-Blocks.md |
| Provides    | block quote container |
| Consumes    | block-type registry, lazy continuation check |

## Purpose

Implement the Block quotes section of the spec as a registered container block.

## Rules

- A block quote marker is `>` with up to three spaces of indentation, optionally followed by one space of indentation. A following tab is treated column-aware, so a partly consumed tab leaves its remaining columns as content indentation.
- Continue rule: a line continues the quote if it has a marker. A line without a marker is a lazy continuation only if it would be paragraph continuation text of the deepest open paragraph. Headings, fences, thematic breaks, list items and indented code do not continue lazily.
- A blank line (or a line with only a marker) behaves as in the spec: a fully blank line ends the quote, so two quotes separated by a blank line stay separate.
- Block quotes can interrupt paragraphs and nest. Any number of leading `>` may be omitted on a lazy line of a nested quote.
- A quote can be empty. It renders as `<blockquote>` and `</blockquote>` with contents on separate lines.

## Reads

- Lines handed to the block engine.

## Writes

- Block quote nodes in the block tree.

## Programmatic Acceptance

The corpus section has examples that use lists, so it is gated in the lists story. The checks here are bounded.

=== AC quote-basic-content ===
Intent: A quote with a heading and paragraph lines renders one blockquote containing one h1 and one paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="> # Foo\n> bar\n> baz\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 1
assert result.stdout.count("<h1>") == 1
assert result.stdout.count("<p>") == 1
=== END AC quote-basic-content ===

=== AC quote-marker-space-optional ===
Intent: The space after the marker is optional, and up to three spaces of indentation are allowed.

import subprocess

for source in ("># Foo\n>bar\n", "   > # Foo\n   > bar\n"):
    result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<h1>") == 1
=== END AC quote-marker-space-optional ===

=== AC quote-lazy-continuation ===
Intent: An unmarked paragraph continuation line stays in the quote's paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="> bar\nbaz\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 1
assert result.stdout.count("<p>") == 1
=== END AC quote-lazy-continuation ===

=== AC quote-nested-lazy ===
Intent: Omitted markers on a nested quote's continuation line still keep three nesting levels and one paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="> > > foo\nbar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 3
assert result.stdout.count("<p>") == 1
=== END AC quote-nested-lazy ===

=== AC quote-blank-line-separates ===
Intent: A blank line separates two quotes, and adjacent marked lines form one quote.

import subprocess

separated = subprocess.run(["./commonmark"], input="> foo\n\n> bar\n", capture_output=True, text=True)
joined = subprocess.run(["./commonmark"], input="> foo\n> bar\n", capture_output=True, text=True)
print(separated.stdout)
print(joined.stdout)
assert separated.returncode == 0
assert joined.returncode == 0
assert separated.stdout.count("<blockquote>") == 2
assert joined.stdout.count("<blockquote>") == 1
=== END AC quote-blank-line-separates ===

=== AC quote-interrupts-paragraph ===
Intent: A quote interrupts a paragraph, leaving one paragraph before it and one inside it.

import subprocess

result = subprocess.run(["./commonmark"], input="foo\n> bar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 1
assert result.stdout.count("<p>") == 2
=== END AC quote-interrupts-paragraph ===

=== AC quote-four-spaces-is-code ===
Intent: Four spaces before the marker make an indented code block, not a quote.

import subprocess

result = subprocess.run(["./commonmark"], input="    > foo\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 0
assert result.stdout.count("<pre>") == 1
=== END AC quote-four-spaces-is-code ===

=== AC quote-no-lazy-code ===
Intent: Laziness does not apply to indented code, so the unmarked indented line becomes its own code block.

import subprocess

result = subprocess.run(["./commonmark"], input=">     foo\n    bar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<blockquote>") == 1
assert result.stdout.count("<pre>") == 2
=== END AC quote-no-lazy-code ===

## User Acceptance

- None.

## Guardrails

- Laziness must apply only to paragraph continuation text.
- Two quotes must never merge across a blank line.
- Do not skip, filter or reinterpret corpus examples.
