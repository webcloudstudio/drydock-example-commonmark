# BIG ERRORS — action required

- Command: `plan`
- Phase: plan verify
- State: Error
- Timestamp: 2026-10-24T23:41:20+00:00
- Execution ID: 20261024.233833.758Z-626da3b2
- Challenge Execution ID: -
- Classification: plan cannot be built as written
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/logs

## Diagnostic

plan verify: commonmark
  5 criteria cannot run as written
  ✗  FEATURE-BlockQuotes.md [block-quotes]: line 12: sources/spec_tests.py --pattern 'Block quotes' selects a subset of a staged corpus: probe arguments cannot be statically resolved
  ✗  FEATURE-CodeSpans.md [code-spans]: line 12: sources/spec_tests.py --pattern 'Code spans' selects a subset of a staged corpus: probe arguments cannot be statically resolved
  ✗  FEATURE-EscapesAndCharacterReferences.md [escapes-and-character-references]: line 12: sources/spec_tests.py --pattern 'Backslash escapes|Entity and numeric character references' selects a subset of a staged corpus: probe arguments cannot be statically resolved
  ✗  FEATURE-Lists.md [lists]: line 12: sources/spec_tests.py --pattern 'List items|Lists' selects a subset of a staged corpus: probe arguments cannot be statically resolved
  ✗  FEATURE-ReferenceDefinitionsAndParagraphs.md [references-and-paragraphs]: line 12: sources/spec_tests.py --pattern 'Link reference definitions|Paragraphs' selects a subset of a staged corpus: probe arguments cannot be statically resolved
  Run: drydock plan repair commonmark

## Recovery

Run: drydock plan repair commonmark
