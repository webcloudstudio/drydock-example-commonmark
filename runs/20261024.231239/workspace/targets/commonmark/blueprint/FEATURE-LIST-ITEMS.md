# FEATURE: List Items

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark list item boundaries, continuation, nesting, and laziness. |
| Depends On  | FEATURE-BLOCK-QUOTES.md, FEATURE-BLANK-LINES.md |
| Provides    | list item parsing and nesting |
| Consumes    | commonmark |

## Purpose

Recognize bullet markers (`-`, `+`, `*`) and ordered markers of one to nine digits followed by `.` or `)`. Parse each item’s content as blocks, including nested blocks, continuation paragraphs, and lazy continuation lines.

## Behavior

- A list marker may be preceded by up to three spaces and must be followed by one to four spaces of content indentation, or be an empty item.
- Support items beginning with indented code or a blank line under the specification’s distinct indentation rules.
- Continuation indentation is based on marker width and the spaces following the marker. Support nested items and lazy continuation only for paragraph continuation text.
- An item cannot interrupt a paragraph when empty; ordered lists interrupt paragraphs only when the marker number is 1.
- A thematic break takes precedence over a list item when both interpretations are possible.
- Render item contents within `<li>` elements; list wrapper grouping and tightness are defined by FEATURE-LISTS.md.

## Programmatic Acceptance

=== AC list-items-conformance ===
Intent: All supplied List items examples pass through the executable.
Suite: scoped
Probe: --list
Probe Count: summary

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "List items"],
    capture_output=True, text=True,
    env={**os.environ, "PYTHONPATH": f"{os.getcwd()}/sources"},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC list-items-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not conflate list item boundaries with list grouping or tight/loose rendering.
- Do not modify supplied scoring assets.
- Do not use a public Markdown implementation.
