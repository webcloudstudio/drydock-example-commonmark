from commonmark_parser.blocks import parse_blocks


def test_marked_paragraph_accepts_lazy_continuation():
    document = parse_blocks("> alpha\ncontinuation\n")
    assert len(document.children) == 1
    quote = document.children[0]
    assert quote.type == "block_quote"
    assert len(quote.children) == 1
    paragraph = quote.children[0]
    assert paragraph.type == "paragraph"
    assert paragraph.literal.splitlines() == ["alpha", "continuation"]


def test_nested_quote_and_unmarked_blank_close():
    document = parse_blocks("> > inside\n\noutside\n")
    assert len(document.children) == 2
    outer, paragraph = document.children
    assert outer.type == "block_quote"
    assert len(outer.children) == 1
    inner = outer.children[0]
    assert inner.type == "block_quote"
    assert inner.children[0].literal == "inside"
    assert paragraph.type == "paragraph"
    assert paragraph.literal == "outside"


def test_explicit_blank_line_remains_in_quote_and_splits_paragraphs():
    quote = parse_blocks("> alpha\n>\n> beta\n").children[0]
    assert quote.type == "block_quote"
    assert [child.literal for child in quote.children] == ["alpha", "beta"]


def test_quote_marker_allows_three_spaces_and_consumes_one_following_space():
    quote = parse_blocks("   >  alpha\n").children[0]
    assert quote.children[0].literal == "alpha"


def test_tab_after_quote_marker_preserves_indented_code_columns():
    html = __import__("commonmark_parser").render(">\t\tfoo\n")
    assert html == "<blockquote>\n<pre><code>  foo\n</code></pre>\n</blockquote>\n"


def test_reference_definition_inside_quote_updates_document_map():
    document = parse_blocks("> [label]: /target\n>\n> visible\n")
    assert document.references == {"label": ("/target", None)}
    assert document.children[0].children[0].literal == "visible"


def test_lazy_quote_setext_like_outer_line_stays_paragraph_text():
    rendered = __import__("commonmark_parser").render("> foo\nbar\n===\n")
    assert rendered == "<blockquote>\n<p>foo\nbar\n===</p>\n</blockquote>\n"


def test_fenced_code_line_does_not_allow_lazy_quote_continuation():
    rendered = __import__("commonmark_parser").render("> ```\nfoo\n```\n")
    assert rendered == "<blockquote>\n<pre><code></code></pre>\n</blockquote>\n<p>foo</p>\n<pre><code></code></pre>\n"
