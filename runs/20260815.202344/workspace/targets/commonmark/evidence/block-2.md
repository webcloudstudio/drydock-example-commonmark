# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 60122
- execution id: 20260815.204259.896Z-c16cfcc8

## Stories built
- Parse CommonMark leaf blocks and link reference definitions. (block-001) [story]

## Reusable compacts
- spec_compact.md
- spec_tests_compact.md
- normalize_compact.md

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Block-Leafs.md (SP 666)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark

## Pre-build acceptance observation
- RED: block-leafs-conformance (FEATURE-Block-Leafs.md)
  intent: The implementation passes every supplied conformance example owned by leaf-block parsing.
  return code: 1
  stdout:
    Example 49 (lines 942-948) Thematic breaks
    Foo
        ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p>Foo ***</p>
    +<p>Foo</p><pre><code>***
    +</code></pre>
    
    Example 55 (lines 994-1004) Thematic breaks
    _ _ _ _ a
    
    a------
    
    ---a---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_ _ _ _ a</p><p>a------</p><p>---a---</p>
    +<p><em> </em> <em> </em> a</p><p>a------</p><p>---a---</p>
    
    Example 57 (lines 1019-1031) Thematic breaks
    - foo
    ***
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr><ul><li>bar</li></ul>
    +<ul><li><p>foo ***</p></li><li>bar</li></ul>
    
    Example 58 (lines 1036-1044) Thematic breaks
    Foo
    ***
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><hr><p>bar</p>
    +<p>Foo *** bar</p>
    
    Example 60 (lines 1066-1078) Thematic breaks
    * Foo
    * * *
    * Bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr><ul><li>Bar</li></ul>
    +<ul><li>Foo</li><li><ul><li>*</li></ul></li><li>Bar</li></ul>
    
    Example 66 (lines 1167-1171) ATX headings
    # foo *bar* \*baz\*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo <em>bar</em> *baz*</h1>
    +<h1>foo <em>bar</em> <em>baz</em></h1>
    
    Example 70 (lines 1206-1212) ATX headings
    foo
        # bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p>foo # bar</p>
    +<p>foo</p><pre><code># bar
    +</code></pre>
    
    Example 79 (lines 1307-1315) ATX headings
    ## 
    #
    ### ###
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2></h2><h1></h1><h3></h3>
    +<h2></h2><h1></h1><h3>###</h3>
    
    Example 81 (lines 1361-1368) Setext headings
    Foo *bar
    baz*
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +<p>Foo *bar baz* ====</p>
    
    Example 82 (lines 1375-1382) Setext headings
      Foo *bar
    baz*	
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +<p>Foo *bar baz*<br>====</p>
    
    Example 87 (lines 1449-1455) Setext headings
    Foo
        ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p>Foo ---</p>
    +<p>Foo</p><pre><code>---
    +</code></pre>
    
    Example 88 (lines 1460-1471) Setext headings
    Foo
    = =
    
    Foo
    --- -
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo = =</p><p>Foo</p><hr>
    +<p>Foo = =</p><p>Foo --- -</p>
    
    Example 93 (lines 1527-1537) Setext headings
    > foo
    bar
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar ===</p></blockquote>
    +<blockquote><p>foo</p></blockquote><h1>bar</h1>
    
    Example 94 (lines 1540-1548) Setext headings
    - Foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr>
    +<ul><li><h2>Foo</h2></li></ul>
    
    Example 95 (lines 1555-1562) Setext headings
    Foo
    Bar
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo Bar</h2>
    +<p>Foo Bar ---</p>
    
    Example 99 (lines 1606-1614) Setext headings
    - foo
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr>
    +<ul><li><h2>foo</h2></li></ul>
    
    Example 105 (lines 1706-1716) Setext headings
    Foo
    bar
    * * *
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar</p><hr><p>baz</p>
    +<p>Foo bar <em> </em> * baz</p>
    
    Example 108 (lines 1763-1774) Indented code blocks
      - foo
    
        bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +<ul><li>foo</li></ul><pre><code>bar
    +</code></pre>
    
    Example 109 (lines 1777-1790) Indented code blocks
    1.  foo
    
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ol><li><p>foo</p><ul><li>bar</li></ul></li></ol>
    +<ol><li>foo</li></ol><pre><code>- bar
    +</code></pre>
    
    Example 113 (lines 1851-1858) Indented code blocks
    Foo
        bar
    
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p>Foo bar</p>
    +<p>Foo</p><pre><code>bar
    +</code></pre>
    
    Example 128 (lines 2091-2102) Fenced code blocks
    > ```
    > aaa
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,3 @@
     <blockquote><pre><code>aaa
    +
     </code></pre></blockquote><p>bbb</p>
    
    Example 131 (lines 2133-2142) Fenced code blocks
     ```
     aaa
    aaa
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,3 @@
    -<pre><code>aaa
    +<pre><code> aaa
     aaa
     </code></pre>
    
    Example 132 (lines 2145-2156) Fenced code blocks
      ```
    aaa
      aaa
    aaa
      ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,4 @@
     <pre><code>aaa
    -aaa
    +  aaa
     aaa
     </code></pre>
    
    Example 133 (lines 2159-2170) Fenced code blocks
       ```
       aaa
        aaa
      aaa
       ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,4 @@
    -<pre><code>aaa
    - aaa
    -aaa
    +<pre><code>   aaa
    +    aaa
    +  aaa
     </code></pre>
    
    Example 146 (lines 2337-2344) Fenced code blocks
    ~~~ aa ``` ~~~
    foo
    ~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code class="language-aa">foo
    -</code></pre>
    +<p>~~~ aa <code></code>` ~~~ foo</p><pre><code></code></pre>
    
    Example 148 (lines 2429-2444) HTML blocks
    <table><tr><td>
    <pre>
    **Hello**,
    
    _world_.
    </pre>
    </td></tr></table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,3 @@
     <table><tr><td><pre>
     **Hello**,<p><em>world</em>.
    -</pre></p></td></tr></table>
    +</pre></td></tr></table></p>
    
    Example 151 (lines 2493-2499) HTML blocks
    </div>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -</div>*foo*
    +<p></div><em>foo</em></p>
    
    Example 152 (lines 2504-2514) HTML blocks
    <DIV CLASS="foo">
    
    *Markdown*
    
    </DIV>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div class="foo"><p><em>Markdown</em></p></div>
    +<div class="foo"><p><em>Markdown</em></p><p></div></p>
    
    Example 163 (lines 2642-2650) HTML blocks
    <a href="foo">
    *bar*
    </a>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<a href="foo"> *bar* </a> 
    +<p><a href="foo"> <em>bar</em> </a></p>
    
    Example 164 (lines 2655-2663) HTML blocks
    <Warning>
    *bar*
    </Warning>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<warning> *bar* </warning> 
    +<p><warning> <em>bar</em> </warning></p>
    
    Example 165 (lines 2666-2674) HTML blocks
    <i class="foo">
    *bar*
    </i>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<i class="foo"> *bar* </i> 
    +<p><i class="foo"> <em>bar</em> </i></p>
    
    Example 166 (lines 2677-2683) HTML blocks
    </ins>
    *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -</ins> *bar* 
    +<p></ins> <em>bar</em></p>
    
    Example 167 (lines 2692-2700) HTML blocks
    <del>
    *foo*
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del> *foo* </del> 
    +<p><del> <em>foo</em> </del></p>
    
    Example 168 (lines 2707-2717) HTML blocks
    <del>
    
    *foo*
    
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del><p><em>foo</em></p></del> 
    +<p><del></p><p><em>foo</em></p><p></del></p>
    
    Example 171 (lines 2753-2769) HTML blocks
    <pre language="haskell"><code>
    import Text.HTML.TagSoup
    
    main :: IO ()
    main = print $ parseTags tags
    </code></pre>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,6 +1,4 @@
     <pre language="haskell"><code>
    -import Text.HTML.TagSoup
    -
    -main :: IO ()
    +import Text.HTML.TagSoup<p>main :: IO ()
     main = print $ parseTags tags
    -</code></pre><p>okay</p>
    +</code></pre>okay</p>
    
    Example 172 (lines 2774-2788) HTML blocks
    <script type="text/javascript">
    // JavaScript example
    
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
    </script>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<script type="text/javascript">// JavaScript example document.getElementById("demo").innerHTML = "Hello JavaScript!";</script><p>okay</p>
    +<script type="text/javascript">// JavaScript example <p>document.getElementById(&quot;demo&quot;).innerHTML = &quot;Hello JavaScript!&quot;;</script>okay</p>
    
    Example 173 (lines 2793-2809) HTML blocks
    <textarea>
    
    *foo*
    
    _bar_
    
    </textarea>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<textarea>*foo* _bar_</textarea>
    +<p><textarea></p> <p><em>foo</em></p> <p><em>bar</em></p> <p></textarea></p>
    
    Example 174 (lines 2813-2829) HTML blocks
    <style
      type="text/css">
    h1 {color:red;}
    
    p {color:blue;}
    </style>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style type="text/css">h1 {color:red;} p {color:blue;}</style><p>okay</p>
    +<style type="text/css">h1 {color:red;} <p>p {color:blue;}</style>okay</p>
    
    Example 175 (lines 2836-2846) HTML blocks
    <style
      type="text/css">
    
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style type="text/css">foo 
    +<style type="text/css"><p>foo</p> 
    
    Example 178 (lines 2878-2884) HTML blocks
    <style>p{color:red;}</style>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style>p{color:red;}</style><p><em>foo</em></p>
    +<style>p{color:red;}</style>*foo*
    
    Example 179 (lines 2887-2893) HTML blocks
    <!-- foo -->*bar*
    *baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<!-- foo -->*bar*<p><em>baz</em></p>
    +<!-- foo -->*bar* *baz* 
    
    Example 181 (lines 2912-2924) HTML blocks
    <!-- Foo
    
    bar
       baz -->
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,5 @@
     <!-- Foo
    -
    -bar
    -   baz --><p>okay</p>
    +<p>bar
    +   baz --&gt;
    +okay</p>
    +-->
    
    Example 182 (lines 2930-2944) HTML blocks
    <?php
    
      echo '>';
    
    ?>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
     <?php
    -
    -  echo '>'; ?><p>okay</p>
    +<p> echo '&gt;';</p><p>?&gt; okay</p>
    
    Example 184 (lines 2958-2986) HTML blocks
    <![CDATA[
    function matchwo(a,b)
    {
      if (a < b && a < 0) then {
        return 1;
    
      } else {
    
        return 0;
      }
    }
    ]]>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -3,10 +3,5 @@
     {
       if (a < b && a < 0) then {
         return 1;
    -
    -  } else {
    -
    -    return 0;
    -  }
    -}
    -]]><p>okay</p>
    +<p> } else {</p><pre><code>return 0;
    +</code></pre><p>} } ]]&gt; okay</p>
    
    Example 187 (lines 3017-3027) HTML blocks
    Foo
    <div>
    bar
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><div>bar</div>
    +<p>Foo<div>bar</div></p>
    
    Example 190 (lines 3090-3100) HTML blocks
    <div>
    
    *Emphasized* text.
    
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div><p><em>Emphasized</em> text.</p></div>
    +<div><p><em>Emphasized</em> text.</p><p></div></p>
    
    Example 192 (lines 3125-3145) HTML blocks
    <table>
    
    <tr>
    
    <td>
    Hi
    </td>
    
    </tr>
    
    </table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<table><tr><td>Hi</td></tr></table>
    +<table><p><tr></p><p><td>Hi</td></p><p></tr></p><p></table></p>
    
    Example 193 (lines 3152-3173) HTML blocks
    <table>
    
      <tr>
    
        <td>
          Hi
        </td>
    
      </tr>
    
    </table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,4 @@
    -<table><tr><pre><code>&lt;td&gt;
    +<table><p><tr></p><pre><code>&lt;td&gt;
       Hi
     &lt;/td&gt;
    -</code></pre></tr></table>
    +</code></pre><p></tr></p><p></table></p>
    
    Example 195 (lines 3210-3218) Link reference definitions
       [foo]: 
          /url  
               'the title'  
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,3 @@
    -<p><a href="/url" title="the title">foo</a></p>
    +<p>[foo]:</p><pre><code>  /url  
    +       'the title'  
    +</code></pre><p>[foo]</p>
    
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
    +<p><a href="&lt;&gt;">foo</a></p>
    
    Example 203 (lines 3312-3319) Link reference definitions
    [foo]: <bar>(baz)
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: <bar>(baz)</p><p>[foo]</p>
    +<p><a href="&lt;bar&gt;(baz)">foo</a></p>
    
    Example 204 (lines 3325-3331) Link reference definitions
    [foo]: /url\bar\*baz "foo\"bar\baz"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%5Cbar*baz" title="foo&quot;bar\baz">foo</a></p>
    +<p>[foo]: /url\bar*baz &quot;foo&quot;bar\baz&quot;</p><p>[foo]</p>
    
    Example 206 (lines 3348-3355) Link reference definitions
    [foo]
    
    [foo]: first
    [foo]: second
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="first">foo</a></p>
    +<p><a href="second">foo</a></p>
    
    Example 208 (lines 3370-3376) Link reference definitions
    [ΑΓΩ]: /φου
    
    [αγω]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/%CF%86%CE%BF%CF%85">αγω</a></p>
    +<p><a href="/φου">αγω</a></p>
    
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
    
    Example 213 (lines 3426-3434) Link reference definitions
        [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code>[foo]: /url &quot;title&quot;
    +<pre><code>[foo]: /url "title"
     </code></pre><p>[foo]</p>
    
    Example 214 (lines 3440-3450) Link reference definitions
    ```
    [foo]: /url
    ```
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>[foo]: /url
    -</code></pre><p>[foo]</p>
    +<pre><code></code></pre><p><a href="/url">foo</a></p>
    
    Example 215 (lines 3455-3464) Link reference definitions
    Foo
    [bar]: /baz
    
    [bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo [bar]: /baz</p><p>[bar]</p>
    +<p>Foo</p><p><a href="/baz">bar</a></p>
    
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
    +<p>&quot;bar&quot;</p><p><a href="/foo-url" title="foo">foo</a>, <a href="/bar-url">bar</a>, <a href="/baz-url">baz</a></p>
    
    Example 220 (lines 3525-3533) Link reference definitions
    [foo]
    
    > [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p><blockquote></blockquote>
    +<p>[foo]</p><blockquote><p>[foo]: /url</p></blockquote>
    
    Example 225 (lines 3600-3608) Paragraphs
    aaa
                 bbb
                                           ccc
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,3 @@
    -<p>aaa bbb ccc</p>
    +<p>aaa</p><pre><code>         bbb
    +                                   ccc
    +</code></pre>
    
    122 passed, 65 failed, 0 errored, 468 skipped
  stderr:
    Traceback (most recent call last):
      File "block-leafs-conformance.py", line 24, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): block-leafs-interface (FEATURE-Block-Leafs.md)
  intent: Leaf parsing remains reachable through the required executable interface.
  return code: 0
  stdout:
    <h1>heading</h1>
    <pre><code>code
    </code></pre>
- GREEN (prepassed): block-leafs-reference-input (FEATURE-Block-Leafs.md)
  intent: Link-reference-definition input is accepted through the executable interface.
  return code: 0
  stdout:
    <p><a href="/destination">label</a></p>

## Post-build programmatic acceptance
- PASS: block-leafs-conformance (FEATURE-Block-Leafs.md)
  intent: The implementation passes every supplied conformance example owned by leaf-block parsing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    187 passed, 0 failed, 0 errored, 468 skipped
- PASS: block-leafs-interface (FEATURE-Block-Leafs.md)
  intent: Leaf parsing remains reachable through the required executable interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <h1>heading</h1>
    <pre><code>code
    </code></pre>
- PASS: block-leafs-reference-input (FEATURE-Block-Leafs.md)
  intent: Link-reference-definition input is accepted through the executable interface.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="/destination">label</a></p>

## Repair attempts
- attempt 0 (initial build): failed; 2/3 checks; 163/187 cases model=gpt-5.6-luna; execution 20260815.203501.159Z-3db12411
- attempt 1 (repair 1): built; 3/3 checks; 187/187 cases model=gpt-5.6-luna; execution 20260815.204259.896Z-c16cfcc8

## Build summary
<reusable-compact filename="spec.txt">
CommonMark 0.31.2 specification: block structure precedes inline parsing. Leaf blocks include thematic breaks, headings, indented/fenced code, HTML blocks, reference definitions, paragraphs, and blank lines. Reference labels normalize via Unicode case-folding and whitespace collapsing; first definition wins.
</reusable-compact>

<reusable-compact filename="spec_tests.py">
Runs supplied CommonMark examples against `--program`, optionally filtered by section pattern. Verdict is the process exit status: failures plus errors; output is diagnostic only.
</reusable-compact>

<reusable-compact filename="normalize.py">
Normalizes HTML for conformance comparison: collapses insignificant whitespace, normalizes attributes and entities, preserves preformatted content, and canonicalizes URLs.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- commonmark

SUMMARY:
Implemented and repaired leaf-block parsing and link-reference collection. Scoped conformance: 187 passed, 0 failed, 0 errored. Direct executable interface verification passed.

BLOCKERS:
- None
