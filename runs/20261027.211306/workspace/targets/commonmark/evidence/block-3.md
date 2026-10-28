# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3261
- execution id: 20261027.212303.580Z-58ebcddd

## Stories built
- Form paragraphs and handle blank lines. (paragraphs) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-Paragraphs.md (SP 589)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/blocks.py
- tests/test_paragraphs.py

## Pre-build acceptance observation
- RED: paragraph-blocks (FEATURE-Paragraphs.md)
  intent: Consecutive lines form one paragraph and a blank line separates the next paragraph while raw content remains available.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "paragraph-blocks.py", line 7, in <module>
        assert len(document.children) == 2
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: paragraph-whitespace (FEATURE-Paragraphs.md)
  intent: Paragraph boundaries discard surrounding blank lines and retain the text of an indented continuation.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "paragraph-whitespace.py", line 6, in <module>
        assert len(document.children) == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: paragraph-blocks (FEATURE-Paragraphs.md)
  intent: Consecutive lines form one paragraph and a blank line separates the next paragraph while raw content remains available.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: paragraph-whitespace (FEATURE-Paragraphs.md)
  intent: Paragraph boundaries discard surrounding blank lines and retain the text of an indented continuation.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/blocks.py
- tests/test_paragraphs.py

SUMMARY:
Implemented paragraph grouping with blank-line separation, ignored boundary blanks, removed continuation indentation, and preserved trailing spaces on continuing lines. Focused checks passed: `pytest -q tests/test_paragraphs.py tests/test_foundation.py` — 10 passed. The full conformance suite was not run.

BLOCKERS:
- None
