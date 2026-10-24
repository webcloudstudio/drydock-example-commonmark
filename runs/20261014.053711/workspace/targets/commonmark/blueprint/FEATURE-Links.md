# FEATURE: Links

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Implement the look-for-link-or-image procedure and the inline, full, collapsed and shortcut link forms with the destination and title grammar. |
| Depends On  | FEATURE-Emphasis.md, FEATURE-Link-Reference-Definitions.md |
| Provides    | look_for_link_or_image procedure, link destination and title grammar |
| Consumes    | delimiter stack, process_emphasis procedure, reference map, normalize_label |

## Purpose

Implement the Links section of the spec following the Appendix "look for link or image" procedure. The `![` machinery is shared with images; image rendering belongs to the images story.

## Procedure

- On `]`, search the delimiter stack from the top for a `[` or `![` opener. If none is found, emit literal `]`. If the opener is inactive, remove it and emit literal `]`.
- Otherwise parse ahead for, in order: an inline link `(`destination, title`)`; a full reference `[label]`; a collapsed reference `[]`; a shortcut reference. References resolve through `normalize_label` and the reference map. A full reference whose label is not defined falls back to the shortcut form of the link text only if it is not followed by a label.
- On success, build the link node from the inlines after the opener, run `process_emphasis` with the opener as `stack_bottom`, and remove the opener. For a link (not an image), set every earlier `[` opener inactive, so links never nest.
- On failure, remove the opener and emit literal `]`.

## Grammar

- A destination is `<...>` with no line ending and no unescaped `<` or `>`, or a nonempty run with no space or control characters and balanced unescaped parentheses (at least three levels). An empty destination is allowed.
- A title is double-quoted, single-quoted or parenthesized, with backslash-escaped delimiters, and no blank line inside.
- Whitespace (spaces, tabs, at most one line ending) is allowed around the destination and title; destination and title must be separated by whitespace.
- A link label has at most 999 characters and no unescaped brackets. No whitespace is allowed between link text and a following label or `()`.
- Brackets inside link text must be balanced or backslash-escaped. Code spans, autolinks and raw HTML bind tighter than brackets.
- Destination and title go through the shared unescape and entity helpers. The href is percent-encoded for non-ASCII and unsafe characters with the shared helper (an existing `%XX` stays as is), and the href and title are HTML-escaped.

## Reads

- Inline text, the reference map.

## Writes

- Link nodes in the inline tree.

## Programmatic Acceptance

The Links corpus section includes image examples, so it is gated in the images story. The checks here are bounded.

=== AC links-inline-destination-and-title ===
Intent: An inline link renders one a element carrying the supplied destination, title and text.

import subprocess

text = "label"
dest = "/uri"
title = "the title"
source = "[" + text + "](" + dest + ' "' + title + '")\n'
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 1
assert ('href="' + dest + '"') in result.stdout
assert ('title="' + title + '"') in result.stdout
assert (">" + text + "</a>") in result.stdout
=== END AC links-inline-destination-and-title ===

=== AC links-reference-forms ===
Intent: Full, collapsed and shortcut references each resolve against a definition and render one a element.

import subprocess

definition = "\n\n[foo]: /url\n"
for use in ("[text][foo]", "[foo][]", "[foo]"):
    result = subprocess.run(["./commonmark"], input=use + definition, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<a ") == 1
=== END AC links-reference-forms ===

=== AC links-reference-case-insensitive ===
Intent: Label matching ignores case.

import subprocess

result = subprocess.run(["./commonmark"], input="[FOO]\n\n[foo]: /url\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 1
=== END AC links-reference-case-insensitive ===

=== AC links-undefined-reference-literal ===
Intent: A shortcut reference with no definition stays literal text.

import subprocess

result = subprocess.run(["./commonmark"], input="[nothing defined]\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 0
=== END AC links-undefined-reference-literal ===

=== AC links-no-nested-links ===
Intent: A link inside link text wins and the outer brackets stay literal, so only one a element appears.

import subprocess

result = subprocess.run(["./commonmark"], input="[foo [bar](/uri)](/uri)\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 1
=== END AC links-no-nested-links ===

=== AC links-space-before-parenthesis ===
Intent: Whitespace between link text and the parenthesis prevents an inline link.

import subprocess

result = subprocess.run(["./commonmark"], input="[link] (/uri)\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 0
=== END AC links-space-before-parenthesis ===

## User Acceptance

- None.

## Guardrails

- Links must never contain other links at any level of nesting.
- Matching is on normalized label strings, not parsed inlines.
- Follow the Appendix procedure; do not backtrack across the whole document.
- Do not skip, filter or reinterpret corpus examples.
