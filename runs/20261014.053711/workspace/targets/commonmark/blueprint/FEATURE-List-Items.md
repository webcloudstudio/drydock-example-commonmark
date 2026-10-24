# FEATURE: List Items

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse list items with bullet and ordered markers, content-offset indentation rules, empty items, start numbers and lazy continuation. |
| Depends On  | FEATURE-Setext-Headings.md |
| Provides    | list item container |
| Consumes    | block-type registry |

## Purpose

Implement the List items section of the spec as a registered container block. Grouping items into lists and tight or loose rendering belong to the lists story.

## Rules

- A bullet marker is `-`, `+` or `*`. An ordered marker is 1 to 9 digits followed by `.` or `)`. The marker may have up to three spaces of indentation. At least one space or tab must follow the marker unless the item is empty.
- Content offset W+N: W is the marker width and N is the number of spaces after it, if that is 1 to 4. If 5 or more spaces follow the marker and the rest of the line is not blank, the item starts with an indented code block and N is 1. If the rest of the line is blank, the item starts with a blank line and N is 1.
- Column-aware indentation with tab stop 4 is used throughout. Continuation lines must be indented at least W+N columns relative to the containing block. Blank lines continue the item.
- An item can begin with at most one blank line: a second consecutive blank line right after an empty marker ends the item.
- Interruption: when a list item would interrupt a paragraph, it must not start with a blank line, and an ordered item must start with number 1. A thematic break line is never a list item.
- Laziness: an unindented line that is paragraph continuation text stays in the item's open paragraph.
- Ordered items carry a start number (leading zeros allowed). Output is `<li>` elements; a loose item wraps paragraphs in `<p>`.

## Reads

- Lines handed to the block engine.

## Writes

- List item nodes in the block tree.

## Programmatic Acceptance

The corpus section examples need list grouping and tightness, so it is gated in the lists story. The checks here are bounded and avoid tight-list paragraph rendering.

=== AC items-bullet-items ===
Intent: Each bullet marker line starts one li element, and consecutive items of one marker form one ul.

import subprocess

items = ["first", "second", "third"]
source = "".join("- " + text + "\n" for text in items)
result = subprocess.run(["./commonmark"], input=source, capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<li>") == len(items)
assert result.stdout.count("<ul>") == 1
for text in items:
    assert text in result.stdout
=== END AC items-bullet-items ===

=== AC items-ordered-start-number ===
Intent: An ordered list takes its start number from the first item, and ten digits is not a marker.

import subprocess

number = 123456789
good = subprocess.run(["./commonmark"], input=str(number) + ". ok\n", capture_output=True, text=True)
bad = subprocess.run(["./commonmark"], input=str(number) + "0. not ok\n", capture_output=True, text=True)
print(good.stdout)
print(bad.stdout)
assert good.returncode == 0
assert bad.returncode == 0
assert ('start="' + str(number) + '"') in good.stdout
assert bad.stdout.count("<ol") == 0
=== END AC items-ordered-start-number ===

=== AC items-continuation-paragraph ===
Intent: A continuation paragraph indented to the content column joins the item, giving a loose item with two paragraphs.

import subprocess

result = subprocess.run(["./commonmark"], input="- one\n\n  two\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<li>") == 1
assert result.stdout.count("<p>") == 2
=== END AC items-continuation-paragraph ===

=== AC items-insufficient-indent-ends-item ===
Intent: A paragraph indented less than the content column is outside the item.

import subprocess

result = subprocess.run(["./commonmark"], input="- one\n\n two\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<li>") == 1
assert result.stdout.count("<p>") == 1
=== END AC items-insufficient-indent-ends-item ===

=== AC items-empty-items ===
Intent: Empty items are allowed in the middle of a list, but an empty item cannot interrupt a paragraph.

import subprocess

middle = subprocess.run(["./commonmark"], input="- foo\n-\n- bar\n", capture_output=True, text=True)
interrupt = subprocess.run(["./commonmark"], input="foo\n*\n", capture_output=True, text=True)
print(middle.stdout)
print(interrupt.stdout)
assert middle.returncode == 0
assert interrupt.returncode == 0
assert middle.stdout.count("<li>") == 2 + 1
assert interrupt.stdout.count("<li>") == 0
=== END AC items-empty-items ===

=== AC items-nested-and-code ===
Intent: A sublist indented to the content column nests, and a code block six spaces in is code inside the item.

import subprocess

nested = subprocess.run(["./commonmark"], input="- foo\n  - bar\n", capture_output=True, text=True)
code = subprocess.run(["./commonmark"], input="- foo\n\n      bar\n", capture_output=True, text=True)
print(nested.stdout)
print(code.stdout)
assert nested.returncode == 0
assert code.returncode == 0
assert nested.stdout.count("<ul>") == 2
assert code.stdout.count("<pre>") == 1
=== END AC items-nested-and-code ===

=== AC items-four-spaces-is-code ===
Intent: A marker indented four spaces is code, not a list item.

import subprocess

result = subprocess.run(["./commonmark"], input="    1.  A paragraph\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<ol") == 0
assert result.stdout.count("<pre>") == 1
=== END AC items-four-spaces-is-code ===

## User Acceptance

- None.

## Guardrails

- A marker must be followed by a space or tab unless the item is empty.
- An ordered list may interrupt a paragraph only when it starts at 1.
- Do not skip, filter or reinterpret corpus examples.
