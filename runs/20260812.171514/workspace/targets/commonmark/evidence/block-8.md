# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57654
- execution id: 20260812.182602.995Z-d9e470df

## Stories built
- Parse code spans and line breaks. (inline-code-breaks) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-INLINE-CODE-BREAKS.md (SP 396)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- renderer/html.py
- test_inline_code_breaks.py

## Pre-build acceptance observation
- RED: code-spans (FEATURE-INLINE-CODE-BREAKS.md)
  intent: The implementation passes code span delimiter, matching, normalization, and precedence examples.
  return code: 1
  stdout:
    Example 332 (lines 5929-5933) Code spans
    ` `` `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>``</code></p>
    +<p><code> </code><code> </code></p>
    
    Example 333 (lines 5937-5941) Code spans
    `  ``  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> `` </code></p>
    +<p><code> </code><code> </code></p>
    
    Example 340 (lines 6012-6016) Code spans
    `foo\`bar`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo\</code>bar`</p>
    +<p><code>foo\`bar</code></p>
    
    Example 342 (lines 6029-6033) Code spans
    ` foo `` bar `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo `` bar</code></p>
    +<p><code>foo</code><code>bar</code></p>
    
    Example 343 (lines 6041-6045) Code spans
    *foo`*`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo<code>*</code></p>
    +<p><em>foo<code></em></code></p>
    
    Example 344 (lines 6050-6054) Code spans
    [not a `link](/foo`)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[not a <code>link](/foo</code>)</p>
    +<p><a href="/foo%3C/code%3E">not a <code>link</a></p>
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +<p><code>&lt;a href="</code>&quot;&gt;`</p>
    
    Example 349 (lines 6097-6101) Code spans
    ```foo``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>```foo``</p>
    +<p><code>`foo</code></p>
    
    Example 351 (lines 6113-6117) Code spans
    `foo``bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>`foo<code>bar</code></p>
    +<p><code>foo</code><code>bar</code>`</p>
    
    13 passed, 9 failed, 0 errored, 633 skipped
  stderr:
    Traceback (most recent call last):
      File "code-spans.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: line-breaks (FEATURE-INLINE-CODE-BREAKS.md)
  intent: The implementation passes hard-break, soft-break, trailing-space, and break-context examples.
  return code: 1
  stdout:
    Example 639 (lines 9285-9291) Hard line breaks
    foo  
         bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>bar</p>
    +<p>foo<br> bar</p>
    
    Example 640 (lines 9294-9300) Hard line breaks
    foo\
         bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>bar</p>
    +<p>foo<br> bar</p>
    
    Example 645 (lines 9344-9350) Hard line breaks
    <a href="foo  
    bar">
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<p><a href="foo  
    +<p><a href="foo&lt;br /&gt;
     bar"></p>
    
    Example 646 (lines 9353-9359) Hard line breaks
    <a href="foo\
    bar">
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<p><a href="foo\
    +<p><a href="foo&lt;br /&gt;
     bar"></p>
    
    13 passed, 4 failed, 0 errored, 638 skipped
  stderr:
    Traceback (most recent call last):
      File "line-breaks.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: code-spans (FEATURE-INLINE-CODE-BREAKS.md)
  intent: The implementation passes code span delimiter, matching, normalization, and precedence examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    22 passed, 0 failed, 0 errored, 633 skipped
- PASS: line-breaks (FEATURE-INLINE-CODE-BREAKS.md)
  intent: The implementation passes hard-break, soft-break, trailing-space, and break-context examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    17 passed, 0 failed, 0 errored, 638 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- renderer/html.py
- test_inline_code_breaks.py

SUMMARY:
Implemented code-span delimiter matching, normalization, precedence, hard breaks, soft breaks, and HTML-tag protection. Added regression tests.

Scoped checks pass: 22/22 and 17/17. Full suite still has unrelated pre-existing block parser failures.

BLOCKERS:
- Full `sh full_test.sh` does not pass due to tab/list/setext block parsing failures outside this story.
