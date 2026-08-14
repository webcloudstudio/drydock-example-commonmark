# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 7767
- execution id: 20260812.172723.109Z-4a4db6be

## Stories built
- Define parser architecture and module boundaries. (architecture) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: ARCHITECTURE.md (SP 749)
- stack: common.md (SP 1807)
- stack: python.md (SP 3892)

## Build directory changes
- README.md
- cmark
- full_test.sh
- parser/__init__.py
- parser/blocks.py
- parser/inlines.py
- renderer/__init__.py
- renderer/html.py
- test_architecture.py

## Pre-build acceptance observation
- RED: architecture-boundaries (ARCHITECTURE.md)
  intent: The implementation exposes separate block, inline, rendering, and executable boundaries.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-boundaries.py", line 8, in <module>
        assert all(path.exists() for path in required)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: architecture-runtime-contract (ARCHITECTURE.md)
  intent: The runtime contains the required POSIX conformance wrapper boundary.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-runtime-contract.py", line 4, in <module>
        assert wrapper.is_file()
               ^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: architecture-boundaries (ARCHITECTURE.md)
  intent: The implementation exposes separate block, inline, rendering, and executable boundaries.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: architecture-runtime-contract (ARCHITECTURE.md)
  intent: The runtime contains the required POSIX conformance wrapper boundary.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- `cmark`
- `parser/__init__.py`
- `parser/blocks.py`
- `parser/inlines.py`
- `renderer/__init__.py`
- `renderer/html.py`
- `full_test.sh`
- `README.md`
- `test_architecture.py`

SUMMARY:
Implemented the two-phase parser, renderer, executable, and conformance-wrapper boundaries. Added deterministic architecture and stdin/stdout contract tests; all 3 focused tests passed.

BLOCKERS:
- None
