# BIG ERRORS — action required

- Command: `plan`
- Phase: plan verify
- State: Error
- Timestamp: 2026-10-24T23:18:30+00:00
- Execution ID: 20261024.231424.750Z-c775fcbc
- Challenge Execution ID: -
- Classification: plan cannot be built as written
- Evidence / logs: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/logs

## Diagnostic

plan verify: commonmark
  19 criteria cannot run as written
  ✗  FEATURE-ATX-HEADINGS.md [atx-headings-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe output does not match the declared 'summary' protocol
  ✗  FEATURE-BACKSLASH-ESCAPES.md [backslash-escape-conformance]: line 5: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-BLANK-LINES.md [blank-lines-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-BLOCK-QUOTES.md [block-quotes-conformance]: line 5: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-CHARACTER-REFERENCES.md [character-reference-conformance]: line 5: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-CODE-SPANS.md [code-span-conformance]: line 5: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-FENCED-CODE.md [fenced-code-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-HARD-LINE-BREAKS.md [hard-line-breaks-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-HTML-BLOCKS.md [html-block-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-INDENTED-CODE.md [indented-code-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe output does not match the declared 'summary' protocol
  ✗  FEATURE-LINK-REFERENCE-DEFINITIONS.md [link-reference-definition-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-LIST-ITEMS.md [list-items-conformance]: line 5: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-LISTS.md [lists-conformance]: line 5: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-PARAGRAPHS.md [paragraph-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-RAW-HTML.md [raw-html-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-SETEXT-HEADINGS.md [setext-headings-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe output does not match the declared 'summary' protocol
  ✗  FEATURE-SOFT-LINE-BREAKS.md [soft-line-breaks-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-TEXTUAL-CONTENT.md [textual-content-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe exited 2: spec_tests.py: error: unrecognized arguments: --list
  ✗  FEATURE-THEMATIC-BREAKS.md [thematic-breaks-conformance]: line 4: sources/spec_tests.py --program './commonmark' selects a subset of a staged corpus: probe output does not match the declared 'summary' protocol
  ⚠  FEATURE-CLI.md [cli-empty-input]: captures a program's output and prints none of it; print its pass/fail counts before asserting so repair can see progress
  ⚠  FEATURE-CLI.md [cli-markdown-input]: captures a program's output and prints none of it; print its pass/fail counts before asserting so repair can see progress
  Run: drydock plan repair commonmark

## Recovery

Run: drydock plan repair commonmark
