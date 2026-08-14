# FEATURE: Inline Links and Images

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines inline links, reference links, images, destinations, titles, and reference resolution. |
| Depends On  | ARCHITECTURE.md, FEATURE-BLOCK-LEAF.md, FEATURE-INLINE-EMPHASIS.md |
| Provides    | link parser, image parser, reference resolver |
| Consumes    | block parser, inline parser |

## Purpose

The inline parser recognizes inline, full-reference, collapsed-reference, and shortcut links and images. It resolves link reference definitions collected during block parsing, supports balanced destinations and titles, and prevents nested links while permitting nested image descriptions.

## Behavior

- Inline destinations may be empty, angle-bracket delimited, escaped, or contain balanced parentheses.
- Titles may use single quotes, double quotes, or parentheses.
- Reference labels are normalized with Unicode case folding and whitespace normalization.
- The first matching reference definition wins.
- Link text is parsed as inline content.
- Image descriptions produce plain-text `alt` content.
- Links cannot contain links; image descriptions may contain links.

## Programmatic Acceptance

=== AC inline-links-suite ===
Intent: The inline link, reference link, and image syntax passes its complete owned conformance scope.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Links|Images)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-links-suite ===

=== AC inline-links-boundaries ===
Intent: The implementation preserves link and image destination, title, reference, and nesting behavior.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Links|Images)$"],
    capture_output=True, text=True,
)
assert result.returncode == 0
=== END AC inline-links-boundaries ===

## User Acceptance

- None.

## Guardrails

- The implementation does not use a public Markdown implementation.
- Reference definitions are resolved globally while preserving first-definition precedence.
