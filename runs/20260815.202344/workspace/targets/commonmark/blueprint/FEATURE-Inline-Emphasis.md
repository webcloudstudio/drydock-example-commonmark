# FEATURE: Inline Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse CommonMark emphasis and strong emphasis using the delimiter-run algorithm. |
| Depends On  | ARCHITECTURE.md, FEATURE-Inline-Basics.md |
| Provides    | emphasis parsing, strong-emphasis parsing |
| Consumes    | executable commonmark, block structure, inline basics |

## Purpose

Implement emphasis and strong emphasis after block parsing and basic inline tokenization.

## Behavior

- Apply the CommonMark delimiter-run algorithm for `*`, `_`, `**`, and `__`.
- Enforce intraword, Unicode whitespace, Unicode punctuation, and multiple-of-three rules.
- Support nested emphasis, strong emphasis, unmatched delimiters, and precedence with code spans, links, images, and HTML.
- Render emphasis as `<em>` and strong emphasis as `<strong>`.

## Programmatic Acceptance

=== AC emphasis-conformance ===
Intent: The implementation passes every supplied conformance example owned by emphasis and strong emphasis.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        "./commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        r"^Emphasis and strong emphasis$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC emphasis-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Preserve block-before-inline parsing.
- Do not modify supplied conformance assets.
