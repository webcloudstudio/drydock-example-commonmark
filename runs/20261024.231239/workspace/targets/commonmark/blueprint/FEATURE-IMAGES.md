# FEATURE: Images

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parse inline and reference-style CommonMark images. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md, FEATURE-ATX-HEADINGS.md, FEATURE-SETEXT-HEADINGS.md, FEATURE-INDENTED-CODE.md, FEATURE-FENCED-CODE.md, FEATURE-HTML-BLOCKS.md, FEATURE-LINK-REFERENCE-DEFINITIONS.md, FEATURE-PARAGRAPHS.md, FEATURE-BLANK-LINES.md, FEATURE-BLOCK-QUOTES.md, FEATURE-LIST-ITEMS.md, FEATURE-LISTS.md, FEATURE-BACKSLASH-ESCAPES.md, FEATURE-CHARACTER-REFERENCES.md, FEATURE-CODE-SPANS.md, FEATURE-EMPHASIS.md, FEATURE-LINKS.md |
| Provides    | Inline and reference images |
| Consumes    | Document link reference definitions |

## Purpose

Parse inline and reference-style images using the CommonMark link and label rules, including full, collapsed, and shortcut references.

## Image behavior

- Support empty descriptions and descriptions containing inline elements, links, and nested image syntax where valid.
- Render images as `<img>` elements with `src`, plain-text `alt`, and an optional `title`. The alt text is the description's plain textual content without inline formatting or markup.
- Resolve reference labels using the document-wide definitions and matching rules.
- Escape `src`, `alt`, and `title` attribute values for HTML.

## Programmatic Acceptance

=== AC images-suite ===
Intent: All supplied examples in the “Images” section pass.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Images"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC images-suite ===

## User Acceptance

- None.

## Guardrails

- Preserve the distinction between links and images; image descriptions render as plain-text alt attributes.
- Do not use a public Markdown implementation or modify supplied scoring assets.
