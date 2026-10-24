"""Block engine tests: column helpers, the cursor, the registry, and the per-line procedure.

Each test builds a block tree with `parse_lines` and reads back the tree: child block type names,
paragraph content, and raw lines. Registry tests use block types defined here, which shows that
the loop never names a concrete type.
"""

import pytest

from mdparser import blocks
from mdparser.blocks import (
    DOCUMENT,
    PARAGRAPH,
    Block,
    BlockRegistry,
    BlockType,
    Cursor,
    DocumentParser,
    indent_columns,
    next_column,
    parse_lines,
)


def kinds(block: Block) -> list[str]:
    return [child.kind.name for child in block.children]


def paragraph_contents(block: Block) -> list[str]:
    return [child.content for child in block.children if child.kind is PARAGRAPH]


# --- Column helpers ---


def test_next_column_for_a_space_advances_one() -> None:
    assert next_column(" ", 3) == 4


def test_next_column_for_a_tab_advances_to_next_tab_stop() -> None:
    assert next_column("\t", 0) == 4
    assert next_column("\t", 2) == 4
    assert next_column("\t", 4) == 8


def test_indent_columns_counts_spaces() -> None:
    assert indent_columns("   x", 0, 0) == 3


def test_indent_columns_expands_a_leading_tab_to_four() -> None:
    assert indent_columns("\tx", 0, 0) == 4


def test_indent_columns_pads_a_tab_after_spaces_to_the_tab_stop() -> None:
    assert indent_columns("  \tx", 0, 0) == 4


def test_indent_columns_counts_two_tabs_as_eight() -> None:
    assert indent_columns("\t\tx", 0, 0) == 8


def test_indent_columns_is_zero_without_leading_whitespace() -> None:
    assert indent_columns("x  ", 0, 0) == 0


def test_indent_columns_starts_from_the_given_column() -> None:
    assert indent_columns("\tx", 0, 2) == 2


# --- Cursor ---


def test_cursor_rest_starts_as_the_whole_line() -> None:
    assert Cursor("abc").rest == "abc"


def test_cursor_is_blank_for_empty_and_whitespace_lines() -> None:
    assert Cursor("").is_blank()
    assert Cursor(" \t ").is_blank()


def test_cursor_is_not_blank_with_text() -> None:
    assert not Cursor("  a").is_blank()


def test_cursor_advance_nonspace_tracks_column_across_a_tab() -> None:
    cursor = Cursor("  \t x")
    cursor.advance_nonspace()
    assert cursor.pos == 4
    assert cursor.col == 5
    assert cursor.rest == "x"


def test_cursor_advance_columns_consumes_whole_tab_when_it_overshoots() -> None:
    cursor = Cursor("\tx")
    cursor.advance_columns(2)
    assert cursor.pos == 1
    assert cursor.col == 4
    assert cursor.rest == "x"


def test_cursor_advance_columns_stops_at_the_target_column() -> None:
    cursor = Cursor("    x")
    cursor.advance_columns(2)
    assert cursor.rest == "  x"


def test_cursor_indent_reports_columns_to_next_text() -> None:
    assert Cursor("\t\tx").indent == 8


def test_cursor_advance_to_moves_by_characters() -> None:
    cursor = Cursor("abc")
    cursor.advance_to(2)
    assert cursor.rest == "c"


# --- Empty and blank input ---


def test_empty_input_gives_empty_document() -> None:
    assert parse_lines([]).children == []


def test_one_empty_line_gives_empty_document() -> None:
    assert parse_lines([""]).children == []


def test_blank_lines_only_give_empty_document() -> None:
    assert parse_lines(["", "  ", "\t", " \t "]).children == []


def test_leading_and_trailing_blank_lines_add_no_blocks() -> None:
    root = parse_lines(["", " ", "word", "", "\t", ""])
    assert kinds(root) == ["paragraph"]
    assert paragraph_contents(root) == ["word"]


# --- Paragraphs ---


def test_single_line_makes_one_paragraph() -> None:
    root = parse_lines(["hello"])
    assert kinds(root) == ["paragraph"]
    assert paragraph_contents(root) == ["hello"]


def test_blank_line_separates_paragraphs() -> None:
    root = parse_lines(["one", "", "two"])
    assert paragraph_contents(root) == ["one", "two"]


def test_repeated_blank_lines_separate_paragraphs_without_extra_blocks() -> None:
    root = parse_lines(["one", "", "", "", "two"])
    assert kinds(root) == ["paragraph", "paragraph"]


def test_consecutive_lines_stay_in_one_paragraph() -> None:
    root = parse_lines(["first", "second", "third"])
    assert kinds(root) == ["paragraph"]
    assert paragraph_contents(root) == ["first\nsecond\nthird"]


def test_continuation_lines_drop_their_leading_indentation() -> None:
    root = parse_lines(["first", "      second", "\tthird"])
    assert paragraph_contents(root) == ["first\nsecond\nthird"]


def test_first_line_drops_leading_spaces() -> None:
    root = parse_lines(["  word"])
    assert paragraph_contents(root) == ["word"]


def test_final_spaces_and_tabs_are_removed_from_content() -> None:
    root = parse_lines(["word \t  "])
    assert paragraph_contents(root) == ["word"]


def test_trailing_spaces_on_an_interior_line_are_kept() -> None:
    root = parse_lines(["foo  ", "bar"])
    assert paragraph_contents(root) == ["foo  \nbar"]


def test_paragraph_is_closed_when_document_ends() -> None:
    root = parse_lines(["word"])
    assert all(not child.is_open for child in root.children)
    assert not root.is_open


def test_paragraph_is_closed_by_a_blank_line_before_the_next_one() -> None:
    root = parse_lines(["one", "", "two"])
    assert [child.is_open for child in root.children] == [False, False]


def test_document_root_is_a_container_with_no_content() -> None:
    root = parse_lines(["a"])
    assert root.kind is DOCUMENT
    assert root.content == ""


def test_paragraph_raw_lines_are_recorded_as_read() -> None:
    root = parse_lines(["one", "   two"])
    assert root.children[0].lines == ["one", "two"]


def _shape(root: Block) -> list[tuple[str, str]]:
    return [(child.kind.name, child.content) for child in root.children]


def test_parsing_the_same_lines_twice_gives_the_same_tree() -> None:
    lines = ["a", "", "b", "c"]
    assert _shape(parse_lines(lines)) == _shape(parse_lines(lines))


# --- Registry ---


def test_registry_rejects_a_duplicate_block_type_name() -> None:
    registry = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
    with pytest.raises(ValueError):
        registry.register(PARAGRAPH)


def test_default_registry_start_rules_are_setext_thematic_break_atx_heading_indented_fenced_html_block_quote_and_list_item() -> None:
    assert blocks.DEFAULT_REGISTRY.starts() == (
        blocks.SETEXT_HEADING,
        blocks.THEMATIC_BREAK,
        blocks.ATX_HEADING,
        blocks.INDENTED_CODE,
        blocks.FENCED_CODE,
        blocks.HTML_BLOCK,
        blocks.BLOCK_QUOTE,
        blocks.LIST_ITEM,
    )


def test_lazy_block_type_must_accept_lines() -> None:
    with pytest.raises(ValueError):
        BlockType("bad", continues=lambda block, cursor: True, lazy=True)


def test_leaf_block_type_must_have_an_add_line_rule() -> None:
    with pytest.raises(ValueError):
        BlockType("bad", continues=lambda block, cursor: True, accepts_lines=True)


# --- Extensibility: block types registered without changing the loop ---


def _rule_start(cursor: Cursor, container: Block) -> Block | None:
    if cursor.rest.strip(" \t") == "***":
        cursor.advance_to(len(cursor.line))
        return Block(RULE)
    return None


RULE = BlockType("rule", continues=lambda block, cursor: False, start=_rule_start)


def test_registered_start_rule_interrupts_a_paragraph() -> None:
    registry = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
    registry.register(RULE)
    root = parse_lines(["a", "***", "b"], registry)
    assert kinds(root) == ["paragraph", "rule", "paragraph"]
    assert paragraph_contents(root) == ["a", "b"]


def test_registered_start_rule_closes_an_unmatched_block_before_it_starts() -> None:
    registry = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
    registry.register(RULE)
    root = parse_lines(["***", "b"], registry)
    assert kinds(root) == ["rule", "paragraph"]
    assert root.children[0].is_open is False


def _raw_start(cursor: Cursor, container: Block) -> Block | None:
    if cursor.rest.startswith("<<"):
        cursor.advance_to(len(cursor.line))
        return Block(RAW)
    return None


RAW = BlockType(
    "raw",
    continues=lambda block, cursor: True,
    accepts_lines=True,
    add_line=lambda block, cursor: block.lines.append(cursor.rest),
    start=_raw_start,
)


def test_start_rule_is_not_tried_inside_a_non_interruptible_leaf() -> None:
    registry = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
    registry.register(RAW)
    registry.register(RULE)
    root = parse_lines(["<<", "***"], registry)
    assert kinds(root) == ["raw"]
    assert root.children[0].lines[-1] == "***"


# --- Lazy paragraph continuation, via a test-only container ---


def _quote_continues(block: Block, cursor: Cursor) -> bool:
    index = cursor.next_nonspace()
    if cursor.line[index : index + 1] == ">":
        cursor.advance_to(index + 1)
        return True
    return False


def _quote_start(cursor: Cursor, container: Block) -> Block | None:
    index = cursor.next_nonspace()
    if cursor.line[index : index + 1] == ">":
        cursor.advance_to(index + 1)
        return Block(QUOTE)
    return None


QUOTE = BlockType("quote", continues=_quote_continues, is_container=True, start=_quote_start)


def quote_registry() -> BlockRegistry:
    registry = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
    registry.register(QUOTE)
    return registry


def test_quote_holds_its_paragraph() -> None:
    root = parse_lines(["> a", "> b"], quote_registry())
    assert kinds(root) == ["quote"]
    assert kinds(root.children[0]) == ["paragraph"]
    assert paragraph_contents(root.children[0]) == ["a\nb"]


def test_unmarked_line_is_a_lazy_continuation_of_the_quote_paragraph() -> None:
    root = parse_lines(["> a", "b"], quote_registry())
    assert kinds(root) == ["quote"]
    assert paragraph_contents(root.children[0]) == ["a\nb"]


def test_blank_line_ends_the_lazy_continuation() -> None:
    root = parse_lines(["> a", "", "b"], quote_registry())
    assert kinds(root) == ["quote", "paragraph"]
    assert paragraph_contents(root.children[0]) == ["a"]
    assert paragraph_contents(root) == ["b"]


def test_document_parser_can_be_driven_one_line_at_a_time() -> None:
    parser = DocumentParser(quote_registry())
    parser.incorporate_line("> a")
    assert parser.root.open_last_child() is not None
    parser.incorporate_line("")
    root = parser.finish()
    assert kinds(root) == ["quote"]
