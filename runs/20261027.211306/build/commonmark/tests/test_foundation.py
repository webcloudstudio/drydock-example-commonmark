import commonmark_parser
from commonmark_parser.blocks import Document, parse_blocks
from commonmark_parser.inlines import parse_inlines


def test_render_is_callable():
    assert callable(commonmark_parser.render)


def test_block_parser_is_callable():
    assert callable(parse_blocks)


def test_inline_parser_is_callable():
    assert callable(parse_inlines)


def test_empty_block_input_returns_document_with_contract_fields():
    document = parse_blocks("")
    assert isinstance(document, Document)
    assert document.children == []
    assert document.references == {}


def test_render_accepts_complete_document():
    assert commonmark_parser.render("") == ""
