# FEATURE: Full Conformance Verification

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Verifies the completed parser using the complete supplied CommonMark 0.31.2 conformance suite. |
| Depends On  | ARCHITECTURE.md, FEATURE-ThematicBreaksAndATXHeadings.md, FEATURE-SetextHeadings.md, FEATURE-CodeBlocks.md, FEATURE-HTMLBlocks.md, FEATURE-ReferenceDefinitionsAndParagraphs.md, FEATURE-BlockQuotes.md, FEATURE-Lists.md, FEATURE-EscapesAndCharacterReferences.md, FEATURE-CodeSpans.md, FEATURE-Emphasis.md, FEATURE-Links.md, FEATURE-Images.md, FEATURE-AutolinksAndRawHTML.md, FEATURE-LineBreaksAndText.md, FEATURE-ExecutableInterface.md |
| Provides    | Full conformance verification |

## Purpose

Run `sh sources/full_test.sh` from the completed application root as the sole unfiltered conformance verification. The supplied harness checks that `./commonmark` is executable and runs the complete suite. Preserve the harness and its assets unchanged.

## Programmatic Acceptance

=== AC full-conformance ===
Intent: The completed parser passes the complete supplied CommonMark 0.31.2 suite.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"], capture_output=True, text=True
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC full-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not invoke the unfiltered suite from scoped checks.
- Do not modify or replace `sources/full_test.sh` or any supplied scoring asset.
- The complete supplied suite is the release conformance gate.
