# FEATURE: Complete Conformance Verification

| Field | Value |
|-------------|-------|
| Version | 20261027 V1 |
| Description | Verify the finished parser against the complete supplied CommonMark suite. |
| Depends On | FEATURE-InlineLineBreaks.md, FEATURE-Documentation.md, FEATURE-CommandLine.md, FEATURE-ParagraphsAndBreaks.md, FEATURE-Headings.md, FEATURE-CodeBlocks.md, FEATURE-HtmlBlocks.md, FEATURE-ReferenceDefinitions.md, FEATURE-BlockQuotes.md, FEATURE-Lists.md, FEATURE-EscapesAndEntities.md, FEATURE-CodeSpans.md, FEATURE-Emphasis.md, FEATURE-Links.md, FEATURE-Images.md, FEATURE-AutolinksAndRawHtml.md |
| Consumes | commonmark, inline line breaks |

## Purpose

Verify the assembled executable against every example in the supplied CommonMark 0.31.2 conformance suite.

## Behavior

Run the supplied scoring entry point from the application root without filtering or altering its assets. Its exit status decides this verification.

## Programmatic Acceptance

=== AC complete-conformance ===
Intent: The completed executable passes the supplied unfiltered CommonMark conformance suite.
Suite: full
Requires: executable=sh; scope=test
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True, text=True, encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC complete-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not modify the supplied scoring harness, runner, normalizer, reference wrapper, or specification.
- Do not alter the full-suite entry point to repair implementation failures.
