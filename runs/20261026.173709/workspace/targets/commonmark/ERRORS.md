# BIG ERRORS — action required

- Command: `plan`
- Phase: plan verify
- State: Error
- Timestamp: 2026-10-26T17:42:44+00:00
- Execution ID: 20261026.173811.198Z-ebafbb76
- Challenge Execution ID: -
- Classification: plan cannot be built as written
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/logs

## Diagnostic

plan verify: commonmark
  3 criteria cannot run as written
  ✗  FEATURE-AutolinksAndRawHTML.md [inline-autolinks-raw-html]: line 4: sources/spec_tests.py --pattern 'Autolinks|Raw HTML' selects a subset of a staged corpus: probe arguments cannot be statically resolved at runner argument 2; declaration-only repair cannot resolve command expressions
  ✗  FEATURE-LineBreaks.md [inline-hard-soft-breaks]: line 5: sources/spec_tests.py --pattern 'Hard line breaks|Soft line breaks' selects a subset of a staged corpus: probe arguments cannot be statically resolved at runner argument 2; declaration-only repair cannot resolve command expressions
  ✗  FEATURE-TextualContent.md [inline-textual-content]: line 5: sources/spec_tests.py --pattern 'Textual content' selects a subset of a staged corpus: probe arguments cannot be statically resolved at runner argument 2; declaration-only repair cannot resolve command expressions
  Run: drydock plan repair commonmark

## Recovery

Run: drydock plan repair commonmark
