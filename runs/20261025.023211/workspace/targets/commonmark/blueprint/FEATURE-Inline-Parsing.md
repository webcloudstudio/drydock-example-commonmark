# FEATURE: Inline Parsing

| Field       | Value |
|-------------|-------|
| Version     | 20261025 V1 |
| Description | Parses CommonMark inline syntax and renders inline HTML. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Parsing.md |
| Provides    | inline parser, HTML renderer |
| Consumes    | block parser, document reference map |

## Purpose

Parse inline content after block structure and document-wide link reference definitions are available. Render the parsed inline elements as HTML.

## Behavior

Implement the CommonMark 0.31.2 inline constructs: escaped text; entity and numeric references; code spans; delimiter-based emphasis and strong emphasis; inline and reference links; images; URI and email autolinks; raw HTML; hard and soft line breaks; and ordinary textual content.

Apply the specification's precedence and delimiter rules, including link and image nesting restrictions, reference-label normalization, URL and title parsing, and code-span normalization. Preserve raw HTML and escape ordinary text and attribute values as required by the specification examples.

## Programmatic Acceptance

=== AC inline-parsing-conformance ===
Intent: All supplied cases in the inline parsing sections pass (the complete inline capability slice).
Suite: scoped
Probe: --dump-tests
Probe Count: json

import subprocess
import sys

sections = (
    "Backslash escapes|Entity and numeric character references|Code spans|"
    "Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|"
    "Hard line breaks|Soft line breaks|Textual content"
)
command = [
    sys.executable, "sources/spec_tests.py",
    "--program", "./commonmark",
    "--spec", "sources/spec.txt",
    "--pattern", sections,
]
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-parsing-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not modify the supplied conformance assets.
- Implement the specified CommonMark 0.31.2 behavior without using a public Markdown implementation.
