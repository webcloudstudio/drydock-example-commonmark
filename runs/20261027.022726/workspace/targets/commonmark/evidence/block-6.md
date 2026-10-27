# Evidence: Block 6 · Service (block-6)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 3273
- execution id: 20261027.024023.492Z-6d2bd12e

## Stories built
- Parse list items and lists with nesting and tightness. (lists) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-Lists.md (SP 781)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/lists.py
- commonmark_parser/stages.py
- tests/test_lists.py

## Pre-build acceptance observation
- RED: list-marker (FEATURE-Lists.md)
  intent: An ordered marker reports its start value and the indentation needed for its content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "list-marker.py", line 1, in <module>
        from commonmark_parser.lists import parse_list_marker
    ModuleNotFoundError: No module named 'commonmark_parser.lists'
- RED: list-paragraph-interruption (FEATURE-Lists.md)
  intent: Only an ordered marker starting at one may interrupt a paragraph.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "list-paragraph-interruption.py", line 1, in <module>
        from commonmark_parser.lists import parse_list_marker
    ModuleNotFoundError: No module named 'commonmark_parser.lists'

## Post-build programmatic acceptance
- PASS: list-marker (FEATURE-Lists.md)
  intent: An ordered marker reports its start value and the indentation needed for its content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: list-paragraph-interruption (FEATURE-Lists.md)
  intent: Only an ordered marker starting at one may interrupt a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/lists.py
- commonmark_parser/stages.py
- tests/test_lists.py

SUMMARY:
Implemented list marker parsing, nested list nodes, ordered start numbers, and tight/loose list rendering. `pytest -q` passed: 34 tests. The staged full conformance suite completed with 307 passed and 348 failed; many failures concern inline parsing and other block features outside this lists step.

BLOCKERS:
- None
