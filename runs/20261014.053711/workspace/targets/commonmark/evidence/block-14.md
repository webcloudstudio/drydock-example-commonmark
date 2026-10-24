# Evidence: Block 14 · Service (block-14)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4457
- execution id: 20261014.065812.667Z-3615fdb5

## Stories built
- Parse thematic breaks. (thematic-breaks) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Thematic-Breaks.md (SP 1277)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_thematic_breaks.py

## Pre-build acceptance observation
- RED: thematic-three-markers (FEATURE-Thematic-Breaks.md)
  intent: Lines of three or more matching marker characters each render one hr element.
  return code: 1
  stdout:
    <p>***</p>
    <p>---</p>
    <p>___</p>
    <p>_____________</p>
    <p>- - -</p>
    <p>**  * ** * ** * **</p>
  stderr:
    --- drydock: values at failure ---
      lines = ['***', '---', '___', '_____________', ' - - -', ' **  * ** * ** * **']
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>***</p>\n<p>---</p>\n<p>___</p>\n<p>_____________</p>\n<p>- - -</p>\n<p>**  * ** * ** * **</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "thematic-three-markers.py", line 8, in <module>
        assert result.stdout.count("<hr />") == len(lines)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): thematic-not-a-break (FEATURE-Thematic-Breaks.md)
  intent: Wrong characters, too few characters, mixed characters and trailing text do not produce hr elements.
  return code: 0
  stdout:
    <p>+++</p>
    <p>--</p>
    <p>_ _ _ _ a</p>
    <p>a------</p>
    <p><em>-</em></p>
- RED: thematic-interrupts-paragraph (FEATURE-Thematic-Breaks.md)
  intent: A thematic break directly after paragraph text splits it into two paragraphs around one hr.
  return code: 1
  stdout:
    <p>Foo
    ***
    bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>Foo\n***\nbar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "thematic-interrupts-paragraph.py", line 6, in <module>
        assert result.stdout.count("<hr />") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: thematic-trailing-whitespace (FEATURE-Thematic-Breaks.md)
  intent: Trailing spaces and tabs after the marker characters are allowed.
  return code: 1
  stdout:
    <p>- - - -</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>- - - -</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "thematic-trailing-whitespace.py", line 6, in <module>
        assert result.stdout.count("<hr />") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: thematic-three-markers (FEATURE-Thematic-Breaks.md)
  intent: Lines of three or more matching marker characters each render one hr element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <hr />
    <hr />
    <hr />
    <hr />
    <hr />
    <hr />
- PASS: thematic-not-a-break (FEATURE-Thematic-Breaks.md)
  intent: Wrong characters, too few characters, mixed characters and trailing text do not produce hr elements.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>+++</p>
    <p>--</p>
    <p>_ _ _ _ a</p>
    <p>a------</p>
    <p><em>-</em></p>
- PASS: thematic-interrupts-paragraph (FEATURE-Thematic-Breaks.md)
  intent: A thematic break directly after paragraph text splits it into two paragraphs around one hr.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo</p>
    <hr />
    <p>bar</p>
- PASS: thematic-trailing-whitespace (FEATURE-Thematic-Breaks.md)
  intent: Trailing spaces and tabs after the marker characters are allowed.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <hr />

## Build summary
Baseline is green (649 passed, 1 skipped). Now I'll add the thematic-break block type as a registered start rule in `blocks.py`.Now the tests: the four declared acceptance checks transcribed unchanged, plus block-tree and exact-output tests for the boundaries.One existing test pins the default registry to zero start rules, which this step intentionally changes. Let me look at it.Now the full project suite, run in the background since it takes about two minutes.Thematic breaks now parse and render as `<hr />`. The full project suite passes: 687 passed, 1 skipped (the skip was already there before this change).

I did not run `sources/full_test.sh`. The feature's acceptance is gated on the lists story, and the conformance corpus needs lists and setext headings.

**What changed**
- `mdparser/blocks.py`: a new `thematic_break` block type with a start rule. It accepts up to three spaces of indentation, then three or more matching `*`, `-` or `_`, with spaces or tabs allowed between and after, and nothing else. It is registered in `DEFAULT_REGISTRY`, so it takes precedence over paragraph text, and it closes on the next line.
- `mdparser/render.py`: renders the block as `<hr />\n`.
- `tests/test_thematic_breaks.py` (new): the four declared checks transcribed with their assertions unchanged, plus boundary tests for marker counts, indentation, mixed and trailing characters, paragraph interaction, and exact output.
- `tests/test_blocks.py`: one existing test asserted the default registry had no start rules. That is now false by design, so I changed it to expect exactly the thematic-break rule. I did not weaken any declared assertion.

**Choices I made**
- The start rule lives in `blocks.py` next to `PARAGRAPH`, following the existing pattern, rather than in a new module.
- The setext precedence and list precedence are not wired, as the spec says; they belong to the later stories.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_thematic_breaks.py

SUMMARY:
Added the thematic-break block type as a registered start rule, rendered it as `<hr />`, and added tests. Declared acceptance checks (thematic-three-markers, thematic-not-a-break, thematic-interrupts-paragraph, thematic-trailing-whitespace) are transcribed in `tests/test_thematic_breaks.py` and pass. Full pytest run: 687 passed, 1 skipped (pre-existing skip). Baseline before the change was 649 passed, 1 skipped. Conformance corpus (`sources/full_test.sh`) was not run because this step's criteria gate it in the lists story.
