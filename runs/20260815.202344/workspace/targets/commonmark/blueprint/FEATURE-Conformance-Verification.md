# FEATURE: Conformance Verification

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Verify the completed parser against the complete supplied CommonMark 0.31.2 conformance suite. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leafs.md, FEATURE-Block-Quotes.md, FEATURE-Block-Lists.md, FEATURE-Inline-Basics.md, FEATURE-Inline-Emphasis.md, FEATURE-Inline-Links-Images.md, FEATURE-Inline-HTML-Autolinks.md |
| Provides    | complete CommonMark conformance verification |
| Consumes    | executable commonmark, all parser capabilities |

## Purpose

Provide the terminal verification step for the completed command-line parser.

## Behavior

- Stage `spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh` unchanged.
- Run `sh sources/full_test.sh` from the completed application root.
- Treat the supplied scoring entry point's exit status as the verification result.
- Keep the suite unfiltered and terminal.

## Programmatic Acceptance

=== AC complete-conformance ===
Intent: The completed parser passes the complete unfiltered supplied CommonMark conformance suite.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC complete-conformance ===

## User Acceptance

- None.

## Guardrails

- This is the only full-suite acceptance check.
- Do not filter, skip, reinterpret, or modify the supplied scoring assets.
- Do not modify the supplied scoring entry point.
