# FEATURE: ATX Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse ATX headings of levels 1 to 6 with optional closing sequences and render them as h1 to h6 elements. |
| Depends On  | FEATURE-Thematic-Breaks.md |
| Provides    | ATX heading block |
| Consumes    | block-type registry, inline parser hook |

## Purpose

Implement the ATX headings section of the spec as a registered block start rule whose content is parsed as inlines.

## Rules

- An opening sequence of 1 to 6 `#` characters, preceded by up to three spaces of indentation, must be followed by a space, a tab or the end of the line. Seven or more `#` is not a heading, and `#hashtag` is not a heading.
- The content is stripped of leading and trailing spaces and tabs before inline parsing.
- An optional closing sequence of `#` characters must be preceded by a space or tab and followed only by spaces or tabs. Backslash-escaped `#` characters are not part of the closing sequence. A `#` run followed by other text is content.
- The heading level equals the number of opening `#` characters. A heading can be empty.
- An ATX heading can interrupt a paragraph and needs no blank lines around it.
- It renders as `<hN>content</hN>`.

## Reads

- Lines handed to the block engine.

## Writes

- Heading nodes in the block tree; inline content is parsed in phase 2.

## Programmatic Acceptance

The corpus section uses indented code and thematic break interactions, so it is gated in the lists story. The checks here are bounded.

=== AC atx-levels-one-to-six ===
Intent: Each opening-sequence length from 1 to 6 renders exactly one heading of that level.

import subprocess

for level in range(1, 7):
    source = "#" * level + " foo\n"
    result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h" + str(level) + ">") == 1
    assert result.stdout.count("<h") == 1
=== END AC atx-levels-one-to-six ===

=== AC atx-not-a-heading ===
Intent: Seven hashes, a missing space, and an escaped hash do not produce headings.

import subprocess

source = "####### foo\n\n#hashtag\n\n\\## foo\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h") == 0
assert result.stdout.count("<p>") == 3
=== END AC atx-not-a-heading ===

=== AC atx-closing-sequence ===
Intent: A closing hash sequence is removed from the heading content.

import subprocess

result = subprocess.run(["./commonmark"], input="## foo ##\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h2>") == 1
assert result.stdout.count("#") == 0
=== END AC atx-closing-sequence ===

=== AC atx-empty-heading ===
Intent: Empty headings are allowed, one per line.

import subprocess

result = subprocess.run(["./commonmark"], input="#\n\n##\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h1>") == 1
assert result.stdout.count("<h2>") == 1
=== END AC atx-empty-heading ===

=== AC atx-interrupts-paragraph ===
Intent: A heading splits a paragraph without blank lines, leaving two paragraphs around it.

import subprocess

result = subprocess.run(["./commonmark"], input="Foo bar\n# baz\nBar foo\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<h1>") == 1
assert result.stdout.count("<p>") == 2
=== END AC atx-interrupts-paragraph ===

=== AC atx-indentation-limit ===
Intent: Up to three spaces of indentation are allowed before the opening sequence, and four are not.

import subprocess

allowed = subprocess.run(["./commonmark"], input="   # foo\n", capture_output=True, text=True)
refused = subprocess.run(["./commonmark"], input="    # foo\n", capture_output=True, text=True)
print(allowed.stdout)
print(refused.stdout)
assert allowed.returncode == 0
assert refused.returncode == 0
assert allowed.stdout.count("<h1>") == 1
assert refused.stdout.count("<h1>") == 0
=== END AC atx-indentation-limit ===

## User Acceptance

- None.

## Guardrails

- A closing sequence must be preceded by whitespace; `foo#` keeps its hash.
- Heading content must go through inline parsing, never be emitted raw.
- Do not skip, filter or reinterpret corpus examples.
