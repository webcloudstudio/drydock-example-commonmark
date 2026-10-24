# MANIFEST: commonmark
updated: 2026-10-24T23:20:08+00:00
state: draft
blocks:      4

## story 1: Provide the root commonmark executable for Markdown input and HTML output.
id:           cli-001
summary:      Provide the root commonmark executable for Markdown input and HTML output.
type:         service
kind:         capability
phase:        1
block:        1
implements:   FEATURE-CLI.md
covers:       CLI-001
instructions: |
  Provide an executable named commonmark at the application root. It reads Markdown from standard input and writes HTML to standard output. Do not use a public Markdown implementation. Keep the executable interface available for subsequent parser stories.
stack:        common.md, python.md
stack_mode:   builder
size:         3589
provides:     commonmark
acceptance:   yes
state:        pending

## story 2: Parse thematic breaks.
id: blk-001
summary: Parse thematic breaks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-THEMATIC-BREAKS.md
covers: BLK-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57680
instructions: Implement thematic break parsing and rendering. Run the supplied conformance examples scoped to the “Thematic breaks” section.
acceptance: yes
depends: cli-001
state: pending

## story 3: Parse ATX headings.
id: blk-002
summary: Parse ATX headings.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-ATX-HEADINGS.md
covers: BLK-002
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57687
instructions: Implement ATX heading parsing and rendering. Run the supplied conformance examples scoped to the “ATX headings” section.
acceptance: yes
depends: cli-001, blk-001
state: pending

## story 4: Parse setext headings.
id: blk-003
summary: Parse setext headings.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-SETEXT-HEADINGS.md
covers: BLK-003
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57720
instructions: Implement setext heading parsing and rendering. Run the supplied conformance examples scoped to the “Setext headings” section.
acceptance: yes
depends: cli-001, blk-001, blk-002
state: pending

## story 5: Parse indented code blocks.
id: blk-004
summary: Parse indented code blocks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-INDENTED-CODE.md
covers: BLK-004
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57732
instructions: Implement indented code block parsing and rendering. Run the supplied conformance examples scoped to the “Indented code blocks” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003
state: pending

## story 6: Parse fenced code blocks.
id: blk-005
summary: Parse fenced code blocks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-FENCED-CODE.md
covers: BLK-005
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57830
instructions: Implement fenced code block parsing and rendering. Run the supplied conformance examples scoped to the “Fenced code blocks” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004
state: pending

## story 7: Parse HTML blocks.
id: blk-006
summary: Parse HTML blocks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-HTML-BLOCKS.md
covers: BLK-006
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57731
instructions: Implement HTML block parsing and rendering. Run the supplied conformance examples scoped to the “HTML blocks” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005
state: pending

## story 8: Parse link reference definitions.
id: blk-007
summary: Parse link reference definitions.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-LINK-REFERENCE-DEFINITIONS.md
covers: BLK-007
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57826
provides: document link reference definitions
instructions: Collect link reference definitions during block parsing so later inline parsing can resolve references across the document, including definitions inside containers. Run the supplied conformance examples scoped to the “Link reference definitions” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006
state: pending

## story 9: Parse paragraphs.
id: blk-008
summary: Parse paragraphs.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-PARAGRAPHS.md
covers: BLK-008
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57717
instructions: Implement paragraph boundaries, continuation lines, and paragraph rendering. Run the supplied conformance examples scoped to the “Paragraphs” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007
state: pending

## story 10: Handle blank lines between blocks.
id: blk-009
summary: Handle blank lines between blocks.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-BLANK-LINES.md
covers: BLK-009
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57719
instructions: Handle blank lines at document boundaries and between blocks, including their effects on list tightness. Run the supplied conformance examples scoped to the “Blank lines” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008
state: pending

## story 11: Parse block quotes.
id: blk-010
summary: Parse block quotes.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-BLOCK-QUOTES.md
covers: BLK-010
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57876
instructions: Implement block quote containers, continuation, and laziness. Run the supplied conformance examples scoped to the “Block quotes” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009
state: pending

## story 12: Parse list items.
id: blk-011
summary: Parse list items.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-LIST-ITEMS.md
covers: BLK-011
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57906
instructions: Implement list item boundaries, continuation, nesting, indentation, and laziness. Run the supplied conformance examples scoped to the “List items” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010
state: pending

## story 13: Parse lists and list tightness.
id: blk-012
summary: Parse lists and list tightness.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-LISTS.md
covers: BLK-012
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57855
provides: bullet and ordered list rendering
instructions: Implement list grouping, list type and start number, and tight or loose rendering based on blank lines. Run the supplied conformance examples scoped to the “Lists” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011
state: pending

## story 14: Parse backslash escapes.
id: inl-001
summary: Parse backslash escapes.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-BACKSLASH-ESCAPES.md
covers: INL-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57827
instructions: Implement inline backslash escapes and hard breaks from a trailing backslash. Run the supplied conformance examples scoped to the “Backslash escapes” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012
state: pending

## story 15: Parse entity and numeric character references.
id: inl-002
summary: Parse entity and numeric character references.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-CHARACTER-REFERENCES.md
covers: INL-002
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57766
instructions: Implement valid HTML entity references and decimal and hexadecimal numeric references, replacing invalid Unicode code points as required. Run the supplied conformance examples scoped to the “Entity and numeric character references” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001
state: pending

## story 16: Parse code spans.
id: inl-003
summary: Parse code spans.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-CODE-SPANS.md
covers: INL-003
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57704
instructions: Implement inline code span matching, normalization, and rendering. Run the supplied conformance examples scoped to the “Code spans” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002
state: pending

## story 17: Parse emphasis and strong emphasis.
id: inl-004
summary: Parse emphasis and strong emphasis.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-EMPHASIS.md
covers: INL-004
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57985
instructions: Implement CommonMark delimiter-run processing for emphasis and strong emphasis, including nesting and delimiter precedence. Run the supplied conformance examples scoped to the “Emphasis and strong emphasis” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003
state: pending

## story 18: Parse links.
id: inl-005
summary: Parse links.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-LINKS.md
covers: INL-005
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57978
provides: inline and reference links
consumes: document link reference definitions
instructions: Implement inline, full, collapsed, and shortcut reference links using document-wide definitions collected during block parsing. Run the supplied conformance examples scoped to the “Links” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004
state: pending

## story 19: Parse images.
id: inl-006
summary: Parse images.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-IMAGES.md
covers: INL-006
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57889
provides: inline and reference images
consumes: document link reference definitions
instructions: Implement inline, full, collapsed, and shortcut reference images, including plain text alt attributes. Run the supplied conformance examples scoped to the “Images” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005
state: pending

## story 20: Parse autolinks.
id: inl-007
summary: Parse autolinks.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-AUTOLINKS.md
covers: INL-007
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57873
instructions: Implement URI and email autolinks. Run the supplied conformance examples scoped to the “Autolinks” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005, inl-006
state: pending

## story 21: Preserve raw HTML inline.
id: inl-008
summary: Preserve raw HTML inline.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-RAW-HTML.md
covers: INL-008
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57716
instructions: Implement raw HTML tags and inline raw HTML forms while preserving their literal markup. Run the supplied conformance examples scoped to the “Raw HTML” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005, inl-006, inl-007
state: pending

## story 22: Parse hard line breaks.
id: inl-009
summary: Parse hard line breaks.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-HARD-LINE-BREAKS.md
covers: INL-009
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57708
instructions: Implement hard line breaks from two or more trailing spaces or a backslash before a line ending, except at the end of a block and inside code spans or HTML tags. Run the supplied conformance examples scoped to the “Hard line breaks” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005, inl-006, inl-007, inl-008
state: pending

## story 23: Parse soft line breaks.
id: inl-010
summary: Parse soft line breaks.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-SOFT-LINE-BREAKS.md
covers: INL-010
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57671
instructions: Implement soft line breaks between inline content, preserving line boundaries as allowed by the specification. Run the supplied conformance examples scoped to the “Soft line breaks” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005, inl-006, inl-007, inl-008, inl-009
state: pending

## story 24: Preserve textual content.
id: inl-011
summary: Preserve textual content.
type: service
kind: capability
phase: 2
block: 3
implements: FEATURE-TEXTUAL-CONTENT.md
covers: INL-011
context: spec.txt, spec_tests.py, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 57642
instructions: Preserve all remaining textual content and escape it appropriately for HTML. Run the supplied conformance examples scoped to the “Textual content” section.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005, inl-006, inl-007, inl-008, inl-009, inl-010
state: pending

## story 25: Pass the complete CommonMark conformance suite.
id: con-001
summary: Pass the complete CommonMark conformance suite.
type: service
kind: test harness
phase: 3
block: 4
implements: VERIFICATION.md
covers: CON-001
accepts: st-001
context: full_test.sh, spec_tests.py, spec.txt, cmark.py, normalize.py
stack: common.md, python.md
stack_mode: consumer
size: 58181
instructions: Run the complete supplied conformance harness from the application root using `sh sources/full_test.sh`. Capture and print standard output and standard error, and assert only that the command exits with status zero. This is the sole full-suite check and implements Sea Trial st-001.
acceptance: yes
depends: cli-001, blk-001, blk-002, blk-003, blk-004, blk-005, blk-006, blk-007, blk-008, blk-009, blk-010, blk-011, blk-012, inl-001, inl-002, inl-003, inl-004, inl-005, inl-006, inl-007, inl-008, inl-009, inl-010, inl-011
state: pending
