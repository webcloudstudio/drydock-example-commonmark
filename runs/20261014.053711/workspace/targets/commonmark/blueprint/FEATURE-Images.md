# FEATURE: Images

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Render images with plain-text alt attributes and verify links, images and emphasis against the conformance corpus. |
| Depends On  | FEATURE-Links.md |
| Provides    | image rendering |
| Consumes    | look_for_link_or_image procedure |

## Purpose

Implement the Images section of the spec on top of the shared link machinery, and gate the Emphasis, Links and Images corpus sections, which are all satisfiable once images exist.

## Rules

- An image description starts with `![` and follows the same bracket rules as link text, except it may contain links.
- All four forms apply: inline, full reference, collapsed and shortcut.
- Render `<img src="..." alt="..." />` with ` title="..."` only when a title exists. The src is percent-encoded and HTML-escaped like a link href.
- The alt value is the plain-text content of the description: emphasis, links and nested images are reduced to their text content (nested images contribute their own alt), code spans contribute their content, and the result is HTML-escaped.
- `\![foo]` is a literal `!` followed by a link; `!\[foo]` is literal text.

## Reads

- The inline tree built by the links story, the reference map.

## Writes

- Image nodes in the inline tree.

## Programmatic Acceptance

The Link reference definitions section is gated in the tabs story because its examples need headings and quotes.

=== AC images-corpus-sections ===
Intent: The Emphasis and strong emphasis, Links and Images conformance sections (roughly 240 cases) pass in full.
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
        "^Emphasis and strong emphasis$|^Links$|^Images$",
    ],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC images-corpus-sections ===

=== AC images-inline-image ===
Intent: An inline image renders one img element carrying the supplied src, alt and title.

import subprocess

alt = "my alt"
src = "/path/pic.jpg"
title = "a title"
source = "![" + alt + "](" + src + ' "' + title + '")\n'
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<img ") == 1
assert ('src="' + src + '"') in result.stdout
assert ('alt="' + alt + '"') in result.stdout
assert ('title="' + title + '"') in result.stdout
=== END AC images-inline-image ===

=== AC images-alt-is-plain-text ===
Intent: Emphasis inside an image description does not appear as markup in the alt attribute.

import subprocess

result = subprocess.run(["./commonmark"], input="![foo *bar*](/u)\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<img ") == 1
assert result.stdout.count("<em>") == 0
=== END AC images-alt-is-plain-text ===

=== AC images-reference-forms ===
Intent: Full, collapsed and shortcut image references each resolve against a definition.

import subprocess

definition = "\n\n[foo]: /url\n"
for use in ("![text][foo]", "![foo][]", "![foo]"):
    result = subprocess.run(["./commonmark"], input=use + definition, capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<img ") == 1
=== END AC images-reference-forms ===

=== AC images-inside-link ===
Intent: An image inside a link produces one a element containing one img element.

import subprocess

result = subprocess.run(["./commonmark"], input="[![moon](moon.jpg)](/uri)\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 1
assert result.stdout.count("<img ") == 1
=== END AC images-inside-link ===

## User Acceptance

- None.

## Guardrails

- The alt attribute must contain plain text only, never markup.
- Do not skip, filter or reinterpret corpus examples.
