# FEATURE: Executable Interface

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Provides the root `commonmark` executable for converting Markdown from standard input to HTML on standard output. |
| Depends On  | ARCHITECTURE.md |
| Provides    | `./commonmark` command |

## Purpose

Provide an executable named `commonmark` at the application root. It reads UTF-8 Markdown from standard input and writes rendered HTML to standard output. Include a concise project README describing this interface.

## Behavior

- Successful conversion exits with status 0.
- An input or conversion failure exits nonzero and reports its diagnostic on standard error.
- The executable accepts Markdown through standard input; callers do not need to pass a source file path.

## Programmatic Acceptance

=== AC cli-success ===
Intent: The root executable accepts Markdown on standard input and completes a conversion successfully.

import subprocess

source = "# heading\n"
result = subprocess.run(
    ["./commonmark"], input=source, capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
assert result.stdout
=== END AC cli-success ===

=== AC cli-empty-input ===
Intent: The root executable handles empty standard input as a successful conversion.

import subprocess

source = ""
result = subprocess.run(
    ["./commonmark"], input=source, capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
assert result.stdout == source
=== END AC cli-empty-input ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation as the parser.
- Keep all supplied conformance assets unchanged.
