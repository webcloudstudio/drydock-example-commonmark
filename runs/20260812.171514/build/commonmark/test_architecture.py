from pathlib import Path


def test_architecture_boundaries_exist() -> None:
    required = [Path("cmark"), Path("parser"), Path("renderer")]
    assert all(path.exists() for path in required)


def test_conformance_wrapper_has_posix_entrypoint() -> None:
    wrapper = Path("full_test.sh")
    assert wrapper.is_file()
    assert wrapper.read_text(encoding="utf-8").startswith("#!")


def test_executable_preserves_standard_io_contract() -> None:
    import subprocess

    result = subprocess.run(
        ["./cmark"],
        input="hello\n",
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout == "<p>hello</p>\n"

