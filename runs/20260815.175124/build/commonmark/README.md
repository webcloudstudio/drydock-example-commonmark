# CommonMark parser

Run the parser with Python. It reads UTF-8 Markdown from standard input and writes
HTML to standard output:

```sh
python3 commonmark.py < input.md > output.html
```

Parsing is organized as input normalization, block parsing and reference collection,
inline parsing, and HTML rendering. The `commonmark` module exposes `parse`, `render`,
and `main` for programmatic and executable use.
