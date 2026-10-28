# Evidence: Block 7 · Service (block-7)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3486
- execution id: 20261027.212834.286Z-b90fd7eb

## Stories built
- Parse list items and lists. (lists) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-Lists.md (SP 829)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/blocks.py
- tests/test_lists.py

## Pre-build acceptance observation
- RED: list-items (FEATURE-Lists.md)
  intent: Matching markers form one tight list with separate items whose paragraph text is preserved.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      listing = Block(kind='paragraph', children=[], literal='- alpha\n- beta', level=None, info='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "list-items.py", line 8, in <module>
        assert listing.type == "list"
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: list-start-and-looseness (FEATURE-Lists.md)
  intent: An ordered list retains its initial number and blank lines between items make it loose.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Block(kind='paragraph', children=[], literal='4. first', level=None, info=''), Block(kind='paragraph', children=[], literal='5. second', level=None, info='')], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "list-start-and-looseness.py", line 7, in <module>
        assert len(document.children) == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: list-items (FEATURE-Lists.md)
  intent: Matching markers form one tight list with separate items whose paragraph text is preserved.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: list-start-and-looseness (FEATURE-Lists.md)
  intent: An ordered list retains its initial number and blank lines between items make it loose.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/blocks.py
- tests/test_lists.py

SUMMARY:
Added list and item block nodes with marker grouping, ordered start numbers, nesting, continuation handling, and tight or loose status. Added focused list tests. The targeted test command passed: `pytest -q tests/test_lists.py tests/test_block_quotes.py tests/test_paragraphs.py tests/test_setext.py tests/test_service_blocks.py tests/test_foundation.py` (37 passed). The full conformance suite was not run.

BLOCKERS:
- None
