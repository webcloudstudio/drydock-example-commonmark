# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 60056
- execution id: 20260815.210928.719Z-4a50798b

## Stories built
- Parse lists, list items, nesting, laziness, and tightness. (block-003) [story]

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Block-Lists.md (SP 627)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark
- tests/test_interface.py

## Pre-build acceptance observation
- RED: lists-conformance (FEATURE-Block-Lists.md)
  intent: The implementation passes every supplied conformance example owned by list items and lists.
  return code: 1
  stdout:
    Example 257 (lines 4212-4221) List items
    - one
    
     two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>one</li></ul><p>two</p>
    +<ul><li><p>one</p></li></ul><p>two</p>
    
    Example 259 (lines 4238-4248) List items
     -    one
    
         two
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li>one</li></ul><pre><code> two
    -</code></pre>
    +<ul><li><p>one</p><p>two</p></li></ul>
    
    Example 262 (lines 4300-4313) List items
    >>- one
    >>
      >  > two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><ul><li>one</li></ul><p>two</p></blockquote></blockquote>
    +<blockquote><blockquote><ul><li><p>one</p></li></ul><p>two</p></blockquote></blockquote>
    
    Example 267 (lines 4399-4405) List items
    123456789. ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="123456789"><li>ok</li></ol>
    +<ol><li>ok</li></ol>
    
    Example 268 (lines 4408-4412) List items
    1234567890. not ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>1234567890. not ok</p>
    +<ol><li>not ok</li></ol>
    
    Example 270 (lines 4426-4432) List items
    003. ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="3"><li>ok</li></ol>
    +<ol start="003"><li>ok</li></ol>
    
    Example 273 (lines 4477-4489) List items
      10.  foo
    
               bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol start="10"><li><p>foo</p><pre><code>bar
    +<ol><li><p>foo</p><pre><code>  bar
     </code></pre></li></ol>
    
    Example 275 (lines 4511-4527) List items
    1.     indented code
    
       paragraph
    
           more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
    -<ol><li><pre><code>indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    -</code></pre></li></ol>
    +<ol><li><p>indented code</p></li></ol><p>paragraph</p><pre><code>   more code
    +</code></pre>
    
    Example 276 (lines 4533-4549) List items
    1.      indented code
    
       paragraph
    
           more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
    -<ol><li><pre><code> indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    -</code></pre></li></ol>
    +<ol><li><p>indented code</p></li></ol><p>paragraph</p><pre><code>   more code
    +</code></pre>
    
    Example 278 (lines 4570-4579) List items
    -    foo
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><p>bar</p>
    +<ul><li><p>foo</p></li></ul><p>bar</p>
    
    Example 280 (lines 4614-4635) List items
    -
      foo
    -
      ```
      bar
      ```
    -
          baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
    -<ul><li>foo</li><li><pre><code>bar
    -</code></pre></li><li><pre><code>baz
    -</code></pre></li></ul>
    +<h2>- foo</h2><pre><code>bar
    +</code></pre><p>- baz</p>
    
    Example 281 (lines 4640-4647) List items
    -   
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul>
    +<ul><li></li></ul><p>foo</p>
    
    Example 282 (lines 4654-4663) List items
    -
    
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul><p>foo</p>
    +<p>-</p><p>foo</p>
    
    Example 283 (lines 4668-4678) List items
    - foo
    -
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li></li><li>bar</li></ul>
    +<ul><li>foo</li></ul><p>- - bar</p>
    
    Example 284 (lines 4683-4693) List items
    - foo
    -   
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li></li><li>bar</li></ul>
    +<ul><li><p>foo</p></li><li></li><li><p>bar</p></li></ul>
    
    Example 285 (lines 4698-4708) List items
    1. foo
    2.
    3. bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li>foo</li><li></li><li>bar</li></ol>
    +<ol><li>foo</li></ol><p>2. 3. bar</p>
    
    Example 286 (lines 4713-4719) List items
    *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul>
    +<p>*</p>
    
    Example 288 (lines 4745-4764) List items
     1.  A paragraph
         with two lines.
    
             indented code
    
         > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code> indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 289 (lines 4769-4788) List items
      1.  A paragraph
          with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>  indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 290 (lines 4793-4812) List items
       1.  A paragraph
           with two lines.
    
               indented code
    
           > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>   indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 292 (lines 4847-4866) List items
      1.  A paragraph
    with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,4 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +<ol><li>A paragraph</li></ol><p>with two lines.</p><pre><code>      indented code
    +
    +  &gt; A block quote.
    +</code></pre>
    
    Example 293 (lines 4871-4879) List items
      1.  A paragraph
        with two lines.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li>A paragraph with two lines.</li></ol>
    +<ol><li><p>A paragraph with two lines.</p></li></ol>
    
    Example 294 (lines 4884-4898) List items
    > 1. > Blockquote
    continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li><blockquote><p>Blockquote</p></blockquote></li></ol><p>continued here.</p></blockquote>
    
    Example 295 (lines 4901-4915) List items
    > 1. > Blockquote
    > continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li><blockquote><p>Blockquote</p></blockquote></li></ol><p>continued here.</p></blockquote>
    
    Example 296 (lines 4929-4950) List items
    - foo
      - bar
        - baz
          - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz<ul><li>boo</li></ul></li></ul></li></ul></li></ul>
    +<ul><li>foo</li><li><p>bar - baz - boo</p></li></ul>
    
    Example 298 (lines 4972-4983) List items
    10) foo
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="10"><li>foo<ul><li>bar</li></ul></li></ol>
    +<ol><li><p>foo - bar</p></li></ol>
    
    Example 299 (lines 4988-4998) List items
    10) foo
       - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="10"><li>foo</li></ol><ul><li>bar</li></ul>
    +<ol><li>foo</li></ol><ul><li>bar</li></ul>
    
    Example 302 (lines 5035-5049) List items
    - # Foo
    - Bar
      ---
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><h1>Foo</h1></li><li><h2>Bar</h2>baz</li></ul>
    +<ul><li><h1>Foo</h1></li><li><h2>Bar</h2><p>baz</p></li></ul>
    
    Example 303 (lines 5271-5283) Lists
    - foo
    - bar
    + baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li></ul><ul><li>baz</li></ul>
    +<ul><li>foo</li><li>bar</li><li>baz</li></ul>
    
    Example 304 (lines 5286-5298) Lists
    1. foo
    2. bar
    3) baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li>foo</li><li>bar</li></ol><ol start="3"><li>baz</li></ol>
    +<ol><li>foo</li><li>bar</li><li>baz</li></ol>
    
    Example 305 (lines 5305-5315) Lists
    Foo
    - bar
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><ul><li>bar</li><li>baz</li></ul>
    +<p>Foo - bar - baz</p>
    
    Example 307 (lines 5392-5400) Lists
    The number of windows in my house is
    1.  The number of doors is 6.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>The number of windows in my house is</p><ol><li>The number of doors is 6.</li></ol>
    +<p>The number of windows in my house is 1. The number of doors is 6.</p>
    
    Example 309 (lines 5427-5449) Lists
    - foo
      - bar
        - baz
    
    
          bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li>foo<ul><li>bar<ul><li><p>baz</p><p>bim</p></li></ul></li></ul></li></ul>
    +<ul><li><p>foo</p></li><li><p>bar - baz</p><pre><code>bim
    +</code></pre></li></ul>
    
    Example 310 (lines 5457-5475) Lists
    - foo
    - bar
    
    <!-- -->
    
    - baz
    - bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li></ul><!-- --><ul><li>baz</li><li>bim</li></ul>
    +<ul><li><p>foo</p></li><li><p>bar</p></li></ul><!-- --><ul><li>baz</li><li>bim</li></ul>
    
    Example 314 (lines 5554-5568) Lists
    - a
     - b
      - c
       - d
        - e
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a</li><li>b</li><li>c</li><li>d - e</li></ul>
    +<ul><li>a</li><li>b</li><li>c</li><li><p>d - e</p></li></ul>
    
    Example 315 (lines 5574-5591) Lists
    1. a
    
      2. b
    
        3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li></ol><pre><code>3. c
    -</code></pre>
    +<ol><li><p>a</p></li><li><p>b</p><ol start="3"><li>c</li></ol></li></ol>
    
    Example 317 (lines 5619-5634) Lists
    * a
    *
    
    * c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li></li><li><p>c</p></li></ul>
    +<ul><li>a</li></ul><p>*</p><ul><li>c</li></ul>
    
    Example 320 (lines 5686-5705) Lists
    - a
    - ```
      b
    
    
      ```
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,4 @@
    -<ul><li>a</li><li><pre><code>b
    +<ul><li><p>a</p></li><li><pre><code>b
     
     
    -</code></pre></li><li>c</li></ul>
    +</code></pre></li><li><p>c</p></li></ul>
    
    Example 321 (lines 5712-5730) Lists
    - a
      - b
    
        c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li><p>b</p><p>c</p></li></ul></li><li>d</li></ul>
    +<ul><li><p>a</p></li><li><p>b</p><p>c</p></li><li><p>d</p></li></ul>
    
    Example 322 (lines 5736-5750) Lists
    * a
      > b
      >
    * c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<blockquote><p>b</p></blockquote></li><li>c</li></ul>
    +<ul><li><p>a</p><blockquote><p>b</p></blockquote></li><li>c</li></ul>
    
    Example 323 (lines 5756-5774) Lists
    - a
      > b
      ```
      c
      ```
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li>a<blockquote><p>b</p></blockquote><pre><code>c
    -</code></pre></li><li>d</li></ul>
    +<ul><li><p>a</p><blockquote><p>b</p><pre><code></code></pre></blockquote><p>c</p><pre><code></code></pre></li><li>d</li></ul>
    
    Example 325 (lines 5788-5799) Lists
    - a
      - b
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li>b</li></ul></li></ul>
    +<ul><li>a</li><li>b</li></ul>
    
    Example 327 (lines 5824-5839) Lists
    * foo
      * bar
    
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><ul><li>bar</li></ul><p>baz</p></li></ul>
    +<ul><li><p>foo</p></li><li><p>bar</p><p>baz</p></li></ul>
    
    Example 328 (lines 5842-5867) Lists
    - a
      - b
      - c
    
    - d
      - e
      - f
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p><ul><li>b</li><li>c</li></ul></li><li><p>d</p><ul><li>e</li><li>f</li></ul></li></ul>
    +<ul><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li><li><p>d</p></li><li><p>e</p></li><li><p>f</p></li></ul>
    
    30 passed, 44 failed, 0 errored, 581 skipped
  stderr:
    Traceback (most recent call last):
      File "lists-conformance.py", line 20, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): lists-interface (FEATURE-Block-Lists.md)
  intent: A bullet list is accepted through the executable interface.
  return code: 0
  stdout:
    <ul><li>one</li><li>two</li></ul>
- GREEN (prepassed): lists-nested-input (FEATURE-Block-Lists.md)
  intent: Nested and ordered list input is accepted through the executable interface.
  return code: 0
  stdout:
    <ol><li>one</li></ol>
    <ul><li>nested</li></ul>

## Post-build programmatic acceptance
- PASS: lists-conformance (FEATURE-Block-Lists.md)
  intent: The implementation passes every supplied conformance example owned by list items and lists.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    74 passed, 0 failed, 0 errored, 581 skipped
- PASS: lists-interface (FEATURE-Block-Lists.md)
  intent: A bullet list is accepted through the executable interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <ul><li>one</li><li>two</li></ul>
- PASS: lists-nested-input (FEATURE-Block-Lists.md)
  intent: Nested and ordered list input is accepted through the executable interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <ol><li>one
    <ul><li>nested</li></ul></li></ol>

## Repair attempts
- attempt 0 (initial build): failed; 2/3 checks; 73/74 cases model=gpt-5.6-luna; execution 20260815.210131.085Z-a3196f28
- attempt 1 (repair 1): built; 3/3 checks; 74/74 cases model=gpt-5.6-luna; execution 20260815.210928.719Z-4a50798b

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark
- tests/test_interface.py

SUMMARY:
Fixed nested-list tightness detection and loose outer-list rendering. List conformance passes: 74 passed, 0 failed. Added deterministic regression tests; all 5 interface tests pass.

BLOCKERS:
- None
