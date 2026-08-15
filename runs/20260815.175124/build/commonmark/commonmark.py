"""Public facade and executable contract for the standalone CommonMark parser."""

import sys

from blocks import Document, parse_blocks
from normalization import normalize_input
from renderer import render_document


def parse(text: str) -> Document:
    """Normalize input and construct the block tree before inline parsing."""
    return parse_blocks(normalize_input(text).text)


def render(document: Document) -> str:
    """Render a parsed document to CommonMark HTML."""
    return render_document(document)


def main() -> int:
    """Read UTF-8 Markdown from stdin and write HTML to stdout."""
    sys.stdout.write(render(parse(sys.stdin.read())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
