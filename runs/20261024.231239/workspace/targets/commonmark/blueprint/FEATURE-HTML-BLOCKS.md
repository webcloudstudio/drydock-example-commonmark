# FEATURE: HTML Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Recognizes CommonMark block HTML and preserves it as raw output. |
| Depends On  | FEATURE-CLI.md |
| Provides    | HTML blocks |

## Purpose

Recognize the seven CommonMark HTML block types and pass their lines through as raw HTML, ending each block according to its type’s termination rule.

## Behavior

- Start conditions allow up to three spaces of indentation.
- Types 1–5 end at their matching end condition; types 6–7 end at a blank line. A block also ends at the containing block or document boundary.
- Types 1–6 may interrupt a paragraph; type 7 may not.
- Preserve block content literally. Do not parse Markdown within an HTML block.

## Programmatic Acceptance

=== AC html-block-conformance ===
Intent: The supplied “HTML blocks” examples define correct block HTML parsing and rendering.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "HTML blocks"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC html-block-conformance ===

## User Acceptance

- None.

## Guardrails

- Preserve raw HTML block content without escaping or interpreting it as Markdown.
- Keep all supplied scoring assets unchanged.
