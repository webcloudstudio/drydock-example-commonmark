<!-- Compacted from ARCHITECTURE.md sha256=31c9332eb2d8fb03ce59b945037d21a6779e2a57c5095549568689664d6abc2d on 2026-10-14 by drydock build agent -->

Package: mdparser (stdlib only, no runtime deps, Python >=3.11)
Executable: ./commonmark (root, plain python3, no venv needed); calls mdparser.cli.main
Modules: cli (stdin bytes to stdout bytes, exit 0 always, diagnostics to stderr only), blocks (phase 1 block tree), refs (reference map, normalize_label = casefold + whitespace collapse), inlines (phase 2 delimiter stack), entities (html.entities.html5 names ending in ';' only, numeric refs, backslash unescape), render (HTML escape, URL percent-encoding)
Decisions: unicodedata P*/S* for flanking punctuation; soft line breaks render as a line ending; no third-party Markdown library
Guardrails: never write to sources/ staged assets; stdout carries only rendered HTML
