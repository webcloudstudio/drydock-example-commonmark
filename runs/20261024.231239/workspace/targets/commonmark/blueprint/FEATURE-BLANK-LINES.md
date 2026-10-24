# FEATURE: Blank Lines

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Handles blank lines between blocks and at document boundaries. |
| Depends On  | FEATURE-CLI.md |
| Provides    | blank line handling |

## Purpose

Ignore blank lines around document blocks while preserving their specified effect on list tightness.

## Behavior

- Blank lines contain no characters or only spaces and tabs.
- Ignore leading and trailing document blank lines and blank lines between ordinary blocks.
- Preserve blank-line information needed to determine whether list items or blocks inside an item make a list loose.

## Programmatic Acceptance

=== AC blank-lines-conformance ===
Intent: The supplied “Blank lines” examples define correct document blank-line handling.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Blank lines"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC blank-lines-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not let blank lines alter ordinary block output beyond their specified list-tightness effect.
- Keep all supplied scoring assets unchanged.
