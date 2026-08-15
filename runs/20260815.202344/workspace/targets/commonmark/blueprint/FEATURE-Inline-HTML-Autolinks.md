# FEATURE: Inline HTML and Autolinks

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse CommonMark URI autolinks, email autolinks, and raw HTML constructs. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leafs.md, FEATURE-Inline-Basics.md |
| Provides    | URI autolinks, email autolinks, raw HTML |
| Consumes    | executable commonmark, block structure, inline basics |

## Purpose

Implement inline autolinks and raw HTML while preserving their precedence over ordinary text and emphasis.

## Behavior

- Parse absolute URI autolinks and valid email autolinks.
- Render URI autolinks as links to their URI and email autolinks with `mailto:` destinations.
- Recognize valid open and closing tags, comments, processing instructions, declarations, and CDATA sections.
- Preserve valid raw HTML without Markdown interpretation inside the raw construct.
- Reject malformed tags and autolinks as literal escaped text.
- Respect precedence with code spans, links, images, and emphasis.

## Programmatic Acceptance

=== AC html-autolinks-conformance ===
Intent: The implementation passes every supplied conformance example owned by autolinks and raw HTML.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        "./commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        r"^(Autolinks|Raw HTML)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC html-autolinks-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Preserve raw HTML exactly where the specification requires it.
- Do not modify supplied conformance assets.
