# Evidence: Block 14 · Service (block-14)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 59490
- execution id: 20260812.201030.919Z-78ba460e

## Stories built
- Normalize URL, title, attribute, and special-character output. (render-normalization) [story]

## Acceptance tooling authorization
- FEATURE-RENDER-NORMALIZATION.md#render-normalization-suite: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-RENDER-NORMALIZATION.md#render-normalization-specials: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-RENDER-NORMALIZATION.md (SP 592)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- renderer/html.py
- test_render_normalization.py

## Pre-build acceptance observation
- GREEN (prepassed): render-normalization-suite (FEATURE-RENDER-NORMALIZATION.md)
  intent: URL, title, attribute, entity, and special-character rendering passes its complete conformance scope.
  return code: 0
  stdout:
    169 passed, 0 failed, 0 errored, 486 skipped
- GREEN (prepassed): render-normalization-specials (FEATURE-RENDER-NORMALIZATION.md)
  intent: Normalized output preserves URL escaping, title escaping, attribute semantics, and special characters.
  return code: 0

## Post-build programmatic acceptance
- PASS: render-normalization-suite (FEATURE-RENDER-NORMALIZATION.md)
  intent: URL, title, attribute, entity, and special-character rendering passes its complete conformance scope.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    169 passed, 0 failed, 0 errored, 486 skipped
- PASS: render-normalization-specials (FEATURE-RENDER-NORMALIZATION.md)
  intent: Normalized output preserves URL escaping, title escaping, attribute semantics, and special characters.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- renderer/html.py
- test_render_normalization.py

SUMMARY:
Fixed inline HTML attribute scanning and added focused normalization tests. Scoped normalization conformance and pytest pass.

BLOCKERS:
- Full suite still has unrelated tab-indentation failures in existing block parsing.
