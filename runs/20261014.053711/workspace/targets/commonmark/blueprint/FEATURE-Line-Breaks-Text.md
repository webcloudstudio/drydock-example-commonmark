# FEATURE: Line Breaks and Text

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Implement hard line breaks, soft line breaks and plain textual content in inline parsing. |
| Depends On  | FEATURE-Images.md |
| Provides    | hard break and soft break inline nodes |
| Consumes    | inline scanner loop |

## Purpose

Implement the Hard line breaks, Soft line breaks and Textual content sections of the spec.

## Rules

- A line ending preceded by two or more spaces, or by a backslash, that is not at the end of the block is a hard break, rendered as `<br />` followed by a line ending. The spaces or backslash are consumed. Leading spaces on the following line are dropped.
- Any other line ending inside a block is a soft break, rendered as a line ending. Spaces at the end of the line and at the start of the next line are removed.
- A hard-break marker at the end of a paragraph or heading is not a break: trailing spaces are dropped and a trailing backslash stays literal.
- Breaks work inside emphasis and link text. They are inert inside code spans (the line ending becomes a space) and inside raw HTML tags.
- All other characters are plain text. Internal spaces are preserved verbatim.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Break and text nodes in the inline tree.

## Programmatic Acceptance

The Hard line breaks section has an ATX heading example, so it is gated in the tabs story. The checks here are bounded.

=== AC breaks-corpus-sections ===
Intent: The Soft line breaks and Textual content conformance sections (5 cases) pass in full.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import os
import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.getcwd() + "/commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "^Soft line breaks$|^Textual content$",
    ],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC breaks-corpus-sections ===

=== AC breaks-hard-break-spaces ===
Intent: Two or more trailing spaces before a line ending give one br element between the two lines.

import subprocess

first = "alpha"
second = "beta"
result = subprocess.run(["./commonmark"], input=first + "   \n" + second + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<br />") == 1
assert first in result.stdout
assert second in result.stdout
=== END AC breaks-hard-break-spaces ===

=== AC breaks-hard-break-backslash ===
Intent: A backslash before a line ending gives one br element.

import subprocess

result = subprocess.run(["./commonmark"], input="alpha\\\nbeta\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<br />") == 1
=== END AC breaks-hard-break-backslash ===

=== AC breaks-soft-break ===
Intent: A plain line ending is not a hard break and both lines stay in one paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="alpha\nbeta\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<br />") == 0
assert result.stdout.count("<p>") == 1
=== END AC breaks-soft-break ===

=== AC breaks-none-at-block-end ===
Intent: Trailing spaces or a trailing backslash at the end of a paragraph do not create a break.

import subprocess

for source in ("alpha  \n", "alpha\\\n"):
    result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<br />") == 0
=== END AC breaks-none-at-block-end ===

=== AC breaks-inert-in-code-span ===
Intent: Trailing spaces before a line ending inside a code span do not create a break.

import subprocess

result = subprocess.run(["./commonmark"], input="`code  \nspan`\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<br />") == 0
assert result.stdout.count("<code>") == 1
=== END AC breaks-inert-in-code-span ===

## User Acceptance

- None.

## Guardrails

- A hard break must never occur at the end of a block.
- Spaces in the middle of a text line must never be collapsed.
- Do not skip, filter or reinterpret corpus examples.
