# FEATURE: Code Spans

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders CommonMark inline code spans. |
| Depends On  | ARCHITECTURE.md |
| Provides    | code spans |

## Purpose

Recognize matching backtick runs in inline content and render their contents as code.

## Behavior

- A code span opens with a run of one or more backticks and closes at the next run of exactly the same length.
- Convert line endings in code-span contents to spaces.
- Remove one leading and trailing space when both are present and the content is not entirely spaces.
- Preserve other content literally, including backslashes and character-reference syntax; escape it for HTML without interpreting Markdown inside the span.
- If no matching closing run exists, treat the opening backticks as literal text.

## Programmatic Acceptance

=== AC code-spans ===
Intent: The parser passes the complete supplied examples for code spans.
Suite: scoped
Requires: executable=python3; scope=test
Probe: --dump-tests
Probe Count: json

import os
import subprocess
import sys

pattern = "Code spans"
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
=== END AC code-spans ===

## User Acceptance

- None.

## Guardrails

- Preserve the supplied conformance assets unchanged.
- Do not use a public Markdown implementation as the parser.
