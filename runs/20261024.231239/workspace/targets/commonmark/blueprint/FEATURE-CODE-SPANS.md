# FEATURE: Code Spans

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses and renders inline CommonMark code spans. |
| Depends On  | FEATURE-CLI.md, FEATURE-PARAGRAPHS.md |
| Provides    | inline code spans |
| Consumes    | commonmark |

## Behavior

Match opening and closing backtick runs of equal length. Convert line endings in the contents to spaces. Remove one leading and trailing ASCII space only when both are present and the content is not entirely spaces. Preserve all other content literally, escaping it for HTML. Backslash escapes and character references are not processed inside code spans.

## Programmatic Acceptance

=== AC code-span-conformance ===
Intent: All supplied Code spans examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern", "Code spans"],
    capture_output=True, text=True,
    env={**os.environ, "PYTHONPATH": f"{os.getcwd()}/sources"},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC code-span-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep all supplied scoring assets unchanged.
