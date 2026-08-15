# FEATURE: Scoped Verification

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Stage conformance assets and provide bounded specification-section checks. |
| Depends On  | FEATURE-CLI-Executable.md |
| Provides    | scoped conformance verification |
| Consumes    | commonmark stdin/stdout executable |

## Verification Contract

The build environment stages the normative specification and its test helpers at:

- `sources/spec.txt`
- `sources/spec_tests.py`
- `sources/cmark.py`
- `sources/normalize.py`

Scoped verification invokes `spec_tests.py` with explicit `--pattern` or `--number` selectors. It must never invoke `full_test.sh`; the unfiltered suite is reserved for `FEATURE-Verification-Full.md`.

## Programmatic Acceptance

=== AC scoped-section ===
Intent: A selected CommonMark specification section executes successfully against the completed executable.
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
        r"^ATX headings$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC scoped-section ===

=== AC scoped-example ===
Intent: A single explicitly selected CommonMark example executes successfully against the completed executable.
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
        "--number",
        "1",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC scoped-example ===

## User Acceptance

- None.

## Guardrails

- Use explicit specification section or example selectors for every scoped check.
- Never invoke `full_test.sh` from scoped verification.
- Treat the conformance runner's exit status as the verdict; do not assert on printed tallies.
- Do not modify the staged conformance assets.
