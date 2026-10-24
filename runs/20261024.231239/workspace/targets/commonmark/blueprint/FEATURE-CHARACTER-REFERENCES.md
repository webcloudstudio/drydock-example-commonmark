# FEATURE: Character References

| Field       | Value |
|-------------|-------|
| Version     | 20261024 V1 |
| Description | Parses valid HTML entity and numeric character references in inline content. |
| Depends On  | FEATURE-CLI.md, FEATURE-PARAGRAPHS.md |
| Provides    | entity and numeric character reference rendering |
| Consumes    | commonmark |

## Behavior

Recognize valid HTML5 named entity references and decimal or hexadecimal numeric references, each with a semicolon. Replace invalid Unicode scalar values and U+0000 with U+FFFD. Preserve invalid references as literal text, escaped for HTML. Do not recognize references in code spans or code blocks. References do not alter block-level Markdown structure.

## Programmatic Acceptance

=== AC character-reference-conformance ===
Intent: All supplied Entity and numeric character references examples pass.
Suite: scoped
Probe: --list
Probe Count: summary

import os
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "sources/spec_tests.py", "--program", "./commonmark",
     "--spec", "sources/spec.txt", "--pattern",
     "Entity and numeric character references"],
    capture_output=True, text=True,
    env={**os.environ, "PYTHONPATH": f"{os.getcwd()}/sources"},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC character-reference-conformance ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Keep all supplied scoring assets unchanged.
