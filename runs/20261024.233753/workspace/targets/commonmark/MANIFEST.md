# MANIFEST: commonmark
updated: 2026-10-24T23:42:04+00:00
state: draft
blocks:      2

## story 1: Establish the Python project structure and stage the supplied conformance assets.
id:           architecture
summary:      Establish the Python project structure and stage the supplied conformance assets.
type:         foundational
kind:         capability
phase:        1
block:        1
implements:   ARCHITECTURE.md
copy:         blueprint/sources/spec.txt -> sources/spec.txt
instructions: |
  Establish the Python project structure for the root commonmark executable and stage the five runtime conformance assets verbatim under sources/. Keep the parser implementation original; do not use a public Markdown implementation.
stack:        common.md, python.md
stack_mode:   builder
size:         3870
acceptance:   yes
state:        pending

## story 2: Parse thematic breaks and ATX headings.
id: blocks_001
summary: Parse thematic breaks and ATX headings.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-ThematicBreaksAndATXHeadings.md
covers: BLOCKS-001
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56614
provides: thematic breaks, ATX headings
instructions: Implement thematic breaks and ATX headings according to CommonMark 0.31.2. Run the complete scoped example slice for these sections.
acceptance: yes
depends: architecture
state: pending

## story 3: Render hard breaks, soft breaks, and textual content.
id: inline_007
summary: Render hard breaks, soft breaks, and textual content.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-LineBreaksAndText.md
covers: INLINE-007
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56424
provides: hard line breaks, soft line breaks, textual content
instructions: Implement inline text rendering, soft line breaks, and hard line breaks. Run the complete scoped example slice for all three sections.
acceptance: yes
depends: architecture
state: pending

## story 4: Parse emphasis and strong emphasis.
id: inline_003
summary: Parse emphasis and strong emphasis.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Emphasis.md
covers: INLINE-003
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56430
provides: emphasis and strong emphasis
instructions: Implement the CommonMark delimiter-run algorithm for emphasis and strong emphasis, including nesting and ambiguity rules. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture
state: pending

## story 5: Parse autolinks and raw HTML.
id: inline_006
summary: Parse autolinks and raw HTML.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-AutolinksAndRawHTML.md
covers: INLINE-006
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56459
provides: URI and email autolinks, inline raw HTML
instructions: Implement URI and email autolinks and raw inline HTML tags, comments, declarations, processing instructions, and CDATA. Run the complete scoped example slice for both sections.
acceptance: yes
depends: architecture
state: pending

## story 6: Parse HTML blocks.
id: blocks_004
summary: Parse HTML blocks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-HTMLBlocks.md
covers: BLOCKS-004
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56554
provides: HTML blocks
instructions: Implement the seven CommonMark HTML block types and their start and end conditions. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture
state: pending

## story 7: Parse code spans.
id: inline_002
summary: Parse code spans.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-CodeSpans.md
covers: INLINE-002
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56561
provides: code spans
instructions: Implement code span delimiter matching and content normalization. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture
state: pending

## story 8: Parse setext headings.
id: blocks_002
summary: Parse setext headings.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-SetextHeadings.md
covers: BLOCKS-002
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56570
provides: setext headings
instructions: Implement setext headings according to CommonMark 0.31.2. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture
state: pending

## story 9: Parse block quotes.
id: blocks_006
summary: Parse block quotes.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-BlockQuotes.md
covers: BLOCKS-006
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56588
provides: block quotes
instructions: Implement block quote parsing, including lazy continuation and nested content. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture
state: pending

## story 10: Parse indented and fenced code blocks.
id: blocks_003
summary: Parse indented and fenced code blocks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-CodeBlocks.md
covers: BLOCKS-003
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56634
provides: indented code blocks, fenced code blocks
instructions: Implement indented and fenced code blocks according to CommonMark 0.31.2. Run the complete scoped example slice for both sections.
acceptance: yes
depends: architecture
state: pending

## story 11: Parse list items, list structure, and tightness.
id: blocks_007
summary: Parse list items, list structure, and tightness.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Lists.md
covers: BLOCKS-007
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56666
provides: list items, lists and tightness
instructions: Implement bullet and ordered list items, nesting, continuation, and tightness according to CommonMark 0.31.2. Run the complete scoped example slice for both sections.
acceptance: yes
depends: architecture
state: pending

## story 12: Parse backslash escapes and character references.
id: inline_001
summary: Parse backslash escapes and character references.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-EscapesAndCharacterReferences.md
covers: INLINE-001
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56675
provides: backslash escapes, entity and numeric character references
instructions: Implement inline backslash escapes and valid HTML entity and numeric character references. Run the complete scoped example slice for both sections.
acceptance: yes
depends: architecture
state: pending

## story 13: Collect link reference definitions and parse paragraphs.
id: blocks_005
summary: Collect link reference definitions and parse paragraphs.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-ReferenceDefinitionsAndParagraphs.md
covers: BLOCKS-005
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56737
provides: link reference definitions, paragraphs
instructions: Implement paragraph formation and document-wide link reference definition collection, including definitions inside containers and first-definition precedence. Run the complete scoped example slice for both sections.
acceptance: yes
depends: architecture
state: pending

## story 14: Parse images.
id: inline_005
summary: Parse images.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Images.md
covers: INLINE-005
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56448
provides: inline and reference images
consumes: link reference definitions
instructions: Implement inline and reference-style images, including plain-text alt attributes. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture, blocks_005
state: pending

## story 15: Parse inline links and reference links.
id: inline_004
summary: Parse inline links and reference links.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Links.md
covers: INLINE-004
context: spec.txt, spec_tests.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 56472
provides: inline links, reference links
consumes: link reference definitions
instructions: Implement inline, full, collapsed, and shortcut links, including destination, title, label normalization, and integration with collected reference definitions. Run the complete scoped example slice for this section.
acceptance: yes
depends: architecture, blocks_005
state: pending

## story 16: Provide the commonmark executable and describe its standard input and output interface.
id: conformance_001
summary: Provide the commonmark executable and describe its standard input and output interface.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-ExecutableInterface.md
covers: CONFORMANCE-001
context: INSTRUCTIONS.md, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 4283
provides: ./commonmark command
instructions: Provide an executable named commonmark at the application root. It reads UTF-8 Markdown from standard input and writes rendered HTML to standard output. Add the concise project README describing this interface.
acceptance: yes
depends: architecture
state: pending

## story 17: Verify the completed parser against the full supplied conformance suite.
id: conformance_002
summary: Verify the completed parser against the full supplied conformance suite.
type: service
kind: test harness
phase: 1
block: 2
implements: FEATURE-FullConformanceVerification.md
covers: CONFORMANCE-002
accepts: st-001
context: full_test.sh, spec_tests.py, cmark.py, normalize.py, spec.txt, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 58985
instructions: Run sh sources/full_test.sh from the completed application root as the sole unfiltered conformance verification. Preserve the supplied harness and assets unchanged.
acceptance: yes
depends: architecture, blocks_001, blocks_002, blocks_003, blocks_004, blocks_005, blocks_006, blocks_007, inline_001, inline_002, inline_003, inline_004, inline_005, inline_006, inline_007, conformance_001
state: pending
