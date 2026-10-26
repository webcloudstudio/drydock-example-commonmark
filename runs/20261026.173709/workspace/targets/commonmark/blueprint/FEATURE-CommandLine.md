# FEATURE: Command Line

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Provides the root-level executable for standard input and output parsing. |
| Depends On  | ARCHITECTURE.md |
| Provides    | commonmark executable |
| Consumes    | commonmark_core |

## Purpose

Deliver an executable named `commonmark` at the application root. It reads UTF-8 Markdown from standard input, invokes `commonmark_core`, and writes rendered HTML to standard output. It must be usable as a program by the supplied conformance runner.

## Workflow

1. Read the complete Markdown document from standard input as UTF-8.
2. Pass the document to the `commonmark_core` parser and renderer.
3. Write the rendered HTML to standard output.

Create a concise project `README.md` describing this standard input/output interface.

## Programmatic Acceptance

=== AC cli-executable-interface ===
Intent: The root executable accepts Markdown on standard input and completes successfully.

import subprocess

payload = "CommonMark command interface\n"
result = subprocess.run(
    ["./commonmark"],
    input=payload,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC cli-executable-interface ===

=== AC cli-empty-input-interface ===
Intent: The executable accepts an empty UTF-8 document and completes successfully.

import subprocess

result = subprocess.run(
    ["./commonmark"],
    input="",
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC cli-empty-input-interface ===

## User Acceptance

- None.

## Guardrails

- The executable must be located at the application root and read UTF-8 Markdown from standard input.
- Write rendered HTML to standard output.
- Do not use a public Markdown implementation.
- Do not modify or replace supplied scoring assets.
- The complete scoring command is `sh sources/full_test.sh`; only the terminal verification story runs it.
