# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57855
- execution id: 20260812.175353.221Z-bce07ac2

## Stories built
- Parse CommonMark leaf blocks. (block-leaf) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-BLOCK-LEAF.md (SP 584)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- cmark.py
- normalize.py
- parser/blocks.py
- renderer/html.py
- spec.txt
- spec_tests.py

## Pre-build acceptance observation
- RED: leaf-blocks-primary (FEATURE-BLOCK-LEAF.md)
  intent: The implementation passes the supplied conformance sections for thematic breaks, headings, and code blocks.
  return code: 1
  stderr:
    /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3: can't open file '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/build/commonmark/spec_tests.py': [Errno 2] No such file or directory
    
    Traceback (most recent call last):
      File "leaf-blocks-primary.py", line 20, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: leaf-blocks-secondary (FEATURE-BLOCK-LEAF.md)
  intent: The implementation passes the supplied conformance sections for HTML blocks, link references, paragraphs, and blank lines.
  return code: 1
  stderr:
    /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3: can't open file '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/build/commonmark/spec_tests.py': [Errno 2] No such file or directory
    
    Traceback (most recent call last):
      File "leaf-blocks-secondary.py", line 20, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: leaf-blocks-primary (FEATURE-BLOCK-LEAF.md)
  intent: The implementation passes the supplied conformance sections for thematic breaks, headings, and code blocks.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    105 passed, 0 failed, 0 errored, 550 skipped
- PASS: leaf-blocks-secondary (FEATURE-BLOCK-LEAF.md)
  intent: The implementation passes the supplied conformance sections for HTML blocks, link references, paragraphs, and blank lines.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    82 passed, 0 failed, 0 errored, 573 skipped

## Repair attempts
- attempt 0 (initial build): failed; 0/2 checks model=gpt-5.6-luna; execution 20260812.173325.448Z-5fbc1324
- attempt 1 (repair 1): failed; 1/2 checks; 185/187 cases model=gpt-5.6-luna; execution 20260812.174121.722Z-c21de7b4
- attempt 2 (repair 2): built; 2/2 checks; 187/187 cases model=gpt-5.6-luna; execution 20260812.175353.221Z-bce07ac2

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- parser/blocks.py
- renderer/html.py

SUMMARY:
Fixed escaped reference labels and invalid multiline titles crossing blank lines. Leaf primary and secondary acceptance checks pass; pytest passes.

BLOCKERS:
- Full suite still has failures in out-of-scope inline/container features.
