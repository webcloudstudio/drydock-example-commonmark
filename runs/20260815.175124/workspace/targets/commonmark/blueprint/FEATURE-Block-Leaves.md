# FEATURE: Block Leaves

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse CommonMark leaf blocks and preserve their structural content for rendering. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Input.md |
| Provides    | thematic breaks, ATX headings, setext headings, paragraphs, indented code blocks, fenced code blocks, HTML blocks |
| Consumes    | normalized UTF-8 input lines, parser architecture |

## Leaf Blocks

Implement the leaf-block forms defined by CommonMark 0.31.2:

- thematic breaks;
- ATX and setext headings;
- paragraphs;
- indented code blocks;
- fenced code blocks with optional language info;
- raw HTML blocks.

Block recognition precedes inline parsing. Code contents remain literal, HTML blocks remain raw, and paragraph or heading contents are retained as raw inline input for later phases.

## Programmatic Acceptance

=== AC block-leaves-basic ===
Intent: The implementation passes thematic-break, ATX-heading, and setext-heading conformance sections.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark",
     "--pattern", r"^(Thematic breaks|ATX headings|Setext headings)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-leaves-basic ===

=== AC block-leaves-code ===
Intent: The implementation passes indented-code and fenced-code conformance sections.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark",
     "--pattern", r"^(Indented code blocks|Fenced code blocks)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-leaves-code ===

=== AC block-leaves-html ===
Intent: The implementation passes the complete HTML-block conformance section.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^HTML blocks$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-leaves-html ===

## User Acceptance

- None.

## Guardrails

- Block structure must take precedence over inline syntax.
- Code blocks must remain literal and must not resolve escapes or references.
- Raw HTML blocks must not be escaped.
- Do not invoke `full_test.sh` from scoped checks.
