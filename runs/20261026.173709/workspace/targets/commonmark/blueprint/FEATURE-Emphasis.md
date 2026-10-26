# FEATURE: Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses CommonMark emphasis and strong emphasis. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | emphasis and strong emphasis parsing |
| Consumes     | commonmark executable |

## Purpose

Parse emphasis and strong emphasis according to the CommonMark 0.31.2 delimiter-run algorithm.

## Behavior

- Identify delimiter runs of `*` and `_`, and determine their left- and right-flanking status using Unicode whitespace and punctuation.
- Apply the distinct opening and closing rules for `*` and `_`, including the restriction on intraword underscore emphasis.
- Match delimiters according to the rule of three, consume one delimiter for emphasis or two for strong emphasis, and leave unused delimiters as literal text.
- Resolve nesting and overlapping spans according to the specification’s ambiguity rules. Code spans, links, images, and HTML tags bind more tightly than emphasis.

## Programmatic Acceptance

=== AC emphasis-conformance ===
Intent: The executable passes every supplied emphasis and strong emphasis example.
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
        "^Emphasis and strong emphasis$",
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

- Do not replace the delimiter-run algorithm with simple delimiter pairing.
- Resolve block structure before inline structure.
- Do not modify the supplied conformance assets.
