"""Deterministic list parsing checks at the cmark process boundary."""

import subprocess


def render(markdown: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["./cmark"], input=markdown, text=True, capture_output=True, check=False
    )


def test_nested_list_and_ordered_start() -> None:
    result = render("10) outer\n    - inner\n")

    assert result.returncode == 0
    assert result.stdout == (
        '<ol start="10">\n<li>\nouter\n<ul>\n<li>inner</li>\n</ul>\n</li>\n</ol>\n'
    )


def test_blank_item_and_loose_list() -> None:
    result = render("- first\n\n-\n\n- third\n")

    assert result.returncode == 0
    assert result.stdout == (
        "<ul>\n<li><p>first</p></li>\n<li></li>\n"
        "<li><p>third</p></li>\n</ul>\n"
    )
