# FEATURE: Full Conformance Verification

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Runs the complete unfiltered CommonMark 0.31.2 conformance suite through a POSIX-compatible wrapper. |
| Depends On  | FEATURE-CLI-Executable.md, FEATURE-CLI-Boundaries.md, FEATURE-Verification-Scoped.md |
| Provides    | full_test.sh, terminal conformance proof |
| Consumes    | commonmark stdin/stdout executable, staged conformance assets |

## Workflow

The terminal verification workflow stages `spec.txt`, `spec_tests.py`, `cmark.py`, and
`normalize.py`, creates an executable-compatible `full_test.sh` wrapper, and runs the
complete supplied suite without selectors. The wrapper must remain POSIX-compatible and
must return the conformance runner's exit status.

The terminal verdict is determined only by the process exit code. Captured standard output
and standard error are printed for diagnosis and are not parsed as acceptance criteria.

## Programmatic Acceptance

Requires: executable=sh; scope=test

=== AC full-conformance-suite ===
Intent: The complete unfiltered supplied CommonMark conformance suite succeeds through the required POSIX wrapper.
Suite: full

import subprocess

result = subprocess.run(
    ["sh", "full_test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC full-conformance-suite ===

## User Acceptance

- None.

## Guardrails

- `full_test.sh` must be POSIX-compatible.
- The complete suite must run without `--pattern`, `--number`, or other selectors.
- This is the only story that invokes the unfiltered suite.
- The verdict must use only the wrapper process exit code; suite tally text must not be parsed or asserted.
- No public Markdown implementation may be used.
