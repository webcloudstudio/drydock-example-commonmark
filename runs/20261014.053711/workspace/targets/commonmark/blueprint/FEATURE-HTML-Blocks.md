# FEATURE: HTML Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse the seven kinds of HTML block and emit their lines as raw HTML. |
| Depends On  | FEATURE-Fenced-Code.md |
| Provides    | HTML block |
| Consumes    | block-type registry |

## Purpose

Implement the HTML blocks section of the spec.

## Start and end conditions

After up to three spaces of indentation:

1. Line begins with `<pre`, `<script`, `<style` or `<textarea` (case-insensitive) followed by a space, tab, `>` or end of line. Ends at a line containing `</pre>`, `</script>`, `</style>` or `</textarea>` (case-insensitive, need not match the start tag).
2. Begins with `<!--`. Ends at a line containing `-->`.
3. Begins with `<?`. Ends at a line containing `?>`.
4. Begins with `<!` and an ASCII letter. Ends at a line containing `>`.
5. Begins with `<![CDATA[`. Ends at a line containing `]]>`.
6. Begins with `<` or `</` and one of the block-level tag names listed in the spec (case-insensitive), followed by a space, tab, end of line, `>` or `/>`. Ends before the next blank line.
7. Begins with a complete open tag (tag name not `pre`, `script`, `style` or `textarea`) or complete closing tag alone on the line, followed only by spaces and tabs. Ends before the next blank line.

## Rules

- If the first line also meets the end condition, the block is that single line. Types 1 to 5 include the line holding the end condition, with anything after the end tag.
- Blocks end at the end of the document or enclosing container if no end condition is met.
- Types 1 to 6 can interrupt a paragraph. Type 7 cannot.
- Lines are emitted unchanged and unescaped, with their original indentation. Content inside the block is never parsed as Markdown, and tags inside it never change parser state.

## Reads

- Lines handed to the block engine.

## Writes

- HTML block nodes in the block tree.

## Programmatic Acceptance

The corpus section has examples that use quotes, lists and indented code, so it is gated in the tabs story. The checks here are bounded.

=== AC htmlblock-type6-raw-lines ===
Intent: A block-level tag block passes through verbatim and its Markdown is not parsed.

import subprocess

block = "<div>\n*foo*\n</div>"
result = subprocess.run(["./commonmark"], input=block + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert block in result.stdout
assert result.stdout.count("<em>") == 0
assert result.stdout.count("<p>") == 0
=== END AC htmlblock-type6-raw-lines ===

=== AC htmlblock-type6-ends-at-blank-line ===
Intent: A type 6 block ends at a blank line and Markdown after it is parsed.

import subprocess

result = subprocess.run(["./commonmark"], input="<div>\nraw\n\n*bar*\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
assert result.stdout.count("<em>") == 1
=== END AC htmlblock-type6-ends-at-blank-line ===

=== AC htmlblock-comment-spans-blank-lines ===
Intent: A comment block keeps blank lines until its end marker, and the following line is a paragraph.

import subprocess

comment = "<!-- Foo\n\nbar\n   baz -->"
result = subprocess.run(["./commonmark"], input=comment + "\nokay\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert comment in result.stdout
assert result.stdout.count("<p>") == 1
=== END AC htmlblock-comment-spans-blank-lines ===

=== AC htmlblock-pre-spans-blank-lines ===
Intent: A pre block keeps blank lines and does not parse the Markdown inside it.

import subprocess

block = "<pre>\n*x*\n\n_y_\n</pre>"
result = subprocess.run(["./commonmark"], input=block + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert block in result.stdout
assert result.stdout.count("<em>") == 0
=== END AC htmlblock-pre-spans-blank-lines ===

=== AC htmlblock-type7-cannot-interrupt ===
Intent: A lone open tag line after paragraph text stays inside the paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input='Foo\n<a href="bar">\nbaz\n', capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
=== END AC htmlblock-type7-cannot-interrupt ===

=== AC htmlblock-type6-interrupts-paragraph ===
Intent: A block-level tag line interrupts a paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="Foo\n<div>\nbar\n</div>\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 1
=== END AC htmlblock-type6-interrupts-paragraph ===

=== AC htmlblock-four-space-indent-is-code ===
Intent: Four spaces of indentation make an indented code block, not an HTML block.

import subprocess

result = subprocess.run(["./commonmark"], input="    <!-- foo -->\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
=== END AC htmlblock-four-space-indent-is-code ===

## User Acceptance

- None.

## Guardrails

- Never escape or alter lines inside an HTML block.
- Type 7 must never interrupt a paragraph.
- Do not skip, filter or reinterpret corpus examples.
