# BIG ERRORS — action required

- Command: `build`
- Phase: build step
- State: Failed
- Timestamp: 2026-10-28T00:23:53+00:00
- Execution ID: 20261028.001809.125Z-549378e5
- Challenge Execution ID: -
- Classification: programmatic acceptance failed: conformance-blocks, conformance-inlines
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark/evidence/block-13.md

## Diagnostic

Block "Block 13 · Service" [block-13] failed its acceptance criteria.
  Story "Exercise all scoped CommonMark examples against the integrated parser." [conformance-integration] does not meet its own acceptance criteria:
    - AC conformance-blocks — The integrated parser passes every example in the supplied leaf block sections.
        assertion: assert result.returncode == 0 → AssertionError
        cases: pass=184 fail=3 error=0 skip=468 total=655 from=result.stdout
        raised at: conformance-blocks.py:12
        process exit code: 1
        values at failure:
… (48 more lines truncated)

## Recovery

Run: drydock build commonmark
  to continue the build. This story resumes where it left off and is retried against the checks it failed.
