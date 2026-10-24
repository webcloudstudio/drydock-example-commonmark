# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Defines the Python command-line parser structure and its block-first, inline-second parsing boundary. |

## Purpose

The application is a Python command-line program rooted at `./commonmark`. It reads UTF-8 Markdown from standard input and writes rendered HTML to standard output.

## Components and boundaries

- The executable delegates parsing and rendering to original project code. It must not use a public Markdown implementation.
- The parser builds block structure before parsing inline content. Link reference definitions are collected during block parsing and made available to the inline phase.
- Block parsing owns paragraphs, headings, code blocks, HTML blocks, thematic breaks, block quotes, and lists. Inline parsing owns inline constructs such as escapes, code spans, emphasis, links, images, autolinks, raw HTML, and line breaks.
- The renderer converts the parsed document to HTML. The supplied conformance runner invokes `./commonmark` and compares normalized HTML with examples from the supplied specification.
- Runtime conformance assets are staged verbatim under `sources/`: `spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh`.

## Module ownership

| Boundary | Owner | Allowed access |
|-----------|-------|----------------|
| Parsing and rendering | Project parser modules | Internal parser and renderer interfaces |
| Configuration | None | No configuration store is specified |
| File store | None | No file store is specified |
| External services | None | No external service is specified |
| Conformance assets | `sources/` | Read-only runtime inputs for the supplied test harness |

## Technology Stack

| Technology | Use |
|------------|-----|
| Python 3 | CLI, parser, renderer, and project checks |
| Python standard library | Runtime implementation without third-party dependencies |
| POSIX shell | Supplied full-suite invocation |

## Programmatic Acceptance

=== AC architecture-staged-assets ===
Intent: The architecture story stages the corpus and runner inputs needed by later scoped checks.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt", "--dump-tests"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
tests = json.loads(result.stdout)
assert len(tests) > 0
=== END AC architecture-staged-assets ===

## User Acceptance

- None.

## Guardrails

- Keep the five supplied runtime conformance assets unchanged.
- Do not modify scoring assets or author or replace `sources/full_test.sh`.
- Preserve the parser boundary between block structure and inline parsing.
- Do not use a public Markdown implementation.
