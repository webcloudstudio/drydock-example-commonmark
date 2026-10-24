# FEATURE: Verification

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Terminal assembly that runs the complete supplied CommonMark conformance suite unfiltered through the supplied scoring entry point. |
| Depends On  | FEATURE-Executable.md, FEATURE-Block-Engine.md, FEATURE-Autolinks.md, FEATURE-Raw-HTML.md, FEATURE-Code-Spans.md, FEATURE-Backslash-Escapes.md, FEATURE-Entities.md, FEATURE-Emphasis.md, FEATURE-Link-Reference-Definitions.md, FEATURE-Links.md, FEATURE-Images.md, FEATURE-Line-Breaks-Text.md, FEATURE-Thematic-Breaks.md, FEATURE-ATX-Headings.md, FEATURE-Indented-Code.md, FEATURE-Fenced-Code.md, FEATURE-HTML-Blocks.md, FEATURE-Block-Quotes.md, FEATURE-Setext-Headings.md, FEATURE-List-Items.md, FEATURE-Lists.md, FEATURE-Tabs.md |
| Provides    | None |
| Consumes    | ./commonmark |

## Purpose

This is the terminal story. Once every parser story has closed, it proves the whole product by running the supplied scoring entry point `sources/full_test.sh`, which runs the complete, unfiltered CommonMark 0.31.2 suite against `./commonmark`.

## Assembly and Intent

- Nothing new is implemented here. A failure points at the parser story that owns the failing example's construct, and the repair belongs in the parser.
- The scoring assets `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py` and `sources/spec.txt` are hash-verified and restored before grading. They must never be modified, and changing the entry point is not a repair.
- The check asserts only the script's exit status. The script itself confirms the clean tally.

## Programmatic Acceptance

=== AC full-conformance-suite ===
Intent: The complete supplied conformance suite passes when run unfiltered through sources/full_test.sh.
Suite: full

import subprocess

result = subprocess.run(["sh", "sources/full_test.sh"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC full-conformance-suite ===

## User Acceptance

- None.

## Guardrails

- Never filter, skip or reinterpret tests.
- Never modify `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py` or `sources/spec.txt`.
- Never use or call a public Markdown implementation.
