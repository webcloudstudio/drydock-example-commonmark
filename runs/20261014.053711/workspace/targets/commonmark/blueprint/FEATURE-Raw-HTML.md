# FEATURE: Raw HTML

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse raw inline HTML tags, comments, processing instructions, declarations and CDATA sections and pass them through unescaped. |
| Depends On  | FEATURE-Block-Engine.md |
| Provides    | raw inline HTML construct |
| Consumes    | inline parser hook |

## Purpose

Implement the Raw HTML section of the spec.

## Grammar

- A tag name is an ASCII letter followed by letters, digits or hyphens.
- An attribute is whitespace (spaces, tabs, at most one line ending), an attribute name, and an optional value specification. An attribute name starts with a letter, `_` or `:` and continues with letters, digits, `_`, `.`, `:` or `-`.
- An unquoted value is nonempty and contains no whitespace, `"`, `'`, `=`, `<`, `>` or backtick. Quoted values use single or double quotes.
- An open tag is `<`, a tag name, attributes, optional whitespace (at most one line ending), an optional `/`, then `>`. A closing tag is `</`, a tag name, optional whitespace, then `>`, with no attributes.
- A comment is `<!-->`, `<!--->`, or `<!--` followed by text not containing `-->` and then `-->`. A processing instruction is `<?` to `?>`. A declaration is `<!`, an ASCII letter, then text up to `>`. CDATA is `<![CDATA[` to `]]>`.

## Rules

- A recognized tag is emitted unescaped and unchanged. Everything else is plain text with `<`, `>`, `&` and `"` escaped.
- Backslash escapes and entities are inert inside raw HTML, so the text is passed through byte for byte.
- Raw HTML binds as tightly as code spans and autolinks. It takes precedence over emphasis delimiters inside its attribute values.
- A line ending inside a tag is kept as written and never becomes a hard break.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Raw HTML nodes in the inline tree.

## Programmatic Acceptance

One corpus example in this section needs block quotes. The Raw HTML section is gated in the tabs story, so the checks here are bounded.

=== AC rawhtml-open-and-close-tags ===
Intent: Valid open, self-closing and closing tags in a paragraph pass through verbatim.

import subprocess

tags = '<a><bab><c2c> <a href="x" data-k=v /> </a></foo >'
result = subprocess.run(["./commonmark"], input="Foo " + tags + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert tags in result.stdout
=== END AC rawhtml-open-and-close-tags ===

=== AC rawhtml-comment-pi-declaration-cdata ===
Intent: Inline comments, processing instructions, declarations and CDATA pass through verbatim.

import subprocess

for fragment in ["<!-- a comment -->", "<?php echo $a; ?>", "<!ELEMENT br EMPTY>", "<![CDATA[>&<]]>"]:
    result = subprocess.run(["./commonmark"], input="foo " + fragment + " bar\n", capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert fragment in result.stdout
=== END AC rawhtml-comment-pi-declaration-cdata ===

=== AC rawhtml-illegal-forms-escaped ===
Intent: Illegal tag names are not raw HTML, so only the paragraph tags contribute angle brackets.

import subprocess

result = subprocess.run(["./commonmark"], input="<33> <__>\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<") == 2
assert result.stdout.count(">") == 2
=== END AC rawhtml-illegal-forms-escaped ===

=== AC rawhtml-closing-tag-with-attributes ===
Intent: A closing tag with attributes is not raw HTML, so no extra angle brackets appear in the output.

import subprocess

result = subprocess.run(["./commonmark"], input='</a href="foo">\n', capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<") == 2
=== END AC rawhtml-closing-tag-with-attributes ===

=== AC rawhtml-backslash-inert ===
Intent: A backslash inside a tag attribute value is preserved and not treated as an escape.

import subprocess

tag = '<a href="\\*">'
result = subprocess.run(["./commonmark"], input="foo " + tag + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert tag in result.stdout
=== END AC rawhtml-backslash-inert ===

## User Acceptance

- None.

## Guardrails

- Never process backslash escapes or entities inside recognized raw HTML.
- Never treat a tag-like string as raw HTML unless it matches the grammar completely.
- Do not skip, filter or reinterpret corpus examples.
