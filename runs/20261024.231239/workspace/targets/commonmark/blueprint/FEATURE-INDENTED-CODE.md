# FEATURE: Indented Code Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders CommonMark indented code blocks. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md, FEATURE-ATX-HEADINGS.md, FEATURE-SETEXT-HEADINGS.md |
| Provides    | Indented code block parsing and rendering |
| Consumes    | commonmark |

## Purpose

Recognize indented code blocks from nonblank lines indented by at least four spaces, including chunks separated by blank lines. Remove the required indentation, retain literal contents and applicable trailing whitespace, and render contents as escaped code without inline parsing. An indented code block cannot interrupt a paragraph.

## Programmatic Acceptance

=== AC indented-code-conformance ===
Intent: The executable passes every supplied example in the Indented code blocks section.
Suite: scoped
Probe: --dump-tests
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program", "./commonmark",
        "--spec", "sources/spec.txt",
        "--pattern", "Indented code blocks",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC indented-code-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow CommonMark 0.31.2 indented code block rules.
- Preserve supplied scoring assets unchanged.
