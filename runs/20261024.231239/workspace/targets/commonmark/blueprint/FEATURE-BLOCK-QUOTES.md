# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses block quote containers and their contents according to CommonMark 0.31.2. |
| Depends On  | FEATURE-PARAGRAPHS.md, FEATURE-ATX-HEADINGS.md, FEATURE-BLANK-LINES.md |
| Provides    | block quote parsing and rendering |
| Consumes    | commonmark |

## Purpose

Parse block quotes as containers around the same block types supported at the document level. A block quote marker is `>` preceded by up to three spaces, optionally followed by one space. The marker may be omitted on paragraph continuation lines when CommonMark laziness rules allow it.

## Behavior

- Consecutive quoted lines form one block quote; a blank line separates adjacent block quotes.
- Quotes may interrupt paragraphs and contain initial or final blank lines.
- Support nested block quotes and lazy paragraph continuation. Laziness applies only when a line continues paragraph text; it cannot continue a heading, code block, list, or other block construct.
- Parse the resulting contents using the document’s block parser and render them inside `<blockquote>` and `</blockquote>`.

## Programmatic Acceptance

=== AC block-quotes-conformance ===
Intent: All supplied Block quotes examples pass through the executable.
Suite: scoped
Probe: --list
Probe Count: summary

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Block quotes"],
    capture_output=True, text=True,
    env={**os.environ, "PYTHONPATH": f"{os.getcwd()}/sources"},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes-conformance ===

## User Acceptance

- None.

## Guardrails

- Preserve quoted content and nesting; do not parse content as inline text until block structure and document link definitions are available.
- Do not modify supplied scoring assets.
- Do not use a public Markdown implementation.
