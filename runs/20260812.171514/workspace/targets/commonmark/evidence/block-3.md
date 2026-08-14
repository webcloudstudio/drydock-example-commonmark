# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 3571
- execution id: 20260812.173136.817Z-ccf9b16e

## Stories built
- Document parser operation and conformance verification. (cli-documentation) [story]

## Reusable compacts
- ARCHITECTURE_compact.md

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-CLI-DOCUMENTATION.md (SP 349)
- context: ARCHITECTURE.md (SP 749)
- stack: common_compact.md (SP 1179)

## Build directory changes
- README.md
- test_documentation.py

## Pre-build acceptance observation
- GREEN (prepassed): cli-documentation-content (FEATURE-CLI-DOCUMENTATION.md)
  intent: README.md documents the standard-input and standard-output interface.
  return code: 0
- GREEN (prepassed): cli-documentation-verification (FEATURE-CLI-DOCUMENTATION.md)
  intent: README.md documents the required complete-suite invocation.
  return code: 0

## Post-build programmatic acceptance
- PASS: cli-documentation-content (FEATURE-CLI-DOCUMENTATION.md)
  intent: README.md documents the standard-input and standard-output interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: cli-documentation-verification (FEATURE-CLI-DOCUMENTATION.md)
  intent: README.md documents the required complete-suite invocation.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Agent self-report (advisory)
The build agent declared a failure. This is advisory only; the programmatic acceptance above is the authority for this block's outcome.
- summary: Full CommonMark conformance suite fails in existing parser implementation.
- detail:
    The requested documentation acceptance checks pass, but `sh full_test.sh` reports multiple parser mismatches unrelated to README.md. Fix the parser behaviors before rerunning the complete build.

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
CommonMark is a Python 3 CLI parser that reads UTF-8 Markdown from standard input, parses blocks before inlines, and writes CommonMark 0.31.2 HTML to standard output. Runtime boundaries are `cmark`, `parser`, `renderer`, and `full_test.sh`; no public Markdown implementation or third-party dependencies are used.
</reusable-compact>

RESULT: FAILED

FILES CHANGED:
- README.md
- test_documentation.py

SUMMARY:
Updated README documentation and added focused acceptance tests. Documentation checks pass; the full conformance suite remains failing on existing parser behavior.

BLOCKERS:
- `sh full_test.sh` fails on parser cases including tabs, escapes, entities, and thematic breaks.

FAILURE_SUMMARY: Full CommonMark conformance suite fails in existing parser implementation.
FAILURE_DETAIL: The requested documentation acceptance checks pass, but `sh full_test.sh` reports multiple parser mismatches unrelated to README.md. Fix the parser behaviors before rerunning the complete build.
