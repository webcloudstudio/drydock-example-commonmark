# commonmark

A command-line CommonMark 0.31.2 parser that converts standard-input Markdown to HTML on standard output.

## Intent

CommonMark is a command-line Markdown parser for users and automation that converts CommonMark 0.31.2 input into HTML. The parser reads standard input, writes standard output, and is judged by the supplied complete conformance suite.

## What It Does

The inline parser recognizes inline, full-reference, collapsed-reference, and shortcut links and images. It resolves link reference definitions collected during block parsing, supports balanced destinations and titles, and prevents nested links while permitting nested image descriptions.

## Next Steps

- Complete the first-run checks above.
