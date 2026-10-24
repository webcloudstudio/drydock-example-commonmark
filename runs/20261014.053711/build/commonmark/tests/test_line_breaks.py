"""Line break and text tests: hard breaks, soft breaks, and plain text, in the inline parser and the
executable, and the corpus sections that the line-breaks-text story gates.

The declared acceptance checks are transcribed from FEATURE-Line-Breaks-Text.md with their assertions
kept as written. The remaining tests compare the returned HTML string, or the executable's stdout,
with its exact expected value.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from mdparser import inlines


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


def parse(source: str) -> str:
    return inlines.parse_inline(source)


# --- Declared acceptance checks (transcribed from FEATURE-Line-Breaks-Text.md) ---


def test_breaks_corpus_sections(project_root: Path) -> None:
    """AC breaks-corpus-sections: the Soft line breaks and Textual content sections pass in full."""
    result = subprocess.run(
        [
            sys.executable,
            "sources/spec_tests.py",
            "--program",
            str(project_root / "commonmark"),
            "--spec",
            "sources/spec.txt",
            "--pattern",
            "^Soft line breaks$|^Textual content$",
        ],
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0


def test_breaks_hard_break_spaces(project_root: Path) -> None:
    """AC breaks-hard-break-spaces: two or more trailing spaces before a line ending give one br element between the two lines."""
    first = "alpha"
    second = "beta"
    result = run_executable(project_root, first + "   \n" + second + "\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<br />") == 1
    assert first in stdout
    assert second in stdout


def test_breaks_hard_break_backslash(project_root: Path) -> None:
    """AC breaks-hard-break-backslash: a backslash before a line ending gives one br element."""
    result = run_executable(project_root, "alpha\\\nbeta\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<br />") == 1


def test_breaks_soft_break(project_root: Path) -> None:
    """AC breaks-soft-break: a plain line ending is not a hard break and both lines stay in one paragraph."""
    result = run_executable(project_root, "alpha\nbeta\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<br />") == 0
    assert stdout.count("<p>") == 1


def test_breaks_none_at_block_end(project_root: Path) -> None:
    """AC breaks-none-at-block-end: trailing spaces or a trailing backslash at the end of a paragraph do not create a break."""
    for source in ("alpha  \n", "alpha\\\n"):
        result = run_executable(project_root, source)
        stdout = result.stdout.decode("utf-8")
        print(stdout)
        assert result.returncode == 0
        assert stdout.count("<br />") == 0


def test_breaks_inert_in_code_span(project_root: Path) -> None:
    """AC breaks-inert-in-code-span: trailing spaces before a line ending inside a code span do not create a break."""
    result = run_executable(project_root, "`code  \nspan`\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<br />") == 0
    assert stdout.count("<code>") == 1


# --- Hard line breaks ---


@pytest.mark.parametrize("spaces", ["  ", "   ", "     "])
def test_hard_break_from_two_or_more_spaces(spaces: str) -> None:
    assert parse("alpha" + spaces + "\nbeta") == "alpha<br />\nbeta"


def test_hard_break_from_backslash() -> None:
    assert parse("alpha\\\nbeta") == "alpha<br />\nbeta"


def test_hard_break_drops_leading_spaces_on_next_line_in_executable(project_root: Path) -> None:
    result = run_executable(project_root, "alpha  \n   beta\n")
    assert result.returncode == 0
    assert result.stdout == b"<p>alpha<br />\nbeta</p>\n"


def test_hard_break_backslash_in_executable(project_root: Path) -> None:
    result = run_executable(project_root, "alpha\\\nbeta\n")
    assert result.returncode == 0
    assert result.stdout == b"<p>alpha<br />\nbeta</p>\n"


def test_two_hard_breaks_in_one_paragraph() -> None:
    assert parse("a  \nb  \nc") == "a<br />\nb<br />\nc"


def test_hard_break_and_backslash_mixed() -> None:
    assert parse("a\\\nb  \nc") == "a<br />\nb<br />\nc"


def test_hard_break_inside_emphasis() -> None:
    assert parse("*foo  \nbar*") == "<em>foo<br />\nbar</em>"


def test_hard_break_inside_link_text() -> None:
    assert parse("[foo  \nbar](/u)") == '<a href="/u">foo<br />\nbar</a>'


def test_hard_break_in_image_alt_is_a_line_ending() -> None:
    assert parse("![foo  \nbar](/u)") == '<img src="/u" alt="foo\nbar" />'


def test_hard_break_is_not_taken_inside_raw_html_tag() -> None:
    assert parse('a <span class="x"  \n>b') == 'a <span class="x"  \n>b'


# --- Soft line breaks ---


def test_soft_break_is_a_line_ending() -> None:
    assert parse("alpha\nbeta") == "alpha\nbeta"


def test_soft_break_drops_single_trailing_space() -> None:
    assert parse("alpha \nbeta") == "alpha\nbeta"


def test_soft_break_drops_trailing_space_and_leading_spaces() -> None:
    assert parse("alpha \n   beta") == "alpha\nbeta"


def test_soft_breaks_across_several_lines() -> None:
    assert parse("a\nb\nc") == "a\nb\nc"


def test_soft_break_inside_emphasis() -> None:
    assert parse("*foo\nbar*") == "<em>foo\nbar</em>"


def test_executable_soft_break_keeps_one_paragraph(project_root: Path) -> None:
    result = run_executable(project_root, "alpha\nbeta\n")
    assert result.returncode == 0
    assert result.stdout == b"<p>alpha\nbeta</p>\n"


# --- Breaks at the end of a block ---


def test_executable_trailing_spaces_at_paragraph_end_are_dropped(project_root: Path) -> None:
    result = run_executable(project_root, "alpha   ")
    assert result.returncode == 0
    assert result.stdout == b"<p>alpha</p>\n"


def test_trailing_backslash_at_paragraph_end_stays_literal() -> None:
    assert parse("alpha\\") == "alpha\\"


def test_executable_trailing_backslash_stays_literal(project_root: Path) -> None:
    result = run_executable(project_root, "alpha\\\n")
    assert result.returncode == 0
    assert result.stdout == b"<p>alpha\\</p>\n"


def test_executable_trailing_spaces_make_no_break(project_root: Path) -> None:
    result = run_executable(project_root, "alpha  \n")
    assert result.returncode == 0
    assert result.stdout == b"<p>alpha</p>\n"


# --- Inert contexts ---


def test_break_inert_in_code_span_becomes_spaces() -> None:
    assert parse("`code  \nspan`") == "<code>code   span</code>"


def test_break_inert_in_code_span_with_backslash() -> None:
    assert parse("`code\\\nspan`") == "<code>code\\ span</code>"


# --- Plain text ---


def test_plain_text_is_unchanged() -> None:
    assert parse("hello") == "hello"


def test_internal_spaces_are_kept_verbatim() -> None:
    assert parse("a   b") == "a   b"


def test_internal_spaces_before_a_word_are_kept_before_a_hard_break() -> None:
    assert parse("a   b  \nc") == "a   b<br />\nc"


def test_single_space_in_text_is_kept() -> None:
    assert parse("a b") == "a b"


def test_escaped_text_is_escaped() -> None:
    assert parse("a < b & c") == "a &lt; b &amp; c"


def test_empty_text_renders_nothing() -> None:
    assert parse("") == ""


def test_executable_plain_paragraph(project_root: Path) -> None:
    result = run_executable(project_root, "hello world\n")
    assert result.returncode == 0
    assert result.stdout == b"<p>hello world</p>\n"
