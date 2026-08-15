# BIG ERRORS — action required

- Command: `build`
- Phase: build step
- State: Failed
- Timestamp: 2026-08-15T18:26:58+00:00
- Execution ID: 20260815.182507.700Z-c801ce17
- Challenge Execution ID: -
- Classification: programmatic acceptance failed: block-references-container
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.175124/workspace/targets/commonmark/evidence/block-4.md

## Diagnostic

Block "Block 4 · Service" [block-4] failed its acceptance criteria.
  Story "Collect and resolve document-wide link reference definitions." [block-references] does not meet its own acceptance criteria:
    - AC block-references-container — The implementation passes reference-definition cases involving document-wide and container-scoped definitions.
        assertion: TypeError: expected str, bytes or os.PathLike object, not int
        process exit code: 1
        error: TypeError: expected str, bytes or os.PathLike object, not int

## Recovery

Run: drydock build commonmark
  to continue the build. This story resumes where it left off and is retried against the checks it failed.
