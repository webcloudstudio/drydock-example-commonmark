# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5130
- execution id: 20261014.061513.130Z-7ed6f384

## Stories built
- Decode HTML5 named, decimal and hexadecimal character references. (entities) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Entities.md (SP 1874)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/entities.py
- mdparser/inlines.py
- tests/test_entities.py

## Pre-build acceptance observation
- RED: entities-decimal-reference (FEATURE-Entities.md)
  intent: A decimal reference decodes to the character with the bound code point.
  return code: 1
  stdout:
    <p>x &amp;#65; y</p>
  stderr:
    --- drydock: values at failure ---
      code_point = 65
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>x &amp;#65; y</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "entities-decimal-reference.py", line 7, in <module>
        assert chr(code_point) in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: entities-hex-reference (FEATURE-Entities.md)
  intent: Lowercase and uppercase hexadecimal references decode to the same character.
  return code: 1
  stdout:
    <p>&amp;#x42;</p>
  stderr:
    --- drydock: values at failure ---
      code_point = 66
      first = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&amp;#x42;</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "entities-hex-reference.py", line 11, in <module>
        assert chr(code_point) in first.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): entities-named-ampersand (FEATURE-Entities.md)
  intent: The named ampersand reference round trips to the same escaped form.
  return code: 0
  stdout:
    <p>a &amp;amp; b</p>
- GREEN (prepassed): entities-unknown-stays-literal (FEATURE-Entities.md)
  intent: An unknown entity name is literal text with its ampersand escaped.
  return code: 0
  stdout:
    <p>&amp;MadeUpEntity;</p>
- RED: entities-nul-reference-replaced (FEATURE-Entities.md)
  intent: The reference for code point zero decodes to the same output as a literal U+FFFD character.
  return code: 1
  stdout:
    <p>&amp;#0;</p>
  stderr:
    --- drydock: values at failure ---
      first = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&amp;#0;</p>\n', stderr='')
      second = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>�</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "entities-nul-reference-replaced.py", line 10, in <module>
        assert first.stdout == second.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): entities-inert-in-code-span (FEATURE-Entities.md)
  intent: A reference inside a code span is not decoded, so its ampersand is escaped.
  return code: 0
  stdout:
    <p><code>&amp;amp;</code></p>

## Post-build programmatic acceptance
- PASS: entities-decimal-reference (FEATURE-Entities.md)
  intent: A decimal reference decodes to the character with the bound code point.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>x A y</p>
- PASS: entities-hex-reference (FEATURE-Entities.md)
  intent: Lowercase and uppercase hexadecimal references decode to the same character.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>B</p>
- PASS: entities-named-ampersand (FEATURE-Entities.md)
  intent: The named ampersand reference round trips to the same escaped form.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>a &amp; b</p>
- PASS: entities-unknown-stays-literal (FEATURE-Entities.md)
  intent: An unknown entity name is literal text with its ampersand escaped.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>&amp;MadeUpEntity;</p>
- PASS: entities-nul-reference-replaced (FEATURE-Entities.md)
  intent: The reference for code point zero decodes to the same output as a literal U+FFFD character.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>�</p>
- PASS: entities-inert-in-code-span (FEATURE-Entities.md)
  intent: A reference inside a code span is not decoded, so its ampersand is escaped.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>&amp;amp;</code></p>

## Build summary
I'll start by checking the build directory and the existing application files.The earlier blocks are already built. Next I'll look at the existing `mdparser` package, tests, and whether an entities module exists yet.The package already has `unescape` and `ASCII_PUNCTUATION` in `entities.py`, and the inline loop escapes `&` as plain text. Before changing anything I'll record the baseline test result so any regression is visible.Baseline is green: 358 tests pass. I'll read the two files I need to edit so the edit tool accepts them.Now I'll write the entity decoder into `entities.py`, keeping the existing `unescape` and `ASCII_PUNCTUATION` unchanged.Next, I'll hook the reference decoder into the inline loop as a plain-text branch, so decoded characters are escaped and never treated as markup.I'll also mention the reference rule in the `parse_inline` docstring so it matches the module's existing style.Before writing tests, a quick smoke check of the executable and the two-codepoint entity.The output matches the spec rules. Now I'll write `tests/test_entities.py`. It transcribes the six declared acceptance checks and adds finer tests that compare exact returned strings and exact stdout.Before running, I checked several expected values by hand and found three mistakes in my own test file: two reference end offsets are off by one (`&#0000065;` is 10 characters, not 11), and `&AMP;` is actually in the HTML5 table, so it is not a good case-sensitivity example. I'll fix those and clarify one misnamed test.Now I'll run the new entity tests, then the full project suite to check for regressions in the earlier blocks.All 419 tests pass: the 358 existing tests plus 61 new ones. I'll confirm the changed-file set and that no staged assets were touched.Block 8 (entities) is implemented. The full project suite passes, 419 tests, and I did not run the conformance runner because no criterion in this block invokes it.

**What changed**

- `mdparser/entities.py`: added `match_reference`, which decodes HTML5 named references (semicolon-terminated names only, looked up in `html.entities.html5`), 1–7 digit decimal references, and 1–6 digit hex references. Zero, surrogates and values above U+10FFFF become U+FFFD. I also added `unescape_and_decode`, the shared helper for destinations, titles and info strings. The existing `unescape` and `ASCII_PUNCTUATION` are unchanged.
- `mdparser/inlines.py`: the inline loop now has an `&` branch. A recognized reference is decoded and its character is HTML-escaped as plain text, so `&#42;` cannot open emphasis and `&#35;` cannot start a heading. Code spans already keep `&` literal, so they are unaffected.
- `tests/test_entities.py`: new. It transcribes all six declared acceptance checks, then adds finer tests for named, decimal and hex references, boundaries (7 vs 8 decimal digits, 6 vs 7 hex digits, the last valid code point), invalid code points, decoded text as plain text, and the helper's single-pass behaviour.

**Choices I made**

- `unescape_and_decode` runs backslash escapes and references in one left-to-right pass. Two separate passes would turn `\&amp;` into `&` when it should stay the literal text `&amp;`.
- Tests compare exact returned strings and exact stdout bytes, not substrings.

**Not done in this block**

- The corpus-level conformance check for entities is gated in a later block, so I did not invoke `sources/full_test.sh`.
- The helper `unescape_and_decode` has no caller yet. The destination, title and info-string stories will call it when they are built.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/entities.py
- mdparser/inlines.py
- tests/test_entities.py

SUMMARY:
Implemented HTML5 named, decimal and hexadecimal character reference decoding. Entity references decode in the inline loop as escaped plain text, are inert in code spans, and are exposed through the shared `unescape_and_decode` helper for later stories. Test runs: `pytest -q` over the whole project, 419 passed (358 existing, 61 new in `tests/test_entities.py`, including all six declared acceptance checks). Staged `sources/` assets are untouched. The conformance runner was not invoked because no criterion in this block calls it.

<blueprint-decisions>
[{"spec":"FEATURE-Entities.md","severity":"Low","subject":"Shared destination/title/info-string helper design","decision":"The spec asks for a shared helper but does not define its shape. I added `unescape_and_decode` in `mdparser/entities.py`, a single left-to-right pass that applies backslash escapes and character references together, so an escaped ampersand is not re-read as a reference. The existing backslash-only `unescape` is kept unchanged. Is that acceptable, or should the helper be split into two passes?"}]
</blueprint-decisions>
