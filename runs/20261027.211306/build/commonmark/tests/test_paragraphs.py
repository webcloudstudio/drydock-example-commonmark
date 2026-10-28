from commonmark_parser.blocks import parse_blocks


def test_consecutive_lines_form_paragraphs_separated_by_blank_lines():
    first, second, third = "alpha", "beta", "gamma"
    document = parse_blocks(first + "\n" + second + "\n\n" + third + "\n")

    assert len(document.children) == 2
    assert all(node.kind == "paragraph" for node in document.children)
    assert document.children[0].literal.splitlines() == [first, second]
    assert document.children[1].literal.strip() == third


def test_boundary_blanks_are_ignored_and_continuation_indent_is_removed():
    document = parse_blocks("\n  alpha\n    beta\n\n")

    assert len(document.children) == 1
    assert document.children[0].kind == "paragraph"
    assert document.children[0].literal.splitlines() == ["alpha", "beta"]


def test_continuation_trailing_spaces_are_preserved_but_final_trailing_spaces_are_trimmed():
    document = parse_blocks("alpha  \n  beta  \n\n")

    assert document.children[0].literal == "alpha  \nbeta"


def test_whitespace_only_lines_separate_paragraphs():
    document = parse_blocks("one\n \t \ntwo")

    assert [node.literal for node in document.children] == ["one", "two"]


def test_empty_and_blank_only_documents_have_no_paragraphs():
    assert parse_blocks("").children == []
    assert parse_blocks(" \t\n\n").children == []
