import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).parents[1]

def run_parser(source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(ROOT / "commonmark")], input=source,
                          capture_output=True, text=True, encoding="utf-8")

def test_executable_exists_and_is_executable():
    executable = ROOT / "commonmark"
    assert executable.is_file()
    assert os.access(executable, os.X_OK)

def test_standard_input_produces_html_on_standard_output():
    result = run_parser("interface probe\n")
    assert result.returncode == 0
    assert result.stdout == "<p>interface probe</p>\n"

def test_utf8_standard_input_round_trips_as_html():
    result = run_parser("café — 東京\n")
    assert result.returncode == 0
    assert result.stdout == "<p>café — 東京</p>\n"

def test_emphasis_delimiter_runs_support_nesting_and_unmatched_markers():
    result = run_parser("***strong emph***\n\nfoo_bar_baz\n\n**foo*\n")
    assert result.returncode == 0
    assert result.stdout == (
        "<p><em><strong>strong emph</strong></em></p>\n"
        "<p>foo_bar_baz</p>\n"
        "<p>*<em>foo</em></p>\n"
    )

def test_emphasis_uses_unicode_flanking_rules():
    result = run_parser("* a *\n\nfoo*bar*\n\nfoo_bar_\n")
    assert result.returncode == 0
    assert result.stdout == (
        "<p>* a *</p>\n"
        "<p>foo<em>bar</em></p>\n"
        "<p>foo_bar_</p>\n"
    )

def test_nested_list_blank_line_does_not_loosen_outer_list():
    source = "- foo\n  - bar\n    - baz\n\n\n      bim\n"
    result = run_parser(source)
    assert result.returncode == 0
    assert result.stdout == (
        "<ul><li>foo\n<ul><li>bar\n<ul><li><p>baz</p>\n<p>bim</p>"
        "</li></ul></li></ul></li></ul>\n"
    )

def test_blank_between_outer_siblings_makes_list_loose():
    source = "- a\n  - b\n  - c\n\n- d\n  - e\n  - f\n"
    result = run_parser(source)
    assert result.returncode == 0
    assert result.stdout == (
        "<ul><li><p>a</p>\n<ul><li>b</li><li>c</li></ul></li>"
        "<li><p>d</p>\n<ul><li>e</li><li>f</li></ul></li></ul>\n"
    )
