# COMPASS: CommonMark

## Compass
CommonMark is a command-line parser for converting Markdown into HTML. It serves callers that provide Markdown on standard input and expect rendered HTML on standard output, with behavior conforming to CommonMark 0.31.2.

## Constraints
- Deliver an executable named `commonmark` at the application root.
- Read UTF-8 Markdown from standard input and write HTML to standard output.
- Keep the supplied conformance assets unchanged; they are hash-verified and restored before grading.
- Include a concise project README describing the standard-input/standard-output interface.

## Guardrails
- Do not use a public Markdown implementation.
- Do not modify or replace the supplied scoring entry point.
- Do not modify the supplied conformance suite, helpers, or specification.
- The final acceptance run must use the complete unfiltered supplied suite.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
