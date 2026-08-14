# FEATURE: Leaf Block Parser

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Parses CommonMark leaf blocks and link reference definitions. |
| Depends On  | FEATURE-CLI-ENTRYPOINT.md |
| Provides    | leaf block parser |
| Consumes    | parser executable |

## Scope

The parser recognizes CommonMark 0.31.2 leaf blocks:

- thematic breaks;
- ATX headings;
- setext headings;
- indented code blocks;
- fenced code blocks;
- HTML blocks;
- paragraphs;
- link reference definitions.

Leaf parsing occurs before inline parsing. Link reference definitions are collected for later resolution and do not render as visible blocks.

## Programmatic Acceptance

Suite: scoped
Requires: executable=python3; scope=test

=== AC leaf-blocks-primary ===
Intent: The implementation passes the supplied conformance sections for thematic breaks, headings, and code blocks.

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "spec_tests.py",
        "--spec",
        "spec.txt",
        "--program",
        "./cmark",
        "--pattern",
        "Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC leaf-blocks-primary ===

=== AC leaf-blocks-secondary ===
Intent: The implementation passes the supplied conformance sections for HTML blocks, link references, paragraphs, and blank lines.

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "spec_tests.py",
        "--spec",
        "spec.txt",
        "--program",
        "./cmark",
        "--pattern",
        "HTML blocks|Link reference definitions|Paragraphs|Blank lines",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC leaf-blocks-secondary ===

## User Acceptance

- None.

## Guardrails

- Leaf blocks are parsed before inline constructs.
- Code blocks preserve literal content and do not parse inline syntax.
- Link reference definitions are not emitted as visible HTML blocks.
- Verification uses the supplied harness with selectors that match example-bearing sections.
