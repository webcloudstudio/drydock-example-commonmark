# Blueprint Analysis: CommonMark

## Commander Expectations

- assert the parser implements CommonMark 0.31.2 and reads Markdown from standard input, writing HTML to standard output
- assert the supplied complete conformance suite passes
- assert the deliverable is an executable named `commonmark` at the application root

## Crew

| Crew | Charge |
|---|---|
| Commander | Defines intent and decides what done means. |
| Team Lead | Confirms epic completeness and stakeholder expectations. |
| Planning Crew | Authors atomic specifications and the ordered Manifest. |
| Shipyard Crew | Builds the tickets without synchronous Commander access. |

## Story List

### Feature: Command-Line Interface

| ID | Story | High-level AC |
|---|---|---|
| CLI-001 | Deliver the standard-input parser executable | The root-level `commonmark` executable reads UTF-8 Markdown from stdin and writes rendered HTML to stdout. Include the concise interface README. |

### Feature: Block Parsing

| ID | Story | High-level AC |
|---|---|---|
| BLOCK-001 | Parse thematic breaks and ATX headings | Thematic breaks and ATX headings follow their CommonMark rules. |
| BLOCK-002 | Parse setext headings and paragraphs | Setext headings and paragraphs preserve the specified boundaries and inline source text. |
| BLOCK-003 | Parse indented and fenced code blocks | Code blocks preserve literal content and apply the specified indentation, fence, and info-string rules. |
| BLOCK-004 | Parse HTML blocks | The seven HTML block types follow their start and end conditions and preserve raw content. |
| BLOCK-005 | Parse link reference definitions | Definitions are collected across the document, with the first matching definition taking precedence. |
| BLOCK-006 | Parse block quotes | Block quotes support markers, laziness, blank lines, and nested content as specified. |
| BLOCK-007 | Parse list items and lists | Lists support item boundaries, nesting, continuation, tightness, and ordered-list attributes as specified. |

### Feature: Inline Parsing

| ID | Story | High-level AC |
|---|---|---|
| INLINE-001 | Parse escapes and character references | Escapes and valid entity and numeric references render according to their contexts. |
| INLINE-002 | Parse code spans and line breaks | Code spans normalize content as specified; hard and soft line breaks follow their respective rules. |
| INLINE-003 | Parse emphasis and strong emphasis | Delimiter runs follow CommonMark flanking, matching, nesting, and precedence rules. |
| INLINE-004 | Parse links and images | Inline, reference, and image forms resolve destinations, titles, labels, and nesting as specified. |
| INLINE-005 | Parse autolinks and raw HTML | URI and email autolinks are rendered as links; valid raw HTML tags remain unescaped. |
| INLINE-006 | Render remaining textual content | Uninterpreted characters render as text, with internal spaces preserved. |

### Feature: Conformance Verification

| ID | Story | High-level AC |
|---|---|---|
| VERIFY-001 | Pass the complete supplied conformance suite | After all parser stories are complete, the supplied unfiltered suite exits successfully. This is the only full-suite acceptance check. |

## Story Guidance

Named stories planning must produce. Authoritative record: `STORY_GUIDANCE.json`.

| Story ID | Provenance | Gate | Note |
|---|---|---|---|
| CLI-001 | plan | — | Build Instructions: executable and standard-input/standard-output interface |
| BLOCK-001 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Thematic breaks|ATX headings` | Thematic breaks; ATX headings |
| BLOCK-002 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Setext headings|Paragraphs|Blank lines` | Setext headings; paragraphs; blank lines |
| BLOCK-003 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Indented code blocks|Fenced code blocks` | Indented and fenced code blocks |
| BLOCK-004 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern HTML blocks` | HTML blocks |
| BLOCK-005 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Link reference definitions` | Link reference definitions |
| BLOCK-006 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Block quotes` | Block quotes |
| BLOCK-007 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern List items|Lists` | List items and lists |
| INLINE-001 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Backslash escapes|Entity and numeric character references` | Escapes and character references |
| INLINE-002 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Code spans|Hard line breaks|Soft line breaks` | Code spans and line breaks |
| INLINE-003 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Emphasis and strong emphasis` | Emphasis and strong emphasis |
| INLINE-004 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Links|Images` | Links and images |
| INLINE-005 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Autolinks|Raw HTML` | Autolinks and raw HTML |
| INLINE-006 | plan | `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern Textual content` | Textual content |
| VERIFY-001 | plan | — | Terminal verification: complete unfiltered supplied suite; depends on all parser implementation stories |

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
| `sources/INSTRUCTIONS.md` | instruction-to-test | `sources/full_test.sh`, `sources/spec_tests.py` | Requires one terminal complete-suite story and scoped implementation checks. | Keep focused story checks separate from the single final full-suite gate. |
| `sources/spec.txt` | test-kit-to-implementation | Block parsing stories | Spec chapters define block behavior and contain conformance examples. | Implement block structure before inline parsing. |
| `sources/spec.txt` | test-kit-to-implementation | Inline parsing stories | Inline chapters define inline behavior and contain conformance examples. | Parse inline content after block structure and reference collection. |
| `sources/full_test.sh` | dependency | `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, `sources/spec.txt` | Harness invokes the test runner; the runner imports sibling modules and reads the spec. | Stage the harness, runner, helper modules, and spec so the final gate can run. |
| `sources/INSTRUCTIONS.md` | dependency | `CLI-001` | Requires a root executable named `commonmark` and a concise README. | Deliver the executable interface and README with the CLI story. |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| `sources/INSTRUCTIONS.md` | author intent | prompt-only | none |
| `sources/cmark.py` | reference implementation | context | stage |
| `sources/full_test.sh` | conformance harness | context | stage |
| `sources/normalize.py` | test helper | context | stage |
| `sources/spec.txt` | normative specification and conformance test suite | context | stage |
| `sources/spec_tests.py` | conformance harness | context | stage |

## Planning Instructions

### Delivery Shape

Build a command-line CommonMark 0.31.2 parser. It accepts Markdown on standard input and emits HTML on standard output. Parse block structure first, collecting link reference definitions, then parse inline content using those definitions. The root-level executable is exercised by the supplied conformance harness.

### Story Realization Map

| Story ID | Durable Blueprint scope | Evidence | Related files | Requires |
|---|---|---|---|---|
| CLI-001 | Executable interface and concise README | `sources/INSTRUCTIONS.md` | `sources/full_test.sh` | Capability |
| BLOCK-001 | Thematic breaks; ATX headings | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| BLOCK-002 | Setext headings; paragraphs; blank lines | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| BLOCK-003 | Indented code blocks; fenced code blocks | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| BLOCK-004 | HTML blocks | `sources/spec.txt` heading | `sources/spec_tests.py` | Capability |
| BLOCK-005 | Link reference definitions | `sources/spec.txt` heading | `sources/spec_tests.py` | Capability |
| BLOCK-006 | Block quotes | `sources/spec.txt` heading | `sources/spec_tests.py` | Capability |
| BLOCK-007 | List items; lists | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| INLINE-001 | Backslash escapes; entity and numeric references | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| INLINE-002 | Code spans; hard and soft line breaks | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| INLINE-003 | Emphasis and strong emphasis | `sources/spec.txt` heading | `sources/spec_tests.py` | Capability |
| INLINE-004 | Links; images | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| INLINE-005 | Autolinks; raw HTML | `sources/spec.txt` headings | `sources/spec_tests.py` | Capability |
| INLINE-006 | Textual content | `sources/spec.txt` heading | `sources/spec_tests.py` | Capability |
| VERIFY-001 | Complete supplied suite | `sources/INSTRUCTIONS.md` | `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, `sources/spec.txt` | Test harness and acceptance contract |

### Test and Acceptance Strategy

Implementation stories use `spec_tests.py` with selectors for the example-owning headings within each story’s scope. Do not run the full harness from scoped checks. VERIFY-001 depends on every implementation story and is the only story with `Suite: full`; it runs `sh sources/full_test.sh`, prints captured stdout and stderr, and asserts only `result.returncode == 0`. Sea Trial `st-001` records the same complete-suite requirement.

### Sequencing and Dependencies

Implement the CLI entry point, then block parsing in source order, followed by inline parsing. Reference definitions collected during block parsing are needed by inline links and images. Stage all supplied scoring assets unchanged. The terminal verification story follows every parser implementation story.

### Source Conflicts and Gaps

No unresolved source conflicts or blockers. Unattended UAT policy prohibits questionnaires and open questions; identity is derived as CommonMark and described as a command-line CommonMark 0.31.2 parser.

## Analysis Notes
generated: 2026-10-26
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.013501/workspace/targets/commonmark/blueprint

Quality: Ready
  blockers: 0
  questions: 0
  features: 4
  stories: 15
  stack: Python
  display_name: CommonMark
  short_description: A command-line CommonMark 0.31.2 parser that reads Markdown from standard input and writes HTML to standard output.

None.
