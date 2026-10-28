# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3277
- execution id: 20261027.213041.126Z-a9181387

## Stories built
- Parse inline code spans. (code-spans) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-CodeSpans.md (SP 630)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/inlines.py
- tests/test_inline_text.py

## Pre-build acceptance observation
- RED: code-span-literal (FEATURE-CodeSpans.md)
  intent: Matching backtick runs yield a code node that preserves its literal content.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = [Inline(type='text', literal='`literal & text`')]
    --- drydock: end values ---
    Traceback (most recent call last):
      File "code-span-literal.py", line 6, in <module>
        assert nodes[0].type == "code"
               ^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: code-span-normalization (FEATURE-CodeSpans.md)
  intent: A matched span converts its line ending to a space and removes one paired surrounding space.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = [Inline(type='text', literal='` alpha'), Inline(type='softbreak', literal=''), Inline(type='text', literal='beta `')]
    --- drydock: end values ---
    Traceback (most recent call last):
      File "code-span-normalization.py", line 6, in <module>
        assert len(nodes) == 1
               ^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): code-span-unmatched (FEATURE-CodeSpans.md)
  intent: An unmatched opening run remains literal text.
  return code: 0

## Post-build programmatic acceptance
- PASS: code-span-literal (FEATURE-CodeSpans.md)
  intent: Matching backtick runs yield a code node that preserves its literal content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: code-span-normalization (FEATURE-CodeSpans.md)
  intent: A matched span converts its line ending to a space and removes one paired surrounding space.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: code-span-unmatched (FEATURE-CodeSpans.md)
  intent: An unmatched opening run remains literal text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/inlines.py
- tests/test_inline_text.py

SUMMARY:
Implemented inline code spans with equal-length backtick matching, line-ending and paired-space normalization, and literal content preservation. Added focused coverage. `pytest -q tests/test_inline_text.py` passed: 13 tests.

BLOCKERS:
- None
