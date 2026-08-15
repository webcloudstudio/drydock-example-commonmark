# commonmark

A command-line CommonMark 0.31.2 parser that converts Markdown from standard input to HTML on standard output.

## Intent

Build a command-line CommonMark 0.31.2 parser for users and automated tooling that need Markdown converted to conformant HTML. The program is the executable `commonmark` at the application root: it reads UTF-8 Markdown from standard input and writes HTML to standard output.

## What It Does

Implement the leaf-block portion of CommonMark block parsing before inline rendering.

Implement bullet and ordered list containers and their list-item block content.

Implement block quote containers and their interaction with leaf blocks.

Provide the terminal verification step for the completed command-line parser.

Implement the foundational inline constructs used by all later inline features.

Implement emphasis and strong emphasis after block parsing and basic inline tokenization.

Implement inline autolinks and raw HTML while preserving their precedence over ordinary text and emphasis.

Implement inline and reference links and images using the document-wide link reference map produced during block parsing.

## Next Steps

- Complete the first-run checks above.
