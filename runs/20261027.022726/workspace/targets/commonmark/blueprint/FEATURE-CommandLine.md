# FEATURE: Command Line

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Provides the root executable that converts standard-input Markdown to standard-output HTML. |
| Depends On | ARCHITECTURE.md |
| Provides | commonmark |
| Consumes | parser foundation |

## Purpose

Callers run `./commonmark` at the application root, supply a UTF-8 Markdown document on standard input, and receive its rendered HTML on standard output. The command connects block parsing, inline parsing, and HTML rendering in that order.

## Operation

Read the complete input document as UTF-8. Pass it through the parser stages and write the resulting HTML as UTF-8 to standard output. Exit zero after successful conversion. Input or processing failures produce a nonzero exit status and diagnostics on standard error. As parser capabilities are added, the same executable exposes them to the supplied conformance runner.

## Programmatic Acceptance

=== AC command-empty-input ===
Intent: The executable accepts an empty UTF-8 document and emits its empty rendered result successfully.
Requires: executable=python3; scope=test

import subprocess
import sys

source = ""
result = subprocess.run(
    ["./commonmark"], input=source, capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
assert result.stdout == source
=== END AC command-empty-input ===

## User Acceptance

- None.

## Guardrails

- The executable is named `commonmark` and is located at the application root.
- Do not use a public Markdown implementation or modify the supplied conformance assets.
