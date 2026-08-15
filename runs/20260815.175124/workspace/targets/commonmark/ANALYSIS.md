# Blueprint Analysis: CommonMark

## Commander Expectations

- assert the parser reads Markdown from standard input, writes HTML to standard output, and passes every supplied CommonMark 0.31.2 conformance test.

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Block Parsing

| ID | Story | High-level AC |
|---|---|---|
| BLOCK-001 | Parse lines, whitespace, tabs, and insecure characters | Input lines and U+0000 handling follow the specification. |
| BLOCK-002 | Parse leaf blocks | Thematic breaks, headings, paragraphs, indented code, fenced code, and HTML blocks render correctly. |
| BLOCK-003 | Parse link reference definitions | Valid definitions are collected document-wide; invalid definitions remain content. |
| BLOCK-004 | Parse block quotes | Block quotes support markers, laziness, nesting, blank lines, and contained blocks. |
| BLOCK-005 | Parse lists and list items | Bullet and ordered lists support nesting, continuation, laziness, empty items, and tight/loose rendering. |

### Feature: Inline Parsing

| ID | Story | High-level AC |
|---|---|---|
| INLINE-001 | Parse escapes and character references | Escapes, named entities, and numeric references follow CommonMark context rules. |
| INLINE-002 | Parse code spans and line breaks | Code spans normalize content correctly; hard and soft breaks render correctly. |
| INLINE-003 | Parse emphasis and strong emphasis | Delimiter runs, nesting, intraword rules, and precedence follow the specification. |
| INLINE-004 | Parse links and images | Inline, reference, collapsed, shortcut, nested-image, destination, and title rules work. |
| INLINE-005 | Parse autolinks and raw HTML | URI/email autolinks and valid raw HTML are preserved or rendered as specified. |

### Feature: HTML Rendering and CLI

| ID | Story | High-level AC |
|---|---|---|
| CLI-001 | Render the parsed document as HTML | Parsed blocks and inlines produce the expected CommonMark HTML representation. |
| CLI-002 | Provide the standard-input/standard-output executable | The executable consumes UTF-8 Markdown from stdin and writes HTML to stdout without requiring a public Markdown implementation. |
| CLI-003 | Handle malformed and boundary input safely | Unclosed constructs, invalid syntax, empty input, and arbitrary Unicode do not crash the parser. |

### Feature: Conformance Verification

| ID | Story | High-level AC |
|---|---|---|
| VERIFY-001 | Stage and run scoped conformance checks | Implementation stories can run bounded `spec_tests.py` sections without invoking the full suite. |
| VERIFY-002 | Run the complete conformance suite | The terminal verification runs `sh full_test.sh` and succeeds only when the complete supplied suite returns exit code 0. |

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | CLI-002 | The executable shall read Markdown from standard input and write rendered HTML to standard output. |
| AC-002 | CLI-002 | The executable shall operate without using a public Markdown implementation. |
| AC-003 | VERIFY-001 | Scoped checks shall select explicit specification sections or examples and shall not invoke `full_test.sh`. |
| AC-004 | VERIFY-002 | The terminal verification shall capture and print standard output and standard error, then assert only that the full-suite return code is 0. |

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/INSTRUCTIONS.md` | markdown | analyzed | readable UTF-8 |
| `sources/cmark.py` | code | analyzed | readable UTF-8 |
| `sources/normalize.py` | code | analyzed | readable UTF-8 |
| `sources/spec.txt` | text | chunked | split into 18 bounded chunks |
| `sources/spec_tests.py` | code | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| `sources/spec.txt` | normative specification and conformance test suite | `sources/spec_tests.py` | The harness extracts examples and compares rendered HTML. | Stage both; implementation stories own bounded specification sections. |
| `sources/spec_tests.py` | test-kit-to-implementation | `sources/cmark.py` | The harness invokes `CMark(prog=...)` and checks process output. | Preserve the executable stdin/stdout contract. |
| `sources/spec_tests.py` | test-kit-to-implementation | `sources/normalize.py` | The harness normalizes HTML before comparison. | Stage the normalizer as a runtime harness dependency. |
| `sources/cmark.py` | conformance harness adapter | parser executable | `pipe_through_prog` sends UTF-8 input and captures output, errors, and return code. | Terminal verification must use the adapter-compatible executable. |
| `sources/INSTRUCTIONS.md` | instruction-to-test | all implementation and verification stories | It defines implementation order, staged assets, scoped checks, and the terminal full-suite story. | Use as planning context; do not stage it. |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| `sources/INSTRUCTIONS.md` | author intent | compass | prompt-only |
| `sources/spec.txt` | normative specification and conformance test suite | context | stage |
| `sources/spec_tests.py` | conformance harness | context | stage |
| `sources/cmark.py` | test helper | context | stage |
| `sources/normalize.py` | test helper | context | stage |

## Planning Instructions

### Delivery Shape

A command-line Markdown-to-HTML parser consumes UTF-8 Markdown on standard input and emits HTML on standard output. Delivery proceeds from block parsing to inline parsing, then rendering and executable integration, followed by bounded checks and one terminal unfiltered conformance run.

### Story Realization Map

| Story ID | Blueprint scope | Evidence | Related files | Delivery kind |
|---|---|---|---|---|
| BLOCK-001 | Input line model and character preprocessing | `sources/spec.txt`, Characters and lines; Insecure characters | parser source | capability |
| BLOCK-002 | Leaf-block parser | `sources/spec.txt`, Leaf blocks | parser source | capability |
| BLOCK-003 | Reference-definition collection | `sources/spec.txt`, Link reference definitions | parser source | capability |
| BLOCK-004 | Block-quote parser | `sources/spec.txt`, Block quotes | parser source | capability |
| BLOCK-005 | List parser and tightness | `sources/spec.txt`, List items; Lists | parser source | capability |
| INLINE-001 | Escapes and references | `sources/spec.txt`, Backslash escapes; Entity references | inline source | capability |
| INLINE-002 | Code spans and breaks | `sources/spec.txt`, Code spans; Hard/Soft line breaks | inline source | capability |
| INLINE-003 | Emphasis algorithm | `sources/spec.txt`, Emphasis and strong emphasis; Appendix algorithm | inline source | capability |
| INLINE-004 | Links and images | `sources/spec.txt`, Links; Images | inline source | capability |
| INLINE-005 | Autolinks and raw HTML | `sources/spec.txt`, Autolinks; Raw HTML | inline source | capability |
| CLI-001 | HTML renderer | `sources/spec.txt` examples | renderer source | capability |
| CLI-002 | Executable interface | `sources/INSTRUCTIONS.md`; `sources/cmark.py` | executable source | integration |
| CLI-003 | Boundary and invalid-input handling | `sources/spec.txt` invalid and unclosed examples | parser and executable | capability |
| VERIFY-001 | Scoped harness execution | `sources/INSTRUCTIONS.md`; `sources/spec_tests.py` | staged harness files | test harness |
| VERIFY-002 | Full-suite wrapper and terminal proof | `sources/INSTRUCTIONS.md`; `SEA_TRIALS.md` | `full_test.sh`, staged harness | acceptance contract |

### Test and Acceptance Strategy

Each parser story uses explicit `spec_tests.py --pattern` or `--number` selectors for its owned sections. Harness dependencies are staged before scoped verification. VERIFY-002 is the only terminal story using the unfiltered suite and carries Sea Trial `st-001`.

### Sequencing and Dependencies

Implement block structure before inline parsing; reference definitions must be available before inline resolution. Rendering and CLI integration follow parser capabilities. Stage `spec.txt`, `spec_tests.py`, `cmark.py`, and `normalize.py` before verification. VERIFY-001 follows the relevant implementation stories; VERIFY-002 depends on every implementation and integration story.

### Source Conflicts and Gaps

No cross-source conflicts were found. The sources define a CLI parser, its processing order, runtime harness, and complete acceptance command. Identity remains pending Commander confirmation.

## Analysis Notes
generated: 2026-08-15
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.175124/workspace/targets/commonmark/blueprint

Quality: Questions
  blockers: 0
  questions: 1
  features: 4
  stories: 15
  stack: Python 3, POSIX shell
  display_name: CommonMark
  short_description: A CommonMark 0.31.2 parser that converts Markdown from standard input into HTML on standard output.

None.
