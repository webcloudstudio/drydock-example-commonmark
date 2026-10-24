# FEATURE: Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Implement the delimiter stack, flanking rules and the Appendix process-emphasis algorithm for emphasis and strong emphasis. |
| Depends On  | FEATURE-Entities.md |
| Provides    | delimiter stack, process_emphasis procedure |
| Consumes    | inline scanner loop |

## Purpose

Implement the Emphasis and strong emphasis section of the spec using the Appendix algorithm directly.

## Delimiter stack

- On a run of `*` or `_`, insert a text node holding the run and push a stack entry with: delimiter type, run length, original length, active flag, and `can_open` and `can_close`.
- The stack also accepts `[` and `![` entries so the links story reuses it.
- Flanking: a run is left-flanking when it is not followed by Unicode whitespace and either is not followed by punctuation, or is followed by punctuation and preceded by whitespace or punctuation. Right-flanking is the mirror. Line start and end count as whitespace. Punctuation means Unicode categories `P*` and `S*` via `unicodedata`.
- For `*`: `can_open` is left-flanking and `can_close` is right-flanking. For `_`: `can_open` is left-flanking and (not right-flanking or preceded by punctuation); `can_close` is right-flanking and (not left-flanking or followed by punctuation).

## process_emphasis(stack_bottom)

- Maintain `openers_bottom` per delimiter type, indexed by closer length mod 3 and whether the closer can also open.
- Find the first potential closer, then search back for a valid opener: same type, can open, and the multiple-of-3 rule satisfied (if either can both open and close, the sum of original lengths must not be a multiple of 3 unless both are).
- If found, use strong when both runs have length of at least 2, otherwise regular. Wrap the nodes between opener and closer, remove delimiters between them, and consume 1 or 2 characters from each side, removing empty entries.
- If not found, lower `openers_bottom`, drop the closer if it cannot open, and advance.
- At the end remove everything above `stack_bottom`. Leftover delimiters stay as literal text.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Emphasis and strong nodes in the inline tree.

## Programmatic Acceptance

The corpus section includes links in rule 9 and rule 17 examples, so it is gated in the images story. The checks here are bounded and structural.

=== AC emphasis-star-and-underscore ===
Intent: Single star and single underscore wrap supplied words in one em element each.

import subprocess

word = "wordy"
for mark in ("*", "_"):
    result = subprocess.run(["./commonmark"], input=mark + word + mark + "\n", capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<em>") == 1
    assert result.stdout.count("<strong>") == 0
    assert word in result.stdout
=== END AC emphasis-star-and-underscore ===

=== AC emphasis-strong ===
Intent: Doubled delimiters produce one strong element.

import subprocess

word = "wordy"
for mark in ("**", "__"):
    result = subprocess.run(["./commonmark"], input=mark + word + mark + "\n", capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<strong>") == 1
    assert result.stdout.count("<em>") == 0
=== END AC emphasis-strong ===

=== AC emphasis-intraword-rules ===
Intent: Intraword emphasis works with star but not with underscore.

import subprocess

star = subprocess.run(["./commonmark"], input="foo*bar*baz\n", capture_output=True, text=True)
under = subprocess.run(["./commonmark"], input="foo_bar_baz\n", capture_output=True, text=True)
print(star.stdout)
print(under.stdout)
assert star.returncode == 0
assert under.returncode == 0
assert star.stdout.count("<em>") == 1
assert under.stdout.count("<em>") == 0
=== END AC emphasis-intraword-rules ===

=== AC emphasis-flanking-whitespace ===
Intent: A delimiter run followed or preceded by whitespace does not form emphasis.

import subprocess

result = subprocess.run(["./commonmark"], input="a * foo bar*\n\nfoo bar *\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<em>") == 0
=== END AC emphasis-flanking-whitespace ===

=== AC emphasis-nesting ===
Intent: Triple delimiters give one em containing one strong, and nested forms keep both elements.

import subprocess

triple = subprocess.run(["./commonmark"], input="***word***\n", capture_output=True, text=True)
nested = subprocess.run(["./commonmark"], input="*a **b** c*\n", capture_output=True, text=True)
print(triple.stdout)
print(nested.stdout)
assert triple.returncode == 0
assert nested.returncode == 0
assert triple.stdout.count("<em>") == 1
assert triple.stdout.count("<strong>") == 1
assert nested.stdout.count("<em>") == 1
assert nested.stdout.count("<strong>") == 1
=== END AC emphasis-nesting ===

=== AC emphasis-code-span-binds-tighter ===
Intent: A star inside a code span cannot close emphasis.

import subprocess

result = subprocess.run(["./commonmark"], input="*foo`*`\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<em>") == 0
assert result.stdout.count("<code>") == 1
=== END AC emphasis-code-span-binds-tighter ===

## User Acceptance

- None.

## Guardrails

- Follow the Appendix algorithm; do not reinvent the emphasis rules or use backtracking.
- Never form empty emphasis.
- Do not skip, filter or reinterpret corpus examples.
