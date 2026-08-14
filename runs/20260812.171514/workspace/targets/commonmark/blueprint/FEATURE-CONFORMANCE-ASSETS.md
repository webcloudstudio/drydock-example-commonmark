# FEATURE: Conformance Assets

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Stages the supplied CommonMark conformance assets and supports bounded verification. |
| Depends On  | FEATURE-RENDER-NORMALIZATION.md |
| Provides    | staged conformance assets, bounded conformance verification |
| Consumes    | parser executable |

## Workflow

The build stages only `spec.txt`, `spec_tests.py`, `cmark.py`, and `normalize.py` at the runtime paths required by the supplied harness. `INSTRUCTIONS.md` remains planning context and is not staged.

Bounded verification invokes `spec_tests.py` with explicit section selectors. It never invokes an unfiltered suite. The harness uses the parser executable through its standard-input and standard-output contract.

## Staged Assets

| Source | Runtime destination |
|---|---|
| `sources/spec.txt` | `spec.txt` |
| `sources/spec_tests.py` | `spec_tests.py` |
| `sources/cmark.py` | `cmark.py` |
| `sources/normalize.py` | `normalize.py` |

## Programmatic Acceptance

Requires: executable=python3; scope=test

=== AC conformance-assets-leaf-scope ===
Intent: The staged conformance harness executes a selected leaf-block scope successfully.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "spec_tests.py",
        "--spec",
        "spec.txt",
        "--program",
        "./program",
        "--pattern",
        "^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|Blank lines)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC conformance-assets-leaf-scope ===

=== AC conformance-assets-inline-scope ===
Intent: The staged conformance harness executes a selected inline scope successfully.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "spec_tests.py",
        "--spec",
        "spec.txt",
        "--program",
        "./program",
        "--pattern",
        "^(Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC conformance-assets-inline-scope ===

## User Acceptance

- None.

## Guardrails

- Only the four required conformance assets are staged.
- Bounded checks use explicit example-bearing section selectors.
- The complete unfiltered suite is reserved for the terminal verification story.
