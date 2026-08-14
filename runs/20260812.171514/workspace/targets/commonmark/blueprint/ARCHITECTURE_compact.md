<!-- Compacted from ARCHITECTURE.md sha256=4401f1eb6d106328681e1aa590de8dce5877d0b58de586bde20e42052098f6e8 on 2026-08-12 by drydock build agent -->

CommonMark is a Python 3 CLI parser that reads UTF-8 Markdown from standard input, parses blocks before inlines, and writes CommonMark 0.31.2 HTML to standard output. Runtime boundaries are `cmark`, `parser`, `renderer`, and `full_test.sh`; no public Markdown implementation or third-party dependencies are used.
