# FEATURE: Autolinks and Raw HTML

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Parses URI and email autolinks and preserves recognized raw HTML. |
| Depends On  | FEATURE-CommandLine.md |
| Provides    | autolinks and raw inline HTML parsing |
| Consumes    | commonmark executable |

## Purpose

Parse inline autolinks and raw HTML according to CommonMark 0.31.2. The command-line executable is the parser interface; these constructs are recognized during inline parsing after block structure is resolved.

## Behavior

- Recognize URI autolinks in angle brackets when the scheme has 2–32 characters, starts with an ASCII letter, and continues with ASCII letters, digits, `+`, `.`, or `-`. The URI may contain no ASCII control characters, spaces, `<`, or `>`.
- Recognize email autolinks in angle brackets using the email-address form specified in CommonMark 0.31.2, and render their destinations with the `mailto:` scheme.
- Treat backslash escapes as inactive inside autolinks.
- Recognize raw HTML open and closing tags, comments, processing instructions, declarations, and CDATA sections using the specification’s grammar. Preserve recognized raw HTML without Markdown escaping.
- Leave text that does not meet an autolink or raw HTML form available for ordinary text rendering.

## Programmatic Acceptance

=== AC inline-autolinks-raw-html ===
Intent: The executable passes the complete supplied conformance slice for autolinks and raw HTML.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        f"{__import__('os').getcwd()}/commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "Autolinks|Raw HTML",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-autolinks-raw-html ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Preserve the supplied scoring assets unchanged.
- Resolve block structure before inline structure.
