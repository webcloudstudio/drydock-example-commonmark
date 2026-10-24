# FEATURE: Tabs

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Make tabs behave as four-column tab stops for block structure while leaving tabs untouched in content, and gate the remaining corpus sections. |
| Depends On  | FEATURE-Lists.md |
| Provides    | tab-stop-aware column handling |
| Consumes    | block container rules |

## Purpose

Implement the Tabs section of the spec, audit every block rule's column handling, and gate the corpus sections whose examples needed all block and inline stories.

## Rules

- Tabs are never expanded into spaces in output. Inside code and text, a tab is passed through as a literal tab.
- Where spaces define block structure (indented code, block quote markers, list marker spacing, list item continuation, ATX heading and thematic break separators), a tab advances to the next multiple of 4 columns.
- A tab that is only partly consumed (for example after a `>` marker or a list marker) leaves its remaining columns as virtual spaces of indentation for the rest of the line.
- All block start and continue rules use the one shared column-aware helper from the block engine.

## Reads

- Lines handed to the block engine.

## Writes

- No new nodes; this story corrects column handling in existing rules.

## Programmatic Acceptance

=== AC tabs-corpus-and-remaining-sections ===
Intent: The Tabs, Link reference definitions, Backslash escapes, Entity and numeric character references, Raw HTML, HTML blocks, Paragraphs, Blank lines and Hard line breaks conformance sections (roughly 160 cases) pass in full.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import os
import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.getcwd() + "/commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "^Tabs$|^Link reference definitions$|^Backslash escapes$|^Entity and numeric character references$|^Raw HTML$|^HTML blocks$|^Paragraphs$|^Blank lines$|^Hard line breaks$",
    ],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC tabs-corpus-and-remaining-sections ===

=== AC tabs-indented-code-and-internal-tabs ===
Intent: A leading tab opens indented code, and internal tabs inside it are kept as tabs.

import subprocess

inner = "a\ta"
result = subprocess.run(["./commonmark"], input="\t" + inner + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert inner in result.stdout
=== END AC tabs-indented-code-and-internal-tabs ===

=== AC tabs-list-continuation ===
Intent: A tab-indented continuation paragraph belongs to the list item.

import subprocess

result = subprocess.run(["./commonmark"], input="  - foo\n\n\tbar\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<li>") == 1
assert result.stdout.count("<p>") == 2
=== END AC tabs-list-continuation ===

=== AC tabs-after-markers ===
Intent: A tab after a quote marker or list marker is consumed as columns, leaving code inside the container.

import subprocess

quote = subprocess.run(["./commonmark"], input=">\t\tfoo\n", capture_output=True, text=True)
item = subprocess.run(["./commonmark"], input="-\t\tfoo\n", capture_output=True, text=True)
print(quote.stdout)
print(item.stdout)
assert quote.returncode == 0
assert item.returncode == 0
assert quote.stdout.count("<blockquote>") == 1
assert quote.stdout.count("<pre>") == 1
assert item.stdout.count("<li>") == 1
assert item.stdout.count("<pre>") == 1
=== END AC tabs-after-markers ===

=== AC tabs-as-separators ===
Intent: Tabs between a heading marker and its text, and between thematic break characters, act as spaces.

import subprocess

heading = subprocess.run(["./commonmark"], input="#\tFoo\n", capture_output=True, text=True)
rule = subprocess.run(["./commonmark"], input="*\t*\t*\t\n", capture_output=True, text=True)
print(heading.stdout)
print(rule.stdout)
assert heading.returncode == 0
assert rule.returncode == 0
assert heading.stdout.count("<h1>") == 1
assert rule.stdout.count("<hr />") == 1
=== END AC tabs-as-separators ===

## User Acceptance

- None.

## Guardrails

- Never expand tabs into spaces in rendered content.
- Do not skip, filter or reinterpret corpus examples.
