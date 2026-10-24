# FEATURE: Complete Conformance Verification

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Verifies the completed parser against the complete supplied conformance suite. |
| Depends On  | ARCHITECTURE.md |
| Provides    | complete CommonMark conformance verification |
| Consumes    | commonmark |

## Purpose

Run the sole terminal verification for CommonMark 0.31.2 after all parser stories are complete.

## Programmatic Acceptance

=== AC full-commonmark-conformance ===
Intent: The supplied full conformance harness succeeds.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC full-commonmark-conformance ===

## User Acceptance

- None.

## Guardrails

- Run only after all parser implementation stories have closed.
- Do not modify or replace any supplied scoring asset.
- The complete harness uses the root executable `./commonmark`.
- Do not run this complete-suite check from implementation stories.
