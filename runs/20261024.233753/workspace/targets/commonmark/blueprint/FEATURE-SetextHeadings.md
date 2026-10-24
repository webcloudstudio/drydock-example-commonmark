# FEATURE: Setext Headings

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses multiline setext headings and their underlines into HTML. |
| Depends On  | ARCHITECTURE.md |
| Provides    | setext headings |

## Purpose

Implement level-one and level-two setext headings from paragraph lines followed by a valid underline.

## Behavior

- Recognize an underline made only of `=` or only of `-`, with up to three leading spaces and optional trailing spaces or tabs.
- Form a heading from one or more eligible paragraph lines followed by the underline; concatenate the lines and trim initial and final spaces or tabs before inline parsing.
- Do not form an empty heading. A line that would start another block construct cannot serve as setext heading text.
- Resolve an eligible dash underline as a setext heading when it follows paragraph content; otherwise preserve thematic-break precedence.

## Programmatic Acceptance

=== AC setext-heading-conformance ===
Intent: The parser passes every supplied Setext headings example.
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
        "--pattern", r"^Setext headings$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC setext-heading-conformance ===

## User Acceptance

- None.

## Guardrails

- A setext heading cannot interrupt a paragraph; paragraph text preceding the underline becomes the heading content.
- A dash-only line interpreted as a thematic break does not become an empty setext heading.
- A possible setext underline in a lazy continuation line of a list item or block quote does not create a setext heading.
