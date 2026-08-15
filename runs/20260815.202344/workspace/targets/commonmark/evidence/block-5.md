# Evidence: Block 5 · Service (block-5)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 60153
- execution id: 20260815.212047.230Z-4bb9dec8

## Stories built
- Parse escapes, entities, code spans, line breaks, and literal text. (inline-001) [story]

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Inline-Basics.md (SP 694)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- README.md
- commonmark

## Pre-build acceptance observation
- RED: inline-basics-conformance (FEATURE-Inline-Basics.md)
  intent: The implementation passes every supplied conformance example owned by foundational inline parsing.
  return code: 1
  stdout:
    Example 14 (lines 509-529) Backslash escapes
    \*not emphasized*
    \<br/> not a tag
    \[not a link](/foo)
    \`not code`
    1\. not a list
    \* not a list
    \# not a heading
    \[foo]: /url "not a reference"
    \&ouml; not a character entity
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*not emphasized* &lt;br/&gt; not a tag [not a link](/foo) `not code` 1. not a list * not a list # not a heading [foo]: /url &quot;not a reference&quot; &amp;ouml; not a character entity</p>
    +<p>*not emphasized* \<br> not a tag [not a link](/foo) \<code>not code</code> 1. not a list * not a list # not a heading [foo]: /url &quot;not a reference&quot; &amp;ouml; not a character entity</p>
    
    Example 20 (lines 580-584) Backslash escapes
    <https://example.com?find=\*>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://example.com?find=%5C*">https://example.com?find=\*</a></p>
    +<https: example.com?find="\*"> 
    
    Example 22 (lines 597-601) Backslash escapes
    [foo](/bar\* "ti\*tle")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/bar*" title="ti*tle">foo</a></p>
    +<p>[foo](/bar* &quot;ti*tle&quot;)</p>
    
    Example 28 (lines 690-700) Entity and numeric character references
    &nbsp &x; &#; &#x;
    &#87654321;
    &#abcdef0;
    &ThisIsNotDefined; &hi?;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;nbsp &amp;x; &amp;#; &amp;#x; &amp;#87654321; &amp;#abcdef0; &amp;ThisIsNotDefined; &amp;hi?;</p>
    +<p>&amp;x; &amp;#; &amp;#x; � &amp;#abcdef0; &ThisIsNotDefined; &amp;hi?;</p>
    
    Example 29 (lines 707-711) Entity and numeric character references
    &copy
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;copy</p>
    +<p>©</p>
    
    Example 30 (lines 717-721) Entity and numeric character references
    &MadeUpEntity;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;MadeUpEntity;</p>
    +<p>&MadeUpEntity;</p>
    
    Example 32 (lines 735-739) Entity and numeric character references
    [foo](/f&ouml;&ouml; "f&ouml;&ouml;")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/f%C3%B6%C3%B6" title="föö">foo</a></p>
    +<p>[foo](/föö &quot;föö&quot;)</p>
    
    Example 33 (lines 742-748) Entity and numeric character references
    [foo]
    
    [foo]: /f&ouml;&ouml; "f&ouml;&ouml;"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/f%C3%B6%C3%B6" title="föö">foo</a></p>
    +<p><a href="/f&amp;ouml;&amp;ouml;" title="f&amp;ouml;&amp;ouml;">foo</a></p>
    
    Example 37 (lines 783-789) Entity and numeric character references
    &#42;foo&#42;
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo* <em>foo</em></p>
    +<p><em>foo</em> <em>foo</em></p>
    
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
    
    Example 342 (lines 6029-6033) Code spans
    ` foo `` bar `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo `` bar</code></p>
    +<p><code>foo</code><code>bar</code></p>
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +<p><code>&lt;a href="</code>&quot;&gt;`</p>
    
    Example 346 (lines 6069-6073) Code spans
    <a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="`">`</p>
    +<p>&lt;a href=&quot;<code>"&gt;</code></p>
    
    Example 348 (lines 6087-6091) Code spans
    <https://foo.bar.`baz>`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://foo.bar.%60baz">https://foo.bar.`baz</a>`</p>
    +<p>&lt;https://foo.bar.<code>baz&gt;</code></p>
    
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
    
    Example 644 (lines 9334-9339) Hard line breaks
    `code\
    span`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>code\ span</code></p>
    +<p><code>code&lt;br /&gt; span</code></p>
    
    Example 646 (lines 9353-9359) Hard line breaks
    <a href="foo\
    bar">
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p><a href="foo\
    -bar"></p>
    +<p>
    
    51 passed, 21 failed, 0 errored, 583 skipped
  stderr:
    Traceback (most recent call last):
      File "inline-basics-conformance.py", line 24, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): inline-basics-interface (FEATURE-Inline-Basics.md)
  intent: Inline source containing escapes, entities, code, and line breaks is accepted through the executable interface.
  return code: 0
  stdout:
    <p>escaped * text &amp; <code>code</code><br />
    next</p>
- GREEN (prepassed): inline-basics-unicode-input (FEATURE-Inline-Basics.md)
  intent: UTF-8 inline text is accepted through the executable interface.
  return code: 0
  stdout:
    <p>Unicode café</p>

## Post-build programmatic acceptance
- PASS: inline-basics-conformance (FEATURE-Inline-Basics.md)
  intent: The implementation passes every supplied conformance example owned by foundational inline parsing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    72 passed, 0 failed, 0 errored, 583 skipped
- PASS: inline-basics-interface (FEATURE-Inline-Basics.md)
  intent: Inline source containing escapes, entities, code, and line breaks is accepted through the executable interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <p>escaped * text &amp; <code>code</code><br />
    next</p>
- PASS: inline-basics-unicode-input (FEATURE-Inline-Basics.md)
  intent: UTF-8 inline text is accepted through the executable interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <p>Unicode café</p>

## Repair attempts
- attempt 0 (initial build): failed; 2/3 checks; 67/72 cases model=gpt-5.6-luna; execution 20260815.211228.205Z-3700ff81
- attempt 1 (repair 1): built; 3/3 checks; 72/72 cases model=gpt-5.6-luna; execution 20260815.212047.230Z-4bb9dec8

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark
- README.md

SUMMARY:
Fixed inline link titles, entity handling, quote escaping, and code-span precedence. Scoped conformance passes: 72/72. Interface and Unicode checks pass.

BLOCKERS:
- None
