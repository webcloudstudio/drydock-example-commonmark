# Blueprint Analysis: CommonMark

## Commander Expectations

- assert the parser reads CommonMark from standard input, writes HTML to standard output, and passes the complete supplied conformance suite.

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Command-Line Parser

| ID | Story | High-level AC |
|---|---|---|
| CLI-001 | Implement standard-input and standard-output entry point | The executable reads UTF-8 Markdown from stdin and writes rendered HTML to stdout. |
| CLI-002 | Implement parser error and process behavior | Invalid operational conditions produce deterministic diagnostics and nonzero exit behavior without corrupting stdout. |
| CLI-003 | Document parser operation | README.md documents the stdin/stdout interface and `sh full_test.sh`. |

### Feature: Block Structure

| ID | Story | High-level AC |
|---|---|---|
| BLOCK-001 | Parse leaf blocks | The parser handles thematic breaks, ATX and setext headings, indented code, fenced code, HTML blocks, paragraphs, and link reference definitions. |
| BLOCK-002 | Parse block quotes | The parser handles block quote markers, nesting, blank lines, lazy continuation, and contained block structure. |
| BLOCK-003 | Parse list items and list structure | The parser handles bullet and ordered lists, nesting, lazy continuation, empty items, indentation, delimiter changes, and tight versus loose rendering. |

### Feature: Inline Parsing

| ID | Story | High-level AC |
|---|---|---|
| INLINE-001 | Parse escapes and character references | The parser handles punctuation escapes, entity references, numeric references, replacement characters, and context restrictions. |
| INLINE-002 | Parse code spans and line breaks | The parser handles code span delimiter lengths, normalization, hard breaks, and soft breaks. |
| INLINE-003 | Parse emphasis and strong emphasis | The parser applies delimiter-run rules, nesting, intraword restrictions, and precedence. |
| INLINE-004 | Parse links and images | The parser handles inline, full, collapsed, and shortcut references plus nested image descriptions and destination/title rules. |
| INLINE-005 | Parse autolinks and raw HTML | The parser handles URI/email autolinks, HTML tags, comments, declarations, processing instructions, and CDATA. |

### Feature: HTML Rendering

| ID | Story | High-level AC |
|---|---|---|
| RENDER-001 | Render block structure as HTML | Parsed blocks render with the required CommonMark HTML elements, nesting, escaping, and list paragraph rules. |
| RENDER-002 | Render inline structure as HTML | Inline nodes render with required escaping, links, images, code, emphasis, breaks, and raw HTML preservation. |
| RENDER-003 | Normalize URL, title, and attribute output | Rendered URLs, titles, attributes, and special characters match the supplied harness expectations. |

### Feature: Conformance Verification

| ID | Story | High-level AC |
|---|---|---|
| VERIFY-001 | Stage the supplied conformance assets | `spec.txt`, `spec_tests.py`, `cmark.py`, and `normalize.py` are available at their required runtime paths. |
| VERIFY-002 | Add bounded story verification | Parser stories run only their selected conformance sections or examples and report failures deterministically. |
| VERIFY-003 | Run the complete conformance suite | The terminal verification story runs `sh full_test.sh`, declares `Suite: full`, and passes the Sea Trial when the command exits zero. |

## Surfaced Acceptance Criteria

| ID | Story ID | Criterion |
|---|---|---|
| AC-001 | CLI-001 | The parser consumes Markdown from standard input and emits HTML to standard output. |
| AC-002 | VERIFY-001 | Runtime conformance assets include the supplied harness and every module it imports. |
| AC-003 | VERIFY-003 | The complete unfiltered supplied suite is executed as the final verification gate. |
| AC-004 | CLI-003 | README.md remains concise and documents the required invocation. |

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
| `sources/INSTRUCTIONS.md` | instruction-to-test | `sources/spec_tests.py` | Defines full-suite policy, scoped selectors, staging, and README requirements. | Planning must preserve bounded story checks and one terminal full-suite story. |
| `sources/spec.txt` | normative specification and conformance test suite | `sources/spec_tests.py` | The harness parses examples from `spec.txt`. | Stage the specification and use section selectors for focused verification. |
| `sources/spec_tests.py` | test-kit-to-implementation | parser executable | `CMark` invokes the deliverable and compares normalized HTML. | The executable must support stdin/stdout operation and deterministic exit codes. |
| `sources/spec_tests.py` | test-kit-to-helper | `sources/cmark.py`, `sources/normalize.py` | The harness imports both modules. | Stage both helper modules with the harness. |
| `sources/cmark.py` | implementation-to-helper | parser executable | Provides subprocess invocation of the tested program. | Conformance verification must invoke the real deliverable entry point. |
| `sources/normalize.py` | parser-to-normalizer | rendered HTML | Normalizes insignificant HTML differences before comparison. | Rendering must preserve all significant HTML semantics. |

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

The system is a command-line CommonMark 0.31.2 parser. It accepts Markdown on stdin, performs block parsing followed by inline parsing, renders HTML on stdout, and is verified by the supplied Python conformance harness and shell wrapper.

### Story Realization Map

| Story ID | Durable Blueprint scope | Evidence | Related files | Delivery kind |
|---|---|---|---|---|
| CLI-001 | Executable interface | `sources/INSTRUCTIONS.md` | `sources/spec_tests.py`, `sources/cmark.py` | capability |
| CLI-002 | Process and failure behavior | `sources/INSTRUCTIONS.md` | `sources/spec_tests.py` | capability and acceptance |
| CLI-003 | Operator documentation | `sources/INSTRUCTIONS.md` | README.md | documentation |
| BLOCK-001 | Leaf block parser | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| BLOCK-002 | Block quote parser | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| BLOCK-003 | List parser | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| INLINE-001 | Escapes and references | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| INLINE-002 | Code spans and breaks | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| INLINE-003 | Emphasis algorithm | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| INLINE-004 | Links and images | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| INLINE-005 | Autolinks and HTML | `sources/spec.txt` | `sources/spec_tests.py` | capability |
| RENDER-001 | Block HTML renderer | `sources/spec.txt` | `sources/normalize.py` | capability |
| RENDER-002 | Inline HTML renderer | `sources/spec.txt` | `sources/normalize.py` | capability |
| RENDER-003 | Output normalization compatibility | `sources/spec.txt`, `sources/normalize.py` | `sources/spec_tests.py` | integration |
| VERIFY-001 | Runtime conformance assets | `sources/INSTRUCTIONS.md`, `sources/spec_tests.py` | all staged source assets | integration |
| VERIFY-002 | Scoped story checks | `sources/INSTRUCTIONS.md`, `sources/spec_tests.py` | selected harness invocations | test harness |
| VERIFY-003 | Full-suite terminal gate | `sources/INSTRUCTIONS.md`, `SEA_TRIALS.md` | `full_test.sh` | acceptance contract |

### Test and Acceptance Strategy

Block and inline stories use focused selectors matching example-bearing headings in `spec.txt`. Rendering stories use bounded harness runs covering their owned syntax. No story other than VERIFY-003 runs the complete suite. VERIFY-003 is the sole terminal verification story, depends on every implementation story, declares `Suite: full`, and proves Sea Trial `st-001` through the exit status of `sh full_test.sh`.

### Sequencing and Dependencies

The executable interface precedes harness integration. Block parsing precedes inline parsing; list parsing depends on the shared block model. Rendering depends on both parser phases. The conformance assets are staged before focused verification. The full-suite story follows all parser and rendering stories and creates or invokes `full_test.sh`.

### Source Conflicts and Gaps

No conflicting product definitions were found. The implementation language and deployment packaging are not specified; the proposed stack records conventional choices without blocking planning. Authentication, persistence, external services, and UI workflows are not applicable to the described CLI parser.

## Analysis Notes
generated: 2026-08-12
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/workspace/targets/commonmark/blueprint

Quality: Questions
  blockers: 0
  questions: 1
  features: 5
  stories: 16
  stack: Python 3 and POSIX shell; no application framework
  display_name: CommonMark
  short_description: A command-line CommonMark 0.31.2 parser that converts standard-input Markdown to HTML on standard output.

None.
