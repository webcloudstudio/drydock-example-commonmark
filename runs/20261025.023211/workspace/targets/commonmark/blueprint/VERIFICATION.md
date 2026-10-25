# FEATURE: Verification

| Field       | Value |
|-------------|-------|
| Version     | 20261025 V1 |
| Description | Verifies the completed parser with the supplied full CommonMark conformance suite. |
| Depends On  | FEATURE-Block-Parsing.md, FEATURE-Inline-Parsing.md, FEATURE-Executable.md |
| Provides    | full conformance verification |

## Purpose

Run the supplied unfiltered CommonMark 0.31.2 suite after the parser and executable are complete.

## Verification

The sole whole-suite check is `sh sources/full_test.sh`. It runs from the application root, invokes the staged runner against `./commonmark`, and reports the suite result. This story depends on every parser implementation story.

## Programmatic Acceptance

=== AC full-commonmark-suite ===
Intent: The supplied full CommonMark conformance suite completes successfully.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC full-commonmark-suite ===

## User Acceptance

- None.

## Guardrails

- Stage `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, and `sources/spec.txt` verbatim.
- Do not modify any supplied scoring asset.
- Do not invoke the full harness from scoped checks.
