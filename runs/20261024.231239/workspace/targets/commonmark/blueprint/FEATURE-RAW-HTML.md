# FEATURE: Raw HTML

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Preserves inline raw HTML tags and markup in rendered output. |
| Depends On  | ARCHITECTURE.md |
| Provides    | inline raw HTML |
| Consumes    | — |

## Purpose

Preserve valid inline HTML tags, comments, processing instructions, declarations, and CDATA sections as literal markup in HTML output.

## Behavior

- Recognize the raw HTML forms defined by CommonMark 0.31.2 within inline content.
- Preserve recognized markup verbatim, including tag names, attributes, whitespace, and line breaks.
- Escape `<` and `>` when the input resembles markup but does not match a recognized raw HTML form.
- Block HTML parsing is owned by `FEATURE-HTML-BLOCKS.md`.

## Programmatic Acceptance

=== AC raw-html-conformance ===
Intent: All supplied Raw HTML examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Raw HTML"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC raw-html-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep supplied scoring assets unchanged.
