# FEATURE: Executable

| Field       | Value |
|-------------|-------|
| Version     | 20261025 V1 |
| Description | Provides the root `commonmark` executable for standard-input to standard-output conversion. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Parsing.md, FEATURE-Inline-Parsing.md |
| Provides    | commonmark |
| Consumes    | block parser, inline parser |

## Purpose

Provide an executable named `commonmark` at the application root. It reads UTF-8 Markdown from standard input and writes converted HTML to standard output.

## Behavior

On successful conversion, exit with status zero. On input or execution errors, exit nonzero and report the error on standard error. The supplied harness invokes the executable from the application root.

## Programmatic Acceptance

=== AC executable-stdin-stdout ===
Intent: The root executable accepts Markdown on standard input and emits converted output on standard output.

import subprocess

source = "ordinary text\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stderr)
assert result.returncode == 0
assert result.stdout
=== END AC executable-stdin-stdout ===

=== AC executable-errors ===
Intent: Invalid UTF-8 input is reported as an unsuccessful process invocation.

import subprocess

result = subprocess.run(
    ["./commonmark"],
    input=b"\xff",
    capture_output=True,
)
print(result.stderr.decode("utf-8", errors="replace"))
assert result.returncode != 0
=== END AC executable-errors ===

## User Acceptance

- None.

## Guardrails

- Keep the supplied conformance assets read-only and stage them verbatim.
- Do not modify `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, or `sources/spec.txt`.
