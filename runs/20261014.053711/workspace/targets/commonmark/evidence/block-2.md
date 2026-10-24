# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5042
- execution id: 20261014.055500.842Z-fcb0e42e

## Stories built
- Provide the executable ./commonmark: UTF-8 stdin to HTML stdout, line intake, and README. (executable-interface) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Executable.md (SP 1571)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- README.md
- commonmark
- data/logs/test_2026-10-14_015613.log
- mdparser/cli.py
- tests/test_executable.py
- tests/test_foundation.py

## Pre-build acceptance observation
- RED: executable-empty-input (FEATURE-Executable.md)
  intent: Empty standard input produces empty standard output and exit status 0 (AC-001).
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 2
      err_msg = 'No such file or directory'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-empty-input.py", line 3, in <module>
        result = subprocess.run(["./commonmark"], input="", capture_output=True, text=True)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
- RED: executable-invalid-utf8 (FEATURE-Executable.md)
  intent: Bytes that are not valid UTF-8 are decoded with replacement and the program exits 0 with decodable output (AC-002).
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 2
      err_msg = 'No such file or directory'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-invalid-utf8.py", line 4, in <module>
        result = subprocess.run(["./commonmark"], input=payload, capture_output=True)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
- RED: executable-stdout-is-html-only (FEATURE-Executable.md)
  intent: A normal run exits 0 and its stdout is valid UTF-8 text while diagnostics stay on stderr (AC-003).
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 2
      err_msg = 'No such file or directory'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-stdout-is-html-only.py", line 4, in <module>
        result = subprocess.run(["./commonmark"], input=source.encode("utf-8"), capture_output=True)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
- RED: executable-line-endings (FEATURE-Executable.md)
  intent: LF, CR and CRLF line endings yield identical output for the same document.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 2
      err_msg = 'No such file or directory'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-line-endings.py", line 7, in <module>
        result = subprocess.run(["./commonmark"], input=source.encode("utf-8"), capture_output=True)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
- RED: executable-nul-replacement (FEATURE-Executable.md)
  intent: U+0000 on input is treated exactly like U+FFFD (the spec's Insecure characters rule).
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 2
      err_msg = 'No such file or directory'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-nul-replacement.py", line 5, in <module>
        first = subprocess.run(["./commonmark"], input=with_nul, capture_output=True, text=True, encoding="utf-8")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.drydock/claude-home/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'

## Post-build programmatic acceptance
- PASS: executable-empty-input (FEATURE-Executable.md)
  intent: Empty standard input produces empty standard output and exit status 0 (AC-001).
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: executable-invalid-utf8 (FEATURE-Executable.md)
  intent: Bytes that are not valid UTF-8 are decoded with replacement and the program exits 0 with decodable output (AC-002).
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    b''
    b''
- PASS: executable-stdout-is-html-only (FEATURE-Executable.md)
  intent: A normal run exits 0 and its stdout is valid UTF-8 text while diagnostics stay on stderr (AC-003).
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    b''
    b''
- PASS: executable-line-endings (FEATURE-Executable.md)
  intent: LF, CR and CRLF line endings yield identical output for the same document.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    b''
    b''
    b''
- PASS: executable-nul-replacement (FEATURE-Executable.md)
  intent: U+0000 on input is treated exactly like U+FFFD (the spec's Insecure characters rule).
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
The package stubs and the foundation test are in place. `test_foundation.py` asserts that `mdparser.cli` has no public attributes, which this block must change because `cli.main` is required. I'll write the code, then update that one assertion and say so in the summary.Two fixes before moving on: the `re` import belongs at module top, and the error path should emit a one-line diagnostic rather than a traceback, matching the guardrail.Now the root executable, README, and the foundation test adjustment.Now the executable's test file. The five declared acceptance checks are transcribed as-is; the rest cover the helper functions, the in-process `main`, and the executable file itself.I'm dropping one test I just wrote: it pins down how extra arguments are handled, which the spec doesn't define. I'm also removing the unused `argv` parameter from `main`.Next, set the executable bit and run the project's declared test command, `bin/test.sh`.All 47 pass. Now I'll confirm the staged assets are untouched and check what git sees.RESULT: SUCCESS

FILES CHANGED:
- commonmark
- README.md
- mdparser/cli.py
- tests/test_executable.py
- tests/test_foundation.py

SUMMARY:
- `./commonmark` is a python3 shebang script with the executable bit set. It puts its own directory on `sys.path` and calls `mdparser.cli.main`. It needs no venv.
- `mdparser/cli.py` reads stdin bytes, decodes UTF-8 with U+FFFD replacement, splits on LF, CR, or CRLF, and replaces U+0000 with U+FFFD. `render_lines` is the placeholder entry point and returns empty HTML, which the spec allows until the block engine lands. `main()` writes UTF-8 bytes to stdout and always returns 0.
- `README.md` describes the stdin/stdout interface.
- `tests/test_executable.py` transcribes the five declared acceptance checks (AC-001, AC-002, AC-003, line endings, NUL replacement) as tests. It also adds tests for the decode and line-split helpers, the in-process `main`, and the executable file itself. Oracles are exit status, stdout bytes, the file mode and shebang, and return values.
- `tests/test_foundation.py`: `cli` now has a public `main`, so the old "no behavior yet" check would fail on it. I split that check into `NO_BEHAVIOR_MODULES`, which leaves out `cli`. The other modules still must have no public attributes.
- `bin/test.sh`: 47 passed, 0 failed. I did not run `sources/full_test.sh`, because no criterion in this block invokes the staged conformance suite. The staged `sources/` files are unchanged.

Choices I made that you may want to change:
- Internal errors during rendering are caught. They print one line to stderr and exit 0, so the "exit 0 for all input" guardrail holds. A bug in the renderer would therefore produce empty output with a stderr line rather than a crash.
- Extra command-line arguments are ignored; the spec doesn't say what to do with them.

<blueprint-decisions>
[{"spec":"FEATURE-Executable.md","severity":"Low","subject":"Catch-all for internal rendering errors","decision":"main() catches any exception raised while decoding or rendering, prints one diagnostic line to stderr, writes empty stdout, and returns 0. This keeps the exit-0-for-all-input guardrail. Once the block engine lands, this may hide renderer bugs as empty output, so it could be narrowed or made to exit non-zero then. Is that acceptable, or should it change on replan?"}]
</blueprint-decisions>
