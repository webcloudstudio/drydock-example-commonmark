# FEATURE: Conformance Integration

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Integrate the parser stages and exercise all scoped specification examples. |
| Depends On | FEATURE-Executable.md, FEATURE-Lists.md, FEATURE-Images.md, FEATURE-Autolinks.md, FEATURE-InlineHTMLBreaks.md |
| Provides | integrated CommonMark parser |
| Consumes | commonmark, list block parsing, image parsing, autolink parsing, inline HTML and hard break parsing |

## Purpose and workflow

Assemble the standard-stream executable with block parsing, document-wide reference collection, inline parsing, and HTML rendering. Finish block structure and reference collection before parsing inline content. The integrated parser must support the interactions among all previously delivered constructs.

Execute every example-owning section of the supplied corpus through its documented `--pattern` selector. The scoped checks below cover Tabs and Precedence as well as the complete block, container, and inline sections. The runner's JSON dump is the selection probe; the acceptance execution itself runs the selected examples against the executable.

## Programmatic Acceptance

=== AC conformance-preliminaries ===
Intent: The integrated parser passes every supplied Tabs and Precedence example.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^(Tabs|Precedence)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC conformance-preliminaries ===

=== AC conformance-blocks ===
Intent: The integrated parser passes every example in the supplied leaf block sections.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|Blank lines)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC conformance-blocks ===

=== AC conformance-containers ===
Intent: The integrated parser passes every supplied block quote, list item, and list example.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^(Block quotes|List items|Lists)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC conformance-containers ===

=== AC conformance-inlines ===
Intent: The integrated parser passes every example in the supplied inline and text sections.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^(Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks|Textual content)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC conformance-inlines ===

## User Acceptance

- None.

## Guardrails

- Preserve the supplied conformance assets verbatim under `sources/`.
- Do not invoke `full_test.sh` from these scoped checks.
- Do not use a public Markdown implementation.
