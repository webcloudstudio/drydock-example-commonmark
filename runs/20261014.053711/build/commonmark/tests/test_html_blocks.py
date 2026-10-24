"""HTML block tests: the seven declared checks from FEATURE-HTML-Blocks.md, then block-tree and
exact-output tests through the `commonmark` executable.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
The corpus section examples that use quotes, lists and indented code are gated in the tabs story
and are not run here.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser.blocks import HTML_BLOCK, Block, parse_lines


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


def html_blocks(lines: list[str]) -> list[Block]:
    """The top-level HTML blocks that `lines` produce, in order."""
    return [child for child in parse_lines(lines).children if child.kind is HTML_BLOCK]


def html_contents(lines: list[str]) -> list[str]:
    """The content of each top-level HTML block, in order."""
    return [block.content for block in html_blocks(lines)]


# --- Declared acceptance checks (transcribed from FEATURE-HTML-Blocks.md) ---


def test_htmlblock_type6_raw_lines(project_root: Path) -> None:
    """A block-level tag block passes through verbatim and its Markdown is not parsed."""
    block = "<div>\n*foo*\n</div>"
    result = run_commonmark(project_root, block + "\n")
    print(result.stdout)
    assert result.returncode == 0
    assert block in result.stdout
    assert result.stdout.count("<em>") == 0
    assert result.stdout.count("<p>") == 0


def test_htmlblock_type6_ends_at_blank_line(project_root: Path) -> None:
    """A type 6 block ends at a blank line and Markdown after it is parsed."""
    result = run_commonmark(project_root, "<div>\nraw\n\n*bar*\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1
    assert result.stdout.count("<em>") == 1


def test_htmlblock_comment_spans_blank_lines(project_root: Path) -> None:
    """A comment block keeps blank lines until its end marker, and the following line is a paragraph."""
    comment = "<!-- Foo\n\nbar\n   baz -->"
    result = run_commonmark(project_root, comment + "\nokay\n")
    print(result.stdout)
    assert result.returncode == 0
    assert comment in result.stdout
    assert result.stdout.count("<p>") == 1


def test_htmlblock_pre_spans_blank_lines(project_root: Path) -> None:
    """A pre block keeps blank lines and does not parse the Markdown inside it."""
    block = "<pre>\n*x*\n\n_y_\n</pre>"
    result = run_commonmark(project_root, block + "\n")
    print(result.stdout)
    assert result.returncode == 0
    assert block in result.stdout
    assert result.stdout.count("<em>") == 0


def test_htmlblock_type7_cannot_interrupt(project_root: Path) -> None:
    """A lone open tag line after paragraph text stays inside the paragraph."""
    result = run_commonmark(project_root, 'Foo\n<a href="bar">\nbaz\n')
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1


def test_htmlblock_type6_interrupts_paragraph(project_root: Path) -> None:
    """A block-level tag line interrupts a paragraph."""
    result = run_commonmark(project_root, "Foo\n<div>\nbar\n</div>\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1


def test_htmlblock_four_space_indent_is_code(project_root: Path) -> None:
    """Four spaces of indentation make an indented code block, not an HTML block."""
    result = run_commonmark(project_root, "    <!-- foo -->\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1


# --- Start conditions ---


@pytest.mark.parametrize("opener", ["<pre>", "<PRE>", "<script>", "<Style>", "<textarea>", "<pre class=\"x\">"])
def test_type1_start_matches_each_raw_text_tag(opener: str) -> None:
    """Start condition 1 holds for pre, script, style and textarea in any case, and keeps blank lines."""
    assert kinds([opener, "*a*", "", "*b*"]) == ["html_block"]


def test_type1_start_needs_a_space_tab_or_end_after_the_name() -> None:
    """`<prefix` is not start condition 1, and it is not a complete tag either."""
    assert kinds(["<prefix", "*a*"]) == ["paragraph"]


def test_type1_end_need_not_match_the_start_tag() -> None:
    """A script block ends at a style end tag."""
    assert html_contents(["<script>", "a", "</style>", "*b*"]) == ["<script>\na\n</style>\n"]


def test_type2_comment_start_and_end() -> None:
    """A comment block ends at the line that contains `-->`."""
    assert html_contents(["<!--", "a", "b -->", "*c*"]) == ["<!--\na\nb -->\n"]


def test_type2_start_needs_the_full_marker() -> None:
    """`<!-x` is not a comment start."""
    assert kinds(["<!-x", "*a*"]) == ["paragraph"]


def test_type3_processing_instruction_start_and_end() -> None:
    """A processing instruction block ends at the line that contains `?>`."""
    assert html_contents(["<?php", "a", "b ?>", "*c*"]) == ["<?php\na\nb ?>\n"]


def test_type4_declaration_ends_at_the_line_with_a_greater_than() -> None:
    """A declaration starts with `<!` and a letter, and its end line is the one with `>`."""
    assert html_contents(["<!DOCTYPE", "html>", "*c*"]) == ["<!DOCTYPE\nhtml>\n"]


def test_type4_needs_a_letter_after_the_bang() -> None:
    """`<!1` is not a declaration start."""
    assert kinds(["<!1x", "*a*"]) == ["paragraph"]


def test_type5_cdata_start_and_end() -> None:
    """A CDATA block ends at the line that contains `]]>`."""
    assert html_contents(["<![CDATA[", "a", "b ]]>", "*c*"]) == ["<![CDATA[\na\nb ]]>\n"]


def test_type5_needs_the_full_cdata_marker() -> None:
    """`<![CDATA` without its closing bracket is not a CDATA start."""
    assert kinds(["<![CDATA x", "*a*"]) == ["paragraph"]


@pytest.mark.parametrize("opener", ["<div>", "<DIV>", "<div/>", "<div class=\"x\">", "<div\t>", "<p>", "</div>"])
def test_type6_start_matches_block_tag_forms(opener: str) -> None:
    """Start condition 6 holds for an open or closing block tag followed by a space, tab, `>` or `/>`."""
    assert kinds([opener, "*a*"]) == ["html_block"]


@pytest.mark.parametrize("opener", ["<divx", "<dix", "<pa"])
def test_type6_start_needs_the_name_to_end_there(opener: str) -> None:
    """A block tag name followed by other letters is not start condition 6, and an incomplete tag is not type 7."""
    assert kinds([opener, "*a*"]) == ["paragraph"]


def test_type6_ends_before_a_blank_line_and_the_blank_is_not_kept() -> None:
    """A type 6 block stops at the blank line, which is not part of its content."""
    assert html_contents(["<div>", "a", "", "*b*"]) == ["<div>\na\n"]
    assert kinds(["<div>", "a", "", "*b*"]) == ["html_block", "paragraph"]


def test_type6_blank_line_with_spaces_and_tabs_ends_the_block() -> None:
    """A line of only spaces and tabs is a blank line for ending a type 6 block."""
    assert kinds(["<div>", "  \t ", "*a*"]) == ["html_block", "paragraph"]


@pytest.mark.parametrize("line", ['<a href="bar">', "<a href='x' title=y data>", "<custom>  ", "</a>", "<a/>"])
def test_type7_start_matches_a_complete_tag_alone_on_its_line(line: str) -> None:
    """Start condition 7 holds for a complete open tag or closing tag, then spaces and tabs."""
    assert kinds([line, "*a*"]) == ["html_block"]


@pytest.mark.parametrize("line", ['<a href="x"', "<a> b", "<a></a>", "< a>", "<a b=>"])
def test_type7_start_refuses_incomplete_or_trailing_content(line: str) -> None:
    """A tag that is not complete, or is followed by other text, is not start condition 7."""
    assert kinds([line, "*a*"]) == ["paragraph"]


def test_pre_tag_is_type1_so_a_blank_line_does_not_end_it() -> None:
    """`<pre>` is start condition 1, not 7, so its block keeps going past the blank line."""
    assert html_contents(["<pre>", "*a*", "", "*b*"]) == ["<pre>\n*a*\n\n*b*\n"]


# --- Interruption of a paragraph ---


@pytest.mark.parametrize("opener", ["<pre>", "<!--", "<?php", "<!DOCTYPE html", "<![CDATA[", "<div>"])
def test_types_1_to_6_interrupt_a_paragraph(opener: str) -> None:
    """Types 1 to 6 close an open paragraph and start an HTML block."""
    assert kinds(["Foo", opener, "*a*"]) == ["paragraph", "html_block"]


@pytest.mark.parametrize("line", ["<custom>", "</custom>", '<a href="b">'])
def test_type7_cannot_interrupt_a_paragraph(line: str) -> None:
    """A complete tag line after paragraph text stays in the paragraph."""
    assert kinds(["Foo", line, "baz"]) == ["paragraph"]


def test_type7_starts_after_a_blank_line_ends_the_paragraph() -> None:
    """Once a blank line closes the paragraph, type 7 can start a block."""
    assert kinds(["Foo", "", "<custom>", "*a*"]) == ["paragraph", "html_block"]


# --- End conditions and single-line blocks ---


@pytest.mark.parametrize(
    "line",
    ["<pre></pre>", "<!-- x -->", "<? x ?>", "<!x>", "<![CDATA[x]]>"],
)
def test_types_1_to_5_on_one_line_make_a_single_line_block(line: str) -> None:
    """When the first line meets both start and end conditions, the block is that line alone."""
    assert kinds([line, "*a*"]) == ["html_block", "paragraph"]
    assert html_contents([line, "*a*"]) == [line + "\n"]


def test_types_1_to_5_end_line_keeps_text_after_the_end_tag() -> None:
    """The end line is part of the block, including anything after its end tag."""
    assert html_contents(["<pre>", "x</pre> tail", "*a*"]) == ["<pre>\nx</pre> tail\n"]


def test_type1_block_runs_to_end_of_document_when_never_closed() -> None:
    """An unclosed type 1 block keeps every line to the end of the document, blank lines included."""
    assert html_contents(["<pre>", "a", "", "b"]) == ["<pre>\na\n\nb\n"]


def test_type2_block_runs_to_end_of_document_when_never_closed() -> None:
    """An unclosed comment block keeps every line to the end of the document."""
    assert html_contents(["<!--", "a", "", "b"]) == ["<!--\na\n\nb\n"]


def test_type6_block_at_end_of_document_has_no_trailing_blank_line() -> None:
    """A type 6 block with no following blank line ends at the end of the document."""
    assert html_contents(["<div>", "a"]) == ["<div>\na\n"]


# --- Raw lines and state ---


def test_lines_keep_their_original_indentation_and_are_not_parsed() -> None:
    """Indentation up to three spaces and inline Markdown are kept as written."""
    assert html_contents(["   <div>", "  *a* & <b>", "</div>"]) == ["   <div>\n  *a* & <b>\n</div>\n"]


def test_tags_inside_a_block_do_not_change_its_state() -> None:
    """A comment start inside a type 6 block is ignored, so the block still ends at the blank line."""
    lines = ["<div>", "<!--", "*x*", "</div>", "", "*y*"]
    assert kinds(lines) == ["html_block", "paragraph"]
    assert html_contents(lines) == ["<div>\n<!--\n*x*\n</div>\n"]


def test_a_three_space_indented_start_is_an_html_block() -> None:
    """Up to three spaces of indentation before the start condition are allowed."""
    assert kinds(["   <!-- x", "y -->"]) == ["html_block"]


def test_type6_block_is_just_its_start_line_when_a_blank_follows() -> None:
    """An HTML block whose start is followed by a blank line holds only the start line."""
    assert html_contents(["<div>", "", "*a*"]) == ["<div>\n"]


# --- Exact stdout through the executable ---


def test_html_block_output_is_the_raw_bytes_with_no_escaping(project_root: Path) -> None:
    """The block goes to stdout exactly as written, with `&` and `<` left unescaped."""
    source = "<div>\n*a* & <b>\n</div>\n"
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    assert result.stdout == "<div>\n*a* & <b>\n</div>\n"


def test_html_block_then_paragraph_output_is_exact(project_root: Path) -> None:
    """A type 6 block followed by a blank line and a paragraph renders both exactly."""
    result = run_commonmark(project_root, "<div>\nraw\n\n*bar*\n")
    assert result.returncode == 0
    assert result.stdout == "<div>\nraw\n<p><em>bar</em></p>\n"


def test_html_block_keeps_non_ascii_text_unchanged(project_root: Path) -> None:
    """Raw HTML is not percent-encoded or escaped, so non-ASCII text passes through."""
    result = run_commonmark(project_root, "<div>é</div>\n")
    assert result.returncode == 0
    assert result.stdout == "<div>é</div>\n"


def test_html_block_with_nested_table_example_output_is_exact(project_root: Path) -> None:
    """A type 6 block ends at its blank line, so the Markdown after it is parsed and the raw text is kept."""
    source = "<table><tr><td>\n<pre>\n**Hello**,\n\n_world_.\n</pre>\n</td></tr></table>\n"
    expected = (
        "<table><tr><td>\n<pre>\n**Hello**,\n"
        "<p><em>world</em>.\n</pre></p>\n"
        "</td></tr></table>\n"
    )
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    assert result.stdout == expected
