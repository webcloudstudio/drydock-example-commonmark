import subprocess


def run_commonmark(source: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["./commonmark"],
        input=source.encode("utf-8"),
        capture_output=True,
        cwd=".",
    )


def test_empty_input_emits_empty_output_successfully():
    result = run_commonmark("")

    assert result.returncode == 0
    assert result.stdout == b""


def test_non_ascii_input_is_accepted_as_utf8():
    result = run_commonmark("café")

    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>café</p>\n"


def test_invalid_utf8_input_fails():
    result = subprocess.run(
        ["./commonmark"], input=b"\xff", capture_output=True, cwd="."
    )

    assert result.returncode != 0
