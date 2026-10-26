# FEATURE: Link Reference Definitions

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Collects link reference definitions for document-wide inline resolution. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | document-wide link reference definitions |
| Consumes    | commonmark executable |

## Purpose

Collect valid CommonMark link reference definitions during block parsing so inline links and images can resolve them anywhere in the document.

## Behavior

- Recognize definitions with up to three leading spaces, a nonempty label, a destination, and an optional properly separated title. Support the permitted line endings within destinations and titles.
- Normalize labels by Unicode case folding, trimming surrounding spaces, tabs, and line endings, and collapsing internal runs of those characters to one space.
- Keep the first definition for each normalized label. Definitions may occur in containers, apply document-wide, and render no block.
- A definition cannot interrupt a paragraph. Invalid definition-like text remains paragraph content.

## Programmatic Acceptance

=== AC link-reference-definitions ===
Intent: The implementation passes all supplied link reference definition conformance examples.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
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
=== END AC link-reference-definitions ===

## User Acceptance

- None.

## Guardrails

- Resolve document structure before inline parsing so definitions later in the document are available.
- Do not modify supplied scoring assets or invoke `sources/full_test.sh` from this scoped check.
