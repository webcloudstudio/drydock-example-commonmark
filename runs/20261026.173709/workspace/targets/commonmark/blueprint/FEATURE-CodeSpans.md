# FEATURE: Code Spans

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses CommonMark code spans in inline content. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | code span parsing |
| Consumes    | commonmark executable |

## Purpose

Parse inline code spans according to CommonMark 0.31.2. Code span parsing runs after block structure is resolved and before other inline formatting is applied.

## Behavior

- A backtick string is a run of one or more backticks not adjacent to another backtick.
- A code span opens with a backtick string and closes at the next backtick string of equal length. Unmatched runs remain literal text.
- Convert line endings inside the span to spaces. If the resulting content begins and ends with U+0020 and is not entirely spaces, remove exactly one space from each end.
- Preserve all other content literally, including backslashes, character references, and Markdown markers. Escape the resulting content for HTML inside `<code>`.

## Programmatic Acceptance

=== AC code-spans-conformance ===
Intent: The executable passes every supplied code span example.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
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
        "^Code spans$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC code-spans-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not parse code span contents as escapes, character references, or other inline syntax.
- Do not modify the supplied conformance assets.
- Resolve block structure before inline structure.
