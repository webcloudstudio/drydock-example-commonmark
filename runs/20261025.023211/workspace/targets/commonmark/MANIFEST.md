# MANIFEST: commonmark
updated:     2026-10-25T02:33:27+00:00
state:       approved
blocks:      2

applied_specs: |
  ARCHITECTURE.md sha256=b6be7922c807305623c683775ec769166358dffdbb4519164fbc5233efaf62fc commit=f08221769f6c1a16aeb7206cf6ae8cc0a201725f applied_by=block-1 applied_at=2026-10-25T02:35:54+00:00 build_sha256=b6be7922c807305623c683775ec769166358dffdbb4519164fbc5233efaf62fc

## story 1: Establish the Python project tree, environment, and test runner.
id:           foundation
finding: ADVISORY: implemented, not verified — no governed acceptance command covers this story. Declare one in ACCEPTANCE.json to gate it.
evidence: evidence/block-1.md
summary:      Establish the Python project tree, environment, and test runner.
type:         foundational
kind:         capability
phase:        1
block:        1
implements:   ARCHITECTURE.md
instructions: |
  Establish the Python project structure and environment, and define the parser module boundaries
  and rendering flow described by the architecture. Keep the implementation self-contained and do
  not use a public Markdown implementation.
stack:        common.md, python.md
stack_mode:   builder
size:         3787
provides:     commonmark parser package structure
acceptance:   yes
state: closed/implemented

## story 2: Parse CommonMark block structure and collect link reference definitions.
id: block_parsing
finding: programmatic acceptance failed: block-parsing-conformance: AssertionError
evidence: evidence/block-2.md
summary: Parse CommonMark block structure and collect link reference definitions.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Block-Parsing.md
covers: BLOCK-001, BLOCK-002, BLOCK-003, BLOCK-004, BLOCK-005
context: spec_tests.py, cmark.py, normalize.py, spec.txt, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 58547
provides: block parser, document reference map
consumes: commonmark parser package structure
instructions: |
  Implement block parsing, link reference definition collection, and block rendering behavior for
  the assigned CommonMark specification sections. Include paragraphs, thematic breaks, headings,
  code blocks, HTML blocks, block quotes, and lists.
acceptance: yes
depends: foundation
state: closed/failed

## story 3: Parse CommonMark inline syntax and render inline HTML.
id: inline_parsing
finding: programmatic acceptance failed: inline-parsing-conformance: AssertionError
evidence: evidence/block-2.md
summary: Parse CommonMark inline syntax and render inline HTML.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Inline-Parsing.md
covers: INLINE-001, INLINE-002, INLINE-003, INLINE-004
context: spec_tests.py, cmark.py, normalize.py, spec.txt, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 58513
provides: inline parser, HTML renderer
consumes: block parser, document reference map
instructions: |
  Implement inline parsing and HTML rendering for the assigned CommonMark specification sections,
  using the complete link reference map produced by block parsing.
acceptance: yes
depends: foundation, block_parsing
state: closed/failed

## story 4: Provide the commonmark stdin/stdout executable.
id: executable
finding: step block-2 failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
evidence: evidence/block-2.md
summary: Provide the commonmark stdin/stdout executable.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Executable.md
covers: CONFORMANCE-001
context: ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 3342
provides: commonmark
consumes: block parser, inline parser
instructions: |
  Provide an executable named commonmark at the application root. It reads UTF-8 Markdown from
  standard input and writes HTML to standard output. Keep the supplied conformance assets unchanged.
acceptance: yes
depends: foundation, block_parsing, inline_parsing
state: closed/failed

## story 5: Verify the completed parser against the full CommonMark suite.
id: full_conformance
finding: programmatic acceptance failed: full-commonmark-suite: AssertionError
evidence: evidence/block-2.md
summary: Verify the completed parser against the full CommonMark suite.
type: service
kind: test harness
phase: 1
block: 2
implements: VERIFICATION.md
covers: CONFORMANCE-002
accepts: st-001
context: full_test.sh, spec_tests.py, cmark.py, normalize.py, spec.txt
stack: common.md, python.md
stack_mode: consumer
size: 58157
provides: full conformance verification
instructions: |
  Run the unfiltered supplied suite with sh sources/full_test.sh, print captured standard output
  and standard error, and require a zero exit status. This is the sole whole-suite check and carries
  Sea Trial st-001.
acceptance: yes
depends: foundation, block_parsing, inline_parsing, executable
state: closed/failed
