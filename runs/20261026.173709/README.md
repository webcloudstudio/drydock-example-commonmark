# COMMONMARK

- Short description: A command-line parser that converts Markdown from standard input to HTML on standard output.
- Status: BLOCKED: UAT STAGE

1 of 4 receipt claims proven. Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

## Receipt

| Claim | Verdict | Recorded outcome | Proof |
|---|---|---|---|
| Lifecycle completed | FAIL | 8 lifecycle commands executed; the run ended at 08-after-plan-build-status. | [result.json](result.json) |
| External conformance suite passed | UNPROVEN | The configured external conformance suite was not executed. | — |
| Release score passed | UNPROVEN | No release score was recorded for this run. | — |
| Integrity verification passed | PASS | 241 files digested; verify with sha256sum -c SHA256SUMS. | [SHA256SUMS](SHA256SUMS) |

## Run facts

- Drydock: `0.8.0` (commit `59bed716137885ddcb214fefb76dbb9e400f6fbf`)
- Provider and model: `codex` / `gpt-6-luna`
- Platform: `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35` on Python `3.12.13`
- Run: `20261026.173709`
- Elapsed: 455.8s
- LLM calls: 12
- Tokens: cached 138,240; uncached 753,719; output 23,103
- LLM elapsed: 260.5s
- Build passes: 0; repairs: not recorded
- Conformance: not executed
- Advisory scores: none recorded

## RUN SUMMARY

- Input specification: [`sources/INSTRUCTIONS.md`](sources/INSTRUCTIONS.md)
- Delivered Code: [`build/commonmark/`](build/commonmark)
- Test Results: not recorded for this run.

## Shortfall

- Failure: CommonMark: stopped at plan-repair: acceptance criteria still cannot run after one repair pass

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock init commonmark` | 0 | 3.6s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock import commonmark sources --format markdown` | 0 | 6.7s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock analyze commonmark` | 0 | 44.9s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) · [llm](evidence/commands/03-analyze.llm.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock plan commonmark --override` | 0 | 282.5s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) · [llm](evidence/commands/04-plan.llm.log) |
| 05-plan-verify | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock plan verify commonmark` | 1 | 32.5s | [stdout](evidence/commands/05-plan-verify.stdout.log) · [stderr](evidence/commands/05-plan-verify.stderr.log) |
| 06-plan-repair | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock plan repair commonmark` | 1 | 52.9s | [stdout](evidence/commands/06-plan-repair.stdout.log) · [stderr](evidence/commands/06-plan-repair.stderr.log) |
| 07-plan-verify-after-repair | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock plan verify commonmark` | 1 | 27.0s | [stdout](evidence/commands/07-plan-verify-after-repair.stdout.log) · [stderr](evidence/commands/07-plan-verify-after-repair.stderr.log) |
| 08-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python -m drydock build status commonmark` | 1 | 1.0s | [stdout](evidence/commands/08-after-plan-build-status.stdout.log) · [stderr](evidence/commands/08-after-plan-build-status.stderr.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`evidence/llm_logs/`](evidence/llm_logs) — call banners and token accounting
- [`result.json`](result.json) — the machine-readable record of this run
