# FEATURE: Hard Line Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses hard line breaks within inline content. |
| Depends On  | ARCHITECTURE.md |
| Provides    | hard line breaks |
| Consumes    | — |

## Behavior

- Render a line ending preceded by at least two spaces as `<br />` when it occurs within a block.
- Render a backslash immediately before a line ending as `<br />` within a block.
- Ignore leading spaces on the following line after a hard break.
- Do not treat either form as a hard break at the end of a block or inside code spans or HTML tags.

## Programmatic Acceptance

=== AC hard-line-breaks-conformance ===
Intent: All supplied Hard line breaks examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Hard line breaks"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC hard-line-breaks-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep supplied scoring assets unchanged.
