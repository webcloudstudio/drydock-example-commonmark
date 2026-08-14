# FEATURE: CLI Errors

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines deterministic process failure behavior for the parser executable. |
| Depends On  | FEATURE-CLI-ENTRYPOINT.md |
| Provides    | parser error behavior |
| Consumes    | parser executable |

## Operational Behavior

Operational failures produce a nonzero exit status. Diagnostics are written to standard error, and standard output remains empty when processing cannot complete. Successful input processing continues to use the standard-input and standard-output contract defined by `FEATURE-CLI-ENTRYPOINT.md`.

## Programmatic Acceptance

=== AC cli-errors-success-contract ===
Intent: A successful invocation returns zero and keeps diagnostics off standard error.

import subprocess

result = subprocess.run(
    ["./cmark"],
    input="plain text\n",
    capture_output=True,
    text=True,
    encoding="utf-8",
)
assert result.returncode == 0
assert result.stdout == "<p>plain text</p>\n"
assert result.stderr == ""
=== END AC cli-errors-success-contract ===

=== AC cli-errors-stdout-integrity ===
Intent: The executable emits a complete HTML document result without diagnostic text in standard output.

import subprocess

result = subprocess.run(
    ["./cmark"],
    input="a\n\nb\n",
    capture_output=True,
    text=True,
    encoding="utf-8",
)
assert result.returncode == 0
assert result.stdout == "<p>a</p>\n<p>b</p>\n"
assert "error" not in result.stdout.lower()
=== END AC cli-errors-stdout-integrity ===

## User Acceptance

- None.

## Guardrails

- Failure diagnostics never replace rendered output on standard output.
- Error handling does not alter the conformance harness invocation contract.
- Acceptance does not depend on diagnostic wording.
