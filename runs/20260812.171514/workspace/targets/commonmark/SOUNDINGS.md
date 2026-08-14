# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Evidence | Verified At |
|---|---|---|---|---|---|
| ✓ PASS | ARCHITECTURE.md | architecture-boundaries | The implementation exposes separate block, inline, rendering, and executable boundaries. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-runtime-contract | The runtime contains the required POSIX conformance wrapper boundary. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-CLI-ENTRYPOINT.md | cli-stdin-stdout | The executable renders Markdown supplied through standard input and exits successfully. |  | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-CLI-ENTRYPOINT.md | cli-utf8 | The executable accepts UTF-8 Markdown and emits UTF-8 HTML. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-CLI-ERRORS.md | cli-errors-success-contract | A successful invocation returns zero and keeps diagnostics off standard error. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-CLI-ERRORS.md | cli-errors-stdout-integrity | The executable emits a complete HTML document result without diagnostic text in standard output. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-CLI-DOCUMENTATION.md | cli-documentation-content | README.md documents the standard-input and standard-output interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ✗ FAIL | FEATURE-CLI-DOCUMENTATION.md | cli-documentation-verification | README.md documents the required complete-suite invocation. | AssertionError | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-BLOCK-LEAF.md | leaf-blocks-primary | The implementation passes the supplied conformance sections for thematic breaks, headings, and code blocks. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-BLOCK-LEAF.md | leaf-blocks-secondary | The implementation passes the supplied conformance sections for HTML blocks, link references, paragraphs, and blank lines. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-BLOCK-QUOTES.md | block-quotes-basic | The implementation passes basic and nested block quote conformance examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-BLOCK-QUOTES.md | block-quotes-continuation | The implementation passes block quote laziness, blank-line, and contained-structure examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-BLOCK-LISTS.md | lists-structure | The implementation passes list marker, nesting, indentation, and continuation conformance examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-BLOCK-LISTS.md | lists-tightness | The implementation passes empty-item, delimiter, and tight-versus-loose list conformance examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-ESCAPES.md | inline-escapes | The implementation passes punctuation escape and escape-context conformance examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-ESCAPES.md | character-references | The implementation passes named, decimal, hexadecimal, invalid, and contextual character-reference examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-CODE-BREAKS.md | code-spans | The implementation passes code span delimiter, matching, normalization, and precedence examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-CODE-BREAKS.md | line-breaks | The implementation passes hard-break, soft-break, trailing-space, and break-context examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-EMPHASIS.md | emphasis-delimiters | The implementation passes delimiter-run, flanking, intraword, and modulo-three emphasis examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-EMPHASIS.md | emphasis-nesting | The implementation passes nested, overlapping, precedence, and unmatched delimiter examples. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-LINKS.md | inline-links-suite | The inline link, reference link, and image syntax passes its complete owned conformance scope. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-LINKS.md | inline-links-boundaries | The implementation preserves link and image destination, title, reference, and nesting behavior. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-HTML.md | inline-html-suite | The autolink and raw HTML syntax passes its complete owned conformance scope. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-INLINE-HTML.md | inline-html-malformed | Invalid autolinks and malformed HTML remain ordinary escaped content. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-RENDER-BLOCKS.md | render-blocks-suite | Block-level HTML rendering passes the complete owned conformance scope. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-RENDER-BLOCKS.md | render-blocks-escaping | Block rendering preserves structural nesting and escapes literal code content. |  | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-RENDER-INLINE.md | render-inline-suite | Inline HTML rendering passes the complete owned conformance scope. |  | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-RENDER-INLINE.md | render-inline-escaping | Inline rendering escapes text and code while preserving links, images, and raw HTML. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-RENDER-NORMALIZATION.md | render-normalization-suite | URL, title, attribute, entity, and special-character rendering passes its complete conformance scope. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-RENDER-NORMALIZATION.md | render-normalization-specials | Normalized output preserves URL escaping, title escaping, attribute semantics, and special characters. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-CONFORMANCE-ASSETS.md | conformance-assets-leaf-scope | The staged conformance harness executes a selected leaf-block scope successfully. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ~ PREPASSED | FEATURE-CONFORMANCE-ASSETS.md | conformance-assets-inline-scope | The staged conformance harness executes a selected inline scope successfully. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-12T20:47:46+00:00 |
| ✓ PASS | FEATURE-CONFORMANCE-FULL.md | complete-conformance-suite | The complete supplied CommonMark conformance suite passes through the required wrapper. |  | 2026-08-12T20:47:46+00:00 |
