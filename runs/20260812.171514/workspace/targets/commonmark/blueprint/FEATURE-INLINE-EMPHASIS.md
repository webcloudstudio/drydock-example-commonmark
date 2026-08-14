# FEATURE: Emphasis and Strong Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines CommonMark delimiter-run parsing for emphasis and strong emphasis. |
| Depends On  | FEATURE-INLINE-CODE-BREAKS.md |
| Provides    | emphasis parser, strong emphasis parser |
| Consumes    | block parser, code span parser |

## Programmatic Acceptance

Requires: executable=python3; scope=test

=== AC emphasis-delimiters ===
Intent: The implementation passes delimiter-run, flanking, intraword, and modulo-three emphasis examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Emphasis and strong emphasis)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC emphasis-delimiters ===

=== AC emphasis-nesting ===
Intent: The implementation passes nested, overlapping, precedence, and unmatched delimiter examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Emphasis and strong emphasis)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC emphasis-nesting ===

## User Acceptance

- None.

## Guardrails

- Intraword underscore emphasis is prohibited according to CommonMark delimiter rules.
- Code spans, links, images, and HTML tags retain precedence over emphasis parsing.
