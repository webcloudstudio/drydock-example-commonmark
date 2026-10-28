from commonmark_parser.fenced_code import parse_fenced_code


def test_fenced_code_preserves_unindented_content_after_indented_fence():
    assert parse_fenced_code([" ```", " aaa", "aaa", "```"])[0] == "aaa\naaa\n"


def test_fenced_code_removes_only_available_indentation():
    assert parse_fenced_code(["  ```", "a", "  b", "  ```"])[0] == "a\nb\n"
