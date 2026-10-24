"""Indented code block tests: the four declared checks from FEATURE-Indented-Code.md, then block-tree
and exact-output tests through the `commonmark` executable.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
The corpus section examples that use lists are gated in the lists story and are not run here.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser.blocks import INDENTED_CODE, PARAGRAPH, parse_lines


def run_commonmark(project_root: Path, source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )


def kinds(lines: list[str]) -> list[str]:
    """Names of the top-level block types that `lines` produce, in order."""
    return [child.kind.name for child in parse_lines(lines).children]


def code_contents(lines: list[str]) -> list[str]:
    """The content of each top-level indented code block, in order."""
    return [child.content for child in parse_lines(lines).children if child.kind is INDENTED_CODE]


# --- Declared acceptance checks (transcribed from FEATURE-Indented-Code.md) ---


def test_indented_simple_block(project_root: Path) -> None:
    """Four-space-indented lines render one pre element whose code keeps the extra indentation and content."""
    first = "a simple"
    second = "  indented code block"
    source = "    " + first + "\n    " + second + "\n"
    result = run_commonmark(project_root, source)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert result.stdout.count("<code>") == 1
    assert first in result.stdout
    assert second in result.stdout


def test_indented_cannot_interrupt_paragraph(project_root: Path) -> None:
    """An indented line directly after paragraph text is a continuation, not a code block."""
    result = run_commonmark(project_root, "Foo\n    bar\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 0
    assert result.stdout.count("<p>") == 1


def test_indented_chunks_and_ending(project_root: Path) -> None:
    """Chunks separated by a blank line form one block, and an unindented line ends it and starts a paragraph."""
    result = run_commonmark(project_root, "    chunk1\n\n    chunk2\nbar\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert result.stdout.count("<p>") == 1


def test_indented_content_escaped_and_literal(project_root: Path) -> None:
    """Code content is escaped and not parsed as Markdown, so only the four code wrapper tags contribute angle brackets."""
    result = run_commonmark(project_root, "    <a/>\n    *hi*\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<") == 4
    assert result.stdout.count("<em>") == 0


def test_indented_tab_indentation(project_root: Path) -> None:
    """A leading tab counts as four columns of indentation."""
    result = run_commonmark(project_root, "\tfoo\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1


# --- Block tree: start rule ---


@pytest.mark.parametrize("indent", [4, 5, 8])
def test_four_or_more_columns_start_a_code_block(indent: int) -> None:
    assert kinds([" " * indent + "foo"]) == [INDENTED_CODE.name]


@pytest.mark.parametrize("indent", [0, 1, 2, 3])
def test_fewer_than_four_columns_do_not_start_a_code_block(indent: int) -> None:
    assert kinds([" " * indent + "foo"]) == [PARAGRAPH.name]


def test_one_tab_starts_a_code_block() -> None:
    assert kinds(["\tfoo"]) == [INDENTED_CODE.name]


def test_two_spaces_then_tab_is_four_columns() -> None:
    assert kinds(["  \tfoo"]) == [INDENTED_CODE.name]


def test_three_spaces_then_tab_is_four_columns() -> None:
    assert kinds(["   \tfoo"]) == [INDENTED_CODE.name]


def test_blank_line_alone_is_not_a_code_block() -> None:
    assert kinds(["    "]) == []


def test_indented_line_after_blank_starts_a_code_block() -> None:
    assert kinds(["Foo", "", "    bar"]) == [PARAGRAPH.name, INDENTED_CODE.name]


def test_indented_line_after_paragraph_is_continuation() -> None:
    assert kinds(["Foo", "    bar"]) == [PARAGRAPH.name]


def test_indented_line_after_paragraph_does_not_add_a_block() -> None:
    (paragraph,) = parse_lines(["Foo", "    bar"]).children
    assert paragraph.kind is PARAGRAPH
    assert paragraph.children == []


# --- Block tree: content and chunks ---


def test_code_content_keeps_indentation_beyond_four_columns() -> None:
    assert code_contents(["      two extra"]) == ["  two extra\n"]


def test_code_content_keeps_trailing_spaces() -> None:
    assert code_contents(["    foo   "]) == ["foo   \n"]


def test_code_content_keeps_tabs_beyond_the_first_four_columns() -> None:
    assert code_contents(["\t\tfoo"]) == ["\tfoo\n"]


def test_code_content_is_literal_markdown() -> None:
    assert code_contents(["    *hi* `x`"]) == ["*hi* `x`\n"]


def test_chunks_separated_by_blank_line_form_one_block() -> None:
    assert kinds(["    chunk1", "", "    chunk2"]) == [INDENTED_CODE.name]


def test_interior_blank_line_is_kept_in_content() -> None:
    assert code_contents(["    a", "", "    b"]) == ["a\n\nb\n"]


def test_interior_blank_line_keeps_indentation_beyond_four_columns() -> None:
    assert code_contents(["    a", "      ", "    b"]) == ["a\n  \nb\n"]


def test_interior_blank_line_with_less_than_four_columns_is_kept_empty() -> None:
    assert code_contents(["    a", "  ", "    b"]) == ["a\n\nb\n"]


def test_leading_blank_lines_are_not_part_of_the_block() -> None:
    assert kinds(["", "    a"]) == [INDENTED_CODE.name]
    assert code_contents(["", "    a"]) == ["a\n"]


def test_trailing_blank_lines_are_not_part_of_the_block() -> None:
    assert code_contents(["    a", "", "   ", ""]) == ["a\n"]


def test_unindented_line_ends_the_block_and_starts_a_paragraph() -> None:
    assert kinds(["    a", "bar"]) == [INDENTED_CODE.name, PARAGRAPH.name]


def test_unindented_heading_ends_the_block() -> None:
    assert kinds(["    a", "# bar"]) == [INDENTED_CODE.name, "atx_heading"]


def test_unindented_thematic_break_ends_the_block() -> None:
    assert kinds(["    a", "***"]) == [INDENTED_CODE.name, "thematic_break"]


def test_code_block_holds_no_children() -> None:
    (block,) = parse_lines(["    a"]).children
    assert block.children == []


def test_consecutive_code_blocks_split_on_unindented_line() -> None:
    assert code_contents(["    a", "b", "", "    c"]) == ["a\n", "c\n"]


# --- Exact output through the executable ---


def test_code_block_renders_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "    foo\n")
    assert result.stdout == "<pre><code>foo\n</code></pre>\n"


def test_code_block_escapes_html_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, '    <a href="x">&amp;</a>\n')
    assert result.stdout == "<pre><code>&lt;a href=&quot;x&quot;&gt;&amp;amp;&lt;/a&gt;\n</code></pre>\n"


def test_code_block_is_not_parsed_as_markdown_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "    *hi*\n")
    assert result.stdout == "<pre><code>*hi*\n</code></pre>\n"


def test_code_block_keeps_indentation_and_trailing_spaces_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "      two   \n")
    assert result.stdout == "<pre><code>  two   \n</code></pre>\n"


def test_chunks_render_as_one_block_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "    chunk1\n\n    chunk2\nbar\n")
    assert result.stdout == "<pre><code>chunk1\n\nchunk2\n</code></pre>\n<p>bar</p>\n"


def test_paragraph_continuation_renders_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "Foo\n    bar\n")
    assert result.stdout == "<p>Foo\nbar</p>\n"


def test_tab_indented_code_renders_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "\tfoo\n")
    assert result.stdout == "<pre><code>foo\n</code></pre>\n"


def test_blank_only_input_renders_no_code_block(project_root: Path) -> None:
    assert run_commonmark(project_root, "    \n\t\n").stdout == ""
