# FEATURE: Links

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark inline and reference links. |
| Depends On  | ARCHITECTURE.md, FEATURE-ReferenceDefinitionsAndParagraphs.md |
| Provides    | inline links, reference links |
| Consumes    | link reference definitions |

## Purpose

Parse inline, full, collapsed, and shortcut links according to CommonMark 0.31.2. Handle destinations, titles, label normalization, and document-wide reference definitions.

## Programmatic Acceptance

=== AC links-conformance ===
Intent: The implementation passes every supplied example in the “Links” section.
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
        "Links",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC links-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow the supplied CommonMark 0.31.2 specification.
- Resolve references using definitions collected during block parsing.
- Do not use a public Markdown implementation as the parser.
- Keep supplied conformance assets under `sources/` unchanged.
