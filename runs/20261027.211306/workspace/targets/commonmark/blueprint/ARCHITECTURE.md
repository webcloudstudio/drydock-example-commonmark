# ARCHITECTURE: CommonMark Parser

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Defines the Python project and the boundaries of the CommonMark parsing pipeline. |
| Provides | Python project foundation |

## Structure and interfaces

The application root owns the Python project, `pyproject.toml`, committed `uv.lock`, the `.venv` environment created by `uv venv`, launchers in `bin/`, and the `pytest -q` test runner. Runtime code uses Python 3 and the standard library only.

Provide a `commonmark_parser` package with these integration interfaces:

- `commonmark_parser.render(markdown: str) -> str` accepts a complete document and returns HTML. The foundation supplies a callable integration point without claiming conformance.
- `commonmark_parser.blocks.parse_blocks(markdown: str) -> Document` produces a document tree. A `Document` has an ordered `children` sequence and a document-wide `references` mapping. Block nodes expose `kind`, `children`, and `literal`; headings also expose `level`.
- `commonmark_parser.inlines.parse_inlines(literal: str, references: dict) -> list` consumes raw paragraph or heading content and the completed reference map.

The block parser consumes lines in document order, maintains open container and leaf blocks, and collects reference definitions when paragraphs close. After the complete block tree and reference map exist, inline parsing processes the raw content of paragraphs and headings. Rendering walks the resulting structure to produce HTML. Preserve raw inline source until the inline phase. The later parser stories extend these interfaces.

Stage the supplied `spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh` verbatim under `sources/`. The runner imports its sibling helpers and accepts the candidate program and specification paths. `sources/INSTRUCTIONS.md` is planning context and is not a runtime asset.

## Technology Stack

Python 3 implements the parser and executable. The Python standard library supplies runtime facilities without third-party runtime dependencies. POSIX shell runs the supplied full-suite entry point.

## Boundary ownership

| Boundary | Owner | Access |
|----------|-------|--------|
| Standard streams and process entry point | Root executable | Reads stdin and writes stdout through the parser integration interface. |
| Block tree and document references | `commonmark_parser.blocks` | Owns block construction and the document reference map. |
| Inline parsing and rendering | `commonmark_parser.inlines` and `commonmark_parser` | Consume completed block contents and references; render HTML. |
| Conformance assets | `sources/` | Read-only supplied files; the runner invokes the root executable. |
| Persistence, configuration, external services | None | No persistent store or external service is required. |

## Programmatic Acceptance

=== AC foundation-integration ===
Intent: The Python foundation exposes the parser integration callable before parser features are implemented.

import commonmark_parser

assert callable(commonmark_parser.render)
=== END AC foundation-integration ===

=== AC foundation-block-boundary ===
Intent: The foundation exposes a callable block parser for later block capabilities.

from commonmark_parser.blocks import parse_blocks

assert callable(parse_blocks)
=== END AC foundation-block-boundary ===

=== AC foundation-inline-boundary ===
Intent: The foundation exposes a callable inline parser for the second parsing phase.

from commonmark_parser.inlines import parse_inlines

assert callable(parse_inlines)
=== END AC foundation-inline-boundary ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep the supplied conformance assets unchanged and stage the five runtime assets verbatim.
- Do not invoke the full-suite entry point from scoped implementation checks.
- Do not add file-presence checks or additional verification stories.
