# FEATURE: Inline Escapes

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse backslash escapes and named or numeric character references in inline content. |
| Depends On  | FEATURE-Block-Lists.md |
| Provides    | escaped punctuation, named entity references, numeric character references |
| Consumes    | block tree, document-wide link reference definition map |

## Workflow

Parse inline text after block structure has been established. Remove backslashes only when they precede ASCII punctuation, preserve backslashes before other characters, and decode valid HTML5 named entities plus decimal and hexadecimal numeric references.

Apply reference parsing outside code spans, fenced code, indented code, autolinks, and raw HTML. Replace U+0000 and invalid numeric code points with U+FFFD, while leaving invalid or unterminated references as literal text.

## Programmatic Acceptance

=== AC inline-escapes-conformance ===
Intent: The implementation passes the authoritative CommonMark examples for backslash escapes and entity or numeric character references owned by this story.
Suite: scoped

import subprocess

result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^(Backslash escapes|Entity and numeric character references)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-escapes-conformance ===

=== AC inline-escapes-selector ===
Intent: The escape and character-reference conformance selector executes successfully.
Suite: scoped

import subprocess

sections = r"^(Backslash escapes|Entity and numeric character references)$"
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
=== END AC inline-escapes-selector ===

## User Acceptance

- None.

## Guardrails

- Do not decode entities or escapes inside code spans or code blocks.
- Do not treat entity references as block-structure markers.
- Do not invoke `full_test.sh` from this story.
