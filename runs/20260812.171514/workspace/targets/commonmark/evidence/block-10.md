# Evidence: Block 10 · Service (block-10)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57886
- execution id: 20260812.190933.972Z-21d3a70b

## Stories built
- Parse links and images. (inline-links) [story]

## Acceptance tooling authorization
- FEATURE-INLINE-LINKS.md#inline-links-suite: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-INLINE-LINKS.md#inline-links-boundaries: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-INLINE-LINKS.md (SP 615)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark
- parser/blocks.py
- renderer/html.py

## Pre-build acceptance observation
- RED: inline-links-suite (FEATURE-INLINE-LINKS.md)
  intent: The inline link, reference link, and image syntax passes its complete owned conformance scope.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/build/commonmark/spec_tests.py", line 164, in <module>
        result = do_test(test, args.normalize, previous.get(str(test['example'])))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/build/commonmark/spec_tests.py", line 44, in do_test
        [retcode, actual_html_bytes, err] = cmark.to_html(test['markdown'])
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/build/commonmark/cmark.py", line 23, in <lambda>
        self.to_html = lambda x: pipe_through_prog(prog, x)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20260812.171514/build/commonmark/cmark.py", line 10, in pipe_through_prog
        p1 = Popen(prog.split(), stdout=PIPE, stdin=PIPE, stderr=PIPE)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    FileNotFoundError: [Errno 2] No such file or directory: './commonmark'
    
    Traceback (most recent call last):
      File "inline-links-suite.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: inline-links-boundaries (FEATURE-INLINE-LINKS.md)
  intent: The implementation preserves link and image destination, title, reference, and nesting behavior.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "inline-links-boundaries.py", line 9, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: inline-links-suite (FEATURE-INLINE-LINKS.md)
  intent: The inline link, reference link, and image syntax passes its complete owned conformance scope.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    112 passed, 0 failed, 0 errored, 543 skipped
- PASS: inline-links-boundaries (FEATURE-INLINE-LINKS.md)
  intent: The implementation preserves link and image destination, title, reference, and nesting behavior.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Repair attempts
- attempt 0 (initial build): failed; 0/2 checks; 89/112 cases model=gpt-5.6-luna; execution 20260812.184119.134Z-7c4c336d
- attempt 1 (repair 1): failed; 0/2 checks; 111/112 cases model=gpt-5.6-luna; execution 20260812.185600.907Z-5cca4fa6
- attempt 2 (repair 2): built; 2/2 checks; 112/112 cases model=gpt-5.6-luna; execution 20260812.190933.972Z-21d3a70b

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- renderer/html.py

SUMMARY:
Fixed nested image alt-text extraction. Links/Images scope passes: 112 passed.

BLOCKERS:
- `sh full_test.sh` still fails on unrelated list/block parsing cases outside this build block.
