# FEATURE: Inline Emphasis

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse emphasis and strong emphasis with the CommonMark delimiter-run algorithm. |
| Depends On  | FEATURE-Inline-Code-Breaks.md |
| Provides    | emphasis and strong-emphasis inline nodes |
| Consumes    | code spans, escaped inline content, block tree |

## Workflow

Build delimiter runs for asterisks and underscores while parsing inline content. Compute left- and right-flanking behavior using Unicode whitespace and punctuation, apply intraword restrictions for underscores, and resolve matching delimiters with the CommonMark delimiter-stack algorithm.

Support single and double emphasis, nested emphasis, rule-of-three behavior, precedence against code spans and other inline constructs, and unmatched delimiter runs. Preserve literal delimiters when no valid pairing exists.

## Programmatic Acceptance

=== AC inline-emphasis-conformance ===
Intent: The implementation passes the authoritative CommonMark examples for emphasis and strong emphasis owned by this story.
Suite: scoped

import subprocess

result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^Emphasis and strong emphasis$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-emphasis-conformance ===

=== AC inline-emphasis-selector ===
Intent: The emphasis conformance selector executes the complete owned specification section successfully.
Suite: scoped

import subprocess

section = r"^Emphasis and strong emphasis$"
result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", section,
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-emphasis-selector ===

## User Acceptance

- None.

## Guardrails

- Apply delimiter matching only after code spans, links, images, and raw HTML precedence is respected.
- Do not allow intraword underscore emphasis.
- Do not invoke `full_test.sh` from this story.
