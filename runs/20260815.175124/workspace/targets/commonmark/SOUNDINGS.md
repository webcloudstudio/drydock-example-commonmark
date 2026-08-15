# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Evidence | Verified At |
|---|---|---|---|---|---|
| ✓ PASS | ARCHITECTURE.md | architecture-input-boundary | The implementation exposes an input-normalization boundary that accepts text input. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-render-boundary | The implementation exposes a rendering boundary that accepts a parsed document. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | ARCHITECTURE.md | architecture-cli-boundary | The executable module exposes a callable process entry point. |  | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Block-Input.md | block-input-tabs | The implementation passes the complete Tabs conformance section. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ~ PREPASSED | FEATURE-Block-Input.md | block-input-characters | The implementation passes the complete Characters and lines conformance section. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T18:27:04+00:00 |
| ~ PREPASSED | FEATURE-Block-Input.md | block-input-insecure | The implementation passes the complete Insecure characters conformance section. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-Block-Leaves.md | block-leaves-basic | The implementation passes thematic-break, ATX-heading, and setext-heading conformance sections. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-Block-Leaves.md | block-leaves-code | The implementation passes indented-code and fenced-code conformance sections. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-Block-Leaves.md | block-leaves-html | The implementation passes the complete HTML-block conformance section. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-Block-References.md | block-references-valid | The implementation passes the complete valid link-reference-definition conformance coverage. |  | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Block-References.md | block-references-container | The implementation passes reference-definition cases involving document-wide and container-scoped definitions. | TypeError: expected str, bytes or os.PathLike object, not int | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Block-Quotes.md | block-quotes-conformance | The implementation passes the complete Block quotes conformance section. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Block-Quotes.md | block-quotes-nesting | The implementation passes nested and lazy block-quote examples within the authoritative section. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Block-Lists.md | block-lists-conformance | The implementation passes the authoritative CommonMark examples for list items and lists owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Block-Lists.md | block-lists-selector | The list conformance selector executes the owned specification sections successfully. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Escapes.md | inline-escapes-conformance | The implementation passes the authoritative CommonMark examples for backslash escapes and entity or numeric character references owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Escapes.md | inline-escapes-selector | The escape and character-reference conformance selector executes successfully. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Code-Breaks.md | inline-code-breaks-conformance | The implementation passes the authoritative CommonMark examples for code spans and hard or soft line breaks owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Code-Breaks.md | inline-code-breaks-selector | The code-span and line-break conformance selector executes successfully. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Emphasis.md | inline-emphasis-conformance | The implementation passes the authoritative CommonMark examples for emphasis and strong emphasis owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Emphasis.md | inline-emphasis-selector | The emphasis conformance selector executes the complete owned specification section successfully. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Links.md | inline-links-conformance | The implementation passes the authoritative CommonMark examples for links and images owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-Links.md | inline-links-selector | The link and image conformance selector executes the complete owned specification sections successfully. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-HTML-Autolinks.md | inline-autolinks | The implementation passes the authoritative CommonMark autolink examples owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Inline-HTML-Autolinks.md | inline-raw-html | The implementation passes the authoritative CommonMark raw HTML examples owned by this story. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-HTML-Renderer.md | renderer-conformance | The renderer passes the authoritative conformance examples covering the implemented rendered surface. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-HTML-Renderer.md | renderer-processes-document | The renderer produces a nonempty HTML document for a valid Markdown document. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-CLI-Executable.md | cli-stdin-stdout | The executable accepts Markdown on standard input and returns successful HTML output on standard output. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-CLI-Executable.md | cli-utf8 | The executable accepts UTF-8 Markdown and emits UTF-8 output without a decoding failure. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-CLI-Executable.md | cli-empty-input | The executable completes successfully for an empty standard-input document. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-CLI-Boundaries.md | boundaries-unclosed | The executable safely processes unclosed and invalid CommonMark constructs. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-CLI-Boundaries.md | boundaries-nul | The executable accepts NUL-containing Markdown without a process failure and emits UTF-8 output. |  | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-CLI-Boundaries.md | boundaries-conformance | The implementation passes the authoritative bounded conformance examples relevant to malformed and unclosed input. | AssertionError | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-Verification-Scoped.md | scoped-section | A selected CommonMark specification section executes successfully against the completed executable. |  | 2026-08-15T18:27:04+00:00 |
| ✓ PASS | FEATURE-Verification-Scoped.md | scoped-example | A single explicitly selected CommonMark example executes successfully against the completed executable. |  | 2026-08-15T18:27:04+00:00 |
| ✗ FAIL | FEATURE-Verification-Full.md | full-conformance-suite | The complete unfiltered supplied CommonMark conformance suite succeeds through the required POSIX wrapper. | AssertionError | 2026-08-15T18:27:04+00:00 |
