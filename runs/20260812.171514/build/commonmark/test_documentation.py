from pathlib import Path


def test_readme_documents_standard_input_and_output() -> None:
    text = Path("README.md").read_text(encoding="utf-8").lower()

    assert "standard input" in text or "stdin" in text
    assert "standard output" in text or "stdout" in text


def test_readme_documents_complete_suite_command() -> None:
    text = Path("README.md").read_text(encoding="utf-8")

    assert "sh full_test.sh" in text
