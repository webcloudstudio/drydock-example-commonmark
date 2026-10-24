"""Setext heading tests: the seven declared checks from FEATURE-Setext-Headings.md, then block-tree and
exact-output tests through the `commonmark` executable.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser.blocks import PARAGRAPH, SETEXT_HEADING, THEMATIC_BREAK, parse_lines


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


def render(project_root: Path, source: str) -> str:
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    return result.stdout


# --- Declared acceptance checks (transcribed from FEATURE-Setext-Headings.md) ---


def test_setext_both_levels(project_root: Path) -> None:
    """Equals underlines give h1 and dash underlines give h2."""
    equals = run_commonmark(project_root, "Foo *bar*\n=========\n")
    dashes = run_commonmark(project_root, "Foo *bar*\n---------\n")
    print(equals.stdout)
    print(dashes.stdout)
    assert equals.returncode == 0
    assert dashes.returncode == 0
    assert equals.stdout.count("<h1>") == 1
    assert dashes.stdout.count("<h2>") == 1
    assert equals.stdout.count("<em>") == 1


def test_setext_multiline_content(project_root: Path) -> None:
    """Several paragraph lines before the underline become one heading with no paragraph."""
    result = run_commonmark(project_root, "Foo\nBar\n---\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h2>") == 1
    assert result.stdout.count("<p>") == 0


def test_setext_underline_beats_thematic_break(project_root: Path) -> None:
    """Dashes after paragraph text make a heading, not a thematic break."""
    result = run_commonmark(project_root, "Foo\n---\nbar\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h2>") == 1
    assert result.stdout.count("<hr />") == 0
    assert result.stdout.count("<p>") == 1


def test_setext_sequence_with_thematic_breaks(project_root: Path) -> None:
    """Dashes with no preceding paragraph are thematic breaks, mixed with two setext headings and a paragraph."""
    result = run_commonmark(project_root, "---\nFoo\n---\nBar\n---\nBaz\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<hr />") == 1
    assert result.stdout.count("<h2>") == 2
    assert result.stdout.count("<p>") == 1


def test_setext_underline_limits(project_root: Path) -> None:
    """Four spaces of indentation or internal spaces disqualify the underline."""
    for source in ("Foo\n    ---\n", "Foo\n= =\n"):
        result = run_commonmark(project_root, source)
        print(result.stdout)
        assert result.returncode == 0
        assert result.stdout.count("<h1>") == 0
        assert result.stdout.count("<h2>") == 0
        assert result.stdout.count("<p>") == 1


def test_setext_not_lazy_in_quote(project_root: Path) -> None:
    """An unmarked underline after a quote paragraph does not make a heading inside the quote."""
    result = run_commonmark(project_root, "> foo\nbar\n===\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h1>") == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<p>") == 1


def test_setext_quote_then_thematic_break(project_root: Path) -> None:
    """Dashes after a quote without a marker are a thematic break outside the quote."""
    result = run_commonmark(project_root, "> Foo\n---\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<blockquote>") == 1
    assert result.stdout.count("<hr />") == 1
    assert result.stdout.count("<h2>") == 0


def test_setext_empty_is_paragraph(project_root: Path) -> None:
    """An underline with no content line is not a heading."""
    result = run_commonmark(project_root, "\n====\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h1>") == 0
    assert result.stdout.count("<p>") == 1


# --- Block tree: underline levels and shape ---


@pytest.mark.parametrize(("marker", "level"), [("=", 1), ("-", 2)])
def test_underline_run_makes_setext_heading_at_its_level(marker: str, level: int) -> None:
    (block,) = parse_lines(["Foo", marker * 3]).children
    assert block.kind is SETEXT_HEADING
    assert block.level == level


@pytest.mark.parametrize("length", [1, 2, 9])
def test_underline_of_any_length_is_a_heading(length: int) -> None:
    assert kinds(["Foo", "=" * length]) == [SETEXT_HEADING.name]


def test_heading_content_is_all_paragraph_lines_joined() -> None:
    (block,) = parse_lines(["Foo", "Bar", "---"]).children
    assert block.content == "Foo\nBar"


def test_heading_content_strips_surrounding_spaces_and_tabs() -> None:
    (block,) = parse_lines([" Foo \t", "==="]).children
    assert block.content == "Foo"


def test_heading_block_holds_no_children_or_lines() -> None:
    (block,) = parse_lines(["Foo", "==="]).children
    assert block.children == []
    assert block.lines == []


def test_trailing_spaces_on_underline_are_allowed() -> None:
    assert kinds(["Foo", "===   \t"]) == [SETEXT_HEADING.name]


@pytest.mark.parametrize("indent", [1, 2, 3])
def test_up_to_three_spaces_before_underline(indent: int) -> None:
    assert kinds(["Foo", " " * indent + "==="]) == [SETEXT_HEADING.name]


def test_four_spaces_before_underline_is_paragraph_text() -> None:
    (block,) = parse_lines(["Foo", "    ==="]).children
    assert block.kind is PARAGRAPH
    assert block.content == "Foo\n==="


def test_internal_space_in_underline_is_paragraph_text() -> None:
    (block,) = parse_lines(["Foo", "= ="]).children
    assert block.kind is PARAGRAPH


def test_underline_with_other_characters_is_paragraph_text() -> None:
    assert kinds(["Foo", "=-="]) == [PARAGRAPH.name]


def test_mixed_marker_underline_is_not_setext() -> None:
    assert kinds(["Foo", "-=-"]) == [PARAGRAPH.name]


# --- Block tree: precedence over thematic break ---


def test_dashes_after_paragraph_are_not_a_thematic_break() -> None:
    assert kinds(["Foo", "---"]) == [SETEXT_HEADING.name]


def test_dashes_without_paragraph_are_a_thematic_break() -> None:
    assert kinds(["---"]) == [THEMATIC_BREAK.name]


def test_asterisks_after_paragraph_are_a_thematic_break() -> None:
    assert kinds(["Foo", "***"]) == [PARAGRAPH.name, THEMATIC_BREAK.name]


def test_underscores_after_paragraph_are_a_thematic_break() -> None:
    assert kinds(["Foo", "___"]) == [PARAGRAPH.name, THEMATIC_BREAK.name]


def test_equals_alone_is_paragraph_text() -> None:
    assert kinds(["===="]) == [PARAGRAPH.name]


def test_empty_setext_heading_is_never_produced() -> None:
    assert kinds(["", "===="]) == [PARAGRAPH.name]


# --- Block tree: neighbours and continuation ---


def test_paragraph_resumes_after_setext_heading() -> None:
    assert kinds(["Foo", "===", "bar"]) == [SETEXT_HEADING.name, PARAGRAPH.name]


def test_setext_heading_followed_by_blank_line_stays_one_block() -> None:
    assert kinds(["Foo", "===", ""]) == [SETEXT_HEADING.name]


def test_paragraph_before_setext_heading_is_replaced_not_kept() -> None:
    assert kinds(["Foo", "Bar", "==="]) == [SETEXT_HEADING.name]


def test_second_underline_after_new_paragraph_makes_second_heading() -> None:
    assert kinds(["Foo", "===", "Bar", "==="]) == [SETEXT_HEADING.name, SETEXT_HEADING.name]


def test_heading_inside_quote_when_underline_is_marked() -> None:
    (quote,) = parse_lines(["> Foo", "> ==="]).children
    assert quote.kind.name == "block_quote"
    assert [child.kind.name for child in quote.children] == [SETEXT_HEADING.name]


def test_link_definition_is_not_heading_text() -> None:
    (block,) = parse_lines(["[foo]: /url", "Bar", "==="]).children
    assert block.kind is SETEXT_HEADING
    assert block.content == "Bar"


def test_link_definition_only_makes_underline_paragraph_text() -> None:
    assert kinds(["[foo]: /url", "==="]) == [PARAGRAPH.name]


def test_link_definition_only_with_dashes_is_a_thematic_break() -> None:
    assert kinds(["[foo]: /url", "---"]) == [THEMATIC_BREAK.name]


# --- Exact output through the executable ---


@pytest.mark.parametrize(("marker", "level"), [("=", 1), ("-", 2)])
def test_setext_renders_exactly_at_each_level(project_root: Path, marker: str, level: int) -> None:
    assert render(project_root, f"Foo\n{marker * 3}\n") == f"<h{level}>Foo</h{level}>\n"


def test_setext_content_is_parsed_as_inlines(project_root: Path) -> None:
    assert render(project_root, "Foo *bar*\n=========\n") == "<h1>Foo <em>bar</em></h1>\n"


def test_setext_multiline_renders_with_soft_line_break(project_root: Path) -> None:
    assert render(project_root, "Foo\nBar\n---\n") == "<h2>Foo\nBar</h2>\n"


def test_setext_trailing_spaces_on_last_line_are_not_a_hard_break(project_root: Path) -> None:
    assert render(project_root, "Foo\nBar  \n---\n") == "<h2>Foo\nBar</h2>\n"


def test_setext_trailing_spaces_on_inner_line_are_a_hard_break(project_root: Path) -> None:
    assert render(project_root, "Foo  \nBar\n---\n") == "<h2>Foo<br />\nBar</h2>\n"


def test_setext_content_is_escaped(project_root: Path) -> None:
    assert render(project_root, "a < b\n===\n") == "<h1>a &lt; b</h1>\n"


def test_setext_sequence_renders_exactly(project_root: Path) -> None:
    assert render(project_root, "---\nFoo\n---\nBar\n---\nBaz\n") == (
        "<hr />\n<h2>Foo</h2>\n<h2>Bar</h2>\n<p>Baz</p>\n"
    )


def test_setext_link_definition_renders_exactly(project_root: Path) -> None:
    assert render(project_root, "[foo]: /url\nBar\n===\n") == "<h1>Bar</h1>\n"


def test_underline_only_renders_as_paragraph_exactly(project_root: Path) -> None:
    assert render(project_root, "====\n") == "<p>====</p>\n"
