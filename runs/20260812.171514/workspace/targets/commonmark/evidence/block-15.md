# Evidence: Block 15 · Service (block-15)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 59930
- execution id: 20260812.202011.429Z-4d350914

## Stories built
- Stage and exercise the supplied conformance harness within bounded story scopes. (conformance-assets) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-CONFORMANCE-ASSETS.md (SP 677)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- full_test.sh
- test_conformance_assets.py

## Pre-build acceptance observation
- GREEN (prepassed): conformance-assets-leaf-scope (FEATURE-CONFORMANCE-ASSETS.md)
  intent: The staged conformance harness executes a selected leaf-block scope successfully.
  return code: 0
  stdout:
    187 passed, 0 failed, 0 errored, 468 skipped
- GREEN (prepassed): conformance-assets-inline-scope (FEATURE-CONFORMANCE-ASSETS.md)
  intent: The staged conformance harness executes a selected inline scope successfully.
  return code: 0
  stdout:
    323 passed, 0 failed, 0 errored, 332 skipped

## Post-build programmatic acceptance
- PASS: conformance-assets-leaf-scope (FEATURE-CONFORMANCE-ASSETS.md)
  intent: The staged conformance harness executes a selected leaf-block scope successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    187 passed, 0 failed, 0 errored, 468 skipped
- PASS: conformance-assets-inline-scope (FEATURE-CONFORMANCE-ASSETS.md)
  intent: The staged conformance harness executes a selected inline scope successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    323 passed, 0 failed, 0 errored, 332 skipped

## Agent self-report (advisory)
The build agent declared a failure. This is advisory only; the programmatic acceptance above is the authority for this block's outcome.
- summary: Broad conformance acceptance did not return.
- detail:
    The parser subprocess remained active during the exact broad selector checks, so the declared acceptance verdict could not be confirmed.

## Build summary
RESULT: FAILED

FILES CHANGED:
- full_test.sh
- test_conformance_assets.py

SUMMARY:
Staged runtime paths and added bounded conformance tests. Individual leaf selectors passed.

BLOCKERS:
- Broad bounded selectors hung before returning an exit status in the execution environment.

FAILURE_SUMMARY: Broad conformance acceptance did not return.
FAILURE_DETAIL: The parser subprocess remained active during the exact broad selector checks, so the declared acceptance verdict could not be confirmed.
