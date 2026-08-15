# FEATURE: CLI Boundary Handling

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Handle malformed, empty, unclosed, and arbitrary Unicode input safely. |
| Depends On  | FEATURE-CLI-Executable.md |
| Provides    | safe malformed-input handling |
| Consumes    | commonmark stdin/stdout executable |

## Intent

The parser and executable remain deterministic and non-crashing when input contains incomplete constructs, invalid syntax, empty documents, NUL characters, arbitrary Unicode, or deeply nested valid structures.

## Behavior

- Treat unclosed fenced code blocks and inline constructs according to CommonMark end-of-document rules.
- Preserve invalid syntax as literal content where the specification requires.
- Replace every U+0000 input character with U+FFFD.
- Accept arbitrary Unicode source text and emit valid UTF-8.
- Complete safely on empty input and documents containing only blank lines.
- Avoid unbounded recursion or delimiter failures on nested constructs.

## Programmatic Acceptance

=== AC boundaries-unclosed ===
Intent: The executable safely processes unclosed and invalid CommonMark constructs.

import subprocess

source = "```\nunclosed\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
=== END AC boundaries-unclosed ===

=== AC boundaries-nul ===
Intent: The executable accepts NUL-containing Markdown without a process failure and emits UTF-8 output.

import subprocess

source = "before\x00after\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
assert result.stdout
=== END AC boundaries-nul ===

=== AC boundaries-conformance ===
Intent: The implementation passes the authoritative bounded conformance examples relevant to malformed and unclosed input.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--spec",
        "sources/spec.txt",
        "--program",
        "./commonmark",
        "--pattern",
        r"^(Fenced code blocks|Code spans|Links|Images|Raw HTML)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC boundaries-conformance ===

## User Acceptance

- None.

## Guardrails

- Never crash on incomplete constructs or empty input.
- Replace U+0000 with U+FFFD before rendering.
- Do not invoke `full_test.sh` from scoped checks.
