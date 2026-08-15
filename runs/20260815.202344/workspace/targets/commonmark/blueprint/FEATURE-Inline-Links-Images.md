# FEATURE: Inline Links and Images

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse CommonMark inline links, reference links, and images with destinations, titles, and label resolution. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leafs.md, FEATURE-Inline-Basics.md |
| Provides    | inline links, reference links, images |
| Consumes    | executable commonmark, link reference definitions, inline basics |

## Purpose

Implement inline and reference links and images using the document-wide link reference map produced during block parsing.

## Behavior

- Parse inline links and images with empty or nonempty destinations and optional titles.
- Parse full-reference, collapsed-reference, and shortcut links and images.
- Normalize labels using case folding and whitespace normalization.
- Support escaped and balanced brackets, escaped destinations and titles, entity references, nested image descriptions, and first-definition precedence.
- Prevent links from containing links while preserving permitted nested image behavior.
- Render links with `<a>` and images with `<img>` using plain-text image alt content.

## Programmatic Acceptance

=== AC links-images-conformance ===
Intent: The implementation passes every supplied conformance example owned by links and images.
Suite: scoped

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
        r"^(Links|Images)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC links-images-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Preserve document-wide reference-definition precedence.
- Do not modify supplied conformance assets.
