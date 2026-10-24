"""Block-engine acceptance and end-to-end tests: paragraphs, blank lines, and HTML escaping through
the `commonmark` executable.

The four declared checks from FEATURE-Block-Engine.md are transcribed first, with their
assertions unchanged. The remaining tests compare the exact stdout bytes, which is the state
the executable hands back.
"""

import subprocess
from pathlib import Path


def run_commonmark(project_root: Path, source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )


# --- Declared acceptance checks (transcribed from FEATURE-Block-Engine.md) ---


def test_engine_paragraph_count(project_root: Path) -> None:
    """Blank-line-separated paragraphs render as one p element each."""
    paragraphs = ["alpha beta", "gamma delta", "epsilon"]
    source = "\n\n".join(paragraphs) + "\n"
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == len(paragraphs)
    assert result.stdout.count("</p>") == len(paragraphs)
    for text in paragraphs:
        assert text in result.stdout


def test_engine_multiline_paragraph(project_root: Path) -> None:
    """Consecutive non-blank lines with arbitrary indentation after the first stay in one paragraph."""
    first = "first line"
    second = "second line"
    third = "third line"
    source = first + "\n" + "             " + second + "\n" + third + "\n"
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1
    for text in (first, second, third):
        assert text in result.stdout


def test_engine_blank_lines_ignored(project_root: Path) -> None:
    """Leading, trailing and repeated blank lines add no blocks; a blank-only document gives no paragraph."""
    word = "content"
    padded = "\n  \n\n" + word + "\n\n\n  \n"
    result = run_commonmark(project_root, padded)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1

    blank = run_commonmark(project_root, "\n \n\t\n")
    assert blank.returncode == 0
    assert blank.stdout.count("<p>") == 0


def test_engine_html_escaping(project_root: Path) -> None:
    """Special characters in paragraph text are escaped, so only the paragraph tags contribute angle brackets."""
    result = run_commonmark(project_root, "x < y > z & w\n")
    assert result.returncode == 0
    assert result.stdout.count("<") == 2
    assert result.stdout.count(">") == 2


# --- Exact output through the executable ---


def test_single_paragraph_output_is_exact(project_root: Path) -> None:
    assert run_commonmark(project_root, "hello world\n").stdout == "<p>hello world</p>\n"


def test_two_paragraphs_output_is_exact(project_root: Path) -> None:
    result = run_commonmark(project_root, "one\n\ntwo\n")
    assert result.stdout == "<p>one</p>\n<p>two</p>\n"


def test_multiline_paragraph_output_is_exact(project_root: Path) -> None:
    source = "first line\n             second line\nthird line\n"
    result = run_commonmark(project_root, source)
    assert result.stdout == "<p>first line\nsecond line\nthird line</p>\n"


def test_escaped_paragraph_output_is_exact(project_root: Path) -> None:
    result = run_commonmark(project_root, "x < y > z & w\n")
    assert result.stdout == "<p>x &lt; y &gt; z &amp; w</p>\n"


def test_padded_document_output_is_exact(project_root: Path) -> None:
    result = run_commonmark(project_root, "\n  \n\ncontent\n\n\n  \n")
    assert result.stdout == "<p>content</p>\n"


def test_blank_only_document_output_is_empty(project_root: Path) -> None:
    assert run_commonmark(project_root, "\n \n\t\n").stdout == ""


def test_paragraph_leading_and_trailing_whitespace_is_removed(project_root: Path) -> None:
    result = run_commonmark(project_root, "  word \t  \n")
    assert result.stdout == "<p>word</p>\n"


def test_crlf_document_renders_the_same_as_lf(project_root: Path) -> None:
    lf = run_commonmark(project_root, "one\ntwo\n\nthree\n")
    crlf = run_commonmark(project_root, "one\r\ntwo\r\n\r\nthree\r\n")
    assert lf.stdout == crlf.stdout == "<p>one\ntwo</p>\n<p>three</p>\n"
