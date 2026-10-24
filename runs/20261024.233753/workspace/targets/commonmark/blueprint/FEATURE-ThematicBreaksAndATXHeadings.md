# FEATURE: Thematic Breaks and ATX Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark thematic breaks and ATX headings into HTML. |
| Depends On  | ARCHITECTURE.md |
| Provides    | thematic breaks, ATX headings |

## Purpose

Implement thematic breaks and ATX headings as CommonMark 0.31.2 block constructs. Block structure takes precedence over inline syntax; heading contents are parsed by the inline parser.

## Behavior

- Recognize thematic breaks with up to three leading spaces and at least three matching `-`, `_`, or `*` markers, allowing spaces or tabs between markers and at the end.
- Recognize ATX headings with one through six opening `#` markers, up to three leading spaces, and the required whitespace or end-of-line after the opening sequence.
- Strip leading and trailing spaces or tabs from heading content and discard a valid optional closing sequence of unescaped `#` markers.
- Keep invalid heading candidates as paragraph content and render all recognized blocks using the CommonMark HTML forms.

## Programmatic Acceptance

=== AC thematic-breaks-atx-conformance ===
Intent: The parser passes every supplied Thematic breaks and ATX headings example.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^(Thematic breaks|ATX headings)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC thematic-breaks-atx-conformance ===

## User Acceptance

- None.

## Guardrails

- Preserve the exact distinction between a thematic break and a list marker where both appear possible; thematic breaks take precedence.
- A setext underline that can also be read as a thematic break is handled by setext-heading precedence.
- Do not treat escaped opening `#` markers as ATX headings.
