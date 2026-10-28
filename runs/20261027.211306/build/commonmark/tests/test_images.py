from commonmark_parser.images import parse_images


def test_inline_image_destination_title_and_alt():
    nodes = parse_images('![picture](/image "caption")', {})
    assert len(nodes) == 1
    image = nodes[0]
    assert (image.type, image.destination, image.title, image.alt) == (
        "image", "/image", "caption", "picture")


def test_reference_image_omits_emphasis_from_alt():
    refs = {"picture": {"destination": "/image", "title": None}}
    nodes = parse_images("![*picture*][picture]", refs)
    assert len(nodes) == 1
    assert (nodes[0].type, nodes[0].destination, nodes[0].title, nodes[0].alt) == (
        "image", "/image", None, "picture")


def test_collapsed_and_shortcut_reference_images():
    refs = {"picture": {"destination": "/image", "title": "caption"}}
    for source in ("![picture][]", "![picture]"):
        nodes = parse_images(source, refs)
        assert [(node.destination, node.title, node.alt) for node in nodes] == [
            ("/image", "caption", "picture")]


def test_image_alt_includes_link_text_and_nested_image_alt():
    refs = {"linked": {"destination": "/link", "title": None}}
    nodes = parse_images("![**bold** [linked](/link) ![inner](x)](outer)", refs)
    assert len(nodes) == 1
    assert nodes[0].alt == "bold linked inner"


def test_unresolved_reference_is_ignored_and_many_images_keep_order():
    nodes = parse_images("![missing][unknown] ![a](one) ![b](two)", {})
    assert [(node.destination, node.alt) for node in nodes] == [("one", "a"), ("two", "b")]


def test_inline_image_accepts_empty_alt_and_escaped_text():
    nodes = parse_images(r"![](x) ![a\*b](y)", {})
    assert [(node.destination, node.alt) for node in nodes] == [("x", ""), ("y", "a*b")]
