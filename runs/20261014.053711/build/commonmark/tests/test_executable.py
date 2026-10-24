"""Executable block tests: the `commonmark` entry point, input decoding, and line intake.

Each test acts on the system and reads the state back: an exit status, stdout bytes, the file
mode and shebang, or a returned value. No test matches on stderr text.
"""

import io
import os
import subprocess
import types
from pathlib import Path

import pytest

from mdparser import cli


def run_executable(project_root: Path, data: bytes) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data,
        capture_output=True,
        cwd=project_root,
        check=False,
    )


# --- Declared acceptance checks (transcribed from FEATURE-Executable.md) ---


def test_executable_empty_input(project_root: Path) -> None:
    """AC-001: empty stdin gives empty stdout and exit status 0."""
    result = subprocess.run(
        [str(project_root / "commonmark")],
        input="",
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    assert result.returncode == 0
    assert len(result.stdout) == 0


def test_executable_invalid_utf8(project_root: Path) -> None:
    """AC-002: invalid UTF-8 bytes are decoded with replacement and the program exits 0."""
    payload = b"\xff\xfe text \xc3\x28 end\n"
    result = run_executable(project_root, payload)
    assert result.returncode == 0
    result.stdout.decode("utf-8")


def test_executable_stdout_is_html_only(project_root: Path) -> None:
    """AC-003: a normal run exits 0 and its stdout is valid UTF-8 text."""
    source = "hello world\n\nsecond paragraph\n"
    result = run_executable(project_root, source.encode("utf-8"))
    assert result.returncode == 0
    result.stdout.decode("utf-8")


def test_executable_line_endings(project_root: Path) -> None:
    """LF, CR and CRLF line endings yield identical output for the same document."""
    lines = "one", "two", "", "three"
    variants = ["\n".join(lines) + "\n", "\r\n".join(lines) + "\r\n", "\r".join(lines) + "\r"]
    outputs = []
    for source in variants:
        result = run_executable(project_root, source.encode("utf-8"))
        assert result.returncode == 0
        outputs.append(result.stdout)
    assert outputs[0] == outputs[1] == outputs[2]


def test_executable_nul_replacement(project_root: Path) -> None:
    """U+0000 on input is treated exactly like U+FFFD."""
    with_nul = "a\x00b\n"
    with_replacement = "a�b\n"
    first = run_executable(project_root, with_nul.encode("utf-8"))
    second = run_executable(project_root, with_replacement.encode("utf-8"))
    assert first.returncode == 0
    assert second.returncode == 0
    assert first.stdout == second.stdout


# --- Executable file ---


def test_executable_file_has_execute_bit(project_root: Path) -> None:
    assert os.access(project_root / "commonmark", os.X_OK)


def test_executable_file_has_python3_shebang(project_root: Path) -> None:
    first_line = (project_root / "commonmark").read_bytes().splitlines()[0]
    assert first_line == b"#!/usr/bin/env python3"


def test_executable_runs_from_another_working_directory(project_root: Path, tmp_path: Path) -> None:
    result = subprocess.run(
        [str(project_root / "commonmark")],
        input=b"text\n",
        capture_output=True,
        cwd=tmp_path,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout == b"<p>text</p>\n"


# --- Decoding ---


def test_decode_source_keeps_valid_utf8() -> None:
    assert cli.decode_source("café ✓".encode("utf-8")) == "café ✓"


def test_decode_source_replaces_invalid_bytes() -> None:
    assert cli.decode_source(b"\xff") == "�"


def test_decode_source_replaces_truncated_sequence_without_eating_next_byte() -> None:
    assert cli.decode_source(b"\xc3\x28") == "�("


def test_decode_source_empty_bytes_gives_empty_text() -> None:
    assert cli.decode_source(b"") == ""


# --- Line intake ---


def test_split_lines_empty_text_is_one_empty_line() -> None:
    assert cli.split_lines("") == [""]


def test_split_lines_lf() -> None:
    assert cli.split_lines("a\nb") == ["a", "b"]


def test_split_lines_crlf_is_one_break() -> None:
    assert cli.split_lines("a\r\nb") == ["a", "b"]


def test_split_lines_cr_alone_is_a_break() -> None:
    assert cli.split_lines("a\rb") == ["a", "b"]


def test_split_lines_mixed_endings() -> None:
    assert cli.split_lines("a\r\nb\rc\nd") == ["a", "b", "c", "d"]


def test_split_lines_trailing_newline_gives_trailing_empty_line() -> None:
    assert cli.split_lines("a\n") == ["a", ""]


def test_split_lines_blank_lines_are_kept() -> None:
    assert cli.split_lines("a\n\n\nb") == ["a", "", "", "b"]


def test_split_lines_replaces_nul_with_replacement_character() -> None:
    assert cli.split_lines("a\x00b") == ["a�b"]


def test_split_lines_nul_is_not_a_line_break() -> None:
    assert cli.split_lines("\x00") == ["�"]


def test_split_lines_is_idempotent_on_its_joined_output() -> None:
    once = cli.split_lines("a\r\nb\rc")
    twice = cli.split_lines("\n".join(once))
    assert once == twice


# --- Rendering placeholder ---


def test_render_lines_renders_each_paragraph() -> None:
    assert cli.render_lines(["alpha", "", "beta"]) == "<p>alpha</p>\n<p>beta</p>\n"


def test_render_lines_empty_list_gives_empty_html() -> None:
    assert cli.render_lines([]) == ""


# --- In-process main ---


def invoke_main(monkeypatch: pytest.MonkeyPatch, data: bytes) -> tuple[int, bytes]:
    stdin = types.SimpleNamespace(buffer=io.BytesIO(data))
    stdout_buffer = io.BytesIO()
    stdout = types.SimpleNamespace(buffer=stdout_buffer)
    monkeypatch.setattr(cli.sys, "stdin", stdin)
    monkeypatch.setattr(cli.sys, "stdout", stdout)
    status = cli.main()
    return status, stdout_buffer.getvalue()


def test_main_returns_zero_and_writes_empty_html_for_empty_input(monkeypatch: pytest.MonkeyPatch) -> None:
    status, out = invoke_main(monkeypatch, b"")
    assert status == 0
    assert out == b""


def test_main_returns_zero_for_invalid_utf8(monkeypatch: pytest.MonkeyPatch) -> None:
    status, out = invoke_main(monkeypatch, b"\xff\xfe\x00")
    assert status == 0
    assert out == "<p>���</p>\n".encode("utf-8")


def test_main_returns_zero_when_rendering_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    def broken_render(lines: list[str]) -> str:
        raise RuntimeError("boom")

    monkeypatch.setattr(cli, "render_lines", broken_render)
    status, out = invoke_main(monkeypatch, b"text\n")
    assert status == 0
    assert out == b""


def test_main_writes_rendered_html_as_utf8(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "render_lines", lambda lines: "<p>" + "\n".join(lines) + "</p>\n")
    status, out = invoke_main(monkeypatch, "é\n".encode("utf-8"))
    assert status == 0
    assert out.decode("utf-8") == "<p>é\n</p>\n"
