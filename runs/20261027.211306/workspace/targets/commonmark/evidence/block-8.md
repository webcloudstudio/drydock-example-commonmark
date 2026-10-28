# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3427
- execution id: 20261027.212943.897Z-4276dc89

## Stories built
- Parse escapes, character references, and text line breaks. (inline-text) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-InlineText.md (SP 767)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/inlines.py
- tests/test_inline_text.py

## Pre-build acceptance observation
- RED: inline-escape (FEATURE-InlineText.md)
  intent: Escaped ASCII punctuation becomes literal text without retaining the escape marker.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = []
    --- drydock: end values ---
    Traceback (most recent call last):
      File "inline-escape.py", line 5, in <module>
        assert len(nodes) == 1
               ^^^^^^^^^^^^^^^
    AssertionError
- RED: inline-soft-break (FEATURE-InlineText.md)
  intent: A regular line ending separates text nodes with a soft break while retaining their text.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = []
    --- drydock: end values ---
    Traceback (most recent call last):
      File "inline-soft-break.py", line 6, in <module>
        assert [node.type for node in nodes] == ["text", "softbreak", "text"]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: inline-numeric-reference (FEATURE-InlineText.md)
  intent: A valid numeric character reference decodes to the character designated by its input code point.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = []
    --- drydock: end values ---
    Traceback (most recent call last):
      File "inline-numeric-reference.py", line 5, in <module>
        assert len(nodes) == 1
               ^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: inline-escape (FEATURE-InlineText.md)
  intent: Escaped ASCII punctuation becomes literal text without retaining the escape marker.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: inline-soft-break (FEATURE-InlineText.md)
  intent: A regular line ending separates text nodes with a soft break while retaining their text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: inline-numeric-reference (FEATURE-InlineText.md)
  intent: A valid numeric character reference decodes to the character designated by its input code point.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/inlines.py
- tests/test_inline_text.py

SUMMARY:
Added inline text parsing for ASCII punctuation escapes, named and numeric character references, invalid numeric scalar replacement, and soft breaks with surrounding spaces trimmed. Added focused tests for these behaviors and edge cases.

CHECKS:
- `pytest -q tests/test_inline_text.py tests/test_foundation.py` — 12 passed.

BLOCKERS:
- None
