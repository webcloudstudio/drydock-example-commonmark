# FEATURE: Block Lists

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse nested bullet and ordered lists with CommonMark tightness and lazy continuation. |
| Depends On  | FEATURE-Block-Quotes.md, FEATURE-Block-References.md |
| Provides    | list nodes, list item nodes, tight and loose list state |
| Consumes    | block quote nodes, leaf blocks, document-wide link reference definition map |

## Workflow

List parsing consumes normalized input after block quotes and reference definitions are available. Recognize bullet and ordered markers, determine item content indentation, recursively parse contained blocks, and group adjacent items only when their marker types match.

Track list tightness from blank lines between items and between directly contained blocks. Preserve ordered-list start numbers, empty items, nested lists, lazy paragraph continuation, and delimiter changes. Render paragraph wrappers according to the computed tight or loose state.

## Programmatic Acceptance

=== AC block-lists-conformance ===
Intent: The implementation passes the authoritative CommonMark examples for list items and lists owned by this story.
Suite: scoped

import subprocess

result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^(List items|Lists)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC block-lists-conformance ===

=== AC block-lists-selector ===
Intent: The list conformance selector executes the owned specification sections successfully.
Suite: scoped

import subprocess

sections = r"^(List items|Lists)$"
result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", sections,
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC block-lists-selector ===

## User Acceptance

- None.

## Guardrails

- Do not invoke `full_test.sh` from this story.
- Preserve CommonMark block-before-inline parsing.
- Do not use a public Markdown implementation.
