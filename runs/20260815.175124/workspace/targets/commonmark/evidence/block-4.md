# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-08-15
- resulting state: closed/failed
- story points (combined assembled cost): 59854
- execution id: 20260815.182507.700Z-c801ce17

## Stories built
- Collect and resolve document-wide link reference definitions. (block-references) [story]

## Stacked context
- compass: COMPASS.md (SP 1237)
- implements: FEATURE-Block-References.md (SP 576)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 124)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- blocks.py
- references.py
- renderer.py
- test_references.py

## Pre-build acceptance observation
- RED: block-references-valid (FEATURE-Block-References.md)
  intent: The implementation passes the complete valid link-reference-definition conformance coverage.
  return code: 1
  stdout:
    Example 194 (lines 3201-3207) Link reference definitions
    [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +<p>[foo]: /url &quot;title&quot;</p><p>[foo]</p>
    
    Example 195 (lines 3210-3218) Link reference definitions
       [foo]: 
          /url  
               'the title'  
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="the title">foo</a></p>
    +<p>[foo]: /url 'the title'</p><p>[foo]</p>
    
    Example 196 (lines 3221-3227) Link reference definitions
    [Foo*bar\]]:my_(url) 'title (with parens)'
    
    [Foo*bar\]]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my_(url)" title="title (with parens)">Foo*bar]</a></p>
    +<p>[Foo*bar]]:my_(url) 'title (with parens)'</p><p>[Foo*bar]]</p>
    
    Example 197 (lines 3230-3238) Link reference definitions
    [Foo bar]:
    <my url>
    'title'
    
    [Foo bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my%20url" title="title">Foo bar</a></p>
    +<p>[Foo bar]: <my url> 'title'</p><p>[Foo bar]</p>
    
    Example 198 (lines 3243-3257) Link reference definitions
    [foo]: /url '
    title
    line1
    line2
    '
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1 @@
    -<p><a href="/url" title="
    -title
    -line1
    -line2
    -">foo</a></p>
    +<p>[foo]: /url ' title line1 line2 '</p><p>[foo]</p>
    
    Example 200 (lines 3277-3284) Link reference definitions
    [foo]:
    /url
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p>
    +<p>[foo]: /url</p><p>[foo]</p>
    
    Example 202 (lines 3301-3307) Link reference definitions
    [foo]: <>
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">foo</a></p>
    +<p>[foo]: &lt;&gt;</p><p>[foo]</p>
    
    Example 204 (lines 3325-3331) Link reference definitions
    [foo]: /url\bar\*baz "foo\"bar\baz"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%5Cbar*baz" title="foo&quot;bar\baz">foo</a></p>
    +<p>[foo]: /url\bar*baz &quot;foo&quot;bar\baz&quot;</p><p>[foo]</p>
    
    Example 205 (lines 3336-3342) Link reference definitions
    [foo]
    
    [foo]: url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="url">foo</a></p>
    +<p>[foo]</p><p>[foo]: url</p>
    
    Example 206 (lines 3348-3355) Link reference definitions
    [foo]
    
    [foo]: first
    [foo]: second
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="first">foo</a></p>
    +<p>[foo]</p><p>[foo]: first [foo]: second</p>
    
    Example 207 (lines 3361-3367) Link reference definitions
    [FOO]: /url
    
    [Foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">Foo</a></p>
    +<p>[FOO]: /url</p><p>[Foo]</p>
    
    Example 208 (lines 3370-3376) Link reference definitions
    [ΑΓΩ]: /φου
    
    [αγω]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/%CF%86%CE%BF%CF%85">αγω</a></p>
    +<p>[ΑΓΩ]: /φου</p><p>[αγω]</p>
    
    Example 209 (lines 3385-3388) Link reference definitions
    [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -
    +<p>[foo]: /url</p>
    
    Example 210 (lines 3393-3400) Link reference definitions
    [
    foo
    ]: /url
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>bar</p>
    +<p>[ foo ]: /url bar</p>
    
    Example 212 (lines 3415-3420) Link reference definitions
    [foo]: /url
    "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&quot;title&quot; ok</p>
    +<p>[foo]: /url &quot;title&quot; ok</p>
    
    Example 216 (lines 3470-3479) Link reference definitions
    # [Foo]
    [foo]: /url
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1><a href="/url">Foo</a></h1><blockquote><p>bar</p></blockquote>
    +<h1>[Foo]</h1><p>[foo]: /url</p><blockquote><p>bar</p></blockquote>
    
    Example 217 (lines 3481-3489) Link reference definitions
    [foo]: /url
    bar
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>bar</h1><p><a href="/url">foo</a></p>
    +<h1>[foo]: /url bar</h1><p>[foo]</p>
    
    Example 218 (lines 3491-3498) Link reference definitions
    [foo]: /url
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>=== <a href="/url">foo</a></p>
    +<h1>[foo]: /url</h1><p>[foo]</p>
    
    Example 219 (lines 3504-3517) Link reference definitions
    [foo]: /foo-url "foo"
    [bar]: /bar-url
      "bar"
    [baz]: /baz-url
    
    [foo],
    [bar],
    [baz]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/foo-url" title="foo">foo</a>, <a href="/bar-url" title="bar">bar</a>, <a href="/baz-url">baz</a></p>
    +<p>[foo]: /foo-url &quot;foo&quot; [bar]: /bar-url &quot;bar&quot; [baz]: /baz-url</p><p>[foo], [bar], [baz]</p>
    
    Example 220 (lines 3525-3533) Link reference definitions
    [foo]
    
    > [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p><blockquote></blockquote>
    +<p>[foo]</p><blockquote><p>[foo]: /url</p></blockquote>
    
    7 passed, 20 failed, 0 errored, 628 skipped
  stderr:
    Traceback (most recent call last):
      File "block-references-valid.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: block-references-container (FEATURE-Block-References.md)
  intent: The implementation passes reference-definition cases involving document-wide and container-scoped definitions.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "block-references-container.py", line 4, in <module>
        result = subprocess.run(
                 ^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1885, in _execute_child
        self.pid = _fork_exec(
                   ^^^^^^^^^^^
    TypeError: expected str, bytes or os.PathLike object, not int

## Post-build programmatic acceptance
- PASS: block-references-valid (FEATURE-Block-References.md)
  intent: The implementation passes the complete valid link-reference-definition conformance coverage.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    27 passed, 0 failed, 0 errored, 628 skipped
- FAIL: block-references-container (FEATURE-Block-References.md)
  intent: The implementation passes reference-definition cases involving document-wide and container-scoped definitions.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "block-references-container.py", line 4, in <module>
        result = subprocess.run(
                 ^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1885, in _execute_child
        self.pid = _fork_exec(
                   ^^^^^^^^^^^
    TypeError: expected str, bytes or os.PathLike object, not int

## Repair attempts
- attempt 0 (initial build): failed; 1/2 checks; 27/27 cases model=gpt-5.6-luna; execution 20260815.181932.834Z-9850addb
- attempt 1 (repair 1): failed; 1/2 checks; 27/27 cases model=gpt-5.6-luna; execution 20260815.182359.473Z-fc3de0c3
- attempt 2 (repair 2): failed; 1/2 checks; 27/27 cases model=gpt-5.6-luna; execution 20260815.182507.700Z-c801ce17; stopped: deterministic acceptance score did not improve on 2 consecutive calls

## Failure
- summary: programmatic acceptance failed: block-references-container
- detail:
    Block "Block 4 · Service" [block-4] failed its acceptance criteria.
      Story "Collect and resolve document-wide link reference definitions." [block-references] does not meet its own acceptance criteria:
        - AC block-references-container — The implementation passes reference-definition cases involving document-wide and container-scoped definitions.
            assertion: TypeError: expected str, bytes or os.PathLike object, not int
            process exit code: 1
            error: TypeError: expected str, bytes or os.PathLike object, not int

## Build summary
AC_BROKEN: block-references-container

RESULT: SUCCESS

FILES CHANGED:
- references.py

SUMMARY:
Reference-definition conformance passes 27/27; project tests pass 10/10. Hardened multiline-title blank-line validation. The container criterion is broken because it passes integer `999999` to `subprocess.run`; the equivalent string argument passes.

BLOCKERS:
- Repair `block-references-container` to pass `"999999"` as a string.
