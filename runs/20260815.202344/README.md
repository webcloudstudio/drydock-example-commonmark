# CommonMark: PASSED

5 of 6 receipt claims proven. Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

## Receipt

| Claim | Verdict | Recorded outcome | Proof |
|---|---|---|---|
| Lifecycle completed | PASS | 18 lifecycle commands executed; the run ended at 18-score-release. | [result.json](result.json) |
| External conformance suite passed | PASS | sh sources/full_test.sh exited 0. | [evidence/commands/15-test.stdout.log](evidence/commands/15-test.stdout.log) |
| Target completion check passed | UNPROVEN | drydock status commonmark --check exited 1. | [evidence/commands/11-initial-complete.stdout.log](evidence/commands/11-initial-complete.stdout.log) |
| Acceptance score passed | PASS | drydock score acceptance exited 0. | [evidence/commands/16-score-acceptance.stdout.log](evidence/commands/16-score-acceptance.stdout.log) |
| Release score passed | PASS | drydock score release exited 0. | [evidence/commands/18-score-release.stdout.log](evidence/commands/18-score-release.stdout.log) |
| Integrity verification passed | PASS | 234 files digested; verify with sha256sum -c SHA256SUMS. | [SHA256SUMS](SHA256SUMS) |

## Run facts

- Drydock: `0.1.8` (commit `ed677ad07fdef9340e3a9ef73d582e071c71e90e`)
- Provider and model: `codex` / `gpt-5.6-luna`
- Platform: `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35` on Python `3.12.13`
- Target: `commonmark`
- Run: `20260815.202344`
- Ran: 2026-08-15 20:18:24 EDT — 2026-08-15 20:22:13 EDT
- Elapsed: 228.8s
- LLM calls: 25
- Tokens: cached 41,656,320; uncached 1,993,137; output 147,678
- LLM elapsed: 4528.3s
- Build passes: 1; repairs: 6 attempts allowed
- Conformance: passed
- Verdict: expected PASSED, observed PASSED
- Advisory scores: acceptance=exit 0, build-report=exit 0, release=exit 0

## RUN SUMMARY

- Input specification: [`sources/INSTRUCTIONS.md`](sources/INSTRUCTIONS.md)
- Delivered Code: [`build/commonmark/`](build/commonmark)
- Test Results: [`evidence/commands/15-test.stdout.log`](evidence/commands/15-test.stdout.log)

## RUN NOTES:

- One run is evidence of one run. It is not a benchmark.
- It is not a security certification of the delivered code.

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock init commonmark` | 0 | 2.2s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import commonmark sources --format markdown` | 0 | 2.2s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock analyze commonmark` | 0 | 65.3s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock plan commonmark --override` | 0 | 320.3s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) |
| 05-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status commonmark` | 0 | 0.6s | [stdout](evidence/commands/05-after-plan-build-status.stdout.log) · [stderr](evidence/commands/05-after-plan-build-status.stderr.log) |
| 06-after-plan-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark` | 0 | 0.8s | [stdout](evidence/commands/06-after-plan-target-status.stdout.log) · [stderr](evidence/commands/06-after-plan-target-status.stderr.log) |
| 07-after-plan-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.4s | [stdout](evidence/commands/07-after-plan-workspace-status.stdout.log) · [stderr](evidence/commands/07-after-plan-workspace-status.stderr.log) |
| 08-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --ready` | 0 | 0.5s | [stdout](evidence/commands/08-initial-ready.stdout.log) · [stderr](evidence/commands/08-initial-ready.stderr.log) |
| 09-initial-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build commonmark --override --repair-attempts 6` | 0 | 4400.9s | [stdout](evidence/commands/09-initial-build-1.stdout.log) · [stderr](evidence/commands/09-initial-build-1.stderr.log) |
| 10-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --ready` | 1 | 0.4s | [stdout](evidence/commands/10-initial-ready.stdout.log) · [stderr](evidence/commands/10-initial-ready.stderr.log) |
| 11-initial-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --check` | 1 | 0.2s | [stdout](evidence/commands/11-initial-complete.stdout.log) · [stderr](evidence/commands/11-initial-complete.stderr.log) |
| 12-after-initial-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status commonmark` | 0 | 0.6s | [stdout](evidence/commands/12-after-initial-build-build-status.stdout.log) · [stderr](evidence/commands/12-after-initial-build-build-status.stderr.log) |
| 13-after-initial-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark` | 0 | 0.8s | [stdout](evidence/commands/13-after-initial-build-target-status.stdout.log) · [stderr](evidence/commands/13-after-initial-build-target-status.stderr.log) |
| 14-after-initial-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.5s | [stdout](evidence/commands/14-after-initial-build-workspace-status.stdout.log) · [stderr](evidence/commands/14-after-initial-build-workspace-status.stderr.log) |
| 15-test | `sh sources/full_test.sh` | 0 | 45.4s | [stdout](evidence/commands/15-test.stdout.log) · [stderr](evidence/commands/15-test.stderr.log) |
| 16-score-acceptance | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score ac commonmark` | 0 | 146.4s | [stdout](evidence/commands/16-score-acceptance.stdout.log) · [stderr](evidence/commands/16-score-acceptance.stderr.log) |
| 17-score-build-report | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score build commonmark` | 0 | 0.5s | [stdout](evidence/commands/17-score-build-report.stdout.log) · [stderr](evidence/commands/17-score-build-report.stderr.log) |
| 18-score-release | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score release commonmark` | 0 | 73.2s | [stdout](evidence/commands/18-score-release.stdout.log) · [stderr](evidence/commands/18-score-release.stderr.log) · [llm](evidence/commands/18-score-release.llm.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`evidence/llm_logs/`](evidence/llm_logs) — call banners and token accounting
- [`result.json`](result.json) — the machine-readable record of this run
