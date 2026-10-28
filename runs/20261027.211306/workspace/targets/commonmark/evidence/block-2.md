# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3053
- execution id: 20261027.212230.188Z-a55fa78c

## Stories built
- Provide the standard-stream executable. (delivery) [story]

## Acceptance tooling authorization
- FEATURE-Executable.md#executable-empty-document: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-Executable.md (SP 385)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- README.md

## Pre-build acceptance observation
- GREEN (prepassed): executable-empty-document (FEATURE-Executable.md)
  intent: The root executable accepts an empty UTF-8 document and completes successfully through the standard-stream interface.
  return code: 0

## Post-build programmatic acceptance
- PASS: executable-empty-document (FEATURE-Executable.md)
  intent: The root executable accepts an empty UTF-8 document and completes successfully through the standard-stream interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- README.md

SUMMARY:
Added concise usage documentation for the UTF-8 stdin to stdout interface. The empty-document acceptance check passed: exit status 0, empty stdout and stderr.

BLOCKERS:
- None.
