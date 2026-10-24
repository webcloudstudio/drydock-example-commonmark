# FEATURE: Textual Content

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Preserves and safely renders plain textual content. |
| Depends On  | ARCHITECTURE.md |
| Provides    | textual content |
| Consumes    | — |

## Behavior

- Preserve characters not assigned another CommonMark interpretation.
- Escape text characters as required for safe HTML text output.
- Preserve internal spaces verbatim.

## Programmatic Acceptance

=== AC textual-content-conformance ===
Intent: All supplied Textual content examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Textual content"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC textual-content-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep supplied scoring assets unchanged.
