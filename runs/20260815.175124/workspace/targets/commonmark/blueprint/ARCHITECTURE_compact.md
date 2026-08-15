<!-- Compacted from ARCHITECTURE.md sha256=5d12940336e991dd110f9831318fafa3500a2d785e5f30e8862b5a73491ce13d on 2026-08-15 by drydock build agent -->

Expose `commonmark.parse(text)`, `commonmark.render(document)`, and `commonmark.main()`. Preserve the pipeline: input normalization → block parsing/reference collection → inline parsing → HTML rendering. Use Python standard library only; stdin/stdout is the executable contract. Replace U+0000 with U+FFFD and preserve indentation/tabs.
