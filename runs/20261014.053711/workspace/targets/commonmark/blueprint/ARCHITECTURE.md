# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Two-phase CommonMark 0.31.2 parser delivered as the stdin-to-stdout executable commonmark, with its module layout and technical decisions. |
| Depends On  | None |
| Provides    | mdparser package, mdparser.blocks, mdparser.inlines, mdparser.refs, mdparser.entities, mdparser.render, mdparser.cli |
| Consumes    | None |

## Overview

The product is a single-process CLI. `./commonmark` reads UTF-8 Markdown from stdin and writes HTML to stdout. It is implemented in the Python package `mdparser` and follows the spec Appendix "A parsing strategy" directly.

- **Phase 1, block structure.** Lines are consumed one at a time. Each line is matched against the open blocks, then new block starts are looked for, then remaining text is added to the deepest open block. Link reference definitions are extracted when a paragraph closes and stored in one document-wide reference map.
- **Phase 2, inline structure.** The finished tree is walked. The raw text of paragraphs and headings is parsed into inlines with the delimiter-stack algorithms (look for link or image, process emphasis), using the reference map.
- **Rendering.** A renderer turns the tree into HTML. The conformance runner compares normalized HTML, so tag structure, entities and URL percent-encoding must match the spec examples.

## Technology Stack

Derived from `TECHNOLOGY_STACK.md`, which remains the decision of record.

| Technology | Where it applies |
|---|---|
| Python 3 | Implementation language for the whole package and the `commonmark` script. |
| Python standard library | The only runtime dependency set: `re`, `unicodedata`, `html.entities`, `sys`. |
| POSIX shell | The supplied `sources/full_test.sh` scoring entry point; it is staged, never authored. |

The Foundation Contract is: source root `./`, environment `.venv` created by `uv venv`, dependencies in `pyproject.toml` with a committed `uv.lock`, and `pytest -q` as the test command. The executable must also run under plain `python3` with no environment activated, because the supplied harness runs `./commonmark` directly.

## Modules

| Module | Responsibility |
|---|---|
| `commonmark` (root script) | Shebang entry point; puts its own directory on `sys.path` and calls `mdparser.cli.main`. |
| `mdparser.cli` | Byte intake, UTF-8 decoding with replacement, line-ending normalization, U+0000 replacement, output writing. |
| `mdparser.blocks` | Block tree, block-type registry (start, continue, close rules), per-line procedure, lazy continuation. |
| `mdparser.refs` | Reference map, link reference definition extraction, `normalize_label`. |
| `mdparser.inlines` | Inline scanner, delimiter stack, `process_emphasis`, look-for-link-or-image. |
| `mdparser.entities` | Entity and numeric character reference decoding, backslash unescape helper. |
| `mdparser.render` | HTML rendering, HTML escaping, URL percent-encoding. |

## Technical Decisions

- Named entities come from the standard library table `html.entities.html5`; only names ending in a semicolon are recognized.
- Label matching uses `str.casefold()` plus whitespace collapse.
- Unicode punctuation for flanking rules is classified with `unicodedata` general categories `P*` and `S*`.
- Soft line breaks render as a line ending.
- No public Markdown implementation is used or imported.
- Exit status is 0 for every input. Invalid UTF-8 is decoded with U+FFFD replacement. Diagnostics go to stderr only.

## Persistence, Configuration and Boundaries

| Boundary | Owner module | Allowed low-level APIs |
|---|---|---|
| Persistence | None. The product is stateless. | None |
| Configuration | None. No arguments or environment are required. | None |
| File store | None. | None |
| External services | None. | None |
| Process I/O | `mdparser.cli` | `sys.stdin.buffer`, `sys.stdout.buffer`, `sys.stderr` |

## Programmatic Acceptance

=== AC foundation-package-imports ===
Intent: The mdparser package and each reserved module import cleanly using only the standard library.

import importlib
import os
import sys

sys.path.insert(0, os.getcwd())

importlib.import_module("mdparser")
for name in ["blocks", "inlines", "refs", "entities", "render", "cli"]:
    full = "mdparser." + name
    module = importlib.import_module(full)
    assert module.__name__ == full
=== END AC foundation-package-imports ===

## User Acceptance

- None.

## Guardrails

- Never use or import a public Markdown implementation.
- Never add a third-party runtime dependency.
- Never write to `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, or `sources/spec.txt`.
- Nothing but rendered HTML is ever written to stdout.
