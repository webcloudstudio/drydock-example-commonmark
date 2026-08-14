# FEATURE: Normalized HTML Output

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Defines URL, title, attribute, entity, and special-character output compatibility with the supplied harness. |
| Depends On  | ARCHITECTURE.md, FEATURE-RENDER-INLINE.md |
| Provides    | normalized URL output, normalized title output, normalized attribute output |
| Consumes    | block HTML renderer, inline HTML renderer |

## Output Rules

- URLs preserve valid percent escapes and encode required spaces, Unicode characters, and backslashes.
- Titles and attribute values are HTML-escaped.
- Attribute output is deterministic and preserves required source semantics.
- Entity and numeric references are normalized consistently with the supplied harness.
- Special characters use the required HTML entities.
- Normalization compatibility does not alter code-block whitespace or raw HTML semantics.

## Programmatic Acceptance

=== AC render-normalization-suite ===
Intent: URL, title, attribute, entity, and special-character rendering passes its complete conformance scope.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Links|Images|Autolinks|Raw HTML|Entity and numeric character references)$"],
    capture_output=True, text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC render-normalization-suite ===

=== AC render-normalization-specials ===
Intent: Normalized output preserves URL escaping, title escaping, attribute semantics, and special characters.
Suite: scoped
Requires: executable=python3; scope=test

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "spec_tests.py", "--spec", "spec.txt", "--program", "./commonmark",
     "--pattern", "^(Links|Images|Autolinks|Raw HTML|Entity and numeric character references)$"],
    capture_output=True, text=True,
)
assert result.returncode == 0
=== END AC render-normalization-specials ===

## User Acceptance

- None.

## Guardrails

- Output normalization is deterministic and does not use a hardcoded pass tally.
- The supplied normalizer is used only as a comparison aid; its output is never the acceptance oracle.
