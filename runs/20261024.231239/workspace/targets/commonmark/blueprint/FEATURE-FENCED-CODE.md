# FEATURE: Fenced Code Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders CommonMark fenced code blocks. |
| Depends On  | FEATURE-CLI.md |
| Provides    | fenced code blocks |

## Purpose

Recognize fenced code blocks using CommonMark 0.31.2 rules, preserving their literal content and rendering the opening fence’s first info-string word as the code language class.

## Behavior

- An opening fence is at least three backticks or tildes, preceded by no more than three spaces. Backticks and tildes cannot be mixed.
- A backtick fence’s info string cannot contain backticks. The trimmed info string’s first word, when present, produces `class="language-{word}"` on `<code>`.
- A closing fence uses the opening character, has at least the opening length, is indented by no more than three spaces, and has only spaces or tabs after it.
- Remove up to the opening fence’s indentation from content lines. Preserve other content literally, including blank lines; escape it for HTML.
- An unclosed fence continues to the end of its containing block or document. Fenced blocks may interrupt paragraphs.

## Programmatic Acceptance

=== AC fenced-code-conformance ===
Intent: The supplied “Fenced code blocks” examples define correct fenced-block parsing and rendering.
Suite: scoped
Probe: --list
Probe Count: summary

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Fenced code blocks"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC fenced-code-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep all supplied scoring assets unchanged.
