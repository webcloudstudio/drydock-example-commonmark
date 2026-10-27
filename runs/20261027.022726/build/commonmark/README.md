# CommonMark command line

Run `./commonmark` from the application root. It reads UTF-8 Markdown from
standard input and writes the rendered HTML to standard output:

```sh
printf '# Hello\n' | ./commonmark
```
