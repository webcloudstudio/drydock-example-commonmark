# Evidence: Block 12 · Service (block-12)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3205
- execution id: 20261027.213456.967Z-29b1441b

## Stories built
- Parse inline and reference images. (images) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-Images.md (SP 556)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/images.py
- tests/test_images.py

## Pre-build acceptance observation
- RED: images-inline (FEATURE-Images.md)
  intent: An inline image retains its destination and title and extracts the plain text of its description.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "images-inline.py", line 1, in <module>
        from commonmark_parser.images import parse_images
    ModuleNotFoundError: No module named 'commonmark_parser.images'
- RED: images-reference (FEATURE-Images.md)
  intent: Reference images resolve the supplied definition and omit emphasis markup from alt text.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "images-reference.py", line 1, in <module>
        from commonmark_parser.images import parse_images
    ModuleNotFoundError: No module named 'commonmark_parser.images'

## Post-build programmatic acceptance
- PASS: images-inline (FEATURE-Images.md)
  intent: An inline image retains its destination and title and extracts the plain text of its description.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: images-reference (FEATURE-Images.md)
  intent: Reference images resolve the supplied definition and omit emphasis markup from alt text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/images.py
- tests/test_images.py

SUMMARY:
Added `parse_images(source, references)` with inline, full, collapsed, and shortcut reference support. Image alt text includes plain text from formatted descriptions, links, and nested images. Added six focused tests.

Checks run: `pytest -q tests/test_images.py` — 6 passed; `pytest -q` — 68 passed.

BLOCKERS:
- None
