# CommonMark

`commonmark` converts Markdown from standard input to HTML on standard output.

Run it from the project root:

```sh
./commonmark < input.md
```

The executable reads the complete document as UTF-8 and writes the rendered HTML to standard output. Operational errors are reported on standard error with a nonzero exit status.
