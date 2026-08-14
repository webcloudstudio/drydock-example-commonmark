# FEATURE: Inline Escapes and Character References

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines CommonMark punctuation escapes and named and numeric character references. |
| Depends On  | FEATURE-BLOCK-LISTS.md |
| Provides    | escape parser, character reference parser |
| Consumes    | block parser |

## Programmatic Acceptance

Requires: executable=python3; scope=test

=== AC inline-escapes ===
Intent: The implementation passes punctuation escape and escape-context conformance examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Backslash escapes)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-escapes ===

=== AC character-references ===
Intent: The implementation passes named, decimal, hexadecimal, invalid, and contextual character-reference examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Entity and numeric character references)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC character-references ===

## User Acceptance

- None.

## Guardrails

- U+0000 is replaced with U+FFFD.
- Escapes and references do not replace structural block markers.
