from commonmark_parser import parse_blocks, render_html
from commonmark_parser.lists import parse_list_marker


def test_ordered_marker_reports_start_and_content_indent():
    result = parse_list_marker("7.  item\n")
    assert result == {"kind": "ordered", "marker": "7.", "start": 7, "content_indent": 4}


def test_paragraph_interruption_rules_for_ordered_and_empty_markers():
    assert parse_list_marker("1. item\n", paragraph_open=True) is not None
    assert parse_list_marker("2. item\n", paragraph_open=True) is None
    assert parse_list_marker("-\n", paragraph_open=True) is None


def test_tight_bullet_list_renders_direct_paragraph_without_paragraph_tags():
    document = parse_blocks("- alpha\n- beta\n")
    assert render_html(document) == "<ul>\n<li>alpha\n</li>\n<li>beta\n</li>\n</ul>\n"


def test_ordered_list_preserves_non_one_start():
    document = parse_blocks("3. alpha\n4. beta\n")
    assert render_html(document) == '<ol start="3">\n<li>alpha\n</li>\n<li>beta\n</li>\n</ol>\n'


def test_nested_list_and_blank_separated_items_render_recursively():
    document = parse_blocks("- outer\n  - inner\n\n- second\n")
    rendered = render_html(document)
    assert rendered == "<ul>\n<li><p>outer</p>\n<ul>\n<li>inner\n</li>\n</ul>\n</li>\n<li><p>second</p>\n</li>\n</ul>\n"


def test_thematic_break_precedes_bullet_marker():
    assert render_html(parse_blocks("---\n")) == "<hr />\n"
