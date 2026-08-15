# Evidence: Block 1 · Foundational (block-1)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 8224
- execution id: 20260815.203018.197Z-421d690d

## Stories built
- Provide the executable standard-input/standard-output interface. (interface-001) [story]

## Reusable compacts
- ARCHITECTURE_compact.md
- cmark_compact.md

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: ARCHITECTURE.md (SP 647)
- context: cmark.py (SP 339)
- stack: common.md (SP 1807)
- stack: python.md (SP 3892)

## Build directory changes
- README.md
- commonmark
- tests/test_interface.py

## Pre-build acceptance observation
- RED: interface-executable (ARCHITECTURE.md)
  intent: The application root contains an executable named commonmark.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "interface-executable.py", line 4, in <module>
        assert os.path.isfile(path)
               ^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: interface-process (ARCHITECTURE.md)
  intent: The executable accepts standard input and terminates successfully.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "interface-process.py", line 4, in <module>
        result = subprocess.run(
                 ^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
- RED: interface-utf8 (ARCHITECTURE.md)
  intent: The executable accepts UTF-8 input and terminates successfully.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "interface-utf8.py", line 4, in <module>
        result = subprocess.run(
                 ^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'

## Post-build programmatic acceptance
- PASS: interface-executable (ARCHITECTURE.md)
  intent: The application root contains an executable named commonmark.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
- PASS: interface-process (ARCHITECTURE.md)
  intent: The executable accepts standard input and terminates successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <p>interface probe</p>
- PASS: interface-utf8 (ARCHITECTURE.md)
  intent: The executable accepts UTF-8 input and terminates successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <p>UTF-8 interface probe</p>

## Agent self-report (advisory)
The build agent declared a failure. This is advisory only; the programmatic acceptance above is the authority for this block's outcome.
- summary: Supplied full conformance suite has 303 failures.
- detail:
    The executable runs successfully, but block parsing and inline edge cases—especially nested lists, HTML blocks, delimiter rules, and autolinks—still differ from the supplied specification. These behaviors require further parser implementation before rerunning the full suite.

## Build summary
<reusable-compact filename="ARCHITECTURE.md">
Executable `commonmark` reads UTF-8 Markdown from stdin and writes HTML to stdout. Python 3 standard library only; replace NUL with U+FFFD. Preserve executable name and immutable `sources/` assets.
</reusable-compact>

<reusable-compact filename="cmark.py">
Support contract: parser process accepts UTF-8 stdin, returns exit code 0 with UTF-8 HTML on stdout, and reports failures through nonzero exit status/stderr.
</reusable-compact>

RESULT: FAILED

FILES CHANGED:
- commonmark
- README.md
- tests/test_interface.py

SUMMARY:
Implemented the executable stdin/stdout interface and self-contained Python parser. Interface probes pass. Full conformance result: 352 passed, 303 failed, 0 errored, 0 skipped.

BLOCKERS:
- Full CommonMark 0.31.2 conformance is not yet satisfied.

FAILURE_SUMMARY: Supplied full conformance suite has 303 failures.

FAILURE_DETAIL: The executable runs successfully, but block parsing and inline edge cases—especially nested lists, HTML blocks, delimiter rules, and autolinks—still differ from the supplied specification. These behaviors require further parser implementation before rerunning the full suite.
