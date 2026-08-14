"""Focused regression checks for block-to-HTML rendering."""

import subprocess


def render(markdown: str) -> str:
    result = subprocess.run(
        ["./cmark"], input=markdown, text=True, capture_output=True, check=False
    )
    assert result.returncode == 0
    return result.stdout


def test_headings_breaks_and_code_are_rendered_as_blocks() -> None:
    assert render("# Title\n\n---\n\n    <tag>\n") == (
        "<h1>Title</h1>\n<hr />\n<pre><code>&lt;tag&gt;\n</code></pre>\n"
    )


def test_raw_html_and_nested_loose_list_rendering() -> None:
    assert render("<div>\n*literal*\n</div>\n\n- one\n\n  - two\n") == (
        "<div>\n*literal*\n</div>\n<ul>\n<li>\n<p>one</p>\n<ul>\n<li>two</li>\n</ul>\n</li>\n</ul>\n"
    )
