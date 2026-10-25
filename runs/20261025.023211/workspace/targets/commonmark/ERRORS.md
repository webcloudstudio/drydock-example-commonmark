# BIG ERRORS — action required

- Command: `build`
- Phase: build step
- State: Failed
- Timestamp: 2026-10-25T20:32:26+00:00
- Execution ID: 20261025.201222.574Z-df20ce13
- Challenge Execution ID: -
- Classification: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/evidence/block-2.md

## Diagnostic

Block "Block 2 · Service" [block-2] failed its acceptance criteria.
  Story "Parse CommonMark block structure and collect link reference definitions." [block_parsing] does not meet its own acceptance criteria:
    - AC block-parsing-conformance — All supplied cases in the block parsing sections pass (the complete block capability slice).
        assertion: assert result.returncode == 0 → AssertionError
        cases: pass=249 fail=37 error=0 skip=369 total=655 from=result.stdout
        raised at: block-parsing-conformance.py:18
        process exit code: 1
        values at failure:
… (77 more lines truncated)

## Recovery

Run: drydock build commonmark
  to continue the build. This story resumes where it left off and is retried against the checks it failed.
