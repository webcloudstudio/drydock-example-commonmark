# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-10-24
- resulting state: closed/verified
- story points (combined assembled cost): 3782
- execution id: 20261025.023455.117Z-2c95b885

## Stories built
- Establish the Python project tree, environment, and test runner. (foundation) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- implements: python.md (SP 761)
- compass: COMPASS.md (SP 462)
- implements: ARCHITECTURE.md (SP 688)
- stack: common.md (SP 1812)

## Build directory changes
- .gitignore
- bin/commonmark
- commonmark/__init__.py
- commonmark/__main__.py
- commonmark/block_parser.py
- commonmark/cli.py
- commonmark/inline_parser.py
- commonmark/model.py
- commonmark/parser.py
- commonmark/renderer.py
- commonmark.egg-info/PKG-INFO
- commonmark.egg-info/SOURCES.txt
- commonmark.egg-info/dependency_links.txt
- commonmark.egg-info/entry_points.txt
- commonmark.egg-info/top_level.txt
- pyproject.toml
- tests/test_foundation.py
- uv.lock

## Pre-build acceptance observation
- RED: parser-package-imports (ARCHITECTURE.md)
  intent: The project exposes an importable Python package for the parser foundation.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      spec = None
    --- drydock: end values ---
    Traceback (most recent call last):
      File "parser-package-imports.py", line 4, in <module>
        assert spec is not None
               ^^^^^^^^^^^^^^^^
    AssertionError
- RED: parser-foundation-tests (ARCHITECTURE.md)
  intent: The foundation's declared pytest test command runs successfully.
  return code: 1
  stdout:
    no tests ran in 0.15s
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['pytest', '-q'], returncode=5, stdout='\nno tests ran in 0.15s\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "parser-foundation-tests.py", line 6, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: parser-package-imports (ARCHITECTURE.md)
  intent: The project exposes an importable Python package for the parser foundation.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: parser-foundation-tests (ARCHITECTURE.md)
  intent: The foundation's declared pytest test command runs successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ..                                                                       [100%]
    2 passed in 0.08s

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
- Provide an importable Python package named `commonmark`.
- Keep parsing self-contained; do not depend on a public Markdown implementation.
- Flow: block parser builds document structure and collects document-wide link references; inline parser processes content using that reference map; renderer emits HTML.
- The CLI reads UTF-8 Markdown from stdin and writes HTML to stdout.
- Boundaries: block parsing, inline parsing, HTML rendering, and CLI. No persistence, configuration, file store, or external service boundary.
- Acceptance: `importlib.util.find_spec("commonmark")` must return a package spec with `submodule_search_locations`; `pytest -q` must succeed.
</reusable-compact>

<blueprint-decisions>
[{"spec":"ARCHITECTURE.md","severity":"Material","subject":"Executable and package naming","decision":"The required importable commonmark/ package occupies the same root path as a root executable named commonmark, so both cannot exist in this filesystem layout. I kept the package acceptance contract and added the commonmark console entry point plus bin/commonmark launcher."}]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- pyproject.toml
- uv.lock
- .gitignore
- commonmark/__init__.py
- commonmark/__main__.py
- commonmark/model.py
- commonmark/block_parser.py
- commonmark/inline_parser.py
- commonmark/renderer.py
- commonmark/parser.py
- commonmark/cli.py
- bin/commonmark
- tests/test_foundation.py

SUMMARY:
Established the Python package, phase boundaries, CLI flow, uv environment and lockfile, and pytest configuration. `pytest -q` passed (2 tests); the installed console command ran successfully with empty input. Parsing non-empty documents remains for later implementation.

BLOCKERS:
- A root executable named `commonmark` conflicts with the required `commonmark/` package directory. The console entry point and `bin/commonmark` launcher provide the command meanwhile.
