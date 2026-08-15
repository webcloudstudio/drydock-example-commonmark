# Blueprint Analysis: CommonMark

## Commander Expectations

- assert the parser reads Markdown from standard input and writes CommonMark-conformant HTML to standard output.

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Parser Interface

| ID | Story | High-level AC |
|---|---|---|
| INTERFACE-001 | Provide the executable standard-input/standard-output interface | An executable `commonmark` accepts UTF-8 Markdown on standard input and writes HTML to standard output. |

### Feature: Block Parsing

| ID | Story | High-level AC |
|---|---|---|
| BLOCK-001 | Parse leaf blocks | The parser handles thematic breaks, ATX and setext headings, indented and fenced code blocks, HTML blocks, paragraphs, and link reference definitions. |
| BLOCK-002 | Parse block quotes | The parser handles block quote markers, nesting, blank lines, lazy continuation, and contained blocks. |
| BLOCK-003 | Parse lists | The parser handles bullet and ordered lists, nesting, continuation, laziness, empty items, tightness, and block content. |

### Feature: Inline Parsing

| ID | Story | High-level AC |
|---|---|---|
| INLINE-001 | Parse escapes, entities, code spans, and line breaks | The parser correctly renders backslash escapes, HTML entities, numeric references, code spans, hard breaks, soft breaks, and literal text. |
| INLINE-002 | Parse emphasis and strong emphasis | The parser applies the CommonMark delimiter-run algorithm, including nesting, intraword rules, delimiter precedence, and unmatched delimiters. |
| INLINE-003 | Parse links and images | The parser handles inline, full, collapsed, and shortcut references, destinations, titles, nested brackets, images, and link restrictions. |
| INLINE-004 | Parse autolinks and raw HTML | The parser handles URI and email autolinks, raw HTML tags, comments, declarations, processing instructions, and CDATA. |

### Feature: Conformance Verification

| ID | Story | High-level AC |
|---|---|---|
| VERIFY-001 | Run the complete conformance suite | `sh sources/full_test.sh` runs unfiltered and exits successfully only when every supplied case passes with zero failures and errors. |

## Surfaced Acceptance Criteria

None.

## Source Inventory

| Path | Content kind | Disposition | Reason |
|---|---|---|---|
| `sources/INSTRUCTIONS.md` | markdown | analyzed | readable UTF-8 |
| `sources/cmark.py` | code | analyzed | readable UTF-8 |
| `sources/full_test.sh` | code | analyzed | readable UTF-8 |
| `sources/normalize.py` | code | analyzed | readable UTF-8 |
| `sources/spec.txt` | text | chunked | split into 18 bounded chunks |
| `sources/spec_tests.py` | code | analyzed | readable UTF-8 |

## Relationship Model

| Source or group | Relationship type | Related source or group | Evidence | Delivery implication |
|---|---|---|---|---|
| `sources/spec.txt` | normative specification and conformance test suite | `sources/spec_tests.py` | The test runner extracts examples and expected HTML from the specification. | Stories must follow the specification sections and use section-scoped checks. |
| `sources/spec_tests.py` | test-kit-to-implementation | `commonmark` | `spec_tests.py` invokes the supplied program through `cmark.py`. | The executable interface must remain stable. |
| `sources/cmark.py` | test helper | `commonmark` | `CMark(prog=...)` pipes UTF-8 input to the program and captures output. | Stage the helper and preserve standard streams. |
| `sources/normalize.py` | test helper | `sources/spec_tests.py` | The runner normalizes HTML before comparison. | Stage the normalizer with the harness. |
| `sources/full_test.sh` | instruction-to-test | `sources/spec_tests.py` | The supplied script invokes the unfiltered suite and checks the clean tally. | The terminal verification story is the only full-suite story. |
| `sources/INSTRUCTIONS.md` | author intent | all implementation stories | It defines implementation order, prohibitions, interface, and acceptance structure. | Use as planning context; do not stage it. |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| `sources/INSTRUCTIONS.md` | author intent | compass | prompt-only |
| `sources/spec.txt` | normative specification and conformance test suite | context | stage |
| `sources/spec_tests.py` | conformance harness | context | stage |
| `sources/cmark.py` | test helper | context | stage |
| `sources/normalize.py` | test helper | context | stage |
| `sources/full_test.sh` | conformance harness | context | stage |

## Planning Instructions

### Delivery Shape

The system is a command-line Markdown parser. It accepts UTF-8 Markdown through standard input, constructs block structure, parses inline content, and emits HTML through standard output. Delivery proceeds from the executable interface to block parsing, then inline parsing, followed by scoped specification checks and one terminal unfiltered conformance run.

### Story Realization Map

| Story ID | Blueprint scope | Evidence | Related files | Delivery type |
|---|---|---|---|---|
| INTERFACE-001 | Executable process boundary and UTF-8 streams | `sources/INSTRUCTIONS.md`, `sources/cmark.py` | `sources/cmark.py` | capability |
| BLOCK-001 | Leaf blocks and reference definitions | `sources/spec.txt` sections `Leaf blocks`, `Paragraphs`, `Link reference definitions` | `sources/spec_tests.py`, `sources/normalize.py` | capability and scoped harness |
| BLOCK-002 | Block quotes | `sources/spec.txt` section `Block quotes` | `sources/spec_tests.py` | capability and scoped harness |
| BLOCK-003 | Lists and tightness | `sources/spec.txt` sections `List items`, `Lists` | `sources/spec_tests.py` | capability and scoped harness |
| INLINE-001 | Escapes, entities, code spans, hard and soft breaks, textual content | `sources/spec.txt` sections `Backslash escapes`, `Entity and numeric character references`, `Code spans`, `Hard line breaks`, `Soft line breaks` | `sources/spec_tests.py` | capability and scoped harness |
| INLINE-002 | Emphasis and strong emphasis | `sources/spec.txt` section `Emphasis and strong emphasis` | `sources/spec_tests.py` | capability and scoped harness |
| INLINE-003 | Links and images | `sources/spec.txt` sections `Links`, `Images` | `sources/spec_tests.py` | capability and scoped harness |
| INLINE-004 | Autolinks and raw HTML | `sources/spec.txt` sections `Autolinks`, `Raw HTML` | `sources/spec_tests.py` | capability and scoped harness |
| VERIFY-001 | Complete supplied suite execution | `sources/full_test.sh` | all staged runtime assets and `commonmark` | acceptance contract |

### Test and Acceptance Strategy

Implementation stories use `spec_tests.py` with explicit section selectors covering only their owned sections and declare `Suite: scoped`. The terminal verification story depends on every implementation story, declares `Suite: full`, and runs `sh sources/full_test.sh`. The supplied harness and its imported helpers are staged unchanged.

### Sequencing and Dependencies

Build the executable interface first. Implement block parsing before inline parsing, with reference definitions available before inline rendering. Stage `spec.txt`, `spec_tests.py`, `cmark.py`, `normalize.py`, and `full_test.sh` before verification. Run scoped checks after each relevant parser capability; run the complete suite only in `VERIFY-001`.

### Source Conflicts and Gaps

No conflicting product definitions were found. The sources do not specify a framework, persistence layer, deployment platform, authentication model, or interactive UI; these are not required for the described local CLI. The source does prohibit use of a public Markdown implementation and modification of supplied conformance assets.

## Analysis Notes
generated: 2026-08-15
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.202344/workspace/targets/commonmark/blueprint

Quality: Questions
  blockers: 0
  questions: 1
  features: 4
  stories: 9
  stack: Python 3 and POSIX shell
  display_name: CommonMark
  short_description: A command-line CommonMark 0.31.2 parser that converts Markdown from standard input to HTML on standard output.

The identity questionnaire remains open because the project display name and short description were blank. No other human-owned planning decisions are required.
