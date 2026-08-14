"""Focused conformance tests for inline escapes and character references."""

import subprocess


def render(markdown: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["./cmark"], input=markdown, text=True, encoding="utf-8",
        capture_output=True, check=False,
    )


def test_punctuation_escapes_are_literal() -> None:
    result = render(r"\*not emphasized* \[not a link](/url) \&ouml;")
    assert result.returncode == 0
    assert result.stdout == "<p>*not emphasized* [not a link](/url) &amp;ouml;</p>\n"


def test_references_decode_only_in_normal_inline_text() -> None:
    result = render("&copy; &#35; &#X22; &#0; `&copy;`\n")
    assert result.returncode == 0
    assert result.stdout == '<p>© # &quot; � <code>&amp;copy;</code></p>\n'


def test_fenced_info_string_decodes_references_and_escapes() -> None:
    result = render(r'''``` f&ouml;\+bar
text
```
''')
    assert result.returncode == 0
    assert result.stdout == '<pre><code class="language-fö+bar">text\n</code></pre>\n'
