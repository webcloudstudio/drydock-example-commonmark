# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 3938
- execution id: 20261027.023448.384Z-651e0f69

## Stories built
- Establish the Python project and parser stage interfaces. (foundation) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- implements: python.md (SP 761)
- compass: COMPASS.md (SP 512)
- implements: ARCHITECTURE.md (SP 747)
- stack: common.md (SP 1812)

## Build directory changes
- commonmark
- commonmark_parser/__init__.py
- commonmark_parser/model.py
- commonmark_parser/stages.py
- pyproject.toml
- tests/test_parser_foundation.py
- uv.lock

## Pre-build acceptance observation
- RED: foundation-empty-document (ARCHITECTURE.md)
  intent: The published parser stages accept an empty document in the required order and render it without content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "foundation-empty-document.py", line 1, in <module>
        from commonmark_parser import parse_blocks, parse_inlines, render_html
    ModuleNotFoundError: No module named 'commonmark_parser'

## Post-build programmatic acceptance
- PASS: foundation-empty-document (ARCHITECTURE.md)
  intent: The published parser stages accept an empty document in the required order and render it without content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
`commonmark_parser` publishes `parse_blocks(markdown: str) -> Document`, `parse_inlines(document: Document) -> Document`, and `render_html(document: Document) -> str`. `Document` holds the block tree and document-wide reference-definition map; block parsing completes before inline parsing, and inline parsing can use definitions collected anywhere in the document. Block nodes retain type, children, and raw content. The root executable `commonmark` reads UTF-8 Markdown from stdin and writes HTML to stdout. Use Python 3.11+, the standard library, `.venv`, `uv`, committed `pyproject.toml` and `uv.lock`, and `pytest -q`. No public Markdown implementation or third-party runtime dependency.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- pyproject.toml
- uv.lock
- commonmark
- commonmark_parser/__init__.py
- commonmark_parser/model.py
- commonmark_parser/stages.py
- tests/test_parser_foundation.py

SUMMARY:
Added the Python project metadata and lockfile, public parser stage interfaces with an empty-document path, and the executable stdin-to-stdout entry point. Added foundation tests; `pytest -q` passed (4 tests), and the executable returned successfully for empty input.

BLOCKERS:
- None
