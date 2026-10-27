from commonmark_parser import Document, Node, parse_blocks, parse_inlines, render_html


def test_empty_document_runs_all_stages_without_content():
    source = ""
    document = parse_blocks(source)
    document = parse_inlines(document)
    assert render_html(document) == source


def test_document_exposes_block_tree_and_reference_map():
    document = Document(children=[Node("paragraph", raw="text")])
    assert document.children[0].type == "paragraph"
    assert document.references == {}


def test_inline_stage_returns_the_shared_document():
    document = parse_blocks("")
    assert parse_inlines(document) is document


def test_empty_rendering_is_idempotent():
    document = parse_inlines(parse_blocks(""))
    assert render_html(document) == render_html(document) == ""


def test_paragraph_block_tree_separates_blank_lines_and_preserves_content():
    document = parse_blocks("alpha\n\nbeta\n")

    assert [(node.type, node.raw_content) for node in document.children] == [
        ("paragraph", "alpha"),
        ("paragraph", "beta"),
    ]


def test_paragraph_accumulates_continuation_lines_and_normalizes_endings():
    document = parse_blocks("  alpha\r\n  beta\r")

    assert len(document.children) == 1
    assert document.children[0].raw_content == "alpha\nbeta"


def test_paragraph_replaces_null_characters():
    document = parse_blocks("a\x00b")

    assert document.children[0].raw_content == "a\ufffdb"


def test_thematic_break_interrupts_paragraph():
    document = parse_blocks("alpha\n* * *\n")

    assert [node.type for node in document.children] == ["paragraph", "thematic_break"]


def test_thematic_break_variants_and_indent_limit():
    document = parse_blocks("   ---\n\t***\n __ __ __")

    assert [node.type for node in document.children] == [
        "thematic_break", "code_block", "thematic_break"
    ]
