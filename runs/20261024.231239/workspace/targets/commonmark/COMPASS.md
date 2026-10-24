# COMPASS: CommonMark

## Compass
CommonMark is a command-line parser for converting CommonMark Markdown into HTML. It serves callers that provide Markdown on standard input and consume HTML on standard output, with conformance to the supplied CommonMark 0.31.2 specification as the project goal.

## Constraints
- Deliver an executable named `commonmark` at the application root.
- Read Markdown from standard input and write HTML to standard output.
- Preserve the supplied scoring assets unchanged; they are restored and hash-verified before grading.
- Keep the instructions file out of the staged application; stage the specified runtime conformance assets.

## Guardrails
- Do not use a public Markdown implementation.
- Do not modify or replace `sources/full_test.sh` or other supplied scoring assets.
- Do not run the full suite from scoped implementation checks; reserve it for the terminal verification story.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261024.231239/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
