# FEATURE: Emphasis

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Resolve emphasis and strong emphasis using delimiter runs. |
| Depends On | FEATURE-CodeSpans.md, FEATURE-EscapesAndEntities.md |
| Provides | emphasis and strong emphasis |
| Consumes | code spans, inline escapes and character references |

## Purpose

Parse emphasis and strong emphasis in inline content while preserving the precedence of other inline constructs.

## Behavior

Classify maximal `*` and `_` delimiter runs using the specification's left- and right-flanking rules, Unicode whitespace and punctuation, and the additional underscore restrictions. Use the delimiter stack and the multiple-of-three restriction to find valid opener and closer pairs. Consume two delimiters on each side for strong emphasis when both runs permit it, otherwise consume one for emphasis. Resolve nesting and overlapping spans according to the specification, leaving unmatched delimiters literal.

Code spans bind more tightly than emphasis. Links, images, autolinks, and HTML also bind more tightly when those capabilities are available. Follow the appendix's process-emphasis procedure, including its stack boundary for link and image contents.

## Programmatic Acceptance

=== AC emphasis-conformance ===
Intent: The completed inline parser passes the authoritative emphasis and strong-emphasis examples.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^Emphasis and strong emphasis$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC emphasis-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Do not modify the supplied conformance assets.
