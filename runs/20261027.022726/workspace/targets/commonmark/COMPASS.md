# COMPASS: CommonMark

## Compass
Build a command-line parser that converts CommonMark 0.31.2 Markdown into HTML for callers supplying documents on standard input. The executable writes the rendered HTML to standard output and must conform to the supplied specification examples.

## Constraints
- Provide an executable named `commonmark` at the application root.
- Read UTF-8 Markdown from standard input and write HTML to standard output.
- Parse block structure before inline structure; make collected reference definitions available to inline parsing.
- Do not use a public Markdown implementation.
- Treat the supplied conformance assets as read-only.

## Guardrails
- Never modify the supplied scoring harness, runner, normalizer, reference wrapper, or specification.
- Do not alter the full-suite entry point to repair implementation failures.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
