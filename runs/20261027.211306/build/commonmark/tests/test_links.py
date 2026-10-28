from commonmark_parser.links import parse_links


def test_inline_link_destination_title_and_children():
    nodes = parse_links('[label](/destination "caption")', {})
    assert len(nodes) == 1
    link = nodes[0]
    assert (link.type, link.destination, link.title) == ("link", "/destination", "caption")
    assert [(child.type, child.literal) for child in link.children] == [("text", "label")]


def test_full_collapsed_and_shortcut_references_normalize_labels():
    refs = {"reference": {"destination": "/target", "title": None}}
    for source in ("[visible][REFERENCE]", "[reference][]", "[reference]"):
        nodes = parse_links(source, refs)
        assert len(nodes) == 1
        assert (nodes[0].type, nodes[0].destination, nodes[0].title) == ("link", "/target", None)


def test_inline_destination_supports_balanced_parentheses_and_escapes():
    nodes = parse_links(r"[x](a_(b\)))", {})
    assert nodes[0].destination == "a_(b))"


def test_angle_destination_decodes_entities_and_title_quote_styles():
    nodes = parse_links("[x](</a&amp;b> 'a \\\'quote\\'')", {})
    assert nodes[0].destination == "/a&b"
    assert nodes[0].title == "a 'quote'"


def test_unresolved_reference_and_image_remain_text():
    nodes = parse_links("[missing] ![image](src)", {})
    assert [(node.type, node.literal) for node in nodes] == [("text", "[missing] ![image](src)")]


def test_links_are_parsed_in_order_and_unlinked_text_is_preserved():
    nodes = parse_links("before [a](/a) middle [b](/b) after", {})
    assert [(n.type, n.literal if n.type == "text" else n.destination) for n in nodes] == [
        ("text", "before "), ("link", "/a"), ("text", " middle "),
        ("link", "/b"), ("text", " after")]
from commonmark_parser import render


def test_brackets_inside_code_span_do_not_start_link():
    assert render("[not a `link](/foo`)\n") == (
        "<p>[not a <code>link](/foo</code>)</p>\n"
    )
