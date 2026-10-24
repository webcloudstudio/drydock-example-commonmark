# FEATURE: Fenced Code

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse fenced code blocks delimited by backtick or tilde fences with info strings and indentation stripping. |
| Depends On  | FEATURE-Indented-Code.md |
| Provides    | fenced code block |
| Consumes    | block-type registry, shared unescape and entity helpers |

## Purpose

Implement the Fenced code blocks section of the spec.

## Rules

- An opening fence is at least three consecutive backticks or tildes, with up to three spaces of indentation. Backtick and tilde fences cannot be mixed. The text after the fence is the info string, trimmed. For a backtick fence the info string must not contain a backtick; otherwise the line is not a fence (it is parsed as a paragraph with a code span).
- Content is all following lines until a closing fence of the same character, at least as long as the opening one, with up to three spaces of indentation and followed only by spaces or tabs. Closing fences have no info string.
- If the opening fence is indented by N spaces, up to N spaces of indentation are removed from each content line.
- An unclosed fence runs to the end of the document or the enclosing container.
- A fenced code block can interrupt a paragraph and needs no blank lines around it.
- The first word of the info string, after backslash unescape and entity decoding, becomes `class="language-WORD"` on the code element. Content is HTML-escaped and never parsed.

## Reads

- Lines handed to the block engine.

## Writes

- Code block nodes in the block tree.

## Programmatic Acceptance

The corpus section examples use quotes, lists and setext headings, so it is gated in the lists story. The checks here are bounded.

=== AC fenced-backtick-and-tilde ===
Intent: Backtick and tilde fences each render one pre element containing the supplied body.

import subprocess

body = "some body text"
for fence in ("```", "~~~"):
    source = fence + "\n" + body + "\n" + fence + "\n"
    result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert body in result.stdout
=== END AC fenced-backtick-and-tilde ===

=== AC fenced-info-string-language-class ===
Intent: The first word of the info string becomes the language class.

import subprocess

language = "ruby"
source = "```" + language + " extra words\ncode\n```\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert ('class="language-' + language + '"') in result.stdout
=== END AC fenced-info-string-language-class ===

=== AC fenced-closing-fence-rules ===
Intent: A fence of the other character, or a shorter fence, does not close the block.

import subprocess

other = "~~~"
shorter = "```"
source = "````\naaa\n" + other + "\n" + shorter + "\n"
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert other in result.stdout
assert shorter in result.stdout
=== END AC fenced-closing-fence-rules ===

=== AC fenced-unclosed-runs-to-end ===
Intent: An unclosed fence consumes the rest of the document as code.

import subprocess

trailing = "still code"
result = subprocess.run(["./commonmark"], input="```\nfirst\n\n" + trailing + "\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert result.stdout.count("<p>") == 0
assert trailing in result.stdout
=== END AC fenced-unclosed-runs-to-end ===

=== AC fenced-interrupts-paragraph ===
Intent: A fence interrupts a paragraph and text after it starts a new paragraph.

import subprocess

result = subprocess.run(["./commonmark"], input="foo\n```\nbar\n```\nbaz\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert result.stdout.count("<p>") == 2
=== END AC fenced-interrupts-paragraph ===

=== AC fenced-two-backticks-not-a-fence ===
Intent: Two backticks do not open a fence; they form a code span instead.

import subprocess

result = subprocess.run(["./commonmark"], input="``\nfoo\n``\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 0
assert result.stdout.count("<code>") == 1
=== END AC fenced-two-backticks-not-a-fence ===

=== AC fenced-indentation-stripped ===
Intent: Content indentation up to the fence indentation is removed, and unindented lines are kept.

import subprocess

result = subprocess.run(["./commonmark"], input=" ```\n aaa\naaa\n```\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<pre>") == 1
assert result.stdout.count("aaa") == 2
assert result.stdout.count(" aaa") == 0
=== END AC fenced-indentation-stripped ===

## User Acceptance

- None.

## Guardrails

- Never parse fenced content as Markdown.
- Never let a closing fence carry an info string.
- Do not skip, filter or reinterpret corpus examples.
