# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20261025 V1 |
| Description | Defines the self-contained Python parser structure and command-line rendering flow. |
| Provides    | commonmark parser package structure |

## Purpose

Provide the Python project foundation for a command-line parser that converts Markdown to HTML. The parser is implemented in this project; it must not depend on a public Markdown implementation.

## Modules and flow

The parser processes a document in two phases:

1. The block parser identifies document structure and collects link reference definitions across the whole document.
2. The inline parser processes paragraph and heading content using that completed reference map. The renderer emits HTML for the resulting structure.

The `commonmark` executable reads UTF-8 Markdown from standard input, invokes the parser, and writes HTML to standard output.

## Module ownership

| Boundary | Owner | Responsibility |
|---|---|---|
| Block parsing | Block parser | Parse block structure and collect document-wide references. |
| Inline parsing | Inline parser | Parse inline syntax and resolve links using the reference map. |
| HTML rendering | Renderer | Convert parsed blocks and inlines to HTML. |
| Command-line interface | `commonmark` executable | Connect standard input and standard output to the parser. |
| Persistence, configuration, file store, external services | None | The parser has no persistent state or external service boundary. |

## Technology Stack

- Python 3 implements the parser and executable.
- Python standard library provides runtime support; no third-party runtime dependency is required.
- POSIX shell is used by the supplied conformance entry point.

## Programmatic Acceptance

=== AC parser-package-imports ===
Intent: The project exposes an importable Python package for the parser foundation.

import importlib.util

spec = importlib.util.find_spec("commonmark")
assert spec is not None
assert spec.submodule_search_locations is not None
=== END AC parser-package-imports ===

=== AC parser-foundation-tests ===
Intent: The foundation's declared pytest test command runs successfully.

import subprocess

result = subprocess.run(["pytest", "-q"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC parser-foundation-tests ===

## User Acceptance

- None.

## Guardrails

- Keep the implementation self-contained; do not use a public Markdown implementation.
- Keep the supplied conformance assets read-only and stage them verbatim.
- Do not modify `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, or `sources/spec.txt`.
