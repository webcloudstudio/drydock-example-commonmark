# FEATURE: Code Blocks

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses indented and fenced code blocks as literal HTML code blocks. |
| Depends On  | ARCHITECTURE.md |
| Provides    | indented code blocks, fenced code blocks |

## Purpose

Implement indented and fenced code blocks according to CommonMark 0.31.2. Code content is literal and is not processed as inline Markdown.

## Behavior

- An indented code block collects indented chunks, removes four spaces of indentation from nonblank lines, preserves content and blank lines, and cannot interrupt a paragraph.
- Fenced blocks begin with at least three matching backticks or tildes and up to three leading spaces. A closing fence uses the same marker, is at least as long, has up to three leading spaces, and is followed only by spaces or tabs.
- An unclosed fenced block continues to the end of its containing block or document.
- Remove up to the opening fence indentation from each content line. Use the first word of an info string as the code language class, escaping it for HTML attributes.
- Escape code text as HTML text while preserving its content.

## Programmatic Acceptance

=== AC code-block-conformance ===
Intent: The parser passes every supplied Indented code blocks and Fenced code blocks example.
Suite: scoped
Probe: --dump-tests
Probe Count: json

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^(Indented code blocks|Fenced code blocks)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC code-block-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not parse code block contents as Markdown or recognize references and character entities inside them.
- Preserve trailing spaces and tabs in code content.
- A fence opener containing invalid internal whitespace or, for backtick fences, backticks in its info string is not a code-fence opener.
