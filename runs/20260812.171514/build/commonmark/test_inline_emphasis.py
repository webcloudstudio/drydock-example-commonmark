"""Regression tests for delimiter-run emphasis parsing."""

import subprocess


def render(markdown: str) -> str:
    result = subprocess.run(
        ["./program"], input=markdown, text=True, capture_output=True, check=True
    )
    return result.stdout


def test_nested_emphasis_and_strong_emphasis() -> None:
    assert render("*foo **bar** baz*\n") == "<p><em>foo <strong>bar</strong> baz</em></p>\n"
    assert render("**foo *bar* baz**\n") == "<p><strong>foo <em>bar</em> baz</strong></p>\n"


def test_intraword_rules_and_modulo_three() -> None:
    assert render("foo*bar* and foo_bar_\n") == "<p>foo<em>bar</em> and foo_bar_</p>\n"
    assert render("*foo**bar**baz*\n") == "<p><em>foo<strong>bar</strong>baz</em></p>\n"


def test_overlapping_spans_use_the_first_opener() -> None:
    assert render("*foo _bar* baz_\n") == "<p><em>foo _bar</em> baz_</p>\n"
