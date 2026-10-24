# COMPASS: commonmark

## Compass
This product is a CommonMark 0.31.2 parser delivered as a single executable, `commonmark`, at the application root. It reads UTF-8 Markdown from standard input and writes HTML to standard output. It is built from the supplied specification text, following the Appendix parsing strategy (block structure first, then inline parsing with the delimiter-stack algorithms). Success means the complete supplied conformance suite passes when run unfiltered through `sh sources/full_test.sh`.

## Constraints
- The deliverable is an executable named `commonmark` at the application root.
- Input is UTF-8 on stdin; output is HTML on stdout; no arguments are required.
- `spec.txt` is normative; the spec's Appendix gives the reference parsing algorithms to follow directly.
- The runner compares normalized HTML, so tag structure, entities, and URL percent-encoding of non-ASCII characters must match the spec examples.
- `sources/INSTRUCTIONS.md` is prose only and is not staged; the staged runtime assets are `spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh`.
- A concise `README.md` describes the stdin/stdout interface; it is not an acceptance criterion.

## Guardrails
- Never use or call a public Markdown implementation.
- Never modify `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, or `sources/spec.txt`; they are hash-verified and restored before grading.
- Never filter, skip, or reinterpret tests; changing the entry point is not a repair.
- Never write anything but rendered HTML to stdout.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
