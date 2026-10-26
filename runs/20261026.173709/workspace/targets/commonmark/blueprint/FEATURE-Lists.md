# FEATURE: Lists

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses CommonMark lists, their items, and tightness. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | list and list item parsing |
| Consumes    | commonmark executable |

## Purpose

Parse bullet and ordered lists, including nesting and the relationship between blank lines and paragraph rendering.

## Behavior

- Recognize `-`, `+`, and `*` bullets and ordered markers of one to nine digits followed by `.` or `)`. Require separating whitespace or an empty item. Thematic breaks take precedence where applicable.
- Determine continuation indentation from marker width and the one to four spaces after a marker. Support list items that start with indented code or a blank line, up to three spaces of marker indentation, lazy paragraph continuation, and nested lists.
- Lists group only items with matching marker type and delimiter. An ordered list’s start value comes from its first item.
- Mark a list loose when blank lines separate its items or separate directly contained blocks within an item; otherwise render it tight. Preserve empty items and render loose-list paragraphs with `<p>` tags.

## Programmatic Acceptance

=== AC lists ===
Intent: The implementation passes all supplied list item and list conformance examples.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import json
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "List items|Lists"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists ===

## User Acceptance

- None.

## Guardrails

- Do not modify supplied scoring assets or invoke `sources/full_test.sh` from this scoped check.
