# FEATURE: Inline Code Spans and Line Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines CommonMark code span normalization and hard and soft line break parsing. |
| Depends On  | FEATURE-BLOCK-LISTS.md |
| Provides    | code span parser, hard break parser, soft break parser |
| Consumes    | block parser |

## Programmatic Acceptance

Requires: executable=python3; scope=test

=== AC code-spans ===
Intent: The implementation passes code span delimiter, matching, normalization, and precedence examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Code spans)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC code-spans ===

=== AC line-breaks ===
Intent: The implementation passes hard-break, soft-break, trailing-space, and break-context examples.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./program", "--pattern", r"^(Hard line breaks|Soft line breaks)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC line-breaks ===

## User Acceptance

- None.

## Guardrails

- Hard breaks are not generated at the end of a block.
- Code spans treat their contents literally and do not parse escapes or references.
