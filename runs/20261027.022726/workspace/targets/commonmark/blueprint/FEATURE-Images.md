# FEATURE: Images

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse inline and reference images and render their descriptions as alt text. |
| Depends On | FEATURE-Links.md, FEATURE-ReferenceDefinitions.md |
| Provides | inline and reference images |
| Consumes | inline and reference links, reference definition map |

## Purpose

Support images in inline content using the link grammar and document-wide reference definitions.

## Behavior

Recognize inline, full, collapsed, and shortcut image forms beginning with `![`. Apply the destination, title, label matching, and precedence rules shared with links. Image descriptions may contain links and nested images. Render the plain textual content of the parsed description as the escaped HTML `alt` attribute, without its formatting tags; render the destination and optional title according to the supplied examples.

Resolve brackets and emphasis using the specification's delimiter-stack procedure. Preserve the distinction between an image opener and a link opener so that image descriptions can contain links.

## Programmatic Acceptance

=== AC images-conformance ===
Intent: The parser passes the authoritative image examples, including nested descriptions and reference forms.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", os.path.abspath("commonmark"),
     "--spec", "sources/spec.txt", "--pattern", "^Images$"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC images-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Do not modify the supplied conformance assets.
