# FEATURE: Line Breaks and Text

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Renders CommonMark textual content and line breaks. |
| Depends On  | ARCHITECTURE.md |
| Provides    | hard line breaks, soft line breaks, textual content |

## Purpose

Render ordinary textual content, soft line breaks, and hard line breaks according to CommonMark 0.31.2.

## Programmatic Acceptance

=== AC line-breaks-and-text-conformance ===
Intent: The implementation passes every supplied example in the “Hard line breaks,” “Soft line breaks,” and “Textual content” sections.
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
        "Hard line breaks|Soft line breaks|Textual content",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC line-breaks-and-text-conformance ===

## User Acceptance

- None.

## Guardrails

- Follow the supplied CommonMark 0.31.2 specification.
- Keep supplied conformance assets under `sources/` unchanged.
