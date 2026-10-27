# FEATURE: Inline Line Breaks

| Field | Value |
|-------------|-------|
| Version | 20261027 V1 |
| Description | Parse and render hard and soft line breaks in inline content. |
| Depends On | FEATURE-AutolinksAndRawHtml.md, FEATURE-Emphasis.md |
| Provides | inline line breaks |
| Consumes | autolinks and raw inline HTML, emphasis and strong emphasis |

## Purpose

Convert line endings within inline content to hard or soft breaks after block parsing has completed.

## Behavior

A line ending preceded by two or more spaces or by a backslash produces a hard break, except at the end of a block. Other inline line endings produce soft breaks. Remove spaces at the end of a soft-break line and indentation at the start of the next line. Ignore indentation at the start of a line following a hard break.

Do not interpret line endings inside code spans or HTML tags as breaks. Apply these rules inside inline constructs that permit inline content. Render hard breaks as HTML break tags and soft breaks as line endings or spaces, consistent with the supplied examples.

With all parser capabilities available, run the previously deferred cross-feature examples as well as the complete sections owned by this story. The scoped patterns below cover the remaining specification sections without invoking the full-suite entry point.

## Programmatic Acceptance

=== AC inline-line-breaks-sections ===
Intent: The parser passes the complete hard and soft line break examples, including their interactions with inline constructs.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"), "--spec", "sources/spec.txt", "--pattern", "^(Hard line breaks|Soft line breaks)$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-line-breaks-sections ===

=== AC deferred-cross-feature-sections ===
Intent: The completed parser passes earlier examples that combine block and inline capabilities, including tabs and ordinary textual content.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"), "--spec", "sources/spec.txt", "--pattern", "^(Tabs|Precedence|Thematic breaks|Paragraphs|Blank lines|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Link reference definitions|Block quotes|List items|Lists|Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Textual content)$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC deferred-cross-feature-sections ===

## User Acceptance

- None.

## Guardrails

- Parse blocks and collect reference definitions before parsing inline content.
- Do not use a public Markdown implementation or modify the supplied conformance assets.
