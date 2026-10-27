# FEATURE: Escapes and Entities

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Resolve CommonMark backslash escapes and character references in eligible contexts. |
| Depends On | FEATURE-Lists.md |
| Provides | inline escapes and character references |
| Consumes | list containers, reference definition map |

## Purpose and behavior

After block structure and document-wide definitions are complete, parse inline content. A backslash escapes only ASCII punctuation; before other characters it remains literal. A backslash immediately before a line ending is a hard-break marker, handled by the line-break capability.

Recognize HTML5 named character references only with a terminating semicolon. Recognize decimal numeric references of one to seven digits and hexadecimal references of one to six digits, also requiring a semicolon. Replace invalid Unicode code points and U+0000 with U+FFFD according to the specification. References do not create structural Markdown delimiters. Neither escapes nor references are interpreted in code spans or code blocks; escapes do not apply inside autolinks or raw HTML.

Apply the same eligible escape and reference rules to destinations, titles, and fenced-code info strings. Preserve raw HTML attributes.

Expose `decode_escapes_and_entities(text)` from `commonmark_parser.inline`. It returns decoded text for an eligible plain-text context; the caller determines context and handles structural syntax before decoding.

The later integration story runs the complete Backslash escapes and Entity and numeric character references sections with links, images, code spans, autolinks, HTML, and line breaks available.

## Programmatic Acceptance

=== AC escaped-punctuation ===
Intent: A backslash before ASCII punctuation produces the punctuation supplied in the source.

from commonmark_parser.inline import decode_escapes_and_entities

punctuation = "*"
source = "\\" + punctuation
assert decode_escapes_and_entities(source) == punctuation
=== END AC escaped-punctuation ===

=== AC unescaped-character ===
Intent: A backslash before a non-punctuation character remains literal.

from commonmark_parser.inline import decode_escapes_and_entities

source = "\\a"
assert decode_escapes_and_entities(source) == source
=== END AC unescaped-character ===

=== AC numeric-reference ===
Intent: A valid numeric character reference resolves to the character represented by its supplied code point.

from commonmark_parser.inline import decode_escapes_and_entities

codepoint = 65
source = f"&#{codepoint};"
assert decode_escapes_and_entities(source) == chr(codepoint)
=== END AC numeric-reference ===

## User Acceptance

- None.

## Guardrails

- Parse blocks and collect reference definitions before parsing inlines.
- Do not use a public Markdown implementation or modify the supplied conformance assets.
