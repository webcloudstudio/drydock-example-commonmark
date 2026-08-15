# ARCHITECTURE: CommonMark Parser

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Defines the executable boundary and standard-library architecture for the CommonMark parser. |
| Depends On  | — |
| Provides    | executable commonmark |
| Consumes    | — |

## Intent

The application is a command-line CommonMark 0.31.2 parser. The executable `commonmark` reads UTF-8 Markdown from standard input and writes rendered HTML to standard output.

## Boundaries

| Module | Responsibility |
|---|---|
| `commonmark` | Executable process boundary, UTF-8 stream handling, and exit status. |
| Parser implementation | Block parsing, link-reference collection, inline parsing, and HTML rendering. |
| `sources/` | Supplied immutable conformance assets used only by verification. |

Block structure is resolved before inline structure. Link-reference definitions collected during block parsing are available to inline parsing.

## Technology Stack

- Python 3 for the executable and parser.
- Python standard library only at runtime.
- POSIX shell for the supplied conformance harness.

## Technical Decisions

- Do not use a public Markdown implementation or third-party runtime dependency.
- Preserve the executable name and standard-input/standard-output contract.
- Replace U+0000 with U+FFFD according to the CommonMark specification.
- Keep supplied scoring assets unchanged.

## Programmatic Acceptance

=== AC interface-executable ===
Intent: The application root contains an executable named commonmark.

import os

path = "commonmark"
assert os.path.isfile(path)
assert os.access(path, os.X_OK)
=== END AC interface-executable ===

=== AC interface-process ===
Intent: The executable accepts standard input and terminates successfully.

import subprocess

source = "interface probe\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC interface-process ===

=== AC interface-utf8 ===
Intent: The executable accepts UTF-8 input and terminates successfully.

import subprocess

source = "UTF-8 interface probe\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC interface-utf8 ===

## User Acceptance

- None.

## Guardrails

- Do not modify supplied conformance assets.
- Do not add a public Markdown implementation as a dependency.
