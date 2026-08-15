# FEATURE: CLI Executable

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Provide the UTF-8 standard-input/standard-output parser executable. |
| Depends On  | FEATURE-HTML-Renderer.md |
| Provides    | commonmark stdin/stdout executable |
| Consumes    | HTML renderer |

## Intent

The executable provides the product boundary: it reads UTF-8 Markdown from standard input, renders it, and writes HTML to standard output without requiring a public Markdown runtime dependency.

## Behavior

- Consume all Markdown from standard input.
- Decode UTF-8 input and emit UTF-8 HTML on standard output.
- Preserve the adapter-compatible process contract used by `sources/cmark.py`.
- Write diagnostics to standard error when a process-level failure occurs.
- Return zero for successfully processed documents and nonzero for unrecoverable process failures.
- Avoid importing or invoking a public Markdown implementation.

## Programmatic Acceptance

=== AC cli-stdin-stdout ===
Intent: The executable accepts Markdown on standard input and returns successful HTML output on standard output.

import subprocess

source = "plain text\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
assert result.stdout
=== END AC cli-stdin-stdout ===

=== AC cli-utf8 ===
Intent: The executable accepts UTF-8 Markdown and emits UTF-8 output without a decoding failure.
Encoding: utf-8

import subprocess

source = "Unicode: café\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
assert result.stdout
=== END AC cli-utf8 ===

=== AC cli-empty-input ===
Intent: The executable completes successfully for an empty standard-input document.

import subprocess

result = subprocess.run(
    ["./commonmark"],
    input="",
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=__import__("sys").stderr)
assert result.returncode == 0
=== END AC cli-empty-input ===

## User Acceptance

- None.

## Guardrails

- Preserve the standard-input/standard-output contract.
- Do not require command-line arguments for ordinary conversion.
- Do not use a public Markdown implementation at runtime.
