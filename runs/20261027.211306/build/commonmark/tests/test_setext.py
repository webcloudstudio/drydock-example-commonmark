from commonmark_parser.blocks import parse_blocks
from commonmark_parser.setext import parse_setext
from commonmark_parser import render


def test_parse_setext_level_one_and_multiline_raw_content():
    assert parse_setext(["alpha", "beta", "==="]) == (1, "alpha\nbeta")


def test_parse_setext_level_two():
    assert parse_setext(["alpha", "---"]) == (2, "alpha")


def test_parse_setext_rejects_empty_or_invalid_underline():
    assert parse_setext(["", "==="]) is None
    assert parse_setext(["alpha", "    ---"]) is None
    assert parse_setext(["alpha", "= ="]) is None


def test_block_parser_setext_takes_precedence_over_thematic_break():
    nodes = parse_blocks("alpha\n---\n").children
    assert [(node.kind, node.level, node.literal) for node in nodes] == [("heading", 2, "alpha")]


def test_block_parser_preserves_multiline_content_and_trims_outer_whitespace():
    nodes = parse_blocks("  alpha \n beta \t\n === \t\n").children
    assert [(node.kind, node.level, node.literal) for node in nodes] == [("heading", 1, "alpha \n beta")]


def test_underline_without_paragraph_remains_thematic_break():
    nodes = parse_blocks("---\n").children
    assert [node.kind for node in nodes] == ["thematic_break"]


def test_four_column_indented_underline_does_not_convert_paragraph():
    nodes = parse_blocks("alpha\n    ---\n").children
    assert [(node.kind, node.literal) for node in nodes] == [("paragraph", "alpha\n---")]


def test_multiline_setext_heading_resolves_emphasis_across_soft_break():
    assert render("Foo *bar\nbaz*\n====\n") == "<h1>Foo <em>bar\nbaz</em></h1>\n"


def test_multiline_setext_heading_keeps_unemphasized_neighbor():
    assert render("Foo bar\nbaz\n====\n") == "<h1>Foo bar\nbaz</h1>\n"
