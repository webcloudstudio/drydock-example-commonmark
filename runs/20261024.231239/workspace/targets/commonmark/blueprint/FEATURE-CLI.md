# FEATURE: Command-line Interface

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Provides the root executable for converting Markdown from standard input to HTML on standard output. |
| Depends On  | — |
| Provides    | commonmark |
| Consumes    | — |

## Purpose

The `commonmark` executable at the application root reads Markdown from standard input and writes the rendered HTML to standard output. The input is UTF-8 Markdown. Do not use a public Markdown implementation.

## Interface

Invoke the executable directly as `./commonmark`. It reads until standard input reaches end of file and writes the resulting HTML to standard output.

## Programmatic Acceptance

=== AC cli-empty-input ===
Intent: The root executable accepts empty standard input and exits successfully.

import subprocess

result = subprocess.run(
    ["./commonmark"], input="", capture_output=True, text=True
)
assert result.returncode == 0
=== END AC cli-empty-input ===

=== AC cli-markdown-input ===
Intent: The root executable accepts Markdown on standard input and exits successfully.

import subprocess

source = "hello\n"
result = subprocess.run(
    ["./commonmark"], input=source, capture_output=True, text=True
)
assert result.returncode == 0
=== END AC cli-markdown-input ===

## User Acceptance

- None.

## Guardrails

- The deliverable is an executable named `commonmark` at the application root.
- Read Markdown from standard input and write HTML to standard output.
- Do not use a public Markdown implementation.
- Do not stage `sources/INSTRUCTIONS.md` into the application.
- Preserve supplied scoring assets unchanged.
