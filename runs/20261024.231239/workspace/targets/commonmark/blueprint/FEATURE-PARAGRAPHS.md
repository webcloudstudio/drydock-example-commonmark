# FEATURE: Paragraphs

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses paragraph boundaries and renders paragraph inline content. |
| Depends On  | FEATURE-CLI.md |
| Provides    | paragraphs |

## Purpose

Recognize paragraphs as sequences of nonblank lines that do not begin another block construct, then render their content as inline text.

## Behavior

- Join continuation lines with line endings.
- Ignore leading and trailing spaces or tabs around the paragraph’s raw content.
- Permit up to three leading spaces on the first line; four spaces begin indented code instead.
- Close a paragraph at a blank line or when a valid interrupting block begins.

## Programmatic Acceptance

=== AC paragraph-conformance ===
Intent: The supplied “Paragraphs” examples define correct paragraph boundaries and rendering.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Paragraphs"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC paragraph-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not treat indented code as a paragraph interrupt.
- Keep all supplied scoring assets unchanged.
