# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses block quotes, nesting, and lazy continuation. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | block quote parsing |
| Consumes    | commonmark executable |

## Purpose

Parse CommonMark block quotes as containers whose contents are parsed using the ordinary block rules.

## Behavior

- Recognize `>` with up to three spaces of leading indentation; consume an optional following space. Support nested and empty quotes and preserve quote boundaries.
- Consecutive quote-marked lines belong to one quote. A blank line separates adjacent quotes and preserves paragraph boundaries inside a quote.
- Permit an unmarked lazy continuation only when it continues paragraph text inside the quote. Do not extend a quote with an unmarked line that starts another block construct or continues code.
- Render the contained blocks within `<blockquote>` elements.

## Programmatic Acceptance

=== AC block-quotes ===
Intent: The implementation passes all supplied block quote conformance examples.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Block quotes"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-quotes ===

## User Acceptance

- None.

## Guardrails

- Do not modify supplied scoring assets or invoke `sources/full_test.sh` from this scoped check.
