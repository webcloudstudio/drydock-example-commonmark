import commonmark_parser


def test_render_paragraph_and_heading_html():
    assert commonmark_parser.render("# title\n\ntext\n") == "<h1>title</h1>\n<p>text</p>\n"


def test_render_resolves_forward_reference_links():
    source = "[label]\n\n[label]: /target\n"
    assert commonmark_parser.render(source) == '<p><a href="/target">label</a></p>\n'


def test_render_code_and_raw_html_blocks():
    source = "```\n<a>&\n```\n\n<!-- raw -->\n"
    assert commonmark_parser.render(source) == "<pre><code>&lt;a&gt;&amp;\n</code></pre>\n<!-- raw -->\n"


def test_html_block_tag_name_can_end_at_line_boundary():
    assert commonmark_parser.render("<div\n> text\n") == "<div\n> text\n"


def test_tight_list_inside_quote_keeps_paragraphs_unwrapped():
    assert commonmark_parser.render("> - foo\n") == (
        "<blockquote>\n<ul>\n<li>foo\n</li>\n</ul>\n</blockquote>\n"
    )


def test_uri_autolink_is_rendered_as_anchor():
    assert commonmark_parser.render("<https://example.com>\n") == (
        '<p><a href="https://example.com">https://example.com</a></p>\n'
    )


def test_uri_autolink_keeps_escaped_punctuation_inside_destination():
    assert commonmark_parser.render("<https://example.com?find=\\*>\n") == (
        '<p><a href="https://example.com?find=%5C*">https://example.com?find=\\*</a></p>\n'
    )


def test_code_span_newlines_are_not_split_as_hard_breaks():
    source = "``\nfoo\nbar  \nbaz\n``"
    assert commonmark_parser.render(source) == "<p><code>foo bar baz</code></p>\n"


def test_link_destination_is_percent_encoded_after_entity_decoding():
    source = "[foo](/f&ouml;)"
    assert commonmark_parser.render(source) == '<p><a href="/f%C3%B6">foo</a></p>\n'


def test_tight_list_suppresses_only_direct_item_paragraph_tags():
    source = "- > quoted\n"
    assert commonmark_parser.render(source) == (
        "<ul>\n<li><blockquote>\n<p>quoted</p>\n</blockquote>\n</li>\n</ul>\n"
    )


def test_blank_line_before_nested_list_makes_parent_list_loose():
    source = "1. foo\n\n    - bar\n"
    assert commonmark_parser.render(source) == (
        "<ol>\n<li><p>foo</p>\n<ul>\n<li>bar\n</li>\n</ul>\n</li>\n</ol>\n"
    )


def test_blank_line_before_nested_list_with_two_space_ordered_marker_makes_parent_loose():
    source = "1.  foo\n\n    - bar\n"
    assert commonmark_parser.render(source) == (
        "<ol>\n<li><p>foo</p>\n<ul>\n<li>bar\n</li>\n</ul>\n</li>\n</ol>\n"
    )


def test_entity_decoded_delimiters_stay_literal():
    assert commonmark_parser.render("&#42;foo&#42;\n") == "<p>*foo*</p>\n"
from commonmark_parser import render


def test_escaped_punctuation_and_angle_bracket_remain_literal():
    assert render("\\*not emphasized*\n\\<br/> not a tag") == (
        "<p>*not emphasized*\n&lt;br/&gt; not a tag</p>\n"
    )
