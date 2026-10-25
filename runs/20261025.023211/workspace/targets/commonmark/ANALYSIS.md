# Blueprint Analysis: CommonMark

## Commander Expectations

- assert the parser reads Markdown from standard input and writes HTML to standard output
- assert the parser conforms to CommonMark 0.31.2
- assert the supplied scoring assets remain unchanged

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
| BLOCK-001 | Parse thematic breaks and headings | Parse thematic breaks, ATX headings, and setext headings according to the specification. |
| BLOCK-002 | Parse code blocks and HTML blocks | Parse indented and fenced code blocks, and all specified HTML block types. |
| BLOCK-003 | Parse paragraphs and link reference definitions | Parse paragraphs and collect valid link reference definitions for document-wide resolution. |
| BLOCK-004 | Parse block quotes | Parse nested block quotes, including lazy paragraph continuation. |
| BLOCK-005 | Parse lists | Parse bullet and ordered lists, nesting, continuation, empty items, and tight or loose rendering. |

### Feature: Inline Parsing and HTML Rendering

| ID | Story | High-level AC |
|---|---|---|
| INLINE-001 | Parse inline text and breaks | Render escaped text, backslash escapes, entities, numeric references, and soft and hard line breaks. |
| INLINE-002 | Parse code spans and emphasis | Parse code spans and nested emphasis and strong emphasis using CommonMark delimiter rules. |
| INLINE-003 | Parse links, images, and autolinks | Parse inline and reference links, images, URI and email autolinks, and resolve destinations and titles. |
| INLINE-004 | Parse raw HTML and render inline elements | Preserve valid raw HTML and render parsed inline elements as HTML. |

### Feature: Executable Interface and Conformance

| ID | Story | High-level AC |
|---|---|---|
| CONFORMANCE-001 | Provide the `commonmark` executable | Provide an executable at the application root that reads UTF-8 Markdown from stdin and writes HTML to stdout. |
| CONFORMANCE-002 | Pass the complete CommonMark conformance suite | Run the unfiltered supplied suite and pass every supplied case. |

## Story Guidance

Named stories planning must produce. Authoritative record: `STORY_GUIDANCE.json`.

None.

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
| `sources/INSTRUCTIONS.md` | instruction-to-test | `sources/full_test.sh` | Defines the executable interface and requires the supplied full suite as the scoring entry point. | Implement the root executable; reserve unfiltered suite execution for terminal verification. |
| `sources/full_test.sh` | test-kit-to-implementation | `sources/spec_tests.py` | Harness invokes the runner with `--program` and `--spec`. | Stage and run the harness with its runner and specification. |
| `sources/spec_tests.py` | test-kit-to-implementation | `sources/cmark.py`, `sources/normalize.py`, `sources/spec.txt` | Runner imports `cmark` and `normalize`, and reads spec examples. | Stage all imported runtime assets alongside the specification. |
| `sources/cmark.py` | reference-to-replacement | `commonmark` executable | The adapter invokes the supplied program and captures its HTML output. | Build a compatible executable; do not treat the adapter as the parser implementation. |
| `sources/spec.txt` | parser-to-normalizer | `sources/normalize.py` | Specification examples define expected HTML; runner normalizes actual and expected HTML before comparison. | Match normalized conformance output while preserving significant content and attributes. |

## Source Roles

| Path | Role | Plan disposition | Build disposition |
|---|---|---|---|
| `sources/INSTRUCTIONS.md` | author intent | prompt-only | none |
| `sources/cmark.py` | test helper | stage | stage |
| `sources/full_test.sh` | conformance harness | stage | stage |
| `sources/normalize.py` | test helper | stage | stage |
| `sources/spec.txt` | normative specification and conformance test suite | stage | stage |
| `sources/spec_tests.py` | conformance harness | stage | stage |

## Planning Instructions

### Delivery Shape

Build a command-line Markdown parser that consumes UTF-8 text on standard input and emits HTML on standard output. Parse block structure first, collecting document-wide link reference definitions; then parse inline content using those definitions and render the resulting document. The supplied suite exercises the executable through the staged harness.

### Story Realization Map

| Story ID | Blueprint scope(s) | Evidence | Related files | Requires |
|---|---|---|---|---|
| BLOCK-001 | Thematic breaks; ATX headings; setext headings | `sources/spec.txt` sections “Thematic breaks,” “ATX headings,” and “Setext headings” | `sources/spec.txt` | capability |
| BLOCK-002 | Indented code blocks; fenced code blocks; HTML blocks | `sources/spec.txt` sections “Indented code blocks,” “Fenced code blocks,” and “HTML blocks” | `sources/spec.txt` | capability |
| BLOCK-003 | Paragraphs; link reference definitions; blank lines | `sources/spec.txt` sections “Link reference definitions,” “Paragraphs,” and “Blank lines” | `sources/spec.txt` | capability |
| BLOCK-004 | Block quotes and lazy continuation | `sources/spec.txt` section “Block quotes” | `sources/spec.txt` | capability |
| BLOCK-005 | List items, lists, nesting, continuation, and tightness | `sources/spec.txt` sections “List items” and “Lists” | `sources/spec.txt` | capability |
| INLINE-001 | Backslash escapes; entities and numeric references; hard and soft breaks; text | `sources/spec.txt` sections “Backslash escapes,” “Entity and numeric character references,” “Hard line breaks,” “Soft line breaks,” and “Textual content” | `sources/spec.txt` | capability |
| INLINE-002 | Code spans; emphasis and strong emphasis | `sources/spec.txt` sections “Code spans” and “Emphasis and strong emphasis” | `sources/spec.txt` | capability |
| INLINE-003 | Links; images; autolinks | `sources/spec.txt` sections “Links,” “Images,” and “Autolinks” | `sources/spec.txt` | capability |
| INLINE-004 | Raw HTML and HTML output behavior | `sources/spec.txt` sections “Raw HTML” and “HTML blocks” | `sources/spec.txt` | capability |
| CONFORMANCE-001 | Root executable and stdin/stdout contract | `sources/INSTRUCTIONS.md`; `sources/full_test.sh` interface check | `sources/full_test.sh` | capability |
| CONFORMANCE-002 | Complete supplied suite verification | `sources/INSTRUCTIONS.md`; `sources/full_test.sh` | `sources/full_test.sh`, `sources/spec_tests.py`, `sources/cmark.py`, `sources/normalize.py`, `sources/spec.txt` | acceptance contract |

### Test and Acceptance Strategy

Parser implementation stories use bounded spec section selectors covering their complete scope; chapter headings that own no examples are not valid scopes. Do not run the full harness from scoped checks. The single terminal verification story depends on every parser implementation story, runs `sh sources/full_test.sh`, prints captured stdout and stderr, asserts only that the return code is zero, and carries Sea Trial `st-001`. Its acceptance declares `Suite: full`.

### Sequencing and Dependencies

Implement block parsing before inline parsing so the parser can identify block content and collect reference definitions before resolving inline links. The executable interface must be available for scoped checks. Stage the supplied full harness, test runner, adapter, normalizer, and specification together. The terminal conformance verification follows all parser implementation stories.

### Source Conflicts and Gaps

No unresolved source conflicts or planning questions. The sources identify the parser behavior, interface, implementation prohibition, and conformance gate. Language and framework are not specified; the stack proposal records the conventional Python choice.

## Analysis Notes
generated: 2026-10-24
blueprint: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/workspace/targets/commonmark/blueprint

Quality: Ready
  blockers: 0
  questions: 0
  features: 3
  stories: 11
  stack: Python
  display_name: CommonMark
  short_description: A command-line parser that converts Markdown from standard input to HTML on standard output.

Identity is proposed from the imported intent; the Commander can confirm or edit it.
