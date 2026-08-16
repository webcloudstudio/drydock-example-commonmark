# Commonmark: DEGRADED

3 of 6 receipt claims proven. Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

## Receipt

| Claim | Verdict | Recorded outcome | Proof |
|---|---|---|---|
| Lifecycle completed | PASS | 17 lifecycle commands executed; the run ended at 17-score-release. Completed with a named shortfall; see the verdict above. | [result.json](result.json) |
| External conformance suite passed | FAIL | sh full_test.sh exited 2. | [evidence/commands/14-test.stdout.log](evidence/commands/14-test.stdout.log) |
| Target completion check passed | UNPROVEN | drydock status commonmark --check exited 1. | [evidence/commands/10-initial-complete.stdout.log](evidence/commands/10-initial-complete.stdout.log) |
| Acceptance score passed | FAIL | drydock score acceptance exited 1. | [evidence/commands/15-score-acceptance.stdout.log](evidence/commands/15-score-acceptance.stdout.log) |
| Release score passed | PASS | drydock score release exited 0. | [evidence/commands/17-score-release.stdout.log](evidence/commands/17-score-release.stdout.log) |
| Integrity verification passed | PASS | 200 files digested; verify with sha256sum -c SHA256SUMS. | [SHA256SUMS](SHA256SUMS) |

## Run facts

- Drydock: `unknown` (commit `29d6ad935e062c936916e0c045e2a4e90c396205`)
- Provider and model: `codex` / `gpt-5.6-luna`
- Platform: `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35` on Python `3.12.13`
- Target: `commonmark`
- Run: `20260815.175124`
- Ran: 2026-08-15 13:51:25 EDT — 2026-08-15 14:31:10 EDT
- Elapsed: 2385.3s
- LLM calls: 19
- Tokens: cached 14,667,776; uncached 1,498,221; output 84,036
- LLM elapsed: 2042.2s
- Build passes: 1; repairs: 6 attempts allowed
- Conformance: failed (exit 2)
- Verdict: expected PASSED, observed ERROR
- Advisory scores: acceptance=exit 1, build-report=exit 1, release=exit 0

## RUN SUMMARY

- Input specification: [`sources/INSTRUCTIONS.md`](sources/INSTRUCTIONS.md)
- Delivered Code: [`build/commonmark/`](build/commonmark)
- Test Results: [`evidence/commands/14-test.stdout.log`](evidence/commands/14-test.stdout.log)

## RUN NOTES:

- One run is evidence of one run. It is not a benchmark.
- It is not a security certification of the delivered code.

## Shortfall

- Degraded: initial-build-1 exited 1; test exited 2

## Manual verification required

The release gate completed. It could not settle the following project guardrails from evidence, so each needs a manual check before release.

- st-001 needs manual verification: The completed parser shall pass every test run by sh full_test.sh.

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock init commonmark` | 0 | 3.5s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import commonmark sources --format markdown` | 0 | 5.4s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock analyze commonmark` | 0 | 62.3s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) · [llm](evidence/llm_logs/20260815.175136.041Z_commonmark_analyze_codex.llm.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock plan commonmark --override` | 0 | 443.0s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) · [llm](evidence/llm_logs/20260815.175238.099Z_commonmark_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.175409.444Z_commonmark_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.175518.041Z_commonmark_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.175614.675Z_commonmark_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.175722.513Z_commonmark_plan_codex.llm.log) · [llm](evidence/llm_logs/20260815.175742.068Z_commonmark_lineage_attribute_codex.llm.log) · [llm](evidence/llm_logs/20260815.175810.993Z_commonmark_lineage_attribute_codex.llm.log) · [llm](evidence/llm_logs/20260815.175832.044Z_commonmark_lineage_attribute_codex.llm.log) · [llm](evidence/llm_logs/20260815.175904.646Z_commonmark_lineage_attribute_codex.llm.log) · [llm](evidence/llm_logs/20260815.175938.165Z_commonmark_lineage_attribute_codex.llm.log) |
| 05-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status commonmark` | 0 | 0.6s | [stdout](evidence/commands/05-after-plan-build-status.stdout.log) · [stderr](evidence/commands/05-after-plan-build-status.stderr.log) |
| 06-after-plan-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark` | 0 | 0.9s | [stdout](evidence/commands/06-after-plan-target-status.stdout.log) · [stderr](evidence/commands/06-after-plan-target-status.stderr.log) |
| 07-after-plan-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.4s | [stdout](evidence/commands/07-after-plan-workspace-status.stdout.log) · [stderr](evidence/commands/07-after-plan-workspace-status.stderr.log) |
| 08-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --ready` | 0 | 0.7s | [stdout](evidence/commands/08-initial-ready.stdout.log) · [stderr](evidence/commands/08-initial-ready.stderr.log) |
| 09-initial-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build commonmark --override --repair-attempts 6` | 1 | 1618.9s | [stdout](evidence/commands/09-initial-build-1.stdout.log) · [stderr](evidence/commands/09-initial-build-1.stderr.log) |
| 10-initial-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --check` | 1 | 0.4s | [stdout](evidence/commands/10-initial-complete.stdout.log) · [stderr](evidence/commands/10-initial-complete.stderr.log) |
| 11-after-initial-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status commonmark` | 0 | 0.9s | [stdout](evidence/commands/11-after-initial-build-build-status.stdout.log) · [stderr](evidence/commands/11-after-initial-build-build-status.stderr.log) |
| 12-after-initial-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark` | 0 | 1.3s | [stdout](evidence/commands/12-after-initial-build-target-status.stdout.log) · [stderr](evidence/commands/12-after-initial-build-target-status.stderr.log) |
| 13-after-initial-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.6s | [stdout](evidence/commands/13-after-initial-build-workspace-status.stdout.log) · [stderr](evidence/commands/13-after-initial-build-workspace-status.stderr.log) |
| 14-test | `sh full_test.sh` | 2 | 0.0s | [stdout](evidence/commands/14-test.stdout.log) · [stderr](evidence/commands/14-test.stderr.log) |
| 15-score-acceptance | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score ac commonmark` | 1 | 215.7s | [stdout](evidence/commands/15-score-acceptance.stdout.log) · [stderr](evidence/commands/15-score-acceptance.stderr.log) |
| 16-score-build-report | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score build commonmark` | 1 | 0.2s | [stdout](evidence/commands/16-score-build-report.stdout.log) · [stderr](evidence/commands/16-score-build-report.stderr.log) |
| 17-score-release | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score release commonmark` | 0 | 25.6s | [stdout](evidence/commands/17-score-release.stdout.log) · [stderr](evidence/commands/17-score-release.stderr.log) · [llm](evidence/llm_logs/20260815.183047.830Z_commonmark_score-release_codex.llm.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`evidence/llm_logs/`](evidence/llm_logs) — call banners and token accounting
- [`result.json`](result.json) — the machine-readable record of this run
