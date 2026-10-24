"""Thematic break tests: the four declared checks from FEATURE-Thematic-Breaks.md, then block-tree
and exact-output tests through the `commonmark` executable.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser.blocks import PARAGRAPH, THEMATIC_BREAK, parse_lines


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


# --- Declared acceptance checks (transcribed from FEATURE-Thematic-Breaks.md) ---


def test_thematic_three_markers(project_root: Path) -> None:
    """Lines of three or more matching marker characters each render one hr element."""
    lines = ["***", "---", "___", "_____________", " - - -", " **  * ** * ** * **"]
    source = "\n\n".join(lines) + "\n"
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    assert result.stdout.count("<hr />") == len(lines)


def test_thematic_not_a_break(project_root: Path) -> None:
    """Wrong characters, too few characters, mixed characters and trailing text do not produce hr elements."""
    source = "+++\n\n--\n\n_ _ _ _ a\n\na------\n\n *-*\n"
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    assert result.stdout.count("<hr />") == 0


def test_thematic_interrupts_paragraph(project_root: Path) -> None:
    """A thematic break directly after paragraph text splits it into two paragraphs around one hr."""
    result = run_commonmark(project_root, "Foo\n***\nbar\n")
    assert result.returncode == 0
    assert result.stdout.count("<hr />") == 1
    assert result.stdout.count("<p>") == 2


def test_thematic_trailing_whitespace(project_root: Path) -> None:
    """Trailing spaces and tabs after the marker characters are allowed."""
    result = run_commonmark(project_root, "- - - -    \t\n")
    assert result.returncode == 0
    assert result.stdout.count("<hr />") == 1


# --- Block tree: start rule boundaries ---


@pytest.mark.parametrize("marker", ["*", "-", "_"])
def test_three_matching_markers_form_a_break(marker: str) -> None:
    assert kinds([marker * 3]) == ["thematic_break"]


@pytest.mark.parametrize("marker", ["*", "-", "_"])
def test_two_markers_do_not_form_a_break(marker: str) -> None:
    assert kinds([marker * 2]) == ["paragraph"]


@pytest.mark.parametrize("marker", ["*", "-", "_"])
def test_long_run_of_markers_forms_a_break(marker: str) -> None:
    assert kinds([marker * 40]) == ["thematic_break"]


@pytest.mark.parametrize("indent", [1, 2, 3])
def test_up_to_three_spaces_of_indentation_form_a_break(indent: int) -> None:
    assert kinds([" " * indent + "***"]) == ["thematic_break"]


def test_four_spaces_of_indentation_is_not_a_break() -> None:
    assert kinds(["    ***"]) == ["indented_code"]


def test_one_tab_of_indentation_is_not_a_break() -> None:
    assert kinds(["\t***"]) == ["indented_code"]


def test_spaces_and_tabs_between_markers_are_allowed() -> None:
    assert kinds(["*\t \t*\t*"]) == ["thematic_break"]


def test_mixed_marker_characters_are_not_a_break() -> None:
    assert kinds(["*-*"]) == ["paragraph"]


def test_trailing_text_is_not_a_break() -> None:
    assert kinds(["***a"]) == ["paragraph"]


def test_leading_text_is_not_a_break() -> None:
    assert kinds(["a***"]) == ["paragraph"]


def test_unsupported_marker_character_is_not_a_break() -> None:
    assert kinds(["+++"]) == ["paragraph"]


def test_marker_run_with_trailing_space_is_a_break() -> None:
    assert kinds(["***   "]) == ["thematic_break"]


def test_blank_line_is_not_a_break() -> None:
    assert kinds(["   "]) == []


# --- Block tree: interaction with paragraphs and neighbours ---


def test_break_directly_after_paragraph_closes_the_paragraph() -> None:
    assert kinds(["Foo", "***"]) == ["paragraph", "thematic_break"]


def test_paragraph_resumes_after_break_without_blank_line() -> None:
    assert kinds(["Foo", "***", "bar"]) == ["paragraph", "thematic_break", "paragraph"]


def test_consecutive_breaks_are_separate_blocks() -> None:
    assert kinds(["***", "***", "***"]) == ["thematic_break"] * 3


def test_break_followed_by_blank_line_stays_one_block() -> None:
    assert kinds(["***", ""]) == ["thematic_break"]


def test_break_block_holds_no_children_or_lines() -> None:
    (block,) = parse_lines(["***"]).children
    assert block.kind is THEMATIC_BREAK
    assert block.children == []
    assert block.content == ""


def test_break_line_keeps_no_line_text() -> None:
    (block,) = parse_lines(["- - -   "]).children
    assert block.kind is THEMATIC_BREAK
    assert block.lines == []


def test_indented_marker_run_after_paragraph_is_paragraph_text() -> None:
    assert kinds(["Foo", "    ***"]) == ["paragraph"]


# --- Exact output through the executable ---


def test_break_renders_as_hr_exactly(project_root: Path) -> None:
    assert run_commonmark(project_root, "***\n").stdout == "<hr />\n"


def test_break_between_paragraphs_renders_exactly(project_root: Path) -> None:
    result = run_commonmark(project_root, "Foo\n***\nbar\n")
    assert result.stdout == "<p>Foo</p>\n<hr />\n<p>bar</p>\n"


def test_consecutive_breaks_render_exactly(project_root: Path) -> None:
    assert run_commonmark(project_root, "***\n\n---\n").stdout == "<hr />\n<hr />\n"


def test_trailing_whitespace_break_renders_exactly(project_root: Path) -> None:
    assert run_commonmark(project_root, "- - - -    \t\n").stdout == "<hr />\n"


def test_non_break_renders_as_code_block_exactly(project_root: Path) -> None:
    assert run_commonmark(project_root, "    ***\n").stdout == "<pre><code>***\n</code></pre>\n"


def test_paragraph_kind_is_unchanged_by_break_registration() -> None:
    assert kinds(["plain text"]) == [PARAGRAPH.name]
