# FEATURE: Lists

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark bullet and ordered lists, including nesting and tightness. |
| Depends On  | ARCHITECTURE.md |
| Provides    | list items, lists and tightness |

## Purpose

Parse bullet and ordered list items as containers, including nested blocks and the tight or loose rendering rules defined by CommonMark 0.31.2.

## Behavior

- Recognize bullet markers `-`, `+`, and `*`, and ordered markers of one to nine digits followed by `.` or `)`.
- Determine item continuation indentation from the marker width and the spaces after it; support the special rules for items beginning with indented code or a blank line.
- Support nested lists, lazy paragraph continuation, empty items, and list items containing any supported block type.
- Start a new list when list marker types differ. The ordered list start value comes from its first item.
- A list is loose when items are separated by blank lines or an item has block children separated by a blank line. Render paragraphs in loose lists with `<p>` tags and omit those tags for paragraphs in tight lists. Determine tightness independently for nested lists.

## Programmatic Acceptance

=== AC lists ===
Intent: The parser passes the complete supplied examples for list items and lists.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

pattern = "List items|Lists"
environment = {
    **os.environ,
    "PYTHONPATH": os.pathsep.join(
        [os.path.abspath("sources"), os.environ.get("PYTHONPATH", "")]
    ).rstrip(os.pathsep),
}
result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.path.abspath("commonmark"),
        "--spec",
        "sources/spec.txt",
        "--pattern",
        pattern,
    ],
    capture_output=True,
    text=True,
    env=environment,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists ===

## User Acceptance

- None.

## Guardrails

- Preserve the supplied conformance assets unchanged.
- Do not use a public Markdown implementation as the parser.
