# FEATURE: Standard-stream Executable

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Exposes the CommonMark parser as a root executable using standard streams. |
| Depends On | ARCHITECTURE.md |
| Provides | commonmark |
| Consumes | Python project foundation |

## Workflow

Run `./commonmark` from the application root. It reads a complete UTF-8 Markdown document from standard input, passes it to `commonmark_parser.render`, and writes the returned HTML to standard output. Successful conversion exits zero. Operational errors exit nonzero and use standard error.

Provide a concise project `README.md` describing the standard-input and standard-output interface. The executable must be usable as the program argument to the supplied conformance runner. Parser conformance is established by later stories.

## Programmatic Acceptance

=== AC executable-empty-document ===
Intent: The root executable accepts an empty UTF-8 document and completes successfully through the standard-stream interface.
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    ["./commonmark"], input="", capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC executable-empty-document ===

## User Acceptance

- None.

## Guardrails

- Preserve stdin and stdout as the conversion interface.
- Do not use a public Markdown implementation.
- Keep supplied conformance assets unchanged.
