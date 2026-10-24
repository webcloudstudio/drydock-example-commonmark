# Scorecard: commonmark

## Specification

> **NOT YET RUN**
> drydock score spec commonmark

## Acceptance

> **PASSED**
> drydock score ac commonmark · 2026-10-14T09:10:17.226+00:00

PASS 79   FAIL 0   UNVERIFIED 0   PREPASSED 47   (126 AC total)

## Build

> **RECORDED**
> drydock score build commonmark

Blocks: 24   Repaired: 0   Failed: 0
Tokens: 20,826,908 (cached 20,087,949, output 738,163)   Cache hit rate: 100.0%

## Release

> **RELEASED**
> drydock score release commonmark · 2026-10-14T09:13:02.123+00:00

- Verdict: PASSED

commonmark: PASSED — 1 of 1

  st-001  MET       governed_gate full: outcome PASS, return_code 0, timed_out false, duration 151886 ms; governed_gate stdout: "655 passed, 0 failed, 0 errored, 0 skipped"; code.dirty false, identity e9d2b96c72a51ed155f642ebd01891734085ca6e

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The completed parser shall pass every test run by sh sources/full_test.sh. | MET | governed_gate full: outcome PASS, return_code 0, timed_out false, duration 151886 ms; governed_gate stdout: "655 passed, 0 failed, 0 errored, 0 skipped"; code.dirty false, identity e9d2b96c72a51ed155f642ebd01891734085ca6e |

**Ranked improvements:**
1. Name the suite in the criterion (for example, 'the 655-case CommonMark conformance suite run by sh sources/full_test.sh') so a future change to the test script cannot silently shrink what 'every test' means.
2. Record the expected test count as a baseline in the trial, so a gate that passes with fewer cases than expected is flagged as a regression.

**Material decisions:**

- Corpus section ownership differs from ANALYSIS.md — 
- Dropping the final empty line in render_lines — 
- Image (![) constructs — 
- List grouping and tight/loose rendering implemented in this step — 
- Two earlier-block test expectations updated for raw HTML — 
