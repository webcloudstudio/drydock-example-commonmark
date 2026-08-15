# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 59919
- execution id: 20260815.180149.286Z-7c7e7eaa

## Stories built
- Normalize Markdown input lines, whitespace, tabs, and insecure characters. (block-input) [story]

## Reusable compacts
- spec_compact.md
- spec_tests_compact.md
- cmark_compact.md
- normalize_compact.md

## Stacked context
- compass: COMPASS.md (SP 1237)
- implements: FEATURE-Block-Input.md (SP 648)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 124)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- blocks.py
- commonmark
- normalization.py
- renderer.py

## Pre-build acceptance observation
- RED: block-input-tabs (FEATURE-Block-Input.md)
  intent: The implementation passes the complete Tabs conformance section.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.175124/build/commonmark/sources/spec_tests.py", line 164, in <module>
        result = do_test(test, args.normalize, previous.get(str(test['example'])))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.175124/build/commonmark/sources/spec_tests.py", line 44, in do_test
        [retcode, actual_html_bytes, err] = cmark.to_html(test['markdown'])
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.175124/build/commonmark/sources/cmark.py", line 23, in <lambda>
        self.to_html = lambda x: pipe_through_prog(prog, x)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.175124/build/commonmark/sources/cmark.py", line 10, in pipe_through_prog
        p1 = Popen(prog.split(), stdout=PIPE, stdin=PIPE, stderr=PIPE)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
    
    Traceback (most recent call last):
      File "block-input-tabs.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): block-input-characters (FEATURE-Block-Input.md)
  intent: The implementation passes the complete Characters and lines conformance section.
  return code: 0
  stdout:
    0 passed, 0 failed, 0 errored, 655 skipped
- GREEN (prepassed): block-input-insecure (FEATURE-Block-Input.md)
  intent: The implementation passes the complete Insecure characters conformance section.
  return code: 0
  stdout:
    0 passed, 0 failed, 0 errored, 655 skipped

## Post-build programmatic acceptance
- PASS: block-input-tabs (FEATURE-Block-Input.md)
  intent: The implementation passes the complete Tabs conformance section.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    11 passed, 0 failed, 0 errored, 644 skipped
- PASS: block-input-characters (FEATURE-Block-Input.md)
  intent: The implementation passes the complete Characters and lines conformance section.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    0 passed, 0 failed, 0 errored, 655 skipped
- PASS: block-input-insecure (FEATURE-Block-Input.md)
  intent: The implementation passes the complete Insecure characters conformance section.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    0 passed, 0 failed, 0 errored, 655 skipped

## Build summary
<reusable-compact filename="spec.txt">
CommonMark 0.31.2 UTF-8 Markdown-to-HTML conformance specification. Input supports Unicode, LF/CRLF/CR line endings, tab-stop indentation, literal internal tabs, and U+0000 → U+FFFD.
</reusable-compact>

<reusable-compact filename="spec_tests.py">
Run scoped conformance with `python sources/spec_tests.py --spec sources/spec.txt --program ./commonmark --pattern REGEX`. Verdict is the process exit code; output is diagnostic only.
</reusable-compact>

<reusable-compact filename="cmark.py">
Conformance harness adapter. Program mode pipes UTF-8 Markdown to the executable and captures return code, stdout, and stderr.
</reusable-compact>

<reusable-compact filename="normalize.py">
HTML comparison normalizer for conformance tests. Collapses insignificant HTML whitespace, normalizes attributes and entities, and preserves preformatted content.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- blocks.py
- normalization.py
- renderer.py
- commonmark

SUMMARY:
Implemented NUL and line-ending normalization, tab-stop-aware indentation, literal internal-tab preservation, and required tab-sensitive block rendering. Tabs suite: 11 passed. Local unit tests: 4 passed.

BLOCKERS:
- None
