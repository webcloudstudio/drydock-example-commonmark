# FEATURE: Block References

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Collect valid document-wide CommonMark link reference definitions for later inline resolution. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leaves.md |
| Provides    | document-wide link reference definition map |
| Consumes    | leaf blocks, normalized UTF-8 input lines |

## Link Reference Definitions

Reference definitions are detected while block content is closed. Valid labels are normalized by stripping boundary whitespace, collapsing internal spaces and line endings, and applying Unicode case folding. The first valid definition for a normalized label wins.

Definitions may contain escaped characters, angle-bracket destinations, titles, and permitted multiline content. Definitions inside block containers populate the document-wide map. Invalid definitions remain visible paragraph content.

## Programmatic Acceptance

=== AC block-references-valid ===
Intent: The implementation passes the complete valid link-reference-definition conformance coverage.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^Link reference definitions$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-references-valid ===

=== AC block-references-container ===
Intent: The implementation passes reference-definition cases involving document-wide and container-scoped definitions.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--number", 999999],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-references-container ===

## User Acceptance

- None.

## Guardrails

- Preserve first-definition precedence.
- Invalid definitions must remain visible content.
- Reference definitions must affect the entire document, including definitions inside containers.
- Do not invoke `full_test.sh` from scoped checks.
