# FEATURE: Inline Code Breaks

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse code spans and hard or soft line breaks according to CommonMark. |
| Depends On  | FEATURE-Inline-Escapes.md |
| Provides    | code spans, hard line breaks, soft line breaks |
| Consumes    | escaped inline content, block tree |

## Workflow

Recognize backtick strings and pair only delimiters of equal length. Normalize line endings inside code spans to spaces, remove one surrounding space when both ends contain spaces and the content is not all spaces, and preserve all other code content literally.

For ordinary inline text, convert a line ending preceded by two or more spaces or a backslash into `<br />` behavior when it is not at block end. Preserve soft line breaks as line endings, remove indentation at the beginning of the continuation line, and leave code spans and HTML tags unaffected.

## Programmatic Acceptance

=== AC inline-code-breaks-conformance ===
Intent: The implementation passes the authoritative CommonMark examples for code spans and hard or soft line breaks owned by this story.
Suite: scoped

import subprocess

result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^(Code spans|Hard line breaks|Soft line breaks)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-code-breaks-conformance ===

=== AC inline-code-breaks-selector ===
Intent: The code-span and line-break conformance selector executes successfully.
Suite: scoped

import subprocess

sections = r"^(Code spans|Hard line breaks|Soft line breaks)$"
result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", sections,
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-code-breaks-selector ===

## User Acceptance

- None.

## Guardrails

- Do not apply escapes or entity references inside code spans.
- Do not emit hard breaks at the end of a block.
- Do not invoke `full_test.sh` from this story.
