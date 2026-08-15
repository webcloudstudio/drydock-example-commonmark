# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse nested CommonMark block quotes with markers, laziness, blank lines, and contained blocks. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leaves.md, FEATURE-Block-References.md |
| Provides    | block quote nodes |
| Consumes    | leaf blocks, document-wide link reference definition map |

## Block Quote Behavior

Recognize block quote markers with up to three spaces of indentation and optional following space or tab. Support empty quotes, nested quotes, lazy paragraph continuation, initial and final blank lines, and separation by blank lines.

Block quotes may contain every supported block form. Marker consumption must occur before child block recognition, and lazy continuation must not incorrectly absorb lines that begin a new block outside the quote.

## Programmatic Acceptance

=== AC block-quotes-conformance ===
Intent: The implementation passes the complete Block quotes conformance section.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^Block quotes$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes-conformance ===

=== AC block-quotes-nesting ===
Intent: The implementation passes nested and lazy block-quote examples within the authoritative section.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^Block quotes$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes-nesting ===

## User Acceptance

- None.

## Guardrails

- Support arbitrary nesting without changing the stdin/stdout contract.
- Apply laziness only to paragraph continuation text.
- Preserve blank-line separation between consecutive block quotes.
- Do not invoke `full_test.sh` from scoped checks.
