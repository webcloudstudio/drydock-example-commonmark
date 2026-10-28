# Scorecard: commonmark

## Specification

> **NOT YET RUN**
> drydock score spec commonmark

## Acceptance

> **PASSED**
> drydock score ac commonmark · 2026-10-28T02:55:47.061+00:00

PASS 41   FAIL 0   UNVERIFIED 0   PREPASSED 5   (46 AC total)

## Build

> **RECORDED**
> drydock score build commonmark

Blocks: 14   Repaired: 1   Failed: 0
Tokens: 5,369,035 (cached 4,800,256, output 46,840)   Cache hit rate: 90.2%

## Release

> **RELEASED**
> drydock score release commonmark · 2026-10-28T02:59:16.184+00:00

- Verdict: PASSED

commonmark: PASSED — 1 of 1

  st-001  MET       sh sources/full_test.sh: exit code 0; 655 passed, 0 failed, 0 errored, 0 skipped

## Project acceptance

| ID | Type | Criterion | Verdict | Observed |
|---|---|---|---|---|
| st-001 | technical | The completed parser shall pass every test run by sh sources/full_test.sh. | MET | sh sources/full_test.sh: exit code 0; 655 passed, 0 failed, 0 errored, 0 skipped |

**Material decisions:**

- Standard-stream execution result — 
- Mixed conformance section ownership — 
