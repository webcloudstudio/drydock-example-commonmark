# Evidence: Block 6 · Service (block-6)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57791
- execution id: 20260812.180817.999Z-c4c95ab1

## Stories built
- Parse CommonMark list items and list structure. (block-lists) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-BLOCK-LISTS.md (SP 523)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- parser/blocks.py
- renderer/html.py
- test_lists.py

## Pre-build acceptance observation
- RED: lists-structure (FEATURE-BLOCK-LISTS.md)
  intent: The implementation passes list marker, nesting, indentation, and continuation conformance examples.
  return code: 1
  stdout:
    Example 256 (lines 4179-4198) List items
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
    
    Example 260 (lines 4251-4262) List items
     -    one
    
          two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li><p>one</p><p>two</p></li></ul>
    +<ul><li><p>one</p><pre><code>two
    +</code></pre></li></ul>
    
    Example 262 (lines 4300-4313) List items
    >>- one
    >>
      >  > two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><ul><li>one</li></ul><p>two</p></blockquote></blockquote>
    +<blockquote><blockquote><ul><li><p>one</p></li></ul><p>two</p></blockquote></blockquote>
    
    Example 273 (lines 4477-4489) List items
      10.  foo
    
               bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol start="10"><li><p>foo</p><pre><code>bar
    +<ol start="10"><li><p>foo</p><pre><code>     bar
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
    +<ol><li><p>indented code</p><p>paragraph</p><pre><code> more code
     </code></pre></li></ol>
    
    Example 276 (lines 4533-4549) List items
    1.      indented code
    
       paragraph
    
           more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
    -<ol><li><pre><code> indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    +<ol><li><p>indented code</p><p>paragraph</p><pre><code> more code
     </code></pre></li></ol>
    
    Example 278 (lines 4570-4579) List items
    -    foo
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><p>bar</p>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
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
    @@ -1,3 +1,3 @@
    -<ul><li>foo</li><li><pre><code>bar
    +<ul><li><p>foo</p></li><li><pre><code>bar
     </code></pre></li><li><pre><code>baz
     </code></pre></li></ul>
    
    Example 281 (lines 4640-4647) List items
    -   
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul>
    +<ul><li><p>foo</p></li></ul>
    
    Example 282 (lines 4654-4663) List items
    -
    
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul><p>foo</p>
    +<ul><li><p>foo</p></li></ul>
    
    Example 288 (lines 4745-4764) List items
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
    
    Example 289 (lines 4769-4788) List items
      1.  A paragraph
          with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,4 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +<ol><li><p>A paragraph with two lines.</p><pre><code>    indented code
    +
    +&gt; A block quote.
    +</code></pre></li></ol>
    
    Example 290 (lines 4793-4812) List items
       1.  A paragraph
           with two lines.
    
               indented code
    
           > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,4 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +<ol><li><p>A paragraph with two lines.</p><pre><code>     indented code
    +
    + &gt; A block quote.
    +</code></pre></li></ol>
    
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
    +<blockquote><ol><li>&gt; Blockquote</li></ol><p>continued here.</p></blockquote>
    
    Example 295 (lines 4901-4915) List items
    > 1. > Blockquote
    > continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li>&gt; Blockquote</li></ol><p>continued here.</p></blockquote>
    
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
    +<ol start="10"><li><p>foo - bar</p></li></ol>
    
    Example 300 (lines 5003-5013) List items
    - - foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><ul><li>foo</li></ul></li></ul>
    +<ul><li>- foo</li></ul>
    
    Example 301 (lines 5016-5030) List items
    1. - 2. foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><ul><li><ol start="2"><li>foo</li></ol></li></ul></li></ol>
    +<ol><li>- 2. foo</li></ol>
    
    Example 302 (lines 5035-5049) List items
    - # Foo
    - Bar
      ---
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><h1>Foo</h1></li><li><h2>Bar</h2>baz</li></ul>
    +<ul><li># Foo</li><li><h2>Bar</h2><p>baz</p></li></ul>
    
    Example 303 (lines 5271-5283) Lists
    - foo
    - bar
    + baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li></ul><ul><li>baz</li></ul>
    +<ul><li>foo</li><li>bar</li><li>baz</li></ul>
    
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
    
    Example 308 (lines 5406-5425) Lists
    - foo
    
    - bar
    
    
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p></li><li><p>bar</p></li><li><p>baz</p></li></ul>
    +<ul><li><p>foo</p></li><li><p>bar</p></li><li>baz</li></ul>
    
    Example 309 (lines 5427-5449) Lists
    - foo
      - bar
        - baz
    
    
          bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li>foo<ul><li>bar<ul><li><p>baz</p><p>bim</p></li></ul></li></ul></li></ul>
    +<ul><li>foo</li><li><p>bar - baz</p><pre><code>bim
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
    +<ul><li>foo</li><li><p>bar</p></li></ul><!-- --><ul><li>baz</li><li>bim</li></ul>
    
    Example 313 (lines 5530-5548) Lists
    1. a
    
      2. b
    
       3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li></ol>
    +<ol><li><p>a</p></li><li><p>b</p></li><li>c</li></ol>
    
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
    
    Example 316 (lines 5597-5614) Lists
    - a
    - b
    
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li></ul>
    +<ul><li>a</li><li><p>b</p></li><li>c</li></ul>
    
    Example 317 (lines 5619-5634) Lists
    * a
    *
    
    * c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li></li><li><p>c</p></li></ul>
    +<ul><li>a</li><li></li><li>c</li></ul>
    
    Example 318 (lines 5641-5660) Lists
    - a
    - b
    
      c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p><p>c</p></li><li><p>d</p></li></ul>
    +<ul><li>a</li><li><p>b</p><p>c</p></li><li>d</li></ul>
    
    Example 319 (lines 5663-5681) Lists
    - a
    - b
    
      [ref]: /url
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p></li><li><p>d</p></li></ul>
    +<ul><li>a</li><li><p>b</p></li><li>d</li></ul>
    
    Example 321 (lines 5712-5730) Lists
    - a
      - b
    
        c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li><p>b</p><p>c</p></li></ul></li><li>d</li></ul>
    +<ul><li>a</li><li><p>b</p><p>c</p></li><li>d</li></ul>
    
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
    @@ -1,2 +1,2 @@
    -<ul><li>a<blockquote><p>b</p></blockquote><pre><code>c
    +<ul><li><p>a</p><blockquote><p>b</p></blockquote><pre><code>c
     </code></pre></li><li>d</li></ul>
    
    Example 325 (lines 5788-5799) Lists
    - a
      - b
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li>b</li></ul></li></ul>
    +<ul><li>a</li><li>b</li></ul>
    
    Example 326 (lines 5805-5819) Lists
    1. ```
       foo
       ```
    
       bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><pre><code>foo
    +<ol><li><pre><code> foo
     </code></pre><p>bar</p></li></ol>
    
    Example 327 (lines 5824-5839) Lists
    * foo
      * bar
    
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><ul><li>bar</li></ul><p>baz</p></li></ul>
    +<ul><li>foo</li><li><p>bar</p><p>baz</p></li></ul>
    
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
    +<ul><li>a</li><li>b</li><li><p>c</p></li><li>d</li><li>e</li><li>f</li></ul>
    
    30 passed, 44 failed, 0 errored, 581 skipped
  stderr:
    Traceback (most recent call last):
      File "lists-structure.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: lists-tightness (FEATURE-BLOCK-LISTS.md)
  intent: The implementation passes empty-item, delimiter, and tight-versus-loose list conformance examples.
  return code: 1
  stdout:
    Example 256 (lines 4179-4198) List items
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
    
    Example 260 (lines 4251-4262) List items
     -    one
    
          two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li><p>one</p><p>two</p></li></ul>
    +<ul><li><p>one</p><pre><code>two
    +</code></pre></li></ul>
    
    Example 262 (lines 4300-4313) List items
    >>- one
    >>
      >  > two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><ul><li>one</li></ul><p>two</p></blockquote></blockquote>
    +<blockquote><blockquote><ul><li><p>one</p></li></ul><p>two</p></blockquote></blockquote>
    
    Example 273 (lines 4477-4489) List items
      10.  foo
    
               bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol start="10"><li><p>foo</p><pre><code>bar
    +<ol start="10"><li><p>foo</p><pre><code>     bar
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
    +<ol><li><p>indented code</p><p>paragraph</p><pre><code> more code
     </code></pre></li></ol>
    
    Example 276 (lines 4533-4549) List items
    1.      indented code
    
       paragraph
    
           more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
    -<ol><li><pre><code> indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    +<ol><li><p>indented code</p><p>paragraph</p><pre><code> more code
     </code></pre></li></ol>
    
    Example 278 (lines 4570-4579) List items
    -    foo
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><p>bar</p>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
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
    @@ -1,3 +1,3 @@
    -<ul><li>foo</li><li><pre><code>bar
    +<ul><li><p>foo</p></li><li><pre><code>bar
     </code></pre></li><li><pre><code>baz
     </code></pre></li></ul>
    
    Example 281 (lines 4640-4647) List items
    -   
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul>
    +<ul><li><p>foo</p></li></ul>
    
    Example 282 (lines 4654-4663) List items
    -
    
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul><p>foo</p>
    +<ul><li><p>foo</p></li></ul>
    
    Example 288 (lines 4745-4764) List items
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
    
    Example 289 (lines 4769-4788) List items
      1.  A paragraph
          with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,4 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +<ol><li><p>A paragraph with two lines.</p><pre><code>    indented code
    +
    +&gt; A block quote.
    +</code></pre></li></ol>
    
    Example 290 (lines 4793-4812) List items
       1.  A paragraph
           with two lines.
    
               indented code
    
           > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,4 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +<ol><li><p>A paragraph with two lines.</p><pre><code>     indented code
    +
    + &gt; A block quote.
    +</code></pre></li></ol>
    
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
    +<blockquote><ol><li>&gt; Blockquote</li></ol><p>continued here.</p></blockquote>
    
    Example 295 (lines 4901-4915) List items
    > 1. > Blockquote
    > continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li>&gt; Blockquote</li></ol><p>continued here.</p></blockquote>
    
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
    +<ol start="10"><li><p>foo - bar</p></li></ol>
    
    Example 300 (lines 5003-5013) List items
    - - foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><ul><li>foo</li></ul></li></ul>
    +<ul><li>- foo</li></ul>
    
    Example 301 (lines 5016-5030) List items
    1. - 2. foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><ul><li><ol start="2"><li>foo</li></ol></li></ul></li></ol>
    +<ol><li>- 2. foo</li></ol>
    
    Example 302 (lines 5035-5049) List items
    - # Foo
    - Bar
      ---
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><h1>Foo</h1></li><li><h2>Bar</h2>baz</li></ul>
    +<ul><li># Foo</li><li><h2>Bar</h2><p>baz</p></li></ul>
    
    Example 303 (lines 5271-5283) Lists
    - foo
    - bar
    + baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li></ul><ul><li>baz</li></ul>
    +<ul><li>foo</li><li>bar</li><li>baz</li></ul>
    
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
    
    Example 308 (lines 5406-5425) Lists
    - foo
    
    - bar
    
    
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p></li><li><p>bar</p></li><li><p>baz</p></li></ul>
    +<ul><li><p>foo</p></li><li><p>bar</p></li><li>baz</li></ul>
    
    Example 309 (lines 5427-5449) Lists
    - foo
      - bar
        - baz
    
    
          bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li>foo<ul><li>bar<ul><li><p>baz</p><p>bim</p></li></ul></li></ul></li></ul>
    +<ul><li>foo</li><li><p>bar - baz</p><pre><code>bim
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
    +<ul><li>foo</li><li><p>bar</p></li></ul><!-- --><ul><li>baz</li><li>bim</li></ul>
    
    Example 313 (lines 5530-5548) Lists
    1. a
    
      2. b
    
       3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li></ol>
    +<ol><li><p>a</p></li><li><p>b</p></li><li>c</li></ol>
    
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
    
    Example 316 (lines 5597-5614) Lists
    - a
    - b
    
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li></ul>
    +<ul><li>a</li><li><p>b</p></li><li>c</li></ul>
    
    Example 317 (lines 5619-5634) Lists
    * a
    *
    
    * c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li></li><li><p>c</p></li></ul>
    +<ul><li>a</li><li></li><li>c</li></ul>
    
    Example 318 (lines 5641-5660) Lists
    - a
    - b
    
      c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p><p>c</p></li><li><p>d</p></li></ul>
    +<ul><li>a</li><li><p>b</p><p>c</p></li><li>d</li></ul>
    
    Example 319 (lines 5663-5681) Lists
    - a
    - b
    
      [ref]: /url
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p></li><li><p>d</p></li></ul>
    +<ul><li>a</li><li><p>b</p></li><li>d</li></ul>
    
    Example 321 (lines 5712-5730) Lists
    - a
      - b
    
        c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li><p>b</p><p>c</p></li></ul></li><li>d</li></ul>
    +<ul><li>a</li><li><p>b</p><p>c</p></li><li>d</li></ul>
    
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
    @@ -1,2 +1,2 @@
    -<ul><li>a<blockquote><p>b</p></blockquote><pre><code>c
    +<ul><li><p>a</p><blockquote><p>b</p></blockquote><pre><code>c
     </code></pre></li><li>d</li></ul>
    
    Example 325 (lines 5788-5799) Lists
    - a
      - b
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li>b</li></ul></li></ul>
    +<ul><li>a</li><li>b</li></ul>
    
    Example 326 (lines 5805-5819) Lists
    1. ```
       foo
       ```
    
       bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><pre><code>foo
    +<ol><li><pre><code> foo
     </code></pre><p>bar</p></li></ol>
    
    Example 327 (lines 5824-5839) Lists
    * foo
      * bar
    
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><ul><li>bar</li></ul><p>baz</p></li></ul>
    +<ul><li>foo</li><li><p>bar</p><p>baz</p></li></ul>
    
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
    +<ul><li>a</li><li>b</li><li><p>c</p></li><li>d</li><li>e</li><li>f</li></ul>
    
    30 passed, 44 failed, 0 errored, 581 skipped
  stderr:
    Traceback (most recent call last):
      File "lists-tightness.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: lists-structure (FEATURE-BLOCK-LISTS.md)
  intent: The implementation passes list marker, nesting, indentation, and continuation conformance examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    74 passed, 0 failed, 0 errored, 581 skipped
- PASS: lists-tightness (FEATURE-BLOCK-LISTS.md)
  intent: The implementation passes empty-item, delimiter, and tight-versus-loose list conformance examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    74 passed, 0 failed, 0 errored, 581 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- parser/blocks.py
- renderer/html.py
- test_lists.py

SUMMARY:
Implemented recursive CommonMark list parsing, nesting, indentation, empty items, delimiter handling, and tight/loose rendering.

Verification: 74 list examples pass; 16 project tests pass.

BLOCKERS:
- None
