"""List tests: the five declared checks from FEATURE-Lists.md, then exact-output tests for grouping, start
numbers, and tight or loose rendering.

The declared checks are transcribed first, with their assertions unchanged. The rest act on the
executable and compare the exact stdout bytes handed back.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_commonmark(project_root: Path, source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )


def render(project_root: Path, source: str) -> str:
    result = run_commonmark(project_root, source)
    assert result.returncode == 0
    return result.stdout


# --- Declared acceptance checks (transcribed from FEATURE-Lists.md) ---


def test_lists_corpus_sections(project_root: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "sources/spec_tests.py",
            "--program",
            str(project_root / "commonmark"),
            "--spec",
            "sources/spec.txt",
            "--pattern",
            "^Lists$|^List items$|^Block quotes$|^Thematic breaks$|^ATX headings$|^Setext headings$|^Indented code blocks$|^Fenced code blocks$|^Precedence$",
        ],
        capture_output=True,
        text=True,
        cwd=project_root,
        env={**os.environ},
        check=False,
    )
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0


def test_lists_changing_marker_starts_new_list(project_root: Path) -> None:
    bullets = run_commonmark(project_root, "- foo\n- bar\n+ baz\n")
    ordered = run_commonmark(project_root, "1. foo\n2. bar\n3) baz\n")
    print(bullets.stdout)
    print(ordered.stdout)
    assert bullets.returncode == 0
    assert ordered.returncode == 0
    assert bullets.stdout.count("<ul>") == 2
    assert ordered.stdout.count("<ol") == 2


def test_lists_tight_versus_loose(project_root: Path) -> None:
    tight = run_commonmark(project_root, "- a\n- b\n")
    loose = run_commonmark(project_root, "- a\n\n- b\n")
    print(tight.stdout)
    print(loose.stdout)
    assert tight.returncode == 0
    assert loose.returncode == 0
    assert tight.stdout.count("<p>") == 0
    assert loose.stdout.count("<p>") == 2


def test_lists_blank_inside_item_makes_loose(project_root: Path) -> None:
    result = run_commonmark(project_root, "- a\n- b\n\n  c\n- d\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 4


def test_lists_blank_in_code_stays_tight(project_root: Path) -> None:
    result = run_commonmark(project_root, "- a\n- ```\n  b\n\n\n  ```\n- c\n")
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 0
    assert result.stdout.count("<pre>") == 1


def test_lists_interrupt_paragraph(project_root: Path) -> None:
    bullet = run_commonmark(project_root, "Foo\n- bar\n- baz\n")
    one = run_commonmark(project_root, "Intro\n1. item\n")
    other = run_commonmark(project_root, "Intro\n14. item\n")
    print(bullet.stdout)
    print(one.stdout)
    print(other.stdout)
    assert bullet.returncode == 0
    assert one.returncode == 0
    assert other.returncode == 0
    assert bullet.stdout.count("<ul>") == 1
    assert one.stdout.count("<ol") == 1
    assert other.stdout.count("<ol") == 0


# --- Grouping items into lists ---


def test_same_bullet_character_forms_one_list(project_root: Path) -> None:
    assert render(project_root, "- a\n- b\n") == "<ul>\n<li>a</li>\n<li>b</li>\n</ul>\n"


def test_same_ordered_delimiter_forms_one_list(project_root: Path) -> None:
    assert render(project_root, "1. a\n1. b\n") == "<ol>\n<li>a</li>\n<li>b</li>\n</ol>\n"


def test_changed_bullet_character_starts_second_list(project_root: Path) -> None:
    assert render(project_root, "- a\n* b\n") == "<ul>\n<li>a</li>\n</ul>\n<ul>\n<li>b</li>\n</ul>\n"


def test_changed_ordered_delimiter_starts_second_list(project_root: Path) -> None:
    assert render(project_root, "1. a\n1) b\n") == "<ol>\n<li>a</li>\n</ol>\n<ol>\n<li>b</li>\n</ol>\n"


def test_bullet_and_ordered_items_do_not_share_a_list(project_root: Path) -> None:
    assert render(project_root, "- a\n1. b\n") == "<ul>\n<li>a</li>\n</ul>\n<ol>\n<li>b</li>\n</ol>\n"


def test_blank_lines_between_items_do_not_split_the_list(project_root: Path) -> None:
    assert render(project_root, "- a\n\n\n- b\n") == "<ul>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n</li>\n</ul>\n"


def test_list_ends_at_a_paragraph_and_the_paragraph_is_outside(project_root: Path) -> None:
    assert render(project_root, "- a\n- b\n\nparagraph\n") == "<ul>\n<li>a</li>\n<li>b</li>\n</ul>\n<p>paragraph</p>\n"


def test_single_item_is_one_list_of_one(project_root: Path) -> None:
    assert render(project_root, "- a\n") == "<ul>\n<li>a</li>\n</ul>\n"


def test_empty_document_has_no_list(project_root: Path) -> None:
    assert render(project_root, "") == ""


# --- Start number ---


def test_ordered_list_starting_at_one_has_no_start_attribute(project_root: Path) -> None:
    assert render(project_root, "1. a\n2. b\n") == "<ol>\n<li>a</li>\n<li>b</li>\n</ol>\n"


def test_ordered_list_starting_elsewhere_states_its_start(project_root: Path) -> None:
    assert render(project_root, "2. a\n3. b\n") == '<ol start="2">\n<li>a</li>\n<li>b</li>\n</ol>\n'


def test_start_number_comes_from_first_item_not_later_items(project_root: Path) -> None:
    assert render(project_root, "3. a\n1. b\n") == '<ol start="3">\n<li>a</li>\n<li>b</li>\n</ol>\n'


# --- Tight and loose rendering ---


def test_tight_list_paragraphs_have_no_p_tags(project_root: Path) -> None:
    assert render(project_root, "- a\n- b\n") == "<ul>\n<li>a</li>\n<li>b</li>\n</ul>\n"


def test_loose_list_paragraphs_have_p_tags(project_root: Path) -> None:
    assert render(project_root, "- a\n\n- b\n") == "<ul>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n</li>\n</ul>\n"


def test_blank_between_two_blocks_of_one_item_makes_whole_list_loose(project_root: Path) -> None:
    assert render(project_root, "- a\n\n  b\n") == "<ul>\n<li>\n<p>a</p>\n<p>b</p>\n</li>\n</ul>\n"


def test_blank_before_last_item_makes_the_earlier_item_loose(project_root: Path) -> None:
    assert render(project_root, "- a\n- b\n\n  c\n- d\n") == (
        "<ul>\n<li>\n<p>a</p>\n</li>\n<li>\n<p>b</p>\n<p>c</p>\n</li>\n<li>\n<p>d</p>\n</li>\n</ul>\n"
    )


def test_blank_inside_fenced_code_does_not_make_list_loose(project_root: Path) -> None:
    assert render(project_root, "- a\n- ```\n  b\n\n  c\n  ```\n- d\n") == (
        "<ul>\n<li>a</li>\n<li><pre><code>b\n\nc\n</code></pre>\n</li>\n<li>d</li>\n</ul>\n"
    )


def test_blank_inside_block_quote_does_not_make_list_loose(project_root: Path) -> None:
    assert render(project_root, "- > a\n  >\n  > b\n- c\n") == (
        "<ul>\n<li><blockquote>\n<p>a</p>\n<p>b</p>\n</blockquote>\n</li>\n<li>c</li>\n</ul>\n"
    )


def test_blank_line_after_list_does_not_make_list_loose(project_root: Path) -> None:
    assert render(project_root, "- a\n- b\n\n") == "<ul>\n<li>a</li>\n<li>b</li>\n</ul>\n"


def test_blank_between_nested_items_does_not_make_outer_list_loose(project_root: Path) -> None:
    assert render(project_root, "- a\n  - b\n\n  - c\n- d\n") == (
        "<ul>\n<li>a\n<ul>\n<li>\n<p>b</p>\n</li>\n<li>\n<p>c</p>\n</li>\n</ul>\n</li>\n<li>d</li>\n</ul>\n"
    )


def test_blank_between_nested_list_and_outer_block_makes_outer_list_loose(project_root: Path) -> None:
    assert render(project_root, "- a\n  - b\n\n  c\n") == (
        "<ul>\n<li>\n<p>a</p>\n<ul>\n<li>b</li>\n</ul>\n<p>c</p>\n</li>\n</ul>\n"
    )


def test_blank_after_nested_list_makes_outer_list_loose_when_item_follows(project_root: Path) -> None:
    assert render(project_root, "- a\n  - b\n\n- c\n") == (
        "<ul>\n<li>\n<p>a</p>\n<ul>\n<li>b</li>\n</ul>\n</li>\n<li>\n<p>c</p>\n</li>\n</ul>\n"
    )


def test_nested_list_decides_its_own_looseness(project_root: Path) -> None:
    assert render(project_root, "- a\n  - b\n  - c\n\n  d\n") == (
        "<ul>\n<li>\n<p>a</p>\n<ul>\n<li>b</li>\n<li>c</li>\n</ul>\n<p>d</p>\n</li>\n</ul>\n"
    )


def test_link_reference_definition_is_not_a_block_for_looseness(project_root: Path) -> None:
    assert render(project_root, "- [a]: /u\n\n  b\n- c\n") == "<ul>\n<li>b</li>\n<li>c</li>\n</ul>\n"


# --- Continuation measured inside an enclosing block quote ---


def test_item_in_block_quote_takes_a_continuation_paragraph(project_root: Path) -> None:
    assert render(project_root, "> 1. a\n>\n>    b\n") == (
        "<blockquote>\n<ol>\n<li>\n<p>a</p>\n<p>b</p>\n</li>\n</ol>\n</blockquote>\n"
    )


def test_paragraph_after_block_quote_marker_closes_item_when_not_indented(project_root: Path) -> None:
    assert render(project_root, "> - a\n>\n> > b\n") == (
        "<blockquote>\n<ul>\n<li>a</li>\n</ul>\n<blockquote>\n<p>b</p>\n</blockquote>\n</blockquote>\n"
    )


def test_item_content_column_is_measured_from_the_enclosing_block_quote(project_root: Path) -> None:
    assert render(project_root, ">- one\n>\n  > two\n") == (
        "<blockquote>\n<ul>\n<li>one</li>\n</ul>\n<p>two</p>\n</blockquote>\n"
    )


def test_item_content_column_is_measured_from_nested_block_quotes(project_root: Path) -> None:
    assert render(project_root, ">>- one\n>>\n  >  > two\n") == (
        "<blockquote>\n<blockquote>\n<ul>\n<li>one</li>\n</ul>\n<p>two</p>\n</blockquote>\n</blockquote>\n"
    )


# --- Looseness is per list ---


def test_looseness_is_decided_per_list(project_root: Path) -> None:
    assert render(project_root, "- a\n\n* b\n") == "<ul>\n<li>a</li>\n</ul>\n<ul>\n<li>b</li>\n</ul>\n"
