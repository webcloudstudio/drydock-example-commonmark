# BIG ERRORS — action required

- Command: `build`
- Phase: build step
- State: Failed
- Timestamp: 2026-10-27T03:23:37+00:00
- Execution ID: 20261027.032209.085Z-31db92e4
- Challenge Execution ID: -
- Classification: programmatic acceptance failed: links-conformance
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark/evidence/block-10.md

## Diagnostic

Block "Block 10 · Service" [block-10] failed its acceptance criteria.
  Story "Parse inline and reference links." [links] does not meet its own acceptance criteria:
    - AC links-conformance — The completed parser passes the authoritative link and link-reference-definition examples.
        assertion: assert result.returncode == 0 → AssertionError
        cases: pass=110 fail=7 error=0 skip=538 total=655 from=result.stdout
        raised at: links-conformance.py:12
        process exit code: 1
        values at failure:
… (21 more lines truncated)

## Recovery

The agent disputes failing acceptance criteria; the claim is unverified.
Run: drydock plan verify commonmark
  Inspect the criteria and evidence before rebuilding.
Run: drydock plan repair commonmark
  Repair confirmed mechanical defects, then verify before rebuilding.
