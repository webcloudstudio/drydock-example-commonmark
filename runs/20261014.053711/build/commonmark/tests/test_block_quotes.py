"""Block quote tests: the eight declared checks from FEATURE-Block-Quotes.md, then block-tree, cursor
and exact-output tests for marker handling, lazy continuation and the blank-line rule.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
"""

import subprocess
from pathlib import Path

from mdparser.blocks import BLOCK_QUOTE, DEFAULT_REGISTRY, PARAGRAPH, Block, Cursor, parse_lines


def run_commonmark(project_root: Path, source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )


def kinds(block: Block) -> list[str]:
    """Names of the child block types of `block`, in order."""
    return [child.kind.name for child in block.children]


def paragraph_texts(block: Block) -> list[str]:
    """Raw content of every paragraph under `block`, in document order."""
    texts: list[str] = []
    for child in block.children:
        if child.kind is PARAGRAPH:
            texts.append(child.content)
        texts.extend(paragraph_texts(child))
    return texts


# --- Declared acceptance checks (transcribed from FEATURE-Block-Quotes.md) ---


def test_quote_basic_content(project_root: Path) -> None:
    result = run_commonmark(project_root, "> # Foo\n> bar\n> baz\n")
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<h1>") == 1
    assert result.stdout.count("<p>") == 1


def test_quote_marker_space_optional(project_root: Path) -> None:
    for source in ("># Foo\n>bar\n", "   > # Foo\n   > bar\n"):
        result = run_commonmark(project_root, source)
        assert result.returncode == 0
        assert result.stdout.count("<blockquote>") == 1
        assert result.stdout.count("<h1>") == 1


def test_quote_lazy_continuation(project_root: Path) -> None:
    result = run_commonmark(project_root, "> bar\nbaz\n")
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<p>") == 1


def test_quote_nested_lazy(project_root: Path) -> None:
    result = run_commonmark(project_root, "> > > foo\nbar\n")
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 3
    assert result.stdout.count("<p>") == 1


def test_quote_blank_line_separates(project_root: Path) -> None:
    separated = run_commonmark(project_root, "> foo\n\n> bar\n")
    joined = run_commonmark(project_root, "> foo\n> bar\n")
    assert separated.returncode == 0
    assert joined.returncode == 0
    assert separated.stdout.count("<blockquote>") == 2
    assert joined.stdout.count("<blockquote>") == 1


def test_quote_interrupts_paragraph(project_root: Path) -> None:
    result = run_commonmark(project_root, "foo\n> bar\n")
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<p>") == 2


def test_quote_four_spaces_is_code(project_root: Path) -> None:
    result = run_commonmark(project_root, "    > foo\n")
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 0
    assert result.stdout.count("<pre>") == 1


def test_quote_no_lazy_code(project_root: Path) -> None:
    result = run_commonmark(project_root, ">     foo\n    bar\n")
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<pre>") == 2


# --- Exact output through the executable ---


def test_single_quote_output_is_exact(project_root: Path) -> None:
    assert run_commonmark(project_root, "> foo\n").stdout == "<blockquote>\n<p>foo</p>\n</blockquote>\n"


def test_empty_quote_marker_only_output_is_exact(project_root: Path) -> None:
    assert run_commonmark(project_root, ">\n").stdout == "<blockquote>\n</blockquote>\n"


def test_empty_input_renders_nothing(project_root: Path) -> None:
    assert run_commonmark(project_root, "").stdout == ""


def test_nested_quotes_output_is_exact(project_root: Path) -> None:
    result = run_commonmark(project_root, "> > foo\n")
    assert result.stdout == "<blockquote>\n<blockquote>\n<p>foo</p>\n</blockquote>\n</blockquote>\n"


def test_marker_only_line_keeps_one_quote_and_splits_paragraphs(project_root: Path) -> None:
    result = run_commonmark(project_root, "> foo\n>\n> bar\n")
    assert result.stdout == "<blockquote>\n<p>foo</p>\n<p>bar</p>\n</blockquote>\n"


def test_blank_line_ends_quote_and_following_text_is_a_paragraph(project_root: Path) -> None:
    result = run_commonmark(project_root, "> foo\n\nbar\n")
    assert result.stdout == "<blockquote>\n<p>foo</p>\n</blockquote>\n<p>bar</p>\n"


def test_quote_with_leading_indent_of_three_spaces_output_is_exact(project_root: Path) -> None:
    assert run_commonmark(project_root, "   > foo\n").stdout == "<blockquote>\n<p>foo</p>\n</blockquote>\n"


def test_quote_marker_with_tab_output_is_exact(project_root: Path) -> None:
    # The tab after the marker is one column of the optional space; its other three columns are text
    # indentation that the paragraph strips.
    assert run_commonmark(project_root, ">\tfoo\n").stdout == "<blockquote>\n<p>foo</p>\n</blockquote>\n"


def test_quote_partly_consumed_tab_leaves_columns_as_code_indentation(project_root: Path) -> None:
    # `>` and one column of the first tab form the marker. The rest of the first tab and the second tab
    # give six columns of indentation; the code rule takes four, leaving two spaces.
    assert run_commonmark(project_root, ">\t\tfoo\n").stdout == (
        "<blockquote>\n<pre><code>  foo\n</code></pre>\n</blockquote>\n"
    )


def test_quote_content_after_no_optional_space_keeps_text(project_root: Path) -> None:
    assert run_commonmark(project_root, ">foo\n").stdout == "<blockquote>\n<p>foo</p>\n</blockquote>\n"


# --- Block tree ---


def test_marker_creates_a_block_quote_holding_its_paragraph() -> None:
    root = parse_lines(["> foo"])
    assert kinds(root) == ["block_quote"]
    assert kinds(root.children[0]) == ["paragraph"]
    assert paragraph_texts(root) == ["foo"]


def test_default_registry_includes_block_quote() -> None:
    assert BLOCK_QUOTE in DEFAULT_REGISTRY.starts()


def test_two_marked_lines_form_one_quote() -> None:
    root = parse_lines(["> foo", "> bar"])
    assert kinds(root) == ["block_quote"]
    assert paragraph_texts(root) == ["foo\nbar"]


def test_blank_line_closes_the_quote_before_the_next_marked_line() -> None:
    root = parse_lines(["> foo", "", "> bar"])
    assert kinds(root) == ["block_quote", "block_quote"]
    assert [paragraph_texts(child) for child in root.children] == [["foo"], ["bar"]]


def test_quote_closes_at_end_of_input_and_is_finalized() -> None:
    root = parse_lines(["> foo"])
    assert root.children[0].is_open is False


def test_quote_may_be_entered_from_a_paragraph_without_a_blank_line() -> None:
    root = parse_lines(["foo", "> bar"])
    assert kinds(root) == ["paragraph", "block_quote"]
    assert paragraph_texts(root) == ["foo", "bar"]


def test_text_after_a_blank_line_is_not_part_of_the_quote_paragraph() -> None:
    root = parse_lines(["> foo", "", "bar"])
    assert kinds(root) == ["block_quote", "paragraph"]
    assert paragraph_texts(root.children[0]) == ["foo"]
    assert paragraph_texts(root) == ["foo", "bar"]


def test_nested_quote_nests_in_the_tree() -> None:
    root = parse_lines(["> > > foo"])
    depth = 0
    node = root
    while node.children and node.children[0].kind is BLOCK_QUOTE:
        node = node.children[0]
        depth += 1
    assert depth == 3
    assert kinds(node) == ["paragraph"]


def test_empty_quote_has_no_children() -> None:
    root = parse_lines([">"])
    assert kinds(root) == ["block_quote"]
    assert root.children[0].children == []


# --- Lazy continuation: only paragraph text may continue a quote without a marker ---


def test_lazy_line_joins_the_paragraph_inside_a_nested_quote() -> None:
    root = parse_lines(["> > foo", "> bar"])
    assert kinds(root) == ["block_quote"]
    assert kinds(root.children[0]) == ["block_quote"]
    assert paragraph_texts(root) == ["foo\nbar"]


def test_heading_does_not_continue_a_quote_lazily() -> None:
    root = parse_lines(["> foo", "# bar"])
    assert kinds(root) == ["block_quote", "atx_heading"]


def test_thematic_break_does_not_continue_a_quote_lazily() -> None:
    root = parse_lines(["> foo", "***"])
    assert kinds(root) == ["block_quote", "thematic_break"]


def test_fence_does_not_continue_a_quote_lazily() -> None:
    root = parse_lines(["> foo", "```", "bar"])
    assert kinds(root) == ["block_quote", "fenced_code"]
    assert paragraph_texts(root) == ["foo"]


def test_indented_code_does_not_continue_a_quote_lazily() -> None:
    root = parse_lines(["> foo", "    bar"])
    assert kinds(root) == ["block_quote"]
    assert paragraph_texts(root) == ["foo\nbar"]


def test_type_seven_html_does_not_interrupt_a_lazy_paragraph() -> None:
    root = parse_lines(["> foo", '<a href="x">'])
    assert kinds(root) == ["block_quote"]
    assert paragraph_texts(root) == ['foo\n<a href="x">']


def test_type_six_html_interrupts_a_quote_paragraph() -> None:
    root = parse_lines(["> foo", "<div>"])
    assert kinds(root) == ["block_quote", "html_block"]


def test_lazy_continuation_follows_the_deepest_open_paragraph() -> None:
    root = parse_lines(["> > foo", "bar", "baz"])
    assert kinds(root) == ["block_quote"]
    assert paragraph_texts(root) == ["foo\nbar\nbaz"]


def test_lazy_line_after_a_closed_inner_block_is_not_lazy() -> None:
    root = parse_lines(["> # foo", "bar"])
    assert kinds(root) == ["block_quote", "paragraph"]


# --- Cursor: column-aware consumption of a tab that is only partly taken ---


def test_consume_columns_splits_a_straddling_tab() -> None:
    cursor = Cursor("\tx")
    cursor.consume_columns(2)
    assert cursor.pos == 0
    assert cursor.col == 2
    assert cursor.rest == "  x"


def test_consume_columns_finishes_a_split_tab_on_the_next_consumption() -> None:
    cursor = Cursor("\tx")
    cursor.consume_columns(2)
    cursor.consume_columns(2)
    assert cursor.pos == 1
    assert cursor.col == 4
    assert cursor.rest == "x"


def test_consume_columns_takes_a_whole_tab_that_fits() -> None:
    cursor = Cursor("\tx")
    cursor.consume_columns(4)
    assert cursor.pos == 1
    assert cursor.rest == "x"


def test_consume_columns_takes_plain_spaces_one_column_each() -> None:
    cursor = Cursor("   x")
    cursor.consume_columns(2)
    assert cursor.rest == " x"


def test_consume_columns_stops_at_text() -> None:
    cursor = Cursor("a  b")
    cursor.consume_columns(3)
    assert cursor.pos == 0
    assert cursor.rest == "a  b"


def test_advance_to_past_a_split_tab_clears_the_split() -> None:
    cursor = Cursor("\tx")
    cursor.consume_columns(2)
    cursor.advance_to(1)
    assert cursor.rest == "x"
    assert cursor.in_tab is False


def test_split_tab_reports_its_remaining_columns_as_indent() -> None:
    cursor = Cursor("\tx")
    cursor.consume_columns(2)
    assert cursor.indent == 2
