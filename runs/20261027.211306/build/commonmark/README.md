# commonmark

A command-line parser that converts CommonMark Markdown from standard input to HTML on standard output.

## Intent

CommonMark is a command-line parser for users who need Markdown converted to HTML. It implements the supplied CommonMark 0.31.2 specification and reads UTF-8 Markdown from standard input, writing HTML to standard output through the root executable `commonmark`.

## What It Does

Parse fenced code as a literal block, including its optional info string, for subsequent HTML rendering.

Identify raw HTML blocks during block parsing and preserve their input without inline interpretation.

Identify indented code chunks during block parsing and retain their literal content for HTML rendering.

Extract definitions from closing paragraphs and make the resulting map available after block parsing, before inline parsing begins.

Recognize a setext underline following eligible paragraph content and retain the heading's raw text for the later inline phase.

## Setup and Running

**Before first run:**

- Confirm the repository has the expected remote with `git remote -v`; add `origin` if the startup guard requires it.
- Run `git status --short` and commit or intentionally stash local changes before deployment-oriented runs.

**Install dependencies:**

```bash
uv sync
```

## Verification

```bash
python -m pytest
```

## Next Steps

- Complete the first-run checks above.
- Run `python -m pytest` before making release or deployment changes.
