"""Code span tests: backtick matching by length, content normalization, literal unmatched runs,
inert backslashes and entities, and precedence against autolinks and raw HTML.

Each test compares a returned string or the executable's stdout bytes with its exact expected
value. No test matches a substring of output.
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


# --- Declared acceptance checks (transcribed from FEATURE-Code-Spans.md) ---


def test_codespans_corpus_sections_pass_in_full(project_root: Path) -> None:
    """AC codespans-corpus-sections: the scoped Code spans and Inlines sections exit 0."""
    result = subprocess.run(
        [
            sys.executable,
            "sources/spec_tests.py",
            "--program",
            str(project_root / "commonmark"),
            "--spec",
            "sources/spec.txt",
            "--pattern",
            "^Code spans$|^Inlines$",
        ],
        capture_output=True,
        cwd=project_root,
        check=False,
    )
    assert result.returncode == 0


def test_codespans_simple(project_root: Path) -> None:
    """AC codespans-simple: a single-backtick span renders one code element with its content."""
    result = run_executable(project_root, "`some code`\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p><code>some code</code></p>\n"


def test_codespans_backtick_length_match(project_root: Path) -> None:
    """AC codespans-backtick-length-match: a double-backtick span keeps a single backtick inside."""
    result = run_executable(project_root, "``a`b``\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p><code>a`b</code></p>\n"


def test_codespans_unclosed_literal(project_root: Path) -> None:
    """AC codespans-unclosed-literal: an unmatched backtick run is literal text, no code element."""
    result = run_executable(project_root, "```foo``\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>```foo``</p>\n"


def test_codespans_escapes_inert(project_root: Path) -> None:
    """AC codespans-escapes-inert: a backslash inside a code span is kept literally."""
    result = run_executable(project_root, "`\\[`\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p><code>\\[</code></p>\n"


# --- Opening and closing runs ---


def test_codespans_run_with_no_content_is_literal(project_root: Path) -> None:
    """Adjacent runs form one maximal run with no content, so no span can open or close on it."""
    assert inlines.parse_inline("````") == "````"


def test_codespans_longer_run_does_not_close_shorter(project_root: Path) -> None:
    """A run of three does not close a span opened by a run of one, so the span stays unmatched."""
    assert inlines.parse_inline("`a```") == "`a```"


def test_codespans_unclosed_run_consumes_whole_run(project_root: Path) -> None:
    """An unclosed run is literal as a whole and is not reread as a shorter opener."""
    assert inlines.parse_inline("``foo`") == "``foo`"


def test_codespans_unclosed_run_then_later_span(project_root: Path) -> None:
    """A literal run does not block a later code span of its own length."""
    assert inlines.parse_inline("`` x `y`") == "`` x <code>y</code>"


def test_codespans_adjacent_spans(project_root: Path) -> None:
    """Two spans separated by a space each render as their own code element."""
    assert inlines.parse_inline("`a` `b`") == "<code>a</code> <code>b</code>"


# --- Content normalization ---


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (" a ", "<code>a</code>"),
        ("  a  ", "<code> a </code>"),
        ("a ", "<code>a </code>"),
        (" a", "<code> a</code>"),
    ],
)
def test_codespans_strip_only_one_space_from_each_end(
    raw: str, expected: str
) -> None:
    """One space is removed from each end only when both ends are spaces."""
    assert inlines.parse_inline(f"`{raw}`") == expected


@pytest.mark.parametrize("raw", [" ", "   "])
def test_codespans_all_spaces_are_not_stripped(raw: str) -> None:
    """Content made entirely of spaces keeps every space."""
    assert inlines.parse_inline(f"`{raw}`") == f"<code>{raw}</code>"


def test_codespans_only_ascii_space_is_stripped(project_root: Path) -> None:
    """A tab at either end is not stripped."""
    assert inlines.parse_inline("`\ta\t`") == "<code>\ta\t</code>"


def test_codespans_line_ending_becomes_space(project_root: Path) -> None:
    """A line ending inside a span becomes a space, and interior spaces are not collapsed."""
    assert inlines.parse_inline("`a\nb  c`") == "<code>a b  c</code>"


def test_codespans_content_is_html_escaped(project_root: Path) -> None:
    """Angle brackets, ampersands and quotes in the content are escaped."""
    assert inlines.parse_inline('`<a href="&">`') == "<code>&lt;a href=&quot;&amp;&quot;&gt;</code>"


def test_codespans_entities_are_inert(project_root: Path) -> None:
    """An entity inside a span is shown as written, with its ampersand escaped."""
    assert inlines.parse_inline("`&amp;`") == "<code>&amp;amp;</code>"


def test_codespans_backslash_before_closing_run_is_content(project_root: Path) -> None:
    """A backslash just before the closing run stays in the content and does not escape it."""
    assert inlines.parse_inline("`foo\\`bar`") == "<code>foo\\</code>bar`"


def test_codespans_escaped_opener_is_literal(project_root: Path) -> None:
    """A backslash before a backtick makes that backtick literal and opens no span."""
    assert inlines.parse_inline("\\`foo`") == "`foo`"


# --- Precedence against autolinks and raw HTML ---


def test_codespans_backtick_first_beats_raw_html(project_root: Path) -> None:
    """When a span starts before a tag, the span takes the tag's characters as content."""
    assert inlines.parse_inline("`<a>`") == "<code>&lt;a&gt;</code>"


def test_codespans_raw_html_first_beats_backtick(project_root: Path) -> None:
    """A tag that starts before a backtick is taken whole, even when it holds a backtick."""
    assert inlines.parse_inline('<a t="`">`') == '<a t="`">`'


def test_codespans_backtick_first_beats_autolink(project_root: Path) -> None:
    """A span that starts before an autolink keeps the autolink's text as code content."""
    assert inlines.parse_inline("`<http://a.b>`") == "<code>&lt;http://a.b&gt;</code>"


def test_codespans_autolink_first_beats_backtick(project_root: Path) -> None:
    """An autolink that starts before a backtick is taken whole, and the backtick is literal."""
    assert inlines.parse_inline("<http://a.b`>`") == '<a href="http://a.b%60">http://a.b`</a>`'


def test_codespans_backtick_inside_raw_html_attribute_is_not_an_opener(
    project_root: Path,
) -> None:
    """A backtick inside a raw HTML tag is part of the tag, so no span opens there."""
    assert inlines.parse_inline('<a href="`">x`') == '<a href="`">x`'


# --- Executable boundary ---


def test_codespans_whole_document_stdout(project_root: Path) -> None:
    """A paragraph with a span renders as one paragraph element on stdout."""
    result = run_executable(project_root, "Use `x` here\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>Use <code>x</code> here</p>\n"
