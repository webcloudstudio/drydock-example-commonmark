# FEATURE: Code Spans

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse code spans and establish the left-to-right inline scanner with code, autolink and raw HTML precedence. |
| Depends On  | FEATURE-Autolinks.md, FEATURE-Raw-HTML.md |
| Provides    | code span inline construct, inline scanner loop |
| Consumes    | autolink inline construct, raw inline HTML construct |

## Purpose

Implement the Code spans and Inlines sections of the spec, and the inline scanner loop that later inline stories extend.

## Rules

- The scanner walks the text left to right. At a backtick, `<` or other special character it tries the matching construct; the first construct that matches wins.
- A backtick string is a maximal run of backticks. A code span opens at a backtick string and closes at the next backtick string of exactly the same length. If none exists, the opening run is literal text.
- Content normalization: convert line endings to spaces; then, if the content both begins and ends with a space and is not entirely spaces, remove one space from each end. Only U+0020 counts, not other whitespace. Interior spaces are not collapsed.
- Content is HTML-escaped. Backslash escapes and entities are inert inside code spans.
- Code spans, raw HTML and autolinks have equal precedence: whichever starts first is parsed first. Bracket and emphasis handling is lower precedence and is added by later stories.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Code nodes in the inline tree.

## Programmatic Acceptance

The Precedence section needs lists and is gated in the lists story.

=== AC codespans-corpus-sections ===
Intent: The Code spans and Inlines conformance sections (23 cases) pass in full.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import os
import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.getcwd() + "/commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "^Code spans$|^Inlines$",
    ],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC codespans-corpus-sections ===

=== AC codespans-simple ===
Intent: A single-backtick span renders one code element containing the supplied content.

import subprocess

content = "some code"
result = subprocess.run(["./commonmark"], input="`" + content + "`\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<code>") == 1
assert content in result.stdout
=== END AC codespans-simple ===

=== AC codespans-backtick-length-match ===
Intent: A double-backtick span may contain a single backtick, which is kept inside one code element.

import subprocess

inner = "a`b"
result = subprocess.run(["./commonmark"], input="``" + inner + "``\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<code>") == 1
assert inner in result.stdout
=== END AC codespans-backtick-length-match ===

=== AC codespans-unclosed-literal ===
Intent: An unmatched backtick run is literal text and produces no code element.

import subprocess

result = subprocess.run(["./commonmark"], input="```foo``\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<code>") == 0
=== END AC codespans-unclosed-literal ===

=== AC codespans-escapes-inert ===
Intent: A backslash inside a code span is kept literally.

import subprocess

content = "\\["
result = subprocess.run(["./commonmark"], input="`" + content + "`\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<code>") == 1
assert content in result.stdout
=== END AC codespans-escapes-inert ===

## User Acceptance

- None.

## Guardrails

- Never strip more than one leading and one trailing space, and never strip when the content is entirely spaces.
- Never process escapes, entities or emphasis inside a code span.
- Do not skip, filter or reinterpret corpus examples.
