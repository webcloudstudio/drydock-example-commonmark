# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 2884
- execution id: 20261027.023526.878Z-e9dcbe15

## Stories built
- Provide the root executable and standard streams interface. (cli) [story]

## Acceptance tooling authorization
- FEATURE-CommandLine.md#command-empty-input: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-CommandLine.md (SP 415)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark
- tests/test_command_line.py

## Pre-build acceptance observation
- GREEN (prepassed): command-empty-input (FEATURE-CommandLine.md)
  intent: The executable accepts an empty UTF-8 document and emits its empty rendered result successfully.
  return code: 0

## Post-build programmatic acceptance
- PASS: command-empty-input (FEATURE-CommandLine.md)
  intent: The executable accepts an empty UTF-8 document and emits its empty rendered result successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark
- tests/test_command_line.py

SUMMARY:
The root executable explicitly decodes stdin and encodes stdout as UTF-8 while passing input through the parser stages in order. The three CLI tests passed, and the declared empty-input acceptance check passed.

BLOCKERS:
- None
