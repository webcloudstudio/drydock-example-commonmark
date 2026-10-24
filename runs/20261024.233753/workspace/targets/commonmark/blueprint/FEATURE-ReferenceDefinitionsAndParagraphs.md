# FEATURE: Reference Definitions and Paragraphs

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Forms paragraphs and collects document-wide link reference definitions. |
| Depends On  | ARCHITECTURE.md |
| Provides    | link reference definitions, paragraphs |

## Purpose

Form paragraphs from consecutive non-blank lines that are not interpreted as other block types. Collect link reference definitions during block parsing so inline links can resolve definitions anywhere in the document.

## Behavior

- Paragraph content is the raw text of its lines, with leading and trailing spaces or tabs removed before inline parsing. A paragraph cannot contain a blank line.
- Recognize link reference definitions with up to three spaces of indentation. Definitions may span lines as allowed by CommonMark 0.31.2 and may have an optional title.
- Definitions do not render as document content. Collect them across the whole document, including inside block quotes and list items.
- Normalize labels by Unicode case folding, trimming surrounding spaces, tabs, and line endings, and collapsing consecutive internal whitespace to one space.
- The first definition for a normalized label takes precedence.
- A link reference definition cannot interrupt a paragraph. Text that does not form a valid definition remains paragraph content.

## Programmatic Acceptance

=== AC references-and-paragraphs ===
Intent: The parser passes the complete supplied examples for link reference definitions and paragraphs.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

pattern = "Link reference definitions|Paragraphs"
environment = {
    **os.environ,
    "PYTHONPATH": os.pathsep.join(
        [os.path.abspath("sources"), os.environ.get("PYTHONPATH", "")]
    ).rstrip(os.pathsep),
}
result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.path.abspath("commonmark"),
        "--spec",
        "sources/spec.txt",
        "--pattern",
        pattern,
    ],
    capture_output=True,
    text=True,
    env=environment,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC references-and-paragraphs ===

## User Acceptance

- None.

## Guardrails

- Preserve the supplied conformance assets unchanged.
- Do not use a public Markdown implementation as the parser.
