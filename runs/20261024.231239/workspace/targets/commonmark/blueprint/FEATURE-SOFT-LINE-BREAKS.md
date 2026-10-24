# FEATURE: Soft Line Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Preserves regular line endings between inline content. |
| Depends On  | ARCHITECTURE.md |
| Provides    | soft line breaks |
| Consumes    | — |

## Behavior

- Parse a regular line ending not covered by hard-break rules as a soft line break.
- Remove trailing spaces and leading spaces around soft line breaks.
- Render soft line breaks as line endings in HTML, consistent with the supplied examples.

## Programmatic Acceptance

=== AC soft-line-breaks-conformance ===
Intent: All supplied Soft line breaks examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Soft line breaks"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC soft-line-breaks-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep supplied scoring assets unchanged.
