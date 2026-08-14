# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines the two-phase Python CommonMark parser architecture and runtime boundaries. |
| Depends On  | — |
| Provides    | parser architecture, block parser boundary, inline parser boundary, renderer boundary |
| Consumes    | — |

## Intent

CommonMark is a command-line parser that reads UTF-8 Markdown from standard input, parses block structure before inline structure, renders CommonMark 0.31.2 HTML, and writes the result to standard output.

## Module Boundaries

| Boundary | Responsibility |
|---|---|
| Executable entry point | Reads standard input, invokes parsing and rendering, writes standard output, and reports process failures. |
| Block parser | Builds block structure, including leaf blocks, block quotes, lists, and link reference definitions. |
| Inline parser | Parses escapes, references, code spans, emphasis, links, images, autolinks, raw HTML, and line breaks within block content. |
| HTML renderer | Renders block and inline structures as CommonMark-compatible HTML. |
| Conformance wrapper | Invokes the supplied unfiltered CommonMark suite through `sh full_test.sh`. |

The parser separates block parsing from inline parsing. Link reference definitions discovered during block parsing are available to inline parsing. The renderer consumes the completed parsed structure and does not determine block structure.

## Technology Stack

- Python 3 implements the parser, executable, and conformance integration.
- Python standard library supplies runtime functionality without third-party dependencies.
- POSIX shell provides the `full_test.sh` wrapper.

## Constraints

- The implementation does not use a public Markdown implementation.
- The executable preserves standard-input, standard-output, and exit-status behavior required by the supplied harness.
- Runtime conformance assets are limited to `spec.txt`, `spec_tests.py`, `cmark.py`, and `normalize.py`.
- `full_test.sh` runs the complete supplied suite without filtering.

## Programmatic Acceptance

=== AC architecture-boundaries ===
Intent: The implementation exposes separate block, inline, rendering, and executable boundaries.

from pathlib import Path

required = [
    Path("cmark"),
    Path("parser"),
    Path("renderer"),
]
assert all(path.exists() for path in required)
=== END AC architecture-boundaries ===

=== AC architecture-runtime-contract ===
Intent: The runtime contains the required POSIX conformance wrapper boundary.

from pathlib import Path

wrapper = Path("full_test.sh")
assert wrapper.is_file()
assert wrapper.read_text(encoding="utf-8").startswith("#!")
=== END AC architecture-runtime-contract ===

## User Acceptance

- None.

## Guardrails

- The parser does not delegate CommonMark behavior to a public Markdown implementation.
- Block parsing precedes inline parsing.
- Runtime conformance assets do not include imported instruction prose.
