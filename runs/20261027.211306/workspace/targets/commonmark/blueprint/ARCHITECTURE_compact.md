<!-- Compacted from ARCHITECTURE.md sha256=0b53aaf9ed367aeab2084f4d0882095e4f24e6cda2057bcc6212d6fb00b1c1b1 on 2026-10-27 by drydock build agent -->

- Python 3.11+; standard library only at runtime. Root owns `pyproject.toml`, committed `uv.lock`, `.venv`, launchers, and `pytest -q`.
- Public interfaces: `commonmark_parser.render(markdown: str) -> str`; `commonmark_parser.blocks.parse_blocks(markdown: str) -> Document`; `commonmark_parser.inlines.parse_inlines(literal: str, references: dict) -> list`.
- `Document` exposes ordered `children` and document-wide `references`. Block nodes expose `kind`, `children`, and `literal`; headings also expose `level`.
- Parse block structure and collect references before parsing paragraph and heading inline content. Preserve raw inline source until that phase.
- Root executable `commonmark` reads UTF-8 Markdown from stdin and writes HTML to stdout.
- Keep `sources/spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh` verbatim under `sources/`. The runner imports sibling helpers and receives program and specification paths.
- Do not use a public Markdown implementation or modify the supplied conformance assets and full-suite entry point.
