# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Standalone Python architecture for a two-phase CommonMark 0.31.2 Markdown-to-HTML parser. |
| Depends On  | — |
| Provides    | parser architecture, block parser boundary, inline parser boundary, renderer boundary |
| Consumes    | — |

## Intent

The application is a standalone command-line parser. It reads UTF-8 Markdown from standard input and writes CommonMark-compatible HTML to standard output without using a public Markdown implementation.

## Architecture

Parsing proceeds in two phases:

1. Input preprocessing creates normalized Unicode lines while preserving required tabs and replacing U+0000 with U+FFFD.
2. Block parsing constructs the document structure and collects document-wide link reference definitions.
3. Inline parsing resolves paragraph and heading content after block parsing completes.
4. Rendering converts the completed block and inline tree to HTML.
5. The executable owns only process I/O, error propagation, and the stdin/stdout contract.

Recommended module boundaries:

| Module boundary | Ownership |
|---|---|
| Input normalization | Unicode preprocessing, line endings, blank lines, indentation columns |
| Block parser | Leaf blocks, containers, lists, and block tree construction |
| Reference collector | Link-reference definition detection and normalized lookup |
| Inline parser | Escapes, references, code spans, emphasis, links, images, autolinks, and raw HTML |
| Renderer | HTML escaping, attributes, URLs, block and inline serialization |
| Executable | UTF-8 stdin, HTML stdout, process exit behavior |

The block tree is the interface between block and inline parsing. Reference definitions are collected during block parsing and supplied to inline parsing. Renderer inputs are completed block and inline nodes, including list tightness and raw HTML nodes.

## Module Ownership

| Concern | Owning boundary | Allowed responsibilities |
|---|---|---|
| Input and Unicode | Input normalization | Decode stdin, normalize line endings, replace insecure characters |
| Block structure | Block parser | Recognize and nest block nodes; do not parse inline emphasis |
| References | Reference collector | Parse definitions and expose normalized document-wide lookup |
| Inline structure | Inline parser | Parse raw inline content using the reference map |
| HTML output | Renderer | Escape text and attributes and serialize nodes |
| Process contract | Executable | Connect stdin/stdout to the parser and renderer |

No module may call a public Markdown implementation. The executable must remain usable by the supplied `cmark.py` adapter.

## Technology Stack

| Technology | Use |
|---|---|
| Python 3 | Parser, renderer, executable, and standard-library tests |
| Python standard library | Unicode, HTML escaping, URL handling, and process support |
| POSIX shell | Terminal `full_test.sh` wrapper |

## Programmatic Acceptance

=== AC architecture-input-boundary ===
Intent: The implementation exposes an input-normalization boundary that accepts text input.
import importlib

module = importlib.import_module("commonmark")
assert callable(getattr(module, "parse", None))
=== END AC architecture-input-boundary ===

=== AC architecture-render-boundary ===
Intent: The implementation exposes a rendering boundary that accepts a parsed document.
import importlib

module = importlib.import_module("commonmark")
assert callable(getattr(module, "render", None))
=== END AC architecture-render-boundary ===

=== AC architecture-cli-boundary ===
Intent: The executable module exposes a callable process entry point.
import importlib

module = importlib.import_module("commonmark")
assert callable(getattr(module, "main", None))
=== END AC architecture-cli-boundary ===

## User Acceptance

- None.

## Guardrails

- Do not depend on a public Markdown implementation.
- Preserve block-before-inline parsing.
- Preserve the standard-input/standard-output executable contract.
- Keep module ownership boundaries explicit so later stories extend rather than replace the architecture.
