# MANIFEST: commonmark
updated:     2026-08-15T17:57:39+00:00
state:       approved
blocks:      16
planning_feedback: |
  analyze-display_name applied ARCHITECTURE.md
  analyze-short_description applied ARCHITECTURE.md

applied: ARCHITECTURE.md=29d6ad935e062c936916e0c045e2a4e90c396205,ARCHITECTURE_compact.md=29d6ad935e062c936916e0c045e2a4e90c396205,FEATURE-Block-Input.md=29d6ad935e062c936916e0c045e2a4e90c396205,FEATURE-Block-Leaves.md=29d6ad935e062c936916e0c045e2a4e90c396205,cmark.py=29d6ad935e062c936916e0c045e2a4e90c396205,common.md=29d6ad935e062c936916e0c045e2a4e90c396205,normalize.py=29d6ad935e062c936916e0c045e2a4e90c396205,python.md=29d6ad935e062c936916e0c045e2a4e90c396205,spec.txt=29d6ad935e062c936916e0c045e2a4e90c396205,spec_tests.py=29d6ad935e062c936916e0c045e2a4e90c396205
applied_specs: |
  ARCHITECTURE.md sha256=5d12940336e991dd110f9831318fafa3500a2d785e5f30e8862b5a73491ce13d commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-1 applied_at=2026-08-15T18:01:48+00:00 build_sha256=11266c9085f1b5d5354acc544b98db8128368c0460f9d4b2d01163329da6f0b3
  ARCHITECTURE_compact.md sha256=1e11cf40802c5e36c2ef87469bfdb3d4e945b40347bc77a391847cc9c2795ee0 commit=- applied_by=block-3 applied_at=2026-08-15T18:19:28+00:00 build_sha256=1e11cf40802c5e36c2ef87469bfdb3d4e945b40347bc77a391847cc9c2795ee0
  FEATURE-Block-Input.md sha256=a510fc465fb8884bd9784e628a5d3281ec4ac85077630727fea79fe44cb0235e commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-2 applied_at=2026-08-15T18:06:47+00:00 build_sha256=09dfdbb1a046903baa86e1233c5257eb5ecd28f5b80c61de71dbcbdd8f7837c9
  FEATURE-Block-Leaves.md sha256=7e8746bc993f37d30e5ece8f022f7921d90604034878bd8dcdc96d6fb9867e29 commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-3 applied_at=2026-08-15T18:19:28+00:00 build_sha256=a9558bab84a04e6aa84214d5da4fff88ec558e7ec479606347dd238043a2da9f
  cmark.py sha256=c5fb45e7c64fd7670b2a3c49a151e46f4af9d0ad3004bedb37ecf9cdc34d2f00 commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-3 applied_at=2026-08-15T18:19:28+00:00 build_sha256=c5fb45e7c64fd7670b2a3c49a151e46f4af9d0ad3004bedb37ecf9cdc34d2f00
  normalize.py sha256=94a9dd253907e3dab7c02fc11e934f06112dcf0f3804255d09d732c8c7c4b5f4 commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-3 applied_at=2026-08-15T18:19:28+00:00 build_sha256=94a9dd253907e3dab7c02fc11e934f06112dcf0f3804255d09d732c8c7c4b5f4
  spec.txt sha256=43fad3e0ac5190a3b0bc6a41f7b1a853201a26ec2e6b74871f5d96239a8c34cf commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-3 applied_at=2026-08-15T18:19:28+00:00 build_sha256=43fad3e0ac5190a3b0bc6a41f7b1a853201a26ec2e6b74871f5d96239a8c34cf
  spec_tests.py sha256=9db1ea4a3ee79c5ec74eebc09c5985eb252427e8d9d19ef45e5cc3f2ae410855 commit=50b04b88e2c8e2ad616db754e416a93b971298b2 applied_by=block-3 applied_at=2026-08-15T18:19:28+00:00 build_sha256=9db1ea4a3ee79c5ec74eebc09c5985eb252427e8d9d19ef45e5cc3f2ae410855

## story 1: Define the standalone CommonMark parser architecture and module boundaries.
id:           architecture
evidence: evidence/block-1.md
summary:      Define the standalone CommonMark parser architecture and module boundaries.
type:         foundational
kind:         capability
phase:        1
block:        1
implements:   ARCHITECTURE.md
scope:        target
instructions: |
  Define the standalone Python architecture for a two-phase CommonMark 0.31.2 parser.
  Establish module ownership for input normalization, block parsing, reference collection,
  inline parsing, HTML rendering, and the stdin/stdout executable. Do not use a public
  Markdown implementation.
  Build the implementation incrementally behind the declared boundaries so later stories
  can extend the parser without changing the executable contract.
stack:        common.md, python.md
stack_mode:   builder
size:         7407
provides:     parser architecture, block parser boundary, inline parser boundary, renderer boundary
acceptance:   yes
state: closed/verified

## story 2: Normalize Markdown input lines, whitespace, tabs, and insecure characters.
id: block-input
evidence: evidence/block-2.md
summary: Normalize Markdown input lines, whitespace, tabs, and insecure characters.
type: service
kind: capability
phase: 1
block: 2
implements: FEATURE-Block-Input.md
covers: BLOCK-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59117
budget: over-target
provides: normalized UTF-8 input lines
consumes: parser architecture
instructions: |
  Implement UTF-8 stdin preprocessing and the CommonMark line model. Handle LF, CRLF,
  and CR line endings, blank lines, tab-stop indentation, arbitrary Unicode, and replacement
  of U+0000 with U+FFFD. Preserve internal tabs where the specification requires literal tabs.
  Run bounded conformance checks using the Tabs section of spec.txt. Do not invoke full_test.sh.
acceptance: yes
depends: architecture
state: closed/verified
scope: target

## story 3: Parse CommonMark leaf blocks and render their structural content.
id: block-leaves
evidence: evidence/block-3.md
summary: Parse CommonMark leaf blocks and render their structural content.
type: service
kind: capability
phase: 1
block: 3
implements: FEATURE-Block-Leaves.md
covers: BLOCK-002
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59163
budget: over-target
provides: thematic breaks, ATX headings, setext headings, paragraphs, indented code blocks, fenced code blocks, HTML blocks
consumes: normalized UTF-8 input lines, parser architecture
instructions: |
  Implement leaf-block recognition and block nodes for thematic breaks, ATX headings,
  setext headings, paragraphs, indented code, fenced code, and HTML blocks. Preserve
  literal code and raw HTML content for the renderer. Run bounded conformance checks for
  the owned sections: Thematic breaks, ATX headings, Setext headings, Indented code blocks,
  Fenced code blocks, and HTML blocks. Do not invoke full_test.sh.
acceptance: yes
depends: block-input
state: closed/verified
scope: target

## story 4: Collect and resolve document-wide link reference definitions.
id: block-references
finding: programmatic acceptance failed: block-references-container: TypeError: expected str, bytes or os.PathLike object, not int
evidence: evidence/block-4.md
summary: Collect and resolve document-wide link reference definitions.
type: service
kind: capability
phase: 1
block: 4
implements: FEATURE-Block-References.md
covers: BLOCK-003
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59052
budget: over-target
provides: document-wide link reference definition map
consumes: leaf blocks, normalized UTF-8 input lines
instructions: |
  Detect valid link reference definitions while closing block content, normalize labels
  using Unicode case folding and whitespace rules, preserve first-definition precedence,
  and leave invalid definitions as paragraph content. Support definitions inside containers
  and multiline destinations or titles. Run bounded conformance checks for Link reference
  definitions. Do not invoke full_test.sh.
acceptance: yes
depends: block-leaves
state: closed/failed
scope: target

## story 5: Parse block quotes with laziness, nesting, blank lines, and contained blocks.
id: block-quotes
summary: Parse block quotes with laziness, nesting, blank lines, and contained blocks.
type: service
kind: capability
phase: 1
block: 5
implements: FEATURE-Block-Quotes.md
covers: BLOCK-004
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 58994
budget: over-target
provides: block quote nodes
consumes: leaf blocks, document-wide link reference definition map
instructions: |
  Implement block quote markers, optional delimiter spacing, nesting, lazy paragraph
  continuation, empty quotes, blank-line separation, and contained leaf blocks. Run bounded
  conformance checks for Block quotes. Do not invoke full_test.sh.
acceptance: yes
depends: block-references
state: pending
scope: target

## story 6: Parse nested bullet and ordered lists with tightness and lazy continuation.
id: block-lists
summary: Parse nested bullet and ordered lists with tightness and lazy continuation.
type: service
kind: capability
phase: 1
block: 6
implements: FEATURE-Block-Lists.md
covers: BLOCK-005
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59034
budget: over-target
provides: list nodes, list item nodes, tight and loose list state
consumes: block quote nodes, leaf blocks, document-wide link reference definition map
instructions: |
  Implement bullet and ordered list markers, marker indentation, nested lists, continuation
  blocks, lazy lines, empty items, list interruption, delimiter changes, ordered starts,
  and tight/loose rendering state. Run bounded conformance checks for List items and Lists.
  Do not invoke full_test.sh.
acceptance: yes
depends: block-quotes, block-references
state: pending
scope: target

## story 7: Parse backslash escapes and entity or numeric character references.
id: inline-escapes
summary: Parse backslash escapes and entity or numeric character references.
type: service
kind: capability
phase: 2
block: 7
implements: FEATURE-Inline-Escapes.md
covers: INLINE-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59062
budget: over-target
provides: escaped punctuation, named entity references, numeric character references
consumes: block tree, document-wide link reference definition map
instructions: |
  Implement ASCII punctuation escapes, literal backslashes before non-punctuation,
  HTML5 named entities, decimal and hexadecimal numeric references, invalid-reference
  handling, and U+0000 replacement in inline references. Run bounded conformance checks
  for Backslash escapes and Entity and numeric character references. Do not invoke full_test.sh.
acceptance: yes
depends: block-lists
state: pending
scope: target

## story 8: Parse code spans, hard line breaks, and soft line breaks.
id: inline-code-breaks
summary: Parse code spans, hard line breaks, and soft line breaks.
type: service
kind: capability
phase: 2
block: 8
implements: FEATURE-Inline-Code-Breaks.md
covers: INLINE-002
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59052
budget: over-target
provides: code spans, hard line breaks, soft line breaks
consumes: escaped inline content, block tree
instructions: |
  Implement equal-length backtick delimiters, code-span line-ending normalization and
  space trimming, backslash and trailing-space hard breaks, and soft-break rendering.
  Ensure code spans do not process escapes or references. Run bounded conformance checks
  for Code spans, Hard line breaks, and Soft line breaks. Do not invoke full_test.sh.
acceptance: yes
depends: inline-escapes
state: pending
scope: target

## story 9: Parse emphasis and strong emphasis using delimiter-run rules.
id: inline-emphasis
summary: Parse emphasis and strong emphasis using delimiter-run rules.
type: service
kind: capability
phase: 2
block: 9
implements: FEATURE-Inline-Emphasis.md
covers: INLINE-003
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59036
budget: over-target
provides: emphasis and strong-emphasis inline nodes
consumes: code spans, escaped inline content, block tree
instructions: |
  Implement the CommonMark delimiter stack algorithm for asterisks and underscores,
  including flanking rules, intraword restrictions, rule-of-three behavior, nesting,
  precedence, and unmatched delimiter handling. Run bounded conformance checks for
  Emphasis and strong emphasis. Do not invoke full_test.sh.
acceptance: yes
depends: inline-code-breaks
state: pending
scope: target

## story 10: Parse inline, reference, collapsed, shortcut links, and images.
id: inline-links
summary: Parse inline, reference, collapsed, shortcut links, and images.
type: service
kind: capability
phase: 2
block: 10
implements: FEATURE-Inline-Links.md
covers: INLINE-004
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59063
budget: over-target
provides: links and images with destinations, titles, references, and alt text
consumes: emphasis inline nodes, code spans, document-wide link reference definition map
instructions: |
  Implement bracket grouping, inline destinations and titles, balanced parentheses,
  full/collapsed/shortcut references, nested images, link non-nesting, URL escaping,
  title escaping, and plain-text image alt construction. Run bounded conformance checks
  for Links and Images. Do not invoke full_test.sh.
acceptance: yes
depends: inline-emphasis, block-references
state: pending
scope: target

## story 11: Parse URI and email autolinks and preserve valid raw HTML.
id: inline-html-autolinks
summary: Parse URI and email autolinks and preserve valid raw HTML.
type: service
kind: capability
phase: 2
block: 11
implements: FEATURE-Inline-HTML-Autolinks.md
covers: INLINE-005
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59101
budget: over-target
provides: URI autolinks, email autolinks, inline raw HTML
consumes: links and images, emphasis inline nodes, code spans
instructions: |
  Implement absolute URI and email autolinks, valid HTML tags, comments, processing
  instructions, declarations, CDATA, attributes, and precedence against code spans,
  links, and emphasis. Run bounded conformance checks for Autolinks and Raw HTML.
  Do not invoke full_test.sh.
acceptance: yes
depends: inline-links
state: pending
scope: target

## story 12: Render the complete parsed document as CommonMark-compatible HTML.
id: html-renderer
summary: Render the complete parsed document as CommonMark-compatible HTML.
type: service
kind: integration
phase: 3
block: 12
implements: FEATURE-HTML-Renderer.md
covers: CLI-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59115
budget: over-target
provides: HTML renderer
consumes: block nodes, inline nodes, list tightness, raw HTML nodes
instructions: |
  Implement HTML rendering for every supported block and inline node, including escaping,
  attributes, URLs, titles, code blocks, raw HTML, list tightness, and standard CommonMark
  tag formatting. Run bounded conformance checks covering the complete rendered surface
  owned by the implementation stories without invoking full_test.sh.
acceptance: yes
depends: inline-html-autolinks
state: pending
scope: target

## story 13: Provide the UTF-8 standard-input/standard-output parser executable.
id: cli-executable
summary: Provide the UTF-8 standard-input/standard-output parser executable.
type: service
kind: integration
phase: 3
block: 13
implements: FEATURE-CLI-Executable.md
covers: CLI-002
context: cmark.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 4312
provides: commonmark stdin/stdout executable
consumes: HTML renderer
instructions: |
  Create the executable entry point that reads UTF-8 Markdown from standard input and
  writes HTML to standard output, with no public Markdown runtime dependency. Preserve
  the adapter-compatible process contract used by cmark.py, including UTF-8 output and
  nonzero failure behavior for unrecoverable process errors.
acceptance: yes
depends: html-renderer
state: pending
scope: target

## story 14: Handle malformed, empty, unclosed, and arbitrary Unicode input safely.
id: cli-boundaries
summary: Handle malformed, empty, unclosed, and arbitrary Unicode input safely.
type: service
kind: capability
phase: 3
block: 14
implements: FEATURE-CLI-Boundaries.md
covers: CLI-003
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59153
budget: over-target
provides: safe malformed-input handling
consumes: commonmark stdin/stdout executable
instructions: |
  Harden the parser and executable against empty documents, unclosed fences and inline
  constructs, invalid syntax, malformed Unicode boundaries, U+0000, and large nesting
  or delimiter cases. Run bounded conformance checks for unclosed and invalid examples
  within the owned implementation sections. Do not invoke full_test.sh.
acceptance: yes
depends: cli-executable
state: pending
scope: target

## story 15: Stage conformance assets and provide bounded specification-section checks.
id: verification-scoped
summary: Stage conformance assets and provide bounded specification-section checks.
type: service
kind: test harness
phase: 3
block: 15
implements: FEATURE-Verification-Scoped.md
covers: VERIFY-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 59015
budget: over-target
provides: scoped conformance verification
consumes: commonmark stdin/stdout executable
instructions: |
  Stage spec.txt, spec_tests.py, cmark.py, and normalize.py into the build environment.
  Provide bounded checks that use explicit section or example selectors and never invoke
  full_test.sh. Verify that the staged runner can execute a selected conformance section
  against the completed executable.
acceptance: yes
depends: cli-executable
state: pending
scope: both

## story 16: Run the complete unfiltered CommonMark conformance suite.
id: verification-full
summary: Run the complete unfiltered CommonMark conformance suite.
type: service
kind: test harness
phase: 4
block: 16
implements: FEATURE-Verification-Full.md
covers: VERIFY-002
accepts: st-001
context: spec.txt, spec_tests.py, cmark.py, normalize.py, ARCHITECTURE_compact.md
stack: common.md, python.md
stack_mode: consumer
size: 58910
budget: over-target
provides: full_test.sh, terminal conformance proof
consumes: commonmark stdin/stdout executable, staged conformance assets
instructions: |
  Create full_test.sh as a POSIX-compatible wrapper around the complete unfiltered supplied
  suite. It must run sh full_test.sh from the target/build directory, print captured stdout
  and stderr for diagnosis, and use only the process exit code as the release verdict.
  This is the sole Suite: full check.
acceptance: yes
depends: architecture, block-input, block-leaves, block-references, block-quotes, block-lists, inline-escapes, inline-code-breaks, inline-emphasis, inline-links, inline-html-autolinks, html-renderer, cli-executable, cli-boundaries, verification-scoped
state: pending
scope: both
