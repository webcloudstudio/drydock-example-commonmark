# FEATURE: Autolinks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Convert valid URI and email autolinks into HTML links. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md, FEATURE-ATX-HEADINGS.md, FEATURE-SETEXT-HEADINGS.md, FEATURE-INDENTED-CODE.md, FEATURE-FENCED-CODE.md, FEATURE-HTML-BLOCKS.md, FEATURE-LINK-REFERENCE-DEFINITIONS.md, FEATURE-PARAGRAPHS.md, FEATURE-BLANK-LINES.md, FEATURE-BLOCK-QUOTES.md, FEATURE-LIST-ITEMS.md, FEATURE-LISTS.md, FEATURE-BACKSLASH-ESCAPES.md, FEATURE-CHARACTER-REFERENCES.md, FEATURE-CODE-SPANS.md, FEATURE-EMPHASIS.md, FEATURE-LINKS.md, FEATURE-IMAGES.md |
| Provides    | URI and email autolinks |
| Consumes    | CommonMark inline content |
 
## Purpose

Recognize valid absolute URI and email address autolinks enclosed in angle brackets. Render them as links whose visible text is the URI or address; email links use the `mailto:` scheme.

## Autolink rules

- URI schemes begin with an ASCII letter, contain 2–32 characters, and use only ASCII letters, digits, `+`, `.`, or `-`.
- URI contents exclude ASCII control characters, spaces, `<`, and `>`.
- Email autolinks follow the email address grammar in the CommonMark specification.
- Backslash escapes are not interpreted inside autolinks.
- Invalid autolinks remain ordinary text and are escaped as HTML text.

## Programmatic Acceptance

=== AC autolinks-suite ===
Intent: All supplied examples in the “Autolinks” section pass.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Autolinks"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC autolinks-suite ===

## User Acceptance

- None.

## Guardrails

- Do not turn plain URI or email text without angle brackets into links.
- Do not use a public Markdown implementation or modify supplied scoring assets.
