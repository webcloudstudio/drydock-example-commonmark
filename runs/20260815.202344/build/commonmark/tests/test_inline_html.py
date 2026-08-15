import subprocess
from pathlib import Path


ROOT = Path(__file__).parents[1]


def render(source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(ROOT / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_uri_and_email_autolinks_render_as_links():
    result = render("<https://example.com?q=1&x=2>\n<foo+special@Bar.example>\n")
    assert result.returncode == 0
    assert result.stdout == (
        '<p><a href="https://example.com?q=1&amp;x=2">'
        "https://example.com?q=1&amp;x=2</a>\n"
        '<a href="mailto:foo+special@Bar.example">'
        "foo+special@Bar.example</a></p>\n"
    )


def test_invalid_autolinks_remain_escaped_text():
    result = render("<foo.bar.baz>\n<foo\\+@bar.example>\n")
    assert result.returncode == 0
    assert result.stdout == (
        "<p>&lt;foo.bar.baz&gt;\n"
        "&lt;foo+@bar.example&gt;</p>\n"
    )


def test_valid_raw_html_is_preserved_but_malformed_tags_are_escaped():
    result = render('before <responsive-image src="foo.jpg" /> after\n<a h*#ref="hi">\n')
    assert result.returncode == 0
    assert result.stdout == (
        '<p>before <responsive-image src="foo.jpg" /> after\n'
        "&lt;a h*#ref=&quot;hi&quot;&gt;</p>\n"
    )
