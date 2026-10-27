from commonmark_parser import parse_blocks, render_html
from commonmark_parser.references import collect_definitions
from commonmark_parser.html_blocks import parse_html_block


def test_atx_heading_level_content_closing_marker_and_empty():
    doc = parse_blocks('  ## title ### \n######\n')
    assert [(n.type, n.level, n.raw_content) for n in doc.children] == [('heading', 2, 'title'), ('heading', 6, '')]


def test_atx_heading_interrupts_paragraph_and_unescaped_marker_rule():
    doc = parse_blocks('text\n# next\n\\# literal\n')
    assert [(n.type, n.raw_content) for n in doc.children] == [('paragraph', 'text'), ('heading', 'next'), ('paragraph', '\\# literal')]


def test_setext_heading_precedes_thematic_break():
    doc = parse_blocks('alpha\n---\n')
    assert [(n.type, n.level, n.raw) for n in doc.children] == [('heading', 2, 'alpha')]


def test_indented_code_preserves_literal_and_trims_outer_blank_lines():
    doc = parse_blocks('\n    a * b\n\n    c\n\n')
    assert len(doc.children) == 1
    assert doc.children[0].literal == 'a * b\n\nc\n'


def test_fenced_code_matches_character_length_and_retains_info():
    doc = parse_blocks('  ~~~~ py demo\n  a * b\n   ~~~~~\n')
    assert len(doc.children) == 1
    assert (doc.children[0].literal, doc.children[0].info) == ('a * b\n', 'py demo')


def test_fenced_code_unclosed_ends_at_document_and_backtick_info_rejects_ticks():
    doc = parse_blocks('```bad`info\ntext\n')
    assert [n.type for n in doc.children] == ['paragraph']
    assert parse_blocks('```\nx\n').children[0].literal == 'x\n'


def test_reference_collection_casefold_first_wins_and_returns_remainder():
    defs = {}
    remainder = collect_definitions('[Straße]: /one\nordinary\n', defs)
    collect_definitions('[STRASSE]: /two\n', defs)
    assert defs == {'strasse': ('/one', None)}
    assert remainder == 'ordinary\n'


def test_reference_titles_and_angle_destinations():
    defs = {}
    assert collect_definitions('[x]: <a&amp;b> "title"\n', defs) == ''
    assert defs == {'x': ('a&b', 'title')}


def test_html_comment_includes_terminator_line_and_intervening_blank():
    lines = ['<!-- start\n', '\n', 'end --> trailing\n', 'after\n']
    assert parse_html_block(lines) == (3, ''.join(lines[:3]))


def test_html_type_seven_does_not_interrupt_paragraph_and_stops_before_blank():
    lines = ['<custom>\n', 'content\n', '\n']
    assert parse_html_block(lines, paragraph_open=True) is None
    assert parse_html_block(lines) == (2, ''.join(lines[:2]))


def test_all_html_start_types_are_recognized():
    starts = ['<script>\n', '<!--x\n', '<?x\n', '<!DOCTYPE x\n', '<![CDATA[x\n', '<div>\n', '<x a="b">\n']
    for line in starts:
        assert parse_html_block([line, 'tail\n']) is not None


def test_rendering_escapes_code_and_preserves_html():
    doc = parse_blocks('## <x>\n\n```\n<a>&\n```\n\n<!-- raw -->\n')
    assert render_html(doc) == '<h2>&lt;x&gt;</h2>\n<pre><code>&lt;a&gt;&amp;\n</code></pre>\n<!-- raw -->\n'
