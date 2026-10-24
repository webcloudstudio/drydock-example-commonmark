# FEATURE: Links

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parse inline and reference-style CommonMark links. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md, FEATURE-ATX-HEADINGS.md, FEATURE-SETEXT-HEADINGS.md, FEATURE-INDENTED-CODE.md, FEATURE-FENCED-CODE.md, FEATURE-HTML-BLOCKS.md, FEATURE-LINK-REFERENCE-DEFINITIONS.md, FEATURE-PARAGRAPHS.md, FEATURE-BLANK-LINES.md, FEATURE-BLOCK-QUOTES.md, FEATURE-LIST-ITEMS.md, FEATURE-LISTS.md, FEATURE-BACKSLASH-ESCAPES.md, FEATURE-CHARACTER-REFERENCES.md, FEATURE-CODE-SPANS.md, FEATURE-EMPHASIS.md |
| Provides    | Inline and reference links |
| Consumes    | Document link reference definitions |

## Purpose

Parse inline links and full, collapsed, and shortcut reference links. Resolve reference labels against the document-wide definitions collected during block parsing.

## Link behavior

- Parse inline destinations in angle-bracket or balanced-parenthesis form, optional titles, escapes, and character references as specified.
- Match reference labels after Unicode case folding, trimming, and collapsing whitespace. The first matching definition wins.
- Support links with empty text or destinations when allowed by the syntax.
- Bracketed link text may contain balanced brackets and inline elements. Links cannot contain nested links; code spans, autolinks, and raw HTML tags bind more tightly than link brackets.
- Render destinations as `href` and optional titles as `title`, escaping attribute values for HTML. Render link text as inline HTML.
- Images use the same syntax but are specified and implemented by the image capability.

## Programmatic Acceptance

=== AC links-suite ===
Intent: All supplied examples in the “Links” section pass.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Links"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC links-suite ===

## User Acceptance

- None.

## Guardrails

- Do not create links when the syntax is invalid or the reference label is undefined.
- Do not allow links to contain nested links.
- Do not use a public Markdown implementation or modify supplied scoring assets.
