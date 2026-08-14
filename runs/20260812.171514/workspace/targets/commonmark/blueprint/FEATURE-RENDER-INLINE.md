# FEATURE: Inline HTML Rendering

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines HTML rendering for parsed inline nodes and inline source constructs. |
| Depends On  | ARCHITECTURE.md, FEATURE-RENDER-BLOCKS.md |
| Provides    | inline HTML renderer |
| Consumes    | inline parser |

## Rendering Contract

- Text escapes HTML-significant characters.
- Emphasis and strong emphasis render as `<em>` and `<strong>`.
- Code spans render as escaped `<code>` content.
- Links render escaped `href` and optional `title` attributes.
- Images render escaped `src`, plain-text `alt`, and optional `title`.
- Hard breaks render as `<br />`; soft breaks preserve permitted line-break semantics.
- Autolinks and raw HTML preserve the required HTML representation.
- Entity references render as their corresponding characters, with HTML escaping where required.

## Programmatic Acceptance

=== AC render-inline-suite ===
Intent: Inline HTML rendering passes the complete owned conformance scope.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Characters and lines|Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks|Textual content)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC render-inline-suite ===

=== AC render-inline-escaping ===
Intent: Inline rendering escapes text and code while preserving links, images, and raw HTML.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Code spans|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks)$"],
    capture_output=True, text=True,
)
assert result.returncode == 0
=== END AC render-inline-escaping ===

## User Acceptance

- None.

## Guardrails

- Renderer output is derived from parsed inline nodes and never from test-result text.
- User text cannot inject markup except through valid raw HTML constructs.
