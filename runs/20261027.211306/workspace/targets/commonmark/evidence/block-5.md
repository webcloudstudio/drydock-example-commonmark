# Evidence: Block 5 · Service (block-5)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3271
- execution id: 20261027.212642.183Z-6ea2d22c

## Stories built
- Parse setext headings. (setext-headings) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-SetextHeadings.md (SP 620)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/blocks.py
- commonmark_parser/setext.py
- tests/test_setext.py

## Pre-build acceptance observation
- RED: setext-valid (FEATURE-SetextHeadings.md)
  intent: Valid underlines convert nonempty multiline paragraph content into the corresponding heading while retaining its raw text.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "setext-valid.py", line 1, in <module>
        from commonmark_parser.setext import parse_setext
    ModuleNotFoundError: No module named 'commonmark_parser.setext'
- RED: setext-invalid (FEATURE-SetextHeadings.md)
  intent: An empty heading, excessive indentation, and internal underline whitespace do not form setext headings.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "setext-invalid.py", line 1, in <module>
        from commonmark_parser.setext import parse_setext
    ModuleNotFoundError: No module named 'commonmark_parser.setext'

## Post-build programmatic acceptance
- PASS: setext-valid (FEATURE-SetextHeadings.md)
  intent: Valid underlines convert nonempty multiline paragraph content into the corresponding heading while retaining its raw text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: setext-invalid (FEATURE-SetextHeadings.md)
  intent: An empty heading, excessive indentation, and internal underline whitespace do not form setext headings.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/setext.py
- commonmark_parser/blocks.py
- tests/test_setext.py

SUMMARY:
Added `parse_setext(lines)` and integrated setext heading recognition into block parsing, preserving raw content for inline parsing. Focused tests passed: `pytest -q tests/test_setext.py tests/test_paragraphs.py tests/test_service_blocks.py` (21 passed).

BLOCKERS:
- None
