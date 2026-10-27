from commonmark_parser import parse_blocks, render_html


def render(markdown: str) -> str:
    return render_html(parse_blocks(markdown))


def test_inline_link_with_title_and_emphasis():
    assert render('[a *link*](https://example.com "title")') == (
        '<p><a href="https://example.com" title="title">a <em>link</em></a></p>\n'
    )


def test_reference_full_collapsed_and_shortcut_forms():
    assert render('[one][x] [x][] [x]\n\n[x]: /target') == (
        '<p><a href="/target">one</a> <a href="/target">x</a> '
        '<a href="/target">x</a></p>\n'
    )


def test_link_destination_escapes_and_unicode_are_encoded():
    assert render(r'[x](</café>)') == '<p><a href="/caf%C3%A9">x</a></p>\n'


def test_links_do_not_accept_whitespace_before_destination_parenthesis():
    assert render('[x] (/target)') == '<p>[x] (/target)</p>\n'
