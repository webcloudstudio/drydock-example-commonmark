# CommonMark: PASSED

Open `index.html` for the linked proof kit; verify it with `sha256sum -c SHA256SUMS`.

- Target: `commonmark`
- Run: `20260812.171514`
- Ran: 2026-08-12 13:15:15 EDT — 2026-08-12 17:21:19 EDT
- Provider and model: `codex` / `gpt-5.6-luna`
- Elapsed: 14764.7s
- Build passes: 1
- LLM calls: 39
- Tokens: cached 77,868,800; uncached 4,047,230; output 244,177
- LLM elapsed: 10205.2s
- Advisory scores: acceptance=exit 1, build-report=exit 0, release=exit 1

## Commands

| # | Command | Exit | Elapsed | Output |
|---|---|---|---|---|
| 01-init | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock init commonmark` | 0 | 1.5s | [stdout](evidence/commands/01-init.stdout.log) · [stderr](evidence/commands/01-init.stderr.log) |
| 02-import-sources | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock import commonmark sources --format markdown` | 0 | 1.9s | [stdout](evidence/commands/02-import-sources.stdout.log) · [stderr](evidence/commands/02-import-sources.stderr.log) |
| 03-analyze | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock analyze commonmark` | 0 | 68.9s | [stdout](evidence/commands/03-analyze.stdout.log) · [stderr](evidence/commands/03-analyze.stderr.log) |
| 04-plan | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock plan commonmark --override` | 0 | 647.4s | [stdout](evidence/commands/04-plan.stdout.log) · [stderr](evidence/commands/04-plan.stderr.log) |
| 05-after-plan-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status commonmark` | 0 | 1.5s | [stdout](evidence/commands/05-after-plan-build-status.stdout.log) · [stderr](evidence/commands/05-after-plan-build-status.stderr.log) |
| 06-after-plan-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark` | 0 | 2.0s | [stdout](evidence/commands/06-after-plan-target-status.stdout.log) · [stderr](evidence/commands/06-after-plan-target-status.stderr.log) |
| 07-after-plan-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.8s | [stdout](evidence/commands/07-after-plan-workspace-status.stdout.log) · [stderr](evidence/commands/07-after-plan-workspace-status.stderr.log) |
| 08-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --ready` | 0 | 0.7s | [stdout](evidence/commands/08-initial-ready.stdout.log) · [stderr](evidence/commands/08-initial-ready.stderr.log) |
| 09-initial-build-1 | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build commonmark --override --repair-attempts 6` | 0 | 11851.5s | [stdout](evidence/commands/09-initial-build-1.stdout.log) · [stderr](evidence/commands/09-initial-build-1.stderr.log) |
| 10-initial-ready | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --ready` | 1 | 0.7s | [stdout](evidence/commands/10-initial-ready.stdout.log) · [stderr](evidence/commands/10-initial-ready.stderr.log) |
| 11-initial-complete | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark --check` | 0 | 0.8s | [stdout](evidence/commands/11-initial-complete.stdout.log) · [stderr](evidence/commands/11-initial-complete.stderr.log) |
| 12-after-initial-build-build-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock build status commonmark` | 0 | 1.3s | [stdout](evidence/commands/12-after-initial-build-build-status.stdout.log) · [stderr](evidence/commands/12-after-initial-build-build-status.stderr.log) |
| 13-after-initial-build-target-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status commonmark` | 0 | 2.3s | [stdout](evidence/commands/13-after-initial-build-target-status.stdout.log) · [stderr](evidence/commands/13-after-initial-build-target-status.stderr.log) |
| 14-after-initial-build-workspace-status | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock status` | 0 | 0.7s | [stdout](evidence/commands/14-after-initial-build-workspace-status.stdout.log) · [stderr](evidence/commands/14-after-initial-build-workspace-status.stderr.log) |
| 15-test | `sh full_test.sh` | 0 | 168.6s | [stdout](evidence/commands/15-test.stdout.log) · [stderr](evidence/commands/15-test.stderr.log) |
| 16-score-acceptance | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score ac commonmark` | 1 | 1129.4s | [stdout](evidence/commands/16-score-acceptance.stdout.log) · [stderr](evidence/commands/16-score-acceptance.stderr.log) |
| 17-score-build-report | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score build commonmark` | 0 | 1.3s | [stdout](evidence/commands/17-score-build-report.stdout.log) · [stderr](evidence/commands/17-score-build-report.stderr.log) |
| 18-score-release | `/mnt/c/Users/barlo/projects/drydock/.venv/bin/python3 -m drydock score release commonmark` | 1 | 870.3s | [stdout](evidence/commands/18-score-release.stdout.log) · [stderr](evidence/commands/18-score-release.stderr.log) |

## Evidence

- [`evidence/commands/`](evidence/commands) — stdout and stderr of every command
- [`evidence/prompts/`](evidence/prompts) — the assembled prompt for every LLM call
- [`evidence/provider_raw/`](evidence/provider_raw) — unmodified provider transcripts
- [`result.json`](result.json) — the machine-readable record of this run
