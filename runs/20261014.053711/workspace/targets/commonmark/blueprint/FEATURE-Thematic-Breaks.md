# FEATURE: Thematic Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse thematic breaks of three or more matching -, _ or * characters and render them as hr elements. |
| Depends On  | FEATURE-Line-Breaks-Text.md |
| Provides    | thematic break block |
| Consumes    | block-type registry |

## Purpose

Implement the Thematic breaks section of the spec as a registered block start rule.

## Rules

- A thematic break is a line with up to three spaces of indentation, then three or more matching `-`, `_` or `*` characters, each optionally followed by any number of spaces or tabs. No other characters may appear on the line.
- All non-space characters must be the same. Four or more spaces of indentation is not a thematic break.
- A thematic break can interrupt a paragraph and needs no blank lines around it.
- When a line could be a thematic break or a list item, the thematic break wins. When a line of dashes could be a thematic break or a setext underline, the setext heading wins; that wiring is added by the setext story.
- It renders as `<hr />`.

## Reads

- Lines handed to the block engine.

## Writes

- Thematic break nodes in the block tree.

## Programmatic Acceptance

The corpus section needs lists, setext headings and emphasis, so it is gated in the lists story. The checks here are bounded.

=== AC thematic-three-markers ===
Intent: Lines of three or more matching marker characters each render one hr element.

import subprocess

lines = ["***", "---", "___", "_____________", " - - -", " **  * ** * ** * **"]
source = "\n\n".join(lines) + "\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<hr />") == len(lines)
=== END AC thematic-three-markers ===

=== AC thematic-not-a-break ===
Intent: Wrong characters, too few characters, mixed characters and trailing text do not produce hr elements.

import subprocess

source = "+++\n\n--\n\n_ _ _ _ a\n\na------\n\n *-*\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<hr />") == 0
=== END AC thematic-not-a-break ===

=== AC thematic-interrupts-paragraph ===
Intent: A thematic break directly after paragraph text splits it into two paragraphs around one hr.

import subprocess

result = subprocess.run(["./commonmark"], input="Foo\n***\nbar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<hr />") == 1
assert result.stdout.count("<p>") == 2
=== END AC thematic-interrupts-paragraph ===

=== AC thematic-trailing-whitespace ===
Intent: Trailing spaces and tabs after the marker characters are allowed.

import subprocess

result = subprocess.run(["./commonmark"], input="- - - -    \t\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<hr />") == 1
=== END AC thematic-trailing-whitespace ===

## User Acceptance

- None.

## Guardrails

- Mixed marker characters on one line must never form a thematic break.
- Four spaces of indentation must never form a thematic break.
- Do not skip, filter or reinterpret corpus examples.
