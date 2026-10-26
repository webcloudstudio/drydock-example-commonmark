# FEATURE: Links and Images

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses inline links, reference links, and images. |
| Depends On  | FEATURE-CommandLine.md, FEATURE-LinkReferenceDefinitions.md |
| Provides    | inline links, reference links, and images |
| Consumes     | commonmark executable, document-wide link reference definitions |

## Purpose

Parse CommonMark inline links, reference links, and images using the resolved document-wide definitions.

## Behavior

- Support inline links and full, collapsed, and shortcut reference links, with matching based on normalized labels and the first matching definition.
- Parse link text and image descriptions with balanced brackets and inline content. Links cannot contain links; image descriptions may contain them.
- Parse destinations and optional titles in angle-bracket and bare forms, honoring escapes, balanced parentheses, whitespace, and line-ending rules.
- Render link destinations and titles with the required HTML and URL escaping. Render image descriptions as plain text in the `alt` attribute.
- Use link reference definitions collected during block parsing, including definitions inside block containers.

## Programmatic Acceptance

=== AC links-and-images-conformance ===
Intent: The executable passes every supplied Links and Images example.
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
        "^(Links|Images)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC links-and-images-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not modify the supplied conformance assets.
- Resolve block structure and reference definitions before inline parsing.
- Do not allow links to contain links.
