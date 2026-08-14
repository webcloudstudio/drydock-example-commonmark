# FEATURE: Block HTML Rendering

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines HTML rendering for parsed block structure and block-level content. |
| Depends On  | ARCHITECTURE.md, FEATURE-BLOCK-LISTS.md, FEATURE-INLINE-HTML.md |
| Provides    | block HTML renderer |
| Consumes    | block parser, inline parser |

## Rendering Contract

- Paragraphs render as `<p>` elements except for paragraphs in tight lists.
- ATX and setext headings render as `<h1>` through `<h6>`.
- Thematic breaks render as `<hr />`.
- Indented and fenced code render as escaped `<pre><code>` content.
- Block quotes render as `<blockquote>`.
- Ordered and unordered lists preserve nesting, start values, item boundaries, and tightness.
- Raw HTML blocks remain unescaped.

## Programmatic Acceptance

=== AC render-blocks-suite ===
Intent: Block-level HTML rendering passes the complete owned conformance scope.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Paragraphs|Blank lines|Block quotes|List items|Lists)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC render-blocks-suite ===

=== AC render-blocks-escaping ===
Intent: Block rendering preserves structural nesting and escapes literal code content.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Indented code blocks|Fenced code blocks|Block quotes|List items|Lists)$"],
    capture_output=True, text=True,
)
assert result.returncode == 0
=== END AC render-blocks-escaping ===

## User Acceptance

- None.

## Guardrails

- Block rendering never treats captured test output as a correctness oracle.
- Literal code content is escaped while raw HTML blocks remain preserved.
