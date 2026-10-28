# COMPASS: CommonMark

## Compass
CommonMark is a command-line parser for users who need Markdown converted to HTML. It implements the supplied CommonMark 0.31.2 specification and reads UTF-8 Markdown from standard input, writing HTML to standard output through the root executable `commonmark`.

## Constraints
- Provide an executable named `commonmark` at the application root.
- Preserve the standard-input and standard-output interface.
- Parse block structure before inline content and resolve reference definitions across the document.
- Keep the supplied conformance assets unchanged; they are restored and hash-verified before grading.
- Stage the supplied runtime conformance assets verbatim under `sources/`.

## Guardrails
- Do not use a public Markdown implementation.
- Do not modify or replace the supplied full-suite entry point.
- Do not invoke the full-suite entry point from scoped implementation checks.
- Do not add file-presence checks or additional verification stories.

<!-- drydock:build-write-guardrail:start -->
## Build Write Guardrail

- Authorized build directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark`
- Authorized Target directory: `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark`
- Build agents have permission to create, modify, and remove files required by the active build block inside these authorized directories.
- No path outside these authorized directories may be modified.
- Protected Drydock artifacts:
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark/blueprint/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark/MANIFEST.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark/COMPASS.md`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark/QuarterDeck/`
  - `/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/workspace/targets/commonmark/evidence/`
<!-- drydock:build-write-guardrail:end -->
