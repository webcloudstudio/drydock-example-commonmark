# FEATURE: Links

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse inline and reference links using document-wide definitions. |
| Depends On | FEATURE-Emphasis.md, FEATURE-ReferenceDefinitions.md |
| Provides | inline and reference links |
| Consumes | reference definition map, emphasis and strong emphasis, code spans |

## Purpose

Turn valid inline and reference link syntax into HTML links using the definitions collected during block parsing.

## Behavior

Recognize inline links and full, collapsed, and shortcut references. Parse destinations and optional titles according to the specification, including balanced or escaped parentheses, angle-delimited destinations, permitted whitespace, and escaped characters and character references. Render destinations and titles with the escaping required by the supplied examples.

Match reference labels using the document-wide normalized definition map; the first matching definition wins. Apply the specified precedence among inline, full, collapsed, and shortcut forms. Link text can contain inline content and balanced brackets, but links cannot contain links. Use the appendix's bracket and delimiter-stack procedure: resolve emphasis within a successful link and deactivate earlier link openers when a link is formed. Code spans, autolinks, and raw HTML bind more tightly than link brackets.

## Programmatic Acceptance

=== AC links-conformance ===
Intent: The completed parser passes the authoritative link and link-reference-definition examples.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^(Links|Link reference definitions)$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC links-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Do not modify the supplied conformance assets.
