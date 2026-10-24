# FEATURE: Link Reference Definitions

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Extract link reference definitions when a paragraph closes and provide the document-wide reference map and label normalization. |
| Depends On  | FEATURE-Block-Engine.md |
| Provides    | reference map, normalize_label |
| Consumes    | block tree builder |

## Purpose

Implement the Link reference definitions section of the spec and the label matching shared with links and images.

## Rules

- When a paragraph closes, repeatedly parse a definition at the start of its text: up to three spaces of indentation, a link label, a colon, optional whitespace with up to one line ending, a link destination, optional whitespace with up to one line ending, and an optional title. Nothing else may follow on the final line.
- A link label has 1 to 999 characters, at least one non-whitespace character, and no unescaped brackets. A destination is either `<...>` with no line ending or unescaped `<` or `>`, or a nonempty run with no spaces or control characters and balanced parentheses. An empty `<>` destination is allowed.
- A title is double-quoted, single-quoted or parenthesized, may span lines, must not contain a blank line, and must be separated from the destination by whitespace.
- If the title does not parse, but the destination ends its line, the definition has no title and the rest of the paragraph remains. If anything else follows the title on its line, the whole attempt fails and the text stays a paragraph.
- The first definition for a normalized label wins. Definitions in containers go into the same document-wide map. A definition cannot interrupt a paragraph, which follows from extracting only at the start of the paragraph's text.
- Remaining text becomes a paragraph. A paragraph that consists only of definitions disappears.
- `normalize_label` strips the brackets, applies `str.casefold()`, strips, and collapses internal spaces, tabs and line endings to one space. Matching compares normalized strings, not parsed inlines.
- Destination and title go through the shared unescape and entity helpers. The stored destination is percent-encoded at render time by the link story.

## Reads

- Closed paragraph text.

## Writes

- Entries in the reference map.

## Programmatic Acceptance

The corpus section needs headings, quotes, setext headings and links, so it is gated in the tabs story. The checks here are bounded and use paragraph counts.

=== AC defs-definition-only-renders-nothing ===
Intent: A document that is only a definition, with or without a title or angle brackets, renders no paragraph.

import subprocess

for source in ['[foo]: /url "title"\n', "[foo]:\n/url\n'title'\n", "[foo]: <>\n"]:
    result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 0
=== END AC defs-definition-only-renders-nothing ===

=== AC defs-remainder-is-paragraph ===
Intent: Text after a definition stays as one paragraph.

import subprocess

rest = "remaining text"
result = subprocess.run(["./commonmark"], input="[foo]: /url\n" + rest + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
assert rest in result.stdout
=== END AC defs-remainder-is-paragraph ===

=== AC defs-trailing-text-not-definition ===
Intent: Extra text after the title means the line is not a definition, so it stays a paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input='[foo]: /url "title" ok\n', capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
=== END AC defs-trailing-text-not-definition ===

=== AC defs-cannot-interrupt-paragraph ===
Intent: A definition line directly after paragraph text is part of that paragraph.

import subprocess

definition = "[bar]: /baz"
result = subprocess.run(["./commonmark"], input="Foo\n" + definition + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
assert definition in result.stdout
=== END AC defs-cannot-interrupt-paragraph ===

=== AC defs-title-with-blank-line ===
Intent: A title containing a blank line is not valid, so the two halves become two paragraphs.

import subprocess

result = subprocess.run(
    ["./commonmark"],
    input="[foo]: /url 'title\n\nwith blank line'\n",
    capture_output=True,
    text=True,
)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 2
=== END AC defs-title-with-blank-line ===

## User Acceptance

- None.

## Guardrails

- A definition must never interrupt a paragraph.
- Label matching is on normalized strings only, never on parsed inline content.
- Do not skip, filter or reinterpret corpus examples.
