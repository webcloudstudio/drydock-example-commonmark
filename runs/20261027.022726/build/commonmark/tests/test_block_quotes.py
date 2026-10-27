from commonmark_parser import parse_blocks, render_html
from commonmark_parser.block_quotes import parse_block_quote


def test_consecutive_marked_lines_extract_contents():
    lines = ["> alpha\n", "> beta\n", "\n"]
    assert parse_block_quote(lines) == (2, ["alpha\n", "beta\n"])


def test_lazy_paragraph_continuation_stops_at_blank():
    lines = ["> alpha\n", "beta\n", "\n", "outside\n"]
    assert parse_block_quote(lines) == (2, ["alpha\n", "beta\n"])


def test_nested_quotes_and_leaf_blocks_render_recursively():
    document = parse_blocks("> outer\n> > inner\n>\n> # title\n")
    assert render_html(document) == (
        "<blockquote>\n<p>outer</p>\n<blockquote>\n<p>inner</p>\n"
        "</blockquote>\n<h1>title</h1>\n</blockquote>\n"
    )


def test_quote_definition_is_added_to_document_map():
    document = parse_blocks("> [ref]: /target\n\ntext\n")
    assert document.references == {"ref": ("/target", None)}
