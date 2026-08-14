# Build Scorecard: commonmark

- Completion gate: INCOMPLETE
- Technical score: 96/100
- Code identity: fbe2a3c24923687cda7ed5bbd2ac5533856697d6

## Technical quality

| Dimension | Score | Gate |
|---|---:|---|
| Specification Completeness | 100 | PASS |
| Implementation Coverage | 94 | PASS |
| Test Coverage | 100 | PASS |
| Documentation Coverage | 80 | PASS |
| Blueprint Drift | 100 | PASS |
| Build Quality | 97 | PASS |
| Acceptance Criteria Coverage | 100 | PASS |

## Project acceptance

| ID | Type | Criterion | Required | Verdict | Evidence |
|---|---|---|---|---|---|
| st-001 | technical | The completed parser shall pass every test run by sh full_test.sh. | yes | PASS | FEATURE-CONFORMANCE-FULL.md:complete-conformance-suite=PASS |

## Completion blockers

- Manifest work is not closed/verified: block-quotes

## Manual verification required

- None.

## Advisory warnings

- Programmatic acceptance failed: cli-documentation-verification

## Ranked improvements

1. Close and verify the incomplete block-quotes Manifest work.
2. Update README.md to document the required complete-suite invocation: sh full_test.sh.
