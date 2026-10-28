# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 4283
- execution id: 20261027.212136.170Z-f219a077

## Stories built
- Establish the Python project and parser integration boundaries. (foundation) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- implements: python.md (SP 814)
- compass: COMPASS.md (SP 548)
- implements: ARCHITECTURE.md (SP 993)
- stack: common.md (SP 1812)

## Build directory changes
- .gitignore
- commonmark
- commonmark_parser/__init__.py
- commonmark_parser/blocks.py
- commonmark_parser/cli.py
- commonmark_parser/inlines.py
- pyproject.toml
- tests/test_foundation.py
- uv.lock

## Pre-build acceptance observation
- RED: foundation-integration (ARCHITECTURE.md)
  intent: The Python foundation exposes the parser integration callable before parser features are implemented.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "foundation-integration.py", line 1, in <module>
        import commonmark_parser
    ModuleNotFoundError: No module named 'commonmark_parser'
- RED: foundation-block-boundary (ARCHITECTURE.md)
  intent: The foundation exposes a callable block parser for later block capabilities.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "foundation-block-boundary.py", line 1, in <module>
        from commonmark_parser.blocks import parse_blocks
    ModuleNotFoundError: No module named 'commonmark_parser'
- RED: foundation-inline-boundary (ARCHITECTURE.md)
  intent: The foundation exposes a callable inline parser for the second parsing phase.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "foundation-inline-boundary.py", line 1, in <module>
        from commonmark_parser.inlines import parse_inlines
    ModuleNotFoundError: No module named 'commonmark_parser'

## Post-build programmatic acceptance
- PASS: foundation-integration (ARCHITECTURE.md)
  intent: The Python foundation exposes the parser integration callable before parser features are implemented.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: foundation-block-boundary (ARCHITECTURE.md)
  intent: The foundation exposes a callable block parser for later block capabilities.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: foundation-inline-boundary (ARCHITECTURE.md)
  intent: The foundation exposes a callable inline parser for the second parsing phase.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
- Python 3.11+; standard library only at runtime. Root owns `pyproject.toml`, committed `uv.lock`, `.venv`, launchers, and `pytest -q`.
- Public interfaces: `commonmark_parser.render(markdown: str) -> str`; `commonmark_parser.blocks.parse_blocks(markdown: str) -> Document`; `commonmark_parser.inlines.parse_inlines(literal: str, references: dict) -> list`.
- `Document` exposes ordered `children` and document-wide `references`. Block nodes expose `kind`, `children`, and `literal`; headings also expose `level`.
- Parse block structure and collect references before parsing paragraph and heading inline content. Preserve raw inline source until that phase.
- Root executable `commonmark` reads UTF-8 Markdown from stdin and writes HTML to stdout.
- Keep `sources/spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh` verbatim under `sources/`. The runner imports sibling helpers and receives program and specification paths.
- Do not use a public Markdown implementation or modify the supplied conformance assets and full-suite entry point.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- .gitignore
- commonmark
- commonmark_parser/__init__.py
- commonmark_parser/blocks.py
- commonmark_parser/cli.py
- commonmark_parser/inlines.py
- pyproject.toml
- tests/test_foundation.py
- uv.lock

SUMMARY:
Added the Python project metadata and lockfile, parser integration interfaces, and stdin/stdout executable. Added five focused foundation tests. `pytest -q` passed (5 tests); `printf 'x' | ./commonmark` exited 0. The supplied conformance suite was not run.

BLOCKERS:
- None
