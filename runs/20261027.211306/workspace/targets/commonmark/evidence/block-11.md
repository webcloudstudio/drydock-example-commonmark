# Evidence: Block 11 · Service (block-11)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3417
- execution id: 20261027.213328.256Z-55fc0c59

## Stories built
- Parse inline and reference links. (links) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-Links.md (SP 753)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/links.py
- tests/test_links.py

## Pre-build acceptance observation
- RED: links-inline (FEATURE-Links.md)
  intent: Inline link parsing returns the supplied destination and title and retains the link text as children.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "links-inline.py", line 1, in <module>
        from commonmark_parser.links import parse_links
    ModuleNotFoundError: No module named 'commonmark_parser.links'
- RED: links-reference (FEATURE-Links.md)
  intent: Full, collapsed, and shortcut references resolve through the supplied normalized reference map.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "links-reference.py", line 1, in <module>
        from commonmark_parser.links import parse_links
    ModuleNotFoundError: No module named 'commonmark_parser.links'

## Post-build programmatic acceptance
- PASS: links-inline (FEATURE-Links.md)
  intent: Inline link parsing returns the supplied destination and title and retains the link text as children.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: links-reference (FEATURE-Links.md)
  intent: Full, collapsed, and shortcut references resolve through the supplied normalized reference map.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/links.py
- tests/test_links.py

SUMMARY:
Implemented inline, full, collapsed, and shortcut reference links with destination and title parsing, entity and escape decoding, balanced parentheses, and normalized reference lookup. Added six focused link tests.

CHECKS:
- `pytest -q tests/test_links.py` — 6 passed.
- `pytest -q` — 62 passed.

BLOCKERS:
- None
