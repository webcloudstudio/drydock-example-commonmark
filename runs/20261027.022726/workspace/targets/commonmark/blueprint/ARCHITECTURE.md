# ARCHITECTURE: CommonMark Parser Foundation

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Establishes the Python project and the interfaces for the two-phase CommonMark parser. |
| Provides | parser foundation |

## Purpose

Provide the project tree, Python environment, dependency manifest, lockfile, test runner, and shared parser interfaces. The application processes a UTF-8 document into HTML without a public Markdown implementation.

## Technology Stack

Python 3 and its standard library implement the parser and its tests. POSIX shell supports the supplied full-suite entry point. The project uses `.venv`, created by `uv venv`, launchers in `bin/`, `pyproject.toml`, a committed `uv.lock`, and `pytest -q` as the project test command.

## Parser Interfaces

The foundation publishes a `commonmark_parser` package with these interfaces:

- `parse_blocks(markdown: str) -> Document` constructs the document's block tree and collects reference definitions.
- `parse_inlines(document: Document) -> Document` parses the raw inline content of paragraphs and headings using the completed document-wide reference map.
- `render_html(document: Document) -> str` renders the resulting document as HTML.

`Document` holds the block tree and the reference-definition map. Block nodes retain their type, children, and raw content as needed by later stories. Reference definitions collected anywhere in the document are available throughout inline parsing. Block structure takes precedence over inline structure; callers complete block parsing before inline parsing.

The foundation establishes these callable boundaries and an empty-document path. Later stories implement the syntax families and their rendering.

## Boundary Ownership

| Boundary | Owner | Access |
|----------|-------|--------|
| Block tree and reference map | `commonmark_parser` | Parser stages share the document object. |
| Inline parsing and HTML rendering | `commonmark_parser` | The command invokes the published stage interfaces. |
| Standard streams | Command-line entry point | Reads stdin and writes stdout. |
| Persistence, configuration, file stores, and external services | None | No persistent store or external service is required. |

## Programmatic Acceptance

=== AC foundation-empty-document ===
Intent: The published parser stages accept an empty document in the required order and render it without content.

from commonmark_parser import parse_blocks, parse_inlines, render_html

source = ""
document = parse_blocks(source)
document = parse_inlines(document)
assert render_html(document) == source
=== END AC foundation-empty-document ===

## User Acceptance

- None.

## Guardrails

- Use no public Markdown implementation or third-party runtime dependency.
- Keep the supplied specification, conformance harness, normalizer, and reference wrapper read-only.
- Preserve block-before-inline processing and make collected definitions available to inline parsing.
