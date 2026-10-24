# FEATURE: Entities

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Decode HTML5 named entities and decimal and hexadecimal numeric character references, with a shared helper for destinations, titles and info strings. |
| Depends On  | FEATURE-Backslash-Escapes.md |
| Provides    | entity decoding rule, shared entity helper |
| Consumes    | inline scanner loop |

## Purpose

Implement the Entity and numeric character references section of the spec.

## Rules

- A named reference is `&`, a name present in `html.entities.html5` with a trailing semicolon, and `;`. References without a semicolon (for example `&copy`) and unknown names are not recognized and stay literal, with `&` escaped as `&amp;`.
- A decimal reference is `&#` plus 1 to 7 digits plus `;`. A hexadecimal reference is `&#` plus `x` or `X` plus 1 to 6 hex digits plus `;`.
- Invalid code points (surrogates, above U+10FFFF) and U+0000 are replaced with U+FFFD.
- A decoded character is always plain text and never structure: `&#42;` cannot start emphasis, a list or a thematic break. The decoded text is HTML-escaped on output.
- References are inert in code spans and code blocks, and are decoded in link destinations, titles and fenced info strings. The shared helper provides that for those stories.
- Some named entities decode to two code points; both are emitted.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Plain text nodes in the inline tree.

## Programmatic Acceptance

The corpus section needs links, definitions, fenced code, indented code and emphasis, so it is gated in the tabs story. The checks here are bounded and derive their expectations from bound inputs.

=== AC entities-decimal-reference ===
Intent: A decimal reference decodes to the character with the bound code point.

import subprocess

code_point = 65
result = subprocess.run(["./commonmark"], input="x &#" + str(code_point) + "; y\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert chr(code_point) in result.stdout
assert result.stdout.count("&#") == 0
=== END AC entities-decimal-reference ===

=== AC entities-hex-reference ===
Intent: Lowercase and uppercase hexadecimal references decode to the same character.

import subprocess

code_point = 66
lower = "&#x" + format(code_point, "x") + ";"
upper = "&#X" + format(code_point, "X") + ";"
first = subprocess.run(["./commonmark"], input=lower + "\n", capture_output=True, text=True)
second = subprocess.run(["./commonmark"], input=upper + "\n", capture_output=True, text=True)
print(first.stdout)
assert first.returncode == 0
assert second.returncode == 0
assert chr(code_point) in first.stdout
assert first.stdout == second.stdout
=== END AC entities-hex-reference ===

=== AC entities-named-ampersand ===
Intent: The named ampersand reference round trips to the same escaped form.

import subprocess

reference = "&amp;"
result = subprocess.run(["./commonmark"], input="a " + reference + " b\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert reference in result.stdout
assert result.stdout.count("&amp;") == 1
=== END AC entities-named-ampersand ===

=== AC entities-unknown-stays-literal ===
Intent: An unknown entity name is literal text with its ampersand escaped.

import subprocess

result = subprocess.run(["./commonmark"], input="&MadeUpEntity;\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("&amp;") == 1
=== END AC entities-unknown-stays-literal ===

=== AC entities-nul-reference-replaced ===
Intent: The reference for code point zero decodes to the same output as a literal U+FFFD character.
Encoding: utf-8

import subprocess

reference = "&#0;"
replacement = chr(0xFFFD)
first = subprocess.run(["./commonmark"], input=reference + "\n", capture_output=True, text=True, encoding="utf-8")
second = subprocess.run(["./commonmark"], input=replacement + "\n", capture_output=True, text=True, encoding="utf-8")
print(first.stdout)
assert first.returncode == 0
assert second.returncode == 0
assert first.stdout == second.stdout
=== END AC entities-nul-reference-replaced ===

=== AC entities-inert-in-code-span ===
Intent: A reference inside a code span is not decoded, so its ampersand is escaped.

import subprocess

result = subprocess.run(["./commonmark"], input="`&amp;`\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("&amp;amp;") == 1
=== END AC entities-inert-in-code-span ===

## User Acceptance

- None.

## Guardrails

- Never recognize named references without a semicolon.
- Never let a decoded reference act as structure (emphasis, list marker, thematic break).
- Never decode references in code spans or code blocks.
- Do not skip, filter or reinterpret corpus examples.
