# FEATURE: Block Engine

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | The phase 1 block engine with an extensible block-type registry, paragraph and blank-line handling, and HTML rendering with escaping. |
| Depends On  | FEATURE-Executable.md |
| Provides    | block tree builder, block-type registry, paragraph renderer, HTML escaping helper, URL percent-encoding helper |
| Consumes    | ./commonmark, inline parser hook |

## Purpose

Implement the per-line procedure from the spec Appendix, "Phase 1: block structure", and render paragraphs. Later block stories add start, continue and close rules to the registry without changing the loop.

## Sequence

For each line:

1. Walk the open blocks from the document down the last-child chain. Each block checks whether the line continues it. Unmatched blocks are not closed yet, because the line may be a lazy continuation.
2. Look for new block starts. If one is found, close the unmatched blocks, then create the new block under the last matched container.
3. Add the remaining text to the deepest open block. A line that is a lazy paragraph continuation is added to the open paragraph.

At end of input all open blocks are closed. Phase 2 then walks the tree and calls the inline parser hook for paragraph and heading content. The hook initially returns the escaped text.

## Rules

- A paragraph is a sequence of non-blank lines that is not another block. Its raw content strips initial and final spaces and tabs. Lines after the first may have any indentation.
- Blank lines separate paragraphs and are otherwise ignored, including at the start and end of the document.
- Column-aware indentation (tab stop 4) is computed in one shared helper, so later block stories reuse it.
- The renderer emits `<p>` elements, one line ending between blocks, and escapes `&`, `<`, `>` and `"` in text.
- The shared URL percent-encoding helper lives here and is reused by the link and autolink stories.

## Reads

- Lines produced by `mdparser.cli`.

## Writes

- HTML string returned to `mdparser.cli`.

## Programmatic Acceptance

The corpus sections Paragraphs and Blank lines need indented code, hard breaks and ATX headings, so they are gated in the tabs story and the terminal story. The checks here are bounded.

=== AC engine-paragraph-count ===
Intent: Blank-line-separated paragraphs render as one p element each.

import subprocess

paragraphs = ["alpha beta", "gamma delta", "epsilon"]
source = "\n\n".join(paragraphs) + "\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
assert result.stdout.count("<p>") == len(paragraphs)
assert result.stdout.count("</p>") == len(paragraphs)
for text in paragraphs:
    assert text in result.stdout
=== END AC engine-paragraph-count ===

=== AC engine-multiline-paragraph ===
Intent: Consecutive non-blank lines with arbitrary indentation after the first stay in one paragraph.

import subprocess

first = "first line"
second = "second line"
third = "third line"
source = first + "\n" + "             " + second + "\n" + third + "\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
for text in (first, second, third):
    assert text in result.stdout
=== END AC engine-multiline-paragraph ===

=== AC engine-blank-lines-ignored ===
Intent: Leading, trailing and repeated blank lines produce no extra blocks, and a blank-only document produces no paragraph.

import subprocess

word = "content"
padded = "\n  \n\n" + word + "\n\n\n  \n"
result = subprocess.run(["./commonmark"], input=padded, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1

blank = subprocess.run(["./commonmark"], input="\n \n\t\n", capture_output=True, text=True)
assert blank.returncode == 0
assert blank.stdout.count("<p>") == 0
=== END AC engine-blank-lines-ignored ===

=== AC engine-html-escaping ===
Intent: Special characters in paragraph text are escaped, so only the paragraph tags contribute angle brackets.

import subprocess

source = "x < y > z & w\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<") == 2
assert result.stdout.count(">") == 2
=== END AC engine-html-escaping ===

## User Acceptance

- None.

## Guardrails

- Do not hard-code block handling in the main loop; every block type is registered through the registry.
- Never close an unmatched block before new block starts have been tried.
- Never write anything but rendered HTML to stdout.
