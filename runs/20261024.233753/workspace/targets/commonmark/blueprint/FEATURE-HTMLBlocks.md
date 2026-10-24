# FEATURE: HTML Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Recognizes CommonMark HTML block types and passes their source through as raw HTML. |
| Depends On  | ARCHITECTURE.md |
| Provides    | HTML blocks |

## Purpose

Implement all seven CommonMark HTML block types, preserving their source text and stopping at the appropriate end condition.

## Behavior

- Recognize start conditions after up to three spaces of indentation.
- For types one through five, continue through the matching end condition, or to the end of the containing block or document.
- For type six, continue until a blank line. For type seven, recognize complete open or closing tags on a line and continue until a blank line.
- Permit types one through six to interrupt paragraphs; type seven cannot interrupt a paragraph.
- Pass block contents through without inline parsing or escaping.

## Programmatic Acceptance

=== AC html-block-conformance ===
Intent: The parser passes every supplied HTML blocks example.
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
        "--pattern", r"^HTML blocks$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC html-block-conformance ===

## User Acceptance

- None.

## Guardrails

- HTML inside a raw HTML block is passed through verbatim, including content that resembles other block syntax.
- Do not extend HTML block termination rules across container boundaries.
- Do not classify an inline HTML tag in the middle of paragraph text as a type seven block.
