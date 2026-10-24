# FEATURE: Link Reference Definitions

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Collects document-wide link reference definitions during block parsing. |
| Depends On  | FEATURE-CLI.md |
| Provides    | document link reference definitions |

## Purpose

Collect valid link reference definitions during block parsing so inline links and images can resolve them document-wide after block structure is complete.

## Behavior

- Definitions may occur before or after uses, inside containers, and in succession.
- Normalize labels by Unicode case folding, trimming surrounding spaces and line endings, and collapsing internal whitespace.
- Keep the first definition for a normalized label.
- A valid definition is removed from visible content; invalid candidates remain ordinary text.
- Parse destinations, optional titles, escapes, and permitted line continuations according to CommonMark 0.31.2.

## Programmatic Acceptance

=== AC link-reference-definition-conformance ===
Intent: The supplied “Link reference definitions” examples define correct collection and visible rendering.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Link reference definitions"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC link-reference-definition-conformance ===

## User Acceptance

- None.

## Guardrails

- Preserve document-wide definition availability, including definitions nested in containers.
- Keep all supplied scoring assets unchanged.
