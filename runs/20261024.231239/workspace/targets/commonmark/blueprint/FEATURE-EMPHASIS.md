# FEATURE: Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parse CommonMark emphasis and strong emphasis in inline content. |
| Depends On  | FEATURE-CLI.md, FEATURE-THEMATIC-BREAKS.md, FEATURE-ATX-HEADINGS.md, FEATURE-SETEXT-HEADINGS.md, FEATURE-INDENTED-CODE.md, FEATURE-FENCED-CODE.md, FEATURE-HTML-BLOCKS.md, FEATURE-LINK-REFERENCE-DEFINITIONS.md, FEATURE-PARAGRAPHS.md, FEATURE-BLANK-LINES.md, FEATURE-BLOCK-QUOTES.md, FEATURE-LIST-ITEMS.md, FEATURE-LISTS.md, FEATURE-BACKSLASH-ESCAPES.md, FEATURE-CHARACTER-REFERENCES.md, FEATURE-CODE-SPANS.md |
| Provides    | CommonMark emphasis and strong emphasis |
| Consumes    | CommonMark inline content |

## Purpose

Interpret `*` and `_` delimiter runs as emphasis or strong emphasis according to the CommonMark delimiter-run rules. Support nested spans, Unicode whitespace and punctuation, intraword `*` emphasis, the restrictions on intraword `_` emphasis, and the specified precedence and ambiguity rules.

## Parsing and rendering

- Determine left- and right-flanking runs from neighboring Unicode whitespace and punctuation.
- Apply the opener and closer rules for `*`, `_`, `**`, and `__`, including the rule of three.
- Use the smallest valid delimiter spans and minimize nesting where the rules require it. Preserve unmatched delimiter characters as text.
- Render emphasis with `<em>` and strong emphasis with `<strong>`. Parse their contents as inline content, including other emphasis constructs.
- Code spans, links, images, and HTML tags bind more tightly than emphasis.

## Programmatic Acceptance

=== AC emphasis-suite ===
Intent: All supplied examples in the “Emphasis and strong emphasis” section pass.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Emphasis and strong emphasis"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC emphasis-suite ===

## User Acceptance

- None.

## Guardrails

- Use the supplied CommonMark 0.31.2 rules and examples as authoritative.
- Preserve escaped delimiter characters and unmatched runs as literal text.
- Do not use a public Markdown implementation.
- Do not modify supplied scoring assets.
