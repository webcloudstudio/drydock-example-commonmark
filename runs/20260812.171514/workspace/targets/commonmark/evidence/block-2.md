# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 9298
- execution id: 20260812.172907.171Z-75e402c6

## Stories built
- Implement the standard-input and standard-output parser entry point. (cli-entrypoint) [story]
- Define deterministic parser process errors and exit behavior. (cli-errors) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-CLI-ENTRYPOINT.md (SP 459)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE.md (SP 749)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)
- implements: FEATURE-CLI-ERRORS.md (SP 448)
- context: spec_tests.py (SP 1609)

## Build directory changes
- cmark
- parser/__init__.py
- parser/blocks.py
- parser/inlines.py
- renderer/html.py
- test_cli.py

## Pre-build acceptance observation
- RED: cli-stdin-stdout (FEATURE-CLI-ENTRYPOINT.md)
  intent: The executable renders Markdown supplied through standard input and exits successfully.
  return code: 1
  stdout:
    <p># Hello</p>
    <p>world</p>
  stderr:
    Traceback (most recent call last):
      File "cli-stdin-stdout.py", line 13, in <module>
        assert result.stdout == "<h1>Hello</h1>\n<p>world</p>\n"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): cli-utf8 (FEATURE-CLI-ENTRYPOINT.md)
  intent: The executable accepts UTF-8 Markdown and emits UTF-8 HTML.
  return code: 0
- GREEN (prepassed): cli-errors-success-contract (FEATURE-CLI-ERRORS.md)
  intent: A successful invocation returns zero and keeps diagnostics off standard error.
  return code: 0
- GREEN (prepassed): cli-errors-stdout-integrity (FEATURE-CLI-ERRORS.md)
  intent: The executable emits a complete HTML document result without diagnostic text in standard output.
  return code: 0

## Post-build programmatic acceptance
- PASS: cli-stdin-stdout (FEATURE-CLI-ENTRYPOINT.md)
  intent: The executable renders Markdown supplied through standard input and exits successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <h1>Hello</h1>
    <p>world</p>
- PASS: cli-utf8 (FEATURE-CLI-ENTRYPOINT.md)
  intent: The executable accepts UTF-8 Markdown and emits UTF-8 HTML.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: cli-errors-success-contract (FEATURE-CLI-ERRORS.md)
  intent: A successful invocation returns zero and keeps diagnostics off standard error.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: cli-errors-stdout-integrity (FEATURE-CLI-ERRORS.md)
  intent: The executable emits a complete HTML document result without diagnostic text in standard output.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- cmark
- parser/blocks.py
- parser/__init__.py
- parser/inlines.py
- renderer/html.py
- test_cli.py

SUMMARY:
Implemented standard-input/output CLI handling, UTF-8 validation, deterministic stderr error reporting, heading and paragraph separation, and CLI regression tests.

Verification: 8 tests passed.

BLOCKERS:
- None
