<!-- Compacted from ARCHITECTURE.md sha256=b6be7922c807305623c683775ec769166358dffdbb4519164fbc5233efaf62fc on 2026-10-24 by drydock build agent -->

- Provide an importable Python package named `commonmark`.
- Keep parsing self-contained; do not depend on a public Markdown implementation.
- Flow: block parser builds document structure and collects document-wide link references; inline parser processes content using that reference map; renderer emits HTML.
- The CLI reads UTF-8 Markdown from stdin and writes HTML to stdout.
- Boundaries: block parsing, inline parsing, HTML rendering, and CLI. No persistence, configuration, file store, or external service boundary.
- Acceptance: `importlib.util.find_spec("commonmark")` must return a package spec with `submodule_search_locations`; `pytest -q` must succeed.
