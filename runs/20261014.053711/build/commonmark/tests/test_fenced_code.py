"""Fenced code block tests: the seven declared checks from FEATURE-Fenced-Code.md, then block-tree and
exact-output tests through the `commonmark` executable.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
block tree returned by `parse_lines` and on the exact stdout bytes, which is the state handed back.
The corpus section examples that use quotes, lists and setext headings are gated in the lists story
and are not run here.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser.blocks import FENCED_CODE, INDENTED_CODE, PARAGRAPH, Block, Fence, parse_lines


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


def fenced_blocks(lines: list[str]) -> list[Block]:
    """The top-level fenced code blocks that `lines` produce, in order."""
    return [child for child in parse_lines(lines).children if child.kind is FENCED_CODE]


def code_contents(lines: list[str]) -> list[str]:
    """The content of each top-level fenced code block, in order."""
    return [block.content for block in fenced_blocks(lines)]


def fence_of(lines: list[str]) -> Fence:
    """The opening fence of the only top-level fenced code block that `lines` produce."""
    (block,) = fenced_blocks(lines)
    assert block.fence is not None
    return block.fence


# --- Declared acceptance checks (transcribed from FEATURE-Fenced-Code.md) ---


def test_fenced_backtick_and_tilde(project_root: Path) -> None:
    """Backtick and tilde fences each render one pre element containing the supplied body."""
    body = "some body text"
    for fence in ("```", "~~~"):
        source = fence + "\n" + body + "\n" + fence + "\n"
        result = run_commonmark(project_root, source)
        print(result.stdout)
        assert result.returncode == 0
        assert result.stdout.count("<pre>") == 1
        assert body in result.stdout


def test_fenced_info_string_language_class(project_root: Path) -> None:
    """The first word of the info string becomes the language class."""
    language = "ruby"
    source = "```" + language + " extra words\ncode\n```\n"
    result = run_commonmark(project_root, source)
    print(result.stdout)
    assert result.returncode == 0
    assert ('class="language-' + language + '"') in result.stdout


def test_fenced_closing_fence_rules(project_root: Path) -> None:
    """A fence of the other character, or a shorter fence, does not close the block."""
    other = "~~~"
    shorter = "```"
    source = "````\naaa\n" + other + "\n" + shorter + "\n"
    result = run_commonmark(project_root, source)
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert other in result.stdout
    assert shorter in result.stdout


def test_fenced_unclosed_runs_to_end(project_root: Path) -> None:
    """An unclosed fence consumes the rest of the document as code."""
    trailing = "still code"
    result = run_commonmark(project_root, "```\nfirst\n\n" + trailing + "\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert result.stdout.count("<p>") == 0
    assert trailing in result.stdout


def test_fenced_interrupts_paragraph(project_root: Path) -> None:
    """A fence interrupts a paragraph and text after it starts a new paragraph."""
    result = run_commonmark(project_root, "foo\n```\nbar\n```\nbaz\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert result.stdout.count("<p>") == 2


def test_fenced_two_backticks_not_a_fence(project_root: Path) -> None:
    """Two backticks do not open a fence; they form a code span instead."""
    result = run_commonmark(project_root, "``\nfoo\n``\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 0
    assert result.stdout.count("<code>") == 1


def test_fenced_indentation_stripped(project_root: Path) -> None:
    """Content indentation up to the fence indentation is removed, and unindented lines are kept."""
    result = run_commonmark(project_root, " ```\n aaa\naaa\n```\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<pre>") == 1
    assert result.stdout.count("aaa") == 2
    assert result.stdout.count(" aaa") == 0


# --- Block tree: opening fence ---


@pytest.mark.parametrize("fence", ["```", "~~~", "````", "~~~~~"])
def test_fence_of_three_or_more_characters_starts_a_block(fence: str) -> None:
    assert kinds([fence, "code", fence]) == [FENCED_CODE.name]


@pytest.mark.parametrize("fence", ["``", "~~", "`", "~"])
def test_fewer_than_three_characters_do_not_start_a_block(fence: str) -> None:
    assert kinds([fence, "code", fence]) == [PARAGRAPH.name]


@pytest.mark.parametrize("indent", [0, 1, 2, 3])
def test_fence_indented_up_to_three_columns_starts_a_block(indent: int) -> None:
    assert kinds([" " * indent + "```", "code", "```"]) == [FENCED_CODE.name]


@pytest.mark.parametrize("indent", [4, 5, 8])
def test_fence_indented_four_or_more_columns_is_not_a_fence(indent: int) -> None:
    assert kinds([" " * indent + "```"]) == [INDENTED_CODE.name]


def test_backtick_info_string_with_a_backtick_is_not_a_fence() -> None:
    assert kinds(["``` aa ```", "foo"]) == [PARAGRAPH.name]


def test_tilde_info_string_may_contain_a_backtick() -> None:
    assert kinds(["~~~ aa ```", "foo", "~~~"]) == [FENCED_CODE.name]


def test_fence_interrupts_a_paragraph() -> None:
    assert kinds(["foo", "```", "bar", "```"]) == [PARAGRAPH.name, FENCED_CODE.name]


def test_fence_without_blank_lines_around_it_is_its_own_block() -> None:
    assert kinds(["```", "a", "```", "b"]) == [FENCED_CODE.name, PARAGRAPH.name]


def test_text_directly_after_closing_fence_starts_a_paragraph() -> None:
    (fenced, paragraph) = parse_lines(["```", "a", "```", "b"]).children
    assert fenced.kind is FENCED_CODE
    assert paragraph.kind is PARAGRAPH


def test_two_fenced_blocks_in_a_row_are_separate() -> None:
    assert code_contents(["```", "a", "```", "```", "b", "```"]) == ["a\n", "b\n"]


# --- Block tree: info string and language ---


def test_language_is_the_first_word_of_the_info_string() -> None:
    assert fence_of(["```ruby extra words", "x", "```"]).language == "ruby"


def test_no_info_string_gives_no_language() -> None:
    assert fence_of(["```", "x", "```"]).language == ""


def test_info_string_of_only_spaces_gives_no_language() -> None:
    assert fence_of(["```   \t", "x", "```"]).language == ""


def test_leading_spaces_before_the_info_string_are_trimmed() -> None:
    assert fence_of(["```    python", "x", "```"]).language == "python"


def test_tilde_fence_info_string_gives_the_language() -> None:
    assert fence_of(["~~~ js", "x", "~~~"]).language == "js"


def test_backslash_escape_in_info_string_is_removed() -> None:
    assert fence_of(["```foo\\+bar", "x", "```"]).language == "foo+bar"


def test_entity_in_info_string_is_decoded() -> None:
    assert fence_of(["```&ouml;kl", "x", "```"]).language == "ökl"


def test_opening_fence_records_its_character_and_length() -> None:
    fence = fence_of(["~~~~ rust", "x", "~~~~"])
    assert (fence.char, fence.length) == ("~", 4)


def test_opening_fence_records_its_indentation() -> None:
    assert fence_of(["  ```", "x", "```"]).indent == 2


# --- Block tree: content ---


def test_content_lines_are_joined_with_line_endings() -> None:
    assert code_contents(["```", "a", "b", "```"]) == ["a\nb\n"]


def test_empty_fence_has_empty_content() -> None:
    assert code_contents(["```", "```"]) == [""]


def test_blank_lines_inside_the_fence_are_kept() -> None:
    assert code_contents(["```", "a", "", "b", "```"]) == ["a\n\nb\n"]


@pytest.mark.parametrize("indent", [0, 1, 2, 3])
def test_content_loses_up_to_the_opening_indentation(indent: int) -> None:
    assert code_contents([" " * indent + "```", "   aaa", "```"]) == [" " * (3 - indent) + "aaa\n"]


def test_content_less_indented_than_the_fence_keeps_its_text() -> None:
    assert code_contents(["   ```", "aaa", "```"]) == ["aaa\n"]


def test_content_indentation_beyond_the_fence_is_kept() -> None:
    assert code_contents(["```", "    indented", "```"]) == ["    indented\n"]


def test_content_is_not_parsed_as_markdown() -> None:
    assert code_contents(["```", "*hi* # head", "```"]) == ["*hi* # head\n"]


def test_content_fence_of_the_same_character_but_shorter_does_not_close() -> None:
    assert code_contents(["````", "aaa", "```", "````"]) == ["aaa\n```\n"]


def test_content_fence_with_an_info_string_does_not_close() -> None:
    assert code_contents(["```", "aaa", "``` aaa", "```"]) == ["aaa\n``` aaa\n"]


def test_content_fence_indented_four_columns_does_not_close() -> None:
    assert code_contents(["```", "aaa", "    ```"]) == ["aaa\n    ```\n"]


def test_unclosed_block_keeps_trailing_blank_lines() -> None:
    # The document "```\na\n\n" has three lines once its final line ending is dropped.
    assert code_contents(["```", "a", ""]) == ["a\n\n"]


def test_unclosed_block_keeps_a_fence_of_the_other_character_as_content() -> None:
    assert code_contents(["```", "~~~"]) == ["~~~\n"]


# --- Block tree: closing fence ---


@pytest.mark.parametrize("closing", ["```", "````", "``````"])
def test_closing_fence_at_least_as_long_closes_the_block(closing: str) -> None:
    assert code_contents(["```", "a", closing, "after"]) == ["a\n"]


@pytest.mark.parametrize("indent", [0, 1, 2, 3])
def test_closing_fence_indented_up_to_three_columns_closes(indent: int) -> None:
    assert code_contents(["```", "a", " " * indent + "```"]) == ["a\n"]


@pytest.mark.parametrize("trailer", ["  ", "\t", " \t "])
def test_closing_fence_followed_by_spaces_or_tabs_closes(trailer: str) -> None:
    assert code_contents(["```", "a", "```" + trailer]) == ["a\n"]


def test_closing_fence_may_not_carry_an_info_string() -> None:
    assert code_contents(["```", "a", "``` x", "```"]) == ["a\n``` x\n"]


def test_closing_fence_must_use_the_opening_character() -> None:
    assert code_contents(["~~~", "a", "```", "~~~"]) == ["a\n```\n"]


def test_closing_fence_adds_no_content_line() -> None:
    assert code_contents(["```", "a", "```"]) == ["a\n"]


def test_line_after_closing_fence_is_not_code() -> None:
    assert kinds(["```", "a", "```", "b"]) == [FENCED_CODE.name, PARAGRAPH.name]


def test_closing_fence_as_last_line_ends_the_document() -> None:
    assert kinds(["```", "a", "```"]) == [FENCED_CODE.name]


# --- Exact output through the executable ---


def test_exact_backtick_fence_output(project_root: Path) -> None:
    result = run_commonmark(project_root, "```\na\n```\n")
    assert result.returncode == 0
    assert result.stdout == "<pre><code>a\n</code></pre>\n"


def test_exact_tilde_fence_output(project_root: Path) -> None:
    result = run_commonmark(project_root, "~~~\na\n~~~\n")
    assert result.returncode == 0
    assert result.stdout == "<pre><code>a\n</code></pre>\n"


def test_exact_language_class_output(project_root: Path) -> None:
    result = run_commonmark(project_root, "```ruby\na\n```\n")
    assert result.stdout == '<pre><code class="language-ruby">a\n</code></pre>\n'


def test_exact_empty_fence_output(project_root: Path) -> None:
    result = run_commonmark(project_root, "```\n```\n")
    assert result.stdout == "<pre><code></code></pre>\n"


def test_exact_unclosed_fence_output(project_root: Path) -> None:
    result = run_commonmark(project_root, "```\na\n")
    assert result.stdout == "<pre><code>a\n</code></pre>\n"


def test_exact_unclosed_fence_keeps_trailing_blank_line(project_root: Path) -> None:
    result = run_commonmark(project_root, "```\na\n\n")
    assert result.stdout == "<pre><code>a\n\n</code></pre>\n"


def test_exact_content_is_escaped(project_root: Path) -> None:
    result = run_commonmark(project_root, "```\n<a>&amp;\"\n```\n")
    assert result.stdout == "<pre><code>&lt;a&gt;&amp;amp;&quot;\n</code></pre>\n"


def test_exact_language_class_is_escaped(project_root: Path) -> None:
    result = run_commonmark(project_root, "```a&quot;b\nx\n```\n")
    assert result.stdout == '<pre><code class="language-a&quot;b">x\n</code></pre>\n'


def test_exact_fence_interrupts_paragraph(project_root: Path) -> None:
    result = run_commonmark(project_root, "foo\n```\nbar\n```\nbaz\n")
    assert result.stdout == "<p>foo</p>\n<pre><code>bar\n</code></pre>\n<p>baz</p>\n"


def test_exact_indentation_stripped(project_root: Path) -> None:
    result = run_commonmark(project_root, "   ```\n   aaa\n    aaa\n  aaa\n   ```\n")
    assert result.stdout == "<pre><code>aaa\n aaa\naaa\n</code></pre>\n"


def test_exact_two_fenced_blocks(project_root: Path) -> None:
    result = run_commonmark(project_root, "```\na\n```\n~~~\nb\n~~~\n")
    assert result.stdout == "<pre><code>a\n</code></pre>\n<pre><code>b\n</code></pre>\n"


def test_exact_missing_final_newline_matches_with_one(project_root: Path) -> None:
    with_newline = run_commonmark(project_root, "```\na\n```\n")
    without_newline = run_commonmark(project_root, "```\na\n```")
    assert without_newline.stdout == with_newline.stdout
