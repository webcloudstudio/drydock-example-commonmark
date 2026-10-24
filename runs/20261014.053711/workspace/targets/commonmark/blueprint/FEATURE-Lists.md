# FEATURE: Lists

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Group list items into lists, compute tight and loose rendering, and gate the block-structure corpus sections. |
| Depends On  | FEATURE-List-Items.md |
| Provides    | list container, tight/loose computation |
| Consumes    | list item container |

## Purpose

Implement the Lists section of the spec, and gate the block-structure sections whose examples need lists.

## Rules

- Consecutive items of the same type form one list. Two items are of the same type if both are bullets with the same character, or both are ordered with the same delimiter. Changing the bullet character or the ordered delimiter starts a new list.
- The start number of an ordered list is that of its first item. The `start` attribute is emitted only when it is not 1.
- Items may be separated by any number of blank lines. Items need not be indented identically, as long as none is indented enough to be inside the previous item.
- A list can interrupt a paragraph; an ordered list does so only if it starts at 1.
- A list is loose if any two of its items are separated by a blank line, or if any item directly contains two block children with a blank line between them. Otherwise it is tight. Blank lines inside fenced code, inside a nested list's own children, or inside a block quote do not make the outer list loose. Link reference definitions do not count as blocks for this purpose.
- In a tight list the paragraphs of the items render without `<p>` tags. In a loose list they render with them. Nested lists decide their own tightness.

## Reads

- List item nodes from the block tree.

## Writes

- List nodes and the tight flag in the block tree.

## Programmatic Acceptance

=== AC lists-corpus-sections ===
Intent: The Lists, List items, Block quotes, Thematic breaks, ATX headings, Setext headings, Indented code blocks, Fenced code blocks and Precedence conformance sections (roughly 300 cases) pass in full.
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
        "^Lists$|^List items$|^Block quotes$|^Thematic breaks$|^ATX headings$|^Setext headings$|^Indented code blocks$|^Fenced code blocks$|^Precedence$",
    ],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC lists-corpus-sections ===

=== AC lists-changing-marker-starts-new-list ===
Intent: Changing the bullet character or ordered delimiter starts a new list.

import subprocess

bullets = subprocess.run(["./commonmark"], input="- foo\n- bar\n+ baz\n", capture_output=True, text=True)
ordered = subprocess.run(["./commonmark"], input="1. foo\n2. bar\n3) baz\n", capture_output=True, text=True)
print(bullets.stdout)
print(ordered.stdout)
assert bullets.returncode == 0
assert ordered.returncode == 0
assert bullets.stdout.count("<ul>") == 2
assert ordered.stdout.count("<ol") == 2
=== END AC lists-changing-marker-starts-new-list ===

=== AC lists-tight-versus-loose ===
Intent: Items without blank lines are tight, and a blank line between items makes the list loose.

import subprocess

tight = subprocess.run(["./commonmark"], input="- a\n- b\n", capture_output=True, text=True)
loose = subprocess.run(["./commonmark"], input="- a\n\n- b\n", capture_output=True, text=True)
print(tight.stdout)
print(loose.stdout)
assert tight.returncode == 0
assert loose.returncode == 0
assert tight.stdout.count("<p>") == 0
assert loose.stdout.count("<p>") == 2
=== END AC lists-tight-versus-loose ===

=== AC lists-blank-inside-item-makes-loose ===
Intent: A blank line between two paragraphs of one item makes the whole list loose.

import subprocess

result = subprocess.run(["./commonmark"], input="- a\n- b\n\n  c\n- d\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 4
=== END AC lists-blank-inside-item-makes-loose ===

=== AC lists-blank-in-code-stays-tight ===
Intent: Blank lines inside a fenced code block do not make a list loose.

import subprocess

result = subprocess.run(
    ["./commonmark"], input="- a\n- ```\n  b\n\n\n  ```\n- c\n", capture_output=True, text=True
)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<p>") == 0
assert result.stdout.count("<pre>") == 1
=== END AC lists-blank-in-code-stays-tight ===

=== AC lists-interrupt-paragraph ===
Intent: A bullet list interrupts a paragraph, and an ordered list does so only when it starts at one.

import subprocess

bullet = subprocess.run(["./commonmark"], input="Foo\n- bar\n- baz\n", capture_output=True, text=True)
one = subprocess.run(["./commonmark"], input="Intro\n1. item\n", capture_output=True, text=True)
other = subprocess.run(["./commonmark"], input="Intro\n14. item\n", capture_output=True, text=True)
print(bullet.stdout)
print(one.stdout)
print(other.stdout)
assert bullet.returncode == 0
assert one.returncode == 0
assert other.returncode == 0
assert bullet.stdout.count("<ul>") == 1
assert one.stdout.count("<ol") == 1
assert other.stdout.count("<ol") == 0
=== END AC lists-interrupt-paragraph ===

## User Acceptance

- None.

## Guardrails

- Looseness is decided per list, never inherited from a nested or enclosing list.
- Do not skip, filter or reinterpret corpus examples.
