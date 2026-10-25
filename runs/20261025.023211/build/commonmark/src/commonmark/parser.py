"""Public parse flow joining block parsing, inline parsing, and rendering."""

from .block_parser import parse_blocks
from .inline_parser import parse_inlines
from .renderer import render_html


def parse(markdown: str) -> str:
    """Convert a Markdown document to HTML."""
    document = parse_blocks(markdown)
    document = parse_inlines(document)
    return render_html(document)
