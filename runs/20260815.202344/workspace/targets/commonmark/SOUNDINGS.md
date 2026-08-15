# Soundings

Per-assertion acceptance board, one row per Blueprint Programmatic Acceptance check.
`drydock plan` projects every assertion as `— UNVERIFIED`; `drydock score ac` sets the
Status column from deterministic proof results. A rerun of `drydock plan` resets Status to
`— UNVERIFIED`; rescore to refresh.

| Status | Blueprint | AC Id | Text | Evidence | Verified At |
|---|---|---|---|---|---|
| ✓ PASS | ARCHITECTURE.md | interface-executable | The application root contains an executable named commonmark. |  | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | ARCHITECTURE.md | interface-process | The executable accepts standard input and terminates successfully. |  | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | ARCHITECTURE.md | interface-utf8 | The executable accepts UTF-8 input and terminates successfully. |  | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Block-Leafs.md | block-leafs-conformance | The implementation passes every supplied conformance example owned by leaf-block parsing. |  | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Block-Leafs.md | block-leafs-interface | Leaf parsing remains reachable through the required executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Block-Leafs.md | block-leafs-reference-input | Link-reference-definition input is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Block-Quotes.md | block-quotes-conformance | The implementation passes every supplied conformance example owned by block quotes. |  | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Block-Quotes.md | block-quotes-interface | A block quote document is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Block-Quotes.md | block-quotes-nested-input | Nested block quote input is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Block-Lists.md | lists-conformance | The implementation passes every supplied conformance example owned by list items and lists. |  | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Block-Lists.md | lists-interface | A bullet list is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Block-Lists.md | lists-nested-input | Nested and ordered list input is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Inline-Basics.md | inline-basics-conformance | The implementation passes every supplied conformance example owned by foundational inline parsing. |  | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Inline-Basics.md | inline-basics-interface | Inline source containing escapes, entities, code, and line breaks is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ~ PREPASSED | FEATURE-Inline-Basics.md | inline-basics-unicode-input | UTF-8 inline text is accepted through the executable interface. | green at this block's baseline too, before its code existed — confirm the criterion exercises the story's work | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Inline-Emphasis.md | emphasis-conformance | The implementation passes every supplied conformance example owned by emphasis and strong emphasis. |  | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Inline-Links-Images.md | links-images-conformance | The implementation passes every supplied conformance example owned by links and images. |  | 2026-08-15T21:44:26+00:00 |
| ✓ PASS | FEATURE-Inline-HTML-Autolinks.md | html-autolinks-conformance | The implementation passes every supplied conformance example owned by autolinks and raw HTML. |  | 2026-08-15T21:44:26+00:00 |
| ✗ FAIL | FEATURE-Conformance-Verification.md | complete-conformance | The completed parser passes the complete unfiltered supplied CommonMark conformance suite. | malformed check: the assertion itself raised NameError (name 'sys' is not defined. Did you forget to import 'sys'?) in its own frame, before reaching the code under test. No implementation can satisfy it. Each check runs as its own script in its own process, so a name bound by another check is not in scope. Repair the assertion in the Blueprint specification. | 2026-08-15T21:44:26+00:00 |
