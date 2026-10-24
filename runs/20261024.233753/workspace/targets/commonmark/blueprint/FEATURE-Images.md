# FEATURE: Images

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark inline and reference images. |
| Depends On  | ARCHITECTURE.md, FEATURE-ReferenceDefinitionsAndParagraphs.md |
| Provides    | inline images, reference images |
| Consumes    | link reference definitions |

## Purpose

Parse inline and reference-style images according to CommonMark 0.31.2. Render the image description as plain text in the `alt` attribute.

## Programmatic Acceptance

=== AC images-conformance ===
Intent: The implementation passes every supplied example in the “Images” section.
Suite: scoped
Probe: --dump-tests
Probe Count: json

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
        "Images",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC images-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow the supplied CommonMark 0.31.2 specification.
- Resolve image references using definitions collected during block parsing.
- Do not use a public Markdown implementation as the parser.
- Keep supplied conformance assets under `sources/` unchanged.
