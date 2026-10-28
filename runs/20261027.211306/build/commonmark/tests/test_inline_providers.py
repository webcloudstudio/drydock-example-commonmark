from commonmark_parser.autolinks import parse_autolinks
from commonmark_parser.inline_html_breaks import parse_inline_html_breaks
from commonmark_parser.inlines import parse_inlines


def test_emphasis_and_strong_nodes():
    nodes = parse_inlines("*alpha* **beta**", {})
    assert [(n.type, n.children[0].literal if n.children else n.literal) for n in nodes] == [
        ("em", "alpha"), ("text", " "), ("strong", "beta")]


def test_underscore_within_word_stays_literal():
    source = "alpha_beta_gamma"
    nodes = parse_inlines(source, {})
    assert all(n.type == "text" for n in nodes)
    assert "".join(n.literal for n in nodes) == source


def test_currency_symbol_flanking_does_not_create_emphasis():
    from commonmark_parser import render

    assert render("*$*alpha.\n\n*£*bravo.\n") == (
        "<p>*$*alpha.</p>\n<p>*£*bravo.</p>\n"
    )


def test_autolinks_uri_email_and_invalid_uri():
    uri = "https://example.test/path"
    nodes = parse_autolinks(f"<{uri}>")
    assert [(n.type, n.destination, n.label) for n in nodes] == [("link", uri, uri)]
    nodes = parse_autolinks("<person@example.test>")
    assert [(n.type, n.destination, n.label) for n in nodes] == [("link", "mailto:person@example.test", "person@example.test")]
    source = "<https://example.test/a b>"
    nodes = parse_autolinks(source)
    assert all(n.type == "text" for n in nodes)
    assert "".join(n.literal for n in nodes) == source


def test_autolink_syntax_inside_code_span_stays_code():
    from commonmark_parser import render

    source = "`<https://foo.bar.`baz>`"
    assert render(source) == "<p><code>&lt;https://foo.bar.</code>baz&gt;`</p>\n"


def test_inline_html_preserves_tag():
    tag = '<custom data-value="sample">'
    nodes = parse_inline_html_breaks(tag)
    assert [(n.type, n.literal) for n in nodes] == [("html", tag)]


def test_hard_breaks_for_spaces_and_backslash():
    for source in ("first  \nsecond", "first\\\nsecond"):
        nodes = parse_inline_html_breaks(source)
        assert sum(n.type == "hardbreak" for n in nodes) == 1
    source = "ending\\"
    nodes = parse_inline_html_breaks(source)
    assert all(n.type != "hardbreak" for n in nodes)
    assert "".join(n.literal for n in nodes if n.type == "text") == source


def test_invalid_html_remains_text():
    source = "<1not>"
    nodes = parse_inline_html_breaks(source)
    assert [(n.type, n.literal) for n in nodes] == [("text", source)]
