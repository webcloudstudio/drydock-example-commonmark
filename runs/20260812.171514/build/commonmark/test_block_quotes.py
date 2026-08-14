"""Focused block-quote behavior at the cmark process boundary."""

import subprocess


def render(markdown: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["./cmark"], input=markdown, text=True, capture_output=True, check=False
    )


def test_nested_quote_and_lazy_continuation() -> None:
    result = render("> > title\ncontinued\n")

    assert result.returncode == 0
    assert result.stdout == "<blockquote>\n<blockquote>\n<p>title\ncontinued</p>\n</blockquote>\n</blockquote>\n"


def test_blank_line_separates_block_quotes() -> None:
    result = render("> first\n\n> second\n")

    assert result.returncode == 0
    assert result.stdout == "<blockquote>\n<p>first</p>\n</blockquote>\n<blockquote>\n<p>second</p>\n</blockquote>\n"


def test_unmarked_code_line_does_not_continue_quoted_code() -> None:
    result = render(">     code\n    outside\n")

    assert result.returncode == 0
    assert result.stdout == "<blockquote>\n<pre><code>code\n</code></pre>\n</blockquote>\n<pre><code>outside\n</code></pre>\n"


def test_unmarked_line_does_not_continue_quoted_fence() -> None:
    result = render("> ```\nfoo\n```\n")

    assert result.returncode == 0
    assert result.stdout == "<blockquote>\n<pre><code></code></pre>\n</blockquote>\n<p>foo</p>\n<pre><code></code></pre>\n"
