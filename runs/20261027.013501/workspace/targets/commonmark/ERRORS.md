# BIG ERRORS — action required

- Command: `plan`
- Phase: post-output validation
- State: Error
- Timestamp: 2026-10-27T01:36:39+00:00
- Execution ID: 20261027.013608.189Z-8721be32
- Challenge Execution ID: -
- Classification: model artifact contract failed
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/logs

## Diagnostic

Stage 1 correction exhausted: TOPOLOGY.md: missing closing artifact marker

## Recovery

Inspect the topology retry evidence, then run: drydock plan commonmark
