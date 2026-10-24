# Evidence: Block 13 · Service (block-13)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4933
- execution id: 20261014.064927.125Z-407c8dc1

## Stories built
- Implement hard and soft line breaks and plain textual content. (line-breaks-text) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Line-Breaks-Text.md (SP 1727)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/inlines.py
- tests/test_line_breaks.py

## Pre-build acceptance observation
- GREEN (prepassed): breaks-corpus-sections (FEATURE-Line-Breaks-Text.md)
  intent: The Soft line breaks and Textual content conformance sections (5 cases) pass in full.
  return code: 0
  stdout:
    5 passed, 0 failed, 0 errored, 650 skipped
- RED: breaks-hard-break-spaces (FEATURE-Line-Breaks-Text.md)
  intent: Two or more trailing spaces before a line ending give one br element between the two lines.
  return code: 1
  stdout:
    <p>alpha   
    beta</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>alpha   \nbeta</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "breaks-hard-break-spaces.py", line 8, in <module>
        assert result.stdout.count("<br />") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: breaks-hard-break-backslash (FEATURE-Line-Breaks-Text.md)
  intent: A backslash before a line ending gives one br element.
  return code: 1
  stdout:
    <p>alpha\
    beta</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>alpha\\\nbeta</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "breaks-hard-break-backslash.py", line 6, in <module>
        assert result.stdout.count("<br />") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): breaks-soft-break (FEATURE-Line-Breaks-Text.md)
  intent: A plain line ending is not a hard break and both lines stay in one paragraph.
  return code: 0
  stdout:
    <p>alpha
    beta</p>
- GREEN (prepassed): breaks-none-at-block-end (FEATURE-Line-Breaks-Text.md)
  intent: Trailing spaces or a trailing backslash at the end of a paragraph do not create a break.
  return code: 0
  stdout:
    <p>alpha</p>
    
    <p>alpha\</p>
- GREEN (prepassed): breaks-inert-in-code-span (FEATURE-Line-Breaks-Text.md)
  intent: Trailing spaces before a line ending inside a code span do not create a break.
  return code: 0
  stdout:
    <p><code>code   span</code></p>

## Post-build programmatic acceptance
- PASS: breaks-corpus-sections (FEATURE-Line-Breaks-Text.md)
  intent: The Soft line breaks and Textual content conformance sections (5 cases) pass in full.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    5 passed, 0 failed, 0 errored, 650 skipped
- PASS: breaks-hard-break-spaces (FEATURE-Line-Breaks-Text.md)
  intent: Two or more trailing spaces before a line ending give one br element between the two lines.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>alpha<br />
    beta</p>
- PASS: breaks-hard-break-backslash (FEATURE-Line-Breaks-Text.md)
  intent: A backslash before a line ending gives one br element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>alpha<br />
    beta</p>
- PASS: breaks-soft-break (FEATURE-Line-Breaks-Text.md)
  intent: A plain line ending is not a hard break and both lines stay in one paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>alpha
    beta</p>
- PASS: breaks-none-at-block-end (FEATURE-Line-Breaks-Text.md)
  intent: Trailing spaces or a trailing backslash at the end of a paragraph do not create a break.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>alpha</p>
    
    <p>alpha\</p>
- PASS: breaks-inert-in-code-span (FEATURE-Line-Breaks-Text.md)
  intent: Trailing spaces before a line ending inside a code span do not create a break.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>code   span</code></p>

## Build summary
The inline scanner in `mdparser/inlines.py` has no line-break handling yet, and paragraph text keeps its interior newlines and trailing spaces. I'll add the break branches to the scan loop, then write the tests.Scoped corpus gate passes (5 passed, 0 failed). Next I'll match the existing test style for the acceptance checks and the finer tests.Baseline is green (612 passed, 1 skipped). Now the tests file, with the six declared acceptance checks transcribed as written and finer tests that compare exact returned or emitted HTML.Two failures, both from my tests calling `parse_inline` directly on input the block layer normally cleans up first. The first is a real gap: the spec says leading spaces on the next line are dropped as part of the break rule, so the inline scanner should not depend on the block layer for that. I'll fix that in the scanner. The second is a test-level mistake: trailing-space stripping belongs to paragraph finalization, so I'll test it through the executable instead. (The file change notice was my own `sed` rename.)All 37 new tests and the related existing suites pass. Now I'll run the full project suite, the scoped gate with its real exit status, and confirm no staged assets changed.The line-break and text story is built. The scoped conformance gate passes, and the full project test suite is green at 649 passed, 1 skipped.

Hard breaks, soft breaks, and plain text now work in `mdparser/inlines.py`. A line ending preceded by two or more spaces or a backslash renders `<br />` plus a line ending. Any other line ending is a soft break, with spaces before it dropped. Breaks are inert inside code spans and raw HTML tags, and at the end of a block they do nothing.

- **Gate:** `^Soft line breaks$|^Textual content$` gives 5 passed, 0 failed, exit 0. The unfiltered `sources/full_test.sh` was not run, since this step does not declare it.
- **Tests:** `tests/test_line_breaks.py` has 37 tests. The six declared acceptance checks are transcribed as written, and the rest compare exact HTML from the inline parser and the executable.
- **Staged assets:** untouched.

Choices I made that you may want to redirect:
- The inline scanner drops the spaces that begin the next line itself, rather than relying only on the block layer. This is what the spec's break rule says.
- Trailing spaces at the end of a paragraph are still dropped by the block layer, not by the inline parser.
- In image alt text, a break becomes a plain line ending, which matches how the spec's reference renderer handles it.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/inlines.py
- tests/test_line_breaks.py

SUMMARY:
Added hard-break, soft-break and plain-text handling to the inline scanner, with helpers `_hard_break`, `_soft_break`, `_skip_spaces` and `_line_ending_after_spaces`. Added `tests/test_line_breaks.py` with the six declared acceptance checks plus finer tests. Scoped corpus gate `^Soft line breaks$|^Textual content$`: 5 passed, 0 failed, exit 0. Full pytest: 649 passed, 1 skipped.

<blueprint-decisions>
[{"spec":"FEATURE-Line-Breaks-Text.md","severity":"Low","subject":"Break text inside image alt","decision":"A hard or soft break inside an image description contributes a plain line ending to the alt attribute, so `![foo  \nbar](/u)` gives alt=\"foo\\nbar\". The spec does not say what alt should contain for a break. Is that acceptable?"}]
</blueprint-decisions>
