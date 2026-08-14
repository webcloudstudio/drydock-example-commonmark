# FEATURE: Autolinks and Raw HTML

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines URI and email autolinks and preservation of raw HTML inline constructs. |
| Depends On  | ARCHITECTURE.md, FEATURE-INLINE-LINKS.md |
| Provides    | autolink parser, raw HTML parser |
| Consumes    | block parser, inline parser |

## Behavior

- Absolute URI autolinks become links whose labels preserve the source URI.
- Valid email autolinks become `mailto:` links.
- HTML tags, comments, declarations, processing instructions, and CDATA are preserved as raw HTML.
- Invalid autolinks and malformed HTML-like text remain escaped text.
- Backslash escapes do not apply inside autolinks or raw HTML.

## Programmatic Acceptance

=== AC inline-html-suite ===
Intent: The autolink and raw HTML syntax passes its complete owned conformance scope.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Autolinks|Raw HTML)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-html-suite ===

=== AC inline-html-malformed ===
Intent: Invalid autolinks and malformed HTML remain ordinary escaped content.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Autolinks|Raw HTML)$"],
    capture_output=True, text=True,
)
assert result.returncode == 0
=== END AC inline-html-malformed ===

## User Acceptance

- None.

## Guardrails

- Raw HTML is preserved only when it satisfies the CommonMark inline grammar.
- The parser does not execute or fetch HTML or URI content.
