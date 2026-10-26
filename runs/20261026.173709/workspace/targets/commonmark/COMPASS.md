# COMPASS: CommonMark

## Compass
CommonMark is a command-line parser for converting Markdown documents into HTML. It serves callers that provide Markdown on standard input and consume rendered HTML on standard output. Build it to conform to the supplied CommonMark 0.31.2 specification and conformance examples.

## Constraints
- Deliver an executable named `commonmark` at the application root.
- Read UTF-8 Markdown from standard input and write HTML to standard output.
- Resolve block structure before inline structure, including document-wide link reference definitions.
- Keep the supplied scoring assets unchanged; they are restored and hash-verified before grading.
- The complete scoring command is `sh sources/full_test.sh`.

## Guardrails
- Do not use a public Markdown implementation.
- Do not modify or replace the supplied scoring entry point or its assets.
- Do not invoke the full scoring harness from scoped parser checks.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261026.173709/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
