# FEATURE: Executable

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | The commonmark executable reads UTF-8 Markdown on stdin, normalizes lines, and writes only HTML to stdout. |
| Depends On  | ARCHITECTURE.md |
| Provides    | ./commonmark |
| Consumes    | mdparser.cli |

## Purpose

Deliver the executable `commonmark` at the application root. It takes no arguments.

## Trigger

A process runs `./commonmark` with Markdown on stdin.

## Sequence

1. Read all of stdin as bytes.
2. Decode as UTF-8 with U+FFFD replacement for invalid bytes.
3. Treat LF, CR and CRLF as line endings. Replace U+0000 with U+FFFD.
4. Pass the lines to the parser entry point in `mdparser.cli`. Until the block engine story lands this may be a placeholder that renders no blocks.
5. Write the rendered HTML to stdout as UTF-8 and exit 0.

## Interface

- File `commonmark` at the application root: python3 shebang, executable bit set, puts its own directory on `sys.path`, and does not need an activated virtual environment.
- stdin: UTF-8 Markdown. stdout: HTML only. stderr: diagnostics only.
- Exit status 0 for all input, including empty input and invalid UTF-8, with no traceback.
- `README.md` at the project root concisely describes the stdin/stdout interface. README content is not an acceptance criterion.

## Reads

- Standard input.

## Writes

- Standard output only. No files.

## Programmatic Acceptance

=== AC executable-empty-input ===
Intent: Empty standard input produces empty standard output and exit status 0 (AC-001).

import subprocess

result = subprocess.run(["./commonmark"], input="", capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
assert len(result.stdout) == 0
=== END AC executable-empty-input ===

=== AC executable-invalid-utf8 ===
Intent: Bytes that are not valid UTF-8 are decoded with replacement and the program exits 0 with decodable output (AC-002).

import subprocess

payload = b"\xff\xfe text \xc3\x28 end\n"
result = subprocess.run(["./commonmark"], input=payload, capture_output=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
result.stdout.decode("utf-8")
=== END AC executable-invalid-utf8 ===

=== AC executable-stdout-is-html-only ===
Intent: A normal run exits 0 and its stdout is valid UTF-8 text while diagnostics stay on stderr (AC-003).

import subprocess

source = "hello world\n\nsecond paragraph\n"
result = subprocess.run(["./commonmark"], input=source.encode("utf-8"), capture_output=True)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
result.stdout.decode("utf-8")
=== END AC executable-stdout-is-html-only ===

=== AC executable-line-endings ===
Intent: LF, CR and CRLF line endings yield identical output for the same document.

import subprocess

lines = "one", "two", "", "three"
variants = ["\n".join(lines) + "\n", "\r\n".join(lines) + "\r\n", "\r".join(lines) + "\r"]
outputs = []
for source in variants:
    result = subprocess.run(["./commonmark"], input=source.encode("utf-8"), capture_output=True)
    print(result.stdout)
    assert result.returncode == 0
    outputs.append(result.stdout)
assert outputs[0] == outputs[1] == outputs[2]
=== END AC executable-line-endings ===

=== AC executable-nul-replacement ===
Intent: U+0000 on input is treated exactly like U+FFFD (the spec's Insecure characters rule).
Encoding: utf-8

import subprocess

with_nul = "a\x00b\n"
with_replacement = "a\ufffdb\n"
first = subprocess.run(["./commonmark"], input=with_nul, capture_output=True, text=True, encoding="utf-8")
second = subprocess.run(["./commonmark"], input=with_replacement, capture_output=True, text=True, encoding="utf-8")
print(first.stdout)
assert first.returncode == 0
assert second.returncode == 0
assert first.stdout == second.stdout
=== END AC executable-nul-replacement ===

## User Acceptance

- None.

## Guardrails

- Never write anything but rendered HTML to stdout.
- Never require command-line arguments.
- Never exit non-zero or emit a traceback because of input content.
