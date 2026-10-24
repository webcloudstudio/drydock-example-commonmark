# COMPASS: CommonMark

## Compass
Build a command-line parser that converts CommonMark 0.31.2 Markdown to HTML. It serves callers that provide Markdown on standard input and consume HTML on standard output. The deliverable is an executable named `commonmark` at the application root.

## Constraints
- Read UTF-8 Markdown from standard input and write HTML to standard output.
- Follow the supplied CommonMark 0.31.2 specification and parsing strategy.
- Keep the supplied conformance assets under `sources/` unchanged.

## Guardrails
- Do not use a public Markdown implementation as the parser.
- Do not modify the supplied scoring assets; changes are reported as tampering.
- Do not author or replace `sources/full_test.sh`.
- Run the full supplied suite only in the terminal verification story.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.233753/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
