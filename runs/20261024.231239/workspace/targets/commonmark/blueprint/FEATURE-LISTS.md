# FEATURE: Lists

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Groups list items and renders ordered and bullet lists with CommonMark tightness. |
| Depends On  | FEATURE-LIST-ITEMS.md, FEATURE-BLANK-LINES.md |
| Provides    | bullet and ordered list rendering |
| Consumes    | list item parsing and nesting |

## Purpose

Group adjacent list items of the same type into lists, determine ordered-list start numbers, and render tight or loose lists according to CommonMark 0.31.2.

## Behavior

- Items belong to the same list only when their bullet character matches, or their ordered delimiter matches.
- The first ordered item sets the list start number; subsequent item numbers do not change it. Emit a `start` attribute when required by the conformance examples.
- A list is loose when items are separated by blank lines or when an item has directly contained blocks separated by a blank line. Otherwise it is tight.
- Tight lists omit paragraph wrappers for item paragraphs; loose lists retain them. Nested lists determine tightness independently.
- A thematic break that takes precedence over a list item ends the current list.

## Programmatic Acceptance

=== AC lists-conformance ===
Intent: All supplied Lists examples pass through the executable.
Suite: scoped
Probe: --list
Probe Count: summary

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Lists"],
    capture_output=True, text=True,
    env={**os.environ, "PYTHONPATH": f"{os.getcwd()}/sources"},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists-conformance ===

## User Acceptance

- None.

## Guardrails

- Keep nested list tightness local to each list.
- Do not modify supplied scoring assets.
- Do not use a public Markdown implementation.
