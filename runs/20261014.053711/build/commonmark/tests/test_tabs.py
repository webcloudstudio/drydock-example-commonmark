"""Tab tests: the column helpers in `mdparser.blocks`, then exact-output tests for tabs in block structure.

Column helpers are checked by reading back the returned column, index or `rest` text. Block structure is
checked by the exact stdout bytes the executable writes. Tabs must never be expanded in rendered content.
"""

import subprocess
from pathlib import Path

from mdparser.blocks import Cursor, indent_columns, next_column


def run_commonmark(project_root: Path, source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )


# --- next_column: a tab advances to the next multiple of four ---


def test_next_column_tab_at_column_zero_advances_to_four() -> None:
    assert next_column("\t", 0) == 4


def test_next_column_tab_at_column_one_advances_to_four() -> None:
    assert next_column("\t", 1) == 4


def test_next_column_tab_on_a_stop_advances_a_full_four() -> None:
    assert next_column("\t", 4) == 8


def test_next_column_space_advances_one() -> None:
    assert next_column(" ", 3) == 4


def test_next_column_other_character_advances_one() -> None:
    assert next_column("x", 5) == 6


# --- indent_columns: width of a run of spaces and tabs ---


def test_indent_columns_empty_run_is_zero() -> None:
    assert indent_columns("foo", 0, 0) == 0


def test_indent_columns_counts_spaces() -> None:
    assert indent_columns("   foo", 0, 0) == 3


def test_indent_columns_single_tab_is_four() -> None:
    assert indent_columns("\tfoo", 0, 0) == 4


def test_indent_columns_tab_after_one_space_is_three() -> None:
    assert indent_columns(" \tfoo", 0, 0) == 4


def test_indent_columns_tab_after_three_spaces_is_one() -> None:
    assert indent_columns("   \tfoo", 0, 0) == 4


def test_indent_columns_two_tabs_is_eight() -> None:
    assert indent_columns("\t\tfoo", 0, 0) == 8


def test_indent_columns_measures_from_a_nonzero_column() -> None:
    assert indent_columns("\tfoo", 0, 2) == 2


# --- Cursor: a tab split by a container leaves its remaining columns as spaces ---


def test_cursor_tab_consumed_whole_moves_to_next_stop() -> None:
    cursor = Cursor("\tfoo")
    cursor.consume_columns(4)
    assert (cursor.pos, cursor.col, cursor.in_tab) == (1, 4, False)
    assert cursor.rest == "foo"


def test_cursor_tab_split_leaves_remaining_columns_as_spaces() -> None:
    cursor = Cursor("\tfoo")
    cursor.consume_columns(2)
    assert (cursor.pos, cursor.col, cursor.in_tab) == (0, 2, True)
    assert cursor.rest == "  foo"


def test_cursor_tab_split_by_one_column_leaves_three_spaces() -> None:
    cursor = Cursor("\tfoo")
    cursor.consume_columns(1)
    assert cursor.rest == "   foo"


def test_cursor_advance_columns_overshoots_a_straddling_tab() -> None:
    cursor = Cursor("\tfoo")
    cursor.advance_columns(2)
    assert (cursor.pos, cursor.col) == (1, 4)
    assert cursor.rest == "foo"


def test_cursor_rest_of_blank_remainder_is_empty() -> None:
    cursor = Cursor("  ")
    cursor.advance_nonspace()
    assert cursor.is_blank()
    assert cursor.rest == ""


# --- Exact output: indented code and tabs inside content ---


def test_leading_tab_opens_indented_code_with_tab_kept(project_root: Path) -> None:
    result = run_commonmark(project_root, "\tfoo\tbaz\t\tbim\n")
    assert result.returncode == 0
    assert result.stdout == "<pre><code>foo\tbaz\t\tbim\n</code></pre>\n"


def test_two_spaces_then_tab_opens_indented_code(project_root: Path) -> None:
    result = run_commonmark(project_root, "  \tfoo\tbaz\t\tbim\n")
    assert result.stdout == "<pre><code>foo\tbaz\t\tbim\n</code></pre>\n"


def test_tab_inside_indented_code_with_non_ascii_is_kept(project_root: Path) -> None:
    result = run_commonmark(project_root, "    a\ta\n    ὐ\ta\n")
    assert result.stdout == "<pre><code>a\ta\nὐ\ta\n</code></pre>\n"


def test_tab_indented_line_after_paragraph_is_lazy_code_text(project_root: Path) -> None:
    result = run_commonmark(project_root, "    foo\n\tbar\n")
    assert result.stdout == "<pre><code>foo\nbar\n</code></pre>\n"


def test_tabs_in_paragraph_text_are_not_expanded(project_root: Path) -> None:
    result = run_commonmark(project_root, "foo\tbar\n")
    assert result.stdout == "<p>foo\tbar</p>\n"


# --- Exact output: list continuation ---


def test_tab_indented_paragraph_continues_list_item(project_root: Path) -> None:
    result = run_commonmark(project_root, "  - foo\n\n\tbar\n")
    assert result.stdout == "<ul>\n<li>\n<p>foo</p>\n<p>bar</p>\n</li>\n</ul>\n"


def test_two_tabs_under_list_item_leave_two_columns_of_code(project_root: Path) -> None:
    result = run_commonmark(project_root, "- foo\n\n\t\tbar\n")
    assert result.stdout == "<ul>\n<li>\n<p>foo</p>\n<pre><code>  bar\n</code></pre>\n</li>\n</ul>\n"


def test_tab_after_ordered_marker_leaves_one_column_of_code(project_root: Path) -> None:
    result = run_commonmark(project_root, "1.\t\tfoo\n")
    assert result.stdout == "<ol>\n<li><pre><code> foo\n</code></pre>\n</li>\n</ol>\n"


# --- Exact output: tabs after container markers ---


def test_tab_after_quote_marker_leaves_code_inside_blockquote(project_root: Path) -> None:
    result = run_commonmark(project_root, ">\t\tfoo\n")
    assert result.stdout == "<blockquote>\n<pre><code>  foo\n</code></pre>\n</blockquote>\n"


def test_tab_after_bullet_marker_leaves_code_inside_item(project_root: Path) -> None:
    result = run_commonmark(project_root, "-\t\tfoo\n")
    assert result.stdout == "<ul>\n<li><pre><code>  foo\n</code></pre>\n</li>\n</ul>\n"


def test_tab_after_quote_marker_then_ordered_item_is_a_list(project_root: Path) -> None:
    result = run_commonmark(project_root, ">\t1.\tfoo\n")
    assert result.stdout == "<blockquote>\n<ol>\n<li>foo</li>\n</ol>\n</blockquote>\n"


# --- Exact output: tabs as separators ---


def test_tab_between_atx_marker_and_text_is_a_separator(project_root: Path) -> None:
    result = run_commonmark(project_root, "#\tFoo\n")
    assert result.stdout == "<h1>Foo</h1>\n"


def test_tabs_between_thematic_break_characters_are_separators(project_root: Path) -> None:
    result = run_commonmark(project_root, "*\t*\t*\t\n")
    assert result.stdout == "<hr />\n"


def test_tab_only_line_is_blank_and_renders_nothing(project_root: Path) -> None:
    result = run_commonmark(project_root, "\t\n")
    assert result.stdout == ""
