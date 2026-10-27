# FEATURE: Documentation

| Field | Value |
|-------------|-------|
| Version | 20261027 V1 |
| Description | Document the command-line standard-stream interface. |
| Depends On | FEATURE-CommandLine.md |
| Consumes | commonmark |

## Purpose

Provide a concise application-root README for callers of the parser.

## Behavior

The README describes invocation of `./commonmark`, UTF-8 Markdown input on standard input, and HTML output on standard output. Include a practical standard-stream invocation.

## Programmatic Acceptance

=== AC documentation-readable ===
Intent: The application README exists and can be read as nonempty UTF-8 documentation.
Encoding: utf-8

from pathlib import Path

content = Path("README.md").read_text(encoding="utf-8")
assert len(content.strip()) > 0
=== END AC documentation-readable ===

## User Acceptance

- None.

## Guardrails

- Keep the README concise and do not modify the supplied conformance assets.
