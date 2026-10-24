# FEATURE: Escapes and Character References

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark backslash escapes and HTML character references. |
| Depends On  | ARCHITECTURE.md |
| Provides    | backslash escapes, entity and numeric character references |

## Purpose

Interpret backslash escapes and valid HTML entity and numeric character references in inline content according to CommonMark 0.31.2.

## Behavior

- A backslash escapes an ASCII punctuation character, rendering that character literally. A backslash before other characters remains literal.
- A backslash at the end of an inline line creates a hard line break.
- Recognize valid HTML5 named entities with semicolons, decimal references of one to seven digits, and hexadecimal references of one to six digits.
- Replace invalid Unicode code points and U+0000 with U+FFFD.
- Escape rendered text appropriately for HTML. References and escapes do not create block structure or replace structural Markdown markers.
- Do not interpret escapes or references inside code spans, code blocks, autolinks, or raw HTML.

## Programmatic Acceptance

=== AC escapes-and-character-references ===
Intent: The parser passes the complete supplied examples for backslash escapes and entity and numeric character references.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

pattern = "Backslash escapes|Entity and numeric character references"
environment = {
    **os.environ,
    "PYTHONPATH": os.pathsep.join(
        [os.path.abspath("sources"), os.environ.get("PYTHONPATH", "")]
    ).rstrip(os.pathsep),
}
result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.path.abspath("commonmark"),
        "--spec",
        "sources/spec.txt",
        "--pattern",
        pattern,
    ],
    capture_output=True,
    text=True,
    env=environment,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC escapes-and-character-references ===

## User Acceptance

- None.

## Guardrails

- Preserve the supplied conformance assets unchanged.
- Do not use a public Markdown implementation as the parser.
