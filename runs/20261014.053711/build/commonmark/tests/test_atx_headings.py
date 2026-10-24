"""ATX heading tests: the six declared checks from FEATURE-ATX-Headings.md, then block-tree and
exact-output tests through the `commonmark` executable.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser.blocks import ATX_HEADING, INDENTED_CODE, PARAGRAPH, parse_lines


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


# --- Declared acceptance checks (transcribed from FEATURE-ATX-Headings.md) ---


@pytest.mark.parametrize("level", range(1, 7))
def test_atx_levels_one_to_six(project_root: Path, level: int) -> None:
    """Each opening-sequence length from 1 to 6 renders exactly one heading of that level."""
    source = "#" * level + " foo\n"
    result = run_commonmark(project_root, source)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h" + str(level) + ">") == 1
    assert result.stdout.count("<h") == 1


def test_atx_not_a_heading(project_root: Path) -> None:
    """Seven hashes, a missing space, and an escaped hash do not produce headings."""
    source = "####### foo\n\n#hashtag\n\n\\## foo\n"
    result = run_commonmark(project_root, source)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h") == 0
    assert result.stdout.count("<p>") == 3


def test_atx_closing_sequence(project_root: Path) -> None:
    """A closing hash sequence is removed from the heading content."""
    result = run_commonmark(project_root, "## foo ##\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h2>") == 1
    assert result.stdout.count("#") == 0


def test_atx_empty_heading(project_root: Path) -> None:
    """Empty headings are allowed, one per line."""
    result = run_commonmark(project_root, "#\n\n##\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h1>") == 1
    assert result.stdout.count("<h2>") == 1


def test_atx_interrupts_paragraph(project_root: Path) -> None:
    """A heading splits a paragraph without blank lines, leaving two paragraphs around it."""
    result = run_commonmark(project_root, "Foo bar\n# baz\nBar foo\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<h1>") == 1
    assert result.stdout.count("<p>") == 2


def test_atx_indentation_limit(project_root: Path) -> None:
    """Up to three spaces of indentation are allowed before the opening sequence, and four are not."""
    allowed = run_commonmark(project_root, "   # foo\n")
    refused = run_commonmark(project_root, "    # foo\n")
    print(allowed.stdout)
    print(refused.stdout)
    assert allowed.returncode == 0
    assert refused.returncode == 0
    assert allowed.stdout.count("<h1>") == 1
    assert refused.stdout.count("<h1>") == 0


# --- Block tree: opening sequence ---


@pytest.mark.parametrize("level", range(1, 7))
def test_opening_run_of_each_length_is_a_heading(level: int) -> None:
    assert kinds(["#" * level + " foo"]) == [ATX_HEADING.name]


@pytest.mark.parametrize("level", range(1, 7))
def test_heading_block_records_its_level(level: int) -> None:
    (block,) = parse_lines(["#" * level + " foo"]).children
    assert block.level == level


def test_seven_hashes_is_not_a_heading() -> None:
    assert kinds(["####### foo"]) == [PARAGRAPH.name]


def test_hash_without_following_space_is_not_a_heading() -> None:
    assert kinds(["#hashtag"]) == [PARAGRAPH.name]


def test_hash_followed_by_tab_is_a_heading() -> None:
    assert kinds(["#\tfoo"]) == [ATX_HEADING.name]


def test_lone_hash_is_an_empty_heading() -> None:
    (block,) = parse_lines(["#"]).children
    assert block.kind is ATX_HEADING
    assert block.level == 1
    assert block.content == ""


@pytest.mark.parametrize("indent", [1, 2, 3])
def test_up_to_three_spaces_of_indentation_form_a_heading(indent: int) -> None:
    assert kinds([" " * indent + "# foo"]) == [ATX_HEADING.name]


def test_four_spaces_of_indentation_is_not_a_heading() -> None:
    assert kinds(["    # foo"]) == [INDENTED_CODE.name]


def test_one_tab_of_indentation_is_not_a_heading() -> None:
    assert kinds(["\t# foo"]) == [INDENTED_CODE.name]


def test_escaped_hash_is_not_a_heading() -> None:
    assert kinds(["\\# foo"]) == [PARAGRAPH.name]


# --- Block tree: content and closing sequence ---


@pytest.mark.parametrize(
    ("line", "content"),
    [
        ("# foo", "foo"),
        ("#   foo   ", "foo"),
        ("#\tfoo\t", "foo"),
        ("# foo ##", "foo"),
        ("# foo #", "foo"),
        ("# foo ##   ", "foo"),
        ("# foo \t#\t", "foo"),
        ("# foo ## bar", "foo ## bar"),
        ("# foo#", "foo#"),
        ("# foo\\#", "foo\\#"),
        ("# foo \\#", "foo \\#"),
        ("# ##", ""),
        ("# #", ""),
        ("#", ""),
    ],
)
def test_heading_content_after_stripping_and_closing_sequence(line: str, content: str) -> None:
    (block,) = parse_lines([line]).children
    assert block.content == content


def test_heading_block_holds_no_children_or_lines() -> None:
    (block,) = parse_lines(["# foo"]).children
    assert block.children == []
    assert block.lines == []


# --- Block tree: interaction with paragraphs and neighbours ---


def test_heading_directly_after_paragraph_closes_the_paragraph() -> None:
    assert kinds(["Foo", "# bar"]) == [PARAGRAPH.name, ATX_HEADING.name]


def test_paragraph_resumes_after_heading_without_blank_line() -> None:
    assert kinds(["Foo", "# bar", "baz"]) == [PARAGRAPH.name, ATX_HEADING.name, PARAGRAPH.name]


def test_consecutive_headings_are_separate_blocks() -> None:
    assert kinds(["# a", "## b", "### c"]) == [ATX_HEADING.name] * 3


def test_heading_followed_by_blank_line_stays_one_block() -> None:
    assert kinds(["# a", ""]) == [ATX_HEADING.name]


def test_text_after_heading_without_blank_line_is_a_new_paragraph() -> None:
    assert kinds(["# a", "b"]) == [ATX_HEADING.name, PARAGRAPH.name]


def test_indented_hash_after_paragraph_is_paragraph_text() -> None:
    assert kinds(["Foo", "    # bar"]) == [PARAGRAPH.name]


# --- Exact output through the executable ---


@pytest.mark.parametrize("level", range(1, 7))
def test_heading_renders_exactly_at_each_level(project_root: Path, level: int) -> None:
    assert render(project_root, "#" * level + " foo\n") == f"<h{level}>foo</h{level}>\n"


def test_heading_content_is_parsed_as_inlines(project_root: Path) -> None:
    assert render(project_root, "# *foo* `bar`\n") == "<h1><em>foo</em> <code>bar</code></h1>\n"


def test_heading_content_is_escaped(project_root: Path) -> None:
    assert render(project_root, "# a < b\n") == "<h1>a &lt; b</h1>\n"


def test_closing_sequence_is_removed_exactly(project_root: Path) -> None:
    assert render(project_root, "## foo ##\n") == "<h2>foo</h2>\n"


def test_escaped_closing_hash_is_kept_exactly(project_root: Path) -> None:
    assert render(project_root, "### foo \\###\n") == "<h3>foo ###</h3>\n"


def test_empty_headings_render_exactly(project_root: Path) -> None:
    assert render(project_root, "#\n\n##\n") == "<h1></h1>\n<h2></h2>\n"


def test_heading_between_paragraphs_renders_exactly(project_root: Path) -> None:
    assert render(project_root, "Foo bar\n# baz\nBar foo\n") == (
        "<p>Foo bar</p>\n<h1>baz</h1>\n<p>Bar foo</p>\n"
    )


def test_heading_trailing_whitespace_renders_exactly(project_root: Path) -> None:
    assert render(project_root, "#   foo   \n") == "<h1>foo</h1>\n"


def test_seven_hashes_renders_as_paragraph_exactly(project_root: Path) -> None:
    assert render(project_root, "####### foo\n") == "<p>####### foo</p>\n"
