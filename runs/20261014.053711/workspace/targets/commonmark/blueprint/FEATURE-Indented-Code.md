# FEATURE: Indented Code

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse indented code blocks made of chunks of lines indented four or more columns and render them as pre and code elements. |
| Depends On  | FEATURE-ATX-Headings.md |
| Provides    | indented code block |
| Consumes    | block-type registry |

## Purpose

Implement the Indented code blocks section of the spec as a registered block start rule.

## Rules

- A line with four or more columns of indentation (column-aware, tab stop 4), that is not blank and does not continue a paragraph, starts an indented code block.
- An indented code block cannot interrupt a paragraph. A non-blank line with fewer than four columns of indentation ends the block immediately.
- Chunks are separated by blank lines. Interior blank lines are kept in the content, with any indentation beyond four columns retained. Leading and trailing blank lines are not part of the block.
- Content is the literal lines minus four columns of indentation, including trailing spaces, and is HTML-escaped. It is never parsed as Markdown. There is no info string.
- It renders as `<pre><code>...</code></pre>` with a final line ending inside the code element.

## Reads

- Lines handed to the block engine.

## Writes

- Code block nodes in the block tree.

## Programmatic Acceptance

The corpus section examples use lists, so it is gated in the lists story. The checks here are bounded.

=== AC indented-simple-block ===
Intent: Four-space-indented lines render one pre element whose code keeps the extra indentation and content.

import subprocess

first = "a simple"
second = "  indented code block"
source = "    " + first + "\n    " + second + "\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert result.stdout.count("<code>") == 1
assert first in result.stdout
assert second in result.stdout
=== END AC indented-simple-block ===

=== AC indented-cannot-interrupt-paragraph ===
Intent: An indented line directly after paragraph text is a continuation, not a code block.

import subprocess

result = subprocess.run(["./commonmark"], input="Foo\n    bar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 0
assert result.stdout.count("<p>") == 1
=== END AC indented-cannot-interrupt-paragraph ===

=== AC indented-chunks-and-ending ===
Intent: Chunks separated by a blank line form one block, and an unindented line ends it and starts a paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="    chunk1\n\n    chunk2\nbar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert result.stdout.count("<p>") == 1
=== END AC indented-chunks-and-ending ===

=== AC indented-content-escaped-and-literal ===
Intent: Code content is escaped and not parsed as Markdown, so only the four code wrapper tags contribute angle brackets.

import subprocess

result = subprocess.run(["./commonmark"], input="    <a/>\n    *hi*\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<") == 4
assert result.stdout.count("<em>") == 0
=== END AC indented-content-escaped-and-literal ===

=== AC indented-tab-indentation ===
Intent: A leading tab counts as four columns of indentation.

import subprocess

result = subprocess.run(["./commonmark"], input="\tfoo\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
=== END AC indented-tab-indentation ===

## User Acceptance

- None.

## Guardrails

- Never let an indented code block interrupt a paragraph.
- Never expand tabs inside code content; only the indentation prefix is column-aware.
- Do not skip, filter or reinterpret corpus examples.
