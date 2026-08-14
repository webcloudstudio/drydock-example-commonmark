# Evidence: Block 7 · Service (block-7)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57659
- execution id: 20260812.181916.284Z-375bff7f

## Stories built
- Parse escapes and character references. (inline-escapes) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-INLINE-ESCAPES.md (SP 396)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- parser/blocks.py
- renderer/html.py
- test_inline_escapes.py

## Pre-build acceptance observation
- RED: inline-escapes (FEATURE-INLINE-ESCAPES.md)
  intent: The implementation passes punctuation escape and escape-context conformance examples.
  return code: 1
  stdout:
    Example 12 (lines 489-493) Backslash escapes
    \!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~</p>
    +<p>!"#$%&amp;'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~</p>
    
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
    +<p>*not emphasized* &lt;br/&gt; not a tag [not a link](/foo) `not code` 1. not a list * not a list # not a heading [foo]: /url &quot;not a reference&quot; \ö not a character entity</p>
    
    Example 17 (lines 555-559) Backslash escapes
    `` \[\` ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>\[\`</code></p>
    +<p><code>[`</code></p>
    
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
    
    Example 24 (lines 613-620) Backslash escapes
    ``` foo\+bar
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code class="language-foo+bar">foo
    +<pre><code class="language-foo\+bar">foo
     </code></pre>
    
    7 passed, 6 failed, 0 errored, 642 skipped
  stderr:
    Traceback (most recent call last):
      File "inline-escapes.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: character-references (FEATURE-INLINE-ESCAPES.md)
  intent: The implementation passes named, decimal, hexadecimal, invalid, and contextual character-reference examples.
  return code: 1
  stdout:
    Example 28 (lines 690-700) Entity and numeric character references
    &nbsp &x; &#; &#x;
    &#87654321;
    &#abcdef0;
    &ThisIsNotDefined; &hi?;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;nbsp &amp;x; &amp;#; &amp;#x; &amp;#87654321; &amp;#abcdef0; &amp;ThisIsNotDefined; &amp;hi?;</p>
    +<p>&amp;x; &amp;#; &amp;#x; � &amp;#abcdef0; &amp;ThisIsNotDefined; &amp;hi?;</p>
    
    Example 29 (lines 707-711) Entity and numeric character references
    &copy
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;copy</p>
    +<p>©</p>
    
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
    +<p><a href="/f%C3%B6%C3%B6" title="f&amp;ouml;&amp;ouml;">foo</a></p>
    
    Example 34 (lines 751-758) Entity and numeric character references
    ``` f&ouml;&ouml;
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code class="language-föö">foo
    +<pre><code class="language-f&amp;ouml;&amp;ouml;">foo
     </code></pre>
    
    Example 35 (lines 764-768) Entity and numeric character references
    `f&ouml;&ouml;`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>f&amp;ouml;&amp;ouml;</code></p>
    +<p><code>föö</code></p>
    
    Example 37 (lines 783-789) Entity and numeric character references
    &#42;foo&#42;
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo* <em>foo</em></p>
    +<p><em>foo</em> <em>foo</em></p>
    
    10 passed, 7 failed, 0 errored, 638 skipped
  stderr:
    Traceback (most recent call last):
      File "character-references.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: inline-escapes (FEATURE-INLINE-ESCAPES.md)
  intent: The implementation passes punctuation escape and escape-context conformance examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    13 passed, 0 failed, 0 errored, 642 skipped
- PASS: character-references (FEATURE-INLINE-ESCAPES.md)
  intent: The implementation passes named, decimal, hexadecimal, invalid, and contextual character-reference examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    17 passed, 0 failed, 0 errored, 638 skipped

## Agent self-report (advisory)
The build agent declared a failure. This is advisory only; the programmatic acceptance above is the authority for this block's outcome.
- summary: Full CommonMark suite remains failing outside inline escapes.
- detail:
    Scoped escape/reference checks pass, but the complete suite fails in Tabs and Thematic breaks cases; fix block parsing before rerunning.

## Build summary
RESULT: FAILED

FILES CHANGED:
- renderer/html.py
- parser/blocks.py
- test_inline_escapes.py

SUMMARY:
Implemented punctuation escapes and named/numeric character references. Both declared scoped acceptances and focused tests pass.

BLOCKERS:
- `sh full_test.sh` fails on pre-existing tab/list/thematic-break behavior outside this story.

FAILURE_SUMMARY: Full CommonMark suite remains failing outside inline escapes.
FAILURE_DETAIL: Scoped escape/reference checks pass, but the complete suite fails in Tabs and Thematic breaks cases; fix block parsing before rerunning.
