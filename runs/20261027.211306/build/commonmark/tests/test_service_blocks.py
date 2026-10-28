from commonmark_parser.blocks import parse_blocks
from commonmark_parser.blocks import _atx
from commonmark_parser.fenced_code import parse_fenced_code
from commonmark_parser.html_blocks import parse_html_block
from commonmark_parser.indented_code import parse_indented_code
from commonmark_parser.references import extract_definitions


def test_thematic_break_interrupts_paragraph_and_rejects_mixed_markers():
    doc = parse_blocks("alpha\n* * *\n* - *\n")
    assert [node.kind for node in doc.children] == ["paragraph", "thematic_break", "paragraph"]


def test_thematic_break_can_be_the_content_of_a_list_item():
    doc = parse_blocks("- Foo\n- * * *\n")
    assert [child.kind for child in doc.children[0].children[1].children] == ["thematic_break"]


def test_atx_heading_level_closing_markers_and_invalid_opening():
    doc = parse_blocks("### alpha ###\n#gamma\n")
    assert [(n.kind, n.level, n.literal.strip()) for n in doc.children] == [("heading", 3, "alpha"), ("paragraph", None, "#gamma")]


def test_atx_heading_with_only_closing_hashes_has_empty_content():
    assert _atx("### ###") == (3, "")


def test_indented_code_preserves_interior_blank_and_extra_indent():
    assert parse_indented_code(["    alpha", "", "      beta", ""]) == ("alpha\n\n  beta\n", 3)


def test_indented_code_preserves_spaces_on_interior_blank_line():
    assert parse_indented_code(["    chunk1", "      ", "      chunk2"]) == (
        "chunk1\n  \n  chunk2\n", 3
    )


def test_indented_code_does_not_interrupt_paragraph():
    assert parse_indented_code(["    alpha"], paragraph_open=True) is None


def test_tab_stops_remain_based_on_the_original_line_after_list_indent():
    doc = parse_blocks("- foo\n\n\t\tbar\n")
    item = doc.children[0].children[0]
    assert [(child.kind, child.literal) for child in item.children] == [
        ("paragraph", "foo"),
        ("indented_code", "  bar\n"),
    ]


def test_tab_stops_after_list_marker_use_the_original_column():
    doc = parse_blocks("-\t\tfoo\n")
    code = doc.children[0].children[0].children[0]
    assert code.kind == "indented_code"
    assert code.literal == "  foo\n"


def test_fenced_code_requires_matching_closer_and_removes_indent():
    assert parse_fenced_code(["  ~~~ py", "  alpha", "~~~~", "tail"]) == ("alpha\n", "py", 3)
    assert parse_fenced_code(["``` bad ` info"]) is None


def test_html_comment_runs_through_closing_line():
    assert parse_html_block(["<!-- start", "", "finish -->", "tail"]) == ("<!-- start\n\nfinish -->\n", 3)


def test_html_custom_standalone_tag_cannot_interrupt_paragraph():
    assert parse_html_block(["<custom>"], paragraph_open=True) is None
    assert parse_html_block(["<div>", "body", "", "tail"], paragraph_open=True) == ("<div>\nbody\n", 2)


def test_reference_definitions_normalize_and_keep_first():
    refs = {}
    remaining = extract_definitions("[Alpha]: /first\n[alpha]: /second\n", refs)
    assert remaining == ""
    assert refs == {"alpha": ("/first", None)}


def test_block_parser_collects_references_document_wide():
    doc = parse_blocks("[Label]: /target\n\nvisible\n")
    assert doc.references == {"label": ("/target", None)}
    assert [node.literal for node in doc.children] == ["visible"]
