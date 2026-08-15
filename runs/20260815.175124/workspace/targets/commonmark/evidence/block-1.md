# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 8084
- execution id: 20260815.180003.650Z-56828128

## Stories built
- Define the standalone CommonMark parser architecture and module boundaries. (architecture) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- compass: COMPASS.md (SP 1237)
- implements: ARCHITECTURE.md (SP 1039)
- stack: common.md (SP 1807)
- stack: python.md (SP 3892)

## Build directory changes
- README.md
- blocks.py
- commonmark.py
- inlines.py
- normalization.py
- references.py
- renderer.py
- test_architecture.py

## Pre-build acceptance observation
- RED: architecture-input-boundary (ARCHITECTURE.md)
  intent: The implementation exposes an input-normalization boundary that accepts text input.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-input-boundary.py", line 3, in <module>
        module = importlib.import_module("commonmark")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py", line 90, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
      File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
      File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
    ModuleNotFoundError: No module named 'commonmark'
- RED: architecture-render-boundary (ARCHITECTURE.md)
  intent: The implementation exposes a rendering boundary that accepts a parsed document.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-render-boundary.py", line 3, in <module>
        module = importlib.import_module("commonmark")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py", line 90, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
      File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
      File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
    ModuleNotFoundError: No module named 'commonmark'
- RED: architecture-cli-boundary (ARCHITECTURE.md)
  intent: The executable module exposes a callable process entry point.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "architecture-cli-boundary.py", line 3, in <module>
        module = importlib.import_module("commonmark")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/importlib/__init__.py", line 90, in import_module
        return _bootstrap._gcd_import(name[level:], package, level)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
      File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
      File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
    ModuleNotFoundError: No module named 'commonmark'

## Post-build programmatic acceptance
- PASS: architecture-input-boundary (ARCHITECTURE.md)
  intent: The implementation exposes an input-normalization boundary that accepts text input.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: architecture-render-boundary (ARCHITECTURE.md)
  intent: The implementation exposes a rendering boundary that accepts a parsed document.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: architecture-cli-boundary (ARCHITECTURE.md)
  intent: The executable module exposes a callable process entry point.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
Expose `commonmark.parse(text)`, `commonmark.render(document)`, and `commonmark.main()`. Preserve the pipeline: input normalization → block parsing/reference collection → inline parsing → HTML rendering. Use Python standard library only; stdin/stdout is the executable contract. Replace U+0000 with U+FFFD and preserve indentation/tabs.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- normalization.py
- references.py
- blocks.py
- inlines.py
- renderer.py
- commonmark.py
- test_architecture.py
- README.md

SUMMARY:
Implemented the standalone parser architecture and verified all declared boundaries. Four architecture tests pass.

BLOCKERS:
- None
