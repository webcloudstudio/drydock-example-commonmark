# FEATURE: HTML Renderer

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Render the complete parsed document as CommonMark-compatible HTML. |
| Depends On  | FEATURE-Inline-HTML-Autolinks.md |
| Provides    | HTML renderer |
| Consumes    | block nodes, inline nodes, list tightness, raw HTML nodes |

## Intent

The renderer converts the completed block and inline tree into the HTML representation required by the supplied CommonMark 0.31.2 examples.

## Behavior

- Render paragraphs, headings, thematic breaks, code blocks, block quotes, lists, and list items.
- Render emphasis, strong emphasis, links, images, code spans, breaks, autolinks, entities, and raw HTML.
- Escape text, code content, attribute values, destinations, and titles according to the conformance examples.
- Preserve raw HTML nodes without escaping their markup.
- Render ordered-list start attributes and omit paragraph tags in tight lists.
- Emit the standard CommonMark HTML tag and whitespace conventions.

## Programmatic Acceptance

=== AC renderer-conformance ===
Intent: The renderer passes the authoritative conformance examples covering the implemented rendered surface.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--spec",
        "sources/spec.txt",
        "--program",
        "./commonmark",
        "--pattern",
        r"^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Block quotes|List items|Lists|Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC renderer-conformance ===

=== AC renderer-processes-document ===
Intent: The renderer produces a nonempty HTML document for a valid Markdown document.
Suite: scoped

import subprocess

source = "# renderer\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
assert result.stdout
=== END AC renderer-processes-document ===

## User Acceptance

- None.

## Guardrails

- Do not hand-code expectations that duplicate the authoritative conformance suite.
- Do not escape raw HTML nodes as ordinary text.
- Do not invoke `full_test.sh` from this story.
