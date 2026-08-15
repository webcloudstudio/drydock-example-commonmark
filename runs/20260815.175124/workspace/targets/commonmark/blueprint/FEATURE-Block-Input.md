# FEATURE: Block Input

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Normalize CommonMark input into Unicode lines with specification-compliant whitespace and insecure-character handling. |
| Depends On  | ARCHITECTURE.md |
| Provides    | normalized UTF-8 input lines |
| Consumes    | parser architecture |

## Workflow

The input boundary accepts Markdown text from the executable, replaces every U+0000 with U+FFFD, normalizes LF, CRLF, and CR line endings into logical lines, and preserves arbitrary Unicode. Block parsing consumes these lines with tab-stop indentation semantics.

Tabs are interpreted as reaching the next four-column tab stop when determining indentation. Internal tabs remain literal content when they are part of code or text. Blank lines contain only spaces and tabs.

## Programmatic Acceptance

=== AC block-input-tabs ===
Intent: The implementation passes the complete Tabs conformance section.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^Tabs$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-input-tabs ===

=== AC block-input-characters ===
Intent: The implementation passes the complete Characters and lines conformance section.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^Characters and lines$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-input-characters ===

=== AC block-input-insecure ===
Intent: The implementation passes the complete Insecure characters conformance section.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--spec", "sources/spec.txt",
     "--program", "./commonmark", "--pattern", r"^Insecure characters$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC block-input-insecure ===

## User Acceptance

- None.

## Guardrails

- Replace U+0000 with U+FFFD before parsing.
- Support LF, CRLF, and CR line endings.
- Preserve arbitrary Unicode and literal internal tabs.
- Do not invoke `full_test.sh` from scoped checks.
