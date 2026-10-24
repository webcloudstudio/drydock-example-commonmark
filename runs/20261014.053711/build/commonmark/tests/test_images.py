"""Image tests: the image construct in its inline and reference forms, the plain-text alt attribute,
nesting with links and images, and the corpus sections that the images story gates.

The declared acceptance checks are transcribed from FEATURE-Images.md with their assertions kept as
written. The remaining tests compare the returned HTML string, or the executable's stdout, with its
exact expected value. Reference maps are built per test, so no state is shared between tests.
"""

import subprocess
import sys
from pathlib import Path

from mdparser import inlines
from mdparser.refs import ReferenceMap


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


def references_with(*definitions: tuple[str, str, str | None]) -> ReferenceMap:
    """A fresh reference map holding each (label, destination, title) definition."""
    references = ReferenceMap()
    for label, destination, title in definitions:
        references.add(label, destination, title)
    return references


def parse(source: str, references: ReferenceMap | None = None) -> str:
    return inlines.parse_inline(source, references)


# --- Declared acceptance checks (transcribed from FEATURE-Images.md) ---


def test_images_corpus_sections(project_root: Path) -> None:
    """AC images-corpus-sections: the Emphasis and strong emphasis, Links and Images sections pass."""
    result = subprocess.run(
        [
            sys.executable,
            "sources/spec_tests.py",
            "--program",
            str(project_root / "commonmark"),
            "--spec",
            "sources/spec.txt",
            "--pattern",
            "^Emphasis and strong emphasis$|^Links$|^Images$",
        ],
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0


def test_images_inline_image(project_root: Path) -> None:
    """AC images-inline-image: an inline image renders one img element carrying the supplied src, alt and title."""
    alt = "my alt"
    src = "/path/pic.jpg"
    title = "a title"
    source = "![" + alt + "](" + src + ' "' + title + '")\n'
    result = subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<img ") == 1
    assert ('src="' + src + '"') in result.stdout
    assert ('alt="' + alt + '"') in result.stdout
    assert ('title="' + title + '"') in result.stdout


def test_images_alt_is_plain_text(project_root: Path) -> None:
    """AC images-alt-is-plain-text: emphasis inside an image description does not appear as markup in alt."""
    result = subprocess.run(
        [str(project_root / "commonmark")],
        input="![foo *bar*](/u)\n",
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<img ") == 1
    assert result.stdout.count("<em>") == 0


def test_images_reference_forms(project_root: Path) -> None:
    """AC images-reference-forms: full, collapsed and shortcut image references each resolve against a definition."""
    definition = "\n\n[foo]: /url\n"
    for use in ("![text][foo]", "![foo][]", "![foo]"):
        result = subprocess.run(
            [str(project_root / "commonmark")],
            input=use + definition,
            capture_output=True,
            text=True,
            cwd=project_root,
            check=False,
        )
        print(result.stdout)
        assert result.returncode == 0
        assert result.stdout.count("<img ") == 1


def test_images_inside_link(project_root: Path) -> None:
    """AC images-inside-link: an image inside a link produces one a element containing one img element."""
    result = subprocess.run(
        [str(project_root / "commonmark")],
        input="[![moon](moon.jpg)](/uri)\n",
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<a ") == 1
    assert result.stdout.count("<img ") == 1


# --- Inline form: attributes ---


def test_inline_image_without_title_has_no_title_attribute() -> None:
    assert parse("![foo](/url)") == '<img src="/url" alt="foo" />'


def test_inline_image_with_title() -> None:
    assert parse('![foo](/url "title")') == '<img src="/url" alt="foo" title="title" />'


def test_inline_image_with_empty_description_has_empty_alt() -> None:
    assert parse("![](/url)") == '<img src="/url" alt="" />'


def test_image_title_is_escaped() -> None:
    assert parse('![a](/u "x&y")') == '<img src="/u" alt="a" title="x&amp;y" />'


def test_image_src_is_percent_encoded() -> None:
    assert parse("![a](</a b>)") == '<img src="/a%20b" alt="a" />'


def test_image_src_is_percent_encoded_for_non_ascii() -> None:
    assert parse("![a](/é)") == '<img src="/%C3%A9" alt="a" />'


# --- Alt text is the plain text of the description ---


def test_alt_drops_strong_emphasis_markup() -> None:
    assert parse("![foo **bar**](/u)") == '<img src="/u" alt="foo bar" />'


def test_alt_keeps_code_span_content() -> None:
    assert parse("![foo `bar`](/u)") == '<img src="/u" alt="foo bar" />'


def test_alt_keeps_link_text_and_drops_the_link() -> None:
    assert parse("![foo [bar](/url)](/url2)") == '<img src="/url2" alt="foo bar" />'


def test_alt_takes_the_alt_of_a_nested_image() -> None:
    assert parse("![foo ![bar](/url)](/url2)") == '<img src="/url2" alt="foo bar" />'


def test_alt_keeps_autolink_text() -> None:
    assert parse("![<http://x.y>](/u)") == '<img src="/u" alt="http://x.y" />'


def test_alt_is_escaped_text() -> None:
    assert parse("![a<b&c](/u)") == '<img src="/u" alt="a&lt;b&amp;c" />'


def test_alt_keeps_an_escaped_punctuation_character_as_text() -> None:
    assert parse("![a\\*b](/u)") == '<img src="/u" alt="a*b" />'


def test_alt_decodes_a_character_reference() -> None:
    assert parse("![&copy;](/u)") == '<img src="/u" alt="©" />'


# --- Reference forms ---


def test_full_reference_image_uses_its_text_as_alt() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("![text][foo]", references) == '<img src="/url" alt="text" />'


def test_collapsed_reference_image_uses_its_label_as_alt() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("![foo][]", references) == '<img src="/url" alt="foo" />'


def test_shortcut_reference_image_uses_its_label_as_alt() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("![foo]", references) == '<img src="/url" alt="foo" />'


def test_reference_image_carries_the_definition_title() -> None:
    references = references_with(("foo", "/url", "t"))
    assert parse("![foo]", references) == '<img src="/url" alt="foo" title="t" />'


def test_unresolved_shortcut_image_is_literal_text() -> None:
    assert parse("![foo]") == "![foo]"


def test_unresolved_full_reference_fails_the_whole_image() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("![text][bar]", references) == "![text][bar]"


# --- Interaction with the other constructs ---


def test_image_inside_link_renders_one_anchor_around_one_image() -> None:
    assert parse("[![moon](moon.jpg)](/uri)") == (
        '<a href="/uri"><img src="moon.jpg" alt="moon" /></a>'
    )


def test_image_in_running_text_keeps_surrounding_text() -> None:
    assert parse("My ![foo](/path) here") == 'My <img src="/path" alt="foo" /> here'


def test_escaped_bang_leaves_a_link_after_it() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("\\![foo]", references) == '!<a href="/url">foo</a>'


def test_escaped_opening_bracket_after_bang_is_literal() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("!\\[foo]", references) == "![foo]"


# --- Executable ---


def test_executable_renders_an_image_paragraph(project_root: Path) -> None:
    result = run_executable(project_root, "![foo](/url)\n")
    assert result.returncode == 0
    assert result.stdout == b'<p><img src="/url" alt="foo" /></p>\n'


def test_executable_resolves_an_image_reference_definition(project_root: Path) -> None:
    result = run_executable(project_root, "![foo]\n\n[foo]: /url\n")
    assert result.returncode == 0
    assert result.stdout == b'<p><img src="/url" alt="foo" /></p>\n'
