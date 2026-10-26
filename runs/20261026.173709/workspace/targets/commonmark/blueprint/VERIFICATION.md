# FEATURE: Complete Conformance Verification

| Field       | Value |
|-------------|-------|
| Version     | 20261026 V1 |
| Description | Runs the complete supplied CommonMark 0.31.2 conformance suite as the terminal project gate. |
| Depends On  | FEATURE-CommandLine.md, FEATURE-ParagraphsAndThematicBreaks.md, FEATURE-Headings.md, FEATURE-CodeBlocks.md, FEATURE-HTMLBlocks.md, FEATURE-LinkReferenceDefinitions.md, FEATURE-BlockQuotes.md, FEATURE-Lists.md, FEATURE-EscapesAndCharacterReferences.md, FEATURE-CodeSpans.md, FEATURE-Emphasis.md, FEATURE-LinksAndImages.md, FEATURE-AutolinksAndRawHTML.md, FEATURE-LineBreaks.md, FEATURE-TextualContent.md |
| Provides    | complete CommonMark conformance verification |
| Consumes    | commonmark executable |

## Purpose

Run the supplied full scoring entry point from the completed application root after the parser implementation stories have completed.

## Verification

Run `sh sources/full_test.sh` without selectors or filters. The supplied harness checks for the executable, runs the complete unfiltered CommonMark 0.31.2 suite against it, and returns a nonzero status unless the suite passes.

## Programmatic Acceptance

=== AC full-commonmark-suite ===
Intent: The supplied scoring entry point succeeds on the complete unfiltered conformance suite.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "sources/full_test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
=== END AC full-commonmark-suite ===

## User Acceptance

- None.

## Guardrails

- Run the supplied full scoring entry point unchanged.
- Do not modify or replace supplied scoring assets.
- Do not use a public Markdown implementation.
- Resolve block structure before inline structure.
