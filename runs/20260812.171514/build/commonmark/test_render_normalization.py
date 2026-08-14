import subprocess


def render(markdown: str) -> str:
    result = subprocess.run(
        ["./commonmark"], input=markdown, text=True, capture_output=True, check=True
    )
    return result.stdout


def test_urls_titles_and_entities_are_escaped_deterministically() -> None:
    assert render('[x](/f&ouml;&ouml; "a &quot;title&quot;")\n') == (
        '<p><a href="/f%C3%B6%C3%B6" title="a &quot;title&quot;">x</a></p>\n'
    )


def test_inline_html_attributes_preserve_raw_attribute_semantics() -> None:
    assert render('before <a href="/a?x=1&amp;y=2" title="a &quot;b&quot;">x</a>\n') == (
        '<p>before <a href="/a?x=1&amp;y=2" title="a &quot;b&quot;">x</a></p>\n'
    )


def test_special_characters_are_html_escaped_in_text() -> None:
    assert render('<&> "quotes"\n') == '<p>&lt;&amp;&gt; &quot;quotes&quot;</p>\n'
