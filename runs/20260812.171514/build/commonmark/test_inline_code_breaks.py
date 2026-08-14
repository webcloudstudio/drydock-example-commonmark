"""Regression tests for inline code spans and line-break rendering."""

import subprocess


def render(markdown: str) -> str:
    result = subprocess.run(
        ["./program"], input=markdown, text=True, capture_output=True, check=True
    )
    return result.stdout


def test_code_span_delimiters_and_normalization() -> None:
    assert render("`  ``  `\n") == "<p><code> `` </code></p>\n"
    assert render("``foo ` bar``\n") == "<p><code>foo ` bar</code></p>\n"
    assert render("`foo\\`bar`\n") == "<p><code>foo\\</code>bar`</p>\n"


def test_code_span_precedes_emphasis_and_links() -> None:
    assert render("*foo`*`\n") == "<p>*foo<code>*</code></p>\n"
    assert render("[not a `link](/foo`)\n") == "<p>[not a <code>link](/foo</code>)</p>\n"


def test_hard_break_strips_following_indentation() -> None:
    assert render("foo  \n     bar\n") == "<p>foo<br />\nbar</p>\n"
    assert render("foo\\\n     bar\n") == "<p>foo<br />\nbar</p>\n"


def test_html_tags_do_not_turn_attribute_newlines_into_breaks() -> None:
    assert render('<a href="foo  \nbar">\n') == '<p><a href="foo  \nbar"></p>\n'
