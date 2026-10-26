# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Defines the Python project foundation and parser module boundary. |
| Provides    | commonmark_core |

## Purpose

CommonMark is a command-line Markdown-to-HTML parser conforming to CommonMark 0.31.2. The parser resolves block structure before inline structure and makes document-wide link reference definitions available to inline parsing.

## Modules and boundaries

The `commonmark_core` package owns parsing and rendering logic. The root-level `commonmark` executable owns the command-line boundary: it reads UTF-8 Markdown from standard input, calls the parser package, and writes HTML to standard output.

Keep block parsing, document-wide reference collection, inline parsing, and HTML rendering behind the package boundary. The executable must not contain a separate parser implementation.

| Boundary | Owner | Allowed access |
|---|---|---|
| Markdown parsing and rendering | `commonmark_core` | Parser modules and standard library |
| Standard input/output | `commonmark` executable | Calls the public `commonmark_core` interface |
| Persistent storage | None | The parser has no persistent state |
| Configuration | None | No configuration contract is defined |
| File storage | None | Input is supplied through standard input |
| External services | None | No external service calls |

## Technology Stack

- Python 3 implements the parser package and executable.
- Python standard library provides runtime functionality without third-party runtime dependencies.
- POSIX shell runs the supplied complete conformance harness.

The project root is `./`. The environment is `.venv`, created with `uv venv` and activated by launchers in `bin/`. The project uses `pyproject.toml`, the committed `uv.lock`, and `pytest -q` as its test command.

## Programmatic Acceptance

=== AC foundation-package-imports ===
Intent: The parser package is importable from the project root.

import importlib.util

assert importlib.util.find_spec("commonmark_core") is not None
=== END AC foundation-package-imports ===

=== AC foundation-tests-run ===
Intent: The Python test command runs successfully after the foundation is established.

import subprocess

result = subprocess.run(
    ["pytest", "-q"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC foundation-tests-run ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep the supplied scoring assets unchanged.
- Do not invoke the complete scoring harness from scoped parser checks.
