# FEATURE: Code Spans

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse backtick-delimited inline code spans. |
| Depends On | FEATURE-EscapesAndEntities.md |
| Provides | code spans |
| Consumes | inline escapes and character references |

## Purpose

Recognize inline code spans in paragraph and heading content after block parsing has completed.

## Behavior

A backtick string is a maximal run of one or more backticks. An opener matches the next backtick string of equal length; unmatched runs remain literal text. Convert line endings in the enclosed content to spaces. If the resulting content begins and ends with an ASCII space and contains a non-space character, remove exactly one space from each end. Preserve all other content, including backslashes and entity syntax, literally; escape it when rendering HTML.

Code spans bind more tightly than emphasis and link brackets. Code spans, autolinks, and raw HTML have equal precedence, resolved in left-to-right parse order. Preserve these interactions as the later inline capabilities are added.

## Programmatic Acceptance

=== AC code-spans-conformance ===
Intent: The completed inline parser passes every authoritative code-span example, including precedence interactions.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^Code spans$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC code-spans-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Do not modify the supplied conformance assets.
