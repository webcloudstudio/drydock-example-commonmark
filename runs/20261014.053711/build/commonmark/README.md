# commonmark

A CommonMark 0.31.2 parser executable that converts Markdown on standard input to HTML on standard output.

## Intent

This product is a CommonMark 0.31.2 parser delivered as a single executable, `commonmark`, at the application root. It reads UTF-8 Markdown from standard input and writes HTML to standard output. It is built from the supplied specification text, following the Appendix parsing strategy (block structure first, then inline parsing with the delimiter-stack algorithms). Success means the complete supplied conformance suite passes when run unfiltered through `sh sources/full_test.sh`.

## What It Does

Implement the ATX headings section of the spec as a registered block start rule whose content is parsed as inlines.

Implement the Autolinks section of the spec.

Implement the Backslash escapes section of the spec.

Implement the per-line procedure from the spec Appendix, "Phase 1: block structure", and render paragraphs. Later block stories add start, continue and close rules to the registry without changing the loop.

Implement the Block quotes section of the spec as a registered container block.

Implement the Code spans and Inlines sections of the spec, and the inline scanner loop that later inline stories extend.

Implement the Emphasis and strong emphasis section of the spec using the Appendix algorithm directly.

Implement the Entity and numeric character references section of the spec.

Deliver the executable `commonmark` at the application root. It takes no arguments.

Implement the Fenced code blocks section of the spec.

Implement the HTML blocks section of the spec.

Implement the Images section of the spec on top of the shared link machinery, and gate the Emphasis, Links and Images corpus sections, which are all satisfiable once images exist.

Implement the Indented code blocks section of the spec as a registered block start rule.

Implement the Hard line breaks, Soft line breaks and Textual content sections of the spec.

Implement the Link reference definitions section of the spec and the label matching shared with links and images.

Implement the Links section of the spec following the Appendix "look for link or image" procedure. The `![` machinery is shared with images; image rendering belongs to the images story.

Implement the List items section of the spec as a registered container block. Grouping items into lists and tight or loose rendering belong to the lists story.

Implement the Lists section of the spec, and gate the block-structure sections whose examples need lists.

Implement the Raw HTML section of the spec.

Implement the Setext headings section of the spec.

Implement the Tabs section of the spec, audit every block rule's column handling, and gate the corpus sections whose examples needed all block and inline stories.

Implement the Thematic breaks section of the spec as a registered block start rule.

This is the terminal story. Once every parser story has closed, it proves the whole product by running the supplied scoring entry point `sources/full_test.sh`, which runs the complete, unfiltered CommonMark 0.31.2 suite against `./commonmark`.

## Setup and Running

**Before first run:**

- Copy `.env.example` to `.env` and fill in local values before starting.
- Confirm the repository has the expected remote with `git remote -v`; add `origin` if the startup guard requires it.
- Run `git status --short` and commit or intentionally stash local changes before deployment-oriented runs.

**Install dependencies:**

```bash
uv sync
```

## Verification

```bash
bash bin/test.sh
```

## Next Steps

- Complete the first-run checks above.
- Run `bash bin/test.sh` before making release or deployment changes.
