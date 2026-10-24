"""Process I/O boundary for the `commonmark` executable.

Responsibility: read raw bytes from `sys.stdin.buffer`, decode UTF-8 with U+FFFD replacement,
normalize line endings, replace U+0000, and write HTML to `sys.stdout.buffer`. Diagnostics go to
`sys.stderr` only, and the exit status is 0 for every input.
"""

import re
import sys

from mdparser import blocks, inlines, render

REPLACEMENT_CHARACTER = "�"
LINE_ENDING_PATTERN = re.compile(r"\r\n|\r|\n")


def decode_source(data: bytes) -> str:
    """Decode raw input bytes as UTF-8, replacing each invalid byte with U+FFFD."""
    return data.decode("utf-8", errors="replace")


def split_lines(text: str) -> list[str]:
    """Split text on LF, CR, or CRLF, and replace each U+0000 with U+FFFD."""
    text = text.replace("\x00", REPLACEMENT_CHARACTER)
    return LINE_ENDING_PATTERN.split(text)


def render_lines(lines: list[str]) -> str:
    """Parse the lines into a block tree and return the HTML document.

    A final line ending terminates the last line rather than starting an empty one, so the one empty
    entry that `split_lines` leaves after it is dropped. Otherwise an unclosed fenced code block would
    gain a blank line.
    """
    if lines and lines[-1] == "":
        lines = lines[:-1]
    root = blocks.parse_lines(lines)
    return render.render_document(root, lambda raw: inlines.parse_inline(raw, root.references))


def main() -> int:
    """Run the executable: stdin Markdown to stdout HTML. Always returns 0."""
    data = sys.stdin.buffer.read()
    try:
        lines = split_lines(decode_source(data))
        html = render_lines(lines)
    except Exception as exc:
        print(f"commonmark: internal error: {exc!r}", file=sys.stderr)
        html = ""
    sys.stdout.buffer.write(html.encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
