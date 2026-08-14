# FEATURE: Complete Conformance Verification

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Runs the complete supplied CommonMark conformance suite through a POSIX wrapper. |
| Depends On  | FEATURE-CONFORMANCE-ASSETS.md, FEATURE-RENDER-NORMALIZATION.md |
| Provides    | full_test.sh, complete conformance verification |
| Consumes    | parser executable, staged conformance assets |

## Workflow

`full_test.sh` is a repository-local POSIX shell wrapper. It invokes the staged `spec_tests.py` harness with `spec.txt`, `cmark.py`, and `normalize.py` available at their required runtime paths. It runs the complete suite without a section selector or test-number filter.

The wrapper preserves the harness exit status. A zero exit status means the complete suite passed. A nonzero exit status means verification failed.

## Programmatic Acceptance

Requires: executable=sh; scope=test

=== AC complete-conformance-suite ===
Intent: The complete supplied CommonMark conformance suite passes through the required wrapper.
Suite: full
Sea Trials: st-001

import subprocess

result = subprocess.run(
    ["sh", "full_test.sh"],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
=== END AC complete-conformance-suite ===

## User Acceptance

- None.

## Guardrails

- `full_test.sh` runs the supplied suite without filtering.
- The suite runner's exit status is the sole acceptance verdict.
- The wrapper does not parse or hardcode the suite tally.
