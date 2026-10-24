# FEATURE: Block Quotes

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses CommonMark block quotes and their nested block content. |
| Depends On  | ARCHITECTURE.md |
| Provides    | block quotes |

## Purpose

Parse block quotes as containers whose contents are parsed using the ordinary block rules.

## Behavior

- A block quote marker is `>` optionally preceded by up to three spaces; one following space or tab is part of the marker and is removed from the content.
- Consecutive marked lines form a quote. Blank marked lines can occur within it.
- Support lazy continuation only for lines that continue an existing paragraph. Do not apply laziness to block starts, code blocks, or other lines that require an explicit quote marker.
- Support nested block quotes and all block types inside quotes.
- A blank line separates consecutive block quotes. Quotes may interrupt paragraphs.

## Programmatic Acceptance

=== AC block-quotes ===
Intent: The parser passes the complete supplied examples for block quotes.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

pattern = "Block quotes"
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
=== END AC block-quotes ===

## User Acceptance

- None.

## Guardrails

- Preserve the supplied conformance assets unchanged.
- Do not use a public Markdown implementation as the parser.
