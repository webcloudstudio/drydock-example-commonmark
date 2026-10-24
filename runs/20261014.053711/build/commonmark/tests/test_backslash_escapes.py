"""Backslash escape tests: escaped ASCII punctuation in text, literal backslashes before other
characters, inertness inside code spans, and the shared `unescape` helper used for link
destinations, titles and info strings.

Each test compares a returned string or the executable's stdout bytes with its exact expected
value. The declared acceptance checks are transcribed from FEATURE-Backslash-Escapes.md.
"""

import string
import subprocess
from pathlib import Path

import pytest

from mdparser import inlines
from mdparser.entities import ASCII_PUNCTUATION, unescape


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


# --- Declared acceptance checks (transcribed from FEATURE-Backslash-Escapes.md) ---


def test_escapes_punctuation_inert(project_root: Path) -> None:
    """AC escapes-punctuation-inert: an escaped asterisk prevents emphasis."""
    result = run_executable(project_root, "\\*not emphasized*\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8").count("<em>") == 0
    assert result.stdout.decode("utf-8").count("\\") == 0


def test_escapes_non_punctuation_literal(project_root: Path) -> None:
    """AC escapes-non-punctuation-literal: a backslash before a non-punctuation character is kept."""
    text = "\\A\\a\\3"
    result = run_executable(project_root, text + "\n")
    assert result.returncode == 0
    assert text in result.stdout.decode("utf-8")


def test_escapes_block_markers(project_root: Path) -> None:
    """AC escapes-block-markers: an escaped heading marker does not start a heading."""
    result = run_executable(project_root, "\\# word\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8").count("<h1>") == 0
    assert result.stdout.decode("utf-8").count("<p>") == 1


def test_escapes_inert_in_code_span(project_root: Path) -> None:
    """AC escapes-inert-in-code-span: a backslash in a code span is not an escape."""
    content = "\\*"
    result = run_executable(project_root, "`" + content + "`\n")
    assert result.returncode == 0
    assert content in result.stdout.decode("utf-8")


# --- Escaped punctuation in text ---


HTML_TEXT_FORM = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}


@pytest.mark.parametrize("char", sorted(string.punctuation))
def test_escaped_punctuation_yields_the_character(char: str) -> None:
    """Every ASCII punctuation character escaped by a backslash is plain text, without the backslash."""
    assert inlines.parse_inline("\\" + char) == HTML_TEXT_FORM.get(char, char)


def test_ascii_punctuation_set_matches_the_spec_list() -> None:
    """The escapable set is exactly the 32 ASCII punctuation characters."""
    assert len(ASCII_PUNCTUATION) == 32
    assert "\\" in ASCII_PUNCTUATION
    assert " " not in ASCII_PUNCTUATION
    assert "A" not in ASCII_PUNCTUATION


@pytest.mark.parametrize("char", ["*", "_", "`", "[", "]", "<", "&", "#", "!", "|"])
def test_escaped_character_that_opens_a_construct_is_inert(char: str) -> None:
    """A backslash makes a construct-opening character literal, so no construct starts there."""
    assert "\\" not in inlines.parse_inline("\\" + char + "x" + char)


def test_escaped_backslash_leaves_next_character_unescaped() -> None:
    """`\\\\` yields one backslash, and the following backtick is still a live opener."""
    assert inlines.parse_inline("\\\\`a`") == "\\<code>a</code>"


def test_escaped_backtick_does_not_open_a_code_span() -> None:
    """A backslash before a backtick makes it literal, so it cannot open a span."""
    assert inlines.parse_inline("\\`a`") == "`a`"


def test_escaped_ampersand_is_escaped_as_text() -> None:
    """An escaped ampersand is shown as a literal ampersand, so an entity-like form is not decoded."""
    assert inlines.parse_inline("\\&amp;") == "&amp;amp;"


def test_escaped_quote_renders_as_quot_entity() -> None:
    """An escaped double quote renders as the `&quot;` entity, with no backslash."""
    assert inlines.parse_inline('\\"') == "&quot;"


def test_trailing_lone_backslash_is_literal() -> None:
    """A backslash at the very end of the text is kept, since nothing follows it."""
    assert inlines.parse_inline("a\\") == "a\\"


def test_backslash_before_non_punctuation_is_kept() -> None:
    """A backslash before a letter, digit or space stays in the text."""
    assert inlines.parse_inline("\\a\\3\\ b") == "\\a\\3\\ b"


def test_escape_inside_a_longer_text_run() -> None:
    """An escape in the middle of plain text consumes only its own two characters."""
    assert inlines.parse_inline("x\\*y*z") == "x*y*z"


def test_escaped_text_output_is_exact(project_root: Path) -> None:
    """The executable writes exactly the escaped paragraph and nothing else."""
    result = run_executable(project_root, "\\*a\\* b\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>*a* b</p>\n"


# --- The shared unescape helper ---


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("plain", "plain"),
        ("\\*", "*"),
        ("\\\\", "\\"),
        ("\\a", "\\a"),
        ("a\\", "a\\"),
        ("\\\\*", "\\*"),
        ("\\*\\_", "*_"),
        ("a\\(b\\)", "a(b)"),
        ("\\ \\\n", "\\ \\\n"),
    ],
)
def test_unescape_applies_the_backslash_rule(text: str, expected: str) -> None:
    """The helper yields escaped punctuation and keeps every other backslash."""
    assert unescape(text) == expected


def test_unescape_leaves_entities_undecoded() -> None:
    """Entity decoding is separate, so `&amp;` passes through the helper as written."""
    assert unescape("\\&amp;") == "&amp;"


def test_unescape_is_idempotent_after_one_pass() -> None:
    """A second pass over an unescaped result changes nothing when no backslash is left."""
    once = unescape("\\*a\\_b")
    assert once == "*a_b"
    assert unescape(once) == once


def test_unescape_empty_string_is_empty() -> None:
    """The empty string has no escapes and stays empty."""
    assert unescape("") == ""
