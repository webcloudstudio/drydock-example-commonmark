# COMPASS: CommonMark

## Compass
A command-line parser for people and tools that need Markdown converted to HTML. It reads UTF-8 Markdown from standard input, parses CommonMark 0.31.2, and writes HTML to standard output.

## Constraints
- Provide an executable named `commonmark` at the application root.
- Do not use a public Markdown implementation.
- Keep the supplied conformance assets read-only and stage them verbatim.

## Guardrails
- Do not modify `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, or `sources/spec.txt`.
- Do not create alternate scoring entry points or alter the supplied harness.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
