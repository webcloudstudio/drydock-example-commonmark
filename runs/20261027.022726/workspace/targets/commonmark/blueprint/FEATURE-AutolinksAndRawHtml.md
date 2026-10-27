# FEATURE: Autolinks and Raw HTML

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse URI and email autolinks and preserve valid inline HTML. |
| Depends On | FEATURE-Images.md |
| Provides | autolinks and raw inline HTML |
| Consumes | inline and reference images, code spans |

## Purpose

Recognize autolinks and raw HTML in inline content while respecting their precedence with other inline constructs.

## Behavior

Recognize angle-delimited absolute URI autolinks using the specified scheme and character rules, and email autolinks using the specified email grammar. Render the URI or email address as link text, with `mailto:` added to email destinations. Apply the escaping required by the examples; backslash escapes do not operate inside autolinks.

Recognize open and closing tags, comments, processing instructions, declarations, and CDATA sections using the specification's inline HTML grammar. Preserve valid raw HTML verbatim; treat invalid forms as ordinary inline text. Code spans, autolinks, and raw HTML have equal precedence and are recognized in left-to-right order. They bind more tightly than emphasis and link brackets.

## Programmatic Acceptance

=== AC autolinks-html-conformance ===
Intent: The parser passes the authoritative autolink and raw-HTML examples.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^(Autolinks|Raw HTML)$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC autolinks-html-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Do not modify the supplied conformance assets.
