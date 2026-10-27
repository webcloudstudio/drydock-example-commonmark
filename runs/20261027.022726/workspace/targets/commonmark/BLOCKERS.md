# Blockers: Uat Stage
- target: commonmark
- source: drydock uat CommonMark
- declared: 2026-10-26T23:23:45-04:00

<!-- drydock-state: {"owner": "uat commonmark", "execution": "", "attempts": 1} -->

## blocker-001: initial-build-1
- kind: environmental
- class: uat stage
- auto-continue: no

### Error

drydock build commonmark exited 1.

stderr:
error: build failed for commonmark: 1 step(s)
  links — closed/failed: programmatic acceptance failed: links-conformance

Evidence:
  stderr: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/evidence/commands/10-initial-build-1.stderr.log
  stdout: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/evidence/commands/10-initial-build-1.stdout.log

### Why blocked

The build did not complete. UAT stopped before acceptance tests and scoring because the application is unfinished. Resolve the build error above before rerunning UAT.
